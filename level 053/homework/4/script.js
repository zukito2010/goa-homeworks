const img = document.getElementById('shrek');
const button = document.getElementById('butn');
img.style.height = 300 + 'px'
function fatter(img) {
    const currentWidth = parseInt(img.style.width) || img.offsetWidth; 
    img.style.width = (currentWidth + 50) + 'px'; 
}

button.onclick = () => fatter(img);