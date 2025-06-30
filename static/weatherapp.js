const weatherButton=document.getElementById("getWeather");
const resultdiv=document.getElementById("result");

weatherButton.addEventListener("click",()=>{ const city=document.getElementById("city").value;
        if(!city)
       {
                   resultdiv.textContent="Please enter a city name.";
                   return;
      }
    
     fetch(`/weather?city=${city}`).then((response)=>{
           if(!response.ok)
         {
              throw new Error("City not Found");
         }
        return response.json();}).then((data)=>{
         resultdiv.innerHTML=`
        <h2>Weather in ${data.city}</h2>
        <p>Temperature:${data.temperature} C deg</p>
         <p>Condition:${data.condition}</p>`; }).catch((error)=>{
       resultdiv.textContent=error.message; }); });


 
   