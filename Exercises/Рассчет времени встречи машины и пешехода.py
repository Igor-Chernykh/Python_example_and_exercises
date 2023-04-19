car_speed = 80
men_speed = 5
distance = 100
min_in_hour = 60
total_speed = car_speed + men_speed
time_hours = (distance // total_speed)
print(time_hours)
time_minutes = int(((distance % total_speed) / total_speed) * min_in_hour)
print(time_minutes)
print("They meet after", time_hours, "hour", time_minutes, "minutes")
