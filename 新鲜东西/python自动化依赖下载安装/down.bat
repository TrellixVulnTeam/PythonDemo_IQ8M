pip download -d spark-libs -r requirements.txt
pause

rem 使用下载命令

rem    pip download -d spark-libs -r requirements.txt

rem -d 后面跟的是下载的包存放目录

rem 4.2 批量安装 WHL 包
rem 比较简单，需要使用下载时用到的 requirements.txt，命令如下：

rem     pip install --no-index --find-links=d:\spark-libs -r requirements.txt

rem –find-links 后面跟的是存放 whl 包的路径。