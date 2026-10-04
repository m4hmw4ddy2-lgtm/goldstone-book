import html
FONT="Georgia, 'Liberation Serif', 'Times New Roman', serif"
INK="#1a1a1a"; GREY="#666"
def esc(t): return html.escape(t)
class SVG:
    def __init__(s,w,h): s.w,s.h=w,h; s.e=[]
    def text(s,x,y,t,size=14,weight="normal",style="normal",fill=INK,anchor="middle"):
        s.e.append(f'<text x="{x}" y="{y}" font-family="{FONT}" font-size="{size}" font-weight="{weight}" font-style="{style}" fill="{fill}" text-anchor="{anchor}">{esc(t)}</text>')
    def line(s,x1,y1,x2,y2,dash=False,w=1.1):
        d=' stroke-dasharray="5,4"' if dash else ''
        s.e.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{INK}" stroke-width="{w}"{d}/>')
    def double(s,x1,x2,y):  # marriage: double line
        s.line(x1,y-2,x2,y-2,w=0.9); s.line(x1,y+2,x2,y+2,w=0.9)
    def node(s,x,y,lines,bold=False):
        # lines: list of (text, kind) kind: name|date|note
        yy=y
        for i,(t,k) in enumerate(lines):
            if k=="name": s.text(x,yy,t,15,"bold" if bold else "normal")
            elif k=="date": s.text(x,yy,t,13,fill=GREY)
            else: s.text(x,yy,t,12,style="italic",fill=GREY)
            yy+=17
    def out(s,path,title):
        body="\n".join(s.e)
        svg=f'<svg xmlns="http://www.w3.org/2000/svg" width="{s.w}" height="{s.h}" viewBox="0 0 {s.w} {s.h}"><rect width="100%" height="100%" fill="#fff"/>{body}</svg>'
        open(path,"w").write(svg)

TOP=-30  # name baseline offset: node text starts at y, connectors attach at y-16 (top) and y+bottom
def kids(s,xs,ybar,ytop):
    s.line(min(xs),ybar,max(xs),ybar)
    for x in xs: s.line(x,ybar,x,ytop)

# ---------------- TREE 1 ----------------
t=SVG(1780,820)
t.text(890,42,"Two families, to 1883",24)
R0,R1,R2,R3,R4=110,240,370,520,700
# Gouldstone side
t.node(1030,R0,[("Robert Goldstone","name"),("bap. 1751","date")])
t.node(1250,R0,[("Rebecca Taylor","name"),("b. c.1752","date")])
t.double(1093,1188,R0-5); t.line(1140,R0-3,1140,R1-22)
t.node(1140,R1,[("Joseph Gouldstone","name"),("bap. 1793","date"),("and other children","note")])
t.node(1360,R1,[("Ruth","name"),("b. c.1793","date")])
t.double(1212,1335,R1-5); t.line(1273,R1-3,1273,R2-40); t.line(1273,R2-40,1230,R2-40); t.line(1230,R2-40,1230,R2-22)
t.node(1230,R2,[("Thomas Gouldstone","name"),("bap. 1821","date")])
t.node(1500,R2,[("Emily Willett","name"),("bap. 1830","date"),("sister of Ann, Mrs Andrews","note")])
t.double(1302,1440,R2-5); t.text(1371,R2-12,"m. 1851",12,style="italic",fill=GREY)
t.line(1371,R2-3,1371,R3-55)
gx=[1010,1120,1230,1340,1450,1560,1670]
g=[("Emily","b. 1854"),("Robert","b. 1855"),("William","b. 1856"),("Thomas","b. 1859"),("Bennett","b. c.1862"),("Flora","b. 1864"),("Hugh","b. 1868")]
kids(t,gx,R3-55,R3-22)
for x,(n,d) in zip(gx,g): t.node(x,R3,[(n,"name"),(d,"date")],bold=(n=="William"))
# Stock / Ansell side
t.node(430,R1,[("Edward Suckling","name"),("b. c.1785–87","date")])
t.node(640,R1,[("Sarah","name")])
t.double(495,618,R1-5); t.line(556,R1-3,556,R2-22)
t.node(556,R2,[("Jemima Suckling","name"),("bap. 1811","date")])
t.node(250,R2,[("John Ansell","name"),("b. c.1813","date")])
t.node(820,R2,[("Thomas Stock","name"),("bap. 1802","date")])
t.double(300,488,R2-5); t.text(394,R2-12,"m. 1833",12,style="italic",fill=GREY)
t.double(624,770,R2-5); t.text(697,R2-12,"m. 1854",12,style="italic",fill=GREY)
ax=[75,160,245,330,415,500,585,670]
a=[("John Nathan","b. 1834"),("Sarah","b. 1835"),("Eliza","b. 1835"),("Alfred","b. c.1838"),("George","b. 1839"),("Emma","b. 1840"),("Arthur","b. 1843"),("Edith","b. c.1845")]
t.line(394,R2-3,394,R3-55); kids(t,ax,R3-55,R3-22)
for x,(n,d) in zip(ax,a): t.node(x,R3,[(n,"name"),(d,"date")])
t.text(202,R3+38,"twins",12,style="italic",fill=GREY)
t.text(372,R3+58,"the eight Ansell children",12,style="italic",fill=GREY)
t.line(697,R2-3,697,R3-40); t.line(697,R3-40,820,R3-40); t.line(820,R3-40,820,R3-22)
t.node(820,R3,[("Elizabeth Stock","name"),("b. 1855","date")],bold=True)
# William = Elizabeth
MB=R3+80
t.line(820,R3+24,820,MB); t.line(1230,R3+24,1230,MB); t.double(820,1230,MB)
t.text(1025,MB-10,"m. 1879",12,style="italic",fill=GREY)
cx=[870,980,1090,1200]
c=[("Charles","b. 1880"),("Herbert","b. 1881"),("Frederick William","b. 1882"),("twin sons","b. 1883")]
t.line(1025,MB+3,1025,R4-55); kids(t,cx,R4-55,R4-22)
for x,(n,d) in zip(cx,c): t.node(x,R4,[(n,"name"),(d,"date")])
t.out("backmatter/family_tree_1_to_1883.svg","Two families, to 1883")

# ---------------- TREE 2 ----------------
u=SVG(1300,900)
u.text(650,42,"Elizabeth’s later family",24)
Q0,Q1,Q2,Q3,Q4=110,280,450,620,790
u.node(650,Q0,[("Elizabeth Stock","name"),("b. 1855","date"),("married William Gouldstone, 1879","note")],bold=True)
# unnamed father
u.text(330,Q0,"father not named",14,style="italic",fill=GREY)
u.line(410,Q0-5,580,Q0-5,dash=True)
u.line(495,Q0-5,495,Q1-22)
u.node(495,Q1,[("Albert Jennet Goldstone","name"),("b. 1887","date"),("m. 1910 Clarie Irene Setterington, b. 1889","note")],bold=True)
# Madams
u.node(1000,Q0,[("William James Madams","name"),("b. 1860","date"),("together from c.1888","note")])
u.double(720,910,Q0-5); u.line(815,Q0-3,815,Q1-55)
mx=[750,950]
kids(u,mx,Q1-55,Q1-22)
u.node(750,Q1,[("Lilian Florence Isabel","name"),("b. 1890","date")])
u.node(950,Q1,[("Eliza Jane","name"),("b. 1891","date")])
# Albert's daughters
dx=[220,400,580,760]
d=[("Lily Alma Rose","b. 1913"),("Clarie Irene","b. 1918"),("Vera Georgina","b. 1921"),("Doris May","b. 1928")]
u.line(495,Q1+40,495,Q2-55); kids(u,dx,Q2-55,Q2-22)
for x,(n,dd) in zip(dx,d):
    extra=[("m. 1942 George William Ferguson, b. 1920","note")] if n=="Vera Georgina" else []
    u.node(x,Q2,[(n,"name"),(dd,"date")]+extra,bold=(n=="Vera Georgina"))
# Vera's sons
sx=[500,700]
u.line(580,Q2+40,580,Q3-55); kids(u,sx,Q3-55,Q3-22)
u.node(500,Q3,[("Michael George Ferguson","name"),("b. 1943","date"),("m. Eileen Adele Ethell, b. 1947","note")],bold=True)
u.node(700,Q3,[("Stephen Albert John","name"),("b. 1944","date")])
u.line(500,Q3+40,500,Q4-55); kids(u,[400,600],Q4-55,Q4-22)
u.node(400,Q4,[("Robert George Ferguson","name"),("b. 1968","date")])
u.node(600,Q4,[("Richard David Ferguson","name"),("b. 1970","date")],bold=True)
u.out("backmatter/family_tree_2_elizabeths_later_family.svg","Elizabeth's later family")
