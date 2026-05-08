[app]
title = SecretVault
package.name = secretvault
package.domain = org.secretvault

source.dir =.
source.include_exts = py,png,jpg,kv,atlas,ttf,json
version = 1.0

requirements = python3,kivy==2.3.0,cryptography

orientation = portrait
log_level = 2

fullscreen = 0

android.permissions = INTERNET
android.api = 33
android.minapi = 21
android.ndk = 23b
android.archs = arm64-v8a

p4a.branch = master

[buildozer]
warn_on_root = 1
