# ChessInfinity
My competitor to AlphaZero

## Algo
```
0. Every historical game represented as two vectors:
0.1 For long-term memory it's some structure to match the same game, and check who won in this position
0.2 For short-term memory it's some structure to match similar positions, 
and check which moves did not leaded to loss of figures
1. Every figure has two types of memory - short-term and long-term
2. Every figure can propose move to king
3. King has biggest long-term memory???, and can make some random moves
4. Every figure process future moves in parallel
5. King is OK about DRAW, but he is not OK about CHECKMATE to himself
6. Every other figure is ok about DRAW or CHECKMATE, if it doesn't sacrafice itself
7. King doesn't know how much memory each figure has
8. On each move, each figure propose move to king
9. King try to check each variant in parallel, at this time other figures doesn't think at all
10. If King didn't find exact match in long-term memory, he uses short-term memory to generate new moves
11. He does that until time is not lesser then opponent time
12. If King didn't find match even in short term memory, but time is equal or less then opponent time, 
he proposes draw, and wait for answer from opponent king 
13. If opponent King didn't agreed, King make some random move (max score in short-term memory)
```
