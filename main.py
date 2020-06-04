#! /usr/bin/env python3
import init
import solution

def main():
    Job = init.cli() # партия деталей
    Job.info()
    solution.bee(Job)
    
main()