#!/usr/bin/env python
# -*- coding: utf-8 -*-
#y= posicao, v=velocidade

def g():
  return 9.80665

# Analitica
def positionA(y0, v0, t):
  return y0 + v0*t - (g() * t**2) / 2.0

def velocityA(v0, t):
  return v0 - g() * t

def freeFallAnalytical(y0, v0, tf, step):
  t = 0
  v = []
  y = []
  while (t <= tf):
    y.append(positionA(y0,v0,t))
    v.append(velocityA(v0,t))
    t += step
    return y,v

# Euler
def positionE(y0, v0, dt):
  return y0 + v0 * dt

def velocityE(v0, dt):
  return v0 - g() * dt

def freeFallEuler(y0, v0, tf, step):
  t = 0
  v = []
  y = []
  while (t <= tf):
    y.append(y0)
    v.append(v0)
    y0 = positionE(y0,v0,step)
    v0 = velocityE(v0,step)
    t += step
  return y,v
