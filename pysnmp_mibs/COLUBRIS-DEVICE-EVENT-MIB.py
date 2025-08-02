_s='colubrisDeviceEventNotificationGroup'
_r='colubrisDeviceEventInfoMIBGroup'
_q='colubrisDeviceEventConfigMIBGroup'
_p='coDeviceEventDeAuthenticationFailure'
_o='coDeviceEventSuccessfulDeAuthentication'
_n='coDeviceEventDisAssociationFailure'
_m='coDeviceEventSuccessfulDisAssociation'
_l='coDeviceEventAuthenticationFailure'
_k='coDeviceEventSuccessfulAuthentication'
_j='coDeviceEventReAssociationFailure'
_i='coDeviceEventSuccessfulReAssociation'
_h='coDeviceEventAssociationFailure'
_g='coDeviceEventSuccessfulAssociation'
_f='coDevEvOperation'
_e='coDevEvCategory'
_d='coDevEvDuplicateCount'
_c='coDevEvRadioIndex'
_b='coDevEvTime'
_a='coDevEvDetMacAddress'
_Z='coDevEvDeAuthenticationFailureNotificationEnabled'
_Y='coDevEvSuccessfulDeAuthenticationNotificationEnabled'
_X='coDevEvDisAssociationFailureNotificationEnabled'
_W='coDevEvSuccessfulDisAssociationNotificationEnabled'
_V='coDevEvAuthenticationFailureNotificationEnabled'
_U='coDevEvSuccessfulAuthenticationNotificationEnabled'
_T='coDevEvReAssociationFailureNotificationEnabled'
_S='coDevEvSuccessfulReAssociationNotificationEnabled'
_R='coDevEvAssociationFailureNotificationEnabled'
_Q='coDevEvSuccessfulAssociationNotificationEnabled'
_P='unknown'
_O='coDevEvLogIndex'
_N='not-accessible'
_M='coDevEvIndex'
_L='coDevDisIndex'
_K='COLUBRIS-DEVICE-MIB'
_J='Integer32'
_I='read-only'
_H='read-write'
_G='ColubrisNotificationEnable'
_F='coDevEvOptionalData'
_E='coDevEvStatus'
_D='coDevEvSSID'
_C='coDevEvMacAddress'
_B='current'
_A='COLUBRIS-DEVICE-EVENT-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
coDevDisIndex,=mibBuilder.importSymbols(_K,_L)
colubrisMgmtV2,=mibBuilder.importSymbols('COLUBRIS-SMI','colubrisMgmtV2')
ColubrisNotificationEnable,ColubrisSSIDOrNone=mibBuilder.importSymbols('COLUBRIS-TC',_G,'ColubrisSSIDOrNone')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_J,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','TextualConvention')
colubrisDeviceEventMIB=ModuleIdentity((1,3,6,1,4,1,8744,5,26))
_ColubrisDeviceEventMIBObjects_ObjectIdentity=ObjectIdentity
colubrisDeviceEventMIBObjects=_ColubrisDeviceEventMIBObjects_ObjectIdentity((1,3,6,1,4,1,8744,5,26,1))
_CoDeviceEventConfigGroup_ObjectIdentity=ObjectIdentity
coDeviceEventConfigGroup=_CoDeviceEventConfigGroup_ObjectIdentity((1,3,6,1,4,1,8744,5,26,1,1))
class _CoDevEvSuccessfulAssociationNotificationEnabled_Type(ColubrisNotificationEnable):defaultValue=2
_CoDevEvSuccessfulAssociationNotificationEnabled_Type.__name__=_G
_CoDevEvSuccessfulAssociationNotificationEnabled_Object=MibScalar
coDevEvSuccessfulAssociationNotificationEnabled=_CoDevEvSuccessfulAssociationNotificationEnabled_Object((1,3,6,1,4,1,8744,5,26,1,1,1),_CoDevEvSuccessfulAssociationNotificationEnabled_Type())
coDevEvSuccessfulAssociationNotificationEnabled.setMaxAccess(_H)
if mibBuilder.loadTexts:coDevEvSuccessfulAssociationNotificationEnabled.setStatus(_B)
class _CoDevEvAssociationFailureNotificationEnabled_Type(ColubrisNotificationEnable):defaultValue=2
_CoDevEvAssociationFailureNotificationEnabled_Type.__name__=_G
_CoDevEvAssociationFailureNotificationEnabled_Object=MibScalar
coDevEvAssociationFailureNotificationEnabled=_CoDevEvAssociationFailureNotificationEnabled_Object((1,3,6,1,4,1,8744,5,26,1,1,2),_CoDevEvAssociationFailureNotificationEnabled_Type())
coDevEvAssociationFailureNotificationEnabled.setMaxAccess(_H)
if mibBuilder.loadTexts:coDevEvAssociationFailureNotificationEnabled.setStatus(_B)
class _CoDevEvSuccessfulReAssociationNotificationEnabled_Type(ColubrisNotificationEnable):defaultValue=2
_CoDevEvSuccessfulReAssociationNotificationEnabled_Type.__name__=_G
_CoDevEvSuccessfulReAssociationNotificationEnabled_Object=MibScalar
coDevEvSuccessfulReAssociationNotificationEnabled=_CoDevEvSuccessfulReAssociationNotificationEnabled_Object((1,3,6,1,4,1,8744,5,26,1,1,3),_CoDevEvSuccessfulReAssociationNotificationEnabled_Type())
coDevEvSuccessfulReAssociationNotificationEnabled.setMaxAccess(_H)
if mibBuilder.loadTexts:coDevEvSuccessfulReAssociationNotificationEnabled.setStatus(_B)
class _CoDevEvReAssociationFailureNotificationEnabled_Type(ColubrisNotificationEnable):defaultValue=2
_CoDevEvReAssociationFailureNotificationEnabled_Type.__name__=_G
_CoDevEvReAssociationFailureNotificationEnabled_Object=MibScalar
coDevEvReAssociationFailureNotificationEnabled=_CoDevEvReAssociationFailureNotificationEnabled_Object((1,3,6,1,4,1,8744,5,26,1,1,4),_CoDevEvReAssociationFailureNotificationEnabled_Type())
coDevEvReAssociationFailureNotificationEnabled.setMaxAccess(_H)
if mibBuilder.loadTexts:coDevEvReAssociationFailureNotificationEnabled.setStatus(_B)
class _CoDevEvSuccessfulAuthenticationNotificationEnabled_Type(ColubrisNotificationEnable):defaultValue=2
_CoDevEvSuccessfulAuthenticationNotificationEnabled_Type.__name__=_G
_CoDevEvSuccessfulAuthenticationNotificationEnabled_Object=MibScalar
coDevEvSuccessfulAuthenticationNotificationEnabled=_CoDevEvSuccessfulAuthenticationNotificationEnabled_Object((1,3,6,1,4,1,8744,5,26,1,1,5),_CoDevEvSuccessfulAuthenticationNotificationEnabled_Type())
coDevEvSuccessfulAuthenticationNotificationEnabled.setMaxAccess(_H)
if mibBuilder.loadTexts:coDevEvSuccessfulAuthenticationNotificationEnabled.setStatus(_B)
class _CoDevEvAuthenticationFailureNotificationEnabled_Type(ColubrisNotificationEnable):defaultValue=2
_CoDevEvAuthenticationFailureNotificationEnabled_Type.__name__=_G
_CoDevEvAuthenticationFailureNotificationEnabled_Object=MibScalar
coDevEvAuthenticationFailureNotificationEnabled=_CoDevEvAuthenticationFailureNotificationEnabled_Object((1,3,6,1,4,1,8744,5,26,1,1,6),_CoDevEvAuthenticationFailureNotificationEnabled_Type())
coDevEvAuthenticationFailureNotificationEnabled.setMaxAccess(_H)
if mibBuilder.loadTexts:coDevEvAuthenticationFailureNotificationEnabled.setStatus(_B)
class _CoDevEvSuccessfulDisAssociationNotificationEnabled_Type(ColubrisNotificationEnable):defaultValue=2
_CoDevEvSuccessfulDisAssociationNotificationEnabled_Type.__name__=_G
_CoDevEvSuccessfulDisAssociationNotificationEnabled_Object=MibScalar
coDevEvSuccessfulDisAssociationNotificationEnabled=_CoDevEvSuccessfulDisAssociationNotificationEnabled_Object((1,3,6,1,4,1,8744,5,26,1,1,7),_CoDevEvSuccessfulDisAssociationNotificationEnabled_Type())
coDevEvSuccessfulDisAssociationNotificationEnabled.setMaxAccess(_H)
if mibBuilder.loadTexts:coDevEvSuccessfulDisAssociationNotificationEnabled.setStatus(_B)
class _CoDevEvDisAssociationFailureNotificationEnabled_Type(ColubrisNotificationEnable):defaultValue=2
_CoDevEvDisAssociationFailureNotificationEnabled_Type.__name__=_G
_CoDevEvDisAssociationFailureNotificationEnabled_Object=MibScalar
coDevEvDisAssociationFailureNotificationEnabled=_CoDevEvDisAssociationFailureNotificationEnabled_Object((1,3,6,1,4,1,8744,5,26,1,1,8),_CoDevEvDisAssociationFailureNotificationEnabled_Type())
coDevEvDisAssociationFailureNotificationEnabled.setMaxAccess(_H)
if mibBuilder.loadTexts:coDevEvDisAssociationFailureNotificationEnabled.setStatus(_B)
class _CoDevEvSuccessfulDeAuthenticationNotificationEnabled_Type(ColubrisNotificationEnable):defaultValue=2
_CoDevEvSuccessfulDeAuthenticationNotificationEnabled_Type.__name__=_G
_CoDevEvSuccessfulDeAuthenticationNotificationEnabled_Object=MibScalar
coDevEvSuccessfulDeAuthenticationNotificationEnabled=_CoDevEvSuccessfulDeAuthenticationNotificationEnabled_Object((1,3,6,1,4,1,8744,5,26,1,1,9),_CoDevEvSuccessfulDeAuthenticationNotificationEnabled_Type())
coDevEvSuccessfulDeAuthenticationNotificationEnabled.setMaxAccess(_H)
if mibBuilder.loadTexts:coDevEvSuccessfulDeAuthenticationNotificationEnabled.setStatus(_B)
class _CoDevEvDeAuthenticationFailureNotificationEnabled_Type(ColubrisNotificationEnable):defaultValue=2
_CoDevEvDeAuthenticationFailureNotificationEnabled_Type.__name__=_G
_CoDevEvDeAuthenticationFailureNotificationEnabled_Object=MibScalar
coDevEvDeAuthenticationFailureNotificationEnabled=_CoDevEvDeAuthenticationFailureNotificationEnabled_Object((1,3,6,1,4,1,8744,5,26,1,1,10),_CoDevEvDeAuthenticationFailureNotificationEnabled_Type())
coDevEvDeAuthenticationFailureNotificationEnabled.setMaxAccess(_H)
if mibBuilder.loadTexts:coDevEvDeAuthenticationFailureNotificationEnabled.setStatus(_B)
_CoDeviceEventInfoGroup_ObjectIdentity=ObjectIdentity
coDeviceEventInfoGroup=_CoDeviceEventInfoGroup_ObjectIdentity((1,3,6,1,4,1,8744,5,26,1,2))
_CoDeviceEventTable_Object=MibTable
coDeviceEventTable=_CoDeviceEventTable_Object((1,3,6,1,4,1,8744,5,26,1,2,1))
if mibBuilder.loadTexts:coDeviceEventTable.setStatus(_B)
_CoDeviceEventEntry_Object=MibTableRow
coDeviceEventEntry=_CoDeviceEventEntry_Object((1,3,6,1,4,1,8744,5,26,1,2,1,1))
coDeviceEventEntry.setIndexNames((0,_K,_L),(0,_A,_M))
if mibBuilder.loadTexts:coDeviceEventEntry.setStatus(_B)
class _CoDevEvIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_CoDevEvIndex_Type.__name__=_J
_CoDevEvIndex_Object=MibTableColumn
coDevEvIndex=_CoDevEvIndex_Object((1,3,6,1,4,1,8744,5,26,1,2,1,1,1),_CoDevEvIndex_Type())
coDevEvIndex.setMaxAccess(_N)
if mibBuilder.loadTexts:coDevEvIndex.setStatus(_B)
_CoDevEvMacAddress_Type=MacAddress
_CoDevEvMacAddress_Object=MibTableColumn
coDevEvMacAddress=_CoDevEvMacAddress_Object((1,3,6,1,4,1,8744,5,26,1,2,1,1,2),_CoDevEvMacAddress_Type())
coDevEvMacAddress.setMaxAccess(_I)
if mibBuilder.loadTexts:coDevEvMacAddress.setStatus(_B)
_CoDeviceEventDetailTable_Object=MibTable
coDeviceEventDetailTable=_CoDeviceEventDetailTable_Object((1,3,6,1,4,1,8744,5,26,1,2,2))
if mibBuilder.loadTexts:coDeviceEventDetailTable.setStatus(_B)
_CoDeviceEventDetailEntry_Object=MibTableRow
coDeviceEventDetailEntry=_CoDeviceEventDetailEntry_Object((1,3,6,1,4,1,8744,5,26,1,2,2,1))
coDeviceEventDetailEntry.setIndexNames((0,_K,_L),(0,_A,_M),(0,_A,_O))
if mibBuilder.loadTexts:coDeviceEventDetailEntry.setStatus(_B)
class _CoDevEvLogIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_CoDevEvLogIndex_Type.__name__=_J
_CoDevEvLogIndex_Object=MibTableColumn
coDevEvLogIndex=_CoDevEvLogIndex_Object((1,3,6,1,4,1,8744,5,26,1,2,2,1,1),_CoDevEvLogIndex_Type())
coDevEvLogIndex.setMaxAccess(_N)
if mibBuilder.loadTexts:coDevEvLogIndex.setStatus(_B)
_CoDevEvDetMacAddress_Type=MacAddress
_CoDevEvDetMacAddress_Object=MibTableColumn
coDevEvDetMacAddress=_CoDevEvDetMacAddress_Object((1,3,6,1,4,1,8744,5,26,1,2,2,1,2),_CoDevEvDetMacAddress_Type())
coDevEvDetMacAddress.setMaxAccess(_I)
if mibBuilder.loadTexts:coDevEvDetMacAddress.setStatus(_B)
_CoDevEvTime_Type=DisplayString
_CoDevEvTime_Object=MibTableColumn
coDevEvTime=_CoDevEvTime_Object((1,3,6,1,4,1,8744,5,26,1,2,2,1,3),_CoDevEvTime_Type())
coDevEvTime.setMaxAccess(_I)
if mibBuilder.loadTexts:coDevEvTime.setStatus(_B)
_CoDevEvSSID_Type=ColubrisSSIDOrNone
_CoDevEvSSID_Object=MibTableColumn
coDevEvSSID=_CoDevEvSSID_Object((1,3,6,1,4,1,8744,5,26,1,2,2,1,4),_CoDevEvSSID_Type())
coDevEvSSID.setMaxAccess(_I)
if mibBuilder.loadTexts:coDevEvSSID.setStatus(_B)
class _CoDevEvRadioIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_CoDevEvRadioIndex_Type.__name__=_J
_CoDevEvRadioIndex_Object=MibTableColumn
coDevEvRadioIndex=_CoDevEvRadioIndex_Object((1,3,6,1,4,1,8744,5,26,1,2,2,1,5),_CoDevEvRadioIndex_Type())
coDevEvRadioIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:coDevEvRadioIndex.setStatus(_B)
_CoDevEvDuplicateCount_Type=Unsigned32
_CoDevEvDuplicateCount_Object=MibTableColumn
coDevEvDuplicateCount=_CoDevEvDuplicateCount_Object((1,3,6,1,4,1,8744,5,26,1,2,2,1,6),_CoDevEvDuplicateCount_Type())
coDevEvDuplicateCount.setMaxAccess(_I)
if mibBuilder.loadTexts:coDevEvDuplicateCount.setStatus(_B)
class _CoDevEvCategory_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('wireless',1),('ieee802dot1x',2),('wpa',3),('macAuthentication',4),('dhcpServer',5),('pptpL2tp',6),('ipSec',7),(_P,8)))
_CoDevEvCategory_Type.__name__=_J
_CoDevEvCategory_Object=MibTableColumn
coDevEvCategory=_CoDevEvCategory_Object((1,3,6,1,4,1,8744,5,26,1,2,2,1,7),_CoDevEvCategory_Type())
coDevEvCategory.setMaxAccess(_I)
if mibBuilder.loadTexts:coDevEvCategory.setStatus(_B)
class _CoDevEvOperation_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('association',1),('authentication',2),('authorization',3),('encryption',4),('addressAllocation',5),('vpnAuthentication',6),('vpnAddressAllocation',7),(_P,8)))
_CoDevEvOperation_Type.__name__=_J
_CoDevEvOperation_Object=MibTableColumn
coDevEvOperation=_CoDevEvOperation_Object((1,3,6,1,4,1,8744,5,26,1,2,2,1,8),_CoDevEvOperation_Type())
coDevEvOperation.setMaxAccess(_I)
if mibBuilder.loadTexts:coDevEvOperation.setStatus(_B)
_CoDevEvStatus_Type=DisplayString
_CoDevEvStatus_Object=MibTableColumn
coDevEvStatus=_CoDevEvStatus_Object((1,3,6,1,4,1,8744,5,26,1,2,2,1,9),_CoDevEvStatus_Type())
coDevEvStatus.setMaxAccess(_I)
if mibBuilder.loadTexts:coDevEvStatus.setStatus(_B)
_CoDevEvOptionalData_Type=DisplayString
_CoDevEvOptionalData_Object=MibTableColumn
coDevEvOptionalData=_CoDevEvOptionalData_Object((1,3,6,1,4,1,8744,5,26,1,2,2,1,10),_CoDevEvOptionalData_Type())
coDevEvOptionalData.setMaxAccess(_I)
if mibBuilder.loadTexts:coDevEvOptionalData.setStatus(_B)
_ColubrisDeviceEventMIBNotificationPrefix_ObjectIdentity=ObjectIdentity
colubrisDeviceEventMIBNotificationPrefix=_ColubrisDeviceEventMIBNotificationPrefix_ObjectIdentity((1,3,6,1,4,1,8744,5,26,2))
_ColubrisDeviceEventMIBNotifications_ObjectIdentity=ObjectIdentity
colubrisDeviceEventMIBNotifications=_ColubrisDeviceEventMIBNotifications_ObjectIdentity((1,3,6,1,4,1,8744,5,26,2,0))
_ColubrisDeviceEventMIBConformance_ObjectIdentity=ObjectIdentity
colubrisDeviceEventMIBConformance=_ColubrisDeviceEventMIBConformance_ObjectIdentity((1,3,6,1,4,1,8744,5,26,3))
_ColubrisDeviceEventMIBCompliances_ObjectIdentity=ObjectIdentity
colubrisDeviceEventMIBCompliances=_ColubrisDeviceEventMIBCompliances_ObjectIdentity((1,3,6,1,4,1,8744,5,26,3,1))
_ColubrisDeviceEventMIBGroups_ObjectIdentity=ObjectIdentity
colubrisDeviceEventMIBGroups=_ColubrisDeviceEventMIBGroups_ObjectIdentity((1,3,6,1,4,1,8744,5,26,3,2))
colubrisDeviceEventConfigMIBGroup=ObjectGroup((1,3,6,1,4,1,8744,5,26,3,2,1))
colubrisDeviceEventConfigMIBGroup.setObjects(*((_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z)))
if mibBuilder.loadTexts:colubrisDeviceEventConfigMIBGroup.setStatus(_B)
colubrisDeviceEventInfoMIBGroup=ObjectGroup((1,3,6,1,4,1,8744,5,26,3,2,2))
colubrisDeviceEventInfoMIBGroup.setObjects(*((_A,_C),(_A,_a),(_A,_b),(_A,_D),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_E),(_A,_F)))
if mibBuilder.loadTexts:colubrisDeviceEventInfoMIBGroup.setStatus(_B)
coDeviceEventSuccessfulAssociation=NotificationType((1,3,6,1,4,1,8744,5,26,2,0,1))
coDeviceEventSuccessfulAssociation.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_F)))
if mibBuilder.loadTexts:coDeviceEventSuccessfulAssociation.setStatus(_B)
coDeviceEventAssociationFailure=NotificationType((1,3,6,1,4,1,8744,5,26,2,0,2))
coDeviceEventAssociationFailure.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_F)))
if mibBuilder.loadTexts:coDeviceEventAssociationFailure.setStatus(_B)
coDeviceEventSuccessfulReAssociation=NotificationType((1,3,6,1,4,1,8744,5,26,2,0,3))
coDeviceEventSuccessfulReAssociation.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_F)))
if mibBuilder.loadTexts:coDeviceEventSuccessfulReAssociation.setStatus(_B)
coDeviceEventReAssociationFailure=NotificationType((1,3,6,1,4,1,8744,5,26,2,0,4))
coDeviceEventReAssociationFailure.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_F)))
if mibBuilder.loadTexts:coDeviceEventReAssociationFailure.setStatus(_B)
coDeviceEventSuccessfulAuthentication=NotificationType((1,3,6,1,4,1,8744,5,26,2,0,5))
coDeviceEventSuccessfulAuthentication.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_F)))
if mibBuilder.loadTexts:coDeviceEventSuccessfulAuthentication.setStatus(_B)
coDeviceEventAuthenticationFailure=NotificationType((1,3,6,1,4,1,8744,5,26,2,0,6))
coDeviceEventAuthenticationFailure.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_F)))
if mibBuilder.loadTexts:coDeviceEventAuthenticationFailure.setStatus(_B)
coDeviceEventSuccessfulDisAssociation=NotificationType((1,3,6,1,4,1,8744,5,26,2,0,7))
coDeviceEventSuccessfulDisAssociation.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_F)))
if mibBuilder.loadTexts:coDeviceEventSuccessfulDisAssociation.setStatus(_B)
coDeviceEventDisAssociationFailure=NotificationType((1,3,6,1,4,1,8744,5,26,2,0,8))
coDeviceEventDisAssociationFailure.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_F)))
if mibBuilder.loadTexts:coDeviceEventDisAssociationFailure.setStatus(_B)
coDeviceEventSuccessfulDeAuthentication=NotificationType((1,3,6,1,4,1,8744,5,26,2,0,9))
coDeviceEventSuccessfulDeAuthentication.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_F)))
if mibBuilder.loadTexts:coDeviceEventSuccessfulDeAuthentication.setStatus(_B)
coDeviceEventDeAuthenticationFailure=NotificationType((1,3,6,1,4,1,8744,5,26,2,0,10))
coDeviceEventDeAuthenticationFailure.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_F)))
if mibBuilder.loadTexts:coDeviceEventDeAuthenticationFailure.setStatus(_B)
colubrisDeviceEventNotificationGroup=NotificationGroup((1,3,6,1,4,1,8744,5,26,3,2,3))
colubrisDeviceEventNotificationGroup.setObjects(*((_A,_g),(_A,_h),(_A,_i),(_A,_j),(_A,_k),(_A,_l),(_A,_m),(_A,_n),(_A,_o),(_A,_p)))
if mibBuilder.loadTexts:colubrisDeviceEventNotificationGroup.setStatus(_B)
colubrisDeviceEventMIBCompliance=ModuleCompliance((1,3,6,1,4,1,8744,5,26,3,1,1))
colubrisDeviceEventMIBCompliance.setObjects(*((_A,_q),(_A,_r),(_A,_s)))
if mibBuilder.loadTexts:colubrisDeviceEventMIBCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'colubrisDeviceEventMIB':colubrisDeviceEventMIB,'colubrisDeviceEventMIBObjects':colubrisDeviceEventMIBObjects,'coDeviceEventConfigGroup':coDeviceEventConfigGroup,_Q:coDevEvSuccessfulAssociationNotificationEnabled,_R:coDevEvAssociationFailureNotificationEnabled,_S:coDevEvSuccessfulReAssociationNotificationEnabled,_T:coDevEvReAssociationFailureNotificationEnabled,_U:coDevEvSuccessfulAuthenticationNotificationEnabled,_V:coDevEvAuthenticationFailureNotificationEnabled,_W:coDevEvSuccessfulDisAssociationNotificationEnabled,_X:coDevEvDisAssociationFailureNotificationEnabled,_Y:coDevEvSuccessfulDeAuthenticationNotificationEnabled,_Z:coDevEvDeAuthenticationFailureNotificationEnabled,'coDeviceEventInfoGroup':coDeviceEventInfoGroup,'coDeviceEventTable':coDeviceEventTable,'coDeviceEventEntry':coDeviceEventEntry,_M:coDevEvIndex,_C:coDevEvMacAddress,'coDeviceEventDetailTable':coDeviceEventDetailTable,'coDeviceEventDetailEntry':coDeviceEventDetailEntry,_O:coDevEvLogIndex,_a:coDevEvDetMacAddress,_b:coDevEvTime,_D:coDevEvSSID,_c:coDevEvRadioIndex,_d:coDevEvDuplicateCount,_e:coDevEvCategory,_f:coDevEvOperation,_E:coDevEvStatus,_F:coDevEvOptionalData,'colubrisDeviceEventMIBNotificationPrefix':colubrisDeviceEventMIBNotificationPrefix,'colubrisDeviceEventMIBNotifications':colubrisDeviceEventMIBNotifications,_g:coDeviceEventSuccessfulAssociation,_h:coDeviceEventAssociationFailure,_i:coDeviceEventSuccessfulReAssociation,_j:coDeviceEventReAssociationFailure,_k:coDeviceEventSuccessfulAuthentication,_l:coDeviceEventAuthenticationFailure,_m:coDeviceEventSuccessfulDisAssociation,_n:coDeviceEventDisAssociationFailure,_o:coDeviceEventSuccessfulDeAuthentication,_p:coDeviceEventDeAuthenticationFailure,'colubrisDeviceEventMIBConformance':colubrisDeviceEventMIBConformance,'colubrisDeviceEventMIBCompliances':colubrisDeviceEventMIBCompliances,'colubrisDeviceEventMIBCompliance':colubrisDeviceEventMIBCompliance,'colubrisDeviceEventMIBGroups':colubrisDeviceEventMIBGroups,_q:colubrisDeviceEventConfigMIBGroup,_r:colubrisDeviceEventInfoMIBGroup,_s:colubrisDeviceEventNotificationGroup})