import numpy as np, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
NAVY="#1B365D"; GOLD="#1E66D0"; GRAY="#A3ABB8"; DGRAY="#5B6575"; RED="#1E66D0"; LGRAY="#E3E7ED"
plt.rcParams.update({"font.family":"DejaVu Sans","font.size":16,"axes.edgecolor":GRAY,
  "axes.labelcolor":DGRAY,"xtick.color":DGRAY,"ytick.color":DGRAY,"axes.spines.top":False,
  "axes.spines.right":False,"svg.fonttype":"path","figure.facecolor":"none","axes.facecolor":"none"})
def clean(ax,left=False):
    ax.spines["left"].set_visible(left); ax.tick_params(length=0)

# 1. Paradoxo
fig,ax=plt.subplots(figsize=(6.8,4.3))
yrs=[2023,2024,2025,2026]; pos=[49,50,52,53]
ax.set_ylim(66,0); ax.set_xlim(-0.6,2.2)
ax.plot([0,1.65],[13,53],color=LGRAY,lw=2,ls="--",zorder=1)
ax.scatter([0],[13],s=420,color=NAVY,zorder=3)
ax.text(-0.12,13,"Top 15",ha="right",va="center",fontsize=24,color=NAVY,fontweight="bold")
ax.text(0,20.5,"produção científica\nem IA",ha="center",va="top",fontsize=14,color=DGRAY)
xs=np.linspace(0.95,1.65,4)
ax.plot(xs,pos,color=GRAY,lw=2.5,zorder=2); ax.scatter(xs[:3],pos[:3],s=60,color=GRAY,zorder=3)
for x,y,a in zip(xs[:3],pos[:3],yrs[:3]): ax.text(x,y-2.6,f"{y}º",ha="center",fontsize=12,color=DGRAY); ax.text(x,y+4.2,str(a),ha="center",fontsize=11,color=GRAY)
ax.scatter([xs[3]],[53],s=420,color=RED,zorder=4)
ax.text(xs[3]+0.12,53,"53º",ha="left",va="center",fontsize=30,color=RED,fontweight="bold")
ax.text(xs[3],57.2,"2026",ha="center",fontsize=11,color=RED)
ax.text(1.3,62.5,"Índice Global de Inovação (OMPI)",ha="center",va="center",fontsize=14,color=DGRAY)
ax.text(0.9,27,"≈ 40 posições",ha="center",fontsize=16,color=RED,fontweight="bold")
ax.set_xticks([]); ax.set_yticks([]); ax.spines["left"].set_visible(False); ax.spines["bottom"].set_visible(False)
fig.tight_layout(); fig.savefig("fig/paradoxo.svg",bbox_inches="tight"); plt.close()

# 2. Dupla descida
rng=np.random.default_rng(7)
n,P,ntest=60,240,2000
beta=rng.normal(size=P)*np.exp(-np.arange(P)/60); beta*=2/np.linalg.norm(beta)
ps=np.arange(2,240,2); risks=[]
for p in ps:
    r=[]
    for _ in range(40):
        X=rng.normal(size=(n,P)); y=X@beta+0.5*rng.normal(size=n)
        Xt=rng.normal(size=(ntest,P)); yt=Xt@beta+0.5*rng.normal(size=ntest)
        b=np.linalg.pinv(X[:,:p])@y; r.append(np.mean((yt-Xt[:,:p]@b)**2))
    risks.append(np.median(r))
risks=np.array(risks)
fig,ax=plt.subplots(figsize=(5.6,3.6))
cl=ps<=n
ax.plot(ps[cl],risks[cl],color=GRAY,lw=3)
ax.plot(ps[~cl],risks[~cl],color=GOLD,lw=4.5)
ax.plot(ps[(ps>=n-2)&(ps<=n+2)],risks[(ps>=n-2)&(ps<=n+2)],color=GRAY,lw=3)
ax.set_yscale("log"); ax.set_ylim(1.5,max(risks)*1.6)
ip=np.argmax(risks); ax.annotate("pico em p ≈ n",xy=(ps[ip],risks[ip]),xytext=(ps[ip]+25,risks[ip]*0.95),fontsize=15,color=DGRAY,arrowprops=dict(arrowstyle="-",color=GRAY))
ax.text(24,risks[0]*1.6,"o “U”\nclássico",ha="center",fontsize=14,color=DGRAY)
ax.text(165,risks[-1]*1.55,"o erro volta a cair",ha="center",fontsize=19,color=GOLD,fontweight="bold")
ax.set_yticks([]); ax.minorticks_off(); ax.spines["left"].set_visible(False); ax.tick_params(length=0)
ax.set_xlabel("nº de parâmetros p   (simulação, n = 60)",fontsize=13)
ax.set_xticks([0,60,120,180,240])
fig.tight_layout(); fig.savefig("fig/dupla_descida.svg",bbox_inches="tight"); plt.close()

# 3. Calibração
conf=np.linspace(0.05,0.95,10); over=conf**1.9*0.92+0.02
fig,ax=plt.subplots(figsize=(5.0,4.2))
ax.plot([0,1],[0,1],color=GRAY,lw=2)
ax.text(0.24,0.33,"calibração perfeita",rotation=40,fontsize=13,color=DGRAY,ha="center")
ax.plot(conf,over,color=RED,lw=4,marker="o",ms=7)
ax.text(0.84,0.2,"modelo\nsobreconfiante",fontsize=15,color=RED,ha="center")
ax.annotate("",xy=(0.95,over[-1]),xytext=(0.95,0.95),arrowprops=dict(arrowstyle="<->",color=RED,lw=2))
ax.scatter([0.95],[0.95],s=60,color=GRAY,zorder=3)
ax.text(0.9,0.97,"diz 95%",ha="right",fontsize=16,color=DGRAY,fontweight="bold")
ax.text(0.9,over[-1]-0.03,"acerta 85%",ha="right",va="top",fontsize=18,color=RED,fontweight="bold")
ax.set_xlim(0,1.02); ax.set_ylim(0,1.05)
ax.set_xticks([0,0.5,1]); ax.set_xticklabels(["0%","50%","100%"]); ax.set_yticks([0,0.5,1]); ax.set_yticklabels(["0%","50%","100%"])
ax.set_xlabel("confiança declarada",fontsize=13); ax.set_ylabel("acerto observado",fontsize=13); ax.tick_params(length=0)
fig.tight_layout(); fig.savefig("fig/calibracao.svg",bbox_inches="tight"); plt.close()

# 4. Conformal
rng=np.random.default_rng(3)
def gen(m):
    x=rng.uniform(0,10,m); s=np.where(x<7,0.4,1.6); y=np.sin(x)+0.3*x+s*rng.normal(size=m); return x,y
f=lambda x: np.sin(x)+0.3*x
xc,yc=gen(2000); sc=np.abs(yc-f(xc)); alpha=0.1
q=np.quantile(sc,np.ceil((len(sc)+1)*(1-alpha))/len(sc),method="higher")
xt,yt=gen(20000); cov=np.abs(yt-f(xt))<=q; g1=xt<7
m,c1,c2=cov.mean(),cov[g1].mean(),cov[~g1].mean(); print("cov",m,c1,c2)
xs,ys=gen(220); inside=np.abs(ys-f(xs))<=q
gx=np.linspace(0,10,400)
fig,ax=plt.subplots(figsize=(5.4,3.8))
ax.axvspan(7,10,color=RED,alpha=.06,lw=0)
ax.fill_between(gx,f(gx)-q,f(gx)+q,color=GRAY,alpha=.25,lw=0)
ax.plot(gx,f(gx),color=DGRAY,lw=2)
ax.scatter(xs[inside],ys[inside],s=13,color=GRAY)
ax.scatter(xs[~inside],ys[~inside],s=34,color=RED,zorder=3)
ax.set_ylim(-3,12.8)
ax.text(3.5,12.4,"Grupo A",ha="center",va="top",color=DGRAY,fontsize=16)
ax.text(3.5,10.6,f"{c1*100:.0f}%",ha="center",va="top",color=DGRAY,fontsize=24,fontweight="bold")
ax.text(8.5,12.4,"Grupo B",ha="center",va="top",color=RED,fontsize=16)
ax.text(8.5,10.6,f"{c2*100:.0f}%",ha="center",va="top",color=RED,fontsize=30,fontweight="bold")
ax.text(5,-2.7,"faixa cinza: intervalo conforme de 90%   ·   pontos azuis: fora",ha="center",va="bottom",color=DGRAY,fontsize=11.5)
ax.set_xticks([]); ax.set_yticks([]); ax.spines["left"].set_visible(False); ax.spines["bottom"].set_visible(False)
fig.tight_layout(); fig.savefig("fig/conforme.svg",bbox_inches="tight"); plt.close()
