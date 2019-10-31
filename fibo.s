.data		
.text		
.global main	
main:

	// on appelle fibo(50)
	mov r0, #50
	bl fibo
	
	bl exit	
	
fibo :
	sub sp, sp, #8 // on deplace le pointeur de pile
	str lr, [sp] // on enregistre l'adresse de retour dans la pile

	cmp r0, #1
	ble fibo0

	sub sp, sp, #8 // On alloue la memoire dans la pile
	str r0, [sp] // on empile r0

	sub r1,r0, #1 // r0 - 1
	bl fibo

	mov r5,r1 //res de fibo(n-1)
	
	sub r1,r0,#2
	bl fibo

	mov r6,r1 //res de fibo(n-2)

	add r0, r5, r6 //fibo(n-1)+fibo(n-2)
	
endf:
	ldr r1, [sp]
	add sp, sp, #8
	ldr lr, [sp]
	add sp, sp, #8
	bx lr
	
fibo0 :
	mov r0, #1
	sub sp, sp, #8
	str r0, [sp]
	b endf
