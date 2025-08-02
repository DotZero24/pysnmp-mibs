_A6='ochCtpPmRealGroup'
_A5='ochCtpPmGroup'
_A4='ochCtpPmRealCrctdBits'
_A3='ochCtpPmRealUnCrctblCW'
_A2='ochCtpPmRealCWProc'
_A1='ochCtpPmRealBerPostFec'
_A0='ochCtpPmRealPhaseCorrection'
_z='ochCtpPmBerPreFec'
_y='ochCtpPmRealSoPmd'
_x='ochCtpPmRealPmd'
_w='ochCtpPmRealChanOchCD'
_v='ochCtpPmRealChanOchQValue'
_u='ochCtpPmRealChanOchMeasuredWavelength'
_t='ochCtpPmRealChanOchLBC'
_s='ochCtpPmRealChanOchOpr'
_r='ochCtpPmRealChanOchOpt'
_q='ochCtpPmCrctdBits'
_p='ochCtpPmUnCrctblCW'
_o='ochCtpPmCWProc'
_n='ochCtpPmBerPostFecAve'
_m='ochCtpPmBerPostFecMax'
_l='ochCtpPmBerPostFecMin'
_k='ochCtpPmPhaseCorrectionAve'
_j='ochCtpPmPhaseCorrectionMax'
_i='ochCtpPmPhaseCorrectionMin'
_h='ochCtpPmBerPreFecAve'
_g='ochCtpPmBerPreFecMax'
_f='ochCtpPmBerPreFecMin'
_e='ochCtpPmSoPmdAve'
_d='ochCtpPmSoPmdMax'
_c='ochCtpPmSoPmdMin'
_b='ochCtpPmPmdAve'
_a='ochCtpPmPmdMax'
_Z='ochCtpPmPmdMin'
_Y='ochCtpPmChanOchCDAve'
_X='ochCtpPmChanOchCDMax'
_W='ochCtpPmChanOchCDMin'
_V='ochCtpPmChanOchQValueAve'
_U='ochCtpPmChanOchQValueMax'
_T='ochCtpPmChanOchQValueMin'
_S='ochCtpPmChanOchLBCAve'
_R='ochCtpPmChanOchLBCMax'
_Q='ochCtpPmChanOchLBCMin'
_P='ochCtpPmChanOchOprAve'
_O='ochCtpPmChanOchOprMax'
_N='ochCtpPmChanOchOprMin'
_M='ochCtpPmChanOchOptAve'
_L='ochCtpPmChanOchOptMax'
_K='ochCtpPmChanOchOptMin'
_J='ochCtpPmValidity'
_I='not-accessible'
_H='ochCtpPmTimestamp'
_G='ochCtpPmSampleDuration'
_F='Integer32'
_E='ifIndex'
_D='IF-MIB'
_C='read-only'
_B='INFINERA-PM-OCHCTP-MIB'
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
ochCtpPmMIB=ModuleIdentity((1,3,6,1,4,1,21296,2,2,2,3,30))
if mibBuilder.loadTexts:ochCtpPmMIB.setRevisions(('2011-10-23 00:00',))
_OchCtpPmRealTable_Object=MibTable
ochCtpPmRealTable=_OchCtpPmRealTable_Object((1,3,6,1,4,1,21296,2,2,2,3,30,1))
if mibBuilder.loadTexts:ochCtpPmRealTable.setStatus(_A)
_OchCtpPmRealEntry_Object=MibTableRow
ochCtpPmRealEntry=_OchCtpPmRealEntry_Object((1,3,6,1,4,1,21296,2,2,2,3,30,1,1))
ochCtpPmRealEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:ochCtpPmRealEntry.setStatus(_A)
_OchCtpPmRealChanOchOpt_Type=FloatHundredths
_OchCtpPmRealChanOchOpt_Object=MibTableColumn
ochCtpPmRealChanOchOpt=_OchCtpPmRealChanOchOpt_Object((1,3,6,1,4,1,21296,2,2,2,3,30,1,1,1),_OchCtpPmRealChanOchOpt_Type())
ochCtpPmRealChanOchOpt.setMaxAccess(_C)
if mibBuilder.loadTexts:ochCtpPmRealChanOchOpt.setStatus(_A)
_OchCtpPmRealChanOchOpr_Type=FloatHundredths
_OchCtpPmRealChanOchOpr_Object=MibTableColumn
ochCtpPmRealChanOchOpr=_OchCtpPmRealChanOchOpr_Object((1,3,6,1,4,1,21296,2,2,2,3,30,1,1,2),_OchCtpPmRealChanOchOpr_Type())
ochCtpPmRealChanOchOpr.setMaxAccess(_C)
if mibBuilder.loadTexts:ochCtpPmRealChanOchOpr.setStatus(_A)
_OchCtpPmRealChanOchLBC_Type=FloatHundredths
_OchCtpPmRealChanOchLBC_Object=MibTableColumn
ochCtpPmRealChanOchLBC=_OchCtpPmRealChanOchLBC_Object((1,3,6,1,4,1,21296,2,2,2,3,30,1,1,3),_OchCtpPmRealChanOchLBC_Type())
ochCtpPmRealChanOchLBC.setMaxAccess(_C)
if mibBuilder.loadTexts:ochCtpPmRealChanOchLBC.setStatus(_A)
_OchCtpPmRealChanOchMeasuredWavelength_Type=FloatHundredths
_OchCtpPmRealChanOchMeasuredWavelength_Object=MibTableColumn
ochCtpPmRealChanOchMeasuredWavelength=_OchCtpPmRealChanOchMeasuredWavelength_Object((1,3,6,1,4,1,21296,2,2,2,3,30,1,1,4),_OchCtpPmRealChanOchMeasuredWavelength_Type())
ochCtpPmRealChanOchMeasuredWavelength.setMaxAccess(_C)
if mibBuilder.loadTexts:ochCtpPmRealChanOchMeasuredWavelength.setStatus(_A)
_OchCtpPmRealChanOchQValue_Type=FloatHundredths
_OchCtpPmRealChanOchQValue_Object=MibTableColumn
ochCtpPmRealChanOchQValue=_OchCtpPmRealChanOchQValue_Object((1,3,6,1,4,1,21296,2,2,2,3,30,1,1,5),_OchCtpPmRealChanOchQValue_Type())
ochCtpPmRealChanOchQValue.setMaxAccess(_C)
if mibBuilder.loadTexts:ochCtpPmRealChanOchQValue.setStatus(_A)
_OchCtpPmRealChanOchCD_Type=FloatHundredths
_OchCtpPmRealChanOchCD_Object=MibTableColumn
ochCtpPmRealChanOchCD=_OchCtpPmRealChanOchCD_Object((1,3,6,1,4,1,21296,2,2,2,3,30,1,1,6),_OchCtpPmRealChanOchCD_Type())
ochCtpPmRealChanOchCD.setMaxAccess(_C)
if mibBuilder.loadTexts:ochCtpPmRealChanOchCD.setStatus(_A)
_OchCtpPmRealPmd_Type=FloatArbitraryPrecision
_OchCtpPmRealPmd_Object=MibTableColumn
ochCtpPmRealPmd=_OchCtpPmRealPmd_Object((1,3,6,1,4,1,21296,2,2,2,3,30,1,1,7),_OchCtpPmRealPmd_Type())
ochCtpPmRealPmd.setMaxAccess(_C)
if mibBuilder.loadTexts:ochCtpPmRealPmd.setStatus(_A)
_OchCtpPmRealSoPmd_Type=FloatArbitraryPrecision
_OchCtpPmRealSoPmd_Object=MibTableColumn
ochCtpPmRealSoPmd=_OchCtpPmRealSoPmd_Object((1,3,6,1,4,1,21296,2,2,2,3,30,1,1,8),_OchCtpPmRealSoPmd_Type())
ochCtpPmRealSoPmd.setMaxAccess(_C)
if mibBuilder.loadTexts:ochCtpPmRealSoPmd.setStatus(_A)
_OchCtpPmBerPreFec_Type=FloatArbitraryPrecision
_OchCtpPmBerPreFec_Object=MibTableColumn
ochCtpPmBerPreFec=_OchCtpPmBerPreFec_Object((1,3,6,1,4,1,21296,2,2,2,3,30,1,1,9),_OchCtpPmBerPreFec_Type())
ochCtpPmBerPreFec.setMaxAccess(_C)
if mibBuilder.loadTexts:ochCtpPmBerPreFec.setStatus(_A)
_OchCtpPmRealPhaseCorrection_Type=FloatHundredths
_OchCtpPmRealPhaseCorrection_Object=MibTableColumn
ochCtpPmRealPhaseCorrection=_OchCtpPmRealPhaseCorrection_Object((1,3,6,1,4,1,21296,2,2,2,3,30,1,1,10),_OchCtpPmRealPhaseCorrection_Type())
ochCtpPmRealPhaseCorrection.setMaxAccess(_C)
if mibBuilder.loadTexts:ochCtpPmRealPhaseCorrection.setStatus(_A)
_OchCtpPmRealBerPostFec_Type=FloatArbitraryPrecision
_OchCtpPmRealBerPostFec_Object=MibTableColumn
ochCtpPmRealBerPostFec=_OchCtpPmRealBerPostFec_Object((1,3,6,1,4,1,21296,2,2,2,3,30,1,1,11),_OchCtpPmRealBerPostFec_Type())
ochCtpPmRealBerPostFec.setMaxAccess(_C)
if mibBuilder.loadTexts:ochCtpPmRealBerPostFec.setStatus(_A)
_OchCtpPmRealCWProc_Type=HCPerfIntervalCount
_OchCtpPmRealCWProc_Object=MibTableColumn
ochCtpPmRealCWProc=_OchCtpPmRealCWProc_Object((1,3,6,1,4,1,21296,2,2,2,3,30,1,1,12),_OchCtpPmRealCWProc_Type())
ochCtpPmRealCWProc.setMaxAccess(_C)
if mibBuilder.loadTexts:ochCtpPmRealCWProc.setStatus(_A)
_OchCtpPmRealUnCrctblCW_Type=HCPerfIntervalCount
_OchCtpPmRealUnCrctblCW_Object=MibTableColumn
ochCtpPmRealUnCrctblCW=_OchCtpPmRealUnCrctblCW_Object((1,3,6,1,4,1,21296,2,2,2,3,30,1,1,13),_OchCtpPmRealUnCrctblCW_Type())
ochCtpPmRealUnCrctblCW.setMaxAccess(_C)
if mibBuilder.loadTexts:ochCtpPmRealUnCrctblCW.setStatus(_A)
_OchCtpPmRealCrctdBits_Type=HCPerfIntervalCount
_OchCtpPmRealCrctdBits_Object=MibTableColumn
ochCtpPmRealCrctdBits=_OchCtpPmRealCrctdBits_Object((1,3,6,1,4,1,21296,2,2,2,3,30,1,1,14),_OchCtpPmRealCrctdBits_Type())
ochCtpPmRealCrctdBits.setMaxAccess(_C)
if mibBuilder.loadTexts:ochCtpPmRealCrctdBits.setStatus(_A)
_OchCtpPmTable_Object=MibTable
ochCtpPmTable=_OchCtpPmTable_Object((1,3,6,1,4,1,21296,2,2,2,3,30,2))
if mibBuilder.loadTexts:ochCtpPmTable.setStatus(_A)
_OchCtpPmEntry_Object=MibTableRow
ochCtpPmEntry=_OchCtpPmEntry_Object((1,3,6,1,4,1,21296,2,2,2,3,30,2,1))
ochCtpPmEntry.setIndexNames((0,_D,_E),(0,_B,_G),(0,_B,_H))
if mibBuilder.loadTexts:ochCtpPmEntry.setStatus(_A)
class _OchCtpPmTimestamp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_OchCtpPmTimestamp_Type.__name__=_F
_OchCtpPmTimestamp_Object=MibTableColumn
ochCtpPmTimestamp=_OchCtpPmTimestamp_Object((1,3,6,1,4,1,21296,2,2,2,3,30,2,1,1),_OchCtpPmTimestamp_Type())
ochCtpPmTimestamp.setMaxAccess(_I)
if mibBuilder.loadTexts:ochCtpPmTimestamp.setStatus(_A)
class _OchCtpPmSampleDuration_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('fifteenMinutes',1),('day',2)))
_OchCtpPmSampleDuration_Type.__name__=_F
_OchCtpPmSampleDuration_Object=MibTableColumn
ochCtpPmSampleDuration=_OchCtpPmSampleDuration_Object((1,3,6,1,4,1,21296,2,2,2,3,30,2,1,2),_OchCtpPmSampleDuration_Type())
ochCtpPmSampleDuration.setMaxAccess(_I)
if mibBuilder.loadTexts:ochCtpPmSampleDuration.setStatus(_A)
_OchCtpPmValidity_Type=TruthValue
_OchCtpPmValidity_Object=MibTableColumn
ochCtpPmValidity=_OchCtpPmValidity_Object((1,3,6,1,4,1,21296,2,2,2,3,30,2,1,3),_OchCtpPmValidity_Type())
ochCtpPmValidity.setMaxAccess(_C)
if mibBuilder.loadTexts:ochCtpPmValidity.setStatus(_A)
_OchCtpPmChanOchOptMin_Type=FloatHundredths
_OchCtpPmChanOchOptMin_Object=MibTableColumn
ochCtpPmChanOchOptMin=_OchCtpPmChanOchOptMin_Object((1,3,6,1,4,1,21296,2,2,2,3,30,2,1,4),_OchCtpPmChanOchOptMin_Type())
ochCtpPmChanOchOptMin.setMaxAccess(_C)
if mibBuilder.loadTexts:ochCtpPmChanOchOptMin.setStatus(_A)
_OchCtpPmChanOchOptMax_Type=FloatHundredths
_OchCtpPmChanOchOptMax_Object=MibTableColumn
ochCtpPmChanOchOptMax=_OchCtpPmChanOchOptMax_Object((1,3,6,1,4,1,21296,2,2,2,3,30,2,1,5),_OchCtpPmChanOchOptMax_Type())
ochCtpPmChanOchOptMax.setMaxAccess(_C)
if mibBuilder.loadTexts:ochCtpPmChanOchOptMax.setStatus(_A)
_OchCtpPmChanOchOptAve_Type=FloatHundredths
_OchCtpPmChanOchOptAve_Object=MibTableColumn
ochCtpPmChanOchOptAve=_OchCtpPmChanOchOptAve_Object((1,3,6,1,4,1,21296,2,2,2,3,30,2,1,6),_OchCtpPmChanOchOptAve_Type())
ochCtpPmChanOchOptAve.setMaxAccess(_C)
if mibBuilder.loadTexts:ochCtpPmChanOchOptAve.setStatus(_A)
_OchCtpPmChanOchOprMin_Type=FloatHundredths
_OchCtpPmChanOchOprMin_Object=MibTableColumn
ochCtpPmChanOchOprMin=_OchCtpPmChanOchOprMin_Object((1,3,6,1,4,1,21296,2,2,2,3,30,2,1,7),_OchCtpPmChanOchOprMin_Type())
ochCtpPmChanOchOprMin.setMaxAccess(_C)
if mibBuilder.loadTexts:ochCtpPmChanOchOprMin.setStatus(_A)
_OchCtpPmChanOchOprMax_Type=FloatHundredths
_OchCtpPmChanOchOprMax_Object=MibTableColumn
ochCtpPmChanOchOprMax=_OchCtpPmChanOchOprMax_Object((1,3,6,1,4,1,21296,2,2,2,3,30,2,1,8),_OchCtpPmChanOchOprMax_Type())
ochCtpPmChanOchOprMax.setMaxAccess(_C)
if mibBuilder.loadTexts:ochCtpPmChanOchOprMax.setStatus(_A)
_OchCtpPmChanOchOprAve_Type=FloatHundredths
_OchCtpPmChanOchOprAve_Object=MibTableColumn
ochCtpPmChanOchOprAve=_OchCtpPmChanOchOprAve_Object((1,3,6,1,4,1,21296,2,2,2,3,30,2,1,9),_OchCtpPmChanOchOprAve_Type())
ochCtpPmChanOchOprAve.setMaxAccess(_C)
if mibBuilder.loadTexts:ochCtpPmChanOchOprAve.setStatus(_A)
_OchCtpPmChanOchLBCMin_Type=FloatHundredths
_OchCtpPmChanOchLBCMin_Object=MibTableColumn
ochCtpPmChanOchLBCMin=_OchCtpPmChanOchLBCMin_Object((1,3,6,1,4,1,21296,2,2,2,3,30,2,1,10),_OchCtpPmChanOchLBCMin_Type())
ochCtpPmChanOchLBCMin.setMaxAccess(_C)
if mibBuilder.loadTexts:ochCtpPmChanOchLBCMin.setStatus(_A)
_OchCtpPmChanOchLBCMax_Type=FloatHundredths
_OchCtpPmChanOchLBCMax_Object=MibTableColumn
ochCtpPmChanOchLBCMax=_OchCtpPmChanOchLBCMax_Object((1,3,6,1,4,1,21296,2,2,2,3,30,2,1,11),_OchCtpPmChanOchLBCMax_Type())
ochCtpPmChanOchLBCMax.setMaxAccess(_C)
if mibBuilder.loadTexts:ochCtpPmChanOchLBCMax.setStatus(_A)
_OchCtpPmChanOchLBCAve_Type=FloatHundredths
_OchCtpPmChanOchLBCAve_Object=MibTableColumn
ochCtpPmChanOchLBCAve=_OchCtpPmChanOchLBCAve_Object((1,3,6,1,4,1,21296,2,2,2,3,30,2,1,12),_OchCtpPmChanOchLBCAve_Type())
ochCtpPmChanOchLBCAve.setMaxAccess(_C)
if mibBuilder.loadTexts:ochCtpPmChanOchLBCAve.setStatus(_A)
_OchCtpPmChanOchQValueMin_Type=FloatHundredths
_OchCtpPmChanOchQValueMin_Object=MibTableColumn
ochCtpPmChanOchQValueMin=_OchCtpPmChanOchQValueMin_Object((1,3,6,1,4,1,21296,2,2,2,3,30,2,1,13),_OchCtpPmChanOchQValueMin_Type())
ochCtpPmChanOchQValueMin.setMaxAccess(_C)
if mibBuilder.loadTexts:ochCtpPmChanOchQValueMin.setStatus(_A)
_OchCtpPmChanOchQValueMax_Type=FloatHundredths
_OchCtpPmChanOchQValueMax_Object=MibTableColumn
ochCtpPmChanOchQValueMax=_OchCtpPmChanOchQValueMax_Object((1,3,6,1,4,1,21296,2,2,2,3,30,2,1,14),_OchCtpPmChanOchQValueMax_Type())
ochCtpPmChanOchQValueMax.setMaxAccess(_C)
if mibBuilder.loadTexts:ochCtpPmChanOchQValueMax.setStatus(_A)
_OchCtpPmChanOchQValueAve_Type=FloatHundredths
_OchCtpPmChanOchQValueAve_Object=MibTableColumn
ochCtpPmChanOchQValueAve=_OchCtpPmChanOchQValueAve_Object((1,3,6,1,4,1,21296,2,2,2,3,30,2,1,15),_OchCtpPmChanOchQValueAve_Type())
ochCtpPmChanOchQValueAve.setMaxAccess(_C)
if mibBuilder.loadTexts:ochCtpPmChanOchQValueAve.setStatus(_A)
_OchCtpPmChanOchCDMin_Type=FloatHundredths
_OchCtpPmChanOchCDMin_Object=MibTableColumn
ochCtpPmChanOchCDMin=_OchCtpPmChanOchCDMin_Object((1,3,6,1,4,1,21296,2,2,2,3,30,2,1,16),_OchCtpPmChanOchCDMin_Type())
ochCtpPmChanOchCDMin.setMaxAccess(_C)
if mibBuilder.loadTexts:ochCtpPmChanOchCDMin.setStatus(_A)
_OchCtpPmChanOchCDMax_Type=FloatHundredths
_OchCtpPmChanOchCDMax_Object=MibTableColumn
ochCtpPmChanOchCDMax=_OchCtpPmChanOchCDMax_Object((1,3,6,1,4,1,21296,2,2,2,3,30,2,1,17),_OchCtpPmChanOchCDMax_Type())
ochCtpPmChanOchCDMax.setMaxAccess(_C)
if mibBuilder.loadTexts:ochCtpPmChanOchCDMax.setStatus(_A)
_OchCtpPmChanOchCDAve_Type=FloatHundredths
_OchCtpPmChanOchCDAve_Object=MibTableColumn
ochCtpPmChanOchCDAve=_OchCtpPmChanOchCDAve_Object((1,3,6,1,4,1,21296,2,2,2,3,30,2,1,18),_OchCtpPmChanOchCDAve_Type())
ochCtpPmChanOchCDAve.setMaxAccess(_C)
if mibBuilder.loadTexts:ochCtpPmChanOchCDAve.setStatus(_A)
_OchCtpPmPmdMin_Type=FloatArbitraryPrecision
_OchCtpPmPmdMin_Object=MibTableColumn
ochCtpPmPmdMin=_OchCtpPmPmdMin_Object((1,3,6,1,4,1,21296,2,2,2,3,30,2,1,19),_OchCtpPmPmdMin_Type())
ochCtpPmPmdMin.setMaxAccess(_C)
if mibBuilder.loadTexts:ochCtpPmPmdMin.setStatus(_A)
_OchCtpPmPmdMax_Type=FloatArbitraryPrecision
_OchCtpPmPmdMax_Object=MibTableColumn
ochCtpPmPmdMax=_OchCtpPmPmdMax_Object((1,3,6,1,4,1,21296,2,2,2,3,30,2,1,20),_OchCtpPmPmdMax_Type())
ochCtpPmPmdMax.setMaxAccess(_C)
if mibBuilder.loadTexts:ochCtpPmPmdMax.setStatus(_A)
_OchCtpPmPmdAve_Type=FloatArbitraryPrecision
_OchCtpPmPmdAve_Object=MibTableColumn
ochCtpPmPmdAve=_OchCtpPmPmdAve_Object((1,3,6,1,4,1,21296,2,2,2,3,30,2,1,21),_OchCtpPmPmdAve_Type())
ochCtpPmPmdAve.setMaxAccess(_C)
if mibBuilder.loadTexts:ochCtpPmPmdAve.setStatus(_A)
_OchCtpPmSoPmdMin_Type=FloatArbitraryPrecision
_OchCtpPmSoPmdMin_Object=MibTableColumn
ochCtpPmSoPmdMin=_OchCtpPmSoPmdMin_Object((1,3,6,1,4,1,21296,2,2,2,3,30,2,1,22),_OchCtpPmSoPmdMin_Type())
ochCtpPmSoPmdMin.setMaxAccess(_C)
if mibBuilder.loadTexts:ochCtpPmSoPmdMin.setStatus(_A)
_OchCtpPmSoPmdMax_Type=FloatArbitraryPrecision
_OchCtpPmSoPmdMax_Object=MibTableColumn
ochCtpPmSoPmdMax=_OchCtpPmSoPmdMax_Object((1,3,6,1,4,1,21296,2,2,2,3,30,2,1,23),_OchCtpPmSoPmdMax_Type())
ochCtpPmSoPmdMax.setMaxAccess(_C)
if mibBuilder.loadTexts:ochCtpPmSoPmdMax.setStatus(_A)
_OchCtpPmSoPmdAve_Type=FloatArbitraryPrecision
_OchCtpPmSoPmdAve_Object=MibTableColumn
ochCtpPmSoPmdAve=_OchCtpPmSoPmdAve_Object((1,3,6,1,4,1,21296,2,2,2,3,30,2,1,24),_OchCtpPmSoPmdAve_Type())
ochCtpPmSoPmdAve.setMaxAccess(_C)
if mibBuilder.loadTexts:ochCtpPmSoPmdAve.setStatus(_A)
_OchCtpPmBerPreFecMin_Type=FloatArbitraryPrecision
_OchCtpPmBerPreFecMin_Object=MibTableColumn
ochCtpPmBerPreFecMin=_OchCtpPmBerPreFecMin_Object((1,3,6,1,4,1,21296,2,2,2,3,30,2,1,25),_OchCtpPmBerPreFecMin_Type())
ochCtpPmBerPreFecMin.setMaxAccess(_C)
if mibBuilder.loadTexts:ochCtpPmBerPreFecMin.setStatus(_A)
_OchCtpPmBerPreFecMax_Type=FloatArbitraryPrecision
_OchCtpPmBerPreFecMax_Object=MibTableColumn
ochCtpPmBerPreFecMax=_OchCtpPmBerPreFecMax_Object((1,3,6,1,4,1,21296,2,2,2,3,30,2,1,26),_OchCtpPmBerPreFecMax_Type())
ochCtpPmBerPreFecMax.setMaxAccess(_C)
if mibBuilder.loadTexts:ochCtpPmBerPreFecMax.setStatus(_A)
_OchCtpPmBerPreFecAve_Type=FloatArbitraryPrecision
_OchCtpPmBerPreFecAve_Object=MibTableColumn
ochCtpPmBerPreFecAve=_OchCtpPmBerPreFecAve_Object((1,3,6,1,4,1,21296,2,2,2,3,30,2,1,27),_OchCtpPmBerPreFecAve_Type())
ochCtpPmBerPreFecAve.setMaxAccess(_C)
if mibBuilder.loadTexts:ochCtpPmBerPreFecAve.setStatus(_A)
_OchCtpPmPhaseCorrectionMin_Type=FloatHundredths
_OchCtpPmPhaseCorrectionMin_Object=MibTableColumn
ochCtpPmPhaseCorrectionMin=_OchCtpPmPhaseCorrectionMin_Object((1,3,6,1,4,1,21296,2,2,2,3,30,2,1,28),_OchCtpPmPhaseCorrectionMin_Type())
ochCtpPmPhaseCorrectionMin.setMaxAccess(_C)
if mibBuilder.loadTexts:ochCtpPmPhaseCorrectionMin.setStatus(_A)
_OchCtpPmPhaseCorrectionMax_Type=FloatHundredths
_OchCtpPmPhaseCorrectionMax_Object=MibTableColumn
ochCtpPmPhaseCorrectionMax=_OchCtpPmPhaseCorrectionMax_Object((1,3,6,1,4,1,21296,2,2,2,3,30,2,1,29),_OchCtpPmPhaseCorrectionMax_Type())
ochCtpPmPhaseCorrectionMax.setMaxAccess(_C)
if mibBuilder.loadTexts:ochCtpPmPhaseCorrectionMax.setStatus(_A)
_OchCtpPmPhaseCorrectionAve_Type=FloatHundredths
_OchCtpPmPhaseCorrectionAve_Object=MibTableColumn
ochCtpPmPhaseCorrectionAve=_OchCtpPmPhaseCorrectionAve_Object((1,3,6,1,4,1,21296,2,2,2,3,30,2,1,30),_OchCtpPmPhaseCorrectionAve_Type())
ochCtpPmPhaseCorrectionAve.setMaxAccess(_C)
if mibBuilder.loadTexts:ochCtpPmPhaseCorrectionAve.setStatus(_A)
_OchCtpPmBerPostFecMin_Type=FloatArbitraryPrecision
_OchCtpPmBerPostFecMin_Object=MibTableColumn
ochCtpPmBerPostFecMin=_OchCtpPmBerPostFecMin_Object((1,3,6,1,4,1,21296,2,2,2,3,30,2,1,31),_OchCtpPmBerPostFecMin_Type())
ochCtpPmBerPostFecMin.setMaxAccess(_C)
if mibBuilder.loadTexts:ochCtpPmBerPostFecMin.setStatus(_A)
_OchCtpPmBerPostFecMax_Type=FloatArbitraryPrecision
_OchCtpPmBerPostFecMax_Object=MibTableColumn
ochCtpPmBerPostFecMax=_OchCtpPmBerPostFecMax_Object((1,3,6,1,4,1,21296,2,2,2,3,30,2,1,32),_OchCtpPmBerPostFecMax_Type())
ochCtpPmBerPostFecMax.setMaxAccess(_C)
if mibBuilder.loadTexts:ochCtpPmBerPostFecMax.setStatus(_A)
_OchCtpPmBerPostFecAve_Type=FloatArbitraryPrecision
_OchCtpPmBerPostFecAve_Object=MibTableColumn
ochCtpPmBerPostFecAve=_OchCtpPmBerPostFecAve_Object((1,3,6,1,4,1,21296,2,2,2,3,30,2,1,33),_OchCtpPmBerPostFecAve_Type())
ochCtpPmBerPostFecAve.setMaxAccess(_C)
if mibBuilder.loadTexts:ochCtpPmBerPostFecAve.setStatus(_A)
_OchCtpPmCWProc_Type=HCPerfIntervalCount
_OchCtpPmCWProc_Object=MibTableColumn
ochCtpPmCWProc=_OchCtpPmCWProc_Object((1,3,6,1,4,1,21296,2,2,2,3,30,2,1,34),_OchCtpPmCWProc_Type())
ochCtpPmCWProc.setMaxAccess(_C)
if mibBuilder.loadTexts:ochCtpPmCWProc.setStatus(_A)
_OchCtpPmUnCrctblCW_Type=HCPerfIntervalCount
_OchCtpPmUnCrctblCW_Object=MibTableColumn
ochCtpPmUnCrctblCW=_OchCtpPmUnCrctblCW_Object((1,3,6,1,4,1,21296,2,2,2,3,30,2,1,35),_OchCtpPmUnCrctblCW_Type())
ochCtpPmUnCrctblCW.setMaxAccess(_C)
if mibBuilder.loadTexts:ochCtpPmUnCrctblCW.setStatus(_A)
_OchCtpPmCrctdBits_Type=HCPerfIntervalCount
_OchCtpPmCrctdBits_Object=MibTableColumn
ochCtpPmCrctdBits=_OchCtpPmCrctdBits_Object((1,3,6,1,4,1,21296,2,2,2,3,30,2,1,36),_OchCtpPmCrctdBits_Type())
ochCtpPmCrctdBits.setMaxAccess(_C)
if mibBuilder.loadTexts:ochCtpPmCrctdBits.setStatus(_A)
_OchCtpPmConformance_ObjectIdentity=ObjectIdentity
ochCtpPmConformance=_OchCtpPmConformance_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,3,30,3))
_OchCtpPmCompliances_ObjectIdentity=ObjectIdentity
ochCtpPmCompliances=_OchCtpPmCompliances_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,3,30,3,1))
_OchCtpPmGroups_ObjectIdentity=ObjectIdentity
ochCtpPmGroups=_OchCtpPmGroups_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,3,30,3,2))
ochCtpPmGroup=ObjectGroup((1,3,6,1,4,1,21296,2,2,2,3,30,3,2,1))
ochCtpPmGroup.setObjects(*((_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q)))
if mibBuilder.loadTexts:ochCtpPmGroup.setStatus(_A)
ochCtpPmRealGroup=ObjectGroup((1,3,6,1,4,1,21296,2,2,2,3,30,3,2,2))
ochCtpPmRealGroup.setObjects(*((_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_x),(_B,_y),(_B,_z),(_B,_A0),(_B,_A1),(_B,_A2),(_B,_A3),(_B,_A4)))
if mibBuilder.loadTexts:ochCtpPmRealGroup.setStatus(_A)
ochCtpPmCompliance=ModuleCompliance((1,3,6,1,4,1,21296,2,2,2,3,30,3,1,1))
ochCtpPmCompliance.setObjects((_B,_A5))
if mibBuilder.loadTexts:ochCtpPmCompliance.setStatus(_A)
ochCtpPmRealCompliance=ModuleCompliance((1,3,6,1,4,1,21296,2,2,2,3,30,3,1,2))
ochCtpPmRealCompliance.setObjects((_B,_A6))
if mibBuilder.loadTexts:ochCtpPmRealCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ochCtpPmMIB':ochCtpPmMIB,'ochCtpPmRealTable':ochCtpPmRealTable,'ochCtpPmRealEntry':ochCtpPmRealEntry,_r:ochCtpPmRealChanOchOpt,_s:ochCtpPmRealChanOchOpr,_t:ochCtpPmRealChanOchLBC,_u:ochCtpPmRealChanOchMeasuredWavelength,_v:ochCtpPmRealChanOchQValue,_w:ochCtpPmRealChanOchCD,_x:ochCtpPmRealPmd,_y:ochCtpPmRealSoPmd,_z:ochCtpPmBerPreFec,_A0:ochCtpPmRealPhaseCorrection,_A1:ochCtpPmRealBerPostFec,_A2:ochCtpPmRealCWProc,_A3:ochCtpPmRealUnCrctblCW,_A4:ochCtpPmRealCrctdBits,'ochCtpPmTable':ochCtpPmTable,'ochCtpPmEntry':ochCtpPmEntry,_H:ochCtpPmTimestamp,_G:ochCtpPmSampleDuration,_J:ochCtpPmValidity,_K:ochCtpPmChanOchOptMin,_L:ochCtpPmChanOchOptMax,_M:ochCtpPmChanOchOptAve,_N:ochCtpPmChanOchOprMin,_O:ochCtpPmChanOchOprMax,_P:ochCtpPmChanOchOprAve,_Q:ochCtpPmChanOchLBCMin,_R:ochCtpPmChanOchLBCMax,_S:ochCtpPmChanOchLBCAve,_T:ochCtpPmChanOchQValueMin,_U:ochCtpPmChanOchQValueMax,_V:ochCtpPmChanOchQValueAve,_W:ochCtpPmChanOchCDMin,_X:ochCtpPmChanOchCDMax,_Y:ochCtpPmChanOchCDAve,_Z:ochCtpPmPmdMin,_a:ochCtpPmPmdMax,_b:ochCtpPmPmdAve,_c:ochCtpPmSoPmdMin,_d:ochCtpPmSoPmdMax,_e:ochCtpPmSoPmdAve,_f:ochCtpPmBerPreFecMin,_g:ochCtpPmBerPreFecMax,_h:ochCtpPmBerPreFecAve,_i:ochCtpPmPhaseCorrectionMin,_j:ochCtpPmPhaseCorrectionMax,_k:ochCtpPmPhaseCorrectionAve,_l:ochCtpPmBerPostFecMin,_m:ochCtpPmBerPostFecMax,_n:ochCtpPmBerPostFecAve,_o:ochCtpPmCWProc,_p:ochCtpPmUnCrctblCW,_q:ochCtpPmCrctdBits,'ochCtpPmConformance':ochCtpPmConformance,'ochCtpPmCompliances':ochCtpPmCompliances,'ochCtpPmCompliance':ochCtpPmCompliance,'ochCtpPmRealCompliance':ochCtpPmRealCompliance,'ochCtpPmGroups':ochCtpPmGroups,_A5:ochCtpPmGroup,_A6:ochCtpPmRealGroup})