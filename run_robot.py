from pyrobot.robot import PyRobot
from config import client_id, redirect_uri, credentials_path
# Initialize robot
trading_robot = PyRobot(
    client_id=client_id,
    redirect_uri=redirect_uri,
    credentials_path=credentials_path
)