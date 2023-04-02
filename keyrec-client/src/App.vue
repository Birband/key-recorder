<template>
  <div id="app">
    <h2>Simple Client</h2> 
    <p id="press">Waiting for key...</p>
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
      document.getElementById("press").innerHTML = event.data
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
</style>
