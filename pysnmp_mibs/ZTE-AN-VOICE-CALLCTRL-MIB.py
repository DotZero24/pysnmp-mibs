_S='zxAnCallEscapePriDLinkTimeslot'
_R='zxAnCallEscapePort'
_Q='zxAnCallOptIndex'
_P='zxAnCallEscapeDsx1LinkNo'
_O='notsend'
_N='send'
_M='DisplayString'
_L='zxAnCallEscapeSlot'
_K='zxAnCallEscapeShelf'
_J='zxAnCallEscapeRack'
_I='notalways'
_H='alwayssend'
_G='not-accessible'
_F='read-create'
_E='read-write'
_D='ZTE-AN-VOICE-CALLCTRL-MIB'
_C='read-only'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DateAndTime,DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime',_M,'MacAddress','PhysAddress','RowStatus','TextualConvention','TruthValue')
zxAnVoiceCallCtrlMib=ModuleIdentity((1,3,6,1,4,1,3902,1015,5200))
_Zte_ObjectIdentity=ObjectIdentity
zte=_Zte_ObjectIdentity((1,3,6,1,4,1,3902))
_ZxAn_ObjectIdentity=ObjectIdentity
zxAn=_ZxAn_ObjectIdentity((1,3,6,1,4,1,3902,1015))
_ZxAnVoiceMgmt_ObjectIdentity=ObjectIdentity
zxAnVoiceMgmt=_ZxAnVoiceMgmt_ObjectIdentity((1,3,6,1,4,1,3902,1015,5200,3))
_ZxAnVoipCallCtrl_ObjectIdentity=ObjectIdentity
zxAnVoipCallCtrl=_ZxAnVoipCallCtrl_ObjectIdentity((1,3,6,1,4,1,3902,1015,5200,3,6))
_MsagCallResStatistic_ObjectIdentity=ObjectIdentity
msagCallResStatistic=_MsagCallResStatistic_ObjectIdentity((1,3,6,1,4,1,3902,1015,5200,3,6,5))
class _MsagCRAccessRatio_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,10))
_MsagCRAccessRatio_Type.__name__=_M
_MsagCRAccessRatio_Object=MibScalar
msagCRAccessRatio=_MsagCRAccessRatio_Object((1,3,6,1,4,1,3902,1015,5200,3,6,5,1),_MsagCRAccessRatio_Type())
msagCRAccessRatio.setMaxAccess(_C)
if mibBuilder.loadTexts:msagCRAccessRatio.setStatus(_A)
class _MsagCRIPSUsingRatio_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,10))
_MsagCRIPSUsingRatio_Type.__name__=_M
_MsagCRIPSUsingRatio_Object=MibScalar
msagCRIPSUsingRatio=_MsagCRIPSUsingRatio_Object((1,3,6,1,4,1,3902,1015,5200,3,6,5,2),_MsagCRIPSUsingRatio_Type())
msagCRIPSUsingRatio.setMaxAccess(_C)
if mibBuilder.loadTexts:msagCRIPSUsingRatio.setStatus(_A)
_MsagCROpenChannelReq_Type=Integer32
_MsagCROpenChannelReq_Object=MibScalar
msagCROpenChannelReq=_MsagCROpenChannelReq_Object((1,3,6,1,4,1,3902,1015,5200,3,6,5,3),_MsagCROpenChannelReq_Type())
msagCROpenChannelReq.setMaxAccess(_C)
if mibBuilder.loadTexts:msagCROpenChannelReq.setStatus(_A)
_MsagCRRecOpenSucces_Type=Integer32
_MsagCRRecOpenSucces_Object=MibScalar
msagCRRecOpenSucces=_MsagCRRecOpenSucces_Object((1,3,6,1,4,1,3902,1015,5200,3,6,5,4),_MsagCRRecOpenSucces_Type())
msagCRRecOpenSucces.setMaxAccess(_C)
if mibBuilder.loadTexts:msagCRRecOpenSucces.setStatus(_A)
_MsagCRRecOpenFail_Type=Integer32
_MsagCRRecOpenFail_Object=MibScalar
msagCRRecOpenFail=_MsagCRRecOpenFail_Object((1,3,6,1,4,1,3902,1015,5200,3,6,5,5),_MsagCRRecOpenFail_Type())
msagCRRecOpenFail.setMaxAccess(_C)
if mibBuilder.loadTexts:msagCRRecOpenFail.setStatus(_A)
_MsagCROpenChannTimerOut_Type=Integer32
_MsagCROpenChannTimerOut_Object=MibScalar
msagCROpenChannTimerOut=_MsagCROpenChannTimerOut_Object((1,3,6,1,4,1,3902,1015,5200,3,6,5,6),_MsagCROpenChannTimerOut_Type())
msagCROpenChannTimerOut.setMaxAccess(_C)
if mibBuilder.loadTexts:msagCROpenChannTimerOut.setStatus(_A)
_MsagCRModifyChannel_Type=Integer32
_MsagCRModifyChannel_Object=MibScalar
msagCRModifyChannel=_MsagCRModifyChannel_Object((1,3,6,1,4,1,3902,1015,5200,3,6,5,7),_MsagCRModifyChannel_Type())
msagCRModifyChannel.setMaxAccess(_C)
if mibBuilder.loadTexts:msagCRModifyChannel.setStatus(_A)
_MsagCRRecModifySucces_Type=Integer32
_MsagCRRecModifySucces_Object=MibScalar
msagCRRecModifySucces=_MsagCRRecModifySucces_Object((1,3,6,1,4,1,3902,1015,5200,3,6,5,8),_MsagCRRecModifySucces_Type())
msagCRRecModifySucces.setMaxAccess(_C)
if mibBuilder.loadTexts:msagCRRecModifySucces.setStatus(_A)
_MsagCRModifyChFail_Type=Integer32
_MsagCRModifyChFail_Object=MibScalar
msagCRModifyChFail=_MsagCRModifyChFail_Object((1,3,6,1,4,1,3902,1015,5200,3,6,5,9),_MsagCRModifyChFail_Type())
msagCRModifyChFail.setMaxAccess(_C)
if mibBuilder.loadTexts:msagCRModifyChFail.setStatus(_A)
_MsagCRWtModifyChannTimerOut_Type=Integer32
_MsagCRWtModifyChannTimerOut_Object=MibScalar
msagCRWtModifyChannTimerOut=_MsagCRWtModifyChannTimerOut_Object((1,3,6,1,4,1,3902,1015,5200,3,6,5,10),_MsagCRWtModifyChannTimerOut_Type())
msagCRWtModifyChannTimerOut.setMaxAccess(_C)
if mibBuilder.loadTexts:msagCRWtModifyChannTimerOut.setStatus(_A)
_MsagCRSendCloseChannel_Type=Integer32
_MsagCRSendCloseChannel_Object=MibScalar
msagCRSendCloseChannel=_MsagCRSendCloseChannel_Object((1,3,6,1,4,1,3902,1015,5200,3,6,5,11),_MsagCRSendCloseChannel_Type())
msagCRSendCloseChannel.setMaxAccess(_C)
if mibBuilder.loadTexts:msagCRSendCloseChannel.setStatus(_A)
_MsagCRRecCloseChanSucc_Type=Integer32
_MsagCRRecCloseChanSucc_Object=MibScalar
msagCRRecCloseChanSucc=_MsagCRRecCloseChanSucc_Object((1,3,6,1,4,1,3902,1015,5200,3,6,5,12),_MsagCRRecCloseChanSucc_Type())
msagCRRecCloseChanSucc.setMaxAccess(_C)
if mibBuilder.loadTexts:msagCRRecCloseChanSucc.setStatus(_A)
_MsagCRRecCloseChanFail_Type=Integer32
_MsagCRRecCloseChanFail_Object=MibScalar
msagCRRecCloseChanFail=_MsagCRRecCloseChanFail_Object((1,3,6,1,4,1,3902,1015,5200,3,6,5,13),_MsagCRRecCloseChanFail_Type())
msagCRRecCloseChanFail.setMaxAccess(_C)
if mibBuilder.loadTexts:msagCRRecCloseChanFail.setStatus(_A)
_MsagCRRecCloseChanTimerOut_Type=Integer32
_MsagCRRecCloseChanTimerOut_Object=MibScalar
msagCRRecCloseChanTimerOut=_MsagCRRecCloseChanTimerOut_Object((1,3,6,1,4,1,3902,1015,5200,3,6,5,14),_MsagCRRecCloseChanTimerOut_Type())
msagCRRecCloseChanTimerOut.setMaxAccess(_C)
if mibBuilder.loadTexts:msagCRRecCloseChanTimerOut.setStatus(_A)
_MsagCRRecMprReload_Type=Integer32
_MsagCRRecMprReload_Object=MibScalar
msagCRRecMprReload=_MsagCRRecMprReload_Object((1,3,6,1,4,1,3902,1015,5200,3,6,5,15),_MsagCRRecMprReload_Type())
msagCRRecMprReload.setMaxAccess(_C)
if mibBuilder.loadTexts:msagCRRecMprReload.setStatus(_A)
class _MsagCRClearRTPRecord_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1))
_MsagCRClearRTPRecord_Type.__name__=_B
_MsagCRClearRTPRecord_Object=MibScalar
msagCRClearRTPRecord=_MsagCRClearRTPRecord_Object((1,3,6,1,4,1,3902,1015,5200,3,6,5,16),_MsagCRClearRTPRecord_Type())
msagCRClearRTPRecord.setMaxAccess(_E)
if mibBuilder.loadTexts:msagCRClearRTPRecord.setStatus(_A)
_ZxAnVoipCallCtrlGlobalObjects_ObjectIdentity=ObjectIdentity
zxAnVoipCallCtrlGlobalObjects=_ZxAnVoipCallCtrlGlobalObjects_ObjectIdentity((1,3,6,1,4,1,3902,1015,5200,3,6,1300))
class _ZxAnVoipCallCtrlMgmtCapabilities_Type(Bits):namedValues=NamedValues(('nbPlatform',0))
_ZxAnVoipCallCtrlMgmtCapabilities_Type.__name__='Bits'
_ZxAnVoipCallCtrlMgmtCapabilities_Object=MibScalar
zxAnVoipCallCtrlMgmtCapabilities=_ZxAnVoipCallCtrlMgmtCapabilities_Object((1,3,6,1,4,1,3902,1015,5200,3,6,1300,1),_ZxAnVoipCallCtrlMgmtCapabilities_Type())
zxAnVoipCallCtrlMgmtCapabilities.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnVoipCallCtrlMgmtCapabilities.setStatus(_A)
_ZxAnCallOptimizationTable_Object=MibTable
zxAnCallOptimizationTable=_ZxAnCallOptimizationTable_Object((1,3,6,1,4,1,3902,1015,5200,3,6,1301))
if mibBuilder.loadTexts:zxAnCallOptimizationTable.setStatus(_A)
_ZxAnCallOptimizationEntry_Object=MibTableRow
zxAnCallOptimizationEntry=_ZxAnCallOptimizationEntry_Object((1,3,6,1,4,1,3902,1015,5200,3,6,1301,1))
zxAnCallOptimizationEntry.setIndexNames((0,_D,_Q))
if mibBuilder.loadTexts:zxAnCallOptimizationEntry.setStatus(_A)
class _ZxAnCallOptIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1))
_ZxAnCallOptIndex_Type.__name__=_B
_ZxAnCallOptIndex_Object=MibTableColumn
zxAnCallOptIndex=_ZxAnCallOptIndex_Object((1,3,6,1,4,1,3902,1015,5200,3,6,1301,1,1),_ZxAnCallOptIndex_Type())
zxAnCallOptIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnCallOptIndex.setStatus(_A)
class _ZxAnCallOptOpenMsgAck_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_N,1),(_O,2)))
_ZxAnCallOptOpenMsgAck_Type.__name__=_B
_ZxAnCallOptOpenMsgAck_Object=MibTableColumn
zxAnCallOptOpenMsgAck=_ZxAnCallOptOpenMsgAck_Object((1,3,6,1,4,1,3902,1015,5200,3,6,1301,1,2),_ZxAnCallOptOpenMsgAck_Type())
zxAnCallOptOpenMsgAck.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnCallOptOpenMsgAck.setStatus(_A)
class _ZxAnCallOptPlayToneAck_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_N,1),(_O,2)))
_ZxAnCallOptPlayToneAck_Type.__name__=_B
_ZxAnCallOptPlayToneAck_Object=MibTableColumn
zxAnCallOptPlayToneAck=_ZxAnCallOptPlayToneAck_Object((1,3,6,1,4,1,3902,1015,5200,3,6,1301,1,3),_ZxAnCallOptPlayToneAck_Type())
zxAnCallOptPlayToneAck.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnCallOptPlayToneAck.setStatus(_A)
class _ZxAnCallOptSubPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('higher',1),('nothigher',2)))
_ZxAnCallOptSubPriority_Type.__name__=_B
_ZxAnCallOptSubPriority_Object=MibTableColumn
zxAnCallOptSubPriority=_ZxAnCallOptSubPriority_Object((1,3,6,1,4,1,3902,1015,5200,3,6,1301,1,4),_ZxAnCallOptSubPriority_Type())
zxAnCallOptSubPriority.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnCallOptSubPriority.setStatus(_A)
class _ZxAnCallOptH248Statistic_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_N,1),(_O,2)))
_ZxAnCallOptH248Statistic_Type.__name__=_B
_ZxAnCallOptH248Statistic_Object=MibTableColumn
zxAnCallOptH248Statistic=_ZxAnCallOptH248Statistic_Object((1,3,6,1,4,1,3902,1015,5200,3,6,1301,1,8),_ZxAnCallOptH248Statistic_Type())
zxAnCallOptH248Statistic.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnCallOptH248Statistic.setStatus(_A)
class _ZxAnCallOptServiceAbnormal_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_ZxAnCallOptServiceAbnormal_Type.__name__=_B
_ZxAnCallOptServiceAbnormal_Object=MibTableColumn
zxAnCallOptServiceAbnormal=_ZxAnCallOptServiceAbnormal_Object((1,3,6,1,4,1,3902,1015,5200,3,6,1301,1,11),_ZxAnCallOptServiceAbnormal_Type())
zxAnCallOptServiceAbnormal.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnCallOptServiceAbnormal.setStatus(_A)
class _ZxAnCallOptMgProtocolErr_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_ZxAnCallOptMgProtocolErr_Type.__name__=_B
_ZxAnCallOptMgProtocolErr_Object=MibTableColumn
zxAnCallOptMgProtocolErr=_ZxAnCallOptMgProtocolErr_Object((1,3,6,1,4,1,3902,1015,5200,3,6,1301,1,12),_ZxAnCallOptMgProtocolErr_Type())
zxAnCallOptMgProtocolErr.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnCallOptMgProtocolErr.setStatus(_A)
class _ZxAnCallOptMgcProtocolErr_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_ZxAnCallOptMgcProtocolErr_Type.__name__=_B
_ZxAnCallOptMgcProtocolErr_Object=MibTableColumn
zxAnCallOptMgcProtocolErr=_ZxAnCallOptMgcProtocolErr_Object((1,3,6,1,4,1,3902,1015,5200,3,6,1301,1,13),_ZxAnCallOptMgcProtocolErr_Type())
zxAnCallOptMgcProtocolErr.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnCallOptMgcProtocolErr.setStatus(_A)
class _ZxAnCallOptMgInsideErr_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_ZxAnCallOptMgInsideErr_Type.__name__=_B
_ZxAnCallOptMgInsideErr_Object=MibTableColumn
zxAnCallOptMgInsideErr=_ZxAnCallOptMgInsideErr_Object((1,3,6,1,4,1,3902,1015,5200,3,6,1301,1,14),_ZxAnCallOptMgInsideErr_Type())
zxAnCallOptMgInsideErr.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnCallOptMgInsideErr.setStatus(_A)
class _ZxAnCallOptCallLimit_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('limitByMg',1),('limitByMgc',2),('noLimit',3)))
_ZxAnCallOptCallLimit_Type.__name__=_B
_ZxAnCallOptCallLimit_Object=MibTableColumn
zxAnCallOptCallLimit=_ZxAnCallOptCallLimit_Object((1,3,6,1,4,1,3902,1015,5200,3,6,1301,1,15),_ZxAnCallOptCallLimit_Type())
zxAnCallOptCallLimit.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnCallOptCallLimit.setStatus(_A)
class _ZxAnCallOptCallLimitMaxUserNum_Type(Integer32):defaultValue=128;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_ZxAnCallOptCallLimitMaxUserNum_Type.__name__=_B
_ZxAnCallOptCallLimitMaxUserNum_Object=MibTableColumn
zxAnCallOptCallLimitMaxUserNum=_ZxAnCallOptCallLimitMaxUserNum_Object((1,3,6,1,4,1,3902,1015,5200,3,6,1301,1,16),_ZxAnCallOptCallLimitMaxUserNum_Type())
zxAnCallOptCallLimitMaxUserNum.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnCallOptCallLimitMaxUserNum.setStatus(_A)
_ZxAnCallEscapeObjects_ObjectIdentity=ObjectIdentity
zxAnCallEscapeObjects=_ZxAnCallEscapeObjects_ObjectIdentity((1,3,6,1,4,1,3902,1015,5200,3,6,1302))
_ZxAnCallEscapeFxoTable_Object=MibTable
zxAnCallEscapeFxoTable=_ZxAnCallEscapeFxoTable_Object((1,3,6,1,4,1,3902,1015,5200,3,6,1302,2))
if mibBuilder.loadTexts:zxAnCallEscapeFxoTable.setStatus(_A)
_ZxAnCallEscapeFxoEntry_Object=MibTableRow
zxAnCallEscapeFxoEntry=_ZxAnCallEscapeFxoEntry_Object((1,3,6,1,4,1,3902,1015,5200,3,6,1302,2,1))
zxAnCallEscapeFxoEntry.setIndexNames((0,_D,_J),(0,_D,_K),(0,_D,_L),(0,_D,_R))
if mibBuilder.loadTexts:zxAnCallEscapeFxoEntry.setStatus(_A)
_ZxAnCallEscapeRack_Type=Integer32
_ZxAnCallEscapeRack_Object=MibTableColumn
zxAnCallEscapeRack=_ZxAnCallEscapeRack_Object((1,3,6,1,4,1,3902,1015,5200,3,6,1302,2,1,1),_ZxAnCallEscapeRack_Type())
zxAnCallEscapeRack.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnCallEscapeRack.setStatus(_A)
_ZxAnCallEscapeShelf_Type=Integer32
_ZxAnCallEscapeShelf_Object=MibTableColumn
zxAnCallEscapeShelf=_ZxAnCallEscapeShelf_Object((1,3,6,1,4,1,3902,1015,5200,3,6,1302,2,1,2),_ZxAnCallEscapeShelf_Type())
zxAnCallEscapeShelf.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnCallEscapeShelf.setStatus(_A)
_ZxAnCallEscapeSlot_Type=Integer32
_ZxAnCallEscapeSlot_Object=MibTableColumn
zxAnCallEscapeSlot=_ZxAnCallEscapeSlot_Object((1,3,6,1,4,1,3902,1015,5200,3,6,1302,2,1,3),_ZxAnCallEscapeSlot_Type())
zxAnCallEscapeSlot.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnCallEscapeSlot.setStatus(_A)
_ZxAnCallEscapePort_Type=Integer32
_ZxAnCallEscapePort_Object=MibTableColumn
zxAnCallEscapePort=_ZxAnCallEscapePort_Object((1,3,6,1,4,1,3902,1015,5200,3,6,1302,2,1,4),_ZxAnCallEscapePort_Type())
zxAnCallEscapePort.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnCallEscapePort.setStatus(_A)
_ZxAnCallEscapeFxoOperNum_Type=Integer32
_ZxAnCallEscapeFxoOperNum_Object=MibTableColumn
zxAnCallEscapeFxoOperNum=_ZxAnCallEscapeFxoOperNum_Object((1,3,6,1,4,1,3902,1015,5200,3,6,1302,2,1,5),_ZxAnCallEscapeFxoOperNum_Type())
zxAnCallEscapeFxoOperNum.setMaxAccess(_F)
if mibBuilder.loadTexts:zxAnCallEscapeFxoOperNum.setStatus(_A)
_ZxAnCallEscapeFxoRowStatus_Type=RowStatus
_ZxAnCallEscapeFxoRowStatus_Object=MibTableColumn
zxAnCallEscapeFxoRowStatus=_ZxAnCallEscapeFxoRowStatus_Object((1,3,6,1,4,1,3902,1015,5200,3,6,1302,2,1,50),_ZxAnCallEscapeFxoRowStatus_Type())
zxAnCallEscapeFxoRowStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:zxAnCallEscapeFxoRowStatus.setStatus(_A)
_ZxAnCallEscapePriTable_Object=MibTable
zxAnCallEscapePriTable=_ZxAnCallEscapePriTable_Object((1,3,6,1,4,1,3902,1015,5200,3,6,1302,3))
if mibBuilder.loadTexts:zxAnCallEscapePriTable.setStatus(_A)
_ZxAnCallEscapePriEntry_Object=MibTableRow
zxAnCallEscapePriEntry=_ZxAnCallEscapePriEntry_Object((1,3,6,1,4,1,3902,1015,5200,3,6,1302,3,1))
zxAnCallEscapePriEntry.setIndexNames((0,_D,_J),(0,_D,_K),(0,_D,_L),(0,_D,_P))
if mibBuilder.loadTexts:zxAnCallEscapePriEntry.setStatus(_A)
_ZxAnCallEscapeDsx1LinkNo_Type=Integer32
_ZxAnCallEscapeDsx1LinkNo_Object=MibTableColumn
zxAnCallEscapeDsx1LinkNo=_ZxAnCallEscapeDsx1LinkNo_Object((1,3,6,1,4,1,3902,1015,5200,3,6,1302,3,1,1),_ZxAnCallEscapeDsx1LinkNo_Type())
zxAnCallEscapeDsx1LinkNo.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnCallEscapeDsx1LinkNo.setStatus(_A)
_ZxAnCallEscapePriOperNum_Type=Integer32
_ZxAnCallEscapePriOperNum_Object=MibTableColumn
zxAnCallEscapePriOperNum=_ZxAnCallEscapePriOperNum_Object((1,3,6,1,4,1,3902,1015,5200,3,6,1302,3,1,2),_ZxAnCallEscapePriOperNum_Type())
zxAnCallEscapePriOperNum.setMaxAccess(_F)
if mibBuilder.loadTexts:zxAnCallEscapePriOperNum.setStatus(_A)
_ZxAnCallEscapePriRowStatus_Type=RowStatus
_ZxAnCallEscapePriRowStatus_Object=MibTableColumn
zxAnCallEscapePriRowStatus=_ZxAnCallEscapePriRowStatus_Object((1,3,6,1,4,1,3902,1015,5200,3,6,1302,3,1,50),_ZxAnCallEscapePriRowStatus_Type())
zxAnCallEscapePriRowStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:zxAnCallEscapePriRowStatus.setStatus(_A)
_ZxAnCallEscapePriDLinkTable_Object=MibTable
zxAnCallEscapePriDLinkTable=_ZxAnCallEscapePriDLinkTable_Object((1,3,6,1,4,1,3902,1015,5200,3,6,1302,4))
if mibBuilder.loadTexts:zxAnCallEscapePriDLinkTable.setStatus(_A)
_ZxAnCallEscapePriDLinkEntry_Object=MibTableRow
zxAnCallEscapePriDLinkEntry=_ZxAnCallEscapePriDLinkEntry_Object((1,3,6,1,4,1,3902,1015,5200,3,6,1302,4,1))
zxAnCallEscapePriDLinkEntry.setIndexNames((0,_D,_J),(0,_D,_K),(0,_D,_L),(0,_D,_P),(0,_D,_S))
if mibBuilder.loadTexts:zxAnCallEscapePriDLinkEntry.setStatus(_A)
class _ZxAnCallEscapePriDLinkTimeslot_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,31))
_ZxAnCallEscapePriDLinkTimeslot_Type.__name__=_B
_ZxAnCallEscapePriDLinkTimeslot_Object=MibTableColumn
zxAnCallEscapePriDLinkTimeslot=_ZxAnCallEscapePriDLinkTimeslot_Object((1,3,6,1,4,1,3902,1015,5200,3,6,1302,4,1,1),_ZxAnCallEscapePriDLinkTimeslot_Type())
zxAnCallEscapePriDLinkTimeslot.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnCallEscapePriDLinkTimeslot.setStatus(_A)
class _ZxAnCallEscapePriDLinkLinkId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,512))
_ZxAnCallEscapePriDLinkLinkId_Type.__name__=_B
_ZxAnCallEscapePriDLinkLinkId_Object=MibTableColumn
zxAnCallEscapePriDLinkLinkId=_ZxAnCallEscapePriDLinkLinkId_Object((1,3,6,1,4,1,3902,1015,5200,3,6,1302,4,1,2),_ZxAnCallEscapePriDLinkLinkId_Type())
zxAnCallEscapePriDLinkLinkId.setMaxAccess(_F)
if mibBuilder.loadTexts:zxAnCallEscapePriDLinkLinkId.setStatus(_A)
_ZxAnCallEscapePriDLinkOperNum_Type=Integer32
_ZxAnCallEscapePriDLinkOperNum_Object=MibTableColumn
zxAnCallEscapePriDLinkOperNum=_ZxAnCallEscapePriDLinkOperNum_Object((1,3,6,1,4,1,3902,1015,5200,3,6,1302,4,1,3),_ZxAnCallEscapePriDLinkOperNum_Type())
zxAnCallEscapePriDLinkOperNum.setMaxAccess(_F)
if mibBuilder.loadTexts:zxAnCallEscapePriDLinkOperNum.setStatus(_A)
class _ZxAnCallEscapePriDLinkLinkType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('networkSide',1),('subscriberSide',2)))
_ZxAnCallEscapePriDLinkLinkType_Type.__name__=_B
_ZxAnCallEscapePriDLinkLinkType_Object=MibTableColumn
zxAnCallEscapePriDLinkLinkType=_ZxAnCallEscapePriDLinkLinkType_Object((1,3,6,1,4,1,3902,1015,5200,3,6,1302,4,1,4),_ZxAnCallEscapePriDLinkLinkType_Type())
zxAnCallEscapePriDLinkLinkType.setMaxAccess(_F)
if mibBuilder.loadTexts:zxAnCallEscapePriDLinkLinkType.setStatus(_A)
_ZxAnCallEscapePriDLinkRowStatus_Type=RowStatus
_ZxAnCallEscapePriDLinkRowStatus_Object=MibTableColumn
zxAnCallEscapePriDLinkRowStatus=_ZxAnCallEscapePriDLinkRowStatus_Object((1,3,6,1,4,1,3902,1015,5200,3,6,1302,4,1,50),_ZxAnCallEscapePriDLinkRowStatus_Type())
zxAnCallEscapePriDLinkRowStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:zxAnCallEscapePriDLinkRowStatus.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'zte':zte,'zxAn':zxAn,'zxAnVoiceCallCtrlMib':zxAnVoiceCallCtrlMib,'zxAnVoiceMgmt':zxAnVoiceMgmt,'zxAnVoipCallCtrl':zxAnVoipCallCtrl,'msagCallResStatistic':msagCallResStatistic,'msagCRAccessRatio':msagCRAccessRatio,'msagCRIPSUsingRatio':msagCRIPSUsingRatio,'msagCROpenChannelReq':msagCROpenChannelReq,'msagCRRecOpenSucces':msagCRRecOpenSucces,'msagCRRecOpenFail':msagCRRecOpenFail,'msagCROpenChannTimerOut':msagCROpenChannTimerOut,'msagCRModifyChannel':msagCRModifyChannel,'msagCRRecModifySucces':msagCRRecModifySucces,'msagCRModifyChFail':msagCRModifyChFail,'msagCRWtModifyChannTimerOut':msagCRWtModifyChannTimerOut,'msagCRSendCloseChannel':msagCRSendCloseChannel,'msagCRRecCloseChanSucc':msagCRRecCloseChanSucc,'msagCRRecCloseChanFail':msagCRRecCloseChanFail,'msagCRRecCloseChanTimerOut':msagCRRecCloseChanTimerOut,'msagCRRecMprReload':msagCRRecMprReload,'msagCRClearRTPRecord':msagCRClearRTPRecord,'zxAnVoipCallCtrlGlobalObjects':zxAnVoipCallCtrlGlobalObjects,'zxAnVoipCallCtrlMgmtCapabilities':zxAnVoipCallCtrlMgmtCapabilities,'zxAnCallOptimizationTable':zxAnCallOptimizationTable,'zxAnCallOptimizationEntry':zxAnCallOptimizationEntry,_Q:zxAnCallOptIndex,'zxAnCallOptOpenMsgAck':zxAnCallOptOpenMsgAck,'zxAnCallOptPlayToneAck':zxAnCallOptPlayToneAck,'zxAnCallOptSubPriority':zxAnCallOptSubPriority,'zxAnCallOptH248Statistic':zxAnCallOptH248Statistic,'zxAnCallOptServiceAbnormal':zxAnCallOptServiceAbnormal,'zxAnCallOptMgProtocolErr':zxAnCallOptMgProtocolErr,'zxAnCallOptMgcProtocolErr':zxAnCallOptMgcProtocolErr,'zxAnCallOptMgInsideErr':zxAnCallOptMgInsideErr,'zxAnCallOptCallLimit':zxAnCallOptCallLimit,'zxAnCallOptCallLimitMaxUserNum':zxAnCallOptCallLimitMaxUserNum,'zxAnCallEscapeObjects':zxAnCallEscapeObjects,'zxAnCallEscapeFxoTable':zxAnCallEscapeFxoTable,'zxAnCallEscapeFxoEntry':zxAnCallEscapeFxoEntry,_J:zxAnCallEscapeRack,_K:zxAnCallEscapeShelf,_L:zxAnCallEscapeSlot,_R:zxAnCallEscapePort,'zxAnCallEscapeFxoOperNum':zxAnCallEscapeFxoOperNum,'zxAnCallEscapeFxoRowStatus':zxAnCallEscapeFxoRowStatus,'zxAnCallEscapePriTable':zxAnCallEscapePriTable,'zxAnCallEscapePriEntry':zxAnCallEscapePriEntry,_P:zxAnCallEscapeDsx1LinkNo,'zxAnCallEscapePriOperNum':zxAnCallEscapePriOperNum,'zxAnCallEscapePriRowStatus':zxAnCallEscapePriRowStatus,'zxAnCallEscapePriDLinkTable':zxAnCallEscapePriDLinkTable,'zxAnCallEscapePriDLinkEntry':zxAnCallEscapePriDLinkEntry,_S:zxAnCallEscapePriDLinkTimeslot,'zxAnCallEscapePriDLinkLinkId':zxAnCallEscapePriDLinkLinkId,'zxAnCallEscapePriDLinkOperNum':zxAnCallEscapePriDLinkOperNum,'zxAnCallEscapePriDLinkLinkType':zxAnCallEscapePriDLinkLinkType,'zxAnCallEscapePriDLinkRowStatus':zxAnCallEscapePriDLinkRowStatus})