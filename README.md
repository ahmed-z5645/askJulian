<h3 align="center">askJulian</h3>

  <p align="center">
    An AI-powered music enthusiast that predicts album ratings and provides witty commentary.
    <br />
     <a href="https://askjulian.xyz">askjulian.xyz</a>
  </p>
</div>

<!-- REMOVE THIS IF YOU DON'T HAVE A DEMO -->
<!-- TIP: You can alternatively directly upload a video up to 100MB by dropping it in while editing the README on GitHub. This displays a video player directly on GitHub instead of making it so that you have to click an image/link -->

https://github.com/user-attachments/assets/beb96580-8b5e-4922-b8b1-86f019de82d8

## Table of Contents

<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#key-features">Key Features</a></li>
      </ul>
    </li>
    <li><a href="#architecture">Architecture</a></li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>

## About The Project

askJulian is a full-stack web application that uses a machine learning model to predict album ratings. Users can input an artist and album, and the application will return a predicted rating along with an album image, release year, and a humorous comment based on the rating. The backend is built with FastAPI and uses a TensorFlow model trained on a dataset of album ratings and tags. The frontend is built with React and Vite, providing a user-friendly interface for interacting with the model.

### Key Features

- **Album Rating Prediction:** Predicts a rating for a given album based on artist, album name, year, and tags.
- **Last.fm Integration:** Fetches album information (image, tags) from the Last.fm API.
- **Humorous Commentary:** Provides a witty comment based on the predicted rating.
- **User-Friendly Interface:** Simple and intuitive React frontend.

## Architecture

The project follows a client-server architecture:

- **Frontend:** React application built with Vite. Handles user input, displays results, and communicates with the backend API.
- **Backend:** FastAPI application. Exposes an API endpoint for retrieving album ratings. Loads and uses a TensorFlow model for prediction. Interacts with the Last.fm API to fetch album information.
- **Model:** A TensorFlow Keras model trained on a dataset of album ratings and tags.

Technologies used:

- **Frontend:** React, Vite, Axios, CSS
- **Backend:** FastAPI, TensorFlow, scikit-learn, Last.fm API, Discogs API, Python
- **Data:** CSV file containing album ratings and tags

## Getting Started

To run the project locally, follow these steps:

### Prerequisites

- Python 3.7+
- Node.js 18+
- npm

### Installation

1.  Clone the repository:

    ```sh
    git clone https://github.com/ahmed-z5645/askjulian.git
    ```

2.  Navigate to the backend directory:

    ```sh
    cd askjulian/back-end
    ```

3.  Create a `.env` file in the `back-end` directory and add your Last.fm API key and Discogs API Key:

    ```
    LASTFM_API_KEY=your_lastfm_api_key
    DISCOGS_API_KEY=your_discogs_api_key
    ```

4.  Install the backend dependencies:

    ```sh
    pip install -r requirements.txt
    ```

5. Run the backend:

    ```sh
    python main.py
    ```

6.  Navigate to the frontend directory:

    ```sh
    cd ../front-end
    ```

7.  Install the frontend dependencies:

    ```sh
    npm install
    ```

8.  Create a `.env` file in the `front-end` directory and add your backend API URL:

    ```
    VITE_BACKEND_API_URL=http://localhost:8000
