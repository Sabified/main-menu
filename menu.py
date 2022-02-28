import pygame

class Menu():
    def __init__(self, game):
        self.game = game
        self.mid_w, self.mid_h = self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2
        
        self.run_display = True

        self.cursor_rect = pygame.Rect(0, 0, 20, 20)
        self.offset = - 200

    def draw_cursor(self):
        self.game.draw_text('*', 40, self.cursor_rect.x, self.cursor_rect.y)
    
    def blit_screen(self):
        self.game.window.blit(self.game.display, (0, 0))
        pygame.display.update()
        self.game.reset_keys()


class MainMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = "Start"
        
        self.startx, self.starty = self.mid_w, self.mid_h + 20
        self.optionsx, self.optionsy = self.mid_w, self.mid_h + 70
        self.creditsx, self.creditsy = self.mid_w, self.mid_h + 120
        self.cursor_rect.midtop = (self.startx + self.offset, self.starty)

    def display_menu(self):
        self.run_display = True

        while self.run_display:
            self.game.check_events()
            self.check_input()

            self.game.display.fill(self.game.BLACK)

            self.game.draw_text('Game Title', 50, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 100)
            self.game.draw_text('Start Game', 32, self.startx, self.starty)
            self.game.draw_text('Options', 32, self.optionsx, self.optionsy)
            self.game.draw_text('Credits', 32, self.creditsx, self.creditsy)

            self.draw_cursor()
            self.blit_screen()
    
    def move_cursor(self):
        if self.game.DOWN_KEY:
            self.game.channel.play(self.game.sel3)
            if self.state == "Start":
                self.cursor_rect.midtop = (self.optionsx + self.offset, self.optionsy)
                self.state = "Options"
            elif self.state == "Options":
                self.cursor_rect.midtop = (self.creditsx + self.offset, self.creditsy)
                self.state = "Credits"
            elif self.state == "Credits":
                self.cursor_rect.midtop = (self.startx + self.offset, self.starty)
                self.state = "Start"
        elif self.game.UP_KEY:
            self.game.channel.play(self.game.sel3)
            if self.state == "Start":
                self.cursor_rect.midtop = (self.creditsx + self.offset, self.creditsy)
                self.state = "Credits"
            elif self.state == "Options":
                self.cursor_rect.midtop = (self.startx + self.offset, self.starty)
                self.state = "Start"
            elif self.state == "Credits":
                self.cursor_rect.midtop = (self.optionsx + self.offset, self.optionsy)
                self.state = "Options"

    def check_input(self):
        self.move_cursor()
        if self.game.SELECT_KEY:
            self.game.channel.play(self.game.sel1)
            if self.state == "Start":
                self.game.playing = True
            elif self.state == "Options":
                self.game.curr_menu = self.game.options_menu
            elif self.state == "Credits":
                self.game.curr_menu = self.game.credits_menu
            self.run_display = False


class OptionsMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)

        self.state = "Volume"
        self.volx, self.voly = self.mid_w, self.mid_h + 20

        self.controlsx, self.controlsy = self.mid_w, self.mid_h + 60

        self.cursor_rect.midtop = (self.volx + self.offset, self.voly)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()

            self.game.display.fill((0, 0, 0))

            self.game.draw_text('Options', 32, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 30)
            self.game.draw_text("Volume", 20, self.volx, self.voly)
            self.game.draw_text("Controls", 20, self.controlsx, self.controlsy)
            
            self.draw_cursor()
            self.blit_screen()

    def check_input(self):
        if self.game.BACK_KEY:
            self.game.curr_menu = self.game.main_menu
            self.run_display = False
            self.game.channel.play(self.game.sel5)
        elif self.game.UP_KEY or self.game.DOWN_KEY:
            self.game.channel.play(self.game.sel3)
            if self.state == "Volume":
                self.state  = 'Controls'
                self.cursor_rect.midtop = (self.controlsx + self.offset, self.controlsy)
            elif self.state == "Controls":
                self.state = 'Volume'
                self.cursor_rect.midtop = (self.volx + self.offset, self.voly)
        elif self.game.SELECT_KEY:
            if self.state == "Volume":
                self.game.channel.play(self.game.sel1)
                self.game.curr_menu = self.game.volume_menu
                self.run_display = False
            else:
                self.game.channel.play(self.game.hit3)

class VolumeMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)

        self.volVarX, self.volVarY = self.mid_w, self.mid_h + 20
        self.volVar = self.game.soundVolume

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()

            self.game.display.fill((0, 0, 0))

            self.game.draw_text('Volume', 32, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 30)
            self.game.draw_text(str(int(self.volVar)), 20, self.volVarX, self.volVarY)
            
            self.game.soundVolume = self.volVar

            self.blit_screen()
    
    def check_input(self):
        if self.game.BACK_KEY:
            self.run_display = False
            self.game.channel.play(self.game.sel5)
            self.game.curr_menu = self.game.options_menu
        
        if self.game.LEFT_KEY:
            self.game.channel.play(self.game.sel3)
            # Remove 25
            self.volVar -= 0.25
            self.game.LEFT_KEY = False
        elif self.game.RIGHT_KEY:
            self.game.channel.play(self.game.sel3)
            # Add 25
            self.volVar += 0.25
            self.game.RIGHT_KEY = False


class CreditsMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)

    def display_menu(self):
        self.run_display = True

        self.game.check_events()

        if self.game.SELECT_KEY or self.game.BACK_KEY:
            self.game.curr_menu = self.game.main_menu
            self.run_display = False

        self.game.display.fill(self.game.BLACK)

        self.game.draw_text("Credits", 20, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 20)
        self.game.draw_text('Made by Sabified', 15, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 + 10)

        self.blit_screen()
