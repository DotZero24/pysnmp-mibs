_AF='dtpCtpGroup'
_AE='dtpCtpCrossConnectType'
_AD='dtpCtpPmHistStatsEnable'
_AC='dtpCtpMuxMode'
_AB='dtpCtpNumDtpSubCh'
_AA='dtpCtpPrbsMonitoringMode'
_A9='dtpCtpPrbsGenerationMode'
_A8='dtpCtpDtpTxUasDayTceReporting'
_A7='dtpCtpDtpTxSesDayTceReporting'
_A6='dtpCtpDtpTxEsDayTceReporting'
_A5='dtpCtpDtpTxCvDayTceReporting'
_A4='dtpCtpDtpTxUas15MinutesTceReporting'
_A3='dtpCtpDtpTxSes15MinutesTceReporting'
_A2='dtpCtpDtpTxEs15MinutesTceReporting'
_A1='dtpCtpDtpTxCv15MinutesTceReporting'
_A0='dtpCtpDtpRxUasDayTceReporting'
_z='dtpCtpDtpRxSesDayTceReporting'
_y='dtpCtpDtpRxEsDayTceReporting'
_x='dtpCtpDtpRxCvDayTceReporting'
_w='dtpCtpDtpRxUas15MinutesTceReporting'
_v='dtpCtpDtpRxSes15MinutesTceReporting'
_u='dtpCtpDtpRxEs15MinutesTceReporting'
_t='dtpCtpDtpRxCv15MinutesTceReporting'
_s='dtpCtpDtpTxUasDayTce'
_r='dtpCtpDtpTxSesDayTce'
_q='dtpCtpDtpTxEsDayTce'
_p='dtpCtpDtpTxCvDayTce'
_o='dtpCtpDtpTxUas15MinutesTce'
_n='dtpCtpDtpTxSes15MinutesTce'
_m='dtpCtpDtpTxEs15MinutesTce'
_l='dtpCtpDtpTxCv15MinutesTce'
_k='dtpCtpDtpRxUasDayTce'
_j='dtpCtpDtpRxSesDayTce'
_i='dtpCtpDtpRxEsDayTce'
_h='dtpCtpDtpRxCvDayTce'
_g='dtpCtpDtpRxUas15MinutesTce'
_f='dtpCtpDtpRxSes15MinutesTce'
_e='dtpCtpDtpRxEs15MinutesTce'
_d='dtpCtpDtpRxCv15MinutesTce'
_c='dtpCtpRecvTxDtpTti'
_b='dtpCtpRxDtpTti'
_a='dtpCtpExpectedTxDtpTti'
_Z='dtpCtpExpectedDtpTti'
_Y='dtpCtpRxDtpTtiWrite'
_X='dtpCtpTxDtpTti'
_W='dtpCtpTxTtiAlarmReporting'
_V='dtpCtpTtiAlarmReporting'
_U='dtpCtpInsertDtpTti'
_T='dtpCtpLoopback'
_S='dtpCtpDataRate'
_R='dtpCtpDetectedPayload'
_Q='dtpCtpSupportingCircuitIdList'
_P='dtpCtpExpectedPayload'
_O='dtpCtpSupportingTP'
_N='dtpCtpSwReason'
_M='dtpCtpProtMod'
_L='dtpCtpCfgProtSt'
_K='ifIndex'
_J='IF-MIB'
_I='none'
_H='enabled'
_G='disabled'
_F='read-only'
_E='TruthValue'
_D='Integer32'
_C='read-write'
_B='INFINERA-TP-DTPCTP-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_J,_K)
terminationPoint,=mibBuilder.importSymbols('INFINERA-REG-MIB','terminationPoint')
InfnServiceType,=mibBuilder.importSymbols('INFINERA-TC-MIB','InfnServiceType')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention',_E)
dtpCtpMIB=ModuleIdentity((1,3,6,1,4,1,21296,2,2,2,2,7))
if mibBuilder.loadTexts:dtpCtpMIB.setRevisions(('2008-10-20 00:00',))
_DtpCtpTable_Object=MibTable
dtpCtpTable=_DtpCtpTable_Object((1,3,6,1,4,1,21296,2,2,2,2,7,1))
if mibBuilder.loadTexts:dtpCtpTable.setStatus(_A)
_DtpCtpEntry_Object=MibTableRow
dtpCtpEntry=_DtpCtpEntry_Object((1,3,6,1,4,1,21296,2,2,2,2,7,1,1))
dtpCtpEntry.setIndexNames((0,_J,_K))
if mibBuilder.loadTexts:dtpCtpEntry.setStatus(_A)
class _DtpCtpCfgProtSt_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('unknown',1),('wrk',2),('prot',3),('relb',4),('pU',5)))
_DtpCtpCfgProtSt_Type.__name__=_D
_DtpCtpCfgProtSt_Object=MibTableColumn
dtpCtpCfgProtSt=_DtpCtpCfgProtSt_Object((1,3,6,1,4,1,21296,2,2,2,2,7,1,1,1),_DtpCtpCfgProtSt_Type())
dtpCtpCfgProtSt.setMaxAccess(_F)
if mibBuilder.loadTexts:dtpCtpCfgProtSt.setStatus(_A)
class _DtpCtpProtMod_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_I,1),('dtDSNCP',2),('stDSNCP',3)))
_DtpCtpProtMod_Type.__name__=_D
_DtpCtpProtMod_Object=MibTableColumn
dtpCtpProtMod=_DtpCtpProtMod_Object((1,3,6,1,4,1,21296,2,2,2,2,7,1,1,2),_DtpCtpProtMod_Type())
dtpCtpProtMod.setMaxAccess(_F)
if mibBuilder.loadTexts:dtpCtpProtMod.setStatus(_A)
class _DtpCtpSwReason_Type(Integer32):defaultValue=6;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15)));namedValues=NamedValues(*(('mSwP',1),('mSwW',2),('wLck',3),('pLck',4),('auto',5),(_I,6),('revert',7),('admLck',8),('unProv',9),('eqFlt',10),('liFlt',11),('liSF',12),('clRxFlt',13),('clTxFlt',14),('sysLof',15)))
_DtpCtpSwReason_Type.__name__=_D
_DtpCtpSwReason_Object=MibTableColumn
dtpCtpSwReason=_DtpCtpSwReason_Object((1,3,6,1,4,1,21296,2,2,2,2,7,1,1,3),_DtpCtpSwReason_Type())
dtpCtpSwReason.setMaxAccess(_F)
if mibBuilder.loadTexts:dtpCtpSwReason.setStatus(_A)
_DtpCtpSupportingTP_Type=DisplayString
_DtpCtpSupportingTP_Object=MibTableColumn
dtpCtpSupportingTP=_DtpCtpSupportingTP_Object((1,3,6,1,4,1,21296,2,2,2,2,7,1,1,4),_DtpCtpSupportingTP_Type())
dtpCtpSupportingTP.setMaxAccess(_C)
if mibBuilder.loadTexts:dtpCtpSupportingTP.setStatus(_A)
_DtpCtpExpectedPayload_Type=InfnServiceType
_DtpCtpExpectedPayload_Object=MibTableColumn
dtpCtpExpectedPayload=_DtpCtpExpectedPayload_Object((1,3,6,1,4,1,21296,2,2,2,2,7,1,1,5),_DtpCtpExpectedPayload_Type())
dtpCtpExpectedPayload.setMaxAccess(_F)
if mibBuilder.loadTexts:dtpCtpExpectedPayload.setStatus(_A)
_DtpCtpSupportingCircuitIdList_Type=DisplayString
_DtpCtpSupportingCircuitIdList_Object=MibTableColumn
dtpCtpSupportingCircuitIdList=_DtpCtpSupportingCircuitIdList_Object((1,3,6,1,4,1,21296,2,2,2,2,7,1,1,6),_DtpCtpSupportingCircuitIdList_Type())
dtpCtpSupportingCircuitIdList.setMaxAccess(_F)
if mibBuilder.loadTexts:dtpCtpSupportingCircuitIdList.setStatus(_A)
_DtpCtpDetectedPayload_Type=InfnServiceType
_DtpCtpDetectedPayload_Object=MibTableColumn
dtpCtpDetectedPayload=_DtpCtpDetectedPayload_Object((1,3,6,1,4,1,21296,2,2,2,2,7,1,1,7),_DtpCtpDetectedPayload_Type())
dtpCtpDetectedPayload.setMaxAccess(_F)
if mibBuilder.loadTexts:dtpCtpDetectedPayload.setStatus(_A)
class _DtpCtpDataRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('rateNotSet',1),('rate10GigAny',2),('rate2g500mAny',3),('rate1GogAny',4),('rate40GigAny',5)))
_DtpCtpDataRate_Type.__name__=_D
_DtpCtpDataRate_Object=MibTableColumn
dtpCtpDataRate=_DtpCtpDataRate_Object((1,3,6,1,4,1,21296,2,2,2,2,7,1,1,8),_DtpCtpDataRate_Type())
dtpCtpDataRate.setMaxAccess(_F)
if mibBuilder.loadTexts:dtpCtpDataRate.setStatus(_A)
class _DtpCtpLoopback_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_I,1),('terminal',2),('facility',3)))
_DtpCtpLoopback_Type.__name__=_D
_DtpCtpLoopback_Object=MibTableColumn
dtpCtpLoopback=_DtpCtpLoopback_Object((1,3,6,1,4,1,21296,2,2,2,2,7,1,1,9),_DtpCtpLoopback_Type())
dtpCtpLoopback.setMaxAccess(_C)
if mibBuilder.loadTexts:dtpCtpLoopback.setStatus(_A)
class _DtpCtpInsertDtpTti_Type(TruthValue):defaultValue=2
_DtpCtpInsertDtpTti_Type.__name__=_E
_DtpCtpInsertDtpTti_Object=MibTableColumn
dtpCtpInsertDtpTti=_DtpCtpInsertDtpTti_Object((1,3,6,1,4,1,21296,2,2,2,2,7,1,1,10),_DtpCtpInsertDtpTti_Type())
dtpCtpInsertDtpTti.setMaxAccess(_C)
if mibBuilder.loadTexts:dtpCtpInsertDtpTti.setStatus(_A)
class _DtpCtpTtiAlarmReporting_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_DtpCtpTtiAlarmReporting_Type.__name__=_D
_DtpCtpTtiAlarmReporting_Object=MibTableColumn
dtpCtpTtiAlarmReporting=_DtpCtpTtiAlarmReporting_Object((1,3,6,1,4,1,21296,2,2,2,2,7,1,1,11),_DtpCtpTtiAlarmReporting_Type())
dtpCtpTtiAlarmReporting.setMaxAccess(_C)
if mibBuilder.loadTexts:dtpCtpTtiAlarmReporting.setStatus(_A)
class _DtpCtpTxTtiAlarmReporting_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_DtpCtpTxTtiAlarmReporting_Type.__name__=_D
_DtpCtpTxTtiAlarmReporting_Object=MibTableColumn
dtpCtpTxTtiAlarmReporting=_DtpCtpTxTtiAlarmReporting_Object((1,3,6,1,4,1,21296,2,2,2,2,7,1,1,12),_DtpCtpTxTtiAlarmReporting_Type())
dtpCtpTxTtiAlarmReporting.setMaxAccess(_C)
if mibBuilder.loadTexts:dtpCtpTxTtiAlarmReporting.setStatus(_A)
_DtpCtpTxDtpTti_Type=DisplayString
_DtpCtpTxDtpTti_Object=MibTableColumn
dtpCtpTxDtpTti=_DtpCtpTxDtpTti_Object((1,3,6,1,4,1,21296,2,2,2,2,7,1,1,13),_DtpCtpTxDtpTti_Type())
dtpCtpTxDtpTti.setMaxAccess(_C)
if mibBuilder.loadTexts:dtpCtpTxDtpTti.setStatus(_A)
_DtpCtpRxDtpTtiWrite_Type=DisplayString
_DtpCtpRxDtpTtiWrite_Object=MibTableColumn
dtpCtpRxDtpTtiWrite=_DtpCtpRxDtpTtiWrite_Object((1,3,6,1,4,1,21296,2,2,2,2,7,1,1,14),_DtpCtpRxDtpTtiWrite_Type())
dtpCtpRxDtpTtiWrite.setMaxAccess(_C)
if mibBuilder.loadTexts:dtpCtpRxDtpTtiWrite.setStatus(_A)
_DtpCtpExpectedDtpTti_Type=DisplayString
_DtpCtpExpectedDtpTti_Object=MibTableColumn
dtpCtpExpectedDtpTti=_DtpCtpExpectedDtpTti_Object((1,3,6,1,4,1,21296,2,2,2,2,7,1,1,15),_DtpCtpExpectedDtpTti_Type())
dtpCtpExpectedDtpTti.setMaxAccess(_C)
if mibBuilder.loadTexts:dtpCtpExpectedDtpTti.setStatus(_A)
_DtpCtpExpectedTxDtpTti_Type=DisplayString
_DtpCtpExpectedTxDtpTti_Object=MibTableColumn
dtpCtpExpectedTxDtpTti=_DtpCtpExpectedTxDtpTti_Object((1,3,6,1,4,1,21296,2,2,2,2,7,1,1,16),_DtpCtpExpectedTxDtpTti_Type())
dtpCtpExpectedTxDtpTti.setMaxAccess(_C)
if mibBuilder.loadTexts:dtpCtpExpectedTxDtpTti.setStatus(_A)
_DtpCtpRxDtpTti_Type=DisplayString
_DtpCtpRxDtpTti_Object=MibTableColumn
dtpCtpRxDtpTti=_DtpCtpRxDtpTti_Object((1,3,6,1,4,1,21296,2,2,2,2,7,1,1,17),_DtpCtpRxDtpTti_Type())
dtpCtpRxDtpTti.setMaxAccess(_F)
if mibBuilder.loadTexts:dtpCtpRxDtpTti.setStatus(_A)
_DtpCtpRecvTxDtpTti_Type=DisplayString
_DtpCtpRecvTxDtpTti_Object=MibTableColumn
dtpCtpRecvTxDtpTti=_DtpCtpRecvTxDtpTti_Object((1,3,6,1,4,1,21296,2,2,2,2,7,1,1,18),_DtpCtpRecvTxDtpTti_Type())
dtpCtpRecvTxDtpTti.setMaxAccess(_F)
if mibBuilder.loadTexts:dtpCtpRecvTxDtpTti.setStatus(_A)
_DtpCtpDtpRxCv15MinutesTce_Type=Counter64
_DtpCtpDtpRxCv15MinutesTce_Object=MibTableColumn
dtpCtpDtpRxCv15MinutesTce=_DtpCtpDtpRxCv15MinutesTce_Object((1,3,6,1,4,1,21296,2,2,2,2,7,1,1,19),_DtpCtpDtpRxCv15MinutesTce_Type())
dtpCtpDtpRxCv15MinutesTce.setMaxAccess(_C)
if mibBuilder.loadTexts:dtpCtpDtpRxCv15MinutesTce.setStatus(_A)
class _DtpCtpDtpRxEs15MinutesTce_Type(Integer32):defaultValue=120
_DtpCtpDtpRxEs15MinutesTce_Type.__name__=_D
_DtpCtpDtpRxEs15MinutesTce_Object=MibTableColumn
dtpCtpDtpRxEs15MinutesTce=_DtpCtpDtpRxEs15MinutesTce_Object((1,3,6,1,4,1,21296,2,2,2,2,7,1,1,20),_DtpCtpDtpRxEs15MinutesTce_Type())
dtpCtpDtpRxEs15MinutesTce.setMaxAccess(_C)
if mibBuilder.loadTexts:dtpCtpDtpRxEs15MinutesTce.setStatus(_A)
class _DtpCtpDtpRxSes15MinutesTce_Type(Integer32):defaultValue=3
_DtpCtpDtpRxSes15MinutesTce_Type.__name__=_D
_DtpCtpDtpRxSes15MinutesTce_Object=MibTableColumn
dtpCtpDtpRxSes15MinutesTce=_DtpCtpDtpRxSes15MinutesTce_Object((1,3,6,1,4,1,21296,2,2,2,2,7,1,1,21),_DtpCtpDtpRxSes15MinutesTce_Type())
dtpCtpDtpRxSes15MinutesTce.setMaxAccess(_C)
if mibBuilder.loadTexts:dtpCtpDtpRxSes15MinutesTce.setStatus(_A)
class _DtpCtpDtpRxUas15MinutesTce_Type(Integer32):defaultValue=10
_DtpCtpDtpRxUas15MinutesTce_Type.__name__=_D
_DtpCtpDtpRxUas15MinutesTce_Object=MibTableColumn
dtpCtpDtpRxUas15MinutesTce=_DtpCtpDtpRxUas15MinutesTce_Object((1,3,6,1,4,1,21296,2,2,2,2,7,1,1,22),_DtpCtpDtpRxUas15MinutesTce_Type())
dtpCtpDtpRxUas15MinutesTce.setMaxAccess(_C)
if mibBuilder.loadTexts:dtpCtpDtpRxUas15MinutesTce.setStatus(_A)
_DtpCtpDtpRxCvDayTce_Type=Counter64
_DtpCtpDtpRxCvDayTce_Object=MibTableColumn
dtpCtpDtpRxCvDayTce=_DtpCtpDtpRxCvDayTce_Object((1,3,6,1,4,1,21296,2,2,2,2,7,1,1,23),_DtpCtpDtpRxCvDayTce_Type())
dtpCtpDtpRxCvDayTce.setMaxAccess(_C)
if mibBuilder.loadTexts:dtpCtpDtpRxCvDayTce.setStatus(_A)
class _DtpCtpDtpRxEsDayTce_Type(Integer32):defaultValue=1200
_DtpCtpDtpRxEsDayTce_Type.__name__=_D
_DtpCtpDtpRxEsDayTce_Object=MibTableColumn
dtpCtpDtpRxEsDayTce=_DtpCtpDtpRxEsDayTce_Object((1,3,6,1,4,1,21296,2,2,2,2,7,1,1,24),_DtpCtpDtpRxEsDayTce_Type())
dtpCtpDtpRxEsDayTce.setMaxAccess(_C)
if mibBuilder.loadTexts:dtpCtpDtpRxEsDayTce.setStatus(_A)
class _DtpCtpDtpRxSesDayTce_Type(Integer32):defaultValue=7
_DtpCtpDtpRxSesDayTce_Type.__name__=_D
_DtpCtpDtpRxSesDayTce_Object=MibTableColumn
dtpCtpDtpRxSesDayTce=_DtpCtpDtpRxSesDayTce_Object((1,3,6,1,4,1,21296,2,2,2,2,7,1,1,25),_DtpCtpDtpRxSesDayTce_Type())
dtpCtpDtpRxSesDayTce.setMaxAccess(_C)
if mibBuilder.loadTexts:dtpCtpDtpRxSesDayTce.setStatus(_A)
class _DtpCtpDtpRxUasDayTce_Type(Integer32):defaultValue=10
_DtpCtpDtpRxUasDayTce_Type.__name__=_D
_DtpCtpDtpRxUasDayTce_Object=MibTableColumn
dtpCtpDtpRxUasDayTce=_DtpCtpDtpRxUasDayTce_Object((1,3,6,1,4,1,21296,2,2,2,2,7,1,1,26),_DtpCtpDtpRxUasDayTce_Type())
dtpCtpDtpRxUasDayTce.setMaxAccess(_C)
if mibBuilder.loadTexts:dtpCtpDtpRxUasDayTce.setStatus(_A)
_DtpCtpDtpTxCv15MinutesTce_Type=Counter64
_DtpCtpDtpTxCv15MinutesTce_Object=MibTableColumn
dtpCtpDtpTxCv15MinutesTce=_DtpCtpDtpTxCv15MinutesTce_Object((1,3,6,1,4,1,21296,2,2,2,2,7,1,1,27),_DtpCtpDtpTxCv15MinutesTce_Type())
dtpCtpDtpTxCv15MinutesTce.setMaxAccess(_C)
if mibBuilder.loadTexts:dtpCtpDtpTxCv15MinutesTce.setStatus(_A)
class _DtpCtpDtpTxEs15MinutesTce_Type(Integer32):defaultValue=120
_DtpCtpDtpTxEs15MinutesTce_Type.__name__=_D
_DtpCtpDtpTxEs15MinutesTce_Object=MibTableColumn
dtpCtpDtpTxEs15MinutesTce=_DtpCtpDtpTxEs15MinutesTce_Object((1,3,6,1,4,1,21296,2,2,2,2,7,1,1,28),_DtpCtpDtpTxEs15MinutesTce_Type())
dtpCtpDtpTxEs15MinutesTce.setMaxAccess(_C)
if mibBuilder.loadTexts:dtpCtpDtpTxEs15MinutesTce.setStatus(_A)
class _DtpCtpDtpTxSes15MinutesTce_Type(Integer32):defaultValue=3
_DtpCtpDtpTxSes15MinutesTce_Type.__name__=_D
_DtpCtpDtpTxSes15MinutesTce_Object=MibTableColumn
dtpCtpDtpTxSes15MinutesTce=_DtpCtpDtpTxSes15MinutesTce_Object((1,3,6,1,4,1,21296,2,2,2,2,7,1,1,29),_DtpCtpDtpTxSes15MinutesTce_Type())
dtpCtpDtpTxSes15MinutesTce.setMaxAccess(_C)
if mibBuilder.loadTexts:dtpCtpDtpTxSes15MinutesTce.setStatus(_A)
class _DtpCtpDtpTxUas15MinutesTce_Type(Integer32):defaultValue=10
_DtpCtpDtpTxUas15MinutesTce_Type.__name__=_D
_DtpCtpDtpTxUas15MinutesTce_Object=MibTableColumn
dtpCtpDtpTxUas15MinutesTce=_DtpCtpDtpTxUas15MinutesTce_Object((1,3,6,1,4,1,21296,2,2,2,2,7,1,1,30),_DtpCtpDtpTxUas15MinutesTce_Type())
dtpCtpDtpTxUas15MinutesTce.setMaxAccess(_C)
if mibBuilder.loadTexts:dtpCtpDtpTxUas15MinutesTce.setStatus(_A)
_DtpCtpDtpTxCvDayTce_Type=Counter64
_DtpCtpDtpTxCvDayTce_Object=MibTableColumn
dtpCtpDtpTxCvDayTce=_DtpCtpDtpTxCvDayTce_Object((1,3,6,1,4,1,21296,2,2,2,2,7,1,1,31),_DtpCtpDtpTxCvDayTce_Type())
dtpCtpDtpTxCvDayTce.setMaxAccess(_C)
if mibBuilder.loadTexts:dtpCtpDtpTxCvDayTce.setStatus(_A)
class _DtpCtpDtpTxEsDayTce_Type(Integer32):defaultValue=1200
_DtpCtpDtpTxEsDayTce_Type.__name__=_D
_DtpCtpDtpTxEsDayTce_Object=MibTableColumn
dtpCtpDtpTxEsDayTce=_DtpCtpDtpTxEsDayTce_Object((1,3,6,1,4,1,21296,2,2,2,2,7,1,1,32),_DtpCtpDtpTxEsDayTce_Type())
dtpCtpDtpTxEsDayTce.setMaxAccess(_C)
if mibBuilder.loadTexts:dtpCtpDtpTxEsDayTce.setStatus(_A)
class _DtpCtpDtpTxSesDayTce_Type(Integer32):defaultValue=7
_DtpCtpDtpTxSesDayTce_Type.__name__=_D
_DtpCtpDtpTxSesDayTce_Object=MibTableColumn
dtpCtpDtpTxSesDayTce=_DtpCtpDtpTxSesDayTce_Object((1,3,6,1,4,1,21296,2,2,2,2,7,1,1,33),_DtpCtpDtpTxSesDayTce_Type())
dtpCtpDtpTxSesDayTce.setMaxAccess(_C)
if mibBuilder.loadTexts:dtpCtpDtpTxSesDayTce.setStatus(_A)
class _DtpCtpDtpTxUasDayTce_Type(Integer32):defaultValue=10
_DtpCtpDtpTxUasDayTce_Type.__name__=_D
_DtpCtpDtpTxUasDayTce_Object=MibTableColumn
dtpCtpDtpTxUasDayTce=_DtpCtpDtpTxUasDayTce_Object((1,3,6,1,4,1,21296,2,2,2,2,7,1,1,34),_DtpCtpDtpTxUasDayTce_Type())
dtpCtpDtpTxUasDayTce.setMaxAccess(_C)
if mibBuilder.loadTexts:dtpCtpDtpTxUasDayTce.setStatus(_A)
class _DtpCtpDtpRxCv15MinutesTceReporting_Type(TruthValue):defaultValue=2
_DtpCtpDtpRxCv15MinutesTceReporting_Type.__name__=_E
_DtpCtpDtpRxCv15MinutesTceReporting_Object=MibTableColumn
dtpCtpDtpRxCv15MinutesTceReporting=_DtpCtpDtpRxCv15MinutesTceReporting_Object((1,3,6,1,4,1,21296,2,2,2,2,7,1,1,35),_DtpCtpDtpRxCv15MinutesTceReporting_Type())
dtpCtpDtpRxCv15MinutesTceReporting.setMaxAccess(_C)
if mibBuilder.loadTexts:dtpCtpDtpRxCv15MinutesTceReporting.setStatus(_A)
class _DtpCtpDtpRxEs15MinutesTceReporting_Type(TruthValue):defaultValue=2
_DtpCtpDtpRxEs15MinutesTceReporting_Type.__name__=_E
_DtpCtpDtpRxEs15MinutesTceReporting_Object=MibTableColumn
dtpCtpDtpRxEs15MinutesTceReporting=_DtpCtpDtpRxEs15MinutesTceReporting_Object((1,3,6,1,4,1,21296,2,2,2,2,7,1,1,36),_DtpCtpDtpRxEs15MinutesTceReporting_Type())
dtpCtpDtpRxEs15MinutesTceReporting.setMaxAccess(_C)
if mibBuilder.loadTexts:dtpCtpDtpRxEs15MinutesTceReporting.setStatus(_A)
class _DtpCtpDtpRxSes15MinutesTceReporting_Type(TruthValue):defaultValue=2
_DtpCtpDtpRxSes15MinutesTceReporting_Type.__name__=_E
_DtpCtpDtpRxSes15MinutesTceReporting_Object=MibTableColumn
dtpCtpDtpRxSes15MinutesTceReporting=_DtpCtpDtpRxSes15MinutesTceReporting_Object((1,3,6,1,4,1,21296,2,2,2,2,7,1,1,37),_DtpCtpDtpRxSes15MinutesTceReporting_Type())
dtpCtpDtpRxSes15MinutesTceReporting.setMaxAccess(_C)
if mibBuilder.loadTexts:dtpCtpDtpRxSes15MinutesTceReporting.setStatus(_A)
class _DtpCtpDtpRxUas15MinutesTceReporting_Type(TruthValue):defaultValue=2
_DtpCtpDtpRxUas15MinutesTceReporting_Type.__name__=_E
_DtpCtpDtpRxUas15MinutesTceReporting_Object=MibTableColumn
dtpCtpDtpRxUas15MinutesTceReporting=_DtpCtpDtpRxUas15MinutesTceReporting_Object((1,3,6,1,4,1,21296,2,2,2,2,7,1,1,38),_DtpCtpDtpRxUas15MinutesTceReporting_Type())
dtpCtpDtpRxUas15MinutesTceReporting.setMaxAccess(_C)
if mibBuilder.loadTexts:dtpCtpDtpRxUas15MinutesTceReporting.setStatus(_A)
class _DtpCtpDtpRxCvDayTceReporting_Type(TruthValue):defaultValue=2
_DtpCtpDtpRxCvDayTceReporting_Type.__name__=_E
_DtpCtpDtpRxCvDayTceReporting_Object=MibTableColumn
dtpCtpDtpRxCvDayTceReporting=_DtpCtpDtpRxCvDayTceReporting_Object((1,3,6,1,4,1,21296,2,2,2,2,7,1,1,39),_DtpCtpDtpRxCvDayTceReporting_Type())
dtpCtpDtpRxCvDayTceReporting.setMaxAccess(_C)
if mibBuilder.loadTexts:dtpCtpDtpRxCvDayTceReporting.setStatus(_A)
class _DtpCtpDtpRxEsDayTceReporting_Type(TruthValue):defaultValue=2
_DtpCtpDtpRxEsDayTceReporting_Type.__name__=_E
_DtpCtpDtpRxEsDayTceReporting_Object=MibTableColumn
dtpCtpDtpRxEsDayTceReporting=_DtpCtpDtpRxEsDayTceReporting_Object((1,3,6,1,4,1,21296,2,2,2,2,7,1,1,40),_DtpCtpDtpRxEsDayTceReporting_Type())
dtpCtpDtpRxEsDayTceReporting.setMaxAccess(_C)
if mibBuilder.loadTexts:dtpCtpDtpRxEsDayTceReporting.setStatus(_A)
class _DtpCtpDtpRxSesDayTceReporting_Type(TruthValue):defaultValue=2
_DtpCtpDtpRxSesDayTceReporting_Type.__name__=_E
_DtpCtpDtpRxSesDayTceReporting_Object=MibTableColumn
dtpCtpDtpRxSesDayTceReporting=_DtpCtpDtpRxSesDayTceReporting_Object((1,3,6,1,4,1,21296,2,2,2,2,7,1,1,41),_DtpCtpDtpRxSesDayTceReporting_Type())
dtpCtpDtpRxSesDayTceReporting.setMaxAccess(_C)
if mibBuilder.loadTexts:dtpCtpDtpRxSesDayTceReporting.setStatus(_A)
class _DtpCtpDtpRxUasDayTceReporting_Type(TruthValue):defaultValue=2
_DtpCtpDtpRxUasDayTceReporting_Type.__name__=_E
_DtpCtpDtpRxUasDayTceReporting_Object=MibTableColumn
dtpCtpDtpRxUasDayTceReporting=_DtpCtpDtpRxUasDayTceReporting_Object((1,3,6,1,4,1,21296,2,2,2,2,7,1,1,42),_DtpCtpDtpRxUasDayTceReporting_Type())
dtpCtpDtpRxUasDayTceReporting.setMaxAccess(_C)
if mibBuilder.loadTexts:dtpCtpDtpRxUasDayTceReporting.setStatus(_A)
class _DtpCtpDtpTxCv15MinutesTceReporting_Type(TruthValue):defaultValue=2
_DtpCtpDtpTxCv15MinutesTceReporting_Type.__name__=_E
_DtpCtpDtpTxCv15MinutesTceReporting_Object=MibTableColumn
dtpCtpDtpTxCv15MinutesTceReporting=_DtpCtpDtpTxCv15MinutesTceReporting_Object((1,3,6,1,4,1,21296,2,2,2,2,7,1,1,43),_DtpCtpDtpTxCv15MinutesTceReporting_Type())
dtpCtpDtpTxCv15MinutesTceReporting.setMaxAccess(_C)
if mibBuilder.loadTexts:dtpCtpDtpTxCv15MinutesTceReporting.setStatus(_A)
class _DtpCtpDtpTxEs15MinutesTceReporting_Type(TruthValue):defaultValue=2
_DtpCtpDtpTxEs15MinutesTceReporting_Type.__name__=_E
_DtpCtpDtpTxEs15MinutesTceReporting_Object=MibTableColumn
dtpCtpDtpTxEs15MinutesTceReporting=_DtpCtpDtpTxEs15MinutesTceReporting_Object((1,3,6,1,4,1,21296,2,2,2,2,7,1,1,44),_DtpCtpDtpTxEs15MinutesTceReporting_Type())
dtpCtpDtpTxEs15MinutesTceReporting.setMaxAccess(_C)
if mibBuilder.loadTexts:dtpCtpDtpTxEs15MinutesTceReporting.setStatus(_A)
class _DtpCtpDtpTxSes15MinutesTceReporting_Type(TruthValue):defaultValue=2
_DtpCtpDtpTxSes15MinutesTceReporting_Type.__name__=_E
_DtpCtpDtpTxSes15MinutesTceReporting_Object=MibTableColumn
dtpCtpDtpTxSes15MinutesTceReporting=_DtpCtpDtpTxSes15MinutesTceReporting_Object((1,3,6,1,4,1,21296,2,2,2,2,7,1,1,45),_DtpCtpDtpTxSes15MinutesTceReporting_Type())
dtpCtpDtpTxSes15MinutesTceReporting.setMaxAccess(_C)
if mibBuilder.loadTexts:dtpCtpDtpTxSes15MinutesTceReporting.setStatus(_A)
class _DtpCtpDtpTxUas15MinutesTceReporting_Type(TruthValue):defaultValue=2
_DtpCtpDtpTxUas15MinutesTceReporting_Type.__name__=_E
_DtpCtpDtpTxUas15MinutesTceReporting_Object=MibTableColumn
dtpCtpDtpTxUas15MinutesTceReporting=_DtpCtpDtpTxUas15MinutesTceReporting_Object((1,3,6,1,4,1,21296,2,2,2,2,7,1,1,46),_DtpCtpDtpTxUas15MinutesTceReporting_Type())
dtpCtpDtpTxUas15MinutesTceReporting.setMaxAccess(_C)
if mibBuilder.loadTexts:dtpCtpDtpTxUas15MinutesTceReporting.setStatus(_A)
class _DtpCtpDtpTxCvDayTceReporting_Type(TruthValue):defaultValue=2
_DtpCtpDtpTxCvDayTceReporting_Type.__name__=_E
_DtpCtpDtpTxCvDayTceReporting_Object=MibTableColumn
dtpCtpDtpTxCvDayTceReporting=_DtpCtpDtpTxCvDayTceReporting_Object((1,3,6,1,4,1,21296,2,2,2,2,7,1,1,47),_DtpCtpDtpTxCvDayTceReporting_Type())
dtpCtpDtpTxCvDayTceReporting.setMaxAccess(_C)
if mibBuilder.loadTexts:dtpCtpDtpTxCvDayTceReporting.setStatus(_A)
class _DtpCtpDtpTxEsDayTceReporting_Type(TruthValue):defaultValue=2
_DtpCtpDtpTxEsDayTceReporting_Type.__name__=_E
_DtpCtpDtpTxEsDayTceReporting_Object=MibTableColumn
dtpCtpDtpTxEsDayTceReporting=_DtpCtpDtpTxEsDayTceReporting_Object((1,3,6,1,4,1,21296,2,2,2,2,7,1,1,48),_DtpCtpDtpTxEsDayTceReporting_Type())
dtpCtpDtpTxEsDayTceReporting.setMaxAccess(_C)
if mibBuilder.loadTexts:dtpCtpDtpTxEsDayTceReporting.setStatus(_A)
class _DtpCtpDtpTxSesDayTceReporting_Type(TruthValue):defaultValue=2
_DtpCtpDtpTxSesDayTceReporting_Type.__name__=_E
_DtpCtpDtpTxSesDayTceReporting_Object=MibTableColumn
dtpCtpDtpTxSesDayTceReporting=_DtpCtpDtpTxSesDayTceReporting_Object((1,3,6,1,4,1,21296,2,2,2,2,7,1,1,49),_DtpCtpDtpTxSesDayTceReporting_Type())
dtpCtpDtpTxSesDayTceReporting.setMaxAccess(_C)
if mibBuilder.loadTexts:dtpCtpDtpTxSesDayTceReporting.setStatus(_A)
class _DtpCtpDtpTxUasDayTceReporting_Type(TruthValue):defaultValue=2
_DtpCtpDtpTxUasDayTceReporting_Type.__name__=_E
_DtpCtpDtpTxUasDayTceReporting_Object=MibTableColumn
dtpCtpDtpTxUasDayTceReporting=_DtpCtpDtpTxUasDayTceReporting_Object((1,3,6,1,4,1,21296,2,2,2,2,7,1,1,50),_DtpCtpDtpTxUasDayTceReporting_Type())
dtpCtpDtpTxUasDayTceReporting.setMaxAccess(_C)
if mibBuilder.loadTexts:dtpCtpDtpTxUasDayTceReporting.setStatus(_A)
class _DtpCtpPrbsGenerationMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_DtpCtpPrbsGenerationMode_Type.__name__=_D
_DtpCtpPrbsGenerationMode_Object=MibTableColumn
dtpCtpPrbsGenerationMode=_DtpCtpPrbsGenerationMode_Object((1,3,6,1,4,1,21296,2,2,2,2,7,1,1,51),_DtpCtpPrbsGenerationMode_Type())
dtpCtpPrbsGenerationMode.setMaxAccess(_C)
if mibBuilder.loadTexts:dtpCtpPrbsGenerationMode.setStatus(_A)
class _DtpCtpPrbsMonitoringMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_DtpCtpPrbsMonitoringMode_Type.__name__=_D
_DtpCtpPrbsMonitoringMode_Object=MibTableColumn
dtpCtpPrbsMonitoringMode=_DtpCtpPrbsMonitoringMode_Object((1,3,6,1,4,1,21296,2,2,2,2,7,1,1,52),_DtpCtpPrbsMonitoringMode_Type())
dtpCtpPrbsMonitoringMode.setMaxAccess(_C)
if mibBuilder.loadTexts:dtpCtpPrbsMonitoringMode.setStatus(_A)
class _DtpCtpNumDtpSubCh_Type(Integer32):defaultValue=0
_DtpCtpNumDtpSubCh_Type.__name__=_D
_DtpCtpNumDtpSubCh_Object=MibTableColumn
dtpCtpNumDtpSubCh=_DtpCtpNumDtpSubCh_Object((1,3,6,1,4,1,21296,2,2,2,2,7,1,1,53),_DtpCtpNumDtpSubCh_Type())
dtpCtpNumDtpSubCh.setMaxAccess(_F)
if mibBuilder.loadTexts:dtpCtpNumDtpSubCh.setStatus(_A)
class _DtpCtpMuxMode_Type(TruthValue):defaultValue=2
_DtpCtpMuxMode_Type.__name__=_E
_DtpCtpMuxMode_Object=MibTableColumn
dtpCtpMuxMode=_DtpCtpMuxMode_Object((1,3,6,1,4,1,21296,2,2,2,2,7,1,1,54),_DtpCtpMuxMode_Type())
dtpCtpMuxMode.setMaxAccess(_F)
if mibBuilder.loadTexts:dtpCtpMuxMode.setStatus(_A)
class _DtpCtpPmHistStatsEnable_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_G,2)))
_DtpCtpPmHistStatsEnable_Type.__name__=_D
_DtpCtpPmHistStatsEnable_Object=MibTableColumn
dtpCtpPmHistStatsEnable=_DtpCtpPmHistStatsEnable_Object((1,3,6,1,4,1,21296,2,2,2,2,7,1,1,55),_DtpCtpPmHistStatsEnable_Type())
dtpCtpPmHistStatsEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:dtpCtpPmHistStatsEnable.setStatus(_A)
class _DtpCtpCrossConnectType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_I,1),('unidirectionFrom',2),('unidirectionTo',3),('unidirectionToAndFrom',4),('bidirection',5),('bidirectionUnidirectionFrom',6),('bidirectionUnidirectionTo',7),('bidirectionUnidirectionToAndFrom',8)))
_DtpCtpCrossConnectType_Type.__name__=_D
_DtpCtpCrossConnectType_Object=MibTableColumn
dtpCtpCrossConnectType=_DtpCtpCrossConnectType_Object((1,3,6,1,4,1,21296,2,2,2,2,7,1,1,56),_DtpCtpCrossConnectType_Type())
dtpCtpCrossConnectType.setMaxAccess(_F)
if mibBuilder.loadTexts:dtpCtpCrossConnectType.setStatus(_A)
_DtpCtpConformance_ObjectIdentity=ObjectIdentity
dtpCtpConformance=_DtpCtpConformance_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,2,7,3))
_DtpCtpCompliances_ObjectIdentity=ObjectIdentity
dtpCtpCompliances=_DtpCtpCompliances_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,2,7,3,1))
_DtpCtpGroups_ObjectIdentity=ObjectIdentity
dtpCtpGroups=_DtpCtpGroups_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,2,7,3,2))
dtpCtpGroup=ObjectGroup((1,3,6,1,4,1,21296,2,2,2,2,7,3,2,1))
dtpCtpGroup.setObjects(*((_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_x),(_B,_y),(_B,_z),(_B,_A0),(_B,_A1),(_B,_A2),(_B,_A3),(_B,_A4),(_B,_A5),(_B,_A6),(_B,_A7),(_B,_A8),(_B,_A9),(_B,_AA),(_B,_AB),(_B,_AC),(_B,_AD),(_B,_AE)))
if mibBuilder.loadTexts:dtpCtpGroup.setStatus(_A)
dtpCtpCompliance=ModuleCompliance((1,3,6,1,4,1,21296,2,2,2,2,7,3,1,1))
dtpCtpCompliance.setObjects((_B,_AF))
if mibBuilder.loadTexts:dtpCtpCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'dtpCtpMIB':dtpCtpMIB,'dtpCtpTable':dtpCtpTable,'dtpCtpEntry':dtpCtpEntry,_L:dtpCtpCfgProtSt,_M:dtpCtpProtMod,_N:dtpCtpSwReason,_O:dtpCtpSupportingTP,_P:dtpCtpExpectedPayload,_Q:dtpCtpSupportingCircuitIdList,_R:dtpCtpDetectedPayload,_S:dtpCtpDataRate,_T:dtpCtpLoopback,_U:dtpCtpInsertDtpTti,_V:dtpCtpTtiAlarmReporting,_W:dtpCtpTxTtiAlarmReporting,_X:dtpCtpTxDtpTti,_Y:dtpCtpRxDtpTtiWrite,_Z:dtpCtpExpectedDtpTti,_a:dtpCtpExpectedTxDtpTti,_b:dtpCtpRxDtpTti,_c:dtpCtpRecvTxDtpTti,_d:dtpCtpDtpRxCv15MinutesTce,_e:dtpCtpDtpRxEs15MinutesTce,_f:dtpCtpDtpRxSes15MinutesTce,_g:dtpCtpDtpRxUas15MinutesTce,_h:dtpCtpDtpRxCvDayTce,_i:dtpCtpDtpRxEsDayTce,_j:dtpCtpDtpRxSesDayTce,_k:dtpCtpDtpRxUasDayTce,_l:dtpCtpDtpTxCv15MinutesTce,_m:dtpCtpDtpTxEs15MinutesTce,_n:dtpCtpDtpTxSes15MinutesTce,_o:dtpCtpDtpTxUas15MinutesTce,_p:dtpCtpDtpTxCvDayTce,_q:dtpCtpDtpTxEsDayTce,_r:dtpCtpDtpTxSesDayTce,_s:dtpCtpDtpTxUasDayTce,_t:dtpCtpDtpRxCv15MinutesTceReporting,_u:dtpCtpDtpRxEs15MinutesTceReporting,_v:dtpCtpDtpRxSes15MinutesTceReporting,_w:dtpCtpDtpRxUas15MinutesTceReporting,_x:dtpCtpDtpRxCvDayTceReporting,_y:dtpCtpDtpRxEsDayTceReporting,_z:dtpCtpDtpRxSesDayTceReporting,_A0:dtpCtpDtpRxUasDayTceReporting,_A1:dtpCtpDtpTxCv15MinutesTceReporting,_A2:dtpCtpDtpTxEs15MinutesTceReporting,_A3:dtpCtpDtpTxSes15MinutesTceReporting,_A4:dtpCtpDtpTxUas15MinutesTceReporting,_A5:dtpCtpDtpTxCvDayTceReporting,_A6:dtpCtpDtpTxEsDayTceReporting,_A7:dtpCtpDtpTxSesDayTceReporting,_A8:dtpCtpDtpTxUasDayTceReporting,_A9:dtpCtpPrbsGenerationMode,_AA:dtpCtpPrbsMonitoringMode,_AB:dtpCtpNumDtpSubCh,_AC:dtpCtpMuxMode,_AD:dtpCtpPmHistStatsEnable,_AE:dtpCtpCrossConnectType,'dtpCtpConformance':dtpCtpConformance,'dtpCtpCompliances':dtpCtpCompliances,'dtpCtpCompliance':dtpCtpCompliance,'dtpCtpGroups':dtpCtpGroups,_AF:dtpCtpGroup})