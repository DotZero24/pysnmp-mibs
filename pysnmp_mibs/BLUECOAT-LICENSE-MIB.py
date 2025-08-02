_N='appLicenseMIBGroup'
_M='appLicenseStateTrap'
_L='appLicenseStatusIndex'
_K='unknown'
_J='Integer32'
_I='appLicenseStatusLicenseState'
_H='appLicenseStatusExpireDate'
_G='appLicenseStatusExpireType'
_F='appLicenseStatusComponentName'
_E='appLicenseStatusFeatureName'
_D='appLicenseStatusApplicationName'
_C='read-only'
_B='current'
_A='BLUECOAT-LICENSE-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
blueCoatMgmt,=mibBuilder.importSymbols('BLUECOAT-MIB','blueCoatMgmt')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_J,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','TextualConvention')
appLicenseMIB=ModuleIdentity((1,3,6,1,4,1,3417,2,16))
if mibBuilder.loadTexts:appLicenseMIB.setRevisions(('2015-01-13 03:00',))
class LicenseState(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_K,0),('active',1),('expired',2)))
class LicenseExpireType(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_K,0),('perpetual',1),('subscription',2),('demo',3)))
_AppLicenseMIBObjects_ObjectIdentity=ObjectIdentity
appLicenseMIBObjects=_AppLicenseMIBObjects_ObjectIdentity((1,3,6,1,4,1,3417,2,16,1))
_AppLicense_ObjectIdentity=ObjectIdentity
appLicense=_AppLicense_ObjectIdentity((1,3,6,1,4,1,3417,2,16,1,1))
_AppLicenseStatusTable_Object=MibTable
appLicenseStatusTable=_AppLicenseStatusTable_Object((1,3,6,1,4,1,3417,2,16,1,1,1))
if mibBuilder.loadTexts:appLicenseStatusTable.setStatus(_B)
_AppLicenseStatusEntry_Object=MibTableRow
appLicenseStatusEntry=_AppLicenseStatusEntry_Object((1,3,6,1,4,1,3417,2,16,1,1,1,1))
appLicenseStatusEntry.setIndexNames((0,_A,_L))
if mibBuilder.loadTexts:appLicenseStatusEntry.setStatus(_B)
class _AppLicenseStatusIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_AppLicenseStatusIndex_Type.__name__=_J
_AppLicenseStatusIndex_Object=MibTableColumn
appLicenseStatusIndex=_AppLicenseStatusIndex_Object((1,3,6,1,4,1,3417,2,16,1,1,1,1,1),_AppLicenseStatusIndex_Type())
appLicenseStatusIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:appLicenseStatusIndex.setStatus(_B)
_AppLicenseStatusApplicationName_Type=DisplayString
_AppLicenseStatusApplicationName_Object=MibTableColumn
appLicenseStatusApplicationName=_AppLicenseStatusApplicationName_Object((1,3,6,1,4,1,3417,2,16,1,1,1,1,2),_AppLicenseStatusApplicationName_Type())
appLicenseStatusApplicationName.setMaxAccess(_C)
if mibBuilder.loadTexts:appLicenseStatusApplicationName.setStatus(_B)
_AppLicenseStatusFeatureName_Type=DisplayString
_AppLicenseStatusFeatureName_Object=MibTableColumn
appLicenseStatusFeatureName=_AppLicenseStatusFeatureName_Object((1,3,6,1,4,1,3417,2,16,1,1,1,1,3),_AppLicenseStatusFeatureName_Type())
appLicenseStatusFeatureName.setMaxAccess(_C)
if mibBuilder.loadTexts:appLicenseStatusFeatureName.setStatus(_B)
_AppLicenseStatusComponentName_Type=DisplayString
_AppLicenseStatusComponentName_Object=MibTableColumn
appLicenseStatusComponentName=_AppLicenseStatusComponentName_Object((1,3,6,1,4,1,3417,2,16,1,1,1,1,4),_AppLicenseStatusComponentName_Type())
appLicenseStatusComponentName.setMaxAccess(_C)
if mibBuilder.loadTexts:appLicenseStatusComponentName.setStatus(_B)
_AppLicenseStatusExpireType_Type=LicenseExpireType
_AppLicenseStatusExpireType_Object=MibTableColumn
appLicenseStatusExpireType=_AppLicenseStatusExpireType_Object((1,3,6,1,4,1,3417,2,16,1,1,1,1,5),_AppLicenseStatusExpireType_Type())
appLicenseStatusExpireType.setMaxAccess(_C)
if mibBuilder.loadTexts:appLicenseStatusExpireType.setStatus(_B)
_AppLicenseStatusExpireDate_Type=DateAndTime
_AppLicenseStatusExpireDate_Object=MibTableColumn
appLicenseStatusExpireDate=_AppLicenseStatusExpireDate_Object((1,3,6,1,4,1,3417,2,16,1,1,1,1,6),_AppLicenseStatusExpireDate_Type())
appLicenseStatusExpireDate.setMaxAccess(_C)
if mibBuilder.loadTexts:appLicenseStatusExpireDate.setStatus(_B)
_AppLicenseStatusLicenseState_Type=LicenseState
_AppLicenseStatusLicenseState_Object=MibTableColumn
appLicenseStatusLicenseState=_AppLicenseStatusLicenseState_Object((1,3,6,1,4,1,3417,2,16,1,1,1,1,7),_AppLicenseStatusLicenseState_Type())
appLicenseStatusLicenseState.setMaxAccess(_C)
if mibBuilder.loadTexts:appLicenseStatusLicenseState.setStatus(_B)
_AppLicenseMIBNotifications_ObjectIdentity=ObjectIdentity
appLicenseMIBNotifications=_AppLicenseMIBNotifications_ObjectIdentity((1,3,6,1,4,1,3417,2,16,2))
_AppLicenseMIBNotificationsPrefix_ObjectIdentity=ObjectIdentity
appLicenseMIBNotificationsPrefix=_AppLicenseMIBNotificationsPrefix_ObjectIdentity((1,3,6,1,4,1,3417,2,16,2,0))
_AppLicenseMIBConformance_ObjectIdentity=ObjectIdentity
appLicenseMIBConformance=_AppLicenseMIBConformance_ObjectIdentity((1,3,6,1,4,1,3417,2,16,3))
_AppLicenseMIBCompliances_ObjectIdentity=ObjectIdentity
appLicenseMIBCompliances=_AppLicenseMIBCompliances_ObjectIdentity((1,3,6,1,4,1,3417,2,16,3,1))
_AppLicenseMIBGroups_ObjectIdentity=ObjectIdentity
appLicenseMIBGroups=_AppLicenseMIBGroups_ObjectIdentity((1,3,6,1,4,1,3417,2,16,3,2))
_AppLicenseMIBNotifGroups_ObjectIdentity=ObjectIdentity
appLicenseMIBNotifGroups=_AppLicenseMIBNotifGroups_ObjectIdentity((1,3,6,1,4,1,3417,2,16,3,3))
appLicenseMIBGroup=ObjectGroup((1,3,6,1,4,1,3417,2,16,3,2,1))
appLicenseMIBGroup.setObjects(*((_A,_D),(_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I)))
if mibBuilder.loadTexts:appLicenseMIBGroup.setStatus(_B)
appLicenseStateTrap=NotificationType((1,3,6,1,4,1,3417,2,16,2,0,1))
appLicenseStateTrap.setObjects(*((_A,_D),(_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I)))
if mibBuilder.loadTexts:appLicenseStateTrap.setStatus(_B)
appLicenseMIBNotifGroup=NotificationGroup((1,3,6,1,4,1,3417,2,16,3,3,1))
appLicenseMIBNotifGroup.setObjects((_A,_M))
if mibBuilder.loadTexts:appLicenseMIBNotifGroup.setStatus(_B)
appLicenseMIBCompliance=ModuleCompliance((1,3,6,1,4,1,3417,2,16,3,1,1))
appLicenseMIBCompliance.setObjects((_A,_N))
if mibBuilder.loadTexts:appLicenseMIBCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'LicenseState':LicenseState,'LicenseExpireType':LicenseExpireType,'appLicenseMIB':appLicenseMIB,'appLicenseMIBObjects':appLicenseMIBObjects,'appLicense':appLicense,'appLicenseStatusTable':appLicenseStatusTable,'appLicenseStatusEntry':appLicenseStatusEntry,_L:appLicenseStatusIndex,_D:appLicenseStatusApplicationName,_E:appLicenseStatusFeatureName,_F:appLicenseStatusComponentName,_G:appLicenseStatusExpireType,_H:appLicenseStatusExpireDate,_I:appLicenseStatusLicenseState,'appLicenseMIBNotifications':appLicenseMIBNotifications,'appLicenseMIBNotificationsPrefix':appLicenseMIBNotificationsPrefix,_M:appLicenseStateTrap,'appLicenseMIBConformance':appLicenseMIBConformance,'appLicenseMIBCompliances':appLicenseMIBCompliances,'appLicenseMIBCompliance':appLicenseMIBCompliance,'appLicenseMIBGroups':appLicenseMIBGroups,_N:appLicenseMIBGroup,'appLicenseMIBNotifGroups':appLicenseMIBNotifGroups,'appLicenseMIBNotifGroup':appLicenseMIBNotifGroup})