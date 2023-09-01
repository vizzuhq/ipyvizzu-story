---
csv_url: ./proglangs.csv
---

# Popularity of Programming Languages

What programming languages do data scientists use?

This was one of the questions in the
[State of Data Science Reports](https://www.anaconda.com/state-of-data-science-report-2022)
published by Anaconda between 2020 and 2022. This data story shows the answers
to this question.

<vizzu-player controller></vizzu-player>

<script type="module" src="./main.js"></script>

```python
import pandas as pd

from ipyvizzu import Data, Config, Style
from ipyvizzustory import Story, Slide, Step


# Create data object, read csv to data frame and add data frame to data object
data = Data()
df = pd.read_csv(
    "https://ipyvizzu-story.vizzuhq.com/latest/examples/proglangs/proglangs.csv",
    dtype={"Year": str},
)
data.add_df(df)


# Create story object, add data to it
story = Story(data=data)

# Set the size of the HTML element
# that appears within the notebook
story.set_size("100%", "600px")

# Switch on the tooltip that appears
# when the user hovers the mouse over a chart element
story.set_feature("tooltip", True)

# Set a handler that prevents showing specific elements
label_handler_method = (
    "if(event.data.text.split(' ')[0] < 5) event.preventDefault()"
)
story.add_event("plot-marker-label-draw", label_handler_method)


# Each slide here is a page in the final interactive story
# Add the first slide
slide1 = Slide(
    Step(
        Data.filter("record.Year == 2022"),
        Config(
            {
                "x": ["Popularity", "Value[%]"],
                "y": ["Language", "Year", "Lang_year"],
                "color": "Popularity",
                "label": "Value[%]",
                "align": "stretch",
                "title": "Use of programming languages by data scientists in 2022",
                "lightness": "Year",
                "legend": "color",
            }
        ),
        Style(
            {
                "logo": {"width": "5em"},
                "plot": {
                    "xAxis": {"title": {"color": "#00000000"}},
                    "paddingLeft": "2.5em",
                    "marker": {
                        "colorPalette": "#3DAE2BFF "
                        + "#00833EFF "
                        + "#00A19BFF "
                        + "#0075A9FF "
                        + "#003764FF",
                        "minLightness": 0,
                        "maxLightness": 0.4,
                    },
                },
                "fontSize": "0.8em",
            }
        ),
    )
)
# Add the slide to the story
story.add_slide(slide1)

slide2 = Slide(
    Step(
        Config(
            {
                "split": True,
                "align": "min",
                "title": "Python is always or frequently used by 58%",
            }
        ),
        Style({"plot": {"xAxis": {"label": {"color": "#00000000"}}}}),
    )
)
story.add_slide(slide2)

slide3 = Slide()
slide3.add_step(
    Step(
        Config({"split": False, "align": "stretch"}),
        Style({"plot": {"xAxis": {"label": {"color": "#999999FF"}}}}),
    )
)
slide3.add_step(
    Step(
        Data.filter(
            """
            (record.Popularity == 'Always' || record.Popularity == 'Frequently') 
            && record.Year == 2022
            """
        ),
        Config({"x": {"range": {"max": 100}}, "align": "min"}),
    )
)
slide3.add_step(
    Step(
        Config(
            {
                "sort": "byValue",
                "title": "Python & SQL are the most popular by a huge margin",
            }
        )
    )
)
story.add_slide(slide3)

slide4 = Slide()
slide4.add_step(
    Step(
        Config(
            {
                "sort": "none",
                "title": "Let's focus on the six languages with data since 2020",
            }
        )
    )
)
slide4.add_step(
    Step(
        Data.filter(
            """
            (record.Popularity == 'Always' || record.Popularity == 'Frequently') 
            && (record.Language == 'R' || 
            record.Language == 'Python' || 
            record.Language == 'JavaScript' || 
            record.Language == 'Java' || 
            record.Language == 'C#' || 
            record.Language == 'C/C++') 
            && record.Year == 2022
            """
        ),
    )
)
slide4.add_step(
    Step(
        Config(
            {
                "y": ["Lang_year", "Year"],
                "x": ["Popularity", "Language", "Value[%]"],
            }
        )
    )
)
story.add_slide(slide4)

slide5 = Slide()
slide5.add_step(
    Step(
        Data.filter(
            """
            (record.Popularity == 'Always' || record.Popularity == 'Frequently') 
            && (record.Language == 'R' || 
            record.Language == 'Python' || 
            record.Language == 'JavaScript' || 
            record.Language == 'Java' || 
            record.Language == 'C#' || 
            record.Language == 'C/C++') 
            && record.Year != 2020
            """
        ),
    )
)
slide5.add_step(
    Step(
        Data.filter(
            """
            (record.Popularity == 'Always' || record.Popularity == 'Frequently') 
            && (record.Language == 'R' || 
            record.Language == 'Python' || 
            record.Language == 'JavaScript' || 
            record.Language == 'Java' || 
            record.Language == 'C#' || 
            record.Language == 'C/C++')
            """
        ),
        Config(
            {
                "title": "C/C++, C#, Java and Javascript are gaining popularity"
            }
        ),
    )
)
story.add_slide(slide5)


# Play the created story!
story.play()
```
