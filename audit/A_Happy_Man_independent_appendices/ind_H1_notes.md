# ind_H1_notes: audit of MASTER_NOTES.md and confirmed_facts_timeline_contradictions.md against chapters and sources

Read in full, in chunks: `notes/MASTER_NOTES.md` (1325 lines) and `notes/confirmed_facts_timeline_contradictions.md` (3496 lines). All 22 chapter files were also read in full. The notes were treated as claims to test. Evidence grade used: image > transcription > press (shared copy = one witness) > notes.

Images I actually viewed: the 1879 marriage certificate; Elizabeth Madams's 1906 death certificate; both pages of the 1881 census (RG 11/301 pp. 47-48). Everything else below was checked against transcriptions only (by grep or reading), not images. Transcriptions that I checked were: Old Bailey text, 1861 and 1871 censuses, Chelmsford Chronicle 1857 and 1861, Lambeth Workhouse register 1887, Navy List 1903, Albert's service record, Setterington census, Chatham cemetery listing, Broadmoor inquest 1935, Whitstable censuses, Evening Standard 21 Jan 1935.

Severity counts (this batch): Errors 6 (high 2, medium 2, low 2). Unsupported/overstated 33 (high 6, medium 15, low 12). Attribution 9 (high 3, medium 4, low 2). Source/notes problems 14. Contradictions: 119 numbered; 25 touched by chapters (see table).

---

## 1. Errors (text wrong against a source)

| # | Where | Text | Source and why wrong | Sev |
|---|---|---|---|---|
| E1 | Ch16 l.5 | "Harcourt … took a week. His letter reached the Sheriff … on Tuesday the twenty-fifth of September" | The sentence follows the trial (Friday 14 Sept). 14 to 25 Sept is 11 days. (The notes give no "week" either; the arithmetic is the chapter's.) | medium |
| E2 | Ch14 l.5 vs l.29 | "apart from his plea, no report has him say a word" | Same chapter l.29 quotes the Essex Weekly News's "I am not guilty" and the Times's "replied in the negative" when asked if he had anything to say. Chapter contradicts itself. (Morning Post 15 Sept also has "I am not guilty", per notes.) | high |
| E3 | Ch18 | "[WARSPITE: one or two sentences on what the ship was … once sourced (F (c)).]" | Unfinished placeholder left in the manuscript text. | high |
| E4 | Ch10 | twin coffin plates "gave their names and ages" (Guardian) vs Ch7 twins "never … given a name" | Chapter contradicts itself. Notes record a burial-register lead "2 males unnamed" (grave 1370A) not held in repo. One of the two statements must go or be qualified. | medium |
| E5 | Ch9 | He "had supplied her immediate wants" attached to the 9 August letter | Notes (timeline) place this phrase in the 10 August letter. Not re-verified in the press transcription; check. | low |
| E6 | Ch19 | "eighteenth birthday … 19 June 1904" | Albert's true birth 19 June 1887 (Lambeth register, image-based transcription): he was 17. The 1886 year is the naval fiction. Chapter does not tell the reader at that point. | low |

## 2. Unsupported or overstated (searched: `transcribed/`, `sources/trial-docs/`, `notes/`)

High:
- U1 Ch10: Martha Gouldstone is stated flatly as Robert's widow, and "Robert died at Walthamstow the December before". The Guardian says only "Mrs Gouldstone, the prisoner's aunt". The notes' chain is census + GRO + baptism with unresolved conflicts (age 63 on death cert vs baptism 1824; two Roberts baptised at Great Sampford in 1824; the Union Road / Helen Cottages households). Needs a "probably" or a note.
- U2 Ch6: "He held them under … for as long as it took"; "Drowning a conscious child is not quick…"; "which means they were swallowing"; "Frederick … went quickly". All are inference (stomach contents, William's "the other little one I soon settled"); the medical statements have no source in the repo.
- U3 Ch7: "He was Dr Twining". Ada says "a Gentleman, a Chemist"; the identification is the notes' reasoning from another witness, not a document. Also "Neither of them had survived long enough even to be given a name" states a reason no document gives.
- U4 Ch14: Married Women's Property Act 1882 exception and "fifteen years" are external legal claims with no repo source. The Act "passed towards the end of the previous month" is marked TO VERIFY in the notes.
- U5 Ch18: "In 1901 doctors were already arguing as much; it was proved in 1913". No source in the repo.
- U6 Ch3/Ch5: the "tuppence" workmen's-train fare, and "streets that had not even existed when William and Elizabeth married". No hit in transcribed, trial-docs or notes. The street claim also sits badly with notes placing Robert Gouldstone at Union Road (1871) and Helen Cottages (1867/1881), Walthamstow.

Medium:
- U7 Ch3: "nine people living in sheds" (Great Sampford 1871) is from Adrian Gray's web page via the notes: secondary, unidentified in text.
- U8 Ch3: lock-out figures (£1,460 to Halstead, 21 March, 3 August vote). Probably from `sources/books/The_Agricultural_Lock_out_of_1874.pdf` (grep hit for 1460) but not confirmed by me; chapter does not name the source.
- U9 Ch4: autumn 1878 "Graves lived at 88 Frampton Park Road … and William lived with him". 88 FPR is first documented in 1879 (certificate, which I viewed) and 1881 (census, viewed). Graves was at 4 Mare Street in 1871.
- U10 Ch4: banns "meant that Elizabeth had been living in the parish". The certificate (viewed) says only "after Banns". Both parties give 88 Frampton Pk Rd as residence, so the inference is plausible, but it is inference.
- U11 Ch4: "The house was full of Graves's children" in 1878: derived from 1881 ages; not documented for 1878.
- U12 Ch5: "Number 8 stood near the station end" (notes: "most likely"); September 1882 move date is a count-back from Emma Clarke's "eleven months"; trains audible; "reach Upper Thames Street by half past seven"; Clarkes on the ground floor (elimination).
- U13 Ch6: Ada's Old Bailey "twenty minutes" is silently dropped when the drownings are fitted to the bed-making window.
- U14 Ch7: Sutton "the man who had delivered the twins" (inferred from "accouchement fees … medical attendant"); Emma "came back up to the bedroom"/"across the landing"; which twin died first from Gould's post-mortem order.
- U15 Ch7: "She gave it to Cheeseman" after Cheeseman had left with William: unreconciled (notes Contradiction 30).
- U16 Ch9: hammer "wrapped in a copy of the Walthamstow Guardian, with a tartan scarf" is the Guardian's version stated flat; IPN says "neck handkerchief".
- U17 Ch9: post-mortem order (3.30 first twin, 4.30 other twin, then the three eldest). Deposition per notes says 3.30 "all the 5" and 4.30 "the other male infant". Chapter order uncertain.
- U18 Ch9: "walked from the cemetery to Courtenay Place" (no source for "walked"); "Two of his brothers" attributed to IPN while Guardian hedges "It is said…".
- U19 Ch10: grave "ten feet deep" given flat; Dover Express says 6 ft (Contradictions 42/52).
- U20 Ch1: "at least four generations" in Great Sampford rests on circumstantial Generation 1 identification (Robert and Rebecca). "Thomas working as a smith on his own account" and 1851 placement rest on a blank street column. 1841 census "twins … six": by the notes' birth date 4 Aug 1835 they were 5 years 10 months. 1841 transcription not in repo; check.
- U21 Ch3: "By 1874 the Chiltons had left London" rests on the withdrawn Chilton inference.
- U22 Ch16: doctors' visit "on the Wednesday" rests on one local report; Sunday Dispatch "six or seven hours" quoted without telling the reader the Essex Weekly News says "nearly three hours" (Contradiction 119). Liverpool Daily Post "the same day" (1 October) comes from a file name only.
- U23 Ch13/15: "The Times printed 'playing' the next morning" and "on the Friday the Times reprinted" (Law Times) need checking against the transcriptions; notes say the Times of 20 Aug prints "preying" and the reprint was in the Guardian 29 Sep. Leeds Mercury / Hansard 21 Aug withdrawal of the Criminal Appeal Bill not in transcribed (Hansard held only for 1916, 1947).
- U24 Ch12: vicar says "ten months in Walthamstow"; Ch5 puts the move at September 1882 (eleven months). Quoted, so defensible, but the book carries both.
- U25 Ch21: Albert's death "21 June 1962" stated as fact. The date comes from the headstone via the Chatham cemetery transcription (viewed as transcription only); the transcription itself says "subject to the death certificates, which govern". Burial 26 June (register). Age 76 on the stone is right only for the naval 1886 year; his true age was 75.

Low: Ch3 Susan Newman "entered as sixteen" (census says 16; she was 15, as the transcription notes; fine, but chapter says nothing); Joseph Gouldstone "80 and a widower in Saffron Walden Union Workhouse": census line gives 80, Widr, Blacksmith; the workhouse is from Findmypast's index (not census image); Hibblethwaite "65" quoted without comment (baptism 1793 implies 64-ish); Ch5 tea "as he often did" is supported by Elizabeth's statement as printed in Ch15.

## 3. Attribution problems

| # | Chapter | Issue | Sev |
|---|---|---|---|
| A1 | Ch6/7 | Press-only lines as unattributed dialogue: "Shall I leave the room…?" / "Yes, do, my dear" (Telegraph and Times 10 Aug: one reporter's text); "He says he has killed the other three children… Go and see, will you?"; "Now, I'll make your bed if you get out" (Daily News and Evening News 11 Aug: one text). | high |
| A2 | Ch6/7 | "You wished they were dead, and now they are" (IPN/Guardian shared copy) placed in Cheeseman's presence. Notes say Cheeseman and Ada deny hearing "wished dead" from Elizabeth. | high |
| A3 | Ch6 | Door reply "I am not a wicked man. I am a happy man." is the coroner-deposition version; the earlier sworn witness statement has "I have killed the children. I am a happy man now." Chosen silently (Contradiction 1). The earliest sworn document favours the latter. | high |
| A4 | Ch6/8 | "Good evening, policeman": check against sworn depositions; notes say Daily News has fuller version. | medium |
| A5 | Ch9 | Hammer wrapper (Guardian) vs IPN. | medium |
| A6 | Ch9 | "Two of his brothers" attributed to IPN; Guardian hedges. | low |
| A7 | Ch10 | "At the request of the mourners" (chosen) vs Times "with the approval" (Contr. 108). | medium |
| A8 | Ch13 | Savage interview "on the Thursday" over Sessions Paper "on Saturday" (Contr. 95); the Sessions Paper prints Saturday itself. | medium |
| A9 | Ch16 | Sunday Dispatch hours; see U22. | low |

## 4. Source problems and problems inside the notes

- N1 Walthamstow Robert: MASTER_NOTES ll.220, 386-388 treat him as probably a different man ("least likely" uncle theory). The confirmed_facts file (c. ll.1745-2260) concludes he is the uncle, d. 20 Dec 1882, and the 1935 Helen Cottages address is his. MASTER, which claims to supersede, was never updated. Ch10 follows the later file.
- N2 Reprieve date: MASTER ll.502-503 "the book's reprieve date is 3 October" and "c.10 October"; timeline: respite made indefinite 1 Oct, letter 3 Oct, certification news 10 Oct (Contr. 105). Ch16 follows the timeline (correct).
- N3 Lewis Graves: notes say "5 months", "a month apart". Census image (viewed): Lewis A. "6m", Herbert G. "4m". Ch4 "six months" is right; notes are wrong.
- N4 Contradiction 74 says no Graves letter of 15 September; l.1572 prints "The Workmen's Letter in Full" signed Graves, 15 Sept (Telegraph 17 Sept).
- N5 Contr. 8 (height 5 ft 6 in "working figure") vs 53 (withdrawn); Contr. 6, 22 vs 96 on Emma's drink evidence.
- N6 IPN portraits: notes say "five" but list six names. Ch12 says five portraits (Craggs, Gould, Hamilton, Clark, "A Witness"); not image-checked by me.
- N7 Timeline header says "Contradictions to 83"; file runs to 119.
- N8 Notes' chapter descriptions and file numbers are stale (e.g. "Chapter Seven … CHAPTER_6.md"); chapters have been restructured to 21.
- N9 Contr. 89: website index age 28 for Elizabeth in 1881 vs 26 on census image (viewed; the image says 26). The notes' own people list uses 28 for 1883, which is correct (b. 18 Feb 1855).
- N10 Items the notes mark unverified that chapters state: Ch17 uses only the certificate's address (fine); Ch14 Act date (U4); "John Street renamed / infirmary half a mile" not used.
- N11 Ada "ten minutes" with Elizabeth: notes l.277 "a few seconds" (9 Aug) vs "ten minutes"; l.827 "ten minutes" is the witness statement's. Ch6 picks one silently.
- N12 Stock death: marriage certificate (viewed) shows "Thomas Stock (dead)" in 1879; fine and consistent with Ch2.
- N13 Chatham cemetery transcription: death dates come from the headstone (MI), burial dates from register; Clarie's stone date is 2 Jan 1958, burial 7 Jan. The "2nd Inter." slip for Albert is noted by the transcriber. No error found in Ch21 beyond U25.
- N14 Transcription flags uncertain legitimacy of Lambeth entry 110; Ch17's counts (11 of 17 illegitimate, 3 stillborn) rest on that reading.

## 5. Contradictions touched by chapters: disclosed or silent

| No. | Subject | Chapter | Disclosed? | Version favoured by sources |
|---|---|---|---|---|
| 1 | Door words | 6 | silent | witness statement ("I have killed the children. I am a happy man now") is earliest sworn |
| 24 | Charles's words | 6 | silent ("My daddy put it there") | unresolved |
| 27 | Kitchen visits | 6 | silent | n/a |
| 30 | Hammer / who took it | 7/9 | silent | unresolved |
| 31 | First twin's death time | 7 | silent ("within hours") | inference |
| 41 | (as notes) | 9 | silent | not checked |
| 42/52 | Grave depth | 10 | silent (10 ft) | two papers 10 ft vs Dover Express 6 ft; Dover Express alone says "common grave" and shares text with Guardian |
| 49 | Throat gesture | 9 | disclosed | n/a |
| 56 | Emma/jury | 9 | handled | n/a |
| 59 | Gould "several times" | 11 | disclosed | n/a |
| 61, 85, 93 | misc.; after verdict | 14 | disclosed | n/a |
| 95 | Savage Thursday/Saturday | 13 | silent | Sessions Paper: Saturday |
| 102 | cord/string | 6 | silent | n/a |
| 105 | reprieve dates | 16 | handled correctly | timeline |
| 108 | request/approval | 10 | silent | Times "with the approval" |
| 113 | who told William | 8 | silent (no messenger) | n/a |
| 115, 116 | Elizabeth's Chelmsford visitors | 12/13 | silent; statement followed | n/a |
| 119 | "hours" of doctors | 16 | silent | EWN "nearly three hours" |
| 21/58 | Ada's date | 7 | silent (1 June) | n/a |
| 22/96 | drink night | 5/7 | silent | n/a |

## 6. Claims tested against primary sources (46)

Supported unless marked.
1. Marriage 15 Mar 1879, St Luke's Hackney (image): supported.
2. William 22, bachelor, iron worker; Elizabeth 24, spinster (image): supported.
3. Both at 88 Frampton Pk Rd (image): supported.
4. Fathers Thomas Goldstone smith; Thomas Stock "(dead)" (image): supported.
5. Married after Banns, John C. Harding; both signed (image): supported.
6. Witnesses Thomas Goldstone (X) and Emily Goldstone (image): supported.
7. 15 Mar 1879 a Saturday: correct.
8. Elizabeth Madams d. 29 June 1906, Beach Alley Whitstable, age 47 (image): supported.
9. "Widow of William Madams General Labourer" (image): supported.
10. "Syphilis 2 years", Jno W. Hayward MRCS (image): supported (Ch18).
11. Informant Lilian Madams, daughter, registered 2 July 1906 (image): supported.
12. 1881 census Graves schedule 249, No. 88 (image): supported.
13. William Graves 52, white smith: supported.
14. Lewis A. "6m" (image): Ch4 right; notes wrong.
15. Schedule 250 William G. Stone 24, blacksmith; Elizabeth G. 26 (image): supported.
16. Charles G. Stone 1, Herbert G. 4m (image): supported.
17. Bennett G., boarder, 19, blacksmith (image): supported.
18. Thomas Goldstone, Old Bailey: "she was in a very bad state of mind when the prisoner was born": supports Ch1.
19. Thomas's "18 years ago" strangling and business troubles: supported.
20. Stock tenement in 1861 sale, "Thomas Stock and Harriet Love": supported.
21. Raven "100 ac. 6 men & 3 boys": supported.
22. Susan Newman entered as 16 (was 15): supported.
23. Joseph 80, Widr, Blacksmith: supported (workhouse from index).
24. Lambeth register entry 105, 19 June 1887, "Albert Jennet", "Illegitimate", "G.H.": supported.
25. Mary Pratt above, "Alice Mary": supported.
26. 17 entries, 11 illegitimate, 3 stillborn: supported (entry 110 uncertain).
27. Civil register entry 113, 20 June; "2 John Street Hercules buildings"; informant "S. Frost": supported.
28. Setterington: colour sergeant, East Surrey, 1891: supported (Ch19).
29. Albert burial 26 June 1962, age 76, "Retired": supported; age 76 matches naval year only.
30. Albert death 21 June 1962: from headstone, subject to certificate (see U25).
31. Clarie Irene d. 2 Jan 1958, age 68, buried 7 Jan, grave 10/534: supported.
32. Brian d. 15 May 1937, buried 20 May: supported as transcribed.
33. Evening Standard 21 Jan 1935: "52 years … 80 years of age … ideal patient": transcription supports Ch21's outline.
34. Milne at 1935 inquest: age 78; blacksmith; "six years"; "Widower Blacksmith": outline supported, not word for word.
35. Lion 26 Nov 01 to 23 June 03; Agincourt 24 June to 8 Sept 03; Prince George 9 Sept 03 (service record): supported.
36. Agincourt 10,600 tons; "Tender to Boscawen as Depot for Boys" (Navy List): supported.
37. 1891 Whitstable census: 2 rooms, "Stepson": supported.
38. 17 Oct 1891, 5 Mar 1910, 10 Mar 1908, 4 Mar 1912 weekdays: correct.
39. Elizabeth's "got me a cup of tea, as he often did before": supported.
40. Wilhelm/Gouldstone "Statement of the Prisoner" headline: unresolved in notes.
41. Albert's true birth 19 June 1887 vs naval 19 June 1886: consistent across register and service record.
42. 1851 Thomas between miller and blacksmith: blank street column; inference.
43. 1861 census neighbours Norris/Ruffle: notes' own correction says not on page; Ch not relying.
44. Graves at 4 Mare Street 1871: noted; Ch4 does not claim otherwise.
45. 1879 Elizabeth's father already dead (cert) vs 1861 sale: consistent with Ch2.
46. Ch10 Martha as widow: not supported by primary (see U1).

Not checked: Ch2 Suckling census ages; Chelmsford Chronicle cholera/1867 sale; City Press 30 Oct 1878 ("67 Upper Thames Street"); Telegraph 10 Aug (ten weeks, Lister/Glenny/Spicer); Guardian 25 Aug ("ten months"); Times 15 Sep ("playing"); Albert/Mabel/William birth certificates (signatures); 1911 and 1921 censuses; 1939 Register; Eliza Jane and Lilian certificates; William Madams's death certificate; Gould "ran out"/"liver"; Folkard "Quite right sir".

## 7. Unused material in the notes worth the author's attention (locate by heading in the notes)

- Millard/Hobbs drowning May 1883, three reports (transcribed): Ch10 uses Mrs Millard only in a quote. A parallel case months earlier.
- Dr Orange's career and 1882 assault (MASTER_NOTES ll.825-831).
- Bucknill's lecture pairing Gouldstone and Cole; James Cole case (Old Bailey t18831015-964); Savage's JMS articles.
- Bennett's daughter Rose Elizabeth, named for Elizabeth; Bennett's wife Alice Cakebread and a Cakebread witness.
- William's second cousin and aunt (Willett/Andrews; Ann Willett = Mrs Andrews, Sunderland).
- Funeral grave 1370A (lead only).
- Robert Gouldstone's multiple households and the 1935 Helen Cottages address; the 1935 "widower" paradox (MASTER l.1143: "Each document records the other's survival under a different man's name").
- Broadmoor admission register page (MASTER ll.1147-1159); 1935 inquest details (time of death, Priest); Forster / Royal Berkshire Archives access letters.
- Lyle's letter; Foxwell's defence of Blythe (used in Ch10).
- Weather for 25 Oct 1873 (Jemima's death day).
- Mrs Pelly's refuge; Rev. Grantham Robinson's biography (d. 21 Mar 1884; St Saviour's baptised Robert's children since 1867).
- John Gouldstone of Marsh Street as "Cousin Gouldstone".
- Saffron Walden Weekly News 1953 (Housden funeral).
- Wethersfield brewery and Raven monument (partly used); Chilton family and Bristol directory.

## 8. Could not check

1841/1851/1861 census details for the Ansells; Hansard 1883; Gladstone bill; Law Times; Leeds Mercury; Times and Telegraph pages beyond the repo transcriptions; full Dover Express and Chronicle texts; Echo, Lloyd's List, Western Mail items for Ch19-20; burial register; GRO index; Findmypast index. The notes' references to these are untested claims.
