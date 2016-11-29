import sys
import random
import pickle
import time
#import androidhelper


#d= androidhelper.Android()


def sleep(n):
  time.sleep(float(n)/166.0)
  #time.sleep(n)
  return


def go(ss,rly=0):
  #return
  if rly!=114:
    print ss
    return
  #d.ttsSpeak(" "+ss)
  #cc=0
  #while d.ttsIsSpeaking().result==True and cc < 200:
  #  cc+=1
  #  print ".",
  #  sys.stdout.flush()
  #  time.sleep(.083)

def shake(n):
 return
 for g in xrange(n/2+1):
    #d.vibrate()
    sleep(0.02)
    

tanks=26
minlen =10
gunodds = 3 # 1 in this chhance of extra guns on the map. (power ups)



cols=40
rows=80
nmg=0
tx=[0]*tanks
ty=[0]*tanks
ips=[0] *tanks
dead=[0] *tanks
killers=[0]*tanks


ucalpha="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lcalpha= ucalpha.lower()
go (ucalpha)

try:
  print 'Loading DNA..'
  f=open("/tmp/tankdnas","r")
  dnas=pickle.load(f)
  f.close()
  print 'Loading Lens..'
  f=open("/tmp/tanklens","r")
  DNAlens=pickle.load(f)
  f.close()

  print 'Loading Gens..'
  f=open("/tmp/tankgens","r")
  gens=pickle.load(f)
  f.close()

except:
  print 'Pre-existing configuration missing or corrupt.  Starting new...'
  dnas=[""]*tanks

  DNAlens=[0]*tanks
  for a in xrange(tanks):
    DNAlens[a] = 200
    for n in xrange(DNAlens[a]):
      dnas[a]+=random.choice(["f","m","e" ,"p","6" ,"j","s"])+random.choice(["^",">", "v", "<"])

  gens=[0]*tanks #do this is pickling fails


for dbg in xrange(1):
  go( ucalpha[dbg] + " " + repr(dnas[dbg]),114)


map=[]
for a in xrange(rows):
  map.append("")
  for n in xrange(cols):
    if random.choice(xrange(gunodds))==0:
      map[a]+="~"
    else:
      map[a]+="."

tx=[0]*tanks
ty=[0]*tanks
ips=[0] *tanks
dead=[0] *tanks
killers=[0]*tanks
score=[0]*tanks
lived=[0]*tanks

guns=[1]*tanks
stack=[[31,34,36,38]]*tanks

mutrate=17
drawevery=55
maxgamelen=2000

for n in xrange(tanks):
  tx[n]=random.choice(xrange(cols))
  ty[n]= random.choice(xrange(rows))

drawctr=drawevery

frames=0
while 1:
  frames+=1
  anyalive=0
  if drawctr==drawevery:
    print
    for line in xrange(rows):
      l = map[line]
      for n in xrange(tanks):
        if ty[n]==line:
          l= list(l)
          if dead[n]>0:
          # so famous records. Uppercase letter is tank is dead
       #also famous records equals show flaming wreckage
      #hidden text to speech for comments 
    #using
            l[tx[n]]= random.choice(["@","&","#","$"])
          else:
            l[tx[n]]=ucalpha[n]
            anyalive += 1
        l="".join(l)
      print l
      drawctr=0
  else:
    drawctr+=1
    for n in xrange(tanks):
      if dead[n]==0:
        anyalive+=1
  
  # wait and clear
  if drawctr==0:
    sleep(80)

  if anyalive <= 1 or frames >= maxgamelen:
    frames=0
    map=[]
    for a in xrange(rows):
      map.append("")
      for n in xrange(cols):
        if random.choice(xrange(gunodds))==0:
          map[a]+="~"
        else:
          map[a]+="."
    top=-1
    hi=0
    score=[0]*tanks
    for tank in xrange(tanks):
      for a in xrange(tanks):
        if killers[a]==tank:
          score[tank]+=1
      try:
        score[tank]=float(score[tank])/float(lived[tank])
      except:
        pass
    for tank in xrange(tanks):
      if score[tank] > hi:
        hi=score[tank]
        top=tank
    
    go( "top tank #"+str(top)+" "+str(gens[top])+" generations. score "+str(score[top]), rly=114)
    topdna=str(dnas[top])
    topgen=gens[top]
    topdl=DNAlens[top]
    dnas=[""]*tanks
    gens=[topgen+1]*tanks
    dnas[0]=str(topdna)
    gens[0]=topgen
    tx=[0]*tanks
    ty=[0]*tanks
    ips=[0] *tanks
    dead=[0] *tanks
    killers=[0]*tanks
    DNAlens=[topdl]*tanks
    score=[0]*tanks
    lived=[0]*tanks
    guns=[1]*tanks
    stack=[[31,34,36,38]]*tanks

    for n in xrange(tanks):
      tx[n]=random.choice(xrange(cols))
      ty[n]= random.choice(xrange(rows))

    for tank in xrange(1,tanks):
      for l in topdna:
        if random.choice(xrange(mutrate))==0:
          if l == "m" or l == "f" or l == "e" or l == "p" or l == "6" or l == "j" or l == "s":
            dnas[tank]+=random.choice(["m","f","e" ,"p","6","j","s" ])
          else:
            dnas[tank]+=random.choice(["^","v","<",">"])
        else:
          dnas[tank]+=l 
      if random.choice(xrange(mutrate))==0:
        #change lengths
        if random.choice(xrange(2)) == 0:
          # longer
          DNAlens[tank]+=1
          dnas[tank]+=random.choice(["m","f","e","p","6","j","s"])
          dnas[tank]+=random.choice(["^","v","<",">"])
        else:
          # shorter
          if DNAlens[tank]>1:
            DNAlens[tank]-=1
            dnas[tank]=dnas[tank][:-2]
    f=open("/tmp/tankdnas","w")
    pickle.dump(dnas,f)
    f.close()
    f=open("/tmp/tanklens","w")
    pickle.dump(DNAlens,f)
    f.close()
    f=open("/tmp/tankgens","w")
    pickle.dump(gens,f)
    f.close()
    # end extinction event
  if drawctr==0:
   # for n in xrange(rows):
    #  print
    pass
# ok
# so, gentically move teh tanks
  for tank in xrange(tanks):
    if dead[tank]>0:
      go( "tank "+ ucalpha[tank] +" is flaming wreckage,")
      #print " & was shot by "+ucalpha[killers[tank]]+"..."
      sleep(.07)
      continue
    lived[tank] += 1
    t=list(map[ty[tank]])
    t[tx[tank]]= lcalpha[tank]
    map[ty[tank]]="".join(t)
    op=dnas[tank][ips[tank]*2:ips[tank]*2+2]
# debug output
    go( "Tank "+ ucalpha[tank])
    if op[0]=="f":
      go( "fires")
    elif op[0]=="m":
      go("moves")
    else:
      #print "???",
      pass
    #print op[1]+" [ip "+str(ips[tank])+"/"+str(DNAlens[tank])+"]"
    #sleep(.1)
# end debug output
    if op[0]=="e":
      #sawself=0
      dist=1
      sawself=0
      if 1 == 1: # animals
          if op[1]=="^":
            xtr=0
            ytr=-1
          elif op[1]=="<":
            xtr=-1
            ytr=0
          elif op[1]=="v":
            xtr=0
            ytr=1
          elif op[1]==">":
            xtr=1
            ytr=0
          else:
            print "it senses an unrecognized way, (" +op[1]+")!"
            #shouldn't happen
            #sleep(.5)
          shoty=ty[tank]
          shotx=tx[tank]
          hit = 0
          while hit == 0 and map[shoty][shotx] != "." and map[shoty][shotx] != "~":
            shoty += ytr
            if shoty < 0:
              shoty+=rows
            elif shoty >= rows:
              shoty -= rows
            shotx += xtr
            if shotx < 0:
              shotx+=cols
            elif shotx >= cols:
              shotx -= cols
            #then the shot is somewhere a tanck has been
            for a in xrange(tanks):
              if dead[a]>0:
                continue
              if tx[a] == shotx and ty[a] == shoty:
                go( "tank "+ ucalpha[tank]+ " SEEES enemy tank "+ucalpha[a]+"!!",1)
               # shake(random.choice(range(5,17)))
                #sleep(2)
                #dead[a]=1
                #killers[a]=tank
                hit=1
                if tank==a:
                  sawself=1
            dist+=1
          if hit == 0:
              #hit wall
            if map[shoty][shotx]==".":
              go ( "Tank "+ucalpha[tank]+" saw a rock!",1)
              hit=2
            elif map[shoty][shotx]=="~":
              go ( "Tank "+ucalpha[tank]+" saw a gun!",1)
              hit=3
            else:
              go("ehat can herr seeee",rly=1)
            #sleep(0.15)
           # t=list(map[shoty])
          #  t[shotx]= "*"
          #  map[shoty]="".join(t)
      if hit == 0:
        go("why hits zero here",1)
      elif hit == 1:
        if sawself==1:
          basejmp = 80
        else:
          basejmp=60    
        stack.append(a)
        go(""+ucalpha[tank]+" stacks sight of "+ucalpha[a],1)
      elif hit == 2:
        basejmp=40
      elif hit==3:
        basejmp=20
      stack[tank].append((hit-1)*random.choice([1,2])  )
      stack[tank].append(dist)
      ips[tank]+=basejmp+dist
      if ips[tank]>=DNAlens[tank]:
        ips[tank]=ips[tank]%DNAlens[tank]
    elif op[0]=="p" or op[0]=="6":
      #pop-to-next-opcode/operand
      # they also need jump by pop bite and push curpop size
      try:
        offs=stack[tank].pop()
      except:
        offs=1
      next=ips[tank]+offs
      if next>=DNAlens[tank]:
        next=next%DNAlens[tank]
      t=list(dnas[tank])
      try:
        newcod=stack[tank].pop()
      except:
        newcod=random.choice([3,4,5])
      if op[0]=="p":
        t[next*2]=["6","p","e","f","m","j","s"][newcod%7]
      else:
        t[(next*2)+1]=[">","^","<","v"][newcod%4]
      dnas[tank]=="".join(t)
    elif op[0]=="j":
      try:
        offs=stack[tank].pop()
      except:
        offs=0
      go(ucalpha[tank]+" jumps by stackpop "+str(offs)) #; print ", leavin "+str(len(stack[tank]))+"-byte stack "#for tank "+ucalpha[tank],1)
      ips[tank]+=offs
      if ips[tank]>=DNAlens[tank]:
        ips[tank]=ips[tank]%DNAlens[tank]
    elif op[0]=="s":
    # pop-size
      stack[tank].append(anyalive)
      go(ucalpha[tank]+" push pop size "+str(anyalive),1)
    elif op[0]=="m":
      if op[1]=="^":
        if ty[tank]>=1:
          ty[tank]-=1
        else:
          ty[tank]=rows-1
      elif op[1]=="<":
        if tx[tank]>=1:
          tx[tank]-=1
        else:
          tx[tank]=cols-1
      elif op[1]=="v":
        if ty[tank]<rows-1:
          ty[tank]+=1
        else: 
          ty[tank]=0
      elif op[1]==">":
        if tx[tank]<cols-1:
          tx[tank]+=1
        else:
          tx[tank]=0
      if map[ty[tank]][tx[tank]] == "~":
        guns[tank]+=1
        go("tank "+ucalpha[tank]+"  now has "+str(guns[tank])+" guns",rly=1)
    elif op[0]=="f":
# firing code
      go( "Tank "+ ucalpha[tank] +" shoot "+op[1])
      shake(guns[tank])
      #sleep(0.35)
      nmg=0
      for v in xrange(guns[tank]):
          if nmg == 1:
            continue
          nmg=0
          if op[1]=="^":
            xtr=0
            ytr=-1
          elif op[1]=="<":
            xtr=-1
            ytr=0
          elif op[1]=="v":
            xtr=0
            ytr=1
          elif op[1]==">":
            xtr=1
            ytr=0
          else:
            print "it shoots an unrecognized way, (" +op[1]+")!"
            #shouldn't happen
            #sleep(.5)
          shoty=ty[tank]
          shotx=tx[tank]
          hit = 0
          while hit == 0 and map[shoty][shotx] != "." and map[shoty][shotx] != "~":
            shoty += ytr
            if shoty < 0:
              shoty+=rows
            elif shoty >= rows:
              shoty -= rows
            shotx += xtr
            if shotx < 0:
              shotx+=cols
            elif shotx >= cols:
              shotx -= cols
            #then the shot is somewhere a tanck has been
            for a in xrange(tanks):
              if dead[a]>0:
                continue
              if tx[a] == shotx and ty[a] == shoty:
                go( "tank "+ ucalpha[tank]+ " KILLS enemy tank "+ucalpha[a]+"!!")
                shake(random.choice(range(5,17)))
                #sleep(3)
                dead[a]=1
                killers[a]=tank
                hit=1
                if tank==a:
                  nmg=1
          
          if hit == 0:
              #hit wall
            go ( "Tank "+ucalpha[tank]+" blew up some rock!")
            #sleep(0.15)
            t=list(map[shoty])
            t[shotx]= "*"
            map[shoty]="".join(t)
                 
    ips[tank]+=1
    if ips[tank]>=DNAlens[tank]:
      ips[tank]=0

      
      
 
