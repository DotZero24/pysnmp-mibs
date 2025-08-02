_s='bandPtpPmRealGroup'
_r='bandPtpPmGroup'
_q='bandPtpPmRealOptOsaTapRatio'
_p='bandPtpPmRealTxEdfaLBC'
_o='bandPtpPmRealRxEdfaLBC'
_n='bandPtpPmRealTxEdfaOpr'
_m='bandPtpPmRealRxEdfaOpr'
_l='bandPtpPmRealTxEdfaOpt'
_k='bandPtpPmRealRxEdfaOpt'
_j='bandPtpPmRealOpr'
_i='bandPtpPmRealOpt'
_h='bandPtpTxEdfaLBCAve'
_g='bandPtpTxEdfaLBCMax'
_f='bandPtpTxEdfaLBCMin'
_e='bandPtpRxEdfaLBCAve'
_d='bandPtpRxEdfaLBCMax'
_c='bandPtpRxEdfaLBCMin'
_b='bandPtpPmTxEdfaOprAve'
_a='bandPtpPmTxEdfaOprMax'
_Z='bandPtpPmTxEdfaOprMin'
_Y='bandPtpPmRxEdfaOprAve'
_X='bandPtpPmRxEdfaOprMax'
_W='bandPtpPmRxEdfaOprMin'
_V='bandPtpPmTxEdfaOptAve'
_U='bandPtpPmTxEdfaOptMax'
_T='bandPtpPmTxEdfaOptMin'
_S='bandPtpPmRxEdfaOptAve'
_R='bandPtpPmRxEdfaOptMax'
_Q='bandPtpPmRxEdfaOptMin'
_P='bandPtpPmOprAve'
_O='bandPtpPmOprMax'
_N='bandPtpPmOprMin'
_M='bandPtpPmOptAve'
_L='bandPtpPmOptMax'
_K='bandPtpPmOptMin'
_J='bandPtpPmValidity'
_I='not-accessible'
_H='bandPtpPmTimestamp'
_G='bandPtpPmSampleDuration'
_F='Integer32'
_E='ifIndex'
_D='IF-MIB'
_C='read-only'
_B='INFINERA-PM-BANDPTP-MIB'
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
bandPtpPmMIB=ModuleIdentity((1,3,6,1,4,1,21296,2,2,2,3,81))
if mibBuilder.loadTexts:bandPtpPmMIB.setRevisions(('2014-02-17 00:00',))
_BandPtpPmRealTable_Object=MibTable
bandPtpPmRealTable=_BandPtpPmRealTable_Object((1,3,6,1,4,1,21296,2,2,2,3,81,1))
if mibBuilder.loadTexts:bandPtpPmRealTable.setStatus(_A)
_BandPtpPmRealEntry_Object=MibTableRow
bandPtpPmRealEntry=_BandPtpPmRealEntry_Object((1,3,6,1,4,1,21296,2,2,2,3,81,1,1))
bandPtpPmRealEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:bandPtpPmRealEntry.setStatus(_A)
_BandPtpPmRealOpt_Type=FloatHundredths
_BandPtpPmRealOpt_Object=MibTableColumn
bandPtpPmRealOpt=_BandPtpPmRealOpt_Object((1,3,6,1,4,1,21296,2,2,2,3,81,1,1,1),_BandPtpPmRealOpt_Type())
bandPtpPmRealOpt.setMaxAccess(_C)
if mibBuilder.loadTexts:bandPtpPmRealOpt.setStatus(_A)
_BandPtpPmRealOpr_Type=FloatHundredths
_BandPtpPmRealOpr_Object=MibTableColumn
bandPtpPmRealOpr=_BandPtpPmRealOpr_Object((1,3,6,1,4,1,21296,2,2,2,3,81,1,1,2),_BandPtpPmRealOpr_Type())
bandPtpPmRealOpr.setMaxAccess(_C)
if mibBuilder.loadTexts:bandPtpPmRealOpr.setStatus(_A)
_BandPtpPmRealRxEdfaOpt_Type=FloatHundredths
_BandPtpPmRealRxEdfaOpt_Object=MibTableColumn
bandPtpPmRealRxEdfaOpt=_BandPtpPmRealRxEdfaOpt_Object((1,3,6,1,4,1,21296,2,2,2,3,81,1,1,3),_BandPtpPmRealRxEdfaOpt_Type())
bandPtpPmRealRxEdfaOpt.setMaxAccess(_C)
if mibBuilder.loadTexts:bandPtpPmRealRxEdfaOpt.setStatus(_A)
_BandPtpPmRealTxEdfaOpt_Type=FloatHundredths
_BandPtpPmRealTxEdfaOpt_Object=MibTableColumn
bandPtpPmRealTxEdfaOpt=_BandPtpPmRealTxEdfaOpt_Object((1,3,6,1,4,1,21296,2,2,2,3,81,1,1,4),_BandPtpPmRealTxEdfaOpt_Type())
bandPtpPmRealTxEdfaOpt.setMaxAccess(_C)
if mibBuilder.loadTexts:bandPtpPmRealTxEdfaOpt.setStatus(_A)
_BandPtpPmRealRxEdfaOpr_Type=FloatHundredths
_BandPtpPmRealRxEdfaOpr_Object=MibTableColumn
bandPtpPmRealRxEdfaOpr=_BandPtpPmRealRxEdfaOpr_Object((1,3,6,1,4,1,21296,2,2,2,3,81,1,1,5),_BandPtpPmRealRxEdfaOpr_Type())
bandPtpPmRealRxEdfaOpr.setMaxAccess(_C)
if mibBuilder.loadTexts:bandPtpPmRealRxEdfaOpr.setStatus(_A)
_BandPtpPmRealTxEdfaOpr_Type=FloatHundredths
_BandPtpPmRealTxEdfaOpr_Object=MibTableColumn
bandPtpPmRealTxEdfaOpr=_BandPtpPmRealTxEdfaOpr_Object((1,3,6,1,4,1,21296,2,2,2,3,81,1,1,6),_BandPtpPmRealTxEdfaOpr_Type())
bandPtpPmRealTxEdfaOpr.setMaxAccess(_C)
if mibBuilder.loadTexts:bandPtpPmRealTxEdfaOpr.setStatus(_A)
_BandPtpPmRealRxEdfaLBC_Type=FloatHundredths
_BandPtpPmRealRxEdfaLBC_Object=MibTableColumn
bandPtpPmRealRxEdfaLBC=_BandPtpPmRealRxEdfaLBC_Object((1,3,6,1,4,1,21296,2,2,2,3,81,1,1,7),_BandPtpPmRealRxEdfaLBC_Type())
bandPtpPmRealRxEdfaLBC.setMaxAccess(_C)
if mibBuilder.loadTexts:bandPtpPmRealRxEdfaLBC.setStatus(_A)
_BandPtpPmRealTxEdfaLBC_Type=FloatHundredths
_BandPtpPmRealTxEdfaLBC_Object=MibTableColumn
bandPtpPmRealTxEdfaLBC=_BandPtpPmRealTxEdfaLBC_Object((1,3,6,1,4,1,21296,2,2,2,3,81,1,1,8),_BandPtpPmRealTxEdfaLBC_Type())
bandPtpPmRealTxEdfaLBC.setMaxAccess(_C)
if mibBuilder.loadTexts:bandPtpPmRealTxEdfaLBC.setStatus(_A)
_BandPtpPmRealOptOsaTapRatio_Type=FloatHundredths
_BandPtpPmRealOptOsaTapRatio_Object=MibTableColumn
bandPtpPmRealOptOsaTapRatio=_BandPtpPmRealOptOsaTapRatio_Object((1,3,6,1,4,1,21296,2,2,2,3,81,1,1,9),_BandPtpPmRealOptOsaTapRatio_Type())
bandPtpPmRealOptOsaTapRatio.setMaxAccess(_C)
if mibBuilder.loadTexts:bandPtpPmRealOptOsaTapRatio.setStatus(_A)
_BandPtpPmTable_Object=MibTable
bandPtpPmTable=_BandPtpPmTable_Object((1,3,6,1,4,1,21296,2,2,2,3,81,2))
if mibBuilder.loadTexts:bandPtpPmTable.setStatus(_A)
_BandPtpPmEntry_Object=MibTableRow
bandPtpPmEntry=_BandPtpPmEntry_Object((1,3,6,1,4,1,21296,2,2,2,3,81,2,1))
bandPtpPmEntry.setIndexNames((0,_D,_E),(0,_B,_G),(0,_B,_H))
if mibBuilder.loadTexts:bandPtpPmEntry.setStatus(_A)
class _BandPtpPmTimestamp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_BandPtpPmTimestamp_Type.__name__=_F
_BandPtpPmTimestamp_Object=MibTableColumn
bandPtpPmTimestamp=_BandPtpPmTimestamp_Object((1,3,6,1,4,1,21296,2,2,2,3,81,2,1,1),_BandPtpPmTimestamp_Type())
bandPtpPmTimestamp.setMaxAccess(_I)
if mibBuilder.loadTexts:bandPtpPmTimestamp.setStatus(_A)
class _BandPtpPmSampleDuration_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('fifteenMinutes',1),('day',2)))
_BandPtpPmSampleDuration_Type.__name__=_F
_BandPtpPmSampleDuration_Object=MibTableColumn
bandPtpPmSampleDuration=_BandPtpPmSampleDuration_Object((1,3,6,1,4,1,21296,2,2,2,3,81,2,1,2),_BandPtpPmSampleDuration_Type())
bandPtpPmSampleDuration.setMaxAccess(_I)
if mibBuilder.loadTexts:bandPtpPmSampleDuration.setStatus(_A)
_BandPtpPmValidity_Type=TruthValue
_BandPtpPmValidity_Object=MibTableColumn
bandPtpPmValidity=_BandPtpPmValidity_Object((1,3,6,1,4,1,21296,2,2,2,3,81,2,1,3),_BandPtpPmValidity_Type())
bandPtpPmValidity.setMaxAccess(_C)
if mibBuilder.loadTexts:bandPtpPmValidity.setStatus(_A)
_BandPtpPmOptMin_Type=FloatHundredths
_BandPtpPmOptMin_Object=MibTableColumn
bandPtpPmOptMin=_BandPtpPmOptMin_Object((1,3,6,1,4,1,21296,2,2,2,3,81,2,1,4),_BandPtpPmOptMin_Type())
bandPtpPmOptMin.setMaxAccess(_C)
if mibBuilder.loadTexts:bandPtpPmOptMin.setStatus(_A)
_BandPtpPmOptMax_Type=FloatHundredths
_BandPtpPmOptMax_Object=MibTableColumn
bandPtpPmOptMax=_BandPtpPmOptMax_Object((1,3,6,1,4,1,21296,2,2,2,3,81,2,1,5),_BandPtpPmOptMax_Type())
bandPtpPmOptMax.setMaxAccess(_C)
if mibBuilder.loadTexts:bandPtpPmOptMax.setStatus(_A)
_BandPtpPmOptAve_Type=FloatHundredths
_BandPtpPmOptAve_Object=MibTableColumn
bandPtpPmOptAve=_BandPtpPmOptAve_Object((1,3,6,1,4,1,21296,2,2,2,3,81,2,1,6),_BandPtpPmOptAve_Type())
bandPtpPmOptAve.setMaxAccess(_C)
if mibBuilder.loadTexts:bandPtpPmOptAve.setStatus(_A)
_BandPtpPmOprMin_Type=FloatHundredths
_BandPtpPmOprMin_Object=MibTableColumn
bandPtpPmOprMin=_BandPtpPmOprMin_Object((1,3,6,1,4,1,21296,2,2,2,3,81,2,1,7),_BandPtpPmOprMin_Type())
bandPtpPmOprMin.setMaxAccess(_C)
if mibBuilder.loadTexts:bandPtpPmOprMin.setStatus(_A)
_BandPtpPmOprMax_Type=FloatHundredths
_BandPtpPmOprMax_Object=MibTableColumn
bandPtpPmOprMax=_BandPtpPmOprMax_Object((1,3,6,1,4,1,21296,2,2,2,3,81,2,1,8),_BandPtpPmOprMax_Type())
bandPtpPmOprMax.setMaxAccess(_C)
if mibBuilder.loadTexts:bandPtpPmOprMax.setStatus(_A)
_BandPtpPmOprAve_Type=FloatHundredths
_BandPtpPmOprAve_Object=MibTableColumn
bandPtpPmOprAve=_BandPtpPmOprAve_Object((1,3,6,1,4,1,21296,2,2,2,3,81,2,1,9),_BandPtpPmOprAve_Type())
bandPtpPmOprAve.setMaxAccess(_C)
if mibBuilder.loadTexts:bandPtpPmOprAve.setStatus(_A)
_BandPtpPmRxEdfaOptMin_Type=FloatHundredths
_BandPtpPmRxEdfaOptMin_Object=MibTableColumn
bandPtpPmRxEdfaOptMin=_BandPtpPmRxEdfaOptMin_Object((1,3,6,1,4,1,21296,2,2,2,3,81,2,1,10),_BandPtpPmRxEdfaOptMin_Type())
bandPtpPmRxEdfaOptMin.setMaxAccess(_C)
if mibBuilder.loadTexts:bandPtpPmRxEdfaOptMin.setStatus(_A)
_BandPtpPmRxEdfaOptMax_Type=FloatHundredths
_BandPtpPmRxEdfaOptMax_Object=MibTableColumn
bandPtpPmRxEdfaOptMax=_BandPtpPmRxEdfaOptMax_Object((1,3,6,1,4,1,21296,2,2,2,3,81,2,1,11),_BandPtpPmRxEdfaOptMax_Type())
bandPtpPmRxEdfaOptMax.setMaxAccess(_C)
if mibBuilder.loadTexts:bandPtpPmRxEdfaOptMax.setStatus(_A)
_BandPtpPmRxEdfaOptAve_Type=FloatHundredths
_BandPtpPmRxEdfaOptAve_Object=MibTableColumn
bandPtpPmRxEdfaOptAve=_BandPtpPmRxEdfaOptAve_Object((1,3,6,1,4,1,21296,2,2,2,3,81,2,1,12),_BandPtpPmRxEdfaOptAve_Type())
bandPtpPmRxEdfaOptAve.setMaxAccess(_C)
if mibBuilder.loadTexts:bandPtpPmRxEdfaOptAve.setStatus(_A)
_BandPtpPmTxEdfaOptMin_Type=FloatHundredths
_BandPtpPmTxEdfaOptMin_Object=MibTableColumn
bandPtpPmTxEdfaOptMin=_BandPtpPmTxEdfaOptMin_Object((1,3,6,1,4,1,21296,2,2,2,3,81,2,1,13),_BandPtpPmTxEdfaOptMin_Type())
bandPtpPmTxEdfaOptMin.setMaxAccess(_C)
if mibBuilder.loadTexts:bandPtpPmTxEdfaOptMin.setStatus(_A)
_BandPtpPmTxEdfaOptMax_Type=FloatHundredths
_BandPtpPmTxEdfaOptMax_Object=MibTableColumn
bandPtpPmTxEdfaOptMax=_BandPtpPmTxEdfaOptMax_Object((1,3,6,1,4,1,21296,2,2,2,3,81,2,1,14),_BandPtpPmTxEdfaOptMax_Type())
bandPtpPmTxEdfaOptMax.setMaxAccess(_C)
if mibBuilder.loadTexts:bandPtpPmTxEdfaOptMax.setStatus(_A)
_BandPtpPmTxEdfaOptAve_Type=FloatHundredths
_BandPtpPmTxEdfaOptAve_Object=MibTableColumn
bandPtpPmTxEdfaOptAve=_BandPtpPmTxEdfaOptAve_Object((1,3,6,1,4,1,21296,2,2,2,3,81,2,1,15),_BandPtpPmTxEdfaOptAve_Type())
bandPtpPmTxEdfaOptAve.setMaxAccess(_C)
if mibBuilder.loadTexts:bandPtpPmTxEdfaOptAve.setStatus(_A)
_BandPtpPmRxEdfaOprMin_Type=FloatHundredths
_BandPtpPmRxEdfaOprMin_Object=MibTableColumn
bandPtpPmRxEdfaOprMin=_BandPtpPmRxEdfaOprMin_Object((1,3,6,1,4,1,21296,2,2,2,3,81,2,1,16),_BandPtpPmRxEdfaOprMin_Type())
bandPtpPmRxEdfaOprMin.setMaxAccess(_C)
if mibBuilder.loadTexts:bandPtpPmRxEdfaOprMin.setStatus(_A)
_BandPtpPmRxEdfaOprMax_Type=FloatHundredths
_BandPtpPmRxEdfaOprMax_Object=MibTableColumn
bandPtpPmRxEdfaOprMax=_BandPtpPmRxEdfaOprMax_Object((1,3,6,1,4,1,21296,2,2,2,3,81,2,1,17),_BandPtpPmRxEdfaOprMax_Type())
bandPtpPmRxEdfaOprMax.setMaxAccess(_C)
if mibBuilder.loadTexts:bandPtpPmRxEdfaOprMax.setStatus(_A)
_BandPtpPmRxEdfaOprAve_Type=FloatHundredths
_BandPtpPmRxEdfaOprAve_Object=MibTableColumn
bandPtpPmRxEdfaOprAve=_BandPtpPmRxEdfaOprAve_Object((1,3,6,1,4,1,21296,2,2,2,3,81,2,1,18),_BandPtpPmRxEdfaOprAve_Type())
bandPtpPmRxEdfaOprAve.setMaxAccess(_C)
if mibBuilder.loadTexts:bandPtpPmRxEdfaOprAve.setStatus(_A)
_BandPtpPmTxEdfaOprMin_Type=FloatHundredths
_BandPtpPmTxEdfaOprMin_Object=MibTableColumn
bandPtpPmTxEdfaOprMin=_BandPtpPmTxEdfaOprMin_Object((1,3,6,1,4,1,21296,2,2,2,3,81,2,1,19),_BandPtpPmTxEdfaOprMin_Type())
bandPtpPmTxEdfaOprMin.setMaxAccess(_C)
if mibBuilder.loadTexts:bandPtpPmTxEdfaOprMin.setStatus(_A)
_BandPtpPmTxEdfaOprMax_Type=FloatHundredths
_BandPtpPmTxEdfaOprMax_Object=MibTableColumn
bandPtpPmTxEdfaOprMax=_BandPtpPmTxEdfaOprMax_Object((1,3,6,1,4,1,21296,2,2,2,3,81,2,1,20),_BandPtpPmTxEdfaOprMax_Type())
bandPtpPmTxEdfaOprMax.setMaxAccess(_C)
if mibBuilder.loadTexts:bandPtpPmTxEdfaOprMax.setStatus(_A)
_BandPtpPmTxEdfaOprAve_Type=FloatHundredths
_BandPtpPmTxEdfaOprAve_Object=MibTableColumn
bandPtpPmTxEdfaOprAve=_BandPtpPmTxEdfaOprAve_Object((1,3,6,1,4,1,21296,2,2,2,3,81,2,1,21),_BandPtpPmTxEdfaOprAve_Type())
bandPtpPmTxEdfaOprAve.setMaxAccess(_C)
if mibBuilder.loadTexts:bandPtpPmTxEdfaOprAve.setStatus(_A)
_BandPtpRxEdfaLBCMin_Type=FloatHundredths
_BandPtpRxEdfaLBCMin_Object=MibTableColumn
bandPtpRxEdfaLBCMin=_BandPtpRxEdfaLBCMin_Object((1,3,6,1,4,1,21296,2,2,2,3,81,2,1,22),_BandPtpRxEdfaLBCMin_Type())
bandPtpRxEdfaLBCMin.setMaxAccess(_C)
if mibBuilder.loadTexts:bandPtpRxEdfaLBCMin.setStatus(_A)
_BandPtpRxEdfaLBCMax_Type=FloatHundredths
_BandPtpRxEdfaLBCMax_Object=MibTableColumn
bandPtpRxEdfaLBCMax=_BandPtpRxEdfaLBCMax_Object((1,3,6,1,4,1,21296,2,2,2,3,81,2,1,23),_BandPtpRxEdfaLBCMax_Type())
bandPtpRxEdfaLBCMax.setMaxAccess(_C)
if mibBuilder.loadTexts:bandPtpRxEdfaLBCMax.setStatus(_A)
_BandPtpRxEdfaLBCAve_Type=FloatHundredths
_BandPtpRxEdfaLBCAve_Object=MibTableColumn
bandPtpRxEdfaLBCAve=_BandPtpRxEdfaLBCAve_Object((1,3,6,1,4,1,21296,2,2,2,3,81,2,1,24),_BandPtpRxEdfaLBCAve_Type())
bandPtpRxEdfaLBCAve.setMaxAccess(_C)
if mibBuilder.loadTexts:bandPtpRxEdfaLBCAve.setStatus(_A)
_BandPtpTxEdfaLBCMin_Type=FloatHundredths
_BandPtpTxEdfaLBCMin_Object=MibTableColumn
bandPtpTxEdfaLBCMin=_BandPtpTxEdfaLBCMin_Object((1,3,6,1,4,1,21296,2,2,2,3,81,2,1,25),_BandPtpTxEdfaLBCMin_Type())
bandPtpTxEdfaLBCMin.setMaxAccess(_C)
if mibBuilder.loadTexts:bandPtpTxEdfaLBCMin.setStatus(_A)
_BandPtpTxEdfaLBCMax_Type=FloatHundredths
_BandPtpTxEdfaLBCMax_Object=MibTableColumn
bandPtpTxEdfaLBCMax=_BandPtpTxEdfaLBCMax_Object((1,3,6,1,4,1,21296,2,2,2,3,81,2,1,26),_BandPtpTxEdfaLBCMax_Type())
bandPtpTxEdfaLBCMax.setMaxAccess(_C)
if mibBuilder.loadTexts:bandPtpTxEdfaLBCMax.setStatus(_A)
_BandPtpTxEdfaLBCAve_Type=FloatHundredths
_BandPtpTxEdfaLBCAve_Object=MibTableColumn
bandPtpTxEdfaLBCAve=_BandPtpTxEdfaLBCAve_Object((1,3,6,1,4,1,21296,2,2,2,3,81,2,1,27),_BandPtpTxEdfaLBCAve_Type())
bandPtpTxEdfaLBCAve.setMaxAccess(_C)
if mibBuilder.loadTexts:bandPtpTxEdfaLBCAve.setStatus(_A)
_BandPtpPmConformance_ObjectIdentity=ObjectIdentity
bandPtpPmConformance=_BandPtpPmConformance_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,3,81,3))
_BandPtpPmCompliances_ObjectIdentity=ObjectIdentity
bandPtpPmCompliances=_BandPtpPmCompliances_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,3,81,3,1))
_BandPtpPmGroups_ObjectIdentity=ObjectIdentity
bandPtpPmGroups=_BandPtpPmGroups_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,3,81,3,2))
bandPtpPmGroup=ObjectGroup((1,3,6,1,4,1,21296,2,2,2,3,81,3,2,1))
bandPtpPmGroup.setObjects(*((_B,_H),(_B,_G),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h)))
if mibBuilder.loadTexts:bandPtpPmGroup.setStatus(_A)
bandPtpPmRealGroup=ObjectGroup((1,3,6,1,4,1,21296,2,2,2,3,81,3,2,2))
bandPtpPmRealGroup.setObjects(*((_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q)))
if mibBuilder.loadTexts:bandPtpPmRealGroup.setStatus(_A)
bandPtpPmCompliance=ModuleCompliance((1,3,6,1,4,1,21296,2,2,2,3,81,3,1,1))
bandPtpPmCompliance.setObjects((_B,_r))
if mibBuilder.loadTexts:bandPtpPmCompliance.setStatus(_A)
bandPtpPmRealCompliance=ModuleCompliance((1,3,6,1,4,1,21296,2,2,2,3,81,3,1,2))
bandPtpPmRealCompliance.setObjects((_B,_s))
if mibBuilder.loadTexts:bandPtpPmRealCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'bandPtpPmMIB':bandPtpPmMIB,'bandPtpPmRealTable':bandPtpPmRealTable,'bandPtpPmRealEntry':bandPtpPmRealEntry,_i:bandPtpPmRealOpt,_j:bandPtpPmRealOpr,_k:bandPtpPmRealRxEdfaOpt,_l:bandPtpPmRealTxEdfaOpt,_m:bandPtpPmRealRxEdfaOpr,_n:bandPtpPmRealTxEdfaOpr,_o:bandPtpPmRealRxEdfaLBC,_p:bandPtpPmRealTxEdfaLBC,_q:bandPtpPmRealOptOsaTapRatio,'bandPtpPmTable':bandPtpPmTable,'bandPtpPmEntry':bandPtpPmEntry,_H:bandPtpPmTimestamp,_G:bandPtpPmSampleDuration,_J:bandPtpPmValidity,_K:bandPtpPmOptMin,_L:bandPtpPmOptMax,_M:bandPtpPmOptAve,_N:bandPtpPmOprMin,_O:bandPtpPmOprMax,_P:bandPtpPmOprAve,_Q:bandPtpPmRxEdfaOptMin,_R:bandPtpPmRxEdfaOptMax,_S:bandPtpPmRxEdfaOptAve,_T:bandPtpPmTxEdfaOptMin,_U:bandPtpPmTxEdfaOptMax,_V:bandPtpPmTxEdfaOptAve,_W:bandPtpPmRxEdfaOprMin,_X:bandPtpPmRxEdfaOprMax,_Y:bandPtpPmRxEdfaOprAve,_Z:bandPtpPmTxEdfaOprMin,_a:bandPtpPmTxEdfaOprMax,_b:bandPtpPmTxEdfaOprAve,_c:bandPtpRxEdfaLBCMin,_d:bandPtpRxEdfaLBCMax,_e:bandPtpRxEdfaLBCAve,_f:bandPtpTxEdfaLBCMin,_g:bandPtpTxEdfaLBCMax,_h:bandPtpTxEdfaLBCAve,'bandPtpPmConformance':bandPtpPmConformance,'bandPtpPmCompliances':bandPtpPmCompliances,'bandPtpPmCompliance':bandPtpPmCompliance,'bandPtpPmRealCompliance':bandPtpPmRealCompliance,'bandPtpPmGroups':bandPtpPmGroups,_r:bandPtpPmGroup,_s:bandPtpPmRealGroup})