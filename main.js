// script.js
document.getElementById('churn-form').addEventListener('submit', function (e) {
    e.preventDefault(); // Prevent the form from reloading the page

    const form = e.target;

    // Collect data from the form
    const customerData = {
        creditScore: parseInt(form['creditScore'].value),
        age: parseInt(form['age'].value),
        tenure: parseInt(form['tenure'].value),
        hasCrCard: form['hasCrCard'].checked,
        isActiveMember: form['isActiveMember'].checked,
        estimatedSalary: parseFloat(form['estimatedSalary'].value),
        geography: form['geography'].value,
        gender: form['gender'].value,
        totalProducts: parseInt(form['totalProducts'].value),
        accountBalance: parseFloat(form['accountBalance'].value)
    };

    // Send the data to the server
    fetch('http://127.0.0.1:8000/predict/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(customerData)
    })
        .then(response => response.json())
        .then(data => {
            // Display the prediction result
            document.getElementById('prediction-result').innerText = `Predicted churn: ${data.prediction}`;
        })
        .catch(error => {
            console.error('Error:', error);
        });
});
