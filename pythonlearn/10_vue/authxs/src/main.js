import { createApp } from 'vue'
import App from './App.vue'
import ElementUI from 'element-ui';	// Element 1
import 'element-ui/lib/theme-chalk/index.css'; // Element 2

// �ر� Vue ��������ʾ
Vue.config.productionTip = false

// ʹ�ò��
Vue.use(ElementUI); // Element 3

// ���� Vue ʵ������
new Vue({
  render: h => h(App),
}).$mount('#app')