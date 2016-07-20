import cts2.application.main.apphub as apphub
import traceback


def main():
    try:
        app = apphub.apphub("cts2/application/packages")
    except:
        print "-"*60
        print "Package Load Error:"
        traceback.print_exc()
        print "-"*60
        raise

    while True:
        try:
            app.GameLoop()
        except Exception as e:
            if e.message == "exit":
                break
            else:
                raise


if __name__ == '__main__':
    main()
