
var SECOND = 1000;
var now = new Date();


var dateBefore = new Date(now - (120 * SECOND));

function wait(ms){
   ms = ms*1000
   var start = new Date().getTime();
   var end = start;
   while(end < start + ms) {
     end = new Date().getTime();
  }
}

console.log(now);
console.log(dateBefore);
mongodb://<user name><Password><address>port/blazemeter
var MongoClient = require('mongodb').MongoClient;

var before = new Date();
var foo = function(db){
  db.collection("ready").find().toArray(function(err, result) {

      console.log('beggining!')
      readyStuff = result.map(function(el){
        return {'length':el['servers'].length, 'sessionId':el['_id'] };
      })
      counter = 0
      sessionsInfo.forEach(el => {
        sessionId = el['id']
        numberOfServers=el['serversCount']
        readySessionStuff = readyStuff.filter(function(el){
            return (el['sessionId'] === sessionId);
        })


        if (!(readySessionStuff === undefined || readySessionStuff.length == 0)){
            if (readySessionStuff[0]['length'] === numberOfServers){
              counter = counter+1
            }
        }
      })
      console.log('required: ' + sessionsInfo.length)
      console.log('actual: ' + counter)
      if (counter < sessionsInfo.length){
        wait(1)
        foo(db);
      }else{

        var after = new Date();
        var difference = after.getTime() - before.getTime();

        var date = new Date(null);
        date.setSeconds(difference/1000);
        difference = date.toISOString().substr(11, 8);


        console.log('provisioning took '+ difference)
        db.close();
      }
    })
}
MongoClient.connect('mongodb://localhost:27019/blazemeter_qa', function(err, db) {
    if (err) {
        console.error(err);
    }
    else{

      db.collection("sessions").find().toArray(function(err, result) {
        if (err) throw err;

        sessionsInfo = result.map(function(el){
          return {'id':el['_id'], 'serversCount':el['configuration']['serversCount']+1};
        })
        console.log('hello?');
        foo(db);
        // while (true){
        //   console.log('bringing data');
        //   wait(2);

        // }

      })
    }
});
