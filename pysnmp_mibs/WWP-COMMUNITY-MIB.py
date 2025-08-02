_K='wwpNotifCommunityDestAddr'
_J='wwpNotifCommunityName'
_I='read-create'
_H='read-write'
_G='wwpCommunityIpAddress'
_F='wwpCommunityName'
_E='Integer32'
_D='OctetString'
_C='read-only'
_B='WWP-COMMUNITY-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_D,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
wwpModules,=mibBuilder.importSymbols('WWP-SMI','wwpModules')
wwpCommunityMIB=ModuleIdentity((1,3,6,1,4,1,6141,2,32))
if mibBuilder.loadTexts:wwpCommunityMIB.setRevisions(('2001-04-03 17:00',))
_WwpCommunityMIBObjects_ObjectIdentity=ObjectIdentity
wwpCommunityMIBObjects=_WwpCommunityMIBObjects_ObjectIdentity((1,3,6,1,4,1,6141,2,32,1))
_WwpCommunity_ObjectIdentity=ObjectIdentity
wwpCommunity=_WwpCommunity_ObjectIdentity((1,3,6,1,4,1,6141,2,32,1,1))
_WwpCommunityTable_Object=MibTable
wwpCommunityTable=_WwpCommunityTable_Object((1,3,6,1,4,1,6141,2,32,1,1,1))
if mibBuilder.loadTexts:wwpCommunityTable.setStatus(_A)
_WwpCommunityEntry_Object=MibTableRow
wwpCommunityEntry=_WwpCommunityEntry_Object((1,3,6,1,4,1,6141,2,32,1,1,1,1))
wwpCommunityEntry.setIndexNames((0,_B,_F),(0,_B,_G))
if mibBuilder.loadTexts:wwpCommunityEntry.setStatus(_A)
class _WwpCommunityName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_WwpCommunityName_Type.__name__=_D
_WwpCommunityName_Object=MibTableColumn
wwpCommunityName=_WwpCommunityName_Object((1,3,6,1,4,1,6141,2,32,1,1,1,1,1),_WwpCommunityName_Type())
wwpCommunityName.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpCommunityName.setStatus(_A)
_WwpCommunityIpAddress_Type=IpAddress
_WwpCommunityIpAddress_Object=MibTableColumn
wwpCommunityIpAddress=_WwpCommunityIpAddress_Object((1,3,6,1,4,1,6141,2,32,1,1,1,1,2),_WwpCommunityIpAddress_Type())
wwpCommunityIpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpCommunityIpAddress.setStatus(_A)
class _WwpCommunityRights_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('readOnly',1),('readWrite',2)))
_WwpCommunityRights_Type.__name__=_E
_WwpCommunityRights_Object=MibTableColumn
wwpCommunityRights=_WwpCommunityRights_Object((1,3,6,1,4,1,6141,2,32,1,1,1,1,3),_WwpCommunityRights_Type())
wwpCommunityRights.setMaxAccess(_H)
if mibBuilder.loadTexts:wwpCommunityRights.setStatus(_A)
_WwpCommunityStatus_Type=RowStatus
_WwpCommunityStatus_Object=MibTableColumn
wwpCommunityStatus=_WwpCommunityStatus_Object((1,3,6,1,4,1,6141,2,32,1,1,1,1,4),_WwpCommunityStatus_Type())
wwpCommunityStatus.setMaxAccess(_I)
if mibBuilder.loadTexts:wwpCommunityStatus.setStatus(_A)
_WwpNotifCommunityTable_Object=MibTable
wwpNotifCommunityTable=_WwpNotifCommunityTable_Object((1,3,6,1,4,1,6141,2,32,1,1,2))
if mibBuilder.loadTexts:wwpNotifCommunityTable.setStatus(_A)
_WwpNotifCommunityEntry_Object=MibTableRow
wwpNotifCommunityEntry=_WwpNotifCommunityEntry_Object((1,3,6,1,4,1,6141,2,32,1,1,2,1))
wwpNotifCommunityEntry.setIndexNames((0,_B,_J),(0,_B,_K))
if mibBuilder.loadTexts:wwpNotifCommunityEntry.setStatus(_A)
class _WwpNotifCommunityName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_WwpNotifCommunityName_Type.__name__=_D
_WwpNotifCommunityName_Object=MibTableColumn
wwpNotifCommunityName=_WwpNotifCommunityName_Object((1,3,6,1,4,1,6141,2,32,1,1,2,1,1),_WwpNotifCommunityName_Type())
wwpNotifCommunityName.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpNotifCommunityName.setStatus(_A)
_WwpNotifCommunityDestAddr_Type=IpAddress
_WwpNotifCommunityDestAddr_Object=MibTableColumn
wwpNotifCommunityDestAddr=_WwpNotifCommunityDestAddr_Object((1,3,6,1,4,1,6141,2,32,1,1,2,1,2),_WwpNotifCommunityDestAddr_Type())
wwpNotifCommunityDestAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpNotifCommunityDestAddr.setStatus(_A)
_WwpNotifCommunityStatus_Type=RowStatus
_WwpNotifCommunityStatus_Object=MibTableColumn
wwpNotifCommunityStatus=_WwpNotifCommunityStatus_Object((1,3,6,1,4,1,6141,2,32,1,1,2,1,3),_WwpNotifCommunityStatus_Type())
wwpNotifCommunityStatus.setMaxAccess(_I)
if mibBuilder.loadTexts:wwpNotifCommunityStatus.setStatus(_A)
class _WwpCommunityPersist_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('none',0),('persist',1)))
_WwpCommunityPersist_Type.__name__=_E
_WwpCommunityPersist_Object=MibScalar
wwpCommunityPersist=_WwpCommunityPersist_Object((1,3,6,1,4,1,6141,2,32,1,1,3),_WwpCommunityPersist_Type())
wwpCommunityPersist.setMaxAccess(_H)
if mibBuilder.loadTexts:wwpCommunityPersist.setStatus(_A)
_WwpCommunityMIBNotificationPrefix_ObjectIdentity=ObjectIdentity
wwpCommunityMIBNotificationPrefix=_WwpCommunityMIBNotificationPrefix_ObjectIdentity((1,3,6,1,4,1,6141,2,32,2))
_WwpCommunityMIBNotifications_ObjectIdentity=ObjectIdentity
wwpCommunityMIBNotifications=_WwpCommunityMIBNotifications_ObjectIdentity((1,3,6,1,4,1,6141,2,32,2,0))
_WwpCommunityMIBConformance_ObjectIdentity=ObjectIdentity
wwpCommunityMIBConformance=_WwpCommunityMIBConformance_ObjectIdentity((1,3,6,1,4,1,6141,2,32,3))
_WwpCommunityMIBCompliances_ObjectIdentity=ObjectIdentity
wwpCommunityMIBCompliances=_WwpCommunityMIBCompliances_ObjectIdentity((1,3,6,1,4,1,6141,2,32,3,1))
_WwpCommunityMIBGroups_ObjectIdentity=ObjectIdentity
wwpCommunityMIBGroups=_WwpCommunityMIBGroups_ObjectIdentity((1,3,6,1,4,1,6141,2,32,3,2))
mibBuilder.exportSymbols(_B,**{'wwpCommunityMIB':wwpCommunityMIB,'wwpCommunityMIBObjects':wwpCommunityMIBObjects,'wwpCommunity':wwpCommunity,'wwpCommunityTable':wwpCommunityTable,'wwpCommunityEntry':wwpCommunityEntry,_F:wwpCommunityName,_G:wwpCommunityIpAddress,'wwpCommunityRights':wwpCommunityRights,'wwpCommunityStatus':wwpCommunityStatus,'wwpNotifCommunityTable':wwpNotifCommunityTable,'wwpNotifCommunityEntry':wwpNotifCommunityEntry,_J:wwpNotifCommunityName,_K:wwpNotifCommunityDestAddr,'wwpNotifCommunityStatus':wwpNotifCommunityStatus,'wwpCommunityPersist':wwpCommunityPersist,'wwpCommunityMIBNotificationPrefix':wwpCommunityMIBNotificationPrefix,'wwpCommunityMIBNotifications':wwpCommunityMIBNotifications,'wwpCommunityMIBConformance':wwpCommunityMIBConformance,'wwpCommunityMIBCompliances':wwpCommunityMIBCompliances,'wwpCommunityMIBGroups':wwpCommunityMIBGroups})