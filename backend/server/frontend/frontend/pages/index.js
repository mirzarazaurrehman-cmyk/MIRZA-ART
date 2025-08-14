import { useState } from "react";
import axios from "axios";

export default function Home() {
  const [prompt, setPrompt] = useState("");
  const [videoUrl, setVideoUrl] = useState("");
  const [loading, setLoading] = useState(false);

  const generateVideo = async () => {
    try {
      setLoading(true);
      const res = await axios.post("http://localhost:8000/api/generate-video", null, {
        params: { prompt }
      });
      setVideoUrl(res.data.video_url);
    } catch (err) {
      alert("Error: " + err.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="flex flex-col items-center p-8">
      <h1 className="text-3xl font-bold mb-4">AI Video Generator</h1>
      <textarea
        className="border p-2 w-96 mb-4"
        placeholder="اپنا ویڈیو پرامپٹ لکھیں..."
        value={prompt}
        onChange={(e) => setPrompt(e.target.value)}
      />
      <button
        className="bg-blue-500 text-white px-4 py-2 rounded"
        onClick={generateVideo}
        disabled={loading}
      >
        {loading ? "Generating..." : "Generate Video"}
      </button>

      {videoUrl && (
        <video className="mt-6" src={videoUrl} controls autoPlay loop width="640" />
      )}
    </div>
  );
}
