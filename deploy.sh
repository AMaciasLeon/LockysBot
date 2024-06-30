#!/bin/bash

# Detener cualquier instancia anterior del bot
pkill -f 'python LockysBot.py'

# Inicia una nueva instancia
nohup python LockysBot.py &