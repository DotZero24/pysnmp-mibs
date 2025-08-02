_u='dsx1PathIntervalUasThreshold'
_t='dsx1PathIntervalCssThreshold'
_s='dsx1PathIntervalSefsThreshold'
_r='dsx1PathIntervalSesThreshold'
_q='dsx1PathIntervalEsThreshold'
_p='dsx1PathIntervalCvThreshold'
_o='dsx1LineIntervalLesThreshold'
_n='enable'
_m='disable'
_l='not-accessible'
_k='dsx1DataStreamStatIndex'
_j='dsx1DataStreamStatIfIndex'
_i='dsx1TotalIndex'
_h='dsx1LoopbackStatus'
_g='dsx1IntervalUASs'
_f='dsx1IntervalSESs'
_e='dsx1IntervalSEFSs'
_d='dsx1IntervalPCVs'
_c='dsx1IntervalNumber'
_b='dsx1IntervalLESs'
_a='dsx1IntervalIndex'
_Z='dsx1IntervalESs'
_Y='dsx1IntervalCSSs'
_X='dsx1CurrentIndex'
_W='dsx1LineIndex'
_V='OctetString'
_U='dsx1LineStatus'
_T='deprecated'
_S='Unsigned32'
_R='notApplicable'
_Q='alarmState'
_P='alarmEventReason'
_O='alarmEventLogSourceName'
_N='alarmEventLogSeverity'
_M='alarmEventLogDescription'
_L='alarmEventLogDateAndTime'
_K='alarmEventLogAlarmOrEventId'
_J='Integer32'
_I='DS1-MIB'
_H='alarmSeverity'
_G='read-write'
_F='ifAlias'
_E='IF-MIB'
_D='RAD-ds1Interface-MIB'
_C='read-only'
_B='RAD-GEN-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_V,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dsx1CurrentIndex,dsx1IntervalCSSs,dsx1IntervalESs,dsx1IntervalIndex,dsx1IntervalLESs,dsx1IntervalNumber,dsx1IntervalPCVs,dsx1IntervalSEFSs,dsx1IntervalSESs,dsx1IntervalUASs,dsx1LineIndex,dsx1LineStatus,dsx1LoopbackStatus,dsx1TotalIndex=mibBuilder.importSymbols(_I,_X,_Y,_Z,_a,_b,_c,_d,_e,_f,_g,_W,_U,_h,_i)
InterfaceIndex,ifAlias=mibBuilder.importSymbols(_E,'InterfaceIndex',_F)
PerfCurrentCount,PerfIntervalCount,PerfTotalCount=mibBuilder.importSymbols('PerfHist-TC-MIB','PerfCurrentCount','PerfIntervalCount','PerfTotalCount')
alarmEventLogAlarmOrEventId,alarmEventLogDateAndTime,alarmEventLogDescription,alarmEventLogSeverity,alarmEventLogSourceName,alarmEventReason=mibBuilder.importSymbols(_B,_K,_L,_M,_N,_O,_P)
diverseIfWanGen,=mibBuilder.importSymbols('RAD-SMI-MIB','diverseIfWanGen')
DayType,=mibBuilder.importSymbols('RAD-TC','DayType')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_J,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_S,'iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
ds1Interface=ModuleIdentity((1,3,6,1,4,1,164,3,1,6,4))
_PrtDS1Events_ObjectIdentity=ObjectIdentity
prtDS1Events=_PrtDS1Events_ObjectIdentity((1,3,6,1,4,1,164,3,1,6,4,0))
_PrtDs1PerfHistory_ObjectIdentity=ObjectIdentity
prtDs1PerfHistory=_PrtDs1PerfHistory_ObjectIdentity((1,3,6,1,4,1,164,3,1,6,4,1))
_Dsx1XCurrentTable_Object=MibTable
dsx1XCurrentTable=_Dsx1XCurrentTable_Object((1,3,6,1,4,1,164,3,1,6,4,1,2))
if mibBuilder.loadTexts:dsx1XCurrentTable.setStatus(_A)
_Dsx1XCurrentEntry_Object=MibTableRow
dsx1XCurrentEntry=_Dsx1XCurrentEntry_Object((1,3,6,1,4,1,164,3,1,6,4,1,2,1))
dsx1XCurrentEntry.setIndexNames((0,_I,_X))
if mibBuilder.loadTexts:dsx1XCurrentEntry.setStatus(_A)
_Dsx1CurrentLOS_Type=PerfCurrentCount
_Dsx1CurrentLOS_Object=MibTableColumn
dsx1CurrentLOS=_Dsx1CurrentLOS_Object((1,3,6,1,4,1,164,3,1,6,4,1,2,1,1),_Dsx1CurrentLOS_Type())
dsx1CurrentLOS.setMaxAccess(_C)
if mibBuilder.loadTexts:dsx1CurrentLOS.setStatus(_A)
_Dsx1CurrentLOF_Type=PerfCurrentCount
_Dsx1CurrentLOF_Object=MibTableColumn
dsx1CurrentLOF=_Dsx1CurrentLOF_Object((1,3,6,1,4,1,164,3,1,6,4,1,2,1,2),_Dsx1CurrentLOF_Type())
dsx1CurrentLOF.setMaxAccess(_C)
if mibBuilder.loadTexts:dsx1CurrentLOF.setStatus(_A)
_Dsx1CurrentLOC_Type=PerfCurrentCount
_Dsx1CurrentLOC_Object=MibTableColumn
dsx1CurrentLOC=_Dsx1CurrentLOC_Object((1,3,6,1,4,1,164,3,1,6,4,1,2,1,3),_Dsx1CurrentLOC_Type())
dsx1CurrentLOC.setMaxAccess(_C)
if mibBuilder.loadTexts:dsx1CurrentLOC.setStatus(_A)
_Dsx1CurrentAIS_Type=PerfCurrentCount
_Dsx1CurrentAIS_Object=MibTableColumn
dsx1CurrentAIS=_Dsx1CurrentAIS_Object((1,3,6,1,4,1,164,3,1,6,4,1,2,1,4),_Dsx1CurrentAIS_Type())
dsx1CurrentAIS.setMaxAccess(_C)
if mibBuilder.loadTexts:dsx1CurrentAIS.setStatus(_A)
_Dsx1CurrentRAI_Type=PerfCurrentCount
_Dsx1CurrentRAI_Object=MibTableColumn
dsx1CurrentRAI=_Dsx1CurrentRAI_Object((1,3,6,1,4,1,164,3,1,6,4,1,2,1,5),_Dsx1CurrentRAI_Type())
dsx1CurrentRAI.setMaxAccess(_C)
if mibBuilder.loadTexts:dsx1CurrentRAI.setStatus(_A)
_Dsx1CurrentLOMF_Type=PerfCurrentCount
_Dsx1CurrentLOMF_Object=MibTableColumn
dsx1CurrentLOMF=_Dsx1CurrentLOMF_Object((1,3,6,1,4,1,164,3,1,6,4,1,2,1,6),_Dsx1CurrentLOMF_Type())
dsx1CurrentLOMF.setMaxAccess(_C)
if mibBuilder.loadTexts:dsx1CurrentLOMF.setStatus(_A)
_Dsx1CurrentFEBE_Type=PerfCurrentCount
_Dsx1CurrentFEBE_Object=MibTableColumn
dsx1CurrentFEBE=_Dsx1CurrentFEBE_Object((1,3,6,1,4,1,164,3,1,6,4,1,2,1,7),_Dsx1CurrentFEBE_Type())
dsx1CurrentFEBE.setMaxAccess(_C)
if mibBuilder.loadTexts:dsx1CurrentFEBE.setStatus(_A)
class _Dsx1CurrentStatus_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
_Dsx1CurrentStatus_Type.__name__=_V
_Dsx1CurrentStatus_Object=MibTableColumn
dsx1CurrentStatus=_Dsx1CurrentStatus_Object((1,3,6,1,4,1,164,3,1,6,4,1,2,1,8),_Dsx1CurrentStatus_Type())
dsx1CurrentStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:dsx1CurrentStatus.setStatus(_A)
_Dsx1CurrentBPV_Type=PerfCurrentCount
_Dsx1CurrentBPV_Object=MibTableColumn
dsx1CurrentBPV=_Dsx1CurrentBPV_Object((1,3,6,1,4,1,164,3,1,6,4,1,2,1,9),_Dsx1CurrentBPV_Type())
dsx1CurrentBPV.setMaxAccess(_C)
if mibBuilder.loadTexts:dsx1CurrentBPV.setStatus(_A)
_Dsx1CurrentLOCRCMF_Type=PerfCurrentCount
_Dsx1CurrentLOCRCMF_Object=MibTableColumn
dsx1CurrentLOCRCMF=_Dsx1CurrentLOCRCMF_Object((1,3,6,1,4,1,164,3,1,6,4,1,2,1,10),_Dsx1CurrentLOCRCMF_Type())
dsx1CurrentLOCRCMF.setMaxAccess(_C)
if mibBuilder.loadTexts:dsx1CurrentLOCRCMF.setStatus(_A)
_Dsx1CurrentLOFC_Type=PerfCurrentCount
_Dsx1CurrentLOFC_Object=MibTableColumn
dsx1CurrentLOFC=_Dsx1CurrentLOFC_Object((1,3,6,1,4,1,164,3,1,6,4,1,2,1,11),_Dsx1CurrentLOFC_Type())
dsx1CurrentLOFC.setMaxAccess(_C)
if mibBuilder.loadTexts:dsx1CurrentLOFC.setStatus(_A)
_Dsx1CurrentCRCErrors_Type=PerfCurrentCount
_Dsx1CurrentCRCErrors_Object=MibTableColumn
dsx1CurrentCRCErrors=_Dsx1CurrentCRCErrors_Object((1,3,6,1,4,1,164,3,1,6,4,1,2,1,12),_Dsx1CurrentCRCErrors_Type())
dsx1CurrentCRCErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:dsx1CurrentCRCErrors.setStatus(_A)
_Dsx1CurrentLSES_Type=PerfCurrentCount
_Dsx1CurrentLSES_Object=MibTableColumn
dsx1CurrentLSES=_Dsx1CurrentLSES_Object((1,3,6,1,4,1,164,3,1,6,4,1,2,1,13),_Dsx1CurrentLSES_Type())
dsx1CurrentLSES.setMaxAccess(_C)
if mibBuilder.loadTexts:dsx1CurrentLSES.setStatus(_A)
_Dsx1CurrentFC_Type=PerfCurrentCount
_Dsx1CurrentFC_Object=MibTableColumn
dsx1CurrentFC=_Dsx1CurrentFC_Object((1,3,6,1,4,1,164,3,1,6,4,1,2,1,14),_Dsx1CurrentFC_Type())
dsx1CurrentFC.setMaxAccess(_C)
if mibBuilder.loadTexts:dsx1CurrentFC.setStatus(_A)
_Dsx1XIntervalTable_Object=MibTable
dsx1XIntervalTable=_Dsx1XIntervalTable_Object((1,3,6,1,4,1,164,3,1,6,4,1,3))
if mibBuilder.loadTexts:dsx1XIntervalTable.setStatus(_T)
_Dsx1XIntervalEntry_Object=MibTableRow
dsx1XIntervalEntry=_Dsx1XIntervalEntry_Object((1,3,6,1,4,1,164,3,1,6,4,1,3,1))
dsx1XIntervalEntry.setIndexNames((0,_I,_a),(0,_I,_c))
if mibBuilder.loadTexts:dsx1XIntervalEntry.setStatus(_T)
_Dsx1IntervalLOS_Type=PerfIntervalCount
_Dsx1IntervalLOS_Object=MibTableColumn
dsx1IntervalLOS=_Dsx1IntervalLOS_Object((1,3,6,1,4,1,164,3,1,6,4,1,3,1,1),_Dsx1IntervalLOS_Type())
dsx1IntervalLOS.setMaxAccess(_C)
if mibBuilder.loadTexts:dsx1IntervalLOS.setStatus(_T)
_Dsx1IntervalLOF_Type=PerfIntervalCount
_Dsx1IntervalLOF_Object=MibTableColumn
dsx1IntervalLOF=_Dsx1IntervalLOF_Object((1,3,6,1,4,1,164,3,1,6,4,1,3,1,2),_Dsx1IntervalLOF_Type())
dsx1IntervalLOF.setMaxAccess(_C)
if mibBuilder.loadTexts:dsx1IntervalLOF.setStatus(_T)
_Dsx1IntervalLOC_Type=PerfIntervalCount
_Dsx1IntervalLOC_Object=MibTableColumn
dsx1IntervalLOC=_Dsx1IntervalLOC_Object((1,3,6,1,4,1,164,3,1,6,4,1,3,1,3),_Dsx1IntervalLOC_Type())
dsx1IntervalLOC.setMaxAccess(_C)
if mibBuilder.loadTexts:dsx1IntervalLOC.setStatus(_A)
_Dsx1IntervalAIS_Type=PerfIntervalCount
_Dsx1IntervalAIS_Object=MibTableColumn
dsx1IntervalAIS=_Dsx1IntervalAIS_Object((1,3,6,1,4,1,164,3,1,6,4,1,3,1,4),_Dsx1IntervalAIS_Type())
dsx1IntervalAIS.setMaxAccess(_C)
if mibBuilder.loadTexts:dsx1IntervalAIS.setStatus(_T)
_Dsx1IntervalRAI_Type=PerfIntervalCount
_Dsx1IntervalRAI_Object=MibTableColumn
dsx1IntervalRAI=_Dsx1IntervalRAI_Object((1,3,6,1,4,1,164,3,1,6,4,1,3,1,5),_Dsx1IntervalRAI_Type())
dsx1IntervalRAI.setMaxAccess(_C)
if mibBuilder.loadTexts:dsx1IntervalRAI.setStatus(_T)
_Dsx1IntervalLOMF_Type=PerfIntervalCount
_Dsx1IntervalLOMF_Object=MibTableColumn
dsx1IntervalLOMF=_Dsx1IntervalLOMF_Object((1,3,6,1,4,1,164,3,1,6,4,1,3,1,6),_Dsx1IntervalLOMF_Type())
dsx1IntervalLOMF.setMaxAccess(_C)
if mibBuilder.loadTexts:dsx1IntervalLOMF.setStatus(_A)
_Dsx1IntervalFEBE_Type=PerfIntervalCount
_Dsx1IntervalFEBE_Object=MibTableColumn
dsx1IntervalFEBE=_Dsx1IntervalFEBE_Object((1,3,6,1,4,1,164,3,1,6,4,1,3,1,7),_Dsx1IntervalFEBE_Type())
dsx1IntervalFEBE.setMaxAccess(_C)
if mibBuilder.loadTexts:dsx1IntervalFEBE.setStatus(_A)
class _Dsx1IntervalStatus_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
_Dsx1IntervalStatus_Type.__name__=_V
_Dsx1IntervalStatus_Object=MibTableColumn
dsx1IntervalStatus=_Dsx1IntervalStatus_Object((1,3,6,1,4,1,164,3,1,6,4,1,3,1,8),_Dsx1IntervalStatus_Type())
dsx1IntervalStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:dsx1IntervalStatus.setStatus(_A)
_Dsx1IntervalBPV_Type=PerfIntervalCount
_Dsx1IntervalBPV_Object=MibTableColumn
dsx1IntervalBPV=_Dsx1IntervalBPV_Object((1,3,6,1,4,1,164,3,1,6,4,1,3,1,9),_Dsx1IntervalBPV_Type())
dsx1IntervalBPV.setMaxAccess(_C)
if mibBuilder.loadTexts:dsx1IntervalBPV.setStatus(_A)
_Dsx1IntervalLOCRCMF_Type=PerfIntervalCount
_Dsx1IntervalLOCRCMF_Object=MibTableColumn
dsx1IntervalLOCRCMF=_Dsx1IntervalLOCRCMF_Object((1,3,6,1,4,1,164,3,1,6,4,1,3,1,10),_Dsx1IntervalLOCRCMF_Type())
dsx1IntervalLOCRCMF.setMaxAccess(_C)
if mibBuilder.loadTexts:dsx1IntervalLOCRCMF.setStatus(_A)
_Dsx1IntervalLOFC_Type=PerfIntervalCount
_Dsx1IntervalLOFC_Object=MibTableColumn
dsx1IntervalLOFC=_Dsx1IntervalLOFC_Object((1,3,6,1,4,1,164,3,1,6,4,1,3,1,11),_Dsx1IntervalLOFC_Type())
dsx1IntervalLOFC.setMaxAccess(_C)
if mibBuilder.loadTexts:dsx1IntervalLOFC.setStatus(_A)
_Dsx1IntervalLSES_Type=PerfIntervalCount
_Dsx1IntervalLSES_Object=MibTableColumn
dsx1IntervalLSES=_Dsx1IntervalLSES_Object((1,3,6,1,4,1,164,3,1,6,4,1,3,1,13),_Dsx1IntervalLSES_Type())
dsx1IntervalLSES.setMaxAccess(_C)
if mibBuilder.loadTexts:dsx1IntervalLSES.setStatus(_T)
_Dsx1IntervalFC_Type=PerfIntervalCount
_Dsx1IntervalFC_Object=MibTableColumn
dsx1IntervalFC=_Dsx1IntervalFC_Object((1,3,6,1,4,1,164,3,1,6,4,1,3,1,14),_Dsx1IntervalFC_Type())
dsx1IntervalFC.setMaxAccess(_C)
if mibBuilder.loadTexts:dsx1IntervalFC.setStatus(_T)
_Dsx1XTotalTable_Object=MibTable
dsx1XTotalTable=_Dsx1XTotalTable_Object((1,3,6,1,4,1,164,3,1,6,4,1,4))
if mibBuilder.loadTexts:dsx1XTotalTable.setStatus(_A)
_Dsx1XTotalEntry_Object=MibTableRow
dsx1XTotalEntry=_Dsx1XTotalEntry_Object((1,3,6,1,4,1,164,3,1,6,4,1,4,1))
dsx1XTotalEntry.setIndexNames((0,_I,_i))
if mibBuilder.loadTexts:dsx1XTotalEntry.setStatus(_A)
_Dsx1TotalLOS_Type=PerfTotalCount
_Dsx1TotalLOS_Object=MibTableColumn
dsx1TotalLOS=_Dsx1TotalLOS_Object((1,3,6,1,4,1,164,3,1,6,4,1,4,1,1),_Dsx1TotalLOS_Type())
dsx1TotalLOS.setMaxAccess(_C)
if mibBuilder.loadTexts:dsx1TotalLOS.setStatus(_A)
_Dsx1TotalLOF_Type=PerfTotalCount
_Dsx1TotalLOF_Object=MibTableColumn
dsx1TotalLOF=_Dsx1TotalLOF_Object((1,3,6,1,4,1,164,3,1,6,4,1,4,1,2),_Dsx1TotalLOF_Type())
dsx1TotalLOF.setMaxAccess(_C)
if mibBuilder.loadTexts:dsx1TotalLOF.setStatus(_A)
_Dsx1TotalAIS_Type=PerfTotalCount
_Dsx1TotalAIS_Object=MibTableColumn
dsx1TotalAIS=_Dsx1TotalAIS_Object((1,3,6,1,4,1,164,3,1,6,4,1,4,1,4),_Dsx1TotalAIS_Type())
dsx1TotalAIS.setMaxAccess(_C)
if mibBuilder.loadTexts:dsx1TotalAIS.setStatus(_A)
_Dsx1TotalRAI_Type=PerfTotalCount
_Dsx1TotalRAI_Object=MibTableColumn
dsx1TotalRAI=_Dsx1TotalRAI_Object((1,3,6,1,4,1,164,3,1,6,4,1,4,1,5),_Dsx1TotalRAI_Type())
dsx1TotalRAI.setMaxAccess(_C)
if mibBuilder.loadTexts:dsx1TotalRAI.setStatus(_A)
_Dsx1TotalBPV_Type=PerfTotalCount
_Dsx1TotalBPV_Object=MibTableColumn
dsx1TotalBPV=_Dsx1TotalBPV_Object((1,3,6,1,4,1,164,3,1,6,4,1,4,1,9),_Dsx1TotalBPV_Type())
dsx1TotalBPV.setMaxAccess(_C)
if mibBuilder.loadTexts:dsx1TotalBPV.setStatus(_A)
_Dsx1TotalLOFC_Type=PerfTotalCount
_Dsx1TotalLOFC_Object=MibTableColumn
dsx1TotalLOFC=_Dsx1TotalLOFC_Object((1,3,6,1,4,1,164,3,1,6,4,1,4,1,11),_Dsx1TotalLOFC_Type())
dsx1TotalLOFC.setMaxAccess(_C)
if mibBuilder.loadTexts:dsx1TotalLOFC.setStatus(_A)
_Dsx1TotalLSES_Type=PerfTotalCount
_Dsx1TotalLSES_Object=MibTableColumn
dsx1TotalLSES=_Dsx1TotalLSES_Object((1,3,6,1,4,1,164,3,1,6,4,1,4,1,13),_Dsx1TotalLSES_Type())
dsx1TotalLSES.setMaxAccess(_C)
if mibBuilder.loadTexts:dsx1TotalLSES.setStatus(_A)
_Dsx1TotalFC_Type=PerfTotalCount
_Dsx1TotalFC_Object=MibTableColumn
dsx1TotalFC=_Dsx1TotalFC_Object((1,3,6,1,4,1,164,3,1,6,4,1,4,1,14),_Dsx1TotalFC_Type())
dsx1TotalFC.setMaxAccess(_C)
if mibBuilder.loadTexts:dsx1TotalFC.setStatus(_A)
_Dsx1DataStreamStatTable_Object=MibTable
dsx1DataStreamStatTable=_Dsx1DataStreamStatTable_Object((1,3,6,1,4,1,164,3,1,6,4,1,5))
if mibBuilder.loadTexts:dsx1DataStreamStatTable.setStatus(_A)
_Dsx1DataStreamStatEntry_Object=MibTableRow
dsx1DataStreamStatEntry=_Dsx1DataStreamStatEntry_Object((1,3,6,1,4,1,164,3,1,6,4,1,5,1))
dsx1DataStreamStatEntry.setIndexNames((0,_D,_j),(0,_D,_k))
if mibBuilder.loadTexts:dsx1DataStreamStatEntry.setStatus(_A)
_Dsx1DataStreamStatIfIndex_Type=Integer32
_Dsx1DataStreamStatIfIndex_Object=MibTableColumn
dsx1DataStreamStatIfIndex=_Dsx1DataStreamStatIfIndex_Object((1,3,6,1,4,1,164,3,1,6,4,1,5,1,1),_Dsx1DataStreamStatIfIndex_Type())
dsx1DataStreamStatIfIndex.setMaxAccess(_l)
if mibBuilder.loadTexts:dsx1DataStreamStatIfIndex.setStatus(_A)
_Dsx1DataStreamStatIndex_Type=Integer32
_Dsx1DataStreamStatIndex_Object=MibTableColumn
dsx1DataStreamStatIndex=_Dsx1DataStreamStatIndex_Object((1,3,6,1,4,1,164,3,1,6,4,1,5,1,2),_Dsx1DataStreamStatIndex_Type())
dsx1DataStreamStatIndex.setMaxAccess(_l)
if mibBuilder.loadTexts:dsx1DataStreamStatIndex.setStatus(_A)
_Dsx1DataStreamStatValid_Type=TruthValue
_Dsx1DataStreamStatValid_Object=MibTableColumn
dsx1DataStreamStatValid=_Dsx1DataStreamStatValid_Object((1,3,6,1,4,1,164,3,1,6,4,1,5,1,3),_Dsx1DataStreamStatValid_Type())
dsx1DataStreamStatValid.setMaxAccess(_C)
if mibBuilder.loadTexts:dsx1DataStreamStatValid.setStatus(_A)
_Dsx1DataStreamStatInFrames_Type=Counter32
_Dsx1DataStreamStatInFrames_Object=MibTableColumn
dsx1DataStreamStatInFrames=_Dsx1DataStreamStatInFrames_Object((1,3,6,1,4,1,164,3,1,6,4,1,5,1,4),_Dsx1DataStreamStatInFrames_Type())
dsx1DataStreamStatInFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:dsx1DataStreamStatInFrames.setStatus(_A)
_Dsx1DataStreamStatInBytes_Type=Counter32
_Dsx1DataStreamStatInBytes_Object=MibTableColumn
dsx1DataStreamStatInBytes=_Dsx1DataStreamStatInBytes_Object((1,3,6,1,4,1,164,3,1,6,4,1,5,1,5),_Dsx1DataStreamStatInBytes_Type())
dsx1DataStreamStatInBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:dsx1DataStreamStatInBytes.setStatus(_A)
_Dsx1DataStreamStatInDiscards_Type=Counter32
_Dsx1DataStreamStatInDiscards_Object=MibTableColumn
dsx1DataStreamStatInDiscards=_Dsx1DataStreamStatInDiscards_Object((1,3,6,1,4,1,164,3,1,6,4,1,5,1,6),_Dsx1DataStreamStatInDiscards_Type())
dsx1DataStreamStatInDiscards.setMaxAccess(_C)
if mibBuilder.loadTexts:dsx1DataStreamStatInDiscards.setStatus(_A)
_Dsx1DataStreamStatInErrors_Type=Counter32
_Dsx1DataStreamStatInErrors_Object=MibTableColumn
dsx1DataStreamStatInErrors=_Dsx1DataStreamStatInErrors_Object((1,3,6,1,4,1,164,3,1,6,4,1,5,1,7),_Dsx1DataStreamStatInErrors_Type())
dsx1DataStreamStatInErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:dsx1DataStreamStatInErrors.setStatus(_A)
_Dsx1DataStreamStatOutFrames_Type=Counter32
_Dsx1DataStreamStatOutFrames_Object=MibTableColumn
dsx1DataStreamStatOutFrames=_Dsx1DataStreamStatOutFrames_Object((1,3,6,1,4,1,164,3,1,6,4,1,5,1,8),_Dsx1DataStreamStatOutFrames_Type())
dsx1DataStreamStatOutFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:dsx1DataStreamStatOutFrames.setStatus(_A)
_Dsx1DataStreamStatOutBytes_Type=Counter32
_Dsx1DataStreamStatOutBytes_Object=MibTableColumn
dsx1DataStreamStatOutBytes=_Dsx1DataStreamStatOutBytes_Object((1,3,6,1,4,1,164,3,1,6,4,1,5,1,9),_Dsx1DataStreamStatOutBytes_Type())
dsx1DataStreamStatOutBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:dsx1DataStreamStatOutBytes.setStatus(_A)
_Dsx1DataStreamStatOutDiscards_Type=Counter32
_Dsx1DataStreamStatOutDiscards_Object=MibTableColumn
dsx1DataStreamStatOutDiscards=_Dsx1DataStreamStatOutDiscards_Object((1,3,6,1,4,1,164,3,1,6,4,1,5,1,10),_Dsx1DataStreamStatOutDiscards_Type())
dsx1DataStreamStatOutDiscards.setMaxAccess(_C)
if mibBuilder.loadTexts:dsx1DataStreamStatOutDiscards.setStatus(_A)
_Dsx1DataStreamStatOutErrors_Type=Counter32
_Dsx1DataStreamStatOutErrors_Object=MibTableColumn
dsx1DataStreamStatOutErrors=_Dsx1DataStreamStatOutErrors_Object((1,3,6,1,4,1,164,3,1,6,4,1,5,1,11),_Dsx1DataStreamStatOutErrors_Type())
dsx1DataStreamStatOutErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:dsx1DataStreamStatOutErrors.setStatus(_A)
_Dsx1XConfigTable_Object=MibTable
dsx1XConfigTable=_Dsx1XConfigTable_Object((1,3,6,1,4,1,164,3,1,6,4,2))
if mibBuilder.loadTexts:dsx1XConfigTable.setStatus(_A)
_Dsx1XConfigEntry_Object=MibTableRow
dsx1XConfigEntry=_Dsx1XConfigEntry_Object((1,3,6,1,4,1,164,3,1,6,4,2,1))
dsx1XConfigEntry.setIndexNames((0,_I,_W))
if mibBuilder.loadTexts:dsx1XConfigEntry.setStatus(_A)
_Dsx1IdleCode_Type=Integer32
_Dsx1IdleCode_Object=MibTableColumn
dsx1IdleCode=_Dsx1IdleCode_Object((1,3,6,1,4,1,164,3,1,6,4,2,1,1),_Dsx1IdleCode_Type())
dsx1IdleCode.setMaxAccess(_G)
if mibBuilder.loadTexts:dsx1IdleCode.setStatus(_A)
class _Dsx1LineMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('csu',1),('dsu',2)))
_Dsx1LineMode_Type.__name__=_J
_Dsx1LineMode_Object=MibTableColumn
dsx1LineMode=_Dsx1LineMode_Object((1,3,6,1,4,1,164,3,1,6,4,2,1,2),_Dsx1LineMode_Type())
dsx1LineMode.setMaxAccess(_G)
if mibBuilder.loadTexts:dsx1LineMode.setStatus(_A)
class _Dsx1dBTxGain_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_R,1),('neg75dB',2),('neg15dB',3),('neg225dB',4),('zerodB',5)))
_Dsx1dBTxGain_Type.__name__=_J
_Dsx1dBTxGain_Object=MibTableColumn
dsx1dBTxGain=_Dsx1dBTxGain_Object((1,3,6,1,4,1,164,3,1,6,4,2,1,3),_Dsx1dBTxGain_Type())
dsx1dBTxGain.setMaxAccess(_G)
if mibBuilder.loadTexts:dsx1dBTxGain.setStatus(_A)
class _Dsx1RxSensitivity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_R,1),('longHaul',2),('shortHaul',3),('monitor',4)))
_Dsx1RxSensitivity_Type.__name__=_J
_Dsx1RxSensitivity_Object=MibTableColumn
dsx1RxSensitivity=_Dsx1RxSensitivity_Object((1,3,6,1,4,1,164,3,1,6,4,2,1,4),_Dsx1RxSensitivity_Type())
dsx1RxSensitivity.setMaxAccess(_G)
if mibBuilder.loadTexts:dsx1RxSensitivity.setStatus(_A)
class _Dsx1RestoreTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('other',1),('sec1',2),('sec10',3),('immediate',4)))
_Dsx1RestoreTime_Type.__name__=_J
_Dsx1RestoreTime_Object=MibTableColumn
dsx1RestoreTime=_Dsx1RestoreTime_Object((1,3,6,1,4,1,164,3,1,6,4,2,1,5),_Dsx1RestoreTime_Type())
dsx1RestoreTime.setMaxAccess(_G)
if mibBuilder.loadTexts:dsx1RestoreTime.setStatus(_A)
_Dsx1TcFirstSignal_Type=Integer32
_Dsx1TcFirstSignal_Object=MibTableColumn
dsx1TcFirstSignal=_Dsx1TcFirstSignal_Object((1,3,6,1,4,1,164,3,1,6,4,2,1,6),_Dsx1TcFirstSignal_Type())
dsx1TcFirstSignal.setMaxAccess(_G)
if mibBuilder.loadTexts:dsx1TcFirstSignal.setStatus(_A)
_Dsx1TcSignal_Type=Integer32
_Dsx1TcSignal_Object=MibTableColumn
dsx1TcSignal=_Dsx1TcSignal_Object((1,3,6,1,4,1,164,3,1,6,4,2,1,7),_Dsx1TcSignal_Type())
dsx1TcSignal.setMaxAccess(_G)
if mibBuilder.loadTexts:dsx1TcSignal.setStatus(_A)
_Dsx1TcPattern_Type=Integer32
_Dsx1TcPattern_Object=MibTableColumn
dsx1TcPattern=_Dsx1TcPattern_Object((1,3,6,1,4,1,164,3,1,6,4,2,1,8),_Dsx1TcPattern_Type())
dsx1TcPattern.setMaxAccess(_G)
if mibBuilder.loadTexts:dsx1TcPattern.setStatus(_A)
class _Dsx1Scramble_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_R,1),('notActive',2),('active',3)))
_Dsx1Scramble_Type.__name__=_J
_Dsx1Scramble_Object=MibTableColumn
dsx1Scramble=_Dsx1Scramble_Object((1,3,6,1,4,1,164,3,1,6,4,2,1,9),_Dsx1Scramble_Type())
dsx1Scramble.setMaxAccess(_G)
if mibBuilder.loadTexts:dsx1Scramble.setStatus(_A)
class _Dsx1LineAdaptiveTimingMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('off',1),('on',2)))
_Dsx1LineAdaptiveTimingMode_Type.__name__=_J
_Dsx1LineAdaptiveTimingMode_Object=MibTableColumn
dsx1LineAdaptiveTimingMode=_Dsx1LineAdaptiveTimingMode_Object((1,3,6,1,4,1,164,3,1,6,4,2,1,10),_Dsx1LineAdaptiveTimingMode_Type())
dsx1LineAdaptiveTimingMode.setMaxAccess(_G)
if mibBuilder.loadTexts:dsx1LineAdaptiveTimingMode.setStatus(_A)
class _Dsx1TxClockSource_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('loopTiming',1),('localTiming',2),('throughTiming',3),('adaptive',4),('system',5)))
_Dsx1TxClockSource_Type.__name__=_J
_Dsx1TxClockSource_Object=MibTableColumn
dsx1TxClockSource=_Dsx1TxClockSource_Object((1,3,6,1,4,1,164,3,1,6,4,2,1,11),_Dsx1TxClockSource_Type())
dsx1TxClockSource.setMaxAccess(_G)
if mibBuilder.loadTexts:dsx1TxClockSource.setStatus(_A)
class _Dsx1AisEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_R,1),(_m,2),(_n,3)))
_Dsx1AisEnable_Type.__name__=_J
_Dsx1AisEnable_Object=MibTableColumn
dsx1AisEnable=_Dsx1AisEnable_Object((1,3,6,1,4,1,164,3,1,6,4,2,1,12),_Dsx1AisEnable_Type())
dsx1AisEnable.setMaxAccess(_G)
if mibBuilder.loadTexts:dsx1AisEnable.setStatus(_A)
class _Dsx1TsEchoCancel_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
_Dsx1TsEchoCancel_Type.__name__=_V
_Dsx1TsEchoCancel_Object=MibTableColumn
dsx1TsEchoCancel=_Dsx1TsEchoCancel_Object((1,3,6,1,4,1,164,3,1,6,4,2,1,13),_Dsx1TsEchoCancel_Type())
dsx1TsEchoCancel.setMaxAccess(_G)
if mibBuilder.loadTexts:dsx1TsEchoCancel.setStatus(_A)
class _Dsx1EchoCancelerModule_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*(('notExist',2),('exist',3)))
_Dsx1EchoCancelerModule_Type.__name__=_J
_Dsx1EchoCancelerModule_Object=MibTableColumn
dsx1EchoCancelerModule=_Dsx1EchoCancelerModule_Object((1,3,6,1,4,1,164,3,1,6,4,2,1,14),_Dsx1EchoCancelerModule_Type())
dsx1EchoCancelerModule.setMaxAccess(_C)
if mibBuilder.loadTexts:dsx1EchoCancelerModule.setStatus(_A)
class _Dsx1PortFunction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_R,1),('uni',2),('ces',3),('ima',4),('cesPsn',5),('abis',6)))
_Dsx1PortFunction_Type.__name__=_J
_Dsx1PortFunction_Object=MibTableColumn
dsx1PortFunction=_Dsx1PortFunction_Object((1,3,6,1,4,1,164,3,1,6,4,2,1,15),_Dsx1PortFunction_Type())
dsx1PortFunction.setMaxAccess(_G)
if mibBuilder.loadTexts:dsx1PortFunction.setStatus(_A)
class _Dsx1PortMultiplier_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_R,1),('r56',2),('r64',3)))
_Dsx1PortMultiplier_Type.__name__=_J
_Dsx1PortMultiplier_Object=MibTableColumn
dsx1PortMultiplier=_Dsx1PortMultiplier_Object((1,3,6,1,4,1,164,3,1,6,4,2,1,16),_Dsx1PortMultiplier_Type())
dsx1PortMultiplier.setMaxAccess(_G)
if mibBuilder.loadTexts:dsx1PortMultiplier.setStatus(_A)
class _Dsx1LeasedLine_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_R,1),(_m,2),(_n,3)))
_Dsx1LeasedLine_Type.__name__=_J
_Dsx1LeasedLine_Object=MibTableColumn
dsx1LeasedLine=_Dsx1LeasedLine_Object((1,3,6,1,4,1,164,3,1,6,4,2,1,17),_Dsx1LeasedLine_Type())
dsx1LeasedLine.setMaxAccess(_G)
if mibBuilder.loadTexts:dsx1LeasedLine.setStatus(_A)
class _Dsx1CsuLoop_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_R,1),('local',2),('transparent',3),('remote',4)))
_Dsx1CsuLoop_Type.__name__=_J
_Dsx1CsuLoop_Object=MibTableColumn
dsx1CsuLoop=_Dsx1CsuLoop_Object((1,3,6,1,4,1,164,3,1,6,4,2,1,18),_Dsx1CsuLoop_Type())
dsx1CsuLoop.setMaxAccess(_G)
if mibBuilder.loadTexts:dsx1CsuLoop.setStatus(_A)
_Dsx1ClockSource_Type=Integer32
_Dsx1ClockSource_Object=MibTableColumn
dsx1ClockSource=_Dsx1ClockSource_Object((1,3,6,1,4,1,164,3,1,6,4,2,1,19),_Dsx1ClockSource_Type())
dsx1ClockSource.setMaxAccess(_G)
if mibBuilder.loadTexts:dsx1ClockSource.setStatus(_A)
class _Dsx1OosSignal_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_R,1),('space',2),('mark',3),('spaceMark',4),('markSpace',5)))
_Dsx1OosSignal_Type.__name__=_J
_Dsx1OosSignal_Object=MibTableColumn
dsx1OosSignal=_Dsx1OosSignal_Object((1,3,6,1,4,1,164,3,1,6,4,2,1,20),_Dsx1OosSignal_Type())
dsx1OosSignal.setMaxAccess(_G)
if mibBuilder.loadTexts:dsx1OosSignal.setStatus(_A)
_Dsx1BundleNextIndex_Type=Integer32
_Dsx1BundleNextIndex_Object=MibTableColumn
dsx1BundleNextIndex=_Dsx1BundleNextIndex_Object((1,3,6,1,4,1,164,3,1,6,4,2,1,21),_Dsx1BundleNextIndex_Type())
dsx1BundleNextIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:dsx1BundleNextIndex.setStatus(_A)
class _Dsx1CRC6CalcMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('jtG704',1),('ituG704',2)))
_Dsx1CRC6CalcMode_Type.__name__=_J
_Dsx1CRC6CalcMode_Object=MibTableColumn
dsx1CRC6CalcMode=_Dsx1CRC6CalcMode_Object((1,3,6,1,4,1,164,3,1,6,4,2,1,22),_Dsx1CRC6CalcMode_Type())
dsx1CRC6CalcMode.setMaxAccess(_G)
if mibBuilder.loadTexts:dsx1CRC6CalcMode.setStatus(_A)
class _Dsx1SendUponFail_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*(('oosCode',2),('ais',3)))
_Dsx1SendUponFail_Type.__name__=_J
_Dsx1SendUponFail_Object=MibTableColumn
dsx1SendUponFail=_Dsx1SendUponFail_Object((1,3,6,1,4,1,164,3,1,6,4,2,1,23),_Dsx1SendUponFail_Type())
dsx1SendUponFail.setMaxAccess(_G)
if mibBuilder.loadTexts:dsx1SendUponFail.setStatus(_A)
class _Dsx1InbandLoopSignal_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,99)));namedValues=NamedValues(*((_R,1),('csu',2),('fdlLine',3),('fdlNetwork',4),('niuFac1',5),('niuFac2',6),('program',99)))
_Dsx1InbandLoopSignal_Type.__name__=_J
_Dsx1InbandLoopSignal_Object=MibTableColumn
dsx1InbandLoopSignal=_Dsx1InbandLoopSignal_Object((1,3,6,1,4,1,164,3,1,6,4,2,1,24),_Dsx1InbandLoopSignal_Type())
dsx1InbandLoopSignal.setMaxAccess(_G)
if mibBuilder.loadTexts:dsx1InbandLoopSignal.setStatus(_A)
_Dsx1InbandLoopUpCode_Type=OctetString
_Dsx1InbandLoopUpCode_Object=MibTableColumn
dsx1InbandLoopUpCode=_Dsx1InbandLoopUpCode_Object((1,3,6,1,4,1,164,3,1,6,4,2,1,25),_Dsx1InbandLoopUpCode_Type())
dsx1InbandLoopUpCode.setMaxAccess(_G)
if mibBuilder.loadTexts:dsx1InbandLoopUpCode.setStatus(_A)
class _Dsx1InbandLoopUpLength_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(3,8))
_Dsx1InbandLoopUpLength_Type.__name__=_S
_Dsx1InbandLoopUpLength_Object=MibTableColumn
dsx1InbandLoopUpLength=_Dsx1InbandLoopUpLength_Object((1,3,6,1,4,1,164,3,1,6,4,2,1,26),_Dsx1InbandLoopUpLength_Type())
dsx1InbandLoopUpLength.setMaxAccess(_G)
if mibBuilder.loadTexts:dsx1InbandLoopUpLength.setStatus(_A)
if mibBuilder.loadTexts:dsx1InbandLoopUpLength.setUnits('bits')
_Dsx1InbandLoopDownCode_Type=OctetString
_Dsx1InbandLoopDownCode_Object=MibTableColumn
dsx1InbandLoopDownCode=_Dsx1InbandLoopDownCode_Object((1,3,6,1,4,1,164,3,1,6,4,2,1,27),_Dsx1InbandLoopDownCode_Type())
dsx1InbandLoopDownCode.setMaxAccess(_G)
if mibBuilder.loadTexts:dsx1InbandLoopDownCode.setStatus(_A)
class _Dsx1InbandLoopDownLength_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(3,8))
_Dsx1InbandLoopDownLength_Type.__name__=_S
_Dsx1InbandLoopDownLength_Object=MibTableColumn
dsx1InbandLoopDownLength=_Dsx1InbandLoopDownLength_Object((1,3,6,1,4,1,164,3,1,6,4,2,1,28),_Dsx1InbandLoopDownLength_Type())
dsx1InbandLoopDownLength.setMaxAccess(_G)
if mibBuilder.loadTexts:dsx1InbandLoopDownLength.setStatus(_A)
if mibBuilder.loadTexts:dsx1InbandLoopDownLength.setUnits('bits')
_Dsx1TxClockInstance_Type=Unsigned32
_Dsx1TxClockInstance_Object=MibTableColumn
dsx1TxClockInstance=_Dsx1TxClockInstance_Object((1,3,6,1,4,1,164,3,1,6,4,2,1,29),_Dsx1TxClockInstance_Type())
dsx1TxClockInstance.setMaxAccess(_G)
if mibBuilder.loadTexts:dsx1TxClockInstance.setStatus(_A)
class _Dsx1TxPortQuality_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_R,1),('stratum1',2),('stratum2',3),('stratum3',4),('stratum3e',5),('stratum4',6)))
_Dsx1TxPortQuality_Type.__name__=_J
_Dsx1TxPortQuality_Object=MibTableColumn
dsx1TxPortQuality=_Dsx1TxPortQuality_Object((1,3,6,1,4,1,164,3,1,6,4,2,1,30),_Dsx1TxPortQuality_Type())
dsx1TxPortQuality.setMaxAccess(_G)
if mibBuilder.loadTexts:dsx1TxPortQuality.setStatus(_A)
_Dsx1XStatThresholdTable_Object=MibTable
dsx1XStatThresholdTable=_Dsx1XStatThresholdTable_Object((1,3,6,1,4,1,164,3,1,6,4,3))
if mibBuilder.loadTexts:dsx1XStatThresholdTable.setStatus(_A)
_Dsx1XStatThresholdEntry_Object=MibTableRow
dsx1XStatThresholdEntry=_Dsx1XStatThresholdEntry_Object((1,3,6,1,4,1,164,3,1,6,4,3,1))
dsx1XStatThresholdEntry.setIndexNames((0,_I,_W))
if mibBuilder.loadTexts:dsx1XStatThresholdEntry.setStatus(_A)
class _Dsx1LineIntervalLesThreshold_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,900))
_Dsx1LineIntervalLesThreshold_Type.__name__=_S
_Dsx1LineIntervalLesThreshold_Object=MibTableColumn
dsx1LineIntervalLesThreshold=_Dsx1LineIntervalLesThreshold_Object((1,3,6,1,4,1,164,3,1,6,4,3,1,1),_Dsx1LineIntervalLesThreshold_Type())
dsx1LineIntervalLesThreshold.setMaxAccess(_G)
if mibBuilder.loadTexts:dsx1LineIntervalLesThreshold.setStatus(_A)
class _Dsx1PathIntervalCvThreshold_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16383))
_Dsx1PathIntervalCvThreshold_Type.__name__=_S
_Dsx1PathIntervalCvThreshold_Object=MibTableColumn
dsx1PathIntervalCvThreshold=_Dsx1PathIntervalCvThreshold_Object((1,3,6,1,4,1,164,3,1,6,4,3,1,2),_Dsx1PathIntervalCvThreshold_Type())
dsx1PathIntervalCvThreshold.setMaxAccess(_G)
if mibBuilder.loadTexts:dsx1PathIntervalCvThreshold.setStatus(_A)
class _Dsx1PathIntervalEsThreshold_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,900))
_Dsx1PathIntervalEsThreshold_Type.__name__=_S
_Dsx1PathIntervalEsThreshold_Object=MibTableColumn
dsx1PathIntervalEsThreshold=_Dsx1PathIntervalEsThreshold_Object((1,3,6,1,4,1,164,3,1,6,4,3,1,3),_Dsx1PathIntervalEsThreshold_Type())
dsx1PathIntervalEsThreshold.setMaxAccess(_G)
if mibBuilder.loadTexts:dsx1PathIntervalEsThreshold.setStatus(_A)
class _Dsx1PathIntervalSesThreshold_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,900))
_Dsx1PathIntervalSesThreshold_Type.__name__=_S
_Dsx1PathIntervalSesThreshold_Object=MibTableColumn
dsx1PathIntervalSesThreshold=_Dsx1PathIntervalSesThreshold_Object((1,3,6,1,4,1,164,3,1,6,4,3,1,4),_Dsx1PathIntervalSesThreshold_Type())
dsx1PathIntervalSesThreshold.setMaxAccess(_G)
if mibBuilder.loadTexts:dsx1PathIntervalSesThreshold.setStatus(_A)
class _Dsx1PathIntervalSefsThreshold_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,900))
_Dsx1PathIntervalSefsThreshold_Type.__name__=_S
_Dsx1PathIntervalSefsThreshold_Object=MibTableColumn
dsx1PathIntervalSefsThreshold=_Dsx1PathIntervalSefsThreshold_Object((1,3,6,1,4,1,164,3,1,6,4,3,1,5),_Dsx1PathIntervalSefsThreshold_Type())
dsx1PathIntervalSefsThreshold.setMaxAccess(_G)
if mibBuilder.loadTexts:dsx1PathIntervalSefsThreshold.setStatus(_A)
class _Dsx1PathIntervalCssThreshold_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,900))
_Dsx1PathIntervalCssThreshold_Type.__name__=_S
_Dsx1PathIntervalCssThreshold_Object=MibTableColumn
dsx1PathIntervalCssThreshold=_Dsx1PathIntervalCssThreshold_Object((1,3,6,1,4,1,164,3,1,6,4,3,1,6),_Dsx1PathIntervalCssThreshold_Type())
dsx1PathIntervalCssThreshold.setMaxAccess(_G)
if mibBuilder.loadTexts:dsx1PathIntervalCssThreshold.setStatus(_A)
class _Dsx1PathIntervalUasThreshold_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,900))
_Dsx1PathIntervalUasThreshold_Type.__name__=_S
_Dsx1PathIntervalUasThreshold_Object=MibTableColumn
dsx1PathIntervalUasThreshold=_Dsx1PathIntervalUasThreshold_Object((1,3,6,1,4,1,164,3,1,6,4,3,1,7),_Dsx1PathIntervalUasThreshold_Type())
dsx1PathIntervalUasThreshold.setMaxAccess(_G)
if mibBuilder.loadTexts:dsx1PathIntervalUasThreshold.setStatus(_A)
ds1LocalMultiframeAlarmTrap=NotificationType((1,3,6,1,4,1,164,3,1,6,4,0,1))
ds1LocalMultiframeAlarmTrap.setObjects(*((_D,_H),(_E,_F)))
if mibBuilder.loadTexts:ds1LocalMultiframeAlarmTrap.setStatus(_A)
ds1RemoteMultiframeAlarmTrap=NotificationType((1,3,6,1,4,1,164,3,1,6,4,0,2))
ds1RemoteMultiframeAlarmTrap.setObjects(*((_D,_H),(_E,_F)))
if mibBuilder.loadTexts:ds1RemoteMultiframeAlarmTrap.setStatus(_A)
ds1LinkFrameSlipTrap=NotificationType((1,3,6,1,4,1,164,3,1,6,4,0,3))
ds1LinkFrameSlipTrap.setObjects(*((_D,_H),(_E,_F)))
if mibBuilder.loadTexts:ds1LinkFrameSlipTrap.setStatus(_A)
ds1BpvErrorTrap=NotificationType((1,3,6,1,4,1,164,3,1,6,4,0,4))
ds1BpvErrorTrap.setObjects(*((_D,_H),(_E,_F)))
if mibBuilder.loadTexts:ds1BpvErrorTrap.setStatus(_A)
ds1ExcessiveBpvTrap=NotificationType((1,3,6,1,4,1,164,3,1,6,4,0,5))
ds1ExcessiveBpvTrap.setObjects(*((_D,_H),(_D,_Q),(_E,_F)))
if mibBuilder.loadTexts:ds1ExcessiveBpvTrap.setStatus(_A)
ds1Crc4ErrorTrap=NotificationType((1,3,6,1,4,1,164,3,1,6,4,0,6))
ds1Crc4ErrorTrap.setObjects(*((_D,_H),(_E,_F)))
if mibBuilder.loadTexts:ds1Crc4ErrorTrap.setStatus(_A)
ds1ExcessiveErrorRatioTrap=NotificationType((1,3,6,1,4,1,164,3,1,6,4,0,7))
ds1ExcessiveErrorRatioTrap.setObjects(*((_D,_H),(_D,_Q),(_E,_F)))
if mibBuilder.loadTexts:ds1ExcessiveErrorRatioTrap.setStatus(_A)
ds1RemoteSyncLossTrap=NotificationType((1,3,6,1,4,1,164,3,1,6,4,0,8))
ds1RemoteSyncLossTrap.setObjects(*((_D,_H),(_D,_Q),(_E,_F)))
if mibBuilder.loadTexts:ds1RemoteSyncLossTrap.setStatus(_A)
ds1LocalSyncLossTrap=NotificationType((1,3,6,1,4,1,164,3,1,6,4,0,9))
ds1LocalSyncLossTrap.setObjects(*((_D,_H),(_D,_Q),(_E,_F)))
if mibBuilder.loadTexts:ds1LocalSyncLossTrap.setStatus(_A)
ds1AisSyncLossTrap=NotificationType((1,3,6,1,4,1,164,3,1,6,4,0,10))
ds1AisSyncLossTrap.setObjects(*((_D,_H),(_E,_F)))
if mibBuilder.loadTexts:ds1AisSyncLossTrap.setStatus(_A)
ds1AisTrap=NotificationType((1,3,6,1,4,1,164,3,1,6,4,0,11))
ds1AisTrap.setObjects(*((_D,_H),(_D,_Q),(_E,_F)))
if mibBuilder.loadTexts:ds1AisTrap.setStatus(_A)
ds1NetworkRemoteLoopTrap=NotificationType((1,3,6,1,4,1,164,3,1,6,4,0,12))
ds1NetworkRemoteLoopTrap.setObjects(*((_D,_H),(_D,_Q),(_E,_F)))
if mibBuilder.loadTexts:ds1NetworkRemoteLoopTrap.setStatus(_A)
ds1RemoteLoopTrap=NotificationType((1,3,6,1,4,1,164,3,1,6,4,0,13))
ds1RemoteLoopTrap.setObjects(*((_D,_H),(_D,_Q),(_E,_F)))
if mibBuilder.loadTexts:ds1RemoteLoopTrap.setStatus(_A)
ds1LocalLoopTrap=NotificationType((1,3,6,1,4,1,164,3,1,6,4,0,14))
ds1LocalLoopTrap.setObjects(*((_D,_H),(_D,_Q),(_E,_F)))
if mibBuilder.loadTexts:ds1LocalLoopTrap.setStatus(_A)
ds1ExcessiveFrameSlipTrap=NotificationType((1,3,6,1,4,1,164,3,1,6,4,0,15))
ds1ExcessiveFrameSlipTrap.setObjects(*((_D,_H),(_D,_Q),(_E,_F)))
if mibBuilder.loadTexts:ds1ExcessiveFrameSlipTrap.setStatus(_A)
ds1ExcessiveCrc4ErrorTrap=NotificationType((1,3,6,1,4,1,164,3,1,6,4,0,16))
ds1ExcessiveCrc4ErrorTrap.setObjects(*((_D,_H),(_D,_Q),(_E,_F)))
if mibBuilder.loadTexts:ds1ExcessiveCrc4ErrorTrap.setStatus(_A)
ds1ExcessiveLocalMfAlarmTrap=NotificationType((1,3,6,1,4,1,164,3,1,6,4,0,17))
ds1ExcessiveLocalMfAlarmTrap.setObjects(*((_D,_H),(_D,_Q),(_E,_F)))
if mibBuilder.loadTexts:ds1ExcessiveLocalMfAlarmTrap.setStatus(_A)
ds1ExcessiveRemoteMfAlarmTrap=NotificationType((1,3,6,1,4,1,164,3,1,6,4,0,18))
ds1ExcessiveRemoteMfAlarmTrap.setObjects(*((_D,_H),(_D,_Q),(_E,_F)))
if mibBuilder.loadTexts:ds1ExcessiveRemoteMfAlarmTrap.setStatus(_A)
ds1ExcessiveRemoteSyncLossTrap=NotificationType((1,3,6,1,4,1,164,3,1,6,4,0,19))
ds1ExcessiveRemoteSyncLossTrap.setObjects(*((_D,_H),(_D,_Q),(_E,_F)))
if mibBuilder.loadTexts:ds1ExcessiveRemoteSyncLossTrap.setStatus(_A)
ds1ExcessiveLocalSyncLossTrap=NotificationType((1,3,6,1,4,1,164,3,1,6,4,0,20))
ds1ExcessiveLocalSyncLossTrap.setObjects(*((_D,_H),(_D,_Q),(_E,_F)))
if mibBuilder.loadTexts:ds1ExcessiveLocalSyncLossTrap.setStatus(_A)
ds1SignalLossTrap=NotificationType((1,3,6,1,4,1,164,3,1,6,4,0,21))
ds1SignalLossTrap.setObjects(*((_D,_H),(_D,_Q),(_E,_F)))
if mibBuilder.loadTexts:ds1SignalLossTrap.setStatus(_A)
e1t1Ais=NotificationType((1,3,6,1,4,1,164,3,1,6,4,0,25))
e1t1Ais.setObjects(*((_B,_O),(_B,_K),(_B,_M),(_B,_N),(_B,_L),(_B,_P),(_E,_F),(_I,_U)))
if mibBuilder.loadTexts:e1t1Ais.setStatus(_A)
e1t1Lof=NotificationType((1,3,6,1,4,1,164,3,1,6,4,0,26))
e1t1Lof.setObjects(*((_B,_O),(_B,_K),(_B,_M),(_B,_N),(_B,_L),(_B,_P),(_E,_F),(_I,_U)))
if mibBuilder.loadTexts:e1t1Lof.setStatus(_A)
e1t1Rai=NotificationType((1,3,6,1,4,1,164,3,1,6,4,0,27))
e1t1Rai.setObjects(*((_B,_O),(_B,_K),(_B,_M),(_B,_N),(_B,_L),(_B,_P),(_E,_F),(_I,_U)))
if mibBuilder.loadTexts:e1t1Rai.setStatus(_A)
e1t1Lomf=NotificationType((1,3,6,1,4,1,164,3,1,6,4,0,28))
e1t1Lomf.setObjects(*((_B,_O),(_B,_K),(_B,_M),(_B,_N),(_B,_L),(_B,_P),(_E,_F),(_I,_U)))
if mibBuilder.loadTexts:e1t1Lomf.setStatus(_A)
e1t1Los=NotificationType((1,3,6,1,4,1,164,3,1,6,4,0,30))
e1t1Los.setObjects(*((_B,_O),(_B,_K),(_B,_M),(_B,_N),(_B,_L),(_B,_P),(_E,_F),(_I,_U)))
if mibBuilder.loadTexts:e1t1Los.setStatus(_A)
e1t1Loopback=NotificationType((1,3,6,1,4,1,164,3,1,6,4,0,36))
e1t1Loopback.setObjects(*((_B,_O),(_B,_K),(_B,_M),(_B,_N),(_B,_L),(_B,_P),(_E,_F),(_I,_h)))
if mibBuilder.loadTexts:e1t1Loopback.setStatus(_A)
e1t1LoopbackOff=NotificationType((1,3,6,1,4,1,164,3,1,6,4,0,37))
e1t1LoopbackOff.setObjects(*((_B,_O),(_B,_K),(_B,_M),(_B,_N),(_B,_L),(_B,_P),(_E,_F)))
if mibBuilder.loadTexts:e1t1LoopbackOff.setStatus(_A)
e1t1EsLineTca=NotificationType((1,3,6,1,4,1,164,3,1,6,4,0,38))
e1t1EsLineTca.setObjects(*((_B,_O),(_B,_K),(_B,_M),(_B,_N),(_B,_L),(_B,_P),(_E,_F),(_I,_b),(_D,_o)))
if mibBuilder.loadTexts:e1t1EsLineTca.setStatus(_A)
e1t1CvPathTca=NotificationType((1,3,6,1,4,1,164,3,1,6,4,0,39))
e1t1CvPathTca.setObjects(*((_B,_O),(_B,_K),(_B,_M),(_B,_N),(_B,_L),(_B,_P),(_E,_F),(_I,_d),(_D,_p)))
if mibBuilder.loadTexts:e1t1CvPathTca.setStatus(_A)
e1t1EsPathTca=NotificationType((1,3,6,1,4,1,164,3,1,6,4,0,40))
e1t1EsPathTca.setObjects(*((_B,_O),(_B,_K),(_B,_M),(_B,_N),(_B,_L),(_B,_P),(_E,_F),(_I,_Z),(_D,_q)))
if mibBuilder.loadTexts:e1t1EsPathTca.setStatus(_A)
e1t1SesPathTca=NotificationType((1,3,6,1,4,1,164,3,1,6,4,0,41))
e1t1SesPathTca.setObjects(*((_B,_O),(_B,_K),(_B,_M),(_B,_N),(_B,_L),(_B,_P),(_E,_F),(_I,_f),(_D,_r)))
if mibBuilder.loadTexts:e1t1SesPathTca.setStatus(_A)
e1t1SefsPathTca=NotificationType((1,3,6,1,4,1,164,3,1,6,4,0,42))
e1t1SefsPathTca.setObjects(*((_B,_O),(_B,_K),(_B,_M),(_B,_N),(_B,_L),(_B,_P),(_E,_F),(_I,_e),(_D,_s)))
if mibBuilder.loadTexts:e1t1SefsPathTca.setStatus(_A)
e1t1CssPathTca=NotificationType((1,3,6,1,4,1,164,3,1,6,4,0,43))
e1t1CssPathTca.setObjects(*((_B,_O),(_B,_K),(_B,_M),(_B,_N),(_B,_L),(_B,_P),(_E,_F),(_I,_Y),(_D,_t)))
if mibBuilder.loadTexts:e1t1CssPathTca.setStatus(_A)
e1t1UasPathTca=NotificationType((1,3,6,1,4,1,164,3,1,6,4,0,44))
e1t1UasPathTca.setObjects(*((_B,_O),(_B,_K),(_B,_M),(_B,_N),(_B,_L),(_B,_P),(_E,_F),(_I,_g),(_D,_u)))
if mibBuilder.loadTexts:e1t1UasPathTca.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'ds1Interface':ds1Interface,'prtDS1Events':prtDS1Events,'ds1LocalMultiframeAlarmTrap':ds1LocalMultiframeAlarmTrap,'ds1RemoteMultiframeAlarmTrap':ds1RemoteMultiframeAlarmTrap,'ds1LinkFrameSlipTrap':ds1LinkFrameSlipTrap,'ds1BpvErrorTrap':ds1BpvErrorTrap,'ds1ExcessiveBpvTrap':ds1ExcessiveBpvTrap,'ds1Crc4ErrorTrap':ds1Crc4ErrorTrap,'ds1ExcessiveErrorRatioTrap':ds1ExcessiveErrorRatioTrap,'ds1RemoteSyncLossTrap':ds1RemoteSyncLossTrap,'ds1LocalSyncLossTrap':ds1LocalSyncLossTrap,'ds1AisSyncLossTrap':ds1AisSyncLossTrap,'ds1AisTrap':ds1AisTrap,'ds1NetworkRemoteLoopTrap':ds1NetworkRemoteLoopTrap,'ds1RemoteLoopTrap':ds1RemoteLoopTrap,'ds1LocalLoopTrap':ds1LocalLoopTrap,'ds1ExcessiveFrameSlipTrap':ds1ExcessiveFrameSlipTrap,'ds1ExcessiveCrc4ErrorTrap':ds1ExcessiveCrc4ErrorTrap,'ds1ExcessiveLocalMfAlarmTrap':ds1ExcessiveLocalMfAlarmTrap,'ds1ExcessiveRemoteMfAlarmTrap':ds1ExcessiveRemoteMfAlarmTrap,'ds1ExcessiveRemoteSyncLossTrap':ds1ExcessiveRemoteSyncLossTrap,'ds1ExcessiveLocalSyncLossTrap':ds1ExcessiveLocalSyncLossTrap,'ds1SignalLossTrap':ds1SignalLossTrap,'e1t1Ais':e1t1Ais,'e1t1Lof':e1t1Lof,'e1t1Rai':e1t1Rai,'e1t1Lomf':e1t1Lomf,'e1t1Los':e1t1Los,'e1t1Loopback':e1t1Loopback,'e1t1LoopbackOff':e1t1LoopbackOff,'e1t1EsLineTca':e1t1EsLineTca,'e1t1CvPathTca':e1t1CvPathTca,'e1t1EsPathTca':e1t1EsPathTca,'e1t1SesPathTca':e1t1SesPathTca,'e1t1SefsPathTca':e1t1SefsPathTca,'e1t1CssPathTca':e1t1CssPathTca,'e1t1UasPathTca':e1t1UasPathTca,'prtDs1PerfHistory':prtDs1PerfHistory,'dsx1XCurrentTable':dsx1XCurrentTable,'dsx1XCurrentEntry':dsx1XCurrentEntry,'dsx1CurrentLOS':dsx1CurrentLOS,'dsx1CurrentLOF':dsx1CurrentLOF,'dsx1CurrentLOC':dsx1CurrentLOC,'dsx1CurrentAIS':dsx1CurrentAIS,'dsx1CurrentRAI':dsx1CurrentRAI,'dsx1CurrentLOMF':dsx1CurrentLOMF,'dsx1CurrentFEBE':dsx1CurrentFEBE,'dsx1CurrentStatus':dsx1CurrentStatus,'dsx1CurrentBPV':dsx1CurrentBPV,'dsx1CurrentLOCRCMF':dsx1CurrentLOCRCMF,'dsx1CurrentLOFC':dsx1CurrentLOFC,'dsx1CurrentCRCErrors':dsx1CurrentCRCErrors,'dsx1CurrentLSES':dsx1CurrentLSES,'dsx1CurrentFC':dsx1CurrentFC,'dsx1XIntervalTable':dsx1XIntervalTable,'dsx1XIntervalEntry':dsx1XIntervalEntry,'dsx1IntervalLOS':dsx1IntervalLOS,'dsx1IntervalLOF':dsx1IntervalLOF,'dsx1IntervalLOC':dsx1IntervalLOC,'dsx1IntervalAIS':dsx1IntervalAIS,'dsx1IntervalRAI':dsx1IntervalRAI,'dsx1IntervalLOMF':dsx1IntervalLOMF,'dsx1IntervalFEBE':dsx1IntervalFEBE,'dsx1IntervalStatus':dsx1IntervalStatus,'dsx1IntervalBPV':dsx1IntervalBPV,'dsx1IntervalLOCRCMF':dsx1IntervalLOCRCMF,'dsx1IntervalLOFC':dsx1IntervalLOFC,'dsx1IntervalLSES':dsx1IntervalLSES,'dsx1IntervalFC':dsx1IntervalFC,'dsx1XTotalTable':dsx1XTotalTable,'dsx1XTotalEntry':dsx1XTotalEntry,'dsx1TotalLOS':dsx1TotalLOS,'dsx1TotalLOF':dsx1TotalLOF,'dsx1TotalAIS':dsx1TotalAIS,'dsx1TotalRAI':dsx1TotalRAI,'dsx1TotalBPV':dsx1TotalBPV,'dsx1TotalLOFC':dsx1TotalLOFC,'dsx1TotalLSES':dsx1TotalLSES,'dsx1TotalFC':dsx1TotalFC,'dsx1DataStreamStatTable':dsx1DataStreamStatTable,'dsx1DataStreamStatEntry':dsx1DataStreamStatEntry,_j:dsx1DataStreamStatIfIndex,_k:dsx1DataStreamStatIndex,'dsx1DataStreamStatValid':dsx1DataStreamStatValid,'dsx1DataStreamStatInFrames':dsx1DataStreamStatInFrames,'dsx1DataStreamStatInBytes':dsx1DataStreamStatInBytes,'dsx1DataStreamStatInDiscards':dsx1DataStreamStatInDiscards,'dsx1DataStreamStatInErrors':dsx1DataStreamStatInErrors,'dsx1DataStreamStatOutFrames':dsx1DataStreamStatOutFrames,'dsx1DataStreamStatOutBytes':dsx1DataStreamStatOutBytes,'dsx1DataStreamStatOutDiscards':dsx1DataStreamStatOutDiscards,'dsx1DataStreamStatOutErrors':dsx1DataStreamStatOutErrors,'dsx1XConfigTable':dsx1XConfigTable,'dsx1XConfigEntry':dsx1XConfigEntry,'dsx1IdleCode':dsx1IdleCode,'dsx1LineMode':dsx1LineMode,'dsx1dBTxGain':dsx1dBTxGain,'dsx1RxSensitivity':dsx1RxSensitivity,'dsx1RestoreTime':dsx1RestoreTime,'dsx1TcFirstSignal':dsx1TcFirstSignal,'dsx1TcSignal':dsx1TcSignal,'dsx1TcPattern':dsx1TcPattern,'dsx1Scramble':dsx1Scramble,'dsx1LineAdaptiveTimingMode':dsx1LineAdaptiveTimingMode,'dsx1TxClockSource':dsx1TxClockSource,'dsx1AisEnable':dsx1AisEnable,'dsx1TsEchoCancel':dsx1TsEchoCancel,'dsx1EchoCancelerModule':dsx1EchoCancelerModule,'dsx1PortFunction':dsx1PortFunction,'dsx1PortMultiplier':dsx1PortMultiplier,'dsx1LeasedLine':dsx1LeasedLine,'dsx1CsuLoop':dsx1CsuLoop,'dsx1ClockSource':dsx1ClockSource,'dsx1OosSignal':dsx1OosSignal,'dsx1BundleNextIndex':dsx1BundleNextIndex,'dsx1CRC6CalcMode':dsx1CRC6CalcMode,'dsx1SendUponFail':dsx1SendUponFail,'dsx1InbandLoopSignal':dsx1InbandLoopSignal,'dsx1InbandLoopUpCode':dsx1InbandLoopUpCode,'dsx1InbandLoopUpLength':dsx1InbandLoopUpLength,'dsx1InbandLoopDownCode':dsx1InbandLoopDownCode,'dsx1InbandLoopDownLength':dsx1InbandLoopDownLength,'dsx1TxClockInstance':dsx1TxClockInstance,'dsx1TxPortQuality':dsx1TxPortQuality,'dsx1XStatThresholdTable':dsx1XStatThresholdTable,'dsx1XStatThresholdEntry':dsx1XStatThresholdEntry,_o:dsx1LineIntervalLesThreshold,_p:dsx1PathIntervalCvThreshold,_q:dsx1PathIntervalEsThreshold,_r:dsx1PathIntervalSesThreshold,_s:dsx1PathIntervalSefsThreshold,_t:dsx1PathIntervalCssThreshold,_u:dsx1PathIntervalUasThreshold})