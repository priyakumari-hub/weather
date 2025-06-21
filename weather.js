const apikey="REDACTED_API_KEY_1";
const weatherButton=document.getElementById("getWeather");
const resultdiv=document.getElementById("result");

weatherButton.addEventListener("click",()=>{ const city=document.getElementById("city").value;
        if(!city)
       {
                   resultdiv.textContent="Please enter a city name.";
                   return;
      }
    
     fetch(`https://api.openweathermap.org/data/2.5/weather?q=${city}&appid=${apikey}&units=metric`).then((response)=>{
           if(!response.ok)
         {
              throw new Error("City not Found");
         }
        return response.json();}).then((data)=>{const{main,weather}=data;
       resultdiv.innerHTML=`
        <h2>Weather in ${city}</h2>
        <p>Temperature:${main.temp} C deg</p>
         <p>Condition:${weather[0].description}</p>`; }).catch((error)=>{
       resultdiv.textContent=error.message; }); });