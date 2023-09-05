#################################
# # IMPORTING RELEVANT MODULES
#################################

import pandas as pd
from ipyvizzu import Data, Config, Style
from ipyvizzustory import Story, Slide, Step
from streamlit.components.v1 import html
import streamlit as st

st.set_page_config(
    page_title="Annotation Demo",
    layout="wide"
)


#################################
# # Taking User Input
#################################
st.subheader(":blue[The Awesome Story]")

selection = 'industry_name'

#################################
# Starting Story - Program Type
#################################

select_data = {
    "year": {
        "0": "2019",
        "1": "2019",
        "2": "2019",
        "3": "2020",
        "4": "2020",
        "5": "2020",
        "6": "2020",
        "7": "2020",
        "8": "2020",
        "9": "2020"
    },
    "industry_name": {
        "0": "Industry1",
        "1": "Industry2",
        "2": "Industry3",
        "3": "Industry1",
        "4": "Industry2",
        "5": "Industry4",
        "6": "Industry5",
        "7": "Industry6",
        "8": "Industry7",
        "9": "Industry3"
    },
    "principal_amount": {
        "0": 10,
        "1": 20,
        "2": 50,
        "3": 120,
        "4": 110,
        "5": 20,
        "6": 80,
        "7": 60,
        "8": 90,
        "9": 200
    },
    "year_int": {
        "0": 2019,
        "1": 2019,
        "2": 2019,
        "3": 2020,
        "4": 2020,
        "5": 2020,
        "6": 2020,
        "7": 2020,
        "8": 2020,
        "9": 2020
    }
}
select_data = pd.DataFrame.from_dict(select_data)

# Create data object, read csv to data frame and add data frame to data object
example_data = Data()

example_data.add_data_frame(select_data)

# Set the style of the charts in the story
example_style = Style(
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
            "paddingTop": "1em",
            # "paddingBottom": "0em",
        },
        "logo": {"width": "0em"},
    }
)

# Create story object, add data and style settings to it
story = Story(data=example_data, style=example_style)

# Set the size of the HTML element
# story.set_size(600, 400)


# Add the first slide,

# Step 3 - zoom to data from the first and last years
range_min = "0"
range_max = "-0max"

slide1 = Slide(
    Step(
        # Only include rows where the Function value != Defense
        # Note, filters currently only accept JavaScript style filters,
        # hence the "!==", rather than "!="
        # Data.filter("record.year !== '2018' && record.year !== '2023'"),
        # Data.filter(filter),

        Config(
            {
                "channels": {
                    "y": {
                        "set": ["principal_amount", selection],
                        # Set the range of the y-axis
                        # to the min and max of the data being shown
                        # default value is 110% of the maximum value
                        "range": {"min": "0%", "max": "100%"},
                    },
                    # "x": {"set": ["year"]},

                    # filtering through range instead of filter so x axis looks clean
                    "x": {"set": ["year"], "range": {"min": range_min, "max": range_max}},

                    "color": selection,
                },
                # "title": "Stacked Trends",
                "geometry": "area",
                # "label": "principal_amount",
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
                "label": "principal_amount",
                # "title": "Split Graph",
            }
        )
    )
)

story.add_slide(slide2)

# Show share of components
slide3 = Slide(
    Step(
        Config(
            {
                "split": False,
                "align": "stretch",
                # "title": "Stacked 100%",
            }
        )
    )
)

story.add_slide(slide3)

#################################
# ### Creating Slides Annotation
#################################


# Splitting html: first part helps embed variable from Python
update_event_html1 = f"""
<script>

const vp = document.querySelector("vizzu-player");

selection = '{selection}'
"""

update_event_html2 = """
vp.addEventListener('update', (e) => {
    
    // Slide Annotation
    var slide_num = Number(`${e.detail.currentSlide}`)+1
    
    switch (selection){
        case 'industry_name':
            switch (slide_num) {
                case 1:
                    slide_title = 'Quick Look Through The Years'
                    slide_annotation = '<li>Great growth in 2020 over 2019</br></br></li>';
                    break;
                case 2:
                    slide_title = 'Split By Industry'
                    slide_annotation = '<li>All existing industries grew</br></br></li> <li>4 new industries sprung up</br></br></li>';
                    break;
                case 3:
                    slide_title = 'Contribution By Industry'
                    slide_annotation = '<li>Great increase in spread</br></br></li><li>Dependance on Top 3 industries down from less than 75%</br></br></li>';
                    break;
                default:
                    slide_title = ''
                    slide_annotation = '';
                }
            break;
        default:
            slide_title = '';
            slide_annotation = '';
    }
    
    // Embedding the html inside the inner HTML
    var elem = document.getElementById('slide-title');
    var html = elem.innerHTML;
    elem.innerHTML = ` <h3 style="color: #4a89d6;">${slide_title}</h3> <div style="color: #777777;font-size: 16px;"><ul>${slide_annotation}</ul></div>`;
});
</script>
"""

#################################
# ### Publishing Story
#################################

# Play the created story!
# story.play()

# Switch on the tooltip that appears
story.set_feature("tooltip", True)

# test width
# width = 300

# production width
width = 800
height = 500
story.set_size(width=width, height=height)

story_html = story.to_html()

update_event_html = update_event_html1 + update_event_html2

title_html = '<div id="slide-title"></div>'

container_html = f'''
    <div style="display:flex;justify-content:flex-end;">
        {story_html}
        <div style="background-color: #eff2f6; padding:20px;margin:0px; width:100%;">
        {title_html}
        </div>
    </div>
'''

html(
    container_html + update_event_html,
    height=height,
    )
