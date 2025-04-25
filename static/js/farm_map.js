document.addEventListener("DOMContentLoaded", function () {
    const farmData = JSON.parse(document.getElementById("farm-data").textContent);

    const lat = parseFloat(farmData.lat);
    const lng = parseFloat(farmData.lng);

    const map = L.map('map').setView([lat, lng], 14);

    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        maxZoom: 19,
        attribution: '© OpenStreetMap contributors'
    }).addTo(map);

    L.marker([lat, lng]).addTo(map)
        .bindPopup("<b>" + farmData.name + "</b><br>" + farmData.location)
        .openPopup();
});
