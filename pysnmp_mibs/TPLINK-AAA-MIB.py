_N='tacacsDeamonServerIp'
_M='radiusDeamonServerIp'
_L='acctDot1xListName'
_K='authenDot1xListName'
_J='authenEnableListName'
_I='authenLoginListName'
_H='moduleId'
_G='Integer32'
_F='read-only'
_E='TPLINK-AAA-MIB'
_D='read-write'
_C='read-create'
_B='OctetString'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_B,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_G,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
tplinkMgmt,=mibBuilder.importSymbols('TPLINK-MIB','tplinkMgmt')
TPRowStatus,=mibBuilder.importSymbols('TPLINK-TC-MIB','TPRowStatus')
tplinkAaaMIB=ModuleIdentity((1,3,6,1,4,1,11863,6,82))
if mibBuilder.loadTexts:tplinkAaaMIB.setRevisions(('2015-06-11 14:30',))
_AaaGlobalConfig_ObjectIdentity=ObjectIdentity
aaaGlobalConfig=_AaaGlobalConfig_ObjectIdentity((1,3,6,1,4,1,11863,6,82,1))
class _AaaEnableAdminPassword_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_AaaEnableAdminPassword_Type.__name__=_B
_AaaEnableAdminPassword_Object=MibScalar
aaaEnableAdminPassword=_AaaEnableAdminPassword_Object((1,3,6,1,4,1,11863,6,82,1,2),_AaaEnableAdminPassword_Type())
aaaEnableAdminPassword.setMaxAccess(_D)
if mibBuilder.loadTexts:aaaEnableAdminPassword.setStatus(_A)
_AaaApplicationList_ObjectIdentity=ObjectIdentity
aaaApplicationList=_AaaApplicationList_ObjectIdentity((1,3,6,1,4,1,11863,6,82,1,3))
_AaaApplicationListTable_Object=MibTable
aaaApplicationListTable=_AaaApplicationListTable_Object((1,3,6,1,4,1,11863,6,82,1,3,1))
if mibBuilder.loadTexts:aaaApplicationListTable.setStatus(_A)
_AaaApplicationListEntry_Object=MibTableRow
aaaApplicationListEntry=_AaaApplicationListEntry_Object((1,3,6,1,4,1,11863,6,82,1,3,1,1))
aaaApplicationListEntry.setIndexNames((0,_E,_H))
if mibBuilder.loadTexts:aaaApplicationListEntry.setStatus(_A)
_ModuleId_Type=Integer32
_ModuleId_Object=MibTableColumn
moduleId=_ModuleId_Object((1,3,6,1,4,1,11863,6,82,1,3,1,1,1),_ModuleId_Type())
moduleId.setMaxAccess(_F)
if mibBuilder.loadTexts:moduleId.setStatus(_A)
class _ModuleName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_ModuleName_Type.__name__=_B
_ModuleName_Object=MibTableColumn
moduleName=_ModuleName_Object((1,3,6,1,4,1,11863,6,82,1,3,1,1,2),_ModuleName_Type())
moduleName.setMaxAccess(_F)
if mibBuilder.loadTexts:moduleName.setStatus(_A)
class _LoginList_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_LoginList_Type.__name__=_B
_LoginList_Object=MibTableColumn
loginList=_LoginList_Object((1,3,6,1,4,1,11863,6,82,1,3,1,1,3),_LoginList_Type())
loginList.setMaxAccess(_D)
if mibBuilder.loadTexts:loginList.setStatus(_A)
class _EnableList_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_EnableList_Type.__name__=_B
_EnableList_Object=MibTableColumn
enableList=_EnableList_Object((1,3,6,1,4,1,11863,6,82,1,3,1,1,4),_EnableList_Type())
enableList.setMaxAccess(_D)
if mibBuilder.loadTexts:enableList.setStatus(_A)
_AaaAuthenticationListConfig_ObjectIdentity=ObjectIdentity
aaaAuthenticationListConfig=_AaaAuthenticationListConfig_ObjectIdentity((1,3,6,1,4,1,11863,6,82,2))
_AuthenticationLoginMethodListTable_Object=MibTable
authenticationLoginMethodListTable=_AuthenticationLoginMethodListTable_Object((1,3,6,1,4,1,11863,6,82,2,1))
if mibBuilder.loadTexts:authenticationLoginMethodListTable.setStatus(_A)
_AuthenticationLoginMethodListEntry_Object=MibTableRow
authenticationLoginMethodListEntry=_AuthenticationLoginMethodListEntry_Object((1,3,6,1,4,1,11863,6,82,2,1,1))
authenticationLoginMethodListEntry.setIndexNames((0,_E,_I))
if mibBuilder.loadTexts:authenticationLoginMethodListEntry.setStatus(_A)
class _AuthenLoginListName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_AuthenLoginListName_Type.__name__=_B
_AuthenLoginListName_Object=MibTableColumn
authenLoginListName=_AuthenLoginListName_Object((1,3,6,1,4,1,11863,6,82,2,1,1,1),_AuthenLoginListName_Type())
authenLoginListName.setMaxAccess(_C)
if mibBuilder.loadTexts:authenLoginListName.setStatus(_A)
class _AuthenLoginPri1_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_AuthenLoginPri1_Type.__name__=_B
_AuthenLoginPri1_Object=MibTableColumn
authenLoginPri1=_AuthenLoginPri1_Object((1,3,6,1,4,1,11863,6,82,2,1,1,2),_AuthenLoginPri1_Type())
authenLoginPri1.setMaxAccess(_D)
if mibBuilder.loadTexts:authenLoginPri1.setStatus(_A)
class _AuthenLoginPri2_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_AuthenLoginPri2_Type.__name__=_B
_AuthenLoginPri2_Object=MibTableColumn
authenLoginPri2=_AuthenLoginPri2_Object((1,3,6,1,4,1,11863,6,82,2,1,1,3),_AuthenLoginPri2_Type())
authenLoginPri2.setMaxAccess(_D)
if mibBuilder.loadTexts:authenLoginPri2.setStatus(_A)
class _AuthenLoginPri3_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_AuthenLoginPri3_Type.__name__=_B
_AuthenLoginPri3_Object=MibTableColumn
authenLoginPri3=_AuthenLoginPri3_Object((1,3,6,1,4,1,11863,6,82,2,1,1,4),_AuthenLoginPri3_Type())
authenLoginPri3.setMaxAccess(_D)
if mibBuilder.loadTexts:authenLoginPri3.setStatus(_A)
class _AuthenLoginPri4_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_AuthenLoginPri4_Type.__name__=_B
_AuthenLoginPri4_Object=MibTableColumn
authenLoginPri4=_AuthenLoginPri4_Object((1,3,6,1,4,1,11863,6,82,2,1,1,5),_AuthenLoginPri4_Type())
authenLoginPri4.setMaxAccess(_D)
if mibBuilder.loadTexts:authenLoginPri4.setStatus(_A)
_AuthenLoginStatus_Type=TPRowStatus
_AuthenLoginStatus_Object=MibTableColumn
authenLoginStatus=_AuthenLoginStatus_Object((1,3,6,1,4,1,11863,6,82,2,1,1,6),_AuthenLoginStatus_Type())
authenLoginStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:authenLoginStatus.setStatus(_A)
_AuthenticationEnableMethodListTable_Object=MibTable
authenticationEnableMethodListTable=_AuthenticationEnableMethodListTable_Object((1,3,6,1,4,1,11863,6,82,2,2))
if mibBuilder.loadTexts:authenticationEnableMethodListTable.setStatus(_A)
_AuthenticationEnableMethodListEntry_Object=MibTableRow
authenticationEnableMethodListEntry=_AuthenticationEnableMethodListEntry_Object((1,3,6,1,4,1,11863,6,82,2,2,1))
authenticationEnableMethodListEntry.setIndexNames((0,_E,_J))
if mibBuilder.loadTexts:authenticationEnableMethodListEntry.setStatus(_A)
class _AuthenEnableListName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_AuthenEnableListName_Type.__name__=_B
_AuthenEnableListName_Object=MibTableColumn
authenEnableListName=_AuthenEnableListName_Object((1,3,6,1,4,1,11863,6,82,2,2,1,1),_AuthenEnableListName_Type())
authenEnableListName.setMaxAccess(_C)
if mibBuilder.loadTexts:authenEnableListName.setStatus(_A)
class _AuthenEnablePri1_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_AuthenEnablePri1_Type.__name__=_B
_AuthenEnablePri1_Object=MibTableColumn
authenEnablePri1=_AuthenEnablePri1_Object((1,3,6,1,4,1,11863,6,82,2,2,1,2),_AuthenEnablePri1_Type())
authenEnablePri1.setMaxAccess(_D)
if mibBuilder.loadTexts:authenEnablePri1.setStatus(_A)
class _AuthenEnablePri2_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_AuthenEnablePri2_Type.__name__=_B
_AuthenEnablePri2_Object=MibTableColumn
authenEnablePri2=_AuthenEnablePri2_Object((1,3,6,1,4,1,11863,6,82,2,2,1,3),_AuthenEnablePri2_Type())
authenEnablePri2.setMaxAccess(_D)
if mibBuilder.loadTexts:authenEnablePri2.setStatus(_A)
class _AuthenEnablePri3_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_AuthenEnablePri3_Type.__name__=_B
_AuthenEnablePri3_Object=MibTableColumn
authenEnablePri3=_AuthenEnablePri3_Object((1,3,6,1,4,1,11863,6,82,2,2,1,4),_AuthenEnablePri3_Type())
authenEnablePri3.setMaxAccess(_D)
if mibBuilder.loadTexts:authenEnablePri3.setStatus(_A)
class _AuthenEnablePri4_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_AuthenEnablePri4_Type.__name__=_B
_AuthenEnablePri4_Object=MibTableColumn
authenEnablePri4=_AuthenEnablePri4_Object((1,3,6,1,4,1,11863,6,82,2,2,1,5),_AuthenEnablePri4_Type())
authenEnablePri4.setMaxAccess(_D)
if mibBuilder.loadTexts:authenEnablePri4.setStatus(_A)
_AuthenEnableStatus_Type=TPRowStatus
_AuthenEnableStatus_Object=MibTableColumn
authenEnableStatus=_AuthenEnableStatus_Object((1,3,6,1,4,1,11863,6,82,2,2,1,6),_AuthenEnableStatus_Type())
authenEnableStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:authenEnableStatus.setStatus(_A)
_AaaDot1xListConfig_ObjectIdentity=ObjectIdentity
aaaDot1xListConfig=_AaaDot1xListConfig_ObjectIdentity((1,3,6,1,4,1,11863,6,82,3))
_AuthenticationDot1xMethodListTable_Object=MibTable
authenticationDot1xMethodListTable=_AuthenticationDot1xMethodListTable_Object((1,3,6,1,4,1,11863,6,82,3,1))
if mibBuilder.loadTexts:authenticationDot1xMethodListTable.setStatus(_A)
_AuthenticationDot1xMethodListEntry_Object=MibTableRow
authenticationDot1xMethodListEntry=_AuthenticationDot1xMethodListEntry_Object((1,3,6,1,4,1,11863,6,82,3,1,1))
authenticationDot1xMethodListEntry.setIndexNames((0,_E,_K))
if mibBuilder.loadTexts:authenticationDot1xMethodListEntry.setStatus(_A)
class _AuthenDot1xListName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_AuthenDot1xListName_Type.__name__=_B
_AuthenDot1xListName_Object=MibTableColumn
authenDot1xListName=_AuthenDot1xListName_Object((1,3,6,1,4,1,11863,6,82,3,1,1,1),_AuthenDot1xListName_Type())
authenDot1xListName.setMaxAccess(_F)
if mibBuilder.loadTexts:authenDot1xListName.setStatus(_A)
class _AuthenDot1xPri1_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_AuthenDot1xPri1_Type.__name__=_B
_AuthenDot1xPri1_Object=MibTableColumn
authenDot1xPri1=_AuthenDot1xPri1_Object((1,3,6,1,4,1,11863,6,82,3,1,1,2),_AuthenDot1xPri1_Type())
authenDot1xPri1.setMaxAccess(_D)
if mibBuilder.loadTexts:authenDot1xPri1.setStatus(_A)
_AuthenDot1xStatus_Type=TPRowStatus
_AuthenDot1xStatus_Object=MibTableColumn
authenDot1xStatus=_AuthenDot1xStatus_Object((1,3,6,1,4,1,11863,6,82,3,1,1,3),_AuthenDot1xStatus_Type())
authenDot1xStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:authenDot1xStatus.setStatus(_A)
_AccountingDot1xMethodListTable_Object=MibTable
accountingDot1xMethodListTable=_AccountingDot1xMethodListTable_Object((1,3,6,1,4,1,11863,6,82,3,2))
if mibBuilder.loadTexts:accountingDot1xMethodListTable.setStatus(_A)
_AccountingDot1xMethodListEntry_Object=MibTableRow
accountingDot1xMethodListEntry=_AccountingDot1xMethodListEntry_Object((1,3,6,1,4,1,11863,6,82,3,2,1))
accountingDot1xMethodListEntry.setIndexNames((0,_E,_L))
if mibBuilder.loadTexts:accountingDot1xMethodListEntry.setStatus(_A)
class _AcctDot1xListName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_AcctDot1xListName_Type.__name__=_B
_AcctDot1xListName_Object=MibTableColumn
acctDot1xListName=_AcctDot1xListName_Object((1,3,6,1,4,1,11863,6,82,3,2,1,1),_AcctDot1xListName_Type())
acctDot1xListName.setMaxAccess(_F)
if mibBuilder.loadTexts:acctDot1xListName.setStatus(_A)
class _AcctDot1xPri1_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_AcctDot1xPri1_Type.__name__=_B
_AcctDot1xPri1_Object=MibTableColumn
acctDot1xPri1=_AcctDot1xPri1_Object((1,3,6,1,4,1,11863,6,82,3,2,1,2),_AcctDot1xPri1_Type())
acctDot1xPri1.setMaxAccess(_D)
if mibBuilder.loadTexts:acctDot1xPri1.setStatus(_A)
_AcctDot1xStatus_Type=TPRowStatus
_AcctDot1xStatus_Object=MibTableColumn
acctDot1xStatus=_AcctDot1xStatus_Object((1,3,6,1,4,1,11863,6,82,3,2,1,3),_AcctDot1xStatus_Type())
acctDot1xStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:acctDot1xStatus.setStatus(_A)
_RadiusDeamonTable_Object=MibTable
radiusDeamonTable=_RadiusDeamonTable_Object((1,3,6,1,4,1,11863,6,82,4))
if mibBuilder.loadTexts:radiusDeamonTable.setStatus(_A)
_RadiusDeamonEntry_Object=MibTableRow
radiusDeamonEntry=_RadiusDeamonEntry_Object((1,3,6,1,4,1,11863,6,82,4,1))
radiusDeamonEntry.setIndexNames((0,_E,_M))
if mibBuilder.loadTexts:radiusDeamonEntry.setStatus(_A)
_RadiusDeamonServerIp_Type=IpAddress
_RadiusDeamonServerIp_Object=MibTableColumn
radiusDeamonServerIp=_RadiusDeamonServerIp_Object((1,3,6,1,4,1,11863,6,82,4,1,1),_RadiusDeamonServerIp_Type())
radiusDeamonServerIp.setMaxAccess(_F)
if mibBuilder.loadTexts:radiusDeamonServerIp.setStatus(_A)
class _RadiusDeamonTimeout_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,9))
_RadiusDeamonTimeout_Type.__name__=_G
_RadiusDeamonTimeout_Object=MibTableColumn
radiusDeamonTimeout=_RadiusDeamonTimeout_Object((1,3,6,1,4,1,11863,6,82,4,1,2),_RadiusDeamonTimeout_Type())
radiusDeamonTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:radiusDeamonTimeout.setStatus(_A)
class _RadiusDeamonRetransimit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,3))
_RadiusDeamonRetransimit_Type.__name__=_G
_RadiusDeamonRetransimit_Object=MibTableColumn
radiusDeamonRetransimit=_RadiusDeamonRetransimit_Object((1,3,6,1,4,1,11863,6,82,4,1,3),_RadiusDeamonRetransimit_Type())
radiusDeamonRetransimit.setMaxAccess(_C)
if mibBuilder.loadTexts:radiusDeamonRetransimit.setStatus(_A)
class _RadiusDeamonKey_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_RadiusDeamonKey_Type.__name__=_B
_RadiusDeamonKey_Object=MibTableColumn
radiusDeamonKey=_RadiusDeamonKey_Object((1,3,6,1,4,1,11863,6,82,4,1,4),_RadiusDeamonKey_Type())
radiusDeamonKey.setMaxAccess(_C)
if mibBuilder.loadTexts:radiusDeamonKey.setStatus(_A)
class _RadiusDeamonAuthPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_RadiusDeamonAuthPort_Type.__name__=_G
_RadiusDeamonAuthPort_Object=MibTableColumn
radiusDeamonAuthPort=_RadiusDeamonAuthPort_Object((1,3,6,1,4,1,11863,6,82,4,1,5),_RadiusDeamonAuthPort_Type())
radiusDeamonAuthPort.setMaxAccess(_C)
if mibBuilder.loadTexts:radiusDeamonAuthPort.setStatus(_A)
class _RadiusDeamonAcctPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_RadiusDeamonAcctPort_Type.__name__=_G
_RadiusDeamonAcctPort_Object=MibTableColumn
radiusDeamonAcctPort=_RadiusDeamonAcctPort_Object((1,3,6,1,4,1,11863,6,82,4,1,6),_RadiusDeamonAcctPort_Type())
radiusDeamonAcctPort.setMaxAccess(_C)
if mibBuilder.loadTexts:radiusDeamonAcctPort.setStatus(_A)
class _RadiusDeamonNasId_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_RadiusDeamonNasId_Type.__name__=_B
_RadiusDeamonNasId_Object=MibTableColumn
radiusDeamonNasId=_RadiusDeamonNasId_Object((1,3,6,1,4,1,11863,6,82,4,1,7),_RadiusDeamonNasId_Type())
radiusDeamonNasId.setMaxAccess(_C)
if mibBuilder.loadTexts:radiusDeamonNasId.setStatus(_A)
_RadiusDeamonStatus_Type=TPRowStatus
_RadiusDeamonStatus_Object=MibTableColumn
radiusDeamonStatus=_RadiusDeamonStatus_Object((1,3,6,1,4,1,11863,6,82,4,1,8),_RadiusDeamonStatus_Type())
radiusDeamonStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:radiusDeamonStatus.setStatus(_A)
_TacacsDeamonTable_Object=MibTable
tacacsDeamonTable=_TacacsDeamonTable_Object((1,3,6,1,4,1,11863,6,82,5))
if mibBuilder.loadTexts:tacacsDeamonTable.setStatus(_A)
_TacacsDeamonEntry_Object=MibTableRow
tacacsDeamonEntry=_TacacsDeamonEntry_Object((1,3,6,1,4,1,11863,6,82,5,1))
tacacsDeamonEntry.setIndexNames((0,_E,_N))
if mibBuilder.loadTexts:tacacsDeamonEntry.setStatus(_A)
_TacacsDeamonServerIp_Type=IpAddress
_TacacsDeamonServerIp_Object=MibTableColumn
tacacsDeamonServerIp=_TacacsDeamonServerIp_Object((1,3,6,1,4,1,11863,6,82,5,1,1),_TacacsDeamonServerIp_Type())
tacacsDeamonServerIp.setMaxAccess(_F)
if mibBuilder.loadTexts:tacacsDeamonServerIp.setStatus(_A)
class _TacacsDeamonTimeout_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_TacacsDeamonTimeout_Type.__name__=_G
_TacacsDeamonTimeout_Object=MibTableColumn
tacacsDeamonTimeout=_TacacsDeamonTimeout_Object((1,3,6,1,4,1,11863,6,82,5,1,2),_TacacsDeamonTimeout_Type())
tacacsDeamonTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:tacacsDeamonTimeout.setStatus(_A)
class _TacacsDeamonKey_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_TacacsDeamonKey_Type.__name__=_B
_TacacsDeamonKey_Object=MibTableColumn
tacacsDeamonKey=_TacacsDeamonKey_Object((1,3,6,1,4,1,11863,6,82,5,1,3),_TacacsDeamonKey_Type())
tacacsDeamonKey.setMaxAccess(_C)
if mibBuilder.loadTexts:tacacsDeamonKey.setStatus(_A)
class _TacacsDeamonPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_TacacsDeamonPort_Type.__name__=_G
_TacacsDeamonPort_Object=MibTableColumn
tacacsDeamonPort=_TacacsDeamonPort_Object((1,3,6,1,4,1,11863,6,82,5,1,4),_TacacsDeamonPort_Type())
tacacsDeamonPort.setMaxAccess(_C)
if mibBuilder.loadTexts:tacacsDeamonPort.setStatus(_A)
_TacacsDeamonStatus_Type=TPRowStatus
_TacacsDeamonStatus_Object=MibTableColumn
tacacsDeamonStatus=_TacacsDeamonStatus_Object((1,3,6,1,4,1,11863,6,82,5,1,5),_TacacsDeamonStatus_Type())
tacacsDeamonStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:tacacsDeamonStatus.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'tplinkAaaMIB':tplinkAaaMIB,'aaaGlobalConfig':aaaGlobalConfig,'aaaEnableAdminPassword':aaaEnableAdminPassword,'aaaApplicationList':aaaApplicationList,'aaaApplicationListTable':aaaApplicationListTable,'aaaApplicationListEntry':aaaApplicationListEntry,_H:moduleId,'moduleName':moduleName,'loginList':loginList,'enableList':enableList,'aaaAuthenticationListConfig':aaaAuthenticationListConfig,'authenticationLoginMethodListTable':authenticationLoginMethodListTable,'authenticationLoginMethodListEntry':authenticationLoginMethodListEntry,_I:authenLoginListName,'authenLoginPri1':authenLoginPri1,'authenLoginPri2':authenLoginPri2,'authenLoginPri3':authenLoginPri3,'authenLoginPri4':authenLoginPri4,'authenLoginStatus':authenLoginStatus,'authenticationEnableMethodListTable':authenticationEnableMethodListTable,'authenticationEnableMethodListEntry':authenticationEnableMethodListEntry,_J:authenEnableListName,'authenEnablePri1':authenEnablePri1,'authenEnablePri2':authenEnablePri2,'authenEnablePri3':authenEnablePri3,'authenEnablePri4':authenEnablePri4,'authenEnableStatus':authenEnableStatus,'aaaDot1xListConfig':aaaDot1xListConfig,'authenticationDot1xMethodListTable':authenticationDot1xMethodListTable,'authenticationDot1xMethodListEntry':authenticationDot1xMethodListEntry,_K:authenDot1xListName,'authenDot1xPri1':authenDot1xPri1,'authenDot1xStatus':authenDot1xStatus,'accountingDot1xMethodListTable':accountingDot1xMethodListTable,'accountingDot1xMethodListEntry':accountingDot1xMethodListEntry,_L:acctDot1xListName,'acctDot1xPri1':acctDot1xPri1,'acctDot1xStatus':acctDot1xStatus,'radiusDeamonTable':radiusDeamonTable,'radiusDeamonEntry':radiusDeamonEntry,_M:radiusDeamonServerIp,'radiusDeamonTimeout':radiusDeamonTimeout,'radiusDeamonRetransimit':radiusDeamonRetransimit,'radiusDeamonKey':radiusDeamonKey,'radiusDeamonAuthPort':radiusDeamonAuthPort,'radiusDeamonAcctPort':radiusDeamonAcctPort,'radiusDeamonNasId':radiusDeamonNasId,'radiusDeamonStatus':radiusDeamonStatus,'tacacsDeamonTable':tacacsDeamonTable,'tacacsDeamonEntry':tacacsDeamonEntry,_N:tacacsDeamonServerIp,'tacacsDeamonTimeout':tacacsDeamonTimeout,'tacacsDeamonKey':tacacsDeamonKey,'tacacsDeamonPort':tacacsDeamonPort,'tacacsDeamonStatus':tacacsDeamonStatus})