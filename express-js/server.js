var express = require('express');
var app = express();
var path = require('path');
var view = __dirname + "/views/";
var public = __dirname + "/public/";
app.get('/', function(req, res) {
 res.sendFile(path.join(view + "home.html"));
});
app.get('/career', function(req, res) {
 res.sendFile(path.join(view + "career.html"));
});
app.get('/photo', function(req, res) {
 res.sendFile(path.join(view + "photo.html"));
});
app.use('/', express.static(public));
app.listen(8080);