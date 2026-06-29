export function ResponseDisplay({ response, loading }) {
    if (loading) return <div style={{ textAlign: 'center', padding: '40px' }}>Searching knowledge base...</div>;
    if (!response) return null;
    
    return (
        <div style={{ backgroundColor: 'white', borderRadius: '12px', padding: '30px', marginTop: '30px' }}>
            <h2>Answer</h2>
            <p style={{ backgroundColor: '#f5f5f5', padding: '20px', borderRadius: '8px' }}>{response.answer}</p>
            {response.sources && response.sources.length > 0 && (
                <div style={{ marginTop: '30px' }}>
                    <h3>Sources ({response.sources.length})</h3>
                    {response.sources.map((source, idx) => (
                        <div key={idx} style={{ backgroundColor: '#f5f5f5', padding: '15px', marginBottom: '10px', borderRadius: '6px' }}>
                            <strong>{source.source}</strong>
                            <p style={{ fontSize: '14px', color: '#666', marginTop: '8px' }}>{source.content.substring(0, 300)}...</p>
                            <small>{(source.score * 100).toFixed(1)}% relevant</small>
                        </div>
                    ))}
                </div>
            )}
        </div>
    );
}