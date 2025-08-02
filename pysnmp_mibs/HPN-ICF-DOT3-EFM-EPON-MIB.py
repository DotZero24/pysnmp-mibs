_AD='hpnicfDot3EponMauGroupFEC'
_AC='hpnicfDot3EponMauGroupAll'
_AB='hpnicfDot3OmpeGroupStat'
_AA='hpnicfDot3OmpeGroupID'
_A9='hpnicfDot3MpcpGroupStat'
_A8='hpnicfDot3MpcpGroupParam'
_A7='hpnicfDot3MpcpGroupBase'
_A6='hpnicfDot3EponMauBufferHeadCodingViolation'
_A5='hpnicfDot3EponMauFECUncorrectableBlocks'
_A4='hpnicfDot3EponMauFECCorrectedBlocks'
_A3='hpnicfDot3EponMauFecMode'
_A2='hpnicfDot3EponMauFecAbility'
_A1='hpnicfDot3EponMauPCSCodingViolation'
_A0='hpnicfDot3OmpEmulationNotBroadcastLLIDNotOnuId'
_z='hpnicfDot3OmpEmulationBroadcastLLIDPlusOnuId'
_y='hpnicfDot3OmpEmulationOnuLLIDNotBroadcast'
_x='hpnicfDot3OmpEmulationBroadcastLLIDNotOnuID'
_w='hpnicfDot3OmpEmulationOltPonCastLLID'
_v='hpnicfDot3OmpEmulationOnuPonCastLLID'
_u='hpnicfDot3OmpEmulationGoodLLID'
_t='hpnicfDot3OmpEmulationBadLLID'
_s='hpnicfDot3OmpEmulationCRC8Errors'
_r='hpnicfDot3OmpEmulationSLDErrors'
_q='hpnicfDot3OmpEmulationType'
_p='hpnicfDot3OmpEmulationID'
_o='hpnicfDot3MpcpRxNotSupportedMPCP'
_n='hpnicfDot3MpcpRxRegister'
_m='hpnicfDot3MpcpTxRegister'
_l='hpnicfDot3MpcpRxGate'
_k='hpnicfDot3MpcpTxGate'
_j='hpnicfDot3MpcpRxReport'
_i='hpnicfDot3MpcpTxReport'
_h='hpnicfDot3MpcpRxRegAck'
_g='hpnicfDot3MpcpTxRegAck'
_f='hpnicfDot3MpcpRxRegRequest'
_e='hpnicfDot3MpcpTxRegRequest'
_d='hpnicfDot3MpcpDiscoveryTimeout'
_c='hpnicfDot3MpcpDiscoveryWindowsSent'
_b='hpnicfDot3MpcpMACCtrlFramesReceived'
_a='hpnicfDot3MpcpMACCtrlFramesTransmitted'
_Z='hpnicfDot3MpcpSyncTime'
_Y='hpnicfDot3MpcpOffTime'
_X='hpnicfDot3MpcpOnTime'
_W='hpnicfDot3MpcpRoundTripTime'
_V='hpnicfDot3MpcpReceiveElapsed'
_U='hpnicfDot3MpcpTransmitElapsed'
_T='hpnicfDot3MpcpAdminState'
_S='hpnicfDot3MpcpMaximumPendingGrants'
_R='hpnicfDot3MpcpRegistrationState'
_Q='hpnicfDot3MpcpRemoteMACAddress'
_P='hpnicfDot3MpcpLinkID'
_O='hpnicfDot3MpcpMode'
_N='hpnicfDot3MpcpOperStatus'
_M='hpnicfDot3MpcpID'
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
_B='HPN-ICF-DOT3-EFM-EPON-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hpnicfEpon,=mibBuilder.importSymbols('HPN-ICF-OID-MIB','hpnicfEpon')
ifIndex,=mibBuilder.importSymbols(_F,_G)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso,mib_2=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso','mib-2')
DisplayString,MacAddress,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','TextualConvention',_K)
hpnicfDot3EfmeponMIB=ModuleIdentity((1,3,6,1,4,1,11,2,14,11,15,2,42,2))
if mibBuilder.loadTexts:hpnicfDot3EfmeponMIB.setRevisions(('2004-09-21 00:00',))
_HpnicfDot3MpcpMIB_ObjectIdentity=ObjectIdentity
hpnicfDot3MpcpMIB=_HpnicfDot3MpcpMIB_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,42,2,1))
_HpnicfDot3MpcpObjects_ObjectIdentity=ObjectIdentity
hpnicfDot3MpcpObjects=_HpnicfDot3MpcpObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,42,2,1,1))
_HpnicfDot3MpcpTable_Object=MibTable
hpnicfDot3MpcpTable=_HpnicfDot3MpcpTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,2,1,1,1))
if mibBuilder.loadTexts:hpnicfDot3MpcpTable.setStatus(_A)
_HpnicfDot3MpcpEntry_Object=MibTableRow
hpnicfDot3MpcpEntry=_HpnicfDot3MpcpEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,2,1,1,1,1))
hpnicfDot3MpcpEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:hpnicfDot3MpcpEntry.setStatus(_A)
_HpnicfDot3MpcpID_Type=Integer32
_HpnicfDot3MpcpID_Object=MibTableColumn
hpnicfDot3MpcpID=_HpnicfDot3MpcpID_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,2,1,1,1,1,1),_HpnicfDot3MpcpID_Type())
hpnicfDot3MpcpID.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot3MpcpID.setStatus(_A)
_HpnicfDot3MpcpOperStatus_Type=TruthValue
_HpnicfDot3MpcpOperStatus_Object=MibTableColumn
hpnicfDot3MpcpOperStatus=_HpnicfDot3MpcpOperStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,2,1,1,1,1,2),_HpnicfDot3MpcpOperStatus_Type())
hpnicfDot3MpcpOperStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot3MpcpOperStatus.setStatus(_A)
class _HpnicfDot3MpcpMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('olt',1),('onu',2)))
_HpnicfDot3MpcpMode_Type.__name__=_E
_HpnicfDot3MpcpMode_Object=MibTableColumn
hpnicfDot3MpcpMode=_HpnicfDot3MpcpMode_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,2,1,1,1,1,3),_HpnicfDot3MpcpMode_Type())
hpnicfDot3MpcpMode.setMaxAccess(_I)
if mibBuilder.loadTexts:hpnicfDot3MpcpMode.setStatus(_A)
_HpnicfDot3MpcpLinkID_Type=Integer32
_HpnicfDot3MpcpLinkID_Object=MibTableColumn
hpnicfDot3MpcpLinkID=_HpnicfDot3MpcpLinkID_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,2,1,1,1,1,4),_HpnicfDot3MpcpLinkID_Type())
hpnicfDot3MpcpLinkID.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot3MpcpLinkID.setStatus(_A)
_HpnicfDot3MpcpRemoteMACAddress_Type=MacAddress
_HpnicfDot3MpcpRemoteMACAddress_Object=MibTableColumn
hpnicfDot3MpcpRemoteMACAddress=_HpnicfDot3MpcpRemoteMACAddress_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,2,1,1,1,1,5),_HpnicfDot3MpcpRemoteMACAddress_Type())
hpnicfDot3MpcpRemoteMACAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot3MpcpRemoteMACAddress.setStatus(_A)
class _HpnicfDot3MpcpRegistrationState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('unregistered',1),('registering',2),('registered',3)))
_HpnicfDot3MpcpRegistrationState_Type.__name__=_E
_HpnicfDot3MpcpRegistrationState_Object=MibTableColumn
hpnicfDot3MpcpRegistrationState=_HpnicfDot3MpcpRegistrationState_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,2,1,1,1,1,6),_HpnicfDot3MpcpRegistrationState_Type())
hpnicfDot3MpcpRegistrationState.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot3MpcpRegistrationState.setStatus(_A)
_HpnicfDot3MpcpTransmitElapsed_Type=Integer32
_HpnicfDot3MpcpTransmitElapsed_Object=MibTableColumn
hpnicfDot3MpcpTransmitElapsed=_HpnicfDot3MpcpTransmitElapsed_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,2,1,1,1,1,7),_HpnicfDot3MpcpTransmitElapsed_Type())
hpnicfDot3MpcpTransmitElapsed.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot3MpcpTransmitElapsed.setStatus(_A)
if mibBuilder.loadTexts:hpnicfDot3MpcpTransmitElapsed.setUnits(_H)
_HpnicfDot3MpcpReceiveElapsed_Type=Integer32
_HpnicfDot3MpcpReceiveElapsed_Object=MibTableColumn
hpnicfDot3MpcpReceiveElapsed=_HpnicfDot3MpcpReceiveElapsed_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,2,1,1,1,1,8),_HpnicfDot3MpcpReceiveElapsed_Type())
hpnicfDot3MpcpReceiveElapsed.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot3MpcpReceiveElapsed.setStatus(_A)
if mibBuilder.loadTexts:hpnicfDot3MpcpReceiveElapsed.setUnits(_H)
_HpnicfDot3MpcpRoundTripTime_Type=Integer32
_HpnicfDot3MpcpRoundTripTime_Object=MibTableColumn
hpnicfDot3MpcpRoundTripTime=_HpnicfDot3MpcpRoundTripTime_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,2,1,1,1,1,9),_HpnicfDot3MpcpRoundTripTime_Type())
hpnicfDot3MpcpRoundTripTime.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot3MpcpRoundTripTime.setStatus(_A)
if mibBuilder.loadTexts:hpnicfDot3MpcpRoundTripTime.setUnits(_H)
class _HpnicfDot3MpcpMaximumPendingGrants_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_HpnicfDot3MpcpMaximumPendingGrants_Type.__name__=_E
_HpnicfDot3MpcpMaximumPendingGrants_Object=MibTableColumn
hpnicfDot3MpcpMaximumPendingGrants=_HpnicfDot3MpcpMaximumPendingGrants_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,2,1,1,1,1,10),_HpnicfDot3MpcpMaximumPendingGrants_Type())
hpnicfDot3MpcpMaximumPendingGrants.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot3MpcpMaximumPendingGrants.setStatus(_A)
class _HpnicfDot3MpcpAdminState_Type(TruthValue):defaultValue=2
_HpnicfDot3MpcpAdminState_Type.__name__=_K
_HpnicfDot3MpcpAdminState_Object=MibTableColumn
hpnicfDot3MpcpAdminState=_HpnicfDot3MpcpAdminState_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,2,1,1,1,1,11),_HpnicfDot3MpcpAdminState_Type())
hpnicfDot3MpcpAdminState.setMaxAccess(_I)
if mibBuilder.loadTexts:hpnicfDot3MpcpAdminState.setStatus(_A)
_HpnicfDot3MpcpOnTime_Type=Integer32
_HpnicfDot3MpcpOnTime_Object=MibTableColumn
hpnicfDot3MpcpOnTime=_HpnicfDot3MpcpOnTime_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,2,1,1,1,1,12),_HpnicfDot3MpcpOnTime_Type())
hpnicfDot3MpcpOnTime.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot3MpcpOnTime.setStatus(_A)
if mibBuilder.loadTexts:hpnicfDot3MpcpOnTime.setUnits(_H)
_HpnicfDot3MpcpOffTime_Type=Integer32
_HpnicfDot3MpcpOffTime_Object=MibTableColumn
hpnicfDot3MpcpOffTime=_HpnicfDot3MpcpOffTime_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,2,1,1,1,1,13),_HpnicfDot3MpcpOffTime_Type())
hpnicfDot3MpcpOffTime.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot3MpcpOffTime.setStatus(_A)
if mibBuilder.loadTexts:hpnicfDot3MpcpOffTime.setUnits(_H)
_HpnicfDot3MpcpSyncTime_Type=Integer32
_HpnicfDot3MpcpSyncTime_Object=MibTableColumn
hpnicfDot3MpcpSyncTime=_HpnicfDot3MpcpSyncTime_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,2,1,1,1,1,14),_HpnicfDot3MpcpSyncTime_Type())
hpnicfDot3MpcpSyncTime.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot3MpcpSyncTime.setStatus(_A)
if mibBuilder.loadTexts:hpnicfDot3MpcpSyncTime.setUnits(_H)
_HpnicfDot3MpcpStatTable_Object=MibTable
hpnicfDot3MpcpStatTable=_HpnicfDot3MpcpStatTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,2,1,1,2))
if mibBuilder.loadTexts:hpnicfDot3MpcpStatTable.setStatus(_A)
_HpnicfDot3MpcpStatEntry_Object=MibTableRow
hpnicfDot3MpcpStatEntry=_HpnicfDot3MpcpStatEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,2,1,1,2,1))
hpnicfDot3MpcpStatEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:hpnicfDot3MpcpStatEntry.setStatus(_A)
_HpnicfDot3MpcpMACCtrlFramesTransmitted_Type=Counter32
_HpnicfDot3MpcpMACCtrlFramesTransmitted_Object=MibTableColumn
hpnicfDot3MpcpMACCtrlFramesTransmitted=_HpnicfDot3MpcpMACCtrlFramesTransmitted_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,2,1,1,2,1,1),_HpnicfDot3MpcpMACCtrlFramesTransmitted_Type())
hpnicfDot3MpcpMACCtrlFramesTransmitted.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot3MpcpMACCtrlFramesTransmitted.setStatus(_A)
if mibBuilder.loadTexts:hpnicfDot3MpcpMACCtrlFramesTransmitted.setUnits(_D)
_HpnicfDot3MpcpMACCtrlFramesReceived_Type=Counter32
_HpnicfDot3MpcpMACCtrlFramesReceived_Object=MibTableColumn
hpnicfDot3MpcpMACCtrlFramesReceived=_HpnicfDot3MpcpMACCtrlFramesReceived_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,2,1,1,2,1,2),_HpnicfDot3MpcpMACCtrlFramesReceived_Type())
hpnicfDot3MpcpMACCtrlFramesReceived.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot3MpcpMACCtrlFramesReceived.setStatus(_A)
if mibBuilder.loadTexts:hpnicfDot3MpcpMACCtrlFramesReceived.setUnits(_D)
_HpnicfDot3MpcpDiscoveryWindowsSent_Type=Counter32
_HpnicfDot3MpcpDiscoveryWindowsSent_Object=MibTableColumn
hpnicfDot3MpcpDiscoveryWindowsSent=_HpnicfDot3MpcpDiscoveryWindowsSent_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,2,1,1,2,1,3),_HpnicfDot3MpcpDiscoveryWindowsSent_Type())
hpnicfDot3MpcpDiscoveryWindowsSent.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot3MpcpDiscoveryWindowsSent.setStatus(_A)
_HpnicfDot3MpcpDiscoveryTimeout_Type=Counter32
_HpnicfDot3MpcpDiscoveryTimeout_Object=MibTableColumn
hpnicfDot3MpcpDiscoveryTimeout=_HpnicfDot3MpcpDiscoveryTimeout_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,2,1,1,2,1,4),_HpnicfDot3MpcpDiscoveryTimeout_Type())
hpnicfDot3MpcpDiscoveryTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot3MpcpDiscoveryTimeout.setStatus(_A)
_HpnicfDot3MpcpTxRegRequest_Type=Counter32
_HpnicfDot3MpcpTxRegRequest_Object=MibTableColumn
hpnicfDot3MpcpTxRegRequest=_HpnicfDot3MpcpTxRegRequest_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,2,1,1,2,1,5),_HpnicfDot3MpcpTxRegRequest_Type())
hpnicfDot3MpcpTxRegRequest.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot3MpcpTxRegRequest.setStatus(_A)
if mibBuilder.loadTexts:hpnicfDot3MpcpTxRegRequest.setUnits(_D)
_HpnicfDot3MpcpRxRegRequest_Type=Counter32
_HpnicfDot3MpcpRxRegRequest_Object=MibTableColumn
hpnicfDot3MpcpRxRegRequest=_HpnicfDot3MpcpRxRegRequest_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,2,1,1,2,1,6),_HpnicfDot3MpcpRxRegRequest_Type())
hpnicfDot3MpcpRxRegRequest.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot3MpcpRxRegRequest.setStatus(_A)
if mibBuilder.loadTexts:hpnicfDot3MpcpRxRegRequest.setUnits(_D)
_HpnicfDot3MpcpTxRegAck_Type=Counter32
_HpnicfDot3MpcpTxRegAck_Object=MibTableColumn
hpnicfDot3MpcpTxRegAck=_HpnicfDot3MpcpTxRegAck_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,2,1,1,2,1,7),_HpnicfDot3MpcpTxRegAck_Type())
hpnicfDot3MpcpTxRegAck.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot3MpcpTxRegAck.setStatus(_A)
if mibBuilder.loadTexts:hpnicfDot3MpcpTxRegAck.setUnits(_D)
_HpnicfDot3MpcpRxRegAck_Type=Counter32
_HpnicfDot3MpcpRxRegAck_Object=MibTableColumn
hpnicfDot3MpcpRxRegAck=_HpnicfDot3MpcpRxRegAck_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,2,1,1,2,1,8),_HpnicfDot3MpcpRxRegAck_Type())
hpnicfDot3MpcpRxRegAck.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot3MpcpRxRegAck.setStatus(_A)
if mibBuilder.loadTexts:hpnicfDot3MpcpRxRegAck.setUnits(_D)
_HpnicfDot3MpcpTxReport_Type=Counter32
_HpnicfDot3MpcpTxReport_Object=MibTableColumn
hpnicfDot3MpcpTxReport=_HpnicfDot3MpcpTxReport_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,2,1,1,2,1,9),_HpnicfDot3MpcpTxReport_Type())
hpnicfDot3MpcpTxReport.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot3MpcpTxReport.setStatus(_A)
if mibBuilder.loadTexts:hpnicfDot3MpcpTxReport.setUnits(_D)
_HpnicfDot3MpcpRxReport_Type=Counter32
_HpnicfDot3MpcpRxReport_Object=MibTableColumn
hpnicfDot3MpcpRxReport=_HpnicfDot3MpcpRxReport_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,2,1,1,2,1,10),_HpnicfDot3MpcpRxReport_Type())
hpnicfDot3MpcpRxReport.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot3MpcpRxReport.setStatus(_A)
if mibBuilder.loadTexts:hpnicfDot3MpcpRxReport.setUnits(_D)
_HpnicfDot3MpcpTxGate_Type=Counter32
_HpnicfDot3MpcpTxGate_Object=MibTableColumn
hpnicfDot3MpcpTxGate=_HpnicfDot3MpcpTxGate_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,2,1,1,2,1,11),_HpnicfDot3MpcpTxGate_Type())
hpnicfDot3MpcpTxGate.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot3MpcpTxGate.setStatus(_A)
if mibBuilder.loadTexts:hpnicfDot3MpcpTxGate.setUnits(_D)
_HpnicfDot3MpcpRxGate_Type=Counter32
_HpnicfDot3MpcpRxGate_Object=MibTableColumn
hpnicfDot3MpcpRxGate=_HpnicfDot3MpcpRxGate_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,2,1,1,2,1,12),_HpnicfDot3MpcpRxGate_Type())
hpnicfDot3MpcpRxGate.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot3MpcpRxGate.setStatus(_A)
if mibBuilder.loadTexts:hpnicfDot3MpcpRxGate.setUnits(_D)
_HpnicfDot3MpcpTxRegister_Type=Counter32
_HpnicfDot3MpcpTxRegister_Object=MibTableColumn
hpnicfDot3MpcpTxRegister=_HpnicfDot3MpcpTxRegister_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,2,1,1,2,1,13),_HpnicfDot3MpcpTxRegister_Type())
hpnicfDot3MpcpTxRegister.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot3MpcpTxRegister.setStatus(_A)
if mibBuilder.loadTexts:hpnicfDot3MpcpTxRegister.setUnits(_D)
_HpnicfDot3MpcpRxRegister_Type=Counter32
_HpnicfDot3MpcpRxRegister_Object=MibTableColumn
hpnicfDot3MpcpRxRegister=_HpnicfDot3MpcpRxRegister_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,2,1,1,2,1,14),_HpnicfDot3MpcpRxRegister_Type())
hpnicfDot3MpcpRxRegister.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot3MpcpRxRegister.setStatus(_A)
if mibBuilder.loadTexts:hpnicfDot3MpcpRxRegister.setUnits(_D)
_HpnicfDot3MpcpRxNotSupportedMPCP_Type=Counter32
_HpnicfDot3MpcpRxNotSupportedMPCP_Object=MibTableColumn
hpnicfDot3MpcpRxNotSupportedMPCP=_HpnicfDot3MpcpRxNotSupportedMPCP_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,2,1,1,2,1,15),_HpnicfDot3MpcpRxNotSupportedMPCP_Type())
hpnicfDot3MpcpRxNotSupportedMPCP.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot3MpcpRxNotSupportedMPCP.setStatus(_A)
if mibBuilder.loadTexts:hpnicfDot3MpcpRxNotSupportedMPCP.setUnits(_D)
_HpnicfDot3MpcpConformance_ObjectIdentity=ObjectIdentity
hpnicfDot3MpcpConformance=_HpnicfDot3MpcpConformance_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,42,2,1,2))
_HpnicfDot3MpcpGroups_ObjectIdentity=ObjectIdentity
hpnicfDot3MpcpGroups=_HpnicfDot3MpcpGroups_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,42,2,1,2,1))
_HpnicfDot3MpcpCompliances_ObjectIdentity=ObjectIdentity
hpnicfDot3MpcpCompliances=_HpnicfDot3MpcpCompliances_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,42,2,1,2,2))
_HpnicfDot3OmpEmulationMIB_ObjectIdentity=ObjectIdentity
hpnicfDot3OmpEmulationMIB=_HpnicfDot3OmpEmulationMIB_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,42,2,2))
_HpnicfDot3OmpEmulationObjects_ObjectIdentity=ObjectIdentity
hpnicfDot3OmpEmulationObjects=_HpnicfDot3OmpEmulationObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,42,2,2,1))
_HpnicfDot3OmpEmulationTable_Object=MibTable
hpnicfDot3OmpEmulationTable=_HpnicfDot3OmpEmulationTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,2,2,1,1))
if mibBuilder.loadTexts:hpnicfDot3OmpEmulationTable.setStatus(_A)
_HpnicfDot3OmpEmulationEntry_Object=MibTableRow
hpnicfDot3OmpEmulationEntry=_HpnicfDot3OmpEmulationEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,2,2,1,1,1))
hpnicfDot3OmpEmulationEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:hpnicfDot3OmpEmulationEntry.setStatus(_A)
_HpnicfDot3OmpEmulationID_Type=Integer32
_HpnicfDot3OmpEmulationID_Object=MibTableColumn
hpnicfDot3OmpEmulationID=_HpnicfDot3OmpEmulationID_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,2,2,1,1,1,1),_HpnicfDot3OmpEmulationID_Type())
hpnicfDot3OmpEmulationID.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot3OmpEmulationID.setStatus(_A)
class _HpnicfDot3OmpEmulationType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_J,1),('olt',2),('onu',3)))
_HpnicfDot3OmpEmulationType_Type.__name__=_E
_HpnicfDot3OmpEmulationType_Object=MibTableColumn
hpnicfDot3OmpEmulationType=_HpnicfDot3OmpEmulationType_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,2,2,1,1,1,2),_HpnicfDot3OmpEmulationType_Type())
hpnicfDot3OmpEmulationType.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot3OmpEmulationType.setStatus(_A)
_HpnicfDot3OmpEmulationStatTable_Object=MibTable
hpnicfDot3OmpEmulationStatTable=_HpnicfDot3OmpEmulationStatTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,2,2,1,2))
if mibBuilder.loadTexts:hpnicfDot3OmpEmulationStatTable.setStatus(_A)
_HpnicfDot3OmpEmulationStatEntry_Object=MibTableRow
hpnicfDot3OmpEmulationStatEntry=_HpnicfDot3OmpEmulationStatEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,2,2,1,2,1))
hpnicfDot3OmpEmulationStatEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:hpnicfDot3OmpEmulationStatEntry.setStatus(_A)
_HpnicfDot3OmpEmulationSLDErrors_Type=Counter32
_HpnicfDot3OmpEmulationSLDErrors_Object=MibTableColumn
hpnicfDot3OmpEmulationSLDErrors=_HpnicfDot3OmpEmulationSLDErrors_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,2,2,1,2,1,1),_HpnicfDot3OmpEmulationSLDErrors_Type())
hpnicfDot3OmpEmulationSLDErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot3OmpEmulationSLDErrors.setStatus(_A)
if mibBuilder.loadTexts:hpnicfDot3OmpEmulationSLDErrors.setUnits(_D)
_HpnicfDot3OmpEmulationCRC8Errors_Type=Counter32
_HpnicfDot3OmpEmulationCRC8Errors_Object=MibTableColumn
hpnicfDot3OmpEmulationCRC8Errors=_HpnicfDot3OmpEmulationCRC8Errors_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,2,2,1,2,1,2),_HpnicfDot3OmpEmulationCRC8Errors_Type())
hpnicfDot3OmpEmulationCRC8Errors.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot3OmpEmulationCRC8Errors.setStatus(_A)
if mibBuilder.loadTexts:hpnicfDot3OmpEmulationCRC8Errors.setUnits(_D)
_HpnicfDot3OmpEmulationBadLLID_Type=Counter32
_HpnicfDot3OmpEmulationBadLLID_Object=MibTableColumn
hpnicfDot3OmpEmulationBadLLID=_HpnicfDot3OmpEmulationBadLLID_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,2,2,1,2,1,3),_HpnicfDot3OmpEmulationBadLLID_Type())
hpnicfDot3OmpEmulationBadLLID.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot3OmpEmulationBadLLID.setStatus(_A)
if mibBuilder.loadTexts:hpnicfDot3OmpEmulationBadLLID.setUnits(_D)
_HpnicfDot3OmpEmulationGoodLLID_Type=Counter32
_HpnicfDot3OmpEmulationGoodLLID_Object=MibTableColumn
hpnicfDot3OmpEmulationGoodLLID=_HpnicfDot3OmpEmulationGoodLLID_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,2,2,1,2,1,4),_HpnicfDot3OmpEmulationGoodLLID_Type())
hpnicfDot3OmpEmulationGoodLLID.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot3OmpEmulationGoodLLID.setStatus(_A)
if mibBuilder.loadTexts:hpnicfDot3OmpEmulationGoodLLID.setUnits(_D)
_HpnicfDot3OmpEmulationOnuPonCastLLID_Type=Counter32
_HpnicfDot3OmpEmulationOnuPonCastLLID_Object=MibTableColumn
hpnicfDot3OmpEmulationOnuPonCastLLID=_HpnicfDot3OmpEmulationOnuPonCastLLID_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,2,2,1,2,1,5),_HpnicfDot3OmpEmulationOnuPonCastLLID_Type())
hpnicfDot3OmpEmulationOnuPonCastLLID.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot3OmpEmulationOnuPonCastLLID.setStatus(_A)
if mibBuilder.loadTexts:hpnicfDot3OmpEmulationOnuPonCastLLID.setUnits(_D)
_HpnicfDot3OmpEmulationOltPonCastLLID_Type=Counter32
_HpnicfDot3OmpEmulationOltPonCastLLID_Object=MibTableColumn
hpnicfDot3OmpEmulationOltPonCastLLID=_HpnicfDot3OmpEmulationOltPonCastLLID_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,2,2,1,2,1,6),_HpnicfDot3OmpEmulationOltPonCastLLID_Type())
hpnicfDot3OmpEmulationOltPonCastLLID.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot3OmpEmulationOltPonCastLLID.setStatus(_A)
if mibBuilder.loadTexts:hpnicfDot3OmpEmulationOltPonCastLLID.setUnits(_D)
_HpnicfDot3OmpEmulationBroadcastLLIDNotOnuID_Type=Counter32
_HpnicfDot3OmpEmulationBroadcastLLIDNotOnuID_Object=MibTableColumn
hpnicfDot3OmpEmulationBroadcastLLIDNotOnuID=_HpnicfDot3OmpEmulationBroadcastLLIDNotOnuID_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,2,2,1,2,1,7),_HpnicfDot3OmpEmulationBroadcastLLIDNotOnuID_Type())
hpnicfDot3OmpEmulationBroadcastLLIDNotOnuID.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot3OmpEmulationBroadcastLLIDNotOnuID.setStatus(_A)
if mibBuilder.loadTexts:hpnicfDot3OmpEmulationBroadcastLLIDNotOnuID.setUnits(_D)
_HpnicfDot3OmpEmulationOnuLLIDNotBroadcast_Type=Counter32
_HpnicfDot3OmpEmulationOnuLLIDNotBroadcast_Object=MibTableColumn
hpnicfDot3OmpEmulationOnuLLIDNotBroadcast=_HpnicfDot3OmpEmulationOnuLLIDNotBroadcast_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,2,2,1,2,1,8),_HpnicfDot3OmpEmulationOnuLLIDNotBroadcast_Type())
hpnicfDot3OmpEmulationOnuLLIDNotBroadcast.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot3OmpEmulationOnuLLIDNotBroadcast.setStatus(_A)
if mibBuilder.loadTexts:hpnicfDot3OmpEmulationOnuLLIDNotBroadcast.setUnits(_D)
_HpnicfDot3OmpEmulationBroadcastLLIDPlusOnuId_Type=Counter32
_HpnicfDot3OmpEmulationBroadcastLLIDPlusOnuId_Object=MibTableColumn
hpnicfDot3OmpEmulationBroadcastLLIDPlusOnuId=_HpnicfDot3OmpEmulationBroadcastLLIDPlusOnuId_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,2,2,1,2,1,9),_HpnicfDot3OmpEmulationBroadcastLLIDPlusOnuId_Type())
hpnicfDot3OmpEmulationBroadcastLLIDPlusOnuId.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot3OmpEmulationBroadcastLLIDPlusOnuId.setStatus(_A)
if mibBuilder.loadTexts:hpnicfDot3OmpEmulationBroadcastLLIDPlusOnuId.setUnits(_D)
_HpnicfDot3OmpEmulationNotBroadcastLLIDNotOnuId_Type=Counter32
_HpnicfDot3OmpEmulationNotBroadcastLLIDNotOnuId_Object=MibTableColumn
hpnicfDot3OmpEmulationNotBroadcastLLIDNotOnuId=_HpnicfDot3OmpEmulationNotBroadcastLLIDNotOnuId_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,2,2,1,2,1,10),_HpnicfDot3OmpEmulationNotBroadcastLLIDNotOnuId_Type())
hpnicfDot3OmpEmulationNotBroadcastLLIDNotOnuId.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot3OmpEmulationNotBroadcastLLIDNotOnuId.setStatus(_A)
if mibBuilder.loadTexts:hpnicfDot3OmpEmulationNotBroadcastLLIDNotOnuId.setUnits(_D)
_HpnicfDot3OmpeConformance_ObjectIdentity=ObjectIdentity
hpnicfDot3OmpeConformance=_HpnicfDot3OmpeConformance_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,42,2,2,2))
_HpnicfDot3OmpeGroups_ObjectIdentity=ObjectIdentity
hpnicfDot3OmpeGroups=_HpnicfDot3OmpeGroups_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,42,2,2,2,1))
_HpnicfDot3OmpeCompliances_ObjectIdentity=ObjectIdentity
hpnicfDot3OmpeCompliances=_HpnicfDot3OmpeCompliances_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,42,2,2,2,2))
_HpnicfDot3EponMauMIB_ObjectIdentity=ObjectIdentity
hpnicfDot3EponMauMIB=_HpnicfDot3EponMauMIB_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,42,2,3))
_HpnicfDot3EponMauObjects_ObjectIdentity=ObjectIdentity
hpnicfDot3EponMauObjects=_HpnicfDot3EponMauObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,42,2,3,1))
_HpnicfDot3EponMauTable_Object=MibTable
hpnicfDot3EponMauTable=_HpnicfDot3EponMauTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,2,3,1,1))
if mibBuilder.loadTexts:hpnicfDot3EponMauTable.setStatus(_A)
_HpnicfDot3EponMauEntry_Object=MibTableRow
hpnicfDot3EponMauEntry=_HpnicfDot3EponMauEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,2,3,1,1,1))
hpnicfDot3EponMauEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:hpnicfDot3EponMauEntry.setStatus(_A)
_HpnicfDot3EponMauPCSCodingViolation_Type=Counter32
_HpnicfDot3EponMauPCSCodingViolation_Object=MibTableColumn
hpnicfDot3EponMauPCSCodingViolation=_HpnicfDot3EponMauPCSCodingViolation_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,2,3,1,1,1,1),_HpnicfDot3EponMauPCSCodingViolation_Type())
hpnicfDot3EponMauPCSCodingViolation.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot3EponMauPCSCodingViolation.setStatus(_A)
if mibBuilder.loadTexts:hpnicfDot3EponMauPCSCodingViolation.setUnits(_L)
class _HpnicfDot3EponMauFecAbility_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_J,1),('nonsupported',2),('supported',3)))
_HpnicfDot3EponMauFecAbility_Type.__name__=_E
_HpnicfDot3EponMauFecAbility_Object=MibTableColumn
hpnicfDot3EponMauFecAbility=_HpnicfDot3EponMauFecAbility_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,2,3,1,1,1,2),_HpnicfDot3EponMauFecAbility_Type())
hpnicfDot3EponMauFecAbility.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot3EponMauFecAbility.setStatus(_A)
class _HpnicfDot3EponMauFecMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_J,1),('disabled',2),('enabled',3)))
_HpnicfDot3EponMauFecMode_Type.__name__=_E
_HpnicfDot3EponMauFecMode_Object=MibTableColumn
hpnicfDot3EponMauFecMode=_HpnicfDot3EponMauFecMode_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,2,3,1,1,1,3),_HpnicfDot3EponMauFecMode_Type())
hpnicfDot3EponMauFecMode.setMaxAccess(_I)
if mibBuilder.loadTexts:hpnicfDot3EponMauFecMode.setStatus(_A)
_HpnicfDot3EponMauFECCorrectedBlocks_Type=Counter32
_HpnicfDot3EponMauFECCorrectedBlocks_Object=MibTableColumn
hpnicfDot3EponMauFECCorrectedBlocks=_HpnicfDot3EponMauFECCorrectedBlocks_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,2,3,1,1,1,4),_HpnicfDot3EponMauFECCorrectedBlocks_Type())
hpnicfDot3EponMauFECCorrectedBlocks.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot3EponMauFECCorrectedBlocks.setStatus(_A)
_HpnicfDot3EponMauFECUncorrectableBlocks_Type=Counter32
_HpnicfDot3EponMauFECUncorrectableBlocks_Object=MibTableColumn
hpnicfDot3EponMauFECUncorrectableBlocks=_HpnicfDot3EponMauFECUncorrectableBlocks_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,2,3,1,1,1,5),_HpnicfDot3EponMauFECUncorrectableBlocks_Type())
hpnicfDot3EponMauFECUncorrectableBlocks.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot3EponMauFECUncorrectableBlocks.setStatus(_A)
_HpnicfDot3EponMauBufferHeadCodingViolation_Type=Counter32
_HpnicfDot3EponMauBufferHeadCodingViolation_Object=MibTableColumn
hpnicfDot3EponMauBufferHeadCodingViolation=_HpnicfDot3EponMauBufferHeadCodingViolation_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,2,3,1,1,1,6),_HpnicfDot3EponMauBufferHeadCodingViolation_Type())
hpnicfDot3EponMauBufferHeadCodingViolation.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot3EponMauBufferHeadCodingViolation.setStatus(_A)
if mibBuilder.loadTexts:hpnicfDot3EponMauBufferHeadCodingViolation.setUnits(_L)
_HpnicfDot3EponMauConformance_ObjectIdentity=ObjectIdentity
hpnicfDot3EponMauConformance=_HpnicfDot3EponMauConformance_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,42,2,3,2))
_HpnicfDot3EponMauGroups_ObjectIdentity=ObjectIdentity
hpnicfDot3EponMauGroups=_HpnicfDot3EponMauGroups_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,42,2,3,2,1))
_HpnicfDot3EponMauCompliances_ObjectIdentity=ObjectIdentity
hpnicfDot3EponMauCompliances=_HpnicfDot3EponMauCompliances_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,42,2,3,2,2))
_HpnicfDot3EponMauType_ObjectIdentity=ObjectIdentity
hpnicfDot3EponMauType=_HpnicfDot3EponMauType_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,42,2,3,3))
_HpnicfEponMauType1000BasePXOLT_ObjectIdentity=ObjectIdentity
hpnicfEponMauType1000BasePXOLT=_HpnicfEponMauType1000BasePXOLT_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,42,2,3,3,1))
if mibBuilder.loadTexts:hpnicfEponMauType1000BasePXOLT.setStatus(_A)
_HpnicfEponMauType1000BasePXONU_ObjectIdentity=ObjectIdentity
hpnicfEponMauType1000BasePXONU=_HpnicfEponMauType1000BasePXONU_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,42,2,3,3,2))
if mibBuilder.loadTexts:hpnicfEponMauType1000BasePXONU.setStatus(_A)
_HpnicfEponMauType1000BasePX10DOLT_ObjectIdentity=ObjectIdentity
hpnicfEponMauType1000BasePX10DOLT=_HpnicfEponMauType1000BasePX10DOLT_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,42,2,3,3,3))
if mibBuilder.loadTexts:hpnicfEponMauType1000BasePX10DOLT.setStatus(_A)
_HpnicfEponMauType1000BasePX10DONU_ObjectIdentity=ObjectIdentity
hpnicfEponMauType1000BasePX10DONU=_HpnicfEponMauType1000BasePX10DONU_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,42,2,3,3,4))
if mibBuilder.loadTexts:hpnicfEponMauType1000BasePX10DONU.setStatus(_A)
_HpnicfEponMauType1000BasePX10UOLT_ObjectIdentity=ObjectIdentity
hpnicfEponMauType1000BasePX10UOLT=_HpnicfEponMauType1000BasePX10UOLT_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,42,2,3,3,5))
if mibBuilder.loadTexts:hpnicfEponMauType1000BasePX10UOLT.setStatus(_A)
_HpnicfEponMauType1000BasePX10UONU_ObjectIdentity=ObjectIdentity
hpnicfEponMauType1000BasePX10UONU=_HpnicfEponMauType1000BasePX10UONU_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,42,2,3,3,6))
if mibBuilder.loadTexts:hpnicfEponMauType1000BasePX10UONU.setStatus(_A)
_HpnicfEponMauType1000BasePX20DOLT_ObjectIdentity=ObjectIdentity
hpnicfEponMauType1000BasePX20DOLT=_HpnicfEponMauType1000BasePX20DOLT_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,42,2,3,3,7))
if mibBuilder.loadTexts:hpnicfEponMauType1000BasePX20DOLT.setStatus(_A)
_HpnicfEponMauType1000BasePX20DONU_ObjectIdentity=ObjectIdentity
hpnicfEponMauType1000BasePX20DONU=_HpnicfEponMauType1000BasePX20DONU_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,42,2,3,3,8))
if mibBuilder.loadTexts:hpnicfEponMauType1000BasePX20DONU.setStatus(_A)
_HpnicfEponMauType1000BasePX20UOLT_ObjectIdentity=ObjectIdentity
hpnicfEponMauType1000BasePX20UOLT=_HpnicfEponMauType1000BasePX20UOLT_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,42,2,3,3,9))
if mibBuilder.loadTexts:hpnicfEponMauType1000BasePX20UOLT.setStatus(_A)
_HpnicfEponMauType1000BasePX20UONU_ObjectIdentity=ObjectIdentity
hpnicfEponMauType1000BasePX20UONU=_HpnicfEponMauType1000BasePX20UONU_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,42,2,3,3,10))
if mibBuilder.loadTexts:hpnicfEponMauType1000BasePX20UONU.setStatus(_A)
hpnicfDot3MpcpGroupBase=ObjectGroup((1,3,6,1,4,1,11,2,14,11,15,2,42,2,1,2,1,1))
hpnicfDot3MpcpGroupBase.setObjects(*((_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T)))
if mibBuilder.loadTexts:hpnicfDot3MpcpGroupBase.setStatus(_A)
hpnicfDot3MpcpGroupParam=ObjectGroup((1,3,6,1,4,1,11,2,14,11,15,2,42,2,1,2,1,2))
hpnicfDot3MpcpGroupParam.setObjects(*((_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z)))
if mibBuilder.loadTexts:hpnicfDot3MpcpGroupParam.setStatus(_A)
hpnicfDot3MpcpGroupStat=ObjectGroup((1,3,6,1,4,1,11,2,14,11,15,2,42,2,1,2,1,3))
hpnicfDot3MpcpGroupStat.setObjects(*((_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o)))
if mibBuilder.loadTexts:hpnicfDot3MpcpGroupStat.setStatus(_A)
hpnicfDot3OmpeGroupID=ObjectGroup((1,3,6,1,4,1,11,2,14,11,15,2,42,2,2,2,1,1))
hpnicfDot3OmpeGroupID.setObjects(*((_B,_p),(_B,_q)))
if mibBuilder.loadTexts:hpnicfDot3OmpeGroupID.setStatus(_A)
hpnicfDot3OmpeGroupStat=ObjectGroup((1,3,6,1,4,1,11,2,14,11,15,2,42,2,2,2,1,2))
hpnicfDot3OmpeGroupStat.setObjects(*((_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_x),(_B,_y),(_B,_z),(_B,_A0)))
if mibBuilder.loadTexts:hpnicfDot3OmpeGroupStat.setStatus(_A)
hpnicfDot3EponMauGroupAll=ObjectGroup((1,3,6,1,4,1,11,2,14,11,15,2,42,2,3,2,1,1))
hpnicfDot3EponMauGroupAll.setObjects((_B,_A1))
if mibBuilder.loadTexts:hpnicfDot3EponMauGroupAll.setStatus(_A)
hpnicfDot3EponMauGroupFEC=ObjectGroup((1,3,6,1,4,1,11,2,14,11,15,2,42,2,3,2,1,2))
hpnicfDot3EponMauGroupFEC.setObjects(*((_B,_A2),(_B,_A3),(_B,_A4),(_B,_A5),(_B,_A6)))
if mibBuilder.loadTexts:hpnicfDot3EponMauGroupFEC.setStatus(_A)
hpnicfDot3MpcpCompliance=ModuleCompliance((1,3,6,1,4,1,11,2,14,11,15,2,42,2,1,2,2,1))
hpnicfDot3MpcpCompliance.setObjects(*((_B,_A7),(_B,_A8),(_B,_A9)))
if mibBuilder.loadTexts:hpnicfDot3MpcpCompliance.setStatus(_A)
hpnicfDot3OmpeCompliance=ModuleCompliance((1,3,6,1,4,1,11,2,14,11,15,2,42,2,2,2,2,1))
hpnicfDot3OmpeCompliance.setObjects(*((_B,_AA),(_B,_AB)))
if mibBuilder.loadTexts:hpnicfDot3OmpeCompliance.setStatus(_A)
hpnicfDot3EponMauCompliance=ModuleCompliance((1,3,6,1,4,1,11,2,14,11,15,2,42,2,3,2,2,1))
hpnicfDot3EponMauCompliance.setObjects(*((_B,_AC),(_B,_AD)))
if mibBuilder.loadTexts:hpnicfDot3EponMauCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'hpnicfDot3EfmeponMIB':hpnicfDot3EfmeponMIB,'hpnicfDot3MpcpMIB':hpnicfDot3MpcpMIB,'hpnicfDot3MpcpObjects':hpnicfDot3MpcpObjects,'hpnicfDot3MpcpTable':hpnicfDot3MpcpTable,'hpnicfDot3MpcpEntry':hpnicfDot3MpcpEntry,_M:hpnicfDot3MpcpID,_N:hpnicfDot3MpcpOperStatus,_O:hpnicfDot3MpcpMode,_P:hpnicfDot3MpcpLinkID,_Q:hpnicfDot3MpcpRemoteMACAddress,_R:hpnicfDot3MpcpRegistrationState,_U:hpnicfDot3MpcpTransmitElapsed,_V:hpnicfDot3MpcpReceiveElapsed,_W:hpnicfDot3MpcpRoundTripTime,_S:hpnicfDot3MpcpMaximumPendingGrants,_T:hpnicfDot3MpcpAdminState,_X:hpnicfDot3MpcpOnTime,_Y:hpnicfDot3MpcpOffTime,_Z:hpnicfDot3MpcpSyncTime,'hpnicfDot3MpcpStatTable':hpnicfDot3MpcpStatTable,'hpnicfDot3MpcpStatEntry':hpnicfDot3MpcpStatEntry,_a:hpnicfDot3MpcpMACCtrlFramesTransmitted,_b:hpnicfDot3MpcpMACCtrlFramesReceived,_c:hpnicfDot3MpcpDiscoveryWindowsSent,_d:hpnicfDot3MpcpDiscoveryTimeout,_e:hpnicfDot3MpcpTxRegRequest,_f:hpnicfDot3MpcpRxRegRequest,_g:hpnicfDot3MpcpTxRegAck,_h:hpnicfDot3MpcpRxRegAck,_i:hpnicfDot3MpcpTxReport,_j:hpnicfDot3MpcpRxReport,_k:hpnicfDot3MpcpTxGate,_l:hpnicfDot3MpcpRxGate,_m:hpnicfDot3MpcpTxRegister,_n:hpnicfDot3MpcpRxRegister,_o:hpnicfDot3MpcpRxNotSupportedMPCP,'hpnicfDot3MpcpConformance':hpnicfDot3MpcpConformance,'hpnicfDot3MpcpGroups':hpnicfDot3MpcpGroups,_A7:hpnicfDot3MpcpGroupBase,_A8:hpnicfDot3MpcpGroupParam,_A9:hpnicfDot3MpcpGroupStat,'hpnicfDot3MpcpCompliances':hpnicfDot3MpcpCompliances,'hpnicfDot3MpcpCompliance':hpnicfDot3MpcpCompliance,'hpnicfDot3OmpEmulationMIB':hpnicfDot3OmpEmulationMIB,'hpnicfDot3OmpEmulationObjects':hpnicfDot3OmpEmulationObjects,'hpnicfDot3OmpEmulationTable':hpnicfDot3OmpEmulationTable,'hpnicfDot3OmpEmulationEntry':hpnicfDot3OmpEmulationEntry,_p:hpnicfDot3OmpEmulationID,_q:hpnicfDot3OmpEmulationType,'hpnicfDot3OmpEmulationStatTable':hpnicfDot3OmpEmulationStatTable,'hpnicfDot3OmpEmulationStatEntry':hpnicfDot3OmpEmulationStatEntry,_r:hpnicfDot3OmpEmulationSLDErrors,_s:hpnicfDot3OmpEmulationCRC8Errors,_t:hpnicfDot3OmpEmulationBadLLID,_u:hpnicfDot3OmpEmulationGoodLLID,_v:hpnicfDot3OmpEmulationOnuPonCastLLID,_w:hpnicfDot3OmpEmulationOltPonCastLLID,_x:hpnicfDot3OmpEmulationBroadcastLLIDNotOnuID,_y:hpnicfDot3OmpEmulationOnuLLIDNotBroadcast,_z:hpnicfDot3OmpEmulationBroadcastLLIDPlusOnuId,_A0:hpnicfDot3OmpEmulationNotBroadcastLLIDNotOnuId,'hpnicfDot3OmpeConformance':hpnicfDot3OmpeConformance,'hpnicfDot3OmpeGroups':hpnicfDot3OmpeGroups,_AA:hpnicfDot3OmpeGroupID,_AB:hpnicfDot3OmpeGroupStat,'hpnicfDot3OmpeCompliances':hpnicfDot3OmpeCompliances,'hpnicfDot3OmpeCompliance':hpnicfDot3OmpeCompliance,'hpnicfDot3EponMauMIB':hpnicfDot3EponMauMIB,'hpnicfDot3EponMauObjects':hpnicfDot3EponMauObjects,'hpnicfDot3EponMauTable':hpnicfDot3EponMauTable,'hpnicfDot3EponMauEntry':hpnicfDot3EponMauEntry,_A1:hpnicfDot3EponMauPCSCodingViolation,_A2:hpnicfDot3EponMauFecAbility,_A3:hpnicfDot3EponMauFecMode,_A4:hpnicfDot3EponMauFECCorrectedBlocks,_A5:hpnicfDot3EponMauFECUncorrectableBlocks,_A6:hpnicfDot3EponMauBufferHeadCodingViolation,'hpnicfDot3EponMauConformance':hpnicfDot3EponMauConformance,'hpnicfDot3EponMauGroups':hpnicfDot3EponMauGroups,_AC:hpnicfDot3EponMauGroupAll,_AD:hpnicfDot3EponMauGroupFEC,'hpnicfDot3EponMauCompliances':hpnicfDot3EponMauCompliances,'hpnicfDot3EponMauCompliance':hpnicfDot3EponMauCompliance,'hpnicfDot3EponMauType':hpnicfDot3EponMauType,'hpnicfEponMauType1000BasePXOLT':hpnicfEponMauType1000BasePXOLT,'hpnicfEponMauType1000BasePXONU':hpnicfEponMauType1000BasePXONU,'hpnicfEponMauType1000BasePX10DOLT':hpnicfEponMauType1000BasePX10DOLT,'hpnicfEponMauType1000BasePX10DONU':hpnicfEponMauType1000BasePX10DONU,'hpnicfEponMauType1000BasePX10UOLT':hpnicfEponMauType1000BasePX10UOLT,'hpnicfEponMauType1000BasePX10UONU':hpnicfEponMauType1000BasePX10UONU,'hpnicfEponMauType1000BasePX20DOLT':hpnicfEponMauType1000BasePX20DOLT,'hpnicfEponMauType1000BasePX20DONU':hpnicfEponMauType1000BasePX20DONU,'hpnicfEponMauType1000BasePX20UOLT':hpnicfEponMauType1000BasePX20UOLT,'hpnicfEponMauType1000BasePX20UONU':hpnicfEponMauType1000BasePX20UONU})