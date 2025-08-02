_H='tptSlotEvent'
_G='tptSlotID'
_F='tptSlotDeviceID'
_E='slotTempIndex'
_D='TPT-BAY-MIB'
_C='OctetString'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_C,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
tpt_tpa_eventsV2,tpt_tpa_objs,tpt_tpa_unkparams=mibBuilder.importSymbols('TPT-TPAMIBS-MIB','tpt-tpa-eventsV2','tpt-tpa-objs','tpt-tpa-unkparams')
tpt_slot_objs=ModuleIdentity((1,3,6,1,4,1,10734,3,3,2,17))
if mibBuilder.loadTexts:tpt_slot_objs.setRevisions(('2016-05-25 18:54',))
class SlotStatus(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('empty',0),('active',1),('error',2)))
class SlotEvent(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('insert',0),('remove',1)))
class SlotModuleType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18)));namedValues=NamedValues(*(('type-12-port-1g-copper',1),('type-12-port-1g-sfp',2),('type-8-port-10g-sfp',3),('type-2-port-40g-sfp',4),('type-6100',5),('type-5100',6),('type-2500',7),('type-1400',8),('type-660',9),('type-330',10),('type-110',11),('type-10',12),('type-empty',13),('type-8-port-1g-copper-bypass',14),('type-4-port-1g-sfp-sr-bypass',15),('type-4-port-1g-sfp-lr-bypass',16),('type-4-port-10g-sfp-sr-bypass',17),('type-4-port-10g-sfp-lr-bypass',18)))
_SlotTempTable_Object=MibTable
slotTempTable=_SlotTempTable_Object((1,3,6,1,4,1,10734,3,3,2,17,1))
if mibBuilder.loadTexts:slotTempTable.setStatus(_A)
_SlotTempEntry_Object=MibTableRow
slotTempEntry=_SlotTempEntry_Object((1,3,6,1,4,1,10734,3,3,2,17,1,1))
slotTempEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:slotTempEntry.setStatus(_A)
_SlotTempIndex_Type=Unsigned32
_SlotTempIndex_Object=MibTableColumn
slotTempIndex=_SlotTempIndex_Object((1,3,6,1,4,1,10734,3,3,2,17,1,1,1),_SlotTempIndex_Type())
slotTempIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:slotTempIndex.setStatus(_A)
class _SlotName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_SlotName_Type.__name__=_C
_SlotName_Object=MibTableColumn
slotName=_SlotName_Object((1,3,6,1,4,1,10734,3,3,2,17,1,1,2),_SlotName_Type())
slotName.setMaxAccess(_B)
if mibBuilder.loadTexts:slotName.setStatus(_A)
class _SlotModuleName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_SlotModuleName_Type.__name__=_C
_SlotModuleName_Object=MibTableColumn
slotModuleName=_SlotModuleName_Object((1,3,6,1,4,1,10734,3,3,2,17,1,1,3),_SlotModuleName_Type())
slotModuleName.setMaxAccess(_B)
if mibBuilder.loadTexts:slotModuleName.setStatus(_A)
_SlotStatus_Type=SlotStatus
_SlotStatus_Object=MibTableColumn
slotStatus=_SlotStatus_Object((1,3,6,1,4,1,10734,3,3,2,17,1,1,4),_SlotStatus_Type())
slotStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:slotStatus.setStatus(_A)
class _SlotModuleSerialNum_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_SlotModuleSerialNum_Type.__name__=_C
_SlotModuleSerialNum_Object=MibTableColumn
slotModuleSerialNum=_SlotModuleSerialNum_Object((1,3,6,1,4,1,10734,3,3,2,17,1,1,5),_SlotModuleSerialNum_Type())
slotModuleSerialNum.setMaxAccess(_B)
if mibBuilder.loadTexts:slotModuleSerialNum.setStatus(_A)
_SlotModuleType_Type=SlotModuleType
_SlotModuleType_Object=MibTableColumn
slotModuleType=_SlotModuleType_Object((1,3,6,1,4,1,10734,3,3,2,17,1,1,6),_SlotModuleType_Type())
slotModuleType.setMaxAccess(_B)
if mibBuilder.loadTexts:slotModuleType.setStatus(_A)
class _TptSlotDeviceID_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,40))
_TptSlotDeviceID_Type.__name__=_C
_TptSlotDeviceID_Object=MibScalar
tptSlotDeviceID=_TptSlotDeviceID_Object((1,3,6,1,4,1,10734,3,3,3,1,281),_TptSlotDeviceID_Type())
tptSlotDeviceID.setMaxAccess(_B)
if mibBuilder.loadTexts:tptSlotDeviceID.setStatus(_A)
_TptSlotID_Type=Unsigned32
_TptSlotID_Object=MibScalar
tptSlotID=_TptSlotID_Object((1,3,6,1,4,1,10734,3,3,3,1,282),_TptSlotID_Type())
tptSlotID.setMaxAccess(_B)
if mibBuilder.loadTexts:tptSlotID.setStatus(_A)
_TptSlotEvent_Type=SlotEvent
_TptSlotEvent_Object=MibScalar
tptSlotEvent=_TptSlotEvent_Object((1,3,6,1,4,1,10734,3,3,3,1,283),_TptSlotEvent_Type())
tptSlotEvent.setMaxAccess(_B)
if mibBuilder.loadTexts:tptSlotEvent.setStatus(_A)
tptSlotChangeNotify=NotificationType((1,3,6,1,4,1,10734,3,3,3,0,54))
tptSlotChangeNotify.setObjects(*((_D,_F),(_D,_G),(_D,_H)))
if mibBuilder.loadTexts:tptSlotChangeNotify.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'SlotStatus':SlotStatus,'SlotEvent':SlotEvent,'SlotModuleType':SlotModuleType,'tpt-slot-objs':tpt_slot_objs,'slotTempTable':slotTempTable,'slotTempEntry':slotTempEntry,_E:slotTempIndex,'slotName':slotName,'slotModuleName':slotModuleName,'slotStatus':slotStatus,'slotModuleSerialNum':slotModuleSerialNum,'slotModuleType':slotModuleType,'tptSlotChangeNotify':tptSlotChangeNotify,_F:tptSlotDeviceID,_G:tptSlotID,_H:tptSlotEvent})