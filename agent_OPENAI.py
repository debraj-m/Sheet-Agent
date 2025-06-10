import pandas as pd
import os
from openai import OpenAI
import time

# --- Config ---
openai_api_key = ""# Replace with your actual API key or set via env var
excel_path = "questions.xlsx"    # Update with your Excel file path
sheet_name = 0                   # Use sheet index or name
start_row = 21                   # Zero-indexed (row 22 in Excel)
q_col1 = "Pre-review Questionnaries"
q_col2 = "Suggestions"
applicable_col = "Applicable (Yes/No)"
response_col = "Response"

# --- OpenAI Client ---
client = OpenAI(api_key=openai_api_key)

# --- Load Data ---
df = pd.read_excel(excel_path, sheet_name=sheet_name)

# Ensure output columns exist and are string dtype
for col in [applicable_col, response_col]:
    if col not in df.columns:
        df[col] = ""
    else:
        df[col] = df[col].astype(str)

# --- Process Each Row ---
for i in range(start_row, len(df)):
    try:
        question1 = str(df.at[i, q_col1]).strip()
        question2 = str(df.at[i, q_col2]).strip()
        combined_q = f"Primary Question:\n{question1}\n\nAdditional Suggestion:\n{question2}"

        prompt = f"""
You are helping with vendor due diligence for a company like GitHub Copilot or Lovable — an AI SaaS tool for developer productivity and user-friendly AI experiences.

Below is a due diligence question and suggestion. Please answer the following:

1. In the column 'Applicable (Yes/No)', indicate if this question applies fully, partially, or not at all to such a company.
2. In the column 'Response', provide a professional, concise answer appropriate for vendor documentation. Prioritize data security, auditability, compliance, privacy, and user trust where relevant.

Here is the question and suggestion:
---
{combined_q}
---
"""

        response = client.chat.completions.create(
            model="gpt-4o",  # ✅ VALID and recommended,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.2
        )

        output = response.choices[0].message.content.strip()
        # Optionally split response if it's in format:
        # "Applicable: Yes\nResponse: ...", etc.
        if "Applicable:" in output and "Response:" in output:
            applicable_value = output.split("Applicable:")[1].split("Response:")[0].strip()
            response_value = output.split("Response:")[1].strip()
        else:
            applicable_value = "Check manually"
            response_value = output

        df.at[i, applicable_col] = applicable_value
        df.at[i, response_col] = response_value
        print(f"Processed row {i+1}")

        time.sleep(1.2)  # Respect rate limits

    except Exception as e:
        df.at[i, applicable_col] = "Error"
        df.at[i, response_col] = str(e)
        print(f"Error at row {i+1}: {e}")

# --- Save Result ---
output_path = "questions_filled.xlsx"
df.to_excel(output_path, index=False)
print(f"Completed. Saved to {output_path}")
