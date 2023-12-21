---
csv_url: ./linkedinpoll.csv
---

# Presentation Poll Results

In August, 2022, we asked data scientists in 5 LinkedIn groups about how often
they have to present the results of their analysis to business stakeholders.
This is a data story about the results of that poll.

<vizzu-player controller></vizzu-player>

<script type="module" src="./main.js"></script>

```python
import pandas as pd

from ipyvizzu import Data, Config, Style
from ipyvizzustory import Story, Slide, Step


# Create data object, read csv to data frame and add data frame to data object
data = Data()
df = pd.read_csv(
    "https://ipyvizzu-story.vizzuhq.com/latest/examples/linkedinpoll/linkedinpoll.csv",
    dtype={"Year": str},
)
data.add_df(
    df, units={"Answer percentage": "%", "Vote percentage": "%"}
)

# Create story object, add data to it
story = Story(data=data)

# Set the size of the HTML element
# that appears within the notebook
story.set_size("100%", "450px")


# Each slide here is a page in the final interactive story
# Add the first slide
slide1 = Slide(
    Step(
        Style(
            {
                "legend": {
                    "label": {"fontSize": "1.1em"},
                    "paddingRight": "-1em",
                },
                "plot": {
                    "marker": {"label": {"fontSize": "1.1em"}},
                    "paddingLeft": "10em",
                    "xAxis": {
                        "title": {"color": "#00000000"},
                        "label": {"fontSize": "1.1em"},
                    },
                    "yAxis": {"label": {"fontSize": "1.1em"}},
                },
                "logo": {"width": "6em"},
                "fontSize": "0.8em",
            }
        ),
        Config(
            {
                "x": {"set": ["Vote percentage", "Answer"]},
                "y": "Group number",
                "color": "Answer",
                "label": "Vote percentage",
                "title": "How often do you present "
                + "your findings to business stakeholders?",
            }
        ),
    )
)
# Add the slide to the story
story.add_slide(slide1)

slide2 = Slide(
    Step(
        Style({"plot": {"xAxis": {"label": {"color": "#00000000"}}}}),
        Config(
            {
                "split": True,
                "title": "2 or more is the most popular answer in every group",
            }
        ),
    )
)
story.add_slide(slide2)

slide3 = Slide(
    Step(
        Style(
            {
                "plot": {
                    "marker": {"label": {"fontSize": "0.916667em"}}
                }
            }
        ),
        Config(
            {
                "x": {"set": ["Vote count", "Answer"]},
                "label": "Vote count",
                "title": "61% of the votes came from one group",
            }
        ),
    )
)
story.add_slide(slide3)

slide4 = Slide()
slide4.add_step(
    Step(
        Style({"plot": {"yAxis": {"title": {"color": "#00000000"}}}}),
        Config(
            {
                "x": "Answer",
                "y": ["Group number", "Vote count"],
                "split": False,
                "legend": "color",
            }
        ),
    )
)
slide4.add_step(
    Step(
        Style({"plot": {"marker": {"label": {"fontSize": "1.1em"}}}}),
        Config(
            {"y": "Vote count", "title": "More than 700 people voted"}
        ),
    )
)
story.add_slide(slide4)

slide5 = Slide()
slide5.add_step(
    Step(
        Config(
            {
                "x": ["Answer percentage", "Answer"],
                "y": None,
                "label": "Answer percentage",
            }
        )
    )
)
slide5.add_step(
    Step(
        Style({"plot": {"xAxis": {"label": {"color": "#00000000"}}}}),
        Config(
            {
                "coordSystem": "polar",
                "title": "More than two-third of respondents present "
                + "at least once per month",
            }
        ),
    )
)
story.add_slide(slide5)


# Play the created story!
story.play()
```

- [Group 1](https://www.linkedin.com/groups/1859449/): AI & ML - Analytics ,
  Data Science . SAP BI/ Analytics Cloud /Tableau /Power BI /Birst

- [Group 2](https://www.linkedin.com/groups/4376214/): Artificial Intelligence,
  Digital Transformation Data Science, Automation, Machine Learning Analytics

- [Group 3](https://www.linkedin.com/groups/6773411/): Data Scientist, Data
  Analyst and Data Engineer

- [Group 4](https://www.linkedin.com/groups/25827/): Python Developers Community
  (moderated)

- [Group 5](https://www.linkedin.com/groups/2064830/): Data Analytics, Data
  Science, Business Analytics, Business Intelligence, Data Scientist & Analyst
