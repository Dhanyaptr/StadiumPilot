import ChatWindow from "./components/ChatWindow";
import "./index.css";

function App() {
  return (
    <div className="app">

      <div className="header">
        <h1>🏟 StadiumPilot AI</h1>
        <p>FIFA World Cup 2026 Navigation Assistant</p>
      </div>

      <ChatWindow />

    </div>
  );
}

export default App;