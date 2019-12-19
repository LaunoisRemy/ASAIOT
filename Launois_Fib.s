.data
i: .word 2
F:      .skip 400
        .balign 8
m: .asciz "%d\n"
.text
.global main
main:
        ldr r0, =i //contient l'adresse de i
        ldr r5, [r0] //contient la v de i
        ldr r1, =F 
        mov r7, #0
        str r7, [r1,#0] 
        mov r7, #1
        str r7, [r1,#8] 
        mov r3, #0 
	//Iterateur
        mov r11, #0
boucle:
        cmp r5,#30 //Boucl itératif jusqua 30
        beq affichage 

fib:
        mov r6, #0 
       	ldr r1, =F
        ldr r8, [r1,r3]
        add r6, r8 
        mov r9, r3
        sub r9, #8
        ldr r8, [r1,r9] 
        add r6, r8 
        mov r2, r6
        mov r4, #8 
        mul r3,r4,r5 
        str r2, [r1,r3] 
        add r5, #1 //i++
        b boucle

affichage:
	cmp r11, #30
        beq fin
        ldr r0,=m
        mov r5, #8
        mul r6, r11, r5
        ldr r1, =F
        ldr r1, [r1,r6]
        add r11, #1
        bl printf
        bl affichage

fin:
        bl exit	
