import React from 'react';
import Camera from './components/Camera';
import Upload from './components/Upload';

function App() {
    return (
        <div className="App">
            <h1>Criminal Face Detection System</h1>
            <Camera />
            <Upload />
        </div>
    );
}

export default App;
