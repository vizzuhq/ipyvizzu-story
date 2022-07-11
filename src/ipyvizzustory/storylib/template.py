"""A module for storing the information needed to generate html code."""


VIZZU_STORY = "https://vizzuhq.github.io/vizzu-ext-js-story/src/vizzu-player.js"

DISPLAY_TEMPLATE = """
<div>
    <vizzu-player id="{id}" controller></vizzu-player>
    <script type="module">
        import VizzuPlayer from "{vizzu_story}";


        function labelHandler(event) {{
            let Year = parseFloat(event.data.text);
            if (!isNaN(Year) && Year > 1950 && Year < 2020 && Year % 5 !== 0) {{
                event.preventDefault();
            }}
        }}

        const vizzuPlayerData = {vizzu_player_data};
        const vizzuPlayer = document.getElementById("{id}")
        vizzuPlayer.slides = vizzuPlayerData;
        vizzuPlayer.vizzu.initializing.then(chart => chart.on("plot-axis-label-draw", labelHandler));
    </script>
</div>
"""
