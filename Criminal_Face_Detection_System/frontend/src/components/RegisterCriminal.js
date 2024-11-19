import React, { useState } from 'react';

function RegisterCriminal() {
    const [formData, setFormData] = useState({ name: '', age: '', crimes: '' });
    const [image, setImage] = useState(null);

    const handleSubmit = async (e) => {
        e.preventDefault();
        const data = new FormData();
        data.append('name', formData.name);
        data.append('age', formData.age);
        data.append('crimes', formData.crimes);
        data.append('image', image);

        const response = await fetch('http://localhost:5000/register_criminal', {
            method: 'POST',
            body: data,
        });
        const result = await response.json();
        alert(result.message);
    };

    return (
        <form onSubmit={handleSubmit}>
            <input
                type="text"
                placeholder="Name"
                value={formData.name}
                onChange={(e) => setFormData({ ...formData, name: e.target.value })}
            />
            <input
                type="number"
                placeholder="Age"
                value={formData.age}
                onChange={(e) => setFormData({ ...formData, age: e.target.value })}
            />
            <input
                type="text"
                placeholder="Crimes"
                value={formData.crimes}
                onChange={(e) => setFormData({ ...formData, crimes: e.target.value })}
            />
            <input type="file" onChange={(e) => setImage(e.target.files[0])} />
            <button type="submit">Register</button>
        </form>
    );
}

export default RegisterCriminal;
