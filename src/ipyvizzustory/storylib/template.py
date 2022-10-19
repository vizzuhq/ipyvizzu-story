"""A module for storing the html templates."""


VIZZU_STORY = "https://cdn.jsdelivr.net/npm/vizzu-story@~0.2.0/dist/vizzu-story.min.js"
"""str: A variable for storing the default url of vizzu-story package."""

DISPLAY_INDENT = "    "
"""str: A variable for storing the default indent in the html template."""

DISPLAY_TEMPLATE = """
<div>
    <vizzu-player id="{id}" controller></vizzu-player>
    <script type="module">
        import VizzuPlayer, {{ Vizzu as lib }} from "{vizzu_story}";


        const vizzuPlayerData = {vizzu_player_data};
        const vizzuPlayer = document.getElementById("{id}")
        // story.set_size()
        {chart_size}
        vizzuPlayer.slides = vizzuPlayerData;
        vizzuPlayer.vizzu.initializing.then(chart => {{
            // story.set_feature()
            {chart_features}
            // story.add_event()
            {chart_events}
        }});
    </script>
</div>
"""
"""str: A variable for storing the vizzu-story html template."""
