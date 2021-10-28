class ConstructiveDilemmaTemplate():
  '''
  RULE: ((p → q) ∧ (r → s) ∧ (p ∨ r)) ⊢ (q ∨ s)
  '''
  def __init__(self, p, q, r, s):
    self.x, self.y = get_objects(p)
    _, self.z = get_objects(q)

    self.a, self.b = get_objects(r)
    _, self.c  = get_objects(s)

    self.p = self.preprocess(p)
    self.q = self.preprocess(q)
    self.r = self.preprocess(r)
    self.s = self.preprocess(s)

  def generate_context(self):
    context = ""
    context += self.M_implies_N(self.p, self.z).capitalize()
    context += self.M_implies_N(self.r, self.c).capitalize()
    context += self.M_or_N(self.p, self.r).capitalize()
    context += self.conclusion(self.x, self.z, self.a, self.c).capitalize()
    return context

  def generate_questions(self):
    questions = {
        f'If {self.p}, is it a {self.z}?' : True,
        f'If {self.p}, is it not a {self.z}?': False,
        f'If {self.r}, is it a {self.c}?' : True,
        f'If {self.r}, is it not a {self.c}?' : False,
        f'If {self.x} is a {self.z}, then is {self.a} a {self.c}?': False,
        f'If {self.x} is a {self.z}, then is {self.a} not a {self.c}?': True,
        f'If {self.a} is a {self.c}, then is {self.x} a {self.z}?': False,
        f'If {self.a} is a {self.c}, then is {self.x} not a {self.z}?': True
    }

    return questions

  def M_implies_N(self, m, n) :
    return f'if {m}, then it\'s a {n}. '

  def M_or_N(self, m, n):
    return f'either {m} or {n}. '

  def conclusion(self, m, n, u, v):
    return f'therfore either {m} is a {n}, or {u} is a {v}.'

  def preprocess(self, text):
    text = text.replace("[[","").replace("]]","")
    return text