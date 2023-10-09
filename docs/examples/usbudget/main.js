// Import VizzuPlayer
// eslint-disable-next-line no-unused-vars
import VizzuPlayer from 'https://cdn.jsdelivr.net/npm/vizzu-story@latest/dist/vizzu-story.min.js'
import Csv2Js from '../../assets/javascripts/csv2js.js'

// Get the created element
const vp = document.querySelector('vizzu-player')

// Create data object
const dataLoaded = Csv2Js.csv('./usbudget.csv', ['Year'])

dataLoaded.then((data) => {
  // Set the style of the charts in the story

  const style = {
    plot: {
      yAxis: {
        label: {
          fontSize: '1em',
          paddingRight: '1.2em'
        },
        title: { color: '#ffffff00' }
      },
      xAxis: {
        label: {
          angle: '2.5',
          fontSize: '1.1em',
          paddingRight: '0em',
          paddingTop: '1em'
        },
        title: { fontSize: '0.8em', paddingTop: '2.5em' }
      }
    },
    logo: { width: '5em' }
  }

  // Each slide here is a page in the final interactive story
  const slides = [
    // Add the first slide,
    // containing a single animation step that sets the initial chart
    {
      // Only include rows where the Function value != Defense
      filter: (record) => record.Function !== 'Defense',
      config: {
        channels: {
          y: {
            set: ['Amount[B$]', 'Function'],
            // Set the range of the y-axis
            // to the min and max of the data being shown
            // default value is 110% of the maximum value
            range: { min: '0%', max: '100%' }
          },
          x: { set: ['Year'] },
          color: 'Function'
        },
        title: 'Stacked Area Chart - U.S. R&D Budget in 1955-2020',
        geometry: 'area'
      }
    },
    // Show components side-by-side
    {
      config: {
        split: true,
        title: 'Show Components Side by Side'
      }
    },
    // This slide contains multiple steps
    [
      // Step 1 - let's get back to the previous view
      { config: { split: false } },
      // Step 2 - Add the defense function to the chart by removing it from the filter
      {
        filter: null,
        config: { title: 'Add New Category While Keeping the Context' }
      }
    ],
    // Show share of components
    {
      config: {
        align: 'stretch',
        title: 'Show Share of Components (%)'
      }
    },
    // Compare data from 1955 and 2020
    [
      // Step 1 - switch back to value instead of percentage
      { config: { align: 'none' } },
      // Step 2 - switch to a stacked column chart by changing the geometry
      {
        config: {
          geometry: 'rectangle'
        }
      },
      // Step 3 - zoom to data from the first and last years
      {
        filter: (record) => record.Year === '1955' || record.Year === '2020',
        config: {
          title: 'Zoom to Specific Elements'
        }
      }
    ],
    // Group & rearrange elements for comparison
    [
      {
        config: {
          x: ['Year', 'Function'],
          y: 'Amount[B$]',
          label: 'Amount[B$]',
          title: 'Group & Rearrange for Better Comparison'
        }
      },
      {
        config: { x: ['Function', 'Year'] }
      }
    ]
  ]

  // Create story configuration object, add data, style and slides to it
  const story = {
    data,
    style,
    slides
  }

  // Set the size of the HTML element
  vp.style.cssText = 'width: 100%; height: 400px;'

  // Set up the created element with the configuration object
  vp.slides = story
  vp.initializing.then((chart) => {
    // Switch on the tooltip that appears
    // when the user hovers the mouse over a chart element
    chart.feature('tooltip', true)

    // Set a handler that prevents showing the year values that are not divisible by 5
    chart.on('plot-axis-label-draw', (event) => {
      const Year = parseFloat(event.data.text)
      if (!isNaN(Year) && Year > 1950 && Year < 2020 && Year % 5 !== 0) {
        event.preventDefault()
      }
    })
  })
})
