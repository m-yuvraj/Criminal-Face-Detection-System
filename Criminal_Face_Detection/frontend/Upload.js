import React, { useState } from 'react';

function Upload() {
    const [file, setFile] = useState(null);
    const [result, setResult] = useState("");

    const handleFileChange = (e) => {
        setFile(e.target.files[0]);
    };

    const uploadAndRecognize = async () => {
        const formData = new FormData();
        formData.append('image', file);

        const response = await fetch('/recognize', {
            method: 'POST',
            body: formData,
        });
        
        const data = await response.json();
        setResult(data.message);
    };

    return (
        <div>
            <input type="file" onChange={handleFileChange} />
            <button onClick={uploadAndRecognize}>Recognize Face</button>
            <p>{result}</p>
        </div>
    );
}

export default Upload;
