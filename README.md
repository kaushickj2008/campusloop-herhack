# CampusLoop

[Live application](https://campusloop-herhack.vercel.app) · [Narrated demo](https://campusloop-herhack.vercel.app/demo.html)


An integrated HerHack Student Innovation prototype connecting campus accessibility, maintenance, reusable electronics, notice checklists, and private incident documentation.

## Run
Node.js 22+; no runtime dependencies or API keys.

```
npm run dev
# http://127.0.0.1:4187
npm test
npm run build
```

## Five connected workflows
- **RepairRoute:** classify a text report using explicit keyword rules, review evidence, create and resolve a ticket.
- **AccessPath:** open accessibility reports trigger an illustrative detour on a synthetic campus map. Resolution updates the route.
- **LabLoop:** recover inspected parts via manual inventory entry; match three curated recipes; reserve kits with inventory deductions.
- **Notice2Action:** paste text, extract dates and imperative sentences, review and confirm a source-preserving checklist. Links lead to inventory and routes.
- **ProofPocket:** session-only incident timeline, email/phone redaction, explicit text export. It does not publish to the campus board.

## Analysis model and scope
`public/engine.js` is a deterministic rules and recipe engine, NOT a trained machine-learning model. No LLM, image recognition, PDF ingestion or cloud inference is implemented. User input is escaped before rendering. This project targets Student Innovation, not claims of state-of-the-art AI.

Campus state uses browser localStorage. There is no shared backend, authentication or live college integration. Private notes use memory only, disappear on reload, and are excluded from localStorage. Redaction is incomplete by design: users must review names, places and other identifying details. The prototype is not a secure evidence vault, emergency service, or verified navigation system. Use synthetic data.

## Deploy on Vercel
Import this folder as the project root. Build: `npm run build`; output: `dist`; framework: Other. Or run `npx vercel deploy --prod` from this directory after authentication. `vercel.json` defines headers. No secrets are needed.

## Architecture
Vanilla JavaScript ES modules, semantic HTML, responsive CSS, pure analysis functions, Node built-in test runner. Zero third-party runtime packages. Six automated tests cover report routing, route changes, redaction, component availability and date extraction. Browser checks are documented separately.

## Originality and data
Built for this hackathon task. Demo records and campus geometry are synthetic. No real-world impact metrics or ML accuracy claims are made. Demo inventory contains illustrative parts only.

## Demo video
The watch page contains an edited walkthrough of actual app screenshots with synthesized narration and English captions. It is not a continuous screen recording. Synthetic data only. The MP4 is hosted on Vercel rather than stored in this repository.
