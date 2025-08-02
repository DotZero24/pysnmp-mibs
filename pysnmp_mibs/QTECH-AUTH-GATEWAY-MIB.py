_AX='qtechWebAuthTrapGroup'
_AW='qtechWebAuthMIBGroup'
_AV='qtechWebAuthSDGUserLeave'
_AU='qtechWebAuthUserExtLeave'
_AT='qtechWebAuthUserLeave'
_AS='qtechWebAuthPortIndex'
_AR='qtechWebAuthType'
_AQ='qtechWebAuthStaTerminalId'
_AP='qtechWebAuthStaReplyMessage'
_AO='qtechWebAuthStaTerminalType'
_AN='qtechWebAuthStaCurChannel'
_AM='qtechWebAuthStaLinkRate'
_AL='qtechWebAuthStaSsid'
_AK='qtechWebAuthStaRssi'
_AJ='qtechWebAuthStaNetAuthMode'
_AI='qtechWebAuthStaAssoAuthMode'
_AH='qtechWebAuthOperTime'
_AG='qtechWebAuthStaWlanId'
_AF='qtechWebAuthStaApRadioType'
_AE='qtechWebAuthStaApRadioId'
_AD='qtechWebAuthStaIpv6'
_AC='qtechWebAuthApIp'
_AB='qtechWebAuthApMac'
_AA='authSDGUserStatus'
_A9='authSDGUserOtherPermissionType'
_A8='authSDGUserSecZonePermissionList'
_A7='authSDGUserSecZonePermissionType'
_A6='authSDGUserSecZoneName'
_A5='authSDGUserRoleName'
_A4='authSDGUserVrf'
_A3='authSDGUserTimeLimit'
_A2='authSDGUserOnlineFlag'
_A1='qtechWebAuthWhiteListStatus'
_A0='qtechWebAuthWhiteListBindArpFlag'
_z='qtechWebAuthWhiteListPort8'
_y='qtechWebAuthWhiteListPort7'
_x='qtechWebAuthWhiteListPort6'
_w='qtechWebAuthWhiteListPort5'
_v='qtechWebAuthWhiteListPort4'
_u='qtechWebAuthWhiteListPort3'
_t='qtechWebAuthWhiteListPort2'
_s='qtechWebAuthWhiteListPort1'
_r='authUserExtStatus'
_q='authUserExtTimeLimit'
_p='authUserExtOnlineFlag'
_o='authUserOtherPermissionType'
_n='authUserSecZonePermissionList'
_m='authUserSecZonePermissionType'
_l='authUserSecZoneName'
_k='authUserRoleName'
_j='authUserStatus'
_i='authUserTimeLimit'
_h='authUserOnlineFlag'
_g='qtechAuthUserMIBIpAddress'
_f='qtechAuthMacUserMacAddr'
_e='InetAddress'
_d='qtechWebAuthStaTerminateCause'
_c='qtechWebAuthStaUsername'
_b='qtechWebAuthStaVlanId'
_a='qtechWebAuthStaOperType'
_Z='qtechWebAuthStaIp'
_Y='qtechWebAuthStaMac'
_X='authSDGUserTerminateCause'
_W='authSDGUserTimeUsed'
_V='authUserExtErrCause'
_U='authUserExtTimeUsed'
_T='authUserExtVlanId'
_S='authUserExtIfIndex'
_R='authUserExtMac'
_Q='authUserTerminateCause'
_P='authUserTimeUsed'
_O='qtechWebAuthWhiteListNetMask'
_N='qtechWebAuthWhiteListAddress'
_M='authSDGUserIpAddr'
_L='authSDGUserVrfg'
_K='authUserExtAddr'
_J='authUserExtAddrType'
_I='authUserIpAddr'
_H='DisplayString'
_G='OctetString'
_F='Integer32'
_E='accessible-for-notify'
_D='read-create'
_C='read-only'
_B='current'
_A='QTECH-AUTH-GATEWAY-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_G,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB',_e,'InetAddressType')
qtechMgmt,=mibBuilder.importSymbols('QTECH-SMI','qtechMgmt')
IfIndex,=mibBuilder.importSymbols('QTECH-TC','IfIndex')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_H,'MacAddress','PhysAddress','RowStatus','TextualConvention')
qtechWebAuthMIB=ModuleIdentity((1,3,6,1,4,1,27514,1,1,10,2,40))
if mibBuilder.loadTexts:qtechWebAuthMIB.setRevisions(('2010-03-08 00:00','2010-02-22 00:00','2009-04-16 00:00'))
_QtechWebAuthMIBObjects_ObjectIdentity=ObjectIdentity
qtechWebAuthMIBObjects=_QtechWebAuthMIBObjects_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,40,1))
_QtechWebAuthUserTable_Object=MibTable
qtechWebAuthUserTable=_QtechWebAuthUserTable_Object((1,3,6,1,4,1,27514,1,1,10,2,40,1,1))
if mibBuilder.loadTexts:qtechWebAuthUserTable.setStatus(_B)
_QtechWebAuthUserEntry_Object=MibTableRow
qtechWebAuthUserEntry=_QtechWebAuthUserEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,40,1,1,1))
qtechWebAuthUserEntry.setIndexNames((0,_A,_I))
if mibBuilder.loadTexts:qtechWebAuthUserEntry.setStatus(_B)
_AuthUserIpAddr_Type=IpAddress
_AuthUserIpAddr_Object=MibTableColumn
authUserIpAddr=_AuthUserIpAddr_Object((1,3,6,1,4,1,27514,1,1,10,2,40,1,1,1,1),_AuthUserIpAddr_Type())
authUserIpAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:authUserIpAddr.setStatus(_B)
_AuthUserOnlineFlag_Type=Gauge32
_AuthUserOnlineFlag_Object=MibTableColumn
authUserOnlineFlag=_AuthUserOnlineFlag_Object((1,3,6,1,4,1,27514,1,1,10,2,40,1,1,1,2),_AuthUserOnlineFlag_Type())
authUserOnlineFlag.setMaxAccess(_C)
if mibBuilder.loadTexts:authUserOnlineFlag.setStatus(_B)
_AuthUserTimeLimit_Type=Gauge32
_AuthUserTimeLimit_Object=MibTableColumn
authUserTimeLimit=_AuthUserTimeLimit_Object((1,3,6,1,4,1,27514,1,1,10,2,40,1,1,1,3),_AuthUserTimeLimit_Type())
authUserTimeLimit.setMaxAccess(_D)
if mibBuilder.loadTexts:authUserTimeLimit.setStatus(_B)
_AuthUserTimeUsed_Type=Gauge32
_AuthUserTimeUsed_Object=MibTableColumn
authUserTimeUsed=_AuthUserTimeUsed_Object((1,3,6,1,4,1,27514,1,1,10,2,40,1,1,1,4),_AuthUserTimeUsed_Type())
authUserTimeUsed.setMaxAccess(_C)
if mibBuilder.loadTexts:authUserTimeUsed.setStatus(_B)
_AuthUserStatus_Type=RowStatus
_AuthUserStatus_Object=MibTableColumn
authUserStatus=_AuthUserStatus_Object((1,3,6,1,4,1,27514,1,1,10,2,40,1,1,1,19),_AuthUserStatus_Type())
authUserStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:authUserStatus.setStatus(_B)
class _AuthUserRoleName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(32,32));fixedLength=32
_AuthUserRoleName_Type.__name__=_G
_AuthUserRoleName_Object=MibTableColumn
authUserRoleName=_AuthUserRoleName_Object((1,3,6,1,4,1,27514,1,1,10,2,40,1,1,1,20),_AuthUserRoleName_Type())
authUserRoleName.setMaxAccess(_D)
if mibBuilder.loadTexts:authUserRoleName.setStatus(_B)
class _AuthUserSecZoneName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(32,32));fixedLength=32
_AuthUserSecZoneName_Type.__name__=_G
_AuthUserSecZoneName_Object=MibTableColumn
authUserSecZoneName=_AuthUserSecZoneName_Object((1,3,6,1,4,1,27514,1,1,10,2,40,1,1,1,21),_AuthUserSecZoneName_Type())
authUserSecZoneName.setMaxAccess(_D)
if mibBuilder.loadTexts:authUserSecZoneName.setStatus(_B)
_AuthUserSecZonePermissionType_Type=Gauge32
_AuthUserSecZonePermissionType_Object=MibTableColumn
authUserSecZonePermissionType=_AuthUserSecZonePermissionType_Object((1,3,6,1,4,1,27514,1,1,10,2,40,1,1,1,22),_AuthUserSecZonePermissionType_Type())
authUserSecZonePermissionType.setMaxAccess(_D)
if mibBuilder.loadTexts:authUserSecZonePermissionType.setStatus(_B)
class _AuthUserSecZonePermissionList_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(512,512));fixedLength=512
_AuthUserSecZonePermissionList_Type.__name__=_G
_AuthUserSecZonePermissionList_Object=MibTableColumn
authUserSecZonePermissionList=_AuthUserSecZonePermissionList_Object((1,3,6,1,4,1,27514,1,1,10,2,40,1,1,1,23),_AuthUserSecZonePermissionList_Type())
authUserSecZonePermissionList.setMaxAccess(_D)
if mibBuilder.loadTexts:authUserSecZonePermissionList.setStatus(_B)
_AuthUserOtherPermissionType_Type=Gauge32
_AuthUserOtherPermissionType_Object=MibTableColumn
authUserOtherPermissionType=_AuthUserOtherPermissionType_Object((1,3,6,1,4,1,27514,1,1,10,2,40,1,1,1,24),_AuthUserOtherPermissionType_Type())
authUserOtherPermissionType.setMaxAccess(_D)
if mibBuilder.loadTexts:authUserOtherPermissionType.setStatus(_B)
_AuthUserTerminateCause_Type=Gauge32
_AuthUserTerminateCause_Object=MibTableColumn
authUserTerminateCause=_AuthUserTerminateCause_Object((1,3,6,1,4,1,27514,1,1,10,2,40,1,1,1,25),_AuthUserTerminateCause_Type())
authUserTerminateCause.setMaxAccess(_C)
if mibBuilder.loadTexts:authUserTerminateCause.setStatus(_B)
_QtechWebAuthUserExtTable_Object=MibTable
qtechWebAuthUserExtTable=_QtechWebAuthUserExtTable_Object((1,3,6,1,4,1,27514,1,1,10,2,40,1,2))
if mibBuilder.loadTexts:qtechWebAuthUserExtTable.setStatus(_B)
_QtechWebAuthUserExtEntry_Object=MibTableRow
qtechWebAuthUserExtEntry=_QtechWebAuthUserExtEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,40,1,2,1))
qtechWebAuthUserExtEntry.setIndexNames((0,_A,_J),(0,_A,_K))
if mibBuilder.loadTexts:qtechWebAuthUserExtEntry.setStatus(_B)
_AuthUserExtAddrType_Type=InetAddressType
_AuthUserExtAddrType_Object=MibTableColumn
authUserExtAddrType=_AuthUserExtAddrType_Object((1,3,6,1,4,1,27514,1,1,10,2,40,1,2,1,1),_AuthUserExtAddrType_Type())
authUserExtAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:authUserExtAddrType.setStatus(_B)
class _AuthUserExtAddr_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_AuthUserExtAddr_Type.__name__=_e
_AuthUserExtAddr_Object=MibTableColumn
authUserExtAddr=_AuthUserExtAddr_Object((1,3,6,1,4,1,27514,1,1,10,2,40,1,2,1,2),_AuthUserExtAddr_Type())
authUserExtAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:authUserExtAddr.setStatus(_B)
_AuthUserExtMac_Type=MacAddress
_AuthUserExtMac_Object=MibTableColumn
authUserExtMac=_AuthUserExtMac_Object((1,3,6,1,4,1,27514,1,1,10,2,40,1,2,1,3),_AuthUserExtMac_Type())
authUserExtMac.setMaxAccess(_C)
if mibBuilder.loadTexts:authUserExtMac.setStatus(_B)
_AuthUserExtIfIndex_Type=IfIndex
_AuthUserExtIfIndex_Object=MibTableColumn
authUserExtIfIndex=_AuthUserExtIfIndex_Object((1,3,6,1,4,1,27514,1,1,10,2,40,1,2,1,4),_AuthUserExtIfIndex_Type())
authUserExtIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:authUserExtIfIndex.setStatus(_B)
_AuthUserExtVlanId_Type=Unsigned32
_AuthUserExtVlanId_Object=MibTableColumn
authUserExtVlanId=_AuthUserExtVlanId_Object((1,3,6,1,4,1,27514,1,1,10,2,40,1,2,1,5),_AuthUserExtVlanId_Type())
authUserExtVlanId.setMaxAccess(_C)
if mibBuilder.loadTexts:authUserExtVlanId.setStatus(_B)
_AuthUserExtOnlineFlag_Type=Gauge32
_AuthUserExtOnlineFlag_Object=MibTableColumn
authUserExtOnlineFlag=_AuthUserExtOnlineFlag_Object((1,3,6,1,4,1,27514,1,1,10,2,40,1,2,1,6),_AuthUserExtOnlineFlag_Type())
authUserExtOnlineFlag.setMaxAccess(_C)
if mibBuilder.loadTexts:authUserExtOnlineFlag.setStatus(_B)
_AuthUserExtTimeLimit_Type=Gauge32
_AuthUserExtTimeLimit_Object=MibTableColumn
authUserExtTimeLimit=_AuthUserExtTimeLimit_Object((1,3,6,1,4,1,27514,1,1,10,2,40,1,2,1,7),_AuthUserExtTimeLimit_Type())
authUserExtTimeLimit.setMaxAccess(_D)
if mibBuilder.loadTexts:authUserExtTimeLimit.setStatus(_B)
_AuthUserExtTimeUsed_Type=Gauge32
_AuthUserExtTimeUsed_Object=MibTableColumn
authUserExtTimeUsed=_AuthUserExtTimeUsed_Object((1,3,6,1,4,1,27514,1,1,10,2,40,1,2,1,8),_AuthUserExtTimeUsed_Type())
authUserExtTimeUsed.setMaxAccess(_C)
if mibBuilder.loadTexts:authUserExtTimeUsed.setStatus(_B)
class _AuthUserExtErrCause_Type(DisplayString):defaultValue=OctetString('');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_AuthUserExtErrCause_Type.__name__=_H
_AuthUserExtErrCause_Object=MibTableColumn
authUserExtErrCause=_AuthUserExtErrCause_Object((1,3,6,1,4,1,27514,1,1,10,2,40,1,2,1,9),_AuthUserExtErrCause_Type())
authUserExtErrCause.setMaxAccess(_C)
if mibBuilder.loadTexts:authUserExtErrCause.setStatus(_B)
_AuthUserExtStatus_Type=RowStatus
_AuthUserExtStatus_Object=MibTableColumn
authUserExtStatus=_AuthUserExtStatus_Object((1,3,6,1,4,1,27514,1,1,10,2,40,1,2,1,10),_AuthUserExtStatus_Type())
authUserExtStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:authUserExtStatus.setStatus(_B)
_QtechWebAuthWhiteListTable_Object=MibTable
qtechWebAuthWhiteListTable=_QtechWebAuthWhiteListTable_Object((1,3,6,1,4,1,27514,1,1,10,2,40,1,3))
if mibBuilder.loadTexts:qtechWebAuthWhiteListTable.setStatus(_B)
_QtechWebAuthWhiteListEntry_Object=MibTableRow
qtechWebAuthWhiteListEntry=_QtechWebAuthWhiteListEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,40,1,3,1))
qtechWebAuthWhiteListEntry.setIndexNames((0,_A,_N),(0,_A,_O))
if mibBuilder.loadTexts:qtechWebAuthWhiteListEntry.setStatus(_B)
_QtechWebAuthWhiteListAddress_Type=IpAddress
_QtechWebAuthWhiteListAddress_Object=MibTableColumn
qtechWebAuthWhiteListAddress=_QtechWebAuthWhiteListAddress_Object((1,3,6,1,4,1,27514,1,1,10,2,40,1,3,1,1),_QtechWebAuthWhiteListAddress_Type())
qtechWebAuthWhiteListAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechWebAuthWhiteListAddress.setStatus(_B)
_QtechWebAuthWhiteListNetMask_Type=IpAddress
_QtechWebAuthWhiteListNetMask_Object=MibTableColumn
qtechWebAuthWhiteListNetMask=_QtechWebAuthWhiteListNetMask_Object((1,3,6,1,4,1,27514,1,1,10,2,40,1,3,1,2),_QtechWebAuthWhiteListNetMask_Type())
qtechWebAuthWhiteListNetMask.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechWebAuthWhiteListNetMask.setStatus(_B)
_QtechWebAuthWhiteListPort1_Type=Unsigned32
_QtechWebAuthWhiteListPort1_Object=MibTableColumn
qtechWebAuthWhiteListPort1=_QtechWebAuthWhiteListPort1_Object((1,3,6,1,4,1,27514,1,1,10,2,40,1,3,1,3),_QtechWebAuthWhiteListPort1_Type())
qtechWebAuthWhiteListPort1.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechWebAuthWhiteListPort1.setStatus(_B)
_QtechWebAuthWhiteListPort2_Type=Unsigned32
_QtechWebAuthWhiteListPort2_Object=MibTableColumn
qtechWebAuthWhiteListPort2=_QtechWebAuthWhiteListPort2_Object((1,3,6,1,4,1,27514,1,1,10,2,40,1,3,1,4),_QtechWebAuthWhiteListPort2_Type())
qtechWebAuthWhiteListPort2.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechWebAuthWhiteListPort2.setStatus(_B)
_QtechWebAuthWhiteListPort3_Type=Unsigned32
_QtechWebAuthWhiteListPort3_Object=MibTableColumn
qtechWebAuthWhiteListPort3=_QtechWebAuthWhiteListPort3_Object((1,3,6,1,4,1,27514,1,1,10,2,40,1,3,1,5),_QtechWebAuthWhiteListPort3_Type())
qtechWebAuthWhiteListPort3.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechWebAuthWhiteListPort3.setStatus(_B)
_QtechWebAuthWhiteListPort4_Type=Unsigned32
_QtechWebAuthWhiteListPort4_Object=MibTableColumn
qtechWebAuthWhiteListPort4=_QtechWebAuthWhiteListPort4_Object((1,3,6,1,4,1,27514,1,1,10,2,40,1,3,1,6),_QtechWebAuthWhiteListPort4_Type())
qtechWebAuthWhiteListPort4.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechWebAuthWhiteListPort4.setStatus(_B)
_QtechWebAuthWhiteListPort5_Type=Unsigned32
_QtechWebAuthWhiteListPort5_Object=MibTableColumn
qtechWebAuthWhiteListPort5=_QtechWebAuthWhiteListPort5_Object((1,3,6,1,4,1,27514,1,1,10,2,40,1,3,1,7),_QtechWebAuthWhiteListPort5_Type())
qtechWebAuthWhiteListPort5.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechWebAuthWhiteListPort5.setStatus(_B)
_QtechWebAuthWhiteListPort6_Type=Unsigned32
_QtechWebAuthWhiteListPort6_Object=MibTableColumn
qtechWebAuthWhiteListPort6=_QtechWebAuthWhiteListPort6_Object((1,3,6,1,4,1,27514,1,1,10,2,40,1,3,1,8),_QtechWebAuthWhiteListPort6_Type())
qtechWebAuthWhiteListPort6.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechWebAuthWhiteListPort6.setStatus(_B)
_QtechWebAuthWhiteListPort7_Type=Unsigned32
_QtechWebAuthWhiteListPort7_Object=MibTableColumn
qtechWebAuthWhiteListPort7=_QtechWebAuthWhiteListPort7_Object((1,3,6,1,4,1,27514,1,1,10,2,40,1,3,1,9),_QtechWebAuthWhiteListPort7_Type())
qtechWebAuthWhiteListPort7.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechWebAuthWhiteListPort7.setStatus(_B)
_QtechWebAuthWhiteListPort8_Type=Unsigned32
_QtechWebAuthWhiteListPort8_Object=MibTableColumn
qtechWebAuthWhiteListPort8=_QtechWebAuthWhiteListPort8_Object((1,3,6,1,4,1,27514,1,1,10,2,40,1,3,1,10),_QtechWebAuthWhiteListPort8_Type())
qtechWebAuthWhiteListPort8.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechWebAuthWhiteListPort8.setStatus(_B)
class _QtechWebAuthWhiteListBindArpFlag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('no',0),('yes',1)))
_QtechWebAuthWhiteListBindArpFlag_Type.__name__=_F
_QtechWebAuthWhiteListBindArpFlag_Object=MibTableColumn
qtechWebAuthWhiteListBindArpFlag=_QtechWebAuthWhiteListBindArpFlag_Object((1,3,6,1,4,1,27514,1,1,10,2,40,1,3,1,11),_QtechWebAuthWhiteListBindArpFlag_Type())
qtechWebAuthWhiteListBindArpFlag.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechWebAuthWhiteListBindArpFlag.setStatus(_B)
_QtechWebAuthWhiteListStatus_Type=RowStatus
_QtechWebAuthWhiteListStatus_Object=MibTableColumn
qtechWebAuthWhiteListStatus=_QtechWebAuthWhiteListStatus_Object((1,3,6,1,4,1,27514,1,1,10,2,40,1,3,1,12),_QtechWebAuthWhiteListStatus_Type())
qtechWebAuthWhiteListStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechWebAuthWhiteListStatus.setStatus(_B)
_QtechWebAuthSDGUserTable_Object=MibTable
qtechWebAuthSDGUserTable=_QtechWebAuthSDGUserTable_Object((1,3,6,1,4,1,27514,1,1,10,2,40,1,4))
if mibBuilder.loadTexts:qtechWebAuthSDGUserTable.setStatus(_B)
_QtechWebAuthSDGUserEntry_Object=MibTableRow
qtechWebAuthSDGUserEntry=_QtechWebAuthSDGUserEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,40,1,4,1))
qtechWebAuthSDGUserEntry.setIndexNames((0,_A,_L),(0,_A,_M))
if mibBuilder.loadTexts:qtechWebAuthSDGUserEntry.setStatus(_B)
class _AuthSDGUserVrfg_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_AuthSDGUserVrfg_Type.__name__=_H
_AuthSDGUserVrfg_Object=MibTableColumn
authSDGUserVrfg=_AuthSDGUserVrfg_Object((1,3,6,1,4,1,27514,1,1,10,2,40,1,4,1,1),_AuthSDGUserVrfg_Type())
authSDGUserVrfg.setMaxAccess(_C)
if mibBuilder.loadTexts:authSDGUserVrfg.setStatus(_B)
_AuthSDGUserIpAddr_Type=IpAddress
_AuthSDGUserIpAddr_Object=MibTableColumn
authSDGUserIpAddr=_AuthSDGUserIpAddr_Object((1,3,6,1,4,1,27514,1,1,10,2,40,1,4,1,2),_AuthSDGUserIpAddr_Type())
authSDGUserIpAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:authSDGUserIpAddr.setStatus(_B)
_AuthSDGUserOnlineFlag_Type=Gauge32
_AuthSDGUserOnlineFlag_Object=MibTableColumn
authSDGUserOnlineFlag=_AuthSDGUserOnlineFlag_Object((1,3,6,1,4,1,27514,1,1,10,2,40,1,4,1,3),_AuthSDGUserOnlineFlag_Type())
authSDGUserOnlineFlag.setMaxAccess(_C)
if mibBuilder.loadTexts:authSDGUserOnlineFlag.setStatus(_B)
_AuthSDGUserTimeLimit_Type=Gauge32
_AuthSDGUserTimeLimit_Object=MibTableColumn
authSDGUserTimeLimit=_AuthSDGUserTimeLimit_Object((1,3,6,1,4,1,27514,1,1,10,2,40,1,4,1,4),_AuthSDGUserTimeLimit_Type())
authSDGUserTimeLimit.setMaxAccess(_D)
if mibBuilder.loadTexts:authSDGUserTimeLimit.setStatus(_B)
_AuthSDGUserTimeUsed_Type=Gauge32
_AuthSDGUserTimeUsed_Object=MibTableColumn
authSDGUserTimeUsed=_AuthSDGUserTimeUsed_Object((1,3,6,1,4,1,27514,1,1,10,2,40,1,4,1,5),_AuthSDGUserTimeUsed_Type())
authSDGUserTimeUsed.setMaxAccess(_C)
if mibBuilder.loadTexts:authSDGUserTimeUsed.setStatus(_B)
_AuthSDGUserVrf_Type=DisplayString
_AuthSDGUserVrf_Object=MibTableColumn
authSDGUserVrf=_AuthSDGUserVrf_Object((1,3,6,1,4,1,27514,1,1,10,2,40,1,4,1,6),_AuthSDGUserVrf_Type())
authSDGUserVrf.setMaxAccess(_C)
if mibBuilder.loadTexts:authSDGUserVrf.setStatus(_B)
class _AuthSDGUserRoleName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(32,32));fixedLength=32
_AuthSDGUserRoleName_Type.__name__=_G
_AuthSDGUserRoleName_Object=MibTableColumn
authSDGUserRoleName=_AuthSDGUserRoleName_Object((1,3,6,1,4,1,27514,1,1,10,2,40,1,4,1,21),_AuthSDGUserRoleName_Type())
authSDGUserRoleName.setMaxAccess(_D)
if mibBuilder.loadTexts:authSDGUserRoleName.setStatus(_B)
class _AuthSDGUserSecZoneName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(32,32));fixedLength=32
_AuthSDGUserSecZoneName_Type.__name__=_G
_AuthSDGUserSecZoneName_Object=MibTableColumn
authSDGUserSecZoneName=_AuthSDGUserSecZoneName_Object((1,3,6,1,4,1,27514,1,1,10,2,40,1,4,1,22),_AuthSDGUserSecZoneName_Type())
authSDGUserSecZoneName.setMaxAccess(_D)
if mibBuilder.loadTexts:authSDGUserSecZoneName.setStatus(_B)
_AuthSDGUserSecZonePermissionType_Type=Gauge32
_AuthSDGUserSecZonePermissionType_Object=MibTableColumn
authSDGUserSecZonePermissionType=_AuthSDGUserSecZonePermissionType_Object((1,3,6,1,4,1,27514,1,1,10,2,40,1,4,1,23),_AuthSDGUserSecZonePermissionType_Type())
authSDGUserSecZonePermissionType.setMaxAccess(_D)
if mibBuilder.loadTexts:authSDGUserSecZonePermissionType.setStatus(_B)
class _AuthSDGUserSecZonePermissionList_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(512,512));fixedLength=512
_AuthSDGUserSecZonePermissionList_Type.__name__=_G
_AuthSDGUserSecZonePermissionList_Object=MibTableColumn
authSDGUserSecZonePermissionList=_AuthSDGUserSecZonePermissionList_Object((1,3,6,1,4,1,27514,1,1,10,2,40,1,4,1,24),_AuthSDGUserSecZonePermissionList_Type())
authSDGUserSecZonePermissionList.setMaxAccess(_D)
if mibBuilder.loadTexts:authSDGUserSecZonePermissionList.setStatus(_B)
_AuthSDGUserOtherPermissionType_Type=Gauge32
_AuthSDGUserOtherPermissionType_Object=MibTableColumn
authSDGUserOtherPermissionType=_AuthSDGUserOtherPermissionType_Object((1,3,6,1,4,1,27514,1,1,10,2,40,1,4,1,25),_AuthSDGUserOtherPermissionType_Type())
authSDGUserOtherPermissionType.setMaxAccess(_D)
if mibBuilder.loadTexts:authSDGUserOtherPermissionType.setStatus(_B)
_AuthSDGUserTerminateCause_Type=Gauge32
_AuthSDGUserTerminateCause_Object=MibTableColumn
authSDGUserTerminateCause=_AuthSDGUserTerminateCause_Object((1,3,6,1,4,1,27514,1,1,10,2,40,1,4,1,26),_AuthSDGUserTerminateCause_Type())
authSDGUserTerminateCause.setMaxAccess(_C)
if mibBuilder.loadTexts:authSDGUserTerminateCause.setStatus(_B)
_AuthSDGUserStatus_Type=RowStatus
_AuthSDGUserStatus_Object=MibTableColumn
authSDGUserStatus=_AuthSDGUserStatus_Object((1,3,6,1,4,1,27514,1,1,10,2,40,1,4,1,27),_AuthSDGUserStatus_Type())
authSDGUserStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:authSDGUserStatus.setStatus(_B)
_QtechWebAuthMacUserTable_Object=MibTable
qtechWebAuthMacUserTable=_QtechWebAuthMacUserTable_Object((1,3,6,1,4,1,27514,1,1,10,2,40,1,5))
if mibBuilder.loadTexts:qtechWebAuthMacUserTable.setStatus(_B)
_QtechWebAuthMacUserEntry_Object=MibTableRow
qtechWebAuthMacUserEntry=_QtechWebAuthMacUserEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,40,1,5,1))
qtechWebAuthMacUserEntry.setIndexNames((0,_A,_f))
if mibBuilder.loadTexts:qtechWebAuthMacUserEntry.setStatus(_B)
_QtechAuthMacUserMacAddr_Type=MacAddress
_QtechAuthMacUserMacAddr_Object=MibTableColumn
qtechAuthMacUserMacAddr=_QtechAuthMacUserMacAddr_Object((1,3,6,1,4,1,27514,1,1,10,2,40,1,5,1,1),_QtechAuthMacUserMacAddr_Type())
qtechAuthMacUserMacAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechAuthMacUserMacAddr.setStatus(_B)
class _QtechAuthMacUserName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(253,253));fixedLength=253
_QtechAuthMacUserName_Type.__name__=_G
_QtechAuthMacUserName_Object=MibTableColumn
qtechAuthMacUserName=_QtechAuthMacUserName_Object((1,3,6,1,4,1,27514,1,1,10,2,40,1,5,1,2),_QtechAuthMacUserName_Type())
qtechAuthMacUserName.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechAuthMacUserName.setStatus(_B)
class _QtechAuthMacUserTerminalId_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(253,253));fixedLength=253
_QtechAuthMacUserTerminalId_Type.__name__=_G
_QtechAuthMacUserTerminalId_Object=MibTableColumn
qtechAuthMacUserTerminalId=_QtechAuthMacUserTerminalId_Object((1,3,6,1,4,1,27514,1,1,10,2,40,1,5,1,3),_QtechAuthMacUserTerminalId_Type())
qtechAuthMacUserTerminalId.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechAuthMacUserTerminalId.setStatus(_B)
_QtechWebAuthUserMIB_ObjectIdentity=ObjectIdentity
qtechWebAuthUserMIB=_QtechWebAuthUserMIB_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,40,1,6))
_QtechWebAuthUserMIBTable_Object=MibTable
qtechWebAuthUserMIBTable=_QtechWebAuthUserMIBTable_Object((1,3,6,1,4,1,27514,1,1,10,2,40,1,6,1))
if mibBuilder.loadTexts:qtechWebAuthUserMIBTable.setStatus(_B)
_QtechWebAuthUserMIBEntry_Object=MibTableRow
qtechWebAuthUserMIBEntry=_QtechWebAuthUserMIBEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,40,1,6,1,1))
qtechWebAuthUserMIBEntry.setIndexNames((0,_A,_g))
if mibBuilder.loadTexts:qtechWebAuthUserMIBEntry.setStatus(_B)
_QtechAuthUserMIBIpAddress_Type=IpAddress
_QtechAuthUserMIBIpAddress_Object=MibTableColumn
qtechAuthUserMIBIpAddress=_QtechAuthUserMIBIpAddress_Object((1,3,6,1,4,1,27514,1,1,10,2,40,1,6,1,1,1),_QtechAuthUserMIBIpAddress_Type())
qtechAuthUserMIBIpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechAuthUserMIBIpAddress.setStatus(_B)
_QtechAuthUserMIBName_Type=OctetString
_QtechAuthUserMIBName_Object=MibTableColumn
qtechAuthUserMIBName=_QtechAuthUserMIBName_Object((1,3,6,1,4,1,27514,1,1,10,2,40,1,6,1,1,2),_QtechAuthUserMIBName_Type())
qtechAuthUserMIBName.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechAuthUserMIBName.setStatus(_B)
_QtechAuthUserMIBAuthType_Type=Gauge32
_QtechAuthUserMIBAuthType_Object=MibTableColumn
qtechAuthUserMIBAuthType=_QtechAuthUserMIBAuthType_Object((1,3,6,1,4,1,27514,1,1,10,2,40,1,6,1,1,3),_QtechAuthUserMIBAuthType_Type())
qtechAuthUserMIBAuthType.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechAuthUserMIBAuthType.setStatus(_B)
_QtechAuthUserMIBMacAddress_Type=MacAddress
_QtechAuthUserMIBMacAddress_Object=MibTableColumn
qtechAuthUserMIBMacAddress=_QtechAuthUserMIBMacAddress_Object((1,3,6,1,4,1,27514,1,1,10,2,40,1,6,1,1,4),_QtechAuthUserMIBMacAddress_Type())
qtechAuthUserMIBMacAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechAuthUserMIBMacAddress.setStatus(_B)
_QtechAuthUserMIBVlanId_Type=Gauge32
_QtechAuthUserMIBVlanId_Object=MibTableColumn
qtechAuthUserMIBVlanId=_QtechAuthUserMIBVlanId_Object((1,3,6,1,4,1,27514,1,1,10,2,40,1,6,1,1,5),_QtechAuthUserMIBVlanId_Type())
qtechAuthUserMIBVlanId.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechAuthUserMIBVlanId.setStatus(_B)
_QtechAuthUserMIBPortIndex_Type=Gauge32
_QtechAuthUserMIBPortIndex_Object=MibTableColumn
qtechAuthUserMIBPortIndex=_QtechAuthUserMIBPortIndex_Object((1,3,6,1,4,1,27514,1,1,10,2,40,1,6,1,1,6),_QtechAuthUserMIBPortIndex_Type())
qtechAuthUserMIBPortIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechAuthUserMIBPortIndex.setStatus(_B)
_QtechAuthUserMIBTimeUsed_Type=Gauge32
_QtechAuthUserMIBTimeUsed_Object=MibTableColumn
qtechAuthUserMIBTimeUsed=_QtechAuthUserMIBTimeUsed_Object((1,3,6,1,4,1,27514,1,1,10,2,40,1,6,1,1,7),_QtechAuthUserMIBTimeUsed_Type())
qtechAuthUserMIBTimeUsed.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechAuthUserMIBTimeUsed.setStatus(_B)
_QtechWebAuthMIBTraps_ObjectIdentity=ObjectIdentity
qtechWebAuthMIBTraps=_QtechWebAuthMIBTraps_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,40,2))
_QtechWebAuthMIBConformance_ObjectIdentity=ObjectIdentity
qtechWebAuthMIBConformance=_QtechWebAuthMIBConformance_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,40,3))
_QtechWebAuthMIBCompliances_ObjectIdentity=ObjectIdentity
qtechWebAuthMIBCompliances=_QtechWebAuthMIBCompliances_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,40,3,1))
_QtechWebAuthMIBGroups_ObjectIdentity=ObjectIdentity
qtechWebAuthMIBGroups=_QtechWebAuthMIBGroups_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,40,3,2))
_QtechWebAuthMIBTrapsObjects_ObjectIdentity=ObjectIdentity
qtechWebAuthMIBTrapsObjects=_QtechWebAuthMIBTrapsObjects_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,40,4))
_QtechWebAuthApMac_Type=MacAddress
_QtechWebAuthApMac_Object=MibScalar
qtechWebAuthApMac=_QtechWebAuthApMac_Object((1,3,6,1,4,1,27514,1,1,10,2,40,4,1),_QtechWebAuthApMac_Type())
qtechWebAuthApMac.setMaxAccess(_E)
if mibBuilder.loadTexts:qtechWebAuthApMac.setStatus(_B)
_QtechWebAuthApIp_Type=IpAddress
_QtechWebAuthApIp_Object=MibScalar
qtechWebAuthApIp=_QtechWebAuthApIp_Object((1,3,6,1,4,1,27514,1,1,10,2,40,4,2),_QtechWebAuthApIp_Type())
qtechWebAuthApIp.setMaxAccess(_E)
if mibBuilder.loadTexts:qtechWebAuthApIp.setStatus(_B)
_QtechWebAuthStaMac_Type=MacAddress
_QtechWebAuthStaMac_Object=MibScalar
qtechWebAuthStaMac=_QtechWebAuthStaMac_Object((1,3,6,1,4,1,27514,1,1,10,2,40,4,3),_QtechWebAuthStaMac_Type())
qtechWebAuthStaMac.setMaxAccess(_E)
if mibBuilder.loadTexts:qtechWebAuthStaMac.setStatus(_B)
_QtechWebAuthStaIp_Type=IpAddress
_QtechWebAuthStaIp_Object=MibScalar
qtechWebAuthStaIp=_QtechWebAuthStaIp_Object((1,3,6,1,4,1,27514,1,1,10,2,40,4,4),_QtechWebAuthStaIp_Type())
qtechWebAuthStaIp.setMaxAccess(_E)
if mibBuilder.loadTexts:qtechWebAuthStaIp.setStatus(_B)
_QtechWebAuthStaIpv6_Type=InetAddress
_QtechWebAuthStaIpv6_Object=MibScalar
qtechWebAuthStaIpv6=_QtechWebAuthStaIpv6_Object((1,3,6,1,4,1,27514,1,1,10,2,40,4,5),_QtechWebAuthStaIpv6_Type())
qtechWebAuthStaIpv6.setMaxAccess(_E)
if mibBuilder.loadTexts:qtechWebAuthStaIpv6.setStatus(_B)
class _QtechWebAuthStaOperType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,3))
_QtechWebAuthStaOperType_Type.__name__=_F
_QtechWebAuthStaOperType_Object=MibScalar
qtechWebAuthStaOperType=_QtechWebAuthStaOperType_Object((1,3,6,1,4,1,27514,1,1,10,2,40,4,6),_QtechWebAuthStaOperType_Type())
qtechWebAuthStaOperType.setMaxAccess(_E)
if mibBuilder.loadTexts:qtechWebAuthStaOperType.setStatus(_B)
class _QtechWebAuthStaApRadioId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_QtechWebAuthStaApRadioId_Type.__name__=_F
_QtechWebAuthStaApRadioId_Object=MibScalar
qtechWebAuthStaApRadioId=_QtechWebAuthStaApRadioId_Object((1,3,6,1,4,1,27514,1,1,10,2,40,4,7),_QtechWebAuthStaApRadioId_Type())
qtechWebAuthStaApRadioId.setMaxAccess(_E)
if mibBuilder.loadTexts:qtechWebAuthStaApRadioId.setStatus(_B)
class _QtechWebAuthStaApRadioType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_QtechWebAuthStaApRadioType_Type.__name__=_F
_QtechWebAuthStaApRadioType_Object=MibScalar
qtechWebAuthStaApRadioType=_QtechWebAuthStaApRadioType_Object((1,3,6,1,4,1,27514,1,1,10,2,40,4,8),_QtechWebAuthStaApRadioType_Type())
qtechWebAuthStaApRadioType.setMaxAccess(_E)
if mibBuilder.loadTexts:qtechWebAuthStaApRadioType.setStatus(_B)
class _QtechWebAuthStaVlanId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_QtechWebAuthStaVlanId_Type.__name__=_F
_QtechWebAuthStaVlanId_Object=MibScalar
qtechWebAuthStaVlanId=_QtechWebAuthStaVlanId_Object((1,3,6,1,4,1,27514,1,1,10,2,40,4,9),_QtechWebAuthStaVlanId_Type())
qtechWebAuthStaVlanId.setMaxAccess(_E)
if mibBuilder.loadTexts:qtechWebAuthStaVlanId.setStatus(_B)
class _QtechWebAuthStaWlanId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_QtechWebAuthStaWlanId_Type.__name__=_F
_QtechWebAuthStaWlanId_Object=MibScalar
qtechWebAuthStaWlanId=_QtechWebAuthStaWlanId_Object((1,3,6,1,4,1,27514,1,1,10,2,40,4,10),_QtechWebAuthStaWlanId_Type())
qtechWebAuthStaWlanId.setMaxAccess(_E)
if mibBuilder.loadTexts:qtechWebAuthStaWlanId.setStatus(_B)
_QtechWebAuthOperTime_Type=TimeTicks
_QtechWebAuthOperTime_Object=MibScalar
qtechWebAuthOperTime=_QtechWebAuthOperTime_Object((1,3,6,1,4,1,27514,1,1,10,2,40,4,11),_QtechWebAuthOperTime_Type())
qtechWebAuthOperTime.setMaxAccess(_E)
if mibBuilder.loadTexts:qtechWebAuthOperTime.setStatus(_B)
class _QtechWebAuthStaAssoAuthMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('open',0),('wep',1),('dot1x-wep',2),('dot1x-wpa',3),('dot1x-wpa2',4),('mab',5),('psk-wpa',6),('psk-wpa2',7),('wapi',8)))
_QtechWebAuthStaAssoAuthMode_Type.__name__=_F
_QtechWebAuthStaAssoAuthMode_Object=MibScalar
qtechWebAuthStaAssoAuthMode=_QtechWebAuthStaAssoAuthMode_Object((1,3,6,1,4,1,27514,1,1,10,2,40,4,12),_QtechWebAuthStaAssoAuthMode_Type())
qtechWebAuthStaAssoAuthMode.setMaxAccess(_E)
if mibBuilder.loadTexts:qtechWebAuthStaAssoAuthMode.setStatus(_B)
class _QtechWebAuthStaNetAuthMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('open',0),('web',1)))
_QtechWebAuthStaNetAuthMode_Type.__name__=_F
_QtechWebAuthStaNetAuthMode_Object=MibScalar
qtechWebAuthStaNetAuthMode=_QtechWebAuthStaNetAuthMode_Object((1,3,6,1,4,1,27514,1,1,10,2,40,4,13),_QtechWebAuthStaNetAuthMode_Type())
qtechWebAuthStaNetAuthMode.setMaxAccess(_E)
if mibBuilder.loadTexts:qtechWebAuthStaNetAuthMode.setStatus(_B)
_QtechWebAuthStaRssi_Type=Integer32
_QtechWebAuthStaRssi_Object=MibScalar
qtechWebAuthStaRssi=_QtechWebAuthStaRssi_Object((1,3,6,1,4,1,27514,1,1,10,2,40,4,14),_QtechWebAuthStaRssi_Type())
qtechWebAuthStaRssi.setMaxAccess(_E)
if mibBuilder.loadTexts:qtechWebAuthStaRssi.setStatus(_B)
_QtechWebAuthStaSsid_Type=DisplayString
_QtechWebAuthStaSsid_Object=MibScalar
qtechWebAuthStaSsid=_QtechWebAuthStaSsid_Object((1,3,6,1,4,1,27514,1,1,10,2,40,4,15),_QtechWebAuthStaSsid_Type())
qtechWebAuthStaSsid.setMaxAccess(_E)
if mibBuilder.loadTexts:qtechWebAuthStaSsid.setStatus(_B)
_QtechWebAuthStaLinkRate_Type=Integer32
_QtechWebAuthStaLinkRate_Object=MibScalar
qtechWebAuthStaLinkRate=_QtechWebAuthStaLinkRate_Object((1,3,6,1,4,1,27514,1,1,10,2,40,4,16),_QtechWebAuthStaLinkRate_Type())
qtechWebAuthStaLinkRate.setMaxAccess(_E)
if mibBuilder.loadTexts:qtechWebAuthStaLinkRate.setStatus(_B)
_QtechWebAuthStaCurChannel_Type=Integer32
_QtechWebAuthStaCurChannel_Object=MibScalar
qtechWebAuthStaCurChannel=_QtechWebAuthStaCurChannel_Object((1,3,6,1,4,1,27514,1,1,10,2,40,4,17),_QtechWebAuthStaCurChannel_Type())
qtechWebAuthStaCurChannel.setMaxAccess(_E)
if mibBuilder.loadTexts:qtechWebAuthStaCurChannel.setStatus(_B)
class _QtechWebAuthStaUsername_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_QtechWebAuthStaUsername_Type.__name__=_H
_QtechWebAuthStaUsername_Object=MibScalar
qtechWebAuthStaUsername=_QtechWebAuthStaUsername_Object((1,3,6,1,4,1,27514,1,1,10,2,40,4,18),_QtechWebAuthStaUsername_Type())
qtechWebAuthStaUsername.setMaxAccess(_E)
if mibBuilder.loadTexts:qtechWebAuthStaUsername.setStatus(_B)
_QtechWebAuthStaTerminalType_Type=DisplayString
_QtechWebAuthStaTerminalType_Object=MibScalar
qtechWebAuthStaTerminalType=_QtechWebAuthStaTerminalType_Object((1,3,6,1,4,1,27514,1,1,10,2,40,4,19),_QtechWebAuthStaTerminalType_Type())
qtechWebAuthStaTerminalType.setMaxAccess(_E)
if mibBuilder.loadTexts:qtechWebAuthStaTerminalType.setStatus(_B)
_QtechWebAuthStaTerminateCause_Type=Integer32
_QtechWebAuthStaTerminateCause_Object=MibScalar
qtechWebAuthStaTerminateCause=_QtechWebAuthStaTerminateCause_Object((1,3,6,1,4,1,27514,1,1,10,2,40,4,20),_QtechWebAuthStaTerminateCause_Type())
qtechWebAuthStaTerminateCause.setMaxAccess(_E)
if mibBuilder.loadTexts:qtechWebAuthStaTerminateCause.setStatus(_B)
_QtechWebAuthStaReplyMessage_Type=DisplayString
_QtechWebAuthStaReplyMessage_Object=MibScalar
qtechWebAuthStaReplyMessage=_QtechWebAuthStaReplyMessage_Object((1,3,6,1,4,1,27514,1,1,10,2,40,4,21),_QtechWebAuthStaReplyMessage_Type())
qtechWebAuthStaReplyMessage.setMaxAccess(_E)
if mibBuilder.loadTexts:qtechWebAuthStaReplyMessage.setStatus(_B)
_QtechWebAuthStaTerminalId_Type=DisplayString
_QtechWebAuthStaTerminalId_Object=MibScalar
qtechWebAuthStaTerminalId=_QtechWebAuthStaTerminalId_Object((1,3,6,1,4,1,27514,1,1,10,2,40,4,22),_QtechWebAuthStaTerminalId_Type())
qtechWebAuthStaTerminalId.setMaxAccess(_E)
if mibBuilder.loadTexts:qtechWebAuthStaTerminalId.setStatus(_B)
class _QtechWebAuthType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_QtechWebAuthType_Type.__name__=_F
_QtechWebAuthType_Object=MibScalar
qtechWebAuthType=_QtechWebAuthType_Object((1,3,6,1,4,1,27514,1,1,10,2,40,4,23),_QtechWebAuthType_Type())
qtechWebAuthType.setMaxAccess(_E)
if mibBuilder.loadTexts:qtechWebAuthType.setStatus(_B)
_QtechWebAuthPortIndex_Type=Integer32
_QtechWebAuthPortIndex_Object=MibScalar
qtechWebAuthPortIndex=_QtechWebAuthPortIndex_Object((1,3,6,1,4,1,27514,1,1,10,2,40,4,24),_QtechWebAuthPortIndex_Type())
qtechWebAuthPortIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:qtechWebAuthPortIndex.setStatus(_B)
qtechWebAuthMIBGroup=ObjectGroup((1,3,6,1,4,1,27514,1,1,10,2,40,3,2,1))
qtechWebAuthMIBGroup.setObjects(*((_A,_I),(_A,_h),(_A,_i),(_A,_P),(_A,_j),(_A,_k),(_A,_l),(_A,_m),(_A,_n),(_A,_o),(_A,_Q),(_A,_J),(_A,_K),(_A,_R),(_A,_S),(_A,_T),(_A,_p),(_A,_q),(_A,_U),(_A,_V),(_A,_r),(_A,_N),(_A,_O),(_A,_s),(_A,_t),(_A,_u),(_A,_v),(_A,_w),(_A,_x),(_A,_y),(_A,_z),(_A,_A0),(_A,_A1),(_A,_L),(_A,_M),(_A,_A2),(_A,_A3),(_A,_W),(_A,_A4),(_A,_A5),(_A,_A6),(_A,_A7),(_A,_A8),(_A,_A9),(_A,_X),(_A,_AA)))
if mibBuilder.loadTexts:qtechWebAuthMIBGroup.setStatus(_B)
qtechWebAuthUserLeave=NotificationType((1,3,6,1,4,1,27514,1,1,10,2,40,2,1))
qtechWebAuthUserLeave.setObjects(*((_A,_I),(_A,_P),(_A,_Q)))
if mibBuilder.loadTexts:qtechWebAuthUserLeave.setStatus(_B)
qtechWebAuthUserExtLeave=NotificationType((1,3,6,1,4,1,27514,1,1,10,2,40,2,2))
qtechWebAuthUserExtLeave.setObjects(*((_A,_J),(_A,_K),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V)))
if mibBuilder.loadTexts:qtechWebAuthUserExtLeave.setStatus(_B)
qtechWebAuthSDGUserLeave=NotificationType((1,3,6,1,4,1,27514,1,1,10,2,40,2,3))
qtechWebAuthSDGUserLeave.setObjects(*((_A,_L),(_A,_M),(_A,_W),(_A,_X)))
if mibBuilder.loadTexts:qtechWebAuthSDGUserLeave.setStatus(_B)
qtechWebAuthWlanMgmt=NotificationType((1,3,6,1,4,1,27514,1,1,10,2,40,2,4))
qtechWebAuthWlanMgmt.setObjects(*((_A,_AB),(_A,_AC),(_A,_Y),(_A,_Z),(_A,_AD),(_A,_a),(_A,_AE),(_A,_AF),(_A,_b),(_A,_AG),(_A,_AH),(_A,_AI),(_A,_AJ),(_A,_AK),(_A,_AL),(_A,_AM),(_A,_AN),(_A,_c),(_A,_AO),(_A,_d),(_A,_AP),(_A,_AQ)))
if mibBuilder.loadTexts:qtechWebAuthWlanMgmt.setStatus(_B)
qtechWebAuthUserOper=NotificationType((1,3,6,1,4,1,27514,1,1,10,2,40,2,5))
qtechWebAuthUserOper.setObjects(*((_A,_a),(_A,_AR),(_A,_c),(_A,_Z),(_A,_Y),(_A,_b),(_A,_AS),(_A,_d)))
if mibBuilder.loadTexts:qtechWebAuthUserOper.setStatus(_B)
qtechWebAuthTrapGroup=NotificationGroup((1,3,6,1,4,1,27514,1,1,10,2,40,3,2,2))
qtechWebAuthTrapGroup.setObjects(*((_A,_AT),(_A,_AU),(_A,_AV)))
if mibBuilder.loadTexts:qtechWebAuthTrapGroup.setStatus(_B)
qtechWebAuthMIBCompliance=ModuleCompliance((1,3,6,1,4,1,27514,1,1,10,2,40,3,1,1))
qtechWebAuthMIBCompliance.setObjects(*((_A,_AW),(_A,_AX)))
if mibBuilder.loadTexts:qtechWebAuthMIBCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'qtechWebAuthMIB':qtechWebAuthMIB,'qtechWebAuthMIBObjects':qtechWebAuthMIBObjects,'qtechWebAuthUserTable':qtechWebAuthUserTable,'qtechWebAuthUserEntry':qtechWebAuthUserEntry,_I:authUserIpAddr,_h:authUserOnlineFlag,_i:authUserTimeLimit,_P:authUserTimeUsed,_j:authUserStatus,_k:authUserRoleName,_l:authUserSecZoneName,_m:authUserSecZonePermissionType,_n:authUserSecZonePermissionList,_o:authUserOtherPermissionType,_Q:authUserTerminateCause,'qtechWebAuthUserExtTable':qtechWebAuthUserExtTable,'qtechWebAuthUserExtEntry':qtechWebAuthUserExtEntry,_J:authUserExtAddrType,_K:authUserExtAddr,_R:authUserExtMac,_S:authUserExtIfIndex,_T:authUserExtVlanId,_p:authUserExtOnlineFlag,_q:authUserExtTimeLimit,_U:authUserExtTimeUsed,_V:authUserExtErrCause,_r:authUserExtStatus,'qtechWebAuthWhiteListTable':qtechWebAuthWhiteListTable,'qtechWebAuthWhiteListEntry':qtechWebAuthWhiteListEntry,_N:qtechWebAuthWhiteListAddress,_O:qtechWebAuthWhiteListNetMask,_s:qtechWebAuthWhiteListPort1,_t:qtechWebAuthWhiteListPort2,_u:qtechWebAuthWhiteListPort3,_v:qtechWebAuthWhiteListPort4,_w:qtechWebAuthWhiteListPort5,_x:qtechWebAuthWhiteListPort6,_y:qtechWebAuthWhiteListPort7,_z:qtechWebAuthWhiteListPort8,_A0:qtechWebAuthWhiteListBindArpFlag,_A1:qtechWebAuthWhiteListStatus,'qtechWebAuthSDGUserTable':qtechWebAuthSDGUserTable,'qtechWebAuthSDGUserEntry':qtechWebAuthSDGUserEntry,_L:authSDGUserVrfg,_M:authSDGUserIpAddr,_A2:authSDGUserOnlineFlag,_A3:authSDGUserTimeLimit,_W:authSDGUserTimeUsed,_A4:authSDGUserVrf,_A5:authSDGUserRoleName,_A6:authSDGUserSecZoneName,_A7:authSDGUserSecZonePermissionType,_A8:authSDGUserSecZonePermissionList,_A9:authSDGUserOtherPermissionType,_X:authSDGUserTerminateCause,_AA:authSDGUserStatus,'qtechWebAuthMacUserTable':qtechWebAuthMacUserTable,'qtechWebAuthMacUserEntry':qtechWebAuthMacUserEntry,_f:qtechAuthMacUserMacAddr,'qtechAuthMacUserName':qtechAuthMacUserName,'qtechAuthMacUserTerminalId':qtechAuthMacUserTerminalId,'qtechWebAuthUserMIB':qtechWebAuthUserMIB,'qtechWebAuthUserMIBTable':qtechWebAuthUserMIBTable,'qtechWebAuthUserMIBEntry':qtechWebAuthUserMIBEntry,_g:qtechAuthUserMIBIpAddress,'qtechAuthUserMIBName':qtechAuthUserMIBName,'qtechAuthUserMIBAuthType':qtechAuthUserMIBAuthType,'qtechAuthUserMIBMacAddress':qtechAuthUserMIBMacAddress,'qtechAuthUserMIBVlanId':qtechAuthUserMIBVlanId,'qtechAuthUserMIBPortIndex':qtechAuthUserMIBPortIndex,'qtechAuthUserMIBTimeUsed':qtechAuthUserMIBTimeUsed,'qtechWebAuthMIBTraps':qtechWebAuthMIBTraps,_AT:qtechWebAuthUserLeave,_AU:qtechWebAuthUserExtLeave,_AV:qtechWebAuthSDGUserLeave,'qtechWebAuthWlanMgmt':qtechWebAuthWlanMgmt,'qtechWebAuthUserOper':qtechWebAuthUserOper,'qtechWebAuthMIBConformance':qtechWebAuthMIBConformance,'qtechWebAuthMIBCompliances':qtechWebAuthMIBCompliances,'qtechWebAuthMIBCompliance':qtechWebAuthMIBCompliance,'qtechWebAuthMIBGroups':qtechWebAuthMIBGroups,_AW:qtechWebAuthMIBGroup,_AX:qtechWebAuthTrapGroup,'qtechWebAuthMIBTrapsObjects':qtechWebAuthMIBTrapsObjects,_AB:qtechWebAuthApMac,_AC:qtechWebAuthApIp,_Y:qtechWebAuthStaMac,_Z:qtechWebAuthStaIp,_AD:qtechWebAuthStaIpv6,_a:qtechWebAuthStaOperType,_AE:qtechWebAuthStaApRadioId,_AF:qtechWebAuthStaApRadioType,_b:qtechWebAuthStaVlanId,_AG:qtechWebAuthStaWlanId,_AH:qtechWebAuthOperTime,_AI:qtechWebAuthStaAssoAuthMode,_AJ:qtechWebAuthStaNetAuthMode,_AK:qtechWebAuthStaRssi,_AL:qtechWebAuthStaSsid,_AM:qtechWebAuthStaLinkRate,_AN:qtechWebAuthStaCurChannel,_c:qtechWebAuthStaUsername,_AO:qtechWebAuthStaTerminalType,_d:qtechWebAuthStaTerminateCause,_AP:qtechWebAuthStaReplyMessage,_AQ:qtechWebAuthStaTerminalId,_AR:qtechWebAuthType,_AS:qtechWebAuthPortIndex})