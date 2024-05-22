<script setup lang="ts">
import type { PostEvent } from '@/types/api'

defineProps<{ event: PostEvent }>()
</script>

<template>
  <form @submit.prevent="">
    <div>
      <input type="text" id="event_type" />
      <label for="event_type"></label>
    </div>
  </form>
</template>
