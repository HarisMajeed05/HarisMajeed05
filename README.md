<div align="center">

![Header](https://capsule-render.vercel.app/api?type=waving&color=0:6D28D9,50:7C3AED,100:22D3EE&height=220&section=header&text=Haris%20Majeed%20Raja&fontSize=48&fontColor=ffffff&animation=fadeIn&fontAlignY=38&desc=AI%20Engineer%20%7C%20Computer%20Vision%20%2B%20Full-Stack%20Engineering&descAlignY=58&descSize=18)

<img src="https://readme-typing-svg.herokuapp.com/?font=Fira+Code&weight=500&size=21&duration=3000&pause=900&color=A78BFA&center=true&vCenter=true&width=700&lines=Computer+Vision+%7C+Detection%2C+Tracking%2C+Fine-tuning;LLM+Apps+%7C+RAG%2C+Retrieval%2C+Streaming+Chat;Multimodal+AI+%7C+VLMs%2C+Speech%2C+Deepfake+Detection;Model+to+API+to+UI+%7C+Shipped+End+to+End" alt="Typing SVG" />

<br/>

![BS Computer Science](https://img.shields.io/badge/BS_Computer_Science-ITU_Lahore-6D28D9?style=flat-square)
![Location](https://img.shields.io/badge/Location-Lahore,_Pakistan-22D3EE?style=flat-square)
![Role](https://img.shields.io/badge/AI_Engineer-MLBench-7C3AED?style=flat-square)

[![Portfolio](https://img.shields.io/badge/Portfolio-View-7C3AED?style=for-the-badge&logo=vercel&logoColor=white)](https://harismajeed05.github.io/portfolio/)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/haris-majeed-raja/)
[![Email](https://img.shields.io/badge/Email-Contact-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:harismajeed0501@gmail.com)
[![Resume](https://img.shields.io/badge/Resume-View-4285F4?style=for-the-badge&logo=googledrive&logoColor=white)](https://drive.google.com/file/d/1E1bMbfKWI_SpXBcua9QnBs4r42S5bjsu/view?usp=sharing)

![Profile Views](https://komarev.com/ghpvc/?username=HarisMajeed05&color=7C3AED&style=flat-square&label=Profile+Views)
![Followers](https://img.shields.io/github/followers/HarisMajeed05?style=flat-square&color=6D28D9&label=Followers)
![Stars](https://img.shields.io/github/stars/HarisMajeed05?style=flat-square&color=22D3EE&label=Stars)

</div>

---

### About

I build AI systems that go from raw data to a working product. At **MLBench** I deliver production computer vision solutions for multiple clients, covering data annotation, model training, evaluation and deployment. Outside of work, I have built RAG assistants, a multilingual voice and gesture interface, and a lightweight multimodal deepfake detector for my final year project at ITU Lahore.

I like owning the full path: data, model, evaluation, API and UI. I also like building core systems from scratch (a compiler, a search engine, a kernel module) so I know exactly what I am trusting when I use a library.

```yaml
Focus:    Computer Vision, Multimodal AI, LLM Applications
Strength: Taking a model from experiment to a usable product
Stack:    Python, PyTorch, FastAPI, React
```

---

### Tech Stack

**Languages**

<img src="https://skillicons.dev/icons?i=py,cpp,c,java,js,html,css" />

**AI / ML**

<img src="https://skillicons.dev/icons?i=pytorch,sklearn,opencv,numpy,pandas" />

**Backend, Frontend & Tools**

<img src="https://skillicons.dev/icons?i=fastapi,flask,react,nodejs,express,mongodb,docker,git,linux,vscode" />

---

### AI / ML Expertise

| Area | What I do | Tools |
| --- | --- | --- |
| Computer Vision | Object detection, tracking, fine-tuning, image classification | YOLO, RF-DETR, DINOv2, ByteTrack, OpenCV, Cellpose-SAM |
| LLM Apps & RAG | Document-grounded Q&A, source citations, streaming chat, per-project retrieval isolation, tool-using assistants | LangChain, FAISS, Groq, sentence-transformers |
| Multimodal & VLMs | Image-text pipelines, explanation and verification of model outputs | CLIP, BLIP-2, LLaVA-Mini, Qwen-VL, HuggingFace Transformers |
| Speech & Voice AI | Multilingual speech-to-text, streaming spoken replies, voice login | Whisper (Groq and faster-whisper) |
| Evaluation & Benchmarking | Precision, recall and F1 comparisons, cross-dataset benchmarks, OCR backend comparisons | scikit-learn, Tesseract, DocTR |
| Deployment | APIs and web apps around models, CPU-friendly and low-resource inference | FastAPI, Flask, React, MongoDB, JWT |

---

### Featured Projects

<details>
<summary><b>Legal AI Chatbot</b></summary>
<br/>

Full-stack RAG assistant where users upload PDFs into projects and get answers that cite their sources.

| | |
| --- | --- |
| **Stack** | React, FastAPI, MongoDB, LangChain, FAISS, sentence-transformers, Groq API |
| **Features** | Conversation memory, streaming replies, answer badges (from documents or general knowledge), PDF chat export, project sharing, optional OCR for scanned PDFs |
| **Scale** | Multiple projects per user, each with its own chats and documents |
| **Performance** | FAISS vector search, GPU-free setup with the LLM on Groq and a small embedding model on CPU |
| **Security** | JWT auth, project-scoped retrieval so documents never leak across projects, rate limits on chat and upload |
| **Impact** | Source-cited answers lower hallucination risk in legal Q&A |
| **Repository** | [github.com/HarisMajeed05/legal-ai-chatbot](https://github.com/HarisMajeed05/legal-ai-chatbot) |

</details>

<details>
<summary><b>GestVox</b></summary>
<br/>

Hands-free Windows control using hand gestures and a multilingual voice assistant.

| | |
| --- | --- |
| **Stack** | Python, MediaPipe, Groq (Whisper and LLM), faster-whisper, PowerShell |
| **Features** | Gesture cursor, click, drag, scroll, zoom and media control, plus voice control of apps, system settings and files with persistent memory |
| **Languages** | English, Urdu, Punjabi and mixed speech, detected per sentence, with spoken replies in the same language |
| **Performance** | Replies stream sentence by sentence and can be interrupted, optional local speech-to-text for offline use, remote camera support over LAN or Tailscale |
| **Security** | Voice biometric login, separate memory per user, spoken confirmation before destructive actions |
| **Impact** | Accessible computer control without a keyboard or mouse |
| **Repository** | [github.com/HarisMajeed05/GestVox](https://github.com/HarisMajeed05/GestVox) |

</details>

<details>
<summary><b>Footfall Counter</b></summary>
<br/>

Real-time people counting system that runs entirely on CPU.

| | |
| --- | --- |
| **Stack** | Python, YOLO / RT-DETR, ByteTrack, OpenCV |
| **Features** | Entry and exit counting across a virtual line at any angle, with an interactive tool to set the line for any camera |
| **Scale** | Real-time video stream processing |
| **Performance** | No GPU needed, with adjustable confidence, IoU and resolution to balance accuracy and speed |
| **Reliability** | ByteTrack keeps person IDs through occlusion for stable counts |
| **Impact** | Foot traffic analytics on low-cost edge hardware |
| **Repository** | [github.com/HarisMajeed05/Footfall-counter-Yolo](https://github.com/HarisMajeed05/Footfall-counter-Yolo) |

</details>

<details>
<summary><b>Multimodal Deepfake Detection (Final Year Project)</b></summary>
<br/>

Three-stage detect, explain and judge pipeline (ExDDV-Judge) that replaces large VLMs with lightweight ones.

| | |
| --- | --- |
| **Stack** | PyTorch, BLIP-2 T5-XL, LLaVA-Mini, CLIP, DeepfakeJudge, Flask |
| **Research** | Benchmarked SBI, AltFreezing and Face Warping Detection on FaceForensics++, Celeb-DF-v2 and HiDF, showing binary detectors fall to near-chance accuracy on high quality deepfakes |
| **Scale** | Runs on a single consumer GPU |
| **Performance** | Over 80% smaller than baseline 11B and 7B VLMs |
| **Reliability** | Dual-DB routing with a fine-tuned CLIP encoder lifted real-frame accuracy from 0% to 83% |
| **Impact** | Explanations with faithfulness scores, delivered through a web app with per-frame labels and trust scores |
| **Supervisor** | Dr. Waqas Sultani, ITU Lahore |

</details>


<details>
<summary><b>C++ Compiler From Scratch</b></summary>
<br/>

Toy compiler written in C++ to learn how compilers work from first principles.

| | |
| --- | --- |
| **Stack** | C++ |
| **Features** | Lexical analysis, recursive descent parser, basic semantic checks, grammar defined in a custom specification |
| **Reliability** | Error detection during parsing |
| **Impact** | Strong systems fundamentals behind how languages and tools are built |
| **Repository** | [github.com/HarisMajeed05/Cpp-Compiler-From-Scratch](https://github.com/HarisMajeed05/Cpp-Compiler-From-Scratch) |

</details>

<details>
<summary><b>Search Engine</b></summary>
<br/>

Document search engine built from scratch in C++ using an inverted index.

| | |
| --- | --- |
| **Stack** | C++ |
| **Features** | Word and position indexing across text files, multi-condition queries, ranked results, command line interface |
| **Performance** | Inverted index for fast keyword lookup |
| **Impact** | Shows the retrieval basics that search and RAG systems build on |
| **Repository** | [github.com/HarisMajeed05/Search-Engine](https://github.com/HarisMajeed05/Search-Engine) |

</details>

---

### Experience

**AI Engineer** | MLBench Pvt Ltd | Jun 2026 to Present

- Deliver computer vision solutions for multiple client projects, from problem scoping to a working, deployed system
- Fine-tune and benchmark detection and classification models (RF-DETR, DINOv2) and pick the best one using measured metrics, not guesswork
- Build training datasets by annotating client data, and track experiments to guide model and tool choices
- Evaluate alternative models and tools such as OCR engines before they go into a pipeline
- Apply VLMs to multimodal and visual inspection problems
- Work across the full stack, from model to API to frontend, so results reach users in a usable form

`Computer Vision` `RF-DETR` `DINOv2` `VLMs` `OCR` `PyTorch` `FastAPI`

**Teaching Assistant, Software Engineering & Artificial Intelligence** | ITU Lahore | Aug 2025 to Jun 2026

- Taught and supported system design, version control, testing, search algorithms and machine learning basics
- Guided student projects on model selection, experiment design and evaluation, and reviewed code in Python, scikit-learn and PyTorch

**Earlier internships**

- Machine Learning Intern, Arch Technologies (Jun 2025 to Aug 2025): spam detection, house price prediction, digit and iris classification
- Front-End Intern, Certura (Jul 2025 to Aug 2025): responsive portfolio site and a weather dashboard using the OpenWeather API
- Salesforce Admin Intern, Incredibles (Jun 2024 to Sep 2024): data modeling, reports, dashboards and flows

---

### Education

**BS Computer Science**, Information Technology University, Lahore | Aug 2022 to Jun 2026 | CGPA 3.28/4.0

---

### GitHub Activity

<p align="center">
  <img src="https://github-profile-summary-cards.vercel.app/api/cards/stats?username=HarisMajeed05&theme=github_dark" />
</p>

<p align="center">
  <img src="https://github-profile-summary-cards.vercel.app/api/cards/repos-per-language?username=HarisMajeed05&theme=github_dark" height="200"/>
  <img src="https://github-profile-summary-cards.vercel.app/api/cards/productive-time?username=HarisMajeed05&theme=github_dark&utcOffset=5" height="200"/>
</p>

<p align="center">
  <img src="https://raw.githubusercontent.com/HarisMajeed05/HarisMajeed05/output/github-contribution-grid-snake-dark.svg" />
</p>

---

### Current Focus

Areas I am building depth in, chosen from what AI engineering teams hire for most today.

| Area | What I am working on |
| --- | --- |
| RAG Systems | Better retrieval quality, chunking, reranking and answer evaluation |
| Agentic AI | Tool-using, multi-step LLM workflows that act reliably |
| LLM Fine-tuning & Evaluation | Adapting open models to a task and measuring results properly |
| MLOps & Deployment | Containerized serving, experiment tracking and monitoring in production |
| Efficient VLMs | Lightweight vision-language models for edge deployment |

---

### Open To

| | |
| --- | --- |
| **Roles** | AI Engineer, Computer Vision Engineer, Applied ML and LLM Engineer |
| **Work I enjoy** | Taking models from experiment to production, building RAG and multimodal products, full-stack AI features |
| **Collaboration** | Computer vision and multimodal research, open source AI projects |
| **Contact** | [harismajeed0501@gmail.com](mailto:harismajeed0501@gmail.com) |

---

### Connect

<p align="center">
  <a href="https://harismajeed05.github.io/portfolio/"><img src="https://img.shields.io/badge/Portfolio-7C3AED?style=for-the-badge&logo=vercel&logoColor=white"/></a>
  <a href="mailto:harismajeed0501@gmail.com"><img src="https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white"/></a>
  <a href="https://www.linkedin.com/in/haris-majeed-raja/"><img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white"/></a>
  <a href="https://github.com/HarisMajeed05"><img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white"/></a>
</p>

<div align="center">
<i>"Build the thing from scratch once, so you know exactly what you're trusting when you don't."</i>
</div>

![Footer](https://capsule-render.vercel.app/api?type=waving&color=0:22D3EE,50:7C3AED,100:6D28D9&height=120&section=footer)