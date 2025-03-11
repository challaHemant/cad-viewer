import React, { useState } from "react";
import { Canvas, useLoader } from "@react-three/fiber";
import { OrbitControls } from "@react-three/drei";
import * as THREE from "three";
import { OBJLoader } from "three/examples/jsm/loaders/OBJLoader.js";
import "./App.css";

const ModelViewer = ({ modelPath }) => {
  const model = useLoader(OBJLoader, modelPath);

  return <primitive object={model} scale={0.5} />;
};


function App() {
    const [file, setFile] = useState(null);
    const [modelPath, setModelPath] = useState(null);
    const [convertedModelPath, setConvertedModelPath] = useState(null);
    const [uploadSuccess, setUploadSuccess] = useState(false);

    const handleFileChange = (event) => {
        setFile(event.target.files[0]);
        setUploadSuccess(false); // Reset success state
        setModelPath(null);
        setConvertedModelPath(null);
    };

    const handleUpload = async () => {
      if (!file) return alert("Please select a file");
  
      const formData = new FormData();
      formData.append("file", file);
  
      try {
          const response = await fetch("http://127.0.0.1:5001/upload", {
              method: "POST",
              body: formData,
          });
  
          const result = await response.json();
          console.log("✅ Upload Response:", result); // Debugging
  
          if (response.ok) {
              setModelPath(result.file_url); // ✅ Fix: Use `file_url`
              setUploadSuccess(true);
              alert("✅ Upload successful!");
          } else {
              alert("❌ Upload failed!");
          }
      } catch (error) {
          console.error("❌ Upload Error:", error);
          alert("Upload failed!");
      }
  };
  

  const handleConvert = async () => {
    if (!modelPath) return alert("No model to convert");

    console.log("🔄 Converting model:", modelPath); // Debugging

    try {
        const response = await fetch("http://127.0.0.1:5001/convert", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ input_path: modelPath }),
        });

        const result = await response.json();
        console.log("✅ Convert Response:", result); // Debugging

        if (response.ok) {
            setConvertedModelPath(result.output_path); // ✅ Fix: Set converted model URL
            alert("✅ Conversion successful!");
        } else {
            alert("❌ Conversion failed!");
        }
    } catch (error) {
        console.error("❌ Convert Error:", error);
        alert("Conversion failed!");
    }
};

  
  

    return (
        <div className="App">
            <header className="App-header">
                <h1>3D Model Upload & Viewer</h1>
                <input type="file" onChange={handleFileChange} />
                <button onClick={handleUpload}>Upload</button>
                <button onClick={handleConvert} disabled={!modelPath}>
    Convert to OBJ
</button>
            </header>
            <div style={{ width: "100vw", height: "80vh" }}>
                <Canvas>
                    <ambientLight />
                    <OrbitControls />
                    {modelPath && <ModelViewer modelPath={convertedModelPath || modelPath} />}
                </Canvas>
            </div>
        </div>
    );
}

export default App;
