import cts2.application.main.apphub as apphub


app = apphub.apphub()

while True:
    try:
        # app.DisplayFrame() --- make parallel
        app.GameLoop()
    except Exception as e:
        if e.message == "exit":
            break
        else:
            raise
