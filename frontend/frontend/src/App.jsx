import { useState } from "react";
import axios from "axios";

function App() {

  const [question, setQuestion] = useState("");
  const [answer, setAnswer] = useState("");

  const askAI = async () => {

    const response = await axios.post(
      "http://127.0.0.1:8000/ask",
      {
        question: question
      }
    );

    setAnswer(response.data.answer);
  };

  return (
    <div style={{ padding: "20px" }}>

      <h1>AI Study Coach</h1>

      <input
        type="text"
        value={question}
        onChange={(e) => setQuestion(e.target.value)}
        placeholder="Ask something..."
        style={{
          width: "300px",
          padding: "10px"
        }}
      />

      <button
        onClick={askAI}
        style={{
          marginLeft: "10px",
          padding: "10px"
        }}
      >
        Ask
      </button>

      <div style={{ marginTop: "20px" }}>
        <strong>Answer:</strong>
        <p>{answer}</p>
      </div>

    </div>
  );
}

export default App;