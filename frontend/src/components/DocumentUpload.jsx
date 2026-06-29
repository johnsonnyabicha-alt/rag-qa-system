import { useState } from 'react';
import { uploadDocument } from '../services/api';

export function DocumentUpload({ onUploadSuccess }) {
    const [loading, setLoading] = useState(false);
    const [uploadHistory, setUploadHistory] = useState([]);
    
    const handleFileChange = async (files) => {
        if (!files || files.length === 0) return;
        const file = files[0];
        setLoading(true);
        
        try {
            const result = await uploadDocument(file);
            setUploadHistory([...uploadHistory, { filename: result.filename, chunks: result.chunks, timestamp: new Date().toLocaleTimeString() }]);
            alert(`Success! Uploaded "${result.filename}" (${result.chunks} chunks)`);
            onUploadSuccess();
        } catch (error) {
            alert(`Error uploading document: ${error.message}`);
        } finally {
            setLoading(false);
        }
    };
    
    return (
        <div style={{ backgroundColor: 'white', borderRadius: '12px', padding: '30px', marginBottom: '30px' }}>
            <h2>Upload Documents</h2>
            <div style={{ border: '2px dashed #ddd', borderRadius: '8px', padding: '40px 20px', textAlign: 'center', backgroundColor: '#f5f5f5' }}>
                <input
                    type="file"
                    onChange={(e) => handleFileChange(e.target.files)}
                    disabled={loading}
                    accept=".txt,.pdf,.doc,.docx"
                    style={{ display: 'none' }}
                    id="file-upload"
                />
                <label htmlFor="file-upload" style={{ cursor: 'pointer' }}>
                    {loading ? <p>Uploading...</p> : <>
                        <p style={{ fontSize: '48px' }}>📁</p>
                        <p><strong>Drag & drop your file here</strong></p>
                        <p style={{ fontSize: '14px', color: '#999' }}>or click to browse</p>
                    </>}
                </label>
            </div>
            {uploadHistory.length > 0 && (
                <div style={{ marginTop: '30px', paddingTop: '30px', borderTop: '1px solid #ddd' }}>
                    <h3>Recent Uploads</h3>
                    <ul style={{ listStyle: 'none' }}>
                        {uploadHistory.map((item, idx) => (
                            <li key={idx} style={{ padding: '12px 0', borderBottom: '1px solid #ddd', display: 'flex', justifyContent: 'space-between' }}>
                                <span><strong>{item.filename}</strong></span>
                                <span style={{ fontSize: '12px', color: '#999' }}>{item.chunks} chunks • {item.timestamp}</span>
                            </li>
                        ))}
                    </ul>
                </div>
            )}
        </div>
    );
}