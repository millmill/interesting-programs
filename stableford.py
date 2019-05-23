'''
This code was written in the second semester of my first year of Computer Applications in DCU.
The task was to create a program to calculate the results of a number of players 
who played a golf game using the stableford rules.
'''


import sys
longest_name = 0

class Hole(object):
   def __init__(self, par, index):
      self.index = index
      self.par = par
      self.score_map = {
      -6 : 8,
      -5 : 7,
      -4 : 6,
      -3 : 5,
      -2 : 4,
      -1 : 3,
      0 : 2,
      1 : 1,
      }

   def score_to_par(self, ttl_stroke):
      return ttl_stroke - self.par

   def score(self, ttl_stroke):
      stp = self.score_to_par(ttl_stroke)
      if stp >= 2:
         return 0
      if stp <= -7:
         return 9
      return self.score_map[stp]

   def hcp_free_strokes(self, handicap):
      starting = handicap / 18
      remaining = handicap % 18

      if self.index <= remaining:
         return starting + 1
      else:
         return starting

class Player(object):
   def __init__(self, name, handicap, stroke_per_hole):
      self.name = name
      self.handicap = handicap
      self.stroke_per_hole = stroke_per_hole
      self.disqualified = False

   
      for stroke in stroke_per_hole:
         if not stroke.isdigit() and stroke != 'X':
            self.disqualified = True
            break

   def stroke_by_hole(self, h_number):
      return self.stroke_per_hole[h_number - 1]

   def scoring(self, score):
      self.score = score

class Course(object):
   def __init__ (self, hole_par, index_par):
      self.holes = []
      for i in range(0, len(hole_par)):
         self.holes.append(Hole(int(hole_par[i]), int(index_par[i])))

def player_in(line_in):
   split_input = line_in.strip().split()
   player_strokes = split_input[-18:]
   player_handicap = int(split_input[:-18][-1:][0])
   player_name = " ".join(split_input[:-19])
   #print(len(player_name))
   return Player(player_name, player_handicap, player_strokes)


def player_result(player):
   return player.score

def main():
   longest_name = 0
   
   lines = sys.stdin.readlines()

   par_by_hole = lines[0].strip().split()
   index_by_hole = lines[1].strip().split()

   # create a collection of holes - a course:
   course = Course(par_by_hole, index_by_hole)

   #create list of players:
   players = []
   create_player = lines[2:]

   for player in create_player:
      players.append(player_in(player))
   #print(players)

   disqualified = []
   qualified = []

   for p in players:
      total_score = 0
      h_number = 1
      
      # this is to calculate the length need for our print statement neatness
      if longest_name < len(p.name):
         longest_name = int(len(p.name))
         #print(longest_name)

      if p.disqualified:
         disqualified.append(p)
         continue

      for hole in course.holes:
         if p.stroke_by_hole(h_number) != 'X':
            ttl_stroke = int(p.stroke_by_hole(h_number)) - int(hole.hcp_free_strokes(p.handicap))
            total_score += hole.score(ttl_stroke)
         h_number += 1
      p.scoring(total_score)
      qualified.append(p)

   # next, we print out the results nicely:

   for p in sorted(qualified, key = player_result, reverse = True):
      print("{:>{}} : {:>2d}".format(p.name, longest_name, p.score))

   for p in disqualified:
      print("{:>{}} : Disqualified".format(p.name, longest_name))

if __name__ == '__main__':
   main()
