
var hasil = "";
var jumlah = 0;
var n = 10;

for(let i = 1; i < n; i++){
    var a = prompt("Ketikkan angka ke:" + i);
    hasil = Number(a);
    jumlah = jumlah + hasil;
}

console.log(jumlah);