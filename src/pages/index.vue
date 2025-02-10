<template>
    <div>
        <section class="relative h-screen flex flex-col items-center justify-center text-center text-white">
            <div class="video-docker absolute top-0 left-0 w-full h-full overflow-hidden">
                <video class="min-w-full min-h-full absolute object-cover"
                    src="../assets/home_video.mp4"
                    type="video/mp4" autoplay muted loop></video>
            </div>
            <div class="grid grid-cols-3 gap-x-12 z-20 my-16">
                <div
                    @click="selectOption('lodging')"
                    :class="[
                        'bg-gray-100 flex justify-center items-center rounded-xl border-4 transition hover:scale-105',
                        selectedOption === 'lodging' ? 'border-blue-400' : 'border-white'
                    ]"
                >
                    <img src="../assets/home.png" class="w-24">
                </div>
                <div
                    @click="selectOption('restaurant')"
                    :class="[
                        'bg-gray-100 flex justify-center items-center rounded-xl border-4 transition hover:scale-105',
                        selectedOption === 'restaurant' ? 'border-blue-400' : 'border-white'
                    ]"
                >
                    <img src="../assets/activity.png" class="w-16">
                </div>
                <div
                    @click="selectOption('transport')"
                    :class="[
                        'bg-gray-100 flex justify-center items-center rounded-xl border-4 transition hover:scale-105',
                        selectedOption === 'transport' ? 'border-blue-400' : 'border-white'
                    ]"
                >
                    <img src="../assets/avion.png" class="w-20">
                </div>
            </div>
            <div class="video-content space-y-2 z-10">
                <transition name="fade">
                    <h1 class="font-extrabold text-6xl text-gray-100" v-if="selectedOption" key="title">
                        Book your <span>{{ selectedOption }}</span>
                    </h1>
                </transition>
                <h3 class="font-light text-3xl">with Booking.yeaaaa</h3>
            </div>
            <div class="relative mt-20 z-40">
                <input type="text" class="h-14 w-96 pr-8 pl-5 rounded z-0 text-gray-700" placeholder="Search anything...">
                <div class="absolute top-4 right-3">
                    <i class="fa fa-search text-gray-400 z-20 hover:text-gray-500"></i>
                </div>
            </div>
        </section>
    </div>
</template>

<script>
export default {
    data() {
        return {
            selectedOption: 'lodging', 
        };
    },
    methods: {
        selectOption(option) {
            this.selectedOption = option; 
        },
    },
};
</script>

<style>
.video-docker video {
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
}

.video-docker::after {
    content: "";
    position: absolute;
    width: 100%;
    height: 100%;
    top: 0;
    left: 0;
    background: rgba(0, 0, 0, 0.4);
    z-index: 1;
}

/* Transition for the title */
.fade-enter-active, .fade-leave-active {
    transition: opacity 0.3s ease-in-out;
}
.fade-enter-from, .fade-leave-to {
    opacity: 0;
}
</style>
