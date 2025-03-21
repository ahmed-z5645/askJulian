import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import Background from './background'
import axois from "axios"

function App() {
  const [count, setCount] = useState(0)
  const [isSong, setIsSong] = useState(false) //true ? search song : search albums

  const handleSubmit = (e) => {
    e.preventDefault()
    console.log('submit')
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
          <p>I'm glad you made it. I'm Julian, an artificial intelligence model designed to have a better in music taste than you. 
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
              required></input>
            <label className="formLabel">Artist</label>
            <input
              type="text"
              placeholder="Example: Clairo" 
              className="formInput"
              name="album"
              required></input>
            <button type="submit">Roast Me</button>
          </form>
        </div>}
        </div>
      </div>
    </div>
  )
}

export default App
