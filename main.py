#! /usr/bin/env python3
import init
import solution

def main():
    Job = init.cli() # партия деталей
    Job.info()
    S, z_max = solution.bee(Job)
    print("---Ответ---")
    print(S, "->", z_max)
    
main()