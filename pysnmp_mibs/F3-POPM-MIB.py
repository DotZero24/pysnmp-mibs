_A9='f3POPMStatsGroup'
_A8='f3POPMFacilityGroup'
_A7='f3EthernetNetPortPOPMHistoryOPROOV'
_A6='f3EthernetNetPortPOPMHistoryOPROOR'
_A5='f3EthernetNetPortPOPMHistoryOPRRTR'
_A4='f3EthernetNetPortPOPMHistoryOPRGlitchRejects'
_A3='f3EthernetNetPortPOPMHistoryOPRMaxVar'
_A2='f3EthernetNetPortPOPMHistoryOPRVar'
_A1='f3EthernetNetPortPOPMHistoryAOPR'
_A0='f3EthernetNetPortPOPMHistoryOPR'
_z='f3EthernetNetPortPOPMStatsOPROOV'
_y='f3EthernetNetPortPOPMStatsOPROOR'
_x='f3EthernetNetPortPOPMStatsOPRRTR'
_w='f3EthernetNetPortPOPMStatsOPRGlitchRejects'
_v='f3EthernetNetPortPOPMStatsOPRMaxVar'
_u='f3EthernetNetPortPOPMStatsOPRVar'
_t='f3EthernetNetPortPOPMStatsAOPR'
_s='f3EthernetNetPortPOPMStatsOPR'
_r='f3EthernetAccPortPOPMHistoryOPROOV'
_q='f3EthernetAccPortPOPMHistoryOPROOR'
_p='f3EthernetAccPortPOPMHistoryOPRRTR'
_o='f3EthernetAccPortPOPMHistoryOPRGlitchRejects'
_n='f3EthernetAccPortPOPMHistoryOPRMaxVar'
_m='f3EthernetAccPortPOPMHistoryOPRVar'
_l='f3EthernetAccPortPOPMHistoryAOPR'
_k='f3EthernetAccPortPOPMHistoryOPR'
_j='f3EthernetAccPortPOPMStatsOPROOV'
_i='f3EthernetAccPortPOPMStatsOPROOR'
_h='f3EthernetAccPortPOPMStatsOPRRTR'
_g='f3EthernetAccPortPOPMStatsOPRGlitchRejects'
_f='f3EthernetAccPortPOPMStatsOPRMaxVar'
_e='f3EthernetAccPortPOPMStatsOPRVar'
_d='f3EthernetAccPortPOPMStatsAOPR'
_c='f3EthernetAccPortPOPMStatsOPR'
_b='f3EthernetNetPortPOPMonitorClearAction'
_a='f3EthernetNetPortPOPMonitorState'
_Z='f3EthernetNetPortPOPMonitorGlitchRejectionLevel'
_Y='f3EthernetNetPortPOPMonitorWindowSize'
_X='f3EthernetNetPortPOPMonitorVariance'
_W='f3EthernetNetPortPOPMonitorOperRangeLow'
_V='f3EthernetNetPortPOPMonitorOperRangeHi'
_U='f3EthernetNetPortPOPMonitorEnabled'
_T='f3EthernetAccPortPOPMonitorClearAction'
_S='f3EthernetAccPortPOPMonitorState'
_R='f3EthernetAccPortPOPMonitorGlitchRejectionLevel'
_Q='f3EthernetAccPortPOPMonitorWindowSize'
_P='f3EthernetAccPortPOPMonitorVariance'
_O='f3EthernetAccPortPOPMonitorOperRangeLow'
_N='f3EthernetAccPortPOPMonitorOperRangeHi'
_M='f3EthernetAccPortPOPMonitorEnabled'
_L='f3EthernetNetPortPOPMHistoryEntry'
_K='f3EthernetNetPortPOPMStatsEntry'
_J='f3EthernetAccPortPOPMHistoryEntry'
_I='f3EthernetAccPortPOPMStatsEntry'
_H='f3EthernetAccPortPOPMonitorEntry'
_G='f3EthernetNetPortPOPMonitorEntry'
_F='not-applicable'
_E='Integer32'
_D='read-write'
_C='read-only'
_B='F3-POPM-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
fsp150cm,=mibBuilder.importSymbols('ADVA-MIB','fsp150cm')
PerfCounter64,=mibBuilder.importSymbols('CM-COMMON-MIB','PerfCounter64')
neIndex,shelfIndex,slotIndex=mibBuilder.importSymbols('CM-ENTITY-MIB','neIndex','shelfIndex','slotIndex')
cmEthernetAccPortEntry,cmEthernetNetPortEntry=mibBuilder.importSymbols('CM-FACILITY-MIB','cmEthernetAccPortEntry','cmEthernetNetPortEntry')
cmEthernetAccPortHistoryEntry,cmEthernetAccPortStatsEntry,cmEthernetNetPortHistoryEntry,cmEthernetNetPortStatsEntry=mibBuilder.importSymbols('CM-PERFORMANCE-MIB','cmEthernetAccPortHistoryEntry','cmEthernetAccPortStatsEntry','cmEthernetNetPortHistoryEntry','cmEthernetNetPortStatsEntry')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,PhysAddress,TextualConvention,TruthValue,VariablePointer=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','TextualConvention','TruthValue','VariablePointer')
f3POPMMib=ModuleIdentity((1,3,6,1,4,1,2544,1,12,16))
if mibBuilder.loadTexts:f3POPMMib.setRevisions(('2011-10-10 00:00',))
class POPMGlitchRejectionLevel(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('none',1),('low',2),('medium',3),('high',4)))
class POPMState(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_F,1),('inoperable',2),('not-available',3),('calibrating',4),('monitoring',5),('paused',6),('inhibited-R',7),('inhibited-NR',8)))
class POPMClearAlarmsAction(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),('clear',1)))
_F3POPMObjects_ObjectIdentity=ObjectIdentity
f3POPMObjects=_F3POPMObjects_ObjectIdentity((1,3,6,1,4,1,2544,1,12,16,1))
_F3EthernetNetPortPOPMonitorTable_Object=MibTable
f3EthernetNetPortPOPMonitorTable=_F3EthernetNetPortPOPMonitorTable_Object((1,3,6,1,4,1,2544,1,12,16,1,1))
if mibBuilder.loadTexts:f3EthernetNetPortPOPMonitorTable.setStatus(_A)
_F3EthernetNetPortPOPMonitorEntry_Object=MibTableRow
f3EthernetNetPortPOPMonitorEntry=_F3EthernetNetPortPOPMonitorEntry_Object((1,3,6,1,4,1,2544,1,12,16,1,1,1))
if mibBuilder.loadTexts:f3EthernetNetPortPOPMonitorEntry.setStatus(_A)
_F3EthernetNetPortPOPMonitorEnabled_Type=TruthValue
_F3EthernetNetPortPOPMonitorEnabled_Object=MibTableColumn
f3EthernetNetPortPOPMonitorEnabled=_F3EthernetNetPortPOPMonitorEnabled_Object((1,3,6,1,4,1,2544,1,12,16,1,1,1,1),_F3EthernetNetPortPOPMonitorEnabled_Type())
f3EthernetNetPortPOPMonitorEnabled.setMaxAccess(_D)
if mibBuilder.loadTexts:f3EthernetNetPortPOPMonitorEnabled.setStatus(_A)
_F3EthernetNetPortPOPMonitorOperRangeHi_Type=Integer32
_F3EthernetNetPortPOPMonitorOperRangeHi_Object=MibTableColumn
f3EthernetNetPortPOPMonitorOperRangeHi=_F3EthernetNetPortPOPMonitorOperRangeHi_Object((1,3,6,1,4,1,2544,1,12,16,1,1,1,2),_F3EthernetNetPortPOPMonitorOperRangeHi_Type())
f3EthernetNetPortPOPMonitorOperRangeHi.setMaxAccess(_C)
if mibBuilder.loadTexts:f3EthernetNetPortPOPMonitorOperRangeHi.setStatus(_A)
_F3EthernetNetPortPOPMonitorOperRangeLow_Type=Integer32
_F3EthernetNetPortPOPMonitorOperRangeLow_Object=MibTableColumn
f3EthernetNetPortPOPMonitorOperRangeLow=_F3EthernetNetPortPOPMonitorOperRangeLow_Object((1,3,6,1,4,1,2544,1,12,16,1,1,1,3),_F3EthernetNetPortPOPMonitorOperRangeLow_Type())
f3EthernetNetPortPOPMonitorOperRangeLow.setMaxAccess(_C)
if mibBuilder.loadTexts:f3EthernetNetPortPOPMonitorOperRangeLow.setStatus(_A)
_F3EthernetNetPortPOPMonitorVariance_Type=Integer32
_F3EthernetNetPortPOPMonitorVariance_Object=MibTableColumn
f3EthernetNetPortPOPMonitorVariance=_F3EthernetNetPortPOPMonitorVariance_Object((1,3,6,1,4,1,2544,1,12,16,1,1,1,4),_F3EthernetNetPortPOPMonitorVariance_Type())
f3EthernetNetPortPOPMonitorVariance.setMaxAccess(_D)
if mibBuilder.loadTexts:f3EthernetNetPortPOPMonitorVariance.setStatus(_A)
class _F3EthernetNetPortPOPMonitorWindowSize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,3600))
_F3EthernetNetPortPOPMonitorWindowSize_Type.__name__=_E
_F3EthernetNetPortPOPMonitorWindowSize_Object=MibTableColumn
f3EthernetNetPortPOPMonitorWindowSize=_F3EthernetNetPortPOPMonitorWindowSize_Object((1,3,6,1,4,1,2544,1,12,16,1,1,1,5),_F3EthernetNetPortPOPMonitorWindowSize_Type())
f3EthernetNetPortPOPMonitorWindowSize.setMaxAccess(_D)
if mibBuilder.loadTexts:f3EthernetNetPortPOPMonitorWindowSize.setStatus(_A)
_F3EthernetNetPortPOPMonitorGlitchRejectionLevel_Type=POPMGlitchRejectionLevel
_F3EthernetNetPortPOPMonitorGlitchRejectionLevel_Object=MibTableColumn
f3EthernetNetPortPOPMonitorGlitchRejectionLevel=_F3EthernetNetPortPOPMonitorGlitchRejectionLevel_Object((1,3,6,1,4,1,2544,1,12,16,1,1,1,6),_F3EthernetNetPortPOPMonitorGlitchRejectionLevel_Type())
f3EthernetNetPortPOPMonitorGlitchRejectionLevel.setMaxAccess(_D)
if mibBuilder.loadTexts:f3EthernetNetPortPOPMonitorGlitchRejectionLevel.setStatus(_A)
_F3EthernetNetPortPOPMonitorState_Type=POPMState
_F3EthernetNetPortPOPMonitorState_Object=MibTableColumn
f3EthernetNetPortPOPMonitorState=_F3EthernetNetPortPOPMonitorState_Object((1,3,6,1,4,1,2544,1,12,16,1,1,1,7),_F3EthernetNetPortPOPMonitorState_Type())
f3EthernetNetPortPOPMonitorState.setMaxAccess(_C)
if mibBuilder.loadTexts:f3EthernetNetPortPOPMonitorState.setStatus(_A)
_F3EthernetNetPortPOPMonitorClearAction_Type=POPMClearAlarmsAction
_F3EthernetNetPortPOPMonitorClearAction_Object=MibTableColumn
f3EthernetNetPortPOPMonitorClearAction=_F3EthernetNetPortPOPMonitorClearAction_Object((1,3,6,1,4,1,2544,1,12,16,1,1,1,8),_F3EthernetNetPortPOPMonitorClearAction_Type())
f3EthernetNetPortPOPMonitorClearAction.setMaxAccess(_D)
if mibBuilder.loadTexts:f3EthernetNetPortPOPMonitorClearAction.setStatus(_A)
_F3EthernetAccPortPOPMonitorTable_Object=MibTable
f3EthernetAccPortPOPMonitorTable=_F3EthernetAccPortPOPMonitorTable_Object((1,3,6,1,4,1,2544,1,12,16,1,2))
if mibBuilder.loadTexts:f3EthernetAccPortPOPMonitorTable.setStatus(_A)
_F3EthernetAccPortPOPMonitorEntry_Object=MibTableRow
f3EthernetAccPortPOPMonitorEntry=_F3EthernetAccPortPOPMonitorEntry_Object((1,3,6,1,4,1,2544,1,12,16,1,2,1))
if mibBuilder.loadTexts:f3EthernetAccPortPOPMonitorEntry.setStatus(_A)
_F3EthernetAccPortPOPMonitorEnabled_Type=TruthValue
_F3EthernetAccPortPOPMonitorEnabled_Object=MibTableColumn
f3EthernetAccPortPOPMonitorEnabled=_F3EthernetAccPortPOPMonitorEnabled_Object((1,3,6,1,4,1,2544,1,12,16,1,2,1,1),_F3EthernetAccPortPOPMonitorEnabled_Type())
f3EthernetAccPortPOPMonitorEnabled.setMaxAccess(_D)
if mibBuilder.loadTexts:f3EthernetAccPortPOPMonitorEnabled.setStatus(_A)
_F3EthernetAccPortPOPMonitorOperRangeHi_Type=Integer32
_F3EthernetAccPortPOPMonitorOperRangeHi_Object=MibTableColumn
f3EthernetAccPortPOPMonitorOperRangeHi=_F3EthernetAccPortPOPMonitorOperRangeHi_Object((1,3,6,1,4,1,2544,1,12,16,1,2,1,2),_F3EthernetAccPortPOPMonitorOperRangeHi_Type())
f3EthernetAccPortPOPMonitorOperRangeHi.setMaxAccess(_C)
if mibBuilder.loadTexts:f3EthernetAccPortPOPMonitorOperRangeHi.setStatus(_A)
_F3EthernetAccPortPOPMonitorOperRangeLow_Type=Integer32
_F3EthernetAccPortPOPMonitorOperRangeLow_Object=MibTableColumn
f3EthernetAccPortPOPMonitorOperRangeLow=_F3EthernetAccPortPOPMonitorOperRangeLow_Object((1,3,6,1,4,1,2544,1,12,16,1,2,1,3),_F3EthernetAccPortPOPMonitorOperRangeLow_Type())
f3EthernetAccPortPOPMonitorOperRangeLow.setMaxAccess(_C)
if mibBuilder.loadTexts:f3EthernetAccPortPOPMonitorOperRangeLow.setStatus(_A)
_F3EthernetAccPortPOPMonitorVariance_Type=Integer32
_F3EthernetAccPortPOPMonitorVariance_Object=MibTableColumn
f3EthernetAccPortPOPMonitorVariance=_F3EthernetAccPortPOPMonitorVariance_Object((1,3,6,1,4,1,2544,1,12,16,1,2,1,4),_F3EthernetAccPortPOPMonitorVariance_Type())
f3EthernetAccPortPOPMonitorVariance.setMaxAccess(_D)
if mibBuilder.loadTexts:f3EthernetAccPortPOPMonitorVariance.setStatus(_A)
class _F3EthernetAccPortPOPMonitorWindowSize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,3600))
_F3EthernetAccPortPOPMonitorWindowSize_Type.__name__=_E
_F3EthernetAccPortPOPMonitorWindowSize_Object=MibTableColumn
f3EthernetAccPortPOPMonitorWindowSize=_F3EthernetAccPortPOPMonitorWindowSize_Object((1,3,6,1,4,1,2544,1,12,16,1,2,1,5),_F3EthernetAccPortPOPMonitorWindowSize_Type())
f3EthernetAccPortPOPMonitorWindowSize.setMaxAccess(_D)
if mibBuilder.loadTexts:f3EthernetAccPortPOPMonitorWindowSize.setStatus(_A)
_F3EthernetAccPortPOPMonitorGlitchRejectionLevel_Type=POPMGlitchRejectionLevel
_F3EthernetAccPortPOPMonitorGlitchRejectionLevel_Object=MibTableColumn
f3EthernetAccPortPOPMonitorGlitchRejectionLevel=_F3EthernetAccPortPOPMonitorGlitchRejectionLevel_Object((1,3,6,1,4,1,2544,1,12,16,1,2,1,6),_F3EthernetAccPortPOPMonitorGlitchRejectionLevel_Type())
f3EthernetAccPortPOPMonitorGlitchRejectionLevel.setMaxAccess(_D)
if mibBuilder.loadTexts:f3EthernetAccPortPOPMonitorGlitchRejectionLevel.setStatus(_A)
_F3EthernetAccPortPOPMonitorState_Type=POPMState
_F3EthernetAccPortPOPMonitorState_Object=MibTableColumn
f3EthernetAccPortPOPMonitorState=_F3EthernetAccPortPOPMonitorState_Object((1,3,6,1,4,1,2544,1,12,16,1,2,1,7),_F3EthernetAccPortPOPMonitorState_Type())
f3EthernetAccPortPOPMonitorState.setMaxAccess(_C)
if mibBuilder.loadTexts:f3EthernetAccPortPOPMonitorState.setStatus(_A)
_F3EthernetAccPortPOPMonitorClearAction_Type=POPMClearAlarmsAction
_F3EthernetAccPortPOPMonitorClearAction_Object=MibTableColumn
f3EthernetAccPortPOPMonitorClearAction=_F3EthernetAccPortPOPMonitorClearAction_Object((1,3,6,1,4,1,2544,1,12,16,1,2,1,8),_F3EthernetAccPortPOPMonitorClearAction_Type())
f3EthernetAccPortPOPMonitorClearAction.setMaxAccess(_D)
if mibBuilder.loadTexts:f3EthernetAccPortPOPMonitorClearAction.setStatus(_A)
_F3POPMPerfObjects_ObjectIdentity=ObjectIdentity
f3POPMPerfObjects=_F3POPMPerfObjects_ObjectIdentity((1,3,6,1,4,1,2544,1,12,16,2))
_F3EthernetAccPortPOPMStatsTable_Object=MibTable
f3EthernetAccPortPOPMStatsTable=_F3EthernetAccPortPOPMStatsTable_Object((1,3,6,1,4,1,2544,1,12,16,2,1))
if mibBuilder.loadTexts:f3EthernetAccPortPOPMStatsTable.setStatus(_A)
_F3EthernetAccPortPOPMStatsEntry_Object=MibTableRow
f3EthernetAccPortPOPMStatsEntry=_F3EthernetAccPortPOPMStatsEntry_Object((1,3,6,1,4,1,2544,1,12,16,2,1,1))
if mibBuilder.loadTexts:f3EthernetAccPortPOPMStatsEntry.setStatus(_A)
_F3EthernetAccPortPOPMStatsOPR_Type=Integer32
_F3EthernetAccPortPOPMStatsOPR_Object=MibTableColumn
f3EthernetAccPortPOPMStatsOPR=_F3EthernetAccPortPOPMStatsOPR_Object((1,3,6,1,4,1,2544,1,12,16,2,1,1,1),_F3EthernetAccPortPOPMStatsOPR_Type())
f3EthernetAccPortPOPMStatsOPR.setMaxAccess(_C)
if mibBuilder.loadTexts:f3EthernetAccPortPOPMStatsOPR.setStatus(_A)
_F3EthernetAccPortPOPMStatsAOPR_Type=Integer32
_F3EthernetAccPortPOPMStatsAOPR_Object=MibTableColumn
f3EthernetAccPortPOPMStatsAOPR=_F3EthernetAccPortPOPMStatsAOPR_Object((1,3,6,1,4,1,2544,1,12,16,2,1,1,2),_F3EthernetAccPortPOPMStatsAOPR_Type())
f3EthernetAccPortPOPMStatsAOPR.setMaxAccess(_C)
if mibBuilder.loadTexts:f3EthernetAccPortPOPMStatsAOPR.setStatus(_A)
_F3EthernetAccPortPOPMStatsOPRVar_Type=Integer32
_F3EthernetAccPortPOPMStatsOPRVar_Object=MibTableColumn
f3EthernetAccPortPOPMStatsOPRVar=_F3EthernetAccPortPOPMStatsOPRVar_Object((1,3,6,1,4,1,2544,1,12,16,2,1,1,3),_F3EthernetAccPortPOPMStatsOPRVar_Type())
f3EthernetAccPortPOPMStatsOPRVar.setMaxAccess(_C)
if mibBuilder.loadTexts:f3EthernetAccPortPOPMStatsOPRVar.setStatus(_A)
_F3EthernetAccPortPOPMStatsOPRMaxVar_Type=Integer32
_F3EthernetAccPortPOPMStatsOPRMaxVar_Object=MibTableColumn
f3EthernetAccPortPOPMStatsOPRMaxVar=_F3EthernetAccPortPOPMStatsOPRMaxVar_Object((1,3,6,1,4,1,2544,1,12,16,2,1,1,4),_F3EthernetAccPortPOPMStatsOPRMaxVar_Type())
f3EthernetAccPortPOPMStatsOPRMaxVar.setMaxAccess(_C)
if mibBuilder.loadTexts:f3EthernetAccPortPOPMStatsOPRMaxVar.setStatus(_A)
_F3EthernetAccPortPOPMStatsOPRGlitchRejects_Type=Unsigned32
_F3EthernetAccPortPOPMStatsOPRGlitchRejects_Object=MibTableColumn
f3EthernetAccPortPOPMStatsOPRGlitchRejects=_F3EthernetAccPortPOPMStatsOPRGlitchRejects_Object((1,3,6,1,4,1,2544,1,12,16,2,1,1,5),_F3EthernetAccPortPOPMStatsOPRGlitchRejects_Type())
f3EthernetAccPortPOPMStatsOPRGlitchRejects.setMaxAccess(_C)
if mibBuilder.loadTexts:f3EthernetAccPortPOPMStatsOPRGlitchRejects.setStatus(_A)
_F3EthernetAccPortPOPMStatsOPRRTR_Type=Unsigned32
_F3EthernetAccPortPOPMStatsOPRRTR_Object=MibTableColumn
f3EthernetAccPortPOPMStatsOPRRTR=_F3EthernetAccPortPOPMStatsOPRRTR_Object((1,3,6,1,4,1,2544,1,12,16,2,1,1,6),_F3EthernetAccPortPOPMStatsOPRRTR_Type())
f3EthernetAccPortPOPMStatsOPRRTR.setMaxAccess(_C)
if mibBuilder.loadTexts:f3EthernetAccPortPOPMStatsOPRRTR.setStatus(_A)
_F3EthernetAccPortPOPMStatsOPROOR_Type=Unsigned32
_F3EthernetAccPortPOPMStatsOPROOR_Object=MibTableColumn
f3EthernetAccPortPOPMStatsOPROOR=_F3EthernetAccPortPOPMStatsOPROOR_Object((1,3,6,1,4,1,2544,1,12,16,2,1,1,7),_F3EthernetAccPortPOPMStatsOPROOR_Type())
f3EthernetAccPortPOPMStatsOPROOR.setMaxAccess(_C)
if mibBuilder.loadTexts:f3EthernetAccPortPOPMStatsOPROOR.setStatus(_A)
_F3EthernetAccPortPOPMStatsOPROOV_Type=Unsigned32
_F3EthernetAccPortPOPMStatsOPROOV_Object=MibTableColumn
f3EthernetAccPortPOPMStatsOPROOV=_F3EthernetAccPortPOPMStatsOPROOV_Object((1,3,6,1,4,1,2544,1,12,16,2,1,1,8),_F3EthernetAccPortPOPMStatsOPROOV_Type())
f3EthernetAccPortPOPMStatsOPROOV.setMaxAccess(_C)
if mibBuilder.loadTexts:f3EthernetAccPortPOPMStatsOPROOV.setStatus(_A)
_F3EthernetAccPortPOPMHistoryTable_Object=MibTable
f3EthernetAccPortPOPMHistoryTable=_F3EthernetAccPortPOPMHistoryTable_Object((1,3,6,1,4,1,2544,1,12,16,2,2))
if mibBuilder.loadTexts:f3EthernetAccPortPOPMHistoryTable.setStatus(_A)
_F3EthernetAccPortPOPMHistoryEntry_Object=MibTableRow
f3EthernetAccPortPOPMHistoryEntry=_F3EthernetAccPortPOPMHistoryEntry_Object((1,3,6,1,4,1,2544,1,12,16,2,2,1))
if mibBuilder.loadTexts:f3EthernetAccPortPOPMHistoryEntry.setStatus(_A)
_F3EthernetAccPortPOPMHistoryOPR_Type=Integer32
_F3EthernetAccPortPOPMHistoryOPR_Object=MibTableColumn
f3EthernetAccPortPOPMHistoryOPR=_F3EthernetAccPortPOPMHistoryOPR_Object((1,3,6,1,4,1,2544,1,12,16,2,2,1,1),_F3EthernetAccPortPOPMHistoryOPR_Type())
f3EthernetAccPortPOPMHistoryOPR.setMaxAccess(_C)
if mibBuilder.loadTexts:f3EthernetAccPortPOPMHistoryOPR.setStatus(_A)
_F3EthernetAccPortPOPMHistoryAOPR_Type=Integer32
_F3EthernetAccPortPOPMHistoryAOPR_Object=MibTableColumn
f3EthernetAccPortPOPMHistoryAOPR=_F3EthernetAccPortPOPMHistoryAOPR_Object((1,3,6,1,4,1,2544,1,12,16,2,2,1,2),_F3EthernetAccPortPOPMHistoryAOPR_Type())
f3EthernetAccPortPOPMHistoryAOPR.setMaxAccess(_C)
if mibBuilder.loadTexts:f3EthernetAccPortPOPMHistoryAOPR.setStatus(_A)
_F3EthernetAccPortPOPMHistoryOPRVar_Type=Integer32
_F3EthernetAccPortPOPMHistoryOPRVar_Object=MibTableColumn
f3EthernetAccPortPOPMHistoryOPRVar=_F3EthernetAccPortPOPMHistoryOPRVar_Object((1,3,6,1,4,1,2544,1,12,16,2,2,1,3),_F3EthernetAccPortPOPMHistoryOPRVar_Type())
f3EthernetAccPortPOPMHistoryOPRVar.setMaxAccess(_C)
if mibBuilder.loadTexts:f3EthernetAccPortPOPMHistoryOPRVar.setStatus(_A)
_F3EthernetAccPortPOPMHistoryOPRMaxVar_Type=Integer32
_F3EthernetAccPortPOPMHistoryOPRMaxVar_Object=MibTableColumn
f3EthernetAccPortPOPMHistoryOPRMaxVar=_F3EthernetAccPortPOPMHistoryOPRMaxVar_Object((1,3,6,1,4,1,2544,1,12,16,2,2,1,4),_F3EthernetAccPortPOPMHistoryOPRMaxVar_Type())
f3EthernetAccPortPOPMHistoryOPRMaxVar.setMaxAccess(_C)
if mibBuilder.loadTexts:f3EthernetAccPortPOPMHistoryOPRMaxVar.setStatus(_A)
_F3EthernetAccPortPOPMHistoryOPRGlitchRejects_Type=Unsigned32
_F3EthernetAccPortPOPMHistoryOPRGlitchRejects_Object=MibTableColumn
f3EthernetAccPortPOPMHistoryOPRGlitchRejects=_F3EthernetAccPortPOPMHistoryOPRGlitchRejects_Object((1,3,6,1,4,1,2544,1,12,16,2,2,1,5),_F3EthernetAccPortPOPMHistoryOPRGlitchRejects_Type())
f3EthernetAccPortPOPMHistoryOPRGlitchRejects.setMaxAccess(_C)
if mibBuilder.loadTexts:f3EthernetAccPortPOPMHistoryOPRGlitchRejects.setStatus(_A)
_F3EthernetAccPortPOPMHistoryOPRRTR_Type=Unsigned32
_F3EthernetAccPortPOPMHistoryOPRRTR_Object=MibTableColumn
f3EthernetAccPortPOPMHistoryOPRRTR=_F3EthernetAccPortPOPMHistoryOPRRTR_Object((1,3,6,1,4,1,2544,1,12,16,2,2,1,6),_F3EthernetAccPortPOPMHistoryOPRRTR_Type())
f3EthernetAccPortPOPMHistoryOPRRTR.setMaxAccess(_C)
if mibBuilder.loadTexts:f3EthernetAccPortPOPMHistoryOPRRTR.setStatus(_A)
_F3EthernetAccPortPOPMHistoryOPROOR_Type=Unsigned32
_F3EthernetAccPortPOPMHistoryOPROOR_Object=MibTableColumn
f3EthernetAccPortPOPMHistoryOPROOR=_F3EthernetAccPortPOPMHistoryOPROOR_Object((1,3,6,1,4,1,2544,1,12,16,2,2,1,7),_F3EthernetAccPortPOPMHistoryOPROOR_Type())
f3EthernetAccPortPOPMHistoryOPROOR.setMaxAccess(_C)
if mibBuilder.loadTexts:f3EthernetAccPortPOPMHistoryOPROOR.setStatus(_A)
_F3EthernetAccPortPOPMHistoryOPROOV_Type=Unsigned32
_F3EthernetAccPortPOPMHistoryOPROOV_Object=MibTableColumn
f3EthernetAccPortPOPMHistoryOPROOV=_F3EthernetAccPortPOPMHistoryOPROOV_Object((1,3,6,1,4,1,2544,1,12,16,2,2,1,8),_F3EthernetAccPortPOPMHistoryOPROOV_Type())
f3EthernetAccPortPOPMHistoryOPROOV.setMaxAccess(_C)
if mibBuilder.loadTexts:f3EthernetAccPortPOPMHistoryOPROOV.setStatus(_A)
_F3EthernetNetPortPOPMStatsTable_Object=MibTable
f3EthernetNetPortPOPMStatsTable=_F3EthernetNetPortPOPMStatsTable_Object((1,3,6,1,4,1,2544,1,12,16,2,3))
if mibBuilder.loadTexts:f3EthernetNetPortPOPMStatsTable.setStatus(_A)
_F3EthernetNetPortPOPMStatsEntry_Object=MibTableRow
f3EthernetNetPortPOPMStatsEntry=_F3EthernetNetPortPOPMStatsEntry_Object((1,3,6,1,4,1,2544,1,12,16,2,3,1))
if mibBuilder.loadTexts:f3EthernetNetPortPOPMStatsEntry.setStatus(_A)
_F3EthernetNetPortPOPMStatsOPR_Type=Integer32
_F3EthernetNetPortPOPMStatsOPR_Object=MibTableColumn
f3EthernetNetPortPOPMStatsOPR=_F3EthernetNetPortPOPMStatsOPR_Object((1,3,6,1,4,1,2544,1,12,16,2,3,1,1),_F3EthernetNetPortPOPMStatsOPR_Type())
f3EthernetNetPortPOPMStatsOPR.setMaxAccess(_C)
if mibBuilder.loadTexts:f3EthernetNetPortPOPMStatsOPR.setStatus(_A)
_F3EthernetNetPortPOPMStatsAOPR_Type=Integer32
_F3EthernetNetPortPOPMStatsAOPR_Object=MibTableColumn
f3EthernetNetPortPOPMStatsAOPR=_F3EthernetNetPortPOPMStatsAOPR_Object((1,3,6,1,4,1,2544,1,12,16,2,3,1,2),_F3EthernetNetPortPOPMStatsAOPR_Type())
f3EthernetNetPortPOPMStatsAOPR.setMaxAccess(_C)
if mibBuilder.loadTexts:f3EthernetNetPortPOPMStatsAOPR.setStatus(_A)
_F3EthernetNetPortPOPMStatsOPRVar_Type=Integer32
_F3EthernetNetPortPOPMStatsOPRVar_Object=MibTableColumn
f3EthernetNetPortPOPMStatsOPRVar=_F3EthernetNetPortPOPMStatsOPRVar_Object((1,3,6,1,4,1,2544,1,12,16,2,3,1,3),_F3EthernetNetPortPOPMStatsOPRVar_Type())
f3EthernetNetPortPOPMStatsOPRVar.setMaxAccess(_C)
if mibBuilder.loadTexts:f3EthernetNetPortPOPMStatsOPRVar.setStatus(_A)
_F3EthernetNetPortPOPMStatsOPRMaxVar_Type=Integer32
_F3EthernetNetPortPOPMStatsOPRMaxVar_Object=MibTableColumn
f3EthernetNetPortPOPMStatsOPRMaxVar=_F3EthernetNetPortPOPMStatsOPRMaxVar_Object((1,3,6,1,4,1,2544,1,12,16,2,3,1,4),_F3EthernetNetPortPOPMStatsOPRMaxVar_Type())
f3EthernetNetPortPOPMStatsOPRMaxVar.setMaxAccess(_C)
if mibBuilder.loadTexts:f3EthernetNetPortPOPMStatsOPRMaxVar.setStatus(_A)
_F3EthernetNetPortPOPMStatsOPRGlitchRejects_Type=Unsigned32
_F3EthernetNetPortPOPMStatsOPRGlitchRejects_Object=MibTableColumn
f3EthernetNetPortPOPMStatsOPRGlitchRejects=_F3EthernetNetPortPOPMStatsOPRGlitchRejects_Object((1,3,6,1,4,1,2544,1,12,16,2,3,1,5),_F3EthernetNetPortPOPMStatsOPRGlitchRejects_Type())
f3EthernetNetPortPOPMStatsOPRGlitchRejects.setMaxAccess(_C)
if mibBuilder.loadTexts:f3EthernetNetPortPOPMStatsOPRGlitchRejects.setStatus(_A)
_F3EthernetNetPortPOPMStatsOPRRTR_Type=Unsigned32
_F3EthernetNetPortPOPMStatsOPRRTR_Object=MibTableColumn
f3EthernetNetPortPOPMStatsOPRRTR=_F3EthernetNetPortPOPMStatsOPRRTR_Object((1,3,6,1,4,1,2544,1,12,16,2,3,1,6),_F3EthernetNetPortPOPMStatsOPRRTR_Type())
f3EthernetNetPortPOPMStatsOPRRTR.setMaxAccess(_C)
if mibBuilder.loadTexts:f3EthernetNetPortPOPMStatsOPRRTR.setStatus(_A)
_F3EthernetNetPortPOPMStatsOPROOR_Type=Unsigned32
_F3EthernetNetPortPOPMStatsOPROOR_Object=MibTableColumn
f3EthernetNetPortPOPMStatsOPROOR=_F3EthernetNetPortPOPMStatsOPROOR_Object((1,3,6,1,4,1,2544,1,12,16,2,3,1,7),_F3EthernetNetPortPOPMStatsOPROOR_Type())
f3EthernetNetPortPOPMStatsOPROOR.setMaxAccess(_C)
if mibBuilder.loadTexts:f3EthernetNetPortPOPMStatsOPROOR.setStatus(_A)
_F3EthernetNetPortPOPMStatsOPROOV_Type=Unsigned32
_F3EthernetNetPortPOPMStatsOPROOV_Object=MibTableColumn
f3EthernetNetPortPOPMStatsOPROOV=_F3EthernetNetPortPOPMStatsOPROOV_Object((1,3,6,1,4,1,2544,1,12,16,2,3,1,8),_F3EthernetNetPortPOPMStatsOPROOV_Type())
f3EthernetNetPortPOPMStatsOPROOV.setMaxAccess(_C)
if mibBuilder.loadTexts:f3EthernetNetPortPOPMStatsOPROOV.setStatus(_A)
_F3EthernetNetPortPOPMHistoryTable_Object=MibTable
f3EthernetNetPortPOPMHistoryTable=_F3EthernetNetPortPOPMHistoryTable_Object((1,3,6,1,4,1,2544,1,12,16,2,4))
if mibBuilder.loadTexts:f3EthernetNetPortPOPMHistoryTable.setStatus(_A)
_F3EthernetNetPortPOPMHistoryEntry_Object=MibTableRow
f3EthernetNetPortPOPMHistoryEntry=_F3EthernetNetPortPOPMHistoryEntry_Object((1,3,6,1,4,1,2544,1,12,16,2,4,1))
if mibBuilder.loadTexts:f3EthernetNetPortPOPMHistoryEntry.setStatus(_A)
_F3EthernetNetPortPOPMHistoryOPR_Type=Integer32
_F3EthernetNetPortPOPMHistoryOPR_Object=MibTableColumn
f3EthernetNetPortPOPMHistoryOPR=_F3EthernetNetPortPOPMHistoryOPR_Object((1,3,6,1,4,1,2544,1,12,16,2,4,1,1),_F3EthernetNetPortPOPMHistoryOPR_Type())
f3EthernetNetPortPOPMHistoryOPR.setMaxAccess(_C)
if mibBuilder.loadTexts:f3EthernetNetPortPOPMHistoryOPR.setStatus(_A)
_F3EthernetNetPortPOPMHistoryAOPR_Type=Integer32
_F3EthernetNetPortPOPMHistoryAOPR_Object=MibTableColumn
f3EthernetNetPortPOPMHistoryAOPR=_F3EthernetNetPortPOPMHistoryAOPR_Object((1,3,6,1,4,1,2544,1,12,16,2,4,1,2),_F3EthernetNetPortPOPMHistoryAOPR_Type())
f3EthernetNetPortPOPMHistoryAOPR.setMaxAccess(_C)
if mibBuilder.loadTexts:f3EthernetNetPortPOPMHistoryAOPR.setStatus(_A)
_F3EthernetNetPortPOPMHistoryOPRVar_Type=Integer32
_F3EthernetNetPortPOPMHistoryOPRVar_Object=MibTableColumn
f3EthernetNetPortPOPMHistoryOPRVar=_F3EthernetNetPortPOPMHistoryOPRVar_Object((1,3,6,1,4,1,2544,1,12,16,2,4,1,3),_F3EthernetNetPortPOPMHistoryOPRVar_Type())
f3EthernetNetPortPOPMHistoryOPRVar.setMaxAccess(_C)
if mibBuilder.loadTexts:f3EthernetNetPortPOPMHistoryOPRVar.setStatus(_A)
_F3EthernetNetPortPOPMHistoryOPRMaxVar_Type=Integer32
_F3EthernetNetPortPOPMHistoryOPRMaxVar_Object=MibTableColumn
f3EthernetNetPortPOPMHistoryOPRMaxVar=_F3EthernetNetPortPOPMHistoryOPRMaxVar_Object((1,3,6,1,4,1,2544,1,12,16,2,4,1,4),_F3EthernetNetPortPOPMHistoryOPRMaxVar_Type())
f3EthernetNetPortPOPMHistoryOPRMaxVar.setMaxAccess(_C)
if mibBuilder.loadTexts:f3EthernetNetPortPOPMHistoryOPRMaxVar.setStatus(_A)
_F3EthernetNetPortPOPMHistoryOPRGlitchRejects_Type=Unsigned32
_F3EthernetNetPortPOPMHistoryOPRGlitchRejects_Object=MibTableColumn
f3EthernetNetPortPOPMHistoryOPRGlitchRejects=_F3EthernetNetPortPOPMHistoryOPRGlitchRejects_Object((1,3,6,1,4,1,2544,1,12,16,2,4,1,5),_F3EthernetNetPortPOPMHistoryOPRGlitchRejects_Type())
f3EthernetNetPortPOPMHistoryOPRGlitchRejects.setMaxAccess(_C)
if mibBuilder.loadTexts:f3EthernetNetPortPOPMHistoryOPRGlitchRejects.setStatus(_A)
_F3EthernetNetPortPOPMHistoryOPRRTR_Type=Unsigned32
_F3EthernetNetPortPOPMHistoryOPRRTR_Object=MibTableColumn
f3EthernetNetPortPOPMHistoryOPRRTR=_F3EthernetNetPortPOPMHistoryOPRRTR_Object((1,3,6,1,4,1,2544,1,12,16,2,4,1,6),_F3EthernetNetPortPOPMHistoryOPRRTR_Type())
f3EthernetNetPortPOPMHistoryOPRRTR.setMaxAccess(_C)
if mibBuilder.loadTexts:f3EthernetNetPortPOPMHistoryOPRRTR.setStatus(_A)
_F3EthernetNetPortPOPMHistoryOPROOR_Type=Unsigned32
_F3EthernetNetPortPOPMHistoryOPROOR_Object=MibTableColumn
f3EthernetNetPortPOPMHistoryOPROOR=_F3EthernetNetPortPOPMHistoryOPROOR_Object((1,3,6,1,4,1,2544,1,12,16,2,4,1,7),_F3EthernetNetPortPOPMHistoryOPROOR_Type())
f3EthernetNetPortPOPMHistoryOPROOR.setMaxAccess(_C)
if mibBuilder.loadTexts:f3EthernetNetPortPOPMHistoryOPROOR.setStatus(_A)
_F3EthernetNetPortPOPMHistoryOPROOV_Type=Unsigned32
_F3EthernetNetPortPOPMHistoryOPROOV_Object=MibTableColumn
f3EthernetNetPortPOPMHistoryOPROOV=_F3EthernetNetPortPOPMHistoryOPROOV_Object((1,3,6,1,4,1,2544,1,12,16,2,4,1,8),_F3EthernetNetPortPOPMHistoryOPROOV_Type())
f3EthernetNetPortPOPMHistoryOPROOV.setMaxAccess(_C)
if mibBuilder.loadTexts:f3EthernetNetPortPOPMHistoryOPROOV.setStatus(_A)
_F3POPMConformance_ObjectIdentity=ObjectIdentity
f3POPMConformance=_F3POPMConformance_ObjectIdentity((1,3,6,1,4,1,2544,1,12,16,3))
_F3POPMCompliances_ObjectIdentity=ObjectIdentity
f3POPMCompliances=_F3POPMCompliances_ObjectIdentity((1,3,6,1,4,1,2544,1,12,16,3,1))
_F3POPMGroups_ObjectIdentity=ObjectIdentity
f3POPMGroups=_F3POPMGroups_ObjectIdentity((1,3,6,1,4,1,2544,1,12,16,3,2))
cmEthernetNetPortEntry.registerAugmentions((_B,_G))
f3EthernetNetPortPOPMonitorEntry.setIndexNames(*cmEthernetNetPortEntry.getIndexNames())
cmEthernetAccPortEntry.registerAugmentions((_B,_H))
f3EthernetAccPortPOPMonitorEntry.setIndexNames(*cmEthernetAccPortEntry.getIndexNames())
cmEthernetAccPortStatsEntry.registerAugmentions((_B,_I))
f3EthernetAccPortPOPMStatsEntry.setIndexNames(*cmEthernetAccPortStatsEntry.getIndexNames())
cmEthernetAccPortHistoryEntry.registerAugmentions((_B,_J))
f3EthernetAccPortPOPMHistoryEntry.setIndexNames(*cmEthernetAccPortHistoryEntry.getIndexNames())
cmEthernetNetPortStatsEntry.registerAugmentions((_B,_K))
f3EthernetNetPortPOPMStatsEntry.setIndexNames(*cmEthernetNetPortStatsEntry.getIndexNames())
cmEthernetNetPortHistoryEntry.registerAugmentions((_B,_L))
f3EthernetNetPortPOPMHistoryEntry.setIndexNames(*cmEthernetNetPortHistoryEntry.getIndexNames())
f3POPMFacilityGroup=ObjectGroup((1,3,6,1,4,1,2544,1,12,16,3,2,1))
f3POPMFacilityGroup.setObjects(*((_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b)))
if mibBuilder.loadTexts:f3POPMFacilityGroup.setStatus(_A)
f3POPMStatsGroup=ObjectGroup((1,3,6,1,4,1,2544,1,12,16,3,2,2))
f3POPMStatsGroup.setObjects(*((_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_x),(_B,_y),(_B,_z),(_B,_A0),(_B,_A1),(_B,_A2),(_B,_A3),(_B,_A4),(_B,_A5),(_B,_A6),(_B,_A7)))
if mibBuilder.loadTexts:f3POPMStatsGroup.setStatus(_A)
f3POPMCompliance=ModuleCompliance((1,3,6,1,4,1,2544,1,12,16,3,1,1))
f3POPMCompliance.setObjects(*((_B,_A8),(_B,_A9)))
if mibBuilder.loadTexts:f3POPMCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'POPMGlitchRejectionLevel':POPMGlitchRejectionLevel,'POPMState':POPMState,'POPMClearAlarmsAction':POPMClearAlarmsAction,'f3POPMMib':f3POPMMib,'f3POPMObjects':f3POPMObjects,'f3EthernetNetPortPOPMonitorTable':f3EthernetNetPortPOPMonitorTable,_G:f3EthernetNetPortPOPMonitorEntry,_U:f3EthernetNetPortPOPMonitorEnabled,_V:f3EthernetNetPortPOPMonitorOperRangeHi,_W:f3EthernetNetPortPOPMonitorOperRangeLow,_X:f3EthernetNetPortPOPMonitorVariance,_Y:f3EthernetNetPortPOPMonitorWindowSize,_Z:f3EthernetNetPortPOPMonitorGlitchRejectionLevel,_a:f3EthernetNetPortPOPMonitorState,_b:f3EthernetNetPortPOPMonitorClearAction,'f3EthernetAccPortPOPMonitorTable':f3EthernetAccPortPOPMonitorTable,_H:f3EthernetAccPortPOPMonitorEntry,_M:f3EthernetAccPortPOPMonitorEnabled,_N:f3EthernetAccPortPOPMonitorOperRangeHi,_O:f3EthernetAccPortPOPMonitorOperRangeLow,_P:f3EthernetAccPortPOPMonitorVariance,_Q:f3EthernetAccPortPOPMonitorWindowSize,_R:f3EthernetAccPortPOPMonitorGlitchRejectionLevel,_S:f3EthernetAccPortPOPMonitorState,_T:f3EthernetAccPortPOPMonitorClearAction,'f3POPMPerfObjects':f3POPMPerfObjects,'f3EthernetAccPortPOPMStatsTable':f3EthernetAccPortPOPMStatsTable,_I:f3EthernetAccPortPOPMStatsEntry,_c:f3EthernetAccPortPOPMStatsOPR,_d:f3EthernetAccPortPOPMStatsAOPR,_e:f3EthernetAccPortPOPMStatsOPRVar,_f:f3EthernetAccPortPOPMStatsOPRMaxVar,_g:f3EthernetAccPortPOPMStatsOPRGlitchRejects,_h:f3EthernetAccPortPOPMStatsOPRRTR,_i:f3EthernetAccPortPOPMStatsOPROOR,_j:f3EthernetAccPortPOPMStatsOPROOV,'f3EthernetAccPortPOPMHistoryTable':f3EthernetAccPortPOPMHistoryTable,_J:f3EthernetAccPortPOPMHistoryEntry,_k:f3EthernetAccPortPOPMHistoryOPR,_l:f3EthernetAccPortPOPMHistoryAOPR,_m:f3EthernetAccPortPOPMHistoryOPRVar,_n:f3EthernetAccPortPOPMHistoryOPRMaxVar,_o:f3EthernetAccPortPOPMHistoryOPRGlitchRejects,_p:f3EthernetAccPortPOPMHistoryOPRRTR,_q:f3EthernetAccPortPOPMHistoryOPROOR,_r:f3EthernetAccPortPOPMHistoryOPROOV,'f3EthernetNetPortPOPMStatsTable':f3EthernetNetPortPOPMStatsTable,_K:f3EthernetNetPortPOPMStatsEntry,_s:f3EthernetNetPortPOPMStatsOPR,_t:f3EthernetNetPortPOPMStatsAOPR,_u:f3EthernetNetPortPOPMStatsOPRVar,_v:f3EthernetNetPortPOPMStatsOPRMaxVar,_w:f3EthernetNetPortPOPMStatsOPRGlitchRejects,_x:f3EthernetNetPortPOPMStatsOPRRTR,_y:f3EthernetNetPortPOPMStatsOPROOR,_z:f3EthernetNetPortPOPMStatsOPROOV,'f3EthernetNetPortPOPMHistoryTable':f3EthernetNetPortPOPMHistoryTable,_L:f3EthernetNetPortPOPMHistoryEntry,_A0:f3EthernetNetPortPOPMHistoryOPR,_A1:f3EthernetNetPortPOPMHistoryAOPR,_A2:f3EthernetNetPortPOPMHistoryOPRVar,_A3:f3EthernetNetPortPOPMHistoryOPRMaxVar,_A4:f3EthernetNetPortPOPMHistoryOPRGlitchRejects,_A5:f3EthernetNetPortPOPMHistoryOPRRTR,_A6:f3EthernetNetPortPOPMHistoryOPROOR,_A7:f3EthernetNetPortPOPMHistoryOPROOV,'f3POPMConformance':f3POPMConformance,'f3POPMCompliances':f3POPMCompliances,'f3POPMCompliance':f3POPMCompliance,'f3POPMGroups':f3POPMGroups,_A8:f3POPMFacilityGroup,_A9:f3POPMStatsGroup})