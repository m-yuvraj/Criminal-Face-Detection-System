import React, { useState } from 'react';

function CriminalDetails() {
    const [search, setSearch] = useState('');
    const [details, setDetails] = useState(null);

    const handleSearch = async () => {
        const response = await fetch(`http://localhost:5000/get_criminal_details/${search}`);
        const result = await response.json();
        setDetails(result);
    };

    return (
        <div>
            <input
                type="text"
                placeholder="Enter Criminal Name or ID"
                value={search}
                onChange={(e) => setSearch(e.target.value)}
            />
            <button onClick={handleSearch}>Search</button>
            {details && (
                <div>
                    <h3>Details:</h3>
                    <p>Name: {details.name}</p>
                    <p>Age: {details.age}</p>
                    <p>Crimes: {details.crimes}</p>
                </div>
            )}
        </div>
    );
}

export default CriminalDetails;
