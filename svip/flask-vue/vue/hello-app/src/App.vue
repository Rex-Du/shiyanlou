<template>
  <div id="app">
    <ul>
      <li v-for="name, index in msg">{{ name }}</li>
    </ul>
  </div>
</template>

<script>
export default {
  name: 'app',
  data () {
    return {
      msg: 'Hello, world!'
    }
  }
}
</script>

<script>
var axios = require('axios');

export default {
  name: 'app',
  data () {
    return {
      msg: ''
    }
  },
  mounted() {
      axios.get('/api/hello').then(response => this.msg=response.data.users)
  }
}
</script>
