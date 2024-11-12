import React, { useState } from 'react';

function Camera() {
    const [result, setResult] = useState("");

    const captureAndDetect = async () => {
        // Capture image from webcam here, and send it to backend for detection
        const response = await fetch('/detect', {
            method: 'POST',
            body: capturedImage,
        });
        
        const data = await response.json();
        setResult(data.message);
    };

    return (
        <div>
            <button onClick={captureAndDetect}>Start Detection</button>
            <p>{result}</p>
        </div>
    );
}

export default Camera;
