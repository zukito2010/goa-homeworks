const me = {
    name:'Zuka',
    lastname:'Tughriashvili',
    age:'14',
    favcolor:'Red',
}

const ioseb = {
    name:'Ioseb',
    lastname:'Jughashvili',
    age:'52',
    favcolor:'Red',
}

const marina = {
    name:'Marina',
    lastname:'Papashvili',
    age:'27',
    favcolor:'Violet',
}


console.log(me.name);
console.log(me.lastname);
console.log(me.age);
console.log(me.favcolor);
console.log(' ')
console.log(ioseb.name);
console.log(ioseb.lastname);
console.log(ioseb.age);
console.log(ioseb.favcolor);
console.log(' ')
console.log(marina.name);
console.log(marina.lastname);
console.log(marina.age);
console.log(marina.favcolor);


// car constructor function

function Car(brand,model,year){
    this.brand = brand; 
    this.model = model ;
    this.year = year ;
}

let car1 = new Car(brand='BMW',model='X5',year = 2016)
let car2 = new Car(brand='Lada',model='Riva',year = 1997)
let car3 = new Car(brand='Honda',model='Odyssey',year = 2014)

console.log(' ');
console.log(car1.brand);
console.log(car1.model);
console.log(car1.year);
console.log(' ');
console.log(car2.brand);
console.log(car2.model);
console.log(car2.year);
console.log(' ');
console.log(car2.brand);
console.log(car2.model);
console.log(car2.year);

// person constructor function

function Person(fname,lname,age,country){
    this.fname = fname;
    this.lname = lname;
    this.age = age;
    this.country = country;

}
let pers1 = new Person('Zuka','Tughriashvili',14,'Georgia');
let pers2 = new Person('Nika','Alaverdashvili',19,'Armenia');
let pers3 = new Person('Greg','Smith',15,'USA');

console.log(' ');
console.log(pers1.fname);
console.log(pers1.lname);
console.log(pers1.age);
console.log(pers1.country);
console.log(' ');
console.log(pers2.fname);
console.log(pers2.lname);
console.log(pers2.age);
console.log(pers2.country);
console.log(' ');
console.log(pers3.fname);
console.log(pers3.lname);
console.log(pers3.age);
console.log(pers3.country);

// animal constructor function

function Animal(animl,name,isPet,){
    this.animl = animl;
    this.name = name;
    this.ispet = isPet;
}

let animal1 = new Animal('Wolf','Ryan',false);
let animal2 = new Animal('Rabbit','Peter',true);
let animal3 = new Animal('Dog','Scooby',true);

console.log(' ');
console.log(animal1.animl);
console.log(animal1.name);
console.log(animal1.ispet);
console.log(' ');
console.log(animal2.animl);
console.log(animal2.name);
console.log(animal2.ispet);
console.log(' ');
console.log(animal3.animl);
console.log(animal3.name);
console.log(animal3.ispet);


// we need constructor functions to make a programmers life easier. with it its very simple to create bunch of objects 