_AC='epc8221LineAmperageEvt'
_AB='epc8221OVPEvt'
_AA='epc8221DewPtDiffEvtSen'
_A9='epc8221AirPressureEvtSen'
_A8='epc8221InputEvtSen'
_A7='epc8221HygroEvtSen'
_A6='epc8221TempEvtSen'
_A5='epc8221SwitchEvtPort'
_A4='epc8221DewPoint'
_A3='epc8221RevEnergyReactiveResettable'
_A2='epc8221RevEnergyActiveResettable'
_A1='epc8221RevEnergyReactive'
_A0='epc8221RevEnergyActive'
_z='epc8221ForwEnergyReactiveResettable'
_y='epc8221ForwEnergyActiveResettable'
_x='epc8221ForwEnergyReactive'
_w='epc8221ForwEnergyActive'
_v='epc8221ResetTime'
_u='epc8221AbsEnergyReactiveResettable'
_t='epc8221AbsEnergyActiveResettable'
_s='epc8221AbsEnergyReactive'
_r='epc8221Pangle'
_q='epc8221PowerFactor'
_p='epc8221AbsEnergyActive'
_o='epc8221ChanStatus'
_n='epc8221ActivePowerChan'
_m='epc8221Buzzer'
_l='epc8221PortRepowerTime'
_k='epc8221PortStartupDelay'
_j='epc8221PortStartupMode'
_i='epc8221portNumber'
_h='epc8221TrapAddr'
_g='epc8221TrapCtrl'
_f='seconds'
_e='Unsigned32'
_d='epc8221DewPointDiff'
_c='epc8221AirPressure'
_b='epc8221InputSensor'
_a='epc8221HygroSensor'
_Z='epc8221TempSensor'
_Y='epc8221OVPStatus'
_X='epc8221PowerReactive'
_W='epc8221PowerApparent'
_V='epc8221Frequency'
_U='epc8221Voltage'
_T='epc8221Current'
_S='epc8221PowerActive'
_R='epc8221PortSwitchCount'
_Q='epc8221PortState'
_P='epc8221PortName'
_O='0.1 degree Celsius'
_N='off'
_M='epc8221TrapIPIndex'
_L='OctetString'
_K='epc8221OVPIndex'
_J='epc8221PowerIndex'
_I='epc8221PortIndex'
_H='VARh'
_G='Wh'
_F='epc8221SensorIndex'
_E='read-write'
_D='Integer32'
_C='read-only'
_B='current'
_A='GUDEADS-EPC8221-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_L,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_e,'enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
gudeads=ModuleIdentity((1,3,6,1,4,1,28507))
if mibBuilder.loadTexts:gudeads.setRevisions(('2007-03-05 13:56',))
_GadsEPC8221_ObjectIdentity=ObjectIdentity
gadsEPC8221=_GadsEPC8221_ObjectIdentity((1,3,6,1,4,1,28507,56))
_Epc8221Objects_ObjectIdentity=ObjectIdentity
epc8221Objects=_Epc8221Objects_ObjectIdentity((1,3,6,1,4,1,28507,56,1))
_Epc8221CommonConfig_ObjectIdentity=ObjectIdentity
epc8221CommonConfig=_Epc8221CommonConfig_ObjectIdentity((1,3,6,1,4,1,28507,56,1,1))
_Epc8221SNMPaccess_ObjectIdentity=ObjectIdentity
epc8221SNMPaccess=_Epc8221SNMPaccess_ObjectIdentity((1,3,6,1,4,1,28507,56,1,1,1))
class _Epc8221TrapCtrl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3))
_Epc8221TrapCtrl_Type.__name__=_D
_Epc8221TrapCtrl_Object=MibScalar
epc8221TrapCtrl=_Epc8221TrapCtrl_Object((1,3,6,1,4,1,28507,56,1,1,1,1),_Epc8221TrapCtrl_Type())
epc8221TrapCtrl.setMaxAccess(_E)
if mibBuilder.loadTexts:epc8221TrapCtrl.setStatus(_B)
_Epc8221TrapIPTable_Object=MibTable
epc8221TrapIPTable=_Epc8221TrapIPTable_Object((1,3,6,1,4,1,28507,56,1,1,1,2))
if mibBuilder.loadTexts:epc8221TrapIPTable.setStatus(_B)
_Epc8221TrapIPEntry_Object=MibTableRow
epc8221TrapIPEntry=_Epc8221TrapIPEntry_Object((1,3,6,1,4,1,28507,56,1,1,1,2,1))
epc8221TrapIPEntry.setIndexNames((0,_A,_M))
if mibBuilder.loadTexts:epc8221TrapIPEntry.setStatus(_B)
class _Epc8221TrapIPIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_Epc8221TrapIPIndex_Type.__name__=_D
_Epc8221TrapIPIndex_Object=MibTableColumn
epc8221TrapIPIndex=_Epc8221TrapIPIndex_Object((1,3,6,1,4,1,28507,56,1,1,1,2,1,1),_Epc8221TrapIPIndex_Type())
epc8221TrapIPIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:epc8221TrapIPIndex.setStatus(_B)
class _Epc8221TrapAddr_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,99))
_Epc8221TrapAddr_Type.__name__=_L
_Epc8221TrapAddr_Object=MibTableColumn
epc8221TrapAddr=_Epc8221TrapAddr_Object((1,3,6,1,4,1,28507,56,1,1,1,2,1,2),_Epc8221TrapAddr_Type())
epc8221TrapAddr.setMaxAccess(_E)
if mibBuilder.loadTexts:epc8221TrapAddr.setStatus(_B)
_Epc8221DeviceConfig_ObjectIdentity=ObjectIdentity
epc8221DeviceConfig=_Epc8221DeviceConfig_ObjectIdentity((1,3,6,1,4,1,28507,56,1,2))
_Epc8221IntActors_ObjectIdentity=ObjectIdentity
epc8221IntActors=_Epc8221IntActors_ObjectIdentity((1,3,6,1,4,1,28507,56,1,3))
_Epc8221relayports_ObjectIdentity=ObjectIdentity
epc8221relayports=_Epc8221relayports_ObjectIdentity((1,3,6,1,4,1,28507,56,1,3,1))
class _Epc8221portNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,12))
_Epc8221portNumber_Type.__name__=_D
_Epc8221portNumber_Object=MibScalar
epc8221portNumber=_Epc8221portNumber_Object((1,3,6,1,4,1,28507,56,1,3,1,1),_Epc8221portNumber_Type())
epc8221portNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:epc8221portNumber.setStatus(_B)
_Epc8221portTable_Object=MibTable
epc8221portTable=_Epc8221portTable_Object((1,3,6,1,4,1,28507,56,1,3,1,2))
if mibBuilder.loadTexts:epc8221portTable.setStatus(_B)
_Epc8221portEntry_Object=MibTableRow
epc8221portEntry=_Epc8221portEntry_Object((1,3,6,1,4,1,28507,56,1,3,1,2,1))
epc8221portEntry.setIndexNames((0,_A,_I))
if mibBuilder.loadTexts:epc8221portEntry.setStatus(_B)
class _Epc8221PortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,12))
_Epc8221PortIndex_Type.__name__=_D
_Epc8221PortIndex_Object=MibTableColumn
epc8221PortIndex=_Epc8221PortIndex_Object((1,3,6,1,4,1,28507,56,1,3,1,2,1,1),_Epc8221PortIndex_Type())
epc8221PortIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:epc8221PortIndex.setStatus(_B)
class _Epc8221PortName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_Epc8221PortName_Type.__name__=_L
_Epc8221PortName_Object=MibTableColumn
epc8221PortName=_Epc8221PortName_Object((1,3,6,1,4,1,28507,56,1,3,1,2,1,2),_Epc8221PortName_Type())
epc8221PortName.setMaxAccess(_E)
if mibBuilder.loadTexts:epc8221PortName.setStatus(_B)
class _Epc8221PortState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_N,0),('on',1)))
_Epc8221PortState_Type.__name__=_D
_Epc8221PortState_Object=MibTableColumn
epc8221PortState=_Epc8221PortState_Object((1,3,6,1,4,1,28507,56,1,3,1,2,1,3),_Epc8221PortState_Type())
epc8221PortState.setMaxAccess(_E)
if mibBuilder.loadTexts:epc8221PortState.setStatus(_B)
_Epc8221PortSwitchCount_Type=Integer32
_Epc8221PortSwitchCount_Object=MibTableColumn
epc8221PortSwitchCount=_Epc8221PortSwitchCount_Object((1,3,6,1,4,1,28507,56,1,3,1,2,1,4),_Epc8221PortSwitchCount_Type())
epc8221PortSwitchCount.setMaxAccess(_C)
if mibBuilder.loadTexts:epc8221PortSwitchCount.setStatus(_B)
class _Epc8221PortStartupMode_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_N,0),('on',1),('laststate',2)))
_Epc8221PortStartupMode_Type.__name__=_D
_Epc8221PortStartupMode_Object=MibTableColumn
epc8221PortStartupMode=_Epc8221PortStartupMode_Object((1,3,6,1,4,1,28507,56,1,3,1,2,1,5),_Epc8221PortStartupMode_Type())
epc8221PortStartupMode.setMaxAccess(_E)
if mibBuilder.loadTexts:epc8221PortStartupMode.setStatus(_B)
class _Epc8221PortStartupDelay_Type(Integer32):defaultValue=0
_Epc8221PortStartupDelay_Type.__name__=_D
_Epc8221PortStartupDelay_Object=MibTableColumn
epc8221PortStartupDelay=_Epc8221PortStartupDelay_Object((1,3,6,1,4,1,28507,56,1,3,1,2,1,6),_Epc8221PortStartupDelay_Type())
epc8221PortStartupDelay.setMaxAccess(_E)
if mibBuilder.loadTexts:epc8221PortStartupDelay.setStatus(_B)
if mibBuilder.loadTexts:epc8221PortStartupDelay.setUnits(_f)
class _Epc8221PortRepowerTime_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Epc8221PortRepowerTime_Type.__name__=_D
_Epc8221PortRepowerTime_Object=MibTableColumn
epc8221PortRepowerTime=_Epc8221PortRepowerTime_Object((1,3,6,1,4,1,28507,56,1,3,1,2,1,7),_Epc8221PortRepowerTime_Type())
epc8221PortRepowerTime.setMaxAccess(_E)
if mibBuilder.loadTexts:epc8221PortRepowerTime.setStatus(_B)
if mibBuilder.loadTexts:epc8221PortRepowerTime.setUnits(_f)
class _Epc8221Buzzer_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Epc8221Buzzer_Type.__name__=_D
_Epc8221Buzzer_Object=MibScalar
epc8221Buzzer=_Epc8221Buzzer_Object((1,3,6,1,4,1,28507,56,1,3,10),_Epc8221Buzzer_Type())
epc8221Buzzer.setMaxAccess(_E)
if mibBuilder.loadTexts:epc8221Buzzer.setStatus(_B)
if mibBuilder.loadTexts:epc8221Buzzer.setUnits('0 = Off, 1 = On')
_Epc8221ExtActors_ObjectIdentity=ObjectIdentity
epc8221ExtActors=_Epc8221ExtActors_ObjectIdentity((1,3,6,1,4,1,28507,56,1,4))
_Epc8221IntSensors_ObjectIdentity=ObjectIdentity
epc8221IntSensors=_Epc8221IntSensors_ObjectIdentity((1,3,6,1,4,1,28507,56,1,5))
_Epc8221PowerChan_ObjectIdentity=ObjectIdentity
epc8221PowerChan=_Epc8221PowerChan_ObjectIdentity((1,3,6,1,4,1,28507,56,1,5,1))
class _Epc8221ActivePowerChan_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1))
_Epc8221ActivePowerChan_Type.__name__=_e
_Epc8221ActivePowerChan_Object=MibScalar
epc8221ActivePowerChan=_Epc8221ActivePowerChan_Object((1,3,6,1,4,1,28507,56,1,5,1,1),_Epc8221ActivePowerChan_Type())
epc8221ActivePowerChan.setMaxAccess(_C)
if mibBuilder.loadTexts:epc8221ActivePowerChan.setStatus(_B)
_Epc8221PowerTable_Object=MibTable
epc8221PowerTable=_Epc8221PowerTable_Object((1,3,6,1,4,1,28507,56,1,5,1,2))
if mibBuilder.loadTexts:epc8221PowerTable.setStatus(_B)
_Epc8221PowerEntry_Object=MibTableRow
epc8221PowerEntry=_Epc8221PowerEntry_Object((1,3,6,1,4,1,28507,56,1,5,1,2,1))
epc8221PowerEntry.setIndexNames((0,_A,_J))
if mibBuilder.loadTexts:epc8221PowerEntry.setStatus(_B)
class _Epc8221PowerIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_Epc8221PowerIndex_Type.__name__=_D
_Epc8221PowerIndex_Object=MibTableColumn
epc8221PowerIndex=_Epc8221PowerIndex_Object((1,3,6,1,4,1,28507,56,1,5,1,2,1,1),_Epc8221PowerIndex_Type())
epc8221PowerIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:epc8221PowerIndex.setStatus(_B)
class _Epc8221ChanStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Epc8221ChanStatus_Type.__name__=_D
_Epc8221ChanStatus_Object=MibTableColumn
epc8221ChanStatus=_Epc8221ChanStatus_Object((1,3,6,1,4,1,28507,56,1,5,1,2,1,2),_Epc8221ChanStatus_Type())
epc8221ChanStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:epc8221ChanStatus.setStatus(_B)
_Epc8221AbsEnergyActive_Type=Gauge32
_Epc8221AbsEnergyActive_Object=MibTableColumn
epc8221AbsEnergyActive=_Epc8221AbsEnergyActive_Object((1,3,6,1,4,1,28507,56,1,5,1,2,1,3),_Epc8221AbsEnergyActive_Type())
epc8221AbsEnergyActive.setMaxAccess(_C)
if mibBuilder.loadTexts:epc8221AbsEnergyActive.setStatus(_B)
if mibBuilder.loadTexts:epc8221AbsEnergyActive.setUnits(_G)
_Epc8221PowerActive_Type=Integer32
_Epc8221PowerActive_Object=MibTableColumn
epc8221PowerActive=_Epc8221PowerActive_Object((1,3,6,1,4,1,28507,56,1,5,1,2,1,4),_Epc8221PowerActive_Type())
epc8221PowerActive.setMaxAccess(_C)
if mibBuilder.loadTexts:epc8221PowerActive.setStatus(_B)
if mibBuilder.loadTexts:epc8221PowerActive.setUnits('W')
_Epc8221Current_Type=Gauge32
_Epc8221Current_Object=MibTableColumn
epc8221Current=_Epc8221Current_Object((1,3,6,1,4,1,28507,56,1,5,1,2,1,5),_Epc8221Current_Type())
epc8221Current.setMaxAccess(_C)
if mibBuilder.loadTexts:epc8221Current.setStatus(_B)
if mibBuilder.loadTexts:epc8221Current.setUnits('mA')
_Epc8221Voltage_Type=Gauge32
_Epc8221Voltage_Object=MibTableColumn
epc8221Voltage=_Epc8221Voltage_Object((1,3,6,1,4,1,28507,56,1,5,1,2,1,6),_Epc8221Voltage_Type())
epc8221Voltage.setMaxAccess(_C)
if mibBuilder.loadTexts:epc8221Voltage.setStatus(_B)
if mibBuilder.loadTexts:epc8221Voltage.setUnits('V')
_Epc8221Frequency_Type=Gauge32
_Epc8221Frequency_Object=MibTableColumn
epc8221Frequency=_Epc8221Frequency_Object((1,3,6,1,4,1,28507,56,1,5,1,2,1,7),_Epc8221Frequency_Type())
epc8221Frequency.setMaxAccess(_C)
if mibBuilder.loadTexts:epc8221Frequency.setStatus(_B)
if mibBuilder.loadTexts:epc8221Frequency.setUnits('0.01 hz')
_Epc8221PowerFactor_Type=Integer32
_Epc8221PowerFactor_Object=MibTableColumn
epc8221PowerFactor=_Epc8221PowerFactor_Object((1,3,6,1,4,1,28507,56,1,5,1,2,1,8),_Epc8221PowerFactor_Type())
epc8221PowerFactor.setMaxAccess(_C)
if mibBuilder.loadTexts:epc8221PowerFactor.setStatus(_B)
if mibBuilder.loadTexts:epc8221PowerFactor.setUnits('0.001')
_Epc8221Pangle_Type=Integer32
_Epc8221Pangle_Object=MibTableColumn
epc8221Pangle=_Epc8221Pangle_Object((1,3,6,1,4,1,28507,56,1,5,1,2,1,9),_Epc8221Pangle_Type())
epc8221Pangle.setMaxAccess(_C)
if mibBuilder.loadTexts:epc8221Pangle.setStatus(_B)
if mibBuilder.loadTexts:epc8221Pangle.setUnits('0.1 degree')
_Epc8221PowerApparent_Type=Integer32
_Epc8221PowerApparent_Object=MibTableColumn
epc8221PowerApparent=_Epc8221PowerApparent_Object((1,3,6,1,4,1,28507,56,1,5,1,2,1,10),_Epc8221PowerApparent_Type())
epc8221PowerApparent.setMaxAccess(_C)
if mibBuilder.loadTexts:epc8221PowerApparent.setStatus(_B)
if mibBuilder.loadTexts:epc8221PowerApparent.setUnits('VA')
_Epc8221PowerReactive_Type=Integer32
_Epc8221PowerReactive_Object=MibTableColumn
epc8221PowerReactive=_Epc8221PowerReactive_Object((1,3,6,1,4,1,28507,56,1,5,1,2,1,11),_Epc8221PowerReactive_Type())
epc8221PowerReactive.setMaxAccess(_C)
if mibBuilder.loadTexts:epc8221PowerReactive.setStatus(_B)
if mibBuilder.loadTexts:epc8221PowerReactive.setUnits('VAR')
_Epc8221AbsEnergyReactive_Type=Gauge32
_Epc8221AbsEnergyReactive_Object=MibTableColumn
epc8221AbsEnergyReactive=_Epc8221AbsEnergyReactive_Object((1,3,6,1,4,1,28507,56,1,5,1,2,1,12),_Epc8221AbsEnergyReactive_Type())
epc8221AbsEnergyReactive.setMaxAccess(_C)
if mibBuilder.loadTexts:epc8221AbsEnergyReactive.setStatus(_B)
if mibBuilder.loadTexts:epc8221AbsEnergyReactive.setUnits(_H)
_Epc8221AbsEnergyActiveResettable_Type=Gauge32
_Epc8221AbsEnergyActiveResettable_Object=MibTableColumn
epc8221AbsEnergyActiveResettable=_Epc8221AbsEnergyActiveResettable_Object((1,3,6,1,4,1,28507,56,1,5,1,2,1,13),_Epc8221AbsEnergyActiveResettable_Type())
epc8221AbsEnergyActiveResettable.setMaxAccess(_E)
if mibBuilder.loadTexts:epc8221AbsEnergyActiveResettable.setStatus(_B)
if mibBuilder.loadTexts:epc8221AbsEnergyActiveResettable.setUnits(_G)
_Epc8221AbsEnergyReactiveResettable_Type=Gauge32
_Epc8221AbsEnergyReactiveResettable_Object=MibTableColumn
epc8221AbsEnergyReactiveResettable=_Epc8221AbsEnergyReactiveResettable_Object((1,3,6,1,4,1,28507,56,1,5,1,2,1,14),_Epc8221AbsEnergyReactiveResettable_Type())
epc8221AbsEnergyReactiveResettable.setMaxAccess(_C)
if mibBuilder.loadTexts:epc8221AbsEnergyReactiveResettable.setStatus(_B)
if mibBuilder.loadTexts:epc8221AbsEnergyReactiveResettable.setUnits(_H)
_Epc8221ResetTime_Type=Gauge32
_Epc8221ResetTime_Object=MibTableColumn
epc8221ResetTime=_Epc8221ResetTime_Object((1,3,6,1,4,1,28507,56,1,5,1,2,1,15),_Epc8221ResetTime_Type())
epc8221ResetTime.setMaxAccess(_C)
if mibBuilder.loadTexts:epc8221ResetTime.setStatus(_B)
if mibBuilder.loadTexts:epc8221ResetTime.setUnits('s')
_Epc8221ForwEnergyActive_Type=Gauge32
_Epc8221ForwEnergyActive_Object=MibTableColumn
epc8221ForwEnergyActive=_Epc8221ForwEnergyActive_Object((1,3,6,1,4,1,28507,56,1,5,1,2,1,16),_Epc8221ForwEnergyActive_Type())
epc8221ForwEnergyActive.setMaxAccess(_C)
if mibBuilder.loadTexts:epc8221ForwEnergyActive.setStatus(_B)
if mibBuilder.loadTexts:epc8221ForwEnergyActive.setUnits(_G)
_Epc8221ForwEnergyReactive_Type=Gauge32
_Epc8221ForwEnergyReactive_Object=MibTableColumn
epc8221ForwEnergyReactive=_Epc8221ForwEnergyReactive_Object((1,3,6,1,4,1,28507,56,1,5,1,2,1,17),_Epc8221ForwEnergyReactive_Type())
epc8221ForwEnergyReactive.setMaxAccess(_C)
if mibBuilder.loadTexts:epc8221ForwEnergyReactive.setStatus(_B)
if mibBuilder.loadTexts:epc8221ForwEnergyReactive.setUnits(_H)
_Epc8221ForwEnergyActiveResettable_Type=Gauge32
_Epc8221ForwEnergyActiveResettable_Object=MibTableColumn
epc8221ForwEnergyActiveResettable=_Epc8221ForwEnergyActiveResettable_Object((1,3,6,1,4,1,28507,56,1,5,1,2,1,18),_Epc8221ForwEnergyActiveResettable_Type())
epc8221ForwEnergyActiveResettable.setMaxAccess(_C)
if mibBuilder.loadTexts:epc8221ForwEnergyActiveResettable.setStatus(_B)
if mibBuilder.loadTexts:epc8221ForwEnergyActiveResettable.setUnits(_G)
_Epc8221ForwEnergyReactiveResettable_Type=Gauge32
_Epc8221ForwEnergyReactiveResettable_Object=MibTableColumn
epc8221ForwEnergyReactiveResettable=_Epc8221ForwEnergyReactiveResettable_Object((1,3,6,1,4,1,28507,56,1,5,1,2,1,19),_Epc8221ForwEnergyReactiveResettable_Type())
epc8221ForwEnergyReactiveResettable.setMaxAccess(_C)
if mibBuilder.loadTexts:epc8221ForwEnergyReactiveResettable.setStatus(_B)
if mibBuilder.loadTexts:epc8221ForwEnergyReactiveResettable.setUnits(_H)
_Epc8221RevEnergyActive_Type=Gauge32
_Epc8221RevEnergyActive_Object=MibTableColumn
epc8221RevEnergyActive=_Epc8221RevEnergyActive_Object((1,3,6,1,4,1,28507,56,1,5,1,2,1,20),_Epc8221RevEnergyActive_Type())
epc8221RevEnergyActive.setMaxAccess(_C)
if mibBuilder.loadTexts:epc8221RevEnergyActive.setStatus(_B)
if mibBuilder.loadTexts:epc8221RevEnergyActive.setUnits(_G)
_Epc8221RevEnergyReactive_Type=Gauge32
_Epc8221RevEnergyReactive_Object=MibTableColumn
epc8221RevEnergyReactive=_Epc8221RevEnergyReactive_Object((1,3,6,1,4,1,28507,56,1,5,1,2,1,21),_Epc8221RevEnergyReactive_Type())
epc8221RevEnergyReactive.setMaxAccess(_C)
if mibBuilder.loadTexts:epc8221RevEnergyReactive.setStatus(_B)
if mibBuilder.loadTexts:epc8221RevEnergyReactive.setUnits(_H)
_Epc8221RevEnergyActiveResettable_Type=Gauge32
_Epc8221RevEnergyActiveResettable_Object=MibTableColumn
epc8221RevEnergyActiveResettable=_Epc8221RevEnergyActiveResettable_Object((1,3,6,1,4,1,28507,56,1,5,1,2,1,22),_Epc8221RevEnergyActiveResettable_Type())
epc8221RevEnergyActiveResettable.setMaxAccess(_C)
if mibBuilder.loadTexts:epc8221RevEnergyActiveResettable.setStatus(_B)
if mibBuilder.loadTexts:epc8221RevEnergyActiveResettable.setUnits(_G)
_Epc8221RevEnergyReactiveResettable_Type=Gauge32
_Epc8221RevEnergyReactiveResettable_Object=MibTableColumn
epc8221RevEnergyReactiveResettable=_Epc8221RevEnergyReactiveResettable_Object((1,3,6,1,4,1,28507,56,1,5,1,2,1,23),_Epc8221RevEnergyReactiveResettable_Type())
epc8221RevEnergyReactiveResettable.setMaxAccess(_C)
if mibBuilder.loadTexts:epc8221RevEnergyReactiveResettable.setStatus(_B)
if mibBuilder.loadTexts:epc8221RevEnergyReactiveResettable.setUnits(_H)
_Epc8221OVPTable_Object=MibTable
epc8221OVPTable=_Epc8221OVPTable_Object((1,3,6,1,4,1,28507,56,1,5,2))
if mibBuilder.loadTexts:epc8221OVPTable.setStatus(_B)
_Epc8221OVPEntry_Object=MibTableRow
epc8221OVPEntry=_Epc8221OVPEntry_Object((1,3,6,1,4,1,28507,56,1,5,2,1))
epc8221OVPEntry.setIndexNames((0,_A,_K))
if mibBuilder.loadTexts:epc8221OVPEntry.setStatus(_B)
class _Epc8221OVPIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_Epc8221OVPIndex_Type.__name__=_D
_Epc8221OVPIndex_Object=MibTableColumn
epc8221OVPIndex=_Epc8221OVPIndex_Object((1,3,6,1,4,1,28507,56,1,5,2,1,1),_Epc8221OVPIndex_Type())
epc8221OVPIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:epc8221OVPIndex.setStatus(_B)
class _Epc8221OVPStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('failure',0),('ok',1),('unknown',2)))
_Epc8221OVPStatus_Type.__name__=_D
_Epc8221OVPStatus_Object=MibTableColumn
epc8221OVPStatus=_Epc8221OVPStatus_Object((1,3,6,1,4,1,28507,56,1,5,2,1,2),_Epc8221OVPStatus_Type())
epc8221OVPStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:epc8221OVPStatus.setStatus(_B)
_Epc8221ExtSensors_ObjectIdentity=ObjectIdentity
epc8221ExtSensors=_Epc8221ExtSensors_ObjectIdentity((1,3,6,1,4,1,28507,56,1,6))
_Epc8221SensorTable_Object=MibTable
epc8221SensorTable=_Epc8221SensorTable_Object((1,3,6,1,4,1,28507,56,1,6,1))
if mibBuilder.loadTexts:epc8221SensorTable.setStatus(_B)
_Epc8221SensorEntry_Object=MibTableRow
epc8221SensorEntry=_Epc8221SensorEntry_Object((1,3,6,1,4,1,28507,56,1,6,1,1))
epc8221SensorEntry.setIndexNames((0,_A,_F))
if mibBuilder.loadTexts:epc8221SensorEntry.setStatus(_B)
class _Epc8221SensorIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_Epc8221SensorIndex_Type.__name__=_D
_Epc8221SensorIndex_Object=MibTableColumn
epc8221SensorIndex=_Epc8221SensorIndex_Object((1,3,6,1,4,1,28507,56,1,6,1,1,1),_Epc8221SensorIndex_Type())
epc8221SensorIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:epc8221SensorIndex.setStatus(_B)
_Epc8221TempSensor_Type=Integer32
_Epc8221TempSensor_Object=MibTableColumn
epc8221TempSensor=_Epc8221TempSensor_Object((1,3,6,1,4,1,28507,56,1,6,1,1,2),_Epc8221TempSensor_Type())
epc8221TempSensor.setMaxAccess(_C)
if mibBuilder.loadTexts:epc8221TempSensor.setStatus(_B)
if mibBuilder.loadTexts:epc8221TempSensor.setUnits(_O)
_Epc8221HygroSensor_Type=Integer32
_Epc8221HygroSensor_Object=MibTableColumn
epc8221HygroSensor=_Epc8221HygroSensor_Object((1,3,6,1,4,1,28507,56,1,6,1,1,3),_Epc8221HygroSensor_Type())
epc8221HygroSensor.setMaxAccess(_C)
if mibBuilder.loadTexts:epc8221HygroSensor.setStatus(_B)
if mibBuilder.loadTexts:epc8221HygroSensor.setUnits('0.1 percent humidity')
class _Epc8221InputSensor_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_N,0),('on',1)))
_Epc8221InputSensor_Type.__name__=_D
_Epc8221InputSensor_Object=MibTableColumn
epc8221InputSensor=_Epc8221InputSensor_Object((1,3,6,1,4,1,28507,56,1,6,1,1,4),_Epc8221InputSensor_Type())
epc8221InputSensor.setMaxAccess(_C)
if mibBuilder.loadTexts:epc8221InputSensor.setStatus(_B)
_Epc8221AirPressure_Type=Integer32
_Epc8221AirPressure_Object=MibTableColumn
epc8221AirPressure=_Epc8221AirPressure_Object((1,3,6,1,4,1,28507,56,1,6,1,1,5),_Epc8221AirPressure_Type())
epc8221AirPressure.setMaxAccess(_C)
if mibBuilder.loadTexts:epc8221AirPressure.setStatus(_B)
if mibBuilder.loadTexts:epc8221AirPressure.setUnits('1 hPA (hectopascal) ~ 1 milibar')
_Epc8221DewPoint_Type=Integer32
_Epc8221DewPoint_Object=MibTableColumn
epc8221DewPoint=_Epc8221DewPoint_Object((1,3,6,1,4,1,28507,56,1,6,1,1,6),_Epc8221DewPoint_Type())
epc8221DewPoint.setMaxAccess(_C)
if mibBuilder.loadTexts:epc8221DewPoint.setStatus(_B)
if mibBuilder.loadTexts:epc8221DewPoint.setUnits(_O)
_Epc8221DewPointDiff_Type=Integer32
_Epc8221DewPointDiff_Object=MibTableColumn
epc8221DewPointDiff=_Epc8221DewPointDiff_Object((1,3,6,1,4,1,28507,56,1,6,1,1,7),_Epc8221DewPointDiff_Type())
epc8221DewPointDiff.setMaxAccess(_C)
if mibBuilder.loadTexts:epc8221DewPointDiff.setStatus(_B)
if mibBuilder.loadTexts:epc8221DewPointDiff.setUnits(_O)
_Epc8221Conf_ObjectIdentity=ObjectIdentity
epc8221Conf=_Epc8221Conf_ObjectIdentity((1,3,6,1,4,1,28507,56,2))
_Epc8221Groups_ObjectIdentity=ObjectIdentity
epc8221Groups=_Epc8221Groups_ObjectIdentity((1,3,6,1,4,1,28507,56,2,1))
_Epc8221Compls_ObjectIdentity=ObjectIdentity
epc8221Compls=_Epc8221Compls_ObjectIdentity((1,3,6,1,4,1,28507,56,2,2))
_Events_ObjectIdentity=ObjectIdentity
events=_Events_ObjectIdentity((1,3,6,1,4,1,28507,56,3))
epc8221BasicGroup=ObjectGroup((1,3,6,1,4,1,28507,56,2,1,1))
epc8221BasicGroup.setObjects(*((_A,_g),(_A,_M),(_A,_h),(_A,_i),(_A,_I),(_A,_P),(_A,_Q),(_A,_R),(_A,_j),(_A,_k),(_A,_l),(_A,_m),(_A,_n),(_A,_J),(_A,_o),(_A,_p),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_q),(_A,_r),(_A,_W),(_A,_X),(_A,_s),(_A,_t),(_A,_u),(_A,_v),(_A,_w),(_A,_x),(_A,_y),(_A,_z),(_A,_A0),(_A,_A1),(_A,_A2),(_A,_A3),(_A,_K),(_A,_Y),(_A,_F),(_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_A4),(_A,_d)))
if mibBuilder.loadTexts:epc8221BasicGroup.setStatus(_B)
epc8221SwitchEvtPort=NotificationType((1,3,6,1,4,1,28507,56,3,1))
epc8221SwitchEvtPort.setObjects(*((_A,_I),(_A,_P),(_A,_Q),(_A,_R)))
if mibBuilder.loadTexts:epc8221SwitchEvtPort.setStatus(_B)
epc8221TempEvtSen=NotificationType((1,3,6,1,4,1,28507,56,3,2))
epc8221TempEvtSen.setObjects(*((_A,_F),(_A,_Z)))
if mibBuilder.loadTexts:epc8221TempEvtSen.setStatus(_B)
epc8221HygroEvtSen=NotificationType((1,3,6,1,4,1,28507,56,3,3))
epc8221HygroEvtSen.setObjects(*((_A,_F),(_A,_a)))
if mibBuilder.loadTexts:epc8221HygroEvtSen.setStatus(_B)
epc8221InputEvtSen=NotificationType((1,3,6,1,4,1,28507,56,3,4))
epc8221InputEvtSen.setObjects(*((_A,_F),(_A,_b)))
if mibBuilder.loadTexts:epc8221InputEvtSen.setStatus(_B)
epc8221AirPressureEvtSen=NotificationType((1,3,6,1,4,1,28507,56,3,5))
epc8221AirPressureEvtSen.setObjects(*((_A,_F),(_A,_c)))
if mibBuilder.loadTexts:epc8221AirPressureEvtSen.setStatus(_B)
epc8221DewPtDiffEvtSen=NotificationType((1,3,6,1,4,1,28507,56,3,6))
epc8221DewPtDiffEvtSen.setObjects(*((_A,_F),(_A,_d)))
if mibBuilder.loadTexts:epc8221DewPtDiffEvtSen.setStatus(_B)
epc8221OVPEvt=NotificationType((1,3,6,1,4,1,28507,56,3,7))
epc8221OVPEvt.setObjects(*((_A,_K),(_A,_Y)))
if mibBuilder.loadTexts:epc8221OVPEvt.setStatus(_B)
epc8221LineAmperageEvt=NotificationType((1,3,6,1,4,1,28507,56,3,8))
epc8221LineAmperageEvt.setObjects(*((_A,_J),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X)))
if mibBuilder.loadTexts:epc8221LineAmperageEvt.setStatus(_B)
epc8221NotificationGroup=NotificationGroup((1,3,6,1,4,1,28507,56,2,1,2))
epc8221NotificationGroup.setObjects(*((_A,_A5),(_A,_A6),(_A,_A7),(_A,_A8),(_A,_A9),(_A,_AA),(_A,_AB),(_A,_AC)))
if mibBuilder.loadTexts:epc8221NotificationGroup.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'gudeads':gudeads,'gadsEPC8221':gadsEPC8221,'epc8221Objects':epc8221Objects,'epc8221CommonConfig':epc8221CommonConfig,'epc8221SNMPaccess':epc8221SNMPaccess,_g:epc8221TrapCtrl,'epc8221TrapIPTable':epc8221TrapIPTable,'epc8221TrapIPEntry':epc8221TrapIPEntry,_M:epc8221TrapIPIndex,_h:epc8221TrapAddr,'epc8221DeviceConfig':epc8221DeviceConfig,'epc8221IntActors':epc8221IntActors,'epc8221relayports':epc8221relayports,_i:epc8221portNumber,'epc8221portTable':epc8221portTable,'epc8221portEntry':epc8221portEntry,_I:epc8221PortIndex,_P:epc8221PortName,_Q:epc8221PortState,_R:epc8221PortSwitchCount,_j:epc8221PortStartupMode,_k:epc8221PortStartupDelay,_l:epc8221PortRepowerTime,_m:epc8221Buzzer,'epc8221ExtActors':epc8221ExtActors,'epc8221IntSensors':epc8221IntSensors,'epc8221PowerChan':epc8221PowerChan,_n:epc8221ActivePowerChan,'epc8221PowerTable':epc8221PowerTable,'epc8221PowerEntry':epc8221PowerEntry,_J:epc8221PowerIndex,_o:epc8221ChanStatus,_p:epc8221AbsEnergyActive,_S:epc8221PowerActive,_T:epc8221Current,_U:epc8221Voltage,_V:epc8221Frequency,_q:epc8221PowerFactor,_r:epc8221Pangle,_W:epc8221PowerApparent,_X:epc8221PowerReactive,_s:epc8221AbsEnergyReactive,_t:epc8221AbsEnergyActiveResettable,_u:epc8221AbsEnergyReactiveResettable,_v:epc8221ResetTime,_w:epc8221ForwEnergyActive,_x:epc8221ForwEnergyReactive,_y:epc8221ForwEnergyActiveResettable,_z:epc8221ForwEnergyReactiveResettable,_A0:epc8221RevEnergyActive,_A1:epc8221RevEnergyReactive,_A2:epc8221RevEnergyActiveResettable,_A3:epc8221RevEnergyReactiveResettable,'epc8221OVPTable':epc8221OVPTable,'epc8221OVPEntry':epc8221OVPEntry,_K:epc8221OVPIndex,_Y:epc8221OVPStatus,'epc8221ExtSensors':epc8221ExtSensors,'epc8221SensorTable':epc8221SensorTable,'epc8221SensorEntry':epc8221SensorEntry,_F:epc8221SensorIndex,_Z:epc8221TempSensor,_a:epc8221HygroSensor,_b:epc8221InputSensor,_c:epc8221AirPressure,_A4:epc8221DewPoint,_d:epc8221DewPointDiff,'epc8221Conf':epc8221Conf,'epc8221Groups':epc8221Groups,'epc8221BasicGroup':epc8221BasicGroup,'epc8221NotificationGroup':epc8221NotificationGroup,'epc8221Compls':epc8221Compls,'events':events,_A5:epc8221SwitchEvtPort,_A6:epc8221TempEvtSen,_A7:epc8221HygroEvtSen,_A8:epc8221InputEvtSen,_A9:epc8221AirPressureEvtSen,_AA:epc8221DewPtDiffEvtSen,_AB:epc8221OVPEvt,_AC:epc8221LineAmperageEvt})