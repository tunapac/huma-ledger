[app]
# (str) Title of your application
title = Tunapac DNA Hub

# (str) Package name
package.name = humanledger

# (str) Package domain (needed for android packaging)
package.domain = com.tunapac.hub

# (str) Source code where the main.py lives
source.dir = .

# (list) Source files to include (let's include everything)
source.include_exts = py,png,jpg,kv,atlas,json

# (str) Application version
version = 1.0.0

# (list) Application requirements
requirements = python3,kivy,requests,certifi

# (list) Permissions for POH, 629 Biometrics, and Sovereign Storage
android.permissions = INTERNET, CAMERA, BIOMETRIC, USE_FINGERPRINT, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE

# --- TECHNICAL SPECS (CRITICAL FIX FOR AIDL ERROR) ---
android.api = 34
android.minapi = 21
android.sdk = 34
android.ndk = 25b
android.build_tools_version = 34.0.0

# (str) Android logcat filters
android.logcat_filters = *:S python:D

# (str) The orientation
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 1

# (list) The Android architectures to build for
android.archs = arm64-v8a, armeabi-v7a

[buildozer]
# (int) Log level (2 = maximum information)
log_level = 2

# (int) Display warning if buildozer is run as root (1 = yes)
warn_on_root = 1


