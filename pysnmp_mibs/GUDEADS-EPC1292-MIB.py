_AB='epc1292HygroEvtSen'
_AA='epc1292LineAmperageEvt'
_A9='epc1292OVPEvt'
_A8='epc1292DewPtDiffEvtSen'
_A7='epc1292AirPressureEvtSen'
_A6='epc1292InputEvtSen'
_A5='epc1292TempEvtSen'
_A4='epc1292SwitchEvtPort'
_A3='epc1292DewPoint'
_A2='epc1292RevEnergyReactiveResettable'
_A1='epc1292RevEnergyActiveResettable'
_A0='epc1292RevEnergyReactive'
_z='epc1292RevEnergyActive'
_y='epc1292ForwEnergyReactiveResettable'
_x='epc1292ForwEnergyActiveResettable'
_w='epc1292ForwEnergyReactive'
_v='epc1292ForwEnergyActive'
_u='epc1292ResetTime'
_t='epc1292AbsEnergyReactiveResettable'
_s='epc1292AbsEnergyActiveResettable'
_r='epc1292AbsEnergyReactive'
_q='epc1292Pangle'
_p='epc1292PowerFactor'
_o='epc1292AbsEnergyActive'
_n='epc1292ChanStatus'
_m='epc1292ActivePowerChan'
_l='epc1292PortRepowerTime'
_k='epc1292PortStartupDelay'
_j='epc1292PortStartupMode'
_i='epc1292portNumber'
_h='epc1292TrapAddr'
_g='epc1292TrapCtrl'
_f='seconds'
_e='Unsigned32'
_d='epc1292DewPointDiff'
_c='epc1292AirPressure'
_b='epc1292InputSensor'
_a='epc1292HygroSensor'
_Z='epc1292TempSensor'
_Y='epc1292OVPStatus'
_X='epc1292PowerReactive'
_W='epc1292PowerApparent'
_V='epc1292Frequency'
_U='epc1292Voltage'
_T='epc1292Current'
_S='epc1292PowerActive'
_R='epc1292PortSwitchCount'
_Q='epc1292PortState'
_P='epc1292PortName'
_O='0.1 degree Celsius'
_N='epc1292OVPIndex'
_M='off'
_L='epc1292TrapIPIndex'
_K='OctetString'
_J='epc1292PowerIndex'
_I='epc1292PortIndex'
_H='VARh'
_G='Wh'
_F='epc1292SensorIndex'
_E='read-write'
_D='Integer32'
_C='read-only'
_B='current'
_A='GUDEADS-EPC1292-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_K,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_e,'enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
gudeads=ModuleIdentity((1,3,6,1,4,1,28507))
if mibBuilder.loadTexts:gudeads.setRevisions(('2007-03-05 13:56',))
_GadsEPC1292_ObjectIdentity=ObjectIdentity
gadsEPC1292=_GadsEPC1292_ObjectIdentity((1,3,6,1,4,1,28507,50))
_Epc1292Objects_ObjectIdentity=ObjectIdentity
epc1292Objects=_Epc1292Objects_ObjectIdentity((1,3,6,1,4,1,28507,50,1))
_Epc1292CommonConfig_ObjectIdentity=ObjectIdentity
epc1292CommonConfig=_Epc1292CommonConfig_ObjectIdentity((1,3,6,1,4,1,28507,50,1,1))
_Epc1292SNMPaccess_ObjectIdentity=ObjectIdentity
epc1292SNMPaccess=_Epc1292SNMPaccess_ObjectIdentity((1,3,6,1,4,1,28507,50,1,1,1))
class _Epc1292TrapCtrl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3))
_Epc1292TrapCtrl_Type.__name__=_D
_Epc1292TrapCtrl_Object=MibScalar
epc1292TrapCtrl=_Epc1292TrapCtrl_Object((1,3,6,1,4,1,28507,50,1,1,1,1),_Epc1292TrapCtrl_Type())
epc1292TrapCtrl.setMaxAccess(_E)
if mibBuilder.loadTexts:epc1292TrapCtrl.setStatus(_B)
_Epc1292TrapIPTable_Object=MibTable
epc1292TrapIPTable=_Epc1292TrapIPTable_Object((1,3,6,1,4,1,28507,50,1,1,1,2))
if mibBuilder.loadTexts:epc1292TrapIPTable.setStatus(_B)
_Epc1292TrapIPEntry_Object=MibTableRow
epc1292TrapIPEntry=_Epc1292TrapIPEntry_Object((1,3,6,1,4,1,28507,50,1,1,1,2,1))
epc1292TrapIPEntry.setIndexNames((0,_A,_L))
if mibBuilder.loadTexts:epc1292TrapIPEntry.setStatus(_B)
class _Epc1292TrapIPIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_Epc1292TrapIPIndex_Type.__name__=_D
_Epc1292TrapIPIndex_Object=MibTableColumn
epc1292TrapIPIndex=_Epc1292TrapIPIndex_Object((1,3,6,1,4,1,28507,50,1,1,1,2,1,1),_Epc1292TrapIPIndex_Type())
epc1292TrapIPIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:epc1292TrapIPIndex.setStatus(_B)
class _Epc1292TrapAddr_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,99))
_Epc1292TrapAddr_Type.__name__=_K
_Epc1292TrapAddr_Object=MibTableColumn
epc1292TrapAddr=_Epc1292TrapAddr_Object((1,3,6,1,4,1,28507,50,1,1,1,2,1,2),_Epc1292TrapAddr_Type())
epc1292TrapAddr.setMaxAccess(_E)
if mibBuilder.loadTexts:epc1292TrapAddr.setStatus(_B)
_Epc1292DeviceConfig_ObjectIdentity=ObjectIdentity
epc1292DeviceConfig=_Epc1292DeviceConfig_ObjectIdentity((1,3,6,1,4,1,28507,50,1,2))
_Epc1292IntActors_ObjectIdentity=ObjectIdentity
epc1292IntActors=_Epc1292IntActors_ObjectIdentity((1,3,6,1,4,1,28507,50,1,3))
_Epc1292relayports_ObjectIdentity=ObjectIdentity
epc1292relayports=_Epc1292relayports_ObjectIdentity((1,3,6,1,4,1,28507,50,1,3,1))
class _Epc1292portNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_Epc1292portNumber_Type.__name__=_D
_Epc1292portNumber_Object=MibScalar
epc1292portNumber=_Epc1292portNumber_Object((1,3,6,1,4,1,28507,50,1,3,1,1),_Epc1292portNumber_Type())
epc1292portNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:epc1292portNumber.setStatus(_B)
_Epc1292portTable_Object=MibTable
epc1292portTable=_Epc1292portTable_Object((1,3,6,1,4,1,28507,50,1,3,1,2))
if mibBuilder.loadTexts:epc1292portTable.setStatus(_B)
_Epc1292portEntry_Object=MibTableRow
epc1292portEntry=_Epc1292portEntry_Object((1,3,6,1,4,1,28507,50,1,3,1,2,1))
epc1292portEntry.setIndexNames((0,_A,_I))
if mibBuilder.loadTexts:epc1292portEntry.setStatus(_B)
class _Epc1292PortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_Epc1292PortIndex_Type.__name__=_D
_Epc1292PortIndex_Object=MibTableColumn
epc1292PortIndex=_Epc1292PortIndex_Object((1,3,6,1,4,1,28507,50,1,3,1,2,1,1),_Epc1292PortIndex_Type())
epc1292PortIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:epc1292PortIndex.setStatus(_B)
class _Epc1292PortName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_Epc1292PortName_Type.__name__=_K
_Epc1292PortName_Object=MibTableColumn
epc1292PortName=_Epc1292PortName_Object((1,3,6,1,4,1,28507,50,1,3,1,2,1,2),_Epc1292PortName_Type())
epc1292PortName.setMaxAccess(_E)
if mibBuilder.loadTexts:epc1292PortName.setStatus(_B)
class _Epc1292PortState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_M,0),('on',1)))
_Epc1292PortState_Type.__name__=_D
_Epc1292PortState_Object=MibTableColumn
epc1292PortState=_Epc1292PortState_Object((1,3,6,1,4,1,28507,50,1,3,1,2,1,3),_Epc1292PortState_Type())
epc1292PortState.setMaxAccess(_E)
if mibBuilder.loadTexts:epc1292PortState.setStatus(_B)
_Epc1292PortSwitchCount_Type=Integer32
_Epc1292PortSwitchCount_Object=MibTableColumn
epc1292PortSwitchCount=_Epc1292PortSwitchCount_Object((1,3,6,1,4,1,28507,50,1,3,1,2,1,4),_Epc1292PortSwitchCount_Type())
epc1292PortSwitchCount.setMaxAccess(_C)
if mibBuilder.loadTexts:epc1292PortSwitchCount.setStatus(_B)
class _Epc1292PortStartupMode_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_M,0),('on',1),('laststate',2)))
_Epc1292PortStartupMode_Type.__name__=_D
_Epc1292PortStartupMode_Object=MibTableColumn
epc1292PortStartupMode=_Epc1292PortStartupMode_Object((1,3,6,1,4,1,28507,50,1,3,1,2,1,5),_Epc1292PortStartupMode_Type())
epc1292PortStartupMode.setMaxAccess(_E)
if mibBuilder.loadTexts:epc1292PortStartupMode.setStatus(_B)
class _Epc1292PortStartupDelay_Type(Integer32):defaultValue=0
_Epc1292PortStartupDelay_Type.__name__=_D
_Epc1292PortStartupDelay_Object=MibTableColumn
epc1292PortStartupDelay=_Epc1292PortStartupDelay_Object((1,3,6,1,4,1,28507,50,1,3,1,2,1,6),_Epc1292PortStartupDelay_Type())
epc1292PortStartupDelay.setMaxAccess(_E)
if mibBuilder.loadTexts:epc1292PortStartupDelay.setStatus(_B)
if mibBuilder.loadTexts:epc1292PortStartupDelay.setUnits(_f)
class _Epc1292PortRepowerTime_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Epc1292PortRepowerTime_Type.__name__=_D
_Epc1292PortRepowerTime_Object=MibTableColumn
epc1292PortRepowerTime=_Epc1292PortRepowerTime_Object((1,3,6,1,4,1,28507,50,1,3,1,2,1,7),_Epc1292PortRepowerTime_Type())
epc1292PortRepowerTime.setMaxAccess(_E)
if mibBuilder.loadTexts:epc1292PortRepowerTime.setStatus(_B)
if mibBuilder.loadTexts:epc1292PortRepowerTime.setUnits(_f)
_Epc1292ExtActors_ObjectIdentity=ObjectIdentity
epc1292ExtActors=_Epc1292ExtActors_ObjectIdentity((1,3,6,1,4,1,28507,50,1,4))
_Epc1292IntSensors_ObjectIdentity=ObjectIdentity
epc1292IntSensors=_Epc1292IntSensors_ObjectIdentity((1,3,6,1,4,1,28507,50,1,5))
_Epc1292PowerChan_ObjectIdentity=ObjectIdentity
epc1292PowerChan=_Epc1292PowerChan_ObjectIdentity((1,3,6,1,4,1,28507,50,1,5,1))
class _Epc1292ActivePowerChan_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1))
_Epc1292ActivePowerChan_Type.__name__=_e
_Epc1292ActivePowerChan_Object=MibScalar
epc1292ActivePowerChan=_Epc1292ActivePowerChan_Object((1,3,6,1,4,1,28507,50,1,5,1,1),_Epc1292ActivePowerChan_Type())
epc1292ActivePowerChan.setMaxAccess(_C)
if mibBuilder.loadTexts:epc1292ActivePowerChan.setStatus(_B)
_Epc1292PowerTable_Object=MibTable
epc1292PowerTable=_Epc1292PowerTable_Object((1,3,6,1,4,1,28507,50,1,5,1,2))
if mibBuilder.loadTexts:epc1292PowerTable.setStatus(_B)
_Epc1292PowerEntry_Object=MibTableRow
epc1292PowerEntry=_Epc1292PowerEntry_Object((1,3,6,1,4,1,28507,50,1,5,1,2,1))
epc1292PowerEntry.setIndexNames((0,_A,_J))
if mibBuilder.loadTexts:epc1292PowerEntry.setStatus(_B)
class _Epc1292PowerIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1))
_Epc1292PowerIndex_Type.__name__=_D
_Epc1292PowerIndex_Object=MibTableColumn
epc1292PowerIndex=_Epc1292PowerIndex_Object((1,3,6,1,4,1,28507,50,1,5,1,2,1,1),_Epc1292PowerIndex_Type())
epc1292PowerIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:epc1292PowerIndex.setStatus(_B)
class _Epc1292ChanStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Epc1292ChanStatus_Type.__name__=_D
_Epc1292ChanStatus_Object=MibTableColumn
epc1292ChanStatus=_Epc1292ChanStatus_Object((1,3,6,1,4,1,28507,50,1,5,1,2,1,2),_Epc1292ChanStatus_Type())
epc1292ChanStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:epc1292ChanStatus.setStatus(_B)
_Epc1292AbsEnergyActive_Type=Gauge32
_Epc1292AbsEnergyActive_Object=MibTableColumn
epc1292AbsEnergyActive=_Epc1292AbsEnergyActive_Object((1,3,6,1,4,1,28507,50,1,5,1,2,1,3),_Epc1292AbsEnergyActive_Type())
epc1292AbsEnergyActive.setMaxAccess(_C)
if mibBuilder.loadTexts:epc1292AbsEnergyActive.setStatus(_B)
if mibBuilder.loadTexts:epc1292AbsEnergyActive.setUnits(_G)
_Epc1292PowerActive_Type=Integer32
_Epc1292PowerActive_Object=MibTableColumn
epc1292PowerActive=_Epc1292PowerActive_Object((1,3,6,1,4,1,28507,50,1,5,1,2,1,4),_Epc1292PowerActive_Type())
epc1292PowerActive.setMaxAccess(_C)
if mibBuilder.loadTexts:epc1292PowerActive.setStatus(_B)
if mibBuilder.loadTexts:epc1292PowerActive.setUnits('W')
_Epc1292Current_Type=Gauge32
_Epc1292Current_Object=MibTableColumn
epc1292Current=_Epc1292Current_Object((1,3,6,1,4,1,28507,50,1,5,1,2,1,5),_Epc1292Current_Type())
epc1292Current.setMaxAccess(_C)
if mibBuilder.loadTexts:epc1292Current.setStatus(_B)
if mibBuilder.loadTexts:epc1292Current.setUnits('mA')
_Epc1292Voltage_Type=Gauge32
_Epc1292Voltage_Object=MibTableColumn
epc1292Voltage=_Epc1292Voltage_Object((1,3,6,1,4,1,28507,50,1,5,1,2,1,6),_Epc1292Voltage_Type())
epc1292Voltage.setMaxAccess(_C)
if mibBuilder.loadTexts:epc1292Voltage.setStatus(_B)
if mibBuilder.loadTexts:epc1292Voltage.setUnits('V')
_Epc1292Frequency_Type=Gauge32
_Epc1292Frequency_Object=MibTableColumn
epc1292Frequency=_Epc1292Frequency_Object((1,3,6,1,4,1,28507,50,1,5,1,2,1,7),_Epc1292Frequency_Type())
epc1292Frequency.setMaxAccess(_C)
if mibBuilder.loadTexts:epc1292Frequency.setStatus(_B)
if mibBuilder.loadTexts:epc1292Frequency.setUnits('0.01 hz')
_Epc1292PowerFactor_Type=Integer32
_Epc1292PowerFactor_Object=MibTableColumn
epc1292PowerFactor=_Epc1292PowerFactor_Object((1,3,6,1,4,1,28507,50,1,5,1,2,1,8),_Epc1292PowerFactor_Type())
epc1292PowerFactor.setMaxAccess(_C)
if mibBuilder.loadTexts:epc1292PowerFactor.setStatus(_B)
if mibBuilder.loadTexts:epc1292PowerFactor.setUnits('0.001')
_Epc1292Pangle_Type=Integer32
_Epc1292Pangle_Object=MibTableColumn
epc1292Pangle=_Epc1292Pangle_Object((1,3,6,1,4,1,28507,50,1,5,1,2,1,9),_Epc1292Pangle_Type())
epc1292Pangle.setMaxAccess(_C)
if mibBuilder.loadTexts:epc1292Pangle.setStatus(_B)
if mibBuilder.loadTexts:epc1292Pangle.setUnits('0.1 degree')
_Epc1292PowerApparent_Type=Integer32
_Epc1292PowerApparent_Object=MibTableColumn
epc1292PowerApparent=_Epc1292PowerApparent_Object((1,3,6,1,4,1,28507,50,1,5,1,2,1,10),_Epc1292PowerApparent_Type())
epc1292PowerApparent.setMaxAccess(_C)
if mibBuilder.loadTexts:epc1292PowerApparent.setStatus(_B)
if mibBuilder.loadTexts:epc1292PowerApparent.setUnits('VA')
_Epc1292PowerReactive_Type=Integer32
_Epc1292PowerReactive_Object=MibTableColumn
epc1292PowerReactive=_Epc1292PowerReactive_Object((1,3,6,1,4,1,28507,50,1,5,1,2,1,11),_Epc1292PowerReactive_Type())
epc1292PowerReactive.setMaxAccess(_C)
if mibBuilder.loadTexts:epc1292PowerReactive.setStatus(_B)
if mibBuilder.loadTexts:epc1292PowerReactive.setUnits('VAR')
_Epc1292AbsEnergyReactive_Type=Gauge32
_Epc1292AbsEnergyReactive_Object=MibTableColumn
epc1292AbsEnergyReactive=_Epc1292AbsEnergyReactive_Object((1,3,6,1,4,1,28507,50,1,5,1,2,1,12),_Epc1292AbsEnergyReactive_Type())
epc1292AbsEnergyReactive.setMaxAccess(_C)
if mibBuilder.loadTexts:epc1292AbsEnergyReactive.setStatus(_B)
if mibBuilder.loadTexts:epc1292AbsEnergyReactive.setUnits(_H)
_Epc1292AbsEnergyActiveResettable_Type=Gauge32
_Epc1292AbsEnergyActiveResettable_Object=MibTableColumn
epc1292AbsEnergyActiveResettable=_Epc1292AbsEnergyActiveResettable_Object((1,3,6,1,4,1,28507,50,1,5,1,2,1,13),_Epc1292AbsEnergyActiveResettable_Type())
epc1292AbsEnergyActiveResettable.setMaxAccess(_E)
if mibBuilder.loadTexts:epc1292AbsEnergyActiveResettable.setStatus(_B)
if mibBuilder.loadTexts:epc1292AbsEnergyActiveResettable.setUnits(_G)
_Epc1292AbsEnergyReactiveResettable_Type=Gauge32
_Epc1292AbsEnergyReactiveResettable_Object=MibTableColumn
epc1292AbsEnergyReactiveResettable=_Epc1292AbsEnergyReactiveResettable_Object((1,3,6,1,4,1,28507,50,1,5,1,2,1,14),_Epc1292AbsEnergyReactiveResettable_Type())
epc1292AbsEnergyReactiveResettable.setMaxAccess(_C)
if mibBuilder.loadTexts:epc1292AbsEnergyReactiveResettable.setStatus(_B)
if mibBuilder.loadTexts:epc1292AbsEnergyReactiveResettable.setUnits(_H)
_Epc1292ResetTime_Type=Gauge32
_Epc1292ResetTime_Object=MibTableColumn
epc1292ResetTime=_Epc1292ResetTime_Object((1,3,6,1,4,1,28507,50,1,5,1,2,1,15),_Epc1292ResetTime_Type())
epc1292ResetTime.setMaxAccess(_C)
if mibBuilder.loadTexts:epc1292ResetTime.setStatus(_B)
if mibBuilder.loadTexts:epc1292ResetTime.setUnits('s')
_Epc1292ForwEnergyActive_Type=Gauge32
_Epc1292ForwEnergyActive_Object=MibTableColumn
epc1292ForwEnergyActive=_Epc1292ForwEnergyActive_Object((1,3,6,1,4,1,28507,50,1,5,1,2,1,16),_Epc1292ForwEnergyActive_Type())
epc1292ForwEnergyActive.setMaxAccess(_C)
if mibBuilder.loadTexts:epc1292ForwEnergyActive.setStatus(_B)
if mibBuilder.loadTexts:epc1292ForwEnergyActive.setUnits(_G)
_Epc1292ForwEnergyReactive_Type=Gauge32
_Epc1292ForwEnergyReactive_Object=MibTableColumn
epc1292ForwEnergyReactive=_Epc1292ForwEnergyReactive_Object((1,3,6,1,4,1,28507,50,1,5,1,2,1,17),_Epc1292ForwEnergyReactive_Type())
epc1292ForwEnergyReactive.setMaxAccess(_C)
if mibBuilder.loadTexts:epc1292ForwEnergyReactive.setStatus(_B)
if mibBuilder.loadTexts:epc1292ForwEnergyReactive.setUnits(_H)
_Epc1292ForwEnergyActiveResettable_Type=Gauge32
_Epc1292ForwEnergyActiveResettable_Object=MibTableColumn
epc1292ForwEnergyActiveResettable=_Epc1292ForwEnergyActiveResettable_Object((1,3,6,1,4,1,28507,50,1,5,1,2,1,18),_Epc1292ForwEnergyActiveResettable_Type())
epc1292ForwEnergyActiveResettable.setMaxAccess(_C)
if mibBuilder.loadTexts:epc1292ForwEnergyActiveResettable.setStatus(_B)
if mibBuilder.loadTexts:epc1292ForwEnergyActiveResettable.setUnits(_G)
_Epc1292ForwEnergyReactiveResettable_Type=Gauge32
_Epc1292ForwEnergyReactiveResettable_Object=MibTableColumn
epc1292ForwEnergyReactiveResettable=_Epc1292ForwEnergyReactiveResettable_Object((1,3,6,1,4,1,28507,50,1,5,1,2,1,19),_Epc1292ForwEnergyReactiveResettable_Type())
epc1292ForwEnergyReactiveResettable.setMaxAccess(_C)
if mibBuilder.loadTexts:epc1292ForwEnergyReactiveResettable.setStatus(_B)
if mibBuilder.loadTexts:epc1292ForwEnergyReactiveResettable.setUnits(_H)
_Epc1292RevEnergyActive_Type=Gauge32
_Epc1292RevEnergyActive_Object=MibTableColumn
epc1292RevEnergyActive=_Epc1292RevEnergyActive_Object((1,3,6,1,4,1,28507,50,1,5,1,2,1,20),_Epc1292RevEnergyActive_Type())
epc1292RevEnergyActive.setMaxAccess(_C)
if mibBuilder.loadTexts:epc1292RevEnergyActive.setStatus(_B)
if mibBuilder.loadTexts:epc1292RevEnergyActive.setUnits(_G)
_Epc1292RevEnergyReactive_Type=Gauge32
_Epc1292RevEnergyReactive_Object=MibTableColumn
epc1292RevEnergyReactive=_Epc1292RevEnergyReactive_Object((1,3,6,1,4,1,28507,50,1,5,1,2,1,21),_Epc1292RevEnergyReactive_Type())
epc1292RevEnergyReactive.setMaxAccess(_C)
if mibBuilder.loadTexts:epc1292RevEnergyReactive.setStatus(_B)
if mibBuilder.loadTexts:epc1292RevEnergyReactive.setUnits(_H)
_Epc1292RevEnergyActiveResettable_Type=Gauge32
_Epc1292RevEnergyActiveResettable_Object=MibTableColumn
epc1292RevEnergyActiveResettable=_Epc1292RevEnergyActiveResettable_Object((1,3,6,1,4,1,28507,50,1,5,1,2,1,22),_Epc1292RevEnergyActiveResettable_Type())
epc1292RevEnergyActiveResettable.setMaxAccess(_C)
if mibBuilder.loadTexts:epc1292RevEnergyActiveResettable.setStatus(_B)
if mibBuilder.loadTexts:epc1292RevEnergyActiveResettable.setUnits(_G)
_Epc1292RevEnergyReactiveResettable_Type=Gauge32
_Epc1292RevEnergyReactiveResettable_Object=MibTableColumn
epc1292RevEnergyReactiveResettable=_Epc1292RevEnergyReactiveResettable_Object((1,3,6,1,4,1,28507,50,1,5,1,2,1,23),_Epc1292RevEnergyReactiveResettable_Type())
epc1292RevEnergyReactiveResettable.setMaxAccess(_C)
if mibBuilder.loadTexts:epc1292RevEnergyReactiveResettable.setStatus(_B)
if mibBuilder.loadTexts:epc1292RevEnergyReactiveResettable.setUnits(_H)
_Epc1292OVPTable_Object=MibTable
epc1292OVPTable=_Epc1292OVPTable_Object((1,3,6,1,4,1,28507,50,1,5,2))
if mibBuilder.loadTexts:epc1292OVPTable.setStatus(_B)
_Epc1292OVPEntry_Object=MibTableRow
epc1292OVPEntry=_Epc1292OVPEntry_Object((1,3,6,1,4,1,28507,50,1,5,2,1))
epc1292OVPEntry.setIndexNames((0,_A,_N))
if mibBuilder.loadTexts:epc1292OVPEntry.setStatus(_B)
class _Epc1292OVPIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1))
_Epc1292OVPIndex_Type.__name__=_D
_Epc1292OVPIndex_Object=MibTableColumn
epc1292OVPIndex=_Epc1292OVPIndex_Object((1,3,6,1,4,1,28507,50,1,5,2,1,1),_Epc1292OVPIndex_Type())
epc1292OVPIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:epc1292OVPIndex.setStatus(_B)
class _Epc1292OVPStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('failure',0),('ok',1),('unknown',2)))
_Epc1292OVPStatus_Type.__name__=_D
_Epc1292OVPStatus_Object=MibTableColumn
epc1292OVPStatus=_Epc1292OVPStatus_Object((1,3,6,1,4,1,28507,50,1,5,2,1,2),_Epc1292OVPStatus_Type())
epc1292OVPStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:epc1292OVPStatus.setStatus(_B)
_Epc1292ExtSensors_ObjectIdentity=ObjectIdentity
epc1292ExtSensors=_Epc1292ExtSensors_ObjectIdentity((1,3,6,1,4,1,28507,50,1,6))
_Epc1292SensorTable_Object=MibTable
epc1292SensorTable=_Epc1292SensorTable_Object((1,3,6,1,4,1,28507,50,1,6,1))
if mibBuilder.loadTexts:epc1292SensorTable.setStatus(_B)
_Epc1292SensorEntry_Object=MibTableRow
epc1292SensorEntry=_Epc1292SensorEntry_Object((1,3,6,1,4,1,28507,50,1,6,1,1))
epc1292SensorEntry.setIndexNames((0,_A,_F))
if mibBuilder.loadTexts:epc1292SensorEntry.setStatus(_B)
class _Epc1292SensorIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1))
_Epc1292SensorIndex_Type.__name__=_D
_Epc1292SensorIndex_Object=MibTableColumn
epc1292SensorIndex=_Epc1292SensorIndex_Object((1,3,6,1,4,1,28507,50,1,6,1,1,1),_Epc1292SensorIndex_Type())
epc1292SensorIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:epc1292SensorIndex.setStatus(_B)
_Epc1292TempSensor_Type=Integer32
_Epc1292TempSensor_Object=MibTableColumn
epc1292TempSensor=_Epc1292TempSensor_Object((1,3,6,1,4,1,28507,50,1,6,1,1,2),_Epc1292TempSensor_Type())
epc1292TempSensor.setMaxAccess(_C)
if mibBuilder.loadTexts:epc1292TempSensor.setStatus(_B)
if mibBuilder.loadTexts:epc1292TempSensor.setUnits(_O)
_Epc1292HygroSensor_Type=Integer32
_Epc1292HygroSensor_Object=MibTableColumn
epc1292HygroSensor=_Epc1292HygroSensor_Object((1,3,6,1,4,1,28507,50,1,6,1,1,3),_Epc1292HygroSensor_Type())
epc1292HygroSensor.setMaxAccess(_C)
if mibBuilder.loadTexts:epc1292HygroSensor.setStatus(_B)
if mibBuilder.loadTexts:epc1292HygroSensor.setUnits('0.1 percent humidity')
class _Epc1292InputSensor_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_M,0),('on',1)))
_Epc1292InputSensor_Type.__name__=_D
_Epc1292InputSensor_Object=MibTableColumn
epc1292InputSensor=_Epc1292InputSensor_Object((1,3,6,1,4,1,28507,50,1,6,1,1,4),_Epc1292InputSensor_Type())
epc1292InputSensor.setMaxAccess(_C)
if mibBuilder.loadTexts:epc1292InputSensor.setStatus(_B)
_Epc1292AirPressure_Type=Integer32
_Epc1292AirPressure_Object=MibTableColumn
epc1292AirPressure=_Epc1292AirPressure_Object((1,3,6,1,4,1,28507,50,1,6,1,1,5),_Epc1292AirPressure_Type())
epc1292AirPressure.setMaxAccess(_C)
if mibBuilder.loadTexts:epc1292AirPressure.setStatus(_B)
if mibBuilder.loadTexts:epc1292AirPressure.setUnits('1 hPA (hectopascal) ~ 1 milibar')
_Epc1292DewPoint_Type=Integer32
_Epc1292DewPoint_Object=MibTableColumn
epc1292DewPoint=_Epc1292DewPoint_Object((1,3,6,1,4,1,28507,50,1,6,1,1,6),_Epc1292DewPoint_Type())
epc1292DewPoint.setMaxAccess(_C)
if mibBuilder.loadTexts:epc1292DewPoint.setStatus(_B)
if mibBuilder.loadTexts:epc1292DewPoint.setUnits(_O)
_Epc1292DewPointDiff_Type=Integer32
_Epc1292DewPointDiff_Object=MibTableColumn
epc1292DewPointDiff=_Epc1292DewPointDiff_Object((1,3,6,1,4,1,28507,50,1,6,1,1,7),_Epc1292DewPointDiff_Type())
epc1292DewPointDiff.setMaxAccess(_C)
if mibBuilder.loadTexts:epc1292DewPointDiff.setStatus(_B)
if mibBuilder.loadTexts:epc1292DewPointDiff.setUnits(_O)
_Epc1292Conf_ObjectIdentity=ObjectIdentity
epc1292Conf=_Epc1292Conf_ObjectIdentity((1,3,6,1,4,1,28507,50,2))
_Epc1292Groups_ObjectIdentity=ObjectIdentity
epc1292Groups=_Epc1292Groups_ObjectIdentity((1,3,6,1,4,1,28507,50,2,1))
_Epc1292Compls_ObjectIdentity=ObjectIdentity
epc1292Compls=_Epc1292Compls_ObjectIdentity((1,3,6,1,4,1,28507,50,2,2))
_Events_ObjectIdentity=ObjectIdentity
events=_Events_ObjectIdentity((1,3,6,1,4,1,28507,50,3))
epc1292BasicGroup=ObjectGroup((1,3,6,1,4,1,28507,50,2,1,1))
epc1292BasicGroup.setObjects(*((_A,_g),(_A,_L),(_A,_h),(_A,_i),(_A,_I),(_A,_P),(_A,_Q),(_A,_R),(_A,_j),(_A,_k),(_A,_l),(_A,_m),(_A,_J),(_A,_n),(_A,_o),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_p),(_A,_q),(_A,_W),(_A,_X),(_A,_r),(_A,_s),(_A,_t),(_A,_u),(_A,_v),(_A,_w),(_A,_x),(_A,_y),(_A,_z),(_A,_A0),(_A,_A1),(_A,_A2),(_A,_N),(_A,_Y),(_A,_F),(_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_A3),(_A,_d)))
if mibBuilder.loadTexts:epc1292BasicGroup.setStatus(_B)
epc1292SwitchEvtPort=NotificationType((1,3,6,1,4,1,28507,50,3,1))
epc1292SwitchEvtPort.setObjects(*((_A,_I),(_A,_P),(_A,_Q),(_A,_R)))
if mibBuilder.loadTexts:epc1292SwitchEvtPort.setStatus(_B)
epc1292TempEvtSen=NotificationType((1,3,6,1,4,1,28507,50,3,2))
epc1292TempEvtSen.setObjects(*((_A,_F),(_A,_Z)))
if mibBuilder.loadTexts:epc1292TempEvtSen.setStatus(_B)
epc1292HygroEvtSen=NotificationType((1,3,6,1,4,1,28507,50,3,3))
epc1292HygroEvtSen.setObjects(*((_A,_F),(_A,_a)))
if mibBuilder.loadTexts:epc1292HygroEvtSen.setStatus(_B)
epc1292InputEvtSen=NotificationType((1,3,6,1,4,1,28507,50,3,4))
epc1292InputEvtSen.setObjects(*((_A,_F),(_A,_b)))
if mibBuilder.loadTexts:epc1292InputEvtSen.setStatus(_B)
epc1292AirPressureEvtSen=NotificationType((1,3,6,1,4,1,28507,50,3,5))
epc1292AirPressureEvtSen.setObjects(*((_A,_F),(_A,_c)))
if mibBuilder.loadTexts:epc1292AirPressureEvtSen.setStatus(_B)
epc1292DewPtDiffEvtSen=NotificationType((1,3,6,1,4,1,28507,50,3,6))
epc1292DewPtDiffEvtSen.setObjects(*((_A,_F),(_A,_d)))
if mibBuilder.loadTexts:epc1292DewPtDiffEvtSen.setStatus(_B)
epc1292OVPEvt=NotificationType((1,3,6,1,4,1,28507,50,3,7))
epc1292OVPEvt.setObjects((_A,_Y))
if mibBuilder.loadTexts:epc1292OVPEvt.setStatus(_B)
epc1292LineAmperageEvt=NotificationType((1,3,6,1,4,1,28507,50,3,8))
epc1292LineAmperageEvt.setObjects(*((_A,_J),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X)))
if mibBuilder.loadTexts:epc1292LineAmperageEvt.setStatus(_B)
epc1292NotificationGroup=NotificationGroup((1,3,6,1,4,1,28507,50,2,1,2))
epc1292NotificationGroup.setObjects(*((_A,_A4),(_A,_A5),(_A,_A6),(_A,_A7),(_A,_A8),(_A,_A9),(_A,_AA),(_A,_AB)))
if mibBuilder.loadTexts:epc1292NotificationGroup.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'gudeads':gudeads,'gadsEPC1292':gadsEPC1292,'epc1292Objects':epc1292Objects,'epc1292CommonConfig':epc1292CommonConfig,'epc1292SNMPaccess':epc1292SNMPaccess,_g:epc1292TrapCtrl,'epc1292TrapIPTable':epc1292TrapIPTable,'epc1292TrapIPEntry':epc1292TrapIPEntry,_L:epc1292TrapIPIndex,_h:epc1292TrapAddr,'epc1292DeviceConfig':epc1292DeviceConfig,'epc1292IntActors':epc1292IntActors,'epc1292relayports':epc1292relayports,_i:epc1292portNumber,'epc1292portTable':epc1292portTable,'epc1292portEntry':epc1292portEntry,_I:epc1292PortIndex,_P:epc1292PortName,_Q:epc1292PortState,_R:epc1292PortSwitchCount,_j:epc1292PortStartupMode,_k:epc1292PortStartupDelay,_l:epc1292PortRepowerTime,'epc1292ExtActors':epc1292ExtActors,'epc1292IntSensors':epc1292IntSensors,'epc1292PowerChan':epc1292PowerChan,_m:epc1292ActivePowerChan,'epc1292PowerTable':epc1292PowerTable,'epc1292PowerEntry':epc1292PowerEntry,_J:epc1292PowerIndex,_n:epc1292ChanStatus,_o:epc1292AbsEnergyActive,_S:epc1292PowerActive,_T:epc1292Current,_U:epc1292Voltage,_V:epc1292Frequency,_p:epc1292PowerFactor,_q:epc1292Pangle,_W:epc1292PowerApparent,_X:epc1292PowerReactive,_r:epc1292AbsEnergyReactive,_s:epc1292AbsEnergyActiveResettable,_t:epc1292AbsEnergyReactiveResettable,_u:epc1292ResetTime,_v:epc1292ForwEnergyActive,_w:epc1292ForwEnergyReactive,_x:epc1292ForwEnergyActiveResettable,_y:epc1292ForwEnergyReactiveResettable,_z:epc1292RevEnergyActive,_A0:epc1292RevEnergyReactive,_A1:epc1292RevEnergyActiveResettable,_A2:epc1292RevEnergyReactiveResettable,'epc1292OVPTable':epc1292OVPTable,'epc1292OVPEntry':epc1292OVPEntry,_N:epc1292OVPIndex,_Y:epc1292OVPStatus,'epc1292ExtSensors':epc1292ExtSensors,'epc1292SensorTable':epc1292SensorTable,'epc1292SensorEntry':epc1292SensorEntry,_F:epc1292SensorIndex,_Z:epc1292TempSensor,_a:epc1292HygroSensor,_b:epc1292InputSensor,_c:epc1292AirPressure,_A3:epc1292DewPoint,_d:epc1292DewPointDiff,'epc1292Conf':epc1292Conf,'epc1292Groups':epc1292Groups,'epc1292BasicGroup':epc1292BasicGroup,'epc1292NotificationGroup':epc1292NotificationGroup,'epc1292Compls':epc1292Compls,'events':events,_A4:epc1292SwitchEvtPort,_A5:epc1292TempEvtSen,_AB:epc1292HygroEvtSen,_A6:epc1292InputEvtSen,_A7:epc1292AirPressureEvtSen,_A8:epc1292DewPtDiffEvtSen,_A9:epc1292OVPEvt,_AA:epc1292LineAmperageEvt})