_A8='epc1105LineAmperageEvt'
_A7='epc1105DewPtDiffEvtSen'
_A6='epc1105AirPressureEvtSen'
_A5='epc1105InputEvtSen'
_A4='epc1105TempEvtSen'
_A3='epc1105SwitchEvtPort'
_A2='epc1105HygroEvtSen'
_A1='epc1105DewPoint'
_A0='epc1105RevEnergyReactiveResettable'
_z='epc1105RevEnergyActiveResettable'
_y='epc1105RevEnergyReactive'
_x='epc1105RevEnergyActive'
_w='epc1105ForwEnergyReactiveResettable'
_v='epc1105ForwEnergyActiveResettable'
_u='epc1105ForwEnergyReactive'
_t='epc1105ForwEnergyActive'
_s='epc1105ResetTime'
_r='epc1105AbsEnergyReactiveResettable'
_q='epc1105AbsEnergyActiveResettable'
_p='epc1105AbsEnergyReactive'
_o='epc1105Pangle'
_n='epc1105PowerFactor'
_m='epc1105AbsEnergyActive'
_l='epc1105ChanStatus'
_k='epc1105ActivePowerChan'
_j='epc1105PortRepowerTime'
_i='epc1105PortStartupDelay'
_h='epc1105PortStartupMode'
_g='epc1105portNumber'
_f='epc1105TrapAddr'
_e='epc1105TrapCtrl'
_d='seconds'
_c='Unsigned32'
_b='epc1105DewPointDiff'
_a='epc1105AirPressure'
_Z='epc1105InputSensor'
_Y='epc1105HygroSensor'
_X='epc1105TempSensor'
_W='epc1105PowerReactive'
_V='epc1105PowerApparent'
_U='epc1105Frequency'
_T='epc1105Voltage'
_S='epc1105Current'
_R='epc1105PowerActive'
_Q='epc1105PortSwitchCount'
_P='epc1105PortState'
_O='epc1105PortName'
_N='0.1 degree Celsius'
_M='off'
_L='epc1105TrapIPIndex'
_K='OctetString'
_J='epc1105PowerIndex'
_I='epc1105PortIndex'
_H='VARh'
_G='Wh'
_F='epc1105SensorIndex'
_E='read-write'
_D='Integer32'
_C='read-only'
_B='current'
_A='GUDEADS-EPC1105-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_K,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_c,'enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
gudeads=ModuleIdentity((1,3,6,1,4,1,28507))
if mibBuilder.loadTexts:gudeads.setRevisions(('2007-03-05 13:56',))
_GadsEPC1105_ObjectIdentity=ObjectIdentity
gadsEPC1105=_GadsEPC1105_ObjectIdentity((1,3,6,1,4,1,28507,69))
_Epc1105Objects_ObjectIdentity=ObjectIdentity
epc1105Objects=_Epc1105Objects_ObjectIdentity((1,3,6,1,4,1,28507,69,1))
_Epc1105CommonConfig_ObjectIdentity=ObjectIdentity
epc1105CommonConfig=_Epc1105CommonConfig_ObjectIdentity((1,3,6,1,4,1,28507,69,1,1))
_Epc1105SNMPaccess_ObjectIdentity=ObjectIdentity
epc1105SNMPaccess=_Epc1105SNMPaccess_ObjectIdentity((1,3,6,1,4,1,28507,69,1,1,1))
class _Epc1105TrapCtrl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3))
_Epc1105TrapCtrl_Type.__name__=_D
_Epc1105TrapCtrl_Object=MibScalar
epc1105TrapCtrl=_Epc1105TrapCtrl_Object((1,3,6,1,4,1,28507,69,1,1,1,1),_Epc1105TrapCtrl_Type())
epc1105TrapCtrl.setMaxAccess(_E)
if mibBuilder.loadTexts:epc1105TrapCtrl.setStatus(_B)
_Epc1105TrapIPTable_Object=MibTable
epc1105TrapIPTable=_Epc1105TrapIPTable_Object((1,3,6,1,4,1,28507,69,1,1,1,2))
if mibBuilder.loadTexts:epc1105TrapIPTable.setStatus(_B)
_Epc1105TrapIPEntry_Object=MibTableRow
epc1105TrapIPEntry=_Epc1105TrapIPEntry_Object((1,3,6,1,4,1,28507,69,1,1,1,2,1))
epc1105TrapIPEntry.setIndexNames((0,_A,_L))
if mibBuilder.loadTexts:epc1105TrapIPEntry.setStatus(_B)
class _Epc1105TrapIPIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_Epc1105TrapIPIndex_Type.__name__=_D
_Epc1105TrapIPIndex_Object=MibTableColumn
epc1105TrapIPIndex=_Epc1105TrapIPIndex_Object((1,3,6,1,4,1,28507,69,1,1,1,2,1,1),_Epc1105TrapIPIndex_Type())
epc1105TrapIPIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:epc1105TrapIPIndex.setStatus(_B)
class _Epc1105TrapAddr_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,99))
_Epc1105TrapAddr_Type.__name__=_K
_Epc1105TrapAddr_Object=MibTableColumn
epc1105TrapAddr=_Epc1105TrapAddr_Object((1,3,6,1,4,1,28507,69,1,1,1,2,1,2),_Epc1105TrapAddr_Type())
epc1105TrapAddr.setMaxAccess(_E)
if mibBuilder.loadTexts:epc1105TrapAddr.setStatus(_B)
_Epc1105DeviceConfig_ObjectIdentity=ObjectIdentity
epc1105DeviceConfig=_Epc1105DeviceConfig_ObjectIdentity((1,3,6,1,4,1,28507,69,1,2))
_Epc1105IntActors_ObjectIdentity=ObjectIdentity
epc1105IntActors=_Epc1105IntActors_ObjectIdentity((1,3,6,1,4,1,28507,69,1,3))
_Epc1105relayports_ObjectIdentity=ObjectIdentity
epc1105relayports=_Epc1105relayports_ObjectIdentity((1,3,6,1,4,1,28507,69,1,3,1))
class _Epc1105portNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1))
_Epc1105portNumber_Type.__name__=_D
_Epc1105portNumber_Object=MibScalar
epc1105portNumber=_Epc1105portNumber_Object((1,3,6,1,4,1,28507,69,1,3,1,1),_Epc1105portNumber_Type())
epc1105portNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:epc1105portNumber.setStatus(_B)
_Epc1105portTable_Object=MibTable
epc1105portTable=_Epc1105portTable_Object((1,3,6,1,4,1,28507,69,1,3,1,2))
if mibBuilder.loadTexts:epc1105portTable.setStatus(_B)
_Epc1105portEntry_Object=MibTableRow
epc1105portEntry=_Epc1105portEntry_Object((1,3,6,1,4,1,28507,69,1,3,1,2,1))
epc1105portEntry.setIndexNames((0,_A,_I))
if mibBuilder.loadTexts:epc1105portEntry.setStatus(_B)
class _Epc1105PortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1))
_Epc1105PortIndex_Type.__name__=_D
_Epc1105PortIndex_Object=MibTableColumn
epc1105PortIndex=_Epc1105PortIndex_Object((1,3,6,1,4,1,28507,69,1,3,1,2,1,1),_Epc1105PortIndex_Type())
epc1105PortIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:epc1105PortIndex.setStatus(_B)
class _Epc1105PortName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_Epc1105PortName_Type.__name__=_K
_Epc1105PortName_Object=MibTableColumn
epc1105PortName=_Epc1105PortName_Object((1,3,6,1,4,1,28507,69,1,3,1,2,1,2),_Epc1105PortName_Type())
epc1105PortName.setMaxAccess(_E)
if mibBuilder.loadTexts:epc1105PortName.setStatus(_B)
class _Epc1105PortState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_M,0),('on',1)))
_Epc1105PortState_Type.__name__=_D
_Epc1105PortState_Object=MibTableColumn
epc1105PortState=_Epc1105PortState_Object((1,3,6,1,4,1,28507,69,1,3,1,2,1,3),_Epc1105PortState_Type())
epc1105PortState.setMaxAccess(_E)
if mibBuilder.loadTexts:epc1105PortState.setStatus(_B)
_Epc1105PortSwitchCount_Type=Integer32
_Epc1105PortSwitchCount_Object=MibTableColumn
epc1105PortSwitchCount=_Epc1105PortSwitchCount_Object((1,3,6,1,4,1,28507,69,1,3,1,2,1,4),_Epc1105PortSwitchCount_Type())
epc1105PortSwitchCount.setMaxAccess(_C)
if mibBuilder.loadTexts:epc1105PortSwitchCount.setStatus(_B)
class _Epc1105PortStartupMode_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_M,0),('on',1),('laststate',2)))
_Epc1105PortStartupMode_Type.__name__=_D
_Epc1105PortStartupMode_Object=MibTableColumn
epc1105PortStartupMode=_Epc1105PortStartupMode_Object((1,3,6,1,4,1,28507,69,1,3,1,2,1,5),_Epc1105PortStartupMode_Type())
epc1105PortStartupMode.setMaxAccess(_E)
if mibBuilder.loadTexts:epc1105PortStartupMode.setStatus(_B)
class _Epc1105PortStartupDelay_Type(Integer32):defaultValue=0
_Epc1105PortStartupDelay_Type.__name__=_D
_Epc1105PortStartupDelay_Object=MibTableColumn
epc1105PortStartupDelay=_Epc1105PortStartupDelay_Object((1,3,6,1,4,1,28507,69,1,3,1,2,1,6),_Epc1105PortStartupDelay_Type())
epc1105PortStartupDelay.setMaxAccess(_E)
if mibBuilder.loadTexts:epc1105PortStartupDelay.setStatus(_B)
if mibBuilder.loadTexts:epc1105PortStartupDelay.setUnits(_d)
class _Epc1105PortRepowerTime_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Epc1105PortRepowerTime_Type.__name__=_D
_Epc1105PortRepowerTime_Object=MibTableColumn
epc1105PortRepowerTime=_Epc1105PortRepowerTime_Object((1,3,6,1,4,1,28507,69,1,3,1,2,1,7),_Epc1105PortRepowerTime_Type())
epc1105PortRepowerTime.setMaxAccess(_E)
if mibBuilder.loadTexts:epc1105PortRepowerTime.setStatus(_B)
if mibBuilder.loadTexts:epc1105PortRepowerTime.setUnits(_d)
_Epc1105ExtActors_ObjectIdentity=ObjectIdentity
epc1105ExtActors=_Epc1105ExtActors_ObjectIdentity((1,3,6,1,4,1,28507,69,1,4))
_Epc1105IntSensors_ObjectIdentity=ObjectIdentity
epc1105IntSensors=_Epc1105IntSensors_ObjectIdentity((1,3,6,1,4,1,28507,69,1,5))
_Epc1105PowerChan_ObjectIdentity=ObjectIdentity
epc1105PowerChan=_Epc1105PowerChan_ObjectIdentity((1,3,6,1,4,1,28507,69,1,5,1))
class _Epc1105ActivePowerChan_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1))
_Epc1105ActivePowerChan_Type.__name__=_c
_Epc1105ActivePowerChan_Object=MibScalar
epc1105ActivePowerChan=_Epc1105ActivePowerChan_Object((1,3,6,1,4,1,28507,69,1,5,1,1),_Epc1105ActivePowerChan_Type())
epc1105ActivePowerChan.setMaxAccess(_C)
if mibBuilder.loadTexts:epc1105ActivePowerChan.setStatus(_B)
_Epc1105PowerTable_Object=MibTable
epc1105PowerTable=_Epc1105PowerTable_Object((1,3,6,1,4,1,28507,69,1,5,1,2))
if mibBuilder.loadTexts:epc1105PowerTable.setStatus(_B)
_Epc1105PowerEntry_Object=MibTableRow
epc1105PowerEntry=_Epc1105PowerEntry_Object((1,3,6,1,4,1,28507,69,1,5,1,2,1))
epc1105PowerEntry.setIndexNames((0,_A,_J))
if mibBuilder.loadTexts:epc1105PowerEntry.setStatus(_B)
class _Epc1105PowerIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1))
_Epc1105PowerIndex_Type.__name__=_D
_Epc1105PowerIndex_Object=MibTableColumn
epc1105PowerIndex=_Epc1105PowerIndex_Object((1,3,6,1,4,1,28507,69,1,5,1,2,1,1),_Epc1105PowerIndex_Type())
epc1105PowerIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:epc1105PowerIndex.setStatus(_B)
class _Epc1105ChanStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Epc1105ChanStatus_Type.__name__=_D
_Epc1105ChanStatus_Object=MibTableColumn
epc1105ChanStatus=_Epc1105ChanStatus_Object((1,3,6,1,4,1,28507,69,1,5,1,2,1,2),_Epc1105ChanStatus_Type())
epc1105ChanStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:epc1105ChanStatus.setStatus(_B)
_Epc1105AbsEnergyActive_Type=Unsigned32
_Epc1105AbsEnergyActive_Object=MibTableColumn
epc1105AbsEnergyActive=_Epc1105AbsEnergyActive_Object((1,3,6,1,4,1,28507,69,1,5,1,2,1,3),_Epc1105AbsEnergyActive_Type())
epc1105AbsEnergyActive.setMaxAccess(_C)
if mibBuilder.loadTexts:epc1105AbsEnergyActive.setStatus(_B)
if mibBuilder.loadTexts:epc1105AbsEnergyActive.setUnits(_G)
_Epc1105PowerActive_Type=Integer32
_Epc1105PowerActive_Object=MibTableColumn
epc1105PowerActive=_Epc1105PowerActive_Object((1,3,6,1,4,1,28507,69,1,5,1,2,1,4),_Epc1105PowerActive_Type())
epc1105PowerActive.setMaxAccess(_C)
if mibBuilder.loadTexts:epc1105PowerActive.setStatus(_B)
if mibBuilder.loadTexts:epc1105PowerActive.setUnits('W')
_Epc1105Current_Type=Unsigned32
_Epc1105Current_Object=MibTableColumn
epc1105Current=_Epc1105Current_Object((1,3,6,1,4,1,28507,69,1,5,1,2,1,5),_Epc1105Current_Type())
epc1105Current.setMaxAccess(_C)
if mibBuilder.loadTexts:epc1105Current.setStatus(_B)
if mibBuilder.loadTexts:epc1105Current.setUnits('mA')
_Epc1105Voltage_Type=Unsigned32
_Epc1105Voltage_Object=MibTableColumn
epc1105Voltage=_Epc1105Voltage_Object((1,3,6,1,4,1,28507,69,1,5,1,2,1,6),_Epc1105Voltage_Type())
epc1105Voltage.setMaxAccess(_C)
if mibBuilder.loadTexts:epc1105Voltage.setStatus(_B)
if mibBuilder.loadTexts:epc1105Voltage.setUnits('V')
_Epc1105Frequency_Type=Unsigned32
_Epc1105Frequency_Object=MibTableColumn
epc1105Frequency=_Epc1105Frequency_Object((1,3,6,1,4,1,28507,69,1,5,1,2,1,7),_Epc1105Frequency_Type())
epc1105Frequency.setMaxAccess(_C)
if mibBuilder.loadTexts:epc1105Frequency.setStatus(_B)
if mibBuilder.loadTexts:epc1105Frequency.setUnits('0.01 hz')
_Epc1105PowerFactor_Type=Integer32
_Epc1105PowerFactor_Object=MibTableColumn
epc1105PowerFactor=_Epc1105PowerFactor_Object((1,3,6,1,4,1,28507,69,1,5,1,2,1,8),_Epc1105PowerFactor_Type())
epc1105PowerFactor.setMaxAccess(_C)
if mibBuilder.loadTexts:epc1105PowerFactor.setStatus(_B)
if mibBuilder.loadTexts:epc1105PowerFactor.setUnits('0.001')
_Epc1105Pangle_Type=Integer32
_Epc1105Pangle_Object=MibTableColumn
epc1105Pangle=_Epc1105Pangle_Object((1,3,6,1,4,1,28507,69,1,5,1,2,1,9),_Epc1105Pangle_Type())
epc1105Pangle.setMaxAccess(_C)
if mibBuilder.loadTexts:epc1105Pangle.setStatus(_B)
if mibBuilder.loadTexts:epc1105Pangle.setUnits('0.1 degree')
_Epc1105PowerApparent_Type=Integer32
_Epc1105PowerApparent_Object=MibTableColumn
epc1105PowerApparent=_Epc1105PowerApparent_Object((1,3,6,1,4,1,28507,69,1,5,1,2,1,10),_Epc1105PowerApparent_Type())
epc1105PowerApparent.setMaxAccess(_C)
if mibBuilder.loadTexts:epc1105PowerApparent.setStatus(_B)
if mibBuilder.loadTexts:epc1105PowerApparent.setUnits('VA')
_Epc1105PowerReactive_Type=Integer32
_Epc1105PowerReactive_Object=MibTableColumn
epc1105PowerReactive=_Epc1105PowerReactive_Object((1,3,6,1,4,1,28507,69,1,5,1,2,1,11),_Epc1105PowerReactive_Type())
epc1105PowerReactive.setMaxAccess(_C)
if mibBuilder.loadTexts:epc1105PowerReactive.setStatus(_B)
if mibBuilder.loadTexts:epc1105PowerReactive.setUnits('VAR')
_Epc1105AbsEnergyReactive_Type=Unsigned32
_Epc1105AbsEnergyReactive_Object=MibTableColumn
epc1105AbsEnergyReactive=_Epc1105AbsEnergyReactive_Object((1,3,6,1,4,1,28507,69,1,5,1,2,1,12),_Epc1105AbsEnergyReactive_Type())
epc1105AbsEnergyReactive.setMaxAccess(_C)
if mibBuilder.loadTexts:epc1105AbsEnergyReactive.setStatus(_B)
if mibBuilder.loadTexts:epc1105AbsEnergyReactive.setUnits(_H)
_Epc1105AbsEnergyActiveResettable_Type=Unsigned32
_Epc1105AbsEnergyActiveResettable_Object=MibTableColumn
epc1105AbsEnergyActiveResettable=_Epc1105AbsEnergyActiveResettable_Object((1,3,6,1,4,1,28507,69,1,5,1,2,1,13),_Epc1105AbsEnergyActiveResettable_Type())
epc1105AbsEnergyActiveResettable.setMaxAccess(_E)
if mibBuilder.loadTexts:epc1105AbsEnergyActiveResettable.setStatus(_B)
if mibBuilder.loadTexts:epc1105AbsEnergyActiveResettable.setUnits(_G)
_Epc1105AbsEnergyReactiveResettable_Type=Unsigned32
_Epc1105AbsEnergyReactiveResettable_Object=MibTableColumn
epc1105AbsEnergyReactiveResettable=_Epc1105AbsEnergyReactiveResettable_Object((1,3,6,1,4,1,28507,69,1,5,1,2,1,14),_Epc1105AbsEnergyReactiveResettable_Type())
epc1105AbsEnergyReactiveResettable.setMaxAccess(_C)
if mibBuilder.loadTexts:epc1105AbsEnergyReactiveResettable.setStatus(_B)
if mibBuilder.loadTexts:epc1105AbsEnergyReactiveResettable.setUnits(_H)
_Epc1105ResetTime_Type=Unsigned32
_Epc1105ResetTime_Object=MibTableColumn
epc1105ResetTime=_Epc1105ResetTime_Object((1,3,6,1,4,1,28507,69,1,5,1,2,1,15),_Epc1105ResetTime_Type())
epc1105ResetTime.setMaxAccess(_C)
if mibBuilder.loadTexts:epc1105ResetTime.setStatus(_B)
if mibBuilder.loadTexts:epc1105ResetTime.setUnits('s')
_Epc1105ForwEnergyActive_Type=Unsigned32
_Epc1105ForwEnergyActive_Object=MibTableColumn
epc1105ForwEnergyActive=_Epc1105ForwEnergyActive_Object((1,3,6,1,4,1,28507,69,1,5,1,2,1,16),_Epc1105ForwEnergyActive_Type())
epc1105ForwEnergyActive.setMaxAccess(_C)
if mibBuilder.loadTexts:epc1105ForwEnergyActive.setStatus(_B)
if mibBuilder.loadTexts:epc1105ForwEnergyActive.setUnits(_G)
_Epc1105ForwEnergyReactive_Type=Unsigned32
_Epc1105ForwEnergyReactive_Object=MibTableColumn
epc1105ForwEnergyReactive=_Epc1105ForwEnergyReactive_Object((1,3,6,1,4,1,28507,69,1,5,1,2,1,17),_Epc1105ForwEnergyReactive_Type())
epc1105ForwEnergyReactive.setMaxAccess(_C)
if mibBuilder.loadTexts:epc1105ForwEnergyReactive.setStatus(_B)
if mibBuilder.loadTexts:epc1105ForwEnergyReactive.setUnits(_H)
_Epc1105ForwEnergyActiveResettable_Type=Unsigned32
_Epc1105ForwEnergyActiveResettable_Object=MibTableColumn
epc1105ForwEnergyActiveResettable=_Epc1105ForwEnergyActiveResettable_Object((1,3,6,1,4,1,28507,69,1,5,1,2,1,18),_Epc1105ForwEnergyActiveResettable_Type())
epc1105ForwEnergyActiveResettable.setMaxAccess(_C)
if mibBuilder.loadTexts:epc1105ForwEnergyActiveResettable.setStatus(_B)
if mibBuilder.loadTexts:epc1105ForwEnergyActiveResettable.setUnits(_G)
_Epc1105ForwEnergyReactiveResettable_Type=Unsigned32
_Epc1105ForwEnergyReactiveResettable_Object=MibTableColumn
epc1105ForwEnergyReactiveResettable=_Epc1105ForwEnergyReactiveResettable_Object((1,3,6,1,4,1,28507,69,1,5,1,2,1,19),_Epc1105ForwEnergyReactiveResettable_Type())
epc1105ForwEnergyReactiveResettable.setMaxAccess(_C)
if mibBuilder.loadTexts:epc1105ForwEnergyReactiveResettable.setStatus(_B)
if mibBuilder.loadTexts:epc1105ForwEnergyReactiveResettable.setUnits(_H)
_Epc1105RevEnergyActive_Type=Unsigned32
_Epc1105RevEnergyActive_Object=MibTableColumn
epc1105RevEnergyActive=_Epc1105RevEnergyActive_Object((1,3,6,1,4,1,28507,69,1,5,1,2,1,20),_Epc1105RevEnergyActive_Type())
epc1105RevEnergyActive.setMaxAccess(_C)
if mibBuilder.loadTexts:epc1105RevEnergyActive.setStatus(_B)
if mibBuilder.loadTexts:epc1105RevEnergyActive.setUnits(_G)
_Epc1105RevEnergyReactive_Type=Unsigned32
_Epc1105RevEnergyReactive_Object=MibTableColumn
epc1105RevEnergyReactive=_Epc1105RevEnergyReactive_Object((1,3,6,1,4,1,28507,69,1,5,1,2,1,21),_Epc1105RevEnergyReactive_Type())
epc1105RevEnergyReactive.setMaxAccess(_C)
if mibBuilder.loadTexts:epc1105RevEnergyReactive.setStatus(_B)
if mibBuilder.loadTexts:epc1105RevEnergyReactive.setUnits(_H)
_Epc1105RevEnergyActiveResettable_Type=Unsigned32
_Epc1105RevEnergyActiveResettable_Object=MibTableColumn
epc1105RevEnergyActiveResettable=_Epc1105RevEnergyActiveResettable_Object((1,3,6,1,4,1,28507,69,1,5,1,2,1,22),_Epc1105RevEnergyActiveResettable_Type())
epc1105RevEnergyActiveResettable.setMaxAccess(_C)
if mibBuilder.loadTexts:epc1105RevEnergyActiveResettable.setStatus(_B)
if mibBuilder.loadTexts:epc1105RevEnergyActiveResettable.setUnits(_G)
_Epc1105RevEnergyReactiveResettable_Type=Unsigned32
_Epc1105RevEnergyReactiveResettable_Object=MibTableColumn
epc1105RevEnergyReactiveResettable=_Epc1105RevEnergyReactiveResettable_Object((1,3,6,1,4,1,28507,69,1,5,1,2,1,23),_Epc1105RevEnergyReactiveResettable_Type())
epc1105RevEnergyReactiveResettable.setMaxAccess(_C)
if mibBuilder.loadTexts:epc1105RevEnergyReactiveResettable.setStatus(_B)
if mibBuilder.loadTexts:epc1105RevEnergyReactiveResettable.setUnits(_H)
_Epc1105ExtSensors_ObjectIdentity=ObjectIdentity
epc1105ExtSensors=_Epc1105ExtSensors_ObjectIdentity((1,3,6,1,4,1,28507,69,1,6))
_Epc1105SensorTable_Object=MibTable
epc1105SensorTable=_Epc1105SensorTable_Object((1,3,6,1,4,1,28507,69,1,6,1))
if mibBuilder.loadTexts:epc1105SensorTable.setStatus(_B)
_Epc1105SensorEntry_Object=MibTableRow
epc1105SensorEntry=_Epc1105SensorEntry_Object((1,3,6,1,4,1,28507,69,1,6,1,1))
epc1105SensorEntry.setIndexNames((0,_A,_F))
if mibBuilder.loadTexts:epc1105SensorEntry.setStatus(_B)
class _Epc1105SensorIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1))
_Epc1105SensorIndex_Type.__name__=_D
_Epc1105SensorIndex_Object=MibTableColumn
epc1105SensorIndex=_Epc1105SensorIndex_Object((1,3,6,1,4,1,28507,69,1,6,1,1,1),_Epc1105SensorIndex_Type())
epc1105SensorIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:epc1105SensorIndex.setStatus(_B)
_Epc1105TempSensor_Type=Integer32
_Epc1105TempSensor_Object=MibTableColumn
epc1105TempSensor=_Epc1105TempSensor_Object((1,3,6,1,4,1,28507,69,1,6,1,1,2),_Epc1105TempSensor_Type())
epc1105TempSensor.setMaxAccess(_C)
if mibBuilder.loadTexts:epc1105TempSensor.setStatus(_B)
if mibBuilder.loadTexts:epc1105TempSensor.setUnits(_N)
_Epc1105HygroSensor_Type=Integer32
_Epc1105HygroSensor_Object=MibTableColumn
epc1105HygroSensor=_Epc1105HygroSensor_Object((1,3,6,1,4,1,28507,69,1,6,1,1,3),_Epc1105HygroSensor_Type())
epc1105HygroSensor.setMaxAccess(_C)
if mibBuilder.loadTexts:epc1105HygroSensor.setStatus(_B)
if mibBuilder.loadTexts:epc1105HygroSensor.setUnits('0.1 percent humidity')
class _Epc1105InputSensor_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_M,0),('on',1)))
_Epc1105InputSensor_Type.__name__=_D
_Epc1105InputSensor_Object=MibTableColumn
epc1105InputSensor=_Epc1105InputSensor_Object((1,3,6,1,4,1,28507,69,1,6,1,1,4),_Epc1105InputSensor_Type())
epc1105InputSensor.setMaxAccess(_C)
if mibBuilder.loadTexts:epc1105InputSensor.setStatus(_B)
_Epc1105AirPressure_Type=Integer32
_Epc1105AirPressure_Object=MibTableColumn
epc1105AirPressure=_Epc1105AirPressure_Object((1,3,6,1,4,1,28507,69,1,6,1,1,5),_Epc1105AirPressure_Type())
epc1105AirPressure.setMaxAccess(_C)
if mibBuilder.loadTexts:epc1105AirPressure.setStatus(_B)
if mibBuilder.loadTexts:epc1105AirPressure.setUnits('1 hPA (hectopascal) ~ 1 milibar')
_Epc1105DewPoint_Type=Integer32
_Epc1105DewPoint_Object=MibTableColumn
epc1105DewPoint=_Epc1105DewPoint_Object((1,3,6,1,4,1,28507,69,1,6,1,1,6),_Epc1105DewPoint_Type())
epc1105DewPoint.setMaxAccess(_C)
if mibBuilder.loadTexts:epc1105DewPoint.setStatus(_B)
if mibBuilder.loadTexts:epc1105DewPoint.setUnits(_N)
_Epc1105DewPointDiff_Type=Integer32
_Epc1105DewPointDiff_Object=MibTableColumn
epc1105DewPointDiff=_Epc1105DewPointDiff_Object((1,3,6,1,4,1,28507,69,1,6,1,1,7),_Epc1105DewPointDiff_Type())
epc1105DewPointDiff.setMaxAccess(_C)
if mibBuilder.loadTexts:epc1105DewPointDiff.setStatus(_B)
if mibBuilder.loadTexts:epc1105DewPointDiff.setUnits(_N)
_Epc1105Conf_ObjectIdentity=ObjectIdentity
epc1105Conf=_Epc1105Conf_ObjectIdentity((1,3,6,1,4,1,28507,69,2))
_Epc1105Groups_ObjectIdentity=ObjectIdentity
epc1105Groups=_Epc1105Groups_ObjectIdentity((1,3,6,1,4,1,28507,69,2,1))
_Epc1105Compls_ObjectIdentity=ObjectIdentity
epc1105Compls=_Epc1105Compls_ObjectIdentity((1,3,6,1,4,1,28507,69,2,2))
_Events_ObjectIdentity=ObjectIdentity
events=_Events_ObjectIdentity((1,3,6,1,4,1,28507,69,3))
epc1105BasicGroup=ObjectGroup((1,3,6,1,4,1,28507,69,2,1,1))
epc1105BasicGroup.setObjects(*((_A,_e),(_A,_L),(_A,_f),(_A,_g),(_A,_I),(_A,_O),(_A,_P),(_A,_Q),(_A,_h),(_A,_i),(_A,_j),(_A,_k),(_A,_J),(_A,_l),(_A,_m),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_n),(_A,_o),(_A,_V),(_A,_W),(_A,_p),(_A,_q),(_A,_r),(_A,_s),(_A,_t),(_A,_u),(_A,_v),(_A,_w),(_A,_x),(_A,_y),(_A,_z),(_A,_A0),(_A,_F),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_A1),(_A,_b)))
if mibBuilder.loadTexts:epc1105BasicGroup.setStatus(_B)
epc1105SwitchEvtPort=NotificationType((1,3,6,1,4,1,28507,69,3,1))
epc1105SwitchEvtPort.setObjects(*((_A,_I),(_A,_O),(_A,_P),(_A,_Q)))
if mibBuilder.loadTexts:epc1105SwitchEvtPort.setStatus(_B)
epc1105TempEvtSen=NotificationType((1,3,6,1,4,1,28507,69,3,2))
epc1105TempEvtSen.setObjects(*((_A,_F),(_A,_X)))
if mibBuilder.loadTexts:epc1105TempEvtSen.setStatus(_B)
epc1105HygroEvtSen=NotificationType((1,3,6,1,4,1,28507,69,3,3))
epc1105HygroEvtSen.setObjects(*((_A,_F),(_A,_Y)))
if mibBuilder.loadTexts:epc1105HygroEvtSen.setStatus(_B)
epc1105InputEvtSen=NotificationType((1,3,6,1,4,1,28507,69,3,4))
epc1105InputEvtSen.setObjects(*((_A,_F),(_A,_Z)))
if mibBuilder.loadTexts:epc1105InputEvtSen.setStatus(_B)
epc1105AirPressureEvtSen=NotificationType((1,3,6,1,4,1,28507,69,3,5))
epc1105AirPressureEvtSen.setObjects(*((_A,_F),(_A,_a)))
if mibBuilder.loadTexts:epc1105AirPressureEvtSen.setStatus(_B)
epc1105DewPtDiffEvtSen=NotificationType((1,3,6,1,4,1,28507,69,3,6))
epc1105DewPtDiffEvtSen.setObjects(*((_A,_F),(_A,_b)))
if mibBuilder.loadTexts:epc1105DewPtDiffEvtSen.setStatus(_B)
epc1105LineAmperageEvt=NotificationType((1,3,6,1,4,1,28507,69,3,7))
epc1105LineAmperageEvt.setObjects(*((_A,_J),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W)))
if mibBuilder.loadTexts:epc1105LineAmperageEvt.setStatus(_B)
epc1105NotificationGroup=NotificationGroup((1,3,6,1,4,1,28507,69,2,1,2))
epc1105NotificationGroup.setObjects(*((_A,_A2),(_A,_A3),(_A,_A4),(_A,_A5),(_A,_A6),(_A,_A7),(_A,_A8)))
if mibBuilder.loadTexts:epc1105NotificationGroup.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'gudeads':gudeads,'gadsEPC1105':gadsEPC1105,'epc1105Objects':epc1105Objects,'epc1105CommonConfig':epc1105CommonConfig,'epc1105SNMPaccess':epc1105SNMPaccess,_e:epc1105TrapCtrl,'epc1105TrapIPTable':epc1105TrapIPTable,'epc1105TrapIPEntry':epc1105TrapIPEntry,_L:epc1105TrapIPIndex,_f:epc1105TrapAddr,'epc1105DeviceConfig':epc1105DeviceConfig,'epc1105IntActors':epc1105IntActors,'epc1105relayports':epc1105relayports,_g:epc1105portNumber,'epc1105portTable':epc1105portTable,'epc1105portEntry':epc1105portEntry,_I:epc1105PortIndex,_O:epc1105PortName,_P:epc1105PortState,_Q:epc1105PortSwitchCount,_h:epc1105PortStartupMode,_i:epc1105PortStartupDelay,_j:epc1105PortRepowerTime,'epc1105ExtActors':epc1105ExtActors,'epc1105IntSensors':epc1105IntSensors,'epc1105PowerChan':epc1105PowerChan,_k:epc1105ActivePowerChan,'epc1105PowerTable':epc1105PowerTable,'epc1105PowerEntry':epc1105PowerEntry,_J:epc1105PowerIndex,_l:epc1105ChanStatus,_m:epc1105AbsEnergyActive,_R:epc1105PowerActive,_S:epc1105Current,_T:epc1105Voltage,_U:epc1105Frequency,_n:epc1105PowerFactor,_o:epc1105Pangle,_V:epc1105PowerApparent,_W:epc1105PowerReactive,_p:epc1105AbsEnergyReactive,_q:epc1105AbsEnergyActiveResettable,_r:epc1105AbsEnergyReactiveResettable,_s:epc1105ResetTime,_t:epc1105ForwEnergyActive,_u:epc1105ForwEnergyReactive,_v:epc1105ForwEnergyActiveResettable,_w:epc1105ForwEnergyReactiveResettable,_x:epc1105RevEnergyActive,_y:epc1105RevEnergyReactive,_z:epc1105RevEnergyActiveResettable,_A0:epc1105RevEnergyReactiveResettable,'epc1105ExtSensors':epc1105ExtSensors,'epc1105SensorTable':epc1105SensorTable,'epc1105SensorEntry':epc1105SensorEntry,_F:epc1105SensorIndex,_X:epc1105TempSensor,_Y:epc1105HygroSensor,_Z:epc1105InputSensor,_a:epc1105AirPressure,_A1:epc1105DewPoint,_b:epc1105DewPointDiff,'epc1105Conf':epc1105Conf,'epc1105Groups':epc1105Groups,'epc1105BasicGroup':epc1105BasicGroup,'epc1105NotificationGroup':epc1105NotificationGroup,'epc1105Compls':epc1105Compls,'events':events,_A3:epc1105SwitchEvtPort,_A4:epc1105TempEvtSen,_A2:epc1105HygroEvtSen,_A5:epc1105InputEvtSen,_A6:epc1105AirPressureEvtSen,_A7:epc1105DewPtDiffEvtSen,_A8:epc1105LineAmperageEvt})