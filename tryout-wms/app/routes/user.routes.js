module.exports = app => {
    const users = require("../controllers/user.controller")
    const auth = require("../middleware/auth")
    let router = require("express").Router()

    //create new post
    router.post("/signup",users.signup)
    router.post("/signin",users.signin)
    router.get("/all/:limit/:pagination",auth.isAuth,users.getAll)
    router.get("/:id",auth.isAuth,users.getId)
    router.put("/:id",auth.isAuth,users.editUser)
    router.delete("/:id",auth.isAuth,users.deleteUser)
    
    app.use("/api/v1/users/",router)
}