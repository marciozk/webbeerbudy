# WebBeerBuddy 🍺

Never forget whose turn it is to buy the next round! WebBeerBuddy helps you and your friends keep track of beer rounds in a fun and fair way.

## Features

- Create and manage drinking groups
- Track who bought the last round
- Smart rotation system
- Real-time notifications
- Mobile-friendly interface

## Tech Stack

- Frontend: React.js with Tailwind CSS
- Backend: Python FastAPI
- Database: SQLite
- Authentication: JWT

## Local Development Setup

### Backend Setup

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: .\venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the backend server:
```bash
uvicorn app.main:app --reload
```

### Frontend Setup

1. Install Node.js dependencies:
```bash
cd frontend
npm install
```

2. Run the development server:
```bash
npm run dev
```

## Deployment

### Backend (Render)

1. Create a new account on render.com
2. Create a new Web Service
3. Connect your GitHub repository
4. Set build command: `pip install -r requirements.txt`
5. Set start command: `uvicorn app.main:app --host 0.0.0.0 --port $PORT`

### Frontend (Vercel)

1. Create a new account on vercel.com
2. Import your GitHub repository
3. Configure build settings:
   - Framework Preset: Next.js
   - Build Command: `npm run build`
   - Output Directory: `dist`

## Contributing

Feel free to submit issues and enhancement requests!
