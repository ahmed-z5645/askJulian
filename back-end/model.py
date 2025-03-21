import pandas as pd
import numpy as np
import tensorflow as tf
import pickle
from tensorflow.keras import layers, models
from sklearn.preprocessing import LabelEncoder
from tensorflow.keras.preprocessing.sequence import pad_sequences
from utils import pad_tags
import os

# Load the dataset
script_dir = os.path.dirname(os.path.abspath(__file__))
needed_path = os.path.join(script_dir, "fantano_ratings_with_tags.csv")
df = pd.read_csv(needed_path)

# Encode album and artist names as int using LabelEncoder from sklearn
album_encoder, artist_encoder = LabelEncoder(), LabelEncoder()


df['encoded_album_name'] = album_encoder.fit_transform(df['project_name'])
df['encoded_artist'] = artist_encoder.fit_transform(df['artist'])

# Process the tags using pad_tags function
df['tags'] = df['tags'].apply(pad_tags)

# Convert tags into one-hot encoding
from sklearn.preprocessing import MultiLabelBinarizer

mlb = MultiLabelBinarizer()
tags_matrix = mlb.fit_transform(df['tags'])
tags_df = pd.DataFrame(tags_matrix, columns=mlb.classes_)

# Combine the new tags matrix back w original dataframe
df = pd.concat([df, tags_df], axis=1)

# Prep the input features (X) and target labels (y)
X = df[['encoded_album_name', 'encoded_artist', 'year'] + list(tags_df.columns)]
y = df['rating']

# Build model
input_album_name = layers.Input(shape=(1,), dtype=tf.int32, name="album_name")
input_artist = layers.Input(shape=(1,), dtype=tf.int32, name="artist")
input_year = layers.Input(shape=(1,), dtype=tf.float32, name="year")
input_tags = layers.Input(shape=(tags_df.shape[1],), dtype=tf.float32, name="tags")

# Embed layers for album and artist
album_embedding = layers.Embedding(input_dim=len(album_encoder.classes_), output_dim=8)(input_album_name)
artist_embedding = layers.Embedding(input_dim=len(artist_encoder.classes_), output_dim=8)(input_artist)

# Flatten embeddings
album_embedding = layers.Flatten()(album_embedding)
artist_embedding = layers.Flatten()(artist_embedding)

# Combine all
x = layers.concatenate([album_embedding, artist_embedding, input_year, input_tags])

# Add Dense layers
x = layers.Dense(64, activation='relu')(x)
x = layers.Dense(32, activation='relu')(x)

# Output layer
output = layers.Dense(1, activation='linear')(x)  # Linear output for rating prediction

# Build and compile model
model = models.Model(inputs=[input_album_name, input_artist, input_year, input_tags], outputs=output)
model.compile(optimizer='adam', loss='mean_squared_error')

# Model summary
model.summary()

# Prep training data
X_train_album_name = np.array(df['encoded_album_name'])
X_train_artist = np.array(df['encoded_artist'])
X_train_year = np.array(df['year'])
X_train_tags = np.array(df[list(tags_df.columns)])

# Train model
model.fit([X_train_album_name, X_train_artist, X_train_year, X_train_tags], y, epochs=10, batch_size=32)

def predict_rating(album_name, artist_name, release_year, tags):
    # Encode input data
    album_input = album_encoder.transform([album_name])
    artist_input = artist_encoder.transform([artist_name])
    tag_input = pad_tags(tags)
    tag_input = mlb.transform([tag_input])
    return model.predict([album_input, artist_input, np.array([release_year]), tag_input])

# Example prediction
predicted_rating = predict_rating('ok computer', 'radiohead', 1997, "alternative, alternative rock, rock, radiohead, indie")
print(predicted_rating)

model.save('julian.h5')
label_encoders = {
    'album': album_encoder,
    'artist': artist_encoder,
    'tags': mlb
}
with open('label_encoders.pkl', 'wb') as f:
    pickle.dump(label_encoders, f)

print("Model successfully built, trained, and saved :)")