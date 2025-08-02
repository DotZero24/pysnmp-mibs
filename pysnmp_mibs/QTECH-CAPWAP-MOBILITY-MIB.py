_Ay='qtechMobilityMIBGroup'
_Ax='qtechMobilityNotifyStaReason'
_Aw='qtechMobilityNotifyStaRssi'
_Av='qtechMobilityNotifyStaClientType'
_Au='qtechMobilityNotifyStaCurChan'
_At='qtechMobilityNotifyStaLinkRate'
_As='qtechMobilityNotifyStaSsid'
_Ar='qtechMobilityNotifyStaNetAuthMode'
_Aq='qtechMobilityNotifyStaAssoAuthMode'
_Ap='qtechMobilityNotifyStaIpv6'
_Ao='qtechMobilityNotifyStaWlanId'
_An='qtechMobilityNotifyStaVlanId'
_Am='qtechMobilityNotifyStaApRadioType'
_Al='qtechMobilityNotifyStaApRadioId'
_Ak='qtechMobilityNotifyStaOperType'
_Aj='qtechMobilityNotifyStaIp'
_Ai='qtechMobilityNotifyApIp'
_Ah='qtechMobilityNotifyStaMac'
_Ag='qtechMobilityNotifyApMac'
_Af='qtechRoamTrackStaOnlineTime'
_Ae='qtechRoamTrackStaIpv6'
_Ad='qtechRoamTrackStaIp'
_Ac='qtechRoamTrackRadioId'
_Ab='qtechRoamTrackApMac'
_Aa='qtechRoamTrackAcAddress'
_AZ='qtechRoamTrackAcAddressType'
_AY='qtechRoamUserRoamInVid'
_AX='qtechRoamUserRoamOutVid'
_AW='qtechRoamUserRoamInApMac'
_AV='qtechRoamUserRoamOutApMac'
_AU='qtechRoamUserRoamInAcAddress'
_AT='qtechRoamUserRoamInAcAddressType'
_AS='qtechRoamUserRoamOutAcAddress'
_AR='qtechRoamUserRoamOutAcAddressType'
_AQ='qtechRoamUserRoamType'
_AP='qtechRoamIPv6MemberCreateStatus'
_AO='qtechRoamIPv6MemberDTLSIsOK'
_AN='qtechRoamIPv6MemberDTLSIsClient'
_AM='qtechRoamIPv6MemberDataChannelFailTimes'
_AL='qtechRoamIPv6MemberDataChannelIsOK'
_AK='qtechRoamIPv6MemberIsList'
_AJ='qtechMobilityACPingIPv6'
_AI='qtechACInterRoamOut'
_AH='qtechACInterRoamIn'
_AG='qtechACIntraRoam'
_AF='qtechTeriaryBackUpACName'
_AE='qtechTeriaryBackUpACip'
_AD='qtechSecondaryBackUpACName'
_AC='qtechSecondaryBackUpACIP'
_AB='qtechPrimaryBackUpACName'
_AA='qtechPrimaryBackUpACIP'
_A9='qtechAPPriorityEnable'
_A8='qtechInitAnchorDenyReceived'
_A7='qtechInitAnchorRequestSent'
_A6='qtechInitHandoffDenyReceived'
_A5='qtechInitHandoffasForeignReceived'
_A4='qtechInitHandoffasLocalReceived'
_A3='qtechInitHandoffReplyReceived'
_A2='qtechInitHandoffRequestsSent'
_A1='qtechRespondeAnchorTransferred'
_A0='qtechRespondeAnchorRequestDenied'
_z='qtechRespondeAnchorRequestsReceived'
_y='qtechRespondeClientHandoffasForeign'
_x='qtechRespondeClientHandoffasLocal'
_w='qtechRespondeHandoffRequestsDenied'
_v='qtechRespondeHandoffRequestsDroped'
_u='qtechRespondePingPongHandoffRequestsDropped'
_t='qtechRespondeHandoffRequestIgnored'
_s='qtechGlobalResourceUnavailable'
_r='qtechGlobalStateTransitionsDisabled'
_q='qtechGlobalHandoffEndRequestsReceived'
_p='qtechGlobalHandoffRequestsReceived'
_o='qtechWLANCtrlCreatStatus'
_n='qtechAnchorACIPaddr'
_m='qtechAPCtrlCreatStatus'
_l='qtechTertiaryACName'
_k='qtechTertiaryACIP'
_j='qtechSecondaryACName'
_i='qtechSecondaryACIP'
_h='qtechPrimaryACName'
_g='qtechPrimaryACIP'
_f='qtechPriority'
_e='qtechRoamMemberCreateStatus'
_d='qtechRoamMemberDTLSIsOK'
_c='qtechRoamMemberDTLSIsClient'
_b='qtechRoamMemberDataChannelFailTimes'
_a='qtechRoamMemberDataChannelIsOK'
_Z='qtechRoamMemberIsList'
_Y='qtechRoamGroupCreateStatus'
_X='qtechRoamGroupIsFast'
_W='qtechRoamGroupKeepaliveInterval'
_V='qtechRoamGroupKeepaliveCount'
_U='qtechRoamGroupMcAddress'
_T='qtechRoamGroupMcEnable'
_S='qtechRoamGroupMyAddress'
_R='qtechRoamGroupName'
_Q='qtechWLANID'
_P='qtechAPName'
_O='qtechRoamMemberPeerAddress'
_N='qtechRoamMemberGroupId'
_M='qtechRoamGroupId'
_L='qtechRoamTrackId'
_K='qtechRoamTrackStaMac'
_J='qtechRoamUserMac'
_I='qtechRoamIPv6MemberPeerAddress'
_H='qtechRoamIPv6MemberGroupId'
_G='accessible-for-notify'
_F='Integer32'
_E='read-write'
_D='read-create'
_C='read-only'
_B='QTECH-CAPWAP-MOBILITY-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
Ipv6Address,=mibBuilder.importSymbols('IPV6-TC','Ipv6Address')
qtechMgmt,=mibBuilder.importSymbols('QTECH-SMI','qtechMgmt')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention')
qtechMobilityMIB=ModuleIdentity((1,3,6,1,4,1,27514,1,1,10,2,64))
if mibBuilder.loadTexts:qtechMobilityMIB.setRevisions(('2009-09-18 00:00',))
_QtechMobilityMIBObjects_ObjectIdentity=ObjectIdentity
qtechMobilityMIBObjects=_QtechMobilityMIBObjects_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,64,1))
_QtechMobility_ObjectIdentity=ObjectIdentity
qtechMobility=_QtechMobility_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,64,1,1))
_QtechMobilityEntryTable_Object=MibTable
qtechMobilityEntryTable=_QtechMobilityEntryTable_Object((1,3,6,1,4,1,27514,1,1,10,2,64,1,1,1))
if mibBuilder.loadTexts:qtechMobilityEntryTable.setStatus(_A)
_QtechMobilityEntry_Object=MibTableRow
qtechMobilityEntry=_QtechMobilityEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,64,1,1,1,1))
qtechMobilityEntry.setIndexNames((0,_B,_M))
if mibBuilder.loadTexts:qtechMobilityEntry.setStatus(_A)
class _QtechRoamGroupId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,8))
_QtechRoamGroupId_Type.__name__=_F
_QtechRoamGroupId_Object=MibTableColumn
qtechRoamGroupId=_QtechRoamGroupId_Object((1,3,6,1,4,1,27514,1,1,10,2,64,1,1,1,1,1),_QtechRoamGroupId_Type())
qtechRoamGroupId.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechRoamGroupId.setStatus(_A)
_QtechRoamGroupName_Type=DisplayString
_QtechRoamGroupName_Object=MibTableColumn
qtechRoamGroupName=_QtechRoamGroupName_Object((1,3,6,1,4,1,27514,1,1,10,2,64,1,1,1,1,2),_QtechRoamGroupName_Type())
qtechRoamGroupName.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechRoamGroupName.setStatus(_A)
_QtechRoamGroupMyAddress_Type=IpAddress
_QtechRoamGroupMyAddress_Object=MibTableColumn
qtechRoamGroupMyAddress=_QtechRoamGroupMyAddress_Object((1,3,6,1,4,1,27514,1,1,10,2,64,1,1,1,1,3),_QtechRoamGroupMyAddress_Type())
qtechRoamGroupMyAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechRoamGroupMyAddress.setStatus(_A)
_QtechRoamGroupMcEnable_Type=Integer32
_QtechRoamGroupMcEnable_Object=MibTableColumn
qtechRoamGroupMcEnable=_QtechRoamGroupMcEnable_Object((1,3,6,1,4,1,27514,1,1,10,2,64,1,1,1,1,4),_QtechRoamGroupMcEnable_Type())
qtechRoamGroupMcEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechRoamGroupMcEnable.setStatus(_A)
_QtechRoamGroupMcAddress_Type=IpAddress
_QtechRoamGroupMcAddress_Object=MibTableColumn
qtechRoamGroupMcAddress=_QtechRoamGroupMcAddress_Object((1,3,6,1,4,1,27514,1,1,10,2,64,1,1,1,1,5),_QtechRoamGroupMcAddress_Type())
qtechRoamGroupMcAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechRoamGroupMcAddress.setStatus(_A)
class _QtechRoamGroupKeepaliveCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,30))
_QtechRoamGroupKeepaliveCount_Type.__name__=_F
_QtechRoamGroupKeepaliveCount_Object=MibTableColumn
qtechRoamGroupKeepaliveCount=_QtechRoamGroupKeepaliveCount_Object((1,3,6,1,4,1,27514,1,1,10,2,64,1,1,1,1,6),_QtechRoamGroupKeepaliveCount_Type())
qtechRoamGroupKeepaliveCount.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechRoamGroupKeepaliveCount.setStatus(_A)
class _QtechRoamGroupKeepaliveInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,30))
_QtechRoamGroupKeepaliveInterval_Type.__name__=_F
_QtechRoamGroupKeepaliveInterval_Object=MibTableColumn
qtechRoamGroupKeepaliveInterval=_QtechRoamGroupKeepaliveInterval_Object((1,3,6,1,4,1,27514,1,1,10,2,64,1,1,1,1,7),_QtechRoamGroupKeepaliveInterval_Type())
qtechRoamGroupKeepaliveInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechRoamGroupKeepaliveInterval.setStatus(_A)
_QtechRoamGroupIsFast_Type=Integer32
_QtechRoamGroupIsFast_Object=MibTableColumn
qtechRoamGroupIsFast=_QtechRoamGroupIsFast_Object((1,3,6,1,4,1,27514,1,1,10,2,64,1,1,1,1,8),_QtechRoamGroupIsFast_Type())
qtechRoamGroupIsFast.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechRoamGroupIsFast.setStatus(_A)
_QtechRoamGroupCreateStatus_Type=RowStatus
_QtechRoamGroupCreateStatus_Object=MibTableColumn
qtechRoamGroupCreateStatus=_QtechRoamGroupCreateStatus_Object((1,3,6,1,4,1,27514,1,1,10,2,64,1,1,1,1,9),_QtechRoamGroupCreateStatus_Type())
qtechRoamGroupCreateStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechRoamGroupCreateStatus.setStatus(_A)
_QtechRoamGroupMyAddressIPv6_Type=Ipv6Address
_QtechRoamGroupMyAddressIPv6_Object=MibTableColumn
qtechRoamGroupMyAddressIPv6=_QtechRoamGroupMyAddressIPv6_Object((1,3,6,1,4,1,27514,1,1,10,2,64,1,1,1,1,10),_QtechRoamGroupMyAddressIPv6_Type())
qtechRoamGroupMyAddressIPv6.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechRoamGroupMyAddressIPv6.setStatus(_A)
_QtechMobilityMemberEntryTable_Object=MibTable
qtechMobilityMemberEntryTable=_QtechMobilityMemberEntryTable_Object((1,3,6,1,4,1,27514,1,1,10,2,64,1,1,2))
if mibBuilder.loadTexts:qtechMobilityMemberEntryTable.setStatus(_A)
_QtechMobilityMemberEntry_Object=MibTableRow
qtechMobilityMemberEntry=_QtechMobilityMemberEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,64,1,1,2,1))
qtechMobilityMemberEntry.setIndexNames((0,_B,_N),(0,_B,_O))
if mibBuilder.loadTexts:qtechMobilityMemberEntry.setStatus(_A)
class _QtechRoamMemberGroupId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,8))
_QtechRoamMemberGroupId_Type.__name__=_F
_QtechRoamMemberGroupId_Object=MibTableColumn
qtechRoamMemberGroupId=_QtechRoamMemberGroupId_Object((1,3,6,1,4,1,27514,1,1,10,2,64,1,1,2,1,1),_QtechRoamMemberGroupId_Type())
qtechRoamMemberGroupId.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechRoamMemberGroupId.setStatus(_A)
_QtechRoamMemberPeerAddress_Type=IpAddress
_QtechRoamMemberPeerAddress_Object=MibTableColumn
qtechRoamMemberPeerAddress=_QtechRoamMemberPeerAddress_Object((1,3,6,1,4,1,27514,1,1,10,2,64,1,1,2,1,2),_QtechRoamMemberPeerAddress_Type())
qtechRoamMemberPeerAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechRoamMemberPeerAddress.setStatus(_A)
class _QtechRoamMemberIsList_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_QtechRoamMemberIsList_Type.__name__=_F
_QtechRoamMemberIsList_Object=MibTableColumn
qtechRoamMemberIsList=_QtechRoamMemberIsList_Object((1,3,6,1,4,1,27514,1,1,10,2,64,1,1,2,1,3),_QtechRoamMemberIsList_Type())
qtechRoamMemberIsList.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechRoamMemberIsList.setStatus(_A)
class _QtechRoamMemberDataChannelIsOK_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_QtechRoamMemberDataChannelIsOK_Type.__name__=_F
_QtechRoamMemberDataChannelIsOK_Object=MibTableColumn
qtechRoamMemberDataChannelIsOK=_QtechRoamMemberDataChannelIsOK_Object((1,3,6,1,4,1,27514,1,1,10,2,64,1,1,2,1,4),_QtechRoamMemberDataChannelIsOK_Type())
qtechRoamMemberDataChannelIsOK.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechRoamMemberDataChannelIsOK.setStatus(_A)
_QtechRoamMemberDataChannelFailTimes_Type=Integer32
_QtechRoamMemberDataChannelFailTimes_Object=MibTableColumn
qtechRoamMemberDataChannelFailTimes=_QtechRoamMemberDataChannelFailTimes_Object((1,3,6,1,4,1,27514,1,1,10,2,64,1,1,2,1,5),_QtechRoamMemberDataChannelFailTimes_Type())
qtechRoamMemberDataChannelFailTimes.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechRoamMemberDataChannelFailTimes.setStatus(_A)
_QtechRoamMemberDTLSIsClient_Type=Integer32
_QtechRoamMemberDTLSIsClient_Object=MibTableColumn
qtechRoamMemberDTLSIsClient=_QtechRoamMemberDTLSIsClient_Object((1,3,6,1,4,1,27514,1,1,10,2,64,1,1,2,1,6),_QtechRoamMemberDTLSIsClient_Type())
qtechRoamMemberDTLSIsClient.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechRoamMemberDTLSIsClient.setStatus(_A)
class _QtechRoamMemberDTLSIsOK_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_QtechRoamMemberDTLSIsOK_Type.__name__=_F
_QtechRoamMemberDTLSIsOK_Object=MibTableColumn
qtechRoamMemberDTLSIsOK=_QtechRoamMemberDTLSIsOK_Object((1,3,6,1,4,1,27514,1,1,10,2,64,1,1,2,1,7),_QtechRoamMemberDTLSIsOK_Type())
qtechRoamMemberDTLSIsOK.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechRoamMemberDTLSIsOK.setStatus(_A)
_QtechRoamMemberCreateStatus_Type=RowStatus
_QtechRoamMemberCreateStatus_Object=MibTableColumn
qtechRoamMemberCreateStatus=_QtechRoamMemberCreateStatus_Object((1,3,6,1,4,1,27514,1,1,10,2,64,1,1,2,1,8),_QtechRoamMemberCreateStatus_Type())
qtechRoamMemberCreateStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechRoamMemberCreateStatus.setStatus(_A)
_QtechAPCtrlCreatEntryTable_Object=MibTable
qtechAPCtrlCreatEntryTable=_QtechAPCtrlCreatEntryTable_Object((1,3,6,1,4,1,27514,1,1,10,2,64,1,1,3))
if mibBuilder.loadTexts:qtechAPCtrlCreatEntryTable.setStatus(_A)
_QtechAPCtrlCreatEntry_Object=MibTableRow
qtechAPCtrlCreatEntry=_QtechAPCtrlCreatEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,64,1,1,3,1))
qtechAPCtrlCreatEntry.setIndexNames((0,_B,_P))
if mibBuilder.loadTexts:qtechAPCtrlCreatEntry.setStatus(_A)
_QtechAPName_Type=DisplayString
_QtechAPName_Object=MibTableColumn
qtechAPName=_QtechAPName_Object((1,3,6,1,4,1,27514,1,1,10,2,64,1,1,3,1,1),_QtechAPName_Type())
qtechAPName.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:qtechAPName.setStatus(_A)
class _QtechPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_QtechPriority_Type.__name__=_F
_QtechPriority_Object=MibTableColumn
qtechPriority=_QtechPriority_Object((1,3,6,1,4,1,27514,1,1,10,2,64,1,1,3,1,2),_QtechPriority_Type())
qtechPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechPriority.setStatus(_A)
_QtechPrimaryACIP_Type=IpAddress
_QtechPrimaryACIP_Object=MibTableColumn
qtechPrimaryACIP=_QtechPrimaryACIP_Object((1,3,6,1,4,1,27514,1,1,10,2,64,1,1,3,1,3),_QtechPrimaryACIP_Type())
qtechPrimaryACIP.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechPrimaryACIP.setStatus(_A)
_QtechPrimaryACName_Type=DisplayString
_QtechPrimaryACName_Object=MibTableColumn
qtechPrimaryACName=_QtechPrimaryACName_Object((1,3,6,1,4,1,27514,1,1,10,2,64,1,1,3,1,4),_QtechPrimaryACName_Type())
qtechPrimaryACName.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechPrimaryACName.setStatus(_A)
_QtechSecondaryACIP_Type=IpAddress
_QtechSecondaryACIP_Object=MibTableColumn
qtechSecondaryACIP=_QtechSecondaryACIP_Object((1,3,6,1,4,1,27514,1,1,10,2,64,1,1,3,1,5),_QtechSecondaryACIP_Type())
qtechSecondaryACIP.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechSecondaryACIP.setStatus(_A)
_QtechSecondaryACName_Type=DisplayString
_QtechSecondaryACName_Object=MibTableColumn
qtechSecondaryACName=_QtechSecondaryACName_Object((1,3,6,1,4,1,27514,1,1,10,2,64,1,1,3,1,6),_QtechSecondaryACName_Type())
qtechSecondaryACName.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechSecondaryACName.setStatus(_A)
_QtechTertiaryACIP_Type=IpAddress
_QtechTertiaryACIP_Object=MibTableColumn
qtechTertiaryACIP=_QtechTertiaryACIP_Object((1,3,6,1,4,1,27514,1,1,10,2,64,1,1,3,1,7),_QtechTertiaryACIP_Type())
qtechTertiaryACIP.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechTertiaryACIP.setStatus(_A)
_QtechTertiaryACName_Type=DisplayString
_QtechTertiaryACName_Object=MibTableColumn
qtechTertiaryACName=_QtechTertiaryACName_Object((1,3,6,1,4,1,27514,1,1,10,2,64,1,1,3,1,8),_QtechTertiaryACName_Type())
qtechTertiaryACName.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechTertiaryACName.setStatus(_A)
_QtechAPCtrlCreatStatus_Type=RowStatus
_QtechAPCtrlCreatStatus_Object=MibTableColumn
qtechAPCtrlCreatStatus=_QtechAPCtrlCreatStatus_Object((1,3,6,1,4,1,27514,1,1,10,2,64,1,1,3,1,9),_QtechAPCtrlCreatStatus_Type())
qtechAPCtrlCreatStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechAPCtrlCreatStatus.setStatus(_A)
_QtechWLANCtrlCreatEntryTable_Object=MibTable
qtechWLANCtrlCreatEntryTable=_QtechWLANCtrlCreatEntryTable_Object((1,3,6,1,4,1,27514,1,1,10,2,64,1,1,4))
if mibBuilder.loadTexts:qtechWLANCtrlCreatEntryTable.setStatus(_A)
_QtechWLANCtrlCreatEntry_Object=MibTableRow
qtechWLANCtrlCreatEntry=_QtechWLANCtrlCreatEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,64,1,1,4,1))
qtechWLANCtrlCreatEntry.setIndexNames((0,_B,_Q))
if mibBuilder.loadTexts:qtechWLANCtrlCreatEntry.setStatus(_A)
_QtechWLANID_Type=Integer32
_QtechWLANID_Object=MibTableColumn
qtechWLANID=_QtechWLANID_Object((1,3,6,1,4,1,27514,1,1,10,2,64,1,1,4,1,1),_QtechWLANID_Type())
qtechWLANID.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechWLANID.setStatus(_A)
_QtechAnchorACIPaddr_Type=IpAddress
_QtechAnchorACIPaddr_Object=MibTableColumn
qtechAnchorACIPaddr=_QtechAnchorACIPaddr_Object((1,3,6,1,4,1,27514,1,1,10,2,64,1,1,4,1,2),_QtechAnchorACIPaddr_Type())
qtechAnchorACIPaddr.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechAnchorACIPaddr.setStatus(_A)
_QtechWLANCtrlCreatStatus_Type=RowStatus
_QtechWLANCtrlCreatStatus_Object=MibTableColumn
qtechWLANCtrlCreatStatus=_QtechWLANCtrlCreatStatus_Object((1,3,6,1,4,1,27514,1,1,10,2,64,1,1,4,1,3),_QtechWLANCtrlCreatStatus_Type())
qtechWLANCtrlCreatStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechWLANCtrlCreatStatus.setStatus(_A)
_QtechAnchorACIPaddrIPv6_Type=Ipv6Address
_QtechAnchorACIPaddrIPv6_Object=MibTableColumn
qtechAnchorACIPaddrIPv6=_QtechAnchorACIPaddrIPv6_Object((1,3,6,1,4,1,27514,1,1,10,2,64,1,1,4,1,4),_QtechAnchorACIPaddrIPv6_Type())
qtechAnchorACIPaddrIPv6.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechAnchorACIPaddrIPv6.setStatus(_A)
_QtechMobilityACPing_Type=IpAddress
_QtechMobilityACPing_Object=MibScalar
qtechMobilityACPing=_QtechMobilityACPing_Object((1,3,6,1,4,1,27514,1,1,10,2,64,1,1,5),_QtechMobilityACPing_Type())
qtechMobilityACPing.setMaxAccess(_E)
if mibBuilder.loadTexts:qtechMobilityACPing.setStatus(_A)
_QtechGlobalHandoffRequestsReceived_Type=Integer32
_QtechGlobalHandoffRequestsReceived_Object=MibScalar
qtechGlobalHandoffRequestsReceived=_QtechGlobalHandoffRequestsReceived_Object((1,3,6,1,4,1,27514,1,1,10,2,64,1,1,6),_QtechGlobalHandoffRequestsReceived_Type())
qtechGlobalHandoffRequestsReceived.setMaxAccess(_E)
if mibBuilder.loadTexts:qtechGlobalHandoffRequestsReceived.setStatus(_A)
_QtechGlobalHandoffEndRequestsReceived_Type=Integer32
_QtechGlobalHandoffEndRequestsReceived_Object=MibScalar
qtechGlobalHandoffEndRequestsReceived=_QtechGlobalHandoffEndRequestsReceived_Object((1,3,6,1,4,1,27514,1,1,10,2,64,1,1,7),_QtechGlobalHandoffEndRequestsReceived_Type())
qtechGlobalHandoffEndRequestsReceived.setMaxAccess(_E)
if mibBuilder.loadTexts:qtechGlobalHandoffEndRequestsReceived.setStatus(_A)
_QtechGlobalStateTransitionsDisabled_Type=Integer32
_QtechGlobalStateTransitionsDisabled_Object=MibScalar
qtechGlobalStateTransitionsDisabled=_QtechGlobalStateTransitionsDisabled_Object((1,3,6,1,4,1,27514,1,1,10,2,64,1,1,8),_QtechGlobalStateTransitionsDisabled_Type())
qtechGlobalStateTransitionsDisabled.setMaxAccess(_E)
if mibBuilder.loadTexts:qtechGlobalStateTransitionsDisabled.setStatus(_A)
_QtechGlobalResourceUnavailable_Type=Integer32
_QtechGlobalResourceUnavailable_Object=MibScalar
qtechGlobalResourceUnavailable=_QtechGlobalResourceUnavailable_Object((1,3,6,1,4,1,27514,1,1,10,2,64,1,1,9),_QtechGlobalResourceUnavailable_Type())
qtechGlobalResourceUnavailable.setMaxAccess(_E)
if mibBuilder.loadTexts:qtechGlobalResourceUnavailable.setStatus(_A)
_QtechRespondeHandoffRequestIgnored_Type=Integer32
_QtechRespondeHandoffRequestIgnored_Object=MibScalar
qtechRespondeHandoffRequestIgnored=_QtechRespondeHandoffRequestIgnored_Object((1,3,6,1,4,1,27514,1,1,10,2,64,1,1,10),_QtechRespondeHandoffRequestIgnored_Type())
qtechRespondeHandoffRequestIgnored.setMaxAccess(_E)
if mibBuilder.loadTexts:qtechRespondeHandoffRequestIgnored.setStatus(_A)
_QtechRespondePingPongHandoffRequestsDropped_Type=Integer32
_QtechRespondePingPongHandoffRequestsDropped_Object=MibScalar
qtechRespondePingPongHandoffRequestsDropped=_QtechRespondePingPongHandoffRequestsDropped_Object((1,3,6,1,4,1,27514,1,1,10,2,64,1,1,11),_QtechRespondePingPongHandoffRequestsDropped_Type())
qtechRespondePingPongHandoffRequestsDropped.setMaxAccess(_E)
if mibBuilder.loadTexts:qtechRespondePingPongHandoffRequestsDropped.setStatus(_A)
_QtechRespondeHandoffRequestsDroped_Type=Integer32
_QtechRespondeHandoffRequestsDroped_Object=MibScalar
qtechRespondeHandoffRequestsDroped=_QtechRespondeHandoffRequestsDroped_Object((1,3,6,1,4,1,27514,1,1,10,2,64,1,1,12),_QtechRespondeHandoffRequestsDroped_Type())
qtechRespondeHandoffRequestsDroped.setMaxAccess(_E)
if mibBuilder.loadTexts:qtechRespondeHandoffRequestsDroped.setStatus(_A)
_QtechRespondeHandoffRequestsDenied_Type=Integer32
_QtechRespondeHandoffRequestsDenied_Object=MibScalar
qtechRespondeHandoffRequestsDenied=_QtechRespondeHandoffRequestsDenied_Object((1,3,6,1,4,1,27514,1,1,10,2,64,1,1,13),_QtechRespondeHandoffRequestsDenied_Type())
qtechRespondeHandoffRequestsDenied.setMaxAccess(_E)
if mibBuilder.loadTexts:qtechRespondeHandoffRequestsDenied.setStatus(_A)
_QtechRespondeClientHandoffasLocal_Type=Integer32
_QtechRespondeClientHandoffasLocal_Object=MibScalar
qtechRespondeClientHandoffasLocal=_QtechRespondeClientHandoffasLocal_Object((1,3,6,1,4,1,27514,1,1,10,2,64,1,1,14),_QtechRespondeClientHandoffasLocal_Type())
qtechRespondeClientHandoffasLocal.setMaxAccess(_E)
if mibBuilder.loadTexts:qtechRespondeClientHandoffasLocal.setStatus(_A)
_QtechRespondeClientHandoffasForeign_Type=Integer32
_QtechRespondeClientHandoffasForeign_Object=MibScalar
qtechRespondeClientHandoffasForeign=_QtechRespondeClientHandoffasForeign_Object((1,3,6,1,4,1,27514,1,1,10,2,64,1,1,15),_QtechRespondeClientHandoffasForeign_Type())
qtechRespondeClientHandoffasForeign.setMaxAccess(_E)
if mibBuilder.loadTexts:qtechRespondeClientHandoffasForeign.setStatus(_A)
_QtechRespondeAnchorRequestsReceived_Type=Integer32
_QtechRespondeAnchorRequestsReceived_Object=MibScalar
qtechRespondeAnchorRequestsReceived=_QtechRespondeAnchorRequestsReceived_Object((1,3,6,1,4,1,27514,1,1,10,2,64,1,1,16),_QtechRespondeAnchorRequestsReceived_Type())
qtechRespondeAnchorRequestsReceived.setMaxAccess(_E)
if mibBuilder.loadTexts:qtechRespondeAnchorRequestsReceived.setStatus(_A)
_QtechRespondeAnchorRequestDenied_Type=Integer32
_QtechRespondeAnchorRequestDenied_Object=MibScalar
qtechRespondeAnchorRequestDenied=_QtechRespondeAnchorRequestDenied_Object((1,3,6,1,4,1,27514,1,1,10,2,64,1,1,17),_QtechRespondeAnchorRequestDenied_Type())
qtechRespondeAnchorRequestDenied.setMaxAccess(_E)
if mibBuilder.loadTexts:qtechRespondeAnchorRequestDenied.setStatus(_A)
_QtechRespondeAnchorTransferred_Type=Integer32
_QtechRespondeAnchorTransferred_Object=MibScalar
qtechRespondeAnchorTransferred=_QtechRespondeAnchorTransferred_Object((1,3,6,1,4,1,27514,1,1,10,2,64,1,1,18),_QtechRespondeAnchorTransferred_Type())
qtechRespondeAnchorTransferred.setMaxAccess(_E)
if mibBuilder.loadTexts:qtechRespondeAnchorTransferred.setStatus(_A)
_QtechInitHandoffRequestsSent_Type=Integer32
_QtechInitHandoffRequestsSent_Object=MibScalar
qtechInitHandoffRequestsSent=_QtechInitHandoffRequestsSent_Object((1,3,6,1,4,1,27514,1,1,10,2,64,1,1,19),_QtechInitHandoffRequestsSent_Type())
qtechInitHandoffRequestsSent.setMaxAccess(_E)
if mibBuilder.loadTexts:qtechInitHandoffRequestsSent.setStatus(_A)
_QtechInitHandoffReplyReceived_Type=Integer32
_QtechInitHandoffReplyReceived_Object=MibScalar
qtechInitHandoffReplyReceived=_QtechInitHandoffReplyReceived_Object((1,3,6,1,4,1,27514,1,1,10,2,64,1,1,20),_QtechInitHandoffReplyReceived_Type())
qtechInitHandoffReplyReceived.setMaxAccess(_E)
if mibBuilder.loadTexts:qtechInitHandoffReplyReceived.setStatus(_A)
_QtechInitHandoffasLocalReceived_Type=Integer32
_QtechInitHandoffasLocalReceived_Object=MibScalar
qtechInitHandoffasLocalReceived=_QtechInitHandoffasLocalReceived_Object((1,3,6,1,4,1,27514,1,1,10,2,64,1,1,21),_QtechInitHandoffasLocalReceived_Type())
qtechInitHandoffasLocalReceived.setMaxAccess(_E)
if mibBuilder.loadTexts:qtechInitHandoffasLocalReceived.setStatus(_A)
_QtechInitHandoffasForeignReceived_Type=Integer32
_QtechInitHandoffasForeignReceived_Object=MibScalar
qtechInitHandoffasForeignReceived=_QtechInitHandoffasForeignReceived_Object((1,3,6,1,4,1,27514,1,1,10,2,64,1,1,22),_QtechInitHandoffasForeignReceived_Type())
qtechInitHandoffasForeignReceived.setMaxAccess(_E)
if mibBuilder.loadTexts:qtechInitHandoffasForeignReceived.setStatus(_A)
_QtechInitHandoffDenyReceived_Type=Integer32
_QtechInitHandoffDenyReceived_Object=MibScalar
qtechInitHandoffDenyReceived=_QtechInitHandoffDenyReceived_Object((1,3,6,1,4,1,27514,1,1,10,2,64,1,1,23),_QtechInitHandoffDenyReceived_Type())
qtechInitHandoffDenyReceived.setMaxAccess(_E)
if mibBuilder.loadTexts:qtechInitHandoffDenyReceived.setStatus(_A)
_QtechInitAnchorRequestSent_Type=Integer32
_QtechInitAnchorRequestSent_Object=MibScalar
qtechInitAnchorRequestSent=_QtechInitAnchorRequestSent_Object((1,3,6,1,4,1,27514,1,1,10,2,64,1,1,24),_QtechInitAnchorRequestSent_Type())
qtechInitAnchorRequestSent.setMaxAccess(_E)
if mibBuilder.loadTexts:qtechInitAnchorRequestSent.setStatus(_A)
_QtechInitAnchorDenyReceived_Type=Integer32
_QtechInitAnchorDenyReceived_Object=MibScalar
qtechInitAnchorDenyReceived=_QtechInitAnchorDenyReceived_Object((1,3,6,1,4,1,27514,1,1,10,2,64,1,1,25),_QtechInitAnchorDenyReceived_Type())
qtechInitAnchorDenyReceived.setMaxAccess(_E)
if mibBuilder.loadTexts:qtechInitAnchorDenyReceived.setStatus(_A)
_QtechAPPriorityEnable_Type=Integer32
_QtechAPPriorityEnable_Object=MibScalar
qtechAPPriorityEnable=_QtechAPPriorityEnable_Object((1,3,6,1,4,1,27514,1,1,10,2,64,1,1,26),_QtechAPPriorityEnable_Type())
qtechAPPriorityEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:qtechAPPriorityEnable.setStatus(_A)
_QtechPrimaryBackUpACIP_Type=IpAddress
_QtechPrimaryBackUpACIP_Object=MibScalar
qtechPrimaryBackUpACIP=_QtechPrimaryBackUpACIP_Object((1,3,6,1,4,1,27514,1,1,10,2,64,1,1,27),_QtechPrimaryBackUpACIP_Type())
qtechPrimaryBackUpACIP.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechPrimaryBackUpACIP.setStatus(_A)
_QtechPrimaryBackUpACName_Type=DisplayString
_QtechPrimaryBackUpACName_Object=MibScalar
qtechPrimaryBackUpACName=_QtechPrimaryBackUpACName_Object((1,3,6,1,4,1,27514,1,1,10,2,64,1,1,28),_QtechPrimaryBackUpACName_Type())
qtechPrimaryBackUpACName.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechPrimaryBackUpACName.setStatus(_A)
_QtechSecondaryBackUpACIP_Type=IpAddress
_QtechSecondaryBackUpACIP_Object=MibScalar
qtechSecondaryBackUpACIP=_QtechSecondaryBackUpACIP_Object((1,3,6,1,4,1,27514,1,1,10,2,64,1,1,29),_QtechSecondaryBackUpACIP_Type())
qtechSecondaryBackUpACIP.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechSecondaryBackUpACIP.setStatus(_A)
_QtechSecondaryBackUpACName_Type=DisplayString
_QtechSecondaryBackUpACName_Object=MibScalar
qtechSecondaryBackUpACName=_QtechSecondaryBackUpACName_Object((1,3,6,1,4,1,27514,1,1,10,2,64,1,1,30),_QtechSecondaryBackUpACName_Type())
qtechSecondaryBackUpACName.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechSecondaryBackUpACName.setStatus(_A)
_QtechTeriaryBackUpACip_Type=IpAddress
_QtechTeriaryBackUpACip_Object=MibScalar
qtechTeriaryBackUpACip=_QtechTeriaryBackUpACip_Object((1,3,6,1,4,1,27514,1,1,10,2,64,1,1,31),_QtechTeriaryBackUpACip_Type())
qtechTeriaryBackUpACip.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechTeriaryBackUpACip.setStatus(_A)
_QtechTeriaryBackUpACName_Type=DisplayString
_QtechTeriaryBackUpACName_Object=MibScalar
qtechTeriaryBackUpACName=_QtechTeriaryBackUpACName_Object((1,3,6,1,4,1,27514,1,1,10,2,64,1,1,32),_QtechTeriaryBackUpACName_Type())
qtechTeriaryBackUpACName.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechTeriaryBackUpACName.setStatus(_A)
_QtechACIntraRoam_Type=Counter32
_QtechACIntraRoam_Object=MibScalar
qtechACIntraRoam=_QtechACIntraRoam_Object((1,3,6,1,4,1,27514,1,1,10,2,64,1,1,33),_QtechACIntraRoam_Type())
qtechACIntraRoam.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechACIntraRoam.setStatus(_A)
_QtechACInterRoamIn_Type=Counter32
_QtechACInterRoamIn_Object=MibScalar
qtechACInterRoamIn=_QtechACInterRoamIn_Object((1,3,6,1,4,1,27514,1,1,10,2,64,1,1,34),_QtechACInterRoamIn_Type())
qtechACInterRoamIn.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechACInterRoamIn.setStatus(_A)
_QtechACInterRoamOut_Type=Counter32
_QtechACInterRoamOut_Object=MibScalar
qtechACInterRoamOut=_QtechACInterRoamOut_Object((1,3,6,1,4,1,27514,1,1,10,2,64,1,1,35),_QtechACInterRoamOut_Type())
qtechACInterRoamOut.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechACInterRoamOut.setStatus(_A)
_QtechMobilityACPingIPv6_Type=Ipv6Address
_QtechMobilityACPingIPv6_Object=MibScalar
qtechMobilityACPingIPv6=_QtechMobilityACPingIPv6_Object((1,3,6,1,4,1,27514,1,1,10,2,64,1,1,36),_QtechMobilityACPingIPv6_Type())
qtechMobilityACPingIPv6.setMaxAccess(_E)
if mibBuilder.loadTexts:qtechMobilityACPingIPv6.setStatus(_A)
_QtechMobilityIPv6MemberEntryTable_Object=MibTable
qtechMobilityIPv6MemberEntryTable=_QtechMobilityIPv6MemberEntryTable_Object((1,3,6,1,4,1,27514,1,1,10,2,64,1,1,37))
if mibBuilder.loadTexts:qtechMobilityIPv6MemberEntryTable.setStatus(_A)
_QtechMobilityIPv6MemberEntry_Object=MibTableRow
qtechMobilityIPv6MemberEntry=_QtechMobilityIPv6MemberEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,64,1,1,37,1))
qtechMobilityIPv6MemberEntry.setIndexNames((0,_B,_H),(0,_B,_I))
if mibBuilder.loadTexts:qtechMobilityIPv6MemberEntry.setStatus(_A)
class _QtechRoamIPv6MemberGroupId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,8))
_QtechRoamIPv6MemberGroupId_Type.__name__=_F
_QtechRoamIPv6MemberGroupId_Object=MibTableColumn
qtechRoamIPv6MemberGroupId=_QtechRoamIPv6MemberGroupId_Object((1,3,6,1,4,1,27514,1,1,10,2,64,1,1,37,1,1),_QtechRoamIPv6MemberGroupId_Type())
qtechRoamIPv6MemberGroupId.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechRoamIPv6MemberGroupId.setStatus(_A)
_QtechRoamIPv6MemberPeerAddress_Type=Ipv6Address
_QtechRoamIPv6MemberPeerAddress_Object=MibTableColumn
qtechRoamIPv6MemberPeerAddress=_QtechRoamIPv6MemberPeerAddress_Object((1,3,6,1,4,1,27514,1,1,10,2,64,1,1,37,1,2),_QtechRoamIPv6MemberPeerAddress_Type())
qtechRoamIPv6MemberPeerAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechRoamIPv6MemberPeerAddress.setStatus(_A)
class _QtechRoamIPv6MemberIsList_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_QtechRoamIPv6MemberIsList_Type.__name__=_F
_QtechRoamIPv6MemberIsList_Object=MibTableColumn
qtechRoamIPv6MemberIsList=_QtechRoamIPv6MemberIsList_Object((1,3,6,1,4,1,27514,1,1,10,2,64,1,1,37,1,3),_QtechRoamIPv6MemberIsList_Type())
qtechRoamIPv6MemberIsList.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechRoamIPv6MemberIsList.setStatus(_A)
class _QtechRoamIPv6MemberDataChannelIsOK_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_QtechRoamIPv6MemberDataChannelIsOK_Type.__name__=_F
_QtechRoamIPv6MemberDataChannelIsOK_Object=MibTableColumn
qtechRoamIPv6MemberDataChannelIsOK=_QtechRoamIPv6MemberDataChannelIsOK_Object((1,3,6,1,4,1,27514,1,1,10,2,64,1,1,37,1,4),_QtechRoamIPv6MemberDataChannelIsOK_Type())
qtechRoamIPv6MemberDataChannelIsOK.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechRoamIPv6MemberDataChannelIsOK.setStatus(_A)
_QtechRoamIPv6MemberDataChannelFailTimes_Type=Integer32
_QtechRoamIPv6MemberDataChannelFailTimes_Object=MibTableColumn
qtechRoamIPv6MemberDataChannelFailTimes=_QtechRoamIPv6MemberDataChannelFailTimes_Object((1,3,6,1,4,1,27514,1,1,10,2,64,1,1,37,1,5),_QtechRoamIPv6MemberDataChannelFailTimes_Type())
qtechRoamIPv6MemberDataChannelFailTimes.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechRoamIPv6MemberDataChannelFailTimes.setStatus(_A)
_QtechRoamIPv6MemberDTLSIsClient_Type=Integer32
_QtechRoamIPv6MemberDTLSIsClient_Object=MibTableColumn
qtechRoamIPv6MemberDTLSIsClient=_QtechRoamIPv6MemberDTLSIsClient_Object((1,3,6,1,4,1,27514,1,1,10,2,64,1,1,37,1,6),_QtechRoamIPv6MemberDTLSIsClient_Type())
qtechRoamIPv6MemberDTLSIsClient.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechRoamIPv6MemberDTLSIsClient.setStatus(_A)
class _QtechRoamIPv6MemberDTLSIsOK_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_QtechRoamIPv6MemberDTLSIsOK_Type.__name__=_F
_QtechRoamIPv6MemberDTLSIsOK_Object=MibTableColumn
qtechRoamIPv6MemberDTLSIsOK=_QtechRoamIPv6MemberDTLSIsOK_Object((1,3,6,1,4,1,27514,1,1,10,2,64,1,1,37,1,7),_QtechRoamIPv6MemberDTLSIsOK_Type())
qtechRoamIPv6MemberDTLSIsOK.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechRoamIPv6MemberDTLSIsOK.setStatus(_A)
_QtechRoamIPv6MemberCreateStatus_Type=RowStatus
_QtechRoamIPv6MemberCreateStatus_Object=MibTableColumn
qtechRoamIPv6MemberCreateStatus=_QtechRoamIPv6MemberCreateStatus_Object((1,3,6,1,4,1,27514,1,1,10,2,64,1,1,37,1,8),_QtechRoamIPv6MemberCreateStatus_Type())
qtechRoamIPv6MemberCreateStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechRoamIPv6MemberCreateStatus.setStatus(_A)
_QtechMobilityUserEntryTable_Object=MibTable
qtechMobilityUserEntryTable=_QtechMobilityUserEntryTable_Object((1,3,6,1,4,1,27514,1,1,10,2,64,1,1,38))
if mibBuilder.loadTexts:qtechMobilityUserEntryTable.setStatus(_A)
_QtechMobilityUserEntry_Object=MibTableRow
qtechMobilityUserEntry=_QtechMobilityUserEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,64,1,1,38,1))
qtechMobilityUserEntry.setIndexNames((0,_B,_J))
if mibBuilder.loadTexts:qtechMobilityUserEntry.setStatus(_A)
_QtechRoamUserMac_Type=MacAddress
_QtechRoamUserMac_Object=MibTableColumn
qtechRoamUserMac=_QtechRoamUserMac_Object((1,3,6,1,4,1,27514,1,1,10,2,64,1,1,38,1,1),_QtechRoamUserMac_Type())
qtechRoamUserMac.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechRoamUserMac.setStatus(_A)
_QtechRoamUserRoamType_Type=Integer32
_QtechRoamUserRoamType_Object=MibTableColumn
qtechRoamUserRoamType=_QtechRoamUserRoamType_Object((1,3,6,1,4,1,27514,1,1,10,2,64,1,1,38,1,2),_QtechRoamUserRoamType_Type())
qtechRoamUserRoamType.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechRoamUserRoamType.setStatus(_A)
_QtechRoamUserRoamOutAcAddressType_Type=InetAddressType
_QtechRoamUserRoamOutAcAddressType_Object=MibTableColumn
qtechRoamUserRoamOutAcAddressType=_QtechRoamUserRoamOutAcAddressType_Object((1,3,6,1,4,1,27514,1,1,10,2,64,1,1,38,1,3),_QtechRoamUserRoamOutAcAddressType_Type())
qtechRoamUserRoamOutAcAddressType.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechRoamUserRoamOutAcAddressType.setStatus(_A)
_QtechRoamUserRoamOutAcAddress_Type=InetAddress
_QtechRoamUserRoamOutAcAddress_Object=MibTableColumn
qtechRoamUserRoamOutAcAddress=_QtechRoamUserRoamOutAcAddress_Object((1,3,6,1,4,1,27514,1,1,10,2,64,1,1,38,1,4),_QtechRoamUserRoamOutAcAddress_Type())
qtechRoamUserRoamOutAcAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechRoamUserRoamOutAcAddress.setStatus(_A)
_QtechRoamUserRoamInAcAddressType_Type=InetAddressType
_QtechRoamUserRoamInAcAddressType_Object=MibTableColumn
qtechRoamUserRoamInAcAddressType=_QtechRoamUserRoamInAcAddressType_Object((1,3,6,1,4,1,27514,1,1,10,2,64,1,1,38,1,5),_QtechRoamUserRoamInAcAddressType_Type())
qtechRoamUserRoamInAcAddressType.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechRoamUserRoamInAcAddressType.setStatus(_A)
_QtechRoamUserRoamInAcAddress_Type=InetAddress
_QtechRoamUserRoamInAcAddress_Object=MibTableColumn
qtechRoamUserRoamInAcAddress=_QtechRoamUserRoamInAcAddress_Object((1,3,6,1,4,1,27514,1,1,10,2,64,1,1,38,1,6),_QtechRoamUserRoamInAcAddress_Type())
qtechRoamUserRoamInAcAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechRoamUserRoamInAcAddress.setStatus(_A)
_QtechRoamUserRoamOutApMac_Type=MacAddress
_QtechRoamUserRoamOutApMac_Object=MibTableColumn
qtechRoamUserRoamOutApMac=_QtechRoamUserRoamOutApMac_Object((1,3,6,1,4,1,27514,1,1,10,2,64,1,1,38,1,7),_QtechRoamUserRoamOutApMac_Type())
qtechRoamUserRoamOutApMac.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechRoamUserRoamOutApMac.setStatus(_A)
_QtechRoamUserRoamInApMac_Type=MacAddress
_QtechRoamUserRoamInApMac_Object=MibTableColumn
qtechRoamUserRoamInApMac=_QtechRoamUserRoamInApMac_Object((1,3,6,1,4,1,27514,1,1,10,2,64,1,1,38,1,8),_QtechRoamUserRoamInApMac_Type())
qtechRoamUserRoamInApMac.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechRoamUserRoamInApMac.setStatus(_A)
_QtechRoamUserRoamOutVid_Type=Integer32
_QtechRoamUserRoamOutVid_Object=MibTableColumn
qtechRoamUserRoamOutVid=_QtechRoamUserRoamOutVid_Object((1,3,6,1,4,1,27514,1,1,10,2,64,1,1,38,1,9),_QtechRoamUserRoamOutVid_Type())
qtechRoamUserRoamOutVid.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechRoamUserRoamOutVid.setStatus(_A)
_QtechRoamUserRoamInVid_Type=Integer32
_QtechRoamUserRoamInVid_Object=MibTableColumn
qtechRoamUserRoamInVid=_QtechRoamUserRoamInVid_Object((1,3,6,1,4,1,27514,1,1,10,2,64,1,1,38,1,10),_QtechRoamUserRoamInVid_Type())
qtechRoamUserRoamInVid.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechRoamUserRoamInVid.setStatus(_A)
_QtechMobilityTrackEntryTable_Object=MibTable
qtechMobilityTrackEntryTable=_QtechMobilityTrackEntryTable_Object((1,3,6,1,4,1,27514,1,1,10,2,64,1,1,39))
if mibBuilder.loadTexts:qtechMobilityTrackEntryTable.setStatus(_A)
_QtechMobilityTrackEntry_Object=MibTableRow
qtechMobilityTrackEntry=_QtechMobilityTrackEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,64,1,1,39,1))
qtechMobilityTrackEntry.setIndexNames((0,_B,_K),(0,_B,_L))
if mibBuilder.loadTexts:qtechMobilityTrackEntry.setStatus(_A)
_QtechRoamTrackStaMac_Type=MacAddress
_QtechRoamTrackStaMac_Object=MibTableColumn
qtechRoamTrackStaMac=_QtechRoamTrackStaMac_Object((1,3,6,1,4,1,27514,1,1,10,2,64,1,1,39,1,1),_QtechRoamTrackStaMac_Type())
qtechRoamTrackStaMac.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechRoamTrackStaMac.setStatus(_A)
_QtechRoamTrackId_Type=Integer32
_QtechRoamTrackId_Object=MibTableColumn
qtechRoamTrackId=_QtechRoamTrackId_Object((1,3,6,1,4,1,27514,1,1,10,2,64,1,1,39,1,2),_QtechRoamTrackId_Type())
qtechRoamTrackId.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechRoamTrackId.setStatus(_A)
_QtechRoamTrackAcAddressType_Type=InetAddressType
_QtechRoamTrackAcAddressType_Object=MibTableColumn
qtechRoamTrackAcAddressType=_QtechRoamTrackAcAddressType_Object((1,3,6,1,4,1,27514,1,1,10,2,64,1,1,39,1,3),_QtechRoamTrackAcAddressType_Type())
qtechRoamTrackAcAddressType.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechRoamTrackAcAddressType.setStatus(_A)
_QtechRoamTrackAcAddress_Type=InetAddress
_QtechRoamTrackAcAddress_Object=MibTableColumn
qtechRoamTrackAcAddress=_QtechRoamTrackAcAddress_Object((1,3,6,1,4,1,27514,1,1,10,2,64,1,1,39,1,4),_QtechRoamTrackAcAddress_Type())
qtechRoamTrackAcAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechRoamTrackAcAddress.setStatus(_A)
_QtechRoamTrackApMac_Type=MacAddress
_QtechRoamTrackApMac_Object=MibTableColumn
qtechRoamTrackApMac=_QtechRoamTrackApMac_Object((1,3,6,1,4,1,27514,1,1,10,2,64,1,1,39,1,5),_QtechRoamTrackApMac_Type())
qtechRoamTrackApMac.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechRoamTrackApMac.setStatus(_A)
_QtechRoamTrackRadioId_Type=Integer32
_QtechRoamTrackRadioId_Object=MibTableColumn
qtechRoamTrackRadioId=_QtechRoamTrackRadioId_Object((1,3,6,1,4,1,27514,1,1,10,2,64,1,1,39,1,6),_QtechRoamTrackRadioId_Type())
qtechRoamTrackRadioId.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechRoamTrackRadioId.setStatus(_A)
_QtechRoamTrackStaIp_Type=IpAddress
_QtechRoamTrackStaIp_Object=MibTableColumn
qtechRoamTrackStaIp=_QtechRoamTrackStaIp_Object((1,3,6,1,4,1,27514,1,1,10,2,64,1,1,39,1,7),_QtechRoamTrackStaIp_Type())
qtechRoamTrackStaIp.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechRoamTrackStaIp.setStatus(_A)
_QtechRoamTrackStaIpv6_Type=Ipv6Address
_QtechRoamTrackStaIpv6_Object=MibTableColumn
qtechRoamTrackStaIpv6=_QtechRoamTrackStaIpv6_Object((1,3,6,1,4,1,27514,1,1,10,2,64,1,1,39,1,8),_QtechRoamTrackStaIpv6_Type())
qtechRoamTrackStaIpv6.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechRoamTrackStaIpv6.setStatus(_A)
_QtechRoamTrackStaOnlineTime_Type=Integer32
_QtechRoamTrackStaOnlineTime_Object=MibTableColumn
qtechRoamTrackStaOnlineTime=_QtechRoamTrackStaOnlineTime_Object((1,3,6,1,4,1,27514,1,1,10,2,64,1,1,39,1,9),_QtechRoamTrackStaOnlineTime_Type())
qtechRoamTrackStaOnlineTime.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechRoamTrackStaOnlineTime.setStatus(_A)
_QtechMobilityIf_ObjectIdentity=ObjectIdentity
qtechMobilityIf=_QtechMobilityIf_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,64,1,2))
_QtechMobilityMIBCompliances_ObjectIdentity=ObjectIdentity
qtechMobilityMIBCompliances=_QtechMobilityMIBCompliances_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,64,1,2,1))
_QtechMobilityMIBGroups_ObjectIdentity=ObjectIdentity
qtechMobilityMIBGroups=_QtechMobilityMIBGroups_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,64,1,2,2))
_QtechMobilityTrap_ObjectIdentity=ObjectIdentity
qtechMobilityTrap=_QtechMobilityTrap_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,64,1,3))
_QtechMobilityTrapSta_ObjectIdentity=ObjectIdentity
qtechMobilityTrapSta=_QtechMobilityTrapSta_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,64,1,3,1))
_QtechMobilityNotifyApMac_Type=MacAddress
_QtechMobilityNotifyApMac_Object=MibScalar
qtechMobilityNotifyApMac=_QtechMobilityNotifyApMac_Object((1,3,6,1,4,1,27514,1,1,10,2,64,1,3,1,1),_QtechMobilityNotifyApMac_Type())
qtechMobilityNotifyApMac.setMaxAccess(_G)
if mibBuilder.loadTexts:qtechMobilityNotifyApMac.setStatus(_A)
_QtechMobilityNotifyStaMac_Type=MacAddress
_QtechMobilityNotifyStaMac_Object=MibScalar
qtechMobilityNotifyStaMac=_QtechMobilityNotifyStaMac_Object((1,3,6,1,4,1,27514,1,1,10,2,64,1,3,1,2),_QtechMobilityNotifyStaMac_Type())
qtechMobilityNotifyStaMac.setMaxAccess(_G)
if mibBuilder.loadTexts:qtechMobilityNotifyStaMac.setStatus(_A)
_QtechMobilityNotifyApIp_Type=IpAddress
_QtechMobilityNotifyApIp_Object=MibScalar
qtechMobilityNotifyApIp=_QtechMobilityNotifyApIp_Object((1,3,6,1,4,1,27514,1,1,10,2,64,1,3,1,3),_QtechMobilityNotifyApIp_Type())
qtechMobilityNotifyApIp.setMaxAccess(_G)
if mibBuilder.loadTexts:qtechMobilityNotifyApIp.setStatus(_A)
_QtechMobilityNotifyStaIp_Type=IpAddress
_QtechMobilityNotifyStaIp_Object=MibScalar
qtechMobilityNotifyStaIp=_QtechMobilityNotifyStaIp_Object((1,3,6,1,4,1,27514,1,1,10,2,64,1,3,1,4),_QtechMobilityNotifyStaIp_Type())
qtechMobilityNotifyStaIp.setMaxAccess(_G)
if mibBuilder.loadTexts:qtechMobilityNotifyStaIp.setStatus(_A)
_QtechMobilityNotifyStaOperType_Type=Integer32
_QtechMobilityNotifyStaOperType_Object=MibScalar
qtechMobilityNotifyStaOperType=_QtechMobilityNotifyStaOperType_Object((1,3,6,1,4,1,27514,1,1,10,2,64,1,3,1,5),_QtechMobilityNotifyStaOperType_Type())
qtechMobilityNotifyStaOperType.setMaxAccess(_G)
if mibBuilder.loadTexts:qtechMobilityNotifyStaOperType.setStatus(_A)
class _QtechMobilityNotifyStaApRadioId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_QtechMobilityNotifyStaApRadioId_Type.__name__=_F
_QtechMobilityNotifyStaApRadioId_Object=MibScalar
qtechMobilityNotifyStaApRadioId=_QtechMobilityNotifyStaApRadioId_Object((1,3,6,1,4,1,27514,1,1,10,2,64,1,3,1,6),_QtechMobilityNotifyStaApRadioId_Type())
qtechMobilityNotifyStaApRadioId.setMaxAccess(_G)
if mibBuilder.loadTexts:qtechMobilityNotifyStaApRadioId.setStatus(_A)
class _QtechMobilityNotifyStaApRadioType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_QtechMobilityNotifyStaApRadioType_Type.__name__=_F
_QtechMobilityNotifyStaApRadioType_Object=MibScalar
qtechMobilityNotifyStaApRadioType=_QtechMobilityNotifyStaApRadioType_Object((1,3,6,1,4,1,27514,1,1,10,2,64,1,3,1,7),_QtechMobilityNotifyStaApRadioType_Type())
qtechMobilityNotifyStaApRadioType.setMaxAccess(_G)
if mibBuilder.loadTexts:qtechMobilityNotifyStaApRadioType.setStatus(_A)
class _QtechMobilityNotifyStaVlanId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_QtechMobilityNotifyStaVlanId_Type.__name__=_F
_QtechMobilityNotifyStaVlanId_Object=MibScalar
qtechMobilityNotifyStaVlanId=_QtechMobilityNotifyStaVlanId_Object((1,3,6,1,4,1,27514,1,1,10,2,64,1,3,1,8),_QtechMobilityNotifyStaVlanId_Type())
qtechMobilityNotifyStaVlanId.setMaxAccess(_G)
if mibBuilder.loadTexts:qtechMobilityNotifyStaVlanId.setStatus(_A)
class _QtechMobilityNotifyStaWlanId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_QtechMobilityNotifyStaWlanId_Type.__name__=_F
_QtechMobilityNotifyStaWlanId_Object=MibScalar
qtechMobilityNotifyStaWlanId=_QtechMobilityNotifyStaWlanId_Object((1,3,6,1,4,1,27514,1,1,10,2,64,1,3,1,9),_QtechMobilityNotifyStaWlanId_Type())
qtechMobilityNotifyStaWlanId.setMaxAccess(_G)
if mibBuilder.loadTexts:qtechMobilityNotifyStaWlanId.setStatus(_A)
_QtechMobilityNotifyStaIpv6_Type=Ipv6Address
_QtechMobilityNotifyStaIpv6_Object=MibScalar
qtechMobilityNotifyStaIpv6=_QtechMobilityNotifyStaIpv6_Object((1,3,6,1,4,1,27514,1,1,10,2,64,1,3,1,10),_QtechMobilityNotifyStaIpv6_Type())
qtechMobilityNotifyStaIpv6.setMaxAccess(_G)
if mibBuilder.loadTexts:qtechMobilityNotifyStaIpv6.setStatus(_A)
class _QtechMobilityNotifyStaAssoAuthMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('open',0),('wep',1),('dot1x-wep',2),('dot1x-wpa',3),('dot1x-wpa2',4),('mab',5),('psk-wpa',6),('psk-wpa2',7),('wapi',8)))
_QtechMobilityNotifyStaAssoAuthMode_Type.__name__=_F
_QtechMobilityNotifyStaAssoAuthMode_Object=MibScalar
qtechMobilityNotifyStaAssoAuthMode=_QtechMobilityNotifyStaAssoAuthMode_Object((1,3,6,1,4,1,27514,1,1,10,2,64,1,3,1,11),_QtechMobilityNotifyStaAssoAuthMode_Type())
qtechMobilityNotifyStaAssoAuthMode.setMaxAccess(_G)
if mibBuilder.loadTexts:qtechMobilityNotifyStaAssoAuthMode.setStatus(_A)
class _QtechMobilityNotifyStaNetAuthMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('open',0),('web',1)))
_QtechMobilityNotifyStaNetAuthMode_Type.__name__=_F
_QtechMobilityNotifyStaNetAuthMode_Object=MibScalar
qtechMobilityNotifyStaNetAuthMode=_QtechMobilityNotifyStaNetAuthMode_Object((1,3,6,1,4,1,27514,1,1,10,2,64,1,3,1,12),_QtechMobilityNotifyStaNetAuthMode_Type())
qtechMobilityNotifyStaNetAuthMode.setMaxAccess(_G)
if mibBuilder.loadTexts:qtechMobilityNotifyStaNetAuthMode.setStatus(_A)
_QtechMobilityNotifyStaSsid_Type=DisplayString
_QtechMobilityNotifyStaSsid_Object=MibScalar
qtechMobilityNotifyStaSsid=_QtechMobilityNotifyStaSsid_Object((1,3,6,1,4,1,27514,1,1,10,2,64,1,3,1,13),_QtechMobilityNotifyStaSsid_Type())
qtechMobilityNotifyStaSsid.setMaxAccess(_G)
if mibBuilder.loadTexts:qtechMobilityNotifyStaSsid.setStatus(_A)
_QtechMobilityNotifyStaLinkRate_Type=Integer32
_QtechMobilityNotifyStaLinkRate_Object=MibScalar
qtechMobilityNotifyStaLinkRate=_QtechMobilityNotifyStaLinkRate_Object((1,3,6,1,4,1,27514,1,1,10,2,64,1,3,1,14),_QtechMobilityNotifyStaLinkRate_Type())
qtechMobilityNotifyStaLinkRate.setMaxAccess(_G)
if mibBuilder.loadTexts:qtechMobilityNotifyStaLinkRate.setStatus(_A)
_QtechMobilityNotifyStaCurChan_Type=Integer32
_QtechMobilityNotifyStaCurChan_Object=MibScalar
qtechMobilityNotifyStaCurChan=_QtechMobilityNotifyStaCurChan_Object((1,3,6,1,4,1,27514,1,1,10,2,64,1,3,1,15),_QtechMobilityNotifyStaCurChan_Type())
qtechMobilityNotifyStaCurChan.setMaxAccess(_G)
if mibBuilder.loadTexts:qtechMobilityNotifyStaCurChan.setStatus(_A)
_QtechMobilityNotifyStaClientType_Type=DisplayString
_QtechMobilityNotifyStaClientType_Object=MibScalar
qtechMobilityNotifyStaClientType=_QtechMobilityNotifyStaClientType_Object((1,3,6,1,4,1,27514,1,1,10,2,64,1,3,1,16),_QtechMobilityNotifyStaClientType_Type())
qtechMobilityNotifyStaClientType.setMaxAccess(_G)
if mibBuilder.loadTexts:qtechMobilityNotifyStaClientType.setStatus(_A)
_QtechMobilityNotifyStaRssi_Type=Integer32
_QtechMobilityNotifyStaRssi_Object=MibScalar
qtechMobilityNotifyStaRssi=_QtechMobilityNotifyStaRssi_Object((1,3,6,1,4,1,27514,1,1,10,2,64,1,3,1,17),_QtechMobilityNotifyStaRssi_Type())
qtechMobilityNotifyStaRssi.setMaxAccess(_G)
if mibBuilder.loadTexts:qtechMobilityNotifyStaRssi.setStatus(_A)
_QtechMobilityNotifyStaReason_Type=DisplayString
_QtechMobilityNotifyStaReason_Object=MibScalar
qtechMobilityNotifyStaReason=_QtechMobilityNotifyStaReason_Object((1,3,6,1,4,1,27514,1,1,10,2,64,1,3,1,18),_QtechMobilityNotifyStaReason_Type())
qtechMobilityNotifyStaReason.setMaxAccess(_G)
if mibBuilder.loadTexts:qtechMobilityNotifyStaReason.setStatus(_A)
_QtechMobilityTrapStaIf_ObjectIdentity=ObjectIdentity
qtechMobilityTrapStaIf=_QtechMobilityTrapStaIf_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,64,1,3,2))
qtechMobilityMIBGroup=ObjectGroup((1,3,6,1,4,1,27514,1,1,10,2,64,1,2,2,1))
qtechMobilityMIBGroup.setObjects(*((_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_x),(_B,_y),(_B,_z),(_B,_A0),(_B,_A1),(_B,_A2),(_B,_A3),(_B,_A4),(_B,_A5),(_B,_A6),(_B,_A7),(_B,_A8),(_B,_A9),(_B,_AA),(_B,_AB),(_B,_AC),(_B,_AD),(_B,_AE),(_B,_AF),(_B,_AG),(_B,_AH),(_B,_AI),(_B,_AJ),(_B,_H),(_B,_I),(_B,_AK),(_B,_AL),(_B,_AM),(_B,_AN),(_B,_AO),(_B,_AP),(_B,_J),(_B,_AQ),(_B,_AR),(_B,_AS),(_B,_AT),(_B,_AU),(_B,_AV),(_B,_AW),(_B,_AX),(_B,_AY),(_B,_K),(_B,_L),(_B,_AZ),(_B,_Aa),(_B,_Ab),(_B,_Ac),(_B,_Ad),(_B,_Ae),(_B,_Af)))
if mibBuilder.loadTexts:qtechMobilityMIBGroup.setStatus(_A)
qtechMobilityNotifyStaOper=NotificationType((1,3,6,1,4,1,27514,1,1,10,2,64,1,3,2,1))
qtechMobilityNotifyStaOper.setObjects(*((_B,_Ag),(_B,_Ah),(_B,_Ai),(_B,_Aj),(_B,_Ak),(_B,_Al),(_B,_Am),(_B,_An),(_B,_Ao),(_B,_Ap),(_B,_Aq),(_B,_Ar),(_B,_As),(_B,_At),(_B,_Au),(_B,_Av),(_B,_Aw),(_B,_Ax)))
if mibBuilder.loadTexts:qtechMobilityNotifyStaOper.setStatus(_A)
qtechMobilityMIBCompliance=ModuleCompliance((1,3,6,1,4,1,27514,1,1,10,2,64,1,2,1,1))
qtechMobilityMIBCompliance.setObjects((_B,_Ay))
if mibBuilder.loadTexts:qtechMobilityMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'qtechMobilityMIB':qtechMobilityMIB,'qtechMobilityMIBObjects':qtechMobilityMIBObjects,'qtechMobility':qtechMobility,'qtechMobilityEntryTable':qtechMobilityEntryTable,'qtechMobilityEntry':qtechMobilityEntry,_M:qtechRoamGroupId,_R:qtechRoamGroupName,_S:qtechRoamGroupMyAddress,_T:qtechRoamGroupMcEnable,_U:qtechRoamGroupMcAddress,_V:qtechRoamGroupKeepaliveCount,_W:qtechRoamGroupKeepaliveInterval,_X:qtechRoamGroupIsFast,_Y:qtechRoamGroupCreateStatus,'qtechRoamGroupMyAddressIPv6':qtechRoamGroupMyAddressIPv6,'qtechMobilityMemberEntryTable':qtechMobilityMemberEntryTable,'qtechMobilityMemberEntry':qtechMobilityMemberEntry,_N:qtechRoamMemberGroupId,_O:qtechRoamMemberPeerAddress,_Z:qtechRoamMemberIsList,_a:qtechRoamMemberDataChannelIsOK,_b:qtechRoamMemberDataChannelFailTimes,_c:qtechRoamMemberDTLSIsClient,_d:qtechRoamMemberDTLSIsOK,_e:qtechRoamMemberCreateStatus,'qtechAPCtrlCreatEntryTable':qtechAPCtrlCreatEntryTable,'qtechAPCtrlCreatEntry':qtechAPCtrlCreatEntry,_P:qtechAPName,_f:qtechPriority,_g:qtechPrimaryACIP,_h:qtechPrimaryACName,_i:qtechSecondaryACIP,_j:qtechSecondaryACName,_k:qtechTertiaryACIP,_l:qtechTertiaryACName,_m:qtechAPCtrlCreatStatus,'qtechWLANCtrlCreatEntryTable':qtechWLANCtrlCreatEntryTable,'qtechWLANCtrlCreatEntry':qtechWLANCtrlCreatEntry,_Q:qtechWLANID,_n:qtechAnchorACIPaddr,_o:qtechWLANCtrlCreatStatus,'qtechAnchorACIPaddrIPv6':qtechAnchorACIPaddrIPv6,'qtechMobilityACPing':qtechMobilityACPing,_p:qtechGlobalHandoffRequestsReceived,_q:qtechGlobalHandoffEndRequestsReceived,_r:qtechGlobalStateTransitionsDisabled,_s:qtechGlobalResourceUnavailable,_t:qtechRespondeHandoffRequestIgnored,_u:qtechRespondePingPongHandoffRequestsDropped,_v:qtechRespondeHandoffRequestsDroped,_w:qtechRespondeHandoffRequestsDenied,_x:qtechRespondeClientHandoffasLocal,_y:qtechRespondeClientHandoffasForeign,_z:qtechRespondeAnchorRequestsReceived,_A0:qtechRespondeAnchorRequestDenied,_A1:qtechRespondeAnchorTransferred,_A2:qtechInitHandoffRequestsSent,_A3:qtechInitHandoffReplyReceived,_A4:qtechInitHandoffasLocalReceived,_A5:qtechInitHandoffasForeignReceived,_A6:qtechInitHandoffDenyReceived,_A7:qtechInitAnchorRequestSent,_A8:qtechInitAnchorDenyReceived,_A9:qtechAPPriorityEnable,_AA:qtechPrimaryBackUpACIP,_AB:qtechPrimaryBackUpACName,_AC:qtechSecondaryBackUpACIP,_AD:qtechSecondaryBackUpACName,_AE:qtechTeriaryBackUpACip,_AF:qtechTeriaryBackUpACName,_AG:qtechACIntraRoam,_AH:qtechACInterRoamIn,_AI:qtechACInterRoamOut,_AJ:qtechMobilityACPingIPv6,'qtechMobilityIPv6MemberEntryTable':qtechMobilityIPv6MemberEntryTable,'qtechMobilityIPv6MemberEntry':qtechMobilityIPv6MemberEntry,_H:qtechRoamIPv6MemberGroupId,_I:qtechRoamIPv6MemberPeerAddress,_AK:qtechRoamIPv6MemberIsList,_AL:qtechRoamIPv6MemberDataChannelIsOK,_AM:qtechRoamIPv6MemberDataChannelFailTimes,_AN:qtechRoamIPv6MemberDTLSIsClient,_AO:qtechRoamIPv6MemberDTLSIsOK,_AP:qtechRoamIPv6MemberCreateStatus,'qtechMobilityUserEntryTable':qtechMobilityUserEntryTable,'qtechMobilityUserEntry':qtechMobilityUserEntry,_J:qtechRoamUserMac,_AQ:qtechRoamUserRoamType,_AR:qtechRoamUserRoamOutAcAddressType,_AS:qtechRoamUserRoamOutAcAddress,_AT:qtechRoamUserRoamInAcAddressType,_AU:qtechRoamUserRoamInAcAddress,_AV:qtechRoamUserRoamOutApMac,_AW:qtechRoamUserRoamInApMac,_AX:qtechRoamUserRoamOutVid,_AY:qtechRoamUserRoamInVid,'qtechMobilityTrackEntryTable':qtechMobilityTrackEntryTable,'qtechMobilityTrackEntry':qtechMobilityTrackEntry,_K:qtechRoamTrackStaMac,_L:qtechRoamTrackId,_AZ:qtechRoamTrackAcAddressType,_Aa:qtechRoamTrackAcAddress,_Ab:qtechRoamTrackApMac,_Ac:qtechRoamTrackRadioId,_Ad:qtechRoamTrackStaIp,_Ae:qtechRoamTrackStaIpv6,_Af:qtechRoamTrackStaOnlineTime,'qtechMobilityIf':qtechMobilityIf,'qtechMobilityMIBCompliances':qtechMobilityMIBCompliances,'qtechMobilityMIBCompliance':qtechMobilityMIBCompliance,'qtechMobilityMIBGroups':qtechMobilityMIBGroups,_Ay:qtechMobilityMIBGroup,'qtechMobilityTrap':qtechMobilityTrap,'qtechMobilityTrapSta':qtechMobilityTrapSta,_Ag:qtechMobilityNotifyApMac,_Ah:qtechMobilityNotifyStaMac,_Ai:qtechMobilityNotifyApIp,_Aj:qtechMobilityNotifyStaIp,_Ak:qtechMobilityNotifyStaOperType,_Al:qtechMobilityNotifyStaApRadioId,_Am:qtechMobilityNotifyStaApRadioType,_An:qtechMobilityNotifyStaVlanId,_Ao:qtechMobilityNotifyStaWlanId,_Ap:qtechMobilityNotifyStaIpv6,_Aq:qtechMobilityNotifyStaAssoAuthMode,_Ar:qtechMobilityNotifyStaNetAuthMode,_As:qtechMobilityNotifyStaSsid,_At:qtechMobilityNotifyStaLinkRate,_Au:qtechMobilityNotifyStaCurChan,_Av:qtechMobilityNotifyStaClientType,_Aw:qtechMobilityNotifyStaRssi,_Ax:qtechMobilityNotifyStaReason,'qtechMobilityTrapStaIf':qtechMobilityTrapStaIf,'qtechMobilityNotifyStaOper':qtechMobilityNotifyStaOper})