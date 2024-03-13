import ephem

def track_moon_phase(date):
    moon = ephem.Moon(date)
    moon_phase = ephem.phase_angle(ephem.Sun(), moon)
    if moon_phase < 0.5:
        return "New Moon"
    elif moon_phase < 1.5:
        return "First Quarter"
    elif moon_phase < 2.5:
        return "Full Moon"
    else:
        return "Last Quarter"

date = ephem.Date("2024/2/14")
phase = track_moon_phase(date)
print(f"Moon phase on {date}: {phase}")
