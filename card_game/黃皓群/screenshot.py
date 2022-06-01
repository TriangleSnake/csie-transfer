from PIL import Image
stx=2
bdx=76
ax=15
sty=14
bdy=115
ay=15
img=Image.open('full.png')
n_img=[]
for i in range(1,14):
    index=0
    for j in 'cdhs':
        img.crop((stx+(i-1)*(bdx+ax),sty+index*(bdy+ay),stx+(i-1)*(bdx+ax)+bdx,sty+(index)*(bdy+ay)+bdy)).save(j+str(i)+'.png','png')
        index+=1

img=Image.open('fold.png')
img=img.resize((76,115))
img.save('fold_n.png','png')