_y='pdu8311DewPtDiffEvtSen'
_x='pdu8311AirPressureEvtSen'
_w='pdu8311LineAmperageEvt'
_v='pdu8311InputEvtSen'
_u='pdu8311HygroEvtSen'
_t='pdu8311TempEvtSen'
_s='pdu8311DewPoint'
_r='pdu8311ResidualCurrent'
_q='pdu8311RevEnergyReactiveResettable'
_p='pdu8311RevEnergyActiveResettable'
_o='pdu8311RevEnergyReactive'
_n='pdu8311RevEnergyActive'
_m='pdu8311ForwEnergyReactiveResettable'
_l='pdu8311ForwEnergyActiveResettable'
_k='pdu8311ForwEnergyReactive'
_j='pdu8311ForwEnergyActive'
_i='pdu8311ResetTime'
_h='pdu8311AbsEnergyReactiveResettable'
_g='pdu8311AbsEnergyActiveResettable'
_f='pdu8311AbsEnergyReactive'
_e='pdu8311Pangle'
_d='pdu8311PowerFactor'
_c='pdu8311AbsEnergyActive'
_b='pdu8311ChanStatus'
_a='pdu8311ActivePowerChan'
_Z='pdu8311TrapAddr'
_Y='pdu8311TrapCtrl'
_X='Unsigned32'
_W='OctetString'
_V='pdu8311DewPointDiff'
_U='pdu8311AirPressure'
_T='pdu8311InputSensor'
_S='pdu8311HygroSensor'
_R='pdu8311TempSensor'
_Q='pdu8311PowerReactive'
_P='pdu8311PowerApparent'
_O='pdu8311Frequency'
_N='pdu8311Voltage'
_M='pdu8311Current'
_L='pdu8311PowerActive'
_K='0.1 degree Celsius'
_J='pdu8311TrapIPIndex'
_I='read-write'
_H='pdu8311PowerIndex'
_G='VARh'
_F='Wh'
_E='Integer32'
_D='pdu8311SensorIndex'
_C='read-only'
_B='current'
_A='GUDEADS-PDU8311-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_W,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_X,'enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
gudeads=ModuleIdentity((1,3,6,1,4,1,28507))
if mibBuilder.loadTexts:gudeads.setRevisions(('2007-03-05 13:56',))
_GadsPDU8311_ObjectIdentity=ObjectIdentity
gadsPDU8311=_GadsPDU8311_ObjectIdentity((1,3,6,1,4,1,28507,62))
_Pdu8311Objects_ObjectIdentity=ObjectIdentity
pdu8311Objects=_Pdu8311Objects_ObjectIdentity((1,3,6,1,4,1,28507,62,1))
_Pdu8311CommonConfig_ObjectIdentity=ObjectIdentity
pdu8311CommonConfig=_Pdu8311CommonConfig_ObjectIdentity((1,3,6,1,4,1,28507,62,1,1))
_Pdu8311SNMPaccess_ObjectIdentity=ObjectIdentity
pdu8311SNMPaccess=_Pdu8311SNMPaccess_ObjectIdentity((1,3,6,1,4,1,28507,62,1,1,1))
class _Pdu8311TrapCtrl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3))
_Pdu8311TrapCtrl_Type.__name__=_E
_Pdu8311TrapCtrl_Object=MibScalar
pdu8311TrapCtrl=_Pdu8311TrapCtrl_Object((1,3,6,1,4,1,28507,62,1,1,1,1),_Pdu8311TrapCtrl_Type())
pdu8311TrapCtrl.setMaxAccess(_I)
if mibBuilder.loadTexts:pdu8311TrapCtrl.setStatus(_B)
_Pdu8311TrapIPTable_Object=MibTable
pdu8311TrapIPTable=_Pdu8311TrapIPTable_Object((1,3,6,1,4,1,28507,62,1,1,1,2))
if mibBuilder.loadTexts:pdu8311TrapIPTable.setStatus(_B)
_Pdu8311TrapIPEntry_Object=MibTableRow
pdu8311TrapIPEntry=_Pdu8311TrapIPEntry_Object((1,3,6,1,4,1,28507,62,1,1,1,2,1))
pdu8311TrapIPEntry.setIndexNames((0,_A,_J))
if mibBuilder.loadTexts:pdu8311TrapIPEntry.setStatus(_B)
class _Pdu8311TrapIPIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_Pdu8311TrapIPIndex_Type.__name__=_E
_Pdu8311TrapIPIndex_Object=MibTableColumn
pdu8311TrapIPIndex=_Pdu8311TrapIPIndex_Object((1,3,6,1,4,1,28507,62,1,1,1,2,1,1),_Pdu8311TrapIPIndex_Type())
pdu8311TrapIPIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:pdu8311TrapIPIndex.setStatus(_B)
class _Pdu8311TrapAddr_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,99))
_Pdu8311TrapAddr_Type.__name__=_W
_Pdu8311TrapAddr_Object=MibTableColumn
pdu8311TrapAddr=_Pdu8311TrapAddr_Object((1,3,6,1,4,1,28507,62,1,1,1,2,1,2),_Pdu8311TrapAddr_Type())
pdu8311TrapAddr.setMaxAccess(_I)
if mibBuilder.loadTexts:pdu8311TrapAddr.setStatus(_B)
_Pdu8311DeviceConfig_ObjectIdentity=ObjectIdentity
pdu8311DeviceConfig=_Pdu8311DeviceConfig_ObjectIdentity((1,3,6,1,4,1,28507,62,1,2))
_Pdu8311IntActors_ObjectIdentity=ObjectIdentity
pdu8311IntActors=_Pdu8311IntActors_ObjectIdentity((1,3,6,1,4,1,28507,62,1,3))
_Pdu8311ExtActors_ObjectIdentity=ObjectIdentity
pdu8311ExtActors=_Pdu8311ExtActors_ObjectIdentity((1,3,6,1,4,1,28507,62,1,4))
_Pdu8311IntSensors_ObjectIdentity=ObjectIdentity
pdu8311IntSensors=_Pdu8311IntSensors_ObjectIdentity((1,3,6,1,4,1,28507,62,1,5))
_Pdu8311PowerChan_ObjectIdentity=ObjectIdentity
pdu8311PowerChan=_Pdu8311PowerChan_ObjectIdentity((1,3,6,1,4,1,28507,62,1,5,1))
class _Pdu8311ActivePowerChan_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,3))
_Pdu8311ActivePowerChan_Type.__name__=_X
_Pdu8311ActivePowerChan_Object=MibScalar
pdu8311ActivePowerChan=_Pdu8311ActivePowerChan_Object((1,3,6,1,4,1,28507,62,1,5,1,1),_Pdu8311ActivePowerChan_Type())
pdu8311ActivePowerChan.setMaxAccess(_C)
if mibBuilder.loadTexts:pdu8311ActivePowerChan.setStatus(_B)
_Pdu8311PowerTable_Object=MibTable
pdu8311PowerTable=_Pdu8311PowerTable_Object((1,3,6,1,4,1,28507,62,1,5,1,2))
if mibBuilder.loadTexts:pdu8311PowerTable.setStatus(_B)
_Pdu8311PowerEntry_Object=MibTableRow
pdu8311PowerEntry=_Pdu8311PowerEntry_Object((1,3,6,1,4,1,28507,62,1,5,1,2,1))
pdu8311PowerEntry.setIndexNames((0,_A,_H))
if mibBuilder.loadTexts:pdu8311PowerEntry.setStatus(_B)
class _Pdu8311PowerIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1))
_Pdu8311PowerIndex_Type.__name__=_E
_Pdu8311PowerIndex_Object=MibTableColumn
pdu8311PowerIndex=_Pdu8311PowerIndex_Object((1,3,6,1,4,1,28507,62,1,5,1,2,1,1),_Pdu8311PowerIndex_Type())
pdu8311PowerIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:pdu8311PowerIndex.setStatus(_B)
class _Pdu8311ChanStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Pdu8311ChanStatus_Type.__name__=_E
_Pdu8311ChanStatus_Object=MibTableColumn
pdu8311ChanStatus=_Pdu8311ChanStatus_Object((1,3,6,1,4,1,28507,62,1,5,1,2,1,2),_Pdu8311ChanStatus_Type())
pdu8311ChanStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:pdu8311ChanStatus.setStatus(_B)
_Pdu8311AbsEnergyActive_Type=Unsigned32
_Pdu8311AbsEnergyActive_Object=MibTableColumn
pdu8311AbsEnergyActive=_Pdu8311AbsEnergyActive_Object((1,3,6,1,4,1,28507,62,1,5,1,2,1,3),_Pdu8311AbsEnergyActive_Type())
pdu8311AbsEnergyActive.setMaxAccess(_C)
if mibBuilder.loadTexts:pdu8311AbsEnergyActive.setStatus(_B)
if mibBuilder.loadTexts:pdu8311AbsEnergyActive.setUnits(_F)
_Pdu8311PowerActive_Type=Integer32
_Pdu8311PowerActive_Object=MibTableColumn
pdu8311PowerActive=_Pdu8311PowerActive_Object((1,3,6,1,4,1,28507,62,1,5,1,2,1,4),_Pdu8311PowerActive_Type())
pdu8311PowerActive.setMaxAccess(_C)
if mibBuilder.loadTexts:pdu8311PowerActive.setStatus(_B)
if mibBuilder.loadTexts:pdu8311PowerActive.setUnits('W')
_Pdu8311Current_Type=Unsigned32
_Pdu8311Current_Object=MibTableColumn
pdu8311Current=_Pdu8311Current_Object((1,3,6,1,4,1,28507,62,1,5,1,2,1,5),_Pdu8311Current_Type())
pdu8311Current.setMaxAccess(_C)
if mibBuilder.loadTexts:pdu8311Current.setStatus(_B)
if mibBuilder.loadTexts:pdu8311Current.setUnits('mA')
_Pdu8311Voltage_Type=Unsigned32
_Pdu8311Voltage_Object=MibTableColumn
pdu8311Voltage=_Pdu8311Voltage_Object((1,3,6,1,4,1,28507,62,1,5,1,2,1,6),_Pdu8311Voltage_Type())
pdu8311Voltage.setMaxAccess(_C)
if mibBuilder.loadTexts:pdu8311Voltage.setStatus(_B)
if mibBuilder.loadTexts:pdu8311Voltage.setUnits('V')
_Pdu8311Frequency_Type=Unsigned32
_Pdu8311Frequency_Object=MibTableColumn
pdu8311Frequency=_Pdu8311Frequency_Object((1,3,6,1,4,1,28507,62,1,5,1,2,1,7),_Pdu8311Frequency_Type())
pdu8311Frequency.setMaxAccess(_C)
if mibBuilder.loadTexts:pdu8311Frequency.setStatus(_B)
if mibBuilder.loadTexts:pdu8311Frequency.setUnits('0.01 hz')
_Pdu8311PowerFactor_Type=Integer32
_Pdu8311PowerFactor_Object=MibTableColumn
pdu8311PowerFactor=_Pdu8311PowerFactor_Object((1,3,6,1,4,1,28507,62,1,5,1,2,1,8),_Pdu8311PowerFactor_Type())
pdu8311PowerFactor.setMaxAccess(_C)
if mibBuilder.loadTexts:pdu8311PowerFactor.setStatus(_B)
if mibBuilder.loadTexts:pdu8311PowerFactor.setUnits('0.001')
_Pdu8311Pangle_Type=Integer32
_Pdu8311Pangle_Object=MibTableColumn
pdu8311Pangle=_Pdu8311Pangle_Object((1,3,6,1,4,1,28507,62,1,5,1,2,1,9),_Pdu8311Pangle_Type())
pdu8311Pangle.setMaxAccess(_C)
if mibBuilder.loadTexts:pdu8311Pangle.setStatus(_B)
if mibBuilder.loadTexts:pdu8311Pangle.setUnits('0.1 degree')
_Pdu8311PowerApparent_Type=Integer32
_Pdu8311PowerApparent_Object=MibTableColumn
pdu8311PowerApparent=_Pdu8311PowerApparent_Object((1,3,6,1,4,1,28507,62,1,5,1,2,1,10),_Pdu8311PowerApparent_Type())
pdu8311PowerApparent.setMaxAccess(_C)
if mibBuilder.loadTexts:pdu8311PowerApparent.setStatus(_B)
if mibBuilder.loadTexts:pdu8311PowerApparent.setUnits('VA')
_Pdu8311PowerReactive_Type=Integer32
_Pdu8311PowerReactive_Object=MibTableColumn
pdu8311PowerReactive=_Pdu8311PowerReactive_Object((1,3,6,1,4,1,28507,62,1,5,1,2,1,11),_Pdu8311PowerReactive_Type())
pdu8311PowerReactive.setMaxAccess(_C)
if mibBuilder.loadTexts:pdu8311PowerReactive.setStatus(_B)
if mibBuilder.loadTexts:pdu8311PowerReactive.setUnits('VAR')
_Pdu8311AbsEnergyReactive_Type=Unsigned32
_Pdu8311AbsEnergyReactive_Object=MibTableColumn
pdu8311AbsEnergyReactive=_Pdu8311AbsEnergyReactive_Object((1,3,6,1,4,1,28507,62,1,5,1,2,1,12),_Pdu8311AbsEnergyReactive_Type())
pdu8311AbsEnergyReactive.setMaxAccess(_C)
if mibBuilder.loadTexts:pdu8311AbsEnergyReactive.setStatus(_B)
if mibBuilder.loadTexts:pdu8311AbsEnergyReactive.setUnits(_G)
_Pdu8311AbsEnergyActiveResettable_Type=Unsigned32
_Pdu8311AbsEnergyActiveResettable_Object=MibTableColumn
pdu8311AbsEnergyActiveResettable=_Pdu8311AbsEnergyActiveResettable_Object((1,3,6,1,4,1,28507,62,1,5,1,2,1,13),_Pdu8311AbsEnergyActiveResettable_Type())
pdu8311AbsEnergyActiveResettable.setMaxAccess(_I)
if mibBuilder.loadTexts:pdu8311AbsEnergyActiveResettable.setStatus(_B)
if mibBuilder.loadTexts:pdu8311AbsEnergyActiveResettable.setUnits(_F)
_Pdu8311AbsEnergyReactiveResettable_Type=Unsigned32
_Pdu8311AbsEnergyReactiveResettable_Object=MibTableColumn
pdu8311AbsEnergyReactiveResettable=_Pdu8311AbsEnergyReactiveResettable_Object((1,3,6,1,4,1,28507,62,1,5,1,2,1,14),_Pdu8311AbsEnergyReactiveResettable_Type())
pdu8311AbsEnergyReactiveResettable.setMaxAccess(_C)
if mibBuilder.loadTexts:pdu8311AbsEnergyReactiveResettable.setStatus(_B)
if mibBuilder.loadTexts:pdu8311AbsEnergyReactiveResettable.setUnits(_G)
_Pdu8311ResetTime_Type=Unsigned32
_Pdu8311ResetTime_Object=MibTableColumn
pdu8311ResetTime=_Pdu8311ResetTime_Object((1,3,6,1,4,1,28507,62,1,5,1,2,1,15),_Pdu8311ResetTime_Type())
pdu8311ResetTime.setMaxAccess(_C)
if mibBuilder.loadTexts:pdu8311ResetTime.setStatus(_B)
if mibBuilder.loadTexts:pdu8311ResetTime.setUnits('s')
_Pdu8311ForwEnergyActive_Type=Unsigned32
_Pdu8311ForwEnergyActive_Object=MibTableColumn
pdu8311ForwEnergyActive=_Pdu8311ForwEnergyActive_Object((1,3,6,1,4,1,28507,62,1,5,1,2,1,16),_Pdu8311ForwEnergyActive_Type())
pdu8311ForwEnergyActive.setMaxAccess(_C)
if mibBuilder.loadTexts:pdu8311ForwEnergyActive.setStatus(_B)
if mibBuilder.loadTexts:pdu8311ForwEnergyActive.setUnits(_F)
_Pdu8311ForwEnergyReactive_Type=Unsigned32
_Pdu8311ForwEnergyReactive_Object=MibTableColumn
pdu8311ForwEnergyReactive=_Pdu8311ForwEnergyReactive_Object((1,3,6,1,4,1,28507,62,1,5,1,2,1,17),_Pdu8311ForwEnergyReactive_Type())
pdu8311ForwEnergyReactive.setMaxAccess(_C)
if mibBuilder.loadTexts:pdu8311ForwEnergyReactive.setStatus(_B)
if mibBuilder.loadTexts:pdu8311ForwEnergyReactive.setUnits(_G)
_Pdu8311ForwEnergyActiveResettable_Type=Unsigned32
_Pdu8311ForwEnergyActiveResettable_Object=MibTableColumn
pdu8311ForwEnergyActiveResettable=_Pdu8311ForwEnergyActiveResettable_Object((1,3,6,1,4,1,28507,62,1,5,1,2,1,18),_Pdu8311ForwEnergyActiveResettable_Type())
pdu8311ForwEnergyActiveResettable.setMaxAccess(_C)
if mibBuilder.loadTexts:pdu8311ForwEnergyActiveResettable.setStatus(_B)
if mibBuilder.loadTexts:pdu8311ForwEnergyActiveResettable.setUnits(_F)
_Pdu8311ForwEnergyReactiveResettable_Type=Unsigned32
_Pdu8311ForwEnergyReactiveResettable_Object=MibTableColumn
pdu8311ForwEnergyReactiveResettable=_Pdu8311ForwEnergyReactiveResettable_Object((1,3,6,1,4,1,28507,62,1,5,1,2,1,19),_Pdu8311ForwEnergyReactiveResettable_Type())
pdu8311ForwEnergyReactiveResettable.setMaxAccess(_C)
if mibBuilder.loadTexts:pdu8311ForwEnergyReactiveResettable.setStatus(_B)
if mibBuilder.loadTexts:pdu8311ForwEnergyReactiveResettable.setUnits(_G)
_Pdu8311RevEnergyActive_Type=Unsigned32
_Pdu8311RevEnergyActive_Object=MibTableColumn
pdu8311RevEnergyActive=_Pdu8311RevEnergyActive_Object((1,3,6,1,4,1,28507,62,1,5,1,2,1,20),_Pdu8311RevEnergyActive_Type())
pdu8311RevEnergyActive.setMaxAccess(_C)
if mibBuilder.loadTexts:pdu8311RevEnergyActive.setStatus(_B)
if mibBuilder.loadTexts:pdu8311RevEnergyActive.setUnits(_F)
_Pdu8311RevEnergyReactive_Type=Unsigned32
_Pdu8311RevEnergyReactive_Object=MibTableColumn
pdu8311RevEnergyReactive=_Pdu8311RevEnergyReactive_Object((1,3,6,1,4,1,28507,62,1,5,1,2,1,21),_Pdu8311RevEnergyReactive_Type())
pdu8311RevEnergyReactive.setMaxAccess(_C)
if mibBuilder.loadTexts:pdu8311RevEnergyReactive.setStatus(_B)
if mibBuilder.loadTexts:pdu8311RevEnergyReactive.setUnits(_G)
_Pdu8311RevEnergyActiveResettable_Type=Unsigned32
_Pdu8311RevEnergyActiveResettable_Object=MibTableColumn
pdu8311RevEnergyActiveResettable=_Pdu8311RevEnergyActiveResettable_Object((1,3,6,1,4,1,28507,62,1,5,1,2,1,22),_Pdu8311RevEnergyActiveResettable_Type())
pdu8311RevEnergyActiveResettable.setMaxAccess(_C)
if mibBuilder.loadTexts:pdu8311RevEnergyActiveResettable.setStatus(_B)
if mibBuilder.loadTexts:pdu8311RevEnergyActiveResettable.setUnits(_F)
_Pdu8311RevEnergyReactiveResettable_Type=Unsigned32
_Pdu8311RevEnergyReactiveResettable_Object=MibTableColumn
pdu8311RevEnergyReactiveResettable=_Pdu8311RevEnergyReactiveResettable_Object((1,3,6,1,4,1,28507,62,1,5,1,2,1,23),_Pdu8311RevEnergyReactiveResettable_Type())
pdu8311RevEnergyReactiveResettable.setMaxAccess(_C)
if mibBuilder.loadTexts:pdu8311RevEnergyReactiveResettable.setStatus(_B)
if mibBuilder.loadTexts:pdu8311RevEnergyReactiveResettable.setUnits(_G)
_Pdu8311ResidualCurrent_Type=Unsigned32
_Pdu8311ResidualCurrent_Object=MibTableColumn
pdu8311ResidualCurrent=_Pdu8311ResidualCurrent_Object((1,3,6,1,4,1,28507,62,1,5,1,2,1,24),_Pdu8311ResidualCurrent_Type())
pdu8311ResidualCurrent.setMaxAccess(_C)
if mibBuilder.loadTexts:pdu8311ResidualCurrent.setStatus(_B)
if mibBuilder.loadTexts:pdu8311ResidualCurrent.setUnits('mA')
_Pdu8311ExtSensors_ObjectIdentity=ObjectIdentity
pdu8311ExtSensors=_Pdu8311ExtSensors_ObjectIdentity((1,3,6,1,4,1,28507,62,1,6))
_Pdu8311SensorTable_Object=MibTable
pdu8311SensorTable=_Pdu8311SensorTable_Object((1,3,6,1,4,1,28507,62,1,6,1))
if mibBuilder.loadTexts:pdu8311SensorTable.setStatus(_B)
_Pdu8311SensorEntry_Object=MibTableRow
pdu8311SensorEntry=_Pdu8311SensorEntry_Object((1,3,6,1,4,1,28507,62,1,6,1,1))
pdu8311SensorEntry.setIndexNames((0,_A,_D))
if mibBuilder.loadTexts:pdu8311SensorEntry.setStatus(_B)
class _Pdu8311SensorIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_Pdu8311SensorIndex_Type.__name__=_E
_Pdu8311SensorIndex_Object=MibTableColumn
pdu8311SensorIndex=_Pdu8311SensorIndex_Object((1,3,6,1,4,1,28507,62,1,6,1,1,1),_Pdu8311SensorIndex_Type())
pdu8311SensorIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:pdu8311SensorIndex.setStatus(_B)
_Pdu8311TempSensor_Type=Integer32
_Pdu8311TempSensor_Object=MibTableColumn
pdu8311TempSensor=_Pdu8311TempSensor_Object((1,3,6,1,4,1,28507,62,1,6,1,1,2),_Pdu8311TempSensor_Type())
pdu8311TempSensor.setMaxAccess(_C)
if mibBuilder.loadTexts:pdu8311TempSensor.setStatus(_B)
if mibBuilder.loadTexts:pdu8311TempSensor.setUnits(_K)
_Pdu8311HygroSensor_Type=Integer32
_Pdu8311HygroSensor_Object=MibTableColumn
pdu8311HygroSensor=_Pdu8311HygroSensor_Object((1,3,6,1,4,1,28507,62,1,6,1,1,3),_Pdu8311HygroSensor_Type())
pdu8311HygroSensor.setMaxAccess(_C)
if mibBuilder.loadTexts:pdu8311HygroSensor.setStatus(_B)
if mibBuilder.loadTexts:pdu8311HygroSensor.setUnits('0.1 percent humidity')
class _Pdu8311InputSensor_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('off',0),('on',1)))
_Pdu8311InputSensor_Type.__name__=_E
_Pdu8311InputSensor_Object=MibTableColumn
pdu8311InputSensor=_Pdu8311InputSensor_Object((1,3,6,1,4,1,28507,62,1,6,1,1,4),_Pdu8311InputSensor_Type())
pdu8311InputSensor.setMaxAccess(_C)
if mibBuilder.loadTexts:pdu8311InputSensor.setStatus(_B)
_Pdu8311AirPressure_Type=Integer32
_Pdu8311AirPressure_Object=MibTableColumn
pdu8311AirPressure=_Pdu8311AirPressure_Object((1,3,6,1,4,1,28507,62,1,6,1,1,5),_Pdu8311AirPressure_Type())
pdu8311AirPressure.setMaxAccess(_C)
if mibBuilder.loadTexts:pdu8311AirPressure.setStatus(_B)
if mibBuilder.loadTexts:pdu8311AirPressure.setUnits('1 hPA (hectopascal) ~ 1 milibar')
_Pdu8311DewPoint_Type=Integer32
_Pdu8311DewPoint_Object=MibTableColumn
pdu8311DewPoint=_Pdu8311DewPoint_Object((1,3,6,1,4,1,28507,62,1,6,1,1,6),_Pdu8311DewPoint_Type())
pdu8311DewPoint.setMaxAccess(_C)
if mibBuilder.loadTexts:pdu8311DewPoint.setStatus(_B)
if mibBuilder.loadTexts:pdu8311DewPoint.setUnits(_K)
_Pdu8311DewPointDiff_Type=Integer32
_Pdu8311DewPointDiff_Object=MibTableColumn
pdu8311DewPointDiff=_Pdu8311DewPointDiff_Object((1,3,6,1,4,1,28507,62,1,6,1,1,7),_Pdu8311DewPointDiff_Type())
pdu8311DewPointDiff.setMaxAccess(_C)
if mibBuilder.loadTexts:pdu8311DewPointDiff.setStatus(_B)
if mibBuilder.loadTexts:pdu8311DewPointDiff.setUnits(_K)
_Pdu8311Conf_ObjectIdentity=ObjectIdentity
pdu8311Conf=_Pdu8311Conf_ObjectIdentity((1,3,6,1,4,1,28507,62,2))
_Pdu8311Groups_ObjectIdentity=ObjectIdentity
pdu8311Groups=_Pdu8311Groups_ObjectIdentity((1,3,6,1,4,1,28507,62,2,1))
_Pdu8311Compls_ObjectIdentity=ObjectIdentity
pdu8311Compls=_Pdu8311Compls_ObjectIdentity((1,3,6,1,4,1,28507,62,2,2))
_Events_ObjectIdentity=ObjectIdentity
events=_Events_ObjectIdentity((1,3,6,1,4,1,28507,62,3))
pdu8311BasicGroup=ObjectGroup((1,3,6,1,4,1,28507,62,2,1,1))
pdu8311BasicGroup.setObjects(*((_A,_Y),(_A,_J),(_A,_Z),(_A,_a),(_A,_H),(_A,_b),(_A,_c),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_d),(_A,_e),(_A,_P),(_A,_Q),(_A,_f),(_A,_g),(_A,_h),(_A,_i),(_A,_j),(_A,_k),(_A,_l),(_A,_m),(_A,_n),(_A,_o),(_A,_p),(_A,_q),(_A,_r),(_A,_D),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_s),(_A,_V)))
if mibBuilder.loadTexts:pdu8311BasicGroup.setStatus(_B)
pdu8311TempEvtSen=NotificationType((1,3,6,1,4,1,28507,62,3,1))
pdu8311TempEvtSen.setObjects(*((_A,_D),(_A,_R)))
if mibBuilder.loadTexts:pdu8311TempEvtSen.setStatus(_B)
pdu8311HygroEvtSen=NotificationType((1,3,6,1,4,1,28507,62,3,2))
pdu8311HygroEvtSen.setObjects(*((_A,_D),(_A,_S)))
if mibBuilder.loadTexts:pdu8311HygroEvtSen.setStatus(_B)
pdu8311InputEvtSen=NotificationType((1,3,6,1,4,1,28507,62,3,3))
pdu8311InputEvtSen.setObjects(*((_A,_D),(_A,_T)))
if mibBuilder.loadTexts:pdu8311InputEvtSen.setStatus(_B)
pdu8311AirPressureEvtSen=NotificationType((1,3,6,1,4,1,28507,62,3,4))
pdu8311AirPressureEvtSen.setObjects(*((_A,_D),(_A,_U)))
if mibBuilder.loadTexts:pdu8311AirPressureEvtSen.setStatus(_B)
pdu8311DewPtDiffEvtSen=NotificationType((1,3,6,1,4,1,28507,62,3,5))
pdu8311DewPtDiffEvtSen.setObjects(*((_A,_D),(_A,_V)))
if mibBuilder.loadTexts:pdu8311DewPtDiffEvtSen.setStatus(_B)
pdu8311LineAmperageEvt=NotificationType((1,3,6,1,4,1,28507,62,3,6))
pdu8311LineAmperageEvt.setObjects(*((_A,_H),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q)))
if mibBuilder.loadTexts:pdu8311LineAmperageEvt.setStatus(_B)
pdu8311NotificationGroup=NotificationGroup((1,3,6,1,4,1,28507,62,2,1,2))
pdu8311NotificationGroup.setObjects(*((_A,_t),(_A,_u),(_A,_v),(_A,_w),(_A,_x),(_A,_y)))
if mibBuilder.loadTexts:pdu8311NotificationGroup.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'gudeads':gudeads,'gadsPDU8311':gadsPDU8311,'pdu8311Objects':pdu8311Objects,'pdu8311CommonConfig':pdu8311CommonConfig,'pdu8311SNMPaccess':pdu8311SNMPaccess,_Y:pdu8311TrapCtrl,'pdu8311TrapIPTable':pdu8311TrapIPTable,'pdu8311TrapIPEntry':pdu8311TrapIPEntry,_J:pdu8311TrapIPIndex,_Z:pdu8311TrapAddr,'pdu8311DeviceConfig':pdu8311DeviceConfig,'pdu8311IntActors':pdu8311IntActors,'pdu8311ExtActors':pdu8311ExtActors,'pdu8311IntSensors':pdu8311IntSensors,'pdu8311PowerChan':pdu8311PowerChan,_a:pdu8311ActivePowerChan,'pdu8311PowerTable':pdu8311PowerTable,'pdu8311PowerEntry':pdu8311PowerEntry,_H:pdu8311PowerIndex,_b:pdu8311ChanStatus,_c:pdu8311AbsEnergyActive,_L:pdu8311PowerActive,_M:pdu8311Current,_N:pdu8311Voltage,_O:pdu8311Frequency,_d:pdu8311PowerFactor,_e:pdu8311Pangle,_P:pdu8311PowerApparent,_Q:pdu8311PowerReactive,_f:pdu8311AbsEnergyReactive,_g:pdu8311AbsEnergyActiveResettable,_h:pdu8311AbsEnergyReactiveResettable,_i:pdu8311ResetTime,_j:pdu8311ForwEnergyActive,_k:pdu8311ForwEnergyReactive,_l:pdu8311ForwEnergyActiveResettable,_m:pdu8311ForwEnergyReactiveResettable,_n:pdu8311RevEnergyActive,_o:pdu8311RevEnergyReactive,_p:pdu8311RevEnergyActiveResettable,_q:pdu8311RevEnergyReactiveResettable,_r:pdu8311ResidualCurrent,'pdu8311ExtSensors':pdu8311ExtSensors,'pdu8311SensorTable':pdu8311SensorTable,'pdu8311SensorEntry':pdu8311SensorEntry,_D:pdu8311SensorIndex,_R:pdu8311TempSensor,_S:pdu8311HygroSensor,_T:pdu8311InputSensor,_U:pdu8311AirPressure,_s:pdu8311DewPoint,_V:pdu8311DewPointDiff,'pdu8311Conf':pdu8311Conf,'pdu8311Groups':pdu8311Groups,'pdu8311BasicGroup':pdu8311BasicGroup,'pdu8311NotificationGroup':pdu8311NotificationGroup,'pdu8311Compls':pdu8311Compls,'events':events,_t:pdu8311TempEvtSen,_u:pdu8311HygroEvtSen,_v:pdu8311InputEvtSen,_x:pdu8311AirPressureEvtSen,_y:pdu8311DewPtDiffEvtSen,_w:pdu8311LineAmperageEvt})