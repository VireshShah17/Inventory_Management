<template>
  <ion-page>
    <ion-header>
      <ion-toolbar color="primary">
        <ion-title>Smart Inventory</ion-title>
      </ion-toolbar>
    </ion-header>

    <ion-content class="ion-padding">
      <ion-grid>
        <ion-row>
          <ion-col v-for="item in menuItems" :key="item.title" size="12" size-sm="6" size-md="4" class="card-col">
            <ion-card button @click="goTo(item.route)" class="module-card">
              <ion-card-content class="ion-text-center">
                <ion-icon :icon="item.icon" size="large" class="module-icon"></ion-icon>
                <ion-card-title class="ion-margin-top">{{ item.title }}</ion-card-title>
                <p class="muted">{{ item.description }}</p>
              </ion-card-content>
            </ion-card>
          </ion-col>
        </ion-row>
      </ion-grid>
    </ion-content>
  </ion-page>
</template>

<script setup lang="ts">
import { useRouter } from 'vue-router';
import {
  IonPage,
  IonHeader,
  IonToolbar,
  IonTitle,
  IonContent,
  IonGrid,
  IonRow,
  IonCol,
  IonCard,
  IonCardContent,
  IonCardTitle,
  IonIcon
} from '@ionic/vue';
import { people, cube, storefront, receipt } from 'ionicons/icons';

const router = useRouter();

const menuItems = [
  {
    title: 'Parties',
    description: 'Manage customers, suppliers, and contacts.',
    icon: people,
    route: '/parties',
  },
  {
    title: 'Products',
    description: 'View and update all products.',
    icon: cube,
    route: '/products',
  },
  {
    title: 'Inventory',
    description: 'Track stock levels across facilities.',
    icon: storefront,
    route: '/inventory',
  },
  {
    title: 'Billing / POS',
    description: 'Create invoices and handle sales.',
    icon: receipt,
    route: '/billing',
  },
];

function goTo(route: string) {
  router.push(route);
}
</script>

<style scoped>
.module-card {
  height: 160px;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: transform 0.14s ease, box-shadow 0.14s ease;
  border-radius: 12px;
  padding: 0;
}

.module-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 6px 20px rgba(0, 0, 0, 0.08);
}

.module-icon {
  font-size: 36px;
  color: var(--ion-color-primary);
}

.muted {
  color: var(--ion-color-medium);
  margin-top: 6px;
  font-size: 0.9rem;
}

.card-col {
  padding: 8px;
}
</style>
