const API_BASE_URL = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000';

export const processImage = async (formData) => {
    try {
        const response = await fetch(`${API_BASE_URL}/api/process-image`, {
            method: 'POST',
            body: formData,
            credentials: 'include',
            mode: 'cors',
            headers: {
                'Accept': 'application/json',
            },
        });

        if (!response.ok) {
            const errorData = await response.json();
            throw new Error(errorData.error || 'Failed to process image');
        }

        return await response.json();
    } catch (error) {
        console.error('API Error:', error);
        throw new Error(`Failed to connect to server: ${error.message}`);
    }
};