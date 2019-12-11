client = mqtt.connect("wss://test.mosquitto.org:8081/mqtt")


client.on('connect', function () {
  console.log("Connected Succesfully")
})

function emergency(){
  client.publish("Project","Emergency");
    var payload="Emergency Alarm";
      document.getElementById("block1").innerHTML = payload;
      document.getElementById("block2").innerHTML = payload;
    }

function eatingTime(){
  client.publish("Project","EatingTime");
    var payload = "Eating Time" 
      document.getElementById("block1").innerHTML = payload;
      document.getElementById("block2").innerHTML = payload;
    }

function goingToUSC(){
  client.publish("Project","GoingToUSC")
      var payload = "Going To USC"
      document.getElementById("block1").innerHTML = payload;
      document.getElementById("block2").innerHTML = payload;
    }


function pagingForSomeoneB2(){
  client.publish("Project","PagingB2")
      var payload = "Paging For Someone"
      document.getElementById("block2").innerHTML = payload;
    }


// PAGING FOR BLOCK ONE
function pagingForSomeoneB1(){
  client.publish("Project", "PagingB1")
      var payload = "Paging For Someone"
      document.getElementById("block1").innerHTML = payload;
    }


client.subscribe({
  'Emergency': { qos: 0 },
  'EatingTime': { qos: 0 },
  'GoingToUSC': { qos: 0 },
  'PagingB1': { qos: 0 },
  'PagingB2': { qos: 0 },
  'Off': { qos: 0 },
})
