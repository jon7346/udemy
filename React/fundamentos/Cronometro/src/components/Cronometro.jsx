import "../App.css"

const Cronometro = () => {
   const tempo = 0.00

    return (
     <>
     <div>
      <h2>Timer: </h2>
      <div>
        <p class = 'Timer'>{tempo} </p>
        <buttun>Iniciar</buttun><br/>  
        <buttun>Pausar</buttun><br/>
        <buttun>Resetar</buttun><br/>  

    
      </div>
     </div>
     </>
    )
} ;

export default Cronometro;