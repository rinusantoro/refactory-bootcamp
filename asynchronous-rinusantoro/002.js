const axios = require('axios');

const url_users = 'https://jsonplaceholder.typicode.com/users';
const url_posts = 'https://jsonplaceholder.typicode.com/posts';

const requestOne = axios.get(url_users);
const requestTwo = axios.get(url_posts);

axios.all([requestOne, requestTwo]).then(axios.spread((...responses) => {
  const responseOne = responses[0];
  const responseTwo = responses[1];

  const users  = responseOne.data;

  const posts  = responseTwo.data;

  for(index in posts){
  	let userid = posts[index].userId;

    let found_user = users.find(user => user.id == userid);
  	if (typeof found_user != 'undefined'){
  		posts[index].user = found_user;
  	}
  	
  }

  console.log(posts);

})).catch(errors => {
  throw new Error(errors.message);
})