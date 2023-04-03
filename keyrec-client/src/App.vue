<template>
  <div id="app">
    <h2>Simple Client</h2> 
    <p>Waiting for key...</p>
    <div>
      <span class="key-button-basic"><p id="press">nic</p></span>
    </div>
  </div>
</template>

<script>
export default {
  name: 'App',
  data: function() {
    return {
      connection: null
    }
  },
  created: function() {
    console.log("Starting connection...")
    this.connection = new WebSocket("ws://127.0.0.1:55555")
  
    this.connection.onmessage = function (event) {
      console.log("Received message: " + event.data)
      // replace backspace in event.data with a <-
      var keyRedacted = event.data
      if (keyRedacted == "backspace") {
        keyRedacted = "<-"
      } else if (keyRedacted == "enter") {
        keyRedacted = "↵"
      } else if (keyRedacted == "space") {
        keyRedacted = "␣"
      }

      document.getElementById("press").innerHTML = keyRedacted
    }

    this.connection.onopen = function () {
      console.log("Connection successful")
    }

    this.connection.onclose = function () {
      console.log("Connection closed")
    }

    this.connection.onerror = function (event) {
      console.log("Connection error")
      console.log(event)
    }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
.key-button-basic {
  position: relative;
  display: inline-block;
  width: 85px;
  height: 85px;
  border-radius: 10px;
  background: linear-gradient(180deg, #f3f3f3, #e7e7e7);
  box-shadow: 0 0 0 2px rgba(0, 0, 0, 0.5),
  5px 5px 10px rgba(0, 0, 0, 0.35),
  inset 0 -10px 10px rgba(255, 255, 255, 0.6),
  inset 10px 10px 20px rgba(0, 0, 0, 0.3);
  overflow: hidden;
}
.key-button-basic::before {
  content: '';
  position: absolute;
  top: 5px;
  left: 5px;
  bottom: 15px;
  right: 15px;
  background: linear-gradient(90deg, #f3f3f3, #e2e2e2);
  border-radius: 10px;
  box-shadow: -10px -10px 15px 10px rgba(100, 100, 100, 0.4), 10px 10px 5px 15px rgba(100, 100, 100, 0.1);
}
.key-button-basic p {
  position: relative;
  color: #000;
  right: 10px;
  font-size: larger;
}
</style>
