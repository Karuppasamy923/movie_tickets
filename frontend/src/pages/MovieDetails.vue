<template>
    <div class="max-w-480px">
        <h1 class="text-gray-900 font-bold text-[32px]">Joe</h1>
        <div class="mt-11 flex felx-row items-center justify-between">
            <div class="flex flex-col space-y-3">
                <h2 class="text-grat-700 text-base font-bold uppercase">director</h2>
                <p class="text-gray-600 text-xl font-semibold">S. Hariharan Ram</p>
            </div>
            <div class="flex flex-col space-y-3">
                <h2 class="text-grat-700 text-base font-bold uppercase">Release Date</h2>
                <p class="text-gray-600 text-xl font-semibold">24th Nov 2023</p>
            </div>
        </div>
        <div class="max-w-full">
            <div class="mx-12" v-if="current === 0">
                <div class="max-w-full flex items-center justify-center px-12 p-2 mt-7 bg-white shadow-2xl rounded">
                    <img src="data:image/jpeg;base64,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" alt="">
                </div>
                <div class="w-full flex items-center justify-center mt-7">
                    <button class="text-white bg-gray-900 size-xl w-40 rounded" @click="current=1"> Book Ticket </button>
                </div>
                <div class="flex flex-col space-y-3 mt-16">
                    <h2 class="text-grat-700 text-base font-bold uppercase">Synopsis</h2>
                    <p class="text-gray-600 text-lg font-normal">I like this movie</p>
                </div> 
            </div>
            <div v-else-if="current === 1">
                <div>
                    <h2 class="font-medium text-xl text-gray-900 mt-7">How Many Seat :</h2>
                </div>
                <div class="flex flex-col w-full space-y-3 mt-3">
                    <button size="lg" :class="{ 'bg-subtle': inx === clickedButton, 'bg-white': inx !== clickedButton }" v-for="(inx) in 8" :key="inx" class="shadow-2xl" @click="setNumberOfSeats(inx)">{{inx}}</button>
                </div>
                <div class="flex flex-row items-center justify-between mt-6">
                    <button v-if="current !== 0" class="text-white bg-gray-900 size-xl w-40 rounded" @click="current=0">Go Back</button>
                    <button v-if="current === 1" class="text-white bg-gray-900 size-xl w-40 rounded" @click="current=2">Next</button>
                </div>   
            </div>
            <div v-else-if="current === 2">
                <div class="flex flex-col space-y-4">
                     <h2 class="font-medium text-xl text-gray-900 mt-7">Date :</h2>
                     <input type="date" class="mt-3"  v-model="bookingData.date"/>
                </div>
                <div class="flex flex-col space-y-4">
                     <h2 class="font-medium text-xl text-gray-900 mt-7">Cinema & Show :</h2>
                    <div class="bg-white shadow-xl p-4 rounded flex flex-col space-y-4">
                         <h3 class="font-bold text-md text-gray-900">Sri Sakthi</h3>
                         <div class="flex flex-row space-x-2">
                            <button class=" w-20 bg-gray-400 rounded">1.00PM</button>
                            <button class=" w-20 bg-gray-400 rounded">4.30PM</button>
                         </div>
                    </div>
                    <div class="bg-white shadow-xl p-4 rounded flex flex-col space-y-4">
                        <h3 class="font-bold text-md text-gray-900">Diamond Films</h3>
                        <div class="flex flex-row space-x-2">
                           <button class=" w-20 bg-gray-400 rounded">9.00AM</button>
                           <button class=" w-20 bg-gray-400 rounded">11.00AM</button>
                        </div>
                   </div>
                </div>
                <div class="flex flex-row items-center justify-between mt-6">
                    <button v-if="current === 2" class="text-white bg-gray-900 size-xl w-40 rounded" @click="current=1">Go Back</button>
                    <button v-if="current === 2" class="text-white bg-gray-900 size-xl w-40 rounded" @click="current=3">Next</button>
                </div> 
            </div>
            <div v-else-if="current === 3" >
                <div class="flex flex-col space-y-4">
                    <h2 class="font-medium text-xl text-gray-900 mt-7">Select Seats :</h2>
               </div>
                <div class="mt-4">
                    <div class="flex flex-row" v-for="row in Object.keys(seatStructure)" :key="row">
                        <span @click="selectSeat(row,seat[0]) " v-for="seat in seatStructure[row]" :key="seat[0]" class="w-6 h-7 m-2 rounded-[2px]" :class="seat[1] === 'Available' ? 'bg-blue-300' : seat[1] === 'Selected' ? 'bg-blue-600': 'bg-blue-300' ">
                        </span>
                    </div>
                </div>
                <div class="flex flex-row items-center justify-between mt-6">
                    <button v-if="current === 3" class="text-white bg-gray-900 size-xl w-40 rounded" @click="current=2">Go Back</button>
                    <button v-if="current === 3" class="text-white bg-gray-900 size-xl w-40 rounded" @click="current=4">Confirm Ticket</button>
                </div> 
            </div>
            <div v-else-if="current === 4">
                <div class="w-full flex flex-col items-center justify-center mt-7">
                    <img src="https://www.youtube.com/s/gaming/emoji/7ff574f2/emoji_u1f37f.png" alt="">
                    <h2 class="font-medium text-xl text-gray-900 mt-7">Enjoy The Movie!</h2>
                </div>
                 <div class="flex flex-row items-center justify-center mt-6">
                    <button v-if="current === 4" class="text-white bg-gray-900 size-xl w-40 rounded" @click="current=0">Home</button>
                </div> 
            </div>    
        </div>
    </div>
</template>

<script setup>
    import {ref, reactive} from "vue";

    const today=new Date().toISOString().substr(0,10);
    const current = ref(0);
    const bookingData = reactive({
        numberOfSeats : 0,
        date: today,
        seats :[],
        selectedSeats :[],
    })
    const seatStructure=reactive(getSeatStructure(
        ['A','B','C','D','E'],
        [1,2,3,4,5,6,7,8]
        ))
    function setNumberOfSeats(n){
        bookingData.numberOfSeats = n;
    }
    function getSeatStructure(alphabets,numbers){
        const structure={}
        for(const alphabet of alphabets){
            structure[alphabet]=[]
            for(const number of numbers){
                structure[alphabet].push([number,'Available'])
            }
        }
        return structure
    }
    function selectSeat(row,number){
        const seat=seatStructure[row].find((seat)=>seat[0]=== number)
        seat[1]='Selected'
        bookingData.selectedSeats.push(`${row}${number}`)
    }
    // export default {
    //     name:'moviedetails',
    // }
</script>

<style scoped>
    
</style>