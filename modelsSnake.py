import arcade.key #นำปุ่มที่ได้รับมาใช้งานในนี้
DIR_UP = 1
DIR_RIGHT = 2
DIR_DOWN = 3
DIR_LEFT = 4
 
DIR_OFFSET = { DIR_UP: (0,1),#สร้างลิสtoople ว่ามี4ข้อมูล แต่ละข้อมูลมี2ข้อมูลย่อน
               DIR_RIGHT: (1,0),
               DIR_DOWN: (0,-1),
               DIR_LEFT: (-1,0) }
class Snake:
    MOVE_WAIT = 0.2 #เวลาที่ใหเรอเพื่อที่จะได้ขยับเป็นช่องๆ
    BLOCK_SIZE = 16 #ขนาดความยาวงู1ช่อง
    def __init__(self, world, x, y):
        self.world = world
        self.x = x
        self.y = y
        self.body = [(x,y),
                     (x-Snake.BLOCK_SIZE, y),
                     (x-2*Snake.BLOCK_SIZE, y)]
        self.length = 3 #ให้งูมีขนาด3ช่อง

        self.wait_time = 0 
        self.direction = DIR_DOWN #เริ่มต้นมาหันหน้าเคลื่อนที่ไปทางขวา
 
    def update(self, delta):
        self.wait_time += delta
 
        if self.wait_time < Snake.MOVE_WAIT: #ต้องรอจนถึงเวลาที่ตั้งไว้ถึงจะขยับได้อีกที
            return
 
        if self.x > self.world.width:
            self.x = 0
        if self.x < 0:
            self.x = self.world.width
        if self.y > self.world.height:
            self.y = 0
        if self.y < 0:
            self.y = self.world.height
        self.x += DIR_OFFSET[self.direction][0]*Snake.BLOCK_SIZE #จะให้ขยับแกนxตามทิศที่หันหน้าอยู่ เลยคูณกับตัวแรกของข้อมูลย่อยในขลิสDIR_OFFSET
        self.y += DIR_OFFSET[self.direction][1]*Snake.BLOCK_SIZE
        self.wait_time = 0 #รีเวลารอเพื่อขยับใหม่
 
class World:
    def __init__(self, width, height):
        self.width = width
        self.height = height
 
        self.snake = Snake(self, width // 2, height // 2)
 
    def on_key_press(self, key, key_modifiers):
        if key == arcade.key.LEFT: #ถ้ากดLEFTจะเปลี่ยนdirectionของงู
            self.snake.direction = DIR_LEFT
        if key == arcade.key.RIGHT: #ถ้ากดRIGHTจะเปลี่ยนdirectionของงู
            self.snake.direction = DIR_RIGHT
        if key == arcade.key.UP:
            self.snake.direction = DIR_UP
        if key == arcade.key.DOWN:
            self.snake.direction = DIR_DOWN
 
    def update(self, delta):
        self.snake.update(delta)