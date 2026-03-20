# Vizzy Labs Coding Challenge - Interviewer Guide

**CONFIDENTIAL - DO NOT SHARE WITH CANDIDATES**

---

## Core Philosophy: Why This Format?

**The Problem with Traditional Challenges:**
Traditional coding challenges test bug-fixing skills. But AI can find and fix bugs instantly. If you give AI code and say "it's slow" or "has bugs", AI will:
- Analyze the code structure
- Identify patterns (N+1 queries, missing validation, etc.)
- Propose exact fixes
- Candidate just accepts → they proved nothing

**Our Solution:**
These challenges test what AI CANNOT do:
1. **Make business decisions** - Trade-offs require human judgment
2. **Interpret ambiguous requirements** - Conflicting stakeholder needs
3. **Prioritize under constraints** - What matters most?
4. **Design solutions** - Not "fix bugs" but "decide what to build"

**The Key Insight:**
> AI can execute. Humans must decide.

Candidates should direct AI tools, not be directed by them.

---

## How These Challenges Work

### The Code is WORKING
- No obvious bugs to find
- System runs correctly
- AI cannot "see" what needs to change

### The Problem is BUSINESS-LEVEL
- Conflicting requirements from stakeholders
- Trade-offs with no "right" answer
- Requires understanding context, not just code

### Candidates Must DECIDE
- What problem to solve first
- What approach to take
- What trade-offs to accept
- AI helps execute their decision

---

## Interview Format

### Total Time: ~22 minutes

| Phase | Duration | Your Role |
|-------|----------|-----------|
| Setup | 1 min | Confirm they can run the code |
| Diagnosis | 3-5 min | Act as stakeholder, answer questions |
| Decision | 2-3 min | Listen to their proposal |
| Implementation | 7-10 min | Observe how they use AI |
| Discussion | 5 min | Evaluate their reasoning |

### Your Role as Stakeholder

You are NOT just observing. You are playing the role of PM/stakeholder:

**When they ask questions, provide context:**
- "What's the creator churn rate?" → "About 5% of flagged creators leave within a week"
- "How many requests per second?" → "About 1000 at peak, mostly mobile"
- "What's the budget for this?" → "We need something shippable this sprint"

**When they propose solutions:**
- Ask clarifying questions
- Present trade-offs: "But what about X?"
- Don't tell them if they're "right" - there is no single right answer

---

## Challenge Details

### AI Automation Challenge

**The Situation:**
Working moderation service with conflicting stakeholder feedback:
- Creator team: Too many false positives (legitimate content flagged)
- Trust & Safety: Too many false negatives (harmful content passes)
- Engineering: No transparency or tunability

**What Good Candidates Do:**
1. Ask questions to understand the problem
   - "How often do false positives happen?"
   - "What categories have the most issues?"
   - "Is there a human review process?"

2. Propose a solution with reasoning
   - "I'd add confidence thresholds because..."
   - "We should implement human review for borderline cases..."
   - "Let me add logging first to understand the patterns..."

3. Implement with AI help
   - They tell AI WHAT to build
   - They review and adjust AI output
   - They can explain why the code does what it does

**What Weak Candidates Do:**
- Immediately ask AI "what's wrong with this code?"
- Accept whatever AI suggests
- Can't explain trade-offs
- Don't ask any clarifying questions

**Good Solutions Include:**
- Confidence thresholds
- Category-specific handling
- Human review queue
- Better prompting for edge cases
- Logging/observability
- Appeal mechanism

All are valid. We evaluate REASONING, not specific implementation.

---

### Mobile Backend Challenge

**The Situation:**
Working API with conflicting mobile team feedback:
- Slow on poor connections (but API is fast)
- High data usage (response payload size)
- No caching (repeated requests)
- Duplicate creators sometimes (pagination edge case)
- Need new analytics endpoint

**What Good Candidates Do:**
1. Investigate before coding
   - Check response size (it's large!)
   - Ask about caching requirements
   - Understand mobile-specific constraints

2. Prioritize with reasoning
   - "Payload size affects all users, I'll tackle that first"
   - "The analytics endpoint is needed for launch, but optimization affects existing users..."

3. Make design decisions
   - Create optimized response schema (fewer fields)
   - Add cache headers
   - Implement cursor-based pagination
   - Choose what to implement given time constraints

**What Weak Candidates Do:**
- Ask AI "what's wrong with this API?"
- Focus on code style instead of architecture
- Don't ask about mobile constraints
- Try to do everything without prioritizing

**Good Solutions Include:**
- Mobile-optimized response schemas (fewer fields)
- Cache-Control headers
- ETag support
- Smaller page sizes
- Cursor-based vs offset pagination
- Analytics endpoint implementation

All are valid approaches. We evaluate PRIORITIZATION and REASONING.

---

## Evaluation Framework

### What We're Actually Testing

| Skill | What to Look For |
|-------|------------------|
| **Problem Diagnosis** | Do they ask questions? Investigate before coding? |
| **Decision Making** | Can they choose between trade-offs? Explain why? |
| **Prioritization** | Do they pick high-impact work? Manage time well? |
| **AI Direction** | Do they tell AI what to build, or ask AI what's wrong? |
| **Technical Understanding** | Can they explain the code they wrote? |

### Scoring Signals

**Strong Hire Signals:**
- Asks 3+ clarifying questions before coding
- Proposes solution with clear reasoning
- Prioritizes effectively ("I'm doing X first because...")
- Directs AI with specific instructions
- Can explain all code they wrote
- Acknowledges trade-offs

**Hire Signals:**
- Some clarifying questions
- Reasonable approach
- Uses AI effectively for execution
- Can explain most of what they built

**No Hire Signals:**
- "Let me ask AI what's wrong" (AI-led, not human-led)
- Can't explain code they wrote
- No prioritization - tries random things
- Doesn't ask any questions
- Gets defensive when asked about trade-offs

---

## Running the Interview

### Phase 1: Setup (1 min)
"The challenge presents a working system with business problems. Your job is to diagnose and improve it. I'll act as your stakeholder - ask me questions."

### Phase 2: Diagnosis (3-5 min)
Let them read the README and ask questions. Answer as if you're the PM/mobile lead/etc.

Good sign: They ask questions
Bad sign: They immediately start coding

### Phase 3: Decision (2-3 min)
Ask: "What do you think the main issues are? What would you tackle first?"

Listen for reasoning, not just answers.

### Phase 4: Implementation (7-10 min)
Observe how they use AI:
- Do they give AI context and direction?
- Do they review AI output?
- Do they make corrections?

### Phase 5: Discussion (5 min)
- "Walk me through what you built and why"
- "What trade-offs did you make?"
- "What would you do differently with more time?"
- "Explain this specific piece of code"

---

## Common Scenarios

### "The code looks fine to me"
Say: "The mobile team is still having issues. What might cause sluggishness even if the API is fast?"

This tests if they think beyond code to user experience.

### They immediately ask AI "what's wrong?"
Let them. But in discussion, ask: "What did you think the problem was before AI analyzed it?"

This reveals if they're thinking or just vibing.

### They finish early
Ask them to improve their solution or add another feature. Or go deeper on discussion questions.

### They're stuck
Give business-level hints, not code hints:
- "What do mobile users care about most?"
- "How might payload size affect 3G users?"
- "What happens when the same creator ranks differently on different pages?"

---

## After the Interview

### Complete Evaluation
1. **Decision Quality** (30 points): Did they make good choices?
2. **Reasoning** (25 points): Could they explain their thinking?
3. **AI Usage** (25 points): Did they direct AI or follow AI?
4. **Technical Execution** (20 points): Does the code work?

### Recommendation Matrix

| Decision + Reasoning | AI Usage | Recommendation |
|---------------------|----------|----------------|
| Strong | Strong | **Strong Hire** |
| Strong | Weak | **Hire** (coach on AI) |
| Weak | Strong | **Maybe** (smart but not thinking) |
| Weak | Weak | **No Hire** |

---

## Key Takeaway

**We're not testing if they can write code.**
**We're testing if they can decide WHAT code to write.**

AI can write code. We need people who can:
- Understand business problems
- Make decisions with incomplete information
- Prioritize under constraints
- Direct AI tools effectively
- Explain their reasoning

That's what these challenges measure.

---

## Contact

Questions: #eng-hiring on Slack
