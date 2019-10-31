.data
i: .word 2
a:      .skip 400
        .balign 8
msg: .asciz "%d\n"
val: .word 1
.text

.global main
//r0 contient l'adresse de i
//r1 contient le tableau
//r2 contient la valeur a mettre dans le tableau
//r3 contient l'increment de l'offset
//r4 contient l'emplacement dans le tableau
//r5 contient la valeur de i
//r6 contient la valeur de fibo(n-1)+fibo(n-2)
//r7 contient les valeurs de fibo(0) et ensuite de fibo(1)
//r8 contient l'emplacement dans le tableau de fibo(n-1) et fibo(n-2)
//r9 contient fibo (n-1)
main:
        ldr r0, =i //on stocke l'increment
        ldr r5, [r0]
        ldr r1, =a //on stocke le tableau

        mov r7, #0
        str r7, [r1,#0] //on definit fibo(0)=0

        ldr r7, =val
        ldr r7, [r7]
        str r7, [r1,#8] //on definit fibo(1)=1

        mov r4, #0 //on definit l'emplacement memoire du tableau à 0
        mov r10, #0
loop:
        cmp r5,#50 //on verifie si l'increment est supérieure à 50
        bgt aff //dans ce cas on quitte le prog

fib:


        mov r6, #0 //on initialise la valeur de fibo(n)
       ldr r1, =a
        ldr r9, [r1,r4] //on recupere fibo(n-1)
        add r6, r9 //fibo(n)=fibo(n-1)
        mov r8, r4
        sub r8, #8
        ldr r9, [r1,r8] //on recupere fibo(n-2)
        add r6, r9 //fibo(n)=fibo(n-2)+fibo(n-1)
        mov r2, r6

        mov r3, #8 //on gere l'offset
        mul r4,r3,r5 //on calcul l'endroit où mettre fibo(n)
        str r2, [r1,r4] //on place fibo(n)

        //ldr r0,=msg //on affiche
        //ldr r1, [r1,r4]
        //bl printf

        add r5, #1 //on incremente
        b loop

aff:
cmp r10, #50
        bgt fin
        ldr r0,=msg
        mov r5, #8
        mul r6, r10, r5
        ldr r1, =a
        ldr r1, [r1,r6]
        add r10, #1
        bl printf
        bl aff

fin:
        //ldr r0, =msg
        //ldr r1, [r1,r4]
        //bl printf
        bl exit	
