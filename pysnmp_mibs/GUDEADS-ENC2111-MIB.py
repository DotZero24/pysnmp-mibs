_q='enc2111POEEvt'
_p='enc2111DewPtDiffEvtSen'
_o='enc2111AirPressureEvtSen'
_n='enc2111InputEvtSen'
_m='enc2111HygroEvtSen'
_l='enc2111TempEvtSen'
_k='enc2111InputEvt'
_j='enc2111SwitchEvtPort'
_i='enc2111DewPoint'
_h='enc2111State3V'
_g='enc2111State12V'
_f='enc2111ActiveInputs'
_e='enc2111PortRepowerTime'
_d='enc2111PortStartupDelay'
_c='enc2111PortStartupMode'
_b='enc2111portNumber'
_a='enc2111TrapAddr'
_Z='enc2111TrapCtrl'
_Y='seconds'
_X='Unsigned32'
_W='enc2111DewPointDiff'
_V='enc2111AirPressure'
_U='enc2111InputSensor'
_T='enc2111HygroSensor'
_S='enc2111TempSensor'
_R='enc2111POE'
_Q='enc2111Input'
_P='enc2111PortSwitchCount'
_O='enc2111PortState'
_N='enc2111PortName'
_M='0.1 degree Celsius'
_L='enc2111TrapIPIndex'
_K='OctetString'
_J='enc2111InputIndex'
_I='on'
_H='off'
_G='enc2111PortIndex'
_F='read-write'
_E='enc2111SensorIndex'
_D='Integer32'
_C='read-only'
_B='current'
_A='GUDEADS-ENC2111-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_K,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_X,'enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
gudeads=ModuleIdentity((1,3,6,1,4,1,28507))
if mibBuilder.loadTexts:gudeads.setRevisions(('2007-03-05 13:56',))
_GadsENC2111_ObjectIdentity=ObjectIdentity
gadsENC2111=_GadsENC2111_ObjectIdentity((1,3,6,1,4,1,28507,60))
_Enc2111Objects_ObjectIdentity=ObjectIdentity
enc2111Objects=_Enc2111Objects_ObjectIdentity((1,3,6,1,4,1,28507,60,1))
_Enc2111CommonConfig_ObjectIdentity=ObjectIdentity
enc2111CommonConfig=_Enc2111CommonConfig_ObjectIdentity((1,3,6,1,4,1,28507,60,1,1))
_Enc2111SNMPaccess_ObjectIdentity=ObjectIdentity
enc2111SNMPaccess=_Enc2111SNMPaccess_ObjectIdentity((1,3,6,1,4,1,28507,60,1,1,1))
class _Enc2111TrapCtrl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3))
_Enc2111TrapCtrl_Type.__name__=_D
_Enc2111TrapCtrl_Object=MibScalar
enc2111TrapCtrl=_Enc2111TrapCtrl_Object((1,3,6,1,4,1,28507,60,1,1,1,1),_Enc2111TrapCtrl_Type())
enc2111TrapCtrl.setMaxAccess(_F)
if mibBuilder.loadTexts:enc2111TrapCtrl.setStatus(_B)
_Enc2111TrapIPTable_Object=MibTable
enc2111TrapIPTable=_Enc2111TrapIPTable_Object((1,3,6,1,4,1,28507,60,1,1,1,2))
if mibBuilder.loadTexts:enc2111TrapIPTable.setStatus(_B)
_Enc2111TrapIPEntry_Object=MibTableRow
enc2111TrapIPEntry=_Enc2111TrapIPEntry_Object((1,3,6,1,4,1,28507,60,1,1,1,2,1))
enc2111TrapIPEntry.setIndexNames((0,_A,_L))
if mibBuilder.loadTexts:enc2111TrapIPEntry.setStatus(_B)
class _Enc2111TrapIPIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_Enc2111TrapIPIndex_Type.__name__=_D
_Enc2111TrapIPIndex_Object=MibTableColumn
enc2111TrapIPIndex=_Enc2111TrapIPIndex_Object((1,3,6,1,4,1,28507,60,1,1,1,2,1,1),_Enc2111TrapIPIndex_Type())
enc2111TrapIPIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:enc2111TrapIPIndex.setStatus(_B)
class _Enc2111TrapAddr_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,99))
_Enc2111TrapAddr_Type.__name__=_K
_Enc2111TrapAddr_Object=MibTableColumn
enc2111TrapAddr=_Enc2111TrapAddr_Object((1,3,6,1,4,1,28507,60,1,1,1,2,1,2),_Enc2111TrapAddr_Type())
enc2111TrapAddr.setMaxAccess(_F)
if mibBuilder.loadTexts:enc2111TrapAddr.setStatus(_B)
_Enc2111DeviceConfig_ObjectIdentity=ObjectIdentity
enc2111DeviceConfig=_Enc2111DeviceConfig_ObjectIdentity((1,3,6,1,4,1,28507,60,1,2))
_Enc2111IntActors_ObjectIdentity=ObjectIdentity
enc2111IntActors=_Enc2111IntActors_ObjectIdentity((1,3,6,1,4,1,28507,60,1,3))
_Enc2111relayports_ObjectIdentity=ObjectIdentity
enc2111relayports=_Enc2111relayports_ObjectIdentity((1,3,6,1,4,1,28507,60,1,3,1))
class _Enc2111portNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,12))
_Enc2111portNumber_Type.__name__=_D
_Enc2111portNumber_Object=MibScalar
enc2111portNumber=_Enc2111portNumber_Object((1,3,6,1,4,1,28507,60,1,3,1,1),_Enc2111portNumber_Type())
enc2111portNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:enc2111portNumber.setStatus(_B)
_Enc2111portTable_Object=MibTable
enc2111portTable=_Enc2111portTable_Object((1,3,6,1,4,1,28507,60,1,3,1,2))
if mibBuilder.loadTexts:enc2111portTable.setStatus(_B)
_Enc2111portEntry_Object=MibTableRow
enc2111portEntry=_Enc2111portEntry_Object((1,3,6,1,4,1,28507,60,1,3,1,2,1))
enc2111portEntry.setIndexNames((0,_A,_G))
if mibBuilder.loadTexts:enc2111portEntry.setStatus(_B)
class _Enc2111PortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_Enc2111PortIndex_Type.__name__=_D
_Enc2111PortIndex_Object=MibTableColumn
enc2111PortIndex=_Enc2111PortIndex_Object((1,3,6,1,4,1,28507,60,1,3,1,2,1,1),_Enc2111PortIndex_Type())
enc2111PortIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:enc2111PortIndex.setStatus(_B)
class _Enc2111PortName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_Enc2111PortName_Type.__name__=_K
_Enc2111PortName_Object=MibTableColumn
enc2111PortName=_Enc2111PortName_Object((1,3,6,1,4,1,28507,60,1,3,1,2,1,2),_Enc2111PortName_Type())
enc2111PortName.setMaxAccess(_F)
if mibBuilder.loadTexts:enc2111PortName.setStatus(_B)
class _Enc2111PortState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_H,0),(_I,1)))
_Enc2111PortState_Type.__name__=_D
_Enc2111PortState_Object=MibTableColumn
enc2111PortState=_Enc2111PortState_Object((1,3,6,1,4,1,28507,60,1,3,1,2,1,3),_Enc2111PortState_Type())
enc2111PortState.setMaxAccess(_F)
if mibBuilder.loadTexts:enc2111PortState.setStatus(_B)
_Enc2111PortSwitchCount_Type=Integer32
_Enc2111PortSwitchCount_Object=MibTableColumn
enc2111PortSwitchCount=_Enc2111PortSwitchCount_Object((1,3,6,1,4,1,28507,60,1,3,1,2,1,4),_Enc2111PortSwitchCount_Type())
enc2111PortSwitchCount.setMaxAccess(_C)
if mibBuilder.loadTexts:enc2111PortSwitchCount.setStatus(_B)
class _Enc2111PortStartupMode_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_H,0),(_I,1),('laststate',2)))
_Enc2111PortStartupMode_Type.__name__=_D
_Enc2111PortStartupMode_Object=MibTableColumn
enc2111PortStartupMode=_Enc2111PortStartupMode_Object((1,3,6,1,4,1,28507,60,1,3,1,2,1,5),_Enc2111PortStartupMode_Type())
enc2111PortStartupMode.setMaxAccess(_F)
if mibBuilder.loadTexts:enc2111PortStartupMode.setStatus(_B)
class _Enc2111PortStartupDelay_Type(Integer32):defaultValue=0
_Enc2111PortStartupDelay_Type.__name__=_D
_Enc2111PortStartupDelay_Object=MibTableColumn
enc2111PortStartupDelay=_Enc2111PortStartupDelay_Object((1,3,6,1,4,1,28507,60,1,3,1,2,1,6),_Enc2111PortStartupDelay_Type())
enc2111PortStartupDelay.setMaxAccess(_F)
if mibBuilder.loadTexts:enc2111PortStartupDelay.setStatus(_B)
if mibBuilder.loadTexts:enc2111PortStartupDelay.setUnits(_Y)
class _Enc2111PortRepowerTime_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Enc2111PortRepowerTime_Type.__name__=_D
_Enc2111PortRepowerTime_Object=MibTableColumn
enc2111PortRepowerTime=_Enc2111PortRepowerTime_Object((1,3,6,1,4,1,28507,60,1,3,1,2,1,7),_Enc2111PortRepowerTime_Type())
enc2111PortRepowerTime.setMaxAccess(_F)
if mibBuilder.loadTexts:enc2111PortRepowerTime.setStatus(_B)
if mibBuilder.loadTexts:enc2111PortRepowerTime.setUnits(_Y)
_Enc2111ExtActors_ObjectIdentity=ObjectIdentity
enc2111ExtActors=_Enc2111ExtActors_ObjectIdentity((1,3,6,1,4,1,28507,60,1,4))
_Enc2111IntSensors_ObjectIdentity=ObjectIdentity
enc2111IntSensors=_Enc2111IntSensors_ObjectIdentity((1,3,6,1,4,1,28507,60,1,5))
_Enc2111Inputs_ObjectIdentity=ObjectIdentity
enc2111Inputs=_Enc2111Inputs_ObjectIdentity((1,3,6,1,4,1,28507,60,1,5,6))
class _Enc2111ActiveInputs_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,12))
_Enc2111ActiveInputs_Type.__name__=_X
_Enc2111ActiveInputs_Object=MibScalar
enc2111ActiveInputs=_Enc2111ActiveInputs_Object((1,3,6,1,4,1,28507,60,1,5,6,1),_Enc2111ActiveInputs_Type())
enc2111ActiveInputs.setMaxAccess(_C)
if mibBuilder.loadTexts:enc2111ActiveInputs.setStatus(_B)
_Enc2111InputTable_Object=MibTable
enc2111InputTable=_Enc2111InputTable_Object((1,3,6,1,4,1,28507,60,1,5,6,2))
if mibBuilder.loadTexts:enc2111InputTable.setStatus(_B)
_Enc2111InputEntry_Object=MibTableRow
enc2111InputEntry=_Enc2111InputEntry_Object((1,3,6,1,4,1,28507,60,1,5,6,2,1))
enc2111InputEntry.setIndexNames((0,_A,_J))
if mibBuilder.loadTexts:enc2111InputEntry.setStatus(_B)
class _Enc2111InputIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,12))
_Enc2111InputIndex_Type.__name__=_D
_Enc2111InputIndex_Object=MibTableColumn
enc2111InputIndex=_Enc2111InputIndex_Object((1,3,6,1,4,1,28507,60,1,5,6,2,1,1),_Enc2111InputIndex_Type())
enc2111InputIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:enc2111InputIndex.setStatus(_B)
class _Enc2111Input_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('lo',0),('hi',1)))
_Enc2111Input_Type.__name__=_D
_Enc2111Input_Object=MibTableColumn
enc2111Input=_Enc2111Input_Object((1,3,6,1,4,1,28507,60,1,5,6,2,1,2),_Enc2111Input_Type())
enc2111Input.setMaxAccess(_C)
if mibBuilder.loadTexts:enc2111Input.setStatus(_B)
_Enc2111VoltageInfo_ObjectIdentity=ObjectIdentity
enc2111VoltageInfo=_Enc2111VoltageInfo_ObjectIdentity((1,3,6,1,4,1,28507,60,1,5,7))
class _Enc2111State12V_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_H,0),('low',1),('high',2),('error',3)))
_Enc2111State12V_Type.__name__=_D
_Enc2111State12V_Object=MibScalar
enc2111State12V=_Enc2111State12V_Object((1,3,6,1,4,1,28507,60,1,5,7,1),_Enc2111State12V_Type())
enc2111State12V.setMaxAccess(_C)
if mibBuilder.loadTexts:enc2111State12V.setStatus(_B)
class _Enc2111State3V_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,3)));namedValues=NamedValues(*((_I,1),('error',3)))
_Enc2111State3V_Type.__name__=_D
_Enc2111State3V_Object=MibScalar
enc2111State3V=_Enc2111State3V_Object((1,3,6,1,4,1,28507,60,1,5,7,2),_Enc2111State3V_Type())
enc2111State3V.setMaxAccess(_C)
if mibBuilder.loadTexts:enc2111State3V.setStatus(_B)
class _Enc2111POE_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Enc2111POE_Type.__name__=_D
_Enc2111POE_Object=MibScalar
enc2111POE=_Enc2111POE_Object((1,3,6,1,4,1,28507,60,1,5,10),_Enc2111POE_Type())
enc2111POE.setMaxAccess(_C)
if mibBuilder.loadTexts:enc2111POE.setStatus(_B)
if mibBuilder.loadTexts:enc2111POE.setUnits('0 = no POE, 1 = POE available')
_Enc2111ExtSensors_ObjectIdentity=ObjectIdentity
enc2111ExtSensors=_Enc2111ExtSensors_ObjectIdentity((1,3,6,1,4,1,28507,60,1,6))
_Enc2111SensorTable_Object=MibTable
enc2111SensorTable=_Enc2111SensorTable_Object((1,3,6,1,4,1,28507,60,1,6,1))
if mibBuilder.loadTexts:enc2111SensorTable.setStatus(_B)
_Enc2111SensorEntry_Object=MibTableRow
enc2111SensorEntry=_Enc2111SensorEntry_Object((1,3,6,1,4,1,28507,60,1,6,1,1))
enc2111SensorEntry.setIndexNames((0,_A,_E))
if mibBuilder.loadTexts:enc2111SensorEntry.setStatus(_B)
class _Enc2111SensorIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_Enc2111SensorIndex_Type.__name__=_D
_Enc2111SensorIndex_Object=MibTableColumn
enc2111SensorIndex=_Enc2111SensorIndex_Object((1,3,6,1,4,1,28507,60,1,6,1,1,1),_Enc2111SensorIndex_Type())
enc2111SensorIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:enc2111SensorIndex.setStatus(_B)
_Enc2111TempSensor_Type=Integer32
_Enc2111TempSensor_Object=MibTableColumn
enc2111TempSensor=_Enc2111TempSensor_Object((1,3,6,1,4,1,28507,60,1,6,1,1,2),_Enc2111TempSensor_Type())
enc2111TempSensor.setMaxAccess(_C)
if mibBuilder.loadTexts:enc2111TempSensor.setStatus(_B)
if mibBuilder.loadTexts:enc2111TempSensor.setUnits(_M)
_Enc2111HygroSensor_Type=Integer32
_Enc2111HygroSensor_Object=MibTableColumn
enc2111HygroSensor=_Enc2111HygroSensor_Object((1,3,6,1,4,1,28507,60,1,6,1,1,3),_Enc2111HygroSensor_Type())
enc2111HygroSensor.setMaxAccess(_C)
if mibBuilder.loadTexts:enc2111HygroSensor.setStatus(_B)
if mibBuilder.loadTexts:enc2111HygroSensor.setUnits('0.1 percent humidity')
class _Enc2111InputSensor_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_H,0),(_I,1)))
_Enc2111InputSensor_Type.__name__=_D
_Enc2111InputSensor_Object=MibTableColumn
enc2111InputSensor=_Enc2111InputSensor_Object((1,3,6,1,4,1,28507,60,1,6,1,1,4),_Enc2111InputSensor_Type())
enc2111InputSensor.setMaxAccess(_C)
if mibBuilder.loadTexts:enc2111InputSensor.setStatus(_B)
_Enc2111AirPressure_Type=Integer32
_Enc2111AirPressure_Object=MibTableColumn
enc2111AirPressure=_Enc2111AirPressure_Object((1,3,6,1,4,1,28507,60,1,6,1,1,5),_Enc2111AirPressure_Type())
enc2111AirPressure.setMaxAccess(_C)
if mibBuilder.loadTexts:enc2111AirPressure.setStatus(_B)
if mibBuilder.loadTexts:enc2111AirPressure.setUnits('1 hPA (hectopascal) ~ 1 milibar')
_Enc2111DewPoint_Type=Integer32
_Enc2111DewPoint_Object=MibTableColumn
enc2111DewPoint=_Enc2111DewPoint_Object((1,3,6,1,4,1,28507,60,1,6,1,1,6),_Enc2111DewPoint_Type())
enc2111DewPoint.setMaxAccess(_C)
if mibBuilder.loadTexts:enc2111DewPoint.setStatus(_B)
if mibBuilder.loadTexts:enc2111DewPoint.setUnits(_M)
_Enc2111DewPointDiff_Type=Integer32
_Enc2111DewPointDiff_Object=MibTableColumn
enc2111DewPointDiff=_Enc2111DewPointDiff_Object((1,3,6,1,4,1,28507,60,1,6,1,1,7),_Enc2111DewPointDiff_Type())
enc2111DewPointDiff.setMaxAccess(_C)
if mibBuilder.loadTexts:enc2111DewPointDiff.setStatus(_B)
if mibBuilder.loadTexts:enc2111DewPointDiff.setUnits(_M)
_Enc2111Conf_ObjectIdentity=ObjectIdentity
enc2111Conf=_Enc2111Conf_ObjectIdentity((1,3,6,1,4,1,28507,60,2))
_Enc2111Groups_ObjectIdentity=ObjectIdentity
enc2111Groups=_Enc2111Groups_ObjectIdentity((1,3,6,1,4,1,28507,60,2,1))
_Enc2111Compls_ObjectIdentity=ObjectIdentity
enc2111Compls=_Enc2111Compls_ObjectIdentity((1,3,6,1,4,1,28507,60,2,2))
_Events_ObjectIdentity=ObjectIdentity
events=_Events_ObjectIdentity((1,3,6,1,4,1,28507,60,3))
enc2111BasicGroup=ObjectGroup((1,3,6,1,4,1,28507,60,2,1,1))
enc2111BasicGroup.setObjects(*((_A,_Z),(_A,_L),(_A,_a),(_A,_b),(_A,_G),(_A,_N),(_A,_O),(_A,_P),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_J),(_A,_Q),(_A,_g),(_A,_h),(_A,_R),(_A,_E),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_i),(_A,_W)))
if mibBuilder.loadTexts:enc2111BasicGroup.setStatus(_B)
enc2111SwitchEvtPort=NotificationType((1,3,6,1,4,1,28507,60,3,1))
enc2111SwitchEvtPort.setObjects(*((_A,_G),(_A,_N),(_A,_O),(_A,_P)))
if mibBuilder.loadTexts:enc2111SwitchEvtPort.setStatus(_B)
enc2111InputEvt=NotificationType((1,3,6,1,4,1,28507,60,3,2))
enc2111InputEvt.setObjects(*((_A,_J),(_A,_Q)))
if mibBuilder.loadTexts:enc2111InputEvt.setStatus(_B)
enc2111TempEvtSen=NotificationType((1,3,6,1,4,1,28507,60,3,3))
enc2111TempEvtSen.setObjects(*((_A,_E),(_A,_S)))
if mibBuilder.loadTexts:enc2111TempEvtSen.setStatus(_B)
enc2111HygroEvtSen=NotificationType((1,3,6,1,4,1,28507,60,3,4))
enc2111HygroEvtSen.setObjects(*((_A,_E),(_A,_T)))
if mibBuilder.loadTexts:enc2111HygroEvtSen.setStatus(_B)
enc2111InputEvtSen=NotificationType((1,3,6,1,4,1,28507,60,3,5))
enc2111InputEvtSen.setObjects(*((_A,_E),(_A,_U)))
if mibBuilder.loadTexts:enc2111InputEvtSen.setStatus(_B)
enc2111AirPressureEvtSen=NotificationType((1,3,6,1,4,1,28507,60,3,6))
enc2111AirPressureEvtSen.setObjects(*((_A,_E),(_A,_V)))
if mibBuilder.loadTexts:enc2111AirPressureEvtSen.setStatus(_B)
enc2111DewPtDiffEvtSen=NotificationType((1,3,6,1,4,1,28507,60,3,7))
enc2111DewPtDiffEvtSen.setObjects(*((_A,_E),(_A,_W)))
if mibBuilder.loadTexts:enc2111DewPtDiffEvtSen.setStatus(_B)
enc2111POEEvt=NotificationType((1,3,6,1,4,1,28507,60,3,8))
enc2111POEEvt.setObjects((_A,_R))
if mibBuilder.loadTexts:enc2111POEEvt.setStatus(_B)
enc2111NotificationGroup=NotificationGroup((1,3,6,1,4,1,28507,60,2,1,2))
enc2111NotificationGroup.setObjects(*((_A,_j),(_A,_k),(_A,_l),(_A,_m),(_A,_n),(_A,_o),(_A,_p),(_A,_q)))
if mibBuilder.loadTexts:enc2111NotificationGroup.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'gudeads':gudeads,'gadsENC2111':gadsENC2111,'enc2111Objects':enc2111Objects,'enc2111CommonConfig':enc2111CommonConfig,'enc2111SNMPaccess':enc2111SNMPaccess,_Z:enc2111TrapCtrl,'enc2111TrapIPTable':enc2111TrapIPTable,'enc2111TrapIPEntry':enc2111TrapIPEntry,_L:enc2111TrapIPIndex,_a:enc2111TrapAddr,'enc2111DeviceConfig':enc2111DeviceConfig,'enc2111IntActors':enc2111IntActors,'enc2111relayports':enc2111relayports,_b:enc2111portNumber,'enc2111portTable':enc2111portTable,'enc2111portEntry':enc2111portEntry,_G:enc2111PortIndex,_N:enc2111PortName,_O:enc2111PortState,_P:enc2111PortSwitchCount,_c:enc2111PortStartupMode,_d:enc2111PortStartupDelay,_e:enc2111PortRepowerTime,'enc2111ExtActors':enc2111ExtActors,'enc2111IntSensors':enc2111IntSensors,'enc2111Inputs':enc2111Inputs,_f:enc2111ActiveInputs,'enc2111InputTable':enc2111InputTable,'enc2111InputEntry':enc2111InputEntry,_J:enc2111InputIndex,_Q:enc2111Input,'enc2111VoltageInfo':enc2111VoltageInfo,_g:enc2111State12V,_h:enc2111State3V,_R:enc2111POE,'enc2111ExtSensors':enc2111ExtSensors,'enc2111SensorTable':enc2111SensorTable,'enc2111SensorEntry':enc2111SensorEntry,_E:enc2111SensorIndex,_S:enc2111TempSensor,_T:enc2111HygroSensor,_U:enc2111InputSensor,_V:enc2111AirPressure,_i:enc2111DewPoint,_W:enc2111DewPointDiff,'enc2111Conf':enc2111Conf,'enc2111Groups':enc2111Groups,'enc2111BasicGroup':enc2111BasicGroup,'enc2111NotificationGroup':enc2111NotificationGroup,'enc2111Compls':enc2111Compls,'events':events,_j:enc2111SwitchEvtPort,_k:enc2111InputEvt,_l:enc2111TempEvtSen,_m:enc2111HygroEvtSen,_n:enc2111InputEvtSen,_o:enc2111AirPressureEvtSen,_p:enc2111DewPtDiffEvtSen,_q:enc2111POEEvt})