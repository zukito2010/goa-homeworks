import React from 'react'
import './App.css'

function App() {
  const names = ['Zuka', 'Luka', 'Lika', 'Tako', 'Genadi']

  return (
    <ul>
      {names.map((name, index) => (
        <li key={index}>{name}</li>
      ))}
    </ul>
  )
}