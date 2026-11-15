# SRC-003 - Website development environments: Charles and Alex

- Type: User-supplied question and Owner reply, preserved as provided
- Question author: User; addressed as Charles in Alex's reply
- Reply author: Alex, identified by the user as the Owner
- Original communication date(s): Unknown
- Added date: 2026-11-15
- Original subject: Unknown
- Descriptive subject: Website sandbox, shared DEV, repository and vendor catalog access
- Credentials: No credential values supplied; FTP access is discussed only

## Question (user)

Quick question, for the client-facing website, should I use a sandbox, or would you prefer that I work directly in the dev environment? I think working in dev could make testing and iteration faster, with changes merged into production after your review and approval. Or would you prefer the same setup as the admin website, where I work in a sandbox and you handle testing in production?
Also, would you be setting up the new repository and its sandbox environments? Thanks

## Answer (Alex)

Hi Charles,


Thanks for the great questions. I've been researching the best setup so you have what you need to test and iterate properly.


Like most teams, we keep production fully separate. Supabase gives access by organization rather than by project, and right now our DEV and PROD projects sit in the same organization, so I can't give access to one without the other. My plan is to move DEV into its own Supabase organization, which will become the shared development space for all of us, with production kept separate. It'll take me a little time to move it and clean it up.


I'm also going to seed DEV with much better test data, including our real vendor catalogs. The catalog is crucial to the website, so understanding how vendor files come in through the FTP puller is important, and later on you could help connect vendors through their APIs. I'll also share the vendor FTP logins separately so you can see how each vendor's files look.


For now, Phase 0 can happen entirely in your sandbox, and there's no rush on it. We don't have a repo for the website yet (I can create one quickly when we need it), so for now any work can start as documentation.


Once we're sharing DEV, the three of us (you, me and Chaze) will follow a simple workflow so we don't step on each other: unfinished work stays in your sandbox, changes go to DEV only when they're ready for review, and nothing sits on DEV that isn't headed for production soon.


I'd like to keep everything on Supabase as it is now and stay within the project framework, but if you have other ideas, I'm always happy to hear them.


Thanks, and have a great weekend!
Alex
