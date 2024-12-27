import React, { useState, useRef, useEffect } from 'react';
import styled from 'styled-components';
import { FaCloudUploadAlt, FaFile } from 'react-icons/fa';


const FormContainer = styled.div`
    width: 100%;
    max-width: 600px;
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 1.5rem;
    margin: 0 auto;
    padding: 1rem;
`;

const UploadArea = styled.div`
    width: 100%;
    position: relative;
    padding: 2rem;
    background: linear-gradient(145deg, #ffffff, #f5f5f5);
    border-radius: 12px;
    box-shadow: 5px 5px 15px #d9d9d9, -5px -5px 15px #ffffff;
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 1rem;
    cursor: pointer;
    transition: all 0.3s ease;

    &:hover {
        transform: translateY(-2px);
        box-shadow: 6px 6px 18px #d9d9d9, -6px -6px 18px #ffffff;
    }
`;

const HiddenInput = styled.input`
    display: none;
`;

const UploadIcon = styled(FaCloudUploadAlt)`
    font-size: 3rem;
    color: #00796b;
    margin-bottom: 1rem;
`;

const UploadText = styled.div`
    text-align: center;
    color: #333;
`;

const MainText = styled.p`
    font-size: 1.2rem;
    font-weight: 600;
    color: #00796b;
    margin-bottom: 0.5rem;
`;

const SubText = styled.p`
    font-size: 0.9rem;
    color: #666;
`;

const SelectedFile = styled.div`
    display: flex;
    align-items: center;
    gap: 0.5rem;
    padding: 0.75rem 1.5rem;
    background-color: #e0f7fa;
    border-radius: 8px;
    color: #00796b;
    font-size: 0.9rem;
`;

const FileIcon = styled(FaFile)`
    font-size: 1.2rem;
`;

const UploadButton = styled.button`
    padding: 0.75rem 2rem;
    background: linear-gradient(135deg, #00796b 0%, #009688 100%);
    color: white;
    border: none;
    border-radius: 8px;
    font-size: 1.1rem;
    font-weight: 600;
    cursor: pointer;
    transition: all 0.3s ease;
    box-shadow: 0 4px 12px rgba(0, 121, 107, 0.2);
    display: flex;
    align-items: center;
    gap: 0.5rem;

    &:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 16px rgba(0, 121, 107, 0.3);
        background: linear-gradient(135deg, #00695c 0%, #00897b 100%);
    }

    &:disabled {
        background: #cccccc;
        cursor: not-allowed;
        transform: none;
        box-shadow: none;
    }
`;

const ImagePreviewWrapper = styled.div`
    width: 100%;
    height: 300px;
    border-radius: 8px;
    overflow: hidden;
    margin: 1rem auto;
    position: relative;
    background-color: #f5f5f5;
    display: flex;
    justify-content: center;
    align-items: center;
`;

const PreviewImage = styled.img`
    max-width: 100%;
    max-height: 100%;
    object-fit: contain;
    display: block;
    margin: auto;
`;

const UploadForm = ({ onUpload }) => {
    const [selectedFile, setSelectedFile] = useState(null);
    const [previewUrl, setPreviewUrl] = useState(null);
    const fileInputRef = useRef(null);
    const [isDragging, setIsDragging] = useState(false);

    const handleFileSelection = (file) => {
        if (file && file.type.startsWith('image/')) {
            setSelectedFile(file);
            const fileUrl = URL.createObjectURL(file);
            setPreviewUrl(fileUrl);
        }
    };

    const handleFileSelect = (event) => {
        const file = event.target.files[0];
        handleFileSelection(file);
    };

    const handleUploadClick = async () => {
        if (selectedFile) {
            const formData = new FormData();
            formData.append('image', selectedFile);
            
            try {
                console.log('Attempting upload to:', process.env.NEXT_PUBLIC_API_URL); // Debug log
                await onUpload(formData);
            } catch (error) {
                console.error('Upload failed:', error);
                alert(`Upload failed: ${error.message}`);
            }
        }
    };

    const handleAreaClick = () => {
        fileInputRef.current.click();
    };

    const handleDragEnter = (e) => {
        e.preventDefault();
        e.stopPropagation();
        setIsDragging(true);
    };

    const handleDragLeave = (e) => {
        e.preventDefault();
        e.stopPropagation();
        setIsDragging(false);
    };

    const handleDragOver = (e) => {
        e.preventDefault();
        e.stopPropagation();
        setIsDragging(true);
    };

    const handleDrop = (e) => {
        e.preventDefault();
        e.stopPropagation();
        setIsDragging(false);

        const file = e.dataTransfer.files[0];
        handleFileSelection(file);
    };

    // Cleanup preview URL when component unmounts or when new file is selected
    const cleanupPreview = () => {
        if (previewUrl) {
            URL.revokeObjectURL(previewUrl);
        }
    };

    // Cleanup on component unmount
    useEffect(() => {
        return () => cleanupPreview();
    }, []);

    // Cleanup previous preview when new file is selected
    useEffect(() => {
        return () => cleanupPreview();
    }, [selectedFile]);

    return (
        <FormContainer>
            <UploadArea
                onClick={handleAreaClick}
                onDragEnter={handleDragEnter}
                onDragOver={handleDragOver}
                onDragLeave={handleDragLeave}
                onDrop={handleDrop}
                style={{
                    borderColor: isDragging ? '#009688' : undefined,
                    background: isDragging ? 'rgba(0, 150, 136, 0.1)' : undefined
                }}
            >
                <HiddenInput
                    type="file"
                    ref={fileInputRef}
                    onChange={handleFileSelect}
                    accept="image/*"
                />
                {!previewUrl ? (
                    <>
                        <UploadIcon />
                        <UploadText>
                            <MainText>
                                {isDragging ? 'Drop your image here' : 'Choose a file or drag it here'}
                            </MainText>
                            <SubText>Supports: JPG, PNG, GIF (max 10MB)</SubText>
                        </UploadText>
                    </>
                ) : (
                    <ImagePreviewWrapper>
                        <PreviewImage src={previewUrl} alt="Preview" />
                    </ImagePreviewWrapper>
                )}
            </UploadArea>

            {selectedFile && (
                <SelectedFile>
                    <FileIcon />
                    {selectedFile.name}
                </SelectedFile>
            )}

            <UploadButton
                onClick={handleUploadClick}
                disabled={!selectedFile}
            >
                <FaCloudUploadAlt />
                {selectedFile ? 'Upload Image' : 'Select an Image'}
            </UploadButton>
        </FormContainer>
    );
};

export default UploadForm;