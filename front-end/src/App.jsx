import { useState } from 'react'
import ratingResponses  from './responses.js'
import './App.css'
import Background from './background'
import axios from "axios"

function App() {
  const [count, setCount] = useState(0)
  const [isSong, setIsSong] = useState(false) //true ? search song : search albums

  const [formData, setFormData] = useState({
    artist: "",
    album: ""
  })
  const[response, setResponse] = useState(null)

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value })
  }

  const ENDPOINT = import.meta.env.VITE_BACKEND_API_URL
  const handleSubmit = async (e) => {
    e.preventDefault()
    console.log(formData)
    setResponse(false);
    try {
      const res =  await axios.get(`${ENDPOINT}/albums/getRating`, {
        params: formData,
        headers: { "Content-Type": "application/json"}})

      console.log(res.data)
      setResponse(res.data)
    } catch (error) {
      setResponse({error: error.message})
    }
  }

  return (
    <div className="app">
      <div className="background">
        <Background />
      </div>
      <div className="content">
        <div className="title">
          <h1>julian</h1>
          <h3>Your Programmed Music <br />Enthusiast</h3>
          <p>I'm glad you made it. I'm Julian, an artificial intelligence model designed to have a better taste in music than you. 
            <br />Give me an album or song, and I'll let you know what I think about it</p>
        </div>
        <div className="func">
          <div className="song-album">
            <button onClick={() => setIsSong(true)}
              style = {{backgroundColor: isSong ? "#3b3b3b" : "#1a1a1a", 
                        borderTopRightRadius: "0px", borderBottomRightRadius: "0px", width: "20%"
              }}
              >Song</button>
            <button onClick={() => setIsSong(false)}
              style = {{backgroundColor: isSong ? "#1a1a1a" : "#3b3b3b", width: "20%",
                        borderTopLeftRadius: "0px", borderBottomLeftRadius: "0px"
              }}
              >Album</button>
          </div>
          {(isSong) ? 
          <div>
            <h3 style ={{fontWeight: "400"}}>Yeah, right. Go listen to an <span style={{fontFamily: "Borel", color: "#e59500"}}>album</span>, the way the music was <span style={{fontFamily: "Borel", color: "#e59500"}}>supposed to be experienced. </span></h3>
            <p>I'm just kidding, coming soon :)</p>
          </div>
          :
          <>
          <div className="Form">
            <p>Are You Valid?</p>
            <form onSubmit={handleSubmit}
              style={{display: "flex", flexDirection: "column", width: "80%", margin: "auto"}}>
              <label className="formLabel">Album</label>
              <input
                type="text"
                placeholder="Example: Sling" 
                className="formInput"
                name="album"
                value={formData.album}
                onChange={handleChange}
                required></input>
              <label className="formLabel">Artist</label>
              <input
                type="text"
                placeholder="Example: Clairo" 
                className="formInput"
                name="artist"
                value={formData.artist}
                onChange={handleChange}
                required></input>
              <button type="submit">Roast Me</button>
            </form>
          </div>
          <div className="response">
          {(response) ? (
            response.error ? (
              <p>something went wrong :(</p>
              ) : (
              <>
                <img style = {{ borderRadius: "1vw",
                                width: "9vw"
                }}src={response["image"]}/>
                <p style={{marginTop: "0", marginBottom: "0", fontSize: "1vw", fontWeight: "500"}}>
                  <span>{response["album"]
                    .toLowerCase()
                    .replace(/\b\w/g, (char) => char.toUpperCase())}{" "}
                    -{" "}
                  </span>
                  <span style={{fontFamily: "Borel", color: "#e59500", fontSize: "1vw", lineHeight:"0"}}>{response["artist"]
                    .toLowerCase()
                    .replace(/\b\w/g, (char) => char.toUpperCase())}
                  </span>
                </p>
                <p style={{marginTop:"0"}}>{response["year"]}</p>
                <p style={{color: "#e59500", 
                          fontSize: "2.5vw", 
                          fontWeight:"1000",
                          margin:"0",
                          marginTop:"5%",
                          lineHeight:"0"}}><span style={{fontFamily: "Borel"}}>{((response["artist"] == "clairo") && (response["album"] == "sling")) ? 11: response["predicted_rating"]}</span> / 10</p>
                <p>{((response["artist"] == "clairo") && (response["album"] == "sling")) ? 
                    <>This is what real music is, nothing else will ever compare</> : 
                    ratingResponses[Math.floor(parseFloat(response["predicted_rating"])) + 1][Math.floor(parseFloat(response["predicted_rating"]) * 10) % 3]}</p>
                </> )): (response == null) ? null : <><p>LOADING</p></>}
            </div>
            </>}
        </div>
      </div>
    </div>
  )
}

export default App
