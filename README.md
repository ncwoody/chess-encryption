# chess
I am making a proof of concept of a way to send binary data over a chess correspondence conversation.
The encryption function is written in python using the python chess library.
The decryption function is currently written in c, but I may have to rewrite it, so I'll probaby stick to python for it for continuity.
Essentially each move will send one binary digit, so you can send relevant information, it would just take a very very long time.
Right now this is just a proof of concept, but if I am board enough or if this somehow gets enough attention I may make a full-blown app out of this.
Born out of my interest in sending data over normal forms of communication and in using binary digits for data exfiltration.
