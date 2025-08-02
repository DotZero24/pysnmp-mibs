_AT='g9982Perf1DayGroup'
_AS='g9982Perf15MinGroup'
_AR='g9982PerfCurrGroup'
_AQ='g9982BacpGroup'
_AP='g9982BceGroup'
_AO='g9982BasicGroup'
_AN='g9982PortPm1DayIntervalValid'
_AM='g9982PortPm1DayIntervalRxOverflows'
_AL='g9982PortPm1DayIntervalRxLostEnds'
_AK='g9982PortPm1DayIntervalRxLostStarts'
_AJ='g9982PortPm1DayIntervalRxLostFragments'
_AI='g9982PortPm1DayIntervalRxBadFragments'
_AH='g9982PortPm1DayIntervalRxLargeFragments'
_AG='g9982PortPm1DayIntervalRxSmallFragments'
_AF='g9982PortPm1DayIntervalRxErrors'
_AE='g9982PortPm1DayIntervalMoniTime'
_AD='g9982PortPm15MinIntervalValid'
_AC='g9982PortPm15MinIntervalRxOverflows'
_AB='g9982PortPm15MinIntervalRxLostEnds'
_AA='g9982PortPm15MinIntervalRxLostStarts'
_A9='g9982PortPm15MinIntervalRxLostFragments'
_A8='g9982PortPm15MinIntervalRxBadFragments'
_A7='g9982PortPm15MinIntervalRxLargeFragments'
_A6='g9982PortPm15MinIntervalRxSmallFragments'
_A5='g9982PortPm15MinIntervalRxErrors'
_A4='g9982PortPm15MinIntervalMoniTime'
_A3='g9982PortPmCur1DayRxOverflows'
_A2='g9982PortPmCur1DayRxLostEnds'
_A1='g9982PortPmCur1DayRxLostStarts'
_A0='g9982PortPmCur1DayRxLostFragments'
_z='g9982PortPmCur1DayRxBadFragments'
_y='g9982PortPmCur1DayRxLargeFragments'
_x='g9982PortPmCur1DayRxSmallFragments'
_w='g9982PortPmCur1DayRxErrors'
_v='g9982PortPmCur1DayTimeElapsed'
_u='g9982PortPm1DayInvalidIntervals'
_t='g9982PortPm1DayValidIntervals'
_s='g9982PortPmCur15MinRxOverflows'
_r='g9982PortPmCur15MinRxLostEnds'
_q='g9982PortPmCur15MinRxLostStarts'
_p='g9982PortPmCur15MinRxLostFragments'
_o='g9982PortPmCur15MinRxBadFragments'
_n='g9982PortPmCur15MinRxLargeFragments'
_m='g9982PortPmCur15MinRxSmallFragments'
_l='g9982PortPmCur15MinRxErrors'
_k='g9982PortPmCur15MinTimeElapsed'
_j='g9982PortPm15MinInvalidIntervals'
_i='g9982PortPm15MinValidIntervals'
_h='g9982BceConfPeerEligibleGroupID'
_g='g9982BceConfEligibleGroupID'
_f='g9982PortStatOperCp'
_e='g9982PortConfAdminCp'
_d='g9982PortStatRxOverflows'
_c='g9982PortStatRxLostEnds'
_b='g9982PortStatRxLostStarts'
_a='g9982PortStatRxLostFragments'
_Z='g9982PortStatRxBadFragments'
_Y='g9982PortStatRxLargeFragments'
_X='g9982PortStatRxSmallFragments'
_W='g9982PortStatRxErrors'
_V='g9982PortStatTcOperType'
_U='g9982PortConfTcAdminType'
_T='g9982PortCapBacpSupported'
_S='g9982PortCapTcTypesSupported'
_R='g9982PortPm1DayIntervalIndex'
_Q='not-accessible'
_P='g9982PortPm15MinIntervalIndex'
_O='G9982CpType'
_N='tcHDLC'
_M='tc6465'
_L='g9982BceStatTcInCrcErrors'
_K='g9982BceStatTcInCodingErrors'
_J='read-write'
_I='PhysAddress'
_H='seconds'
_G='Unsigned32'
_F='ifIndex'
_E='IF-MIB'
_D='fragments'
_C='read-only'
_B='G9982-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
HCPerfCurrentCount,HCPerfInvalidIntervals,HCPerfTimeElapsed,HCPerfValidIntervals=mibBuilder.importSymbols('HC-PerfHist-TC-MIB','HCPerfCurrentCount','HCPerfInvalidIntervals','HCPerfTimeElapsed','HCPerfValidIntervals')
ifIndex,=mibBuilder.importSymbols(_E,_F)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso,mib_2=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_G,'iso','mib-2')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString',_I,'TextualConvention','TruthValue')
g9982MIB=ModuleIdentity((1,3,6,1,2,1,264))
if mibBuilder.loadTexts:g9982MIB.setRevisions(('2013-02-20 00:00',))
class G9982PtmTcType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_M,1),(_N,2)))
class G9982CpType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('unknown',0),('cpHS',1),('cpBACP',2)))
_G9982Objects_ObjectIdentity=ObjectIdentity
g9982Objects=_G9982Objects_ObjectIdentity((1,3,6,1,2,1,264,1))
_G9982Port_ObjectIdentity=ObjectIdentity
g9982Port=_G9982Port_ObjectIdentity((1,3,6,1,2,1,264,1,1))
_G9982PortConfTable_Object=MibTable
g9982PortConfTable=_G9982PortConfTable_Object((1,3,6,1,2,1,264,1,1,1))
if mibBuilder.loadTexts:g9982PortConfTable.setStatus(_A)
_G9982PortConfEntry_Object=MibTableRow
g9982PortConfEntry=_G9982PortConfEntry_Object((1,3,6,1,2,1,264,1,1,1,1))
g9982PortConfEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:g9982PortConfEntry.setStatus(_A)
_G9982PortConfTcAdminType_Type=G9982PtmTcType
_G9982PortConfTcAdminType_Object=MibTableColumn
g9982PortConfTcAdminType=_G9982PortConfTcAdminType_Object((1,3,6,1,2,1,264,1,1,1,1,1),_G9982PortConfTcAdminType_Type())
g9982PortConfTcAdminType.setMaxAccess(_J)
if mibBuilder.loadTexts:g9982PortConfTcAdminType.setStatus(_A)
class _G9982PortConfAdminCp_Type(G9982CpType):defaultValue=1
_G9982PortConfAdminCp_Type.__name__=_O
_G9982PortConfAdminCp_Object=MibTableColumn
g9982PortConfAdminCp=_G9982PortConfAdminCp_Object((1,3,6,1,2,1,264,1,1,1,1,2),_G9982PortConfAdminCp_Type())
g9982PortConfAdminCp.setMaxAccess(_J)
if mibBuilder.loadTexts:g9982PortConfAdminCp.setStatus(_A)
_G9982PortCapTable_Object=MibTable
g9982PortCapTable=_G9982PortCapTable_Object((1,3,6,1,2,1,264,1,1,2))
if mibBuilder.loadTexts:g9982PortCapTable.setStatus(_A)
_G9982PortCapEntry_Object=MibTableRow
g9982PortCapEntry=_G9982PortCapEntry_Object((1,3,6,1,2,1,264,1,1,2,1))
g9982PortCapEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:g9982PortCapEntry.setStatus(_A)
class _G9982PortCapTcTypesSupported_Type(Bits):namedValues=NamedValues(*((_M,0),(_N,1)))
_G9982PortCapTcTypesSupported_Type.__name__='Bits'
_G9982PortCapTcTypesSupported_Object=MibTableColumn
g9982PortCapTcTypesSupported=_G9982PortCapTcTypesSupported_Object((1,3,6,1,2,1,264,1,1,2,1,1),_G9982PortCapTcTypesSupported_Type())
g9982PortCapTcTypesSupported.setMaxAccess(_C)
if mibBuilder.loadTexts:g9982PortCapTcTypesSupported.setStatus(_A)
_G9982PortCapBacpSupported_Type=TruthValue
_G9982PortCapBacpSupported_Object=MibTableColumn
g9982PortCapBacpSupported=_G9982PortCapBacpSupported_Object((1,3,6,1,2,1,264,1,1,2,1,2),_G9982PortCapBacpSupported_Type())
g9982PortCapBacpSupported.setMaxAccess(_C)
if mibBuilder.loadTexts:g9982PortCapBacpSupported.setStatus(_A)
_G9982PortStatTable_Object=MibTable
g9982PortStatTable=_G9982PortStatTable_Object((1,3,6,1,2,1,264,1,1,3))
if mibBuilder.loadTexts:g9982PortStatTable.setStatus(_A)
_G9982PortStatEntry_Object=MibTableRow
g9982PortStatEntry=_G9982PortStatEntry_Object((1,3,6,1,2,1,264,1,1,3,1))
g9982PortStatEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:g9982PortStatEntry.setStatus(_A)
_G9982PortStatTcOperType_Type=G9982PtmTcType
_G9982PortStatTcOperType_Object=MibTableColumn
g9982PortStatTcOperType=_G9982PortStatTcOperType_Object((1,3,6,1,2,1,264,1,1,3,1,1),_G9982PortStatTcOperType_Type())
g9982PortStatTcOperType.setMaxAccess(_C)
if mibBuilder.loadTexts:g9982PortStatTcOperType.setStatus(_A)
_G9982PortStatOperCp_Type=G9982CpType
_G9982PortStatOperCp_Object=MibTableColumn
g9982PortStatOperCp=_G9982PortStatOperCp_Object((1,3,6,1,2,1,264,1,1,3,1,2),_G9982PortStatOperCp_Type())
g9982PortStatOperCp.setMaxAccess(_C)
if mibBuilder.loadTexts:g9982PortStatOperCp.setStatus(_A)
_G9982PortStatRxErrors_Type=Counter32
_G9982PortStatRxErrors_Object=MibTableColumn
g9982PortStatRxErrors=_G9982PortStatRxErrors_Object((1,3,6,1,2,1,264,1,1,3,1,3),_G9982PortStatRxErrors_Type())
g9982PortStatRxErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:g9982PortStatRxErrors.setStatus(_A)
if mibBuilder.loadTexts:g9982PortStatRxErrors.setUnits(_D)
_G9982PortStatRxSmallFragments_Type=Counter32
_G9982PortStatRxSmallFragments_Object=MibTableColumn
g9982PortStatRxSmallFragments=_G9982PortStatRxSmallFragments_Object((1,3,6,1,2,1,264,1,1,3,1,4),_G9982PortStatRxSmallFragments_Type())
g9982PortStatRxSmallFragments.setMaxAccess(_C)
if mibBuilder.loadTexts:g9982PortStatRxSmallFragments.setStatus(_A)
if mibBuilder.loadTexts:g9982PortStatRxSmallFragments.setUnits(_D)
_G9982PortStatRxLargeFragments_Type=Counter32
_G9982PortStatRxLargeFragments_Object=MibTableColumn
g9982PortStatRxLargeFragments=_G9982PortStatRxLargeFragments_Object((1,3,6,1,2,1,264,1,1,3,1,5),_G9982PortStatRxLargeFragments_Type())
g9982PortStatRxLargeFragments.setMaxAccess(_C)
if mibBuilder.loadTexts:g9982PortStatRxLargeFragments.setStatus(_A)
if mibBuilder.loadTexts:g9982PortStatRxLargeFragments.setUnits(_D)
_G9982PortStatRxBadFragments_Type=Counter32
_G9982PortStatRxBadFragments_Object=MibTableColumn
g9982PortStatRxBadFragments=_G9982PortStatRxBadFragments_Object((1,3,6,1,2,1,264,1,1,3,1,6),_G9982PortStatRxBadFragments_Type())
g9982PortStatRxBadFragments.setMaxAccess(_C)
if mibBuilder.loadTexts:g9982PortStatRxBadFragments.setStatus(_A)
if mibBuilder.loadTexts:g9982PortStatRxBadFragments.setUnits(_D)
_G9982PortStatRxLostFragments_Type=Counter32
_G9982PortStatRxLostFragments_Object=MibTableColumn
g9982PortStatRxLostFragments=_G9982PortStatRxLostFragments_Object((1,3,6,1,2,1,264,1,1,3,1,7),_G9982PortStatRxLostFragments_Type())
g9982PortStatRxLostFragments.setMaxAccess(_C)
if mibBuilder.loadTexts:g9982PortStatRxLostFragments.setStatus(_A)
if mibBuilder.loadTexts:g9982PortStatRxLostFragments.setUnits(_D)
_G9982PortStatRxLostStarts_Type=Counter32
_G9982PortStatRxLostStarts_Object=MibTableColumn
g9982PortStatRxLostStarts=_G9982PortStatRxLostStarts_Object((1,3,6,1,2,1,264,1,1,3,1,8),_G9982PortStatRxLostStarts_Type())
g9982PortStatRxLostStarts.setMaxAccess(_C)
if mibBuilder.loadTexts:g9982PortStatRxLostStarts.setStatus(_A)
_G9982PortStatRxLostEnds_Type=Counter32
_G9982PortStatRxLostEnds_Object=MibTableColumn
g9982PortStatRxLostEnds=_G9982PortStatRxLostEnds_Object((1,3,6,1,2,1,264,1,1,3,1,9),_G9982PortStatRxLostEnds_Type())
g9982PortStatRxLostEnds.setMaxAccess(_C)
if mibBuilder.loadTexts:g9982PortStatRxLostEnds.setStatus(_A)
_G9982PortStatRxOverflows_Type=Counter32
_G9982PortStatRxOverflows_Object=MibTableColumn
g9982PortStatRxOverflows=_G9982PortStatRxOverflows_Object((1,3,6,1,2,1,264,1,1,3,1,10),_G9982PortStatRxOverflows_Type())
g9982PortStatRxOverflows.setMaxAccess(_C)
if mibBuilder.loadTexts:g9982PortStatRxOverflows.setStatus(_A)
if mibBuilder.loadTexts:g9982PortStatRxOverflows.setUnits(_D)
_G9982PM_ObjectIdentity=ObjectIdentity
g9982PM=_G9982PM_ObjectIdentity((1,3,6,1,2,1,264,1,1,4))
_G9982PortPmCurTable_Object=MibTable
g9982PortPmCurTable=_G9982PortPmCurTable_Object((1,3,6,1,2,1,264,1,1,4,1))
if mibBuilder.loadTexts:g9982PortPmCurTable.setStatus(_A)
_G9982PortPmCurEntry_Object=MibTableRow
g9982PortPmCurEntry=_G9982PortPmCurEntry_Object((1,3,6,1,2,1,264,1,1,4,1,1))
g9982PortPmCurEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:g9982PortPmCurEntry.setStatus(_A)
_G9982PortPm15MinValidIntervals_Type=HCPerfValidIntervals
_G9982PortPm15MinValidIntervals_Object=MibTableColumn
g9982PortPm15MinValidIntervals=_G9982PortPm15MinValidIntervals_Object((1,3,6,1,2,1,264,1,1,4,1,1,1),_G9982PortPm15MinValidIntervals_Type())
g9982PortPm15MinValidIntervals.setMaxAccess(_C)
if mibBuilder.loadTexts:g9982PortPm15MinValidIntervals.setStatus(_A)
_G9982PortPm15MinInvalidIntervals_Type=HCPerfInvalidIntervals
_G9982PortPm15MinInvalidIntervals_Object=MibTableColumn
g9982PortPm15MinInvalidIntervals=_G9982PortPm15MinInvalidIntervals_Object((1,3,6,1,2,1,264,1,1,4,1,1,2),_G9982PortPm15MinInvalidIntervals_Type())
g9982PortPm15MinInvalidIntervals.setMaxAccess(_C)
if mibBuilder.loadTexts:g9982PortPm15MinInvalidIntervals.setStatus(_A)
_G9982PortPmCur15MinTimeElapsed_Type=HCPerfTimeElapsed
_G9982PortPmCur15MinTimeElapsed_Object=MibTableColumn
g9982PortPmCur15MinTimeElapsed=_G9982PortPmCur15MinTimeElapsed_Object((1,3,6,1,2,1,264,1,1,4,1,1,3),_G9982PortPmCur15MinTimeElapsed_Type())
g9982PortPmCur15MinTimeElapsed.setMaxAccess(_C)
if mibBuilder.loadTexts:g9982PortPmCur15MinTimeElapsed.setStatus(_A)
if mibBuilder.loadTexts:g9982PortPmCur15MinTimeElapsed.setUnits(_H)
_G9982PortPmCur15MinRxErrors_Type=HCPerfCurrentCount
_G9982PortPmCur15MinRxErrors_Object=MibTableColumn
g9982PortPmCur15MinRxErrors=_G9982PortPmCur15MinRxErrors_Object((1,3,6,1,2,1,264,1,1,4,1,1,4),_G9982PortPmCur15MinRxErrors_Type())
g9982PortPmCur15MinRxErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:g9982PortPmCur15MinRxErrors.setStatus(_A)
if mibBuilder.loadTexts:g9982PortPmCur15MinRxErrors.setUnits(_D)
_G9982PortPmCur15MinRxSmallFragments_Type=HCPerfCurrentCount
_G9982PortPmCur15MinRxSmallFragments_Object=MibTableColumn
g9982PortPmCur15MinRxSmallFragments=_G9982PortPmCur15MinRxSmallFragments_Object((1,3,6,1,2,1,264,1,1,4,1,1,5),_G9982PortPmCur15MinRxSmallFragments_Type())
g9982PortPmCur15MinRxSmallFragments.setMaxAccess(_C)
if mibBuilder.loadTexts:g9982PortPmCur15MinRxSmallFragments.setStatus(_A)
if mibBuilder.loadTexts:g9982PortPmCur15MinRxSmallFragments.setUnits(_D)
_G9982PortPmCur15MinRxLargeFragments_Type=HCPerfCurrentCount
_G9982PortPmCur15MinRxLargeFragments_Object=MibTableColumn
g9982PortPmCur15MinRxLargeFragments=_G9982PortPmCur15MinRxLargeFragments_Object((1,3,6,1,2,1,264,1,1,4,1,1,6),_G9982PortPmCur15MinRxLargeFragments_Type())
g9982PortPmCur15MinRxLargeFragments.setMaxAccess(_C)
if mibBuilder.loadTexts:g9982PortPmCur15MinRxLargeFragments.setStatus(_A)
if mibBuilder.loadTexts:g9982PortPmCur15MinRxLargeFragments.setUnits(_D)
_G9982PortPmCur15MinRxBadFragments_Type=HCPerfCurrentCount
_G9982PortPmCur15MinRxBadFragments_Object=MibTableColumn
g9982PortPmCur15MinRxBadFragments=_G9982PortPmCur15MinRxBadFragments_Object((1,3,6,1,2,1,264,1,1,4,1,1,7),_G9982PortPmCur15MinRxBadFragments_Type())
g9982PortPmCur15MinRxBadFragments.setMaxAccess(_C)
if mibBuilder.loadTexts:g9982PortPmCur15MinRxBadFragments.setStatus(_A)
if mibBuilder.loadTexts:g9982PortPmCur15MinRxBadFragments.setUnits(_D)
_G9982PortPmCur15MinRxLostFragments_Type=HCPerfCurrentCount
_G9982PortPmCur15MinRxLostFragments_Object=MibTableColumn
g9982PortPmCur15MinRxLostFragments=_G9982PortPmCur15MinRxLostFragments_Object((1,3,6,1,2,1,264,1,1,4,1,1,8),_G9982PortPmCur15MinRxLostFragments_Type())
g9982PortPmCur15MinRxLostFragments.setMaxAccess(_C)
if mibBuilder.loadTexts:g9982PortPmCur15MinRxLostFragments.setStatus(_A)
if mibBuilder.loadTexts:g9982PortPmCur15MinRxLostFragments.setUnits(_D)
_G9982PortPmCur15MinRxLostStarts_Type=HCPerfCurrentCount
_G9982PortPmCur15MinRxLostStarts_Object=MibTableColumn
g9982PortPmCur15MinRxLostStarts=_G9982PortPmCur15MinRxLostStarts_Object((1,3,6,1,2,1,264,1,1,4,1,1,9),_G9982PortPmCur15MinRxLostStarts_Type())
g9982PortPmCur15MinRxLostStarts.setMaxAccess(_C)
if mibBuilder.loadTexts:g9982PortPmCur15MinRxLostStarts.setStatus(_A)
_G9982PortPmCur15MinRxLostEnds_Type=HCPerfCurrentCount
_G9982PortPmCur15MinRxLostEnds_Object=MibTableColumn
g9982PortPmCur15MinRxLostEnds=_G9982PortPmCur15MinRxLostEnds_Object((1,3,6,1,2,1,264,1,1,4,1,1,10),_G9982PortPmCur15MinRxLostEnds_Type())
g9982PortPmCur15MinRxLostEnds.setMaxAccess(_C)
if mibBuilder.loadTexts:g9982PortPmCur15MinRxLostEnds.setStatus(_A)
_G9982PortPmCur15MinRxOverflows_Type=HCPerfCurrentCount
_G9982PortPmCur15MinRxOverflows_Object=MibTableColumn
g9982PortPmCur15MinRxOverflows=_G9982PortPmCur15MinRxOverflows_Object((1,3,6,1,2,1,264,1,1,4,1,1,11),_G9982PortPmCur15MinRxOverflows_Type())
g9982PortPmCur15MinRxOverflows.setMaxAccess(_C)
if mibBuilder.loadTexts:g9982PortPmCur15MinRxOverflows.setStatus(_A)
if mibBuilder.loadTexts:g9982PortPmCur15MinRxOverflows.setUnits(_D)
class _G9982PortPm1DayValidIntervals_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_G9982PortPm1DayValidIntervals_Type.__name__=_G
_G9982PortPm1DayValidIntervals_Object=MibTableColumn
g9982PortPm1DayValidIntervals=_G9982PortPm1DayValidIntervals_Object((1,3,6,1,2,1,264,1,1,4,1,1,12),_G9982PortPm1DayValidIntervals_Type())
g9982PortPm1DayValidIntervals.setMaxAccess(_C)
if mibBuilder.loadTexts:g9982PortPm1DayValidIntervals.setStatus(_A)
if mibBuilder.loadTexts:g9982PortPm1DayValidIntervals.setUnits('days')
class _G9982PortPm1DayInvalidIntervals_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_G9982PortPm1DayInvalidIntervals_Type.__name__=_G
_G9982PortPm1DayInvalidIntervals_Object=MibTableColumn
g9982PortPm1DayInvalidIntervals=_G9982PortPm1DayInvalidIntervals_Object((1,3,6,1,2,1,264,1,1,4,1,1,13),_G9982PortPm1DayInvalidIntervals_Type())
g9982PortPm1DayInvalidIntervals.setMaxAccess(_C)
if mibBuilder.loadTexts:g9982PortPm1DayInvalidIntervals.setStatus(_A)
if mibBuilder.loadTexts:g9982PortPm1DayInvalidIntervals.setUnits('days')
_G9982PortPmCur1DayTimeElapsed_Type=HCPerfTimeElapsed
_G9982PortPmCur1DayTimeElapsed_Object=MibTableColumn
g9982PortPmCur1DayTimeElapsed=_G9982PortPmCur1DayTimeElapsed_Object((1,3,6,1,2,1,264,1,1,4,1,1,14),_G9982PortPmCur1DayTimeElapsed_Type())
g9982PortPmCur1DayTimeElapsed.setMaxAccess(_C)
if mibBuilder.loadTexts:g9982PortPmCur1DayTimeElapsed.setStatus(_A)
if mibBuilder.loadTexts:g9982PortPmCur1DayTimeElapsed.setUnits(_H)
_G9982PortPmCur1DayRxErrors_Type=HCPerfCurrentCount
_G9982PortPmCur1DayRxErrors_Object=MibTableColumn
g9982PortPmCur1DayRxErrors=_G9982PortPmCur1DayRxErrors_Object((1,3,6,1,2,1,264,1,1,4,1,1,15),_G9982PortPmCur1DayRxErrors_Type())
g9982PortPmCur1DayRxErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:g9982PortPmCur1DayRxErrors.setStatus(_A)
if mibBuilder.loadTexts:g9982PortPmCur1DayRxErrors.setUnits(_D)
_G9982PortPmCur1DayRxSmallFragments_Type=HCPerfCurrentCount
_G9982PortPmCur1DayRxSmallFragments_Object=MibTableColumn
g9982PortPmCur1DayRxSmallFragments=_G9982PortPmCur1DayRxSmallFragments_Object((1,3,6,1,2,1,264,1,1,4,1,1,16),_G9982PortPmCur1DayRxSmallFragments_Type())
g9982PortPmCur1DayRxSmallFragments.setMaxAccess(_C)
if mibBuilder.loadTexts:g9982PortPmCur1DayRxSmallFragments.setStatus(_A)
if mibBuilder.loadTexts:g9982PortPmCur1DayRxSmallFragments.setUnits(_D)
_G9982PortPmCur1DayRxLargeFragments_Type=HCPerfCurrentCount
_G9982PortPmCur1DayRxLargeFragments_Object=MibTableColumn
g9982PortPmCur1DayRxLargeFragments=_G9982PortPmCur1DayRxLargeFragments_Object((1,3,6,1,2,1,264,1,1,4,1,1,17),_G9982PortPmCur1DayRxLargeFragments_Type())
g9982PortPmCur1DayRxLargeFragments.setMaxAccess(_C)
if mibBuilder.loadTexts:g9982PortPmCur1DayRxLargeFragments.setStatus(_A)
if mibBuilder.loadTexts:g9982PortPmCur1DayRxLargeFragments.setUnits(_D)
_G9982PortPmCur1DayRxBadFragments_Type=HCPerfCurrentCount
_G9982PortPmCur1DayRxBadFragments_Object=MibTableColumn
g9982PortPmCur1DayRxBadFragments=_G9982PortPmCur1DayRxBadFragments_Object((1,3,6,1,2,1,264,1,1,4,1,1,18),_G9982PortPmCur1DayRxBadFragments_Type())
g9982PortPmCur1DayRxBadFragments.setMaxAccess(_C)
if mibBuilder.loadTexts:g9982PortPmCur1DayRxBadFragments.setStatus(_A)
if mibBuilder.loadTexts:g9982PortPmCur1DayRxBadFragments.setUnits(_D)
_G9982PortPmCur1DayRxLostFragments_Type=HCPerfCurrentCount
_G9982PortPmCur1DayRxLostFragments_Object=MibTableColumn
g9982PortPmCur1DayRxLostFragments=_G9982PortPmCur1DayRxLostFragments_Object((1,3,6,1,2,1,264,1,1,4,1,1,19),_G9982PortPmCur1DayRxLostFragments_Type())
g9982PortPmCur1DayRxLostFragments.setMaxAccess(_C)
if mibBuilder.loadTexts:g9982PortPmCur1DayRxLostFragments.setStatus(_A)
if mibBuilder.loadTexts:g9982PortPmCur1DayRxLostFragments.setUnits(_D)
_G9982PortPmCur1DayRxLostStarts_Type=HCPerfCurrentCount
_G9982PortPmCur1DayRxLostStarts_Object=MibTableColumn
g9982PortPmCur1DayRxLostStarts=_G9982PortPmCur1DayRxLostStarts_Object((1,3,6,1,2,1,264,1,1,4,1,1,20),_G9982PortPmCur1DayRxLostStarts_Type())
g9982PortPmCur1DayRxLostStarts.setMaxAccess(_C)
if mibBuilder.loadTexts:g9982PortPmCur1DayRxLostStarts.setStatus(_A)
_G9982PortPmCur1DayRxLostEnds_Type=HCPerfCurrentCount
_G9982PortPmCur1DayRxLostEnds_Object=MibTableColumn
g9982PortPmCur1DayRxLostEnds=_G9982PortPmCur1DayRxLostEnds_Object((1,3,6,1,2,1,264,1,1,4,1,1,21),_G9982PortPmCur1DayRxLostEnds_Type())
g9982PortPmCur1DayRxLostEnds.setMaxAccess(_C)
if mibBuilder.loadTexts:g9982PortPmCur1DayRxLostEnds.setStatus(_A)
_G9982PortPmCur1DayRxOverflows_Type=HCPerfCurrentCount
_G9982PortPmCur1DayRxOverflows_Object=MibTableColumn
g9982PortPmCur1DayRxOverflows=_G9982PortPmCur1DayRxOverflows_Object((1,3,6,1,2,1,264,1,1,4,1,1,22),_G9982PortPmCur1DayRxOverflows_Type())
g9982PortPmCur1DayRxOverflows.setMaxAccess(_C)
if mibBuilder.loadTexts:g9982PortPmCur1DayRxOverflows.setStatus(_A)
if mibBuilder.loadTexts:g9982PortPmCur1DayRxOverflows.setUnits(_D)
_G9982PortPm15MinTable_Object=MibTable
g9982PortPm15MinTable=_G9982PortPm15MinTable_Object((1,3,6,1,2,1,264,1,1,4,2))
if mibBuilder.loadTexts:g9982PortPm15MinTable.setStatus(_A)
_G9982PortPm15MinEntry_Object=MibTableRow
g9982PortPm15MinEntry=_G9982PortPm15MinEntry_Object((1,3,6,1,2,1,264,1,1,4,2,1))
g9982PortPm15MinEntry.setIndexNames((0,_E,_F),(0,_B,_P))
if mibBuilder.loadTexts:g9982PortPm15MinEntry.setStatus(_A)
class _G9982PortPm15MinIntervalIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,96))
_G9982PortPm15MinIntervalIndex_Type.__name__=_G
_G9982PortPm15MinIntervalIndex_Object=MibTableColumn
g9982PortPm15MinIntervalIndex=_G9982PortPm15MinIntervalIndex_Object((1,3,6,1,2,1,264,1,1,4,2,1,1),_G9982PortPm15MinIntervalIndex_Type())
g9982PortPm15MinIntervalIndex.setMaxAccess(_Q)
if mibBuilder.loadTexts:g9982PortPm15MinIntervalIndex.setStatus(_A)
_G9982PortPm15MinIntervalMoniTime_Type=HCPerfTimeElapsed
_G9982PortPm15MinIntervalMoniTime_Object=MibTableColumn
g9982PortPm15MinIntervalMoniTime=_G9982PortPm15MinIntervalMoniTime_Object((1,3,6,1,2,1,264,1,1,4,2,1,2),_G9982PortPm15MinIntervalMoniTime_Type())
g9982PortPm15MinIntervalMoniTime.setMaxAccess(_C)
if mibBuilder.loadTexts:g9982PortPm15MinIntervalMoniTime.setStatus(_A)
if mibBuilder.loadTexts:g9982PortPm15MinIntervalMoniTime.setUnits(_H)
_G9982PortPm15MinIntervalRxErrors_Type=HCPerfCurrentCount
_G9982PortPm15MinIntervalRxErrors_Object=MibTableColumn
g9982PortPm15MinIntervalRxErrors=_G9982PortPm15MinIntervalRxErrors_Object((1,3,6,1,2,1,264,1,1,4,2,1,3),_G9982PortPm15MinIntervalRxErrors_Type())
g9982PortPm15MinIntervalRxErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:g9982PortPm15MinIntervalRxErrors.setStatus(_A)
if mibBuilder.loadTexts:g9982PortPm15MinIntervalRxErrors.setUnits(_D)
_G9982PortPm15MinIntervalRxSmallFragments_Type=HCPerfCurrentCount
_G9982PortPm15MinIntervalRxSmallFragments_Object=MibTableColumn
g9982PortPm15MinIntervalRxSmallFragments=_G9982PortPm15MinIntervalRxSmallFragments_Object((1,3,6,1,2,1,264,1,1,4,2,1,4),_G9982PortPm15MinIntervalRxSmallFragments_Type())
g9982PortPm15MinIntervalRxSmallFragments.setMaxAccess(_C)
if mibBuilder.loadTexts:g9982PortPm15MinIntervalRxSmallFragments.setStatus(_A)
if mibBuilder.loadTexts:g9982PortPm15MinIntervalRxSmallFragments.setUnits(_D)
_G9982PortPm15MinIntervalRxLargeFragments_Type=HCPerfCurrentCount
_G9982PortPm15MinIntervalRxLargeFragments_Object=MibTableColumn
g9982PortPm15MinIntervalRxLargeFragments=_G9982PortPm15MinIntervalRxLargeFragments_Object((1,3,6,1,2,1,264,1,1,4,2,1,5),_G9982PortPm15MinIntervalRxLargeFragments_Type())
g9982PortPm15MinIntervalRxLargeFragments.setMaxAccess(_C)
if mibBuilder.loadTexts:g9982PortPm15MinIntervalRxLargeFragments.setStatus(_A)
if mibBuilder.loadTexts:g9982PortPm15MinIntervalRxLargeFragments.setUnits(_D)
_G9982PortPm15MinIntervalRxBadFragments_Type=HCPerfCurrentCount
_G9982PortPm15MinIntervalRxBadFragments_Object=MibTableColumn
g9982PortPm15MinIntervalRxBadFragments=_G9982PortPm15MinIntervalRxBadFragments_Object((1,3,6,1,2,1,264,1,1,4,2,1,6),_G9982PortPm15MinIntervalRxBadFragments_Type())
g9982PortPm15MinIntervalRxBadFragments.setMaxAccess(_C)
if mibBuilder.loadTexts:g9982PortPm15MinIntervalRxBadFragments.setStatus(_A)
if mibBuilder.loadTexts:g9982PortPm15MinIntervalRxBadFragments.setUnits(_D)
_G9982PortPm15MinIntervalRxLostFragments_Type=HCPerfCurrentCount
_G9982PortPm15MinIntervalRxLostFragments_Object=MibTableColumn
g9982PortPm15MinIntervalRxLostFragments=_G9982PortPm15MinIntervalRxLostFragments_Object((1,3,6,1,2,1,264,1,1,4,2,1,7),_G9982PortPm15MinIntervalRxLostFragments_Type())
g9982PortPm15MinIntervalRxLostFragments.setMaxAccess(_C)
if mibBuilder.loadTexts:g9982PortPm15MinIntervalRxLostFragments.setStatus(_A)
if mibBuilder.loadTexts:g9982PortPm15MinIntervalRxLostFragments.setUnits(_D)
_G9982PortPm15MinIntervalRxLostStarts_Type=HCPerfCurrentCount
_G9982PortPm15MinIntervalRxLostStarts_Object=MibTableColumn
g9982PortPm15MinIntervalRxLostStarts=_G9982PortPm15MinIntervalRxLostStarts_Object((1,3,6,1,2,1,264,1,1,4,2,1,8),_G9982PortPm15MinIntervalRxLostStarts_Type())
g9982PortPm15MinIntervalRxLostStarts.setMaxAccess(_C)
if mibBuilder.loadTexts:g9982PortPm15MinIntervalRxLostStarts.setStatus(_A)
_G9982PortPm15MinIntervalRxLostEnds_Type=HCPerfCurrentCount
_G9982PortPm15MinIntervalRxLostEnds_Object=MibTableColumn
g9982PortPm15MinIntervalRxLostEnds=_G9982PortPm15MinIntervalRxLostEnds_Object((1,3,6,1,2,1,264,1,1,4,2,1,9),_G9982PortPm15MinIntervalRxLostEnds_Type())
g9982PortPm15MinIntervalRxLostEnds.setMaxAccess(_C)
if mibBuilder.loadTexts:g9982PortPm15MinIntervalRxLostEnds.setStatus(_A)
_G9982PortPm15MinIntervalRxOverflows_Type=HCPerfCurrentCount
_G9982PortPm15MinIntervalRxOverflows_Object=MibTableColumn
g9982PortPm15MinIntervalRxOverflows=_G9982PortPm15MinIntervalRxOverflows_Object((1,3,6,1,2,1,264,1,1,4,2,1,10),_G9982PortPm15MinIntervalRxOverflows_Type())
g9982PortPm15MinIntervalRxOverflows.setMaxAccess(_C)
if mibBuilder.loadTexts:g9982PortPm15MinIntervalRxOverflows.setStatus(_A)
if mibBuilder.loadTexts:g9982PortPm15MinIntervalRxOverflows.setUnits(_D)
_G9982PortPm15MinIntervalValid_Type=TruthValue
_G9982PortPm15MinIntervalValid_Object=MibTableColumn
g9982PortPm15MinIntervalValid=_G9982PortPm15MinIntervalValid_Object((1,3,6,1,2,1,264,1,1,4,2,1,11),_G9982PortPm15MinIntervalValid_Type())
g9982PortPm15MinIntervalValid.setMaxAccess(_C)
if mibBuilder.loadTexts:g9982PortPm15MinIntervalValid.setStatus(_A)
_G9982PortPm1DayTable_Object=MibTable
g9982PortPm1DayTable=_G9982PortPm1DayTable_Object((1,3,6,1,2,1,264,1,1,4,3))
if mibBuilder.loadTexts:g9982PortPm1DayTable.setStatus(_A)
_G9982PortPm1DayEntry_Object=MibTableRow
g9982PortPm1DayEntry=_G9982PortPm1DayEntry_Object((1,3,6,1,2,1,264,1,1,4,3,1))
g9982PortPm1DayEntry.setIndexNames((0,_E,_F),(0,_B,_R))
if mibBuilder.loadTexts:g9982PortPm1DayEntry.setStatus(_A)
class _G9982PortPm1DayIntervalIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,7))
_G9982PortPm1DayIntervalIndex_Type.__name__=_G
_G9982PortPm1DayIntervalIndex_Object=MibTableColumn
g9982PortPm1DayIntervalIndex=_G9982PortPm1DayIntervalIndex_Object((1,3,6,1,2,1,264,1,1,4,3,1,1),_G9982PortPm1DayIntervalIndex_Type())
g9982PortPm1DayIntervalIndex.setMaxAccess(_Q)
if mibBuilder.loadTexts:g9982PortPm1DayIntervalIndex.setStatus(_A)
_G9982PortPm1DayIntervalMoniTime_Type=HCPerfTimeElapsed
_G9982PortPm1DayIntervalMoniTime_Object=MibTableColumn
g9982PortPm1DayIntervalMoniTime=_G9982PortPm1DayIntervalMoniTime_Object((1,3,6,1,2,1,264,1,1,4,3,1,2),_G9982PortPm1DayIntervalMoniTime_Type())
g9982PortPm1DayIntervalMoniTime.setMaxAccess(_C)
if mibBuilder.loadTexts:g9982PortPm1DayIntervalMoniTime.setStatus(_A)
if mibBuilder.loadTexts:g9982PortPm1DayIntervalMoniTime.setUnits(_H)
_G9982PortPm1DayIntervalRxErrors_Type=HCPerfCurrentCount
_G9982PortPm1DayIntervalRxErrors_Object=MibTableColumn
g9982PortPm1DayIntervalRxErrors=_G9982PortPm1DayIntervalRxErrors_Object((1,3,6,1,2,1,264,1,1,4,3,1,3),_G9982PortPm1DayIntervalRxErrors_Type())
g9982PortPm1DayIntervalRxErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:g9982PortPm1DayIntervalRxErrors.setStatus(_A)
if mibBuilder.loadTexts:g9982PortPm1DayIntervalRxErrors.setUnits(_D)
_G9982PortPm1DayIntervalRxSmallFragments_Type=HCPerfCurrentCount
_G9982PortPm1DayIntervalRxSmallFragments_Object=MibTableColumn
g9982PortPm1DayIntervalRxSmallFragments=_G9982PortPm1DayIntervalRxSmallFragments_Object((1,3,6,1,2,1,264,1,1,4,3,1,4),_G9982PortPm1DayIntervalRxSmallFragments_Type())
g9982PortPm1DayIntervalRxSmallFragments.setMaxAccess(_C)
if mibBuilder.loadTexts:g9982PortPm1DayIntervalRxSmallFragments.setStatus(_A)
if mibBuilder.loadTexts:g9982PortPm1DayIntervalRxSmallFragments.setUnits(_D)
_G9982PortPm1DayIntervalRxLargeFragments_Type=HCPerfCurrentCount
_G9982PortPm1DayIntervalRxLargeFragments_Object=MibTableColumn
g9982PortPm1DayIntervalRxLargeFragments=_G9982PortPm1DayIntervalRxLargeFragments_Object((1,3,6,1,2,1,264,1,1,4,3,1,5),_G9982PortPm1DayIntervalRxLargeFragments_Type())
g9982PortPm1DayIntervalRxLargeFragments.setMaxAccess(_C)
if mibBuilder.loadTexts:g9982PortPm1DayIntervalRxLargeFragments.setStatus(_A)
if mibBuilder.loadTexts:g9982PortPm1DayIntervalRxLargeFragments.setUnits(_D)
_G9982PortPm1DayIntervalRxBadFragments_Type=HCPerfCurrentCount
_G9982PortPm1DayIntervalRxBadFragments_Object=MibTableColumn
g9982PortPm1DayIntervalRxBadFragments=_G9982PortPm1DayIntervalRxBadFragments_Object((1,3,6,1,2,1,264,1,1,4,3,1,6),_G9982PortPm1DayIntervalRxBadFragments_Type())
g9982PortPm1DayIntervalRxBadFragments.setMaxAccess(_C)
if mibBuilder.loadTexts:g9982PortPm1DayIntervalRxBadFragments.setStatus(_A)
if mibBuilder.loadTexts:g9982PortPm1DayIntervalRxBadFragments.setUnits(_D)
_G9982PortPm1DayIntervalRxLostFragments_Type=HCPerfCurrentCount
_G9982PortPm1DayIntervalRxLostFragments_Object=MibTableColumn
g9982PortPm1DayIntervalRxLostFragments=_G9982PortPm1DayIntervalRxLostFragments_Object((1,3,6,1,2,1,264,1,1,4,3,1,7),_G9982PortPm1DayIntervalRxLostFragments_Type())
g9982PortPm1DayIntervalRxLostFragments.setMaxAccess(_C)
if mibBuilder.loadTexts:g9982PortPm1DayIntervalRxLostFragments.setStatus(_A)
if mibBuilder.loadTexts:g9982PortPm1DayIntervalRxLostFragments.setUnits(_D)
_G9982PortPm1DayIntervalRxLostStarts_Type=HCPerfCurrentCount
_G9982PortPm1DayIntervalRxLostStarts_Object=MibTableColumn
g9982PortPm1DayIntervalRxLostStarts=_G9982PortPm1DayIntervalRxLostStarts_Object((1,3,6,1,2,1,264,1,1,4,3,1,8),_G9982PortPm1DayIntervalRxLostStarts_Type())
g9982PortPm1DayIntervalRxLostStarts.setMaxAccess(_C)
if mibBuilder.loadTexts:g9982PortPm1DayIntervalRxLostStarts.setStatus(_A)
_G9982PortPm1DayIntervalRxLostEnds_Type=HCPerfCurrentCount
_G9982PortPm1DayIntervalRxLostEnds_Object=MibTableColumn
g9982PortPm1DayIntervalRxLostEnds=_G9982PortPm1DayIntervalRxLostEnds_Object((1,3,6,1,2,1,264,1,1,4,3,1,9),_G9982PortPm1DayIntervalRxLostEnds_Type())
g9982PortPm1DayIntervalRxLostEnds.setMaxAccess(_C)
if mibBuilder.loadTexts:g9982PortPm1DayIntervalRxLostEnds.setStatus(_A)
_G9982PortPm1DayIntervalRxOverflows_Type=HCPerfCurrentCount
_G9982PortPm1DayIntervalRxOverflows_Object=MibTableColumn
g9982PortPm1DayIntervalRxOverflows=_G9982PortPm1DayIntervalRxOverflows_Object((1,3,6,1,2,1,264,1,1,4,3,1,10),_G9982PortPm1DayIntervalRxOverflows_Type())
g9982PortPm1DayIntervalRxOverflows.setMaxAccess(_C)
if mibBuilder.loadTexts:g9982PortPm1DayIntervalRxOverflows.setStatus(_A)
if mibBuilder.loadTexts:g9982PortPm1DayIntervalRxOverflows.setUnits(_D)
_G9982PortPm1DayIntervalValid_Type=TruthValue
_G9982PortPm1DayIntervalValid_Object=MibTableColumn
g9982PortPm1DayIntervalValid=_G9982PortPm1DayIntervalValid_Object((1,3,6,1,2,1,264,1,1,4,3,1,11),_G9982PortPm1DayIntervalValid_Type())
g9982PortPm1DayIntervalValid.setMaxAccess(_C)
if mibBuilder.loadTexts:g9982PortPm1DayIntervalValid.setStatus(_A)
_G9982Bce_ObjectIdentity=ObjectIdentity
g9982Bce=_G9982Bce_ObjectIdentity((1,3,6,1,2,1,264,1,2))
_G9982BceConfTable_Object=MibTable
g9982BceConfTable=_G9982BceConfTable_Object((1,3,6,1,2,1,264,1,2,1))
if mibBuilder.loadTexts:g9982BceConfTable.setStatus(_A)
_G9982BceConfEntry_Object=MibTableRow
g9982BceConfEntry=_G9982BceConfEntry_Object((1,3,6,1,2,1,264,1,2,1,1))
g9982BceConfEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:g9982BceConfEntry.setStatus(_A)
class _G9982BceConfEligibleGroupID_Type(PhysAddress):subtypeSpec=PhysAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,0),ValueSizeConstraint(6,6))
_G9982BceConfEligibleGroupID_Type.__name__=_I
_G9982BceConfEligibleGroupID_Object=MibTableColumn
g9982BceConfEligibleGroupID=_G9982BceConfEligibleGroupID_Object((1,3,6,1,2,1,264,1,2,1,1,1),_G9982BceConfEligibleGroupID_Type())
g9982BceConfEligibleGroupID.setMaxAccess(_J)
if mibBuilder.loadTexts:g9982BceConfEligibleGroupID.setStatus(_A)
class _G9982BceConfPeerEligibleGroupID_Type(PhysAddress):subtypeSpec=PhysAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,0),ValueSizeConstraint(6,6))
_G9982BceConfPeerEligibleGroupID_Type.__name__=_I
_G9982BceConfPeerEligibleGroupID_Object=MibTableColumn
g9982BceConfPeerEligibleGroupID=_G9982BceConfPeerEligibleGroupID_Object((1,3,6,1,2,1,264,1,2,1,1,2),_G9982BceConfPeerEligibleGroupID_Type())
g9982BceConfPeerEligibleGroupID.setMaxAccess(_C)
if mibBuilder.loadTexts:g9982BceConfPeerEligibleGroupID.setStatus(_A)
_G9982BceStatTable_Object=MibTable
g9982BceStatTable=_G9982BceStatTable_Object((1,3,6,1,2,1,264,1,2,2))
if mibBuilder.loadTexts:g9982BceStatTable.setStatus(_A)
_G9982BceStatEntry_Object=MibTableRow
g9982BceStatEntry=_G9982BceStatEntry_Object((1,3,6,1,2,1,264,1,2,2,1))
g9982BceStatEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:g9982BceStatEntry.setStatus(_A)
_G9982BceStatTcInCodingErrors_Type=Counter32
_G9982BceStatTcInCodingErrors_Object=MibTableColumn
g9982BceStatTcInCodingErrors=_G9982BceStatTcInCodingErrors_Object((1,3,6,1,2,1,264,1,2,2,1,1),_G9982BceStatTcInCodingErrors_Type())
g9982BceStatTcInCodingErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:g9982BceStatTcInCodingErrors.setStatus(_A)
_G9982BceStatTcInCrcErrors_Type=Counter32
_G9982BceStatTcInCrcErrors_Object=MibTableColumn
g9982BceStatTcInCrcErrors=_G9982BceStatTcInCrcErrors_Object((1,3,6,1,2,1,264,1,2,2,1,2),_G9982BceStatTcInCrcErrors_Type())
g9982BceStatTcInCrcErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:g9982BceStatTcInCrcErrors.setStatus(_A)
_G9982Conformance_ObjectIdentity=ObjectIdentity
g9982Conformance=_G9982Conformance_ObjectIdentity((1,3,6,1,2,1,264,2))
_G9982Groups_ObjectIdentity=ObjectIdentity
g9982Groups=_G9982Groups_ObjectIdentity((1,3,6,1,2,1,264,2,1))
_G9982Compliances_ObjectIdentity=ObjectIdentity
g9982Compliances=_G9982Compliances_ObjectIdentity((1,3,6,1,2,1,264,2,2))
g9982BasicGroup=ObjectGroup((1,3,6,1,2,1,264,2,1,1))
g9982BasicGroup.setObjects(*((_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_K),(_B,_L)))
if mibBuilder.loadTexts:g9982BasicGroup.setStatus(_A)
g9982BacpGroup=ObjectGroup((1,3,6,1,2,1,264,2,1,2))
g9982BacpGroup.setObjects(*((_B,_e),(_B,_f),(_B,_g),(_B,_h)))
if mibBuilder.loadTexts:g9982BacpGroup.setStatus(_A)
g9982BceGroup=ObjectGroup((1,3,6,1,2,1,264,2,1,3))
g9982BceGroup.setObjects(*((_B,_K),(_B,_L)))
if mibBuilder.loadTexts:g9982BceGroup.setStatus(_A)
g9982PerfCurrGroup=ObjectGroup((1,3,6,1,2,1,264,2,1,4))
g9982PerfCurrGroup.setObjects(*((_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_x),(_B,_y),(_B,_z),(_B,_A0),(_B,_A1),(_B,_A2),(_B,_A3)))
if mibBuilder.loadTexts:g9982PerfCurrGroup.setStatus(_A)
g9982Perf15MinGroup=ObjectGroup((1,3,6,1,2,1,264,2,1,5))
g9982Perf15MinGroup.setObjects(*((_B,_A4),(_B,_A5),(_B,_A6),(_B,_A7),(_B,_A8),(_B,_A9),(_B,_AA),(_B,_AB),(_B,_AC),(_B,_AD)))
if mibBuilder.loadTexts:g9982Perf15MinGroup.setStatus(_A)
g9982Perf1DayGroup=ObjectGroup((1,3,6,1,2,1,264,2,1,6))
g9982Perf1DayGroup.setObjects(*((_B,_AE),(_B,_AF),(_B,_AG),(_B,_AH),(_B,_AI),(_B,_AJ),(_B,_AK),(_B,_AL),(_B,_AM),(_B,_AN)))
if mibBuilder.loadTexts:g9982Perf1DayGroup.setStatus(_A)
g9982Compliance=ModuleCompliance((1,3,6,1,2,1,264,2,2,1))
g9982Compliance.setObjects(*((_B,_AO),(_B,_AP),(_B,_AQ),(_B,_AR),(_B,_AS),(_B,_AT)))
if mibBuilder.loadTexts:g9982Compliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'G9982PtmTcType':G9982PtmTcType,_O:G9982CpType,'g9982MIB':g9982MIB,'g9982Objects':g9982Objects,'g9982Port':g9982Port,'g9982PortConfTable':g9982PortConfTable,'g9982PortConfEntry':g9982PortConfEntry,_U:g9982PortConfTcAdminType,_e:g9982PortConfAdminCp,'g9982PortCapTable':g9982PortCapTable,'g9982PortCapEntry':g9982PortCapEntry,_S:g9982PortCapTcTypesSupported,_T:g9982PortCapBacpSupported,'g9982PortStatTable':g9982PortStatTable,'g9982PortStatEntry':g9982PortStatEntry,_V:g9982PortStatTcOperType,_f:g9982PortStatOperCp,_W:g9982PortStatRxErrors,_X:g9982PortStatRxSmallFragments,_Y:g9982PortStatRxLargeFragments,_Z:g9982PortStatRxBadFragments,_a:g9982PortStatRxLostFragments,_b:g9982PortStatRxLostStarts,_c:g9982PortStatRxLostEnds,_d:g9982PortStatRxOverflows,'g9982PM':g9982PM,'g9982PortPmCurTable':g9982PortPmCurTable,'g9982PortPmCurEntry':g9982PortPmCurEntry,_i:g9982PortPm15MinValidIntervals,_j:g9982PortPm15MinInvalidIntervals,_k:g9982PortPmCur15MinTimeElapsed,_l:g9982PortPmCur15MinRxErrors,_m:g9982PortPmCur15MinRxSmallFragments,_n:g9982PortPmCur15MinRxLargeFragments,_o:g9982PortPmCur15MinRxBadFragments,_p:g9982PortPmCur15MinRxLostFragments,_q:g9982PortPmCur15MinRxLostStarts,_r:g9982PortPmCur15MinRxLostEnds,_s:g9982PortPmCur15MinRxOverflows,_t:g9982PortPm1DayValidIntervals,_u:g9982PortPm1DayInvalidIntervals,_v:g9982PortPmCur1DayTimeElapsed,_w:g9982PortPmCur1DayRxErrors,_x:g9982PortPmCur1DayRxSmallFragments,_y:g9982PortPmCur1DayRxLargeFragments,_z:g9982PortPmCur1DayRxBadFragments,_A0:g9982PortPmCur1DayRxLostFragments,_A1:g9982PortPmCur1DayRxLostStarts,_A2:g9982PortPmCur1DayRxLostEnds,_A3:g9982PortPmCur1DayRxOverflows,'g9982PortPm15MinTable':g9982PortPm15MinTable,'g9982PortPm15MinEntry':g9982PortPm15MinEntry,_P:g9982PortPm15MinIntervalIndex,_A4:g9982PortPm15MinIntervalMoniTime,_A5:g9982PortPm15MinIntervalRxErrors,_A6:g9982PortPm15MinIntervalRxSmallFragments,_A7:g9982PortPm15MinIntervalRxLargeFragments,_A8:g9982PortPm15MinIntervalRxBadFragments,_A9:g9982PortPm15MinIntervalRxLostFragments,_AA:g9982PortPm15MinIntervalRxLostStarts,_AB:g9982PortPm15MinIntervalRxLostEnds,_AC:g9982PortPm15MinIntervalRxOverflows,_AD:g9982PortPm15MinIntervalValid,'g9982PortPm1DayTable':g9982PortPm1DayTable,'g9982PortPm1DayEntry':g9982PortPm1DayEntry,_R:g9982PortPm1DayIntervalIndex,_AE:g9982PortPm1DayIntervalMoniTime,_AF:g9982PortPm1DayIntervalRxErrors,_AG:g9982PortPm1DayIntervalRxSmallFragments,_AH:g9982PortPm1DayIntervalRxLargeFragments,_AI:g9982PortPm1DayIntervalRxBadFragments,_AJ:g9982PortPm1DayIntervalRxLostFragments,_AK:g9982PortPm1DayIntervalRxLostStarts,_AL:g9982PortPm1DayIntervalRxLostEnds,_AM:g9982PortPm1DayIntervalRxOverflows,_AN:g9982PortPm1DayIntervalValid,'g9982Bce':g9982Bce,'g9982BceConfTable':g9982BceConfTable,'g9982BceConfEntry':g9982BceConfEntry,_g:g9982BceConfEligibleGroupID,_h:g9982BceConfPeerEligibleGroupID,'g9982BceStatTable':g9982BceStatTable,'g9982BceStatEntry':g9982BceStatEntry,_K:g9982BceStatTcInCodingErrors,_L:g9982BceStatTcInCrcErrors,'g9982Conformance':g9982Conformance,'g9982Groups':g9982Groups,_AO:g9982BasicGroup,_AQ:g9982BacpGroup,_AP:g9982BceGroup,_AR:g9982PerfCurrGroup,_AS:g9982Perf15MinGroup,_AT:g9982Perf1DayGroup,'g9982Compliances':g9982Compliances,'g9982Compliance':g9982Compliance})