# Aegis / Aegis Prime

![Build](https://img.shields.io/badge/build-passing-brightgreen)
![Coverage](https://img.shields.io/badge/coverage-92%25-green)
![License](https://img.shields.io/badge/license-MIT-blue)
![Python](https://img.shields.io/badge/python-3.10%2B-blue)
![Status](https://img.shields.io/badge/status-production--ready-success)

---
## 🏗️ Project Structure

Aegis consists of several complementary components:

| Component | Purpose |
|------------|---------|
| Aegis Core | Test execution and orchestration |
| Aegis Prime | Failure intelligence and AI analysis |
| AQL | Universal query language for systems, data, APIs, files, and infrastructure |

➡️ See the AQL documentation: ./aql/README.md
---

# ⚡ Aegis

## Testing Intelligence for Modern Engineering Teams

### 🎥 Watch Aegis in Action

See real demos, walkthroughs, and feature showcases:

➡️ [YouTube Playlist](https://www.youtube.com/playlist?list=PL2UX2VsIBUY0POiTGRRpyHesG_Oezvkba)

### Table of Contents

- Why Aegis Exists
- What Aegis Does
- AQL (Aegis Query Language)
- Hero Architecture
- What Makes It Different
- Real-World Impact
- Example Workflow
- Designed for Modern Engineering
- Vision
- Roadmap
- Built For
- License

> Turn failing tests into clear, actionable engineering decisions — not noise.

Aegis is a **testing intelligence platform** that transforms raw test failures and logs into structured insights, root cause guidance, and prioritized fixes.

Instead of spending hours digging through CI logs, teams get answers instantly:

* What broke?
* Why did it break?
* Where should I look first?

**Aegis removes the guesswork from debugging.**

---

## 🚀 Why Aegis Exists

Modern CI systems are fast — but not smart.

They tell you:

> ❌ “Tests failed”

But not:

> ❓ “What actually matters?”

Engineering teams waste time:

* Scrolling through logs
* Reproducing failures
* Chasing duplicate issues
* Interpreting unclear stack traces

Aegis fixes this by turning raw test output into **structured intelligence for developers.**

---

## 💡 What Aegis Does

### 🧠 1. Understands Failures

Groups related test failures so engineers don’t debug the same issue multiple times.

### 🔗 2. Connects System Behavior

Maps logs and failures back to services, APIs, and components.

### ⚡ 3. Prioritizes What Matters

Surfaces the most impactful failures first — not just the first one that appears.

### 🤖 4. Explains With AI (Aegis Prime)

Turns technical failures into human-readable explanations and likely root causes.

## 🔍 AQL (Aegis Query Language)

Aegis includes AQL, a universal query language that allows engineers to query databases, APIs, files, streams, and infrastructure through a single interface.

➡️ See the full AQL documentation: [AQL README](./aql/README.md)
---

## 🧭 Hero Architecture

```text
        CI / Test Pipeline (pytest, automation)
                      │
                      ▼
        ┌────────────────────────────┐
        │   Raw Test Results & Logs   │
        └─────────────┬──────────────┘
                      │
                      ▼
        ┌────────────────────────────┐
        │   Aegis Intelligence Core   │
        │                            │
        │ • Failure Detection        │
        │ • Pattern Grouping         │
        │ • Log Correlation          │
        └─────────────┬──────────────┘
                      │
                      ▼
        ┌────────────────────────────┐
        │     Aegis Prime AI Layer   │
        │                            │
        │ • Root Cause Analysis      │
        │ • Natural Language Output  │
        └─────────────┬──────────────┘
                      │
                      ▼
        ┌────────────────────────────┐
        │  Developer Action Layer    │
        │                            │
        │ • Grouped Failures        │
        │ • Prioritized Insights    │
        │ • Fix Recommendations     │
        └────────────────────────────┘
```

---

## ⚙️ What Makes It Different

Most tools stop at reporting.

Aegis goes further:

| Traditional CI Tools | Aegis                           |
| -------------------- | ------------------------------- |
| Shows failures       | Explains failures               |
| Dumps logs           | Correlates logs                 |
| Manual debugging     | AI-assisted root cause analysis |
| Flat output          | Structured intelligence         |

---

## ⚡ Real-World Impact

Teams using Aegis aim to:

* ⏱ Reduce debugging time (MTTR)
* 🚀 Improve CI feedback speed
* 🔍 Eliminate duplicate failure analysis
* 🧠 Improve engineering decision-making speed

---

## 🖥️ Example Workflow

1. Developer pushes code
2. CI runs test suite
3. Aegis analyzes failures
4. Failures are grouped + prioritized
5. AI explains likely root cause
6. Developer gets actionable next step — not raw logs

---

## 🔌 Designed for Modern Engineering

Aegis is built to fit into existing workflows:

* Works with pytest-based pipelines
* CI/CD compatible
* Extensible analysis engine
* AI provider optional (Aegis Prime layer)

---

## 🧠 Vision

Aegis is part of a shift in engineering tools:

> From **observability dashboards** → to **decision intelligence systems**

We believe the future of testing is not just detection — it’s **understanding.**

---

## 📈 Roadmap

* Web-based intelligence dashboard
* GitHub Actions / GitLab CI integrations
* Flaky test prediction engine
* Real-time failure intelligence streams
* Historical failure pattern learning

---

## 🤝 Built For

* Platform engineers
* SRE teams
* QA automation teams
* Fast-moving startup engineering orgs

---

## 📄 License

MIT License

---

## ⚡ Closing Thought

If CI tells you what broke, Aegis tells you what to do next.
