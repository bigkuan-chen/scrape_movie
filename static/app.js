// Application State
let moviesData = [];
let availableCategories = new Set();

// DOM Elements
const searchInput = document.getElementById('search-input');
const searchClearBtn = document.getElementById('search-clear-btn');
const categoryFilter = document.getElementById('category-filter');
const sortSelect = document.getElementById('sort-select');
const statsText = document.getElementById('stats-text');
const loader = document.getElementById('loader');
const emptyState = document.getElementById('empty-state');
const moviesGrid = document.getElementById('movies-grid');
const themeToggleBtn = document.getElementById('theme-toggle');
const themeIconDark = themeToggleBtn.querySelector('.theme-icon-dark');
const themeIconLight = themeToggleBtn.querySelector('.theme-icon-light');

// Fetch and Initialize App
async function initApp() {
    try {
        const response = await fetch('/api/movies');
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        moviesData = await response.json();
        
        // Parse unique categories
        moviesData.forEach(movie => {
            if (movie.categories) {
                movie.categories.forEach(cat => availableCategories.add(cat));
            }
        });
        
        // Populate category dropdown
        populateCategories();
        
        // Render initial view
        filterAndRenderMovies();
        
        // Hide loader & show grid
        loader.style.display = 'none';
        moviesGrid.style.display = 'grid';
    } catch (error) {
        console.error('Error loading movie data:', error);
        statsText.innerText = 'Error loading movies. Please make sure the scraper has run successfully.';
        loader.style.display = 'none';
    }
}

// Populate Category Filter Options
function populateCategories() {
    // Sort categories alphabetically
    const sortedCats = Array.from(availableCategories).sort();
    sortedCats.forEach(cat => {
        const opt = document.createElement('option');
        opt.value = cat;
        opt.textContent = cat;
        categoryFilter.appendChild(opt);
    });
}

// Filter, Sort, and Render Loop
function filterAndRenderMovies() {
    const searchQuery = searchInput.value.toLowerCase().trim();
    const selectedCategory = categoryFilter.value;
    const selectedSort = sortSelect.value;
    
    // Toggle Search Clear Button
    searchClearBtn.style.display = searchQuery ? 'block' : 'none';

    // 1. Filter
    let filtered = moviesData.filter(movie => {
        // Search matches
        const matchesSearch = !searchQuery || 
            movie.title_cn.toLowerCase().includes(searchQuery) ||
            movie.title_en.toLowerCase().includes(searchQuery) ||
            movie.regions.toLowerCase().includes(searchQuery) ||
            movie.duration.toLowerCase().includes(searchQuery);
            
        // Category matches
        const matchesCategory = !selectedCategory || 
            (movie.categories && movie.categories.includes(selectedCategory));
            
        return matchesSearch && matchesCategory;
    });

    // 2. Sort
    if (selectedSort === 'score-desc') {
        filtered.sort((a, b) => b.score - a.score);
    } else if (selectedSort === 'score-asc') {
        filtered.sort((a, b) => a.score - b.score);
    } else if (selectedSort === 'release-desc') {
        filtered.sort((a, b) => {
            const dateA = a.release_date === 'N/A' ? '' : a.release_date;
            const dateB = b.release_date === 'N/A' ? '' : b.release_date;
            return dateB.localeCompare(dateA);
        });
    } else if (selectedSort === 'release-asc') {
        filtered.sort((a, b) => {
            const dateA = a.release_date === 'N/A' ? '9999-99-99' : a.release_date;
            const dateB = b.release_date === 'N/A' ? '9999-99-99' : b.release_date;
            return dateA.localeCompare(dateB);
        });
    } else {
        // Default sort (by ID)
        filtered.sort((a, b) => a.id - b.id);
    }

    // Update stats bar
    statsText.innerText = `Showing ${filtered.length} of ${moviesData.length} movies`;

    // Render Grid
    renderGrid(filtered);
}

// Render Grid markup
function renderGrid(movies) {
    moviesGrid.innerHTML = '';
    
    if (movies.length === 0) {
        moviesGrid.style.display = 'none';
        emptyState.style.display = 'block';
        return;
    }
    
    emptyState.style.display = 'none';
    moviesGrid.style.display = 'grid';

    movies.forEach(movie => {
        const card = document.createElement('article');
        card.className = 'movie-card';
        
        // Category badges string
        const categoriesHtml = movie.categories
            ? movie.categories.map(cat => `<span class="category-badge">${cat}</span>`).join('')
            : '';

        card.innerHTML = `
            <div class="movie-card-media">
                <img src="${movie.poster_url}" alt="${movie.title_cn}" loading="lazy" onerror="this.src='https://images.unsplash.com/photo-1542204111-374534680411?auto=format&fit=crop&q=80&w=400'">
                <div class="score-badge">
                    <i class="fa-solid fa-star"></i>
                    <span>${movie.score.toFixed(1)}</span>
                </div>
            </div>
            <div class="movie-card-body">
                <div class="movie-title-container">
                    <h3 class="movie-title-cn">${movie.title_cn}</h3>
                    <h4 class="movie-title-en">${movie.title_en || 'Original Title'}</h4>
                </div>
                <div class="movie-categories">
                    ${categoriesHtml}
                </div>
                <div class="movie-metadata">
                    <div class="meta-row">
                        <i class="fa-solid fa-earth-americas"></i>
                        <span>${movie.regions}</span>
                    </div>
                    <div class="meta-row">
                        <i class="fa-solid fa-clock"></i>
                        <span>${movie.duration}</span>
                    </div>
                    <div class="meta-row">
                        <i class="fa-solid fa-calendar-days"></i>
                        <span>${movie.release_date}</span>
                    </div>
                </div>
                <a href="${movie.detail_link}" target="_blank" class="movie-detail-btn">
                    <span>View Detail</span>
                    <i class="fa-solid fa-arrow-up-right-from-square"></i>
                </a>
            </div>
        `;
        moviesGrid.appendChild(card);
    });
}

// Reset Filters Functionality
function resetFilters() {
    searchInput.value = '';
    categoryFilter.value = '';
    sortSelect.value = 'default';
    filterAndRenderMovies();
}

// Download Excel File Trigger
function downloadExcel() {
    window.location.href = '/api/download';
}

// Theme Switching Feature
function initTheme() {
    const savedTheme = localStorage.getItem('theme') || 'dark';
    document.documentElement.setAttribute('data-theme', savedTheme);
    updateThemeIcons(savedTheme);
}

function updateThemeIcons(theme) {
    if (theme === 'dark') {
        themeIconDark.style.display = 'none';
        themeIconLight.style.display = 'block';
    } else {
        themeIconDark.style.display = 'block';
        themeIconLight.style.display = 'none';
    }
}

themeToggleBtn.addEventListener('click', () => {
    const currentTheme = document.documentElement.getAttribute('data-theme');
    const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
    
    document.documentElement.setAttribute('data-theme', newTheme);
    localStorage.setItem('theme', newTheme);
    updateThemeIcons(newTheme);
});

// Event Listeners
searchInput.addEventListener('input', filterAndRenderMovies);
categoryFilter.addEventListener('change', filterAndRenderMovies);
sortSelect.addEventListener('change', filterAndRenderMovies);

searchClearBtn.addEventListener('click', () => {
    searchInput.value = '';
    filterAndRenderMovies();
    searchInput.focus();
});

// Chat Widget Client Side Controller
const chatToggleBtn = document.getElementById('chat-toggle-btn');
const chatCloseBtn = document.getElementById('chat-close-btn');
const chatWindow = document.getElementById('chat-window');
const chatMessages = document.getElementById('chat-messages');
const chatInput = document.getElementById('chat-input');
const chatSendBtn = document.getElementById('chat-send-btn');

// Toggle chat window visibility
chatToggleBtn.addEventListener('click', () => {
    chatWindow.classList.toggle('active');
    chatInput.focus();
});

chatCloseBtn.addEventListener('click', () => {
    chatWindow.classList.remove('active');
});

// Send message function
async function sendMessage(text) {
    const messageText = text || chatInput.value.trim();
    if (!messageText) return;

    if (!text) {
        chatInput.value = '';
    }

    // Append User Message
    appendMessage(messageText, 'user-message');
    
    // Add Typing Indicator
    const typingIndicator = showTypingIndicator();
    scrollToBottom();

    try {
        const response = await fetch('/api/chat', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ message: messageText })
        });
        
        // Remove Typing Indicator
        typingIndicator.remove();

        if (response.ok) {
            const data = await response.json();
            appendMessage(data.response, 'bot-message');
        } else {
            appendMessage('Sorry, I encountered an error. Please try again.', 'bot-message');
        }
    } catch (error) {
        if (typingIndicator) typingIndicator.remove();
        console.error('Chat error:', error);
        appendMessage('Connection error. Please make sure the server is online.', 'bot-message');
    }
    
    scrollToBottom();
}

function appendMessage(text, className) {
    const msgDiv = document.createElement('div');
    msgDiv.className = `message ${className}`;
    msgDiv.innerHTML = text; // Uses innerHTML to render bold and links from the backend
    chatMessages.appendChild(msgDiv);
}

function showTypingIndicator() {
    const indicator = document.createElement('div');
    indicator.className = 'typing-indicator';
    indicator.innerHTML = `
        <div class="typing-dot"></div>
        <div class="typing-dot"></div>
        <div class="typing-dot"></div>
    `;
    chatMessages.appendChild(indicator);
    return indicator;
}

function scrollToBottom() {
    chatMessages.scrollTop = chatMessages.scrollHeight;
}

// Make sendSuggestion globally available for HTML onclick attribute
window.sendSuggestion = function(text) {
    sendMessage(text);
};

// Event Listeners for Send Action
chatSendBtn.addEventListener('click', () => sendMessage());
chatInput.addEventListener('keypress', (e) => {
    if (e.key === 'Enter') {
        sendMessage();
    }
});

// Start the App
initTheme();
initApp();
