import { useState, useRef, useEffect } from "react";
import API from "../services/api";
import "./ChatWindow.css";
import Message from "./Message";
import ChatInput from "./ChatInput";

function ChatWindow() {

    const [messages, setMessages] = useState([
        {
            sender: "bot",
            text: "👋 Welcome to StadiumPilot AI! How can I help you today?"
        }
    ]);

    // One unique session for this browser tab
    const [sessionId] = useState(crypto.randomUUID());
    const messagesEndRef = useRef(null);

    useEffect(() => {
        messagesEndRef.current?.scrollIntoView({
            behavior: "smooth"
        });
    }, [messages]);
    const [isTyping, setIsTyping] = useState(false);
    const handleSend = async (text) => {

        // Add user message
        setMessages(prev => [
            ...prev,
            {
                sender: "user",
                text
            }
        ]);
        setIsTyping(true);
        try {

            const response = await API.post("/chat", {
                session_id: sessionId,
                message: text
            });

            setMessages(prev => [
                ...prev,
                {
                    sender: "bot",
                    text: response.data.reply
                }
            ]);
            setIsTyping(false);
        } catch (error) {

            console.error(error);

            setMessages(prev => [
                ...prev,
                {
                    sender: "bot",
                    text: "Something went wrong."
                }
            ]);
            setIsTyping(false);
        }

    };

    return (

        <div className="chat-container">

            <div className="messages">

                {messages.map((msg, index) => (

                    <Message
                        key={index}
                        sender={msg.sender}
                        text={msg.text}
                    />

                ))}

                {isTyping && (

                    <Message
                        sender="bot"
                        text="StadiumPilot AI is typing..."
                    />

                )}

                <div ref={messagesEndRef}></div>

            </div>

            <ChatInput onSend={handleSend} />

        </div>

    );

}

export default ChatWindow;