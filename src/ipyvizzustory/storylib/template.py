"""A module for storing the information needed to generate html code."""


VIZZU_STORY = "https://vizzuhq.github.io/vizzu-ext-js-story/src/vizzu-player.js"

DISPLAY_INDENT = "            "

DISPLAY_TEMPLATE = """
<div>
    <vizzu-player id="{id}" controller></vizzu-player>
    <script type="module">
        import VizzuPlayer from "{vizzu_story}";


        const vizzuPlayerData = {vizzu_player_data};
        const vizzuPlayer = document.getElementById("{id}")
        vizzuPlayer.slides = vizzuPlayerData;
        vizzuPlayer.vizzu.initializing.then(chart => {{
            // chart.feature()
            {chart_features}
            // chart.on()
            {chart_events}
        }});
    </script>
</div>
"""
