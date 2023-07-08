#!/usr/bin/env python3
# App.py

from tkinter import *
from tkinter import ttk

import random

def get_key_from_value(d, val):
  keys = [k for k, v in d.items() if v == val]
  if keys:
    return keys[0]
  return None

root = Tk()

root.title(u"11cards")
root.geometry("800x600")

frame = Frame(root)

def main():
  app = App()
  app.select()

def create_select(hands, callback):
  global frame
  frame.destroy()
  frame = Frame(root)
  Label(frame, text=f"あなたの手札：{len(hands[0])}").pack()
  Label(frame, text=f"敵の手札：{len(hands[1])}").pack()
  hands[0].sort()
  for i in range(len(hands[0])):
    card = App.conv_card(hands[0][i])
    button = Button(frame, text=card, width="20")
    button.bind("<Button-1>", callback)
    button.pack()
  frame.pack()

def notice_result(hands):
  global frame
  frame.destroy()
  frame = Frame(root)
  Label(frame, text=f"あなたの手札：{len(hands[0])}").pack()
  Label(frame, text=f"敵の手札：{len(hands[1])}").pack()
  text = "You Win!" if len(hands[0]) else "You Lose!" if len(hands[1]) else "Drow!"
  print(text)
  Label(frame, text=text).pack()
  Button(frame, text="retry", width="20", command=main).pack()
  frame.pack()

class App:
  alp = {'A':1, 'J':11, 'Q':12, 'K':13}

  def __init__(self):
    cards = [i for i in range(1,14)] * 2
    # cards = [i if i != 1 else 'A' for i in range(1,14)] * 2
    random.shuffle(cards)
    self.hands = [cards[:11], cards[12:23]]
    print(self.hands)

  def select(self):
    create_select(self.hands, self.selected)

  def selected(self, event):
    selected_item = self.conv_int(event.widget["text"])
    print(selected_item)
    self.hands[0].remove(selected_item)
    res = self.judge(selected_item, self.hands[1].pop())
    if res[0] is not None:
      self.hands[0].append(res[0])
    if res[1] is not None:
      self.hands[1].append(res[1])
      random.shuffle(self.hands[1])
    print(self.hands)
    if len(self.hands[0]) and len(self.hands[1]):
      self.select()
    else:
      notice_result(self.hands)

  @staticmethod
  def conv_int(card):
    if card in App.alp:
      return App.alp[card]
    else:
      return int(card)

  @staticmethod
  def conv_card(num):
    if num in App.alp.values():
      return get_key_from_value(App.alp, num)
    else:
      return num

  @staticmethod
  def judge(a, b):
    print([a, b])
    if a == 1 and b > 10:
      return [b, None]
    elif a > 10 and b == 1:
      return [None, a]
    elif a > b:
      return [b, None]
    elif a < b:
      return [None, a]
    else:
      return [None, None]

main()
root.mainloop()
