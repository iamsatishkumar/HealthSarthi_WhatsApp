document.addEventListener('DOMContentLoaded', function() {
    const messageInput = document.getElementById('messageInput');
    const sendButton = document.getElementById('sendButton');
    const chatMessages = document.getElementById('chatMessages');
    const languageSelect = document.getElementById('languageSelect');
    const hospitalSearch = document.getElementById('hospitalSearch');
    const hospitalsList = document.getElementById('hospitalsList');

    let currentLanguage = 'en';
    let languages = {};
    let currentSection = 'home';
    
    // Load language data
    async function loadLanguages() {
        try {
        const response = await fetch('http://127.0.0.1:8000/api/languages');    
            languages = await response.json();
            updateUI();
        } catch (error) {
            console.error('Error loading languages:', error);
        }
    }
    
    // Update UI text based on selected language
    function updateUI() {
        if (!languages[currentLanguage]) return;
        
        const lang = languages[currentLanguage];
        
        document.getElementById('headerTitle').textContent = `🩺 ${lang.ui.title}`;
        document.getElementById('headerSubtitle').textContent = lang.ui.subtitle;
        document.getElementById('messageInput').placeholder = lang.ui.placeholder;
        document.getElementById('sendButton').innerHTML = lang.ui.send;
        
        // Update features
        document.getElementById('feature1Title').textContent = lang.ui.features.ai.title;
        document.getElementById('feature1Desc').textContent = lang.ui.features.ai.desc;
        document.getElementById('feature2Title').textContent = lang.ui.features.sms.title;
        document.getElementById('feature2Desc').textContent = lang.ui.features.sms.desc;
        document.getElementById('feature3Title').textContent = lang.ui.features.database.title;
        document.getElementById('feature3Desc').textContent = lang.ui.features.database.desc;
    }
    
    // Language change handler
    languageSelect.addEventListener('change', function() {
        currentLanguage = this.value;
        updateUI();
    });
    
    // Section Navigation
    function showSection(sectionName) {
        // Hide all sections
        const sections = document.querySelectorAll('.content-section');
        sections.forEach(section => section.classList.remove('active'));

        // Show selected section
        const targetSection = document.getElementById(sectionName + '-section');
        if (targetSection) {
            targetSection.classList.add('active');
        }

        // Update navigation
        const navLinks = document.querySelectorAll('.nav-link');
        navLinks.forEach(link => link.classList.remove('active'));

        const activeLink = document.querySelector(`[onclick="showSection('${sectionName}')"]`);
        if (activeLink) {
            activeLink.classList.add('active');
        }

        currentSection = sectionName;

        // Load section-specific data
        if (sectionName === 'hospitals') {
            loadHospitals();
        }
    }

    // Hospital Search and Display
    async function loadHospitals(location = null) {
        try {
        const url = location 
    ? `http://127.0.0.1:8000/api/hospitals?location=${location}` 
    : 'http://127.0.0.1:8000/api/hospitals';
    
            const response = await fetch(url);
            const hospitals = await response.json();
            displayHospitals(hospitals);
        } catch (error) {
            console.error('Error loading hospitals:', error);
            hospitalsList.innerHTML = '<p class="error">Failed to load hospitals. Please try again.</p>';
        }
    }

    function displayHospitals(hospitals) {
        if (!hospitals || hospitals.length === 0) {
            hospitalsList.innerHTML = '<p class="no-results">No hospitals found for this location.</p>';
            return;
        }

        hospitalsList.innerHTML = hospitals.map(hospital => `
            <div class="hospital-card">
                <div class="hospital-header">
                    <div class="hospital-name">${hospital.name}</div>
                    <div class="hospital-type">${hospital.type}</div>
                    <div class="hospital-specialty">${hospital.specialty}</div>
                </div>
                <div class="hospital-body">
                    <div class="hospital-info">
                        <div class="info-item">
                            <span class="info-icon">📍</span>
                            <span class="info-text">${hospital.address}</span>
                        </div>
                        <div class="info-item">
                            <span class="info-icon">📞</span>
                            <span class="info-text">${hospital.phone}</span>
                        </div>
                        <div class="info-item">
                            <span class="info-icon">🚨</span>
                            <span class="info-text">${hospital.emergency}</span>
                        </div>
                    </div>
                    <div class="hospital-services">
                        <h4>Services:</h4>
                        <div class="services-list">
                            ${hospital.services.map(service => `<span class="service-tag">${service}</span>`).join('')}
                        </div>
                    </div>
                    <div class="hospital-rating">
                        <span class="rating-stars">⭐⭐⭐⭐⭐</span>
                        <span class="rating-text">${hospital.rating} (${hospital.distance})</span>
                    </div>
                    <div class="hospital-actions">
                        <button class="action-btn call" onclick="callHospital('${hospital.phone}')">
                            📞 Call
                        </button>
                        <button class="action-btn directions" onclick="getDirections('${hospital.address}')">
                            🗺️ Directions
                        </button>
                    </div>
                </div>
            </div>
        `).join('');
    }

    async function searchHospitals() {
        const query = hospitalSearch.value.trim();
        if (!query) {
            loadHospitals();
            return;
        }

        try {
            const response = await fetch(`http://127.0.0.1:8000/api/hospitals/search?query=${encodeURIComponent(query)}`);
            const results = await response.json();
            displayHospitals(results);
        } catch (error) {
            console.error('Error searching hospitals:', error);
            hospitalsList.innerHTML = '<p class="error">Search failed. Please try again.</p>';
        }
    }

    // Emergency Services
    function callEmergency(number) {
        if (confirm(`Call emergency number ${number}?`)) {
            window.location.href = `tel:${number}`;
        }
    }

    function callHospital(number) {
        if (confirm(`Call hospital at ${number}?`)) {
            window.location.href = `tel:${number}`;
        }
    }

    function getDirections(address) {
        const encodedAddress = encodeURIComponent(address);
        window.open(`https://maps.google.com/maps?q=${encodedAddress}`, '_blank');
    }

    // Education Functions
    function showVaccinations() {
        showSection('education');
        // Could add specific vaccination content loading here
    }

    function showOutbreaks() {
        showSection('education');
        // Could add specific outbreak content loading here
    }

    function showEducation(topic) {
        showSection('education');
        // Could add specific topic content loading here
    }

    // Initialize
    loadLanguages();
    showSection('home'); // Start with home section

    // Function to add message to chat
    function addMessage(content, isUser = false) {
        const messageDiv = document.createElement('div');
        messageDiv.className = `message ${isUser ? 'user-message' : 'bot-message'}`;

        const avatar = document.createElement('div');
        avatar.className = 'message-avatar';
        avatar.textContent = isUser ? '👤' : '🤖';

        const messageContent = document.createElement('div');
        messageContent.className = 'message-content';

        // Check if content contains structured disease information
        if (!isUser && content.includes('**')) {
            messageContent.innerHTML = formatDiseaseResponse(content);
        } else {
            messageContent.innerHTML = `<p>${content.replace(/\n/g, '<br>')}</p>`;
        }

        messageDiv.appendChild(avatar);
        messageDiv.appendChild(messageContent);
        chatMessages.appendChild(messageDiv);

        // Scroll to bottom
        chatMessages.scrollTop = chatMessages.scrollHeight;
    }

    // Function to format disease response
    function formatDiseaseResponse(content) {
        // Convert markdown-style formatting to HTML
        let formatted = content
            .replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>') // Bold text
            .replace(/\n\n/g, '</p><p>') // Paragraph breaks
            .replace(/\n/g, '<br>'); // Line breaks

        // Add proper paragraph structure
        if (!formatted.startsWith('<p>')) {
            formatted = '<p>' + formatted;
        }
        if (!formatted.endsWith('</p>')) {
            formatted = formatted + '</p>';
        }

        return formatted;
    }

    // Function to send message
    async function sendMessage() {
        const message = messageInput.value.trim();
        if (!message) return;

        // Add user message
        addMessage(message, true);
        messageInput.value = '';

        // Show typing indicator
        const typingDiv = document.createElement('div');
        typingDiv.className = 'message bot-message';
        const thinkingText = languages[currentLanguage]?.ui?.thinking || 'Thinking...';
        typingDiv.innerHTML = `
            <div class="message-avatar">🤖</div>
            <div class="message-content">
                <p><em>${thinkingText}</em></p>
            </div>
        `;
        chatMessages.appendChild(typingDiv);
        chatMessages.scrollTop = chatMessages.scrollHeight;

        try {
            const response = await fetch('http://127.0.0.1:8000/chat', {

                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ message: message, userId: 'web-user', language: currentLanguage }),
            });

            const data = await response.json();

            // Remove typing indicator
            chatMessages.removeChild(typingDiv);

            // Add bot response
            addMessage(data.response);

        } catch (error) {
            console.error('Error:', error);
            chatMessages.removeChild(typingDiv);
            addMessage('Sorry, I encountered an error. Please try again.');
        }
    }

    // Event listeners
    sendButton.addEventListener('click', sendMessage);

    messageInput.addEventListener('keypress', function(e) {
        if (e.key === 'Enter') {
            sendMessage();
        }
    });

    // Hospital search event listeners
    if (hospitalSearch) {
        hospitalSearch.addEventListener('keypress', function(e) {
            if (e.key === 'Enter') {
                searchHospitals();
            }
        });
    }

    // Global functions for HTML onclick
    window.showSection = showSection;
    window.callEmergency = callEmergency;
    window.callHospital = callHospital;
    window.getDirections = getDirections;
    window.showVaccinations = showVaccinations;
    window.showOutbreaks = showOutbreaks;
    window.showEducation = showEducation;
    window.searchHospitals = searchHospitals;

    // Focus on input when chat section is active
    if (messageInput) {
        messageInput.focus();
    }
});