[app]
title = SecretVault
package.name = secretvault
package.domain = org.example

source.dir =.
source.include_exts = py,png,jpg,kv,txt

version = 1.0

requirements = python3,kivy==2.3.0,sdl2,pyjnius,android

orientation = portrait

android.api = 33
android.minapi = 21
android.ndk = 23b
android.sdk_path = /home/runner/.buildozer/android/platform/android-sdk

android.archs = arm64-v8a

p4a.branch = master
