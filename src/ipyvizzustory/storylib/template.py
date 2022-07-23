"""A module for storing the information needed to generate html code."""


VIZZU_STORY = "https://cdn.jsdelivr.net/npm/vizzu-story@~0.1.0/dist/vizzu-story.min.js"

DISPLAY_INDENT = "    "

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
