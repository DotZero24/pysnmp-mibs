_Al='vrrpNotificationGroup'
_Ak='vrrpTrapGroup'
_Aj='vrrpStatsGroup'
_Ai='vrrpOperGroup'
_Ah='vrrpTrapProtoError'
_Ag='vrrpTrapAuthFailure'
_Af='vrrpStatisticsRefreshRate'
_Ae='vrrpStatisticsDiscontinuityTime'
_Ad='vrrpStatisticsRcvdInvalidAuthentications'
_Ac='vrrpStatisticsPacketLengthErrors'
_Ab='vrrpStatisticsAddressListErrors'
_Aa='vrrpStatisticsIpTtlErrors'
_AZ='vrrpStatisticsRcvdInvalidTypePkts'
_AY='vrrpStatisticsSentPriZeroPackets'
_AX='vrrpStatisticsRcvdPriZeroPackets'
_AW='vrrpStatisticsAdvIntervalErrors'
_AV='vrrpStatisticsRcvdAdvertisements'
_AU='vrrpStatisticsMasterTransitions'
_AT='vrrpAssociatedIpAddrRowStatus'
_AS='vrrpAssociatedStorageType'
_AR='vrrpOperationsPrimaryIpAddr'
_AQ='vrrpOperationsAddrCount'
_AP='vrrpOperationsRowStatus'
_AO='vrrpOperationsStorageType'
_AN='vrrpOperationsUpTime'
_AM='vrrpOperationsAcceptMode'
_AL='vrrpOperationsPreemptMode'
_AK='vrrpOperationsAdvInterval'
_AJ='vrrpOperationsPriority'
_AI='vrrpOperationsState'
_AH='vrrpOperationsVirtualMacAddr'
_AG='vrrpStatsPacketLengthErrors'
_AF='vrrpStatsAuthTypeMismatch'
_AE='vrrpStatsInvalidAuthType'
_AD='vrrpStatsAddressListErrors'
_AC='vrrpStatsInvalidTypePktsRcvd'
_AB='vrrpStatsPriorityZeroPktsSent'
_AA='vrrpStatsPriorityZeroPktsRcvd'
_A9='vrrpStatsIpTtlErrors'
_A8='vrrpStatsAuthFailures'
_A7='vrrpStatsAdvertiseIntervalErrors'
_A6='vrrpStatsAdvertiseRcvd'
_A5='vrrpStatsBecomeMaster'
_A4='vrrpAssoIpAddrRowStatus'
_A3='vrrpOperRowStatus'
_A2='vrrpOperProtocol'
_A1='vrrpOperVirtualRouterUpTime'
_A0='vrrpOperPreemptMode'
_z='vrrpOperAdvertisementInterval'
_y='vrrpOperAuthKey'
_x='vrrpOperAuthType'
_w='vrrpOperPrimaryIpAddr'
_v='vrrpOperMasterIpAddr'
_u='vrrpOperIpAddrCount'
_t='vrrpOperPriority'
_s='vrrpOperAdminState'
_r='vrrpOperState'
_q='vrrpOperVirtualMacAddr'
_p='vrrpNodeVersion'
_o='vrrpRouterStatisticsEntry'
_n='vrrpRouterStatsEntry'
_m='vrrpAssociatedIpAddr'
_l='vrrpAssoIpAddr'
_k='master'
_j='backup'
_i='initialize'
_h='TimeInterval'
_g='Unsigned32'
_f='IpAddress'
_e='InetAddress'
_d='OctetString'
_c='vrrpNotificationsGroup'
_b='vrrpTrapInfoGroup'
_a='vrrpStatisticsGroup'
_Z='vrrpOperationsGroup'
_Y='vrrpTrapNewMaster'
_X='vrrpTrapProtoErrReason'
_W='vrrpNewMasterReason'
_V='vrrpOperationsMasterIpAddr'
_U='vrrpTrapAuthErrorType'
_T='vrrpTrapPacketSrc'
_S='vrrpRouterVrIdErrors'
_R='vrrpRouterVersionErrors'
_Q='vrrpRouterChecksumErrors'
_P='vrrpNotificationCntl'
_O='vrrpOperationsVrId'
_N='vrrpOperationsInetAddrType'
_M='accessible-for-notify'
_L='vrrpOperVrId'
_K='StorageType'
_J='TruthValue'
_I='not-accessible'
_H='ifIndex'
_G='IF-MIB'
_F='Integer32'
_E='read-create'
_D='read-only'
_C='deprecated'
_B='current'
_A='VRRP-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_d,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_G,_H)
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB',_e,'InetAddressType')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso,mib_2=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,_f,'ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_g,'iso','mib-2')
DisplayString,MacAddress,PhysAddress,RowStatus,StorageType,TextualConvention,TimeInterval,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus',_K,'TextualConvention',_h,'TimeStamp',_J)
vrrpMIB=ModuleIdentity((1,3,6,1,2,1,68))
if mibBuilder.loadTexts:vrrpMIB.setRevisions(('2006-12-13 00:00','2000-03-03 00:00'))
class VrId(TextualConvention,Integer32):status=_B;displayHint='d';subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_VrrpNotifications_ObjectIdentity=ObjectIdentity
vrrpNotifications=_VrrpNotifications_ObjectIdentity((1,3,6,1,2,1,68,0))
_VrrpOperations_ObjectIdentity=ObjectIdentity
vrrpOperations=_VrrpOperations_ObjectIdentity((1,3,6,1,2,1,68,1))
_VrrpNodeVersion_Type=Integer32
_VrrpNodeVersion_Object=MibScalar
vrrpNodeVersion=_VrrpNodeVersion_Object((1,3,6,1,2,1,68,1,1),_VrrpNodeVersion_Type())
vrrpNodeVersion.setMaxAccess(_D)
if mibBuilder.loadTexts:vrrpNodeVersion.setStatus(_C)
class _VrrpNotificationCntl_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),('disabled',2)))
_VrrpNotificationCntl_Type.__name__=_F
_VrrpNotificationCntl_Object=MibScalar
vrrpNotificationCntl=_VrrpNotificationCntl_Object((1,3,6,1,2,1,68,1,2),_VrrpNotificationCntl_Type())
vrrpNotificationCntl.setMaxAccess('read-write')
if mibBuilder.loadTexts:vrrpNotificationCntl.setStatus(_B)
_VrrpOperTable_Object=MibTable
vrrpOperTable=_VrrpOperTable_Object((1,3,6,1,2,1,68,1,3))
if mibBuilder.loadTexts:vrrpOperTable.setStatus(_C)
_VrrpOperEntry_Object=MibTableRow
vrrpOperEntry=_VrrpOperEntry_Object((1,3,6,1,2,1,68,1,3,1))
vrrpOperEntry.setIndexNames((0,_G,_H),(0,_A,_L))
if mibBuilder.loadTexts:vrrpOperEntry.setStatus(_C)
_VrrpOperVrId_Type=VrId
_VrrpOperVrId_Object=MibTableColumn
vrrpOperVrId=_VrrpOperVrId_Object((1,3,6,1,2,1,68,1,3,1,1),_VrrpOperVrId_Type())
vrrpOperVrId.setMaxAccess(_I)
if mibBuilder.loadTexts:vrrpOperVrId.setStatus(_C)
_VrrpOperVirtualMacAddr_Type=MacAddress
_VrrpOperVirtualMacAddr_Object=MibTableColumn
vrrpOperVirtualMacAddr=_VrrpOperVirtualMacAddr_Object((1,3,6,1,2,1,68,1,3,1,2),_VrrpOperVirtualMacAddr_Type())
vrrpOperVirtualMacAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:vrrpOperVirtualMacAddr.setStatus(_C)
class _VrrpOperState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_i,1),(_j,2),(_k,3)))
_VrrpOperState_Type.__name__=_F
_VrrpOperState_Object=MibTableColumn
vrrpOperState=_VrrpOperState_Object((1,3,6,1,2,1,68,1,3,1,3),_VrrpOperState_Type())
vrrpOperState.setMaxAccess(_D)
if mibBuilder.loadTexts:vrrpOperState.setStatus(_C)
class _VrrpOperAdminState_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('up',1),('down',2)))
_VrrpOperAdminState_Type.__name__=_F
_VrrpOperAdminState_Object=MibTableColumn
vrrpOperAdminState=_VrrpOperAdminState_Object((1,3,6,1,2,1,68,1,3,1,4),_VrrpOperAdminState_Type())
vrrpOperAdminState.setMaxAccess(_E)
if mibBuilder.loadTexts:vrrpOperAdminState.setStatus(_C)
class _VrrpOperPriority_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_VrrpOperPriority_Type.__name__=_F
_VrrpOperPriority_Object=MibTableColumn
vrrpOperPriority=_VrrpOperPriority_Object((1,3,6,1,2,1,68,1,3,1,5),_VrrpOperPriority_Type())
vrrpOperPriority.setMaxAccess(_E)
if mibBuilder.loadTexts:vrrpOperPriority.setStatus(_C)
class _VrrpOperIpAddrCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_VrrpOperIpAddrCount_Type.__name__=_F
_VrrpOperIpAddrCount_Object=MibTableColumn
vrrpOperIpAddrCount=_VrrpOperIpAddrCount_Object((1,3,6,1,2,1,68,1,3,1,6),_VrrpOperIpAddrCount_Type())
vrrpOperIpAddrCount.setMaxAccess(_D)
if mibBuilder.loadTexts:vrrpOperIpAddrCount.setStatus(_C)
_VrrpOperMasterIpAddr_Type=IpAddress
_VrrpOperMasterIpAddr_Object=MibTableColumn
vrrpOperMasterIpAddr=_VrrpOperMasterIpAddr_Object((1,3,6,1,2,1,68,1,3,1,7),_VrrpOperMasterIpAddr_Type())
vrrpOperMasterIpAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:vrrpOperMasterIpAddr.setStatus(_C)
class _VrrpOperPrimaryIpAddr_Type(IpAddress):defaultHexValue='00000000'
_VrrpOperPrimaryIpAddr_Type.__name__=_f
_VrrpOperPrimaryIpAddr_Object=MibTableColumn
vrrpOperPrimaryIpAddr=_VrrpOperPrimaryIpAddr_Object((1,3,6,1,2,1,68,1,3,1,8),_VrrpOperPrimaryIpAddr_Type())
vrrpOperPrimaryIpAddr.setMaxAccess(_E)
if mibBuilder.loadTexts:vrrpOperPrimaryIpAddr.setStatus(_C)
class _VrrpOperAuthType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('noAuthentication',1),('simpleTextPassword',2),('ipAuthenticationHeader',3)))
_VrrpOperAuthType_Type.__name__=_F
_VrrpOperAuthType_Object=MibTableColumn
vrrpOperAuthType=_VrrpOperAuthType_Object((1,3,6,1,2,1,68,1,3,1,9),_VrrpOperAuthType_Type())
vrrpOperAuthType.setMaxAccess(_E)
if mibBuilder.loadTexts:vrrpOperAuthType.setStatus(_C)
class _VrrpOperAuthKey_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_VrrpOperAuthKey_Type.__name__=_d
_VrrpOperAuthKey_Object=MibTableColumn
vrrpOperAuthKey=_VrrpOperAuthKey_Object((1,3,6,1,2,1,68,1,3,1,10),_VrrpOperAuthKey_Type())
vrrpOperAuthKey.setMaxAccess(_E)
if mibBuilder.loadTexts:vrrpOperAuthKey.setStatus(_C)
class _VrrpOperAdvertisementInterval_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_VrrpOperAdvertisementInterval_Type.__name__=_F
_VrrpOperAdvertisementInterval_Object=MibTableColumn
vrrpOperAdvertisementInterval=_VrrpOperAdvertisementInterval_Object((1,3,6,1,2,1,68,1,3,1,11),_VrrpOperAdvertisementInterval_Type())
vrrpOperAdvertisementInterval.setMaxAccess(_E)
if mibBuilder.loadTexts:vrrpOperAdvertisementInterval.setStatus(_C)
if mibBuilder.loadTexts:vrrpOperAdvertisementInterval.setUnits('seconds')
class _VrrpOperPreemptMode_Type(TruthValue):defaultValue=1
_VrrpOperPreemptMode_Type.__name__=_J
_VrrpOperPreemptMode_Object=MibTableColumn
vrrpOperPreemptMode=_VrrpOperPreemptMode_Object((1,3,6,1,2,1,68,1,3,1,12),_VrrpOperPreemptMode_Type())
vrrpOperPreemptMode.setMaxAccess(_E)
if mibBuilder.loadTexts:vrrpOperPreemptMode.setStatus(_C)
_VrrpOperVirtualRouterUpTime_Type=TimeStamp
_VrrpOperVirtualRouterUpTime_Object=MibTableColumn
vrrpOperVirtualRouterUpTime=_VrrpOperVirtualRouterUpTime_Object((1,3,6,1,2,1,68,1,3,1,13),_VrrpOperVirtualRouterUpTime_Type())
vrrpOperVirtualRouterUpTime.setMaxAccess(_D)
if mibBuilder.loadTexts:vrrpOperVirtualRouterUpTime.setStatus(_C)
class _VrrpOperProtocol_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('ip',1),('bridge',2),('decnet',3),('other',4)))
_VrrpOperProtocol_Type.__name__=_F
_VrrpOperProtocol_Object=MibTableColumn
vrrpOperProtocol=_VrrpOperProtocol_Object((1,3,6,1,2,1,68,1,3,1,14),_VrrpOperProtocol_Type())
vrrpOperProtocol.setMaxAccess(_E)
if mibBuilder.loadTexts:vrrpOperProtocol.setStatus(_C)
_VrrpOperRowStatus_Type=RowStatus
_VrrpOperRowStatus_Object=MibTableColumn
vrrpOperRowStatus=_VrrpOperRowStatus_Object((1,3,6,1,2,1,68,1,3,1,15),_VrrpOperRowStatus_Type())
vrrpOperRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:vrrpOperRowStatus.setStatus(_C)
_VrrpAssoIpAddrTable_Object=MibTable
vrrpAssoIpAddrTable=_VrrpAssoIpAddrTable_Object((1,3,6,1,2,1,68,1,4))
if mibBuilder.loadTexts:vrrpAssoIpAddrTable.setStatus(_C)
_VrrpAssoIpAddrEntry_Object=MibTableRow
vrrpAssoIpAddrEntry=_VrrpAssoIpAddrEntry_Object((1,3,6,1,2,1,68,1,4,1))
vrrpAssoIpAddrEntry.setIndexNames((0,_G,_H),(0,_A,_L),(0,_A,_l))
if mibBuilder.loadTexts:vrrpAssoIpAddrEntry.setStatus(_C)
_VrrpAssoIpAddr_Type=IpAddress
_VrrpAssoIpAddr_Object=MibTableColumn
vrrpAssoIpAddr=_VrrpAssoIpAddr_Object((1,3,6,1,2,1,68,1,4,1,1),_VrrpAssoIpAddr_Type())
vrrpAssoIpAddr.setMaxAccess(_I)
if mibBuilder.loadTexts:vrrpAssoIpAddr.setStatus(_C)
_VrrpAssoIpAddrRowStatus_Type=RowStatus
_VrrpAssoIpAddrRowStatus_Object=MibTableColumn
vrrpAssoIpAddrRowStatus=_VrrpAssoIpAddrRowStatus_Object((1,3,6,1,2,1,68,1,4,1,2),_VrrpAssoIpAddrRowStatus_Type())
vrrpAssoIpAddrRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:vrrpAssoIpAddrRowStatus.setStatus(_C)
_VrrpTrapPacketSrc_Type=IpAddress
_VrrpTrapPacketSrc_Object=MibScalar
vrrpTrapPacketSrc=_VrrpTrapPacketSrc_Object((1,3,6,1,2,1,68,1,5),_VrrpTrapPacketSrc_Type())
vrrpTrapPacketSrc.setMaxAccess(_M)
if mibBuilder.loadTexts:vrrpTrapPacketSrc.setStatus(_C)
class _VrrpTrapAuthErrorType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('invalidAuthType',1),('authTypeMismatch',2),('authFailure',3)))
_VrrpTrapAuthErrorType_Type.__name__=_F
_VrrpTrapAuthErrorType_Object=MibScalar
vrrpTrapAuthErrorType=_VrrpTrapAuthErrorType_Object((1,3,6,1,2,1,68,1,6),_VrrpTrapAuthErrorType_Type())
vrrpTrapAuthErrorType.setMaxAccess(_M)
if mibBuilder.loadTexts:vrrpTrapAuthErrorType.setStatus(_C)
_VrrpOperationsTable_Object=MibTable
vrrpOperationsTable=_VrrpOperationsTable_Object((1,3,6,1,2,1,68,1,7))
if mibBuilder.loadTexts:vrrpOperationsTable.setStatus(_B)
_VrrpOperationsEntry_Object=MibTableRow
vrrpOperationsEntry=_VrrpOperationsEntry_Object((1,3,6,1,2,1,68,1,7,1))
vrrpOperationsEntry.setIndexNames((0,_A,_N),(0,_A,_O),(0,_G,_H))
if mibBuilder.loadTexts:vrrpOperationsEntry.setStatus(_B)
_VrrpOperationsInetAddrType_Type=InetAddressType
_VrrpOperationsInetAddrType_Object=MibTableColumn
vrrpOperationsInetAddrType=_VrrpOperationsInetAddrType_Object((1,3,6,1,2,1,68,1,7,1,1),_VrrpOperationsInetAddrType_Type())
vrrpOperationsInetAddrType.setMaxAccess(_I)
if mibBuilder.loadTexts:vrrpOperationsInetAddrType.setStatus(_B)
_VrrpOperationsVrId_Type=VrId
_VrrpOperationsVrId_Object=MibTableColumn
vrrpOperationsVrId=_VrrpOperationsVrId_Object((1,3,6,1,2,1,68,1,7,1,2),_VrrpOperationsVrId_Type())
vrrpOperationsVrId.setMaxAccess(_I)
if mibBuilder.loadTexts:vrrpOperationsVrId.setStatus(_B)
_VrrpOperationsVirtualMacAddr_Type=MacAddress
_VrrpOperationsVirtualMacAddr_Object=MibTableColumn
vrrpOperationsVirtualMacAddr=_VrrpOperationsVirtualMacAddr_Object((1,3,6,1,2,1,68,1,7,1,3),_VrrpOperationsVirtualMacAddr_Type())
vrrpOperationsVirtualMacAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:vrrpOperationsVirtualMacAddr.setStatus(_B)
class _VrrpOperationsState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_i,1),(_j,2),(_k,3)))
_VrrpOperationsState_Type.__name__=_F
_VrrpOperationsState_Object=MibTableColumn
vrrpOperationsState=_VrrpOperationsState_Object((1,3,6,1,2,1,68,1,7,1,4),_VrrpOperationsState_Type())
vrrpOperationsState.setMaxAccess(_D)
if mibBuilder.loadTexts:vrrpOperationsState.setStatus(_B)
class _VrrpOperationsPriority_Type(Unsigned32):defaultValue=100;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_VrrpOperationsPriority_Type.__name__=_g
_VrrpOperationsPriority_Object=MibTableColumn
vrrpOperationsPriority=_VrrpOperationsPriority_Object((1,3,6,1,2,1,68,1,7,1,5),_VrrpOperationsPriority_Type())
vrrpOperationsPriority.setMaxAccess(_E)
if mibBuilder.loadTexts:vrrpOperationsPriority.setStatus(_B)
class _VrrpOperationsAddrCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_VrrpOperationsAddrCount_Type.__name__=_F
_VrrpOperationsAddrCount_Object=MibTableColumn
vrrpOperationsAddrCount=_VrrpOperationsAddrCount_Object((1,3,6,1,2,1,68,1,7,1,6),_VrrpOperationsAddrCount_Type())
vrrpOperationsAddrCount.setMaxAccess(_D)
if mibBuilder.loadTexts:vrrpOperationsAddrCount.setStatus(_B)
_VrrpOperationsMasterIpAddr_Type=InetAddress
_VrrpOperationsMasterIpAddr_Object=MibTableColumn
vrrpOperationsMasterIpAddr=_VrrpOperationsMasterIpAddr_Object((1,3,6,1,2,1,68,1,7,1,7),_VrrpOperationsMasterIpAddr_Type())
vrrpOperationsMasterIpAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:vrrpOperationsMasterIpAddr.setStatus(_B)
_VrrpOperationsPrimaryIpAddr_Type=InetAddress
_VrrpOperationsPrimaryIpAddr_Object=MibTableColumn
vrrpOperationsPrimaryIpAddr=_VrrpOperationsPrimaryIpAddr_Object((1,3,6,1,2,1,68,1,7,1,8),_VrrpOperationsPrimaryIpAddr_Type())
vrrpOperationsPrimaryIpAddr.setMaxAccess(_E)
if mibBuilder.loadTexts:vrrpOperationsPrimaryIpAddr.setStatus(_B)
class _VrrpOperationsAdvInterval_Type(TimeInterval):defaultValue=100;subtypeSpec=TimeInterval.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4096))
_VrrpOperationsAdvInterval_Type.__name__=_h
_VrrpOperationsAdvInterval_Object=MibTableColumn
vrrpOperationsAdvInterval=_VrrpOperationsAdvInterval_Object((1,3,6,1,2,1,68,1,7,1,9),_VrrpOperationsAdvInterval_Type())
vrrpOperationsAdvInterval.setMaxAccess(_E)
if mibBuilder.loadTexts:vrrpOperationsAdvInterval.setStatus(_B)
if mibBuilder.loadTexts:vrrpOperationsAdvInterval.setUnits('centiseconds')
class _VrrpOperationsPreemptMode_Type(TruthValue):defaultValue=1
_VrrpOperationsPreemptMode_Type.__name__=_J
_VrrpOperationsPreemptMode_Object=MibTableColumn
vrrpOperationsPreemptMode=_VrrpOperationsPreemptMode_Object((1,3,6,1,2,1,68,1,7,1,10),_VrrpOperationsPreemptMode_Type())
vrrpOperationsPreemptMode.setMaxAccess(_E)
if mibBuilder.loadTexts:vrrpOperationsPreemptMode.setStatus(_B)
class _VrrpOperationsAcceptMode_Type(TruthValue):defaultValue=2
_VrrpOperationsAcceptMode_Type.__name__=_J
_VrrpOperationsAcceptMode_Object=MibTableColumn
vrrpOperationsAcceptMode=_VrrpOperationsAcceptMode_Object((1,3,6,1,2,1,68,1,7,1,11),_VrrpOperationsAcceptMode_Type())
vrrpOperationsAcceptMode.setMaxAccess(_E)
if mibBuilder.loadTexts:vrrpOperationsAcceptMode.setStatus(_B)
_VrrpOperationsUpTime_Type=TimeStamp
_VrrpOperationsUpTime_Object=MibTableColumn
vrrpOperationsUpTime=_VrrpOperationsUpTime_Object((1,3,6,1,2,1,68,1,7,1,12),_VrrpOperationsUpTime_Type())
vrrpOperationsUpTime.setMaxAccess(_D)
if mibBuilder.loadTexts:vrrpOperationsUpTime.setStatus(_B)
class _VrrpOperationsStorageType_Type(StorageType):defaultValue=3
_VrrpOperationsStorageType_Type.__name__=_K
_VrrpOperationsStorageType_Object=MibTableColumn
vrrpOperationsStorageType=_VrrpOperationsStorageType_Object((1,3,6,1,2,1,68,1,7,1,13),_VrrpOperationsStorageType_Type())
vrrpOperationsStorageType.setMaxAccess(_E)
if mibBuilder.loadTexts:vrrpOperationsStorageType.setStatus(_B)
_VrrpOperationsRowStatus_Type=RowStatus
_VrrpOperationsRowStatus_Object=MibTableColumn
vrrpOperationsRowStatus=_VrrpOperationsRowStatus_Object((1,3,6,1,2,1,68,1,7,1,14),_VrrpOperationsRowStatus_Type())
vrrpOperationsRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:vrrpOperationsRowStatus.setStatus(_B)
_VrrpAssociatedIpAddrTable_Object=MibTable
vrrpAssociatedIpAddrTable=_VrrpAssociatedIpAddrTable_Object((1,3,6,1,2,1,68,1,8))
if mibBuilder.loadTexts:vrrpAssociatedIpAddrTable.setStatus(_B)
_VrrpAssociatedIpAddrEntry_Object=MibTableRow
vrrpAssociatedIpAddrEntry=_VrrpAssociatedIpAddrEntry_Object((1,3,6,1,2,1,68,1,8,1))
vrrpAssociatedIpAddrEntry.setIndexNames((0,_A,_N),(0,_A,_O),(0,_G,_H),(0,_A,_m))
if mibBuilder.loadTexts:vrrpAssociatedIpAddrEntry.setStatus(_B)
class _VrrpAssociatedIpAddr_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,0),ValueSizeConstraint(4,4),ValueSizeConstraint(16,16))
_VrrpAssociatedIpAddr_Type.__name__=_e
_VrrpAssociatedIpAddr_Object=MibTableColumn
vrrpAssociatedIpAddr=_VrrpAssociatedIpAddr_Object((1,3,6,1,2,1,68,1,8,1,1),_VrrpAssociatedIpAddr_Type())
vrrpAssociatedIpAddr.setMaxAccess(_I)
if mibBuilder.loadTexts:vrrpAssociatedIpAddr.setStatus(_B)
class _VrrpAssociatedStorageType_Type(StorageType):defaultValue=3
_VrrpAssociatedStorageType_Type.__name__=_K
_VrrpAssociatedStorageType_Object=MibTableColumn
vrrpAssociatedStorageType=_VrrpAssociatedStorageType_Object((1,3,6,1,2,1,68,1,8,1,2),_VrrpAssociatedStorageType_Type())
vrrpAssociatedStorageType.setMaxAccess(_E)
if mibBuilder.loadTexts:vrrpAssociatedStorageType.setStatus(_B)
_VrrpAssociatedIpAddrRowStatus_Type=RowStatus
_VrrpAssociatedIpAddrRowStatus_Object=MibTableColumn
vrrpAssociatedIpAddrRowStatus=_VrrpAssociatedIpAddrRowStatus_Object((1,3,6,1,2,1,68,1,8,1,3),_VrrpAssociatedIpAddrRowStatus_Type())
vrrpAssociatedIpAddrRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:vrrpAssociatedIpAddrRowStatus.setStatus(_B)
class _VrrpNewMasterReason_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('notmaster',0),('priority',1),('preempted',2),('masterNoResponse',3)))
_VrrpNewMasterReason_Type.__name__=_F
_VrrpNewMasterReason_Object=MibScalar
vrrpNewMasterReason=_VrrpNewMasterReason_Object((1,3,6,1,2,1,68,1,9),_VrrpNewMasterReason_Type())
vrrpNewMasterReason.setMaxAccess(_D)
if mibBuilder.loadTexts:vrrpNewMasterReason.setStatus(_B)
class _VrrpTrapProtoErrReason_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('hopLimitError',0),('versionError',1),('checksumError',2),('vridError',3)))
_VrrpTrapProtoErrReason_Type.__name__=_F
_VrrpTrapProtoErrReason_Object=MibScalar
vrrpTrapProtoErrReason=_VrrpTrapProtoErrReason_Object((1,3,6,1,2,1,68,1,10),_VrrpTrapProtoErrReason_Type())
vrrpTrapProtoErrReason.setMaxAccess(_M)
if mibBuilder.loadTexts:vrrpTrapProtoErrReason.setStatus(_B)
_VrrpStatistics_ObjectIdentity=ObjectIdentity
vrrpStatistics=_VrrpStatistics_ObjectIdentity((1,3,6,1,2,1,68,2))
_VrrpRouterChecksumErrors_Type=Counter32
_VrrpRouterChecksumErrors_Object=MibScalar
vrrpRouterChecksumErrors=_VrrpRouterChecksumErrors_Object((1,3,6,1,2,1,68,2,1),_VrrpRouterChecksumErrors_Type())
vrrpRouterChecksumErrors.setMaxAccess(_D)
if mibBuilder.loadTexts:vrrpRouterChecksumErrors.setStatus(_B)
_VrrpRouterVersionErrors_Type=Counter32
_VrrpRouterVersionErrors_Object=MibScalar
vrrpRouterVersionErrors=_VrrpRouterVersionErrors_Object((1,3,6,1,2,1,68,2,2),_VrrpRouterVersionErrors_Type())
vrrpRouterVersionErrors.setMaxAccess(_D)
if mibBuilder.loadTexts:vrrpRouterVersionErrors.setStatus(_B)
_VrrpRouterVrIdErrors_Type=Counter32
_VrrpRouterVrIdErrors_Object=MibScalar
vrrpRouterVrIdErrors=_VrrpRouterVrIdErrors_Object((1,3,6,1,2,1,68,2,3),_VrrpRouterVrIdErrors_Type())
vrrpRouterVrIdErrors.setMaxAccess(_D)
if mibBuilder.loadTexts:vrrpRouterVrIdErrors.setStatus(_B)
_VrrpRouterStatsTable_Object=MibTable
vrrpRouterStatsTable=_VrrpRouterStatsTable_Object((1,3,6,1,2,1,68,2,4))
if mibBuilder.loadTexts:vrrpRouterStatsTable.setStatus(_C)
_VrrpRouterStatsEntry_Object=MibTableRow
vrrpRouterStatsEntry=_VrrpRouterStatsEntry_Object((1,3,6,1,2,1,68,2,4,1))
if mibBuilder.loadTexts:vrrpRouterStatsEntry.setStatus(_C)
_VrrpStatsBecomeMaster_Type=Counter32
_VrrpStatsBecomeMaster_Object=MibTableColumn
vrrpStatsBecomeMaster=_VrrpStatsBecomeMaster_Object((1,3,6,1,2,1,68,2,4,1,1),_VrrpStatsBecomeMaster_Type())
vrrpStatsBecomeMaster.setMaxAccess(_D)
if mibBuilder.loadTexts:vrrpStatsBecomeMaster.setStatus(_C)
_VrrpStatsAdvertiseRcvd_Type=Counter32
_VrrpStatsAdvertiseRcvd_Object=MibTableColumn
vrrpStatsAdvertiseRcvd=_VrrpStatsAdvertiseRcvd_Object((1,3,6,1,2,1,68,2,4,1,2),_VrrpStatsAdvertiseRcvd_Type())
vrrpStatsAdvertiseRcvd.setMaxAccess(_D)
if mibBuilder.loadTexts:vrrpStatsAdvertiseRcvd.setStatus(_C)
_VrrpStatsAdvertiseIntervalErrors_Type=Counter32
_VrrpStatsAdvertiseIntervalErrors_Object=MibTableColumn
vrrpStatsAdvertiseIntervalErrors=_VrrpStatsAdvertiseIntervalErrors_Object((1,3,6,1,2,1,68,2,4,1,3),_VrrpStatsAdvertiseIntervalErrors_Type())
vrrpStatsAdvertiseIntervalErrors.setMaxAccess(_D)
if mibBuilder.loadTexts:vrrpStatsAdvertiseIntervalErrors.setStatus(_C)
_VrrpStatsAuthFailures_Type=Counter32
_VrrpStatsAuthFailures_Object=MibTableColumn
vrrpStatsAuthFailures=_VrrpStatsAuthFailures_Object((1,3,6,1,2,1,68,2,4,1,4),_VrrpStatsAuthFailures_Type())
vrrpStatsAuthFailures.setMaxAccess(_D)
if mibBuilder.loadTexts:vrrpStatsAuthFailures.setStatus(_C)
_VrrpStatsIpTtlErrors_Type=Counter32
_VrrpStatsIpTtlErrors_Object=MibTableColumn
vrrpStatsIpTtlErrors=_VrrpStatsIpTtlErrors_Object((1,3,6,1,2,1,68,2,4,1,5),_VrrpStatsIpTtlErrors_Type())
vrrpStatsIpTtlErrors.setMaxAccess(_D)
if mibBuilder.loadTexts:vrrpStatsIpTtlErrors.setStatus(_C)
_VrrpStatsPriorityZeroPktsRcvd_Type=Counter32
_VrrpStatsPriorityZeroPktsRcvd_Object=MibTableColumn
vrrpStatsPriorityZeroPktsRcvd=_VrrpStatsPriorityZeroPktsRcvd_Object((1,3,6,1,2,1,68,2,4,1,6),_VrrpStatsPriorityZeroPktsRcvd_Type())
vrrpStatsPriorityZeroPktsRcvd.setMaxAccess(_D)
if mibBuilder.loadTexts:vrrpStatsPriorityZeroPktsRcvd.setStatus(_C)
_VrrpStatsPriorityZeroPktsSent_Type=Counter32
_VrrpStatsPriorityZeroPktsSent_Object=MibTableColumn
vrrpStatsPriorityZeroPktsSent=_VrrpStatsPriorityZeroPktsSent_Object((1,3,6,1,2,1,68,2,4,1,7),_VrrpStatsPriorityZeroPktsSent_Type())
vrrpStatsPriorityZeroPktsSent.setMaxAccess(_D)
if mibBuilder.loadTexts:vrrpStatsPriorityZeroPktsSent.setStatus(_C)
_VrrpStatsInvalidTypePktsRcvd_Type=Counter32
_VrrpStatsInvalidTypePktsRcvd_Object=MibTableColumn
vrrpStatsInvalidTypePktsRcvd=_VrrpStatsInvalidTypePktsRcvd_Object((1,3,6,1,2,1,68,2,4,1,8),_VrrpStatsInvalidTypePktsRcvd_Type())
vrrpStatsInvalidTypePktsRcvd.setMaxAccess(_D)
if mibBuilder.loadTexts:vrrpStatsInvalidTypePktsRcvd.setStatus(_C)
_VrrpStatsAddressListErrors_Type=Counter32
_VrrpStatsAddressListErrors_Object=MibTableColumn
vrrpStatsAddressListErrors=_VrrpStatsAddressListErrors_Object((1,3,6,1,2,1,68,2,4,1,9),_VrrpStatsAddressListErrors_Type())
vrrpStatsAddressListErrors.setMaxAccess(_D)
if mibBuilder.loadTexts:vrrpStatsAddressListErrors.setStatus(_C)
_VrrpStatsInvalidAuthType_Type=Counter32
_VrrpStatsInvalidAuthType_Object=MibTableColumn
vrrpStatsInvalidAuthType=_VrrpStatsInvalidAuthType_Object((1,3,6,1,2,1,68,2,4,1,10),_VrrpStatsInvalidAuthType_Type())
vrrpStatsInvalidAuthType.setMaxAccess(_D)
if mibBuilder.loadTexts:vrrpStatsInvalidAuthType.setStatus(_C)
_VrrpStatsAuthTypeMismatch_Type=Counter32
_VrrpStatsAuthTypeMismatch_Object=MibTableColumn
vrrpStatsAuthTypeMismatch=_VrrpStatsAuthTypeMismatch_Object((1,3,6,1,2,1,68,2,4,1,11),_VrrpStatsAuthTypeMismatch_Type())
vrrpStatsAuthTypeMismatch.setMaxAccess(_D)
if mibBuilder.loadTexts:vrrpStatsAuthTypeMismatch.setStatus(_C)
_VrrpStatsPacketLengthErrors_Type=Counter32
_VrrpStatsPacketLengthErrors_Object=MibTableColumn
vrrpStatsPacketLengthErrors=_VrrpStatsPacketLengthErrors_Object((1,3,6,1,2,1,68,2,4,1,12),_VrrpStatsPacketLengthErrors_Type())
vrrpStatsPacketLengthErrors.setMaxAccess(_D)
if mibBuilder.loadTexts:vrrpStatsPacketLengthErrors.setStatus(_C)
_VrrpRouterStatisticsTable_Object=MibTable
vrrpRouterStatisticsTable=_VrrpRouterStatisticsTable_Object((1,3,6,1,2,1,68,2,5))
if mibBuilder.loadTexts:vrrpRouterStatisticsTable.setStatus(_B)
_VrrpRouterStatisticsEntry_Object=MibTableRow
vrrpRouterStatisticsEntry=_VrrpRouterStatisticsEntry_Object((1,3,6,1,2,1,68,2,5,1))
if mibBuilder.loadTexts:vrrpRouterStatisticsEntry.setStatus(_B)
_VrrpStatisticsMasterTransitions_Type=Counter32
_VrrpStatisticsMasterTransitions_Object=MibTableColumn
vrrpStatisticsMasterTransitions=_VrrpStatisticsMasterTransitions_Object((1,3,6,1,2,1,68,2,5,1,1),_VrrpStatisticsMasterTransitions_Type())
vrrpStatisticsMasterTransitions.setMaxAccess(_D)
if mibBuilder.loadTexts:vrrpStatisticsMasterTransitions.setStatus(_B)
_VrrpStatisticsRcvdAdvertisements_Type=Counter32
_VrrpStatisticsRcvdAdvertisements_Object=MibTableColumn
vrrpStatisticsRcvdAdvertisements=_VrrpStatisticsRcvdAdvertisements_Object((1,3,6,1,2,1,68,2,5,1,2),_VrrpStatisticsRcvdAdvertisements_Type())
vrrpStatisticsRcvdAdvertisements.setMaxAccess(_D)
if mibBuilder.loadTexts:vrrpStatisticsRcvdAdvertisements.setStatus(_B)
_VrrpStatisticsAdvIntervalErrors_Type=Counter32
_VrrpStatisticsAdvIntervalErrors_Object=MibTableColumn
vrrpStatisticsAdvIntervalErrors=_VrrpStatisticsAdvIntervalErrors_Object((1,3,6,1,2,1,68,2,5,1,3),_VrrpStatisticsAdvIntervalErrors_Type())
vrrpStatisticsAdvIntervalErrors.setMaxAccess(_D)
if mibBuilder.loadTexts:vrrpStatisticsAdvIntervalErrors.setStatus(_B)
_VrrpStatisticsIpTtlErrors_Type=Counter32
_VrrpStatisticsIpTtlErrors_Object=MibTableColumn
vrrpStatisticsIpTtlErrors=_VrrpStatisticsIpTtlErrors_Object((1,3,6,1,2,1,68,2,5,1,4),_VrrpStatisticsIpTtlErrors_Type())
vrrpStatisticsIpTtlErrors.setMaxAccess(_D)
if mibBuilder.loadTexts:vrrpStatisticsIpTtlErrors.setStatus(_B)
_VrrpStatisticsRcvdPriZeroPackets_Type=Counter32
_VrrpStatisticsRcvdPriZeroPackets_Object=MibTableColumn
vrrpStatisticsRcvdPriZeroPackets=_VrrpStatisticsRcvdPriZeroPackets_Object((1,3,6,1,2,1,68,2,5,1,5),_VrrpStatisticsRcvdPriZeroPackets_Type())
vrrpStatisticsRcvdPriZeroPackets.setMaxAccess(_D)
if mibBuilder.loadTexts:vrrpStatisticsRcvdPriZeroPackets.setStatus(_B)
_VrrpStatisticsSentPriZeroPackets_Type=Counter32
_VrrpStatisticsSentPriZeroPackets_Object=MibTableColumn
vrrpStatisticsSentPriZeroPackets=_VrrpStatisticsSentPriZeroPackets_Object((1,3,6,1,2,1,68,2,5,1,6),_VrrpStatisticsSentPriZeroPackets_Type())
vrrpStatisticsSentPriZeroPackets.setMaxAccess(_D)
if mibBuilder.loadTexts:vrrpStatisticsSentPriZeroPackets.setStatus(_B)
_VrrpStatisticsRcvdInvalidTypePkts_Type=Counter32
_VrrpStatisticsRcvdInvalidTypePkts_Object=MibTableColumn
vrrpStatisticsRcvdInvalidTypePkts=_VrrpStatisticsRcvdInvalidTypePkts_Object((1,3,6,1,2,1,68,2,5,1,7),_VrrpStatisticsRcvdInvalidTypePkts_Type())
vrrpStatisticsRcvdInvalidTypePkts.setMaxAccess(_D)
if mibBuilder.loadTexts:vrrpStatisticsRcvdInvalidTypePkts.setStatus(_B)
_VrrpStatisticsAddressListErrors_Type=Counter32
_VrrpStatisticsAddressListErrors_Object=MibTableColumn
vrrpStatisticsAddressListErrors=_VrrpStatisticsAddressListErrors_Object((1,3,6,1,2,1,68,2,5,1,8),_VrrpStatisticsAddressListErrors_Type())
vrrpStatisticsAddressListErrors.setMaxAccess(_D)
if mibBuilder.loadTexts:vrrpStatisticsAddressListErrors.setStatus(_B)
_VrrpStatisticsPacketLengthErrors_Type=Counter32
_VrrpStatisticsPacketLengthErrors_Object=MibTableColumn
vrrpStatisticsPacketLengthErrors=_VrrpStatisticsPacketLengthErrors_Object((1,3,6,1,2,1,68,2,5,1,9),_VrrpStatisticsPacketLengthErrors_Type())
vrrpStatisticsPacketLengthErrors.setMaxAccess(_D)
if mibBuilder.loadTexts:vrrpStatisticsPacketLengthErrors.setStatus(_B)
_VrrpStatisticsRcvdInvalidAuthentications_Type=Counter32
_VrrpStatisticsRcvdInvalidAuthentications_Object=MibTableColumn
vrrpStatisticsRcvdInvalidAuthentications=_VrrpStatisticsRcvdInvalidAuthentications_Object((1,3,6,1,2,1,68,2,5,1,10),_VrrpStatisticsRcvdInvalidAuthentications_Type())
vrrpStatisticsRcvdInvalidAuthentications.setMaxAccess(_D)
if mibBuilder.loadTexts:vrrpStatisticsRcvdInvalidAuthentications.setStatus(_B)
_VrrpStatisticsDiscontinuityTime_Type=TimeStamp
_VrrpStatisticsDiscontinuityTime_Object=MibTableColumn
vrrpStatisticsDiscontinuityTime=_VrrpStatisticsDiscontinuityTime_Object((1,3,6,1,2,1,68,2,5,1,11),_VrrpStatisticsDiscontinuityTime_Type())
vrrpStatisticsDiscontinuityTime.setMaxAccess(_D)
if mibBuilder.loadTexts:vrrpStatisticsDiscontinuityTime.setStatus(_B)
_VrrpStatisticsRefreshRate_Type=Unsigned32
_VrrpStatisticsRefreshRate_Object=MibTableColumn
vrrpStatisticsRefreshRate=_VrrpStatisticsRefreshRate_Object((1,3,6,1,2,1,68,2,5,1,12),_VrrpStatisticsRefreshRate_Type())
vrrpStatisticsRefreshRate.setMaxAccess(_D)
if mibBuilder.loadTexts:vrrpStatisticsRefreshRate.setStatus(_B)
if mibBuilder.loadTexts:vrrpStatisticsRefreshRate.setUnits('milli-seconds')
_VrrpConformance_ObjectIdentity=ObjectIdentity
vrrpConformance=_VrrpConformance_ObjectIdentity((1,3,6,1,2,1,68,3))
_VrrpMIBCompliances_ObjectIdentity=ObjectIdentity
vrrpMIBCompliances=_VrrpMIBCompliances_ObjectIdentity((1,3,6,1,2,1,68,3,1))
_VrrpMIBGroups_ObjectIdentity=ObjectIdentity
vrrpMIBGroups=_VrrpMIBGroups_ObjectIdentity((1,3,6,1,2,1,68,3,2))
vrrpOperEntry.registerAugmentions((_A,_n))
vrrpRouterStatsEntry.setIndexNames(*vrrpOperEntry.getIndexNames())
vrrpOperationsEntry.registerAugmentions((_A,_o))
vrrpRouterStatisticsEntry.setIndexNames(*vrrpOperationsEntry.getIndexNames())
vrrpOperGroup=ObjectGroup((1,3,6,1,2,1,68,3,2,1))
vrrpOperGroup.setObjects(*((_A,_p),(_A,_P),(_A,_q),(_A,_r),(_A,_s),(_A,_t),(_A,_u),(_A,_v),(_A,_w),(_A,_x),(_A,_y),(_A,_z),(_A,_A0),(_A,_A1),(_A,_A2),(_A,_A3),(_A,_A4)))
if mibBuilder.loadTexts:vrrpOperGroup.setStatus(_C)
vrrpStatsGroup=ObjectGroup((1,3,6,1,2,1,68,3,2,2))
vrrpStatsGroup.setObjects(*((_A,_Q),(_A,_R),(_A,_S),(_A,_A5),(_A,_A6),(_A,_A7),(_A,_A8),(_A,_A9),(_A,_AA),(_A,_AB),(_A,_AC),(_A,_AD),(_A,_AE),(_A,_AF),(_A,_AG)))
if mibBuilder.loadTexts:vrrpStatsGroup.setStatus(_C)
vrrpTrapGroup=ObjectGroup((1,3,6,1,2,1,68,3,2,3))
vrrpTrapGroup.setObjects(*((_A,_T),(_A,_U)))
if mibBuilder.loadTexts:vrrpTrapGroup.setStatus(_C)
vrrpOperationsGroup=ObjectGroup((1,3,6,1,2,1,68,3,2,5))
vrrpOperationsGroup.setObjects(*((_A,_P),(_A,_AH),(_A,_AI),(_A,_AJ),(_A,_V),(_A,_AK),(_A,_AL),(_A,_AM),(_A,_AN),(_A,_AO),(_A,_AP),(_A,_AQ),(_A,_AR),(_A,_AS),(_A,_AT)))
if mibBuilder.loadTexts:vrrpOperationsGroup.setStatus(_B)
vrrpStatisticsGroup=ObjectGroup((1,3,6,1,2,1,68,3,2,6))
vrrpStatisticsGroup.setObjects(*((_A,_Q),(_A,_R),(_A,_S),(_A,_AU),(_A,_AV),(_A,_AW),(_A,_AX),(_A,_AY),(_A,_AZ),(_A,_Aa),(_A,_Ab),(_A,_Ac),(_A,_Ad),(_A,_Ae),(_A,_Af)))
if mibBuilder.loadTexts:vrrpStatisticsGroup.setStatus(_B)
vrrpTrapInfoGroup=ObjectGroup((1,3,6,1,2,1,68,3,2,7))
vrrpTrapInfoGroup.setObjects(*((_A,_W),(_A,_X)))
if mibBuilder.loadTexts:vrrpTrapInfoGroup.setStatus(_B)
vrrpTrapNewMaster=NotificationType((1,3,6,1,2,1,68,0,1))
vrrpTrapNewMaster.setObjects(*((_A,_V),(_A,_W)))
if mibBuilder.loadTexts:vrrpTrapNewMaster.setStatus(_B)
vrrpTrapAuthFailure=NotificationType((1,3,6,1,2,1,68,0,2))
vrrpTrapAuthFailure.setObjects(*((_A,_T),(_A,_U)))
if mibBuilder.loadTexts:vrrpTrapAuthFailure.setStatus(_C)
vrrpTrapProtoError=NotificationType((1,3,6,1,2,1,68,0,3))
vrrpTrapProtoError.setObjects((_A,_X))
if mibBuilder.loadTexts:vrrpTrapProtoError.setStatus(_B)
vrrpNotificationGroup=NotificationGroup((1,3,6,1,2,1,68,3,2,4))
vrrpNotificationGroup.setObjects(*((_A,_Y),(_A,_Ag)))
if mibBuilder.loadTexts:vrrpNotificationGroup.setStatus(_C)
vrrpNotificationsGroup=NotificationGroup((1,3,6,1,2,1,68,3,2,8))
vrrpNotificationsGroup.setObjects(*((_A,_Y),(_A,_Ah)))
if mibBuilder.loadTexts:vrrpNotificationsGroup.setStatus(_B)
vrrpMIBCompliance=ModuleCompliance((1,3,6,1,2,1,68,3,1,1))
vrrpMIBCompliance.setObjects(*((_A,_Ai),(_A,_Aj),(_A,_Ak),(_A,_Al)))
if mibBuilder.loadTexts:vrrpMIBCompliance.setStatus(_C)
vrrpModuleFullCompliance=ModuleCompliance((1,3,6,1,2,1,68,3,1,2))
vrrpModuleFullCompliance.setObjects(*((_A,_Z),(_A,_a),(_A,_b),(_A,_c)))
if mibBuilder.loadTexts:vrrpModuleFullCompliance.setStatus(_B)
vrrpModuleReadOnlyCompliance=ModuleCompliance((1,3,6,1,2,1,68,3,1,3))
vrrpModuleReadOnlyCompliance.setObjects(*((_A,_Z),(_A,_a),(_A,_b),(_A,_c)))
if mibBuilder.loadTexts:vrrpModuleReadOnlyCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'VrId':VrId,'vrrpMIB':vrrpMIB,'vrrpNotifications':vrrpNotifications,_Y:vrrpTrapNewMaster,_Ag:vrrpTrapAuthFailure,_Ah:vrrpTrapProtoError,'vrrpOperations':vrrpOperations,_p:vrrpNodeVersion,_P:vrrpNotificationCntl,'vrrpOperTable':vrrpOperTable,'vrrpOperEntry':vrrpOperEntry,_L:vrrpOperVrId,_q:vrrpOperVirtualMacAddr,_r:vrrpOperState,_s:vrrpOperAdminState,_t:vrrpOperPriority,_u:vrrpOperIpAddrCount,_v:vrrpOperMasterIpAddr,_w:vrrpOperPrimaryIpAddr,_x:vrrpOperAuthType,_y:vrrpOperAuthKey,_z:vrrpOperAdvertisementInterval,_A0:vrrpOperPreemptMode,_A1:vrrpOperVirtualRouterUpTime,_A2:vrrpOperProtocol,_A3:vrrpOperRowStatus,'vrrpAssoIpAddrTable':vrrpAssoIpAddrTable,'vrrpAssoIpAddrEntry':vrrpAssoIpAddrEntry,_l:vrrpAssoIpAddr,_A4:vrrpAssoIpAddrRowStatus,_T:vrrpTrapPacketSrc,_U:vrrpTrapAuthErrorType,'vrrpOperationsTable':vrrpOperationsTable,'vrrpOperationsEntry':vrrpOperationsEntry,_N:vrrpOperationsInetAddrType,_O:vrrpOperationsVrId,_AH:vrrpOperationsVirtualMacAddr,_AI:vrrpOperationsState,_AJ:vrrpOperationsPriority,_AQ:vrrpOperationsAddrCount,_V:vrrpOperationsMasterIpAddr,_AR:vrrpOperationsPrimaryIpAddr,_AK:vrrpOperationsAdvInterval,_AL:vrrpOperationsPreemptMode,_AM:vrrpOperationsAcceptMode,_AN:vrrpOperationsUpTime,_AO:vrrpOperationsStorageType,_AP:vrrpOperationsRowStatus,'vrrpAssociatedIpAddrTable':vrrpAssociatedIpAddrTable,'vrrpAssociatedIpAddrEntry':vrrpAssociatedIpAddrEntry,_m:vrrpAssociatedIpAddr,_AS:vrrpAssociatedStorageType,_AT:vrrpAssociatedIpAddrRowStatus,_W:vrrpNewMasterReason,_X:vrrpTrapProtoErrReason,'vrrpStatistics':vrrpStatistics,_Q:vrrpRouterChecksumErrors,_R:vrrpRouterVersionErrors,_S:vrrpRouterVrIdErrors,'vrrpRouterStatsTable':vrrpRouterStatsTable,_n:vrrpRouterStatsEntry,_A5:vrrpStatsBecomeMaster,_A6:vrrpStatsAdvertiseRcvd,_A7:vrrpStatsAdvertiseIntervalErrors,_A8:vrrpStatsAuthFailures,_A9:vrrpStatsIpTtlErrors,_AA:vrrpStatsPriorityZeroPktsRcvd,_AB:vrrpStatsPriorityZeroPktsSent,_AC:vrrpStatsInvalidTypePktsRcvd,_AD:vrrpStatsAddressListErrors,_AE:vrrpStatsInvalidAuthType,_AF:vrrpStatsAuthTypeMismatch,_AG:vrrpStatsPacketLengthErrors,'vrrpRouterStatisticsTable':vrrpRouterStatisticsTable,_o:vrrpRouterStatisticsEntry,_AU:vrrpStatisticsMasterTransitions,_AV:vrrpStatisticsRcvdAdvertisements,_AW:vrrpStatisticsAdvIntervalErrors,_Aa:vrrpStatisticsIpTtlErrors,_AX:vrrpStatisticsRcvdPriZeroPackets,_AY:vrrpStatisticsSentPriZeroPackets,_AZ:vrrpStatisticsRcvdInvalidTypePkts,_Ab:vrrpStatisticsAddressListErrors,_Ac:vrrpStatisticsPacketLengthErrors,_Ad:vrrpStatisticsRcvdInvalidAuthentications,_Ae:vrrpStatisticsDiscontinuityTime,_Af:vrrpStatisticsRefreshRate,'vrrpConformance':vrrpConformance,'vrrpMIBCompliances':vrrpMIBCompliances,'vrrpMIBCompliance':vrrpMIBCompliance,'vrrpModuleFullCompliance':vrrpModuleFullCompliance,'vrrpModuleReadOnlyCompliance':vrrpModuleReadOnlyCompliance,'vrrpMIBGroups':vrrpMIBGroups,_Ai:vrrpOperGroup,_Aj:vrrpStatsGroup,_Ak:vrrpTrapGroup,_Al:vrrpNotificationGroup,_Z:vrrpOperationsGroup,_a:vrrpStatisticsGroup,_b:vrrpTrapInfoGroup,_c:vrrpNotificationsGroup})