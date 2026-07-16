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

        <div className="chat-input">

            <input
                value={message}
                placeholder="Ask me anything..."
                onChange={(e) => setMessage(e.target.value)}
                onKeyDown={(e) => {
                    if (e.key === "Enter") {
                        handleSend();
                    }
                }}
            />

            <button onClick={handleSend}>
                Send
            </button>

        </div>

    );

}

export default ChatInput;