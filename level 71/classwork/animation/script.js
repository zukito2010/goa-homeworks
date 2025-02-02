let box = document.getElementById('box');
let x = 0
let y = 0
const moveRight = setInterval(function(){
    if (x === 430){
        clearInterval(moveright)
        const moveDown = setInterval(function(){
            // if (y === 430){
            //     clearInterval(moveDown)
            // }
            
            y++
            box.style.bottom = `${y}px`
        },10)
    }
    
    x++
    box.style.left = `${x}px`
},10)