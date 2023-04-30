# Basic example

The below story shows a basic use case for `ipyvizzu-story`.

<vizzu-player controller></vizzu-player>

<script type="module" src="./main.js"></script>

```python
from ipyvizzu import Data, Config
from ipyvizzustory import Story, Slide, Step


# Create data object
data = Data()
data.add_series("Foo", ["Alice", "Bob", "Ted"])
data.add_series("Bar", [15, 32, 12])
data.add_series("Baz", [5, 3, 2])


# Create story object, add data to it
story = Story(data=data)


# Each slide here is a page in the final interactive story
# Add the first slide
slide1 = Slide(
    Step(
        Config({"x": "Foo", "y": "Bar"}),
    )
)
# Add the slide to the story
story.add_slide(slide1)

# Create the second slide
# Configs provided here are changes to the visualization
# created in the previous Step
slide2 = Slide(
    Step(
        Config({"color": "Foo", "x": "Baz", "geometry": "circle"}),
    )
)
story.add_slide(slide2)


# Play the created story!
story.play()
```
