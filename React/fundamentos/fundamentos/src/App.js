import FirstComponent from "./component/FirstComponent"
import TemplateExpressions from "./component/TemplateExpressions"
import MyComponent from "./component/MyComponent"
import Events from "./component/Events"
import Challenge from "./component/Challenge"

import './App.css';

function App() {
  return (
    <div className="App">
      <h1>Primeiro projeto</h1>
      <FirstComponent/>
      <TemplateExpressions/>
      <MyComponent/>
      <Events/>
      <Challenge/>
      
    </div>
  );
}

export default App;
