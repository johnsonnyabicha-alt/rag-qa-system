import { useState } from 'react';
import { queryDocuments } from './services/api';
import { QueryInput } from './components/QueryInput';
import { ResponseDisplay } from './components/ResponseDisplay';
import { DocumentUpload } from './components/DocumentUpload';

function App() {
    const [response, setResponse] = useState(null);
    const [chatHistory, setChatHistory] = useState([]);
    const [loading, setLoading] = useState(false);
    
    const handleQuery = async (query, topK) => {
        setLoading(true);
        try {
            const result = await queryDocuments(query, topK);
            setResponse(result);
            setChatHistory([{ query, response: result }, ...chatHistory]);
        } catch (error) {
            alert('Error: ' + error.message);
        } finally {
            setLoading(false);
        }
    };
    
    return (
        <div style={{ minHeight: '100vh', display: 'flex', flexDirection: 'column', backgroundColor: '#f0f2f5' }}>
            <header style={{ background: 'linear-gradient(135deg, #007bff 0%, #0056b3 100%)', color: 'white', padding: '50px 20px', textAlign: 'center' }}>
                <h1 style={{ fontSize: '36px', marginBottom: '10px' }}>🌍 Philosophy, Politics & Economics RAG</h1>
                <p style={{ fontSize: '18px' }}>AI-powered knowledge base for understanding global affairs</p>
            </header>
            
            <main style={{ flex: 1, padding: '40px 20px' }}>
                <div style={{ maxWidth: '900px', margin: '0 auto' }}>
                    <DocumentUpload onUploadSuccess={() => console.log('Document uploaded')} />
                    <QueryInput onSubmit={handleQuery} loading={loading} />
                    <ResponseDisplay response={response} loading={loading} />
                    
                    {chatHistory.length > 0 && (
                        <div style={{ backgroundColor: 'white', borderRadius: '12px', padding: '30px', marginTop: '40px' }}>
                            <h2>Chat History</h2>
                            {chatHistory.map((item, idx) => (
                                <div key={idx} style={{ borderBottom: '1px solid #ddd', padding: '12px 0' }}>
                                    <strong>Q:</strong> {item.query}
                                    <p style={{ marginTop: '8px', color: '#666' }}><strong>A:</strong> {item.response.answer.substring(0, 150)}...</p>
                                </div>
                            ))}
                        </div>
                    )}
                </div>
            </main>
            
            <footer style={{ backgroundColor: '#333', color: 'white', textAlign: 'center', padding: '20px', fontSize: '14px' }}>
                <p>PPE RAG Q&A System v1.0 | Built with FastAPI, React & Pinecone</p>
            </footer>
        </div>
    );
}

export default App;