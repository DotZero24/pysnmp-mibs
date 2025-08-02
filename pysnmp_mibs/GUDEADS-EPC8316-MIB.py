_AZ='epc8316PortAmperageEvt'
_AY='epc8316LineAmperageEvt'
_AX='epc8316DewPtDiffEvtSen'
_AW='epc8316AirPressureEvtSen'
_AV='epc8316InputEvtSen'
_AU='epc8316HygroEvtSen'
_AT='epc8316TempEvtSen'
_AS='epc8316SwitchEvtPort'
_AR='epc8316DewPoint'
_AQ='epc8316spRevEnergyReactiveResettable'
_AP='epc8316spRevEnergyActiveResettable'
_AO='epc8316spRevEnergyReactive'
_AN='epc8316spRevEnergyActive'
_AM='epc8316spForwEnergyReactiveResettable'
_AL='epc8316spForwEnergyActiveResettable'
_AK='epc8316spForwEnergyReactive'
_AJ='epc8316spForwEnergyActive'
_AI='epc8316spResetTime'
_AH='epc8316spAbsEnergyReactiveResettable'
_AG='epc8316spAbsEnergyActiveResettable'
_AF='epc8316spAbsEnergyReactive'
_AE='epc8316spPangle'
_AD='epc8316spPowerFactor'
_AC='epc8316spAbsEnergyActive'
_AB='epc8316spChanStatus'
_AA='epc8316spActivePowerChan'
_A9='epc8316RevEnergyReactiveResettable'
_A8='epc8316RevEnergyActiveResettable'
_A7='epc8316RevEnergyReactive'
_A6='epc8316RevEnergyActive'
_A5='epc8316ForwEnergyReactiveResettable'
_A4='epc8316ForwEnergyActiveResettable'
_A3='epc8316ForwEnergyReactive'
_A2='epc8316ForwEnergyActive'
_A1='epc8316ResetTime'
_A0='epc8316AbsEnergyReactiveResettable'
_z='epc8316AbsEnergyActiveResettable'
_y='epc8316AbsEnergyReactive'
_x='epc8316Pangle'
_w='epc8316PowerFactor'
_v='epc8316AbsEnergyActive'
_u='epc8316ChanStatus'
_t='epc8316ActivePowerChan'
_s='epc8316PortRepowerTime'
_r='epc8316PortStartupDelay'
_q='epc8316PortStartupMode'
_p='epc8316portNumber'
_o='epc8316TrapAddr'
_n='epc8316TrapCtrl'
_m='0.1 degree'
_l='0.01 hz'
_k='seconds'
_j='epc8316DewPointDiff'
_i='epc8316AirPressure'
_h='epc8316InputSensor'
_g='epc8316HygroSensor'
_f='epc8316TempSensor'
_e='epc8316spPowerReactive'
_d='epc8316spPowerApparent'
_c='epc8316spFrequency'
_b='epc8316spVoltage'
_a='epc8316spCurrent'
_Z='epc8316spPowerActive'
_Y='epc8316PowerReactive'
_X='epc8316PowerApparent'
_W='epc8316Frequency'
_V='epc8316Voltage'
_U='epc8316Current'
_T='epc8316PowerActive'
_S='epc8316PortSwitchCount'
_R='epc8316PortState'
_Q='epc8316PortName'
_P='0.1 degree Celsius'
_O='off'
_N='epc8316TrapIPIndex'
_M='Unsigned32'
_L='OctetString'
_K='epc8316spPowerIndex'
_J='epc8316PowerIndex'
_I='epc8316PortIndex'
_H='epc8316SensorIndex'
_G='read-write'
_F='VARh'
_E='Wh'
_D='Integer32'
_C='read-only'
_B='current'
_A='GUDEADS-EPC8316-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_L,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_M,'enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
gudeads=ModuleIdentity((1,3,6,1,4,1,28507))
if mibBuilder.loadTexts:gudeads.setRevisions(('2007-03-05 13:56',))
_GadsEPC8316_ObjectIdentity=ObjectIdentity
gadsEPC8316=_GadsEPC8316_ObjectIdentity((1,3,6,1,4,1,28507,64))
_Epc8316Objects_ObjectIdentity=ObjectIdentity
epc8316Objects=_Epc8316Objects_ObjectIdentity((1,3,6,1,4,1,28507,64,1))
_Epc8316CommonConfig_ObjectIdentity=ObjectIdentity
epc8316CommonConfig=_Epc8316CommonConfig_ObjectIdentity((1,3,6,1,4,1,28507,64,1,1))
_Epc8316SNMPaccess_ObjectIdentity=ObjectIdentity
epc8316SNMPaccess=_Epc8316SNMPaccess_ObjectIdentity((1,3,6,1,4,1,28507,64,1,1,1))
class _Epc8316TrapCtrl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3))
_Epc8316TrapCtrl_Type.__name__=_D
_Epc8316TrapCtrl_Object=MibScalar
epc8316TrapCtrl=_Epc8316TrapCtrl_Object((1,3,6,1,4,1,28507,64,1,1,1,1),_Epc8316TrapCtrl_Type())
epc8316TrapCtrl.setMaxAccess(_G)
if mibBuilder.loadTexts:epc8316TrapCtrl.setStatus(_B)
_Epc8316TrapIPTable_Object=MibTable
epc8316TrapIPTable=_Epc8316TrapIPTable_Object((1,3,6,1,4,1,28507,64,1,1,1,2))
if mibBuilder.loadTexts:epc8316TrapIPTable.setStatus(_B)
_Epc8316TrapIPEntry_Object=MibTableRow
epc8316TrapIPEntry=_Epc8316TrapIPEntry_Object((1,3,6,1,4,1,28507,64,1,1,1,2,1))
epc8316TrapIPEntry.setIndexNames((0,_A,_N))
if mibBuilder.loadTexts:epc8316TrapIPEntry.setStatus(_B)
class _Epc8316TrapIPIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_Epc8316TrapIPIndex_Type.__name__=_D
_Epc8316TrapIPIndex_Object=MibTableColumn
epc8316TrapIPIndex=_Epc8316TrapIPIndex_Object((1,3,6,1,4,1,28507,64,1,1,1,2,1,1),_Epc8316TrapIPIndex_Type())
epc8316TrapIPIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:epc8316TrapIPIndex.setStatus(_B)
class _Epc8316TrapAddr_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,99))
_Epc8316TrapAddr_Type.__name__=_L
_Epc8316TrapAddr_Object=MibTableColumn
epc8316TrapAddr=_Epc8316TrapAddr_Object((1,3,6,1,4,1,28507,64,1,1,1,2,1,2),_Epc8316TrapAddr_Type())
epc8316TrapAddr.setMaxAccess(_G)
if mibBuilder.loadTexts:epc8316TrapAddr.setStatus(_B)
_Epc8316DeviceConfig_ObjectIdentity=ObjectIdentity
epc8316DeviceConfig=_Epc8316DeviceConfig_ObjectIdentity((1,3,6,1,4,1,28507,64,1,2))
_Epc8316IntActors_ObjectIdentity=ObjectIdentity
epc8316IntActors=_Epc8316IntActors_ObjectIdentity((1,3,6,1,4,1,28507,64,1,3))
_Epc8316relayports_ObjectIdentity=ObjectIdentity
epc8316relayports=_Epc8316relayports_ObjectIdentity((1,3,6,1,4,1,28507,64,1,3,1))
class _Epc8316portNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,12))
_Epc8316portNumber_Type.__name__=_D
_Epc8316portNumber_Object=MibScalar
epc8316portNumber=_Epc8316portNumber_Object((1,3,6,1,4,1,28507,64,1,3,1,1),_Epc8316portNumber_Type())
epc8316portNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:epc8316portNumber.setStatus(_B)
_Epc8316portTable_Object=MibTable
epc8316portTable=_Epc8316portTable_Object((1,3,6,1,4,1,28507,64,1,3,1,2))
if mibBuilder.loadTexts:epc8316portTable.setStatus(_B)
_Epc8316portEntry_Object=MibTableRow
epc8316portEntry=_Epc8316portEntry_Object((1,3,6,1,4,1,28507,64,1,3,1,2,1))
epc8316portEntry.setIndexNames((0,_A,_I))
if mibBuilder.loadTexts:epc8316portEntry.setStatus(_B)
class _Epc8316PortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_Epc8316PortIndex_Type.__name__=_D
_Epc8316PortIndex_Object=MibTableColumn
epc8316PortIndex=_Epc8316PortIndex_Object((1,3,6,1,4,1,28507,64,1,3,1,2,1,1),_Epc8316PortIndex_Type())
epc8316PortIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:epc8316PortIndex.setStatus(_B)
class _Epc8316PortName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_Epc8316PortName_Type.__name__=_L
_Epc8316PortName_Object=MibTableColumn
epc8316PortName=_Epc8316PortName_Object((1,3,6,1,4,1,28507,64,1,3,1,2,1,2),_Epc8316PortName_Type())
epc8316PortName.setMaxAccess(_G)
if mibBuilder.loadTexts:epc8316PortName.setStatus(_B)
class _Epc8316PortState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_O,0),('on',1)))
_Epc8316PortState_Type.__name__=_D
_Epc8316PortState_Object=MibTableColumn
epc8316PortState=_Epc8316PortState_Object((1,3,6,1,4,1,28507,64,1,3,1,2,1,3),_Epc8316PortState_Type())
epc8316PortState.setMaxAccess(_G)
if mibBuilder.loadTexts:epc8316PortState.setStatus(_B)
_Epc8316PortSwitchCount_Type=Integer32
_Epc8316PortSwitchCount_Object=MibTableColumn
epc8316PortSwitchCount=_Epc8316PortSwitchCount_Object((1,3,6,1,4,1,28507,64,1,3,1,2,1,4),_Epc8316PortSwitchCount_Type())
epc8316PortSwitchCount.setMaxAccess(_C)
if mibBuilder.loadTexts:epc8316PortSwitchCount.setStatus(_B)
class _Epc8316PortStartupMode_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_O,0),('on',1),('laststate',2)))
_Epc8316PortStartupMode_Type.__name__=_D
_Epc8316PortStartupMode_Object=MibTableColumn
epc8316PortStartupMode=_Epc8316PortStartupMode_Object((1,3,6,1,4,1,28507,64,1,3,1,2,1,5),_Epc8316PortStartupMode_Type())
epc8316PortStartupMode.setMaxAccess(_G)
if mibBuilder.loadTexts:epc8316PortStartupMode.setStatus(_B)
class _Epc8316PortStartupDelay_Type(Integer32):defaultValue=0
_Epc8316PortStartupDelay_Type.__name__=_D
_Epc8316PortStartupDelay_Object=MibTableColumn
epc8316PortStartupDelay=_Epc8316PortStartupDelay_Object((1,3,6,1,4,1,28507,64,1,3,1,2,1,6),_Epc8316PortStartupDelay_Type())
epc8316PortStartupDelay.setMaxAccess(_G)
if mibBuilder.loadTexts:epc8316PortStartupDelay.setStatus(_B)
if mibBuilder.loadTexts:epc8316PortStartupDelay.setUnits(_k)
class _Epc8316PortRepowerTime_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Epc8316PortRepowerTime_Type.__name__=_D
_Epc8316PortRepowerTime_Object=MibTableColumn
epc8316PortRepowerTime=_Epc8316PortRepowerTime_Object((1,3,6,1,4,1,28507,64,1,3,1,2,1,7),_Epc8316PortRepowerTime_Type())
epc8316PortRepowerTime.setMaxAccess(_G)
if mibBuilder.loadTexts:epc8316PortRepowerTime.setStatus(_B)
if mibBuilder.loadTexts:epc8316PortRepowerTime.setUnits(_k)
_Epc8316ExtActors_ObjectIdentity=ObjectIdentity
epc8316ExtActors=_Epc8316ExtActors_ObjectIdentity((1,3,6,1,4,1,28507,64,1,4))
_Epc8316IntSensors_ObjectIdentity=ObjectIdentity
epc8316IntSensors=_Epc8316IntSensors_ObjectIdentity((1,3,6,1,4,1,28507,64,1,5))
_Epc8316PowerChan_ObjectIdentity=ObjectIdentity
epc8316PowerChan=_Epc8316PowerChan_ObjectIdentity((1,3,6,1,4,1,28507,64,1,5,1))
class _Epc8316ActivePowerChan_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1))
_Epc8316ActivePowerChan_Type.__name__=_M
_Epc8316ActivePowerChan_Object=MibScalar
epc8316ActivePowerChan=_Epc8316ActivePowerChan_Object((1,3,6,1,4,1,28507,64,1,5,1,1),_Epc8316ActivePowerChan_Type())
epc8316ActivePowerChan.setMaxAccess(_C)
if mibBuilder.loadTexts:epc8316ActivePowerChan.setStatus(_B)
_Epc8316PowerTable_Object=MibTable
epc8316PowerTable=_Epc8316PowerTable_Object((1,3,6,1,4,1,28507,64,1,5,1,2))
if mibBuilder.loadTexts:epc8316PowerTable.setStatus(_B)
_Epc8316PowerEntry_Object=MibTableRow
epc8316PowerEntry=_Epc8316PowerEntry_Object((1,3,6,1,4,1,28507,64,1,5,1,2,1))
epc8316PowerEntry.setIndexNames((0,_A,_J))
if mibBuilder.loadTexts:epc8316PowerEntry.setStatus(_B)
class _Epc8316PowerIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1))
_Epc8316PowerIndex_Type.__name__=_D
_Epc8316PowerIndex_Object=MibTableColumn
epc8316PowerIndex=_Epc8316PowerIndex_Object((1,3,6,1,4,1,28507,64,1,5,1,2,1,1),_Epc8316PowerIndex_Type())
epc8316PowerIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:epc8316PowerIndex.setStatus(_B)
class _Epc8316ChanStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Epc8316ChanStatus_Type.__name__=_D
_Epc8316ChanStatus_Object=MibTableColumn
epc8316ChanStatus=_Epc8316ChanStatus_Object((1,3,6,1,4,1,28507,64,1,5,1,2,1,2),_Epc8316ChanStatus_Type())
epc8316ChanStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:epc8316ChanStatus.setStatus(_B)
_Epc8316AbsEnergyActive_Type=Unsigned32
_Epc8316AbsEnergyActive_Object=MibTableColumn
epc8316AbsEnergyActive=_Epc8316AbsEnergyActive_Object((1,3,6,1,4,1,28507,64,1,5,1,2,1,3),_Epc8316AbsEnergyActive_Type())
epc8316AbsEnergyActive.setMaxAccess(_C)
if mibBuilder.loadTexts:epc8316AbsEnergyActive.setStatus(_B)
if mibBuilder.loadTexts:epc8316AbsEnergyActive.setUnits(_E)
_Epc8316PowerActive_Type=Integer32
_Epc8316PowerActive_Object=MibTableColumn
epc8316PowerActive=_Epc8316PowerActive_Object((1,3,6,1,4,1,28507,64,1,5,1,2,1,4),_Epc8316PowerActive_Type())
epc8316PowerActive.setMaxAccess(_C)
if mibBuilder.loadTexts:epc8316PowerActive.setStatus(_B)
if mibBuilder.loadTexts:epc8316PowerActive.setUnits('W')
_Epc8316Current_Type=Unsigned32
_Epc8316Current_Object=MibTableColumn
epc8316Current=_Epc8316Current_Object((1,3,6,1,4,1,28507,64,1,5,1,2,1,5),_Epc8316Current_Type())
epc8316Current.setMaxAccess(_C)
if mibBuilder.loadTexts:epc8316Current.setStatus(_B)
if mibBuilder.loadTexts:epc8316Current.setUnits('mA')
_Epc8316Voltage_Type=Unsigned32
_Epc8316Voltage_Object=MibTableColumn
epc8316Voltage=_Epc8316Voltage_Object((1,3,6,1,4,1,28507,64,1,5,1,2,1,6),_Epc8316Voltage_Type())
epc8316Voltage.setMaxAccess(_C)
if mibBuilder.loadTexts:epc8316Voltage.setStatus(_B)
if mibBuilder.loadTexts:epc8316Voltage.setUnits('V')
_Epc8316Frequency_Type=Unsigned32
_Epc8316Frequency_Object=MibTableColumn
epc8316Frequency=_Epc8316Frequency_Object((1,3,6,1,4,1,28507,64,1,5,1,2,1,7),_Epc8316Frequency_Type())
epc8316Frequency.setMaxAccess(_C)
if mibBuilder.loadTexts:epc8316Frequency.setStatus(_B)
if mibBuilder.loadTexts:epc8316Frequency.setUnits(_l)
_Epc8316PowerFactor_Type=Integer32
_Epc8316PowerFactor_Object=MibTableColumn
epc8316PowerFactor=_Epc8316PowerFactor_Object((1,3,6,1,4,1,28507,64,1,5,1,2,1,8),_Epc8316PowerFactor_Type())
epc8316PowerFactor.setMaxAccess(_C)
if mibBuilder.loadTexts:epc8316PowerFactor.setStatus(_B)
if mibBuilder.loadTexts:epc8316PowerFactor.setUnits('0.001')
_Epc8316Pangle_Type=Integer32
_Epc8316Pangle_Object=MibTableColumn
epc8316Pangle=_Epc8316Pangle_Object((1,3,6,1,4,1,28507,64,1,5,1,2,1,9),_Epc8316Pangle_Type())
epc8316Pangle.setMaxAccess(_C)
if mibBuilder.loadTexts:epc8316Pangle.setStatus(_B)
if mibBuilder.loadTexts:epc8316Pangle.setUnits(_m)
_Epc8316PowerApparent_Type=Integer32
_Epc8316PowerApparent_Object=MibTableColumn
epc8316PowerApparent=_Epc8316PowerApparent_Object((1,3,6,1,4,1,28507,64,1,5,1,2,1,10),_Epc8316PowerApparent_Type())
epc8316PowerApparent.setMaxAccess(_C)
if mibBuilder.loadTexts:epc8316PowerApparent.setStatus(_B)
if mibBuilder.loadTexts:epc8316PowerApparent.setUnits('VA')
_Epc8316PowerReactive_Type=Integer32
_Epc8316PowerReactive_Object=MibTableColumn
epc8316PowerReactive=_Epc8316PowerReactive_Object((1,3,6,1,4,1,28507,64,1,5,1,2,1,11),_Epc8316PowerReactive_Type())
epc8316PowerReactive.setMaxAccess(_C)
if mibBuilder.loadTexts:epc8316PowerReactive.setStatus(_B)
if mibBuilder.loadTexts:epc8316PowerReactive.setUnits('VAR')
_Epc8316AbsEnergyReactive_Type=Unsigned32
_Epc8316AbsEnergyReactive_Object=MibTableColumn
epc8316AbsEnergyReactive=_Epc8316AbsEnergyReactive_Object((1,3,6,1,4,1,28507,64,1,5,1,2,1,12),_Epc8316AbsEnergyReactive_Type())
epc8316AbsEnergyReactive.setMaxAccess(_C)
if mibBuilder.loadTexts:epc8316AbsEnergyReactive.setStatus(_B)
if mibBuilder.loadTexts:epc8316AbsEnergyReactive.setUnits(_F)
_Epc8316AbsEnergyActiveResettable_Type=Unsigned32
_Epc8316AbsEnergyActiveResettable_Object=MibTableColumn
epc8316AbsEnergyActiveResettable=_Epc8316AbsEnergyActiveResettable_Object((1,3,6,1,4,1,28507,64,1,5,1,2,1,13),_Epc8316AbsEnergyActiveResettable_Type())
epc8316AbsEnergyActiveResettable.setMaxAccess(_G)
if mibBuilder.loadTexts:epc8316AbsEnergyActiveResettable.setStatus(_B)
if mibBuilder.loadTexts:epc8316AbsEnergyActiveResettable.setUnits(_E)
_Epc8316AbsEnergyReactiveResettable_Type=Unsigned32
_Epc8316AbsEnergyReactiveResettable_Object=MibTableColumn
epc8316AbsEnergyReactiveResettable=_Epc8316AbsEnergyReactiveResettable_Object((1,3,6,1,4,1,28507,64,1,5,1,2,1,14),_Epc8316AbsEnergyReactiveResettable_Type())
epc8316AbsEnergyReactiveResettable.setMaxAccess(_C)
if mibBuilder.loadTexts:epc8316AbsEnergyReactiveResettable.setStatus(_B)
if mibBuilder.loadTexts:epc8316AbsEnergyReactiveResettable.setUnits(_F)
_Epc8316ResetTime_Type=Unsigned32
_Epc8316ResetTime_Object=MibTableColumn
epc8316ResetTime=_Epc8316ResetTime_Object((1,3,6,1,4,1,28507,64,1,5,1,2,1,15),_Epc8316ResetTime_Type())
epc8316ResetTime.setMaxAccess(_C)
if mibBuilder.loadTexts:epc8316ResetTime.setStatus(_B)
if mibBuilder.loadTexts:epc8316ResetTime.setUnits('s')
_Epc8316ForwEnergyActive_Type=Unsigned32
_Epc8316ForwEnergyActive_Object=MibTableColumn
epc8316ForwEnergyActive=_Epc8316ForwEnergyActive_Object((1,3,6,1,4,1,28507,64,1,5,1,2,1,16),_Epc8316ForwEnergyActive_Type())
epc8316ForwEnergyActive.setMaxAccess(_C)
if mibBuilder.loadTexts:epc8316ForwEnergyActive.setStatus(_B)
if mibBuilder.loadTexts:epc8316ForwEnergyActive.setUnits(_E)
_Epc8316ForwEnergyReactive_Type=Unsigned32
_Epc8316ForwEnergyReactive_Object=MibTableColumn
epc8316ForwEnergyReactive=_Epc8316ForwEnergyReactive_Object((1,3,6,1,4,1,28507,64,1,5,1,2,1,17),_Epc8316ForwEnergyReactive_Type())
epc8316ForwEnergyReactive.setMaxAccess(_C)
if mibBuilder.loadTexts:epc8316ForwEnergyReactive.setStatus(_B)
if mibBuilder.loadTexts:epc8316ForwEnergyReactive.setUnits(_F)
_Epc8316ForwEnergyActiveResettable_Type=Unsigned32
_Epc8316ForwEnergyActiveResettable_Object=MibTableColumn
epc8316ForwEnergyActiveResettable=_Epc8316ForwEnergyActiveResettable_Object((1,3,6,1,4,1,28507,64,1,5,1,2,1,18),_Epc8316ForwEnergyActiveResettable_Type())
epc8316ForwEnergyActiveResettable.setMaxAccess(_C)
if mibBuilder.loadTexts:epc8316ForwEnergyActiveResettable.setStatus(_B)
if mibBuilder.loadTexts:epc8316ForwEnergyActiveResettable.setUnits(_E)
_Epc8316ForwEnergyReactiveResettable_Type=Unsigned32
_Epc8316ForwEnergyReactiveResettable_Object=MibTableColumn
epc8316ForwEnergyReactiveResettable=_Epc8316ForwEnergyReactiveResettable_Object((1,3,6,1,4,1,28507,64,1,5,1,2,1,19),_Epc8316ForwEnergyReactiveResettable_Type())
epc8316ForwEnergyReactiveResettable.setMaxAccess(_C)
if mibBuilder.loadTexts:epc8316ForwEnergyReactiveResettable.setStatus(_B)
if mibBuilder.loadTexts:epc8316ForwEnergyReactiveResettable.setUnits(_F)
_Epc8316RevEnergyActive_Type=Unsigned32
_Epc8316RevEnergyActive_Object=MibTableColumn
epc8316RevEnergyActive=_Epc8316RevEnergyActive_Object((1,3,6,1,4,1,28507,64,1,5,1,2,1,20),_Epc8316RevEnergyActive_Type())
epc8316RevEnergyActive.setMaxAccess(_C)
if mibBuilder.loadTexts:epc8316RevEnergyActive.setStatus(_B)
if mibBuilder.loadTexts:epc8316RevEnergyActive.setUnits(_E)
_Epc8316RevEnergyReactive_Type=Unsigned32
_Epc8316RevEnergyReactive_Object=MibTableColumn
epc8316RevEnergyReactive=_Epc8316RevEnergyReactive_Object((1,3,6,1,4,1,28507,64,1,5,1,2,1,21),_Epc8316RevEnergyReactive_Type())
epc8316RevEnergyReactive.setMaxAccess(_C)
if mibBuilder.loadTexts:epc8316RevEnergyReactive.setStatus(_B)
if mibBuilder.loadTexts:epc8316RevEnergyReactive.setUnits(_F)
_Epc8316RevEnergyActiveResettable_Type=Unsigned32
_Epc8316RevEnergyActiveResettable_Object=MibTableColumn
epc8316RevEnergyActiveResettable=_Epc8316RevEnergyActiveResettable_Object((1,3,6,1,4,1,28507,64,1,5,1,2,1,22),_Epc8316RevEnergyActiveResettable_Type())
epc8316RevEnergyActiveResettable.setMaxAccess(_C)
if mibBuilder.loadTexts:epc8316RevEnergyActiveResettable.setStatus(_B)
if mibBuilder.loadTexts:epc8316RevEnergyActiveResettable.setUnits(_E)
_Epc8316RevEnergyReactiveResettable_Type=Unsigned32
_Epc8316RevEnergyReactiveResettable_Object=MibTableColumn
epc8316RevEnergyReactiveResettable=_Epc8316RevEnergyReactiveResettable_Object((1,3,6,1,4,1,28507,64,1,5,1,2,1,23),_Epc8316RevEnergyReactiveResettable_Type())
epc8316RevEnergyReactiveResettable.setMaxAccess(_C)
if mibBuilder.loadTexts:epc8316RevEnergyReactiveResettable.setStatus(_B)
if mibBuilder.loadTexts:epc8316RevEnergyReactiveResettable.setUnits(_F)
_Epc8316SinglePortPowerChan_ObjectIdentity=ObjectIdentity
epc8316SinglePortPowerChan=_Epc8316SinglePortPowerChan_ObjectIdentity((1,3,6,1,4,1,28507,64,1,5,5))
class _Epc8316spActivePowerChan_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_Epc8316spActivePowerChan_Type.__name__=_M
_Epc8316spActivePowerChan_Object=MibScalar
epc8316spActivePowerChan=_Epc8316spActivePowerChan_Object((1,3,6,1,4,1,28507,64,1,5,5,1),_Epc8316spActivePowerChan_Type())
epc8316spActivePowerChan.setMaxAccess(_C)
if mibBuilder.loadTexts:epc8316spActivePowerChan.setStatus(_B)
_Epc8316spPowerTable_Object=MibTable
epc8316spPowerTable=_Epc8316spPowerTable_Object((1,3,6,1,4,1,28507,64,1,5,5,2))
if mibBuilder.loadTexts:epc8316spPowerTable.setStatus(_B)
_Epc8316spPowerEntry_Object=MibTableRow
epc8316spPowerEntry=_Epc8316spPowerEntry_Object((1,3,6,1,4,1,28507,64,1,5,5,2,1))
epc8316spPowerEntry.setIndexNames((0,_A,_K))
if mibBuilder.loadTexts:epc8316spPowerEntry.setStatus(_B)
class _Epc8316spPowerIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_Epc8316spPowerIndex_Type.__name__=_D
_Epc8316spPowerIndex_Object=MibTableColumn
epc8316spPowerIndex=_Epc8316spPowerIndex_Object((1,3,6,1,4,1,28507,64,1,5,5,2,1,1),_Epc8316spPowerIndex_Type())
epc8316spPowerIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:epc8316spPowerIndex.setStatus(_B)
class _Epc8316spChanStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Epc8316spChanStatus_Type.__name__=_D
_Epc8316spChanStatus_Object=MibTableColumn
epc8316spChanStatus=_Epc8316spChanStatus_Object((1,3,6,1,4,1,28507,64,1,5,5,2,1,2),_Epc8316spChanStatus_Type())
epc8316spChanStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:epc8316spChanStatus.setStatus(_B)
_Epc8316spAbsEnergyActive_Type=Unsigned32
_Epc8316spAbsEnergyActive_Object=MibTableColumn
epc8316spAbsEnergyActive=_Epc8316spAbsEnergyActive_Object((1,3,6,1,4,1,28507,64,1,5,5,2,1,3),_Epc8316spAbsEnergyActive_Type())
epc8316spAbsEnergyActive.setMaxAccess(_C)
if mibBuilder.loadTexts:epc8316spAbsEnergyActive.setStatus(_B)
if mibBuilder.loadTexts:epc8316spAbsEnergyActive.setUnits(_E)
_Epc8316spPowerActive_Type=Integer32
_Epc8316spPowerActive_Object=MibTableColumn
epc8316spPowerActive=_Epc8316spPowerActive_Object((1,3,6,1,4,1,28507,64,1,5,5,2,1,4),_Epc8316spPowerActive_Type())
epc8316spPowerActive.setMaxAccess(_C)
if mibBuilder.loadTexts:epc8316spPowerActive.setStatus(_B)
if mibBuilder.loadTexts:epc8316spPowerActive.setUnits('W')
_Epc8316spCurrent_Type=Unsigned32
_Epc8316spCurrent_Object=MibTableColumn
epc8316spCurrent=_Epc8316spCurrent_Object((1,3,6,1,4,1,28507,64,1,5,5,2,1,5),_Epc8316spCurrent_Type())
epc8316spCurrent.setMaxAccess(_C)
if mibBuilder.loadTexts:epc8316spCurrent.setStatus(_B)
if mibBuilder.loadTexts:epc8316spCurrent.setUnits('mA')
_Epc8316spVoltage_Type=Unsigned32
_Epc8316spVoltage_Object=MibTableColumn
epc8316spVoltage=_Epc8316spVoltage_Object((1,3,6,1,4,1,28507,64,1,5,5,2,1,6),_Epc8316spVoltage_Type())
epc8316spVoltage.setMaxAccess(_C)
if mibBuilder.loadTexts:epc8316spVoltage.setStatus(_B)
if mibBuilder.loadTexts:epc8316spVoltage.setUnits('V')
_Epc8316spFrequency_Type=Unsigned32
_Epc8316spFrequency_Object=MibTableColumn
epc8316spFrequency=_Epc8316spFrequency_Object((1,3,6,1,4,1,28507,64,1,5,5,2,1,7),_Epc8316spFrequency_Type())
epc8316spFrequency.setMaxAccess(_C)
if mibBuilder.loadTexts:epc8316spFrequency.setStatus(_B)
if mibBuilder.loadTexts:epc8316spFrequency.setUnits(_l)
_Epc8316spPowerFactor_Type=Integer32
_Epc8316spPowerFactor_Object=MibTableColumn
epc8316spPowerFactor=_Epc8316spPowerFactor_Object((1,3,6,1,4,1,28507,64,1,5,5,2,1,8),_Epc8316spPowerFactor_Type())
epc8316spPowerFactor.setMaxAccess(_C)
if mibBuilder.loadTexts:epc8316spPowerFactor.setStatus(_B)
if mibBuilder.loadTexts:epc8316spPowerFactor.setUnits('0.001')
_Epc8316spPangle_Type=Integer32
_Epc8316spPangle_Object=MibTableColumn
epc8316spPangle=_Epc8316spPangle_Object((1,3,6,1,4,1,28507,64,1,5,5,2,1,9),_Epc8316spPangle_Type())
epc8316spPangle.setMaxAccess(_C)
if mibBuilder.loadTexts:epc8316spPangle.setStatus(_B)
if mibBuilder.loadTexts:epc8316spPangle.setUnits(_m)
_Epc8316spPowerApparent_Type=Integer32
_Epc8316spPowerApparent_Object=MibTableColumn
epc8316spPowerApparent=_Epc8316spPowerApparent_Object((1,3,6,1,4,1,28507,64,1,5,5,2,1,10),_Epc8316spPowerApparent_Type())
epc8316spPowerApparent.setMaxAccess(_C)
if mibBuilder.loadTexts:epc8316spPowerApparent.setStatus(_B)
if mibBuilder.loadTexts:epc8316spPowerApparent.setUnits('VA')
_Epc8316spPowerReactive_Type=Integer32
_Epc8316spPowerReactive_Object=MibTableColumn
epc8316spPowerReactive=_Epc8316spPowerReactive_Object((1,3,6,1,4,1,28507,64,1,5,5,2,1,11),_Epc8316spPowerReactive_Type())
epc8316spPowerReactive.setMaxAccess(_C)
if mibBuilder.loadTexts:epc8316spPowerReactive.setStatus(_B)
if mibBuilder.loadTexts:epc8316spPowerReactive.setUnits('VAR')
_Epc8316spAbsEnergyReactive_Type=Unsigned32
_Epc8316spAbsEnergyReactive_Object=MibTableColumn
epc8316spAbsEnergyReactive=_Epc8316spAbsEnergyReactive_Object((1,3,6,1,4,1,28507,64,1,5,5,2,1,12),_Epc8316spAbsEnergyReactive_Type())
epc8316spAbsEnergyReactive.setMaxAccess(_C)
if mibBuilder.loadTexts:epc8316spAbsEnergyReactive.setStatus(_B)
if mibBuilder.loadTexts:epc8316spAbsEnergyReactive.setUnits(_F)
_Epc8316spAbsEnergyActiveResettable_Type=Unsigned32
_Epc8316spAbsEnergyActiveResettable_Object=MibTableColumn
epc8316spAbsEnergyActiveResettable=_Epc8316spAbsEnergyActiveResettable_Object((1,3,6,1,4,1,28507,64,1,5,5,2,1,13),_Epc8316spAbsEnergyActiveResettable_Type())
epc8316spAbsEnergyActiveResettable.setMaxAccess(_G)
if mibBuilder.loadTexts:epc8316spAbsEnergyActiveResettable.setStatus(_B)
if mibBuilder.loadTexts:epc8316spAbsEnergyActiveResettable.setUnits(_E)
_Epc8316spAbsEnergyReactiveResettable_Type=Unsigned32
_Epc8316spAbsEnergyReactiveResettable_Object=MibTableColumn
epc8316spAbsEnergyReactiveResettable=_Epc8316spAbsEnergyReactiveResettable_Object((1,3,6,1,4,1,28507,64,1,5,5,2,1,14),_Epc8316spAbsEnergyReactiveResettable_Type())
epc8316spAbsEnergyReactiveResettable.setMaxAccess(_C)
if mibBuilder.loadTexts:epc8316spAbsEnergyReactiveResettable.setStatus(_B)
if mibBuilder.loadTexts:epc8316spAbsEnergyReactiveResettable.setUnits(_F)
_Epc8316spResetTime_Type=Unsigned32
_Epc8316spResetTime_Object=MibTableColumn
epc8316spResetTime=_Epc8316spResetTime_Object((1,3,6,1,4,1,28507,64,1,5,5,2,1,15),_Epc8316spResetTime_Type())
epc8316spResetTime.setMaxAccess(_C)
if mibBuilder.loadTexts:epc8316spResetTime.setStatus(_B)
if mibBuilder.loadTexts:epc8316spResetTime.setUnits('s')
_Epc8316spForwEnergyActive_Type=Unsigned32
_Epc8316spForwEnergyActive_Object=MibTableColumn
epc8316spForwEnergyActive=_Epc8316spForwEnergyActive_Object((1,3,6,1,4,1,28507,64,1,5,5,2,1,16),_Epc8316spForwEnergyActive_Type())
epc8316spForwEnergyActive.setMaxAccess(_C)
if mibBuilder.loadTexts:epc8316spForwEnergyActive.setStatus(_B)
if mibBuilder.loadTexts:epc8316spForwEnergyActive.setUnits(_E)
_Epc8316spForwEnergyReactive_Type=Unsigned32
_Epc8316spForwEnergyReactive_Object=MibTableColumn
epc8316spForwEnergyReactive=_Epc8316spForwEnergyReactive_Object((1,3,6,1,4,1,28507,64,1,5,5,2,1,17),_Epc8316spForwEnergyReactive_Type())
epc8316spForwEnergyReactive.setMaxAccess(_C)
if mibBuilder.loadTexts:epc8316spForwEnergyReactive.setStatus(_B)
if mibBuilder.loadTexts:epc8316spForwEnergyReactive.setUnits(_F)
_Epc8316spForwEnergyActiveResettable_Type=Unsigned32
_Epc8316spForwEnergyActiveResettable_Object=MibTableColumn
epc8316spForwEnergyActiveResettable=_Epc8316spForwEnergyActiveResettable_Object((1,3,6,1,4,1,28507,64,1,5,5,2,1,18),_Epc8316spForwEnergyActiveResettable_Type())
epc8316spForwEnergyActiveResettable.setMaxAccess(_C)
if mibBuilder.loadTexts:epc8316spForwEnergyActiveResettable.setStatus(_B)
if mibBuilder.loadTexts:epc8316spForwEnergyActiveResettable.setUnits(_E)
_Epc8316spForwEnergyReactiveResettable_Type=Unsigned32
_Epc8316spForwEnergyReactiveResettable_Object=MibTableColumn
epc8316spForwEnergyReactiveResettable=_Epc8316spForwEnergyReactiveResettable_Object((1,3,6,1,4,1,28507,64,1,5,5,2,1,19),_Epc8316spForwEnergyReactiveResettable_Type())
epc8316spForwEnergyReactiveResettable.setMaxAccess(_C)
if mibBuilder.loadTexts:epc8316spForwEnergyReactiveResettable.setStatus(_B)
if mibBuilder.loadTexts:epc8316spForwEnergyReactiveResettable.setUnits(_F)
_Epc8316spRevEnergyActive_Type=Unsigned32
_Epc8316spRevEnergyActive_Object=MibTableColumn
epc8316spRevEnergyActive=_Epc8316spRevEnergyActive_Object((1,3,6,1,4,1,28507,64,1,5,5,2,1,20),_Epc8316spRevEnergyActive_Type())
epc8316spRevEnergyActive.setMaxAccess(_C)
if mibBuilder.loadTexts:epc8316spRevEnergyActive.setStatus(_B)
if mibBuilder.loadTexts:epc8316spRevEnergyActive.setUnits(_E)
_Epc8316spRevEnergyReactive_Type=Unsigned32
_Epc8316spRevEnergyReactive_Object=MibTableColumn
epc8316spRevEnergyReactive=_Epc8316spRevEnergyReactive_Object((1,3,6,1,4,1,28507,64,1,5,5,2,1,21),_Epc8316spRevEnergyReactive_Type())
epc8316spRevEnergyReactive.setMaxAccess(_C)
if mibBuilder.loadTexts:epc8316spRevEnergyReactive.setStatus(_B)
if mibBuilder.loadTexts:epc8316spRevEnergyReactive.setUnits(_F)
_Epc8316spRevEnergyActiveResettable_Type=Unsigned32
_Epc8316spRevEnergyActiveResettable_Object=MibTableColumn
epc8316spRevEnergyActiveResettable=_Epc8316spRevEnergyActiveResettable_Object((1,3,6,1,4,1,28507,64,1,5,5,2,1,22),_Epc8316spRevEnergyActiveResettable_Type())
epc8316spRevEnergyActiveResettable.setMaxAccess(_C)
if mibBuilder.loadTexts:epc8316spRevEnergyActiveResettable.setStatus(_B)
if mibBuilder.loadTexts:epc8316spRevEnergyActiveResettable.setUnits(_E)
_Epc8316spRevEnergyReactiveResettable_Type=Unsigned32
_Epc8316spRevEnergyReactiveResettable_Object=MibTableColumn
epc8316spRevEnergyReactiveResettable=_Epc8316spRevEnergyReactiveResettable_Object((1,3,6,1,4,1,28507,64,1,5,5,2,1,23),_Epc8316spRevEnergyReactiveResettable_Type())
epc8316spRevEnergyReactiveResettable.setMaxAccess(_C)
if mibBuilder.loadTexts:epc8316spRevEnergyReactiveResettable.setStatus(_B)
if mibBuilder.loadTexts:epc8316spRevEnergyReactiveResettable.setUnits(_F)
_Epc8316ExtSensors_ObjectIdentity=ObjectIdentity
epc8316ExtSensors=_Epc8316ExtSensors_ObjectIdentity((1,3,6,1,4,1,28507,64,1,6))
_Epc8316SensorTable_Object=MibTable
epc8316SensorTable=_Epc8316SensorTable_Object((1,3,6,1,4,1,28507,64,1,6,1))
if mibBuilder.loadTexts:epc8316SensorTable.setStatus(_B)
_Epc8316SensorEntry_Object=MibTableRow
epc8316SensorEntry=_Epc8316SensorEntry_Object((1,3,6,1,4,1,28507,64,1,6,1,1))
epc8316SensorEntry.setIndexNames((0,_A,_H))
if mibBuilder.loadTexts:epc8316SensorEntry.setStatus(_B)
class _Epc8316SensorIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_Epc8316SensorIndex_Type.__name__=_D
_Epc8316SensorIndex_Object=MibTableColumn
epc8316SensorIndex=_Epc8316SensorIndex_Object((1,3,6,1,4,1,28507,64,1,6,1,1,1),_Epc8316SensorIndex_Type())
epc8316SensorIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:epc8316SensorIndex.setStatus(_B)
_Epc8316TempSensor_Type=Integer32
_Epc8316TempSensor_Object=MibTableColumn
epc8316TempSensor=_Epc8316TempSensor_Object((1,3,6,1,4,1,28507,64,1,6,1,1,2),_Epc8316TempSensor_Type())
epc8316TempSensor.setMaxAccess(_C)
if mibBuilder.loadTexts:epc8316TempSensor.setStatus(_B)
if mibBuilder.loadTexts:epc8316TempSensor.setUnits(_P)
_Epc8316HygroSensor_Type=Integer32
_Epc8316HygroSensor_Object=MibTableColumn
epc8316HygroSensor=_Epc8316HygroSensor_Object((1,3,6,1,4,1,28507,64,1,6,1,1,3),_Epc8316HygroSensor_Type())
epc8316HygroSensor.setMaxAccess(_C)
if mibBuilder.loadTexts:epc8316HygroSensor.setStatus(_B)
if mibBuilder.loadTexts:epc8316HygroSensor.setUnits('0.1 percent humidity')
class _Epc8316InputSensor_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_O,0),('on',1)))
_Epc8316InputSensor_Type.__name__=_D
_Epc8316InputSensor_Object=MibTableColumn
epc8316InputSensor=_Epc8316InputSensor_Object((1,3,6,1,4,1,28507,64,1,6,1,1,4),_Epc8316InputSensor_Type())
epc8316InputSensor.setMaxAccess(_C)
if mibBuilder.loadTexts:epc8316InputSensor.setStatus(_B)
_Epc8316AirPressure_Type=Integer32
_Epc8316AirPressure_Object=MibTableColumn
epc8316AirPressure=_Epc8316AirPressure_Object((1,3,6,1,4,1,28507,64,1,6,1,1,5),_Epc8316AirPressure_Type())
epc8316AirPressure.setMaxAccess(_C)
if mibBuilder.loadTexts:epc8316AirPressure.setStatus(_B)
if mibBuilder.loadTexts:epc8316AirPressure.setUnits('1 hPA (hectopascal) ~ 1 milibar')
_Epc8316DewPoint_Type=Integer32
_Epc8316DewPoint_Object=MibTableColumn
epc8316DewPoint=_Epc8316DewPoint_Object((1,3,6,1,4,1,28507,64,1,6,1,1,6),_Epc8316DewPoint_Type())
epc8316DewPoint.setMaxAccess(_C)
if mibBuilder.loadTexts:epc8316DewPoint.setStatus(_B)
if mibBuilder.loadTexts:epc8316DewPoint.setUnits(_P)
_Epc8316DewPointDiff_Type=Integer32
_Epc8316DewPointDiff_Object=MibTableColumn
epc8316DewPointDiff=_Epc8316DewPointDiff_Object((1,3,6,1,4,1,28507,64,1,6,1,1,7),_Epc8316DewPointDiff_Type())
epc8316DewPointDiff.setMaxAccess(_C)
if mibBuilder.loadTexts:epc8316DewPointDiff.setStatus(_B)
if mibBuilder.loadTexts:epc8316DewPointDiff.setUnits(_P)
_Epc8316Conf_ObjectIdentity=ObjectIdentity
epc8316Conf=_Epc8316Conf_ObjectIdentity((1,3,6,1,4,1,28507,64,2))
_Epc8316Groups_ObjectIdentity=ObjectIdentity
epc8316Groups=_Epc8316Groups_ObjectIdentity((1,3,6,1,4,1,28507,64,2,1))
_Epc8316Compls_ObjectIdentity=ObjectIdentity
epc8316Compls=_Epc8316Compls_ObjectIdentity((1,3,6,1,4,1,28507,64,2,2))
_Events_ObjectIdentity=ObjectIdentity
events=_Events_ObjectIdentity((1,3,6,1,4,1,28507,64,3))
epc8316BasicGroup=ObjectGroup((1,3,6,1,4,1,28507,64,2,1,1))
epc8316BasicGroup.setObjects(*((_A,_n),(_A,_N),(_A,_o),(_A,_p),(_A,_I),(_A,_Q),(_A,_R),(_A,_S),(_A,_q),(_A,_r),(_A,_s),(_A,_t),(_A,_J),(_A,_u),(_A,_v),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_w),(_A,_x),(_A,_X),(_A,_Y),(_A,_y),(_A,_z),(_A,_A0),(_A,_A1),(_A,_A2),(_A,_A3),(_A,_A4),(_A,_A5),(_A,_A6),(_A,_A7),(_A,_A8),(_A,_A9),(_A,_AA),(_A,_K),(_A,_AB),(_A,_AC),(_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_AD),(_A,_AE),(_A,_d),(_A,_e),(_A,_AF),(_A,_AG),(_A,_AH),(_A,_AI),(_A,_AJ),(_A,_AK),(_A,_AL),(_A,_AM),(_A,_AN),(_A,_AO),(_A,_AP),(_A,_AQ),(_A,_H),(_A,_f),(_A,_g),(_A,_h),(_A,_i),(_A,_AR),(_A,_j)))
if mibBuilder.loadTexts:epc8316BasicGroup.setStatus(_B)
epc8316SwitchEvtPort=NotificationType((1,3,6,1,4,1,28507,64,3,1))
epc8316SwitchEvtPort.setObjects(*((_A,_I),(_A,_Q),(_A,_R),(_A,_S)))
if mibBuilder.loadTexts:epc8316SwitchEvtPort.setStatus(_B)
epc8316TempEvtSen=NotificationType((1,3,6,1,4,1,28507,64,3,2))
epc8316TempEvtSen.setObjects(*((_A,_H),(_A,_f)))
if mibBuilder.loadTexts:epc8316TempEvtSen.setStatus(_B)
epc8316HygroEvtSen=NotificationType((1,3,6,1,4,1,28507,64,3,3))
epc8316HygroEvtSen.setObjects(*((_A,_H),(_A,_g)))
if mibBuilder.loadTexts:epc8316HygroEvtSen.setStatus(_B)
epc8316InputEvtSen=NotificationType((1,3,6,1,4,1,28507,64,3,4))
epc8316InputEvtSen.setObjects(*((_A,_H),(_A,_h)))
if mibBuilder.loadTexts:epc8316InputEvtSen.setStatus(_B)
epc8316AirPressureEvtSen=NotificationType((1,3,6,1,4,1,28507,64,3,5))
epc8316AirPressureEvtSen.setObjects(*((_A,_H),(_A,_i)))
if mibBuilder.loadTexts:epc8316AirPressureEvtSen.setStatus(_B)
epc8316DewPtDiffEvtSen=NotificationType((1,3,6,1,4,1,28507,64,3,6))
epc8316DewPtDiffEvtSen.setObjects(*((_A,_H),(_A,_j)))
if mibBuilder.loadTexts:epc8316DewPtDiffEvtSen.setStatus(_B)
epc8316LineAmperageEvt=NotificationType((1,3,6,1,4,1,28507,64,3,7))
epc8316LineAmperageEvt.setObjects(*((_A,_J),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y)))
if mibBuilder.loadTexts:epc8316LineAmperageEvt.setStatus(_B)
epc8316PortAmperageEvt=NotificationType((1,3,6,1,4,1,28507,64,3,8))
epc8316PortAmperageEvt.setObjects(*((_A,_K),(_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_e)))
if mibBuilder.loadTexts:epc8316PortAmperageEvt.setStatus(_B)
epc8316NotificationGroup=NotificationGroup((1,3,6,1,4,1,28507,64,2,1,2))
epc8316NotificationGroup.setObjects(*((_A,_AS),(_A,_AT),(_A,_AU),(_A,_AV),(_A,_AW),(_A,_AX),(_A,_AY),(_A,_AZ)))
if mibBuilder.loadTexts:epc8316NotificationGroup.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'gudeads':gudeads,'gadsEPC8316':gadsEPC8316,'epc8316Objects':epc8316Objects,'epc8316CommonConfig':epc8316CommonConfig,'epc8316SNMPaccess':epc8316SNMPaccess,_n:epc8316TrapCtrl,'epc8316TrapIPTable':epc8316TrapIPTable,'epc8316TrapIPEntry':epc8316TrapIPEntry,_N:epc8316TrapIPIndex,_o:epc8316TrapAddr,'epc8316DeviceConfig':epc8316DeviceConfig,'epc8316IntActors':epc8316IntActors,'epc8316relayports':epc8316relayports,_p:epc8316portNumber,'epc8316portTable':epc8316portTable,'epc8316portEntry':epc8316portEntry,_I:epc8316PortIndex,_Q:epc8316PortName,_R:epc8316PortState,_S:epc8316PortSwitchCount,_q:epc8316PortStartupMode,_r:epc8316PortStartupDelay,_s:epc8316PortRepowerTime,'epc8316ExtActors':epc8316ExtActors,'epc8316IntSensors':epc8316IntSensors,'epc8316PowerChan':epc8316PowerChan,_t:epc8316ActivePowerChan,'epc8316PowerTable':epc8316PowerTable,'epc8316PowerEntry':epc8316PowerEntry,_J:epc8316PowerIndex,_u:epc8316ChanStatus,_v:epc8316AbsEnergyActive,_T:epc8316PowerActive,_U:epc8316Current,_V:epc8316Voltage,_W:epc8316Frequency,_w:epc8316PowerFactor,_x:epc8316Pangle,_X:epc8316PowerApparent,_Y:epc8316PowerReactive,_y:epc8316AbsEnergyReactive,_z:epc8316AbsEnergyActiveResettable,_A0:epc8316AbsEnergyReactiveResettable,_A1:epc8316ResetTime,_A2:epc8316ForwEnergyActive,_A3:epc8316ForwEnergyReactive,_A4:epc8316ForwEnergyActiveResettable,_A5:epc8316ForwEnergyReactiveResettable,_A6:epc8316RevEnergyActive,_A7:epc8316RevEnergyReactive,_A8:epc8316RevEnergyActiveResettable,_A9:epc8316RevEnergyReactiveResettable,'epc8316SinglePortPowerChan':epc8316SinglePortPowerChan,_AA:epc8316spActivePowerChan,'epc8316spPowerTable':epc8316spPowerTable,'epc8316spPowerEntry':epc8316spPowerEntry,_K:epc8316spPowerIndex,_AB:epc8316spChanStatus,_AC:epc8316spAbsEnergyActive,_Z:epc8316spPowerActive,_a:epc8316spCurrent,_b:epc8316spVoltage,_c:epc8316spFrequency,_AD:epc8316spPowerFactor,_AE:epc8316spPangle,_d:epc8316spPowerApparent,_e:epc8316spPowerReactive,_AF:epc8316spAbsEnergyReactive,_AG:epc8316spAbsEnergyActiveResettable,_AH:epc8316spAbsEnergyReactiveResettable,_AI:epc8316spResetTime,_AJ:epc8316spForwEnergyActive,_AK:epc8316spForwEnergyReactive,_AL:epc8316spForwEnergyActiveResettable,_AM:epc8316spForwEnergyReactiveResettable,_AN:epc8316spRevEnergyActive,_AO:epc8316spRevEnergyReactive,_AP:epc8316spRevEnergyActiveResettable,_AQ:epc8316spRevEnergyReactiveResettable,'epc8316ExtSensors':epc8316ExtSensors,'epc8316SensorTable':epc8316SensorTable,'epc8316SensorEntry':epc8316SensorEntry,_H:epc8316SensorIndex,_f:epc8316TempSensor,_g:epc8316HygroSensor,_h:epc8316InputSensor,_i:epc8316AirPressure,_AR:epc8316DewPoint,_j:epc8316DewPointDiff,'epc8316Conf':epc8316Conf,'epc8316Groups':epc8316Groups,'epc8316BasicGroup':epc8316BasicGroup,'epc8316NotificationGroup':epc8316NotificationGroup,'epc8316Compls':epc8316Compls,'events':events,_AS:epc8316SwitchEvtPort,_AT:epc8316TempEvtSen,_AU:epc8316HygroEvtSen,_AV:epc8316InputEvtSen,_AW:epc8316AirPressureEvtSen,_AX:epc8316DewPtDiffEvtSen,_AY:epc8316LineAmperageEvt,_AZ:epc8316PortAmperageEvt})