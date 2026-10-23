# Independent audit H2: PDFs, ChatGPT archive, dramatis personae, genealogy, correspondence, backmatter

Repo root: `/Users/rferguson/Downloads/goldstone-book-main/`. All paths below are relative to it.

## 0. How far I read

- **PDFs.** Every PDF in `sources/pdfs/` and `sources/books/The_Agricultural_Lock_out_of_1874.pdf` has a text layer, apart from the Savage "Private Nursing" PDF. I ran `pdftotext -layout` and read in full: JMS pp. 534-539, JMS pp. 603-607, Bucknill, Weatherly, Nicolson, Criminal Evidence Act, PublicLifeAssurance, the three WalthamstowMurder PDFs and Savage's Private Nursing (OCR'd). Where I did not read a PDF in full, I searched it by keyword and say so. That applies to the Medico-legal Journal (234 pp), VolumeInformation, Merkulova (297 pp), Conley (269 pp) and the Agricultural Lock-out book (419 pp).
- **Images.** I viewed `sources/images/marriage-certificates/William Gouldstone-Elizabeth Stock Marriage.jpg`, `correspondence/images/IMG_0049.PNG` and the two `backmatter/family_tree_*_print.png` files. I did not view IMG_0050.
- **Notes.** `notes/dramatis_personae.md` read fully (611 lines).
- **ChatGPT archive.** I read the reset file's main body and every [USER] turn over 25 characters in the feedback file (about 350). I read the AI's replies only where they bear on a claim. I read the witness-statement file's [USER] turns only (it is transcription-correction chat).
- **Genealogy.** Both CSVs in full. GEDCOMs searched by script for the key people and families; I did not read them end to end.
- **Correspondence and backmatter.** All text files read. IMG_0050 not viewed.

---

## 1. Errors (text wrong against a source)

**No chapter-text factual error found in this batch that rises to "high".** The items below are what I found, and most sit outside the chapters.

| # | Where | Finding | Severity |
|---|---|---|---|
| E1 | `chapters/CHAPTER_18.md` line 35 | An unresolved drafting placeholder is left in the clean chapter: `[WARSPITE: one or two sentences on what the ship was and where she lay in April 1901, once sourced (F (c)).]`. The Caird Library enquiry (`correspondence/Caird_Library_Warspite_enquiry_2026-10-10.md`) is still unanswered, as of 22 Oct. | medium (publication blocker) |
| E2 | `backmatter/PEOPLE_IN_THIS_STORY.md`, Thomas Gouldstone: "blacksmith, and later publican" | The author's own correction in `dramatis_personae.md` says the 1871 census image gives "Blacksmith & Beer Retailer (CORRECTED 21 October 2026 ... not 'Publican')". Chapter 3 uses "beer retailer", so the backmatter contradicts the chapter and the notes. | medium |
| E3 | Same file, Emily Gouldstone née Willett "(bap. 1830)" and the same "bap. 1830" in `family_tree_1_to_1883_print.png` | No baptism for Emily is cited anywhere I looked. The dramatis says her age "never resolves to a single consistent birth year" (1830, 1834, 1837, 1833, 1835 across censuses), and the 1830 figure is the 1851-census inference. The backmatter and tree present an unsourced baptism date. Chapter 1 correctly gives no date. | medium |
| E4 | Same tree: John Nathan Ansell "b. 1834", Jemima's marriage to John Ansell "m. 1833" | The dramatis gives m. 25 Dec 1833 and John Nathan b. 19 May 1834. That is under five months after the wedding. It is not an error, but readers will notice it. The tree should not suggest otherwise, and it is unremarked in Chapter 2 (not checked). | low |
| E5 | `ChatGPT-archive` claims contradicted by chapters/primary (see section 3) | For example "Dr Lorning" (press and notes: Twining), the 2 Helen Cottages address as the home, 10 Sept as trial date, "councillor", "S. Frost ... lived at 2 John Street". None of these made it into the chapters. | n/a, info |

I read **Chapter 18, lines 29 and 31** for ages. The chapter says "By March 1901 he was thirteen" and then "Albert was now his 'Son', fifteen". The dramatis says the 1901 census age 15 is "true 13". The chapter shows both figures without saying the census overstated his age. This is low severity, and a one-clause fix would do.

---

## 2. Unsupported or overstated

- **The inquiry doctors (Chapter 16, lines 11 and 17).** The chapter says "Dr Orange ... and Dr Clarke, from London", attributed to the Sunday Dispatch. That is accurately attributed. But three other sources I read name different people:
  - Nicolson's BMJ obituary of Orange (13 Jan 1917, p. 67 col. 2): "the Walthamstow murder, in 1883 where William Gouldstone took the lives of his five children. Here Drs. Orange and Gover found distinct evidence of insanity." Nicolson says Gover was "the Medical Inspector of Prisons".
  - BMJ, 29 Sept 1883, `WalthamstowMurder-1883 (2).pdf`: "the probability is that Dr. Orange, of Broadmoor, and Dr. Gower, Her Majesty's Inspector of Prisons".
  - Medico-legal Journal, Dec 1884, p. 341 (Clark Bell): "Dr. Orange and Dr. Clarke" for Gouldstone, and "Dr. Orange and Dr. Glover" for Cole.
  - The Sunday Dispatch, Guardian and Essex Weekly News (`transcribed/`) all say "Clarke" or "Clark". The Medico-legal Journal may simply copy that press name.
  - The author's notes treat the "Gover" in Nicolson as a conflation with Cole, and call it an inference. That is possible, but Nicolson was Orange's deputy at Broadmoor and wrote in 1917 about Orange's own cases. The chapter's "Dr Clarke" is correctly sourced to the press; it should say so in a note or hedge it ("the Dispatch named...") because a reader with Nicolson will see a conflict. Medium.
- **Elizabeth's Madams "marriage".** The Ancestry GEDCOM carries `MARR Abt. 1888` on the Madams/Stock family. The chapters correctly avoid saying they married. The ChatGPT archive (reset file) states flatly "1888: Elizabeth marries William Madams". That is unsupported. The chapter is safe. Keep the backmatter tree as drawn (a line, no "m.").
- **Dramatis claim that the 1879 wedding witnesses were William's parents.** The dramatis says Thomas and Emily Goldstone, "Attended William's 1879 wedding as witness alongside wife Emily". I looked at the certificate image. It shows "Thomas Goldstone his [x] mark" and "Emily Goldstone". The names match, but the certificate does not say "father" or "mother". William's sister Emily (b. 1854) and brother Thomas (b. 1859) are equally possible. This is an inference. The chapters do not use it (Chapter 4 names only the fathers' column), so it is safe in the manuscript. The ChatGPT archive says "James Goldstone (a smith)" was the witness, which is wrong against the image.
- **Chapter 18, line 43:** "In 1901 doctors were already arguing as much; it was proved in 1913." I found no source for this in the repo (searched chapters and transcribed for "1913"; the only hits are about other things). It is true in history (Noguchi and Moore, 1913), but it is unsupported in the apparatus. Low.
- **Merkulova (2022) and the brief's list of ships.** The brief asked me to find "every passage relevant to Albert, the Navy, boy sailors, ships Pioneer/Powerful/Drake/Shannon, or Russian service". There is none. Merkulova is a Leeds PhD on psychiatric education ("Pedagogy and the Building of British Psychiatry at the Age of Asylum, 1792-1914"). Keyword hits for Pioneer, Powerful, Navy and Russia are all generic. Russia appears only in the acknowledgements ("a senseless war my country of origin decided to wage"). The only case content is one paragraph at pp. 199-200 (see 3a).

---

## 3. What each source is, what it says, what the chapters use and miss

### 3a. Source-by-source

**JMS Jan 1884 pp. 534-539, "The Case of Gouldstone" (Savage), plus the unsigned "Case of Cole" (pp. 539ff).**
- Savage's retrospective in the *Journal of Mental Science* vol. 29 no. 128.
- Facts that bear on the case:
  - Mother insane at his birth; mother's sister insane.
  - Father's sister insane; two cousins, one of whom died in an asylum, "probably of general paralysis".
  - Occupation: "a fitter of grates which had been sent up from the foundry".
  - "He would, like Joseph of old, tell strange dreams ... heaven opened".
  - Double hernia; talk of "whether it would be painless to be crushed by the lift".
  - "rarely had animal food"; the twins' news; at the firm's "bean-feast" he "was at home, and appeared moody, and at times was in tears".
  - "contemplated suicide"; "He even considered whether he should use a revolver or not. He is said to have taken more drink than usual".
  - After the arrest "he seemed to be suffering from melancholia; so said the doctor, though for some reason his evidence was never given in Court" (the House of Detention doctor).
  - His own court account: "I could only say 'yes' when asked if the man knew he had killed ... his children".
  - Examination "from 20 minutes to half-an-hour".
  - Description of the brothers: "dull men".
- The chapters use the Lancet letter and the Times letters (Ch. 15), not this retrospective.
- Items **unused** and worth a line: the "fitter of grates" description, which differs from "whitesmith"; the brothers "intellectually weak and slow of perception"; "a murderer I once before examined" (comparison); his "melancholia ... out of relation to its causes". The "House of Detention medical officer called it melancholia" point is also in Savage's Times letter of 15 Sept, which the notes mention but the chapter does not use.
- Misses: none. Contradictions with chapters: none found.

**JMS Jan 1884 pp. 603-607, "Notes and News: William Gouldstone".**
- Reprints the Times report of 15 Sept 1883 and Savage's Times letter. Fully consistent with the chapters' trial narrative.
- Check: Poland in the Times "fitter"/"blacksmith": the Times calls him "blacksmith, 26" and the indictment lists the five children as "Charles, Herbert, and Frederick Gouldstone, and two male infants".
- Quote check: the chapters quote Savage's evidence in more detail than this reprint, which is abridged. The long quotations in Chapter 13 (e.g. "I have heard the evidence as to his being a steady workman...") are not in this PDF, so they must come from the full Times/Old Bailey texts. I did not re-verify them here.
- Nothing in the JMS reprint contradicts Chapter 13 or Chapter 14.

**Bucknill, "A Lecture on the Relation of Madness to Crime", BMJ 15 Mar 1884.**
- The first Gouldstone mention is in the section where Bucknill treats Day's charge as the "latest exposition" of the McNaghten law, quoting the summing-up: "if the prisoner, at the time he killed the children, knew the nature and quality of the act he was committing, and knew that he was doing wrong, then he was guilty of wilful murder." Bucknill uses it alongside Denman's sentence on Cole.
- Not used by the chapters. Bucknill's Gouldstone passage matches the JMS reprint of Day's charge word for word, so it is a confirming source for that quotation.
- Extra: the pages bound in the PDF include an unrelated cholera lecture. No other relevance.

**Weatherly et al., "Discussion on the law in relation to the criminal responsibility of the insane", BMJ 18 Aug 1894.**
- One passage, in Weatherly's paper: "Mr. Justice Day, in the case of Gouldstone, allowed the fellow-workmen of the prisoner to state their belief in his insanity; allowed evidence of the insanity not only of the prisoner himself, but of his mother and sister, of his aunt, and of a second cousin once removed."
- The point is useful: a ten-years-on lawyer-doctor view that Day did admit the lay opinion evidence. This sits against the common impression (and Savage's complaint) that Day was dismissive. The chapters do not use it. It is worth a sentence in Part Three if the author wants a balance point. The Times, though, shows Day also refused Savage the conclusion. Weatherly's list says "sister" where the Times says Emily gave evidence about the mother, so "sister" is his compression.
- Also contains Savage's own contribution (section VI, "The Question Ripe for Action"); no Gouldstone detail there.

**Nicolson, "William Orange, C.B." (BMJ obituary, 13 Jan 1917).**
- Confirms Orange's 1883-84 presidency of the Medico-Psychological Society, and the "Walthamstow murder" inquiry: "Drs. Orange and Gover found distinct evidence of insanity". Also the Christiana Edmunds case.
- Chapter 16 describes Orange from the Times and press. The obituary's biographical detail (the 1882 assault by a patient, per the dramatis) is not in the chapters.
- Conflict with "Dr Clarke": see section 2.

**Criminal Evidence Act 1898 (61 & 62 Vict. c. 36).**
- Section 1: the accused and spouse are competent witnesses for the defence. This is context for why William could not speak at his own trial and why Elizabeth's evidence could not be called by him in 1883. Used? I found no chapter citing it. Medico-legal Journal (Dec 1884, p. 352) cites the pre-Act rule that Cole's wife "could not give evidence in court". If the book wants to say that neither William nor Elizabeth could testify in 1883 (the Act is 15 years later), this is the source. Unused but apt.
- Also includes ch. 35 (Vexatious Actions (Scotland) Act), irrelevant.

**The Public and Life-Assurance, BMJ 20 Oct 1883, p. 784.**
- The page is a news-notes page. The only relevant item is a notice: "At the South London District Branch meeting, which will be held on Wednesday evening next [24 Oct 1883], in the Governors' Court Room, St. Thomas's Hospital, ... Dr. Savage will read a paper on 'The Gouldstone Murder, in its relation to the Plea of Insanity in Criminal Cases'".
- This is unused in the chapters and is a dated lead: Savage lectured on the case in October 1883. A report of that paper (BMJ late Oct/Nov 1883) would be primary and is not in the repo. The JMS Jan 1884 article cites "the October meeting of the Metropolitan Branch" for the resolution on early examination. Unverified lead.

**BMJ "The Walthamstow Murder", three copies (`WalthamstowMurder-1883.pdf`, `(1)`, `(2)`).**
1. 22 Sept 1883, pp. 583-585 (leading article, pp. 583-585 in the PDF with an unrelated Barron case also on 583).
   - Quotes the words: "Now I am a happy man." That is the leader's rendering of the same speech the chapters record as "I have killed the children, and I am happy now" (Times) and "I am not a wicked man. I am a happy man" (Ada's 10 Aug deposition, used in Ch. 6).
   - The leader gives "I thought it was too hot to have five kids in about three years and a half, and thought I would put a stop to it", and "Dr. Savage, the only specialist examined at the trial". It claims he would have been "justified in going further, and declaring that he did not know the nature and quality of his act".
   - It also says Savage "saw William Gouldstone on one occasion, for between a quarter and half an hour".
   - Chapter 15 quotes other press about Savage but I found no use of this leader. Chapter 12 or 15 could use "Now I am a happy man" because it gives the book's title phrase a contemporaneous medical source. Unused.
2. 29 Sept 1883, pp. 639-640: Home Secretary "intends to commute the sentence ... to penal servitude for life"; Orange and "Gower"; "the touching narrative of his wife, and the clear statement of the vicar". Used in Chapter 16 (accurately quoted: "the touching narrative of his wife, and the clear statement of the vicar of the parish in which he lived"). The Chapter 16 summary says "It had heard that Harcourt meant to commute the sentence to penal servitude for life" matches. The chapter omits the "Gower" speculation (see section 2).
3. 6 Oct 1883, pp. 682-683: "The decision of the Home Secretary in this case is both satisfactory and unsatisfactory ... It may be taken as demonstrated beyond reasonable doubt that Gouldstone was insane"; also compares the Matlock "youth Benn". Unused: the Benn comparison (a boy who murdered his father at Matlock and went to an asylum without trial) is a good contrast case. Also: "the execution of a lunatic is generally followed by a copious crop of lunatic homicides" (Dr Guy).
- Also the transcribed BMJ files in `transcribed/` exist for each, so the chapters cite those. No discrepancy seen between the PDFs and the quoted phrases in Chapter 16.

**BMJ 1883 Volume Information (index), `VolumeInformation-1883.pdf`.**
- Index entries: "Gouldstone, William, case of, 583, 639"; "Murder at Walthamstow, 583, 639, 682"; "Criminal lunatics, 445, 682, 829, 854, 880, 930"; "Insanity ... and unreason, 638"; "crime and insanity, 854".
- Leads: BMJ pp. 445 (Orange's presidential address, per the Nicolson obituary), 829, 854, 880, 930 (criminal lunatics) are not in the repo. p. 854 is "crime and insanity". Unverified leads: whether they discuss Gouldstone.
- The index does not contain an entry for the 22 Sept leader's page 584-585 separately; 583 covers it. Fine.

**Medico-legal Journal, vol. 2 no. 3, Dec 1884 (Clark Bell, "Madness and Crime", pp. 338ff).** I searched by keyword; I read pp. 341-352 and the Guiteau-comparison passage and the letters.
- Gives the trial in summary, reprints Savage's Times letter (15 Sept) and his Daily Telegraph letter of 17 Sept ("I have patients of the most insanely dangerous class here who have said the same things which Gouldstone said"), the foreman's card, Tallack's and Dr W. Wood's Times letters, and quotes JMS January 1884 extracts.
- It names the inquiry doctors as "Dr. Orange and Dr. Clarke" and says Orange and "Glover" examined Cole.
- It attributes the unsigned JMS article on "The Case of Cole, and the Legal Procedure" to **Dr. D. Hack Tuke, "editor"**: "Dr. D. Hack Tuke, in a forcible criticism of both these cases of Gouldstone and Cole". In the JMS PDF the piece is unsigned (it follows Savage's signed one). So the Tuke attribution rests on Bell. If the book names Tuke, it should say "attributed to Tuke". No chapter does.
- It reprints the "Times" Day charge and the sentence on Cole.
- Also p. 357: a US lawyer wrote in Oct 1884: "As to Gouldstone, the mental condition permits of more doubt."
- Check against Chapter 15: Chapter 15 says the Times letter from Savage was sent "that Saturday" (15 Sept). Bell's reprint is dated "[Sept.] 15, 1883". Consistent. The Daily Telegraph reply is dated "Sept. 17" in Bell; Chapter 15 says "One of the Jury answered it that day, writing to the Telegraph from Tottenham" and the transcription file is dated 18 Sept. Not contradictory.
- A **discrepancy between Bell and the JMS**: Bell prints the Times letter as ending "I am not one who is in the habit of defending criminals on the plea of insanity" with an extra paragraph about delusions ("I have no doubt he would have sooner or later developed delusions"). The JMS reprint of the Times letter (p. 607) is cut off after the third paragraph; the page ends mid-letter in the PDF. So the extra paragraphs come from Bell, not the JMS. Chapter 15 uses a letter; I did not check which version.

**Savage, "Private Nursing of Mental Patients" (Wellcome, 1911/12; OCR).** An address to the York Retreat nursing staff of 23 Nov 1911. No mention of Gouldstone, Albert, Navy or the case (searched the OCR for Gould, Goldst, Broadmoor, murder, children, Walthamstow, Albert). Irrelevant to the book except as a Savage biographical item; no chapter uses it.

**Conley, *Certain Other Countries* (Ohio State UP, 2007), ch. 6 pp. 182-183 and notes.**
- p. 182: "William Gouldstone felt his wife had been having children too quickly. When she gave birth to twins, he stopped speaking to her. A week later he killed their three young children and severely wounded the twins." Then quotes police, workmates, defence counsel, notes 82-85.
- Her notes: n. 82 Times 9 Aug 1883, 9f; n. 83 Times 6 Sept 1883, 5f; n. 84 Times 15 Sept 1883, 12a-c; n. 85 Times 15 Sept 1883, 9e-f (the leader, "We admit that he has acted after his kind...").
- Notes in the repo (`transcribed/Conley_2007_Certain_Other_Countries_Gouldstone_notes.txt`) say Rik found that Conley's n. 83 item "does not exist". The "stopped speaking to her" sentence has no cited source in her notes (n. 82 is the 9 Aug Times). The chapters do not use Conley. This is right: she is secondary and partly wrong.
- Leads unused: the Times leader of 15 Sept quote ("after his kind ... the type of man against whom our criminal code has been enacted") is the Times leader that Chapter 15 already draws on, so check whether Chapter 15 quotes it; I found "we couple our pity with abhorrence" instead. The "after his kind" sentence is a vivid line the chapter does not use (transcription exists as `The_Times_15_Sep_leader_transcription.txt`).

**Merkulova (2022).** pp. 199-200 only: Gouldstone listed with Lamson (1882) and Mapleton (1881) as 1880s trials with insanity pleas where "expert testimony was either conflicting or not sufficient and led to a verdict of sane and guilty". "In the case of Gouldstone medical testimony did not convince the jury and he was convicted of murder but received a reprieve for the duration of a new medical inquiry into his sanity. In the end he was proclaimed insane and confined to Broadmoor". Her n. 169 cites The Standard, 28 Sept 1883, p. 5 and 11 Oct 1883, p. 2. These two Standard issues are not in the repo: an unverified lead (a Standard report of the Oct 10 respite/inquiry). No Albert or Navy content.

**Agricultural Lock-out of 1874 (Clifford, 1875).** Used for Chapter 3. I checked three claims:
- "the men round Newmarket were locked out from the twenty-first of March": source p. 14 "The men were locked out on the 21st of March, three weeks after the strike". Correct.
- "between March and August the union sent £1,460 to its Halstead district alone": p. 21 table "Halstead, Essex, 1,460 0 0", "between the months of March and August 1874". Correct. (Newmarket/Exning got £14,984 10s 7d, so "alone" is fine but Halstead is a small fraction of the national relief. The sentence does not claim otherwise.)
- "On the third of August the union's executive voted to pay the locked-out men one week more and no longer, and to give no lasting relief to the old and infirm": p. 147 n. "On August 3, the executive committee ... decides to pay one week more to locked-out men not in employment ... do not feel justified ... to give permanent relief to such men, who, by reason of age or infirmity, are unable to migrate". Correct.
- "North Essex and Suffolk went first": the book's p. 14 says "Little attention had been aroused outside the district by the lock-out in North Essex and Suffolk. But soon after the lock-out around Newmarket became known...". It does not say these went first. The wording of Clifford is ambiguous. Low: an inference from an ambiguous sentence.
- The Halstead claim that "the lock-out reached Halstead" is not in Clifford; it is from the Halstead Times via notes. The grant table supports "Halstead had locked-out men". Fine.
- No mention of Great Sampford, Finchingfield or Wethersfield in Clifford (I searched). The chapter does not claim otherwise.

### 3b. Attribution problems

- **"Now I am a happy man" (BMJ 22 Sept, a medical leader) versus "I am happy now" (Times).** The book's title phrase and Chapter 6 line 73 ("I am not a wicked man. I am a happy man.") come from Ada's 10 Aug deposition per the dramatis. The BMJ's version is a fourth wording. Chapter 6 uses only one. That is defensible, but the dramatis itself flags this as an "unresolved tension". Chapter 6 states it as what he said at the door. A footnote that other sworn versions differ ("I have killed the children, I am a happy man now", 9 Aug) would be safer. Low.
- **Ch. 13 Savage quotes.** The JMS reprint of the Times is abridged ("from the examination alone he considered him rather weak in his mind, as was evidenced by slowness of appreciation of questions concerning the crime"). Chapter 13 gives verbatim first-person text; it must come from the Old Bailey/Times full text. Fine, but I did not check them against the Old Bailey transcript here.

---

## 4. Source problems

- **The `Medico-legal Journal` PDF's name for the inquiry doctors** (Clarke/Glover) and the BMJ's "Gower" are both speculation or press copying. Nicolson's "Gover" is the only source by a Broadmoor insider, and it is 34 years later. See section 2.
- **Ancestry GEDCOM versus primary documents** (checked by script):
  - William Gouldstone b. "1857" (birth certificate per notes: 10 Oct 1856; MyHeritage tree has 1856). Ancestry is wrong.
  - William's MyHeritage death "MAR 1935" (death 19 Jan 1935); trial "10 SEP 1883" (the Old Bailey session start; trial was 14 Sept).
  - Clarie Irene Setterington d. "7 Jan 1958" in Ancestry (that is the burial date; Chapter 21 says died 2 Jan, buried five days later). MyHeritage says "1958". The chapter is right.
  - Lily: Ancestry "1914", MyHeritage "Lilian Alma Irene", ChatGPT archive "14-12-14". The dramatis says 14 Dec 1913 (baptised 11 Jan 1914), and the backmatter tree says 1913. The archive's "14-12-14" cannot be right if the baptism was Jan 1914.
  - Steve's birthplace: Ancestry "Chatham", MyHeritage "Gillingham".
  - Eliza Jane: Ancestry "16 Sep 1891" (matches Chapter 18), MyHeritage "DEC 1891".
  - Elizabeth's birth: MyHeritage "18 FEB 1855 The Village, Weathersfield" matches the GRO per notes. Ancestry "1855". Death: Ancestry "1906 Blean" (district), MyHeritage "JUL 1906". Chapter says 29 June 1906.
  - Mabel Frances Gouldstone: Ancestry lists her as a child of Thomas and Emily (wrong per her birth certificate, which makes her the illegitimate daughter of the sister Emily); MyHeritage has a family with no father and Emily Willett Gouldstone as mother. The latter agrees with the dramatis.
  - Madams: Ancestry has a marriage "Abt. 1888"; none found. The Ancestry child "Lilian Florence Isobel /Rowden/" shows her married name.
  - Ancestry Elizabeth's father Thomas Stock died "22 November 1873" (ChatGPT also says 22 Nov); Chapter 3 says 22 December per the death certificate (dramatis). MyHeritage says 22 Dec 1873. Chapter correct.
- **Chromato CSVs** (the arithmetic): Both files cover chromosomes 1-9 only; rows for 10-22, X and Y are "-". For each file the header total equals the chr 1-9 sum:
  - Mary: 79.2+62.6+108.6+83.1+77.2+154.5+48.6+100.2+134.7 = 848.7 = header.
  - Steve: sum = 1,012.5 versus header 1,012.6 (0.1 rounding).
  - The "Match %" column is cM divided by an implied chromosome length (281.9, 264.1, 224.4 ... matching standard cM lengths), so each file is internally consistent.
  - The author's note in `notes/master-index.md` says the totals are "roughly half the expected figure ... so the tool undercounts consistently". The better explanation is truncation: chr 1-9 contain about 54% of autosomal cM (about 1,911 of about 3,500). 1,012.6 / 0.54 = about 1,880 (uncle expected about 1,741); 848.7 / 0.54 = about 1,570 (grandmother expected about 1,754). Both are plausible. So the totals are the sums of nine chromosomes, not a "tool undercount". The notes' conclusion (do not use these files) is right, but the stated reason is not.
  - Also the label "1C (avg 850)" is the tool's label for the cM bracket and is wrong for an uncle or grandmother. The CSVs do not name either kit's owner. They cannot show which relationship, which parent's side, or anything about Albert, Elizabeth or Madams. They contain no segment positions, so no triangulation is possible. They support nothing in the book and the chapters correctly do not use them.
- **The Bronwyn Joule match** (77.6 cM, 6 segments, largest 24.1 cM) is recorded only in the notes, not in the repo as an image or CSV. It is the only DNA evidence bearing on Elizabeth/Albert. The notes' claim "PROVEN" that Albert and Eliza Jane share a mother rests on a family-tree-based MyHeritage "Theory of Family Relativity", a 77.6 cM third-cousin-range match and the two birth certificates. It is a reasonable inference. Note that the match alone is equally consistent with half or full siblings (see notes' own discussion). In the chapters, check that DNA is described as "same mother", not "same father". I found no DNA claim in the chapters.

---

## 5. Unused material worth the author's attention

1. **BMJ 20 Oct 1883 p. 784**: notice that Savage would read "The Gouldstone Murder, in its relation to the Plea of Insanity in Criminal Cases" at the South London District Branch (St Thomas's, Wed 24 Oct 1883). Lead: find the BMJ report of the meeting (Oct 27 or Nov 3).
2. **BMJ 6 Oct 1883 leader** compares Gouldstone with the Matlock boy Benn, sent to an asylum without trial: "the rich murderer might go to Broadmoor, and the poor one to the gallows".
3. **BMJ 22 Sept leader** "Now I am a happy man" and its statement that Savage "would have been justified in going further" and its prediction that medical men "would have testified emphatically" if Stephen's definition were law.
4. **Weatherly 1894**: Day "allowed the fellow-workmen ... to state their belief".
5. **Medico-legal Journal p. 352 (Tuke, in JMS)**: "his wife could not give evidence in court" for Cole. This is the pre-1898 rule; the Criminal Evidence Act PDF is the later change. Directly relevant to Elizabeth.
6. **Savage's Telegraph letter, 17 Sept** ("I have patients ... who have said the same things which Gouldstone said") is in the repo as a transcription but the Bell reprint gives it a second witness.
7. **Inquest address**: the 1935 inquest slip gives William's address as "2 Helen Cottages, Queens Road, West Walthamstow" (`transcribed/Broadmoor_Inquest_COR_R1_7_3_1935_Transcription.txt`), not 8 Courtenay Place. The notes explain this in the correspondence draft: Helen Cottages belonged to "a related family" (a baptism of 1867 at 5 Helen Cottages, the 1881 census at 2 Helen Cottages, James Road, a death certificate of Dec 1882 at "Queens Road"). Chapter 21 quotes the inquest but never mentions the address. A footnote would head off a reader (or ChatGPT-derived "facts" in the wild) who sees "Helen Cottages" on William's papers.
8. **Dramatis details not in chapters** (selection): William 5 ft 4 in (IPN 18 Aug; Essex Weekly News 21 Sept); amateur musician (concertina, cornet, flute); Elizabeth's statement that he made her tea every morning "from their birth till their death"; Clarke's remark about rabbits; Hamilton's "chemist" sighting identifying Twining; Dr Sunderland's Times letter of 22 Sept; Laurence Peel's letter of 26 Sept; Miss Skinner's visit; Mr Sutton as the confinement doctor.
9. **1891 and 1901 census ages** of Elizabeth (34 for true 36; 43 for true 46; death certificate 47 for true 51), a documented pattern of under-statement after the murders. Chapter 18 does not mention it. The notes say "Do not put a motive in the prose". A neutral sentence of the pattern would be a fresh, documented fact.
10. **Brian Ronald Albert** (1932-1937) appears in Chapter 21, so already used.

---

## 6. ChatGPT archive (claims and leads, per brief)

### 6a. Linda Neaves's letter, full text
(From `ChatGPT-archive/chatgpt-book-proposal-feedback.txt`, [USER] turn at line ~10157, "Reply from Linda":)

> I'm not sure how helpful I can be, but I'll share what little I know.
>
> Firstly, I never met him. I think he died before I was born. My mum said very little about him.I grew up believing the story told to me by Lil, backed up by my mum, that he was born in France and sent over to England as a baby. His mother was a french maid and his father was a nobleman, so it was all hushed up. Years later Sue had a conversation with Rene about this and she said it was absolute rubbish. Rene was always the level headed one. So perhaps it was one of his stories, made up to hide his background. I suppose we'll never know.
> I think it was Steve who uncovered the German link, but again I have no idea if it's true.
> I don't know anything about a name change.
>
> My mum rarely spoke of him, so I don't know what sort of person he was. She often told me that at Christmas he would buy a huge Edam cheese, cut off the red wax and wear it on his head. I'd like to think that the group photo you sent me was at one of those gatherings.
> Years ago I took mum for a day at Chatham Dockyard, with my three boys. We were in the ropery, which is a  huge shed like building a quarter of a mile long, when she told the tour guide that her dad was the foreman there and rode a bicycle up and down the building to keep an eye on everyone. It was the first I'd heard of it.
>
> And that's the limit of my knowledge. There was always a mystery around him and I really don't know if mum actually believed the story she told me. She would always tell me I was part French. Now I don't have a clue.
>
> I hope David and Malcolm can fill in the blanks a bit more.
> Good luck .I love that you're doing this.
>
> Love Linda xx

Note: the AI's retelling (replies after this, e.g. line ~10334) says "Albert died in 1962; Linda was born in 1960, so she would have been just two". That is the AI's arithmetic; Linda herself says she thinks he died before she was born. Albert died 21 June 1962 (Ch. 21) and Linda was born 1960. So Linda's belief is mistaken, or she means "before I knew him". Small oral-history point.

Other family statements from the author's side (all in [USER] turns):
- Rik: "There was always talk of a dark family secret on my father's side ... Albert ... lying on official census (1911) and on his Royal Navy admission papers that he had been born in Germany ... 'Heckenning Houzellon'." "No stories were told of his mother or her ex-husband".
- Eileen Ferguson Smith (Rik's mother), WhatsApp 25 Jun 2025 (`correspondence/images/IMG_0049.PNG`, which I viewed): "Aunty Lil and Nanny Vere spoke about him being a Councillor for Chatham Borough Council ... It was Sue who told us excitedly she had discovered the Goldstone 'mystery'!" And, when asked what Sue said: "the original family name was Goldstein and they were Jewish escapees from Germany at some point and changed their name to Goldstone. Albert said it was to keep their past a secret. Linda might know more. I always thought Vera looked possibly Jewish!" And later: "Same year as Micks fathers died in the February. No wonder Vera was so badly hit."
- Uncle Steve (Rik's message pasted at feedback #1315): Dot "called Elizabeth's daughter Lillian 'auntie Lil' and thought she may have been her dad's half sister"; "Albert is recorded in the 1891 census as William Madams stepson and in 1901 as his son though there is no evidence to say he was adopted ... his father is named as William Goldstone on his marriage certificate"; "Sue's suggestion that he was German looks as though it may be true"; "The property the Madams lived in in Harbour Street Whitstable was used as a hairdressers. 'Auntie Lil' was married to a barber"; Dot knew her mum's father as "Old Jake".
- None of the French, Jewish-escapee, councillor or Edam/ropery stories is in the chapters (Part Six is unwritten). The councillor story is contradicted by primary sources: the notes' Chatham Observer reports show Albert lost both elections (Luton ward 1933 by 35; Christ Church ward 1934 by 327), and Chapter 21 says so. The ChatGPT archive treats "councillor" as a fact ("Albert Goldstone may have served as a councillor") and weaves it into its draft text. Wrong.
- The Prologue (lines 13-15) tells the reader that Albert named "William Goldstone, deceased, a commercial traveller" on his 1910 marriage (verified in `transcribed/Albert_Goldstone_Rennie_Setterington_marriage_1910_transcription.md`: col. 7 "William Goldstone, deceased.", col. 8 "Commercial Traveller"). Good.

### 6b. Albert's father, William Madams, 2 John Street / Hercules Buildings
- Archive: author's stance throughout: "William Goldstone was not the biological father of Albert, that not possible, his father is unknown" (#43). Confirmed by dates (William confined from 8 Aug 1883; Albert conceived about Sept 1886).
- **William Madams.** The author's turns: 1891 census Albert is "Stepson" (the author first typed "Arthur James Madams", an error corrected elsewhere to William James); 1901 "Albert Madams, son"; "William Madams died on 23 Nov 1901 ... admitted as a Lunacy Patient at Chatham Asylum on 4 Sep". Chapter 18 gives the Chartham admission on 4 Sept and death on 23 Nov. Archive claim "no marriage records for Elizabeth and William Madams that I can find" (#1246): consistent with Chapter 18 ("living as husband and wife"). ChatGPT's reset file claims "1888: Elizabeth marries William Madams (your family file)". Unsupported.
  - ChatGPT stated Madams had "two sons George (1885) and Arthur (1880)" (author turn #21 text: "William already had two sons George (1885) and Arthur (1880)"). I could not find this in the chapters, the dramatis or the correspondence. Unverified lead, probably an error of the author's early notes (Ancestry tree artefact), since the dramatis says Madams's Whitstable record starts 1890.
- **2 John Street, Hercules Buildings.** Author's census turns: 1881 "Henry Smith 27 (head), Elizabeth Smith 27, Henry J 2, Elizabeth A 3 months, Alice Whale (sister-in-law) 24, lodger James Lomes 26"; 1891 "Esther Hooper widow with son Charles 25, daughter Sarah 22, son Arthur 19" and, separately, "Charles Giggs 36, Mary Giggs 27". The dramatis and notes (CHAPTER_17_skeleton line 41) record these; the chapters do not use them (Ch. 17 gives only the address on the birth entry). ChatGPT's claim that "S. Frost ... lived at 2 John Street" is wrong: the certificate (`transcribed/Albert_Goldstone_birth_certificate_1887_transcription.txt` line 23) gives Frost's residence as "Workhouse Infirmary Brook Street Lambeth", and Chapter 17 line 19 says so. ChatGPT's claim "She did not remarry until 1888" is the same unsupported Madams marriage. Verified (author's own turns, consistent with notes); unverified in the sense that no census image is in the repo.
- **ChatGPT claim "Orbita 1930, Bermuda, rigger, 46 Edinburgh Road, age 44"** matches Chapter 21 line 13 as far as it goes (Orbita, Bermuda, rigger). Verified in part.
- **ChatGPT claim "Albert enlisted 1901 using Goldstone"; birthplace "Heckenning Houzellon"**: matches Prologue ("Heckenning Houzellon"). The AI's own embellishments ("Rochonberg, Germany"; "he wrote it twice, once in the Navy, once in the census"; "Hohenzollern" decoding) are not in the sources. The 1911 census reads "Hukening, Honyllon" (Ch. 20), the 1921 "spelling changed" (Prologue). The Hohenzollern idea is Rik's own query ("hohe Zollern??") and is speculation; Chapters rightly leave it out.
- **Date/location errors by the AI (not in chapters):** "2 Helen Cottages, Queens Road" as the family's home (inquest slip; see 5.7); trial "Sept 10" (session opening; chapters say 14 Sept); "Dr Lorning/Jeoning" (press: Twining); "locked in a sprat room" (author rejected); Savage's age claims; "Elizabeth ... physical injuries" (author rejected).
- **Naval details in the author's turn #1355**: "He stood 5'5" ... tattoos ... 'I love H' ... discharge 1919 for heart disease". The dramatis says the sheet reads "I love [K/F/T?] C" and the discharge is "Invalided / Org Heart Disease" (26 March 1919). Rik's "H" is struck. "From 1913 to 1918 seaman gunner" etc. are in the service record transcription (not rechecked here).
- **1881 and 1891 census as a lead for Elizabeth's pre-1887 whereabouts**: the author says Elizabeth does not appear in the 1881 John Street household (correct; she was at 88 Frampton Park Road). Nothing links her to John Street except the birth entry. Chapter 17 handles this as an address only.

### 6c. Leads in the archive not in the chapters, marked
| Lead | Where | Status |
|---|---|---|
| Bennett Gouldstone later life; son Charles Bennett married Mabel Frances (first cousins, 1908, Newington) | feedback #302-#340 | **Verified** against notes (dramatis) and the GEDCOM; not in chapters |
| Bennett's daughter Rose Elizabeth (b. 1891) "named for Elizabeth Stock"; descendant line to Marie Mabel, Linda Marie, Bennett C Housden | feedback #419-#656 | **Partly verified** (GEDCOM has Rose Elizabeth b. 9 Sep 1891, d. Jul 1972 Rochford; the "named for Elizabeth" is an interpretation; Bennett's marriage to Alice Cakebread is in both GEDCOMs) |
| Hugh C. Gouldstone (1868-1919), son Montague (1897-1954), grandson Barry (b. 1933, 1939 Register "weird edits") as living William-line relatives | #1273, #1287 | **Verified** in GEDCOM (Barry b. 15 May 1933); no relevance to book facts |
| "George Stock a long lost cousin" (Steve) | #1315 | **Unverified**; not in sources I read |
| Brother Bennett boarded with William (1881) | #286 | **Verified** (Ch. 4 line 31) |
| "Thomas Graves, gardener" as William's father | feedback early | **Contradicted** by Graves's baptism (father George) per dramatis; real Thomas Graves is in the 1874 Great Sampford directory but unrelated |
| Newspaper cutting on Albert's truanting, Whitstable Times 21 May 1898 | #928 | **Verified** (a Whitstable Times 25 Jun 1898 School Board transcription exists; Ch. 18 covers the School Board warnings; I did not check the 21 May date) |
| Savage biography; Merkulova thesis; HathiTrust docs 1-6 | #1160-#1186 | Merkulova **verified** (one paragraph); HathiTrust docs not in repo |
| Savage letter to the Lancet dated "Sept. 14th" | reset file | **Verified** (transcription header and Ch. 15) |

---

## 7. `notes/dramatis_personae.md`: differences from chapters, and facts only there

### 7a. Facts that differ from the chapters (or the backmatter)
1. **Inquiry doctor**: notes keep "Clarke" as working figure and flag Nicolson's "Gover" as unresolved (matches the chapter's attribution; see section 2).
2. **Thomas Gouldstone's trade**: dramatis (corrected 21 Oct) "Blacksmith & Beer Retailer" versus backmatter "later publican" (error E2).
3. **Emily Willett's birth**: dramatis "never resolves"; backmatter and tree "bap. 1830" (E3).
4. **Savage's date of examination**: dramatis "13 September 1883 — day before trial" (Thursday). Chapter 13 says "on the Thursday, the day before the trial". Consistent.
5. **Elizabeth in 1881**: dramatis reads the census "G. Stone" for every family member ("not an indexing error"). Chapter 4 line 31 gives "William G. Stone" and then Elizabeth as written. Consistent.
6. **Albert's age in 1901**: dramatis "15 (true 13)"; chapter shows "fifteen" without the correction (section 1).
7. **Duration of William's detention**: dramatis "51 years (corrected from '52')"; Prologue "more than fifty-one years"; Chapter 21 quotes the Standard's "52 years", clearly as a quotation. Consistent.
8. **Madams's paternity**: dramatis downgrades "almost certainly" to open; the chapters I read (18) say "stepson/son" and do not assert paternity. Consistent.
9. **Elizabeth's cause of death**: dramatis says do not assign direction of syphilis transmission; Chapter 18 line 43 says "she and Madams had died of the same disease", with no direction. Consistent.
10. **Dr Twining**: dramatis says the Honey statement's "Lorning" is a transcription error. Chapter 7 uses Twining.

### 7b. Facts present only in the dramatis (not in chapters, as far as I looked)
- William: 5 ft 4 in, fair, moustache, curly hair; amateur musician; Salvation Army hymns at work; the lift-rope incident with Skelton ("it will only kill me out of the way"); the 1856 birth; his own letter to Elizabeth of 15 Sept 1883 (full text, dramatis p. 1).
- Elizabeth: the GRO birth (18 Feb 1855, "The Village"); the eight Ansell half-siblings and their deaths (partly in Chapter 2); the age pattern across five documents; "No marriage found in FreeBMD 1887-1892".
- Parish and trade details for Thomas Gouldstone (1841-1891 census run, Cock Inn, White House Moor End, Finchingfield 1881); the Willett siblings; "Mrs Andrews" identified as Ann Willett (Chapter 1 line 27 uses Ann).
- Mr Sutton (confinement doctor), Mr Batchelor, Mr Atkinson, Mr Gepp, Joseph Blythe's Times account, Laurence Peel, W. Wood, Tallack, Sunderland's Times letter of 22 Sept, Miss Skinner, Mrs Pelly and St Agatha's Refuge.
- Brian Ronald Albert (used in Ch. 21), Eliza Jane Madams married Percy Coombs, emigrated to NZ 29 June 1927 on SS Ionic with seven children, died 1 Apr 1976 (Rangimarie Home, New Plymouth). Her DNA match Bronwyn Joule.
- Albert: 1933 and 1934 election results (used in Ch. 21), Working Men's Club secretaryship (used), Clarie's father George Setterington as a colour sergeant, 31st (East Surrey) Regiment (used in Ch. 19 line 33).

### 7c. Issues inside the dramatis
- Marriage witnesses described as the parents (inference, section 2).
- The dramatis keeps a list of "TO VERIFY ... not for prose" items for 2 John Street (renaming to Newnham Terrace 1893, Park Plaza Hotel site, "not a workhouse inmate", half-mile distance). The chapters correctly omit these.
- The Standard's "William Goldstone ... 80 years of age" versus coroner 78: chapter 21 quotes both correctly in context.

---

## 8. Genealogy files, short form

- **Chromato CSVs**: see section 4. Nothing in them can be used. They show no named kits, no segment coordinates (only per-chromosome totals), and chr 10-22/X are blank in both. The "1C (avg 850)" labels do not fit the stated relationships (uncle, grandmother). The header totals are exactly the chr 1-9 sums, so the author's "undercount" explanation should read "truncated to chromosomes 1-9".
- **Ancestry GEDCOM ("Ferguson Scratch Tree", exported 22 Jun 2026; 533 persons)** and **MyHeritage GEDCOM (08 Sep 2026; 1,078 persons)**. Key people:
  - Albert Jennet Goldstone: b. 19 Jun 1887 Lambeth (Ancestry also stores two German birthplaces "Heckenning Houzellon" and "Hukening Honyllon, Germany"); d. Jun 1962 Chatham. Both trees show Elizabeth Stock as sole parent (family with no husband).
  - Elizabeth Stock: see section 4.
  - William Gouldstone: Ancestry b. 1857 (wrong), MyHeritage b. 1856, both d. Jan/Mar 1935.
  - William James Madams: b. 1860 (Ancestry), "1 May 1860" (MyHeritage; notes say unsourced), d. 23 Nov 1901.
  - Clarie Irene Setterington: b. 7 Jun 1889 Kingston Barracks (both); Ancestry parents George William Setterington and Priscilla Eliza Thomas (Ancestry); MyHeritage lists a "Charles Frederick" and an "Albert" among the siblings that Ancestry lacks. Not used in chapters.
  - William Savage: no entry (not a family member).
  - Both trees include Charles Thomas, Herbert Ernest, Frederick William (Ancestry shows "Goldstone", as on his GRO entry) and two unnamed twins, all d. 8 Aug 1883.
  - The trees agree with the primary transcriptions except where I list in section 4.

---

## 9. Correspondence and backmatter: status

| File | Status | Bears on book facts |
|---|---|---|
| `Caird_Library_Warspite_enquiry_2026-10-10.md` | Sent 10 Oct, chaser 22 Oct, RMG acknowledged 22 Oct (answer expected about 5 Nov) | Chapter 18 has the unfilled `[WARSPITE ...]` placeholder (E1). Rik's letter correctly says Albert "was 13 in April 1901, though the court reports give his age as 14". |
| `Kent_Archives_Madams_Chartham_enquiry_2026-10-10.md` | Sent 10 Oct; reply 14 Oct from Dr Helen Wicker. References: case books MH/T3/Mc44 or Mc45, Admission Register MH/T3/Ka7, Burial Register MH/T3/Kz2. No reception order survives. Open (over 100 years); £12.50 per 15 min. | Madams's case notes could give next of kin (was Elizabeth named, and as what?) and a photograph. Not commissioned yet. Chapter 18 uses only the admission date and death certificate. |
| `Forster_RBA_letters_2025.md` | Letters 1-4; Letter 4 (29 Sept 2026): coroner's middle name "Oswald" and "six years" confirmed (both are in Chapter 21: "poor bodily health for the last six years" and the name as Milne); case book D/H14/D2/1/1/4 closed until 2053; patient file closed until Jan 2036; archive offers to forward a request if Rik proves descent from the wife. | Confirms Chapter 21's inquest quotation. Notes on letter 3: Rik wrote "He left no descendants". |
| `DRAFT_letter_to_Forster_casebook.md` | Superseded draft | none |
| `DRAFT_archives_and_historical_society_enquiries.md` | **Not recorded as sent**: Waltham Forest Archives and Walthamstow Historical Society. Draft includes a Helen Cottages explanation (5 Helen Cottages 1867; 2 Helen Cottages, James Road 1881; Queens Road Dec 1882) and a juror list (William Smith foreman, David Casey, Joseph Blythe, ... William Weston). It also records the claim that Courtenay Place was on Frampton land as unverified. | Courtenay Place not in the 1881 census; no. 8 appears in 1891; gone by 1911 (Rik's own search). The Chapter 5 line "a new development called Courtenay Place" fits. The Frampton claim does not appear in the chapters. |
| `correspondence/images/IMG_0049.PNG`, `IMG_0050.PNG` | WhatsApp screenshots with Eileen Ferguson Smith (25 Jun 2025). 0049 viewed; 0050 not viewed. | Source of the councillor and Goldstein stories (section 6a). |
| `backmatter/PEOPLE_IN_THIS_STORY.md` | Draft list, 2.4 KB | Errors E2, E3 above. Also lists "Martha Graves ... in whose household Elizabeth and William lived for the first years of their marriage". Martha Graves is the 1881 wife; the notes say Graves's wife in 1861 was Harriet. Chapter 4 line 31 gives Martha, 40, in 1881. In 1879 (marriage) which wife? Unknown. The 1871 census gives Martha, so she was probably the wife in 1879 as well. Low. |
| `backmatter/family_tree_1_to_1883_print.png`, `_2_elizabeths_later_family_print.png`, SVG, PDF, `make_family_trees*.py` | Two trees; I viewed the print PNGs. Tree 2 shows Lily b. 1913, Clarie Irene 1918, Vera 1921, Doris 1928, Brian Ronald Albert 1932; Steve 1944; Robert George 1968 | Tree 1: Emily Willett "bap. 1830" (E3); John Nathan b. 1834 / Jemima m. 1833 (E4). Tree 2 matches the chapters' dates (Lily 1913 per the dramatis, baptised Jan 1914). It draws a solid line from Elizabeth to Madams without "m."; good. |

---

## 10. What I could not check

- Savage's evidence quotations in Chapter 13 against the full Times/Old Bailey texts (the JMS reprint is abridged); the Savage Lancet quotations in Chapter 15 beyond confirming the transcription header (the transcription says it was checked against the image by the author).
- BMJ pages 445, 829, 854, 880, 930 (indexed under "Criminal lunatics"/"crime and insanity"), The Standard 28 Sept and 11 Oct 1883: not in the repo.
- Whether the Gouldstone passages in the Medico-legal Journal beyond pp. 341-352 and 356-357 add anything (I searched by keyword; line 3384 is the Daniels letter). I did not read the other 230 pages.
- The Agricultural Lock-out book beyond the cited pages and keyword searches.
- Conley beyond pp. 182-183 and notes.
- The whole of the ChatGPT feedback file (674 KB) and witness-statement file (423 KB); I read the user turns and sampled AI replies.
- IMG_0050.PNG; the SVG/PDF versions of the family trees; the make_family_trees scripts.
- GEDCOMs read by targeted search only.
- Whether Dr Gover or Dr Clarke is correct: no primary document (Home Office file, HO 144) is in the repo.
