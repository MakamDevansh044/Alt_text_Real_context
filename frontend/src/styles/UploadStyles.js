import styled from 'styled-components';

export const Container = styled.div`
  padding: 2rem;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 1rem;
`;

export const UploadForm = styled.form`
  max-width: 500px;
  width: 100%;
  padding: 1rem;
`;

export const Button = styled.button`
  margin-top: 1rem;
  padding: 0.5rem 1rem;
  background-color: #0070f3;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;

  &:hover {
    background-color: #0051b3;
  }
`; 