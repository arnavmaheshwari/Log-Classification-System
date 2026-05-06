from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
import os
import re


load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")


def classify_with_llm(log_msg):
    """
    Generate a variant of the input sentence. For example,
    If input sentence is "User session timed out unexpectedly, user ID: 9250.",
    variant would be "Session timed out for user 9251"
    """
    prompt = f'''Classify the log message into one of these categories: 
    Workflow Error and Deprecation Warning.
    If you can't figure out a category, use "Unclassified".
    Put the category inside <category> </category> tags. 
    Log message: {log_msg}'''

    llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash-lite",
    temperature=0.5,
    api_key=GEMINI_API_KEY
)

    content = llm.invoke(prompt)
    match = re.search(r'<category>(.*)<\/category>', content.content, flags=re.DOTALL)
    category = "Unclassified"
    if match:
        category = match.group(1)

    return category


if __name__ == "__main__":
    print(classify_with_llm(
        "Case escalation for ticket ID 7324 failed because the assigned support agent is no longer active."))
    print(classify_with_llm(
        "The 'ReportGenerator' module will be retired in version 4.0. Please migrate to the 'AdvancedAnalyticsSuite' by Dec 2025"))
    print(classify_with_llm("System reboot initiated by user 12345."))