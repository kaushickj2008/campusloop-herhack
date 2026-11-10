# CampusLoop — Small actions. Shared impact.
Track: Student Innovation

## Problem
Campus issues are fragmented across maintenance messages, accessibility complaints, unused electronics, scattered notices and personal records. Students cannot easily connect a reported problem to the next useful action.

## Solution
CampusLoop connects five tools around a campus action workflow. A damaged electronics cart blocking a ramp becomes a reviewed maintenance ticket and an accessibility detour. Once resolved, a user can recover inspected components into an inventory and reserve a kit for a workshop. Workshop notices become source-preserving checklists. A separate, session-only incident notebook lets users organize their own notes without adding sensitive content to the campus feed.

## What we built
A working browser prototype with deterministic text analysis, stateful issue tracking, illustrative routing, component matching and kit reservations, notice extraction, and private timeline export. Campus state persists locally; private notes do not. No trained AI model, live campus integration, or secure evidence-storage capability is claimed.

## Technologies
JavaScript ES modules, HTML, CSS, Node.js built-in tests, Vercel static hosting.

## Validation
Six automated tests cover core rules, inventory availability, redaction, routing and dates. See README for reproducible setup. Real-user validation remains future work.

## Required before submission
- Public repository URL and runnable demo URL
- Recorded demo video URL
- Actual team member identities and roles
- Final organizer eligibility and deadline checks

## Demo script (approximately 2 minutes)
0:00 Show dashboard: one workspace connecting five campus needs.
0:15 Open RepairRoute; load sample; analyze; confirm three module links; create ticket.
0:35 Show AccessPath detour. Resolve open barriers in RepairRoute and show direct route.
0:55 Recover components; add inspected parts; reserve a matching LabLoop kit.
1:15 Load Notice2Action sample, extract, review dates, confirm checklist and complete an action.
1:35 Open ProofPocket, load synthetic note, add timeline, show redaction and explicit export.
1:55 State limitations: synthetic campus, local rules, browser-only state, no trained ML model.
