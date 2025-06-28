## Importing libraries and files
from crewai import Task
from agents import doctor, verifier, nutritionist, exercise_specialist
from tools import search_tool, BloodTestReportTool, NutritionTool, ExerciseTool

## Creating a task to verify the blood report
verification = Task(
    description="Verify if the uploaded file at {file_path} is a valid blood test report. "
                "Check for medical terminology and structure.",
    expected_output="A confirmation that the file is a valid blood report or an explanation if it's not.",
    agent=verifier,
    tools=[BloodTestReportTool()],
    async_execution=False,
)

## Creating a task to help solve user's query
help_patients = Task(
    description="Analyze the blood test report at {file_path} and address the user's query: {query}. "
                "Provide evidence-based medical advice and identify any abnormalities.",
    expected_output="A detailed medical analysis with:\n"
                   "- Summary of key blood test findings\n"
                   "- Answers to the user's query\n"
                   "- Recommendations for further medical evaluation if needed",
    agent=doctor,
    tools=[BloodTestReportTool(), search_tool],
    async_execution=False,
)

## Creating a nutrition analysis task
nutrition_analysis = Task(
    description="Analyze the blood test report at {file_path} and provide nutrition recommendations. "
                "Address the user's query: {query} if relevant.",
    expected_output="A nutrition plan with:\n"
                   "- Dietary recommendations based on blood test results\n"
                   "- Suggested supplements if necessary\n"
                   "- References to scientific guidelines",
    agent=nutritionist,
    tools=[BloodTestReportTool(), NutritionTool()],
    async_execution=False,
)

## Creating an exercise planning task
exercise_planning = Task(
    description="Create an exercise plan based on the blood test report at {file_path}. "
                "Consider the user's query: {query} and ensure the plan is safe and tailored.",
    expected_output="An exercise plan with:\n"
                   "- Recommended exercises based on health status\n"
                   "- Safety precautions\n"
                   "- Progression timeline",
    agent=exercise_specialist,
    tools=[BloodTestReportTool(), ExerciseTool()],
    async_execution=False,
)