<script setup lang="ts">
import { onMounted, ref } from 'vue'
import HelloWorld from './components/HelloWorld.vue'
import TheWelcome from './components/TheWelcome.vue'
interface PostItem {
  name: string
  description: string
}
interface PostResponse {
  message: string
}
const data = ref({} as PostResponse)
onMounted(async () => {
  data.value.message = 'loading...'
  const proc = async () => {
    const postitem = {
      name: 'test',
      description: 'description',
    } as PostItem
    const resp = await fetch('http://localhost:8001/items/', {
      method: 'Post',
      body: JSON.stringify(postitem),
      headers: { 'Content-Type': 'application/json' },
    })
    data.value = (await resp.json()) as PostResponse
  }
  setTimeout(proc, 2000)
})
</script>

<template>
  <header>
    <img alt="Vue logo" class="logo" src="./assets/logo.svg" width="125" height="125" />
    <div class="wrapper">
      <HelloWorld msg="You did it!" />
    </div>
  </header>

  <main>
    <h1>从服务端返回的值：{{ data.message }}</h1>
    <TheWelcome />
  </main>
</template>

<style scoped>
header {
  line-height: 1.5;
}

.logo {
  display: block;
  margin: 0 auto 2rem;
}

@media (min-width: 1024px) {
  header {
    display: flex;
    place-items: center;
    padding-right: calc(var(--section-gap) / 2);
  }

  .logo {
    margin: 0 2rem 0 0;
  }

  header .wrapper {
    display: flex;
    place-items: flex-start;
    flex-wrap: wrap;
  }
}
</style>
