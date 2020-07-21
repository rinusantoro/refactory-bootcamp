function reverseString(str) {
 // 1. split string menjadi array substring
 var splitString = str.split('');
 
 // 2. reverse array
 var reverseArray = splitString.reverse();

 // 3. gabungkan semua element array menjadi string
 var joinArray = reverseArray.join('');
 
 return joinArray;
}
console.log(reverseString('semua kata-kata'));