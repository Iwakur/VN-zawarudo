# Function to play a sound while text is being displayed.
init python:
    from functools import partial

    def dialogue_blip(event, interact=True, sound_file=None, **kwargs):
        if event == "show":
            renpy.sound.play(sound_file, channel="sound", loop=True)
        elif event == "slow_done" or event == "end":
            renpy.sound.stop(channel="sound")


define e = Character(
    "Eileen",
    color="#c8ffc8",
    callback=partial(dialogue_blip, sound_file="audio/sfx/beeps/eileen.ogg"),
    what_slow_cps=35
)

define r = Character(
    "Rika",
    color="#ffc8e8",
    callback=partial(dialogue_blip, sound_file="audio/sfx/beeps/rika.ogg"),
    what_slow_cps=50
)

define m = Character(
    "Mysterious Voice",
    color="#c8d8ff",
    callback=partial(dialogue_blip, sound_file="audio/sfx/beeps/mysterious.ogg"),
    what_slow_cps=20
)

default current_map = "start"

label start:


    scene bg room


    e "This is Eileen talking."
    r "This is Rika talking faster."
    m "This voice talks slowly."

    return
