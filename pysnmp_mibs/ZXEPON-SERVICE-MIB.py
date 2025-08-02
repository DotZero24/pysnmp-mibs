_R='dot3QueueSetIndex'
_Q='dot3QueueSetQueueIndex'
_P='dot3QueueIndex'
_O='octets'
_N='not-accessible'
_M='unknown'
_L='ZXEPON-SERVICE-MIB'
_K='TQ (16nsec)'
_J='TruthValue'
_I='Integer32'
_H='0.1 dbm'
_G='Unsigned32'
_F='ifIndex'
_E='IF-MIB'
_D='read-write'
_C='frames'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_E,_F)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_I,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_G,'iso')
DisplayString,MacAddress,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','TextualConvention',_J)
zxAnEponMib,=mibBuilder.importSymbols('ZTE-MASTER-MIB','zxAnEponMib')
_Dot3MpcpObjects_ObjectIdentity=ObjectIdentity
dot3MpcpObjects=_Dot3MpcpObjects_ObjectIdentity((1,3,6,1,4,1,3902,1015,1010,1,2))
_Dot3MpcpControlTable_Object=MibTable
dot3MpcpControlTable=_Dot3MpcpControlTable_Object((1,3,6,1,4,1,3902,1015,1010,1,2,1))
if mibBuilder.loadTexts:dot3MpcpControlTable.setStatus(_A)
_Dot3MpcpControlEntry_Object=MibTableRow
dot3MpcpControlEntry=_Dot3MpcpControlEntry_Object((1,3,6,1,4,1,3902,1015,1010,1,2,1,1))
dot3MpcpControlEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:dot3MpcpControlEntry.setStatus(_A)
_Dot3MpcpOperStatus_Type=TruthValue
_Dot3MpcpOperStatus_Object=MibTableColumn
dot3MpcpOperStatus=_Dot3MpcpOperStatus_Object((1,3,6,1,4,1,3902,1015,1010,1,2,1,1,1),_Dot3MpcpOperStatus_Type())
dot3MpcpOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:dot3MpcpOperStatus.setStatus(_A)
class _Dot3MpcpAdminState_Type(TruthValue):defaultValue=2
_Dot3MpcpAdminState_Type.__name__=_J
_Dot3MpcpAdminState_Object=MibTableColumn
dot3MpcpAdminState=_Dot3MpcpAdminState_Object((1,3,6,1,4,1,3902,1015,1010,1,2,1,1,2),_Dot3MpcpAdminState_Type())
dot3MpcpAdminState.setMaxAccess(_D)
if mibBuilder.loadTexts:dot3MpcpAdminState.setStatus(_A)
class _Dot3MpcpMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('olt',1),('onu',2)))
_Dot3MpcpMode_Type.__name__=_I
_Dot3MpcpMode_Object=MibTableColumn
dot3MpcpMode=_Dot3MpcpMode_Object((1,3,6,1,4,1,3902,1015,1010,1,2,1,1,3),_Dot3MpcpMode_Type())
dot3MpcpMode.setMaxAccess(_B)
if mibBuilder.loadTexts:dot3MpcpMode.setStatus(_A)
_Dot3MpcpSyncTime_Type=Unsigned32
_Dot3MpcpSyncTime_Object=MibTableColumn
dot3MpcpSyncTime=_Dot3MpcpSyncTime_Object((1,3,6,1,4,1,3902,1015,1010,1,2,1,1,4),_Dot3MpcpSyncTime_Type())
dot3MpcpSyncTime.setMaxAccess(_B)
if mibBuilder.loadTexts:dot3MpcpSyncTime.setStatus(_A)
if mibBuilder.loadTexts:dot3MpcpSyncTime.setUnits(_K)
_Dot3MpcpLinkID_Type=Unsigned32
_Dot3MpcpLinkID_Object=MibTableColumn
dot3MpcpLinkID=_Dot3MpcpLinkID_Object((1,3,6,1,4,1,3902,1015,1010,1,2,1,1,5),_Dot3MpcpLinkID_Type())
dot3MpcpLinkID.setMaxAccess(_B)
if mibBuilder.loadTexts:dot3MpcpLinkID.setStatus(_A)
_Dot3MpcpRemoteMACAddress_Type=MacAddress
_Dot3MpcpRemoteMACAddress_Object=MibTableColumn
dot3MpcpRemoteMACAddress=_Dot3MpcpRemoteMACAddress_Object((1,3,6,1,4,1,3902,1015,1010,1,2,1,1,6),_Dot3MpcpRemoteMACAddress_Type())
dot3MpcpRemoteMACAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:dot3MpcpRemoteMACAddress.setStatus(_A)
class _Dot3MpcpRegistrationState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('unregistered',1),('registering',2),('registered',3)))
_Dot3MpcpRegistrationState_Type.__name__=_I
_Dot3MpcpRegistrationState_Object=MibTableColumn
dot3MpcpRegistrationState=_Dot3MpcpRegistrationState_Object((1,3,6,1,4,1,3902,1015,1010,1,2,1,1,7),_Dot3MpcpRegistrationState_Type())
dot3MpcpRegistrationState.setMaxAccess(_B)
if mibBuilder.loadTexts:dot3MpcpRegistrationState.setStatus(_A)
_Dot3MpcpTransmitElapsed_Type=Unsigned32
_Dot3MpcpTransmitElapsed_Object=MibTableColumn
dot3MpcpTransmitElapsed=_Dot3MpcpTransmitElapsed_Object((1,3,6,1,4,1,3902,1015,1010,1,2,1,1,8),_Dot3MpcpTransmitElapsed_Type())
dot3MpcpTransmitElapsed.setMaxAccess(_B)
if mibBuilder.loadTexts:dot3MpcpTransmitElapsed.setStatus(_A)
if mibBuilder.loadTexts:dot3MpcpTransmitElapsed.setUnits(_K)
_Dot3MpcpReceiveElapsed_Type=Unsigned32
_Dot3MpcpReceiveElapsed_Object=MibTableColumn
dot3MpcpReceiveElapsed=_Dot3MpcpReceiveElapsed_Object((1,3,6,1,4,1,3902,1015,1010,1,2,1,1,9),_Dot3MpcpReceiveElapsed_Type())
dot3MpcpReceiveElapsed.setMaxAccess(_B)
if mibBuilder.loadTexts:dot3MpcpReceiveElapsed.setStatus(_A)
if mibBuilder.loadTexts:dot3MpcpReceiveElapsed.setUnits(_K)
class _Dot3MpcpRoundTripTime_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Dot3MpcpRoundTripTime_Type.__name__=_G
_Dot3MpcpRoundTripTime_Object=MibTableColumn
dot3MpcpRoundTripTime=_Dot3MpcpRoundTripTime_Object((1,3,6,1,4,1,3902,1015,1010,1,2,1,1,10),_Dot3MpcpRoundTripTime_Type())
dot3MpcpRoundTripTime.setMaxAccess(_B)
if mibBuilder.loadTexts:dot3MpcpRoundTripTime.setStatus(_A)
if mibBuilder.loadTexts:dot3MpcpRoundTripTime.setUnits(_K)
class _Dot3MpcpMaximumPendingGrants_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_Dot3MpcpMaximumPendingGrants_Type.__name__=_G
_Dot3MpcpMaximumPendingGrants_Object=MibTableColumn
dot3MpcpMaximumPendingGrants=_Dot3MpcpMaximumPendingGrants_Object((1,3,6,1,4,1,3902,1015,1010,1,2,1,1,11),_Dot3MpcpMaximumPendingGrants_Type())
dot3MpcpMaximumPendingGrants.setMaxAccess(_B)
if mibBuilder.loadTexts:dot3MpcpMaximumPendingGrants.setStatus(_A)
_Dot3MpcpStatTable_Object=MibTable
dot3MpcpStatTable=_Dot3MpcpStatTable_Object((1,3,6,1,4,1,3902,1015,1010,1,2,2))
if mibBuilder.loadTexts:dot3MpcpStatTable.setStatus(_A)
_Dot3MpcpStatEntry_Object=MibTableRow
dot3MpcpStatEntry=_Dot3MpcpStatEntry_Object((1,3,6,1,4,1,3902,1015,1010,1,2,2,1))
dot3MpcpStatEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:dot3MpcpStatEntry.setStatus(_A)
_Dot3MpcpMACCtrlFramesTransmitted_Type=Counter64
_Dot3MpcpMACCtrlFramesTransmitted_Object=MibTableColumn
dot3MpcpMACCtrlFramesTransmitted=_Dot3MpcpMACCtrlFramesTransmitted_Object((1,3,6,1,4,1,3902,1015,1010,1,2,2,1,1),_Dot3MpcpMACCtrlFramesTransmitted_Type())
dot3MpcpMACCtrlFramesTransmitted.setMaxAccess(_B)
if mibBuilder.loadTexts:dot3MpcpMACCtrlFramesTransmitted.setStatus(_A)
if mibBuilder.loadTexts:dot3MpcpMACCtrlFramesTransmitted.setUnits(_C)
_Dot3MpcpMACCtrlFramesReceived_Type=Counter64
_Dot3MpcpMACCtrlFramesReceived_Object=MibTableColumn
dot3MpcpMACCtrlFramesReceived=_Dot3MpcpMACCtrlFramesReceived_Object((1,3,6,1,4,1,3902,1015,1010,1,2,2,1,2),_Dot3MpcpMACCtrlFramesReceived_Type())
dot3MpcpMACCtrlFramesReceived.setMaxAccess(_B)
if mibBuilder.loadTexts:dot3MpcpMACCtrlFramesReceived.setStatus(_A)
if mibBuilder.loadTexts:dot3MpcpMACCtrlFramesReceived.setUnits(_C)
_Dot3MpcpDiscoveryWindowsSent_Type=Counter32
_Dot3MpcpDiscoveryWindowsSent_Object=MibTableColumn
dot3MpcpDiscoveryWindowsSent=_Dot3MpcpDiscoveryWindowsSent_Object((1,3,6,1,4,1,3902,1015,1010,1,2,2,1,3),_Dot3MpcpDiscoveryWindowsSent_Type())
dot3MpcpDiscoveryWindowsSent.setMaxAccess(_B)
if mibBuilder.loadTexts:dot3MpcpDiscoveryWindowsSent.setStatus(_A)
_Dot3MpcpDiscoveryTimeout_Type=Counter32
_Dot3MpcpDiscoveryTimeout_Object=MibTableColumn
dot3MpcpDiscoveryTimeout=_Dot3MpcpDiscoveryTimeout_Object((1,3,6,1,4,1,3902,1015,1010,1,2,2,1,4),_Dot3MpcpDiscoveryTimeout_Type())
dot3MpcpDiscoveryTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:dot3MpcpDiscoveryTimeout.setStatus(_A)
_Dot3MpcpTxRegRequest_Type=Counter64
_Dot3MpcpTxRegRequest_Object=MibTableColumn
dot3MpcpTxRegRequest=_Dot3MpcpTxRegRequest_Object((1,3,6,1,4,1,3902,1015,1010,1,2,2,1,5),_Dot3MpcpTxRegRequest_Type())
dot3MpcpTxRegRequest.setMaxAccess(_B)
if mibBuilder.loadTexts:dot3MpcpTxRegRequest.setStatus(_A)
if mibBuilder.loadTexts:dot3MpcpTxRegRequest.setUnits(_C)
_Dot3MpcpRxRegRequest_Type=Counter64
_Dot3MpcpRxRegRequest_Object=MibTableColumn
dot3MpcpRxRegRequest=_Dot3MpcpRxRegRequest_Object((1,3,6,1,4,1,3902,1015,1010,1,2,2,1,6),_Dot3MpcpRxRegRequest_Type())
dot3MpcpRxRegRequest.setMaxAccess(_B)
if mibBuilder.loadTexts:dot3MpcpRxRegRequest.setStatus(_A)
if mibBuilder.loadTexts:dot3MpcpRxRegRequest.setUnits(_C)
_Dot3MpcpTxRegAck_Type=Counter64
_Dot3MpcpTxRegAck_Object=MibTableColumn
dot3MpcpTxRegAck=_Dot3MpcpTxRegAck_Object((1,3,6,1,4,1,3902,1015,1010,1,2,2,1,7),_Dot3MpcpTxRegAck_Type())
dot3MpcpTxRegAck.setMaxAccess(_B)
if mibBuilder.loadTexts:dot3MpcpTxRegAck.setStatus(_A)
if mibBuilder.loadTexts:dot3MpcpTxRegAck.setUnits(_C)
_Dot3MpcpRxRegAck_Type=Counter64
_Dot3MpcpRxRegAck_Object=MibTableColumn
dot3MpcpRxRegAck=_Dot3MpcpRxRegAck_Object((1,3,6,1,4,1,3902,1015,1010,1,2,2,1,8),_Dot3MpcpRxRegAck_Type())
dot3MpcpRxRegAck.setMaxAccess(_B)
if mibBuilder.loadTexts:dot3MpcpRxRegAck.setStatus(_A)
if mibBuilder.loadTexts:dot3MpcpRxRegAck.setUnits(_C)
_Dot3MpcpTxReport_Type=Counter64
_Dot3MpcpTxReport_Object=MibTableColumn
dot3MpcpTxReport=_Dot3MpcpTxReport_Object((1,3,6,1,4,1,3902,1015,1010,1,2,2,1,9),_Dot3MpcpTxReport_Type())
dot3MpcpTxReport.setMaxAccess(_B)
if mibBuilder.loadTexts:dot3MpcpTxReport.setStatus(_A)
if mibBuilder.loadTexts:dot3MpcpTxReport.setUnits(_C)
_Dot3MpcpRxReport_Type=Counter64
_Dot3MpcpRxReport_Object=MibTableColumn
dot3MpcpRxReport=_Dot3MpcpRxReport_Object((1,3,6,1,4,1,3902,1015,1010,1,2,2,1,10),_Dot3MpcpRxReport_Type())
dot3MpcpRxReport.setMaxAccess(_B)
if mibBuilder.loadTexts:dot3MpcpRxReport.setStatus(_A)
if mibBuilder.loadTexts:dot3MpcpRxReport.setUnits(_C)
_Dot3MpcpTxGate_Type=Counter64
_Dot3MpcpTxGate_Object=MibTableColumn
dot3MpcpTxGate=_Dot3MpcpTxGate_Object((1,3,6,1,4,1,3902,1015,1010,1,2,2,1,11),_Dot3MpcpTxGate_Type())
dot3MpcpTxGate.setMaxAccess(_B)
if mibBuilder.loadTexts:dot3MpcpTxGate.setStatus(_A)
if mibBuilder.loadTexts:dot3MpcpTxGate.setUnits(_C)
_Dot3MpcpRxGate_Type=Counter64
_Dot3MpcpRxGate_Object=MibTableColumn
dot3MpcpRxGate=_Dot3MpcpRxGate_Object((1,3,6,1,4,1,3902,1015,1010,1,2,2,1,12),_Dot3MpcpRxGate_Type())
dot3MpcpRxGate.setMaxAccess(_B)
if mibBuilder.loadTexts:dot3MpcpRxGate.setStatus(_A)
if mibBuilder.loadTexts:dot3MpcpRxGate.setUnits(_C)
_Dot3MpcpTxRegister_Type=Counter64
_Dot3MpcpTxRegister_Object=MibTableColumn
dot3MpcpTxRegister=_Dot3MpcpTxRegister_Object((1,3,6,1,4,1,3902,1015,1010,1,2,2,1,13),_Dot3MpcpTxRegister_Type())
dot3MpcpTxRegister.setMaxAccess(_B)
if mibBuilder.loadTexts:dot3MpcpTxRegister.setStatus(_A)
if mibBuilder.loadTexts:dot3MpcpTxRegister.setUnits(_C)
_Dot3MpcpRxRegister_Type=Counter64
_Dot3MpcpRxRegister_Object=MibTableColumn
dot3MpcpRxRegister=_Dot3MpcpRxRegister_Object((1,3,6,1,4,1,3902,1015,1010,1,2,2,1,14),_Dot3MpcpRxRegister_Type())
dot3MpcpRxRegister.setMaxAccess(_B)
if mibBuilder.loadTexts:dot3MpcpRxRegister.setStatus(_A)
if mibBuilder.loadTexts:dot3MpcpRxRegister.setUnits(_C)
_Dot3OmpEmulationObjects_ObjectIdentity=ObjectIdentity
dot3OmpEmulationObjects=_Dot3OmpEmulationObjects_ObjectIdentity((1,3,6,1,4,1,3902,1015,1010,1,3))
_Dot3OmpEmulationTable_Object=MibTable
dot3OmpEmulationTable=_Dot3OmpEmulationTable_Object((1,3,6,1,4,1,3902,1015,1010,1,3,1))
if mibBuilder.loadTexts:dot3OmpEmulationTable.setStatus(_A)
_Dot3OmpEmulationEntry_Object=MibTableRow
dot3OmpEmulationEntry=_Dot3OmpEmulationEntry_Object((1,3,6,1,4,1,3902,1015,1010,1,3,1,1))
dot3OmpEmulationEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:dot3OmpEmulationEntry.setStatus(_A)
class _Dot3OmpEmulationType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_M,1),('olt',2),('onu',3)))
_Dot3OmpEmulationType_Type.__name__=_I
_Dot3OmpEmulationType_Object=MibTableColumn
dot3OmpEmulationType=_Dot3OmpEmulationType_Object((1,3,6,1,4,1,3902,1015,1010,1,3,1,1,1),_Dot3OmpEmulationType_Type())
dot3OmpEmulationType.setMaxAccess(_B)
if mibBuilder.loadTexts:dot3OmpEmulationType.setStatus(_A)
_Dot3OmpEmulationStatTable_Object=MibTable
dot3OmpEmulationStatTable=_Dot3OmpEmulationStatTable_Object((1,3,6,1,4,1,3902,1015,1010,1,3,2))
if mibBuilder.loadTexts:dot3OmpEmulationStatTable.setStatus(_A)
_Dot3OmpEmulationStatEntry_Object=MibTableRow
dot3OmpEmulationStatEntry=_Dot3OmpEmulationStatEntry_Object((1,3,6,1,4,1,3902,1015,1010,1,3,2,1))
dot3OmpEmulationStatEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:dot3OmpEmulationStatEntry.setStatus(_A)
_Dot3OmpEmulationSLDErrors_Type=Counter64
_Dot3OmpEmulationSLDErrors_Object=MibTableColumn
dot3OmpEmulationSLDErrors=_Dot3OmpEmulationSLDErrors_Object((1,3,6,1,4,1,3902,1015,1010,1,3,2,1,1),_Dot3OmpEmulationSLDErrors_Type())
dot3OmpEmulationSLDErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:dot3OmpEmulationSLDErrors.setStatus(_A)
if mibBuilder.loadTexts:dot3OmpEmulationSLDErrors.setUnits(_C)
_Dot3OmpEmulationCRC8Errors_Type=Counter64
_Dot3OmpEmulationCRC8Errors_Object=MibTableColumn
dot3OmpEmulationCRC8Errors=_Dot3OmpEmulationCRC8Errors_Object((1,3,6,1,4,1,3902,1015,1010,1,3,2,1,2),_Dot3OmpEmulationCRC8Errors_Type())
dot3OmpEmulationCRC8Errors.setMaxAccess(_B)
if mibBuilder.loadTexts:dot3OmpEmulationCRC8Errors.setStatus(_A)
if mibBuilder.loadTexts:dot3OmpEmulationCRC8Errors.setUnits(_C)
_Dot3OmpEmulationBadLLID_Type=Counter64
_Dot3OmpEmulationBadLLID_Object=MibTableColumn
dot3OmpEmulationBadLLID=_Dot3OmpEmulationBadLLID_Object((1,3,6,1,4,1,3902,1015,1010,1,3,2,1,3),_Dot3OmpEmulationBadLLID_Type())
dot3OmpEmulationBadLLID.setMaxAccess(_B)
if mibBuilder.loadTexts:dot3OmpEmulationBadLLID.setStatus(_A)
if mibBuilder.loadTexts:dot3OmpEmulationBadLLID.setUnits(_C)
_Dot3OmpEmulationGoodLLID_Type=Counter64
_Dot3OmpEmulationGoodLLID_Object=MibTableColumn
dot3OmpEmulationGoodLLID=_Dot3OmpEmulationGoodLLID_Object((1,3,6,1,4,1,3902,1015,1010,1,3,2,1,4),_Dot3OmpEmulationGoodLLID_Type())
dot3OmpEmulationGoodLLID.setMaxAccess(_B)
if mibBuilder.loadTexts:dot3OmpEmulationGoodLLID.setStatus(_A)
if mibBuilder.loadTexts:dot3OmpEmulationGoodLLID.setUnits(_C)
_Dot3OmpEmulationOnuPonCastLLID_Type=Counter64
_Dot3OmpEmulationOnuPonCastLLID_Object=MibTableColumn
dot3OmpEmulationOnuPonCastLLID=_Dot3OmpEmulationOnuPonCastLLID_Object((1,3,6,1,4,1,3902,1015,1010,1,3,2,1,5),_Dot3OmpEmulationOnuPonCastLLID_Type())
dot3OmpEmulationOnuPonCastLLID.setMaxAccess(_B)
if mibBuilder.loadTexts:dot3OmpEmulationOnuPonCastLLID.setStatus(_A)
if mibBuilder.loadTexts:dot3OmpEmulationOnuPonCastLLID.setUnits(_C)
_Dot3OmpEmulationOltPonCastLLID_Type=Counter64
_Dot3OmpEmulationOltPonCastLLID_Object=MibTableColumn
dot3OmpEmulationOltPonCastLLID=_Dot3OmpEmulationOltPonCastLLID_Object((1,3,6,1,4,1,3902,1015,1010,1,3,2,1,6),_Dot3OmpEmulationOltPonCastLLID_Type())
dot3OmpEmulationOltPonCastLLID.setMaxAccess(_B)
if mibBuilder.loadTexts:dot3OmpEmulationOltPonCastLLID.setStatus(_A)
if mibBuilder.loadTexts:dot3OmpEmulationOltPonCastLLID.setUnits(_C)
_Dot3OmpEmulationBroadcastBitNotOnuLlid_Type=Counter64
_Dot3OmpEmulationBroadcastBitNotOnuLlid_Object=MibTableColumn
dot3OmpEmulationBroadcastBitNotOnuLlid=_Dot3OmpEmulationBroadcastBitNotOnuLlid_Object((1,3,6,1,4,1,3902,1015,1010,1,3,2,1,7),_Dot3OmpEmulationBroadcastBitNotOnuLlid_Type())
dot3OmpEmulationBroadcastBitNotOnuLlid.setMaxAccess(_B)
if mibBuilder.loadTexts:dot3OmpEmulationBroadcastBitNotOnuLlid.setStatus(_A)
if mibBuilder.loadTexts:dot3OmpEmulationBroadcastBitNotOnuLlid.setUnits(_C)
_Dot3OmpEmulationOnuLLIDNotBroadcast_Type=Counter64
_Dot3OmpEmulationOnuLLIDNotBroadcast_Object=MibTableColumn
dot3OmpEmulationOnuLLIDNotBroadcast=_Dot3OmpEmulationOnuLLIDNotBroadcast_Object((1,3,6,1,4,1,3902,1015,1010,1,3,2,1,8),_Dot3OmpEmulationOnuLLIDNotBroadcast_Type())
dot3OmpEmulationOnuLLIDNotBroadcast.setMaxAccess(_B)
if mibBuilder.loadTexts:dot3OmpEmulationOnuLLIDNotBroadcast.setStatus(_A)
if mibBuilder.loadTexts:dot3OmpEmulationOnuLLIDNotBroadcast.setUnits(_C)
_Dot3OmpEmulationBroadcastBitPlusOnuLlid_Type=Counter64
_Dot3OmpEmulationBroadcastBitPlusOnuLlid_Object=MibTableColumn
dot3OmpEmulationBroadcastBitPlusOnuLlid=_Dot3OmpEmulationBroadcastBitPlusOnuLlid_Object((1,3,6,1,4,1,3902,1015,1010,1,3,2,1,9),_Dot3OmpEmulationBroadcastBitPlusOnuLlid_Type())
dot3OmpEmulationBroadcastBitPlusOnuLlid.setMaxAccess(_B)
if mibBuilder.loadTexts:dot3OmpEmulationBroadcastBitPlusOnuLlid.setStatus(_A)
if mibBuilder.loadTexts:dot3OmpEmulationBroadcastBitPlusOnuLlid.setUnits(_C)
_Dot3OmpEmulationNotBroadcastBitNotOnuLlid_Type=Counter64
_Dot3OmpEmulationNotBroadcastBitNotOnuLlid_Object=MibTableColumn
dot3OmpEmulationNotBroadcastBitNotOnuLlid=_Dot3OmpEmulationNotBroadcastBitNotOnuLlid_Object((1,3,6,1,4,1,3902,1015,1010,1,3,2,1,10),_Dot3OmpEmulationNotBroadcastBitNotOnuLlid_Type())
dot3OmpEmulationNotBroadcastBitNotOnuLlid.setMaxAccess(_B)
if mibBuilder.loadTexts:dot3OmpEmulationNotBroadcastBitNotOnuLlid.setStatus(_A)
if mibBuilder.loadTexts:dot3OmpEmulationNotBroadcastBitNotOnuLlid.setUnits(_C)
_Dot3EponFecObjects_ObjectIdentity=ObjectIdentity
dot3EponFecObjects=_Dot3EponFecObjects_ObjectIdentity((1,3,6,1,4,1,3902,1015,1010,1,4))
_Dot3EponFecTable_Object=MibTable
dot3EponFecTable=_Dot3EponFecTable_Object((1,3,6,1,4,1,3902,1015,1010,1,4,1))
if mibBuilder.loadTexts:dot3EponFecTable.setStatus(_A)
_Dot3EponFecEntry_Object=MibTableRow
dot3EponFecEntry=_Dot3EponFecEntry_Object((1,3,6,1,4,1,3902,1015,1010,1,4,1,1))
dot3EponFecEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:dot3EponFecEntry.setStatus(_A)
_Dot3EponFecPCSCodingViolation_Type=Counter64
_Dot3EponFecPCSCodingViolation_Object=MibTableColumn
dot3EponFecPCSCodingViolation=_Dot3EponFecPCSCodingViolation_Object((1,3,6,1,4,1,3902,1015,1010,1,4,1,1,1),_Dot3EponFecPCSCodingViolation_Type())
dot3EponFecPCSCodingViolation.setMaxAccess(_B)
if mibBuilder.loadTexts:dot3EponFecPCSCodingViolation.setStatus(_A)
if mibBuilder.loadTexts:dot3EponFecPCSCodingViolation.setUnits(_O)
class _Dot3EponFecAbility_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_M,1),('unsupported',2),('supported',3)))
_Dot3EponFecAbility_Type.__name__=_I
_Dot3EponFecAbility_Object=MibTableColumn
dot3EponFecAbility=_Dot3EponFecAbility_Object((1,3,6,1,4,1,3902,1015,1010,1,4,1,1,2),_Dot3EponFecAbility_Type())
dot3EponFecAbility.setMaxAccess(_B)
if mibBuilder.loadTexts:dot3EponFecAbility.setStatus(_A)
class _Dot3EponFecMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_M,1),('disabled',2),('enabled',3)))
_Dot3EponFecMode_Type.__name__=_I
_Dot3EponFecMode_Object=MibTableColumn
dot3EponFecMode=_Dot3EponFecMode_Object((1,3,6,1,4,1,3902,1015,1010,1,4,1,1,3),_Dot3EponFecMode_Type())
dot3EponFecMode.setMaxAccess(_D)
if mibBuilder.loadTexts:dot3EponFecMode.setStatus(_A)
_Dot3EponFecCorrectedBlocks_Type=Counter64
_Dot3EponFecCorrectedBlocks_Object=MibTableColumn
dot3EponFecCorrectedBlocks=_Dot3EponFecCorrectedBlocks_Object((1,3,6,1,4,1,3902,1015,1010,1,4,1,1,4),_Dot3EponFecCorrectedBlocks_Type())
dot3EponFecCorrectedBlocks.setMaxAccess(_B)
if mibBuilder.loadTexts:dot3EponFecCorrectedBlocks.setStatus(_A)
_Dot3EponFecUncorrectableBlocks_Type=Counter64
_Dot3EponFecUncorrectableBlocks_Object=MibTableColumn
dot3EponFecUncorrectableBlocks=_Dot3EponFecUncorrectableBlocks_Object((1,3,6,1,4,1,3902,1015,1010,1,4,1,1,5),_Dot3EponFecUncorrectableBlocks_Type())
dot3EponFecUncorrectableBlocks.setMaxAccess(_B)
if mibBuilder.loadTexts:dot3EponFecUncorrectableBlocks.setStatus(_A)
_Dot3EponFecBufferHeadCodingViolation_Type=Counter64
_Dot3EponFecBufferHeadCodingViolation_Object=MibTableColumn
dot3EponFecBufferHeadCodingViolation=_Dot3EponFecBufferHeadCodingViolation_Object((1,3,6,1,4,1,3902,1015,1010,1,4,1,1,6),_Dot3EponFecBufferHeadCodingViolation_Type())
dot3EponFecBufferHeadCodingViolation.setMaxAccess(_B)
if mibBuilder.loadTexts:dot3EponFecBufferHeadCodingViolation.setStatus(_A)
if mibBuilder.loadTexts:dot3EponFecBufferHeadCodingViolation.setUnits(_O)
_Dot3ExtPkgObjects_ObjectIdentity=ObjectIdentity
dot3ExtPkgObjects=_Dot3ExtPkgObjects_ObjectIdentity((1,3,6,1,4,1,3902,1015,1010,1,5))
_Dot3ExtPkgControlObjects_ObjectIdentity=ObjectIdentity
dot3ExtPkgControlObjects=_Dot3ExtPkgControlObjects_ObjectIdentity((1,3,6,1,4,1,3902,1015,1010,1,5,1))
_Dot3ExtPkgControlTable_Object=MibTable
dot3ExtPkgControlTable=_Dot3ExtPkgControlTable_Object((1,3,6,1,4,1,3902,1015,1010,1,5,1,1))
if mibBuilder.loadTexts:dot3ExtPkgControlTable.setStatus(_A)
_Dot3ExtPkgControlEntry_Object=MibTableRow
dot3ExtPkgControlEntry=_Dot3ExtPkgControlEntry_Object((1,3,6,1,4,1,3902,1015,1010,1,5,1,1,1))
dot3ExtPkgControlEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:dot3ExtPkgControlEntry.setStatus(_A)
class _Dot3ExtPkgObjectReset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('running',1),('reset',2)))
_Dot3ExtPkgObjectReset_Type.__name__=_I
_Dot3ExtPkgObjectReset_Object=MibTableColumn
dot3ExtPkgObjectReset=_Dot3ExtPkgObjectReset_Object((1,3,6,1,4,1,3902,1015,1010,1,5,1,1,1,1),_Dot3ExtPkgObjectReset_Type())
dot3ExtPkgObjectReset.setMaxAccess(_D)
if mibBuilder.loadTexts:dot3ExtPkgObjectReset.setStatus(_A)
_Dot3ExtPkgObjectPowerDown_Type=TruthValue
_Dot3ExtPkgObjectPowerDown_Object=MibTableColumn
dot3ExtPkgObjectPowerDown=_Dot3ExtPkgObjectPowerDown_Object((1,3,6,1,4,1,3902,1015,1010,1,5,1,1,1,2),_Dot3ExtPkgObjectPowerDown_Type())
dot3ExtPkgObjectPowerDown.setMaxAccess(_D)
if mibBuilder.loadTexts:dot3ExtPkgObjectPowerDown.setStatus(_A)
_Dot3ExtPkgObjectNumberOfLLIDs_Type=Unsigned32
_Dot3ExtPkgObjectNumberOfLLIDs_Object=MibTableColumn
dot3ExtPkgObjectNumberOfLLIDs=_Dot3ExtPkgObjectNumberOfLLIDs_Object((1,3,6,1,4,1,3902,1015,1010,1,5,1,1,1,3),_Dot3ExtPkgObjectNumberOfLLIDs_Type())
dot3ExtPkgObjectNumberOfLLIDs.setMaxAccess(_B)
if mibBuilder.loadTexts:dot3ExtPkgObjectNumberOfLLIDs.setStatus(_A)
class _Dot3ExtPkgObjectFecEnabled_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('noFecEnabled',1),('fecTxEnabled',2),('fecRxEnabled',3),('fecTxRxEnabled',4)))
_Dot3ExtPkgObjectFecEnabled_Type.__name__=_I
_Dot3ExtPkgObjectFecEnabled_Object=MibTableColumn
dot3ExtPkgObjectFecEnabled=_Dot3ExtPkgObjectFecEnabled_Object((1,3,6,1,4,1,3902,1015,1010,1,5,1,1,1,4),_Dot3ExtPkgObjectFecEnabled_Type())
dot3ExtPkgObjectFecEnabled.setMaxAccess(_D)
if mibBuilder.loadTexts:dot3ExtPkgObjectFecEnabled.setStatus(_A)
class _Dot3ExtPkgObjectReportMaximumNumQueues_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_Dot3ExtPkgObjectReportMaximumNumQueues_Type.__name__=_G
_Dot3ExtPkgObjectReportMaximumNumQueues_Object=MibTableColumn
dot3ExtPkgObjectReportMaximumNumQueues=_Dot3ExtPkgObjectReportMaximumNumQueues_Object((1,3,6,1,4,1,3902,1015,1010,1,5,1,1,1,5),_Dot3ExtPkgObjectReportMaximumNumQueues_Type())
dot3ExtPkgObjectReportMaximumNumQueues.setMaxAccess(_B)
if mibBuilder.loadTexts:dot3ExtPkgObjectReportMaximumNumQueues.setStatus(_A)
class _Dot3ExtPkgObjectRegisterAction_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('none',1),('register',2),('deregister',3),('reregister',4)))
_Dot3ExtPkgObjectRegisterAction_Type.__name__=_I
_Dot3ExtPkgObjectRegisterAction_Object=MibTableColumn
dot3ExtPkgObjectRegisterAction=_Dot3ExtPkgObjectRegisterAction_Object((1,3,6,1,4,1,3902,1015,1010,1,5,1,1,1,6),_Dot3ExtPkgObjectRegisterAction_Type())
dot3ExtPkgObjectRegisterAction.setMaxAccess(_D)
if mibBuilder.loadTexts:dot3ExtPkgObjectRegisterAction.setStatus(_A)
_Dot3ExtPkgQueueTable_Object=MibTable
dot3ExtPkgQueueTable=_Dot3ExtPkgQueueTable_Object((1,3,6,1,4,1,3902,1015,1010,1,5,1,2))
if mibBuilder.loadTexts:dot3ExtPkgQueueTable.setStatus(_A)
_Dot3ExtPkgQueueEntry_Object=MibTableRow
dot3ExtPkgQueueEntry=_Dot3ExtPkgQueueEntry_Object((1,3,6,1,4,1,3902,1015,1010,1,5,1,2,1))
dot3ExtPkgQueueEntry.setIndexNames((0,_E,_F),(0,_L,_P))
if mibBuilder.loadTexts:dot3ExtPkgQueueEntry.setStatus(_A)
class _Dot3QueueIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_Dot3QueueIndex_Type.__name__=_G
_Dot3QueueIndex_Object=MibTableColumn
dot3QueueIndex=_Dot3QueueIndex_Object((1,3,6,1,4,1,3902,1015,1010,1,5,1,2,1,1),_Dot3QueueIndex_Type())
dot3QueueIndex.setMaxAccess(_N)
if mibBuilder.loadTexts:dot3QueueIndex.setStatus(_A)
class _Dot3ExtPkgObjectReportNumThreshold_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_Dot3ExtPkgObjectReportNumThreshold_Type.__name__=_G
_Dot3ExtPkgObjectReportNumThreshold_Object=MibTableColumn
dot3ExtPkgObjectReportNumThreshold=_Dot3ExtPkgObjectReportNumThreshold_Object((1,3,6,1,4,1,3902,1015,1010,1,5,1,2,1,2),_Dot3ExtPkgObjectReportNumThreshold_Type())
dot3ExtPkgObjectReportNumThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:dot3ExtPkgObjectReportNumThreshold.setStatus(_A)
class _Dot3ExtPkgObjectReportMaximumNumThreshold_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_Dot3ExtPkgObjectReportMaximumNumThreshold_Type.__name__=_G
_Dot3ExtPkgObjectReportMaximumNumThreshold_Object=MibTableColumn
dot3ExtPkgObjectReportMaximumNumThreshold=_Dot3ExtPkgObjectReportMaximumNumThreshold_Object((1,3,6,1,4,1,3902,1015,1010,1,5,1,2,1,3),_Dot3ExtPkgObjectReportMaximumNumThreshold_Type())
dot3ExtPkgObjectReportMaximumNumThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:dot3ExtPkgObjectReportMaximumNumThreshold.setStatus(_A)
_Dot3ExtPkgStatTxFramesQueue_Type=Counter64
_Dot3ExtPkgStatTxFramesQueue_Object=MibTableColumn
dot3ExtPkgStatTxFramesQueue=_Dot3ExtPkgStatTxFramesQueue_Object((1,3,6,1,4,1,3902,1015,1010,1,5,1,2,1,4),_Dot3ExtPkgStatTxFramesQueue_Type())
dot3ExtPkgStatTxFramesQueue.setMaxAccess(_B)
if mibBuilder.loadTexts:dot3ExtPkgStatTxFramesQueue.setStatus(_A)
if mibBuilder.loadTexts:dot3ExtPkgStatTxFramesQueue.setUnits(_C)
_Dot3ExtPkgStatRxFramesQueue_Type=Counter64
_Dot3ExtPkgStatRxFramesQueue_Object=MibTableColumn
dot3ExtPkgStatRxFramesQueue=_Dot3ExtPkgStatRxFramesQueue_Object((1,3,6,1,4,1,3902,1015,1010,1,5,1,2,1,5),_Dot3ExtPkgStatRxFramesQueue_Type())
dot3ExtPkgStatRxFramesQueue.setMaxAccess(_B)
if mibBuilder.loadTexts:dot3ExtPkgStatRxFramesQueue.setStatus(_A)
if mibBuilder.loadTexts:dot3ExtPkgStatRxFramesQueue.setUnits(_C)
_Dot3ExtPkgStatDroppedFramesQueue_Type=Counter64
_Dot3ExtPkgStatDroppedFramesQueue_Object=MibTableColumn
dot3ExtPkgStatDroppedFramesQueue=_Dot3ExtPkgStatDroppedFramesQueue_Object((1,3,6,1,4,1,3902,1015,1010,1,5,1,2,1,6),_Dot3ExtPkgStatDroppedFramesQueue_Type())
dot3ExtPkgStatDroppedFramesQueue.setMaxAccess(_B)
if mibBuilder.loadTexts:dot3ExtPkgStatDroppedFramesQueue.setStatus(_A)
if mibBuilder.loadTexts:dot3ExtPkgStatDroppedFramesQueue.setUnits(_C)
_Dot3ExtPkgQueueSetsTable_Object=MibTable
dot3ExtPkgQueueSetsTable=_Dot3ExtPkgQueueSetsTable_Object((1,3,6,1,4,1,3902,1015,1010,1,5,1,3))
if mibBuilder.loadTexts:dot3ExtPkgQueueSetsTable.setStatus(_A)
_Dot3ExtPkgQueueSetsEntry_Object=MibTableRow
dot3ExtPkgQueueSetsEntry=_Dot3ExtPkgQueueSetsEntry_Object((1,3,6,1,4,1,3902,1015,1010,1,5,1,3,1))
dot3ExtPkgQueueSetsEntry.setIndexNames((0,_E,_F),(0,_L,_Q),(0,_L,_R))
if mibBuilder.loadTexts:dot3ExtPkgQueueSetsEntry.setStatus(_A)
class _Dot3QueueSetQueueIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_Dot3QueueSetQueueIndex_Type.__name__=_G
_Dot3QueueSetQueueIndex_Object=MibTableColumn
dot3QueueSetQueueIndex=_Dot3QueueSetQueueIndex_Object((1,3,6,1,4,1,3902,1015,1010,1,5,1,3,1,1),_Dot3QueueSetQueueIndex_Type())
dot3QueueSetQueueIndex.setMaxAccess(_N)
if mibBuilder.loadTexts:dot3QueueSetQueueIndex.setStatus(_A)
class _Dot3QueueSetIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_Dot3QueueSetIndex_Type.__name__=_G
_Dot3QueueSetIndex_Object=MibTableColumn
dot3QueueSetIndex=_Dot3QueueSetIndex_Object((1,3,6,1,4,1,3902,1015,1010,1,5,1,3,1,2),_Dot3QueueSetIndex_Type())
dot3QueueSetIndex.setMaxAccess(_N)
if mibBuilder.loadTexts:dot3QueueSetIndex.setStatus(_A)
class _Dot3ExtPkgObjectReportThreshold_Type(Unsigned32):defaultValue=0
_Dot3ExtPkgObjectReportThreshold_Type.__name__=_G
_Dot3ExtPkgObjectReportThreshold_Object=MibTableColumn
dot3ExtPkgObjectReportThreshold=_Dot3ExtPkgObjectReportThreshold_Object((1,3,6,1,4,1,3902,1015,1010,1,5,1,3,1,3),_Dot3ExtPkgObjectReportThreshold_Type())
dot3ExtPkgObjectReportThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:dot3ExtPkgObjectReportThreshold.setStatus(_A)
if mibBuilder.loadTexts:dot3ExtPkgObjectReportThreshold.setUnits(_K)
_Dot3ExtPkgOptIfTable_Object=MibTable
dot3ExtPkgOptIfTable=_Dot3ExtPkgOptIfTable_Object((1,3,6,1,4,1,3902,1015,1010,1,5,1,5))
if mibBuilder.loadTexts:dot3ExtPkgOptIfTable.setStatus(_A)
_Dot3ExtPkgOptIfEntry_Object=MibTableRow
dot3ExtPkgOptIfEntry=_Dot3ExtPkgOptIfEntry_Object((1,3,6,1,4,1,3902,1015,1010,1,5,1,5,1))
dot3ExtPkgOptIfEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:dot3ExtPkgOptIfEntry.setStatus(_A)
_Dot3ExtPkgOptIfSuspectedFlag_Type=TruthValue
_Dot3ExtPkgOptIfSuspectedFlag_Object=MibTableColumn
dot3ExtPkgOptIfSuspectedFlag=_Dot3ExtPkgOptIfSuspectedFlag_Object((1,3,6,1,4,1,3902,1015,1010,1,5,1,5,1,1),_Dot3ExtPkgOptIfSuspectedFlag_Type())
dot3ExtPkgOptIfSuspectedFlag.setMaxAccess(_B)
if mibBuilder.loadTexts:dot3ExtPkgOptIfSuspectedFlag.setStatus(_A)
_Dot3ExtPkgOptIfInputPower_Type=Integer32
_Dot3ExtPkgOptIfInputPower_Object=MibTableColumn
dot3ExtPkgOptIfInputPower=_Dot3ExtPkgOptIfInputPower_Object((1,3,6,1,4,1,3902,1015,1010,1,5,1,5,1,2),_Dot3ExtPkgOptIfInputPower_Type())
dot3ExtPkgOptIfInputPower.setMaxAccess(_B)
if mibBuilder.loadTexts:dot3ExtPkgOptIfInputPower.setStatus(_A)
if mibBuilder.loadTexts:dot3ExtPkgOptIfInputPower.setUnits(_H)
_Dot3ExtPkgOptIfLowInputPower_Type=Integer32
_Dot3ExtPkgOptIfLowInputPower_Object=MibTableColumn
dot3ExtPkgOptIfLowInputPower=_Dot3ExtPkgOptIfLowInputPower_Object((1,3,6,1,4,1,3902,1015,1010,1,5,1,5,1,3),_Dot3ExtPkgOptIfLowInputPower_Type())
dot3ExtPkgOptIfLowInputPower.setMaxAccess(_B)
if mibBuilder.loadTexts:dot3ExtPkgOptIfLowInputPower.setStatus(_A)
if mibBuilder.loadTexts:dot3ExtPkgOptIfLowInputPower.setUnits(_H)
_Dot3ExtPkgOptIfHighInputPower_Type=Integer32
_Dot3ExtPkgOptIfHighInputPower_Object=MibTableColumn
dot3ExtPkgOptIfHighInputPower=_Dot3ExtPkgOptIfHighInputPower_Object((1,3,6,1,4,1,3902,1015,1010,1,5,1,5,1,4),_Dot3ExtPkgOptIfHighInputPower_Type())
dot3ExtPkgOptIfHighInputPower.setMaxAccess(_B)
if mibBuilder.loadTexts:dot3ExtPkgOptIfHighInputPower.setStatus(_A)
if mibBuilder.loadTexts:dot3ExtPkgOptIfHighInputPower.setUnits(_H)
_Dot3ExtPkgOptIfLowerInputPowerThreshold_Type=Integer32
_Dot3ExtPkgOptIfLowerInputPowerThreshold_Object=MibTableColumn
dot3ExtPkgOptIfLowerInputPowerThreshold=_Dot3ExtPkgOptIfLowerInputPowerThreshold_Object((1,3,6,1,4,1,3902,1015,1010,1,5,1,5,1,5),_Dot3ExtPkgOptIfLowerInputPowerThreshold_Type())
dot3ExtPkgOptIfLowerInputPowerThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:dot3ExtPkgOptIfLowerInputPowerThreshold.setStatus(_A)
if mibBuilder.loadTexts:dot3ExtPkgOptIfLowerInputPowerThreshold.setUnits(_H)
_Dot3ExtPkgOptIfUpperInputPowerThreshold_Type=Integer32
_Dot3ExtPkgOptIfUpperInputPowerThreshold_Object=MibTableColumn
dot3ExtPkgOptIfUpperInputPowerThreshold=_Dot3ExtPkgOptIfUpperInputPowerThreshold_Object((1,3,6,1,4,1,3902,1015,1010,1,5,1,5,1,6),_Dot3ExtPkgOptIfUpperInputPowerThreshold_Type())
dot3ExtPkgOptIfUpperInputPowerThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:dot3ExtPkgOptIfUpperInputPowerThreshold.setStatus(_A)
if mibBuilder.loadTexts:dot3ExtPkgOptIfUpperInputPowerThreshold.setUnits(_H)
_Dot3ExtPkgOptIfOutputPower_Type=Integer32
_Dot3ExtPkgOptIfOutputPower_Object=MibTableColumn
dot3ExtPkgOptIfOutputPower=_Dot3ExtPkgOptIfOutputPower_Object((1,3,6,1,4,1,3902,1015,1010,1,5,1,5,1,7),_Dot3ExtPkgOptIfOutputPower_Type())
dot3ExtPkgOptIfOutputPower.setMaxAccess(_B)
if mibBuilder.loadTexts:dot3ExtPkgOptIfOutputPower.setStatus(_A)
if mibBuilder.loadTexts:dot3ExtPkgOptIfOutputPower.setUnits(_H)
_Dot3ExtPkgOptIfLowOutputPower_Type=Integer32
_Dot3ExtPkgOptIfLowOutputPower_Object=MibTableColumn
dot3ExtPkgOptIfLowOutputPower=_Dot3ExtPkgOptIfLowOutputPower_Object((1,3,6,1,4,1,3902,1015,1010,1,5,1,5,1,8),_Dot3ExtPkgOptIfLowOutputPower_Type())
dot3ExtPkgOptIfLowOutputPower.setMaxAccess(_B)
if mibBuilder.loadTexts:dot3ExtPkgOptIfLowOutputPower.setStatus(_A)
if mibBuilder.loadTexts:dot3ExtPkgOptIfLowOutputPower.setUnits(_H)
_Dot3ExtPkgOptIfHighOutputPower_Type=Integer32
_Dot3ExtPkgOptIfHighOutputPower_Object=MibTableColumn
dot3ExtPkgOptIfHighOutputPower=_Dot3ExtPkgOptIfHighOutputPower_Object((1,3,6,1,4,1,3902,1015,1010,1,5,1,5,1,9),_Dot3ExtPkgOptIfHighOutputPower_Type())
dot3ExtPkgOptIfHighOutputPower.setMaxAccess(_B)
if mibBuilder.loadTexts:dot3ExtPkgOptIfHighOutputPower.setStatus(_A)
if mibBuilder.loadTexts:dot3ExtPkgOptIfHighOutputPower.setUnits(_H)
_Dot3ExtPkgOptIfLowerOutputPowerThreshold_Type=Integer32
_Dot3ExtPkgOptIfLowerOutputPowerThreshold_Object=MibTableColumn
dot3ExtPkgOptIfLowerOutputPowerThreshold=_Dot3ExtPkgOptIfLowerOutputPowerThreshold_Object((1,3,6,1,4,1,3902,1015,1010,1,5,1,5,1,10),_Dot3ExtPkgOptIfLowerOutputPowerThreshold_Type())
dot3ExtPkgOptIfLowerOutputPowerThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:dot3ExtPkgOptIfLowerOutputPowerThreshold.setStatus(_A)
if mibBuilder.loadTexts:dot3ExtPkgOptIfLowerOutputPowerThreshold.setUnits(_H)
_Dot3ExtPkgOptIfUpperOutputPowerThreshold_Type=Integer32
_Dot3ExtPkgOptIfUpperOutputPowerThreshold_Object=MibTableColumn
dot3ExtPkgOptIfUpperOutputPowerThreshold=_Dot3ExtPkgOptIfUpperOutputPowerThreshold_Object((1,3,6,1,4,1,3902,1015,1010,1,5,1,5,1,11),_Dot3ExtPkgOptIfUpperOutputPowerThreshold_Type())
dot3ExtPkgOptIfUpperOutputPowerThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:dot3ExtPkgOptIfUpperOutputPowerThreshold.setStatus(_A)
if mibBuilder.loadTexts:dot3ExtPkgOptIfUpperOutputPowerThreshold.setUnits(_H)
class _Dot3ExtPkgOptIfSignalDetect_Type(TruthValue):defaultValue=2
_Dot3ExtPkgOptIfSignalDetect_Type.__name__=_J
_Dot3ExtPkgOptIfSignalDetect_Object=MibTableColumn
dot3ExtPkgOptIfSignalDetect=_Dot3ExtPkgOptIfSignalDetect_Object((1,3,6,1,4,1,3902,1015,1010,1,5,1,5,1,12),_Dot3ExtPkgOptIfSignalDetect_Type())
dot3ExtPkgOptIfSignalDetect.setMaxAccess(_B)
if mibBuilder.loadTexts:dot3ExtPkgOptIfSignalDetect.setStatus(_A)
class _Dot3ExtPkgOptIfTransmitAlarm_Type(TruthValue):defaultValue=2
_Dot3ExtPkgOptIfTransmitAlarm_Type.__name__=_J
_Dot3ExtPkgOptIfTransmitAlarm_Object=MibTableColumn
dot3ExtPkgOptIfTransmitAlarm=_Dot3ExtPkgOptIfTransmitAlarm_Object((1,3,6,1,4,1,3902,1015,1010,1,5,1,5,1,13),_Dot3ExtPkgOptIfTransmitAlarm_Type())
dot3ExtPkgOptIfTransmitAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:dot3ExtPkgOptIfTransmitAlarm.setStatus(_A)
class _Dot3ExtPkgOptIfTransmitEnable_Type(TruthValue):defaultValue=2
_Dot3ExtPkgOptIfTransmitEnable_Type.__name__=_J
_Dot3ExtPkgOptIfTransmitEnable_Object=MibTableColumn
dot3ExtPkgOptIfTransmitEnable=_Dot3ExtPkgOptIfTransmitEnable_Object((1,3,6,1,4,1,3902,1015,1010,1,5,1,5,1,14),_Dot3ExtPkgOptIfTransmitEnable_Type())
dot3ExtPkgOptIfTransmitEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:dot3ExtPkgOptIfTransmitEnable.setStatus(_A)
mibBuilder.exportSymbols(_L,**{'dot3MpcpObjects':dot3MpcpObjects,'dot3MpcpControlTable':dot3MpcpControlTable,'dot3MpcpControlEntry':dot3MpcpControlEntry,'dot3MpcpOperStatus':dot3MpcpOperStatus,'dot3MpcpAdminState':dot3MpcpAdminState,'dot3MpcpMode':dot3MpcpMode,'dot3MpcpSyncTime':dot3MpcpSyncTime,'dot3MpcpLinkID':dot3MpcpLinkID,'dot3MpcpRemoteMACAddress':dot3MpcpRemoteMACAddress,'dot3MpcpRegistrationState':dot3MpcpRegistrationState,'dot3MpcpTransmitElapsed':dot3MpcpTransmitElapsed,'dot3MpcpReceiveElapsed':dot3MpcpReceiveElapsed,'dot3MpcpRoundTripTime':dot3MpcpRoundTripTime,'dot3MpcpMaximumPendingGrants':dot3MpcpMaximumPendingGrants,'dot3MpcpStatTable':dot3MpcpStatTable,'dot3MpcpStatEntry':dot3MpcpStatEntry,'dot3MpcpMACCtrlFramesTransmitted':dot3MpcpMACCtrlFramesTransmitted,'dot3MpcpMACCtrlFramesReceived':dot3MpcpMACCtrlFramesReceived,'dot3MpcpDiscoveryWindowsSent':dot3MpcpDiscoveryWindowsSent,'dot3MpcpDiscoveryTimeout':dot3MpcpDiscoveryTimeout,'dot3MpcpTxRegRequest':dot3MpcpTxRegRequest,'dot3MpcpRxRegRequest':dot3MpcpRxRegRequest,'dot3MpcpTxRegAck':dot3MpcpTxRegAck,'dot3MpcpRxRegAck':dot3MpcpRxRegAck,'dot3MpcpTxReport':dot3MpcpTxReport,'dot3MpcpRxReport':dot3MpcpRxReport,'dot3MpcpTxGate':dot3MpcpTxGate,'dot3MpcpRxGate':dot3MpcpRxGate,'dot3MpcpTxRegister':dot3MpcpTxRegister,'dot3MpcpRxRegister':dot3MpcpRxRegister,'dot3OmpEmulationObjects':dot3OmpEmulationObjects,'dot3OmpEmulationTable':dot3OmpEmulationTable,'dot3OmpEmulationEntry':dot3OmpEmulationEntry,'dot3OmpEmulationType':dot3OmpEmulationType,'dot3OmpEmulationStatTable':dot3OmpEmulationStatTable,'dot3OmpEmulationStatEntry':dot3OmpEmulationStatEntry,'dot3OmpEmulationSLDErrors':dot3OmpEmulationSLDErrors,'dot3OmpEmulationCRC8Errors':dot3OmpEmulationCRC8Errors,'dot3OmpEmulationBadLLID':dot3OmpEmulationBadLLID,'dot3OmpEmulationGoodLLID':dot3OmpEmulationGoodLLID,'dot3OmpEmulationOnuPonCastLLID':dot3OmpEmulationOnuPonCastLLID,'dot3OmpEmulationOltPonCastLLID':dot3OmpEmulationOltPonCastLLID,'dot3OmpEmulationBroadcastBitNotOnuLlid':dot3OmpEmulationBroadcastBitNotOnuLlid,'dot3OmpEmulationOnuLLIDNotBroadcast':dot3OmpEmulationOnuLLIDNotBroadcast,'dot3OmpEmulationBroadcastBitPlusOnuLlid':dot3OmpEmulationBroadcastBitPlusOnuLlid,'dot3OmpEmulationNotBroadcastBitNotOnuLlid':dot3OmpEmulationNotBroadcastBitNotOnuLlid,'dot3EponFecObjects':dot3EponFecObjects,'dot3EponFecTable':dot3EponFecTable,'dot3EponFecEntry':dot3EponFecEntry,'dot3EponFecPCSCodingViolation':dot3EponFecPCSCodingViolation,'dot3EponFecAbility':dot3EponFecAbility,'dot3EponFecMode':dot3EponFecMode,'dot3EponFecCorrectedBlocks':dot3EponFecCorrectedBlocks,'dot3EponFecUncorrectableBlocks':dot3EponFecUncorrectableBlocks,'dot3EponFecBufferHeadCodingViolation':dot3EponFecBufferHeadCodingViolation,'dot3ExtPkgObjects':dot3ExtPkgObjects,'dot3ExtPkgControlObjects':dot3ExtPkgControlObjects,'dot3ExtPkgControlTable':dot3ExtPkgControlTable,'dot3ExtPkgControlEntry':dot3ExtPkgControlEntry,'dot3ExtPkgObjectReset':dot3ExtPkgObjectReset,'dot3ExtPkgObjectPowerDown':dot3ExtPkgObjectPowerDown,'dot3ExtPkgObjectNumberOfLLIDs':dot3ExtPkgObjectNumberOfLLIDs,'dot3ExtPkgObjectFecEnabled':dot3ExtPkgObjectFecEnabled,'dot3ExtPkgObjectReportMaximumNumQueues':dot3ExtPkgObjectReportMaximumNumQueues,'dot3ExtPkgObjectRegisterAction':dot3ExtPkgObjectRegisterAction,'dot3ExtPkgQueueTable':dot3ExtPkgQueueTable,'dot3ExtPkgQueueEntry':dot3ExtPkgQueueEntry,_P:dot3QueueIndex,'dot3ExtPkgObjectReportNumThreshold':dot3ExtPkgObjectReportNumThreshold,'dot3ExtPkgObjectReportMaximumNumThreshold':dot3ExtPkgObjectReportMaximumNumThreshold,'dot3ExtPkgStatTxFramesQueue':dot3ExtPkgStatTxFramesQueue,'dot3ExtPkgStatRxFramesQueue':dot3ExtPkgStatRxFramesQueue,'dot3ExtPkgStatDroppedFramesQueue':dot3ExtPkgStatDroppedFramesQueue,'dot3ExtPkgQueueSetsTable':dot3ExtPkgQueueSetsTable,'dot3ExtPkgQueueSetsEntry':dot3ExtPkgQueueSetsEntry,_Q:dot3QueueSetQueueIndex,_R:dot3QueueSetIndex,'dot3ExtPkgObjectReportThreshold':dot3ExtPkgObjectReportThreshold,'dot3ExtPkgOptIfTable':dot3ExtPkgOptIfTable,'dot3ExtPkgOptIfEntry':dot3ExtPkgOptIfEntry,'dot3ExtPkgOptIfSuspectedFlag':dot3ExtPkgOptIfSuspectedFlag,'dot3ExtPkgOptIfInputPower':dot3ExtPkgOptIfInputPower,'dot3ExtPkgOptIfLowInputPower':dot3ExtPkgOptIfLowInputPower,'dot3ExtPkgOptIfHighInputPower':dot3ExtPkgOptIfHighInputPower,'dot3ExtPkgOptIfLowerInputPowerThreshold':dot3ExtPkgOptIfLowerInputPowerThreshold,'dot3ExtPkgOptIfUpperInputPowerThreshold':dot3ExtPkgOptIfUpperInputPowerThreshold,'dot3ExtPkgOptIfOutputPower':dot3ExtPkgOptIfOutputPower,'dot3ExtPkgOptIfLowOutputPower':dot3ExtPkgOptIfLowOutputPower,'dot3ExtPkgOptIfHighOutputPower':dot3ExtPkgOptIfHighOutputPower,'dot3ExtPkgOptIfLowerOutputPowerThreshold':dot3ExtPkgOptIfLowerOutputPowerThreshold,'dot3ExtPkgOptIfUpperOutputPowerThreshold':dot3ExtPkgOptIfUpperOutputPowerThreshold,'dot3ExtPkgOptIfSignalDetect':dot3ExtPkgOptIfSignalDetect,'dot3ExtPkgOptIfTransmitAlarm':dot3ExtPkgOptIfTransmitAlarm,'dot3ExtPkgOptIfTransmitEnable':dot3ExtPkgOptIfTransmitEnable})