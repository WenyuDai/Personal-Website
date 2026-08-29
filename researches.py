from pydantic import BaseModel

class Research(BaseModel):
    projectName: str
    startTime: str
    endTime: str
    location: str
    bullets: list[str]

researches = [
    Research(
        projectName = "Capstone Project: LLM Representation of SES in Educational Data",
        startTime = "July 2025",
        endTime = "Present",
        location = "AUSTRALIAN NATIONAL UNIVERSITY",
        bullets = [
            "Analysed multi-country PISA 2018 student-level data using Python (pandas, numpy, scikit-learn, PyTorch, Hugging Face Transformers) to investigate socioeconomic-status (SES) representation in large language model (LLM) outputs and internal activations, applying AI interpretability techniques to identify bias patterns.",
            "Produced analysis-ready tables, statistical summaries, correlation results, heatmaps, and visualisations to identify and communicate trends and patterns across countries, models, and prompt variants.",
            "Documented methodology, assumptions, data quality considerations, and findings in a formal research report and academic poster."
        ]
    )
]