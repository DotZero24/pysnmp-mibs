_W='currentNotificationGroup'
_V='currentObjectGroup'
_U='h3cCfCardHotSwapOff'
_T='h3cCfCardHotSwapOn'
_S='h3cCfCardFreeSize'
_R='h3cCfCardUsedSize'
_Q='h3cCfCardSize'
_P='h3cCfCardState'
_O='h3cCfCardModelNumber'
_N='h3cCfCardFirewareVersion'
_M='h3cCfCardSerialNumber'
_L='h3cCfCardIsPresent'
_K='h3cCfCardNumber'
_J='byte'
_I='h3cCfCardIndex'
_H='h3cCfCardDescription'
_G='h3cCfCardParentRelPos'
_F='h3cCfCardContainedIn'
_E='OctetString'
_D='Integer32'
_C='read-only'
_B='A3COM-HUAWEI-CFCARD-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_E,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
h3cCfCard,=mibBuilder.importSymbols('A3COM-HUAWEI-OID-MIB','h3cCfCard')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
h3cCfCardMIB=ModuleIdentity((1,3,6,1,4,1,43,45,1,10,2,41,1))
_H3cCfCardMIBObjects_ObjectIdentity=ObjectIdentity
h3cCfCardMIBObjects=_H3cCfCardMIBObjects_ObjectIdentity((1,3,6,1,4,1,43,45,1,10,2,41,1,1))
if mibBuilder.loadTexts:h3cCfCardMIBObjects.setStatus(_A)
_H3cCfCardScalarObjects_ObjectIdentity=ObjectIdentity
h3cCfCardScalarObjects=_H3cCfCardScalarObjects_ObjectIdentity((1,3,6,1,4,1,43,45,1,10,2,41,1,1,1))
if mibBuilder.loadTexts:h3cCfCardScalarObjects.setStatus(_A)
class _H3cCfCardNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_H3cCfCardNumber_Type.__name__=_D
_H3cCfCardNumber_Object=MibScalar
h3cCfCardNumber=_H3cCfCardNumber_Object((1,3,6,1,4,1,43,45,1,10,2,41,1,1,1,1),_H3cCfCardNumber_Type())
h3cCfCardNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cCfCardNumber.setStatus(_A)
_H3cCfCardInfoObjects_ObjectIdentity=ObjectIdentity
h3cCfCardInfoObjects=_H3cCfCardInfoObjects_ObjectIdentity((1,3,6,1,4,1,43,45,1,10,2,41,1,1,2))
if mibBuilder.loadTexts:h3cCfCardInfoObjects.setStatus(_A)
_H3cCfCardInfoTable_Object=MibTable
h3cCfCardInfoTable=_H3cCfCardInfoTable_Object((1,3,6,1,4,1,43,45,1,10,2,41,1,1,2,2))
if mibBuilder.loadTexts:h3cCfCardInfoTable.setStatus(_A)
_H3CfCardInfoEntry_Object=MibTableRow
h3CfCardInfoEntry=_H3CfCardInfoEntry_Object((1,3,6,1,4,1,43,45,1,10,2,41,1,1,2,2,1))
h3CfCardInfoEntry.setIndexNames((0,_B,_I))
if mibBuilder.loadTexts:h3CfCardInfoEntry.setStatus(_A)
class _H3cCfCardIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_H3cCfCardIndex_Type.__name__=_D
_H3cCfCardIndex_Object=MibTableColumn
h3cCfCardIndex=_H3cCfCardIndex_Object((1,3,6,1,4,1,43,45,1,10,2,41,1,1,2,2,1,1),_H3cCfCardIndex_Type())
h3cCfCardIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cCfCardIndex.setStatus(_A)
class _H3cCfCardIsPresent_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('yes',1),('no',2)))
_H3cCfCardIsPresent_Type.__name__=_D
_H3cCfCardIsPresent_Object=MibTableColumn
h3cCfCardIsPresent=_H3cCfCardIsPresent_Object((1,3,6,1,4,1,43,45,1,10,2,41,1,1,2,2,1,2),_H3cCfCardIsPresent_Type())
h3cCfCardIsPresent.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cCfCardIsPresent.setStatus(_A)
class _H3cCfCardContainedIn_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_H3cCfCardContainedIn_Type.__name__=_D
_H3cCfCardContainedIn_Object=MibTableColumn
h3cCfCardContainedIn=_H3cCfCardContainedIn_Object((1,3,6,1,4,1,43,45,1,10,2,41,1,1,2,2,1,3),_H3cCfCardContainedIn_Type())
h3cCfCardContainedIn.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cCfCardContainedIn.setStatus(_A)
class _H3cCfCardParentRelPos_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_H3cCfCardParentRelPos_Type.__name__=_D
_H3cCfCardParentRelPos_Object=MibTableColumn
h3cCfCardParentRelPos=_H3cCfCardParentRelPos_Object((1,3,6,1,4,1,43,45,1,10,2,41,1,1,2,2,1,4),_H3cCfCardParentRelPos_Type())
h3cCfCardParentRelPos.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cCfCardParentRelPos.setStatus(_A)
class _H3cCfCardDescription_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_H3cCfCardDescription_Type.__name__=_E
_H3cCfCardDescription_Object=MibTableColumn
h3cCfCardDescription=_H3cCfCardDescription_Object((1,3,6,1,4,1,43,45,1,10,2,41,1,1,2,2,1,5),_H3cCfCardDescription_Type())
h3cCfCardDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cCfCardDescription.setStatus(_A)
class _H3cCfCardSerialNumber_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_H3cCfCardSerialNumber_Type.__name__=_E
_H3cCfCardSerialNumber_Object=MibTableColumn
h3cCfCardSerialNumber=_H3cCfCardSerialNumber_Object((1,3,6,1,4,1,43,45,1,10,2,41,1,1,2,2,1,6),_H3cCfCardSerialNumber_Type())
h3cCfCardSerialNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cCfCardSerialNumber.setStatus(_A)
class _H3cCfCardFirewareVersion_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_H3cCfCardFirewareVersion_Type.__name__=_E
_H3cCfCardFirewareVersion_Object=MibTableColumn
h3cCfCardFirewareVersion=_H3cCfCardFirewareVersion_Object((1,3,6,1,4,1,43,45,1,10,2,41,1,1,2,2,1,7),_H3cCfCardFirewareVersion_Type())
h3cCfCardFirewareVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cCfCardFirewareVersion.setStatus(_A)
class _H3cCfCardModelNumber_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_H3cCfCardModelNumber_Type.__name__=_E
_H3cCfCardModelNumber_Object=MibTableColumn
h3cCfCardModelNumber=_H3cCfCardModelNumber_Object((1,3,6,1,4,1,43,45,1,10,2,41,1,1,2,2,1,8),_H3cCfCardModelNumber_Type())
h3cCfCardModelNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cCfCardModelNumber.setStatus(_A)
class _H3cCfCardState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,128,240,255)));namedValues=NamedValues(*(('sNoError',1),('sFormatError',2),('sSectorBufferError',3),('sECCError',4),('sCMPError',5),('sSlaveError',128),('sIOError',240),('sOther',255)))
_H3cCfCardState_Type.__name__=_D
_H3cCfCardState_Object=MibTableColumn
h3cCfCardState=_H3cCfCardState_Object((1,3,6,1,4,1,43,45,1,10,2,41,1,1,2,2,1,9),_H3cCfCardState_Type())
h3cCfCardState.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cCfCardState.setStatus(_A)
_H3cCfCardSize_Type=Unsigned32
_H3cCfCardSize_Object=MibTableColumn
h3cCfCardSize=_H3cCfCardSize_Object((1,3,6,1,4,1,43,45,1,10,2,41,1,1,2,2,1,10),_H3cCfCardSize_Type())
h3cCfCardSize.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cCfCardSize.setStatus(_A)
if mibBuilder.loadTexts:h3cCfCardSize.setUnits(_J)
_H3cCfCardUsedSize_Type=Unsigned32
_H3cCfCardUsedSize_Object=MibTableColumn
h3cCfCardUsedSize=_H3cCfCardUsedSize_Object((1,3,6,1,4,1,43,45,1,10,2,41,1,1,2,2,1,11),_H3cCfCardUsedSize_Type())
h3cCfCardUsedSize.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cCfCardUsedSize.setStatus(_A)
if mibBuilder.loadTexts:h3cCfCardUsedSize.setUnits(_J)
_H3cCfCardFreeSize_Type=Unsigned32
_H3cCfCardFreeSize_Object=MibTableColumn
h3cCfCardFreeSize=_H3cCfCardFreeSize_Object((1,3,6,1,4,1,43,45,1,10,2,41,1,1,2,2,1,12),_H3cCfCardFreeSize_Type())
h3cCfCardFreeSize.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cCfCardFreeSize.setStatus(_A)
if mibBuilder.loadTexts:h3cCfCardFreeSize.setUnits(_J)
_H3cCfCardNotifications_ObjectIdentity=ObjectIdentity
h3cCfCardNotifications=_H3cCfCardNotifications_ObjectIdentity((1,3,6,1,4,1,43,45,1,10,2,41,1,2))
if mibBuilder.loadTexts:h3cCfCardNotifications.setStatus(_A)
_H3cCfCardNotificationsV2_ObjectIdentity=ObjectIdentity
h3cCfCardNotificationsV2=_H3cCfCardNotificationsV2_ObjectIdentity((1,3,6,1,4,1,43,45,1,10,2,41,1,2,0))
if mibBuilder.loadTexts:h3cCfCardNotificationsV2.setStatus(_A)
_H3cCfCardMIBConformance_ObjectIdentity=ObjectIdentity
h3cCfCardMIBConformance=_H3cCfCardMIBConformance_ObjectIdentity((1,3,6,1,4,1,43,45,1,10,2,41,1,4))
_H3cCfCardMIBGroups_ObjectIdentity=ObjectIdentity
h3cCfCardMIBGroups=_H3cCfCardMIBGroups_ObjectIdentity((1,3,6,1,4,1,43,45,1,10,2,41,1,4,1))
_H3cCfCardMIBCompliances_ObjectIdentity=ObjectIdentity
h3cCfCardMIBCompliances=_H3cCfCardMIBCompliances_ObjectIdentity((1,3,6,1,4,1,43,45,1,10,2,41,1,4,2))
currentObjectGroup=ObjectGroup((1,3,6,1,4,1,43,45,1,10,2,41,1,4,1,1))
currentObjectGroup.setObjects(*((_B,_K),(_B,_I),(_B,_L),(_B,_F),(_B,_G),(_B,_H),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S)))
if mibBuilder.loadTexts:currentObjectGroup.setStatus(_A)
h3cCfCardHotSwapOn=NotificationType((1,3,6,1,4,1,43,45,1,10,2,41,1,2,0,1))
h3cCfCardHotSwapOn.setObjects(*((_B,_F),(_B,_G),(_B,_H)))
if mibBuilder.loadTexts:h3cCfCardHotSwapOn.setStatus(_A)
h3cCfCardHotSwapOff=NotificationType((1,3,6,1,4,1,43,45,1,10,2,41,1,2,0,2))
h3cCfCardHotSwapOff.setObjects(*((_B,_F),(_B,_G),(_B,_H)))
if mibBuilder.loadTexts:h3cCfCardHotSwapOff.setStatus(_A)
currentNotificationGroup=NotificationGroup((1,3,6,1,4,1,43,45,1,10,2,41,1,4,1,2))
currentNotificationGroup.setObjects(*((_B,_T),(_B,_U)))
if mibBuilder.loadTexts:currentNotificationGroup.setStatus(_A)
basicCompliance=ModuleCompliance((1,3,6,1,4,1,43,45,1,10,2,41,1,4,2,1))
basicCompliance.setObjects(*((_B,_V),(_B,_W)))
if mibBuilder.loadTexts:basicCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'h3cCfCardMIB':h3cCfCardMIB,'h3cCfCardMIBObjects':h3cCfCardMIBObjects,'h3cCfCardScalarObjects':h3cCfCardScalarObjects,_K:h3cCfCardNumber,'h3cCfCardInfoObjects':h3cCfCardInfoObjects,'h3cCfCardInfoTable':h3cCfCardInfoTable,'h3CfCardInfoEntry':h3CfCardInfoEntry,_I:h3cCfCardIndex,_L:h3cCfCardIsPresent,_F:h3cCfCardContainedIn,_G:h3cCfCardParentRelPos,_H:h3cCfCardDescription,_M:h3cCfCardSerialNumber,_N:h3cCfCardFirewareVersion,_O:h3cCfCardModelNumber,_P:h3cCfCardState,_Q:h3cCfCardSize,_R:h3cCfCardUsedSize,_S:h3cCfCardFreeSize,'h3cCfCardNotifications':h3cCfCardNotifications,'h3cCfCardNotificationsV2':h3cCfCardNotificationsV2,_T:h3cCfCardHotSwapOn,_U:h3cCfCardHotSwapOff,'h3cCfCardMIBConformance':h3cCfCardMIBConformance,'h3cCfCardMIBGroups':h3cCfCardMIBGroups,_V:currentObjectGroup,_W:currentNotificationGroup,'h3cCfCardMIBCompliances':h3cCfCardMIBCompliances,'basicCompliance':basicCompliance})