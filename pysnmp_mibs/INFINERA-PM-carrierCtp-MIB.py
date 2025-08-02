_A6='carrierCtpPmRealGroup'
_A5='carrierCtpPmGroup'
_A4='carrierCtpPmRealWavelength'
_A3='carrierCtpPmRealCorrectedBits'
_A2='carrierCtpPmRealUnCorrectedCodeWord'
_A1='carrierCtpPmRealCodeWord'
_A0='carrierCtpPmRealBerPostFec'
_z='carrierCtpPmRealPhaseCorrection'
_y='carrierCtpPmRealChromaticDispersion'
_x='carrierCtpPmRealSoPmd'
_w='carrierCtpPmRealPmd'
_v='carrierCtpPmRealRxLBC'
_u='carrierCtpPmRealTxLBC'
_t='carrierCtpPmRealBerPreFec'
_s='carrierCtpPmRealQPreFec'
_r='carrierCtpPmRealOpt'
_q='carrierCtpPmCorrectedBits'
_p='carrierCtpPmUnCorrectedCodeWord'
_o='carrierCtpPmCodeWord'
_n='carrierCtpPmBerPostFecAve'
_m='carrierCtpPmBerPostFecMax'
_l='carrierCtpPmBerPostFecMin'
_k='carrierCtpPmPhaseCorrectionAve'
_j='carrierCtpPmPhaseCorrectionMax'
_i='carrierCtpPmPhaseCorrectionMin'
_h='carrierCtpPmChromaticDispersionAve'
_g='carrierCtpPmChromaticDispersionMax'
_f='carrierCtpPmChromaticDispersionMin'
_e='carrierCtpPmSoPmdAve'
_d='carrierCtpPmSoPmdMax'
_c='carrierCtpPmSoPmdMin'
_b='carrierCtpPmPmdAve'
_a='carrierCtpPmPmdMax'
_Z='carrierCtpPmPmdMin'
_Y='carrierCtpPmRxLBCAve'
_X='carrierCtpPmRxLBCMax'
_W='carrierCtpPmRxLBCMin'
_V='carrierCtpPmTxLBCAve'
_U='carrierCtpPmTxLBCMax'
_T='carrierCtpPmTxLBCMin'
_S='carrierCtpPmBerPreFecAve'
_R='carrierCtpPmBerPreFecMax'
_Q='carrierCtpPmBerPreFecMin'
_P='carrierCtpPmQPreFecAve'
_O='carrierCtpPmQPreFecMax'
_N='carrierCtpPmQPreFecMin'
_M='carrierCtpPmOptAve'
_L='carrierCtpPmOptMax'
_K='carrierCtpPmOptMin'
_J='carrierCtpPmValidity'
_I='not-accessible'
_H='carrierCtpPmTimestamp'
_G='carrierCtpPmSampleDuration'
_F='Integer32'
_E='ifIndex'
_D='IF-MIB'
_C='read-only'
_B='INFINERA-PM-carrierCtp-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
HCPerfIntervalCount,=mibBuilder.importSymbols('HC-PerfHist-TC-MIB','HCPerfIntervalCount')
ifIndex,=mibBuilder.importSymbols(_D,_E)
perfMon,=mibBuilder.importSymbols('INFINERA-REG-MIB','perfMon')
FloatArbitraryPrecision,FloatHundredths=mibBuilder.importSymbols('INFINERA-TC-MIB','FloatArbitraryPrecision','FloatHundredths')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
carrierCtpPmMIB=ModuleIdentity((1,3,6,1,4,1,21296,2,2,2,3,200))
if mibBuilder.loadTexts:carrierCtpPmMIB.setRevisions(('2013-10-08 00:00',))
_CarrierCtpPmRealTable_Object=MibTable
carrierCtpPmRealTable=_CarrierCtpPmRealTable_Object((1,3,6,1,4,1,21296,2,2,2,3,200,1))
if mibBuilder.loadTexts:carrierCtpPmRealTable.setStatus(_A)
_CarrierCtpPmRealEntry_Object=MibTableRow
carrierCtpPmRealEntry=_CarrierCtpPmRealEntry_Object((1,3,6,1,4,1,21296,2,2,2,3,200,1,1))
carrierCtpPmRealEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:carrierCtpPmRealEntry.setStatus(_A)
_CarrierCtpPmRealOpt_Type=FloatHundredths
_CarrierCtpPmRealOpt_Object=MibTableColumn
carrierCtpPmRealOpt=_CarrierCtpPmRealOpt_Object((1,3,6,1,4,1,21296,2,2,2,3,200,1,1,1),_CarrierCtpPmRealOpt_Type())
carrierCtpPmRealOpt.setMaxAccess(_C)
if mibBuilder.loadTexts:carrierCtpPmRealOpt.setStatus(_A)
_CarrierCtpPmRealQPreFec_Type=FloatHundredths
_CarrierCtpPmRealQPreFec_Object=MibTableColumn
carrierCtpPmRealQPreFec=_CarrierCtpPmRealQPreFec_Object((1,3,6,1,4,1,21296,2,2,2,3,200,1,1,2),_CarrierCtpPmRealQPreFec_Type())
carrierCtpPmRealQPreFec.setMaxAccess(_C)
if mibBuilder.loadTexts:carrierCtpPmRealQPreFec.setStatus(_A)
_CarrierCtpPmRealBerPreFec_Type=FloatArbitraryPrecision
_CarrierCtpPmRealBerPreFec_Object=MibTableColumn
carrierCtpPmRealBerPreFec=_CarrierCtpPmRealBerPreFec_Object((1,3,6,1,4,1,21296,2,2,2,3,200,1,1,3),_CarrierCtpPmRealBerPreFec_Type())
carrierCtpPmRealBerPreFec.setMaxAccess(_C)
if mibBuilder.loadTexts:carrierCtpPmRealBerPreFec.setStatus(_A)
_CarrierCtpPmRealTxLBC_Type=FloatHundredths
_CarrierCtpPmRealTxLBC_Object=MibTableColumn
carrierCtpPmRealTxLBC=_CarrierCtpPmRealTxLBC_Object((1,3,6,1,4,1,21296,2,2,2,3,200,1,1,4),_CarrierCtpPmRealTxLBC_Type())
carrierCtpPmRealTxLBC.setMaxAccess(_C)
if mibBuilder.loadTexts:carrierCtpPmRealTxLBC.setStatus(_A)
_CarrierCtpPmRealRxLBC_Type=FloatHundredths
_CarrierCtpPmRealRxLBC_Object=MibTableColumn
carrierCtpPmRealRxLBC=_CarrierCtpPmRealRxLBC_Object((1,3,6,1,4,1,21296,2,2,2,3,200,1,1,5),_CarrierCtpPmRealRxLBC_Type())
carrierCtpPmRealRxLBC.setMaxAccess(_C)
if mibBuilder.loadTexts:carrierCtpPmRealRxLBC.setStatus(_A)
_CarrierCtpPmRealPmd_Type=FloatArbitraryPrecision
_CarrierCtpPmRealPmd_Object=MibTableColumn
carrierCtpPmRealPmd=_CarrierCtpPmRealPmd_Object((1,3,6,1,4,1,21296,2,2,2,3,200,1,1,6),_CarrierCtpPmRealPmd_Type())
carrierCtpPmRealPmd.setMaxAccess(_C)
if mibBuilder.loadTexts:carrierCtpPmRealPmd.setStatus(_A)
_CarrierCtpPmRealSoPmd_Type=FloatArbitraryPrecision
_CarrierCtpPmRealSoPmd_Object=MibTableColumn
carrierCtpPmRealSoPmd=_CarrierCtpPmRealSoPmd_Object((1,3,6,1,4,1,21296,2,2,2,3,200,1,1,7),_CarrierCtpPmRealSoPmd_Type())
carrierCtpPmRealSoPmd.setMaxAccess(_C)
if mibBuilder.loadTexts:carrierCtpPmRealSoPmd.setStatus(_A)
_CarrierCtpPmRealChromaticDispersion_Type=FloatArbitraryPrecision
_CarrierCtpPmRealChromaticDispersion_Object=MibTableColumn
carrierCtpPmRealChromaticDispersion=_CarrierCtpPmRealChromaticDispersion_Object((1,3,6,1,4,1,21296,2,2,2,3,200,1,1,8),_CarrierCtpPmRealChromaticDispersion_Type())
carrierCtpPmRealChromaticDispersion.setMaxAccess(_C)
if mibBuilder.loadTexts:carrierCtpPmRealChromaticDispersion.setStatus(_A)
_CarrierCtpPmRealPhaseCorrection_Type=FloatHundredths
_CarrierCtpPmRealPhaseCorrection_Object=MibTableColumn
carrierCtpPmRealPhaseCorrection=_CarrierCtpPmRealPhaseCorrection_Object((1,3,6,1,4,1,21296,2,2,2,3,200,1,1,9),_CarrierCtpPmRealPhaseCorrection_Type())
carrierCtpPmRealPhaseCorrection.setMaxAccess(_C)
if mibBuilder.loadTexts:carrierCtpPmRealPhaseCorrection.setStatus(_A)
_CarrierCtpPmRealBerPostFec_Type=FloatArbitraryPrecision
_CarrierCtpPmRealBerPostFec_Object=MibTableColumn
carrierCtpPmRealBerPostFec=_CarrierCtpPmRealBerPostFec_Object((1,3,6,1,4,1,21296,2,2,2,3,200,1,1,10),_CarrierCtpPmRealBerPostFec_Type())
carrierCtpPmRealBerPostFec.setMaxAccess(_C)
if mibBuilder.loadTexts:carrierCtpPmRealBerPostFec.setStatus(_A)
_CarrierCtpPmRealCodeWord_Type=Counter64
_CarrierCtpPmRealCodeWord_Object=MibTableColumn
carrierCtpPmRealCodeWord=_CarrierCtpPmRealCodeWord_Object((1,3,6,1,4,1,21296,2,2,2,3,200,1,1,11),_CarrierCtpPmRealCodeWord_Type())
carrierCtpPmRealCodeWord.setMaxAccess(_C)
if mibBuilder.loadTexts:carrierCtpPmRealCodeWord.setStatus(_A)
_CarrierCtpPmRealUnCorrectedCodeWord_Type=Counter64
_CarrierCtpPmRealUnCorrectedCodeWord_Object=MibTableColumn
carrierCtpPmRealUnCorrectedCodeWord=_CarrierCtpPmRealUnCorrectedCodeWord_Object((1,3,6,1,4,1,21296,2,2,2,3,200,1,1,12),_CarrierCtpPmRealUnCorrectedCodeWord_Type())
carrierCtpPmRealUnCorrectedCodeWord.setMaxAccess(_C)
if mibBuilder.loadTexts:carrierCtpPmRealUnCorrectedCodeWord.setStatus(_A)
_CarrierCtpPmRealCorrectedBits_Type=Counter64
_CarrierCtpPmRealCorrectedBits_Object=MibTableColumn
carrierCtpPmRealCorrectedBits=_CarrierCtpPmRealCorrectedBits_Object((1,3,6,1,4,1,21296,2,2,2,3,200,1,1,13),_CarrierCtpPmRealCorrectedBits_Type())
carrierCtpPmRealCorrectedBits.setMaxAccess(_C)
if mibBuilder.loadTexts:carrierCtpPmRealCorrectedBits.setStatus(_A)
_CarrierCtpPmRealWavelength_Type=FloatHundredths
_CarrierCtpPmRealWavelength_Object=MibTableColumn
carrierCtpPmRealWavelength=_CarrierCtpPmRealWavelength_Object((1,3,6,1,4,1,21296,2,2,2,3,200,1,1,14),_CarrierCtpPmRealWavelength_Type())
carrierCtpPmRealWavelength.setMaxAccess(_C)
if mibBuilder.loadTexts:carrierCtpPmRealWavelength.setStatus(_A)
_CarrierCtpPmTable_Object=MibTable
carrierCtpPmTable=_CarrierCtpPmTable_Object((1,3,6,1,4,1,21296,2,2,2,3,200,2))
if mibBuilder.loadTexts:carrierCtpPmTable.setStatus(_A)
_CarrierCtpPmEntry_Object=MibTableRow
carrierCtpPmEntry=_CarrierCtpPmEntry_Object((1,3,6,1,4,1,21296,2,2,2,3,200,2,1))
carrierCtpPmEntry.setIndexNames((0,_D,_E),(0,_B,_G),(0,_B,_H))
if mibBuilder.loadTexts:carrierCtpPmEntry.setStatus(_A)
class _CarrierCtpPmTimestamp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CarrierCtpPmTimestamp_Type.__name__=_F
_CarrierCtpPmTimestamp_Object=MibTableColumn
carrierCtpPmTimestamp=_CarrierCtpPmTimestamp_Object((1,3,6,1,4,1,21296,2,2,2,3,200,2,1,1),_CarrierCtpPmTimestamp_Type())
carrierCtpPmTimestamp.setMaxAccess(_I)
if mibBuilder.loadTexts:carrierCtpPmTimestamp.setStatus(_A)
class _CarrierCtpPmSampleDuration_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('fifteenMinutes',1),('day',2)))
_CarrierCtpPmSampleDuration_Type.__name__=_F
_CarrierCtpPmSampleDuration_Object=MibTableColumn
carrierCtpPmSampleDuration=_CarrierCtpPmSampleDuration_Object((1,3,6,1,4,1,21296,2,2,2,3,200,2,1,2),_CarrierCtpPmSampleDuration_Type())
carrierCtpPmSampleDuration.setMaxAccess(_I)
if mibBuilder.loadTexts:carrierCtpPmSampleDuration.setStatus(_A)
_CarrierCtpPmValidity_Type=TruthValue
_CarrierCtpPmValidity_Object=MibTableColumn
carrierCtpPmValidity=_CarrierCtpPmValidity_Object((1,3,6,1,4,1,21296,2,2,2,3,200,2,1,3),_CarrierCtpPmValidity_Type())
carrierCtpPmValidity.setMaxAccess(_C)
if mibBuilder.loadTexts:carrierCtpPmValidity.setStatus(_A)
_CarrierCtpPmOptMin_Type=FloatHundredths
_CarrierCtpPmOptMin_Object=MibTableColumn
carrierCtpPmOptMin=_CarrierCtpPmOptMin_Object((1,3,6,1,4,1,21296,2,2,2,3,200,2,1,4),_CarrierCtpPmOptMin_Type())
carrierCtpPmOptMin.setMaxAccess(_C)
if mibBuilder.loadTexts:carrierCtpPmOptMin.setStatus(_A)
_CarrierCtpPmOptMax_Type=FloatHundredths
_CarrierCtpPmOptMax_Object=MibTableColumn
carrierCtpPmOptMax=_CarrierCtpPmOptMax_Object((1,3,6,1,4,1,21296,2,2,2,3,200,2,1,5),_CarrierCtpPmOptMax_Type())
carrierCtpPmOptMax.setMaxAccess(_C)
if mibBuilder.loadTexts:carrierCtpPmOptMax.setStatus(_A)
_CarrierCtpPmOptAve_Type=FloatHundredths
_CarrierCtpPmOptAve_Object=MibTableColumn
carrierCtpPmOptAve=_CarrierCtpPmOptAve_Object((1,3,6,1,4,1,21296,2,2,2,3,200,2,1,6),_CarrierCtpPmOptAve_Type())
carrierCtpPmOptAve.setMaxAccess(_C)
if mibBuilder.loadTexts:carrierCtpPmOptAve.setStatus(_A)
_CarrierCtpPmQPreFecMin_Type=FloatHundredths
_CarrierCtpPmQPreFecMin_Object=MibTableColumn
carrierCtpPmQPreFecMin=_CarrierCtpPmQPreFecMin_Object((1,3,6,1,4,1,21296,2,2,2,3,200,2,1,7),_CarrierCtpPmQPreFecMin_Type())
carrierCtpPmQPreFecMin.setMaxAccess(_C)
if mibBuilder.loadTexts:carrierCtpPmQPreFecMin.setStatus(_A)
_CarrierCtpPmQPreFecMax_Type=FloatHundredths
_CarrierCtpPmQPreFecMax_Object=MibTableColumn
carrierCtpPmQPreFecMax=_CarrierCtpPmQPreFecMax_Object((1,3,6,1,4,1,21296,2,2,2,3,200,2,1,8),_CarrierCtpPmQPreFecMax_Type())
carrierCtpPmQPreFecMax.setMaxAccess(_C)
if mibBuilder.loadTexts:carrierCtpPmQPreFecMax.setStatus(_A)
_CarrierCtpPmQPreFecAve_Type=FloatHundredths
_CarrierCtpPmQPreFecAve_Object=MibTableColumn
carrierCtpPmQPreFecAve=_CarrierCtpPmQPreFecAve_Object((1,3,6,1,4,1,21296,2,2,2,3,200,2,1,9),_CarrierCtpPmQPreFecAve_Type())
carrierCtpPmQPreFecAve.setMaxAccess(_C)
if mibBuilder.loadTexts:carrierCtpPmQPreFecAve.setStatus(_A)
_CarrierCtpPmBerPreFecMin_Type=FloatArbitraryPrecision
_CarrierCtpPmBerPreFecMin_Object=MibTableColumn
carrierCtpPmBerPreFecMin=_CarrierCtpPmBerPreFecMin_Object((1,3,6,1,4,1,21296,2,2,2,3,200,2,1,10),_CarrierCtpPmBerPreFecMin_Type())
carrierCtpPmBerPreFecMin.setMaxAccess(_C)
if mibBuilder.loadTexts:carrierCtpPmBerPreFecMin.setStatus(_A)
_CarrierCtpPmBerPreFecMax_Type=FloatArbitraryPrecision
_CarrierCtpPmBerPreFecMax_Object=MibTableColumn
carrierCtpPmBerPreFecMax=_CarrierCtpPmBerPreFecMax_Object((1,3,6,1,4,1,21296,2,2,2,3,200,2,1,11),_CarrierCtpPmBerPreFecMax_Type())
carrierCtpPmBerPreFecMax.setMaxAccess(_C)
if mibBuilder.loadTexts:carrierCtpPmBerPreFecMax.setStatus(_A)
_CarrierCtpPmBerPreFecAve_Type=FloatArbitraryPrecision
_CarrierCtpPmBerPreFecAve_Object=MibTableColumn
carrierCtpPmBerPreFecAve=_CarrierCtpPmBerPreFecAve_Object((1,3,6,1,4,1,21296,2,2,2,3,200,2,1,12),_CarrierCtpPmBerPreFecAve_Type())
carrierCtpPmBerPreFecAve.setMaxAccess(_C)
if mibBuilder.loadTexts:carrierCtpPmBerPreFecAve.setStatus(_A)
_CarrierCtpPmTxLBCMin_Type=FloatHundredths
_CarrierCtpPmTxLBCMin_Object=MibTableColumn
carrierCtpPmTxLBCMin=_CarrierCtpPmTxLBCMin_Object((1,3,6,1,4,1,21296,2,2,2,3,200,2,1,13),_CarrierCtpPmTxLBCMin_Type())
carrierCtpPmTxLBCMin.setMaxAccess(_C)
if mibBuilder.loadTexts:carrierCtpPmTxLBCMin.setStatus(_A)
_CarrierCtpPmTxLBCMax_Type=FloatHundredths
_CarrierCtpPmTxLBCMax_Object=MibTableColumn
carrierCtpPmTxLBCMax=_CarrierCtpPmTxLBCMax_Object((1,3,6,1,4,1,21296,2,2,2,3,200,2,1,14),_CarrierCtpPmTxLBCMax_Type())
carrierCtpPmTxLBCMax.setMaxAccess(_C)
if mibBuilder.loadTexts:carrierCtpPmTxLBCMax.setStatus(_A)
_CarrierCtpPmTxLBCAve_Type=FloatHundredths
_CarrierCtpPmTxLBCAve_Object=MibTableColumn
carrierCtpPmTxLBCAve=_CarrierCtpPmTxLBCAve_Object((1,3,6,1,4,1,21296,2,2,2,3,200,2,1,15),_CarrierCtpPmTxLBCAve_Type())
carrierCtpPmTxLBCAve.setMaxAccess(_C)
if mibBuilder.loadTexts:carrierCtpPmTxLBCAve.setStatus(_A)
_CarrierCtpPmRxLBCMin_Type=FloatHundredths
_CarrierCtpPmRxLBCMin_Object=MibTableColumn
carrierCtpPmRxLBCMin=_CarrierCtpPmRxLBCMin_Object((1,3,6,1,4,1,21296,2,2,2,3,200,2,1,16),_CarrierCtpPmRxLBCMin_Type())
carrierCtpPmRxLBCMin.setMaxAccess(_C)
if mibBuilder.loadTexts:carrierCtpPmRxLBCMin.setStatus(_A)
_CarrierCtpPmRxLBCMax_Type=FloatHundredths
_CarrierCtpPmRxLBCMax_Object=MibTableColumn
carrierCtpPmRxLBCMax=_CarrierCtpPmRxLBCMax_Object((1,3,6,1,4,1,21296,2,2,2,3,200,2,1,17),_CarrierCtpPmRxLBCMax_Type())
carrierCtpPmRxLBCMax.setMaxAccess(_C)
if mibBuilder.loadTexts:carrierCtpPmRxLBCMax.setStatus(_A)
_CarrierCtpPmRxLBCAve_Type=FloatHundredths
_CarrierCtpPmRxLBCAve_Object=MibTableColumn
carrierCtpPmRxLBCAve=_CarrierCtpPmRxLBCAve_Object((1,3,6,1,4,1,21296,2,2,2,3,200,2,1,18),_CarrierCtpPmRxLBCAve_Type())
carrierCtpPmRxLBCAve.setMaxAccess(_C)
if mibBuilder.loadTexts:carrierCtpPmRxLBCAve.setStatus(_A)
_CarrierCtpPmPmdMin_Type=FloatArbitraryPrecision
_CarrierCtpPmPmdMin_Object=MibTableColumn
carrierCtpPmPmdMin=_CarrierCtpPmPmdMin_Object((1,3,6,1,4,1,21296,2,2,2,3,200,2,1,19),_CarrierCtpPmPmdMin_Type())
carrierCtpPmPmdMin.setMaxAccess(_C)
if mibBuilder.loadTexts:carrierCtpPmPmdMin.setStatus(_A)
_CarrierCtpPmPmdMax_Type=FloatArbitraryPrecision
_CarrierCtpPmPmdMax_Object=MibTableColumn
carrierCtpPmPmdMax=_CarrierCtpPmPmdMax_Object((1,3,6,1,4,1,21296,2,2,2,3,200,2,1,20),_CarrierCtpPmPmdMax_Type())
carrierCtpPmPmdMax.setMaxAccess(_C)
if mibBuilder.loadTexts:carrierCtpPmPmdMax.setStatus(_A)
_CarrierCtpPmPmdAve_Type=FloatArbitraryPrecision
_CarrierCtpPmPmdAve_Object=MibTableColumn
carrierCtpPmPmdAve=_CarrierCtpPmPmdAve_Object((1,3,6,1,4,1,21296,2,2,2,3,200,2,1,21),_CarrierCtpPmPmdAve_Type())
carrierCtpPmPmdAve.setMaxAccess(_C)
if mibBuilder.loadTexts:carrierCtpPmPmdAve.setStatus(_A)
_CarrierCtpPmSoPmdMin_Type=FloatArbitraryPrecision
_CarrierCtpPmSoPmdMin_Object=MibTableColumn
carrierCtpPmSoPmdMin=_CarrierCtpPmSoPmdMin_Object((1,3,6,1,4,1,21296,2,2,2,3,200,2,1,22),_CarrierCtpPmSoPmdMin_Type())
carrierCtpPmSoPmdMin.setMaxAccess(_C)
if mibBuilder.loadTexts:carrierCtpPmSoPmdMin.setStatus(_A)
_CarrierCtpPmSoPmdMax_Type=FloatArbitraryPrecision
_CarrierCtpPmSoPmdMax_Object=MibTableColumn
carrierCtpPmSoPmdMax=_CarrierCtpPmSoPmdMax_Object((1,3,6,1,4,1,21296,2,2,2,3,200,2,1,23),_CarrierCtpPmSoPmdMax_Type())
carrierCtpPmSoPmdMax.setMaxAccess(_C)
if mibBuilder.loadTexts:carrierCtpPmSoPmdMax.setStatus(_A)
_CarrierCtpPmSoPmdAve_Type=FloatArbitraryPrecision
_CarrierCtpPmSoPmdAve_Object=MibTableColumn
carrierCtpPmSoPmdAve=_CarrierCtpPmSoPmdAve_Object((1,3,6,1,4,1,21296,2,2,2,3,200,2,1,24),_CarrierCtpPmSoPmdAve_Type())
carrierCtpPmSoPmdAve.setMaxAccess(_C)
if mibBuilder.loadTexts:carrierCtpPmSoPmdAve.setStatus(_A)
_CarrierCtpPmChromaticDispersionMin_Type=FloatArbitraryPrecision
_CarrierCtpPmChromaticDispersionMin_Object=MibTableColumn
carrierCtpPmChromaticDispersionMin=_CarrierCtpPmChromaticDispersionMin_Object((1,3,6,1,4,1,21296,2,2,2,3,200,2,1,25),_CarrierCtpPmChromaticDispersionMin_Type())
carrierCtpPmChromaticDispersionMin.setMaxAccess(_C)
if mibBuilder.loadTexts:carrierCtpPmChromaticDispersionMin.setStatus(_A)
_CarrierCtpPmChromaticDispersionMax_Type=FloatArbitraryPrecision
_CarrierCtpPmChromaticDispersionMax_Object=MibTableColumn
carrierCtpPmChromaticDispersionMax=_CarrierCtpPmChromaticDispersionMax_Object((1,3,6,1,4,1,21296,2,2,2,3,200,2,1,26),_CarrierCtpPmChromaticDispersionMax_Type())
carrierCtpPmChromaticDispersionMax.setMaxAccess(_C)
if mibBuilder.loadTexts:carrierCtpPmChromaticDispersionMax.setStatus(_A)
_CarrierCtpPmChromaticDispersionAve_Type=FloatArbitraryPrecision
_CarrierCtpPmChromaticDispersionAve_Object=MibTableColumn
carrierCtpPmChromaticDispersionAve=_CarrierCtpPmChromaticDispersionAve_Object((1,3,6,1,4,1,21296,2,2,2,3,200,2,1,27),_CarrierCtpPmChromaticDispersionAve_Type())
carrierCtpPmChromaticDispersionAve.setMaxAccess(_C)
if mibBuilder.loadTexts:carrierCtpPmChromaticDispersionAve.setStatus(_A)
_CarrierCtpPmPhaseCorrectionMin_Type=FloatHundredths
_CarrierCtpPmPhaseCorrectionMin_Object=MibTableColumn
carrierCtpPmPhaseCorrectionMin=_CarrierCtpPmPhaseCorrectionMin_Object((1,3,6,1,4,1,21296,2,2,2,3,200,2,1,28),_CarrierCtpPmPhaseCorrectionMin_Type())
carrierCtpPmPhaseCorrectionMin.setMaxAccess(_C)
if mibBuilder.loadTexts:carrierCtpPmPhaseCorrectionMin.setStatus(_A)
_CarrierCtpPmPhaseCorrectionMax_Type=FloatHundredths
_CarrierCtpPmPhaseCorrectionMax_Object=MibTableColumn
carrierCtpPmPhaseCorrectionMax=_CarrierCtpPmPhaseCorrectionMax_Object((1,3,6,1,4,1,21296,2,2,2,3,200,2,1,29),_CarrierCtpPmPhaseCorrectionMax_Type())
carrierCtpPmPhaseCorrectionMax.setMaxAccess(_C)
if mibBuilder.loadTexts:carrierCtpPmPhaseCorrectionMax.setStatus(_A)
_CarrierCtpPmPhaseCorrectionAve_Type=FloatHundredths
_CarrierCtpPmPhaseCorrectionAve_Object=MibTableColumn
carrierCtpPmPhaseCorrectionAve=_CarrierCtpPmPhaseCorrectionAve_Object((1,3,6,1,4,1,21296,2,2,2,3,200,2,1,30),_CarrierCtpPmPhaseCorrectionAve_Type())
carrierCtpPmPhaseCorrectionAve.setMaxAccess(_C)
if mibBuilder.loadTexts:carrierCtpPmPhaseCorrectionAve.setStatus(_A)
_CarrierCtpPmBerPostFecMin_Type=FloatArbitraryPrecision
_CarrierCtpPmBerPostFecMin_Object=MibTableColumn
carrierCtpPmBerPostFecMin=_CarrierCtpPmBerPostFecMin_Object((1,3,6,1,4,1,21296,2,2,2,3,200,2,1,31),_CarrierCtpPmBerPostFecMin_Type())
carrierCtpPmBerPostFecMin.setMaxAccess(_C)
if mibBuilder.loadTexts:carrierCtpPmBerPostFecMin.setStatus(_A)
_CarrierCtpPmBerPostFecMax_Type=FloatArbitraryPrecision
_CarrierCtpPmBerPostFecMax_Object=MibTableColumn
carrierCtpPmBerPostFecMax=_CarrierCtpPmBerPostFecMax_Object((1,3,6,1,4,1,21296,2,2,2,3,200,2,1,32),_CarrierCtpPmBerPostFecMax_Type())
carrierCtpPmBerPostFecMax.setMaxAccess(_C)
if mibBuilder.loadTexts:carrierCtpPmBerPostFecMax.setStatus(_A)
_CarrierCtpPmBerPostFecAve_Type=FloatArbitraryPrecision
_CarrierCtpPmBerPostFecAve_Object=MibTableColumn
carrierCtpPmBerPostFecAve=_CarrierCtpPmBerPostFecAve_Object((1,3,6,1,4,1,21296,2,2,2,3,200,2,1,33),_CarrierCtpPmBerPostFecAve_Type())
carrierCtpPmBerPostFecAve.setMaxAccess(_C)
if mibBuilder.loadTexts:carrierCtpPmBerPostFecAve.setStatus(_A)
_CarrierCtpPmCodeWord_Type=HCPerfIntervalCount
_CarrierCtpPmCodeWord_Object=MibTableColumn
carrierCtpPmCodeWord=_CarrierCtpPmCodeWord_Object((1,3,6,1,4,1,21296,2,2,2,3,200,2,1,34),_CarrierCtpPmCodeWord_Type())
carrierCtpPmCodeWord.setMaxAccess(_C)
if mibBuilder.loadTexts:carrierCtpPmCodeWord.setStatus(_A)
_CarrierCtpPmUnCorrectedCodeWord_Type=HCPerfIntervalCount
_CarrierCtpPmUnCorrectedCodeWord_Object=MibTableColumn
carrierCtpPmUnCorrectedCodeWord=_CarrierCtpPmUnCorrectedCodeWord_Object((1,3,6,1,4,1,21296,2,2,2,3,200,2,1,35),_CarrierCtpPmUnCorrectedCodeWord_Type())
carrierCtpPmUnCorrectedCodeWord.setMaxAccess(_C)
if mibBuilder.loadTexts:carrierCtpPmUnCorrectedCodeWord.setStatus(_A)
_CarrierCtpPmCorrectedBits_Type=HCPerfIntervalCount
_CarrierCtpPmCorrectedBits_Object=MibTableColumn
carrierCtpPmCorrectedBits=_CarrierCtpPmCorrectedBits_Object((1,3,6,1,4,1,21296,2,2,2,3,200,2,1,36),_CarrierCtpPmCorrectedBits_Type())
carrierCtpPmCorrectedBits.setMaxAccess(_C)
if mibBuilder.loadTexts:carrierCtpPmCorrectedBits.setStatus(_A)
_CarrierCtpPmConformance_ObjectIdentity=ObjectIdentity
carrierCtpPmConformance=_CarrierCtpPmConformance_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,3,200,3))
_CarrierCtpPmCompliances_ObjectIdentity=ObjectIdentity
carrierCtpPmCompliances=_CarrierCtpPmCompliances_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,3,200,3,1))
_CarrierCtpPmGroups_ObjectIdentity=ObjectIdentity
carrierCtpPmGroups=_CarrierCtpPmGroups_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,3,200,3,2))
carrierCtpPmGroup=ObjectGroup((1,3,6,1,4,1,21296,2,2,2,3,200,3,2,1))
carrierCtpPmGroup.setObjects(*((_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q)))
if mibBuilder.loadTexts:carrierCtpPmGroup.setStatus(_A)
carrierCtpPmRealGroup=ObjectGroup((1,3,6,1,4,1,21296,2,2,2,3,200,3,2,2))
carrierCtpPmRealGroup.setObjects(*((_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_x),(_B,_y),(_B,_z),(_B,_A0),(_B,_A1),(_B,_A2),(_B,_A3),(_B,_A4)))
if mibBuilder.loadTexts:carrierCtpPmRealGroup.setStatus(_A)
carrierCtpPmCompliance=ModuleCompliance((1,3,6,1,4,1,21296,2,2,2,3,200,3,1,1))
carrierCtpPmCompliance.setObjects((_B,_A5))
if mibBuilder.loadTexts:carrierCtpPmCompliance.setStatus(_A)
carrierCtpPmRealCompliance=ModuleCompliance((1,3,6,1,4,1,21296,2,2,2,3,200,3,1,2))
carrierCtpPmRealCompliance.setObjects((_B,_A6))
if mibBuilder.loadTexts:carrierCtpPmRealCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'carrierCtpPmMIB':carrierCtpPmMIB,'carrierCtpPmRealTable':carrierCtpPmRealTable,'carrierCtpPmRealEntry':carrierCtpPmRealEntry,_r:carrierCtpPmRealOpt,_s:carrierCtpPmRealQPreFec,_t:carrierCtpPmRealBerPreFec,_u:carrierCtpPmRealTxLBC,_v:carrierCtpPmRealRxLBC,_w:carrierCtpPmRealPmd,_x:carrierCtpPmRealSoPmd,_y:carrierCtpPmRealChromaticDispersion,_z:carrierCtpPmRealPhaseCorrection,_A0:carrierCtpPmRealBerPostFec,_A1:carrierCtpPmRealCodeWord,_A2:carrierCtpPmRealUnCorrectedCodeWord,_A3:carrierCtpPmRealCorrectedBits,_A4:carrierCtpPmRealWavelength,'carrierCtpPmTable':carrierCtpPmTable,'carrierCtpPmEntry':carrierCtpPmEntry,_H:carrierCtpPmTimestamp,_G:carrierCtpPmSampleDuration,_J:carrierCtpPmValidity,_K:carrierCtpPmOptMin,_L:carrierCtpPmOptMax,_M:carrierCtpPmOptAve,_N:carrierCtpPmQPreFecMin,_O:carrierCtpPmQPreFecMax,_P:carrierCtpPmQPreFecAve,_Q:carrierCtpPmBerPreFecMin,_R:carrierCtpPmBerPreFecMax,_S:carrierCtpPmBerPreFecAve,_T:carrierCtpPmTxLBCMin,_U:carrierCtpPmTxLBCMax,_V:carrierCtpPmTxLBCAve,_W:carrierCtpPmRxLBCMin,_X:carrierCtpPmRxLBCMax,_Y:carrierCtpPmRxLBCAve,_Z:carrierCtpPmPmdMin,_a:carrierCtpPmPmdMax,_b:carrierCtpPmPmdAve,_c:carrierCtpPmSoPmdMin,_d:carrierCtpPmSoPmdMax,_e:carrierCtpPmSoPmdAve,_f:carrierCtpPmChromaticDispersionMin,_g:carrierCtpPmChromaticDispersionMax,_h:carrierCtpPmChromaticDispersionAve,_i:carrierCtpPmPhaseCorrectionMin,_j:carrierCtpPmPhaseCorrectionMax,_k:carrierCtpPmPhaseCorrectionAve,_l:carrierCtpPmBerPostFecMin,_m:carrierCtpPmBerPostFecMax,_n:carrierCtpPmBerPostFecAve,_o:carrierCtpPmCodeWord,_p:carrierCtpPmUnCorrectedCodeWord,_q:carrierCtpPmCorrectedBits,'carrierCtpPmConformance':carrierCtpPmConformance,'carrierCtpPmCompliances':carrierCtpPmCompliances,'carrierCtpPmCompliance':carrierCtpPmCompliance,'carrierCtpPmRealCompliance':carrierCtpPmRealCompliance,'carrierCtpPmGroups':carrierCtpPmGroups,_A5:carrierCtpPmGroup,_A6:carrierCtpPmRealGroup})