from pydantic import BaseModel

class LinkedIn(BaseModel):
    prefix: str
    label: str
    url: str

class Portfolio(BaseModel):
    intro: str
    content: str
    linkedin: LinkedIn

portfolio = Portfolio(
    intro = "Hi, my name is Wenyu.",
    content = "I'm an experienced software engineer with a Master of Computing (Advanced) from the Australian National University. \n\n" \
              "Beyond software engineering, I'm passionate about data analysis, education, and research. \n\n" \
              "Have a look around to learn more about my experience and work. \n\n",
    linkedin = LinkedIn(
        prefix = "You're also welcome to connect with me on",
        label = "LinkedIn",
        url = "https://www.linkedin.com/in/wenyu-dai/"
    )
)

