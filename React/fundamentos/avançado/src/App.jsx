import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import ListRender from './components/ListRender.jsx'
import ConditionalList from './components/ConditionalList.jsx'
import ShowUserName from './components/ShowUserName.jsx'
import CarDetails from './components/CarDetails.jsx'
function App() {
 

  return (
    <div>
      <h1>LISTA</h1>
      <ListRender />
      <ConditionalList/>
      <ShowUserName name = 'matheus' />
      <CarDetails color = 'azul' marca ='nen' km = {100000} />
    </div>
  )
}

export default App
