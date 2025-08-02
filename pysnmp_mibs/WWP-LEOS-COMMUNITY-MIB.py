_G='wwpLeosNotifIndex'
_F='wwpLeosCommunityIndex'
_E='WWP-LEOS-COMMUNITY-MIB'
_D='read-only'
_C='Integer32'
_B='read-create'
_A='deprecated'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
wwpModulesLeos,=mibBuilder.importSymbols('WWP-SMI','wwpModulesLeos')
wwpLeosCommunityMIB=ModuleIdentity((1,3,6,1,4,1,6141,2,60,22))
if mibBuilder.loadTexts:wwpLeosCommunityMIB.setRevisions(('2001-04-03 17:00',))
_WwpLeosCommunityMIBObjects_ObjectIdentity=ObjectIdentity
wwpLeosCommunityMIBObjects=_WwpLeosCommunityMIBObjects_ObjectIdentity((1,3,6,1,4,1,6141,2,60,22,1))
_WwpLeosCommunity_ObjectIdentity=ObjectIdentity
wwpLeosCommunity=_WwpLeosCommunity_ObjectIdentity((1,3,6,1,4,1,6141,2,60,22,1,1))
_WwpLeosCommunityTable_Object=MibTable
wwpLeosCommunityTable=_WwpLeosCommunityTable_Object((1,3,6,1,4,1,6141,2,60,22,1,1,1))
if mibBuilder.loadTexts:wwpLeosCommunityTable.setStatus(_A)
_WwpLeosCommunityEntry_Object=MibTableRow
wwpLeosCommunityEntry=_WwpLeosCommunityEntry_Object((1,3,6,1,4,1,6141,2,60,22,1,1,1,1))
wwpLeosCommunityEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:wwpLeosCommunityEntry.setStatus(_A)
class _WwpLeosCommunityIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_WwpLeosCommunityIndex_Type.__name__=_C
_WwpLeosCommunityIndex_Object=MibTableColumn
wwpLeosCommunityIndex=_WwpLeosCommunityIndex_Object((1,3,6,1,4,1,6141,2,60,22,1,1,1,1,1),_WwpLeosCommunityIndex_Type())
wwpLeosCommunityIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosCommunityIndex.setStatus(_A)
_WwpLeosCommunityName_Type=DisplayString
_WwpLeosCommunityName_Object=MibTableColumn
wwpLeosCommunityName=_WwpLeosCommunityName_Object((1,3,6,1,4,1,6141,2,60,22,1,1,1,1,2),_WwpLeosCommunityName_Type())
wwpLeosCommunityName.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosCommunityName.setStatus(_A)
_WwpLeosCommunityAddr_Type=DisplayString
_WwpLeosCommunityAddr_Object=MibTableColumn
wwpLeosCommunityAddr=_WwpLeosCommunityAddr_Object((1,3,6,1,4,1,6141,2,60,22,1,1,1,1,3),_WwpLeosCommunityAddr_Type())
wwpLeosCommunityAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosCommunityAddr.setStatus(_A)
_WwpLeosCommunityResolvedIp_Type=IpAddress
_WwpLeosCommunityResolvedIp_Object=MibTableColumn
wwpLeosCommunityResolvedIp=_WwpLeosCommunityResolvedIp_Object((1,3,6,1,4,1,6141,2,60,22,1,1,1,1,4),_WwpLeosCommunityResolvedIp_Type())
wwpLeosCommunityResolvedIp.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosCommunityResolvedIp.setStatus(_A)
class _WwpLeosCommunityRights_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('readOnly',1),('readWrite',2)))
_WwpLeosCommunityRights_Type.__name__=_C
_WwpLeosCommunityRights_Object=MibTableColumn
wwpLeosCommunityRights=_WwpLeosCommunityRights_Object((1,3,6,1,4,1,6141,2,60,22,1,1,1,1,5),_WwpLeosCommunityRights_Type())
wwpLeosCommunityRights.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosCommunityRights.setStatus(_A)
_WwpLeosCommunityStatus_Type=RowStatus
_WwpLeosCommunityStatus_Object=MibTableColumn
wwpLeosCommunityStatus=_WwpLeosCommunityStatus_Object((1,3,6,1,4,1,6141,2,60,22,1,1,1,1,6),_WwpLeosCommunityStatus_Type())
wwpLeosCommunityStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosCommunityStatus.setStatus(_A)
_WwpLeosNotifCommunityTable_Object=MibTable
wwpLeosNotifCommunityTable=_WwpLeosNotifCommunityTable_Object((1,3,6,1,4,1,6141,2,60,22,1,1,2))
if mibBuilder.loadTexts:wwpLeosNotifCommunityTable.setStatus(_A)
_WwpLeosNotifCommunityEntry_Object=MibTableRow
wwpLeosNotifCommunityEntry=_WwpLeosNotifCommunityEntry_Object((1,3,6,1,4,1,6141,2,60,22,1,1,2,1))
wwpLeosNotifCommunityEntry.setIndexNames((0,_E,_G))
if mibBuilder.loadTexts:wwpLeosNotifCommunityEntry.setStatus(_A)
class _WwpLeosNotifIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_WwpLeosNotifIndex_Type.__name__=_C
_WwpLeosNotifIndex_Object=MibTableColumn
wwpLeosNotifIndex=_WwpLeosNotifIndex_Object((1,3,6,1,4,1,6141,2,60,22,1,1,2,1,1),_WwpLeosNotifIndex_Type())
wwpLeosNotifIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosNotifIndex.setStatus(_A)
_WwpLeosNotifCommunityName_Type=DisplayString
_WwpLeosNotifCommunityName_Object=MibTableColumn
wwpLeosNotifCommunityName=_WwpLeosNotifCommunityName_Object((1,3,6,1,4,1,6141,2,60,22,1,1,2,1,2),_WwpLeosNotifCommunityName_Type())
wwpLeosNotifCommunityName.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosNotifCommunityName.setStatus(_A)
_WwpLeosNotifCommunityDestAddr_Type=DisplayString
_WwpLeosNotifCommunityDestAddr_Object=MibTableColumn
wwpLeosNotifCommunityDestAddr=_WwpLeosNotifCommunityDestAddr_Object((1,3,6,1,4,1,6141,2,60,22,1,1,2,1,3),_WwpLeosNotifCommunityDestAddr_Type())
wwpLeosNotifCommunityDestAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosNotifCommunityDestAddr.setStatus(_A)
_WwpLeosNotifCommunityResolvedIpAddr_Type=IpAddress
_WwpLeosNotifCommunityResolvedIpAddr_Object=MibTableColumn
wwpLeosNotifCommunityResolvedIpAddr=_WwpLeosNotifCommunityResolvedIpAddr_Object((1,3,6,1,4,1,6141,2,60,22,1,1,2,1,4),_WwpLeosNotifCommunityResolvedIpAddr_Type())
wwpLeosNotifCommunityResolvedIpAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosNotifCommunityResolvedIpAddr.setStatus(_A)
_WwpLeosNotifCommunityStatus_Type=RowStatus
_WwpLeosNotifCommunityStatus_Object=MibTableColumn
wwpLeosNotifCommunityStatus=_WwpLeosNotifCommunityStatus_Object((1,3,6,1,4,1,6141,2,60,22,1,1,2,1,5),_WwpLeosNotifCommunityStatus_Type())
wwpLeosNotifCommunityStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosNotifCommunityStatus.setStatus(_A)
_WwpLeosCommunityMIBNotificationPrefix_ObjectIdentity=ObjectIdentity
wwpLeosCommunityMIBNotificationPrefix=_WwpLeosCommunityMIBNotificationPrefix_ObjectIdentity((1,3,6,1,4,1,6141,2,60,22,2))
_WwpLeosCommunityMIBNotifications_ObjectIdentity=ObjectIdentity
wwpLeosCommunityMIBNotifications=_WwpLeosCommunityMIBNotifications_ObjectIdentity((1,3,6,1,4,1,6141,2,60,22,2,0))
_WwpLeosCommunityMIBConformance_ObjectIdentity=ObjectIdentity
wwpLeosCommunityMIBConformance=_WwpLeosCommunityMIBConformance_ObjectIdentity((1,3,6,1,4,1,6141,2,60,22,3))
_WwpLeosCommunityMIBCompliances_ObjectIdentity=ObjectIdentity
wwpLeosCommunityMIBCompliances=_WwpLeosCommunityMIBCompliances_ObjectIdentity((1,3,6,1,4,1,6141,2,60,22,3,1))
_WwpLeosCommunityMIBGroups_ObjectIdentity=ObjectIdentity
wwpLeosCommunityMIBGroups=_WwpLeosCommunityMIBGroups_ObjectIdentity((1,3,6,1,4,1,6141,2,60,22,3,2))
mibBuilder.exportSymbols(_E,**{'wwpLeosCommunityMIB':wwpLeosCommunityMIB,'wwpLeosCommunityMIBObjects':wwpLeosCommunityMIBObjects,'wwpLeosCommunity':wwpLeosCommunity,'wwpLeosCommunityTable':wwpLeosCommunityTable,'wwpLeosCommunityEntry':wwpLeosCommunityEntry,_F:wwpLeosCommunityIndex,'wwpLeosCommunityName':wwpLeosCommunityName,'wwpLeosCommunityAddr':wwpLeosCommunityAddr,'wwpLeosCommunityResolvedIp':wwpLeosCommunityResolvedIp,'wwpLeosCommunityRights':wwpLeosCommunityRights,'wwpLeosCommunityStatus':wwpLeosCommunityStatus,'wwpLeosNotifCommunityTable':wwpLeosNotifCommunityTable,'wwpLeosNotifCommunityEntry':wwpLeosNotifCommunityEntry,_G:wwpLeosNotifIndex,'wwpLeosNotifCommunityName':wwpLeosNotifCommunityName,'wwpLeosNotifCommunityDestAddr':wwpLeosNotifCommunityDestAddr,'wwpLeosNotifCommunityResolvedIpAddr':wwpLeosNotifCommunityResolvedIpAddr,'wwpLeosNotifCommunityStatus':wwpLeosNotifCommunityStatus,'wwpLeosCommunityMIBNotificationPrefix':wwpLeosCommunityMIBNotificationPrefix,'wwpLeosCommunityMIBNotifications':wwpLeosCommunityMIBNotifications,'wwpLeosCommunityMIBConformance':wwpLeosCommunityMIBConformance,'wwpLeosCommunityMIBCompliances':wwpLeosCommunityMIBCompliances,'wwpLeosCommunityMIBGroups':wwpLeosCommunityMIBGroups})