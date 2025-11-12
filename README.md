# 🌸 IRIS Classification CI/CD Scaling on GCP

![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/Achin-Aggarwal/iris-api-w7/main.yml?label=CI%2FCD%20Status&style=flat-square)
![GCP](https://img.shields.io/badge/Google%20Cloud-GKE%20%7C%20Artifact%20Registry-blue?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)

---

## 📘 Project Overview
This project demonstrates a **CI/CD pipeline with autoscaling** for a **Flask-based IRIS Classification API** deployed on **Google Kubernetes Engine (GKE)**.

The goal was to **extend the existing pipeline** to handle high concurrent loads and observe **Kubernetes Horizontal Pod Autoscaling (HPA)** behavior.

---

## 🎯 Objectives

- Automate **Build → Push → Deploy** using **GitHub Actions**
- Deploy containerized IRIS API to **Google Kubernetes Engine**
- Use **wrk** tool to simulate **1000+ concurrent requests**
- Demonstrate **HPA scaling** between `1` and `3` pods
- Observe bottlenecks when scaling restricted to `1` pod

---

## ⚙️ Architecture Overview

