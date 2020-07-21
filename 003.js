const deretAngka = new Set();
while(deretAngka.size !== 100) {
  deretAngka.add(Math.floor(Math.random() * 100) + 1);
}

var max = Math.max(...deretAngka);
var min = Math.min(...deretAngka);
var array = [...deretAngka];

// Getting sum of numbers
var sum = array.reduce(function(a, b){
    return a + b;
}, 0);

var average = sum/deretAngka.size;

console.log([...deretAngka]);
console.log(max);
console.log(min);
console.log(sum); 
console.log(average);