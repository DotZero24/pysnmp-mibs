_A3='g9981Perf1DayGroup'
_A2='g9981Perf15MinGroup'
_A1='g9981PerfCurrGroup'
_A0='g9981NotificationGroup'
_z='g9981AlarmConfGroup'
_y='g9981BasicGroup'
_x='g9981DnDiffDelayToleranceExceeded'
_w='g9981UpDiffDelayToleranceExceeded'
_v='g9981PortPm1DayIntervalValid'
_u='g9981PortPm1DayIntervalDnDiffDelay'
_t='g9981PortPm1DayIntervalUpDiffDelay'
_s='g9981PortPm1DayIntervalTxLostCells'
_r='g9981PortPm1DayIntervalRxLostCells'
_q='g9981PortPm1DayIntervalMoniTime'
_p='g9981PortPm15MinIntervalValid'
_o='g9981PortPm15MinIntervalDnDiffDelay'
_n='g9981PortPm15MinIntervalUpDiffDelay'
_m='g9981PortPm15MinIntervalTxLostCells'
_l='g9981PortPm15MinIntervalRxLostCells'
_k='g9981PortPm15MinIntervalMoniTime'
_j='g9981PortPmCur1DayDnDiffDelay'
_i='g9981PortPmCur1DayUpDiffDelay'
_h='g9981PortPmCur1DayTxLostCells'
_g='g9981PortPmCur1DayRxLostCells'
_f='g9981PortPmCur1DayTimeElapsed'
_e='g9981PortPmCur1DayInvalidIntervals'
_d='g9981PortPmCur1DayValidIntervals'
_c='g9981PortPmCur15MinDnDiffDelay'
_b='g9981PortPmCur15MinUpDiffDelay'
_a='g9981PortPmCur15MinTxLostCells'
_Z='g9981PortPmCur15MinRxLostCells'
_Y='g9981PortPmCur15MinTimeElapsed'
_X='g9981PortPmCur15MinInvalidIntervals'
_W='g9981PortPmCur15MinValidIntervals'
_V='g9981PortConfDiffDelayToleranceExceededEnable'
_U='g9981PortStatTxLostCells'
_T='g9981PortStatRxLostCells'
_S='g9981PortPm1DayIntervalIndex'
_R='not-accessible'
_Q='g9981PortPm15MinIntervalIndex'
_P='milliseconds'
_O='g9981PortConfDnDiffDelayTolerance'
_N='g9981PortConfUpDiffDelayTolerance'
_M='g9981PortStatMaxDnDiffDelay'
_L='g9981PortStatMaxUpDiffDelay'
_K='read-write'
_J='MilliSeconds'
_I='seconds'
_H='Unsigned32'
_G='ifIndex'
_F='IF-MIB'
_E='0.1 ms'
_D='cells'
_C='read-only'
_B='G9981-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
HCPerfCurrentCount,HCPerfIntervalCount,HCPerfInvalidIntervals,HCPerfTimeElapsed,HCPerfValidIntervals=mibBuilder.importSymbols('HC-PerfHist-TC-MIB','HCPerfCurrentCount','HCPerfIntervalCount','HCPerfInvalidIntervals','HCPerfTimeElapsed','HCPerfValidIntervals')
ifIndex,=mibBuilder.importSymbols(_F,_G)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso,mib_2=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_H,'iso','mib-2')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
g9981MIB=ModuleIdentity((1,3,6,1,2,1,208))
if mibBuilder.loadTexts:g9981MIB.setRevisions(('2013-02-20 00:00',))
class MilliSeconds(TextualConvention,Unsigned32):status=_A;displayHint='d'
_G9981Objects_ObjectIdentity=ObjectIdentity
g9981Objects=_G9981Objects_ObjectIdentity((1,3,6,1,2,1,208,1))
_G9981Port_ObjectIdentity=ObjectIdentity
g9981Port=_G9981Port_ObjectIdentity((1,3,6,1,2,1,208,1,1))
_G9981PortNotifications_ObjectIdentity=ObjectIdentity
g9981PortNotifications=_G9981PortNotifications_ObjectIdentity((1,3,6,1,2,1,208,1,1,0))
_G9981PortConfTable_Object=MibTable
g9981PortConfTable=_G9981PortConfTable_Object((1,3,6,1,2,1,208,1,1,1))
if mibBuilder.loadTexts:g9981PortConfTable.setStatus(_A)
_G9981PortConfEntry_Object=MibTableRow
g9981PortConfEntry=_G9981PortConfEntry_Object((1,3,6,1,2,1,208,1,1,1,1))
g9981PortConfEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:g9981PortConfEntry.setStatus(_A)
class _G9981PortConfUpDiffDelayTolerance_Type(MilliSeconds):subtypeSpec=MilliSeconds.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2047))
_G9981PortConfUpDiffDelayTolerance_Type.__name__=_J
_G9981PortConfUpDiffDelayTolerance_Object=MibTableColumn
g9981PortConfUpDiffDelayTolerance=_G9981PortConfUpDiffDelayTolerance_Object((1,3,6,1,2,1,208,1,1,1,1,1),_G9981PortConfUpDiffDelayTolerance_Type())
g9981PortConfUpDiffDelayTolerance.setMaxAccess(_K)
if mibBuilder.loadTexts:g9981PortConfUpDiffDelayTolerance.setStatus(_A)
if mibBuilder.loadTexts:g9981PortConfUpDiffDelayTolerance.setUnits(_P)
class _G9981PortConfDnDiffDelayTolerance_Type(MilliSeconds):subtypeSpec=MilliSeconds.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2047))
_G9981PortConfDnDiffDelayTolerance_Type.__name__=_J
_G9981PortConfDnDiffDelayTolerance_Object=MibTableColumn
g9981PortConfDnDiffDelayTolerance=_G9981PortConfDnDiffDelayTolerance_Object((1,3,6,1,2,1,208,1,1,1,1,2),_G9981PortConfDnDiffDelayTolerance_Type())
g9981PortConfDnDiffDelayTolerance.setMaxAccess(_K)
if mibBuilder.loadTexts:g9981PortConfDnDiffDelayTolerance.setStatus(_A)
if mibBuilder.loadTexts:g9981PortConfDnDiffDelayTolerance.setUnits(_P)
_G9981PortConfDiffDelayToleranceExceededEnable_Type=TruthValue
_G9981PortConfDiffDelayToleranceExceededEnable_Object=MibTableColumn
g9981PortConfDiffDelayToleranceExceededEnable=_G9981PortConfDiffDelayToleranceExceededEnable_Object((1,3,6,1,2,1,208,1,1,1,1,3),_G9981PortConfDiffDelayToleranceExceededEnable_Type())
g9981PortConfDiffDelayToleranceExceededEnable.setMaxAccess(_K)
if mibBuilder.loadTexts:g9981PortConfDiffDelayToleranceExceededEnable.setStatus(_A)
_G9981PortStatTable_Object=MibTable
g9981PortStatTable=_G9981PortStatTable_Object((1,3,6,1,2,1,208,1,1,2))
if mibBuilder.loadTexts:g9981PortStatTable.setStatus(_A)
_G9981PortStatEntry_Object=MibTableRow
g9981PortStatEntry=_G9981PortStatEntry_Object((1,3,6,1,2,1,208,1,1,2,1))
g9981PortStatEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:g9981PortStatEntry.setStatus(_A)
_G9981PortStatRxLostCells_Type=Counter32
_G9981PortStatRxLostCells_Object=MibTableColumn
g9981PortStatRxLostCells=_G9981PortStatRxLostCells_Object((1,3,6,1,2,1,208,1,1,2,1,1),_G9981PortStatRxLostCells_Type())
g9981PortStatRxLostCells.setMaxAccess(_C)
if mibBuilder.loadTexts:g9981PortStatRxLostCells.setStatus(_A)
if mibBuilder.loadTexts:g9981PortStatRxLostCells.setUnits(_D)
_G9981PortStatTxLostCells_Type=Counter32
_G9981PortStatTxLostCells_Object=MibTableColumn
g9981PortStatTxLostCells=_G9981PortStatTxLostCells_Object((1,3,6,1,2,1,208,1,1,2,1,2),_G9981PortStatTxLostCells_Type())
g9981PortStatTxLostCells.setMaxAccess(_C)
if mibBuilder.loadTexts:g9981PortStatTxLostCells.setStatus(_A)
if mibBuilder.loadTexts:g9981PortStatTxLostCells.setUnits(_D)
_G9981PortStatMaxUpDiffDelay_Type=Unsigned32
_G9981PortStatMaxUpDiffDelay_Object=MibTableColumn
g9981PortStatMaxUpDiffDelay=_G9981PortStatMaxUpDiffDelay_Object((1,3,6,1,2,1,208,1,1,2,1,3),_G9981PortStatMaxUpDiffDelay_Type())
g9981PortStatMaxUpDiffDelay.setMaxAccess(_C)
if mibBuilder.loadTexts:g9981PortStatMaxUpDiffDelay.setStatus(_A)
if mibBuilder.loadTexts:g9981PortStatMaxUpDiffDelay.setUnits(_E)
_G9981PortStatMaxDnDiffDelay_Type=Unsigned32
_G9981PortStatMaxDnDiffDelay_Object=MibTableColumn
g9981PortStatMaxDnDiffDelay=_G9981PortStatMaxDnDiffDelay_Object((1,3,6,1,2,1,208,1,1,2,1,4),_G9981PortStatMaxDnDiffDelay_Type())
g9981PortStatMaxDnDiffDelay.setMaxAccess(_C)
if mibBuilder.loadTexts:g9981PortStatMaxDnDiffDelay.setStatus(_A)
if mibBuilder.loadTexts:g9981PortStatMaxDnDiffDelay.setUnits(_E)
_G9981PM_ObjectIdentity=ObjectIdentity
g9981PM=_G9981PM_ObjectIdentity((1,3,6,1,2,1,208,1,1,3))
_G9981PortPmCurTable_Object=MibTable
g9981PortPmCurTable=_G9981PortPmCurTable_Object((1,3,6,1,2,1,208,1,1,3,1))
if mibBuilder.loadTexts:g9981PortPmCurTable.setStatus(_A)
_G9981PortPmCurEntry_Object=MibTableRow
g9981PortPmCurEntry=_G9981PortPmCurEntry_Object((1,3,6,1,2,1,208,1,1,3,1,1))
g9981PortPmCurEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:g9981PortPmCurEntry.setStatus(_A)
_G9981PortPmCur15MinValidIntervals_Type=HCPerfValidIntervals
_G9981PortPmCur15MinValidIntervals_Object=MibTableColumn
g9981PortPmCur15MinValidIntervals=_G9981PortPmCur15MinValidIntervals_Object((1,3,6,1,2,1,208,1,1,3,1,1,1),_G9981PortPmCur15MinValidIntervals_Type())
g9981PortPmCur15MinValidIntervals.setMaxAccess(_C)
if mibBuilder.loadTexts:g9981PortPmCur15MinValidIntervals.setStatus(_A)
_G9981PortPmCur15MinInvalidIntervals_Type=HCPerfInvalidIntervals
_G9981PortPmCur15MinInvalidIntervals_Object=MibTableColumn
g9981PortPmCur15MinInvalidIntervals=_G9981PortPmCur15MinInvalidIntervals_Object((1,3,6,1,2,1,208,1,1,3,1,1,2),_G9981PortPmCur15MinInvalidIntervals_Type())
g9981PortPmCur15MinInvalidIntervals.setMaxAccess(_C)
if mibBuilder.loadTexts:g9981PortPmCur15MinInvalidIntervals.setStatus(_A)
_G9981PortPmCur15MinTimeElapsed_Type=HCPerfTimeElapsed
_G9981PortPmCur15MinTimeElapsed_Object=MibTableColumn
g9981PortPmCur15MinTimeElapsed=_G9981PortPmCur15MinTimeElapsed_Object((1,3,6,1,2,1,208,1,1,3,1,1,3),_G9981PortPmCur15MinTimeElapsed_Type())
g9981PortPmCur15MinTimeElapsed.setMaxAccess(_C)
if mibBuilder.loadTexts:g9981PortPmCur15MinTimeElapsed.setStatus(_A)
if mibBuilder.loadTexts:g9981PortPmCur15MinTimeElapsed.setUnits(_I)
_G9981PortPmCur15MinRxLostCells_Type=HCPerfCurrentCount
_G9981PortPmCur15MinRxLostCells_Object=MibTableColumn
g9981PortPmCur15MinRxLostCells=_G9981PortPmCur15MinRxLostCells_Object((1,3,6,1,2,1,208,1,1,3,1,1,4),_G9981PortPmCur15MinRxLostCells_Type())
g9981PortPmCur15MinRxLostCells.setMaxAccess(_C)
if mibBuilder.loadTexts:g9981PortPmCur15MinRxLostCells.setStatus(_A)
if mibBuilder.loadTexts:g9981PortPmCur15MinRxLostCells.setUnits(_D)
_G9981PortPmCur15MinTxLostCells_Type=HCPerfCurrentCount
_G9981PortPmCur15MinTxLostCells_Object=MibTableColumn
g9981PortPmCur15MinTxLostCells=_G9981PortPmCur15MinTxLostCells_Object((1,3,6,1,2,1,208,1,1,3,1,1,5),_G9981PortPmCur15MinTxLostCells_Type())
g9981PortPmCur15MinTxLostCells.setMaxAccess(_C)
if mibBuilder.loadTexts:g9981PortPmCur15MinTxLostCells.setStatus(_A)
if mibBuilder.loadTexts:g9981PortPmCur15MinTxLostCells.setUnits(_D)
_G9981PortPmCur15MinUpDiffDelay_Type=HCPerfCurrentCount
_G9981PortPmCur15MinUpDiffDelay_Object=MibTableColumn
g9981PortPmCur15MinUpDiffDelay=_G9981PortPmCur15MinUpDiffDelay_Object((1,3,6,1,2,1,208,1,1,3,1,1,6),_G9981PortPmCur15MinUpDiffDelay_Type())
g9981PortPmCur15MinUpDiffDelay.setMaxAccess(_C)
if mibBuilder.loadTexts:g9981PortPmCur15MinUpDiffDelay.setStatus(_A)
if mibBuilder.loadTexts:g9981PortPmCur15MinUpDiffDelay.setUnits(_E)
_G9981PortPmCur15MinDnDiffDelay_Type=HCPerfCurrentCount
_G9981PortPmCur15MinDnDiffDelay_Object=MibTableColumn
g9981PortPmCur15MinDnDiffDelay=_G9981PortPmCur15MinDnDiffDelay_Object((1,3,6,1,2,1,208,1,1,3,1,1,7),_G9981PortPmCur15MinDnDiffDelay_Type())
g9981PortPmCur15MinDnDiffDelay.setMaxAccess(_C)
if mibBuilder.loadTexts:g9981PortPmCur15MinDnDiffDelay.setStatus(_A)
if mibBuilder.loadTexts:g9981PortPmCur15MinDnDiffDelay.setUnits(_E)
class _G9981PortPmCur1DayValidIntervals_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_G9981PortPmCur1DayValidIntervals_Type.__name__=_H
_G9981PortPmCur1DayValidIntervals_Object=MibTableColumn
g9981PortPmCur1DayValidIntervals=_G9981PortPmCur1DayValidIntervals_Object((1,3,6,1,2,1,208,1,1,3,1,1,8),_G9981PortPmCur1DayValidIntervals_Type())
g9981PortPmCur1DayValidIntervals.setMaxAccess(_C)
if mibBuilder.loadTexts:g9981PortPmCur1DayValidIntervals.setStatus(_A)
if mibBuilder.loadTexts:g9981PortPmCur1DayValidIntervals.setUnits('days')
class _G9981PortPmCur1DayInvalidIntervals_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_G9981PortPmCur1DayInvalidIntervals_Type.__name__=_H
_G9981PortPmCur1DayInvalidIntervals_Object=MibTableColumn
g9981PortPmCur1DayInvalidIntervals=_G9981PortPmCur1DayInvalidIntervals_Object((1,3,6,1,2,1,208,1,1,3,1,1,9),_G9981PortPmCur1DayInvalidIntervals_Type())
g9981PortPmCur1DayInvalidIntervals.setMaxAccess(_C)
if mibBuilder.loadTexts:g9981PortPmCur1DayInvalidIntervals.setStatus(_A)
if mibBuilder.loadTexts:g9981PortPmCur1DayInvalidIntervals.setUnits('days')
_G9981PortPmCur1DayTimeElapsed_Type=HCPerfTimeElapsed
_G9981PortPmCur1DayTimeElapsed_Object=MibTableColumn
g9981PortPmCur1DayTimeElapsed=_G9981PortPmCur1DayTimeElapsed_Object((1,3,6,1,2,1,208,1,1,3,1,1,10),_G9981PortPmCur1DayTimeElapsed_Type())
g9981PortPmCur1DayTimeElapsed.setMaxAccess(_C)
if mibBuilder.loadTexts:g9981PortPmCur1DayTimeElapsed.setStatus(_A)
if mibBuilder.loadTexts:g9981PortPmCur1DayTimeElapsed.setUnits(_I)
_G9981PortPmCur1DayRxLostCells_Type=HCPerfCurrentCount
_G9981PortPmCur1DayRxLostCells_Object=MibTableColumn
g9981PortPmCur1DayRxLostCells=_G9981PortPmCur1DayRxLostCells_Object((1,3,6,1,2,1,208,1,1,3,1,1,11),_G9981PortPmCur1DayRxLostCells_Type())
g9981PortPmCur1DayRxLostCells.setMaxAccess(_C)
if mibBuilder.loadTexts:g9981PortPmCur1DayRxLostCells.setStatus(_A)
if mibBuilder.loadTexts:g9981PortPmCur1DayRxLostCells.setUnits(_D)
_G9981PortPmCur1DayTxLostCells_Type=HCPerfCurrentCount
_G9981PortPmCur1DayTxLostCells_Object=MibTableColumn
g9981PortPmCur1DayTxLostCells=_G9981PortPmCur1DayTxLostCells_Object((1,3,6,1,2,1,208,1,1,3,1,1,12),_G9981PortPmCur1DayTxLostCells_Type())
g9981PortPmCur1DayTxLostCells.setMaxAccess(_C)
if mibBuilder.loadTexts:g9981PortPmCur1DayTxLostCells.setStatus(_A)
if mibBuilder.loadTexts:g9981PortPmCur1DayTxLostCells.setUnits(_D)
_G9981PortPmCur1DayUpDiffDelay_Type=HCPerfCurrentCount
_G9981PortPmCur1DayUpDiffDelay_Object=MibTableColumn
g9981PortPmCur1DayUpDiffDelay=_G9981PortPmCur1DayUpDiffDelay_Object((1,3,6,1,2,1,208,1,1,3,1,1,13),_G9981PortPmCur1DayUpDiffDelay_Type())
g9981PortPmCur1DayUpDiffDelay.setMaxAccess(_C)
if mibBuilder.loadTexts:g9981PortPmCur1DayUpDiffDelay.setStatus(_A)
if mibBuilder.loadTexts:g9981PortPmCur1DayUpDiffDelay.setUnits(_E)
_G9981PortPmCur1DayDnDiffDelay_Type=HCPerfCurrentCount
_G9981PortPmCur1DayDnDiffDelay_Object=MibTableColumn
g9981PortPmCur1DayDnDiffDelay=_G9981PortPmCur1DayDnDiffDelay_Object((1,3,6,1,2,1,208,1,1,3,1,1,14),_G9981PortPmCur1DayDnDiffDelay_Type())
g9981PortPmCur1DayDnDiffDelay.setMaxAccess(_C)
if mibBuilder.loadTexts:g9981PortPmCur1DayDnDiffDelay.setStatus(_A)
if mibBuilder.loadTexts:g9981PortPmCur1DayDnDiffDelay.setUnits(_E)
_G9981PortPm15MinTable_Object=MibTable
g9981PortPm15MinTable=_G9981PortPm15MinTable_Object((1,3,6,1,2,1,208,1,1,3,2))
if mibBuilder.loadTexts:g9981PortPm15MinTable.setStatus(_A)
_G9981PortPm15MinEntry_Object=MibTableRow
g9981PortPm15MinEntry=_G9981PortPm15MinEntry_Object((1,3,6,1,2,1,208,1,1,3,2,1))
g9981PortPm15MinEntry.setIndexNames((0,_F,_G),(0,_B,_Q))
if mibBuilder.loadTexts:g9981PortPm15MinEntry.setStatus(_A)
class _G9981PortPm15MinIntervalIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,96))
_G9981PortPm15MinIntervalIndex_Type.__name__=_H
_G9981PortPm15MinIntervalIndex_Object=MibTableColumn
g9981PortPm15MinIntervalIndex=_G9981PortPm15MinIntervalIndex_Object((1,3,6,1,2,1,208,1,1,3,2,1,1),_G9981PortPm15MinIntervalIndex_Type())
g9981PortPm15MinIntervalIndex.setMaxAccess(_R)
if mibBuilder.loadTexts:g9981PortPm15MinIntervalIndex.setStatus(_A)
_G9981PortPm15MinIntervalMoniTime_Type=HCPerfTimeElapsed
_G9981PortPm15MinIntervalMoniTime_Object=MibTableColumn
g9981PortPm15MinIntervalMoniTime=_G9981PortPm15MinIntervalMoniTime_Object((1,3,6,1,2,1,208,1,1,3,2,1,2),_G9981PortPm15MinIntervalMoniTime_Type())
g9981PortPm15MinIntervalMoniTime.setMaxAccess(_C)
if mibBuilder.loadTexts:g9981PortPm15MinIntervalMoniTime.setStatus(_A)
if mibBuilder.loadTexts:g9981PortPm15MinIntervalMoniTime.setUnits(_I)
_G9981PortPm15MinIntervalRxLostCells_Type=HCPerfIntervalCount
_G9981PortPm15MinIntervalRxLostCells_Object=MibTableColumn
g9981PortPm15MinIntervalRxLostCells=_G9981PortPm15MinIntervalRxLostCells_Object((1,3,6,1,2,1,208,1,1,3,2,1,3),_G9981PortPm15MinIntervalRxLostCells_Type())
g9981PortPm15MinIntervalRxLostCells.setMaxAccess(_C)
if mibBuilder.loadTexts:g9981PortPm15MinIntervalRxLostCells.setStatus(_A)
if mibBuilder.loadTexts:g9981PortPm15MinIntervalRxLostCells.setUnits(_D)
_G9981PortPm15MinIntervalTxLostCells_Type=HCPerfIntervalCount
_G9981PortPm15MinIntervalTxLostCells_Object=MibTableColumn
g9981PortPm15MinIntervalTxLostCells=_G9981PortPm15MinIntervalTxLostCells_Object((1,3,6,1,2,1,208,1,1,3,2,1,4),_G9981PortPm15MinIntervalTxLostCells_Type())
g9981PortPm15MinIntervalTxLostCells.setMaxAccess(_C)
if mibBuilder.loadTexts:g9981PortPm15MinIntervalTxLostCells.setStatus(_A)
if mibBuilder.loadTexts:g9981PortPm15MinIntervalTxLostCells.setUnits(_D)
_G9981PortPm15MinIntervalUpDiffDelay_Type=HCPerfIntervalCount
_G9981PortPm15MinIntervalUpDiffDelay_Object=MibTableColumn
g9981PortPm15MinIntervalUpDiffDelay=_G9981PortPm15MinIntervalUpDiffDelay_Object((1,3,6,1,2,1,208,1,1,3,2,1,5),_G9981PortPm15MinIntervalUpDiffDelay_Type())
g9981PortPm15MinIntervalUpDiffDelay.setMaxAccess(_C)
if mibBuilder.loadTexts:g9981PortPm15MinIntervalUpDiffDelay.setStatus(_A)
if mibBuilder.loadTexts:g9981PortPm15MinIntervalUpDiffDelay.setUnits(_E)
_G9981PortPm15MinIntervalDnDiffDelay_Type=HCPerfIntervalCount
_G9981PortPm15MinIntervalDnDiffDelay_Object=MibTableColumn
g9981PortPm15MinIntervalDnDiffDelay=_G9981PortPm15MinIntervalDnDiffDelay_Object((1,3,6,1,2,1,208,1,1,3,2,1,6),_G9981PortPm15MinIntervalDnDiffDelay_Type())
g9981PortPm15MinIntervalDnDiffDelay.setMaxAccess(_C)
if mibBuilder.loadTexts:g9981PortPm15MinIntervalDnDiffDelay.setStatus(_A)
if mibBuilder.loadTexts:g9981PortPm15MinIntervalDnDiffDelay.setUnits(_E)
_G9981PortPm15MinIntervalValid_Type=TruthValue
_G9981PortPm15MinIntervalValid_Object=MibTableColumn
g9981PortPm15MinIntervalValid=_G9981PortPm15MinIntervalValid_Object((1,3,6,1,2,1,208,1,1,3,2,1,7),_G9981PortPm15MinIntervalValid_Type())
g9981PortPm15MinIntervalValid.setMaxAccess(_C)
if mibBuilder.loadTexts:g9981PortPm15MinIntervalValid.setStatus(_A)
_G9981PortPm1DayTable_Object=MibTable
g9981PortPm1DayTable=_G9981PortPm1DayTable_Object((1,3,6,1,2,1,208,1,1,3,3))
if mibBuilder.loadTexts:g9981PortPm1DayTable.setStatus(_A)
_G9981PortPm1DayEntry_Object=MibTableRow
g9981PortPm1DayEntry=_G9981PortPm1DayEntry_Object((1,3,6,1,2,1,208,1,1,3,3,1))
g9981PortPm1DayEntry.setIndexNames((0,_F,_G),(0,_B,_S))
if mibBuilder.loadTexts:g9981PortPm1DayEntry.setStatus(_A)
class _G9981PortPm1DayIntervalIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,7))
_G9981PortPm1DayIntervalIndex_Type.__name__=_H
_G9981PortPm1DayIntervalIndex_Object=MibTableColumn
g9981PortPm1DayIntervalIndex=_G9981PortPm1DayIntervalIndex_Object((1,3,6,1,2,1,208,1,1,3,3,1,1),_G9981PortPm1DayIntervalIndex_Type())
g9981PortPm1DayIntervalIndex.setMaxAccess(_R)
if mibBuilder.loadTexts:g9981PortPm1DayIntervalIndex.setStatus(_A)
_G9981PortPm1DayIntervalMoniTime_Type=HCPerfTimeElapsed
_G9981PortPm1DayIntervalMoniTime_Object=MibTableColumn
g9981PortPm1DayIntervalMoniTime=_G9981PortPm1DayIntervalMoniTime_Object((1,3,6,1,2,1,208,1,1,3,3,1,2),_G9981PortPm1DayIntervalMoniTime_Type())
g9981PortPm1DayIntervalMoniTime.setMaxAccess(_C)
if mibBuilder.loadTexts:g9981PortPm1DayIntervalMoniTime.setStatus(_A)
if mibBuilder.loadTexts:g9981PortPm1DayIntervalMoniTime.setUnits(_I)
_G9981PortPm1DayIntervalRxLostCells_Type=HCPerfIntervalCount
_G9981PortPm1DayIntervalRxLostCells_Object=MibTableColumn
g9981PortPm1DayIntervalRxLostCells=_G9981PortPm1DayIntervalRxLostCells_Object((1,3,6,1,2,1,208,1,1,3,3,1,3),_G9981PortPm1DayIntervalRxLostCells_Type())
g9981PortPm1DayIntervalRxLostCells.setMaxAccess(_C)
if mibBuilder.loadTexts:g9981PortPm1DayIntervalRxLostCells.setStatus(_A)
if mibBuilder.loadTexts:g9981PortPm1DayIntervalRxLostCells.setUnits(_D)
_G9981PortPm1DayIntervalTxLostCells_Type=HCPerfIntervalCount
_G9981PortPm1DayIntervalTxLostCells_Object=MibTableColumn
g9981PortPm1DayIntervalTxLostCells=_G9981PortPm1DayIntervalTxLostCells_Object((1,3,6,1,2,1,208,1,1,3,3,1,4),_G9981PortPm1DayIntervalTxLostCells_Type())
g9981PortPm1DayIntervalTxLostCells.setMaxAccess(_C)
if mibBuilder.loadTexts:g9981PortPm1DayIntervalTxLostCells.setStatus(_A)
if mibBuilder.loadTexts:g9981PortPm1DayIntervalTxLostCells.setUnits(_D)
_G9981PortPm1DayIntervalUpDiffDelay_Type=HCPerfIntervalCount
_G9981PortPm1DayIntervalUpDiffDelay_Object=MibTableColumn
g9981PortPm1DayIntervalUpDiffDelay=_G9981PortPm1DayIntervalUpDiffDelay_Object((1,3,6,1,2,1,208,1,1,3,3,1,5),_G9981PortPm1DayIntervalUpDiffDelay_Type())
g9981PortPm1DayIntervalUpDiffDelay.setMaxAccess(_C)
if mibBuilder.loadTexts:g9981PortPm1DayIntervalUpDiffDelay.setStatus(_A)
if mibBuilder.loadTexts:g9981PortPm1DayIntervalUpDiffDelay.setUnits(_E)
_G9981PortPm1DayIntervalDnDiffDelay_Type=HCPerfIntervalCount
_G9981PortPm1DayIntervalDnDiffDelay_Object=MibTableColumn
g9981PortPm1DayIntervalDnDiffDelay=_G9981PortPm1DayIntervalDnDiffDelay_Object((1,3,6,1,2,1,208,1,1,3,3,1,6),_G9981PortPm1DayIntervalDnDiffDelay_Type())
g9981PortPm1DayIntervalDnDiffDelay.setMaxAccess(_C)
if mibBuilder.loadTexts:g9981PortPm1DayIntervalDnDiffDelay.setStatus(_A)
if mibBuilder.loadTexts:g9981PortPm1DayIntervalDnDiffDelay.setUnits(_E)
_G9981PortPm1DayIntervalValid_Type=TruthValue
_G9981PortPm1DayIntervalValid_Object=MibTableColumn
g9981PortPm1DayIntervalValid=_G9981PortPm1DayIntervalValid_Object((1,3,6,1,2,1,208,1,1,3,3,1,7),_G9981PortPm1DayIntervalValid_Type())
g9981PortPm1DayIntervalValid.setMaxAccess(_C)
if mibBuilder.loadTexts:g9981PortPm1DayIntervalValid.setStatus(_A)
_G9981Conformance_ObjectIdentity=ObjectIdentity
g9981Conformance=_G9981Conformance_ObjectIdentity((1,3,6,1,2,1,208,2))
_G9981Groups_ObjectIdentity=ObjectIdentity
g9981Groups=_G9981Groups_ObjectIdentity((1,3,6,1,2,1,208,2,1))
_G9981Compliances_ObjectIdentity=ObjectIdentity
g9981Compliances=_G9981Compliances_ObjectIdentity((1,3,6,1,2,1,208,2,2))
g9981BasicGroup=ObjectGroup((1,3,6,1,2,1,208,2,1,1))
g9981BasicGroup.setObjects(*((_B,_T),(_B,_U),(_B,_L),(_B,_M)))
if mibBuilder.loadTexts:g9981BasicGroup.setStatus(_A)
g9981AlarmConfGroup=ObjectGroup((1,3,6,1,2,1,208,2,1,2))
g9981AlarmConfGroup.setObjects(*((_B,_N),(_B,_O),(_B,_V)))
if mibBuilder.loadTexts:g9981AlarmConfGroup.setStatus(_A)
g9981PerfCurrGroup=ObjectGroup((1,3,6,1,2,1,208,2,1,4))
g9981PerfCurrGroup.setObjects(*((_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j)))
if mibBuilder.loadTexts:g9981PerfCurrGroup.setStatus(_A)
g9981Perf15MinGroup=ObjectGroup((1,3,6,1,2,1,208,2,1,5))
g9981Perf15MinGroup.setObjects(*((_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p)))
if mibBuilder.loadTexts:g9981Perf15MinGroup.setStatus(_A)
g9981Perf1DayGroup=ObjectGroup((1,3,6,1,2,1,208,2,1,6))
g9981Perf1DayGroup.setObjects(*((_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v)))
if mibBuilder.loadTexts:g9981Perf1DayGroup.setStatus(_A)
g9981UpDiffDelayToleranceExceeded=NotificationType((1,3,6,1,2,1,208,1,1,0,1))
g9981UpDiffDelayToleranceExceeded.setObjects(*((_B,_N),(_B,_L)))
if mibBuilder.loadTexts:g9981UpDiffDelayToleranceExceeded.setStatus(_A)
g9981DnDiffDelayToleranceExceeded=NotificationType((1,3,6,1,2,1,208,1,1,0,2))
g9981DnDiffDelayToleranceExceeded.setObjects(*((_B,_O),(_B,_M)))
if mibBuilder.loadTexts:g9981DnDiffDelayToleranceExceeded.setStatus(_A)
g9981NotificationGroup=NotificationGroup((1,3,6,1,2,1,208,2,1,3))
g9981NotificationGroup.setObjects(*((_B,_w),(_B,_x)))
if mibBuilder.loadTexts:g9981NotificationGroup.setStatus(_A)
g9981Compliance=ModuleCompliance((1,3,6,1,2,1,208,2,2,1))
g9981Compliance.setObjects(*((_B,_y),(_B,_z),(_B,_A0),(_B,_A1),(_B,_A2),(_B,_A3)))
if mibBuilder.loadTexts:g9981Compliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{_J:MilliSeconds,'g9981MIB':g9981MIB,'g9981Objects':g9981Objects,'g9981Port':g9981Port,'g9981PortNotifications':g9981PortNotifications,_w:g9981UpDiffDelayToleranceExceeded,_x:g9981DnDiffDelayToleranceExceeded,'g9981PortConfTable':g9981PortConfTable,'g9981PortConfEntry':g9981PortConfEntry,_N:g9981PortConfUpDiffDelayTolerance,_O:g9981PortConfDnDiffDelayTolerance,_V:g9981PortConfDiffDelayToleranceExceededEnable,'g9981PortStatTable':g9981PortStatTable,'g9981PortStatEntry':g9981PortStatEntry,_T:g9981PortStatRxLostCells,_U:g9981PortStatTxLostCells,_L:g9981PortStatMaxUpDiffDelay,_M:g9981PortStatMaxDnDiffDelay,'g9981PM':g9981PM,'g9981PortPmCurTable':g9981PortPmCurTable,'g9981PortPmCurEntry':g9981PortPmCurEntry,_W:g9981PortPmCur15MinValidIntervals,_X:g9981PortPmCur15MinInvalidIntervals,_Y:g9981PortPmCur15MinTimeElapsed,_Z:g9981PortPmCur15MinRxLostCells,_a:g9981PortPmCur15MinTxLostCells,_b:g9981PortPmCur15MinUpDiffDelay,_c:g9981PortPmCur15MinDnDiffDelay,_d:g9981PortPmCur1DayValidIntervals,_e:g9981PortPmCur1DayInvalidIntervals,_f:g9981PortPmCur1DayTimeElapsed,_g:g9981PortPmCur1DayRxLostCells,_h:g9981PortPmCur1DayTxLostCells,_i:g9981PortPmCur1DayUpDiffDelay,_j:g9981PortPmCur1DayDnDiffDelay,'g9981PortPm15MinTable':g9981PortPm15MinTable,'g9981PortPm15MinEntry':g9981PortPm15MinEntry,_Q:g9981PortPm15MinIntervalIndex,_k:g9981PortPm15MinIntervalMoniTime,_l:g9981PortPm15MinIntervalRxLostCells,_m:g9981PortPm15MinIntervalTxLostCells,_n:g9981PortPm15MinIntervalUpDiffDelay,_o:g9981PortPm15MinIntervalDnDiffDelay,_p:g9981PortPm15MinIntervalValid,'g9981PortPm1DayTable':g9981PortPm1DayTable,'g9981PortPm1DayEntry':g9981PortPm1DayEntry,_S:g9981PortPm1DayIntervalIndex,_q:g9981PortPm1DayIntervalMoniTime,_r:g9981PortPm1DayIntervalRxLostCells,_s:g9981PortPm1DayIntervalTxLostCells,_t:g9981PortPm1DayIntervalUpDiffDelay,_u:g9981PortPm1DayIntervalDnDiffDelay,_v:g9981PortPm1DayIntervalValid,'g9981Conformance':g9981Conformance,'g9981Groups':g9981Groups,_y:g9981BasicGroup,_z:g9981AlarmConfGroup,_A0:g9981NotificationGroup,_A1:g9981PerfCurrGroup,_A2:g9981Perf15MinGroup,_A3:g9981Perf1DayGroup,'g9981Compliances':g9981Compliances,'g9981Compliance':g9981Compliance})