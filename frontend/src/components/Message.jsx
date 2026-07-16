import "./Message.css";

function Message({ sender, text }) {

    return (

        <div
            className={`message-row ${sender === "user" ? "user-row" : "bot-row"}`}
        >

            {sender === "bot" && (
                <div className="avatar bot-avatar">
                    🤖
                </div>
            )}

            <div
                className={`message-bubble ${
                    sender === "user" ? "user-bubble" : "bot-bubble"
                }`}
            >
                {text}
            </div>

            {sender === "user" && (
                <div className="avatar user-avatar">
                    👤
                </div>
            )}

        </div>

    );

}

export default Message;