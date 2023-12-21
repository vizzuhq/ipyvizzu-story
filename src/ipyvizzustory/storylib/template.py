"""A module for storing the `HTML` templates."""


VIZZU_STORY: str = (
    "https://cdn.jsdelivr.net/npm/vizzu-story@0.7/dist/vizzu-story.min.js"
)
"""A variable for storing the default url of the `vizzu-story` package."""

DISPLAY_INDENT: str = "    "
"""A variable for storing the default indent in the `HTML` template."""

DISPLAY_TEMPLATE: str = """
<div>
    <vizzu-player id="{id}" {vizzu} {start_slide} controller></vizzu-player>
    <script type="module">
        import VizzuPlayer from "{vizzu_story}";

        class IpyvizzuStory {{
            static version = "{version}";
            static analytics = undefined;

            static changeAnalyticsTo(analytics) {{
                if (IpyvizzuStory.analytics !== analytics) {{
                    console.log("ipyvizzu-story gather usage stats:", analytics);
                    IpyvizzuStory.analytics = analytics;
                }}
                if (analytics) {{
                    IpyvizzuStory._addHeadScript();
                }} else {{
                    IpyvizzuStory._removeScript("ipyvizzu-story-analytics-head");
                }}
            }}

            static _addHeadScript() {{
                const scriptId = "ipyvizzu-story-analytics-head";
                if (!IpyvizzuStory._isScriptAppended(scriptId)) {{
                    const script = document.createElement("script");
                    script.defer = true;
                    script.src = "https://plausible.io/js/script.local.js";
                    script.dataset.domain = "usage.ipyvizzu-story.com";
                    script.id = scriptId;
                    document.getElementsByTagName("head")[0].appendChild(script);
                }}
            }}

            static _isScriptAppended(id) {{
                return document.querySelector(`script[id="${{id}}"]`) !== null;
            }}

            static _removeScript(id) {{
                const script = document.getElementById(id);
                if (script) script.remove();
            }}
        }}

        if (IpyvizzuStory.version !== window.IpyvizzuStory?.version) {{
            window.IpyvizzuStory = IpyvizzuStory;
            console.log(`ipyvizzu-story ${{IpyvizzuStory.version}}`);
        }}

        window.IpyvizzuStory?.changeAnalyticsTo({analytics});

        class Plugins {{
            static _resolveVizzuVersion(vp) {{
                const url = vp.vizzuUrl;
                const versionMatch = url.match(/vizzu@([^\\/]+)\\//);
                return versionMatch[1];
            }}

            static _resolveUrl(plugin, tag) {{
                if (!plugin.includes('/')) {{
                    const jsdelivr = "https://cdn.jsdelivr.net/npm/@vizzu";
                    return `${{jsdelivr}}/${{plugin}}@${{tag}}/dist/mjs/index.min.js`;
                }}
                return plugin;
            }}

            static register(vp, chart, plugins) {{
                const tag = `vizzu-${{Plugins._resolveVizzuVersion(vp)}}`;
                const pluginsRegistered = [];
                for (const plugin of plugins) {{
                    const pluginUrl = Plugins._resolveUrl(plugin.plugin, tag);
                    const pluginRegistered = import(pluginUrl).then(pluginModule => {{
                        const pluginInstance = new pluginModule[plugin.name](plugin.options);
                        chart.feature(pluginInstance, true);
                    }}).catch((error) => {{
                        console.error('Error importing plugin:', pluginUrl, error)
                    }});
                    pluginsRegistered.push(pluginRegistered);
                }}
                return Promise.all(pluginsRegistered);
            }}
        }}

        const vp = document.getElementById("{id}");
        vp.initializing.then(chart => {{
            const lib = vp.Vizzu;

            // story.set_size()
            {chart_size}

            // story.add_plugin()
            const plugins = [];
            {chart_plugins}
            Plugins.register(vp, chart, plugins).then(() => {{
                // story.set_feature()
                {chart_features}
                // story.add_event()
                {chart_events}

                const vizzuPlayerData = {vizzu_player_data};
                vp.slides = vizzuPlayerData;
            }});
        }});
    </script>
</div>
"""
"""A variable for storing the `vizzu-story` `HTML` template."""
