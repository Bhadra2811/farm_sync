document.addEventListener("DOMContentLoaded", function () {
    const farmData = JSON.parse(document.getElementById('farm-map-data').textContent);

    var map = L.map('map').setView([10.0, 76.0], 7);
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '© OpenStreetMap contributors'
    }).addTo(map);

    farmData.forEach(farm => {
        L.marker([farm.lat, farm.lng])
            .addTo(map)
            .bindPopup(`<b>${farm.name}</b><br>${farm.location}`);
    });
});
