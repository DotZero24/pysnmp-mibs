_V='pdu8110HygroEvtSen2'
_U='pdu8110HygroEvtSen1'
_T='pdu8110TempEvtSen2'
_S='pdu8110TempEvtSen1'
_R='pdu8110Current'
_Q='pdu8110ChanStatus'
_P='pdu8110ActivePowerChan'
_O='pdu8110TrapAddr'
_N='pdu8110TrapCtrl'
_M='pdu8110SensorIndex'
_L='pdu8110PowerIndex'
_K='pdu8110TrapIPIndex'
_J='read-write'
_I='Unsigned32'
_H='OctetString'
_G='not-accessible'
_F='pdu8110HygroSensor'
_E='pdu8110TempSensor'
_D='read-only'
_C='Integer32'
_B='GUDEADS-PDU8110-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_H,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_I,'enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
gudeads=ModuleIdentity((1,3,6,1,4,1,28507))
if mibBuilder.loadTexts:gudeads.setRevisions(('2007-03-05 13:56',))
_GadsPDU8110_ObjectIdentity=ObjectIdentity
gadsPDU8110=_GadsPDU8110_ObjectIdentity((1,3,6,1,4,1,28507,23))
_Events_ObjectIdentity=ObjectIdentity
events=_Events_ObjectIdentity((1,3,6,1,4,1,28507,23,0))
_Pdu8110Objects_ObjectIdentity=ObjectIdentity
pdu8110Objects=_Pdu8110Objects_ObjectIdentity((1,3,6,1,4,1,28507,23,1))
_Pdu8110CommonConfig_ObjectIdentity=ObjectIdentity
pdu8110CommonConfig=_Pdu8110CommonConfig_ObjectIdentity((1,3,6,1,4,1,28507,23,1,1))
_Pdu8110SNMPaccess_ObjectIdentity=ObjectIdentity
pdu8110SNMPaccess=_Pdu8110SNMPaccess_ObjectIdentity((1,3,6,1,4,1,28507,23,1,1,1))
class _Pdu8110TrapCtrl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_Pdu8110TrapCtrl_Type.__name__=_C
_Pdu8110TrapCtrl_Object=MibScalar
pdu8110TrapCtrl=_Pdu8110TrapCtrl_Object((1,3,6,1,4,1,28507,23,1,1,1,1),_Pdu8110TrapCtrl_Type())
pdu8110TrapCtrl.setMaxAccess(_J)
if mibBuilder.loadTexts:pdu8110TrapCtrl.setStatus(_A)
_Pdu8110TrapIPTable_Object=MibTable
pdu8110TrapIPTable=_Pdu8110TrapIPTable_Object((1,3,6,1,4,1,28507,23,1,1,1,2))
if mibBuilder.loadTexts:pdu8110TrapIPTable.setStatus(_A)
_Pdu8110TrapIPEntry_Object=MibTableRow
pdu8110TrapIPEntry=_Pdu8110TrapIPEntry_Object((1,3,6,1,4,1,28507,23,1,1,1,2,1))
pdu8110TrapIPEntry.setIndexNames((0,_B,_K))
if mibBuilder.loadTexts:pdu8110TrapIPEntry.setStatus(_A)
class _Pdu8110TrapIPIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_Pdu8110TrapIPIndex_Type.__name__=_C
_Pdu8110TrapIPIndex_Object=MibTableColumn
pdu8110TrapIPIndex=_Pdu8110TrapIPIndex_Object((1,3,6,1,4,1,28507,23,1,1,1,2,1,1),_Pdu8110TrapIPIndex_Type())
pdu8110TrapIPIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:pdu8110TrapIPIndex.setStatus(_A)
class _Pdu8110TrapAddr_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,99))
_Pdu8110TrapAddr_Type.__name__=_H
_Pdu8110TrapAddr_Object=MibTableColumn
pdu8110TrapAddr=_Pdu8110TrapAddr_Object((1,3,6,1,4,1,28507,23,1,1,1,2,1,2),_Pdu8110TrapAddr_Type())
pdu8110TrapAddr.setMaxAccess(_J)
if mibBuilder.loadTexts:pdu8110TrapAddr.setStatus(_A)
_Pdu8110DeviceConfig_ObjectIdentity=ObjectIdentity
pdu8110DeviceConfig=_Pdu8110DeviceConfig_ObjectIdentity((1,3,6,1,4,1,28507,23,1,2))
_Pdu8110IntActors_ObjectIdentity=ObjectIdentity
pdu8110IntActors=_Pdu8110IntActors_ObjectIdentity((1,3,6,1,4,1,28507,23,1,3))
_Pdu8110ExtActors_ObjectIdentity=ObjectIdentity
pdu8110ExtActors=_Pdu8110ExtActors_ObjectIdentity((1,3,6,1,4,1,28507,23,1,4))
_Pdu8110IntSensors_ObjectIdentity=ObjectIdentity
pdu8110IntSensors=_Pdu8110IntSensors_ObjectIdentity((1,3,6,1,4,1,28507,23,1,5))
_Pdu8110PowerChan_ObjectIdentity=ObjectIdentity
pdu8110PowerChan=_Pdu8110PowerChan_ObjectIdentity((1,3,6,1,4,1,28507,23,1,5,1))
class _Pdu8110ActivePowerChan_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_Pdu8110ActivePowerChan_Type.__name__=_I
_Pdu8110ActivePowerChan_Object=MibScalar
pdu8110ActivePowerChan=_Pdu8110ActivePowerChan_Object((1,3,6,1,4,1,28507,23,1,5,1,1),_Pdu8110ActivePowerChan_Type())
pdu8110ActivePowerChan.setMaxAccess(_D)
if mibBuilder.loadTexts:pdu8110ActivePowerChan.setStatus(_A)
_Pdu8110PowerTable_Object=MibTable
pdu8110PowerTable=_Pdu8110PowerTable_Object((1,3,6,1,4,1,28507,23,1,5,1,2))
if mibBuilder.loadTexts:pdu8110PowerTable.setStatus(_A)
_Pdu8110PowerEntry_Object=MibTableRow
pdu8110PowerEntry=_Pdu8110PowerEntry_Object((1,3,6,1,4,1,28507,23,1,5,1,2,1))
pdu8110PowerEntry.setIndexNames((0,_B,_L))
if mibBuilder.loadTexts:pdu8110PowerEntry.setStatus(_A)
class _Pdu8110PowerIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1))
_Pdu8110PowerIndex_Type.__name__=_C
_Pdu8110PowerIndex_Object=MibTableColumn
pdu8110PowerIndex=_Pdu8110PowerIndex_Object((1,3,6,1,4,1,28507,23,1,5,1,2,1,1),_Pdu8110PowerIndex_Type())
pdu8110PowerIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:pdu8110PowerIndex.setStatus(_A)
class _Pdu8110ChanStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Pdu8110ChanStatus_Type.__name__=_C
_Pdu8110ChanStatus_Object=MibTableColumn
pdu8110ChanStatus=_Pdu8110ChanStatus_Object((1,3,6,1,4,1,28507,23,1,5,1,2,1,2),_Pdu8110ChanStatus_Type())
pdu8110ChanStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:pdu8110ChanStatus.setStatus(_A)
_Pdu8110Current_Type=Unsigned32
_Pdu8110Current_Object=MibTableColumn
pdu8110Current=_Pdu8110Current_Object((1,3,6,1,4,1,28507,23,1,5,1,2,1,5),_Pdu8110Current_Type())
pdu8110Current.setMaxAccess(_D)
if mibBuilder.loadTexts:pdu8110Current.setStatus(_A)
if mibBuilder.loadTexts:pdu8110Current.setUnits('mA')
_Pdu8110ExtSensors_ObjectIdentity=ObjectIdentity
pdu8110ExtSensors=_Pdu8110ExtSensors_ObjectIdentity((1,3,6,1,4,1,28507,23,1,6))
_Pdu8110SensorTable_Object=MibTable
pdu8110SensorTable=_Pdu8110SensorTable_Object((1,3,6,1,4,1,28507,23,1,6,1))
if mibBuilder.loadTexts:pdu8110SensorTable.setStatus(_A)
_Pdu8110SensorEntry_Object=MibTableRow
pdu8110SensorEntry=_Pdu8110SensorEntry_Object((1,3,6,1,4,1,28507,23,1,6,1,1))
pdu8110SensorEntry.setIndexNames((0,_B,_M))
if mibBuilder.loadTexts:pdu8110SensorEntry.setStatus(_A)
class _Pdu8110SensorIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_Pdu8110SensorIndex_Type.__name__=_C
_Pdu8110SensorIndex_Object=MibTableColumn
pdu8110SensorIndex=_Pdu8110SensorIndex_Object((1,3,6,1,4,1,28507,23,1,6,1,1,1),_Pdu8110SensorIndex_Type())
pdu8110SensorIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:pdu8110SensorIndex.setStatus(_A)
_Pdu8110TempSensor_Type=Integer32
_Pdu8110TempSensor_Object=MibTableColumn
pdu8110TempSensor=_Pdu8110TempSensor_Object((1,3,6,1,4,1,28507,23,1,6,1,1,2),_Pdu8110TempSensor_Type())
pdu8110TempSensor.setMaxAccess(_D)
if mibBuilder.loadTexts:pdu8110TempSensor.setStatus(_A)
if mibBuilder.loadTexts:pdu8110TempSensor.setUnits('0.1 degree Celsius')
_Pdu8110HygroSensor_Type=Integer32
_Pdu8110HygroSensor_Object=MibTableColumn
pdu8110HygroSensor=_Pdu8110HygroSensor_Object((1,3,6,1,4,1,28507,23,1,6,1,1,3),_Pdu8110HygroSensor_Type())
pdu8110HygroSensor.setMaxAccess(_D)
if mibBuilder.loadTexts:pdu8110HygroSensor.setStatus(_A)
if mibBuilder.loadTexts:pdu8110HygroSensor.setUnits('0.1 percent humidity')
_Pdu8110Conf_ObjectIdentity=ObjectIdentity
pdu8110Conf=_Pdu8110Conf_ObjectIdentity((1,3,6,1,4,1,28507,23,2))
_Pdu8110Groups_ObjectIdentity=ObjectIdentity
pdu8110Groups=_Pdu8110Groups_ObjectIdentity((1,3,6,1,4,1,28507,23,2,1))
_Pdu8110Compls_ObjectIdentity=ObjectIdentity
pdu8110Compls=_Pdu8110Compls_ObjectIdentity((1,3,6,1,4,1,28507,23,2,2))
pdu8110BasicGroup=ObjectGroup((1,3,6,1,4,1,28507,23,2,1,1))
pdu8110BasicGroup.setObjects(*((_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_E),(_B,_F)))
if mibBuilder.loadTexts:pdu8110BasicGroup.setStatus(_A)
pdu8110TempEvtSen1=NotificationType((1,3,6,1,4,1,28507,23,0,1))
pdu8110TempEvtSen1.setObjects((_B,_E))
if mibBuilder.loadTexts:pdu8110TempEvtSen1.setStatus(_A)
pdu8110TempEvtSen2=NotificationType((1,3,6,1,4,1,28507,23,0,2))
pdu8110TempEvtSen2.setObjects((_B,_E))
if mibBuilder.loadTexts:pdu8110TempEvtSen2.setStatus(_A)
pdu8110HygroEvtSen1=NotificationType((1,3,6,1,4,1,28507,23,0,3))
pdu8110HygroEvtSen1.setObjects((_B,_F))
if mibBuilder.loadTexts:pdu8110HygroEvtSen1.setStatus(_A)
pdu8110HygroEvtSen2=NotificationType((1,3,6,1,4,1,28507,23,0,4))
pdu8110HygroEvtSen2.setObjects((_B,_F))
if mibBuilder.loadTexts:pdu8110HygroEvtSen2.setStatus(_A)
pdu8110NotificationGroup=NotificationGroup((1,3,6,1,4,1,28507,23,2,1,2))
pdu8110NotificationGroup.setObjects(*((_B,_S),(_B,_T),(_B,_U),(_B,_V)))
if mibBuilder.loadTexts:pdu8110NotificationGroup.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'gudeads':gudeads,'gadsPDU8110':gadsPDU8110,'events':events,_S:pdu8110TempEvtSen1,_T:pdu8110TempEvtSen2,_U:pdu8110HygroEvtSen1,_V:pdu8110HygroEvtSen2,'pdu8110Objects':pdu8110Objects,'pdu8110CommonConfig':pdu8110CommonConfig,'pdu8110SNMPaccess':pdu8110SNMPaccess,_N:pdu8110TrapCtrl,'pdu8110TrapIPTable':pdu8110TrapIPTable,'pdu8110TrapIPEntry':pdu8110TrapIPEntry,_K:pdu8110TrapIPIndex,_O:pdu8110TrapAddr,'pdu8110DeviceConfig':pdu8110DeviceConfig,'pdu8110IntActors':pdu8110IntActors,'pdu8110ExtActors':pdu8110ExtActors,'pdu8110IntSensors':pdu8110IntSensors,'pdu8110PowerChan':pdu8110PowerChan,_P:pdu8110ActivePowerChan,'pdu8110PowerTable':pdu8110PowerTable,'pdu8110PowerEntry':pdu8110PowerEntry,_L:pdu8110PowerIndex,_Q:pdu8110ChanStatus,_R:pdu8110Current,'pdu8110ExtSensors':pdu8110ExtSensors,'pdu8110SensorTable':pdu8110SensorTable,'pdu8110SensorEntry':pdu8110SensorEntry,_M:pdu8110SensorIndex,_E:pdu8110TempSensor,_F:pdu8110HygroSensor,'pdu8110Conf':pdu8110Conf,'pdu8110Groups':pdu8110Groups,'pdu8110BasicGroup':pdu8110BasicGroup,'pdu8110NotificationGroup':pdu8110NotificationGroup,'pdu8110Compls':pdu8110Compls})