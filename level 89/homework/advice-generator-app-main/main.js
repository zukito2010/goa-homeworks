fetch("https://api.adviceslip.com/advice")
    .then(res => res.json())
    .then(data => {
    const adviceDiv = document.getElementById('advice');
    const advice = data.slip;
    adviceDiv.innerHTML = `
        <p>Advice: ${advice.id}</p>
        <h4>${advice.advice}</h4>
        <img src='./images/pattern-divider-desktop.svg'>
        <button class="dice-button" onclick="location.reload()"><img src='./images/icon-dice.svg'></button>
    `;
    })
    .catch(error => {
    document.getElementById('advice').innerHTML = 'Failed to load advice.';
    console.error(error);
    });

