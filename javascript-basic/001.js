const data = [4, 2, 1, 3, 5];

function sort(data){
    const sort = data.sort()
    return sort
}

function reverse(data){
    const reverse = data.reverse()
    return reverse
}

function splice(data){
    const splice = data.splice(3,0,6)
    return splice
}

sort(data)
reverse(data)
splice(data)
console.log(data)


//const fruits = ['Rambutan', 'Jeruk', 'Anggur']
//const index = fruits.indexOf('Anggur')
//fruits.splice(index, 1)
// console.log(index)
