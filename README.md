# AltContextPro

An AI-powered image analysis tool that generates detailed alt text, contextual information, and sentiment analysis for images using multiple AI models.

## Features

- 🖼️ Image Upload & Processing with drag-and-drop support
- 🤖 AI-Powered Alt Text Generation
- 📝 Enhanced Context Generation
- 🎭 Sentiment Analysis with emotional elements
- 🔄 Multiple AI Model Support (OpenAI, Gemini, Hugging Face)
- 🎨 Modern, Responsive UI with styled-components

## Project Structure

## Deployment on Vercel

### Frontend Deployment

1. **Prepare Frontend**

   ```bash
   cd frontend
   npm run build  # Test build locally first
   ```

2. **Install Vercel CLI**

   ```bash
   npm install -g vercel
   ```

3. **Deploy to Vercel**

   ```bash
   vercel login
   vercel
   ```

   Or deploy through Vercel Dashboard:
   - Push your code to GitHub
   - Import your repository in Vercel Dashboard
   - Configure build settings:

     ```
     Build Command: npm run build
     Output Directory: .next
     Install Command: npm install
     ```

   - Add environment variables:

     ```
     NEXT_PUBLIC_API_URL=https://your-backend-url.vercel.app
     ```

### Backend Deployment

1. **Prepare Backend**
   - Create `vercel.json` in backend directory:

   ```json:backend/vercel.json
   {
     "version": 2,
     "builds": [
       {
         "src": "run.py",
         "use": "@vercel/python"
       }
     ],
     "routes": [
       {
         "src": "/(.*)",
         "dest": "run.py"
       }
     ]
   }
   ```

   - Create `requirements.txt`:

   ```bash
   cd backend
   pipenv lock -r > requirements.txt
   ```

2. **Deploy Backend**
   ```bash
   vercel
   ```

   Or through Vercel Dashboard:
   - Import your backend repository
   - Configure build settings:
     ```
     Build Command: pip install -r requirements.txt
     Output Directory: .
     Install Command: python run.py
     ```
   - Add environment variables:
     ```
     HUGGINGFACE_API_KEY=your_key
     OPENAI_API_KEY=your_key
     GEMINI_API_KEY=your_key
     ```

### Post-Deployment

1. **Update Frontend API URL**
   - Get your backend deployment URL from Vercel
   - Update frontend environment variable:
   ```
   NEXT_PUBLIC_API_URL=https://your-backend-url.vercel.app
   ```

2. **Configure CORS**
   - Update backend CORS settings in `app/__init__.py`:
   ```python
   CORS(app, resources={
       r"/api/*": {
           "origins": ["https://your-frontend-url.vercel.app"],
           "methods": ["GET", "POST", "OPTIONS"]
       }
   })
   ```

3. **Verify Deployment**
   - Test frontend: `https://your-frontend-url.vercel.app`
   - Test backend: `https://your-backend-url.vercel.app/api/test`

### Troubleshooting Deployment

1. **Backend Issues**
   - Check Vercel logs for Python errors
   - Verify environment variables are set
   - Test API endpoints using Postman

2. **Frontend Issues**
   - Check build logs in Vercel dashboard
   - Verify API URL is correct
   - Check browser console for CORS errors

3. **Common Solutions**
   - Redeploy after environment variable changes
   - Clear Vercel cache if needed
   - Check function execution timeout limits
