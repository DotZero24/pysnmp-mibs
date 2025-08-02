_AD='ciscoWanFrConnQueueStatsGroup'
_AC='ciscoWanFrConnABRStatsGroup'
_AB='ciscoWanFrConnStatsGroup'
_AA='frChanFrmNotTurnedAroundCnt'
_A9='frChanBrmRcvFromNetworkCnt'
_A8='frChanFrmRcvFromNetworkCnt'
_A7='frChanCrcErrRmRcvFromNetworkCnt'
_A6='frChanBrmXmtToNetworkCnt'
_A5='frChanFrmXmtToNetworkCnt'
_A4='xmtFramesDiscXceedDEThresh'
_A3='xmtBytesDiscXceedQDepth'
_A2='xmtFramesDiscXceedQDepth'
_A1='rcvFramesDiscXceedDEThresh'
_A0='rcvBytesDiscXceedQDepth'
_z='rcvFramesDiscXceedQDepth'
_y='rcvBytesDEDiscard'
_x='xmtBytesDEDiscard'
_w='rcvFramesUnknownProtocols'
_v='xmtFramesUnknownProtocols'
_u='xmtFramesOversizedSDUs'
_t='xmtFramesLengthViolations'
_s='xmtFramesInvalidCPIs'
_r='xmtFramesTaggedDE'
_q='xmtBytesTaggedDE'
_p='rcvFramesDiscUPC'
_o='chanSecUpTime'
_n='chanClrButton'
_m='xmtKbpsAIR'
_l='xmtFramesTaggedBECN'
_k='xmtFramesTaggedFECN'
_j='xmtBytesDuringLMIAlarm'
_i='xmtFramesDuringLMIAlarm'
_h='xmtFramesDiscSrcAbort'
_g='xmtFramesDiscReassmFail'
_f='xmtFramesDiscCRCError'
_e='xmtFramesDiscPhyLayerFail'
_d='xmtBytesDiscard'
_c='xmtFramesDiscard'
_b='xmtBytesDE'
_a='xmtFramesDE'
_Z='xmtFramesBECN'
_Y='xmtFramesFECN'
_X='xmtBytes'
_W='xmtFrames'
_V='rcvKbpsAIR'
_U='rcvBytesTaggedDE'
_T='rcvFramesTaggedDE'
_S='rcvFramesTaggedBECN'
_R='rcvFramesTaggedFECN'
_Q='rcvFramesBECN'
_P='rcvFramesFECN'
_O='rcvFramesDiscShelfAlarm'
_N='rcvBytesDiscard'
_M='rcvFramesDiscard'
_L='rcvBytesDE'
_K='rcvFramesDE'
_J='rcvBytes'
_I='rcvFrames'
_H='frstdABRcntChanNum'
_G='cntChanNum'
_F='Integer32'
_E='Bytes'
_D='Frames'
_C='read-only'
_B='CISCO-WAN-FR-CONN-STAT-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
frChan,=mibBuilder.importSymbols('BASIS-MIB','frChan')
ciscoWan,=mibBuilder.importSymbols('CISCOWAN-SMI','ciscoWan')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
ciscoWanFrConnStatMIB=ModuleIdentity((1,3,6,1,4,1,351,150,48))
if mibBuilder.loadTexts:ciscoWanFrConnStatMIB.setRevisions(('2002-10-18 00:00',))
_FrChanCntGrp_ObjectIdentity=ObjectIdentity
frChanCntGrp=_FrChanCntGrp_ObjectIdentity((1,3,6,1,4,1,351,110,5,1,2,3))
_FrChanCntGrpTable_Object=MibTable
frChanCntGrpTable=_FrChanCntGrpTable_Object((1,3,6,1,4,1,351,110,5,1,2,3,1))
if mibBuilder.loadTexts:frChanCntGrpTable.setStatus(_A)
_FrChanCntGrpEntry_Object=MibTableRow
frChanCntGrpEntry=_FrChanCntGrpEntry_Object((1,3,6,1,4,1,351,110,5,1,2,3,1,1))
frChanCntGrpEntry.setIndexNames((0,_B,_G))
if mibBuilder.loadTexts:frChanCntGrpEntry.setStatus(_A)
class _CntChanNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_CntChanNum_Type.__name__=_F
_CntChanNum_Object=MibTableColumn
cntChanNum=_CntChanNum_Object((1,3,6,1,4,1,351,110,5,1,2,3,1,1,1),_CntChanNum_Type())
cntChanNum.setMaxAccess(_C)
if mibBuilder.loadTexts:cntChanNum.setStatus(_A)
_RcvFrames_Type=Counter32
_RcvFrames_Object=MibTableColumn
rcvFrames=_RcvFrames_Object((1,3,6,1,4,1,351,110,5,1,2,3,1,1,2),_RcvFrames_Type())
rcvFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:rcvFrames.setStatus(_A)
if mibBuilder.loadTexts:rcvFrames.setUnits(_D)
_RcvBytes_Type=Counter32
_RcvBytes_Object=MibTableColumn
rcvBytes=_RcvBytes_Object((1,3,6,1,4,1,351,110,5,1,2,3,1,1,3),_RcvBytes_Type())
rcvBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:rcvBytes.setStatus(_A)
if mibBuilder.loadTexts:rcvBytes.setUnits(_E)
_RcvFramesDE_Type=Counter32
_RcvFramesDE_Object=MibTableColumn
rcvFramesDE=_RcvFramesDE_Object((1,3,6,1,4,1,351,110,5,1,2,3,1,1,4),_RcvFramesDE_Type())
rcvFramesDE.setMaxAccess(_C)
if mibBuilder.loadTexts:rcvFramesDE.setStatus(_A)
if mibBuilder.loadTexts:rcvFramesDE.setUnits(_D)
_RcvBytesDE_Type=Counter32
_RcvBytesDE_Object=MibTableColumn
rcvBytesDE=_RcvBytesDE_Object((1,3,6,1,4,1,351,110,5,1,2,3,1,1,5),_RcvBytesDE_Type())
rcvBytesDE.setMaxAccess(_C)
if mibBuilder.loadTexts:rcvBytesDE.setStatus(_A)
if mibBuilder.loadTexts:rcvBytesDE.setUnits(_E)
_RcvFramesDiscard_Type=Counter32
_RcvFramesDiscard_Object=MibTableColumn
rcvFramesDiscard=_RcvFramesDiscard_Object((1,3,6,1,4,1,351,110,5,1,2,3,1,1,6),_RcvFramesDiscard_Type())
rcvFramesDiscard.setMaxAccess(_C)
if mibBuilder.loadTexts:rcvFramesDiscard.setStatus(_A)
if mibBuilder.loadTexts:rcvFramesDiscard.setUnits(_D)
_RcvBytesDiscard_Type=Counter32
_RcvBytesDiscard_Object=MibTableColumn
rcvBytesDiscard=_RcvBytesDiscard_Object((1,3,6,1,4,1,351,110,5,1,2,3,1,1,7),_RcvBytesDiscard_Type())
rcvBytesDiscard.setMaxAccess(_C)
if mibBuilder.loadTexts:rcvBytesDiscard.setStatus(_A)
if mibBuilder.loadTexts:rcvBytesDiscard.setUnits(_E)
_RcvFramesDiscShelfAlarm_Type=Counter32
_RcvFramesDiscShelfAlarm_Object=MibTableColumn
rcvFramesDiscShelfAlarm=_RcvFramesDiscShelfAlarm_Object((1,3,6,1,4,1,351,110,5,1,2,3,1,1,8),_RcvFramesDiscShelfAlarm_Type())
rcvFramesDiscShelfAlarm.setMaxAccess(_C)
if mibBuilder.loadTexts:rcvFramesDiscShelfAlarm.setStatus(_A)
if mibBuilder.loadTexts:rcvFramesDiscShelfAlarm.setUnits(_D)
_RcvFramesDiscXceedQDepth_Type=Counter32
_RcvFramesDiscXceedQDepth_Object=MibTableColumn
rcvFramesDiscXceedQDepth=_RcvFramesDiscXceedQDepth_Object((1,3,6,1,4,1,351,110,5,1,2,3,1,1,9),_RcvFramesDiscXceedQDepth_Type())
rcvFramesDiscXceedQDepth.setMaxAccess(_C)
if mibBuilder.loadTexts:rcvFramesDiscXceedQDepth.setStatus(_A)
if mibBuilder.loadTexts:rcvFramesDiscXceedQDepth.setUnits(_D)
_RcvBytesDiscXceedQDepth_Type=Counter32
_RcvBytesDiscXceedQDepth_Object=MibTableColumn
rcvBytesDiscXceedQDepth=_RcvBytesDiscXceedQDepth_Object((1,3,6,1,4,1,351,110,5,1,2,3,1,1,10),_RcvBytesDiscXceedQDepth_Type())
rcvBytesDiscXceedQDepth.setMaxAccess(_C)
if mibBuilder.loadTexts:rcvBytesDiscXceedQDepth.setStatus(_A)
if mibBuilder.loadTexts:rcvBytesDiscXceedQDepth.setUnits(_E)
_RcvFramesDiscXceedDEThresh_Type=Counter32
_RcvFramesDiscXceedDEThresh_Object=MibTableColumn
rcvFramesDiscXceedDEThresh=_RcvFramesDiscXceedDEThresh_Object((1,3,6,1,4,1,351,110,5,1,2,3,1,1,11),_RcvFramesDiscXceedDEThresh_Type())
rcvFramesDiscXceedDEThresh.setMaxAccess(_C)
if mibBuilder.loadTexts:rcvFramesDiscXceedDEThresh.setStatus(_A)
if mibBuilder.loadTexts:rcvFramesDiscXceedDEThresh.setUnits(_D)
_RcvFramesFECN_Type=Counter32
_RcvFramesFECN_Object=MibTableColumn
rcvFramesFECN=_RcvFramesFECN_Object((1,3,6,1,4,1,351,110,5,1,2,3,1,1,12),_RcvFramesFECN_Type())
rcvFramesFECN.setMaxAccess(_C)
if mibBuilder.loadTexts:rcvFramesFECN.setStatus(_A)
if mibBuilder.loadTexts:rcvFramesFECN.setUnits(_D)
_RcvFramesBECN_Type=Counter32
_RcvFramesBECN_Object=MibTableColumn
rcvFramesBECN=_RcvFramesBECN_Object((1,3,6,1,4,1,351,110,5,1,2,3,1,1,13),_RcvFramesBECN_Type())
rcvFramesBECN.setMaxAccess(_C)
if mibBuilder.loadTexts:rcvFramesBECN.setStatus(_A)
if mibBuilder.loadTexts:rcvFramesBECN.setUnits(_D)
_RcvFramesTaggedFECN_Type=Counter32
_RcvFramesTaggedFECN_Object=MibTableColumn
rcvFramesTaggedFECN=_RcvFramesTaggedFECN_Object((1,3,6,1,4,1,351,110,5,1,2,3,1,1,14),_RcvFramesTaggedFECN_Type())
rcvFramesTaggedFECN.setMaxAccess(_C)
if mibBuilder.loadTexts:rcvFramesTaggedFECN.setStatus(_A)
if mibBuilder.loadTexts:rcvFramesTaggedFECN.setUnits(_D)
_RcvFramesTaggedBECN_Type=Counter32
_RcvFramesTaggedBECN_Object=MibTableColumn
rcvFramesTaggedBECN=_RcvFramesTaggedBECN_Object((1,3,6,1,4,1,351,110,5,1,2,3,1,1,15),_RcvFramesTaggedBECN_Type())
rcvFramesTaggedBECN.setMaxAccess(_C)
if mibBuilder.loadTexts:rcvFramesTaggedBECN.setStatus(_A)
if mibBuilder.loadTexts:rcvFramesTaggedBECN.setUnits(_D)
_RcvFramesTaggedDE_Type=Counter32
_RcvFramesTaggedDE_Object=MibTableColumn
rcvFramesTaggedDE=_RcvFramesTaggedDE_Object((1,3,6,1,4,1,351,110,5,1,2,3,1,1,16),_RcvFramesTaggedDE_Type())
rcvFramesTaggedDE.setMaxAccess(_C)
if mibBuilder.loadTexts:rcvFramesTaggedDE.setStatus(_A)
if mibBuilder.loadTexts:rcvFramesTaggedDE.setUnits(_D)
_RcvBytesTaggedDE_Type=Counter32
_RcvBytesTaggedDE_Object=MibTableColumn
rcvBytesTaggedDE=_RcvBytesTaggedDE_Object((1,3,6,1,4,1,351,110,5,1,2,3,1,1,17),_RcvBytesTaggedDE_Type())
rcvBytesTaggedDE.setMaxAccess(_C)
if mibBuilder.loadTexts:rcvBytesTaggedDE.setStatus(_A)
if mibBuilder.loadTexts:rcvBytesTaggedDE.setUnits(_E)
_RcvKbpsAIR_Type=Integer32
_RcvKbpsAIR_Object=MibTableColumn
rcvKbpsAIR=_RcvKbpsAIR_Object((1,3,6,1,4,1,351,110,5,1,2,3,1,1,18),_RcvKbpsAIR_Type())
rcvKbpsAIR.setMaxAccess(_C)
if mibBuilder.loadTexts:rcvKbpsAIR.setStatus(_A)
if mibBuilder.loadTexts:rcvKbpsAIR.setUnits('kbps')
_XmtFrames_Type=Counter32
_XmtFrames_Object=MibTableColumn
xmtFrames=_XmtFrames_Object((1,3,6,1,4,1,351,110,5,1,2,3,1,1,19),_XmtFrames_Type())
xmtFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:xmtFrames.setStatus(_A)
if mibBuilder.loadTexts:xmtFrames.setUnits(_D)
_XmtBytes_Type=Counter32
_XmtBytes_Object=MibTableColumn
xmtBytes=_XmtBytes_Object((1,3,6,1,4,1,351,110,5,1,2,3,1,1,20),_XmtBytes_Type())
xmtBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:xmtBytes.setStatus(_A)
if mibBuilder.loadTexts:xmtBytes.setUnits(_E)
_XmtFramesFECN_Type=Counter32
_XmtFramesFECN_Object=MibTableColumn
xmtFramesFECN=_XmtFramesFECN_Object((1,3,6,1,4,1,351,110,5,1,2,3,1,1,21),_XmtFramesFECN_Type())
xmtFramesFECN.setMaxAccess(_C)
if mibBuilder.loadTexts:xmtFramesFECN.setStatus(_A)
if mibBuilder.loadTexts:xmtFramesFECN.setUnits(_D)
_XmtFramesBECN_Type=Counter32
_XmtFramesBECN_Object=MibTableColumn
xmtFramesBECN=_XmtFramesBECN_Object((1,3,6,1,4,1,351,110,5,1,2,3,1,1,22),_XmtFramesBECN_Type())
xmtFramesBECN.setMaxAccess(_C)
if mibBuilder.loadTexts:xmtFramesBECN.setStatus(_A)
if mibBuilder.loadTexts:xmtFramesBECN.setUnits(_D)
_XmtFramesDE_Type=Counter32
_XmtFramesDE_Object=MibTableColumn
xmtFramesDE=_XmtFramesDE_Object((1,3,6,1,4,1,351,110,5,1,2,3,1,1,23),_XmtFramesDE_Type())
xmtFramesDE.setMaxAccess(_C)
if mibBuilder.loadTexts:xmtFramesDE.setStatus(_A)
if mibBuilder.loadTexts:xmtFramesDE.setUnits(_D)
_XmtBytesDE_Type=Counter32
_XmtBytesDE_Object=MibTableColumn
xmtBytesDE=_XmtBytesDE_Object((1,3,6,1,4,1,351,110,5,1,2,3,1,1,24),_XmtBytesDE_Type())
xmtBytesDE.setMaxAccess(_C)
if mibBuilder.loadTexts:xmtBytesDE.setStatus(_A)
if mibBuilder.loadTexts:xmtBytesDE.setUnits(_E)
_XmtFramesDiscard_Type=Counter32
_XmtFramesDiscard_Object=MibTableColumn
xmtFramesDiscard=_XmtFramesDiscard_Object((1,3,6,1,4,1,351,110,5,1,2,3,1,1,25),_XmtFramesDiscard_Type())
xmtFramesDiscard.setMaxAccess(_C)
if mibBuilder.loadTexts:xmtFramesDiscard.setStatus(_A)
if mibBuilder.loadTexts:xmtFramesDiscard.setUnits(_D)
_XmtBytesDiscard_Type=Counter32
_XmtBytesDiscard_Object=MibTableColumn
xmtBytesDiscard=_XmtBytesDiscard_Object((1,3,6,1,4,1,351,110,5,1,2,3,1,1,26),_XmtBytesDiscard_Type())
xmtBytesDiscard.setMaxAccess(_C)
if mibBuilder.loadTexts:xmtBytesDiscard.setStatus(_A)
if mibBuilder.loadTexts:xmtBytesDiscard.setUnits(_E)
_XmtFramesDiscXceedQDepth_Type=Counter32
_XmtFramesDiscXceedQDepth_Object=MibTableColumn
xmtFramesDiscXceedQDepth=_XmtFramesDiscXceedQDepth_Object((1,3,6,1,4,1,351,110,5,1,2,3,1,1,27),_XmtFramesDiscXceedQDepth_Type())
xmtFramesDiscXceedQDepth.setMaxAccess(_C)
if mibBuilder.loadTexts:xmtFramesDiscXceedQDepth.setStatus(_A)
if mibBuilder.loadTexts:xmtFramesDiscXceedQDepth.setUnits(_D)
_XmtBytesDiscXceedQDepth_Type=Counter32
_XmtBytesDiscXceedQDepth_Object=MibTableColumn
xmtBytesDiscXceedQDepth=_XmtBytesDiscXceedQDepth_Object((1,3,6,1,4,1,351,110,5,1,2,3,1,1,28),_XmtBytesDiscXceedQDepth_Type())
xmtBytesDiscXceedQDepth.setMaxAccess(_C)
if mibBuilder.loadTexts:xmtBytesDiscXceedQDepth.setStatus(_A)
if mibBuilder.loadTexts:xmtBytesDiscXceedQDepth.setUnits(_E)
_XmtFramesDiscXceedDEThresh_Type=Counter32
_XmtFramesDiscXceedDEThresh_Object=MibTableColumn
xmtFramesDiscXceedDEThresh=_XmtFramesDiscXceedDEThresh_Object((1,3,6,1,4,1,351,110,5,1,2,3,1,1,29),_XmtFramesDiscXceedDEThresh_Type())
xmtFramesDiscXceedDEThresh.setMaxAccess(_C)
if mibBuilder.loadTexts:xmtFramesDiscXceedDEThresh.setStatus(_A)
if mibBuilder.loadTexts:xmtFramesDiscXceedDEThresh.setUnits(_D)
_XmtFramesDiscPhyLayerFail_Type=Counter32
_XmtFramesDiscPhyLayerFail_Object=MibTableColumn
xmtFramesDiscPhyLayerFail=_XmtFramesDiscPhyLayerFail_Object((1,3,6,1,4,1,351,110,5,1,2,3,1,1,30),_XmtFramesDiscPhyLayerFail_Type())
xmtFramesDiscPhyLayerFail.setMaxAccess(_C)
if mibBuilder.loadTexts:xmtFramesDiscPhyLayerFail.setStatus(_A)
if mibBuilder.loadTexts:xmtFramesDiscPhyLayerFail.setUnits(_D)
_XmtFramesDiscCRCError_Type=Counter32
_XmtFramesDiscCRCError_Object=MibTableColumn
xmtFramesDiscCRCError=_XmtFramesDiscCRCError_Object((1,3,6,1,4,1,351,110,5,1,2,3,1,1,31),_XmtFramesDiscCRCError_Type())
xmtFramesDiscCRCError.setMaxAccess(_C)
if mibBuilder.loadTexts:xmtFramesDiscCRCError.setStatus(_A)
if mibBuilder.loadTexts:xmtFramesDiscCRCError.setUnits(_D)
_XmtFramesDiscReassmFail_Type=Counter32
_XmtFramesDiscReassmFail_Object=MibTableColumn
xmtFramesDiscReassmFail=_XmtFramesDiscReassmFail_Object((1,3,6,1,4,1,351,110,5,1,2,3,1,1,32),_XmtFramesDiscReassmFail_Type())
xmtFramesDiscReassmFail.setMaxAccess(_C)
if mibBuilder.loadTexts:xmtFramesDiscReassmFail.setStatus(_A)
_XmtFramesDiscSrcAbort_Type=Counter32
_XmtFramesDiscSrcAbort_Object=MibTableColumn
xmtFramesDiscSrcAbort=_XmtFramesDiscSrcAbort_Object((1,3,6,1,4,1,351,110,5,1,2,3,1,1,33),_XmtFramesDiscSrcAbort_Type())
xmtFramesDiscSrcAbort.setMaxAccess(_C)
if mibBuilder.loadTexts:xmtFramesDiscSrcAbort.setStatus(_A)
_XmtFramesDuringLMIAlarm_Type=Counter32
_XmtFramesDuringLMIAlarm_Object=MibTableColumn
xmtFramesDuringLMIAlarm=_XmtFramesDuringLMIAlarm_Object((1,3,6,1,4,1,351,110,5,1,2,3,1,1,34),_XmtFramesDuringLMIAlarm_Type())
xmtFramesDuringLMIAlarm.setMaxAccess(_C)
if mibBuilder.loadTexts:xmtFramesDuringLMIAlarm.setStatus(_A)
_XmtBytesDuringLMIAlarm_Type=Counter32
_XmtBytesDuringLMIAlarm_Object=MibTableColumn
xmtBytesDuringLMIAlarm=_XmtBytesDuringLMIAlarm_Object((1,3,6,1,4,1,351,110,5,1,2,3,1,1,35),_XmtBytesDuringLMIAlarm_Type())
xmtBytesDuringLMIAlarm.setMaxAccess(_C)
if mibBuilder.loadTexts:xmtBytesDuringLMIAlarm.setStatus(_A)
_XmtFramesTaggedFECN_Type=Counter32
_XmtFramesTaggedFECN_Object=MibTableColumn
xmtFramesTaggedFECN=_XmtFramesTaggedFECN_Object((1,3,6,1,4,1,351,110,5,1,2,3,1,1,36),_XmtFramesTaggedFECN_Type())
xmtFramesTaggedFECN.setMaxAccess(_C)
if mibBuilder.loadTexts:xmtFramesTaggedFECN.setStatus(_A)
_XmtFramesTaggedBECN_Type=Counter32
_XmtFramesTaggedBECN_Object=MibTableColumn
xmtFramesTaggedBECN=_XmtFramesTaggedBECN_Object((1,3,6,1,4,1,351,110,5,1,2,3,1,1,37),_XmtFramesTaggedBECN_Type())
xmtFramesTaggedBECN.setMaxAccess(_C)
if mibBuilder.loadTexts:xmtFramesTaggedBECN.setStatus(_A)
if mibBuilder.loadTexts:xmtFramesTaggedBECN.setUnits(_D)
_XmtKbpsAIR_Type=Integer32
_XmtKbpsAIR_Object=MibTableColumn
xmtKbpsAIR=_XmtKbpsAIR_Object((1,3,6,1,4,1,351,110,5,1,2,3,1,1,38),_XmtKbpsAIR_Type())
xmtKbpsAIR.setMaxAccess(_C)
if mibBuilder.loadTexts:xmtKbpsAIR.setStatus(_A)
if mibBuilder.loadTexts:xmtKbpsAIR.setUnits('kbps')
class _ChanClrButton_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('noaction',1),('clear',2)))
_ChanClrButton_Type.__name__=_F
_ChanClrButton_Object=MibTableColumn
chanClrButton=_ChanClrButton_Object((1,3,6,1,4,1,351,110,5,1,2,3,1,1,39),_ChanClrButton_Type())
chanClrButton.setMaxAccess('read-write')
if mibBuilder.loadTexts:chanClrButton.setStatus(_A)
_XmtFramesTaggedDE_Type=Counter32
_XmtFramesTaggedDE_Object=MibTableColumn
xmtFramesTaggedDE=_XmtFramesTaggedDE_Object((1,3,6,1,4,1,351,110,5,1,2,3,1,1,40),_XmtFramesTaggedDE_Type())
xmtFramesTaggedDE.setMaxAccess(_C)
if mibBuilder.loadTexts:xmtFramesTaggedDE.setStatus(_A)
if mibBuilder.loadTexts:xmtFramesTaggedDE.setUnits(_D)
_XmtBytesTaggedDE_Type=Counter32
_XmtBytesTaggedDE_Object=MibTableColumn
xmtBytesTaggedDE=_XmtBytesTaggedDE_Object((1,3,6,1,4,1,351,110,5,1,2,3,1,1,41),_XmtBytesTaggedDE_Type())
xmtBytesTaggedDE.setMaxAccess(_C)
if mibBuilder.loadTexts:xmtBytesTaggedDE.setStatus(_A)
if mibBuilder.loadTexts:xmtBytesTaggedDE.setUnits(_E)
_RcvFramesDiscUPC_Type=Counter32
_RcvFramesDiscUPC_Object=MibTableColumn
rcvFramesDiscUPC=_RcvFramesDiscUPC_Object((1,3,6,1,4,1,351,110,5,1,2,3,1,1,42),_RcvFramesDiscUPC_Type())
rcvFramesDiscUPC.setMaxAccess(_C)
if mibBuilder.loadTexts:rcvFramesDiscUPC.setStatus(_A)
if mibBuilder.loadTexts:rcvFramesDiscUPC.setUnits(_D)
_ChanSecUpTime_Type=Counter32
_ChanSecUpTime_Object=MibTableColumn
chanSecUpTime=_ChanSecUpTime_Object((1,3,6,1,4,1,351,110,5,1,2,3,1,1,43),_ChanSecUpTime_Type())
chanSecUpTime.setMaxAccess(_C)
if mibBuilder.loadTexts:chanSecUpTime.setStatus(_A)
if mibBuilder.loadTexts:chanSecUpTime.setUnits('seconds')
_XmtFramesInvalidCPIs_Type=Counter32
_XmtFramesInvalidCPIs_Object=MibTableColumn
xmtFramesInvalidCPIs=_XmtFramesInvalidCPIs_Object((1,3,6,1,4,1,351,110,5,1,2,3,1,1,44),_XmtFramesInvalidCPIs_Type())
xmtFramesInvalidCPIs.setMaxAccess(_C)
if mibBuilder.loadTexts:xmtFramesInvalidCPIs.setStatus(_A)
if mibBuilder.loadTexts:xmtFramesInvalidCPIs.setUnits(_D)
_XmtFramesLengthViolations_Type=Counter32
_XmtFramesLengthViolations_Object=MibTableColumn
xmtFramesLengthViolations=_XmtFramesLengthViolations_Object((1,3,6,1,4,1,351,110,5,1,2,3,1,1,45),_XmtFramesLengthViolations_Type())
xmtFramesLengthViolations.setMaxAccess(_C)
if mibBuilder.loadTexts:xmtFramesLengthViolations.setStatus(_A)
if mibBuilder.loadTexts:xmtFramesLengthViolations.setUnits(_D)
_XmtFramesOversizedSDUs_Type=Counter32
_XmtFramesOversizedSDUs_Object=MibTableColumn
xmtFramesOversizedSDUs=_XmtFramesOversizedSDUs_Object((1,3,6,1,4,1,351,110,5,1,2,3,1,1,46),_XmtFramesOversizedSDUs_Type())
xmtFramesOversizedSDUs.setMaxAccess(_C)
if mibBuilder.loadTexts:xmtFramesOversizedSDUs.setStatus(_A)
if mibBuilder.loadTexts:xmtFramesOversizedSDUs.setUnits(_D)
_XmtFramesUnknownProtocols_Type=Counter32
_XmtFramesUnknownProtocols_Object=MibTableColumn
xmtFramesUnknownProtocols=_XmtFramesUnknownProtocols_Object((1,3,6,1,4,1,351,110,5,1,2,3,1,1,47),_XmtFramesUnknownProtocols_Type())
xmtFramesUnknownProtocols.setMaxAccess(_C)
if mibBuilder.loadTexts:xmtFramesUnknownProtocols.setStatus(_A)
_RcvFramesUnknownProtocols_Type=Counter32
_RcvFramesUnknownProtocols_Object=MibTableColumn
rcvFramesUnknownProtocols=_RcvFramesUnknownProtocols_Object((1,3,6,1,4,1,351,110,5,1,2,3,1,1,48),_RcvFramesUnknownProtocols_Type())
rcvFramesUnknownProtocols.setMaxAccess(_C)
if mibBuilder.loadTexts:rcvFramesUnknownProtocols.setStatus(_A)
if mibBuilder.loadTexts:rcvFramesUnknownProtocols.setUnits(_D)
_XmtBytesDEDiscard_Type=Counter32
_XmtBytesDEDiscard_Object=MibTableColumn
xmtBytesDEDiscard=_XmtBytesDEDiscard_Object((1,3,6,1,4,1,351,110,5,1,2,3,1,1,49),_XmtBytesDEDiscard_Type())
xmtBytesDEDiscard.setMaxAccess(_C)
if mibBuilder.loadTexts:xmtBytesDEDiscard.setStatus(_A)
if mibBuilder.loadTexts:xmtBytesDEDiscard.setUnits(_E)
_RcvBytesDEDiscard_Type=Counter32
_RcvBytesDEDiscard_Object=MibTableColumn
rcvBytesDEDiscard=_RcvBytesDEDiscard_Object((1,3,6,1,4,1,351,110,5,1,2,3,1,1,50),_RcvBytesDEDiscard_Type())
rcvBytesDEDiscard.setMaxAccess(_C)
if mibBuilder.loadTexts:rcvBytesDEDiscard.setStatus(_A)
if mibBuilder.loadTexts:rcvBytesDEDiscard.setUnits(_E)
_FrstdABRCntGrpTable_Object=MibTable
frstdABRCntGrpTable=_FrstdABRCntGrpTable_Object((1,3,6,1,4,1,351,110,5,1,2,3,2))
if mibBuilder.loadTexts:frstdABRCntGrpTable.setStatus(_A)
_FrstdABRCntGrpEntry_Object=MibTableRow
frstdABRCntGrpEntry=_FrstdABRCntGrpEntry_Object((1,3,6,1,4,1,351,110,5,1,2,3,2,1))
frstdABRCntGrpEntry.setIndexNames((0,_B,_H))
if mibBuilder.loadTexts:frstdABRCntGrpEntry.setStatus(_A)
class _FrstdABRcntChanNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_FrstdABRcntChanNum_Type.__name__=_F
_FrstdABRcntChanNum_Object=MibTableColumn
frstdABRcntChanNum=_FrstdABRcntChanNum_Object((1,3,6,1,4,1,351,110,5,1,2,3,2,1,1),_FrstdABRcntChanNum_Type())
frstdABRcntChanNum.setMaxAccess(_C)
if mibBuilder.loadTexts:frstdABRcntChanNum.setStatus(_A)
_FrChanFrmXmtToNetworkCnt_Type=Counter32
_FrChanFrmXmtToNetworkCnt_Object=MibTableColumn
frChanFrmXmtToNetworkCnt=_FrChanFrmXmtToNetworkCnt_Object((1,3,6,1,4,1,351,110,5,1,2,3,2,1,2),_FrChanFrmXmtToNetworkCnt_Type())
frChanFrmXmtToNetworkCnt.setMaxAccess(_C)
if mibBuilder.loadTexts:frChanFrmXmtToNetworkCnt.setStatus(_A)
_FrChanBrmXmtToNetworkCnt_Type=Counter32
_FrChanBrmXmtToNetworkCnt_Object=MibTableColumn
frChanBrmXmtToNetworkCnt=_FrChanBrmXmtToNetworkCnt_Object((1,3,6,1,4,1,351,110,5,1,2,3,2,1,3),_FrChanBrmXmtToNetworkCnt_Type())
frChanBrmXmtToNetworkCnt.setMaxAccess(_C)
if mibBuilder.loadTexts:frChanBrmXmtToNetworkCnt.setStatus(_A)
_FrChanCrcErrRmRcvFromNetworkCnt_Type=Counter32
_FrChanCrcErrRmRcvFromNetworkCnt_Object=MibTableColumn
frChanCrcErrRmRcvFromNetworkCnt=_FrChanCrcErrRmRcvFromNetworkCnt_Object((1,3,6,1,4,1,351,110,5,1,2,3,2,1,4),_FrChanCrcErrRmRcvFromNetworkCnt_Type())
frChanCrcErrRmRcvFromNetworkCnt.setMaxAccess(_C)
if mibBuilder.loadTexts:frChanCrcErrRmRcvFromNetworkCnt.setStatus(_A)
_FrChanFrmRcvFromNetworkCnt_Type=Counter32
_FrChanFrmRcvFromNetworkCnt_Object=MibTableColumn
frChanFrmRcvFromNetworkCnt=_FrChanFrmRcvFromNetworkCnt_Object((1,3,6,1,4,1,351,110,5,1,2,3,2,1,5),_FrChanFrmRcvFromNetworkCnt_Type())
frChanFrmRcvFromNetworkCnt.setMaxAccess(_C)
if mibBuilder.loadTexts:frChanFrmRcvFromNetworkCnt.setStatus(_A)
_FrChanBrmRcvFromNetworkCnt_Type=Counter32
_FrChanBrmRcvFromNetworkCnt_Object=MibTableColumn
frChanBrmRcvFromNetworkCnt=_FrChanBrmRcvFromNetworkCnt_Object((1,3,6,1,4,1,351,110,5,1,2,3,2,1,6),_FrChanBrmRcvFromNetworkCnt_Type())
frChanBrmRcvFromNetworkCnt.setMaxAccess(_C)
if mibBuilder.loadTexts:frChanBrmRcvFromNetworkCnt.setStatus(_A)
_FrChanFrmNotTurnedAroundCnt_Type=Counter32
_FrChanFrmNotTurnedAroundCnt_Object=MibTableColumn
frChanFrmNotTurnedAroundCnt=_FrChanFrmNotTurnedAroundCnt_Object((1,3,6,1,4,1,351,110,5,1,2,3,2,1,7),_FrChanFrmNotTurnedAroundCnt_Type())
frChanFrmNotTurnedAroundCnt.setMaxAccess(_C)
if mibBuilder.loadTexts:frChanFrmNotTurnedAroundCnt.setStatus(_A)
_CwfConnStatMIBConformance_ObjectIdentity=ObjectIdentity
cwfConnStatMIBConformance=_CwfConnStatMIBConformance_ObjectIdentity((1,3,6,1,4,1,351,150,48,2))
_CwfConnStatMIBGroups_ObjectIdentity=ObjectIdentity
cwfConnStatMIBGroups=_CwfConnStatMIBGroups_ObjectIdentity((1,3,6,1,4,1,351,150,48,2,1))
_CwfConnStatMIBCompliances_ObjectIdentity=ObjectIdentity
cwfConnStatMIBCompliances=_CwfConnStatMIBCompliances_ObjectIdentity((1,3,6,1,4,1,351,150,48,2,2))
ciscoWanFrConnStatsGroup=ObjectGroup((1,3,6,1,4,1,351,150,48,2,1,1))
ciscoWanFrConnStatsGroup.setObjects(*((_B,_G),(_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_x),(_B,_y)))
if mibBuilder.loadTexts:ciscoWanFrConnStatsGroup.setStatus(_A)
ciscoWanFrConnQueueStatsGroup=ObjectGroup((1,3,6,1,4,1,351,150,48,2,1,2))
ciscoWanFrConnQueueStatsGroup.setObjects(*((_B,_z),(_B,_A0),(_B,_A1),(_B,_A2),(_B,_A3),(_B,_A4)))
if mibBuilder.loadTexts:ciscoWanFrConnQueueStatsGroup.setStatus(_A)
ciscoWanFrConnABRStatsGroup=ObjectGroup((1,3,6,1,4,1,351,150,48,2,1,3))
ciscoWanFrConnABRStatsGroup.setObjects(*((_B,_H),(_B,_A5),(_B,_A6),(_B,_A7),(_B,_A8),(_B,_A9),(_B,_AA)))
if mibBuilder.loadTexts:ciscoWanFrConnABRStatsGroup.setStatus(_A)
ciscoWanFrConnStatCompliance=ModuleCompliance((1,3,6,1,4,1,351,150,48,2,2,1))
ciscoWanFrConnStatCompliance.setObjects(*((_B,_AB),(_B,_AC),(_B,_AD)))
if mibBuilder.loadTexts:ciscoWanFrConnStatCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'frChanCntGrp':frChanCntGrp,'frChanCntGrpTable':frChanCntGrpTable,'frChanCntGrpEntry':frChanCntGrpEntry,_G:cntChanNum,_I:rcvFrames,_J:rcvBytes,_K:rcvFramesDE,_L:rcvBytesDE,_M:rcvFramesDiscard,_N:rcvBytesDiscard,_O:rcvFramesDiscShelfAlarm,_z:rcvFramesDiscXceedQDepth,_A0:rcvBytesDiscXceedQDepth,_A1:rcvFramesDiscXceedDEThresh,_P:rcvFramesFECN,_Q:rcvFramesBECN,_R:rcvFramesTaggedFECN,_S:rcvFramesTaggedBECN,_T:rcvFramesTaggedDE,_U:rcvBytesTaggedDE,_V:rcvKbpsAIR,_W:xmtFrames,_X:xmtBytes,_Y:xmtFramesFECN,_Z:xmtFramesBECN,_a:xmtFramesDE,_b:xmtBytesDE,_c:xmtFramesDiscard,_d:xmtBytesDiscard,_A2:xmtFramesDiscXceedQDepth,_A3:xmtBytesDiscXceedQDepth,_A4:xmtFramesDiscXceedDEThresh,_e:xmtFramesDiscPhyLayerFail,_f:xmtFramesDiscCRCError,_g:xmtFramesDiscReassmFail,_h:xmtFramesDiscSrcAbort,_i:xmtFramesDuringLMIAlarm,_j:xmtBytesDuringLMIAlarm,_k:xmtFramesTaggedFECN,_l:xmtFramesTaggedBECN,_m:xmtKbpsAIR,_n:chanClrButton,_r:xmtFramesTaggedDE,_q:xmtBytesTaggedDE,_p:rcvFramesDiscUPC,_o:chanSecUpTime,_s:xmtFramesInvalidCPIs,_t:xmtFramesLengthViolations,_u:xmtFramesOversizedSDUs,_v:xmtFramesUnknownProtocols,_w:rcvFramesUnknownProtocols,_x:xmtBytesDEDiscard,_y:rcvBytesDEDiscard,'frstdABRCntGrpTable':frstdABRCntGrpTable,'frstdABRCntGrpEntry':frstdABRCntGrpEntry,_H:frstdABRcntChanNum,_A5:frChanFrmXmtToNetworkCnt,_A6:frChanBrmXmtToNetworkCnt,_A7:frChanCrcErrRmRcvFromNetworkCnt,_A8:frChanFrmRcvFromNetworkCnt,_A9:frChanBrmRcvFromNetworkCnt,_AA:frChanFrmNotTurnedAroundCnt,'ciscoWanFrConnStatMIB':ciscoWanFrConnStatMIB,'cwfConnStatMIBConformance':cwfConnStatMIBConformance,'cwfConnStatMIBGroups':cwfConnStatMIBGroups,_AB:ciscoWanFrConnStatsGroup,_AD:ciscoWanFrConnQueueStatsGroup,_AC:ciscoWanFrConnABRStatsGroup,'cwfConnStatMIBCompliances':cwfConnStatMIBCompliances,'ciscoWanFrConnStatCompliance':ciscoWanFrConnStatCompliance})