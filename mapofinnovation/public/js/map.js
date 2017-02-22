
var map = L.map('map', {
	minZoom: 2,
	worldCopyJump: true
}).setView([20,0], 2);
L.tileLayer('https://api.mapbox.com/styles/v1/albiebrown/civehqtub00022ikc7sgmp1n2/tiles/256/{z}/{x}/{y}?access_token=pk.eyJ1IjoiYWxiaWVicm93biIsImEiOiJjaXZlaDh1a2MwMWl6MnlwZDJldzFvYjNxIn0.d04rCBRG42H2JkkiID2qpA', {
    attribution: 'Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors, <a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="http://mapbox.com">Mapbox</a>',
    maxZoom: 18,
}).addTo(map);

var markerClusters = L.markerClusterGroup({
		spiderfyOnMaxZoom: true,
    showCoverageOnHover: false,
    zoomToBoundsOnClick: true,
    maxClusterRadius: 40
});

var allTypes = {
	"hub": "Hub",
	"workshop": "Workshop",
	"event": "Event",
	"art gallery": "Art Gallery",
	"gallery": "Art Gallery",
	"factory": "Factory",
	"retail": "Retail",
	"virtual": "Virtual",
	"ecovillage": "Ecovillage",
	"cluster": "Cluster",
	"library": "Library",
	"lab": "Lab",
	"": "Hub"
};

var myIcon = L.icon({
    iconUrl: '../assets/pin1.png',
    iconSize: [23, 30],
    iconAnchor: [11, 29],
    popupAnchor: [0, -30]
});

var allMarkers = [];
var noLocation = [];
var placeInfoRequired = ['name', 'city', 'country', 'primary_type', 'theme'];

$.get('baseapi/getAllSpaces',{cache: true}, function(spaces) {
	buildMarkers(spaces);
});

function buildMarkers(allSpaces) {
	$(".loader-text").text("Building Map . . .");
	for (i=0; i<allSpaces.length; ++i) {	
		var space = allSpaces[i];
		if (space.latitude && space.longitude) {
			try {
				var marker = L.marker([space.latitude, space.longitude], {icon: myIcon});
				var placeData = {}
				placeInfoRequired.forEach(function(key) {
					if (typeof space[key] !== 'undefined') {
						if (key == 'primary_type') {
							placeData['type'] = space[key].toLowerCase().trim();
						} else if (key == 'theme') {
							placeData['theme'] = space[key].toLowerCase().trim();
						} else {
							placeData[key] = space[key];
						}
					}	
				});
				marker.placeData = placeData;
				var popup = createPopup(space);
				marker.bindPopup(popup, {minWidth: "250"});
				markerClusters.addLayer(marker);
				allMarkers.push(marker);
			} catch (e) {
				// console.log("TypeError: " + space.name);
				// console.log(e.message);
			}
		} else {
			noLocation.push(space);
		}
	}
	map.addLayer(markerClusters, {"chunkedLoading": true});
	$("#loading").fadeOut();
}

function createPopup(space) {
	
	var popupText = "<div class='popup-header'>";
	popupText += "<h3>"+space.name+"</h3>";
	popupText += "</div>";
	popupText += "<p><img src='../assets/pin2.png' height='14' class='popup-location-text'><span style='margin-bottom:3px;position:fixed;'>";

	if (space.city != "") {
		popupText += space.city+", "+space.country;
 	} else {
		popupText += space.country;
 	}
	popupText += "</span></p>"+"<a class='popup-website-link' target='_blank' href='http://"+space.primary_website+"'>"+space.primary_website+"</a><div class='popup-type-container'>"; 

	var types = [];
	if (space.primary_type.trim() != "" && types.indexOf(space.primary_type) === -1) {
		types.push(space.primary_type);
	} else {
		console.log("No primary type: " + space.name);
	}
	if (space.multitypes != "") {
		var multis = space.types_multiple.split(", ");
		for (j=0; j<multis.length; j++) {
		if (multis[j].toLowerCase().trim() != space.primary_type.trim().toLowerCase()) {
				types.push(multis[j]);
			}
		}
	}
	for (k=0; k<types.length; k++) {
		var color = "";
		var type = types[k];
		type = allTypes[type.toLowerCase().trim()]
		if (type) {
				popupText += "<div class='popup-type-color " + type.toLowerCase().replace(" ", "-")+"-color" + "'></div><span class='popup-type-text'>"
							+type+"</span>";
		} else {
			console.log("Unknown type: "+types[k]);
		}
 	}
	popupText += "</div>";
	popupText += "<p>"+space.description+"</p>";			
	popupText += "<a href='"+space.wiki+"'><img src='../assets/space_page.png' class='space-page-button'></a>";

	return popupText;
 }
 
var appliedFilters = [];

function runFilter() {	
	markerClusters.clearLayers();
	for(var i = 0; i < allMarkers.length; i++) {
		if(matchesFilter(allMarkers[i])) {
			markerClusters.addLayer(allMarkers[i]);
		}
	}
	map.addLayer(markerClusters, {"chunkedLoading": true});
}

function matchesFilter(marker) {
	console.log(appliedFilters[0][0]);
	for(var i = 0; i < appliedFilters.length; i++) {
		if(appliedFilters[i][1] == 'all') {
			return true;
		}

		if(!marker.placeData[appliedFilters[i][0]] || marker.placeData[appliedFilters[i][0]] !== appliedFilters[i][1]) {
			return false;
		}
	}
	return true;
}

$(document).ready(function() {

	// Button handlers
	$("#filter-bar .filter-bar-button").click(function(e) {		
		e.preventDefault();	
		$("#filter-bar a.active").not(this).removeClass('active');
		$(this).toggleClass('active');
		var filterType = $(this).data('filter');
		$("#filters .active").not($("#"+filterType+"-filter")).removeClass('active');
		$("#"+filterType+"-filter").toggleClass('active');
	});

	$(".filter-item").click(function(e) {		
		e.preventDefault();
		appliedFilters = [];
		var filterType = $(this).data('filterGroup');
		var filter = $(this).data('filterItem');
		appliedFilters.push([filterType, filter]);
		runFilter();
	});
});
