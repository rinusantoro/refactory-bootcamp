
module.exports = app => {
    const auth = 
    require('../middleware/auth');
    const posts = 
    require("../controllers/post.controllers");

    let router = 
    require("express").Router();

    //create a new post
    router.post("/", posts.create);
    router.get("/", posts.findAll);
    
    router.put("/image-photo/:id/:title", posts.uploadImagePost);


    app.use("/api/posts", auth.isAuth,router);
}