# Setup Guide for Vizzy Labs Coding Challenges

**INTERNAL DOCUMENT - DO NOT SHARE WITH CANDIDATES**

---

## Quick Reference

### Candidate Repos (Share with Candidates)

| Track | Position | GitHub Repo |
|-------|----------|-------------|
| **AI Automation** | Intern | https://github.com/Vispie-AI/vizzy-ai-automation-challenge |
| **Mobile Backend** | Full-time | https://github.com/Vispie-AI/vizzy-mobile-backend-challenge |

### Interviewer Resources

| Document | Purpose |
|----------|---------|
| `UNIFIED_INTERVIEW_GUIDE.md` | **Main guide** - All evaluation questions + scoring |
| `solutions/` | Reference solutions (never share with candidates) |

---

## Repository Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                    INTERVIEWER REPO (this one)                   │
│              github.com/Vispie-AI/vizzylabs-code-challenge      │
│                                                                  │
│  ├── ai-automation-challenge/    ← Source code                  │
│  ├── mobile-backend-challenge/   ← Source code                  │
│  └── internal/                   ← NEVER SHARE                  │
│      ├── UNIFIED_INTERVIEW_GUIDE.md                             │
│      ├── SETUP_GUIDE.md (this file)                             │
│      ├── solutions/              ← Reference answers            │
│      └── archive/                ← Old evaluation docs          │
└─────────────────────────────────────────────────────────────────┘
           │
           │ Separate repos (only code, no solutions)
           ▼
┌──────────────────────────────┐  ┌──────────────────────────────┐
│     CANDIDATE REPO #1         │  │     CANDIDATE REPO #2         │
│  vizzy-ai-automation-challenge│  │ vizzy-mobile-backend-challenge│
│                               │  │                               │
│  ✓ README.md                  │  │  ✓ README.md                  │
│  ✓ Source code                │  │  ✓ Source code                │
│  ✓ requirements.txt           │  │  ✓ requirements.txt           │
│  ✗ NO solutions               │  │  ✗ NO solutions               │
│  ✗ NO internal guides         │  │  ✗ NO internal guides         │
└──────────────────────────────┘  └──────────────────────────────┘
```

---

## Before the Interview

### 1. Invite Candidate to Repo

**For AI Automation Challenge (Intern):**
```bash
gh api repos/Vispie-AI/vizzy-ai-automation-challenge/collaborators/GITHUB_USERNAME \
  -X PUT -f permission=push
```

**For Mobile Backend Challenge (Full-time):**
```bash
gh api repos/Vispie-AI/vizzy-mobile-backend-challenge/collaborators/GITHUB_USERNAME \
  -X PUT -f permission=push
```

Or manually: GitHub repo → Settings → Collaborators → Add people

### 2. Pre-Interview Email Template

```
Subject: Vizzy Labs Interview - Technical Challenge

Hi [Name],

Here's your coding challenge for our upcoming interview:

Repo: [PASTE REPO URL]

Please:
1. Clone the repo before the interview
2. Make sure you can run `pip install -r requirements.txt`
3. Have your AI coding tool ready (Cursor, Copilot, etc.)

The challenge is 15 minutes. We'll discuss your approach afterward.

See you soon!
```

---

## Quick Setup Test

### AI Automation Challenge

```bash
cd ai-automation-challenge
pip install -r requirements.txt
uvicorn main:app --reload
```

Test endpoint:
```bash
curl -X POST "http://localhost:8000/moderate" \
  -H "Content-Type: application/json" \
  -d '{"content": "Check out my cooking tutorial!", "creator_id": "chef123"}'
```

**Expected:** Server starts, returns moderation result (the code WORKS - this is intentional)

### Mobile Backend Challenge

```bash
cd mobile-backend-challenge
pip install -r requirements.txt
uvicorn main:app --reload
```

Test endpoint:
```bash
curl "http://localhost:8000/creators/feed?page=1&page_size=20"
```

**Expected:** Server starts, returns feed data (the code WORKS - this is intentional)

---

## Interview Flow Summary

| Phase | Time | What Happens |
|-------|------|--------------|
| 1. Setup | 1 min | Confirm screen share, repo cloned |
| 2. Diagnosis | 3-5 min | Candidate reads README, asks YOU questions |
| 3. Decision | 2-3 min | Candidate proposes what to build |
| 4. Implementation | 7-10 min | Candidate codes with AI help |
| 5. Discussion | 5-7 min | AI Workflow evaluation (CRITICAL!) |

**See `UNIFIED_INTERVIEW_GUIDE.md` for detailed questions and scoring.**

---

## Important: Challenge Philosophy

**❌ These are NOT bug-fixing challenges**
- The code runs and works
- There are no obvious bugs to find

**✅ These are DECISION-MAKING challenges**
- Conflicting business requirements
- No single "right" answer
- Tests how candidates make trade-offs

**Key Question: Did they DIRECT AI, or did AI DIRECT them?**

---

## After the Interview

### Remove Candidate Access

```bash
gh api repos/Vispie-AI/vizzy-ai-automation-challenge/collaborators/GITHUB_USERNAME -X DELETE
# or
gh api repos/Vispie-AI/vizzy-mobile-backend-challenge/collaborators/GITHUB_USERNAME -X DELETE
```

### Submit Evaluation

Complete scoring in `UNIFIED_INTERVIEW_GUIDE.md` and share in #eng-hiring

---

## Syncing Candidate Repos

If you update the challenge code in this main repo, sync to candidate repos:

```bash
# AI Automation Challenge
cd /tmp
rm -rf vizzy-ai-automation-challenge
git clone git@github.com:Vispie-AI/vizzy-ai-automation-challenge.git
cp -r /path/to/vizzylabs-code-challenge/ai-automation-challenge/* vizzy-ai-automation-challenge/
cd vizzy-ai-automation-challenge
git add -A && git commit -m "Sync from main repo" && git push

# Mobile Backend Challenge
cd /tmp
rm -rf vizzy-mobile-backend-challenge
git clone git@github.com:Vispie-AI/vizzy-mobile-backend-challenge.git
cp -r /path/to/vizzylabs-code-challenge/mobile-backend-challenge/* vizzy-mobile-backend-challenge/
cd vizzy-mobile-backend-challenge
git add -A && git commit -m "Sync from main repo" && git push
```

---

## Troubleshooting

### "No module named 'fastapi'"
```bash
pip install -r requirements.txt
```

### "Port 8000 already in use"
```bash
uvicorn main:app --port 8001
```

### "Database not seeding" (Mobile Backend)
Restart the app - seed_data runs on startup

---

## Support

Questions: #eng-hiring on Slack
