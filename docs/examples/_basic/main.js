// Import VizzuPlayer
// eslint-disable-next-line no-unused-vars
import VizzuPlayer from 'https://cdn.jsdelivr.net/npm/vizzu-story@latest/dist/vizzu-story.min.js'

// Get the created element
const vp = document.querySelector('vizzu-player')

// Create data object
const data = {
	series: [
		{
			name: 'Foo',
			values: ['Alice', 'Bob', 'Ted']
		},
		{
			name: 'Bar',
			values: [15, 32, 12]
		},
		{
			name: 'Baz',
			values: [5, 3, 2]
		}
	]
}

// Each slide here is a page in the final interactive story
const slides = [
	{
		config: {
			x: 'Foo',
			y: 'Bar'
		}
	},
	{
		config: {
			color: 'Foo',
			x: 'Baz',
			geometry: 'circle'
		}
	}
]

// Create story configuration object, add data and slides to it
const story = {
	data,
	slides
}

// Set up the created element with the configuration object
vp.slides = story
