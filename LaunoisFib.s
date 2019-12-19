.data
i: .word 2
F:      .skip 400
        .balign 8
msg: .asciz "%d\n"
val: .word 1
.text

.global main

//r1 contient le tableau
//r2 contient la valeur a mettre dans le tableau
//r4 contient l'increment de l'offset
//r3 contient l'emplacement dans le tableau
//r6 contient la valeur de fibo(n-1)+fibo(n-2)
//r7 contient les valeurs de fibo(0) et ensuite de fibo(1)
//r8 contient l'emplacement dans le tableau de fibo(n-1) et fibo(n-2)
//r9 contient fibo (n-1)
main:
        ldr r5, =i //r5 = i
        ldr r0, [r5]//r0 = i
        ldr r1, =F //on stocke le tableau
        mov r7, #0
        str r7, [r1,#0]
        ldr r7, =val
        ldr r7, [r7]
        str r7, [r1,#8]
        mov r3, #0
        mov r11, #0 compteur pour le tableau

boucle:
        cmp r0,#50 //on verifie si l'increment est supérieure à 50
        bgt printTab //dans ce cas on quitte le prog

fib:


        mov r6, #0 //on initialise la valeur de fibo(n)
        ldr r1, =F
        ldr r9, [r1,r3] //on recupere fibo(n-1)
        add r6, r9 //fibo(n)=fibo(n-1)
        mov r8, r3
        sub r8, #8
        ldr r9, [r1,r8] //on recupere fibo(n-2)
        add r6, r9 //fibo(n)=fibo(n-2)+fibo(n-1)
        mov r2, r6

        mov r4, #8 //on gere l'offset
        mul r3,r4,r0 //on calcul l'endroit où mettre fibo(n)
        str r2, [r1,r3] //on place fibo(n)
        add r0, #1 //on incremente
        b boucle

printTab:
        cmp r11, #50
        bgt fin
        ldr r5,=msg
        mov r0, #8
        mul r6, r11, r0
        ldr r1, =F
        ldr r1, [r1,r6]
        add r11, #1
        bl printf
        bl printTab

fin:
        bl exit	
