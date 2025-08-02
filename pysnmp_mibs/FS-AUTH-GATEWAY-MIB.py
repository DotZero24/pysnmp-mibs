_B0='fsWebAuthTrapGroup'
_A_='fsWebAuthMIBGroup'
_Az='fsWebAuthSDGUserLeave'
_Ay='fsWebAuthUserExtLeave'
_Ax='fsWebAuthUserLeave'
_Aw='fsWebAuthTlv'
_Av='fsWebAuthTlvNum'
_Au='fsWebAuthPortIndex'
_At='fsWebAuthType'
_As='fsWebAuthStaTerminalId'
_Ar='fsWebAuthStaReplyMessage'
_Aq='fsWebAuthStaTerminalType'
_Ap='fsWebAuthStaCurChannel'
_Ao='fsWebAuthStaLinkRate'
_An='fsWebAuthStaSsid'
_Am='fsWebAuthStaRssi'
_Al='fsWebAuthStaNetAuthMode'
_Ak='fsWebAuthStaAssoAuthMode'
_Aj='fsWebAuthOperTime'
_Ai='fsWebAuthStaWlanId'
_Ah='fsWebAuthStaApRadioType'
_Ag='fsWebAuthStaApRadioId'
_Af='fsWebAuthStaIpv6'
_Ae='fsWebAuthApIp'
_Ad='fsWebAuthApMac'
_Ac='fsWebAuthMaximumOnlineUser'
_Ab='fsWebAuthCurrentUser'
_Aa='fsWebAuthCurrentOnlineUser'
_AZ='fsWebAuthOfflineDetectStatus'
_AY='fsWebAuthFreeAcctUrlStatus'
_AX='fsWebAuthFreeAcctIpStatus'
_AW='fsWebAuthDirectHostPortIfx'
_AV='fsWebAuthDirectHostStatus'
_AU='fsWebAuthDirectHostBindArpFlag'
_AT='fsWebAuthDirectHostPort8'
_AS='fsWebAuthDirectHostPort7'
_AR='fsWebAuthDirectHostPort6'
_AQ='fsWebAuthDirectHostPort5'
_AP='fsWebAuthDirectHostPort4'
_AO='fsWebAuthDirectHostPort3'
_AN='fsWebAuthDirectHostPort2'
_AM='fsWebAuthDirectHostPort1'
_AL='fsWebAuthDirectSiteBindArpFlag'
_AK='fsWebAuthDirectSiteStatus'
_AJ='authSDGUserStatus'
_AI='authSDGUserOtherPermissionType'
_AH='authSDGUserSecZonePermissionList'
_AG='authSDGUserSecZonePermissionType'
_AF='authSDGUserSecZoneName'
_AE='authSDGUserRoleName'
_AD='authSDGUserVrf'
_AC='authSDGUserTimeLimit'
_AB='authSDGUserOnlineFlag'
_AA='fsWebAuthWhiteListStatus'
_A9='fsWebAuthWhiteListBindArpFlag'
_A8='fsWebAuthWhiteListPort8'
_A7='fsWebAuthWhiteListPort7'
_A6='fsWebAuthWhiteListPort6'
_A5='fsWebAuthWhiteListPort5'
_A4='fsWebAuthWhiteListPort4'
_A3='fsWebAuthWhiteListPort3'
_A2='fsWebAuthWhiteListPort2'
_A1='fsWebAuthWhiteListPort1'
_A0='authUserExtStatus'
_z='authUserExtTimeLimit'
_y='authUserExtOnlineFlag'
_x='authUserOtherPermissionType'
_w='authUserSecZonePermissionList'
_v='authUserSecZonePermissionType'
_u='authUserSecZoneName'
_t='authUserRoleName'
_s='authUserStatus'
_r='authUserTimeLimit'
_q='authUserOnlineFlag'
_p='fsAuthUserMIBIpAddress'
_o='fsAuthMacUserMacAddr'
_n='InetAddress'
_m='fsWebAuthStaTerminateCause'
_l='fsWebAuthStaUsername'
_k='fsWebAuthStaVlanId'
_j='fsWebAuthStaOperType'
_i='fsWebAuthStaIp'
_h='fsWebAuthStaMac'
_g='authSDGUserTerminateCause'
_f='authSDGUserTimeUsed'
_e='authUserExtErrCause'
_d='authUserExtTimeUsed'
_c='authUserExtVlanId'
_b='authUserExtIfIndex'
_a='authUserExtMac'
_Z='authUserTerminateCause'
_Y='authUserTimeUsed'
_X='fsWebAuthOfflineDetectime'
_W='fsWebAuthFreeAcctUrl'
_V='fsWebAuthFreeAcctIpNetMask'
_U='fsWebAuthFreeAcctIpAddress'
_T='fsWebAuthDirectHostNetMask'
_S='fsWebAuthDirectHostAddress'
_R='fsWebAuthDirectSiteNetMask'
_Q='fsWebAuthDirectSiteAddress'
_P='yes'
_O='fsWebAuthWhiteListNetMask'
_N='fsWebAuthWhiteListAddress'
_M='authSDGUserIpAddr'
_L='authSDGUserVrfg'
_K='authUserExtAddr'
_J='authUserExtAddrType'
_I='authUserIpAddr'
_H='DisplayString'
_G='OctetString'
_F='Integer32'
_E='accessible-for-notify'
_D='read-only'
_C='read-create'
_B='current'
_A='FS-AUTH-GATEWAY-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_G,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
fsMgmt,=mibBuilder.importSymbols('FS-SMI','fsMgmt')
IfIndex,=mibBuilder.importSymbols('FS-TC','IfIndex')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB',_n,'InetAddressType')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_H,'MacAddress','PhysAddress','RowStatus','TextualConvention')
fsWebAuthMIB=ModuleIdentity((1,3,6,1,4,1,52642,1,1,10,2,40))
if mibBuilder.loadTexts:fsWebAuthMIB.setRevisions(('2010-03-08 00:00','2010-02-22 00:00','2009-04-16 00:00'))
_FsWebAuthMIBObjects_ObjectIdentity=ObjectIdentity
fsWebAuthMIBObjects=_FsWebAuthMIBObjects_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,40,1))
_FsWebAuthUserTable_Object=MibTable
fsWebAuthUserTable=_FsWebAuthUserTable_Object((1,3,6,1,4,1,52642,1,1,10,2,40,1,1))
if mibBuilder.loadTexts:fsWebAuthUserTable.setStatus(_B)
_FsWebAuthUserEntry_Object=MibTableRow
fsWebAuthUserEntry=_FsWebAuthUserEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,40,1,1,1))
fsWebAuthUserEntry.setIndexNames((0,_A,_I))
if mibBuilder.loadTexts:fsWebAuthUserEntry.setStatus(_B)
_AuthUserIpAddr_Type=IpAddress
_AuthUserIpAddr_Object=MibTableColumn
authUserIpAddr=_AuthUserIpAddr_Object((1,3,6,1,4,1,52642,1,1,10,2,40,1,1,1,1),_AuthUserIpAddr_Type())
authUserIpAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:authUserIpAddr.setStatus(_B)
_AuthUserOnlineFlag_Type=Gauge32
_AuthUserOnlineFlag_Object=MibTableColumn
authUserOnlineFlag=_AuthUserOnlineFlag_Object((1,3,6,1,4,1,52642,1,1,10,2,40,1,1,1,2),_AuthUserOnlineFlag_Type())
authUserOnlineFlag.setMaxAccess(_D)
if mibBuilder.loadTexts:authUserOnlineFlag.setStatus(_B)
_AuthUserTimeLimit_Type=Gauge32
_AuthUserTimeLimit_Object=MibTableColumn
authUserTimeLimit=_AuthUserTimeLimit_Object((1,3,6,1,4,1,52642,1,1,10,2,40,1,1,1,3),_AuthUserTimeLimit_Type())
authUserTimeLimit.setMaxAccess(_C)
if mibBuilder.loadTexts:authUserTimeLimit.setStatus(_B)
_AuthUserTimeUsed_Type=Gauge32
_AuthUserTimeUsed_Object=MibTableColumn
authUserTimeUsed=_AuthUserTimeUsed_Object((1,3,6,1,4,1,52642,1,1,10,2,40,1,1,1,4),_AuthUserTimeUsed_Type())
authUserTimeUsed.setMaxAccess(_D)
if mibBuilder.loadTexts:authUserTimeUsed.setStatus(_B)
_AuthUserStatus_Type=RowStatus
_AuthUserStatus_Object=MibTableColumn
authUserStatus=_AuthUserStatus_Object((1,3,6,1,4,1,52642,1,1,10,2,40,1,1,1,19),_AuthUserStatus_Type())
authUserStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:authUserStatus.setStatus(_B)
class _AuthUserRoleName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(32,32));fixedLength=32
_AuthUserRoleName_Type.__name__=_G
_AuthUserRoleName_Object=MibTableColumn
authUserRoleName=_AuthUserRoleName_Object((1,3,6,1,4,1,52642,1,1,10,2,40,1,1,1,20),_AuthUserRoleName_Type())
authUserRoleName.setMaxAccess(_C)
if mibBuilder.loadTexts:authUserRoleName.setStatus(_B)
class _AuthUserSecZoneName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(32,32));fixedLength=32
_AuthUserSecZoneName_Type.__name__=_G
_AuthUserSecZoneName_Object=MibTableColumn
authUserSecZoneName=_AuthUserSecZoneName_Object((1,3,6,1,4,1,52642,1,1,10,2,40,1,1,1,21),_AuthUserSecZoneName_Type())
authUserSecZoneName.setMaxAccess(_C)
if mibBuilder.loadTexts:authUserSecZoneName.setStatus(_B)
_AuthUserSecZonePermissionType_Type=Gauge32
_AuthUserSecZonePermissionType_Object=MibTableColumn
authUserSecZonePermissionType=_AuthUserSecZonePermissionType_Object((1,3,6,1,4,1,52642,1,1,10,2,40,1,1,1,22),_AuthUserSecZonePermissionType_Type())
authUserSecZonePermissionType.setMaxAccess(_C)
if mibBuilder.loadTexts:authUserSecZonePermissionType.setStatus(_B)
class _AuthUserSecZonePermissionList_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(512,512));fixedLength=512
_AuthUserSecZonePermissionList_Type.__name__=_G
_AuthUserSecZonePermissionList_Object=MibTableColumn
authUserSecZonePermissionList=_AuthUserSecZonePermissionList_Object((1,3,6,1,4,1,52642,1,1,10,2,40,1,1,1,23),_AuthUserSecZonePermissionList_Type())
authUserSecZonePermissionList.setMaxAccess(_C)
if mibBuilder.loadTexts:authUserSecZonePermissionList.setStatus(_B)
_AuthUserOtherPermissionType_Type=Gauge32
_AuthUserOtherPermissionType_Object=MibTableColumn
authUserOtherPermissionType=_AuthUserOtherPermissionType_Object((1,3,6,1,4,1,52642,1,1,10,2,40,1,1,1,24),_AuthUserOtherPermissionType_Type())
authUserOtherPermissionType.setMaxAccess(_C)
if mibBuilder.loadTexts:authUserOtherPermissionType.setStatus(_B)
_AuthUserTerminateCause_Type=Gauge32
_AuthUserTerminateCause_Object=MibTableColumn
authUserTerminateCause=_AuthUserTerminateCause_Object((1,3,6,1,4,1,52642,1,1,10,2,40,1,1,1,25),_AuthUserTerminateCause_Type())
authUserTerminateCause.setMaxAccess(_D)
if mibBuilder.loadTexts:authUserTerminateCause.setStatus(_B)
_FsWebAuthUserExtTable_Object=MibTable
fsWebAuthUserExtTable=_FsWebAuthUserExtTable_Object((1,3,6,1,4,1,52642,1,1,10,2,40,1,2))
if mibBuilder.loadTexts:fsWebAuthUserExtTable.setStatus(_B)
_FsWebAuthUserExtEntry_Object=MibTableRow
fsWebAuthUserExtEntry=_FsWebAuthUserExtEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,40,1,2,1))
fsWebAuthUserExtEntry.setIndexNames((0,_A,_J),(0,_A,_K))
if mibBuilder.loadTexts:fsWebAuthUserExtEntry.setStatus(_B)
_AuthUserExtAddrType_Type=InetAddressType
_AuthUserExtAddrType_Object=MibTableColumn
authUserExtAddrType=_AuthUserExtAddrType_Object((1,3,6,1,4,1,52642,1,1,10,2,40,1,2,1,1),_AuthUserExtAddrType_Type())
authUserExtAddrType.setMaxAccess(_D)
if mibBuilder.loadTexts:authUserExtAddrType.setStatus(_B)
class _AuthUserExtAddr_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_AuthUserExtAddr_Type.__name__=_n
_AuthUserExtAddr_Object=MibTableColumn
authUserExtAddr=_AuthUserExtAddr_Object((1,3,6,1,4,1,52642,1,1,10,2,40,1,2,1,2),_AuthUserExtAddr_Type())
authUserExtAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:authUserExtAddr.setStatus(_B)
_AuthUserExtMac_Type=MacAddress
_AuthUserExtMac_Object=MibTableColumn
authUserExtMac=_AuthUserExtMac_Object((1,3,6,1,4,1,52642,1,1,10,2,40,1,2,1,3),_AuthUserExtMac_Type())
authUserExtMac.setMaxAccess(_D)
if mibBuilder.loadTexts:authUserExtMac.setStatus(_B)
_AuthUserExtIfIndex_Type=IfIndex
_AuthUserExtIfIndex_Object=MibTableColumn
authUserExtIfIndex=_AuthUserExtIfIndex_Object((1,3,6,1,4,1,52642,1,1,10,2,40,1,2,1,4),_AuthUserExtIfIndex_Type())
authUserExtIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:authUserExtIfIndex.setStatus(_B)
_AuthUserExtVlanId_Type=Unsigned32
_AuthUserExtVlanId_Object=MibTableColumn
authUserExtVlanId=_AuthUserExtVlanId_Object((1,3,6,1,4,1,52642,1,1,10,2,40,1,2,1,5),_AuthUserExtVlanId_Type())
authUserExtVlanId.setMaxAccess(_D)
if mibBuilder.loadTexts:authUserExtVlanId.setStatus(_B)
_AuthUserExtOnlineFlag_Type=Gauge32
_AuthUserExtOnlineFlag_Object=MibTableColumn
authUserExtOnlineFlag=_AuthUserExtOnlineFlag_Object((1,3,6,1,4,1,52642,1,1,10,2,40,1,2,1,6),_AuthUserExtOnlineFlag_Type())
authUserExtOnlineFlag.setMaxAccess(_D)
if mibBuilder.loadTexts:authUserExtOnlineFlag.setStatus(_B)
_AuthUserExtTimeLimit_Type=Gauge32
_AuthUserExtTimeLimit_Object=MibTableColumn
authUserExtTimeLimit=_AuthUserExtTimeLimit_Object((1,3,6,1,4,1,52642,1,1,10,2,40,1,2,1,7),_AuthUserExtTimeLimit_Type())
authUserExtTimeLimit.setMaxAccess(_C)
if mibBuilder.loadTexts:authUserExtTimeLimit.setStatus(_B)
_AuthUserExtTimeUsed_Type=Gauge32
_AuthUserExtTimeUsed_Object=MibTableColumn
authUserExtTimeUsed=_AuthUserExtTimeUsed_Object((1,3,6,1,4,1,52642,1,1,10,2,40,1,2,1,8),_AuthUserExtTimeUsed_Type())
authUserExtTimeUsed.setMaxAccess(_D)
if mibBuilder.loadTexts:authUserExtTimeUsed.setStatus(_B)
class _AuthUserExtErrCause_Type(DisplayString):defaultValue=OctetString('');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_AuthUserExtErrCause_Type.__name__=_H
_AuthUserExtErrCause_Object=MibTableColumn
authUserExtErrCause=_AuthUserExtErrCause_Object((1,3,6,1,4,1,52642,1,1,10,2,40,1,2,1,9),_AuthUserExtErrCause_Type())
authUserExtErrCause.setMaxAccess(_D)
if mibBuilder.loadTexts:authUserExtErrCause.setStatus(_B)
_AuthUserExtStatus_Type=RowStatus
_AuthUserExtStatus_Object=MibTableColumn
authUserExtStatus=_AuthUserExtStatus_Object((1,3,6,1,4,1,52642,1,1,10,2,40,1,2,1,10),_AuthUserExtStatus_Type())
authUserExtStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:authUserExtStatus.setStatus(_B)
_FsWebAuthWhiteListTable_Object=MibTable
fsWebAuthWhiteListTable=_FsWebAuthWhiteListTable_Object((1,3,6,1,4,1,52642,1,1,10,2,40,1,3))
if mibBuilder.loadTexts:fsWebAuthWhiteListTable.setStatus(_B)
_FsWebAuthWhiteListEntry_Object=MibTableRow
fsWebAuthWhiteListEntry=_FsWebAuthWhiteListEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,40,1,3,1))
fsWebAuthWhiteListEntry.setIndexNames((0,_A,_N),(0,_A,_O))
if mibBuilder.loadTexts:fsWebAuthWhiteListEntry.setStatus(_B)
_FsWebAuthWhiteListAddress_Type=IpAddress
_FsWebAuthWhiteListAddress_Object=MibTableColumn
fsWebAuthWhiteListAddress=_FsWebAuthWhiteListAddress_Object((1,3,6,1,4,1,52642,1,1,10,2,40,1,3,1,1),_FsWebAuthWhiteListAddress_Type())
fsWebAuthWhiteListAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:fsWebAuthWhiteListAddress.setStatus(_B)
_FsWebAuthWhiteListNetMask_Type=IpAddress
_FsWebAuthWhiteListNetMask_Object=MibTableColumn
fsWebAuthWhiteListNetMask=_FsWebAuthWhiteListNetMask_Object((1,3,6,1,4,1,52642,1,1,10,2,40,1,3,1,2),_FsWebAuthWhiteListNetMask_Type())
fsWebAuthWhiteListNetMask.setMaxAccess(_D)
if mibBuilder.loadTexts:fsWebAuthWhiteListNetMask.setStatus(_B)
_FsWebAuthWhiteListPort1_Type=Unsigned32
_FsWebAuthWhiteListPort1_Object=MibTableColumn
fsWebAuthWhiteListPort1=_FsWebAuthWhiteListPort1_Object((1,3,6,1,4,1,52642,1,1,10,2,40,1,3,1,3),_FsWebAuthWhiteListPort1_Type())
fsWebAuthWhiteListPort1.setMaxAccess(_C)
if mibBuilder.loadTexts:fsWebAuthWhiteListPort1.setStatus(_B)
_FsWebAuthWhiteListPort2_Type=Unsigned32
_FsWebAuthWhiteListPort2_Object=MibTableColumn
fsWebAuthWhiteListPort2=_FsWebAuthWhiteListPort2_Object((1,3,6,1,4,1,52642,1,1,10,2,40,1,3,1,4),_FsWebAuthWhiteListPort2_Type())
fsWebAuthWhiteListPort2.setMaxAccess(_C)
if mibBuilder.loadTexts:fsWebAuthWhiteListPort2.setStatus(_B)
_FsWebAuthWhiteListPort3_Type=Unsigned32
_FsWebAuthWhiteListPort3_Object=MibTableColumn
fsWebAuthWhiteListPort3=_FsWebAuthWhiteListPort3_Object((1,3,6,1,4,1,52642,1,1,10,2,40,1,3,1,5),_FsWebAuthWhiteListPort3_Type())
fsWebAuthWhiteListPort3.setMaxAccess(_C)
if mibBuilder.loadTexts:fsWebAuthWhiteListPort3.setStatus(_B)
_FsWebAuthWhiteListPort4_Type=Unsigned32
_FsWebAuthWhiteListPort4_Object=MibTableColumn
fsWebAuthWhiteListPort4=_FsWebAuthWhiteListPort4_Object((1,3,6,1,4,1,52642,1,1,10,2,40,1,3,1,6),_FsWebAuthWhiteListPort4_Type())
fsWebAuthWhiteListPort4.setMaxAccess(_C)
if mibBuilder.loadTexts:fsWebAuthWhiteListPort4.setStatus(_B)
_FsWebAuthWhiteListPort5_Type=Unsigned32
_FsWebAuthWhiteListPort5_Object=MibTableColumn
fsWebAuthWhiteListPort5=_FsWebAuthWhiteListPort5_Object((1,3,6,1,4,1,52642,1,1,10,2,40,1,3,1,7),_FsWebAuthWhiteListPort5_Type())
fsWebAuthWhiteListPort5.setMaxAccess(_C)
if mibBuilder.loadTexts:fsWebAuthWhiteListPort5.setStatus(_B)
_FsWebAuthWhiteListPort6_Type=Unsigned32
_FsWebAuthWhiteListPort6_Object=MibTableColumn
fsWebAuthWhiteListPort6=_FsWebAuthWhiteListPort6_Object((1,3,6,1,4,1,52642,1,1,10,2,40,1,3,1,8),_FsWebAuthWhiteListPort6_Type())
fsWebAuthWhiteListPort6.setMaxAccess(_C)
if mibBuilder.loadTexts:fsWebAuthWhiteListPort6.setStatus(_B)
_FsWebAuthWhiteListPort7_Type=Unsigned32
_FsWebAuthWhiteListPort7_Object=MibTableColumn
fsWebAuthWhiteListPort7=_FsWebAuthWhiteListPort7_Object((1,3,6,1,4,1,52642,1,1,10,2,40,1,3,1,9),_FsWebAuthWhiteListPort7_Type())
fsWebAuthWhiteListPort7.setMaxAccess(_C)
if mibBuilder.loadTexts:fsWebAuthWhiteListPort7.setStatus(_B)
_FsWebAuthWhiteListPort8_Type=Unsigned32
_FsWebAuthWhiteListPort8_Object=MibTableColumn
fsWebAuthWhiteListPort8=_FsWebAuthWhiteListPort8_Object((1,3,6,1,4,1,52642,1,1,10,2,40,1,3,1,10),_FsWebAuthWhiteListPort8_Type())
fsWebAuthWhiteListPort8.setMaxAccess(_C)
if mibBuilder.loadTexts:fsWebAuthWhiteListPort8.setStatus(_B)
class _FsWebAuthWhiteListBindArpFlag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('no',0),(_P,1)))
_FsWebAuthWhiteListBindArpFlag_Type.__name__=_F
_FsWebAuthWhiteListBindArpFlag_Object=MibTableColumn
fsWebAuthWhiteListBindArpFlag=_FsWebAuthWhiteListBindArpFlag_Object((1,3,6,1,4,1,52642,1,1,10,2,40,1,3,1,11),_FsWebAuthWhiteListBindArpFlag_Type())
fsWebAuthWhiteListBindArpFlag.setMaxAccess(_C)
if mibBuilder.loadTexts:fsWebAuthWhiteListBindArpFlag.setStatus(_B)
_FsWebAuthWhiteListStatus_Type=RowStatus
_FsWebAuthWhiteListStatus_Object=MibTableColumn
fsWebAuthWhiteListStatus=_FsWebAuthWhiteListStatus_Object((1,3,6,1,4,1,52642,1,1,10,2,40,1,3,1,12),_FsWebAuthWhiteListStatus_Type())
fsWebAuthWhiteListStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:fsWebAuthWhiteListStatus.setStatus(_B)
_FsWebAuthSDGUserTable_Object=MibTable
fsWebAuthSDGUserTable=_FsWebAuthSDGUserTable_Object((1,3,6,1,4,1,52642,1,1,10,2,40,1,4))
if mibBuilder.loadTexts:fsWebAuthSDGUserTable.setStatus(_B)
_FsWebAuthSDGUserEntry_Object=MibTableRow
fsWebAuthSDGUserEntry=_FsWebAuthSDGUserEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,40,1,4,1))
fsWebAuthSDGUserEntry.setIndexNames((0,_A,_L),(0,_A,_M))
if mibBuilder.loadTexts:fsWebAuthSDGUserEntry.setStatus(_B)
class _AuthSDGUserVrfg_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_AuthSDGUserVrfg_Type.__name__=_H
_AuthSDGUserVrfg_Object=MibTableColumn
authSDGUserVrfg=_AuthSDGUserVrfg_Object((1,3,6,1,4,1,52642,1,1,10,2,40,1,4,1,1),_AuthSDGUserVrfg_Type())
authSDGUserVrfg.setMaxAccess(_D)
if mibBuilder.loadTexts:authSDGUserVrfg.setStatus(_B)
_AuthSDGUserIpAddr_Type=IpAddress
_AuthSDGUserIpAddr_Object=MibTableColumn
authSDGUserIpAddr=_AuthSDGUserIpAddr_Object((1,3,6,1,4,1,52642,1,1,10,2,40,1,4,1,2),_AuthSDGUserIpAddr_Type())
authSDGUserIpAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:authSDGUserIpAddr.setStatus(_B)
_AuthSDGUserOnlineFlag_Type=Gauge32
_AuthSDGUserOnlineFlag_Object=MibTableColumn
authSDGUserOnlineFlag=_AuthSDGUserOnlineFlag_Object((1,3,6,1,4,1,52642,1,1,10,2,40,1,4,1,3),_AuthSDGUserOnlineFlag_Type())
authSDGUserOnlineFlag.setMaxAccess(_D)
if mibBuilder.loadTexts:authSDGUserOnlineFlag.setStatus(_B)
_AuthSDGUserTimeLimit_Type=Gauge32
_AuthSDGUserTimeLimit_Object=MibTableColumn
authSDGUserTimeLimit=_AuthSDGUserTimeLimit_Object((1,3,6,1,4,1,52642,1,1,10,2,40,1,4,1,4),_AuthSDGUserTimeLimit_Type())
authSDGUserTimeLimit.setMaxAccess(_C)
if mibBuilder.loadTexts:authSDGUserTimeLimit.setStatus(_B)
_AuthSDGUserTimeUsed_Type=Gauge32
_AuthSDGUserTimeUsed_Object=MibTableColumn
authSDGUserTimeUsed=_AuthSDGUserTimeUsed_Object((1,3,6,1,4,1,52642,1,1,10,2,40,1,4,1,5),_AuthSDGUserTimeUsed_Type())
authSDGUserTimeUsed.setMaxAccess(_D)
if mibBuilder.loadTexts:authSDGUserTimeUsed.setStatus(_B)
_AuthSDGUserVrf_Type=DisplayString
_AuthSDGUserVrf_Object=MibTableColumn
authSDGUserVrf=_AuthSDGUserVrf_Object((1,3,6,1,4,1,52642,1,1,10,2,40,1,4,1,6),_AuthSDGUserVrf_Type())
authSDGUserVrf.setMaxAccess(_D)
if mibBuilder.loadTexts:authSDGUserVrf.setStatus(_B)
class _AuthSDGUserRoleName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(32,32));fixedLength=32
_AuthSDGUserRoleName_Type.__name__=_G
_AuthSDGUserRoleName_Object=MibTableColumn
authSDGUserRoleName=_AuthSDGUserRoleName_Object((1,3,6,1,4,1,52642,1,1,10,2,40,1,4,1,21),_AuthSDGUserRoleName_Type())
authSDGUserRoleName.setMaxAccess(_C)
if mibBuilder.loadTexts:authSDGUserRoleName.setStatus(_B)
class _AuthSDGUserSecZoneName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(32,32));fixedLength=32
_AuthSDGUserSecZoneName_Type.__name__=_G
_AuthSDGUserSecZoneName_Object=MibTableColumn
authSDGUserSecZoneName=_AuthSDGUserSecZoneName_Object((1,3,6,1,4,1,52642,1,1,10,2,40,1,4,1,22),_AuthSDGUserSecZoneName_Type())
authSDGUserSecZoneName.setMaxAccess(_C)
if mibBuilder.loadTexts:authSDGUserSecZoneName.setStatus(_B)
_AuthSDGUserSecZonePermissionType_Type=Gauge32
_AuthSDGUserSecZonePermissionType_Object=MibTableColumn
authSDGUserSecZonePermissionType=_AuthSDGUserSecZonePermissionType_Object((1,3,6,1,4,1,52642,1,1,10,2,40,1,4,1,23),_AuthSDGUserSecZonePermissionType_Type())
authSDGUserSecZonePermissionType.setMaxAccess(_C)
if mibBuilder.loadTexts:authSDGUserSecZonePermissionType.setStatus(_B)
class _AuthSDGUserSecZonePermissionList_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(512,512));fixedLength=512
_AuthSDGUserSecZonePermissionList_Type.__name__=_G
_AuthSDGUserSecZonePermissionList_Object=MibTableColumn
authSDGUserSecZonePermissionList=_AuthSDGUserSecZonePermissionList_Object((1,3,6,1,4,1,52642,1,1,10,2,40,1,4,1,24),_AuthSDGUserSecZonePermissionList_Type())
authSDGUserSecZonePermissionList.setMaxAccess(_C)
if mibBuilder.loadTexts:authSDGUserSecZonePermissionList.setStatus(_B)
_AuthSDGUserOtherPermissionType_Type=Gauge32
_AuthSDGUserOtherPermissionType_Object=MibTableColumn
authSDGUserOtherPermissionType=_AuthSDGUserOtherPermissionType_Object((1,3,6,1,4,1,52642,1,1,10,2,40,1,4,1,25),_AuthSDGUserOtherPermissionType_Type())
authSDGUserOtherPermissionType.setMaxAccess(_C)
if mibBuilder.loadTexts:authSDGUserOtherPermissionType.setStatus(_B)
_AuthSDGUserTerminateCause_Type=Gauge32
_AuthSDGUserTerminateCause_Object=MibTableColumn
authSDGUserTerminateCause=_AuthSDGUserTerminateCause_Object((1,3,6,1,4,1,52642,1,1,10,2,40,1,4,1,26),_AuthSDGUserTerminateCause_Type())
authSDGUserTerminateCause.setMaxAccess(_D)
if mibBuilder.loadTexts:authSDGUserTerminateCause.setStatus(_B)
_AuthSDGUserStatus_Type=RowStatus
_AuthSDGUserStatus_Object=MibTableColumn
authSDGUserStatus=_AuthSDGUserStatus_Object((1,3,6,1,4,1,52642,1,1,10,2,40,1,4,1,27),_AuthSDGUserStatus_Type())
authSDGUserStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:authSDGUserStatus.setStatus(_B)
_FsWebAuthMacUserTable_Object=MibTable
fsWebAuthMacUserTable=_FsWebAuthMacUserTable_Object((1,3,6,1,4,1,52642,1,1,10,2,40,1,5))
if mibBuilder.loadTexts:fsWebAuthMacUserTable.setStatus(_B)
_FsWebAuthMacUserEntry_Object=MibTableRow
fsWebAuthMacUserEntry=_FsWebAuthMacUserEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,40,1,5,1))
fsWebAuthMacUserEntry.setIndexNames((0,_A,_o))
if mibBuilder.loadTexts:fsWebAuthMacUserEntry.setStatus(_B)
_FsAuthMacUserMacAddr_Type=MacAddress
_FsAuthMacUserMacAddr_Object=MibTableColumn
fsAuthMacUserMacAddr=_FsAuthMacUserMacAddr_Object((1,3,6,1,4,1,52642,1,1,10,2,40,1,5,1,1),_FsAuthMacUserMacAddr_Type())
fsAuthMacUserMacAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:fsAuthMacUserMacAddr.setStatus(_B)
class _FsAuthMacUserName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(253,253));fixedLength=253
_FsAuthMacUserName_Type.__name__=_G
_FsAuthMacUserName_Object=MibTableColumn
fsAuthMacUserName=_FsAuthMacUserName_Object((1,3,6,1,4,1,52642,1,1,10,2,40,1,5,1,2),_FsAuthMacUserName_Type())
fsAuthMacUserName.setMaxAccess(_D)
if mibBuilder.loadTexts:fsAuthMacUserName.setStatus(_B)
class _FsAuthMacUserTerminalId_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(253,253));fixedLength=253
_FsAuthMacUserTerminalId_Type.__name__=_G
_FsAuthMacUserTerminalId_Object=MibTableColumn
fsAuthMacUserTerminalId=_FsAuthMacUserTerminalId_Object((1,3,6,1,4,1,52642,1,1,10,2,40,1,5,1,3),_FsAuthMacUserTerminalId_Type())
fsAuthMacUserTerminalId.setMaxAccess(_D)
if mibBuilder.loadTexts:fsAuthMacUserTerminalId.setStatus(_B)
_FsWebAuthUserMIB_ObjectIdentity=ObjectIdentity
fsWebAuthUserMIB=_FsWebAuthUserMIB_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,40,1,6))
_FsWebAuthUserMIBTable_Object=MibTable
fsWebAuthUserMIBTable=_FsWebAuthUserMIBTable_Object((1,3,6,1,4,1,52642,1,1,10,2,40,1,6,1))
if mibBuilder.loadTexts:fsWebAuthUserMIBTable.setStatus(_B)
_FsWebAuthUserMIBEntry_Object=MibTableRow
fsWebAuthUserMIBEntry=_FsWebAuthUserMIBEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,40,1,6,1,1))
fsWebAuthUserMIBEntry.setIndexNames((0,_A,_p))
if mibBuilder.loadTexts:fsWebAuthUserMIBEntry.setStatus(_B)
_FsAuthUserMIBIpAddress_Type=IpAddress
_FsAuthUserMIBIpAddress_Object=MibTableColumn
fsAuthUserMIBIpAddress=_FsAuthUserMIBIpAddress_Object((1,3,6,1,4,1,52642,1,1,10,2,40,1,6,1,1,1),_FsAuthUserMIBIpAddress_Type())
fsAuthUserMIBIpAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:fsAuthUserMIBIpAddress.setStatus(_B)
_FsAuthUserMIBName_Type=OctetString
_FsAuthUserMIBName_Object=MibTableColumn
fsAuthUserMIBName=_FsAuthUserMIBName_Object((1,3,6,1,4,1,52642,1,1,10,2,40,1,6,1,1,2),_FsAuthUserMIBName_Type())
fsAuthUserMIBName.setMaxAccess(_D)
if mibBuilder.loadTexts:fsAuthUserMIBName.setStatus(_B)
_FsAuthUserMIBAuthType_Type=Gauge32
_FsAuthUserMIBAuthType_Object=MibTableColumn
fsAuthUserMIBAuthType=_FsAuthUserMIBAuthType_Object((1,3,6,1,4,1,52642,1,1,10,2,40,1,6,1,1,3),_FsAuthUserMIBAuthType_Type())
fsAuthUserMIBAuthType.setMaxAccess(_D)
if mibBuilder.loadTexts:fsAuthUserMIBAuthType.setStatus(_B)
_FsAuthUserMIBMacAddress_Type=MacAddress
_FsAuthUserMIBMacAddress_Object=MibTableColumn
fsAuthUserMIBMacAddress=_FsAuthUserMIBMacAddress_Object((1,3,6,1,4,1,52642,1,1,10,2,40,1,6,1,1,4),_FsAuthUserMIBMacAddress_Type())
fsAuthUserMIBMacAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:fsAuthUserMIBMacAddress.setStatus(_B)
_FsAuthUserMIBVlanId_Type=Gauge32
_FsAuthUserMIBVlanId_Object=MibTableColumn
fsAuthUserMIBVlanId=_FsAuthUserMIBVlanId_Object((1,3,6,1,4,1,52642,1,1,10,2,40,1,6,1,1,5),_FsAuthUserMIBVlanId_Type())
fsAuthUserMIBVlanId.setMaxAccess(_D)
if mibBuilder.loadTexts:fsAuthUserMIBVlanId.setStatus(_B)
_FsAuthUserMIBPortIndex_Type=Gauge32
_FsAuthUserMIBPortIndex_Object=MibTableColumn
fsAuthUserMIBPortIndex=_FsAuthUserMIBPortIndex_Object((1,3,6,1,4,1,52642,1,1,10,2,40,1,6,1,1,6),_FsAuthUserMIBPortIndex_Type())
fsAuthUserMIBPortIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:fsAuthUserMIBPortIndex.setStatus(_B)
_FsAuthUserMIBTimeUsed_Type=Gauge32
_FsAuthUserMIBTimeUsed_Object=MibTableColumn
fsAuthUserMIBTimeUsed=_FsAuthUserMIBTimeUsed_Object((1,3,6,1,4,1,52642,1,1,10,2,40,1,6,1,1,7),_FsAuthUserMIBTimeUsed_Type())
fsAuthUserMIBTimeUsed.setMaxAccess(_D)
if mibBuilder.loadTexts:fsAuthUserMIBTimeUsed.setStatus(_B)
_FsWebAuthDirectSiteTable_Object=MibTable
fsWebAuthDirectSiteTable=_FsWebAuthDirectSiteTable_Object((1,3,6,1,4,1,52642,1,1,10,2,40,1,7))
if mibBuilder.loadTexts:fsWebAuthDirectSiteTable.setStatus(_B)
_FsWebAuthDirectSiteEntry_Object=MibTableRow
fsWebAuthDirectSiteEntry=_FsWebAuthDirectSiteEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,40,1,7,1))
fsWebAuthDirectSiteEntry.setIndexNames((0,_A,_Q),(0,_A,_R))
if mibBuilder.loadTexts:fsWebAuthDirectSiteEntry.setStatus(_B)
_FsWebAuthDirectSiteAddress_Type=IpAddress
_FsWebAuthDirectSiteAddress_Object=MibTableColumn
fsWebAuthDirectSiteAddress=_FsWebAuthDirectSiteAddress_Object((1,3,6,1,4,1,52642,1,1,10,2,40,1,7,1,1),_FsWebAuthDirectSiteAddress_Type())
fsWebAuthDirectSiteAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:fsWebAuthDirectSiteAddress.setStatus(_B)
_FsWebAuthDirectSiteNetMask_Type=IpAddress
_FsWebAuthDirectSiteNetMask_Object=MibTableColumn
fsWebAuthDirectSiteNetMask=_FsWebAuthDirectSiteNetMask_Object((1,3,6,1,4,1,52642,1,1,10,2,40,1,7,1,2),_FsWebAuthDirectSiteNetMask_Type())
fsWebAuthDirectSiteNetMask.setMaxAccess(_D)
if mibBuilder.loadTexts:fsWebAuthDirectSiteNetMask.setStatus(_B)
_FsWebAuthDirectSiteStatus_Type=RowStatus
_FsWebAuthDirectSiteStatus_Object=MibTableColumn
fsWebAuthDirectSiteStatus=_FsWebAuthDirectSiteStatus_Object((1,3,6,1,4,1,52642,1,1,10,2,40,1,7,1,3),_FsWebAuthDirectSiteStatus_Type())
fsWebAuthDirectSiteStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:fsWebAuthDirectSiteStatus.setStatus(_B)
class _FsWebAuthDirectSiteBindArpFlag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('no',0),(_P,1)))
_FsWebAuthDirectSiteBindArpFlag_Type.__name__=_F
_FsWebAuthDirectSiteBindArpFlag_Object=MibTableColumn
fsWebAuthDirectSiteBindArpFlag=_FsWebAuthDirectSiteBindArpFlag_Object((1,3,6,1,4,1,52642,1,1,10,2,40,1,7,1,4),_FsWebAuthDirectSiteBindArpFlag_Type())
fsWebAuthDirectSiteBindArpFlag.setMaxAccess(_C)
if mibBuilder.loadTexts:fsWebAuthDirectSiteBindArpFlag.setStatus(_B)
_FsWebAuthDirectHostTable_Object=MibTable
fsWebAuthDirectHostTable=_FsWebAuthDirectHostTable_Object((1,3,6,1,4,1,52642,1,1,10,2,40,1,8))
if mibBuilder.loadTexts:fsWebAuthDirectHostTable.setStatus(_B)
_FsWebAuthDirectHostEntry_Object=MibTableRow
fsWebAuthDirectHostEntry=_FsWebAuthDirectHostEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,40,1,8,1))
fsWebAuthDirectHostEntry.setIndexNames((0,_A,_S),(0,_A,_T))
if mibBuilder.loadTexts:fsWebAuthDirectHostEntry.setStatus(_B)
_FsWebAuthDirectHostAddress_Type=IpAddress
_FsWebAuthDirectHostAddress_Object=MibTableColumn
fsWebAuthDirectHostAddress=_FsWebAuthDirectHostAddress_Object((1,3,6,1,4,1,52642,1,1,10,2,40,1,8,1,1),_FsWebAuthDirectHostAddress_Type())
fsWebAuthDirectHostAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:fsWebAuthDirectHostAddress.setStatus(_B)
_FsWebAuthDirectHostNetMask_Type=IpAddress
_FsWebAuthDirectHostNetMask_Object=MibTableColumn
fsWebAuthDirectHostNetMask=_FsWebAuthDirectHostNetMask_Object((1,3,6,1,4,1,52642,1,1,10,2,40,1,8,1,2),_FsWebAuthDirectHostNetMask_Type())
fsWebAuthDirectHostNetMask.setMaxAccess(_D)
if mibBuilder.loadTexts:fsWebAuthDirectHostNetMask.setStatus(_B)
_FsWebAuthDirectHostPort1_Type=Unsigned32
_FsWebAuthDirectHostPort1_Object=MibTableColumn
fsWebAuthDirectHostPort1=_FsWebAuthDirectHostPort1_Object((1,3,6,1,4,1,52642,1,1,10,2,40,1,8,1,3),_FsWebAuthDirectHostPort1_Type())
fsWebAuthDirectHostPort1.setMaxAccess(_C)
if mibBuilder.loadTexts:fsWebAuthDirectHostPort1.setStatus(_B)
_FsWebAuthDirectHostPort2_Type=Unsigned32
_FsWebAuthDirectHostPort2_Object=MibTableColumn
fsWebAuthDirectHostPort2=_FsWebAuthDirectHostPort2_Object((1,3,6,1,4,1,52642,1,1,10,2,40,1,8,1,4),_FsWebAuthDirectHostPort2_Type())
fsWebAuthDirectHostPort2.setMaxAccess(_C)
if mibBuilder.loadTexts:fsWebAuthDirectHostPort2.setStatus(_B)
_FsWebAuthDirectHostPort3_Type=Unsigned32
_FsWebAuthDirectHostPort3_Object=MibTableColumn
fsWebAuthDirectHostPort3=_FsWebAuthDirectHostPort3_Object((1,3,6,1,4,1,52642,1,1,10,2,40,1,8,1,5),_FsWebAuthDirectHostPort3_Type())
fsWebAuthDirectHostPort3.setMaxAccess(_C)
if mibBuilder.loadTexts:fsWebAuthDirectHostPort3.setStatus(_B)
_FsWebAuthDirectHostPort4_Type=Unsigned32
_FsWebAuthDirectHostPort4_Object=MibTableColumn
fsWebAuthDirectHostPort4=_FsWebAuthDirectHostPort4_Object((1,3,6,1,4,1,52642,1,1,10,2,40,1,8,1,6),_FsWebAuthDirectHostPort4_Type())
fsWebAuthDirectHostPort4.setMaxAccess(_C)
if mibBuilder.loadTexts:fsWebAuthDirectHostPort4.setStatus(_B)
_FsWebAuthDirectHostPort5_Type=Unsigned32
_FsWebAuthDirectHostPort5_Object=MibTableColumn
fsWebAuthDirectHostPort5=_FsWebAuthDirectHostPort5_Object((1,3,6,1,4,1,52642,1,1,10,2,40,1,8,1,7),_FsWebAuthDirectHostPort5_Type())
fsWebAuthDirectHostPort5.setMaxAccess(_C)
if mibBuilder.loadTexts:fsWebAuthDirectHostPort5.setStatus(_B)
_FsWebAuthDirectHostPort6_Type=Unsigned32
_FsWebAuthDirectHostPort6_Object=MibTableColumn
fsWebAuthDirectHostPort6=_FsWebAuthDirectHostPort6_Object((1,3,6,1,4,1,52642,1,1,10,2,40,1,8,1,8),_FsWebAuthDirectHostPort6_Type())
fsWebAuthDirectHostPort6.setMaxAccess(_C)
if mibBuilder.loadTexts:fsWebAuthDirectHostPort6.setStatus(_B)
_FsWebAuthDirectHostPort7_Type=Unsigned32
_FsWebAuthDirectHostPort7_Object=MibTableColumn
fsWebAuthDirectHostPort7=_FsWebAuthDirectHostPort7_Object((1,3,6,1,4,1,52642,1,1,10,2,40,1,8,1,9),_FsWebAuthDirectHostPort7_Type())
fsWebAuthDirectHostPort7.setMaxAccess(_C)
if mibBuilder.loadTexts:fsWebAuthDirectHostPort7.setStatus(_B)
_FsWebAuthDirectHostPort8_Type=Unsigned32
_FsWebAuthDirectHostPort8_Object=MibTableColumn
fsWebAuthDirectHostPort8=_FsWebAuthDirectHostPort8_Object((1,3,6,1,4,1,52642,1,1,10,2,40,1,8,1,10),_FsWebAuthDirectHostPort8_Type())
fsWebAuthDirectHostPort8.setMaxAccess(_C)
if mibBuilder.loadTexts:fsWebAuthDirectHostPort8.setStatus(_B)
class _FsWebAuthDirectHostBindArpFlag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('no',0),(_P,1)))
_FsWebAuthDirectHostBindArpFlag_Type.__name__=_F
_FsWebAuthDirectHostBindArpFlag_Object=MibTableColumn
fsWebAuthDirectHostBindArpFlag=_FsWebAuthDirectHostBindArpFlag_Object((1,3,6,1,4,1,52642,1,1,10,2,40,1,8,1,11),_FsWebAuthDirectHostBindArpFlag_Type())
fsWebAuthDirectHostBindArpFlag.setMaxAccess(_C)
if mibBuilder.loadTexts:fsWebAuthDirectHostBindArpFlag.setStatus(_B)
_FsWebAuthDirectHostStatus_Type=RowStatus
_FsWebAuthDirectHostStatus_Object=MibTableColumn
fsWebAuthDirectHostStatus=_FsWebAuthDirectHostStatus_Object((1,3,6,1,4,1,52642,1,1,10,2,40,1,8,1,12),_FsWebAuthDirectHostStatus_Type())
fsWebAuthDirectHostStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:fsWebAuthDirectHostStatus.setStatus(_B)
_FsWebAuthDirectHostPortIfx_Type=Gauge32
_FsWebAuthDirectHostPortIfx_Object=MibTableColumn
fsWebAuthDirectHostPortIfx=_FsWebAuthDirectHostPortIfx_Object((1,3,6,1,4,1,52642,1,1,10,2,40,1,8,1,13),_FsWebAuthDirectHostPortIfx_Type())
fsWebAuthDirectHostPortIfx.setMaxAccess(_C)
if mibBuilder.loadTexts:fsWebAuthDirectHostPortIfx.setStatus(_B)
_FsWebAuthFreeAcctIpTable_Object=MibTable
fsWebAuthFreeAcctIpTable=_FsWebAuthFreeAcctIpTable_Object((1,3,6,1,4,1,52642,1,1,10,2,40,1,9))
if mibBuilder.loadTexts:fsWebAuthFreeAcctIpTable.setStatus(_B)
_FsWebAuthFreeAcctIpEntry_Object=MibTableRow
fsWebAuthFreeAcctIpEntry=_FsWebAuthFreeAcctIpEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,40,1,9,1))
fsWebAuthFreeAcctIpEntry.setIndexNames((0,_A,_U),(0,_A,_V))
if mibBuilder.loadTexts:fsWebAuthFreeAcctIpEntry.setStatus(_B)
_FsWebAuthFreeAcctIpAddress_Type=IpAddress
_FsWebAuthFreeAcctIpAddress_Object=MibTableColumn
fsWebAuthFreeAcctIpAddress=_FsWebAuthFreeAcctIpAddress_Object((1,3,6,1,4,1,52642,1,1,10,2,40,1,9,1,1),_FsWebAuthFreeAcctIpAddress_Type())
fsWebAuthFreeAcctIpAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:fsWebAuthFreeAcctIpAddress.setStatus(_B)
_FsWebAuthFreeAcctIpNetMask_Type=IpAddress
_FsWebAuthFreeAcctIpNetMask_Object=MibTableColumn
fsWebAuthFreeAcctIpNetMask=_FsWebAuthFreeAcctIpNetMask_Object((1,3,6,1,4,1,52642,1,1,10,2,40,1,9,1,2),_FsWebAuthFreeAcctIpNetMask_Type())
fsWebAuthFreeAcctIpNetMask.setMaxAccess(_D)
if mibBuilder.loadTexts:fsWebAuthFreeAcctIpNetMask.setStatus(_B)
_FsWebAuthFreeAcctIpStatus_Type=RowStatus
_FsWebAuthFreeAcctIpStatus_Object=MibTableColumn
fsWebAuthFreeAcctIpStatus=_FsWebAuthFreeAcctIpStatus_Object((1,3,6,1,4,1,52642,1,1,10,2,40,1,9,1,3),_FsWebAuthFreeAcctIpStatus_Type())
fsWebAuthFreeAcctIpStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:fsWebAuthFreeAcctIpStatus.setStatus(_B)
_FsWebAuthFreeAcctUrlTable_Object=MibTable
fsWebAuthFreeAcctUrlTable=_FsWebAuthFreeAcctUrlTable_Object((1,3,6,1,4,1,52642,1,1,10,2,40,1,10))
if mibBuilder.loadTexts:fsWebAuthFreeAcctUrlTable.setStatus(_B)
_FsWebAuthFreeAcctUrlEntry_Object=MibTableRow
fsWebAuthFreeAcctUrlEntry=_FsWebAuthFreeAcctUrlEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,40,1,10,1))
fsWebAuthFreeAcctUrlEntry.setIndexNames((0,_A,_W))
if mibBuilder.loadTexts:fsWebAuthFreeAcctUrlEntry.setStatus(_B)
_FsWebAuthFreeAcctUrl_Type=OctetString
_FsWebAuthFreeAcctUrl_Object=MibTableColumn
fsWebAuthFreeAcctUrl=_FsWebAuthFreeAcctUrl_Object((1,3,6,1,4,1,52642,1,1,10,2,40,1,10,1,1),_FsWebAuthFreeAcctUrl_Type())
fsWebAuthFreeAcctUrl.setMaxAccess(_D)
if mibBuilder.loadTexts:fsWebAuthFreeAcctUrl.setStatus(_B)
_FsWebAuthFreeAcctUrlStatus_Type=RowStatus
_FsWebAuthFreeAcctUrlStatus_Object=MibTableColumn
fsWebAuthFreeAcctUrlStatus=_FsWebAuthFreeAcctUrlStatus_Object((1,3,6,1,4,1,52642,1,1,10,2,40,1,10,1,2),_FsWebAuthFreeAcctUrlStatus_Type())
fsWebAuthFreeAcctUrlStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:fsWebAuthFreeAcctUrlStatus.setStatus(_B)
_FsWebAuthOfflineDetectTable_Object=MibTable
fsWebAuthOfflineDetectTable=_FsWebAuthOfflineDetectTable_Object((1,3,6,1,4,1,52642,1,1,10,2,40,1,11))
if mibBuilder.loadTexts:fsWebAuthOfflineDetectTable.setStatus(_B)
_FsWebAuthOfflineDetectEntry_Object=MibTableRow
fsWebAuthOfflineDetectEntry=_FsWebAuthOfflineDetectEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,40,1,11,1))
fsWebAuthOfflineDetectEntry.setIndexNames((0,_A,_X))
if mibBuilder.loadTexts:fsWebAuthOfflineDetectEntry.setStatus(_B)
_FsWebAuthOfflineDetectime_Type=Unsigned32
_FsWebAuthOfflineDetectime_Object=MibTableColumn
fsWebAuthOfflineDetectime=_FsWebAuthOfflineDetectime_Object((1,3,6,1,4,1,52642,1,1,10,2,40,1,11,1,1),_FsWebAuthOfflineDetectime_Type())
fsWebAuthOfflineDetectime.setMaxAccess(_D)
if mibBuilder.loadTexts:fsWebAuthOfflineDetectime.setStatus(_B)
_FsWebAuthOfflineDetectStatus_Type=RowStatus
_FsWebAuthOfflineDetectStatus_Object=MibTableColumn
fsWebAuthOfflineDetectStatus=_FsWebAuthOfflineDetectStatus_Object((1,3,6,1,4,1,52642,1,1,10,2,40,1,11,1,2),_FsWebAuthOfflineDetectStatus_Type())
fsWebAuthOfflineDetectStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:fsWebAuthOfflineDetectStatus.setStatus(_B)
_FsWebAuthCurrentOnlineUser_Type=Integer32
_FsWebAuthCurrentOnlineUser_Object=MibScalar
fsWebAuthCurrentOnlineUser=_FsWebAuthCurrentOnlineUser_Object((1,3,6,1,4,1,52642,1,1,10,2,40,1,12),_FsWebAuthCurrentOnlineUser_Type())
fsWebAuthCurrentOnlineUser.setMaxAccess(_D)
if mibBuilder.loadTexts:fsWebAuthCurrentOnlineUser.setStatus(_B)
_FsWebAuthCurrentUser_Type=Integer32
_FsWebAuthCurrentUser_Object=MibScalar
fsWebAuthCurrentUser=_FsWebAuthCurrentUser_Object((1,3,6,1,4,1,52642,1,1,10,2,40,1,13),_FsWebAuthCurrentUser_Type())
fsWebAuthCurrentUser.setMaxAccess(_D)
if mibBuilder.loadTexts:fsWebAuthCurrentUser.setStatus(_B)
_FsWebAuthMaximumOnlineUser_Type=Integer32
_FsWebAuthMaximumOnlineUser_Object=MibScalar
fsWebAuthMaximumOnlineUser=_FsWebAuthMaximumOnlineUser_Object((1,3,6,1,4,1,52642,1,1,10,2,40,1,14),_FsWebAuthMaximumOnlineUser_Type())
fsWebAuthMaximumOnlineUser.setMaxAccess(_D)
if mibBuilder.loadTexts:fsWebAuthMaximumOnlineUser.setStatus(_B)
_FsWebAuthMIBTraps_ObjectIdentity=ObjectIdentity
fsWebAuthMIBTraps=_FsWebAuthMIBTraps_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,40,2))
_FsWebAuthMIBConformance_ObjectIdentity=ObjectIdentity
fsWebAuthMIBConformance=_FsWebAuthMIBConformance_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,40,3))
_FsWebAuthMIBCompliances_ObjectIdentity=ObjectIdentity
fsWebAuthMIBCompliances=_FsWebAuthMIBCompliances_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,40,3,1))
_FsWebAuthMIBGroups_ObjectIdentity=ObjectIdentity
fsWebAuthMIBGroups=_FsWebAuthMIBGroups_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,40,3,2))
_FsWebAuthMIBTrapsObjects_ObjectIdentity=ObjectIdentity
fsWebAuthMIBTrapsObjects=_FsWebAuthMIBTrapsObjects_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,40,4))
_FsWebAuthApMac_Type=MacAddress
_FsWebAuthApMac_Object=MibScalar
fsWebAuthApMac=_FsWebAuthApMac_Object((1,3,6,1,4,1,52642,1,1,10,2,40,4,1),_FsWebAuthApMac_Type())
fsWebAuthApMac.setMaxAccess(_E)
if mibBuilder.loadTexts:fsWebAuthApMac.setStatus(_B)
_FsWebAuthApIp_Type=IpAddress
_FsWebAuthApIp_Object=MibScalar
fsWebAuthApIp=_FsWebAuthApIp_Object((1,3,6,1,4,1,52642,1,1,10,2,40,4,2),_FsWebAuthApIp_Type())
fsWebAuthApIp.setMaxAccess(_E)
if mibBuilder.loadTexts:fsWebAuthApIp.setStatus(_B)
_FsWebAuthStaMac_Type=MacAddress
_FsWebAuthStaMac_Object=MibScalar
fsWebAuthStaMac=_FsWebAuthStaMac_Object((1,3,6,1,4,1,52642,1,1,10,2,40,4,3),_FsWebAuthStaMac_Type())
fsWebAuthStaMac.setMaxAccess(_E)
if mibBuilder.loadTexts:fsWebAuthStaMac.setStatus(_B)
_FsWebAuthStaIp_Type=IpAddress
_FsWebAuthStaIp_Object=MibScalar
fsWebAuthStaIp=_FsWebAuthStaIp_Object((1,3,6,1,4,1,52642,1,1,10,2,40,4,4),_FsWebAuthStaIp_Type())
fsWebAuthStaIp.setMaxAccess(_E)
if mibBuilder.loadTexts:fsWebAuthStaIp.setStatus(_B)
_FsWebAuthStaIpv6_Type=InetAddress
_FsWebAuthStaIpv6_Object=MibScalar
fsWebAuthStaIpv6=_FsWebAuthStaIpv6_Object((1,3,6,1,4,1,52642,1,1,10,2,40,4,5),_FsWebAuthStaIpv6_Type())
fsWebAuthStaIpv6.setMaxAccess(_E)
if mibBuilder.loadTexts:fsWebAuthStaIpv6.setStatus(_B)
class _FsWebAuthStaOperType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,3))
_FsWebAuthStaOperType_Type.__name__=_F
_FsWebAuthStaOperType_Object=MibScalar
fsWebAuthStaOperType=_FsWebAuthStaOperType_Object((1,3,6,1,4,1,52642,1,1,10,2,40,4,6),_FsWebAuthStaOperType_Type())
fsWebAuthStaOperType.setMaxAccess(_E)
if mibBuilder.loadTexts:fsWebAuthStaOperType.setStatus(_B)
class _FsWebAuthStaApRadioId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_FsWebAuthStaApRadioId_Type.__name__=_F
_FsWebAuthStaApRadioId_Object=MibScalar
fsWebAuthStaApRadioId=_FsWebAuthStaApRadioId_Object((1,3,6,1,4,1,52642,1,1,10,2,40,4,7),_FsWebAuthStaApRadioId_Type())
fsWebAuthStaApRadioId.setMaxAccess(_E)
if mibBuilder.loadTexts:fsWebAuthStaApRadioId.setStatus(_B)
class _FsWebAuthStaApRadioType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_FsWebAuthStaApRadioType_Type.__name__=_F
_FsWebAuthStaApRadioType_Object=MibScalar
fsWebAuthStaApRadioType=_FsWebAuthStaApRadioType_Object((1,3,6,1,4,1,52642,1,1,10,2,40,4,8),_FsWebAuthStaApRadioType_Type())
fsWebAuthStaApRadioType.setMaxAccess(_E)
if mibBuilder.loadTexts:fsWebAuthStaApRadioType.setStatus(_B)
class _FsWebAuthStaVlanId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_FsWebAuthStaVlanId_Type.__name__=_F
_FsWebAuthStaVlanId_Object=MibScalar
fsWebAuthStaVlanId=_FsWebAuthStaVlanId_Object((1,3,6,1,4,1,52642,1,1,10,2,40,4,9),_FsWebAuthStaVlanId_Type())
fsWebAuthStaVlanId.setMaxAccess(_E)
if mibBuilder.loadTexts:fsWebAuthStaVlanId.setStatus(_B)
class _FsWebAuthStaWlanId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_FsWebAuthStaWlanId_Type.__name__=_F
_FsWebAuthStaWlanId_Object=MibScalar
fsWebAuthStaWlanId=_FsWebAuthStaWlanId_Object((1,3,6,1,4,1,52642,1,1,10,2,40,4,10),_FsWebAuthStaWlanId_Type())
fsWebAuthStaWlanId.setMaxAccess(_E)
if mibBuilder.loadTexts:fsWebAuthStaWlanId.setStatus(_B)
_FsWebAuthOperTime_Type=TimeTicks
_FsWebAuthOperTime_Object=MibScalar
fsWebAuthOperTime=_FsWebAuthOperTime_Object((1,3,6,1,4,1,52642,1,1,10,2,40,4,11),_FsWebAuthOperTime_Type())
fsWebAuthOperTime.setMaxAccess(_E)
if mibBuilder.loadTexts:fsWebAuthOperTime.setStatus(_B)
class _FsWebAuthStaAssoAuthMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('open',0),('wep',1),('dot1x-wep',2),('dot1x-wpa',3),('dot1x-wpa2',4),('mab',5),('psk-wpa',6),('psk-wpa2',7),('wapi',8)))
_FsWebAuthStaAssoAuthMode_Type.__name__=_F
_FsWebAuthStaAssoAuthMode_Object=MibScalar
fsWebAuthStaAssoAuthMode=_FsWebAuthStaAssoAuthMode_Object((1,3,6,1,4,1,52642,1,1,10,2,40,4,12),_FsWebAuthStaAssoAuthMode_Type())
fsWebAuthStaAssoAuthMode.setMaxAccess(_E)
if mibBuilder.loadTexts:fsWebAuthStaAssoAuthMode.setStatus(_B)
class _FsWebAuthStaNetAuthMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('open',0),('web',1)))
_FsWebAuthStaNetAuthMode_Type.__name__=_F
_FsWebAuthStaNetAuthMode_Object=MibScalar
fsWebAuthStaNetAuthMode=_FsWebAuthStaNetAuthMode_Object((1,3,6,1,4,1,52642,1,1,10,2,40,4,13),_FsWebAuthStaNetAuthMode_Type())
fsWebAuthStaNetAuthMode.setMaxAccess(_E)
if mibBuilder.loadTexts:fsWebAuthStaNetAuthMode.setStatus(_B)
_FsWebAuthStaRssi_Type=Integer32
_FsWebAuthStaRssi_Object=MibScalar
fsWebAuthStaRssi=_FsWebAuthStaRssi_Object((1,3,6,1,4,1,52642,1,1,10,2,40,4,14),_FsWebAuthStaRssi_Type())
fsWebAuthStaRssi.setMaxAccess(_E)
if mibBuilder.loadTexts:fsWebAuthStaRssi.setStatus(_B)
_FsWebAuthStaSsid_Type=DisplayString
_FsWebAuthStaSsid_Object=MibScalar
fsWebAuthStaSsid=_FsWebAuthStaSsid_Object((1,3,6,1,4,1,52642,1,1,10,2,40,4,15),_FsWebAuthStaSsid_Type())
fsWebAuthStaSsid.setMaxAccess(_E)
if mibBuilder.loadTexts:fsWebAuthStaSsid.setStatus(_B)
_FsWebAuthStaLinkRate_Type=Integer32
_FsWebAuthStaLinkRate_Object=MibScalar
fsWebAuthStaLinkRate=_FsWebAuthStaLinkRate_Object((1,3,6,1,4,1,52642,1,1,10,2,40,4,16),_FsWebAuthStaLinkRate_Type())
fsWebAuthStaLinkRate.setMaxAccess(_E)
if mibBuilder.loadTexts:fsWebAuthStaLinkRate.setStatus(_B)
_FsWebAuthStaCurChannel_Type=Integer32
_FsWebAuthStaCurChannel_Object=MibScalar
fsWebAuthStaCurChannel=_FsWebAuthStaCurChannel_Object((1,3,6,1,4,1,52642,1,1,10,2,40,4,17),_FsWebAuthStaCurChannel_Type())
fsWebAuthStaCurChannel.setMaxAccess(_E)
if mibBuilder.loadTexts:fsWebAuthStaCurChannel.setStatus(_B)
class _FsWebAuthStaUsername_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_FsWebAuthStaUsername_Type.__name__=_H
_FsWebAuthStaUsername_Object=MibScalar
fsWebAuthStaUsername=_FsWebAuthStaUsername_Object((1,3,6,1,4,1,52642,1,1,10,2,40,4,18),_FsWebAuthStaUsername_Type())
fsWebAuthStaUsername.setMaxAccess(_E)
if mibBuilder.loadTexts:fsWebAuthStaUsername.setStatus(_B)
_FsWebAuthStaTerminalType_Type=DisplayString
_FsWebAuthStaTerminalType_Object=MibScalar
fsWebAuthStaTerminalType=_FsWebAuthStaTerminalType_Object((1,3,6,1,4,1,52642,1,1,10,2,40,4,19),_FsWebAuthStaTerminalType_Type())
fsWebAuthStaTerminalType.setMaxAccess(_E)
if mibBuilder.loadTexts:fsWebAuthStaTerminalType.setStatus(_B)
_FsWebAuthStaTerminateCause_Type=Integer32
_FsWebAuthStaTerminateCause_Object=MibScalar
fsWebAuthStaTerminateCause=_FsWebAuthStaTerminateCause_Object((1,3,6,1,4,1,52642,1,1,10,2,40,4,20),_FsWebAuthStaTerminateCause_Type())
fsWebAuthStaTerminateCause.setMaxAccess(_E)
if mibBuilder.loadTexts:fsWebAuthStaTerminateCause.setStatus(_B)
_FsWebAuthStaReplyMessage_Type=DisplayString
_FsWebAuthStaReplyMessage_Object=MibScalar
fsWebAuthStaReplyMessage=_FsWebAuthStaReplyMessage_Object((1,3,6,1,4,1,52642,1,1,10,2,40,4,21),_FsWebAuthStaReplyMessage_Type())
fsWebAuthStaReplyMessage.setMaxAccess(_E)
if mibBuilder.loadTexts:fsWebAuthStaReplyMessage.setStatus(_B)
_FsWebAuthStaTerminalId_Type=DisplayString
_FsWebAuthStaTerminalId_Object=MibScalar
fsWebAuthStaTerminalId=_FsWebAuthStaTerminalId_Object((1,3,6,1,4,1,52642,1,1,10,2,40,4,22),_FsWebAuthStaTerminalId_Type())
fsWebAuthStaTerminalId.setMaxAccess(_E)
if mibBuilder.loadTexts:fsWebAuthStaTerminalId.setStatus(_B)
class _FsWebAuthType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_FsWebAuthType_Type.__name__=_F
_FsWebAuthType_Object=MibScalar
fsWebAuthType=_FsWebAuthType_Object((1,3,6,1,4,1,52642,1,1,10,2,40,4,23),_FsWebAuthType_Type())
fsWebAuthType.setMaxAccess(_E)
if mibBuilder.loadTexts:fsWebAuthType.setStatus(_B)
_FsWebAuthPortIndex_Type=Integer32
_FsWebAuthPortIndex_Object=MibScalar
fsWebAuthPortIndex=_FsWebAuthPortIndex_Object((1,3,6,1,4,1,52642,1,1,10,2,40,4,24),_FsWebAuthPortIndex_Type())
fsWebAuthPortIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:fsWebAuthPortIndex.setStatus(_B)
_FsWebAuthTlvNum_Type=Integer32
_FsWebAuthTlvNum_Object=MibScalar
fsWebAuthTlvNum=_FsWebAuthTlvNum_Object((1,3,6,1,4,1,52642,1,1,10,2,40,4,25),_FsWebAuthTlvNum_Type())
fsWebAuthTlvNum.setMaxAccess(_E)
if mibBuilder.loadTexts:fsWebAuthTlvNum.setStatus(_B)
_FsWebAuthTlv_Type=DisplayString
_FsWebAuthTlv_Object=MibScalar
fsWebAuthTlv=_FsWebAuthTlv_Object((1,3,6,1,4,1,52642,1,1,10,2,40,4,26),_FsWebAuthTlv_Type())
fsWebAuthTlv.setMaxAccess(_E)
if mibBuilder.loadTexts:fsWebAuthTlv.setStatus(_B)
fsWebAuthMIBGroup=ObjectGroup((1,3,6,1,4,1,52642,1,1,10,2,40,3,2,1))
fsWebAuthMIBGroup.setObjects(*((_A,_I),(_A,_q),(_A,_r),(_A,_Y),(_A,_s),(_A,_t),(_A,_u),(_A,_v),(_A,_w),(_A,_x),(_A,_Z),(_A,_J),(_A,_K),(_A,_a),(_A,_b),(_A,_c),(_A,_y),(_A,_z),(_A,_d),(_A,_e),(_A,_A0),(_A,_N),(_A,_O),(_A,_A1),(_A,_A2),(_A,_A3),(_A,_A4),(_A,_A5),(_A,_A6),(_A,_A7),(_A,_A8),(_A,_A9),(_A,_AA),(_A,_L),(_A,_M),(_A,_AB),(_A,_AC),(_A,_f),(_A,_AD),(_A,_AE),(_A,_AF),(_A,_AG),(_A,_AH),(_A,_AI),(_A,_g),(_A,_AJ),(_A,_Q),(_A,_R),(_A,_AK),(_A,_AL),(_A,_S),(_A,_T),(_A,_AM),(_A,_AN),(_A,_AO),(_A,_AP),(_A,_AQ),(_A,_AR),(_A,_AS),(_A,_AT),(_A,_AU),(_A,_AV),(_A,_AW),(_A,_U),(_A,_V),(_A,_AX),(_A,_W),(_A,_AY),(_A,_X),(_A,_AZ),(_A,_Aa),(_A,_Ab),(_A,_Ac)))
if mibBuilder.loadTexts:fsWebAuthMIBGroup.setStatus(_B)
fsWebAuthUserLeave=NotificationType((1,3,6,1,4,1,52642,1,1,10,2,40,2,1))
fsWebAuthUserLeave.setObjects(*((_A,_I),(_A,_Y),(_A,_Z)))
if mibBuilder.loadTexts:fsWebAuthUserLeave.setStatus(_B)
fsWebAuthUserExtLeave=NotificationType((1,3,6,1,4,1,52642,1,1,10,2,40,2,2))
fsWebAuthUserExtLeave.setObjects(*((_A,_J),(_A,_K),(_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_e)))
if mibBuilder.loadTexts:fsWebAuthUserExtLeave.setStatus(_B)
fsWebAuthSDGUserLeave=NotificationType((1,3,6,1,4,1,52642,1,1,10,2,40,2,3))
fsWebAuthSDGUserLeave.setObjects(*((_A,_L),(_A,_M),(_A,_f),(_A,_g)))
if mibBuilder.loadTexts:fsWebAuthSDGUserLeave.setStatus(_B)
fsWebAuthWlanMgmt=NotificationType((1,3,6,1,4,1,52642,1,1,10,2,40,2,4))
fsWebAuthWlanMgmt.setObjects(*((_A,_Ad),(_A,_Ae),(_A,_h),(_A,_i),(_A,_Af),(_A,_j),(_A,_Ag),(_A,_Ah),(_A,_k),(_A,_Ai),(_A,_Aj),(_A,_Ak),(_A,_Al),(_A,_Am),(_A,_An),(_A,_Ao),(_A,_Ap),(_A,_l),(_A,_Aq),(_A,_m),(_A,_Ar),(_A,_As)))
if mibBuilder.loadTexts:fsWebAuthWlanMgmt.setStatus(_B)
fsWebAuthUserOper=NotificationType((1,3,6,1,4,1,52642,1,1,10,2,40,2,5))
fsWebAuthUserOper.setObjects(*((_A,_j),(_A,_At),(_A,_l),(_A,_i),(_A,_h),(_A,_k),(_A,_Au),(_A,_m)))
if mibBuilder.loadTexts:fsWebAuthUserOper.setStatus(_B)
fsWebAuthRedirectInfo=NotificationType((1,3,6,1,4,1,52642,1,1,10,2,40,2,6))
fsWebAuthRedirectInfo.setObjects(*((_A,_Av),(_A,_Aw)))
if mibBuilder.loadTexts:fsWebAuthRedirectInfo.setStatus(_B)
fsWebAuthTrapGroup=NotificationGroup((1,3,6,1,4,1,52642,1,1,10,2,40,3,2,2))
fsWebAuthTrapGroup.setObjects(*((_A,_Ax),(_A,_Ay),(_A,_Az)))
if mibBuilder.loadTexts:fsWebAuthTrapGroup.setStatus(_B)
fsWebAuthMIBCompliance=ModuleCompliance((1,3,6,1,4,1,52642,1,1,10,2,40,3,1,1))
fsWebAuthMIBCompliance.setObjects(*((_A,_A_),(_A,_B0)))
if mibBuilder.loadTexts:fsWebAuthMIBCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'fsWebAuthMIB':fsWebAuthMIB,'fsWebAuthMIBObjects':fsWebAuthMIBObjects,'fsWebAuthUserTable':fsWebAuthUserTable,'fsWebAuthUserEntry':fsWebAuthUserEntry,_I:authUserIpAddr,_q:authUserOnlineFlag,_r:authUserTimeLimit,_Y:authUserTimeUsed,_s:authUserStatus,_t:authUserRoleName,_u:authUserSecZoneName,_v:authUserSecZonePermissionType,_w:authUserSecZonePermissionList,_x:authUserOtherPermissionType,_Z:authUserTerminateCause,'fsWebAuthUserExtTable':fsWebAuthUserExtTable,'fsWebAuthUserExtEntry':fsWebAuthUserExtEntry,_J:authUserExtAddrType,_K:authUserExtAddr,_a:authUserExtMac,_b:authUserExtIfIndex,_c:authUserExtVlanId,_y:authUserExtOnlineFlag,_z:authUserExtTimeLimit,_d:authUserExtTimeUsed,_e:authUserExtErrCause,_A0:authUserExtStatus,'fsWebAuthWhiteListTable':fsWebAuthWhiteListTable,'fsWebAuthWhiteListEntry':fsWebAuthWhiteListEntry,_N:fsWebAuthWhiteListAddress,_O:fsWebAuthWhiteListNetMask,_A1:fsWebAuthWhiteListPort1,_A2:fsWebAuthWhiteListPort2,_A3:fsWebAuthWhiteListPort3,_A4:fsWebAuthWhiteListPort4,_A5:fsWebAuthWhiteListPort5,_A6:fsWebAuthWhiteListPort6,_A7:fsWebAuthWhiteListPort7,_A8:fsWebAuthWhiteListPort8,_A9:fsWebAuthWhiteListBindArpFlag,_AA:fsWebAuthWhiteListStatus,'fsWebAuthSDGUserTable':fsWebAuthSDGUserTable,'fsWebAuthSDGUserEntry':fsWebAuthSDGUserEntry,_L:authSDGUserVrfg,_M:authSDGUserIpAddr,_AB:authSDGUserOnlineFlag,_AC:authSDGUserTimeLimit,_f:authSDGUserTimeUsed,_AD:authSDGUserVrf,_AE:authSDGUserRoleName,_AF:authSDGUserSecZoneName,_AG:authSDGUserSecZonePermissionType,_AH:authSDGUserSecZonePermissionList,_AI:authSDGUserOtherPermissionType,_g:authSDGUserTerminateCause,_AJ:authSDGUserStatus,'fsWebAuthMacUserTable':fsWebAuthMacUserTable,'fsWebAuthMacUserEntry':fsWebAuthMacUserEntry,_o:fsAuthMacUserMacAddr,'fsAuthMacUserName':fsAuthMacUserName,'fsAuthMacUserTerminalId':fsAuthMacUserTerminalId,'fsWebAuthUserMIB':fsWebAuthUserMIB,'fsWebAuthUserMIBTable':fsWebAuthUserMIBTable,'fsWebAuthUserMIBEntry':fsWebAuthUserMIBEntry,_p:fsAuthUserMIBIpAddress,'fsAuthUserMIBName':fsAuthUserMIBName,'fsAuthUserMIBAuthType':fsAuthUserMIBAuthType,'fsAuthUserMIBMacAddress':fsAuthUserMIBMacAddress,'fsAuthUserMIBVlanId':fsAuthUserMIBVlanId,'fsAuthUserMIBPortIndex':fsAuthUserMIBPortIndex,'fsAuthUserMIBTimeUsed':fsAuthUserMIBTimeUsed,'fsWebAuthDirectSiteTable':fsWebAuthDirectSiteTable,'fsWebAuthDirectSiteEntry':fsWebAuthDirectSiteEntry,_Q:fsWebAuthDirectSiteAddress,_R:fsWebAuthDirectSiteNetMask,_AK:fsWebAuthDirectSiteStatus,_AL:fsWebAuthDirectSiteBindArpFlag,'fsWebAuthDirectHostTable':fsWebAuthDirectHostTable,'fsWebAuthDirectHostEntry':fsWebAuthDirectHostEntry,_S:fsWebAuthDirectHostAddress,_T:fsWebAuthDirectHostNetMask,_AM:fsWebAuthDirectHostPort1,_AN:fsWebAuthDirectHostPort2,_AO:fsWebAuthDirectHostPort3,_AP:fsWebAuthDirectHostPort4,_AQ:fsWebAuthDirectHostPort5,_AR:fsWebAuthDirectHostPort6,_AS:fsWebAuthDirectHostPort7,_AT:fsWebAuthDirectHostPort8,_AU:fsWebAuthDirectHostBindArpFlag,_AV:fsWebAuthDirectHostStatus,_AW:fsWebAuthDirectHostPortIfx,'fsWebAuthFreeAcctIpTable':fsWebAuthFreeAcctIpTable,'fsWebAuthFreeAcctIpEntry':fsWebAuthFreeAcctIpEntry,_U:fsWebAuthFreeAcctIpAddress,_V:fsWebAuthFreeAcctIpNetMask,_AX:fsWebAuthFreeAcctIpStatus,'fsWebAuthFreeAcctUrlTable':fsWebAuthFreeAcctUrlTable,'fsWebAuthFreeAcctUrlEntry':fsWebAuthFreeAcctUrlEntry,_W:fsWebAuthFreeAcctUrl,_AY:fsWebAuthFreeAcctUrlStatus,'fsWebAuthOfflineDetectTable':fsWebAuthOfflineDetectTable,'fsWebAuthOfflineDetectEntry':fsWebAuthOfflineDetectEntry,_X:fsWebAuthOfflineDetectime,_AZ:fsWebAuthOfflineDetectStatus,_Aa:fsWebAuthCurrentOnlineUser,_Ab:fsWebAuthCurrentUser,_Ac:fsWebAuthMaximumOnlineUser,'fsWebAuthMIBTraps':fsWebAuthMIBTraps,_Ax:fsWebAuthUserLeave,_Ay:fsWebAuthUserExtLeave,_Az:fsWebAuthSDGUserLeave,'fsWebAuthWlanMgmt':fsWebAuthWlanMgmt,'fsWebAuthUserOper':fsWebAuthUserOper,'fsWebAuthRedirectInfo':fsWebAuthRedirectInfo,'fsWebAuthMIBConformance':fsWebAuthMIBConformance,'fsWebAuthMIBCompliances':fsWebAuthMIBCompliances,'fsWebAuthMIBCompliance':fsWebAuthMIBCompliance,'fsWebAuthMIBGroups':fsWebAuthMIBGroups,_A_:fsWebAuthMIBGroup,_B0:fsWebAuthTrapGroup,'fsWebAuthMIBTrapsObjects':fsWebAuthMIBTrapsObjects,_Ad:fsWebAuthApMac,_Ae:fsWebAuthApIp,_h:fsWebAuthStaMac,_i:fsWebAuthStaIp,_Af:fsWebAuthStaIpv6,_j:fsWebAuthStaOperType,_Ag:fsWebAuthStaApRadioId,_Ah:fsWebAuthStaApRadioType,_k:fsWebAuthStaVlanId,_Ai:fsWebAuthStaWlanId,_Aj:fsWebAuthOperTime,_Ak:fsWebAuthStaAssoAuthMode,_Al:fsWebAuthStaNetAuthMode,_Am:fsWebAuthStaRssi,_An:fsWebAuthStaSsid,_Ao:fsWebAuthStaLinkRate,_Ap:fsWebAuthStaCurChannel,_l:fsWebAuthStaUsername,_Aq:fsWebAuthStaTerminalType,_m:fsWebAuthStaTerminateCause,_Ar:fsWebAuthStaReplyMessage,_As:fsWebAuthStaTerminalId,_At:fsWebAuthType,_Au:fsWebAuthPortIndex,_Av:fsWebAuthTlvNum,_Aw:fsWebAuthTlv})