_Z='hpicfSvcsV1AppGroup'
_Y='hpicfSvcsV1AppRowStatus'
_X='hpicfSvcsV1AppURL'
_W='hpicfSvcsV1AppJNumber'
_V='hpicfSvcsV1AppStatus'
_U='hpicfSvcsV1AppVersion'
_T='hpicfSvcsV1AppDescription'
_S='hpicfSvcsV1AppName'
_R='hpicfSvcsV1AppCLIAvailable'
_Q='hpicfSvcsV1AppIndex'
_P='hpicfSvcsInstalledAppRowStatus'
_O='hpicfSvcsInstalledAppLicensingStatus'
_N='hpicfSvcsInstalledAppJNumber'
_M='hpicfSvcsInstalledAppStatus'
_L='hpicfSvcsInstalledAppVersion'
_K='hpicfSvcsInstalledAppDescription'
_J='hpicfSvcsInstalledAppPlatformType'
_I='unknown'
_H='hpicfSvcsInstalledAppGroup'
_G='Integer32'
_F='entPhysicalIndex'
_E='ENTITY-MIB'
_D='SnmpAdminString'
_C='read-create'
_B='HP-ICF-SVCS-APP-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
entPhysicalIndex,=mibBuilder.importSymbols(_E,_F)
hpSwitch,=mibBuilder.importSymbols('HP-ICF-OID','hpSwitch')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
PortList,=mibBuilder.importSymbols('Q-BRIDGE-MIB','PortList')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_D)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_G,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
AutonomousType,DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','AutonomousType','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention','TruthValue')
hpicfSvcsAppMIB=ModuleIdentity((1,3,6,1,4,1,11,2,14,11,5,1,86))
if mibBuilder.loadTexts:hpicfSvcsAppMIB.setRevisions(('2011-05-27 00:00',))
class AppStatus(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12)));namedValues=NamedValues(*(('other',1),(_I,2),('bootInit',3),('booting',4),('bootFailure',5),('halted',6),('rebooting',7),('ready',8),('appInit',9),('appError',10),('appRunning',11),('shuttingDown',12)))
_HpicfSvcsAppNotifications_ObjectIdentity=ObjectIdentity
hpicfSvcsAppNotifications=_HpicfSvcsAppNotifications_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,86,0))
_HpicfSvcsAppObjects_ObjectIdentity=ObjectIdentity
hpicfSvcsAppObjects=_HpicfSvcsAppObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,86,1))
_HpicfSvcsInstalledAppTable_Object=MibTable
hpicfSvcsInstalledAppTable=_HpicfSvcsInstalledAppTable_Object((1,3,6,1,4,1,11,2,14,11,5,1,86,1,1))
if mibBuilder.loadTexts:hpicfSvcsInstalledAppTable.setStatus(_A)
_HpicfSvcsInstalledAppEntry_Object=MibTableRow
hpicfSvcsInstalledAppEntry=_HpicfSvcsInstalledAppEntry_Object((1,3,6,1,4,1,11,2,14,11,5,1,86,1,1,1))
hpicfSvcsInstalledAppEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:hpicfSvcsInstalledAppEntry.setStatus(_A)
_HpicfSvcsInstalledAppPlatformType_Type=AutonomousType
_HpicfSvcsInstalledAppPlatformType_Object=MibTableColumn
hpicfSvcsInstalledAppPlatformType=_HpicfSvcsInstalledAppPlatformType_Object((1,3,6,1,4,1,11,2,14,11,5,1,86,1,1,1,1),_HpicfSvcsInstalledAppPlatformType_Type())
hpicfSvcsInstalledAppPlatformType.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfSvcsInstalledAppPlatformType.setStatus(_A)
class _HpicfSvcsInstalledAppDescription_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_HpicfSvcsInstalledAppDescription_Type.__name__=_D
_HpicfSvcsInstalledAppDescription_Object=MibTableColumn
hpicfSvcsInstalledAppDescription=_HpicfSvcsInstalledAppDescription_Object((1,3,6,1,4,1,11,2,14,11,5,1,86,1,1,1,2),_HpicfSvcsInstalledAppDescription_Type())
hpicfSvcsInstalledAppDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfSvcsInstalledAppDescription.setStatus(_A)
class _HpicfSvcsInstalledAppVersion_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_HpicfSvcsInstalledAppVersion_Type.__name__=_D
_HpicfSvcsInstalledAppVersion_Object=MibTableColumn
hpicfSvcsInstalledAppVersion=_HpicfSvcsInstalledAppVersion_Object((1,3,6,1,4,1,11,2,14,11,5,1,86,1,1,1,3),_HpicfSvcsInstalledAppVersion_Type())
hpicfSvcsInstalledAppVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfSvcsInstalledAppVersion.setStatus(_A)
_HpicfSvcsInstalledAppStatus_Type=AppStatus
_HpicfSvcsInstalledAppStatus_Object=MibTableColumn
hpicfSvcsInstalledAppStatus=_HpicfSvcsInstalledAppStatus_Object((1,3,6,1,4,1,11,2,14,11,5,1,86,1,1,1,4),_HpicfSvcsInstalledAppStatus_Type())
hpicfSvcsInstalledAppStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfSvcsInstalledAppStatus.setStatus(_A)
class _HpicfSvcsInstalledAppJNumber_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_HpicfSvcsInstalledAppJNumber_Type.__name__=_D
_HpicfSvcsInstalledAppJNumber_Object=MibTableColumn
hpicfSvcsInstalledAppJNumber=_HpicfSvcsInstalledAppJNumber_Object((1,3,6,1,4,1,11,2,14,11,5,1,86,1,1,1,5),_HpicfSvcsInstalledAppJNumber_Type())
hpicfSvcsInstalledAppJNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfSvcsInstalledAppJNumber.setStatus(_A)
class _HpicfSvcsInstalledAppLicensingStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('active',1),('expired',2),(_I,3)))
_HpicfSvcsInstalledAppLicensingStatus_Type.__name__=_G
_HpicfSvcsInstalledAppLicensingStatus_Object=MibTableColumn
hpicfSvcsInstalledAppLicensingStatus=_HpicfSvcsInstalledAppLicensingStatus_Object((1,3,6,1,4,1,11,2,14,11,5,1,86,1,1,1,6),_HpicfSvcsInstalledAppLicensingStatus_Type())
hpicfSvcsInstalledAppLicensingStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfSvcsInstalledAppLicensingStatus.setStatus(_A)
_HpicfSvcsInstalledAppRowStatus_Type=RowStatus
_HpicfSvcsInstalledAppRowStatus_Object=MibTableColumn
hpicfSvcsInstalledAppRowStatus=_HpicfSvcsInstalledAppRowStatus_Object((1,3,6,1,4,1,11,2,14,11,5,1,86,1,1,1,7),_HpicfSvcsInstalledAppRowStatus_Type())
hpicfSvcsInstalledAppRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfSvcsInstalledAppRowStatus.setStatus(_A)
_HpicfSvcsV1AppTable_Object=MibTable
hpicfSvcsV1AppTable=_HpicfSvcsV1AppTable_Object((1,3,6,1,4,1,11,2,14,11,5,1,86,1,2))
if mibBuilder.loadTexts:hpicfSvcsV1AppTable.setStatus(_A)
_HpicfSvcsV1AppEntry_Object=MibTableRow
hpicfSvcsV1AppEntry=_HpicfSvcsV1AppEntry_Object((1,3,6,1,4,1,11,2,14,11,5,1,86,1,2,1))
hpicfSvcsV1AppEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:hpicfSvcsV1AppEntry.setStatus(_A)
class _HpicfSvcsV1AppIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_HpicfSvcsV1AppIndex_Type.__name__=_G
_HpicfSvcsV1AppIndex_Object=MibTableColumn
hpicfSvcsV1AppIndex=_HpicfSvcsV1AppIndex_Object((1,3,6,1,4,1,11,2,14,11,5,1,86,1,2,1,1),_HpicfSvcsV1AppIndex_Type())
hpicfSvcsV1AppIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfSvcsV1AppIndex.setStatus(_A)
_HpicfSvcsV1AppCLIAvailable_Type=TruthValue
_HpicfSvcsV1AppCLIAvailable_Object=MibTableColumn
hpicfSvcsV1AppCLIAvailable=_HpicfSvcsV1AppCLIAvailable_Object((1,3,6,1,4,1,11,2,14,11,5,1,86,1,2,1,2),_HpicfSvcsV1AppCLIAvailable_Type())
hpicfSvcsV1AppCLIAvailable.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfSvcsV1AppCLIAvailable.setStatus(_A)
class _HpicfSvcsV1AppName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_HpicfSvcsV1AppName_Type.__name__=_D
_HpicfSvcsV1AppName_Object=MibTableColumn
hpicfSvcsV1AppName=_HpicfSvcsV1AppName_Object((1,3,6,1,4,1,11,2,14,11,5,1,86,1,2,1,3),_HpicfSvcsV1AppName_Type())
hpicfSvcsV1AppName.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfSvcsV1AppName.setStatus(_A)
class _HpicfSvcsV1AppDescription_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_HpicfSvcsV1AppDescription_Type.__name__=_D
_HpicfSvcsV1AppDescription_Object=MibTableColumn
hpicfSvcsV1AppDescription=_HpicfSvcsV1AppDescription_Object((1,3,6,1,4,1,11,2,14,11,5,1,86,1,2,1,4),_HpicfSvcsV1AppDescription_Type())
hpicfSvcsV1AppDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfSvcsV1AppDescription.setStatus(_A)
class _HpicfSvcsV1AppVersion_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_HpicfSvcsV1AppVersion_Type.__name__=_D
_HpicfSvcsV1AppVersion_Object=MibTableColumn
hpicfSvcsV1AppVersion=_HpicfSvcsV1AppVersion_Object((1,3,6,1,4,1,11,2,14,11,5,1,86,1,2,1,5),_HpicfSvcsV1AppVersion_Type())
hpicfSvcsV1AppVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfSvcsV1AppVersion.setStatus(_A)
_HpicfSvcsV1AppStatus_Type=AppStatus
_HpicfSvcsV1AppStatus_Object=MibTableColumn
hpicfSvcsV1AppStatus=_HpicfSvcsV1AppStatus_Object((1,3,6,1,4,1,11,2,14,11,5,1,86,1,2,1,6),_HpicfSvcsV1AppStatus_Type())
hpicfSvcsV1AppStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfSvcsV1AppStatus.setStatus(_A)
class _HpicfSvcsV1AppJNumber_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_HpicfSvcsV1AppJNumber_Type.__name__=_D
_HpicfSvcsV1AppJNumber_Object=MibTableColumn
hpicfSvcsV1AppJNumber=_HpicfSvcsV1AppJNumber_Object((1,3,6,1,4,1,11,2,14,11,5,1,86,1,2,1,7),_HpicfSvcsV1AppJNumber_Type())
hpicfSvcsV1AppJNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfSvcsV1AppJNumber.setStatus(_A)
class _HpicfSvcsV1AppURL_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_HpicfSvcsV1AppURL_Type.__name__=_D
_HpicfSvcsV1AppURL_Object=MibTableColumn
hpicfSvcsV1AppURL=_HpicfSvcsV1AppURL_Object((1,3,6,1,4,1,11,2,14,11,5,1,86,1,2,1,8),_HpicfSvcsV1AppURL_Type())
hpicfSvcsV1AppURL.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfSvcsV1AppURL.setStatus(_A)
_HpicfSvcsV1AppRowStatus_Type=RowStatus
_HpicfSvcsV1AppRowStatus_Object=MibTableColumn
hpicfSvcsV1AppRowStatus=_HpicfSvcsV1AppRowStatus_Object((1,3,6,1,4,1,11,2,14,11,5,1,86,1,2,1,9),_HpicfSvcsV1AppRowStatus_Type())
hpicfSvcsV1AppRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfSvcsV1AppRowStatus.setStatus(_A)
_HpicfSvcsAppConformance_ObjectIdentity=ObjectIdentity
hpicfSvcsAppConformance=_HpicfSvcsAppConformance_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,86,2))
_HpicfSvcsAppCompliances_ObjectIdentity=ObjectIdentity
hpicfSvcsAppCompliances=_HpicfSvcsAppCompliances_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,86,2,1))
_HpicfSvcsAppGroups_ObjectIdentity=ObjectIdentity
hpicfSvcsAppGroups=_HpicfSvcsAppGroups_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,86,2,2))
hpicfSvcsInstalledAppGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,86,2,2,1))
hpicfSvcsInstalledAppGroup.setObjects(*((_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P)))
if mibBuilder.loadTexts:hpicfSvcsInstalledAppGroup.setStatus(_A)
hpicfSvcsV1AppGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,86,2,2,2))
hpicfSvcsV1AppGroup.setObjects(*((_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y)))
if mibBuilder.loadTexts:hpicfSvcsV1AppGroup.setStatus(_A)
hpicfSvcsAppCompliance=ModuleCompliance((1,3,6,1,4,1,11,2,14,11,5,1,86,2,1,1))
hpicfSvcsAppCompliance.setObjects(*((_B,_H),(_B,_Z),(_B,_H)))
if mibBuilder.loadTexts:hpicfSvcsAppCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'AppStatus':AppStatus,'hpicfSvcsAppMIB':hpicfSvcsAppMIB,'hpicfSvcsAppNotifications':hpicfSvcsAppNotifications,'hpicfSvcsAppObjects':hpicfSvcsAppObjects,'hpicfSvcsInstalledAppTable':hpicfSvcsInstalledAppTable,'hpicfSvcsInstalledAppEntry':hpicfSvcsInstalledAppEntry,_J:hpicfSvcsInstalledAppPlatformType,_K:hpicfSvcsInstalledAppDescription,_L:hpicfSvcsInstalledAppVersion,_M:hpicfSvcsInstalledAppStatus,_N:hpicfSvcsInstalledAppJNumber,_O:hpicfSvcsInstalledAppLicensingStatus,_P:hpicfSvcsInstalledAppRowStatus,'hpicfSvcsV1AppTable':hpicfSvcsV1AppTable,'hpicfSvcsV1AppEntry':hpicfSvcsV1AppEntry,_Q:hpicfSvcsV1AppIndex,_R:hpicfSvcsV1AppCLIAvailable,_S:hpicfSvcsV1AppName,_T:hpicfSvcsV1AppDescription,_U:hpicfSvcsV1AppVersion,_V:hpicfSvcsV1AppStatus,_W:hpicfSvcsV1AppJNumber,_X:hpicfSvcsV1AppURL,_Y:hpicfSvcsV1AppRowStatus,'hpicfSvcsAppConformance':hpicfSvcsAppConformance,'hpicfSvcsAppCompliances':hpicfSvcsAppCompliances,'hpicfSvcsAppCompliance':hpicfSvcsAppCompliance,'hpicfSvcsAppGroups':hpicfSvcsAppGroups,_H:hpicfSvcsInstalledAppGroup,_Z:hpicfSvcsV1AppGroup})