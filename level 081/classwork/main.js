class Car{
    constructor(brand,year,engine,color){
        this.brand = brand
        this.year = year
        this.engine = engine
        this.color = color
    }
    yearPassed(){
        return this.year+=1
    }
    changeColor(color){
        return this.color = color
    }

}

const car1 = new Car('Audi',2009,5.0,'Red');
const car2 = new Car('Ford',2015,7.0,'blue');
const car3 = new Car('BMW',2004,3.0,'black');

console.log(car1.brand);
console.log(car2.brand);
console.log(car3.brand);

console.log(car1.year);
console.log(car2.year);
console.log(car3.year);

console.log(car1.engine);
console.log(car2.engine);
console.log(car3.engine);

console.log(car1.color);
console.log(car2.color);
console.log(car3.color);

console.log(car1.yearPassed())
console.log(car2.yearPassed())
console.log(car3.yearPassed())

console.log(car1.changeColor('Gray'))
console.log(car2.changeColor('Green'))
console.log(car3.changeColor('Pink'))