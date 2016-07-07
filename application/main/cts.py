import cts2.application.main.packagelisting as pl
import cts2.application.main.apphub as apphub
import traceback


path_to_app_packages = "cts2/application/packages"
py_path_to_app_packages = path_to_app_packages.replace("/", ".")
try:
    app = apphub.apphub(
        [
            ".".join(
                [
                    py_path_to_app_packages,
                    pkg,
                    pkg + "handler",
                    pkg + "handler"
                ]
            ) for pkg in pl.ListPackages(
                path_to_app_packages
            )
        ]
    )
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
