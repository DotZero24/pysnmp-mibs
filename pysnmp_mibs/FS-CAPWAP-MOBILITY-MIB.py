_A_='fsMobilityMIBGroup'
_Az='fsMobilityNotifyStaReason'
_Ay='fsMobilityNotifyStaRssi'
_Ax='fsMobilityNotifyStaClientType'
_Aw='fsMobilityNotifyStaCurChan'
_Av='fsMobilityNotifyStaLinkRate'
_Au='fsMobilityNotifyStaSsid'
_At='fsMobilityNotifyStaNetAuthMode'
_As='fsMobilityNotifyStaAssoAuthMode'
_Ar='fsMobilityNotifyStaIpv6'
_Aq='fsMobilityNotifyStaWlanId'
_Ap='fsMobilityNotifyStaVlanId'
_Ao='fsMobilityNotifyStaApRadioType'
_An='fsMobilityNotifyStaApRadioId'
_Am='fsMobilityNotifyStaOperType'
_Al='fsMobilityNotifyStaIp'
_Ak='fsMobilityNotifyApIp'
_Aj='fsMobilityNotifyStaMac'
_Ai='fsMobilityNotifyApMac'
_Ah='fsRoamTrackStaOnlineTime'
_Ag='fsRoamTrackStaIpv6'
_Af='fsRoamTrackStaIp'
_Ae='fsRoamTrackRadioId'
_Ad='fsRoamTrackApMac'
_Ac='fsRoamTrackAcAddress'
_Ab='fsRoamTrackAcAddressType'
_Aa='fsRoamUserRoamInVid'
_AZ='fsRoamUserRoamOutVid'
_AY='fsRoamUserRoamInApMac'
_AX='fsRoamUserRoamOutApMac'
_AW='fsRoamUserRoamInAcAddress'
_AV='fsRoamUserRoamInAcAddressType'
_AU='fsRoamUserRoamOutAcAddress'
_AT='fsRoamUserRoamOutAcAddressType'
_AS='fsRoamUserRoamType'
_AR='fsRoamIPv6MemberCreateStatus'
_AQ='fsRoamIPv6MemberDTLSIsOK'
_AP='fsRoamIPv6MemberDTLSIsClient'
_AO='fsRoamIPv6MemberDataChannelFailTimes'
_AN='fsRoamIPv6MemberDataChannelIsOK'
_AM='fsRoamIPv6MemberIsList'
_AL='fsMobilityACPingIPv6'
_AK='fsACInterRoamOut'
_AJ='fsACInterRoamIn'
_AI='fsACIntraRoam'
_AH='fsTeriaryBackUpACName'
_AG='fsTeriaryBackUpACip'
_AF='fsSecondaryBackUpACName'
_AE='fsSecondaryBackUpACIP'
_AD='fsPrimaryBackUpACName'
_AC='fsPrimaryBackUpACIP'
_AB='fsAPPriorityEnable'
_AA='fsInitAnchorDenyReceived'
_A9='fsInitAnchorRequestSent'
_A8='fsInitHandoffDenyReceived'
_A7='fsInitHandoffasForeignReceived'
_A6='fsInitHandoffasLocalReceived'
_A5='fsInitHandoffReplyReceived'
_A4='fsInitHandoffRequestsSent'
_A3='fsRespondeAnchorTransferred'
_A2='fsRespondeAnchorRequestDenied'
_A1='fsRespondeAnchorRequestsReceived'
_A0='fsRespondeClientHandoffasForeign'
_z='fsRespondeClientHandoffasLocal'
_y='fsRespondeHandoffRequestsDenied'
_x='fsRespondeHandoffRequestsDroped'
_w='fsRespondePingPongHandoffRequestsDropped'
_v='fsRespondeHandoffRequestIgnored'
_u='fsGlobalResourceUnavailable'
_t='fsGlobalStateTransitionsDisabled'
_s='fsGlobalHandoffEndRequestsReceived'
_r='fsGlobalHandoffRequestsReceived'
_q='fsWLANCtrlCreatStatus'
_p='fsAnchorACIPaddr'
_o='fsAPCtrlCreatStatus'
_n='fsTertiaryACName'
_m='fsTertiaryACIP'
_l='fsSecondaryACName'
_k='fsSecondaryACIP'
_j='fsPrimaryACName'
_i='fsPrimaryACIP'
_h='fsPriority'
_g='fsRoamMemberCreateStatus'
_f='fsRoamMemberDTLSIsOK'
_e='fsRoamMemberDTLSIsClient'
_d='fsRoamMemberDataChannelFailTimes'
_c='fsRoamMemberDataChannelIsOK'
_b='fsRoamMemberIsList'
_a='fsRoamGroupCreateStatus'
_Z='fsRoamGroupIsFast'
_Y='fsRoamGroupKeepaliveInterval'
_X='fsRoamGroupKeepaliveCount'
_W='fsRoamGroupMcAddress'
_V='fsRoamGroupMcEnable'
_U='fsRoamGroupMyAddress'
_T='fsRoamGroupName'
_S='fsMobilityUserJsonMacAddr'
_R='fsWLANID'
_Q='fsAPName'
_P='fsRoamMemberPeerAddress'
_O='fsRoamMemberGroupId'
_N='fsRoamGroupId'
_M='OctetString'
_L='fsRoamTrackId'
_K='fsRoamTrackStaMac'
_J='fsRoamUserMac'
_I='fsRoamIPv6MemberPeerAddress'
_H='fsRoamIPv6MemberGroupId'
_G='accessible-for-notify'
_F='Integer32'
_E='read-write'
_D='read-create'
_C='read-only'
_B='FS-CAPWAP-MOBILITY-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_M,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
fsMgmt,=mibBuilder.importSymbols('FS-SMI','fsMgmt')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
Ipv6Address,=mibBuilder.importSymbols('IPV6-TC','Ipv6Address')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention')
fsMobilityMIB=ModuleIdentity((1,3,6,1,4,1,52642,1,1,10,2,64))
if mibBuilder.loadTexts:fsMobilityMIB.setRevisions(('2009-09-18 00:00',))
_FsMobilityMIBObjects_ObjectIdentity=ObjectIdentity
fsMobilityMIBObjects=_FsMobilityMIBObjects_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,64,1))
_FsMobility_ObjectIdentity=ObjectIdentity
fsMobility=_FsMobility_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,64,1,1))
_FsMobilityEntryTable_Object=MibTable
fsMobilityEntryTable=_FsMobilityEntryTable_Object((1,3,6,1,4,1,52642,1,1,10,2,64,1,1,1))
if mibBuilder.loadTexts:fsMobilityEntryTable.setStatus(_A)
_FsMobilityEntry_Object=MibTableRow
fsMobilityEntry=_FsMobilityEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,64,1,1,1,1))
fsMobilityEntry.setIndexNames((0,_B,_N))
if mibBuilder.loadTexts:fsMobilityEntry.setStatus(_A)
class _FsRoamGroupId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,8))
_FsRoamGroupId_Type.__name__=_F
_FsRoamGroupId_Object=MibTableColumn
fsRoamGroupId=_FsRoamGroupId_Object((1,3,6,1,4,1,52642,1,1,10,2,64,1,1,1,1,1),_FsRoamGroupId_Type())
fsRoamGroupId.setMaxAccess(_C)
if mibBuilder.loadTexts:fsRoamGroupId.setStatus(_A)
_FsRoamGroupName_Type=DisplayString
_FsRoamGroupName_Object=MibTableColumn
fsRoamGroupName=_FsRoamGroupName_Object((1,3,6,1,4,1,52642,1,1,10,2,64,1,1,1,1,2),_FsRoamGroupName_Type())
fsRoamGroupName.setMaxAccess(_D)
if mibBuilder.loadTexts:fsRoamGroupName.setStatus(_A)
_FsRoamGroupMyAddress_Type=IpAddress
_FsRoamGroupMyAddress_Object=MibTableColumn
fsRoamGroupMyAddress=_FsRoamGroupMyAddress_Object((1,3,6,1,4,1,52642,1,1,10,2,64,1,1,1,1,3),_FsRoamGroupMyAddress_Type())
fsRoamGroupMyAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:fsRoamGroupMyAddress.setStatus(_A)
_FsRoamGroupMcEnable_Type=Integer32
_FsRoamGroupMcEnable_Object=MibTableColumn
fsRoamGroupMcEnable=_FsRoamGroupMcEnable_Object((1,3,6,1,4,1,52642,1,1,10,2,64,1,1,1,1,4),_FsRoamGroupMcEnable_Type())
fsRoamGroupMcEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:fsRoamGroupMcEnable.setStatus(_A)
_FsRoamGroupMcAddress_Type=IpAddress
_FsRoamGroupMcAddress_Object=MibTableColumn
fsRoamGroupMcAddress=_FsRoamGroupMcAddress_Object((1,3,6,1,4,1,52642,1,1,10,2,64,1,1,1,1,5),_FsRoamGroupMcAddress_Type())
fsRoamGroupMcAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:fsRoamGroupMcAddress.setStatus(_A)
class _FsRoamGroupKeepaliveCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,30))
_FsRoamGroupKeepaliveCount_Type.__name__=_F
_FsRoamGroupKeepaliveCount_Object=MibTableColumn
fsRoamGroupKeepaliveCount=_FsRoamGroupKeepaliveCount_Object((1,3,6,1,4,1,52642,1,1,10,2,64,1,1,1,1,6),_FsRoamGroupKeepaliveCount_Type())
fsRoamGroupKeepaliveCount.setMaxAccess(_D)
if mibBuilder.loadTexts:fsRoamGroupKeepaliveCount.setStatus(_A)
class _FsRoamGroupKeepaliveInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,30))
_FsRoamGroupKeepaliveInterval_Type.__name__=_F
_FsRoamGroupKeepaliveInterval_Object=MibTableColumn
fsRoamGroupKeepaliveInterval=_FsRoamGroupKeepaliveInterval_Object((1,3,6,1,4,1,52642,1,1,10,2,64,1,1,1,1,7),_FsRoamGroupKeepaliveInterval_Type())
fsRoamGroupKeepaliveInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:fsRoamGroupKeepaliveInterval.setStatus(_A)
_FsRoamGroupIsFast_Type=Integer32
_FsRoamGroupIsFast_Object=MibTableColumn
fsRoamGroupIsFast=_FsRoamGroupIsFast_Object((1,3,6,1,4,1,52642,1,1,10,2,64,1,1,1,1,8),_FsRoamGroupIsFast_Type())
fsRoamGroupIsFast.setMaxAccess(_D)
if mibBuilder.loadTexts:fsRoamGroupIsFast.setStatus(_A)
_FsRoamGroupCreateStatus_Type=RowStatus
_FsRoamGroupCreateStatus_Object=MibTableColumn
fsRoamGroupCreateStatus=_FsRoamGroupCreateStatus_Object((1,3,6,1,4,1,52642,1,1,10,2,64,1,1,1,1,9),_FsRoamGroupCreateStatus_Type())
fsRoamGroupCreateStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:fsRoamGroupCreateStatus.setStatus(_A)
_FsRoamGroupMyAddressIPv6_Type=Ipv6Address
_FsRoamGroupMyAddressIPv6_Object=MibTableColumn
fsRoamGroupMyAddressIPv6=_FsRoamGroupMyAddressIPv6_Object((1,3,6,1,4,1,52642,1,1,10,2,64,1,1,1,1,10),_FsRoamGroupMyAddressIPv6_Type())
fsRoamGroupMyAddressIPv6.setMaxAccess(_C)
if mibBuilder.loadTexts:fsRoamGroupMyAddressIPv6.setStatus(_A)
_FsMobilityMemberEntryTable_Object=MibTable
fsMobilityMemberEntryTable=_FsMobilityMemberEntryTable_Object((1,3,6,1,4,1,52642,1,1,10,2,64,1,1,2))
if mibBuilder.loadTexts:fsMobilityMemberEntryTable.setStatus(_A)
_FsMobilityMemberEntry_Object=MibTableRow
fsMobilityMemberEntry=_FsMobilityMemberEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,64,1,1,2,1))
fsMobilityMemberEntry.setIndexNames((0,_B,_O),(0,_B,_P))
if mibBuilder.loadTexts:fsMobilityMemberEntry.setStatus(_A)
class _FsRoamMemberGroupId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,8))
_FsRoamMemberGroupId_Type.__name__=_F
_FsRoamMemberGroupId_Object=MibTableColumn
fsRoamMemberGroupId=_FsRoamMemberGroupId_Object((1,3,6,1,4,1,52642,1,1,10,2,64,1,1,2,1,1),_FsRoamMemberGroupId_Type())
fsRoamMemberGroupId.setMaxAccess(_C)
if mibBuilder.loadTexts:fsRoamMemberGroupId.setStatus(_A)
_FsRoamMemberPeerAddress_Type=IpAddress
_FsRoamMemberPeerAddress_Object=MibTableColumn
fsRoamMemberPeerAddress=_FsRoamMemberPeerAddress_Object((1,3,6,1,4,1,52642,1,1,10,2,64,1,1,2,1,2),_FsRoamMemberPeerAddress_Type())
fsRoamMemberPeerAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:fsRoamMemberPeerAddress.setStatus(_A)
class _FsRoamMemberIsList_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_FsRoamMemberIsList_Type.__name__=_F
_FsRoamMemberIsList_Object=MibTableColumn
fsRoamMemberIsList=_FsRoamMemberIsList_Object((1,3,6,1,4,1,52642,1,1,10,2,64,1,1,2,1,3),_FsRoamMemberIsList_Type())
fsRoamMemberIsList.setMaxAccess(_D)
if mibBuilder.loadTexts:fsRoamMemberIsList.setStatus(_A)
class _FsRoamMemberDataChannelIsOK_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_FsRoamMemberDataChannelIsOK_Type.__name__=_F
_FsRoamMemberDataChannelIsOK_Object=MibTableColumn
fsRoamMemberDataChannelIsOK=_FsRoamMemberDataChannelIsOK_Object((1,3,6,1,4,1,52642,1,1,10,2,64,1,1,2,1,4),_FsRoamMemberDataChannelIsOK_Type())
fsRoamMemberDataChannelIsOK.setMaxAccess(_C)
if mibBuilder.loadTexts:fsRoamMemberDataChannelIsOK.setStatus(_A)
_FsRoamMemberDataChannelFailTimes_Type=Integer32
_FsRoamMemberDataChannelFailTimes_Object=MibTableColumn
fsRoamMemberDataChannelFailTimes=_FsRoamMemberDataChannelFailTimes_Object((1,3,6,1,4,1,52642,1,1,10,2,64,1,1,2,1,5),_FsRoamMemberDataChannelFailTimes_Type())
fsRoamMemberDataChannelFailTimes.setMaxAccess(_C)
if mibBuilder.loadTexts:fsRoamMemberDataChannelFailTimes.setStatus(_A)
_FsRoamMemberDTLSIsClient_Type=Integer32
_FsRoamMemberDTLSIsClient_Object=MibTableColumn
fsRoamMemberDTLSIsClient=_FsRoamMemberDTLSIsClient_Object((1,3,6,1,4,1,52642,1,1,10,2,64,1,1,2,1,6),_FsRoamMemberDTLSIsClient_Type())
fsRoamMemberDTLSIsClient.setMaxAccess(_C)
if mibBuilder.loadTexts:fsRoamMemberDTLSIsClient.setStatus(_A)
class _FsRoamMemberDTLSIsOK_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_FsRoamMemberDTLSIsOK_Type.__name__=_F
_FsRoamMemberDTLSIsOK_Object=MibTableColumn
fsRoamMemberDTLSIsOK=_FsRoamMemberDTLSIsOK_Object((1,3,6,1,4,1,52642,1,1,10,2,64,1,1,2,1,7),_FsRoamMemberDTLSIsOK_Type())
fsRoamMemberDTLSIsOK.setMaxAccess(_C)
if mibBuilder.loadTexts:fsRoamMemberDTLSIsOK.setStatus(_A)
_FsRoamMemberCreateStatus_Type=RowStatus
_FsRoamMemberCreateStatus_Object=MibTableColumn
fsRoamMemberCreateStatus=_FsRoamMemberCreateStatus_Object((1,3,6,1,4,1,52642,1,1,10,2,64,1,1,2,1,8),_FsRoamMemberCreateStatus_Type())
fsRoamMemberCreateStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:fsRoamMemberCreateStatus.setStatus(_A)
_FsAPCtrlCreatEntryTable_Object=MibTable
fsAPCtrlCreatEntryTable=_FsAPCtrlCreatEntryTable_Object((1,3,6,1,4,1,52642,1,1,10,2,64,1,1,3))
if mibBuilder.loadTexts:fsAPCtrlCreatEntryTable.setStatus(_A)
_FsAPCtrlCreatEntry_Object=MibTableRow
fsAPCtrlCreatEntry=_FsAPCtrlCreatEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,64,1,1,3,1))
fsAPCtrlCreatEntry.setIndexNames((0,_B,_Q))
if mibBuilder.loadTexts:fsAPCtrlCreatEntry.setStatus(_A)
_FsAPName_Type=DisplayString
_FsAPName_Object=MibTableColumn
fsAPName=_FsAPName_Object((1,3,6,1,4,1,52642,1,1,10,2,64,1,1,3,1,1),_FsAPName_Type())
fsAPName.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:fsAPName.setStatus(_A)
class _FsPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_FsPriority_Type.__name__=_F
_FsPriority_Object=MibTableColumn
fsPriority=_FsPriority_Object((1,3,6,1,4,1,52642,1,1,10,2,64,1,1,3,1,2),_FsPriority_Type())
fsPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:fsPriority.setStatus(_A)
_FsPrimaryACIP_Type=IpAddress
_FsPrimaryACIP_Object=MibTableColumn
fsPrimaryACIP=_FsPrimaryACIP_Object((1,3,6,1,4,1,52642,1,1,10,2,64,1,1,3,1,3),_FsPrimaryACIP_Type())
fsPrimaryACIP.setMaxAccess(_D)
if mibBuilder.loadTexts:fsPrimaryACIP.setStatus(_A)
_FsPrimaryACName_Type=DisplayString
_FsPrimaryACName_Object=MibTableColumn
fsPrimaryACName=_FsPrimaryACName_Object((1,3,6,1,4,1,52642,1,1,10,2,64,1,1,3,1,4),_FsPrimaryACName_Type())
fsPrimaryACName.setMaxAccess(_D)
if mibBuilder.loadTexts:fsPrimaryACName.setStatus(_A)
_FsSecondaryACIP_Type=IpAddress
_FsSecondaryACIP_Object=MibTableColumn
fsSecondaryACIP=_FsSecondaryACIP_Object((1,3,6,1,4,1,52642,1,1,10,2,64,1,1,3,1,5),_FsSecondaryACIP_Type())
fsSecondaryACIP.setMaxAccess(_D)
if mibBuilder.loadTexts:fsSecondaryACIP.setStatus(_A)
_FsSecondaryACName_Type=DisplayString
_FsSecondaryACName_Object=MibTableColumn
fsSecondaryACName=_FsSecondaryACName_Object((1,3,6,1,4,1,52642,1,1,10,2,64,1,1,3,1,6),_FsSecondaryACName_Type())
fsSecondaryACName.setMaxAccess(_D)
if mibBuilder.loadTexts:fsSecondaryACName.setStatus(_A)
_FsTertiaryACIP_Type=IpAddress
_FsTertiaryACIP_Object=MibTableColumn
fsTertiaryACIP=_FsTertiaryACIP_Object((1,3,6,1,4,1,52642,1,1,10,2,64,1,1,3,1,7),_FsTertiaryACIP_Type())
fsTertiaryACIP.setMaxAccess(_D)
if mibBuilder.loadTexts:fsTertiaryACIP.setStatus(_A)
_FsTertiaryACName_Type=DisplayString
_FsTertiaryACName_Object=MibTableColumn
fsTertiaryACName=_FsTertiaryACName_Object((1,3,6,1,4,1,52642,1,1,10,2,64,1,1,3,1,8),_FsTertiaryACName_Type())
fsTertiaryACName.setMaxAccess(_D)
if mibBuilder.loadTexts:fsTertiaryACName.setStatus(_A)
_FsAPCtrlCreatStatus_Type=RowStatus
_FsAPCtrlCreatStatus_Object=MibTableColumn
fsAPCtrlCreatStatus=_FsAPCtrlCreatStatus_Object((1,3,6,1,4,1,52642,1,1,10,2,64,1,1,3,1,9),_FsAPCtrlCreatStatus_Type())
fsAPCtrlCreatStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:fsAPCtrlCreatStatus.setStatus(_A)
_FsWLANCtrlCreatEntryTable_Object=MibTable
fsWLANCtrlCreatEntryTable=_FsWLANCtrlCreatEntryTable_Object((1,3,6,1,4,1,52642,1,1,10,2,64,1,1,4))
if mibBuilder.loadTexts:fsWLANCtrlCreatEntryTable.setStatus(_A)
_FsWLANCtrlCreatEntry_Object=MibTableRow
fsWLANCtrlCreatEntry=_FsWLANCtrlCreatEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,64,1,1,4,1))
fsWLANCtrlCreatEntry.setIndexNames((0,_B,_R))
if mibBuilder.loadTexts:fsWLANCtrlCreatEntry.setStatus(_A)
_FsWLANID_Type=Integer32
_FsWLANID_Object=MibTableColumn
fsWLANID=_FsWLANID_Object((1,3,6,1,4,1,52642,1,1,10,2,64,1,1,4,1,1),_FsWLANID_Type())
fsWLANID.setMaxAccess(_C)
if mibBuilder.loadTexts:fsWLANID.setStatus(_A)
_FsAnchorACIPaddr_Type=IpAddress
_FsAnchorACIPaddr_Object=MibTableColumn
fsAnchorACIPaddr=_FsAnchorACIPaddr_Object((1,3,6,1,4,1,52642,1,1,10,2,64,1,1,4,1,2),_FsAnchorACIPaddr_Type())
fsAnchorACIPaddr.setMaxAccess(_D)
if mibBuilder.loadTexts:fsAnchorACIPaddr.setStatus(_A)
_FsWLANCtrlCreatStatus_Type=RowStatus
_FsWLANCtrlCreatStatus_Object=MibTableColumn
fsWLANCtrlCreatStatus=_FsWLANCtrlCreatStatus_Object((1,3,6,1,4,1,52642,1,1,10,2,64,1,1,4,1,3),_FsWLANCtrlCreatStatus_Type())
fsWLANCtrlCreatStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:fsWLANCtrlCreatStatus.setStatus(_A)
_FsAnchorACIPaddrIPv6_Type=Ipv6Address
_FsAnchorACIPaddrIPv6_Object=MibTableColumn
fsAnchorACIPaddrIPv6=_FsAnchorACIPaddrIPv6_Object((1,3,6,1,4,1,52642,1,1,10,2,64,1,1,4,1,4),_FsAnchorACIPaddrIPv6_Type())
fsAnchorACIPaddrIPv6.setMaxAccess(_D)
if mibBuilder.loadTexts:fsAnchorACIPaddrIPv6.setStatus(_A)
_FsMobilityACPing_Type=IpAddress
_FsMobilityACPing_Object=MibScalar
fsMobilityACPing=_FsMobilityACPing_Object((1,3,6,1,4,1,52642,1,1,10,2,64,1,1,5),_FsMobilityACPing_Type())
fsMobilityACPing.setMaxAccess(_E)
if mibBuilder.loadTexts:fsMobilityACPing.setStatus(_A)
_FsGlobalHandoffRequestsReceived_Type=Integer32
_FsGlobalHandoffRequestsReceived_Object=MibScalar
fsGlobalHandoffRequestsReceived=_FsGlobalHandoffRequestsReceived_Object((1,3,6,1,4,1,52642,1,1,10,2,64,1,1,6),_FsGlobalHandoffRequestsReceived_Type())
fsGlobalHandoffRequestsReceived.setMaxAccess(_E)
if mibBuilder.loadTexts:fsGlobalHandoffRequestsReceived.setStatus(_A)
_FsGlobalHandoffEndRequestsReceived_Type=Integer32
_FsGlobalHandoffEndRequestsReceived_Object=MibScalar
fsGlobalHandoffEndRequestsReceived=_FsGlobalHandoffEndRequestsReceived_Object((1,3,6,1,4,1,52642,1,1,10,2,64,1,1,7),_FsGlobalHandoffEndRequestsReceived_Type())
fsGlobalHandoffEndRequestsReceived.setMaxAccess(_E)
if mibBuilder.loadTexts:fsGlobalHandoffEndRequestsReceived.setStatus(_A)
_FsGlobalStateTransitionsDisabled_Type=Integer32
_FsGlobalStateTransitionsDisabled_Object=MibScalar
fsGlobalStateTransitionsDisabled=_FsGlobalStateTransitionsDisabled_Object((1,3,6,1,4,1,52642,1,1,10,2,64,1,1,8),_FsGlobalStateTransitionsDisabled_Type())
fsGlobalStateTransitionsDisabled.setMaxAccess(_E)
if mibBuilder.loadTexts:fsGlobalStateTransitionsDisabled.setStatus(_A)
_FsGlobalResourceUnavailable_Type=Integer32
_FsGlobalResourceUnavailable_Object=MibScalar
fsGlobalResourceUnavailable=_FsGlobalResourceUnavailable_Object((1,3,6,1,4,1,52642,1,1,10,2,64,1,1,9),_FsGlobalResourceUnavailable_Type())
fsGlobalResourceUnavailable.setMaxAccess(_E)
if mibBuilder.loadTexts:fsGlobalResourceUnavailable.setStatus(_A)
_FsRespondeHandoffRequestIgnored_Type=Integer32
_FsRespondeHandoffRequestIgnored_Object=MibScalar
fsRespondeHandoffRequestIgnored=_FsRespondeHandoffRequestIgnored_Object((1,3,6,1,4,1,52642,1,1,10,2,64,1,1,10),_FsRespondeHandoffRequestIgnored_Type())
fsRespondeHandoffRequestIgnored.setMaxAccess(_E)
if mibBuilder.loadTexts:fsRespondeHandoffRequestIgnored.setStatus(_A)
_FsRespondePingPongHandoffRequestsDropped_Type=Integer32
_FsRespondePingPongHandoffRequestsDropped_Object=MibScalar
fsRespondePingPongHandoffRequestsDropped=_FsRespondePingPongHandoffRequestsDropped_Object((1,3,6,1,4,1,52642,1,1,10,2,64,1,1,11),_FsRespondePingPongHandoffRequestsDropped_Type())
fsRespondePingPongHandoffRequestsDropped.setMaxAccess(_E)
if mibBuilder.loadTexts:fsRespondePingPongHandoffRequestsDropped.setStatus(_A)
_FsRespondeHandoffRequestsDroped_Type=Integer32
_FsRespondeHandoffRequestsDroped_Object=MibScalar
fsRespondeHandoffRequestsDroped=_FsRespondeHandoffRequestsDroped_Object((1,3,6,1,4,1,52642,1,1,10,2,64,1,1,12),_FsRespondeHandoffRequestsDroped_Type())
fsRespondeHandoffRequestsDroped.setMaxAccess(_E)
if mibBuilder.loadTexts:fsRespondeHandoffRequestsDroped.setStatus(_A)
_FsRespondeHandoffRequestsDenied_Type=Integer32
_FsRespondeHandoffRequestsDenied_Object=MibScalar
fsRespondeHandoffRequestsDenied=_FsRespondeHandoffRequestsDenied_Object((1,3,6,1,4,1,52642,1,1,10,2,64,1,1,13),_FsRespondeHandoffRequestsDenied_Type())
fsRespondeHandoffRequestsDenied.setMaxAccess(_E)
if mibBuilder.loadTexts:fsRespondeHandoffRequestsDenied.setStatus(_A)
_FsRespondeClientHandoffasLocal_Type=Integer32
_FsRespondeClientHandoffasLocal_Object=MibScalar
fsRespondeClientHandoffasLocal=_FsRespondeClientHandoffasLocal_Object((1,3,6,1,4,1,52642,1,1,10,2,64,1,1,14),_FsRespondeClientHandoffasLocal_Type())
fsRespondeClientHandoffasLocal.setMaxAccess(_E)
if mibBuilder.loadTexts:fsRespondeClientHandoffasLocal.setStatus(_A)
_FsRespondeClientHandoffasForeign_Type=Integer32
_FsRespondeClientHandoffasForeign_Object=MibScalar
fsRespondeClientHandoffasForeign=_FsRespondeClientHandoffasForeign_Object((1,3,6,1,4,1,52642,1,1,10,2,64,1,1,15),_FsRespondeClientHandoffasForeign_Type())
fsRespondeClientHandoffasForeign.setMaxAccess(_E)
if mibBuilder.loadTexts:fsRespondeClientHandoffasForeign.setStatus(_A)
_FsRespondeAnchorRequestsReceived_Type=Integer32
_FsRespondeAnchorRequestsReceived_Object=MibScalar
fsRespondeAnchorRequestsReceived=_FsRespondeAnchorRequestsReceived_Object((1,3,6,1,4,1,52642,1,1,10,2,64,1,1,16),_FsRespondeAnchorRequestsReceived_Type())
fsRespondeAnchorRequestsReceived.setMaxAccess(_E)
if mibBuilder.loadTexts:fsRespondeAnchorRequestsReceived.setStatus(_A)
_FsRespondeAnchorRequestDenied_Type=Integer32
_FsRespondeAnchorRequestDenied_Object=MibScalar
fsRespondeAnchorRequestDenied=_FsRespondeAnchorRequestDenied_Object((1,3,6,1,4,1,52642,1,1,10,2,64,1,1,17),_FsRespondeAnchorRequestDenied_Type())
fsRespondeAnchorRequestDenied.setMaxAccess(_E)
if mibBuilder.loadTexts:fsRespondeAnchorRequestDenied.setStatus(_A)
_FsRespondeAnchorTransferred_Type=Integer32
_FsRespondeAnchorTransferred_Object=MibScalar
fsRespondeAnchorTransferred=_FsRespondeAnchorTransferred_Object((1,3,6,1,4,1,52642,1,1,10,2,64,1,1,18),_FsRespondeAnchorTransferred_Type())
fsRespondeAnchorTransferred.setMaxAccess(_E)
if mibBuilder.loadTexts:fsRespondeAnchorTransferred.setStatus(_A)
_FsInitHandoffRequestsSent_Type=Integer32
_FsInitHandoffRequestsSent_Object=MibScalar
fsInitHandoffRequestsSent=_FsInitHandoffRequestsSent_Object((1,3,6,1,4,1,52642,1,1,10,2,64,1,1,19),_FsInitHandoffRequestsSent_Type())
fsInitHandoffRequestsSent.setMaxAccess(_E)
if mibBuilder.loadTexts:fsInitHandoffRequestsSent.setStatus(_A)
_FsInitHandoffReplyReceived_Type=Integer32
_FsInitHandoffReplyReceived_Object=MibScalar
fsInitHandoffReplyReceived=_FsInitHandoffReplyReceived_Object((1,3,6,1,4,1,52642,1,1,10,2,64,1,1,20),_FsInitHandoffReplyReceived_Type())
fsInitHandoffReplyReceived.setMaxAccess(_E)
if mibBuilder.loadTexts:fsInitHandoffReplyReceived.setStatus(_A)
_FsInitHandoffasLocalReceived_Type=Integer32
_FsInitHandoffasLocalReceived_Object=MibScalar
fsInitHandoffasLocalReceived=_FsInitHandoffasLocalReceived_Object((1,3,6,1,4,1,52642,1,1,10,2,64,1,1,21),_FsInitHandoffasLocalReceived_Type())
fsInitHandoffasLocalReceived.setMaxAccess(_E)
if mibBuilder.loadTexts:fsInitHandoffasLocalReceived.setStatus(_A)
_FsInitHandoffasForeignReceived_Type=Integer32
_FsInitHandoffasForeignReceived_Object=MibScalar
fsInitHandoffasForeignReceived=_FsInitHandoffasForeignReceived_Object((1,3,6,1,4,1,52642,1,1,10,2,64,1,1,22),_FsInitHandoffasForeignReceived_Type())
fsInitHandoffasForeignReceived.setMaxAccess(_E)
if mibBuilder.loadTexts:fsInitHandoffasForeignReceived.setStatus(_A)
_FsInitHandoffDenyReceived_Type=Integer32
_FsInitHandoffDenyReceived_Object=MibScalar
fsInitHandoffDenyReceived=_FsInitHandoffDenyReceived_Object((1,3,6,1,4,1,52642,1,1,10,2,64,1,1,23),_FsInitHandoffDenyReceived_Type())
fsInitHandoffDenyReceived.setMaxAccess(_E)
if mibBuilder.loadTexts:fsInitHandoffDenyReceived.setStatus(_A)
_FsInitAnchorRequestSent_Type=Integer32
_FsInitAnchorRequestSent_Object=MibScalar
fsInitAnchorRequestSent=_FsInitAnchorRequestSent_Object((1,3,6,1,4,1,52642,1,1,10,2,64,1,1,24),_FsInitAnchorRequestSent_Type())
fsInitAnchorRequestSent.setMaxAccess(_E)
if mibBuilder.loadTexts:fsInitAnchorRequestSent.setStatus(_A)
_FsInitAnchorDenyReceived_Type=Integer32
_FsInitAnchorDenyReceived_Object=MibScalar
fsInitAnchorDenyReceived=_FsInitAnchorDenyReceived_Object((1,3,6,1,4,1,52642,1,1,10,2,64,1,1,25),_FsInitAnchorDenyReceived_Type())
fsInitAnchorDenyReceived.setMaxAccess(_E)
if mibBuilder.loadTexts:fsInitAnchorDenyReceived.setStatus(_A)
_FsAPPriorityEnable_Type=Integer32
_FsAPPriorityEnable_Object=MibScalar
fsAPPriorityEnable=_FsAPPriorityEnable_Object((1,3,6,1,4,1,52642,1,1,10,2,64,1,1,26),_FsAPPriorityEnable_Type())
fsAPPriorityEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:fsAPPriorityEnable.setStatus(_A)
_FsPrimaryBackUpACIP_Type=IpAddress
_FsPrimaryBackUpACIP_Object=MibScalar
fsPrimaryBackUpACIP=_FsPrimaryBackUpACIP_Object((1,3,6,1,4,1,52642,1,1,10,2,64,1,1,27),_FsPrimaryBackUpACIP_Type())
fsPrimaryBackUpACIP.setMaxAccess(_D)
if mibBuilder.loadTexts:fsPrimaryBackUpACIP.setStatus(_A)
_FsPrimaryBackUpACName_Type=DisplayString
_FsPrimaryBackUpACName_Object=MibScalar
fsPrimaryBackUpACName=_FsPrimaryBackUpACName_Object((1,3,6,1,4,1,52642,1,1,10,2,64,1,1,28),_FsPrimaryBackUpACName_Type())
fsPrimaryBackUpACName.setMaxAccess(_D)
if mibBuilder.loadTexts:fsPrimaryBackUpACName.setStatus(_A)
_FsSecondaryBackUpACIP_Type=IpAddress
_FsSecondaryBackUpACIP_Object=MibScalar
fsSecondaryBackUpACIP=_FsSecondaryBackUpACIP_Object((1,3,6,1,4,1,52642,1,1,10,2,64,1,1,29),_FsSecondaryBackUpACIP_Type())
fsSecondaryBackUpACIP.setMaxAccess(_D)
if mibBuilder.loadTexts:fsSecondaryBackUpACIP.setStatus(_A)
_FsSecondaryBackUpACName_Type=DisplayString
_FsSecondaryBackUpACName_Object=MibScalar
fsSecondaryBackUpACName=_FsSecondaryBackUpACName_Object((1,3,6,1,4,1,52642,1,1,10,2,64,1,1,30),_FsSecondaryBackUpACName_Type())
fsSecondaryBackUpACName.setMaxAccess(_D)
if mibBuilder.loadTexts:fsSecondaryBackUpACName.setStatus(_A)
_FsTeriaryBackUpACip_Type=IpAddress
_FsTeriaryBackUpACip_Object=MibScalar
fsTeriaryBackUpACip=_FsTeriaryBackUpACip_Object((1,3,6,1,4,1,52642,1,1,10,2,64,1,1,31),_FsTeriaryBackUpACip_Type())
fsTeriaryBackUpACip.setMaxAccess(_D)
if mibBuilder.loadTexts:fsTeriaryBackUpACip.setStatus(_A)
_FsTeriaryBackUpACName_Type=DisplayString
_FsTeriaryBackUpACName_Object=MibScalar
fsTeriaryBackUpACName=_FsTeriaryBackUpACName_Object((1,3,6,1,4,1,52642,1,1,10,2,64,1,1,32),_FsTeriaryBackUpACName_Type())
fsTeriaryBackUpACName.setMaxAccess(_D)
if mibBuilder.loadTexts:fsTeriaryBackUpACName.setStatus(_A)
_FsACIntraRoam_Type=Counter32
_FsACIntraRoam_Object=MibScalar
fsACIntraRoam=_FsACIntraRoam_Object((1,3,6,1,4,1,52642,1,1,10,2,64,1,1,33),_FsACIntraRoam_Type())
fsACIntraRoam.setMaxAccess(_C)
if mibBuilder.loadTexts:fsACIntraRoam.setStatus(_A)
_FsACInterRoamIn_Type=Counter32
_FsACInterRoamIn_Object=MibScalar
fsACInterRoamIn=_FsACInterRoamIn_Object((1,3,6,1,4,1,52642,1,1,10,2,64,1,1,34),_FsACInterRoamIn_Type())
fsACInterRoamIn.setMaxAccess(_C)
if mibBuilder.loadTexts:fsACInterRoamIn.setStatus(_A)
_FsACInterRoamOut_Type=Counter32
_FsACInterRoamOut_Object=MibScalar
fsACInterRoamOut=_FsACInterRoamOut_Object((1,3,6,1,4,1,52642,1,1,10,2,64,1,1,35),_FsACInterRoamOut_Type())
fsACInterRoamOut.setMaxAccess(_C)
if mibBuilder.loadTexts:fsACInterRoamOut.setStatus(_A)
_FsMobilityACPingIPv6_Type=Ipv6Address
_FsMobilityACPingIPv6_Object=MibScalar
fsMobilityACPingIPv6=_FsMobilityACPingIPv6_Object((1,3,6,1,4,1,52642,1,1,10,2,64,1,1,36),_FsMobilityACPingIPv6_Type())
fsMobilityACPingIPv6.setMaxAccess(_E)
if mibBuilder.loadTexts:fsMobilityACPingIPv6.setStatus(_A)
_FsMobilityIPv6MemberEntryTable_Object=MibTable
fsMobilityIPv6MemberEntryTable=_FsMobilityIPv6MemberEntryTable_Object((1,3,6,1,4,1,52642,1,1,10,2,64,1,1,37))
if mibBuilder.loadTexts:fsMobilityIPv6MemberEntryTable.setStatus(_A)
_FsMobilityIPv6MemberEntry_Object=MibTableRow
fsMobilityIPv6MemberEntry=_FsMobilityIPv6MemberEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,64,1,1,37,1))
fsMobilityIPv6MemberEntry.setIndexNames((0,_B,_H),(0,_B,_I))
if mibBuilder.loadTexts:fsMobilityIPv6MemberEntry.setStatus(_A)
class _FsRoamIPv6MemberGroupId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,8))
_FsRoamIPv6MemberGroupId_Type.__name__=_F
_FsRoamIPv6MemberGroupId_Object=MibTableColumn
fsRoamIPv6MemberGroupId=_FsRoamIPv6MemberGroupId_Object((1,3,6,1,4,1,52642,1,1,10,2,64,1,1,37,1,1),_FsRoamIPv6MemberGroupId_Type())
fsRoamIPv6MemberGroupId.setMaxAccess(_C)
if mibBuilder.loadTexts:fsRoamIPv6MemberGroupId.setStatus(_A)
_FsRoamIPv6MemberPeerAddress_Type=Ipv6Address
_FsRoamIPv6MemberPeerAddress_Object=MibTableColumn
fsRoamIPv6MemberPeerAddress=_FsRoamIPv6MemberPeerAddress_Object((1,3,6,1,4,1,52642,1,1,10,2,64,1,1,37,1,2),_FsRoamIPv6MemberPeerAddress_Type())
fsRoamIPv6MemberPeerAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:fsRoamIPv6MemberPeerAddress.setStatus(_A)
class _FsRoamIPv6MemberIsList_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_FsRoamIPv6MemberIsList_Type.__name__=_F
_FsRoamIPv6MemberIsList_Object=MibTableColumn
fsRoamIPv6MemberIsList=_FsRoamIPv6MemberIsList_Object((1,3,6,1,4,1,52642,1,1,10,2,64,1,1,37,1,3),_FsRoamIPv6MemberIsList_Type())
fsRoamIPv6MemberIsList.setMaxAccess(_D)
if mibBuilder.loadTexts:fsRoamIPv6MemberIsList.setStatus(_A)
class _FsRoamIPv6MemberDataChannelIsOK_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_FsRoamIPv6MemberDataChannelIsOK_Type.__name__=_F
_FsRoamIPv6MemberDataChannelIsOK_Object=MibTableColumn
fsRoamIPv6MemberDataChannelIsOK=_FsRoamIPv6MemberDataChannelIsOK_Object((1,3,6,1,4,1,52642,1,1,10,2,64,1,1,37,1,4),_FsRoamIPv6MemberDataChannelIsOK_Type())
fsRoamIPv6MemberDataChannelIsOK.setMaxAccess(_C)
if mibBuilder.loadTexts:fsRoamIPv6MemberDataChannelIsOK.setStatus(_A)
_FsRoamIPv6MemberDataChannelFailTimes_Type=Integer32
_FsRoamIPv6MemberDataChannelFailTimes_Object=MibTableColumn
fsRoamIPv6MemberDataChannelFailTimes=_FsRoamIPv6MemberDataChannelFailTimes_Object((1,3,6,1,4,1,52642,1,1,10,2,64,1,1,37,1,5),_FsRoamIPv6MemberDataChannelFailTimes_Type())
fsRoamIPv6MemberDataChannelFailTimes.setMaxAccess(_C)
if mibBuilder.loadTexts:fsRoamIPv6MemberDataChannelFailTimes.setStatus(_A)
_FsRoamIPv6MemberDTLSIsClient_Type=Integer32
_FsRoamIPv6MemberDTLSIsClient_Object=MibTableColumn
fsRoamIPv6MemberDTLSIsClient=_FsRoamIPv6MemberDTLSIsClient_Object((1,3,6,1,4,1,52642,1,1,10,2,64,1,1,37,1,6),_FsRoamIPv6MemberDTLSIsClient_Type())
fsRoamIPv6MemberDTLSIsClient.setMaxAccess(_C)
if mibBuilder.loadTexts:fsRoamIPv6MemberDTLSIsClient.setStatus(_A)
class _FsRoamIPv6MemberDTLSIsOK_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_FsRoamIPv6MemberDTLSIsOK_Type.__name__=_F
_FsRoamIPv6MemberDTLSIsOK_Object=MibTableColumn
fsRoamIPv6MemberDTLSIsOK=_FsRoamIPv6MemberDTLSIsOK_Object((1,3,6,1,4,1,52642,1,1,10,2,64,1,1,37,1,7),_FsRoamIPv6MemberDTLSIsOK_Type())
fsRoamIPv6MemberDTLSIsOK.setMaxAccess(_C)
if mibBuilder.loadTexts:fsRoamIPv6MemberDTLSIsOK.setStatus(_A)
_FsRoamIPv6MemberCreateStatus_Type=RowStatus
_FsRoamIPv6MemberCreateStatus_Object=MibTableColumn
fsRoamIPv6MemberCreateStatus=_FsRoamIPv6MemberCreateStatus_Object((1,3,6,1,4,1,52642,1,1,10,2,64,1,1,37,1,8),_FsRoamIPv6MemberCreateStatus_Type())
fsRoamIPv6MemberCreateStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:fsRoamIPv6MemberCreateStatus.setStatus(_A)
_FsMobilityUserEntryTable_Object=MibTable
fsMobilityUserEntryTable=_FsMobilityUserEntryTable_Object((1,3,6,1,4,1,52642,1,1,10,2,64,1,1,38))
if mibBuilder.loadTexts:fsMobilityUserEntryTable.setStatus(_A)
_FsMobilityUserEntry_Object=MibTableRow
fsMobilityUserEntry=_FsMobilityUserEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,64,1,1,38,1))
fsMobilityUserEntry.setIndexNames((0,_B,_J))
if mibBuilder.loadTexts:fsMobilityUserEntry.setStatus(_A)
_FsRoamUserMac_Type=MacAddress
_FsRoamUserMac_Object=MibTableColumn
fsRoamUserMac=_FsRoamUserMac_Object((1,3,6,1,4,1,52642,1,1,10,2,64,1,1,38,1,1),_FsRoamUserMac_Type())
fsRoamUserMac.setMaxAccess(_C)
if mibBuilder.loadTexts:fsRoamUserMac.setStatus(_A)
_FsRoamUserRoamType_Type=Integer32
_FsRoamUserRoamType_Object=MibTableColumn
fsRoamUserRoamType=_FsRoamUserRoamType_Object((1,3,6,1,4,1,52642,1,1,10,2,64,1,1,38,1,2),_FsRoamUserRoamType_Type())
fsRoamUserRoamType.setMaxAccess(_C)
if mibBuilder.loadTexts:fsRoamUserRoamType.setStatus(_A)
_FsRoamUserRoamOutAcAddressType_Type=InetAddressType
_FsRoamUserRoamOutAcAddressType_Object=MibTableColumn
fsRoamUserRoamOutAcAddressType=_FsRoamUserRoamOutAcAddressType_Object((1,3,6,1,4,1,52642,1,1,10,2,64,1,1,38,1,3),_FsRoamUserRoamOutAcAddressType_Type())
fsRoamUserRoamOutAcAddressType.setMaxAccess(_C)
if mibBuilder.loadTexts:fsRoamUserRoamOutAcAddressType.setStatus(_A)
_FsRoamUserRoamOutAcAddress_Type=InetAddress
_FsRoamUserRoamOutAcAddress_Object=MibTableColumn
fsRoamUserRoamOutAcAddress=_FsRoamUserRoamOutAcAddress_Object((1,3,6,1,4,1,52642,1,1,10,2,64,1,1,38,1,4),_FsRoamUserRoamOutAcAddress_Type())
fsRoamUserRoamOutAcAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:fsRoamUserRoamOutAcAddress.setStatus(_A)
_FsRoamUserRoamInAcAddressType_Type=InetAddressType
_FsRoamUserRoamInAcAddressType_Object=MibTableColumn
fsRoamUserRoamInAcAddressType=_FsRoamUserRoamInAcAddressType_Object((1,3,6,1,4,1,52642,1,1,10,2,64,1,1,38,1,5),_FsRoamUserRoamInAcAddressType_Type())
fsRoamUserRoamInAcAddressType.setMaxAccess(_C)
if mibBuilder.loadTexts:fsRoamUserRoamInAcAddressType.setStatus(_A)
_FsRoamUserRoamInAcAddress_Type=InetAddress
_FsRoamUserRoamInAcAddress_Object=MibTableColumn
fsRoamUserRoamInAcAddress=_FsRoamUserRoamInAcAddress_Object((1,3,6,1,4,1,52642,1,1,10,2,64,1,1,38,1,6),_FsRoamUserRoamInAcAddress_Type())
fsRoamUserRoamInAcAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:fsRoamUserRoamInAcAddress.setStatus(_A)
_FsRoamUserRoamOutApMac_Type=MacAddress
_FsRoamUserRoamOutApMac_Object=MibTableColumn
fsRoamUserRoamOutApMac=_FsRoamUserRoamOutApMac_Object((1,3,6,1,4,1,52642,1,1,10,2,64,1,1,38,1,7),_FsRoamUserRoamOutApMac_Type())
fsRoamUserRoamOutApMac.setMaxAccess(_C)
if mibBuilder.loadTexts:fsRoamUserRoamOutApMac.setStatus(_A)
_FsRoamUserRoamInApMac_Type=MacAddress
_FsRoamUserRoamInApMac_Object=MibTableColumn
fsRoamUserRoamInApMac=_FsRoamUserRoamInApMac_Object((1,3,6,1,4,1,52642,1,1,10,2,64,1,1,38,1,8),_FsRoamUserRoamInApMac_Type())
fsRoamUserRoamInApMac.setMaxAccess(_C)
if mibBuilder.loadTexts:fsRoamUserRoamInApMac.setStatus(_A)
_FsRoamUserRoamOutVid_Type=Integer32
_FsRoamUserRoamOutVid_Object=MibTableColumn
fsRoamUserRoamOutVid=_FsRoamUserRoamOutVid_Object((1,3,6,1,4,1,52642,1,1,10,2,64,1,1,38,1,9),_FsRoamUserRoamOutVid_Type())
fsRoamUserRoamOutVid.setMaxAccess(_C)
if mibBuilder.loadTexts:fsRoamUserRoamOutVid.setStatus(_A)
_FsRoamUserRoamInVid_Type=Integer32
_FsRoamUserRoamInVid_Object=MibTableColumn
fsRoamUserRoamInVid=_FsRoamUserRoamInVid_Object((1,3,6,1,4,1,52642,1,1,10,2,64,1,1,38,1,10),_FsRoamUserRoamInVid_Type())
fsRoamUserRoamInVid.setMaxAccess(_C)
if mibBuilder.loadTexts:fsRoamUserRoamInVid.setStatus(_A)
_FsMobilityTrackEntryTable_Object=MibTable
fsMobilityTrackEntryTable=_FsMobilityTrackEntryTable_Object((1,3,6,1,4,1,52642,1,1,10,2,64,1,1,39))
if mibBuilder.loadTexts:fsMobilityTrackEntryTable.setStatus(_A)
_FsMobilityTrackEntry_Object=MibTableRow
fsMobilityTrackEntry=_FsMobilityTrackEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,64,1,1,39,1))
fsMobilityTrackEntry.setIndexNames((0,_B,_K),(0,_B,_L))
if mibBuilder.loadTexts:fsMobilityTrackEntry.setStatus(_A)
_FsRoamTrackStaMac_Type=MacAddress
_FsRoamTrackStaMac_Object=MibTableColumn
fsRoamTrackStaMac=_FsRoamTrackStaMac_Object((1,3,6,1,4,1,52642,1,1,10,2,64,1,1,39,1,1),_FsRoamTrackStaMac_Type())
fsRoamTrackStaMac.setMaxAccess(_C)
if mibBuilder.loadTexts:fsRoamTrackStaMac.setStatus(_A)
_FsRoamTrackId_Type=Integer32
_FsRoamTrackId_Object=MibTableColumn
fsRoamTrackId=_FsRoamTrackId_Object((1,3,6,1,4,1,52642,1,1,10,2,64,1,1,39,1,2),_FsRoamTrackId_Type())
fsRoamTrackId.setMaxAccess(_C)
if mibBuilder.loadTexts:fsRoamTrackId.setStatus(_A)
_FsRoamTrackAcAddressType_Type=InetAddressType
_FsRoamTrackAcAddressType_Object=MibTableColumn
fsRoamTrackAcAddressType=_FsRoamTrackAcAddressType_Object((1,3,6,1,4,1,52642,1,1,10,2,64,1,1,39,1,3),_FsRoamTrackAcAddressType_Type())
fsRoamTrackAcAddressType.setMaxAccess(_C)
if mibBuilder.loadTexts:fsRoamTrackAcAddressType.setStatus(_A)
_FsRoamTrackAcAddress_Type=InetAddress
_FsRoamTrackAcAddress_Object=MibTableColumn
fsRoamTrackAcAddress=_FsRoamTrackAcAddress_Object((1,3,6,1,4,1,52642,1,1,10,2,64,1,1,39,1,4),_FsRoamTrackAcAddress_Type())
fsRoamTrackAcAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:fsRoamTrackAcAddress.setStatus(_A)
_FsRoamTrackApMac_Type=MacAddress
_FsRoamTrackApMac_Object=MibTableColumn
fsRoamTrackApMac=_FsRoamTrackApMac_Object((1,3,6,1,4,1,52642,1,1,10,2,64,1,1,39,1,5),_FsRoamTrackApMac_Type())
fsRoamTrackApMac.setMaxAccess(_C)
if mibBuilder.loadTexts:fsRoamTrackApMac.setStatus(_A)
_FsRoamTrackRadioId_Type=Integer32
_FsRoamTrackRadioId_Object=MibTableColumn
fsRoamTrackRadioId=_FsRoamTrackRadioId_Object((1,3,6,1,4,1,52642,1,1,10,2,64,1,1,39,1,6),_FsRoamTrackRadioId_Type())
fsRoamTrackRadioId.setMaxAccess(_C)
if mibBuilder.loadTexts:fsRoamTrackRadioId.setStatus(_A)
_FsRoamTrackStaIp_Type=IpAddress
_FsRoamTrackStaIp_Object=MibTableColumn
fsRoamTrackStaIp=_FsRoamTrackStaIp_Object((1,3,6,1,4,1,52642,1,1,10,2,64,1,1,39,1,7),_FsRoamTrackStaIp_Type())
fsRoamTrackStaIp.setMaxAccess(_C)
if mibBuilder.loadTexts:fsRoamTrackStaIp.setStatus(_A)
_FsRoamTrackStaIpv6_Type=Ipv6Address
_FsRoamTrackStaIpv6_Object=MibTableColumn
fsRoamTrackStaIpv6=_FsRoamTrackStaIpv6_Object((1,3,6,1,4,1,52642,1,1,10,2,64,1,1,39,1,8),_FsRoamTrackStaIpv6_Type())
fsRoamTrackStaIpv6.setMaxAccess(_C)
if mibBuilder.loadTexts:fsRoamTrackStaIpv6.setStatus(_A)
_FsRoamTrackStaOnlineTime_Type=Integer32
_FsRoamTrackStaOnlineTime_Object=MibTableColumn
fsRoamTrackStaOnlineTime=_FsRoamTrackStaOnlineTime_Object((1,3,6,1,4,1,52642,1,1,10,2,64,1,1,39,1,9),_FsRoamTrackStaOnlineTime_Type())
fsRoamTrackStaOnlineTime.setMaxAccess(_C)
if mibBuilder.loadTexts:fsRoamTrackStaOnlineTime.setStatus(_A)
_FsMobilityUserJsonTable_Object=MibTable
fsMobilityUserJsonTable=_FsMobilityUserJsonTable_Object((1,3,6,1,4,1,52642,1,1,10,2,64,1,1,40))
if mibBuilder.loadTexts:fsMobilityUserJsonTable.setStatus(_A)
_FsMobilityUserJsonEntry_Object=MibTableRow
fsMobilityUserJsonEntry=_FsMobilityUserJsonEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,64,1,1,40,1))
fsMobilityUserJsonEntry.setIndexNames((0,_B,_S))
if mibBuilder.loadTexts:fsMobilityUserJsonEntry.setStatus(_A)
_FsMobilityUserJsonMacAddr_Type=MacAddress
_FsMobilityUserJsonMacAddr_Object=MibTableColumn
fsMobilityUserJsonMacAddr=_FsMobilityUserJsonMacAddr_Object((1,3,6,1,4,1,52642,1,1,10,2,64,1,1,40,1,1),_FsMobilityUserJsonMacAddr_Type())
fsMobilityUserJsonMacAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMobilityUserJsonMacAddr.setStatus(_A)
class _FsMobilityUserJsonContent_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,1023))
_FsMobilityUserJsonContent_Type.__name__=_M
_FsMobilityUserJsonContent_Object=MibTableColumn
fsMobilityUserJsonContent=_FsMobilityUserJsonContent_Object((1,3,6,1,4,1,52642,1,1,10,2,64,1,1,40,1,2),_FsMobilityUserJsonContent_Type())
fsMobilityUserJsonContent.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMobilityUserJsonContent.setStatus(_A)
_FsMobilityIf_ObjectIdentity=ObjectIdentity
fsMobilityIf=_FsMobilityIf_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,64,1,2))
_FsMobilityMIBCompliances_ObjectIdentity=ObjectIdentity
fsMobilityMIBCompliances=_FsMobilityMIBCompliances_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,64,1,2,1))
_FsMobilityMIBGroups_ObjectIdentity=ObjectIdentity
fsMobilityMIBGroups=_FsMobilityMIBGroups_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,64,1,2,2))
_FsMobilityTrap_ObjectIdentity=ObjectIdentity
fsMobilityTrap=_FsMobilityTrap_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,64,1,3))
_FsMobilityTrapSta_ObjectIdentity=ObjectIdentity
fsMobilityTrapSta=_FsMobilityTrapSta_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,64,1,3,1))
_FsMobilityNotifyApMac_Type=MacAddress
_FsMobilityNotifyApMac_Object=MibScalar
fsMobilityNotifyApMac=_FsMobilityNotifyApMac_Object((1,3,6,1,4,1,52642,1,1,10,2,64,1,3,1,1),_FsMobilityNotifyApMac_Type())
fsMobilityNotifyApMac.setMaxAccess(_G)
if mibBuilder.loadTexts:fsMobilityNotifyApMac.setStatus(_A)
_FsMobilityNotifyStaMac_Type=MacAddress
_FsMobilityNotifyStaMac_Object=MibScalar
fsMobilityNotifyStaMac=_FsMobilityNotifyStaMac_Object((1,3,6,1,4,1,52642,1,1,10,2,64,1,3,1,2),_FsMobilityNotifyStaMac_Type())
fsMobilityNotifyStaMac.setMaxAccess(_G)
if mibBuilder.loadTexts:fsMobilityNotifyStaMac.setStatus(_A)
_FsMobilityNotifyApIp_Type=IpAddress
_FsMobilityNotifyApIp_Object=MibScalar
fsMobilityNotifyApIp=_FsMobilityNotifyApIp_Object((1,3,6,1,4,1,52642,1,1,10,2,64,1,3,1,3),_FsMobilityNotifyApIp_Type())
fsMobilityNotifyApIp.setMaxAccess(_G)
if mibBuilder.loadTexts:fsMobilityNotifyApIp.setStatus(_A)
_FsMobilityNotifyStaIp_Type=IpAddress
_FsMobilityNotifyStaIp_Object=MibScalar
fsMobilityNotifyStaIp=_FsMobilityNotifyStaIp_Object((1,3,6,1,4,1,52642,1,1,10,2,64,1,3,1,4),_FsMobilityNotifyStaIp_Type())
fsMobilityNotifyStaIp.setMaxAccess(_G)
if mibBuilder.loadTexts:fsMobilityNotifyStaIp.setStatus(_A)
_FsMobilityNotifyStaOperType_Type=Integer32
_FsMobilityNotifyStaOperType_Object=MibScalar
fsMobilityNotifyStaOperType=_FsMobilityNotifyStaOperType_Object((1,3,6,1,4,1,52642,1,1,10,2,64,1,3,1,5),_FsMobilityNotifyStaOperType_Type())
fsMobilityNotifyStaOperType.setMaxAccess(_G)
if mibBuilder.loadTexts:fsMobilityNotifyStaOperType.setStatus(_A)
class _FsMobilityNotifyStaApRadioId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_FsMobilityNotifyStaApRadioId_Type.__name__=_F
_FsMobilityNotifyStaApRadioId_Object=MibScalar
fsMobilityNotifyStaApRadioId=_FsMobilityNotifyStaApRadioId_Object((1,3,6,1,4,1,52642,1,1,10,2,64,1,3,1,6),_FsMobilityNotifyStaApRadioId_Type())
fsMobilityNotifyStaApRadioId.setMaxAccess(_G)
if mibBuilder.loadTexts:fsMobilityNotifyStaApRadioId.setStatus(_A)
class _FsMobilityNotifyStaApRadioType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_FsMobilityNotifyStaApRadioType_Type.__name__=_F
_FsMobilityNotifyStaApRadioType_Object=MibScalar
fsMobilityNotifyStaApRadioType=_FsMobilityNotifyStaApRadioType_Object((1,3,6,1,4,1,52642,1,1,10,2,64,1,3,1,7),_FsMobilityNotifyStaApRadioType_Type())
fsMobilityNotifyStaApRadioType.setMaxAccess(_G)
if mibBuilder.loadTexts:fsMobilityNotifyStaApRadioType.setStatus(_A)
class _FsMobilityNotifyStaVlanId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_FsMobilityNotifyStaVlanId_Type.__name__=_F
_FsMobilityNotifyStaVlanId_Object=MibScalar
fsMobilityNotifyStaVlanId=_FsMobilityNotifyStaVlanId_Object((1,3,6,1,4,1,52642,1,1,10,2,64,1,3,1,8),_FsMobilityNotifyStaVlanId_Type())
fsMobilityNotifyStaVlanId.setMaxAccess(_G)
if mibBuilder.loadTexts:fsMobilityNotifyStaVlanId.setStatus(_A)
class _FsMobilityNotifyStaWlanId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_FsMobilityNotifyStaWlanId_Type.__name__=_F
_FsMobilityNotifyStaWlanId_Object=MibScalar
fsMobilityNotifyStaWlanId=_FsMobilityNotifyStaWlanId_Object((1,3,6,1,4,1,52642,1,1,10,2,64,1,3,1,9),_FsMobilityNotifyStaWlanId_Type())
fsMobilityNotifyStaWlanId.setMaxAccess(_G)
if mibBuilder.loadTexts:fsMobilityNotifyStaWlanId.setStatus(_A)
_FsMobilityNotifyStaIpv6_Type=Ipv6Address
_FsMobilityNotifyStaIpv6_Object=MibScalar
fsMobilityNotifyStaIpv6=_FsMobilityNotifyStaIpv6_Object((1,3,6,1,4,1,52642,1,1,10,2,64,1,3,1,10),_FsMobilityNotifyStaIpv6_Type())
fsMobilityNotifyStaIpv6.setMaxAccess(_G)
if mibBuilder.loadTexts:fsMobilityNotifyStaIpv6.setStatus(_A)
class _FsMobilityNotifyStaAssoAuthMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('open',0),('wep',1),('dot1x-wep',2),('dot1x-wpa',3),('dot1x-wpa2',4),('mab',5),('psk-wpa',6),('psk-wpa2',7),('wapi',8)))
_FsMobilityNotifyStaAssoAuthMode_Type.__name__=_F
_FsMobilityNotifyStaAssoAuthMode_Object=MibScalar
fsMobilityNotifyStaAssoAuthMode=_FsMobilityNotifyStaAssoAuthMode_Object((1,3,6,1,4,1,52642,1,1,10,2,64,1,3,1,11),_FsMobilityNotifyStaAssoAuthMode_Type())
fsMobilityNotifyStaAssoAuthMode.setMaxAccess(_G)
if mibBuilder.loadTexts:fsMobilityNotifyStaAssoAuthMode.setStatus(_A)
class _FsMobilityNotifyStaNetAuthMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('open',0),('web',1)))
_FsMobilityNotifyStaNetAuthMode_Type.__name__=_F
_FsMobilityNotifyStaNetAuthMode_Object=MibScalar
fsMobilityNotifyStaNetAuthMode=_FsMobilityNotifyStaNetAuthMode_Object((1,3,6,1,4,1,52642,1,1,10,2,64,1,3,1,12),_FsMobilityNotifyStaNetAuthMode_Type())
fsMobilityNotifyStaNetAuthMode.setMaxAccess(_G)
if mibBuilder.loadTexts:fsMobilityNotifyStaNetAuthMode.setStatus(_A)
_FsMobilityNotifyStaSsid_Type=DisplayString
_FsMobilityNotifyStaSsid_Object=MibScalar
fsMobilityNotifyStaSsid=_FsMobilityNotifyStaSsid_Object((1,3,6,1,4,1,52642,1,1,10,2,64,1,3,1,13),_FsMobilityNotifyStaSsid_Type())
fsMobilityNotifyStaSsid.setMaxAccess(_G)
if mibBuilder.loadTexts:fsMobilityNotifyStaSsid.setStatus(_A)
_FsMobilityNotifyStaLinkRate_Type=Integer32
_FsMobilityNotifyStaLinkRate_Object=MibScalar
fsMobilityNotifyStaLinkRate=_FsMobilityNotifyStaLinkRate_Object((1,3,6,1,4,1,52642,1,1,10,2,64,1,3,1,14),_FsMobilityNotifyStaLinkRate_Type())
fsMobilityNotifyStaLinkRate.setMaxAccess(_G)
if mibBuilder.loadTexts:fsMobilityNotifyStaLinkRate.setStatus(_A)
_FsMobilityNotifyStaCurChan_Type=Integer32
_FsMobilityNotifyStaCurChan_Object=MibScalar
fsMobilityNotifyStaCurChan=_FsMobilityNotifyStaCurChan_Object((1,3,6,1,4,1,52642,1,1,10,2,64,1,3,1,15),_FsMobilityNotifyStaCurChan_Type())
fsMobilityNotifyStaCurChan.setMaxAccess(_G)
if mibBuilder.loadTexts:fsMobilityNotifyStaCurChan.setStatus(_A)
_FsMobilityNotifyStaClientType_Type=DisplayString
_FsMobilityNotifyStaClientType_Object=MibScalar
fsMobilityNotifyStaClientType=_FsMobilityNotifyStaClientType_Object((1,3,6,1,4,1,52642,1,1,10,2,64,1,3,1,16),_FsMobilityNotifyStaClientType_Type())
fsMobilityNotifyStaClientType.setMaxAccess(_G)
if mibBuilder.loadTexts:fsMobilityNotifyStaClientType.setStatus(_A)
_FsMobilityNotifyStaRssi_Type=Integer32
_FsMobilityNotifyStaRssi_Object=MibScalar
fsMobilityNotifyStaRssi=_FsMobilityNotifyStaRssi_Object((1,3,6,1,4,1,52642,1,1,10,2,64,1,3,1,17),_FsMobilityNotifyStaRssi_Type())
fsMobilityNotifyStaRssi.setMaxAccess(_G)
if mibBuilder.loadTexts:fsMobilityNotifyStaRssi.setStatus(_A)
_FsMobilityNotifyStaReason_Type=DisplayString
_FsMobilityNotifyStaReason_Object=MibScalar
fsMobilityNotifyStaReason=_FsMobilityNotifyStaReason_Object((1,3,6,1,4,1,52642,1,1,10,2,64,1,3,1,18),_FsMobilityNotifyStaReason_Type())
fsMobilityNotifyStaReason.setMaxAccess(_G)
if mibBuilder.loadTexts:fsMobilityNotifyStaReason.setStatus(_A)
_FsMobilityTrapStaIf_ObjectIdentity=ObjectIdentity
fsMobilityTrapStaIf=_FsMobilityTrapStaIf_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,64,1,3,2))
fsMobilityMIBGroup=ObjectGroup((1,3,6,1,4,1,52642,1,1,10,2,64,1,2,2,1))
fsMobilityMIBGroup.setObjects(*((_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_x),(_B,_y),(_B,_z),(_B,_A0),(_B,_A1),(_B,_A2),(_B,_A3),(_B,_A4),(_B,_A5),(_B,_A6),(_B,_A7),(_B,_A8),(_B,_A9),(_B,_AA),(_B,_AB),(_B,_AC),(_B,_AD),(_B,_AE),(_B,_AF),(_B,_AG),(_B,_AH),(_B,_AI),(_B,_AJ),(_B,_AK),(_B,_AL),(_B,_H),(_B,_I),(_B,_AM),(_B,_AN),(_B,_AO),(_B,_AP),(_B,_AQ),(_B,_AR),(_B,_J),(_B,_AS),(_B,_AT),(_B,_AU),(_B,_AV),(_B,_AW),(_B,_AX),(_B,_AY),(_B,_AZ),(_B,_Aa),(_B,_K),(_B,_L),(_B,_Ab),(_B,_Ac),(_B,_Ad),(_B,_Ae),(_B,_Af),(_B,_Ag),(_B,_Ah)))
if mibBuilder.loadTexts:fsMobilityMIBGroup.setStatus(_A)
fsMobilityNotifyStaOper=NotificationType((1,3,6,1,4,1,52642,1,1,10,2,64,1,3,2,1))
fsMobilityNotifyStaOper.setObjects(*((_B,_Ai),(_B,_Aj),(_B,_Ak),(_B,_Al),(_B,_Am),(_B,_An),(_B,_Ao),(_B,_Ap),(_B,_Aq),(_B,_Ar),(_B,_As),(_B,_At),(_B,_Au),(_B,_Av),(_B,_Aw),(_B,_Ax),(_B,_Ay),(_B,_Az)))
if mibBuilder.loadTexts:fsMobilityNotifyStaOper.setStatus(_A)
fsMobilityMIBCompliance=ModuleCompliance((1,3,6,1,4,1,52642,1,1,10,2,64,1,2,1,1))
fsMobilityMIBCompliance.setObjects((_B,_A_))
if mibBuilder.loadTexts:fsMobilityMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'fsMobilityMIB':fsMobilityMIB,'fsMobilityMIBObjects':fsMobilityMIBObjects,'fsMobility':fsMobility,'fsMobilityEntryTable':fsMobilityEntryTable,'fsMobilityEntry':fsMobilityEntry,_N:fsRoamGroupId,_T:fsRoamGroupName,_U:fsRoamGroupMyAddress,_V:fsRoamGroupMcEnable,_W:fsRoamGroupMcAddress,_X:fsRoamGroupKeepaliveCount,_Y:fsRoamGroupKeepaliveInterval,_Z:fsRoamGroupIsFast,_a:fsRoamGroupCreateStatus,'fsRoamGroupMyAddressIPv6':fsRoamGroupMyAddressIPv6,'fsMobilityMemberEntryTable':fsMobilityMemberEntryTable,'fsMobilityMemberEntry':fsMobilityMemberEntry,_O:fsRoamMemberGroupId,_P:fsRoamMemberPeerAddress,_b:fsRoamMemberIsList,_c:fsRoamMemberDataChannelIsOK,_d:fsRoamMemberDataChannelFailTimes,_e:fsRoamMemberDTLSIsClient,_f:fsRoamMemberDTLSIsOK,_g:fsRoamMemberCreateStatus,'fsAPCtrlCreatEntryTable':fsAPCtrlCreatEntryTable,'fsAPCtrlCreatEntry':fsAPCtrlCreatEntry,_Q:fsAPName,_h:fsPriority,_i:fsPrimaryACIP,_j:fsPrimaryACName,_k:fsSecondaryACIP,_l:fsSecondaryACName,_m:fsTertiaryACIP,_n:fsTertiaryACName,_o:fsAPCtrlCreatStatus,'fsWLANCtrlCreatEntryTable':fsWLANCtrlCreatEntryTable,'fsWLANCtrlCreatEntry':fsWLANCtrlCreatEntry,_R:fsWLANID,_p:fsAnchorACIPaddr,_q:fsWLANCtrlCreatStatus,'fsAnchorACIPaddrIPv6':fsAnchorACIPaddrIPv6,'fsMobilityACPing':fsMobilityACPing,_r:fsGlobalHandoffRequestsReceived,_s:fsGlobalHandoffEndRequestsReceived,_t:fsGlobalStateTransitionsDisabled,_u:fsGlobalResourceUnavailable,_v:fsRespondeHandoffRequestIgnored,_w:fsRespondePingPongHandoffRequestsDropped,_x:fsRespondeHandoffRequestsDroped,_y:fsRespondeHandoffRequestsDenied,_z:fsRespondeClientHandoffasLocal,_A0:fsRespondeClientHandoffasForeign,_A1:fsRespondeAnchorRequestsReceived,_A2:fsRespondeAnchorRequestDenied,_A3:fsRespondeAnchorTransferred,_A4:fsInitHandoffRequestsSent,_A5:fsInitHandoffReplyReceived,_A6:fsInitHandoffasLocalReceived,_A7:fsInitHandoffasForeignReceived,_A8:fsInitHandoffDenyReceived,_A9:fsInitAnchorRequestSent,_AA:fsInitAnchorDenyReceived,_AB:fsAPPriorityEnable,_AC:fsPrimaryBackUpACIP,_AD:fsPrimaryBackUpACName,_AE:fsSecondaryBackUpACIP,_AF:fsSecondaryBackUpACName,_AG:fsTeriaryBackUpACip,_AH:fsTeriaryBackUpACName,_AI:fsACIntraRoam,_AJ:fsACInterRoamIn,_AK:fsACInterRoamOut,_AL:fsMobilityACPingIPv6,'fsMobilityIPv6MemberEntryTable':fsMobilityIPv6MemberEntryTable,'fsMobilityIPv6MemberEntry':fsMobilityIPv6MemberEntry,_H:fsRoamIPv6MemberGroupId,_I:fsRoamIPv6MemberPeerAddress,_AM:fsRoamIPv6MemberIsList,_AN:fsRoamIPv6MemberDataChannelIsOK,_AO:fsRoamIPv6MemberDataChannelFailTimes,_AP:fsRoamIPv6MemberDTLSIsClient,_AQ:fsRoamIPv6MemberDTLSIsOK,_AR:fsRoamIPv6MemberCreateStatus,'fsMobilityUserEntryTable':fsMobilityUserEntryTable,'fsMobilityUserEntry':fsMobilityUserEntry,_J:fsRoamUserMac,_AS:fsRoamUserRoamType,_AT:fsRoamUserRoamOutAcAddressType,_AU:fsRoamUserRoamOutAcAddress,_AV:fsRoamUserRoamInAcAddressType,_AW:fsRoamUserRoamInAcAddress,_AX:fsRoamUserRoamOutApMac,_AY:fsRoamUserRoamInApMac,_AZ:fsRoamUserRoamOutVid,_Aa:fsRoamUserRoamInVid,'fsMobilityTrackEntryTable':fsMobilityTrackEntryTable,'fsMobilityTrackEntry':fsMobilityTrackEntry,_K:fsRoamTrackStaMac,_L:fsRoamTrackId,_Ab:fsRoamTrackAcAddressType,_Ac:fsRoamTrackAcAddress,_Ad:fsRoamTrackApMac,_Ae:fsRoamTrackRadioId,_Af:fsRoamTrackStaIp,_Ag:fsRoamTrackStaIpv6,_Ah:fsRoamTrackStaOnlineTime,'fsMobilityUserJsonTable':fsMobilityUserJsonTable,'fsMobilityUserJsonEntry':fsMobilityUserJsonEntry,_S:fsMobilityUserJsonMacAddr,'fsMobilityUserJsonContent':fsMobilityUserJsonContent,'fsMobilityIf':fsMobilityIf,'fsMobilityMIBCompliances':fsMobilityMIBCompliances,'fsMobilityMIBCompliance':fsMobilityMIBCompliance,'fsMobilityMIBGroups':fsMobilityMIBGroups,_A_:fsMobilityMIBGroup,'fsMobilityTrap':fsMobilityTrap,'fsMobilityTrapSta':fsMobilityTrapSta,_Ai:fsMobilityNotifyApMac,_Aj:fsMobilityNotifyStaMac,_Ak:fsMobilityNotifyApIp,_Al:fsMobilityNotifyStaIp,_Am:fsMobilityNotifyStaOperType,_An:fsMobilityNotifyStaApRadioId,_Ao:fsMobilityNotifyStaApRadioType,_Ap:fsMobilityNotifyStaVlanId,_Aq:fsMobilityNotifyStaWlanId,_Ar:fsMobilityNotifyStaIpv6,_As:fsMobilityNotifyStaAssoAuthMode,_At:fsMobilityNotifyStaNetAuthMode,_Au:fsMobilityNotifyStaSsid,_Av:fsMobilityNotifyStaLinkRate,_Aw:fsMobilityNotifyStaCurChan,_Ax:fsMobilityNotifyStaClientType,_Ay:fsMobilityNotifyStaRssi,_Az:fsMobilityNotifyStaReason,'fsMobilityTrapStaIf':fsMobilityTrapStaIf,'fsMobilityNotifyStaOper':fsMobilityNotifyStaOper})