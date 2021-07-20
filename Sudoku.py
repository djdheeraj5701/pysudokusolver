from tkinter import *

def columnChecker(arr,column,i):
    for j in range(9):
        if i==arr[j][column]:
            return False
    return True

def blockChecker(arr,row,column,element):
    for i in range((row//3)*3,(row//3+1)*3):
        for j in range((column//3)*3,(column//3+1)*3):
            if element==arr[i][j]:
                return False
    return True

def Solved(arr):
    for i in range(9):
        for j in range(9):
            Label(f3, text=arr[i][j], font=("Bold", 20), bg="light green", width=2).grid(row=i, column=j)

def sudokuSolver(arr,row,column):
    if column == len(arr):
        row += 1
        column = 0
    if row == len(arr):
        Solved(arr)
        return True

    if arr[row][column] != 0:
        return sudokuSolver(arr, row, column + 1)

    toChoose=list()
    for i in range(1,10):
        if i not in arr[row]:
            if columnChecker(arr,column,i) and blockChecker(arr,row,column,i):
                toChoose.append(i)

    for i in toChoose:
        arr[row][column]=i
        if sudokuSolver(arr,row,column+1):
            return True
    arr[row][column]=0
    return False

def EmptyGrid(gridEntry):
    for i in range(9):
        for j in range(9):
            gridEntry.append(Entry(f1, font=("Bold", 20), width=2))
            gridEntry[-1].grid(row=i, column=j)

def EntriesGrid(gridEntry,arr):
    for i in range(9):
        x=[]
        for j in range(9):
            y=gridEntry[9*i+j].get()
            gridEntry[9*i+j].delete(0, len(gridEntry[9*i+j].get()))
            if y=="":
                y=0
            x.append(int(y))
        arr.append(x)
    sudokuSolver(arr, 0, 0)

root=Tk(className='Play Sudoku')
root.minsize(800,500)

f1=Frame(root)
f1.grid(row=0,column=0)

f2=Frame(root)
f2.grid(row=1,column=1)

f3=Frame(root)
f3.grid(row=0,column=2)

gridEntry=[]
Button(f2,text="Empty Sudoku",bg="pink",width=10,command=lambda:EmptyGrid(gridEntry)).grid(row=0,column=0)
Button(f2,text="Solve Sudoku",bg="pink",width=10,command=lambda:EntriesGrid(gridEntry,[])).grid(row=1,column=0)

root.mainloop()

'''
[1, 2, 3, 4, 5, 6, 7, 8, 9], 
[4, 5, 6, 7, 8, 9, 1, 2, 3], 
[7, 8, 9, 1, 2, 3, 4, 5, 6], 
[2, 1, 4, 3, 6, 5, 8, 9, 7], 
[3, 6, 5, 8, 9, 7, 2, 1, 4], 
[8, 9, 7, 2, 1, 4, 3, 6, 5], 
[5, 3, 1, 6, 4, 2, 9, 7, 8], 
[6, 4, 2, 9, 7, 8, 5, 3, 1], 
[9, 7, 8, 5, 3, 1, 6, 4, 2]
'''