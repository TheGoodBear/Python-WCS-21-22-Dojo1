"""
    Randomly draw all persons from a list
    and animate between lists
    Original list : alphabetically sorter
    Drawn list : order or drawing sorted
"""
# coding: utf-8

# imports
import random
import os
import time

# variables and constants
Persons = [
    "Timothée",
    "Gaël",
    "David",
    "Quentin",
    "Théo",
    "Nicolas",
    "Jojo",
    "Jordan",
    "Adrien",
    "Cécilia"]
SelectedPersons = []

# tables
Table1X = 5
Table1Y = 1
Table2X = Table1X + 40
Table2Y = Table1Y
TablePadding = 1
TableInnerWidth = 12

# special characters
UL = "╔"
UR = "╗"
BL = "╚"
BR = "╝"
HBor = "═"
VBor = "║"
HSep = "─"

# rich console
FormatPrefix = "\033["
ForegroundPrefix = "3"
BackgroundPrefix = "4"
StyleAndColorReset = "0m"
StyleAndColorSuffix = "m"
PositionSuffix = "H"
CursorVisible = "?25h"
CursorInvisible = "?25l"
WhiteOnBlack = "0"
BlackOnYellow = "30;43"


# functions
def main():
    """
        Randomly draw all persons from a list
    """

    # clear console
    os.system("cls")

    # draw board
    # print("     Tirage des participants")
    DrawTable(Table1X, Table1Y, TableInnerWidth, len(Persons))
    DrawTable(Table2X, Table2Y, TableInnerWidth, len(Persons))

    # print list of Persons (sorted)
    Persons.sort()
    OriginalList = list(Persons)
    for Index in range(len(Persons)):
        PrintAt(
            Table1Y + 1 + (Index * 2),
            Table1X + 2,
            Persons[Index])

    # randomly select each person and put it in second list    
    for Index in range(1, len(Persons) + 1):
        time.sleep(1)
        PersonIndex = random.randint(0, len(Persons) - 1)
        Person = Persons.pop(PersonIndex)
        SelectedPersons.append(f"{len(SelectedPersons) + 1} - {Person}")
        MovePerson(OriginalList.index(Person), len(SelectedPersons))

    # end
    print("\nTerminé...\n")


def DrawTable(
    StartX = 1,
    StartY = 1,
    Width = 30,
    Height = 10,
    Padding = 1,
    SeparatorLines = True):
    """
        Width and Height = inner (content excluding padding)
        Padding = horizontal blank spaces before and after content
    """

    EndX = StartX + Width + 2 + Padding * 2
    EndY = StartY + Height + 1
    if SeparatorLines:
        EndY += Height - 1

    for Y in range(StartY, EndY + 1):
        for X in range(StartX, EndX + 1):
            Character = " "
            if (Y == StartY and X == StartX):
                Character = UL
            elif (Y == StartY and X == EndX):
                Character = UR
            elif (Y == EndY and X == StartX):
                Character = BL
            elif (Y == EndY and X == EndX):
                Character = BR
            elif (Y == StartY or Y == EndY):
                Character = HBor
            elif (X == StartX or X == EndX):
                Character = VBor
            elif SeparatorLines and (Y - StartY) % 2 == 0:
                Character = HSep

            print(f"{FormatPrefix}{Y};{X}{PositionSuffix}{Character}", end="")


def MovePerson(
    StartLine,
    EndLine):
    """
    """

    StartY = Table1Y + 1 + (StartLine * 2)
    EndY = Table2Y + 1 + ((EndLine - 1) * 2)
    StartX = Table1X + 2
    EndX = Table2X + 2
    MiddleX = StartX + ((EndX - StartX) // 2)
    DoorTable1X = StartX + TableInnerWidth + TablePadding * 2
    DoorTable2X = EndX - TablePadding * 2
    Text = SelectedPersons[EndLine-1]

    # PrintAt(StartY, StartX, " " * TableInnerWidth)

    # open door 1
    PrintAt(StartY, DoorTable1X , " ")

    # move name to middle X
    MoveText(Text, StartX, StartY, MiddleX)

    # close door 1
    PrintAt(StartY, DoorTable1X , VBor)

    # move name to new Y
    MoveText(Text, MiddleX, StartY, EndY = EndY)

    # open door 2
    PrintAt(EndY, DoorTable2X, " ")

    # move name to table 2
    MoveText(Text, MiddleX, EndY, EndX)

    # close door 2
    PrintAt(EndY, DoorTable2X, VBor)

    # Move(StepLine, StepColumn)

    PrintAt(EndY, EndX, SelectedPersons[EndLine-1], BlackOnYellow)


def PrintAt(Y, X, Text, Color = WhiteOnBlack):
    """
    """
    print(f"{FormatPrefix}{Y};{X}{PositionSuffix}{FormatPrefix}{Color}{StyleAndColorSuffix}{Text}{FormatPrefix}{WhiteOnBlack}{StyleAndColorSuffix}")


def MoveText(
    Text,
    StartX,
    StartY,
    EndX = None,
    EndY = None,
    Speed = 0.01):
    """
    """

    Step = 1

    if EndX:
        for X in range(StartX, EndX + 1):
            time.sleep(Speed)
            PrintAt(StartY, X, Text)
            PrintAt(StartY, X - 1, " ")
    elif EndY :
        if EndY < StartY:
            Step = -1
        for Y in range(StartY, EndY + Step, Step):
            time.sleep(Speed)
            PrintAt(Y, StartX, Text)
            PrintAt(Y - Step, StartX, " " * TableInnerWidth)



# code starts here
if __name__ == "__main__":
    main()
