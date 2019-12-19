	.data
return: .word	0
enter:	.asciz "Entrer n : "
scan:	.asciz "%d"
msg:	.asciz "somme des n = %d \n"

	.text
	.global main
	
fib:
	cmp r0, #1
	ble fin 		//si n < 1 on retourne n 
	mov r3,#1  	//[r3]=i
	mov r1,#1	//[r1]=a
	mov r2,#1	//[r2]=b
for:				//for i in (1,..,n) (a,b) -> (b,a+b) avec a=1 et b=1
	cmp r3,r0
	beq fin
	mov r4,r2
	add r2,r1
	mov r1,r4
	add r3,#1
	bl for
	


main:
	ldr r0, =enter	//on affiche le message pour inviter l'utilisateur a rentree une valeur
	bl printf
	ldr r0, =scan
	ldr r1, =return
	bl scanf
	ldr r1, =return
	ldr r2, [r1]	
	mov r0,r2	//on stock dans r0 la valeur entree dans le scanf
	bl fib


fin:
	mov r1,r2
	ldr r0,=msg		//on affiche le resultat 
	bl printf
	bl exit
	