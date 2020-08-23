module.exports = (sequelize, Sequelize)=>{
    const Post = sequelize.define("posts", {
        title:{
            type: Sequelize.STRING
        },
        description:{
            type: Sequelize.STRING
        },
        photo:{
            type: Sequelize.STRING
        },
        published:{
            type: Sequelize.BOOLEAN

        }
    });
    return Post;
}