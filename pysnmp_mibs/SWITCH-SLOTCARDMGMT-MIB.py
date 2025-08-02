_G='raisecomSlotCardState'
_F='raisecomSlotCardIndex'
_E='SWITCH-SLOTCARDMGMT-MIB'
_D='Integer32'
_C='OctetString'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_C,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
raisecomAgent,=mibBuilder.importSymbols('RAISECOM-BASE-MIB','raisecomAgent')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
EnableVar,=mibBuilder.importSymbols('SWITCH-TC','EnableVar')
raisecomSlotCardmgmt=ModuleIdentity((1,3,6,1,4,1,8886,1,23))
if mibBuilder.loadTexts:raisecomSlotCardmgmt.setRevisions(('2011-01-04 00:00',))
_RaisecomSlotCardNotification_ObjectIdentity=ObjectIdentity
raisecomSlotCardNotification=_RaisecomSlotCardNotification_ObjectIdentity((1,3,6,1,4,1,8886,1,23,1))
_RaisecomSlotCardMibObjects_ObjectIdentity=ObjectIdentity
raisecomSlotCardMibObjects=_RaisecomSlotCardMibObjects_ObjectIdentity((1,3,6,1,4,1,8886,1,23,2))
_RaisecomSlotCardGlobalGroup_ObjectIdentity=ObjectIdentity
raisecomSlotCardGlobalGroup=_RaisecomSlotCardGlobalGroup_ObjectIdentity((1,3,6,1,4,1,8886,1,23,2,1))
_RaisecomSlotCardNum_Type=Unsigned32
_RaisecomSlotCardNum_Object=MibScalar
raisecomSlotCardNum=_RaisecomSlotCardNum_Object((1,3,6,1,4,1,8886,1,23,2,1,1),_RaisecomSlotCardNum_Type())
raisecomSlotCardNum.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomSlotCardNum.setStatus(_A)
_RaisecomSlotCardTrapEnable_Type=EnableVar
_RaisecomSlotCardTrapEnable_Object=MibScalar
raisecomSlotCardTrapEnable=_RaisecomSlotCardTrapEnable_Object((1,3,6,1,4,1,8886,1,23,2,1,2),_RaisecomSlotCardTrapEnable_Type())
raisecomSlotCardTrapEnable.setMaxAccess('read-write')
if mibBuilder.loadTexts:raisecomSlotCardTrapEnable.setStatus(_A)
_RaisecomSlotCardTable_Object=MibTable
raisecomSlotCardTable=_RaisecomSlotCardTable_Object((1,3,6,1,4,1,8886,1,23,2,2))
if mibBuilder.loadTexts:raisecomSlotCardTable.setStatus(_A)
_RaisecomSlotCardEntry_Object=MibTableRow
raisecomSlotCardEntry=_RaisecomSlotCardEntry_Object((1,3,6,1,4,1,8886,1,23,2,2,1))
raisecomSlotCardEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:raisecomSlotCardEntry.setStatus(_A)
_RaisecomSlotCardIndex_Type=Unsigned32
_RaisecomSlotCardIndex_Object=MibTableColumn
raisecomSlotCardIndex=_RaisecomSlotCardIndex_Object((1,3,6,1,4,1,8886,1,23,2,2,1,1),_RaisecomSlotCardIndex_Type())
raisecomSlotCardIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:raisecomSlotCardIndex.setStatus(_A)
class _RaisecomSlotCardSerialNumber_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(32,32));fixedLength=32
_RaisecomSlotCardSerialNumber_Type.__name__=_C
_RaisecomSlotCardSerialNumber_Object=MibTableColumn
raisecomSlotCardSerialNumber=_RaisecomSlotCardSerialNumber_Object((1,3,6,1,4,1,8886,1,23,2,2,1,2),_RaisecomSlotCardSerialNumber_Type())
raisecomSlotCardSerialNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomSlotCardSerialNumber.setStatus(_A)
class _RaisecomSlotCardState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('up',1),('down',2)))
_RaisecomSlotCardState_Type.__name__=_D
_RaisecomSlotCardState_Object=MibTableColumn
raisecomSlotCardState=_RaisecomSlotCardState_Object((1,3,6,1,4,1,8886,1,23,2,2,1,3),_RaisecomSlotCardState_Type())
raisecomSlotCardState.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomSlotCardState.setStatus(_A)
class _RaisecomSlotCardType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*(('card-ptp-synce',1),('card-tdmop',2),('null',255)))
_RaisecomSlotCardType_Type.__name__=_D
_RaisecomSlotCardType_Object=MibTableColumn
raisecomSlotCardType=_RaisecomSlotCardType_Object((1,3,6,1,4,1,8886,1,23,2,2,1,4),_RaisecomSlotCardType_Type())
raisecomSlotCardType.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomSlotCardType.setStatus(_A)
class _RaisecomSlotCardDescr_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(240,240));fixedLength=240
_RaisecomSlotCardDescr_Type.__name__=_C
_RaisecomSlotCardDescr_Object=MibTableColumn
raisecomSlotCardDescr=_RaisecomSlotCardDescr_Object((1,3,6,1,4,1,8886,1,23,2,2,1,5),_RaisecomSlotCardDescr_Type())
raisecomSlotCardDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomSlotCardDescr.setStatus(_A)
raisecomSlotCardStateChange=NotificationType((1,3,6,1,4,1,8886,1,23,1,1))
raisecomSlotCardStateChange.setObjects((_E,_G))
if mibBuilder.loadTexts:raisecomSlotCardStateChange.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'raisecomSlotCardmgmt':raisecomSlotCardmgmt,'raisecomSlotCardNotification':raisecomSlotCardNotification,'raisecomSlotCardStateChange':raisecomSlotCardStateChange,'raisecomSlotCardMibObjects':raisecomSlotCardMibObjects,'raisecomSlotCardGlobalGroup':raisecomSlotCardGlobalGroup,'raisecomSlotCardNum':raisecomSlotCardNum,'raisecomSlotCardTrapEnable':raisecomSlotCardTrapEnable,'raisecomSlotCardTable':raisecomSlotCardTable,'raisecomSlotCardEntry':raisecomSlotCardEntry,_F:raisecomSlotCardIndex,'raisecomSlotCardSerialNumber':raisecomSlotCardSerialNumber,_G:raisecomSlotCardState,'raisecomSlotCardType':raisecomSlotCardType,'raisecomSlotCardDescr':raisecomSlotCardDescr})