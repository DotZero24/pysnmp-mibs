_n='ochCtpGroup'
_m='ochCtpBwResilientCtLoopControl'
_l='ochCtpBwResilientSsLoopControl'
_k='ochCtpAggresivePolarizationTracking'
_j='ochCtpRapidRecovery'
_i='ochCtpFineGranularPreFecQSampling'
_h='ochCtpFineGranularPreFecQ'
_g='ochCtpChromaticDispersionRange'
_f='ochCtpSupportingCarrierList'
_e='ochCtpPreFecBERSigDegTCAReporting'
_d='ochCtpPreFecBERSigDegHysteresis'
_c='ochCtpPreFecBERSigDegThreshold'
_b='ochCtpPreFecQSigDegTCAReporting'
_a='ochCtpPreFecQSigDegHysteresis'
_Z='ochCtpPreFecQSigDegThreshold'
_Y='ochCtpPmdHighTCAReporting'
_X='ochCtpPmdHighThreshold'
_W='ochCtpTxXYAlignment'
_V='ochCtpEncodingMode'
_U='ochCtpTxShutdown'
_T='ochCtpTxDisableActionOnAdminLock'
_S='ochCtpLaneShuffling'
_R='ochCtpFFCRXYAveraging'
_Q='ochCtpFFCRBlockSize'
_P='ochCtpFFCRMode'
_O='ochCtpChromaticDispersionSet'
_N='ochCtpCDCompMode'
_M='ochCtpDataUsageState'
_L='ochCtpRate'
_K='ochCtpModulation'
_J='ochCtpCarrierGroupMode'
_I='ochCtpPmHistStatsEnable'
_H='ochCtpSignalDegradeReporting'
_G='InfnPmHistStatsControl'
_F='ifIndex'
_E='IF-MIB'
_D='read-only'
_C='read-write'
_B='INFINERA-TP-OCHCTP-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_E,_F)
terminationPoint,=mibBuilder.importSymbols('INFINERA-REG-MIB','terminationPoint')
FloatTenths,InfnCDCompType,InfnCDRange,InfnCarrierType,InfnEnableDisable,InfnEncoding,InfnFFCRMode,InfnModulation,InfnPmHistStatsControl,InfnReporting,InfnTxDisableActionOnAdminLock,InfnUsageState,InfnXYAlignment=mibBuilder.importSymbols('INFINERA-TC-MIB','FloatTenths','InfnCDCompType','InfnCDRange','InfnCarrierType','InfnEnableDisable','InfnEncoding','InfnFFCRMode','InfnModulation',_G,'InfnReporting','InfnTxDisableActionOnAdminLock','InfnUsageState','InfnXYAlignment')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
ochCtpMIB=ModuleIdentity((1,3,6,1,4,1,21296,2,2,2,2,33))
if mibBuilder.loadTexts:ochCtpMIB.setRevisions(('2011-09-03 00:00',))
_OchCtpTable_Object=MibTable
ochCtpTable=_OchCtpTable_Object((1,3,6,1,4,1,21296,2,2,2,2,33,1))
if mibBuilder.loadTexts:ochCtpTable.setStatus(_A)
_OchCtpEntry_Object=MibTableRow
ochCtpEntry=_OchCtpEntry_Object((1,3,6,1,4,1,21296,2,2,2,2,33,1,1))
ochCtpEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:ochCtpEntry.setStatus(_A)
_OchCtpSignalDegradeReporting_Type=InfnReporting
_OchCtpSignalDegradeReporting_Object=MibTableColumn
ochCtpSignalDegradeReporting=_OchCtpSignalDegradeReporting_Object((1,3,6,1,4,1,21296,2,2,2,2,33,1,1,1),_OchCtpSignalDegradeReporting_Type())
ochCtpSignalDegradeReporting.setMaxAccess(_C)
if mibBuilder.loadTexts:ochCtpSignalDegradeReporting.setStatus(_A)
class _OchCtpPmHistStatsEnable_Type(InfnPmHistStatsControl):defaultValue=1
_OchCtpPmHistStatsEnable_Type.__name__=_G
_OchCtpPmHistStatsEnable_Object=MibTableColumn
ochCtpPmHistStatsEnable=_OchCtpPmHistStatsEnable_Object((1,3,6,1,4,1,21296,2,2,2,2,33,1,1,2),_OchCtpPmHistStatsEnable_Type())
ochCtpPmHistStatsEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:ochCtpPmHistStatsEnable.setStatus(_A)
_OchCtpCarrierGroupMode_Type=InfnCarrierType
_OchCtpCarrierGroupMode_Object=MibTableColumn
ochCtpCarrierGroupMode=_OchCtpCarrierGroupMode_Object((1,3,6,1,4,1,21296,2,2,2,2,33,1,1,3),_OchCtpCarrierGroupMode_Type())
ochCtpCarrierGroupMode.setMaxAccess(_C)
if mibBuilder.loadTexts:ochCtpCarrierGroupMode.setStatus(_A)
_OchCtpModulation_Type=InfnModulation
_OchCtpModulation_Object=MibTableColumn
ochCtpModulation=_OchCtpModulation_Object((1,3,6,1,4,1,21296,2,2,2,2,33,1,1,4),_OchCtpModulation_Type())
ochCtpModulation.setMaxAccess(_C)
if mibBuilder.loadTexts:ochCtpModulation.setStatus(_A)
_OchCtpRate_Type=Integer32
_OchCtpRate_Object=MibTableColumn
ochCtpRate=_OchCtpRate_Object((1,3,6,1,4,1,21296,2,2,2,2,33,1,1,5),_OchCtpRate_Type())
ochCtpRate.setMaxAccess(_D)
if mibBuilder.loadTexts:ochCtpRate.setStatus(_A)
_OchCtpDataUsageState_Type=InfnUsageState
_OchCtpDataUsageState_Object=MibTableColumn
ochCtpDataUsageState=_OchCtpDataUsageState_Object((1,3,6,1,4,1,21296,2,2,2,2,33,1,1,6),_OchCtpDataUsageState_Type())
ochCtpDataUsageState.setMaxAccess(_D)
if mibBuilder.loadTexts:ochCtpDataUsageState.setStatus(_A)
_OchCtpCDCompMode_Type=InfnCDCompType
_OchCtpCDCompMode_Object=MibTableColumn
ochCtpCDCompMode=_OchCtpCDCompMode_Object((1,3,6,1,4,1,21296,2,2,2,2,33,1,1,7),_OchCtpCDCompMode_Type())
ochCtpCDCompMode.setMaxAccess(_C)
if mibBuilder.loadTexts:ochCtpCDCompMode.setStatus(_A)
_OchCtpChromaticDispersionSet_Type=FloatTenths
_OchCtpChromaticDispersionSet_Object=MibTableColumn
ochCtpChromaticDispersionSet=_OchCtpChromaticDispersionSet_Object((1,3,6,1,4,1,21296,2,2,2,2,33,1,1,8),_OchCtpChromaticDispersionSet_Type())
ochCtpChromaticDispersionSet.setMaxAccess(_C)
if mibBuilder.loadTexts:ochCtpChromaticDispersionSet.setStatus(_A)
_OchCtpFFCRMode_Type=InfnFFCRMode
_OchCtpFFCRMode_Object=MibTableColumn
ochCtpFFCRMode=_OchCtpFFCRMode_Object((1,3,6,1,4,1,21296,2,2,2,2,33,1,1,9),_OchCtpFFCRMode_Type())
ochCtpFFCRMode.setMaxAccess(_C)
if mibBuilder.loadTexts:ochCtpFFCRMode.setStatus(_A)
_OchCtpFFCRBlockSize_Type=FloatTenths
_OchCtpFFCRBlockSize_Object=MibTableColumn
ochCtpFFCRBlockSize=_OchCtpFFCRBlockSize_Object((1,3,6,1,4,1,21296,2,2,2,2,33,1,1,10),_OchCtpFFCRBlockSize_Type())
ochCtpFFCRBlockSize.setMaxAccess(_C)
if mibBuilder.loadTexts:ochCtpFFCRBlockSize.setStatus(_A)
_OchCtpFFCRXYAveraging_Type=Integer32
_OchCtpFFCRXYAveraging_Object=MibTableColumn
ochCtpFFCRXYAveraging=_OchCtpFFCRXYAveraging_Object((1,3,6,1,4,1,21296,2,2,2,2,33,1,1,11),_OchCtpFFCRXYAveraging_Type())
ochCtpFFCRXYAveraging.setMaxAccess(_C)
if mibBuilder.loadTexts:ochCtpFFCRXYAveraging.setStatus(_A)
_OchCtpLaneShuffling_Type=InfnEnableDisable
_OchCtpLaneShuffling_Object=MibTableColumn
ochCtpLaneShuffling=_OchCtpLaneShuffling_Object((1,3,6,1,4,1,21296,2,2,2,2,33,1,1,12),_OchCtpLaneShuffling_Type())
ochCtpLaneShuffling.setMaxAccess(_C)
if mibBuilder.loadTexts:ochCtpLaneShuffling.setStatus(_A)
_OchCtpTxDisableActionOnAdminLock_Type=InfnTxDisableActionOnAdminLock
_OchCtpTxDisableActionOnAdminLock_Object=MibTableColumn
ochCtpTxDisableActionOnAdminLock=_OchCtpTxDisableActionOnAdminLock_Object((1,3,6,1,4,1,21296,2,2,2,2,33,1,1,13),_OchCtpTxDisableActionOnAdminLock_Type())
ochCtpTxDisableActionOnAdminLock.setMaxAccess(_C)
if mibBuilder.loadTexts:ochCtpTxDisableActionOnAdminLock.setStatus(_A)
_OchCtpTxShutdown_Type=TruthValue
_OchCtpTxShutdown_Object=MibTableColumn
ochCtpTxShutdown=_OchCtpTxShutdown_Object((1,3,6,1,4,1,21296,2,2,2,2,33,1,1,14),_OchCtpTxShutdown_Type())
ochCtpTxShutdown.setMaxAccess(_D)
if mibBuilder.loadTexts:ochCtpTxShutdown.setStatus(_A)
_OchCtpEncodingMode_Type=InfnEncoding
_OchCtpEncodingMode_Object=MibTableColumn
ochCtpEncodingMode=_OchCtpEncodingMode_Object((1,3,6,1,4,1,21296,2,2,2,2,33,1,1,15),_OchCtpEncodingMode_Type())
ochCtpEncodingMode.setMaxAccess(_D)
if mibBuilder.loadTexts:ochCtpEncodingMode.setStatus(_A)
_OchCtpTxXYAlignment_Type=InfnXYAlignment
_OchCtpTxXYAlignment_Object=MibTableColumn
ochCtpTxXYAlignment=_OchCtpTxXYAlignment_Object((1,3,6,1,4,1,21296,2,2,2,2,33,1,1,16),_OchCtpTxXYAlignment_Type())
ochCtpTxXYAlignment.setMaxAccess(_C)
if mibBuilder.loadTexts:ochCtpTxXYAlignment.setStatus(_A)
_OchCtpPmdHighThreshold_Type=FloatTenths
_OchCtpPmdHighThreshold_Object=MibTableColumn
ochCtpPmdHighThreshold=_OchCtpPmdHighThreshold_Object((1,3,6,1,4,1,21296,2,2,2,2,33,1,1,17),_OchCtpPmdHighThreshold_Type())
ochCtpPmdHighThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:ochCtpPmdHighThreshold.setStatus(_A)
_OchCtpPmdHighTCAReporting_Type=InfnEnableDisable
_OchCtpPmdHighTCAReporting_Object=MibTableColumn
ochCtpPmdHighTCAReporting=_OchCtpPmdHighTCAReporting_Object((1,3,6,1,4,1,21296,2,2,2,2,33,1,1,18),_OchCtpPmdHighTCAReporting_Type())
ochCtpPmdHighTCAReporting.setMaxAccess(_C)
if mibBuilder.loadTexts:ochCtpPmdHighTCAReporting.setStatus(_A)
_OchCtpPreFecQSigDegThreshold_Type=FloatTenths
_OchCtpPreFecQSigDegThreshold_Object=MibTableColumn
ochCtpPreFecQSigDegThreshold=_OchCtpPreFecQSigDegThreshold_Object((1,3,6,1,4,1,21296,2,2,2,2,33,1,1,19),_OchCtpPreFecQSigDegThreshold_Type())
ochCtpPreFecQSigDegThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:ochCtpPreFecQSigDegThreshold.setStatus(_A)
_OchCtpPreFecQSigDegHysteresis_Type=FloatTenths
_OchCtpPreFecQSigDegHysteresis_Object=MibTableColumn
ochCtpPreFecQSigDegHysteresis=_OchCtpPreFecQSigDegHysteresis_Object((1,3,6,1,4,1,21296,2,2,2,2,33,1,1,20),_OchCtpPreFecQSigDegHysteresis_Type())
ochCtpPreFecQSigDegHysteresis.setMaxAccess(_C)
if mibBuilder.loadTexts:ochCtpPreFecQSigDegHysteresis.setStatus(_A)
_OchCtpPreFecQSigDegTCAReporting_Type=InfnEnableDisable
_OchCtpPreFecQSigDegTCAReporting_Object=MibTableColumn
ochCtpPreFecQSigDegTCAReporting=_OchCtpPreFecQSigDegTCAReporting_Object((1,3,6,1,4,1,21296,2,2,2,2,33,1,1,21),_OchCtpPreFecQSigDegTCAReporting_Type())
ochCtpPreFecQSigDegTCAReporting.setMaxAccess(_C)
if mibBuilder.loadTexts:ochCtpPreFecQSigDegTCAReporting.setStatus(_A)
_OchCtpPreFecBERSigDegThreshold_Type=FloatTenths
_OchCtpPreFecBERSigDegThreshold_Object=MibTableColumn
ochCtpPreFecBERSigDegThreshold=_OchCtpPreFecBERSigDegThreshold_Object((1,3,6,1,4,1,21296,2,2,2,2,33,1,1,22),_OchCtpPreFecBERSigDegThreshold_Type())
ochCtpPreFecBERSigDegThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:ochCtpPreFecBERSigDegThreshold.setStatus(_A)
_OchCtpPreFecBERSigDegHysteresis_Type=FloatTenths
_OchCtpPreFecBERSigDegHysteresis_Object=MibTableColumn
ochCtpPreFecBERSigDegHysteresis=_OchCtpPreFecBERSigDegHysteresis_Object((1,3,6,1,4,1,21296,2,2,2,2,33,1,1,23),_OchCtpPreFecBERSigDegHysteresis_Type())
ochCtpPreFecBERSigDegHysteresis.setMaxAccess(_D)
if mibBuilder.loadTexts:ochCtpPreFecBERSigDegHysteresis.setStatus(_A)
_OchCtpPreFecBERSigDegTCAReporting_Type=InfnEnableDisable
_OchCtpPreFecBERSigDegTCAReporting_Object=MibTableColumn
ochCtpPreFecBERSigDegTCAReporting=_OchCtpPreFecBERSigDegTCAReporting_Object((1,3,6,1,4,1,21296,2,2,2,2,33,1,1,24),_OchCtpPreFecBERSigDegTCAReporting_Type())
ochCtpPreFecBERSigDegTCAReporting.setMaxAccess(_D)
if mibBuilder.loadTexts:ochCtpPreFecBERSigDegTCAReporting.setStatus(_A)
_OchCtpSupportingCarrierList_Type=DisplayString
_OchCtpSupportingCarrierList_Object=MibTableColumn
ochCtpSupportingCarrierList=_OchCtpSupportingCarrierList_Object((1,3,6,1,4,1,21296,2,2,2,2,33,1,1,25),_OchCtpSupportingCarrierList_Type())
ochCtpSupportingCarrierList.setMaxAccess(_D)
if mibBuilder.loadTexts:ochCtpSupportingCarrierList.setStatus(_A)
_OchCtpChromaticDispersionRange_Type=InfnCDRange
_OchCtpChromaticDispersionRange_Object=MibTableColumn
ochCtpChromaticDispersionRange=_OchCtpChromaticDispersionRange_Object((1,3,6,1,4,1,21296,2,2,2,2,33,1,1,26),_OchCtpChromaticDispersionRange_Type())
ochCtpChromaticDispersionRange.setMaxAccess(_C)
if mibBuilder.loadTexts:ochCtpChromaticDispersionRange.setStatus(_A)
_OchCtpFineGranularPreFecQ_Type=InfnEnableDisable
_OchCtpFineGranularPreFecQ_Object=MibTableColumn
ochCtpFineGranularPreFecQ=_OchCtpFineGranularPreFecQ_Object((1,3,6,1,4,1,21296,2,2,2,2,33,1,1,27),_OchCtpFineGranularPreFecQ_Type())
ochCtpFineGranularPreFecQ.setMaxAccess(_D)
if mibBuilder.loadTexts:ochCtpFineGranularPreFecQ.setStatus(_A)
_OchCtpFineGranularPreFecQSampling_Type=Integer32
_OchCtpFineGranularPreFecQSampling_Object=MibTableColumn
ochCtpFineGranularPreFecQSampling=_OchCtpFineGranularPreFecQSampling_Object((1,3,6,1,4,1,21296,2,2,2,2,33,1,1,28),_OchCtpFineGranularPreFecQSampling_Type())
ochCtpFineGranularPreFecQSampling.setMaxAccess(_D)
if mibBuilder.loadTexts:ochCtpFineGranularPreFecQSampling.setStatus(_A)
_OchCtpRapidRecovery_Type=InfnEnableDisable
_OchCtpRapidRecovery_Object=MibTableColumn
ochCtpRapidRecovery=_OchCtpRapidRecovery_Object((1,3,6,1,4,1,21296,2,2,2,2,33,1,1,29),_OchCtpRapidRecovery_Type())
ochCtpRapidRecovery.setMaxAccess(_C)
if mibBuilder.loadTexts:ochCtpRapidRecovery.setStatus(_A)
_OchCtpAggresivePolarizationTracking_Type=InfnEnableDisable
_OchCtpAggresivePolarizationTracking_Object=MibTableColumn
ochCtpAggresivePolarizationTracking=_OchCtpAggresivePolarizationTracking_Object((1,3,6,1,4,1,21296,2,2,2,2,33,1,1,30),_OchCtpAggresivePolarizationTracking_Type())
ochCtpAggresivePolarizationTracking.setMaxAccess(_C)
if mibBuilder.loadTexts:ochCtpAggresivePolarizationTracking.setStatus(_A)
_OchCtpBwResilientSsLoopControl_Type=InfnEnableDisable
_OchCtpBwResilientSsLoopControl_Object=MibTableColumn
ochCtpBwResilientSsLoopControl=_OchCtpBwResilientSsLoopControl_Object((1,3,6,1,4,1,21296,2,2,2,2,33,1,1,31),_OchCtpBwResilientSsLoopControl_Type())
ochCtpBwResilientSsLoopControl.setMaxAccess(_C)
if mibBuilder.loadTexts:ochCtpBwResilientSsLoopControl.setStatus(_A)
_OchCtpBwResilientCtLoopControl_Type=InfnEnableDisable
_OchCtpBwResilientCtLoopControl_Object=MibTableColumn
ochCtpBwResilientCtLoopControl=_OchCtpBwResilientCtLoopControl_Object((1,3,6,1,4,1,21296,2,2,2,2,33,1,1,32),_OchCtpBwResilientCtLoopControl_Type())
ochCtpBwResilientCtLoopControl.setMaxAccess(_C)
if mibBuilder.loadTexts:ochCtpBwResilientCtLoopControl.setStatus(_A)
_OchCtpConformance_ObjectIdentity=ObjectIdentity
ochCtpConformance=_OchCtpConformance_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,2,33,3))
_OchCtpCompliances_ObjectIdentity=ObjectIdentity
ochCtpCompliances=_OchCtpCompliances_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,2,33,3,1))
_OchCtpGroups_ObjectIdentity=ObjectIdentity
ochCtpGroups=_OchCtpGroups_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,2,33,3,2))
ochCtpGroup=ObjectGroup((1,3,6,1,4,1,21296,2,2,2,2,33,3,2,1))
ochCtpGroup.setObjects(*((_B,_H),(_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m)))
if mibBuilder.loadTexts:ochCtpGroup.setStatus(_A)
ochCtpCompliance=ModuleCompliance((1,3,6,1,4,1,21296,2,2,2,2,33,3,1,1))
ochCtpCompliance.setObjects((_B,_n))
if mibBuilder.loadTexts:ochCtpCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ochCtpMIB':ochCtpMIB,'ochCtpTable':ochCtpTable,'ochCtpEntry':ochCtpEntry,_H:ochCtpSignalDegradeReporting,_I:ochCtpPmHistStatsEnable,_J:ochCtpCarrierGroupMode,_K:ochCtpModulation,_L:ochCtpRate,_M:ochCtpDataUsageState,_N:ochCtpCDCompMode,_O:ochCtpChromaticDispersionSet,_P:ochCtpFFCRMode,_Q:ochCtpFFCRBlockSize,_R:ochCtpFFCRXYAveraging,_S:ochCtpLaneShuffling,_T:ochCtpTxDisableActionOnAdminLock,_U:ochCtpTxShutdown,_V:ochCtpEncodingMode,_W:ochCtpTxXYAlignment,_X:ochCtpPmdHighThreshold,_Y:ochCtpPmdHighTCAReporting,_Z:ochCtpPreFecQSigDegThreshold,_a:ochCtpPreFecQSigDegHysteresis,_b:ochCtpPreFecQSigDegTCAReporting,_c:ochCtpPreFecBERSigDegThreshold,_d:ochCtpPreFecBERSigDegHysteresis,_e:ochCtpPreFecBERSigDegTCAReporting,_f:ochCtpSupportingCarrierList,_g:ochCtpChromaticDispersionRange,_h:ochCtpFineGranularPreFecQ,_i:ochCtpFineGranularPreFecQSampling,_j:ochCtpRapidRecovery,_k:ochCtpAggresivePolarizationTracking,_l:ochCtpBwResilientSsLoopControl,_m:ochCtpBwResilientCtLoopControl,'ochCtpConformance':ochCtpConformance,'ochCtpCompliances':ochCtpCompliances,'ochCtpCompliance':ochCtpCompliance,'ochCtpGroups':ochCtpGroups,_n:ochCtpGroup})