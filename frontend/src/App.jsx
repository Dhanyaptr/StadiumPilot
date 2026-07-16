import ChatWindow from "./components/ChatWindow";
import "./index.css";

function App() {
  return (
    <div className="app">

      <div className="header">

    <div className="header-content">

        <h1>🏟 StadiumPilot AI</h1>

        <p>Your Smart FIFA World Cup 2026 Stadium Assistant</p>

        <div className="header-features">

            <span>🧭 Navigation</span>
            <span>🍔 Food</span>
            <span>🚻 Restrooms</span>
            <span>🏥 Medical</span>
            <span>🛍 Merchandise</span>
            <span>📖 Rules</span>
            <span>♿ Accessibility</span>

        </div>

    </div>

</div>

      <ChatWindow />

    </div>
  );
}

export default App;