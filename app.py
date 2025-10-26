import gradio as gr
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import joblib
import os

# Load the model and tokenizer
MODEL_PATH = "./final-model"
LABEL_ENCODER_PATH = "./label_encoder.pkl"

print("Loading model and tokenizer...")
tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH)
model = AutoModelForSequenceClassification.from_pretrained(MODEL_PATH)
label_encoder = joblib.load(LABEL_ENCODER_PATH)
print("Model loaded successfully!")

def predict_position(question):
    """
    Predict the position based on the input question
    """
    try:
        # Tokenize input
        inputs = tokenizer(question, return_tensors="pt", truncation=True, padding=True, max_length=128)
        
        # Get prediction
        with torch.no_grad():
            outputs = model(**inputs)
            predictions = torch.nn.functional.softmax(outputs.logits, dim=-1)
            predicted_class_id = predictions.argmax().item()
            confidence = predictions.max().item()
        
        # Decode prediction
        predicted_position = label_encoder.inverse_transform([predicted_class_id])[0]
        
        return f"⚽ Position: **{predicted_position}** (Confidence: {confidence:.2%})"
    
    except Exception as e:
        return f"❌ Error: {str(e)}"

# Create Gradio interface
demo = gr.Interface(
    fn=predict_position,
    inputs=gr.Textbox(
        label="Ask about a player's position",
        placeholder="Example: What position does Lionel Messi play?",
        lines=2
    ),
    outputs=gr.Textbox(label="Answer"),
    title="⚽ Sports AI - Football Position Predictor",
    description="Ask me about any football player's position! I'm trained on data from FIFA, transfers, and match statistics.",
    examples=[
        ["What position does Lionel Messi play?"],
        ["What position does Virgil van Dijk play?"],
        ["Tell me about Cristiano Ronaldo's position"],
        ["What position does Kevin De Bruyne play?"],
        ["What does Kylian Mbappé play as?"]
    ],
    theme=gr.themes.Soft()
)

if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=7860)
