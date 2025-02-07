# Advanced-ATS-Analyzer

## Objective
The **Advanced ATS Analyzer** is an AI-powered tool designed to analyze resumes against job descriptions. By leveraging OpenAI's language models, this system evaluates a candidate's qualifications, skills, and experience based on the requirements outlined in a job description. The tool provides structured feedback to improve resumes, helping candidates tailor their profiles to match job opportunities more effectively.

## Features
- **Job Description and Resume Upload**: Users can input a job description and upload a PDF resume for analysis.
- **AI-powered Resume Evaluation**: The tool uses advanced AI models to analyze resumes against job descriptions based on technical skills, experience, education, and certifications.
- **Model Selection**: Choose between different OpenAI models (GPT-3.5, GPT-4, and GPT-4 Turbo) to customize the analysis.
- **Temperature Control**: Adjust the creativity and response style with a temperature slider to generate more or less creative results.
- **Downloadable Report**: After analysis, users can download a structured JSON report with the analysis results and suggested improvements.
- **Clear Feedback**: Detailed evaluation of the resume with missing keywords, improvement suggestions, and match percentage.

## Tech Stack
- **Streamlit**: For building the interactive web application.
- **OpenAI API**: For generating responses based on the provided resume and job description using GPT models.
- **PyPDF2**: For extracting text from PDF resumes.
- **dotenv**: For managing environment variables like OpenAI API keys.
- **JSON**: For structuring and returning analysis results.

## Implementation

### 1. **Model Selection and Fine-tuning**
   - The tool utilizes OpenAI's language models (GPT-3.5 and GPT-4) to analyze the resume against the provided job description.
   - The fine-tuning capability allows customization to improve ATS performance based on example inputs and outputs.

### 2. **Resume Analysis**
   - Users can upload their resumes in PDF format.
   - The **input_pdf_text** function extracts text from the uploaded resume, which is then passed to the model for analysis.
   - The **get_gpt_response** function is used to call the OpenAI API and generate an evaluation based on the provided job description and extracted resume text.

### 3. **User Interface**
   - Streamlit is used to create a clean and user-friendly interface where users can input job descriptions, upload resumes, and analyze them with ease.
   - The app allows the selection of different models and adjusts the response creativity with a temperature slider.

### 4. **JSON Response**
   - After the analysis, the tool returns a structured response in JSON format, including:
     - **JD Match**: Percentage match between the job description and the resume.
     - **Technical Skills**: Lists of matching and missing skills.
     - **Experience Match**: Evaluation of relevant experience, including years and relevance.
     - **Missing Keywords**: Keywords that should be added to the resume.
     - **Improvement Suggestions**: Suggestions for resume optimization.

### 5. **Download Report**
   - After the analysis is complete, the user can download a detailed analysis report in JSON format, which includes all feedback and suggestions.

## Conclusion
The **Advanced ATS Analyzer** helps job seekers optimize their resumes to meet the specific requirements of job descriptions. By leveraging AI, the tool evaluates key aspects such as technical skills, experience, and certifications. It provides actionable insights to improve resumes, ensuring better chances of passing ATS filters and making a strong impression on recruiters.
