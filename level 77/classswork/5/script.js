const man = {
    firstName: "Arthur",
    lastName: "Morgan",
    fullName: function() {
      console.log(this.firstName + " " + this.lastName);
    }
};

man.fullName()





function createPerson(property, value) {
    return {
        [property]: value,
    };
}

const person1 = createPerson("name", "zuka");
console.log(person1);




const person2 = {
    name:'Lasha',
    age:15
} 
const person3 = {
    name:'Zviadi',
    height:170
} 

const pperson = Object.assign({},person2,person3)

console.log(pperson)