_T='licenseFeatureId'
_S='licenseId'
_R='SnmpAdminString'
_Q='fileSystemPath'
_P='fileSystemObjType'
_O='fileSystemObjName'
_N='licenseFeatureName'
_M='Integer32'
_L='sysName'
_K='SNMPv2-MIB'
_J='alarmEventReason'
_I='alarmEventLogSourceName'
_H='alarmEventLogSeverity'
_G='alarmEventLogDescription'
_F='alarmEventLogDateAndTime'
_E='alarmEventLogAlarmOrEventId'
_D='RAD-License-MIB'
_C='read-only'
_B='current'
_A='RAD-GEN-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
alarmEventLogAlarmOrEventId,alarmEventLogDateAndTime,alarmEventLogDescription,alarmEventLogSeverity,alarmEventLogSourceName,alarmEventReason,fileSystemObjName,fileSystemObjType,fileSystemPath=mibBuilder.importSymbols(_A,_E,_F,_G,_H,_I,_J,_O,_P,_Q)
agnt,=mibBuilder.importSymbols('RAD-SMI-MIB','agnt')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_R)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
sysName,=mibBuilder.importSymbols(_K,_L)
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_M,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','TextualConvention')
agnLicense=ModuleIdentity((1,3,6,1,4,1,164,6,2,73))
_LicenseNotifications_ObjectIdentity=ObjectIdentity
licenseNotifications=_LicenseNotifications_ObjectIdentity((1,3,6,1,4,1,164,6,2,73,0))
_LicenseConfig_ObjectIdentity=ObjectIdentity
licenseConfig=_LicenseConfig_ObjectIdentity((1,3,6,1,4,1,164,6,2,73,1))
_LicenseTable_Object=MibTable
licenseTable=_LicenseTable_Object((1,3,6,1,4,1,164,6,2,73,1,1))
if mibBuilder.loadTexts:licenseTable.setStatus(_B)
_LicenseEntry_Object=MibTableRow
licenseEntry=_LicenseEntry_Object((1,3,6,1,4,1,164,6,2,73,1,1,1))
licenseEntry.setIndexNames((0,_A,_Q),(0,_A,_P),(1,_A,_O))
if mibBuilder.loadTexts:licenseEntry.setStatus(_B)
_LicenseId_Type=Unsigned32
_LicenseId_Object=MibTableColumn
licenseId=_LicenseId_Object((1,3,6,1,4,1,164,6,2,73,1,1,1,1),_LicenseId_Type())
licenseId.setMaxAccess(_C)
if mibBuilder.loadTexts:licenseId.setStatus(_B)
_LicenseFeatureTable_Object=MibTable
licenseFeatureTable=_LicenseFeatureTable_Object((1,3,6,1,4,1,164,6,2,73,1,2))
if mibBuilder.loadTexts:licenseFeatureTable.setStatus(_B)
_LicenseFeatureEntry_Object=MibTableRow
licenseFeatureEntry=_LicenseFeatureEntry_Object((1,3,6,1,4,1,164,6,2,73,1,2,1))
licenseFeatureEntry.setIndexNames((0,_D,_S),(0,_D,_T))
if mibBuilder.loadTexts:licenseFeatureEntry.setStatus(_B)
_LicenseFeatureId_Type=Unsigned32
_LicenseFeatureId_Object=MibTableColumn
licenseFeatureId=_LicenseFeatureId_Object((1,3,6,1,4,1,164,6,2,73,1,2,1,1),_LicenseFeatureId_Type())
licenseFeatureId.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:licenseFeatureId.setStatus(_B)
class _LicenseFeatureName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_LicenseFeatureName_Type.__name__=_R
_LicenseFeatureName_Object=MibTableColumn
licenseFeatureName=_LicenseFeatureName_Object((1,3,6,1,4,1,164,6,2,73,1,2,1,2),_LicenseFeatureName_Type())
licenseFeatureName.setMaxAccess(_C)
if mibBuilder.loadTexts:licenseFeatureName.setStatus(_B)
class _LicenseFeatureStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('inactive',1),('perpetual',2),('perpeutalAll',3),('temporary',4),('temporaryAll',5),('expired',6)))
_LicenseFeatureStatus_Type.__name__=_M
_LicenseFeatureStatus_Object=MibTableColumn
licenseFeatureStatus=_LicenseFeatureStatus_Object((1,3,6,1,4,1,164,6,2,73,1,2,1,3),_LicenseFeatureStatus_Type())
licenseFeatureStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:licenseFeatureStatus.setStatus(_B)
_LicenseFeatureMaxAvailableQuantity_Type=Unsigned32
_LicenseFeatureMaxAvailableQuantity_Object=MibTableColumn
licenseFeatureMaxAvailableQuantity=_LicenseFeatureMaxAvailableQuantity_Object((1,3,6,1,4,1,164,6,2,73,1,2,1,4),_LicenseFeatureMaxAvailableQuantity_Type())
licenseFeatureMaxAvailableQuantity.setMaxAccess(_C)
if mibBuilder.loadTexts:licenseFeatureMaxAvailableQuantity.setStatus(_B)
_LicenseFeatureAllowedQuantity_Type=Unsigned32
_LicenseFeatureAllowedQuantity_Object=MibTableColumn
licenseFeatureAllowedQuantity=_LicenseFeatureAllowedQuantity_Object((1,3,6,1,4,1,164,6,2,73,1,2,1,5),_LicenseFeatureAllowedQuantity_Type())
licenseFeatureAllowedQuantity.setMaxAccess(_C)
if mibBuilder.loadTexts:licenseFeatureAllowedQuantity.setStatus(_B)
_LicenseFeatureQuantityInUse_Type=Unsigned32
_LicenseFeatureQuantityInUse_Object=MibTableColumn
licenseFeatureQuantityInUse=_LicenseFeatureQuantityInUse_Object((1,3,6,1,4,1,164,6,2,73,1,2,1,6),_LicenseFeatureQuantityInUse_Type())
licenseFeatureQuantityInUse.setMaxAccess(_C)
if mibBuilder.loadTexts:licenseFeatureQuantityInUse.setStatus(_B)
_LicenseFeatureExpiration_Type=Unsigned32
_LicenseFeatureExpiration_Object=MibTableColumn
licenseFeatureExpiration=_LicenseFeatureExpiration_Object((1,3,6,1,4,1,164,6,2,73,1,2,1,7),_LicenseFeatureExpiration_Type())
licenseFeatureExpiration.setMaxAccess(_C)
if mibBuilder.loadTexts:licenseFeatureExpiration.setStatus(_B)
class _LicenseFeatureActivationCmd_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('activate',1),('deactivate',2)))
_LicenseFeatureActivationCmd_Type.__name__=_M
_LicenseFeatureActivationCmd_Object=MibTableColumn
licenseFeatureActivationCmd=_LicenseFeatureActivationCmd_Object((1,3,6,1,4,1,164,6,2,73,1,2,1,8),_LicenseFeatureActivationCmd_Type())
licenseFeatureActivationCmd.setMaxAccess('read-write')
if mibBuilder.loadTexts:licenseFeatureActivationCmd.setStatus(_B)
systemLicenseEnabled=NotificationType((1,3,6,1,4,1,164,6,2,73,0,8))
systemLicenseEnabled.setObjects(*((_A,_I),(_A,_E),(_A,_G),(_A,_H),(_A,_F),(_A,_J),(_K,_L),(_D,_N)))
if mibBuilder.loadTexts:systemLicenseEnabled.setStatus(_B)
systemLicenseDisabled=NotificationType((1,3,6,1,4,1,164,6,2,73,0,9))
systemLicenseDisabled.setObjects(*((_A,_I),(_A,_E),(_A,_G),(_A,_H),(_A,_F),(_A,_J),(_K,_L),(_D,_N)))
if mibBuilder.loadTexts:systemLicenseDisabled.setStatus(_B)
mibBuilder.exportSymbols(_D,**{'agnLicense':agnLicense,'licenseNotifications':licenseNotifications,'systemLicenseEnabled':systemLicenseEnabled,'systemLicenseDisabled':systemLicenseDisabled,'licenseConfig':licenseConfig,'licenseTable':licenseTable,'licenseEntry':licenseEntry,_S:licenseId,'licenseFeatureTable':licenseFeatureTable,'licenseFeatureEntry':licenseFeatureEntry,_T:licenseFeatureId,_N:licenseFeatureName,'licenseFeatureStatus':licenseFeatureStatus,'licenseFeatureMaxAvailableQuantity':licenseFeatureMaxAvailableQuantity,'licenseFeatureAllowedQuantity':licenseFeatureAllowedQuantity,'licenseFeatureQuantityInUse':licenseFeatureQuantityInUse,'licenseFeatureExpiration':licenseFeatureExpiration,'licenseFeatureActivationCmd':licenseFeatureActivationCmd})