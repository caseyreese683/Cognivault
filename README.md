# 🧠 Cognivault — Privacy-Preserving Knowledge Network

Cognivault is an AI-powered encrypted knowledge vault.  
Your data stays yours — embeddings are stored locally, encrypted with AES-256.  
LLM queries run privately through LangChain routers, never leaving your vault.

## ✨ Features
- AES-256 encryption of embeddings
- Wallet-based authentication (MetaMask)
- Local semantic search
- Modular FastAPI backend + React frontend
- Dockerized deployment

## 🧩 Tech Stack
**Backend:** FastAPI, LangChain, PyCryptodome  
**Frontend:** React + Vite + TypeScript  
**Database:** Postgres + local VectorStore  
**Auth:** Web3 wallet signature (Metamask, WalletConnect)

## 🚀 Run locally
```bash
docker-compose up --build
