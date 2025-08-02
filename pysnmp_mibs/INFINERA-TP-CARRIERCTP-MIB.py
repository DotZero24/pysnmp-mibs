_w='carrierCtpGroup'
_v='carrierCtpNLCStatus'
_u='carrierCtpNLCSetting'
_t='carrierCtpClockMode'
_s='carrierCtpInstCDSet'
_r='carrierCtpProvLatency'
_q='carrierCtpBwResilientCtLoopControl'
_p='carrierCtpBwResilientSsLoopControl'
_o='carrierCtpTuningStatus'
_n='carrierCtpOpticalSignal'
_m='carrierCtpLatency'
_l='carrierCtpProvTxCD'
_k='carrierCtpTxCD'
_j='carrierCtpFecIterations'
_i='carrierCtpProvFecIterations'
_h='carrierCtpGainSharing'
_g='carrierCtpProvGainSharing'
_f='carrierCtpBaudRate'
_e='carrierCtpFFCRAveraging'
_d='carrierCtpFrequency'
_c='carrierCtpAggresivePolarizationTracking'
_b='carrierCtpRapidRecovery'
_a='carrierCtpFineGranularPreFecQSampling'
_Z='carrierCtpFineGranularPreFecQ'
_Y='carrierCtpCDSet'
_X='carrierCtpFFCRXYAveraging'
_W='carrierCtpPreFecBERSigDegHysteresis'
_V='carrierCtpPreFecQSigDegHysteresis'
_U='carrierCtpPreFecQSigDegTh'
_T='carrierCtpPreFecBerSigDegTh'
_S='carrierCtpPreFecQSigDegTcaRept'
_R='carrierCtpPreFecBerSigDegTcaRept'
_Q='carrierCtpFFCRBlockSize'
_P='carrierCtpFFCRMode'
_O='carrierCtpCDRange'
_N='carrierCtpCDCompMode'
_M='carrierCtpPMDHighTCAReporting'
_L='carrierCtpPMDHighThreshold'
_K='carrierCtpEncodingMode'
_J='carrierCtpCarrierRate'
_I='carrierCtpModulation'
_H='carrierCtpPmHistStatsEnable'
_G='ifIndex'
_F='IF-MIB'
_E='Integer32'
_D='read-only'
_C='read-write'
_B='INFINERA-TP-CARRIERCTP-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_F,_G)
terminationPoint,=mibBuilder.importSymbols('INFINERA-REG-MIB','terminationPoint')
FloatArbitraryPrecision,FloatHundredths,FloatTenths,InfnCDCompType,InfnCDRange,InfnCarrierType,InfnEnableDisable,InfnEnableDisableType,InfnEncoding,InfnEqptType,InfnFFCRAveraging,InfnFFCRMode,InfnLatencyMode,InfnOperationalState,InfnOpticalSignal,InfnProvBaudRate,InfnTuningStatus=mibBuilder.importSymbols('INFINERA-TC-MIB','FloatArbitraryPrecision','FloatHundredths','FloatTenths','InfnCDCompType','InfnCDRange','InfnCarrierType','InfnEnableDisable','InfnEnableDisableType','InfnEncoding','InfnEqptType','InfnFFCRAveraging','InfnFFCRMode','InfnLatencyMode','InfnOperationalState','InfnOpticalSignal','InfnProvBaudRate','InfnTuningStatus')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
carrierCtpMIB=ModuleIdentity((1,3,6,1,4,1,21296,2,2,2,2,38))
_CarrierCtpTable_Object=MibTable
carrierCtpTable=_CarrierCtpTable_Object((1,3,6,1,4,1,21296,2,2,2,2,38,1))
if mibBuilder.loadTexts:carrierCtpTable.setStatus(_A)
_CarrierCtpEntry_Object=MibTableRow
carrierCtpEntry=_CarrierCtpEntry_Object((1,3,6,1,4,1,21296,2,2,2,2,38,1,1))
carrierCtpEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:carrierCtpEntry.setStatus(_A)
class _CarrierCtpPmHistStatsEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),('disabled',2)))
_CarrierCtpPmHistStatsEnable_Type.__name__=_E
_CarrierCtpPmHistStatsEnable_Object=MibTableColumn
carrierCtpPmHistStatsEnable=_CarrierCtpPmHistStatsEnable_Object((1,3,6,1,4,1,21296,2,2,2,2,38,1,1,1),_CarrierCtpPmHistStatsEnable_Type())
carrierCtpPmHistStatsEnable.setMaxAccess('read-create')
if mibBuilder.loadTexts:carrierCtpPmHistStatsEnable.setStatus(_A)
class _CarrierCtpModulation_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,101)));namedValues=NamedValues(*(('pmQPSK',1),('pmBPSK',2),('pmEnhancedBPSK',3),('pm3QAM',4),('pm8QAM',5),('pm16QAM',6),('pmNONE',101)))
_CarrierCtpModulation_Type.__name__=_E
_CarrierCtpModulation_Object=MibTableColumn
carrierCtpModulation=_CarrierCtpModulation_Object((1,3,6,1,4,1,21296,2,2,2,2,38,1,1,2),_CarrierCtpModulation_Type())
carrierCtpModulation.setMaxAccess(_D)
if mibBuilder.loadTexts:carrierCtpModulation.setStatus(_A)
_CarrierCtpCarrierRate_Type=FloatTenths
_CarrierCtpCarrierRate_Object=MibTableColumn
carrierCtpCarrierRate=_CarrierCtpCarrierRate_Object((1,3,6,1,4,1,21296,2,2,2,2,38,1,1,3),_CarrierCtpCarrierRate_Type())
carrierCtpCarrierRate.setMaxAccess(_D)
if mibBuilder.loadTexts:carrierCtpCarrierRate.setStatus(_A)
_CarrierCtpEncodingMode_Type=InfnEncoding
_CarrierCtpEncodingMode_Object=MibTableColumn
carrierCtpEncodingMode=_CarrierCtpEncodingMode_Object((1,3,6,1,4,1,21296,2,2,2,2,38,1,1,4),_CarrierCtpEncodingMode_Type())
carrierCtpEncodingMode.setMaxAccess(_D)
if mibBuilder.loadTexts:carrierCtpEncodingMode.setStatus(_A)
_CarrierCtpPMDHighThreshold_Type=FloatTenths
_CarrierCtpPMDHighThreshold_Object=MibTableColumn
carrierCtpPMDHighThreshold=_CarrierCtpPMDHighThreshold_Object((1,3,6,1,4,1,21296,2,2,2,2,38,1,1,5),_CarrierCtpPMDHighThreshold_Type())
carrierCtpPMDHighThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:carrierCtpPMDHighThreshold.setStatus(_A)
_CarrierCtpPMDHighTCAReporting_Type=InfnEnableDisable
_CarrierCtpPMDHighTCAReporting_Object=MibTableColumn
carrierCtpPMDHighTCAReporting=_CarrierCtpPMDHighTCAReporting_Object((1,3,6,1,4,1,21296,2,2,2,2,38,1,1,6),_CarrierCtpPMDHighTCAReporting_Type())
carrierCtpPMDHighTCAReporting.setMaxAccess(_C)
if mibBuilder.loadTexts:carrierCtpPMDHighTCAReporting.setStatus(_A)
_CarrierCtpCDCompMode_Type=InfnCDCompType
_CarrierCtpCDCompMode_Object=MibTableColumn
carrierCtpCDCompMode=_CarrierCtpCDCompMode_Object((1,3,6,1,4,1,21296,2,2,2,2,38,1,1,7),_CarrierCtpCDCompMode_Type())
carrierCtpCDCompMode.setMaxAccess(_C)
if mibBuilder.loadTexts:carrierCtpCDCompMode.setStatus(_A)
_CarrierCtpCDSet_Type=Integer32
_CarrierCtpCDSet_Object=MibTableColumn
carrierCtpCDSet=_CarrierCtpCDSet_Object((1,3,6,1,4,1,21296,2,2,2,2,38,1,1,8),_CarrierCtpCDSet_Type())
carrierCtpCDSet.setMaxAccess(_C)
if mibBuilder.loadTexts:carrierCtpCDSet.setStatus(_A)
_CarrierCtpCDRange_Type=InfnCDRange
_CarrierCtpCDRange_Object=MibTableColumn
carrierCtpCDRange=_CarrierCtpCDRange_Object((1,3,6,1,4,1,21296,2,2,2,2,38,1,1,9),_CarrierCtpCDRange_Type())
carrierCtpCDRange.setMaxAccess(_C)
if mibBuilder.loadTexts:carrierCtpCDRange.setStatus(_A)
_CarrierCtpFFCRMode_Type=InfnFFCRMode
_CarrierCtpFFCRMode_Object=MibTableColumn
carrierCtpFFCRMode=_CarrierCtpFFCRMode_Object((1,3,6,1,4,1,21296,2,2,2,2,38,1,1,10),_CarrierCtpFFCRMode_Type())
carrierCtpFFCRMode.setMaxAccess(_C)
if mibBuilder.loadTexts:carrierCtpFFCRMode.setStatus(_A)
_CarrierCtpFFCRBlockSize_Type=FloatTenths
_CarrierCtpFFCRBlockSize_Object=MibTableColumn
carrierCtpFFCRBlockSize=_CarrierCtpFFCRBlockSize_Object((1,3,6,1,4,1,21296,2,2,2,2,38,1,1,11),_CarrierCtpFFCRBlockSize_Type())
carrierCtpFFCRBlockSize.setMaxAccess(_C)
if mibBuilder.loadTexts:carrierCtpFFCRBlockSize.setStatus(_A)
_CarrierCtpFFCRXYAveraging_Type=Integer32
_CarrierCtpFFCRXYAveraging_Object=MibTableColumn
carrierCtpFFCRXYAveraging=_CarrierCtpFFCRXYAveraging_Object((1,3,6,1,4,1,21296,2,2,2,2,38,1,1,12),_CarrierCtpFFCRXYAveraging_Type())
carrierCtpFFCRXYAveraging.setMaxAccess(_D)
if mibBuilder.loadTexts:carrierCtpFFCRXYAveraging.setStatus(_A)
_CarrierCtpPreFecBerSigDegTcaRept_Type=InfnEnableDisable
_CarrierCtpPreFecBerSigDegTcaRept_Object=MibTableColumn
carrierCtpPreFecBerSigDegTcaRept=_CarrierCtpPreFecBerSigDegTcaRept_Object((1,3,6,1,4,1,21296,2,2,2,2,38,1,1,13),_CarrierCtpPreFecBerSigDegTcaRept_Type())
carrierCtpPreFecBerSigDegTcaRept.setMaxAccess(_C)
if mibBuilder.loadTexts:carrierCtpPreFecBerSigDegTcaRept.setStatus(_A)
_CarrierCtpPreFecQSigDegTcaRept_Type=InfnEnableDisable
_CarrierCtpPreFecQSigDegTcaRept_Object=MibTableColumn
carrierCtpPreFecQSigDegTcaRept=_CarrierCtpPreFecQSigDegTcaRept_Object((1,3,6,1,4,1,21296,2,2,2,2,38,1,1,14),_CarrierCtpPreFecQSigDegTcaRept_Type())
carrierCtpPreFecQSigDegTcaRept.setMaxAccess(_C)
if mibBuilder.loadTexts:carrierCtpPreFecQSigDegTcaRept.setStatus(_A)
_CarrierCtpPreFecBerSigDegTh_Type=FloatArbitraryPrecision
_CarrierCtpPreFecBerSigDegTh_Object=MibTableColumn
carrierCtpPreFecBerSigDegTh=_CarrierCtpPreFecBerSigDegTh_Object((1,3,6,1,4,1,21296,2,2,2,2,38,1,1,15),_CarrierCtpPreFecBerSigDegTh_Type())
carrierCtpPreFecBerSigDegTh.setMaxAccess(_D)
if mibBuilder.loadTexts:carrierCtpPreFecBerSigDegTh.setStatus(_A)
_CarrierCtpPreFecQSigDegTh_Type=FloatArbitraryPrecision
_CarrierCtpPreFecQSigDegTh_Object=MibTableColumn
carrierCtpPreFecQSigDegTh=_CarrierCtpPreFecQSigDegTh_Object((1,3,6,1,4,1,21296,2,2,2,2,38,1,1,16),_CarrierCtpPreFecQSigDegTh_Type())
carrierCtpPreFecQSigDegTh.setMaxAccess(_C)
if mibBuilder.loadTexts:carrierCtpPreFecQSigDegTh.setStatus(_A)
_CarrierCtpPreFecQSigDegHysteresis_Type=FloatTenths
_CarrierCtpPreFecQSigDegHysteresis_Object=MibTableColumn
carrierCtpPreFecQSigDegHysteresis=_CarrierCtpPreFecQSigDegHysteresis_Object((1,3,6,1,4,1,21296,2,2,2,2,38,1,1,17),_CarrierCtpPreFecQSigDegHysteresis_Type())
carrierCtpPreFecQSigDegHysteresis.setMaxAccess(_C)
if mibBuilder.loadTexts:carrierCtpPreFecQSigDegHysteresis.setStatus(_A)
_CarrierCtpPreFecBERSigDegHysteresis_Type=FloatTenths
_CarrierCtpPreFecBERSigDegHysteresis_Object=MibTableColumn
carrierCtpPreFecBERSigDegHysteresis=_CarrierCtpPreFecBERSigDegHysteresis_Object((1,3,6,1,4,1,21296,2,2,2,2,38,1,1,18),_CarrierCtpPreFecBERSigDegHysteresis_Type())
carrierCtpPreFecBERSigDegHysteresis.setMaxAccess(_D)
if mibBuilder.loadTexts:carrierCtpPreFecBERSigDegHysteresis.setStatus(_A)
_CarrierCtpFineGranularPreFecQ_Type=InfnEnableDisable
_CarrierCtpFineGranularPreFecQ_Object=MibTableColumn
carrierCtpFineGranularPreFecQ=_CarrierCtpFineGranularPreFecQ_Object((1,3,6,1,4,1,21296,2,2,2,2,38,1,1,19),_CarrierCtpFineGranularPreFecQ_Type())
carrierCtpFineGranularPreFecQ.setMaxAccess(_C)
if mibBuilder.loadTexts:carrierCtpFineGranularPreFecQ.setStatus(_A)
_CarrierCtpFineGranularPreFecQSampling_Type=Integer32
_CarrierCtpFineGranularPreFecQSampling_Object=MibTableColumn
carrierCtpFineGranularPreFecQSampling=_CarrierCtpFineGranularPreFecQSampling_Object((1,3,6,1,4,1,21296,2,2,2,2,38,1,1,20),_CarrierCtpFineGranularPreFecQSampling_Type())
carrierCtpFineGranularPreFecQSampling.setMaxAccess(_D)
if mibBuilder.loadTexts:carrierCtpFineGranularPreFecQSampling.setStatus(_A)
_CarrierCtpRapidRecovery_Type=InfnEnableDisable
_CarrierCtpRapidRecovery_Object=MibTableColumn
carrierCtpRapidRecovery=_CarrierCtpRapidRecovery_Object((1,3,6,1,4,1,21296,2,2,2,2,38,1,1,21),_CarrierCtpRapidRecovery_Type())
carrierCtpRapidRecovery.setMaxAccess(_C)
if mibBuilder.loadTexts:carrierCtpRapidRecovery.setStatus(_A)
_CarrierCtpAggresivePolarizationTracking_Type=InfnEnableDisable
_CarrierCtpAggresivePolarizationTracking_Object=MibTableColumn
carrierCtpAggresivePolarizationTracking=_CarrierCtpAggresivePolarizationTracking_Object((1,3,6,1,4,1,21296,2,2,2,2,38,1,1,22),_CarrierCtpAggresivePolarizationTracking_Type())
carrierCtpAggresivePolarizationTracking.setMaxAccess(_C)
if mibBuilder.loadTexts:carrierCtpAggresivePolarizationTracking.setStatus(_A)
_CarrierCtpFrequency_Type=DisplayString
_CarrierCtpFrequency_Object=MibTableColumn
carrierCtpFrequency=_CarrierCtpFrequency_Object((1,3,6,1,4,1,21296,2,2,2,2,38,1,1,23),_CarrierCtpFrequency_Type())
carrierCtpFrequency.setMaxAccess(_D)
if mibBuilder.loadTexts:carrierCtpFrequency.setStatus(_A)
_CarrierCtpFFCRAveraging_Type=InfnFFCRAveraging
_CarrierCtpFFCRAveraging_Object=MibTableColumn
carrierCtpFFCRAveraging=_CarrierCtpFFCRAveraging_Object((1,3,6,1,4,1,21296,2,2,2,2,38,1,1,24),_CarrierCtpFFCRAveraging_Type())
carrierCtpFFCRAveraging.setMaxAccess(_C)
if mibBuilder.loadTexts:carrierCtpFFCRAveraging.setStatus(_A)
_CarrierCtpBaudRate_Type=InfnProvBaudRate
_CarrierCtpBaudRate_Object=MibTableColumn
carrierCtpBaudRate=_CarrierCtpBaudRate_Object((1,3,6,1,4,1,21296,2,2,2,2,38,1,1,25),_CarrierCtpBaudRate_Type())
carrierCtpBaudRate.setMaxAccess(_D)
if mibBuilder.loadTexts:carrierCtpBaudRate.setStatus(_A)
_CarrierCtpProvGainSharing_Type=InfnOperationalState
_CarrierCtpProvGainSharing_Object=MibTableColumn
carrierCtpProvGainSharing=_CarrierCtpProvGainSharing_Object((1,3,6,1,4,1,21296,2,2,2,2,38,1,1,26),_CarrierCtpProvGainSharing_Type())
carrierCtpProvGainSharing.setMaxAccess(_C)
if mibBuilder.loadTexts:carrierCtpProvGainSharing.setStatus(_A)
_CarrierCtpGainSharing_Type=InfnOperationalState
_CarrierCtpGainSharing_Object=MibTableColumn
carrierCtpGainSharing=_CarrierCtpGainSharing_Object((1,3,6,1,4,1,21296,2,2,2,2,38,1,1,27),_CarrierCtpGainSharing_Type())
carrierCtpGainSharing.setMaxAccess(_D)
if mibBuilder.loadTexts:carrierCtpGainSharing.setStatus(_A)
_CarrierCtpProvFecIterations_Type=Integer32
_CarrierCtpProvFecIterations_Object=MibTableColumn
carrierCtpProvFecIterations=_CarrierCtpProvFecIterations_Object((1,3,6,1,4,1,21296,2,2,2,2,38,1,1,28),_CarrierCtpProvFecIterations_Type())
carrierCtpProvFecIterations.setMaxAccess(_C)
if mibBuilder.loadTexts:carrierCtpProvFecIterations.setStatus(_A)
_CarrierCtpFecIterations_Type=Integer32
_CarrierCtpFecIterations_Object=MibTableColumn
carrierCtpFecIterations=_CarrierCtpFecIterations_Object((1,3,6,1,4,1,21296,2,2,2,2,38,1,1,29),_CarrierCtpFecIterations_Type())
carrierCtpFecIterations.setMaxAccess(_D)
if mibBuilder.loadTexts:carrierCtpFecIterations.setStatus(_A)
_CarrierCtpTxCD_Type=Integer32
_CarrierCtpTxCD_Object=MibTableColumn
carrierCtpTxCD=_CarrierCtpTxCD_Object((1,3,6,1,4,1,21296,2,2,2,2,38,1,1,30),_CarrierCtpTxCD_Type())
carrierCtpTxCD.setMaxAccess(_D)
if mibBuilder.loadTexts:carrierCtpTxCD.setStatus(_A)
_CarrierCtpProvTxCD_Type=Integer32
_CarrierCtpProvTxCD_Object=MibTableColumn
carrierCtpProvTxCD=_CarrierCtpProvTxCD_Object((1,3,6,1,4,1,21296,2,2,2,2,38,1,1,31),_CarrierCtpProvTxCD_Type())
carrierCtpProvTxCD.setMaxAccess(_C)
if mibBuilder.loadTexts:carrierCtpProvTxCD.setStatus(_A)
_CarrierCtpLatency_Type=InfnLatencyMode
_CarrierCtpLatency_Object=MibTableColumn
carrierCtpLatency=_CarrierCtpLatency_Object((1,3,6,1,4,1,21296,2,2,2,2,38,1,1,32),_CarrierCtpLatency_Type())
carrierCtpLatency.setMaxAccess(_D)
if mibBuilder.loadTexts:carrierCtpLatency.setStatus(_A)
_CarrierCtpOpticalSignal_Type=InfnOpticalSignal
_CarrierCtpOpticalSignal_Object=MibTableColumn
carrierCtpOpticalSignal=_CarrierCtpOpticalSignal_Object((1,3,6,1,4,1,21296,2,2,2,2,38,1,1,33),_CarrierCtpOpticalSignal_Type())
carrierCtpOpticalSignal.setMaxAccess(_C)
if mibBuilder.loadTexts:carrierCtpOpticalSignal.setStatus(_A)
_CarrierCtpTuningStatus_Type=InfnTuningStatus
_CarrierCtpTuningStatus_Object=MibTableColumn
carrierCtpTuningStatus=_CarrierCtpTuningStatus_Object((1,3,6,1,4,1,21296,2,2,2,2,38,1,1,34),_CarrierCtpTuningStatus_Type())
carrierCtpTuningStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:carrierCtpTuningStatus.setStatus(_A)
_CarrierCtpBwResilientSsLoopControl_Type=InfnEnableDisableType
_CarrierCtpBwResilientSsLoopControl_Object=MibTableColumn
carrierCtpBwResilientSsLoopControl=_CarrierCtpBwResilientSsLoopControl_Object((1,3,6,1,4,1,21296,2,2,2,2,38,1,1,35),_CarrierCtpBwResilientSsLoopControl_Type())
carrierCtpBwResilientSsLoopControl.setMaxAccess(_C)
if mibBuilder.loadTexts:carrierCtpBwResilientSsLoopControl.setStatus(_A)
_CarrierCtpBwResilientCtLoopControl_Type=InfnEnableDisableType
_CarrierCtpBwResilientCtLoopControl_Object=MibTableColumn
carrierCtpBwResilientCtLoopControl=_CarrierCtpBwResilientCtLoopControl_Object((1,3,6,1,4,1,21296,2,2,2,2,38,1,1,36),_CarrierCtpBwResilientCtLoopControl_Type())
carrierCtpBwResilientCtLoopControl.setMaxAccess(_C)
if mibBuilder.loadTexts:carrierCtpBwResilientCtLoopControl.setStatus(_A)
_CarrierCtpProvLatency_Type=InfnLatencyMode
_CarrierCtpProvLatency_Object=MibTableColumn
carrierCtpProvLatency=_CarrierCtpProvLatency_Object((1,3,6,1,4,1,21296,2,2,2,2,38,1,1,37),_CarrierCtpProvLatency_Type())
carrierCtpProvLatency.setMaxAccess(_C)
if mibBuilder.loadTexts:carrierCtpProvLatency.setStatus(_A)
_CarrierCtpInstCDSet_Type=Integer32
_CarrierCtpInstCDSet_Object=MibTableColumn
carrierCtpInstCDSet=_CarrierCtpInstCDSet_Object((1,3,6,1,4,1,21296,2,2,2,2,38,1,1,38),_CarrierCtpInstCDSet_Type())
carrierCtpInstCDSet.setMaxAccess(_D)
if mibBuilder.loadTexts:carrierCtpInstCDSet.setStatus(_A)
_CarrierCtpClockMode_Type=Unsigned32
_CarrierCtpClockMode_Object=MibTableColumn
carrierCtpClockMode=_CarrierCtpClockMode_Object((1,3,6,1,4,1,21296,2,2,2,2,38,1,1,39),_CarrierCtpClockMode_Type())
carrierCtpClockMode.setMaxAccess(_C)
if mibBuilder.loadTexts:carrierCtpClockMode.setStatus(_A)
_CarrierCtpNLCSetting_Type=Unsigned32
_CarrierCtpNLCSetting_Object=MibTableColumn
carrierCtpNLCSetting=_CarrierCtpNLCSetting_Object((1,3,6,1,4,1,21296,2,2,2,2,38,1,1,40),_CarrierCtpNLCSetting_Type())
carrierCtpNLCSetting.setMaxAccess(_C)
if mibBuilder.loadTexts:carrierCtpNLCSetting.setStatus(_A)
_CarrierCtpNLCStatus_Type=Unsigned32
_CarrierCtpNLCStatus_Object=MibTableColumn
carrierCtpNLCStatus=_CarrierCtpNLCStatus_Object((1,3,6,1,4,1,21296,2,2,2,2,38,1,1,41),_CarrierCtpNLCStatus_Type())
carrierCtpNLCStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:carrierCtpNLCStatus.setStatus(_A)
_CarrierCtpConformance_ObjectIdentity=ObjectIdentity
carrierCtpConformance=_CarrierCtpConformance_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,2,38,37))
_CarrierCtpCompliances_ObjectIdentity=ObjectIdentity
carrierCtpCompliances=_CarrierCtpCompliances_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,2,38,37,1))
_CarrierCtpGroups_ObjectIdentity=ObjectIdentity
carrierCtpGroups=_CarrierCtpGroups_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,2,38,37,2))
carrierCtpGroup=ObjectGroup((1,3,6,1,4,1,21296,2,2,2,2,38,37,2,1))
carrierCtpGroup.setObjects(*((_B,_H),(_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v)))
if mibBuilder.loadTexts:carrierCtpGroup.setStatus(_A)
carrierCtpCompliance=ModuleCompliance((1,3,6,1,4,1,21296,2,2,2,2,38,37,1,1))
carrierCtpCompliance.setObjects((_B,_w))
if mibBuilder.loadTexts:carrierCtpCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'carrierCtpMIB':carrierCtpMIB,'carrierCtpTable':carrierCtpTable,'carrierCtpEntry':carrierCtpEntry,_H:carrierCtpPmHistStatsEnable,_I:carrierCtpModulation,_J:carrierCtpCarrierRate,_K:carrierCtpEncodingMode,_L:carrierCtpPMDHighThreshold,_M:carrierCtpPMDHighTCAReporting,_N:carrierCtpCDCompMode,_Y:carrierCtpCDSet,_O:carrierCtpCDRange,_P:carrierCtpFFCRMode,_Q:carrierCtpFFCRBlockSize,_X:carrierCtpFFCRXYAveraging,_R:carrierCtpPreFecBerSigDegTcaRept,_S:carrierCtpPreFecQSigDegTcaRept,_T:carrierCtpPreFecBerSigDegTh,_U:carrierCtpPreFecQSigDegTh,_V:carrierCtpPreFecQSigDegHysteresis,_W:carrierCtpPreFecBERSigDegHysteresis,_Z:carrierCtpFineGranularPreFecQ,_a:carrierCtpFineGranularPreFecQSampling,_b:carrierCtpRapidRecovery,_c:carrierCtpAggresivePolarizationTracking,_d:carrierCtpFrequency,_e:carrierCtpFFCRAveraging,_f:carrierCtpBaudRate,_g:carrierCtpProvGainSharing,_h:carrierCtpGainSharing,_i:carrierCtpProvFecIterations,_j:carrierCtpFecIterations,_k:carrierCtpTxCD,_l:carrierCtpProvTxCD,_m:carrierCtpLatency,_n:carrierCtpOpticalSignal,_o:carrierCtpTuningStatus,_p:carrierCtpBwResilientSsLoopControl,_q:carrierCtpBwResilientCtLoopControl,_r:carrierCtpProvLatency,_s:carrierCtpInstCDSet,_t:carrierCtpClockMode,_u:carrierCtpNLCSetting,_v:carrierCtpNLCStatus,'carrierCtpConformance':carrierCtpConformance,'carrierCtpCompliances':carrierCtpCompliances,'carrierCtpCompliance':carrierCtpCompliance,'carrierCtpGroups':carrierCtpGroups,_w:carrierCtpGroup})