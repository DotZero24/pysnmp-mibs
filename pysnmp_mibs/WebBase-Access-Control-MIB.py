_X='swWebAuthUserNameIndex'
_W='swWebAuthPortIndex'
_V='swWACAuthStateMACAddr'
_U='swWACAuthStateOriginalVid'
_T='swWACAuthStatePort'
_S='delete'
_R='active'
_Q='blocked'
_P='authenticating'
_O='swWACAuthInfoMACAddr'
_N='swWACAuthInfoAuthStatus'
_M='swWACAuthInfoPort'
_L='authenticated'
_K='read-create'
_J='other'
_I='enabled'
_H='disabled'
_G='obsolete'
_F='WebBase-Access-Control-MIB'
_E='DisplayString'
_D='read-only'
_C='Integer32'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dlink_common_mgmt,=mibBuilder.importSymbols('DLINK-ID-REC-MIB','dlink-common-mgmt')
Ipv6Address,=mibBuilder.importSymbols('IPV6-TC','Ipv6Address')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_E,'MacAddress','PhysAddress','RowStatus','TextualConvention')
swWACMIB=ModuleIdentity((1,3,6,1,4,1,171,12,27))
class VlanId(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_SwWACCtrl_ObjectIdentity=ObjectIdentity
swWACCtrl=_SwWACCtrl_ObjectIdentity((1,3,6,1,4,1,171,12,27,1))
class _SwWebAuthAdminState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_J,1),(_H,2),(_I,3)))
_SwWebAuthAdminState_Type.__name__=_C
_SwWebAuthAdminState_Object=MibScalar
swWebAuthAdminState=_SwWebAuthAdminState_Object((1,3,6,1,4,1,171,12,27,1,1),_SwWebAuthAdminState_Type())
swWebAuthAdminState.setMaxAccess(_B)
if mibBuilder.loadTexts:swWebAuthAdminState.setStatus(_A)
class _SwWebAuthMethod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('local',1),('radius',2)))
_SwWebAuthMethod_Type.__name__=_C
_SwWebAuthMethod_Object=MibScalar
swWebAuthMethod=_SwWebAuthMethod_Object((1,3,6,1,4,1,171,12,27,1,2),_SwWebAuthMethod_Type())
swWebAuthMethod.setMaxAccess(_B)
if mibBuilder.loadTexts:swWebAuthMethod.setStatus(_A)
class _SwWebAuthVlanName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_SwWebAuthVlanName_Type.__name__=_E
_SwWebAuthVlanName_Object=MibScalar
swWebAuthVlanName=_SwWebAuthVlanName_Object((1,3,6,1,4,1,171,12,27,1,3),_SwWebAuthVlanName_Type())
swWebAuthVlanName.setMaxAccess(_B)
if mibBuilder.loadTexts:swWebAuthVlanName.setStatus(_G)
class _SwWebAuthAllPortstate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_J,1),(_H,2),(_I,3)))
_SwWebAuthAllPortstate_Type.__name__=_C
_SwWebAuthAllPortstate_Object=MibScalar
swWebAuthAllPortstate=_SwWebAuthAllPortstate_Object((1,3,6,1,4,1,171,12,27,1,4),_SwWebAuthAllPortstate_Type())
swWebAuthAllPortstate.setMaxAccess(_B)
if mibBuilder.loadTexts:swWebAuthAllPortstate.setStatus(_G)
class _SwWebAuthDefaultredirpath_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_SwWebAuthDefaultredirpath_Type.__name__=_E
_SwWebAuthDefaultredirpath_Object=MibScalar
swWebAuthDefaultredirpath=_SwWebAuthDefaultredirpath_Object((1,3,6,1,4,1,171,12,27,1,5),_SwWebAuthDefaultredirpath_Type())
swWebAuthDefaultredirpath.setMaxAccess(_B)
if mibBuilder.loadTexts:swWebAuthDefaultredirpath.setStatus(_A)
class _SwWebAuthLogouttimer_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1440))
_SwWebAuthLogouttimer_Type.__name__=_C
_SwWebAuthLogouttimer_Object=MibScalar
swWebAuthLogouttimer=_SwWebAuthLogouttimer_Object((1,3,6,1,4,1,171,12,27,1,6),_SwWebAuthLogouttimer_Type())
swWebAuthLogouttimer.setMaxAccess(_B)
if mibBuilder.loadTexts:swWebAuthLogouttimer.setStatus(_G)
_SwWACVirtualIpAddr_Type=IpAddress
_SwWACVirtualIpAddr_Object=MibScalar
swWACVirtualIpAddr=_SwWACVirtualIpAddr_Object((1,3,6,1,4,1,171,12,27,1,7),_SwWACVirtualIpAddr_Type())
swWACVirtualIpAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:swWACVirtualIpAddr.setStatus(_A)
class _SwWACSwitchHttpProtocol_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('http',1),('https',2)))
_SwWACSwitchHttpProtocol_Type.__name__=_C
_SwWACSwitchHttpProtocol_Object=MibScalar
swWACSwitchHttpProtocol=_SwWACSwitchHttpProtocol_Object((1,3,6,1,4,1,171,12,27,1,8),_SwWACSwitchHttpProtocol_Type())
swWACSwitchHttpProtocol.setMaxAccess(_B)
if mibBuilder.loadTexts:swWACSwitchHttpProtocol.setStatus(_A)
class _SwWACSwitchHttpPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_SwWACSwitchHttpPort_Type.__name__=_C
_SwWACSwitchHttpPort_Object=MibScalar
swWACSwitchHttpPort=_SwWACSwitchHttpPort_Object((1,3,6,1,4,1,171,12,27,1,9),_SwWACSwitchHttpPort_Type())
swWACSwitchHttpPort.setMaxAccess(_B)
if mibBuilder.loadTexts:swWACSwitchHttpPort.setStatus(_A)
class _SwWACAuthFailOverState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_H,2)))
_SwWACAuthFailOverState_Type.__name__=_C
_SwWACAuthFailOverState_Object=MibScalar
swWACAuthFailOverState=_SwWACAuthFailOverState_Object((1,3,6,1,4,1,171,12,27,1,10),_SwWACAuthFailOverState_Type())
swWACAuthFailOverState.setMaxAccess(_B)
if mibBuilder.loadTexts:swWACAuthFailOverState.setStatus(_A)
class _SwWACRadiusAuthorizationState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_H,2)))
_SwWACRadiusAuthorizationState_Type.__name__=_C
_SwWACRadiusAuthorizationState_Object=MibScalar
swWACRadiusAuthorizationState=_SwWACRadiusAuthorizationState_Object((1,3,6,1,4,1,171,12,27,1,11),_SwWACRadiusAuthorizationState_Type())
swWACRadiusAuthorizationState.setMaxAccess(_B)
if mibBuilder.loadTexts:swWACRadiusAuthorizationState.setStatus(_A)
class _SwWACLocalAuthorizationState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_H,2)))
_SwWACLocalAuthorizationState_Type.__name__=_C
_SwWACLocalAuthorizationState_Object=MibScalar
swWACLocalAuthorizationState=_SwWACLocalAuthorizationState_Object((1,3,6,1,4,1,171,12,27,1,12),_SwWACLocalAuthorizationState_Type())
swWACLocalAuthorizationState.setMaxAccess(_B)
if mibBuilder.loadTexts:swWACLocalAuthorizationState.setStatus(_A)
class _SwWACAuthClearDefaultredirpath_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),('start',2)))
_SwWACAuthClearDefaultredirpath_Type.__name__=_C
_SwWACAuthClearDefaultredirpath_Object=MibScalar
swWACAuthClearDefaultredirpath=_SwWACAuthClearDefaultredirpath_Object((1,3,6,1,4,1,171,12,27,1,13),_SwWACAuthClearDefaultredirpath_Type())
swWACAuthClearDefaultredirpath.setMaxAccess(_B)
if mibBuilder.loadTexts:swWACAuthClearDefaultredirpath.setStatus(_A)
_SwWACVirtualIPv6Addr_Type=Ipv6Address
_SwWACVirtualIPv6Addr_Object=MibScalar
swWACVirtualIPv6Addr=_SwWACVirtualIPv6Addr_Object((1,3,6,1,4,1,171,12,27,1,14),_SwWACVirtualIPv6Addr_Type())
swWACVirtualIPv6Addr.setMaxAccess(_B)
if mibBuilder.loadTexts:swWACVirtualIPv6Addr.setStatus(_A)
class _SwWACPageElementPageTitle_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_SwWACPageElementPageTitle_Type.__name__=_E
_SwWACPageElementPageTitle_Object=MibScalar
swWACPageElementPageTitle=_SwWACPageElementPageTitle_Object((1,3,6,1,4,1,171,12,27,1,30),_SwWACPageElementPageTitle_Type())
swWACPageElementPageTitle.setMaxAccess(_B)
if mibBuilder.loadTexts:swWACPageElementPageTitle.setStatus(_A)
class _SwWACPageElementLoginWindowTitle_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_SwWACPageElementLoginWindowTitle_Type.__name__=_E
_SwWACPageElementLoginWindowTitle_Object=MibScalar
swWACPageElementLoginWindowTitle=_SwWACPageElementLoginWindowTitle_Object((1,3,6,1,4,1,171,12,27,1,31),_SwWACPageElementLoginWindowTitle_Type())
swWACPageElementLoginWindowTitle.setMaxAccess(_B)
if mibBuilder.loadTexts:swWACPageElementLoginWindowTitle.setStatus(_A)
class _SwWACPageElementUserName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_SwWACPageElementUserName_Type.__name__=_E
_SwWACPageElementUserName_Object=MibScalar
swWACPageElementUserName=_SwWACPageElementUserName_Object((1,3,6,1,4,1,171,12,27,1,32),_SwWACPageElementUserName_Type())
swWACPageElementUserName.setMaxAccess(_B)
if mibBuilder.loadTexts:swWACPageElementUserName.setStatus(_A)
class _SwWACPageElementPassWord_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_SwWACPageElementPassWord_Type.__name__=_E
_SwWACPageElementPassWord_Object=MibScalar
swWACPageElementPassWord=_SwWACPageElementPassWord_Object((1,3,6,1,4,1,171,12,27,1,33),_SwWACPageElementPassWord_Type())
swWACPageElementPassWord.setMaxAccess(_B)
if mibBuilder.loadTexts:swWACPageElementPassWord.setStatus(_A)
class _SwJWACPageElementLogoutWindowTitle_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_SwJWACPageElementLogoutWindowTitle_Type.__name__=_E
_SwJWACPageElementLogoutWindowTitle_Object=MibScalar
swJWACPageElementLogoutWindowTitle=_SwJWACPageElementLogoutWindowTitle_Object((1,3,6,1,4,1,171,12,27,1,34),_SwJWACPageElementLogoutWindowTitle_Type())
swJWACPageElementLogoutWindowTitle.setMaxAccess(_B)
if mibBuilder.loadTexts:swJWACPageElementLogoutWindowTitle.setStatus(_A)
class _SwWACPageElementNotificationLine1_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_SwWACPageElementNotificationLine1_Type.__name__=_E
_SwWACPageElementNotificationLine1_Object=MibScalar
swWACPageElementNotificationLine1=_SwWACPageElementNotificationLine1_Object((1,3,6,1,4,1,171,12,27,1,35),_SwWACPageElementNotificationLine1_Type())
swWACPageElementNotificationLine1.setMaxAccess(_B)
if mibBuilder.loadTexts:swWACPageElementNotificationLine1.setStatus(_A)
class _SwWACPageElementNotificationLine2_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_SwWACPageElementNotificationLine2_Type.__name__=_E
_SwWACPageElementNotificationLine2_Object=MibScalar
swWACPageElementNotificationLine2=_SwWACPageElementNotificationLine2_Object((1,3,6,1,4,1,171,12,27,1,36),_SwWACPageElementNotificationLine2_Type())
swWACPageElementNotificationLine2.setMaxAccess(_B)
if mibBuilder.loadTexts:swWACPageElementNotificationLine2.setStatus(_A)
class _SwWACPageElementNotificationLine3_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_SwWACPageElementNotificationLine3_Type.__name__=_E
_SwWACPageElementNotificationLine3_Object=MibScalar
swWACPageElementNotificationLine3=_SwWACPageElementNotificationLine3_Object((1,3,6,1,4,1,171,12,27,1,37),_SwWACPageElementNotificationLine3_Type())
swWACPageElementNotificationLine3.setMaxAccess(_B)
if mibBuilder.loadTexts:swWACPageElementNotificationLine3.setStatus(_A)
class _SwWACPageElementNotificationLine4_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_SwWACPageElementNotificationLine4_Type.__name__=_E
_SwWACPageElementNotificationLine4_Object=MibScalar
swWACPageElementNotificationLine4=_SwWACPageElementNotificationLine4_Object((1,3,6,1,4,1,171,12,27,1,38),_SwWACPageElementNotificationLine4_Type())
swWACPageElementNotificationLine4.setMaxAccess(_B)
if mibBuilder.loadTexts:swWACPageElementNotificationLine4.setStatus(_A)
class _SwWACPageElementNotificationLine5_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_SwWACPageElementNotificationLine5_Type.__name__=_E
_SwWACPageElementNotificationLine5_Object=MibScalar
swWACPageElementNotificationLine5=_SwWACPageElementNotificationLine5_Object((1,3,6,1,4,1,171,12,27,1,39),_SwWACPageElementNotificationLine5_Type())
swWACPageElementNotificationLine5.setMaxAccess(_B)
if mibBuilder.loadTexts:swWACPageElementNotificationLine5.setStatus(_A)
_SwWACInfo_ObjectIdentity=ObjectIdentity
swWACInfo=_SwWACInfo_ObjectIdentity((1,3,6,1,4,1,171,12,27,2))
_SwWACAuthInfoTable_Object=MibTable
swWACAuthInfoTable=_SwWACAuthInfoTable_Object((1,3,6,1,4,1,171,12,27,2,1))
if mibBuilder.loadTexts:swWACAuthInfoTable.setStatus(_A)
_SwWACAuthInfoEntry_Object=MibTableRow
swWACAuthInfoEntry=_SwWACAuthInfoEntry_Object((1,3,6,1,4,1,171,12,27,2,1,1))
swWACAuthInfoEntry.setIndexNames((0,_F,_M),(0,_F,_N),(0,_F,_O))
if mibBuilder.loadTexts:swWACAuthInfoEntry.setStatus(_A)
_SwWACAuthInfoPort_Type=Integer32
_SwWACAuthInfoPort_Object=MibTableColumn
swWACAuthInfoPort=_SwWACAuthInfoPort_Object((1,3,6,1,4,1,171,12,27,2,1,1,1),_SwWACAuthInfoPort_Type())
swWACAuthInfoPort.setMaxAccess(_D)
if mibBuilder.loadTexts:swWACAuthInfoPort.setStatus(_A)
class _SwWACAuthInfoAuthStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_L,1),(_P,2),(_Q,3)))
_SwWACAuthInfoAuthStatus_Type.__name__=_C
_SwWACAuthInfoAuthStatus_Object=MibTableColumn
swWACAuthInfoAuthStatus=_SwWACAuthInfoAuthStatus_Object((1,3,6,1,4,1,171,12,27,2,1,1,2),_SwWACAuthInfoAuthStatus_Type())
swWACAuthInfoAuthStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:swWACAuthInfoAuthStatus.setStatus(_A)
_SwWACAuthInfoMACAddr_Type=MacAddress
_SwWACAuthInfoMACAddr_Object=MibTableColumn
swWACAuthInfoMACAddr=_SwWACAuthInfoMACAddr_Object((1,3,6,1,4,1,171,12,27,2,1,1,3),_SwWACAuthInfoMACAddr_Type())
swWACAuthInfoMACAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:swWACAuthInfoMACAddr.setStatus(_A)
_SwWACAuthInfoVID_Type=VlanId
_SwWACAuthInfoVID_Object=MibTableColumn
swWACAuthInfoVID=_SwWACAuthInfoVID_Object((1,3,6,1,4,1,171,12,27,2,1,1,4),_SwWACAuthInfoVID_Type())
swWACAuthInfoVID.setMaxAccess(_D)
if mibBuilder.loadTexts:swWACAuthInfoVID.setStatus(_A)
_SwWACAuthInfoRemainAgeTime_Type=Integer32
_SwWACAuthInfoRemainAgeTime_Object=MibTableColumn
swWACAuthInfoRemainAgeTime=_SwWACAuthInfoRemainAgeTime_Object((1,3,6,1,4,1,171,12,27,2,1,1,5),_SwWACAuthInfoRemainAgeTime_Type())
swWACAuthInfoRemainAgeTime.setMaxAccess(_D)
if mibBuilder.loadTexts:swWACAuthInfoRemainAgeTime.setStatus(_A)
_SwWACAuthInfoIdleTime_Type=Integer32
_SwWACAuthInfoIdleTime_Object=MibTableColumn
swWACAuthInfoIdleTime=_SwWACAuthInfoIdleTime_Object((1,3,6,1,4,1,171,12,27,2,1,1,6),_SwWACAuthInfoIdleTime_Type())
swWACAuthInfoIdleTime.setMaxAccess(_D)
if mibBuilder.loadTexts:swWACAuthInfoIdleTime.setStatus(_A)
_SwWACAuthInfoBlockTime_Type=Integer32
_SwWACAuthInfoBlockTime_Object=MibTableColumn
swWACAuthInfoBlockTime=_SwWACAuthInfoBlockTime_Object((1,3,6,1,4,1,171,12,27,2,1,1,7),_SwWACAuthInfoBlockTime_Type())
swWACAuthInfoBlockTime.setMaxAccess(_D)
if mibBuilder.loadTexts:swWACAuthInfoBlockTime.setStatus(_A)
class _SwWACAuthInfoStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_R,1),(_S,2)))
_SwWACAuthInfoStatus_Type.__name__=_C
_SwWACAuthInfoStatus_Object=MibTableColumn
swWACAuthInfoStatus=_SwWACAuthInfoStatus_Object((1,3,6,1,4,1,171,12,27,2,1,1,8),_SwWACAuthInfoStatus_Type())
swWACAuthInfoStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:swWACAuthInfoStatus.setStatus(_A)
_SwWACAuthInfoPriority_Type=Integer32
_SwWACAuthInfoPriority_Object=MibTableColumn
swWACAuthInfoPriority=_SwWACAuthInfoPriority_Object((1,3,6,1,4,1,171,12,27,2,1,1,9),_SwWACAuthInfoPriority_Type())
swWACAuthInfoPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:swWACAuthInfoPriority.setStatus(_A)
_SwWACAuthStateTable_Object=MibTable
swWACAuthStateTable=_SwWACAuthStateTable_Object((1,3,6,1,4,1,171,12,27,2,2))
if mibBuilder.loadTexts:swWACAuthStateTable.setStatus(_A)
_SwWACAuthStateEntry_Object=MibTableRow
swWACAuthStateEntry=_SwWACAuthStateEntry_Object((1,3,6,1,4,1,171,12,27,2,2,1))
swWACAuthStateEntry.setIndexNames((0,_F,_T),(0,_F,_U),(0,_F,_V))
if mibBuilder.loadTexts:swWACAuthStateEntry.setStatus(_A)
_SwWACAuthStatePort_Type=Integer32
_SwWACAuthStatePort_Object=MibTableColumn
swWACAuthStatePort=_SwWACAuthStatePort_Object((1,3,6,1,4,1,171,12,27,2,2,1,1),_SwWACAuthStatePort_Type())
swWACAuthStatePort.setMaxAccess(_D)
if mibBuilder.loadTexts:swWACAuthStatePort.setStatus(_A)
_SwWACAuthStateOriginalVid_Type=VlanId
_SwWACAuthStateOriginalVid_Object=MibTableColumn
swWACAuthStateOriginalVid=_SwWACAuthStateOriginalVid_Object((1,3,6,1,4,1,171,12,27,2,2,1,2),_SwWACAuthStateOriginalVid_Type())
swWACAuthStateOriginalVid.setMaxAccess(_D)
if mibBuilder.loadTexts:swWACAuthStateOriginalVid.setStatus(_A)
_SwWACAuthStateMACAddr_Type=MacAddress
_SwWACAuthStateMACAddr_Object=MibTableColumn
swWACAuthStateMACAddr=_SwWACAuthStateMACAddr_Object((1,3,6,1,4,1,171,12,27,2,2,1,3),_SwWACAuthStateMACAddr_Type())
swWACAuthStateMACAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:swWACAuthStateMACAddr.setStatus(_A)
class _SwWACAuthStateAuthStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_L,1),(_P,2),(_Q,3)))
_SwWACAuthStateAuthStatus_Type.__name__=_C
_SwWACAuthStateAuthStatus_Object=MibTableColumn
swWACAuthStateAuthStatus=_SwWACAuthStateAuthStatus_Object((1,3,6,1,4,1,171,12,27,2,2,1,5),_SwWACAuthStateAuthStatus_Type())
swWACAuthStateAuthStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:swWACAuthStateAuthStatus.setStatus(_A)
_SwWACAuthStateAssignVid_Type=VlanId
_SwWACAuthStateAssignVid_Object=MibTableColumn
swWACAuthStateAssignVid=_SwWACAuthStateAssignVid_Object((1,3,6,1,4,1,171,12,27,2,2,1,7),_SwWACAuthStateAssignVid_Type())
swWACAuthStateAssignVid.setMaxAccess(_D)
if mibBuilder.loadTexts:swWACAuthStateAssignVid.setStatus(_A)
_SwWACAuthStateAssignPriority_Type=Integer32
_SwWACAuthStateAssignPriority_Object=MibTableColumn
swWACAuthStateAssignPriority=_SwWACAuthStateAssignPriority_Object((1,3,6,1,4,1,171,12,27,2,2,1,8),_SwWACAuthStateAssignPriority_Type())
swWACAuthStateAssignPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:swWACAuthStateAssignPriority.setStatus(_A)
_SwWACAuthStateRemainTime_Type=Integer32
_SwWACAuthStateRemainTime_Object=MibTableColumn
swWACAuthStateRemainTime=_SwWACAuthStateRemainTime_Object((1,3,6,1,4,1,171,12,27,2,2,1,12),_SwWACAuthStateRemainTime_Type())
swWACAuthStateRemainTime.setMaxAccess(_D)
if mibBuilder.loadTexts:swWACAuthStateRemainTime.setStatus(_A)
_SwWACAuthStateIdleTime_Type=Integer32
_SwWACAuthStateIdleTime_Object=MibTableColumn
swWACAuthStateIdleTime=_SwWACAuthStateIdleTime_Object((1,3,6,1,4,1,171,12,27,2,2,1,14),_SwWACAuthStateIdleTime_Type())
swWACAuthStateIdleTime.setMaxAccess(_D)
if mibBuilder.loadTexts:swWACAuthStateIdleTime.setStatus(_A)
class _SwWACAuthStateDelAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_R,1),(_S,2)))
_SwWACAuthStateDelAction_Type.__name__=_C
_SwWACAuthStateDelAction_Object=MibTableColumn
swWACAuthStateDelAction=_SwWACAuthStateDelAction_Object((1,3,6,1,4,1,171,12,27,2,2,1,25),_SwWACAuthStateDelAction_Type())
swWACAuthStateDelAction.setMaxAccess(_B)
if mibBuilder.loadTexts:swWACAuthStateDelAction.setStatus(_A)
_SwWACMgmt_ObjectIdentity=ObjectIdentity
swWACMgmt=_SwWACMgmt_ObjectIdentity((1,3,6,1,4,1,171,12,27,3))
_SwWebAuthPortTable_Object=MibTable
swWebAuthPortTable=_SwWebAuthPortTable_Object((1,3,6,1,4,1,171,12,27,3,1))
if mibBuilder.loadTexts:swWebAuthPortTable.setStatus(_A)
_SwWebAuthPortEntry_Object=MibTableRow
swWebAuthPortEntry=_SwWebAuthPortEntry_Object((1,3,6,1,4,1,171,12,27,3,1,1))
swWebAuthPortEntry.setIndexNames((0,_F,_W))
if mibBuilder.loadTexts:swWebAuthPortEntry.setStatus(_A)
_SwWebAuthPortIndex_Type=Integer32
_SwWebAuthPortIndex_Object=MibTableColumn
swWebAuthPortIndex=_SwWebAuthPortIndex_Object((1,3,6,1,4,1,171,12,27,3,1,1,1),_SwWebAuthPortIndex_Type())
swWebAuthPortIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:swWebAuthPortIndex.setStatus(_A)
class _SwWebAuthPortState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_J,1),(_H,2),(_I,3)))
_SwWebAuthPortState_Type.__name__=_C
_SwWebAuthPortState_Object=MibTableColumn
swWebAuthPortState=_SwWebAuthPortState_Object((1,3,6,1,4,1,171,12,27,3,1,1,2),_SwWebAuthPortState_Type())
swWebAuthPortState.setMaxAccess(_B)
if mibBuilder.loadTexts:swWebAuthPortState.setStatus(_A)
_SwWebAuthPortUserName_Type=DisplayString
_SwWebAuthPortUserName_Object=MibTableColumn
swWebAuthPortUserName=_SwWebAuthPortUserName_Object((1,3,6,1,4,1,171,12,27,3,1,1,3),_SwWebAuthPortUserName_Type())
swWebAuthPortUserName.setMaxAccess(_D)
if mibBuilder.loadTexts:swWebAuthPortUserName.setStatus(_G)
class _SwWebAuthAuthStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('unauthenticated',1),(_L,2)))
_SwWebAuthAuthStatus_Type.__name__=_C
_SwWebAuthAuthStatus_Object=MibTableColumn
swWebAuthAuthStatus=_SwWebAuthAuthStatus_Object((1,3,6,1,4,1,171,12,27,3,1,1,4),_SwWebAuthAuthStatus_Type())
swWebAuthAuthStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:swWebAuthAuthStatus.setStatus(_G)
_SwWebAuthAssignedVID_Type=Integer32
_SwWebAuthAssignedVID_Object=MibTableColumn
swWebAuthAssignedVID=_SwWebAuthAssignedVID_Object((1,3,6,1,4,1,171,12,27,3,1,1,5),_SwWebAuthAssignedVID_Type())
swWebAuthAssignedVID.setMaxAccess(_D)
if mibBuilder.loadTexts:swWebAuthAssignedVID.setStatus(_G)
class _SwWACPortAgeingTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1440))
_SwWACPortAgeingTime_Type.__name__=_C
_SwWACPortAgeingTime_Object=MibTableColumn
swWACPortAgeingTime=_SwWACPortAgeingTime_Object((1,3,6,1,4,1,171,12,27,3,1,1,6),_SwWACPortAgeingTime_Type())
swWACPortAgeingTime.setMaxAccess(_B)
if mibBuilder.loadTexts:swWACPortAgeingTime.setStatus(_A)
class _SwWACPortIdleTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1440))
_SwWACPortIdleTime_Type.__name__=_C
_SwWACPortIdleTime_Object=MibTableColumn
swWACPortIdleTime=_SwWACPortIdleTime_Object((1,3,6,1,4,1,171,12,27,3,1,1,7),_SwWACPortIdleTime_Type())
swWACPortIdleTime.setMaxAccess(_B)
if mibBuilder.loadTexts:swWACPortIdleTime.setStatus(_A)
class _SwWACPortBlockTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,300))
_SwWACPortBlockTime_Type.__name__=_C
_SwWACPortBlockTime_Object=MibTableColumn
swWACPortBlockTime=_SwWACPortBlockTime_Object((1,3,6,1,4,1,171,12,27,3,1,1,8),_SwWACPortBlockTime_Type())
swWACPortBlockTime.setMaxAccess(_B)
if mibBuilder.loadTexts:swWACPortBlockTime.setStatus(_A)
_SwWebAuthUserTable_Object=MibTable
swWebAuthUserTable=_SwWebAuthUserTable_Object((1,3,6,1,4,1,171,12,27,3,2))
if mibBuilder.loadTexts:swWebAuthUserTable.setStatus(_A)
_SwWebAuthUserEntry_Object=MibTableRow
swWebAuthUserEntry=_SwWebAuthUserEntry_Object((1,3,6,1,4,1,171,12,27,3,2,1))
swWebAuthUserEntry.setIndexNames((0,_F,_X))
if mibBuilder.loadTexts:swWebAuthUserEntry.setStatus(_A)
class _SwWebAuthUserNameIndex_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,15))
_SwWebAuthUserNameIndex_Type.__name__=_E
_SwWebAuthUserNameIndex_Object=MibTableColumn
swWebAuthUserNameIndex=_SwWebAuthUserNameIndex_Object((1,3,6,1,4,1,171,12,27,3,2,1,1),_SwWebAuthUserNameIndex_Type())
swWebAuthUserNameIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:swWebAuthUserNameIndex.setStatus(_A)
class _SwWebAuthUserPWD_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,15))
_SwWebAuthUserPWD_Type.__name__=_E
_SwWebAuthUserPWD_Object=MibTableColumn
swWebAuthUserPWD=_SwWebAuthUserPWD_Object((1,3,6,1,4,1,171,12,27,3,2,1,2),_SwWebAuthUserPWD_Type())
swWebAuthUserPWD.setMaxAccess(_K)
if mibBuilder.loadTexts:swWebAuthUserPWD.setStatus(_A)
class _SwWebAuthUserVlanName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_SwWebAuthUserVlanName_Type.__name__=_E
_SwWebAuthUserVlanName_Object=MibTableColumn
swWebAuthUserVlanName=_SwWebAuthUserVlanName_Object((1,3,6,1,4,1,171,12,27,3,2,1,3),_SwWebAuthUserVlanName_Type())
swWebAuthUserVlanName.setMaxAccess(_K)
if mibBuilder.loadTexts:swWebAuthUserVlanName.setStatus(_G)
_SwWebAuthUserStatus_Type=RowStatus
_SwWebAuthUserStatus_Object=MibTableColumn
swWebAuthUserStatus=_SwWebAuthUserStatus_Object((1,3,6,1,4,1,171,12,27,3,2,1,4),_SwWebAuthUserStatus_Type())
swWebAuthUserStatus.setMaxAccess(_K)
if mibBuilder.loadTexts:swWebAuthUserStatus.setStatus(_A)
class _SwWebAuthUserVID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4094))
_SwWebAuthUserVID_Type.__name__=_C
_SwWebAuthUserVID_Object=MibTableColumn
swWebAuthUserVID=_SwWebAuthUserVID_Object((1,3,6,1,4,1,171,12,27,3,2,1,5),_SwWebAuthUserVID_Type())
swWebAuthUserVID.setMaxAccess(_K)
if mibBuilder.loadTexts:swWebAuthUserVID.setStatus(_A)
mibBuilder.exportSymbols(_F,**{'VlanId':VlanId,'swWACMIB':swWACMIB,'swWACCtrl':swWACCtrl,'swWebAuthAdminState':swWebAuthAdminState,'swWebAuthMethod':swWebAuthMethod,'swWebAuthVlanName':swWebAuthVlanName,'swWebAuthAllPortstate':swWebAuthAllPortstate,'swWebAuthDefaultredirpath':swWebAuthDefaultredirpath,'swWebAuthLogouttimer':swWebAuthLogouttimer,'swWACVirtualIpAddr':swWACVirtualIpAddr,'swWACSwitchHttpProtocol':swWACSwitchHttpProtocol,'swWACSwitchHttpPort':swWACSwitchHttpPort,'swWACAuthFailOverState':swWACAuthFailOverState,'swWACRadiusAuthorizationState':swWACRadiusAuthorizationState,'swWACLocalAuthorizationState':swWACLocalAuthorizationState,'swWACAuthClearDefaultredirpath':swWACAuthClearDefaultredirpath,'swWACVirtualIPv6Addr':swWACVirtualIPv6Addr,'swWACPageElementPageTitle':swWACPageElementPageTitle,'swWACPageElementLoginWindowTitle':swWACPageElementLoginWindowTitle,'swWACPageElementUserName':swWACPageElementUserName,'swWACPageElementPassWord':swWACPageElementPassWord,'swJWACPageElementLogoutWindowTitle':swJWACPageElementLogoutWindowTitle,'swWACPageElementNotificationLine1':swWACPageElementNotificationLine1,'swWACPageElementNotificationLine2':swWACPageElementNotificationLine2,'swWACPageElementNotificationLine3':swWACPageElementNotificationLine3,'swWACPageElementNotificationLine4':swWACPageElementNotificationLine4,'swWACPageElementNotificationLine5':swWACPageElementNotificationLine5,'swWACInfo':swWACInfo,'swWACAuthInfoTable':swWACAuthInfoTable,'swWACAuthInfoEntry':swWACAuthInfoEntry,_M:swWACAuthInfoPort,_N:swWACAuthInfoAuthStatus,_O:swWACAuthInfoMACAddr,'swWACAuthInfoVID':swWACAuthInfoVID,'swWACAuthInfoRemainAgeTime':swWACAuthInfoRemainAgeTime,'swWACAuthInfoIdleTime':swWACAuthInfoIdleTime,'swWACAuthInfoBlockTime':swWACAuthInfoBlockTime,'swWACAuthInfoStatus':swWACAuthInfoStatus,'swWACAuthInfoPriority':swWACAuthInfoPriority,'swWACAuthStateTable':swWACAuthStateTable,'swWACAuthStateEntry':swWACAuthStateEntry,_T:swWACAuthStatePort,_U:swWACAuthStateOriginalVid,_V:swWACAuthStateMACAddr,'swWACAuthStateAuthStatus':swWACAuthStateAuthStatus,'swWACAuthStateAssignVid':swWACAuthStateAssignVid,'swWACAuthStateAssignPriority':swWACAuthStateAssignPriority,'swWACAuthStateRemainTime':swWACAuthStateRemainTime,'swWACAuthStateIdleTime':swWACAuthStateIdleTime,'swWACAuthStateDelAction':swWACAuthStateDelAction,'swWACMgmt':swWACMgmt,'swWebAuthPortTable':swWebAuthPortTable,'swWebAuthPortEntry':swWebAuthPortEntry,_W:swWebAuthPortIndex,'swWebAuthPortState':swWebAuthPortState,'swWebAuthPortUserName':swWebAuthPortUserName,'swWebAuthAuthStatus':swWebAuthAuthStatus,'swWebAuthAssignedVID':swWebAuthAssignedVID,'swWACPortAgeingTime':swWACPortAgeingTime,'swWACPortIdleTime':swWACPortIdleTime,'swWACPortBlockTime':swWACPortBlockTime,'swWebAuthUserTable':swWebAuthUserTable,'swWebAuthUserEntry':swWebAuthUserEntry,_X:swWebAuthUserNameIndex,'swWebAuthUserPWD':swWebAuthUserPWD,'swWebAuthUserVlanName':swWebAuthUserVlanName,'swWebAuthUserStatus':swWebAuthUserStatus,'swWebAuthUserVID':swWebAuthUserVID})