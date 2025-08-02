_Ad='epc8226PortAmperageEvt'
_Ac='epc8226LineAmperageEvt'
_Ab='epc8226OVPEvt'
_Aa='epc8226DewPtDiffEvtSen'
_AZ='epc8226AirPressureEvtSen'
_AY='epc8226InputEvtSen'
_AX='epc8226HygroEvtSen'
_AW='epc8226TempEvtSen'
_AV='epc8226SwitchEvtPort'
_AU='epc8226DewPoint'
_AT='epc8226spRevEnergyReactiveResettable'
_AS='epc8226spRevEnergyActiveResettable'
_AR='epc8226spRevEnergyReactive'
_AQ='epc8226spRevEnergyActive'
_AP='epc8226spForwEnergyReactiveResettable'
_AO='epc8226spForwEnergyActiveResettable'
_AN='epc8226spForwEnergyReactive'
_AM='epc8226spForwEnergyActive'
_AL='epc8226spResetTime'
_AK='epc8226spAbsEnergyReactiveResettable'
_AJ='epc8226spAbsEnergyActiveResettable'
_AI='epc8226spAbsEnergyReactive'
_AH='epc8226spPangle'
_AG='epc8226spPowerFactor'
_AF='epc8226spAbsEnergyActive'
_AE='epc8226spChanStatus'
_AD='epc8226spActivePowerChan'
_AC='epc8226RevEnergyReactiveResettable'
_AB='epc8226RevEnergyActiveResettable'
_AA='epc8226RevEnergyReactive'
_A9='epc8226RevEnergyActive'
_A8='epc8226ForwEnergyReactiveResettable'
_A7='epc8226ForwEnergyActiveResettable'
_A6='epc8226ForwEnergyReactive'
_A5='epc8226ForwEnergyActive'
_A4='epc8226ResetTime'
_A3='epc8226AbsEnergyReactiveResettable'
_A2='epc8226AbsEnergyActiveResettable'
_A1='epc8226AbsEnergyReactive'
_A0='epc8226Pangle'
_z='epc8226PowerFactor'
_y='epc8226AbsEnergyActive'
_x='epc8226ChanStatus'
_w='epc8226ActivePowerChan'
_v='epc8226Buzzer'
_u='epc8226PortRepowerTime'
_t='epc8226PortStartupDelay'
_s='epc8226PortStartupMode'
_r='epc8226portNumber'
_q='epc8226TrapAddr'
_p='epc8226TrapCtrl'
_o='0.1 degree'
_n='0.01 hz'
_m='seconds'
_l='epc8226DewPointDiff'
_k='epc8226AirPressure'
_j='epc8226InputSensor'
_i='epc8226HygroSensor'
_h='epc8226TempSensor'
_g='epc8226spPowerReactive'
_f='epc8226spPowerApparent'
_e='epc8226spFrequency'
_d='epc8226spVoltage'
_c='epc8226spCurrent'
_b='epc8226spPowerActive'
_a='epc8226OVPStatus'
_Z='epc8226PowerReactive'
_Y='epc8226PowerApparent'
_X='epc8226Frequency'
_W='epc8226Voltage'
_V='epc8226Current'
_U='epc8226PowerActive'
_T='epc8226PortSwitchCount'
_S='epc8226PortState'
_R='epc8226PortName'
_Q='0.1 degree Celsius'
_P='off'
_O='epc8226TrapIPIndex'
_N='Unsigned32'
_M='OctetString'
_L='epc8226spPowerIndex'
_K='epc8226OVPIndex'
_J='epc8226PowerIndex'
_I='epc8226PortIndex'
_H='epc8226SensorIndex'
_G='read-write'
_F='VARh'
_E='Wh'
_D='Integer32'
_C='read-only'
_B='current'
_A='GUDEADS-EPC8226-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_M,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_N,'enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
gudeads=ModuleIdentity((1,3,6,1,4,1,28507))
if mibBuilder.loadTexts:gudeads.setRevisions(('2007-03-05 13:56',))
_GadsEPC8226_ObjectIdentity=ObjectIdentity
gadsEPC8226=_GadsEPC8226_ObjectIdentity((1,3,6,1,4,1,28507,58))
_Epc8226Objects_ObjectIdentity=ObjectIdentity
epc8226Objects=_Epc8226Objects_ObjectIdentity((1,3,6,1,4,1,28507,58,1))
_Epc8226CommonConfig_ObjectIdentity=ObjectIdentity
epc8226CommonConfig=_Epc8226CommonConfig_ObjectIdentity((1,3,6,1,4,1,28507,58,1,1))
_Epc8226SNMPaccess_ObjectIdentity=ObjectIdentity
epc8226SNMPaccess=_Epc8226SNMPaccess_ObjectIdentity((1,3,6,1,4,1,28507,58,1,1,1))
class _Epc8226TrapCtrl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3))
_Epc8226TrapCtrl_Type.__name__=_D
_Epc8226TrapCtrl_Object=MibScalar
epc8226TrapCtrl=_Epc8226TrapCtrl_Object((1,3,6,1,4,1,28507,58,1,1,1,1),_Epc8226TrapCtrl_Type())
epc8226TrapCtrl.setMaxAccess(_G)
if mibBuilder.loadTexts:epc8226TrapCtrl.setStatus(_B)
_Epc8226TrapIPTable_Object=MibTable
epc8226TrapIPTable=_Epc8226TrapIPTable_Object((1,3,6,1,4,1,28507,58,1,1,1,2))
if mibBuilder.loadTexts:epc8226TrapIPTable.setStatus(_B)
_Epc8226TrapIPEntry_Object=MibTableRow
epc8226TrapIPEntry=_Epc8226TrapIPEntry_Object((1,3,6,1,4,1,28507,58,1,1,1,2,1))
epc8226TrapIPEntry.setIndexNames((0,_A,_O))
if mibBuilder.loadTexts:epc8226TrapIPEntry.setStatus(_B)
class _Epc8226TrapIPIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_Epc8226TrapIPIndex_Type.__name__=_D
_Epc8226TrapIPIndex_Object=MibTableColumn
epc8226TrapIPIndex=_Epc8226TrapIPIndex_Object((1,3,6,1,4,1,28507,58,1,1,1,2,1,1),_Epc8226TrapIPIndex_Type())
epc8226TrapIPIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:epc8226TrapIPIndex.setStatus(_B)
class _Epc8226TrapAddr_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,99))
_Epc8226TrapAddr_Type.__name__=_M
_Epc8226TrapAddr_Object=MibTableColumn
epc8226TrapAddr=_Epc8226TrapAddr_Object((1,3,6,1,4,1,28507,58,1,1,1,2,1,2),_Epc8226TrapAddr_Type())
epc8226TrapAddr.setMaxAccess(_G)
if mibBuilder.loadTexts:epc8226TrapAddr.setStatus(_B)
_Epc8226DeviceConfig_ObjectIdentity=ObjectIdentity
epc8226DeviceConfig=_Epc8226DeviceConfig_ObjectIdentity((1,3,6,1,4,1,28507,58,1,2))
_Epc8226IntActors_ObjectIdentity=ObjectIdentity
epc8226IntActors=_Epc8226IntActors_ObjectIdentity((1,3,6,1,4,1,28507,58,1,3))
_Epc8226relayports_ObjectIdentity=ObjectIdentity
epc8226relayports=_Epc8226relayports_ObjectIdentity((1,3,6,1,4,1,28507,58,1,3,1))
class _Epc8226portNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,12))
_Epc8226portNumber_Type.__name__=_D
_Epc8226portNumber_Object=MibScalar
epc8226portNumber=_Epc8226portNumber_Object((1,3,6,1,4,1,28507,58,1,3,1,1),_Epc8226portNumber_Type())
epc8226portNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:epc8226portNumber.setStatus(_B)
_Epc8226portTable_Object=MibTable
epc8226portTable=_Epc8226portTable_Object((1,3,6,1,4,1,28507,58,1,3,1,2))
if mibBuilder.loadTexts:epc8226portTable.setStatus(_B)
_Epc8226portEntry_Object=MibTableRow
epc8226portEntry=_Epc8226portEntry_Object((1,3,6,1,4,1,28507,58,1,3,1,2,1))
epc8226portEntry.setIndexNames((0,_A,_I))
if mibBuilder.loadTexts:epc8226portEntry.setStatus(_B)
class _Epc8226PortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,12))
_Epc8226PortIndex_Type.__name__=_D
_Epc8226PortIndex_Object=MibTableColumn
epc8226PortIndex=_Epc8226PortIndex_Object((1,3,6,1,4,1,28507,58,1,3,1,2,1,1),_Epc8226PortIndex_Type())
epc8226PortIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:epc8226PortIndex.setStatus(_B)
class _Epc8226PortName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_Epc8226PortName_Type.__name__=_M
_Epc8226PortName_Object=MibTableColumn
epc8226PortName=_Epc8226PortName_Object((1,3,6,1,4,1,28507,58,1,3,1,2,1,2),_Epc8226PortName_Type())
epc8226PortName.setMaxAccess(_G)
if mibBuilder.loadTexts:epc8226PortName.setStatus(_B)
class _Epc8226PortState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_P,0),('on',1)))
_Epc8226PortState_Type.__name__=_D
_Epc8226PortState_Object=MibTableColumn
epc8226PortState=_Epc8226PortState_Object((1,3,6,1,4,1,28507,58,1,3,1,2,1,3),_Epc8226PortState_Type())
epc8226PortState.setMaxAccess(_G)
if mibBuilder.loadTexts:epc8226PortState.setStatus(_B)
_Epc8226PortSwitchCount_Type=Integer32
_Epc8226PortSwitchCount_Object=MibTableColumn
epc8226PortSwitchCount=_Epc8226PortSwitchCount_Object((1,3,6,1,4,1,28507,58,1,3,1,2,1,4),_Epc8226PortSwitchCount_Type())
epc8226PortSwitchCount.setMaxAccess(_C)
if mibBuilder.loadTexts:epc8226PortSwitchCount.setStatus(_B)
class _Epc8226PortStartupMode_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_P,0),('on',1),('laststate',2)))
_Epc8226PortStartupMode_Type.__name__=_D
_Epc8226PortStartupMode_Object=MibTableColumn
epc8226PortStartupMode=_Epc8226PortStartupMode_Object((1,3,6,1,4,1,28507,58,1,3,1,2,1,5),_Epc8226PortStartupMode_Type())
epc8226PortStartupMode.setMaxAccess(_G)
if mibBuilder.loadTexts:epc8226PortStartupMode.setStatus(_B)
class _Epc8226PortStartupDelay_Type(Integer32):defaultValue=0
_Epc8226PortStartupDelay_Type.__name__=_D
_Epc8226PortStartupDelay_Object=MibTableColumn
epc8226PortStartupDelay=_Epc8226PortStartupDelay_Object((1,3,6,1,4,1,28507,58,1,3,1,2,1,6),_Epc8226PortStartupDelay_Type())
epc8226PortStartupDelay.setMaxAccess(_G)
if mibBuilder.loadTexts:epc8226PortStartupDelay.setStatus(_B)
if mibBuilder.loadTexts:epc8226PortStartupDelay.setUnits(_m)
class _Epc8226PortRepowerTime_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Epc8226PortRepowerTime_Type.__name__=_D
_Epc8226PortRepowerTime_Object=MibTableColumn
epc8226PortRepowerTime=_Epc8226PortRepowerTime_Object((1,3,6,1,4,1,28507,58,1,3,1,2,1,7),_Epc8226PortRepowerTime_Type())
epc8226PortRepowerTime.setMaxAccess(_G)
if mibBuilder.loadTexts:epc8226PortRepowerTime.setStatus(_B)
if mibBuilder.loadTexts:epc8226PortRepowerTime.setUnits(_m)
class _Epc8226Buzzer_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Epc8226Buzzer_Type.__name__=_D
_Epc8226Buzzer_Object=MibScalar
epc8226Buzzer=_Epc8226Buzzer_Object((1,3,6,1,4,1,28507,58,1,3,10),_Epc8226Buzzer_Type())
epc8226Buzzer.setMaxAccess(_G)
if mibBuilder.loadTexts:epc8226Buzzer.setStatus(_B)
if mibBuilder.loadTexts:epc8226Buzzer.setUnits('0 = Off, 1 = On')
_Epc8226ExtActors_ObjectIdentity=ObjectIdentity
epc8226ExtActors=_Epc8226ExtActors_ObjectIdentity((1,3,6,1,4,1,28507,58,1,4))
_Epc8226IntSensors_ObjectIdentity=ObjectIdentity
epc8226IntSensors=_Epc8226IntSensors_ObjectIdentity((1,3,6,1,4,1,28507,58,1,5))
_Epc8226PowerChan_ObjectIdentity=ObjectIdentity
epc8226PowerChan=_Epc8226PowerChan_ObjectIdentity((1,3,6,1,4,1,28507,58,1,5,1))
class _Epc8226ActivePowerChan_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1))
_Epc8226ActivePowerChan_Type.__name__=_N
_Epc8226ActivePowerChan_Object=MibScalar
epc8226ActivePowerChan=_Epc8226ActivePowerChan_Object((1,3,6,1,4,1,28507,58,1,5,1,1),_Epc8226ActivePowerChan_Type())
epc8226ActivePowerChan.setMaxAccess(_C)
if mibBuilder.loadTexts:epc8226ActivePowerChan.setStatus(_B)
_Epc8226PowerTable_Object=MibTable
epc8226PowerTable=_Epc8226PowerTable_Object((1,3,6,1,4,1,28507,58,1,5,1,2))
if mibBuilder.loadTexts:epc8226PowerTable.setStatus(_B)
_Epc8226PowerEntry_Object=MibTableRow
epc8226PowerEntry=_Epc8226PowerEntry_Object((1,3,6,1,4,1,28507,58,1,5,1,2,1))
epc8226PowerEntry.setIndexNames((0,_A,_J))
if mibBuilder.loadTexts:epc8226PowerEntry.setStatus(_B)
class _Epc8226PowerIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_Epc8226PowerIndex_Type.__name__=_D
_Epc8226PowerIndex_Object=MibTableColumn
epc8226PowerIndex=_Epc8226PowerIndex_Object((1,3,6,1,4,1,28507,58,1,5,1,2,1,1),_Epc8226PowerIndex_Type())
epc8226PowerIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:epc8226PowerIndex.setStatus(_B)
class _Epc8226ChanStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Epc8226ChanStatus_Type.__name__=_D
_Epc8226ChanStatus_Object=MibTableColumn
epc8226ChanStatus=_Epc8226ChanStatus_Object((1,3,6,1,4,1,28507,58,1,5,1,2,1,2),_Epc8226ChanStatus_Type())
epc8226ChanStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:epc8226ChanStatus.setStatus(_B)
_Epc8226AbsEnergyActive_Type=Gauge32
_Epc8226AbsEnergyActive_Object=MibTableColumn
epc8226AbsEnergyActive=_Epc8226AbsEnergyActive_Object((1,3,6,1,4,1,28507,58,1,5,1,2,1,3),_Epc8226AbsEnergyActive_Type())
epc8226AbsEnergyActive.setMaxAccess(_C)
if mibBuilder.loadTexts:epc8226AbsEnergyActive.setStatus(_B)
if mibBuilder.loadTexts:epc8226AbsEnergyActive.setUnits(_E)
_Epc8226PowerActive_Type=Integer32
_Epc8226PowerActive_Object=MibTableColumn
epc8226PowerActive=_Epc8226PowerActive_Object((1,3,6,1,4,1,28507,58,1,5,1,2,1,4),_Epc8226PowerActive_Type())
epc8226PowerActive.setMaxAccess(_C)
if mibBuilder.loadTexts:epc8226PowerActive.setStatus(_B)
if mibBuilder.loadTexts:epc8226PowerActive.setUnits('W')
_Epc8226Current_Type=Gauge32
_Epc8226Current_Object=MibTableColumn
epc8226Current=_Epc8226Current_Object((1,3,6,1,4,1,28507,58,1,5,1,2,1,5),_Epc8226Current_Type())
epc8226Current.setMaxAccess(_C)
if mibBuilder.loadTexts:epc8226Current.setStatus(_B)
if mibBuilder.loadTexts:epc8226Current.setUnits('mA')
_Epc8226Voltage_Type=Gauge32
_Epc8226Voltage_Object=MibTableColumn
epc8226Voltage=_Epc8226Voltage_Object((1,3,6,1,4,1,28507,58,1,5,1,2,1,6),_Epc8226Voltage_Type())
epc8226Voltage.setMaxAccess(_C)
if mibBuilder.loadTexts:epc8226Voltage.setStatus(_B)
if mibBuilder.loadTexts:epc8226Voltage.setUnits('V')
_Epc8226Frequency_Type=Gauge32
_Epc8226Frequency_Object=MibTableColumn
epc8226Frequency=_Epc8226Frequency_Object((1,3,6,1,4,1,28507,58,1,5,1,2,1,7),_Epc8226Frequency_Type())
epc8226Frequency.setMaxAccess(_C)
if mibBuilder.loadTexts:epc8226Frequency.setStatus(_B)
if mibBuilder.loadTexts:epc8226Frequency.setUnits(_n)
_Epc8226PowerFactor_Type=Integer32
_Epc8226PowerFactor_Object=MibTableColumn
epc8226PowerFactor=_Epc8226PowerFactor_Object((1,3,6,1,4,1,28507,58,1,5,1,2,1,8),_Epc8226PowerFactor_Type())
epc8226PowerFactor.setMaxAccess(_C)
if mibBuilder.loadTexts:epc8226PowerFactor.setStatus(_B)
if mibBuilder.loadTexts:epc8226PowerFactor.setUnits('0.001')
_Epc8226Pangle_Type=Integer32
_Epc8226Pangle_Object=MibTableColumn
epc8226Pangle=_Epc8226Pangle_Object((1,3,6,1,4,1,28507,58,1,5,1,2,1,9),_Epc8226Pangle_Type())
epc8226Pangle.setMaxAccess(_C)
if mibBuilder.loadTexts:epc8226Pangle.setStatus(_B)
if mibBuilder.loadTexts:epc8226Pangle.setUnits(_o)
_Epc8226PowerApparent_Type=Integer32
_Epc8226PowerApparent_Object=MibTableColumn
epc8226PowerApparent=_Epc8226PowerApparent_Object((1,3,6,1,4,1,28507,58,1,5,1,2,1,10),_Epc8226PowerApparent_Type())
epc8226PowerApparent.setMaxAccess(_C)
if mibBuilder.loadTexts:epc8226PowerApparent.setStatus(_B)
if mibBuilder.loadTexts:epc8226PowerApparent.setUnits('VA')
_Epc8226PowerReactive_Type=Integer32
_Epc8226PowerReactive_Object=MibTableColumn
epc8226PowerReactive=_Epc8226PowerReactive_Object((1,3,6,1,4,1,28507,58,1,5,1,2,1,11),_Epc8226PowerReactive_Type())
epc8226PowerReactive.setMaxAccess(_C)
if mibBuilder.loadTexts:epc8226PowerReactive.setStatus(_B)
if mibBuilder.loadTexts:epc8226PowerReactive.setUnits('VAR')
_Epc8226AbsEnergyReactive_Type=Gauge32
_Epc8226AbsEnergyReactive_Object=MibTableColumn
epc8226AbsEnergyReactive=_Epc8226AbsEnergyReactive_Object((1,3,6,1,4,1,28507,58,1,5,1,2,1,12),_Epc8226AbsEnergyReactive_Type())
epc8226AbsEnergyReactive.setMaxAccess(_C)
if mibBuilder.loadTexts:epc8226AbsEnergyReactive.setStatus(_B)
if mibBuilder.loadTexts:epc8226AbsEnergyReactive.setUnits(_F)
_Epc8226AbsEnergyActiveResettable_Type=Gauge32
_Epc8226AbsEnergyActiveResettable_Object=MibTableColumn
epc8226AbsEnergyActiveResettable=_Epc8226AbsEnergyActiveResettable_Object((1,3,6,1,4,1,28507,58,1,5,1,2,1,13),_Epc8226AbsEnergyActiveResettable_Type())
epc8226AbsEnergyActiveResettable.setMaxAccess(_G)
if mibBuilder.loadTexts:epc8226AbsEnergyActiveResettable.setStatus(_B)
if mibBuilder.loadTexts:epc8226AbsEnergyActiveResettable.setUnits(_E)
_Epc8226AbsEnergyReactiveResettable_Type=Gauge32
_Epc8226AbsEnergyReactiveResettable_Object=MibTableColumn
epc8226AbsEnergyReactiveResettable=_Epc8226AbsEnergyReactiveResettable_Object((1,3,6,1,4,1,28507,58,1,5,1,2,1,14),_Epc8226AbsEnergyReactiveResettable_Type())
epc8226AbsEnergyReactiveResettable.setMaxAccess(_C)
if mibBuilder.loadTexts:epc8226AbsEnergyReactiveResettable.setStatus(_B)
if mibBuilder.loadTexts:epc8226AbsEnergyReactiveResettable.setUnits(_F)
_Epc8226ResetTime_Type=Gauge32
_Epc8226ResetTime_Object=MibTableColumn
epc8226ResetTime=_Epc8226ResetTime_Object((1,3,6,1,4,1,28507,58,1,5,1,2,1,15),_Epc8226ResetTime_Type())
epc8226ResetTime.setMaxAccess(_C)
if mibBuilder.loadTexts:epc8226ResetTime.setStatus(_B)
if mibBuilder.loadTexts:epc8226ResetTime.setUnits('s')
_Epc8226ForwEnergyActive_Type=Gauge32
_Epc8226ForwEnergyActive_Object=MibTableColumn
epc8226ForwEnergyActive=_Epc8226ForwEnergyActive_Object((1,3,6,1,4,1,28507,58,1,5,1,2,1,16),_Epc8226ForwEnergyActive_Type())
epc8226ForwEnergyActive.setMaxAccess(_C)
if mibBuilder.loadTexts:epc8226ForwEnergyActive.setStatus(_B)
if mibBuilder.loadTexts:epc8226ForwEnergyActive.setUnits(_E)
_Epc8226ForwEnergyReactive_Type=Gauge32
_Epc8226ForwEnergyReactive_Object=MibTableColumn
epc8226ForwEnergyReactive=_Epc8226ForwEnergyReactive_Object((1,3,6,1,4,1,28507,58,1,5,1,2,1,17),_Epc8226ForwEnergyReactive_Type())
epc8226ForwEnergyReactive.setMaxAccess(_C)
if mibBuilder.loadTexts:epc8226ForwEnergyReactive.setStatus(_B)
if mibBuilder.loadTexts:epc8226ForwEnergyReactive.setUnits(_F)
_Epc8226ForwEnergyActiveResettable_Type=Gauge32
_Epc8226ForwEnergyActiveResettable_Object=MibTableColumn
epc8226ForwEnergyActiveResettable=_Epc8226ForwEnergyActiveResettable_Object((1,3,6,1,4,1,28507,58,1,5,1,2,1,18),_Epc8226ForwEnergyActiveResettable_Type())
epc8226ForwEnergyActiveResettable.setMaxAccess(_C)
if mibBuilder.loadTexts:epc8226ForwEnergyActiveResettable.setStatus(_B)
if mibBuilder.loadTexts:epc8226ForwEnergyActiveResettable.setUnits(_E)
_Epc8226ForwEnergyReactiveResettable_Type=Gauge32
_Epc8226ForwEnergyReactiveResettable_Object=MibTableColumn
epc8226ForwEnergyReactiveResettable=_Epc8226ForwEnergyReactiveResettable_Object((1,3,6,1,4,1,28507,58,1,5,1,2,1,19),_Epc8226ForwEnergyReactiveResettable_Type())
epc8226ForwEnergyReactiveResettable.setMaxAccess(_C)
if mibBuilder.loadTexts:epc8226ForwEnergyReactiveResettable.setStatus(_B)
if mibBuilder.loadTexts:epc8226ForwEnergyReactiveResettable.setUnits(_F)
_Epc8226RevEnergyActive_Type=Gauge32
_Epc8226RevEnergyActive_Object=MibTableColumn
epc8226RevEnergyActive=_Epc8226RevEnergyActive_Object((1,3,6,1,4,1,28507,58,1,5,1,2,1,20),_Epc8226RevEnergyActive_Type())
epc8226RevEnergyActive.setMaxAccess(_C)
if mibBuilder.loadTexts:epc8226RevEnergyActive.setStatus(_B)
if mibBuilder.loadTexts:epc8226RevEnergyActive.setUnits(_E)
_Epc8226RevEnergyReactive_Type=Gauge32
_Epc8226RevEnergyReactive_Object=MibTableColumn
epc8226RevEnergyReactive=_Epc8226RevEnergyReactive_Object((1,3,6,1,4,1,28507,58,1,5,1,2,1,21),_Epc8226RevEnergyReactive_Type())
epc8226RevEnergyReactive.setMaxAccess(_C)
if mibBuilder.loadTexts:epc8226RevEnergyReactive.setStatus(_B)
if mibBuilder.loadTexts:epc8226RevEnergyReactive.setUnits(_F)
_Epc8226RevEnergyActiveResettable_Type=Gauge32
_Epc8226RevEnergyActiveResettable_Object=MibTableColumn
epc8226RevEnergyActiveResettable=_Epc8226RevEnergyActiveResettable_Object((1,3,6,1,4,1,28507,58,1,5,1,2,1,22),_Epc8226RevEnergyActiveResettable_Type())
epc8226RevEnergyActiveResettable.setMaxAccess(_C)
if mibBuilder.loadTexts:epc8226RevEnergyActiveResettable.setStatus(_B)
if mibBuilder.loadTexts:epc8226RevEnergyActiveResettable.setUnits(_E)
_Epc8226RevEnergyReactiveResettable_Type=Gauge32
_Epc8226RevEnergyReactiveResettable_Object=MibTableColumn
epc8226RevEnergyReactiveResettable=_Epc8226RevEnergyReactiveResettable_Object((1,3,6,1,4,1,28507,58,1,5,1,2,1,23),_Epc8226RevEnergyReactiveResettable_Type())
epc8226RevEnergyReactiveResettable.setMaxAccess(_C)
if mibBuilder.loadTexts:epc8226RevEnergyReactiveResettable.setStatus(_B)
if mibBuilder.loadTexts:epc8226RevEnergyReactiveResettable.setUnits(_F)
_Epc8226OVPTable_Object=MibTable
epc8226OVPTable=_Epc8226OVPTable_Object((1,3,6,1,4,1,28507,58,1,5,2))
if mibBuilder.loadTexts:epc8226OVPTable.setStatus(_B)
_Epc8226OVPEntry_Object=MibTableRow
epc8226OVPEntry=_Epc8226OVPEntry_Object((1,3,6,1,4,1,28507,58,1,5,2,1))
epc8226OVPEntry.setIndexNames((0,_A,_K))
if mibBuilder.loadTexts:epc8226OVPEntry.setStatus(_B)
class _Epc8226OVPIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_Epc8226OVPIndex_Type.__name__=_D
_Epc8226OVPIndex_Object=MibTableColumn
epc8226OVPIndex=_Epc8226OVPIndex_Object((1,3,6,1,4,1,28507,58,1,5,2,1,1),_Epc8226OVPIndex_Type())
epc8226OVPIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:epc8226OVPIndex.setStatus(_B)
class _Epc8226OVPStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('failure',0),('ok',1),('unknown',2)))
_Epc8226OVPStatus_Type.__name__=_D
_Epc8226OVPStatus_Object=MibTableColumn
epc8226OVPStatus=_Epc8226OVPStatus_Object((1,3,6,1,4,1,28507,58,1,5,2,1,2),_Epc8226OVPStatus_Type())
epc8226OVPStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:epc8226OVPStatus.setStatus(_B)
_Epc8226SinglePortPowerChan_ObjectIdentity=ObjectIdentity
epc8226SinglePortPowerChan=_Epc8226SinglePortPowerChan_ObjectIdentity((1,3,6,1,4,1,28507,58,1,5,5))
class _Epc8226spActivePowerChan_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1))
_Epc8226spActivePowerChan_Type.__name__=_N
_Epc8226spActivePowerChan_Object=MibScalar
epc8226spActivePowerChan=_Epc8226spActivePowerChan_Object((1,3,6,1,4,1,28507,58,1,5,5,1),_Epc8226spActivePowerChan_Type())
epc8226spActivePowerChan.setMaxAccess(_C)
if mibBuilder.loadTexts:epc8226spActivePowerChan.setStatus(_B)
_Epc8226spPowerTable_Object=MibTable
epc8226spPowerTable=_Epc8226spPowerTable_Object((1,3,6,1,4,1,28507,58,1,5,5,2))
if mibBuilder.loadTexts:epc8226spPowerTable.setStatus(_B)
_Epc8226spPowerEntry_Object=MibTableRow
epc8226spPowerEntry=_Epc8226spPowerEntry_Object((1,3,6,1,4,1,28507,58,1,5,5,2,1))
epc8226spPowerEntry.setIndexNames((0,_A,_L))
if mibBuilder.loadTexts:epc8226spPowerEntry.setStatus(_B)
class _Epc8226spPowerIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,12))
_Epc8226spPowerIndex_Type.__name__=_D
_Epc8226spPowerIndex_Object=MibTableColumn
epc8226spPowerIndex=_Epc8226spPowerIndex_Object((1,3,6,1,4,1,28507,58,1,5,5,2,1,1),_Epc8226spPowerIndex_Type())
epc8226spPowerIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:epc8226spPowerIndex.setStatus(_B)
class _Epc8226spChanStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Epc8226spChanStatus_Type.__name__=_D
_Epc8226spChanStatus_Object=MibTableColumn
epc8226spChanStatus=_Epc8226spChanStatus_Object((1,3,6,1,4,1,28507,58,1,5,5,2,1,2),_Epc8226spChanStatus_Type())
epc8226spChanStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:epc8226spChanStatus.setStatus(_B)
_Epc8226spAbsEnergyActive_Type=Gauge32
_Epc8226spAbsEnergyActive_Object=MibTableColumn
epc8226spAbsEnergyActive=_Epc8226spAbsEnergyActive_Object((1,3,6,1,4,1,28507,58,1,5,5,2,1,3),_Epc8226spAbsEnergyActive_Type())
epc8226spAbsEnergyActive.setMaxAccess(_C)
if mibBuilder.loadTexts:epc8226spAbsEnergyActive.setStatus(_B)
if mibBuilder.loadTexts:epc8226spAbsEnergyActive.setUnits(_E)
_Epc8226spPowerActive_Type=Integer32
_Epc8226spPowerActive_Object=MibTableColumn
epc8226spPowerActive=_Epc8226spPowerActive_Object((1,3,6,1,4,1,28507,58,1,5,5,2,1,4),_Epc8226spPowerActive_Type())
epc8226spPowerActive.setMaxAccess(_C)
if mibBuilder.loadTexts:epc8226spPowerActive.setStatus(_B)
if mibBuilder.loadTexts:epc8226spPowerActive.setUnits('W')
_Epc8226spCurrent_Type=Gauge32
_Epc8226spCurrent_Object=MibTableColumn
epc8226spCurrent=_Epc8226spCurrent_Object((1,3,6,1,4,1,28507,58,1,5,5,2,1,5),_Epc8226spCurrent_Type())
epc8226spCurrent.setMaxAccess(_C)
if mibBuilder.loadTexts:epc8226spCurrent.setStatus(_B)
if mibBuilder.loadTexts:epc8226spCurrent.setUnits('mA')
_Epc8226spVoltage_Type=Gauge32
_Epc8226spVoltage_Object=MibTableColumn
epc8226spVoltage=_Epc8226spVoltage_Object((1,3,6,1,4,1,28507,58,1,5,5,2,1,6),_Epc8226spVoltage_Type())
epc8226spVoltage.setMaxAccess(_C)
if mibBuilder.loadTexts:epc8226spVoltage.setStatus(_B)
if mibBuilder.loadTexts:epc8226spVoltage.setUnits('V')
_Epc8226spFrequency_Type=Gauge32
_Epc8226spFrequency_Object=MibTableColumn
epc8226spFrequency=_Epc8226spFrequency_Object((1,3,6,1,4,1,28507,58,1,5,5,2,1,7),_Epc8226spFrequency_Type())
epc8226spFrequency.setMaxAccess(_C)
if mibBuilder.loadTexts:epc8226spFrequency.setStatus(_B)
if mibBuilder.loadTexts:epc8226spFrequency.setUnits(_n)
_Epc8226spPowerFactor_Type=Integer32
_Epc8226spPowerFactor_Object=MibTableColumn
epc8226spPowerFactor=_Epc8226spPowerFactor_Object((1,3,6,1,4,1,28507,58,1,5,5,2,1,8),_Epc8226spPowerFactor_Type())
epc8226spPowerFactor.setMaxAccess(_C)
if mibBuilder.loadTexts:epc8226spPowerFactor.setStatus(_B)
if mibBuilder.loadTexts:epc8226spPowerFactor.setUnits('0.001')
_Epc8226spPangle_Type=Integer32
_Epc8226spPangle_Object=MibTableColumn
epc8226spPangle=_Epc8226spPangle_Object((1,3,6,1,4,1,28507,58,1,5,5,2,1,9),_Epc8226spPangle_Type())
epc8226spPangle.setMaxAccess(_C)
if mibBuilder.loadTexts:epc8226spPangle.setStatus(_B)
if mibBuilder.loadTexts:epc8226spPangle.setUnits(_o)
_Epc8226spPowerApparent_Type=Integer32
_Epc8226spPowerApparent_Object=MibTableColumn
epc8226spPowerApparent=_Epc8226spPowerApparent_Object((1,3,6,1,4,1,28507,58,1,5,5,2,1,10),_Epc8226spPowerApparent_Type())
epc8226spPowerApparent.setMaxAccess(_C)
if mibBuilder.loadTexts:epc8226spPowerApparent.setStatus(_B)
if mibBuilder.loadTexts:epc8226spPowerApparent.setUnits('VA')
_Epc8226spPowerReactive_Type=Integer32
_Epc8226spPowerReactive_Object=MibTableColumn
epc8226spPowerReactive=_Epc8226spPowerReactive_Object((1,3,6,1,4,1,28507,58,1,5,5,2,1,11),_Epc8226spPowerReactive_Type())
epc8226spPowerReactive.setMaxAccess(_C)
if mibBuilder.loadTexts:epc8226spPowerReactive.setStatus(_B)
if mibBuilder.loadTexts:epc8226spPowerReactive.setUnits('VAR')
_Epc8226spAbsEnergyReactive_Type=Gauge32
_Epc8226spAbsEnergyReactive_Object=MibTableColumn
epc8226spAbsEnergyReactive=_Epc8226spAbsEnergyReactive_Object((1,3,6,1,4,1,28507,58,1,5,5,2,1,12),_Epc8226spAbsEnergyReactive_Type())
epc8226spAbsEnergyReactive.setMaxAccess(_C)
if mibBuilder.loadTexts:epc8226spAbsEnergyReactive.setStatus(_B)
if mibBuilder.loadTexts:epc8226spAbsEnergyReactive.setUnits(_F)
_Epc8226spAbsEnergyActiveResettable_Type=Gauge32
_Epc8226spAbsEnergyActiveResettable_Object=MibTableColumn
epc8226spAbsEnergyActiveResettable=_Epc8226spAbsEnergyActiveResettable_Object((1,3,6,1,4,1,28507,58,1,5,5,2,1,13),_Epc8226spAbsEnergyActiveResettable_Type())
epc8226spAbsEnergyActiveResettable.setMaxAccess(_G)
if mibBuilder.loadTexts:epc8226spAbsEnergyActiveResettable.setStatus(_B)
if mibBuilder.loadTexts:epc8226spAbsEnergyActiveResettable.setUnits(_E)
_Epc8226spAbsEnergyReactiveResettable_Type=Gauge32
_Epc8226spAbsEnergyReactiveResettable_Object=MibTableColumn
epc8226spAbsEnergyReactiveResettable=_Epc8226spAbsEnergyReactiveResettable_Object((1,3,6,1,4,1,28507,58,1,5,5,2,1,14),_Epc8226spAbsEnergyReactiveResettable_Type())
epc8226spAbsEnergyReactiveResettable.setMaxAccess(_C)
if mibBuilder.loadTexts:epc8226spAbsEnergyReactiveResettable.setStatus(_B)
if mibBuilder.loadTexts:epc8226spAbsEnergyReactiveResettable.setUnits(_F)
_Epc8226spResetTime_Type=Gauge32
_Epc8226spResetTime_Object=MibTableColumn
epc8226spResetTime=_Epc8226spResetTime_Object((1,3,6,1,4,1,28507,58,1,5,5,2,1,15),_Epc8226spResetTime_Type())
epc8226spResetTime.setMaxAccess(_C)
if mibBuilder.loadTexts:epc8226spResetTime.setStatus(_B)
if mibBuilder.loadTexts:epc8226spResetTime.setUnits('s')
_Epc8226spForwEnergyActive_Type=Gauge32
_Epc8226spForwEnergyActive_Object=MibTableColumn
epc8226spForwEnergyActive=_Epc8226spForwEnergyActive_Object((1,3,6,1,4,1,28507,58,1,5,5,2,1,16),_Epc8226spForwEnergyActive_Type())
epc8226spForwEnergyActive.setMaxAccess(_C)
if mibBuilder.loadTexts:epc8226spForwEnergyActive.setStatus(_B)
if mibBuilder.loadTexts:epc8226spForwEnergyActive.setUnits(_E)
_Epc8226spForwEnergyReactive_Type=Gauge32
_Epc8226spForwEnergyReactive_Object=MibTableColumn
epc8226spForwEnergyReactive=_Epc8226spForwEnergyReactive_Object((1,3,6,1,4,1,28507,58,1,5,5,2,1,17),_Epc8226spForwEnergyReactive_Type())
epc8226spForwEnergyReactive.setMaxAccess(_C)
if mibBuilder.loadTexts:epc8226spForwEnergyReactive.setStatus(_B)
if mibBuilder.loadTexts:epc8226spForwEnergyReactive.setUnits(_F)
_Epc8226spForwEnergyActiveResettable_Type=Gauge32
_Epc8226spForwEnergyActiveResettable_Object=MibTableColumn
epc8226spForwEnergyActiveResettable=_Epc8226spForwEnergyActiveResettable_Object((1,3,6,1,4,1,28507,58,1,5,5,2,1,18),_Epc8226spForwEnergyActiveResettable_Type())
epc8226spForwEnergyActiveResettable.setMaxAccess(_C)
if mibBuilder.loadTexts:epc8226spForwEnergyActiveResettable.setStatus(_B)
if mibBuilder.loadTexts:epc8226spForwEnergyActiveResettable.setUnits(_E)
_Epc8226spForwEnergyReactiveResettable_Type=Gauge32
_Epc8226spForwEnergyReactiveResettable_Object=MibTableColumn
epc8226spForwEnergyReactiveResettable=_Epc8226spForwEnergyReactiveResettable_Object((1,3,6,1,4,1,28507,58,1,5,5,2,1,19),_Epc8226spForwEnergyReactiveResettable_Type())
epc8226spForwEnergyReactiveResettable.setMaxAccess(_C)
if mibBuilder.loadTexts:epc8226spForwEnergyReactiveResettable.setStatus(_B)
if mibBuilder.loadTexts:epc8226spForwEnergyReactiveResettable.setUnits(_F)
_Epc8226spRevEnergyActive_Type=Gauge32
_Epc8226spRevEnergyActive_Object=MibTableColumn
epc8226spRevEnergyActive=_Epc8226spRevEnergyActive_Object((1,3,6,1,4,1,28507,58,1,5,5,2,1,20),_Epc8226spRevEnergyActive_Type())
epc8226spRevEnergyActive.setMaxAccess(_C)
if mibBuilder.loadTexts:epc8226spRevEnergyActive.setStatus(_B)
if mibBuilder.loadTexts:epc8226spRevEnergyActive.setUnits(_E)
_Epc8226spRevEnergyReactive_Type=Gauge32
_Epc8226spRevEnergyReactive_Object=MibTableColumn
epc8226spRevEnergyReactive=_Epc8226spRevEnergyReactive_Object((1,3,6,1,4,1,28507,58,1,5,5,2,1,21),_Epc8226spRevEnergyReactive_Type())
epc8226spRevEnergyReactive.setMaxAccess(_C)
if mibBuilder.loadTexts:epc8226spRevEnergyReactive.setStatus(_B)
if mibBuilder.loadTexts:epc8226spRevEnergyReactive.setUnits(_F)
_Epc8226spRevEnergyActiveResettable_Type=Gauge32
_Epc8226spRevEnergyActiveResettable_Object=MibTableColumn
epc8226spRevEnergyActiveResettable=_Epc8226spRevEnergyActiveResettable_Object((1,3,6,1,4,1,28507,58,1,5,5,2,1,22),_Epc8226spRevEnergyActiveResettable_Type())
epc8226spRevEnergyActiveResettable.setMaxAccess(_C)
if mibBuilder.loadTexts:epc8226spRevEnergyActiveResettable.setStatus(_B)
if mibBuilder.loadTexts:epc8226spRevEnergyActiveResettable.setUnits(_E)
_Epc8226spRevEnergyReactiveResettable_Type=Gauge32
_Epc8226spRevEnergyReactiveResettable_Object=MibTableColumn
epc8226spRevEnergyReactiveResettable=_Epc8226spRevEnergyReactiveResettable_Object((1,3,6,1,4,1,28507,58,1,5,5,2,1,23),_Epc8226spRevEnergyReactiveResettable_Type())
epc8226spRevEnergyReactiveResettable.setMaxAccess(_C)
if mibBuilder.loadTexts:epc8226spRevEnergyReactiveResettable.setStatus(_B)
if mibBuilder.loadTexts:epc8226spRevEnergyReactiveResettable.setUnits(_F)
_Epc8226ExtSensors_ObjectIdentity=ObjectIdentity
epc8226ExtSensors=_Epc8226ExtSensors_ObjectIdentity((1,3,6,1,4,1,28507,58,1,6))
_Epc8226SensorTable_Object=MibTable
epc8226SensorTable=_Epc8226SensorTable_Object((1,3,6,1,4,1,28507,58,1,6,1))
if mibBuilder.loadTexts:epc8226SensorTable.setStatus(_B)
_Epc8226SensorEntry_Object=MibTableRow
epc8226SensorEntry=_Epc8226SensorEntry_Object((1,3,6,1,4,1,28507,58,1,6,1,1))
epc8226SensorEntry.setIndexNames((0,_A,_H))
if mibBuilder.loadTexts:epc8226SensorEntry.setStatus(_B)
class _Epc8226SensorIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_Epc8226SensorIndex_Type.__name__=_D
_Epc8226SensorIndex_Object=MibTableColumn
epc8226SensorIndex=_Epc8226SensorIndex_Object((1,3,6,1,4,1,28507,58,1,6,1,1,1),_Epc8226SensorIndex_Type())
epc8226SensorIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:epc8226SensorIndex.setStatus(_B)
_Epc8226TempSensor_Type=Integer32
_Epc8226TempSensor_Object=MibTableColumn
epc8226TempSensor=_Epc8226TempSensor_Object((1,3,6,1,4,1,28507,58,1,6,1,1,2),_Epc8226TempSensor_Type())
epc8226TempSensor.setMaxAccess(_C)
if mibBuilder.loadTexts:epc8226TempSensor.setStatus(_B)
if mibBuilder.loadTexts:epc8226TempSensor.setUnits(_Q)
_Epc8226HygroSensor_Type=Integer32
_Epc8226HygroSensor_Object=MibTableColumn
epc8226HygroSensor=_Epc8226HygroSensor_Object((1,3,6,1,4,1,28507,58,1,6,1,1,3),_Epc8226HygroSensor_Type())
epc8226HygroSensor.setMaxAccess(_C)
if mibBuilder.loadTexts:epc8226HygroSensor.setStatus(_B)
if mibBuilder.loadTexts:epc8226HygroSensor.setUnits('0.1 percent humidity')
class _Epc8226InputSensor_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_P,0),('on',1)))
_Epc8226InputSensor_Type.__name__=_D
_Epc8226InputSensor_Object=MibTableColumn
epc8226InputSensor=_Epc8226InputSensor_Object((1,3,6,1,4,1,28507,58,1,6,1,1,4),_Epc8226InputSensor_Type())
epc8226InputSensor.setMaxAccess(_C)
if mibBuilder.loadTexts:epc8226InputSensor.setStatus(_B)
_Epc8226AirPressure_Type=Integer32
_Epc8226AirPressure_Object=MibTableColumn
epc8226AirPressure=_Epc8226AirPressure_Object((1,3,6,1,4,1,28507,58,1,6,1,1,5),_Epc8226AirPressure_Type())
epc8226AirPressure.setMaxAccess(_C)
if mibBuilder.loadTexts:epc8226AirPressure.setStatus(_B)
if mibBuilder.loadTexts:epc8226AirPressure.setUnits('1 hPA (hectopascal) ~ 1 milibar')
_Epc8226DewPoint_Type=Integer32
_Epc8226DewPoint_Object=MibTableColumn
epc8226DewPoint=_Epc8226DewPoint_Object((1,3,6,1,4,1,28507,58,1,6,1,1,6),_Epc8226DewPoint_Type())
epc8226DewPoint.setMaxAccess(_C)
if mibBuilder.loadTexts:epc8226DewPoint.setStatus(_B)
if mibBuilder.loadTexts:epc8226DewPoint.setUnits(_Q)
_Epc8226DewPointDiff_Type=Integer32
_Epc8226DewPointDiff_Object=MibTableColumn
epc8226DewPointDiff=_Epc8226DewPointDiff_Object((1,3,6,1,4,1,28507,58,1,6,1,1,7),_Epc8226DewPointDiff_Type())
epc8226DewPointDiff.setMaxAccess(_C)
if mibBuilder.loadTexts:epc8226DewPointDiff.setStatus(_B)
if mibBuilder.loadTexts:epc8226DewPointDiff.setUnits(_Q)
_Epc8226Conf_ObjectIdentity=ObjectIdentity
epc8226Conf=_Epc8226Conf_ObjectIdentity((1,3,6,1,4,1,28507,58,2))
_Epc8226Groups_ObjectIdentity=ObjectIdentity
epc8226Groups=_Epc8226Groups_ObjectIdentity((1,3,6,1,4,1,28507,58,2,1))
_Epc8226Compls_ObjectIdentity=ObjectIdentity
epc8226Compls=_Epc8226Compls_ObjectIdentity((1,3,6,1,4,1,28507,58,2,2))
_Events_ObjectIdentity=ObjectIdentity
events=_Events_ObjectIdentity((1,3,6,1,4,1,28507,58,3))
epc8226BasicGroup=ObjectGroup((1,3,6,1,4,1,28507,58,2,1,1))
epc8226BasicGroup.setObjects(*((_A,_p),(_A,_q),(_A,_r),(_A,_R),(_A,_S),(_A,_T),(_A,_s),(_A,_t),(_A,_u),(_A,_v),(_A,_w),(_A,_x),(_A,_y),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_z),(_A,_A0),(_A,_Y),(_A,_Z),(_A,_A1),(_A,_A2),(_A,_A3),(_A,_A4),(_A,_A5),(_A,_A6),(_A,_A7),(_A,_A8),(_A,_A9),(_A,_AA),(_A,_AB),(_A,_AC),(_A,_a),(_A,_AD),(_A,_AE),(_A,_AF),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_AG),(_A,_AH),(_A,_f),(_A,_g),(_A,_AI),(_A,_AJ),(_A,_AK),(_A,_AL),(_A,_AM),(_A,_AN),(_A,_AO),(_A,_AP),(_A,_AQ),(_A,_AR),(_A,_AS),(_A,_AT),(_A,_h),(_A,_i),(_A,_j),(_A,_O),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_H),(_A,_k),(_A,_AU),(_A,_l)))
if mibBuilder.loadTexts:epc8226BasicGroup.setStatus(_B)
epc8226SwitchEvtPort=NotificationType((1,3,6,1,4,1,28507,58,3,1))
epc8226SwitchEvtPort.setObjects(*((_A,_I),(_A,_R),(_A,_S),(_A,_T)))
if mibBuilder.loadTexts:epc8226SwitchEvtPort.setStatus(_B)
epc8226TempEvtSen=NotificationType((1,3,6,1,4,1,28507,58,3,2))
epc8226TempEvtSen.setObjects(*((_A,_H),(_A,_h)))
if mibBuilder.loadTexts:epc8226TempEvtSen.setStatus(_B)
epc8226HygroEvtSen=NotificationType((1,3,6,1,4,1,28507,58,3,3))
epc8226HygroEvtSen.setObjects(*((_A,_H),(_A,_i)))
if mibBuilder.loadTexts:epc8226HygroEvtSen.setStatus(_B)
epc8226InputEvtSen=NotificationType((1,3,6,1,4,1,28507,58,3,4))
epc8226InputEvtSen.setObjects(*((_A,_H),(_A,_j)))
if mibBuilder.loadTexts:epc8226InputEvtSen.setStatus(_B)
epc8226AirPressureEvtSen=NotificationType((1,3,6,1,4,1,28507,58,3,5))
epc8226AirPressureEvtSen.setObjects(*((_A,_H),(_A,_k)))
if mibBuilder.loadTexts:epc8226AirPressureEvtSen.setStatus(_B)
epc8226DewPtDiffEvtSen=NotificationType((1,3,6,1,4,1,28507,58,3,6))
epc8226DewPtDiffEvtSen.setObjects(*((_A,_H),(_A,_l)))
if mibBuilder.loadTexts:epc8226DewPtDiffEvtSen.setStatus(_B)
epc8226OVPEvt=NotificationType((1,3,6,1,4,1,28507,58,3,7))
epc8226OVPEvt.setObjects(*((_A,_K),(_A,_a)))
if mibBuilder.loadTexts:epc8226OVPEvt.setStatus(_B)
epc8226LineAmperageEvt=NotificationType((1,3,6,1,4,1,28507,58,3,8))
epc8226LineAmperageEvt.setObjects(*((_A,_J),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z)))
if mibBuilder.loadTexts:epc8226LineAmperageEvt.setStatus(_B)
epc8226PortAmperageEvt=NotificationType((1,3,6,1,4,1,28507,58,3,9))
epc8226PortAmperageEvt.setObjects(*((_A,_L),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_g)))
if mibBuilder.loadTexts:epc8226PortAmperageEvt.setStatus(_B)
epc8226NotificationGroup=NotificationGroup((1,3,6,1,4,1,28507,58,2,1,2))
epc8226NotificationGroup.setObjects(*((_A,_AV),(_A,_AW),(_A,_AX),(_A,_AY),(_A,_AZ),(_A,_Aa),(_A,_Ab),(_A,_Ac),(_A,_Ad)))
if mibBuilder.loadTexts:epc8226NotificationGroup.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'gudeads':gudeads,'gadsEPC8226':gadsEPC8226,'epc8226Objects':epc8226Objects,'epc8226CommonConfig':epc8226CommonConfig,'epc8226SNMPaccess':epc8226SNMPaccess,_p:epc8226TrapCtrl,'epc8226TrapIPTable':epc8226TrapIPTable,'epc8226TrapIPEntry':epc8226TrapIPEntry,_O:epc8226TrapIPIndex,_q:epc8226TrapAddr,'epc8226DeviceConfig':epc8226DeviceConfig,'epc8226IntActors':epc8226IntActors,'epc8226relayports':epc8226relayports,_r:epc8226portNumber,'epc8226portTable':epc8226portTable,'epc8226portEntry':epc8226portEntry,_I:epc8226PortIndex,_R:epc8226PortName,_S:epc8226PortState,_T:epc8226PortSwitchCount,_s:epc8226PortStartupMode,_t:epc8226PortStartupDelay,_u:epc8226PortRepowerTime,_v:epc8226Buzzer,'epc8226ExtActors':epc8226ExtActors,'epc8226IntSensors':epc8226IntSensors,'epc8226PowerChan':epc8226PowerChan,_w:epc8226ActivePowerChan,'epc8226PowerTable':epc8226PowerTable,'epc8226PowerEntry':epc8226PowerEntry,_J:epc8226PowerIndex,_x:epc8226ChanStatus,_y:epc8226AbsEnergyActive,_U:epc8226PowerActive,_V:epc8226Current,_W:epc8226Voltage,_X:epc8226Frequency,_z:epc8226PowerFactor,_A0:epc8226Pangle,_Y:epc8226PowerApparent,_Z:epc8226PowerReactive,_A1:epc8226AbsEnergyReactive,_A2:epc8226AbsEnergyActiveResettable,_A3:epc8226AbsEnergyReactiveResettable,_A4:epc8226ResetTime,_A5:epc8226ForwEnergyActive,_A6:epc8226ForwEnergyReactive,_A7:epc8226ForwEnergyActiveResettable,_A8:epc8226ForwEnergyReactiveResettable,_A9:epc8226RevEnergyActive,_AA:epc8226RevEnergyReactive,_AB:epc8226RevEnergyActiveResettable,_AC:epc8226RevEnergyReactiveResettable,'epc8226OVPTable':epc8226OVPTable,'epc8226OVPEntry':epc8226OVPEntry,_K:epc8226OVPIndex,_a:epc8226OVPStatus,'epc8226SinglePortPowerChan':epc8226SinglePortPowerChan,_AD:epc8226spActivePowerChan,'epc8226spPowerTable':epc8226spPowerTable,'epc8226spPowerEntry':epc8226spPowerEntry,_L:epc8226spPowerIndex,_AE:epc8226spChanStatus,_AF:epc8226spAbsEnergyActive,_b:epc8226spPowerActive,_c:epc8226spCurrent,_d:epc8226spVoltage,_e:epc8226spFrequency,_AG:epc8226spPowerFactor,_AH:epc8226spPangle,_f:epc8226spPowerApparent,_g:epc8226spPowerReactive,_AI:epc8226spAbsEnergyReactive,_AJ:epc8226spAbsEnergyActiveResettable,_AK:epc8226spAbsEnergyReactiveResettable,_AL:epc8226spResetTime,_AM:epc8226spForwEnergyActive,_AN:epc8226spForwEnergyReactive,_AO:epc8226spForwEnergyActiveResettable,_AP:epc8226spForwEnergyReactiveResettable,_AQ:epc8226spRevEnergyActive,_AR:epc8226spRevEnergyReactive,_AS:epc8226spRevEnergyActiveResettable,_AT:epc8226spRevEnergyReactiveResettable,'epc8226ExtSensors':epc8226ExtSensors,'epc8226SensorTable':epc8226SensorTable,'epc8226SensorEntry':epc8226SensorEntry,_H:epc8226SensorIndex,_h:epc8226TempSensor,_i:epc8226HygroSensor,_j:epc8226InputSensor,_k:epc8226AirPressure,_AU:epc8226DewPoint,_l:epc8226DewPointDiff,'epc8226Conf':epc8226Conf,'epc8226Groups':epc8226Groups,'epc8226BasicGroup':epc8226BasicGroup,'epc8226NotificationGroup':epc8226NotificationGroup,'epc8226Compls':epc8226Compls,'events':events,_AV:epc8226SwitchEvtPort,_AW:epc8226TempEvtSen,_AX:epc8226HygroEvtSen,_AY:epc8226InputEvtSen,_AZ:epc8226AirPressureEvtSen,_Aa:epc8226DewPtDiffEvtSen,_Ab:epc8226OVPEvt,_Ac:epc8226LineAmperageEvt,_Ad:epc8226PortAmperageEvt})