_U='tapSharedMedia'
_T='tapFilterCnx'
_S='tapMarkCnx'
_R='tapDeleteCnx'
_Q='tapIgnore'
_P='halfCnxDone'
_O='alterCnxDone'
_N='alterCnx'
_M='halfCnx'
_L='decisionUnknown'
_K='probeNotFound'
_J='keepOutport'
_I='disableOutport'
_H='sfpsTapHeaderDASA'
_G='CTRON-SFPS-TAP-MIB'
_F='unassigned'
_E='other'
_D='read-write'
_C='Integer32'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
sfpsCallTap,sfpsTap,sfpsTapStats=mibBuilder.importSymbols('CTRON-SFPS-INCLUDE-MIB','sfpsCallTap','sfpsTap','sfpsTapStats')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
class _SfpsCallTapVerb_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_E,1),('call-tap',2),('call-untap',3),('vlan-tap',4),('vlan-untap',5)))
_SfpsCallTapVerb_Type.__name__=_C
_SfpsCallTapVerb_Object=MibScalar
sfpsCallTapVerb=_SfpsCallTapVerb_Object((1,3,6,1,4,1,52,4,2,4,2,1,11,1),_SfpsCallTapVerb_Type())
sfpsCallTapVerb.setMaxAccess(_D)
if mibBuilder.loadTexts:sfpsCallTapVerb.setStatus(_A)
class _SfpsCallTapHeaderType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),('mac-da-sa',2),('atm-vpi-vci',3)))
_SfpsCallTapHeaderType_Type.__name__=_C
_SfpsCallTapHeaderType_Object=MibScalar
sfpsCallTapHeaderType=_SfpsCallTapHeaderType_Object((1,3,6,1,4,1,52,4,2,4,2,1,11,2),_SfpsCallTapHeaderType_Type())
sfpsCallTapHeaderType.setMaxAccess(_D)
if mibBuilder.loadTexts:sfpsCallTapHeaderType.setStatus(_A)
_SfpsCallTapHeaderLength_Type=Integer32
_SfpsCallTapHeaderLength_Object=MibScalar
sfpsCallTapHeaderLength=_SfpsCallTapHeaderLength_Object((1,3,6,1,4,1,52,4,2,4,2,1,11,3),_SfpsCallTapHeaderLength_Type())
sfpsCallTapHeaderLength.setMaxAccess(_D)
if mibBuilder.loadTexts:sfpsCallTapHeaderLength.setStatus(_A)
_SfpsCallTapHeaderValue_Type=DisplayString
_SfpsCallTapHeaderValue_Object=MibScalar
sfpsCallTapHeaderValue=_SfpsCallTapHeaderValue_Object((1,3,6,1,4,1,52,4,2,4,2,1,11,4),_SfpsCallTapHeaderValue_Type())
sfpsCallTapHeaderValue.setMaxAccess(_D)
if mibBuilder.loadTexts:sfpsCallTapHeaderValue.setStatus(_A)
class _SfpsCallTapArgDirection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),('bi',2),('uni',3)))
_SfpsCallTapArgDirection_Type.__name__=_C
_SfpsCallTapArgDirection_Object=MibScalar
sfpsCallTapArgDirection=_SfpsCallTapArgDirection_Object((1,3,6,1,4,1,52,4,2,4,2,1,11,5),_SfpsCallTapArgDirection_Type())
sfpsCallTapArgDirection.setMaxAccess(_D)
if mibBuilder.loadTexts:sfpsCallTapArgDirection.setStatus(_A)
_SfpsCallTapProbeSwitch_Type=OctetString
_SfpsCallTapProbeSwitch_Object=MibScalar
sfpsCallTapProbeSwitch=_SfpsCallTapProbeSwitch_Object((1,3,6,1,4,1,52,4,2,4,2,1,11,6),_SfpsCallTapProbeSwitch_Type())
sfpsCallTapProbeSwitch.setMaxAccess(_D)
if mibBuilder.loadTexts:sfpsCallTapProbeSwitch.setStatus(_A)
_SfpsCallTapProbePort_Type=Integer32
_SfpsCallTapProbePort_Object=MibScalar
sfpsCallTapProbePort=_SfpsCallTapProbePort_Object((1,3,6,1,4,1,52,4,2,4,2,1,11,7),_SfpsCallTapProbePort_Type())
sfpsCallTapProbePort.setMaxAccess(_D)
if mibBuilder.loadTexts:sfpsCallTapProbePort.setStatus(_A)
_SfpsTapTable_Object=MibTable
sfpsTapTable=_SfpsTapTable_Object((1,3,6,1,4,1,52,4,2,4,2,1,12,1))
if mibBuilder.loadTexts:sfpsTapTable.setStatus(_A)
_SfpsTapEntry_Object=MibTableRow
sfpsTapEntry=_SfpsTapEntry_Object((1,3,6,1,4,1,52,4,2,4,2,1,12,1,1))
sfpsTapEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:sfpsTapEntry.setStatus(_A)
_SfpsTapHeaderDASA_Type=DisplayString
_SfpsTapHeaderDASA_Object=MibTableColumn
sfpsTapHeaderDASA=_SfpsTapHeaderDASA_Object((1,3,6,1,4,1,52,4,2,4,2,1,12,1,1,1),_SfpsTapHeaderDASA_Type())
sfpsTapHeaderDASA.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsTapHeaderDASA.setStatus(_A)
_SfpsTapRQPort_Type=Integer32
_SfpsTapRQPort_Object=MibTableColumn
sfpsTapRQPort=_SfpsTapRQPort_Object((1,3,6,1,4,1,52,4,2,4,2,1,12,1,1,2),_SfpsTapRQPort_Type())
sfpsTapRQPort.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsTapRQPort.setStatus(_A)
_SfpsTapRSPPort_Type=Integer32
_SfpsTapRSPPort_Object=MibTableColumn
sfpsTapRSPPort=_SfpsTapRSPPort_Object((1,3,6,1,4,1,52,4,2,4,2,1,12,1,1,3),_SfpsTapRSPPort_Type())
sfpsTapRSPPort.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsTapRSPPort.setStatus(_A)
_SfpsTapRetries_Type=Integer32
_SfpsTapRetries_Object=MibTableColumn
sfpsTapRetries=_SfpsTapRetries_Object((1,3,6,1,4,1,52,4,2,4,2,1,12,1,1,4),_SfpsTapRetries_Type())
sfpsTapRetries.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsTapRetries.setStatus(_A)
class _SfpsTapSwitchState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('awaitingTapRsps',1),('receivingTapRsps',2),('retryingTapRequest',3),('tapActive',4),('awaitingUnTapRsps',5),('receivingUnTapRsps',6),('retryingUnTapRequest',7),(_F,8)))
_SfpsTapSwitchState_Type.__name__=_C
_SfpsTapSwitchState_Object=MibTableColumn
sfpsTapSwitchState=_SfpsTapSwitchState_Object((1,3,6,1,4,1,52,4,2,4,2,1,12,1,1,5),_SfpsTapSwitchState_Type())
sfpsTapSwitchState.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsTapSwitchState.setStatus(_A)
class _SfpsTapSwitchType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('originatingTap',1),('intermediate',2),('terminal',3),('originatingUntap',4)))
_SfpsTapSwitchType_Type.__name__=_C
_SfpsTapSwitchType_Object=MibTableColumn
sfpsTapSwitchType=_SfpsTapSwitchType_Object((1,3,6,1,4,1,52,4,2,4,2,1,12,1,1,6),_SfpsTapSwitchType_Type())
sfpsTapSwitchType.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsTapSwitchType.setStatus(_A)
class _SfpsTapSwitchStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14)));namedValues=NamedValues(*((_I,1),(_J,2),(_K,3),(_L,4),(_F,5),(_M,6),(_N,7),(_O,8),(_P,9),(_Q,10),(_R,11),(_S,12),(_T,13),(_U,14)))
_SfpsTapSwitchStatus_Type.__name__=_C
_SfpsTapSwitchStatus_Object=MibTableColumn
sfpsTapSwitchStatus=_SfpsTapSwitchStatus_Object((1,3,6,1,4,1,52,4,2,4,2,1,12,1,1,7),_SfpsTapSwitchStatus_Type())
sfpsTapSwitchStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsTapSwitchStatus.setStatus(_A)
class _SfpsTapDirection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),('bi-Directional',2),('uni-Directional',3)))
_SfpsTapDirection_Type.__name__=_C
_SfpsTapDirection_Object=MibTableColumn
sfpsTapDirection=_SfpsTapDirection_Object((1,3,6,1,4,1,52,4,2,4,2,1,12,1,1,8),_SfpsTapDirection_Type())
sfpsTapDirection.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsTapDirection.setStatus(_A)
_SfpsTapDirectRouteMAC_Type=DisplayString
_SfpsTapDirectRouteMAC_Object=MibTableColumn
sfpsTapDirectRouteMAC=_SfpsTapDirectRouteMAC_Object((1,3,6,1,4,1,52,4,2,4,2,1,12,1,1,9),_SfpsTapDirectRouteMAC_Type())
sfpsTapDirectRouteMAC.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsTapDirectRouteMAC.setStatus(_A)
class _SfpsTapResponseStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14)));namedValues=NamedValues(*((_I,1),(_J,2),(_K,3),(_L,4),(_F,5),(_M,6),(_N,7),(_O,8),(_P,9),(_Q,10),(_R,11),(_S,12),(_T,13),(_U,14)))
_SfpsTapResponseStatus_Type.__name__=_C
_SfpsTapResponseStatus_Object=MibTableColumn
sfpsTapResponseStatus=_SfpsTapResponseStatus_Object((1,3,6,1,4,1,52,4,2,4,2,1,12,1,1,10),_SfpsTapResponseStatus_Type())
sfpsTapResponseStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsTapResponseStatus.setStatus(_A)
_SfpsTapProbeSwitchMac_Type=DisplayString
_SfpsTapProbeSwitchMac_Object=MibTableColumn
sfpsTapProbeSwitchMac=_SfpsTapProbeSwitchMac_Object((1,3,6,1,4,1,52,4,2,4,2,1,12,1,1,11),_SfpsTapProbeSwitchMac_Type())
sfpsTapProbeSwitchMac.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsTapProbeSwitchMac.setStatus(_A)
_SfpsTapProbePort_Type=Integer32
_SfpsTapProbePort_Object=MibTableColumn
sfpsTapProbePort=_SfpsTapProbePort_Object((1,3,6,1,4,1,52,4,2,4,2,1,12,1,1,12),_SfpsTapProbePort_Type())
sfpsTapProbePort.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsTapProbePort.setStatus(_A)
_SfpsTapStatsTapReqCnt_Type=Integer32
_SfpsTapStatsTapReqCnt_Object=MibScalar
sfpsTapStatsTapReqCnt=_SfpsTapStatsTapReqCnt_Object((1,3,6,1,4,1,52,4,2,4,2,1,13,1),_SfpsTapStatsTapReqCnt_Type())
sfpsTapStatsTapReqCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsTapStatsTapReqCnt.setStatus(_A)
_SfpsTapStatsTapRespCnt_Type=Integer32
_SfpsTapStatsTapRespCnt_Object=MibScalar
sfpsTapStatsTapRespCnt=_SfpsTapStatsTapRespCnt_Object((1,3,6,1,4,1,52,4,2,4,2,1,13,2),_SfpsTapStatsTapRespCnt_Type())
sfpsTapStatsTapRespCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsTapStatsTapRespCnt.setStatus(_A)
_SfpsTapStatsUntapReqCnt_Type=Integer32
_SfpsTapStatsUntapReqCnt_Object=MibScalar
sfpsTapStatsUntapReqCnt=_SfpsTapStatsUntapReqCnt_Object((1,3,6,1,4,1,52,4,2,4,2,1,13,3),_SfpsTapStatsUntapReqCnt_Type())
sfpsTapStatsUntapReqCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsTapStatsUntapReqCnt.setStatus(_A)
_SfpsTapStatsUntapRespCnt_Type=Integer32
_SfpsTapStatsUntapRespCnt_Object=MibScalar
sfpsTapStatsUntapRespCnt=_SfpsTapStatsUntapRespCnt_Object((1,3,6,1,4,1,52,4,2,4,2,1,13,4),_SfpsTapStatsUntapRespCnt_Type())
sfpsTapStatsUntapRespCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsTapStatsUntapRespCnt.setStatus(_A)
_SfpsTapStatsErrorCnt_Type=Integer32
_SfpsTapStatsErrorCnt_Object=MibScalar
sfpsTapStatsErrorCnt=_SfpsTapStatsErrorCnt_Object((1,3,6,1,4,1,52,4,2,4,2,1,13,5),_SfpsTapStatsErrorCnt_Type())
sfpsTapStatsErrorCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsTapStatsErrorCnt.setStatus(_A)
_SfpsTapStatsStaleEntCnt_Type=Integer32
_SfpsTapStatsStaleEntCnt_Object=MibScalar
sfpsTapStatsStaleEntCnt=_SfpsTapStatsStaleEntCnt_Object((1,3,6,1,4,1,52,4,2,4,2,1,13,6),_SfpsTapStatsStaleEntCnt_Type())
sfpsTapStatsStaleEntCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsTapStatsStaleEntCnt.setStatus(_A)
mibBuilder.exportSymbols(_G,**{'sfpsCallTapVerb':sfpsCallTapVerb,'sfpsCallTapHeaderType':sfpsCallTapHeaderType,'sfpsCallTapHeaderLength':sfpsCallTapHeaderLength,'sfpsCallTapHeaderValue':sfpsCallTapHeaderValue,'sfpsCallTapArgDirection':sfpsCallTapArgDirection,'sfpsCallTapProbeSwitch':sfpsCallTapProbeSwitch,'sfpsCallTapProbePort':sfpsCallTapProbePort,'sfpsTapTable':sfpsTapTable,'sfpsTapEntry':sfpsTapEntry,_H:sfpsTapHeaderDASA,'sfpsTapRQPort':sfpsTapRQPort,'sfpsTapRSPPort':sfpsTapRSPPort,'sfpsTapRetries':sfpsTapRetries,'sfpsTapSwitchState':sfpsTapSwitchState,'sfpsTapSwitchType':sfpsTapSwitchType,'sfpsTapSwitchStatus':sfpsTapSwitchStatus,'sfpsTapDirection':sfpsTapDirection,'sfpsTapDirectRouteMAC':sfpsTapDirectRouteMAC,'sfpsTapResponseStatus':sfpsTapResponseStatus,'sfpsTapProbeSwitchMac':sfpsTapProbeSwitchMac,'sfpsTapProbePort':sfpsTapProbePort,'sfpsTapStatsTapReqCnt':sfpsTapStatsTapReqCnt,'sfpsTapStatsTapRespCnt':sfpsTapStatsTapRespCnt,'sfpsTapStatsUntapReqCnt':sfpsTapStatsUntapReqCnt,'sfpsTapStatsUntapRespCnt':sfpsTapStatsUntapRespCnt,'sfpsTapStatsErrorCnt':sfpsTapStatsErrorCnt,'sfpsTapStatsStaleEntCnt':sfpsTapStatsStaleEntCnt})