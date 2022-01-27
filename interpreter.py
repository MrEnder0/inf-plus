from win10toast import ToastNotifier
from datetime import date
from logger import *
from config import *
import webbrowser, threading, random, time, os

today = date.today()
date = today.strftime("%m/%d/%y")
vars = {'autousb_version': '0.7.6', 'autousb_release_type': 's', 'autousb_author': 'Team Codingo', 'date_today': today, 'num_pi': '3.1415926535', 'num_e': '2.7182818284'}

#prepare the file
def preinterpret(letter):
    file = open(letter + ":\\" + "main.autousb", "r")
    interpret(letter, file)

#main function
def interpret(letter, file):
    if not os.path.exists(letter + ":\\autousbtemp"):
        os.makedirs(letter + ":\\autousbtemp")

    for line in file:
        if line.startswith(";"):
            pass

        if line.startswith("exit"):
            break

        if line.startswith("loop"):
            try:
                syntax = line
                syntax = syntax.replace("loop ","");
                syntax = syntax.replace("\n","");
                syntaxsplit = syntax.split(" || ")
                command = str(syntaxsplit[1])
                times = str(syntaxsplit[0])
                times = replacevars(times)
                createloop(letter, command, times)
                syntax = letter + ":\\autousbtemp\\" + "loop.autousb"
                time.sleep(0.2)
                loopthread = threading.Thread(target=interpret(letter, open(syntax, "r"))).start()
                while loopthread.is_alive():
                    pass
                pass
            except:
                logadd("[!]", f'[{date}]', "syntax error in loop")
                pass

        if line.startswith("if"):
            try:
                syntax = line
                syntax = syntax.replace("if ","");
                syntax = syntax.replace("\n","");
                syntaxsplit = syntax.split(" || ")
                condition = syntaxsplit[0]
                condition = replacevars(condition)
                command = syntaxsplit[1]
                if " = " in condition:
                    syntaxsplit = condition.split(" = ")
                    if syntaxsplit[0] == syntaxsplit[1]:
                        createif(letter, command)
                        syntax = letter + ":\\autousbtemp\\" + "if.autousb"
                        time.sleep(0.2)
                        ifthread = threading.Thread(target=interpret(letter, open(syntax, "r"))).start()
                        while ifthread.is_alive():
                            pass
                        pass
                elif " != " in condition:
                    syntaxsplit = condition.split(" != ")
                    if syntaxsplit[0] != syntaxsplit[1]:
                        createif(letter, command)
                        syntax = letter + ":\\autousbtemp\\" + "if.autousb"
                        time.sleep(0.2)
                        ifthread = threading.Thread(target=interpret(letter, open(syntax, "r"))).start()
                        while ifthread.is_alive():
                            pass
                        pass
                elif " > " in condition:
                    syntaxsplit = condition.split(" > ")
                    if int(syntaxsplit[0]) > int(syntaxsplit[1]):
                        createif(letter, command)
                        syntax = letter + ":\\autousbtemp\\" + "if.autousb"
                        time.sleep(0.2)
                        ifthread = threading.Thread(target=interpret(letter, open(syntax, "r"))).start()
                        while ifthread.is_alive():
                            pass
                        pass
                elif " < " in condition:
                    syntaxsplit = condition.split(" < ")
                    if int(syntaxsplit[0]) < int(syntaxsplit[1]):
                        createif(letter, command)
                        syntax = letter + ":\\autousbtemp\\" + "if.autousb"
                        time.sleep(0.2)
                        ifthread = threading.Thread(target=interpret(letter, open(syntax, "r"))).start()
                        while ifthread.is_alive():
                            pass
                        pass
                elif " >= " in condition:
                    syntaxsplit = condition.split(" >= ")
                    if int(syntaxsplit[0]) >= int(syntaxsplit[1]):
                        createif(letter, command)
                        syntax = letter + ":\\autousbtemp\\" + "if.autousb"
                        time.sleep(0.2)
                        ifthread = threading.Thread(target=interpret(letter, open(syntax, "r"))).start()
                        while ifthread.is_alive():
                            pass
                        pass
                elif " <= " in condition:
                    syntaxsplit = condition.split(" <= ")
                    if int(syntaxsplit[0]) <= int(syntaxsplit[1]):
                        createif(letter, command)
                        syntax = letter + ":\\autousbtemp\\" + "if.autousb"
                        time.sleep(0.2)
                        ifthread = threading.Thread(target=interpret(letter, open(syntax, "r"))).start()
                        while ifthread.is_alive():
                            pass
                        pass
                elif " contains " in condition:
                    syntaxsplit = condition.split(" contains ")
                    if syntaxsplit[1] in syntaxsplit[0]:
                        createif(letter, command)
                        syntax = letter + ":\\autousbtemp\\" + "if.autousb"
                        time.sleep(0.2)
                        ifthread = threading.Thread(target=interpret(letter, open(syntax, "r"))).start()
                        while ifthread.is_alive():
                            pass
                        pass
                else:
                    logadd("[!]", f'[{date}]', f'invalid if statement from drive {letter}')
                    pass
            except:
                logadd("[!]", f'[{date}]', f'failed to create if from drive {letter}')
                pass

        if line.startswith("setvar"):
            try:
                syntax = line
                syntax = syntax.replace("setvar ","");
                syntax = syntax.replace("\n","");
                if " = " in syntax:
                    syntaxsplit = syntax.split(" = ")
                    vars[str(syntaxsplit[0])] = str(syntaxsplit[1])
                elif " += " in syntax:
                    syntaxsplit = syntax.split(" += ")
                    syntax1 = replacevars(syntaxsplit[0])
                    syntax2 = replacevars(syntaxsplit[1])
                    vars[str(syntaxsplit[0])] = str(int(syntax1) + int(syntax2))
                elif " -= " in syntax:
                    syntaxsplit = syntax.split(" -= ")
                    syntax1 = replacevars(syntaxsplit[0])
                    syntax2 = replacevars(syntaxsplit[1])
                    vars[str(syntaxsplit[0])] = str(int(syntax1) - int(syntax2))
                elif " *= " in syntax:
                    syntaxsplit = syntax.split(" *= ")
                    syntax1 = replacevars(syntaxsplit[0])
                    syntax2 = replacevars(syntaxsplit[1])
                    vars[str(syntaxsplit[0])] = str(int(syntax1) * int(syntax2))
                elif " /= " in syntax:
                    syntaxsplit = syntax.split(" /= ")
                    syntax1 = replacevars(syntaxsplit[0])
                    syntax2 = replacevars(syntaxsplit[1])
                    vars[str(syntaxsplit[0])] = str(int(syntax1) / int(syntax2))
                elif " random " in syntax:
                    syntaxsplit = syntax.split(" random ")
                    var = syntaxsplit[0]
                    syntaxsplit = str(syntaxsplit[1]).split(" to ")
                    syntax1 = replacevars(syntaxsplit[0])
                    syntax2 = replacevars(syntaxsplit[1])
                    vars[str(var)] = str(random.randint(int(syntax1), int(syntax2)))
                else:
                    logadd("[!]", f'[{date}]', f'failed to set variable from drive {letter}')
                    pass
            except:
                logadd("[!]", f'[{date}]', f'failed to set variable {syntax} from drive {letter}')
                pass

        if line.startswith("delvar"):
            try:
                syntax = line
                syntax = syntax.replace("delvar ","");
                syntax = syntax.replace("\n","");
                syntaxsplit = syntax.split(" = ")
                name = syntaxsplit[0]
                del vars[name]
            except:
                logadd("[!]", f'[{date}]', f'failed to delete variable {syntax} from drive {letter}')
                pass

        if line.startswith("wait"):
            try:
                syntax = line
                syntax = syntax.replace("wait ","");
                syntax = syntax.replace("\n","");
                syntax = replacevars(syntax)
                syntax = int(syntax)
                time.sleep(syntax)
                pass
            except:
                logadd("[!]", f'[{date}]', f'failed to wait {syntax} from drive {letter}')
                pass

        if line.startswith("run"):
            try:
                syntax = line.split(" ")
                syntax = letter + ":\\" + syntax[1]
                syntax = syntax.replace("\n","");
                syntax = replacevars(syntax)
                if ".autousb" in line:
                    thread = threading.Thread(target=interpret(letter, open(syntax, "r"))).start()
                    while thread.is_alive():
                        pass
                    pass
                else:
                    if allowProgramExecution == True:
                        os.startfile(syntax)
                        logadd("[#]", f'[{date}]', f'launched {syntax} from drive {letter}')
                    pass
            except:
                logadd("[!]", f'[{date}]', f'could not launch {syntax} from drive {letter}')
                pass

        if line.startswith("log"):
            try:
                syntax = line
                syntax = syntax.replace("log ","");
                syntax = syntax.replace("\n","");
                syntax = replacevars(syntax)
                logadd("[*]", f'[{date}]', f'logged "{syntax}" from drive {letter}')
                pass
            except:
                logadd("[!]", f'[{date}]', f'could not log, from drive {letter}')
                pass

        if line.startswith("logclear"):
            if allowLogClearing == True:
                logclear()
                logadd("[#]", f'[{date}]', f'the log was cleared from drive {letter}')
            pass

        if line.startswith("notify"):
            try:
                syntax = line
                syntax = syntax.replace("notify ","");
                syntax = syntax.replace("\n","");
                syntax = replacevars(syntax)
                try:
                    syntax = syntax.split(" for ")
                    toaster = ToastNotifier()
                    toaster.show_toast("AutoUSB Project", f"{str(syntax[0])}", duration=int(syntax[1]), threaded=True)
                    pass
                except:
                    toaster = ToastNotifier()
                    toaster.show_toast("AutoUSB Project", f"{syntax}", threaded=True)
                    pass    
            except:
                logadd("[!]", f'[{date}]', f'failed to display notification from drive {letter}')
                pass

        if line.startswith("search"):
            try:
                syntax = line
                syntax = syntax.replace("search ","");
                syntax = syntax.replace("\n","");
                syntax = replacevars(syntax)
                webbrowser.open(f'https://www.google.com/search?q={syntax}')
                pass
            except:
                logadd("[!]", f'[{date}]', f'failed to search {syntax} from drive {letter}')
                pass

#part of loop code
def createloop(letter, command, times):
    try:
        loopcommands = open(letter + ":\\autousbtemp\\" + "loop.autousb", "w")
        commands = command.split(" | ")
        timeswritten = 0

        while int(times) > timeswritten:
            for command in commands:
                loopcommands.write(f'{command}\n')
            timeswritten += 1
    except:
        logadd("[!]", f'[{date}]', f'failed to create loop from drive {letter}')
        pass

#part of if code
def createif(letter, command):
    try:
        ifcommands = open(letter + ":\\autousbtemp\\" + "if.autousb", "w")
        commands = command.split(" | ")
        for command in commands:
            ifcommands.write(command + '\n')
    except:
        logadd("[!]", f'[{date}]', f'failed to create if from drive {letter}')
        pass

#part of varible code
def replacevars(input):
    for keyword, value in vars.items():
        if keyword in input:
            input = input.replace(keyword, value)
    return input
