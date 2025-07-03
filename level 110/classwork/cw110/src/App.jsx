import { useState } from 'react'
import Parent from './components/parent'



function App() {
  
  const handleHover = () => {
    console.log('hovering')
  };

  return (
    <>
      <Parent onMouseEnter={handleHover}>
        <h1>gela</h1>
      </Parent>
    </>
  )
}

export default App
