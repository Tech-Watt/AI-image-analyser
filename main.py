import streamlit as st 
import os 
from dotenv import load_dotenv
import base64
from openai import OpenAI


load_dotenv()
key = os.getenv('OPENAI_API_KEY')
MODEL = 'gpt-4o'
client = OpenAI(api_key = key)

def encode_image(image):
    return base64.b64encode(image.read()).decode('utf-8')

st.title('Image Analyzer')
image_file = st.file_uploader('Upload an image file',type = ['png', 'jpg', 'jpeg'])
if image_file:
    st.image(image_file,caption = 'Uploaded image',use_column_width =True)

    base64_image = encode_image(image_file)

    response = client.chat.completions.create(
        model = MODEL,
    messages=[
        {"role": "system", "content": "You are a helpful  assistant that responds in Markdown."},
        {"role": "user", "content": [
        {"type": "text", "text": "Could you describe the image and create a report to highlight important details and provide recommendations. Create a report with Observations, important details, and Recommendations with bullet points."},
            {"type": "image_url", "image_url": {
            "url": f"data:image/png;base64,{base64_image}"}
                    }
                ]}
            ],
            temperature=0.0,
        )
    
    st.markdown(response.choices[0].message.content)