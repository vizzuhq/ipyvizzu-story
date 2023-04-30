// Import VizzuPlayer
// eslint-disable-next-line no-unused-vars
import VizzuPlayer from "https://cdn.jsdelivr.net/npm/vizzu-story@latest/dist/vizzu-story.min.js";
import Csv2Js from "../../assets/javascripts/csv2js.js";

// Get the created element
const vp = document.querySelector("vizzu-player");

// Create data object
const dataLoaded = Csv2Js.csv("./proglangs.csv", ["Year"]);

dataLoaded.then((data) => {
  // Each slide here is a page in the final interactive story
  const slides = [
    {
      filter: (record) => record.Year === "2022",
      style: {
        logo: { width: "5em" },
        plot: {
          xAxis: { title: { color: "#00000000" } },
          paddingLeft: "2.5em",
          marker: {
            colorPalette:
              "#3DAE2BFF " +
              "#00833EFF " +
              "#00A19BFF " +
              "#0075A9FF " +
              "#003764FF",
            minLightness: 0,
            maxLightness: 0.4,
          },
        },
        fontSize: "0.8em",
      },
      config: {
        x: ["Popularity", "Value[%]"],
        y: ["Language", "Year", "Lang_year"],
        color: "Popularity",
        label: "Value[%]",
        align: "stretch",
        title: "Use of programming languages by data scientists in 2022",
        lightness: "Year",
        legend: "color",
      },
    },
    {
      style: { plot: { xAxis: { label: { color: "#00000000" } } } },
      config: {
        split: true,
        align: "min",
        title: "Python is always or frequently used by 58%",
      },
    },

    [
      {
        style: { plot: { xAxis: { label: { color: "#999999FF" } } } },
        config: { split: false, align: "stretch" },
      },
      {
        filter: (record) =>
          (record.Popularity === "Always" ||
            record.Popularity === "Frequently") &&
          record.Year === "2022",
        config: { x: { range: { max: 100 } }, align: "min" },
      },
      {
        config: {
          sort: "byValue",
          title: "Python & SQL are the most popular by a huge margin",
        },
      },
    ],
    [
      {
        config: {
          sort: "none",
          title: "Let's focus on the six languages with data since 2020",
        },
      },
      {
        filter: (record) =>
          (record.Popularity === "Always" ||
            record.Popularity === "Frequently") &&
          (record.Language === "R" ||
            record.Language === "Python" ||
            record.Language === "JavaScript" ||
            record.Language === "Java" ||
            record.Language === "C#" ||
            record.Language === "C/C++") &&
          record.Year === "2022",
      },
      {
        config: {
          y: ["Lang_year", "Year"],
          x: ["Popularity", "Language", "Value[%]"],
        },
      },
    ],
    [
      {
        filter: (record) =>
          (record.Popularity === "Always" ||
            record.Popularity === "Frequently") &&
          (record.Language === "R" ||
            record.Language === "Python" ||
            record.Language === "JavaScript" ||
            record.Language === "Java" ||
            record.Language === "C#" ||
            record.Language === "C/C++") &&
          record.Year !== "2020",
      },
      {
        filter: (record) =>
          (record.Popularity === "Always" ||
            record.Popularity === "Frequently") &&
          (record.Language === "R" ||
            record.Language === "Python" ||
            record.Language === "JavaScript" ||
            record.Language === "Java" ||
            record.Language === "C#" ||
            record.Language === "C/C++"),
        config: {
          title: "C/C++, C#, Java and Javascript are gaining popularity",
        },
      },
    ],
  ];

  // Create story configuration object, add data and slides to it
  const story = {
    data,
    slides,
  };

  // Set the size of the HTML element
  vp.style.cssText = "width: 100%; height: 600px;";

  // Set up the created element with the configuration object
  vp.slides = story;
  vp.initializing.then((chart) => {
    // Switch on the tooltip that appears
    // when the user hovers the mouse over a chart element
    chart.feature("tooltip", true);

    // Set a handler that prevents showing specific elements
    chart.on("plot-marker-label-draw", (event) => {
      if (event.data.text.split(" ")[0] < 5) event.preventDefault();
    });
  });
});
