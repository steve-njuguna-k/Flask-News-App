from app import app

@app.route('/')
def home():
    return 'Flask App Initialized!'