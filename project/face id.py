import tkinter as toplevel
import random
x,y=400,400
class SnakeGame:
    voucher=0
    def __init__(self, master, width, height):
        self.master = master
        self.width = width
        self.height = height
        self.bgsnakenoi = toplevel.Canvas(master, width=x, height=y,bg="black")
        self.bgsnakenoi.pack()
        self.setup_game()
        self.master.bind('<KeyPress>', self.on_keypress)
        self.controlsnake = 'Right'
        self.score = 0
        self.score_label = toplevel.Label(master, text="Score: 0")
        self.score_label.pack()
        self.move()
    def setup_game(self):
        self.snake = [(20,20)]
        self.food = self.generate_food()
        self.draw_snake()
        self.draw_food()
    def generate_food(self):
        x = random.randint(0, 19 ) * 20
        y = random.randint(0, 19) * 20
        return (x, y)      
    def draw_snake(self):
        self.bgsnakenoi.delete('snake')
        for segment in self.snake:
            x, y = segment
            self.bgsnakenoi.create_rectangle(x, y, x + 20, y + 20, fill='blue', tags='snake')
    def draw_food(self):
        self.bgsnakenoi.delete('food')
        x, y = self.food
        self.bgsnakenoi.create_rectangle(x, y, x + 20, y + 20, fill='pink', tags='food')
    def move(self):
        head = self.snake[-1]
        if self.controlsnake == 'Up':
            new_head = (head[0], head[1] - 20)
        elif self.controlsnake == 'Down':
            new_head = (head[0], head[1] + 20)
        elif self.controlsnake == 'Left':
            new_head = (head[0] - 20, head[1])
        elif self.controlsnake == 'Right':
            new_head = (head[0] + 20, head[1])
        self.snake.append(new_head)
        if new_head == self.food:  
            self.food = self.generate_food()
            self.draw_food()
            self.score += 10
            self.update_score()
        else:
            self.snake.pop(0)
        self.draw_snake()
        self.check_collision()
        self.master.after(40, self.move)
    def check_collision(self):
        head = self.snake[-1]
        if head in self.snake[:-1] or head[0] < 0 or head[0] >= self.width or head[1] < 0 or head[1] >= self.height:
            print("Game Over")
            voucher=self.score
            print(voucher)
            self.master.destroy()
    def update_score(self):
        self.score_label.config(text="Score: {}".format(self.score))
    def on_keypress(self,cont):
        key = cont.keysym
        if (key == 'Up' and self.controlsnake != 'Down') or (key == 'Down' and self.controlsnake != 'Up') or (key == 'Left' and self.controlsnake != 'Right') or (key == 'Right' and self.controlsnake != 'Left'):
            self.controlsnake = key
snakegamegui = toplevel.Tk()
snakegamegui.title("Snake Game")
game = SnakeGame(snakegamegui, width=x,height=y)
snakegamegui.mainloop()
