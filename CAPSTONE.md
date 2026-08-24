# Week 6 Capstone — Dhruv AI

## 1. Concept

I wanted to turn my developer portfolio into an interactive experience
rather than a static website.

The concept was to build a personal AI agent that acts as an AI
representative of my developer profile.

Visitors can ask questions about my projects, skills, experience, and
technical background instead of manually searching through the portfolio.

## 2. Personal Brand

My personal brand is centered around being a Computer Science student
focused on software development, artificial intelligence, and machine
learning.

The portfolio presents the projects I have built while the AI agent
provides an interactive way for visitors to understand my background.

## 3. Problem

A traditional portfolio requires visitors to navigate through multiple
sections to find information.

I wanted to create a more natural interface where someone could simply
ask a question and receive a relevant answer about me.

## 4. Solution

I built Dhruv AI, a personal AI agent connected to my portfolio.

The system combines:

- A React-based personal portfolio
- A FastAPI backend
- A personal knowledge base
- Google Gemini for AI-generated responses
- A deployed cloud API

## 5. AI Stack

### Frontend

- React
- Vite

### Backend

- Python
- FastAPI
- Pydantic

### AI

- Google Gemini API

### Deployment

- Netlify for the portfolio
- Render for the AI backend
- GitHub for source control

## 6. Architecture

```text
Visitor
   |
   v
Personal Portfolio
   |
   v
Dhruv AI Interface
   |
   | POST /chat
   v
FastAPI Backend
   |
   v
AI Agent
   |
   +----> Personal Knowledge Base
   |
   v
Google Gemini
   |
   v
Generated Response
   |
   v
Portfolio
7. Development Process

I first created the personal AI agent locally using Python and a virtual
environment.

I then integrated the Gemini API and created a FastAPI endpoint that could
receive questions and return AI-generated responses.

After testing the agent locally, I deployed the backend to Render.

I then connected the React portfolio to the deployed API.

Finally, I deployed the updated portfolio to Netlify.

8. Challenges

The project involved several real development problems.

API and package configuration

I had to configure the Python environment and resolve package
dependencies while setting up the Gemini SDK.

Model compatibility

The initial Gemini model was no longer available to new users, so I had
to update the implementation to use an available model.

Environment variables

The deployed backend initially failed because the Gemini API key was not
configured correctly in the production environment.

I fixed this by configuring the API key as a Render environment variable.

Frontend deployment

The portfolio initially failed to build on Netlify because of a Vite
permission issue.

I traced the problem to node_modules being tracked in the repository,
removed it from Git tracking, and redeployed the project with a clean
dependency installation.

9. Final Result

The final system consists of a live personal portfolio and a deployed AI
agent.

Portfolio:

https://dhruvbudhwani-portfolio.netlify.app/

AI Agent:

https://dhruv-ai-agent-2.onrender.com/

API Documentation:

https://dhruv-ai-agent-2.onrender.com/docs

10. Example Interaction

User:

"What projects has Dhruv built?"

The agent responds with information about projects including:

Personal AI Study Coach
Job Portal
Talkify
11. What I Learned

This project taught me that building an AI application involves more than
calling an AI API.

I had to connect multiple parts of a real application:

Frontend
Backend
AI model
Personal data
Environment variables
APIs
Cloud deployment
GitHub

I also learned how important debugging and deployment configuration are
when moving an application from local development to production.

12. Future Improvements

Future versions could include:

Conversation memory
More detailed personal knowledge
GitHub API integration
Resume-aware responses
Project-specific information
Visitor analytics
Improved UI for the AI assistant
## 13. Demo

A live demonstration of the project is available here:

https://drive.google.com/file/d/1tXzbrBZwWznYI3OsK6FVSMHaUL50SPtb/view?usp=drive_link