import zcatalyst_sdk as catalyst

class CheckUser:
    def __init__(self):
        pass

    def get_user(self, request):
        print(":: Inside ::")
        catalystApp = catalyst.initialize(req=request)
        username = request.form["username"]
        password = request.form["password"]
        result = catalystApp.zcql().execute_query(f"SELECT * FROM Users WHERE USERNAME = '{username}' AND PASSWORD = '{password}'")
        return result
