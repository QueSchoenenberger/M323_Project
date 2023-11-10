

// Get all elements with the "clickable-cell" class by class name
let clickableCells = document.getElementsByClassName('clickable-cell');

// Add click event listeners to the clickable cells
for (let i = 0; i < clickableCells.length; i++) {
    clickableCells[i].addEventListener('click', function() {
        let dataHref = this.getAttribute('data-href');
        console.log(dataHref)
        if (dataHref) {
            window.location.href = dataHref; // Navigate to the specified URL
        }
    });
}


function runCode(elementId) {
    // Get the code and output elements by their IDs
    const codeElement = document.getElementById(elementId);
    const outputElement = codeElement;

    // Get the code from the <pre> element
    const code = codeElement.textContent;

    // Send the code to the backend using a POST request
    fetch('/runcode', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ code: code }),
    })
    .then(response => response.json())
    .then(data => {
        // Display the output in the <pre> element with ">>"
        if (data.error) {
            outputElement.innerText += '\n>> Error: ' + data.error;
        } else {
            outputElement.innerText += '\n>> Output:\n' + data.output;
        }
    })
    .catch(error => {
        console.error('Error:', error);
    });
}

function download(filename) {
        // Construct the download URL with the filename parameter
        window.location.href = '/download_pdf/' + filename;
    }