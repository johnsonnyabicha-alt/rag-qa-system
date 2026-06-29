import { useState } from 'react';

export function QueryInput({ onSubmit, loading }) {
    const [query, setQuery] = useState('');
    const [topK, setTopK] = useState(5);
    
    const handleSubmit = async (e) => {
        e.preventDefault();
        if (!query.trim()) return;
        await onSubmit(query, topK);
        setQuery('');
    };
    
    return (
        <form onSubmit={handleSubmit}>
            <div style={{ display: 'flex', gap: '10px', marginBottom: '15px' }}>
                <input
                    type="text"
                    value={query}
                    onChange={(e) => setQuery(e.target.value)}
                    placeholder="Ask about philosophy, politics, or economics..."
                    style={{ flex: 1, padding: '15px', borderRadius: '8px', border: '2px solid #ddd' }}
                    disabled={loading}
                />
                <button type="submit" disabled={loading || !query.trim()} style={{ padding: '15px 30px', backgroundColor: '#007bff', color: 'white', border: 'none', borderRadius: '8px' }}>
                    {loading ? 'Searching...' : 'Search'}
                </button>
            </div>
            <label style={{ fontSize: '14px' }}>
                Top Results: <select value={topK} onChange={(e) => setTopK(Number(e.target.value))}>
                    <option value={3}>3</option>
                    <option value={5}>5</option>
                    <option value={10}>10</option>
                </select>
            </label>
        </form>
    );
}