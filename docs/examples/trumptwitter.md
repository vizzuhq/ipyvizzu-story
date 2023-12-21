---
csv_url: ./trumptwitter.csv
---

# Trump Twitter Tirade

<vizzu-player controller></vizzu-player>

<script type="module" src="./main.js"></script>

```python
import math
import pandas as pd

from ipyvizzu import Data, Config, Style
from ipyvizzustory import Story, Slide, Step


# Create data object, read csv to data frame and add data frame to data object
data = Data()
df = pd.read_csv(
    "https://ipyvizzu-story.vizzuhq.com/latest/examples/trumptwitter/trumptwitter.csv",
)
data.add_df(df)


# Set the style of the charts in the story
style = Style(
    {
        "tooltip": {"fontSize": "22px"},
        "title": {"paddingTop": "1.2em", "fontSize": "2.5em"},
        "legend": {"label": {"fontSize": "1.8em"}, "width": "16em"},
        "logo": {"width": "6em"},
        "plot": {
            "marker": {"label": {"fontSize": "1.5em"}},
            "yAxis": {
                "label": {
                    "fontSize": "1.5em",
                },
                "title": {"color": "#ffffff00"},
                "interlacing": {"color": "#ffffff00"},
            },
            "xAxis": {
                "label": {
                    "fontSize": "1.6em",
                    "paddingTop": "1em",
                },
                "title": {"fontSize": "1.4em", "paddingTop": "2.5em"},
            },
        },
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
        Data.filter(
            "record.Firsttweet === 'Yes' && record.Dummy === 'No'"
        ),
        Config(
            {
                "channels": {
                    "y": {
                        "set": ["tweets"],
                    },
                    "x": {"set": ["Period", "year", "month"]},
                    "color": "Period",
                },
                "title": "Trump started tweeting in May '09",
            }
        ),
    )
)
# Add the slide to the story
story.add_slide(slide1)

slide2 = Slide(
    Step(
        Data.filter(
            "record.Period === 'New to Twitter' && record.Dummy === 'No'"
        ),
        Config(
            {
                "title": "In the first two years he wasn't very active",
            }
        ),
    )
)
story.add_slide(slide2)

slide3 = Slide(
    Step(
        Data.filter(
            """
            (record.Period === 'New to Twitter' || record.Period === 'Businessman')
            && record.Dummy === 'No'
            """
        ),
        Config(
            {
                "title": "Then he got hooked on",
            }
        ),
    )
)
story.add_slide(slide3)

slide4 = Slide(
    Step(
        Data.filter(
            """
            (record.Period === 'New to Twitter' || 
            record.Period === 'Businessman' || 
            record.Period === 'Nominee')
            && record.Dummy === 'No'
            """
        ),
        Config(
            {
                "title": "Interesting trend after becoming a presidential nominee",
            }
        ),
    )
)
story.add_slide(slide4)

slide5 = Slide(
    Step(
        Data.filter("record.Dummy === 'No'"),
        Config(
            {
                "title": "And after he became President",
            }
        ),
    )
)
story.add_slide(slide5)

slide6 = Slide()
slide6.add_step(
    Step(
        Config({"geometry": "area", "align": "center"}),
    )
)
slide6.add_step(
    Step(
        Config(
            {
                "title": "All of Trump's tweets until May 2020",
            }
        ),
    )
)
story.add_slide(slide6)

slide7 = Slide(
    Step(
        Config(
            {
                "y": "retweetcount",
                "title": "And the number of times these were retweeted",
            }
        ),
    )
)
story.add_slide(slide7)

slide8 = Slide()
slide8.add_step(
    Step(
        Config(
            {
                "y": "tweets",
                "title": "Let's focus on the number of tweets for now",
            }
        ),
    )
),
slide8.add_step(
    Step(
        Config(
            {
                "x": {"set": ["year", "month"]},
                "color": None,
            }
        )
    )
)
story.add_slide(slide8)

slide9 = Slide(
    Step(
        Config(
            {
                "y": ["tweets", "Type"],
                "color": "Type",
                "title": "Original tweets, retweets & replies sent",
            }
        ),
        Style(
            {
                "plot": {
                    "marker": {
                        "colorPalette": "#A0CDEBFF #60C0E6FF #1DA1F3FF"
                    }
                }
            },
        ),
    )
)
story.add_slide(slide9)

slide10 = Slide(
    Step(
        Config({"split": True, "align": "none"}),
        Style({"plot": {"yAxis": {"label": {"color": "#ffffff00"}}}}),
    )
)
story.add_slide(slide10)

slide11 = Slide(
    Step(
        Config(
            {
                "split": False,
                "align": "stretch",
                "title": "Original tweets, retweets & replies sent (%)",
            }
        ),
        Style({"plot": {"yAxis": {"label": {"color": "#999999ff"}}}}),
    )
)
story.add_slide(slide11)

slide12 = Slide()
slide12.add_step(
    Step(
        Config(
            {
                "align": "center",
                "title": "",
            }
        ),
    )
)
slide12.add_step(
    Step(
        Config({"y": "tweets", "color": None, "legend": "lightness"}),
        Style(
            {"plot": {"marker": {"colorPalette": "null"}}},
        ),
    )
)
slide12.add_step(
    Step(
        Config(
            {
                "y": ["tweets", "Tool"],
                "color": "Tool",
                "title": "Tools Trump Used to Tweet",
                "legend": "color",
            }
        ),
        Style(
            {
                "plot": {
                    "marker": {
                        "colorPalette": "#597696FF #ED2828FF #26EC87FF #29B9BFFF "
                    }
                }
            },
        ),
    )
)
story.add_slide(slide12)

slide13 = Slide(
    Step(
        Config({"split": True, "align": "none"}),
        Style({"plot": {"yAxis": {"label": {"color": "#ffffff00"}}}}),
    )
)
story.add_slide(slide13)

slide14 = Slide()
slide14.add_step(
    Step(
        Config(
            {
                "geometry": "rectangle",
            }
        ),
    )
)
slide14.add_step(
    Step(
        Config(
            {
                "x": ["tweets", "year", "month"],
                "y": "Tool",
                "geometry": "rectangle",
                "split": False,
                "align": "none",
            }
        ),
        Style(
            {
                "plot": {
                    "xAxis": {"title": {"color": "#ffffff00"}},
                    "yAxis": {"label": {"color": "#999999ff"}},
                }
            },
        ),
    )
)
slide14.add_step(
    Step(
        Config(
            {
                "x": "tweets",
                "label": "tweets",
            }
        ),
    )
)
story.add_slide(slide14)

slide15 = Slide()
slide15.add_step(
    Step(
        Config(
            {
                "x": ["tweets", "AMPM", "hour12"],
                "label": None,
            }
        ),
    )
)
slide15.add_step(
    Step(
        Config(
            {
                "y": ["tweets", "Tool"],
                "x": ["AMPM", "hour12"],
                "align": "max",
            }
        ),
    )
)
slide15.add_step(
    Step(
        Config(
            {
                "geometry": "area",
            }
        ),
    )
)
slide15.add_step(
    Step(
        Config(
            {
                "coordSystem": "polar",
                "angle": math.pi,
                "title": "Time of Day When Trump Tweeted",
            }
        ),
        Style(
            {
                "plot": {
                    "yAxis": {"label": {"color": "#ffffff00"}},
                    "xAxis": {
                        "label": {
                            "fontSize": "2em",
                            "paddingBottom": "2.5em",
                            "paddingTop": "2.5em",
                            "paddingLeft": "2.5em",
                            "paddingRight": "2.5em",
                        }
                    },
                }
            }
        ),
    )
)
story.add_slide(slide15)

slide16 = Slide(
    Step(
        Config(
            {
                "y": ["Businessman", "Tool"],
                "title": "Times Trump Tweeted When Being a Businessman",
            }
        ),
    )
)
story.add_slide(slide16)

slide17 = Slide(
    Step(
        Config(
            {
                "y": ["President", "Tool"],
                "title": "Times Trump Tweeted When Being President",
            }
        ),
    )
)
story.add_slide(slide17)


# Play the created story!
story.play()
```
