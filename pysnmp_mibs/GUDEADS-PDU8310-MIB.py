_b='pdu8310AmperageEvt1'
_a='pdu8310ResetTime'
_Z='pdu8310EnergyReactiveResettable'
_Y='pdu8310EnergyActiveResettable'
_X='pdu8310EnergyReactive'
_W='pdu8310Pangle'
_V='pdu8310PowerFactor'
_U='pdu8310EnergyActive'
_T='pdu8310ChanStatus'
_S='pdu8310ActivePowerChan'
_R='pdu8310TrapAddr'
_Q='pdu8310TrapCtrl'
_P='pdu8310PowerIndex'
_O='not-accessible'
_N='pdu8310TrapIPIndex'
_M='read-write'
_L='Unsigned32'
_K='OctetString'
_J='pdu8310PowerReactive'
_I='pdu8310PowerApparent'
_H='pdu8310Frequency'
_G='pdu8310Voltage'
_F='pdu8310Current'
_E='pdu8310PowerActive'
_D='Integer32'
_C='read-only'
_B='current'
_A='GUDEADS-PDU8310-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_K,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_L,'enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
gudeads=ModuleIdentity((1,3,6,1,4,1,28507))
if mibBuilder.loadTexts:gudeads.setRevisions(('2007-03-05 13:56',))
_GadsPDU8310_ObjectIdentity=ObjectIdentity
gadsPDU8310=_GadsPDU8310_ObjectIdentity((1,3,6,1,4,1,28507,27))
_Events_ObjectIdentity=ObjectIdentity
events=_Events_ObjectIdentity((1,3,6,1,4,1,28507,27,0))
_Pdu8310Objects_ObjectIdentity=ObjectIdentity
pdu8310Objects=_Pdu8310Objects_ObjectIdentity((1,3,6,1,4,1,28507,27,1))
_Pdu8310CommonConfig_ObjectIdentity=ObjectIdentity
pdu8310CommonConfig=_Pdu8310CommonConfig_ObjectIdentity((1,3,6,1,4,1,28507,27,1,1))
_Pdu8310SNMPaccess_ObjectIdentity=ObjectIdentity
pdu8310SNMPaccess=_Pdu8310SNMPaccess_ObjectIdentity((1,3,6,1,4,1,28507,27,1,1,1))
class _Pdu8310TrapCtrl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_Pdu8310TrapCtrl_Type.__name__=_D
_Pdu8310TrapCtrl_Object=MibScalar
pdu8310TrapCtrl=_Pdu8310TrapCtrl_Object((1,3,6,1,4,1,28507,27,1,1,1,1),_Pdu8310TrapCtrl_Type())
pdu8310TrapCtrl.setMaxAccess(_M)
if mibBuilder.loadTexts:pdu8310TrapCtrl.setStatus(_B)
_Pdu8310TrapIPTable_Object=MibTable
pdu8310TrapIPTable=_Pdu8310TrapIPTable_Object((1,3,6,1,4,1,28507,27,1,1,1,2))
if mibBuilder.loadTexts:pdu8310TrapIPTable.setStatus(_B)
_Pdu8310TrapIPEntry_Object=MibTableRow
pdu8310TrapIPEntry=_Pdu8310TrapIPEntry_Object((1,3,6,1,4,1,28507,27,1,1,1,2,1))
pdu8310TrapIPEntry.setIndexNames((0,_A,_N))
if mibBuilder.loadTexts:pdu8310TrapIPEntry.setStatus(_B)
class _Pdu8310TrapIPIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_Pdu8310TrapIPIndex_Type.__name__=_D
_Pdu8310TrapIPIndex_Object=MibTableColumn
pdu8310TrapIPIndex=_Pdu8310TrapIPIndex_Object((1,3,6,1,4,1,28507,27,1,1,1,2,1,1),_Pdu8310TrapIPIndex_Type())
pdu8310TrapIPIndex.setMaxAccess(_O)
if mibBuilder.loadTexts:pdu8310TrapIPIndex.setStatus(_B)
class _Pdu8310TrapAddr_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,99))
_Pdu8310TrapAddr_Type.__name__=_K
_Pdu8310TrapAddr_Object=MibTableColumn
pdu8310TrapAddr=_Pdu8310TrapAddr_Object((1,3,6,1,4,1,28507,27,1,1,1,2,1,2),_Pdu8310TrapAddr_Type())
pdu8310TrapAddr.setMaxAccess(_M)
if mibBuilder.loadTexts:pdu8310TrapAddr.setStatus(_B)
_Pdu8310DeviceConfig_ObjectIdentity=ObjectIdentity
pdu8310DeviceConfig=_Pdu8310DeviceConfig_ObjectIdentity((1,3,6,1,4,1,28507,27,1,2))
_Pdu8310IntActors_ObjectIdentity=ObjectIdentity
pdu8310IntActors=_Pdu8310IntActors_ObjectIdentity((1,3,6,1,4,1,28507,27,1,3))
_Pdu8310ExtActors_ObjectIdentity=ObjectIdentity
pdu8310ExtActors=_Pdu8310ExtActors_ObjectIdentity((1,3,6,1,4,1,28507,27,1,4))
_Pdu8310IntSensors_ObjectIdentity=ObjectIdentity
pdu8310IntSensors=_Pdu8310IntSensors_ObjectIdentity((1,3,6,1,4,1,28507,27,1,5))
_Pdu8310PowerChan_ObjectIdentity=ObjectIdentity
pdu8310PowerChan=_Pdu8310PowerChan_ObjectIdentity((1,3,6,1,4,1,28507,27,1,5,1))
class _Pdu8310ActivePowerChan_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1))
_Pdu8310ActivePowerChan_Type.__name__=_L
_Pdu8310ActivePowerChan_Object=MibScalar
pdu8310ActivePowerChan=_Pdu8310ActivePowerChan_Object((1,3,6,1,4,1,28507,27,1,5,1,1),_Pdu8310ActivePowerChan_Type())
pdu8310ActivePowerChan.setMaxAccess(_C)
if mibBuilder.loadTexts:pdu8310ActivePowerChan.setStatus(_B)
_Pdu8310PowerTable_Object=MibTable
pdu8310PowerTable=_Pdu8310PowerTable_Object((1,3,6,1,4,1,28507,27,1,5,1,2))
if mibBuilder.loadTexts:pdu8310PowerTable.setStatus(_B)
_Pdu8310PowerEntry_Object=MibTableRow
pdu8310PowerEntry=_Pdu8310PowerEntry_Object((1,3,6,1,4,1,28507,27,1,5,1,2,1))
pdu8310PowerEntry.setIndexNames((0,_A,_P))
if mibBuilder.loadTexts:pdu8310PowerEntry.setStatus(_B)
class _Pdu8310PowerIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1))
_Pdu8310PowerIndex_Type.__name__=_D
_Pdu8310PowerIndex_Object=MibTableColumn
pdu8310PowerIndex=_Pdu8310PowerIndex_Object((1,3,6,1,4,1,28507,27,1,5,1,2,1,1),_Pdu8310PowerIndex_Type())
pdu8310PowerIndex.setMaxAccess(_O)
if mibBuilder.loadTexts:pdu8310PowerIndex.setStatus(_B)
class _Pdu8310ChanStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Pdu8310ChanStatus_Type.__name__=_D
_Pdu8310ChanStatus_Object=MibTableColumn
pdu8310ChanStatus=_Pdu8310ChanStatus_Object((1,3,6,1,4,1,28507,27,1,5,1,2,1,2),_Pdu8310ChanStatus_Type())
pdu8310ChanStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:pdu8310ChanStatus.setStatus(_B)
_Pdu8310EnergyActive_Type=Unsigned32
_Pdu8310EnergyActive_Object=MibTableColumn
pdu8310EnergyActive=_Pdu8310EnergyActive_Object((1,3,6,1,4,1,28507,27,1,5,1,2,1,3),_Pdu8310EnergyActive_Type())
pdu8310EnergyActive.setMaxAccess(_C)
if mibBuilder.loadTexts:pdu8310EnergyActive.setStatus(_B)
if mibBuilder.loadTexts:pdu8310EnergyActive.setUnits('Wh')
_Pdu8310PowerActive_Type=Unsigned32
_Pdu8310PowerActive_Object=MibTableColumn
pdu8310PowerActive=_Pdu8310PowerActive_Object((1,3,6,1,4,1,28507,27,1,5,1,2,1,4),_Pdu8310PowerActive_Type())
pdu8310PowerActive.setMaxAccess(_C)
if mibBuilder.loadTexts:pdu8310PowerActive.setStatus(_B)
if mibBuilder.loadTexts:pdu8310PowerActive.setUnits('W')
_Pdu8310Current_Type=Unsigned32
_Pdu8310Current_Object=MibTableColumn
pdu8310Current=_Pdu8310Current_Object((1,3,6,1,4,1,28507,27,1,5,1,2,1,5),_Pdu8310Current_Type())
pdu8310Current.setMaxAccess(_C)
if mibBuilder.loadTexts:pdu8310Current.setStatus(_B)
if mibBuilder.loadTexts:pdu8310Current.setUnits('mA')
_Pdu8310Voltage_Type=Unsigned32
_Pdu8310Voltage_Object=MibTableColumn
pdu8310Voltage=_Pdu8310Voltage_Object((1,3,6,1,4,1,28507,27,1,5,1,2,1,6),_Pdu8310Voltage_Type())
pdu8310Voltage.setMaxAccess(_C)
if mibBuilder.loadTexts:pdu8310Voltage.setStatus(_B)
if mibBuilder.loadTexts:pdu8310Voltage.setUnits('V')
_Pdu8310Frequency_Type=Unsigned32
_Pdu8310Frequency_Object=MibTableColumn
pdu8310Frequency=_Pdu8310Frequency_Object((1,3,6,1,4,1,28507,27,1,5,1,2,1,7),_Pdu8310Frequency_Type())
pdu8310Frequency.setMaxAccess(_C)
if mibBuilder.loadTexts:pdu8310Frequency.setStatus(_B)
if mibBuilder.loadTexts:pdu8310Frequency.setUnits('0.01 hz')
_Pdu8310PowerFactor_Type=Integer32
_Pdu8310PowerFactor_Object=MibTableColumn
pdu8310PowerFactor=_Pdu8310PowerFactor_Object((1,3,6,1,4,1,28507,27,1,5,1,2,1,8),_Pdu8310PowerFactor_Type())
pdu8310PowerFactor.setMaxAccess(_C)
if mibBuilder.loadTexts:pdu8310PowerFactor.setStatus(_B)
if mibBuilder.loadTexts:pdu8310PowerFactor.setUnits('0.001')
_Pdu8310Pangle_Type=Integer32
_Pdu8310Pangle_Object=MibTableColumn
pdu8310Pangle=_Pdu8310Pangle_Object((1,3,6,1,4,1,28507,27,1,5,1,2,1,9),_Pdu8310Pangle_Type())
pdu8310Pangle.setMaxAccess(_C)
if mibBuilder.loadTexts:pdu8310Pangle.setStatus(_B)
if mibBuilder.loadTexts:pdu8310Pangle.setUnits('0.1 degree')
_Pdu8310PowerApparent_Type=Unsigned32
_Pdu8310PowerApparent_Object=MibTableColumn
pdu8310PowerApparent=_Pdu8310PowerApparent_Object((1,3,6,1,4,1,28507,27,1,5,1,2,1,10),_Pdu8310PowerApparent_Type())
pdu8310PowerApparent.setMaxAccess(_C)
if mibBuilder.loadTexts:pdu8310PowerApparent.setStatus(_B)
if mibBuilder.loadTexts:pdu8310PowerApparent.setUnits('VA')
_Pdu8310PowerReactive_Type=Unsigned32
_Pdu8310PowerReactive_Object=MibTableColumn
pdu8310PowerReactive=_Pdu8310PowerReactive_Object((1,3,6,1,4,1,28507,27,1,5,1,2,1,11),_Pdu8310PowerReactive_Type())
pdu8310PowerReactive.setMaxAccess(_C)
if mibBuilder.loadTexts:pdu8310PowerReactive.setStatus(_B)
if mibBuilder.loadTexts:pdu8310PowerReactive.setUnits('VAR')
_Pdu8310EnergyReactive_Type=Unsigned32
_Pdu8310EnergyReactive_Object=MibTableColumn
pdu8310EnergyReactive=_Pdu8310EnergyReactive_Object((1,3,6,1,4,1,28507,27,1,5,1,2,1,12),_Pdu8310EnergyReactive_Type())
pdu8310EnergyReactive.setMaxAccess(_C)
if mibBuilder.loadTexts:pdu8310EnergyReactive.setStatus(_B)
if mibBuilder.loadTexts:pdu8310EnergyReactive.setUnits('VARh')
_Pdu8310EnergyActiveResettable_Type=Unsigned32
_Pdu8310EnergyActiveResettable_Object=MibTableColumn
pdu8310EnergyActiveResettable=_Pdu8310EnergyActiveResettable_Object((1,3,6,1,4,1,28507,27,1,5,1,2,1,13),_Pdu8310EnergyActiveResettable_Type())
pdu8310EnergyActiveResettable.setMaxAccess(_C)
if mibBuilder.loadTexts:pdu8310EnergyActiveResettable.setStatus(_B)
if mibBuilder.loadTexts:pdu8310EnergyActiveResettable.setUnits('Wh')
_Pdu8310EnergyReactiveResettable_Type=Unsigned32
_Pdu8310EnergyReactiveResettable_Object=MibTableColumn
pdu8310EnergyReactiveResettable=_Pdu8310EnergyReactiveResettable_Object((1,3,6,1,4,1,28507,27,1,5,1,2,1,14),_Pdu8310EnergyReactiveResettable_Type())
pdu8310EnergyReactiveResettable.setMaxAccess(_C)
if mibBuilder.loadTexts:pdu8310EnergyReactiveResettable.setStatus(_B)
if mibBuilder.loadTexts:pdu8310EnergyReactiveResettable.setUnits('VARh')
_Pdu8310ResetTime_Type=Unsigned32
_Pdu8310ResetTime_Object=MibTableColumn
pdu8310ResetTime=_Pdu8310ResetTime_Object((1,3,6,1,4,1,28507,27,1,5,1,2,1,15),_Pdu8310ResetTime_Type())
pdu8310ResetTime.setMaxAccess(_C)
if mibBuilder.loadTexts:pdu8310ResetTime.setStatus(_B)
if mibBuilder.loadTexts:pdu8310ResetTime.setUnits('s')
_Pdu8310ExtSensors_ObjectIdentity=ObjectIdentity
pdu8310ExtSensors=_Pdu8310ExtSensors_ObjectIdentity((1,3,6,1,4,1,28507,27,1,6))
_Pdu8310Conf_ObjectIdentity=ObjectIdentity
pdu8310Conf=_Pdu8310Conf_ObjectIdentity((1,3,6,1,4,1,28507,27,2))
_Pdu8310Groups_ObjectIdentity=ObjectIdentity
pdu8310Groups=_Pdu8310Groups_ObjectIdentity((1,3,6,1,4,1,28507,27,2,1))
_Pdu8310Compls_ObjectIdentity=ObjectIdentity
pdu8310Compls=_Pdu8310Compls_ObjectIdentity((1,3,6,1,4,1,28507,27,2,2))
pdu8310BasicGroup=ObjectGroup((1,3,6,1,4,1,28507,27,2,1,1))
pdu8310BasicGroup.setObjects(*((_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_V),(_A,_W),(_A,_I),(_A,_J),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a)))
if mibBuilder.loadTexts:pdu8310BasicGroup.setStatus(_B)
pdu8310AmperageEvt1=NotificationType((1,3,6,1,4,1,28507,27,0,1))
pdu8310AmperageEvt1.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J)))
if mibBuilder.loadTexts:pdu8310AmperageEvt1.setStatus(_B)
pdu8310NotificationGroup=NotificationGroup((1,3,6,1,4,1,28507,27,2,1,2))
pdu8310NotificationGroup.setObjects((_A,_b))
if mibBuilder.loadTexts:pdu8310NotificationGroup.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'gudeads':gudeads,'gadsPDU8310':gadsPDU8310,'events':events,_b:pdu8310AmperageEvt1,'pdu8310Objects':pdu8310Objects,'pdu8310CommonConfig':pdu8310CommonConfig,'pdu8310SNMPaccess':pdu8310SNMPaccess,_Q:pdu8310TrapCtrl,'pdu8310TrapIPTable':pdu8310TrapIPTable,'pdu8310TrapIPEntry':pdu8310TrapIPEntry,_N:pdu8310TrapIPIndex,_R:pdu8310TrapAddr,'pdu8310DeviceConfig':pdu8310DeviceConfig,'pdu8310IntActors':pdu8310IntActors,'pdu8310ExtActors':pdu8310ExtActors,'pdu8310IntSensors':pdu8310IntSensors,'pdu8310PowerChan':pdu8310PowerChan,_S:pdu8310ActivePowerChan,'pdu8310PowerTable':pdu8310PowerTable,'pdu8310PowerEntry':pdu8310PowerEntry,_P:pdu8310PowerIndex,_T:pdu8310ChanStatus,_U:pdu8310EnergyActive,_E:pdu8310PowerActive,_F:pdu8310Current,_G:pdu8310Voltage,_H:pdu8310Frequency,_V:pdu8310PowerFactor,_W:pdu8310Pangle,_I:pdu8310PowerApparent,_J:pdu8310PowerReactive,_X:pdu8310EnergyReactive,_Y:pdu8310EnergyActiveResettable,_Z:pdu8310EnergyReactiveResettable,_a:pdu8310ResetTime,'pdu8310ExtSensors':pdu8310ExtSensors,'pdu8310Conf':pdu8310Conf,'pdu8310Groups':pdu8310Groups,'pdu8310BasicGroup':pdu8310BasicGroup,'pdu8310NotificationGroup':pdu8310NotificationGroup,'pdu8310Compls':pdu8310Compls})