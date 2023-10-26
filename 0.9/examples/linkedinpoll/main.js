// Import VizzuPlayer
// eslint-disable-next-line no-unused-vars
import VizzuPlayer from 'https://cdn.jsdelivr.net/npm/vizzu-story@0.6/dist/vizzu-story.min.js'
import Csv2Js from '../../assets/javascripts/csv2js.js'

// Get the created element
const vp = document.querySelector('vizzu-player')

// Create data object
const dataLoaded = Csv2Js.csv('./linkedinpoll.csv', ['Year'])
dataLoaded.then((data) => {
  // Each slide here is a page in the final interactive story
  const slides = [
    {
      style: {
        legend: {
          label: { fontSize: '1.1em' },
          paddingRight: '-1em'
        },
        plot: {
          marker: { label: { fontSize: '1.1em' } },
          paddingLeft: '10em',
          xAxis: {
            title: { color: '#00000000' },
            label: { fontSize: '1.1em' }
          },
          yAxis: { label: { fontSize: '1.1em' } }
        },
        logo: { width: '6em' },
        fontSize: '0.8em'
      },
      config: {
        x: { set: ['Vote percentage [%]', 'Answer'] },
        y: 'Group number',
        color: 'Answer',
        label: 'Vote percentage [%]',
        title: 'How often do you present your findings to business stakeholders?'
      }
    },
    {
      style: { plot: { xAxis: { label: { color: '#00000000' } } } },
      config: {
        split: true,
        title: '2 or more is the most popular answer in every group'
      }
    },
    {
      style: {
        plot: {
          marker: { label: { fontSize: '0.916667em' } }
        }
      },
      config: {
        x: { set: ['Vote count', 'Answer'] },
        label: 'Vote count',
        title: '61% of the votes came from one group'
      }
    },
    [
      {
        style: { plot: { yAxis: { title: { color: '#00000000' } } } },
        config: {
          x: 'Answer',
          y: ['Group number', 'Vote count'],
          split: false,
          legend: 'color'
        }
      },
      {
        style: { plot: { marker: { label: { fontSize: '1.1em' } } } },
        config: { y: 'Vote count', title: 'More than 700 people voted' }
      }
    ],
    [
      {
        config: {
          x: ['Answer percentage [%]', 'Answer'],
          y: null,
          label: 'Answer percentage [%]'
        }
      },
      {
        style: { plot: { xAxis: { label: { color: '#00000000' } } } },
        config: {
          coordSystem: 'polar',
          title: 'More than two-third of respondents present at least once per month'
        }
      }
    ]
  ]

  // Create story configuration object, add data and slides to it
  const story = {
    data,
    slides
  }

  // Set the size of the HTML element
  vp.style.cssText = 'width: 100%; height: 450px;'

  // Set up the created element with the configuration object
  vp.slides = story
})
