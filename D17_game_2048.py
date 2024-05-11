import numpy as np
import random

#creating the main class
class Game_2048():
    #creating board object by calling Play()
    def __init__(self):
        self.row=4
        self.col=4
        self.board= np.zeros(shape=(self.row,self.col),dtype=np.int64) # 4 X 4 numpy zero matrix
        self.new_row= random.randint(0,3)  # choosing a random row and col for placing new 2
        self.new_col= random.randint(0,3)
        self.board[(self.new_row, self.new_col)]=2

   
    

    #defining play button class
    def play(self):
        not_empty= Operations(self.board).check()
        if not_empty:
            return f"******GAME OVER******"
        
        while True:
            mode= input("Enter move( r/l/u/d) or q to quit : ").lower()
            if mode =="q":
                quit()
            elif mode=="r":
                Operations(self.board).right()
                self.print()
            elif mode=="l":
                Operations(self.board).left()
                self.print()
            elif mode=="u":
                Operations(self.board).up()
                self.print()
            elif mode=="d":
                Operations(self.board).down()
                self.print()
            else:
                print("Enter a valid mode.")

    def print(self):
       
        # Find the maximum digit length in the matrix 
        max_digit_length = 5

        # Calculate the maximum width for each column
        max_widths = np.max(np.floor(np.log10(np.abs(self.board))) + 1, axis=0).astype(int)

        # Adjust the width of each column to ensure a minimum width of max_digit_length
        max_widths = np.maximum(max_widths, max_digit_length)

        # Align the matrix
        aligned_matrix = np.array([[f"{item:>{width}}" for item, width in zip(row, max_widths)] for row in self.board])

        # Print aligned matrix
        for row in aligned_matrix:
            print("-"* 32)
            print(f'|{" | ".join(row)} |')
            
        print("-"* 32)
        
    
# creating the logical operations
class Operations():
    #Operations() will take a matrix as input and perform its operations
    def __init__(self, matrix):
        self.matrix= matrix
        self.row, self.col = np.shape(matrix)

    #dealing with empty spaces
    '''eg: [2 0 0 0]-> [0 0 0 2]; [2 0 4 0]-> [0 0 2 4]'''

    def shift_right(self, row):
        i=3
        while i!=0:
            if row[i]==0:
                for j in range(1,i+1):
                    if row[i-j]!=0:
                        row[i]=row[i-j]
                        row[i-j]=0
                        break
            else: 
                i-=1 
                continue    
            i-=1
        return row
    # adding same numbers and placing it to right side
    '''eg: [0 0 4 4]->[0 0 0 8]'''

    def right(self):
        for row in range(0,4):
            self.matrix[row]= self.shift_right(self.matrix[row])
            for col in range(0,3):
                if self.matrix[row][3-col]==self.matrix[row][3-(col+1)]:
                    self.matrix[row][3-col]=self.matrix[row][3-col]+self.matrix[row][3-(col+1)]
                    self.matrix[row][3-(col+1)]=0
                    col= col+1
                else:
                    pass

                if self.matrix[row][3-col]==16:
                    print("CONGRATES . YOU WON")
                    quit()
        
            self.matrix[row]= self.shift_right(self.matrix[row])
        
        #generate a 2 after the operation
        flag= True
        while flag:
            i=random.randint(0,3)
            j=random.randint(0,3)
            if self.matrix[i][j]==0:
                self.matrix[i][j]=2
                flag= False

        return self.matrix
    


    #dealing with empty spaces
    def shift_left(self, row):
        i=0
        while i!=3:
            if row[i]==0:
                for j in range(i+1,4):
                    if row[j]!=0:
                        row[i]=row[j]
                        row[j]=0
                        break
            else: 
                i+=1 
                continue    
            i+=1
        return row

    def left(self):
        for row in range(0,4):
            self.matrix[row]= self.shift_left(self.matrix[row])
            for col in range(0,3):
                if self.matrix[row][col]==self.matrix[row][col+1]:
                    self.matrix[row][col]=self.matrix[row][col]+self.matrix[row][col+1]
                    self.matrix[row][col+1]=0
                    col= col+1
                else:
                    pass
                
                if self.matrix[row][col]==16:
                    print("CONGRATES . YOU WON")
                    quit()
                    
            self.matrix[row]= self.shift_left(self.matrix[row])
        
        #generate a 2 after the operation
        flag= True
        while flag:
            i=random.randint(0,3)
            j=random.randint(0,3)
            if self.matrix[i][j]==0:
                self.matrix[i][j]=2
                flag= False
                

        return self.matrix
    # up operation is nothing but Transpose + Left + Transpose
    def up(self):
        self.matrix= np.transpose(self.matrix)
        self.matrix= self.left()
        self.matrix= np.transpose(self.matrix)
        return self.matrix
    
    def down(self):
        self.matrix= np.transpose(self.matrix)
        self.matrix= self.right()
        self.matrix= np.transpose(self.matrix)
        return self.matrix

    #checking if there is empty space or not to place a 2
    def check(self):
        return np.all(self.matrix)


#Play the game
game= Game_2048()
game.print() #prints the initial board
game.play()

