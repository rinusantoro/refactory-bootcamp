const db = require("../models/index");
const slack = require("../slack/it.slack");
const jwt = require('jsonwebtoken');
const Post = db.posts;
const Op = db.Sequelize.Op;
require("dotenv").config()


//post
exports.create = (req, res) => {
    
    var user = 
    (jwt.verify
        (req.headers.token, 
            process.env.SECRET_JWT));
    console.log("user "+user.id);

    //Validate request
    if (!req.body.title  ) {
        res.status(400).send(
            {
                message: "Content can not be empty"
            }
        );
        return;
    }
    //Create post
    const post = {
        title: req.body.title,
        description: req.body.description,
        photo: "-",
        published: req.body.published ? 
        req.body.published : false

    }
    Post.create(post)
        .then((data) => {
            res.send(data);
        }).catch((err) => {
            res.status(500).send({
                message: err.message || 
                "some error occured while creating the Post"
            })
        });

    slack.sendMessage("rinu","upttik",
    "Title : "+post.title +" | Description : "+post.description);
    };

//put upload image
exports.uploadImagePost = async (req, res) => {
    const id = req.params.id;
    const title = req.params.title;

    try {
        if (!req.files) {
            res.send({
                status: false,
                message: 'No file uploaded'
            });
        } else {
            //Use the name of the input field 
            let photo = req.files.photo;
            var renamePhoto = + id
                + "-"
                + title
                + (photo.name).substring((photo.name).indexOf("."))

            Post.update({
                photo: renamePhoto

            }, {
                where: { id: id }
            }).then((result) => {
                if (result == 1) {
                    photo.mv('./uploads/' + renamePhoto);
                    //send response
                    res.send({
                        status: true,
                        message: 
                        'Photo post File is uploaded',
                        data: {
                            name: photo.name,
                            rename : renamePhoto,
                            mimetype: photo.mimetype,
                            size: photo.size
                        }
                    });
                } else {
                    res.send({
                        message: 
                        `Cannot update Post with id = ${id}`
                    })
                }
            }).catch((err) => {
                res.status(500).send({
                    message: `Error updating post id = ${id}`
                })
            })

        }
    } catch (err) {
        res.status(500).send(err);
    }
};

//retrive all
exports.findAll = (req, res) => {
    const title = req.query.title;
   
    let condition = 
    title ? { title: { [Op.like]: `%${title}%` } } : null;
   
    Post.findAll({ where: condition })
        .then((data) => {
            res.send(data);
        }).catch((err) => {
            res.status(500).send({
                message:
                    err.message 
                    || "Some error occured while find post"
            })
        });
};