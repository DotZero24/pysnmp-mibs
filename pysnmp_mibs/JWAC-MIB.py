_g='swJWACAuthStateMACAddr'
_f='swJWACAuthStateOriginalVid'
_e='swJWACAuthStatePort'
_d='swJWACWebAuthUserNameIndex'
_c='swJWACPageElementPage'
_b='delete'
_a='blocked'
_Z='authenticating'
_Y='authenticated'
_X='swJWACHostMACAddr'
_W='swJWACHostAuthStatus'
_V='swJWACHostPort'
_U='swJWACPortIndex'
_T='swJWACUpdateSVRPort'
_S='swJWACUpdateSVRProtocol'
_R='swJWACUpdateSVRMask'
_Q='swJWACUpdateSVRIpAddr'
_P='english'
_O='japanese'
_N='swJWACUpdateServerMask'
_M='swJWACUpdateServerIpAddr'
_L='not-accessible'
_K='active'
_J='read-create'
_I='obsolete'
_H='disabled'
_G='enabled'
_F='DisplayString'
_E='JWAC-MIB'
_D='read-only'
_C='Integer32'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dlink_common_mgmt,=mibBuilder.importSymbols('DLINK-ID-REC-MIB','dlink-common-mgmt')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_F,'MacAddress','PhysAddress','RowStatus','TextualConvention')
swJWACMIB=ModuleIdentity((1,3,6,1,4,1,171,12,39))
class VlanId(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_SwJWACCtrl_ObjectIdentity=ObjectIdentity
swJWACCtrl=_SwJWACCtrl_ObjectIdentity((1,3,6,1,4,1,171,12,39,1))
class _SwJWACState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_SwJWACState_Type.__name__=_C
_SwJWACState_Object=MibScalar
swJWACState=_SwJWACState_Object((1,3,6,1,4,1,171,12,39,1,1),_SwJWACState_Type())
swJWACState.setMaxAccess(_B)
if mibBuilder.loadTexts:swJWACState.setStatus(_A)
class _SwJWACRedirectState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_SwJWACRedirectState_Type.__name__=_C
_SwJWACRedirectState_Object=MibScalar
swJWACRedirectState=_SwJWACRedirectState_Object((1,3,6,1,4,1,171,12,39,1,2),_SwJWACRedirectState_Type())
swJWACRedirectState.setMaxAccess(_B)
if mibBuilder.loadTexts:swJWACRedirectState.setStatus(_A)
class _SwJWACForcibleLogoutState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_SwJWACForcibleLogoutState_Type.__name__=_C
_SwJWACForcibleLogoutState_Object=MibScalar
swJWACForcibleLogoutState=_SwJWACForcibleLogoutState_Object((1,3,6,1,4,1,171,12,39,1,3),_SwJWACForcibleLogoutState_Type())
swJWACForcibleLogoutState.setMaxAccess(_B)
if mibBuilder.loadTexts:swJWACForcibleLogoutState.setStatus(_A)
class _SwJWACUDPFilteringState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_SwJWACUDPFilteringState_Type.__name__=_C
_SwJWACUDPFilteringState_Object=MibScalar
swJWACUDPFilteringState=_SwJWACUDPFilteringState_Object((1,3,6,1,4,1,171,12,39,1,4),_SwJWACUDPFilteringState_Type())
swJWACUDPFilteringState.setMaxAccess(_B)
if mibBuilder.loadTexts:swJWACUDPFilteringState.setStatus(_A)
class _SwJWACQuarantineServerMonitorState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_SwJWACQuarantineServerMonitorState_Type.__name__=_C
_SwJWACQuarantineServerMonitorState_Object=MibScalar
swJWACQuarantineServerMonitorState=_SwJWACQuarantineServerMonitorState_Object((1,3,6,1,4,1,171,12,39,1,5),_SwJWACQuarantineServerMonitorState_Type())
swJWACQuarantineServerMonitorState.setMaxAccess(_B)
if mibBuilder.loadTexts:swJWACQuarantineServerMonitorState.setStatus(_A)
class _SwJWACQuarantineServerErrorTimeOut_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,300))
_SwJWACQuarantineServerErrorTimeOut_Type.__name__=_C
_SwJWACQuarantineServerErrorTimeOut_Object=MibScalar
swJWACQuarantineServerErrorTimeOut=_SwJWACQuarantineServerErrorTimeOut_Object((1,3,6,1,4,1,171,12,39,1,6),_SwJWACQuarantineServerErrorTimeOut_Type())
swJWACQuarantineServerErrorTimeOut.setMaxAccess(_B)
if mibBuilder.loadTexts:swJWACQuarantineServerErrorTimeOut.setStatus(_A)
class _SwJWACRedirectDestination_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('quarantine_server',1),('jwac_login_page',2)))
_SwJWACRedirectDestination_Type.__name__=_C
_SwJWACRedirectDestination_Object=MibScalar
swJWACRedirectDestination=_SwJWACRedirectDestination_Object((1,3,6,1,4,1,171,12,39,1,7),_SwJWACRedirectDestination_Type())
swJWACRedirectDestination.setMaxAccess(_B)
if mibBuilder.loadTexts:swJWACRedirectDestination.setStatus(_A)
class _SwJWACRedirectDelayTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10))
_SwJWACRedirectDelayTime_Type.__name__=_C
_SwJWACRedirectDelayTime_Object=MibScalar
swJWACRedirectDelayTime=_SwJWACRedirectDelayTime_Object((1,3,6,1,4,1,171,12,39,1,8),_SwJWACRedirectDelayTime_Type())
swJWACRedirectDelayTime.setMaxAccess(_B)
if mibBuilder.loadTexts:swJWACRedirectDelayTime.setStatus(_A)
_SwJWACVirtualIpAddr_Type=IpAddress
_SwJWACVirtualIpAddr_Object=MibScalar
swJWACVirtualIpAddr=_SwJWACVirtualIpAddr_Object((1,3,6,1,4,1,171,12,39,1,9),_SwJWACVirtualIpAddr_Type())
swJWACVirtualIpAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:swJWACVirtualIpAddr.setStatus(_A)
class _SwJWACQuarantineServerURL_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_SwJWACQuarantineServerURL_Type.__name__=_F
_SwJWACQuarantineServerURL_Object=MibScalar
swJWACQuarantineServerURL=_SwJWACQuarantineServerURL_Object((1,3,6,1,4,1,171,12,39,1,10),_SwJWACQuarantineServerURL_Type())
swJWACQuarantineServerURL.setMaxAccess(_B)
if mibBuilder.loadTexts:swJWACQuarantineServerURL.setStatus(_A)
class _SwJWACSwitchHttpPortNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_SwJWACSwitchHttpPortNumber_Type.__name__=_C
_SwJWACSwitchHttpPortNumber_Object=MibScalar
swJWACSwitchHttpPortNumber=_SwJWACSwitchHttpPortNumber_Object((1,3,6,1,4,1,171,12,39,1,11),_SwJWACSwitchHttpPortNumber_Type())
swJWACSwitchHttpPortNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:swJWACSwitchHttpPortNumber.setStatus(_A)
class _SwJWACSwitchHttpProtocol_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('http',1),('https',2)))
_SwJWACSwitchHttpProtocol_Type.__name__=_C
_SwJWACSwitchHttpProtocol_Object=MibScalar
swJWACSwitchHttpProtocol=_SwJWACSwitchHttpProtocol_Object((1,3,6,1,4,1,171,12,39,1,12),_SwJWACSwitchHttpProtocol_Type())
swJWACSwitchHttpProtocol.setMaxAccess(_B)
if mibBuilder.loadTexts:swJWACSwitchHttpProtocol.setStatus(_A)
class _SwJWACRadiusProtocol_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('local',1),('pap',2),('chap',3),('ms_chap',4),('ms_chapv2',5),('eap_md5',6)))
_SwJWACRadiusProtocol_Type.__name__=_C
_SwJWACRadiusProtocol_Object=MibScalar
swJWACRadiusProtocol=_SwJWACRadiusProtocol_Object((1,3,6,1,4,1,171,12,39,1,13),_SwJWACRadiusProtocol_Type())
swJWACRadiusProtocol.setMaxAccess(_B)
if mibBuilder.loadTexts:swJWACRadiusProtocol.setStatus(_A)
_SwJWACUpdateServerTable_Object=MibTable
swJWACUpdateServerTable=_SwJWACUpdateServerTable_Object((1,3,6,1,4,1,171,12,39,1,14))
if mibBuilder.loadTexts:swJWACUpdateServerTable.setStatus(_I)
_SwJWACUpdateServerEntry_Object=MibTableRow
swJWACUpdateServerEntry=_SwJWACUpdateServerEntry_Object((1,3,6,1,4,1,171,12,39,1,14,1))
swJWACUpdateServerEntry.setIndexNames((0,_E,_M),(0,_E,_N))
if mibBuilder.loadTexts:swJWACUpdateServerEntry.setStatus(_I)
_SwJWACUpdateServerIpAddr_Type=IpAddress
_SwJWACUpdateServerIpAddr_Object=MibTableColumn
swJWACUpdateServerIpAddr=_SwJWACUpdateServerIpAddr_Object((1,3,6,1,4,1,171,12,39,1,14,1,1),_SwJWACUpdateServerIpAddr_Type())
swJWACUpdateServerIpAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:swJWACUpdateServerIpAddr.setStatus(_I)
_SwJWACUpdateServerMask_Type=IpAddress
_SwJWACUpdateServerMask_Object=MibTableColumn
swJWACUpdateServerMask=_SwJWACUpdateServerMask_Object((1,3,6,1,4,1,171,12,39,1,14,1,2),_SwJWACUpdateServerMask_Type())
swJWACUpdateServerMask.setMaxAccess(_D)
if mibBuilder.loadTexts:swJWACUpdateServerMask.setStatus(_I)
_SwJWACUpdateServerStatus_Type=RowStatus
_SwJWACUpdateServerStatus_Object=MibTableColumn
swJWACUpdateServerStatus=_SwJWACUpdateServerStatus_Object((1,3,6,1,4,1,171,12,39,1,14,1,3),_SwJWACUpdateServerStatus_Type())
swJWACUpdateServerStatus.setMaxAccess(_J)
if mibBuilder.loadTexts:swJWACUpdateServerStatus.setStatus(_I)
class _SwJWACAuthenticatePage_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_O,1),(_P,2)))
_SwJWACAuthenticatePage_Type.__name__=_C
_SwJWACAuthenticatePage_Object=MibScalar
swJWACAuthenticatePage=_SwJWACAuthenticatePage_Object((1,3,6,1,4,1,171,12,39,1,15),_SwJWACAuthenticatePage_Type())
swJWACAuthenticatePage.setMaxAccess(_B)
if mibBuilder.loadTexts:swJWACAuthenticatePage.setStatus(_A)
class _SwJWACAuthFailOverState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_SwJWACAuthFailOverState_Type.__name__=_C
_SwJWACAuthFailOverState_Object=MibScalar
swJWACAuthFailOverState=_SwJWACAuthFailOverState_Object((1,3,6,1,4,1,171,12,39,1,16),_SwJWACAuthFailOverState_Type())
swJWACAuthFailOverState.setMaxAccess(_B)
if mibBuilder.loadTexts:swJWACAuthFailOverState.setStatus(_A)
class _SwJWACRadiusAuthorizeState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_SwJWACRadiusAuthorizeState_Type.__name__=_C
_SwJWACRadiusAuthorizeState_Object=MibScalar
swJWACRadiusAuthorizeState=_SwJWACRadiusAuthorizeState_Object((1,3,6,1,4,1,171,12,39,1,17),_SwJWACRadiusAuthorizeState_Type())
swJWACRadiusAuthorizeState.setMaxAccess(_B)
if mibBuilder.loadTexts:swJWACRadiusAuthorizeState.setStatus(_A)
class _SwJWACLocalAuthorizeState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_SwJWACLocalAuthorizeState_Type.__name__=_C
_SwJWACLocalAuthorizeState_Object=MibScalar
swJWACLocalAuthorizeState=_SwJWACLocalAuthorizeState_Object((1,3,6,1,4,1,171,12,39,1,18),_SwJWACLocalAuthorizeState_Type())
swJWACLocalAuthorizeState.setMaxAccess(_B)
if mibBuilder.loadTexts:swJWACLocalAuthorizeState.setStatus(_A)
_SwJWACUpdateSVRTable_Object=MibTable
swJWACUpdateSVRTable=_SwJWACUpdateSVRTable_Object((1,3,6,1,4,1,171,12,39,1,19))
if mibBuilder.loadTexts:swJWACUpdateSVRTable.setStatus(_A)
_SwJWACUpdateSVREntry_Object=MibTableRow
swJWACUpdateSVREntry=_SwJWACUpdateSVREntry_Object((1,3,6,1,4,1,171,12,39,1,19,1))
swJWACUpdateSVREntry.setIndexNames((0,_E,_Q),(0,_E,_R),(0,_E,_S),(0,_E,_T))
if mibBuilder.loadTexts:swJWACUpdateSVREntry.setStatus(_A)
_SwJWACUpdateSVRIpAddr_Type=IpAddress
_SwJWACUpdateSVRIpAddr_Object=MibTableColumn
swJWACUpdateSVRIpAddr=_SwJWACUpdateSVRIpAddr_Object((1,3,6,1,4,1,171,12,39,1,19,1,1),_SwJWACUpdateSVRIpAddr_Type())
swJWACUpdateSVRIpAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:swJWACUpdateSVRIpAddr.setStatus(_A)
_SwJWACUpdateSVRMask_Type=IpAddress
_SwJWACUpdateSVRMask_Object=MibTableColumn
swJWACUpdateSVRMask=_SwJWACUpdateSVRMask_Object((1,3,6,1,4,1,171,12,39,1,19,1,2),_SwJWACUpdateSVRMask_Type())
swJWACUpdateSVRMask.setMaxAccess(_D)
if mibBuilder.loadTexts:swJWACUpdateSVRMask.setStatus(_A)
class _SwJWACUpdateSVRProtocol_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('all',1),('tcp',2),('udp',3)))
_SwJWACUpdateSVRProtocol_Type.__name__=_C
_SwJWACUpdateSVRProtocol_Object=MibTableColumn
swJWACUpdateSVRProtocol=_SwJWACUpdateSVRProtocol_Object((1,3,6,1,4,1,171,12,39,1,19,1,3),_SwJWACUpdateSVRProtocol_Type())
swJWACUpdateSVRProtocol.setMaxAccess(_D)
if mibBuilder.loadTexts:swJWACUpdateSVRProtocol.setStatus(_A)
class _SwJWACUpdateSVRPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SwJWACUpdateSVRPort_Type.__name__=_C
_SwJWACUpdateSVRPort_Object=MibTableColumn
swJWACUpdateSVRPort=_SwJWACUpdateSVRPort_Object((1,3,6,1,4,1,171,12,39,1,19,1,4),_SwJWACUpdateSVRPort_Type())
swJWACUpdateSVRPort.setMaxAccess(_D)
if mibBuilder.loadTexts:swJWACUpdateSVRPort.setStatus(_A)
_SwJWACUpdateSVRStatus_Type=RowStatus
_SwJWACUpdateSVRStatus_Object=MibTableColumn
swJWACUpdateSVRStatus=_SwJWACUpdateSVRStatus_Object((1,3,6,1,4,1,171,12,39,1,19,1,5),_SwJWACUpdateSVRStatus_Type())
swJWACUpdateSVRStatus.setMaxAccess(_J)
if mibBuilder.loadTexts:swJWACUpdateSVRStatus.setStatus(_A)
class _SwJWACUpdateSVRState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),('inactive',2)))
_SwJWACUpdateSVRState_Type.__name__=_C
_SwJWACUpdateSVRState_Object=MibTableColumn
swJWACUpdateSVRState=_SwJWACUpdateSVRState_Object((1,3,6,1,4,1,171,12,39,1,19,1,6),_SwJWACUpdateSVRState_Type())
swJWACUpdateSVRState.setMaxAccess(_D)
if mibBuilder.loadTexts:swJWACUpdateSVRState.setStatus(_A)
class _SwJWACVirtualIpURL_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_SwJWACVirtualIpURL_Type.__name__=_F
_SwJWACVirtualIpURL_Object=MibScalar
swJWACVirtualIpURL=_SwJWACVirtualIpURL_Object((1,3,6,1,4,1,171,12,39,1,20),_SwJWACVirtualIpURL_Type())
swJWACVirtualIpURL.setMaxAccess(_B)
if mibBuilder.loadTexts:swJWACVirtualIpURL.setStatus(_A)
_SwJWACInfo_ObjectIdentity=ObjectIdentity
swJWACInfo=_SwJWACInfo_ObjectIdentity((1,3,6,1,4,1,171,12,39,2))
_SwJWACPortMgmt_ObjectIdentity=ObjectIdentity
swJWACPortMgmt=_SwJWACPortMgmt_ObjectIdentity((1,3,6,1,4,1,171,12,39,3))
_SwJWACPortTable_Object=MibTable
swJWACPortTable=_SwJWACPortTable_Object((1,3,6,1,4,1,171,12,39,3,1))
if mibBuilder.loadTexts:swJWACPortTable.setStatus(_A)
_SwJWACPortEntry_Object=MibTableRow
swJWACPortEntry=_SwJWACPortEntry_Object((1,3,6,1,4,1,171,12,39,3,1,1))
swJWACPortEntry.setIndexNames((0,_E,_U))
if mibBuilder.loadTexts:swJWACPortEntry.setStatus(_A)
_SwJWACPortIndex_Type=Integer32
_SwJWACPortIndex_Object=MibTableColumn
swJWACPortIndex=_SwJWACPortIndex_Object((1,3,6,1,4,1,171,12,39,3,1,1,1),_SwJWACPortIndex_Type())
swJWACPortIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:swJWACPortIndex.setStatus(_A)
class _SwJWACPortState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_SwJWACPortState_Type.__name__=_C
_SwJWACPortState_Object=MibTableColumn
swJWACPortState=_SwJWACPortState_Object((1,3,6,1,4,1,171,12,39,3,1,1,2),_SwJWACPortState_Type())
swJWACPortState.setMaxAccess(_B)
if mibBuilder.loadTexts:swJWACPortState.setStatus(_A)
_SwJWACPortMaxAuthHost_Type=Integer32
_SwJWACPortMaxAuthHost_Object=MibTableColumn
swJWACPortMaxAuthHost=_SwJWACPortMaxAuthHost_Object((1,3,6,1,4,1,171,12,39,3,1,1,3),_SwJWACPortMaxAuthHost_Type())
swJWACPortMaxAuthHost.setMaxAccess(_B)
if mibBuilder.loadTexts:swJWACPortMaxAuthHost.setStatus(_A)
class _SwJWACPortAgeingTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1440))
_SwJWACPortAgeingTime_Type.__name__=_C
_SwJWACPortAgeingTime_Object=MibTableColumn
swJWACPortAgeingTime=_SwJWACPortAgeingTime_Object((1,3,6,1,4,1,171,12,39,3,1,1,4),_SwJWACPortAgeingTime_Type())
swJWACPortAgeingTime.setMaxAccess(_B)
if mibBuilder.loadTexts:swJWACPortAgeingTime.setStatus(_A)
class _SwJWACPortIdleTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1440))
_SwJWACPortIdleTime_Type.__name__=_C
_SwJWACPortIdleTime_Object=MibTableColumn
swJWACPortIdleTime=_SwJWACPortIdleTime_Object((1,3,6,1,4,1,171,12,39,3,1,1,5),_SwJWACPortIdleTime_Type())
swJWACPortIdleTime.setMaxAccess(_B)
if mibBuilder.loadTexts:swJWACPortIdleTime.setStatus(_A)
class _SwJWACPortBlockTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,300))
_SwJWACPortBlockTime_Type.__name__=_C
_SwJWACPortBlockTime_Object=MibTableColumn
swJWACPortBlockTime=_SwJWACPortBlockTime_Object((1,3,6,1,4,1,171,12,39,3,1,1,6),_SwJWACPortBlockTime_Type())
swJWACPortBlockTime.setMaxAccess(_B)
if mibBuilder.loadTexts:swJWACPortBlockTime.setStatus(_A)
class _SwJWACPortAuthMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('hostbased',1),('portbased',2)))
_SwJWACPortAuthMode_Type.__name__=_C
_SwJWACPortAuthMode_Object=MibTableColumn
swJWACPortAuthMode=_SwJWACPortAuthMode_Object((1,3,6,1,4,1,171,12,39,3,1,1,7),_SwJWACPortAuthMode_Type())
swJWACPortAuthMode.setMaxAccess(_B)
if mibBuilder.loadTexts:swJWACPortAuthMode.setStatus(_A)
_SwJWACMgmt_ObjectIdentity=ObjectIdentity
swJWACMgmt=_SwJWACMgmt_ObjectIdentity((1,3,6,1,4,1,171,12,39,4))
_SwJWACHostTable_Object=MibTable
swJWACHostTable=_SwJWACHostTable_Object((1,3,6,1,4,1,171,12,39,4,1))
if mibBuilder.loadTexts:swJWACHostTable.setStatus(_A)
_SwJWACHostEntry_Object=MibTableRow
swJWACHostEntry=_SwJWACHostEntry_Object((1,3,6,1,4,1,171,12,39,4,1,1))
swJWACHostEntry.setIndexNames((0,_E,_V),(0,_E,_W),(0,_E,_X))
if mibBuilder.loadTexts:swJWACHostEntry.setStatus(_A)
_SwJWACHostPort_Type=Integer32
_SwJWACHostPort_Object=MibTableColumn
swJWACHostPort=_SwJWACHostPort_Object((1,3,6,1,4,1,171,12,39,4,1,1,1),_SwJWACHostPort_Type())
swJWACHostPort.setMaxAccess(_D)
if mibBuilder.loadTexts:swJWACHostPort.setStatus(_A)
class _SwJWACHostAuthStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_Y,1),(_Z,2),(_a,3)))
_SwJWACHostAuthStatus_Type.__name__=_C
_SwJWACHostAuthStatus_Object=MibTableColumn
swJWACHostAuthStatus=_SwJWACHostAuthStatus_Object((1,3,6,1,4,1,171,12,39,4,1,1,2),_SwJWACHostAuthStatus_Type())
swJWACHostAuthStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:swJWACHostAuthStatus.setStatus(_A)
_SwJWACHostMACAddr_Type=MacAddress
_SwJWACHostMACAddr_Object=MibTableColumn
swJWACHostMACAddr=_SwJWACHostMACAddr_Object((1,3,6,1,4,1,171,12,39,4,1,1,3),_SwJWACHostMACAddr_Type())
swJWACHostMACAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:swJWACHostMACAddr.setStatus(_A)
_SwJWACHostVID_Type=VlanId
_SwJWACHostVID_Object=MibTableColumn
swJWACHostVID=_SwJWACHostVID_Object((1,3,6,1,4,1,171,12,39,4,1,1,4),_SwJWACHostVID_Type())
swJWACHostVID.setMaxAccess(_D)
if mibBuilder.loadTexts:swJWACHostVID.setStatus(_A)
_SwJWACHostRemainAgeTime_Type=Integer32
_SwJWACHostRemainAgeTime_Object=MibTableColumn
swJWACHostRemainAgeTime=_SwJWACHostRemainAgeTime_Object((1,3,6,1,4,1,171,12,39,4,1,1,5),_SwJWACHostRemainAgeTime_Type())
swJWACHostRemainAgeTime.setMaxAccess(_D)
if mibBuilder.loadTexts:swJWACHostRemainAgeTime.setStatus(_A)
_SwJWACHostIdleTime_Type=Integer32
_SwJWACHostIdleTime_Object=MibTableColumn
swJWACHostIdleTime=_SwJWACHostIdleTime_Object((1,3,6,1,4,1,171,12,39,4,1,1,6),_SwJWACHostIdleTime_Type())
swJWACHostIdleTime.setMaxAccess(_D)
if mibBuilder.loadTexts:swJWACHostIdleTime.setStatus(_A)
_SwJWACHostBlockTime_Type=Integer32
_SwJWACHostBlockTime_Object=MibTableColumn
swJWACHostBlockTime=_SwJWACHostBlockTime_Object((1,3,6,1,4,1,171,12,39,4,1,1,7),_SwJWACHostBlockTime_Type())
swJWACHostBlockTime.setMaxAccess(_D)
if mibBuilder.loadTexts:swJWACHostBlockTime.setStatus(_A)
class _SwJWACHostStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_b,2)))
_SwJWACHostStatus_Type.__name__=_C
_SwJWACHostStatus_Object=MibTableColumn
swJWACHostStatus=_SwJWACHostStatus_Object((1,3,6,1,4,1,171,12,39,4,1,1,8),_SwJWACHostStatus_Type())
swJWACHostStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:swJWACHostStatus.setStatus(_A)
_SwJWACHostPriority_Type=Integer32
_SwJWACHostPriority_Object=MibTableColumn
swJWACHostPriority=_SwJWACHostPriority_Object((1,3,6,1,4,1,171,12,39,4,1,1,9),_SwJWACHostPriority_Type())
swJWACHostPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:swJWACHostPriority.setStatus(_A)
_SwJWACHostUserName_Type=DisplayString
_SwJWACHostUserName_Object=MibTableColumn
swJWACHostUserName=_SwJWACHostUserName_Object((1,3,6,1,4,1,171,12,39,4,1,1,10),_SwJWACHostUserName_Type())
swJWACHostUserName.setMaxAccess(_D)
if mibBuilder.loadTexts:swJWACHostUserName.setStatus(_A)
_SwJWACHostIP_Type=IpAddress
_SwJWACHostIP_Object=MibTableColumn
swJWACHostIP=_SwJWACHostIP_Object((1,3,6,1,4,1,171,12,39,4,1,1,11),_SwJWACHostIP_Type())
swJWACHostIP.setMaxAccess(_D)
if mibBuilder.loadTexts:swJWACHostIP.setStatus(_A)
_SwJWACPageElementTable_Object=MibTable
swJWACPageElementTable=_SwJWACPageElementTable_Object((1,3,6,1,4,1,171,12,39,4,2))
if mibBuilder.loadTexts:swJWACPageElementTable.setStatus(_A)
_SwJWACPageElementEntry_Object=MibTableRow
swJWACPageElementEntry=_SwJWACPageElementEntry_Object((1,3,6,1,4,1,171,12,39,4,2,1))
swJWACPageElementEntry.setIndexNames((0,_E,_c))
if mibBuilder.loadTexts:swJWACPageElementEntry.setStatus(_A)
class _SwJWACPageElementPage_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_O,1),(_P,2)))
_SwJWACPageElementPage_Type.__name__=_C
_SwJWACPageElementPage_Object=MibTableColumn
swJWACPageElementPage=_SwJWACPageElementPage_Object((1,3,6,1,4,1,171,12,39,4,2,1,1),_SwJWACPageElementPage_Type())
swJWACPageElementPage.setMaxAccess(_D)
if mibBuilder.loadTexts:swJWACPageElementPage.setStatus(_A)
class _SwJWACPageElementPageTitle_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_SwJWACPageElementPageTitle_Type.__name__=_F
_SwJWACPageElementPageTitle_Object=MibTableColumn
swJWACPageElementPageTitle=_SwJWACPageElementPageTitle_Object((1,3,6,1,4,1,171,12,39,4,2,1,2),_SwJWACPageElementPageTitle_Type())
swJWACPageElementPageTitle.setMaxAccess(_B)
if mibBuilder.loadTexts:swJWACPageElementPageTitle.setStatus(_A)
class _SwJWACPageElementLoginWindowTitle_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_SwJWACPageElementLoginWindowTitle_Type.__name__=_F
_SwJWACPageElementLoginWindowTitle_Object=MibTableColumn
swJWACPageElementLoginWindowTitle=_SwJWACPageElementLoginWindowTitle_Object((1,3,6,1,4,1,171,12,39,4,2,1,3),_SwJWACPageElementLoginWindowTitle_Type())
swJWACPageElementLoginWindowTitle.setMaxAccess(_B)
if mibBuilder.loadTexts:swJWACPageElementLoginWindowTitle.setStatus(_A)
class _SwJWACPageElementUserName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_SwJWACPageElementUserName_Type.__name__=_F
_SwJWACPageElementUserName_Object=MibTableColumn
swJWACPageElementUserName=_SwJWACPageElementUserName_Object((1,3,6,1,4,1,171,12,39,4,2,1,4),_SwJWACPageElementUserName_Type())
swJWACPageElementUserName.setMaxAccess(_B)
if mibBuilder.loadTexts:swJWACPageElementUserName.setStatus(_A)
class _SwJWACPageElementPassWord_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_SwJWACPageElementPassWord_Type.__name__=_F
_SwJWACPageElementPassWord_Object=MibTableColumn
swJWACPageElementPassWord=_SwJWACPageElementPassWord_Object((1,3,6,1,4,1,171,12,39,4,2,1,5),_SwJWACPageElementPassWord_Type())
swJWACPageElementPassWord.setMaxAccess(_B)
if mibBuilder.loadTexts:swJWACPageElementPassWord.setStatus(_A)
class _SwJWACPageElementLogoutWindowTitle_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_SwJWACPageElementLogoutWindowTitle_Type.__name__=_F
_SwJWACPageElementLogoutWindowTitle_Object=MibTableColumn
swJWACPageElementLogoutWindowTitle=_SwJWACPageElementLogoutWindowTitle_Object((1,3,6,1,4,1,171,12,39,4,2,1,6),_SwJWACPageElementLogoutWindowTitle_Type())
swJWACPageElementLogoutWindowTitle.setMaxAccess(_B)
if mibBuilder.loadTexts:swJWACPageElementLogoutWindowTitle.setStatus(_A)
class _SwJWACPageElementNotificationLine1_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_SwJWACPageElementNotificationLine1_Type.__name__=_F
_SwJWACPageElementNotificationLine1_Object=MibTableColumn
swJWACPageElementNotificationLine1=_SwJWACPageElementNotificationLine1_Object((1,3,6,1,4,1,171,12,39,4,2,1,7),_SwJWACPageElementNotificationLine1_Type())
swJWACPageElementNotificationLine1.setMaxAccess(_B)
if mibBuilder.loadTexts:swJWACPageElementNotificationLine1.setStatus(_A)
class _SwJWACPageElementNotificationLine2_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_SwJWACPageElementNotificationLine2_Type.__name__=_F
_SwJWACPageElementNotificationLine2_Object=MibTableColumn
swJWACPageElementNotificationLine2=_SwJWACPageElementNotificationLine2_Object((1,3,6,1,4,1,171,12,39,4,2,1,8),_SwJWACPageElementNotificationLine2_Type())
swJWACPageElementNotificationLine2.setMaxAccess(_B)
if mibBuilder.loadTexts:swJWACPageElementNotificationLine2.setStatus(_A)
class _SwJWACPageElementNotificationLine3_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_SwJWACPageElementNotificationLine3_Type.__name__=_F
_SwJWACPageElementNotificationLine3_Object=MibTableColumn
swJWACPageElementNotificationLine3=_SwJWACPageElementNotificationLine3_Object((1,3,6,1,4,1,171,12,39,4,2,1,9),_SwJWACPageElementNotificationLine3_Type())
swJWACPageElementNotificationLine3.setMaxAccess(_B)
if mibBuilder.loadTexts:swJWACPageElementNotificationLine3.setStatus(_A)
class _SwJWACPageElementNotificationLine4_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_SwJWACPageElementNotificationLine4_Type.__name__=_F
_SwJWACPageElementNotificationLine4_Object=MibTableColumn
swJWACPageElementNotificationLine4=_SwJWACPageElementNotificationLine4_Object((1,3,6,1,4,1,171,12,39,4,2,1,10),_SwJWACPageElementNotificationLine4_Type())
swJWACPageElementNotificationLine4.setMaxAccess(_B)
if mibBuilder.loadTexts:swJWACPageElementNotificationLine4.setStatus(_A)
class _SwJWACPageElementNotificationLine5_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_SwJWACPageElementNotificationLine5_Type.__name__=_F
_SwJWACPageElementNotificationLine5_Object=MibTableColumn
swJWACPageElementNotificationLine5=_SwJWACPageElementNotificationLine5_Object((1,3,6,1,4,1,171,12,39,4,2,1,11),_SwJWACPageElementNotificationLine5_Type())
swJWACPageElementNotificationLine5.setMaxAccess(_B)
if mibBuilder.loadTexts:swJWACPageElementNotificationLine5.setStatus(_A)
_SwJWACWebAuthUserTable_Object=MibTable
swJWACWebAuthUserTable=_SwJWACWebAuthUserTable_Object((1,3,6,1,4,1,171,12,39,4,3))
if mibBuilder.loadTexts:swJWACWebAuthUserTable.setStatus(_A)
_SwJWACWebAuthUserEntry_Object=MibTableRow
swJWACWebAuthUserEntry=_SwJWACWebAuthUserEntry_Object((1,3,6,1,4,1,171,12,39,4,3,1))
swJWACWebAuthUserEntry.setIndexNames((0,_E,_d))
if mibBuilder.loadTexts:swJWACWebAuthUserEntry.setStatus(_A)
class _SwJWACWebAuthUserNameIndex_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,15))
_SwJWACWebAuthUserNameIndex_Type.__name__=_F
_SwJWACWebAuthUserNameIndex_Object=MibTableColumn
swJWACWebAuthUserNameIndex=_SwJWACWebAuthUserNameIndex_Object((1,3,6,1,4,1,171,12,39,4,3,1,1),_SwJWACWebAuthUserNameIndex_Type())
swJWACWebAuthUserNameIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:swJWACWebAuthUserNameIndex.setStatus(_A)
class _SwJWACWebAuthUserPWD_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,15))
_SwJWACWebAuthUserPWD_Type.__name__=_F
_SwJWACWebAuthUserPWD_Object=MibTableColumn
swJWACWebAuthUserPWD=_SwJWACWebAuthUserPWD_Object((1,3,6,1,4,1,171,12,39,4,3,1,2),_SwJWACWebAuthUserPWD_Type())
swJWACWebAuthUserPWD.setMaxAccess(_J)
if mibBuilder.loadTexts:swJWACWebAuthUserPWD.setStatus(_A)
_SwJWACWebAuthUserVID_Type=VlanId
_SwJWACWebAuthUserVID_Object=MibTableColumn
swJWACWebAuthUserVID=_SwJWACWebAuthUserVID_Object((1,3,6,1,4,1,171,12,39,4,3,1,3),_SwJWACWebAuthUserVID_Type())
swJWACWebAuthUserVID.setMaxAccess(_J)
if mibBuilder.loadTexts:swJWACWebAuthUserVID.setStatus(_A)
_SwJWACWebAuthUserStatus_Type=RowStatus
_SwJWACWebAuthUserStatus_Object=MibTableColumn
swJWACWebAuthUserStatus=_SwJWACWebAuthUserStatus_Object((1,3,6,1,4,1,171,12,39,4,3,1,4),_SwJWACWebAuthUserStatus_Type())
swJWACWebAuthUserStatus.setMaxAccess(_J)
if mibBuilder.loadTexts:swJWACWebAuthUserStatus.setStatus(_A)
_SwJWACAuthStateTable_Object=MibTable
swJWACAuthStateTable=_SwJWACAuthStateTable_Object((1,3,6,1,4,1,171,12,39,4,4))
if mibBuilder.loadTexts:swJWACAuthStateTable.setStatus(_A)
_SwJWACAuthStateEntry_Object=MibTableRow
swJWACAuthStateEntry=_SwJWACAuthStateEntry_Object((1,3,6,1,4,1,171,12,39,4,4,1))
swJWACAuthStateEntry.setIndexNames((0,_E,_e),(0,_E,_f),(0,_E,_g))
if mibBuilder.loadTexts:swJWACAuthStateEntry.setStatus(_A)
_SwJWACAuthStatePort_Type=Integer32
_SwJWACAuthStatePort_Object=MibTableColumn
swJWACAuthStatePort=_SwJWACAuthStatePort_Object((1,3,6,1,4,1,171,12,39,4,4,1,1),_SwJWACAuthStatePort_Type())
swJWACAuthStatePort.setMaxAccess(_L)
if mibBuilder.loadTexts:swJWACAuthStatePort.setStatus(_A)
_SwJWACAuthStateOriginalVid_Type=VlanId
_SwJWACAuthStateOriginalVid_Object=MibTableColumn
swJWACAuthStateOriginalVid=_SwJWACAuthStateOriginalVid_Object((1,3,6,1,4,1,171,12,39,4,4,1,2),_SwJWACAuthStateOriginalVid_Type())
swJWACAuthStateOriginalVid.setMaxAccess(_L)
if mibBuilder.loadTexts:swJWACAuthStateOriginalVid.setStatus(_A)
_SwJWACAuthStateMACAddr_Type=MacAddress
_SwJWACAuthStateMACAddr_Object=MibTableColumn
swJWACAuthStateMACAddr=_SwJWACAuthStateMACAddr_Object((1,3,6,1,4,1,171,12,39,4,4,1,3),_SwJWACAuthStateMACAddr_Type())
swJWACAuthStateMACAddr.setMaxAccess(_L)
if mibBuilder.loadTexts:swJWACAuthStateMACAddr.setStatus(_A)
class _SwJWACAuthStateAuthStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_Y,1),(_Z,2),(_a,3)))
_SwJWACAuthStateAuthStatus_Type.__name__=_C
_SwJWACAuthStateAuthStatus_Object=MibTableColumn
swJWACAuthStateAuthStatus=_SwJWACAuthStateAuthStatus_Object((1,3,6,1,4,1,171,12,39,4,4,1,5),_SwJWACAuthStateAuthStatus_Type())
swJWACAuthStateAuthStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:swJWACAuthStateAuthStatus.setStatus(_A)
_SwJWACAuthStateAssignVid_Type=VlanId
_SwJWACAuthStateAssignVid_Object=MibTableColumn
swJWACAuthStateAssignVid=_SwJWACAuthStateAssignVid_Object((1,3,6,1,4,1,171,12,39,4,4,1,7),_SwJWACAuthStateAssignVid_Type())
swJWACAuthStateAssignVid.setMaxAccess(_D)
if mibBuilder.loadTexts:swJWACAuthStateAssignVid.setStatus(_A)
_SwJWACAuthStateAssignPriority_Type=Integer32
_SwJWACAuthStateAssignPriority_Object=MibTableColumn
swJWACAuthStateAssignPriority=_SwJWACAuthStateAssignPriority_Object((1,3,6,1,4,1,171,12,39,4,4,1,8),_SwJWACAuthStateAssignPriority_Type())
swJWACAuthStateAssignPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:swJWACAuthStateAssignPriority.setStatus(_A)
_SwJWACAuthStateRemainTime_Type=Integer32
_SwJWACAuthStateRemainTime_Object=MibTableColumn
swJWACAuthStateRemainTime=_SwJWACAuthStateRemainTime_Object((1,3,6,1,4,1,171,12,39,4,4,1,12),_SwJWACAuthStateRemainTime_Type())
swJWACAuthStateRemainTime.setMaxAccess(_D)
if mibBuilder.loadTexts:swJWACAuthStateRemainTime.setStatus(_A)
if mibBuilder.loadTexts:swJWACAuthStateRemainTime.setUnits('minutes/seconds')
_SwJWACAuthStateIdleTime_Type=Integer32
_SwJWACAuthStateIdleTime_Object=MibTableColumn
swJWACAuthStateIdleTime=_SwJWACAuthStateIdleTime_Object((1,3,6,1,4,1,171,12,39,4,4,1,14),_SwJWACAuthStateIdleTime_Type())
swJWACAuthStateIdleTime.setMaxAccess(_D)
if mibBuilder.loadTexts:swJWACAuthStateIdleTime.setStatus(_A)
if mibBuilder.loadTexts:swJWACAuthStateIdleTime.setUnits('seconds')
_SwJWACAuthStateUserName_Type=DisplayString
_SwJWACAuthStateUserName_Object=MibTableColumn
swJWACAuthStateUserName=_SwJWACAuthStateUserName_Object((1,3,6,1,4,1,171,12,39,4,4,1,18),_SwJWACAuthStateUserName_Type())
swJWACAuthStateUserName.setMaxAccess(_D)
if mibBuilder.loadTexts:swJWACAuthStateUserName.setStatus(_A)
_SwJWACAuthStateIP_Type=IpAddress
_SwJWACAuthStateIP_Object=MibTableColumn
swJWACAuthStateIP=_SwJWACAuthStateIP_Object((1,3,6,1,4,1,171,12,39,4,4,1,20),_SwJWACAuthStateIP_Type())
swJWACAuthStateIP.setMaxAccess(_D)
if mibBuilder.loadTexts:swJWACAuthStateIP.setStatus(_A)
class _SwJWACAuthStateDelAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_b,2)))
_SwJWACAuthStateDelAction_Type.__name__=_C
_SwJWACAuthStateDelAction_Object=MibTableColumn
swJWACAuthStateDelAction=_SwJWACAuthStateDelAction_Object((1,3,6,1,4,1,171,12,39,4,4,1,30),_SwJWACAuthStateDelAction_Type())
swJWACAuthStateDelAction.setMaxAccess(_B)
if mibBuilder.loadTexts:swJWACAuthStateDelAction.setStatus(_A)
_SwJWACNotify_ObjectIdentity=ObjectIdentity
swJWACNotify=_SwJWACNotify_ObjectIdentity((1,3,6,1,4,1,171,12,39,5))
mibBuilder.exportSymbols(_E,**{'VlanId':VlanId,'swJWACMIB':swJWACMIB,'swJWACCtrl':swJWACCtrl,'swJWACState':swJWACState,'swJWACRedirectState':swJWACRedirectState,'swJWACForcibleLogoutState':swJWACForcibleLogoutState,'swJWACUDPFilteringState':swJWACUDPFilteringState,'swJWACQuarantineServerMonitorState':swJWACQuarantineServerMonitorState,'swJWACQuarantineServerErrorTimeOut':swJWACQuarantineServerErrorTimeOut,'swJWACRedirectDestination':swJWACRedirectDestination,'swJWACRedirectDelayTime':swJWACRedirectDelayTime,'swJWACVirtualIpAddr':swJWACVirtualIpAddr,'swJWACQuarantineServerURL':swJWACQuarantineServerURL,'swJWACSwitchHttpPortNumber':swJWACSwitchHttpPortNumber,'swJWACSwitchHttpProtocol':swJWACSwitchHttpProtocol,'swJWACRadiusProtocol':swJWACRadiusProtocol,'swJWACUpdateServerTable':swJWACUpdateServerTable,'swJWACUpdateServerEntry':swJWACUpdateServerEntry,_M:swJWACUpdateServerIpAddr,_N:swJWACUpdateServerMask,'swJWACUpdateServerStatus':swJWACUpdateServerStatus,'swJWACAuthenticatePage':swJWACAuthenticatePage,'swJWACAuthFailOverState':swJWACAuthFailOverState,'swJWACRadiusAuthorizeState':swJWACRadiusAuthorizeState,'swJWACLocalAuthorizeState':swJWACLocalAuthorizeState,'swJWACUpdateSVRTable':swJWACUpdateSVRTable,'swJWACUpdateSVREntry':swJWACUpdateSVREntry,_Q:swJWACUpdateSVRIpAddr,_R:swJWACUpdateSVRMask,_S:swJWACUpdateSVRProtocol,_T:swJWACUpdateSVRPort,'swJWACUpdateSVRStatus':swJWACUpdateSVRStatus,'swJWACUpdateSVRState':swJWACUpdateSVRState,'swJWACVirtualIpURL':swJWACVirtualIpURL,'swJWACInfo':swJWACInfo,'swJWACPortMgmt':swJWACPortMgmt,'swJWACPortTable':swJWACPortTable,'swJWACPortEntry':swJWACPortEntry,_U:swJWACPortIndex,'swJWACPortState':swJWACPortState,'swJWACPortMaxAuthHost':swJWACPortMaxAuthHost,'swJWACPortAgeingTime':swJWACPortAgeingTime,'swJWACPortIdleTime':swJWACPortIdleTime,'swJWACPortBlockTime':swJWACPortBlockTime,'swJWACPortAuthMode':swJWACPortAuthMode,'swJWACMgmt':swJWACMgmt,'swJWACHostTable':swJWACHostTable,'swJWACHostEntry':swJWACHostEntry,_V:swJWACHostPort,_W:swJWACHostAuthStatus,_X:swJWACHostMACAddr,'swJWACHostVID':swJWACHostVID,'swJWACHostRemainAgeTime':swJWACHostRemainAgeTime,'swJWACHostIdleTime':swJWACHostIdleTime,'swJWACHostBlockTime':swJWACHostBlockTime,'swJWACHostStatus':swJWACHostStatus,'swJWACHostPriority':swJWACHostPriority,'swJWACHostUserName':swJWACHostUserName,'swJWACHostIP':swJWACHostIP,'swJWACPageElementTable':swJWACPageElementTable,'swJWACPageElementEntry':swJWACPageElementEntry,_c:swJWACPageElementPage,'swJWACPageElementPageTitle':swJWACPageElementPageTitle,'swJWACPageElementLoginWindowTitle':swJWACPageElementLoginWindowTitle,'swJWACPageElementUserName':swJWACPageElementUserName,'swJWACPageElementPassWord':swJWACPageElementPassWord,'swJWACPageElementLogoutWindowTitle':swJWACPageElementLogoutWindowTitle,'swJWACPageElementNotificationLine1':swJWACPageElementNotificationLine1,'swJWACPageElementNotificationLine2':swJWACPageElementNotificationLine2,'swJWACPageElementNotificationLine3':swJWACPageElementNotificationLine3,'swJWACPageElementNotificationLine4':swJWACPageElementNotificationLine4,'swJWACPageElementNotificationLine5':swJWACPageElementNotificationLine5,'swJWACWebAuthUserTable':swJWACWebAuthUserTable,'swJWACWebAuthUserEntry':swJWACWebAuthUserEntry,_d:swJWACWebAuthUserNameIndex,'swJWACWebAuthUserPWD':swJWACWebAuthUserPWD,'swJWACWebAuthUserVID':swJWACWebAuthUserVID,'swJWACWebAuthUserStatus':swJWACWebAuthUserStatus,'swJWACAuthStateTable':swJWACAuthStateTable,'swJWACAuthStateEntry':swJWACAuthStateEntry,_e:swJWACAuthStatePort,_f:swJWACAuthStateOriginalVid,_g:swJWACAuthStateMACAddr,'swJWACAuthStateAuthStatus':swJWACAuthStateAuthStatus,'swJWACAuthStateAssignVid':swJWACAuthStateAssignVid,'swJWACAuthStateAssignPriority':swJWACAuthStateAssignPriority,'swJWACAuthStateRemainTime':swJWACAuthStateRemainTime,'swJWACAuthStateIdleTime':swJWACAuthStateIdleTime,'swJWACAuthStateUserName':swJWACAuthStateUserName,'swJWACAuthStateIP':swJWACAuthStateIP,'swJWACAuthStateDelAction':swJWACAuthStateDelAction,'swJWACNotify':swJWACNotify})