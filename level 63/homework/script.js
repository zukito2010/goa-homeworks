//3)  this keyword is exactly like self keyword in pythons classes

// 4)
function Computer(gpu,cpu,ram){
    this.gpu = gpu;
    this.cpu = cpu;
    this.ram = ram;
}

const pc1 = new Computer('Geforce GTX 1650', 'i3 10105F', '7.9GB');

console.log(pc1.cpu);
console.log(pc1.gpu);
console.log(pc1.ram);

function Keyboard(brand,ismechanical,size){
    this.brand = brand;
    this.ismechanical = ismechanical;
    this.size = size;
}

const keyboard1 = new keyboard('gxt',false,'100%');

console.log(keyboard1.brand);
console.log(keyboard1.ismechanical);
console.log(keyboard1.size);

function Bus(color,seats){
    this.color = color;
    this.seats = seats;

};

const bus1 = new Bus('green',35);

