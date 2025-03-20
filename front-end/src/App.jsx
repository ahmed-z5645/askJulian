import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'

function App() {
  const [count, setCount] = useState(0)
  const [isSong, setIsSong] = useState(true) //treu ? search song : search albums

  const handleSubmit = (e) => {
    e.preventDefault()
    console.log('submit')
  }
  return (
    <>
      <h1>Hey, I'm Julian</h1>
      <p>Welcome to askjulian.xyz ! I'm glad you could make it. 
        <br />
        Select "Song" or "Album" below, and then I'll let you know what I think of it, and some songs that are similar (and probably better) 
      </p>
      <div className="song-album">
        <button onClick={() => setIsSong(true)}
          style = {{backgroundColor: isSong ? "#3b3b3b" : "#1a1a1a", 
                    borderTopRightRadius: "0px", borderBottomRightRadius: "0px"
          }}
          >song</button>
        <button onClick={() => setIsSong(false)}
          style = {{backgroundColor: isSong ? "#1a1a1a" : "#3b3b3b",
                    borderTopLeftRadius: "0px", borderBottomLeftRadius: "0px"
          }}
          >album</button>
      </div>
      <div className="Form">
        <h3>Am I valid?</h3>
        <form onSubmit={handleSubmit}
          style={{display: "flex", flexDirection: "column",}}>
          <input
            type="text"
            placeholder={isSong ? "Song" : "Album"}></input>
          <input
            type="text"
            placeholder="Artist"></input>
          <button type="submit">Roast Me</button>
        </form>
      </div>
    </>
  )
}

export default App
