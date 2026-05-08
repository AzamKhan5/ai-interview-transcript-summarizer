# Prompt Iterations

This document contains the 3 main prompt iterations used while building the interview transcript summarizer.  
The goal was to create a prompt that works well for both:

- Technical interviews (Frontend/Mobile Engineer transcript)
- Operations/Program Management interviews

---

# Iteration 1

## Full Prompt

```text
Analyze the following interview transcript and summarize the candidate.

Transcript:
{transcript}
```

---

## Input Used (Technical Transcript)

```text
Candidate: I have around nine plus years of experience in software development.
My core expertise is Angular, React and Ionic framework.
I worked on mobile applications and service-based applications.
```

---

## Output Produced

```text
The candidate has experience in software development and frontend technologies.
They worked on Angular, React and mobile applications.
The candidate appears technically skilled and experienced.
```

---

## What Worked

- The model understood the general topic of the interview.
- It correctly identified frontend and mobile development experience.
- The summary was readable and short.

## What Didn't Work

- The output was too generic and lacked structure.
- It did not identify candidate role fit or seniority.
- Important discussion topics were missing.
- The same prompt performed poorly on the management transcript because it generated very shallow summaries.

## Changes Made for Next Iteration

For the next version, I decided to:
- explicitly ask for sections,
- include role/profile prediction,
- and request strengths and weaknesses separately.

---

# Iteration 2

## Full Prompt

```text
Analyze the interview transcript and provide:

1. Main topics discussed
2. Candidate role fit
3. Candidate strengths
4. Candidate weaknesses
5. Overall summary

Keep the response concise.

Transcript:
{transcript}
```

---

## Input Used (Management Transcript)

```text
Candidate: I built fraud detection dashboards and worked with vendors.
I collaborated with leadership teams and handled KPIs and BRDs.
I managed operations and analytics.
```

---

## Output Produced

```text
Main Topics:
- Fraud detection
- Vendor management
- Analytics
- KPI tracking

Role Fit:
Operations Manager

Strengths:
- Leadership
- Stakeholder management
- Data analysis

Weaknesses:
- Communication clarity

Overall Summary:
The candidate has experience in operations, analytics and fraud prevention systems. 
They appear suitable for operational leadership roles.
```

---

## What Worked

- The structure became much clearer.
- The model handled the management transcript better.
- Role prediction improved significantly.
- Strengths and weaknesses became more specific.

## What Didn't Work

- Formatting was inconsistent across transcripts.
- Sometimes the model gave very short outputs.
- Candidate summaries lacked detailed overall impression.
- Technical transcript responses still missed deeper engineering themes like state management and scalable architecture.

## Changes Made for Next Iteration

For the final version, I:
- added stricter formatting instructions,
- requested bullet points,
- added sentence limits,
- and explicitly asked for background, strengths, concerns, and overall impression.

This was done to make outputs more consistent across both transcript styles.

---

# Iteration 3 (Final Version)

## Full Prompt

```text
You are an interview transcript analyzer.

Read the transcript carefully and generate a structured summary with exactly these 3 sections:

1. Topics Covered
- Mention the major themes discussed in the interview.
- Use bullet points.
- Focus on technical, managerial, behavioral, or domain-specific topics.

2. Profile
- Identify the most suitable candidate profile or role.
- Mention probable seniority level if possible.
- Give a short justification based on the transcript.

3. Candidate Summary
- Write a short paragraph of 3 to 6 sentences.
- Include:
  - candidate background
  - strengths
  - concerns or weaknesses
  - communication or leadership observations
  - overall hiring impression

Keep the response clean, concise, and professional.
Do not hallucinate information outside the transcript.

Transcript:
{transcript}
```

---

## Input Used (Technical Transcript)

```text
Candidate: I worked mostly on Angular, React and Ionic applications.
I used AI tools like Cursor and GitHub Copilot.
I focused on reusable components, API integration and scalable architecture.
```

---

## Output Produced

```text
Topics Covered
- Angular and React development
- Ionic mobile application architecture
- AI-assisted coding tools
- State management
- API integration
- Reusable UI components

Profile
Frontend/Mobile Engineer — Mid to Senior Level

The candidate demonstrates strong experience in Angular, React, Ionic and hybrid mobile application development. Their discussion around reusable architecture, API integration and AI-assisted workflows indicates practical industry experience.

Candidate Summary

The candidate has around nine years of experience in frontend and hybrid mobile application development. They demonstrated solid understanding of Angular, React, Ionic, reusable UI architecture and API integration. The candidate also showed familiarity with AI-assisted coding tools such as Cursor and GitHub Copilot. One concern was limited confidence in advanced state management concepts like Zustand and Redux slice implementation. Overall, the candidate appears suitable for a mid-to-senior frontend or mobile engineering role.
```

---

## What Worked

- The formatting became consistent across both transcripts.
- The prompt handled technical and management interviews reasonably well.
- Outputs became more informative while still staying concise.
- Explicit instructions improved profile prediction and candidate summaries.
- Asking the model not to hallucinate reduced random assumptions.

## Remaining Limitations

- Seniority prediction can still be imperfect when transcripts are vague.
- Communication quality assessment depends heavily on transcript clarity.
- Sometimes the model overemphasizes frequently repeated topics in long transcripts.

## Why This Became the Final Prompt

This version produced the most balanced and reliable results across both sample transcripts.  
It maintained structure, generated clearer summaries, and adapted well to different interview styles without requiring separate prompts for technical and management roles.