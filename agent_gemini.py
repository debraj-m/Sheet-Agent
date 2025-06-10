import pandas as pd
import google.generativeai as genai
import time

# Step 1: Configure Gemini
genai.configure(api_key="")  # Replace with your real key

# Step 2: Create model object
model = genai.GenerativeModel(model_name="models/gemini-1.5-pro-latest")  # ✅ Correct model name

# Step 3: Load Excel file
file_path = "questions.xlsx"  # Replace with your file path
df = pd.read_excel(file_path)

# Step 4: Loop through rows from index 21 (Row 22)
for i in range(21, len(df)):
    question = str(df.at[i, 'Pre-review Questionnaries'])
    suggestion = str(df.at[i, 'Suggestions']) if 'Suggestions' in df.columns else ""

    if pd.isna(question) or question.strip() == "":
        continue  # Skip empty rows

    prompt = f"""
You are answering a vendor due diligence questionnaire for a company like GitHub Copilot or Lovable — an AI SaaS company focused on developer productivity and user-friendly AI experiences.

Question: {question}
Suggestion: {suggestion}

Answer in this format:
1. Applicable (Yes/No)
2. Response (short and professional, addressing data security, privacy, auditability, and compliance when relevant)
"""

    try:
        response = model.generate_content(prompt)
        text = response.text.strip()

        if "Yes" in text[:20]:
            df.at[i, 'Applicability'] = "Yes"
        elif "No" in text[:20]:
            df.at[i, 'Applicability'] = "No"
        else:
            df.at[i, 'Applicability'] = "Yes"  # fallback

        df.at[i, 'Response'] = text

    except Exception as e:
        print(f"Error at row {i+1}: {e}")
        df.at[i, 'Applicability'] = "Error"
        df.at[i, 'Response'] = str(e)

    time.sleep(1.5)  # Respect rate limits

# Step 5: Save results
df.to_excel("answered_due_diligence.xlsx", index=False)
print("✅ Done. Output saved to 'answered_due_diligence.xlsx'")
