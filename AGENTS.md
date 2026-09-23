# Instructions for coding agents

Read this at the start of every session. Applies to any agent working in this
repository.

## Version control

- Work only on the current branch. Never commit to `main`.
- After each change that leaves the tests passing, make a commit.
- One commit per change. Do not batch unrelated edits.
- Write the commit message: what changed, then why, in the imperative.
- Ask me for the `Checked:` lines before committing. Do not invent them.
- Do not merge until I say the branch is reviewed and finished.
- When I do, merge into `main` with `--no-ff`, push, and delete the branch.
- Name branches after the issue number, e.g. `12-pubmed-harvester`.

## Research integrity

A citation or number that turns out to be wrong is not a bug. It is misconduct,
and it is the most common way this kind of project fails.

- Never add an entry to `paper/references.bib` for a paper that has not been
  opened. Not the abstract. Not a search result. The paper.
- Never report a number that has not been read in the source document.
- Every claim in `notes/` carries an access tag: `[VERIFIED]` (full text read),
  `[PARTIAL]` (say which sections were accessible), or `[UNVERIFIED]`.
- An `[UNVERIFIED]` claim may not move into the paper, a presentation, or a
  wiki page without being opened first.
- If a source is paywalled, say so plainly. A confident guess is not an answer.
- Do not run an analysis and report the result as a finding. I re-run anything
  that goes in the write-up.

## Scope

- `sandbox/` is illustration, never infrastructure. Nothing in the pipeline
  imports from it.
- Ask for the test before the fix. Confirm the test fails without the fix.
- If a change is too long to read in one sitting, the issue was too large.

## Security

- Never write a token, key, or password into a file in this repository.
- Never echo a secret into the terminal or into a prompt.
- Flag any dependency added, with a one-line reason.
- When parsing anything fetched from the network, assume it is hostile and say
  which parser setting makes it safe.
