"""
当你要安装很多插件的时候是不是很头疼，快试试这个，解放双手
"""
import os
import time

# 主需要把要安装的插件名称统一粘贴过来，循环一波即可
string_ = "bdw-gc, libffi, m4, libtool, libunistring, pkg-config, readline, guile, gettext, libidn2, libtasn1, " \
          "nettle, p11-kit, openssl@1.1, libevent, libnghttp2, unbound, gnutls, lame, fribidi, pcre, gdbm, mpdecimal, " \
          "sqlite, xz, python@3.9, glib, libpthread-stubs, xorgproto, libxau, libxdmcp, libxcb, libx11, libxext, " \
          "libxrender, lzo, pixman, cairo, gobject-introspection, graphite2, icu4c, harfbuzz, libass, libbluray, " \
          "cjson, cmocka, mbedtls, librist, libsoxr, libvidstab, libogg, libvorbis, libvpx, opencore-amr, " \
          "little-cms2, openjpeg, opus, rav1e, flac, libsndfile, libsamplerate, rubberband, sdl2, snappy, speex, srt, " \
          "leptonica, libb2, lz4, zstd, libarchive, tesseract, theora, x264, x265, xvid, libsodium, zeromq, zimg , " \
          "ffmpeg "

list = string_.split(",")  # 按照符号把字符串分割放入列表里
print(list)
for n in list:
    print("*"*100)
    print(n, "安装中")
    os.system("brew install {}".format(n))
    print(n, "安装结束，继续下一个")
    time.sleep(0.5)
