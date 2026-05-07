[app]
title = SecretVault
package.name = secretvault
package.domain = org.vault

source.dir = .
source.include_exts = py,png,jpg,kv,json

version = 1.0

requirements = python3,kivy==2.3.1

orientation = portrait
fullscreen = 0

android.permissions = INTERNET,VIBRATE

android.api = 33
android.minapi = 21
android.archs = arm64-v8a,armeabi-v7a

android.build_tools_version = 33.0.2
android.accept_sdk_license = True


[buildozer]
log_level = 2
warn_on_root = 1
