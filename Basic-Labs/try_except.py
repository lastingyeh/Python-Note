def error():
	while True:

		try:
			val = int(eval(input("Enter an integer: ")))

			g = lambda x: x * 3 if x > 10 else "too low"

			if g(val) > 20:
				print("Lambda is", g(val))
				print("Input value is", val)
				break
			else:
				print("No output")
		except:
			print("Try again, Please")
			continue
		finally:
			print("End Code")

error()
