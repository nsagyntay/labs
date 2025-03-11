#Create music player with keyboard controller.
#  You have to be able to press keyboard: play,
#  stop, next and previous as some keys. Player has
#  to react to the given command appropriately.
import pygame
import os

pygame.init()
screen = pygame.display.set_mode((400, 400))
pygame.display.set_caption("Music Player")

music_folder =r"C:\Users\User\OneDrive\Рабочий стол\ns_vs\lab_7\music_folder"
playlist = [f for f in os.listdir(music_folder) if f.endswith(".mp3")]
curr_track = 0

pygame.mixer.init()
if playlist:
    pygame.mixer.music.load(os.path.join(music_folder, playlist[curr_track]))

def play_music():
    pygame.mixer.music.play()

def stop_music():
    pygame.mixer.music.stop()

def next_track():
    global curr_track
    curr_track = (curr_track + 1) % len(playlist)
    pygame.mixer.music.load(os.path.join(music_folder, playlist[curr_track]))
    play_music()

def prev_track():
    global curr_track
    curr_track = (curr_track - 1) % len(playlist)
    pygame.mixer.music.load(os.path.join(music_folder, playlist[curr_track]))
    play_music()

running = True
while running:
    screen.fill((30, 30, 30))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                play_music()
            elif event.key == pygame.K_s:
                stop_music()
            elif event.key == pygame.K_d:
                next_track()
            elif event.key == pygame.K_a:
                prev_track()
    
    pygame.display.flip()

pygame.quit()