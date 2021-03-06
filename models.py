import arcade.key

class Model:
    def __init__(self, world, x, y, angle):
        self.world = world
        self.x = x
        self.y = y
        self.angle = 0

class World:
    def __init__(self, width, height):
        self.width = width
        self.height = height
 
        self.ship = Ship(self, 100, 100)
        self.gold = Gold(self, 400, 400)

    def on_key_press(self, key, key_modifiers):
        if key == arcade.key.SPACE: #ถ้ากดspaceจะเรียกใช้switch_direction
            self.ship.switch_direction()
 
    def update(self, delta):
        self.ship.update(delta)

class Ship(Model): #สืบทอดสมบัติมาจากModel(มีคลาสแม่คือModel) คือที่โมเดลทำได้ Shipจะทำได้ เช่นในModelมีdef jump(): Shipจะjump()ได้เลย ไม่ต้องnew object
#เช่นjump()
    DIR_HORIZONTAL = 0
    DIR_VERTICAL = 1
    
    def __init__(self, world, x, y): 
        super().__init__(world, x, y, 0) #เอาคุณสมบัติของclassแม่มาหมด
 
        self.direction = Ship.DIR_VERTICAL
 
 
    def switch_direction(self):
        if self.direction == Ship.DIR_HORIZONTAL:
            self.direction = Ship.DIR_VERTICAL
            self.angle = 0
        else:
            self.direction = Ship.DIR_HORIZONTAL
            self.angle = -90
 
 
    def update(self, delta):
        if self.direction == Ship.DIR_VERTICAL:
            if self.y > self.world.height:
                self.y = 0
            self.y += 5
        else:
            if self.x > self.world.width:
                self.x = 0
            self.x += 5

class Gold(Model):
    def __init__(self, world, x, y):
        super().__init__(world, x, y, 0)