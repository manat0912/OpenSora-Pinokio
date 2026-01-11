import traceback
import sys
import os

print("--- Testing av import ---")
try:
    import av
    print(f"av version: {av.__version__}")
    print(f"av file: {av.__file__}")
except Exception:
    traceback.print_exc()

print("\n--- Testing opensora.datasets import ---")
try:
    from opensora.datasets import IMG_FPS
    print("Success: Imported IMG_FPS from opensora.datasets")
except Exception:
    traceback.print_exc()
