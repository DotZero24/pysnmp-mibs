_x='vrrpv3ProtoError'
_w='vrrpv3NewMaster'
_v='vrrpv3StatisticsRefreshRate'
_u='vrrpv3StatisticsDiscontinuityTime'
_t='vrrpv3StatisticsPacketLengthErrors'
_s='vrrpv3StatisticsAddressListErrors'
_r='vrrpv3StatisticsIpTtlErrors'
_q='vrrpv3StatisticsRcvdInvalidTypePackets'
_p='vrrpv3StatisticsSentPriZeroPackets'
_o='vrrpv3StatisticsRcvdPriZeroPackets'
_n='vrrpv3StatisticsAdvIntervalErrors'
_m='vrrpv3StatisticsRcvdAdvertisements'
_l='vrrpv3StatisticsMasterTransitions'
_k='vrrpv3RouterVrIdErrors'
_j='vrrpv3RouterVersionErrors'
_i='vrrpv3RouterChecksumErrors'
_h='vrrpv3AssociatedIpAddrRowStatus'
_g='vrrpv3OperationsPrimaryIpAddr'
_f='vrrpv3OperationsAddrCount'
_e='vrrpv3OperationsRowStatus'
_d='vrrpv3OperationsUpTime'
_c='vrrpv3OperationsAcceptMode'
_b='vrrpv3OperationsPreemptMode'
_a='vrrpv3OperationsAdvInterval'
_Z='vrrpv3OperationsPriority'
_Y='vrrpv3OperStatus'
_X='vrrpv3OperationsVirtualMacAddr'
_W='vrrpv3StatisticsEntry'
_V='vrrpv3AssociatedIpAddr'
_U='TimeInterval'
_T='Unsigned32'
_S='InetAddress'
_R='vrrpv3NotificationsGroup'
_Q='vrrpv3InfoGroup'
_P='vrrpv3StatisticsGroup'
_O='vrrpv3OperationsGroup'
_N='vrrpv3OperationsMasterIpAddr'
_M='not-accessible'
_L='vrrpv3OperationsInetAddrType'
_K='vrrpv3OperationsVrId'
_J='TruthValue'
_I='ifIndex'
_H='IF-MIB'
_G='vrrpv3StatisticsProtoErrReason'
_F='vrrpv3StatisticsNewMasterReason'
_E='Integer32'
_D='read-create'
_C='read-only'
_B='current'
_A='CISCOSB-VRRPV3-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ipSpec,=mibBuilder.importSymbols('CISCOSB-IP','ipSpec')
ifIndex,=mibBuilder.importSymbols(_H,_I)
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB',_S,'InetAddressType')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso,mib_2=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_T,'iso','mib-2')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TimeInterval,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention',_U,'TimeStamp',_J)
vrrpv3MIB=ModuleIdentity((1,3,6,1,2,1,68))
if mibBuilder.loadTexts:vrrpv3MIB.setRevisions(('2010-06-09 00:00',))
class Vrrpv3VrIdTC(TextualConvention,Integer32):status=_B;displayHint='d';subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_Vrrpv3Notifications_ObjectIdentity=ObjectIdentity
vrrpv3Notifications=_Vrrpv3Notifications_ObjectIdentity((1,3,6,1,2,1,68,0))
_Vrrpv3Objects_ObjectIdentity=ObjectIdentity
vrrpv3Objects=_Vrrpv3Objects_ObjectIdentity((1,3,6,1,2,1,68,1))
_Vrrpv3Operations_ObjectIdentity=ObjectIdentity
vrrpv3Operations=_Vrrpv3Operations_ObjectIdentity((1,3,6,1,2,1,68,1,1))
_Vrrpv3OperationsTable_Object=MibTable
vrrpv3OperationsTable=_Vrrpv3OperationsTable_Object((1,3,6,1,2,1,68,1,1,1))
if mibBuilder.loadTexts:vrrpv3OperationsTable.setStatus(_B)
_Vrrpv3OperationsEntry_Object=MibTableRow
vrrpv3OperationsEntry=_Vrrpv3OperationsEntry_Object((1,3,6,1,2,1,68,1,1,1,1))
vrrpv3OperationsEntry.setIndexNames((0,_H,_I),(0,_A,_K),(0,_A,_L))
if mibBuilder.loadTexts:vrrpv3OperationsEntry.setStatus(_B)
_Vrrpv3OperationsVrId_Type=Vrrpv3VrIdTC
_Vrrpv3OperationsVrId_Object=MibTableColumn
vrrpv3OperationsVrId=_Vrrpv3OperationsVrId_Object((1,3,6,1,2,1,68,1,1,1,1,1),_Vrrpv3OperationsVrId_Type())
vrrpv3OperationsVrId.setMaxAccess(_M)
if mibBuilder.loadTexts:vrrpv3OperationsVrId.setStatus(_B)
_Vrrpv3OperationsInetAddrType_Type=InetAddressType
_Vrrpv3OperationsInetAddrType_Object=MibTableColumn
vrrpv3OperationsInetAddrType=_Vrrpv3OperationsInetAddrType_Object((1,3,6,1,2,1,68,1,1,1,1,2),_Vrrpv3OperationsInetAddrType_Type())
vrrpv3OperationsInetAddrType.setMaxAccess(_M)
if mibBuilder.loadTexts:vrrpv3OperationsInetAddrType.setStatus(_B)
_Vrrpv3OperationsMasterIpAddr_Type=InetAddress
_Vrrpv3OperationsMasterIpAddr_Object=MibTableColumn
vrrpv3OperationsMasterIpAddr=_Vrrpv3OperationsMasterIpAddr_Object((1,3,6,1,2,1,68,1,1,1,1,3),_Vrrpv3OperationsMasterIpAddr_Type())
vrrpv3OperationsMasterIpAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:vrrpv3OperationsMasterIpAddr.setStatus(_B)
_Vrrpv3OperationsPrimaryIpAddr_Type=InetAddress
_Vrrpv3OperationsPrimaryIpAddr_Object=MibTableColumn
vrrpv3OperationsPrimaryIpAddr=_Vrrpv3OperationsPrimaryIpAddr_Object((1,3,6,1,2,1,68,1,1,1,1,4),_Vrrpv3OperationsPrimaryIpAddr_Type())
vrrpv3OperationsPrimaryIpAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:vrrpv3OperationsPrimaryIpAddr.setStatus(_B)
_Vrrpv3OperationsVirtualMacAddr_Type=MacAddress
_Vrrpv3OperationsVirtualMacAddr_Object=MibTableColumn
vrrpv3OperationsVirtualMacAddr=_Vrrpv3OperationsVirtualMacAddr_Object((1,3,6,1,2,1,68,1,1,1,1,5),_Vrrpv3OperationsVirtualMacAddr_Type())
vrrpv3OperationsVirtualMacAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:vrrpv3OperationsVirtualMacAddr.setStatus(_B)
class _Vrrpv3OperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('initialize',1),('backup',2),('master',3)))
_Vrrpv3OperStatus_Type.__name__=_E
_Vrrpv3OperStatus_Object=MibTableColumn
vrrpv3OperStatus=_Vrrpv3OperStatus_Object((1,3,6,1,2,1,68,1,1,1,1,6),_Vrrpv3OperStatus_Type())
vrrpv3OperStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:vrrpv3OperStatus.setStatus(_B)
class _Vrrpv3OperationsPriority_Type(Unsigned32):defaultValue=100;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_Vrrpv3OperationsPriority_Type.__name__=_T
_Vrrpv3OperationsPriority_Object=MibTableColumn
vrrpv3OperationsPriority=_Vrrpv3OperationsPriority_Object((1,3,6,1,2,1,68,1,1,1,1,7),_Vrrpv3OperationsPriority_Type())
vrrpv3OperationsPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:vrrpv3OperationsPriority.setStatus(_B)
class _Vrrpv3OperationsAddrCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_Vrrpv3OperationsAddrCount_Type.__name__=_E
_Vrrpv3OperationsAddrCount_Object=MibTableColumn
vrrpv3OperationsAddrCount=_Vrrpv3OperationsAddrCount_Object((1,3,6,1,2,1,68,1,1,1,1,8),_Vrrpv3OperationsAddrCount_Type())
vrrpv3OperationsAddrCount.setMaxAccess(_C)
if mibBuilder.loadTexts:vrrpv3OperationsAddrCount.setStatus(_B)
class _Vrrpv3OperationsAdvInterval_Type(TimeInterval):defaultValue=100;subtypeSpec=TimeInterval.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_Vrrpv3OperationsAdvInterval_Type.__name__=_U
_Vrrpv3OperationsAdvInterval_Object=MibTableColumn
vrrpv3OperationsAdvInterval=_Vrrpv3OperationsAdvInterval_Object((1,3,6,1,2,1,68,1,1,1,1,9),_Vrrpv3OperationsAdvInterval_Type())
vrrpv3OperationsAdvInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:vrrpv3OperationsAdvInterval.setStatus(_B)
if mibBuilder.loadTexts:vrrpv3OperationsAdvInterval.setUnits('centiseconds')
class _Vrrpv3OperationsPreemptMode_Type(TruthValue):defaultValue=1
_Vrrpv3OperationsPreemptMode_Type.__name__=_J
_Vrrpv3OperationsPreemptMode_Object=MibTableColumn
vrrpv3OperationsPreemptMode=_Vrrpv3OperationsPreemptMode_Object((1,3,6,1,2,1,68,1,1,1,1,10),_Vrrpv3OperationsPreemptMode_Type())
vrrpv3OperationsPreemptMode.setMaxAccess(_D)
if mibBuilder.loadTexts:vrrpv3OperationsPreemptMode.setStatus(_B)
class _Vrrpv3OperationsAcceptMode_Type(TruthValue):defaultValue=2
_Vrrpv3OperationsAcceptMode_Type.__name__=_J
_Vrrpv3OperationsAcceptMode_Object=MibTableColumn
vrrpv3OperationsAcceptMode=_Vrrpv3OperationsAcceptMode_Object((1,3,6,1,2,1,68,1,1,1,1,11),_Vrrpv3OperationsAcceptMode_Type())
vrrpv3OperationsAcceptMode.setMaxAccess(_D)
if mibBuilder.loadTexts:vrrpv3OperationsAcceptMode.setStatus(_B)
_Vrrpv3OperationsUpTime_Type=TimeStamp
_Vrrpv3OperationsUpTime_Object=MibTableColumn
vrrpv3OperationsUpTime=_Vrrpv3OperationsUpTime_Object((1,3,6,1,2,1,68,1,1,1,1,12),_Vrrpv3OperationsUpTime_Type())
vrrpv3OperationsUpTime.setMaxAccess(_C)
if mibBuilder.loadTexts:vrrpv3OperationsUpTime.setStatus(_B)
_Vrrpv3OperationsRowStatus_Type=RowStatus
_Vrrpv3OperationsRowStatus_Object=MibTableColumn
vrrpv3OperationsRowStatus=_Vrrpv3OperationsRowStatus_Object((1,3,6,1,2,1,68,1,1,1,1,13),_Vrrpv3OperationsRowStatus_Type())
vrrpv3OperationsRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:vrrpv3OperationsRowStatus.setStatus(_B)
_Vrrpv3AssociatedIpAddrTable_Object=MibTable
vrrpv3AssociatedIpAddrTable=_Vrrpv3AssociatedIpAddrTable_Object((1,3,6,1,2,1,68,1,1,2))
if mibBuilder.loadTexts:vrrpv3AssociatedIpAddrTable.setStatus(_B)
_Vrrpv3AssociatedIpAddrEntry_Object=MibTableRow
vrrpv3AssociatedIpAddrEntry=_Vrrpv3AssociatedIpAddrEntry_Object((1,3,6,1,2,1,68,1,1,2,1))
vrrpv3AssociatedIpAddrEntry.setIndexNames((0,_H,_I),(0,_A,_K),(0,_A,_L),(0,_A,_V))
if mibBuilder.loadTexts:vrrpv3AssociatedIpAddrEntry.setStatus(_B)
class _Vrrpv3AssociatedIpAddr_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,0),ValueSizeConstraint(4,4),ValueSizeConstraint(16,16))
_Vrrpv3AssociatedIpAddr_Type.__name__=_S
_Vrrpv3AssociatedIpAddr_Object=MibTableColumn
vrrpv3AssociatedIpAddr=_Vrrpv3AssociatedIpAddr_Object((1,3,6,1,2,1,68,1,1,2,1,1),_Vrrpv3AssociatedIpAddr_Type())
vrrpv3AssociatedIpAddr.setMaxAccess(_M)
if mibBuilder.loadTexts:vrrpv3AssociatedIpAddr.setStatus(_B)
_Vrrpv3AssociatedIpAddrRowStatus_Type=RowStatus
_Vrrpv3AssociatedIpAddrRowStatus_Object=MibTableColumn
vrrpv3AssociatedIpAddrRowStatus=_Vrrpv3AssociatedIpAddrRowStatus_Object((1,3,6,1,2,1,68,1,1,2,1,2),_Vrrpv3AssociatedIpAddrRowStatus_Type())
vrrpv3AssociatedIpAddrRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:vrrpv3AssociatedIpAddrRowStatus.setStatus(_B)
_Vrrpv3Statistics_ObjectIdentity=ObjectIdentity
vrrpv3Statistics=_Vrrpv3Statistics_ObjectIdentity((1,3,6,1,2,1,68,1,2))
_Vrrpv3RouterChecksumErrors_Type=Counter32
_Vrrpv3RouterChecksumErrors_Object=MibScalar
vrrpv3RouterChecksumErrors=_Vrrpv3RouterChecksumErrors_Object((1,3,6,1,2,1,68,1,2,1),_Vrrpv3RouterChecksumErrors_Type())
vrrpv3RouterChecksumErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:vrrpv3RouterChecksumErrors.setStatus(_B)
_Vrrpv3RouterVersionErrors_Type=Counter32
_Vrrpv3RouterVersionErrors_Object=MibScalar
vrrpv3RouterVersionErrors=_Vrrpv3RouterVersionErrors_Object((1,3,6,1,2,1,68,1,2,2),_Vrrpv3RouterVersionErrors_Type())
vrrpv3RouterVersionErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:vrrpv3RouterVersionErrors.setStatus(_B)
_Vrrpv3RouterVrIdErrors_Type=Counter32
_Vrrpv3RouterVrIdErrors_Object=MibScalar
vrrpv3RouterVrIdErrors=_Vrrpv3RouterVrIdErrors_Object((1,3,6,1,2,1,68,1,2,3),_Vrrpv3RouterVrIdErrors_Type())
vrrpv3RouterVrIdErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:vrrpv3RouterVrIdErrors.setStatus(_B)
_Vrrpv3StatisticsTable_Object=MibTable
vrrpv3StatisticsTable=_Vrrpv3StatisticsTable_Object((1,3,6,1,2,1,68,1,2,4))
if mibBuilder.loadTexts:vrrpv3StatisticsTable.setStatus(_B)
_Vrrpv3StatisticsEntry_Object=MibTableRow
vrrpv3StatisticsEntry=_Vrrpv3StatisticsEntry_Object((1,3,6,1,2,1,68,1,2,4,1))
if mibBuilder.loadTexts:vrrpv3StatisticsEntry.setStatus(_B)
_Vrrpv3StatisticsMasterTransitions_Type=Counter32
_Vrrpv3StatisticsMasterTransitions_Object=MibTableColumn
vrrpv3StatisticsMasterTransitions=_Vrrpv3StatisticsMasterTransitions_Object((1,3,6,1,2,1,68,1,2,4,1,1),_Vrrpv3StatisticsMasterTransitions_Type())
vrrpv3StatisticsMasterTransitions.setMaxAccess(_C)
if mibBuilder.loadTexts:vrrpv3StatisticsMasterTransitions.setStatus(_B)
class _Vrrpv3StatisticsNewMasterReason_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('notMaster',0),('priority',1),('preempted',2),('masterNoResponse',3)))
_Vrrpv3StatisticsNewMasterReason_Type.__name__=_E
_Vrrpv3StatisticsNewMasterReason_Object=MibTableColumn
vrrpv3StatisticsNewMasterReason=_Vrrpv3StatisticsNewMasterReason_Object((1,3,6,1,2,1,68,1,2,4,1,2),_Vrrpv3StatisticsNewMasterReason_Type())
vrrpv3StatisticsNewMasterReason.setMaxAccess(_C)
if mibBuilder.loadTexts:vrrpv3StatisticsNewMasterReason.setStatus(_B)
_Vrrpv3StatisticsRcvdAdvertisements_Type=Counter32
_Vrrpv3StatisticsRcvdAdvertisements_Object=MibTableColumn
vrrpv3StatisticsRcvdAdvertisements=_Vrrpv3StatisticsRcvdAdvertisements_Object((1,3,6,1,2,1,68,1,2,4,1,3),_Vrrpv3StatisticsRcvdAdvertisements_Type())
vrrpv3StatisticsRcvdAdvertisements.setMaxAccess(_C)
if mibBuilder.loadTexts:vrrpv3StatisticsRcvdAdvertisements.setStatus(_B)
_Vrrpv3StatisticsAdvIntervalErrors_Type=Counter32
_Vrrpv3StatisticsAdvIntervalErrors_Object=MibTableColumn
vrrpv3StatisticsAdvIntervalErrors=_Vrrpv3StatisticsAdvIntervalErrors_Object((1,3,6,1,2,1,68,1,2,4,1,4),_Vrrpv3StatisticsAdvIntervalErrors_Type())
vrrpv3StatisticsAdvIntervalErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:vrrpv3StatisticsAdvIntervalErrors.setStatus(_B)
_Vrrpv3StatisticsIpTtlErrors_Type=Counter32
_Vrrpv3StatisticsIpTtlErrors_Object=MibTableColumn
vrrpv3StatisticsIpTtlErrors=_Vrrpv3StatisticsIpTtlErrors_Object((1,3,6,1,2,1,68,1,2,4,1,5),_Vrrpv3StatisticsIpTtlErrors_Type())
vrrpv3StatisticsIpTtlErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:vrrpv3StatisticsIpTtlErrors.setStatus(_B)
class _Vrrpv3StatisticsProtoErrReason_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*(('noError',0),('ipTtlError',1),('versionError',2),('checksumError',3),('vrIdError',4)))
_Vrrpv3StatisticsProtoErrReason_Type.__name__=_E
_Vrrpv3StatisticsProtoErrReason_Object=MibTableColumn
vrrpv3StatisticsProtoErrReason=_Vrrpv3StatisticsProtoErrReason_Object((1,3,6,1,2,1,68,1,2,4,1,6),_Vrrpv3StatisticsProtoErrReason_Type())
vrrpv3StatisticsProtoErrReason.setMaxAccess(_C)
if mibBuilder.loadTexts:vrrpv3StatisticsProtoErrReason.setStatus(_B)
_Vrrpv3StatisticsRcvdPriZeroPackets_Type=Counter32
_Vrrpv3StatisticsRcvdPriZeroPackets_Object=MibTableColumn
vrrpv3StatisticsRcvdPriZeroPackets=_Vrrpv3StatisticsRcvdPriZeroPackets_Object((1,3,6,1,2,1,68,1,2,4,1,7),_Vrrpv3StatisticsRcvdPriZeroPackets_Type())
vrrpv3StatisticsRcvdPriZeroPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:vrrpv3StatisticsRcvdPriZeroPackets.setStatus(_B)
_Vrrpv3StatisticsSentPriZeroPackets_Type=Counter32
_Vrrpv3StatisticsSentPriZeroPackets_Object=MibTableColumn
vrrpv3StatisticsSentPriZeroPackets=_Vrrpv3StatisticsSentPriZeroPackets_Object((1,3,6,1,2,1,68,1,2,4,1,8),_Vrrpv3StatisticsSentPriZeroPackets_Type())
vrrpv3StatisticsSentPriZeroPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:vrrpv3StatisticsSentPriZeroPackets.setStatus(_B)
_Vrrpv3StatisticsRcvdInvalidTypePackets_Type=Counter32
_Vrrpv3StatisticsRcvdInvalidTypePackets_Object=MibTableColumn
vrrpv3StatisticsRcvdInvalidTypePackets=_Vrrpv3StatisticsRcvdInvalidTypePackets_Object((1,3,6,1,2,1,68,1,2,4,1,9),_Vrrpv3StatisticsRcvdInvalidTypePackets_Type())
vrrpv3StatisticsRcvdInvalidTypePackets.setMaxAccess(_C)
if mibBuilder.loadTexts:vrrpv3StatisticsRcvdInvalidTypePackets.setStatus(_B)
_Vrrpv3StatisticsAddressListErrors_Type=Counter32
_Vrrpv3StatisticsAddressListErrors_Object=MibTableColumn
vrrpv3StatisticsAddressListErrors=_Vrrpv3StatisticsAddressListErrors_Object((1,3,6,1,2,1,68,1,2,4,1,10),_Vrrpv3StatisticsAddressListErrors_Type())
vrrpv3StatisticsAddressListErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:vrrpv3StatisticsAddressListErrors.setStatus(_B)
_Vrrpv3StatisticsPacketLengthErrors_Type=Counter32
_Vrrpv3StatisticsPacketLengthErrors_Object=MibTableColumn
vrrpv3StatisticsPacketLengthErrors=_Vrrpv3StatisticsPacketLengthErrors_Object((1,3,6,1,2,1,68,1,2,4,1,11),_Vrrpv3StatisticsPacketLengthErrors_Type())
vrrpv3StatisticsPacketLengthErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:vrrpv3StatisticsPacketLengthErrors.setStatus(_B)
_Vrrpv3StatisticsDiscontinuityTime_Type=TimeStamp
_Vrrpv3StatisticsDiscontinuityTime_Object=MibTableColumn
vrrpv3StatisticsDiscontinuityTime=_Vrrpv3StatisticsDiscontinuityTime_Object((1,3,6,1,2,1,68,1,2,4,1,12),_Vrrpv3StatisticsDiscontinuityTime_Type())
vrrpv3StatisticsDiscontinuityTime.setMaxAccess(_C)
if mibBuilder.loadTexts:vrrpv3StatisticsDiscontinuityTime.setStatus(_B)
_Vrrpv3StatisticsRefreshRate_Type=Unsigned32
_Vrrpv3StatisticsRefreshRate_Object=MibTableColumn
vrrpv3StatisticsRefreshRate=_Vrrpv3StatisticsRefreshRate_Object((1,3,6,1,2,1,68,1,2,4,1,13),_Vrrpv3StatisticsRefreshRate_Type())
vrrpv3StatisticsRefreshRate.setMaxAccess(_C)
if mibBuilder.loadTexts:vrrpv3StatisticsRefreshRate.setStatus(_B)
if mibBuilder.loadTexts:vrrpv3StatisticsRefreshRate.setUnits('milli-seconds')
_Vrrpv3Conformance_ObjectIdentity=ObjectIdentity
vrrpv3Conformance=_Vrrpv3Conformance_ObjectIdentity((1,3,6,1,2,1,68,2))
_Vrrpv3Compliances_ObjectIdentity=ObjectIdentity
vrrpv3Compliances=_Vrrpv3Compliances_ObjectIdentity((1,3,6,1,2,1,68,2,1))
_Vrrpv3Groups_ObjectIdentity=ObjectIdentity
vrrpv3Groups=_Vrrpv3Groups_ObjectIdentity((1,3,6,1,2,1,68,2,2))
vrrpv3OperationsEntry.registerAugmentions((_A,_W))
vrrpv3StatisticsEntry.setIndexNames(*vrrpv3OperationsEntry.getIndexNames())
vrrpv3OperationsGroup=ObjectGroup((1,3,6,1,2,1,68,2,2,1))
vrrpv3OperationsGroup.setObjects(*((_A,_X),(_A,_Y),(_A,_Z),(_A,_N),(_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_g),(_A,_h)))
if mibBuilder.loadTexts:vrrpv3OperationsGroup.setStatus(_B)
vrrpv3StatisticsGroup=ObjectGroup((1,3,6,1,2,1,68,2,2,2))
vrrpv3StatisticsGroup.setObjects(*((_A,_i),(_A,_j),(_A,_k),(_A,_l),(_A,_F),(_A,_m),(_A,_n),(_A,_o),(_A,_p),(_A,_q),(_A,_r),(_A,_G),(_A,_s),(_A,_t),(_A,_u),(_A,_v)))
if mibBuilder.loadTexts:vrrpv3StatisticsGroup.setStatus(_B)
vrrpv3InfoGroup=ObjectGroup((1,3,6,1,2,1,68,2,2,3))
vrrpv3InfoGroup.setObjects(*((_A,_G),(_A,_F)))
if mibBuilder.loadTexts:vrrpv3InfoGroup.setStatus(_B)
vrrpv3NewMaster=NotificationType((1,3,6,1,2,1,68,0,1))
vrrpv3NewMaster.setObjects(*((_A,_N),(_A,_F)))
if mibBuilder.loadTexts:vrrpv3NewMaster.setStatus(_B)
vrrpv3ProtoError=NotificationType((1,3,6,1,2,1,68,0,2))
vrrpv3ProtoError.setObjects((_A,_G))
if mibBuilder.loadTexts:vrrpv3ProtoError.setStatus(_B)
vrrpv3NotificationsGroup=NotificationGroup((1,3,6,1,2,1,68,2,2,4))
vrrpv3NotificationsGroup.setObjects(*((_A,_w),(_A,_x)))
if mibBuilder.loadTexts:vrrpv3NotificationsGroup.setStatus(_B)
vrrpv3FullCompliance=ModuleCompliance((1,3,6,1,2,1,68,2,1,1))
vrrpv3FullCompliance.setObjects(*((_A,_O),(_A,_P),(_A,_Q),(_A,_R)))
if mibBuilder.loadTexts:vrrpv3FullCompliance.setStatus(_B)
vrrpv3ReadOnlyCompliance=ModuleCompliance((1,3,6,1,2,1,68,2,1,2))
vrrpv3ReadOnlyCompliance.setObjects(*((_A,_O),(_A,_P),(_A,_Q),(_A,_R)))
if mibBuilder.loadTexts:vrrpv3ReadOnlyCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'Vrrpv3VrIdTC':Vrrpv3VrIdTC,'vrrpv3MIB':vrrpv3MIB,'vrrpv3Notifications':vrrpv3Notifications,_w:vrrpv3NewMaster,_x:vrrpv3ProtoError,'vrrpv3Objects':vrrpv3Objects,'vrrpv3Operations':vrrpv3Operations,'vrrpv3OperationsTable':vrrpv3OperationsTable,'vrrpv3OperationsEntry':vrrpv3OperationsEntry,_K:vrrpv3OperationsVrId,_L:vrrpv3OperationsInetAddrType,_N:vrrpv3OperationsMasterIpAddr,_g:vrrpv3OperationsPrimaryIpAddr,_X:vrrpv3OperationsVirtualMacAddr,_Y:vrrpv3OperStatus,_Z:vrrpv3OperationsPriority,_f:vrrpv3OperationsAddrCount,_a:vrrpv3OperationsAdvInterval,_b:vrrpv3OperationsPreemptMode,_c:vrrpv3OperationsAcceptMode,_d:vrrpv3OperationsUpTime,_e:vrrpv3OperationsRowStatus,'vrrpv3AssociatedIpAddrTable':vrrpv3AssociatedIpAddrTable,'vrrpv3AssociatedIpAddrEntry':vrrpv3AssociatedIpAddrEntry,_V:vrrpv3AssociatedIpAddr,_h:vrrpv3AssociatedIpAddrRowStatus,'vrrpv3Statistics':vrrpv3Statistics,_i:vrrpv3RouterChecksumErrors,_j:vrrpv3RouterVersionErrors,_k:vrrpv3RouterVrIdErrors,'vrrpv3StatisticsTable':vrrpv3StatisticsTable,_W:vrrpv3StatisticsEntry,_l:vrrpv3StatisticsMasterTransitions,_F:vrrpv3StatisticsNewMasterReason,_m:vrrpv3StatisticsRcvdAdvertisements,_n:vrrpv3StatisticsAdvIntervalErrors,_r:vrrpv3StatisticsIpTtlErrors,_G:vrrpv3StatisticsProtoErrReason,_o:vrrpv3StatisticsRcvdPriZeroPackets,_p:vrrpv3StatisticsSentPriZeroPackets,_q:vrrpv3StatisticsRcvdInvalidTypePackets,_s:vrrpv3StatisticsAddressListErrors,_t:vrrpv3StatisticsPacketLengthErrors,_u:vrrpv3StatisticsDiscontinuityTime,_v:vrrpv3StatisticsRefreshRate,'vrrpv3Conformance':vrrpv3Conformance,'vrrpv3Compliances':vrrpv3Compliances,'vrrpv3FullCompliance':vrrpv3FullCompliance,'vrrpv3ReadOnlyCompliance':vrrpv3ReadOnlyCompliance,'vrrpv3Groups':vrrpv3Groups,_O:vrrpv3OperationsGroup,_P:vrrpv3StatisticsGroup,_Q:vrrpv3InfoGroup,_R:vrrpv3NotificationsGroup})