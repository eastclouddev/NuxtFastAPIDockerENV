<template>
  <NuxtLayout>
    <div>
      <h1>ユーザー削除</h1>
      <input v-model="userId" type="number" placeholder="Enter User ID to delete" />
      <button @click="deleteUser">Delete User</button>
    </div>
  </NuxtLayout>
</template>
  
<script setup>
  import { ref } from 'vue';
  import { UserService } from '~/services/UserService.js';
  import { useRouter } from 'vue-router';
  
  const router = useRouter();
  const userId = ref('');
  
  const deleteUser = async () => {
    if (!userId.value) {
      alert('Please enter a valid User ID');
      return;
    }

    try {
      await UserService.deleteUser(userId.value);
      alert('User delete successfully');
      userId.value = '';
    } catch (error) {
      alert(error.message);
    }
    // router.push('/users'); 
  };
</script>