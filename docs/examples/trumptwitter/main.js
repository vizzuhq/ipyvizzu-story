// Import VizzuPlayer
// eslint-disable-next-line no-unused-vars
import VizzuPlayer from "https://cdn.jsdelivr.net/npm/vizzu-story@latest/dist/vizzu-story.min.js";
import Csv2Js from "../../assets/javascripts/csv2js.js";

// Get the created element
const vp = document.querySelector("vizzu-player");

// Create data object
const dataLoaded = Csv2Js.csv("./trumptwitter.csv", null, [
  "NewtoTwitter",
  "Businessman",
  "Nominee",
  "President",
  "RT_New to Twitter",
  "RT_Businessman",
  "RT_Nominee",
  "RT_President",
  "Obama",
]);

dataLoaded.then((data) => {
  // Set the style of the charts in the story
  const style = {
    tooltip: { fontSize: "22px" },
    title: { paddingTop: "1.2em", fontSize: "2.5em" },
    legend: { label: { fontSize: "1.8em" }, width: "16em" },
    logo: { width: "6em" },
    plot: {
      marker: { label: { fontSize: "1.5em" } },
      yAxis: {
        label: { fontSize: "1.5em" },
        title: { color: "#ffffff00" },
        interlacing: { color: "#ffffff00" },
      },
      xAxis: {
        label: { fontSize: "1.6em", paddingTop: "1em" },
        title: { fontSize: "1.4em", paddingTop: "2.5em" },
      },
    },
  };

  // Each slide here is a page in the final interactive story
  const slides = [
    [
      {
        filter: (record) =>
          record.Firsttweet === "Yes" && record.Dummy === "No",
        config: {
          channels: {
            y: { set: ["tweets"] },
            x: { set: ["Period", "year", "month"] },
            color: "Period",
          },
          title: "Trump started tweeting in May '09",
        },
      },
    ],
    [
      {
        filter: (record) =>
          record.Period === "New to Twitter" && record.Dummy === "No",
        config: { title: "In the first two years he wasn't very active" },
      },
    ],
    [
      {
        filter: (record) =>
          (record.Period === "New to Twitter" ||
            record.Period === "Businessman") &&
          record.Dummy === "No",
        config: { title: "Then he got hooked on" },
      },
    ],
    [
      {
        filter: (record) =>
          (record.Period === "New to Twitter" ||
            record.Period === "Businessman" ||
            record.Period === "Nominee") &&
          record.Dummy === "No",
        config: {
          title: "Interesting trend after becoming a presidential nominee",
        },
      },
    ],
    [
      {
        filter: (record) => record.Dummy === "No",
        config: { title: "And after he became President" },
      },
    ],
    [
      { config: { geometry: "area", align: "center" } },
      { config: { title: "All of Trump's tweets until May 2020" } },
    ],
    [
      {
        config: {
          y: "retweetcount",
          title: "And the number of times these were retweeted",
        },
      },
    ],
    [
      {
        config: {
          y: "tweets",
          title: "Let's focus on the number of tweets for now",
        },
      },
      { config: { x: { set: ["year", "month"] }, color: null } },
    ],
    [
      {
        config: {
          y: ["tweets", "Type"],
          color: "Type",
          title: "Original tweets, retweets & replies sent",
        },
        style: {
          plot: { marker: { colorPalette: "#A0CDEBFF #60C0E6FF #1DA1F3FF" } },
        },
      },
    ],
    [
      {
        config: { split: true, align: "none" },
        style: { plot: { yAxis: { label: { color: "#ffffff00" } } } },
      },
    ],
    [
      {
        config: {
          split: false,
          align: "stretch",
          title: "Original tweets, retweets & replies sent (%)",
        },
        style: { plot: { yAxis: { label: { color: "#999999ff" } } } },
      },
    ],
    [
      { config: { align: "center", title: "" } },
      {
        config: { y: "tweets", color: null, legend: "lightness" },
        style: { plot: { marker: { colorPalette: "null" } } },
      },
      {
        config: {
          y: ["tweets", "Tool"],
          color: "Tool",
          title: "Tools Trump Used to Tweet",
          legend: "color",
        },
        style: {
          plot: {
            marker: {
              colorPalette: "#597696FF #ED2828FF #26EC87FF #29B9BFFF ",
            },
          },
        },
      },
    ],
    [
      {
        config: { split: true, align: "none" },
        style: { plot: { yAxis: { label: { color: "#ffffff00" } } } },
      },
    ],
    [
      { config: { geometry: "rectangle" } },
      {
        config: {
          x: ["tweets", "year", "month"],
          y: "Tool",
          geometry: "rectangle",
          split: false,
          align: "none",
        },
        style: {
          plot: {
            xAxis: { title: { color: "#ffffff00" } },
            yAxis: { label: { color: "#999999ff" } },
          },
        },
      },
      { config: { x: "tweets", label: "tweets" } },
    ],
    [
      { config: { x: ["tweets", "AMPM", "hour12"], label: null } },
      {
        config: { y: ["tweets", "Tool"], x: ["AMPM", "hour12"], align: "max" },
      },
      { config: { geometry: "area" } },
      {
        config: {
          coordSystem: "polar",
          rotate: 180,
          title: "Time of Day When Trump Tweeted",
        },
        style: {
          plot: {
            yAxis: { label: { color: "#ffffff00" } },
            xAxis: {
              label: {
                fontSize: "2em",
                paddingBottom: "2.5em",
                paddingTop: "2.5em",
                paddingLeft: "2.5em",
                paddingRight: "2.5em",
              },
            },
          },
        },
      },
    ],
    [
      {
        config: {
          y: ["Businessman", "Tool"],
          title: "Times Trump Tweeted When Being a Businessman",
        },
      },
    ],
    [
      {
        config: {
          y: ["President", "Tool"],
          title: "Times Trump Tweeted When Being President",
        },
      },
    ],
  ];

  // Create story configuration object, add data and slides to it
  const story = {
    data,
    style,
    slides,
  };

  // Set the size of the HTML element
  vp.style.cssText = "width: 100%; height: 400px;";

  // Set up the created element with the configuration object
  vp.slides = story;
  vp.initializing.then((chart) => {
    // Switch on the tooltip that appears
    // when the user hovers the mouse over a chart element
    chart.feature("tooltip", true);
  });
});
