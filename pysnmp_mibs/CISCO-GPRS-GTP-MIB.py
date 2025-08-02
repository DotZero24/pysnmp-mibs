_AI='cgprsGtpGgsnStatusGroup'
_AH='cgprsGtpGgsnStatsGroup'
_AG='cgprsGtpGgsnConfigGroup'
_AF='cgprsGtpGeneralStatsGroup'
_AE='cgprsGtpGeneralConfigGroup'
_AD='cgprsGtpSecondaryChargingGWDownNotif'
_AC='cgprsGtpSecondaryChargingGWUpNotif'
_AB='cgprsGtpPrimaryChargingGWDownNotif'
_AA='cgprsGtpPrimaryChargingGWUpNotif'
_A9='cgprsGtpPDPCxtActivationRejNotif'
_A8='cgprsGtpGSNPathRecoveredNotif'
_A7='cgprsGtpGSNPathFailedNotif'
_A6='cgprsGtpNumAllocIpAddr'
_A5='cgprsGtpVersion'
_A4='cgprsGtpChargingMsgCnt'
_A3='cgprsGtpTotalNumAllocIpAddr'
_A2='cgprsGtpGSNEchoFailedNotifCnt'
_A1='cgprsGtpCurGSNBandwidthResrcUsed'
_A0='cgprsGtpCurMTForBestEffortQos'
_z='cgprsGtpCurMTForNormalQos'
_y='cgprsGtpCurMTForPremiumQos'
_x='cgprsGtpDroppedPktsCnt'
_w='cgprsGtpDroppedPktsTimeFrame'
_v='cgprsGtpTotalPktsDropped'
_u='cgprsGtpCurRejPDPCxtActivationCnt'
_t='cgprsGtpCurUnexpRxGpduCnt'
_s='cgprsGtpCurActivatedPDPCxtsCnt'
_r='cgprsGtpCurRxPacketQueueSize'
_q='cgprsGtpAPNRowStatus'
_p='cgprsGtpAPNAddrAllocMethod'
_o='cgprsGtpAPNName'
_n='cgprsGtpChargingGWRowStatus'
_m='cgprsGtpChargingGWNotifEnable'
_l='cgprsGtpChargingGWOperState'
_k='cgprsGtpChargingGWType'
_j='cgprsGtpChargingGWName'
_i='cgprsGtpAPNAddrAllocMethodGlobDef'
_h='cgprsGtpPDPCxtActRejNotifEnable'
_g='cgprsGtpNoRespToEchoNotifEnable'
_f='cgprsGtpDroppedPktsMonTime'
_e='cgprsGtpMaxNumPDPCxts'
_d='cgprsGtpGSNTotalBandwidthResrc'
_c='cgprsGtpEchoRequestTimer'
_b='cgprsGtpN3BufferSize'
_a='cgprsGtpN3Request'
_Z='cgprsGtpT3ResponseTimer'
_Y='cgprsGtpT3TunnelTimer'
_X='cgprsGtpGSNid'
_W='packets'
_V='cgprsGtpChargingGWid'
_U='notconfig'
_T='disable'
_S='radius'
_R='DisplayString'
_Q='cgprsGtpRejReasonOfLastUnexpPDPCxt'
_P='cgprsGtpTIDOfLastUnexpPDPCxt'
_O='cgprsGtpGSNidOfLastUnexpPDPCxt'
_N='cgprsGtpLastGSNidRecovered'
_M='cgprsGtpLastGSNidNoRespToEcho'
_L='cgprsGtpAPNId'
_K='not-accessible'
_J='PDP contexts'
_I='TruthValue'
_H='bits/sec'
_G='seconds'
_F='read-create'
_E='read-write'
_D='Integer32'
_C='read-only'
_B='CISCO-GPRS-GTP-MIB'
_A='obsolete'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoExperiment,=mibBuilder.importSymbols('CISCO-SMI','ciscoExperiment')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_R,'PhysAddress','RowStatus','TextualConvention',_I)
ciscoGprsGtpMIB=ModuleIdentity((1,3,6,1,4,1,9,10,48))
if mibBuilder.loadTexts:ciscoGprsGtpMIB.setRevisions(('2005-09-19 00:00','2001-07-30 00:00','2001-03-08 00:00','1999-07-12 00:00'))
_CiscoGprsGtpMIBObjects_ObjectIdentity=ObjectIdentity
ciscoGprsGtpMIBObjects=_CiscoGprsGtpMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,10,48,1))
_CiscoGprsGtpConfig_ObjectIdentity=ObjectIdentity
ciscoGprsGtpConfig=_CiscoGprsGtpConfig_ObjectIdentity((1,3,6,1,4,1,9,10,48,1,1))
_CgprsGtpGeneralConfig_ObjectIdentity=ObjectIdentity
cgprsGtpGeneralConfig=_CgprsGtpGeneralConfig_ObjectIdentity((1,3,6,1,4,1,9,10,48,1,1,1))
class _CgprsGtpT3TunnelTimer_Type(Integer32):defaultValue=20;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,180))
_CgprsGtpT3TunnelTimer_Type.__name__=_D
_CgprsGtpT3TunnelTimer_Object=MibScalar
cgprsGtpT3TunnelTimer=_CgprsGtpT3TunnelTimer_Object((1,3,6,1,4,1,9,10,48,1,1,1,1),_CgprsGtpT3TunnelTimer_Type())
cgprsGtpT3TunnelTimer.setMaxAccess(_E)
if mibBuilder.loadTexts:cgprsGtpT3TunnelTimer.setStatus(_A)
if mibBuilder.loadTexts:cgprsGtpT3TunnelTimer.setUnits(_G)
class _CgprsGtpT3ResponseTimer_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,60))
_CgprsGtpT3ResponseTimer_Type.__name__=_D
_CgprsGtpT3ResponseTimer_Object=MibScalar
cgprsGtpT3ResponseTimer=_CgprsGtpT3ResponseTimer_Object((1,3,6,1,4,1,9,10,48,1,1,1,2),_CgprsGtpT3ResponseTimer_Type())
cgprsGtpT3ResponseTimer.setMaxAccess(_E)
if mibBuilder.loadTexts:cgprsGtpT3ResponseTimer.setStatus(_A)
if mibBuilder.loadTexts:cgprsGtpT3ResponseTimer.setUnits(_G)
class _CgprsGtpN3Request_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,20))
_CgprsGtpN3Request_Type.__name__=_D
_CgprsGtpN3Request_Object=MibScalar
cgprsGtpN3Request=_CgprsGtpN3Request_Object((1,3,6,1,4,1,9,10,48,1,1,1,3),_CgprsGtpN3Request_Type())
cgprsGtpN3Request.setMaxAccess(_E)
if mibBuilder.loadTexts:cgprsGtpN3Request.setStatus(_A)
if mibBuilder.loadTexts:cgprsGtpN3Request.setUnits('messages')
class _CgprsGtpN3BufferSize_Type(Integer32):defaultValue=8192;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_CgprsGtpN3BufferSize_Type.__name__=_D
_CgprsGtpN3BufferSize_Object=MibScalar
cgprsGtpN3BufferSize=_CgprsGtpN3BufferSize_Object((1,3,6,1,4,1,9,10,48,1,1,1,4),_CgprsGtpN3BufferSize_Type())
cgprsGtpN3BufferSize.setMaxAccess(_E)
if mibBuilder.loadTexts:cgprsGtpN3BufferSize.setStatus(_A)
if mibBuilder.loadTexts:cgprsGtpN3BufferSize.setUnits('bytes')
class _CgprsGtpEchoRequestTimer_Type(Integer32):defaultValue=60;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(60,300))
_CgprsGtpEchoRequestTimer_Type.__name__=_D
_CgprsGtpEchoRequestTimer_Object=MibScalar
cgprsGtpEchoRequestTimer=_CgprsGtpEchoRequestTimer_Object((1,3,6,1,4,1,9,10,48,1,1,1,5),_CgprsGtpEchoRequestTimer_Type())
cgprsGtpEchoRequestTimer.setMaxAccess(_E)
if mibBuilder.loadTexts:cgprsGtpEchoRequestTimer.setStatus(_A)
if mibBuilder.loadTexts:cgprsGtpEchoRequestTimer.setUnits(_G)
class _CgprsGtpGSNTotalBandwidthResrc_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,3000))
_CgprsGtpGSNTotalBandwidthResrc_Type.__name__=_D
_CgprsGtpGSNTotalBandwidthResrc_Object=MibScalar
cgprsGtpGSNTotalBandwidthResrc=_CgprsGtpGSNTotalBandwidthResrc_Object((1,3,6,1,4,1,9,10,48,1,1,1,6),_CgprsGtpGSNTotalBandwidthResrc_Type())
cgprsGtpGSNTotalBandwidthResrc.setMaxAccess(_E)
if mibBuilder.loadTexts:cgprsGtpGSNTotalBandwidthResrc.setStatus(_A)
if mibBuilder.loadTexts:cgprsGtpGSNTotalBandwidthResrc.setUnits(_H)
class _CgprsGtpMaxNumPDPCxts_Type(Integer32):defaultValue=45000;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1000000))
_CgprsGtpMaxNumPDPCxts_Type.__name__=_D
_CgprsGtpMaxNumPDPCxts_Object=MibScalar
cgprsGtpMaxNumPDPCxts=_CgprsGtpMaxNumPDPCxts_Object((1,3,6,1,4,1,9,10,48,1,1,1,7),_CgprsGtpMaxNumPDPCxts_Type())
cgprsGtpMaxNumPDPCxts.setMaxAccess(_E)
if mibBuilder.loadTexts:cgprsGtpMaxNumPDPCxts.setStatus(_A)
if mibBuilder.loadTexts:cgprsGtpMaxNumPDPCxts.setUnits(_J)
class _CgprsGtpDroppedPktsMonTime_Type(Integer32):defaultValue=300;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CgprsGtpDroppedPktsMonTime_Type.__name__=_D
_CgprsGtpDroppedPktsMonTime_Object=MibScalar
cgprsGtpDroppedPktsMonTime=_CgprsGtpDroppedPktsMonTime_Object((1,3,6,1,4,1,9,10,48,1,1,1,8),_CgprsGtpDroppedPktsMonTime_Type())
cgprsGtpDroppedPktsMonTime.setMaxAccess(_E)
if mibBuilder.loadTexts:cgprsGtpDroppedPktsMonTime.setStatus(_A)
if mibBuilder.loadTexts:cgprsGtpDroppedPktsMonTime.setUnits(_G)
class _CgprsGtpNoRespToEchoNotifEnable_Type(TruthValue):defaultValue=1
_CgprsGtpNoRespToEchoNotifEnable_Type.__name__=_I
_CgprsGtpNoRespToEchoNotifEnable_Object=MibScalar
cgprsGtpNoRespToEchoNotifEnable=_CgprsGtpNoRespToEchoNotifEnable_Object((1,3,6,1,4,1,9,10,48,1,1,1,9),_CgprsGtpNoRespToEchoNotifEnable_Type())
cgprsGtpNoRespToEchoNotifEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:cgprsGtpNoRespToEchoNotifEnable.setStatus(_A)
class _CgprsGtpPDPCxtActRejNotifEnable_Type(TruthValue):defaultValue=1
_CgprsGtpPDPCxtActRejNotifEnable_Type.__name__=_I
_CgprsGtpPDPCxtActRejNotifEnable_Object=MibScalar
cgprsGtpPDPCxtActRejNotifEnable=_CgprsGtpPDPCxtActRejNotifEnable_Object((1,3,6,1,4,1,9,10,48,1,1,1,10),_CgprsGtpPDPCxtActRejNotifEnable_Type())
cgprsGtpPDPCxtActRejNotifEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:cgprsGtpPDPCxtActRejNotifEnable.setStatus(_A)
_CgprsGtpGgsnConfig_ObjectIdentity=ObjectIdentity
cgprsGtpGgsnConfig=_CgprsGtpGgsnConfig_ObjectIdentity((1,3,6,1,4,1,9,10,48,1,1,2))
class _CgprsGtpAPNAddrAllocMethodGlobDef_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_S,1),('dhcp',2),(_T,3),(_U,4)))
_CgprsGtpAPNAddrAllocMethodGlobDef_Type.__name__=_D
_CgprsGtpAPNAddrAllocMethodGlobDef_Object=MibScalar
cgprsGtpAPNAddrAllocMethodGlobDef=_CgprsGtpAPNAddrAllocMethodGlobDef_Object((1,3,6,1,4,1,9,10,48,1,1,2,1),_CgprsGtpAPNAddrAllocMethodGlobDef_Type())
cgprsGtpAPNAddrAllocMethodGlobDef.setMaxAccess(_E)
if mibBuilder.loadTexts:cgprsGtpAPNAddrAllocMethodGlobDef.setStatus(_A)
_CgprsGtpChargingGWTable_Object=MibTable
cgprsGtpChargingGWTable=_CgprsGtpChargingGWTable_Object((1,3,6,1,4,1,9,10,48,1,1,2,2))
if mibBuilder.loadTexts:cgprsGtpChargingGWTable.setStatus(_A)
_CgprsGtpChargingGWEntry_Object=MibTableRow
cgprsGtpChargingGWEntry=_CgprsGtpChargingGWEntry_Object((1,3,6,1,4,1,9,10,48,1,1,2,2,1))
cgprsGtpChargingGWEntry.setIndexNames((0,_B,_V))
if mibBuilder.loadTexts:cgprsGtpChargingGWEntry.setStatus(_A)
_CgprsGtpChargingGWid_Type=IpAddress
_CgprsGtpChargingGWid_Object=MibTableColumn
cgprsGtpChargingGWid=_CgprsGtpChargingGWid_Object((1,3,6,1,4,1,9,10,48,1,1,2,2,1,1),_CgprsGtpChargingGWid_Type())
cgprsGtpChargingGWid.setMaxAccess(_K)
if mibBuilder.loadTexts:cgprsGtpChargingGWid.setStatus(_A)
class _CgprsGtpChargingGWName_Type(DisplayString):defaultValue=OctetString('')
_CgprsGtpChargingGWName_Type.__name__=_R
_CgprsGtpChargingGWName_Object=MibTableColumn
cgprsGtpChargingGWName=_CgprsGtpChargingGWName_Object((1,3,6,1,4,1,9,10,48,1,1,2,2,1,2),_CgprsGtpChargingGWName_Type())
cgprsGtpChargingGWName.setMaxAccess(_F)
if mibBuilder.loadTexts:cgprsGtpChargingGWName.setStatus(_A)
class _CgprsGtpChargingGWType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('primary',1),('backup',2)))
_CgprsGtpChargingGWType_Type.__name__=_D
_CgprsGtpChargingGWType_Object=MibTableColumn
cgprsGtpChargingGWType=_CgprsGtpChargingGWType_Object((1,3,6,1,4,1,9,10,48,1,1,2,2,1,3),_CgprsGtpChargingGWType_Type())
cgprsGtpChargingGWType.setMaxAccess(_F)
if mibBuilder.loadTexts:cgprsGtpChargingGWType.setStatus(_A)
class _CgprsGtpChargingGWOperState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('up',1),('down',2),('unknown',3)))
_CgprsGtpChargingGWOperState_Type.__name__=_D
_CgprsGtpChargingGWOperState_Object=MibTableColumn
cgprsGtpChargingGWOperState=_CgprsGtpChargingGWOperState_Object((1,3,6,1,4,1,9,10,48,1,1,2,2,1,4),_CgprsGtpChargingGWOperState_Type())
cgprsGtpChargingGWOperState.setMaxAccess(_C)
if mibBuilder.loadTexts:cgprsGtpChargingGWOperState.setStatus(_A)
class _CgprsGtpChargingGWNotifEnable_Type(TruthValue):defaultValue=1
_CgprsGtpChargingGWNotifEnable_Type.__name__=_I
_CgprsGtpChargingGWNotifEnable_Object=MibTableColumn
cgprsGtpChargingGWNotifEnable=_CgprsGtpChargingGWNotifEnable_Object((1,3,6,1,4,1,9,10,48,1,1,2,2,1,5),_CgprsGtpChargingGWNotifEnable_Type())
cgprsGtpChargingGWNotifEnable.setMaxAccess(_F)
if mibBuilder.loadTexts:cgprsGtpChargingGWNotifEnable.setStatus(_A)
_CgprsGtpChargingGWRowStatus_Type=RowStatus
_CgprsGtpChargingGWRowStatus_Object=MibTableColumn
cgprsGtpChargingGWRowStatus=_CgprsGtpChargingGWRowStatus_Object((1,3,6,1,4,1,9,10,48,1,1,2,2,1,6),_CgprsGtpChargingGWRowStatus_Type())
cgprsGtpChargingGWRowStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:cgprsGtpChargingGWRowStatus.setStatus(_A)
_CgprsGtpAPNTable_Object=MibTable
cgprsGtpAPNTable=_CgprsGtpAPNTable_Object((1,3,6,1,4,1,9,10,48,1,1,2,3))
if mibBuilder.loadTexts:cgprsGtpAPNTable.setStatus(_A)
_CgprsGtpAPNEntry_Object=MibTableRow
cgprsGtpAPNEntry=_CgprsGtpAPNEntry_Object((1,3,6,1,4,1,9,10,48,1,1,2,3,1))
cgprsGtpAPNEntry.setIndexNames((0,_B,_L))
if mibBuilder.loadTexts:cgprsGtpAPNEntry.setStatus(_A)
class _CgprsGtpAPNId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CgprsGtpAPNId_Type.__name__=_D
_CgprsGtpAPNId_Object=MibTableColumn
cgprsGtpAPNId=_CgprsGtpAPNId_Object((1,3,6,1,4,1,9,10,48,1,1,2,3,1,1),_CgprsGtpAPNId_Type())
cgprsGtpAPNId.setMaxAccess(_K)
if mibBuilder.loadTexts:cgprsGtpAPNId.setStatus(_A)
_CgprsGtpAPNName_Type=DisplayString
_CgprsGtpAPNName_Object=MibTableColumn
cgprsGtpAPNName=_CgprsGtpAPNName_Object((1,3,6,1,4,1,9,10,48,1,1,2,3,1,2),_CgprsGtpAPNName_Type())
cgprsGtpAPNName.setMaxAccess(_F)
if mibBuilder.loadTexts:cgprsGtpAPNName.setStatus(_A)
class _CgprsGtpAPNAddrAllocMethod_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_S,1),('dhcp',2),(_T,3),(_U,4)))
_CgprsGtpAPNAddrAllocMethod_Type.__name__=_D
_CgprsGtpAPNAddrAllocMethod_Object=MibTableColumn
cgprsGtpAPNAddrAllocMethod=_CgprsGtpAPNAddrAllocMethod_Object((1,3,6,1,4,1,9,10,48,1,1,2,3,1,3),_CgprsGtpAPNAddrAllocMethod_Type())
cgprsGtpAPNAddrAllocMethod.setMaxAccess(_F)
if mibBuilder.loadTexts:cgprsGtpAPNAddrAllocMethod.setStatus(_A)
_CgprsGtpAPNRowStatus_Type=RowStatus
_CgprsGtpAPNRowStatus_Object=MibTableColumn
cgprsGtpAPNRowStatus=_CgprsGtpAPNRowStatus_Object((1,3,6,1,4,1,9,10,48,1,1,2,3,1,4),_CgprsGtpAPNRowStatus_Type())
cgprsGtpAPNRowStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:cgprsGtpAPNRowStatus.setStatus(_A)
_CiscoGprsGtpStats_ObjectIdentity=ObjectIdentity
ciscoGprsGtpStats=_CiscoGprsGtpStats_ObjectIdentity((1,3,6,1,4,1,9,10,48,1,2))
_CgprsGtpGeneralStats_ObjectIdentity=ObjectIdentity
cgprsGtpGeneralStats=_CgprsGtpGeneralStats_ObjectIdentity((1,3,6,1,4,1,9,10,48,1,2,1))
_CgprsGtpCurRxPacketQueueSize_Type=Gauge32
_CgprsGtpCurRxPacketQueueSize_Object=MibScalar
cgprsGtpCurRxPacketQueueSize=_CgprsGtpCurRxPacketQueueSize_Object((1,3,6,1,4,1,9,10,48,1,2,1,1),_CgprsGtpCurRxPacketQueueSize_Type())
cgprsGtpCurRxPacketQueueSize.setMaxAccess(_C)
if mibBuilder.loadTexts:cgprsGtpCurRxPacketQueueSize.setStatus(_A)
if mibBuilder.loadTexts:cgprsGtpCurRxPacketQueueSize.setUnits(_W)
_CgprsGtpCurActivatedPDPCxtsCnt_Type=Gauge32
_CgprsGtpCurActivatedPDPCxtsCnt_Object=MibScalar
cgprsGtpCurActivatedPDPCxtsCnt=_CgprsGtpCurActivatedPDPCxtsCnt_Object((1,3,6,1,4,1,9,10,48,1,2,1,2),_CgprsGtpCurActivatedPDPCxtsCnt_Type())
cgprsGtpCurActivatedPDPCxtsCnt.setMaxAccess(_C)
if mibBuilder.loadTexts:cgprsGtpCurActivatedPDPCxtsCnt.setStatus(_A)
if mibBuilder.loadTexts:cgprsGtpCurActivatedPDPCxtsCnt.setUnits(_J)
_CgprsGtpCurUnexpRxGpduCnt_Type=Counter32
_CgprsGtpCurUnexpRxGpduCnt_Object=MibScalar
cgprsGtpCurUnexpRxGpduCnt=_CgprsGtpCurUnexpRxGpduCnt_Object((1,3,6,1,4,1,9,10,48,1,2,1,3),_CgprsGtpCurUnexpRxGpduCnt_Type())
cgprsGtpCurUnexpRxGpduCnt.setMaxAccess(_C)
if mibBuilder.loadTexts:cgprsGtpCurUnexpRxGpduCnt.setStatus(_A)
if mibBuilder.loadTexts:cgprsGtpCurUnexpRxGpduCnt.setUnits('PDUs')
_CgprsGtpCurRejPDPCxtActivationCnt_Type=Counter32
_CgprsGtpCurRejPDPCxtActivationCnt_Object=MibScalar
cgprsGtpCurRejPDPCxtActivationCnt=_CgprsGtpCurRejPDPCxtActivationCnt_Object((1,3,6,1,4,1,9,10,48,1,2,1,4),_CgprsGtpCurRejPDPCxtActivationCnt_Type())
cgprsGtpCurRejPDPCxtActivationCnt.setMaxAccess(_C)
if mibBuilder.loadTexts:cgprsGtpCurRejPDPCxtActivationCnt.setStatus(_A)
if mibBuilder.loadTexts:cgprsGtpCurRejPDPCxtActivationCnt.setUnits(_J)
_CgprsGtpTotalPktsDropped_Type=Counter32
_CgprsGtpTotalPktsDropped_Object=MibScalar
cgprsGtpTotalPktsDropped=_CgprsGtpTotalPktsDropped_Object((1,3,6,1,4,1,9,10,48,1,2,1,5),_CgprsGtpTotalPktsDropped_Type())
cgprsGtpTotalPktsDropped.setMaxAccess(_C)
if mibBuilder.loadTexts:cgprsGtpTotalPktsDropped.setStatus(_A)
if mibBuilder.loadTexts:cgprsGtpTotalPktsDropped.setUnits(_W)
class _CgprsGtpDroppedPktsTimeFrame_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CgprsGtpDroppedPktsTimeFrame_Type.__name__=_D
_CgprsGtpDroppedPktsTimeFrame_Object=MibScalar
cgprsGtpDroppedPktsTimeFrame=_CgprsGtpDroppedPktsTimeFrame_Object((1,3,6,1,4,1,9,10,48,1,2,1,6),_CgprsGtpDroppedPktsTimeFrame_Type())
cgprsGtpDroppedPktsTimeFrame.setMaxAccess(_C)
if mibBuilder.loadTexts:cgprsGtpDroppedPktsTimeFrame.setStatus(_A)
if mibBuilder.loadTexts:cgprsGtpDroppedPktsTimeFrame.setUnits(_G)
_CgprsGtpDroppedPktsCnt_Type=Counter32
_CgprsGtpDroppedPktsCnt_Object=MibScalar
cgprsGtpDroppedPktsCnt=_CgprsGtpDroppedPktsCnt_Object((1,3,6,1,4,1,9,10,48,1,2,1,7),_CgprsGtpDroppedPktsCnt_Type())
cgprsGtpDroppedPktsCnt.setMaxAccess(_C)
if mibBuilder.loadTexts:cgprsGtpDroppedPktsCnt.setStatus(_A)
_CgprsGtpCurMTForPremiumQos_Type=Gauge32
_CgprsGtpCurMTForPremiumQos_Object=MibScalar
cgprsGtpCurMTForPremiumQos=_CgprsGtpCurMTForPremiumQos_Object((1,3,6,1,4,1,9,10,48,1,2,1,8),_CgprsGtpCurMTForPremiumQos_Type())
cgprsGtpCurMTForPremiumQos.setMaxAccess(_C)
if mibBuilder.loadTexts:cgprsGtpCurMTForPremiumQos.setStatus(_A)
if mibBuilder.loadTexts:cgprsGtpCurMTForPremiumQos.setUnits(_H)
_CgprsGtpCurMTForNormalQos_Type=Gauge32
_CgprsGtpCurMTForNormalQos_Object=MibScalar
cgprsGtpCurMTForNormalQos=_CgprsGtpCurMTForNormalQos_Object((1,3,6,1,4,1,9,10,48,1,2,1,9),_CgprsGtpCurMTForNormalQos_Type())
cgprsGtpCurMTForNormalQos.setMaxAccess(_C)
if mibBuilder.loadTexts:cgprsGtpCurMTForNormalQos.setStatus(_A)
if mibBuilder.loadTexts:cgprsGtpCurMTForNormalQos.setUnits(_H)
_CgprsGtpCurMTForBestEffortQos_Type=Gauge32
_CgprsGtpCurMTForBestEffortQos_Object=MibScalar
cgprsGtpCurMTForBestEffortQos=_CgprsGtpCurMTForBestEffortQos_Object((1,3,6,1,4,1,9,10,48,1,2,1,10),_CgprsGtpCurMTForBestEffortQos_Type())
cgprsGtpCurMTForBestEffortQos.setMaxAccess(_C)
if mibBuilder.loadTexts:cgprsGtpCurMTForBestEffortQos.setStatus(_A)
if mibBuilder.loadTexts:cgprsGtpCurMTForBestEffortQos.setUnits(_H)
_CgprsGtpCurGSNBandwidthResrcUsed_Type=Gauge32
_CgprsGtpCurGSNBandwidthResrcUsed_Object=MibScalar
cgprsGtpCurGSNBandwidthResrcUsed=_CgprsGtpCurGSNBandwidthResrcUsed_Object((1,3,6,1,4,1,9,10,48,1,2,1,11),_CgprsGtpCurGSNBandwidthResrcUsed_Type())
cgprsGtpCurGSNBandwidthResrcUsed.setMaxAccess(_C)
if mibBuilder.loadTexts:cgprsGtpCurGSNBandwidthResrcUsed.setStatus(_A)
if mibBuilder.loadTexts:cgprsGtpCurGSNBandwidthResrcUsed.setUnits(_H)
_CgprsGtpGSNTable_Object=MibTable
cgprsGtpGSNTable=_CgprsGtpGSNTable_Object((1,3,6,1,4,1,9,10,48,1,2,1,12))
if mibBuilder.loadTexts:cgprsGtpGSNTable.setStatus(_A)
_CgprsGtpGSNEntry_Object=MibTableRow
cgprsGtpGSNEntry=_CgprsGtpGSNEntry_Object((1,3,6,1,4,1,9,10,48,1,2,1,12,1))
cgprsGtpGSNEntry.setIndexNames((0,_B,_X))
if mibBuilder.loadTexts:cgprsGtpGSNEntry.setStatus(_A)
_CgprsGtpGSNid_Type=IpAddress
_CgprsGtpGSNid_Object=MibTableColumn
cgprsGtpGSNid=_CgprsGtpGSNid_Object((1,3,6,1,4,1,9,10,48,1,2,1,12,1,1),_CgprsGtpGSNid_Type())
cgprsGtpGSNid.setMaxAccess(_K)
if mibBuilder.loadTexts:cgprsGtpGSNid.setStatus(_A)
_CgprsGtpGSNEchoFailedNotifCnt_Type=Counter32
_CgprsGtpGSNEchoFailedNotifCnt_Object=MibTableColumn
cgprsGtpGSNEchoFailedNotifCnt=_CgprsGtpGSNEchoFailedNotifCnt_Object((1,3,6,1,4,1,9,10,48,1,2,1,12,1,2),_CgprsGtpGSNEchoFailedNotifCnt_Type())
cgprsGtpGSNEchoFailedNotifCnt.setMaxAccess(_C)
if mibBuilder.loadTexts:cgprsGtpGSNEchoFailedNotifCnt.setStatus(_A)
_CgprsGtpGgsnStats_ObjectIdentity=ObjectIdentity
cgprsGtpGgsnStats=_CgprsGtpGgsnStats_ObjectIdentity((1,3,6,1,4,1,9,10,48,1,2,2))
_CgprsGtpTotalNumAllocIpAddr_Type=Gauge32
_CgprsGtpTotalNumAllocIpAddr_Object=MibScalar
cgprsGtpTotalNumAllocIpAddr=_CgprsGtpTotalNumAllocIpAddr_Object((1,3,6,1,4,1,9,10,48,1,2,2,1),_CgprsGtpTotalNumAllocIpAddr_Type())
cgprsGtpTotalNumAllocIpAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:cgprsGtpTotalNumAllocIpAddr.setStatus(_A)
if mibBuilder.loadTexts:cgprsGtpTotalNumAllocIpAddr.setUnits('allocated dynamic addreses')
_CgprsGtpChargingMsgCnt_Type=Gauge32
_CgprsGtpChargingMsgCnt_Object=MibScalar
cgprsGtpChargingMsgCnt=_CgprsGtpChargingMsgCnt_Object((1,3,6,1,4,1,9,10,48,1,2,2,2),_CgprsGtpChargingMsgCnt_Type())
cgprsGtpChargingMsgCnt.setMaxAccess(_C)
if mibBuilder.loadTexts:cgprsGtpChargingMsgCnt.setStatus(_A)
_CgprsGtpNumAllocIpAddrTable_Object=MibTable
cgprsGtpNumAllocIpAddrTable=_CgprsGtpNumAllocIpAddrTable_Object((1,3,6,1,4,1,9,10,48,1,2,2,3))
if mibBuilder.loadTexts:cgprsGtpNumAllocIpAddrTable.setStatus(_A)
_CgprsGtpNumAllocIpAddrEntry_Object=MibTableRow
cgprsGtpNumAllocIpAddrEntry=_CgprsGtpNumAllocIpAddrEntry_Object((1,3,6,1,4,1,9,10,48,1,2,2,3,1))
cgprsGtpNumAllocIpAddrEntry.setIndexNames((0,_B,_L))
if mibBuilder.loadTexts:cgprsGtpNumAllocIpAddrEntry.setStatus(_A)
_CgprsGtpNumAllocIpAddr_Type=Gauge32
_CgprsGtpNumAllocIpAddr_Object=MibTableColumn
cgprsGtpNumAllocIpAddr=_CgprsGtpNumAllocIpAddr_Object((1,3,6,1,4,1,9,10,48,1,2,2,3,1,1),_CgprsGtpNumAllocIpAddr_Type())
cgprsGtpNumAllocIpAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:cgprsGtpNumAllocIpAddr.setStatus(_A)
_CgprsGtpGgsnStatus_ObjectIdentity=ObjectIdentity
cgprsGtpGgsnStatus=_CgprsGtpGgsnStatus_ObjectIdentity((1,3,6,1,4,1,9,10,48,1,2,3))
_CgprsGtpVersion_Type=DisplayString
_CgprsGtpVersion_Object=MibScalar
cgprsGtpVersion=_CgprsGtpVersion_Object((1,3,6,1,4,1,9,10,48,1,2,3,1),_CgprsGtpVersion_Type())
cgprsGtpVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:cgprsGtpVersion.setStatus(_A)
_CgprsGtpLastGSNidNoRespToEcho_Type=DisplayString
_CgprsGtpLastGSNidNoRespToEcho_Object=MibScalar
cgprsGtpLastGSNidNoRespToEcho=_CgprsGtpLastGSNidNoRespToEcho_Object((1,3,6,1,4,1,9,10,48,1,2,3,2),_CgprsGtpLastGSNidNoRespToEcho_Type())
cgprsGtpLastGSNidNoRespToEcho.setMaxAccess(_C)
if mibBuilder.loadTexts:cgprsGtpLastGSNidNoRespToEcho.setStatus(_A)
_CgprsGtpLastGSNidRecovered_Type=DisplayString
_CgprsGtpLastGSNidRecovered_Object=MibScalar
cgprsGtpLastGSNidRecovered=_CgprsGtpLastGSNidRecovered_Object((1,3,6,1,4,1,9,10,48,1,2,3,3),_CgprsGtpLastGSNidRecovered_Type())
cgprsGtpLastGSNidRecovered.setMaxAccess(_C)
if mibBuilder.loadTexts:cgprsGtpLastGSNidRecovered.setStatus(_A)
_CgprsGtpGSNidOfLastUnexpPDPCxt_Type=DisplayString
_CgprsGtpGSNidOfLastUnexpPDPCxt_Object=MibScalar
cgprsGtpGSNidOfLastUnexpPDPCxt=_CgprsGtpGSNidOfLastUnexpPDPCxt_Object((1,3,6,1,4,1,9,10,48,1,2,3,4),_CgprsGtpGSNidOfLastUnexpPDPCxt_Type())
cgprsGtpGSNidOfLastUnexpPDPCxt.setMaxAccess(_C)
if mibBuilder.loadTexts:cgprsGtpGSNidOfLastUnexpPDPCxt.setStatus(_A)
_CgprsGtpTIDOfLastUnexpPDPCxt_Type=DisplayString
_CgprsGtpTIDOfLastUnexpPDPCxt_Object=MibScalar
cgprsGtpTIDOfLastUnexpPDPCxt=_CgprsGtpTIDOfLastUnexpPDPCxt_Object((1,3,6,1,4,1,9,10,48,1,2,3,5),_CgprsGtpTIDOfLastUnexpPDPCxt_Type())
cgprsGtpTIDOfLastUnexpPDPCxt.setMaxAccess(_C)
if mibBuilder.loadTexts:cgprsGtpTIDOfLastUnexpPDPCxt.setStatus(_A)
_CgprsGtpRejReasonOfLastUnexpPDPCxt_Type=DisplayString
_CgprsGtpRejReasonOfLastUnexpPDPCxt_Object=MibScalar
cgprsGtpRejReasonOfLastUnexpPDPCxt=_CgprsGtpRejReasonOfLastUnexpPDPCxt_Object((1,3,6,1,4,1,9,10,48,1,2,3,6),_CgprsGtpRejReasonOfLastUnexpPDPCxt_Type())
cgprsGtpRejReasonOfLastUnexpPDPCxt.setMaxAccess(_C)
if mibBuilder.loadTexts:cgprsGtpRejReasonOfLastUnexpPDPCxt.setStatus(_A)
_CiscoGprsGtpNotifPrefix_ObjectIdentity=ObjectIdentity
ciscoGprsGtpNotifPrefix=_CiscoGprsGtpNotifPrefix_ObjectIdentity((1,3,6,1,4,1,9,10,48,2))
_CiscoGprsGtpNotifs_ObjectIdentity=ObjectIdentity
ciscoGprsGtpNotifs=_CiscoGprsGtpNotifs_ObjectIdentity((1,3,6,1,4,1,9,10,48,2,0))
_CiscoGprsGtpConformances_ObjectIdentity=ObjectIdentity
ciscoGprsGtpConformances=_CiscoGprsGtpConformances_ObjectIdentity((1,3,6,1,4,1,9,10,48,3))
_CgprsGtpCompliances_ObjectIdentity=ObjectIdentity
cgprsGtpCompliances=_CgprsGtpCompliances_ObjectIdentity((1,3,6,1,4,1,9,10,48,3,1))
_CgprsGtpGroups_ObjectIdentity=ObjectIdentity
cgprsGtpGroups=_CgprsGtpGroups_ObjectIdentity((1,3,6,1,4,1,9,10,48,3,2))
cgprsGtpGeneralConfigGroup=ObjectGroup((1,3,6,1,4,1,9,10,48,3,2,1))
cgprsGtpGeneralConfigGroup.setObjects(*((_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h)))
if mibBuilder.loadTexts:cgprsGtpGeneralConfigGroup.setStatus(_A)
cgprsGtpGgsnConfigGroup=ObjectGroup((1,3,6,1,4,1,9,10,48,3,2,2))
cgprsGtpGgsnConfigGroup.setObjects(*((_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q)))
if mibBuilder.loadTexts:cgprsGtpGgsnConfigGroup.setStatus(_A)
cgprsGtpGeneralStatsGroup=ObjectGroup((1,3,6,1,4,1,9,10,48,3,2,3))
cgprsGtpGeneralStatsGroup.setObjects(*((_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_x),(_B,_y),(_B,_z),(_B,_A0),(_B,_A1),(_B,_A2)))
if mibBuilder.loadTexts:cgprsGtpGeneralStatsGroup.setStatus(_A)
cgprsGtpGgsnStatsGroup=ObjectGroup((1,3,6,1,4,1,9,10,48,3,2,4))
cgprsGtpGgsnStatsGroup.setObjects(*((_B,_A3),(_B,_A4)))
if mibBuilder.loadTexts:cgprsGtpGgsnStatsGroup.setStatus(_A)
cgprsGtpGgsnStatusGroup=ObjectGroup((1,3,6,1,4,1,9,10,48,3,2,5))
cgprsGtpGgsnStatusGroup.setObjects(*((_B,_A5),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_A6)))
if mibBuilder.loadTexts:cgprsGtpGgsnStatusGroup.setStatus(_A)
cgprsGtpGSNPathFailedNotif=NotificationType((1,3,6,1,4,1,9,10,48,2,0,1))
cgprsGtpGSNPathFailedNotif.setObjects((_B,_M))
if mibBuilder.loadTexts:cgprsGtpGSNPathFailedNotif.setStatus(_A)
cgprsGtpGSNPathRecoveredNotif=NotificationType((1,3,6,1,4,1,9,10,48,2,0,2))
cgprsGtpGSNPathRecoveredNotif.setObjects((_B,_N))
if mibBuilder.loadTexts:cgprsGtpGSNPathRecoveredNotif.setStatus(_A)
cgprsGtpPDPCxtActivationRejNotif=NotificationType((1,3,6,1,4,1,9,10,48,2,0,3))
cgprsGtpPDPCxtActivationRejNotif.setObjects(*((_B,_O),(_B,_P),(_B,_Q)))
if mibBuilder.loadTexts:cgprsGtpPDPCxtActivationRejNotif.setStatus(_A)
cgprsGtpPrimaryChargingGWUpNotif=NotificationType((1,3,6,1,4,1,9,10,48,2,0,4))
if mibBuilder.loadTexts:cgprsGtpPrimaryChargingGWUpNotif.setStatus(_A)
cgprsGtpPrimaryChargingGWDownNotif=NotificationType((1,3,6,1,4,1,9,10,48,2,0,5))
if mibBuilder.loadTexts:cgprsGtpPrimaryChargingGWDownNotif.setStatus(_A)
cgprsGtpSecondaryChargingGWUpNotif=NotificationType((1,3,6,1,4,1,9,10,48,2,0,6))
if mibBuilder.loadTexts:cgprsGtpSecondaryChargingGWUpNotif.setStatus(_A)
cgprsGtpSecondaryChargingGWDownNotif=NotificationType((1,3,6,1,4,1,9,10,48,2,0,7))
if mibBuilder.loadTexts:cgprsGtpSecondaryChargingGWDownNotif.setStatus(_A)
cgprsGtpGgsnNotifGroup=NotificationGroup((1,3,6,1,4,1,9,10,48,3,2,6))
cgprsGtpGgsnNotifGroup.setObjects(*((_B,_A7),(_B,_A8),(_B,_A9),(_B,_AA),(_B,_AB),(_B,_AC),(_B,_AD)))
if mibBuilder.loadTexts:cgprsGtpGgsnNotifGroup.setStatus(_A)
cgprsGtpCompliance=ModuleCompliance((1,3,6,1,4,1,9,10,48,3,1,1))
cgprsGtpCompliance.setObjects(*((_B,_AE),(_B,_AF),(_B,_AG),(_B,_AH),(_B,_AI)))
if mibBuilder.loadTexts:cgprsGtpCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ciscoGprsGtpMIB':ciscoGprsGtpMIB,'ciscoGprsGtpMIBObjects':ciscoGprsGtpMIBObjects,'ciscoGprsGtpConfig':ciscoGprsGtpConfig,'cgprsGtpGeneralConfig':cgprsGtpGeneralConfig,_Y:cgprsGtpT3TunnelTimer,_Z:cgprsGtpT3ResponseTimer,_a:cgprsGtpN3Request,_b:cgprsGtpN3BufferSize,_c:cgprsGtpEchoRequestTimer,_d:cgprsGtpGSNTotalBandwidthResrc,_e:cgprsGtpMaxNumPDPCxts,_f:cgprsGtpDroppedPktsMonTime,_g:cgprsGtpNoRespToEchoNotifEnable,_h:cgprsGtpPDPCxtActRejNotifEnable,'cgprsGtpGgsnConfig':cgprsGtpGgsnConfig,_i:cgprsGtpAPNAddrAllocMethodGlobDef,'cgprsGtpChargingGWTable':cgprsGtpChargingGWTable,'cgprsGtpChargingGWEntry':cgprsGtpChargingGWEntry,_V:cgprsGtpChargingGWid,_j:cgprsGtpChargingGWName,_k:cgprsGtpChargingGWType,_l:cgprsGtpChargingGWOperState,_m:cgprsGtpChargingGWNotifEnable,_n:cgprsGtpChargingGWRowStatus,'cgprsGtpAPNTable':cgprsGtpAPNTable,'cgprsGtpAPNEntry':cgprsGtpAPNEntry,_L:cgprsGtpAPNId,_o:cgprsGtpAPNName,_p:cgprsGtpAPNAddrAllocMethod,_q:cgprsGtpAPNRowStatus,'ciscoGprsGtpStats':ciscoGprsGtpStats,'cgprsGtpGeneralStats':cgprsGtpGeneralStats,_r:cgprsGtpCurRxPacketQueueSize,_s:cgprsGtpCurActivatedPDPCxtsCnt,_t:cgprsGtpCurUnexpRxGpduCnt,_u:cgprsGtpCurRejPDPCxtActivationCnt,_v:cgprsGtpTotalPktsDropped,_w:cgprsGtpDroppedPktsTimeFrame,_x:cgprsGtpDroppedPktsCnt,_y:cgprsGtpCurMTForPremiumQos,_z:cgprsGtpCurMTForNormalQos,_A0:cgprsGtpCurMTForBestEffortQos,_A1:cgprsGtpCurGSNBandwidthResrcUsed,'cgprsGtpGSNTable':cgprsGtpGSNTable,'cgprsGtpGSNEntry':cgprsGtpGSNEntry,_X:cgprsGtpGSNid,_A2:cgprsGtpGSNEchoFailedNotifCnt,'cgprsGtpGgsnStats':cgprsGtpGgsnStats,_A3:cgprsGtpTotalNumAllocIpAddr,_A4:cgprsGtpChargingMsgCnt,'cgprsGtpNumAllocIpAddrTable':cgprsGtpNumAllocIpAddrTable,'cgprsGtpNumAllocIpAddrEntry':cgprsGtpNumAllocIpAddrEntry,_A6:cgprsGtpNumAllocIpAddr,'cgprsGtpGgsnStatus':cgprsGtpGgsnStatus,_A5:cgprsGtpVersion,_M:cgprsGtpLastGSNidNoRespToEcho,_N:cgprsGtpLastGSNidRecovered,_O:cgprsGtpGSNidOfLastUnexpPDPCxt,_P:cgprsGtpTIDOfLastUnexpPDPCxt,_Q:cgprsGtpRejReasonOfLastUnexpPDPCxt,'ciscoGprsGtpNotifPrefix':ciscoGprsGtpNotifPrefix,'ciscoGprsGtpNotifs':ciscoGprsGtpNotifs,_A7:cgprsGtpGSNPathFailedNotif,_A8:cgprsGtpGSNPathRecoveredNotif,_A9:cgprsGtpPDPCxtActivationRejNotif,_AA:cgprsGtpPrimaryChargingGWUpNotif,_AB:cgprsGtpPrimaryChargingGWDownNotif,_AC:cgprsGtpSecondaryChargingGWUpNotif,_AD:cgprsGtpSecondaryChargingGWDownNotif,'ciscoGprsGtpConformances':ciscoGprsGtpConformances,'cgprsGtpCompliances':cgprsGtpCompliances,'cgprsGtpCompliance':cgprsGtpCompliance,'cgprsGtpGroups':cgprsGtpGroups,_AE:cgprsGtpGeneralConfigGroup,_AG:cgprsGtpGgsnConfigGroup,_AF:cgprsGtpGeneralStatsGroup,_AH:cgprsGtpGgsnStatsGroup,_AI:cgprsGtpGgsnStatusGroup,'cgprsGtpGgsnNotifGroup':cgprsGtpGgsnNotifGroup})