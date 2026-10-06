# Family trees for the printed page, drawn at actual size (millimetres and points).
# Run from the repository root:  python3 backmatter/make_family_trees_print.py
# Writes backmatter/family_tree_1_to_1883_print.pdf and family_tree_2_elizabeths_later_family_print.pdf.
#
# Built for the SMALLEST likely trade format, B-format paperback (198 x 129 mm, text area about 100 x 160 mm),
# so that the same drawing sits at 100% in any larger format (Demy 234 x 156 and up) without scaling.
# Names 8.5 pt, dates 7 pt, notes 6.5 pt italic. Never scale these down; if content grows, re-lay out.
# Font: Liberation Serif (Times metrics) for the proof; the typesetter swaps in the book face.
# Content rules (Rik, 4 October 2026): birth year only ("bap." for a baptism, "c." when counted back), never a death year.
from reportlab.pdfgen import canvas
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

FD = "/usr/share/fonts/truetype/liberation/"
pdfmetrics.registerFont(TTFont("R", FD + "LiberationSerif-Regular.ttf"))
pdfmetrics.registerFont(TTFont("B", FD + "LiberationSerif-Bold.ttf"))
pdfmetrics.registerFont(TTFont("I", FD + "LiberationSerif-Italic.ttf"))

PAGE_W, PAGE_H = 129 * mm, 198 * mm
TB_W, TB_H = 100 * mm, 160 * mm            # text block
OX, OY = (PAGE_W - TB_W) / 2, (PAGE_H - TB_H) / 2
NAME, DATE, NOTE, TITLE = 8.5, 7, 6.5, 11
INK, GREY = (0.1, 0.1, 0.1), (0.38, 0.38, 0.38)
LW = 0.35  # line weight, points


class Page:
    """Coordinates in mm from the top-left corner of the text block."""
    def __init__(self, c):
        self.c = c

    def P(self, x, y):
        return OX + x * mm, OY + TB_H - y * mm

    def text(self, x, y, t, font="R", size=NAME, grey=False, anchor="middle"):
        c = self.c
        c.setFillColorRGB(*(GREY if grey else INK))
        c.setFont(font, size)
        px, py = self.P(x, y)
        {"middle": c.drawCentredString, "left": c.drawString, "right": c.drawRightString}[anchor](px, py, t)

    def width(self, t, font="R", size=NAME):
        return pdfmetrics.stringWidth(t, font, size) / mm

    def line(self, x1, y1, x2, y2, dash=False):
        c = self.c
        c.setStrokeColorRGB(*INK)
        c.setLineWidth(LW)
        c.setDash(1.2, 1.2) if dash else c.setDash()
        c.line(*self.P(x1, y1), *self.P(x2, y2))
        c.setDash()

    def double(self, x1, x2, y):  # marriage
        self.line(x1, y - 0.45, x2, y - 0.45)
        self.line(x1, y + 0.45, x2, y + 0.45)

    def person(self, x, y, name, date, bold=False, anchor="middle", note=None):
        """Name baseline at y; date on the next line; optional italic note below. Returns bottom y."""
        self.text(x, y, name, "B" if bold else "R", NAME, anchor=anchor)
        self.text(x, y + 3.2, date, "R", DATE, grey=True, anchor=anchor)
        if note:
            self.text(x, y + 6.0, note, "I", NOTE, grey=True, anchor=anchor)
            return y + 6.8
        return y + 4.0

    def inline(self, x, y, name, date, bold=False):
        """Name and date on one line, left-aligned (for sibling lists). Returns x of end of text."""
        self.text(x, y, name, "B" if bold else "R", NAME, anchor="left")
        w = self.width(name, "B" if bold else "R")
        self.text(x + w + 1.4, y, date, "R", DATE, grey=True, anchor="left")
        return x + w + 1.4 + self.width(date, "R", DATE)


def sibling_list(p, x, y0, people, step=4.0, bold_name=None):
    """Bracket on the left at x, entries indented. Returns dict name->(y, end_x) and last y."""
    pos = {}
    for i, (n, d) in enumerate(people):
        y = y0 + i * step
        p.line(x, y - 1.1, x + 2.2, y - 1.1)
        end = p.inline(x + 3.0, y, n, d, bold=(n == bold_name))
        pos[n] = (y, end)
    p.line(x, y0 - 1.1 - 2.5, x, y0 + (len(people) - 1) * step - 1.1)
    return pos


# ---------------------------------------------------------------- TREE 1
c = canvas.Canvas("backmatter/family_tree_1_to_1883_print.pdf", pagesize=(PAGE_W, PAGE_H))
c.setTitle("Two families, to 1883")
p = Page(c)
p.text(50, 4, "Two families, to 1883", "R", TITLE)

L, R = 3, 52  # column left edges (mm)

# Left column: Suckling, Ansell, Stock
p.text(L, 14, "Edward Suckling", "R", NAME, anchor="left")
p.text(L, 17.2, "b. c.1785–87", "R", DATE, grey=True, anchor="left")
wE = p.width("Edward Suckling")
p.double(L + wE + 1.5, L + wE + 6, 13)
p.text(L + wE + 7.5, 14, "Sarah", "R", NAME, anchor="left")
sx = L + wE + 3.75
p.line(sx, 13.5, sx, 24)
p.line(L + 1, 24, sx, 24)
p.line(L + 1, 24, L + 1, 27)
p.text(L, 30, "Jemima Suckling", "R", NAME, anchor="left")
p.text(L, 33.2, "bap. 1811", "R", DATE, grey=True, anchor="left")
JX = L + 1
p.line(JX, 34.5, JX, 64)          # Jemima's two marriages hang from this line

# (1) John Ansell
p.line(JX, 39, JX + 3, 39)
p.text(JX + 4, 40, "= John Ansell", "R", NAME, anchor="left")
p.text(JX + 4 + p.width("= John Ansell") + 1.4, 40, "b. c.1813, m. 1833", "R", DATE, grey=True, anchor="left")
ansell = [("John Nathan", "b. 1834"), ("Sarah", "b. 1835"), ("Eliza", "b. 1835"), ("Alfred", "b. c.1838"),
          ("George", "b. 1839"), ("Emma", "b. 1840"), ("Arthur", "b. 1843"), ("Edith", "b. c.1845")]
apos = sibling_list(p, JX + 6, 46, ansell)
ty = (apos["Sarah"][0] + apos["Eliza"][0]) / 2 - 1.1
p.line(max(apos["Sarah"][1], apos["Eliza"][1]) + 1.2, apos["Sarah"][0] - 1.1, max(apos["Sarah"][1], apos["Eliza"][1]) + 2.2, ty)
p.line(max(apos["Sarah"][1], apos["Eliza"][1]) + 1.2, apos["Eliza"][0] - 1.1, max(apos["Sarah"][1], apos["Eliza"][1]) + 2.2, ty)
p.text(max(apos["Sarah"][1], apos["Eliza"][1]) + 3.2, ty + 1.0, "twins", "I", NOTE, grey=True, anchor="left")

# (2) Thomas Stock
SY = 82
p.line(JX, 64, JX, SY - 1)
p.line(JX, SY - 1, JX + 3, SY - 1)
p.text(JX + 4, SY, "= Thomas Stock", "R", NAME, anchor="left")
p.text(JX + 4 + p.width("= Thomas Stock") + 1.4, SY, "bap. 1802, m. 1854", "R", DATE, grey=True, anchor="left")
EX = JX + 10
p.line(EX, SY + 1.5, EX, 101)

# Right column: Gouldstone
p.text(R, 14, "Robert Goldstone", "R", NAME, anchor="left")
p.text(R, 17.2, "bap. 1751", "R", DATE, grey=True, anchor="left")
w = p.width("Robert Goldstone")
p.double(R + w + 1.5, R + w + 5, 13)
p.text(R + w + 6.5, 14, "Rebecca Taylor", "R", NAME, anchor="left")
p.text(R + w + 6.5, 17.2, "b. c.1752", "R", DATE, grey=True, anchor="left")
RX = R + 1
p.line(RX, 18.5, RX, 27)
p.text(R, 30, "Joseph Gouldstone", "R", NAME, anchor="left")
p.text(R, 33.2, "bap. 1793", "R", DATE, grey=True, anchor="left")
p.text(R, 36.0, "and other children", "I", NOTE, grey=True, anchor="left")
w = p.width("Joseph Gouldstone")
p.double(R + w + 1.5, R + w + 5, 29)
p.text(R + w + 6.5, 30, "Ruth", "R", NAME, anchor="left")
p.text(R + w + 6.5, 33.2, "b. c.1793", "R", DATE, grey=True, anchor="left")
p.line(RX, 37.2, RX, 43)
p.text(R, 46, "Thomas Gouldstone", "R", NAME, anchor="left")
p.text(R, 49.2, "bap. 1821", "R", DATE, grey=True, anchor="left")
w = p.width("Thomas Gouldstone")
p.double(R + w + 1.5, R + w + 5, 45)
p.text(R + w + 3.25, 43.2, "m. 1851", "I", NOTE, grey=True)
p.text(R + w + 6.5, 46, "Emily Willett", "R", NAME, anchor="left")
p.text(R + w + 6.5, 49.2, "bap. 1830", "R", DATE, grey=True, anchor="left")
p.text(R + w + 6.5, 52.0, "sister of Ann,", "I", NOTE, grey=True, anchor="left")
p.text(R + w + 6.5, 54.6, "Mrs Andrews", "I", NOTE, grey=True, anchor="left")
gould = [("Emily", "b. 1854"), ("Robert", "b. 1855"), ("William", "b. 1856"), ("Thomas", "b. 1859"),
         ("Bennett", "b. c.1862"), ("Flora", "b. 1864"), ("Hugh", "b. 1868")]
gpos = sibling_list(p, RX, 62, gould, bold_name="William")
# William's line leaves his entry to the right and runs down to the marriage
wy, wend = gpos["William"]
WX = 86
p.line(wend + 1.2, wy - 1.1, WX, wy - 1.1)
p.line(WX, wy - 1.1, WX, 101)

# The marriage, 1879
NY = 104.5
p.text(EX, NY, "Elizabeth Stock", "B", NAME)
p.text(EX, NY + 3.2, "b. 1855", "R", DATE, grey=True)
p.text(WX, NY, "William Gouldstone", "B", NAME)
p.text(WX, NY + 3.2, "b. 1856", "R", DATE, grey=True)
BY = NY + 8
p.line(EX, NY + 4.3, EX, BY)
p.line(WX, NY + 4.3, WX, BY)
p.double(EX, WX, BY)
mid = (EX + WX) / 2
p.text(mid, BY - 1.3, "m. 1879", "I", NOTE, grey=True)
kids_x = [12, 35, 61, 87]
KY = BY + 10
p.line(mid, BY + 0.45, mid, KY - 4)
p.line(kids_x[0], KY - 4, kids_x[-1], KY - 4)
for x, (n, d) in zip(kids_x, [("Charles", "b. 1880"), ("Herbert", "b. 1881"),
                               ("Frederick William", "b. 1882"), ("twin sons", "b. 1883")]):
    p.line(x, KY - 4, x, KY - 2.6)
    p.person(x, KY, n, d)
c.showPage()
c.save()

# ---------------------------------------------------------------- TREE 2
c = canvas.Canvas("backmatter/family_tree_2_elizabeths_later_family_print.pdf", pagesize=(PAGE_W, PAGE_H))
c.setTitle("From Elizabeth to the author")
p = Page(c)
p.text(50, 4, "From Elizabeth to the author", "R", TITLE)

# Top: Elizabeth, the unnamed father (dashed) and William James Madams (double line)
EY = 16
p.text(50, EY, "Elizabeth Stock", "B", NAME)
p.text(50, EY + 3.2, "b. 1855", "R", DATE, grey=True)
p.text(50, EY + 6.0, "married William", "I", NOTE, grey=True)
p.text(50, EY + 8.6, "Gouldstone, 1879", "I", NOTE, grey=True)
p.text(24, EY, "father not named", "I", NOTE, grey=True, anchor="right")
p.line(25.5, EY - 1.1, 38.5, EY - 1.1, dash=True)
SX = 32
p.line(SX, EY - 1.1, SX, 40.6)
MX = 85
p.double(61.5, 68.5, EY - 1.1)
p.person(MX, EY, "William James Madams", "b. 1860", note="together from c.1888")
p.line(65, EY - 0.65, 65, 26.5)
p.line(65, 26.5, 91, 26.5)
p.line(91, 26.5, 91, 27.9)
p.person(65, 30.5, "Lilian Florence Isabel", "b. 1890")
p.person(91, 30.5, "Eliza Jane", "b. 1891")

def spouse(x, y, t, side):
    p.text(x + (1.5 if side == "right" else -1.5), y, t, "I", NOTE, grey=True,
           anchor="left" if side == "right" else "right")

# Albert
y = 44
p.person(SX, y, "Albert Jennet Goldstone", "b. 1887", bold=True)
p.line(SX, y + 4.5, SX, y + 18)
spouse(SX, y + 9.0, "= Clarie Irene Setterington, b. 1889, m. 1910", "right")
# Albert's daughters
ry = y + 22
dx = [11, 33, 55, 78]
p.line(dx[0], ry - 4, dx[-1], ry - 4)
for x, (n, d) in zip(dx, [("Lily Alma Rose", "b. 1913"), ("Clarie Irene", "b. 1918"),
                          ("Vera Georgina", "b. 1921"), ("Doris May", "b. 1928")]):
    p.line(x, ry - 4, x, ry - 2.6)
    p.person(x, ry, n, d, bold=(n == "Vera Georgina"))
# Vera
VX = 55
y = ry
p.line(VX, y + 4.5, VX, y + 18)
spouse(VX, y + 9.0, "= George William Ferguson, b. 1920, m. 1942", "left")
ry = y + 22
sons = [38, 78]
p.line(sons[0], ry - 4, sons[1], ry - 4)
for x in sons:
    p.line(x, ry - 4, x, ry - 2.6)
p.person(38, ry, "Michael George Ferguson", "b. 1943", bold=True)
p.person(78, ry, "Stephen Albert John", "b. 1944")
# Michael
y = ry
p.line(38, y + 4.5, 38, y + 18)
spouse(38, y + 9.0, "= Eileen Adele Ethell, b. 1947", "left")
ry = y + 22
gs = [20, 62]
p.line(gs[0], ry - 4, gs[1], ry - 4)
for x in gs:
    p.line(x, ry - 4, x, ry - 2.6)
p.person(20, ry, "Robert George Ferguson", "b. 1968")
p.person(62, ry, "Richard David Ferguson", "b. 1970", bold=True)
c.showPage()
c.save()
