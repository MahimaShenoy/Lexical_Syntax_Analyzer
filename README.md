# Lexical_and_Syntax_Analyzer

#### Design a lexical and LR parser for the following code snippet:

```
int main()
begin
   int count=1;
   while(n>1)
   begin
      count=count+1;
      n=n/2;
   end while
 return count;
end 
```
#### The LR1 grammar is :
```
S' -> S

S -> datatype MAINFUNC

MAINFUNC -> MAIN begin NL STMTS end NL

MAIN -> main ( ) NL

STMTS -> STMT STMTS

STMTS -> STMT

STMT -> DECLARE SC NL

STMT -> EXPRESSION SC NL

STMT -> WHILESTMT

STMT -> RETURNSTMT SC NL

DECLARE -> datatype DECVARS

DECVARS -> DECVAR

DECVARS -> DECVAR comma DECVARS

DECVAR -> id

DECVAR -> id equalsto number

EXPRESSION -> id equalsto VARNUM

EXPRESSION -> id equalsto VARNUM operator VARNUM

VARNUM -> id

VARNUM -> number

WHILESTMT -> while ( id condition VARNUM ) WTSTMT

WTSTMT -> NL begin NL STMTS end while NL

RETURNSTMT -> return VARNUM
```
#### Terminals are :
```
a -> datatype

b -> begin

c -> NL

d -> end

e -> main

f -> (

g -> )

h -> SC

i -> comma

j -> id

k -> equalsto

l -> number

m -> operator

n -> while

o -> condition(>,<,>=,<=,==,!=)

p -> return
```
#### Non-Terminals are :
```
A -> MAINFUNC

B -> MAIN

C -> STMTS

D -> STMT

E -> DECLARE

F -> EXPRESSION

G -> WHILESTMT

H -> RETURNSTMT

I -> DECVARS

J -> DECVAR

K -> VARNUM

L -> WSTMT

```
#### New grammar is:
```
S' -> S

S -> a A

A -> B b c C d c

B -> e f g c

C -> D C

C -> D

D -> E h c

D -> F h c

D -> G

D -> H h c

E -> a I

I -> J

I -> J i I

J -> j

J -> j k l

F -> j k K

F -> j k K m K

K -> j

K -> l

G -> n f j o K g L

L -> c b c C d n c

H -> p K
```
#### String to be parsed:
```
a e f g c b c a j k l h c n f j o l g c b c j k j m l h c j k j m l h c d n c p j h c d c
```
