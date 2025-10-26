# ink-bot-react1
sports ai



# Sports AI - Football Position Predictor 🚽

An AI model trained to predict football players' positions based on natural language questions.

## 🎯 Features
- Trained on 21,000+ player records from FIFA, transfer data, and match statistics
- Predicts positions for 34 different football positions
- Natural language question answering
- Web interface powered by Gradio

## 🚀 Deployment

### Option 1: Hugging Face Spaces (Recommended)
1. Fork this repository
2. Go to [Hugging Face Spaces](https://huggingface.co/spaces)
3. Create a new Space
4. Connect your GitHub repository
5. Set Space SDK to "Gradio"
6. Deploy!

### Option 2: Render.com
1. Push your code to GitHub
2. Create a new Web Service on Render
3. Connect your repository
4. Set build command: `pip install -r requirements.txt`
5. Set start command: `python app.py`
6. Deploy!

### Option 3: Local Development
```bash
# Install dependencies
pip install -r requirements.txt

# Run the app
python app.py
```

## 📊 Model Details
- **Model**: DistilBERT (distilbert-base-uncased)
- **Training Data**: 21,153 samples
- **Positions**: 34 unique football positions
- **Validation Accuracy**: 15.86%

## 🎮 Usage
Ask questions like:
- "What position does Lionel Messi play?"
- "Tell me about Cristiano Ronaldo's position"
- "What does Kevin De Bruyne play as?"

## 📁 Project Structure
