---
csv_url: ./usbudget.csv
---

# US Federal R&D budget

US Federal R&D budget In this more involved example, we explore the history of
the US Federal R&D budget between 1955-2020. On top of the base functionality,
this story showcases:

- Styling the overall Story
- Setting the size of the Story
- Slides with multiple steps

<vizzu-player controller></vizzu-player>

<script type="module" src="./main.js"></script>

```python
import pandas as pd

from ipyvizzu import Data, Config, Style
from ipyvizzustory import Story, Slide, Step


# Create data object, read csv to data frame and add data frame to data object
data = Data()
df = pd.read_csv(
    "https://ipyvizzu-story.vizzuhq.com/latest/examples/usbudget/usbudget.csv",
    dtype={"Year": str},
)
data.add_df(df, units={"Amount": "B$"})


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
                "title": {"fontSize": "0.8em", "paddingTop": "2.5em"},
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


# Add the first slide,
# containing a single animation step that sets the initial chart
slide1 = Slide(
    Step(
        # Only include rows where the Function value != Defense
        # Note, filters currently only accept JavaScript style filters,
        # hence the "!==", rather than "!="
        Data.filter("record.Function !== 'Defense'"),
        Config(
            {
                "channels": {
                    "y": {
                        "set": ["Amount", "Function"],
                        # Set the range of the y-axis
                        # to the min and max of the data being shown
                        # default value is 110% of the maximum value
                        "range": {"min": "0%", "max": "100%"},
                    },
                    "x": {"set": ["Year"]},
                    "color": "Function",
                },
                "title": "Stacked Area Chart - U.S. R&D Budget in 1955-2020",
                "geometry": "area",
            }
        ),
    )
)
# Add the slide to the story
story.add_slide(slide1)

# Show components side-by-side
slide2 = Slide(
    Step(
        Config(
            {
                "split": True,
                "title": "Show Components Side by Side",
            }
        )
    )
)
story.add_slide(slide2)

# This slide contains multiple steps
# Note that the slide is created as an empty object,
# then steps are added to it one-by-one
slide3 = Slide()
# Step 1 - let's get back to the previous view
slide3.add_step(Step(Config({"split": False})))
# Step 2 - Add the defense function to the chart by removing it from the filter
slide3.add_step(
    Step(
        Data.filter(None),
        Config(
            {"title": "Add New Category While Keeping the Context"}
        ),
    )
)
# Add the multi-step slide to the story, just like any other slide
story.add_slide(slide3)

# Show share of components
slide4 = Slide(
    Step(
        Config(
            {
                "align": "stretch",
                "title": "Show Share of Components (%)",
            }
        )
    )
)
story.add_slide(slide4)

# Compare data from 1955 and 2020
slide5 = Slide()
# Step 1 - switch back to value instead of percentage
slide5.add_step(Step(Config({"align": "none"})))
# Step 2 - switch to a stacked column chart by changing the geometry
slide5.add_step(
    Step(
        Config(
            {
                "geometry": "rectangle",
            }
        )
    )
)
# Step 3 - zoom to data from the first and last years
slide5.add_step(
    Step(
        Data.filter(
            "record.Year === '1955' || record.Year === '2020' "
        ),
        Config(
            {
                "title": "Zoom to Specific Elements",
            }
        ),
    ),
)
story.add_slide(slide5)

# Group & rearrange elements for comparison
slide6 = Slide()
slide6.add_step(
    Step(
        Config(
            {
                "x": ["Year", "Function"],
                "y": "Amount",
                "label": "Amount",
                "title": "Group & Rearrange for Better Comparison",
            }
        )
    )
)

slide6.add_step(Step(Config({"x": ["Function", "Year"]})))
story.add_slide(slide6)


# Switch on the tooltip that appears
# when the user hovers the mouse over a chart element
story.set_feature("tooltip", True)


# Set a handler that prevents showing the year values that are not divisible by 5
handler = """
let Year = parseFloat(event.data.text);
if (!isNaN(Year) && Year > 1950 && Year < 2020 && Year % 5 !== 0) {
    event.preventDefault();
}
"""
# Add handler to the plot-axis-label-draw event so that it takes effect
story.add_event("plot-axis-label-draw", handler)


# If you want to save the story as an interactive HTML
# (containing only the output of the previous cell),
# use the following command:
# story.export_to_html(filename="mystory.html")


# Play the created story!
story.play()
```
