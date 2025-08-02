_R='apSwCfgActivateNotification'
_Q='apSwCfgTrapCurrentVersion'
_P='apSwCfgTrapPreviousVersion'
_O='apSwCfgBackupName'
_N='apSwCfgRunningVersion'
_M='apSwCfgCurrentVersion'
_L='apSwBootStatus'
_K='apSwBootType'
_J='apSwBootDescr'
_I='accessible-for-notify'
_H='apSwCfgBackupIndex'
_G='not-accessible'
_F='apSwBootIndex'
_E='DisplayString'
_D='read-only'
_C='Integer32'
_B='APSWINVENTORY-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
acmepacketMgmt,=mibBuilder.importSymbols('ACMEPACKET-SMI','acmepacketMgmt')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_E,'PhysAddress','TextualConvention')
apSwInventoryModule=ModuleIdentity((1,3,6,1,4,1,9148,3,4))
if mibBuilder.loadTexts:apSwInventoryModule.setRevisions(('2012-07-13 00:00',))
_ApSwInventoryMIBObjects_ObjectIdentity=ObjectIdentity
apSwInventoryMIBObjects=_ApSwInventoryMIBObjects_ObjectIdentity((1,3,6,1,4,1,9148,3,4,1))
_ApSwInventoryBootObjects_ObjectIdentity=ObjectIdentity
apSwInventoryBootObjects=_ApSwInventoryBootObjects_ObjectIdentity((1,3,6,1,4,1,9148,3,4,1,1))
_ApSwBootTable_Object=MibTable
apSwBootTable=_ApSwBootTable_Object((1,3,6,1,4,1,9148,3,4,1,1,1))
if mibBuilder.loadTexts:apSwBootTable.setStatus(_A)
_ApSwBootEntry_Object=MibTableRow
apSwBootEntry=_ApSwBootEntry_Object((1,3,6,1,4,1,9148,3,4,1,1,1,1))
apSwBootEntry.setIndexNames((0,_B,_F))
if mibBuilder.loadTexts:apSwBootEntry.setStatus(_A)
class _ApSwBootIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_ApSwBootIndex_Type.__name__=_C
_ApSwBootIndex_Object=MibTableColumn
apSwBootIndex=_ApSwBootIndex_Object((1,3,6,1,4,1,9148,3,4,1,1,1,1,1),_ApSwBootIndex_Type())
apSwBootIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:apSwBootIndex.setStatus(_A)
class _ApSwBootDescr_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,128))
_ApSwBootDescr_Type.__name__=_E
_ApSwBootDescr_Object=MibTableColumn
apSwBootDescr=_ApSwBootDescr_Object((1,3,6,1,4,1,9148,3,4,1,1,1,1,2),_ApSwBootDescr_Type())
apSwBootDescr.setMaxAccess(_D)
if mibBuilder.loadTexts:apSwBootDescr.setStatus(_A)
class _ApSwBootType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('bootImage',1),('bootLoader',2)))
_ApSwBootType_Type.__name__=_C
_ApSwBootType_Object=MibTableColumn
apSwBootType=_ApSwBootType_Object((1,3,6,1,4,1,9148,3,4,1,1,1,1,3),_ApSwBootType_Type())
apSwBootType.setMaxAccess(_D)
if mibBuilder.loadTexts:apSwBootType.setStatus(_A)
class _ApSwBootStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('currentUsing',1),('previousUsed',2)))
_ApSwBootStatus_Type.__name__=_C
_ApSwBootStatus_Object=MibTableColumn
apSwBootStatus=_ApSwBootStatus_Object((1,3,6,1,4,1,9148,3,4,1,1,1,1,4),_ApSwBootStatus_Type())
apSwBootStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:apSwBootStatus.setStatus(_A)
_ApSwInventoryCfgObjects_ObjectIdentity=ObjectIdentity
apSwInventoryCfgObjects=_ApSwInventoryCfgObjects_ObjectIdentity((1,3,6,1,4,1,9148,3,4,1,2))
class _ApSwCfgCurrentVersion_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_ApSwCfgCurrentVersion_Type.__name__=_C
_ApSwCfgCurrentVersion_Object=MibScalar
apSwCfgCurrentVersion=_ApSwCfgCurrentVersion_Object((1,3,6,1,4,1,9148,3,4,1,2,1),_ApSwCfgCurrentVersion_Type())
apSwCfgCurrentVersion.setMaxAccess(_D)
if mibBuilder.loadTexts:apSwCfgCurrentVersion.setStatus(_A)
class _ApSwCfgRunningVersion_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_ApSwCfgRunningVersion_Type.__name__=_C
_ApSwCfgRunningVersion_Object=MibScalar
apSwCfgRunningVersion=_ApSwCfgRunningVersion_Object((1,3,6,1,4,1,9148,3,4,1,2,2),_ApSwCfgRunningVersion_Type())
apSwCfgRunningVersion.setMaxAccess(_D)
if mibBuilder.loadTexts:apSwCfgRunningVersion.setStatus(_A)
_ApSwCfgBackuptable_Object=MibTable
apSwCfgBackuptable=_ApSwCfgBackuptable_Object((1,3,6,1,4,1,9148,3,4,1,2,3))
if mibBuilder.loadTexts:apSwCfgBackuptable.setStatus(_A)
_ApSwCfgBackupEntry_Object=MibTableRow
apSwCfgBackupEntry=_ApSwCfgBackupEntry_Object((1,3,6,1,4,1,9148,3,4,1,2,3,1))
apSwCfgBackupEntry.setIndexNames((0,_B,_H))
if mibBuilder.loadTexts:apSwCfgBackupEntry.setStatus(_A)
class _ApSwCfgBackupIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_ApSwCfgBackupIndex_Type.__name__=_C
_ApSwCfgBackupIndex_Object=MibTableColumn
apSwCfgBackupIndex=_ApSwCfgBackupIndex_Object((1,3,6,1,4,1,9148,3,4,1,2,3,1,1),_ApSwCfgBackupIndex_Type())
apSwCfgBackupIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:apSwCfgBackupIndex.setStatus(_A)
class _ApSwCfgBackupName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_ApSwCfgBackupName_Type.__name__=_E
_ApSwCfgBackupName_Object=MibTableColumn
apSwCfgBackupName=_ApSwCfgBackupName_Object((1,3,6,1,4,1,9148,3,4,1,2,3,1,2),_ApSwCfgBackupName_Type())
apSwCfgBackupName.setMaxAccess(_D)
if mibBuilder.loadTexts:apSwCfgBackupName.setStatus(_A)
_ApSwInventoryNotificationObjects_ObjectIdentity=ObjectIdentity
apSwInventoryNotificationObjects=_ApSwInventoryNotificationObjects_ObjectIdentity((1,3,6,1,4,1,9148,3,4,2))
_ApSwCfgNotificationObjects_ObjectIdentity=ObjectIdentity
apSwCfgNotificationObjects=_ApSwCfgNotificationObjects_ObjectIdentity((1,3,6,1,4,1,9148,3,4,2,1))
class _ApSwCfgTrapPreviousVersion_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_ApSwCfgTrapPreviousVersion_Type.__name__=_C
_ApSwCfgTrapPreviousVersion_Object=MibScalar
apSwCfgTrapPreviousVersion=_ApSwCfgTrapPreviousVersion_Object((1,3,6,1,4,1,9148,3,4,2,1,1),_ApSwCfgTrapPreviousVersion_Type())
apSwCfgTrapPreviousVersion.setMaxAccess(_I)
if mibBuilder.loadTexts:apSwCfgTrapPreviousVersion.setStatus(_A)
class _ApSwCfgTrapCurrentVersion_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_ApSwCfgTrapCurrentVersion_Type.__name__=_C
_ApSwCfgTrapCurrentVersion_Object=MibScalar
apSwCfgTrapCurrentVersion=_ApSwCfgTrapCurrentVersion_Object((1,3,6,1,4,1,9148,3,4,2,1,2),_ApSwCfgTrapCurrentVersion_Type())
apSwCfgTrapCurrentVersion.setMaxAccess(_I)
if mibBuilder.loadTexts:apSwCfgTrapCurrentVersion.setStatus(_A)
_ApSwInventoryNotificationPrefix_ObjectIdentity=ObjectIdentity
apSwInventoryNotificationPrefix=_ApSwInventoryNotificationPrefix_ObjectIdentity((1,3,6,1,4,1,9148,3,4,3))
_ApSwInventoryNotifications_ObjectIdentity=ObjectIdentity
apSwInventoryNotifications=_ApSwInventoryNotifications_ObjectIdentity((1,3,6,1,4,1,9148,3,4,3,0))
_ApSwInventoryConformance_ObjectIdentity=ObjectIdentity
apSwInventoryConformance=_ApSwInventoryConformance_ObjectIdentity((1,3,6,1,4,1,9148,3,4,4))
_ApSwInventoryCompliances_ObjectIdentity=ObjectIdentity
apSwInventoryCompliances=_ApSwInventoryCompliances_ObjectIdentity((1,3,6,1,4,1,9148,3,4,4,1))
_ApSwInventoryGroups_ObjectIdentity=ObjectIdentity
apSwInventoryGroups=_ApSwInventoryGroups_ObjectIdentity((1,3,6,1,4,1,9148,3,4,4,2))
_ApSwInventoryNotificationsGroups_ObjectIdentity=ObjectIdentity
apSwInventoryNotificationsGroups=_ApSwInventoryNotificationsGroups_ObjectIdentity((1,3,6,1,4,1,9148,3,4,4,3))
apSwBootObjectsGroup=ObjectGroup((1,3,6,1,4,1,9148,3,4,4,2,1))
apSwBootObjectsGroup.setObjects(*((_B,_J),(_B,_K),(_B,_L)))
if mibBuilder.loadTexts:apSwBootObjectsGroup.setStatus(_A)
apSwCfgObjectsGroup=ObjectGroup((1,3,6,1,4,1,9148,3,4,4,2,2))
apSwCfgObjectsGroup.setObjects(*((_B,_M),(_B,_N),(_B,_O)))
if mibBuilder.loadTexts:apSwCfgObjectsGroup.setStatus(_A)
apSwCfgActivateNotification=NotificationType((1,3,6,1,4,1,9148,3,4,3,0,1))
apSwCfgActivateNotification.setObjects(*((_B,_P),(_B,_Q)))
if mibBuilder.loadTexts:apSwCfgActivateNotification.setStatus(_A)
apSwInventoryNotificationsGroup=NotificationGroup((1,3,6,1,4,1,9148,3,4,4,3,1))
apSwInventoryNotificationsGroup.setObjects((_B,_R))
if mibBuilder.loadTexts:apSwInventoryNotificationsGroup.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'apSwInventoryModule':apSwInventoryModule,'apSwInventoryMIBObjects':apSwInventoryMIBObjects,'apSwInventoryBootObjects':apSwInventoryBootObjects,'apSwBootTable':apSwBootTable,'apSwBootEntry':apSwBootEntry,_F:apSwBootIndex,_J:apSwBootDescr,_K:apSwBootType,_L:apSwBootStatus,'apSwInventoryCfgObjects':apSwInventoryCfgObjects,_M:apSwCfgCurrentVersion,_N:apSwCfgRunningVersion,'apSwCfgBackuptable':apSwCfgBackuptable,'apSwCfgBackupEntry':apSwCfgBackupEntry,_H:apSwCfgBackupIndex,_O:apSwCfgBackupName,'apSwInventoryNotificationObjects':apSwInventoryNotificationObjects,'apSwCfgNotificationObjects':apSwCfgNotificationObjects,_P:apSwCfgTrapPreviousVersion,_Q:apSwCfgTrapCurrentVersion,'apSwInventoryNotificationPrefix':apSwInventoryNotificationPrefix,'apSwInventoryNotifications':apSwInventoryNotifications,_R:apSwCfgActivateNotification,'apSwInventoryConformance':apSwInventoryConformance,'apSwInventoryCompliances':apSwInventoryCompliances,'apSwInventoryGroups':apSwInventoryGroups,'apSwBootObjectsGroup':apSwBootObjectsGroup,'apSwCfgObjectsGroup':apSwCfgObjectsGroup,'apSwInventoryNotificationsGroups':apSwInventoryNotificationsGroups,'apSwInventoryNotificationsGroup':apSwInventoryNotificationsGroup})