## Importing libraries and files
import os
from dotenv import load_dotenv
from crewai_tools import Tool
from langchain_community.document_loaders import PyPDFLoader

load_dotenv()

## Creating search tool
search_tool = Tool(
    name="Internet Search",
    func=lambda query: f"Searching the web for: {query}",  # Placeholder for actual search
    description="Performs a web search using an external API."
)

## Creating custom PDF reader tool
class BloodTestReportTool(Tool):
    def __init__(self):
        super().__init__(
            name="Blood Test Report Reader",
            func=self.read_data_tool,
            description="Reads and extracts text from a PDF blood test report."
        )

    def read_data_tool(self, path: str = 'data/sample.pdf') -> str:
        """Tool to read data from a PDF file from a path

        Args:
            path (str, optional): Path of the PDF file. Defaults to 'data/sample.pdf'.

        Returns:
            str: Full Blood Test report file content
        """
        try:
            loader = PyPDFLoader(file_path=path)
            docs = loader.load()

            full_report = ""
            for data in docs:
                content = data.page_content
                # Remove extra whitespaces and format properly
                while "\n\n" in content:
                    content = content.replace("\n\n", "\n")
                full_report += content + "\n"
            return full_report
        except Exception as e:
            return f"Error reading PDF: {str(e)}"

## Creating Nutrition Analysis Tool
class NutritionTool(Tool):
    def __init__(self):
        super().__init__(
            name="Nutrition Analysis",
            func=self.analyze_nutrition_tool,
            description="Analyzes blood report data to provide nutrition recommendations."
        )

    def analyze_nutrition_tool(self, blood_report_data: str) -> str:
        # Basic implementation (can be expanded)
        return (
            f"Based on the blood report:\n"
            f"- Increase intake of vitamin D-rich foods (e.g., salmon, eggs).\n"
            f"- Consider a balanced Mediterranean diet.\n"
            f"- Recommended supplements: Omega-3, Vitamin B12."
        )

## Creating Exercise Planning Tool
class ExerciseTool(Tool):
    def __init__(self):
        super().__init__(
            name="Exercise Planning",
            func=self.create_exercise_plan_tool,
            description="Creates an exercise plan based on blood report data."
        )

    def create_exercise_plan_tool(self, blood_report_data: str) -> str:
        # Basic implementation (can be expanded)
        return (
            f"Exercise Plan based on blood report:\n"
            f"- Moderate cardio (30 min, 5x/week).\n"
            f"- Strength training (2x/week, focus on major muscle groups).\n"
            f"- Consult a physician if you have pre-existing conditions."
        )