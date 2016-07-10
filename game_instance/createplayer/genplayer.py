import cts2.game_instance.player.player as player
import cts2.game_instance.player.playstrength as playstrength
import cts2.database.nameinterface as nameinterface
from random import normalvariate, uniform

elo_fuzz_mu = 0
elo_fuzz_sigma = 25

def GenCountry():
    return nameinterface.GetRandomCountry()

def GenAge():
    return int(uniform(20,50))

def GenPlayStrength(age, default_options):
    strength = normalvariate(
        default_options["play_strength_mu"],
        default_options["play_strength_sigma"]
    )
    temp_play_strength = playstrength.playstrength(age, strength)
    return temp_play_strength

def GenElo(elo):
    elo_fuzz = normalvariate(elo_fuzz_mu, elo_fuzz_sigma)
    return elo + elo_fuzz

def GenGender():
    index = uniform(0,1)
    gender = ""

    if index <= .75:
        gender = "male"
    else:
        gender = "female"

    return gender

def GenFirstName(gender, country=""):
    return nameinterface.GetRandomFirst(gender, country)

def GenLastName(gender, country=""):
    return nameinterface.GetRandomLast(gender, country)

def GenPlayer(default_options):
    country = GenCountry()
    age = GenAge()
    play_strength = GenPlayStrength(age, default_options)
    elo = GenElo(play_strength.GetPlayStrength())
    gender = GenGender()
    first_name = GenFirstName(gender, country)
    last_name = GenLastName(gender, country)

    ret_player = player.player(
        first_name,
        last_name,
        age,
        gender = gender,
        country = country,
        elo = elo,
        play_strength = play_strength
    )

    return ret_player
