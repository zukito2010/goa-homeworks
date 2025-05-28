const child = document.getElementById("child-container");

let left = 0;
let y = 0;
let direction = "down"

const moveDown = setInterval(function(){
    if(direction == "down"){
        y++;
        if(y == 300){
            direction = "right"
        }
    } else if(direction == "right"){
        left++;
        if(left == 300){
            direction = "up";
        }
    } else if(direction == "up"){
        y--;
        if(y == 0){
            direction = "left"
        }
    } else{
        left--;
        if(left == 0 && left == 0){
            clearInterval(moveDown);
        }
    }

    child.style.left = left + 'px';
    child.style.top = y + 'px';
}, 10);