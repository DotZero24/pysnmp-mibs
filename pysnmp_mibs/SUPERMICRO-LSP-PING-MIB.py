_S='fsLsppRequestOwner'
_R='fsLsppActualHopCount'
_Q='fsLsppHopIndex'
_P='fsLsppSequenceNumber'
_O='DisplayString'
_N='fsLsppStatus'
_M='fsLsppTrapContextName'
_L='fsLsppSenderHandle'
_K='not-accessible'
_J='FsLsppTimeUnit'
_I='fsLsppContextId'
_H='Integer32'
_G='TruthValue'
_F='OctetString'
_E='Unsigned32'
_D='SUPERMICRO-LSP-PING-MIB'
_C='read-write'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_F,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_H,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_E,'enterprises','iso')
DisplayString,PhysAddress,RowPointer,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_O,'PhysAddress','RowPointer','RowStatus','TextualConvention',_G)
fsLspp=ModuleIdentity((1,3,6,1,4,1,10876,101,1,13,11))
if mibBuilder.loadTexts:fsLspp.setRevisions(('2012-09-05 00:00',))
class FsLsppTimeUnit(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('milliseconds',1),('seconds',2),('minutes',3)))
class FsLsppAddressType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*(('notApplicable',0),('ipv4Numbered',1),('ipv4UnNumbered',2),('ipv6Numbered',3),('ipv6UnNumbered',4)))
_FsLsppGlobals_ObjectIdentity=ObjectIdentity
fsLsppGlobals=_FsLsppGlobals_ObjectIdentity((1,3,6,1,4,1,10876,101,1,13,11,1))
_FsLsppGlobalConfigTable_Object=MibTable
fsLsppGlobalConfigTable=_FsLsppGlobalConfigTable_Object((1,3,6,1,4,1,10876,101,1,13,11,1,1))
if mibBuilder.loadTexts:fsLsppGlobalConfigTable.setStatus(_A)
_FsLsppGlobalConfigTableEntry_Object=MibTableRow
fsLsppGlobalConfigTableEntry=_FsLsppGlobalConfigTableEntry_Object((1,3,6,1,4,1,10876,101,1,13,11,1,1,1))
fsLsppGlobalConfigTableEntry.setIndexNames((0,_D,_I))
if mibBuilder.loadTexts:fsLsppGlobalConfigTableEntry.setStatus(_A)
_FsLsppContextId_Type=Unsigned32
_FsLsppContextId_Object=MibTableColumn
fsLsppContextId=_FsLsppContextId_Object((1,3,6,1,4,1,10876,101,1,13,11,1,1,1,1),_FsLsppContextId_Type())
fsLsppContextId.setMaxAccess(_K)
if mibBuilder.loadTexts:fsLsppContextId.setStatus(_A)
class _FsLsppSystemControl_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('start',1),('shutdown',2)))
_FsLsppSystemControl_Type.__name__=_H
_FsLsppSystemControl_Object=MibTableColumn
fsLsppSystemControl=_FsLsppSystemControl_Object((1,3,6,1,4,1,10876,101,1,13,11,1,1,1,2),_FsLsppSystemControl_Type())
fsLsppSystemControl.setMaxAccess(_C)
if mibBuilder.loadTexts:fsLsppSystemControl.setStatus(_A)
class _FsLsppTrapStatus_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_FsLsppTrapStatus_Type.__name__=_H
_FsLsppTrapStatus_Object=MibTableColumn
fsLsppTrapStatus=_FsLsppTrapStatus_Object((1,3,6,1,4,1,10876,101,1,13,11,1,1,1,3),_FsLsppTrapStatus_Type())
fsLsppTrapStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:fsLsppTrapStatus.setStatus(_A)
class _FsLsppTraceLevel_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,8191))
_FsLsppTraceLevel_Type.__name__=_H
_FsLsppTraceLevel_Object=MibTableColumn
fsLsppTraceLevel=_FsLsppTraceLevel_Object((1,3,6,1,4,1,10876,101,1,13,11,1,1,1,4),_FsLsppTraceLevel_Type())
fsLsppTraceLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:fsLsppTraceLevel.setStatus(_A)
class _FsLsppAgeOutTime_Type(Unsigned32):defaultValue=1;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1000))
_FsLsppAgeOutTime_Type.__name__=_E
_FsLsppAgeOutTime_Object=MibTableColumn
fsLsppAgeOutTime=_FsLsppAgeOutTime_Object((1,3,6,1,4,1,10876,101,1,13,11,1,1,1,5),_FsLsppAgeOutTime_Type())
fsLsppAgeOutTime.setMaxAccess(_C)
if mibBuilder.loadTexts:fsLsppAgeOutTime.setStatus(_A)
class _FsLsppAgeOutTmrUnit_Type(FsLsppTimeUnit):defaultValue=3
_FsLsppAgeOutTmrUnit_Type.__name__=_J
_FsLsppAgeOutTmrUnit_Object=MibTableColumn
fsLsppAgeOutTmrUnit=_FsLsppAgeOutTmrUnit_Object((1,3,6,1,4,1,10876,101,1,13,11,1,1,1,6),_FsLsppAgeOutTmrUnit_Type())
fsLsppAgeOutTmrUnit.setMaxAccess(_C)
if mibBuilder.loadTexts:fsLsppAgeOutTmrUnit.setStatus(_A)
class _FsLsppClearEchoStats_Type(TruthValue):defaultValue=2
_FsLsppClearEchoStats_Type.__name__=_G
_FsLsppClearEchoStats_Object=MibTableColumn
fsLsppClearEchoStats=_FsLsppClearEchoStats_Object((1,3,6,1,4,1,10876,101,1,13,11,1,1,1,7),_FsLsppClearEchoStats_Type())
fsLsppClearEchoStats.setMaxAccess(_C)
if mibBuilder.loadTexts:fsLsppClearEchoStats.setStatus(_A)
class _FsLsppBfdBtStrapRespReq_Type(TruthValue):defaultValue=1
_FsLsppBfdBtStrapRespReq_Type.__name__=_G
_FsLsppBfdBtStrapRespReq_Object=MibTableColumn
fsLsppBfdBtStrapRespReq=_FsLsppBfdBtStrapRespReq_Object((1,3,6,1,4,1,10876,101,1,13,11,1,1,1,8),_FsLsppBfdBtStrapRespReq_Type())
fsLsppBfdBtStrapRespReq.setMaxAccess(_C)
if mibBuilder.loadTexts:fsLsppBfdBtStrapRespReq.setStatus(_A)
class _FsLsppBfdBtStrapAgeOutTime_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1000))
_FsLsppBfdBtStrapAgeOutTime_Type.__name__=_E
_FsLsppBfdBtStrapAgeOutTime_Object=MibTableColumn
fsLsppBfdBtStrapAgeOutTime=_FsLsppBfdBtStrapAgeOutTime_Object((1,3,6,1,4,1,10876,101,1,13,11,1,1,1,9),_FsLsppBfdBtStrapAgeOutTime_Type())
fsLsppBfdBtStrapAgeOutTime.setMaxAccess(_C)
if mibBuilder.loadTexts:fsLsppBfdBtStrapAgeOutTime.setStatus(_A)
class _FsLsppBfdBtStrapAgeOutTmrUnit_Type(FsLsppTimeUnit):defaultValue=3
_FsLsppBfdBtStrapAgeOutTmrUnit_Type.__name__=_J
_FsLsppBfdBtStrapAgeOutTmrUnit_Object=MibTableColumn
fsLsppBfdBtStrapAgeOutTmrUnit=_FsLsppBfdBtStrapAgeOutTmrUnit_Object((1,3,6,1,4,1,10876,101,1,13,11,1,1,1,10),_FsLsppBfdBtStrapAgeOutTmrUnit_Type())
fsLsppBfdBtStrapAgeOutTmrUnit.setMaxAccess(_C)
if mibBuilder.loadTexts:fsLsppBfdBtStrapAgeOutTmrUnit.setStatus(_A)
_FsLsppGlobalStatsTable_Object=MibTable
fsLsppGlobalStatsTable=_FsLsppGlobalStatsTable_Object((1,3,6,1,4,1,10876,101,1,13,11,1,2))
if mibBuilder.loadTexts:fsLsppGlobalStatsTable.setStatus(_A)
_FsLsppGlobalStatsTableEntry_Object=MibTableRow
fsLsppGlobalStatsTableEntry=_FsLsppGlobalStatsTableEntry_Object((1,3,6,1,4,1,10876,101,1,13,11,1,2,1))
fsLsppGlobalStatsTableEntry.setIndexNames((0,_D,_I))
if mibBuilder.loadTexts:fsLsppGlobalStatsTableEntry.setStatus(_A)
_FsLsppGlbStatReqTx_Type=Counter32
_FsLsppGlbStatReqTx_Object=MibTableColumn
fsLsppGlbStatReqTx=_FsLsppGlbStatReqTx_Object((1,3,6,1,4,1,10876,101,1,13,11,1,2,1,1),_FsLsppGlbStatReqTx_Type())
fsLsppGlbStatReqTx.setMaxAccess(_B)
if mibBuilder.loadTexts:fsLsppGlbStatReqTx.setStatus(_A)
_FsLsppGlbStatReqRx_Type=Counter32
_FsLsppGlbStatReqRx_Object=MibTableColumn
fsLsppGlbStatReqRx=_FsLsppGlbStatReqRx_Object((1,3,6,1,4,1,10876,101,1,13,11,1,2,1,2),_FsLsppGlbStatReqRx_Type())
fsLsppGlbStatReqRx.setMaxAccess(_B)
if mibBuilder.loadTexts:fsLsppGlbStatReqRx.setStatus(_A)
_FsLsppGlbStatReqTimedOut_Type=Counter32
_FsLsppGlbStatReqTimedOut_Object=MibTableColumn
fsLsppGlbStatReqTimedOut=_FsLsppGlbStatReqTimedOut_Object((1,3,6,1,4,1,10876,101,1,13,11,1,2,1,3),_FsLsppGlbStatReqTimedOut_Type())
fsLsppGlbStatReqTimedOut.setMaxAccess(_B)
if mibBuilder.loadTexts:fsLsppGlbStatReqTimedOut.setStatus(_A)
_FsLsppGlbStatReqUnSent_Type=Counter32
_FsLsppGlbStatReqUnSent_Object=MibTableColumn
fsLsppGlbStatReqUnSent=_FsLsppGlbStatReqUnSent_Object((1,3,6,1,4,1,10876,101,1,13,11,1,2,1,4),_FsLsppGlbStatReqUnSent_Type())
fsLsppGlbStatReqUnSent.setMaxAccess(_B)
if mibBuilder.loadTexts:fsLsppGlbStatReqUnSent.setStatus(_A)
_FsLsppGlbStatReplyTx_Type=Counter32
_FsLsppGlbStatReplyTx_Object=MibTableColumn
fsLsppGlbStatReplyTx=_FsLsppGlbStatReplyTx_Object((1,3,6,1,4,1,10876,101,1,13,11,1,2,1,5),_FsLsppGlbStatReplyTx_Type())
fsLsppGlbStatReplyTx.setMaxAccess(_B)
if mibBuilder.loadTexts:fsLsppGlbStatReplyTx.setStatus(_A)
_FsLsppGlbStatReplyRx_Type=Counter32
_FsLsppGlbStatReplyRx_Object=MibTableColumn
fsLsppGlbStatReplyRx=_FsLsppGlbStatReplyRx_Object((1,3,6,1,4,1,10876,101,1,13,11,1,2,1,6),_FsLsppGlbStatReplyRx_Type())
fsLsppGlbStatReplyRx.setMaxAccess(_B)
if mibBuilder.loadTexts:fsLsppGlbStatReplyRx.setStatus(_A)
_FsLsppGlbStatReplyDropped_Type=Counter32
_FsLsppGlbStatReplyDropped_Object=MibTableColumn
fsLsppGlbStatReplyDropped=_FsLsppGlbStatReplyDropped_Object((1,3,6,1,4,1,10876,101,1,13,11,1,2,1,7),_FsLsppGlbStatReplyDropped_Type())
fsLsppGlbStatReplyDropped.setMaxAccess(_B)
if mibBuilder.loadTexts:fsLsppGlbStatReplyDropped.setStatus(_A)
_FsLsppGlbStatReplyUnSent_Type=Counter32
_FsLsppGlbStatReplyUnSent_Object=MibTableColumn
fsLsppGlbStatReplyUnSent=_FsLsppGlbStatReplyUnSent_Object((1,3,6,1,4,1,10876,101,1,13,11,1,2,1,8),_FsLsppGlbStatReplyUnSent_Type())
fsLsppGlbStatReplyUnSent.setMaxAccess(_B)
if mibBuilder.loadTexts:fsLsppGlbStatReplyUnSent.setStatus(_A)
_FsLsppGlbStatReplyFromEgr_Type=Counter32
_FsLsppGlbStatReplyFromEgr_Object=MibTableColumn
fsLsppGlbStatReplyFromEgr=_FsLsppGlbStatReplyFromEgr_Object((1,3,6,1,4,1,10876,101,1,13,11,1,2,1,9),_FsLsppGlbStatReplyFromEgr_Type())
fsLsppGlbStatReplyFromEgr.setMaxAccess(_B)
if mibBuilder.loadTexts:fsLsppGlbStatReplyFromEgr.setStatus(_A)
_FsLsppGlbStatUnLbldOutIf_Type=Counter32
_FsLsppGlbStatUnLbldOutIf_Object=MibTableColumn
fsLsppGlbStatUnLbldOutIf=_FsLsppGlbStatUnLbldOutIf_Object((1,3,6,1,4,1,10876,101,1,13,11,1,2,1,10),_FsLsppGlbStatUnLbldOutIf_Type())
fsLsppGlbStatUnLbldOutIf.setMaxAccess(_B)
if mibBuilder.loadTexts:fsLsppGlbStatUnLbldOutIf.setStatus(_A)
_FsLsppGlbStatDsMapMismatch_Type=Counter32
_FsLsppGlbStatDsMapMismatch_Object=MibTableColumn
fsLsppGlbStatDsMapMismatch=_FsLsppGlbStatDsMapMismatch_Object((1,3,6,1,4,1,10876,101,1,13,11,1,2,1,11),_FsLsppGlbStatDsMapMismatch_Type())
fsLsppGlbStatDsMapMismatch.setMaxAccess(_B)
if mibBuilder.loadTexts:fsLsppGlbStatDsMapMismatch.setStatus(_A)
_FsLsppGlbStatFecLblMismatch_Type=Counter32
_FsLsppGlbStatFecLblMismatch_Object=MibTableColumn
fsLsppGlbStatFecLblMismatch=_FsLsppGlbStatFecLblMismatch_Object((1,3,6,1,4,1,10876,101,1,13,11,1,2,1,12),_FsLsppGlbStatFecLblMismatch_Type())
fsLsppGlbStatFecLblMismatch.setMaxAccess(_B)
if mibBuilder.loadTexts:fsLsppGlbStatFecLblMismatch.setStatus(_A)
_FsLsppGlbStatNoFecMapping_Type=Counter32
_FsLsppGlbStatNoFecMapping_Object=MibTableColumn
fsLsppGlbStatNoFecMapping=_FsLsppGlbStatNoFecMapping_Object((1,3,6,1,4,1,10876,101,1,13,11,1,2,1,13),_FsLsppGlbStatNoFecMapping_Type())
fsLsppGlbStatNoFecMapping.setMaxAccess(_B)
if mibBuilder.loadTexts:fsLsppGlbStatNoFecMapping.setStatus(_A)
_FsLsppGlbStatUnKUpstreamIf_Type=Counter32
_FsLsppGlbStatUnKUpstreamIf_Object=MibTableColumn
fsLsppGlbStatUnKUpstreamIf=_FsLsppGlbStatUnKUpstreamIf_Object((1,3,6,1,4,1,10876,101,1,13,11,1,2,1,14),_FsLsppGlbStatUnKUpstreamIf_Type())
fsLsppGlbStatUnKUpstreamIf.setMaxAccess(_B)
if mibBuilder.loadTexts:fsLsppGlbStatUnKUpstreamIf.setStatus(_A)
_FsLsppGlbStatReqLblSwitched_Type=Counter32
_FsLsppGlbStatReqLblSwitched_Object=MibTableColumn
fsLsppGlbStatReqLblSwitched=_FsLsppGlbStatReqLblSwitched_Object((1,3,6,1,4,1,10876,101,1,13,11,1,2,1,15),_FsLsppGlbStatReqLblSwitched_Type())
fsLsppGlbStatReqLblSwitched.setMaxAccess(_B)
if mibBuilder.loadTexts:fsLsppGlbStatReqLblSwitched.setStatus(_A)
_FsLsppGlbStatReqUnSupptdTlv_Type=Counter32
_FsLsppGlbStatReqUnSupptdTlv_Object=MibTableColumn
fsLsppGlbStatReqUnSupptdTlv=_FsLsppGlbStatReqUnSupptdTlv_Object((1,3,6,1,4,1,10876,101,1,13,11,1,2,1,16),_FsLsppGlbStatReqUnSupptdTlv_Type())
fsLsppGlbStatReqUnSupptdTlv.setMaxAccess(_B)
if mibBuilder.loadTexts:fsLsppGlbStatReqUnSupptdTlv.setStatus(_A)
_FsLsppGlbStatMalformedReq_Type=Counter32
_FsLsppGlbStatMalformedReq_Object=MibTableColumn
fsLsppGlbStatMalformedReq=_FsLsppGlbStatMalformedReq_Object((1,3,6,1,4,1,10876,101,1,13,11,1,2,1,17),_FsLsppGlbStatMalformedReq_Type())
fsLsppGlbStatMalformedReq.setMaxAccess(_B)
if mibBuilder.loadTexts:fsLsppGlbStatMalformedReq.setStatus(_A)
_FsLsppGlbStatNoLblEntry_Type=Counter32
_FsLsppGlbStatNoLblEntry_Object=MibTableColumn
fsLsppGlbStatNoLblEntry=_FsLsppGlbStatNoLblEntry_Object((1,3,6,1,4,1,10876,101,1,13,11,1,2,1,18),_FsLsppGlbStatNoLblEntry_Type())
fsLsppGlbStatNoLblEntry.setMaxAccess(_B)
if mibBuilder.loadTexts:fsLsppGlbStatNoLblEntry.setStatus(_A)
_FsLsppGlbStatPreTermReq_Type=Counter32
_FsLsppGlbStatPreTermReq_Object=MibTableColumn
fsLsppGlbStatPreTermReq=_FsLsppGlbStatPreTermReq_Object((1,3,6,1,4,1,10876,101,1,13,11,1,2,1,19),_FsLsppGlbStatPreTermReq_Type())
fsLsppGlbStatPreTermReq.setMaxAccess(_B)
if mibBuilder.loadTexts:fsLsppGlbStatPreTermReq.setStatus(_A)
_FsLsppGlbStatProtMismatch_Type=Counter32
_FsLsppGlbStatProtMismatch_Object=MibTableColumn
fsLsppGlbStatProtMismatch=_FsLsppGlbStatProtMismatch_Object((1,3,6,1,4,1,10876,101,1,13,11,1,2,1,20),_FsLsppGlbStatProtMismatch_Type())
fsLsppGlbStatProtMismatch.setMaxAccess(_B)
if mibBuilder.loadTexts:fsLsppGlbStatProtMismatch.setStatus(_A)
_FsLsppGlbStatRsvdRetCode_Type=Counter32
_FsLsppGlbStatRsvdRetCode_Object=MibTableColumn
fsLsppGlbStatRsvdRetCode=_FsLsppGlbStatRsvdRetCode_Object((1,3,6,1,4,1,10876,101,1,13,11,1,2,1,21),_FsLsppGlbStatRsvdRetCode_Type())
fsLsppGlbStatRsvdRetCode.setMaxAccess(_B)
if mibBuilder.loadTexts:fsLsppGlbStatRsvdRetCode.setStatus(_A)
_FsLsppGlbStatNoRetCode_Type=Counter32
_FsLsppGlbStatNoRetCode_Object=MibTableColumn
fsLsppGlbStatNoRetCode=_FsLsppGlbStatNoRetCode_Object((1,3,6,1,4,1,10876,101,1,13,11,1,2,1,22),_FsLsppGlbStatNoRetCode_Type())
fsLsppGlbStatNoRetCode.setMaxAccess(_B)
if mibBuilder.loadTexts:fsLsppGlbStatNoRetCode.setStatus(_A)
_FsLsppGlbStatUndefRetCode_Type=Counter32
_FsLsppGlbStatUndefRetCode_Object=MibTableColumn
fsLsppGlbStatUndefRetCode=_FsLsppGlbStatUndefRetCode_Object((1,3,6,1,4,1,10876,101,1,13,11,1,2,1,23),_FsLsppGlbStatUndefRetCode_Type())
fsLsppGlbStatUndefRetCode.setMaxAccess(_B)
if mibBuilder.loadTexts:fsLsppGlbStatUndefRetCode.setStatus(_A)
_FsLsppGlbStatInvalidPktDropped_Type=Counter32
_FsLsppGlbStatInvalidPktDropped_Object=MibTableColumn
fsLsppGlbStatInvalidPktDropped=_FsLsppGlbStatInvalidPktDropped_Object((1,3,6,1,4,1,10876,101,1,13,11,1,2,1,24),_FsLsppGlbStatInvalidPktDropped_Type())
fsLsppGlbStatInvalidPktDropped.setMaxAccess(_B)
if mibBuilder.loadTexts:fsLsppGlbStatInvalidPktDropped.setStatus(_A)
_FsLsppPingTrace_ObjectIdentity=ObjectIdentity
fsLsppPingTrace=_FsLsppPingTrace_ObjectIdentity((1,3,6,1,4,1,10876,101,1,13,11,2))
_FsLsppPingTraceTable_Object=MibTable
fsLsppPingTraceTable=_FsLsppPingTraceTable_Object((1,3,6,1,4,1,10876,101,1,13,11,2,1))
if mibBuilder.loadTexts:fsLsppPingTraceTable.setStatus(_A)
_FsLsppPingTraceTableEntry_Object=MibTableRow
fsLsppPingTraceTableEntry=_FsLsppPingTraceTableEntry_Object((1,3,6,1,4,1,10876,101,1,13,11,2,1,1))
fsLsppPingTraceTableEntry.setIndexNames((0,_D,_I),(0,_D,_L))
if mibBuilder.loadTexts:fsLsppPingTraceTableEntry.setStatus(_A)
class _FsLsppSenderHandle_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_FsLsppSenderHandle_Type.__name__=_E
_FsLsppSenderHandle_Object=MibTableColumn
fsLsppSenderHandle=_FsLsppSenderHandle_Object((1,3,6,1,4,1,10876,101,1,13,11,2,1,1,1),_FsLsppSenderHandle_Type())
fsLsppSenderHandle.setMaxAccess(_K)
if mibBuilder.loadTexts:fsLsppSenderHandle.setStatus(_A)
class _FsLsppRequestType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('ping',1),('traceRoute',2)))
_FsLsppRequestType_Type.__name__=_H
_FsLsppRequestType_Object=MibTableColumn
fsLsppRequestType=_FsLsppRequestType_Object((1,3,6,1,4,1,10876,101,1,13,11,2,1,1,2),_FsLsppRequestType_Type())
fsLsppRequestType.setMaxAccess(_C)
if mibBuilder.loadTexts:fsLsppRequestType.setStatus(_A)
class _FsLsppRequestOwner_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('management',1),('bfd',2)))
_FsLsppRequestOwner_Type.__name__=_H
_FsLsppRequestOwner_Object=MibTableColumn
fsLsppRequestOwner=_FsLsppRequestOwner_Object((1,3,6,1,4,1,10876,101,1,13,11,2,1,1,3),_FsLsppRequestOwner_Type())
fsLsppRequestOwner.setMaxAccess(_B)
if mibBuilder.loadTexts:fsLsppRequestOwner.setStatus(_A)
class _FsLsppPathType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('ldpIpv4',1),('ldpIpv6',2),('rsvpIpv4',3),('rsvpIpv6',4),('fec128Pw',5),('fec129Pw',6),('mep',7)))
_FsLsppPathType_Type.__name__=_H
_FsLsppPathType_Object=MibTableColumn
fsLsppPathType=_FsLsppPathType_Object((1,3,6,1,4,1,10876,101,1,13,11,2,1,1,4),_FsLsppPathType_Type())
fsLsppPathType.setMaxAccess(_C)
if mibBuilder.loadTexts:fsLsppPathType.setStatus(_A)
_FsLsppPathPointer_Type=RowPointer
_FsLsppPathPointer_Object=MibTableColumn
fsLsppPathPointer=_FsLsppPathPointer_Object((1,3,6,1,4,1,10876,101,1,13,11,2,1,1,5),_FsLsppPathPointer_Type())
fsLsppPathPointer.setMaxAccess(_C)
if mibBuilder.loadTexts:fsLsppPathPointer.setStatus(_A)
_FsLsppTgtMipGlobalId_Type=Unsigned32
_FsLsppTgtMipGlobalId_Object=MibTableColumn
fsLsppTgtMipGlobalId=_FsLsppTgtMipGlobalId_Object((1,3,6,1,4,1,10876,101,1,13,11,2,1,1,6),_FsLsppTgtMipGlobalId_Type())
fsLsppTgtMipGlobalId.setMaxAccess(_C)
if mibBuilder.loadTexts:fsLsppTgtMipGlobalId.setStatus(_A)
_FsLsppTgtMipNodeId_Type=Unsigned32
_FsLsppTgtMipNodeId_Object=MibTableColumn
fsLsppTgtMipNodeId=_FsLsppTgtMipNodeId_Object((1,3,6,1,4,1,10876,101,1,13,11,2,1,1,7),_FsLsppTgtMipNodeId_Type())
fsLsppTgtMipNodeId.setMaxAccess(_C)
if mibBuilder.loadTexts:fsLsppTgtMipNodeId.setStatus(_A)
_FsLsppTgtMipIfNum_Type=Unsigned32
_FsLsppTgtMipIfNum_Object=MibTableColumn
fsLsppTgtMipIfNum=_FsLsppTgtMipIfNum_Object((1,3,6,1,4,1,10876,101,1,13,11,2,1,1,8),_FsLsppTgtMipIfNum_Type())
fsLsppTgtMipIfNum.setMaxAccess(_C)
if mibBuilder.loadTexts:fsLsppTgtMipIfNum.setStatus(_A)
class _FsLsppReplyMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('noReply',1),('ip',2),('ipRouterAlert',3),('controlChannel',4)))
_FsLsppReplyMode_Type.__name__=_H
_FsLsppReplyMode_Object=MibTableColumn
fsLsppReplyMode=_FsLsppReplyMode_Object((1,3,6,1,4,1,10876,101,1,13,11,2,1,1,9),_FsLsppReplyMode_Type())
fsLsppReplyMode.setMaxAccess(_C)
if mibBuilder.loadTexts:fsLsppReplyMode.setStatus(_A)
class _FsLsppRepeatCount_Type(Unsigned32):defaultValue=5;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_FsLsppRepeatCount_Type.__name__=_E
_FsLsppRepeatCount_Object=MibTableColumn
fsLsppRepeatCount=_FsLsppRepeatCount_Object((1,3,6,1,4,1,10876,101,1,13,11,2,1,1,10),_FsLsppRepeatCount_Type())
fsLsppRepeatCount.setMaxAccess(_C)
if mibBuilder.loadTexts:fsLsppRepeatCount.setStatus(_A)
class _FsLsppPacketSize_Type(Unsigned32):defaultValue=200;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(40,18024))
_FsLsppPacketSize_Type.__name__=_E
_FsLsppPacketSize_Object=MibTableColumn
fsLsppPacketSize=_FsLsppPacketSize_Object((1,3,6,1,4,1,10876,101,1,13,11,2,1,1,11),_FsLsppPacketSize_Type())
fsLsppPacketSize.setMaxAccess(_C)
if mibBuilder.loadTexts:fsLsppPacketSize.setStatus(_A)
class _FsLsppPadPattern_Type(OctetString):defaultHexValue='ABCD';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,16))
_FsLsppPadPattern_Type.__name__=_F
_FsLsppPadPattern_Object=MibTableColumn
fsLsppPadPattern=_FsLsppPadPattern_Object((1,3,6,1,4,1,10876,101,1,13,11,2,1,1,12),_FsLsppPadPattern_Type())
fsLsppPadPattern.setMaxAccess(_C)
if mibBuilder.loadTexts:fsLsppPadPattern.setStatus(_A)
class _FsLsppTTLValue_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_FsLsppTTLValue_Type.__name__=_E
_FsLsppTTLValue_Object=MibTableColumn
fsLsppTTLValue=_FsLsppTTLValue_Object((1,3,6,1,4,1,10876,101,1,13,11,2,1,1,13),_FsLsppTTLValue_Type())
fsLsppTTLValue.setMaxAccess(_C)
if mibBuilder.loadTexts:fsLsppTTLValue.setStatus(_A)
class _FsLsppWFRInterval_Type(Unsigned32):defaultValue=2;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1000))
_FsLsppWFRInterval_Type.__name__=_E
_FsLsppWFRInterval_Object=MibTableColumn
fsLsppWFRInterval=_FsLsppWFRInterval_Object((1,3,6,1,4,1,10876,101,1,13,11,2,1,1,14),_FsLsppWFRInterval_Type())
fsLsppWFRInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:fsLsppWFRInterval.setStatus(_A)
class _FsLsppWFRTmrUnit_Type(FsLsppTimeUnit):defaultValue=2
_FsLsppWFRTmrUnit_Type.__name__=_J
_FsLsppWFRTmrUnit_Object=MibTableColumn
fsLsppWFRTmrUnit=_FsLsppWFRTmrUnit_Object((1,3,6,1,4,1,10876,101,1,13,11,2,1,1,15),_FsLsppWFRTmrUnit_Type())
fsLsppWFRTmrUnit.setMaxAccess(_C)
if mibBuilder.loadTexts:fsLsppWFRTmrUnit.setStatus(_A)
class _FsLsppWTSInterval_Type(Unsigned32):defaultValue=1;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1000))
_FsLsppWTSInterval_Type.__name__=_E
_FsLsppWTSInterval_Object=MibTableColumn
fsLsppWTSInterval=_FsLsppWTSInterval_Object((1,3,6,1,4,1,10876,101,1,13,11,2,1,1,16),_FsLsppWTSInterval_Type())
fsLsppWTSInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:fsLsppWTSInterval.setStatus(_A)
class _FsLsppWTSTmrUnit_Type(FsLsppTimeUnit):defaultValue=2
_FsLsppWTSTmrUnit_Type.__name__=_J
_FsLsppWTSTmrUnit_Object=MibTableColumn
fsLsppWTSTmrUnit=_FsLsppWTSTmrUnit_Object((1,3,6,1,4,1,10876,101,1,13,11,2,1,1,17),_FsLsppWTSTmrUnit_Type())
fsLsppWTSTmrUnit.setMaxAccess(_C)
if mibBuilder.loadTexts:fsLsppWTSTmrUnit.setStatus(_A)
class _FsLsppReplyDscpValue_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
_FsLsppReplyDscpValue_Type.__name__=_E
_FsLsppReplyDscpValue_Object=MibTableColumn
fsLsppReplyDscpValue=_FsLsppReplyDscpValue_Object((1,3,6,1,4,1,10876,101,1,13,11,2,1,1,18),_FsLsppReplyDscpValue_Type())
fsLsppReplyDscpValue.setMaxAccess(_C)
if mibBuilder.loadTexts:fsLsppReplyDscpValue.setStatus(_A)
class _FsLsppSweepOption_Type(TruthValue):defaultValue=2
_FsLsppSweepOption_Type.__name__=_G
_FsLsppSweepOption_Object=MibTableColumn
fsLsppSweepOption=_FsLsppSweepOption_Object((1,3,6,1,4,1,10876,101,1,13,11,2,1,1,19),_FsLsppSweepOption_Type())
fsLsppSweepOption.setMaxAccess(_C)
if mibBuilder.loadTexts:fsLsppSweepOption.setStatus(_A)
class _FsLsppSweepMinimum_Type(Unsigned32):defaultValue=100
_FsLsppSweepMinimum_Type.__name__=_E
_FsLsppSweepMinimum_Object=MibTableColumn
fsLsppSweepMinimum=_FsLsppSweepMinimum_Object((1,3,6,1,4,1,10876,101,1,13,11,2,1,1,20),_FsLsppSweepMinimum_Type())
fsLsppSweepMinimum.setMaxAccess(_C)
if mibBuilder.loadTexts:fsLsppSweepMinimum.setStatus(_A)
class _FsLsppSweepMaximum_Type(Unsigned32):defaultValue=17986
_FsLsppSweepMaximum_Type.__name__=_E
_FsLsppSweepMaximum_Object=MibTableColumn
fsLsppSweepMaximum=_FsLsppSweepMaximum_Object((1,3,6,1,4,1,10876,101,1,13,11,2,1,1,21),_FsLsppSweepMaximum_Type())
fsLsppSweepMaximum.setMaxAccess(_C)
if mibBuilder.loadTexts:fsLsppSweepMaximum.setStatus(_A)
class _FsLsppSweepIncrement_Type(Unsigned32):defaultValue=100;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,1000))
_FsLsppSweepIncrement_Type.__name__=_E
_FsLsppSweepIncrement_Object=MibTableColumn
fsLsppSweepIncrement=_FsLsppSweepIncrement_Object((1,3,6,1,4,1,10876,101,1,13,11,2,1,1,22),_FsLsppSweepIncrement_Type())
fsLsppSweepIncrement.setMaxAccess(_C)
if mibBuilder.loadTexts:fsLsppSweepIncrement.setStatus(_A)
class _FsLsppBurstOption_Type(TruthValue):defaultValue=2
_FsLsppBurstOption_Type.__name__=_G
_FsLsppBurstOption_Object=MibTableColumn
fsLsppBurstOption=_FsLsppBurstOption_Object((1,3,6,1,4,1,10876,101,1,13,11,2,1,1,23),_FsLsppBurstOption_Type())
fsLsppBurstOption.setMaxAccess(_C)
if mibBuilder.loadTexts:fsLsppBurstOption.setStatus(_A)
class _FsLsppBurstSize_Type(Unsigned32):defaultValue=3;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1000))
_FsLsppBurstSize_Type.__name__=_E
_FsLsppBurstSize_Object=MibTableColumn
fsLsppBurstSize=_FsLsppBurstSize_Object((1,3,6,1,4,1,10876,101,1,13,11,2,1,1,24),_FsLsppBurstSize_Type())
fsLsppBurstSize.setMaxAccess(_C)
if mibBuilder.loadTexts:fsLsppBurstSize.setStatus(_A)
class _FsLsppEXPValue_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_FsLsppEXPValue_Type.__name__=_E
_FsLsppEXPValue_Object=MibTableColumn
fsLsppEXPValue=_FsLsppEXPValue_Object((1,3,6,1,4,1,10876,101,1,13,11,2,1,1,25),_FsLsppEXPValue_Type())
fsLsppEXPValue.setMaxAccess(_C)
if mibBuilder.loadTexts:fsLsppEXPValue.setStatus(_A)
class _FsLsppDsMap_Type(TruthValue):defaultValue=2
_FsLsppDsMap_Type.__name__=_G
_FsLsppDsMap_Object=MibTableColumn
fsLsppDsMap=_FsLsppDsMap_Object((1,3,6,1,4,1,10876,101,1,13,11,2,1,1,26),_FsLsppDsMap_Type())
fsLsppDsMap.setMaxAccess(_C)
if mibBuilder.loadTexts:fsLsppDsMap.setStatus(_A)
class _FsLsppFecValidate_Type(TruthValue):defaultValue=1
_FsLsppFecValidate_Type.__name__=_G
_FsLsppFecValidate_Object=MibTableColumn
fsLsppFecValidate=_FsLsppFecValidate_Object((1,3,6,1,4,1,10876,101,1,13,11,2,1,1,27),_FsLsppFecValidate_Type())
fsLsppFecValidate.setMaxAccess(_C)
if mibBuilder.loadTexts:fsLsppFecValidate.setStatus(_A)
class _FsLsppReplyPadTlv_Type(TruthValue):defaultValue=2
_FsLsppReplyPadTlv_Type.__name__=_G
_FsLsppReplyPadTlv_Object=MibTableColumn
fsLsppReplyPadTlv=_FsLsppReplyPadTlv_Object((1,3,6,1,4,1,10876,101,1,13,11,2,1,1,28),_FsLsppReplyPadTlv_Type())
fsLsppReplyPadTlv.setMaxAccess(_C)
if mibBuilder.loadTexts:fsLsppReplyPadTlv.setStatus(_A)
class _FsLsppForceExplicitNull_Type(TruthValue):defaultValue=2
_FsLsppForceExplicitNull_Type.__name__=_G
_FsLsppForceExplicitNull_Object=MibTableColumn
fsLsppForceExplicitNull=_FsLsppForceExplicitNull_Object((1,3,6,1,4,1,10876,101,1,13,11,2,1,1,29),_FsLsppForceExplicitNull_Type())
fsLsppForceExplicitNull.setMaxAccess(_C)
if mibBuilder.loadTexts:fsLsppForceExplicitNull.setStatus(_A)
class _FsLsppInterfaceLabelTlv_Type(TruthValue):defaultValue=2
_FsLsppInterfaceLabelTlv_Type.__name__=_G
_FsLsppInterfaceLabelTlv_Object=MibTableColumn
fsLsppInterfaceLabelTlv=_FsLsppInterfaceLabelTlv_Object((1,3,6,1,4,1,10876,101,1,13,11,2,1,1,30),_FsLsppInterfaceLabelTlv_Type())
fsLsppInterfaceLabelTlv.setMaxAccess(_C)
if mibBuilder.loadTexts:fsLsppInterfaceLabelTlv.setStatus(_A)
class _FsLsppSameSeqNumOption_Type(TruthValue):defaultValue=2
_FsLsppSameSeqNumOption_Type.__name__=_G
_FsLsppSameSeqNumOption_Object=MibTableColumn
fsLsppSameSeqNumOption=_FsLsppSameSeqNumOption_Object((1,3,6,1,4,1,10876,101,1,13,11,2,1,1,31),_FsLsppSameSeqNumOption_Type())
fsLsppSameSeqNumOption.setMaxAccess(_C)
if mibBuilder.loadTexts:fsLsppSameSeqNumOption.setStatus(_A)
class _FsLsppVerbose_Type(TruthValue):defaultValue=2
_FsLsppVerbose_Type.__name__=_G
_FsLsppVerbose_Object=MibTableColumn
fsLsppVerbose=_FsLsppVerbose_Object((1,3,6,1,4,1,10876,101,1,13,11,2,1,1,32),_FsLsppVerbose_Type())
fsLsppVerbose.setMaxAccess(_C)
if mibBuilder.loadTexts:fsLsppVerbose.setStatus(_A)
class _FsLsppReversePathVerify_Type(TruthValue):defaultValue=2
_FsLsppReversePathVerify_Type.__name__=_G
_FsLsppReversePathVerify_Object=MibTableColumn
fsLsppReversePathVerify=_FsLsppReversePathVerify_Object((1,3,6,1,4,1,10876,101,1,13,11,2,1,1,33),_FsLsppReversePathVerify_Type())
fsLsppReversePathVerify.setMaxAccess(_C)
if mibBuilder.loadTexts:fsLsppReversePathVerify.setStatus(_A)
class _FsLsppEncapType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('mplsIp',1),('mplsAch',2),('mplsAchIp',3),('vccvNegotiated',4)))
_FsLsppEncapType_Type.__name__=_H
_FsLsppEncapType_Object=MibTableColumn
fsLsppEncapType=_FsLsppEncapType_Object((1,3,6,1,4,1,10876,101,1,13,11,2,1,1,34),_FsLsppEncapType_Type())
fsLsppEncapType.setMaxAccess(_C)
if mibBuilder.loadTexts:fsLsppEncapType.setStatus(_A)
class _FsLsppStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('inProgress',1),('success',2),('failure',3)))
_FsLsppStatus_Type.__name__=_H
_FsLsppStatus_Object=MibTableColumn
fsLsppStatus=_FsLsppStatus_Object((1,3,6,1,4,1,10876,101,1,13,11,2,1,1,35),_FsLsppStatus_Type())
fsLsppStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:fsLsppStatus.setStatus(_A)
_FsLsppActualHopCount_Type=Unsigned32
_FsLsppActualHopCount_Object=MibTableColumn
fsLsppActualHopCount=_FsLsppActualHopCount_Object((1,3,6,1,4,1,10876,101,1,13,11,2,1,1,36),_FsLsppActualHopCount_Type())
fsLsppActualHopCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsLsppActualHopCount.setStatus(_A)
_FsLsppResponderAddrType_Type=FsLsppAddressType
_FsLsppResponderAddrType_Object=MibTableColumn
fsLsppResponderAddrType=_FsLsppResponderAddrType_Object((1,3,6,1,4,1,10876,101,1,13,11,2,1,1,37),_FsLsppResponderAddrType_Type())
fsLsppResponderAddrType.setMaxAccess(_B)
if mibBuilder.loadTexts:fsLsppResponderAddrType.setStatus(_A)
class _FsLsppResponderAddr_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,16))
_FsLsppResponderAddr_Type.__name__=_F
_FsLsppResponderAddr_Object=MibTableColumn
fsLsppResponderAddr=_FsLsppResponderAddr_Object((1,3,6,1,4,1,10876,101,1,13,11,2,1,1,38),_FsLsppResponderAddr_Type())
fsLsppResponderAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:fsLsppResponderAddr.setStatus(_A)
_FsLsppResponderGlobalId_Type=Unsigned32
_FsLsppResponderGlobalId_Object=MibTableColumn
fsLsppResponderGlobalId=_FsLsppResponderGlobalId_Object((1,3,6,1,4,1,10876,101,1,13,11,2,1,1,39),_FsLsppResponderGlobalId_Type())
fsLsppResponderGlobalId.setMaxAccess(_B)
if mibBuilder.loadTexts:fsLsppResponderGlobalId.setStatus(_A)
_FsLsppResponderId_Type=Unsigned32
_FsLsppResponderId_Object=MibTableColumn
fsLsppResponderId=_FsLsppResponderId_Object((1,3,6,1,4,1,10876,101,1,13,11,2,1,1,40),_FsLsppResponderId_Type())
fsLsppResponderId.setMaxAccess(_B)
if mibBuilder.loadTexts:fsLsppResponderId.setStatus(_A)
_FsLsppMaxRtt_Type=Unsigned32
_FsLsppMaxRtt_Object=MibTableColumn
fsLsppMaxRtt=_FsLsppMaxRtt_Object((1,3,6,1,4,1,10876,101,1,13,11,2,1,1,41),_FsLsppMaxRtt_Type())
fsLsppMaxRtt.setMaxAccess(_B)
if mibBuilder.loadTexts:fsLsppMaxRtt.setStatus(_A)
_FsLsppMinRtt_Type=Unsigned32
_FsLsppMinRtt_Object=MibTableColumn
fsLsppMinRtt=_FsLsppMinRtt_Object((1,3,6,1,4,1,10876,101,1,13,11,2,1,1,42),_FsLsppMinRtt_Type())
fsLsppMinRtt.setMaxAccess(_B)
if mibBuilder.loadTexts:fsLsppMinRtt.setStatus(_A)
_FsLsppAverageRtt_Type=Unsigned32
_FsLsppAverageRtt_Object=MibTableColumn
fsLsppAverageRtt=_FsLsppAverageRtt_Object((1,3,6,1,4,1,10876,101,1,13,11,2,1,1,43),_FsLsppAverageRtt_Type())
fsLsppAverageRtt.setMaxAccess(_B)
if mibBuilder.loadTexts:fsLsppAverageRtt.setStatus(_A)
_FsLsppPktsTx_Type=Counter32
_FsLsppPktsTx_Object=MibTableColumn
fsLsppPktsTx=_FsLsppPktsTx_Object((1,3,6,1,4,1,10876,101,1,13,11,2,1,1,44),_FsLsppPktsTx_Type())
fsLsppPktsTx.setMaxAccess(_B)
if mibBuilder.loadTexts:fsLsppPktsTx.setStatus(_A)
_FsLsppPktsRx_Type=Counter32
_FsLsppPktsRx_Object=MibTableColumn
fsLsppPktsRx=_FsLsppPktsRx_Object((1,3,6,1,4,1,10876,101,1,13,11,2,1,1,45),_FsLsppPktsRx_Type())
fsLsppPktsRx.setMaxAccess(_B)
if mibBuilder.loadTexts:fsLsppPktsRx.setStatus(_A)
_FsLsppPktsUnSent_Type=Counter32
_FsLsppPktsUnSent_Object=MibTableColumn
fsLsppPktsUnSent=_FsLsppPktsUnSent_Object((1,3,6,1,4,1,10876,101,1,13,11,2,1,1,46),_FsLsppPktsUnSent_Type())
fsLsppPktsUnSent.setMaxAccess(_B)
if mibBuilder.loadTexts:fsLsppPktsUnSent.setStatus(_A)
_FsLsppRowStatus_Type=RowStatus
_FsLsppRowStatus_Object=MibTableColumn
fsLsppRowStatus=_FsLsppRowStatus_Object((1,3,6,1,4,1,10876,101,1,13,11,2,1,1,47),_FsLsppRowStatus_Type())
fsLsppRowStatus.setMaxAccess('read-create')
if mibBuilder.loadTexts:fsLsppRowStatus.setStatus(_A)
class _FsLsppStatusPathDirection_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('forward',1),('reverse',2),('both',3)))
_FsLsppStatusPathDirection_Type.__name__=_H
_FsLsppStatusPathDirection_Object=MibTableColumn
fsLsppStatusPathDirection=_FsLsppStatusPathDirection_Object((1,3,6,1,4,1,10876,101,1,13,11,2,1,1,48),_FsLsppStatusPathDirection_Type())
fsLsppStatusPathDirection.setMaxAccess(_B)
if mibBuilder.loadTexts:fsLsppStatusPathDirection.setStatus(_A)
class _FsLsppResponderIcc_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,6))
_FsLsppResponderIcc_Type.__name__=_F
_FsLsppResponderIcc_Object=MibTableColumn
fsLsppResponderIcc=_FsLsppResponderIcc_Object((1,3,6,1,4,1,10876,101,1,13,11,2,1,1,49),_FsLsppResponderIcc_Type())
fsLsppResponderIcc.setMaxAccess(_B)
if mibBuilder.loadTexts:fsLsppResponderIcc.setStatus(_A)
class _FsLsppResponderUMC_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,7))
_FsLsppResponderUMC_Type.__name__=_F
_FsLsppResponderUMC_Object=MibTableColumn
fsLsppResponderUMC=_FsLsppResponderUMC_Object((1,3,6,1,4,1,10876,101,1,13,11,2,1,1,50),_FsLsppResponderUMC_Type())
fsLsppResponderUMC.setMaxAccess(_B)
if mibBuilder.loadTexts:fsLsppResponderUMC.setStatus(_A)
_FsLsppResponderMepIndex_Type=Unsigned32
_FsLsppResponderMepIndex_Object=MibTableColumn
fsLsppResponderMepIndex=_FsLsppResponderMepIndex_Object((1,3,6,1,4,1,10876,101,1,13,11,2,1,1,51),_FsLsppResponderMepIndex_Type())
fsLsppResponderMepIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:fsLsppResponderMepIndex.setStatus(_A)
_FsLsppEchoSequenceTable_Object=MibTable
fsLsppEchoSequenceTable=_FsLsppEchoSequenceTable_Object((1,3,6,1,4,1,10876,101,1,13,11,2,2))
if mibBuilder.loadTexts:fsLsppEchoSequenceTable.setStatus(_A)
_FsLsppEchoSequenceTableEntry_Object=MibTableRow
fsLsppEchoSequenceTableEntry=_FsLsppEchoSequenceTableEntry_Object((1,3,6,1,4,1,10876,101,1,13,11,2,2,1))
fsLsppEchoSequenceTableEntry.setIndexNames((0,_D,_I),(0,_D,_L),(0,_D,_P))
if mibBuilder.loadTexts:fsLsppEchoSequenceTableEntry.setStatus(_A)
_FsLsppSequenceNumber_Type=Unsigned32
_FsLsppSequenceNumber_Object=MibTableColumn
fsLsppSequenceNumber=_FsLsppSequenceNumber_Object((1,3,6,1,4,1,10876,101,1,13,11,2,2,1,1),_FsLsppSequenceNumber_Type())
fsLsppSequenceNumber.setMaxAccess(_K)
if mibBuilder.loadTexts:fsLsppSequenceNumber.setStatus(_A)
_FsLsppReturnCode_Type=Unsigned32
_FsLsppReturnCode_Object=MibTableColumn
fsLsppReturnCode=_FsLsppReturnCode_Object((1,3,6,1,4,1,10876,101,1,13,11,2,2,1,2),_FsLsppReturnCode_Type())
fsLsppReturnCode.setMaxAccess(_B)
if mibBuilder.loadTexts:fsLsppReturnCode.setStatus(_A)
_FsLsppReturnSubCode_Type=Unsigned32
_FsLsppReturnSubCode_Object=MibTableColumn
fsLsppReturnSubCode=_FsLsppReturnSubCode_Object((1,3,6,1,4,1,10876,101,1,13,11,2,2,1,3),_FsLsppReturnSubCode_Type())
fsLsppReturnSubCode.setMaxAccess(_B)
if mibBuilder.loadTexts:fsLsppReturnSubCode.setStatus(_A)
class _FsLsppReturnCodeStr_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,128))
_FsLsppReturnCodeStr_Type.__name__=_F
_FsLsppReturnCodeStr_Object=MibTableColumn
fsLsppReturnCodeStr=_FsLsppReturnCodeStr_Object((1,3,6,1,4,1,10876,101,1,13,11,2,2,1,4),_FsLsppReturnCodeStr_Type())
fsLsppReturnCodeStr.setMaxAccess(_B)
if mibBuilder.loadTexts:fsLsppReturnCodeStr.setStatus(_A)
_FsLsppHopTable_Object=MibTable
fsLsppHopTable=_FsLsppHopTable_Object((1,3,6,1,4,1,10876,101,1,13,11,2,3))
if mibBuilder.loadTexts:fsLsppHopTable.setStatus(_A)
_FsLsppHopTableEntry_Object=MibTableRow
fsLsppHopTableEntry=_FsLsppHopTableEntry_Object((1,3,6,1,4,1,10876,101,1,13,11,2,3,1))
fsLsppHopTableEntry.setIndexNames((0,_D,_I),(0,_D,_L),(0,_D,_Q))
if mibBuilder.loadTexts:fsLsppHopTableEntry.setStatus(_A)
_FsLsppHopIndex_Type=Unsigned32
_FsLsppHopIndex_Object=MibTableColumn
fsLsppHopIndex=_FsLsppHopIndex_Object((1,3,6,1,4,1,10876,101,1,13,11,2,3,1,1),_FsLsppHopIndex_Type())
fsLsppHopIndex.setMaxAccess(_K)
if mibBuilder.loadTexts:fsLsppHopIndex.setStatus(_A)
_FsLsppHopAddrType_Type=FsLsppAddressType
_FsLsppHopAddrType_Object=MibTableColumn
fsLsppHopAddrType=_FsLsppHopAddrType_Object((1,3,6,1,4,1,10876,101,1,13,11,2,3,1,2),_FsLsppHopAddrType_Type())
fsLsppHopAddrType.setMaxAccess(_B)
if mibBuilder.loadTexts:fsLsppHopAddrType.setStatus(_A)
class _FsLsppHopAddr_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,16))
_FsLsppHopAddr_Type.__name__=_F
_FsLsppHopAddr_Object=MibTableColumn
fsLsppHopAddr=_FsLsppHopAddr_Object((1,3,6,1,4,1,10876,101,1,13,11,2,3,1,3),_FsLsppHopAddr_Type())
fsLsppHopAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:fsLsppHopAddr.setStatus(_A)
_FsLsppHopGlobalId_Type=Unsigned32
_FsLsppHopGlobalId_Object=MibTableColumn
fsLsppHopGlobalId=_FsLsppHopGlobalId_Object((1,3,6,1,4,1,10876,101,1,13,11,2,3,1,4),_FsLsppHopGlobalId_Type())
fsLsppHopGlobalId.setMaxAccess(_B)
if mibBuilder.loadTexts:fsLsppHopGlobalId.setStatus(_A)
_FsLsppHopId_Type=Unsigned32
_FsLsppHopId_Object=MibTableColumn
fsLsppHopId=_FsLsppHopId_Object((1,3,6,1,4,1,10876,101,1,13,11,2,3,1,5),_FsLsppHopId_Type())
fsLsppHopId.setMaxAccess(_B)
if mibBuilder.loadTexts:fsLsppHopId.setStatus(_A)
_FsLsppHopIfNum_Type=Unsigned32
_FsLsppHopIfNum_Object=MibTableColumn
fsLsppHopIfNum=_FsLsppHopIfNum_Object((1,3,6,1,4,1,10876,101,1,13,11,2,3,1,6),_FsLsppHopIfNum_Type())
fsLsppHopIfNum.setMaxAccess(_B)
if mibBuilder.loadTexts:fsLsppHopIfNum.setStatus(_A)
_FsLsppHopReturnCode_Type=Unsigned32
_FsLsppHopReturnCode_Object=MibTableColumn
fsLsppHopReturnCode=_FsLsppHopReturnCode_Object((1,3,6,1,4,1,10876,101,1,13,11,2,3,1,7),_FsLsppHopReturnCode_Type())
fsLsppHopReturnCode.setMaxAccess(_B)
if mibBuilder.loadTexts:fsLsppHopReturnCode.setStatus(_A)
_FsLsppHopReturnSubCode_Type=Unsigned32
_FsLsppHopReturnSubCode_Object=MibTableColumn
fsLsppHopReturnSubCode=_FsLsppHopReturnSubCode_Object((1,3,6,1,4,1,10876,101,1,13,11,2,3,1,8),_FsLsppHopReturnSubCode_Type())
fsLsppHopReturnSubCode.setMaxAccess(_B)
if mibBuilder.loadTexts:fsLsppHopReturnSubCode.setStatus(_A)
class _FsLsppHopReturnCodeStr_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,128))
_FsLsppHopReturnCodeStr_Type.__name__=_F
_FsLsppHopReturnCodeStr_Object=MibTableColumn
fsLsppHopReturnCodeStr=_FsLsppHopReturnCodeStr_Object((1,3,6,1,4,1,10876,101,1,13,11,2,3,1,9),_FsLsppHopReturnCodeStr_Type())
fsLsppHopReturnCodeStr.setMaxAccess(_B)
if mibBuilder.loadTexts:fsLsppHopReturnCodeStr.setStatus(_A)
_FsLsppHopRxAddrType_Type=FsLsppAddressType
_FsLsppHopRxAddrType_Object=MibTableColumn
fsLsppHopRxAddrType=_FsLsppHopRxAddrType_Object((1,3,6,1,4,1,10876,101,1,13,11,2,3,1,10),_FsLsppHopRxAddrType_Type())
fsLsppHopRxAddrType.setMaxAccess(_B)
if mibBuilder.loadTexts:fsLsppHopRxAddrType.setStatus(_A)
class _FsLsppHopRxIPAddr_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,16))
_FsLsppHopRxIPAddr_Type.__name__=_F
_FsLsppHopRxIPAddr_Object=MibTableColumn
fsLsppHopRxIPAddr=_FsLsppHopRxIPAddr_Object((1,3,6,1,4,1,10876,101,1,13,11,2,3,1,11),_FsLsppHopRxIPAddr_Type())
fsLsppHopRxIPAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:fsLsppHopRxIPAddr.setStatus(_A)
class _FsLsppHopRxIfAddr_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,16))
_FsLsppHopRxIfAddr_Type.__name__=_F
_FsLsppHopRxIfAddr_Object=MibTableColumn
fsLsppHopRxIfAddr=_FsLsppHopRxIfAddr_Object((1,3,6,1,4,1,10876,101,1,13,11,2,3,1,12),_FsLsppHopRxIfAddr_Type())
fsLsppHopRxIfAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:fsLsppHopRxIfAddr.setStatus(_A)
_FsLsppHopRxIfNum_Type=Unsigned32
_FsLsppHopRxIfNum_Object=MibTableColumn
fsLsppHopRxIfNum=_FsLsppHopRxIfNum_Object((1,3,6,1,4,1,10876,101,1,13,11,2,3,1,13),_FsLsppHopRxIfNum_Type())
fsLsppHopRxIfNum.setMaxAccess(_B)
if mibBuilder.loadTexts:fsLsppHopRxIfNum.setStatus(_A)
_FsLsppHopRxLabelStack_Type=OctetString
_FsLsppHopRxLabelStack_Object=MibTableColumn
fsLsppHopRxLabelStack=_FsLsppHopRxLabelStack_Object((1,3,6,1,4,1,10876,101,1,13,11,2,3,1,14),_FsLsppHopRxLabelStack_Type())
fsLsppHopRxLabelStack.setMaxAccess(_B)
if mibBuilder.loadTexts:fsLsppHopRxLabelStack.setStatus(_A)
_FsLsppHopRxLabelExp_Type=OctetString
_FsLsppHopRxLabelExp_Object=MibTableColumn
fsLsppHopRxLabelExp=_FsLsppHopRxLabelExp_Object((1,3,6,1,4,1,10876,101,1,13,11,2,3,1,15),_FsLsppHopRxLabelExp_Type())
fsLsppHopRxLabelExp.setMaxAccess(_B)
if mibBuilder.loadTexts:fsLsppHopRxLabelExp.setStatus(_A)
_FsLsppHopRtt_Type=Unsigned32
_FsLsppHopRtt_Object=MibTableColumn
fsLsppHopRtt=_FsLsppHopRtt_Object((1,3,6,1,4,1,10876,101,1,13,11,2,3,1,16),_FsLsppHopRtt_Type())
fsLsppHopRtt.setMaxAccess(_B)
if mibBuilder.loadTexts:fsLsppHopRtt.setStatus(_A)
_FsLsppHopDsMtu_Type=Unsigned32
_FsLsppHopDsMtu_Object=MibTableColumn
fsLsppHopDsMtu=_FsLsppHopDsMtu_Object((1,3,6,1,4,1,10876,101,1,13,11,2,3,1,17),_FsLsppHopDsMtu_Type())
fsLsppHopDsMtu.setMaxAccess(_B)
if mibBuilder.loadTexts:fsLsppHopDsMtu.setStatus(_A)
_FsLsppHopDsAddrType_Type=FsLsppAddressType
_FsLsppHopDsAddrType_Object=MibTableColumn
fsLsppHopDsAddrType=_FsLsppHopDsAddrType_Object((1,3,6,1,4,1,10876,101,1,13,11,2,3,1,18),_FsLsppHopDsAddrType_Type())
fsLsppHopDsAddrType.setMaxAccess(_B)
if mibBuilder.loadTexts:fsLsppHopDsAddrType.setStatus(_A)
class _FsLsppHopDsIPAddr_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,16))
_FsLsppHopDsIPAddr_Type.__name__=_F
_FsLsppHopDsIPAddr_Object=MibTableColumn
fsLsppHopDsIPAddr=_FsLsppHopDsIPAddr_Object((1,3,6,1,4,1,10876,101,1,13,11,2,3,1,19),_FsLsppHopDsIPAddr_Type())
fsLsppHopDsIPAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:fsLsppHopDsIPAddr.setStatus(_A)
class _FsLsppHopDsIfAddr_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,16))
_FsLsppHopDsIfAddr_Type.__name__=_F
_FsLsppHopDsIfAddr_Object=MibTableColumn
fsLsppHopDsIfAddr=_FsLsppHopDsIfAddr_Object((1,3,6,1,4,1,10876,101,1,13,11,2,3,1,20),_FsLsppHopDsIfAddr_Type())
fsLsppHopDsIfAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:fsLsppHopDsIfAddr.setStatus(_A)
_FsLsppHopDsIfNum_Type=Unsigned32
_FsLsppHopDsIfNum_Object=MibTableColumn
fsLsppHopDsIfNum=_FsLsppHopDsIfNum_Object((1,3,6,1,4,1,10876,101,1,13,11,2,3,1,21),_FsLsppHopDsIfNum_Type())
fsLsppHopDsIfNum.setMaxAccess(_B)
if mibBuilder.loadTexts:fsLsppHopDsIfNum.setStatus(_A)
_FsLsppHopDsLabelStack_Type=OctetString
_FsLsppHopDsLabelStack_Object=MibTableColumn
fsLsppHopDsLabelStack=_FsLsppHopDsLabelStack_Object((1,3,6,1,4,1,10876,101,1,13,11,2,3,1,22),_FsLsppHopDsLabelStack_Type())
fsLsppHopDsLabelStack.setMaxAccess(_B)
if mibBuilder.loadTexts:fsLsppHopDsLabelStack.setStatus(_A)
_FsLsppHopDsLabelExp_Type=OctetString
_FsLsppHopDsLabelExp_Object=MibTableColumn
fsLsppHopDsLabelExp=_FsLsppHopDsLabelExp_Object((1,3,6,1,4,1,10876,101,1,13,11,2,3,1,23),_FsLsppHopDsLabelExp_Type())
fsLsppHopDsLabelExp.setMaxAccess(_B)
if mibBuilder.loadTexts:fsLsppHopDsLabelExp.setStatus(_A)
class _FsLsppHopIcc_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,6))
_FsLsppHopIcc_Type.__name__=_F
_FsLsppHopIcc_Object=MibTableColumn
fsLsppHopIcc=_FsLsppHopIcc_Object((1,3,6,1,4,1,10876,101,1,13,11,2,3,1,24),_FsLsppHopIcc_Type())
fsLsppHopIcc.setMaxAccess(_B)
if mibBuilder.loadTexts:fsLsppHopIcc.setStatus(_A)
class _FsLsppHopUMC_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,7))
_FsLsppHopUMC_Type.__name__=_F
_FsLsppHopUMC_Object=MibTableColumn
fsLsppHopUMC=_FsLsppHopUMC_Object((1,3,6,1,4,1,10876,101,1,13,11,2,3,1,25),_FsLsppHopUMC_Type())
fsLsppHopUMC.setMaxAccess(_B)
if mibBuilder.loadTexts:fsLsppHopUMC.setStatus(_A)
_FsLsppHopMepIndex_Type=Unsigned32
_FsLsppHopMepIndex_Object=MibTableColumn
fsLsppHopMepIndex=_FsLsppHopMepIndex_Object((1,3,6,1,4,1,10876,101,1,13,11,2,3,1,26),_FsLsppHopMepIndex_Type())
fsLsppHopMepIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:fsLsppHopMepIndex.setStatus(_A)
_FsLsppNotifications_ObjectIdentity=ObjectIdentity
fsLsppNotifications=_FsLsppNotifications_ObjectIdentity((1,3,6,1,4,1,10876,101,1,13,11,3))
_FsLsppTraps_ObjectIdentity=ObjectIdentity
fsLsppTraps=_FsLsppTraps_ObjectIdentity((1,3,6,1,4,1,10876,101,1,13,11,3,0))
class _FsLsppTrapContextName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_FsLsppTrapContextName_Type.__name__=_O
_FsLsppTrapContextName_Object=MibScalar
fsLsppTrapContextName=_FsLsppTrapContextName_Object((1,3,6,1,4,1,10876,101,1,13,11,3,1),_FsLsppTrapContextName_Type())
fsLsppTrapContextName.setMaxAccess('accessible-for-notify')
if mibBuilder.loadTexts:fsLsppTrapContextName.setStatus(_A)
fsLsppPingCompletionTrap=NotificationType((1,3,6,1,4,1,10876,101,1,13,11,3,0,1))
fsLsppPingCompletionTrap.setObjects(*((_D,_M),(_D,_N)))
if mibBuilder.loadTexts:fsLsppPingCompletionTrap.setStatus(_A)
fsLsppTraceRouteTrap=NotificationType((1,3,6,1,4,1,10876,101,1,13,11,3,0,2))
fsLsppTraceRouteTrap.setObjects(*((_D,_M),(_D,_N),(_D,_R)))
if mibBuilder.loadTexts:fsLsppTraceRouteTrap.setStatus(_A)
fsLsppBFDBootstrapReqRcvdTrap=NotificationType((1,3,6,1,4,1,10876,101,1,13,11,3,0,3))
fsLsppBFDBootstrapReqRcvdTrap.setObjects(*((_D,_M),(_D,_S)))
if mibBuilder.loadTexts:fsLsppBFDBootstrapReqRcvdTrap.setStatus(_A)
mibBuilder.exportSymbols(_D,**{_J:FsLsppTimeUnit,'FsLsppAddressType':FsLsppAddressType,'fsLspp':fsLspp,'fsLsppGlobals':fsLsppGlobals,'fsLsppGlobalConfigTable':fsLsppGlobalConfigTable,'fsLsppGlobalConfigTableEntry':fsLsppGlobalConfigTableEntry,_I:fsLsppContextId,'fsLsppSystemControl':fsLsppSystemControl,'fsLsppTrapStatus':fsLsppTrapStatus,'fsLsppTraceLevel':fsLsppTraceLevel,'fsLsppAgeOutTime':fsLsppAgeOutTime,'fsLsppAgeOutTmrUnit':fsLsppAgeOutTmrUnit,'fsLsppClearEchoStats':fsLsppClearEchoStats,'fsLsppBfdBtStrapRespReq':fsLsppBfdBtStrapRespReq,'fsLsppBfdBtStrapAgeOutTime':fsLsppBfdBtStrapAgeOutTime,'fsLsppBfdBtStrapAgeOutTmrUnit':fsLsppBfdBtStrapAgeOutTmrUnit,'fsLsppGlobalStatsTable':fsLsppGlobalStatsTable,'fsLsppGlobalStatsTableEntry':fsLsppGlobalStatsTableEntry,'fsLsppGlbStatReqTx':fsLsppGlbStatReqTx,'fsLsppGlbStatReqRx':fsLsppGlbStatReqRx,'fsLsppGlbStatReqTimedOut':fsLsppGlbStatReqTimedOut,'fsLsppGlbStatReqUnSent':fsLsppGlbStatReqUnSent,'fsLsppGlbStatReplyTx':fsLsppGlbStatReplyTx,'fsLsppGlbStatReplyRx':fsLsppGlbStatReplyRx,'fsLsppGlbStatReplyDropped':fsLsppGlbStatReplyDropped,'fsLsppGlbStatReplyUnSent':fsLsppGlbStatReplyUnSent,'fsLsppGlbStatReplyFromEgr':fsLsppGlbStatReplyFromEgr,'fsLsppGlbStatUnLbldOutIf':fsLsppGlbStatUnLbldOutIf,'fsLsppGlbStatDsMapMismatch':fsLsppGlbStatDsMapMismatch,'fsLsppGlbStatFecLblMismatch':fsLsppGlbStatFecLblMismatch,'fsLsppGlbStatNoFecMapping':fsLsppGlbStatNoFecMapping,'fsLsppGlbStatUnKUpstreamIf':fsLsppGlbStatUnKUpstreamIf,'fsLsppGlbStatReqLblSwitched':fsLsppGlbStatReqLblSwitched,'fsLsppGlbStatReqUnSupptdTlv':fsLsppGlbStatReqUnSupptdTlv,'fsLsppGlbStatMalformedReq':fsLsppGlbStatMalformedReq,'fsLsppGlbStatNoLblEntry':fsLsppGlbStatNoLblEntry,'fsLsppGlbStatPreTermReq':fsLsppGlbStatPreTermReq,'fsLsppGlbStatProtMismatch':fsLsppGlbStatProtMismatch,'fsLsppGlbStatRsvdRetCode':fsLsppGlbStatRsvdRetCode,'fsLsppGlbStatNoRetCode':fsLsppGlbStatNoRetCode,'fsLsppGlbStatUndefRetCode':fsLsppGlbStatUndefRetCode,'fsLsppGlbStatInvalidPktDropped':fsLsppGlbStatInvalidPktDropped,'fsLsppPingTrace':fsLsppPingTrace,'fsLsppPingTraceTable':fsLsppPingTraceTable,'fsLsppPingTraceTableEntry':fsLsppPingTraceTableEntry,_L:fsLsppSenderHandle,'fsLsppRequestType':fsLsppRequestType,_S:fsLsppRequestOwner,'fsLsppPathType':fsLsppPathType,'fsLsppPathPointer':fsLsppPathPointer,'fsLsppTgtMipGlobalId':fsLsppTgtMipGlobalId,'fsLsppTgtMipNodeId':fsLsppTgtMipNodeId,'fsLsppTgtMipIfNum':fsLsppTgtMipIfNum,'fsLsppReplyMode':fsLsppReplyMode,'fsLsppRepeatCount':fsLsppRepeatCount,'fsLsppPacketSize':fsLsppPacketSize,'fsLsppPadPattern':fsLsppPadPattern,'fsLsppTTLValue':fsLsppTTLValue,'fsLsppWFRInterval':fsLsppWFRInterval,'fsLsppWFRTmrUnit':fsLsppWFRTmrUnit,'fsLsppWTSInterval':fsLsppWTSInterval,'fsLsppWTSTmrUnit':fsLsppWTSTmrUnit,'fsLsppReplyDscpValue':fsLsppReplyDscpValue,'fsLsppSweepOption':fsLsppSweepOption,'fsLsppSweepMinimum':fsLsppSweepMinimum,'fsLsppSweepMaximum':fsLsppSweepMaximum,'fsLsppSweepIncrement':fsLsppSweepIncrement,'fsLsppBurstOption':fsLsppBurstOption,'fsLsppBurstSize':fsLsppBurstSize,'fsLsppEXPValue':fsLsppEXPValue,'fsLsppDsMap':fsLsppDsMap,'fsLsppFecValidate':fsLsppFecValidate,'fsLsppReplyPadTlv':fsLsppReplyPadTlv,'fsLsppForceExplicitNull':fsLsppForceExplicitNull,'fsLsppInterfaceLabelTlv':fsLsppInterfaceLabelTlv,'fsLsppSameSeqNumOption':fsLsppSameSeqNumOption,'fsLsppVerbose':fsLsppVerbose,'fsLsppReversePathVerify':fsLsppReversePathVerify,'fsLsppEncapType':fsLsppEncapType,_N:fsLsppStatus,_R:fsLsppActualHopCount,'fsLsppResponderAddrType':fsLsppResponderAddrType,'fsLsppResponderAddr':fsLsppResponderAddr,'fsLsppResponderGlobalId':fsLsppResponderGlobalId,'fsLsppResponderId':fsLsppResponderId,'fsLsppMaxRtt':fsLsppMaxRtt,'fsLsppMinRtt':fsLsppMinRtt,'fsLsppAverageRtt':fsLsppAverageRtt,'fsLsppPktsTx':fsLsppPktsTx,'fsLsppPktsRx':fsLsppPktsRx,'fsLsppPktsUnSent':fsLsppPktsUnSent,'fsLsppRowStatus':fsLsppRowStatus,'fsLsppStatusPathDirection':fsLsppStatusPathDirection,'fsLsppResponderIcc':fsLsppResponderIcc,'fsLsppResponderUMC':fsLsppResponderUMC,'fsLsppResponderMepIndex':fsLsppResponderMepIndex,'fsLsppEchoSequenceTable':fsLsppEchoSequenceTable,'fsLsppEchoSequenceTableEntry':fsLsppEchoSequenceTableEntry,_P:fsLsppSequenceNumber,'fsLsppReturnCode':fsLsppReturnCode,'fsLsppReturnSubCode':fsLsppReturnSubCode,'fsLsppReturnCodeStr':fsLsppReturnCodeStr,'fsLsppHopTable':fsLsppHopTable,'fsLsppHopTableEntry':fsLsppHopTableEntry,_Q:fsLsppHopIndex,'fsLsppHopAddrType':fsLsppHopAddrType,'fsLsppHopAddr':fsLsppHopAddr,'fsLsppHopGlobalId':fsLsppHopGlobalId,'fsLsppHopId':fsLsppHopId,'fsLsppHopIfNum':fsLsppHopIfNum,'fsLsppHopReturnCode':fsLsppHopReturnCode,'fsLsppHopReturnSubCode':fsLsppHopReturnSubCode,'fsLsppHopReturnCodeStr':fsLsppHopReturnCodeStr,'fsLsppHopRxAddrType':fsLsppHopRxAddrType,'fsLsppHopRxIPAddr':fsLsppHopRxIPAddr,'fsLsppHopRxIfAddr':fsLsppHopRxIfAddr,'fsLsppHopRxIfNum':fsLsppHopRxIfNum,'fsLsppHopRxLabelStack':fsLsppHopRxLabelStack,'fsLsppHopRxLabelExp':fsLsppHopRxLabelExp,'fsLsppHopRtt':fsLsppHopRtt,'fsLsppHopDsMtu':fsLsppHopDsMtu,'fsLsppHopDsAddrType':fsLsppHopDsAddrType,'fsLsppHopDsIPAddr':fsLsppHopDsIPAddr,'fsLsppHopDsIfAddr':fsLsppHopDsIfAddr,'fsLsppHopDsIfNum':fsLsppHopDsIfNum,'fsLsppHopDsLabelStack':fsLsppHopDsLabelStack,'fsLsppHopDsLabelExp':fsLsppHopDsLabelExp,'fsLsppHopIcc':fsLsppHopIcc,'fsLsppHopUMC':fsLsppHopUMC,'fsLsppHopMepIndex':fsLsppHopMepIndex,'fsLsppNotifications':fsLsppNotifications,'fsLsppTraps':fsLsppTraps,'fsLsppPingCompletionTrap':fsLsppPingCompletionTrap,'fsLsppTraceRouteTrap':fsLsppTraceRouteTrap,'fsLsppBFDBootstrapReqRcvdTrap':fsLsppBFDBootstrapReqRcvdTrap,_M:fsLsppTrapContextName})