_n='lmOchPtpPmRealGroup'
_m='lmOchPtpPmGroup'
_l='lmOchPtpPmRealChanOchSoPmd'
_k='lmOchPtpPmRealChanOchPmd'
_j='lmOchPtpPmRealChanOchQ'
_i='lmOchPtpPmRealChanOchChromaticDispersion'
_h='lmOchPtpPmRealChanOchLBC'
_g='lmOchPtpPmRealChanOchOpr'
_f='lmOchPtpPmRealChanOchOpt'
_e='lmOchPtpPmChanOchSoPmdAve'
_d='lmOchPtpPmChanOchSoPmdMax'
_c='lmOchPtpPmChanOchSoPmdMin'
_b='lmOchPtpPmChanOchPmdAve'
_a='lmOchPtpPmChanOchPmdMax'
_Z='lmOchPtpPmChanOchPmdMin'
_Y='lmOchPtpPmChanOchQAve'
_X='lmOchPtpPmChanOchQMax'
_W='lmOchPtpPmChanOchQMin'
_V='lmOchPtpPmChanOchChromaticDispersionAve'
_U='lmOchPtpPmChanOchChromaticDispersionMax'
_T='lmOchPtpPmChanOchChromaticDispersionMin'
_S='lmOchPtpPmChanOchLBCAve'
_R='lmOchPtpPmChanOchLBCMax'
_Q='lmOchPtpPmChanOchLBCMin'
_P='lmOchPtpPmChanOchOprAve'
_O='lmOchPtpPmChanOchOprMax'
_N='lmOchPtpPmChanOchOprMin'
_M='lmOchPtpPmChanOchOptAve'
_L='lmOchPtpPmChanOchOptMax'
_K='lmOchPtpPmChanOchOptMin'
_J='lmOchPtpPmValidity'
_I='not-accessible'
_H='lmOchPtpPmTimestamp'
_G='lmOchPtpPmSampleDuration'
_F='Integer32'
_E='ifIndex'
_D='IF-MIB'
_C='read-only'
_B='INFINERA-PM-LMOCHPTP-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_D,_E)
perfMon,=mibBuilder.importSymbols('INFINERA-REG-MIB','perfMon')
FloatArbitraryPrecision,FloatHundredths=mibBuilder.importSymbols('INFINERA-TC-MIB','FloatArbitraryPrecision','FloatHundredths')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
lmOchPtpPmMIB=ModuleIdentity((1,3,6,1,4,1,21296,2,2,2,3,24))
if mibBuilder.loadTexts:lmOchPtpPmMIB.setRevisions(('2011-05-23 00:00',))
_LmOchPtpPmRealTable_Object=MibTable
lmOchPtpPmRealTable=_LmOchPtpPmRealTable_Object((1,3,6,1,4,1,21296,2,2,2,3,24,1))
if mibBuilder.loadTexts:lmOchPtpPmRealTable.setStatus(_A)
_LmOchPtpPmRealEntry_Object=MibTableRow
lmOchPtpPmRealEntry=_LmOchPtpPmRealEntry_Object((1,3,6,1,4,1,21296,2,2,2,3,24,1,1))
lmOchPtpPmRealEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:lmOchPtpPmRealEntry.setStatus(_A)
_LmOchPtpPmRealChanOchOpt_Type=FloatHundredths
_LmOchPtpPmRealChanOchOpt_Object=MibTableColumn
lmOchPtpPmRealChanOchOpt=_LmOchPtpPmRealChanOchOpt_Object((1,3,6,1,4,1,21296,2,2,2,3,24,1,1,1),_LmOchPtpPmRealChanOchOpt_Type())
lmOchPtpPmRealChanOchOpt.setMaxAccess(_C)
if mibBuilder.loadTexts:lmOchPtpPmRealChanOchOpt.setStatus(_A)
_LmOchPtpPmRealChanOchOpr_Type=FloatHundredths
_LmOchPtpPmRealChanOchOpr_Object=MibTableColumn
lmOchPtpPmRealChanOchOpr=_LmOchPtpPmRealChanOchOpr_Object((1,3,6,1,4,1,21296,2,2,2,3,24,1,1,2),_LmOchPtpPmRealChanOchOpr_Type())
lmOchPtpPmRealChanOchOpr.setMaxAccess(_C)
if mibBuilder.loadTexts:lmOchPtpPmRealChanOchOpr.setStatus(_A)
_LmOchPtpPmRealChanOchLBC_Type=FloatHundredths
_LmOchPtpPmRealChanOchLBC_Object=MibTableColumn
lmOchPtpPmRealChanOchLBC=_LmOchPtpPmRealChanOchLBC_Object((1,3,6,1,4,1,21296,2,2,2,3,24,1,1,3),_LmOchPtpPmRealChanOchLBC_Type())
lmOchPtpPmRealChanOchLBC.setMaxAccess(_C)
if mibBuilder.loadTexts:lmOchPtpPmRealChanOchLBC.setStatus(_A)
_LmOchPtpPmRealChanOchChromaticDispersion_Type=FloatHundredths
_LmOchPtpPmRealChanOchChromaticDispersion_Object=MibTableColumn
lmOchPtpPmRealChanOchChromaticDispersion=_LmOchPtpPmRealChanOchChromaticDispersion_Object((1,3,6,1,4,1,21296,2,2,2,3,24,1,1,4),_LmOchPtpPmRealChanOchChromaticDispersion_Type())
lmOchPtpPmRealChanOchChromaticDispersion.setMaxAccess(_C)
if mibBuilder.loadTexts:lmOchPtpPmRealChanOchChromaticDispersion.setStatus(_A)
_LmOchPtpPmRealChanOchQ_Type=FloatHundredths
_LmOchPtpPmRealChanOchQ_Object=MibTableColumn
lmOchPtpPmRealChanOchQ=_LmOchPtpPmRealChanOchQ_Object((1,3,6,1,4,1,21296,2,2,2,3,24,1,1,5),_LmOchPtpPmRealChanOchQ_Type())
lmOchPtpPmRealChanOchQ.setMaxAccess(_C)
if mibBuilder.loadTexts:lmOchPtpPmRealChanOchQ.setStatus(_A)
_LmOchPtpPmRealChanOchPmd_Type=FloatArbitraryPrecision
_LmOchPtpPmRealChanOchPmd_Object=MibTableColumn
lmOchPtpPmRealChanOchPmd=_LmOchPtpPmRealChanOchPmd_Object((1,3,6,1,4,1,21296,2,2,2,3,24,1,1,6),_LmOchPtpPmRealChanOchPmd_Type())
lmOchPtpPmRealChanOchPmd.setMaxAccess(_C)
if mibBuilder.loadTexts:lmOchPtpPmRealChanOchPmd.setStatus(_A)
_LmOchPtpPmRealChanOchSoPmd_Type=FloatArbitraryPrecision
_LmOchPtpPmRealChanOchSoPmd_Object=MibTableColumn
lmOchPtpPmRealChanOchSoPmd=_LmOchPtpPmRealChanOchSoPmd_Object((1,3,6,1,4,1,21296,2,2,2,3,24,1,1,7),_LmOchPtpPmRealChanOchSoPmd_Type())
lmOchPtpPmRealChanOchSoPmd.setMaxAccess(_C)
if mibBuilder.loadTexts:lmOchPtpPmRealChanOchSoPmd.setStatus(_A)
_LmOchPtpPmTable_Object=MibTable
lmOchPtpPmTable=_LmOchPtpPmTable_Object((1,3,6,1,4,1,21296,2,2,2,3,24,2))
if mibBuilder.loadTexts:lmOchPtpPmTable.setStatus(_A)
_LmOchPtpPmEntry_Object=MibTableRow
lmOchPtpPmEntry=_LmOchPtpPmEntry_Object((1,3,6,1,4,1,21296,2,2,2,3,24,2,1))
lmOchPtpPmEntry.setIndexNames((0,_D,_E),(0,_B,_G),(0,_B,_H))
if mibBuilder.loadTexts:lmOchPtpPmEntry.setStatus(_A)
class _LmOchPtpPmTimestamp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_LmOchPtpPmTimestamp_Type.__name__=_F
_LmOchPtpPmTimestamp_Object=MibTableColumn
lmOchPtpPmTimestamp=_LmOchPtpPmTimestamp_Object((1,3,6,1,4,1,21296,2,2,2,3,24,2,1,1),_LmOchPtpPmTimestamp_Type())
lmOchPtpPmTimestamp.setMaxAccess(_I)
if mibBuilder.loadTexts:lmOchPtpPmTimestamp.setStatus(_A)
class _LmOchPtpPmSampleDuration_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('fifteenMinutes',1),('day',2)))
_LmOchPtpPmSampleDuration_Type.__name__=_F
_LmOchPtpPmSampleDuration_Object=MibTableColumn
lmOchPtpPmSampleDuration=_LmOchPtpPmSampleDuration_Object((1,3,6,1,4,1,21296,2,2,2,3,24,2,1,2),_LmOchPtpPmSampleDuration_Type())
lmOchPtpPmSampleDuration.setMaxAccess(_I)
if mibBuilder.loadTexts:lmOchPtpPmSampleDuration.setStatus(_A)
_LmOchPtpPmValidity_Type=TruthValue
_LmOchPtpPmValidity_Object=MibTableColumn
lmOchPtpPmValidity=_LmOchPtpPmValidity_Object((1,3,6,1,4,1,21296,2,2,2,3,24,2,1,3),_LmOchPtpPmValidity_Type())
lmOchPtpPmValidity.setMaxAccess(_C)
if mibBuilder.loadTexts:lmOchPtpPmValidity.setStatus(_A)
_LmOchPtpPmChanOchOptMin_Type=FloatHundredths
_LmOchPtpPmChanOchOptMin_Object=MibTableColumn
lmOchPtpPmChanOchOptMin=_LmOchPtpPmChanOchOptMin_Object((1,3,6,1,4,1,21296,2,2,2,3,24,2,1,4),_LmOchPtpPmChanOchOptMin_Type())
lmOchPtpPmChanOchOptMin.setMaxAccess(_C)
if mibBuilder.loadTexts:lmOchPtpPmChanOchOptMin.setStatus(_A)
_LmOchPtpPmChanOchOptMax_Type=FloatHundredths
_LmOchPtpPmChanOchOptMax_Object=MibTableColumn
lmOchPtpPmChanOchOptMax=_LmOchPtpPmChanOchOptMax_Object((1,3,6,1,4,1,21296,2,2,2,3,24,2,1,5),_LmOchPtpPmChanOchOptMax_Type())
lmOchPtpPmChanOchOptMax.setMaxAccess(_C)
if mibBuilder.loadTexts:lmOchPtpPmChanOchOptMax.setStatus(_A)
_LmOchPtpPmChanOchOptAve_Type=FloatHundredths
_LmOchPtpPmChanOchOptAve_Object=MibTableColumn
lmOchPtpPmChanOchOptAve=_LmOchPtpPmChanOchOptAve_Object((1,3,6,1,4,1,21296,2,2,2,3,24,2,1,6),_LmOchPtpPmChanOchOptAve_Type())
lmOchPtpPmChanOchOptAve.setMaxAccess(_C)
if mibBuilder.loadTexts:lmOchPtpPmChanOchOptAve.setStatus(_A)
_LmOchPtpPmChanOchOprMin_Type=FloatHundredths
_LmOchPtpPmChanOchOprMin_Object=MibTableColumn
lmOchPtpPmChanOchOprMin=_LmOchPtpPmChanOchOprMin_Object((1,3,6,1,4,1,21296,2,2,2,3,24,2,1,7),_LmOchPtpPmChanOchOprMin_Type())
lmOchPtpPmChanOchOprMin.setMaxAccess(_C)
if mibBuilder.loadTexts:lmOchPtpPmChanOchOprMin.setStatus(_A)
_LmOchPtpPmChanOchOprMax_Type=FloatHundredths
_LmOchPtpPmChanOchOprMax_Object=MibTableColumn
lmOchPtpPmChanOchOprMax=_LmOchPtpPmChanOchOprMax_Object((1,3,6,1,4,1,21296,2,2,2,3,24,2,1,8),_LmOchPtpPmChanOchOprMax_Type())
lmOchPtpPmChanOchOprMax.setMaxAccess(_C)
if mibBuilder.loadTexts:lmOchPtpPmChanOchOprMax.setStatus(_A)
_LmOchPtpPmChanOchOprAve_Type=FloatHundredths
_LmOchPtpPmChanOchOprAve_Object=MibTableColumn
lmOchPtpPmChanOchOprAve=_LmOchPtpPmChanOchOprAve_Object((1,3,6,1,4,1,21296,2,2,2,3,24,2,1,9),_LmOchPtpPmChanOchOprAve_Type())
lmOchPtpPmChanOchOprAve.setMaxAccess(_C)
if mibBuilder.loadTexts:lmOchPtpPmChanOchOprAve.setStatus(_A)
_LmOchPtpPmChanOchLBCMin_Type=FloatHundredths
_LmOchPtpPmChanOchLBCMin_Object=MibTableColumn
lmOchPtpPmChanOchLBCMin=_LmOchPtpPmChanOchLBCMin_Object((1,3,6,1,4,1,21296,2,2,2,3,24,2,1,10),_LmOchPtpPmChanOchLBCMin_Type())
lmOchPtpPmChanOchLBCMin.setMaxAccess(_C)
if mibBuilder.loadTexts:lmOchPtpPmChanOchLBCMin.setStatus(_A)
_LmOchPtpPmChanOchLBCMax_Type=FloatHundredths
_LmOchPtpPmChanOchLBCMax_Object=MibTableColumn
lmOchPtpPmChanOchLBCMax=_LmOchPtpPmChanOchLBCMax_Object((1,3,6,1,4,1,21296,2,2,2,3,24,2,1,11),_LmOchPtpPmChanOchLBCMax_Type())
lmOchPtpPmChanOchLBCMax.setMaxAccess(_C)
if mibBuilder.loadTexts:lmOchPtpPmChanOchLBCMax.setStatus(_A)
_LmOchPtpPmChanOchLBCAve_Type=FloatHundredths
_LmOchPtpPmChanOchLBCAve_Object=MibTableColumn
lmOchPtpPmChanOchLBCAve=_LmOchPtpPmChanOchLBCAve_Object((1,3,6,1,4,1,21296,2,2,2,3,24,2,1,12),_LmOchPtpPmChanOchLBCAve_Type())
lmOchPtpPmChanOchLBCAve.setMaxAccess(_C)
if mibBuilder.loadTexts:lmOchPtpPmChanOchLBCAve.setStatus(_A)
_LmOchPtpPmChanOchChromaticDispersionMin_Type=FloatHundredths
_LmOchPtpPmChanOchChromaticDispersionMin_Object=MibTableColumn
lmOchPtpPmChanOchChromaticDispersionMin=_LmOchPtpPmChanOchChromaticDispersionMin_Object((1,3,6,1,4,1,21296,2,2,2,3,24,2,1,13),_LmOchPtpPmChanOchChromaticDispersionMin_Type())
lmOchPtpPmChanOchChromaticDispersionMin.setMaxAccess(_C)
if mibBuilder.loadTexts:lmOchPtpPmChanOchChromaticDispersionMin.setStatus(_A)
_LmOchPtpPmChanOchChromaticDispersionMax_Type=FloatHundredths
_LmOchPtpPmChanOchChromaticDispersionMax_Object=MibTableColumn
lmOchPtpPmChanOchChromaticDispersionMax=_LmOchPtpPmChanOchChromaticDispersionMax_Object((1,3,6,1,4,1,21296,2,2,2,3,24,2,1,14),_LmOchPtpPmChanOchChromaticDispersionMax_Type())
lmOchPtpPmChanOchChromaticDispersionMax.setMaxAccess(_C)
if mibBuilder.loadTexts:lmOchPtpPmChanOchChromaticDispersionMax.setStatus(_A)
_LmOchPtpPmChanOchChromaticDispersionAve_Type=FloatHundredths
_LmOchPtpPmChanOchChromaticDispersionAve_Object=MibTableColumn
lmOchPtpPmChanOchChromaticDispersionAve=_LmOchPtpPmChanOchChromaticDispersionAve_Object((1,3,6,1,4,1,21296,2,2,2,3,24,2,1,15),_LmOchPtpPmChanOchChromaticDispersionAve_Type())
lmOchPtpPmChanOchChromaticDispersionAve.setMaxAccess(_C)
if mibBuilder.loadTexts:lmOchPtpPmChanOchChromaticDispersionAve.setStatus(_A)
_LmOchPtpPmChanOchQMin_Type=FloatHundredths
_LmOchPtpPmChanOchQMin_Object=MibTableColumn
lmOchPtpPmChanOchQMin=_LmOchPtpPmChanOchQMin_Object((1,3,6,1,4,1,21296,2,2,2,3,24,2,1,16),_LmOchPtpPmChanOchQMin_Type())
lmOchPtpPmChanOchQMin.setMaxAccess(_C)
if mibBuilder.loadTexts:lmOchPtpPmChanOchQMin.setStatus(_A)
_LmOchPtpPmChanOchQMax_Type=FloatHundredths
_LmOchPtpPmChanOchQMax_Object=MibTableColumn
lmOchPtpPmChanOchQMax=_LmOchPtpPmChanOchQMax_Object((1,3,6,1,4,1,21296,2,2,2,3,24,2,1,17),_LmOchPtpPmChanOchQMax_Type())
lmOchPtpPmChanOchQMax.setMaxAccess(_C)
if mibBuilder.loadTexts:lmOchPtpPmChanOchQMax.setStatus(_A)
_LmOchPtpPmChanOchQAve_Type=FloatHundredths
_LmOchPtpPmChanOchQAve_Object=MibTableColumn
lmOchPtpPmChanOchQAve=_LmOchPtpPmChanOchQAve_Object((1,3,6,1,4,1,21296,2,2,2,3,24,2,1,18),_LmOchPtpPmChanOchQAve_Type())
lmOchPtpPmChanOchQAve.setMaxAccess(_C)
if mibBuilder.loadTexts:lmOchPtpPmChanOchQAve.setStatus(_A)
_LmOchPtpPmChanOchPmdMin_Type=FloatArbitraryPrecision
_LmOchPtpPmChanOchPmdMin_Object=MibTableColumn
lmOchPtpPmChanOchPmdMin=_LmOchPtpPmChanOchPmdMin_Object((1,3,6,1,4,1,21296,2,2,2,3,24,2,1,19),_LmOchPtpPmChanOchPmdMin_Type())
lmOchPtpPmChanOchPmdMin.setMaxAccess(_C)
if mibBuilder.loadTexts:lmOchPtpPmChanOchPmdMin.setStatus(_A)
_LmOchPtpPmChanOchPmdMax_Type=FloatArbitraryPrecision
_LmOchPtpPmChanOchPmdMax_Object=MibTableColumn
lmOchPtpPmChanOchPmdMax=_LmOchPtpPmChanOchPmdMax_Object((1,3,6,1,4,1,21296,2,2,2,3,24,2,1,20),_LmOchPtpPmChanOchPmdMax_Type())
lmOchPtpPmChanOchPmdMax.setMaxAccess(_C)
if mibBuilder.loadTexts:lmOchPtpPmChanOchPmdMax.setStatus(_A)
_LmOchPtpPmChanOchPmdAve_Type=FloatArbitraryPrecision
_LmOchPtpPmChanOchPmdAve_Object=MibTableColumn
lmOchPtpPmChanOchPmdAve=_LmOchPtpPmChanOchPmdAve_Object((1,3,6,1,4,1,21296,2,2,2,3,24,2,1,21),_LmOchPtpPmChanOchPmdAve_Type())
lmOchPtpPmChanOchPmdAve.setMaxAccess(_C)
if mibBuilder.loadTexts:lmOchPtpPmChanOchPmdAve.setStatus(_A)
_LmOchPtpPmChanOchSoPmdMin_Type=FloatArbitraryPrecision
_LmOchPtpPmChanOchSoPmdMin_Object=MibTableColumn
lmOchPtpPmChanOchSoPmdMin=_LmOchPtpPmChanOchSoPmdMin_Object((1,3,6,1,4,1,21296,2,2,2,3,24,2,1,22),_LmOchPtpPmChanOchSoPmdMin_Type())
lmOchPtpPmChanOchSoPmdMin.setMaxAccess(_C)
if mibBuilder.loadTexts:lmOchPtpPmChanOchSoPmdMin.setStatus(_A)
_LmOchPtpPmChanOchSoPmdMax_Type=FloatArbitraryPrecision
_LmOchPtpPmChanOchSoPmdMax_Object=MibTableColumn
lmOchPtpPmChanOchSoPmdMax=_LmOchPtpPmChanOchSoPmdMax_Object((1,3,6,1,4,1,21296,2,2,2,3,24,2,1,23),_LmOchPtpPmChanOchSoPmdMax_Type())
lmOchPtpPmChanOchSoPmdMax.setMaxAccess(_C)
if mibBuilder.loadTexts:lmOchPtpPmChanOchSoPmdMax.setStatus(_A)
_LmOchPtpPmChanOchSoPmdAve_Type=FloatArbitraryPrecision
_LmOchPtpPmChanOchSoPmdAve_Object=MibTableColumn
lmOchPtpPmChanOchSoPmdAve=_LmOchPtpPmChanOchSoPmdAve_Object((1,3,6,1,4,1,21296,2,2,2,3,24,2,1,24),_LmOchPtpPmChanOchSoPmdAve_Type())
lmOchPtpPmChanOchSoPmdAve.setMaxAccess(_C)
if mibBuilder.loadTexts:lmOchPtpPmChanOchSoPmdAve.setStatus(_A)
_LmOchPtpPmConformance_ObjectIdentity=ObjectIdentity
lmOchPtpPmConformance=_LmOchPtpPmConformance_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,3,24,3))
_LmOchPtpPmCompliances_ObjectIdentity=ObjectIdentity
lmOchPtpPmCompliances=_LmOchPtpPmCompliances_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,3,24,3,1))
_LmOchPtpPmGroups_ObjectIdentity=ObjectIdentity
lmOchPtpPmGroups=_LmOchPtpPmGroups_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,3,24,3,2))
lmOchPtpPmGroup=ObjectGroup((1,3,6,1,4,1,21296,2,2,2,3,24,3,2,1))
lmOchPtpPmGroup.setObjects(*((_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e)))
if mibBuilder.loadTexts:lmOchPtpPmGroup.setStatus(_A)
lmOchPtpPmRealGroup=ObjectGroup((1,3,6,1,4,1,21296,2,2,2,3,24,3,2,2))
lmOchPtpPmRealGroup.setObjects(*((_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l)))
if mibBuilder.loadTexts:lmOchPtpPmRealGroup.setStatus(_A)
lmOchPtpPmCompliance=ModuleCompliance((1,3,6,1,4,1,21296,2,2,2,3,24,3,1,1))
lmOchPtpPmCompliance.setObjects((_B,_m))
if mibBuilder.loadTexts:lmOchPtpPmCompliance.setStatus(_A)
lmOchPtpPmRealCompliance=ModuleCompliance((1,3,6,1,4,1,21296,2,2,2,3,24,3,1,2))
lmOchPtpPmRealCompliance.setObjects((_B,_n))
if mibBuilder.loadTexts:lmOchPtpPmRealCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'lmOchPtpPmMIB':lmOchPtpPmMIB,'lmOchPtpPmRealTable':lmOchPtpPmRealTable,'lmOchPtpPmRealEntry':lmOchPtpPmRealEntry,_f:lmOchPtpPmRealChanOchOpt,_g:lmOchPtpPmRealChanOchOpr,_h:lmOchPtpPmRealChanOchLBC,_i:lmOchPtpPmRealChanOchChromaticDispersion,_j:lmOchPtpPmRealChanOchQ,_k:lmOchPtpPmRealChanOchPmd,_l:lmOchPtpPmRealChanOchSoPmd,'lmOchPtpPmTable':lmOchPtpPmTable,'lmOchPtpPmEntry':lmOchPtpPmEntry,_H:lmOchPtpPmTimestamp,_G:lmOchPtpPmSampleDuration,_J:lmOchPtpPmValidity,_K:lmOchPtpPmChanOchOptMin,_L:lmOchPtpPmChanOchOptMax,_M:lmOchPtpPmChanOchOptAve,_N:lmOchPtpPmChanOchOprMin,_O:lmOchPtpPmChanOchOprMax,_P:lmOchPtpPmChanOchOprAve,_Q:lmOchPtpPmChanOchLBCMin,_R:lmOchPtpPmChanOchLBCMax,_S:lmOchPtpPmChanOchLBCAve,_T:lmOchPtpPmChanOchChromaticDispersionMin,_U:lmOchPtpPmChanOchChromaticDispersionMax,_V:lmOchPtpPmChanOchChromaticDispersionAve,_W:lmOchPtpPmChanOchQMin,_X:lmOchPtpPmChanOchQMax,_Y:lmOchPtpPmChanOchQAve,_Z:lmOchPtpPmChanOchPmdMin,_a:lmOchPtpPmChanOchPmdMax,_b:lmOchPtpPmChanOchPmdAve,_c:lmOchPtpPmChanOchSoPmdMin,_d:lmOchPtpPmChanOchSoPmdMax,_e:lmOchPtpPmChanOchSoPmdAve,'lmOchPtpPmConformance':lmOchPtpPmConformance,'lmOchPtpPmCompliances':lmOchPtpPmCompliances,'lmOchPtpPmCompliance':lmOchPtpPmCompliance,'lmOchPtpPmRealCompliance':lmOchPtpPmRealCompliance,'lmOchPtpPmGroups':lmOchPtpPmGroups,_m:lmOchPtpPmGroup,_n:lmOchPtpPmRealGroup})