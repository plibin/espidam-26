import sys

def test_installation():
    print("\nTesting ESPIDAM environment installation...\n")
    
    success = True
    
    # 1. Test basic data science libraries
    try:
        import numpy as np
        import pandas as pd
        import matplotlib.pyplot as plt
        print("✅ Numpy, Pandas, Matplotlib imported successfully.")
    except ImportError as e:
        print(f"❌ Error importing basic libraries: {e}")
        success = False

    # 2. Test PyTorch
    try:
        import torch
        print(f"✅ PyTorch imported successfully (Version: {torch.__version__}).")
        print(f"   CUDA available: {torch.cuda.is_available()}")
    except ImportError as e:
        print(f"❌ Error importing PyTorch: {e}")
        success = False

    # 3. Test TensorFlow
    try:
        import tensorflow as tf
        import keras
        print(f"✅ TensorFlow imported successfully (Version: {tf.__version__}).")
    except ImportError as e:
        print(f"❌ Error importing TensorFlow: {e}")
        success = False

    # 4. Test Stable Baselines 3
    try:
        import stable_baselines3
        print(f"✅ Stable Baselines 3 imported successfully (Version: {stable_baselines3.__version__}).")
    except ImportError as e:
        print(f"❌ Error importing Stable Baselines 3: {e}")
        success = False

    # 5. Test Gymnasium and Box2D (The one that usually causes issues)
    try:
        import gymnasium as gym
        print(f"✅ Gymnasium imported successfully (Version: {gym.__version__}).")
        
        # Test if Box2D environment can be created (LunarLander uses Box2D)
        # Box2D is notoriously difficult to install and often causes issues
        env = gym.make("LunarLander-v2")
        env.reset()
        env.close()
        print("✅ Gymnasium Box2D (LunarLander) environment created successfully. Box2D is working!")
    except ImportError as e:
        print(f"❌ Error importing Gymnasium: {e}")
        success = False
    except Exception as e:
        print(f"❌ Error creating Box2D environment (this is often the problematic library!): {e}")
        success = False

    # 6. Test Jupyter Environment
    try:
        import jupyter_core
        import ipykernel
        print(f"✅ Jupyter environment (jupyter_core, ipykernel) imported successfully.")
    except ImportError as e:
        print(f"❌ Error importing Jupyter environment: {e}")
        success = False

    print("\n" + "="*50)
    if success:
        print("🎉 All tests passed! The environment is set up correctly.\n")
    else:
        print("⚠️ Some tests failed. Please check the errors above.\n")
        sys.exit(1)

if __name__ == "__main__":
    test_installation()
