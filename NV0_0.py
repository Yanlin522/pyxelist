""" v info v """"""
Name: pyxelist
version: TNPVo.0
"""""" ^ info ^ """

""" v imports v """
import turtle
""" ^ imports ^ """

""" v setup v """
# Nothing yet
""" ^ setup ^ """

""" v README v """"""
Object creation:
> example starting: Art = [['#======','#000000'],['#000000','#======']]
> example object: thing = pyxel(0,0,Art,5,type='solid',width='auto',height='auto')
> positioning: the first two reaspond to `xpos` and `ypos` the x and y of the shape
> drawing and size of drawing: the `Art,5,` part is the drawing and the scale of which it should be drawn
> drawing type: type is either 'solid' or 'animated', selecting animated will put the `frame=` in `thing.draw(frame='use list or dict')`
> sizing: an extra feature, no not the 'auto', you can basically under scall or over scall to your likings
Basic usage:
> step 0, create the objects art: square_art = [['#000000','#000000'],['#000000','#000000'],['#000000','#000000']] # can also just jam it in the code
> step 1, create object: square = pyxel(0,0,square_art,1) # You can add in `width=,height=` if needed, but will set it auto matically
> step 2, draw the object: square.draw()
> Tip 1: '#======' is taken as an empty space
Movement:
> Moving the object: square.move('both',(10,-10))
> Teleporting the object: square.set('x',0)
> Tip 1: 'both' needs a (int,int) however 'x' or 'y' needs just one int
> Tip 2: you can change any self.var by self.var=what_you_need, but that's boring
Animations:
> step 0, create the art: square_loading_screen_art = [[['#======','#======'],['#======','#000000']],[['#======','#======'],['#000000','#======']],[['#000000','#======'],['#======','#======']],[['#======','#000000'],['#======','#======']]]
> step 1, create object: square_loading_screen = pyxel(0,0,square_loading_screen_art,10,type='animated')
> step 2, draw the frame you want squar_loading_screen.draw(2)
> Tip 1: a dict may work better example: `{'this':data,2:data,'that':data}` but it's no different
Reading the version:
> first letter: [U]n/[T]ested
> second letter: [P]rototype/[L]aunched
> third letter: [V]ersion
> the rest: version(int).updates(int)
"""""" ^ README ^ """

""" v CODE v """
class pyxelist:
    def __init__(self,xpos:int,ypos:int,data:list|dict,size:int,obj_type:str='solid',width:str|int='auto',height:str|int='auto'):
        self.data=data
        self.size=size
        self.type=obj_type
        self.pos=(xpos,ypos)
        if height=='auto':height=len(data)
        if width=='auto':width=len(data[0])
        self.dym=(width,height)
        self.t=turtle
        self.t.hideturtle()
        self.t.penup()
        return
    def draw(self,frame=0):
        sx=round(self.pos[0]-self.dym[0]*self.size/2)
        sy=round(self.pos[1]+self.dym[1]*self.size/2)
        self.t.goto(sx,sy)
        self.t.setheading(0)
        if self.type=='solid':
            nl_loop=0
            for list in self.data:
                self.t.goto(sx,sy-nl_loop*self.size)
                for color in list:
                    if color=='#======':pass
                    else:self.t.color(color),self.t.begin_fill()
                    for side in range(4):
                        self.t.forward(self.size)
                        self.t.right(90)
                    if color!='#======':self.t.end_fill()
                    self.t.forward(self.size)
                nl_loop+=1
            pass
        elif self.type=='animated':
            nl_loop=0
            for list in self.data[frame]:
                self.t.goto(sx,sy-nl_loop*self.size)
                for color in list:
                    if color=='#======':pass
                    else:self.t.color(color),self.t.begin_fill()
                    for side in range(4):
                        self.t.forward(self.size)
                        self.t.right(90)
                    if color!='#======':self.t.end_fill()
                    self.t.forward(self.size)
                nl_loop+=1
            pass
        return
    def set(self,pos:str,by:int|tuple):
        if pos.lower()=='x':
            self.pos[0]=by
            pass
        elif pos.lower()=='y':
            self.pos[1]=by
            pass
        elif pos.lower()=='both':
            self.pos=by
            pass
        pass
    def move(self,pos:str,by:int|tuple):
        if pos.lower()=='x':
            self.pos[0]+=by
            pass
        elif pos.lower()=='y':
            self.pos[1]+=by
            pass
        elif pos.lower()=='both':
            self.pos+=by
            pass
        pass
    pass
""" ^ CODE ^ """

""" v CREDITS v """"""
Developer:
    Github user@yanlin522: created it
"""""" ^ CREDITS ^ """