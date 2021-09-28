<template>
  <form @submit.prevent="sbmt">
      Temperature: <input type="number" v-model="temp_hum.temperature"/>
      <br>
      Humidity: <input type="number" v-model="temp_hum.humidity"/>
      <br>
      <input type="submit" value="submit" />
  </form>
</template>

<script>
export default {
    data() {
        return {
            temp_hum: {
                temperature:  0,
                humidity: 0
            }
        }
    },
    methods: {
        sbmt () {
            alert("Clicked")
        }
    }
}
</script>

<style>

</style>