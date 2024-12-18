
# Sample-CodeChatter: Python/Flask

CodeChatter is an advanced Flask-based application that harnesses the power of the Groq API to provide intelligent coding assistance. This versatile tool offers multiple AI model selections, enabling developers to leverage artificial intelligence for various coding tasks, including code completion, debugging, and optimization.

| **Category**| **Technology**|
|--------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Backend**| ![Python](https://skillicons.dev/icons?i=python) ![Flask](https://skillicons.dev/icons?i=flask)|
| **Frontend**| ![JavaScript](https://skillicons.dev/icons?i=js) ![HTML5](https://skillicons.dev/icons?i=html) ![CSS3](https://skillicons.dev/icons?i=css)|
| **Groq AI Integration**| ![Groq API](https://github.com/user-attachments/assets/7610e24d-f44c-4805-a29b-6215df7ffe13)                                 |
| **Version Control**| ![Git](https://skillicons.dev/icons?i=git) ![GitHub](https://skillicons.dev/icons?i=github)|
| **Development Environment**| ![Visual Studio Code](https://skillicons.dev/icons?i=vscode)|
| **Dev Manager**| ![Daytona](https://github.com/user-attachments/assets/f22ffdb6-3bfe-4462-b53d-493b858e869f)|



## 🛠️ Getting Started

1. **Install Daytona**: Follow the [Daytona installation guide](https://www.daytona.io/docs/installation/installation/).  
2. **Create the Workspace**:  
   ```bash  
   daytona create https://github.com/yashksaini-coder/sample-codechatter
   ```  

3. **Set Up a Virtual Environment** (Recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

4. **Configure Environment Variables**
   Create a `.env` file in the root directory with the following content:

   ```
   GROQ_API_KEY=your_api_key_here
   ```
   Replace `your_api_key_here` with your actual Groq API key.

5. **Run the Application**
   ```bash
   python app.py
   ```

6. **Access the Application**
   Open your web browser and navigate to `http://localhost:5000`

## 🌟 Key Features

- **AI-Powered Coding Assistance**: Utilize state-of-the-art AI models to enhance your coding process.
- **Multi-Model Support**: Choose from a range of AI models to best suit your specific coding needs.
- **Syntax Highlighting**: Enjoy clear, color-coded syntax for multiple programming languages.
- **One-Click Code Copying**: Easily copy generated code snippets with a single click.
- **Responsive Design**: Access CodeChatter seamlessly across various devices and screen sizes.
- **User-Friendly Interface**: Intuitive design for effortless interaction with AI models.

## 💻 Usage Guide

1. **Enter Your Query**: Type your coding question or describe the task in the provided textarea.
2. **Select AI Model**: Choose the most appropriate AI model for your task from the dropdown menu.
3. **Submit Query**: Click the "Ask" button to send your request to the AI.
4. **View Response**: The AI-generated code or explanation will appear in the display area.
5. **Copy Code**: Use the copy button next to code snippets for easy copying.
