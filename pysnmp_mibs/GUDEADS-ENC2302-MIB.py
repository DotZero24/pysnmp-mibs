_l='enc2302DewPtDiffEvtSen'
_k='enc2302AirPressureEvtSen'
_j='enc2302InputEvtSen'
_i='enc2302HygroEvtSen'
_h='enc2302TempEvtSen'
_g='enc2302InputEvt'
_f='enc2302SwitchEvtPort'
_e='enc2302DewPoint'
_d='enc2302ActiveInputs'
_c='enc2302PortRepowerTime'
_b='enc2302PortStartupDelay'
_a='enc2302PortStartupMode'
_Z='enc2302portNumber'
_Y='enc2302TrapAddr'
_X='enc2302TrapCtrl'
_W='seconds'
_V='Unsigned32'
_U='enc2302DewPointDiff'
_T='enc2302AirPressure'
_S='enc2302InputSensor'
_R='enc2302HygroSensor'
_Q='enc2302TempSensor'
_P='enc2302Input'
_O='enc2302PortSwitchCount'
_N='enc2302PortState'
_M='enc2302PortName'
_L='0.1 degree Celsius'
_K='off'
_J='enc2302TrapIPIndex'
_I='OctetString'
_H='enc2302InputIndex'
_G='enc2302PortIndex'
_F='read-write'
_E='enc2302SensorIndex'
_D='Integer32'
_C='read-only'
_B='current'
_A='GUDEADS-ENC2302-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_I,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_V,'enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
gudeads=ModuleIdentity((1,3,6,1,4,1,28507))
if mibBuilder.loadTexts:gudeads.setRevisions(('2007-03-05 13:56',))
_GadsENC2302_ObjectIdentity=ObjectIdentity
gadsENC2302=_GadsENC2302_ObjectIdentity((1,3,6,1,4,1,28507,70))
_Enc2302Objects_ObjectIdentity=ObjectIdentity
enc2302Objects=_Enc2302Objects_ObjectIdentity((1,3,6,1,4,1,28507,70,1))
_Enc2302CommonConfig_ObjectIdentity=ObjectIdentity
enc2302CommonConfig=_Enc2302CommonConfig_ObjectIdentity((1,3,6,1,4,1,28507,70,1,1))
_Enc2302SNMPaccess_ObjectIdentity=ObjectIdentity
enc2302SNMPaccess=_Enc2302SNMPaccess_ObjectIdentity((1,3,6,1,4,1,28507,70,1,1,1))
class _Enc2302TrapCtrl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3))
_Enc2302TrapCtrl_Type.__name__=_D
_Enc2302TrapCtrl_Object=MibScalar
enc2302TrapCtrl=_Enc2302TrapCtrl_Object((1,3,6,1,4,1,28507,70,1,1,1,1),_Enc2302TrapCtrl_Type())
enc2302TrapCtrl.setMaxAccess(_F)
if mibBuilder.loadTexts:enc2302TrapCtrl.setStatus(_B)
_Enc2302TrapIPTable_Object=MibTable
enc2302TrapIPTable=_Enc2302TrapIPTable_Object((1,3,6,1,4,1,28507,70,1,1,1,2))
if mibBuilder.loadTexts:enc2302TrapIPTable.setStatus(_B)
_Enc2302TrapIPEntry_Object=MibTableRow
enc2302TrapIPEntry=_Enc2302TrapIPEntry_Object((1,3,6,1,4,1,28507,70,1,1,1,2,1))
enc2302TrapIPEntry.setIndexNames((0,_A,_J))
if mibBuilder.loadTexts:enc2302TrapIPEntry.setStatus(_B)
class _Enc2302TrapIPIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_Enc2302TrapIPIndex_Type.__name__=_D
_Enc2302TrapIPIndex_Object=MibTableColumn
enc2302TrapIPIndex=_Enc2302TrapIPIndex_Object((1,3,6,1,4,1,28507,70,1,1,1,2,1,1),_Enc2302TrapIPIndex_Type())
enc2302TrapIPIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:enc2302TrapIPIndex.setStatus(_B)
class _Enc2302TrapAddr_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,99))
_Enc2302TrapAddr_Type.__name__=_I
_Enc2302TrapAddr_Object=MibTableColumn
enc2302TrapAddr=_Enc2302TrapAddr_Object((1,3,6,1,4,1,28507,70,1,1,1,2,1,2),_Enc2302TrapAddr_Type())
enc2302TrapAddr.setMaxAccess(_F)
if mibBuilder.loadTexts:enc2302TrapAddr.setStatus(_B)
_Enc2302DeviceConfig_ObjectIdentity=ObjectIdentity
enc2302DeviceConfig=_Enc2302DeviceConfig_ObjectIdentity((1,3,6,1,4,1,28507,70,1,2))
_Enc2302IntActors_ObjectIdentity=ObjectIdentity
enc2302IntActors=_Enc2302IntActors_ObjectIdentity((1,3,6,1,4,1,28507,70,1,3))
_Enc2302relayports_ObjectIdentity=ObjectIdentity
enc2302relayports=_Enc2302relayports_ObjectIdentity((1,3,6,1,4,1,28507,70,1,3,1))
class _Enc2302portNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_Enc2302portNumber_Type.__name__=_D
_Enc2302portNumber_Object=MibScalar
enc2302portNumber=_Enc2302portNumber_Object((1,3,6,1,4,1,28507,70,1,3,1,1),_Enc2302portNumber_Type())
enc2302portNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:enc2302portNumber.setStatus(_B)
_Enc2302portTable_Object=MibTable
enc2302portTable=_Enc2302portTable_Object((1,3,6,1,4,1,28507,70,1,3,1,2))
if mibBuilder.loadTexts:enc2302portTable.setStatus(_B)
_Enc2302portEntry_Object=MibTableRow
enc2302portEntry=_Enc2302portEntry_Object((1,3,6,1,4,1,28507,70,1,3,1,2,1))
enc2302portEntry.setIndexNames((0,_A,_G))
if mibBuilder.loadTexts:enc2302portEntry.setStatus(_B)
class _Enc2302PortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_Enc2302PortIndex_Type.__name__=_D
_Enc2302PortIndex_Object=MibTableColumn
enc2302PortIndex=_Enc2302PortIndex_Object((1,3,6,1,4,1,28507,70,1,3,1,2,1,1),_Enc2302PortIndex_Type())
enc2302PortIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:enc2302PortIndex.setStatus(_B)
class _Enc2302PortName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_Enc2302PortName_Type.__name__=_I
_Enc2302PortName_Object=MibTableColumn
enc2302PortName=_Enc2302PortName_Object((1,3,6,1,4,1,28507,70,1,3,1,2,1,2),_Enc2302PortName_Type())
enc2302PortName.setMaxAccess(_F)
if mibBuilder.loadTexts:enc2302PortName.setStatus(_B)
class _Enc2302PortState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_K,0),('on',1)))
_Enc2302PortState_Type.__name__=_D
_Enc2302PortState_Object=MibTableColumn
enc2302PortState=_Enc2302PortState_Object((1,3,6,1,4,1,28507,70,1,3,1,2,1,3),_Enc2302PortState_Type())
enc2302PortState.setMaxAccess(_F)
if mibBuilder.loadTexts:enc2302PortState.setStatus(_B)
_Enc2302PortSwitchCount_Type=Integer32
_Enc2302PortSwitchCount_Object=MibTableColumn
enc2302PortSwitchCount=_Enc2302PortSwitchCount_Object((1,3,6,1,4,1,28507,70,1,3,1,2,1,4),_Enc2302PortSwitchCount_Type())
enc2302PortSwitchCount.setMaxAccess(_C)
if mibBuilder.loadTexts:enc2302PortSwitchCount.setStatus(_B)
class _Enc2302PortStartupMode_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_K,0),('on',1),('laststate',2)))
_Enc2302PortStartupMode_Type.__name__=_D
_Enc2302PortStartupMode_Object=MibTableColumn
enc2302PortStartupMode=_Enc2302PortStartupMode_Object((1,3,6,1,4,1,28507,70,1,3,1,2,1,5),_Enc2302PortStartupMode_Type())
enc2302PortStartupMode.setMaxAccess(_F)
if mibBuilder.loadTexts:enc2302PortStartupMode.setStatus(_B)
class _Enc2302PortStartupDelay_Type(Integer32):defaultValue=0
_Enc2302PortStartupDelay_Type.__name__=_D
_Enc2302PortStartupDelay_Object=MibTableColumn
enc2302PortStartupDelay=_Enc2302PortStartupDelay_Object((1,3,6,1,4,1,28507,70,1,3,1,2,1,6),_Enc2302PortStartupDelay_Type())
enc2302PortStartupDelay.setMaxAccess(_F)
if mibBuilder.loadTexts:enc2302PortStartupDelay.setStatus(_B)
if mibBuilder.loadTexts:enc2302PortStartupDelay.setUnits(_W)
class _Enc2302PortRepowerTime_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Enc2302PortRepowerTime_Type.__name__=_D
_Enc2302PortRepowerTime_Object=MibTableColumn
enc2302PortRepowerTime=_Enc2302PortRepowerTime_Object((1,3,6,1,4,1,28507,70,1,3,1,2,1,7),_Enc2302PortRepowerTime_Type())
enc2302PortRepowerTime.setMaxAccess(_F)
if mibBuilder.loadTexts:enc2302PortRepowerTime.setStatus(_B)
if mibBuilder.loadTexts:enc2302PortRepowerTime.setUnits(_W)
_Enc2302ExtActors_ObjectIdentity=ObjectIdentity
enc2302ExtActors=_Enc2302ExtActors_ObjectIdentity((1,3,6,1,4,1,28507,70,1,4))
_Enc2302IntSensors_ObjectIdentity=ObjectIdentity
enc2302IntSensors=_Enc2302IntSensors_ObjectIdentity((1,3,6,1,4,1,28507,70,1,5))
_Enc2302Inputs_ObjectIdentity=ObjectIdentity
enc2302Inputs=_Enc2302Inputs_ObjectIdentity((1,3,6,1,4,1,28507,70,1,5,6))
class _Enc2302ActiveInputs_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1))
_Enc2302ActiveInputs_Type.__name__=_V
_Enc2302ActiveInputs_Object=MibScalar
enc2302ActiveInputs=_Enc2302ActiveInputs_Object((1,3,6,1,4,1,28507,70,1,5,6,1),_Enc2302ActiveInputs_Type())
enc2302ActiveInputs.setMaxAccess(_C)
if mibBuilder.loadTexts:enc2302ActiveInputs.setStatus(_B)
_Enc2302InputTable_Object=MibTable
enc2302InputTable=_Enc2302InputTable_Object((1,3,6,1,4,1,28507,70,1,5,6,2))
if mibBuilder.loadTexts:enc2302InputTable.setStatus(_B)
_Enc2302InputEntry_Object=MibTableRow
enc2302InputEntry=_Enc2302InputEntry_Object((1,3,6,1,4,1,28507,70,1,5,6,2,1))
enc2302InputEntry.setIndexNames((0,_A,_H))
if mibBuilder.loadTexts:enc2302InputEntry.setStatus(_B)
class _Enc2302InputIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_Enc2302InputIndex_Type.__name__=_D
_Enc2302InputIndex_Object=MibTableColumn
enc2302InputIndex=_Enc2302InputIndex_Object((1,3,6,1,4,1,28507,70,1,5,6,2,1,1),_Enc2302InputIndex_Type())
enc2302InputIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:enc2302InputIndex.setStatus(_B)
class _Enc2302Input_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('lo',0),('hi',1)))
_Enc2302Input_Type.__name__=_D
_Enc2302Input_Object=MibTableColumn
enc2302Input=_Enc2302Input_Object((1,3,6,1,4,1,28507,70,1,5,6,2,1,2),_Enc2302Input_Type())
enc2302Input.setMaxAccess(_C)
if mibBuilder.loadTexts:enc2302Input.setStatus(_B)
_Enc2302ExtSensors_ObjectIdentity=ObjectIdentity
enc2302ExtSensors=_Enc2302ExtSensors_ObjectIdentity((1,3,6,1,4,1,28507,70,1,6))
_Enc2302SensorTable_Object=MibTable
enc2302SensorTable=_Enc2302SensorTable_Object((1,3,6,1,4,1,28507,70,1,6,1))
if mibBuilder.loadTexts:enc2302SensorTable.setStatus(_B)
_Enc2302SensorEntry_Object=MibTableRow
enc2302SensorEntry=_Enc2302SensorEntry_Object((1,3,6,1,4,1,28507,70,1,6,1,1))
enc2302SensorEntry.setIndexNames((0,_A,_E))
if mibBuilder.loadTexts:enc2302SensorEntry.setStatus(_B)
class _Enc2302SensorIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_Enc2302SensorIndex_Type.__name__=_D
_Enc2302SensorIndex_Object=MibTableColumn
enc2302SensorIndex=_Enc2302SensorIndex_Object((1,3,6,1,4,1,28507,70,1,6,1,1,1),_Enc2302SensorIndex_Type())
enc2302SensorIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:enc2302SensorIndex.setStatus(_B)
_Enc2302TempSensor_Type=Integer32
_Enc2302TempSensor_Object=MibTableColumn
enc2302TempSensor=_Enc2302TempSensor_Object((1,3,6,1,4,1,28507,70,1,6,1,1,2),_Enc2302TempSensor_Type())
enc2302TempSensor.setMaxAccess(_C)
if mibBuilder.loadTexts:enc2302TempSensor.setStatus(_B)
if mibBuilder.loadTexts:enc2302TempSensor.setUnits(_L)
_Enc2302HygroSensor_Type=Integer32
_Enc2302HygroSensor_Object=MibTableColumn
enc2302HygroSensor=_Enc2302HygroSensor_Object((1,3,6,1,4,1,28507,70,1,6,1,1,3),_Enc2302HygroSensor_Type())
enc2302HygroSensor.setMaxAccess(_C)
if mibBuilder.loadTexts:enc2302HygroSensor.setStatus(_B)
if mibBuilder.loadTexts:enc2302HygroSensor.setUnits('0.1 percent humidity')
class _Enc2302InputSensor_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_K,0),('on',1)))
_Enc2302InputSensor_Type.__name__=_D
_Enc2302InputSensor_Object=MibTableColumn
enc2302InputSensor=_Enc2302InputSensor_Object((1,3,6,1,4,1,28507,70,1,6,1,1,4),_Enc2302InputSensor_Type())
enc2302InputSensor.setMaxAccess(_C)
if mibBuilder.loadTexts:enc2302InputSensor.setStatus(_B)
_Enc2302AirPressure_Type=Integer32
_Enc2302AirPressure_Object=MibTableColumn
enc2302AirPressure=_Enc2302AirPressure_Object((1,3,6,1,4,1,28507,70,1,6,1,1,5),_Enc2302AirPressure_Type())
enc2302AirPressure.setMaxAccess(_C)
if mibBuilder.loadTexts:enc2302AirPressure.setStatus(_B)
if mibBuilder.loadTexts:enc2302AirPressure.setUnits('1 hPA (hectopascal) ~ 1 milibar')
_Enc2302DewPoint_Type=Integer32
_Enc2302DewPoint_Object=MibTableColumn
enc2302DewPoint=_Enc2302DewPoint_Object((1,3,6,1,4,1,28507,70,1,6,1,1,6),_Enc2302DewPoint_Type())
enc2302DewPoint.setMaxAccess(_C)
if mibBuilder.loadTexts:enc2302DewPoint.setStatus(_B)
if mibBuilder.loadTexts:enc2302DewPoint.setUnits(_L)
_Enc2302DewPointDiff_Type=Integer32
_Enc2302DewPointDiff_Object=MibTableColumn
enc2302DewPointDiff=_Enc2302DewPointDiff_Object((1,3,6,1,4,1,28507,70,1,6,1,1,7),_Enc2302DewPointDiff_Type())
enc2302DewPointDiff.setMaxAccess(_C)
if mibBuilder.loadTexts:enc2302DewPointDiff.setStatus(_B)
if mibBuilder.loadTexts:enc2302DewPointDiff.setUnits(_L)
_Enc2302Conf_ObjectIdentity=ObjectIdentity
enc2302Conf=_Enc2302Conf_ObjectIdentity((1,3,6,1,4,1,28507,70,2))
_Enc2302Groups_ObjectIdentity=ObjectIdentity
enc2302Groups=_Enc2302Groups_ObjectIdentity((1,3,6,1,4,1,28507,70,2,1))
_Enc2302Compls_ObjectIdentity=ObjectIdentity
enc2302Compls=_Enc2302Compls_ObjectIdentity((1,3,6,1,4,1,28507,70,2,2))
_Events_ObjectIdentity=ObjectIdentity
events=_Events_ObjectIdentity((1,3,6,1,4,1,28507,70,3))
enc2302BasicGroup=ObjectGroup((1,3,6,1,4,1,28507,70,2,1,1))
enc2302BasicGroup.setObjects(*((_A,_X),(_A,_J),(_A,_Y),(_A,_Z),(_A,_G),(_A,_M),(_A,_N),(_A,_O),(_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_H),(_A,_P),(_A,_E),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_e),(_A,_U)))
if mibBuilder.loadTexts:enc2302BasicGroup.setStatus(_B)
enc2302SwitchEvtPort=NotificationType((1,3,6,1,4,1,28507,70,3,1))
enc2302SwitchEvtPort.setObjects(*((_A,_G),(_A,_M),(_A,_N),(_A,_O)))
if mibBuilder.loadTexts:enc2302SwitchEvtPort.setStatus(_B)
enc2302InputEvt=NotificationType((1,3,6,1,4,1,28507,70,3,2))
enc2302InputEvt.setObjects(*((_A,_H),(_A,_P)))
if mibBuilder.loadTexts:enc2302InputEvt.setStatus(_B)
enc2302TempEvtSen=NotificationType((1,3,6,1,4,1,28507,70,3,3))
enc2302TempEvtSen.setObjects(*((_A,_E),(_A,_Q)))
if mibBuilder.loadTexts:enc2302TempEvtSen.setStatus(_B)
enc2302HygroEvtSen=NotificationType((1,3,6,1,4,1,28507,70,3,4))
enc2302HygroEvtSen.setObjects(*((_A,_E),(_A,_R)))
if mibBuilder.loadTexts:enc2302HygroEvtSen.setStatus(_B)
enc2302InputEvtSen=NotificationType((1,3,6,1,4,1,28507,70,3,5))
enc2302InputEvtSen.setObjects(*((_A,_E),(_A,_S)))
if mibBuilder.loadTexts:enc2302InputEvtSen.setStatus(_B)
enc2302AirPressureEvtSen=NotificationType((1,3,6,1,4,1,28507,70,3,6))
enc2302AirPressureEvtSen.setObjects(*((_A,_E),(_A,_T)))
if mibBuilder.loadTexts:enc2302AirPressureEvtSen.setStatus(_B)
enc2302DewPtDiffEvtSen=NotificationType((1,3,6,1,4,1,28507,70,3,7))
enc2302DewPtDiffEvtSen.setObjects(*((_A,_E),(_A,_U)))
if mibBuilder.loadTexts:enc2302DewPtDiffEvtSen.setStatus(_B)
enc2302NotificationGroup=NotificationGroup((1,3,6,1,4,1,28507,70,2,1,2))
enc2302NotificationGroup.setObjects(*((_A,_f),(_A,_g),(_A,_h),(_A,_i),(_A,_j),(_A,_k),(_A,_l)))
if mibBuilder.loadTexts:enc2302NotificationGroup.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'gudeads':gudeads,'gadsENC2302':gadsENC2302,'enc2302Objects':enc2302Objects,'enc2302CommonConfig':enc2302CommonConfig,'enc2302SNMPaccess':enc2302SNMPaccess,_X:enc2302TrapCtrl,'enc2302TrapIPTable':enc2302TrapIPTable,'enc2302TrapIPEntry':enc2302TrapIPEntry,_J:enc2302TrapIPIndex,_Y:enc2302TrapAddr,'enc2302DeviceConfig':enc2302DeviceConfig,'enc2302IntActors':enc2302IntActors,'enc2302relayports':enc2302relayports,_Z:enc2302portNumber,'enc2302portTable':enc2302portTable,'enc2302portEntry':enc2302portEntry,_G:enc2302PortIndex,_M:enc2302PortName,_N:enc2302PortState,_O:enc2302PortSwitchCount,_a:enc2302PortStartupMode,_b:enc2302PortStartupDelay,_c:enc2302PortRepowerTime,'enc2302ExtActors':enc2302ExtActors,'enc2302IntSensors':enc2302IntSensors,'enc2302Inputs':enc2302Inputs,_d:enc2302ActiveInputs,'enc2302InputTable':enc2302InputTable,'enc2302InputEntry':enc2302InputEntry,_H:enc2302InputIndex,_P:enc2302Input,'enc2302ExtSensors':enc2302ExtSensors,'enc2302SensorTable':enc2302SensorTable,'enc2302SensorEntry':enc2302SensorEntry,_E:enc2302SensorIndex,_Q:enc2302TempSensor,_R:enc2302HygroSensor,_S:enc2302InputSensor,_T:enc2302AirPressure,_e:enc2302DewPoint,_U:enc2302DewPointDiff,'enc2302Conf':enc2302Conf,'enc2302Groups':enc2302Groups,'enc2302BasicGroup':enc2302BasicGroup,'enc2302NotificationGroup':enc2302NotificationGroup,'enc2302Compls':enc2302Compls,'events':events,_f:enc2302SwitchEvtPort,_g:enc2302InputEvt,_h:enc2302TempEvtSen,_i:enc2302HygroEvtSen,_j:enc2302InputEvtSen,_k:enc2302AirPressureEvtSen,_l:enc2302DewPtDiffEvtSen})