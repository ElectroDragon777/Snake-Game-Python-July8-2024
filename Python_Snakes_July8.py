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
clock = PythonSnakes.time.Clock()
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
        self.Direction = "RIGHT"
    
    def Move(self):
        Snake_Head = self.Body[0]
        SH_X, SH_Y = Snake_Head

        if self.Direction == "UP":
            SH_Y -= Grid_Size
        elif self.Direction == "DOWN":
            SH_Y += Grid_Size
        elif self.Direction == "RIGHT":
            SH_X += Grid_Size
        elif self.Direction == "LEFT":
            SH_X -= Grid_Size

        self.Body.insert(0, (SH_X, SH_Y))

        if len(self.Body) > self.Size:
            self.Body.pop()
    
    # Direction Changes
    def Direction_Change(self, New_Direction):
        if New_Direction in ("UP", "DOWN", "RIGHT", "LEFT"):
            # Complex IF - Disallow Opposite direction movement
            if (New_Direction == "UP" and self.Direction != "DOWN") or (New_Direction == "DOWN" and self.Direction != "UP") or (New_Direction == "RIGHT" and self.Direction != "LEFT") or (New_Direction == "LEFT" and self.Direction != "RIGHT"): 
                self.Direction = New_Direction
    
    # Score increase (by eating the apples, or just the food in general :3 )
    def Food_Collision(self):
        self.Size += 1
    
    # Collision. If you collide with any side of the window, you die. If you die. you die. F to pay respect if you die, and if no death happens, congratulations! :D
    def Collision_Check(self):
        Snake_Head = self.Body[0]
        if Snake_Head[0] < 0 or Snake_Head[0] >= Width or Snake_Head[1] < 0 or Snake_Head[1] >= Width:
            return True
        if Snake_Head in self.Body[0]:
            return True
        return False
    
    # Draw the snake. Or you will be invisible. Hard mode possibility?
    def Draw_Snake(self):
        for SH_X, SH_Y in self.Body:
            rect = PythonSnakes.Rect(SH_X, SH_Y, Grid_Size, Grid_Size)
            PythonSnakes.draw.rect(Game_Window, Green, rect)
# Apple / Food:
class Food:
    def __init__(self):
        self.Position = self.Generate_Placement_X_Y()
    def Generate_Placement_X_Y(self):
        Food_X = Random.randint(0, Grid_Width - 1) * Grid_Size
        Food_Y = Random.randint(0, Grid_Width - 1) * Grid_Size
        return Food_X, Food_Y
    
    def Draw_Food(self):
        PythonSnakes.draw.rect(Game_Window, Red, (self.Position[0], self.Position[1], Grid_Size, Grid_Size))

# Class callings:
Window_Snake = Snake()
Window_Food = Food()

Game_Running = True
Game_Clock = PythonSnakes.time.Clock()
Game_Over = False

# Game is running. Now play the game.
Game_Window.fill(Black)
while Game_Running:
    # Register input.
    for Event_Executed in PythonSnakes.event.get():
        if Event_Executed.type == PythonSnakes.KEYDOWN:
            if Event_Executed.key == "UP":
                    Snake.Direction_Change("UP")
            elif Event_Executed.key == "DOWN":
                    Snake.Direction_Change("DOWN")
            elif Event_Executed.key == "LEFT":
                    Snake.Direction_Change("LEFT")
            elif Event_Executed.key == "RIGHT":
                    Snake.Direction_Change("RIGHT")

    # Game over check. If no, snake moves. 
    if not Game_Over:
        Window_Snake.Move()
        
        # Food consumption.
        if Window_Snake.Body[0] == Window_Food.Position:
            Window_Snake.Food_Collision()
            Window_Food.Position = Window_Food.Generate_Placement_X_Y()
            Score += 1
            
        if Window_Snake.Collision_Check():
            Game_Over = True
    
    Window_Snake.Draw_Snake()
    Window_Food.Draw_Food()
    Game_Clock.tick(FPS)
    PythonSnakes.display.flip()
    Score_Text = Font.render(f"Score: {Score}", True, White)
    Game_Window.blit(Score_Text, (10, 10))
    
    if Game_Over:
        Game_Over_Text = Font.render("Game Over", True, White)
        Game_Over_Rectangle = Game_Over_Text.get_rect(center = (Width//2, Height//2))
        Game_Window.blit(Game_Over_Text, Game_Over_Rectangle)
        Game_Running = False
        
    PythonSnakes.display.update()
