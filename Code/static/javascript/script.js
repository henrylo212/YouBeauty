const wrapperLocation = document.querySelector(".wrapper-location"),
selectBtn = wrapperLocation.querySelector(".select-btn"),
searchInp = wrapperLocation.querySelector("input"),
options = wrapperLocation.querySelector(".options");

let countries = ["Camperdown", "Darlington", "Chippendale", "Hornsby", "Epping", "Strathfield", "Burwood", "Chatswood"]

function addCountry() {
    options.innerHTML = "";
    countries.forEach(country => {
        let li = `<li onclick="updateName(this)">${country}</li>`;
        options.insertAdjacentHTML("beforeend", li);
    });
}
addCountry();

function updateName(selectedLi) {
    searchInp.value = "";
    addCountry();
    wrapperLocation.classList.remove("active");
    selectBtn.firstElementChild.innerText = selectedLi.innerText;
}

searchInp.addEventListener("keyup", () => {
    let arr= [];
    let searchedVal = searchInp.value.toLowerCase();
    arr = countries.filter(data => {
        return data.toLowerCase().startsWith(searchedVal);
    }).map(data => `<li onclick="updateName(this)">${data}</li>`).join("");
    options.innerHTML = arr;
});

selectBtn.addEventListener("click", () => {
    wrapperLocation.classList.toggle("active");
    wrapperService.classList.remove("active");
    wrapperTime.classList.remove("active");
});

// Service Search
const wrapperService = document.querySelector(".wrapper-service"),
serviceBtn = wrapperService.querySelector(".service-btn"),
searchInpService = wrapperService.querySelector("input"),
optionsService = wrapperService.querySelector(".options");

let services = ["Basic Cut", "Blowdry", "Wash and Cut", "Perm", "Bleach", "Dye", "Straighten", "Curl"]

function addService() {
    optionsService.innerHTML = "";
    services.forEach(service => {
        let li = `<li onclick="updateServiceName(this)">${service}</li>`;
        optionsService.insertAdjacentHTML("beforeend", li);
    });
}
addService();

function updateServiceName(selectedLi) {
    searchInpService.value = "";
    addService();
    wrapperService.classList.remove("active");
    serviceBtn.firstElementChild.innerText = selectedLi.innerText;
}

searchInpService.addEventListener("keyup", () => {
    let arr= [];
    let searchedVal = searchInpService.value.toLowerCase();
    arr = services.filter(data => {
        return data.toLowerCase().startsWith(searchedVal);
    }).map(data => `<li onclick="updateServiceName(this)">${data}</li>`).join("");
    optionsService.innerHTML = arr;
});

serviceBtn.addEventListener("click", () => {
    wrapperService.classList.toggle("active");
    wrapperLocation.classList.remove("active");
    wrapperTime.classList.remove("active");
});


// Time Search
const wrapperTime = document.querySelector(".wrapper-time"),
timeBtn = wrapperTime.querySelector(".time-btn"),
searchInpTime = wrapperTime.querySelector("input"),
optionsTime = wrapperTime.querySelector(".options");

let times = ["9am", "10am", "11am", "12pm", "1pm", "2pm", "3pm", "4pm", "5pm"]

function addTime() {
    optionsTime.innerHTML = "";
    times.forEach(time => {
        let li = `<li onclick="updateTimeName(this)">${time}</li>`;
        optionsTime.insertAdjacentHTML("beforeend", li);
    });
}
addTime();

function updateTimeName(selectedLi) {
    searchInpTime.value = "";
    addTime();
    wrapperTime.classList.remove("active");
    timeBtn.firstElementChild.innerText = selectedLi.innerText;
}

searchInpTime.addEventListener("keyup", () => {
    let arr= [];
    let searchedVal = searchInpTime.value.toLowerCase();
    arr = times.filter(data => {
        return data.toLowerCase().startsWith(searchedVal);
    }).map(data => `<li onclick="updateTimeName(this)">${data}</li>`).join("");
    optionsTime.innerHTML = arr;
});

timeBtn.addEventListener("click", () => {
    wrapperTime.classList.toggle("active");
    wrapperLocation.classList.remove("active");
    wrapperService.classList.remove("active");
});