import { useState } from "react";
import "./App.css";

export default function App() {
  const [file, setFile] = useState(null);
  const [question, setQuestion] = useState("");
  const [answer, setAnswer] = useState("");
  const [loading, setLoading] = useState(false);

  const uploadPDF = async () => {
    if (!file) {
      alert("Please select a PDF file");
      return;
    }

    const formData = new FormData();
    formData.append("file", file);

    await fetch("http://localhost:8000/upload", {
      method: "POST",
      body: formData,
    });

    alert("PDF uploaded successfully");
  };

  const askQuestion = async () => {
    if (!question) return;

    setLoading(true);
    setAnswer("");

    const res = await fetch(
      `http://localhost:8000/ask?question=${encodeURIComponent(question)}`,
      { method: "POST" }
    );

    const data = await res.json();
    setAnswer(data.answer);
    setLoading(false);
  };

  return (
    <div className="page">
      <div className="glass-card">
        <h1 className="hero-title">Ask Your PDF</h1>
        <p className="hero-subtitle">
          Upload a document and chat with its content using AI
        </p>

        {/* Upload */}
        <div className="block">
          <label className="label">Upload PDF</label>
          <input
            type="file"
            accept="application/pdf"
            className="file-input"
            onChange={(e) => setFile(e.target.files[0])}
          />
          <button className="btn primary" onClick={uploadPDF}>
            Upload Document
          </button>
        </div>

        {/* Question */}
        <div className="block">
          <label className="label">Ask a question</label>
          <input
            className="text-input"
            value={question}
            onChange={(e) => setQuestion(e.target.value)}
          />
          <button
            className="btn secondary"
            onClick={askQuestion}
            disabled={loading}
          >
            {loading ? "Thinking..." : "Ask AI"}
          </button>
        </div>

        {/* Answer */}
        {answer && (
          <div className="chat">
            <div className="chat-bubble">{answer}</div>
          </div>
        )}
      </div>
    </div>
  );
}
