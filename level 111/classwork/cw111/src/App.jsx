import { useState } from 'react'

function App() {
  const [count, setCount] = useState(0)

  const handleClick = () => {
    setCount(count+1);
  }

  return (
    <>
      <h1>clicks: {count}</h1>
      <button onClick={handleClick}>click me</button>
    </>
  )
}

export default App
