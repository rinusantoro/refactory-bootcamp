var nilai = prompt("Inputkan nilai akhir:");
var grade = "";

if(nilai >= 90) grade = "A"
else if(nilai >= 80 && nilai <= 89) grade = "B"
else if(nilai >= 70 && nilai <= 79) grade = "C"
else if(nilai >= 60 && nilai <= 69) grade = "D"
else if(nilai < 59) grade = "E"

console.log(grade);
