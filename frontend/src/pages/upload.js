import { useState } from 'react';
import styled from 'styled-components';
import { ErrorBoundary } from 'react-error-boundary';
import { Spinner } from '@/components/Spinner';
import UploadForm from '@/components/UploadForm';
import { processImage } from '@/utils/api';


const PageContainer = styled.div`
    min-height: 100vh;
    background: linear-gradient(135deg, #e0f7fa 0%, #b2ebf2 100%);
    padding: 2rem;
`;

const ResultContainer = styled.div`
    margin-top: 2rem;
    padding: 2rem;
    background-color: white;
    border-radius: 12px;
    box-shadow: 0 4px 16px rgba(0, 0, 0, 0.1);
    width: 100%;
    max-width: 800px;
    margin: 2rem auto;
`;

const ResultItem = styled.div`
    margin: 1.5rem 0;
    padding: 1.5rem;
    background: #ffffff;
    border-radius: 8px;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.05);
    
    h3 {
        color: #00796b;
        margin-bottom: 1rem;
        font-size: 1.3rem;
        border-bottom: 2px solid #e0f2f1;
        padding-bottom: 0.5rem;
    }
    
    p {
        color: #333;
        line-height: 1.6;
        font-size: 1.1rem;
        margin-bottom: 1rem;
    }

    .context-label {
        font-weight: 600;
        color: #00796b;
        margin-top: 1rem;
    }
`;

const SentimentBox = styled.div`
    display: flex;
    flex-direction: column;
    gap: 1rem;
`;

const SentimentItem = styled.div`
    display: flex;
    align-items: center;
    gap: 1rem;
    padding: 0.8rem;
    background: ${props => props.type === 'emotional_elements' ? '#f3e5f5' : getSentimentColor(props.type, props.value)};
    border-radius: 6px;
    
    span.label {
        font-weight: 600;
        min-width: 120px;
    }
    
    span.score {
        color: ${props => props.type === 'emotional_elements' ? '#6a1b9a' : getSentimentTextColor(props.type, props.value)};
        font-weight: 500;
    }
`;

// Helper functions for sentiment colors
const getSentimentColor = (type, value) => {
    if (type === 'polarity') {
        return value > 0 ? '#e8f5e9' : value < 0 ? '#ffebee' : '#f5f5f5';
    }
    return '#f5f5f5';
};

const getSentimentTextColor = (type, value) => {
    if (type === 'polarity') {
        return value > 0 ? '#2e7d32' : value < 0 ? '#c62828' : '#424242';
    }
    return '#424242';
};

const formatSentimentValue = (type, value) => {
    if (type === 'emotional_elements' && Array.isArray(value)) {
        return value.join(', ');
    }
    if (type === 'polarity' || type === 'subjectivity') {
        return `${(value * 100).toFixed(1)}%`;
    }
    return value;
};

const ErrorMessage = styled.div`
    background-color: #ffebee;
    color: #c62828;
    padding: 1rem;
    border-radius: 8px;
    margin-bottom: 1rem;
    text-align: center;
    width: 100%;
    max-width: 600px;
    margin: 0 auto;
`;

const ErrorFallback = ({ error }) => {
    return (
        <div role="alert">
            <p>Something went wrong:</p>
            <pre style={{ color: 'red' }}>{error.message}</pre>
        </div>
    );
};

const UploadPage = () => {
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState(null);
    const [result, setResult] = useState(null);

    const handleUpload = async (formData) => {
        try {
            setLoading(true);
            setError(null);
            
            console.log('Starting upload process...'); // Debug log
            const data = await processImage(formData);
            console.log('Upload successful, sentiment data:', data.sentiment_analysis); // Add this debug log
            setResult(data);
        } catch (err) {
            console.error('Upload error:', err);
            setError(err.message || 'Failed to upload image');
        } finally {
            setLoading(false);
        }
    };

    return (
        <ErrorBoundary FallbackComponent={ErrorFallback}>
            <PageContainer>
                {error && <ErrorMessage>{error}</ErrorMessage>}
                <UploadForm onUpload={handleUpload} />
                {loading && <Spinner />}
                {result && (
                    <ResultContainer>
                        <h2>Results:</h2>
                        <ResultItem>
                            <h3>Alt Text</h3>
                            <p>{result.alt_text}</p>
                        </ResultItem>
                        <ResultItem>
                            <h3>Image Analysis</h3>
                            <div className="context-label">Basic Context:</div>
                            <p>{result.context}</p>
                            <div className="context-label">Enhanced Analysis:</div>
                            <p>{result.enhanced_context}</p>
                        </ResultItem>
                        <ResultItem>
                            <h3>Sentiment Analysis</h3>
                            <SentimentBox>
                                {result.sentiment_analysis && typeof result.sentiment_analysis === 'object' && (
                                    <>
                                        {Object.entries(result.sentiment_analysis).map(([key, value]) => {
                                            const label = key.charAt(0).toUpperCase() + 
                                                        key.slice(1).replace(/_/g, ' ');
                                            return (
                                                <SentimentItem 
                                                    key={key} 
                                                    type={key.toLowerCase()} 
                                                    value={value}
                                                >
                                                    <span className="label">{label}:</span>
                                                    <span className="score">
                                                        {formatSentimentValue(key.toLowerCase(), value)}
                                                    </span>
                                                </SentimentItem>
                                            );
                                        })}
                                    </>
                                )}
                            </SentimentBox>
                        </ResultItem>
                    </ResultContainer>
                )}
            </PageContainer>
        </ErrorBoundary>
    );
};

export default UploadPage;