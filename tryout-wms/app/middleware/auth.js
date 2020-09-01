const jwt = require("jsonwebtoken")

module.exports = {
    isAuth: (req,res,next)=>{
        try {
           const token = req.headers.token
           var decoded = jwt.verify(token,process.env.SECRET_JWT) 
           req.user = decoded
           next()
        } catch (err) {
            res.status(401).json({
                err: err.message,
                message : 'token is invalid'
            })
        }
    }
}