import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import ListRender from './components/ListRender.jsx'
import ConditionalList from './components/ConditionalList.jsx'
import ShowUserName from './components/ShowUserName.jsx'
function App() {
  
  return (
    <div>
      <h1>LISTA</h1>
      <ListRender />
      <ConditionalList/>
      <ShowUserName name = 'matheus' />
    </div>
  )
}

export default App
