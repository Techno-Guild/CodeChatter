from flask import Flask, render_template, request, jsonify
from markupsafe import Markup
import os
import re
from groq import Groq
from dotenv import load_dotenv
from flask_wtf.csrf import CSRFProtect
from flask_caching import Cache

# Load environment variables
load_dotenv()

# Initialize Flask app and CSRF protection
app = Flask(__name__)
csrf = CSRFProtect(app)

# Configure cache
cache = Cache(config={'CACHE_TYPE': 'simple'})

# Initialize cache with app
cache.init_app(app)

# Get API key from environment variables
api = os.getenv("GROQ_API_KEY")
if not api:
    print("Error: GROQ_API_KEY environment variable is not set")
    exit(1)

# Initialize Groq client
client = Groq(api_key=api)

# Model options for the dropdown
model_options = [
    {"value": "gemma2-9b-it", "name": "Gemma 2 9B"},
    {"value": "gemma-7b-it", "name": "Gemma 7B"},
    {"value": "llama3-groq-70b-8192-tool-use-preview", "name": "Llama 3 Groq 70B Tool Use (Preview)"},
    {"value": "llama3-groq-8b-8192-tool-use-preview", "name": "Llama 3 Groq 8B Tool Use (Preview)"},
    {"value": "llama-3.1-70b-versatile", "name": "Llama 3.1 70B (Preview)"},
    {"value": "llama-3.1-8b-instant", "name": "Llama 3.1 8B (Preview)"},
    {"value": "llama3-70b-8192", "name": "Meta Llama 3 70B"},
    {"value": "llama3-8b-8192", "name": "Meta Llama 3 8B"},
    {"value": "mixtral-8x7b-32768", "name": "Mixtral 8x7B"},
]

@app.route('/')
@cache.cached(timeout=50)  # Cache this view for 50 seconds
def index():
    return render_template('index.html', model_options=model_options)

@app.route('/query', methods=['POST'])
@csrf.exempt
def ask():
    try:
        question = request.form.get('question')
        if not question:
            return jsonify({"error": "Please enter a question"}), 400

        # Add user message HTML
        response_html = f"""
        <div class="message user">
            <div class="message-bubble">{question}</div>
        </div>
        """

        selected_model = request.form.get('model', 'mixtral-8x7b-32768')
        template = """
                You are an AI-powered coding assistant here to help with programming challenges.
                You can assist with various tasks, including:
                Debugging Code: Identify and fix errors in code shared by the user. 
                Explaining Concepts: Provide detailed explanations of programming concepts. 
                Code Suggestions: Offer code snippets and suggest approaches to implement features. 
                Optimization Tips: Advise on improving code performance.
        """
        
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": template
                },
                {
                    "role": "user",
                    "content": question,
                },
            ],
            model=selected_model,
        )

        response = chat_completion.choices[0].message.content

        # Process the response and wrap it in assistant message HTML
        def replace_code_block(match):
            language = match.group(1) or 'plaintext'
            code = match.group(2)
            return f'<pre><code class="language-{language}">{code}</code></pre>'

        processed_response = re.sub(r'```(\w+)?\n(.*?)```', replace_code_block, response, flags=re.DOTALL)
        
        response_html += f"""
        <div class="message assistant">
            <div class="message-bubble">{processed_response}</div>
        </div>
        """

        return Markup(response_html)
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

@app.errorhandler(500)
def server_error(e):
    return render_template('500.html'), 500

@app.errorhandler(404)
def not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    try:
        app.run(debug=True, ssl_context='adhoc')
    except Exception as e:
        print(f"Failed to start the server: {e}")
        exit(1)
