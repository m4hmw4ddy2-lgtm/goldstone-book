# Independent audit: common brief (read this first)

Book: *A Happy Man: The Walthamstow Murders and a Century of Silence*, by Rik Ferguson. Narrative non-fiction. William Gouldstone drowned his five children at 8 Courtenay Place, Walthamstow, on 8 August 1883 (tried 14 September 1883; respited; Broadmoor 15 October 1883; died there January 1935). His wife Elizabeth (née Stock) later had a son, Albert Jennet Goldstone (b. 19 June 1887, Lambeth Workhouse Infirmary), the author's great-grandfather. Parts: Prologue; One (ch 1–5) Before; Two (6–8) The Evening; Three (9–16) The Reckoning; Four (17–18) Elizabeth; Five (19–21) Albert; Six unwritten.

## What "independent" means here
The author has asked for an independent audit, not one run to his own rules. So:
- Do NOT apply the author's "DO NOT USE", "RULED", "NO GIVEAWAYS" or press-only conventions, and do not treat anything in `notes/` or `ChatGPT-archive/` as evidence. Those are the author's (or an AI's) claims, not sources. Do not read them unless your own batch brief names them, and then only as claims to test.
- Judge the manuscript as a careful editor and fact-checker would: is each statement of fact supported by a primary or clearly identified source in the repo? Is a quotation word-for-word and correctly attributed (right witness, right paper, right date)? Is an inference presented as fact? Is arithmetic right? Does the book contradict itself? Are there overclaims, loaded words, or narrator statements with no source?
- Where the author made a choice that is defensible, say so and move on. Where a choice is unsupported by any source, say so, whatever the notes say.
- Grade evidence yourself: primary document image > transcription of it > contemporary press (shared copy across papers counts as one witness) > later secondary > the author's notes > AI archive.

## Where things are
Local clone (host path for Read/Grep/Glob): `/Users/rferguson/Downloads/goldstone-book-main/`. In bash the same folder is `/sessions/elegant-adoring-allen/mnt/goldstone-book-main/`. Use Read/Grep/Glob with the host path, bash with the VM path.
- `chapters/PROLOGUE.md`, `CHAPTER_1.md` … `CHAPTER_21.md`: the manuscript (clean markdown). `chapters/archive/` is superseded; ignore unless asked.
- `transcribed/`: about 188 transcriptions of newspapers, certificates, censuses, depositions, ship clips. Each has a header describing the image it came from.
- `sources/images/` (426 images), `sources/trial-docs/` (44 scans of CRIM 1/19/2 pages 0001–0044 plus transcriptions, and `Trial Account Old Bailey website.txt`), `sources/pdfs/`, `sources/books/`, `sources/genealogy/`.
- You CAN view images with the Read tool (jpg/png). Use this: where a chapter relies on a specific word, number, date or name from a handwritten or printed document, look at the image and compare it with both the transcription and the chapter. Transcriptions may contain errors; the image governs. Log every case where image, transcription and chapter disagree.
- Manuscript quotation check already done by script: of 437 quoted strings (three words or more) in the chapters, 415 appear verbatim (after normalising punctuation and case) somewhere in the transcriptions or trial-doc texts. That does NOT show they are attributed to the right witness or paper, or that they are in the right context. List of the 22 non-matching strings: `outputs/work/ind/unmatched/` (host path: `/Users/rferguson/Library/Application Support/Claude/local-agent-mode-sessions/bd2f85af-6bfc-4ab8-8a4e-6b1acaf6fd21/9d7fb66a-ca31-478c-975c-30fa642a5cac/84ecf240/outputs/work/ind/unmatched/`). Weekday-and-date pairs (31) were all verified correct by script.
- An earlier, rules-bound audit exists in `outputs/A_Happy_Man_audit_appendices/` (same outputs folder). You may read it for pointers only if told to in your batch brief; do not adopt its conclusions without checking against the sources yourself.

## What to deliver
Write your findings to the file named in your batch brief (Write tool, host path under `outputs/work/ind/`, i.e. `/Users/rferguson/Library/Application Support/Claude/local-agent-mode-sessions/bd2f85af-6bfc-4ab8-8a4e-6b1acaf6fd21/9d7fb66a-ca31-478c-975c-30fa642a5cac/84ecf240/outputs/work/ind/<name>`). Structure:
1. **Errors** (the text is wrong against the source): chapter, the manuscript sentence quoted, the source and exact words (file, and image name if you looked), why it is wrong, severity (high = changes a fact the reader will rely on; medium; low).
2. **Unsupported or overstated** (no source found, or the source says less/other): same format. Say exactly what you searched.
3. **Attribution problems** (right words, wrong witness/paper/date; or several papers presented as separate witnesses when they share one text).
4. **Source problems** (a transcription disagrees with its image; a header note is wrong).
5. **Unused material worth the author's attention**: concrete facts with the source location.
6. **What you could not check**, and why.
Be exact and brief. Quote short strings. Never invent a source or a page. If you did not look at an image, do not say you did. Your final reply to the caller must be under 250 words: what you covered, counts by severity, the five findings that matter most, and the output file path.
