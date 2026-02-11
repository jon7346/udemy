import { useState } from "react" ;

const ConditionalList = () => {
    //criando um componente apenas para validar 
    const [x] = useState(true); 

    //criando a variavel e uma função que permite mudar seu valor
    //(assim como em uma classe)
    const [name, setName] = useState("oão")

    return (
     <div> 
        <h1> isso será exibido? </h1>
        
        { x && <p>se x for true, sim!</p> }
        {!x && <p>agora x é falso</p>}
        { name == "João" ? 
        (
            <div>nome é {name}</div>
        ): 
        (<div>
            <p>o nome não foi encontrado</p>
        </div>) }
        <button onClick={() => setName("João")  }>clica aqui </button>
     </div>);  
}; 

export default ConditionalList; 