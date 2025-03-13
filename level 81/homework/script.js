// 2)

class Shows{
    constructor(title,year,author){
        this.title = title
        this.year = year
        this.author = author
    }

}
class Books{
    constructor(title,year,author){
        this.title = title
        this.year = year
        this.author = author
    }
    
}
class Films{
    constructor(title,year,author){
        this.title = title
        this.year = year
        this.author = author
    }
    
}

// 3)
class Animal{
    constructor(name,hasOwner){
        this.name = name
        this.hasOwner = hasOwner
    }

}

class Dog extends Animal{
    constructor(breed){
        super()
        this.breed = breed
    }
}
class Cat extends Animal{
    constructor(eats){
        super()
        this.eats = eats
    }
}

class Horse extends Animal{
    constructor(speed){
        this.speed = speed

    }
}

// 4)
// Inheritence - is a property of a class to pass on its properties to its heirs. it takes all of the constructors of a parent class and gives it to child ones using super function

// super - super function like said takes parent class's constructor properties and gives it to child class

// 5)
// we use classes as a blueprint of what we need. 