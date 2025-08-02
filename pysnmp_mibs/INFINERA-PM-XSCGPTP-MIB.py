_r='xScgPtpPmRealGroup'
_q='xScgPtpPmGroup'
_p='xScgPtpPmRealRxEdfaLbc'
_o='xScgPtpPmRealRxEdfaOpt'
_n='xScgPtpPmRealRxEdfaOpr'
_m='xScgPtpPmRealTxEdfaLbc'
_l='xScgPtpPmRealTxEdfaOpt'
_k='xScgPtpPmRealTxEdfaOpr'
_j='xScgPtpPmRealChanScgOpr'
_i='xScgPtpPmRealChanScgOpt'
_h='xScgPtpPmChanScgOprAve'
_g='xScgPtpPmChanScgOprMax'
_f='xScgPtpPmChanScgOprMin'
_e='xScgPtpPmChanScgOptAve'
_d='xScgPtpPmChanScgOptMax'
_c='xScgPtpPmChanScgOptMin'
_b='xScgPtpPmRxEdfaLbcAve'
_a='xScgPtpPmRxEdfaLbcMax'
_Z='xScgPtpPmRxEdfaLbcMin'
_Y='xScgPtpPmRxEdfaOptAve'
_X='xScgPtpPmRxEdfaOptMax'
_W='xScgPtpPmRxEdfaOptMin'
_V='xScgPtpPmRxEdfaOprAve'
_U='xScgPtpPmRxEdfaOprMax'
_T='xScgPtpPmRxEdfaOprMin'
_S='xScgPtpPmTxEdfaLbcAve'
_R='xScgPtpPmTxEdfaLbcMax'
_Q='xScgPtpPmTxEdfaLbcMin'
_P='xScgPtpPmTxEdfaOptAve'
_O='xScgPtpPmTxEdfaOptMax'
_N='xScgPtpPmTxEdfaOptMin'
_M='xScgPtpPmTxEdfaOprAve'
_L='xScgPtpPmTxEdfaOprMax'
_K='xScgPtpPmTxEdfaOprMin'
_J='xScgPtpPmValidity'
_I='not-accessible'
_H='xScgPtpPmTimestamp'
_G='xScgPtpPmSampleDuration'
_F='Integer32'
_E='ifIndex'
_D='IF-MIB'
_C='read-only'
_B='INFINERA-PM-XSCGPTP-MIB'
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
xScgPtpPmMIB=ModuleIdentity((1,3,6,1,4,1,21296,2,2,2,3,33))
if mibBuilder.loadTexts:xScgPtpPmMIB.setRevisions(('2015-12-28 00:00',))
_XScgPtpPmRealTable_Object=MibTable
xScgPtpPmRealTable=_XScgPtpPmRealTable_Object((1,3,6,1,4,1,21296,2,2,2,3,33,1))
if mibBuilder.loadTexts:xScgPtpPmRealTable.setStatus(_A)
_XScgPtpPmRealEntry_Object=MibTableRow
xScgPtpPmRealEntry=_XScgPtpPmRealEntry_Object((1,3,6,1,4,1,21296,2,2,2,3,33,1,1))
xScgPtpPmRealEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:xScgPtpPmRealEntry.setStatus(_A)
_XScgPtpPmRealChanScgOpt_Type=FloatHundredths
_XScgPtpPmRealChanScgOpt_Object=MibTableColumn
xScgPtpPmRealChanScgOpt=_XScgPtpPmRealChanScgOpt_Object((1,3,6,1,4,1,21296,2,2,2,3,33,1,1,1),_XScgPtpPmRealChanScgOpt_Type())
xScgPtpPmRealChanScgOpt.setMaxAccess(_C)
if mibBuilder.loadTexts:xScgPtpPmRealChanScgOpt.setStatus(_A)
_XScgPtpPmRealChanScgOpr_Type=FloatHundredths
_XScgPtpPmRealChanScgOpr_Object=MibTableColumn
xScgPtpPmRealChanScgOpr=_XScgPtpPmRealChanScgOpr_Object((1,3,6,1,4,1,21296,2,2,2,3,33,1,1,2),_XScgPtpPmRealChanScgOpr_Type())
xScgPtpPmRealChanScgOpr.setMaxAccess(_C)
if mibBuilder.loadTexts:xScgPtpPmRealChanScgOpr.setStatus(_A)
_XScgPtpPmRealTxEdfaOpr_Type=FloatHundredths
_XScgPtpPmRealTxEdfaOpr_Object=MibTableColumn
xScgPtpPmRealTxEdfaOpr=_XScgPtpPmRealTxEdfaOpr_Object((1,3,6,1,4,1,21296,2,2,2,3,33,1,1,3),_XScgPtpPmRealTxEdfaOpr_Type())
xScgPtpPmRealTxEdfaOpr.setMaxAccess(_C)
if mibBuilder.loadTexts:xScgPtpPmRealTxEdfaOpr.setStatus(_A)
_XScgPtpPmRealTxEdfaOpt_Type=FloatHundredths
_XScgPtpPmRealTxEdfaOpt_Object=MibTableColumn
xScgPtpPmRealTxEdfaOpt=_XScgPtpPmRealTxEdfaOpt_Object((1,3,6,1,4,1,21296,2,2,2,3,33,1,1,4),_XScgPtpPmRealTxEdfaOpt_Type())
xScgPtpPmRealTxEdfaOpt.setMaxAccess(_C)
if mibBuilder.loadTexts:xScgPtpPmRealTxEdfaOpt.setStatus(_A)
_XScgPtpPmRealTxEdfaLbc_Type=FloatHundredths
_XScgPtpPmRealTxEdfaLbc_Object=MibTableColumn
xScgPtpPmRealTxEdfaLbc=_XScgPtpPmRealTxEdfaLbc_Object((1,3,6,1,4,1,21296,2,2,2,3,33,1,1,5),_XScgPtpPmRealTxEdfaLbc_Type())
xScgPtpPmRealTxEdfaLbc.setMaxAccess(_C)
if mibBuilder.loadTexts:xScgPtpPmRealTxEdfaLbc.setStatus(_A)
_XScgPtpPmRealRxEdfaOpr_Type=FloatHundredths
_XScgPtpPmRealRxEdfaOpr_Object=MibTableColumn
xScgPtpPmRealRxEdfaOpr=_XScgPtpPmRealRxEdfaOpr_Object((1,3,6,1,4,1,21296,2,2,2,3,33,1,1,6),_XScgPtpPmRealRxEdfaOpr_Type())
xScgPtpPmRealRxEdfaOpr.setMaxAccess(_C)
if mibBuilder.loadTexts:xScgPtpPmRealRxEdfaOpr.setStatus(_A)
_XScgPtpPmRealRxEdfaOpt_Type=FloatHundredths
_XScgPtpPmRealRxEdfaOpt_Object=MibTableColumn
xScgPtpPmRealRxEdfaOpt=_XScgPtpPmRealRxEdfaOpt_Object((1,3,6,1,4,1,21296,2,2,2,3,33,1,1,7),_XScgPtpPmRealRxEdfaOpt_Type())
xScgPtpPmRealRxEdfaOpt.setMaxAccess(_C)
if mibBuilder.loadTexts:xScgPtpPmRealRxEdfaOpt.setStatus(_A)
_XScgPtpPmRealRxEdfaLbc_Type=FloatHundredths
_XScgPtpPmRealRxEdfaLbc_Object=MibTableColumn
xScgPtpPmRealRxEdfaLbc=_XScgPtpPmRealRxEdfaLbc_Object((1,3,6,1,4,1,21296,2,2,2,3,33,1,1,8),_XScgPtpPmRealRxEdfaLbc_Type())
xScgPtpPmRealRxEdfaLbc.setMaxAccess(_C)
if mibBuilder.loadTexts:xScgPtpPmRealRxEdfaLbc.setStatus(_A)
_XScgPtpPmTable_Object=MibTable
xScgPtpPmTable=_XScgPtpPmTable_Object((1,3,6,1,4,1,21296,2,2,2,3,33,2))
if mibBuilder.loadTexts:xScgPtpPmTable.setStatus(_A)
_XScgPtpPmEntry_Object=MibTableRow
xScgPtpPmEntry=_XScgPtpPmEntry_Object((1,3,6,1,4,1,21296,2,2,2,3,33,2,1))
xScgPtpPmEntry.setIndexNames((0,_D,_E),(0,_B,_G),(0,_B,_H))
if mibBuilder.loadTexts:xScgPtpPmEntry.setStatus(_A)
class _XScgPtpPmTimestamp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_XScgPtpPmTimestamp_Type.__name__=_F
_XScgPtpPmTimestamp_Object=MibTableColumn
xScgPtpPmTimestamp=_XScgPtpPmTimestamp_Object((1,3,6,1,4,1,21296,2,2,2,3,33,2,1,1),_XScgPtpPmTimestamp_Type())
xScgPtpPmTimestamp.setMaxAccess(_I)
if mibBuilder.loadTexts:xScgPtpPmTimestamp.setStatus(_A)
class _XScgPtpPmSampleDuration_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('fifteenMinutes',1),('day',2)))
_XScgPtpPmSampleDuration_Type.__name__=_F
_XScgPtpPmSampleDuration_Object=MibTableColumn
xScgPtpPmSampleDuration=_XScgPtpPmSampleDuration_Object((1,3,6,1,4,1,21296,2,2,2,3,33,2,1,2),_XScgPtpPmSampleDuration_Type())
xScgPtpPmSampleDuration.setMaxAccess(_I)
if mibBuilder.loadTexts:xScgPtpPmSampleDuration.setStatus(_A)
_XScgPtpPmValidity_Type=TruthValue
_XScgPtpPmValidity_Object=MibTableColumn
xScgPtpPmValidity=_XScgPtpPmValidity_Object((1,3,6,1,4,1,21296,2,2,2,3,33,2,1,3),_XScgPtpPmValidity_Type())
xScgPtpPmValidity.setMaxAccess(_C)
if mibBuilder.loadTexts:xScgPtpPmValidity.setStatus(_A)
_XScgPtpPmTxEdfaOprMin_Type=FloatHundredths
_XScgPtpPmTxEdfaOprMin_Object=MibTableColumn
xScgPtpPmTxEdfaOprMin=_XScgPtpPmTxEdfaOprMin_Object((1,3,6,1,4,1,21296,2,2,2,3,33,2,1,4),_XScgPtpPmTxEdfaOprMin_Type())
xScgPtpPmTxEdfaOprMin.setMaxAccess(_C)
if mibBuilder.loadTexts:xScgPtpPmTxEdfaOprMin.setStatus(_A)
_XScgPtpPmTxEdfaOprMax_Type=FloatHundredths
_XScgPtpPmTxEdfaOprMax_Object=MibTableColumn
xScgPtpPmTxEdfaOprMax=_XScgPtpPmTxEdfaOprMax_Object((1,3,6,1,4,1,21296,2,2,2,3,33,2,1,5),_XScgPtpPmTxEdfaOprMax_Type())
xScgPtpPmTxEdfaOprMax.setMaxAccess(_C)
if mibBuilder.loadTexts:xScgPtpPmTxEdfaOprMax.setStatus(_A)
_XScgPtpPmTxEdfaOprAve_Type=FloatHundredths
_XScgPtpPmTxEdfaOprAve_Object=MibTableColumn
xScgPtpPmTxEdfaOprAve=_XScgPtpPmTxEdfaOprAve_Object((1,3,6,1,4,1,21296,2,2,2,3,33,2,1,6),_XScgPtpPmTxEdfaOprAve_Type())
xScgPtpPmTxEdfaOprAve.setMaxAccess(_C)
if mibBuilder.loadTexts:xScgPtpPmTxEdfaOprAve.setStatus(_A)
_XScgPtpPmTxEdfaOptMin_Type=FloatHundredths
_XScgPtpPmTxEdfaOptMin_Object=MibTableColumn
xScgPtpPmTxEdfaOptMin=_XScgPtpPmTxEdfaOptMin_Object((1,3,6,1,4,1,21296,2,2,2,3,33,2,1,7),_XScgPtpPmTxEdfaOptMin_Type())
xScgPtpPmTxEdfaOptMin.setMaxAccess(_C)
if mibBuilder.loadTexts:xScgPtpPmTxEdfaOptMin.setStatus(_A)
_XScgPtpPmTxEdfaOptMax_Type=FloatHundredths
_XScgPtpPmTxEdfaOptMax_Object=MibTableColumn
xScgPtpPmTxEdfaOptMax=_XScgPtpPmTxEdfaOptMax_Object((1,3,6,1,4,1,21296,2,2,2,3,33,2,1,8),_XScgPtpPmTxEdfaOptMax_Type())
xScgPtpPmTxEdfaOptMax.setMaxAccess(_C)
if mibBuilder.loadTexts:xScgPtpPmTxEdfaOptMax.setStatus(_A)
_XScgPtpPmTxEdfaOptAve_Type=FloatHundredths
_XScgPtpPmTxEdfaOptAve_Object=MibTableColumn
xScgPtpPmTxEdfaOptAve=_XScgPtpPmTxEdfaOptAve_Object((1,3,6,1,4,1,21296,2,2,2,3,33,2,1,9),_XScgPtpPmTxEdfaOptAve_Type())
xScgPtpPmTxEdfaOptAve.setMaxAccess(_C)
if mibBuilder.loadTexts:xScgPtpPmTxEdfaOptAve.setStatus(_A)
_XScgPtpPmTxEdfaLbcMin_Type=FloatHundredths
_XScgPtpPmTxEdfaLbcMin_Object=MibTableColumn
xScgPtpPmTxEdfaLbcMin=_XScgPtpPmTxEdfaLbcMin_Object((1,3,6,1,4,1,21296,2,2,2,3,33,2,1,10),_XScgPtpPmTxEdfaLbcMin_Type())
xScgPtpPmTxEdfaLbcMin.setMaxAccess(_C)
if mibBuilder.loadTexts:xScgPtpPmTxEdfaLbcMin.setStatus(_A)
_XScgPtpPmTxEdfaLbcMax_Type=FloatHundredths
_XScgPtpPmTxEdfaLbcMax_Object=MibTableColumn
xScgPtpPmTxEdfaLbcMax=_XScgPtpPmTxEdfaLbcMax_Object((1,3,6,1,4,1,21296,2,2,2,3,33,2,1,11),_XScgPtpPmTxEdfaLbcMax_Type())
xScgPtpPmTxEdfaLbcMax.setMaxAccess(_C)
if mibBuilder.loadTexts:xScgPtpPmTxEdfaLbcMax.setStatus(_A)
_XScgPtpPmTxEdfaLbcAve_Type=FloatHundredths
_XScgPtpPmTxEdfaLbcAve_Object=MibTableColumn
xScgPtpPmTxEdfaLbcAve=_XScgPtpPmTxEdfaLbcAve_Object((1,3,6,1,4,1,21296,2,2,2,3,33,2,1,12),_XScgPtpPmTxEdfaLbcAve_Type())
xScgPtpPmTxEdfaLbcAve.setMaxAccess(_C)
if mibBuilder.loadTexts:xScgPtpPmTxEdfaLbcAve.setStatus(_A)
_XScgPtpPmRxEdfaOprMin_Type=FloatHundredths
_XScgPtpPmRxEdfaOprMin_Object=MibTableColumn
xScgPtpPmRxEdfaOprMin=_XScgPtpPmRxEdfaOprMin_Object((1,3,6,1,4,1,21296,2,2,2,3,33,2,1,13),_XScgPtpPmRxEdfaOprMin_Type())
xScgPtpPmRxEdfaOprMin.setMaxAccess(_C)
if mibBuilder.loadTexts:xScgPtpPmRxEdfaOprMin.setStatus(_A)
_XScgPtpPmRxEdfaOprMax_Type=FloatHundredths
_XScgPtpPmRxEdfaOprMax_Object=MibTableColumn
xScgPtpPmRxEdfaOprMax=_XScgPtpPmRxEdfaOprMax_Object((1,3,6,1,4,1,21296,2,2,2,3,33,2,1,14),_XScgPtpPmRxEdfaOprMax_Type())
xScgPtpPmRxEdfaOprMax.setMaxAccess(_C)
if mibBuilder.loadTexts:xScgPtpPmRxEdfaOprMax.setStatus(_A)
_XScgPtpPmRxEdfaOprAve_Type=FloatHundredths
_XScgPtpPmRxEdfaOprAve_Object=MibTableColumn
xScgPtpPmRxEdfaOprAve=_XScgPtpPmRxEdfaOprAve_Object((1,3,6,1,4,1,21296,2,2,2,3,33,2,1,15),_XScgPtpPmRxEdfaOprAve_Type())
xScgPtpPmRxEdfaOprAve.setMaxAccess(_C)
if mibBuilder.loadTexts:xScgPtpPmRxEdfaOprAve.setStatus(_A)
_XScgPtpPmRxEdfaOptMin_Type=FloatHundredths
_XScgPtpPmRxEdfaOptMin_Object=MibTableColumn
xScgPtpPmRxEdfaOptMin=_XScgPtpPmRxEdfaOptMin_Object((1,3,6,1,4,1,21296,2,2,2,3,33,2,1,16),_XScgPtpPmRxEdfaOptMin_Type())
xScgPtpPmRxEdfaOptMin.setMaxAccess(_C)
if mibBuilder.loadTexts:xScgPtpPmRxEdfaOptMin.setStatus(_A)
_XScgPtpPmRxEdfaOptMax_Type=FloatHundredths
_XScgPtpPmRxEdfaOptMax_Object=MibTableColumn
xScgPtpPmRxEdfaOptMax=_XScgPtpPmRxEdfaOptMax_Object((1,3,6,1,4,1,21296,2,2,2,3,33,2,1,17),_XScgPtpPmRxEdfaOptMax_Type())
xScgPtpPmRxEdfaOptMax.setMaxAccess(_C)
if mibBuilder.loadTexts:xScgPtpPmRxEdfaOptMax.setStatus(_A)
_XScgPtpPmRxEdfaOptAve_Type=FloatHundredths
_XScgPtpPmRxEdfaOptAve_Object=MibTableColumn
xScgPtpPmRxEdfaOptAve=_XScgPtpPmRxEdfaOptAve_Object((1,3,6,1,4,1,21296,2,2,2,3,33,2,1,18),_XScgPtpPmRxEdfaOptAve_Type())
xScgPtpPmRxEdfaOptAve.setMaxAccess(_C)
if mibBuilder.loadTexts:xScgPtpPmRxEdfaOptAve.setStatus(_A)
_XScgPtpPmRxEdfaLbcMin_Type=FloatHundredths
_XScgPtpPmRxEdfaLbcMin_Object=MibTableColumn
xScgPtpPmRxEdfaLbcMin=_XScgPtpPmRxEdfaLbcMin_Object((1,3,6,1,4,1,21296,2,2,2,3,33,2,1,19),_XScgPtpPmRxEdfaLbcMin_Type())
xScgPtpPmRxEdfaLbcMin.setMaxAccess(_C)
if mibBuilder.loadTexts:xScgPtpPmRxEdfaLbcMin.setStatus(_A)
_XScgPtpPmRxEdfaLbcMax_Type=FloatHundredths
_XScgPtpPmRxEdfaLbcMax_Object=MibTableColumn
xScgPtpPmRxEdfaLbcMax=_XScgPtpPmRxEdfaLbcMax_Object((1,3,6,1,4,1,21296,2,2,2,3,33,2,1,20),_XScgPtpPmRxEdfaLbcMax_Type())
xScgPtpPmRxEdfaLbcMax.setMaxAccess(_C)
if mibBuilder.loadTexts:xScgPtpPmRxEdfaLbcMax.setStatus(_A)
_XScgPtpPmRxEdfaLbcAve_Type=FloatHundredths
_XScgPtpPmRxEdfaLbcAve_Object=MibTableColumn
xScgPtpPmRxEdfaLbcAve=_XScgPtpPmRxEdfaLbcAve_Object((1,3,6,1,4,1,21296,2,2,2,3,33,2,1,21),_XScgPtpPmRxEdfaLbcAve_Type())
xScgPtpPmRxEdfaLbcAve.setMaxAccess(_C)
if mibBuilder.loadTexts:xScgPtpPmRxEdfaLbcAve.setStatus(_A)
_XScgPtpPmChanScgOptMin_Type=FloatHundredths
_XScgPtpPmChanScgOptMin_Object=MibTableColumn
xScgPtpPmChanScgOptMin=_XScgPtpPmChanScgOptMin_Object((1,3,6,1,4,1,21296,2,2,2,3,33,2,1,22),_XScgPtpPmChanScgOptMin_Type())
xScgPtpPmChanScgOptMin.setMaxAccess(_C)
if mibBuilder.loadTexts:xScgPtpPmChanScgOptMin.setStatus(_A)
_XScgPtpPmChanScgOptMax_Type=FloatHundredths
_XScgPtpPmChanScgOptMax_Object=MibTableColumn
xScgPtpPmChanScgOptMax=_XScgPtpPmChanScgOptMax_Object((1,3,6,1,4,1,21296,2,2,2,3,33,2,1,23),_XScgPtpPmChanScgOptMax_Type())
xScgPtpPmChanScgOptMax.setMaxAccess(_C)
if mibBuilder.loadTexts:xScgPtpPmChanScgOptMax.setStatus(_A)
_XScgPtpPmChanScgOptAve_Type=FloatHundredths
_XScgPtpPmChanScgOptAve_Object=MibTableColumn
xScgPtpPmChanScgOptAve=_XScgPtpPmChanScgOptAve_Object((1,3,6,1,4,1,21296,2,2,2,3,33,2,1,24),_XScgPtpPmChanScgOptAve_Type())
xScgPtpPmChanScgOptAve.setMaxAccess(_C)
if mibBuilder.loadTexts:xScgPtpPmChanScgOptAve.setStatus(_A)
_XScgPtpPmChanScgOprMin_Type=FloatHundredths
_XScgPtpPmChanScgOprMin_Object=MibTableColumn
xScgPtpPmChanScgOprMin=_XScgPtpPmChanScgOprMin_Object((1,3,6,1,4,1,21296,2,2,2,3,33,2,1,25),_XScgPtpPmChanScgOprMin_Type())
xScgPtpPmChanScgOprMin.setMaxAccess(_C)
if mibBuilder.loadTexts:xScgPtpPmChanScgOprMin.setStatus(_A)
_XScgPtpPmChanScgOprMax_Type=FloatHundredths
_XScgPtpPmChanScgOprMax_Object=MibTableColumn
xScgPtpPmChanScgOprMax=_XScgPtpPmChanScgOprMax_Object((1,3,6,1,4,1,21296,2,2,2,3,33,2,1,26),_XScgPtpPmChanScgOprMax_Type())
xScgPtpPmChanScgOprMax.setMaxAccess(_C)
if mibBuilder.loadTexts:xScgPtpPmChanScgOprMax.setStatus(_A)
_XScgPtpPmChanScgOprAve_Type=FloatHundredths
_XScgPtpPmChanScgOprAve_Object=MibTableColumn
xScgPtpPmChanScgOprAve=_XScgPtpPmChanScgOprAve_Object((1,3,6,1,4,1,21296,2,2,2,3,33,2,1,27),_XScgPtpPmChanScgOprAve_Type())
xScgPtpPmChanScgOprAve.setMaxAccess(_C)
if mibBuilder.loadTexts:xScgPtpPmChanScgOprAve.setStatus(_A)
_XScgPtpPmConformance_ObjectIdentity=ObjectIdentity
xScgPtpPmConformance=_XScgPtpPmConformance_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,3,33,3))
_XScgPtpPmCompliances_ObjectIdentity=ObjectIdentity
xScgPtpPmCompliances=_XScgPtpPmCompliances_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,3,33,3,1))
_XScgPtpPmGroups_ObjectIdentity=ObjectIdentity
xScgPtpPmGroups=_XScgPtpPmGroups_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,3,33,3,2))
xScgPtpPmGroup=ObjectGroup((1,3,6,1,4,1,21296,2,2,2,3,33,3,2,1))
xScgPtpPmGroup.setObjects(*((_B,_H),(_B,_G),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h)))
if mibBuilder.loadTexts:xScgPtpPmGroup.setStatus(_A)
xScgPtpPmRealGroup=ObjectGroup((1,3,6,1,4,1,21296,2,2,2,3,33,3,2,2))
xScgPtpPmRealGroup.setObjects(*((_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p)))
if mibBuilder.loadTexts:xScgPtpPmRealGroup.setStatus(_A)
xScgPtpPmCompliance=ModuleCompliance((1,3,6,1,4,1,21296,2,2,2,3,33,3,1,1))
xScgPtpPmCompliance.setObjects((_B,_q))
if mibBuilder.loadTexts:xScgPtpPmCompliance.setStatus(_A)
xScgPtpPmRealCompliance=ModuleCompliance((1,3,6,1,4,1,21296,2,2,2,3,33,3,1,2))
xScgPtpPmRealCompliance.setObjects((_B,_r))
if mibBuilder.loadTexts:xScgPtpPmRealCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'xScgPtpPmMIB':xScgPtpPmMIB,'xScgPtpPmRealTable':xScgPtpPmRealTable,'xScgPtpPmRealEntry':xScgPtpPmRealEntry,_i:xScgPtpPmRealChanScgOpt,_j:xScgPtpPmRealChanScgOpr,_k:xScgPtpPmRealTxEdfaOpr,_l:xScgPtpPmRealTxEdfaOpt,_m:xScgPtpPmRealTxEdfaLbc,_n:xScgPtpPmRealRxEdfaOpr,_o:xScgPtpPmRealRxEdfaOpt,_p:xScgPtpPmRealRxEdfaLbc,'xScgPtpPmTable':xScgPtpPmTable,'xScgPtpPmEntry':xScgPtpPmEntry,_H:xScgPtpPmTimestamp,_G:xScgPtpPmSampleDuration,_J:xScgPtpPmValidity,_K:xScgPtpPmTxEdfaOprMin,_L:xScgPtpPmTxEdfaOprMax,_M:xScgPtpPmTxEdfaOprAve,_N:xScgPtpPmTxEdfaOptMin,_O:xScgPtpPmTxEdfaOptMax,_P:xScgPtpPmTxEdfaOptAve,_Q:xScgPtpPmTxEdfaLbcMin,_R:xScgPtpPmTxEdfaLbcMax,_S:xScgPtpPmTxEdfaLbcAve,_T:xScgPtpPmRxEdfaOprMin,_U:xScgPtpPmRxEdfaOprMax,_V:xScgPtpPmRxEdfaOprAve,_W:xScgPtpPmRxEdfaOptMin,_X:xScgPtpPmRxEdfaOptMax,_Y:xScgPtpPmRxEdfaOptAve,_Z:xScgPtpPmRxEdfaLbcMin,_a:xScgPtpPmRxEdfaLbcMax,_b:xScgPtpPmRxEdfaLbcAve,_c:xScgPtpPmChanScgOptMin,_d:xScgPtpPmChanScgOptMax,_e:xScgPtpPmChanScgOptAve,_f:xScgPtpPmChanScgOprMin,_g:xScgPtpPmChanScgOprMax,_h:xScgPtpPmChanScgOprAve,'xScgPtpPmConformance':xScgPtpPmConformance,'xScgPtpPmCompliances':xScgPtpPmCompliances,'xScgPtpPmCompliance':xScgPtpPmCompliance,'xScgPtpPmRealCompliance':xScgPtpPmRealCompliance,'xScgPtpPmGroups':xScgPtpPmGroups,_q:xScgPtpPmGroup,_r:xScgPtpPmRealGroup})