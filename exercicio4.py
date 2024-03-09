"""
4) Você está em uma sala com três interruptores, cada um conectado a uma lâmpada em uma sala diferente. 
Você não pode ver as lâmpadas da sala em que está, mas pode ligar e desligar os interruptores quantas vezes quiser. 
Seu objetivo é descobrir qual interruptor controla qual lâmpada.

Como você faria para descobrir, usando apenas duas idas até uma das salas das lâmpadas, qual interruptor controla cada lâmpada?

"""
# RESPOSTA
"""
Na primeira visita à sala das lâmpadas:

Ligue o primeiro interruptor por alguns minutos e, em seguida, desligue-o.
Ligue o segundo interruptor e mantenha-o ligado.
Deixe o terceiro interruptor desligado.
Depois disso, teremos as seguintes situações:

Se a lâmpada estiver acesa, sabemos que o segundo interruptor controla essa lâmpada.
Se a lâmpada estiver desligada, então:
Se a lâmpada estiver quente, o primeiro interruptor controla essa lâmpada.
Se a lâmpada estiver fria e apagada, o terceiro interruptor controla essa lâmpada.

"""
