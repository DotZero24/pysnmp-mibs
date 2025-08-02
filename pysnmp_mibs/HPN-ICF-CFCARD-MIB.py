_W='hpnicfcurrentNotificationGroup'
_V='hpnicfcurrentObjectGroup'
_U='hpnicfCfCardHotSwapOff'
_T='hpnicfCfCardHotSwapOn'
_S='hpnicfCfCardFreeSize'
_R='hpnicfCfCardUsedSize'
_Q='hpnicfCfCardSize'
_P='hpnicfCfCardState'
_O='hpnicfCfCardModelNumber'
_N='hpnicfCfCardFirewareVersion'
_M='hpnicfCfCardSerialNumber'
_L='hpnicfCfCardIsPresent'
_K='hpnicfCfCardNumber'
_J='byte'
_I='hpnicfCfCardIndex'
_H='hpnicfCfCardDescription'
_G='hpnicfCfCardParentRelPos'
_F='hpnicfCfCardContainedIn'
_E='OctetString'
_D='Integer32'
_C='read-only'
_B='HPN-ICF-CFCARD-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_E,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hpnicfCfCard,=mibBuilder.importSymbols('HPN-ICF-OID-MIB','hpnicfCfCard')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
hpnicfCfCardMIB=ModuleIdentity((1,3,6,1,4,1,11,2,14,11,15,2,41,1))
_HpnicfCfCardMIBObjects_ObjectIdentity=ObjectIdentity
hpnicfCfCardMIBObjects=_HpnicfCfCardMIBObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,41,1,1))
if mibBuilder.loadTexts:hpnicfCfCardMIBObjects.setStatus(_A)
_HpnicfCfCardScalarObjects_ObjectIdentity=ObjectIdentity
hpnicfCfCardScalarObjects=_HpnicfCfCardScalarObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,41,1,1,1))
if mibBuilder.loadTexts:hpnicfCfCardScalarObjects.setStatus(_A)
class _HpnicfCfCardNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_HpnicfCfCardNumber_Type.__name__=_D
_HpnicfCfCardNumber_Object=MibScalar
hpnicfCfCardNumber=_HpnicfCfCardNumber_Object((1,3,6,1,4,1,11,2,14,11,15,2,41,1,1,1,1),_HpnicfCfCardNumber_Type())
hpnicfCfCardNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfCfCardNumber.setStatus(_A)
_HpnicfCfCardInfoObjects_ObjectIdentity=ObjectIdentity
hpnicfCfCardInfoObjects=_HpnicfCfCardInfoObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,41,1,1,2))
if mibBuilder.loadTexts:hpnicfCfCardInfoObjects.setStatus(_A)
_HpnicfCfCardInfoTable_Object=MibTable
hpnicfCfCardInfoTable=_HpnicfCfCardInfoTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,41,1,1,2,2))
if mibBuilder.loadTexts:hpnicfCfCardInfoTable.setStatus(_A)
_HpnicfCfCardInfoEntry_Object=MibTableRow
hpnicfCfCardInfoEntry=_HpnicfCfCardInfoEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,41,1,1,2,2,1))
hpnicfCfCardInfoEntry.setIndexNames((0,_B,_I))
if mibBuilder.loadTexts:hpnicfCfCardInfoEntry.setStatus(_A)
class _HpnicfCfCardIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_HpnicfCfCardIndex_Type.__name__=_D
_HpnicfCfCardIndex_Object=MibTableColumn
hpnicfCfCardIndex=_HpnicfCfCardIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,41,1,1,2,2,1,1),_HpnicfCfCardIndex_Type())
hpnicfCfCardIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfCfCardIndex.setStatus(_A)
class _HpnicfCfCardIsPresent_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('yes',1),('no',2)))
_HpnicfCfCardIsPresent_Type.__name__=_D
_HpnicfCfCardIsPresent_Object=MibTableColumn
hpnicfCfCardIsPresent=_HpnicfCfCardIsPresent_Object((1,3,6,1,4,1,11,2,14,11,15,2,41,1,1,2,2,1,2),_HpnicfCfCardIsPresent_Type())
hpnicfCfCardIsPresent.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfCfCardIsPresent.setStatus(_A)
class _HpnicfCfCardContainedIn_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_HpnicfCfCardContainedIn_Type.__name__=_D
_HpnicfCfCardContainedIn_Object=MibTableColumn
hpnicfCfCardContainedIn=_HpnicfCfCardContainedIn_Object((1,3,6,1,4,1,11,2,14,11,15,2,41,1,1,2,2,1,3),_HpnicfCfCardContainedIn_Type())
hpnicfCfCardContainedIn.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfCfCardContainedIn.setStatus(_A)
class _HpnicfCfCardParentRelPos_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_HpnicfCfCardParentRelPos_Type.__name__=_D
_HpnicfCfCardParentRelPos_Object=MibTableColumn
hpnicfCfCardParentRelPos=_HpnicfCfCardParentRelPos_Object((1,3,6,1,4,1,11,2,14,11,15,2,41,1,1,2,2,1,4),_HpnicfCfCardParentRelPos_Type())
hpnicfCfCardParentRelPos.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfCfCardParentRelPos.setStatus(_A)
class _HpnicfCfCardDescription_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_HpnicfCfCardDescription_Type.__name__=_E
_HpnicfCfCardDescription_Object=MibTableColumn
hpnicfCfCardDescription=_HpnicfCfCardDescription_Object((1,3,6,1,4,1,11,2,14,11,15,2,41,1,1,2,2,1,5),_HpnicfCfCardDescription_Type())
hpnicfCfCardDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfCfCardDescription.setStatus(_A)
class _HpnicfCfCardSerialNumber_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_HpnicfCfCardSerialNumber_Type.__name__=_E
_HpnicfCfCardSerialNumber_Object=MibTableColumn
hpnicfCfCardSerialNumber=_HpnicfCfCardSerialNumber_Object((1,3,6,1,4,1,11,2,14,11,15,2,41,1,1,2,2,1,6),_HpnicfCfCardSerialNumber_Type())
hpnicfCfCardSerialNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfCfCardSerialNumber.setStatus(_A)
class _HpnicfCfCardFirewareVersion_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_HpnicfCfCardFirewareVersion_Type.__name__=_E
_HpnicfCfCardFirewareVersion_Object=MibTableColumn
hpnicfCfCardFirewareVersion=_HpnicfCfCardFirewareVersion_Object((1,3,6,1,4,1,11,2,14,11,15,2,41,1,1,2,2,1,7),_HpnicfCfCardFirewareVersion_Type())
hpnicfCfCardFirewareVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfCfCardFirewareVersion.setStatus(_A)
class _HpnicfCfCardModelNumber_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_HpnicfCfCardModelNumber_Type.__name__=_E
_HpnicfCfCardModelNumber_Object=MibTableColumn
hpnicfCfCardModelNumber=_HpnicfCfCardModelNumber_Object((1,3,6,1,4,1,11,2,14,11,15,2,41,1,1,2,2,1,8),_HpnicfCfCardModelNumber_Type())
hpnicfCfCardModelNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfCfCardModelNumber.setStatus(_A)
class _HpnicfCfCardState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,128,240,255)));namedValues=NamedValues(*(('sNoError',1),('sFormatError',2),('sSectorBufferError',3),('sECCError',4),('sCMPError',5),('sSlaveError',128),('sIOError',240),('sOther',255)))
_HpnicfCfCardState_Type.__name__=_D
_HpnicfCfCardState_Object=MibTableColumn
hpnicfCfCardState=_HpnicfCfCardState_Object((1,3,6,1,4,1,11,2,14,11,15,2,41,1,1,2,2,1,9),_HpnicfCfCardState_Type())
hpnicfCfCardState.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfCfCardState.setStatus(_A)
_HpnicfCfCardSize_Type=Unsigned32
_HpnicfCfCardSize_Object=MibTableColumn
hpnicfCfCardSize=_HpnicfCfCardSize_Object((1,3,6,1,4,1,11,2,14,11,15,2,41,1,1,2,2,1,10),_HpnicfCfCardSize_Type())
hpnicfCfCardSize.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfCfCardSize.setStatus(_A)
if mibBuilder.loadTexts:hpnicfCfCardSize.setUnits(_J)
_HpnicfCfCardUsedSize_Type=Unsigned32
_HpnicfCfCardUsedSize_Object=MibTableColumn
hpnicfCfCardUsedSize=_HpnicfCfCardUsedSize_Object((1,3,6,1,4,1,11,2,14,11,15,2,41,1,1,2,2,1,11),_HpnicfCfCardUsedSize_Type())
hpnicfCfCardUsedSize.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfCfCardUsedSize.setStatus(_A)
if mibBuilder.loadTexts:hpnicfCfCardUsedSize.setUnits(_J)
_HpnicfCfCardFreeSize_Type=Unsigned32
_HpnicfCfCardFreeSize_Object=MibTableColumn
hpnicfCfCardFreeSize=_HpnicfCfCardFreeSize_Object((1,3,6,1,4,1,11,2,14,11,15,2,41,1,1,2,2,1,12),_HpnicfCfCardFreeSize_Type())
hpnicfCfCardFreeSize.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfCfCardFreeSize.setStatus(_A)
if mibBuilder.loadTexts:hpnicfCfCardFreeSize.setUnits(_J)
_HpnicfCfCardNotifications_ObjectIdentity=ObjectIdentity
hpnicfCfCardNotifications=_HpnicfCfCardNotifications_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,41,1,2))
if mibBuilder.loadTexts:hpnicfCfCardNotifications.setStatus(_A)
_HpnicfCfCardNotificationsV2_ObjectIdentity=ObjectIdentity
hpnicfCfCardNotificationsV2=_HpnicfCfCardNotificationsV2_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,41,1,2,0))
if mibBuilder.loadTexts:hpnicfCfCardNotificationsV2.setStatus(_A)
_HpnicfCfCardMIBConformance_ObjectIdentity=ObjectIdentity
hpnicfCfCardMIBConformance=_HpnicfCfCardMIBConformance_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,41,1,4))
_HpnicfCfCardMIBGroups_ObjectIdentity=ObjectIdentity
hpnicfCfCardMIBGroups=_HpnicfCfCardMIBGroups_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,41,1,4,1))
_HpnicfCfCardMIBCompliances_ObjectIdentity=ObjectIdentity
hpnicfCfCardMIBCompliances=_HpnicfCfCardMIBCompliances_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,41,1,4,2))
hpnicfcurrentObjectGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,15,2,41,1,4,1,1))
hpnicfcurrentObjectGroup.setObjects(*((_B,_K),(_B,_I),(_B,_L),(_B,_F),(_B,_G),(_B,_H),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S)))
if mibBuilder.loadTexts:hpnicfcurrentObjectGroup.setStatus(_A)
hpnicfCfCardHotSwapOn=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,41,1,2,0,1))
hpnicfCfCardHotSwapOn.setObjects(*((_B,_F),(_B,_G),(_B,_H)))
if mibBuilder.loadTexts:hpnicfCfCardHotSwapOn.setStatus(_A)
hpnicfCfCardHotSwapOff=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,41,1,2,0,2))
hpnicfCfCardHotSwapOff.setObjects(*((_B,_F),(_B,_G),(_B,_H)))
if mibBuilder.loadTexts:hpnicfCfCardHotSwapOff.setStatus(_A)
hpnicfcurrentNotificationGroup=NotificationGroup((1,3,6,1,4,1,11,2,14,11,15,2,41,1,4,1,2))
hpnicfcurrentNotificationGroup.setObjects(*((_B,_T),(_B,_U)))
if mibBuilder.loadTexts:hpnicfcurrentNotificationGroup.setStatus(_A)
hpnicfbasicCompliance=ModuleCompliance((1,3,6,1,4,1,11,2,14,11,15,2,41,1,4,2,1))
hpnicfbasicCompliance.setObjects(*((_B,_V),(_B,_W)))
if mibBuilder.loadTexts:hpnicfbasicCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'hpnicfCfCardMIB':hpnicfCfCardMIB,'hpnicfCfCardMIBObjects':hpnicfCfCardMIBObjects,'hpnicfCfCardScalarObjects':hpnicfCfCardScalarObjects,_K:hpnicfCfCardNumber,'hpnicfCfCardInfoObjects':hpnicfCfCardInfoObjects,'hpnicfCfCardInfoTable':hpnicfCfCardInfoTable,'hpnicfCfCardInfoEntry':hpnicfCfCardInfoEntry,_I:hpnicfCfCardIndex,_L:hpnicfCfCardIsPresent,_F:hpnicfCfCardContainedIn,_G:hpnicfCfCardParentRelPos,_H:hpnicfCfCardDescription,_M:hpnicfCfCardSerialNumber,_N:hpnicfCfCardFirewareVersion,_O:hpnicfCfCardModelNumber,_P:hpnicfCfCardState,_Q:hpnicfCfCardSize,_R:hpnicfCfCardUsedSize,_S:hpnicfCfCardFreeSize,'hpnicfCfCardNotifications':hpnicfCfCardNotifications,'hpnicfCfCardNotificationsV2':hpnicfCfCardNotificationsV2,_T:hpnicfCfCardHotSwapOn,_U:hpnicfCfCardHotSwapOff,'hpnicfCfCardMIBConformance':hpnicfCfCardMIBConformance,'hpnicfCfCardMIBGroups':hpnicfCfCardMIBGroups,_V:hpnicfcurrentObjectGroup,_W:hpnicfcurrentNotificationGroup,'hpnicfCfCardMIBCompliances':hpnicfCfCardMIBCompliances,'hpnicfbasicCompliance':hpnicfbasicCompliance})