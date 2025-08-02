_g='epc1104DewPtDiffEvtSen'
_f='epc1104AirPressureEvtSen'
_e='epc1104InputEvtSen'
_d='epc1104HygroEvtSen'
_c='epc1104TempEvtSen'
_b='epc1104SwitchEvtPort'
_a='epc1104DewPoint'
_Z='epc1104PortRepowerTime'
_Y='epc1104PortStartupDelay'
_X='epc1104PortStartupMode'
_W='epc1104portNumber'
_V='epc1104TrapAddr'
_U='epc1104TrapCtrl'
_T='seconds'
_S='epc1104DewPointDiff'
_R='epc1104AirPressure'
_Q='epc1104InputSensor'
_P='epc1104HygroSensor'
_O='epc1104TempSensor'
_N='epc1104PortSwitchCount'
_M='epc1104PortState'
_L='epc1104PortName'
_K='0.1 degree Celsius'
_J='off'
_I='epc1104TrapIPIndex'
_H='OctetString'
_G='epc1104PortIndex'
_F='read-write'
_E='epc1104SensorIndex'
_D='read-only'
_C='Integer32'
_B='current'
_A='GUDEADS-EPC1104-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_H,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
gudeads=ModuleIdentity((1,3,6,1,4,1,28507))
if mibBuilder.loadTexts:gudeads.setRevisions(('2007-03-05 13:56',))
_GadsEPC1104_ObjectIdentity=ObjectIdentity
gadsEPC1104=_GadsEPC1104_ObjectIdentity((1,3,6,1,4,1,28507,68))
_Epc1104Objects_ObjectIdentity=ObjectIdentity
epc1104Objects=_Epc1104Objects_ObjectIdentity((1,3,6,1,4,1,28507,68,1))
_Epc1104CommonConfig_ObjectIdentity=ObjectIdentity
epc1104CommonConfig=_Epc1104CommonConfig_ObjectIdentity((1,3,6,1,4,1,28507,68,1,1))
_Epc1104SNMPaccess_ObjectIdentity=ObjectIdentity
epc1104SNMPaccess=_Epc1104SNMPaccess_ObjectIdentity((1,3,6,1,4,1,28507,68,1,1,1))
class _Epc1104TrapCtrl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3))
_Epc1104TrapCtrl_Type.__name__=_C
_Epc1104TrapCtrl_Object=MibScalar
epc1104TrapCtrl=_Epc1104TrapCtrl_Object((1,3,6,1,4,1,28507,68,1,1,1,1),_Epc1104TrapCtrl_Type())
epc1104TrapCtrl.setMaxAccess(_F)
if mibBuilder.loadTexts:epc1104TrapCtrl.setStatus(_B)
_Epc1104TrapIPTable_Object=MibTable
epc1104TrapIPTable=_Epc1104TrapIPTable_Object((1,3,6,1,4,1,28507,68,1,1,1,2))
if mibBuilder.loadTexts:epc1104TrapIPTable.setStatus(_B)
_Epc1104TrapIPEntry_Object=MibTableRow
epc1104TrapIPEntry=_Epc1104TrapIPEntry_Object((1,3,6,1,4,1,28507,68,1,1,1,2,1))
epc1104TrapIPEntry.setIndexNames((0,_A,_I))
if mibBuilder.loadTexts:epc1104TrapIPEntry.setStatus(_B)
class _Epc1104TrapIPIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_Epc1104TrapIPIndex_Type.__name__=_C
_Epc1104TrapIPIndex_Object=MibTableColumn
epc1104TrapIPIndex=_Epc1104TrapIPIndex_Object((1,3,6,1,4,1,28507,68,1,1,1,2,1,1),_Epc1104TrapIPIndex_Type())
epc1104TrapIPIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:epc1104TrapIPIndex.setStatus(_B)
class _Epc1104TrapAddr_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,99))
_Epc1104TrapAddr_Type.__name__=_H
_Epc1104TrapAddr_Object=MibTableColumn
epc1104TrapAddr=_Epc1104TrapAddr_Object((1,3,6,1,4,1,28507,68,1,1,1,2,1,2),_Epc1104TrapAddr_Type())
epc1104TrapAddr.setMaxAccess(_F)
if mibBuilder.loadTexts:epc1104TrapAddr.setStatus(_B)
_Epc1104DeviceConfig_ObjectIdentity=ObjectIdentity
epc1104DeviceConfig=_Epc1104DeviceConfig_ObjectIdentity((1,3,6,1,4,1,28507,68,1,2))
_Epc1104IntActors_ObjectIdentity=ObjectIdentity
epc1104IntActors=_Epc1104IntActors_ObjectIdentity((1,3,6,1,4,1,28507,68,1,3))
_Epc1104relayports_ObjectIdentity=ObjectIdentity
epc1104relayports=_Epc1104relayports_ObjectIdentity((1,3,6,1,4,1,28507,68,1,3,1))
class _Epc1104portNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1))
_Epc1104portNumber_Type.__name__=_C
_Epc1104portNumber_Object=MibScalar
epc1104portNumber=_Epc1104portNumber_Object((1,3,6,1,4,1,28507,68,1,3,1,1),_Epc1104portNumber_Type())
epc1104portNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:epc1104portNumber.setStatus(_B)
_Epc1104portTable_Object=MibTable
epc1104portTable=_Epc1104portTable_Object((1,3,6,1,4,1,28507,68,1,3,1,2))
if mibBuilder.loadTexts:epc1104portTable.setStatus(_B)
_Epc1104portEntry_Object=MibTableRow
epc1104portEntry=_Epc1104portEntry_Object((1,3,6,1,4,1,28507,68,1,3,1,2,1))
epc1104portEntry.setIndexNames((0,_A,_G))
if mibBuilder.loadTexts:epc1104portEntry.setStatus(_B)
class _Epc1104PortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1))
_Epc1104PortIndex_Type.__name__=_C
_Epc1104PortIndex_Object=MibTableColumn
epc1104PortIndex=_Epc1104PortIndex_Object((1,3,6,1,4,1,28507,68,1,3,1,2,1,1),_Epc1104PortIndex_Type())
epc1104PortIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:epc1104PortIndex.setStatus(_B)
class _Epc1104PortName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_Epc1104PortName_Type.__name__=_H
_Epc1104PortName_Object=MibTableColumn
epc1104PortName=_Epc1104PortName_Object((1,3,6,1,4,1,28507,68,1,3,1,2,1,2),_Epc1104PortName_Type())
epc1104PortName.setMaxAccess(_F)
if mibBuilder.loadTexts:epc1104PortName.setStatus(_B)
class _Epc1104PortState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_J,0),('on',1)))
_Epc1104PortState_Type.__name__=_C
_Epc1104PortState_Object=MibTableColumn
epc1104PortState=_Epc1104PortState_Object((1,3,6,1,4,1,28507,68,1,3,1,2,1,3),_Epc1104PortState_Type())
epc1104PortState.setMaxAccess(_F)
if mibBuilder.loadTexts:epc1104PortState.setStatus(_B)
_Epc1104PortSwitchCount_Type=Integer32
_Epc1104PortSwitchCount_Object=MibTableColumn
epc1104PortSwitchCount=_Epc1104PortSwitchCount_Object((1,3,6,1,4,1,28507,68,1,3,1,2,1,4),_Epc1104PortSwitchCount_Type())
epc1104PortSwitchCount.setMaxAccess(_D)
if mibBuilder.loadTexts:epc1104PortSwitchCount.setStatus(_B)
class _Epc1104PortStartupMode_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_J,0),('on',1),('laststate',2)))
_Epc1104PortStartupMode_Type.__name__=_C
_Epc1104PortStartupMode_Object=MibTableColumn
epc1104PortStartupMode=_Epc1104PortStartupMode_Object((1,3,6,1,4,1,28507,68,1,3,1,2,1,5),_Epc1104PortStartupMode_Type())
epc1104PortStartupMode.setMaxAccess(_F)
if mibBuilder.loadTexts:epc1104PortStartupMode.setStatus(_B)
class _Epc1104PortStartupDelay_Type(Integer32):defaultValue=0
_Epc1104PortStartupDelay_Type.__name__=_C
_Epc1104PortStartupDelay_Object=MibTableColumn
epc1104PortStartupDelay=_Epc1104PortStartupDelay_Object((1,3,6,1,4,1,28507,68,1,3,1,2,1,6),_Epc1104PortStartupDelay_Type())
epc1104PortStartupDelay.setMaxAccess(_F)
if mibBuilder.loadTexts:epc1104PortStartupDelay.setStatus(_B)
if mibBuilder.loadTexts:epc1104PortStartupDelay.setUnits(_T)
class _Epc1104PortRepowerTime_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Epc1104PortRepowerTime_Type.__name__=_C
_Epc1104PortRepowerTime_Object=MibTableColumn
epc1104PortRepowerTime=_Epc1104PortRepowerTime_Object((1,3,6,1,4,1,28507,68,1,3,1,2,1,7),_Epc1104PortRepowerTime_Type())
epc1104PortRepowerTime.setMaxAccess(_F)
if mibBuilder.loadTexts:epc1104PortRepowerTime.setStatus(_B)
if mibBuilder.loadTexts:epc1104PortRepowerTime.setUnits(_T)
_Epc1104ExtActors_ObjectIdentity=ObjectIdentity
epc1104ExtActors=_Epc1104ExtActors_ObjectIdentity((1,3,6,1,4,1,28507,68,1,4))
_Epc1104IntSensors_ObjectIdentity=ObjectIdentity
epc1104IntSensors=_Epc1104IntSensors_ObjectIdentity((1,3,6,1,4,1,28507,68,1,5))
_Epc1104ExtSensors_ObjectIdentity=ObjectIdentity
epc1104ExtSensors=_Epc1104ExtSensors_ObjectIdentity((1,3,6,1,4,1,28507,68,1,6))
_Epc1104SensorTable_Object=MibTable
epc1104SensorTable=_Epc1104SensorTable_Object((1,3,6,1,4,1,28507,68,1,6,1))
if mibBuilder.loadTexts:epc1104SensorTable.setStatus(_B)
_Epc1104SensorEntry_Object=MibTableRow
epc1104SensorEntry=_Epc1104SensorEntry_Object((1,3,6,1,4,1,28507,68,1,6,1,1))
epc1104SensorEntry.setIndexNames((0,_A,_E))
if mibBuilder.loadTexts:epc1104SensorEntry.setStatus(_B)
class _Epc1104SensorIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1))
_Epc1104SensorIndex_Type.__name__=_C
_Epc1104SensorIndex_Object=MibTableColumn
epc1104SensorIndex=_Epc1104SensorIndex_Object((1,3,6,1,4,1,28507,68,1,6,1,1,1),_Epc1104SensorIndex_Type())
epc1104SensorIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:epc1104SensorIndex.setStatus(_B)
_Epc1104TempSensor_Type=Integer32
_Epc1104TempSensor_Object=MibTableColumn
epc1104TempSensor=_Epc1104TempSensor_Object((1,3,6,1,4,1,28507,68,1,6,1,1,2),_Epc1104TempSensor_Type())
epc1104TempSensor.setMaxAccess(_D)
if mibBuilder.loadTexts:epc1104TempSensor.setStatus(_B)
if mibBuilder.loadTexts:epc1104TempSensor.setUnits(_K)
_Epc1104HygroSensor_Type=Integer32
_Epc1104HygroSensor_Object=MibTableColumn
epc1104HygroSensor=_Epc1104HygroSensor_Object((1,3,6,1,4,1,28507,68,1,6,1,1,3),_Epc1104HygroSensor_Type())
epc1104HygroSensor.setMaxAccess(_D)
if mibBuilder.loadTexts:epc1104HygroSensor.setStatus(_B)
if mibBuilder.loadTexts:epc1104HygroSensor.setUnits('0.1 percent humidity')
class _Epc1104InputSensor_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_J,0),('on',1)))
_Epc1104InputSensor_Type.__name__=_C
_Epc1104InputSensor_Object=MibTableColumn
epc1104InputSensor=_Epc1104InputSensor_Object((1,3,6,1,4,1,28507,68,1,6,1,1,4),_Epc1104InputSensor_Type())
epc1104InputSensor.setMaxAccess(_D)
if mibBuilder.loadTexts:epc1104InputSensor.setStatus(_B)
_Epc1104AirPressure_Type=Integer32
_Epc1104AirPressure_Object=MibTableColumn
epc1104AirPressure=_Epc1104AirPressure_Object((1,3,6,1,4,1,28507,68,1,6,1,1,5),_Epc1104AirPressure_Type())
epc1104AirPressure.setMaxAccess(_D)
if mibBuilder.loadTexts:epc1104AirPressure.setStatus(_B)
if mibBuilder.loadTexts:epc1104AirPressure.setUnits('1 hPA (hectopascal) ~ 1 milibar')
_Epc1104DewPoint_Type=Integer32
_Epc1104DewPoint_Object=MibTableColumn
epc1104DewPoint=_Epc1104DewPoint_Object((1,3,6,1,4,1,28507,68,1,6,1,1,6),_Epc1104DewPoint_Type())
epc1104DewPoint.setMaxAccess(_D)
if mibBuilder.loadTexts:epc1104DewPoint.setStatus(_B)
if mibBuilder.loadTexts:epc1104DewPoint.setUnits(_K)
_Epc1104DewPointDiff_Type=Integer32
_Epc1104DewPointDiff_Object=MibTableColumn
epc1104DewPointDiff=_Epc1104DewPointDiff_Object((1,3,6,1,4,1,28507,68,1,6,1,1,7),_Epc1104DewPointDiff_Type())
epc1104DewPointDiff.setMaxAccess(_D)
if mibBuilder.loadTexts:epc1104DewPointDiff.setStatus(_B)
if mibBuilder.loadTexts:epc1104DewPointDiff.setUnits(_K)
_Epc1104Conf_ObjectIdentity=ObjectIdentity
epc1104Conf=_Epc1104Conf_ObjectIdentity((1,3,6,1,4,1,28507,68,2))
_Epc1104Groups_ObjectIdentity=ObjectIdentity
epc1104Groups=_Epc1104Groups_ObjectIdentity((1,3,6,1,4,1,28507,68,2,1))
_Epc1104Compls_ObjectIdentity=ObjectIdentity
epc1104Compls=_Epc1104Compls_ObjectIdentity((1,3,6,1,4,1,28507,68,2,2))
_Events_ObjectIdentity=ObjectIdentity
events=_Events_ObjectIdentity((1,3,6,1,4,1,28507,68,3))
epc1104BasicGroup=ObjectGroup((1,3,6,1,4,1,28507,68,2,1,1))
epc1104BasicGroup.setObjects(*((_A,_U),(_A,_I),(_A,_V),(_A,_W),(_A,_G),(_A,_L),(_A,_M),(_A,_N),(_A,_X),(_A,_Y),(_A,_Z),(_A,_E),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_a),(_A,_S)))
if mibBuilder.loadTexts:epc1104BasicGroup.setStatus(_B)
epc1104SwitchEvtPort=NotificationType((1,3,6,1,4,1,28507,68,3,1))
epc1104SwitchEvtPort.setObjects(*((_A,_G),(_A,_L),(_A,_M),(_A,_N)))
if mibBuilder.loadTexts:epc1104SwitchEvtPort.setStatus(_B)
epc1104TempEvtSen=NotificationType((1,3,6,1,4,1,28507,68,3,2))
epc1104TempEvtSen.setObjects(*((_A,_E),(_A,_O)))
if mibBuilder.loadTexts:epc1104TempEvtSen.setStatus(_B)
epc1104HygroEvtSen=NotificationType((1,3,6,1,4,1,28507,68,3,3))
epc1104HygroEvtSen.setObjects(*((_A,_E),(_A,_P)))
if mibBuilder.loadTexts:epc1104HygroEvtSen.setStatus(_B)
epc1104InputEvtSen=NotificationType((1,3,6,1,4,1,28507,68,3,4))
epc1104InputEvtSen.setObjects(*((_A,_E),(_A,_Q)))
if mibBuilder.loadTexts:epc1104InputEvtSen.setStatus(_B)
epc1104AirPressureEvtSen=NotificationType((1,3,6,1,4,1,28507,68,3,5))
epc1104AirPressureEvtSen.setObjects(*((_A,_E),(_A,_R)))
if mibBuilder.loadTexts:epc1104AirPressureEvtSen.setStatus(_B)
epc1104DewPtDiffEvtSen=NotificationType((1,3,6,1,4,1,28507,68,3,6))
epc1104DewPtDiffEvtSen.setObjects(*((_A,_E),(_A,_S)))
if mibBuilder.loadTexts:epc1104DewPtDiffEvtSen.setStatus(_B)
epc1104NotificationGroup=NotificationGroup((1,3,6,1,4,1,28507,68,2,1,2))
epc1104NotificationGroup.setObjects(*((_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_g)))
if mibBuilder.loadTexts:epc1104NotificationGroup.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'gudeads':gudeads,'gadsEPC1104':gadsEPC1104,'epc1104Objects':epc1104Objects,'epc1104CommonConfig':epc1104CommonConfig,'epc1104SNMPaccess':epc1104SNMPaccess,_U:epc1104TrapCtrl,'epc1104TrapIPTable':epc1104TrapIPTable,'epc1104TrapIPEntry':epc1104TrapIPEntry,_I:epc1104TrapIPIndex,_V:epc1104TrapAddr,'epc1104DeviceConfig':epc1104DeviceConfig,'epc1104IntActors':epc1104IntActors,'epc1104relayports':epc1104relayports,_W:epc1104portNumber,'epc1104portTable':epc1104portTable,'epc1104portEntry':epc1104portEntry,_G:epc1104PortIndex,_L:epc1104PortName,_M:epc1104PortState,_N:epc1104PortSwitchCount,_X:epc1104PortStartupMode,_Y:epc1104PortStartupDelay,_Z:epc1104PortRepowerTime,'epc1104ExtActors':epc1104ExtActors,'epc1104IntSensors':epc1104IntSensors,'epc1104ExtSensors':epc1104ExtSensors,'epc1104SensorTable':epc1104SensorTable,'epc1104SensorEntry':epc1104SensorEntry,_E:epc1104SensorIndex,_O:epc1104TempSensor,_P:epc1104HygroSensor,_Q:epc1104InputSensor,_R:epc1104AirPressure,_a:epc1104DewPoint,_S:epc1104DewPointDiff,'epc1104Conf':epc1104Conf,'epc1104Groups':epc1104Groups,'epc1104BasicGroup':epc1104BasicGroup,'epc1104NotificationGroup':epc1104NotificationGroup,'epc1104Compls':epc1104Compls,'events':events,_b:epc1104SwitchEvtPort,_c:epc1104TempEvtSen,_d:epc1104HygroEvtSen,_e:epc1104InputEvtSen,_f:epc1104AirPressureEvtSen,_g:epc1104DewPtDiffEvtSen})