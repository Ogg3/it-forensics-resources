def do_one():
  pass

def do_two():
  pass

def do_default():
  pass

actions = {1: do_one, 2: do_two}

actions = actions.get(x, do_default)
action(x)
