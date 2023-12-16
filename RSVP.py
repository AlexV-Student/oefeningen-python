 # file -> list of dicts

# file inlezen
with open("logfile.txt", "r") as f:
  lines = f.readlines()

# lijnen opsplitsen in datum, uur, proces, info
lines = [line.split(':.') for line in lines]
for i, line in enumerate(lines):
  if len(line) > 1:
    tmp = line[0].strip().split(" ")
    lines[i] = {"date": tmp[0], "hour": tmp[1], "type": tmp[2], "text": line[1].strip()}
  else:
    lines[i] = {"date": None, "hour": None, "type": "BLOCK", "text": line[0].strip()}

# voorbeelden
print(lines[0])
print(lines[20])

# RSVP Agent opgestart:
datum = lines[1]["date"]
uur = lines[1]["hour"]
print(f"De agent werd op {datum} opgestart om {uur}")

# RSVP Agent afgesloten:
datum = lines[-1]["date"]
uur = lines[-1]["hour"]
print(f"De agent werd op {datum} afgesloten om {uur}")


# lijst met events
events = [line for line in lines if line["type"].lower() == "event"]
for event in events:
  print(event["date"], event["hour"], event["type"] + ":", event["text"])