"""A module for storing the `HTML` templates."""


VIZZU_STORY: str = (
    "https://cdn.jsdelivr.net/npm/vizzu-story@0.4/dist/vizzu-story.min.js"
)
"""A variable for storing the default url of the `vizzu-story` package."""

DISPLAY_INDENT: str = "    "
"""A variable for storing the default indent in the `HTML` template."""

DISPLAY_TEMPLATE: str = """
<div>
    <vizzu-player id="{id}" {vizzu_attribute} controller></vizzu-player>
    <script type="module">
        import VizzuPlayer from "{vizzu_story}";

        const vp = document.getElementById("{id}");
        import(vp.vizzuUrl).then(vizzuLoaded => {{
            const lib = vizzuLoaded.default;
            const vizzuPlayerData = {vizzu_player_data};
            // story.set_size()
            {chart_size}
            vp.slides = vizzuPlayerData;
            vp.initializing.then(chart => {{
                // story.set_feature()
                {chart_features}
                // story.add_event()
                {chart_events}
            }});
        }});
    </script>
</div>
"""
"""A variable for storing the `vizzu-story` `HTML` template."""
