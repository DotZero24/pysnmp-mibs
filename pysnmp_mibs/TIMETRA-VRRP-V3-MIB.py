_y='vrrpTrapProtoError'
_x='vrrpNewMasterReason'
_w='vrrpStatisticsRefreshRate'
_v='vrrpStatisticsDiscontinuityTime'
_u='vrrpStatisticsRcvdInvalidAuthentications'
_t='vrrpStatisticsPacketLengthErrors'
_s='vrrpStatisticsAddressListErrors'
_r='vrrpStatisticsIpTtlErrors'
_q='vrrpStatisticsRcvdInvalidTypePkts'
_p='vrrpStatisticsSentPriZeroPackets'
_o='vrrpStatisticsRcvdPriZeroPackets'
_n='vrrpStatisticsAdvIntervalErrors'
_m='vrrpStatisticsRcvdAdvertisements'
_l='vrrpStatisticsMasterTransitions'
_k='vrrpAssociatedIpAddrRowStatus'
_j='vrrpAssociatedStorageType'
_i='vrrpOperationsPrimaryIpAddr'
_h='vrrpOperationsAddrCount'
_g='vrrpOperationsRowStatus'
_f='vrrpOperationsStorageType'
_e='vrrpOperationsUpTime'
_d='vrrpOperationsAcceptMode'
_c='vrrpOperationsPreemptMode'
_b='vrrpOperationsAdvInterval'
_a='vrrpOperationsMasterIpAddr'
_Z='vrrpOperationsPriority'
_Y='vrrpOperationsState'
_X='vrrpOperationsVirtualMacAddr'
_W='vrrpRouterStatisticsEntry'
_V='vrrpAssociatedIpAddr'
_U='TimeInterval'
_T='Unsigned32'
_S='InetAddress'
_R='vrrpNotifyObjsGroup'
_Q='vrrpNotificationsGroup'
_P='vrrpTrapInfoGroup'
_O='vrrpStatisticsGroup'
_N='vrrpOperationsGroup'
_M='vrrpTrapProtoErrReason'
_L='not-accessible'
_K='vrrpOperationsVrId'
_J='vrrpOperationsInetAddrType'
_I='TruthValue'
_H='StorageType'
_G='ifIndex'
_F='IF-MIB'
_E='Integer32'
_D='read-create'
_C='read-only'
_B='current'
_A='TIMETRA-VRRP-V3-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_F,_G)
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB',_S,'InetAddressType')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_T,'iso')
DisplayString,MacAddress,PhysAddress,RowStatus,StorageType,TextualConvention,TimeInterval,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus',_H,'TextualConvention',_U,'TimeStamp',_I)
timetraSRMIBModules,=mibBuilder.importSymbols('TIMETRA-GLOBAL-MIB','timetraSRMIBModules')
VrId,vrrpMIB,vrrpOperations=mibBuilder.importSymbols('VRRP-MIB','VrId','vrrpMIB','vrrpOperations')
timetraVrrpV3MibModule=ModuleIdentity((1,3,6,1,4,1,6527,1,1,3,57))
if mibBuilder.loadTexts:timetraVrrpV3MibModule.setRevisions(('2009-02-28 00:00','2008-04-28 00:00'))
_VrrpNotifications_ObjectIdentity=ObjectIdentity
vrrpNotifications=_VrrpNotifications_ObjectIdentity((1,3,6,1,2,1,68,0))
_VrrpOperationsTable_Object=MibTable
vrrpOperationsTable=_VrrpOperationsTable_Object((1,3,6,1,2,1,68,1,7))
if mibBuilder.loadTexts:vrrpOperationsTable.setStatus(_B)
_VrrpOperationsEntry_Object=MibTableRow
vrrpOperationsEntry=_VrrpOperationsEntry_Object((1,3,6,1,2,1,68,1,7,1))
vrrpOperationsEntry.setIndexNames((0,_A,_J),(0,_A,_K),(0,_F,_G))
if mibBuilder.loadTexts:vrrpOperationsEntry.setStatus(_B)
_VrrpOperationsInetAddrType_Type=InetAddressType
_VrrpOperationsInetAddrType_Object=MibTableColumn
vrrpOperationsInetAddrType=_VrrpOperationsInetAddrType_Object((1,3,6,1,2,1,68,1,7,1,1),_VrrpOperationsInetAddrType_Type())
vrrpOperationsInetAddrType.setMaxAccess(_L)
if mibBuilder.loadTexts:vrrpOperationsInetAddrType.setStatus(_B)
_VrrpOperationsVrId_Type=VrId
_VrrpOperationsVrId_Object=MibTableColumn
vrrpOperationsVrId=_VrrpOperationsVrId_Object((1,3,6,1,2,1,68,1,7,1,2),_VrrpOperationsVrId_Type())
vrrpOperationsVrId.setMaxAccess(_L)
if mibBuilder.loadTexts:vrrpOperationsVrId.setStatus(_B)
_VrrpOperationsVirtualMacAddr_Type=MacAddress
_VrrpOperationsVirtualMacAddr_Object=MibTableColumn
vrrpOperationsVirtualMacAddr=_VrrpOperationsVirtualMacAddr_Object((1,3,6,1,2,1,68,1,7,1,3),_VrrpOperationsVirtualMacAddr_Type())
vrrpOperationsVirtualMacAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:vrrpOperationsVirtualMacAddr.setStatus(_B)
class _VrrpOperationsState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('initialize',1),('backup',2),('master',3)))
_VrrpOperationsState_Type.__name__=_E
_VrrpOperationsState_Object=MibTableColumn
vrrpOperationsState=_VrrpOperationsState_Object((1,3,6,1,2,1,68,1,7,1,4),_VrrpOperationsState_Type())
vrrpOperationsState.setMaxAccess(_C)
if mibBuilder.loadTexts:vrrpOperationsState.setStatus(_B)
class _VrrpOperationsPriority_Type(Unsigned32):defaultValue=100;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_VrrpOperationsPriority_Type.__name__=_T
_VrrpOperationsPriority_Object=MibTableColumn
vrrpOperationsPriority=_VrrpOperationsPriority_Object((1,3,6,1,2,1,68,1,7,1,5),_VrrpOperationsPriority_Type())
vrrpOperationsPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:vrrpOperationsPriority.setStatus(_B)
class _VrrpOperationsAddrCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_VrrpOperationsAddrCount_Type.__name__=_E
_VrrpOperationsAddrCount_Object=MibTableColumn
vrrpOperationsAddrCount=_VrrpOperationsAddrCount_Object((1,3,6,1,2,1,68,1,7,1,6),_VrrpOperationsAddrCount_Type())
vrrpOperationsAddrCount.setMaxAccess(_C)
if mibBuilder.loadTexts:vrrpOperationsAddrCount.setStatus(_B)
_VrrpOperationsMasterIpAddr_Type=InetAddress
_VrrpOperationsMasterIpAddr_Object=MibTableColumn
vrrpOperationsMasterIpAddr=_VrrpOperationsMasterIpAddr_Object((1,3,6,1,2,1,68,1,7,1,7),_VrrpOperationsMasterIpAddr_Type())
vrrpOperationsMasterIpAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:vrrpOperationsMasterIpAddr.setStatus(_B)
_VrrpOperationsPrimaryIpAddr_Type=InetAddress
_VrrpOperationsPrimaryIpAddr_Object=MibTableColumn
vrrpOperationsPrimaryIpAddr=_VrrpOperationsPrimaryIpAddr_Object((1,3,6,1,2,1,68,1,7,1,8),_VrrpOperationsPrimaryIpAddr_Type())
vrrpOperationsPrimaryIpAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:vrrpOperationsPrimaryIpAddr.setStatus(_B)
class _VrrpOperationsAdvInterval_Type(TimeInterval):defaultValue=100;subtypeSpec=TimeInterval.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_VrrpOperationsAdvInterval_Type.__name__=_U
_VrrpOperationsAdvInterval_Object=MibTableColumn
vrrpOperationsAdvInterval=_VrrpOperationsAdvInterval_Object((1,3,6,1,2,1,68,1,7,1,9),_VrrpOperationsAdvInterval_Type())
vrrpOperationsAdvInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:vrrpOperationsAdvInterval.setStatus(_B)
if mibBuilder.loadTexts:vrrpOperationsAdvInterval.setUnits('centiseconds')
class _VrrpOperationsPreemptMode_Type(TruthValue):defaultValue=1
_VrrpOperationsPreemptMode_Type.__name__=_I
_VrrpOperationsPreemptMode_Object=MibTableColumn
vrrpOperationsPreemptMode=_VrrpOperationsPreemptMode_Object((1,3,6,1,2,1,68,1,7,1,10),_VrrpOperationsPreemptMode_Type())
vrrpOperationsPreemptMode.setMaxAccess(_D)
if mibBuilder.loadTexts:vrrpOperationsPreemptMode.setStatus(_B)
class _VrrpOperationsAcceptMode_Type(TruthValue):defaultValue=2
_VrrpOperationsAcceptMode_Type.__name__=_I
_VrrpOperationsAcceptMode_Object=MibTableColumn
vrrpOperationsAcceptMode=_VrrpOperationsAcceptMode_Object((1,3,6,1,2,1,68,1,7,1,11),_VrrpOperationsAcceptMode_Type())
vrrpOperationsAcceptMode.setMaxAccess(_D)
if mibBuilder.loadTexts:vrrpOperationsAcceptMode.setStatus(_B)
_VrrpOperationsUpTime_Type=TimeStamp
_VrrpOperationsUpTime_Object=MibTableColumn
vrrpOperationsUpTime=_VrrpOperationsUpTime_Object((1,3,6,1,2,1,68,1,7,1,12),_VrrpOperationsUpTime_Type())
vrrpOperationsUpTime.setMaxAccess(_C)
if mibBuilder.loadTexts:vrrpOperationsUpTime.setStatus(_B)
class _VrrpOperationsStorageType_Type(StorageType):defaultValue=3
_VrrpOperationsStorageType_Type.__name__=_H
_VrrpOperationsStorageType_Object=MibTableColumn
vrrpOperationsStorageType=_VrrpOperationsStorageType_Object((1,3,6,1,2,1,68,1,7,1,13),_VrrpOperationsStorageType_Type())
vrrpOperationsStorageType.setMaxAccess(_D)
if mibBuilder.loadTexts:vrrpOperationsStorageType.setStatus(_B)
_VrrpOperationsRowStatus_Type=RowStatus
_VrrpOperationsRowStatus_Object=MibTableColumn
vrrpOperationsRowStatus=_VrrpOperationsRowStatus_Object((1,3,6,1,2,1,68,1,7,1,14),_VrrpOperationsRowStatus_Type())
vrrpOperationsRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:vrrpOperationsRowStatus.setStatus(_B)
_VrrpAssociatedIpAddrTable_Object=MibTable
vrrpAssociatedIpAddrTable=_VrrpAssociatedIpAddrTable_Object((1,3,6,1,2,1,68,1,8))
if mibBuilder.loadTexts:vrrpAssociatedIpAddrTable.setStatus(_B)
_VrrpAssociatedIpAddrEntry_Object=MibTableRow
vrrpAssociatedIpAddrEntry=_VrrpAssociatedIpAddrEntry_Object((1,3,6,1,2,1,68,1,8,1))
vrrpAssociatedIpAddrEntry.setIndexNames((0,_A,_J),(0,_A,_K),(0,_F,_G),(0,_A,_V))
if mibBuilder.loadTexts:vrrpAssociatedIpAddrEntry.setStatus(_B)
class _VrrpAssociatedIpAddr_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,0),ValueSizeConstraint(4,4),ValueSizeConstraint(16,16))
_VrrpAssociatedIpAddr_Type.__name__=_S
_VrrpAssociatedIpAddr_Object=MibTableColumn
vrrpAssociatedIpAddr=_VrrpAssociatedIpAddr_Object((1,3,6,1,2,1,68,1,8,1,1),_VrrpAssociatedIpAddr_Type())
vrrpAssociatedIpAddr.setMaxAccess(_L)
if mibBuilder.loadTexts:vrrpAssociatedIpAddr.setStatus(_B)
class _VrrpAssociatedStorageType_Type(StorageType):defaultValue=3
_VrrpAssociatedStorageType_Type.__name__=_H
_VrrpAssociatedStorageType_Object=MibTableColumn
vrrpAssociatedStorageType=_VrrpAssociatedStorageType_Object((1,3,6,1,2,1,68,1,8,1,2),_VrrpAssociatedStorageType_Type())
vrrpAssociatedStorageType.setMaxAccess(_D)
if mibBuilder.loadTexts:vrrpAssociatedStorageType.setStatus(_B)
_VrrpAssociatedIpAddrRowStatus_Type=RowStatus
_VrrpAssociatedIpAddrRowStatus_Object=MibTableColumn
vrrpAssociatedIpAddrRowStatus=_VrrpAssociatedIpAddrRowStatus_Object((1,3,6,1,2,1,68,1,8,1,3),_VrrpAssociatedIpAddrRowStatus_Type())
vrrpAssociatedIpAddrRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:vrrpAssociatedIpAddrRowStatus.setStatus(_B)
class _VrrpNewMasterReason_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('notmaster',0),('priority',1),('preempted',2),('masterNoResponse',3)))
_VrrpNewMasterReason_Type.__name__=_E
_VrrpNewMasterReason_Object=MibScalar
vrrpNewMasterReason=_VrrpNewMasterReason_Object((1,3,6,1,2,1,68,1,9),_VrrpNewMasterReason_Type())
vrrpNewMasterReason.setMaxAccess(_C)
if mibBuilder.loadTexts:vrrpNewMasterReason.setStatus(_B)
class _VrrpTrapProtoErrReason_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('hopLimitError',0),('versionError',1),('checksumError',2),('vridError',3)))
_VrrpTrapProtoErrReason_Type.__name__=_E
_VrrpTrapProtoErrReason_Object=MibScalar
vrrpTrapProtoErrReason=_VrrpTrapProtoErrReason_Object((1,3,6,1,2,1,68,1,10),_VrrpTrapProtoErrReason_Type())
vrrpTrapProtoErrReason.setMaxAccess('accessible-for-notify')
if mibBuilder.loadTexts:vrrpTrapProtoErrReason.setStatus(_B)
_VrrpStatistics_ObjectIdentity=ObjectIdentity
vrrpStatistics=_VrrpStatistics_ObjectIdentity((1,3,6,1,2,1,68,2))
_VrrpRouterStatisticsTable_Object=MibTable
vrrpRouterStatisticsTable=_VrrpRouterStatisticsTable_Object((1,3,6,1,2,1,68,2,5))
if mibBuilder.loadTexts:vrrpRouterStatisticsTable.setStatus(_B)
_VrrpRouterStatisticsEntry_Object=MibTableRow
vrrpRouterStatisticsEntry=_VrrpRouterStatisticsEntry_Object((1,3,6,1,2,1,68,2,5,1))
if mibBuilder.loadTexts:vrrpRouterStatisticsEntry.setStatus(_B)
_VrrpStatisticsMasterTransitions_Type=Counter32
_VrrpStatisticsMasterTransitions_Object=MibTableColumn
vrrpStatisticsMasterTransitions=_VrrpStatisticsMasterTransitions_Object((1,3,6,1,2,1,68,2,5,1,1),_VrrpStatisticsMasterTransitions_Type())
vrrpStatisticsMasterTransitions.setMaxAccess(_C)
if mibBuilder.loadTexts:vrrpStatisticsMasterTransitions.setStatus(_B)
_VrrpStatisticsRcvdAdvertisements_Type=Counter32
_VrrpStatisticsRcvdAdvertisements_Object=MibTableColumn
vrrpStatisticsRcvdAdvertisements=_VrrpStatisticsRcvdAdvertisements_Object((1,3,6,1,2,1,68,2,5,1,2),_VrrpStatisticsRcvdAdvertisements_Type())
vrrpStatisticsRcvdAdvertisements.setMaxAccess(_C)
if mibBuilder.loadTexts:vrrpStatisticsRcvdAdvertisements.setStatus(_B)
_VrrpStatisticsAdvIntervalErrors_Type=Counter32
_VrrpStatisticsAdvIntervalErrors_Object=MibTableColumn
vrrpStatisticsAdvIntervalErrors=_VrrpStatisticsAdvIntervalErrors_Object((1,3,6,1,2,1,68,2,5,1,3),_VrrpStatisticsAdvIntervalErrors_Type())
vrrpStatisticsAdvIntervalErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:vrrpStatisticsAdvIntervalErrors.setStatus(_B)
_VrrpStatisticsIpTtlErrors_Type=Counter32
_VrrpStatisticsIpTtlErrors_Object=MibTableColumn
vrrpStatisticsIpTtlErrors=_VrrpStatisticsIpTtlErrors_Object((1,3,6,1,2,1,68,2,5,1,4),_VrrpStatisticsIpTtlErrors_Type())
vrrpStatisticsIpTtlErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:vrrpStatisticsIpTtlErrors.setStatus(_B)
_VrrpStatisticsRcvdPriZeroPackets_Type=Counter32
_VrrpStatisticsRcvdPriZeroPackets_Object=MibTableColumn
vrrpStatisticsRcvdPriZeroPackets=_VrrpStatisticsRcvdPriZeroPackets_Object((1,3,6,1,2,1,68,2,5,1,5),_VrrpStatisticsRcvdPriZeroPackets_Type())
vrrpStatisticsRcvdPriZeroPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:vrrpStatisticsRcvdPriZeroPackets.setStatus(_B)
_VrrpStatisticsSentPriZeroPackets_Type=Counter32
_VrrpStatisticsSentPriZeroPackets_Object=MibTableColumn
vrrpStatisticsSentPriZeroPackets=_VrrpStatisticsSentPriZeroPackets_Object((1,3,6,1,2,1,68,2,5,1,6),_VrrpStatisticsSentPriZeroPackets_Type())
vrrpStatisticsSentPriZeroPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:vrrpStatisticsSentPriZeroPackets.setStatus(_B)
_VrrpStatisticsRcvdInvalidTypePkts_Type=Counter32
_VrrpStatisticsRcvdInvalidTypePkts_Object=MibTableColumn
vrrpStatisticsRcvdInvalidTypePkts=_VrrpStatisticsRcvdInvalidTypePkts_Object((1,3,6,1,2,1,68,2,5,1,7),_VrrpStatisticsRcvdInvalidTypePkts_Type())
vrrpStatisticsRcvdInvalidTypePkts.setMaxAccess(_C)
if mibBuilder.loadTexts:vrrpStatisticsRcvdInvalidTypePkts.setStatus(_B)
_VrrpStatisticsAddressListErrors_Type=Counter32
_VrrpStatisticsAddressListErrors_Object=MibTableColumn
vrrpStatisticsAddressListErrors=_VrrpStatisticsAddressListErrors_Object((1,3,6,1,2,1,68,2,5,1,8),_VrrpStatisticsAddressListErrors_Type())
vrrpStatisticsAddressListErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:vrrpStatisticsAddressListErrors.setStatus(_B)
_VrrpStatisticsPacketLengthErrors_Type=Counter32
_VrrpStatisticsPacketLengthErrors_Object=MibTableColumn
vrrpStatisticsPacketLengthErrors=_VrrpStatisticsPacketLengthErrors_Object((1,3,6,1,2,1,68,2,5,1,9),_VrrpStatisticsPacketLengthErrors_Type())
vrrpStatisticsPacketLengthErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:vrrpStatisticsPacketLengthErrors.setStatus(_B)
_VrrpStatisticsRcvdInvalidAuthentications_Type=Counter32
_VrrpStatisticsRcvdInvalidAuthentications_Object=MibTableColumn
vrrpStatisticsRcvdInvalidAuthentications=_VrrpStatisticsRcvdInvalidAuthentications_Object((1,3,6,1,2,1,68,2,5,1,10),_VrrpStatisticsRcvdInvalidAuthentications_Type())
vrrpStatisticsRcvdInvalidAuthentications.setMaxAccess(_C)
if mibBuilder.loadTexts:vrrpStatisticsRcvdInvalidAuthentications.setStatus(_B)
_VrrpStatisticsDiscontinuityTime_Type=TimeStamp
_VrrpStatisticsDiscontinuityTime_Object=MibTableColumn
vrrpStatisticsDiscontinuityTime=_VrrpStatisticsDiscontinuityTime_Object((1,3,6,1,2,1,68,2,5,1,11),_VrrpStatisticsDiscontinuityTime_Type())
vrrpStatisticsDiscontinuityTime.setMaxAccess(_C)
if mibBuilder.loadTexts:vrrpStatisticsDiscontinuityTime.setStatus(_B)
_VrrpStatisticsRefreshRate_Type=Unsigned32
_VrrpStatisticsRefreshRate_Object=MibTableColumn
vrrpStatisticsRefreshRate=_VrrpStatisticsRefreshRate_Object((1,3,6,1,2,1,68,2,5,1,12),_VrrpStatisticsRefreshRate_Type())
vrrpStatisticsRefreshRate.setMaxAccess(_C)
if mibBuilder.loadTexts:vrrpStatisticsRefreshRate.setStatus(_B)
if mibBuilder.loadTexts:vrrpStatisticsRefreshRate.setUnits('milliseconds')
_VrrpConformance_ObjectIdentity=ObjectIdentity
vrrpConformance=_VrrpConformance_ObjectIdentity((1,3,6,1,2,1,68,3))
_VrrpMIBCompliances_ObjectIdentity=ObjectIdentity
vrrpMIBCompliances=_VrrpMIBCompliances_ObjectIdentity((1,3,6,1,2,1,68,3,1))
_VrrpMIBGroups_ObjectIdentity=ObjectIdentity
vrrpMIBGroups=_VrrpMIBGroups_ObjectIdentity((1,3,6,1,2,1,68,3,2))
vrrpOperationsEntry.registerAugmentions((_A,_W))
vrrpRouterStatisticsEntry.setIndexNames(*vrrpOperationsEntry.getIndexNames())
vrrpOperationsGroup=ObjectGroup((1,3,6,1,2,1,68,3,2,5))
vrrpOperationsGroup.setObjects(*((_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_g),(_A,_h),(_A,_i),(_A,_j),(_A,_k)))
if mibBuilder.loadTexts:vrrpOperationsGroup.setStatus(_B)
vrrpStatisticsGroup=ObjectGroup((1,3,6,1,2,1,68,3,2,6))
vrrpStatisticsGroup.setObjects(*((_A,_l),(_A,_m),(_A,_n),(_A,_o),(_A,_p),(_A,_q),(_A,_r),(_A,_s),(_A,_t),(_A,_u),(_A,_v),(_A,_w)))
if mibBuilder.loadTexts:vrrpStatisticsGroup.setStatus(_B)
vrrpTrapInfoGroup=ObjectGroup((1,3,6,1,2,1,68,3,2,7))
vrrpTrapInfoGroup.setObjects((_A,_x))
if mibBuilder.loadTexts:vrrpTrapInfoGroup.setStatus(_B)
vrrpNotifyObjsGroup=ObjectGroup((1,3,6,1,2,1,68,3,2,9))
vrrpNotifyObjsGroup.setObjects((_A,_M))
if mibBuilder.loadTexts:vrrpNotifyObjsGroup.setStatus(_B)
vrrpTrapProtoError=NotificationType((1,3,6,1,2,1,68,0,3))
vrrpTrapProtoError.setObjects((_A,_M))
if mibBuilder.loadTexts:vrrpTrapProtoError.setStatus(_B)
vrrpNotificationsGroup=NotificationGroup((1,3,6,1,2,1,68,3,2,8))
vrrpNotificationsGroup.setObjects((_A,_y))
if mibBuilder.loadTexts:vrrpNotificationsGroup.setStatus(_B)
vrrpModuleFullCompliance=ModuleCompliance((1,3,6,1,2,1,68,3,1,2))
vrrpModuleFullCompliance.setObjects(*((_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R)))
if mibBuilder.loadTexts:vrrpModuleFullCompliance.setStatus(_B)
vrrpModuleReadOnlyCompliance=ModuleCompliance((1,3,6,1,2,1,68,3,1,3))
vrrpModuleReadOnlyCompliance.setObjects(*((_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R)))
if mibBuilder.loadTexts:vrrpModuleReadOnlyCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'vrrpNotifications':vrrpNotifications,_y:vrrpTrapProtoError,'vrrpOperationsTable':vrrpOperationsTable,'vrrpOperationsEntry':vrrpOperationsEntry,_J:vrrpOperationsInetAddrType,_K:vrrpOperationsVrId,_X:vrrpOperationsVirtualMacAddr,_Y:vrrpOperationsState,_Z:vrrpOperationsPriority,_h:vrrpOperationsAddrCount,_a:vrrpOperationsMasterIpAddr,_i:vrrpOperationsPrimaryIpAddr,_b:vrrpOperationsAdvInterval,_c:vrrpOperationsPreemptMode,_d:vrrpOperationsAcceptMode,_e:vrrpOperationsUpTime,_f:vrrpOperationsStorageType,_g:vrrpOperationsRowStatus,'vrrpAssociatedIpAddrTable':vrrpAssociatedIpAddrTable,'vrrpAssociatedIpAddrEntry':vrrpAssociatedIpAddrEntry,_V:vrrpAssociatedIpAddr,_j:vrrpAssociatedStorageType,_k:vrrpAssociatedIpAddrRowStatus,_x:vrrpNewMasterReason,_M:vrrpTrapProtoErrReason,'vrrpStatistics':vrrpStatistics,'vrrpRouterStatisticsTable':vrrpRouterStatisticsTable,_W:vrrpRouterStatisticsEntry,_l:vrrpStatisticsMasterTransitions,_m:vrrpStatisticsRcvdAdvertisements,_n:vrrpStatisticsAdvIntervalErrors,_r:vrrpStatisticsIpTtlErrors,_o:vrrpStatisticsRcvdPriZeroPackets,_p:vrrpStatisticsSentPriZeroPackets,_q:vrrpStatisticsRcvdInvalidTypePkts,_s:vrrpStatisticsAddressListErrors,_t:vrrpStatisticsPacketLengthErrors,_u:vrrpStatisticsRcvdInvalidAuthentications,_v:vrrpStatisticsDiscontinuityTime,_w:vrrpStatisticsRefreshRate,'vrrpConformance':vrrpConformance,'vrrpMIBCompliances':vrrpMIBCompliances,'vrrpModuleFullCompliance':vrrpModuleFullCompliance,'vrrpModuleReadOnlyCompliance':vrrpModuleReadOnlyCompliance,'vrrpMIBGroups':vrrpMIBGroups,_N:vrrpOperationsGroup,_O:vrrpStatisticsGroup,_P:vrrpTrapInfoGroup,_Q:vrrpNotificationsGroup,_R:vrrpNotifyObjsGroup,'timetraVrrpV3MibModule':timetraVrrpV3MibModule})