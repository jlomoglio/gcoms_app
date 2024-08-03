/*******************************************************************************************************
 * regions MAP
 * ****************************************************************************************************/

// ROAD MAP: https://tile.openstreetmap.org/{z}/{x}/{y}.png
// SATALITE MAP: https://basemap.nationalmap.gov/arcgis/rest/services/USGSImageryOnly/MapServer/tile/{z}/{y}/{x}

// must use var instead of const or let, otherwise HTMX wont reinitilize the map
let regionMap = L.map('regions-map').setView([28.01888, -82.11469], 3); //starting position
let bounds = new L.LatLngBounds(new L.LatLng(28.01888, -82.11469), new L.LatLng(61.2, 2.5));
let myAPIKey = 'ac2f04a36afe49d2a5b7ea34eab0cead' // https://www.geoapify.com/

$(window).on("resize", function () { $("#regions-map").height($(window).height()); regionMap.invalidateSize(); }).trigger("resize");

console.log("Regions JS has been loaded ----------------->")

function loadRoadMap() {
    //console.log("regions_vals --> " + document.getElementById("regions_vals").value)
    
    /** MAP MARKERS */
    let regionIcon
    let regions = document.getElementById("regions_vals").value

    const response = fetch('/regions')
        .then(response => {
            if (!response) {
                console.error(err.message);
            }

            console.log("response --> " + JSON.stringify(response, null, 2))

            return response.json();
        })
        .then(data => {
            /** MAP MARKERS */
            let regionIcon

            console.log("data --> " + JSON.stringify(data, null, 2))

            for (let i=0; i < data.length; i++) {
                let marker = L.marker([data[i].reg_lat, data[i].reg_lng])
                    .bindTooltip(data[i].reg_name, { permanent: true })
                    .openTooltip()
                    .addTo(regionMap)
            }

            /** MAP TILES */
            //API KEY: c03aea95c948480d8ec40331f8012ff1 || https://www.geoapify.com/geocoding-api
            L.tileLayer('https://maps.geoapify.com/v1/tile/osm-bright-smooth/{z}/{x}/{y}@2x.png?apiKey=' + myAPIKey, {
                minZoom: 3,
                maxZoom: 19.5
            }).addTo(regionMap);

            /** MAP BOUNDRY */
            let southWest = L.latLng(-89.98155760646617, -240);
            let northEast = L.latLng(89.99346179538875, 240);
            let bounds = L.latLngBounds(southWest, northEast);

            regionMap.setMaxBounds(bounds);
            regionMap.on('drag', function() {
                regionMap.panInsideBounds(bounds, { animate: true });
            });
        })
    
}

loadRoadMap()


function loadSatMap() {

    /** GET MAP MARKERS DATA */
    const response = fetch('/regions/map')
        .then(response => {
            if (!response) {
                console.error(err.message);
            }

            return response.json();
        })
        .then(data => {
            /** MAP MARKERS */
            let regionIcon

            for (let i=0; i < data.length; i++) {
                let marker = L.marker([data[i].reg_lat, data[i].reg_lng])
                    .bindTooltip(data[i].reg_name, { permanent: true })
                    .openTooltip()
                    .addTo(regionMap)
            }

            /** MAP TILES */
            L.tileLayer('https://basemap.nationalmap.gov/arcgis/rest/services/USGSImageryOnly/MapServer/tile/{z}/{y}/{x}', {
                minZoom: 3,
                maxZoom: 19.5
            }).addTo(regionMap);

            /** MAP BOUNDRY */
            let southWest = L.latLng(-89.98155760646617, -240);
            let northEast = L.latLng(89.99346179538875, 240);
            let bounds = L.latLngBounds(southWest, northEast);

            regionMap.setMaxBounds(bounds);
            regionMap.on('drag', function() {
                regionMap.panInsideBounds(bounds, { animate: true });
            });
        })
}

function showOnMap(lat, lng) {

    /** GET MAP MARKERS DATA */
    const response = fetch('/regions/map')
        .then(response => {
            if (!response) {
                console.error(err.message);
            }
            return response.json();
        })
        .then(data => {
            /** MAP MARKERS */
            let regionIcon

            for (let i=0; i < data.length; i++) {
                if(data[i].reg_type == "Manufacturing") {
                    regionIcon = L.divIcon({
                        className: 'custom-div-icon',
                        html: "<div style='background-color:#4838cc;' class='marker-pin'></div><i class='fa-solid fa-industry'></i>",
                        iconSize: [60, 42],
                        iconAnchor: [30, 42]
                    });
                }
                else if(data[i].reg_type == "Housing") {
                    regionIcon = L.divIcon({
                        className: 'custom-div-icon',
                        html: "<div style='background-color:#4838cc;' class='marker-pin housing-pin'></div><i class='fa-solid fa-house awesome text-[blue]'>",
                        iconSize: [60, 42],
                        iconAnchor: [30, 42]
                    });
                }
                else if(data[i].reg_type == "Farming") {
                    regionIcon = L.divIcon({
                        className: 'custom-div-icon',
                        html: "<div style='background:#298608 !important;' class='marker-pin farming-pin'></div><i class='fa fa-seedling awesome !text-[yellow]'>",
                        iconSize: [60, 42],
                        iconAnchor: [30, 42]
                    });
                }
                else if(data[i].reg_type == "Energy") {
                    regionIcon = L.divIcon({
                        className: 'custom-div-icon',
                        html: "<div style='background-color:#4838cc;' class='marker-pin'></div><i class='fa fa-atom awesome'>",
                        iconSize: [60, 42],
                        iconAnchor: [30, 42]
                    });
                }
                else if(data[i].reg_type == "Remote Office") {
                    regionIcon = L.divIcon({
                        className: 'custom-div-icon',
                        html: "<div style='background-color:#4838cc;' class='marker-pin'></div><i class='fa-solid fa-house awesome'>",
                        iconSize: [60, 42],
                        iconAnchor: [30, 42]
                    });
                }

                L.Icon.Default.prototype.options = {
                    iconUrl: '',
                    iconSize: [0, 0],
                    iconAnchor: [0, 0]
                }
            }

            var marker = L.marker(lat, lng, { icon: regionIcon, title: '' })
            regionMap.flyTo([lat, lng], 7);
        })
}

function resetMap(lat, lng) {

    /** GET MAP MARKERS DATA */
    const response = fetch('/regions/map')
        .then(response => {
            if (!response) {
                console.error(err.message);
            }
            return response.json();
        })
        .then(data => {
            /** MAP MARKERS */
            let regionIcon

            for (let i=0; i < data.length; i++) {
                if(data[i].region_type == "Manufacturing") {
                    regionIcon = L.divIcon({
                        className: 'custom-div-icon',
                        html: "<div style='background-color:#4838cc;' class='marker-pin'></div><i class='fa-solid fa-industry'></i>",
                        iconSize: [60, 42],
                        iconAnchor: [30, 42]
                    });
                }
                else if(data[i].region_type == "Housing") {
                    regionIcon = L.divIcon({
                        className: 'custom-div-icon',
                        html: "<div style='background-color:#4838cc;' class='marker-pin housing-pin'></div><i class='fa-solid fa-house awesome text-[blue]'>",
                        iconSize: [60, 42],
                        iconAnchor: [30, 42]
                    });
                }
                else if(data[i].region_type == "Farming") {
                    regionIcon = L.divIcon({
                        className: 'custom-div-icon',
                        html: "<div style='background:#298608 !important;' class='marker-pin farming-pin'></div><i class='fa fa-seedling awesome !text-[yellow]'>",
                        iconSize: [60, 42],
                        iconAnchor: [30, 42]
                    });
                }
                else if(data[i].region_type == "Energy") {
                    regionIcon = L.divIcon({
                        className: 'custom-div-icon',
                        html: "<div style='background-color:#4838cc;' class='marker-pin'></div><i class='fa fa-atom awesome'>",
                        iconSize: [60, 42],
                        iconAnchor: [30, 42]
                    });
                }
                else if(data[i].region_type == "Remote Office") {
                    regionIcon = L.divIcon({
                        className: 'custom-div-icon',
                        html: "<div style='background-color:#4838cc;' class='marker-pin'></div><i class='fa-solid fa-house awesome'>",
                        iconSize: [60, 42],
                        iconAnchor: [30, 42]
                    });
                }

                L.Icon.Default.prototype.options = {
                    iconUrl: '',
                    iconSize: [0, 0],
                    iconAnchor: [0, 0]
                }
            }

            var marker = L.marker(lat, lng, { icon: regionIcon, title: '' })
            regionMap.flyTo([28.01888, -82.11469], 3);
        })
}
/*******************************************************************************************************
 * END regions MAP
 * ****************************************************************************************************/



/*******************************************************************************************************
 * regions COORDS
 * ****************************************************************************************************/
function getCoords() {
    var address = $("#region_address").val()
    var city = $("#region_city").val()
    var state = $("#region_state").val()
    var zip = $("#region_zip").val()

    //var fullAddress = address + ', ' + city + ' ' + state + ' ' + zip
    var fullAddress = '599 eagles nest, plant city fl 33565'


    // Instantiate a map and platform object:
    var platform = new H.service.Platform({
        'apikey': 'VrAphDSRziIUkYqjpF3Q-Oi5QCJu9Uu3niiKGCQZ75E'
    });

    // Get an instance of the geocoding service:
    var service = platform.getSearchService();

    // Call the geocode method with the geocoding parameters,
    // the callback and an error callback function (called if a
    // communication error occurs):
    service.geocode({ q: fullAddress }, (result) => {

        result.items.forEach((item) => {
            document.getElementById("lat").value = item.position.lat
            document.getElementById("lng").value = item.position.lng

            console.log("item ->> " + JSON.stringify(item, null, 3))
            //console.log("item  TIME ZONE ->> " + JSON.stringify(item.timeZone.utcoffset, null, 2))
            console.log("item  LAT ->> " + JSON.stringify(item.position.lat, null, 2))
            console.log("item  LNG ->> " + JSON.stringify(item.position.lng, null, 2))
        });

        getTimeZone(fullAddress)
    }, alert);
}
/*******************************************************************************************************
 * END regions COORDS
 * ****************************************************************************************************/



/*******************************************************************************************************
 * regions TIME ZONE
 * ****************************************************************************************************/
function getTimezone () {
    const apiKey = 'VrAphDSRziIUkYqjpF3Q-Oi5QCJu9Uu3niiKGCQZ75E'

    $.getJSON('https://geocode.search.hereapi.com/v1/geocode?q=' + fullAddress + '&show=tz&apiKey=' + apiKey, function(tz) {
        document.getElementById("loc_tz_name").value = tz.items[0].timeZone.name
        document.getElementById("loc_tz_utcoffset").value = tz.items[0].timeZone.utcOffset
    })
}
/*******************************************************************************************************
 * END regions TIME ZONE
 * ****************************************************************************************************/





function getLocationData() {
    const API_KEY = 'c03aea95c948480d8ec40331f8012ff1'
    const address = $("#loc_address").val()
    const city = $("#loc_city").val()
    const query = address + ' ' + city

    fetch("https://api.geoapify.com/v1/geocode/search?text=" + query + "&format=json&apiKey=" + API_KEY)
        .then(response => response.json())
        .then(result => {
            console.log("result --> " + JSON.stringify(result.results, null, 2))
            // console.log("LAT --> " + result.results.lat)
            let r = result.results
            //console.log("LON --> " + r[0].lon)
            $("#loc_lat").val(r[0].lat)
            $("#loc_lng").val(r[0].lon)
            $("#loc_state").val(r[0].state_code)
            $("#loc_zip").val(r[0].postcode)
            $("#loc_tz_name").val(r[0].timezone.name)
            $("#loc_tz_utcoffset").val(r[0].timezone.offset_STD + ' ' + r[0].timezone.abbreviation_STD)
            $("#loc_country").val(r[0].country)

            //console.log("r --> " + JSON.stringify(r, null, 2))
        })
        .catch(error => console.log('error', error));
}




