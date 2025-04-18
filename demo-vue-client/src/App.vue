<script setup lang="ts">
import { onMounted, ref } from 'vue'
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
const rows = ref([] as { id: number }[])
fetch('http://localhost:8001/items/1')
  .then((resp) => resp.json())
  .then((data) => {
    rows.value = data.rows
  })
</script>

<template>
  <header>
    <img alt="Vue logo" class="logo" src="./assets/logo.svg" width="125" height="125" />
    <div class="wrapper"></div>
  </header>

  <main>
    <h1>从服务端返回的值：{{ data.message }}</h1>
    <div>rows 0: id={{ rows.length > 0 ? rows[0].id : '没数据' }}</div>
    <div>
      <div v-for="item in rows" :key="item.id">
        <p>id: {{ item.id }}</p>
      </div>
    </div>
  </main>
</template>

<style scoped></style>
