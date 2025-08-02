_AD='h3cDot3EponMauGroupFEC'
_AC='h3cDot3EponMauGroupAll'
_AB='h3cDot3OmpeGroupStat'
_AA='h3cDot3OmpeGroupID'
_A9='h3cDot3MpcpGroupStat'
_A8='h3cDot3MpcpGroupParam'
_A7='h3cDot3MpcpGroupBase'
_A6='h3cDot3EponMauBufferHeadCodingViolation'
_A5='h3cDot3EponMauFECUncorrectableBlocks'
_A4='h3cDot3EponMauFECCorrectedBlocks'
_A3='h3cDot3EponMauFecMode'
_A2='h3cDot3EponMauFecAbility'
_A1='h3cDot3EponMauPCSCodingViolation'
_A0='h3cDot3OmpEmulationNotBroadcastLLIDNotOnuId'
_z='h3cDot3OmpEmulationBroadcastLLIDPlusOnuId'
_y='h3cDot3OmpEmulationOnuLLIDNotBroadcast'
_x='h3cDot3OmpEmulationBroadcastLLIDNotOnuID'
_w='h3cDot3OmpEmulationOltPonCastLLID'
_v='h3cDot3OmpEmulationOnuPonCastLLID'
_u='h3cDot3OmpEmulationGoodLLID'
_t='h3cDot3OmpEmulationBadLLID'
_s='h3cDot3OmpEmulationCRC8Errors'
_r='h3cDot3OmpEmulationSLDErrors'
_q='h3cDot3OmpEmulationType'
_p='h3cDot3OmpEmulationID'
_o='h3cDot3MpcpRxNotSupportedMPCP'
_n='h3cDot3MpcpRxRegister'
_m='h3cDot3MpcpTxRegister'
_l='h3cDot3MpcpRxGate'
_k='h3cDot3MpcpTxGate'
_j='h3cDot3MpcpRxReport'
_i='h3cDot3MpcpTxReport'
_h='h3cDot3MpcpRxRegAck'
_g='h3cDot3MpcpTxRegAck'
_f='h3cDot3MpcpRxRegRequest'
_e='h3cDot3MpcpTxRegRequest'
_d='h3cDot3MpcpDiscoveryTimeout'
_c='h3cDot3MpcpDiscoveryWindowsSent'
_b='h3cDot3MpcpMACCtrlFramesReceived'
_a='h3cDot3MpcpMACCtrlFramesTransmitted'
_Z='h3cDot3MpcpSyncTime'
_Y='h3cDot3MpcpOffTime'
_X='h3cDot3MpcpOnTime'
_W='h3cDot3MpcpRoundTripTime'
_V='h3cDot3MpcpReceiveElapsed'
_U='h3cDot3MpcpTransmitElapsed'
_T='h3cDot3MpcpAdminState'
_S='h3cDot3MpcpMaximumPendingGrants'
_R='h3cDot3MpcpRegistrationState'
_Q='h3cDot3MpcpRemoteMACAddress'
_P='h3cDot3MpcpLinkID'
_O='h3cDot3MpcpMode'
_N='h3cDot3MpcpOperStatus'
_M='h3cDot3MpcpID'
_L='octets'
_K='TruthValue'
_J='unknown'
_I='read-write'
_H='TQ (16nsec)'
_G='ifIndex'
_F='IF-MIB'
_E='Integer32'
_D='frames'
_C='read-only'
_B='H3C-DOT3-EFM-EPON-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
h3cEpon,=mibBuilder.importSymbols('HUAWEI-3COM-OID-MIB','h3cEpon')
ifIndex,=mibBuilder.importSymbols(_F,_G)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso,mib_2=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso','mib-2')
DisplayString,MacAddress,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','TextualConvention',_K)
h3cDot3EfmeponMIB=ModuleIdentity((1,3,6,1,4,1,2011,10,2,42,2))
if mibBuilder.loadTexts:h3cDot3EfmeponMIB.setRevisions(('2004-09-21 00:00',))
_H3cDot3MpcpMIB_ObjectIdentity=ObjectIdentity
h3cDot3MpcpMIB=_H3cDot3MpcpMIB_ObjectIdentity((1,3,6,1,4,1,2011,10,2,42,2,1))
_H3cDot3MpcpObjects_ObjectIdentity=ObjectIdentity
h3cDot3MpcpObjects=_H3cDot3MpcpObjects_ObjectIdentity((1,3,6,1,4,1,2011,10,2,42,2,1,1))
_H3cDot3MpcpTable_Object=MibTable
h3cDot3MpcpTable=_H3cDot3MpcpTable_Object((1,3,6,1,4,1,2011,10,2,42,2,1,1,1))
if mibBuilder.loadTexts:h3cDot3MpcpTable.setStatus(_A)
_H3cDot3MpcpEntry_Object=MibTableRow
h3cDot3MpcpEntry=_H3cDot3MpcpEntry_Object((1,3,6,1,4,1,2011,10,2,42,2,1,1,1,1))
h3cDot3MpcpEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:h3cDot3MpcpEntry.setStatus(_A)
_H3cDot3MpcpID_Type=Integer32
_H3cDot3MpcpID_Object=MibTableColumn
h3cDot3MpcpID=_H3cDot3MpcpID_Object((1,3,6,1,4,1,2011,10,2,42,2,1,1,1,1,1),_H3cDot3MpcpID_Type())
h3cDot3MpcpID.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cDot3MpcpID.setStatus(_A)
_H3cDot3MpcpOperStatus_Type=TruthValue
_H3cDot3MpcpOperStatus_Object=MibTableColumn
h3cDot3MpcpOperStatus=_H3cDot3MpcpOperStatus_Object((1,3,6,1,4,1,2011,10,2,42,2,1,1,1,1,2),_H3cDot3MpcpOperStatus_Type())
h3cDot3MpcpOperStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cDot3MpcpOperStatus.setStatus(_A)
class _H3cDot3MpcpMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('olt',1),('onu',2)))
_H3cDot3MpcpMode_Type.__name__=_E
_H3cDot3MpcpMode_Object=MibTableColumn
h3cDot3MpcpMode=_H3cDot3MpcpMode_Object((1,3,6,1,4,1,2011,10,2,42,2,1,1,1,1,3),_H3cDot3MpcpMode_Type())
h3cDot3MpcpMode.setMaxAccess(_I)
if mibBuilder.loadTexts:h3cDot3MpcpMode.setStatus(_A)
_H3cDot3MpcpLinkID_Type=Integer32
_H3cDot3MpcpLinkID_Object=MibTableColumn
h3cDot3MpcpLinkID=_H3cDot3MpcpLinkID_Object((1,3,6,1,4,1,2011,10,2,42,2,1,1,1,1,4),_H3cDot3MpcpLinkID_Type())
h3cDot3MpcpLinkID.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cDot3MpcpLinkID.setStatus(_A)
_H3cDot3MpcpRemoteMACAddress_Type=MacAddress
_H3cDot3MpcpRemoteMACAddress_Object=MibTableColumn
h3cDot3MpcpRemoteMACAddress=_H3cDot3MpcpRemoteMACAddress_Object((1,3,6,1,4,1,2011,10,2,42,2,1,1,1,1,5),_H3cDot3MpcpRemoteMACAddress_Type())
h3cDot3MpcpRemoteMACAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cDot3MpcpRemoteMACAddress.setStatus(_A)
class _H3cDot3MpcpRegistrationState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('unregistered',1),('registering',2),('registered',3)))
_H3cDot3MpcpRegistrationState_Type.__name__=_E
_H3cDot3MpcpRegistrationState_Object=MibTableColumn
h3cDot3MpcpRegistrationState=_H3cDot3MpcpRegistrationState_Object((1,3,6,1,4,1,2011,10,2,42,2,1,1,1,1,6),_H3cDot3MpcpRegistrationState_Type())
h3cDot3MpcpRegistrationState.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cDot3MpcpRegistrationState.setStatus(_A)
_H3cDot3MpcpTransmitElapsed_Type=Integer32
_H3cDot3MpcpTransmitElapsed_Object=MibTableColumn
h3cDot3MpcpTransmitElapsed=_H3cDot3MpcpTransmitElapsed_Object((1,3,6,1,4,1,2011,10,2,42,2,1,1,1,1,7),_H3cDot3MpcpTransmitElapsed_Type())
h3cDot3MpcpTransmitElapsed.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cDot3MpcpTransmitElapsed.setStatus(_A)
if mibBuilder.loadTexts:h3cDot3MpcpTransmitElapsed.setUnits(_H)
_H3cDot3MpcpReceiveElapsed_Type=Integer32
_H3cDot3MpcpReceiveElapsed_Object=MibTableColumn
h3cDot3MpcpReceiveElapsed=_H3cDot3MpcpReceiveElapsed_Object((1,3,6,1,4,1,2011,10,2,42,2,1,1,1,1,8),_H3cDot3MpcpReceiveElapsed_Type())
h3cDot3MpcpReceiveElapsed.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cDot3MpcpReceiveElapsed.setStatus(_A)
if mibBuilder.loadTexts:h3cDot3MpcpReceiveElapsed.setUnits(_H)
_H3cDot3MpcpRoundTripTime_Type=Integer32
_H3cDot3MpcpRoundTripTime_Object=MibTableColumn
h3cDot3MpcpRoundTripTime=_H3cDot3MpcpRoundTripTime_Object((1,3,6,1,4,1,2011,10,2,42,2,1,1,1,1,9),_H3cDot3MpcpRoundTripTime_Type())
h3cDot3MpcpRoundTripTime.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cDot3MpcpRoundTripTime.setStatus(_A)
if mibBuilder.loadTexts:h3cDot3MpcpRoundTripTime.setUnits(_H)
class _H3cDot3MpcpMaximumPendingGrants_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_H3cDot3MpcpMaximumPendingGrants_Type.__name__=_E
_H3cDot3MpcpMaximumPendingGrants_Object=MibTableColumn
h3cDot3MpcpMaximumPendingGrants=_H3cDot3MpcpMaximumPendingGrants_Object((1,3,6,1,4,1,2011,10,2,42,2,1,1,1,1,10),_H3cDot3MpcpMaximumPendingGrants_Type())
h3cDot3MpcpMaximumPendingGrants.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cDot3MpcpMaximumPendingGrants.setStatus(_A)
class _H3cDot3MpcpAdminState_Type(TruthValue):defaultValue=2
_H3cDot3MpcpAdminState_Type.__name__=_K
_H3cDot3MpcpAdminState_Object=MibTableColumn
h3cDot3MpcpAdminState=_H3cDot3MpcpAdminState_Object((1,3,6,1,4,1,2011,10,2,42,2,1,1,1,1,11),_H3cDot3MpcpAdminState_Type())
h3cDot3MpcpAdminState.setMaxAccess(_I)
if mibBuilder.loadTexts:h3cDot3MpcpAdminState.setStatus(_A)
_H3cDot3MpcpOnTime_Type=Integer32
_H3cDot3MpcpOnTime_Object=MibTableColumn
h3cDot3MpcpOnTime=_H3cDot3MpcpOnTime_Object((1,3,6,1,4,1,2011,10,2,42,2,1,1,1,1,12),_H3cDot3MpcpOnTime_Type())
h3cDot3MpcpOnTime.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cDot3MpcpOnTime.setStatus(_A)
if mibBuilder.loadTexts:h3cDot3MpcpOnTime.setUnits(_H)
_H3cDot3MpcpOffTime_Type=Integer32
_H3cDot3MpcpOffTime_Object=MibTableColumn
h3cDot3MpcpOffTime=_H3cDot3MpcpOffTime_Object((1,3,6,1,4,1,2011,10,2,42,2,1,1,1,1,13),_H3cDot3MpcpOffTime_Type())
h3cDot3MpcpOffTime.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cDot3MpcpOffTime.setStatus(_A)
if mibBuilder.loadTexts:h3cDot3MpcpOffTime.setUnits(_H)
_H3cDot3MpcpSyncTime_Type=Integer32
_H3cDot3MpcpSyncTime_Object=MibTableColumn
h3cDot3MpcpSyncTime=_H3cDot3MpcpSyncTime_Object((1,3,6,1,4,1,2011,10,2,42,2,1,1,1,1,14),_H3cDot3MpcpSyncTime_Type())
h3cDot3MpcpSyncTime.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cDot3MpcpSyncTime.setStatus(_A)
if mibBuilder.loadTexts:h3cDot3MpcpSyncTime.setUnits(_H)
_H3cDot3MpcpStatTable_Object=MibTable
h3cDot3MpcpStatTable=_H3cDot3MpcpStatTable_Object((1,3,6,1,4,1,2011,10,2,42,2,1,1,2))
if mibBuilder.loadTexts:h3cDot3MpcpStatTable.setStatus(_A)
_H3cDot3MpcpStatEntry_Object=MibTableRow
h3cDot3MpcpStatEntry=_H3cDot3MpcpStatEntry_Object((1,3,6,1,4,1,2011,10,2,42,2,1,1,2,1))
h3cDot3MpcpStatEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:h3cDot3MpcpStatEntry.setStatus(_A)
_H3cDot3MpcpMACCtrlFramesTransmitted_Type=Counter32
_H3cDot3MpcpMACCtrlFramesTransmitted_Object=MibTableColumn
h3cDot3MpcpMACCtrlFramesTransmitted=_H3cDot3MpcpMACCtrlFramesTransmitted_Object((1,3,6,1,4,1,2011,10,2,42,2,1,1,2,1,1),_H3cDot3MpcpMACCtrlFramesTransmitted_Type())
h3cDot3MpcpMACCtrlFramesTransmitted.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cDot3MpcpMACCtrlFramesTransmitted.setStatus(_A)
if mibBuilder.loadTexts:h3cDot3MpcpMACCtrlFramesTransmitted.setUnits(_D)
_H3cDot3MpcpMACCtrlFramesReceived_Type=Counter32
_H3cDot3MpcpMACCtrlFramesReceived_Object=MibTableColumn
h3cDot3MpcpMACCtrlFramesReceived=_H3cDot3MpcpMACCtrlFramesReceived_Object((1,3,6,1,4,1,2011,10,2,42,2,1,1,2,1,2),_H3cDot3MpcpMACCtrlFramesReceived_Type())
h3cDot3MpcpMACCtrlFramesReceived.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cDot3MpcpMACCtrlFramesReceived.setStatus(_A)
if mibBuilder.loadTexts:h3cDot3MpcpMACCtrlFramesReceived.setUnits(_D)
_H3cDot3MpcpDiscoveryWindowsSent_Type=Counter32
_H3cDot3MpcpDiscoveryWindowsSent_Object=MibTableColumn
h3cDot3MpcpDiscoveryWindowsSent=_H3cDot3MpcpDiscoveryWindowsSent_Object((1,3,6,1,4,1,2011,10,2,42,2,1,1,2,1,3),_H3cDot3MpcpDiscoveryWindowsSent_Type())
h3cDot3MpcpDiscoveryWindowsSent.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cDot3MpcpDiscoveryWindowsSent.setStatus(_A)
_H3cDot3MpcpDiscoveryTimeout_Type=Counter32
_H3cDot3MpcpDiscoveryTimeout_Object=MibTableColumn
h3cDot3MpcpDiscoveryTimeout=_H3cDot3MpcpDiscoveryTimeout_Object((1,3,6,1,4,1,2011,10,2,42,2,1,1,2,1,4),_H3cDot3MpcpDiscoveryTimeout_Type())
h3cDot3MpcpDiscoveryTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cDot3MpcpDiscoveryTimeout.setStatus(_A)
_H3cDot3MpcpTxRegRequest_Type=Counter32
_H3cDot3MpcpTxRegRequest_Object=MibTableColumn
h3cDot3MpcpTxRegRequest=_H3cDot3MpcpTxRegRequest_Object((1,3,6,1,4,1,2011,10,2,42,2,1,1,2,1,5),_H3cDot3MpcpTxRegRequest_Type())
h3cDot3MpcpTxRegRequest.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cDot3MpcpTxRegRequest.setStatus(_A)
if mibBuilder.loadTexts:h3cDot3MpcpTxRegRequest.setUnits(_D)
_H3cDot3MpcpRxRegRequest_Type=Counter32
_H3cDot3MpcpRxRegRequest_Object=MibTableColumn
h3cDot3MpcpRxRegRequest=_H3cDot3MpcpRxRegRequest_Object((1,3,6,1,4,1,2011,10,2,42,2,1,1,2,1,6),_H3cDot3MpcpRxRegRequest_Type())
h3cDot3MpcpRxRegRequest.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cDot3MpcpRxRegRequest.setStatus(_A)
if mibBuilder.loadTexts:h3cDot3MpcpRxRegRequest.setUnits(_D)
_H3cDot3MpcpTxRegAck_Type=Counter32
_H3cDot3MpcpTxRegAck_Object=MibTableColumn
h3cDot3MpcpTxRegAck=_H3cDot3MpcpTxRegAck_Object((1,3,6,1,4,1,2011,10,2,42,2,1,1,2,1,7),_H3cDot3MpcpTxRegAck_Type())
h3cDot3MpcpTxRegAck.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cDot3MpcpTxRegAck.setStatus(_A)
if mibBuilder.loadTexts:h3cDot3MpcpTxRegAck.setUnits(_D)
_H3cDot3MpcpRxRegAck_Type=Counter32
_H3cDot3MpcpRxRegAck_Object=MibTableColumn
h3cDot3MpcpRxRegAck=_H3cDot3MpcpRxRegAck_Object((1,3,6,1,4,1,2011,10,2,42,2,1,1,2,1,8),_H3cDot3MpcpRxRegAck_Type())
h3cDot3MpcpRxRegAck.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cDot3MpcpRxRegAck.setStatus(_A)
if mibBuilder.loadTexts:h3cDot3MpcpRxRegAck.setUnits(_D)
_H3cDot3MpcpTxReport_Type=Counter32
_H3cDot3MpcpTxReport_Object=MibTableColumn
h3cDot3MpcpTxReport=_H3cDot3MpcpTxReport_Object((1,3,6,1,4,1,2011,10,2,42,2,1,1,2,1,9),_H3cDot3MpcpTxReport_Type())
h3cDot3MpcpTxReport.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cDot3MpcpTxReport.setStatus(_A)
if mibBuilder.loadTexts:h3cDot3MpcpTxReport.setUnits(_D)
_H3cDot3MpcpRxReport_Type=Counter32
_H3cDot3MpcpRxReport_Object=MibTableColumn
h3cDot3MpcpRxReport=_H3cDot3MpcpRxReport_Object((1,3,6,1,4,1,2011,10,2,42,2,1,1,2,1,10),_H3cDot3MpcpRxReport_Type())
h3cDot3MpcpRxReport.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cDot3MpcpRxReport.setStatus(_A)
if mibBuilder.loadTexts:h3cDot3MpcpRxReport.setUnits(_D)
_H3cDot3MpcpTxGate_Type=Counter32
_H3cDot3MpcpTxGate_Object=MibTableColumn
h3cDot3MpcpTxGate=_H3cDot3MpcpTxGate_Object((1,3,6,1,4,1,2011,10,2,42,2,1,1,2,1,11),_H3cDot3MpcpTxGate_Type())
h3cDot3MpcpTxGate.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cDot3MpcpTxGate.setStatus(_A)
if mibBuilder.loadTexts:h3cDot3MpcpTxGate.setUnits(_D)
_H3cDot3MpcpRxGate_Type=Counter32
_H3cDot3MpcpRxGate_Object=MibTableColumn
h3cDot3MpcpRxGate=_H3cDot3MpcpRxGate_Object((1,3,6,1,4,1,2011,10,2,42,2,1,1,2,1,12),_H3cDot3MpcpRxGate_Type())
h3cDot3MpcpRxGate.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cDot3MpcpRxGate.setStatus(_A)
if mibBuilder.loadTexts:h3cDot3MpcpRxGate.setUnits(_D)
_H3cDot3MpcpTxRegister_Type=Counter32
_H3cDot3MpcpTxRegister_Object=MibTableColumn
h3cDot3MpcpTxRegister=_H3cDot3MpcpTxRegister_Object((1,3,6,1,4,1,2011,10,2,42,2,1,1,2,1,13),_H3cDot3MpcpTxRegister_Type())
h3cDot3MpcpTxRegister.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cDot3MpcpTxRegister.setStatus(_A)
if mibBuilder.loadTexts:h3cDot3MpcpTxRegister.setUnits(_D)
_H3cDot3MpcpRxRegister_Type=Counter32
_H3cDot3MpcpRxRegister_Object=MibTableColumn
h3cDot3MpcpRxRegister=_H3cDot3MpcpRxRegister_Object((1,3,6,1,4,1,2011,10,2,42,2,1,1,2,1,14),_H3cDot3MpcpRxRegister_Type())
h3cDot3MpcpRxRegister.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cDot3MpcpRxRegister.setStatus(_A)
if mibBuilder.loadTexts:h3cDot3MpcpRxRegister.setUnits(_D)
_H3cDot3MpcpRxNotSupportedMPCP_Type=Counter32
_H3cDot3MpcpRxNotSupportedMPCP_Object=MibTableColumn
h3cDot3MpcpRxNotSupportedMPCP=_H3cDot3MpcpRxNotSupportedMPCP_Object((1,3,6,1,4,1,2011,10,2,42,2,1,1,2,1,15),_H3cDot3MpcpRxNotSupportedMPCP_Type())
h3cDot3MpcpRxNotSupportedMPCP.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cDot3MpcpRxNotSupportedMPCP.setStatus(_A)
if mibBuilder.loadTexts:h3cDot3MpcpRxNotSupportedMPCP.setUnits(_D)
_H3cDot3MpcpConformance_ObjectIdentity=ObjectIdentity
h3cDot3MpcpConformance=_H3cDot3MpcpConformance_ObjectIdentity((1,3,6,1,4,1,2011,10,2,42,2,1,2))
_H3cDot3MpcpGroups_ObjectIdentity=ObjectIdentity
h3cDot3MpcpGroups=_H3cDot3MpcpGroups_ObjectIdentity((1,3,6,1,4,1,2011,10,2,42,2,1,2,1))
_H3cDot3MpcpCompliances_ObjectIdentity=ObjectIdentity
h3cDot3MpcpCompliances=_H3cDot3MpcpCompliances_ObjectIdentity((1,3,6,1,4,1,2011,10,2,42,2,1,2,2))
_H3cDot3OmpEmulationMIB_ObjectIdentity=ObjectIdentity
h3cDot3OmpEmulationMIB=_H3cDot3OmpEmulationMIB_ObjectIdentity((1,3,6,1,4,1,2011,10,2,42,2,2))
_H3cDot3OmpEmulationObjects_ObjectIdentity=ObjectIdentity
h3cDot3OmpEmulationObjects=_H3cDot3OmpEmulationObjects_ObjectIdentity((1,3,6,1,4,1,2011,10,2,42,2,2,1))
_H3cDot3OmpEmulationTable_Object=MibTable
h3cDot3OmpEmulationTable=_H3cDot3OmpEmulationTable_Object((1,3,6,1,4,1,2011,10,2,42,2,2,1,1))
if mibBuilder.loadTexts:h3cDot3OmpEmulationTable.setStatus(_A)
_H3cDot3OmpEmulationEntry_Object=MibTableRow
h3cDot3OmpEmulationEntry=_H3cDot3OmpEmulationEntry_Object((1,3,6,1,4,1,2011,10,2,42,2,2,1,1,1))
h3cDot3OmpEmulationEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:h3cDot3OmpEmulationEntry.setStatus(_A)
_H3cDot3OmpEmulationID_Type=Integer32
_H3cDot3OmpEmulationID_Object=MibTableColumn
h3cDot3OmpEmulationID=_H3cDot3OmpEmulationID_Object((1,3,6,1,4,1,2011,10,2,42,2,2,1,1,1,1),_H3cDot3OmpEmulationID_Type())
h3cDot3OmpEmulationID.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cDot3OmpEmulationID.setStatus(_A)
class _H3cDot3OmpEmulationType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_J,1),('olt',2),('onu',3)))
_H3cDot3OmpEmulationType_Type.__name__=_E
_H3cDot3OmpEmulationType_Object=MibTableColumn
h3cDot3OmpEmulationType=_H3cDot3OmpEmulationType_Object((1,3,6,1,4,1,2011,10,2,42,2,2,1,1,1,2),_H3cDot3OmpEmulationType_Type())
h3cDot3OmpEmulationType.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cDot3OmpEmulationType.setStatus(_A)
_H3cDot3OmpEmulationStatTable_Object=MibTable
h3cDot3OmpEmulationStatTable=_H3cDot3OmpEmulationStatTable_Object((1,3,6,1,4,1,2011,10,2,42,2,2,1,2))
if mibBuilder.loadTexts:h3cDot3OmpEmulationStatTable.setStatus(_A)
_H3cDot3OmpEmulationStatEntry_Object=MibTableRow
h3cDot3OmpEmulationStatEntry=_H3cDot3OmpEmulationStatEntry_Object((1,3,6,1,4,1,2011,10,2,42,2,2,1,2,1))
h3cDot3OmpEmulationStatEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:h3cDot3OmpEmulationStatEntry.setStatus(_A)
_H3cDot3OmpEmulationSLDErrors_Type=Counter32
_H3cDot3OmpEmulationSLDErrors_Object=MibTableColumn
h3cDot3OmpEmulationSLDErrors=_H3cDot3OmpEmulationSLDErrors_Object((1,3,6,1,4,1,2011,10,2,42,2,2,1,2,1,1),_H3cDot3OmpEmulationSLDErrors_Type())
h3cDot3OmpEmulationSLDErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cDot3OmpEmulationSLDErrors.setStatus(_A)
if mibBuilder.loadTexts:h3cDot3OmpEmulationSLDErrors.setUnits(_D)
_H3cDot3OmpEmulationCRC8Errors_Type=Counter32
_H3cDot3OmpEmulationCRC8Errors_Object=MibTableColumn
h3cDot3OmpEmulationCRC8Errors=_H3cDot3OmpEmulationCRC8Errors_Object((1,3,6,1,4,1,2011,10,2,42,2,2,1,2,1,2),_H3cDot3OmpEmulationCRC8Errors_Type())
h3cDot3OmpEmulationCRC8Errors.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cDot3OmpEmulationCRC8Errors.setStatus(_A)
if mibBuilder.loadTexts:h3cDot3OmpEmulationCRC8Errors.setUnits(_D)
_H3cDot3OmpEmulationBadLLID_Type=Counter32
_H3cDot3OmpEmulationBadLLID_Object=MibTableColumn
h3cDot3OmpEmulationBadLLID=_H3cDot3OmpEmulationBadLLID_Object((1,3,6,1,4,1,2011,10,2,42,2,2,1,2,1,3),_H3cDot3OmpEmulationBadLLID_Type())
h3cDot3OmpEmulationBadLLID.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cDot3OmpEmulationBadLLID.setStatus(_A)
if mibBuilder.loadTexts:h3cDot3OmpEmulationBadLLID.setUnits(_D)
_H3cDot3OmpEmulationGoodLLID_Type=Counter32
_H3cDot3OmpEmulationGoodLLID_Object=MibTableColumn
h3cDot3OmpEmulationGoodLLID=_H3cDot3OmpEmulationGoodLLID_Object((1,3,6,1,4,1,2011,10,2,42,2,2,1,2,1,4),_H3cDot3OmpEmulationGoodLLID_Type())
h3cDot3OmpEmulationGoodLLID.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cDot3OmpEmulationGoodLLID.setStatus(_A)
if mibBuilder.loadTexts:h3cDot3OmpEmulationGoodLLID.setUnits(_D)
_H3cDot3OmpEmulationOnuPonCastLLID_Type=Counter32
_H3cDot3OmpEmulationOnuPonCastLLID_Object=MibTableColumn
h3cDot3OmpEmulationOnuPonCastLLID=_H3cDot3OmpEmulationOnuPonCastLLID_Object((1,3,6,1,4,1,2011,10,2,42,2,2,1,2,1,5),_H3cDot3OmpEmulationOnuPonCastLLID_Type())
h3cDot3OmpEmulationOnuPonCastLLID.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cDot3OmpEmulationOnuPonCastLLID.setStatus(_A)
if mibBuilder.loadTexts:h3cDot3OmpEmulationOnuPonCastLLID.setUnits(_D)
_H3cDot3OmpEmulationOltPonCastLLID_Type=Counter32
_H3cDot3OmpEmulationOltPonCastLLID_Object=MibTableColumn
h3cDot3OmpEmulationOltPonCastLLID=_H3cDot3OmpEmulationOltPonCastLLID_Object((1,3,6,1,4,1,2011,10,2,42,2,2,1,2,1,6),_H3cDot3OmpEmulationOltPonCastLLID_Type())
h3cDot3OmpEmulationOltPonCastLLID.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cDot3OmpEmulationOltPonCastLLID.setStatus(_A)
if mibBuilder.loadTexts:h3cDot3OmpEmulationOltPonCastLLID.setUnits(_D)
_H3cDot3OmpEmulationBroadcastLLIDNotOnuID_Type=Counter32
_H3cDot3OmpEmulationBroadcastLLIDNotOnuID_Object=MibTableColumn
h3cDot3OmpEmulationBroadcastLLIDNotOnuID=_H3cDot3OmpEmulationBroadcastLLIDNotOnuID_Object((1,3,6,1,4,1,2011,10,2,42,2,2,1,2,1,7),_H3cDot3OmpEmulationBroadcastLLIDNotOnuID_Type())
h3cDot3OmpEmulationBroadcastLLIDNotOnuID.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cDot3OmpEmulationBroadcastLLIDNotOnuID.setStatus(_A)
if mibBuilder.loadTexts:h3cDot3OmpEmulationBroadcastLLIDNotOnuID.setUnits(_D)
_H3cDot3OmpEmulationOnuLLIDNotBroadcast_Type=Counter32
_H3cDot3OmpEmulationOnuLLIDNotBroadcast_Object=MibTableColumn
h3cDot3OmpEmulationOnuLLIDNotBroadcast=_H3cDot3OmpEmulationOnuLLIDNotBroadcast_Object((1,3,6,1,4,1,2011,10,2,42,2,2,1,2,1,8),_H3cDot3OmpEmulationOnuLLIDNotBroadcast_Type())
h3cDot3OmpEmulationOnuLLIDNotBroadcast.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cDot3OmpEmulationOnuLLIDNotBroadcast.setStatus(_A)
if mibBuilder.loadTexts:h3cDot3OmpEmulationOnuLLIDNotBroadcast.setUnits(_D)
_H3cDot3OmpEmulationBroadcastLLIDPlusOnuId_Type=Counter32
_H3cDot3OmpEmulationBroadcastLLIDPlusOnuId_Object=MibTableColumn
h3cDot3OmpEmulationBroadcastLLIDPlusOnuId=_H3cDot3OmpEmulationBroadcastLLIDPlusOnuId_Object((1,3,6,1,4,1,2011,10,2,42,2,2,1,2,1,9),_H3cDot3OmpEmulationBroadcastLLIDPlusOnuId_Type())
h3cDot3OmpEmulationBroadcastLLIDPlusOnuId.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cDot3OmpEmulationBroadcastLLIDPlusOnuId.setStatus(_A)
if mibBuilder.loadTexts:h3cDot3OmpEmulationBroadcastLLIDPlusOnuId.setUnits(_D)
_H3cDot3OmpEmulationNotBroadcastLLIDNotOnuId_Type=Counter32
_H3cDot3OmpEmulationNotBroadcastLLIDNotOnuId_Object=MibTableColumn
h3cDot3OmpEmulationNotBroadcastLLIDNotOnuId=_H3cDot3OmpEmulationNotBroadcastLLIDNotOnuId_Object((1,3,6,1,4,1,2011,10,2,42,2,2,1,2,1,10),_H3cDot3OmpEmulationNotBroadcastLLIDNotOnuId_Type())
h3cDot3OmpEmulationNotBroadcastLLIDNotOnuId.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cDot3OmpEmulationNotBroadcastLLIDNotOnuId.setStatus(_A)
if mibBuilder.loadTexts:h3cDot3OmpEmulationNotBroadcastLLIDNotOnuId.setUnits(_D)
_H3cDot3OmpeConformance_ObjectIdentity=ObjectIdentity
h3cDot3OmpeConformance=_H3cDot3OmpeConformance_ObjectIdentity((1,3,6,1,4,1,2011,10,2,42,2,2,2))
_H3cDot3OmpeGroups_ObjectIdentity=ObjectIdentity
h3cDot3OmpeGroups=_H3cDot3OmpeGroups_ObjectIdentity((1,3,6,1,4,1,2011,10,2,42,2,2,2,1))
_H3cDot3OmpeCompliances_ObjectIdentity=ObjectIdentity
h3cDot3OmpeCompliances=_H3cDot3OmpeCompliances_ObjectIdentity((1,3,6,1,4,1,2011,10,2,42,2,2,2,2))
_H3cDot3EponMauMIB_ObjectIdentity=ObjectIdentity
h3cDot3EponMauMIB=_H3cDot3EponMauMIB_ObjectIdentity((1,3,6,1,4,1,2011,10,2,42,2,3))
_H3cDot3EponMauObjects_ObjectIdentity=ObjectIdentity
h3cDot3EponMauObjects=_H3cDot3EponMauObjects_ObjectIdentity((1,3,6,1,4,1,2011,10,2,42,2,3,1))
_H3cDot3EponMauTable_Object=MibTable
h3cDot3EponMauTable=_H3cDot3EponMauTable_Object((1,3,6,1,4,1,2011,10,2,42,2,3,1,1))
if mibBuilder.loadTexts:h3cDot3EponMauTable.setStatus(_A)
_H3cDot3EponMauEntry_Object=MibTableRow
h3cDot3EponMauEntry=_H3cDot3EponMauEntry_Object((1,3,6,1,4,1,2011,10,2,42,2,3,1,1,1))
h3cDot3EponMauEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:h3cDot3EponMauEntry.setStatus(_A)
_H3cDot3EponMauPCSCodingViolation_Type=Counter32
_H3cDot3EponMauPCSCodingViolation_Object=MibTableColumn
h3cDot3EponMauPCSCodingViolation=_H3cDot3EponMauPCSCodingViolation_Object((1,3,6,1,4,1,2011,10,2,42,2,3,1,1,1,1),_H3cDot3EponMauPCSCodingViolation_Type())
h3cDot3EponMauPCSCodingViolation.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cDot3EponMauPCSCodingViolation.setStatus(_A)
if mibBuilder.loadTexts:h3cDot3EponMauPCSCodingViolation.setUnits(_L)
class _H3cDot3EponMauFecAbility_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_J,1),('nonsupported',2),('supported',3)))
_H3cDot3EponMauFecAbility_Type.__name__=_E
_H3cDot3EponMauFecAbility_Object=MibTableColumn
h3cDot3EponMauFecAbility=_H3cDot3EponMauFecAbility_Object((1,3,6,1,4,1,2011,10,2,42,2,3,1,1,1,2),_H3cDot3EponMauFecAbility_Type())
h3cDot3EponMauFecAbility.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cDot3EponMauFecAbility.setStatus(_A)
class _H3cDot3EponMauFecMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_J,1),('disabled',2),('enabled',3)))
_H3cDot3EponMauFecMode_Type.__name__=_E
_H3cDot3EponMauFecMode_Object=MibTableColumn
h3cDot3EponMauFecMode=_H3cDot3EponMauFecMode_Object((1,3,6,1,4,1,2011,10,2,42,2,3,1,1,1,3),_H3cDot3EponMauFecMode_Type())
h3cDot3EponMauFecMode.setMaxAccess(_I)
if mibBuilder.loadTexts:h3cDot3EponMauFecMode.setStatus(_A)
_H3cDot3EponMauFECCorrectedBlocks_Type=Counter32
_H3cDot3EponMauFECCorrectedBlocks_Object=MibTableColumn
h3cDot3EponMauFECCorrectedBlocks=_H3cDot3EponMauFECCorrectedBlocks_Object((1,3,6,1,4,1,2011,10,2,42,2,3,1,1,1,4),_H3cDot3EponMauFECCorrectedBlocks_Type())
h3cDot3EponMauFECCorrectedBlocks.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cDot3EponMauFECCorrectedBlocks.setStatus(_A)
_H3cDot3EponMauFECUncorrectableBlocks_Type=Counter32
_H3cDot3EponMauFECUncorrectableBlocks_Object=MibTableColumn
h3cDot3EponMauFECUncorrectableBlocks=_H3cDot3EponMauFECUncorrectableBlocks_Object((1,3,6,1,4,1,2011,10,2,42,2,3,1,1,1,5),_H3cDot3EponMauFECUncorrectableBlocks_Type())
h3cDot3EponMauFECUncorrectableBlocks.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cDot3EponMauFECUncorrectableBlocks.setStatus(_A)
_H3cDot3EponMauBufferHeadCodingViolation_Type=Counter32
_H3cDot3EponMauBufferHeadCodingViolation_Object=MibTableColumn
h3cDot3EponMauBufferHeadCodingViolation=_H3cDot3EponMauBufferHeadCodingViolation_Object((1,3,6,1,4,1,2011,10,2,42,2,3,1,1,1,6),_H3cDot3EponMauBufferHeadCodingViolation_Type())
h3cDot3EponMauBufferHeadCodingViolation.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cDot3EponMauBufferHeadCodingViolation.setStatus(_A)
if mibBuilder.loadTexts:h3cDot3EponMauBufferHeadCodingViolation.setUnits(_L)
_H3cDot3EponMauConformance_ObjectIdentity=ObjectIdentity
h3cDot3EponMauConformance=_H3cDot3EponMauConformance_ObjectIdentity((1,3,6,1,4,1,2011,10,2,42,2,3,2))
_H3cDot3EponMauGroups_ObjectIdentity=ObjectIdentity
h3cDot3EponMauGroups=_H3cDot3EponMauGroups_ObjectIdentity((1,3,6,1,4,1,2011,10,2,42,2,3,2,1))
_H3cDot3EponMauCompliances_ObjectIdentity=ObjectIdentity
h3cDot3EponMauCompliances=_H3cDot3EponMauCompliances_ObjectIdentity((1,3,6,1,4,1,2011,10,2,42,2,3,2,2))
_H3cDot3EponMauType_ObjectIdentity=ObjectIdentity
h3cDot3EponMauType=_H3cDot3EponMauType_ObjectIdentity((1,3,6,1,4,1,2011,10,2,42,2,3,3))
_H3cEponMauType1000BasePXOLT_ObjectIdentity=ObjectIdentity
h3cEponMauType1000BasePXOLT=_H3cEponMauType1000BasePXOLT_ObjectIdentity((1,3,6,1,4,1,2011,10,2,42,2,3,3,1))
if mibBuilder.loadTexts:h3cEponMauType1000BasePXOLT.setStatus(_A)
_H3cEponMauType1000BasePXONU_ObjectIdentity=ObjectIdentity
h3cEponMauType1000BasePXONU=_H3cEponMauType1000BasePXONU_ObjectIdentity((1,3,6,1,4,1,2011,10,2,42,2,3,3,2))
if mibBuilder.loadTexts:h3cEponMauType1000BasePXONU.setStatus(_A)
_H3cEponMauType1000BasePX10DOLT_ObjectIdentity=ObjectIdentity
h3cEponMauType1000BasePX10DOLT=_H3cEponMauType1000BasePX10DOLT_ObjectIdentity((1,3,6,1,4,1,2011,10,2,42,2,3,3,3))
if mibBuilder.loadTexts:h3cEponMauType1000BasePX10DOLT.setStatus(_A)
_H3cEponMauType1000BasePX10DONU_ObjectIdentity=ObjectIdentity
h3cEponMauType1000BasePX10DONU=_H3cEponMauType1000BasePX10DONU_ObjectIdentity((1,3,6,1,4,1,2011,10,2,42,2,3,3,4))
if mibBuilder.loadTexts:h3cEponMauType1000BasePX10DONU.setStatus(_A)
_H3cEponMauType1000BasePX10UOLT_ObjectIdentity=ObjectIdentity
h3cEponMauType1000BasePX10UOLT=_H3cEponMauType1000BasePX10UOLT_ObjectIdentity((1,3,6,1,4,1,2011,10,2,42,2,3,3,5))
if mibBuilder.loadTexts:h3cEponMauType1000BasePX10UOLT.setStatus(_A)
_H3cEponMauType1000BasePX10UONU_ObjectIdentity=ObjectIdentity
h3cEponMauType1000BasePX10UONU=_H3cEponMauType1000BasePX10UONU_ObjectIdentity((1,3,6,1,4,1,2011,10,2,42,2,3,3,6))
if mibBuilder.loadTexts:h3cEponMauType1000BasePX10UONU.setStatus(_A)
_H3cEponMauType1000BasePX20DOLT_ObjectIdentity=ObjectIdentity
h3cEponMauType1000BasePX20DOLT=_H3cEponMauType1000BasePX20DOLT_ObjectIdentity((1,3,6,1,4,1,2011,10,2,42,2,3,3,7))
if mibBuilder.loadTexts:h3cEponMauType1000BasePX20DOLT.setStatus(_A)
_H3cEponMauType1000BasePX20DONU_ObjectIdentity=ObjectIdentity
h3cEponMauType1000BasePX20DONU=_H3cEponMauType1000BasePX20DONU_ObjectIdentity((1,3,6,1,4,1,2011,10,2,42,2,3,3,8))
if mibBuilder.loadTexts:h3cEponMauType1000BasePX20DONU.setStatus(_A)
_H3cEponMauType1000BasePX20UOLT_ObjectIdentity=ObjectIdentity
h3cEponMauType1000BasePX20UOLT=_H3cEponMauType1000BasePX20UOLT_ObjectIdentity((1,3,6,1,4,1,2011,10,2,42,2,3,3,9))
if mibBuilder.loadTexts:h3cEponMauType1000BasePX20UOLT.setStatus(_A)
_H3cEponMauType1000BasePX20UONU_ObjectIdentity=ObjectIdentity
h3cEponMauType1000BasePX20UONU=_H3cEponMauType1000BasePX20UONU_ObjectIdentity((1,3,6,1,4,1,2011,10,2,42,2,3,3,10))
if mibBuilder.loadTexts:h3cEponMauType1000BasePX20UONU.setStatus(_A)
h3cDot3MpcpGroupBase=ObjectGroup((1,3,6,1,4,1,2011,10,2,42,2,1,2,1,1))
h3cDot3MpcpGroupBase.setObjects(*((_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T)))
if mibBuilder.loadTexts:h3cDot3MpcpGroupBase.setStatus(_A)
h3cDot3MpcpGroupParam=ObjectGroup((1,3,6,1,4,1,2011,10,2,42,2,1,2,1,2))
h3cDot3MpcpGroupParam.setObjects(*((_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z)))
if mibBuilder.loadTexts:h3cDot3MpcpGroupParam.setStatus(_A)
h3cDot3MpcpGroupStat=ObjectGroup((1,3,6,1,4,1,2011,10,2,42,2,1,2,1,3))
h3cDot3MpcpGroupStat.setObjects(*((_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o)))
if mibBuilder.loadTexts:h3cDot3MpcpGroupStat.setStatus(_A)
h3cDot3OmpeGroupID=ObjectGroup((1,3,6,1,4,1,2011,10,2,42,2,2,2,1,1))
h3cDot3OmpeGroupID.setObjects(*((_B,_p),(_B,_q)))
if mibBuilder.loadTexts:h3cDot3OmpeGroupID.setStatus(_A)
h3cDot3OmpeGroupStat=ObjectGroup((1,3,6,1,4,1,2011,10,2,42,2,2,2,1,2))
h3cDot3OmpeGroupStat.setObjects(*((_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_x),(_B,_y),(_B,_z),(_B,_A0)))
if mibBuilder.loadTexts:h3cDot3OmpeGroupStat.setStatus(_A)
h3cDot3EponMauGroupAll=ObjectGroup((1,3,6,1,4,1,2011,10,2,42,2,3,2,1,1))
h3cDot3EponMauGroupAll.setObjects((_B,_A1))
if mibBuilder.loadTexts:h3cDot3EponMauGroupAll.setStatus(_A)
h3cDot3EponMauGroupFEC=ObjectGroup((1,3,6,1,4,1,2011,10,2,42,2,3,2,1,2))
h3cDot3EponMauGroupFEC.setObjects(*((_B,_A2),(_B,_A3),(_B,_A4),(_B,_A5),(_B,_A6)))
if mibBuilder.loadTexts:h3cDot3EponMauGroupFEC.setStatus(_A)
h3cDot3MpcpCompliance=ModuleCompliance((1,3,6,1,4,1,2011,10,2,42,2,1,2,2,1))
h3cDot3MpcpCompliance.setObjects(*((_B,_A7),(_B,_A8),(_B,_A9)))
if mibBuilder.loadTexts:h3cDot3MpcpCompliance.setStatus(_A)
h3cDot3OmpeCompliance=ModuleCompliance((1,3,6,1,4,1,2011,10,2,42,2,2,2,2,1))
h3cDot3OmpeCompliance.setObjects(*((_B,_AA),(_B,_AB)))
if mibBuilder.loadTexts:h3cDot3OmpeCompliance.setStatus(_A)
h3cDot3EponMauCompliance=ModuleCompliance((1,3,6,1,4,1,2011,10,2,42,2,3,2,2,1))
h3cDot3EponMauCompliance.setObjects(*((_B,_AC),(_B,_AD)))
if mibBuilder.loadTexts:h3cDot3EponMauCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'h3cDot3EfmeponMIB':h3cDot3EfmeponMIB,'h3cDot3MpcpMIB':h3cDot3MpcpMIB,'h3cDot3MpcpObjects':h3cDot3MpcpObjects,'h3cDot3MpcpTable':h3cDot3MpcpTable,'h3cDot3MpcpEntry':h3cDot3MpcpEntry,_M:h3cDot3MpcpID,_N:h3cDot3MpcpOperStatus,_O:h3cDot3MpcpMode,_P:h3cDot3MpcpLinkID,_Q:h3cDot3MpcpRemoteMACAddress,_R:h3cDot3MpcpRegistrationState,_U:h3cDot3MpcpTransmitElapsed,_V:h3cDot3MpcpReceiveElapsed,_W:h3cDot3MpcpRoundTripTime,_S:h3cDot3MpcpMaximumPendingGrants,_T:h3cDot3MpcpAdminState,_X:h3cDot3MpcpOnTime,_Y:h3cDot3MpcpOffTime,_Z:h3cDot3MpcpSyncTime,'h3cDot3MpcpStatTable':h3cDot3MpcpStatTable,'h3cDot3MpcpStatEntry':h3cDot3MpcpStatEntry,_a:h3cDot3MpcpMACCtrlFramesTransmitted,_b:h3cDot3MpcpMACCtrlFramesReceived,_c:h3cDot3MpcpDiscoveryWindowsSent,_d:h3cDot3MpcpDiscoveryTimeout,_e:h3cDot3MpcpTxRegRequest,_f:h3cDot3MpcpRxRegRequest,_g:h3cDot3MpcpTxRegAck,_h:h3cDot3MpcpRxRegAck,_i:h3cDot3MpcpTxReport,_j:h3cDot3MpcpRxReport,_k:h3cDot3MpcpTxGate,_l:h3cDot3MpcpRxGate,_m:h3cDot3MpcpTxRegister,_n:h3cDot3MpcpRxRegister,_o:h3cDot3MpcpRxNotSupportedMPCP,'h3cDot3MpcpConformance':h3cDot3MpcpConformance,'h3cDot3MpcpGroups':h3cDot3MpcpGroups,_A7:h3cDot3MpcpGroupBase,_A8:h3cDot3MpcpGroupParam,_A9:h3cDot3MpcpGroupStat,'h3cDot3MpcpCompliances':h3cDot3MpcpCompliances,'h3cDot3MpcpCompliance':h3cDot3MpcpCompliance,'h3cDot3OmpEmulationMIB':h3cDot3OmpEmulationMIB,'h3cDot3OmpEmulationObjects':h3cDot3OmpEmulationObjects,'h3cDot3OmpEmulationTable':h3cDot3OmpEmulationTable,'h3cDot3OmpEmulationEntry':h3cDot3OmpEmulationEntry,_p:h3cDot3OmpEmulationID,_q:h3cDot3OmpEmulationType,'h3cDot3OmpEmulationStatTable':h3cDot3OmpEmulationStatTable,'h3cDot3OmpEmulationStatEntry':h3cDot3OmpEmulationStatEntry,_r:h3cDot3OmpEmulationSLDErrors,_s:h3cDot3OmpEmulationCRC8Errors,_t:h3cDot3OmpEmulationBadLLID,_u:h3cDot3OmpEmulationGoodLLID,_v:h3cDot3OmpEmulationOnuPonCastLLID,_w:h3cDot3OmpEmulationOltPonCastLLID,_x:h3cDot3OmpEmulationBroadcastLLIDNotOnuID,_y:h3cDot3OmpEmulationOnuLLIDNotBroadcast,_z:h3cDot3OmpEmulationBroadcastLLIDPlusOnuId,_A0:h3cDot3OmpEmulationNotBroadcastLLIDNotOnuId,'h3cDot3OmpeConformance':h3cDot3OmpeConformance,'h3cDot3OmpeGroups':h3cDot3OmpeGroups,_AA:h3cDot3OmpeGroupID,_AB:h3cDot3OmpeGroupStat,'h3cDot3OmpeCompliances':h3cDot3OmpeCompliances,'h3cDot3OmpeCompliance':h3cDot3OmpeCompliance,'h3cDot3EponMauMIB':h3cDot3EponMauMIB,'h3cDot3EponMauObjects':h3cDot3EponMauObjects,'h3cDot3EponMauTable':h3cDot3EponMauTable,'h3cDot3EponMauEntry':h3cDot3EponMauEntry,_A1:h3cDot3EponMauPCSCodingViolation,_A2:h3cDot3EponMauFecAbility,_A3:h3cDot3EponMauFecMode,_A4:h3cDot3EponMauFECCorrectedBlocks,_A5:h3cDot3EponMauFECUncorrectableBlocks,_A6:h3cDot3EponMauBufferHeadCodingViolation,'h3cDot3EponMauConformance':h3cDot3EponMauConformance,'h3cDot3EponMauGroups':h3cDot3EponMauGroups,_AC:h3cDot3EponMauGroupAll,_AD:h3cDot3EponMauGroupFEC,'h3cDot3EponMauCompliances':h3cDot3EponMauCompliances,'h3cDot3EponMauCompliance':h3cDot3EponMauCompliance,'h3cDot3EponMauType':h3cDot3EponMauType,'h3cEponMauType1000BasePXOLT':h3cEponMauType1000BasePXOLT,'h3cEponMauType1000BasePXONU':h3cEponMauType1000BasePXONU,'h3cEponMauType1000BasePX10DOLT':h3cEponMauType1000BasePX10DOLT,'h3cEponMauType1000BasePX10DONU':h3cEponMauType1000BasePX10DONU,'h3cEponMauType1000BasePX10UOLT':h3cEponMauType1000BasePX10UOLT,'h3cEponMauType1000BasePX10UONU':h3cEponMauType1000BasePX10UONU,'h3cEponMauType1000BasePX20DOLT':h3cEponMauType1000BasePX20DOLT,'h3cEponMauType1000BasePX20DONU':h3cEponMauType1000BasePX20DONU,'h3cEponMauType1000BasePX20UOLT':h3cEponMauType1000BasePX20UOLT,'h3cEponMauType1000BasePX20UONU':h3cEponMauType1000BasePX20UONU})