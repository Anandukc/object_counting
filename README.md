# Object counting using ultralytics

This project utilizes Ultralytics to perform object counting, incorporating advanced tracking algorithms for enhanced accuracy and efficiency. The supported tracking algorithms include BOTSORT and BYTETRACK.



## Features

- Object counting using state-of-the-art deep learning models
- Counts object moving in and out
- Flexible configuration options for model customization
- Object tracking for improved accuracy and robustness
- Support for BOTSORT and BYTETRACK algorithms



## Installation

- Create a virtual environment: (recommended)

Linux/macOS:

```bash
  # Create a virtual environment
    python3 -m venv venv

  # Activate the virtual environment
    source venv/bin/activate
  
```

 Windows:

```powershell
  # Create a virtual environment
    python -m venv venv

  # Activate the virtual environment
    venv\Scripts\activate
  
```

- Clone the repository:


```bash
  git clone https://github.com/Anandukc/object_counting.git
```





- Install ultralytics:
note: Install the latest version

```bash
  pip install ultralytics
```

- Set the video path

  Modify the line ``` 
  cap = cv2.VideoCapture("path to input image")" ``` in the detect.py file to the path of ```bottle.mp4```

- Run the script:

```bash
  python detect.py
```
  
  note: users can set the classes of object they want to detect by using the argument classes=[0,1,2]



## output result

