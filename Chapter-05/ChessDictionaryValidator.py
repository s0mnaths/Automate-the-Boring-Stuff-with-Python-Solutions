def isValidChessBoard(aDict):
    ans=1
    numOfWKing=0
    numOfBKing=0
    numOfB=0
    numOfW=0
    numOfWPawn=0
    numOfBPawn=0
    for position,cPiece in aDict.items():
        posLetters=['a','b','c','d','e','f','g','h']
        posNumbers=['1','2','3','4','5','6','7','8']
        pieceColor=['w','b']
        pieceRank=['king','queen','bishop','knight','rook','pawn']
        strRank=cPiece[1:]

        if (position[0] not in posNumbers or \
            position[1] not in posLetters or \
            cPiece[0] not in pieceColor or \
            strRank not in pieceRank ):
            ans=0
            break
        if cPiece[0]=='w':
            numOfW+=1
            if strRank=='king':
                numOfWKing+=1
            elif strRank=='pawn':
                numOfWPawn+=1
        
        else:
            numOfB+=1
            if strRank=='king':
                numOfBKing+=1
            elif strRank=='pawn':
                numOfBPawn+=1
        
    if(numOfB>16 or numOfW>16 or numOfWPawn>8 or numOfBPawn>8 or numOfWKing!=1 or numOfBKing!=1):
        ans=0

    #print(ans)
    if ans==0:
        return False
    else:
        return True
                

'''theBoard={'1a': 'bking', '1b': 'bqueen', '1c': 'bbishop', '1d': 'bknight', '1e': 'brook', '1f': 'bbishop', '1g': 'bknight', '1h': 'brook', \
          '2a': 'bpawn', '2b': 'bpawn', '2c': 'bpawn', '2d': 'bpawn', '2e': 'bpawn', '2f': 'bpawn', '2g': 'bpawn', '2h': 'bpawn', '3a': 'wking'}
print(isValidChessBoard(theBoard))'''