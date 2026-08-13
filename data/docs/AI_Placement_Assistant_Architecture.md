# AI Placement Assistant — Architecture & Roadmap

**Owner:** Prateek
**Type:** Flagship placement-prep AI project
**Approach:** Backend-first, project-driven learning (learn only what each task needs)

---

## 1. Project Vision

An AI-powered platform that helps students prepare for placements end-to-end:
resume analysis → skill-gap detection → tracked preparation (DSA/SQL/aptitude) →
company-specific prep → AI-powered mock interviews with a multi-persona panel.

The **Interview Panel Simulator** (technical / HR / hiring-manager personas) is the
centerpiece demo feature — it personalizes questions using resume + tracker data,
making the project feel like a product rather than a coursework submission.

---

## 2. High-Level Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                        FRONTEND (React)                     │
│   Dashboard | Resume Upload | Trackers | Interview Panel UI │
└───────────────────────────┬──────────────────────────────────┘
                             │ REST API (JSON)
┌───────────────────────────▼──────────────────────────────────┐
│                     BACKEND (FastAPI)                        │
│  ┌───────────────┐ ┌───────────────┐ ┌──────────────────┐   │
│  │ Auth Service  │ │ Resume Service│ │ Tracker Service   │   │
│  └───────────────┘ └───────────────┘ └──────────────────┘   │
│  ┌───────────────┐ ┌───────────────┐ ┌──────────────────┐   │
│  │ RAG Service   │ │ Agent Service │ │ Interview Service │   │
│  └───────────────┘ └───────────────┘ └──────────────────┘   │
└───────┬───────────────┬───────────────────┬──────────────────┘
        │               │                   │
┌───────▼──────┐ ┌──────▼───────┐   ┌───────▼────────────┐
│    MySQL     │ │ Vector Store │   │   LLM Provider      │
│ (users, res- │ │ (FAISS/      │   │ (Claude/OpenAI API) │
│  umes,       │ │  Chroma) for │   │  for generation +   │
│  trackers)   │ │  RAG + skill │   │  personas           │
│              │ │  embeddings  │   │                      │
└──────────────┘ └──────────────┘   └──────────────────────┘
```

**Core design principle:** each service is independently learnable and testable —
you build and understand one box at a time, not the whole diagram at once.

---

## 3. Folder Structure (target — grows incrementally, don't pre-build empty folders)

```
ai-placement-assistant/
├── backend/
│   └── app/
│       ├── core/              # config, settings, security
│       ├── db/                # SQLAlchemy models, session, migrations
│       ├── parsers/           # resume text extraction & parsing
│       ├── services/
│       │   ├── auth/
│       │   ├── resume/        # ATS scoring, skill-gap analysis
│       │   ├── tracker/       # DSA/SQL/aptitude tracking
│       │   ├── rag/           # ingestion, embeddings, retrieval
│       │   ├── agents/        # planner agent, tool definitions
│       │   └── interview/     # persona definitions, panel orchestration
│       ├── api/                # FastAPI routers per service
│       ├── evals/              # test sets + scoring scripts for AI features
│       └── main.py
├── frontend/                   # React app (Phase 10)
├── data/
│   ├── sample_resumes/
│   └── placement_resources/    # company Q&A data for RAG
├── docker/                     # Dockerfiles, docker-compose (Phase 11)
├── .github/workflows/          # CI/CD (Phase 12)
├── .gitignore
├── requirements.txt
└── README.md
```

---

## 4. Phase Roadmap

| # | Phase | What gets built | Tech to learn | Learn scope |
|---|---|---|---|---|
| 1 | Foundation | Repo, plain-Python resume text extractor | — | (in progress) |
| 2 | API layer | FastAPI wrapping parser, basic auth | FastAPI (routes, models, params) | Just CRUD basics |
| 3 | Database | User/resume/tracker schema | MySQL + SQLAlchemy | Schema design, joins, ORM basics |
| 4 | Resume intelligence | ATS score, keyword skill-gap | NLP basics (NER, TF-IDF) | Rule-based only |
| 5 | NLP upgrade | Semantic skill matching | Transformers/embeddings | `sentence-transformers`, cosine similarity |
| 6 | Trackers & dashboard | DSA/SQL/aptitude tracking, stats | More FastAPI + MySQL | — |
| 7 | RAG | Retrieval over placement + company-specific resources | RAG (chunking, vector store) | One working pipeline, FAISS/Chroma |
| 8 | LLM features (single persona) | Mock interview generator, JD analysis | LLM prompting | Practical prompting, structured output |
| 9 | AI Agents + Interview Panel | Multi-persona panel, planner agent | Agents (tool calling, ReAct) | One working agent + panel handoff logic |
| 10 | Frontend | React dashboard, upload, interview UI | React | Components, state, API calls, routing |
| 11 | Containerization | Docker for backend + frontend | Docker | Dockerfile, docker-compose |
| 12 | Deployment & CI/CD | Ship it | Cloud (AWS/GCP/Azure) + GitHub Actions | One deployed service, one automated pipeline |

---

## 5. Interview Panel Simulator — Design Notes

**Personas (Phase 9):**
- **Technical interviewer** — DSA/CS fundamentals, follow-up probing
- **HR interviewer** — behavioral, culture-fit, communication
- **Hiring manager** — project deep-dives, "why hire you," pressure questions

**Build sequence:**
1. Phase 8: get **one** persona working end-to-end — prompting, multi-turn conversation state, answer evaluation
2. Phase 9: expand to the full panel — persona handoff logic, panel decides who asks what next, personalization using resume/tracker weak-area data

**Personalization hook:** the panel's question selection should read from your
resume analysis (Phase 4/5) and tracker data (Phase 6) — e.g., if your tracker
shows low DSA completion, the technical persona weights questions accordingly.
This is what turns it from "a chatbot" into "a system that knows the user."

---

## 6. Differentiators Baked Into the Plan

| Differentiator | Where it lives |
|---|---|
| Semantic (not keyword) skill matching | Phase 5 |
| Eval pipeline for AI features (accuracy tracking over versions) | `backend/app/evals/`, ongoing from Phase 4 onward |
| Company-specific RAG (not generic placement content) | Phase 7 |
| Multi-agent interview panel with visible reasoning | Phase 9 |
| Stylized, custom-designed dashboard (not default templates) | Phase 10 |

---

## 7. Working Agreement (Mentorship Rules)

- Mentor breaks work into milestones → tasks; explains *why* each task exists
- Learner writes all code first; mentor reviews, doesn't rewrite
- New tech is taught only to the scope the current task needs (✅ learn / ❌ skip / 📖 one doc link)
- No complete code given unless explicitly requested
- Folder structure grows only when a phase needs it — no premature scaffolding

---

## 8. Current Status

- ✅ Milestone 1, Task 1: Repo structure created & pushed to GitHub
- 🔲 Milestone 1, Task 2: PDF text extractor (`backend/app/parsers/pdf_extractor.py`) — in progress
