import { useState } from "react";
import "./ChatInput.css";

function ChatInput({ onSend }) {

    const [message, setMessage] = useState("");

    const handleSend = () => {

        if (!message.trim()) return;

        onSend(message);

        setMessage("");

    };

    return (

        <div className="chat-input-container">

            <input
                className="chat-input"
                value={message}
                placeholder="Ask me anything..."
                onChange={(e) => setMessage(e.target.value)}
                onKeyDown={(e) => {
                    if (e.key === "Enter") {
                        handleSend();
                    }
                }}
            />

            <button
                className="send-btn"
                onClick={handleSend}
            >
                ➤
            </button>

        </div>

    );

}

export default ChatInput;