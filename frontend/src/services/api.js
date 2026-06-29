const API_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000/api';

export const uploadDocument = async (file) => {
    const formData = new FormData();
    formData.append('file', file);
    const response = await fetch(`${API_URL}/upload`, { method: 'POST', body: formData });
    if (!response.ok) throw new Error(`Upload failed: ${response.statusText}`);
    return response.json();
};

export const queryDocuments = async (query, topK = 5) => {
    const response = await fetch(`${API_URL}/query`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ query, top_k: topK }),
    });
    if (!response.ok) throw new Error(`Query failed: ${response.statusText}`);
    return response.json();
};