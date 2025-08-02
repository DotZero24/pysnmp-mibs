_Ag='dot3ExtPkgGroupOptIf'
_Af='dot3ExtPkgGroupQueueSets'
_Ae='dot3ExtPkgGroupQueue'
_Ad='dot3ExtPkgGroupControl'
_Ac='dot3EponFecGroupAll'
_Ab='dot3OmpeGroupStat'
_Aa='dot3OmpeGroupID'
_AZ='dot3MpcpGroupStat'
_AY='dot3MpcpGroupBase'
_AX='dot3ExtPkgOptIfTransmitEnable'
_AW='dot3ExtPkgOptIfTransmitAlarm'
_AV='dot3ExtPkgOptIfSignalDetect'
_AU='dot3ExtPkgOptIfUpperOutputPowerThreshold'
_AT='dot3ExtPkgOptIfLowerOutputPowerThreshold'
_AS='dot3ExtPkgOptIfHighOutputPower'
_AR='dot3ExtPkgOptIfLowOutputPower'
_AQ='dot3ExtPkgOptIfOutputPower'
_AP='dot3ExtPkgOptIfUpperInputPowerThreshold'
_AO='dot3ExtPkgOptIfLowerInputPowerThreshold'
_AN='dot3ExtPkgOptIfHighInputPower'
_AM='dot3ExtPkgOptIfLowInputPower'
_AL='dot3ExtPkgOptIfInputPower'
_AK='dot3ExtPkgOptIfSuspectedFlag'
_AJ='dot3ExtPkgObjectReportThreshold'
_AI='dot3ExtPkgStatDroppedFramesQueue'
_AH='dot3ExtPkgStatRxFramesQueue'
_AG='dot3ExtPkgStatTxFramesQueue'
_AF='dot3ExtPkgObjectReportMaximumNumThreshold'
_AE='dot3ExtPkgObjectReportNumThreshold'
_AD='dot3ExtPkgObjectRegisterAction'
_AC='dot3ExtPkgObjectReportMaximumNumQueues'
_AB='dot3ExtPkgObjectFecEnabled'
_AA='dot3ExtPkgObjectNumberOfLLIDs'
_A9='dot3ExtPkgObjectPowerDown'
_A8='dot3ExtPkgObjectReset'
_A7='dot3EponFecBufferHeadCodingViolation'
_A6='dot3EponFecUncorrectableBlocks'
_A5='dot3EponFecCorrectedBlocks'
_A4='dot3EponFecMode'
_A3='dot3EponFecAbility'
_A2='dot3EponFecPCSCodingViolation'
_A1='dot3OmpEmulationNotBroadcastBitNotOnuLlid'
_A0='dot3OmpEmulationBroadcastBitPlusOnuLlid'
_z='dot3OmpEmulationOnuLLIDNotBroadcast'
_y='dot3OmpEmulationBroadcastBitNotOnuLlid'
_x='dot3OmpEmulationOltPonCastLLID'
_w='dot3OmpEmulationOnuPonCastLLID'
_v='dot3OmpEmulationGoodLLID'
_u='dot3OmpEmulationBadLLID'
_t='dot3OmpEmulationCRC8Errors'
_s='dot3OmpEmulationSLDErrors'
_r='dot3OmpEmulationType'
_q='dot3MpcpRxRegister'
_p='dot3MpcpTxRegister'
_o='dot3MpcpRxGate'
_n='dot3MpcpTxGate'
_m='dot3MpcpRxReport'
_l='dot3MpcpTxReport'
_k='dot3MpcpRxRegAck'
_j='dot3MpcpTxRegAck'
_i='dot3MpcpRxRegRequest'
_h='dot3MpcpTxRegRequest'
_g='dot3MpcpDiscoveryTimeout'
_f='dot3MpcpDiscoveryWindowsSent'
_e='dot3MpcpMACCtrlFramesReceived'
_d='dot3MpcpMACCtrlFramesTransmitted'
_c='dot3MpcpRoundTripTime'
_b='dot3MpcpReceiveElapsed'
_a='dot3MpcpTransmitElapsed'
_Z='dot3MpcpMaximumPendingGrants'
_Y='dot3MpcpRegistrationState'
_X='dot3MpcpRemoteMACAddress'
_W='dot3MpcpLinkID'
_V='dot3MpcpSyncTime'
_U='dot3MpcpMode'
_T='dot3MpcpAdminState'
_S='dot3MpcpOperStatus'
_R='dot3QueueSetIndex'
_Q='dot3QueueSetQueueIndex'
_P='dot3QueueIndex'
_O='octets'
_N='not-accessible'
_M='unknown'
_L='TQ (16nsec)'
_K='TruthValue'
_J='Integer32'
_I='0.1 dbm'
_H='Unsigned32'
_G='ifIndex'
_F='IF-MIB'
_E='read-write'
_D='frames'
_C='read-only'
_B='DOT3-EPON-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_F,_G)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso,mib_2=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_J,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_H,'iso','mib-2')
DisplayString,MacAddress,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','TextualConvention',_K)
dot3EponMIB=ModuleIdentity((1,3,6,1,2,1,155))
if mibBuilder.loadTexts:dot3EponMIB.setRevisions(('2007-03-29 00:00',))
_Dot3EponObjects_ObjectIdentity=ObjectIdentity
dot3EponObjects=_Dot3EponObjects_ObjectIdentity((1,3,6,1,2,1,155,1))
_Dot3EponMpcpObjects_ObjectIdentity=ObjectIdentity
dot3EponMpcpObjects=_Dot3EponMpcpObjects_ObjectIdentity((1,3,6,1,2,1,155,1,1))
_Dot3MpcpControlTable_Object=MibTable
dot3MpcpControlTable=_Dot3MpcpControlTable_Object((1,3,6,1,2,1,155,1,1,1))
if mibBuilder.loadTexts:dot3MpcpControlTable.setStatus(_A)
_Dot3MpcpControlEntry_Object=MibTableRow
dot3MpcpControlEntry=_Dot3MpcpControlEntry_Object((1,3,6,1,2,1,155,1,1,1,1))
dot3MpcpControlEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:dot3MpcpControlEntry.setStatus(_A)
_Dot3MpcpOperStatus_Type=TruthValue
_Dot3MpcpOperStatus_Object=MibTableColumn
dot3MpcpOperStatus=_Dot3MpcpOperStatus_Object((1,3,6,1,2,1,155,1,1,1,1,1),_Dot3MpcpOperStatus_Type())
dot3MpcpOperStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:dot3MpcpOperStatus.setStatus(_A)
class _Dot3MpcpAdminState_Type(TruthValue):defaultValue=2
_Dot3MpcpAdminState_Type.__name__=_K
_Dot3MpcpAdminState_Object=MibTableColumn
dot3MpcpAdminState=_Dot3MpcpAdminState_Object((1,3,6,1,2,1,155,1,1,1,1,2),_Dot3MpcpAdminState_Type())
dot3MpcpAdminState.setMaxAccess(_E)
if mibBuilder.loadTexts:dot3MpcpAdminState.setStatus(_A)
class _Dot3MpcpMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('olt',1),('onu',2)))
_Dot3MpcpMode_Type.__name__=_J
_Dot3MpcpMode_Object=MibTableColumn
dot3MpcpMode=_Dot3MpcpMode_Object((1,3,6,1,2,1,155,1,1,1,1,3),_Dot3MpcpMode_Type())
dot3MpcpMode.setMaxAccess(_C)
if mibBuilder.loadTexts:dot3MpcpMode.setStatus(_A)
_Dot3MpcpSyncTime_Type=Unsigned32
_Dot3MpcpSyncTime_Object=MibTableColumn
dot3MpcpSyncTime=_Dot3MpcpSyncTime_Object((1,3,6,1,2,1,155,1,1,1,1,4),_Dot3MpcpSyncTime_Type())
dot3MpcpSyncTime.setMaxAccess(_C)
if mibBuilder.loadTexts:dot3MpcpSyncTime.setStatus(_A)
if mibBuilder.loadTexts:dot3MpcpSyncTime.setUnits(_L)
_Dot3MpcpLinkID_Type=Unsigned32
_Dot3MpcpLinkID_Object=MibTableColumn
dot3MpcpLinkID=_Dot3MpcpLinkID_Object((1,3,6,1,2,1,155,1,1,1,1,5),_Dot3MpcpLinkID_Type())
dot3MpcpLinkID.setMaxAccess(_C)
if mibBuilder.loadTexts:dot3MpcpLinkID.setStatus(_A)
_Dot3MpcpRemoteMACAddress_Type=MacAddress
_Dot3MpcpRemoteMACAddress_Object=MibTableColumn
dot3MpcpRemoteMACAddress=_Dot3MpcpRemoteMACAddress_Object((1,3,6,1,2,1,155,1,1,1,1,6),_Dot3MpcpRemoteMACAddress_Type())
dot3MpcpRemoteMACAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:dot3MpcpRemoteMACAddress.setStatus(_A)
class _Dot3MpcpRegistrationState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('unregistered',1),('registering',2),('registered',3)))
_Dot3MpcpRegistrationState_Type.__name__=_J
_Dot3MpcpRegistrationState_Object=MibTableColumn
dot3MpcpRegistrationState=_Dot3MpcpRegistrationState_Object((1,3,6,1,2,1,155,1,1,1,1,7),_Dot3MpcpRegistrationState_Type())
dot3MpcpRegistrationState.setMaxAccess(_C)
if mibBuilder.loadTexts:dot3MpcpRegistrationState.setStatus(_A)
_Dot3MpcpTransmitElapsed_Type=Unsigned32
_Dot3MpcpTransmitElapsed_Object=MibTableColumn
dot3MpcpTransmitElapsed=_Dot3MpcpTransmitElapsed_Object((1,3,6,1,2,1,155,1,1,1,1,8),_Dot3MpcpTransmitElapsed_Type())
dot3MpcpTransmitElapsed.setMaxAccess(_C)
if mibBuilder.loadTexts:dot3MpcpTransmitElapsed.setStatus(_A)
if mibBuilder.loadTexts:dot3MpcpTransmitElapsed.setUnits(_L)
_Dot3MpcpReceiveElapsed_Type=Unsigned32
_Dot3MpcpReceiveElapsed_Object=MibTableColumn
dot3MpcpReceiveElapsed=_Dot3MpcpReceiveElapsed_Object((1,3,6,1,2,1,155,1,1,1,1,9),_Dot3MpcpReceiveElapsed_Type())
dot3MpcpReceiveElapsed.setMaxAccess(_C)
if mibBuilder.loadTexts:dot3MpcpReceiveElapsed.setStatus(_A)
if mibBuilder.loadTexts:dot3MpcpReceiveElapsed.setUnits(_L)
class _Dot3MpcpRoundTripTime_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Dot3MpcpRoundTripTime_Type.__name__=_H
_Dot3MpcpRoundTripTime_Object=MibTableColumn
dot3MpcpRoundTripTime=_Dot3MpcpRoundTripTime_Object((1,3,6,1,2,1,155,1,1,1,1,10),_Dot3MpcpRoundTripTime_Type())
dot3MpcpRoundTripTime.setMaxAccess(_C)
if mibBuilder.loadTexts:dot3MpcpRoundTripTime.setStatus(_A)
if mibBuilder.loadTexts:dot3MpcpRoundTripTime.setUnits(_L)
class _Dot3MpcpMaximumPendingGrants_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_Dot3MpcpMaximumPendingGrants_Type.__name__=_H
_Dot3MpcpMaximumPendingGrants_Object=MibTableColumn
dot3MpcpMaximumPendingGrants=_Dot3MpcpMaximumPendingGrants_Object((1,3,6,1,2,1,155,1,1,1,1,11),_Dot3MpcpMaximumPendingGrants_Type())
dot3MpcpMaximumPendingGrants.setMaxAccess(_C)
if mibBuilder.loadTexts:dot3MpcpMaximumPendingGrants.setStatus(_A)
_Dot3MpcpStatTable_Object=MibTable
dot3MpcpStatTable=_Dot3MpcpStatTable_Object((1,3,6,1,2,1,155,1,1,2))
if mibBuilder.loadTexts:dot3MpcpStatTable.setStatus(_A)
_Dot3MpcpStatEntry_Object=MibTableRow
dot3MpcpStatEntry=_Dot3MpcpStatEntry_Object((1,3,6,1,2,1,155,1,1,2,1))
dot3MpcpStatEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:dot3MpcpStatEntry.setStatus(_A)
_Dot3MpcpMACCtrlFramesTransmitted_Type=Counter64
_Dot3MpcpMACCtrlFramesTransmitted_Object=MibTableColumn
dot3MpcpMACCtrlFramesTransmitted=_Dot3MpcpMACCtrlFramesTransmitted_Object((1,3,6,1,2,1,155,1,1,2,1,1),_Dot3MpcpMACCtrlFramesTransmitted_Type())
dot3MpcpMACCtrlFramesTransmitted.setMaxAccess(_C)
if mibBuilder.loadTexts:dot3MpcpMACCtrlFramesTransmitted.setStatus(_A)
if mibBuilder.loadTexts:dot3MpcpMACCtrlFramesTransmitted.setUnits(_D)
_Dot3MpcpMACCtrlFramesReceived_Type=Counter64
_Dot3MpcpMACCtrlFramesReceived_Object=MibTableColumn
dot3MpcpMACCtrlFramesReceived=_Dot3MpcpMACCtrlFramesReceived_Object((1,3,6,1,2,1,155,1,1,2,1,2),_Dot3MpcpMACCtrlFramesReceived_Type())
dot3MpcpMACCtrlFramesReceived.setMaxAccess(_C)
if mibBuilder.loadTexts:dot3MpcpMACCtrlFramesReceived.setStatus(_A)
if mibBuilder.loadTexts:dot3MpcpMACCtrlFramesReceived.setUnits(_D)
_Dot3MpcpDiscoveryWindowsSent_Type=Counter32
_Dot3MpcpDiscoveryWindowsSent_Object=MibTableColumn
dot3MpcpDiscoveryWindowsSent=_Dot3MpcpDiscoveryWindowsSent_Object((1,3,6,1,2,1,155,1,1,2,1,3),_Dot3MpcpDiscoveryWindowsSent_Type())
dot3MpcpDiscoveryWindowsSent.setMaxAccess(_C)
if mibBuilder.loadTexts:dot3MpcpDiscoveryWindowsSent.setStatus(_A)
_Dot3MpcpDiscoveryTimeout_Type=Counter32
_Dot3MpcpDiscoveryTimeout_Object=MibTableColumn
dot3MpcpDiscoveryTimeout=_Dot3MpcpDiscoveryTimeout_Object((1,3,6,1,2,1,155,1,1,2,1,4),_Dot3MpcpDiscoveryTimeout_Type())
dot3MpcpDiscoveryTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:dot3MpcpDiscoveryTimeout.setStatus(_A)
_Dot3MpcpTxRegRequest_Type=Counter64
_Dot3MpcpTxRegRequest_Object=MibTableColumn
dot3MpcpTxRegRequest=_Dot3MpcpTxRegRequest_Object((1,3,6,1,2,1,155,1,1,2,1,5),_Dot3MpcpTxRegRequest_Type())
dot3MpcpTxRegRequest.setMaxAccess(_C)
if mibBuilder.loadTexts:dot3MpcpTxRegRequest.setStatus(_A)
if mibBuilder.loadTexts:dot3MpcpTxRegRequest.setUnits(_D)
_Dot3MpcpRxRegRequest_Type=Counter64
_Dot3MpcpRxRegRequest_Object=MibTableColumn
dot3MpcpRxRegRequest=_Dot3MpcpRxRegRequest_Object((1,3,6,1,2,1,155,1,1,2,1,6),_Dot3MpcpRxRegRequest_Type())
dot3MpcpRxRegRequest.setMaxAccess(_C)
if mibBuilder.loadTexts:dot3MpcpRxRegRequest.setStatus(_A)
if mibBuilder.loadTexts:dot3MpcpRxRegRequest.setUnits(_D)
_Dot3MpcpTxRegAck_Type=Counter64
_Dot3MpcpTxRegAck_Object=MibTableColumn
dot3MpcpTxRegAck=_Dot3MpcpTxRegAck_Object((1,3,6,1,2,1,155,1,1,2,1,7),_Dot3MpcpTxRegAck_Type())
dot3MpcpTxRegAck.setMaxAccess(_C)
if mibBuilder.loadTexts:dot3MpcpTxRegAck.setStatus(_A)
if mibBuilder.loadTexts:dot3MpcpTxRegAck.setUnits(_D)
_Dot3MpcpRxRegAck_Type=Counter64
_Dot3MpcpRxRegAck_Object=MibTableColumn
dot3MpcpRxRegAck=_Dot3MpcpRxRegAck_Object((1,3,6,1,2,1,155,1,1,2,1,8),_Dot3MpcpRxRegAck_Type())
dot3MpcpRxRegAck.setMaxAccess(_C)
if mibBuilder.loadTexts:dot3MpcpRxRegAck.setStatus(_A)
if mibBuilder.loadTexts:dot3MpcpRxRegAck.setUnits(_D)
_Dot3MpcpTxReport_Type=Counter64
_Dot3MpcpTxReport_Object=MibTableColumn
dot3MpcpTxReport=_Dot3MpcpTxReport_Object((1,3,6,1,2,1,155,1,1,2,1,9),_Dot3MpcpTxReport_Type())
dot3MpcpTxReport.setMaxAccess(_C)
if mibBuilder.loadTexts:dot3MpcpTxReport.setStatus(_A)
if mibBuilder.loadTexts:dot3MpcpTxReport.setUnits(_D)
_Dot3MpcpRxReport_Type=Counter64
_Dot3MpcpRxReport_Object=MibTableColumn
dot3MpcpRxReport=_Dot3MpcpRxReport_Object((1,3,6,1,2,1,155,1,1,2,1,10),_Dot3MpcpRxReport_Type())
dot3MpcpRxReport.setMaxAccess(_C)
if mibBuilder.loadTexts:dot3MpcpRxReport.setStatus(_A)
if mibBuilder.loadTexts:dot3MpcpRxReport.setUnits(_D)
_Dot3MpcpTxGate_Type=Counter64
_Dot3MpcpTxGate_Object=MibTableColumn
dot3MpcpTxGate=_Dot3MpcpTxGate_Object((1,3,6,1,2,1,155,1,1,2,1,11),_Dot3MpcpTxGate_Type())
dot3MpcpTxGate.setMaxAccess(_C)
if mibBuilder.loadTexts:dot3MpcpTxGate.setStatus(_A)
if mibBuilder.loadTexts:dot3MpcpTxGate.setUnits(_D)
_Dot3MpcpRxGate_Type=Counter64
_Dot3MpcpRxGate_Object=MibTableColumn
dot3MpcpRxGate=_Dot3MpcpRxGate_Object((1,3,6,1,2,1,155,1,1,2,1,12),_Dot3MpcpRxGate_Type())
dot3MpcpRxGate.setMaxAccess(_C)
if mibBuilder.loadTexts:dot3MpcpRxGate.setStatus(_A)
if mibBuilder.loadTexts:dot3MpcpRxGate.setUnits(_D)
_Dot3MpcpTxRegister_Type=Counter64
_Dot3MpcpTxRegister_Object=MibTableColumn
dot3MpcpTxRegister=_Dot3MpcpTxRegister_Object((1,3,6,1,2,1,155,1,1,2,1,13),_Dot3MpcpTxRegister_Type())
dot3MpcpTxRegister.setMaxAccess(_C)
if mibBuilder.loadTexts:dot3MpcpTxRegister.setStatus(_A)
if mibBuilder.loadTexts:dot3MpcpTxRegister.setUnits(_D)
_Dot3MpcpRxRegister_Type=Counter64
_Dot3MpcpRxRegister_Object=MibTableColumn
dot3MpcpRxRegister=_Dot3MpcpRxRegister_Object((1,3,6,1,2,1,155,1,1,2,1,14),_Dot3MpcpRxRegister_Type())
dot3MpcpRxRegister.setMaxAccess(_C)
if mibBuilder.loadTexts:dot3MpcpRxRegister.setStatus(_A)
if mibBuilder.loadTexts:dot3MpcpRxRegister.setUnits(_D)
_Dot3OmpEmulationObjects_ObjectIdentity=ObjectIdentity
dot3OmpEmulationObjects=_Dot3OmpEmulationObjects_ObjectIdentity((1,3,6,1,2,1,155,1,2))
_Dot3OmpEmulationTable_Object=MibTable
dot3OmpEmulationTable=_Dot3OmpEmulationTable_Object((1,3,6,1,2,1,155,1,2,1))
if mibBuilder.loadTexts:dot3OmpEmulationTable.setStatus(_A)
_Dot3OmpEmulationEntry_Object=MibTableRow
dot3OmpEmulationEntry=_Dot3OmpEmulationEntry_Object((1,3,6,1,2,1,155,1,2,1,1))
dot3OmpEmulationEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:dot3OmpEmulationEntry.setStatus(_A)
class _Dot3OmpEmulationType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_M,1),('olt',2),('onu',3)))
_Dot3OmpEmulationType_Type.__name__=_J
_Dot3OmpEmulationType_Object=MibTableColumn
dot3OmpEmulationType=_Dot3OmpEmulationType_Object((1,3,6,1,2,1,155,1,2,1,1,1),_Dot3OmpEmulationType_Type())
dot3OmpEmulationType.setMaxAccess(_C)
if mibBuilder.loadTexts:dot3OmpEmulationType.setStatus(_A)
_Dot3OmpEmulationStatTable_Object=MibTable
dot3OmpEmulationStatTable=_Dot3OmpEmulationStatTable_Object((1,3,6,1,2,1,155,1,2,2))
if mibBuilder.loadTexts:dot3OmpEmulationStatTable.setStatus(_A)
_Dot3OmpEmulationStatEntry_Object=MibTableRow
dot3OmpEmulationStatEntry=_Dot3OmpEmulationStatEntry_Object((1,3,6,1,2,1,155,1,2,2,1))
dot3OmpEmulationStatEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:dot3OmpEmulationStatEntry.setStatus(_A)
_Dot3OmpEmulationSLDErrors_Type=Counter64
_Dot3OmpEmulationSLDErrors_Object=MibTableColumn
dot3OmpEmulationSLDErrors=_Dot3OmpEmulationSLDErrors_Object((1,3,6,1,2,1,155,1,2,2,1,1),_Dot3OmpEmulationSLDErrors_Type())
dot3OmpEmulationSLDErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:dot3OmpEmulationSLDErrors.setStatus(_A)
if mibBuilder.loadTexts:dot3OmpEmulationSLDErrors.setUnits(_D)
_Dot3OmpEmulationCRC8Errors_Type=Counter64
_Dot3OmpEmulationCRC8Errors_Object=MibTableColumn
dot3OmpEmulationCRC8Errors=_Dot3OmpEmulationCRC8Errors_Object((1,3,6,1,2,1,155,1,2,2,1,2),_Dot3OmpEmulationCRC8Errors_Type())
dot3OmpEmulationCRC8Errors.setMaxAccess(_C)
if mibBuilder.loadTexts:dot3OmpEmulationCRC8Errors.setStatus(_A)
if mibBuilder.loadTexts:dot3OmpEmulationCRC8Errors.setUnits(_D)
_Dot3OmpEmulationBadLLID_Type=Counter64
_Dot3OmpEmulationBadLLID_Object=MibTableColumn
dot3OmpEmulationBadLLID=_Dot3OmpEmulationBadLLID_Object((1,3,6,1,2,1,155,1,2,2,1,3),_Dot3OmpEmulationBadLLID_Type())
dot3OmpEmulationBadLLID.setMaxAccess(_C)
if mibBuilder.loadTexts:dot3OmpEmulationBadLLID.setStatus(_A)
if mibBuilder.loadTexts:dot3OmpEmulationBadLLID.setUnits(_D)
_Dot3OmpEmulationGoodLLID_Type=Counter64
_Dot3OmpEmulationGoodLLID_Object=MibTableColumn
dot3OmpEmulationGoodLLID=_Dot3OmpEmulationGoodLLID_Object((1,3,6,1,2,1,155,1,2,2,1,4),_Dot3OmpEmulationGoodLLID_Type())
dot3OmpEmulationGoodLLID.setMaxAccess(_C)
if mibBuilder.loadTexts:dot3OmpEmulationGoodLLID.setStatus(_A)
if mibBuilder.loadTexts:dot3OmpEmulationGoodLLID.setUnits(_D)
_Dot3OmpEmulationOnuPonCastLLID_Type=Counter64
_Dot3OmpEmulationOnuPonCastLLID_Object=MibTableColumn
dot3OmpEmulationOnuPonCastLLID=_Dot3OmpEmulationOnuPonCastLLID_Object((1,3,6,1,2,1,155,1,2,2,1,5),_Dot3OmpEmulationOnuPonCastLLID_Type())
dot3OmpEmulationOnuPonCastLLID.setMaxAccess(_C)
if mibBuilder.loadTexts:dot3OmpEmulationOnuPonCastLLID.setStatus(_A)
if mibBuilder.loadTexts:dot3OmpEmulationOnuPonCastLLID.setUnits(_D)
_Dot3OmpEmulationOltPonCastLLID_Type=Counter64
_Dot3OmpEmulationOltPonCastLLID_Object=MibTableColumn
dot3OmpEmulationOltPonCastLLID=_Dot3OmpEmulationOltPonCastLLID_Object((1,3,6,1,2,1,155,1,2,2,1,6),_Dot3OmpEmulationOltPonCastLLID_Type())
dot3OmpEmulationOltPonCastLLID.setMaxAccess(_C)
if mibBuilder.loadTexts:dot3OmpEmulationOltPonCastLLID.setStatus(_A)
if mibBuilder.loadTexts:dot3OmpEmulationOltPonCastLLID.setUnits(_D)
_Dot3OmpEmulationBroadcastBitNotOnuLlid_Type=Counter64
_Dot3OmpEmulationBroadcastBitNotOnuLlid_Object=MibTableColumn
dot3OmpEmulationBroadcastBitNotOnuLlid=_Dot3OmpEmulationBroadcastBitNotOnuLlid_Object((1,3,6,1,2,1,155,1,2,2,1,7),_Dot3OmpEmulationBroadcastBitNotOnuLlid_Type())
dot3OmpEmulationBroadcastBitNotOnuLlid.setMaxAccess(_C)
if mibBuilder.loadTexts:dot3OmpEmulationBroadcastBitNotOnuLlid.setStatus(_A)
if mibBuilder.loadTexts:dot3OmpEmulationBroadcastBitNotOnuLlid.setUnits(_D)
_Dot3OmpEmulationOnuLLIDNotBroadcast_Type=Counter64
_Dot3OmpEmulationOnuLLIDNotBroadcast_Object=MibTableColumn
dot3OmpEmulationOnuLLIDNotBroadcast=_Dot3OmpEmulationOnuLLIDNotBroadcast_Object((1,3,6,1,2,1,155,1,2,2,1,8),_Dot3OmpEmulationOnuLLIDNotBroadcast_Type())
dot3OmpEmulationOnuLLIDNotBroadcast.setMaxAccess(_C)
if mibBuilder.loadTexts:dot3OmpEmulationOnuLLIDNotBroadcast.setStatus(_A)
if mibBuilder.loadTexts:dot3OmpEmulationOnuLLIDNotBroadcast.setUnits(_D)
_Dot3OmpEmulationBroadcastBitPlusOnuLlid_Type=Counter64
_Dot3OmpEmulationBroadcastBitPlusOnuLlid_Object=MibTableColumn
dot3OmpEmulationBroadcastBitPlusOnuLlid=_Dot3OmpEmulationBroadcastBitPlusOnuLlid_Object((1,3,6,1,2,1,155,1,2,2,1,9),_Dot3OmpEmulationBroadcastBitPlusOnuLlid_Type())
dot3OmpEmulationBroadcastBitPlusOnuLlid.setMaxAccess(_C)
if mibBuilder.loadTexts:dot3OmpEmulationBroadcastBitPlusOnuLlid.setStatus(_A)
if mibBuilder.loadTexts:dot3OmpEmulationBroadcastBitPlusOnuLlid.setUnits(_D)
_Dot3OmpEmulationNotBroadcastBitNotOnuLlid_Type=Counter64
_Dot3OmpEmulationNotBroadcastBitNotOnuLlid_Object=MibTableColumn
dot3OmpEmulationNotBroadcastBitNotOnuLlid=_Dot3OmpEmulationNotBroadcastBitNotOnuLlid_Object((1,3,6,1,2,1,155,1,2,2,1,10),_Dot3OmpEmulationNotBroadcastBitNotOnuLlid_Type())
dot3OmpEmulationNotBroadcastBitNotOnuLlid.setMaxAccess(_C)
if mibBuilder.loadTexts:dot3OmpEmulationNotBroadcastBitNotOnuLlid.setStatus(_A)
if mibBuilder.loadTexts:dot3OmpEmulationNotBroadcastBitNotOnuLlid.setUnits(_D)
_Dot3EponFecObjects_ObjectIdentity=ObjectIdentity
dot3EponFecObjects=_Dot3EponFecObjects_ObjectIdentity((1,3,6,1,2,1,155,1,3))
_Dot3EponFecTable_Object=MibTable
dot3EponFecTable=_Dot3EponFecTable_Object((1,3,6,1,2,1,155,1,3,1))
if mibBuilder.loadTexts:dot3EponFecTable.setStatus(_A)
_Dot3EponFecEntry_Object=MibTableRow
dot3EponFecEntry=_Dot3EponFecEntry_Object((1,3,6,1,2,1,155,1,3,1,1))
dot3EponFecEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:dot3EponFecEntry.setStatus(_A)
_Dot3EponFecPCSCodingViolation_Type=Counter64
_Dot3EponFecPCSCodingViolation_Object=MibTableColumn
dot3EponFecPCSCodingViolation=_Dot3EponFecPCSCodingViolation_Object((1,3,6,1,2,1,155,1,3,1,1,1),_Dot3EponFecPCSCodingViolation_Type())
dot3EponFecPCSCodingViolation.setMaxAccess(_C)
if mibBuilder.loadTexts:dot3EponFecPCSCodingViolation.setStatus(_A)
if mibBuilder.loadTexts:dot3EponFecPCSCodingViolation.setUnits(_O)
class _Dot3EponFecAbility_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_M,1),('supported',2),('unsupported',3)))
_Dot3EponFecAbility_Type.__name__=_J
_Dot3EponFecAbility_Object=MibTableColumn
dot3EponFecAbility=_Dot3EponFecAbility_Object((1,3,6,1,2,1,155,1,3,1,1,2),_Dot3EponFecAbility_Type())
dot3EponFecAbility.setMaxAccess(_C)
if mibBuilder.loadTexts:dot3EponFecAbility.setStatus(_A)
class _Dot3EponFecMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_M,1),('disabled',2),('enabled',3)))
_Dot3EponFecMode_Type.__name__=_J
_Dot3EponFecMode_Object=MibTableColumn
dot3EponFecMode=_Dot3EponFecMode_Object((1,3,6,1,2,1,155,1,3,1,1,3),_Dot3EponFecMode_Type())
dot3EponFecMode.setMaxAccess(_E)
if mibBuilder.loadTexts:dot3EponFecMode.setStatus(_A)
_Dot3EponFecCorrectedBlocks_Type=Counter64
_Dot3EponFecCorrectedBlocks_Object=MibTableColumn
dot3EponFecCorrectedBlocks=_Dot3EponFecCorrectedBlocks_Object((1,3,6,1,2,1,155,1,3,1,1,4),_Dot3EponFecCorrectedBlocks_Type())
dot3EponFecCorrectedBlocks.setMaxAccess(_C)
if mibBuilder.loadTexts:dot3EponFecCorrectedBlocks.setStatus(_A)
_Dot3EponFecUncorrectableBlocks_Type=Counter64
_Dot3EponFecUncorrectableBlocks_Object=MibTableColumn
dot3EponFecUncorrectableBlocks=_Dot3EponFecUncorrectableBlocks_Object((1,3,6,1,2,1,155,1,3,1,1,5),_Dot3EponFecUncorrectableBlocks_Type())
dot3EponFecUncorrectableBlocks.setMaxAccess(_C)
if mibBuilder.loadTexts:dot3EponFecUncorrectableBlocks.setStatus(_A)
_Dot3EponFecBufferHeadCodingViolation_Type=Counter64
_Dot3EponFecBufferHeadCodingViolation_Object=MibTableColumn
dot3EponFecBufferHeadCodingViolation=_Dot3EponFecBufferHeadCodingViolation_Object((1,3,6,1,2,1,155,1,3,1,1,6),_Dot3EponFecBufferHeadCodingViolation_Type())
dot3EponFecBufferHeadCodingViolation.setMaxAccess(_C)
if mibBuilder.loadTexts:dot3EponFecBufferHeadCodingViolation.setStatus(_A)
if mibBuilder.loadTexts:dot3EponFecBufferHeadCodingViolation.setUnits(_O)
_Dot3ExtPkgObjects_ObjectIdentity=ObjectIdentity
dot3ExtPkgObjects=_Dot3ExtPkgObjects_ObjectIdentity((1,3,6,1,2,1,155,1,4))
_Dot3ExtPkgControlObjects_ObjectIdentity=ObjectIdentity
dot3ExtPkgControlObjects=_Dot3ExtPkgControlObjects_ObjectIdentity((1,3,6,1,2,1,155,1,4,1))
_Dot3ExtPkgControlTable_Object=MibTable
dot3ExtPkgControlTable=_Dot3ExtPkgControlTable_Object((1,3,6,1,2,1,155,1,4,1,1))
if mibBuilder.loadTexts:dot3ExtPkgControlTable.setStatus(_A)
_Dot3ExtPkgControlEntry_Object=MibTableRow
dot3ExtPkgControlEntry=_Dot3ExtPkgControlEntry_Object((1,3,6,1,2,1,155,1,4,1,1,1))
dot3ExtPkgControlEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:dot3ExtPkgControlEntry.setStatus(_A)
class _Dot3ExtPkgObjectReset_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('running',1),('reset',2)))
_Dot3ExtPkgObjectReset_Type.__name__=_J
_Dot3ExtPkgObjectReset_Object=MibTableColumn
dot3ExtPkgObjectReset=_Dot3ExtPkgObjectReset_Object((1,3,6,1,2,1,155,1,4,1,1,1,1),_Dot3ExtPkgObjectReset_Type())
dot3ExtPkgObjectReset.setMaxAccess(_E)
if mibBuilder.loadTexts:dot3ExtPkgObjectReset.setStatus(_A)
class _Dot3ExtPkgObjectPowerDown_Type(TruthValue):defaultValue=2
_Dot3ExtPkgObjectPowerDown_Type.__name__=_K
_Dot3ExtPkgObjectPowerDown_Object=MibTableColumn
dot3ExtPkgObjectPowerDown=_Dot3ExtPkgObjectPowerDown_Object((1,3,6,1,2,1,155,1,4,1,1,1,2),_Dot3ExtPkgObjectPowerDown_Type())
dot3ExtPkgObjectPowerDown.setMaxAccess(_E)
if mibBuilder.loadTexts:dot3ExtPkgObjectPowerDown.setStatus(_A)
_Dot3ExtPkgObjectNumberOfLLIDs_Type=Unsigned32
_Dot3ExtPkgObjectNumberOfLLIDs_Object=MibTableColumn
dot3ExtPkgObjectNumberOfLLIDs=_Dot3ExtPkgObjectNumberOfLLIDs_Object((1,3,6,1,2,1,155,1,4,1,1,1,3),_Dot3ExtPkgObjectNumberOfLLIDs_Type())
dot3ExtPkgObjectNumberOfLLIDs.setMaxAccess(_C)
if mibBuilder.loadTexts:dot3ExtPkgObjectNumberOfLLIDs.setStatus(_A)
class _Dot3ExtPkgObjectFecEnabled_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('noFecEnabled',1),('fecTxEnabled',2),('fecRxEnabled',3),('fecTxRxEnabled',4)))
_Dot3ExtPkgObjectFecEnabled_Type.__name__=_J
_Dot3ExtPkgObjectFecEnabled_Object=MibTableColumn
dot3ExtPkgObjectFecEnabled=_Dot3ExtPkgObjectFecEnabled_Object((1,3,6,1,2,1,155,1,4,1,1,1,4),_Dot3ExtPkgObjectFecEnabled_Type())
dot3ExtPkgObjectFecEnabled.setMaxAccess(_E)
if mibBuilder.loadTexts:dot3ExtPkgObjectFecEnabled.setStatus(_A)
class _Dot3ExtPkgObjectReportMaximumNumQueues_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_Dot3ExtPkgObjectReportMaximumNumQueues_Type.__name__=_H
_Dot3ExtPkgObjectReportMaximumNumQueues_Object=MibTableColumn
dot3ExtPkgObjectReportMaximumNumQueues=_Dot3ExtPkgObjectReportMaximumNumQueues_Object((1,3,6,1,2,1,155,1,4,1,1,1,5),_Dot3ExtPkgObjectReportMaximumNumQueues_Type())
dot3ExtPkgObjectReportMaximumNumQueues.setMaxAccess(_C)
if mibBuilder.loadTexts:dot3ExtPkgObjectReportMaximumNumQueues.setStatus(_A)
class _Dot3ExtPkgObjectRegisterAction_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('none',1),('register',2),('deregister',3),('reregister',4)))
_Dot3ExtPkgObjectRegisterAction_Type.__name__=_J
_Dot3ExtPkgObjectRegisterAction_Object=MibTableColumn
dot3ExtPkgObjectRegisterAction=_Dot3ExtPkgObjectRegisterAction_Object((1,3,6,1,2,1,155,1,4,1,1,1,6),_Dot3ExtPkgObjectRegisterAction_Type())
dot3ExtPkgObjectRegisterAction.setMaxAccess(_E)
if mibBuilder.loadTexts:dot3ExtPkgObjectRegisterAction.setStatus(_A)
_Dot3ExtPkgQueueTable_Object=MibTable
dot3ExtPkgQueueTable=_Dot3ExtPkgQueueTable_Object((1,3,6,1,2,1,155,1,4,1,2))
if mibBuilder.loadTexts:dot3ExtPkgQueueTable.setStatus(_A)
_Dot3ExtPkgQueueEntry_Object=MibTableRow
dot3ExtPkgQueueEntry=_Dot3ExtPkgQueueEntry_Object((1,3,6,1,2,1,155,1,4,1,2,1))
dot3ExtPkgQueueEntry.setIndexNames((0,_F,_G),(0,_B,_P))
if mibBuilder.loadTexts:dot3ExtPkgQueueEntry.setStatus(_A)
class _Dot3QueueIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_Dot3QueueIndex_Type.__name__=_H
_Dot3QueueIndex_Object=MibTableColumn
dot3QueueIndex=_Dot3QueueIndex_Object((1,3,6,1,2,1,155,1,4,1,2,1,1),_Dot3QueueIndex_Type())
dot3QueueIndex.setMaxAccess(_N)
if mibBuilder.loadTexts:dot3QueueIndex.setStatus(_A)
class _Dot3ExtPkgObjectReportNumThreshold_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_Dot3ExtPkgObjectReportNumThreshold_Type.__name__=_H
_Dot3ExtPkgObjectReportNumThreshold_Object=MibTableColumn
dot3ExtPkgObjectReportNumThreshold=_Dot3ExtPkgObjectReportNumThreshold_Object((1,3,6,1,2,1,155,1,4,1,2,1,2),_Dot3ExtPkgObjectReportNumThreshold_Type())
dot3ExtPkgObjectReportNumThreshold.setMaxAccess(_E)
if mibBuilder.loadTexts:dot3ExtPkgObjectReportNumThreshold.setStatus(_A)
class _Dot3ExtPkgObjectReportMaximumNumThreshold_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_Dot3ExtPkgObjectReportMaximumNumThreshold_Type.__name__=_H
_Dot3ExtPkgObjectReportMaximumNumThreshold_Object=MibTableColumn
dot3ExtPkgObjectReportMaximumNumThreshold=_Dot3ExtPkgObjectReportMaximumNumThreshold_Object((1,3,6,1,2,1,155,1,4,1,2,1,3),_Dot3ExtPkgObjectReportMaximumNumThreshold_Type())
dot3ExtPkgObjectReportMaximumNumThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:dot3ExtPkgObjectReportMaximumNumThreshold.setStatus(_A)
_Dot3ExtPkgStatTxFramesQueue_Type=Counter64
_Dot3ExtPkgStatTxFramesQueue_Object=MibTableColumn
dot3ExtPkgStatTxFramesQueue=_Dot3ExtPkgStatTxFramesQueue_Object((1,3,6,1,2,1,155,1,4,1,2,1,4),_Dot3ExtPkgStatTxFramesQueue_Type())
dot3ExtPkgStatTxFramesQueue.setMaxAccess(_C)
if mibBuilder.loadTexts:dot3ExtPkgStatTxFramesQueue.setStatus(_A)
if mibBuilder.loadTexts:dot3ExtPkgStatTxFramesQueue.setUnits(_D)
_Dot3ExtPkgStatRxFramesQueue_Type=Counter64
_Dot3ExtPkgStatRxFramesQueue_Object=MibTableColumn
dot3ExtPkgStatRxFramesQueue=_Dot3ExtPkgStatRxFramesQueue_Object((1,3,6,1,2,1,155,1,4,1,2,1,5),_Dot3ExtPkgStatRxFramesQueue_Type())
dot3ExtPkgStatRxFramesQueue.setMaxAccess(_C)
if mibBuilder.loadTexts:dot3ExtPkgStatRxFramesQueue.setStatus(_A)
if mibBuilder.loadTexts:dot3ExtPkgStatRxFramesQueue.setUnits(_D)
_Dot3ExtPkgStatDroppedFramesQueue_Type=Counter64
_Dot3ExtPkgStatDroppedFramesQueue_Object=MibTableColumn
dot3ExtPkgStatDroppedFramesQueue=_Dot3ExtPkgStatDroppedFramesQueue_Object((1,3,6,1,2,1,155,1,4,1,2,1,6),_Dot3ExtPkgStatDroppedFramesQueue_Type())
dot3ExtPkgStatDroppedFramesQueue.setMaxAccess(_C)
if mibBuilder.loadTexts:dot3ExtPkgStatDroppedFramesQueue.setStatus(_A)
if mibBuilder.loadTexts:dot3ExtPkgStatDroppedFramesQueue.setUnits(_D)
_Dot3ExtPkgQueueSetsTable_Object=MibTable
dot3ExtPkgQueueSetsTable=_Dot3ExtPkgQueueSetsTable_Object((1,3,6,1,2,1,155,1,4,1,3))
if mibBuilder.loadTexts:dot3ExtPkgQueueSetsTable.setStatus(_A)
_Dot3ExtPkgQueueSetsEntry_Object=MibTableRow
dot3ExtPkgQueueSetsEntry=_Dot3ExtPkgQueueSetsEntry_Object((1,3,6,1,2,1,155,1,4,1,3,1))
dot3ExtPkgQueueSetsEntry.setIndexNames((0,_F,_G),(0,_B,_Q),(0,_B,_R))
if mibBuilder.loadTexts:dot3ExtPkgQueueSetsEntry.setStatus(_A)
class _Dot3QueueSetQueueIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_Dot3QueueSetQueueIndex_Type.__name__=_H
_Dot3QueueSetQueueIndex_Object=MibTableColumn
dot3QueueSetQueueIndex=_Dot3QueueSetQueueIndex_Object((1,3,6,1,2,1,155,1,4,1,3,1,1),_Dot3QueueSetQueueIndex_Type())
dot3QueueSetQueueIndex.setMaxAccess(_N)
if mibBuilder.loadTexts:dot3QueueSetQueueIndex.setStatus(_A)
class _Dot3QueueSetIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_Dot3QueueSetIndex_Type.__name__=_H
_Dot3QueueSetIndex_Object=MibTableColumn
dot3QueueSetIndex=_Dot3QueueSetIndex_Object((1,3,6,1,2,1,155,1,4,1,3,1,2),_Dot3QueueSetIndex_Type())
dot3QueueSetIndex.setMaxAccess(_N)
if mibBuilder.loadTexts:dot3QueueSetIndex.setStatus(_A)
class _Dot3ExtPkgObjectReportThreshold_Type(Unsigned32):defaultValue=0
_Dot3ExtPkgObjectReportThreshold_Type.__name__=_H
_Dot3ExtPkgObjectReportThreshold_Object=MibTableColumn
dot3ExtPkgObjectReportThreshold=_Dot3ExtPkgObjectReportThreshold_Object((1,3,6,1,2,1,155,1,4,1,3,1,3),_Dot3ExtPkgObjectReportThreshold_Type())
dot3ExtPkgObjectReportThreshold.setMaxAccess(_E)
if mibBuilder.loadTexts:dot3ExtPkgObjectReportThreshold.setStatus(_A)
if mibBuilder.loadTexts:dot3ExtPkgObjectReportThreshold.setUnits(_L)
_Dot3ExtPkgOptIfTable_Object=MibTable
dot3ExtPkgOptIfTable=_Dot3ExtPkgOptIfTable_Object((1,3,6,1,2,1,155,1,4,1,5))
if mibBuilder.loadTexts:dot3ExtPkgOptIfTable.setStatus(_A)
_Dot3ExtPkgOptIfEntry_Object=MibTableRow
dot3ExtPkgOptIfEntry=_Dot3ExtPkgOptIfEntry_Object((1,3,6,1,2,1,155,1,4,1,5,1))
dot3ExtPkgOptIfEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:dot3ExtPkgOptIfEntry.setStatus(_A)
_Dot3ExtPkgOptIfSuspectedFlag_Type=TruthValue
_Dot3ExtPkgOptIfSuspectedFlag_Object=MibTableColumn
dot3ExtPkgOptIfSuspectedFlag=_Dot3ExtPkgOptIfSuspectedFlag_Object((1,3,6,1,2,1,155,1,4,1,5,1,1),_Dot3ExtPkgOptIfSuspectedFlag_Type())
dot3ExtPkgOptIfSuspectedFlag.setMaxAccess(_C)
if mibBuilder.loadTexts:dot3ExtPkgOptIfSuspectedFlag.setStatus(_A)
_Dot3ExtPkgOptIfInputPower_Type=Integer32
_Dot3ExtPkgOptIfInputPower_Object=MibTableColumn
dot3ExtPkgOptIfInputPower=_Dot3ExtPkgOptIfInputPower_Object((1,3,6,1,2,1,155,1,4,1,5,1,2),_Dot3ExtPkgOptIfInputPower_Type())
dot3ExtPkgOptIfInputPower.setMaxAccess(_C)
if mibBuilder.loadTexts:dot3ExtPkgOptIfInputPower.setStatus(_A)
if mibBuilder.loadTexts:dot3ExtPkgOptIfInputPower.setUnits(_I)
_Dot3ExtPkgOptIfLowInputPower_Type=Integer32
_Dot3ExtPkgOptIfLowInputPower_Object=MibTableColumn
dot3ExtPkgOptIfLowInputPower=_Dot3ExtPkgOptIfLowInputPower_Object((1,3,6,1,2,1,155,1,4,1,5,1,3),_Dot3ExtPkgOptIfLowInputPower_Type())
dot3ExtPkgOptIfLowInputPower.setMaxAccess(_C)
if mibBuilder.loadTexts:dot3ExtPkgOptIfLowInputPower.setStatus(_A)
if mibBuilder.loadTexts:dot3ExtPkgOptIfLowInputPower.setUnits(_I)
_Dot3ExtPkgOptIfHighInputPower_Type=Integer32
_Dot3ExtPkgOptIfHighInputPower_Object=MibTableColumn
dot3ExtPkgOptIfHighInputPower=_Dot3ExtPkgOptIfHighInputPower_Object((1,3,6,1,2,1,155,1,4,1,5,1,4),_Dot3ExtPkgOptIfHighInputPower_Type())
dot3ExtPkgOptIfHighInputPower.setMaxAccess(_C)
if mibBuilder.loadTexts:dot3ExtPkgOptIfHighInputPower.setStatus(_A)
if mibBuilder.loadTexts:dot3ExtPkgOptIfHighInputPower.setUnits(_I)
_Dot3ExtPkgOptIfLowerInputPowerThreshold_Type=Integer32
_Dot3ExtPkgOptIfLowerInputPowerThreshold_Object=MibTableColumn
dot3ExtPkgOptIfLowerInputPowerThreshold=_Dot3ExtPkgOptIfLowerInputPowerThreshold_Object((1,3,6,1,2,1,155,1,4,1,5,1,5),_Dot3ExtPkgOptIfLowerInputPowerThreshold_Type())
dot3ExtPkgOptIfLowerInputPowerThreshold.setMaxAccess(_E)
if mibBuilder.loadTexts:dot3ExtPkgOptIfLowerInputPowerThreshold.setStatus(_A)
if mibBuilder.loadTexts:dot3ExtPkgOptIfLowerInputPowerThreshold.setUnits(_I)
_Dot3ExtPkgOptIfUpperInputPowerThreshold_Type=Integer32
_Dot3ExtPkgOptIfUpperInputPowerThreshold_Object=MibTableColumn
dot3ExtPkgOptIfUpperInputPowerThreshold=_Dot3ExtPkgOptIfUpperInputPowerThreshold_Object((1,3,6,1,2,1,155,1,4,1,5,1,6),_Dot3ExtPkgOptIfUpperInputPowerThreshold_Type())
dot3ExtPkgOptIfUpperInputPowerThreshold.setMaxAccess(_E)
if mibBuilder.loadTexts:dot3ExtPkgOptIfUpperInputPowerThreshold.setStatus(_A)
if mibBuilder.loadTexts:dot3ExtPkgOptIfUpperInputPowerThreshold.setUnits(_I)
_Dot3ExtPkgOptIfOutputPower_Type=Integer32
_Dot3ExtPkgOptIfOutputPower_Object=MibTableColumn
dot3ExtPkgOptIfOutputPower=_Dot3ExtPkgOptIfOutputPower_Object((1,3,6,1,2,1,155,1,4,1,5,1,7),_Dot3ExtPkgOptIfOutputPower_Type())
dot3ExtPkgOptIfOutputPower.setMaxAccess(_C)
if mibBuilder.loadTexts:dot3ExtPkgOptIfOutputPower.setStatus(_A)
if mibBuilder.loadTexts:dot3ExtPkgOptIfOutputPower.setUnits(_I)
_Dot3ExtPkgOptIfLowOutputPower_Type=Integer32
_Dot3ExtPkgOptIfLowOutputPower_Object=MibTableColumn
dot3ExtPkgOptIfLowOutputPower=_Dot3ExtPkgOptIfLowOutputPower_Object((1,3,6,1,2,1,155,1,4,1,5,1,8),_Dot3ExtPkgOptIfLowOutputPower_Type())
dot3ExtPkgOptIfLowOutputPower.setMaxAccess(_C)
if mibBuilder.loadTexts:dot3ExtPkgOptIfLowOutputPower.setStatus(_A)
if mibBuilder.loadTexts:dot3ExtPkgOptIfLowOutputPower.setUnits(_I)
_Dot3ExtPkgOptIfHighOutputPower_Type=Integer32
_Dot3ExtPkgOptIfHighOutputPower_Object=MibTableColumn
dot3ExtPkgOptIfHighOutputPower=_Dot3ExtPkgOptIfHighOutputPower_Object((1,3,6,1,2,1,155,1,4,1,5,1,9),_Dot3ExtPkgOptIfHighOutputPower_Type())
dot3ExtPkgOptIfHighOutputPower.setMaxAccess(_C)
if mibBuilder.loadTexts:dot3ExtPkgOptIfHighOutputPower.setStatus(_A)
if mibBuilder.loadTexts:dot3ExtPkgOptIfHighOutputPower.setUnits(_I)
_Dot3ExtPkgOptIfLowerOutputPowerThreshold_Type=Integer32
_Dot3ExtPkgOptIfLowerOutputPowerThreshold_Object=MibTableColumn
dot3ExtPkgOptIfLowerOutputPowerThreshold=_Dot3ExtPkgOptIfLowerOutputPowerThreshold_Object((1,3,6,1,2,1,155,1,4,1,5,1,10),_Dot3ExtPkgOptIfLowerOutputPowerThreshold_Type())
dot3ExtPkgOptIfLowerOutputPowerThreshold.setMaxAccess(_E)
if mibBuilder.loadTexts:dot3ExtPkgOptIfLowerOutputPowerThreshold.setStatus(_A)
if mibBuilder.loadTexts:dot3ExtPkgOptIfLowerOutputPowerThreshold.setUnits(_I)
_Dot3ExtPkgOptIfUpperOutputPowerThreshold_Type=Integer32
_Dot3ExtPkgOptIfUpperOutputPowerThreshold_Object=MibTableColumn
dot3ExtPkgOptIfUpperOutputPowerThreshold=_Dot3ExtPkgOptIfUpperOutputPowerThreshold_Object((1,3,6,1,2,1,155,1,4,1,5,1,11),_Dot3ExtPkgOptIfUpperOutputPowerThreshold_Type())
dot3ExtPkgOptIfUpperOutputPowerThreshold.setMaxAccess(_E)
if mibBuilder.loadTexts:dot3ExtPkgOptIfUpperOutputPowerThreshold.setStatus(_A)
if mibBuilder.loadTexts:dot3ExtPkgOptIfUpperOutputPowerThreshold.setUnits(_I)
class _Dot3ExtPkgOptIfSignalDetect_Type(TruthValue):defaultValue=2
_Dot3ExtPkgOptIfSignalDetect_Type.__name__=_K
_Dot3ExtPkgOptIfSignalDetect_Object=MibTableColumn
dot3ExtPkgOptIfSignalDetect=_Dot3ExtPkgOptIfSignalDetect_Object((1,3,6,1,2,1,155,1,4,1,5,1,12),_Dot3ExtPkgOptIfSignalDetect_Type())
dot3ExtPkgOptIfSignalDetect.setMaxAccess(_C)
if mibBuilder.loadTexts:dot3ExtPkgOptIfSignalDetect.setStatus(_A)
class _Dot3ExtPkgOptIfTransmitAlarm_Type(TruthValue):defaultValue=2
_Dot3ExtPkgOptIfTransmitAlarm_Type.__name__=_K
_Dot3ExtPkgOptIfTransmitAlarm_Object=MibTableColumn
dot3ExtPkgOptIfTransmitAlarm=_Dot3ExtPkgOptIfTransmitAlarm_Object((1,3,6,1,2,1,155,1,4,1,5,1,13),_Dot3ExtPkgOptIfTransmitAlarm_Type())
dot3ExtPkgOptIfTransmitAlarm.setMaxAccess(_C)
if mibBuilder.loadTexts:dot3ExtPkgOptIfTransmitAlarm.setStatus(_A)
class _Dot3ExtPkgOptIfTransmitEnable_Type(TruthValue):defaultValue=2
_Dot3ExtPkgOptIfTransmitEnable_Type.__name__=_K
_Dot3ExtPkgOptIfTransmitEnable_Object=MibTableColumn
dot3ExtPkgOptIfTransmitEnable=_Dot3ExtPkgOptIfTransmitEnable_Object((1,3,6,1,2,1,155,1,4,1,5,1,14),_Dot3ExtPkgOptIfTransmitEnable_Type())
dot3ExtPkgOptIfTransmitEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:dot3ExtPkgOptIfTransmitEnable.setStatus(_A)
_Dot3EponConformance_ObjectIdentity=ObjectIdentity
dot3EponConformance=_Dot3EponConformance_ObjectIdentity((1,3,6,1,2,1,155,2))
_Dot3EponGroups_ObjectIdentity=ObjectIdentity
dot3EponGroups=_Dot3EponGroups_ObjectIdentity((1,3,6,1,2,1,155,2,1))
_Dot3EponCompliances_ObjectIdentity=ObjectIdentity
dot3EponCompliances=_Dot3EponCompliances_ObjectIdentity((1,3,6,1,2,1,155,2,2))
dot3MpcpGroupBase=ObjectGroup((1,3,6,1,2,1,155,2,1,1))
dot3MpcpGroupBase.setObjects(*((_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c)))
if mibBuilder.loadTexts:dot3MpcpGroupBase.setStatus(_A)
dot3MpcpGroupStat=ObjectGroup((1,3,6,1,2,1,155,2,1,2))
dot3MpcpGroupStat.setObjects(*((_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q)))
if mibBuilder.loadTexts:dot3MpcpGroupStat.setStatus(_A)
dot3OmpeGroupID=ObjectGroup((1,3,6,1,2,1,155,2,1,3))
dot3OmpeGroupID.setObjects((_B,_r))
if mibBuilder.loadTexts:dot3OmpeGroupID.setStatus(_A)
dot3OmpeGroupStat=ObjectGroup((1,3,6,1,2,1,155,2,1,4))
dot3OmpeGroupStat.setObjects(*((_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_x),(_B,_y),(_B,_z),(_B,_A0),(_B,_A1)))
if mibBuilder.loadTexts:dot3OmpeGroupStat.setStatus(_A)
dot3EponFecGroupAll=ObjectGroup((1,3,6,1,2,1,155,2,1,5))
dot3EponFecGroupAll.setObjects(*((_B,_A2),(_B,_A3),(_B,_A4),(_B,_A5),(_B,_A6),(_B,_A7)))
if mibBuilder.loadTexts:dot3EponFecGroupAll.setStatus(_A)
dot3ExtPkgGroupControl=ObjectGroup((1,3,6,1,2,1,155,2,1,6))
dot3ExtPkgGroupControl.setObjects(*((_B,_A8),(_B,_A9),(_B,_AA),(_B,_AB),(_B,_AC),(_B,_AD)))
if mibBuilder.loadTexts:dot3ExtPkgGroupControl.setStatus(_A)
dot3ExtPkgGroupQueue=ObjectGroup((1,3,6,1,2,1,155,2,1,7))
dot3ExtPkgGroupQueue.setObjects(*((_B,_AE),(_B,_AF),(_B,_AG),(_B,_AH),(_B,_AI)))
if mibBuilder.loadTexts:dot3ExtPkgGroupQueue.setStatus(_A)
dot3ExtPkgGroupQueueSets=ObjectGroup((1,3,6,1,2,1,155,2,1,8))
dot3ExtPkgGroupQueueSets.setObjects((_B,_AJ))
if mibBuilder.loadTexts:dot3ExtPkgGroupQueueSets.setStatus(_A)
dot3ExtPkgGroupOptIf=ObjectGroup((1,3,6,1,2,1,155,2,1,9))
dot3ExtPkgGroupOptIf.setObjects(*((_B,_AK),(_B,_AL),(_B,_AM),(_B,_AN),(_B,_AO),(_B,_AP),(_B,_AQ),(_B,_AR),(_B,_AS),(_B,_AT),(_B,_AU),(_B,_AV),(_B,_AW),(_B,_AX)))
if mibBuilder.loadTexts:dot3ExtPkgGroupOptIf.setStatus(_A)
dot3MPCPCompliance=ModuleCompliance((1,3,6,1,2,1,155,2,2,1))
dot3MPCPCompliance.setObjects(*((_B,_AY),(_B,_AZ)))
if mibBuilder.loadTexts:dot3MPCPCompliance.setStatus(_A)
dot3OmpeCompliance=ModuleCompliance((1,3,6,1,2,1,155,2,2,2))
dot3OmpeCompliance.setObjects(*((_B,_Aa),(_B,_Ab)))
if mibBuilder.loadTexts:dot3OmpeCompliance.setStatus(_A)
dot3EponFecCompliance=ModuleCompliance((1,3,6,1,2,1,155,2,2,3))
dot3EponFecCompliance.setObjects((_B,_Ac))
if mibBuilder.loadTexts:dot3EponFecCompliance.setStatus(_A)
dot3ExtPkgCompliance=ModuleCompliance((1,3,6,1,2,1,155,2,2,4))
dot3ExtPkgCompliance.setObjects(*((_B,_Ad),(_B,_Ae),(_B,_Af),(_B,_Ag)))
if mibBuilder.loadTexts:dot3ExtPkgCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'dot3EponMIB':dot3EponMIB,'dot3EponObjects':dot3EponObjects,'dot3EponMpcpObjects':dot3EponMpcpObjects,'dot3MpcpControlTable':dot3MpcpControlTable,'dot3MpcpControlEntry':dot3MpcpControlEntry,_S:dot3MpcpOperStatus,_T:dot3MpcpAdminState,_U:dot3MpcpMode,_V:dot3MpcpSyncTime,_W:dot3MpcpLinkID,_X:dot3MpcpRemoteMACAddress,_Y:dot3MpcpRegistrationState,_a:dot3MpcpTransmitElapsed,_b:dot3MpcpReceiveElapsed,_c:dot3MpcpRoundTripTime,_Z:dot3MpcpMaximumPendingGrants,'dot3MpcpStatTable':dot3MpcpStatTable,'dot3MpcpStatEntry':dot3MpcpStatEntry,_d:dot3MpcpMACCtrlFramesTransmitted,_e:dot3MpcpMACCtrlFramesReceived,_f:dot3MpcpDiscoveryWindowsSent,_g:dot3MpcpDiscoveryTimeout,_h:dot3MpcpTxRegRequest,_i:dot3MpcpRxRegRequest,_j:dot3MpcpTxRegAck,_k:dot3MpcpRxRegAck,_l:dot3MpcpTxReport,_m:dot3MpcpRxReport,_n:dot3MpcpTxGate,_o:dot3MpcpRxGate,_p:dot3MpcpTxRegister,_q:dot3MpcpRxRegister,'dot3OmpEmulationObjects':dot3OmpEmulationObjects,'dot3OmpEmulationTable':dot3OmpEmulationTable,'dot3OmpEmulationEntry':dot3OmpEmulationEntry,_r:dot3OmpEmulationType,'dot3OmpEmulationStatTable':dot3OmpEmulationStatTable,'dot3OmpEmulationStatEntry':dot3OmpEmulationStatEntry,_s:dot3OmpEmulationSLDErrors,_t:dot3OmpEmulationCRC8Errors,_u:dot3OmpEmulationBadLLID,_v:dot3OmpEmulationGoodLLID,_w:dot3OmpEmulationOnuPonCastLLID,_x:dot3OmpEmulationOltPonCastLLID,_y:dot3OmpEmulationBroadcastBitNotOnuLlid,_z:dot3OmpEmulationOnuLLIDNotBroadcast,_A0:dot3OmpEmulationBroadcastBitPlusOnuLlid,_A1:dot3OmpEmulationNotBroadcastBitNotOnuLlid,'dot3EponFecObjects':dot3EponFecObjects,'dot3EponFecTable':dot3EponFecTable,'dot3EponFecEntry':dot3EponFecEntry,_A2:dot3EponFecPCSCodingViolation,_A3:dot3EponFecAbility,_A4:dot3EponFecMode,_A5:dot3EponFecCorrectedBlocks,_A6:dot3EponFecUncorrectableBlocks,_A7:dot3EponFecBufferHeadCodingViolation,'dot3ExtPkgObjects':dot3ExtPkgObjects,'dot3ExtPkgControlObjects':dot3ExtPkgControlObjects,'dot3ExtPkgControlTable':dot3ExtPkgControlTable,'dot3ExtPkgControlEntry':dot3ExtPkgControlEntry,_A8:dot3ExtPkgObjectReset,_A9:dot3ExtPkgObjectPowerDown,_AA:dot3ExtPkgObjectNumberOfLLIDs,_AB:dot3ExtPkgObjectFecEnabled,_AC:dot3ExtPkgObjectReportMaximumNumQueues,_AD:dot3ExtPkgObjectRegisterAction,'dot3ExtPkgQueueTable':dot3ExtPkgQueueTable,'dot3ExtPkgQueueEntry':dot3ExtPkgQueueEntry,_P:dot3QueueIndex,_AE:dot3ExtPkgObjectReportNumThreshold,_AF:dot3ExtPkgObjectReportMaximumNumThreshold,_AG:dot3ExtPkgStatTxFramesQueue,_AH:dot3ExtPkgStatRxFramesQueue,_AI:dot3ExtPkgStatDroppedFramesQueue,'dot3ExtPkgQueueSetsTable':dot3ExtPkgQueueSetsTable,'dot3ExtPkgQueueSetsEntry':dot3ExtPkgQueueSetsEntry,_Q:dot3QueueSetQueueIndex,_R:dot3QueueSetIndex,_AJ:dot3ExtPkgObjectReportThreshold,'dot3ExtPkgOptIfTable':dot3ExtPkgOptIfTable,'dot3ExtPkgOptIfEntry':dot3ExtPkgOptIfEntry,_AK:dot3ExtPkgOptIfSuspectedFlag,_AL:dot3ExtPkgOptIfInputPower,_AM:dot3ExtPkgOptIfLowInputPower,_AN:dot3ExtPkgOptIfHighInputPower,_AO:dot3ExtPkgOptIfLowerInputPowerThreshold,_AP:dot3ExtPkgOptIfUpperInputPowerThreshold,_AQ:dot3ExtPkgOptIfOutputPower,_AR:dot3ExtPkgOptIfLowOutputPower,_AS:dot3ExtPkgOptIfHighOutputPower,_AT:dot3ExtPkgOptIfLowerOutputPowerThreshold,_AU:dot3ExtPkgOptIfUpperOutputPowerThreshold,_AV:dot3ExtPkgOptIfSignalDetect,_AW:dot3ExtPkgOptIfTransmitAlarm,_AX:dot3ExtPkgOptIfTransmitEnable,'dot3EponConformance':dot3EponConformance,'dot3EponGroups':dot3EponGroups,_AY:dot3MpcpGroupBase,_AZ:dot3MpcpGroupStat,_Aa:dot3OmpeGroupID,_Ab:dot3OmpeGroupStat,_Ac:dot3EponFecGroupAll,_Ad:dot3ExtPkgGroupControl,_Ae:dot3ExtPkgGroupQueue,_Af:dot3ExtPkgGroupQueueSets,_Ag:dot3ExtPkgGroupOptIf,'dot3EponCompliances':dot3EponCompliances,'dot3MPCPCompliance':dot3MPCPCompliance,'dot3OmpeCompliance':dot3OmpeCompliance,'dot3EponFecCompliance':dot3EponFecCompliance,'dot3ExtPkgCompliance':dot3ExtPkgCompliance})