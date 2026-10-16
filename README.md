# The Goldstone book: working repository

Research and manuscript for a work of narrative non-fiction by Richard (Rik) Ferguson about the Walthamstow murders of
8 August 1883, the life of Elizabeth Gouldstone (née Stock) afterwards, and the author's descent from her.

This file says where things are and which file has the final word on what. It holds no facts about the case and no
chapter status, so that it never needs correcting when they change.

## Which file governs what

| For | The authority is | Notes |
|---|---|---|
| Chapter status, and what comes next | `notes/live_lists.md`, section 0 | The only record. Nowhere else. |
| Open questions, decisions waiting, pending actions, sources to obtain | `notes/live_lists.md`, sections 1 to 4 | Settled items are struck through and kept, not deleted. |
| What must not be used, and press usable only as press | `notes/live_lists.md`, sections 5 and 6 | Section 6 also lists shared copy (several papers, one witness). |
| Facts | `notes/MASTER_NOTES.md`, `notes/confirmed_facts_timeline_contradictions.md`, `notes/dramatis_personae.md` | The single dates table is in the timeline file, Part Two. Contradictions are numbered there. |
| A person | Their entry in `notes/dramatis_personae.md` | Read it before logging a contradiction about them. |
| A chapter's plan and every decision taken on it | `notes/CHAPTER_NN_skeleton.md` (Part Four: also `notes/PART_FOUR_plan.md`) | Some skeletons cover two chapters; section 0 says which. Rulings at the foot govern where they differ from the body. |
| Elizabeth | `notes/elizabeth_thread_presence_as_absence.md` | Also the sourced list of every word she is recorded as saying. |
| Law and medicine in 1883 | `notes/part_three_context_law_and_medicine.md` | Items marked TO VERIFY are not to be used until verified. |
| What a transcription has been checked against | The header of that transcription | Check once, record it there, and nowhere else. |
| Where a source is | `notes/master-index.md` | Entries are pointers; the transcription header is the authority on the text. |
| Acknowledgements | `notes/acknowledgements_running_list.md` | Private individuals are working entries until asked. |

Superseded session logs and retired sections are in `notes/archive/`. Search them when a note cites one; never treat
them as current.

## Outside this repository

These govern the work but are kept in the claude.ai project, not here:
- the project instructions (the working rules, the writing rules and the shape of the book);
- `rik-voice-writing-gate.md` and `AI_Writing_Tells_Gate.md`, which every draft is checked against;
- `My book.txt`, the voice reference.

Where the project instructions and the notes disagree on a fact or a status, the notes are right.

## The manuscript

`chapters/`, in reading order: `PROLOGUE.md`, then `CHAPTER_1.md` to `CHAPTER_21.md` (later chapters are added as they
are approved; drafts are held locally until then).

| Part | Chapters |
|---|---|
| Prologue | `PROLOGUE.md` |
| (after the Prologue) | the first family tree, "Two families, to 1883" |
| One, Before | 1 to 6 |
| Two, The Evening | 7 to 9 |
| Three, The Reckoning | 10 to 17 |
| Four, Elizabeth | 18 and 19 (the second family tree stands before its title page, after Chapter 17) |
| Five, Albert | 20 and 21 (22 to come) |
| Six, The Researcher; Coda | not begun |

The two family trees stand in the text: the first, "Two families, to 1883", after the Prologue, before Part One; the second, "From Elizabeth to the author", after Chapter 17, before Part Four. Back matter, in this order: "People in This Story", notes, sources, acknowledgements.
`backmatter/` holds the list and both family trees. The trees have two generators, `make_family_trees.py` (SVG
previews) and `make_family_trees_print.py` (print PDFs, B-format); any change goes into both, run from the repository
root, and every export is regenerated.

## The sources

| Folder | Holds |
|---|---|
| `transcribed/` | Transcriptions of press, certificates, censuses, registers and letters, each with its own header. The active path (not `transcriptions/`). |
| `sources/trial-docs/` | The 1883 depositions and statements (CRIM 1/19/2), with page images, and the Old Bailey text. The committal statement sits under `Coroner Depositions/Commital/` by an old misfiling, left in place on purpose (see the index). |
| `sources/images/` | Page images: press (`Media-coverage/`), certificates, censuses, Broadmoor documents, maps, photographs. |
| `sources/pdfs/` | Journals and books as PDFs. |
| `sources/genealogy/` | The Ancestry and MyHeritage family trees (GEDCOM), and two DNA comparison exports. A tree is weaker than a certificate; the comparison exports undercount (see the index). |
| `correspondence/` | Letters to and from archives, as sent, with what each reply changed. |
| `ChatGPT-archive/` | Earlier AI-assisted sessions. Never a source; every quotation is checked against the repository. |

## How changes reach the repository

Rik uploads every file himself. A session clones fresh (`git clone --depth 1`), works and commits locally, checks that
`origin/main` has not moved (and reconciles if it has), and hands over the changed files with the folder each belongs
in. Unfinished chapters are not sent until approved.
