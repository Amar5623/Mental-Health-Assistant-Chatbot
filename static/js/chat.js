document.addEventListener('DOMContentLoaded', function() {
    const chatMessages = document.getElementById('chat-messages');
    const userInput = document.getElementById('user-input');
    const sendButton = document.getElementById('send-button');
    const clearButton = document.getElementById('clear-button');
    const resourcesButton = document.getElementById('resources-button');
    
    // Send a welcome message when the page loads
    setTimeout(() => {
        addBotMessage("Hello! I'm your mental health assistant. How are you feeling today?");
    }, 500);
    
    // Send message when the send button is clicked
    sendButton.addEventListener('click', sendMessage);
    
    // Send message when Enter key is pressed
    userInput.addEventListener('keypress', function(e) {
        if (e.key === 'Enter') {
            sendMessage();
        }
    });
    
    // Clear chat history
    if (clearButton) {
        clearButton.addEventListener('click', function() {
            if (confirm('Are you sure you want to clear the chat history?')) {
                chatMessages.innerHTML = '';
                addBotMessage("Chat history cleared. How can I help you today?");
            }
        });
    }
    
    // Request resources
    if (resourcesButton) {
        resourcesButton.addEventListener('click', function() {
            addUserMessage("I'd like to see mental health resources");
            showTypingIndicator();
            
            fetch('/send_message', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ message: "resources" }),
            })
            .then(response => response.json())
            .then(data => {
                removeTypingIndicator();
                addBotMessage(data.response, data.timestamp);
            })
            .catch(error => {
                console.error('Error:', error);
                removeTypingIndicator();
                addBotMessage("I'm sorry, I'm having trouble retrieving resources. Please try again later.");
            });
        });
    }
    
    function sendMessage() {
        const message = userInput.value.trim();
        if (message === '') return;
        
        // Add user message to chat
        addUserMessage(message);
        
        // Clear input field
        userInput.value = '';
        
        // Show typing indicator
        showTypingIndicator();
        
        // Send message to server
        fetch('/send_message', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ message: message }),
        })
        .then(response => response.json())
        .then(data => {
            // Remove typing indicator
            removeTypingIndicator();
            
            // Add bot response to chat
            addBotMessage(data.response, data.timestamp);
        })
        .catch(error => {
            console.error('Error:', error);
            removeTypingIndicator();
            addBotMessage("I'm sorry, I'm having trouble connecting. Please try again later.");
        });
    }
    
    function addUserMessage(message) {
        const messageElement = document.createElement('div');
        messageElement.classList.add('message', 'user-message');
        
        const messageText = document.createElement('div');
        messageText.textContent = message;
        
        const messageTime = document.createElement('div');
        messageTime.classList.add('message-time');
        const now = new Date();
        messageTime.textContent = now.getHours().toString().padStart(2, '0') + ':' + 
                                 now.getMinutes().toString().padStart(2, '0');
        
        messageElement.appendChild(messageText);
        messageElement.appendChild(messageTime);
        
        chatMessages.appendChild(messageElement);
        scrollToBottom();
    }
    
    function addBotMessage(message, timestamp) {
        const messageElement = document.createElement('div');
        messageElement.classList.add('message', 'bot-message');
        
        // Format links in the message
        const messageText = document.createElement('div');
        messageText.innerHTML = formatLinks(message);
        
        const messageTime = document.createElement('div');
        messageTime.classList.add('message-time');
        
        if (timestamp) {
            messageTime.textContent = timestamp;
        } else {
            const now = new Date();
            messageTime.textContent = now.getHours().toString().padStart(2, '0') + ':' + 
                                     now.getMinutes().toString().padStart(2, '0');
        }
        
        messageElement.appendChild(messageText);
        messageElement.appendChild(messageTime);
        
        chatMessages.appendChild(messageElement);
        scrollToBottom();
    }
    
    function formatLinks(text) {
        // Convert URLs to clickable links
        const urlRegex = /(https?:\/\/[^\s]+)/g;
        return text.replace(urlRegex, function(url) {
            return '<a href="' + url + '" target="_blank" rel="noopener noreferrer">' + url + '</a>';
        }).replace(/\n/g, '<br>');
    }
    
    function showTypingIndicator() {
        const typingIndicator = document.createElement('div');
        typingIndicator.classList.add('typing-indicator');
        typingIndicator.id = 'typing-indicator';
        
        for (let i = 0; i < 3; i++) {
            const dot = document.createElement('span');
            typingIndicator.appendChild(dot);
        }
        
        chatMessages.appendChild(typingIndicator);
        scrollToBottom();
    }
    
    function removeTypingIndicator() {
        const typingIndicator = document.getElementById('typing-indicator');
        if (typingIndicator) {
            typingIndicator.remove();
        }
    }
    
    function scrollToBottom() {
        chatMessages.scrollTop = chatMessages.scrollHeight;
    }
    
    // Add quick response buttons when appropriate
    function addQuickResponseButtons(options) {
        const quickResponsesContainer = document.createElement('div');
        quickResponsesContainer.classList.add('quick-responses');
        
        options.forEach(option => {
            const button = document.createElement('button');
            button.classList.add('quick-response-button');
            button.textContent = option;
            
            button.addEventListener('click', function() {
                userInput.value = option;
                sendMessage();
                quickResponsesContainer.remove();
            });
            
            quickResponsesContainer.appendChild(button);
        });
        
        chatMessages.appendChild(quickResponsesContainer);
        scrollToBottom();
    }
    
    // Example of how to use quick response buttons
    // This could be triggered based on bot responses
    function checkForQuickResponses(botMessage) {
        if (botMessage.includes("How are you feeling today?")) {
            addQuickResponseButtons([
                "I'm feeling good",
                "I'm feeling okay",
                "I'm feeling down",
                "I'm feeling anxious"
            ]);
        } else if (botMessage.includes("Would you like to see some resources?")) {
            addQuickResponseButtons([
                "Yes, please",
                "No, thanks"
            ]);
        }
    }
});
