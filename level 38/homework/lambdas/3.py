text = "Spot of come to ever hand as lady meet on. Delicate contempt received two yet advanced. Gentleman as belonging he commanded believing dejection in by."

text = text.split()

filtered = list(filter(lambda x: len(x)>4,text))
filtered = " ".join(filtered)

print(filtered)