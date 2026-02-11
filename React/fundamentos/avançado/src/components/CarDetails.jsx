import { useState } from "react"; 

const CarDetails = ({marca, cor, km}) => {
  
  return (
    <div>
    <h2>
     Detalhes do Carro 
    </h2>
     <ul>
        <li>marca : {marca}</li>
        <li>KM : {cor}</li>
        <li>Cor : {km}</li>
        
     </ul>
    </div>

  ) 
}

export default CarDetails; 