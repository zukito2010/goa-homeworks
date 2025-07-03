import { useState } from 'react'

function App() {
  const [count, setCount] = useState([])

  const handleClick = () => {
    const inpValue = document.getElementById('inp').value
    if (inpValue){
      setCount(prev => [...prev, <li >{inpValue}</li>])
    }else{
      alert('no empty strings')
    }
    }

  return (
    <>
      <input type="text" id='inp' />
      <button type='submit' onClick={handleClick}>add to list</button>
      <ol>{count}</ol>
    </>
  )
}

export default App
