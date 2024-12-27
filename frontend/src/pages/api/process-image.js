export default async function handler(req, res) {
    if (req.method === 'POST') {
        const response = await fetch('http://localhost:8000/api/process-image', {
            method: 'POST',
            body: req.body,
        });

        const data = await response.json();
        res.status(response.status).json(data);
    } else {
        res.setHeader('Allow', ['POST']);
        res.status(405).end(`Method ${req.method} Not Allowed`);
    }
}