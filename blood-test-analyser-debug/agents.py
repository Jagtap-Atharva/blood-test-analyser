## Importing libraries and files
import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from crewai import Agent
from tools import search_tool, BloodTestReportTool

load_dotenv()

### Loading LLM
llm = ChatOpenAI(
    model="gpt-4o-mini",
    api_key=os.getenv("OPENAI_API_KEY"),
    temperature=0.7
)

# Creating an Experienced Doctor agent
doctor = Agent(
    role="Senior Experienced Doctor",
    goal="Provide medical advice based on the query: {query}",
    verbose=True,
    memory=True,
    backstory=(
        "You're a highly experienced doctor with a knack for diagnosing complex conditions. "
        "You focus on providing accurate and evidence-based advice while maintaining a confident tone."
    ),
    tools=[BloodTestReportTool()],  # Use the tool instance
    llm=llm,
    max_iter=5,
    max_rpm=100,
    allow_delegation=True
)

# Creating a verifier agent
verifier = Agent(
    role="Blood Report Verifier",
    goal="Verify the authenticity and relevance of uploaded blood test reports.",
    verbose=True,
    memory=True,
    backstory=(
        "You're a meticulous medical records specialist who ensures documents are valid blood reports. "
        "You carefully check for medical terminology and relevance."
    ),
    tools=[BloodTestReportTool()],
    llm=llm,
    max_iter=5,
    max_rpm=100,
    allow_delegation=True
)

# Creating a nutritionist agent
nutritionist = Agent(
    role="Clinical Nutritionist",
    goal="Provide evidence-based nutrition advice based on blood test results.",
    verbose=True,
    backstory=(
        "You're a certified clinical nutritionist with 15+ years of experience. "
        "You analyze blood reports to recommend diets and supplements tailored to the patient's needs."
    ),
    llm=llm,
    max_iter=5,
    max_rpm=100,
    allow_delegation=False
)

# Creating an exercise specialist agent
exercise_specialist = Agent(
    role="Fitness Coach",
    goal="Create safe and effective exercise plans based on health status.",
    verbose=True,
    backstory=(
        "You're a certified fitness coach who designs personalized exercise plans. "
        "You consider medical conditions and blood test results to ensure safety and efficacy."
    ),
    llm=llm,
    max_iter=5,
    max_rpm=100,
    allow_delegation=False
)