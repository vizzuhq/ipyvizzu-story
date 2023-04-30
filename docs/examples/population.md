---
csv_url: ./population.csv
---

# UN Population Forecast

In this example, we explore the population of Africa between 1953-2098. On top
of that, this story shows how to use the chart configuration presets. Check
[ipyvizzu - Chart presets chapter](https://ipyvizzu.vizzuhq.com/latest/tutorial/chart_presets/)
and
[ipyvizzu - Preset charts gallery](https://ipyvizzu.vizzuhq.com/latest/examples/presets/)
for more details on the available chart presets.

<vizzu-player controller></vizzu-player>

<script type="module" src="./main.js"></script>

```python
import pandas as pd

from ipyvizzu import Data, Config, Style
from ipyvizzustory import Story, Slide, Step


# Create data object, read csv to data frame and add data frame to data object
data = Data()
df = pd.read_csv(
    "https://ipyvizzu-story.vizzuhq.com/latest/examples/population/population.csv",
    dtype={"Year": str},
)
data.add_data_frame(df)


# Create story object, add data to it
story = Story(data=data)

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
        Data.filter("record.Continent == 'Africa'"),
        Config.stackedArea(
            {
                "x": "Year",
                "y": "Medium",
                "stackedBy": "Subregion",
                "title": "Population of Africa 1953-2098",
            }
        ),
        Style({"plot": {"xAxis": {"label": {"angle": 2.0}}}}),
    )
)
# Add the slide to the story
story.add_slide(slide1)

slide2 = Slide(
    Step(
        Config.percentageArea(
            {
                "x": "Year",
                "y": "Medium",
                "stackedBy": "Subregion",
            }
        ),
    )
)
story.add_slide(slide2)

slide3 = Slide(
    Step(
        Config.stream(
            {
                "x": "Year",
                "y": "Medium",
                "stackedBy": "Subregion",
            }
        ),
    )
)
story.add_slide(slide3)

slide4 = Slide(
    Step(
        Config.violin(
            {
                "x": "Year",
                "y": "Medium",
                "splittedBy": "Subregion",
            }
        ),
    )
)
story.add_slide(slide4)


# Play the created story!
story.play()
```
