_z='pdu8341LineAmperageEvt'
_y='pdu8341DewPtDiffEvtSen'
_x='pdu8341AirPressureEvtSen'
_w='pdu8341InputEvtSen'
_v='pdu8341HygroEvtSen'
_u='pdu8341TempEvtSen'
_t='pdu8341DewPoint'
_s='pdu8341ResidualCurrent'
_r='pdu8341RevEnergyReactiveResettable'
_q='pdu8341RevEnergyActiveResettable'
_p='pdu8341RevEnergyReactive'
_o='pdu8341RevEnergyActive'
_n='pdu8341ForwEnergyReactiveResettable'
_m='pdu8341ForwEnergyActiveResettable'
_l='pdu8341ForwEnergyReactive'
_k='pdu8341ForwEnergyActive'
_j='pdu8341ResetTime'
_i='pdu8341AbsEnergyReactiveResettable'
_h='pdu8341AbsEnergyActiveResettable'
_g='pdu8341AbsEnergyReactive'
_f='pdu8341Pangle'
_e='pdu8341PowerFactor'
_d='pdu8341AbsEnergyActive'
_c='pdu8341ChanStatus'
_b='pdu8341ActivePowerChan'
_a='pdu8341Buzzer'
_Z='pdu8341TrapAddr'
_Y='pdu8341TrapCtrl'
_X='Unsigned32'
_W='OctetString'
_V='pdu8341DewPointDiff'
_U='pdu8341AirPressure'
_T='pdu8341InputSensor'
_S='pdu8341HygroSensor'
_R='pdu8341TempSensor'
_Q='pdu8341PowerReactive'
_P='pdu8341PowerApparent'
_O='pdu8341Frequency'
_N='pdu8341Voltage'
_M='pdu8341Current'
_L='pdu8341PowerActive'
_K='0.1 degree Celsius'
_J='pdu8341TrapIPIndex'
_I='pdu8341PowerIndex'
_H='read-write'
_G='VARh'
_F='Wh'
_E='pdu8341SensorIndex'
_D='Integer32'
_C='read-only'
_B='current'
_A='GUDEADS-PDU8341-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_W,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_X,'enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
gudeads=ModuleIdentity((1,3,6,1,4,1,28507))
if mibBuilder.loadTexts:gudeads.setRevisions(('2007-03-05 13:56',))
_GadsPDU8341_ObjectIdentity=ObjectIdentity
gadsPDU8341=_GadsPDU8341_ObjectIdentity((1,3,6,1,4,1,28507,65))
_Pdu8341Objects_ObjectIdentity=ObjectIdentity
pdu8341Objects=_Pdu8341Objects_ObjectIdentity((1,3,6,1,4,1,28507,65,1))
_Pdu8341CommonConfig_ObjectIdentity=ObjectIdentity
pdu8341CommonConfig=_Pdu8341CommonConfig_ObjectIdentity((1,3,6,1,4,1,28507,65,1,1))
_Pdu8341SNMPaccess_ObjectIdentity=ObjectIdentity
pdu8341SNMPaccess=_Pdu8341SNMPaccess_ObjectIdentity((1,3,6,1,4,1,28507,65,1,1,1))
class _Pdu8341TrapCtrl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3))
_Pdu8341TrapCtrl_Type.__name__=_D
_Pdu8341TrapCtrl_Object=MibScalar
pdu8341TrapCtrl=_Pdu8341TrapCtrl_Object((1,3,6,1,4,1,28507,65,1,1,1,1),_Pdu8341TrapCtrl_Type())
pdu8341TrapCtrl.setMaxAccess(_H)
if mibBuilder.loadTexts:pdu8341TrapCtrl.setStatus(_B)
_Pdu8341TrapIPTable_Object=MibTable
pdu8341TrapIPTable=_Pdu8341TrapIPTable_Object((1,3,6,1,4,1,28507,65,1,1,1,2))
if mibBuilder.loadTexts:pdu8341TrapIPTable.setStatus(_B)
_Pdu8341TrapIPEntry_Object=MibTableRow
pdu8341TrapIPEntry=_Pdu8341TrapIPEntry_Object((1,3,6,1,4,1,28507,65,1,1,1,2,1))
pdu8341TrapIPEntry.setIndexNames((0,_A,_J))
if mibBuilder.loadTexts:pdu8341TrapIPEntry.setStatus(_B)
class _Pdu8341TrapIPIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_Pdu8341TrapIPIndex_Type.__name__=_D
_Pdu8341TrapIPIndex_Object=MibTableColumn
pdu8341TrapIPIndex=_Pdu8341TrapIPIndex_Object((1,3,6,1,4,1,28507,65,1,1,1,2,1,1),_Pdu8341TrapIPIndex_Type())
pdu8341TrapIPIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:pdu8341TrapIPIndex.setStatus(_B)
class _Pdu8341TrapAddr_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,99))
_Pdu8341TrapAddr_Type.__name__=_W
_Pdu8341TrapAddr_Object=MibTableColumn
pdu8341TrapAddr=_Pdu8341TrapAddr_Object((1,3,6,1,4,1,28507,65,1,1,1,2,1,2),_Pdu8341TrapAddr_Type())
pdu8341TrapAddr.setMaxAccess(_H)
if mibBuilder.loadTexts:pdu8341TrapAddr.setStatus(_B)
_Pdu8341DeviceConfig_ObjectIdentity=ObjectIdentity
pdu8341DeviceConfig=_Pdu8341DeviceConfig_ObjectIdentity((1,3,6,1,4,1,28507,65,1,2))
_Pdu8341IntActors_ObjectIdentity=ObjectIdentity
pdu8341IntActors=_Pdu8341IntActors_ObjectIdentity((1,3,6,1,4,1,28507,65,1,3))
class _Pdu8341Buzzer_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Pdu8341Buzzer_Type.__name__=_D
_Pdu8341Buzzer_Object=MibScalar
pdu8341Buzzer=_Pdu8341Buzzer_Object((1,3,6,1,4,1,28507,65,1,3,10),_Pdu8341Buzzer_Type())
pdu8341Buzzer.setMaxAccess(_H)
if mibBuilder.loadTexts:pdu8341Buzzer.setStatus(_B)
if mibBuilder.loadTexts:pdu8341Buzzer.setUnits('0 = Off, 1 = On')
_Pdu8341ExtActors_ObjectIdentity=ObjectIdentity
pdu8341ExtActors=_Pdu8341ExtActors_ObjectIdentity((1,3,6,1,4,1,28507,65,1,4))
_Pdu8341IntSensors_ObjectIdentity=ObjectIdentity
pdu8341IntSensors=_Pdu8341IntSensors_ObjectIdentity((1,3,6,1,4,1,28507,65,1,5))
_Pdu8341PowerChan_ObjectIdentity=ObjectIdentity
pdu8341PowerChan=_Pdu8341PowerChan_ObjectIdentity((1,3,6,1,4,1,28507,65,1,5,1))
class _Pdu8341ActivePowerChan_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_Pdu8341ActivePowerChan_Type.__name__=_X
_Pdu8341ActivePowerChan_Object=MibScalar
pdu8341ActivePowerChan=_Pdu8341ActivePowerChan_Object((1,3,6,1,4,1,28507,65,1,5,1,1),_Pdu8341ActivePowerChan_Type())
pdu8341ActivePowerChan.setMaxAccess(_C)
if mibBuilder.loadTexts:pdu8341ActivePowerChan.setStatus(_B)
_Pdu8341PowerTable_Object=MibTable
pdu8341PowerTable=_Pdu8341PowerTable_Object((1,3,6,1,4,1,28507,65,1,5,1,2))
if mibBuilder.loadTexts:pdu8341PowerTable.setStatus(_B)
_Pdu8341PowerEntry_Object=MibTableRow
pdu8341PowerEntry=_Pdu8341PowerEntry_Object((1,3,6,1,4,1,28507,65,1,5,1,2,1))
pdu8341PowerEntry.setIndexNames((0,_A,_I))
if mibBuilder.loadTexts:pdu8341PowerEntry.setStatus(_B)
class _Pdu8341PowerIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_Pdu8341PowerIndex_Type.__name__=_D
_Pdu8341PowerIndex_Object=MibTableColumn
pdu8341PowerIndex=_Pdu8341PowerIndex_Object((1,3,6,1,4,1,28507,65,1,5,1,2,1,1),_Pdu8341PowerIndex_Type())
pdu8341PowerIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:pdu8341PowerIndex.setStatus(_B)
class _Pdu8341ChanStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Pdu8341ChanStatus_Type.__name__=_D
_Pdu8341ChanStatus_Object=MibTableColumn
pdu8341ChanStatus=_Pdu8341ChanStatus_Object((1,3,6,1,4,1,28507,65,1,5,1,2,1,2),_Pdu8341ChanStatus_Type())
pdu8341ChanStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:pdu8341ChanStatus.setStatus(_B)
_Pdu8341AbsEnergyActive_Type=Unsigned32
_Pdu8341AbsEnergyActive_Object=MibTableColumn
pdu8341AbsEnergyActive=_Pdu8341AbsEnergyActive_Object((1,3,6,1,4,1,28507,65,1,5,1,2,1,3),_Pdu8341AbsEnergyActive_Type())
pdu8341AbsEnergyActive.setMaxAccess(_C)
if mibBuilder.loadTexts:pdu8341AbsEnergyActive.setStatus(_B)
if mibBuilder.loadTexts:pdu8341AbsEnergyActive.setUnits(_F)
_Pdu8341PowerActive_Type=Integer32
_Pdu8341PowerActive_Object=MibTableColumn
pdu8341PowerActive=_Pdu8341PowerActive_Object((1,3,6,1,4,1,28507,65,1,5,1,2,1,4),_Pdu8341PowerActive_Type())
pdu8341PowerActive.setMaxAccess(_C)
if mibBuilder.loadTexts:pdu8341PowerActive.setStatus(_B)
if mibBuilder.loadTexts:pdu8341PowerActive.setUnits('W')
_Pdu8341Current_Type=Unsigned32
_Pdu8341Current_Object=MibTableColumn
pdu8341Current=_Pdu8341Current_Object((1,3,6,1,4,1,28507,65,1,5,1,2,1,5),_Pdu8341Current_Type())
pdu8341Current.setMaxAccess(_C)
if mibBuilder.loadTexts:pdu8341Current.setStatus(_B)
if mibBuilder.loadTexts:pdu8341Current.setUnits('mA')
_Pdu8341Voltage_Type=Unsigned32
_Pdu8341Voltage_Object=MibTableColumn
pdu8341Voltage=_Pdu8341Voltage_Object((1,3,6,1,4,1,28507,65,1,5,1,2,1,6),_Pdu8341Voltage_Type())
pdu8341Voltage.setMaxAccess(_C)
if mibBuilder.loadTexts:pdu8341Voltage.setStatus(_B)
if mibBuilder.loadTexts:pdu8341Voltage.setUnits('V')
_Pdu8341Frequency_Type=Unsigned32
_Pdu8341Frequency_Object=MibTableColumn
pdu8341Frequency=_Pdu8341Frequency_Object((1,3,6,1,4,1,28507,65,1,5,1,2,1,7),_Pdu8341Frequency_Type())
pdu8341Frequency.setMaxAccess(_C)
if mibBuilder.loadTexts:pdu8341Frequency.setStatus(_B)
if mibBuilder.loadTexts:pdu8341Frequency.setUnits('0.01 hz')
_Pdu8341PowerFactor_Type=Integer32
_Pdu8341PowerFactor_Object=MibTableColumn
pdu8341PowerFactor=_Pdu8341PowerFactor_Object((1,3,6,1,4,1,28507,65,1,5,1,2,1,8),_Pdu8341PowerFactor_Type())
pdu8341PowerFactor.setMaxAccess(_C)
if mibBuilder.loadTexts:pdu8341PowerFactor.setStatus(_B)
if mibBuilder.loadTexts:pdu8341PowerFactor.setUnits('0.001')
_Pdu8341Pangle_Type=Integer32
_Pdu8341Pangle_Object=MibTableColumn
pdu8341Pangle=_Pdu8341Pangle_Object((1,3,6,1,4,1,28507,65,1,5,1,2,1,9),_Pdu8341Pangle_Type())
pdu8341Pangle.setMaxAccess(_C)
if mibBuilder.loadTexts:pdu8341Pangle.setStatus(_B)
if mibBuilder.loadTexts:pdu8341Pangle.setUnits('0.1 degree')
_Pdu8341PowerApparent_Type=Integer32
_Pdu8341PowerApparent_Object=MibTableColumn
pdu8341PowerApparent=_Pdu8341PowerApparent_Object((1,3,6,1,4,1,28507,65,1,5,1,2,1,10),_Pdu8341PowerApparent_Type())
pdu8341PowerApparent.setMaxAccess(_C)
if mibBuilder.loadTexts:pdu8341PowerApparent.setStatus(_B)
if mibBuilder.loadTexts:pdu8341PowerApparent.setUnits('VA')
_Pdu8341PowerReactive_Type=Integer32
_Pdu8341PowerReactive_Object=MibTableColumn
pdu8341PowerReactive=_Pdu8341PowerReactive_Object((1,3,6,1,4,1,28507,65,1,5,1,2,1,11),_Pdu8341PowerReactive_Type())
pdu8341PowerReactive.setMaxAccess(_C)
if mibBuilder.loadTexts:pdu8341PowerReactive.setStatus(_B)
if mibBuilder.loadTexts:pdu8341PowerReactive.setUnits('VAR')
_Pdu8341AbsEnergyReactive_Type=Unsigned32
_Pdu8341AbsEnergyReactive_Object=MibTableColumn
pdu8341AbsEnergyReactive=_Pdu8341AbsEnergyReactive_Object((1,3,6,1,4,1,28507,65,1,5,1,2,1,12),_Pdu8341AbsEnergyReactive_Type())
pdu8341AbsEnergyReactive.setMaxAccess(_C)
if mibBuilder.loadTexts:pdu8341AbsEnergyReactive.setStatus(_B)
if mibBuilder.loadTexts:pdu8341AbsEnergyReactive.setUnits(_G)
_Pdu8341AbsEnergyActiveResettable_Type=Unsigned32
_Pdu8341AbsEnergyActiveResettable_Object=MibTableColumn
pdu8341AbsEnergyActiveResettable=_Pdu8341AbsEnergyActiveResettable_Object((1,3,6,1,4,1,28507,65,1,5,1,2,1,13),_Pdu8341AbsEnergyActiveResettable_Type())
pdu8341AbsEnergyActiveResettable.setMaxAccess(_H)
if mibBuilder.loadTexts:pdu8341AbsEnergyActiveResettable.setStatus(_B)
if mibBuilder.loadTexts:pdu8341AbsEnergyActiveResettable.setUnits(_F)
_Pdu8341AbsEnergyReactiveResettable_Type=Unsigned32
_Pdu8341AbsEnergyReactiveResettable_Object=MibTableColumn
pdu8341AbsEnergyReactiveResettable=_Pdu8341AbsEnergyReactiveResettable_Object((1,3,6,1,4,1,28507,65,1,5,1,2,1,14),_Pdu8341AbsEnergyReactiveResettable_Type())
pdu8341AbsEnergyReactiveResettable.setMaxAccess(_C)
if mibBuilder.loadTexts:pdu8341AbsEnergyReactiveResettable.setStatus(_B)
if mibBuilder.loadTexts:pdu8341AbsEnergyReactiveResettable.setUnits(_G)
_Pdu8341ResetTime_Type=Unsigned32
_Pdu8341ResetTime_Object=MibTableColumn
pdu8341ResetTime=_Pdu8341ResetTime_Object((1,3,6,1,4,1,28507,65,1,5,1,2,1,15),_Pdu8341ResetTime_Type())
pdu8341ResetTime.setMaxAccess(_C)
if mibBuilder.loadTexts:pdu8341ResetTime.setStatus(_B)
if mibBuilder.loadTexts:pdu8341ResetTime.setUnits('s')
_Pdu8341ForwEnergyActive_Type=Unsigned32
_Pdu8341ForwEnergyActive_Object=MibTableColumn
pdu8341ForwEnergyActive=_Pdu8341ForwEnergyActive_Object((1,3,6,1,4,1,28507,65,1,5,1,2,1,16),_Pdu8341ForwEnergyActive_Type())
pdu8341ForwEnergyActive.setMaxAccess(_C)
if mibBuilder.loadTexts:pdu8341ForwEnergyActive.setStatus(_B)
if mibBuilder.loadTexts:pdu8341ForwEnergyActive.setUnits(_F)
_Pdu8341ForwEnergyReactive_Type=Unsigned32
_Pdu8341ForwEnergyReactive_Object=MibTableColumn
pdu8341ForwEnergyReactive=_Pdu8341ForwEnergyReactive_Object((1,3,6,1,4,1,28507,65,1,5,1,2,1,17),_Pdu8341ForwEnergyReactive_Type())
pdu8341ForwEnergyReactive.setMaxAccess(_C)
if mibBuilder.loadTexts:pdu8341ForwEnergyReactive.setStatus(_B)
if mibBuilder.loadTexts:pdu8341ForwEnergyReactive.setUnits(_G)
_Pdu8341ForwEnergyActiveResettable_Type=Unsigned32
_Pdu8341ForwEnergyActiveResettable_Object=MibTableColumn
pdu8341ForwEnergyActiveResettable=_Pdu8341ForwEnergyActiveResettable_Object((1,3,6,1,4,1,28507,65,1,5,1,2,1,18),_Pdu8341ForwEnergyActiveResettable_Type())
pdu8341ForwEnergyActiveResettable.setMaxAccess(_C)
if mibBuilder.loadTexts:pdu8341ForwEnergyActiveResettable.setStatus(_B)
if mibBuilder.loadTexts:pdu8341ForwEnergyActiveResettable.setUnits(_F)
_Pdu8341ForwEnergyReactiveResettable_Type=Unsigned32
_Pdu8341ForwEnergyReactiveResettable_Object=MibTableColumn
pdu8341ForwEnergyReactiveResettable=_Pdu8341ForwEnergyReactiveResettable_Object((1,3,6,1,4,1,28507,65,1,5,1,2,1,19),_Pdu8341ForwEnergyReactiveResettable_Type())
pdu8341ForwEnergyReactiveResettable.setMaxAccess(_C)
if mibBuilder.loadTexts:pdu8341ForwEnergyReactiveResettable.setStatus(_B)
if mibBuilder.loadTexts:pdu8341ForwEnergyReactiveResettable.setUnits(_G)
_Pdu8341RevEnergyActive_Type=Unsigned32
_Pdu8341RevEnergyActive_Object=MibTableColumn
pdu8341RevEnergyActive=_Pdu8341RevEnergyActive_Object((1,3,6,1,4,1,28507,65,1,5,1,2,1,20),_Pdu8341RevEnergyActive_Type())
pdu8341RevEnergyActive.setMaxAccess(_C)
if mibBuilder.loadTexts:pdu8341RevEnergyActive.setStatus(_B)
if mibBuilder.loadTexts:pdu8341RevEnergyActive.setUnits(_F)
_Pdu8341RevEnergyReactive_Type=Unsigned32
_Pdu8341RevEnergyReactive_Object=MibTableColumn
pdu8341RevEnergyReactive=_Pdu8341RevEnergyReactive_Object((1,3,6,1,4,1,28507,65,1,5,1,2,1,21),_Pdu8341RevEnergyReactive_Type())
pdu8341RevEnergyReactive.setMaxAccess(_C)
if mibBuilder.loadTexts:pdu8341RevEnergyReactive.setStatus(_B)
if mibBuilder.loadTexts:pdu8341RevEnergyReactive.setUnits(_G)
_Pdu8341RevEnergyActiveResettable_Type=Unsigned32
_Pdu8341RevEnergyActiveResettable_Object=MibTableColumn
pdu8341RevEnergyActiveResettable=_Pdu8341RevEnergyActiveResettable_Object((1,3,6,1,4,1,28507,65,1,5,1,2,1,22),_Pdu8341RevEnergyActiveResettable_Type())
pdu8341RevEnergyActiveResettable.setMaxAccess(_C)
if mibBuilder.loadTexts:pdu8341RevEnergyActiveResettable.setStatus(_B)
if mibBuilder.loadTexts:pdu8341RevEnergyActiveResettable.setUnits(_F)
_Pdu8341RevEnergyReactiveResettable_Type=Unsigned32
_Pdu8341RevEnergyReactiveResettable_Object=MibTableColumn
pdu8341RevEnergyReactiveResettable=_Pdu8341RevEnergyReactiveResettable_Object((1,3,6,1,4,1,28507,65,1,5,1,2,1,23),_Pdu8341RevEnergyReactiveResettable_Type())
pdu8341RevEnergyReactiveResettable.setMaxAccess(_C)
if mibBuilder.loadTexts:pdu8341RevEnergyReactiveResettable.setStatus(_B)
if mibBuilder.loadTexts:pdu8341RevEnergyReactiveResettable.setUnits(_G)
_Pdu8341ResidualCurrent_Type=Unsigned32
_Pdu8341ResidualCurrent_Object=MibTableColumn
pdu8341ResidualCurrent=_Pdu8341ResidualCurrent_Object((1,3,6,1,4,1,28507,65,1,5,1,2,1,24),_Pdu8341ResidualCurrent_Type())
pdu8341ResidualCurrent.setMaxAccess(_C)
if mibBuilder.loadTexts:pdu8341ResidualCurrent.setStatus(_B)
if mibBuilder.loadTexts:pdu8341ResidualCurrent.setUnits('mA')
_Pdu8341ExtSensors_ObjectIdentity=ObjectIdentity
pdu8341ExtSensors=_Pdu8341ExtSensors_ObjectIdentity((1,3,6,1,4,1,28507,65,1,6))
_Pdu8341SensorTable_Object=MibTable
pdu8341SensorTable=_Pdu8341SensorTable_Object((1,3,6,1,4,1,28507,65,1,6,1))
if mibBuilder.loadTexts:pdu8341SensorTable.setStatus(_B)
_Pdu8341SensorEntry_Object=MibTableRow
pdu8341SensorEntry=_Pdu8341SensorEntry_Object((1,3,6,1,4,1,28507,65,1,6,1,1))
pdu8341SensorEntry.setIndexNames((0,_A,_E))
if mibBuilder.loadTexts:pdu8341SensorEntry.setStatus(_B)
class _Pdu8341SensorIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_Pdu8341SensorIndex_Type.__name__=_D
_Pdu8341SensorIndex_Object=MibTableColumn
pdu8341SensorIndex=_Pdu8341SensorIndex_Object((1,3,6,1,4,1,28507,65,1,6,1,1,1),_Pdu8341SensorIndex_Type())
pdu8341SensorIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:pdu8341SensorIndex.setStatus(_B)
_Pdu8341TempSensor_Type=Integer32
_Pdu8341TempSensor_Object=MibTableColumn
pdu8341TempSensor=_Pdu8341TempSensor_Object((1,3,6,1,4,1,28507,65,1,6,1,1,2),_Pdu8341TempSensor_Type())
pdu8341TempSensor.setMaxAccess(_C)
if mibBuilder.loadTexts:pdu8341TempSensor.setStatus(_B)
if mibBuilder.loadTexts:pdu8341TempSensor.setUnits(_K)
_Pdu8341HygroSensor_Type=Integer32
_Pdu8341HygroSensor_Object=MibTableColumn
pdu8341HygroSensor=_Pdu8341HygroSensor_Object((1,3,6,1,4,1,28507,65,1,6,1,1,3),_Pdu8341HygroSensor_Type())
pdu8341HygroSensor.setMaxAccess(_C)
if mibBuilder.loadTexts:pdu8341HygroSensor.setStatus(_B)
if mibBuilder.loadTexts:pdu8341HygroSensor.setUnits('0.1 percent humidity')
class _Pdu8341InputSensor_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('off',0),('on',1)))
_Pdu8341InputSensor_Type.__name__=_D
_Pdu8341InputSensor_Object=MibTableColumn
pdu8341InputSensor=_Pdu8341InputSensor_Object((1,3,6,1,4,1,28507,65,1,6,1,1,4),_Pdu8341InputSensor_Type())
pdu8341InputSensor.setMaxAccess(_C)
if mibBuilder.loadTexts:pdu8341InputSensor.setStatus(_B)
_Pdu8341AirPressure_Type=Integer32
_Pdu8341AirPressure_Object=MibTableColumn
pdu8341AirPressure=_Pdu8341AirPressure_Object((1,3,6,1,4,1,28507,65,1,6,1,1,5),_Pdu8341AirPressure_Type())
pdu8341AirPressure.setMaxAccess(_C)
if mibBuilder.loadTexts:pdu8341AirPressure.setStatus(_B)
if mibBuilder.loadTexts:pdu8341AirPressure.setUnits('1 hPA (hectopascal) ~ 1 milibar')
_Pdu8341DewPoint_Type=Integer32
_Pdu8341DewPoint_Object=MibTableColumn
pdu8341DewPoint=_Pdu8341DewPoint_Object((1,3,6,1,4,1,28507,65,1,6,1,1,6),_Pdu8341DewPoint_Type())
pdu8341DewPoint.setMaxAccess(_C)
if mibBuilder.loadTexts:pdu8341DewPoint.setStatus(_B)
if mibBuilder.loadTexts:pdu8341DewPoint.setUnits(_K)
_Pdu8341DewPointDiff_Type=Integer32
_Pdu8341DewPointDiff_Object=MibTableColumn
pdu8341DewPointDiff=_Pdu8341DewPointDiff_Object((1,3,6,1,4,1,28507,65,1,6,1,1,7),_Pdu8341DewPointDiff_Type())
pdu8341DewPointDiff.setMaxAccess(_C)
if mibBuilder.loadTexts:pdu8341DewPointDiff.setStatus(_B)
if mibBuilder.loadTexts:pdu8341DewPointDiff.setUnits(_K)
_Pdu8341Conf_ObjectIdentity=ObjectIdentity
pdu8341Conf=_Pdu8341Conf_ObjectIdentity((1,3,6,1,4,1,28507,65,2))
_Pdu8341Groups_ObjectIdentity=ObjectIdentity
pdu8341Groups=_Pdu8341Groups_ObjectIdentity((1,3,6,1,4,1,28507,65,2,1))
_Pdu8341Compls_ObjectIdentity=ObjectIdentity
pdu8341Compls=_Pdu8341Compls_ObjectIdentity((1,3,6,1,4,1,28507,65,2,2))
_Events_ObjectIdentity=ObjectIdentity
events=_Events_ObjectIdentity((1,3,6,1,4,1,28507,65,3))
pdu8341BasicGroup=ObjectGroup((1,3,6,1,4,1,28507,65,2,1,1))
pdu8341BasicGroup.setObjects(*((_A,_Y),(_A,_J),(_A,_Z),(_A,_a),(_A,_b),(_A,_I),(_A,_c),(_A,_d),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_e),(_A,_f),(_A,_P),(_A,_Q),(_A,_g),(_A,_h),(_A,_i),(_A,_j),(_A,_k),(_A,_l),(_A,_m),(_A,_n),(_A,_o),(_A,_p),(_A,_q),(_A,_r),(_A,_s),(_A,_E),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_t),(_A,_V)))
if mibBuilder.loadTexts:pdu8341BasicGroup.setStatus(_B)
pdu8341TempEvtSen=NotificationType((1,3,6,1,4,1,28507,65,3,1))
pdu8341TempEvtSen.setObjects(*((_A,_E),(_A,_R)))
if mibBuilder.loadTexts:pdu8341TempEvtSen.setStatus(_B)
pdu8341HygroEvtSen=NotificationType((1,3,6,1,4,1,28507,65,3,2))
pdu8341HygroEvtSen.setObjects(*((_A,_E),(_A,_S)))
if mibBuilder.loadTexts:pdu8341HygroEvtSen.setStatus(_B)
pdu8341InputEvtSen=NotificationType((1,3,6,1,4,1,28507,65,3,3))
pdu8341InputEvtSen.setObjects(*((_A,_E),(_A,_T)))
if mibBuilder.loadTexts:pdu8341InputEvtSen.setStatus(_B)
pdu8341AirPressureEvtSen=NotificationType((1,3,6,1,4,1,28507,65,3,4))
pdu8341AirPressureEvtSen.setObjects(*((_A,_E),(_A,_U)))
if mibBuilder.loadTexts:pdu8341AirPressureEvtSen.setStatus(_B)
pdu8341DewPtDiffEvtSen=NotificationType((1,3,6,1,4,1,28507,65,3,5))
pdu8341DewPtDiffEvtSen.setObjects(*((_A,_E),(_A,_V)))
if mibBuilder.loadTexts:pdu8341DewPtDiffEvtSen.setStatus(_B)
pdu8341LineAmperageEvt=NotificationType((1,3,6,1,4,1,28507,65,3,6))
pdu8341LineAmperageEvt.setObjects(*((_A,_I),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q)))
if mibBuilder.loadTexts:pdu8341LineAmperageEvt.setStatus(_B)
pdu8341NotificationGroup=NotificationGroup((1,3,6,1,4,1,28507,65,2,1,2))
pdu8341NotificationGroup.setObjects(*((_A,_u),(_A,_v),(_A,_w),(_A,_x),(_A,_y),(_A,_z)))
if mibBuilder.loadTexts:pdu8341NotificationGroup.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'gudeads':gudeads,'gadsPDU8341':gadsPDU8341,'pdu8341Objects':pdu8341Objects,'pdu8341CommonConfig':pdu8341CommonConfig,'pdu8341SNMPaccess':pdu8341SNMPaccess,_Y:pdu8341TrapCtrl,'pdu8341TrapIPTable':pdu8341TrapIPTable,'pdu8341TrapIPEntry':pdu8341TrapIPEntry,_J:pdu8341TrapIPIndex,_Z:pdu8341TrapAddr,'pdu8341DeviceConfig':pdu8341DeviceConfig,'pdu8341IntActors':pdu8341IntActors,_a:pdu8341Buzzer,'pdu8341ExtActors':pdu8341ExtActors,'pdu8341IntSensors':pdu8341IntSensors,'pdu8341PowerChan':pdu8341PowerChan,_b:pdu8341ActivePowerChan,'pdu8341PowerTable':pdu8341PowerTable,'pdu8341PowerEntry':pdu8341PowerEntry,_I:pdu8341PowerIndex,_c:pdu8341ChanStatus,_d:pdu8341AbsEnergyActive,_L:pdu8341PowerActive,_M:pdu8341Current,_N:pdu8341Voltage,_O:pdu8341Frequency,_e:pdu8341PowerFactor,_f:pdu8341Pangle,_P:pdu8341PowerApparent,_Q:pdu8341PowerReactive,_g:pdu8341AbsEnergyReactive,_h:pdu8341AbsEnergyActiveResettable,_i:pdu8341AbsEnergyReactiveResettable,_j:pdu8341ResetTime,_k:pdu8341ForwEnergyActive,_l:pdu8341ForwEnergyReactive,_m:pdu8341ForwEnergyActiveResettable,_n:pdu8341ForwEnergyReactiveResettable,_o:pdu8341RevEnergyActive,_p:pdu8341RevEnergyReactive,_q:pdu8341RevEnergyActiveResettable,_r:pdu8341RevEnergyReactiveResettable,_s:pdu8341ResidualCurrent,'pdu8341ExtSensors':pdu8341ExtSensors,'pdu8341SensorTable':pdu8341SensorTable,'pdu8341SensorEntry':pdu8341SensorEntry,_E:pdu8341SensorIndex,_R:pdu8341TempSensor,_S:pdu8341HygroSensor,_T:pdu8341InputSensor,_U:pdu8341AirPressure,_t:pdu8341DewPoint,_V:pdu8341DewPointDiff,'pdu8341Conf':pdu8341Conf,'pdu8341Groups':pdu8341Groups,'pdu8341BasicGroup':pdu8341BasicGroup,'pdu8341NotificationGroup':pdu8341NotificationGroup,'pdu8341Compls':pdu8341Compls,'events':events,_u:pdu8341TempEvtSen,_v:pdu8341HygroEvtSen,_w:pdu8341InputEvtSen,_x:pdu8341AirPressureEvtSen,_y:pdu8341DewPtDiffEvtSen,_z:pdu8341LineAmperageEvt})