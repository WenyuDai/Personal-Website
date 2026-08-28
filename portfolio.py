from pydantic import BaseModel

class Portfolio(BaseModel):
    intro: str
    content: str

portfolio = Portfolio(
    intro = "Hi, my name is Wenyu.",
    content = "I'm an experienced software engineer with a Master of Computing (Advanced) from the Australian National University. \n\n" \
              "Beyond software engineering, I'm passionate about data analysis, education, and research. \n\n" \
              "Have a look around to learn more about my experience and work."
)