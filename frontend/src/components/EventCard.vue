<script setup lang="ts">
import type { Event, PostEvent } from '@/types/api'

defineProps<{ event: Event | PostEvent }>()
</script>

<template>
  <section>
    <h3 class="text-xl">{{ event.type?.toUpperCase() }}</h3>
    <p class="mb-2 mt-2">
      {{ event.explanation }}
    </p>
    <ol class="flex m-2">
      🔗
      <li v-for="link of event.links" :key="link.url" class="underline text-blue-600 ml-2">
        <a :href="link.url">{{ link.url }}</a>
      </li>
    </ol>
    <ol class="flex m-2">
      📎
      <li v-for="attach of event.attachments" :key="attach.filename" class="underline ml-2">
        <a :href="`file:///home/docs/${attach.filename}`">{{ attach.filename }}</a>
      </li>
    </ol>
  </section>
</template>
