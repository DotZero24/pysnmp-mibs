_z='ats3020AmperageEvt1'
_y='ats3020InputEvtSen1'
_x='ats3020HygroEvtSen1'
_w='ats3020TempEvtSen1'
_v='ats3020PowerSelectEvt'
_u='ats3020SecondaryPowerChangeEvt'
_t='ats3020PrimaryPowerChangeEvt'
_s='ats3020RevEnergyReactiveResettable'
_r='ats3020RevEnergyActiveResettable'
_q='ats3020RevEnergyReactive'
_p='ats3020RevEnergyActive'
_o='ats3020ForwEnergyReactiveResettable'
_n='ats3020ForwEnergyActiveResettable'
_m='ats3020ForwEnergyReactive'
_l='ats3020ForwEnergyActive'
_k='ats3020ResetTime'
_j='ats3020AbsEnergyReactiveResettable'
_i='ats3020AbsEnergyActiveResettable'
_h='ats3020AbsEnergyReactive'
_g='ats3020Pangle'
_f='ats3020PowerFactor'
_e='ats3020AbsEnergyActive'
_d='ats3020ChanStatus'
_c='ats3020ActivePowerChan'
_b='ats3020Buzzer'
_a='ats3020TrapAddr'
_Z='ats3020TrapCtrl'
_Y='ats3020SensorIndex'
_X='ats3020PowerIndex'
_W='ats3020TrapIPIndex'
_V='Unsigned32'
_U='OctetString'
_T='ats3020InputSensor'
_S='ats3020HygroSensor'
_R='ats3020TempSensor'
_Q='ats3020PowerSelect'
_P='ats3020SecPowAvail'
_O='ats3020PrimPowAvail'
_N='ats3020PowerReactive'
_M='ats3020PowerApparent'
_L='ats3020Frequency'
_K='ats3020Voltage'
_J='ats3020Current'
_I='ats3020PowerActive'
_H='not-accessible'
_G='read-write'
_F='VARh'
_E='Wh'
_D='Integer32'
_C='read-only'
_B='current'
_A='GUDEADS-ATS3020-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_U,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_V,'enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
gudeads=ModuleIdentity((1,3,6,1,4,1,28507))
if mibBuilder.loadTexts:gudeads.setRevisions(('2007-05-23 12:44',))
_GadsATS3020_ObjectIdentity=ObjectIdentity
gadsATS3020=_GadsATS3020_ObjectIdentity((1,3,6,1,4,1,28507,40))
_Ats3020Events_ObjectIdentity=ObjectIdentity
ats3020Events=_Ats3020Events_ObjectIdentity((1,3,6,1,4,1,28507,40,0))
_Ats3020Objects_ObjectIdentity=ObjectIdentity
ats3020Objects=_Ats3020Objects_ObjectIdentity((1,3,6,1,4,1,28507,40,1))
_Ats3020CommonConfig_ObjectIdentity=ObjectIdentity
ats3020CommonConfig=_Ats3020CommonConfig_ObjectIdentity((1,3,6,1,4,1,28507,40,1,1))
_Ats3020SNMPaccess_ObjectIdentity=ObjectIdentity
ats3020SNMPaccess=_Ats3020SNMPaccess_ObjectIdentity((1,3,6,1,4,1,28507,40,1,1,1))
class _Ats3020TrapCtrl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_Ats3020TrapCtrl_Type.__name__=_D
_Ats3020TrapCtrl_Object=MibScalar
ats3020TrapCtrl=_Ats3020TrapCtrl_Object((1,3,6,1,4,1,28507,40,1,1,1,1),_Ats3020TrapCtrl_Type())
ats3020TrapCtrl.setMaxAccess(_G)
if mibBuilder.loadTexts:ats3020TrapCtrl.setStatus(_B)
_Ats3020TrapIPTable_Object=MibTable
ats3020TrapIPTable=_Ats3020TrapIPTable_Object((1,3,6,1,4,1,28507,40,1,1,1,2))
if mibBuilder.loadTexts:ats3020TrapIPTable.setStatus(_B)
_Ats3020TrapIPEntry_Object=MibTableRow
ats3020TrapIPEntry=_Ats3020TrapIPEntry_Object((1,3,6,1,4,1,28507,40,1,1,1,2,1))
ats3020TrapIPEntry.setIndexNames((0,_A,_W))
if mibBuilder.loadTexts:ats3020TrapIPEntry.setStatus(_B)
class _Ats3020TrapIPIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_Ats3020TrapIPIndex_Type.__name__=_D
_Ats3020TrapIPIndex_Object=MibTableColumn
ats3020TrapIPIndex=_Ats3020TrapIPIndex_Object((1,3,6,1,4,1,28507,40,1,1,1,2,1,1),_Ats3020TrapIPIndex_Type())
ats3020TrapIPIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:ats3020TrapIPIndex.setStatus(_B)
class _Ats3020TrapAddr_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,99))
_Ats3020TrapAddr_Type.__name__=_U
_Ats3020TrapAddr_Object=MibTableColumn
ats3020TrapAddr=_Ats3020TrapAddr_Object((1,3,6,1,4,1,28507,40,1,1,1,2,1,2),_Ats3020TrapAddr_Type())
ats3020TrapAddr.setMaxAccess(_G)
if mibBuilder.loadTexts:ats3020TrapAddr.setStatus(_B)
_Ats3020IntActors_ObjectIdentity=ObjectIdentity
ats3020IntActors=_Ats3020IntActors_ObjectIdentity((1,3,6,1,4,1,28507,40,1,3))
class _Ats3020Buzzer_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Ats3020Buzzer_Type.__name__=_D
_Ats3020Buzzer_Object=MibScalar
ats3020Buzzer=_Ats3020Buzzer_Object((1,3,6,1,4,1,28507,40,1,3,10),_Ats3020Buzzer_Type())
ats3020Buzzer.setMaxAccess(_G)
if mibBuilder.loadTexts:ats3020Buzzer.setStatus(_B)
if mibBuilder.loadTexts:ats3020Buzzer.setUnits('0 = Off, 1 = On')
_Ats3020IntSensors_ObjectIdentity=ObjectIdentity
ats3020IntSensors=_Ats3020IntSensors_ObjectIdentity((1,3,6,1,4,1,28507,40,1,5))
_Ats3020PowerChan_ObjectIdentity=ObjectIdentity
ats3020PowerChan=_Ats3020PowerChan_ObjectIdentity((1,3,6,1,4,1,28507,40,1,5,1))
class _Ats3020ActivePowerChan_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1))
_Ats3020ActivePowerChan_Type.__name__=_V
_Ats3020ActivePowerChan_Object=MibScalar
ats3020ActivePowerChan=_Ats3020ActivePowerChan_Object((1,3,6,1,4,1,28507,40,1,5,1,1),_Ats3020ActivePowerChan_Type())
ats3020ActivePowerChan.setMaxAccess(_C)
if mibBuilder.loadTexts:ats3020ActivePowerChan.setStatus(_B)
_Ats3020PowerTable_Object=MibTable
ats3020PowerTable=_Ats3020PowerTable_Object((1,3,6,1,4,1,28507,40,1,5,1,2))
if mibBuilder.loadTexts:ats3020PowerTable.setStatus(_B)
_Ats3020PowerEntry_Object=MibTableRow
ats3020PowerEntry=_Ats3020PowerEntry_Object((1,3,6,1,4,1,28507,40,1,5,1,2,1))
ats3020PowerEntry.setIndexNames((0,_A,_X))
if mibBuilder.loadTexts:ats3020PowerEntry.setStatus(_B)
class _Ats3020PowerIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1))
_Ats3020PowerIndex_Type.__name__=_D
_Ats3020PowerIndex_Object=MibTableColumn
ats3020PowerIndex=_Ats3020PowerIndex_Object((1,3,6,1,4,1,28507,40,1,5,1,2,1,1),_Ats3020PowerIndex_Type())
ats3020PowerIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:ats3020PowerIndex.setStatus(_B)
class _Ats3020ChanStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Ats3020ChanStatus_Type.__name__=_D
_Ats3020ChanStatus_Object=MibTableColumn
ats3020ChanStatus=_Ats3020ChanStatus_Object((1,3,6,1,4,1,28507,40,1,5,1,2,1,2),_Ats3020ChanStatus_Type())
ats3020ChanStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ats3020ChanStatus.setStatus(_B)
_Ats3020AbsEnergyActive_Type=Unsigned32
_Ats3020AbsEnergyActive_Object=MibTableColumn
ats3020AbsEnergyActive=_Ats3020AbsEnergyActive_Object((1,3,6,1,4,1,28507,40,1,5,1,2,1,3),_Ats3020AbsEnergyActive_Type())
ats3020AbsEnergyActive.setMaxAccess(_C)
if mibBuilder.loadTexts:ats3020AbsEnergyActive.setStatus(_B)
if mibBuilder.loadTexts:ats3020AbsEnergyActive.setUnits(_E)
_Ats3020PowerActive_Type=Integer32
_Ats3020PowerActive_Object=MibTableColumn
ats3020PowerActive=_Ats3020PowerActive_Object((1,3,6,1,4,1,28507,40,1,5,1,2,1,4),_Ats3020PowerActive_Type())
ats3020PowerActive.setMaxAccess(_C)
if mibBuilder.loadTexts:ats3020PowerActive.setStatus(_B)
if mibBuilder.loadTexts:ats3020PowerActive.setUnits('W')
_Ats3020Current_Type=Unsigned32
_Ats3020Current_Object=MibTableColumn
ats3020Current=_Ats3020Current_Object((1,3,6,1,4,1,28507,40,1,5,1,2,1,5),_Ats3020Current_Type())
ats3020Current.setMaxAccess(_C)
if mibBuilder.loadTexts:ats3020Current.setStatus(_B)
if mibBuilder.loadTexts:ats3020Current.setUnits('mA')
_Ats3020Voltage_Type=Unsigned32
_Ats3020Voltage_Object=MibTableColumn
ats3020Voltage=_Ats3020Voltage_Object((1,3,6,1,4,1,28507,40,1,5,1,2,1,6),_Ats3020Voltage_Type())
ats3020Voltage.setMaxAccess(_C)
if mibBuilder.loadTexts:ats3020Voltage.setStatus(_B)
if mibBuilder.loadTexts:ats3020Voltage.setUnits('V')
_Ats3020Frequency_Type=Unsigned32
_Ats3020Frequency_Object=MibTableColumn
ats3020Frequency=_Ats3020Frequency_Object((1,3,6,1,4,1,28507,40,1,5,1,2,1,7),_Ats3020Frequency_Type())
ats3020Frequency.setMaxAccess(_C)
if mibBuilder.loadTexts:ats3020Frequency.setStatus(_B)
if mibBuilder.loadTexts:ats3020Frequency.setUnits('0.01 hz')
_Ats3020PowerFactor_Type=Integer32
_Ats3020PowerFactor_Object=MibTableColumn
ats3020PowerFactor=_Ats3020PowerFactor_Object((1,3,6,1,4,1,28507,40,1,5,1,2,1,8),_Ats3020PowerFactor_Type())
ats3020PowerFactor.setMaxAccess(_C)
if mibBuilder.loadTexts:ats3020PowerFactor.setStatus(_B)
if mibBuilder.loadTexts:ats3020PowerFactor.setUnits('0.001')
_Ats3020Pangle_Type=Integer32
_Ats3020Pangle_Object=MibTableColumn
ats3020Pangle=_Ats3020Pangle_Object((1,3,6,1,4,1,28507,40,1,5,1,2,1,9),_Ats3020Pangle_Type())
ats3020Pangle.setMaxAccess(_C)
if mibBuilder.loadTexts:ats3020Pangle.setStatus(_B)
if mibBuilder.loadTexts:ats3020Pangle.setUnits('0.1 degree')
_Ats3020PowerApparent_Type=Integer32
_Ats3020PowerApparent_Object=MibTableColumn
ats3020PowerApparent=_Ats3020PowerApparent_Object((1,3,6,1,4,1,28507,40,1,5,1,2,1,10),_Ats3020PowerApparent_Type())
ats3020PowerApparent.setMaxAccess(_C)
if mibBuilder.loadTexts:ats3020PowerApparent.setStatus(_B)
if mibBuilder.loadTexts:ats3020PowerApparent.setUnits('VA')
_Ats3020PowerReactive_Type=Integer32
_Ats3020PowerReactive_Object=MibTableColumn
ats3020PowerReactive=_Ats3020PowerReactive_Object((1,3,6,1,4,1,28507,40,1,5,1,2,1,11),_Ats3020PowerReactive_Type())
ats3020PowerReactive.setMaxAccess(_C)
if mibBuilder.loadTexts:ats3020PowerReactive.setStatus(_B)
if mibBuilder.loadTexts:ats3020PowerReactive.setUnits('VAR')
_Ats3020AbsEnergyReactive_Type=Unsigned32
_Ats3020AbsEnergyReactive_Object=MibTableColumn
ats3020AbsEnergyReactive=_Ats3020AbsEnergyReactive_Object((1,3,6,1,4,1,28507,40,1,5,1,2,1,12),_Ats3020AbsEnergyReactive_Type())
ats3020AbsEnergyReactive.setMaxAccess(_C)
if mibBuilder.loadTexts:ats3020AbsEnergyReactive.setStatus(_B)
if mibBuilder.loadTexts:ats3020AbsEnergyReactive.setUnits(_F)
_Ats3020AbsEnergyActiveResettable_Type=Unsigned32
_Ats3020AbsEnergyActiveResettable_Object=MibTableColumn
ats3020AbsEnergyActiveResettable=_Ats3020AbsEnergyActiveResettable_Object((1,3,6,1,4,1,28507,40,1,5,1,2,1,13),_Ats3020AbsEnergyActiveResettable_Type())
ats3020AbsEnergyActiveResettable.setMaxAccess(_C)
if mibBuilder.loadTexts:ats3020AbsEnergyActiveResettable.setStatus(_B)
if mibBuilder.loadTexts:ats3020AbsEnergyActiveResettable.setUnits(_E)
_Ats3020AbsEnergyReactiveResettable_Type=Unsigned32
_Ats3020AbsEnergyReactiveResettable_Object=MibTableColumn
ats3020AbsEnergyReactiveResettable=_Ats3020AbsEnergyReactiveResettable_Object((1,3,6,1,4,1,28507,40,1,5,1,2,1,14),_Ats3020AbsEnergyReactiveResettable_Type())
ats3020AbsEnergyReactiveResettable.setMaxAccess(_C)
if mibBuilder.loadTexts:ats3020AbsEnergyReactiveResettable.setStatus(_B)
if mibBuilder.loadTexts:ats3020AbsEnergyReactiveResettable.setUnits(_F)
_Ats3020ResetTime_Type=Unsigned32
_Ats3020ResetTime_Object=MibTableColumn
ats3020ResetTime=_Ats3020ResetTime_Object((1,3,6,1,4,1,28507,40,1,5,1,2,1,15),_Ats3020ResetTime_Type())
ats3020ResetTime.setMaxAccess(_C)
if mibBuilder.loadTexts:ats3020ResetTime.setStatus(_B)
if mibBuilder.loadTexts:ats3020ResetTime.setUnits('s')
_Ats3020ForwEnergyActive_Type=Unsigned32
_Ats3020ForwEnergyActive_Object=MibTableColumn
ats3020ForwEnergyActive=_Ats3020ForwEnergyActive_Object((1,3,6,1,4,1,28507,40,1,5,1,2,1,16),_Ats3020ForwEnergyActive_Type())
ats3020ForwEnergyActive.setMaxAccess(_C)
if mibBuilder.loadTexts:ats3020ForwEnergyActive.setStatus(_B)
if mibBuilder.loadTexts:ats3020ForwEnergyActive.setUnits(_E)
_Ats3020ForwEnergyReactive_Type=Unsigned32
_Ats3020ForwEnergyReactive_Object=MibTableColumn
ats3020ForwEnergyReactive=_Ats3020ForwEnergyReactive_Object((1,3,6,1,4,1,28507,40,1,5,1,2,1,17),_Ats3020ForwEnergyReactive_Type())
ats3020ForwEnergyReactive.setMaxAccess(_C)
if mibBuilder.loadTexts:ats3020ForwEnergyReactive.setStatus(_B)
if mibBuilder.loadTexts:ats3020ForwEnergyReactive.setUnits(_F)
_Ats3020ForwEnergyActiveResettable_Type=Unsigned32
_Ats3020ForwEnergyActiveResettable_Object=MibTableColumn
ats3020ForwEnergyActiveResettable=_Ats3020ForwEnergyActiveResettable_Object((1,3,6,1,4,1,28507,40,1,5,1,2,1,18),_Ats3020ForwEnergyActiveResettable_Type())
ats3020ForwEnergyActiveResettable.setMaxAccess(_C)
if mibBuilder.loadTexts:ats3020ForwEnergyActiveResettable.setStatus(_B)
if mibBuilder.loadTexts:ats3020ForwEnergyActiveResettable.setUnits(_E)
_Ats3020ForwEnergyReactiveResettable_Type=Unsigned32
_Ats3020ForwEnergyReactiveResettable_Object=MibTableColumn
ats3020ForwEnergyReactiveResettable=_Ats3020ForwEnergyReactiveResettable_Object((1,3,6,1,4,1,28507,40,1,5,1,2,1,19),_Ats3020ForwEnergyReactiveResettable_Type())
ats3020ForwEnergyReactiveResettable.setMaxAccess(_C)
if mibBuilder.loadTexts:ats3020ForwEnergyReactiveResettable.setStatus(_B)
if mibBuilder.loadTexts:ats3020ForwEnergyReactiveResettable.setUnits(_F)
_Ats3020RevEnergyActive_Type=Unsigned32
_Ats3020RevEnergyActive_Object=MibTableColumn
ats3020RevEnergyActive=_Ats3020RevEnergyActive_Object((1,3,6,1,4,1,28507,40,1,5,1,2,1,20),_Ats3020RevEnergyActive_Type())
ats3020RevEnergyActive.setMaxAccess(_C)
if mibBuilder.loadTexts:ats3020RevEnergyActive.setStatus(_B)
if mibBuilder.loadTexts:ats3020RevEnergyActive.setUnits(_E)
_Ats3020RevEnergyReactive_Type=Unsigned32
_Ats3020RevEnergyReactive_Object=MibTableColumn
ats3020RevEnergyReactive=_Ats3020RevEnergyReactive_Object((1,3,6,1,4,1,28507,40,1,5,1,2,1,21),_Ats3020RevEnergyReactive_Type())
ats3020RevEnergyReactive.setMaxAccess(_C)
if mibBuilder.loadTexts:ats3020RevEnergyReactive.setStatus(_B)
if mibBuilder.loadTexts:ats3020RevEnergyReactive.setUnits(_F)
_Ats3020RevEnergyActiveResettable_Type=Unsigned32
_Ats3020RevEnergyActiveResettable_Object=MibTableColumn
ats3020RevEnergyActiveResettable=_Ats3020RevEnergyActiveResettable_Object((1,3,6,1,4,1,28507,40,1,5,1,2,1,22),_Ats3020RevEnergyActiveResettable_Type())
ats3020RevEnergyActiveResettable.setMaxAccess(_C)
if mibBuilder.loadTexts:ats3020RevEnergyActiveResettable.setStatus(_B)
if mibBuilder.loadTexts:ats3020RevEnergyActiveResettable.setUnits(_E)
_Ats3020RevEnergyReactiveResettable_Type=Unsigned32
_Ats3020RevEnergyReactiveResettable_Object=MibTableColumn
ats3020RevEnergyReactiveResettable=_Ats3020RevEnergyReactiveResettable_Object((1,3,6,1,4,1,28507,40,1,5,1,2,1,23),_Ats3020RevEnergyReactiveResettable_Type())
ats3020RevEnergyReactiveResettable.setMaxAccess(_C)
if mibBuilder.loadTexts:ats3020RevEnergyReactiveResettable.setStatus(_B)
if mibBuilder.loadTexts:ats3020RevEnergyReactiveResettable.setUnits(_F)
_Ats3020PowerInfo_ObjectIdentity=ObjectIdentity
ats3020PowerInfo=_Ats3020PowerInfo_ObjectIdentity((1,3,6,1,4,1,28507,40,1,5,11))
_Ats3020PrimPowAvail_Type=Integer32
_Ats3020PrimPowAvail_Object=MibScalar
ats3020PrimPowAvail=_Ats3020PrimPowAvail_Object((1,3,6,1,4,1,28507,40,1,5,11,1),_Ats3020PrimPowAvail_Type())
ats3020PrimPowAvail.setMaxAccess(_C)
if mibBuilder.loadTexts:ats3020PrimPowAvail.setStatus(_B)
_Ats3020SecPowAvail_Type=Integer32
_Ats3020SecPowAvail_Object=MibScalar
ats3020SecPowAvail=_Ats3020SecPowAvail_Object((1,3,6,1,4,1,28507,40,1,5,11,2),_Ats3020SecPowAvail_Type())
ats3020SecPowAvail.setMaxAccess(_C)
if mibBuilder.loadTexts:ats3020SecPowAvail.setStatus(_B)
_Ats3020PowerSelect_Type=Integer32
_Ats3020PowerSelect_Object=MibScalar
ats3020PowerSelect=_Ats3020PowerSelect_Object((1,3,6,1,4,1,28507,40,1,5,11,4),_Ats3020PowerSelect_Type())
ats3020PowerSelect.setMaxAccess(_C)
if mibBuilder.loadTexts:ats3020PowerSelect.setStatus(_B)
_Ats3020ExtSensors_ObjectIdentity=ObjectIdentity
ats3020ExtSensors=_Ats3020ExtSensors_ObjectIdentity((1,3,6,1,4,1,28507,40,1,6))
_Ats3020SensorTable_Object=MibTable
ats3020SensorTable=_Ats3020SensorTable_Object((1,3,6,1,4,1,28507,40,1,6,1))
if mibBuilder.loadTexts:ats3020SensorTable.setStatus(_B)
_Ats3020SensorEntry_Object=MibTableRow
ats3020SensorEntry=_Ats3020SensorEntry_Object((1,3,6,1,4,1,28507,40,1,6,1,1))
ats3020SensorEntry.setIndexNames((0,_A,_Y))
if mibBuilder.loadTexts:ats3020SensorEntry.setStatus(_B)
class _Ats3020SensorIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_Ats3020SensorIndex_Type.__name__=_D
_Ats3020SensorIndex_Object=MibTableColumn
ats3020SensorIndex=_Ats3020SensorIndex_Object((1,3,6,1,4,1,28507,40,1,6,1,1,1),_Ats3020SensorIndex_Type())
ats3020SensorIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:ats3020SensorIndex.setStatus(_B)
_Ats3020TempSensor_Type=Integer32
_Ats3020TempSensor_Object=MibTableColumn
ats3020TempSensor=_Ats3020TempSensor_Object((1,3,6,1,4,1,28507,40,1,6,1,1,2),_Ats3020TempSensor_Type())
ats3020TempSensor.setMaxAccess(_C)
if mibBuilder.loadTexts:ats3020TempSensor.setStatus(_B)
if mibBuilder.loadTexts:ats3020TempSensor.setUnits('0.1 degree Celsius')
_Ats3020HygroSensor_Type=Integer32
_Ats3020HygroSensor_Object=MibTableColumn
ats3020HygroSensor=_Ats3020HygroSensor_Object((1,3,6,1,4,1,28507,40,1,6,1,1,3),_Ats3020HygroSensor_Type())
ats3020HygroSensor.setMaxAccess(_C)
if mibBuilder.loadTexts:ats3020HygroSensor.setStatus(_B)
if mibBuilder.loadTexts:ats3020HygroSensor.setUnits('0.1 percent humidity')
class _Ats3020InputSensor_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('off',0),('on',1)))
_Ats3020InputSensor_Type.__name__=_D
_Ats3020InputSensor_Object=MibTableColumn
ats3020InputSensor=_Ats3020InputSensor_Object((1,3,6,1,4,1,28507,40,1,6,1,1,4),_Ats3020InputSensor_Type())
ats3020InputSensor.setMaxAccess(_C)
if mibBuilder.loadTexts:ats3020InputSensor.setStatus(_B)
_Ats3020Conf_ObjectIdentity=ObjectIdentity
ats3020Conf=_Ats3020Conf_ObjectIdentity((1,3,6,1,4,1,28507,40,3))
_Ats3020Groups_ObjectIdentity=ObjectIdentity
ats3020Groups=_Ats3020Groups_ObjectIdentity((1,3,6,1,4,1,28507,40,3,1))
_Ats3020Compls_ObjectIdentity=ObjectIdentity
ats3020Compls=_Ats3020Compls_ObjectIdentity((1,3,6,1,4,1,28507,40,3,2))
ats3020BasicGroup=ObjectGroup((1,3,6,1,4,1,28507,40,3,1,1))
ats3020BasicGroup.setObjects(*((_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_f),(_A,_g),(_A,_M),(_A,_N),(_A,_h),(_A,_i),(_A,_j),(_A,_k),(_A,_l),(_A,_m),(_A,_n),(_A,_o),(_A,_p),(_A,_q),(_A,_r),(_A,_s),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T)))
if mibBuilder.loadTexts:ats3020BasicGroup.setStatus(_B)
ats3020PrimaryPowerChangeEvt=NotificationType((1,3,6,1,4,1,28507,40,0,1))
ats3020PrimaryPowerChangeEvt.setObjects((_A,_O))
if mibBuilder.loadTexts:ats3020PrimaryPowerChangeEvt.setStatus(_B)
ats3020SecondaryPowerChangeEvt=NotificationType((1,3,6,1,4,1,28507,40,0,2))
ats3020SecondaryPowerChangeEvt.setObjects((_A,_P))
if mibBuilder.loadTexts:ats3020SecondaryPowerChangeEvt.setStatus(_B)
ats3020PowerSelectEvt=NotificationType((1,3,6,1,4,1,28507,40,0,3))
ats3020PowerSelectEvt.setObjects((_A,_Q))
if mibBuilder.loadTexts:ats3020PowerSelectEvt.setStatus(_B)
ats3020TempEvtSen1=NotificationType((1,3,6,1,4,1,28507,40,0,4))
ats3020TempEvtSen1.setObjects((_A,_R))
if mibBuilder.loadTexts:ats3020TempEvtSen1.setStatus(_B)
ats3020HygroEvtSen1=NotificationType((1,3,6,1,4,1,28507,40,0,5))
ats3020HygroEvtSen1.setObjects((_A,_S))
if mibBuilder.loadTexts:ats3020HygroEvtSen1.setStatus(_B)
ats3020InputEvtSen1=NotificationType((1,3,6,1,4,1,28507,40,0,6))
ats3020InputEvtSen1.setObjects((_A,_T))
if mibBuilder.loadTexts:ats3020InputEvtSen1.setStatus(_B)
ats3020AmperageEvt1=NotificationType((1,3,6,1,4,1,28507,40,0,7))
ats3020AmperageEvt1.setObjects(*((_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N)))
if mibBuilder.loadTexts:ats3020AmperageEvt1.setStatus(_B)
ats3020NotificationGroup=NotificationGroup((1,3,6,1,4,1,28507,40,3,1,2))
ats3020NotificationGroup.setObjects(*((_A,_t),(_A,_u),(_A,_v),(_A,_w),(_A,_x),(_A,_y),(_A,_z)))
if mibBuilder.loadTexts:ats3020NotificationGroup.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'gudeads':gudeads,'gadsATS3020':gadsATS3020,'ats3020Events':ats3020Events,_t:ats3020PrimaryPowerChangeEvt,_u:ats3020SecondaryPowerChangeEvt,_v:ats3020PowerSelectEvt,_w:ats3020TempEvtSen1,_x:ats3020HygroEvtSen1,_y:ats3020InputEvtSen1,_z:ats3020AmperageEvt1,'ats3020Objects':ats3020Objects,'ats3020CommonConfig':ats3020CommonConfig,'ats3020SNMPaccess':ats3020SNMPaccess,_Z:ats3020TrapCtrl,'ats3020TrapIPTable':ats3020TrapIPTable,'ats3020TrapIPEntry':ats3020TrapIPEntry,_W:ats3020TrapIPIndex,_a:ats3020TrapAddr,'ats3020IntActors':ats3020IntActors,_b:ats3020Buzzer,'ats3020IntSensors':ats3020IntSensors,'ats3020PowerChan':ats3020PowerChan,_c:ats3020ActivePowerChan,'ats3020PowerTable':ats3020PowerTable,'ats3020PowerEntry':ats3020PowerEntry,_X:ats3020PowerIndex,_d:ats3020ChanStatus,_e:ats3020AbsEnergyActive,_I:ats3020PowerActive,_J:ats3020Current,_K:ats3020Voltage,_L:ats3020Frequency,_f:ats3020PowerFactor,_g:ats3020Pangle,_M:ats3020PowerApparent,_N:ats3020PowerReactive,_h:ats3020AbsEnergyReactive,_i:ats3020AbsEnergyActiveResettable,_j:ats3020AbsEnergyReactiveResettable,_k:ats3020ResetTime,_l:ats3020ForwEnergyActive,_m:ats3020ForwEnergyReactive,_n:ats3020ForwEnergyActiveResettable,_o:ats3020ForwEnergyReactiveResettable,_p:ats3020RevEnergyActive,_q:ats3020RevEnergyReactive,_r:ats3020RevEnergyActiveResettable,_s:ats3020RevEnergyReactiveResettable,'ats3020PowerInfo':ats3020PowerInfo,_O:ats3020PrimPowAvail,_P:ats3020SecPowAvail,_Q:ats3020PowerSelect,'ats3020ExtSensors':ats3020ExtSensors,'ats3020SensorTable':ats3020SensorTable,'ats3020SensorEntry':ats3020SensorEntry,_Y:ats3020SensorIndex,_R:ats3020TempSensor,_S:ats3020HygroSensor,_T:ats3020InputSensor,'ats3020Conf':ats3020Conf,'ats3020Groups':ats3020Groups,'ats3020BasicGroup':ats3020BasicGroup,'ats3020NotificationGroup':ats3020NotificationGroup,'ats3020Compls':ats3020Compls})