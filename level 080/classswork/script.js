class Car {
    constructor(brand,model,speed,year){
        this._brand = brand;
        this._model = model;
        this._speed = speed;
        this._year = year;

    }

    get brand(){
        return this._brand;
    }
    
    get acceleration(){
        return this.speed += 20;

    }


}

let car1 = new Car('Toyota', 'Prius', 120 , 2017);
let car2 = new Car('Mercedes', 'ML', 210 ,2015 );
let car3 = new Car('Nissan', 'Sky Line', 300 , 2012);

console.log(car1._brand);
console.log(car1._model);
console.log(car1._speed);
console.log(car1._year);