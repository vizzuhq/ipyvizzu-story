
Build, present and share animated data stories in `Jupyter Notebook` and similar environments.

`ipyvizzu-story` package consists of two main parts:

* [Storylib][ipyvizzustory.storylib]: environment independent modules
* [Env][ipyvizzustory.env]: environment dependent modules

`ipyvizzu-story` package tries to figure out the environment and import the correct type of `Story`,
however `Story` could be imported with full path.

`ipyvizzu-story` package imports the following objects in `__init__.py`:


* `Story` from [Env.py.story][ipyvizzustory.env.py.story] or
    [Env.ipy.story][ipyvizzustory.env.ipy.story] or
    [Env.st.story][ipyvizzustory.env.st.story]
* [Step][ipyvizzustory.storylib.story.Step]
* [Slide][ipyvizzustory.storylib.story.Slide]

::: ipyvizzustory.get_story
    options:
      show_root_members_full_path: false
::: ipyvizzustory.Story
    options:
      show_root_members_full_path: false
::: ipyvizzustory.Slide
    options:
      show_root_members_full_path: false
::: ipyvizzustory.Step
    options:
      show_root_members_full_path: false
