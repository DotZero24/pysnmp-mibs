_t='ofxScgPtpPmRealGroup'
_s='ofxScgPtpPmGroup'
_r='ofxScgPtpPmRealBerPreFec'
_q='ofxScgPtpPmRealQPreFec'
_p='ofxScgPtpPmRealRxEdfaLbc'
_o='ofxScgPtpPmRealRxEdfaOpt'
_n='ofxScgPtpPmRealRxEdfaOpr'
_m='ofxScgPtpPmRealTxEdfaLbc'
_l='ofxScgPtpPmRealTxEdfaOpt'
_k='ofxScgPtpPmRealTxEdfaOpr'
_j='ofxScgPtpPmRealChanScgOpr'
_i='ofxScgPtpPmRealChanScgOpt'
_h='ofxScgPtpPmBerPreFecAve'
_g='ofxScgPtpPmBerPreFecMax'
_f='ofxScgPtpPmBerPreFecMin'
_e='ofxScgPtpPmQPreFecAve'
_d='ofxScgPtpPmQPreFecMax'
_c='ofxScgPtpPmQPreFecMin'
_b='ofxScgPtpPmRxEdfaLbcAve'
_a='ofxScgPtpPmRxEdfaLbcMax'
_Z='ofxScgPtpPmRxEdfaLbcMin'
_Y='ofxScgPtpPmRxEdfaOptAve'
_X='ofxScgPtpPmRxEdfaOptMax'
_W='ofxScgPtpPmRxEdfaOptMin'
_V='ofxScgPtpPmRxEdfaOprAve'
_U='ofxScgPtpPmRxEdfaOprMax'
_T='ofxScgPtpPmRxEdfaOprMin'
_S='ofxScgPtpPmTxEdfaLbcAve'
_R='ofxScgPtpPmTxEdfaLbcMax'
_Q='ofxScgPtpPmTxEdfaLbcMin'
_P='ofxScgPtpPmTxEdfaOptAve'
_O='ofxScgPtpPmTxEdfaOptMax'
_N='ofxScgPtpPmTxEdfaOptMin'
_M='ofxScgPtpPmTxEdfaOprAve'
_L='ofxScgPtpPmTxEdfaOprMax'
_K='ofxScgPtpPmTxEdfaOprMin'
_J='ofxScgPtpPmValidity'
_I='ofxScgPtpPmSampleDuration'
_H='ofxScgPtpPmTimestamp'
_G='not-accessible'
_F='Integer32'
_E='ifIndex'
_D='IF-MIB'
_C='read-only'
_B='INFINERA-PM-OFXSCGPTP-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_D,_E)
perfMon,=mibBuilder.importSymbols('INFINERA-REG-MIB','perfMon')
FloatHundredths,=mibBuilder.importSymbols('INFINERA-TC-MIB','FloatHundredths')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
ofxScgPtpPmMIB=ModuleIdentity((1,3,6,1,4,1,21296,2,2,2,3,39))
if mibBuilder.loadTexts:ofxScgPtpPmMIB.setRevisions(('2013-10-08 00:00',))
_OfxScgPtpPmRealTable_Object=MibTable
ofxScgPtpPmRealTable=_OfxScgPtpPmRealTable_Object((1,3,6,1,4,1,21296,2,2,2,3,39,1))
if mibBuilder.loadTexts:ofxScgPtpPmRealTable.setStatus(_A)
_OfxScgPtpPmRealEntry_Object=MibTableRow
ofxScgPtpPmRealEntry=_OfxScgPtpPmRealEntry_Object((1,3,6,1,4,1,21296,2,2,2,3,39,1,1))
ofxScgPtpPmRealEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:ofxScgPtpPmRealEntry.setStatus(_A)
_OfxScgPtpPmRealChanScgOpt_Type=FloatHundredths
_OfxScgPtpPmRealChanScgOpt_Object=MibTableColumn
ofxScgPtpPmRealChanScgOpt=_OfxScgPtpPmRealChanScgOpt_Object((1,3,6,1,4,1,21296,2,2,2,3,39,1,1,1),_OfxScgPtpPmRealChanScgOpt_Type())
ofxScgPtpPmRealChanScgOpt.setMaxAccess(_C)
if mibBuilder.loadTexts:ofxScgPtpPmRealChanScgOpt.setStatus(_A)
_OfxScgPtpPmRealChanScgOpr_Type=FloatHundredths
_OfxScgPtpPmRealChanScgOpr_Object=MibTableColumn
ofxScgPtpPmRealChanScgOpr=_OfxScgPtpPmRealChanScgOpr_Object((1,3,6,1,4,1,21296,2,2,2,3,39,1,1,2),_OfxScgPtpPmRealChanScgOpr_Type())
ofxScgPtpPmRealChanScgOpr.setMaxAccess(_C)
if mibBuilder.loadTexts:ofxScgPtpPmRealChanScgOpr.setStatus(_A)
_OfxScgPtpPmRealTxEdfaOpr_Type=FloatHundredths
_OfxScgPtpPmRealTxEdfaOpr_Object=MibTableColumn
ofxScgPtpPmRealTxEdfaOpr=_OfxScgPtpPmRealTxEdfaOpr_Object((1,3,6,1,4,1,21296,2,2,2,3,39,1,1,3),_OfxScgPtpPmRealTxEdfaOpr_Type())
ofxScgPtpPmRealTxEdfaOpr.setMaxAccess(_C)
if mibBuilder.loadTexts:ofxScgPtpPmRealTxEdfaOpr.setStatus(_A)
_OfxScgPtpPmRealTxEdfaOpt_Type=FloatHundredths
_OfxScgPtpPmRealTxEdfaOpt_Object=MibTableColumn
ofxScgPtpPmRealTxEdfaOpt=_OfxScgPtpPmRealTxEdfaOpt_Object((1,3,6,1,4,1,21296,2,2,2,3,39,1,1,4),_OfxScgPtpPmRealTxEdfaOpt_Type())
ofxScgPtpPmRealTxEdfaOpt.setMaxAccess(_C)
if mibBuilder.loadTexts:ofxScgPtpPmRealTxEdfaOpt.setStatus(_A)
_OfxScgPtpPmRealTxEdfaLbc_Type=FloatHundredths
_OfxScgPtpPmRealTxEdfaLbc_Object=MibTableColumn
ofxScgPtpPmRealTxEdfaLbc=_OfxScgPtpPmRealTxEdfaLbc_Object((1,3,6,1,4,1,21296,2,2,2,3,39,1,1,5),_OfxScgPtpPmRealTxEdfaLbc_Type())
ofxScgPtpPmRealTxEdfaLbc.setMaxAccess(_C)
if mibBuilder.loadTexts:ofxScgPtpPmRealTxEdfaLbc.setStatus(_A)
_OfxScgPtpPmRealRxEdfaOpr_Type=FloatHundredths
_OfxScgPtpPmRealRxEdfaOpr_Object=MibTableColumn
ofxScgPtpPmRealRxEdfaOpr=_OfxScgPtpPmRealRxEdfaOpr_Object((1,3,6,1,4,1,21296,2,2,2,3,39,1,1,6),_OfxScgPtpPmRealRxEdfaOpr_Type())
ofxScgPtpPmRealRxEdfaOpr.setMaxAccess(_C)
if mibBuilder.loadTexts:ofxScgPtpPmRealRxEdfaOpr.setStatus(_A)
_OfxScgPtpPmRealRxEdfaOpt_Type=FloatHundredths
_OfxScgPtpPmRealRxEdfaOpt_Object=MibTableColumn
ofxScgPtpPmRealRxEdfaOpt=_OfxScgPtpPmRealRxEdfaOpt_Object((1,3,6,1,4,1,21296,2,2,2,3,39,1,1,7),_OfxScgPtpPmRealRxEdfaOpt_Type())
ofxScgPtpPmRealRxEdfaOpt.setMaxAccess(_C)
if mibBuilder.loadTexts:ofxScgPtpPmRealRxEdfaOpt.setStatus(_A)
_OfxScgPtpPmRealRxEdfaLbc_Type=FloatHundredths
_OfxScgPtpPmRealRxEdfaLbc_Object=MibTableColumn
ofxScgPtpPmRealRxEdfaLbc=_OfxScgPtpPmRealRxEdfaLbc_Object((1,3,6,1,4,1,21296,2,2,2,3,39,1,1,8),_OfxScgPtpPmRealRxEdfaLbc_Type())
ofxScgPtpPmRealRxEdfaLbc.setMaxAccess(_C)
if mibBuilder.loadTexts:ofxScgPtpPmRealRxEdfaLbc.setStatus(_A)
_OfxScgPtpPmRealQPreFec_Type=FloatHundredths
_OfxScgPtpPmRealQPreFec_Object=MibTableColumn
ofxScgPtpPmRealQPreFec=_OfxScgPtpPmRealQPreFec_Object((1,3,6,1,4,1,21296,2,2,2,3,39,1,1,9),_OfxScgPtpPmRealQPreFec_Type())
ofxScgPtpPmRealQPreFec.setMaxAccess(_C)
if mibBuilder.loadTexts:ofxScgPtpPmRealQPreFec.setStatus(_A)
_OfxScgPtpPmRealBerPreFec_Type=FloatHundredths
_OfxScgPtpPmRealBerPreFec_Object=MibTableColumn
ofxScgPtpPmRealBerPreFec=_OfxScgPtpPmRealBerPreFec_Object((1,3,6,1,4,1,21296,2,2,2,3,39,1,1,10),_OfxScgPtpPmRealBerPreFec_Type())
ofxScgPtpPmRealBerPreFec.setMaxAccess(_C)
if mibBuilder.loadTexts:ofxScgPtpPmRealBerPreFec.setStatus(_A)
_OfxScgPtpPmTable_Object=MibTable
ofxScgPtpPmTable=_OfxScgPtpPmTable_Object((1,3,6,1,4,1,21296,2,2,2,3,39,2))
if mibBuilder.loadTexts:ofxScgPtpPmTable.setStatus(_A)
_OfxScgPtpPmEntry_Object=MibTableRow
ofxScgPtpPmEntry=_OfxScgPtpPmEntry_Object((1,3,6,1,4,1,21296,2,2,2,3,39,2,1))
ofxScgPtpPmEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:ofxScgPtpPmEntry.setStatus(_A)
class _OfxScgPtpPmTimestamp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_OfxScgPtpPmTimestamp_Type.__name__=_F
_OfxScgPtpPmTimestamp_Object=MibTableColumn
ofxScgPtpPmTimestamp=_OfxScgPtpPmTimestamp_Object((1,3,6,1,4,1,21296,2,2,2,3,39,2,1,1),_OfxScgPtpPmTimestamp_Type())
ofxScgPtpPmTimestamp.setMaxAccess(_G)
if mibBuilder.loadTexts:ofxScgPtpPmTimestamp.setStatus(_A)
class _OfxScgPtpPmSampleDuration_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('fifteenMinutes',1),('day',2)))
_OfxScgPtpPmSampleDuration_Type.__name__=_F
_OfxScgPtpPmSampleDuration_Object=MibTableColumn
ofxScgPtpPmSampleDuration=_OfxScgPtpPmSampleDuration_Object((1,3,6,1,4,1,21296,2,2,2,3,39,2,1,2),_OfxScgPtpPmSampleDuration_Type())
ofxScgPtpPmSampleDuration.setMaxAccess(_G)
if mibBuilder.loadTexts:ofxScgPtpPmSampleDuration.setStatus(_A)
_OfxScgPtpPmValidity_Type=TruthValue
_OfxScgPtpPmValidity_Object=MibTableColumn
ofxScgPtpPmValidity=_OfxScgPtpPmValidity_Object((1,3,6,1,4,1,21296,2,2,2,3,39,2,1,3),_OfxScgPtpPmValidity_Type())
ofxScgPtpPmValidity.setMaxAccess(_C)
if mibBuilder.loadTexts:ofxScgPtpPmValidity.setStatus(_A)
_OfxScgPtpPmTxEdfaOprMin_Type=FloatHundredths
_OfxScgPtpPmTxEdfaOprMin_Object=MibTableColumn
ofxScgPtpPmTxEdfaOprMin=_OfxScgPtpPmTxEdfaOprMin_Object((1,3,6,1,4,1,21296,2,2,2,3,39,2,1,4),_OfxScgPtpPmTxEdfaOprMin_Type())
ofxScgPtpPmTxEdfaOprMin.setMaxAccess(_C)
if mibBuilder.loadTexts:ofxScgPtpPmTxEdfaOprMin.setStatus(_A)
_OfxScgPtpPmTxEdfaOprMax_Type=FloatHundredths
_OfxScgPtpPmTxEdfaOprMax_Object=MibTableColumn
ofxScgPtpPmTxEdfaOprMax=_OfxScgPtpPmTxEdfaOprMax_Object((1,3,6,1,4,1,21296,2,2,2,3,39,2,1,5),_OfxScgPtpPmTxEdfaOprMax_Type())
ofxScgPtpPmTxEdfaOprMax.setMaxAccess(_C)
if mibBuilder.loadTexts:ofxScgPtpPmTxEdfaOprMax.setStatus(_A)
_OfxScgPtpPmTxEdfaOprAve_Type=FloatHundredths
_OfxScgPtpPmTxEdfaOprAve_Object=MibTableColumn
ofxScgPtpPmTxEdfaOprAve=_OfxScgPtpPmTxEdfaOprAve_Object((1,3,6,1,4,1,21296,2,2,2,3,39,2,1,6),_OfxScgPtpPmTxEdfaOprAve_Type())
ofxScgPtpPmTxEdfaOprAve.setMaxAccess(_C)
if mibBuilder.loadTexts:ofxScgPtpPmTxEdfaOprAve.setStatus(_A)
_OfxScgPtpPmTxEdfaOptMin_Type=FloatHundredths
_OfxScgPtpPmTxEdfaOptMin_Object=MibTableColumn
ofxScgPtpPmTxEdfaOptMin=_OfxScgPtpPmTxEdfaOptMin_Object((1,3,6,1,4,1,21296,2,2,2,3,39,2,1,7),_OfxScgPtpPmTxEdfaOptMin_Type())
ofxScgPtpPmTxEdfaOptMin.setMaxAccess(_C)
if mibBuilder.loadTexts:ofxScgPtpPmTxEdfaOptMin.setStatus(_A)
_OfxScgPtpPmTxEdfaOptMax_Type=FloatHundredths
_OfxScgPtpPmTxEdfaOptMax_Object=MibTableColumn
ofxScgPtpPmTxEdfaOptMax=_OfxScgPtpPmTxEdfaOptMax_Object((1,3,6,1,4,1,21296,2,2,2,3,39,2,1,8),_OfxScgPtpPmTxEdfaOptMax_Type())
ofxScgPtpPmTxEdfaOptMax.setMaxAccess(_C)
if mibBuilder.loadTexts:ofxScgPtpPmTxEdfaOptMax.setStatus(_A)
_OfxScgPtpPmTxEdfaOptAve_Type=FloatHundredths
_OfxScgPtpPmTxEdfaOptAve_Object=MibTableColumn
ofxScgPtpPmTxEdfaOptAve=_OfxScgPtpPmTxEdfaOptAve_Object((1,3,6,1,4,1,21296,2,2,2,3,39,2,1,9),_OfxScgPtpPmTxEdfaOptAve_Type())
ofxScgPtpPmTxEdfaOptAve.setMaxAccess(_C)
if mibBuilder.loadTexts:ofxScgPtpPmTxEdfaOptAve.setStatus(_A)
_OfxScgPtpPmTxEdfaLbcMin_Type=FloatHundredths
_OfxScgPtpPmTxEdfaLbcMin_Object=MibTableColumn
ofxScgPtpPmTxEdfaLbcMin=_OfxScgPtpPmTxEdfaLbcMin_Object((1,3,6,1,4,1,21296,2,2,2,3,39,2,1,10),_OfxScgPtpPmTxEdfaLbcMin_Type())
ofxScgPtpPmTxEdfaLbcMin.setMaxAccess(_C)
if mibBuilder.loadTexts:ofxScgPtpPmTxEdfaLbcMin.setStatus(_A)
_OfxScgPtpPmTxEdfaLbcMax_Type=FloatHundredths
_OfxScgPtpPmTxEdfaLbcMax_Object=MibTableColumn
ofxScgPtpPmTxEdfaLbcMax=_OfxScgPtpPmTxEdfaLbcMax_Object((1,3,6,1,4,1,21296,2,2,2,3,39,2,1,11),_OfxScgPtpPmTxEdfaLbcMax_Type())
ofxScgPtpPmTxEdfaLbcMax.setMaxAccess(_C)
if mibBuilder.loadTexts:ofxScgPtpPmTxEdfaLbcMax.setStatus(_A)
_OfxScgPtpPmTxEdfaLbcAve_Type=FloatHundredths
_OfxScgPtpPmTxEdfaLbcAve_Object=MibTableColumn
ofxScgPtpPmTxEdfaLbcAve=_OfxScgPtpPmTxEdfaLbcAve_Object((1,3,6,1,4,1,21296,2,2,2,3,39,2,1,12),_OfxScgPtpPmTxEdfaLbcAve_Type())
ofxScgPtpPmTxEdfaLbcAve.setMaxAccess(_C)
if mibBuilder.loadTexts:ofxScgPtpPmTxEdfaLbcAve.setStatus(_A)
_OfxScgPtpPmRxEdfaOprMin_Type=FloatHundredths
_OfxScgPtpPmRxEdfaOprMin_Object=MibTableColumn
ofxScgPtpPmRxEdfaOprMin=_OfxScgPtpPmRxEdfaOprMin_Object((1,3,6,1,4,1,21296,2,2,2,3,39,2,1,13),_OfxScgPtpPmRxEdfaOprMin_Type())
ofxScgPtpPmRxEdfaOprMin.setMaxAccess(_C)
if mibBuilder.loadTexts:ofxScgPtpPmRxEdfaOprMin.setStatus(_A)
_OfxScgPtpPmRxEdfaOprMax_Type=FloatHundredths
_OfxScgPtpPmRxEdfaOprMax_Object=MibTableColumn
ofxScgPtpPmRxEdfaOprMax=_OfxScgPtpPmRxEdfaOprMax_Object((1,3,6,1,4,1,21296,2,2,2,3,39,2,1,14),_OfxScgPtpPmRxEdfaOprMax_Type())
ofxScgPtpPmRxEdfaOprMax.setMaxAccess(_C)
if mibBuilder.loadTexts:ofxScgPtpPmRxEdfaOprMax.setStatus(_A)
_OfxScgPtpPmRxEdfaOprAve_Type=FloatHundredths
_OfxScgPtpPmRxEdfaOprAve_Object=MibTableColumn
ofxScgPtpPmRxEdfaOprAve=_OfxScgPtpPmRxEdfaOprAve_Object((1,3,6,1,4,1,21296,2,2,2,3,39,2,1,15),_OfxScgPtpPmRxEdfaOprAve_Type())
ofxScgPtpPmRxEdfaOprAve.setMaxAccess(_C)
if mibBuilder.loadTexts:ofxScgPtpPmRxEdfaOprAve.setStatus(_A)
_OfxScgPtpPmRxEdfaOptMin_Type=FloatHundredths
_OfxScgPtpPmRxEdfaOptMin_Object=MibTableColumn
ofxScgPtpPmRxEdfaOptMin=_OfxScgPtpPmRxEdfaOptMin_Object((1,3,6,1,4,1,21296,2,2,2,3,39,2,1,16),_OfxScgPtpPmRxEdfaOptMin_Type())
ofxScgPtpPmRxEdfaOptMin.setMaxAccess(_C)
if mibBuilder.loadTexts:ofxScgPtpPmRxEdfaOptMin.setStatus(_A)
_OfxScgPtpPmRxEdfaOptMax_Type=FloatHundredths
_OfxScgPtpPmRxEdfaOptMax_Object=MibTableColumn
ofxScgPtpPmRxEdfaOptMax=_OfxScgPtpPmRxEdfaOptMax_Object((1,3,6,1,4,1,21296,2,2,2,3,39,2,1,17),_OfxScgPtpPmRxEdfaOptMax_Type())
ofxScgPtpPmRxEdfaOptMax.setMaxAccess(_C)
if mibBuilder.loadTexts:ofxScgPtpPmRxEdfaOptMax.setStatus(_A)
_OfxScgPtpPmRxEdfaOptAve_Type=FloatHundredths
_OfxScgPtpPmRxEdfaOptAve_Object=MibTableColumn
ofxScgPtpPmRxEdfaOptAve=_OfxScgPtpPmRxEdfaOptAve_Object((1,3,6,1,4,1,21296,2,2,2,3,39,2,1,18),_OfxScgPtpPmRxEdfaOptAve_Type())
ofxScgPtpPmRxEdfaOptAve.setMaxAccess(_C)
if mibBuilder.loadTexts:ofxScgPtpPmRxEdfaOptAve.setStatus(_A)
_OfxScgPtpPmRxEdfaLbcMin_Type=FloatHundredths
_OfxScgPtpPmRxEdfaLbcMin_Object=MibTableColumn
ofxScgPtpPmRxEdfaLbcMin=_OfxScgPtpPmRxEdfaLbcMin_Object((1,3,6,1,4,1,21296,2,2,2,3,39,2,1,19),_OfxScgPtpPmRxEdfaLbcMin_Type())
ofxScgPtpPmRxEdfaLbcMin.setMaxAccess(_C)
if mibBuilder.loadTexts:ofxScgPtpPmRxEdfaLbcMin.setStatus(_A)
_OfxScgPtpPmRxEdfaLbcMax_Type=FloatHundredths
_OfxScgPtpPmRxEdfaLbcMax_Object=MibTableColumn
ofxScgPtpPmRxEdfaLbcMax=_OfxScgPtpPmRxEdfaLbcMax_Object((1,3,6,1,4,1,21296,2,2,2,3,39,2,1,20),_OfxScgPtpPmRxEdfaLbcMax_Type())
ofxScgPtpPmRxEdfaLbcMax.setMaxAccess(_C)
if mibBuilder.loadTexts:ofxScgPtpPmRxEdfaLbcMax.setStatus(_A)
_OfxScgPtpPmRxEdfaLbcAve_Type=FloatHundredths
_OfxScgPtpPmRxEdfaLbcAve_Object=MibTableColumn
ofxScgPtpPmRxEdfaLbcAve=_OfxScgPtpPmRxEdfaLbcAve_Object((1,3,6,1,4,1,21296,2,2,2,3,39,2,1,21),_OfxScgPtpPmRxEdfaLbcAve_Type())
ofxScgPtpPmRxEdfaLbcAve.setMaxAccess(_C)
if mibBuilder.loadTexts:ofxScgPtpPmRxEdfaLbcAve.setStatus(_A)
_OfxScgPtpPmQPreFecMin_Type=FloatHundredths
_OfxScgPtpPmQPreFecMin_Object=MibTableColumn
ofxScgPtpPmQPreFecMin=_OfxScgPtpPmQPreFecMin_Object((1,3,6,1,4,1,21296,2,2,2,3,39,2,1,22),_OfxScgPtpPmQPreFecMin_Type())
ofxScgPtpPmQPreFecMin.setMaxAccess(_C)
if mibBuilder.loadTexts:ofxScgPtpPmQPreFecMin.setStatus(_A)
_OfxScgPtpPmQPreFecMax_Type=FloatHundredths
_OfxScgPtpPmQPreFecMax_Object=MibTableColumn
ofxScgPtpPmQPreFecMax=_OfxScgPtpPmQPreFecMax_Object((1,3,6,1,4,1,21296,2,2,2,3,39,2,1,23),_OfxScgPtpPmQPreFecMax_Type())
ofxScgPtpPmQPreFecMax.setMaxAccess(_C)
if mibBuilder.loadTexts:ofxScgPtpPmQPreFecMax.setStatus(_A)
_OfxScgPtpPmQPreFecAve_Type=FloatHundredths
_OfxScgPtpPmQPreFecAve_Object=MibTableColumn
ofxScgPtpPmQPreFecAve=_OfxScgPtpPmQPreFecAve_Object((1,3,6,1,4,1,21296,2,2,2,3,39,2,1,24),_OfxScgPtpPmQPreFecAve_Type())
ofxScgPtpPmQPreFecAve.setMaxAccess(_C)
if mibBuilder.loadTexts:ofxScgPtpPmQPreFecAve.setStatus(_A)
_OfxScgPtpPmBerPreFecMin_Type=FloatHundredths
_OfxScgPtpPmBerPreFecMin_Object=MibTableColumn
ofxScgPtpPmBerPreFecMin=_OfxScgPtpPmBerPreFecMin_Object((1,3,6,1,4,1,21296,2,2,2,3,39,2,1,25),_OfxScgPtpPmBerPreFecMin_Type())
ofxScgPtpPmBerPreFecMin.setMaxAccess(_C)
if mibBuilder.loadTexts:ofxScgPtpPmBerPreFecMin.setStatus(_A)
_OfxScgPtpPmBerPreFecMax_Type=FloatHundredths
_OfxScgPtpPmBerPreFecMax_Object=MibTableColumn
ofxScgPtpPmBerPreFecMax=_OfxScgPtpPmBerPreFecMax_Object((1,3,6,1,4,1,21296,2,2,2,3,39,2,1,26),_OfxScgPtpPmBerPreFecMax_Type())
ofxScgPtpPmBerPreFecMax.setMaxAccess(_C)
if mibBuilder.loadTexts:ofxScgPtpPmBerPreFecMax.setStatus(_A)
_OfxScgPtpPmBerPreFecAve_Type=FloatHundredths
_OfxScgPtpPmBerPreFecAve_Object=MibTableColumn
ofxScgPtpPmBerPreFecAve=_OfxScgPtpPmBerPreFecAve_Object((1,3,6,1,4,1,21296,2,2,2,3,39,2,1,27),_OfxScgPtpPmBerPreFecAve_Type())
ofxScgPtpPmBerPreFecAve.setMaxAccess(_C)
if mibBuilder.loadTexts:ofxScgPtpPmBerPreFecAve.setStatus(_A)
_OfxScgPtpPmConformance_ObjectIdentity=ObjectIdentity
ofxScgPtpPmConformance=_OfxScgPtpPmConformance_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,3,39,3))
_OfxScgPtpPmCompliances_ObjectIdentity=ObjectIdentity
ofxScgPtpPmCompliances=_OfxScgPtpPmCompliances_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,3,39,3,1))
_OfxScgPtpPmGroups_ObjectIdentity=ObjectIdentity
ofxScgPtpPmGroups=_OfxScgPtpPmGroups_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,3,39,3,2))
ofxScgPtpPmGroup=ObjectGroup((1,3,6,1,4,1,21296,2,2,2,3,39,3,2,1))
ofxScgPtpPmGroup.setObjects(*((_B,_H),(_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h)))
if mibBuilder.loadTexts:ofxScgPtpPmGroup.setStatus(_A)
ofxScgPtpPmRealGroup=ObjectGroup((1,3,6,1,4,1,21296,2,2,2,3,39,3,2,2))
ofxScgPtpPmRealGroup.setObjects(*((_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r)))
if mibBuilder.loadTexts:ofxScgPtpPmRealGroup.setStatus(_A)
ofxScgPtpPmCompliance=ModuleCompliance((1,3,6,1,4,1,21296,2,2,2,3,39,3,1,1))
ofxScgPtpPmCompliance.setObjects((_B,_s))
if mibBuilder.loadTexts:ofxScgPtpPmCompliance.setStatus(_A)
ofxScgPtpPmRealCompliance=ModuleCompliance((1,3,6,1,4,1,21296,2,2,2,3,39,3,1,2))
ofxScgPtpPmRealCompliance.setObjects((_B,_t))
if mibBuilder.loadTexts:ofxScgPtpPmRealCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ofxScgPtpPmMIB':ofxScgPtpPmMIB,'ofxScgPtpPmRealTable':ofxScgPtpPmRealTable,'ofxScgPtpPmRealEntry':ofxScgPtpPmRealEntry,_i:ofxScgPtpPmRealChanScgOpt,_j:ofxScgPtpPmRealChanScgOpr,_k:ofxScgPtpPmRealTxEdfaOpr,_l:ofxScgPtpPmRealTxEdfaOpt,_m:ofxScgPtpPmRealTxEdfaLbc,_n:ofxScgPtpPmRealRxEdfaOpr,_o:ofxScgPtpPmRealRxEdfaOpt,_p:ofxScgPtpPmRealRxEdfaLbc,_q:ofxScgPtpPmRealQPreFec,_r:ofxScgPtpPmRealBerPreFec,'ofxScgPtpPmTable':ofxScgPtpPmTable,'ofxScgPtpPmEntry':ofxScgPtpPmEntry,_H:ofxScgPtpPmTimestamp,_I:ofxScgPtpPmSampleDuration,_J:ofxScgPtpPmValidity,_K:ofxScgPtpPmTxEdfaOprMin,_L:ofxScgPtpPmTxEdfaOprMax,_M:ofxScgPtpPmTxEdfaOprAve,_N:ofxScgPtpPmTxEdfaOptMin,_O:ofxScgPtpPmTxEdfaOptMax,_P:ofxScgPtpPmTxEdfaOptAve,_Q:ofxScgPtpPmTxEdfaLbcMin,_R:ofxScgPtpPmTxEdfaLbcMax,_S:ofxScgPtpPmTxEdfaLbcAve,_T:ofxScgPtpPmRxEdfaOprMin,_U:ofxScgPtpPmRxEdfaOprMax,_V:ofxScgPtpPmRxEdfaOprAve,_W:ofxScgPtpPmRxEdfaOptMin,_X:ofxScgPtpPmRxEdfaOptMax,_Y:ofxScgPtpPmRxEdfaOptAve,_Z:ofxScgPtpPmRxEdfaLbcMin,_a:ofxScgPtpPmRxEdfaLbcMax,_b:ofxScgPtpPmRxEdfaLbcAve,_c:ofxScgPtpPmQPreFecMin,_d:ofxScgPtpPmQPreFecMax,_e:ofxScgPtpPmQPreFecAve,_f:ofxScgPtpPmBerPreFecMin,_g:ofxScgPtpPmBerPreFecMax,_h:ofxScgPtpPmBerPreFecAve,'ofxScgPtpPmConformance':ofxScgPtpPmConformance,'ofxScgPtpPmCompliances':ofxScgPtpPmCompliances,'ofxScgPtpPmCompliance':ofxScgPtpPmCompliance,'ofxScgPtpPmRealCompliance':ofxScgPtpPmRealCompliance,'ofxScgPtpPmGroups':ofxScgPtpPmGroups,_s:ofxScgPtpPmGroup,_t:ofxScgPtpPmRealGroup})