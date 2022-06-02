%matplotlib inline
from MeanStars import MeanStars
import matplotlib.pyplot as plt
import matplotlib
import matplotlib.colors as colors
import numpy as np
import pandas as pd
import matplotlib.patches as patches
import matplotlib.patheffects as PathEffects

from matplotlib import rc
rc('font',**{'family':'serif','serif':['Helvetica']})
plt.rcParams['pdf.fonttype'] = 42


ms = MeanStars()

temp = np.linspace(start=2060, stop=30000, num=3000)
distance = np.linspace(start=0, stop=8000, num=3000)

mass = []
mags = []
color = []
for i in temp:
    mags.append(ms.TeffOther('M_Ks',i))
    mass.append(ms.TeffOther('Msun',i))
    color.append(ms.TeffColor('H','Ks',i))

KeckLimit=21.1

A = []
for i in distance:
    Ksmag=KeckLimit
    A.append(float(Ksmag))

X = []
count=-1
for i in distance:
    count=count+1
    Ksmag=3.27+5*np.log10(i/10)+color[count]
    X.append(float(Ksmag))    

    
# Mass 0.67
Z = []
count=-1
for i in distance:
    count=count+1
    Ksmag=4.525+5*np.log10(i/10)+color[count]
    Z.append(float(Ksmag))
    
# Mass 1.00 (+0.33)
Y = []
count=-1
for i in distance:
    count=count+1
    Ksmag=3.27+5*np.log10(i/10)+color[count]
    Y.append(float(Ksmag))
    
# Mass 0.5
P = []
count=-1
for i in distance:
    count=count+1
    Ksmag=ms.TeffOther('M_Ks',3720)+5*np.log10(i/10)+color[count]
    P.append(float(Ksmag))
    
# Mass 0.6
P = []
count=-1
for i in distance:
    count=count+1
    Ksmag=ms.TeffOther('M_Ks',3950)+5*np.log10(i/10)+color[count]
    P.append(float(Ksmag))
    
# Mass 0.93
F = []
count=-1
for i in distance:
    count=count+1
    Ksmag=ms.TeffOther('M_Ks',5455)+5*np.log10(i/10)+color[count]
    F.append(float(Ksmag))

# Mass 1.4
J = []
count=-1
for i in distance:
    count=count+1
    Ksmag=ms.TeffOther('M_Ks',6660)+5*np.log10(i/10)+color[count]
    J.append(float(Ksmag))   
    
# Mass 0.3
L = []
count=-1
for i in distance:
    count=count+1
    Ksmag=ms.TeffOther('M_Ks',3300)+5*np.log10(i/10)+color[count]
    L.append(float(Ksmag))   

#print(ms.TeffOther('Msun',3008))
# Mass 0.54 (-[0.13])
#U = []
#count=-1
#for i in distance:
#    count=count+1
#    Ksmag=5.36+5*np.log10(i/10)+color[count]
#    U.append(float(Ksmag))
    
# Mass 0.16
U = []
count=-1
for i in distance:
    count=count+1
    Ksmag=8.36+5*np.log10(i/10)+color[count]
    U.append(float(Ksmag))
    
# Mass 0.075
#U = []
#count=-1
#for i in distance:
#    count=count+1
#    Ksmag=10.9+5*np.log10(i/10)+color[count]
#    U.append(float(Ksmag))
    
# Mass < 0.075
UU = []
count=-1
for i in distance:
    count=count+1
    Ksmag=11.55+5*np.log10(i/10)+color[count]
    UU.append(float(Ksmag))


# Lower Mass limit with parallax (0.13)
#N = []
#count=-1
#for i in distance:
 #   count=count+1
 #   Ksmag=ms.TeffOther('M_Ks',3008)+5*np.log10(i/10)+color[count]
 #   N.append(float(Ksmag))
    
# Lower Mass limit with parallax (0.10)
N = []
count=-1
for i in distance:
    count=count+1
    Ksmag=ms.TeffOther('M_Ks',2850)+5*np.log10(i/10)+color[count]
    N.append(float(Ksmag))

## PLOT THETA_E
C = []
count=-1
for i in distance:
    count=count+1
    #massey=1.38*(i/8000)/(1-(i/8000))
    massey=0.9823*(1.26)**2*(i/8000)/(1-(i/8000))*(8000/8000)
    C.append(float(massey))

data = [mass, mags, C]
df = pd.DataFrame(data) 
df = df.T
df.columns=['Mass','M_Ks','ThetaE Mass']

z = np.polyfit(mass, mags, 10)
p = np.poly1d(z)
V = []
V=p(C[:])
K=V.tolist()

D = []
count=-1
for i in distance:
    count=count+1
    Ksmag=K[count]+5*np.log10(i/10)+color[count]
    D.append(float(Ksmag))
    
## PLOT THETA_E_MIN
C = []
count=-1
for i in distance:
    count=count+1
    #massey=1.27*(i/8000)/(1-(i/8000))
    massey=0.9823*(1.20)**2*(i/8000)/(1-(i/8000))*(8000/8000)
    C.append(float(massey))

data = [mass, mags, C]
df = pd.DataFrame(data) 
df = df.T
df.columns=['Mass','M_Ks','ThetaE Mass']

z = np.polyfit(mass, mags, 10)
p = np.poly1d(z)
V = []
V=p(C[:])
K=V.tolist()
    
Dmin = []
count=-1
for i in distance:
    count=count+1
    Ksmag=K[count]+5*np.log10(i/10)+color[count]
    Dmin.append(float(Ksmag))
    
## PLOT THETA_E_MAX
C = []
count=-1
for i in distance:
    count=count+1
    #massey=1.49*(i/8000)/(1-(i/8000))
    massey=0.9823*(1.32)**2*(i/8000)/(1-(i/8000))*(8000/8000)
    C.append(float(massey))

data = [mass, mags, C]
df = pd.DataFrame(data) 
df = df.T
df.columns=['Mass','M_Ks','ThetaE Mass']

z = np.polyfit(mass, mags, 10)
p = np.poly1d(z)
V = []
V=p(C[:])
K=V.tolist()
    
Dmax = []
count=-1
for i in distance:
    count=count+1
    Ksmag=K[count]+5*np.log10(i/10)+color[count]
    Dmax.append(float(Ksmag))

    
mag = []
Msun2=[]
MKs2=[]
Dist2=[]
color2=[]
count=-1
for i in mass:
    count=count+1
    for j in distance:
        Ksmag=mags[count]+5*np.log10(j/10)+color[count]
        mag.append(float(Ksmag))
        Msun2.append(i)
        MKs2.append(mags[count])
        color2.append(color[count])
        Dist2.append(j)

#Create Figure
fig = plt.figure(figsize=(16, 12))
ax = fig.add_subplot(111)
    
ax.tick_params(direction='in', length=6, which='major', width=3, grid_alpha=0.5, top=0, right=0)
ax.tick_params(direction='in', length=4, which='minor', width=2, grid_alpha=0.5, top=1, right=1)
    
fontsize = 24
hfont = {'fontname':'Helvetica'}
    
for axis in ['top','bottom','left','right']:
    ax.spines[axis].set_linewidth(2.5)
        
for tick in ax.xaxis.get_major_ticks():
    tick.set_pad(9.)
    tick.label1.set_fontsize(fontsize)
    tick.label1.set_fontweight('bold')
    tick.label1.set_fontname(**hfont)
for tick in ax.yaxis.get_major_ticks():
    tick.set_pad(9.)
    tick.label1.set_fontsize(fontsize)
    tick.label1.set_fontweight('bold')
    tick.label1.set_fontname(**hfont)
    
#raph = ax.scatter(x, y, c=z, cmap='coolwarm', s=200)    
#b = fig.colorbar(graph)
#b.set_label('Mean Value', rotation=-90, va='bottom')

plt.ylabel('H-band Magnitude', fontsize = 24, fontweight='bold', labelpad=15, **hfont)
plt.xlabel('Distance (pc)', fontsize = 24, fontweight='bold', labelpad=10, **hfont)
plt.ylim(22, 12)
plt.xlim(500, 4500)

thetaE_color='#4ECDC4'
limit_color='#3b3c40'
whitelabel='#f7f7f7'
scatter=ax.scatter(Dist2, mag, c=Msun2, s=150, rasterized=True, edgecolor='', norm=colors.LogNorm(vmin=min(Msun2), vmax=max(Msun2)), marker=",", alpha=0.2, 
                   cmap='magma')
#plt.hexbin(Dist2, mag, C=Msun2, norm=colors.LogNorm(vmin=min(Msun2), vmax=max(Msun2)), alpha=0.5, gridsize=(70,70), cmap=plt.cm.viridis)
#cmap=plt.cm.Greens
#ax.tricontour(Dist2, mag, Msun2, 15, linewidths=0.5, colors='k')
#ax.plot(distance, X,color = thetaE_color, markersize = 1.0, label='')
#ax.plot(distance, Y,color = thetaE_color, markersize = 1.0, label='')
#ax.plot(distance, Z,color = thetaE_color, markersize = 1.0, label='')
ax.plot(distance, D,color = whitelabel, linewidth=8, markersize = 1.0, label='')
ax.plot(distance, Dmin,color = whitelabel, linewidth=8, markersize = 1.0, label='')
ax.plot(distance, Dmax,color = whitelabel, linewidth=8, markersize = 1.0, label='')

ax.plot(distance, A, color = whitelabel, linewidth=3, markersize = 1.0, label='')



#ax.plot(distance, Z,'-',color = whitelabel, linewidth=2, markersize = 1.0, label='')
#PLOT PARALLAX LOWER LIMIT
#ax.plot(distance, N,'--',color = whitelabel, linewidth=3, dashes=(6, 2), markersize = 1.0, label='')
#ax.plot(distance, X,'--',color = whitelabel, linewidth=3, dashes=(6, 2), markersize = 1.0, label='')
#ax.plot(distance, Y,'--',color = whitelabel, linewidth=3, dashes=(6, 2), markersize = 1.0, label='')
ax.plot(distance, F,color = whitelabel, linewidth=3, markersize = 1.0, label='')
ax.plot(distance, L,'--',color = whitelabel, linewidth=3, dashes=(6, 2), markersize = 1.0, label='')
ax.plot(distance, P,'--',color = whitelabel, linewidth=3, dashes=(6, 2), markersize = 1.0, label='')
ax.plot(distance, U,'-',color = whitelabel, linewidth=3, markersize = 1.0, label='')
#plt.fill_between(distance, U, Y, color=thetaE_color, alpha='0.3')
#plt.fill_between([500,2900],0,KeckLimit, hatch="//",color='#CDCDCD',  alpha='0.2')
#plt.fill_between([500,2900],KeckLimit,25, hatch="//",color='#CDCDCD',  alpha='0.2')
#plt.fill_between(0,8000,22,19.5, color='#CDCDCD', alpha='0.2')
#plt.fill_between([0,1700],22,KeckLimit, color='#CDCDCD', alpha='0.5')
#plt.fill_between([1700,2900],22,KeckLimit, color='#CDCDCD', alpha='0.5')
#plt.fill_between([2900,8000],22,KeckLimit, color='#CDCDCD', alpha='0.5') 
#plt.fill_between([3700,10000],0,KeckLimit, color='#CDCDCD',  alpha='0.2')
plt.fill_between([0,8000],22,KeckLimit, color='#CDCDCD', alpha=0.6) 
plt.fill_between(distance,22, U, color='#CDCDCD', alpha=0.3) 
plt.fill_between(distance, F, 12, color='#CDCDCD', alpha=0.3) 
plt.fill_between(distance, Dmin, Dmax, color=whitelabel, alpha=1.0, rasterized=True)
ax.set_xticks(ax.get_xticks()[1:])
#ax.axvspan(1700, 2900, hatch="X", linewidth=0.0)
#ax.axhspan(22,15, color='#CDCDCD', alpha='0.2')
matplotlib.rcParams['mathtext.fontset'] = 'cm'
#matplotlib.rcParams['mathtext.rm'] = 'Computer Modern'
#matplotlib.rcParams['mathtext.bf'] = 'Computer Modern:bold'
##Insert Labels (Manual Position)
#txt=ax.text(750, 20.15, r'\pi_E', fontsize=35, weight='bold', alpha=0.8, color='#f7f7f7', **hfont)
#xt=ax.text(750, 20.65, r'lower limit, fontsize=35, weight='bold', alpha=0.8, color='#f7f7f7', **hfont)

#LOWER_LIMIT_PI_E_LABEL
txt=ax.text(900, 20.12, r'lower limit', fontsize=24, weight='bold', alpha=0.8, color='#f7f7f7', **hfont)
txt=ax.text(900, 20.50, r'from $\mathrm{\pi_E}$', fontsize=24, weight='bold', alpha=0.8, color='#f7f7f7', **hfont)

#UPPER_LIMIT_PI_E_LABEL
txt=ax.text(3225, 16.95, r'upper limit', fontsize=24, weight='bold', alpha=0.8, color='#f7f7f7', **hfont)
txt=ax.text(3225, 17.33, r'from $\mathrm{\pi_E}$', fontsize=24, weight='bold', alpha=0.8, color='#f7f7f7', **hfont)

#txt=ax.text(2900, 20.85, r'Keck Detection Limit', fontsize=35, weight='bold', alpha=0.8, color='#f7f7f7', **hfont)
txt=ax.text(1800, 21.68, r'Keck Detection Limit', fontsize=24, weight='bold', alpha=0.8, color='#f7f7f7', **hfont)
txt=ax.text(3240, 13.90, r'$\theta_E$ constraint', fontsize=24, weight='bold', alpha=1.0, color='#f7f7f7', **hfont)
#txt=ax.text(1035, 13.32, r'$1.0M_{\odot}$', fontsize=30, weight='bold', alpha=1.0, color='#f7f7f7', **hfont)
txt=ax.text(1035, 13.62, r'0.93', fontsize=24, weight='bold', alpha=1.0, color='#f7f7f7', **hfont)
txt=ax.text(1295, 13.63, r'M$_{\odot}$', fontsize=24, weight='bold', alpha=1.0, color='#f7f7f7', **hfont)
txt=ax.text(890, 14.72, r'0.6', fontsize=24, weight='bold', alpha=1.0, color='#f7f7f7', **hfont)
txt=ax.text(1075, 14.73, r'M$_{\odot}$', fontsize=24, weight='bold', alpha=1.0, color='#f7f7f7', **hfont)
#txt=ax.text(2350, 18.55, r'$0.3M_{\odot}$', fontsize=30, weight='bold', alpha=1.0, color='#f7f7f7', **hfont)
txt=ax.text(735, 16.3, r'0.3', fontsize=24, weight='bold', alpha=1.0, color='#f7f7f7', **hfont)
txt=ax.text(920, 16.31, r'M$_{\odot}$', fontsize=24, weight='bold', alpha=1.0, color='#f7f7f7', **hfont)
txt=ax.text(1490, 19.15, r'0.15', fontsize=24, weight='bold', alpha=1.0, color='#f7f7f7', **hfont)
txt=ax.text(1750, 19.16, r'M$_{\odot}$', fontsize=24, weight='bold', alpha=1.0, color='#f7f7f7', **hfont)
#txt=ax.text(590, 17.4, r'$0.16M_{\odot}$', fontsize=23, weight='bold', alpha=1.0, color='#f7f7f7', **hfont)

style="Simple,tail_width=2.8,head_width=14,head_length=16"
kw = dict(arrowstyle=style, color= whitelabel)
a = patches.FancyArrowPatch((890,19.65), (1100,18.85),connectionstyle="arc3,rad=-.4", **kw)
a = patches.FancyArrowPatch((1530,20.2), (1800,19.8),connectionstyle="arc3,rad=.4", **kw)
b = patches.FancyArrowPatch((4050,13.77), (4270,14.17),connectionstyle="arc3,rad=-.4", **kw)
c = patches.FancyArrowPatch((1750,21.60), (1580,21.20),connectionstyle="arc3,rad=-.3", **kw)
d = patches.FancyArrowPatch((3850,17.15), (4070,16.75),connectionstyle="arc3,rad=.4", **kw)
plt.gca().add_patch(a)
plt.gca().add_patch(b)
plt.gca().add_patch(c)
plt.gca().add_patch(d)
#txt=ax.text(3600, 14.5, 'MOA 2010-BLG-477\nMass Constraint', fontsize=35, weight='bold', alpha=0.8, color='#011627', **hfont)
#txt=ax.text(3850, 17.1, 'MOA 2010-BLG-477 Mass Constraint', rotation=-12, fontsize=25, weight='bold', alpha=0.8, color='#011627', **hfont)
#txt.set_path_effects([PathEffects.withStroke(linewidth=2.5, foreground='#011638')])
cbar=plt.colorbar(scatter, pad=0.02)
cbar.set_label(r'Stellar Mass (M$_\odot)$', weight='bold', labelpad=1.2, size=fontsize, **hfont)
cbar.set_alpha(1)
cbar.draw_all()
cbar.outline.set_linewidth(2)
cbar.ax.set_yticklabels(['0.1','1','10'],  weight='bold', size=fontsize, **hfont)
cbar.ax.tick_params(which='major', width=3, length=5)
cbar.ax.tick_params(which='minor', width=2, length=3)

ticks = ax.get_xticks()
ax.set_xticks(ticks[:-1])

#ax.set_rasterization_zorder=0

#cbar.ax.set_ticks()

plt.savefig('MS_new v2.pdf', dpi=300)
#plt.show()
