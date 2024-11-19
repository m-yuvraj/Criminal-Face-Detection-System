import React, { useState } from 'react';

function DetectFromVideo() {
    const [results, setResults] = useState([]);

    const handleVideo = () => {
        const eventSource = new EventSource('http://localhost:5000/detect_video');
        eventSource.onmessage = (event) => {
            const data = JSON.parse(event.data);
            setResults((prev) => [...prev, data]);
        };
    };

    return (
        <div>
            <button onClick={handleVideo}>Start Video Detection</button>
            {results.length > 0 && (
                <div>
                    <h3>Detected Criminals:</h3>
                    <ul>
                        {results.map((criminal, index) => (
                            <li key={index}>{criminal.name}</li>
                        ))}
                    </ul>
                </div>
            )}
        </div>
    );
}

export default DetectFromVideo;
