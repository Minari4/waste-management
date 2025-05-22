// Offline location data for Surigao City
const surigaoLocations = [
    {
        name: "Surigao City Hall",
        lat: 9.7843,
        lng: 125.4888,
        address: "Surigao City Hall, Surigao City",
        type: "Government Building"
    },
    {
        name: "Surigao City Port",
        lat: 9.7833,
        lng: 125.4833,
        address: "Surigao City Port, Surigao City",
        type: "Transportation Hub"
    },
    {
        name: "Surigao City Medical Center",
        lat: 9.7867,
        lng: 125.4917,
        address: "Surigao City Medical Center, Surigao City",
        type: "Hospital"
    },
    {
        name: "Surigao City Public Market",
        lat: 9.7850,
        lng: 125.4867,
        address: "Surigao City Public Market, Surigao City",
        type: "Market"
    },
    {
        name: "Surigao City Cathedral",
        lat: 9.7833,
        lng: 125.4833,
        address: "Surigao City Cathedral, Surigao City",
        type: "Religious Site"
    },
    {
        name: "Surigao City Plaza",
        lat: 9.7842,
        lng: 125.4883,
        address: "Surigao City Plaza, Surigao City",
        type: "Public Space"
    },
    {
        name: "Surigao City Airport",
        lat: 9.7833,
        lng: 125.4833,
        address: "Surigao City Airport, Surigao City",
        type: "Transportation Hub"
    },
    {
        name: "Surigao City Bus Terminal",
        lat: 9.7850,
        lng: 125.4867,
        address: "Surigao City Bus Terminal, Surigao City",
        type: "Transportation Hub"
    },
    {
        name: "Surigao City Police Station",
        lat: 9.7842,
        lng: 125.4883,
        address: "Surigao City Police Station, Surigao City",
        type: "Government Building"
    },
    {
        name: "Surigao City Fire Station",
        lat: 9.7842,
        lng: 125.4883,
        address: "Surigao City Fire Station, Surigao City",
        type: "Government Building"
    },
    {
        name: "Surigao City Public Library",
        lat: 9.7845,
        lng: 125.4880,
        address: "Surigao City Public Library, Surigao City",
        type: "Public Facility"
    },
    {
        name: "Surigao City Sports Complex",
        lat: 9.7855,
        lng: 125.4870,
        address: "Surigao City Sports Complex, Surigao City",
        type: "Sports Facility"
    },
    {
        name: "Surigao City Elementary School",
        lat: 9.7848,
        lng: 125.4885,
        address: "Surigao City Elementary School, Surigao City",
        type: "Educational Institution"
    },
    {
        name: "Surigao City High School",
        lat: 9.7852,
        lng: 125.4875,
        address: "Surigao City High School, Surigao City",
        type: "Educational Institution"
    },
    {
        name: "Surigao City Park",
        lat: 9.7840,
        lng: 125.4890,
        address: "Surigao City Park, Surigao City",
        type: "Public Space"
    }
];

// Function to search locations offline with improved matching
function searchOfflineLocations(query) {
    if (!query) return [];
    
    query = query.toLowerCase().trim();
    const searchTerms = query.split(' ').filter(term => term.length > 0);
    
    return surigaoLocations.filter(location => {
        const searchableText = [
            location.name,
            location.address,
            location.type
        ].join(' ').toLowerCase();
        
        return searchTerms.every(term => searchableText.includes(term));
    });
}

// Function to get location by coordinates with improved precision
function getLocationByCoordinates(lat, lng) {
    const PRECISION = 0.0005; // Increased precision for better matching
    return surigaoLocations.find(location => 
        Math.abs(location.lat - lat) < PRECISION && 
        Math.abs(location.lng - lng) < PRECISION
    );
}

// Function to get nearby locations
function getNearbyLocations(lat, lng, radius = 0.01) {
    return surigaoLocations.filter(location => 
        Math.abs(location.lat - lat) < radius && 
        Math.abs(location.lng - lng) < radius
    );
} 