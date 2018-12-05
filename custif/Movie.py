#!/usr/bin/env python3

message = 'You don\'t know much about movies , do you?'
print('Which movie is your favorite: Harry Potter, Lord of the Rings, Star Wars, or The Muppetts?')

movie = str(input())
if movie in 'Harry Potter':
	message = message
elif movie in 'Lord of the Rings':
	message = 'Great choice!'
elif movie in 'Star Wars':
	message = 'Great choice!'
elif movie in 'The Muppetts':
	message = message
print(message)