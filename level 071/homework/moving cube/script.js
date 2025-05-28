const deBox = document.getElementById("deBox");

let moveAmount = 10;
let x = 0;
let y = 0;

document.addEventListener('keydown', e => {
    deBox.textContent = '🚶🏻‍♂️';
    deBox.style.backgroundColor = 'lightblue';
    if (e.key.startsWith('Arrow')){
        switch(e.key){
            case 'ArrowUp':
                y -= moveAmount;
                break;
            case 'ArrowRight':
                x += moveAmount;
                break;
            case 'ArrowDown':
                y += moveAmount;
                break;
            case 'ArrowLeft':
                x -= moveAmount;
                break;
        }
        deBox.style.top = `${y}px`
        deBox.style.left = `${x}px`

    }

});

document.addEventListener('keyup', e => {
    deBox.textContent = '🙍🏻‍♂️';
    deBox.style.backgroundColor = 'rgb(187, 176, 247)';
});