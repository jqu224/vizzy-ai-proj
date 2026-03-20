# Vizzy Labs Coding Challenge - Unified Interview Guide

**CONFIDENTIAL - DO NOT SHARE WITH CANDIDATES**

---

## Quick Reference

| Track | Position | Time | Key Focus |
|-------|----------|------|-----------|
| **AI Automation** | Intern | 15 min coding + 5-7 min discussion | Decision-making on conflicting requirements |
| **Mobile Backend** | Full-time | 15 min coding + 5-7 min discussion | Prioritization + mobile optimization |

---

## Core Philosophy

> **We're NOT testing bug-fixing. We're testing decision-making.**

AI can find and fix bugs instantly. These challenges test what AI CANNOT do:
- Make business decisions (trade-offs require human judgment)
- Interpret ambiguous requirements (conflicting stakeholder needs)
- Prioritize under constraints (what matters most?)

**Key Question Throughout: Did they DIRECT AI, or did AI DIRECT them?**

---

# PART 1: INTERVIEW FLOW

## Total Time: ~22 minutes

| Phase | Time | What Happens |
|-------|------|--------------|
| 1. Setup | 1 min | Confirm they can run code |
| 2. Diagnosis | 3-5 min | They read README, ask YOU questions |
| 3. Decision | 2-3 min | They propose what to tackle first |
| 4. Implementation | 7-10 min | They code with AI help |
| 5. Discussion | 5-7 min | **AI Workflow Evaluation** (critical!) |

---

## Phase 1: Setup (1 min)

**Say:**
> "This challenge presents a working system with business problems. Your job is to diagnose, decide, and improve. I'll act as your stakeholder - ask me questions. Feel free to use AI tools."

**Confirm they can run:**
```bash
# AI Automation
cd ai-automation-challenge && pip install -r requirements.txt && uvicorn main:app --reload

# Mobile Backend
cd mobile-backend-challenge && pip install -r requirements.txt && uvicorn main:app --reload
```

---

## Phase 2: Diagnosis (3-5 min)

**Your Role:** You are the PM/stakeholder. Answer their questions realistically.

### Signal Assessment

| Signal | What It Means |
|--------|---------------|
| ✅ **Good:** Asks 3+ questions | Understands they need context |
| ✅ **Good:** Investigates code | Wants to understand before changing |
| ⚠️ **Okay:** Asks 1-2 questions | Moving quickly but aware |
| ❌ **Bad:** Jumps to AI immediately | "What's wrong with this code?" |
| ❌ **Bad:** No questions at all | Not diagnosing, just doing |

### Context to Provide When Asked

**AI Automation Track:**
| Question | Answer |
|----------|--------|
| "How often do false positives happen?" | "~50 tickets/week, mostly cooking/fitness content" |
| "What's the creator churn rate?" | "About 5% of flagged creators leave within a week" |
| "Is there human review?" | "Not currently - that's one of the issues" |
| "What categories have the most issues?" | "Violence (cooking) and Adult (fitness)" |

**Mobile Backend Track:**
| Question | Answer |
|----------|--------|
| "How many requests per second?" | "About 1000 at peak, mostly mobile" |
| "What's the average response size?" | "About 15KB per page - check it yourself" |
| "Do we use any caching?" | "Not currently on the API side" |
| "How often does pagination duplication happen?" | "QA says about 5% of sessions" |

---

## Phase 3: Decision (2-3 min)

**Ask:**
> "What do you think the main issues are? What would you tackle first, and why?"

### What to Listen For

| Good Response | Bad Response |
|---------------|--------------|
| "I'd prioritize X because it affects Y users" | "I'll just fix everything" |
| "There's a trade-off between A and B..." | "Let me ask AI what's wrong" |
| "Given 15 minutes, the highest impact is..." | No prioritization mentioned |

### Record Their Plan
Write down their stated approach - you'll compare this to what actually happened in Phase 5.

**Their stated plan:**
1. _______________________
2. _______________________
3. _______________________

---

## Phase 4: Implementation (7-10 min)

**Your Role:** Observe silently. Take notes on their AI usage.

### Observation Checklist

**Watch for:**
- [ ] Do they give AI context before asking for code?
- [ ] Do they read AI output before accepting?
- [ ] Do they iterate on prompts?
- [ ] Do they make manual corrections?
- [ ] Do they test their changes?

**Note specific examples:**
- Prompt they gave: _______________________
- How they reviewed output: _______________________
- Corrections they made: _______________________

### If They Get Stuck

Give **business hints**, not code hints:
- "What do mobile users care about most?"
- "How might payload size affect 3G users?"
- "What's the worst case if a false positive happens?"

---

## Phase 5: Discussion & AI Workflow Evaluation (5-7 min)

**⚠️ THIS IS CRITICAL - Don't skip this!**

This phase evaluates whether they truly understand AI-assisted development or are just "vibe coding."

### Question 1: Prompt Construction (2 min)

**Ask:**
> "Walk me through how you structured your prompts to the AI. What was your reasoning?"

**Follow-up:**
> "Show me an example of a prompt you gave. Would you change anything about it now?"

**Listen for:**
| Green Flags | Red Flags |
|-------------|-----------|
| "I gave context about the architecture first" | "I just asked it to fix everything" |
| "I asked for specific changes rather than general fixes" | "I don't remember what I typed" |
| "I had to refine my prompt because..." | "I just accepted whatever it suggested" |

**Score:** ___/10

---

### Question 2: Workflow & Planning (2 min)

**Ask:**
> "How well did the AI follow your original plan? Did it go off course at any point?"

**Follow-up:**
> "Was there a point where you disagreed with what the AI suggested? What did you do?"

**Compare to their stated plan from Phase 3:**
- Did they stick to the plan? □ Yes □ Partially □ No
- Did they notice deviations? □ Yes □ No
- Did they course-correct? □ Yes □ No

**Listen for:**
| Green Flags | Red Flags |
|-------------|-----------|
| "AI wanted to do X but I kept it focused on Y" | "I just accepted everything" |
| "I modified the output because it missed this edge case" | "The AI knows better than me" |
| "The AI suggested X, but I knew that wouldn't work because Y" | "I didn't notice anything wrong" |

**Score:** ___/15

---

### Question 3: Step-by-Step Breakdown (2 min)

**Ask:**
> "Walk me through what the AI did at each step. What commands or tools did it use? What was the purpose of each?"

**Then point to a specific piece of code and ask:**
> "Explain this code. Why does it work?"

**For AI Automation, ask about:**
- The fallback chain / confidence threshold logic
- The prompt structure for moderation
- The error handling pattern

**For Mobile Backend, ask about:**
- The query optimization approach
- The cache header implementation
- The pagination logic

**Listen for:**
| Green Flags | Red Flags |
|-------------|-----------|
| Names each tool/command, explains purpose | Cannot recall what AI did |
| Explains code fluently, understands concepts | "That's what the AI generated" |
| Knows why this approach vs alternatives | Cannot modify when asked |

**Score:** ___/20

---

### Question 4: AI Correction Capability (1 min)

**Ask:**
> "Was there anything you had to manually correct in the AI's output? Show me."

**OR if they accepted everything:**
> "If the AI had generated code with a subtle bug, how would you catch it?"

**Score:** ___/10

---

# PART 2: SCORING

## Quick Scoring Sheet

### Section A: Problem Diagnosis (25 points)
| Score | Behavior |
|-------|----------|
| 23-25 | Asked 4+ questions, understood constraints, identified trade-offs |
| 18-22 | Asked 2-3 good questions, reasonable understanding |
| 12-17 | Asked 1 question, moved to coding quickly |
| 6-11 | Briefly read README, went straight to AI/code |
| 0-5 | No investigation, immediately asked AI "what's wrong?" |

**Score: ___/25**

### Section B: Decision Quality (30 points)
| Score | Behavior |
|-------|----------|
| 27-30 | Clear reasoning, addressed root cause, acknowledged trade-offs |
| 21-26 | Good approach, explained reasoning, reasonable prioritization |
| 15-20 | Okay approach, limited reasoning given |
| 8-14 | Random approach, couldn't explain why |
| 0-7 | No decision - did whatever AI suggested |

**Score: ___/30**

### Section C: AI Workflow Understanding (55 points)
| Component | Max | Score |
|-----------|-----|-------|
| Prompt Construction | 10 | ___/10 |
| Workflow & Planning | 15 | ___/15 |
| Step-by-Step Breakdown | 20 | ___/20 |
| AI Correction Capability | 10 | ___/10 |

**Score: ___/55**

### Section D: Technical Execution (20 points)
| Score | Result |
|-------|--------|
| 18-20 | Code works, well-structured, addresses the issue |
| 14-17 | Code mostly works, reasonable structure |
| 10-13 | Code partially works, has some issues |
| 5-9 | Code doesn't work well, poor structure |
| 0-4 | Minimal progress, major issues |

**Score: ___/20**

---

## Total Score Calculation

| Section | Max | Score |
|---------|-----|-------|
| A: Problem Diagnosis | 25 | |
| B: Decision Quality | 30 | |
| C: AI Workflow Understanding | 55 | |
| D: Technical Execution | 20 | |
| **TOTAL** | **130** | |

---

## Recommendation Matrix

### By Total Score

| Score | Recommendation |
|-------|----------------|
| 105-130 | **Strong Hire** |
| 85-104 | **Hire** |
| 65-84 | **Maybe** - Discuss |
| <65 | **No Hire** |

### By Track (Adjust for Position Level)

**AI Automation Intern:**
- Score 75+ with AI Workflow ≥35 = **Hire** (can be trained)
- Strong reasoning compensates for less technical polish

**Mobile Backend Full-time:**
- Score 95+ with AI Workflow ≥40 = **Strong Hire**
- Expect stronger technical execution and prioritization

### Decision Matrix

| Technical + Decision | AI Workflow | Recommendation |
|---------------------|-------------|----------------|
| Strong | Strong (40+) | **Strong Hire** |
| Strong | Moderate (25-39) | **Hire** (coach on AI) |
| Moderate | Strong (40+) | **Maybe** (smart but needs guidance) |
| Weak | Any | **No Hire** |
| Any | Weak (<25) | **No Hire** (vibe coder) |

---

# PART 3: RED FLAGS & GREEN FLAGS

## Red Flags Checklist

**Vibe Coding Indicators:**
- [ ] Cannot explain what specific code does
- [ ] No memory of prompts used
- [ ] No plan before starting
- [ ] Accepted first AI output without iteration
- [ ] "The AI just figured it out"
- [ ] Over-reliance: "I couldn't have done it without AI"

**Black-box User:**
- [ ] Asked AI "what's wrong with this code?" (immediate disqualifier)
- [ ] Code works but candidate can't explain why
- [ ] Cannot modify AI output when asked
- [ ] Defensive about AI choices ("AI knows best")

**Lack of Agency:**
- [ ] Followed AI suggestions even when clearly wrong
- [ ] No evidence of redirecting or correcting AI
- [ ] Cannot articulate disagreements with AI choices

## Green Flags Checklist

**Deliberate AI Usage:**
- [ ] Structured prompts with context
- [ ] Iterative refinement based on output
- [ ] Clear understanding of when to use AI vs manual coding
- [ ] Selective acceptance of AI suggestions

**Maintained Control:**
- [ ] Had a plan before AI interaction
- [ ] Corrected AI when it deviated
- [ ] Made manual improvements to AI output
- [ ] Could identify AI mistakes or suboptimal solutions

**Deep Understanding:**
- [ ] Can explain all AI-generated code
- [ ] Understands trade-offs of chosen approach
- [ ] Can suggest alternatives
- [ ] Can modify AI output confidently

---

# PART 4: TRACK-SPECIFIC NOTES

## AI Automation Track (Intern)

**The Challenge:** Conflicting requirements between Creator Success (fewer false positives) and Trust & Safety (fewer false negatives).

**Good Solutions Include:**
- Confidence thresholds
- Category-specific handling
- Human review queue
- Better prompting for edge cases
- Logging/observability
- Appeal mechanism

**What Distinguishes Strong Candidates:**
- Asks about creator churn impact
- Considers both stakeholder perspectives
- Proposes phased approach
- Acknowledges trade-offs explicitly

**Intern-Specific Calibration:**
- Accept less polished code if reasoning is strong
- Value learning orientation and curiosity
- Look for growth potential over perfection

## Mobile Backend Track (Full-time)

**The Challenge:** Multiple issues (slow on mobile, high data usage, no caching, pagination duplicates, missing analytics endpoint).

**Good Solutions Include:**
- Mobile-optimized response schemas (fewer fields)
- Cache-Control headers / ETag support
- Smaller page sizes
- Cursor-based vs offset pagination
- Analytics endpoint implementation

**What Distinguishes Strong Candidates:**
- Investigates response size immediately
- Prioritizes based on user impact
- Understands mobile-specific constraints (3G, data caps)
- Makes trade-offs explicit ("I chose X over Y because...")

**Full-time-Specific Calibration:**
- Expect strong technical execution
- Expect clear prioritization reasoning
- Should demonstrate ownership mindset
- Should ask about production constraints

---

# PART 5: POST-INTERVIEW

## Summary Template

**Candidate:** _______________________
**Position:** [ ] AI Automation Intern  [ ] Mobile Backend Full-time
**Date:** _______________________
**Interviewer:** _______________________

### Scores
| Section | Score | Max |
|---------|-------|-----|
| Problem Diagnosis | | 25 |
| Decision Quality | | 30 |
| AI Workflow | | 55 |
| Technical Execution | | 20 |
| **TOTAL** | | **130** |

### Key Observations

**Strengths:**
1. _______________________
2. _______________________

**Concerns:**
1. _______________________
2. _______________________

**AI Usage Pattern:**
[ ] Expert (directs AI, understands output, corrects mistakes)
[ ] Proficient (good usage, some areas for growth)
[ ] Developing (tends toward black-box usage)
[ ] Vibe Coder (treats AI as magic)

### Recommendation

[ ] **Strong Hire** - Demonstrated strong decision-making AND AI understanding
[ ] **Hire** - Solid performance, can be coached on areas of growth
[ ] **Maybe** - Discuss with team, specific concerns: _______________________
[ ] **No Hire** - Reason: _______________________

### 2-3 Sentence Summary
_______________________
_______________________
_______________________

---

## Contact

Questions: #eng-hiring on Slack
