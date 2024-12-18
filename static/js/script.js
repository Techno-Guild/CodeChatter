document.body.addEventListener('htmx:afterRequest', function(event) {
    if (event.detail.elt.getAttribute('hx-target') === '#code-display') {
        const codeDisplay = document.getElementById('code-display');
        codeDisplay.innerHTML = event.detail.xhr.responseText;
        codeDisplay.classList.add('show');
        
        // Apply syntax highlighting
        codeDisplay.querySelectorAll('pre code').forEach((block) => {
            hljs.highlightElement(block);
        });
    }
});

// Handle enter key press
document.querySelector('.chat-input').addEventListener('keydown', function(e) {
    if (e.key === 'Enter' && !e.shiftKey) {
        e.preventDefault();
        const form = this.closest('form');
        if (this.value.trim()) {
            form.dispatchEvent(new Event('submit'));
        }
    }
});

// Auto resize textarea as user types
document.querySelector('.chat-input').addEventListener('input', function() {
    this.style.height = '60px';
    this.style.height = Math.min(this.scrollHeight, 150) + 'px';
});

function copyCode() {
    const codeDisplay = document.getElementById('code-display');
    navigator.clipboard.writeText(codeDisplay.textContent).then(() => {
        const copyButton = document.getElementById('copy-button');
        const originalIcon = copyButton.innerHTML;
        copyButton.innerHTML = '<i class="fas fa-check"></i>';
        setTimeout(() => {
            copyButton.innerHTML = originalIcon;
        }, 2000);
    });
}
