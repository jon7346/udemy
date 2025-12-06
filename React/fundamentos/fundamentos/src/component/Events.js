const Events = () => {
    const handleMyEvent = (e) => { 
        console.log(e);
        console.log ("Ativou meu envento");
    }; 
    const renderSomething = (x) => 
    {
        if(x) {
          return  <div>posso renderizar isso </div>

        }
        else {
         return<div>ou isso </div>
        }
    }
    return (
        <div>
            <div>
                <button onClick = {handleMyEvent}>Clique aqui</button>
            </div>
            <div>
                <btton onClick = {()=> console.log("Clicou")}>
                    Clique aqui também!
                </btton>
            </div>
            {renderSomething(true)}
            {renderSomething(false)}
        </div>
    )
}
export default Events 