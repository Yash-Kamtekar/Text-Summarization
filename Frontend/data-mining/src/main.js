import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import 'bootstrap/dist/css/bootstrap.css';
import 'font-awesome/css/font-awesome.css'
import 'mdbootstrap/css/bootstrap.css'

import 'vuetify/dist/vuetify.min.css'

createApp(App).use(router).mount('#app')

