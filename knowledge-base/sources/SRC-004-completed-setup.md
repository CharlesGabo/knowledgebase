# SRC-004 - Completed operations setup and knowledge-base instructions

- Author: User (Charles); original checklist author unknown
- Original checklist date: Unknown; relative weekend/Monday references are not dated
- User report date: Unknown
- Added: 2026-11-15
- Subject: Existing operations sandbox, completed onboarding, Notion questions and current scope intake
- Type: User report with supplied checked checklist; completion is self-reported, not independently tested
- Redactions: None required; credential references contain no credential values

## Supplied wording

i already have a sandbox for the operations side system i had already done these checklist # Weekend setup (before Monday)

Welcome! This is your setup list for the weekend, so you're ready to start on Monday. Alex is around this weekend if anything gets stuck.

**Log your time.** Setup counts as work. Add an entry to the Work Log for each session: date, hours, and "Weekend setup" as the summary.

## 1. Your work email (do this first)

- [x]  Sign in at gmail.com with your work email and the temporary password Alex sent you. Google will ask you to choose your own password.
- [x]  Turn on 2-Step Verification (Google Account → Security).
- [x]  Use this email for every TMA account below.

## 2. Accept your invites (they're in your work inbox)

- [x]  **Claude:** accept the Team invite and sign in with your work email.
- [x]  **Notion:** accept the invite. Check that you can see the **tmalg.com website** teamspace and this **Charles — Private** page.

## 3. GitHub (so Alex can add you)

- [x]  Create an account at github.com with your **work email** (or add your work email to an existing account).
- [x]  Turn on two-factor authentication (Settings ? Password and authentication).
- [x]  **Send Alex your GitHub username.** She'll add you to the repository with Write access, and you'll get an email invite to accept.

## 4. Install your tools

- [x]  VS Code, Git, Node.js 20 or newer, Python 3.11+, and Docker Desktop.
- [x]  On Windows, run this once before cloning: `git config --global core.autocrlf input` (it's required; see the repo's local setup guide).
- [x]  The **Claude Code** extension in VS Code, signed in with your work email.
- [x]  Codex too, if you'd like to use it (optional).
- [x]  GitHub's command-line tool (`gh`), then run `gh auth login`. Claude uses it to read your issues and post updates.

## 5. Get the code running (after Alex adds you on GitHub)

- [x]  Accept the GitHub invite email.
- [x]  Clone `tmalgops/tma-operations-platform-v2` and open the folder in VS Code.
- [x]  Follow `docs/onboarding/02-local-setup.md`. You'll build your own local sandbox on your computer with test data. You don't need any database account or password.
- [x]  Get the app running with `npm run dev` and log in with a test persona.

## 6. Read (in this order)

- [x]  **Start Here**, then Onboarding pages 1–7 in the website teamspace.
- [x]  **Project Framework** and the **Roadmap**.
- [x]  In the repo: `AGENTS.md`, `docs/business-context.md`, and `docs/onboarding/08-async-workflow.md`.

## 7. Turn on hour tracking (you're paid hourly)

- [x]  Hour tracking in the shift commands is off by default. Turn it on once, in Git Bash: `echo "track_hours=yes" > ~/.tma-contributor` (or PowerShell: `Set-Content -Path "$HOME\.tma-contributor" -Value "track_hours=yes"`). Details are in `docs/onboarding/08-async-workflow.md`.

## 8. Try the routine

- [x]  In Claude Code, inside the repo, type `/start-shift` to see what it does.
- [x]  At the end of a session, type `/end-shift`. It suggests your hours and drafts your Work Log entry.

## Stuck?

Add it to Questions for Alex with Area set to **Access / tools**, or message Alex directly this weekend.
make sure to note there that i have that question thingy on notion for my questions so when i have a questin for alex that is not in here you shold recommend me to use that. I will also put here the project scope so you have context on what i should revise tomorrow on how i would integrate this operation system to the new client facing website i will make (this is phase 0). This file contains all the phases of the current project scope version we have so this is important for us to always be on track. TMALG-Website-Counter-Proposal.docx its here, you can convert this to md file.
