_N='colubrisUserAccountStatusMIBGroup'
_M='coUserAccExpirationTime'
_L='coUserAccStatus'
_K='coUserAccRemainingSessionTime'
_J='coUserAccFirstLoginTime'
_I='coUserAccRemainingOnlineTime'
_H='coUserAccPlanName'
_G='coUserAccUserName'
_F='seconds'
_E='coUserAccIndex'
_D='Integer32'
_C='read-only'
_B='COLUBRIS-USER-ACCOUNT-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
colubrisMgmtV2,=mibBuilder.importSymbols('COLUBRIS-SMI','colubrisMgmtV2')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
colubrisUserAccountMIB=ModuleIdentity((1,3,6,1,4,1,8744,5,35))
_ColubrisUserAccountMIBObjects_ObjectIdentity=ObjectIdentity
colubrisUserAccountMIBObjects=_ColubrisUserAccountMIBObjects_ObjectIdentity((1,3,6,1,4,1,8744,5,35,1))
_CoUserAccountStatusGroup_ObjectIdentity=ObjectIdentity
coUserAccountStatusGroup=_CoUserAccountStatusGroup_ObjectIdentity((1,3,6,1,4,1,8744,5,35,1,1))
_CoUserAccountStatusTable_Object=MibTable
coUserAccountStatusTable=_CoUserAccountStatusTable_Object((1,3,6,1,4,1,8744,5,35,1,1,1))
if mibBuilder.loadTexts:coUserAccountStatusTable.setStatus(_A)
_CoUserAccountStatusEntry_Object=MibTableRow
coUserAccountStatusEntry=_CoUserAccountStatusEntry_Object((1,3,6,1,4,1,8744,5,35,1,1,1,1))
coUserAccountStatusEntry.setIndexNames((0,_B,_E))
if mibBuilder.loadTexts:coUserAccountStatusEntry.setStatus(_A)
class _CoUserAccIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_CoUserAccIndex_Type.__name__=_D
_CoUserAccIndex_Object=MibTableColumn
coUserAccIndex=_CoUserAccIndex_Object((1,3,6,1,4,1,8744,5,35,1,1,1,1,1),_CoUserAccIndex_Type())
coUserAccIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:coUserAccIndex.setStatus(_A)
_CoUserAccUserName_Type=DisplayString
_CoUserAccUserName_Object=MibTableColumn
coUserAccUserName=_CoUserAccUserName_Object((1,3,6,1,4,1,8744,5,35,1,1,1,1,2),_CoUserAccUserName_Type())
coUserAccUserName.setMaxAccess(_C)
if mibBuilder.loadTexts:coUserAccUserName.setStatus(_A)
_CoUserAccPlanName_Type=DisplayString
_CoUserAccPlanName_Object=MibTableColumn
coUserAccPlanName=_CoUserAccPlanName_Object((1,3,6,1,4,1,8744,5,35,1,1,1,1,3),_CoUserAccPlanName_Type())
coUserAccPlanName.setMaxAccess(_C)
if mibBuilder.loadTexts:coUserAccPlanName.setStatus(_A)
_CoUserAccRemainingOnlineTime_Type=Integer32
_CoUserAccRemainingOnlineTime_Object=MibTableColumn
coUserAccRemainingOnlineTime=_CoUserAccRemainingOnlineTime_Object((1,3,6,1,4,1,8744,5,35,1,1,1,1,4),_CoUserAccRemainingOnlineTime_Type())
coUserAccRemainingOnlineTime.setMaxAccess(_C)
if mibBuilder.loadTexts:coUserAccRemainingOnlineTime.setStatus(_A)
if mibBuilder.loadTexts:coUserAccRemainingOnlineTime.setUnits(_F)
_CoUserAccFirstLoginTime_Type=DisplayString
_CoUserAccFirstLoginTime_Object=MibTableColumn
coUserAccFirstLoginTime=_CoUserAccFirstLoginTime_Object((1,3,6,1,4,1,8744,5,35,1,1,1,1,5),_CoUserAccFirstLoginTime_Type())
coUserAccFirstLoginTime.setMaxAccess(_C)
if mibBuilder.loadTexts:coUserAccFirstLoginTime.setStatus(_A)
_CoUserAccRemainingSessionTime_Type=Integer32
_CoUserAccRemainingSessionTime_Object=MibTableColumn
coUserAccRemainingSessionTime=_CoUserAccRemainingSessionTime_Object((1,3,6,1,4,1,8744,5,35,1,1,1,1,6),_CoUserAccRemainingSessionTime_Type())
coUserAccRemainingSessionTime.setMaxAccess(_C)
if mibBuilder.loadTexts:coUserAccRemainingSessionTime.setStatus(_A)
if mibBuilder.loadTexts:coUserAccRemainingSessionTime.setUnits(_F)
class _CoUserAccStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('valid',1),('invalid',2)))
_CoUserAccStatus_Type.__name__=_D
_CoUserAccStatus_Object=MibTableColumn
coUserAccStatus=_CoUserAccStatus_Object((1,3,6,1,4,1,8744,5,35,1,1,1,1,7),_CoUserAccStatus_Type())
coUserAccStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:coUserAccStatus.setStatus(_A)
_CoUserAccExpirationTime_Type=DisplayString
_CoUserAccExpirationTime_Object=MibTableColumn
coUserAccExpirationTime=_CoUserAccExpirationTime_Object((1,3,6,1,4,1,8744,5,35,1,1,1,1,8),_CoUserAccExpirationTime_Type())
coUserAccExpirationTime.setMaxAccess(_C)
if mibBuilder.loadTexts:coUserAccExpirationTime.setStatus(_A)
_ColubrisUserAccountMIBNotificationPrefix_ObjectIdentity=ObjectIdentity
colubrisUserAccountMIBNotificationPrefix=_ColubrisUserAccountMIBNotificationPrefix_ObjectIdentity((1,3,6,1,4,1,8744,5,35,2))
_ColubrisUserAccountMIBNotifications_ObjectIdentity=ObjectIdentity
colubrisUserAccountMIBNotifications=_ColubrisUserAccountMIBNotifications_ObjectIdentity((1,3,6,1,4,1,8744,5,35,2,0))
_ColubrisUserAccountMIBConformance_ObjectIdentity=ObjectIdentity
colubrisUserAccountMIBConformance=_ColubrisUserAccountMIBConformance_ObjectIdentity((1,3,6,1,4,1,8744,5,35,3))
_ColubrisUserAccountMIBCompliances_ObjectIdentity=ObjectIdentity
colubrisUserAccountMIBCompliances=_ColubrisUserAccountMIBCompliances_ObjectIdentity((1,3,6,1,4,1,8744,5,35,3,1))
_ColubrisUserAccountMIBGroups_ObjectIdentity=ObjectIdentity
colubrisUserAccountMIBGroups=_ColubrisUserAccountMIBGroups_ObjectIdentity((1,3,6,1,4,1,8744,5,35,3,2))
colubrisUserAccountStatusMIBGroup=ObjectGroup((1,3,6,1,4,1,8744,5,35,3,2,1))
colubrisUserAccountStatusMIBGroup.setObjects(*((_B,_G),(_B,_H),(_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M)))
if mibBuilder.loadTexts:colubrisUserAccountStatusMIBGroup.setStatus(_A)
colubrisUserAccountMIBCompliance=ModuleCompliance((1,3,6,1,4,1,8744,5,35,3,1,1))
colubrisUserAccountMIBCompliance.setObjects((_B,_N))
if mibBuilder.loadTexts:colubrisUserAccountMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'colubrisUserAccountMIB':colubrisUserAccountMIB,'colubrisUserAccountMIBObjects':colubrisUserAccountMIBObjects,'coUserAccountStatusGroup':coUserAccountStatusGroup,'coUserAccountStatusTable':coUserAccountStatusTable,'coUserAccountStatusEntry':coUserAccountStatusEntry,_E:coUserAccIndex,_G:coUserAccUserName,_H:coUserAccPlanName,_I:coUserAccRemainingOnlineTime,_J:coUserAccFirstLoginTime,_K:coUserAccRemainingSessionTime,_L:coUserAccStatus,_M:coUserAccExpirationTime,'colubrisUserAccountMIBNotificationPrefix':colubrisUserAccountMIBNotificationPrefix,'colubrisUserAccountMIBNotifications':colubrisUserAccountMIBNotifications,'colubrisUserAccountMIBConformance':colubrisUserAccountMIBConformance,'colubrisUserAccountMIBCompliances':colubrisUserAccountMIBCompliances,'colubrisUserAccountMIBCompliance':colubrisUserAccountMIBCompliance,'colubrisUserAccountMIBGroups':colubrisUserAccountMIBGroups,_N:colubrisUserAccountStatusMIBGroup})