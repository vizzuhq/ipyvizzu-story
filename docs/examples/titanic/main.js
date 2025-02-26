// Import VizzuPlayer
// eslint-disable-next-line no-unused-vars
import VizzuPlayer from 'https://cdn.jsdelivr.net/npm/vizzu-story@latest/dist/vizzu-story.min.js'
import Csv2Js from '../../assets/javascripts/csv2js.js'

// Get the created element
const vp = document.querySelector('vizzu-player')
const vizzuLoaded = import(vp.vizzuUrl)

// Create data object
const dataLoaded = Csv2Js.csv('./titanic_js.csv', { dimensions: ['Pclass'] })

Promise.all([dataLoaded, vizzuLoaded]).then((results) => {
	const data = results[0]
	const Vizzu = results[1].default

	// Set the style of the charts in the story
	const style = {
		plot: {
			yAxis: {
				label: { fontSize: '1em', paddingRight: '1.2em' },
				title: { color: '#ffffff00' }
			},
			xAxis: {
				label: {
					angle: '2.5',
					fontSize: '1.1em',
					paddingRight: '0em',
					paddingTop: '1em'
				},
				title: { fontSize: '1em', paddingTop: '2.5em' }
			}
		},
		logo: { width: '5em' }
	}

	// Each slide here is a page in the final interactive story
	const slides = [
		[
			{
				config: Vizzu.presets.bar({
					x: 'Count',
					title: 'Passengers of the Titanic'
				})
			}
		],
		[
			{ config: Vizzu.presets.stackedBar({ x: 'Count', stackedBy: 'Sex' }) },
			{
				config: Vizzu.presets.groupedBar({
					x: 'Count',
					y: 'Sex',
					legend: 'color',
					title: 'Rougly one-third of the passengers were ladies'
				})
			}
		],
		[
			{
				config: {
					x: ['Count', 'Survived'],
					y: 'Sex',
					color: 'Sex',
					lightness: 'Survived',
					label: ['Survived', 'Count']
				}
			},
			{
				config: {
					align: 'stretch',
					title: 'Much more women survived than men'
				}
			}
		],
		[
			{
				config: {
					x: 'Count',
					align: 'none',
					label: null,
					lightness: null,
					title: "Let's add the age of the passengers to the mix"
				}
			},
			{ config: { y: ['Count', 'Sex'], x: 'Age_group', label: 'Count' } }
		],
		[
			{
				config: {
					label: null,
					title: "Let's see how many people survived/died in these age groups"
				}
			},
			{
				config: {
					y: ['Count', 'Sex', 'Survived'],
					lightness: 'Survived',
					legend: 'lightness'
				}
			},
			{ config: { y: ['Count', 'Survived', 'Sex'] } }
		],
		[
			{
				config: {
					align: 'stretch',
					title: 'Survival rate varies a bit between age groups'
				}
			}
		],
		[
			{
				filter: (record) => record.Sex === 'male',
				config: {
					title: 'But again shows a very different picture for men...'
				}
			}
		],
		[
			{ filter: null },
			{
				filter: (record) => record.Sex === 'female',
				config: { title: '...and women' }
			}
		]
	]

	// Create story configuration object, add data and slides to it
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
	})
})
