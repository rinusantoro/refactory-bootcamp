function palindrome(str) {
  
  var tr = false;
  var gnjl = 0;
  str = str.toLowerCase();
  str = str.replace(/[\W_]+/g,'');
   
  var strs = str.split("");
  var strl = strs.length;
  var cntr = Math.ceil(strl/2);
  if(strl%2==1) gnjl = 1;
     
  //console.log('string: '+strs);
  //console.log('length: '+strl);
  //console.log('center: '+cntr);
  var str1 = [];
  var str2 = [];
  for(var i=0;i<=cntr-1;i++){
        str1.push(strs[i]);
    }
    for(var i=cntr-1;i<strl;i++){
        str2.push(strs[i]);
  }
  if(gnjl){ 
 
  }else{
      str2.splice(0,1);
  }
  str1 = str1.join('');
  str2 = str2.reverse().join('');
  if(str1 == str2) tr =true;
   
  console.log('apakah '+str1+' = '+str2+'?');
  console.log('hasil: '+tr);
  //return tr;
}
palindrome("Cigar? Toss it in a can. It is so tragic"); // output true
palindrome("I did, did I?") // output true
palindrome("Red rum, sir, is murder") // output true
palindrome("Eva, can I see bees in a cave?") // output true
palindrome("Hello World") // output false
