_A8='ets8801DewPtDiffEvtSen'
_A7='ets8801AirPressureEvtSen'
_A6='ets8801InputEvtSen'
_A5='ets8801HygroEvtSen'
_A4='ets8801TempEvtSen'
_A3='ets8801LineAmperageEvt'
_A2='ets8801PowerSelectEvt'
_A1='ets8801SecondaryPowerChangeEvt'
_A0='ets8801PrimaryPowerChangeEvt'
_z='ets8801DewPoint'
_y='ets8801LineSelectRequest'
_x='ets8801ResidualCurrent'
_w='ets8801RevEnergyReactiveResettable'
_v='ets8801RevEnergyActiveResettable'
_u='ets8801RevEnergyReactive'
_t='ets8801RevEnergyActive'
_s='ets8801ForwEnergyReactiveResettable'
_r='ets8801ForwEnergyActiveResettable'
_q='ets8801ForwEnergyReactive'
_p='ets8801ForwEnergyActive'
_o='ets8801ResetTime'
_n='ets8801AbsEnergyReactiveResettable'
_m='ets8801AbsEnergyActiveResettable'
_l='ets8801AbsEnergyReactive'
_k='ets8801Pangle'
_j='ets8801PowerFactor'
_i='ets8801AbsEnergyActive'
_h='ets8801ChanStatus'
_g='ets8801ActivePowerChan'
_f='ets8801Buzzer'
_e='ets8801TrapAddr'
_d='ets8801TrapCtrl'
_c='secondary'
_b='primary'
_a='Unsigned32'
_Z='OctetString'
_Y='ets8801DewPointDiff'
_X='ets8801AirPressure'
_W='ets8801InputSensor'
_V='ets8801HygroSensor'
_U='ets8801TempSensor'
_T='ets8801PowerLineSelected'
_S='ets8801PowerReactive'
_R='ets8801PowerApparent'
_Q='ets8801Frequency'
_P='ets8801Voltage'
_O='ets8801Current'
_N='ets8801PowerActive'
_M='0.1 degree Celsius'
_L='ets8801TrapIPIndex'
_K='ets8801SecondaryPowerAvail'
_J='ets8801PrimaryPowerAvail'
_I='ets8801PowerIndex'
_H='read-write'
_G='VARh'
_F='Wh'
_E='ets8801SensorIndex'
_D='Integer32'
_C='read-only'
_B='current'
_A='GUDEADS-ETS8801-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_Z,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_a,'enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
gudeads=ModuleIdentity((1,3,6,1,4,1,28507))
if mibBuilder.loadTexts:gudeads.setRevisions(('2007-05-23 12:44',))
_GadsETS8801_ObjectIdentity=ObjectIdentity
gadsETS8801=_GadsETS8801_ObjectIdentity((1,3,6,1,4,1,28507,41))
_Ets8801Objects_ObjectIdentity=ObjectIdentity
ets8801Objects=_Ets8801Objects_ObjectIdentity((1,3,6,1,4,1,28507,41,1))
_Ets8801CommonConfig_ObjectIdentity=ObjectIdentity
ets8801CommonConfig=_Ets8801CommonConfig_ObjectIdentity((1,3,6,1,4,1,28507,41,1,1))
_Ets8801SNMPaccess_ObjectIdentity=ObjectIdentity
ets8801SNMPaccess=_Ets8801SNMPaccess_ObjectIdentity((1,3,6,1,4,1,28507,41,1,1,1))
class _Ets8801TrapCtrl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3))
_Ets8801TrapCtrl_Type.__name__=_D
_Ets8801TrapCtrl_Object=MibScalar
ets8801TrapCtrl=_Ets8801TrapCtrl_Object((1,3,6,1,4,1,28507,41,1,1,1,1),_Ets8801TrapCtrl_Type())
ets8801TrapCtrl.setMaxAccess(_H)
if mibBuilder.loadTexts:ets8801TrapCtrl.setStatus(_B)
_Ets8801TrapIPTable_Object=MibTable
ets8801TrapIPTable=_Ets8801TrapIPTable_Object((1,3,6,1,4,1,28507,41,1,1,1,2))
if mibBuilder.loadTexts:ets8801TrapIPTable.setStatus(_B)
_Ets8801TrapIPEntry_Object=MibTableRow
ets8801TrapIPEntry=_Ets8801TrapIPEntry_Object((1,3,6,1,4,1,28507,41,1,1,1,2,1))
ets8801TrapIPEntry.setIndexNames((0,_A,_L))
if mibBuilder.loadTexts:ets8801TrapIPEntry.setStatus(_B)
class _Ets8801TrapIPIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_Ets8801TrapIPIndex_Type.__name__=_D
_Ets8801TrapIPIndex_Object=MibTableColumn
ets8801TrapIPIndex=_Ets8801TrapIPIndex_Object((1,3,6,1,4,1,28507,41,1,1,1,2,1,1),_Ets8801TrapIPIndex_Type())
ets8801TrapIPIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:ets8801TrapIPIndex.setStatus(_B)
class _Ets8801TrapAddr_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,99))
_Ets8801TrapAddr_Type.__name__=_Z
_Ets8801TrapAddr_Object=MibTableColumn
ets8801TrapAddr=_Ets8801TrapAddr_Object((1,3,6,1,4,1,28507,41,1,1,1,2,1,2),_Ets8801TrapAddr_Type())
ets8801TrapAddr.setMaxAccess(_H)
if mibBuilder.loadTexts:ets8801TrapAddr.setStatus(_B)
_Ets8801IntActors_ObjectIdentity=ObjectIdentity
ets8801IntActors=_Ets8801IntActors_ObjectIdentity((1,3,6,1,4,1,28507,41,1,3))
class _Ets8801Buzzer_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Ets8801Buzzer_Type.__name__=_D
_Ets8801Buzzer_Object=MibScalar
ets8801Buzzer=_Ets8801Buzzer_Object((1,3,6,1,4,1,28507,41,1,3,10),_Ets8801Buzzer_Type())
ets8801Buzzer.setMaxAccess(_H)
if mibBuilder.loadTexts:ets8801Buzzer.setStatus(_B)
if mibBuilder.loadTexts:ets8801Buzzer.setUnits('0 = Off, 1 = On')
_Ets8801IntSensors_ObjectIdentity=ObjectIdentity
ets8801IntSensors=_Ets8801IntSensors_ObjectIdentity((1,3,6,1,4,1,28507,41,1,5))
_Ets8801PowerChan_ObjectIdentity=ObjectIdentity
ets8801PowerChan=_Ets8801PowerChan_ObjectIdentity((1,3,6,1,4,1,28507,41,1,5,1))
class _Ets8801ActivePowerChan_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1))
_Ets8801ActivePowerChan_Type.__name__=_a
_Ets8801ActivePowerChan_Object=MibScalar
ets8801ActivePowerChan=_Ets8801ActivePowerChan_Object((1,3,6,1,4,1,28507,41,1,5,1,1),_Ets8801ActivePowerChan_Type())
ets8801ActivePowerChan.setMaxAccess(_C)
if mibBuilder.loadTexts:ets8801ActivePowerChan.setStatus(_B)
_Ets8801PowerTable_Object=MibTable
ets8801PowerTable=_Ets8801PowerTable_Object((1,3,6,1,4,1,28507,41,1,5,1,2))
if mibBuilder.loadTexts:ets8801PowerTable.setStatus(_B)
_Ets8801PowerEntry_Object=MibTableRow
ets8801PowerEntry=_Ets8801PowerEntry_Object((1,3,6,1,4,1,28507,41,1,5,1,2,1))
ets8801PowerEntry.setIndexNames((0,_A,_I))
if mibBuilder.loadTexts:ets8801PowerEntry.setStatus(_B)
class _Ets8801PowerIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1))
_Ets8801PowerIndex_Type.__name__=_D
_Ets8801PowerIndex_Object=MibTableColumn
ets8801PowerIndex=_Ets8801PowerIndex_Object((1,3,6,1,4,1,28507,41,1,5,1,2,1,1),_Ets8801PowerIndex_Type())
ets8801PowerIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:ets8801PowerIndex.setStatus(_B)
class _Ets8801ChanStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Ets8801ChanStatus_Type.__name__=_D
_Ets8801ChanStatus_Object=MibTableColumn
ets8801ChanStatus=_Ets8801ChanStatus_Object((1,3,6,1,4,1,28507,41,1,5,1,2,1,2),_Ets8801ChanStatus_Type())
ets8801ChanStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ets8801ChanStatus.setStatus(_B)
_Ets8801AbsEnergyActive_Type=Unsigned32
_Ets8801AbsEnergyActive_Object=MibTableColumn
ets8801AbsEnergyActive=_Ets8801AbsEnergyActive_Object((1,3,6,1,4,1,28507,41,1,5,1,2,1,3),_Ets8801AbsEnergyActive_Type())
ets8801AbsEnergyActive.setMaxAccess(_C)
if mibBuilder.loadTexts:ets8801AbsEnergyActive.setStatus(_B)
if mibBuilder.loadTexts:ets8801AbsEnergyActive.setUnits(_F)
_Ets8801PowerActive_Type=Integer32
_Ets8801PowerActive_Object=MibTableColumn
ets8801PowerActive=_Ets8801PowerActive_Object((1,3,6,1,4,1,28507,41,1,5,1,2,1,4),_Ets8801PowerActive_Type())
ets8801PowerActive.setMaxAccess(_C)
if mibBuilder.loadTexts:ets8801PowerActive.setStatus(_B)
if mibBuilder.loadTexts:ets8801PowerActive.setUnits('W')
_Ets8801Current_Type=Unsigned32
_Ets8801Current_Object=MibTableColumn
ets8801Current=_Ets8801Current_Object((1,3,6,1,4,1,28507,41,1,5,1,2,1,5),_Ets8801Current_Type())
ets8801Current.setMaxAccess(_C)
if mibBuilder.loadTexts:ets8801Current.setStatus(_B)
if mibBuilder.loadTexts:ets8801Current.setUnits('mA')
_Ets8801Voltage_Type=Unsigned32
_Ets8801Voltage_Object=MibTableColumn
ets8801Voltage=_Ets8801Voltage_Object((1,3,6,1,4,1,28507,41,1,5,1,2,1,6),_Ets8801Voltage_Type())
ets8801Voltage.setMaxAccess(_C)
if mibBuilder.loadTexts:ets8801Voltage.setStatus(_B)
if mibBuilder.loadTexts:ets8801Voltage.setUnits('V')
_Ets8801Frequency_Type=Unsigned32
_Ets8801Frequency_Object=MibTableColumn
ets8801Frequency=_Ets8801Frequency_Object((1,3,6,1,4,1,28507,41,1,5,1,2,1,7),_Ets8801Frequency_Type())
ets8801Frequency.setMaxAccess(_C)
if mibBuilder.loadTexts:ets8801Frequency.setStatus(_B)
if mibBuilder.loadTexts:ets8801Frequency.setUnits('0.01 hz')
_Ets8801PowerFactor_Type=Integer32
_Ets8801PowerFactor_Object=MibTableColumn
ets8801PowerFactor=_Ets8801PowerFactor_Object((1,3,6,1,4,1,28507,41,1,5,1,2,1,8),_Ets8801PowerFactor_Type())
ets8801PowerFactor.setMaxAccess(_C)
if mibBuilder.loadTexts:ets8801PowerFactor.setStatus(_B)
if mibBuilder.loadTexts:ets8801PowerFactor.setUnits('0.001')
_Ets8801Pangle_Type=Integer32
_Ets8801Pangle_Object=MibTableColumn
ets8801Pangle=_Ets8801Pangle_Object((1,3,6,1,4,1,28507,41,1,5,1,2,1,9),_Ets8801Pangle_Type())
ets8801Pangle.setMaxAccess(_C)
if mibBuilder.loadTexts:ets8801Pangle.setStatus(_B)
if mibBuilder.loadTexts:ets8801Pangle.setUnits('0.1 degree')
_Ets8801PowerApparent_Type=Integer32
_Ets8801PowerApparent_Object=MibTableColumn
ets8801PowerApparent=_Ets8801PowerApparent_Object((1,3,6,1,4,1,28507,41,1,5,1,2,1,10),_Ets8801PowerApparent_Type())
ets8801PowerApparent.setMaxAccess(_C)
if mibBuilder.loadTexts:ets8801PowerApparent.setStatus(_B)
if mibBuilder.loadTexts:ets8801PowerApparent.setUnits('VA')
_Ets8801PowerReactive_Type=Integer32
_Ets8801PowerReactive_Object=MibTableColumn
ets8801PowerReactive=_Ets8801PowerReactive_Object((1,3,6,1,4,1,28507,41,1,5,1,2,1,11),_Ets8801PowerReactive_Type())
ets8801PowerReactive.setMaxAccess(_C)
if mibBuilder.loadTexts:ets8801PowerReactive.setStatus(_B)
if mibBuilder.loadTexts:ets8801PowerReactive.setUnits('VAR')
_Ets8801AbsEnergyReactive_Type=Unsigned32
_Ets8801AbsEnergyReactive_Object=MibTableColumn
ets8801AbsEnergyReactive=_Ets8801AbsEnergyReactive_Object((1,3,6,1,4,1,28507,41,1,5,1,2,1,12),_Ets8801AbsEnergyReactive_Type())
ets8801AbsEnergyReactive.setMaxAccess(_C)
if mibBuilder.loadTexts:ets8801AbsEnergyReactive.setStatus(_B)
if mibBuilder.loadTexts:ets8801AbsEnergyReactive.setUnits(_G)
_Ets8801AbsEnergyActiveResettable_Type=Unsigned32
_Ets8801AbsEnergyActiveResettable_Object=MibTableColumn
ets8801AbsEnergyActiveResettable=_Ets8801AbsEnergyActiveResettable_Object((1,3,6,1,4,1,28507,41,1,5,1,2,1,13),_Ets8801AbsEnergyActiveResettable_Type())
ets8801AbsEnergyActiveResettable.setMaxAccess(_H)
if mibBuilder.loadTexts:ets8801AbsEnergyActiveResettable.setStatus(_B)
if mibBuilder.loadTexts:ets8801AbsEnergyActiveResettable.setUnits(_F)
_Ets8801AbsEnergyReactiveResettable_Type=Unsigned32
_Ets8801AbsEnergyReactiveResettable_Object=MibTableColumn
ets8801AbsEnergyReactiveResettable=_Ets8801AbsEnergyReactiveResettable_Object((1,3,6,1,4,1,28507,41,1,5,1,2,1,14),_Ets8801AbsEnergyReactiveResettable_Type())
ets8801AbsEnergyReactiveResettable.setMaxAccess(_C)
if mibBuilder.loadTexts:ets8801AbsEnergyReactiveResettable.setStatus(_B)
if mibBuilder.loadTexts:ets8801AbsEnergyReactiveResettable.setUnits(_G)
_Ets8801ResetTime_Type=Unsigned32
_Ets8801ResetTime_Object=MibTableColumn
ets8801ResetTime=_Ets8801ResetTime_Object((1,3,6,1,4,1,28507,41,1,5,1,2,1,15),_Ets8801ResetTime_Type())
ets8801ResetTime.setMaxAccess(_C)
if mibBuilder.loadTexts:ets8801ResetTime.setStatus(_B)
if mibBuilder.loadTexts:ets8801ResetTime.setUnits('s')
_Ets8801ForwEnergyActive_Type=Unsigned32
_Ets8801ForwEnergyActive_Object=MibTableColumn
ets8801ForwEnergyActive=_Ets8801ForwEnergyActive_Object((1,3,6,1,4,1,28507,41,1,5,1,2,1,16),_Ets8801ForwEnergyActive_Type())
ets8801ForwEnergyActive.setMaxAccess(_C)
if mibBuilder.loadTexts:ets8801ForwEnergyActive.setStatus(_B)
if mibBuilder.loadTexts:ets8801ForwEnergyActive.setUnits(_F)
_Ets8801ForwEnergyReactive_Type=Unsigned32
_Ets8801ForwEnergyReactive_Object=MibTableColumn
ets8801ForwEnergyReactive=_Ets8801ForwEnergyReactive_Object((1,3,6,1,4,1,28507,41,1,5,1,2,1,17),_Ets8801ForwEnergyReactive_Type())
ets8801ForwEnergyReactive.setMaxAccess(_C)
if mibBuilder.loadTexts:ets8801ForwEnergyReactive.setStatus(_B)
if mibBuilder.loadTexts:ets8801ForwEnergyReactive.setUnits(_G)
_Ets8801ForwEnergyActiveResettable_Type=Unsigned32
_Ets8801ForwEnergyActiveResettable_Object=MibTableColumn
ets8801ForwEnergyActiveResettable=_Ets8801ForwEnergyActiveResettable_Object((1,3,6,1,4,1,28507,41,1,5,1,2,1,18),_Ets8801ForwEnergyActiveResettable_Type())
ets8801ForwEnergyActiveResettable.setMaxAccess(_C)
if mibBuilder.loadTexts:ets8801ForwEnergyActiveResettable.setStatus(_B)
if mibBuilder.loadTexts:ets8801ForwEnergyActiveResettable.setUnits(_F)
_Ets8801ForwEnergyReactiveResettable_Type=Unsigned32
_Ets8801ForwEnergyReactiveResettable_Object=MibTableColumn
ets8801ForwEnergyReactiveResettable=_Ets8801ForwEnergyReactiveResettable_Object((1,3,6,1,4,1,28507,41,1,5,1,2,1,19),_Ets8801ForwEnergyReactiveResettable_Type())
ets8801ForwEnergyReactiveResettable.setMaxAccess(_C)
if mibBuilder.loadTexts:ets8801ForwEnergyReactiveResettable.setStatus(_B)
if mibBuilder.loadTexts:ets8801ForwEnergyReactiveResettable.setUnits(_G)
_Ets8801RevEnergyActive_Type=Unsigned32
_Ets8801RevEnergyActive_Object=MibTableColumn
ets8801RevEnergyActive=_Ets8801RevEnergyActive_Object((1,3,6,1,4,1,28507,41,1,5,1,2,1,20),_Ets8801RevEnergyActive_Type())
ets8801RevEnergyActive.setMaxAccess(_C)
if mibBuilder.loadTexts:ets8801RevEnergyActive.setStatus(_B)
if mibBuilder.loadTexts:ets8801RevEnergyActive.setUnits(_F)
_Ets8801RevEnergyReactive_Type=Unsigned32
_Ets8801RevEnergyReactive_Object=MibTableColumn
ets8801RevEnergyReactive=_Ets8801RevEnergyReactive_Object((1,3,6,1,4,1,28507,41,1,5,1,2,1,21),_Ets8801RevEnergyReactive_Type())
ets8801RevEnergyReactive.setMaxAccess(_C)
if mibBuilder.loadTexts:ets8801RevEnergyReactive.setStatus(_B)
if mibBuilder.loadTexts:ets8801RevEnergyReactive.setUnits(_G)
_Ets8801RevEnergyActiveResettable_Type=Unsigned32
_Ets8801RevEnergyActiveResettable_Object=MibTableColumn
ets8801RevEnergyActiveResettable=_Ets8801RevEnergyActiveResettable_Object((1,3,6,1,4,1,28507,41,1,5,1,2,1,22),_Ets8801RevEnergyActiveResettable_Type())
ets8801RevEnergyActiveResettable.setMaxAccess(_C)
if mibBuilder.loadTexts:ets8801RevEnergyActiveResettable.setStatus(_B)
if mibBuilder.loadTexts:ets8801RevEnergyActiveResettable.setUnits(_F)
_Ets8801RevEnergyReactiveResettable_Type=Unsigned32
_Ets8801RevEnergyReactiveResettable_Object=MibTableColumn
ets8801RevEnergyReactiveResettable=_Ets8801RevEnergyReactiveResettable_Object((1,3,6,1,4,1,28507,41,1,5,1,2,1,23),_Ets8801RevEnergyReactiveResettable_Type())
ets8801RevEnergyReactiveResettable.setMaxAccess(_C)
if mibBuilder.loadTexts:ets8801RevEnergyReactiveResettable.setStatus(_B)
if mibBuilder.loadTexts:ets8801RevEnergyReactiveResettable.setUnits(_G)
_Ets8801ResidualCurrent_Type=Unsigned32
_Ets8801ResidualCurrent_Object=MibTableColumn
ets8801ResidualCurrent=_Ets8801ResidualCurrent_Object((1,3,6,1,4,1,28507,41,1,5,1,2,1,24),_Ets8801ResidualCurrent_Type())
ets8801ResidualCurrent.setMaxAccess(_C)
if mibBuilder.loadTexts:ets8801ResidualCurrent.setStatus(_B)
if mibBuilder.loadTexts:ets8801ResidualCurrent.setUnits('mA')
_Ets8801ETSPowerInfo_ObjectIdentity=ObjectIdentity
ets8801ETSPowerInfo=_Ets8801ETSPowerInfo_ObjectIdentity((1,3,6,1,4,1,28507,41,1,5,11))
class _Ets8801PrimaryPowerAvail_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('void',0),('power',1)))
_Ets8801PrimaryPowerAvail_Type.__name__=_D
_Ets8801PrimaryPowerAvail_Object=MibScalar
ets8801PrimaryPowerAvail=_Ets8801PrimaryPowerAvail_Object((1,3,6,1,4,1,28507,41,1,5,11,1),_Ets8801PrimaryPowerAvail_Type())
ets8801PrimaryPowerAvail.setMaxAccess(_C)
if mibBuilder.loadTexts:ets8801PrimaryPowerAvail.setStatus(_B)
class _Ets8801SecondaryPowerAvail_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('void',0),('power',1)))
_Ets8801SecondaryPowerAvail_Type.__name__=_D
_Ets8801SecondaryPowerAvail_Object=MibScalar
ets8801SecondaryPowerAvail=_Ets8801SecondaryPowerAvail_Object((1,3,6,1,4,1,28507,41,1,5,11,2),_Ets8801SecondaryPowerAvail_Type())
ets8801SecondaryPowerAvail.setMaxAccess(_C)
if mibBuilder.loadTexts:ets8801SecondaryPowerAvail.setStatus(_B)
class _Ets8801LineSelectRequest_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('norequest',0),(_b,1),(_c,2)))
_Ets8801LineSelectRequest_Type.__name__=_D
_Ets8801LineSelectRequest_Object=MibScalar
ets8801LineSelectRequest=_Ets8801LineSelectRequest_Object((1,3,6,1,4,1,28507,41,1,5,11,3),_Ets8801LineSelectRequest_Type())
ets8801LineSelectRequest.setMaxAccess(_H)
if mibBuilder.loadTexts:ets8801LineSelectRequest.setStatus(_B)
class _Ets8801PowerLineSelected_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_b,1),(_c,2)))
_Ets8801PowerLineSelected_Type.__name__=_D
_Ets8801PowerLineSelected_Object=MibScalar
ets8801PowerLineSelected=_Ets8801PowerLineSelected_Object((1,3,6,1,4,1,28507,41,1,5,11,4),_Ets8801PowerLineSelected_Type())
ets8801PowerLineSelected.setMaxAccess(_C)
if mibBuilder.loadTexts:ets8801PowerLineSelected.setStatus(_B)
_Ets8801ExtSensors_ObjectIdentity=ObjectIdentity
ets8801ExtSensors=_Ets8801ExtSensors_ObjectIdentity((1,3,6,1,4,1,28507,41,1,6))
_Ets8801SensorTable_Object=MibTable
ets8801SensorTable=_Ets8801SensorTable_Object((1,3,6,1,4,1,28507,41,1,6,1))
if mibBuilder.loadTexts:ets8801SensorTable.setStatus(_B)
_Ets8801SensorEntry_Object=MibTableRow
ets8801SensorEntry=_Ets8801SensorEntry_Object((1,3,6,1,4,1,28507,41,1,6,1,1))
ets8801SensorEntry.setIndexNames((0,_A,_E))
if mibBuilder.loadTexts:ets8801SensorEntry.setStatus(_B)
class _Ets8801SensorIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_Ets8801SensorIndex_Type.__name__=_D
_Ets8801SensorIndex_Object=MibTableColumn
ets8801SensorIndex=_Ets8801SensorIndex_Object((1,3,6,1,4,1,28507,41,1,6,1,1,1),_Ets8801SensorIndex_Type())
ets8801SensorIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:ets8801SensorIndex.setStatus(_B)
_Ets8801TempSensor_Type=Integer32
_Ets8801TempSensor_Object=MibTableColumn
ets8801TempSensor=_Ets8801TempSensor_Object((1,3,6,1,4,1,28507,41,1,6,1,1,2),_Ets8801TempSensor_Type())
ets8801TempSensor.setMaxAccess(_C)
if mibBuilder.loadTexts:ets8801TempSensor.setStatus(_B)
if mibBuilder.loadTexts:ets8801TempSensor.setUnits(_M)
_Ets8801HygroSensor_Type=Integer32
_Ets8801HygroSensor_Object=MibTableColumn
ets8801HygroSensor=_Ets8801HygroSensor_Object((1,3,6,1,4,1,28507,41,1,6,1,1,3),_Ets8801HygroSensor_Type())
ets8801HygroSensor.setMaxAccess(_C)
if mibBuilder.loadTexts:ets8801HygroSensor.setStatus(_B)
if mibBuilder.loadTexts:ets8801HygroSensor.setUnits('0.1 percent humidity')
class _Ets8801InputSensor_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('off',0),('on',1)))
_Ets8801InputSensor_Type.__name__=_D
_Ets8801InputSensor_Object=MibTableColumn
ets8801InputSensor=_Ets8801InputSensor_Object((1,3,6,1,4,1,28507,41,1,6,1,1,4),_Ets8801InputSensor_Type())
ets8801InputSensor.setMaxAccess(_C)
if mibBuilder.loadTexts:ets8801InputSensor.setStatus(_B)
_Ets8801AirPressure_Type=Integer32
_Ets8801AirPressure_Object=MibTableColumn
ets8801AirPressure=_Ets8801AirPressure_Object((1,3,6,1,4,1,28507,41,1,6,1,1,5),_Ets8801AirPressure_Type())
ets8801AirPressure.setMaxAccess(_C)
if mibBuilder.loadTexts:ets8801AirPressure.setStatus(_B)
if mibBuilder.loadTexts:ets8801AirPressure.setUnits('1 hPA (hectopascal) ~ 1 milibar')
_Ets8801DewPoint_Type=Integer32
_Ets8801DewPoint_Object=MibTableColumn
ets8801DewPoint=_Ets8801DewPoint_Object((1,3,6,1,4,1,28507,41,1,6,1,1,6),_Ets8801DewPoint_Type())
ets8801DewPoint.setMaxAccess(_C)
if mibBuilder.loadTexts:ets8801DewPoint.setStatus(_B)
if mibBuilder.loadTexts:ets8801DewPoint.setUnits(_M)
_Ets8801DewPointDiff_Type=Integer32
_Ets8801DewPointDiff_Object=MibTableColumn
ets8801DewPointDiff=_Ets8801DewPointDiff_Object((1,3,6,1,4,1,28507,41,1,6,1,1,7),_Ets8801DewPointDiff_Type())
ets8801DewPointDiff.setMaxAccess(_C)
if mibBuilder.loadTexts:ets8801DewPointDiff.setStatus(_B)
if mibBuilder.loadTexts:ets8801DewPointDiff.setUnits(_M)
_Ets8801Conf_ObjectIdentity=ObjectIdentity
ets8801Conf=_Ets8801Conf_ObjectIdentity((1,3,6,1,4,1,28507,41,2))
_Ets8801Groups_ObjectIdentity=ObjectIdentity
ets8801Groups=_Ets8801Groups_ObjectIdentity((1,3,6,1,4,1,28507,41,2,1))
_Ets8801Compls_ObjectIdentity=ObjectIdentity
ets8801Compls=_Ets8801Compls_ObjectIdentity((1,3,6,1,4,1,28507,41,2,2))
_Ets8801Events_ObjectIdentity=ObjectIdentity
ets8801Events=_Ets8801Events_ObjectIdentity((1,3,6,1,4,1,28507,41,3))
ets8801BasicGroup=ObjectGroup((1,3,6,1,4,1,28507,41,2,1,1))
ets8801BasicGroup.setObjects(*((_A,_d),(_A,_L),(_A,_e),(_A,_f),(_A,_g),(_A,_I),(_A,_h),(_A,_i),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_j),(_A,_k),(_A,_R),(_A,_S),(_A,_l),(_A,_m),(_A,_n),(_A,_o),(_A,_p),(_A,_q),(_A,_r),(_A,_s),(_A,_t),(_A,_u),(_A,_v),(_A,_w),(_A,_x),(_A,_J),(_A,_K),(_A,_y),(_A,_T),(_A,_E),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_z),(_A,_Y)))
if mibBuilder.loadTexts:ets8801BasicGroup.setStatus(_B)
ets8801PrimaryPowerChangeEvt=NotificationType((1,3,6,1,4,1,28507,41,3,1))
ets8801PrimaryPowerChangeEvt.setObjects(*((_A,_J),(_A,_K)))
if mibBuilder.loadTexts:ets8801PrimaryPowerChangeEvt.setStatus(_B)
ets8801SecondaryPowerChangeEvt=NotificationType((1,3,6,1,4,1,28507,41,3,2))
ets8801SecondaryPowerChangeEvt.setObjects(*((_A,_J),(_A,_K)))
if mibBuilder.loadTexts:ets8801SecondaryPowerChangeEvt.setStatus(_B)
ets8801PowerSelectEvt=NotificationType((1,3,6,1,4,1,28507,41,3,3))
ets8801PowerSelectEvt.setObjects((_A,_T))
if mibBuilder.loadTexts:ets8801PowerSelectEvt.setStatus(_B)
ets8801TempEvtSen=NotificationType((1,3,6,1,4,1,28507,41,3,4))
ets8801TempEvtSen.setObjects(*((_A,_E),(_A,_U)))
if mibBuilder.loadTexts:ets8801TempEvtSen.setStatus(_B)
ets8801HygroEvtSen=NotificationType((1,3,6,1,4,1,28507,41,3,5))
ets8801HygroEvtSen.setObjects(*((_A,_E),(_A,_V)))
if mibBuilder.loadTexts:ets8801HygroEvtSen.setStatus(_B)
ets8801InputEvtSen=NotificationType((1,3,6,1,4,1,28507,41,3,6))
ets8801InputEvtSen.setObjects(*((_A,_E),(_A,_W)))
if mibBuilder.loadTexts:ets8801InputEvtSen.setStatus(_B)
ets8801AirPressureEvtSen=NotificationType((1,3,6,1,4,1,28507,41,3,7))
ets8801AirPressureEvtSen.setObjects(*((_A,_E),(_A,_X)))
if mibBuilder.loadTexts:ets8801AirPressureEvtSen.setStatus(_B)
ets8801DewPtDiffEvtSen=NotificationType((1,3,6,1,4,1,28507,41,3,8))
ets8801DewPtDiffEvtSen.setObjects(*((_A,_E),(_A,_Y)))
if mibBuilder.loadTexts:ets8801DewPtDiffEvtSen.setStatus(_B)
ets8801LineAmperageEvt=NotificationType((1,3,6,1,4,1,28507,41,3,9))
ets8801LineAmperageEvt.setObjects(*((_A,_I),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S)))
if mibBuilder.loadTexts:ets8801LineAmperageEvt.setStatus(_B)
ets8801NotificationGroup=NotificationGroup((1,3,6,1,4,1,28507,41,2,1,2))
ets8801NotificationGroup.setObjects(*((_A,_A0),(_A,_A1),(_A,_A2),(_A,_A3),(_A,_A4),(_A,_A5),(_A,_A6),(_A,_A7),(_A,_A8)))
if mibBuilder.loadTexts:ets8801NotificationGroup.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'gudeads':gudeads,'gadsETS8801':gadsETS8801,'ets8801Objects':ets8801Objects,'ets8801CommonConfig':ets8801CommonConfig,'ets8801SNMPaccess':ets8801SNMPaccess,_d:ets8801TrapCtrl,'ets8801TrapIPTable':ets8801TrapIPTable,'ets8801TrapIPEntry':ets8801TrapIPEntry,_L:ets8801TrapIPIndex,_e:ets8801TrapAddr,'ets8801IntActors':ets8801IntActors,_f:ets8801Buzzer,'ets8801IntSensors':ets8801IntSensors,'ets8801PowerChan':ets8801PowerChan,_g:ets8801ActivePowerChan,'ets8801PowerTable':ets8801PowerTable,'ets8801PowerEntry':ets8801PowerEntry,_I:ets8801PowerIndex,_h:ets8801ChanStatus,_i:ets8801AbsEnergyActive,_N:ets8801PowerActive,_O:ets8801Current,_P:ets8801Voltage,_Q:ets8801Frequency,_j:ets8801PowerFactor,_k:ets8801Pangle,_R:ets8801PowerApparent,_S:ets8801PowerReactive,_l:ets8801AbsEnergyReactive,_m:ets8801AbsEnergyActiveResettable,_n:ets8801AbsEnergyReactiveResettable,_o:ets8801ResetTime,_p:ets8801ForwEnergyActive,_q:ets8801ForwEnergyReactive,_r:ets8801ForwEnergyActiveResettable,_s:ets8801ForwEnergyReactiveResettable,_t:ets8801RevEnergyActive,_u:ets8801RevEnergyReactive,_v:ets8801RevEnergyActiveResettable,_w:ets8801RevEnergyReactiveResettable,_x:ets8801ResidualCurrent,'ets8801ETSPowerInfo':ets8801ETSPowerInfo,_J:ets8801PrimaryPowerAvail,_K:ets8801SecondaryPowerAvail,_y:ets8801LineSelectRequest,_T:ets8801PowerLineSelected,'ets8801ExtSensors':ets8801ExtSensors,'ets8801SensorTable':ets8801SensorTable,'ets8801SensorEntry':ets8801SensorEntry,_E:ets8801SensorIndex,_U:ets8801TempSensor,_V:ets8801HygroSensor,_W:ets8801InputSensor,_X:ets8801AirPressure,_z:ets8801DewPoint,_Y:ets8801DewPointDiff,'ets8801Conf':ets8801Conf,'ets8801Groups':ets8801Groups,'ets8801BasicGroup':ets8801BasicGroup,'ets8801NotificationGroup':ets8801NotificationGroup,'ets8801Compls':ets8801Compls,'ets8801Events':ets8801Events,_A0:ets8801PrimaryPowerChangeEvt,_A1:ets8801SecondaryPowerChangeEvt,_A2:ets8801PowerSelectEvt,_A4:ets8801TempEvtSen,_A5:ets8801HygroEvtSen,_A6:ets8801InputEvtSen,_A7:ets8801AirPressureEvtSen,_A8:ets8801DewPtDiffEvtSen,_A3:ets8801LineAmperageEvt})