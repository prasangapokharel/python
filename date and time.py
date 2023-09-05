import pendulum

# Create timezones
utc = pendulum.timezone('UTC')
pst = pendulum.timezone('America/Los_Angeles')
ist = pendulum.timezone('Asia/Kathmandu')  # Note: 'Asia/Calcutta' is an old name; use 'Asia/Kolkata'

# Get current time in each timezone
utc_time = pendulum.now(utc)
pst_time = pendulum.now(pst)
ist_time = pendulum.now(ist)

# Print current time in each timezone
print(type(utc))
print('Current Date Time in UTC =', utc_time)
print('Current Date Time in PST =', pst_time)
print('Current Date Time in IST =', ist_time)
print(type(ist_time))

# Manipulate time
utc_time = utc_time.add(years=1)
utc_time = utc_time.subtract(months=2)

# Print manipulated time
print('Updated UTC Time', utc_time)
