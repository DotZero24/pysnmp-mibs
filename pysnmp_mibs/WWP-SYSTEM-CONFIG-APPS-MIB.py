_I='wwpSystemAppsName'
_H='wwpSystemConfIndex'
_G='wwpSystemAppsImage'
_F='TruthValue'
_E='Integer32'
_D='WWP-SYSTEM-CONFIG-APPS-MIB'
_C='read-write'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention',_F)
wwpModules,=mibBuilder.importSymbols('WWP-SMI','wwpModules')
wwpSystemConfAppsMIB=ModuleIdentity((1,3,6,1,4,1,6141,2,20))
if mibBuilder.loadTexts:wwpSystemConfAppsMIB.setRevisions(('2001-04-03 17:00',))
_WwpSystemConfAppsMIBObjects_ObjectIdentity=ObjectIdentity
wwpSystemConfAppsMIBObjects=_WwpSystemConfAppsMIBObjects_ObjectIdentity((1,3,6,1,4,1,6141,2,20,1))
_WwpSystemApps_ObjectIdentity=ObjectIdentity
wwpSystemApps=_WwpSystemApps_ObjectIdentity((1,3,6,1,4,1,6141,2,20,1,1))
_WwpSystemRunningApps_Type=DisplayString
_WwpSystemRunningApps_Object=MibScalar
wwpSystemRunningApps=_WwpSystemRunningApps_Object((1,3,6,1,4,1,6141,2,20,1,1,1),_WwpSystemRunningApps_Type())
wwpSystemRunningApps.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpSystemRunningApps.setStatus(_A)
class _WwpSystemAppsSwapActivate_Type(TruthValue):defaultValue=2
_WwpSystemAppsSwapActivate_Type.__name__=_F
_WwpSystemAppsSwapActivate_Object=MibScalar
wwpSystemAppsSwapActivate=_WwpSystemAppsSwapActivate_Object((1,3,6,1,4,1,6141,2,20,1,1,2),_WwpSystemAppsSwapActivate_Type())
wwpSystemAppsSwapActivate.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpSystemAppsSwapActivate.setStatus(_A)
_WwpSystemAppsTable_Object=MibTable
wwpSystemAppsTable=_WwpSystemAppsTable_Object((1,3,6,1,4,1,6141,2,20,1,1,3))
if mibBuilder.loadTexts:wwpSystemAppsTable.setStatus(_A)
_WwpSystemAppsEntry_Object=MibTableRow
wwpSystemAppsEntry=_WwpSystemAppsEntry_Object((1,3,6,1,4,1,6141,2,20,1,1,3,1))
wwpSystemAppsEntry.setIndexNames((0,_D,_G))
if mibBuilder.loadTexts:wwpSystemAppsEntry.setStatus(_A)
class _WwpSystemAppsImage_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('primary',1),('backup',2)))
_WwpSystemAppsImage_Type.__name__=_E
_WwpSystemAppsImage_Object=MibTableColumn
wwpSystemAppsImage=_WwpSystemAppsImage_Object((1,3,6,1,4,1,6141,2,20,1,1,3,1,1),_WwpSystemAppsImage_Type())
wwpSystemAppsImage.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpSystemAppsImage.setStatus(_A)
_WwpSystemAppsName_Type=DisplayString
_WwpSystemAppsName_Object=MibTableColumn
wwpSystemAppsName=_WwpSystemAppsName_Object((1,3,6,1,4,1,6141,2,20,1,1,3,1,2),_WwpSystemAppsName_Type())
wwpSystemAppsName.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpSystemAppsName.setStatus(_A)
class _WwpSystemBackupNotifEnabled_Type(TruthValue):defaultValue=1
_WwpSystemBackupNotifEnabled_Type.__name__=_F
_WwpSystemBackupNotifEnabled_Object=MibScalar
wwpSystemBackupNotifEnabled=_WwpSystemBackupNotifEnabled_Object((1,3,6,1,4,1,6141,2,20,1,1,4),_WwpSystemBackupNotifEnabled_Type())
wwpSystemBackupNotifEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpSystemBackupNotifEnabled.setStatus(_A)
_WwpSystemConf_ObjectIdentity=ObjectIdentity
wwpSystemConf=_WwpSystemConf_ObjectIdentity((1,3,6,1,4,1,6141,2,20,1,2))
_WwpSystemConfTable_Object=MibTable
wwpSystemConfTable=_WwpSystemConfTable_Object((1,3,6,1,4,1,6141,2,20,1,2,1))
if mibBuilder.loadTexts:wwpSystemConfTable.setStatus(_A)
_WwpSystemConfEntry_Object=MibTableRow
wwpSystemConfEntry=_WwpSystemConfEntry_Object((1,3,6,1,4,1,6141,2,20,1,2,1,1))
wwpSystemConfEntry.setIndexNames((0,_D,_H))
if mibBuilder.loadTexts:wwpSystemConfEntry.setStatus(_A)
class _WwpSystemConfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_WwpSystemConfIndex_Type.__name__=_E
_WwpSystemConfIndex_Object=MibTableColumn
wwpSystemConfIndex=_WwpSystemConfIndex_Object((1,3,6,1,4,1,6141,2,20,1,2,1,1,1),_WwpSystemConfIndex_Type())
wwpSystemConfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpSystemConfIndex.setStatus(_A)
_WwpSystemConfName_Type=DisplayString
_WwpSystemConfName_Object=MibTableColumn
wwpSystemConfName=_WwpSystemConfName_Object((1,3,6,1,4,1,6141,2,20,1,2,1,1,2),_WwpSystemConfName_Type())
wwpSystemConfName.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpSystemConfName.setStatus(_A)
_WwpSystemBootConfName_Type=DisplayString
_WwpSystemBootConfName_Object=MibScalar
wwpSystemBootConfName=_WwpSystemBootConfName_Object((1,3,6,1,4,1,6141,2,20,1,2,2),_WwpSystemBootConfName_Type())
wwpSystemBootConfName.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpSystemBootConfName.setStatus(_A)
_WwpSystemConfSaveName_Type=DisplayString
_WwpSystemConfSaveName_Object=MibScalar
wwpSystemConfSaveName=_WwpSystemConfSaveName_Object((1,3,6,1,4,1,6141,2,20,1,2,3),_WwpSystemConfSaveName_Type())
wwpSystemConfSaveName.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpSystemConfSaveName.setStatus(_A)
_WwpSystemConfAppsMIBNotificationPrefix_ObjectIdentity=ObjectIdentity
wwpSystemConfAppsMIBNotificationPrefix=_WwpSystemConfAppsMIBNotificationPrefix_ObjectIdentity((1,3,6,1,4,1,6141,2,20,2))
_WwpSystemConfAppsMIBNotifications_ObjectIdentity=ObjectIdentity
wwpSystemConfAppsMIBNotifications=_WwpSystemConfAppsMIBNotifications_ObjectIdentity((1,3,6,1,4,1,6141,2,20,2,0))
_WwpSystemConfAppsMIBConformance_ObjectIdentity=ObjectIdentity
wwpSystemConfAppsMIBConformance=_WwpSystemConfAppsMIBConformance_ObjectIdentity((1,3,6,1,4,1,6141,2,20,3))
_WwpSystemConfAppsMIBCompliances_ObjectIdentity=ObjectIdentity
wwpSystemConfAppsMIBCompliances=_WwpSystemConfAppsMIBCompliances_ObjectIdentity((1,3,6,1,4,1,6141,2,20,3,1))
_WwpSystemConfAppsMIBGroups_ObjectIdentity=ObjectIdentity
wwpSystemConfAppsMIBGroups=_WwpSystemConfAppsMIBGroups_ObjectIdentity((1,3,6,1,4,1,6141,2,20,3,2))
wwpSystemLoadBackupAppNotification=NotificationType((1,3,6,1,4,1,6141,2,20,2,0,1))
wwpSystemLoadBackupAppNotification.setObjects((_D,_I))
if mibBuilder.loadTexts:wwpSystemLoadBackupAppNotification.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'wwpSystemConfAppsMIB':wwpSystemConfAppsMIB,'wwpSystemConfAppsMIBObjects':wwpSystemConfAppsMIBObjects,'wwpSystemApps':wwpSystemApps,'wwpSystemRunningApps':wwpSystemRunningApps,'wwpSystemAppsSwapActivate':wwpSystemAppsSwapActivate,'wwpSystemAppsTable':wwpSystemAppsTable,'wwpSystemAppsEntry':wwpSystemAppsEntry,_G:wwpSystemAppsImage,_I:wwpSystemAppsName,'wwpSystemBackupNotifEnabled':wwpSystemBackupNotifEnabled,'wwpSystemConf':wwpSystemConf,'wwpSystemConfTable':wwpSystemConfTable,'wwpSystemConfEntry':wwpSystemConfEntry,_H:wwpSystemConfIndex,'wwpSystemConfName':wwpSystemConfName,'wwpSystemBootConfName':wwpSystemBootConfName,'wwpSystemConfSaveName':wwpSystemConfSaveName,'wwpSystemConfAppsMIBNotificationPrefix':wwpSystemConfAppsMIBNotificationPrefix,'wwpSystemConfAppsMIBNotifications':wwpSystemConfAppsMIBNotifications,'wwpSystemLoadBackupAppNotification':wwpSystemLoadBackupAppNotification,'wwpSystemConfAppsMIBConformance':wwpSystemConfAppsMIBConformance,'wwpSystemConfAppsMIBCompliances':wwpSystemConfAppsMIBCompliances,'wwpSystemConfAppsMIBGroups':wwpSystemConfAppsMIBGroups})