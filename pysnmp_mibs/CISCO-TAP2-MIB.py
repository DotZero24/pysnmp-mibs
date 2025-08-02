_A4='ciscoTap2DebugComplianceGroupRev1'
_A3='ciscoTap2Switchover'
_A2='ciscoTap2StreamDebug'
_A1='ciscoTap2MediationDebug'
_A0='ciscoTap2MediationTimedOut'
_z='ciscoTap2MIBActive'
_y='cTap2DebugUserStatus'
_x='cTap2DebugUserStorageType'
_w='cTap2DebugUserTimeout'
_v='cTap2StreamInterceptHCDrops'
_u='cTap2StreamInterceptedHCPackets'
_t='cTap2MediationCapabilities'
_s='cTap2StreamStatus'
_r='cTap2StreamInterceptDrops'
_q='cTap2StreamInterceptedPackets'
_p='cTap2StreamInterceptEnable'
_o='cTap2StreamType'
_n='cTap2MediationNotificationEnable'
_m='cTap2MediationTransport'
_l='cTap2MediationTimeout'
_k='cTap2MediationRetransmitType'
_j='cTap2MediationDataType'
_i='cTap2MediationDscp'
_h='cTap2MediationRtcpPort'
_g='cTap2MediationSrcInterface'
_f='cTap2MediationDestPort'
_e='cTap2MediationDestAddress'
_d='cTap2MediationDestAddressType'
_c='cTap2MediationNewIndex'
_b='cTap2DebugUserName'
_a='cTap2DebugIndex'
_Z='cTap2StreamIndex'
_Y='rtpNack'
_X='Ctap2Dscp'
_W='StorageType'
_V='SnmpAdminString'
_U='ciscoTap2StreamHCStatsGroup'
_T='deprecated'
_S='cTap2DebugStatus'
_R='cTap2DebugMaxEntries'
_Q='cTap2DebugAge'
_P='cTap2MediationStatus'
_O='TruthValue'
_N='ciscoTap2NotificationGroup'
_M='ciscoTap2MediationCpbComplianceGroup'
_L='ciscoTap2StreamComplianceGroup'
_K='ciscoTap2MediationComplianceGroup'
_J='cTap2DebugStreamId'
_I='not-accessible'
_H='cTap2MediationContentId'
_G='cTap2DebugMessage'
_F='cTap2DebugMediationId'
_E='Integer32'
_D='read-only'
_C='read-create'
_B='current'
_A='CISCO-TAP2-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
InterfaceIndexOrZero,=mibBuilder.importSymbols('IF-MIB','InterfaceIndexOrZero')
InetAddress,InetAddressType,InetPortNumber=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType','InetPortNumber')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_V)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,PhysAddress,RowStatus,StorageType,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','RowStatus',_W,'TextualConvention',_O)
ciscoTap2MIB=ModuleIdentity((1,3,6,1,4,1,9,9,399))
if mibBuilder.loadTexts:ciscoTap2MIB.setRevisions(('2008-09-10 00:00','2007-12-21 00:00','2006-11-27 00:00','2004-03-11 00:00','2004-01-27 00:00'))
class Ctap2Dscp(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
_CiscoTap2MIBNotifs_ObjectIdentity=ObjectIdentity
ciscoTap2MIBNotifs=_CiscoTap2MIBNotifs_ObjectIdentity((1,3,6,1,4,1,9,9,399,0))
_CiscoTap2MIBObjects_ObjectIdentity=ObjectIdentity
ciscoTap2MIBObjects=_CiscoTap2MIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,399,1))
_CTap2MediationGroup_ObjectIdentity=ObjectIdentity
cTap2MediationGroup=_CTap2MediationGroup_ObjectIdentity((1,3,6,1,4,1,9,9,399,1,1))
class _CTap2MediationNewIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_CTap2MediationNewIndex_Type.__name__=_E
_CTap2MediationNewIndex_Object=MibScalar
cTap2MediationNewIndex=_CTap2MediationNewIndex_Object((1,3,6,1,4,1,9,9,399,1,1,1),_CTap2MediationNewIndex_Type())
cTap2MediationNewIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:cTap2MediationNewIndex.setStatus(_B)
_CTap2MediationTable_Object=MibTable
cTap2MediationTable=_CTap2MediationTable_Object((1,3,6,1,4,1,9,9,399,1,1,2))
if mibBuilder.loadTexts:cTap2MediationTable.setStatus(_B)
_CTap2MediationEntry_Object=MibTableRow
cTap2MediationEntry=_CTap2MediationEntry_Object((1,3,6,1,4,1,9,9,399,1,1,2,1))
cTap2MediationEntry.setIndexNames((0,_A,_H))
if mibBuilder.loadTexts:cTap2MediationEntry.setStatus(_B)
class _CTap2MediationContentId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_CTap2MediationContentId_Type.__name__=_E
_CTap2MediationContentId_Object=MibTableColumn
cTap2MediationContentId=_CTap2MediationContentId_Object((1,3,6,1,4,1,9,9,399,1,1,2,1,1),_CTap2MediationContentId_Type())
cTap2MediationContentId.setMaxAccess(_I)
if mibBuilder.loadTexts:cTap2MediationContentId.setStatus(_B)
_CTap2MediationDestAddressType_Type=InetAddressType
_CTap2MediationDestAddressType_Object=MibTableColumn
cTap2MediationDestAddressType=_CTap2MediationDestAddressType_Object((1,3,6,1,4,1,9,9,399,1,1,2,1,2),_CTap2MediationDestAddressType_Type())
cTap2MediationDestAddressType.setMaxAccess(_C)
if mibBuilder.loadTexts:cTap2MediationDestAddressType.setStatus(_B)
_CTap2MediationDestAddress_Type=InetAddress
_CTap2MediationDestAddress_Object=MibTableColumn
cTap2MediationDestAddress=_CTap2MediationDestAddress_Object((1,3,6,1,4,1,9,9,399,1,1,2,1,3),_CTap2MediationDestAddress_Type())
cTap2MediationDestAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:cTap2MediationDestAddress.setStatus(_B)
_CTap2MediationDestPort_Type=InetPortNumber
_CTap2MediationDestPort_Object=MibTableColumn
cTap2MediationDestPort=_CTap2MediationDestPort_Object((1,3,6,1,4,1,9,9,399,1,1,2,1,4),_CTap2MediationDestPort_Type())
cTap2MediationDestPort.setMaxAccess(_C)
if mibBuilder.loadTexts:cTap2MediationDestPort.setStatus(_B)
_CTap2MediationSrcInterface_Type=InterfaceIndexOrZero
_CTap2MediationSrcInterface_Object=MibTableColumn
cTap2MediationSrcInterface=_CTap2MediationSrcInterface_Object((1,3,6,1,4,1,9,9,399,1,1,2,1,5),_CTap2MediationSrcInterface_Type())
cTap2MediationSrcInterface.setMaxAccess(_C)
if mibBuilder.loadTexts:cTap2MediationSrcInterface.setStatus(_B)
_CTap2MediationRtcpPort_Type=InetPortNumber
_CTap2MediationRtcpPort_Object=MibTableColumn
cTap2MediationRtcpPort=_CTap2MediationRtcpPort_Object((1,3,6,1,4,1,9,9,399,1,1,2,1,6),_CTap2MediationRtcpPort_Type())
cTap2MediationRtcpPort.setMaxAccess(_D)
if mibBuilder.loadTexts:cTap2MediationRtcpPort.setStatus(_B)
class _CTap2MediationDscp_Type(Ctap2Dscp):defaultValue=34
_CTap2MediationDscp_Type.__name__=_X
_CTap2MediationDscp_Object=MibTableColumn
cTap2MediationDscp=_CTap2MediationDscp_Object((1,3,6,1,4,1,9,9,399,1,1,2,1,7),_CTap2MediationDscp_Type())
cTap2MediationDscp.setMaxAccess(_C)
if mibBuilder.loadTexts:cTap2MediationDscp.setStatus(_B)
class _CTap2MediationDataType_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,127))
_CTap2MediationDataType_Type.__name__=_E
_CTap2MediationDataType_Object=MibTableColumn
cTap2MediationDataType=_CTap2MediationDataType_Object((1,3,6,1,4,1,9,9,399,1,1,2,1,8),_CTap2MediationDataType_Type())
cTap2MediationDataType.setMaxAccess(_C)
if mibBuilder.loadTexts:cTap2MediationDataType.setStatus(_B)
class _CTap2MediationRetransmitType_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,127))
_CTap2MediationRetransmitType_Type.__name__=_E
_CTap2MediationRetransmitType_Object=MibTableColumn
cTap2MediationRetransmitType=_CTap2MediationRetransmitType_Object((1,3,6,1,4,1,9,9,399,1,1,2,1,9),_CTap2MediationRetransmitType_Type())
cTap2MediationRetransmitType.setMaxAccess(_C)
if mibBuilder.loadTexts:cTap2MediationRetransmitType.setStatus(_B)
_CTap2MediationTimeout_Type=DateAndTime
_CTap2MediationTimeout_Object=MibTableColumn
cTap2MediationTimeout=_CTap2MediationTimeout_Object((1,3,6,1,4,1,9,9,399,1,1,2,1,10),_CTap2MediationTimeout_Type())
cTap2MediationTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:cTap2MediationTimeout.setStatus(_B)
class _CTap2MediationTransport_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('udp',1),(_Y,2),('tcp',3),('sctp',4),('rtp',5)))
_CTap2MediationTransport_Type.__name__=_E
_CTap2MediationTransport_Object=MibTableColumn
cTap2MediationTransport=_CTap2MediationTransport_Object((1,3,6,1,4,1,9,9,399,1,1,2,1,11),_CTap2MediationTransport_Type())
cTap2MediationTransport.setMaxAccess(_C)
if mibBuilder.loadTexts:cTap2MediationTransport.setStatus(_B)
class _CTap2MediationNotificationEnable_Type(TruthValue):defaultValue=1
_CTap2MediationNotificationEnable_Type.__name__=_O
_CTap2MediationNotificationEnable_Object=MibTableColumn
cTap2MediationNotificationEnable=_CTap2MediationNotificationEnable_Object((1,3,6,1,4,1,9,9,399,1,1,2,1,12),_CTap2MediationNotificationEnable_Type())
cTap2MediationNotificationEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:cTap2MediationNotificationEnable.setStatus(_B)
_CTap2MediationStatus_Type=RowStatus
_CTap2MediationStatus_Object=MibTableColumn
cTap2MediationStatus=_CTap2MediationStatus_Object((1,3,6,1,4,1,9,9,399,1,1,2,1,13),_CTap2MediationStatus_Type())
cTap2MediationStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cTap2MediationStatus.setStatus(_B)
class _CTap2MediationCapabilities_Type(Bits):namedValues=NamedValues(*(('ipV4SrcInterface',0),('ipV6SrcInterface',1),('udp',2),(_Y,3),('tcp',4),('sctp',5),('rtp',6)))
_CTap2MediationCapabilities_Type.__name__='Bits'
_CTap2MediationCapabilities_Object=MibScalar
cTap2MediationCapabilities=_CTap2MediationCapabilities_Object((1,3,6,1,4,1,9,9,399,1,1,3),_CTap2MediationCapabilities_Type())
cTap2MediationCapabilities.setMaxAccess(_D)
if mibBuilder.loadTexts:cTap2MediationCapabilities.setStatus(_B)
_CTap2StreamGroup_ObjectIdentity=ObjectIdentity
cTap2StreamGroup=_CTap2StreamGroup_ObjectIdentity((1,3,6,1,4,1,9,9,399,1,2))
_CTap2StreamTable_Object=MibTable
cTap2StreamTable=_CTap2StreamTable_Object((1,3,6,1,4,1,9,9,399,1,2,1))
if mibBuilder.loadTexts:cTap2StreamTable.setStatus(_B)
_CTap2StreamEntry_Object=MibTableRow
cTap2StreamEntry=_CTap2StreamEntry_Object((1,3,6,1,4,1,9,9,399,1,2,1,1))
cTap2StreamEntry.setIndexNames((0,_A,_H),(0,_A,_Z))
if mibBuilder.loadTexts:cTap2StreamEntry.setStatus(_B)
class _CTap2StreamIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_CTap2StreamIndex_Type.__name__=_E
_CTap2StreamIndex_Object=MibTableColumn
cTap2StreamIndex=_CTap2StreamIndex_Object((1,3,6,1,4,1,9,9,399,1,2,1,1,1),_CTap2StreamIndex_Type())
cTap2StreamIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:cTap2StreamIndex.setStatus(_B)
class _CTap2StreamType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('ip',1),('mac',2),('userConnection',3),('msPdsn',4),('mobility',5)))
_CTap2StreamType_Type.__name__=_E
_CTap2StreamType_Object=MibTableColumn
cTap2StreamType=_CTap2StreamType_Object((1,3,6,1,4,1,9,9,399,1,2,1,1,2),_CTap2StreamType_Type())
cTap2StreamType.setMaxAccess(_C)
if mibBuilder.loadTexts:cTap2StreamType.setStatus(_B)
class _CTap2StreamInterceptEnable_Type(TruthValue):defaultValue=2
_CTap2StreamInterceptEnable_Type.__name__=_O
_CTap2StreamInterceptEnable_Object=MibTableColumn
cTap2StreamInterceptEnable=_CTap2StreamInterceptEnable_Object((1,3,6,1,4,1,9,9,399,1,2,1,1,3),_CTap2StreamInterceptEnable_Type())
cTap2StreamInterceptEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:cTap2StreamInterceptEnable.setStatus(_B)
_CTap2StreamInterceptedPackets_Type=Counter32
_CTap2StreamInterceptedPackets_Object=MibTableColumn
cTap2StreamInterceptedPackets=_CTap2StreamInterceptedPackets_Object((1,3,6,1,4,1,9,9,399,1,2,1,1,4),_CTap2StreamInterceptedPackets_Type())
cTap2StreamInterceptedPackets.setMaxAccess(_D)
if mibBuilder.loadTexts:cTap2StreamInterceptedPackets.setStatus(_B)
_CTap2StreamInterceptDrops_Type=Counter32
_CTap2StreamInterceptDrops_Object=MibTableColumn
cTap2StreamInterceptDrops=_CTap2StreamInterceptDrops_Object((1,3,6,1,4,1,9,9,399,1,2,1,1,5),_CTap2StreamInterceptDrops_Type())
cTap2StreamInterceptDrops.setMaxAccess(_D)
if mibBuilder.loadTexts:cTap2StreamInterceptDrops.setStatus(_B)
_CTap2StreamStatus_Type=RowStatus
_CTap2StreamStatus_Object=MibTableColumn
cTap2StreamStatus=_CTap2StreamStatus_Object((1,3,6,1,4,1,9,9,399,1,2,1,1,6),_CTap2StreamStatus_Type())
cTap2StreamStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cTap2StreamStatus.setStatus(_B)
_CTap2StreamInterceptedHCPackets_Type=Counter64
_CTap2StreamInterceptedHCPackets_Object=MibTableColumn
cTap2StreamInterceptedHCPackets=_CTap2StreamInterceptedHCPackets_Object((1,3,6,1,4,1,9,9,399,1,2,1,1,7),_CTap2StreamInterceptedHCPackets_Type())
cTap2StreamInterceptedHCPackets.setMaxAccess(_D)
if mibBuilder.loadTexts:cTap2StreamInterceptedHCPackets.setStatus(_B)
_CTap2StreamInterceptHCDrops_Type=Counter64
_CTap2StreamInterceptHCDrops_Object=MibTableColumn
cTap2StreamInterceptHCDrops=_CTap2StreamInterceptHCDrops_Object((1,3,6,1,4,1,9,9,399,1,2,1,1,8),_CTap2StreamInterceptHCDrops_Type())
cTap2StreamInterceptHCDrops.setMaxAccess(_D)
if mibBuilder.loadTexts:cTap2StreamInterceptHCDrops.setStatus(_B)
_CTap2DebugGroup_ObjectIdentity=ObjectIdentity
cTap2DebugGroup=_CTap2DebugGroup_ObjectIdentity((1,3,6,1,4,1,9,9,399,1,3))
class _CTap2DebugAge_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_CTap2DebugAge_Type.__name__=_E
_CTap2DebugAge_Object=MibScalar
cTap2DebugAge=_CTap2DebugAge_Object((1,3,6,1,4,1,9,9,399,1,3,1),_CTap2DebugAge_Type())
cTap2DebugAge.setMaxAccess(_D)
if mibBuilder.loadTexts:cTap2DebugAge.setStatus(_B)
class _CTap2DebugMaxEntries_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_CTap2DebugMaxEntries_Type.__name__=_E
_CTap2DebugMaxEntries_Object=MibScalar
cTap2DebugMaxEntries=_CTap2DebugMaxEntries_Object((1,3,6,1,4,1,9,9,399,1,3,2),_CTap2DebugMaxEntries_Type())
cTap2DebugMaxEntries.setMaxAccess(_D)
if mibBuilder.loadTexts:cTap2DebugMaxEntries.setStatus(_B)
_CTap2DebugTable_Object=MibTable
cTap2DebugTable=_CTap2DebugTable_Object((1,3,6,1,4,1,9,9,399,1,3,3))
if mibBuilder.loadTexts:cTap2DebugTable.setStatus(_B)
_CTap2DebugEntry_Object=MibTableRow
cTap2DebugEntry=_CTap2DebugEntry_Object((1,3,6,1,4,1,9,9,399,1,3,3,1))
cTap2DebugEntry.setIndexNames((0,_A,_a))
if mibBuilder.loadTexts:cTap2DebugEntry.setStatus(_B)
class _CTap2DebugIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_CTap2DebugIndex_Type.__name__=_E
_CTap2DebugIndex_Object=MibTableColumn
cTap2DebugIndex=_CTap2DebugIndex_Object((1,3,6,1,4,1,9,9,399,1,3,3,1,1),_CTap2DebugIndex_Type())
cTap2DebugIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:cTap2DebugIndex.setStatus(_B)
_CTap2DebugMediationId_Type=Unsigned32
_CTap2DebugMediationId_Object=MibTableColumn
cTap2DebugMediationId=_CTap2DebugMediationId_Object((1,3,6,1,4,1,9,9,399,1,3,3,1,2),_CTap2DebugMediationId_Type())
cTap2DebugMediationId.setMaxAccess(_D)
if mibBuilder.loadTexts:cTap2DebugMediationId.setStatus(_B)
_CTap2DebugStreamId_Type=Unsigned32
_CTap2DebugStreamId_Object=MibTableColumn
cTap2DebugStreamId=_CTap2DebugStreamId_Object((1,3,6,1,4,1,9,9,399,1,3,3,1,3),_CTap2DebugStreamId_Type())
cTap2DebugStreamId.setMaxAccess(_D)
if mibBuilder.loadTexts:cTap2DebugStreamId.setStatus(_B)
_CTap2DebugMessage_Type=SnmpAdminString
_CTap2DebugMessage_Object=MibTableColumn
cTap2DebugMessage=_CTap2DebugMessage_Object((1,3,6,1,4,1,9,9,399,1,3,3,1,4),_CTap2DebugMessage_Type())
cTap2DebugMessage.setMaxAccess(_D)
if mibBuilder.loadTexts:cTap2DebugMessage.setStatus(_B)
_CTap2DebugStatus_Type=RowStatus
_CTap2DebugStatus_Object=MibTableColumn
cTap2DebugStatus=_CTap2DebugStatus_Object((1,3,6,1,4,1,9,9,399,1,3,3,1,5),_CTap2DebugStatus_Type())
cTap2DebugStatus.setMaxAccess('read-write')
if mibBuilder.loadTexts:cTap2DebugStatus.setStatus(_B)
_CTap2DebugUserTable_Object=MibTable
cTap2DebugUserTable=_CTap2DebugUserTable_Object((1,3,6,1,4,1,9,9,399,1,3,4))
if mibBuilder.loadTexts:cTap2DebugUserTable.setStatus(_B)
_CTap2DebugUserEntry_Object=MibTableRow
cTap2DebugUserEntry=_CTap2DebugUserEntry_Object((1,3,6,1,4,1,9,9,399,1,3,4,1))
cTap2DebugUserEntry.setIndexNames((0,_A,_H),(0,_A,_b))
if mibBuilder.loadTexts:cTap2DebugUserEntry.setStatus(_B)
class _CTap2DebugUserName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_CTap2DebugUserName_Type.__name__=_V
_CTap2DebugUserName_Object=MibTableColumn
cTap2DebugUserName=_CTap2DebugUserName_Object((1,3,6,1,4,1,9,9,399,1,3,4,1,1),_CTap2DebugUserName_Type())
cTap2DebugUserName.setMaxAccess(_I)
if mibBuilder.loadTexts:cTap2DebugUserName.setStatus(_B)
_CTap2DebugUserTimeout_Type=DateAndTime
_CTap2DebugUserTimeout_Object=MibTableColumn
cTap2DebugUserTimeout=_CTap2DebugUserTimeout_Object((1,3,6,1,4,1,9,9,399,1,3,4,1,2),_CTap2DebugUserTimeout_Type())
cTap2DebugUserTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:cTap2DebugUserTimeout.setStatus(_B)
class _CTap2DebugUserStorageType_Type(StorageType):defaultValue=2
_CTap2DebugUserStorageType_Type.__name__=_W
_CTap2DebugUserStorageType_Object=MibTableColumn
cTap2DebugUserStorageType=_CTap2DebugUserStorageType_Object((1,3,6,1,4,1,9,9,399,1,3,4,1,3),_CTap2DebugUserStorageType_Type())
cTap2DebugUserStorageType.setMaxAccess(_C)
if mibBuilder.loadTexts:cTap2DebugUserStorageType.setStatus(_B)
_CTap2DebugUserStatus_Type=RowStatus
_CTap2DebugUserStatus_Object=MibTableColumn
cTap2DebugUserStatus=_CTap2DebugUserStatus_Object((1,3,6,1,4,1,9,9,399,1,3,4,1,4),_CTap2DebugUserStatus_Type())
cTap2DebugUserStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cTap2DebugUserStatus.setStatus(_B)
_CiscoTap2MIBConform_ObjectIdentity=ObjectIdentity
ciscoTap2MIBConform=_CiscoTap2MIBConform_ObjectIdentity((1,3,6,1,4,1,9,9,399,2))
_CiscoTap2MIBCompliances_ObjectIdentity=ObjectIdentity
ciscoTap2MIBCompliances=_CiscoTap2MIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,399,2,1))
_CiscoTap2MIBGroups_ObjectIdentity=ObjectIdentity
ciscoTap2MIBGroups=_CiscoTap2MIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,399,2,2))
ciscoTap2MediationComplianceGroup=ObjectGroup((1,3,6,1,4,1,9,9,399,2,2,1))
ciscoTap2MediationComplianceGroup.setObjects(*((_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_g),(_A,_h),(_A,_i),(_A,_j),(_A,_k),(_A,_l),(_A,_m),(_A,_n),(_A,_P)))
if mibBuilder.loadTexts:ciscoTap2MediationComplianceGroup.setStatus(_B)
ciscoTap2StreamComplianceGroup=ObjectGroup((1,3,6,1,4,1,9,9,399,2,2,2))
ciscoTap2StreamComplianceGroup.setObjects(*((_A,_o),(_A,_p),(_A,_q),(_A,_r),(_A,_s)))
if mibBuilder.loadTexts:ciscoTap2StreamComplianceGroup.setStatus(_B)
ciscoTap2MediationCpbComplianceGroup=ObjectGroup((1,3,6,1,4,1,9,9,399,2,2,4))
ciscoTap2MediationCpbComplianceGroup.setObjects((_A,_t))
if mibBuilder.loadTexts:ciscoTap2MediationCpbComplianceGroup.setStatus(_B)
ciscoTap2DebugComplianceGroup=ObjectGroup((1,3,6,1,4,1,9,9,399,2,2,5))
ciscoTap2DebugComplianceGroup.setObjects(*((_A,_Q),(_A,_R),(_A,_F),(_A,_J),(_A,_G),(_A,_S)))
if mibBuilder.loadTexts:ciscoTap2DebugComplianceGroup.setStatus(_T)
ciscoTap2StreamHCStatsGroup=ObjectGroup((1,3,6,1,4,1,9,9,399,2,2,6))
ciscoTap2StreamHCStatsGroup.setObjects(*((_A,_u),(_A,_v)))
if mibBuilder.loadTexts:ciscoTap2StreamHCStatsGroup.setStatus(_B)
ciscoTap2DebugComplianceGroupRev1=ObjectGroup((1,3,6,1,4,1,9,9,399,2,2,7))
ciscoTap2DebugComplianceGroupRev1.setObjects(*((_A,_Q),(_A,_R),(_A,_F),(_A,_J),(_A,_G),(_A,_S),(_A,_w),(_A,_x),(_A,_y)))
if mibBuilder.loadTexts:ciscoTap2DebugComplianceGroupRev1.setStatus(_B)
ciscoTap2MIBActive=NotificationType((1,3,6,1,4,1,9,9,399,0,1))
if mibBuilder.loadTexts:ciscoTap2MIBActive.setStatus(_B)
ciscoTap2MediationTimedOut=NotificationType((1,3,6,1,4,1,9,9,399,0,2))
ciscoTap2MediationTimedOut.setObjects((_A,_P))
if mibBuilder.loadTexts:ciscoTap2MediationTimedOut.setStatus(_B)
ciscoTap2MediationDebug=NotificationType((1,3,6,1,4,1,9,9,399,0,3))
ciscoTap2MediationDebug.setObjects(*((_A,_F),(_A,_G)))
if mibBuilder.loadTexts:ciscoTap2MediationDebug.setStatus(_B)
ciscoTap2StreamDebug=NotificationType((1,3,6,1,4,1,9,9,399,0,4))
ciscoTap2StreamDebug.setObjects(*((_A,_F),(_A,_J),(_A,_G)))
if mibBuilder.loadTexts:ciscoTap2StreamDebug.setStatus(_B)
ciscoTap2Switchover=NotificationType((1,3,6,1,4,1,9,9,399,0,5))
if mibBuilder.loadTexts:ciscoTap2Switchover.setStatus(_B)
ciscoTap2NotificationGroup=NotificationGroup((1,3,6,1,4,1,9,9,399,2,2,3))
ciscoTap2NotificationGroup.setObjects(*((_A,_z),(_A,_A0),(_A,_A1),(_A,_A2),(_A,_A3)))
if mibBuilder.loadTexts:ciscoTap2NotificationGroup.setStatus(_B)
ciscoTap2MIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,399,2,1,1))
ciscoTap2MIBCompliance.setObjects(*((_A,_K),(_A,_L),(_A,_M),(_A,_N)))
if mibBuilder.loadTexts:ciscoTap2MIBCompliance.setStatus(_T)
ciscoTap2MIBComplianceRev2=ModuleCompliance((1,3,6,1,4,1,9,9,399,2,1,2))
ciscoTap2MIBComplianceRev2.setObjects(*((_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_U)))
if mibBuilder.loadTexts:ciscoTap2MIBComplianceRev2.setStatus(_T)
ciscoTap2MIBComplianceRev3=ModuleCompliance((1,3,6,1,4,1,9,9,399,2,1,3))
ciscoTap2MIBComplianceRev3.setObjects(*((_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_U),(_A,_A4)))
if mibBuilder.loadTexts:ciscoTap2MIBComplianceRev3.setStatus(_B)
mibBuilder.exportSymbols(_A,**{_X:Ctap2Dscp,'ciscoTap2MIB':ciscoTap2MIB,'ciscoTap2MIBNotifs':ciscoTap2MIBNotifs,_z:ciscoTap2MIBActive,_A0:ciscoTap2MediationTimedOut,_A1:ciscoTap2MediationDebug,_A2:ciscoTap2StreamDebug,_A3:ciscoTap2Switchover,'ciscoTap2MIBObjects':ciscoTap2MIBObjects,'cTap2MediationGroup':cTap2MediationGroup,_c:cTap2MediationNewIndex,'cTap2MediationTable':cTap2MediationTable,'cTap2MediationEntry':cTap2MediationEntry,_H:cTap2MediationContentId,_d:cTap2MediationDestAddressType,_e:cTap2MediationDestAddress,_f:cTap2MediationDestPort,_g:cTap2MediationSrcInterface,_h:cTap2MediationRtcpPort,_i:cTap2MediationDscp,_j:cTap2MediationDataType,_k:cTap2MediationRetransmitType,_l:cTap2MediationTimeout,_m:cTap2MediationTransport,_n:cTap2MediationNotificationEnable,_P:cTap2MediationStatus,_t:cTap2MediationCapabilities,'cTap2StreamGroup':cTap2StreamGroup,'cTap2StreamTable':cTap2StreamTable,'cTap2StreamEntry':cTap2StreamEntry,_Z:cTap2StreamIndex,_o:cTap2StreamType,_p:cTap2StreamInterceptEnable,_q:cTap2StreamInterceptedPackets,_r:cTap2StreamInterceptDrops,_s:cTap2StreamStatus,_u:cTap2StreamInterceptedHCPackets,_v:cTap2StreamInterceptHCDrops,'cTap2DebugGroup':cTap2DebugGroup,_Q:cTap2DebugAge,_R:cTap2DebugMaxEntries,'cTap2DebugTable':cTap2DebugTable,'cTap2DebugEntry':cTap2DebugEntry,_a:cTap2DebugIndex,_F:cTap2DebugMediationId,_J:cTap2DebugStreamId,_G:cTap2DebugMessage,_S:cTap2DebugStatus,'cTap2DebugUserTable':cTap2DebugUserTable,'cTap2DebugUserEntry':cTap2DebugUserEntry,_b:cTap2DebugUserName,_w:cTap2DebugUserTimeout,_x:cTap2DebugUserStorageType,_y:cTap2DebugUserStatus,'ciscoTap2MIBConform':ciscoTap2MIBConform,'ciscoTap2MIBCompliances':ciscoTap2MIBCompliances,'ciscoTap2MIBCompliance':ciscoTap2MIBCompliance,'ciscoTap2MIBComplianceRev2':ciscoTap2MIBComplianceRev2,'ciscoTap2MIBComplianceRev3':ciscoTap2MIBComplianceRev3,'ciscoTap2MIBGroups':ciscoTap2MIBGroups,_K:ciscoTap2MediationComplianceGroup,_L:ciscoTap2StreamComplianceGroup,_N:ciscoTap2NotificationGroup,_M:ciscoTap2MediationCpbComplianceGroup,'ciscoTap2DebugComplianceGroup':ciscoTap2DebugComplianceGroup,_U:ciscoTap2StreamHCStatsGroup,_A4:ciscoTap2DebugComplianceGroupRev1})