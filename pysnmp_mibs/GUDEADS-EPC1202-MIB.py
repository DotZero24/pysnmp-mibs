_AB='epc1202HygroEvtSen'
_AA='epc1202LineAmperageEvt'
_A9='epc1202OVPEvt'
_A8='epc1202DewPtDiffEvtSen'
_A7='epc1202AirPressureEvtSen'
_A6='epc1202InputEvtSen'
_A5='epc1202TempEvtSen'
_A4='epc1202SwitchEvtPort'
_A3='epc1202DewPoint'
_A2='epc1202RevEnergyReactiveResettable'
_A1='epc1202RevEnergyActiveResettable'
_A0='epc1202RevEnergyReactive'
_z='epc1202RevEnergyActive'
_y='epc1202ForwEnergyReactiveResettable'
_x='epc1202ForwEnergyActiveResettable'
_w='epc1202ForwEnergyReactive'
_v='epc1202ForwEnergyActive'
_u='epc1202ResetTime'
_t='epc1202AbsEnergyReactiveResettable'
_s='epc1202AbsEnergyActiveResettable'
_r='epc1202AbsEnergyReactive'
_q='epc1202Pangle'
_p='epc1202PowerFactor'
_o='epc1202AbsEnergyActive'
_n='epc1202ChanStatus'
_m='epc1202ActivePowerChan'
_l='epc1202PortRepowerTime'
_k='epc1202PortStartupDelay'
_j='epc1202PortStartupMode'
_i='epc1202portNumber'
_h='epc1202TrapAddr'
_g='epc1202TrapCtrl'
_f='seconds'
_e='Unsigned32'
_d='epc1202DewPointDiff'
_c='epc1202AirPressure'
_b='epc1202InputSensor'
_a='epc1202HygroSensor'
_Z='epc1202TempSensor'
_Y='epc1202OVPStatus'
_X='epc1202PowerReactive'
_W='epc1202PowerApparent'
_V='epc1202Frequency'
_U='epc1202Voltage'
_T='epc1202Current'
_S='epc1202PowerActive'
_R='epc1202PortSwitchCount'
_Q='epc1202PortState'
_P='epc1202PortName'
_O='0.1 degree Celsius'
_N='epc1202OVPIndex'
_M='off'
_L='epc1202TrapIPIndex'
_K='OctetString'
_J='epc1202PowerIndex'
_I='epc1202PortIndex'
_H='VARh'
_G='Wh'
_F='epc1202SensorIndex'
_E='read-write'
_D='Integer32'
_C='read-only'
_B='current'
_A='GUDEADS-EPC1202-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_K,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_e,'enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
gudeads=ModuleIdentity((1,3,6,1,4,1,28507))
if mibBuilder.loadTexts:gudeads.setRevisions(('2007-03-05 13:56',))
_GadsEPC1202_ObjectIdentity=ObjectIdentity
gadsEPC1202=_GadsEPC1202_ObjectIdentity((1,3,6,1,4,1,28507,43))
_Epc1202Objects_ObjectIdentity=ObjectIdentity
epc1202Objects=_Epc1202Objects_ObjectIdentity((1,3,6,1,4,1,28507,43,1))
_Epc1202CommonConfig_ObjectIdentity=ObjectIdentity
epc1202CommonConfig=_Epc1202CommonConfig_ObjectIdentity((1,3,6,1,4,1,28507,43,1,1))
_Epc1202SNMPaccess_ObjectIdentity=ObjectIdentity
epc1202SNMPaccess=_Epc1202SNMPaccess_ObjectIdentity((1,3,6,1,4,1,28507,43,1,1,1))
class _Epc1202TrapCtrl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3))
_Epc1202TrapCtrl_Type.__name__=_D
_Epc1202TrapCtrl_Object=MibScalar
epc1202TrapCtrl=_Epc1202TrapCtrl_Object((1,3,6,1,4,1,28507,43,1,1,1,1),_Epc1202TrapCtrl_Type())
epc1202TrapCtrl.setMaxAccess(_E)
if mibBuilder.loadTexts:epc1202TrapCtrl.setStatus(_B)
_Epc1202TrapIPTable_Object=MibTable
epc1202TrapIPTable=_Epc1202TrapIPTable_Object((1,3,6,1,4,1,28507,43,1,1,1,2))
if mibBuilder.loadTexts:epc1202TrapIPTable.setStatus(_B)
_Epc1202TrapIPEntry_Object=MibTableRow
epc1202TrapIPEntry=_Epc1202TrapIPEntry_Object((1,3,6,1,4,1,28507,43,1,1,1,2,1))
epc1202TrapIPEntry.setIndexNames((0,_A,_L))
if mibBuilder.loadTexts:epc1202TrapIPEntry.setStatus(_B)
class _Epc1202TrapIPIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_Epc1202TrapIPIndex_Type.__name__=_D
_Epc1202TrapIPIndex_Object=MibTableColumn
epc1202TrapIPIndex=_Epc1202TrapIPIndex_Object((1,3,6,1,4,1,28507,43,1,1,1,2,1,1),_Epc1202TrapIPIndex_Type())
epc1202TrapIPIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:epc1202TrapIPIndex.setStatus(_B)
class _Epc1202TrapAddr_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,99))
_Epc1202TrapAddr_Type.__name__=_K
_Epc1202TrapAddr_Object=MibTableColumn
epc1202TrapAddr=_Epc1202TrapAddr_Object((1,3,6,1,4,1,28507,43,1,1,1,2,1,2),_Epc1202TrapAddr_Type())
epc1202TrapAddr.setMaxAccess(_E)
if mibBuilder.loadTexts:epc1202TrapAddr.setStatus(_B)
_Epc1202DeviceConfig_ObjectIdentity=ObjectIdentity
epc1202DeviceConfig=_Epc1202DeviceConfig_ObjectIdentity((1,3,6,1,4,1,28507,43,1,2))
_Epc1202IntActors_ObjectIdentity=ObjectIdentity
epc1202IntActors=_Epc1202IntActors_ObjectIdentity((1,3,6,1,4,1,28507,43,1,3))
_Epc1202relayports_ObjectIdentity=ObjectIdentity
epc1202relayports=_Epc1202relayports_ObjectIdentity((1,3,6,1,4,1,28507,43,1,3,1))
class _Epc1202portNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_Epc1202portNumber_Type.__name__=_D
_Epc1202portNumber_Object=MibScalar
epc1202portNumber=_Epc1202portNumber_Object((1,3,6,1,4,1,28507,43,1,3,1,1),_Epc1202portNumber_Type())
epc1202portNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:epc1202portNumber.setStatus(_B)
_Epc1202portTable_Object=MibTable
epc1202portTable=_Epc1202portTable_Object((1,3,6,1,4,1,28507,43,1,3,1,2))
if mibBuilder.loadTexts:epc1202portTable.setStatus(_B)
_Epc1202portEntry_Object=MibTableRow
epc1202portEntry=_Epc1202portEntry_Object((1,3,6,1,4,1,28507,43,1,3,1,2,1))
epc1202portEntry.setIndexNames((0,_A,_I))
if mibBuilder.loadTexts:epc1202portEntry.setStatus(_B)
class _Epc1202PortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_Epc1202PortIndex_Type.__name__=_D
_Epc1202PortIndex_Object=MibTableColumn
epc1202PortIndex=_Epc1202PortIndex_Object((1,3,6,1,4,1,28507,43,1,3,1,2,1,1),_Epc1202PortIndex_Type())
epc1202PortIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:epc1202PortIndex.setStatus(_B)
class _Epc1202PortName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_Epc1202PortName_Type.__name__=_K
_Epc1202PortName_Object=MibTableColumn
epc1202PortName=_Epc1202PortName_Object((1,3,6,1,4,1,28507,43,1,3,1,2,1,2),_Epc1202PortName_Type())
epc1202PortName.setMaxAccess(_E)
if mibBuilder.loadTexts:epc1202PortName.setStatus(_B)
class _Epc1202PortState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_M,0),('on',1)))
_Epc1202PortState_Type.__name__=_D
_Epc1202PortState_Object=MibTableColumn
epc1202PortState=_Epc1202PortState_Object((1,3,6,1,4,1,28507,43,1,3,1,2,1,3),_Epc1202PortState_Type())
epc1202PortState.setMaxAccess(_E)
if mibBuilder.loadTexts:epc1202PortState.setStatus(_B)
_Epc1202PortSwitchCount_Type=Integer32
_Epc1202PortSwitchCount_Object=MibTableColumn
epc1202PortSwitchCount=_Epc1202PortSwitchCount_Object((1,3,6,1,4,1,28507,43,1,3,1,2,1,4),_Epc1202PortSwitchCount_Type())
epc1202PortSwitchCount.setMaxAccess(_C)
if mibBuilder.loadTexts:epc1202PortSwitchCount.setStatus(_B)
class _Epc1202PortStartupMode_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_M,0),('on',1),('laststate',2)))
_Epc1202PortStartupMode_Type.__name__=_D
_Epc1202PortStartupMode_Object=MibTableColumn
epc1202PortStartupMode=_Epc1202PortStartupMode_Object((1,3,6,1,4,1,28507,43,1,3,1,2,1,5),_Epc1202PortStartupMode_Type())
epc1202PortStartupMode.setMaxAccess(_E)
if mibBuilder.loadTexts:epc1202PortStartupMode.setStatus(_B)
class _Epc1202PortStartupDelay_Type(Integer32):defaultValue=0
_Epc1202PortStartupDelay_Type.__name__=_D
_Epc1202PortStartupDelay_Object=MibTableColumn
epc1202PortStartupDelay=_Epc1202PortStartupDelay_Object((1,3,6,1,4,1,28507,43,1,3,1,2,1,6),_Epc1202PortStartupDelay_Type())
epc1202PortStartupDelay.setMaxAccess(_E)
if mibBuilder.loadTexts:epc1202PortStartupDelay.setStatus(_B)
if mibBuilder.loadTexts:epc1202PortStartupDelay.setUnits(_f)
class _Epc1202PortRepowerTime_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Epc1202PortRepowerTime_Type.__name__=_D
_Epc1202PortRepowerTime_Object=MibTableColumn
epc1202PortRepowerTime=_Epc1202PortRepowerTime_Object((1,3,6,1,4,1,28507,43,1,3,1,2,1,7),_Epc1202PortRepowerTime_Type())
epc1202PortRepowerTime.setMaxAccess(_E)
if mibBuilder.loadTexts:epc1202PortRepowerTime.setStatus(_B)
if mibBuilder.loadTexts:epc1202PortRepowerTime.setUnits(_f)
_Epc1202ExtActors_ObjectIdentity=ObjectIdentity
epc1202ExtActors=_Epc1202ExtActors_ObjectIdentity((1,3,6,1,4,1,28507,43,1,4))
_Epc1202IntSensors_ObjectIdentity=ObjectIdentity
epc1202IntSensors=_Epc1202IntSensors_ObjectIdentity((1,3,6,1,4,1,28507,43,1,5))
_Epc1202PowerChan_ObjectIdentity=ObjectIdentity
epc1202PowerChan=_Epc1202PowerChan_ObjectIdentity((1,3,6,1,4,1,28507,43,1,5,1))
class _Epc1202ActivePowerChan_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1))
_Epc1202ActivePowerChan_Type.__name__=_e
_Epc1202ActivePowerChan_Object=MibScalar
epc1202ActivePowerChan=_Epc1202ActivePowerChan_Object((1,3,6,1,4,1,28507,43,1,5,1,1),_Epc1202ActivePowerChan_Type())
epc1202ActivePowerChan.setMaxAccess(_C)
if mibBuilder.loadTexts:epc1202ActivePowerChan.setStatus(_B)
_Epc1202PowerTable_Object=MibTable
epc1202PowerTable=_Epc1202PowerTable_Object((1,3,6,1,4,1,28507,43,1,5,1,2))
if mibBuilder.loadTexts:epc1202PowerTable.setStatus(_B)
_Epc1202PowerEntry_Object=MibTableRow
epc1202PowerEntry=_Epc1202PowerEntry_Object((1,3,6,1,4,1,28507,43,1,5,1,2,1))
epc1202PowerEntry.setIndexNames((0,_A,_J))
if mibBuilder.loadTexts:epc1202PowerEntry.setStatus(_B)
class _Epc1202PowerIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1))
_Epc1202PowerIndex_Type.__name__=_D
_Epc1202PowerIndex_Object=MibTableColumn
epc1202PowerIndex=_Epc1202PowerIndex_Object((1,3,6,1,4,1,28507,43,1,5,1,2,1,1),_Epc1202PowerIndex_Type())
epc1202PowerIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:epc1202PowerIndex.setStatus(_B)
class _Epc1202ChanStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Epc1202ChanStatus_Type.__name__=_D
_Epc1202ChanStatus_Object=MibTableColumn
epc1202ChanStatus=_Epc1202ChanStatus_Object((1,3,6,1,4,1,28507,43,1,5,1,2,1,2),_Epc1202ChanStatus_Type())
epc1202ChanStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:epc1202ChanStatus.setStatus(_B)
_Epc1202AbsEnergyActive_Type=Gauge32
_Epc1202AbsEnergyActive_Object=MibTableColumn
epc1202AbsEnergyActive=_Epc1202AbsEnergyActive_Object((1,3,6,1,4,1,28507,43,1,5,1,2,1,3),_Epc1202AbsEnergyActive_Type())
epc1202AbsEnergyActive.setMaxAccess(_C)
if mibBuilder.loadTexts:epc1202AbsEnergyActive.setStatus(_B)
if mibBuilder.loadTexts:epc1202AbsEnergyActive.setUnits(_G)
_Epc1202PowerActive_Type=Integer32
_Epc1202PowerActive_Object=MibTableColumn
epc1202PowerActive=_Epc1202PowerActive_Object((1,3,6,1,4,1,28507,43,1,5,1,2,1,4),_Epc1202PowerActive_Type())
epc1202PowerActive.setMaxAccess(_C)
if mibBuilder.loadTexts:epc1202PowerActive.setStatus(_B)
if mibBuilder.loadTexts:epc1202PowerActive.setUnits('W')
_Epc1202Current_Type=Gauge32
_Epc1202Current_Object=MibTableColumn
epc1202Current=_Epc1202Current_Object((1,3,6,1,4,1,28507,43,1,5,1,2,1,5),_Epc1202Current_Type())
epc1202Current.setMaxAccess(_C)
if mibBuilder.loadTexts:epc1202Current.setStatus(_B)
if mibBuilder.loadTexts:epc1202Current.setUnits('mA')
_Epc1202Voltage_Type=Gauge32
_Epc1202Voltage_Object=MibTableColumn
epc1202Voltage=_Epc1202Voltage_Object((1,3,6,1,4,1,28507,43,1,5,1,2,1,6),_Epc1202Voltage_Type())
epc1202Voltage.setMaxAccess(_C)
if mibBuilder.loadTexts:epc1202Voltage.setStatus(_B)
if mibBuilder.loadTexts:epc1202Voltage.setUnits('V')
_Epc1202Frequency_Type=Gauge32
_Epc1202Frequency_Object=MibTableColumn
epc1202Frequency=_Epc1202Frequency_Object((1,3,6,1,4,1,28507,43,1,5,1,2,1,7),_Epc1202Frequency_Type())
epc1202Frequency.setMaxAccess(_C)
if mibBuilder.loadTexts:epc1202Frequency.setStatus(_B)
if mibBuilder.loadTexts:epc1202Frequency.setUnits('0.01 hz')
_Epc1202PowerFactor_Type=Integer32
_Epc1202PowerFactor_Object=MibTableColumn
epc1202PowerFactor=_Epc1202PowerFactor_Object((1,3,6,1,4,1,28507,43,1,5,1,2,1,8),_Epc1202PowerFactor_Type())
epc1202PowerFactor.setMaxAccess(_C)
if mibBuilder.loadTexts:epc1202PowerFactor.setStatus(_B)
if mibBuilder.loadTexts:epc1202PowerFactor.setUnits('0.001')
_Epc1202Pangle_Type=Integer32
_Epc1202Pangle_Object=MibTableColumn
epc1202Pangle=_Epc1202Pangle_Object((1,3,6,1,4,1,28507,43,1,5,1,2,1,9),_Epc1202Pangle_Type())
epc1202Pangle.setMaxAccess(_C)
if mibBuilder.loadTexts:epc1202Pangle.setStatus(_B)
if mibBuilder.loadTexts:epc1202Pangle.setUnits('0.1 degree')
_Epc1202PowerApparent_Type=Integer32
_Epc1202PowerApparent_Object=MibTableColumn
epc1202PowerApparent=_Epc1202PowerApparent_Object((1,3,6,1,4,1,28507,43,1,5,1,2,1,10),_Epc1202PowerApparent_Type())
epc1202PowerApparent.setMaxAccess(_C)
if mibBuilder.loadTexts:epc1202PowerApparent.setStatus(_B)
if mibBuilder.loadTexts:epc1202PowerApparent.setUnits('VA')
_Epc1202PowerReactive_Type=Integer32
_Epc1202PowerReactive_Object=MibTableColumn
epc1202PowerReactive=_Epc1202PowerReactive_Object((1,3,6,1,4,1,28507,43,1,5,1,2,1,11),_Epc1202PowerReactive_Type())
epc1202PowerReactive.setMaxAccess(_C)
if mibBuilder.loadTexts:epc1202PowerReactive.setStatus(_B)
if mibBuilder.loadTexts:epc1202PowerReactive.setUnits('VAR')
_Epc1202AbsEnergyReactive_Type=Gauge32
_Epc1202AbsEnergyReactive_Object=MibTableColumn
epc1202AbsEnergyReactive=_Epc1202AbsEnergyReactive_Object((1,3,6,1,4,1,28507,43,1,5,1,2,1,12),_Epc1202AbsEnergyReactive_Type())
epc1202AbsEnergyReactive.setMaxAccess(_C)
if mibBuilder.loadTexts:epc1202AbsEnergyReactive.setStatus(_B)
if mibBuilder.loadTexts:epc1202AbsEnergyReactive.setUnits(_H)
_Epc1202AbsEnergyActiveResettable_Type=Gauge32
_Epc1202AbsEnergyActiveResettable_Object=MibTableColumn
epc1202AbsEnergyActiveResettable=_Epc1202AbsEnergyActiveResettable_Object((1,3,6,1,4,1,28507,43,1,5,1,2,1,13),_Epc1202AbsEnergyActiveResettable_Type())
epc1202AbsEnergyActiveResettable.setMaxAccess(_E)
if mibBuilder.loadTexts:epc1202AbsEnergyActiveResettable.setStatus(_B)
if mibBuilder.loadTexts:epc1202AbsEnergyActiveResettable.setUnits(_G)
_Epc1202AbsEnergyReactiveResettable_Type=Gauge32
_Epc1202AbsEnergyReactiveResettable_Object=MibTableColumn
epc1202AbsEnergyReactiveResettable=_Epc1202AbsEnergyReactiveResettable_Object((1,3,6,1,4,1,28507,43,1,5,1,2,1,14),_Epc1202AbsEnergyReactiveResettable_Type())
epc1202AbsEnergyReactiveResettable.setMaxAccess(_C)
if mibBuilder.loadTexts:epc1202AbsEnergyReactiveResettable.setStatus(_B)
if mibBuilder.loadTexts:epc1202AbsEnergyReactiveResettable.setUnits(_H)
_Epc1202ResetTime_Type=Gauge32
_Epc1202ResetTime_Object=MibTableColumn
epc1202ResetTime=_Epc1202ResetTime_Object((1,3,6,1,4,1,28507,43,1,5,1,2,1,15),_Epc1202ResetTime_Type())
epc1202ResetTime.setMaxAccess(_C)
if mibBuilder.loadTexts:epc1202ResetTime.setStatus(_B)
if mibBuilder.loadTexts:epc1202ResetTime.setUnits('s')
_Epc1202ForwEnergyActive_Type=Gauge32
_Epc1202ForwEnergyActive_Object=MibTableColumn
epc1202ForwEnergyActive=_Epc1202ForwEnergyActive_Object((1,3,6,1,4,1,28507,43,1,5,1,2,1,16),_Epc1202ForwEnergyActive_Type())
epc1202ForwEnergyActive.setMaxAccess(_C)
if mibBuilder.loadTexts:epc1202ForwEnergyActive.setStatus(_B)
if mibBuilder.loadTexts:epc1202ForwEnergyActive.setUnits(_G)
_Epc1202ForwEnergyReactive_Type=Gauge32
_Epc1202ForwEnergyReactive_Object=MibTableColumn
epc1202ForwEnergyReactive=_Epc1202ForwEnergyReactive_Object((1,3,6,1,4,1,28507,43,1,5,1,2,1,17),_Epc1202ForwEnergyReactive_Type())
epc1202ForwEnergyReactive.setMaxAccess(_C)
if mibBuilder.loadTexts:epc1202ForwEnergyReactive.setStatus(_B)
if mibBuilder.loadTexts:epc1202ForwEnergyReactive.setUnits(_H)
_Epc1202ForwEnergyActiveResettable_Type=Gauge32
_Epc1202ForwEnergyActiveResettable_Object=MibTableColumn
epc1202ForwEnergyActiveResettable=_Epc1202ForwEnergyActiveResettable_Object((1,3,6,1,4,1,28507,43,1,5,1,2,1,18),_Epc1202ForwEnergyActiveResettable_Type())
epc1202ForwEnergyActiveResettable.setMaxAccess(_C)
if mibBuilder.loadTexts:epc1202ForwEnergyActiveResettable.setStatus(_B)
if mibBuilder.loadTexts:epc1202ForwEnergyActiveResettable.setUnits(_G)
_Epc1202ForwEnergyReactiveResettable_Type=Gauge32
_Epc1202ForwEnergyReactiveResettable_Object=MibTableColumn
epc1202ForwEnergyReactiveResettable=_Epc1202ForwEnergyReactiveResettable_Object((1,3,6,1,4,1,28507,43,1,5,1,2,1,19),_Epc1202ForwEnergyReactiveResettable_Type())
epc1202ForwEnergyReactiveResettable.setMaxAccess(_C)
if mibBuilder.loadTexts:epc1202ForwEnergyReactiveResettable.setStatus(_B)
if mibBuilder.loadTexts:epc1202ForwEnergyReactiveResettable.setUnits(_H)
_Epc1202RevEnergyActive_Type=Gauge32
_Epc1202RevEnergyActive_Object=MibTableColumn
epc1202RevEnergyActive=_Epc1202RevEnergyActive_Object((1,3,6,1,4,1,28507,43,1,5,1,2,1,20),_Epc1202RevEnergyActive_Type())
epc1202RevEnergyActive.setMaxAccess(_C)
if mibBuilder.loadTexts:epc1202RevEnergyActive.setStatus(_B)
if mibBuilder.loadTexts:epc1202RevEnergyActive.setUnits(_G)
_Epc1202RevEnergyReactive_Type=Gauge32
_Epc1202RevEnergyReactive_Object=MibTableColumn
epc1202RevEnergyReactive=_Epc1202RevEnergyReactive_Object((1,3,6,1,4,1,28507,43,1,5,1,2,1,21),_Epc1202RevEnergyReactive_Type())
epc1202RevEnergyReactive.setMaxAccess(_C)
if mibBuilder.loadTexts:epc1202RevEnergyReactive.setStatus(_B)
if mibBuilder.loadTexts:epc1202RevEnergyReactive.setUnits(_H)
_Epc1202RevEnergyActiveResettable_Type=Gauge32
_Epc1202RevEnergyActiveResettable_Object=MibTableColumn
epc1202RevEnergyActiveResettable=_Epc1202RevEnergyActiveResettable_Object((1,3,6,1,4,1,28507,43,1,5,1,2,1,22),_Epc1202RevEnergyActiveResettable_Type())
epc1202RevEnergyActiveResettable.setMaxAccess(_C)
if mibBuilder.loadTexts:epc1202RevEnergyActiveResettable.setStatus(_B)
if mibBuilder.loadTexts:epc1202RevEnergyActiveResettable.setUnits(_G)
_Epc1202RevEnergyReactiveResettable_Type=Gauge32
_Epc1202RevEnergyReactiveResettable_Object=MibTableColumn
epc1202RevEnergyReactiveResettable=_Epc1202RevEnergyReactiveResettable_Object((1,3,6,1,4,1,28507,43,1,5,1,2,1,23),_Epc1202RevEnergyReactiveResettable_Type())
epc1202RevEnergyReactiveResettable.setMaxAccess(_C)
if mibBuilder.loadTexts:epc1202RevEnergyReactiveResettable.setStatus(_B)
if mibBuilder.loadTexts:epc1202RevEnergyReactiveResettable.setUnits(_H)
_Epc1202OVPTable_Object=MibTable
epc1202OVPTable=_Epc1202OVPTable_Object((1,3,6,1,4,1,28507,43,1,5,2))
if mibBuilder.loadTexts:epc1202OVPTable.setStatus(_B)
_Epc1202OVPEntry_Object=MibTableRow
epc1202OVPEntry=_Epc1202OVPEntry_Object((1,3,6,1,4,1,28507,43,1,5,2,1))
epc1202OVPEntry.setIndexNames((0,_A,_N))
if mibBuilder.loadTexts:epc1202OVPEntry.setStatus(_B)
class _Epc1202OVPIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1))
_Epc1202OVPIndex_Type.__name__=_D
_Epc1202OVPIndex_Object=MibTableColumn
epc1202OVPIndex=_Epc1202OVPIndex_Object((1,3,6,1,4,1,28507,43,1,5,2,1,1),_Epc1202OVPIndex_Type())
epc1202OVPIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:epc1202OVPIndex.setStatus(_B)
class _Epc1202OVPStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('failure',0),('ok',1),('unknown',2)))
_Epc1202OVPStatus_Type.__name__=_D
_Epc1202OVPStatus_Object=MibTableColumn
epc1202OVPStatus=_Epc1202OVPStatus_Object((1,3,6,1,4,1,28507,43,1,5,2,1,2),_Epc1202OVPStatus_Type())
epc1202OVPStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:epc1202OVPStatus.setStatus(_B)
_Epc1202ExtSensors_ObjectIdentity=ObjectIdentity
epc1202ExtSensors=_Epc1202ExtSensors_ObjectIdentity((1,3,6,1,4,1,28507,43,1,6))
_Epc1202SensorTable_Object=MibTable
epc1202SensorTable=_Epc1202SensorTable_Object((1,3,6,1,4,1,28507,43,1,6,1))
if mibBuilder.loadTexts:epc1202SensorTable.setStatus(_B)
_Epc1202SensorEntry_Object=MibTableRow
epc1202SensorEntry=_Epc1202SensorEntry_Object((1,3,6,1,4,1,28507,43,1,6,1,1))
epc1202SensorEntry.setIndexNames((0,_A,_F))
if mibBuilder.loadTexts:epc1202SensorEntry.setStatus(_B)
class _Epc1202SensorIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1))
_Epc1202SensorIndex_Type.__name__=_D
_Epc1202SensorIndex_Object=MibTableColumn
epc1202SensorIndex=_Epc1202SensorIndex_Object((1,3,6,1,4,1,28507,43,1,6,1,1,1),_Epc1202SensorIndex_Type())
epc1202SensorIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:epc1202SensorIndex.setStatus(_B)
_Epc1202TempSensor_Type=Integer32
_Epc1202TempSensor_Object=MibTableColumn
epc1202TempSensor=_Epc1202TempSensor_Object((1,3,6,1,4,1,28507,43,1,6,1,1,2),_Epc1202TempSensor_Type())
epc1202TempSensor.setMaxAccess(_C)
if mibBuilder.loadTexts:epc1202TempSensor.setStatus(_B)
if mibBuilder.loadTexts:epc1202TempSensor.setUnits(_O)
_Epc1202HygroSensor_Type=Integer32
_Epc1202HygroSensor_Object=MibTableColumn
epc1202HygroSensor=_Epc1202HygroSensor_Object((1,3,6,1,4,1,28507,43,1,6,1,1,3),_Epc1202HygroSensor_Type())
epc1202HygroSensor.setMaxAccess(_C)
if mibBuilder.loadTexts:epc1202HygroSensor.setStatus(_B)
if mibBuilder.loadTexts:epc1202HygroSensor.setUnits('0.1 percent humidity')
class _Epc1202InputSensor_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_M,0),('on',1)))
_Epc1202InputSensor_Type.__name__=_D
_Epc1202InputSensor_Object=MibTableColumn
epc1202InputSensor=_Epc1202InputSensor_Object((1,3,6,1,4,1,28507,43,1,6,1,1,4),_Epc1202InputSensor_Type())
epc1202InputSensor.setMaxAccess(_C)
if mibBuilder.loadTexts:epc1202InputSensor.setStatus(_B)
_Epc1202AirPressure_Type=Integer32
_Epc1202AirPressure_Object=MibTableColumn
epc1202AirPressure=_Epc1202AirPressure_Object((1,3,6,1,4,1,28507,43,1,6,1,1,5),_Epc1202AirPressure_Type())
epc1202AirPressure.setMaxAccess(_C)
if mibBuilder.loadTexts:epc1202AirPressure.setStatus(_B)
if mibBuilder.loadTexts:epc1202AirPressure.setUnits('1 hPA (hectopascal) ~ 1 milibar')
_Epc1202DewPoint_Type=Integer32
_Epc1202DewPoint_Object=MibTableColumn
epc1202DewPoint=_Epc1202DewPoint_Object((1,3,6,1,4,1,28507,43,1,6,1,1,6),_Epc1202DewPoint_Type())
epc1202DewPoint.setMaxAccess(_C)
if mibBuilder.loadTexts:epc1202DewPoint.setStatus(_B)
if mibBuilder.loadTexts:epc1202DewPoint.setUnits(_O)
_Epc1202DewPointDiff_Type=Integer32
_Epc1202DewPointDiff_Object=MibTableColumn
epc1202DewPointDiff=_Epc1202DewPointDiff_Object((1,3,6,1,4,1,28507,43,1,6,1,1,7),_Epc1202DewPointDiff_Type())
epc1202DewPointDiff.setMaxAccess(_C)
if mibBuilder.loadTexts:epc1202DewPointDiff.setStatus(_B)
if mibBuilder.loadTexts:epc1202DewPointDiff.setUnits(_O)
_Epc1202Conf_ObjectIdentity=ObjectIdentity
epc1202Conf=_Epc1202Conf_ObjectIdentity((1,3,6,1,4,1,28507,43,2))
_Epc1202Groups_ObjectIdentity=ObjectIdentity
epc1202Groups=_Epc1202Groups_ObjectIdentity((1,3,6,1,4,1,28507,43,2,1))
_Epc1202Compls_ObjectIdentity=ObjectIdentity
epc1202Compls=_Epc1202Compls_ObjectIdentity((1,3,6,1,4,1,28507,43,2,2))
_Events_ObjectIdentity=ObjectIdentity
events=_Events_ObjectIdentity((1,3,6,1,4,1,28507,43,3))
epc1202BasicGroup=ObjectGroup((1,3,6,1,4,1,28507,43,2,1,1))
epc1202BasicGroup.setObjects(*((_A,_g),(_A,_L),(_A,_h),(_A,_i),(_A,_I),(_A,_P),(_A,_Q),(_A,_R),(_A,_j),(_A,_k),(_A,_l),(_A,_m),(_A,_J),(_A,_n),(_A,_o),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_p),(_A,_q),(_A,_W),(_A,_X),(_A,_r),(_A,_s),(_A,_t),(_A,_u),(_A,_v),(_A,_w),(_A,_x),(_A,_y),(_A,_z),(_A,_A0),(_A,_A1),(_A,_A2),(_A,_N),(_A,_Y),(_A,_F),(_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_A3),(_A,_d)))
if mibBuilder.loadTexts:epc1202BasicGroup.setStatus(_B)
epc1202SwitchEvtPort=NotificationType((1,3,6,1,4,1,28507,43,3,1))
epc1202SwitchEvtPort.setObjects(*((_A,_I),(_A,_P),(_A,_Q),(_A,_R)))
if mibBuilder.loadTexts:epc1202SwitchEvtPort.setStatus(_B)
epc1202TempEvtSen=NotificationType((1,3,6,1,4,1,28507,43,3,2))
epc1202TempEvtSen.setObjects(*((_A,_F),(_A,_Z)))
if mibBuilder.loadTexts:epc1202TempEvtSen.setStatus(_B)
epc1202HygroEvtSen=NotificationType((1,3,6,1,4,1,28507,43,3,3))
epc1202HygroEvtSen.setObjects(*((_A,_F),(_A,_a)))
if mibBuilder.loadTexts:epc1202HygroEvtSen.setStatus(_B)
epc1202InputEvtSen=NotificationType((1,3,6,1,4,1,28507,43,3,4))
epc1202InputEvtSen.setObjects(*((_A,_F),(_A,_b)))
if mibBuilder.loadTexts:epc1202InputEvtSen.setStatus(_B)
epc1202AirPressureEvtSen=NotificationType((1,3,6,1,4,1,28507,43,3,5))
epc1202AirPressureEvtSen.setObjects(*((_A,_F),(_A,_c)))
if mibBuilder.loadTexts:epc1202AirPressureEvtSen.setStatus(_B)
epc1202DewPtDiffEvtSen=NotificationType((1,3,6,1,4,1,28507,43,3,6))
epc1202DewPtDiffEvtSen.setObjects(*((_A,_F),(_A,_d)))
if mibBuilder.loadTexts:epc1202DewPtDiffEvtSen.setStatus(_B)
epc1202OVPEvt=NotificationType((1,3,6,1,4,1,28507,43,3,7))
epc1202OVPEvt.setObjects((_A,_Y))
if mibBuilder.loadTexts:epc1202OVPEvt.setStatus(_B)
epc1202LineAmperageEvt=NotificationType((1,3,6,1,4,1,28507,43,3,8))
epc1202LineAmperageEvt.setObjects(*((_A,_J),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X)))
if mibBuilder.loadTexts:epc1202LineAmperageEvt.setStatus(_B)
epc1202NotificationGroup=NotificationGroup((1,3,6,1,4,1,28507,43,2,1,2))
epc1202NotificationGroup.setObjects(*((_A,_A4),(_A,_A5),(_A,_A6),(_A,_A7),(_A,_A8),(_A,_A9),(_A,_AA),(_A,_AB)))
if mibBuilder.loadTexts:epc1202NotificationGroup.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'gudeads':gudeads,'gadsEPC1202':gadsEPC1202,'epc1202Objects':epc1202Objects,'epc1202CommonConfig':epc1202CommonConfig,'epc1202SNMPaccess':epc1202SNMPaccess,_g:epc1202TrapCtrl,'epc1202TrapIPTable':epc1202TrapIPTable,'epc1202TrapIPEntry':epc1202TrapIPEntry,_L:epc1202TrapIPIndex,_h:epc1202TrapAddr,'epc1202DeviceConfig':epc1202DeviceConfig,'epc1202IntActors':epc1202IntActors,'epc1202relayports':epc1202relayports,_i:epc1202portNumber,'epc1202portTable':epc1202portTable,'epc1202portEntry':epc1202portEntry,_I:epc1202PortIndex,_P:epc1202PortName,_Q:epc1202PortState,_R:epc1202PortSwitchCount,_j:epc1202PortStartupMode,_k:epc1202PortStartupDelay,_l:epc1202PortRepowerTime,'epc1202ExtActors':epc1202ExtActors,'epc1202IntSensors':epc1202IntSensors,'epc1202PowerChan':epc1202PowerChan,_m:epc1202ActivePowerChan,'epc1202PowerTable':epc1202PowerTable,'epc1202PowerEntry':epc1202PowerEntry,_J:epc1202PowerIndex,_n:epc1202ChanStatus,_o:epc1202AbsEnergyActive,_S:epc1202PowerActive,_T:epc1202Current,_U:epc1202Voltage,_V:epc1202Frequency,_p:epc1202PowerFactor,_q:epc1202Pangle,_W:epc1202PowerApparent,_X:epc1202PowerReactive,_r:epc1202AbsEnergyReactive,_s:epc1202AbsEnergyActiveResettable,_t:epc1202AbsEnergyReactiveResettable,_u:epc1202ResetTime,_v:epc1202ForwEnergyActive,_w:epc1202ForwEnergyReactive,_x:epc1202ForwEnergyActiveResettable,_y:epc1202ForwEnergyReactiveResettable,_z:epc1202RevEnergyActive,_A0:epc1202RevEnergyReactive,_A1:epc1202RevEnergyActiveResettable,_A2:epc1202RevEnergyReactiveResettable,'epc1202OVPTable':epc1202OVPTable,'epc1202OVPEntry':epc1202OVPEntry,_N:epc1202OVPIndex,_Y:epc1202OVPStatus,'epc1202ExtSensors':epc1202ExtSensors,'epc1202SensorTable':epc1202SensorTable,'epc1202SensorEntry':epc1202SensorEntry,_F:epc1202SensorIndex,_Z:epc1202TempSensor,_a:epc1202HygroSensor,_b:epc1202InputSensor,_c:epc1202AirPressure,_A3:epc1202DewPoint,_d:epc1202DewPointDiff,'epc1202Conf':epc1202Conf,'epc1202Groups':epc1202Groups,'epc1202BasicGroup':epc1202BasicGroup,'epc1202NotificationGroup':epc1202NotificationGroup,'epc1202Compls':epc1202Compls,'events':events,_A4:epc1202SwitchEvtPort,_A5:epc1202TempEvtSen,_AB:epc1202HygroEvtSen,_A6:epc1202InputEvtSen,_A7:epc1202AirPressureEvtSen,_A8:epc1202DewPtDiffEvtSen,_A9:epc1202OVPEvt,_AA:epc1202LineAmperageEvt})