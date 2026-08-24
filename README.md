\# Dhruv AI Agent



A personal AI agent built as part of my Week 6 capstone.



The agent is integrated with my personal developer portfolio and allows

visitors to ask questions about my projects, skills, experience, and

technical background.



\## Live Project



Portfolio:

https://dhruvbudhwani-portfolio.netlify.app/



AI Agent API:

https://dhruv-ai-agent-2.onrender.com/



API Documentation:

https://dhruv-ai-agent-2.onrender.com/docs



\## Features



\- Answers questions about Dhruv's profile and projects

\- Uses a personal knowledge base

\- Generates responses using Google Gemini

\- Exposes a REST API using FastAPI

\- Integrated with a React portfolio

\- Deployed as a live cloud service



\## Architecture



```text

Visitor

&#x20;  |

&#x20;  v

React Portfolio

&#x20;  |

&#x20;  | POST /chat

&#x20;  v

FastAPI Backend

&#x20;  |

&#x20;  v

AI Agent

&#x20;  |

&#x20;  +----> Personal Knowledge Base

&#x20;  |

&#x20;  v

Google Gemini

&#x20;  |

&#x20;  v

Response

&#x20;  |

&#x20;  v

React Portfolio

