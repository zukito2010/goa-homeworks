// 1) https://www.codewars.com/kata/56dec885c54a926dcd001095/train/javascript
function opposite(number) {
    return -number
  }

// 2) https://www.codewars.com/kata/5168bb5dfe9a00b126000018/train/javascript
function solution(str){
    return str.split('').reverse('').join('');
  }

// 3) https://www.codewars.com/kata/53369039d7ab3ac506000467/train/javascript
function boolToWord( bool ){
    if (bool){
      return 'Yes';
    }else{
      return 'No';
    }
  }

// 4) https://www.codewars.com/kata/5715eaedb436cf5606000381/train/javascript
function positiveSum(arr) {
    let res = 0
    for (let i of arr){
      if (i > 0){
        res += i
        
      }else{
        continue
      
      }
    }
      return res
  }

// 5) https://www.codewars.com/kata/57a0e5c372292dd76d000d7e/train/javascript
function repeatStr (n, s) {
    return s.repeat(n);
  }