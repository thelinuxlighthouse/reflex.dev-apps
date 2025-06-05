# Reflex.dev Apps Collection

This repository contains my Reflex.dev projects — starting with a real-time **System Monitoring Dashboard** that displays live CPU, memory, and disk usage in your browser.

## 💡 About

[Reflex.dev](https://reflex.dev) is a modern Python framework that compiles frontend code from Python functions into a performant, real-time web application using React under the hood — all without writing JavaScript.

This repo serves as both a learning journey and a toolbox for building web apps using Reflex. It will grow to include more apps and features over time.

---

## 🚀 Projects

### 1. 📊 System Monitoring Dashboard

A responsive Reflex web app that:
- Displays live CPU, memory, and disk usage
- Uses Python backend + real-time frontend updates
- Requires **no JavaScript**

![Dashboard Screenshot](./screenshot.png)

---

## 📦 Tech Stack

- **Reflex.dev** (Python-based fullstack web framework)
- **psutil** for system metrics
- **distro** for system info

---

## 🧰 Requirements

- Python 3.13+
- Reflex CLI (`pip install reflex`)

---

## ▶️ Running the App

```bash
git clone https://github.com/YOUR_USERNAME/reflex.dev-apps.git
cd reflex.dev-apps/dashboard
reflex run
