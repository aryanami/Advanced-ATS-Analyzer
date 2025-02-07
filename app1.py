import streamlit as st
import json
import openai
import os
import PyPDF2 as pdf
from dotenv import load_dotenv
from openai import OpenAIError

load_dotenv() 

client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
# Model selection options
AVAILABLE_MODELS = {
    "GPT-3.5 Turbo": "gpt-3.5-turbo",
    "GPT-4": "gpt-4",
    "GPT-4 Turbo": "gpt-4-turbo-preview"
}

def get_gpt_response(input_prompt, model="gpt-4-turbo-preview", temperature=0.7):
    try:
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": "You are an expert ATS system analyzer specializing in tech industry resume evaluation."},
                {"role": "user", "content": input_prompt}
            ],
            max_tokens=1000,
            temperature=temperature,
            presence_penalty=0.1,
            frequency_penalty=0.1
        )
        return response.choices[0].message.content.strip()   # Ensure valid JSON output
    except OpenAIError as e:
        return {"error": f"OpenAI API error: {str(e)}"}  # Return a JSON error response
    except json.JSONDecodeError:
        return {"error": "Invalid JSON response from API"}  # Catch JSON parsing issues
    except Exception as e:
        return {"error": f"Unexpected error: {str(e)}"}

# Fine-tuning related functions
def prepare_training_data(examples):
    """Prepare data for fine-tuning"""
    return [
        {
            "messages": [
                {"role": "system", "content": "You are an expert ATS system analyzer."},
                {"role": "user", "content": example["input"]},
                {"role": "assistant", "content": example["output"]}
            ]
        }
        for example in examples
    ]

def fine_tune_model(training_data, model="gpt-3.5-turbo"):
    """Initialize fine-tuning job"""
    try:
        # Create fine-tuning job
        response = openai.FineTuningJob.create(
            training_file=training_data,
            model=model,
            hyperparameters={
                "n_epochs": 3
            }
        )
        return response
    except Exception as e:
        return f"Fine-tuning error: {str(e)}"

#Reading the pdf and extracting text from the pdf

def input_pdf_text(uploaded_file):
    reader=pdf.PdfReader(uploaded_file)
    text=""
    for page in range(len(reader.pages)):
        page=reader.pages[page]
        text+=str(page.extract_text())
    return text

# Enhanced prompt template
input_prompt="""
Analyze the following resume against the job description with these specific requirements:

1. Technical Skills Match:
   - Core technical skills alignment
   - Programming languages match
   - Tools and frameworks expertise

2. Experience Evaluation:
   - Years of relevant experience
   - Project relevance
   - Industry-specific experience

3. Education and Certifications:
   - Required qualifications match
   - Relevant certifications

4. Detailed Feedback:
   - Specific missing keywords
   - Suggested improvements
   - Format and presentation feedback

Resume: {text}
Job Description: {jd}

Provide a structured response in JSON format:
{{
    "JD Match": "percentage",
    "Technical Skills": {{
        "Matching": [],
        "Missing": []
    }},
    "Experience Match": {{
        "Years": "evaluation",
        "Relevance": "analysis"
    }},
    "MissingKeywords": [],
    "Profile Summary": "",
    "Improvement Suggestions": []
}}
"""

## Streamlit app with enhanced UI
st.title("Advanced ATS Analyzer")
st.text("AI-Powered Resume Analysis and Optimization")

# Model selection
selected_model = st.sidebar.selectbox(
    "Select GPT Model",
    list(AVAILABLE_MODELS.keys())
)

# Temperature slider
temperature = st.sidebar.slider(
    "Response Creativity (Temperature)",
    min_value=0.0,
    max_value=1.0,
    value=0.7,
    step=0.1
)

st.header("Step 1: Job Description")
jd = st.text_area("Paste the Job Description")

st.header("Step 2: Upload Your Resume")
uploaded_file = st.file_uploader("Upload Your Resume", type="pdf", help="Please upload the pdf")

submit = st.button("Analyze Resume")

if submit:
    if uploaded_file is not None:
        with st.spinner('Analyzing your resume...'):
            text = input_pdf_text(uploaded_file)
            if text and jd:
                response = get_gpt_response(
                    input_prompt,
                    model=AVAILABLE_MODELS[selected_model],
                    temperature=temperature
                )
                st.subheader("Analysis Results")
                st.json(response)  # Better formatting for JSON response
                st.download_button(
                    "Download Analysis",
                    response,
                    file_name="Resume_Analysis.json"
                )
            else:
                st.error("Please ensure both the resume and job description are provided.")
