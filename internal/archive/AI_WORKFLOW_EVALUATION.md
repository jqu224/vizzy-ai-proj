# AI Workflow Evaluation Framework

**Purpose:** Evaluate whether candidates truly understand AI-assisted development or are just "vibe coding" (treating AI as a black box).

This framework goes beyond checking if the code works. It assesses whether the candidate:
1. Understands what the AI is doing
2. Can direct and correct AI when needed
3. Has a mental model of the implementation
4. Can explain and defend their approach

---

## When to Use This Framework

Conduct this evaluation **after the coding portion** (during the 5-minute discussion phase). Use these questions to probe the candidate's understanding of their AI-assisted development process.

---

## Part 1: Prompt Construction (10 points)

**Goal:** Understand how the candidate communicates with AI and why they structured their prompts the way they did.

### Questions to Ask

**1.1 "Walk me through how you structured your prompts to the AI. What was your reasoning?"**

Listen for:
- [ ] **Deliberate structure** - Did they provide context before asking for code?
- [ ] **Specificity** - Did they give the AI specific requirements vs vague requests?
- [ ] **Iteration awareness** - Did they refine prompts based on AI output?
- [ ] **Constraint setting** - Did they specify what NOT to do?

**Scoring:**
| Response Quality | Points |
|-----------------|--------|
| Clear reasoning, deliberate prompt structure, explains why | 9-10 |
| Some reasoning, generally good prompts | 6-8 |
| Vague or generic prompts, limited reasoning | 3-5 |
| No clear prompting strategy, just accepting first output | 0-2 |

**1.2 "Show me an example of a prompt you gave the AI. Would you change anything about it now?"**

Listen for:
- [ ] **Self-awareness** - Can they critique their own prompts?
- [ ] **Learning** - Did they adapt their approach during the challenge?
- [ ] **Specificity** - Were prompts targeted or generic "fix this"?

**Red Flags:**
- "I just asked it to fix everything"
- "I don't remember what I typed"
- "I just accepted whatever it suggested"

**Green Flags:**
- "I gave it context about the architecture first"
- "I asked for specific changes rather than general fixes"
- "I had to refine my prompt because the first output didn't match what I needed"

---

## Part 2: Workflow & Planning (15 points)

**Goal:** Assess whether the candidate had a plan before using AI, and whether they could evaluate if AI followed that plan.

### Pre-Implementation Questions

**2.1 "Before you started coding, what was your mental plan for approaching this challenge?"**

Listen for:
- [ ] **Problem decomposition** - Did they break down the problem?
- [ ] **Prioritization** - Did they have an order of operations?
- [ ] **Risk identification** - Did they identify potential blockers?

**Scoring:**
| Response Quality | Points |
|-----------------|--------|
| Clear plan with prioritized steps, identified risks | 7-8 |
| General plan, some prioritization | 4-6 |
| Vague plan, unclear ordering | 2-3 |
| No plan, just started asking AI | 0-1 |

### Post-Implementation Questions

**2.2 "How well did the AI follow your original plan? Did it go off course at any point?"**

Listen for:
- [ ] **Deviation awareness** - Did they notice when AI diverged from the plan?
- [ ] **Course correction** - Did they redirect the AI when needed?
- [ ] **Adaptation** - Did they update their plan based on what AI revealed?

**Scoring:**
| Response Quality | Points |
|-----------------|--------|
| Clear awareness of deviations, corrected course | 6-7 |
| Some awareness, occasional corrections | 3-5 |
| Limited awareness, mostly followed AI's lead | 1-2 |
| No plan to compare against | 0 |

**2.3 "Was there a point where you disagreed with what the AI suggested? What did you do?"**

Listen for:
- [ ] **Critical evaluation** - Can they evaluate AI suggestions objectively?
- [ ] **Independence** - Will they override AI when they know better?
- [ ] **Judgment** - Do they understand when AI is right vs wrong?

**Red Flags:**
- "I just accepted everything it suggested"
- "The AI knows better than me"
- "I didn't notice anything wrong"

**Green Flags:**
- "The AI suggested X, but I knew that wouldn't work because Y"
- "I asked it to redo the implementation with these constraints"
- "I modified the AI's output because it missed this edge case"

---

## Part 3: Step-by-Step Breakdown (20 points)

**Goal:** Verify the candidate understands what the AI did at each step, not just that it worked.

### Technical Understanding Questions

**3.1 "Walk me through the commands or tools the AI used. What was the purpose of each one?"**

Listen for:
- [ ] **Tool awareness** - Can they name the tools/commands AI used?
- [ ] **Purpose understanding** - Do they know why each tool was used?
- [ ] **Flow comprehension** - Can they trace the logical flow?

**Scoring:**
| Response Quality | Points |
|-----------------|--------|
| Names each tool/command, explains purpose and flow | 7-8 |
| Identifies most tools, explains main purposes | 4-6 |
| Limited recall, vague understanding | 2-3 |
| Cannot explain what AI did | 0-1 |

**3.2 "Explain [specific piece of code the AI generated]. Why does this work?"**

Pick a non-trivial piece of AI-generated code and ask them to explain it.

Listen for:
- [ ] **Code comprehension** - Can they read and explain the code?
- [ ] **Concept understanding** - Do they understand the underlying concepts?
- [ ] **Trade-off awareness** - Do they know why this approach vs alternatives?

**For AI Challenge, ask about:**
- The fallback chain implementation
- The Pydantic validator logic
- The async/await error handling pattern
- The prompt structure for Anthropic

**For Mobile Challenge, ask about:**
- The query optimization approach
- Why this eliminates the performance issue
- The engagement calculation
- The pagination logic

**Scoring:**
| Response Quality | Points |
|-----------------|--------|
| Explains code fluently, understands concepts | 7-8 |
| Generally understands, some gaps | 4-6 |
| Surface-level understanding, misses key concepts | 2-3 |
| Cannot explain the code | 0-1 |

### Implementation Classification Questions

**3.3 "Which parts of your solution were the original plan vs adjustments made during implementation?"**

Listen for:
- [ ] **Self-awareness** - Can they distinguish planned vs reactive changes?
- [ ] **Transparency** - Are they honest about what was improvised?
- [ ] **Learning** - Did they incorporate lessons from AI interactions?

**Scoring:**
| Response Quality | Points |
|-----------------|--------|
| Clear distinction, explains both planned and reactive | 3-4 |
| Some distinction, generally aware | 2 |
| Cannot distinguish, everything blended together | 0-1 |

---

## Part 4: AI Correction Capability (10 points)

**Goal:** Assess whether the candidate can identify and correct AI mistakes.

### Scenario Question

**4.1 "If the AI had generated code with a subtle bug (like a race condition or security issue), how would you catch it?"**

Listen for:
- [ ] **Review process** - Do they have a systematic review approach?
- [ ] **Testing awareness** - Would they test AI-generated code?
- [ ] **Domain knowledge** - Can they apply their expertise to validate AI output?

**Scoring:**
| Response Quality | Points |
|-----------------|--------|
| Describes systematic review process, specific checks | 4-5 |
| General review approach, some specific checks | 2-3 |
| Vague or no review process | 0-1 |

### Correction Demonstration

**4.2 "Was there anything you had to manually correct in the AI's output? Show me."**

If they made manual corrections, this is a **positive signal** showing they:
- Critically evaluated AI output
- Had sufficient knowledge to identify issues
- Weren't blindly accepting suggestions

**Scoring:**
| Response Quality | Points |
|-----------------|--------|
| Identified and corrected meaningful issues | 4-5 |
| Minor corrections or improvements | 2-3 |
| Accepted all AI output without changes | 0-1 |

---

## Scoring Summary

| Category | Max Points |
|----------|-----------|
| Part 1: Prompt Construction | 10 |
| Part 2: Workflow & Planning | 15 |
| Part 3: Step-by-Step Breakdown | 20 |
| Part 4: AI Correction Capability | 10 |
| **Total AI Workflow Score** | **55** |

### AI Workflow Score Interpretation

| Score | Interpretation |
|-------|----------------|
| 45-55 | **Expert AI User** - Understands AI as a tool, maintains control and oversight |
| 35-44 | **Proficient AI User** - Good understanding, some areas for growth |
| 25-34 | **Developing AI User** - Basic understanding, tends toward black-box usage |
| 15-24 | **Novice AI User** - Limited understanding, mostly vibe coding |
| 0-14 | **Black-box User** - Treats AI as magic, no understanding of process |

---

## Red Flags Checklist

During the evaluation, watch for these warning signs:

### Vibe Coding Indicators
- [ ] Cannot explain what specific code does
- [ ] No memory of prompts used
- [ ] No plan before starting
- [ ] Accepted first AI output without iteration
- [ ] Cannot distinguish AI-generated vs planned code
- [ ] No corrections or critical evaluation
- [ ] "The AI just figured it out"
- [ ] Over-reliance: "I couldn't have done it without AI"

### Copy-Paste Without Understanding
- [ ] Code works but candidate can't explain why
- [ ] Cannot modify AI output when asked
- [ ] Doesn't know why certain patterns were used
- [ ] Cannot identify trade-offs or alternatives

### Lack of Agency
- [ ] Followed AI suggestions even when clearly wrong
- [ ] No evidence of redirecting or correcting AI
- [ ] Cannot articulate disagreements with AI choices
- [ ] Defensive about AI choices ("AI knows best")

---

## Green Flags Checklist

Signs of a candidate who truly understands AI-assisted development:

### Deliberate AI Usage
- [ ] Structured prompts with context
- [ ] Iterative refinement based on output
- [ ] Clear understanding of when to use AI vs manual coding
- [ ] Selective acceptance of AI suggestions

### Maintained Control
- [ ] Had a plan before AI interaction
- [ ] Corrected AI when it deviated
- [ ] Made manual improvements to AI output
- [ ] Could identify AI mistakes or suboptimal solutions

### Deep Understanding
- [ ] Can explain all AI-generated code
- [ ] Understands trade-offs of chosen approach
- [ ] Can suggest alternatives
- [ ] Can modify AI output confidently

### Learning Orientation
- [ ] Learned something from AI during the challenge
- [ ] Updated mental model based on AI interaction
- [ ] Can articulate what they'd do differently

---

## Recommended Interview Flow

### During Coding (15 minutes)
**Observe silently, take notes:**
- How do they interact with AI?
- Do they read AI output before accepting?
- Do they iterate on prompts?
- Do they make manual corrections?
- Do they test their changes?

### After Coding (5-7 minutes)
**Use this framework:**
1. Start with a prompt construction question (1-2 min)
2. Ask about their workflow and planning (1-2 min)
3. Pick one piece of code for step-by-step breakdown (2-3 min)
4. If time, ask about corrections or disagreements

### Scoring
1. Complete the technical scoring sheet first
2. Complete this AI Workflow evaluation
3. Combine scores for final recommendation

---

## Final Recommendation Guidance

### Strong Hire Indicators
- Technical score: 70+ AND
- AI Workflow score: 35+ AND
- No major red flags

### Hire with Growth Potential
- Technical score: 70+ AND
- AI Workflow score: 25-34 AND
- Shows learning orientation
- Can be coached on AI best practices

### No Hire Indicators
- AI Workflow score: <25 regardless of technical score
- Multiple red flags present
- Cannot explain code they "wrote"
- Over-reliance without understanding

---

## Notes for Interviewers

1. **This is not about AI being "bad"** - We want developers who can leverage AI effectively, not avoid it.

2. **Understanding > Completion** - A candidate who completes 70% but understands everything is better than one who completes 100% but can't explain it.

3. **We're testing collaboration skills** - Working with AI is a form of collaboration. Good collaborators understand their partner's contributions.

4. **Calibrate expectations** - Not everyone will score 45+. A score of 35+ with good technical skills is a solid candidate.

5. **Look for potential** - If a candidate shows awareness of gaps and learning orientation, that's valuable.

---

## Example Evaluation Notes

### Example: Strong Candidate

> **Prompt Construction (8/10):** "I first gave the AI context about the service architecture, then asked specifically about the validation pattern. When it gave me a generic validator, I asked it to use Pydantic's @validator specifically."

> **Workflow (13/15):** "My plan was: fix validation first because it's quick, then tackle the service layer, then initialization. The AI wanted to do everything at once but I kept it focused on one thing at a time."

> **Step-by-Step (16/20):** Could explain the async/await pattern and why wait_for was used. Slight confusion about exception chaining but understood the concept.

> **Correction (8/10):** "The AI initially used a try/except that was too broad. I narrowed it to specific exceptions."

> **Total: 45/55 - Strong AI user with good technical understanding**

### Example: Concerning Candidate

> **Prompt Construction (3/10):** "I just told it to fix the bugs and it did."

> **Workflow (4/15):** "I didn't really have a plan, I just started with what seemed obvious."

> **Step-by-Step (5/20):** Could not explain why asyncio.wait_for was used. When asked about the validator, said "that's what the AI generated."

> **Correction (2/10):** "Everything worked so I didn't change anything."

> **Total: 14/55 - Black-box user, does not understand the code**

---

*This framework should be used alongside the technical scoring sheet for a complete candidate evaluation.*
