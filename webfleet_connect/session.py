from .credentials import Credentials
from .connection import Connection, Action
from .config import Config

def create(params = {}):
  credentials = Credentials(params)
  config = Config(params)
  session = Session(credentials, config)
  session.set_connection()
  return session

class Session:
  def __init__(self, credentials, config):
    self._credentials = credentials
    self._config = config

  def set_connection(self):
    self._connection = Connection(self)

  def has_json(self):
    return self._config.has_json()
  
  def _exec(self, action):
    return self._connection.exec(self._url(action))

  def _url(self, action):
    return f'{str(self._config)}&{str(self._credentials)}&{str(action)}'

  def create_queue_extern(self, args):
    return self._exec(Action('createQueueExtern', args))

  def delete_queue_extern(self, args):
    return self._exec(Action('deleteQueueExtern', args))

  def pop_queue_messages_extern(self, args):
    return self._exec(Action('popQueueMessagesExtern', args))

  def ack_queue_messages_extern(self, args):
    return self._exec(Action('ackQueueMessagesExtern', args))

  def show_object_report_extern(self, args = {}):
    return self._exec(Action('showObjectReportExtern', args))

  def show_vehicle_report_extern(self, args):
    return self._exec(Action('showVehicleReportExtern', args))

  def show_nearest_vehicles(self, args):
    return self._exec(Action('showNearestVehicles', args))

  def show_contracts(self, args):
    return self._exec(Action('showContracts', args))

  def update_vehicle(self, args):
    return self._exec(Action('updateVehicle', args))

  def show_object_groups(self, args):
    return self._exec(Action('showObjectGroups', args))

  def show_object_group_objects(self, args):
    return self._exec(Action('showObjectGroupObjects', args))

  def attach_object_to_group(self, args):
    return self._exec(Action('attachObjectToGroup', args))

  def detach_object_from_group(self, args):
    return self._exec(Action('detachObjectFromGroup', args))

  def insert_object_group(self, args):
    return self._exec(Action('insertObjectGroup', args))

  def delete_object_group(self, args):
    return self._exec(Action('deleteObjectGroup', args))

  def update_object_group(self, args):
    return self._exec(Action('updateObjectGroup', args))

  def switch_output(self, args):
    return self._exec(Action('switchOutput', args))

  def show_wakeup_timers(self, args):
    return self._exec(Action('showWakeupTimers', args))

  def update_wakeup_timers(self, args):
    return self._exec(Action('updateWakeupTimers', args))

  def get_object_features(self, args):
    return self._exec(Action('getObjectFeatures', args))

  def update_contract_info(self, args):
    return self._exec(Action('updateContractInfo', args))

  def get_object_can_signals(self, args):
    return self._exec(Action('getObjectCanSignals', args))

  def get_object_can_malfunctions(self, args):
    return self._exec(Action('getObjectCanMalfunctions', args))

  def get_electric_vehicle_data(self, args):
    return self._exec(Action('getElectricVehicleData', args))

  def get_active_asset_couplings(self, args):
    return self._exec(Action('getActiveAssetCouplings', args))

  def send_order_extern(self, args):
    return self._exec(Action('sendOrderExtern', args))

  def send_destination_order_extern(self, args):
    return self._exec(Action('sendDestinationOrderExtern', args))

  def update_order_extern(self, args):
    return self._exec(Action('updateOrderExtern', args))

  def update_destination_order_extern(self, args):
    return self._exec(Action('updateDestinationOrderExtern', args))

  def insert_destination_order_extern(self, args):
    return self._exec(Action('insertDestinationOrderExtern', args))

  def cancel_order_extern(self, args):
    return self._exec(Action('cancelOrderExtern', args))

  def assign_order_extern(self, args):
    return self._exec(Action('assignOrderExtern', args))

  def reassign_order_extern(self, args):
    return self._exec(Action('reassignOrderExtern', args))

  def delete_order_extern(self, args):
    return self._exec(Action('deleteOrderExtern', args))