
var Slack = require('node-slack');
var slack = new Slack("https://hooks.slack.com/services/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");

exports.sendMessage = async (username, channel, message) => {

    try {

        await slack.send({
            text: message,
            channel: '#' + channel,
            username: username
        });
    } catch (err) {
        console.log("ERR " + err);
    }
    console.log('Sending message', message, 'to channel', channel);
}

