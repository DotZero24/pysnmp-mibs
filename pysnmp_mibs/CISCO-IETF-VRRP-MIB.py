_A0='cVrrpNotificationProtoError'
_z='cVrrpNotificationNewMaster'
_y='cVrrpStatisticsInvalidAuthType'
_x='cVrrpStatisticsRefreshRate'
_w='cVrrpStatisticsDiscontinuityTime'
_v='cVrrpStatisticsPacketLengthErrors'
_u='cVrrpStatisticsAddressListErrors'
_t='cVrrpStatisticsIpTtlErrors'
_s='cVrrpStatisticsInvldTypePktsRcvd'
_r='cVrrpStatisticsPriZeroPktsSent'
_q='cVrrpStatisticsPriZeroPktsRcvd'
_p='cVrrpStatisticsAdvIntervalErrors'
_o='cVrrpStatisticsAdvertiseRcvd'
_n='cVrrpStatisticsBecomeMaster'
_m='cVrrpRouterVrIdErrors'
_l='cVrrpRouterVersionErrors'
_k='cVrrpRouterChecksumErrors'
_j='cVrrpAssociatedIpAddrRowStatus'
_i='cVrrpOperationsPrimaryIpAddr'
_h='cVrrpOperationsAddrCount'
_g='cVrrpOperationsRowStatus'
_f='cVrrpOperationsUpTime'
_e='cVrrpOperationsAcceptMode'
_d='cVrrpOperationsPreemptMode'
_c='cVrrpOperationsAdvInterval'
_b='cVrrpOperationsVersion'
_a='cVrrpOperationsPriority'
_Z='cVrrpOperationsState'
_Y='cVrrpOperationsVirtualMacAddr'
_X='cVrrpNotificationCntl'
_W='accessible-for-notify'
_V='cVrrpAssociatedIpAddr'
_U='cVrrpAssociatedInetAddrType'
_T='TimeInterval'
_S='InetAddress'
_R='cVrrpNotificationsGroup'
_Q='cVrrpNotificationInfoGroup'
_P='cVrrpStatisticsGroup'
_O='cVrrpOperationsGroup'
_N='cVrrpNotificationProtoErrReason'
_M='cVrrpNotificationNewMasterReason'
_L='cVrrpOperationsMasterIpAddr'
_K='cVrrpOperationsInetAddrType'
_J='TruthValue'
_I='not-accessible'
_H='cVrrpOperationsVrId'
_G='ifIndex'
_F='IF-MIB'
_E='read-create'
_D='Integer32'
_C='read-only'
_B='current'
_A='CISCO-IETF-VRRP-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoExperiment,=mibBuilder.importSymbols('CISCO-SMI','ciscoExperiment')
ifIndex,=mibBuilder.importSymbols(_F,_G)
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB',_S,'InetAddressType')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TimeInterval,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention',_T,'TimeStamp',_J)
ciscoVrrpMIB=ModuleIdentity((1,3,6,1,4,1,9,10,999))
if mibBuilder.loadTexts:ciscoVrrpMIB.setRevisions(('2005-11-17 00:00',))
class CVrId(TextualConvention,Integer32):status=_B;displayHint='d';subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_CVrrpNotifications_ObjectIdentity=ObjectIdentity
cVrrpNotifications=_CVrrpNotifications_ObjectIdentity((1,3,6,1,4,1,9,10,999,0))
_CVrrpOperations_ObjectIdentity=ObjectIdentity
cVrrpOperations=_CVrrpOperations_ObjectIdentity((1,3,6,1,4,1,9,10,999,1))
class _CVrrpNotificationCntl_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),('disabled',2)))
_CVrrpNotificationCntl_Type.__name__=_D
_CVrrpNotificationCntl_Object=MibScalar
cVrrpNotificationCntl=_CVrrpNotificationCntl_Object((1,3,6,1,4,1,9,10,999,1,2),_CVrrpNotificationCntl_Type())
cVrrpNotificationCntl.setMaxAccess('read-write')
if mibBuilder.loadTexts:cVrrpNotificationCntl.setStatus(_B)
_CVrrpOperationsTable_Object=MibTable
cVrrpOperationsTable=_CVrrpOperationsTable_Object((1,3,6,1,4,1,9,10,999,1,7))
if mibBuilder.loadTexts:cVrrpOperationsTable.setStatus(_B)
_CVrrpOperationsEntry_Object=MibTableRow
cVrrpOperationsEntry=_CVrrpOperationsEntry_Object((1,3,6,1,4,1,9,10,999,1,7,1))
cVrrpOperationsEntry.setIndexNames((0,_A,_K),(0,_A,_H),(0,_F,_G))
if mibBuilder.loadTexts:cVrrpOperationsEntry.setStatus(_B)
_CVrrpOperationsInetAddrType_Type=InetAddressType
_CVrrpOperationsInetAddrType_Object=MibTableColumn
cVrrpOperationsInetAddrType=_CVrrpOperationsInetAddrType_Object((1,3,6,1,4,1,9,10,999,1,7,1,1),_CVrrpOperationsInetAddrType_Type())
cVrrpOperationsInetAddrType.setMaxAccess(_I)
if mibBuilder.loadTexts:cVrrpOperationsInetAddrType.setStatus(_B)
_CVrrpOperationsVrId_Type=CVrId
_CVrrpOperationsVrId_Object=MibTableColumn
cVrrpOperationsVrId=_CVrrpOperationsVrId_Object((1,3,6,1,4,1,9,10,999,1,7,1,2),_CVrrpOperationsVrId_Type())
cVrrpOperationsVrId.setMaxAccess(_I)
if mibBuilder.loadTexts:cVrrpOperationsVrId.setStatus(_B)
_CVrrpOperationsVirtualMacAddr_Type=MacAddress
_CVrrpOperationsVirtualMacAddr_Object=MibTableColumn
cVrrpOperationsVirtualMacAddr=_CVrrpOperationsVirtualMacAddr_Object((1,3,6,1,4,1,9,10,999,1,7,1,3),_CVrrpOperationsVirtualMacAddr_Type())
cVrrpOperationsVirtualMacAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:cVrrpOperationsVirtualMacAddr.setStatus(_B)
class _CVrrpOperationsState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('initialize',1),('backup',2),('master',3)))
_CVrrpOperationsState_Type.__name__=_D
_CVrrpOperationsState_Object=MibTableColumn
cVrrpOperationsState=_CVrrpOperationsState_Object((1,3,6,1,4,1,9,10,999,1,7,1,4),_CVrrpOperationsState_Type())
cVrrpOperationsState.setMaxAccess(_C)
if mibBuilder.loadTexts:cVrrpOperationsState.setStatus(_B)
class _CVrrpOperationsPriority_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CVrrpOperationsPriority_Type.__name__=_D
_CVrrpOperationsPriority_Object=MibTableColumn
cVrrpOperationsPriority=_CVrrpOperationsPriority_Object((1,3,6,1,4,1,9,10,999,1,7,1,5),_CVrrpOperationsPriority_Type())
cVrrpOperationsPriority.setMaxAccess(_E)
if mibBuilder.loadTexts:cVrrpOperationsPriority.setStatus(_B)
class _CVrrpOperationsVersion_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('vrrpv2',1),('vrrpv3',2)))
_CVrrpOperationsVersion_Type.__name__=_D
_CVrrpOperationsVersion_Object=MibTableColumn
cVrrpOperationsVersion=_CVrrpOperationsVersion_Object((1,3,6,1,4,1,9,10,999,1,7,1,6),_CVrrpOperationsVersion_Type())
cVrrpOperationsVersion.setMaxAccess(_E)
if mibBuilder.loadTexts:cVrrpOperationsVersion.setStatus(_B)
class _CVrrpOperationsAddrCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CVrrpOperationsAddrCount_Type.__name__=_D
_CVrrpOperationsAddrCount_Object=MibTableColumn
cVrrpOperationsAddrCount=_CVrrpOperationsAddrCount_Object((1,3,6,1,4,1,9,10,999,1,7,1,7),_CVrrpOperationsAddrCount_Type())
cVrrpOperationsAddrCount.setMaxAccess(_C)
if mibBuilder.loadTexts:cVrrpOperationsAddrCount.setStatus(_B)
_CVrrpOperationsMasterIpAddr_Type=InetAddress
_CVrrpOperationsMasterIpAddr_Object=MibTableColumn
cVrrpOperationsMasterIpAddr=_CVrrpOperationsMasterIpAddr_Object((1,3,6,1,4,1,9,10,999,1,7,1,9),_CVrrpOperationsMasterIpAddr_Type())
cVrrpOperationsMasterIpAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:cVrrpOperationsMasterIpAddr.setStatus(_B)
_CVrrpOperationsPrimaryIpAddr_Type=InetAddress
_CVrrpOperationsPrimaryIpAddr_Object=MibTableColumn
cVrrpOperationsPrimaryIpAddr=_CVrrpOperationsPrimaryIpAddr_Object((1,3,6,1,4,1,9,10,999,1,7,1,10),_CVrrpOperationsPrimaryIpAddr_Type())
cVrrpOperationsPrimaryIpAddr.setMaxAccess(_E)
if mibBuilder.loadTexts:cVrrpOperationsPrimaryIpAddr.setStatus(_B)
class _CVrrpOperationsAdvInterval_Type(TimeInterval):defaultValue=100;subtypeSpec=TimeInterval.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4096))
_CVrrpOperationsAdvInterval_Type.__name__=_T
_CVrrpOperationsAdvInterval_Object=MibTableColumn
cVrrpOperationsAdvInterval=_CVrrpOperationsAdvInterval_Object((1,3,6,1,4,1,9,10,999,1,7,1,11),_CVrrpOperationsAdvInterval_Type())
cVrrpOperationsAdvInterval.setMaxAccess(_E)
if mibBuilder.loadTexts:cVrrpOperationsAdvInterval.setStatus(_B)
if mibBuilder.loadTexts:cVrrpOperationsAdvInterval.setUnits('centiseconds')
class _CVrrpOperationsPreemptMode_Type(TruthValue):defaultValue=1
_CVrrpOperationsPreemptMode_Type.__name__=_J
_CVrrpOperationsPreemptMode_Object=MibTableColumn
cVrrpOperationsPreemptMode=_CVrrpOperationsPreemptMode_Object((1,3,6,1,4,1,9,10,999,1,7,1,12),_CVrrpOperationsPreemptMode_Type())
cVrrpOperationsPreemptMode.setMaxAccess(_E)
if mibBuilder.loadTexts:cVrrpOperationsPreemptMode.setStatus(_B)
class _CVrrpOperationsAcceptMode_Type(TruthValue):defaultValue=2
_CVrrpOperationsAcceptMode_Type.__name__=_J
_CVrrpOperationsAcceptMode_Object=MibTableColumn
cVrrpOperationsAcceptMode=_CVrrpOperationsAcceptMode_Object((1,3,6,1,4,1,9,10,999,1,7,1,13),_CVrrpOperationsAcceptMode_Type())
cVrrpOperationsAcceptMode.setMaxAccess(_E)
if mibBuilder.loadTexts:cVrrpOperationsAcceptMode.setStatus(_B)
_CVrrpOperationsUpTime_Type=TimeStamp
_CVrrpOperationsUpTime_Object=MibTableColumn
cVrrpOperationsUpTime=_CVrrpOperationsUpTime_Object((1,3,6,1,4,1,9,10,999,1,7,1,14),_CVrrpOperationsUpTime_Type())
cVrrpOperationsUpTime.setMaxAccess(_C)
if mibBuilder.loadTexts:cVrrpOperationsUpTime.setStatus(_B)
_CVrrpOperationsRowStatus_Type=RowStatus
_CVrrpOperationsRowStatus_Object=MibTableColumn
cVrrpOperationsRowStatus=_CVrrpOperationsRowStatus_Object((1,3,6,1,4,1,9,10,999,1,7,1,15),_CVrrpOperationsRowStatus_Type())
cVrrpOperationsRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:cVrrpOperationsRowStatus.setStatus(_B)
_CVrrpAssociatedIpAddrTable_Object=MibTable
cVrrpAssociatedIpAddrTable=_CVrrpAssociatedIpAddrTable_Object((1,3,6,1,4,1,9,10,999,1,8))
if mibBuilder.loadTexts:cVrrpAssociatedIpAddrTable.setStatus(_B)
_CVrrpAssociatedIpAddrEntry_Object=MibTableRow
cVrrpAssociatedIpAddrEntry=_CVrrpAssociatedIpAddrEntry_Object((1,3,6,1,4,1,9,10,999,1,8,1))
cVrrpAssociatedIpAddrEntry.setIndexNames((0,_A,_U),(0,_A,_H),(0,_F,_G),(0,_A,_V))
if mibBuilder.loadTexts:cVrrpAssociatedIpAddrEntry.setStatus(_B)
_CVrrpAssociatedInetAddrType_Type=InetAddressType
_CVrrpAssociatedInetAddrType_Object=MibTableColumn
cVrrpAssociatedInetAddrType=_CVrrpAssociatedInetAddrType_Object((1,3,6,1,4,1,9,10,999,1,8,1,2),_CVrrpAssociatedInetAddrType_Type())
cVrrpAssociatedInetAddrType.setMaxAccess(_I)
if mibBuilder.loadTexts:cVrrpAssociatedInetAddrType.setStatus(_B)
class _CVrrpAssociatedIpAddr_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,16));fixedLength=16
_CVrrpAssociatedIpAddr_Type.__name__=_S
_CVrrpAssociatedIpAddr_Object=MibTableColumn
cVrrpAssociatedIpAddr=_CVrrpAssociatedIpAddr_Object((1,3,6,1,4,1,9,10,999,1,8,1,3),_CVrrpAssociatedIpAddr_Type())
cVrrpAssociatedIpAddr.setMaxAccess(_I)
if mibBuilder.loadTexts:cVrrpAssociatedIpAddr.setStatus(_B)
_CVrrpAssociatedIpAddrRowStatus_Type=RowStatus
_CVrrpAssociatedIpAddrRowStatus_Object=MibTableColumn
cVrrpAssociatedIpAddrRowStatus=_CVrrpAssociatedIpAddrRowStatus_Object((1,3,6,1,4,1,9,10,999,1,8,1,4),_CVrrpAssociatedIpAddrRowStatus_Type())
cVrrpAssociatedIpAddrRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:cVrrpAssociatedIpAddrRowStatus.setStatus(_B)
class _CVrrpNotificationNewMasterReason_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('priority',0),('preempted',1),('masterNoResponse',2)))
_CVrrpNotificationNewMasterReason_Type.__name__=_D
_CVrrpNotificationNewMasterReason_Object=MibScalar
cVrrpNotificationNewMasterReason=_CVrrpNotificationNewMasterReason_Object((1,3,6,1,4,1,9,10,999,1,9),_CVrrpNotificationNewMasterReason_Type())
cVrrpNotificationNewMasterReason.setMaxAccess(_W)
if mibBuilder.loadTexts:cVrrpNotificationNewMasterReason.setStatus(_B)
class _CVrrpNotificationProtoErrReason_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('hopLimitError',0),('versionError',1),('checksumError',2),('vridError',3)))
_CVrrpNotificationProtoErrReason_Type.__name__=_D
_CVrrpNotificationProtoErrReason_Object=MibScalar
cVrrpNotificationProtoErrReason=_CVrrpNotificationProtoErrReason_Object((1,3,6,1,4,1,9,10,999,1,10),_CVrrpNotificationProtoErrReason_Type())
cVrrpNotificationProtoErrReason.setMaxAccess(_W)
if mibBuilder.loadTexts:cVrrpNotificationProtoErrReason.setStatus(_B)
_CVrrpStatistics_ObjectIdentity=ObjectIdentity
cVrrpStatistics=_CVrrpStatistics_ObjectIdentity((1,3,6,1,4,1,9,10,999,2))
_CVrrpRouterChecksumErrors_Type=Counter32
_CVrrpRouterChecksumErrors_Object=MibScalar
cVrrpRouterChecksumErrors=_CVrrpRouterChecksumErrors_Object((1,3,6,1,4,1,9,10,999,2,1),_CVrrpRouterChecksumErrors_Type())
cVrrpRouterChecksumErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:cVrrpRouterChecksumErrors.setStatus(_B)
_CVrrpRouterVersionErrors_Type=Counter32
_CVrrpRouterVersionErrors_Object=MibScalar
cVrrpRouterVersionErrors=_CVrrpRouterVersionErrors_Object((1,3,6,1,4,1,9,10,999,2,2),_CVrrpRouterVersionErrors_Type())
cVrrpRouterVersionErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:cVrrpRouterVersionErrors.setStatus(_B)
_CVrrpRouterVrIdErrors_Type=Counter32
_CVrrpRouterVrIdErrors_Object=MibScalar
cVrrpRouterVrIdErrors=_CVrrpRouterVrIdErrors_Object((1,3,6,1,4,1,9,10,999,2,3),_CVrrpRouterVrIdErrors_Type())
cVrrpRouterVrIdErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:cVrrpRouterVrIdErrors.setStatus(_B)
_CVrrpRouterStatisticsTable_Object=MibTable
cVrrpRouterStatisticsTable=_CVrrpRouterStatisticsTable_Object((1,3,6,1,4,1,9,10,999,2,5))
if mibBuilder.loadTexts:cVrrpRouterStatisticsTable.setStatus(_B)
_CVrrpRouterStatisticsEntry_Object=MibTableRow
cVrrpRouterStatisticsEntry=_CVrrpRouterStatisticsEntry_Object((1,3,6,1,4,1,9,10,999,2,5,1))
cVrrpRouterStatisticsEntry.setIndexNames((0,_A,_K),(0,_A,_H),(0,_F,_G))
if mibBuilder.loadTexts:cVrrpRouterStatisticsEntry.setStatus(_B)
_CVrrpStatisticsBecomeMaster_Type=Counter32
_CVrrpStatisticsBecomeMaster_Object=MibTableColumn
cVrrpStatisticsBecomeMaster=_CVrrpStatisticsBecomeMaster_Object((1,3,6,1,4,1,9,10,999,2,5,1,1),_CVrrpStatisticsBecomeMaster_Type())
cVrrpStatisticsBecomeMaster.setMaxAccess(_C)
if mibBuilder.loadTexts:cVrrpStatisticsBecomeMaster.setStatus(_B)
_CVrrpStatisticsAdvertiseRcvd_Type=Counter32
_CVrrpStatisticsAdvertiseRcvd_Object=MibTableColumn
cVrrpStatisticsAdvertiseRcvd=_CVrrpStatisticsAdvertiseRcvd_Object((1,3,6,1,4,1,9,10,999,2,5,1,2),_CVrrpStatisticsAdvertiseRcvd_Type())
cVrrpStatisticsAdvertiseRcvd.setMaxAccess(_C)
if mibBuilder.loadTexts:cVrrpStatisticsAdvertiseRcvd.setStatus(_B)
_CVrrpStatisticsAdvIntervalErrors_Type=Counter32
_CVrrpStatisticsAdvIntervalErrors_Object=MibTableColumn
cVrrpStatisticsAdvIntervalErrors=_CVrrpStatisticsAdvIntervalErrors_Object((1,3,6,1,4,1,9,10,999,2,5,1,3),_CVrrpStatisticsAdvIntervalErrors_Type())
cVrrpStatisticsAdvIntervalErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:cVrrpStatisticsAdvIntervalErrors.setStatus(_B)
_CVrrpStatisticsIpTtlErrors_Type=Counter32
_CVrrpStatisticsIpTtlErrors_Object=MibTableColumn
cVrrpStatisticsIpTtlErrors=_CVrrpStatisticsIpTtlErrors_Object((1,3,6,1,4,1,9,10,999,2,5,1,4),_CVrrpStatisticsIpTtlErrors_Type())
cVrrpStatisticsIpTtlErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:cVrrpStatisticsIpTtlErrors.setStatus(_B)
_CVrrpStatisticsPriZeroPktsRcvd_Type=Counter32
_CVrrpStatisticsPriZeroPktsRcvd_Object=MibTableColumn
cVrrpStatisticsPriZeroPktsRcvd=_CVrrpStatisticsPriZeroPktsRcvd_Object((1,3,6,1,4,1,9,10,999,2,5,1,5),_CVrrpStatisticsPriZeroPktsRcvd_Type())
cVrrpStatisticsPriZeroPktsRcvd.setMaxAccess(_C)
if mibBuilder.loadTexts:cVrrpStatisticsPriZeroPktsRcvd.setStatus(_B)
_CVrrpStatisticsPriZeroPktsSent_Type=Counter32
_CVrrpStatisticsPriZeroPktsSent_Object=MibTableColumn
cVrrpStatisticsPriZeroPktsSent=_CVrrpStatisticsPriZeroPktsSent_Object((1,3,6,1,4,1,9,10,999,2,5,1,6),_CVrrpStatisticsPriZeroPktsSent_Type())
cVrrpStatisticsPriZeroPktsSent.setMaxAccess(_C)
if mibBuilder.loadTexts:cVrrpStatisticsPriZeroPktsSent.setStatus(_B)
_CVrrpStatisticsInvldTypePktsRcvd_Type=Counter32
_CVrrpStatisticsInvldTypePktsRcvd_Object=MibTableColumn
cVrrpStatisticsInvldTypePktsRcvd=_CVrrpStatisticsInvldTypePktsRcvd_Object((1,3,6,1,4,1,9,10,999,2,5,1,7),_CVrrpStatisticsInvldTypePktsRcvd_Type())
cVrrpStatisticsInvldTypePktsRcvd.setMaxAccess(_C)
if mibBuilder.loadTexts:cVrrpStatisticsInvldTypePktsRcvd.setStatus(_B)
_CVrrpStatisticsAddressListErrors_Type=Counter32
_CVrrpStatisticsAddressListErrors_Object=MibTableColumn
cVrrpStatisticsAddressListErrors=_CVrrpStatisticsAddressListErrors_Object((1,3,6,1,4,1,9,10,999,2,5,1,8),_CVrrpStatisticsAddressListErrors_Type())
cVrrpStatisticsAddressListErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:cVrrpStatisticsAddressListErrors.setStatus(_B)
_CVrrpStatisticsPacketLengthErrors_Type=Counter32
_CVrrpStatisticsPacketLengthErrors_Object=MibTableColumn
cVrrpStatisticsPacketLengthErrors=_CVrrpStatisticsPacketLengthErrors_Object((1,3,6,1,4,1,9,10,999,2,5,1,11),_CVrrpStatisticsPacketLengthErrors_Type())
cVrrpStatisticsPacketLengthErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:cVrrpStatisticsPacketLengthErrors.setStatus(_B)
_CVrrpStatisticsDiscontinuityTime_Type=TimeStamp
_CVrrpStatisticsDiscontinuityTime_Object=MibTableColumn
cVrrpStatisticsDiscontinuityTime=_CVrrpStatisticsDiscontinuityTime_Object((1,3,6,1,4,1,9,10,999,2,5,1,12),_CVrrpStatisticsDiscontinuityTime_Type())
cVrrpStatisticsDiscontinuityTime.setMaxAccess(_C)
if mibBuilder.loadTexts:cVrrpStatisticsDiscontinuityTime.setStatus(_B)
_CVrrpStatisticsRefreshRate_Type=Unsigned32
_CVrrpStatisticsRefreshRate_Object=MibTableColumn
cVrrpStatisticsRefreshRate=_CVrrpStatisticsRefreshRate_Object((1,3,6,1,4,1,9,10,999,2,5,1,13),_CVrrpStatisticsRefreshRate_Type())
cVrrpStatisticsRefreshRate.setMaxAccess(_C)
if mibBuilder.loadTexts:cVrrpStatisticsRefreshRate.setStatus(_B)
if mibBuilder.loadTexts:cVrrpStatisticsRefreshRate.setUnits('milli-seconds')
_CVrrpStatisticsInvalidAuthType_Type=Counter32
_CVrrpStatisticsInvalidAuthType_Object=MibTableColumn
cVrrpStatisticsInvalidAuthType=_CVrrpStatisticsInvalidAuthType_Object((1,3,6,1,4,1,9,10,999,2,5,1,14),_CVrrpStatisticsInvalidAuthType_Type())
cVrrpStatisticsInvalidAuthType.setMaxAccess(_C)
if mibBuilder.loadTexts:cVrrpStatisticsInvalidAuthType.setStatus(_B)
_CVrrpConformance_ObjectIdentity=ObjectIdentity
cVrrpConformance=_CVrrpConformance_ObjectIdentity((1,3,6,1,4,1,9,10,999,3))
_CVrrpMIBCompliances_ObjectIdentity=ObjectIdentity
cVrrpMIBCompliances=_CVrrpMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,10,999,3,1))
_CVrrpMIBGroups_ObjectIdentity=ObjectIdentity
cVrrpMIBGroups=_CVrrpMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,10,999,3,2))
cVrrpOperationsGroup=ObjectGroup((1,3,6,1,4,1,9,10,999,3,2,5))
cVrrpOperationsGroup.setObjects(*((_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_L),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_g),(_A,_h),(_A,_i),(_A,_j)))
if mibBuilder.loadTexts:cVrrpOperationsGroup.setStatus(_B)
cVrrpStatisticsGroup=ObjectGroup((1,3,6,1,4,1,9,10,999,3,2,6))
cVrrpStatisticsGroup.setObjects(*((_A,_k),(_A,_l),(_A,_m),(_A,_n),(_A,_o),(_A,_p),(_A,_q),(_A,_r),(_A,_s),(_A,_t),(_A,_u),(_A,_v),(_A,_w),(_A,_x),(_A,_y)))
if mibBuilder.loadTexts:cVrrpStatisticsGroup.setStatus(_B)
cVrrpNotificationInfoGroup=ObjectGroup((1,3,6,1,4,1,9,10,999,3,2,8))
cVrrpNotificationInfoGroup.setObjects(*((_A,_M),(_A,_N)))
if mibBuilder.loadTexts:cVrrpNotificationInfoGroup.setStatus(_B)
cVrrpNotificationNewMaster=NotificationType((1,3,6,1,4,1,9,10,999,0,1))
cVrrpNotificationNewMaster.setObjects(*((_A,_L),(_A,_M)))
if mibBuilder.loadTexts:cVrrpNotificationNewMaster.setStatus(_B)
cVrrpNotificationProtoError=NotificationType((1,3,6,1,4,1,9,10,999,0,3))
cVrrpNotificationProtoError.setObjects((_A,_N))
if mibBuilder.loadTexts:cVrrpNotificationProtoError.setStatus(_B)
cVrrpNotificationsGroup=NotificationGroup((1,3,6,1,4,1,9,10,999,3,2,9))
cVrrpNotificationsGroup.setObjects(*((_A,_z),(_A,_A0)))
if mibBuilder.loadTexts:cVrrpNotificationsGroup.setStatus(_B)
cVrrpMIBCompliance2=ModuleCompliance((1,3,6,1,4,1,9,10,999,3,1,2))
cVrrpMIBCompliance2.setObjects(*((_A,_O),(_A,_P),(_A,_Q),(_A,_R)))
if mibBuilder.loadTexts:cVrrpMIBCompliance2.setStatus(_B)
cVrrpMIBReadOnlyCompliance=ModuleCompliance((1,3,6,1,4,1,9,10,999,3,1,3))
cVrrpMIBReadOnlyCompliance.setObjects(*((_A,_O),(_A,_P),(_A,_Q),(_A,_R)))
if mibBuilder.loadTexts:cVrrpMIBReadOnlyCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'CVrId':CVrId,'ciscoVrrpMIB':ciscoVrrpMIB,'cVrrpNotifications':cVrrpNotifications,_z:cVrrpNotificationNewMaster,_A0:cVrrpNotificationProtoError,'cVrrpOperations':cVrrpOperations,_X:cVrrpNotificationCntl,'cVrrpOperationsTable':cVrrpOperationsTable,'cVrrpOperationsEntry':cVrrpOperationsEntry,_K:cVrrpOperationsInetAddrType,_H:cVrrpOperationsVrId,_Y:cVrrpOperationsVirtualMacAddr,_Z:cVrrpOperationsState,_a:cVrrpOperationsPriority,_b:cVrrpOperationsVersion,_h:cVrrpOperationsAddrCount,_L:cVrrpOperationsMasterIpAddr,_i:cVrrpOperationsPrimaryIpAddr,_c:cVrrpOperationsAdvInterval,_d:cVrrpOperationsPreemptMode,_e:cVrrpOperationsAcceptMode,_f:cVrrpOperationsUpTime,_g:cVrrpOperationsRowStatus,'cVrrpAssociatedIpAddrTable':cVrrpAssociatedIpAddrTable,'cVrrpAssociatedIpAddrEntry':cVrrpAssociatedIpAddrEntry,_U:cVrrpAssociatedInetAddrType,_V:cVrrpAssociatedIpAddr,_j:cVrrpAssociatedIpAddrRowStatus,_M:cVrrpNotificationNewMasterReason,_N:cVrrpNotificationProtoErrReason,'cVrrpStatistics':cVrrpStatistics,_k:cVrrpRouterChecksumErrors,_l:cVrrpRouterVersionErrors,_m:cVrrpRouterVrIdErrors,'cVrrpRouterStatisticsTable':cVrrpRouterStatisticsTable,'cVrrpRouterStatisticsEntry':cVrrpRouterStatisticsEntry,_n:cVrrpStatisticsBecomeMaster,_o:cVrrpStatisticsAdvertiseRcvd,_p:cVrrpStatisticsAdvIntervalErrors,_t:cVrrpStatisticsIpTtlErrors,_q:cVrrpStatisticsPriZeroPktsRcvd,_r:cVrrpStatisticsPriZeroPktsSent,_s:cVrrpStatisticsInvldTypePktsRcvd,_u:cVrrpStatisticsAddressListErrors,_v:cVrrpStatisticsPacketLengthErrors,_w:cVrrpStatisticsDiscontinuityTime,_x:cVrrpStatisticsRefreshRate,_y:cVrrpStatisticsInvalidAuthType,'cVrrpConformance':cVrrpConformance,'cVrrpMIBCompliances':cVrrpMIBCompliances,'cVrrpMIBCompliance2':cVrrpMIBCompliance2,'cVrrpMIBReadOnlyCompliance':cVrrpMIBReadOnlyCompliance,'cVrrpMIBGroups':cVrrpMIBGroups,_O:cVrrpOperationsGroup,_P:cVrrpStatisticsGroup,_Q:cVrrpNotificationInfoGroup,_R:cVrrpNotificationsGroup})