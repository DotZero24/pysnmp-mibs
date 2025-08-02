_A3='bandCtpPmRealGroup'
_A2='bandCtpPmGroup'
_A1='bandCtpPmRealOptOsaTapRatio'
_A0='bandCtpPmRealRxEdfaOpt'
_z='bandCtpPmRealTxEdfaOpr'
_y='bandCtpPmRealPostOsaTapRatio'
_x='bandCtpPmRealOprQ'
_w='bandCtpPmRealDampUpdateTS'
_v='bandCtpPmRealBmmPostEdfa'
_u='bandCtpPmRealBmmEdfaLbc2'
_t='bandCtpPmRealBmmEdfaLbc1'
_s='bandCtpPmRealBandOptNum'
_r='bandCtpPmRealBandOchOpt'
_q='bandCtpPmRealBandOptTx'
_p='bandCtpPmRealBmmBandEdfaLbcTx'
_o='bandCtpPmRealOamBandTxEdfaLbc2'
_n='bandCtpPmRealOamBandTxEdfaLbc1'
_m='bandCtpPmRealBandOprNum'
_l='bandCtpPmRealBandOchOpr'
_k='bandCtpPmRealBandOpr'
_j='bandCtpPmRealNetSpanLoss'
_i='bandCtpPmRealOchSpanLoss'
_h='bandCtpPmOptOsaTapRatioAve'
_g='bandCtpPmOptOsaTapRatioMax'
_f='bandCtpPmOptOsaTapRatioMin'
_e='bandCtpPmRxEdfaOptAve'
_d='bandCtpPmRxEdfaOptMax'
_c='bandCtpPmRxEdfaOptMin'
_b='bandCtpPmTxEdfaOprAve'
_a='bandCtpPmTxEdfaOprMax'
_Z='bandCtpPmTxEdfaOprMin'
_Y='bandCtpPmBmmPostEdfaAve'
_X='bandCtpPmBmmPostEdfaMax'
_W='bandCtpPmBmmPostEdfaMin'
_V='bandCtpPmBandOptAve'
_U='bandCtpPmBandOptMax'
_T='bandCtpPmBandOptMin'
_S='bandCtpPmBandOprAve'
_R='bandCtpPmBandOprMax'
_Q='bandCtpPmBandOprMin'
_P='bandCtpPmNetSpanLossAve'
_O='bandCtpPmNetSpanLossMax'
_N='bandCtpPmNetSpanLossMin'
_M='bandCtpPmOchSpanLossAve'
_L='bandCtpPmOchSpanLossMax'
_K='bandCtpPmOchSpanLossMin'
_J='bandCtpPmValidity'
_I='not-accessible'
_H='bandCtpPmTimestamp'
_G='bandCtpPmSampleDuration'
_F='Integer32'
_E='ifIndex'
_D='IF-MIB'
_C='read-only'
_B='INFINERA-PM-BANDCTP-MIB'
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
bandCtpPmMIB=ModuleIdentity((1,3,6,1,4,1,21296,2,2,2,3,1))
if mibBuilder.loadTexts:bandCtpPmMIB.setRevisions(('2008-10-20 00:00',))
_BandCtpPmRealTable_Object=MibTable
bandCtpPmRealTable=_BandCtpPmRealTable_Object((1,3,6,1,4,1,21296,2,2,2,3,1,1))
if mibBuilder.loadTexts:bandCtpPmRealTable.setStatus(_A)
_BandCtpPmRealEntry_Object=MibTableRow
bandCtpPmRealEntry=_BandCtpPmRealEntry_Object((1,3,6,1,4,1,21296,2,2,2,3,1,1,1))
bandCtpPmRealEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:bandCtpPmRealEntry.setStatus(_A)
_BandCtpPmRealOchSpanLoss_Type=FloatHundredths
_BandCtpPmRealOchSpanLoss_Object=MibTableColumn
bandCtpPmRealOchSpanLoss=_BandCtpPmRealOchSpanLoss_Object((1,3,6,1,4,1,21296,2,2,2,3,1,1,1,1),_BandCtpPmRealOchSpanLoss_Type())
bandCtpPmRealOchSpanLoss.setMaxAccess(_C)
if mibBuilder.loadTexts:bandCtpPmRealOchSpanLoss.setStatus(_A)
_BandCtpPmRealNetSpanLoss_Type=FloatHundredths
_BandCtpPmRealNetSpanLoss_Object=MibTableColumn
bandCtpPmRealNetSpanLoss=_BandCtpPmRealNetSpanLoss_Object((1,3,6,1,4,1,21296,2,2,2,3,1,1,1,2),_BandCtpPmRealNetSpanLoss_Type())
bandCtpPmRealNetSpanLoss.setMaxAccess(_C)
if mibBuilder.loadTexts:bandCtpPmRealNetSpanLoss.setStatus(_A)
_BandCtpPmRealBandOpr_Type=FloatHundredths
_BandCtpPmRealBandOpr_Object=MibTableColumn
bandCtpPmRealBandOpr=_BandCtpPmRealBandOpr_Object((1,3,6,1,4,1,21296,2,2,2,3,1,1,1,3),_BandCtpPmRealBandOpr_Type())
bandCtpPmRealBandOpr.setMaxAccess(_C)
if mibBuilder.loadTexts:bandCtpPmRealBandOpr.setStatus(_A)
_BandCtpPmRealBandOchOpr_Type=FloatHundredths
_BandCtpPmRealBandOchOpr_Object=MibTableColumn
bandCtpPmRealBandOchOpr=_BandCtpPmRealBandOchOpr_Object((1,3,6,1,4,1,21296,2,2,2,3,1,1,1,4),_BandCtpPmRealBandOchOpr_Type())
bandCtpPmRealBandOchOpr.setMaxAccess(_C)
if mibBuilder.loadTexts:bandCtpPmRealBandOchOpr.setStatus(_A)
_BandCtpPmRealBandOprNum_Type=FloatHundredths
_BandCtpPmRealBandOprNum_Object=MibTableColumn
bandCtpPmRealBandOprNum=_BandCtpPmRealBandOprNum_Object((1,3,6,1,4,1,21296,2,2,2,3,1,1,1,5),_BandCtpPmRealBandOprNum_Type())
bandCtpPmRealBandOprNum.setMaxAccess(_C)
if mibBuilder.loadTexts:bandCtpPmRealBandOprNum.setStatus(_A)
_BandCtpPmRealOamBandTxEdfaLbc1_Type=FloatHundredths
_BandCtpPmRealOamBandTxEdfaLbc1_Object=MibTableColumn
bandCtpPmRealOamBandTxEdfaLbc1=_BandCtpPmRealOamBandTxEdfaLbc1_Object((1,3,6,1,4,1,21296,2,2,2,3,1,1,1,6),_BandCtpPmRealOamBandTxEdfaLbc1_Type())
bandCtpPmRealOamBandTxEdfaLbc1.setMaxAccess(_C)
if mibBuilder.loadTexts:bandCtpPmRealOamBandTxEdfaLbc1.setStatus(_A)
_BandCtpPmRealOamBandTxEdfaLbc2_Type=FloatHundredths
_BandCtpPmRealOamBandTxEdfaLbc2_Object=MibTableColumn
bandCtpPmRealOamBandTxEdfaLbc2=_BandCtpPmRealOamBandTxEdfaLbc2_Object((1,3,6,1,4,1,21296,2,2,2,3,1,1,1,7),_BandCtpPmRealOamBandTxEdfaLbc2_Type())
bandCtpPmRealOamBandTxEdfaLbc2.setMaxAccess(_C)
if mibBuilder.loadTexts:bandCtpPmRealOamBandTxEdfaLbc2.setStatus(_A)
_BandCtpPmRealBmmBandEdfaLbcTx_Type=FloatHundredths
_BandCtpPmRealBmmBandEdfaLbcTx_Object=MibTableColumn
bandCtpPmRealBmmBandEdfaLbcTx=_BandCtpPmRealBmmBandEdfaLbcTx_Object((1,3,6,1,4,1,21296,2,2,2,3,1,1,1,8),_BandCtpPmRealBmmBandEdfaLbcTx_Type())
bandCtpPmRealBmmBandEdfaLbcTx.setMaxAccess(_C)
if mibBuilder.loadTexts:bandCtpPmRealBmmBandEdfaLbcTx.setStatus(_A)
_BandCtpPmRealBandOptTx_Type=FloatHundredths
_BandCtpPmRealBandOptTx_Object=MibTableColumn
bandCtpPmRealBandOptTx=_BandCtpPmRealBandOptTx_Object((1,3,6,1,4,1,21296,2,2,2,3,1,1,1,9),_BandCtpPmRealBandOptTx_Type())
bandCtpPmRealBandOptTx.setMaxAccess(_C)
if mibBuilder.loadTexts:bandCtpPmRealBandOptTx.setStatus(_A)
_BandCtpPmRealBandOchOpt_Type=FloatHundredths
_BandCtpPmRealBandOchOpt_Object=MibTableColumn
bandCtpPmRealBandOchOpt=_BandCtpPmRealBandOchOpt_Object((1,3,6,1,4,1,21296,2,2,2,3,1,1,1,10),_BandCtpPmRealBandOchOpt_Type())
bandCtpPmRealBandOchOpt.setMaxAccess(_C)
if mibBuilder.loadTexts:bandCtpPmRealBandOchOpt.setStatus(_A)
_BandCtpPmRealBandOptNum_Type=FloatHundredths
_BandCtpPmRealBandOptNum_Object=MibTableColumn
bandCtpPmRealBandOptNum=_BandCtpPmRealBandOptNum_Object((1,3,6,1,4,1,21296,2,2,2,3,1,1,1,11),_BandCtpPmRealBandOptNum_Type())
bandCtpPmRealBandOptNum.setMaxAccess(_C)
if mibBuilder.loadTexts:bandCtpPmRealBandOptNum.setStatus(_A)
_BandCtpPmRealBmmEdfaLbc1_Type=FloatHundredths
_BandCtpPmRealBmmEdfaLbc1_Object=MibTableColumn
bandCtpPmRealBmmEdfaLbc1=_BandCtpPmRealBmmEdfaLbc1_Object((1,3,6,1,4,1,21296,2,2,2,3,1,1,1,12),_BandCtpPmRealBmmEdfaLbc1_Type())
bandCtpPmRealBmmEdfaLbc1.setMaxAccess(_C)
if mibBuilder.loadTexts:bandCtpPmRealBmmEdfaLbc1.setStatus(_A)
_BandCtpPmRealBmmEdfaLbc2_Type=FloatHundredths
_BandCtpPmRealBmmEdfaLbc2_Object=MibTableColumn
bandCtpPmRealBmmEdfaLbc2=_BandCtpPmRealBmmEdfaLbc2_Object((1,3,6,1,4,1,21296,2,2,2,3,1,1,1,13),_BandCtpPmRealBmmEdfaLbc2_Type())
bandCtpPmRealBmmEdfaLbc2.setMaxAccess(_C)
if mibBuilder.loadTexts:bandCtpPmRealBmmEdfaLbc2.setStatus(_A)
_BandCtpPmRealBmmPostEdfa_Type=FloatHundredths
_BandCtpPmRealBmmPostEdfa_Object=MibTableColumn
bandCtpPmRealBmmPostEdfa=_BandCtpPmRealBmmPostEdfa_Object((1,3,6,1,4,1,21296,2,2,2,3,1,1,1,14),_BandCtpPmRealBmmPostEdfa_Type())
bandCtpPmRealBmmPostEdfa.setMaxAccess(_C)
if mibBuilder.loadTexts:bandCtpPmRealBmmPostEdfa.setStatus(_A)
_BandCtpPmRealDampUpdateTS_Type=DisplayString
_BandCtpPmRealDampUpdateTS_Object=MibTableColumn
bandCtpPmRealDampUpdateTS=_BandCtpPmRealDampUpdateTS_Object((1,3,6,1,4,1,21296,2,2,2,3,1,1,1,15),_BandCtpPmRealDampUpdateTS_Type())
bandCtpPmRealDampUpdateTS.setMaxAccess(_C)
if mibBuilder.loadTexts:bandCtpPmRealDampUpdateTS.setStatus(_A)
_BandCtpPmRealOprQ_Type=DisplayString
_BandCtpPmRealOprQ_Object=MibTableColumn
bandCtpPmRealOprQ=_BandCtpPmRealOprQ_Object((1,3,6,1,4,1,21296,2,2,2,3,1,1,1,16),_BandCtpPmRealOprQ_Type())
bandCtpPmRealOprQ.setMaxAccess(_C)
if mibBuilder.loadTexts:bandCtpPmRealOprQ.setStatus(_A)
_BandCtpPmRealPostOsaTapRatio_Type=FloatHundredths
_BandCtpPmRealPostOsaTapRatio_Object=MibTableColumn
bandCtpPmRealPostOsaTapRatio=_BandCtpPmRealPostOsaTapRatio_Object((1,3,6,1,4,1,21296,2,2,2,3,1,1,1,17),_BandCtpPmRealPostOsaTapRatio_Type())
bandCtpPmRealPostOsaTapRatio.setMaxAccess(_C)
if mibBuilder.loadTexts:bandCtpPmRealPostOsaTapRatio.setStatus(_A)
_BandCtpPmRealTxEdfaOpr_Type=FloatHundredths
_BandCtpPmRealTxEdfaOpr_Object=MibTableColumn
bandCtpPmRealTxEdfaOpr=_BandCtpPmRealTxEdfaOpr_Object((1,3,6,1,4,1,21296,2,2,2,3,1,1,1,18),_BandCtpPmRealTxEdfaOpr_Type())
bandCtpPmRealTxEdfaOpr.setMaxAccess(_C)
if mibBuilder.loadTexts:bandCtpPmRealTxEdfaOpr.setStatus(_A)
_BandCtpPmRealRxEdfaOpt_Type=FloatHundredths
_BandCtpPmRealRxEdfaOpt_Object=MibTableColumn
bandCtpPmRealRxEdfaOpt=_BandCtpPmRealRxEdfaOpt_Object((1,3,6,1,4,1,21296,2,2,2,3,1,1,1,19),_BandCtpPmRealRxEdfaOpt_Type())
bandCtpPmRealRxEdfaOpt.setMaxAccess(_C)
if mibBuilder.loadTexts:bandCtpPmRealRxEdfaOpt.setStatus(_A)
_BandCtpPmRealOptOsaTapRatio_Type=FloatHundredths
_BandCtpPmRealOptOsaTapRatio_Object=MibTableColumn
bandCtpPmRealOptOsaTapRatio=_BandCtpPmRealOptOsaTapRatio_Object((1,3,6,1,4,1,21296,2,2,2,3,1,1,1,20),_BandCtpPmRealOptOsaTapRatio_Type())
bandCtpPmRealOptOsaTapRatio.setMaxAccess(_C)
if mibBuilder.loadTexts:bandCtpPmRealOptOsaTapRatio.setStatus(_A)
_BandCtpPmTable_Object=MibTable
bandCtpPmTable=_BandCtpPmTable_Object((1,3,6,1,4,1,21296,2,2,2,3,1,2))
if mibBuilder.loadTexts:bandCtpPmTable.setStatus(_A)
_BandCtpPmEntry_Object=MibTableRow
bandCtpPmEntry=_BandCtpPmEntry_Object((1,3,6,1,4,1,21296,2,2,2,3,1,2,1))
bandCtpPmEntry.setIndexNames((0,_D,_E),(0,_B,_G),(0,_B,_H))
if mibBuilder.loadTexts:bandCtpPmEntry.setStatus(_A)
class _BandCtpPmTimestamp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_BandCtpPmTimestamp_Type.__name__=_F
_BandCtpPmTimestamp_Object=MibTableColumn
bandCtpPmTimestamp=_BandCtpPmTimestamp_Object((1,3,6,1,4,1,21296,2,2,2,3,1,2,1,1),_BandCtpPmTimestamp_Type())
bandCtpPmTimestamp.setMaxAccess(_I)
if mibBuilder.loadTexts:bandCtpPmTimestamp.setStatus(_A)
class _BandCtpPmSampleDuration_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('fifteenMinutes',1),('day',2)))
_BandCtpPmSampleDuration_Type.__name__=_F
_BandCtpPmSampleDuration_Object=MibTableColumn
bandCtpPmSampleDuration=_BandCtpPmSampleDuration_Object((1,3,6,1,4,1,21296,2,2,2,3,1,2,1,2),_BandCtpPmSampleDuration_Type())
bandCtpPmSampleDuration.setMaxAccess(_I)
if mibBuilder.loadTexts:bandCtpPmSampleDuration.setStatus(_A)
_BandCtpPmValidity_Type=TruthValue
_BandCtpPmValidity_Object=MibTableColumn
bandCtpPmValidity=_BandCtpPmValidity_Object((1,3,6,1,4,1,21296,2,2,2,3,1,2,1,3),_BandCtpPmValidity_Type())
bandCtpPmValidity.setMaxAccess(_C)
if mibBuilder.loadTexts:bandCtpPmValidity.setStatus(_A)
_BandCtpPmOchSpanLossMin_Type=FloatHundredths
_BandCtpPmOchSpanLossMin_Object=MibTableColumn
bandCtpPmOchSpanLossMin=_BandCtpPmOchSpanLossMin_Object((1,3,6,1,4,1,21296,2,2,2,3,1,2,1,4),_BandCtpPmOchSpanLossMin_Type())
bandCtpPmOchSpanLossMin.setMaxAccess(_C)
if mibBuilder.loadTexts:bandCtpPmOchSpanLossMin.setStatus(_A)
_BandCtpPmOchSpanLossMax_Type=FloatHundredths
_BandCtpPmOchSpanLossMax_Object=MibTableColumn
bandCtpPmOchSpanLossMax=_BandCtpPmOchSpanLossMax_Object((1,3,6,1,4,1,21296,2,2,2,3,1,2,1,5),_BandCtpPmOchSpanLossMax_Type())
bandCtpPmOchSpanLossMax.setMaxAccess(_C)
if mibBuilder.loadTexts:bandCtpPmOchSpanLossMax.setStatus(_A)
_BandCtpPmOchSpanLossAve_Type=FloatHundredths
_BandCtpPmOchSpanLossAve_Object=MibTableColumn
bandCtpPmOchSpanLossAve=_BandCtpPmOchSpanLossAve_Object((1,3,6,1,4,1,21296,2,2,2,3,1,2,1,6),_BandCtpPmOchSpanLossAve_Type())
bandCtpPmOchSpanLossAve.setMaxAccess(_C)
if mibBuilder.loadTexts:bandCtpPmOchSpanLossAve.setStatus(_A)
_BandCtpPmNetSpanLossMin_Type=FloatHundredths
_BandCtpPmNetSpanLossMin_Object=MibTableColumn
bandCtpPmNetSpanLossMin=_BandCtpPmNetSpanLossMin_Object((1,3,6,1,4,1,21296,2,2,2,3,1,2,1,7),_BandCtpPmNetSpanLossMin_Type())
bandCtpPmNetSpanLossMin.setMaxAccess(_C)
if mibBuilder.loadTexts:bandCtpPmNetSpanLossMin.setStatus(_A)
_BandCtpPmNetSpanLossMax_Type=FloatHundredths
_BandCtpPmNetSpanLossMax_Object=MibTableColumn
bandCtpPmNetSpanLossMax=_BandCtpPmNetSpanLossMax_Object((1,3,6,1,4,1,21296,2,2,2,3,1,2,1,8),_BandCtpPmNetSpanLossMax_Type())
bandCtpPmNetSpanLossMax.setMaxAccess(_C)
if mibBuilder.loadTexts:bandCtpPmNetSpanLossMax.setStatus(_A)
_BandCtpPmNetSpanLossAve_Type=FloatHundredths
_BandCtpPmNetSpanLossAve_Object=MibTableColumn
bandCtpPmNetSpanLossAve=_BandCtpPmNetSpanLossAve_Object((1,3,6,1,4,1,21296,2,2,2,3,1,2,1,9),_BandCtpPmNetSpanLossAve_Type())
bandCtpPmNetSpanLossAve.setMaxAccess(_C)
if mibBuilder.loadTexts:bandCtpPmNetSpanLossAve.setStatus(_A)
_BandCtpPmBandOprMin_Type=FloatHundredths
_BandCtpPmBandOprMin_Object=MibTableColumn
bandCtpPmBandOprMin=_BandCtpPmBandOprMin_Object((1,3,6,1,4,1,21296,2,2,2,3,1,2,1,10),_BandCtpPmBandOprMin_Type())
bandCtpPmBandOprMin.setMaxAccess(_C)
if mibBuilder.loadTexts:bandCtpPmBandOprMin.setStatus(_A)
_BandCtpPmBandOprMax_Type=FloatHundredths
_BandCtpPmBandOprMax_Object=MibTableColumn
bandCtpPmBandOprMax=_BandCtpPmBandOprMax_Object((1,3,6,1,4,1,21296,2,2,2,3,1,2,1,11),_BandCtpPmBandOprMax_Type())
bandCtpPmBandOprMax.setMaxAccess(_C)
if mibBuilder.loadTexts:bandCtpPmBandOprMax.setStatus(_A)
_BandCtpPmBandOprAve_Type=FloatHundredths
_BandCtpPmBandOprAve_Object=MibTableColumn
bandCtpPmBandOprAve=_BandCtpPmBandOprAve_Object((1,3,6,1,4,1,21296,2,2,2,3,1,2,1,12),_BandCtpPmBandOprAve_Type())
bandCtpPmBandOprAve.setMaxAccess(_C)
if mibBuilder.loadTexts:bandCtpPmBandOprAve.setStatus(_A)
_BandCtpPmBandOptMin_Type=FloatHundredths
_BandCtpPmBandOptMin_Object=MibTableColumn
bandCtpPmBandOptMin=_BandCtpPmBandOptMin_Object((1,3,6,1,4,1,21296,2,2,2,3,1,2,1,13),_BandCtpPmBandOptMin_Type())
bandCtpPmBandOptMin.setMaxAccess(_C)
if mibBuilder.loadTexts:bandCtpPmBandOptMin.setStatus(_A)
_BandCtpPmBandOptMax_Type=FloatHundredths
_BandCtpPmBandOptMax_Object=MibTableColumn
bandCtpPmBandOptMax=_BandCtpPmBandOptMax_Object((1,3,6,1,4,1,21296,2,2,2,3,1,2,1,14),_BandCtpPmBandOptMax_Type())
bandCtpPmBandOptMax.setMaxAccess(_C)
if mibBuilder.loadTexts:bandCtpPmBandOptMax.setStatus(_A)
_BandCtpPmBandOptAve_Type=FloatHundredths
_BandCtpPmBandOptAve_Object=MibTableColumn
bandCtpPmBandOptAve=_BandCtpPmBandOptAve_Object((1,3,6,1,4,1,21296,2,2,2,3,1,2,1,15),_BandCtpPmBandOptAve_Type())
bandCtpPmBandOptAve.setMaxAccess(_C)
if mibBuilder.loadTexts:bandCtpPmBandOptAve.setStatus(_A)
_BandCtpPmBmmPostEdfaMin_Type=FloatHundredths
_BandCtpPmBmmPostEdfaMin_Object=MibTableColumn
bandCtpPmBmmPostEdfaMin=_BandCtpPmBmmPostEdfaMin_Object((1,3,6,1,4,1,21296,2,2,2,3,1,2,1,16),_BandCtpPmBmmPostEdfaMin_Type())
bandCtpPmBmmPostEdfaMin.setMaxAccess(_C)
if mibBuilder.loadTexts:bandCtpPmBmmPostEdfaMin.setStatus(_A)
_BandCtpPmBmmPostEdfaMax_Type=FloatHundredths
_BandCtpPmBmmPostEdfaMax_Object=MibTableColumn
bandCtpPmBmmPostEdfaMax=_BandCtpPmBmmPostEdfaMax_Object((1,3,6,1,4,1,21296,2,2,2,3,1,2,1,17),_BandCtpPmBmmPostEdfaMax_Type())
bandCtpPmBmmPostEdfaMax.setMaxAccess(_C)
if mibBuilder.loadTexts:bandCtpPmBmmPostEdfaMax.setStatus(_A)
_BandCtpPmBmmPostEdfaAve_Type=FloatHundredths
_BandCtpPmBmmPostEdfaAve_Object=MibTableColumn
bandCtpPmBmmPostEdfaAve=_BandCtpPmBmmPostEdfaAve_Object((1,3,6,1,4,1,21296,2,2,2,3,1,2,1,18),_BandCtpPmBmmPostEdfaAve_Type())
bandCtpPmBmmPostEdfaAve.setMaxAccess(_C)
if mibBuilder.loadTexts:bandCtpPmBmmPostEdfaAve.setStatus(_A)
_BandCtpPmTxEdfaOprMin_Type=FloatHundredths
_BandCtpPmTxEdfaOprMin_Object=MibTableColumn
bandCtpPmTxEdfaOprMin=_BandCtpPmTxEdfaOprMin_Object((1,3,6,1,4,1,21296,2,2,2,3,1,2,1,19),_BandCtpPmTxEdfaOprMin_Type())
bandCtpPmTxEdfaOprMin.setMaxAccess(_C)
if mibBuilder.loadTexts:bandCtpPmTxEdfaOprMin.setStatus(_A)
_BandCtpPmTxEdfaOprMax_Type=FloatHundredths
_BandCtpPmTxEdfaOprMax_Object=MibTableColumn
bandCtpPmTxEdfaOprMax=_BandCtpPmTxEdfaOprMax_Object((1,3,6,1,4,1,21296,2,2,2,3,1,2,1,20),_BandCtpPmTxEdfaOprMax_Type())
bandCtpPmTxEdfaOprMax.setMaxAccess(_C)
if mibBuilder.loadTexts:bandCtpPmTxEdfaOprMax.setStatus(_A)
_BandCtpPmTxEdfaOprAve_Type=FloatHundredths
_BandCtpPmTxEdfaOprAve_Object=MibTableColumn
bandCtpPmTxEdfaOprAve=_BandCtpPmTxEdfaOprAve_Object((1,3,6,1,4,1,21296,2,2,2,3,1,2,1,21),_BandCtpPmTxEdfaOprAve_Type())
bandCtpPmTxEdfaOprAve.setMaxAccess(_C)
if mibBuilder.loadTexts:bandCtpPmTxEdfaOprAve.setStatus(_A)
_BandCtpPmRxEdfaOptMin_Type=FloatHundredths
_BandCtpPmRxEdfaOptMin_Object=MibTableColumn
bandCtpPmRxEdfaOptMin=_BandCtpPmRxEdfaOptMin_Object((1,3,6,1,4,1,21296,2,2,2,3,1,2,1,22),_BandCtpPmRxEdfaOptMin_Type())
bandCtpPmRxEdfaOptMin.setMaxAccess(_C)
if mibBuilder.loadTexts:bandCtpPmRxEdfaOptMin.setStatus(_A)
_BandCtpPmRxEdfaOptMax_Type=FloatHundredths
_BandCtpPmRxEdfaOptMax_Object=MibTableColumn
bandCtpPmRxEdfaOptMax=_BandCtpPmRxEdfaOptMax_Object((1,3,6,1,4,1,21296,2,2,2,3,1,2,1,23),_BandCtpPmRxEdfaOptMax_Type())
bandCtpPmRxEdfaOptMax.setMaxAccess(_C)
if mibBuilder.loadTexts:bandCtpPmRxEdfaOptMax.setStatus(_A)
_BandCtpPmRxEdfaOptAve_Type=FloatHundredths
_BandCtpPmRxEdfaOptAve_Object=MibTableColumn
bandCtpPmRxEdfaOptAve=_BandCtpPmRxEdfaOptAve_Object((1,3,6,1,4,1,21296,2,2,2,3,1,2,1,24),_BandCtpPmRxEdfaOptAve_Type())
bandCtpPmRxEdfaOptAve.setMaxAccess(_C)
if mibBuilder.loadTexts:bandCtpPmRxEdfaOptAve.setStatus(_A)
_BandCtpPmOptOsaTapRatioMin_Type=FloatHundredths
_BandCtpPmOptOsaTapRatioMin_Object=MibTableColumn
bandCtpPmOptOsaTapRatioMin=_BandCtpPmOptOsaTapRatioMin_Object((1,3,6,1,4,1,21296,2,2,2,3,1,2,1,25),_BandCtpPmOptOsaTapRatioMin_Type())
bandCtpPmOptOsaTapRatioMin.setMaxAccess(_C)
if mibBuilder.loadTexts:bandCtpPmOptOsaTapRatioMin.setStatus(_A)
_BandCtpPmOptOsaTapRatioMax_Type=FloatHundredths
_BandCtpPmOptOsaTapRatioMax_Object=MibTableColumn
bandCtpPmOptOsaTapRatioMax=_BandCtpPmOptOsaTapRatioMax_Object((1,3,6,1,4,1,21296,2,2,2,3,1,2,1,26),_BandCtpPmOptOsaTapRatioMax_Type())
bandCtpPmOptOsaTapRatioMax.setMaxAccess(_C)
if mibBuilder.loadTexts:bandCtpPmOptOsaTapRatioMax.setStatus(_A)
_BandCtpPmOptOsaTapRatioAve_Type=FloatHundredths
_BandCtpPmOptOsaTapRatioAve_Object=MibTableColumn
bandCtpPmOptOsaTapRatioAve=_BandCtpPmOptOsaTapRatioAve_Object((1,3,6,1,4,1,21296,2,2,2,3,1,2,1,27),_BandCtpPmOptOsaTapRatioAve_Type())
bandCtpPmOptOsaTapRatioAve.setMaxAccess(_C)
if mibBuilder.loadTexts:bandCtpPmOptOsaTapRatioAve.setStatus(_A)
_BandCtpPmConformance_ObjectIdentity=ObjectIdentity
bandCtpPmConformance=_BandCtpPmConformance_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,3,1,3))
_BandCtpPmCompliances_ObjectIdentity=ObjectIdentity
bandCtpPmCompliances=_BandCtpPmCompliances_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,3,1,3,1))
_BandCtpPmGroups_ObjectIdentity=ObjectIdentity
bandCtpPmGroups=_BandCtpPmGroups_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,3,1,3,2))
bandCtpPmGroup=ObjectGroup((1,3,6,1,4,1,21296,2,2,2,3,1,3,2,1))
bandCtpPmGroup.setObjects(*((_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h)))
if mibBuilder.loadTexts:bandCtpPmGroup.setStatus(_A)
bandCtpPmRealGroup=ObjectGroup((1,3,6,1,4,1,21296,2,2,2,3,1,3,2,2))
bandCtpPmRealGroup.setObjects(*((_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_x),(_B,_y),(_B,_z),(_B,_A0),(_B,_A1)))
if mibBuilder.loadTexts:bandCtpPmRealGroup.setStatus(_A)
bandCtpPmCompliance=ModuleCompliance((1,3,6,1,4,1,21296,2,2,2,3,1,3,1,1))
bandCtpPmCompliance.setObjects((_B,_A2))
if mibBuilder.loadTexts:bandCtpPmCompliance.setStatus(_A)
bandCtpPmRealCompliance=ModuleCompliance((1,3,6,1,4,1,21296,2,2,2,3,1,3,1,2))
bandCtpPmRealCompliance.setObjects((_B,_A3))
if mibBuilder.loadTexts:bandCtpPmRealCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'bandCtpPmMIB':bandCtpPmMIB,'bandCtpPmRealTable':bandCtpPmRealTable,'bandCtpPmRealEntry':bandCtpPmRealEntry,_i:bandCtpPmRealOchSpanLoss,_j:bandCtpPmRealNetSpanLoss,_k:bandCtpPmRealBandOpr,_l:bandCtpPmRealBandOchOpr,_m:bandCtpPmRealBandOprNum,_n:bandCtpPmRealOamBandTxEdfaLbc1,_o:bandCtpPmRealOamBandTxEdfaLbc2,_p:bandCtpPmRealBmmBandEdfaLbcTx,_q:bandCtpPmRealBandOptTx,_r:bandCtpPmRealBandOchOpt,_s:bandCtpPmRealBandOptNum,_t:bandCtpPmRealBmmEdfaLbc1,_u:bandCtpPmRealBmmEdfaLbc2,_v:bandCtpPmRealBmmPostEdfa,_w:bandCtpPmRealDampUpdateTS,_x:bandCtpPmRealOprQ,_y:bandCtpPmRealPostOsaTapRatio,_z:bandCtpPmRealTxEdfaOpr,_A0:bandCtpPmRealRxEdfaOpt,_A1:bandCtpPmRealOptOsaTapRatio,'bandCtpPmTable':bandCtpPmTable,'bandCtpPmEntry':bandCtpPmEntry,_H:bandCtpPmTimestamp,_G:bandCtpPmSampleDuration,_J:bandCtpPmValidity,_K:bandCtpPmOchSpanLossMin,_L:bandCtpPmOchSpanLossMax,_M:bandCtpPmOchSpanLossAve,_N:bandCtpPmNetSpanLossMin,_O:bandCtpPmNetSpanLossMax,_P:bandCtpPmNetSpanLossAve,_Q:bandCtpPmBandOprMin,_R:bandCtpPmBandOprMax,_S:bandCtpPmBandOprAve,_T:bandCtpPmBandOptMin,_U:bandCtpPmBandOptMax,_V:bandCtpPmBandOptAve,_W:bandCtpPmBmmPostEdfaMin,_X:bandCtpPmBmmPostEdfaMax,_Y:bandCtpPmBmmPostEdfaAve,_Z:bandCtpPmTxEdfaOprMin,_a:bandCtpPmTxEdfaOprMax,_b:bandCtpPmTxEdfaOprAve,_c:bandCtpPmRxEdfaOptMin,_d:bandCtpPmRxEdfaOptMax,_e:bandCtpPmRxEdfaOptAve,_f:bandCtpPmOptOsaTapRatioMin,_g:bandCtpPmOptOsaTapRatioMax,_h:bandCtpPmOptOsaTapRatioAve,'bandCtpPmConformance':bandCtpPmConformance,'bandCtpPmCompliances':bandCtpPmCompliances,'bandCtpPmCompliance':bandCtpPmCompliance,'bandCtpPmRealCompliance':bandCtpPmRealCompliance,'bandCtpPmGroups':bandCtpPmGroups,_A2:bandCtpPmGroup,_A3:bandCtpPmRealGroup})