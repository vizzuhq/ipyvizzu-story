---
csv_url: ./titanic.csv
---

# Passengers of the Titanic

<vizzu-player controller></vizzu-player>

<script type="module" src="./main.js"></script>

```python
import pandas as pd

from ipyvizzu import Data, Config, Style
from ipyvizzustory import Story, Slide, Step


# Create data object, read csv to data frame and add data frame to data object
data = Data()
df = pd.read_csv(
    "https://ipyvizzu-story.vizzuhq.com/latest/examples/titanic/titanic.csv",
    dtype={"Pclass": str},
)

df.loc[df["Age"].between(0, 20, "both"), "Age_group"] = "20-"
df.loc[df["Age"].between(20, 30, "right"), "Age_group"] = "20-30"
df.loc[df["Age"].between(30, 40, "right"), "Age_group"] = "30-40"
df.loc[df["Age"].between(40, 50, "right"), "Age_group"] = "40-50"
df.loc[df["Age"].between(50, 60, "right"), "Age_group"] = "50-60"
df.loc[df["Age"].between(60, 100, "right"), "Age_group"] = "60+"
df["Age_group"] = df["Age_group"].fillna("NaN")

# Prepare to sort the dataframe by salary list
agegroupsorter = [
    "20-",
    "20-30",
    "30-40",
    "40-50",
    "50-60",
    "60+",
    "NaN",
]

# Create the dictionary that defines the order for sorting
sorterIndex = dict(zip(agegroupsorter, range(len(agegroupsorter))))

# Generate a rank column that will be used to sort
# the dataframe numerically
df["Age_group_rank"] = df["Age_group"].map(sorterIndex)
df.sort_values(["Age_group_rank"], inplace=True)

data.add_df(df)


# Set the style of the charts in the story
style = Style(
    {
        "plot": {
            "yAxis": {
                "label": {
                    "fontSize": "1em",
                    "paddingRight": "1.2em",
                },
                "title": {"color": "#ffffff00"},
            },
            "xAxis": {
                "label": {
                    "angle": "2.5",
                    "fontSize": "1.1em",
                    "paddingRight": "0em",
                    "paddingTop": "1em",
                },
                "title": {"fontSize": "1em", "paddingTop": "2.5em"},
            },
        },
        "logo": {"width": "5em"},
    }
)

# Create story object, add data and style settings to it
story = Story(data=data, style=style)

# Set the size of the HTML element
# that appears within the notebook
story.set_size("100%", "400px")

# Switch on the tooltip that appears
# when the user hovers the mouse over a chart element
story.set_feature("tooltip", True)


# Each slide here is a page in the final interactive story
# Add the first slide
slide1 = Slide(
    Step(
        Config.bar(
            {"x": "Count", "title": "Passengers of the Titanic"}
        ),
    )
)
# Add the slide to the story
story.add_slide(slide1)

slide2 = Slide()
slide2.add_step(
    Step(
        Config.stackedBar({"x": "Count", "stackedBy": "Sex"}),
    )
)
slide2.add_step(
    Step(
        Config.groupedBar(
            {
                "x": "Count",
                "y": "Sex",
                "groupedBy": "Sex",
                "legend": "color",
                "title": "Rougly one-third of the passengers were ladies",
            }
        ),
    )
)
story.add_slide(slide2)

slide3 = Slide()
slide3.add_step(
    Step(
        Config(
            {
                "x": ["Count", "Survived"],
                "y": "Sex",
                "color": "Sex",
                "lightness": "Survived",
                "label": ["Survived", "Count"],
            }
        ),
    )
)
slide3.add_step(
    Step(
        Config(
            {
                "align": "stretch",
                "title": "Much more women survived than men",
            }
        ),
    )
)
story.add_slide(slide3)

slide4 = Slide()
slide4.add_step(
    Step(
        Config(
            {
                "x": "Count",
                "align": "none",
                "label": None,
                "lightness": None,
                "title": "Let's add the age of the passengers to the mix",
            }
        ),
    )
)
slide4.add_step(
    Step(
        Config(
            {
                "y": ["Count", "Sex"],
                "x": "Age_group",
                "label": "Count",
            }
        ),
    )
)
story.add_slide(slide4)

slide5 = Slide()
slide5.add_step(
    Step(
        Config(
            {
                "label": None,
                "title": "Let's see how many people survived/died "
                + "in these age groups",
            }
        ),
    )
)
slide5.add_step(
    Step(
        Config(
            {
                "y": ["Count", "Sex", "Survived"],
                "lightness": "Survived",
                "legend": "lightness",
            }
        ),
    )
)
slide5.add_step(
    Step(
        Config(
            {
                "y": ["Count", "Survived", "Sex"],
            }
        ),
    )
)
story.add_slide(slide5)

slide6 = Slide(
    Step(
        Config(
            {
                "align": "stretch",
                "title": "Survival rate varies a bit between age groups",
            }
        ),
    )
)
story.add_slide(slide6)

slide7 = Slide(
    Step(
        Data.filter("record.Sex == 'male'"),
        Config(
            {
                "title": "But again shows a very different picture for men..."
            }
        ),
    )
)
story.add_slide(slide7)

slide8 = Slide()
slide8.add_step(Step(Data.filter(None)))
slide8.add_step(
    Step(
        Data.filter("record.Sex == 'female'"),
        Config({"title": "...and women"}),
    )
)
story.add_slide(slide8)


# Play the created story!
story.play()
```
