// Get form element and results element
const form = document.querySelector('form');
const results = document.querySelector('#results');

// Add submit event listener to form
form.addEventListener('submit', async (event) => {
event.preventDefault();

// Get project name from form input
const projectName = form.elements.projectName.value;

// Call API to generate justification
const response = await fetch('/generate', {
method: 'POST',
headers: {
'Content-Type': 'application/json'
},
body: JSON.stringify({projectName})
});

// Parse response as text
const justification = await response.text();

// Set justification as the HTML of the results element
results.innerHTML = justification;
});
