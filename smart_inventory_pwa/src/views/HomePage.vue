<template>
  <ion-page>
    <ion-header>
      <ion-toolbar color="primary">
        <ion-title>Smart Inventory</ion-title>
      </ion-toolbar>
    </ion-header>

    <ion-content class="ion-padding dashboard-bg">
      <ion-grid>
        <ion-row>
          <ion-col v-for="(item, index) in menuItems" :key="item.title" size="12" size-sm="6" size-md="4"
            class="card-col">
            <ModuleCard :ref="(el) => collectCardRef(el, index)" :title="item.title" :description="item.description"
              :icon="item.icon" :route="item.route" :color="item.color" />
          </ion-col>
        </ion-row>
      </ion-grid>
    </ion-content>
  </ion-page>
</template>

<script setup lang="ts">
import {
  IonPage,
  IonHeader,
  IonToolbar,
  IonTitle,
  IonContent,
  IonGrid,
  IonRow,
  IonCol,
} from "@ionic/vue";
import ModuleCard from "@/components/ModuleCard.vue";
import { peopleCircle, receipt, analytics, pricetags } from "ionicons/icons";
import { createAnimation } from "@ionic/vue";
import { ref, onMounted, nextTick } from "vue";

// holds DOM references
const cards = ref<HTMLElement[]>([]);

// dashboard menu items
const menuItems = [
  {
    title: "Parties",
    description: "Manage customers, suppliers, and contacts.",
    icon: peopleCircle,
    route: "/parties",
    color: "primary",
  },
  {
    title: "Products",
    description: "View and update all products.",
    icon: pricetags,
    route: "/products",
    color: "tertiary",
  },
  {
    title: "Inventory",
    description: "Track stock levels across facilities.",
    icon: analytics,
    route: "/inventory",
    color: "success",
  },
  {
    title: "Billing / POS",
    description: "Create invoices and handle sales.",
    icon: receipt,
    route: "/billing",
    color: "warning",
  },
];

// store card references safely
const collectCardRef = (el: any, index: number) => {
  // Vue calls this twice: once with null (unmount) and once with instance (mount)
  if (el && el.$el) {
    cards.value[index] = el.$el; // ✅ directly assign, no push()
  }
};

// animation setup
onMounted(async () => {
  await nextTick();

  cards.value.forEach((card, i) => {
    if (!card) return;

    createAnimation()
      .addElement(card)
      .duration(500)
      .delay(i * 100)
      .fromTo("opacity", "0", "1")
      .fromTo("transform", "translateY(20px)", "translateY(0)")
      .play();
  });
});
</script>

<style scoped>
.card-col {
  padding: 8px;
}

.dashboard-bg {
  --background: linear-gradient(180deg, #f9fafc 0%, #eef1f6 100%);
}

.module-card {
  opacity: 0;
  transform: translateY(20px);
}
</style>
