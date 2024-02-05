<template>
    <div class="max-w-480px" v-if="!movieResource.loading && movieResource.doc">
        <div v-if="current !== 4">
            <h1 class="text-gray-900 font-bold text-[32px]">{{ movieDoc.title }}</h1>
            <div class="mt-11 flex flex-row items-center justify-between">
                <div class="flex flex-col space-y-3">
                    <h2 class="text-grat-700 text-base font-bold uppercase">Director</h2>
                    <p class="text-gray-600 text-xl font-semibold">{{ movieDoc.director }}</p>
                </div>
                <div class="flex flex-col space-y-3">
                    <h2 class="text-grat-700 text-base font-bold uppercase">Release Date</h2>
                    <p class="text-gray-600 text-xl font-semibold">{{ movieDoc.release_date }}</p>
                </div>
            </div>
        </div>
        <div class="max-w-full">
            <div class="mx-12 flex flex-col items-center justify-center" v-if="current === 0">
                <div class="w-[340px] flex items-center justify-center px-12 p-2 mt-7 bg-white shadow-2xl rounded">
                    <img class="flex w-[300px] h-[340px]" :src="movieDoc.poster" alt="">
                </div>
                <div class="w-full flex items-center justify-center mt-7">
                    <Button size="lg" variant="solid" class="text-white bg-gray-900 size-xl w-40 rounded" @click="current = 1">Book Ticket</Button>
                </div>
                <div class="flex flex-col space-y-3 mt-16">
                    <h2 class="text-grat-700 text-base font-bold uppercase">Synopsis</h2>
                    <p class="text-gray-600 text-lg font-normal">{{movieDoc.synopsis}}</p>
                </div>
            </div>
            <div v-else-if="current === 1">
                <div>
                    <h2 class="font-medium text-xl text-gray-900 mt-7">How Many Seat :</h2>
                </div>
                <div class="flex flex-col w-full space-y-3 mt-3">
                    <Button size="lg" 
                    :variant="inx === bookingData.numberOfSeats ? 'subtle':'white'" 
                    class="shadow-lg"
                     v-for="(inx) in 8" :key="inx" 
                     @click="setNumberOfSeats(inx)">{{inx}}</Button>
                </div>
                <!-- <div class="flex flex-row items-center justify-between mt-6">
                    <button v-if="current !== 0" class="text-white bg-gray-900 size-xl w-40 rounded" @click="current=0">Go Back</button>
                    <button v-if="current === 1" class="text-white bg-gray-900 size-xl w-40 rounded" @click="current=2">Next</button>
                </div>    -->
            </div>
            <div v-else-if="current === 2">
                <div class="flex flex-col space-y-4">
                     <h2 class="font-medium text-xl text-gray-900 mt-7">Date :</h2>
                     <input type="date" class="mt-3"  v-model="bookingData.date"/>
                </div>
                <div class="flex flex-col space-y-4">
                    <h2 class="font-medium text-xl text-gray-900 mt-7">Cinema & Show :</h2>
                      <div v-for="theater in Object.keys(theaters.data)" :key="theater" class="bg-white shadow-xl p-4 rounded flex flex-col space-y-4"> 
                         <h3 class="font-bold text-md text-gray-900">{{theater}}</h3>
                         <div class="flex flex-row space-x-2">
                            <Button
                            v-for="show in theaters.data[theater]" 
                            :key="show.name"
                             @click="handleTheaterSelection(theater,show.start_time)" 
                            size="sm"
                            :variant="show.name === bookingData.show?'subtle':'outline'">{{show.start_time}}
                            
                            </Button>
                         </div>
                    </div>
                </div> 
                <!-- <div class="flex flex-row items-center justify-between mt-6">
                    <button v-if="current === 2" class="text-white bg-gray-900 size-xl w-40 rounded" @click="current=1">Go Back</button>
                    <button v-if="current === 2" class="text-white bg-gray-900 size-xl w-40 rounded" @click="current=3">Next</button>
                </div>  -->
            </div>
            <div v-else-if="current === 3" >
                <div class="flex flex-col space-y-4">
                    <h2 class="font-medium text-xl text-gray-900 mt-7">Select Seats :</h2>
               </div>
                <div class="mt-4">
                    <div class="flex flex-row" v-for="row in Object.keys(seatStructure)" :key="row">
                        <span @click="selectSeat(row,seat[0]) " 
                        v-for="seat in seatStructure[row]" :key="seat[0]" 
                        class="w-6 h-7 m-2 rounded-[2px] "

                        :class="[
                        seat[1] === 'Available' 
                        ? 'bg-blue-300' 
                        : seat[1] === 'Selected' 
                        ? 'bg-blue-600'
                        : 'bg-blue-300',
                        hasSelectedCorrectNumberOfSeats
                        ? 'cursor-not-allowed'
                        : 'cursor-pointer', 
                        ]">
                        </span>
                    </div>
                </div>
                <!-- <div class="flex flex-row items-center justify-between mt-6">
                    <button v-if="current === 3" class="text-white bg-gray-900 size-xl w-40 rounded" @click="current=2">Go Back</button>
                    <button v-if="current === 3" class="text-white bg-gray-900 size-xl w-40 rounded" @click="current=4">Confirm Ticket</button>
                </div>  -->
            </div>
            <div v-else-if="current === 4">
                <div class="w-full flex flex-col items-center justify-center mt-7">
                    <img src="https://www.youtube.com/s/gaming/emoji/7ff574f2/emoji_u1f37f.png" alt="">
                    <h2 class="font-medium text-xl text-gray-900 mt-7">Enjoy The Movie!</h2>
                </div>
                <table class="mt-5">
                    <tr>
                        <td><label>Movie Name</label></td>
                        <td><h1>: {{ movieDoc.title }}</h1></td>
                    </tr>
                    <tr>
                        <td><label>Theater Name</label></td>
                        <td><h1>: {{ bookingData.theater }}</h1></td>
                    </tr>
                    <tr>
                        <td><label>Show Date</label></td>
                        <td><h1>: {{ bookingData.date }}</h1></td>
                    </tr>
                    <tr>
                        <td><label>Show Time</label></td>
                        <td><h1>: {{ bookingData.show }}</h1></td>
                    </tr>
                    <tr>
                        <td><label>Number Of Seats Booked</label></td>
                        <td><h1>: {{ bookingData.numberOfSeats }}</h1></td>
                    </tr>
                    <tr>
                        <td><label>Booked Seat's Number</label></td>
                        <td><h1>: {{ `${bookingData.selectedSeats.join(', ')}` }}</h1></td>
                    </tr>
                </table>
                <div class="flex flex-row items-center justify-center mt-6">
                    <button v-if="current === 4" class="text-white bg-gray-900 size-xl w-40 rounded" @click="current=0">Home</button>
                </div> 
            </div>   
        </div>
        <div class="flex flex-row items-center justify-between mt-6">
            <Button size="lg"
            variant="subtle"
            v-if="current !== 0 && current !==4"
            @click="current--">Go Back</Button>
            <Button size="lg"
            variant="solid"
            :disabled="!NextButtonEnabled"
            v-if="current !== 0 && current !==4"
            @click="hanndleNext()">Next</Button>
        </div>  
    </div>
</template>

<script setup>
import { ref, reactive, computed } from "vue";
import { createDocumentResource, createListResource } from "frappe-ui";

const props = defineProps({
    movieName:{
        type: String,
        required: true,
    },
})

const movieResource = createDocumentResource({
  doctype: "Movie",
  name: props.movieName,
  onSuccess(doc) {
    console.log(doc);
  },
  auto: true,
});
const movieDoc = computed(() => movieResource.doc);

const theaters = createListResource({
    doctype:"Theater Show",
    fields: ['theater', 'start_time'],
    auto:true,
    transform: (shows) => {
        const groupedShows ={}
        for(const show of shows){
            if(!groupedShows[show.theater]){
                groupedShows[show.theater]=[]
            }
            groupedShows[show.theater].push(show)
        }
     return groupedShows   
    },
})

const  movieBooking = createListResource({
    doctype:"Ticket Booking",
    insert:{
        onSuccess(){
            console.log("Booking created")
            current.value++
        }
    }
})

const today = new Date().toISOString().substr(0, 10);
const current = ref(0);
const bookingData = reactive({
  numberOfSeats: 0,
  date: today,
  seats: [],
  selectedSeats: [],
  show: null,
  theater:null
});
const seatStructure = reactive(getSeatStructure(
  ['A', 'B', 'C', 'D', 'E'],
  [1, 2, 3, 4, 5, 6, 7, 8]
));
function setNumberOfSeats(n) {
  bookingData.numberOfSeats = n;
}
function getSeatStructure(alphabets, numbers) {
  const structure = {};
  for (const alphabet of alphabets) {
    structure[alphabet] = [];
    for (const number of numbers) {
      structure[alphabet].push([number, 'Available']);
    }
  }
  return structure;
}
function selectSeat(row, number) {
  if (hasSelectedCorrectNumberOfSeats.value) {
    return;
  }
  const seat = seatStructure[row].find((seat) => seat[0] === number);
  seat[1] = 'Selected';
  bookingData.selectedSeats.push(`${row}${number}`);
}

const hasSelectedCorrectNumberOfSeats = computed(() => {
  return bookingData.selectedSeats.length === bookingData.numberOfSeats;
});

console.log(movieDoc.title);

const NextButtonEnabled = computed(() => {
    if(current.value === 1){
        console.log(bookingData.numberOfSeats)
        return bookingData.numberOfSeats
    }else if(current.value === 2){
        console.log(bookingData.show)
        console.log(bookingData.date)
        return bookingData.date && bookingData.show !== null
    }else if(current.value === 3){
        return hasSelectedCorrectNumberOfSeats.value
    }
})

function hanndleNext(){
    if (current.value != 3){
        current.value++
        return
    }else{
        console.log(bookingData.show)
        movieBooking.insert.submit({
            movie: props.movieName,
            date: bookingData.date,
            show: bookingData.show,
            selected_seats: JSON.stringify(bookingData.selectedSeats),
            number_of_tickets:bookingData.numberOfSeats,
        })
    }
}
function handleTheaterSelection(theater,startTime){
    bookingData.show = startTime;
    bookingData.theater= theater;
}
</script>

<style scoped>

</style>
