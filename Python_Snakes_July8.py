# All imports I will need for this.
from lib2to3 import pygram
import pygame as PythonSnakes
import random as Random

# Game Initialisation
PythonSnakes.init()

# Game properties
Width = 640
Height = 480

Grid_Size = 20
Grid_Width = Width
Grid_Height = Height

FPS = 10

Black = (0, 0, 0)
White = (255, 255, 255)
Red = (255, 0, 0)
Green = (0, 255, 0)

Score = 0
Best_Score = 0
# Window
Game_Window = PythonSnakes.display.set_mode((Width, Height))
PythonSnakes.display.set_caption("Snakes Game - v.1.0a")

Font = PythonSnakes.font.Font(None,36)

# Game - Step 1: Snake
class Snake:
    def __init__(self):
        # Defaults of the snake
        self.Size = 1
        self.Body = [(Width//2, Height//2)]
        # Default starting to right direction
        self.Direction = "Right"
    
    def Move(self): # Snake movement.
        Snake_Head = self.Body[0]
        SH_X,SH_Y = Snake_Head
        
        # Directions - depending on direction, x or y change.
        match self.Direction:
            case "Up":
                SH_Y -= Grid_Size
            case "Down":
                SH_Y += Grid_Size
            case "Right":
                SH_X += Grid_Size
            case "Left":
                SH_X -= Grid_Size
        
        """ if self.Direction == "Up":
            SH_Y += Grid_Size
        elif self. """
        
        self.Body.insert(0, (SH_X,SH_Y))
        
        if len(self.Body) > self.Size:
            self.Body.pop()
    
    # Direction Changes
    def Direction_Change(self, New_Direction):
        if New_Direction in ("Up", "Down", "Right", "Left"):
            # Complex IF - Disallow Opposite direction movement
            if (New_Direction == "Up" and self.Direction != "Down") or (New_Direction == "Down" and self.Direction != "Up") or (New_Direction == "Right" and self.Direction != "Left") or (New_Direction == "Left" and self.Direction != "Right"): 
                self.Direction = New_Direction
    
    # Score increase (by eating the apples, or just the food in general :3 )
    def Food_Collision(self):
        self.Size += 1
    
    # Collision. If you collide with any side of the window, you die. If you die. you die. F to pay respect if you die, and if no death happens, congratulations! :D
    def Collision_Check(self):
        Snake_Head = self.Body[0]
        if Snake_Head[0] < 0 or Snake_Head[0] >= Width or Snake_Head[1] < 0 or Snake_Head[1] >= Width:
            return True
        if Snake_Head in self.Body[1]:
            return True
        return False
    
    # Draw the snake. Or you will be invisible. Hard mode possibility?
    def Draw_Snake(self):
        for SH_X, SH_Y in self.Body:
            PythonSnakes.Draw.Rect(Game_Window, Green, Grid_Size, Grid_Size)

# Apple / Food:
class Food:
    def __init__(self):
        self.Position = self.Generate_Placement_X_Y()
    def Generate_Placement_X_Y(self):
        Food_X = Random.randint(0, Grid_Width - 1) * Grid_Size
        Food_Y = Random.randint(0, Grid_Width - 1) * Grid_Size
        return Food_X, Food_Y
    
    def Draw_Food(self):
        PythonSnakes.Draw.Rect(Game_Window, RED, (self.Position[0], self.Position[1], Grid_Size, Grid_Size))

# Class callings:
Window_Snake = Snake()
Window_Food = Food()

Game_Running = True
Game_Clock = PythonSnakes.time.Clock()
Game_Over = False

# Game is running. Now play the game.
while Game_Running:
    # Register input.
    for Event_Executed in PythonSnakes.event.get():
        if Event_Executed.type == PythonSnakes.quit():
            Game_Running = False
        elif Event_Executed.type == PythonSnakes.KEYDOWN:
            match Event_Executed.Key:
                case "Up":
                    Snake.Direction_Change("Up")
                case "Down":
                    Snake.Direction_Change("Down")
                case "Left":
                    Snake.Direction_Change("Left")
                case "Right":
                    Snake.Direction_Change("Right")

    # Game over check. If no, snake moves. 
    if not Game_Over:
        Snake.Move(self=Snake)
        
        # Food consumption.
        if Snake.Body[0] == Food.Position:
            Snake.Food_Collision()
            Food.Position = Food.Generate_Placement_X_Y()
            Score += 1
            
        if Snake.Collision_Check():
            Game_Over = True
        
    Game_Window.Fill(Black)
    
    Snake.Draw_Snake()
    Food.Draw_Food()
    
    Score_Text = Font.Render(f"Score: {Score}", True, White)
    Game_Window.Blit(Score_Text, (10, 10))
    
    if Game_Over:
        Game_Over_Text = Font.Render("Game Over", True, White)
        Game_Over_Rectangle = Game_Over_Text.Get_Rect(center = (Width//2, Height//2))
        Game_Window.Blit(Game_Over_Text, Game_Over_Rectangle)
        
    PythonSnakes.Display.Update()
    Clock.tick(FPS)