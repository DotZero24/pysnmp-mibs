_F='zyServiceRegisterServiceExpiration'
_E='read-only'
_D='Integer32'
_C='zyServiceRegisterServiceName'
_B='ZYXEL-SERVICE-REGISTER-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
esMgmt,=mibBuilder.importSymbols('ZYXEL-ES-SMI','esMgmt')
zyxelServiceRegister=ModuleIdentity((1,3,6,1,4,1,890,1,15,3,118))
_ZyxelServiceRegisterSetup_ObjectIdentity=ObjectIdentity
zyxelServiceRegisterSetup=_ZyxelServiceRegisterSetup_ObjectIdentity((1,3,6,1,4,1,890,1,15,3,118,1))
_ZyxelServiceRegisterStatus_ObjectIdentity=ObjectIdentity
zyxelServiceRegisterStatus=_ZyxelServiceRegisterStatus_ObjectIdentity((1,3,6,1,4,1,890,1,15,3,118,2))
_ZyxelServiceRegisterServiceTable_Object=MibTable
zyxelServiceRegisterServiceTable=_ZyxelServiceRegisterServiceTable_Object((1,3,6,1,4,1,890,1,15,3,118,2,1))
if mibBuilder.loadTexts:zyxelServiceRegisterServiceTable.setStatus(_A)
_ZyxelServiceRegisterServiceEntry_Object=MibTableRow
zyxelServiceRegisterServiceEntry=_ZyxelServiceRegisterServiceEntry_Object((1,3,6,1,4,1,890,1,15,3,118,2,1,1))
zyxelServiceRegisterServiceEntry.setIndexNames((0,_B,_C))
if mibBuilder.loadTexts:zyxelServiceRegisterServiceEntry.setStatus(_A)
_ZyServiceRegisterServiceName_Type=OctetString
_ZyServiceRegisterServiceName_Object=MibTableColumn
zyServiceRegisterServiceName=_ZyServiceRegisterServiceName_Object((1,3,6,1,4,1,890,1,15,3,118,2,1,1,1),_ZyServiceRegisterServiceName_Type())
zyServiceRegisterServiceName.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:zyServiceRegisterServiceName.setStatus(_A)
class _ZyServiceRegisterServiceStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('notLicensed',0),('licensed',1)))
_ZyServiceRegisterServiceStatus_Type.__name__=_D
_ZyServiceRegisterServiceStatus_Object=MibTableColumn
zyServiceRegisterServiceStatus=_ZyServiceRegisterServiceStatus_Object((1,3,6,1,4,1,890,1,15,3,118,2,1,1,2),_ZyServiceRegisterServiceStatus_Type())
zyServiceRegisterServiceStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:zyServiceRegisterServiceStatus.setStatus(_A)
class _ZyServiceRegisterServiceType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('none',0),('trial',1),('standard',2)))
_ZyServiceRegisterServiceType_Type.__name__=_D
_ZyServiceRegisterServiceType_Object=MibTableColumn
zyServiceRegisterServiceType=_ZyServiceRegisterServiceType_Object((1,3,6,1,4,1,890,1,15,3,118,2,1,1,3),_ZyServiceRegisterServiceType_Type())
zyServiceRegisterServiceType.setMaxAccess(_E)
if mibBuilder.loadTexts:zyServiceRegisterServiceType.setStatus(_A)
_ZyServiceRegisterServiceExpiration_Type=Integer32
_ZyServiceRegisterServiceExpiration_Object=MibTableColumn
zyServiceRegisterServiceExpiration=_ZyServiceRegisterServiceExpiration_Object((1,3,6,1,4,1,890,1,15,3,118,2,1,1,4),_ZyServiceRegisterServiceExpiration_Type())
zyServiceRegisterServiceExpiration.setMaxAccess(_E)
if mibBuilder.loadTexts:zyServiceRegisterServiceExpiration.setStatus(_A)
_ZyxelServiceRegisterTrapInfoObjects_ObjectIdentity=ObjectIdentity
zyxelServiceRegisterTrapInfoObjects=_ZyxelServiceRegisterTrapInfoObjects_ObjectIdentity((1,3,6,1,4,1,890,1,15,3,118,3))
_ZyxelServiceRegisterNotifications_ObjectIdentity=ObjectIdentity
zyxelServiceRegisterNotifications=_ZyxelServiceRegisterNotifications_ObjectIdentity((1,3,6,1,4,1,890,1,15,3,118,4))
zyServiceRegisterTheServiceHasExpired=NotificationType((1,3,6,1,4,1,890,1,15,3,118,4,1))
zyServiceRegisterTheServiceHasExpired.setObjects((_B,_C))
if mibBuilder.loadTexts:zyServiceRegisterTheServiceHasExpired.setStatus(_A)
zyServiceRegisterTheServiceIsDueToExpireInSomeHours=NotificationType((1,3,6,1,4,1,890,1,15,3,118,4,2))
zyServiceRegisterTheServiceIsDueToExpireInSomeHours.setObjects(*((_B,_C),(_B,_F)))
if mibBuilder.loadTexts:zyServiceRegisterTheServiceIsDueToExpireInSomeHours.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'zyxelServiceRegister':zyxelServiceRegister,'zyxelServiceRegisterSetup':zyxelServiceRegisterSetup,'zyxelServiceRegisterStatus':zyxelServiceRegisterStatus,'zyxelServiceRegisterServiceTable':zyxelServiceRegisterServiceTable,'zyxelServiceRegisterServiceEntry':zyxelServiceRegisterServiceEntry,_C:zyServiceRegisterServiceName,'zyServiceRegisterServiceStatus':zyServiceRegisterServiceStatus,'zyServiceRegisterServiceType':zyServiceRegisterServiceType,_F:zyServiceRegisterServiceExpiration,'zyxelServiceRegisterTrapInfoObjects':zyxelServiceRegisterTrapInfoObjects,'zyxelServiceRegisterNotifications':zyxelServiceRegisterNotifications,'zyServiceRegisterTheServiceHasExpired':zyServiceRegisterTheServiceHasExpired,'zyServiceRegisterTheServiceIsDueToExpireInSomeHours':zyServiceRegisterTheServiceIsDueToExpireInSomeHours})