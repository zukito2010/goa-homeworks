class Person{
    constructor(name,year,height){
        this.name = name
        this.__year = year
        this.__height = height
    }

    get year(){
        return this.__year;
    }
    get height(){
        return this.__height;
    }
}

const human = new Person('gia',2005,184);

console.log(human.year);
console.log(human.height);