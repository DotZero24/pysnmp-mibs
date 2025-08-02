_P='radiusServersPriority'
_O='radiusServersService'
_N='radius'
_M='servicesAaaTypeService'
_L='usersStatusUserName'
_K='observer'
_J='usersUserName'
_I='MxEnableState'
_H='MxIpHostNamePort'
_G='Unsigned32'
_F='MX-AAA-MIB'
_E='OctetString'
_D='read-only'
_C='Integer32'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_E,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
mediatrixServices,=mibBuilder.importSymbols('MX-SMI2','mediatrixServices')
MxActivationState,MxAdvancedIpPort,MxDigitMap,MxEnableState,MxIpAddress,MxIpHostName,MxIpPort,MxIpSubnetMask=mibBuilder.importSymbols('MX-TC','MxActivationState','MxAdvancedIpPort','MxDigitMap',_I,'MxIpAddress','MxIpHostName','MxIpPort','MxIpSubnetMask')
MxFloat32,MxIpAddr,MxIpAddrMask,MxIpAddrPort,MxIpHostNamePort,MxUInt64,MxUri,MxUrl=mibBuilder.importSymbols('MX-TC2','MxFloat32','MxIpAddr','MxIpAddrMask','MxIpAddrPort',_H,'MxUInt64','MxUri','MxUrl')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_G,'iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
aaaMIB=ModuleIdentity((1,3,6,1,4,1,4935,1000,100,200,100,1000))
_AaaMIBObjects_ObjectIdentity=ObjectIdentity
aaaMIBObjects=_AaaMIBObjects_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,1000,1))
_UsersTable_Object=MibTable
usersTable=_UsersTable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1000,1,100))
if mibBuilder.loadTexts:usersTable.setStatus(_A)
_UsersEntry_Object=MibTableRow
usersEntry=_UsersEntry_Object((1,3,6,1,4,1,4935,1000,100,200,100,1000,1,100,1))
usersEntry.setIndexNames((0,_F,_J))
if mibBuilder.loadTexts:usersEntry.setStatus(_A)
class _UsersUserName_Type(OctetString):defaultValue=OctetString('');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,50))
_UsersUserName_Type.__name__=_E
_UsersUserName_Object=MibTableColumn
usersUserName=_UsersUserName_Object((1,3,6,1,4,1,4935,1000,100,200,100,1000,1,100,1,100),_UsersUserName_Type())
usersUserName.setMaxAccess(_D)
if mibBuilder.loadTexts:usersUserName.setStatus(_A)
class _UsersPassword_Type(OctetString):defaultValue=OctetString('')
_UsersPassword_Type.__name__=_E
_UsersPassword_Object=MibTableColumn
usersPassword=_UsersPassword_Object((1,3,6,1,4,1,4935,1000,100,200,100,1000,1,100,1,200),_UsersPassword_Type())
usersPassword.setMaxAccess(_B)
if mibBuilder.loadTexts:usersPassword.setStatus(_A)
class _UsersAccessRights_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200,300)));namedValues=NamedValues(*(('admin',100),('user',200),(_K,300)))
_UsersAccessRights_Type.__name__=_C
_UsersAccessRights_Object=MibTableColumn
usersAccessRights=_UsersAccessRights_Object((1,3,6,1,4,1,4935,1000,100,200,100,1000,1,100,1,250),_UsersAccessRights_Type())
usersAccessRights.setMaxAccess(_B)
if mibBuilder.loadTexts:usersAccessRights.setStatus(_A)
class _UsersLockProtectionEnable_Type(MxEnableState):defaultValue=1
_UsersLockProtectionEnable_Type.__name__=_I
_UsersLockProtectionEnable_Object=MibTableColumn
usersLockProtectionEnable=_UsersLockProtectionEnable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1000,1,100,1,275),_UsersLockProtectionEnable_Type())
usersLockProtectionEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:usersLockProtectionEnable.setStatus(_A)
class _UsersDelete_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,10)));namedValues=NamedValues(*(('noOp',0),('delete',10)))
_UsersDelete_Type.__name__=_C
_UsersDelete_Object=MibTableColumn
usersDelete=_UsersDelete_Object((1,3,6,1,4,1,4935,1000,100,200,100,1000,1,100,1,300),_UsersDelete_Type())
usersDelete.setMaxAccess(_B)
if mibBuilder.loadTexts:usersDelete.setStatus(_A)
_UsersStatusTable_Object=MibTable
usersStatusTable=_UsersStatusTable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1000,1,150))
if mibBuilder.loadTexts:usersStatusTable.setStatus(_A)
_UsersStatusEntry_Object=MibTableRow
usersStatusEntry=_UsersStatusEntry_Object((1,3,6,1,4,1,4935,1000,100,200,100,1000,1,150,1))
usersStatusEntry.setIndexNames((0,_F,_L))
if mibBuilder.loadTexts:usersStatusEntry.setStatus(_A)
_UsersStatusUserName_Type=OctetString
_UsersStatusUserName_Object=MibTableColumn
usersStatusUserName=_UsersStatusUserName_Object((1,3,6,1,4,1,4935,1000,100,200,100,1000,1,150,1,100),_UsersStatusUserName_Type())
usersStatusUserName.setMaxAccess(_D)
if mibBuilder.loadTexts:usersStatusUserName.setStatus(_A)
_UsersStatusPassword_Type=OctetString
_UsersStatusPassword_Object=MibTableColumn
usersStatusPassword=_UsersStatusPassword_Object((1,3,6,1,4,1,4935,1000,100,200,100,1000,1,150,1,200),_UsersStatusPassword_Type())
usersStatusPassword.setMaxAccess(_D)
if mibBuilder.loadTexts:usersStatusPassword.setStatus(_A)
class _UsersStatusLocked_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200)));namedValues=NamedValues(*(('unlocked',100),('locked',200)))
_UsersStatusLocked_Type.__name__=_C
_UsersStatusLocked_Object=MibTableColumn
usersStatusLocked=_UsersStatusLocked_Object((1,3,6,1,4,1,4935,1000,100,200,100,1000,1,150,1,300),_UsersStatusLocked_Type())
usersStatusLocked.setMaxAccess(_D)
if mibBuilder.loadTexts:usersStatusLocked.setStatus(_A)
class _BatchUser_Type(OctetString):defaultValue=OctetString('')
_BatchUser_Type.__name__=_E
_BatchUser_Object=MibScalar
batchUser=_BatchUser_Object((1,3,6,1,4,1,4935,1000,100,200,100,1000,1,200),_BatchUser_Type())
batchUser.setMaxAccess(_B)
if mibBuilder.loadTexts:batchUser.setStatus(_A)
_ServicesAaaTypeTable_Object=MibTable
servicesAaaTypeTable=_ServicesAaaTypeTable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1000,1,300))
if mibBuilder.loadTexts:servicesAaaTypeTable.setStatus(_A)
_ServicesAaaTypeEntry_Object=MibTableRow
servicesAaaTypeEntry=_ServicesAaaTypeEntry_Object((1,3,6,1,4,1,4935,1000,100,200,100,1000,1,300,1))
servicesAaaTypeEntry.setIndexNames((0,_F,_M))
if mibBuilder.loadTexts:servicesAaaTypeEntry.setStatus(_A)
class _ServicesAaaTypeService_Type(OctetString):defaultValue=OctetString('')
_ServicesAaaTypeService_Type.__name__=_E
_ServicesAaaTypeService_Object=MibTableColumn
servicesAaaTypeService=_ServicesAaaTypeService_Object((1,3,6,1,4,1,4935,1000,100,200,100,1000,1,300,1,100),_ServicesAaaTypeService_Type())
servicesAaaTypeService.setMaxAccess(_D)
if mibBuilder.loadTexts:servicesAaaTypeService.setStatus(_A)
class _ServicesAaaTypeAuthenticationType_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200)));namedValues=NamedValues(*(('local',100),(_N,200)))
_ServicesAaaTypeAuthenticationType_Type.__name__=_C
_ServicesAaaTypeAuthenticationType_Object=MibTableColumn
servicesAaaTypeAuthenticationType=_ServicesAaaTypeAuthenticationType_Object((1,3,6,1,4,1,4935,1000,100,200,100,1000,1,300,1,200),_ServicesAaaTypeAuthenticationType_Type())
servicesAaaTypeAuthenticationType.setMaxAccess(_B)
if mibBuilder.loadTexts:servicesAaaTypeAuthenticationType.setStatus(_A)
class _ServicesAaaTypeAccountingType_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200)));namedValues=NamedValues(*(('none',100),(_N,200)))
_ServicesAaaTypeAccountingType_Type.__name__=_C
_ServicesAaaTypeAccountingType_Object=MibTableColumn
servicesAaaTypeAccountingType=_ServicesAaaTypeAccountingType_Object((1,3,6,1,4,1,4935,1000,100,200,100,1000,1,300,1,300),_ServicesAaaTypeAccountingType_Type())
servicesAaaTypeAccountingType.setMaxAccess(_B)
if mibBuilder.loadTexts:servicesAaaTypeAccountingType.setStatus(_A)
_RadiusGroup_ObjectIdentity=ObjectIdentity
radiusGroup=_RadiusGroup_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,1000,1,10000))
class _RadiusServersTimeoutS_Type(Unsigned32):defaultValue=5;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,5))
_RadiusServersTimeoutS_Type.__name__=_G
_RadiusServersTimeoutS_Object=MibScalar
radiusServersTimeoutS=_RadiusServersTimeoutS_Object((1,3,6,1,4,1,4935,1000,100,200,100,1000,1,10000,100),_RadiusServersTimeoutS_Type())
radiusServersTimeoutS.setMaxAccess(_B)
if mibBuilder.loadTexts:radiusServersTimeoutS.setStatus(_A)
class _RadiusUserAccessRights_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200,300)));namedValues=NamedValues(*(('admin',100),('user',200),(_K,300)))
_RadiusUserAccessRights_Type.__name__=_C
_RadiusUserAccessRights_Object=MibScalar
radiusUserAccessRights=_RadiusUserAccessRights_Object((1,3,6,1,4,1,4935,1000,100,200,100,1000,1,10000,200),_RadiusUserAccessRights_Type())
radiusUserAccessRights.setMaxAccess(_B)
if mibBuilder.loadTexts:radiusUserAccessRights.setStatus(_A)
_RadiusServersTable_Object=MibTable
radiusServersTable=_RadiusServersTable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1000,1,10000,1000))
if mibBuilder.loadTexts:radiusServersTable.setStatus(_A)
_RadiusServersEntry_Object=MibTableRow
radiusServersEntry=_RadiusServersEntry_Object((1,3,6,1,4,1,4935,1000,100,200,100,1000,1,10000,1000,1))
radiusServersEntry.setIndexNames((0,_F,_O),(0,_F,_P))
if mibBuilder.loadTexts:radiusServersEntry.setStatus(_A)
_RadiusServersService_Type=OctetString
_RadiusServersService_Object=MibTableColumn
radiusServersService=_RadiusServersService_Object((1,3,6,1,4,1,4935,1000,100,200,100,1000,1,10000,1000,1,100),_RadiusServersService_Type())
radiusServersService.setMaxAccess(_D)
if mibBuilder.loadTexts:radiusServersService.setStatus(_A)
_RadiusServersPriority_Type=Unsigned32
_RadiusServersPriority_Object=MibTableColumn
radiusServersPriority=_RadiusServersPriority_Object((1,3,6,1,4,1,4935,1000,100,200,100,1000,1,10000,1000,1,200),_RadiusServersPriority_Type())
radiusServersPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:radiusServersPriority.setStatus(_A)
class _RadiusServersAuthenticationHost_Type(MxIpHostNamePort):defaultValue=OctetString('')
_RadiusServersAuthenticationHost_Type.__name__=_H
_RadiusServersAuthenticationHost_Object=MibTableColumn
radiusServersAuthenticationHost=_RadiusServersAuthenticationHost_Object((1,3,6,1,4,1,4935,1000,100,200,100,1000,1,10000,1000,1,300),_RadiusServersAuthenticationHost_Type())
radiusServersAuthenticationHost.setMaxAccess(_B)
if mibBuilder.loadTexts:radiusServersAuthenticationHost.setStatus(_A)
class _RadiusServersAuthenticationSecret_Type(OctetString):defaultValue=OctetString('');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,512))
_RadiusServersAuthenticationSecret_Type.__name__=_E
_RadiusServersAuthenticationSecret_Object=MibTableColumn
radiusServersAuthenticationSecret=_RadiusServersAuthenticationSecret_Object((1,3,6,1,4,1,4935,1000,100,200,100,1000,1,10000,1000,1,400),_RadiusServersAuthenticationSecret_Type())
radiusServersAuthenticationSecret.setMaxAccess(_B)
if mibBuilder.loadTexts:radiusServersAuthenticationSecret.setStatus(_A)
class _RadiusServersAccountingHost_Type(MxIpHostNamePort):defaultValue=OctetString('')
_RadiusServersAccountingHost_Type.__name__=_H
_RadiusServersAccountingHost_Object=MibTableColumn
radiusServersAccountingHost=_RadiusServersAccountingHost_Object((1,3,6,1,4,1,4935,1000,100,200,100,1000,1,10000,1000,1,500),_RadiusServersAccountingHost_Type())
radiusServersAccountingHost.setMaxAccess(_B)
if mibBuilder.loadTexts:radiusServersAccountingHost.setStatus(_A)
class _RadiusServersAccountingSecret_Type(OctetString):defaultValue=OctetString('');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,512))
_RadiusServersAccountingSecret_Type.__name__=_E
_RadiusServersAccountingSecret_Object=MibTableColumn
radiusServersAccountingSecret=_RadiusServersAccountingSecret_Object((1,3,6,1,4,1,4935,1000,100,200,100,1000,1,10000,1000,1,600),_RadiusServersAccountingSecret_Type())
radiusServersAccountingSecret.setMaxAccess(_B)
if mibBuilder.loadTexts:radiusServersAccountingSecret.setStatus(_A)
_SecurityGroup_ObjectIdentity=ObjectIdentity
securityGroup=_SecurityGroup_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,1000,1,20000))
class _LoginLockedMaxRetry_Type(Unsigned32):defaultValue=5;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,5))
_LoginLockedMaxRetry_Type.__name__=_G
_LoginLockedMaxRetry_Object=MibScalar
loginLockedMaxRetry=_LoginLockedMaxRetry_Object((1,3,6,1,4,1,4935,1000,100,200,100,1000,1,20000,100),_LoginLockedMaxRetry_Type())
loginLockedMaxRetry.setMaxAccess(_B)
if mibBuilder.loadTexts:loginLockedMaxRetry.setStatus(_A)
class _LoginLockedTimeoutS_Type(Unsigned32):defaultValue=300;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,3600))
_LoginLockedTimeoutS_Type.__name__=_G
_LoginLockedTimeoutS_Object=MibScalar
loginLockedTimeoutS=_LoginLockedTimeoutS_Object((1,3,6,1,4,1,4935,1000,100,200,100,1000,1,20000,200),_LoginLockedTimeoutS_Type())
loginLockedTimeoutS.setMaxAccess(_B)
if mibBuilder.loadTexts:loginLockedTimeoutS.setStatus(_A)
_NotificationsGroup_ObjectIdentity=ObjectIdentity
notificationsGroup=_NotificationsGroup_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,1000,1,60010))
class _MinSeverity_Type(Integer32):defaultValue=300;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,100,200,300,400,500)));namedValues=NamedValues(*(('disable',0),('debug',100),('info',200),('warning',300),('error',400),('critical',500)))
_MinSeverity_Type.__name__=_C
_MinSeverity_Object=MibScalar
minSeverity=_MinSeverity_Object((1,3,6,1,4,1,4935,1000,100,200,100,1000,1,60010,100),_MinSeverity_Type())
minSeverity.setMaxAccess(_B)
if mibBuilder.loadTexts:minSeverity.setStatus(_A)
_ConfigurationGroup_ObjectIdentity=ObjectIdentity
configurationGroup=_ConfigurationGroup_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,1000,1,60020))
class _NeedRestartInfo_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,100)));namedValues=NamedValues(*(('no',0),('yes',100)))
_NeedRestartInfo_Type.__name__=_C
_NeedRestartInfo_Object=MibScalar
needRestartInfo=_NeedRestartInfo_Object((1,3,6,1,4,1,4935,1000,100,200,100,1000,1,60020,100),_NeedRestartInfo_Type())
needRestartInfo.setMaxAccess(_D)
if mibBuilder.loadTexts:needRestartInfo.setStatus(_A)
mibBuilder.exportSymbols(_F,**{'aaaMIB':aaaMIB,'aaaMIBObjects':aaaMIBObjects,'usersTable':usersTable,'usersEntry':usersEntry,_J:usersUserName,'usersPassword':usersPassword,'usersAccessRights':usersAccessRights,'usersLockProtectionEnable':usersLockProtectionEnable,'usersDelete':usersDelete,'usersStatusTable':usersStatusTable,'usersStatusEntry':usersStatusEntry,_L:usersStatusUserName,'usersStatusPassword':usersStatusPassword,'usersStatusLocked':usersStatusLocked,'batchUser':batchUser,'servicesAaaTypeTable':servicesAaaTypeTable,'servicesAaaTypeEntry':servicesAaaTypeEntry,_M:servicesAaaTypeService,'servicesAaaTypeAuthenticationType':servicesAaaTypeAuthenticationType,'servicesAaaTypeAccountingType':servicesAaaTypeAccountingType,'radiusGroup':radiusGroup,'radiusServersTimeoutS':radiusServersTimeoutS,'radiusUserAccessRights':radiusUserAccessRights,'radiusServersTable':radiusServersTable,'radiusServersEntry':radiusServersEntry,_O:radiusServersService,_P:radiusServersPriority,'radiusServersAuthenticationHost':radiusServersAuthenticationHost,'radiusServersAuthenticationSecret':radiusServersAuthenticationSecret,'radiusServersAccountingHost':radiusServersAccountingHost,'radiusServersAccountingSecret':radiusServersAccountingSecret,'securityGroup':securityGroup,'loginLockedMaxRetry':loginLockedMaxRetry,'loginLockedTimeoutS':loginLockedTimeoutS,'notificationsGroup':notificationsGroup,'minSeverity':minSeverity,'configurationGroup':configurationGroup,'needRestartInfo':needRestartInfo})