# standard modules
#  https://github.com/graktung/myterminal
import pygame
import time
from pygame.locals import*
import sys
import random
import pyperclip
from shlex import split
# my modules
import data.directory as directory

'''
    displays the terminal on the screen and takes in data
        from the user
    calls the directory file to parse the commands and
        display the output to the user
'''

class Terminal(object):
    def __init__(self, size, player):
        self.player = player
        self.width, self.height = size
        self.fullLine = 18
        self.BLACK = 0, 0, 0
        self.WHITE = 255, 255, 255
        self.RED = 255, 0, 0
        self.ERRORCOLOR = 204, 0, 0
        self.BLUE = 0, 0, 205
        self.GREEN = 0, 128, 0
        self.YELLOW = 255, 255, 0
        self.PINK = 255, 0, 255
        self.font = pygame.font.SysFont("consolas", 16)
        self.listColor = [self.WHITE, self.RED, self.BLUE, self.GREEN, self.YELLOW, self.PINK]
        self.changeColor = 0
        self.showCur = 0
        self.colorCur = self.listColor.pop(self.listColor.index(random.choice(self.listColor)))
        self.SCREEN = pygame.display.get_surface()

        self.content = []
        self.contentDisplay = []
        self.listCommand = []
        self.indexListCommand = 0
        self.contentLineCurrent = ''
        self.contentLineCurrentDisplay = '|'
        self.posCursor = 0
        self.currentLine = True
        self.root = 'player@game:~# '
        self.camTop = 0
        self.camBot = 0
        self.line = 0

    def displayText(self, text, at, x, y, color, bg=None):
        if text.startswith('1f401268'):
            text = text.replace('1f401268', '')
            label = self.font.render(text, at, self.ERRORCOLOR, bg)
            self.SCREEN.blit(label, (x, y))
        elif text.startswith('7084338a'):
            text = text.replace('7084338a', '')
            label = self.font.render(text, at, self.GREEN, bg)
            self.SCREEN.blit(label, (x, y))
        elif text.startswith('36ac99f1'):
            text = text.replace('36ac99f1', '')
            label = self.font.render(text, at, self.BLUE, bg)
            self.SCREEN.blit(label, (x, y))
        elif not 'player@game:~# ' in text:
            label = self.font.render(text, at, self.WHITE, bg)
            self.SCREEN.blit(label, (x, y))    
        else:
            labelUser = self.font.render('player@game', at, (self.RED), bg)
            labelColon = self.font.render(':', at, (self.WHITE), bg)
            labelNS = self.font.render('#', at, (self.WHITE), bg)
            labelTilde = self.font.render('~', at, (self.BLUE), bg)
            self.SCREEN.blit(labelUser, (0, y))
            self.SCREEN.blit(labelColon, (145, y))
            self.SCREEN.blit(labelTilde, (153, y))
            self.SCREEN.blit(labelNS, (165, y))
            text = text.replace('player@game:~#', '')
            labelText = self.font.render(text, at, color, bg)
            self.SCREEN.blit(labelText, (170, y))

    def readChar(self, event):
        if event.key == pygame.K_BACKSPACE:
            return 'backspace'
        elif event.key == pygame.K_PAGEUP:
            return 'pageup'
        elif event.key == pygame.K_PAGEDOWN:
            return 'pagedown'
        elif event.key == pygame.K_TAB:
            return 'tab'
        elif event.key == pygame.K_RETURN:
            return 'enter'
        elif event.key == pygame.K_ESCAPE:
            return 'esc'
        elif event.key in (pygame.K_RSHIFT, pygame.K_LSHIFT):
            return 'shift'
        elif event.key in (pygame.K_RCTRL, pygame.K_LCTRL):
            return 'control'
        elif event.key == pygame.K_RIGHT:
            return 'kright'
        elif event.key == pygame.K_LEFT:
            return 'kleft'
        elif event.key == pygame.K_UP:
            return 'kup'
        elif event.key == pygame.K_DOWN:
            return 'kdown'
        elif event.key == pygame.K_CAPSLOCK:
            return None
        elif event.key == 282:
            return 'paste'
        elif event.key == 283:
            return 'begincur'
        elif event.key == 284:
            return 'endcur'
        elif event.key == 285:
            return 'delall'
        else:
            return event.unicode

    def helpCommand(self):
        lstHelp = [[]]
        # lstHelp.append(["7084338aTerminal Working"])
        lstHelp.append(['"exit" -> stop Terminal from working'])
        lstHelp.append(['"clear" -> clear all command lines which is displayed in Terminal'])
        # lstHelp.append([])
        # lstHelp.append(["7084338aDirectory Working"])
        lstHelp.append(['"ls" -> List all the folders and the files at current working directory'])
        lstHelp.append(['"pwd" -> Print the current working directory'])
        lstHelp.append(['"cd new_working_directory" -> Change current working directory to new_working_directory'])
        # lstHelp.append([])
        # lstHelp.append(["7084338aFiles And Folders Working"])
        lstHelp.append(['"move file_name/folder_name new_place" -> move the file or the folder to new_place'])
        lstHelp.append(['"rename file_name/folder_name new_name" -> rename the file or the folder to new_name'])
        lstHelp.append(['"rmf file_name" -> remove the file file_name'])
        lstHelp.append(['"rmdir folder_name" -> remove the folder folder_name'])
        lstHelp.append(['"mkf file_name" -> create file file_name'])
        lstHelp.append(['"mkdir folder_name" -> create folder folder_name'])
        lstHelp.append(['"cat file_name" -> get content of the file_name'])
        lstHelp.append(['"checkpath path" -> check whether path valid or not'])
        lstHelp.append(['"grep PATTERN file -> prints lines matching the RegEx pattern in the file'])
        lstHelp.append(['"checkdir folder_name" -> check whether folder folder_name exist or not'])
        lstHelp.append(['"checkf file_name" -> check whether file file_name exist or not'])
        lstHelp.append(['"zip ls file_zip" -> get the list in file_zip'])
        lstHelp.append(['"zip getfilesize item file_zip" -> get file size of item in file_zip'])
        lstHelp.append(['"zip getcomsize item file_zip" -> get compress size of item in file_zip'])
        lstHelp.append(['"unzipall file_zip [path]" -> extract all file in file_zip into the path'])
        lstHelp.append(['"unzip item file_zip [path] - > extract item in the file zip into the path'])
        lstHelp.append(['"zip file/folder_name file_zip" -> create a zip file from file/folder_name'])
        return lstHelp

    def processCommand(self, cmd):
        cmd = cmd.strip()
        if cmd == '':
            return []
        elif cmd == 'exit':
            sys.exit(0)
        elif cmd == 'help':
            return self.helpCommand()
        elif cmd == 'pwd':
            return [directory.getPWD().replace('\\', '/')]
        elif cmd == 'ls':
            return directory.getList()
        elif cmd.startswith('cd '):
            direc = cmd[3:]
            direc = direc.strip()
            if '~' in direc:
                self.player.numRoomsCompleted += 1
                self.player.roomFiveCompleted = True
                self.player.selectStartPos("right")
                self.player.scene.nextRoom = "left"
                self.player.scene.manager.nextScene()
                return ["You solved the island room!"]
            directory.changePWD(direc)
            return directory.getPWD()
        elif cmd.startswith('move '):
            cmd = cmd[5:]
            return directory.move(cmd)
        elif cmd.startswith('rename '):
            cmd = cmd[7:]
            return directory.rename(cmd)
        elif cmd.startswith('rmf '):
            cmd = cmd[4:]
            return directory.removeFile(cmd)
        elif cmd.startswith('rmdir '):
            cmd = cmd[6:]
            return directory.removeDir(cmd) 
        elif cmd.startswith('mkdir '):
            cmd = cmd[6:]
            return directory.makeDir(cmd)
        elif cmd.startswith('mkf '):
            cmd = cmd[4:]
            return directory.makeFile(cmd)
        elif cmd == 'p':
            self.player.roomThreeCompleted = True
            self.player.roomFourCompleted = True
            self.player.roomFiveOneCompleted = True
            self.player.roomSevenOneCompleted = True
            self.player.roomEightOneCompleted = True
            self.player.roomNineOneCompleted = True
            self.player.roomTenOneCompleted = True
            self.player.roomElevenOneCompleted = True
            self.player.roomTwelveOneCompleted = True
            self.player.numRoomsCompleted = 9
            return []
        elif cmd.startswith('cat '):
            cmd = cmd[4:]
            # if 'thisIsTheFlagFile.txt' in cmd:
            #     self.player.roomEightCompleted = True
            #     return ["You completed the cat room!"]
            return directory.getContent(cmd)
        elif cmd.startswith('tac '):
            cmd = cmd[4:]
            # if 'FileFlagTheIsthis.txt' in cmd:
            #     self.player.roomNineCompleted = True
            #     return ["You completed the tac room!"]
            return directory.getReverseContent(cmd)
        elif cmd.startswith('grep '):
            cmd = split(cmd[5:])
            return directory.findContent(cmd[1], cmd[0])
        elif cmd.startswith('expr '):
            cmd = cmd[5:]
            if '43' in cmd and '9762' in cmd and '476112' in cmd:
                if cmd.index('+') > 0 and cmd.index('-') > cmd.index('+'):
                    if str(eval(cmd) == (43+9762-476112)):
                        self.player.numRoomsCompleted += 1
                        self.player.roomNineCompleted = True
                        return ["You found the right answer!"]
            return ([str(eval(cmd))])
        elif cmd.startswith('sudo'):
            self.player.sudoPerms = True
            self.player.roomFourCompleted = True
            self.player.numRoomsCompleted += 1
            return []
        elif cmd.startswith('xrandr '):
            if '-brightness' in cmd:
                self.player.roomSevenCompleted = True
                self.player.numRoomsCompleted += 1
                return ["You solved the brightness room!"]
            return ["Not quite"]
        elif 'THI5_I5_TH3_GR3P_T0_5UCC355' in cmd:
            self.player.roomThreeCompleted = True
            self.player.numRoomsCompleted += 1
            return ["You found the flag to the grep/trashcan room!"]
        elif 'C4T5_4R3_V3RY_C00l_92733' in cmd:
            self.player.roomEightCompleted = True
            self.player.numRoomsCompleted += 1
            return ["You found the flag to the cat room!"]
        elif 'C001_V3RY_4R3_C4T5_18335' in cmd:
            self.player.roomNineCompleted = True
            self.player.numRoomsCompleted += 1
            return ["You found the flag to the tac room!"]
        elif 'UNZ1P_Y0UR_TR345UR3_39823' in cmd:
            self.player.roomTwelveCompleted = True
            self.player.numRoomsCompleted += 1
            return ["You found the flag to the zip room!"]
        elif cmd.startswith('cowsay '):
            cmd = cmd[7:]
            self.player.roomEightCompleted = True
            self.player.numRoomsCompleted += 1
            return directory.cowsay(cmd)
        elif cmd.startswith('checkpath '):
            cmd = cmd[10:]
            return directory.checkPath(cmd)
        elif cmd.startswith('checkdir '):
            cmd = cmd[9:].startswith('FLAG3').startswith('FLAG3')
            return directory.checkDir(cmd)
        elif cmd.startswith('checkf '):
            cmd = cmd[7:]
            return directory.checkFile(cmd)
        elif cmd.startswith('zip ls '):
            cmd = cmd[7:]
            return directory.zipLS(cmd)
        elif cmd.startswith('zip getfilesize '):
            cmd = cmd[16:]
            return directory.zipGetFileSize(cmd)
        elif cmd.startswith('zip getcomsize '):
            cmd = cmd[15:]
            return directory.zipGetComSize(cmd)
        elif cmd.startswith('zip '):
            cmd = cmd[4:]
            return directory.createZip(cmd)
        elif cmd.startswith('unzipall '):
            cmd = cmd[9:]
            return directory.unzipAll(cmd)
        elif cmd.startswith('unzip '):
            cmd = cmd[6:]
            # if 'aVeryCompressedFile.zip' in cmd:
            #     self.player.numRoomsCompleted += 1
            #     self.player.roomTwelveCompleted = True
            #     return ["You unzipped the right file!"]
            return directory.unzip(cmd)
        else:
            return ['%r not found.' %(cmd), '7084338aIf you have no idea what to do use "help" command.']

    def update(self, events):
        self.fullLine = (self.height - 120) // 20
        if self.currentLine:
            if self.camBot - self.camTop == (self.fullLine - 1):
                self.camBot = len(self.contentDisplay)
                self.camTop = self.camBot - (self.fullLine - 1)
        for event in events:
            print (event)
            if event.type == pygame.VIDEORESIZE:
                self.SCREEN = pygame.display.set_mode(event.dict['size'],HWSURFACE|DOUBLEBUF|RESIZABLE)
                self.width, self.height = pygame.display.get_surface().get_size()
                if self.width < 400:
                    self.width = 400
                    self.SCREEN = pygame.display.set_mode((self.width,self.height), HWSURFACE|DOUBLEBUF|RESIZABLE)
                if self.height < 400:
                    self.height = 400
                    self.SCREEN = pygame.display.set_mode((self.width,self.height), HWSURFACE|DOUBLEBUF|RESIZABLE)
                self.fullLine = (self.height - 120) // 20
                if len(self.contentDisplay) >= self.fullLine:
                    self.camBot = len(self.contentDisplay)
                    self.camTop = self.camBot - (self.fullLine - 1)
                else:
                    self.camBot = len(self.contentDisplay)
                    self.camTop = 0
                self.currentLine = True
            elif event.type == pygame.QUIT: sys.exit()
            elif event.type == pygame.KEYDOWN:
                newChar = self.readChar(event)
                print(newChar)
                if newChar not in ('delall', 'begincur', 'endcur', 'backspace', 'tab', 'enter', 'esc', 'pageup', 'pagedown',\
                    'shift', 'control', None, 'kright', 'kleft', 'kup', 'kdown', 'paste'):
                    try:
                        self.contentLineCurrent = list(self.contentLineCurrent)
                        self.contentLineCurrent.insert(self.posCursor, newChar)
                        self.contentLineCurrent = ''.join(self.contentLineCurrent)
                        self.posCursor += 1
                        lstChar = list(self.contentLineCurrent)
                        lstChar.insert(self.posCursor, '|')
                        self.contentLineCurrentDisplay = ''.join(lstChar)
                    except:
                        pass     
                    self.indexListCommand = 0
                    self.showCur = 0   
                    self.currentLine = True
                elif newChar == 'delall':
                    self.contentLineCurrent = ''
                    self.posCursor = 0
                    self.contentLineCurrentDisplay = '|'
                    self.currentLine = True
                elif newChar == 'begincur':
                    self.posCursor = 0
                    self.contentLineCurrentDisplay = '|' + self.contentLineCurrent
                    self.currentLine = True
                elif newChar == 'endcur':
                    self.posCursor = len(self.contentLineCurrent)
                    self.contentLineCurrentDisplay = self.contentLineCurrent + '|'
                    self.currentLine = True
                elif newChar == 'paste':
                    # if canCopy:
                    paste = pyperclip.paste()
                    self.showCur = 0
                    self.contentLineCurrent = list(self.contentLineCurrent)
                    self.contentLineCurrent.insert(self.posCursor, paste)
                    self.contentLineCurrent = ''.join(self.contentLineCurrent)
                    self.posCursor += len(paste)
                    lstChar = list(self.contentLineCurrent)
                    lstChar.insert(self.posCursor, '|')
                    self.contentLineCurrentDisplay = ''.join(lstChar)
                    # else:
                    #     print('Require Pyperclip module for Paste.')
                    self.currentLine = True
                elif newChar == 'pageup':    
                    if not len(self.listCommand) == 0:
                        if -len(self.listCommand) != self.indexListCommand:
                            self.indexListCommand -= 1
                            self.contentLineCurrent = self.listCommand[self.indexListCommand]
                            self.contentLineCurrentDisplay = self.contentLineCurrent + '|'
                            self.posCursor = len(self.contentLineCurrent)
                    self.currentLine = True
                    self.showCur = 0
                elif newChar == 'pagedown':
                    if not len(self.listCommand) == 0:
                        if self.indexListCommand < -1:
                            self.indexListCommand += 1
                            self.contentLineCurrent = self.listCommand[self.indexListCommand]
                            self.contentLineCurrentDisplay = self.contentLineCurrent + '|'
                            self.posCursor = len(self.contentLineCurrent)
                    self.currentLine = True
                    self.showCur = 0
                elif newChar == 'kup':
                    if self.camTop != 0:
                        if self.camBot - self.camTop == (self.fullLine - 1):
                            self.camBot -= 1
                            self.camTop -= 1
                            self.currentLine = False
                    self.showCur = 0
                elif newChar == 'kdown':
                    if self.camBot < len(self.contentDisplay):
                        self.camBot += 1
                        self.camTop += 1
                    self.showCur = 0
                elif newChar == 'kright':
                    if not len(self.contentLineCurrent) == self.posCursor:
                        self.posCursor += 1
                        lstChar = list(self.contentLineCurrent)
                        lstChar.insert(self.posCursor, '|')
                        self.contentLineCurrentDisplay = ''.join(lstChar)
                    self.currentLine = True
                    self.showCur = 0
                elif newChar == 'kleft':
                    if self.posCursor != 0:
                        self.posCursor -= 1
                        lstChar = list(self.contentLineCurrent)
                        lstChar.insert(self.posCursor, '|')
                        self.contentLineCurrentDisplay = ''.join(lstChar)
                    self.currentLine = True
                    self.showCur = 0
                elif newChar == 'backspace':
                    if len(self.contentLineCurrent) != 0 and self.posCursor != 0:
                        try:
                            self.contentLineCurrent = list(self.contentLineCurrent)
                            wordPoped = self.contentLineCurrent.pop(self.posCursor - 1)
                            self.contentLineCurrent = ''.join(self.contentLineCurrent)
                            self.posCursor -= 1
                        except:
                            self.contentLineCurrent = self.contentLineCurrent[1:]
                            self.posCursor = len(self.contentLineCurrent)
                        lstChar = list(self.contentLineCurrent)
                        lstChar.insert(self.posCursor, '|')
                        self.contentLineCurrentDisplay = ''.join(lstChar)
                        self.currentLine = True
                    self.showCur = 0
                elif newChar == 'enter':
                    self.currentLine = True
                    self.indexListCommand = 0
                    if self.camBot - self.camTop == (self.fullLine - 1):
                        self.camTop += 1
                    self.camBot += 1
                    self.content.append([self.root + self.contentLineCurrent])
                    if self.contentLineCurrent.strip() == 'clear':
                        self.camTop = 0
                        self.camBot = 0
                        self.posCursor = 0
                        self.content = []
                        self.contentLineCurrent = ''
                        self.contentLineCurrentDisplay = '|'
                    else:
                        contentAppend = self.processCommand(self.contentLineCurrent)
                        for eachLine in contentAppend:
                            if self.camBot - self.camTop == (self.fullLine - 1):
                                self.camTop += 1
                            self.camBot += 1
                            self.content.append(eachLine)
                    if len(self.contentLineCurrent.strip(' ')) != 0:
                        self.listCommand.append(self.contentLineCurrent)
                    self.posCursor = 0
                    self.contentLineCurrent = ''
                    self.contentLineCurrentDisplay = '|'
                    self.showCur = 0
        self.SCREEN.fill(self.BLACK)
        self.changeColor += 1
        self.showCur += 1
        if self.changeColor > 500:
            self.changeColor = 0
            appColorAgain = self.colorCur
            self.colorCur = self.listColor.pop(self.listColor.index(random.choice(self.listColor)))
            self.listColor.append(appColorAgain)

        self.contentDisplay = []
        for i in range(len(self.content)):
            text = ''.join(self.content[i])
            if len(text) * 8 > self.width:
                while len(text) * 8 > self.width:
                    textMini = text[:self.width // 8 - 1]
                    self.contentDisplay.append(textMini)
                    text = text[self.width // 8 - 1:]
                self.contentDisplay.append(text)
            else:
                self.contentDisplay.append(text)
        if self.currentLine:
            if len(self.contentDisplay) >= self.fullLine:
                self.camBot = len(self.contentDisplay)
                self.camTop = self.camBot - (self.fullLine - 1)
            else:
                self.camBot = len(self.contentDisplay)
                self.camTop = 0
        for i in range(self.camTop, self.camBot):
            self.displayText(self.contentDisplay[i], 1, 0, self.line * 20, self.WHITE)
            self.line += 1
        if self.camBot == len(self.contentDisplay):
            if self.showCur < 500:
                self.displayText(self.root + self.contentLineCurrentDisplay, 1, 0, self.line * 20, self.WHITE)
            else:
                self.displayText(self.root + self.contentLineCurrent, 1, 0, self.line * 20, self.WHITE)
            if self.showCur > 1000:
                self.showCur = 0
        else:
            self.displayText(''.join(self.contentDisplay[self.camBot]), 1, 0, self.line * 20, self.WHITE)
        self.line = 0
        pygame.display.flip()