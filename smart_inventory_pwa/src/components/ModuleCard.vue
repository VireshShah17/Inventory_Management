<template>
    <ion-card button @click="navigate" class="module-card" :style="cardStyle">
        <ion-card-content class="ion-text-center">
            <ion-icon :icon="icon" size="large" class="module-icon"></ion-icon>
            <ion-card-title class="ion-margin-top">{{ title }}</ion-card-title>
            <p class="muted">{{ description }}</p>
        </ion-card-content>
    </ion-card>
</template>

<script setup lang="ts">
import { IonCard, IonCardContent, IonCardTitle, IonIcon } from "@ionic/vue";
import { useRouter } from "vue-router";
import { computed } from "vue";

const props = defineProps<{
    title: string;
    description: string;
    icon: any;
    route: string;
    color?: string;
}>();

const router = useRouter();
const navigate = () => router.push(props.route);

// gradient backgrounds per color
const gradients: Record<string, string> = {
    primary: "linear-gradient(135deg, #4285F4, #1A73E8)",
    tertiary: "linear-gradient(135deg, #8E2DE2, #4A00E0)",
    success: "linear-gradient(135deg, #00C851, #007E33)",
    warning: "linear-gradient(135deg, #FFB300, #FF8C00)",
};

const cardStyle = computed(() => ({
    background: gradients[props.color || "primary"],
}));
</script>

<style scoped>
.module-card {
    height: 180px;
    display: flex;
    align-items: center;
    justify-content: center;
    border-radius: 16px;
    transition: transform 0.2s ease, box-shadow 0.2s ease;
    color: #fff;
    box-shadow: 0 8px 16px rgba(0, 0, 0, 0.12);
}

.module-card:hover {
    transform: translateY(-6px);
    box-shadow: 0 12px 22px rgba(0, 0, 0, 0.18);
}

.module-icon {
    font-size: 40px;
    color: #fff;
}

ion-card-title {
    font-weight: 600;
    font-size: 1.2rem;
}

.muted {
    opacity: 0.9;
    font-size: 0.9rem;
    margin-top: 8px;
}
</style>
