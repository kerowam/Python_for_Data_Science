def NULL_not_found(object: any)-> int:
	object_type = type(object)

	try:
		match object:
			case None:
				print(f"Nothing : {object} {object_type}")
				return 0
			case float() if str(object) == "nan":
				print(f"Cheese : {object} {object_type}")
				return 0
			case 0:
				print(f"Zero : {object} {object_type}")
				return 0
			case '' :
				print(f"Empty : {object} {object_type}")
				return 0
			case False :
				print(f"Fake : {object} {object_type}")
				return 0
			case _:
				print("Type not found")
				return 1
		
	except Exception as e:
		print(e)
	return 1