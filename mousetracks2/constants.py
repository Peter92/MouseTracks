from enum import Enum, auto


class ThreadState(Enum):
    """Current state of the main thread being run from the GUI.

    Enums:
        Running: The thread is running and processing commands.
        Paused: The thread is running but ignoring commands.
        Stopped: The thread is not running.
    """

    Running = auto()
    Stopped = auto()
    Paused = auto()


class GUICommand(Enum):
    """Command sent from the GUI to the main thread.

    Enums:
        Start: Start the thread.
        Stop: Stop the thread.
        Pause: Pause the thread.
        Unpause: Unpause the thread.
        TogglePause: Toggle the paused state of the thread.
        RaiseException: Manually raise an exception in the thread.
            This is only meant to be used for debugging.
    """

    Start = auto()
    Stop = auto()
    Pause = auto()
    Unpause = auto()
    TogglePause = auto()
    RaiseException = auto()


class ThreadEvent(Enum):
    """Event from the main thread sent to the GUI.

    Enums:
        Started: After starting the thread.
        Stopped: Before safely exiting the thread.
        Paused: After pausing the thread.
        Unpaused: After unpausing the thread.
        Exception: Before an exception is raised.
            The thread will shut down if this occurrs.
        MouseMove: After moving the mouse.
            The purpose is for the GUI to update a preview image.
            Arguments:
                Tuple of mouse position coordinates.
                    Each coordinate is within a range of 0 to 1, where
                    (0, 0) is top left.
        MouseDistance: Distance the mouse has moved.
            Just for fun and will be removed later.
        MouseSpeed: Current speed of the mouse.
            Just for fun and will be removed later.
    """

    Started = auto()
    Stopped = auto()
    Paused = auto()
    Unpaused = auto()
    Exception = auto()
    MouseMove = auto()
    MouseDistance = auto()
    MouseSpeed = auto()


class ProcessCommand(Enum):
    """Command from the main thread sent to the processing thread.

    Enums:
        Pause: Forget certain settings when the thread is paused.
        Tick: Send each tick while the program is actively running.
            Arguments:
                int of total ticks.
        MonitorChanged: When different monitors are detected.
            Arguments:
                Tuple of monitor data in the format (x1, y1, x2, y2).
        MouseMove: When moving the mouse.
            Arguments:
                Tuple of mouse position coordinates.
                    Each coordinate is within a range of 0 to 1, where
                    (0, 0) is top left.
        KeyPressed: When a key is pressed.
            Arguments:
                Scan code of the key as an int.
                Number of times pressed in quick succession.
        KeyHeld: When a key is held down.
            Arguments:
                Scan code of the key as an int.
        KeyReleased: When a key is released.
            Arguments:
                Scan code of the key as an int.
        GamepadButtonPressed: When a gamepad button is pressed.
            Arguments:
                Index of controller.
                Name of the button.
                Number of times pressed in quick succession.
        GamepadButtonHeld: When a gamepad button is held down.
            Arguments:
                Index of controller.
                Name of the button.
        GamepadButtonReleased: When a gamepad button is released.
            Arguments:
                Index of controller.
                Name of the button.
        GamepadThumb(L/R): When a gamepad thumbstick is moved.
            Arguments:
                Index of controller.
                Tuple of thumbstick coordinates.
        GamepadTrigger(L/R): When a gamepad trigger is moved.
            Arguments:
                Index of controller.
                Value of trigger.
    """
    Pause = auto()
    Tick = auto()
    MonitorChanged = auto()
    MouseMove = auto()
    KeyPressed = auto()
    KeyHeld = auto()
    KeyReleased = auto()
    GamepadButtonPressed = auto()
    GamepadButtonHeld = auto()
    GamepadButtonReleased = auto()
    GamepadThumbL = auto()
    GamepadThumbR = auto()
    GamepadTriggerL = auto()
    GamepadTriggerR = auto()


class ProcessEvent(Enum):
    """Event from the processing thread sent to the main thread.

    Error: Stop execution if an exception occurred.
    MouseDistance: The distance calculated from the mouse movement.
    """
    Error = auto()
    MouseDistance = auto()