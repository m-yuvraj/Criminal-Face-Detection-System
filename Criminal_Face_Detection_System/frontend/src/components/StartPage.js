import React from 'react';
import { Link } from 'react-router-dom';

function StartPage() {
    return (
        <div>
            <h1>Criminal Face Detection System</h1>
            <ul>
                <li><Link to="/register">Register a Criminal</Link></li>
                <li><Link to="/detect-photo">Detect from Photo</Link></li>
                <li><Link to="/details">Criminal Details</Link></li>
                <li><Link to="/detect-video">Detect from Video</Link></li>
            </ul>
        </div>
    );
}

export default StartPage;
