from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def dice(request):
    return render(request,'dice.html')
def possible_combination(request):
    total_combinations=36;
    dice_A=['1','2','3','4','5','6'];
    dice_B=['1','2','3','4','5','6'];
    totalCombinations=[];
    for i in range(len(dice_A)):
        for j in range(len(dice_B)):
            r=[dice_A[i],dice_B[j]];
            totalCombinations.append(r);
    s=""
    for i in totalCombinations:
        a="("
        for j in range(len(i)-1):
            a=a+i[j]+","
        a=a+i[len(i)-1]
        a=a+")"+" "
        s=s+a

    return render(request,'possible_combination.html',{'total':total_combinations,'Combinations':s})
def possible_distribution(request):
    dice_A=[1,2,3,4,5,6];
    dice_B=[1,2,3,4,5,6];
    distributions={};
    for i in range(len(dice_A)):
        for j in range(len(dice_B)):
            distributions[(dice_A[i]+dice_B[j])]=0;
    for i in range(len(dice_A)):
        for j in range(len(dice_B)):
            distributions[(dice_A[i]+dice_B[j])]+=1;
    #print("Distributions of all possible combinations on rolling the dice: ");
    q=[];
    for i in distributions:
        q.append(f"The total count of sum of {i} is {distributions[i]}");
    return render(request,'possible_distribution.html',{'distribution':q})
def possible_probability(request):
    dice_A=[1,2,3,4,5,6];
    dice_B=[1,2,3,4,5,6];
    distributions={};
    for i in range(len(dice_A)):
        for j in range(len(dice_B)):
            distributions[(dice_A[i]+dice_B[j])]=0;
    for i in range(len(dice_A)):
        for j in range(len(dice_B)):
            distributions[(dice_A[i]+dice_B[j])]+=1;
    r=[];
    for i in distributions:
        r.append(f"The probability of having a sum of {i} is {distributions[i]}/36 ({distributions[i]/36})");
    return render(request,'possible_probability.html',{'probability':r})
def doom_dice_challenge(request):
    if request.method=='POST' and request.POST['dice1'] !='' and request.POST['dice2'] !='':
        r,c=6,6 
        new_A=request.POST['dice1'];
        new_B=request.POST['dice2'];
        new_A=list(map(int,new_A.split(',')));
        new_B=list(map(int,new_B.split(',')));
        r,c=6,6 
        def pro(val1,val2):
            prob=[] 
            t=[]
            for i in range(r):
                for j in range(c):
                    t.append(val1[i]+val2[j])
            for i in range(2,13):
                prob.append(t.count(i))
            return prob
        def comb(lis,val):
            if val==0:
                return [[]]
            l=[]
            for i in range(0, len(lis)):
                m=lis[i]
                n=lis[i + 1:]
                r=comb(n, val-1)
                for p in r:
                    if [m,*p] not in l:
                        l.append([m, *p])
            return l
        pos_a=comb([int(i) for i in "111111222222333333444444"],6)
        pos_b=comb([j for j in range(1,12)],6)
        prob_org=pro([1,2,3,4,5,6],[1,2,3,4,5,6])
        for i in pos_a:
            a=i
            for b in pos_b:
                prob_pos=pro(a,b)
                if prob_pos==prob_org:
                    new_A=a
                    new_B=b
        new_dice_A="";
        new_dice_B="";
        for i in new_A:
            new_dice_A=new_dice_A+str(i)+" ";
        for i in new_B:
            new_dice_B=new_dice_B+str(i)+" ";
                    
        return render(request,'doom_dice_challenge.html',{'diceA':new_dice_A,'diceB':new_dice_B})
    else:
        return render(request,'dice.html')
