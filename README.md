# 🧵 Threads Auto Uploader

Threads Uploader is a lightweight Python project for publishing content to
Threads using the official API provided by Meta.

The repository is designed with clarity and long-term maintainability in mind.
It avoids browser-level automation and instead relies on direct HTTP requests,
making the behavior predictable and easier to extend.

---

## 📌 Overview

This project provides a small command-line interface and a modular Python API
that allows you to publish content to Threads programmatically.

The focus is on:

- 🧩 clean structure  
- 🧼 minimal dependencies  
- 📖 readable code  
- 🧱 clear separation of responsibilities  

It can be used as a standalone utility or as a building block inside a larger
content or automation pipeline.

---

## 🖼 Supported Content Types

The uploader currently supports:

- ✍️ Text-only posts  
- 🖼 Image posts via public image URLs  
- 🎥 Video posts via public video URLs  

Each content type can optionally include a caption where supported by the API.

---

## 🧠 Design Principles

- ✅ Uses the official Threads API  
- 🚫 Avoids browser automation and UI-level interaction  
- 🔐 Keeps configuration external to the codebase  
- 🎯 Prefers explicit behavior over implicit side effects  
- 🛠 Designed to be easy to read and modify  

The project structure mirrors these goals by keeping API logic, media handling,
and CLI logic separate.

---

## ⚙️ Requirements

- 🐍 Python 3.9 or newer  
- 🔑 A valid Threads API access token  
- 👤 A Threads user ID associated with the token  

All external dependencies are listed in `requirements.txt`.

