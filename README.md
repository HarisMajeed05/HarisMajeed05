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

I build AI systems that go from raw data to a working product. At **MLBench** I design computer vision pipelines for real client documents. Outside of that, I have built RAG assistants, a multilingual voice and gesture interface, and a lightweight multimodal deepfake detector for my final year project at ITU Lahore.

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
| LLM Apps & RAG | Document-grounded Q&A, source citations, streaming chat, per-project retrieval isolation | LangChain, FAISS, Groq, sentence-transformers |
| Multimodal & VLMs | Image-text pipelines, explanation and verification of model outputs | CLIP, BLIP-2, LLaVA-Mini, Qwen-VL, HuggingFace Transformers |
| Speech & Voice AI | Multilingual speech-to-text, streaming spoken replies, voice login | Whisper (Groq and faster-whisper) |
| Evaluation & Benchmarking | Precision, recall and F1 comparisons, cross-dataset benchmarks, OCR backend comparisons | scikit-learn, Tesseract, DocTR |
| Deployment | APIs and web apps around models, CPU-friendly and low-resource inference | FastAPI, Flask, React, MongoDB, JWT |

---

### Featured Projects

#### Legal AI Chatbot
A document-grounded legal assistant. Users upload PDFs into projects, and every answer cites its source.
- Per-project retrieval so documents from one case never leak into another
- JWT auth, conversation memory, streaming replies, PDF chat export, optional OCR for scanned files
- Runs without a GPU: LLM on Groq, small embedding model on CPU

<details>
<summary><b>Legal AI Chatbot</b></summary>
<br/>

Full-stack RAG-based legal assistant with project-scoped retrieval and source-cited answers.

| | |
| --- | --- |
| **Stack** | React, FastAPI, MongoDB, LangChain, FAISS, Groq API |
| **Scale** | Multi-project document retrieval |
| **Performance** | Low-latency retrieval via FAISS vector search |
| **Security** | Project-scoped access to prevent cross-document leakage |
| **Impact** | Source-cited answers reduce hallucination risk in legal Q&A |
| **Repository** | [github.com/HarisMajeed05/legal-ai-chatbot](https://github.com/HarisMajeed05/legal-ai-chatbot) |

</details>

**Skills shown:** RAG design, LLM integration, backend API design, full-stack delivery
**Stack:** React, FastAPI, MongoDB, LangChain, FAISS, Groq
[View repository](https://github.com/HarisMajeed05/legal-ai-chatbot)

#### GestVox
Hands-free Windows control with hand gestures and a multilingual voice assistant.
- Gesture control through MediaPipe hand tracking (cursor, click, scroll, zoom, media)
- Voice assistant that understands English, Urdu, Punjabi and mixed speech, with persistent memory and per-user voice login
- Streams replies sentence by sentence, supports interruption, and asks for spoken confirmation before risky actions

**Skills shown:** Real-time vision, speech AI, LLM tool use, system design for users
**Stack:** Python, MediaPipe, Whisper, Groq
[View repository](https://github.com/HarisMajeed05/GestVox)

#### Footfall Counter
A real-time people counter that runs fully on CPU.
- YOLO / RT-DETR detection with ByteTrack tracking that holds IDs through occlusion
- Entry and exit counting across a virtual line at any angle, with an interactive setup tool
- Tunable confidence, IoU and resolution settings for accuracy versus speed

**Skills shown:** Detection and tracking, performance tuning, edge-friendly deployment
**Stack:** Python, YOLO, RT-DETR, ByteTrack, OpenCV
[View repository](https://github.com/HarisMajeed05/Footfall-counter-Yolo)

#### Search Engine
A document search engine built from scratch using an inverted index.
- Indexes words with positions across text files
- Multi-condition queries with ranked results through a command line interface

**Skills shown:** Information retrieval fundamentals that sit under every RAG system
**Stack:** C++
[View repository](https://github.com/HarisMajeed05/Search-Engine)

#### C++ Compiler From Scratch
A toy compiler written in C++ to learn how compilers work.
- Lexical analysis, recursive descent parser and basic semantic checks
- Error detection against a custom grammar specification

**Skills shown:** Systems thinking, parsing, strong CS fundamentals
**Stack:** C++
[View repository](https://github.com/HarisMajeed05/Cpp-Compiler-From-Scratch)

#### Research Highlight: Multimodal Deepfake Detection (Final Year Project)
Supervised by Dr. Waqas Sultani, ITU Lahore.
- Benchmarked SBI, AltFreezing and Face Warping Detection on FaceForensics++, Celeb-DF-v2 and HiDF, showing that binary detectors drop to near-chance accuracy on high quality deepfakes
- Designed **ExDDV-Judge**, a detect, explain and judge pipeline using BLIP-2 T5-XL and LLaVA-Mini that cuts model size by over 80% and runs on a single consumer GPU
- Fixed a real-frame misclassification problem with a Dual-DB routing system and a fine-tuned CLIP encoder, lifting real-frame accuracy from 0% to 83%
- Shipped a Flask web app with per-frame labels, written explanations and trust scores

---

### Experience

**AI Engineer** | MLBench Pvt Ltd | Jun 2026 to Present

- Replaced a client's three-model document field detection pipeline (YOLO, FFDNet/FFDetr, geometry classifier) with a single fine-tuned RF-DETR-Base model
- Improved F1 from 0.8568 to 0.8896 (precision 0.9335, recall 0.8496) against the client's existing setup
- Compared Tesseract and DocTR for OCR and found DocTR fixed checkbox glyph misreads and low-resolution footer text errors
- Annotated client PDFs for field geometry, type and role to build the training set, and tracked experiments to guide model choice
- Contributed to a rice grain quality and variety analysis tool using DINOv2-based classifiers trained at multiple image resolutions

`Computer Vision` `RF-DETR` `DINOv2` `OCR` `PyTorch`

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

```yaml
Building:
  - Production-ready computer vision and LLM systems
  - Clean APIs and interfaces around trained models
Learning:
  - Advanced retrieval strategies for RAG systems
  - Lightweight VLM architectures for edge deployment
Improving:
  - Evaluation and benchmarking of vision and language models
```

---

### Open To

```yaml
Roles:
  - AI Engineer (computer vision, multimodal, LLM applications)
  - Applied ML and full-stack AI product work
Collaboration:
  - Computer vision and multimodal research
```

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
