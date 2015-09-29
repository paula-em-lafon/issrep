var express = require('express')
,app = express()
,server = require('http').createServer(app)
,io = require('socket.io').listen(server)
,amqp = require('amqp')
;


app.configure(function() {
    app.use(express.static(__dirname + '/public2'));
});



var q = 'node';


var open = require('amqplib').connect('amqp://localhost');


// Consumer
open.then(function(conn) {
  var ok = conn.createChannel();
  ok = ok.then(function(ch) {
    ch.assertQueue(q);
    ch.consume(q, function(msg) {
      
      ch.ack(msg);
      //var d = {id:34, title:"fromRabbitMq", body:msg.content.toString()};

      //var demo = {title:"Examen", data:msg.content.toString()};
      console.log(" -----> " + msg.content.toString() + " <----- ");
      var m = JSON.parse(msg.content.toString());

      console.log("------> " + m.x + "<------");
      console.log("------> " + m.y + "<------");
      
      io.sockets.emit('message', m);
    });
  });
  return ok;
}).then(null, console.warn);



/*
var connection = amqp.createConnection({ host: '127.0.0.1' });

// Wait for connection to become established.
connection.on('ready', function () {
  // Use the default 'amq.topic' exchange
  connection.queue('node', function(q){
      // Catch all messages
      q.bind('#');

      // Receive messages
      q.subscribe(function (message) {
        // Print messages to stdout
        console.log(message.data.toString());
      });
  });
});

*/

io.sockets.on('connection', function(socket) {
	
  socket.on('senMessage', function(data){
    socket.broadcast.emit('message', data);
    //console.log('senMessage --> ' + data);
    //console.log('senMessage --> ' + data.title);
    //console.log('senMessage --> ' + data.msg);
  });

});
console.log("Server start on 3000");
server.listen(3000);
