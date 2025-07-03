// 6kyu 
function digitalRoot(n) {
    let tot = []
    while (n>=10){
      n = n
        .toString() //makes it string
        .split('') //splits
        .map(Number) //converts to int
        .reduce((acc, val) => acc + val, 0); //sums
      
    }
      return n
  }
