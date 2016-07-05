import cts2.application.main.packagelisting as pl
import cts2.application.main.apphub as apphub


path_to_app_packages = "cts2/application/packages"
py_path_to_app_packages = path_to_app_packages.replace("/", ".")
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

while True:
    try:
        app.GameLoop()
    except Exception as e:
        if e.message == "exit":
            break
        else:
            raise
