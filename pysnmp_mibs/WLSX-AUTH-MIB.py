_I='portalServerIndex'
_H='not-accessible'
_G='Integer32'
_F='authServerName'
_E='read-create'
_D='WLSX-AUTH-MIB'
_C='DisplayString'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
wlsxEnterpriseMibModules,=mibBuilder.importSymbols('ARUBA-MIB','wlsxEnterpriseMibModules')
ArubaAuthServerType,ArubaAuthenticationMethods,ArubaEnableValue,ArubaEncryptionMethods,ArubaHashAlgorithms=mibBuilder.importSymbols('ARUBA-TC','ArubaAuthServerType','ArubaAuthenticationMethods','ArubaEnableValue','ArubaEncryptionMethods','ArubaHashAlgorithms')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso,snmpModules=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_G,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso','snmpModules')
DisplayString,MacAddress,PhysAddress,RowStatus,StorageType,TAddress,TDomain,TextualConvention,TestAndIncr,TimeInterval,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_C,'MacAddress','PhysAddress','RowStatus','StorageType','TAddress','TDomain','TextualConvention','TestAndIncr','TimeInterval','TruthValue')
wlsxAuthMIB=ModuleIdentity((1,3,6,1,4,1,14823,2,2,1,8))
if mibBuilder.loadTexts:wlsxAuthMIB.setRevisions(('2020-08-14 17:45',))
_WlsxAuthenticationServerGroup_ObjectIdentity=ObjectIdentity
wlsxAuthenticationServerGroup=_WlsxAuthenticationServerGroup_ObjectIdentity((1,3,6,1,4,1,14823,2,2,1,8,1))
_WlsxAuthenticationServerTable_Object=MibTable
wlsxAuthenticationServerTable=_WlsxAuthenticationServerTable_Object((1,3,6,1,4,1,14823,2,2,1,8,1,1))
if mibBuilder.loadTexts:wlsxAuthenticationServerTable.setStatus(_A)
_WlsxAuthenticationServerEntry_Object=MibTableRow
wlsxAuthenticationServerEntry=_WlsxAuthenticationServerEntry_Object((1,3,6,1,4,1,14823,2,2,1,8,1,1,1))
wlsxAuthenticationServerEntry.setIndexNames((0,_D,_F))
if mibBuilder.loadTexts:wlsxAuthenticationServerEntry.setStatus(_A)
class _AuthServerName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_AuthServerName_Type.__name__=_C
_AuthServerName_Object=MibTableColumn
authServerName=_AuthServerName_Object((1,3,6,1,4,1,14823,2,2,1,8,1,1,1,1),_AuthServerName_Type())
authServerName.setMaxAccess(_H)
if mibBuilder.loadTexts:authServerName.setStatus(_A)
_AuthServerType_Type=ArubaAuthServerType
_AuthServerType_Object=MibTableColumn
authServerType=_AuthServerType_Object((1,3,6,1,4,1,14823,2,2,1,8,1,1,1,2),_AuthServerType_Type())
authServerType.setMaxAccess(_B)
if mibBuilder.loadTexts:authServerType.setStatus(_A)
class _AuthServerAddress_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,48))
_AuthServerAddress_Type.__name__=_C
_AuthServerAddress_Object=MibTableColumn
authServerAddress=_AuthServerAddress_Object((1,3,6,1,4,1,14823,2,2,1,8,1,1,1,3),_AuthServerAddress_Type())
authServerAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:authServerAddress.setStatus(_A)
_AuthServerPort_Type=Integer32
_AuthServerPort_Object=MibTableColumn
authServerPort=_AuthServerPort_Object((1,3,6,1,4,1,14823,2,2,1,8,1,1,1,4),_AuthServerPort_Type())
authServerPort.setMaxAccess(_E)
if mibBuilder.loadTexts:authServerPort.setStatus(_A)
_AuthServerRetryCount_Type=Integer32
_AuthServerRetryCount_Object=MibTableColumn
authServerRetryCount=_AuthServerRetryCount_Object((1,3,6,1,4,1,14823,2,2,1,8,1,1,1,5),_AuthServerRetryCount_Type())
authServerRetryCount.setMaxAccess(_E)
if mibBuilder.loadTexts:authServerRetryCount.setStatus(_A)
_AuthServerTimeOutValue_Type=Integer32
_AuthServerTimeOutValue_Object=MibTableColumn
authServerTimeOutValue=_AuthServerTimeOutValue_Object((1,3,6,1,4,1,14823,2,2,1,8,1,1,1,6),_AuthServerTimeOutValue_Type())
authServerTimeOutValue.setMaxAccess(_E)
if mibBuilder.loadTexts:authServerTimeOutValue.setStatus(_A)
_AuthServerState_Type=ArubaEnableValue
_AuthServerState_Object=MibTableColumn
authServerState=_AuthServerState_Object((1,3,6,1,4,1,14823,2,2,1,8,1,1,1,7),_AuthServerState_Type())
authServerState.setMaxAccess(_B)
if mibBuilder.loadTexts:authServerState.setStatus(_A)
_AuthServerInservice_Type=TruthValue
_AuthServerInservice_Object=MibTableColumn
authServerInservice=_AuthServerInservice_Object((1,3,6,1,4,1,14823,2,2,1,8,1,1,1,8),_AuthServerInservice_Type())
authServerInservice.setMaxAccess(_B)
if mibBuilder.loadTexts:authServerInservice.setStatus(_A)
_AuthServerUsageCount_Type=Counter32
_AuthServerUsageCount_Object=MibTableColumn
authServerUsageCount=_AuthServerUsageCount_Object((1,3,6,1,4,1,14823,2,2,1,8,1,1,1,9),_AuthServerUsageCount_Type())
authServerUsageCount.setMaxAccess(_B)
if mibBuilder.loadTexts:authServerUsageCount.setStatus(_A)
_AuthServerSuccessfullAuths_Type=Counter32
_AuthServerSuccessfullAuths_Object=MibTableColumn
authServerSuccessfullAuths=_AuthServerSuccessfullAuths_Object((1,3,6,1,4,1,14823,2,2,1,8,1,1,1,10),_AuthServerSuccessfullAuths_Type())
authServerSuccessfullAuths.setMaxAccess(_B)
if mibBuilder.loadTexts:authServerSuccessfullAuths.setStatus(_A)
_AuthServerFailedAuths_Type=Counter32
_AuthServerFailedAuths_Object=MibTableColumn
authServerFailedAuths=_AuthServerFailedAuths_Object((1,3,6,1,4,1,14823,2,2,1,8,1,1,1,11),_AuthServerFailedAuths_Type())
authServerFailedAuths.setMaxAccess(_B)
if mibBuilder.loadTexts:authServerFailedAuths.setStatus(_A)
_AuthServerTimeouts_Type=Counter32
_AuthServerTimeouts_Object=MibTableColumn
authServerTimeouts=_AuthServerTimeouts_Object((1,3,6,1,4,1,14823,2,2,1,8,1,1,1,12),_AuthServerTimeouts_Type())
authServerTimeouts.setMaxAccess(_B)
if mibBuilder.loadTexts:authServerTimeouts.setStatus(_A)
_AuthServerAvgResponseTime_Type=Integer32
_AuthServerAvgResponseTime_Object=MibTableColumn
authServerAvgResponseTime=_AuthServerAvgResponseTime_Object((1,3,6,1,4,1,14823,2,2,1,8,1,1,1,13),_AuthServerAvgResponseTime_Type())
authServerAvgResponseTime.setMaxAccess(_B)
if mibBuilder.loadTexts:authServerAvgResponseTime.setStatus(_A)
_AuthServerOutStandingRequests_Type=Integer32
_AuthServerOutStandingRequests_Object=MibTableColumn
authServerOutStandingRequests=_AuthServerOutStandingRequests_Object((1,3,6,1,4,1,14823,2,2,1,8,1,1,1,14),_AuthServerOutStandingRequests_Type())
authServerOutStandingRequests.setMaxAccess(_B)
if mibBuilder.loadTexts:authServerOutStandingRequests.setStatus(_A)
_AuthServerUptime_Type=Integer32
_AuthServerUptime_Object=MibTableColumn
authServerUptime=_AuthServerUptime_Object((1,3,6,1,4,1,14823,2,2,1,8,1,1,1,15),_AuthServerUptime_Type())
authServerUptime.setMaxAccess(_B)
if mibBuilder.loadTexts:authServerUptime.setStatus(_A)
_WlsxPortalServerTable_Object=MibTable
wlsxPortalServerTable=_WlsxPortalServerTable_Object((1,3,6,1,4,1,14823,2,2,1,8,1,2))
if mibBuilder.loadTexts:wlsxPortalServerTable.setStatus(_A)
_WlsxPortalServerEntry_Object=MibTableRow
wlsxPortalServerEntry=_WlsxPortalServerEntry_Object((1,3,6,1,4,1,14823,2,2,1,8,1,2,1))
wlsxPortalServerEntry.setIndexNames((0,_D,_I))
if mibBuilder.loadTexts:wlsxPortalServerEntry.setStatus(_A)
class _PortalServerIndex_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,256))
_PortalServerIndex_Type.__name__=_C
_PortalServerIndex_Object=MibTableColumn
portalServerIndex=_PortalServerIndex_Object((1,3,6,1,4,1,14823,2,2,1,8,1,2,1,1),_PortalServerIndex_Type())
portalServerIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:portalServerIndex.setStatus(_A)
class _PortalServerHost_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,256))
_PortalServerHost_Type.__name__=_C
_PortalServerHost_Object=MibTableColumn
portalServerHost=_PortalServerHost_Object((1,3,6,1,4,1,14823,2,2,1,8,1,2,1,2),_PortalServerHost_Type())
portalServerHost.setMaxAccess(_B)
if mibBuilder.loadTexts:portalServerHost.setStatus(_A)
_PortalServerPort_Type=Integer32
_PortalServerPort_Object=MibTableColumn
portalServerPort=_PortalServerPort_Object((1,3,6,1,4,1,14823,2,2,1,8,1,2,1,3),_PortalServerPort_Type())
portalServerPort.setMaxAccess(_B)
if mibBuilder.loadTexts:portalServerPort.setStatus(_A)
class _PortalServerPage_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,256))
_PortalServerPage_Type.__name__=_C
_PortalServerPage_Object=MibTableColumn
portalServerPage=_PortalServerPage_Object((1,3,6,1,4,1,14823,2,2,1,8,1,2,1,4),_PortalServerPage_Type())
portalServerPage.setMaxAccess(_B)
if mibBuilder.loadTexts:portalServerPage.setStatus(_A)
_PortalServerProtocol_Type=DisplayString
_PortalServerProtocol_Object=MibTableColumn
portalServerProtocol=_PortalServerProtocol_Object((1,3,6,1,4,1,14823,2,2,1,8,1,2,1,5),_PortalServerProtocol_Type())
portalServerProtocol.setMaxAccess(_B)
if mibBuilder.loadTexts:portalServerProtocol.setStatus(_A)
_WlsxLdapServerStateTable_Object=MibTable
wlsxLdapServerStateTable=_WlsxLdapServerStateTable_Object((1,3,6,1,4,1,14823,2,2,1,8,1,5))
if mibBuilder.loadTexts:wlsxLdapServerStateTable.setStatus(_A)
_WlsxLdapServerStateEntry_Object=MibTableRow
wlsxLdapServerStateEntry=_WlsxLdapServerStateEntry_Object((1,3,6,1,4,1,14823,2,2,1,8,1,5,1))
wlsxLdapServerStateEntry.setIndexNames((0,_D,_F))
if mibBuilder.loadTexts:wlsxLdapServerStateEntry.setStatus(_A)
_LdapInitDone_Type=TruthValue
_LdapInitDone_Object=MibTableColumn
ldapInitDone=_LdapInitDone_Object((1,3,6,1,4,1,14823,2,2,1,8,1,5,1,1),_LdapInitDone_Type())
ldapInitDone.setMaxAccess(_B)
if mibBuilder.loadTexts:ldapInitDone.setStatus(_A)
class _LdapAdminBound_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('no',1),('yes',2),('inProgress',3)))
_LdapAdminBound_Type.__name__=_G
_LdapAdminBound_Object=MibTableColumn
ldapAdminBound=_LdapAdminBound_Object((1,3,6,1,4,1,14823,2,2,1,8,1,5,1,2),_LdapAdminBound_Type())
ldapAdminBound.setMaxAccess(_B)
if mibBuilder.loadTexts:ldapAdminBound.setStatus(_A)
_LdapReBindCount_Type=Counter32
_LdapReBindCount_Object=MibTableColumn
ldapReBindCount=_LdapReBindCount_Object((1,3,6,1,4,1,14823,2,2,1,8,1,5,1,3),_LdapReBindCount_Type())
ldapReBindCount.setMaxAccess(_B)
if mibBuilder.loadTexts:ldapReBindCount.setStatus(_A)
_WlsxAuthenticationInfoGroup_ObjectIdentity=ObjectIdentity
wlsxAuthenticationInfoGroup=_WlsxAuthenticationInfoGroup_ObjectIdentity((1,3,6,1,4,1,14823,2,2,1,8,2))
_WlsxAuthenticationGroup_ObjectIdentity=ObjectIdentity
wlsxAuthenticationGroup=_WlsxAuthenticationGroup_ObjectIdentity((1,3,6,1,4,1,14823,2,2,1,8,3))
mibBuilder.exportSymbols(_D,**{'wlsxAuthMIB':wlsxAuthMIB,'wlsxAuthenticationServerGroup':wlsxAuthenticationServerGroup,'wlsxAuthenticationServerTable':wlsxAuthenticationServerTable,'wlsxAuthenticationServerEntry':wlsxAuthenticationServerEntry,_F:authServerName,'authServerType':authServerType,'authServerAddress':authServerAddress,'authServerPort':authServerPort,'authServerRetryCount':authServerRetryCount,'authServerTimeOutValue':authServerTimeOutValue,'authServerState':authServerState,'authServerInservice':authServerInservice,'authServerUsageCount':authServerUsageCount,'authServerSuccessfullAuths':authServerSuccessfullAuths,'authServerFailedAuths':authServerFailedAuths,'authServerTimeouts':authServerTimeouts,'authServerAvgResponseTime':authServerAvgResponseTime,'authServerOutStandingRequests':authServerOutStandingRequests,'authServerUptime':authServerUptime,'wlsxPortalServerTable':wlsxPortalServerTable,'wlsxPortalServerEntry':wlsxPortalServerEntry,_I:portalServerIndex,'portalServerHost':portalServerHost,'portalServerPort':portalServerPort,'portalServerPage':portalServerPage,'portalServerProtocol':portalServerProtocol,'wlsxLdapServerStateTable':wlsxLdapServerStateTable,'wlsxLdapServerStateEntry':wlsxLdapServerStateEntry,'ldapInitDone':ldapInitDone,'ldapAdminBound':ldapAdminBound,'ldapReBindCount':ldapReBindCount,'wlsxAuthenticationInfoGroup':wlsxAuthenticationInfoGroup,'wlsxAuthenticationGroup':wlsxAuthenticationGroup})