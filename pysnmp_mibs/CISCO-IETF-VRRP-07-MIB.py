_Ap='c07vrrpNotificationGroup'
_Ao='c07vrrpTrapGroup'
_An='c07vrrpStatsGroup'
_Am='c07vrrpOperGroup'
_Al='c07vrrpTrapProtoError'
_Ak='c07vrrpTrapNewMaster'
_Aj='c07vrrpTrapAuthFailure'
_Ai='c07vrrpStatisticsRefreshRate'
_Ah='c07vrrpStatisticsDiscontinuityTime'
_Ag='c07vrrpStatisticsRcvdInvalidAuthentications'
_Af='c07vrrpStatisticsPacketLengthErrors'
_Ae='c07vrrpStatisticsAddressListErrors'
_Ad='c07vrrpStatisticsIpTtlErrors'
_Ac='c07vrrpStatisticsRcvdInvalidTypePkts'
_Ab='c07vrrpStatisticsSentPriZeroPackets'
_Aa='c07vrrpStatisticsRcvdPriZeroPackets'
_AZ='c07vrrpStatisticsAdvIntervalErrors'
_AY='c07vrrpStatisticsRcvdAdvertisements'
_AX='c07vrrpStatisticsMasterTransitions'
_AW='c07vrrpAssociatedIpAddrRowStatus'
_AV='c07vrrpAssociatedStorageType'
_AU='c07vrrpOperationsPrimaryIpAddr'
_AT='c07vrrpOperationsAddrCount'
_AS='c07vrrpOperationsRowStatus'
_AR='c07vrrpOperationsStorageType'
_AQ='c07vrrpOperationsUpTime'
_AP='c07vrrpOperationsAcceptMode'
_AO='c07vrrpOperationsPreemptMode'
_AN='c07vrrpOperationsAdvInterval'
_AM='c07vrrpOperationsPriority'
_AL='c07vrrpOperationsState'
_AK='c07vrrpOperationsVirtualMacAddr'
_AJ='c07vrrpTrapProtoErrorCntl'
_AI='c07vrrpTrapNewMasterCntl'
_AH='c07vrrpStatsPacketLengthErrors'
_AG='c07vrrpStatsAuthTypeMismatch'
_AF='c07vrrpStatsInvalidAuthType'
_AE='c07vrrpStatsAddressListErrors'
_AD='c07vrrpStatsInvalidTypePktsRcvd'
_AC='c07vrrpStatsPriorityZeroPktsSent'
_AB='c07vrrpStatsPriorityZeroPktsRcvd'
_AA='c07vrrpStatsIpTtlErrors'
_A9='c07vrrpStatsAuthFailures'
_A8='c07vrrpStatsAdvertiseIntervalErrors'
_A7='c07vrrpStatsAdvertiseRcvd'
_A6='c07vrrpStatsBecomeMaster'
_A5='c07vrrpAssoIpAddrRowStatus'
_A4='c07vrrpOperRowStatus'
_A3='c07vrrpOperProtocol'
_A2='c07vrrpOperVirtualRouterUpTime'
_A1='c07vrrpOperPreemptMode'
_A0='c07vrrpOperAdvertisementInterval'
_z='c07vrrpOperAuthKey'
_y='c07vrrpOperAuthType'
_x='c07vrrpOperPrimaryIpAddr'
_w='c07vrrpOperMasterIpAddr'
_v='c07vrrpOperIpAddrCount'
_u='c07vrrpOperPriority'
_t='c07vrrpOperAdminState'
_s='c07vrrpOperState'
_r='c07vrrpOperVirtualMacAddr'
_q='c07vrrpNotificationCntl'
_p='c07vrrpNodeVersion'
_o='c07vrrpRouterStatisticsEntry'
_n='c07vrrpRouterStatsEntry'
_m='c07vrrpAssociatedIpAddr'
_l='c07vrrpAssoIpAddr'
_k='master'
_j='backup'
_i='initialize'
_h='TimeInterval'
_g='Unsigned32'
_f='IpAddress'
_e='OctetString'
_d='c07vrrpNotificationsGroup'
_c='c07vrrpTrapInfoGroup'
_b='c07vrrpStatisticsGroup'
_a='c07vrrpOperationsGroup'
_Z='c07vrrpNewMasterReason'
_Y='c07vrrpTrapProtoErrReason'
_X='c07vrrpOperationsMasterIpAddr'
_W='c07vrrpTrapAuthErrorType'
_V='c07vrrpTrapPacketSrc'
_U='c07vrrpRouterVrIdErrors'
_T='c07vrrpRouterVersionErrors'
_S='c07vrrpRouterChecksumErrors'
_R='c07vrrpOperationsVrId'
_Q='c07vrrpOperationsInetAddrType'
_P='c07vrrpOperVrId'
_O='read-write'
_N='disabled'
_M='enabled'
_L='StorageType'
_K='accessible-for-notify'
_J='TruthValue'
_I='not-accessible'
_H='ifIndex'
_G='IF-MIB'
_F='Integer32'
_E='read-create'
_D='read-only'
_C='deprecated'
_B='current'
_A='CISCO-IETF-VRRP-07-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_e,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoExperiment,=mibBuilder.importSymbols('CISCO-SMI','ciscoExperiment')
ifIndex,=mibBuilder.importSymbols(_G,_H)
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,_f,'ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_g,'iso')
DisplayString,MacAddress,PhysAddress,RowStatus,StorageType,TextualConvention,TimeInterval,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus',_L,'TextualConvention',_h,'TimeStamp',_J)
ciscoVrrp07MIB=ModuleIdentity((1,3,6,1,4,1,9,10,143))
if mibBuilder.loadTexts:ciscoVrrp07MIB.setRevisions(('2010-02-23 00:00','2009-03-10 00:00','2000-03-03 00:00'))
class C07VrId(TextualConvention,Integer32):status=_B;displayHint='d';subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_C07vrrpNotifications_ObjectIdentity=ObjectIdentity
c07vrrpNotifications=_C07vrrpNotifications_ObjectIdentity((1,3,6,1,4,1,9,10,143,0))
_C07vrrpOperations_ObjectIdentity=ObjectIdentity
c07vrrpOperations=_C07vrrpOperations_ObjectIdentity((1,3,6,1,4,1,9,10,143,1))
_C07vrrpNodeVersion_Type=Integer32
_C07vrrpNodeVersion_Object=MibScalar
c07vrrpNodeVersion=_C07vrrpNodeVersion_Object((1,3,6,1,4,1,9,10,143,1,1),_C07vrrpNodeVersion_Type())
c07vrrpNodeVersion.setMaxAccess(_D)
if mibBuilder.loadTexts:c07vrrpNodeVersion.setStatus(_C)
class _C07vrrpNotificationCntl_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_M,1),(_N,2)))
_C07vrrpNotificationCntl_Type.__name__=_F
_C07vrrpNotificationCntl_Object=MibScalar
c07vrrpNotificationCntl=_C07vrrpNotificationCntl_Object((1,3,6,1,4,1,9,10,143,1,2),_C07vrrpNotificationCntl_Type())
c07vrrpNotificationCntl.setMaxAccess(_O)
if mibBuilder.loadTexts:c07vrrpNotificationCntl.setStatus(_C)
_C07vrrpOperTable_Object=MibTable
c07vrrpOperTable=_C07vrrpOperTable_Object((1,3,6,1,4,1,9,10,143,1,3))
if mibBuilder.loadTexts:c07vrrpOperTable.setStatus(_C)
_C07vrrpOperEntry_Object=MibTableRow
c07vrrpOperEntry=_C07vrrpOperEntry_Object((1,3,6,1,4,1,9,10,143,1,3,1))
c07vrrpOperEntry.setIndexNames((0,_G,_H),(0,_A,_P))
if mibBuilder.loadTexts:c07vrrpOperEntry.setStatus(_C)
_C07vrrpOperVrId_Type=C07VrId
_C07vrrpOperVrId_Object=MibTableColumn
c07vrrpOperVrId=_C07vrrpOperVrId_Object((1,3,6,1,4,1,9,10,143,1,3,1,1),_C07vrrpOperVrId_Type())
c07vrrpOperVrId.setMaxAccess(_I)
if mibBuilder.loadTexts:c07vrrpOperVrId.setStatus(_C)
_C07vrrpOperVirtualMacAddr_Type=MacAddress
_C07vrrpOperVirtualMacAddr_Object=MibTableColumn
c07vrrpOperVirtualMacAddr=_C07vrrpOperVirtualMacAddr_Object((1,3,6,1,4,1,9,10,143,1,3,1,2),_C07vrrpOperVirtualMacAddr_Type())
c07vrrpOperVirtualMacAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:c07vrrpOperVirtualMacAddr.setStatus(_C)
class _C07vrrpOperState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_i,1),(_j,2),(_k,3)))
_C07vrrpOperState_Type.__name__=_F
_C07vrrpOperState_Object=MibTableColumn
c07vrrpOperState=_C07vrrpOperState_Object((1,3,6,1,4,1,9,10,143,1,3,1,3),_C07vrrpOperState_Type())
c07vrrpOperState.setMaxAccess(_D)
if mibBuilder.loadTexts:c07vrrpOperState.setStatus(_C)
class _C07vrrpOperAdminState_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('up',1),('down',2)))
_C07vrrpOperAdminState_Type.__name__=_F
_C07vrrpOperAdminState_Object=MibTableColumn
c07vrrpOperAdminState=_C07vrrpOperAdminState_Object((1,3,6,1,4,1,9,10,143,1,3,1,4),_C07vrrpOperAdminState_Type())
c07vrrpOperAdminState.setMaxAccess(_E)
if mibBuilder.loadTexts:c07vrrpOperAdminState.setStatus(_C)
class _C07vrrpOperPriority_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_C07vrrpOperPriority_Type.__name__=_F
_C07vrrpOperPriority_Object=MibTableColumn
c07vrrpOperPriority=_C07vrrpOperPriority_Object((1,3,6,1,4,1,9,10,143,1,3,1,5),_C07vrrpOperPriority_Type())
c07vrrpOperPriority.setMaxAccess(_E)
if mibBuilder.loadTexts:c07vrrpOperPriority.setStatus(_C)
class _C07vrrpOperIpAddrCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_C07vrrpOperIpAddrCount_Type.__name__=_F
_C07vrrpOperIpAddrCount_Object=MibTableColumn
c07vrrpOperIpAddrCount=_C07vrrpOperIpAddrCount_Object((1,3,6,1,4,1,9,10,143,1,3,1,6),_C07vrrpOperIpAddrCount_Type())
c07vrrpOperIpAddrCount.setMaxAccess(_D)
if mibBuilder.loadTexts:c07vrrpOperIpAddrCount.setStatus(_C)
_C07vrrpOperMasterIpAddr_Type=IpAddress
_C07vrrpOperMasterIpAddr_Object=MibTableColumn
c07vrrpOperMasterIpAddr=_C07vrrpOperMasterIpAddr_Object((1,3,6,1,4,1,9,10,143,1,3,1,7),_C07vrrpOperMasterIpAddr_Type())
c07vrrpOperMasterIpAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:c07vrrpOperMasterIpAddr.setStatus(_C)
class _C07vrrpOperPrimaryIpAddr_Type(IpAddress):defaultHexValue='00000000'
_C07vrrpOperPrimaryIpAddr_Type.__name__=_f
_C07vrrpOperPrimaryIpAddr_Object=MibTableColumn
c07vrrpOperPrimaryIpAddr=_C07vrrpOperPrimaryIpAddr_Object((1,3,6,1,4,1,9,10,143,1,3,1,8),_C07vrrpOperPrimaryIpAddr_Type())
c07vrrpOperPrimaryIpAddr.setMaxAccess(_E)
if mibBuilder.loadTexts:c07vrrpOperPrimaryIpAddr.setStatus(_C)
class _C07vrrpOperAuthType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('noAuthentication',1),('simpleTextPassword',2),('ipAuthenticationHeader',3)))
_C07vrrpOperAuthType_Type.__name__=_F
_C07vrrpOperAuthType_Object=MibTableColumn
c07vrrpOperAuthType=_C07vrrpOperAuthType_Object((1,3,6,1,4,1,9,10,143,1,3,1,9),_C07vrrpOperAuthType_Type())
c07vrrpOperAuthType.setMaxAccess(_E)
if mibBuilder.loadTexts:c07vrrpOperAuthType.setStatus(_C)
class _C07vrrpOperAuthKey_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_C07vrrpOperAuthKey_Type.__name__=_e
_C07vrrpOperAuthKey_Object=MibTableColumn
c07vrrpOperAuthKey=_C07vrrpOperAuthKey_Object((1,3,6,1,4,1,9,10,143,1,3,1,10),_C07vrrpOperAuthKey_Type())
c07vrrpOperAuthKey.setMaxAccess(_E)
if mibBuilder.loadTexts:c07vrrpOperAuthKey.setStatus(_C)
class _C07vrrpOperAdvertisementInterval_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_C07vrrpOperAdvertisementInterval_Type.__name__=_F
_C07vrrpOperAdvertisementInterval_Object=MibTableColumn
c07vrrpOperAdvertisementInterval=_C07vrrpOperAdvertisementInterval_Object((1,3,6,1,4,1,9,10,143,1,3,1,11),_C07vrrpOperAdvertisementInterval_Type())
c07vrrpOperAdvertisementInterval.setMaxAccess(_E)
if mibBuilder.loadTexts:c07vrrpOperAdvertisementInterval.setStatus(_C)
if mibBuilder.loadTexts:c07vrrpOperAdvertisementInterval.setUnits('seconds')
class _C07vrrpOperPreemptMode_Type(TruthValue):defaultValue=1
_C07vrrpOperPreemptMode_Type.__name__=_J
_C07vrrpOperPreemptMode_Object=MibTableColumn
c07vrrpOperPreemptMode=_C07vrrpOperPreemptMode_Object((1,3,6,1,4,1,9,10,143,1,3,1,12),_C07vrrpOperPreemptMode_Type())
c07vrrpOperPreemptMode.setMaxAccess(_E)
if mibBuilder.loadTexts:c07vrrpOperPreemptMode.setStatus(_C)
_C07vrrpOperVirtualRouterUpTime_Type=TimeStamp
_C07vrrpOperVirtualRouterUpTime_Object=MibTableColumn
c07vrrpOperVirtualRouterUpTime=_C07vrrpOperVirtualRouterUpTime_Object((1,3,6,1,4,1,9,10,143,1,3,1,13),_C07vrrpOperVirtualRouterUpTime_Type())
c07vrrpOperVirtualRouterUpTime.setMaxAccess(_D)
if mibBuilder.loadTexts:c07vrrpOperVirtualRouterUpTime.setStatus(_C)
class _C07vrrpOperProtocol_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('ip',1),('bridge',2),('decnet',3),('other',4)))
_C07vrrpOperProtocol_Type.__name__=_F
_C07vrrpOperProtocol_Object=MibTableColumn
c07vrrpOperProtocol=_C07vrrpOperProtocol_Object((1,3,6,1,4,1,9,10,143,1,3,1,14),_C07vrrpOperProtocol_Type())
c07vrrpOperProtocol.setMaxAccess(_E)
if mibBuilder.loadTexts:c07vrrpOperProtocol.setStatus(_C)
_C07vrrpOperRowStatus_Type=RowStatus
_C07vrrpOperRowStatus_Object=MibTableColumn
c07vrrpOperRowStatus=_C07vrrpOperRowStatus_Object((1,3,6,1,4,1,9,10,143,1,3,1,15),_C07vrrpOperRowStatus_Type())
c07vrrpOperRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:c07vrrpOperRowStatus.setStatus(_C)
_C07vrrpAssoIpAddrTable_Object=MibTable
c07vrrpAssoIpAddrTable=_C07vrrpAssoIpAddrTable_Object((1,3,6,1,4,1,9,10,143,1,4))
if mibBuilder.loadTexts:c07vrrpAssoIpAddrTable.setStatus(_C)
_C07vrrpAssoIpAddrEntry_Object=MibTableRow
c07vrrpAssoIpAddrEntry=_C07vrrpAssoIpAddrEntry_Object((1,3,6,1,4,1,9,10,143,1,4,1))
c07vrrpAssoIpAddrEntry.setIndexNames((0,_G,_H),(0,_A,_P),(0,_A,_l))
if mibBuilder.loadTexts:c07vrrpAssoIpAddrEntry.setStatus(_C)
_C07vrrpAssoIpAddr_Type=IpAddress
_C07vrrpAssoIpAddr_Object=MibTableColumn
c07vrrpAssoIpAddr=_C07vrrpAssoIpAddr_Object((1,3,6,1,4,1,9,10,143,1,4,1,1),_C07vrrpAssoIpAddr_Type())
c07vrrpAssoIpAddr.setMaxAccess(_I)
if mibBuilder.loadTexts:c07vrrpAssoIpAddr.setStatus(_C)
_C07vrrpAssoIpAddrRowStatus_Type=RowStatus
_C07vrrpAssoIpAddrRowStatus_Object=MibTableColumn
c07vrrpAssoIpAddrRowStatus=_C07vrrpAssoIpAddrRowStatus_Object((1,3,6,1,4,1,9,10,143,1,4,1,2),_C07vrrpAssoIpAddrRowStatus_Type())
c07vrrpAssoIpAddrRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:c07vrrpAssoIpAddrRowStatus.setStatus(_C)
_C07vrrpTrapPacketSrc_Type=IpAddress
_C07vrrpTrapPacketSrc_Object=MibScalar
c07vrrpTrapPacketSrc=_C07vrrpTrapPacketSrc_Object((1,3,6,1,4,1,9,10,143,1,5),_C07vrrpTrapPacketSrc_Type())
c07vrrpTrapPacketSrc.setMaxAccess(_K)
if mibBuilder.loadTexts:c07vrrpTrapPacketSrc.setStatus(_C)
class _C07vrrpTrapAuthErrorType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('invalidAuthType',1),('authTypeMismatch',2),('authFailure',3)))
_C07vrrpTrapAuthErrorType_Type.__name__=_F
_C07vrrpTrapAuthErrorType_Object=MibScalar
c07vrrpTrapAuthErrorType=_C07vrrpTrapAuthErrorType_Object((1,3,6,1,4,1,9,10,143,1,6),_C07vrrpTrapAuthErrorType_Type())
c07vrrpTrapAuthErrorType.setMaxAccess(_K)
if mibBuilder.loadTexts:c07vrrpTrapAuthErrorType.setStatus(_C)
_C07vrrpOperationsTable_Object=MibTable
c07vrrpOperationsTable=_C07vrrpOperationsTable_Object((1,3,6,1,4,1,9,10,143,1,7))
if mibBuilder.loadTexts:c07vrrpOperationsTable.setStatus(_B)
_C07vrrpOperationsEntry_Object=MibTableRow
c07vrrpOperationsEntry=_C07vrrpOperationsEntry_Object((1,3,6,1,4,1,9,10,143,1,7,1))
c07vrrpOperationsEntry.setIndexNames((0,_A,_Q),(0,_A,_R),(0,_G,_H))
if mibBuilder.loadTexts:c07vrrpOperationsEntry.setStatus(_B)
_C07vrrpOperationsInetAddrType_Type=InetAddressType
_C07vrrpOperationsInetAddrType_Object=MibTableColumn
c07vrrpOperationsInetAddrType=_C07vrrpOperationsInetAddrType_Object((1,3,6,1,4,1,9,10,143,1,7,1,1),_C07vrrpOperationsInetAddrType_Type())
c07vrrpOperationsInetAddrType.setMaxAccess(_I)
if mibBuilder.loadTexts:c07vrrpOperationsInetAddrType.setStatus(_B)
_C07vrrpOperationsVrId_Type=C07VrId
_C07vrrpOperationsVrId_Object=MibTableColumn
c07vrrpOperationsVrId=_C07vrrpOperationsVrId_Object((1,3,6,1,4,1,9,10,143,1,7,1,2),_C07vrrpOperationsVrId_Type())
c07vrrpOperationsVrId.setMaxAccess(_I)
if mibBuilder.loadTexts:c07vrrpOperationsVrId.setStatus(_B)
_C07vrrpOperationsVirtualMacAddr_Type=MacAddress
_C07vrrpOperationsVirtualMacAddr_Object=MibTableColumn
c07vrrpOperationsVirtualMacAddr=_C07vrrpOperationsVirtualMacAddr_Object((1,3,6,1,4,1,9,10,143,1,7,1,3),_C07vrrpOperationsVirtualMacAddr_Type())
c07vrrpOperationsVirtualMacAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:c07vrrpOperationsVirtualMacAddr.setStatus(_B)
class _C07vrrpOperationsState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_i,1),(_j,2),(_k,3)))
_C07vrrpOperationsState_Type.__name__=_F
_C07vrrpOperationsState_Object=MibTableColumn
c07vrrpOperationsState=_C07vrrpOperationsState_Object((1,3,6,1,4,1,9,10,143,1,7,1,4),_C07vrrpOperationsState_Type())
c07vrrpOperationsState.setMaxAccess(_D)
if mibBuilder.loadTexts:c07vrrpOperationsState.setStatus(_B)
class _C07vrrpOperationsPriority_Type(Unsigned32):defaultValue=100;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_C07vrrpOperationsPriority_Type.__name__=_g
_C07vrrpOperationsPriority_Object=MibTableColumn
c07vrrpOperationsPriority=_C07vrrpOperationsPriority_Object((1,3,6,1,4,1,9,10,143,1,7,1,5),_C07vrrpOperationsPriority_Type())
c07vrrpOperationsPriority.setMaxAccess(_E)
if mibBuilder.loadTexts:c07vrrpOperationsPriority.setStatus(_B)
class _C07vrrpOperationsAddrCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_C07vrrpOperationsAddrCount_Type.__name__=_F
_C07vrrpOperationsAddrCount_Object=MibTableColumn
c07vrrpOperationsAddrCount=_C07vrrpOperationsAddrCount_Object((1,3,6,1,4,1,9,10,143,1,7,1,6),_C07vrrpOperationsAddrCount_Type())
c07vrrpOperationsAddrCount.setMaxAccess(_D)
if mibBuilder.loadTexts:c07vrrpOperationsAddrCount.setStatus(_B)
_C07vrrpOperationsMasterIpAddr_Type=InetAddress
_C07vrrpOperationsMasterIpAddr_Object=MibTableColumn
c07vrrpOperationsMasterIpAddr=_C07vrrpOperationsMasterIpAddr_Object((1,3,6,1,4,1,9,10,143,1,7,1,7),_C07vrrpOperationsMasterIpAddr_Type())
c07vrrpOperationsMasterIpAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:c07vrrpOperationsMasterIpAddr.setStatus(_B)
_C07vrrpOperationsPrimaryIpAddr_Type=InetAddress
_C07vrrpOperationsPrimaryIpAddr_Object=MibTableColumn
c07vrrpOperationsPrimaryIpAddr=_C07vrrpOperationsPrimaryIpAddr_Object((1,3,6,1,4,1,9,10,143,1,7,1,8),_C07vrrpOperationsPrimaryIpAddr_Type())
c07vrrpOperationsPrimaryIpAddr.setMaxAccess(_E)
if mibBuilder.loadTexts:c07vrrpOperationsPrimaryIpAddr.setStatus(_B)
class _C07vrrpOperationsAdvInterval_Type(TimeInterval):defaultValue=100;subtypeSpec=TimeInterval.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_C07vrrpOperationsAdvInterval_Type.__name__=_h
_C07vrrpOperationsAdvInterval_Object=MibTableColumn
c07vrrpOperationsAdvInterval=_C07vrrpOperationsAdvInterval_Object((1,3,6,1,4,1,9,10,143,1,7,1,9),_C07vrrpOperationsAdvInterval_Type())
c07vrrpOperationsAdvInterval.setMaxAccess(_E)
if mibBuilder.loadTexts:c07vrrpOperationsAdvInterval.setStatus(_B)
if mibBuilder.loadTexts:c07vrrpOperationsAdvInterval.setUnits('centiseconds')
class _C07vrrpOperationsPreemptMode_Type(TruthValue):defaultValue=1
_C07vrrpOperationsPreemptMode_Type.__name__=_J
_C07vrrpOperationsPreemptMode_Object=MibTableColumn
c07vrrpOperationsPreemptMode=_C07vrrpOperationsPreemptMode_Object((1,3,6,1,4,1,9,10,143,1,7,1,10),_C07vrrpOperationsPreemptMode_Type())
c07vrrpOperationsPreemptMode.setMaxAccess(_E)
if mibBuilder.loadTexts:c07vrrpOperationsPreemptMode.setStatus(_B)
class _C07vrrpOperationsAcceptMode_Type(TruthValue):defaultValue=2
_C07vrrpOperationsAcceptMode_Type.__name__=_J
_C07vrrpOperationsAcceptMode_Object=MibTableColumn
c07vrrpOperationsAcceptMode=_C07vrrpOperationsAcceptMode_Object((1,3,6,1,4,1,9,10,143,1,7,1,11),_C07vrrpOperationsAcceptMode_Type())
c07vrrpOperationsAcceptMode.setMaxAccess(_E)
if mibBuilder.loadTexts:c07vrrpOperationsAcceptMode.setStatus(_B)
_C07vrrpOperationsUpTime_Type=TimeStamp
_C07vrrpOperationsUpTime_Object=MibTableColumn
c07vrrpOperationsUpTime=_C07vrrpOperationsUpTime_Object((1,3,6,1,4,1,9,10,143,1,7,1,12),_C07vrrpOperationsUpTime_Type())
c07vrrpOperationsUpTime.setMaxAccess(_D)
if mibBuilder.loadTexts:c07vrrpOperationsUpTime.setStatus(_B)
class _C07vrrpOperationsStorageType_Type(StorageType):defaultValue=3
_C07vrrpOperationsStorageType_Type.__name__=_L
_C07vrrpOperationsStorageType_Object=MibTableColumn
c07vrrpOperationsStorageType=_C07vrrpOperationsStorageType_Object((1,3,6,1,4,1,9,10,143,1,7,1,13),_C07vrrpOperationsStorageType_Type())
c07vrrpOperationsStorageType.setMaxAccess(_E)
if mibBuilder.loadTexts:c07vrrpOperationsStorageType.setStatus(_B)
_C07vrrpOperationsRowStatus_Type=RowStatus
_C07vrrpOperationsRowStatus_Object=MibTableColumn
c07vrrpOperationsRowStatus=_C07vrrpOperationsRowStatus_Object((1,3,6,1,4,1,9,10,143,1,7,1,14),_C07vrrpOperationsRowStatus_Type())
c07vrrpOperationsRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:c07vrrpOperationsRowStatus.setStatus(_B)
_C07vrrpAssociatedIpAddrTable_Object=MibTable
c07vrrpAssociatedIpAddrTable=_C07vrrpAssociatedIpAddrTable_Object((1,3,6,1,4,1,9,10,143,1,8))
if mibBuilder.loadTexts:c07vrrpAssociatedIpAddrTable.setStatus(_B)
_C07vrrpAssociatedIpAddrEntry_Object=MibTableRow
c07vrrpAssociatedIpAddrEntry=_C07vrrpAssociatedIpAddrEntry_Object((1,3,6,1,4,1,9,10,143,1,8,1))
c07vrrpAssociatedIpAddrEntry.setIndexNames((0,_A,_Q),(0,_A,_R),(0,_G,_H),(0,_A,_m))
if mibBuilder.loadTexts:c07vrrpAssociatedIpAddrEntry.setStatus(_B)
_C07vrrpAssociatedIpAddr_Type=InetAddress
_C07vrrpAssociatedIpAddr_Object=MibTableColumn
c07vrrpAssociatedIpAddr=_C07vrrpAssociatedIpAddr_Object((1,3,6,1,4,1,9,10,143,1,8,1,1),_C07vrrpAssociatedIpAddr_Type())
c07vrrpAssociatedIpAddr.setMaxAccess(_I)
if mibBuilder.loadTexts:c07vrrpAssociatedIpAddr.setStatus(_B)
class _C07vrrpAssociatedStorageType_Type(StorageType):defaultValue=3
_C07vrrpAssociatedStorageType_Type.__name__=_L
_C07vrrpAssociatedStorageType_Object=MibTableColumn
c07vrrpAssociatedStorageType=_C07vrrpAssociatedStorageType_Object((1,3,6,1,4,1,9,10,143,1,8,1,2),_C07vrrpAssociatedStorageType_Type())
c07vrrpAssociatedStorageType.setMaxAccess(_E)
if mibBuilder.loadTexts:c07vrrpAssociatedStorageType.setStatus(_B)
_C07vrrpAssociatedIpAddrRowStatus_Type=RowStatus
_C07vrrpAssociatedIpAddrRowStatus_Object=MibTableColumn
c07vrrpAssociatedIpAddrRowStatus=_C07vrrpAssociatedIpAddrRowStatus_Object((1,3,6,1,4,1,9,10,143,1,8,1,3),_C07vrrpAssociatedIpAddrRowStatus_Type())
c07vrrpAssociatedIpAddrRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:c07vrrpAssociatedIpAddrRowStatus.setStatus(_B)
class _C07vrrpNewMasterReason_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('notmaster',0),('priority',1),('preempted',2),('masterNoResponse',3)))
_C07vrrpNewMasterReason_Type.__name__=_F
_C07vrrpNewMasterReason_Object=MibScalar
c07vrrpNewMasterReason=_C07vrrpNewMasterReason_Object((1,3,6,1,4,1,9,10,143,1,9),_C07vrrpNewMasterReason_Type())
c07vrrpNewMasterReason.setMaxAccess(_K)
if mibBuilder.loadTexts:c07vrrpNewMasterReason.setStatus(_B)
class _C07vrrpTrapProtoErrReason_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('ipTtlError',0),('versionError',1),('checksumError',2),('vridError',3)))
_C07vrrpTrapProtoErrReason_Type.__name__=_F
_C07vrrpTrapProtoErrReason_Object=MibScalar
c07vrrpTrapProtoErrReason=_C07vrrpTrapProtoErrReason_Object((1,3,6,1,4,1,9,10,143,1,10),_C07vrrpTrapProtoErrReason_Type())
c07vrrpTrapProtoErrReason.setMaxAccess(_K)
if mibBuilder.loadTexts:c07vrrpTrapProtoErrReason.setStatus(_B)
class _C07vrrpTrapNewMasterCntl_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_M,1),(_N,2)))
_C07vrrpTrapNewMasterCntl_Type.__name__=_F
_C07vrrpTrapNewMasterCntl_Object=MibScalar
c07vrrpTrapNewMasterCntl=_C07vrrpTrapNewMasterCntl_Object((1,3,6,1,4,1,9,10,143,1,11),_C07vrrpTrapNewMasterCntl_Type())
c07vrrpTrapNewMasterCntl.setMaxAccess(_O)
if mibBuilder.loadTexts:c07vrrpTrapNewMasterCntl.setStatus(_B)
class _C07vrrpTrapProtoErrorCntl_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_M,1),(_N,2)))
_C07vrrpTrapProtoErrorCntl_Type.__name__=_F
_C07vrrpTrapProtoErrorCntl_Object=MibScalar
c07vrrpTrapProtoErrorCntl=_C07vrrpTrapProtoErrorCntl_Object((1,3,6,1,4,1,9,10,143,1,12),_C07vrrpTrapProtoErrorCntl_Type())
c07vrrpTrapProtoErrorCntl.setMaxAccess(_O)
if mibBuilder.loadTexts:c07vrrpTrapProtoErrorCntl.setStatus(_B)
_C07vrrpStatistics_ObjectIdentity=ObjectIdentity
c07vrrpStatistics=_C07vrrpStatistics_ObjectIdentity((1,3,6,1,4,1,9,10,143,2))
_C07vrrpRouterChecksumErrors_Type=Counter32
_C07vrrpRouterChecksumErrors_Object=MibScalar
c07vrrpRouterChecksumErrors=_C07vrrpRouterChecksumErrors_Object((1,3,6,1,4,1,9,10,143,2,1),_C07vrrpRouterChecksumErrors_Type())
c07vrrpRouterChecksumErrors.setMaxAccess(_D)
if mibBuilder.loadTexts:c07vrrpRouterChecksumErrors.setStatus(_B)
_C07vrrpRouterVersionErrors_Type=Counter32
_C07vrrpRouterVersionErrors_Object=MibScalar
c07vrrpRouterVersionErrors=_C07vrrpRouterVersionErrors_Object((1,3,6,1,4,1,9,10,143,2,2),_C07vrrpRouterVersionErrors_Type())
c07vrrpRouterVersionErrors.setMaxAccess(_D)
if mibBuilder.loadTexts:c07vrrpRouterVersionErrors.setStatus(_B)
_C07vrrpRouterVrIdErrors_Type=Counter32
_C07vrrpRouterVrIdErrors_Object=MibScalar
c07vrrpRouterVrIdErrors=_C07vrrpRouterVrIdErrors_Object((1,3,6,1,4,1,9,10,143,2,3),_C07vrrpRouterVrIdErrors_Type())
c07vrrpRouterVrIdErrors.setMaxAccess(_D)
if mibBuilder.loadTexts:c07vrrpRouterVrIdErrors.setStatus(_B)
_C07vrrpRouterStatsTable_Object=MibTable
c07vrrpRouterStatsTable=_C07vrrpRouterStatsTable_Object((1,3,6,1,4,1,9,10,143,2,4))
if mibBuilder.loadTexts:c07vrrpRouterStatsTable.setStatus(_C)
_C07vrrpRouterStatsEntry_Object=MibTableRow
c07vrrpRouterStatsEntry=_C07vrrpRouterStatsEntry_Object((1,3,6,1,4,1,9,10,143,2,4,1))
if mibBuilder.loadTexts:c07vrrpRouterStatsEntry.setStatus(_C)
_C07vrrpStatsBecomeMaster_Type=Counter32
_C07vrrpStatsBecomeMaster_Object=MibTableColumn
c07vrrpStatsBecomeMaster=_C07vrrpStatsBecomeMaster_Object((1,3,6,1,4,1,9,10,143,2,4,1,1),_C07vrrpStatsBecomeMaster_Type())
c07vrrpStatsBecomeMaster.setMaxAccess(_D)
if mibBuilder.loadTexts:c07vrrpStatsBecomeMaster.setStatus(_C)
_C07vrrpStatsAdvertiseRcvd_Type=Counter32
_C07vrrpStatsAdvertiseRcvd_Object=MibTableColumn
c07vrrpStatsAdvertiseRcvd=_C07vrrpStatsAdvertiseRcvd_Object((1,3,6,1,4,1,9,10,143,2,4,1,2),_C07vrrpStatsAdvertiseRcvd_Type())
c07vrrpStatsAdvertiseRcvd.setMaxAccess(_D)
if mibBuilder.loadTexts:c07vrrpStatsAdvertiseRcvd.setStatus(_C)
_C07vrrpStatsAdvertiseIntervalErrors_Type=Counter32
_C07vrrpStatsAdvertiseIntervalErrors_Object=MibTableColumn
c07vrrpStatsAdvertiseIntervalErrors=_C07vrrpStatsAdvertiseIntervalErrors_Object((1,3,6,1,4,1,9,10,143,2,4,1,3),_C07vrrpStatsAdvertiseIntervalErrors_Type())
c07vrrpStatsAdvertiseIntervalErrors.setMaxAccess(_D)
if mibBuilder.loadTexts:c07vrrpStatsAdvertiseIntervalErrors.setStatus(_C)
_C07vrrpStatsAuthFailures_Type=Counter32
_C07vrrpStatsAuthFailures_Object=MibTableColumn
c07vrrpStatsAuthFailures=_C07vrrpStatsAuthFailures_Object((1,3,6,1,4,1,9,10,143,2,4,1,4),_C07vrrpStatsAuthFailures_Type())
c07vrrpStatsAuthFailures.setMaxAccess(_D)
if mibBuilder.loadTexts:c07vrrpStatsAuthFailures.setStatus(_C)
_C07vrrpStatsIpTtlErrors_Type=Counter32
_C07vrrpStatsIpTtlErrors_Object=MibTableColumn
c07vrrpStatsIpTtlErrors=_C07vrrpStatsIpTtlErrors_Object((1,3,6,1,4,1,9,10,143,2,4,1,5),_C07vrrpStatsIpTtlErrors_Type())
c07vrrpStatsIpTtlErrors.setMaxAccess(_D)
if mibBuilder.loadTexts:c07vrrpStatsIpTtlErrors.setStatus(_C)
_C07vrrpStatsPriorityZeroPktsRcvd_Type=Counter32
_C07vrrpStatsPriorityZeroPktsRcvd_Object=MibTableColumn
c07vrrpStatsPriorityZeroPktsRcvd=_C07vrrpStatsPriorityZeroPktsRcvd_Object((1,3,6,1,4,1,9,10,143,2,4,1,6),_C07vrrpStatsPriorityZeroPktsRcvd_Type())
c07vrrpStatsPriorityZeroPktsRcvd.setMaxAccess(_D)
if mibBuilder.loadTexts:c07vrrpStatsPriorityZeroPktsRcvd.setStatus(_C)
_C07vrrpStatsPriorityZeroPktsSent_Type=Counter32
_C07vrrpStatsPriorityZeroPktsSent_Object=MibTableColumn
c07vrrpStatsPriorityZeroPktsSent=_C07vrrpStatsPriorityZeroPktsSent_Object((1,3,6,1,4,1,9,10,143,2,4,1,7),_C07vrrpStatsPriorityZeroPktsSent_Type())
c07vrrpStatsPriorityZeroPktsSent.setMaxAccess(_D)
if mibBuilder.loadTexts:c07vrrpStatsPriorityZeroPktsSent.setStatus(_C)
_C07vrrpStatsInvalidTypePktsRcvd_Type=Counter32
_C07vrrpStatsInvalidTypePktsRcvd_Object=MibTableColumn
c07vrrpStatsInvalidTypePktsRcvd=_C07vrrpStatsInvalidTypePktsRcvd_Object((1,3,6,1,4,1,9,10,143,2,4,1,8),_C07vrrpStatsInvalidTypePktsRcvd_Type())
c07vrrpStatsInvalidTypePktsRcvd.setMaxAccess(_D)
if mibBuilder.loadTexts:c07vrrpStatsInvalidTypePktsRcvd.setStatus(_C)
_C07vrrpStatsAddressListErrors_Type=Counter32
_C07vrrpStatsAddressListErrors_Object=MibTableColumn
c07vrrpStatsAddressListErrors=_C07vrrpStatsAddressListErrors_Object((1,3,6,1,4,1,9,10,143,2,4,1,9),_C07vrrpStatsAddressListErrors_Type())
c07vrrpStatsAddressListErrors.setMaxAccess(_D)
if mibBuilder.loadTexts:c07vrrpStatsAddressListErrors.setStatus(_C)
_C07vrrpStatsInvalidAuthType_Type=Counter32
_C07vrrpStatsInvalidAuthType_Object=MibTableColumn
c07vrrpStatsInvalidAuthType=_C07vrrpStatsInvalidAuthType_Object((1,3,6,1,4,1,9,10,143,2,4,1,10),_C07vrrpStatsInvalidAuthType_Type())
c07vrrpStatsInvalidAuthType.setMaxAccess(_D)
if mibBuilder.loadTexts:c07vrrpStatsInvalidAuthType.setStatus(_C)
_C07vrrpStatsAuthTypeMismatch_Type=Counter32
_C07vrrpStatsAuthTypeMismatch_Object=MibTableColumn
c07vrrpStatsAuthTypeMismatch=_C07vrrpStatsAuthTypeMismatch_Object((1,3,6,1,4,1,9,10,143,2,4,1,11),_C07vrrpStatsAuthTypeMismatch_Type())
c07vrrpStatsAuthTypeMismatch.setMaxAccess(_D)
if mibBuilder.loadTexts:c07vrrpStatsAuthTypeMismatch.setStatus(_C)
_C07vrrpStatsPacketLengthErrors_Type=Counter32
_C07vrrpStatsPacketLengthErrors_Object=MibTableColumn
c07vrrpStatsPacketLengthErrors=_C07vrrpStatsPacketLengthErrors_Object((1,3,6,1,4,1,9,10,143,2,4,1,12),_C07vrrpStatsPacketLengthErrors_Type())
c07vrrpStatsPacketLengthErrors.setMaxAccess(_D)
if mibBuilder.loadTexts:c07vrrpStatsPacketLengthErrors.setStatus(_C)
_C07vrrpRouterStatisticsTable_Object=MibTable
c07vrrpRouterStatisticsTable=_C07vrrpRouterStatisticsTable_Object((1,3,6,1,4,1,9,10,143,2,5))
if mibBuilder.loadTexts:c07vrrpRouterStatisticsTable.setStatus(_B)
_C07vrrpRouterStatisticsEntry_Object=MibTableRow
c07vrrpRouterStatisticsEntry=_C07vrrpRouterStatisticsEntry_Object((1,3,6,1,4,1,9,10,143,2,5,1))
if mibBuilder.loadTexts:c07vrrpRouterStatisticsEntry.setStatus(_B)
_C07vrrpStatisticsMasterTransitions_Type=Counter32
_C07vrrpStatisticsMasterTransitions_Object=MibTableColumn
c07vrrpStatisticsMasterTransitions=_C07vrrpStatisticsMasterTransitions_Object((1,3,6,1,4,1,9,10,143,2,5,1,1),_C07vrrpStatisticsMasterTransitions_Type())
c07vrrpStatisticsMasterTransitions.setMaxAccess(_D)
if mibBuilder.loadTexts:c07vrrpStatisticsMasterTransitions.setStatus(_B)
_C07vrrpStatisticsRcvdAdvertisements_Type=Counter32
_C07vrrpStatisticsRcvdAdvertisements_Object=MibTableColumn
c07vrrpStatisticsRcvdAdvertisements=_C07vrrpStatisticsRcvdAdvertisements_Object((1,3,6,1,4,1,9,10,143,2,5,1,2),_C07vrrpStatisticsRcvdAdvertisements_Type())
c07vrrpStatisticsRcvdAdvertisements.setMaxAccess(_D)
if mibBuilder.loadTexts:c07vrrpStatisticsRcvdAdvertisements.setStatus(_B)
_C07vrrpStatisticsAdvIntervalErrors_Type=Counter32
_C07vrrpStatisticsAdvIntervalErrors_Object=MibTableColumn
c07vrrpStatisticsAdvIntervalErrors=_C07vrrpStatisticsAdvIntervalErrors_Object((1,3,6,1,4,1,9,10,143,2,5,1,3),_C07vrrpStatisticsAdvIntervalErrors_Type())
c07vrrpStatisticsAdvIntervalErrors.setMaxAccess(_D)
if mibBuilder.loadTexts:c07vrrpStatisticsAdvIntervalErrors.setStatus(_B)
_C07vrrpStatisticsIpTtlErrors_Type=Counter32
_C07vrrpStatisticsIpTtlErrors_Object=MibTableColumn
c07vrrpStatisticsIpTtlErrors=_C07vrrpStatisticsIpTtlErrors_Object((1,3,6,1,4,1,9,10,143,2,5,1,4),_C07vrrpStatisticsIpTtlErrors_Type())
c07vrrpStatisticsIpTtlErrors.setMaxAccess(_D)
if mibBuilder.loadTexts:c07vrrpStatisticsIpTtlErrors.setStatus(_B)
_C07vrrpStatisticsRcvdPriZeroPackets_Type=Counter32
_C07vrrpStatisticsRcvdPriZeroPackets_Object=MibTableColumn
c07vrrpStatisticsRcvdPriZeroPackets=_C07vrrpStatisticsRcvdPriZeroPackets_Object((1,3,6,1,4,1,9,10,143,2,5,1,5),_C07vrrpStatisticsRcvdPriZeroPackets_Type())
c07vrrpStatisticsRcvdPriZeroPackets.setMaxAccess(_D)
if mibBuilder.loadTexts:c07vrrpStatisticsRcvdPriZeroPackets.setStatus(_B)
_C07vrrpStatisticsSentPriZeroPackets_Type=Counter32
_C07vrrpStatisticsSentPriZeroPackets_Object=MibTableColumn
c07vrrpStatisticsSentPriZeroPackets=_C07vrrpStatisticsSentPriZeroPackets_Object((1,3,6,1,4,1,9,10,143,2,5,1,6),_C07vrrpStatisticsSentPriZeroPackets_Type())
c07vrrpStatisticsSentPriZeroPackets.setMaxAccess(_D)
if mibBuilder.loadTexts:c07vrrpStatisticsSentPriZeroPackets.setStatus(_B)
_C07vrrpStatisticsRcvdInvalidTypePkts_Type=Counter32
_C07vrrpStatisticsRcvdInvalidTypePkts_Object=MibTableColumn
c07vrrpStatisticsRcvdInvalidTypePkts=_C07vrrpStatisticsRcvdInvalidTypePkts_Object((1,3,6,1,4,1,9,10,143,2,5,1,7),_C07vrrpStatisticsRcvdInvalidTypePkts_Type())
c07vrrpStatisticsRcvdInvalidTypePkts.setMaxAccess(_D)
if mibBuilder.loadTexts:c07vrrpStatisticsRcvdInvalidTypePkts.setStatus(_B)
_C07vrrpStatisticsAddressListErrors_Type=Counter32
_C07vrrpStatisticsAddressListErrors_Object=MibTableColumn
c07vrrpStatisticsAddressListErrors=_C07vrrpStatisticsAddressListErrors_Object((1,3,6,1,4,1,9,10,143,2,5,1,8),_C07vrrpStatisticsAddressListErrors_Type())
c07vrrpStatisticsAddressListErrors.setMaxAccess(_D)
if mibBuilder.loadTexts:c07vrrpStatisticsAddressListErrors.setStatus(_B)
_C07vrrpStatisticsPacketLengthErrors_Type=Counter32
_C07vrrpStatisticsPacketLengthErrors_Object=MibTableColumn
c07vrrpStatisticsPacketLengthErrors=_C07vrrpStatisticsPacketLengthErrors_Object((1,3,6,1,4,1,9,10,143,2,5,1,9),_C07vrrpStatisticsPacketLengthErrors_Type())
c07vrrpStatisticsPacketLengthErrors.setMaxAccess(_D)
if mibBuilder.loadTexts:c07vrrpStatisticsPacketLengthErrors.setStatus(_B)
_C07vrrpStatisticsRcvdInvalidAuthentications_Type=Counter32
_C07vrrpStatisticsRcvdInvalidAuthentications_Object=MibTableColumn
c07vrrpStatisticsRcvdInvalidAuthentications=_C07vrrpStatisticsRcvdInvalidAuthentications_Object((1,3,6,1,4,1,9,10,143,2,5,1,10),_C07vrrpStatisticsRcvdInvalidAuthentications_Type())
c07vrrpStatisticsRcvdInvalidAuthentications.setMaxAccess(_D)
if mibBuilder.loadTexts:c07vrrpStatisticsRcvdInvalidAuthentications.setStatus(_B)
_C07vrrpStatisticsDiscontinuityTime_Type=TimeStamp
_C07vrrpStatisticsDiscontinuityTime_Object=MibTableColumn
c07vrrpStatisticsDiscontinuityTime=_C07vrrpStatisticsDiscontinuityTime_Object((1,3,6,1,4,1,9,10,143,2,5,1,11),_C07vrrpStatisticsDiscontinuityTime_Type())
c07vrrpStatisticsDiscontinuityTime.setMaxAccess(_D)
if mibBuilder.loadTexts:c07vrrpStatisticsDiscontinuityTime.setStatus(_B)
_C07vrrpStatisticsRefreshRate_Type=Unsigned32
_C07vrrpStatisticsRefreshRate_Object=MibTableColumn
c07vrrpStatisticsRefreshRate=_C07vrrpStatisticsRefreshRate_Object((1,3,6,1,4,1,9,10,143,2,5,1,12),_C07vrrpStatisticsRefreshRate_Type())
c07vrrpStatisticsRefreshRate.setMaxAccess(_D)
if mibBuilder.loadTexts:c07vrrpStatisticsRefreshRate.setStatus(_B)
if mibBuilder.loadTexts:c07vrrpStatisticsRefreshRate.setUnits('milli-seconds')
_C07vrrpConformance_ObjectIdentity=ObjectIdentity
c07vrrpConformance=_C07vrrpConformance_ObjectIdentity((1,3,6,1,4,1,9,10,143,3))
_C07vrrpMIBCompliances_ObjectIdentity=ObjectIdentity
c07vrrpMIBCompliances=_C07vrrpMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,10,143,3,1))
_C07vrrpMIBGroups_ObjectIdentity=ObjectIdentity
c07vrrpMIBGroups=_C07vrrpMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,10,143,3,2))
c07vrrpOperEntry.registerAugmentions((_A,_n))
c07vrrpRouterStatsEntry.setIndexNames(*c07vrrpOperEntry.getIndexNames())
c07vrrpOperationsEntry.registerAugmentions((_A,_o))
c07vrrpRouterStatisticsEntry.setIndexNames(*c07vrrpOperationsEntry.getIndexNames())
c07vrrpOperGroup=ObjectGroup((1,3,6,1,4,1,9,10,143,3,2,1))
c07vrrpOperGroup.setObjects(*((_A,_p),(_A,_q),(_A,_r),(_A,_s),(_A,_t),(_A,_u),(_A,_v),(_A,_w),(_A,_x),(_A,_y),(_A,_z),(_A,_A0),(_A,_A1),(_A,_A2),(_A,_A3),(_A,_A4),(_A,_A5)))
if mibBuilder.loadTexts:c07vrrpOperGroup.setStatus(_C)
c07vrrpStatsGroup=ObjectGroup((1,3,6,1,4,1,9,10,143,3,2,2))
c07vrrpStatsGroup.setObjects(*((_A,_S),(_A,_T),(_A,_U),(_A,_A6),(_A,_A7),(_A,_A8),(_A,_A9),(_A,_AA),(_A,_AB),(_A,_AC),(_A,_AD),(_A,_AE),(_A,_AF),(_A,_AG),(_A,_AH)))
if mibBuilder.loadTexts:c07vrrpStatsGroup.setStatus(_C)
c07vrrpTrapGroup=ObjectGroup((1,3,6,1,4,1,9,10,143,3,2,3))
c07vrrpTrapGroup.setObjects(*((_A,_V),(_A,_W)))
if mibBuilder.loadTexts:c07vrrpTrapGroup.setStatus(_C)
c07vrrpOperationsGroup=ObjectGroup((1,3,6,1,4,1,9,10,143,3,2,5))
c07vrrpOperationsGroup.setObjects(*((_A,_AI),(_A,_AJ),(_A,_AK),(_A,_AL),(_A,_AM),(_A,_X),(_A,_AN),(_A,_AO),(_A,_AP),(_A,_AQ),(_A,_AR),(_A,_AS),(_A,_AT),(_A,_AU),(_A,_AV),(_A,_AW)))
if mibBuilder.loadTexts:c07vrrpOperationsGroup.setStatus(_B)
c07vrrpStatisticsGroup=ObjectGroup((1,3,6,1,4,1,9,10,143,3,2,6))
c07vrrpStatisticsGroup.setObjects(*((_A,_S),(_A,_T),(_A,_U),(_A,_AX),(_A,_AY),(_A,_AZ),(_A,_Aa),(_A,_Ab),(_A,_Ac),(_A,_Ad),(_A,_Ae),(_A,_Af),(_A,_Ag),(_A,_Ah),(_A,_Ai)))
if mibBuilder.loadTexts:c07vrrpStatisticsGroup.setStatus(_B)
c07vrrpTrapInfoGroup=ObjectGroup((1,3,6,1,4,1,9,10,143,3,2,8))
c07vrrpTrapInfoGroup.setObjects(*((_A,_Y),(_A,_Z)))
if mibBuilder.loadTexts:c07vrrpTrapInfoGroup.setStatus(_B)
c07vrrpTrapNewMaster=NotificationType((1,3,6,1,4,1,9,10,143,0,1))
c07vrrpTrapNewMaster.setObjects(*((_A,_X),(_A,_Z)))
if mibBuilder.loadTexts:c07vrrpTrapNewMaster.setStatus(_B)
c07vrrpTrapAuthFailure=NotificationType((1,3,6,1,4,1,9,10,143,0,2))
c07vrrpTrapAuthFailure.setObjects(*((_A,_V),(_A,_W)))
if mibBuilder.loadTexts:c07vrrpTrapAuthFailure.setStatus(_C)
c07vrrpTrapProtoError=NotificationType((1,3,6,1,4,1,9,10,143,0,3))
c07vrrpTrapProtoError.setObjects((_A,_Y))
if mibBuilder.loadTexts:c07vrrpTrapProtoError.setStatus(_B)
c07vrrpNotificationGroup=NotificationGroup((1,3,6,1,4,1,9,10,143,3,2,4))
c07vrrpNotificationGroup.setObjects((_A,_Aj))
if mibBuilder.loadTexts:c07vrrpNotificationGroup.setStatus(_C)
c07vrrpNotificationsGroup=NotificationGroup((1,3,6,1,4,1,9,10,143,3,2,9))
c07vrrpNotificationsGroup.setObjects(*((_A,_Ak),(_A,_Al)))
if mibBuilder.loadTexts:c07vrrpNotificationsGroup.setStatus(_B)
c07vrrpMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,10,143,3,1,1))
c07vrrpMIBCompliance.setObjects(*((_A,_Am),(_A,_An),(_A,_Ao),(_A,_Ap)))
if mibBuilder.loadTexts:c07vrrpMIBCompliance.setStatus(_C)
c07vrrpModuleFullCompliance=ModuleCompliance((1,3,6,1,4,1,9,10,143,3,1,2))
c07vrrpModuleFullCompliance.setObjects(*((_A,_a),(_A,_b),(_A,_c),(_A,_d)))
if mibBuilder.loadTexts:c07vrrpModuleFullCompliance.setStatus(_B)
c07vrrpModuleReadOnlyCompliance=ModuleCompliance((1,3,6,1,4,1,9,10,143,3,1,3))
c07vrrpModuleReadOnlyCompliance.setObjects(*((_A,_a),(_A,_b),(_A,_c),(_A,_d)))
if mibBuilder.loadTexts:c07vrrpModuleReadOnlyCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'C07VrId':C07VrId,'ciscoVrrp07MIB':ciscoVrrp07MIB,'c07vrrpNotifications':c07vrrpNotifications,_Ak:c07vrrpTrapNewMaster,_Aj:c07vrrpTrapAuthFailure,_Al:c07vrrpTrapProtoError,'c07vrrpOperations':c07vrrpOperations,_p:c07vrrpNodeVersion,_q:c07vrrpNotificationCntl,'c07vrrpOperTable':c07vrrpOperTable,'c07vrrpOperEntry':c07vrrpOperEntry,_P:c07vrrpOperVrId,_r:c07vrrpOperVirtualMacAddr,_s:c07vrrpOperState,_t:c07vrrpOperAdminState,_u:c07vrrpOperPriority,_v:c07vrrpOperIpAddrCount,_w:c07vrrpOperMasterIpAddr,_x:c07vrrpOperPrimaryIpAddr,_y:c07vrrpOperAuthType,_z:c07vrrpOperAuthKey,_A0:c07vrrpOperAdvertisementInterval,_A1:c07vrrpOperPreemptMode,_A2:c07vrrpOperVirtualRouterUpTime,_A3:c07vrrpOperProtocol,_A4:c07vrrpOperRowStatus,'c07vrrpAssoIpAddrTable':c07vrrpAssoIpAddrTable,'c07vrrpAssoIpAddrEntry':c07vrrpAssoIpAddrEntry,_l:c07vrrpAssoIpAddr,_A5:c07vrrpAssoIpAddrRowStatus,_V:c07vrrpTrapPacketSrc,_W:c07vrrpTrapAuthErrorType,'c07vrrpOperationsTable':c07vrrpOperationsTable,'c07vrrpOperationsEntry':c07vrrpOperationsEntry,_Q:c07vrrpOperationsInetAddrType,_R:c07vrrpOperationsVrId,_AK:c07vrrpOperationsVirtualMacAddr,_AL:c07vrrpOperationsState,_AM:c07vrrpOperationsPriority,_AT:c07vrrpOperationsAddrCount,_X:c07vrrpOperationsMasterIpAddr,_AU:c07vrrpOperationsPrimaryIpAddr,_AN:c07vrrpOperationsAdvInterval,_AO:c07vrrpOperationsPreemptMode,_AP:c07vrrpOperationsAcceptMode,_AQ:c07vrrpOperationsUpTime,_AR:c07vrrpOperationsStorageType,_AS:c07vrrpOperationsRowStatus,'c07vrrpAssociatedIpAddrTable':c07vrrpAssociatedIpAddrTable,'c07vrrpAssociatedIpAddrEntry':c07vrrpAssociatedIpAddrEntry,_m:c07vrrpAssociatedIpAddr,_AV:c07vrrpAssociatedStorageType,_AW:c07vrrpAssociatedIpAddrRowStatus,_Z:c07vrrpNewMasterReason,_Y:c07vrrpTrapProtoErrReason,_AI:c07vrrpTrapNewMasterCntl,_AJ:c07vrrpTrapProtoErrorCntl,'c07vrrpStatistics':c07vrrpStatistics,_S:c07vrrpRouterChecksumErrors,_T:c07vrrpRouterVersionErrors,_U:c07vrrpRouterVrIdErrors,'c07vrrpRouterStatsTable':c07vrrpRouterStatsTable,_n:c07vrrpRouterStatsEntry,_A6:c07vrrpStatsBecomeMaster,_A7:c07vrrpStatsAdvertiseRcvd,_A8:c07vrrpStatsAdvertiseIntervalErrors,_A9:c07vrrpStatsAuthFailures,_AA:c07vrrpStatsIpTtlErrors,_AB:c07vrrpStatsPriorityZeroPktsRcvd,_AC:c07vrrpStatsPriorityZeroPktsSent,_AD:c07vrrpStatsInvalidTypePktsRcvd,_AE:c07vrrpStatsAddressListErrors,_AF:c07vrrpStatsInvalidAuthType,_AG:c07vrrpStatsAuthTypeMismatch,_AH:c07vrrpStatsPacketLengthErrors,'c07vrrpRouterStatisticsTable':c07vrrpRouterStatisticsTable,_o:c07vrrpRouterStatisticsEntry,_AX:c07vrrpStatisticsMasterTransitions,_AY:c07vrrpStatisticsRcvdAdvertisements,_AZ:c07vrrpStatisticsAdvIntervalErrors,_Ad:c07vrrpStatisticsIpTtlErrors,_Aa:c07vrrpStatisticsRcvdPriZeroPackets,_Ab:c07vrrpStatisticsSentPriZeroPackets,_Ac:c07vrrpStatisticsRcvdInvalidTypePkts,_Ae:c07vrrpStatisticsAddressListErrors,_Af:c07vrrpStatisticsPacketLengthErrors,_Ag:c07vrrpStatisticsRcvdInvalidAuthentications,_Ah:c07vrrpStatisticsDiscontinuityTime,_Ai:c07vrrpStatisticsRefreshRate,'c07vrrpConformance':c07vrrpConformance,'c07vrrpMIBCompliances':c07vrrpMIBCompliances,'c07vrrpMIBCompliance':c07vrrpMIBCompliance,'c07vrrpModuleFullCompliance':c07vrrpModuleFullCompliance,'c07vrrpModuleReadOnlyCompliance':c07vrrpModuleReadOnlyCompliance,'c07vrrpMIBGroups':c07vrrpMIBGroups,_Am:c07vrrpOperGroup,_An:c07vrrpStatsGroup,_Ao:c07vrrpTrapGroup,_Ap:c07vrrpNotificationGroup,_a:c07vrrpOperationsGroup,_b:c07vrrpStatisticsGroup,_c:c07vrrpTrapInfoGroup,_d:c07vrrpNotificationsGroup})