_AF='otsPtpPmRealGroup'
_AE='otsPtpPmGroup'
_AD='otsPtpPmRealOprQ'
_AC='otsPtpPmRealRxPostEdfaOsaTapRatio'
_AB='otsPtpPmRealOtsAlsLbc'
_AA='otsPtpPmRealOtsAlsOpt'
_A9='otsPtpPmRealOtsAlsOpr'
_A8='otsPtpPmRealOtsLpwr4'
_A7='otsPtpPmRealOtsLpwr3'
_A6='otsPtpPmRealOtsLpwr2'
_A5='otsPtpPmRealOtsLpwr1'
_A4='otsPtpPmRealOtsLbc4'
_A3='otsPtpPmRealOtsLbc3'
_A2='otsPtpPmRealOtsLbc2'
_A1='otsPtpPmRealOtsLbc1'
_A0='otsPtpPmRealOtsOprOsaTapRatio'
_z='otsPtpPmRealOtsOpr'
_y='otsPtpPmRealOtsOptOsaTapRatio'
_x='otsPtpPmRealOtsOpt'
_w='otsPtpOtsAlsLbcAve'
_v='otsPtpOtsAlsLbcMax'
_u='otsPtpOtsAlsLbcMin'
_t='otsPtpOtsAlsOptAve'
_s='otsPtpOtsAlsOptMax'
_r='otsPtpOtsAlsOptMin'
_q='otsPtpOtsAlsOprAve'
_p='otsPtpOtsAlsOprMax'
_o='otsPtpOtsAlsOprMin'
_n='otsPtpPmOtsLpwr4Ave'
_m='otsPtpPmOtsLpwr4Max'
_l='otsPtpPmOtsLpwr4Min'
_k='otsPtpPmOtsLpwr3Ave'
_j='otsPtpPmOtsLpwr3Max'
_i='otsPtpPmOtsLpwr3Min'
_h='otsPtpPmOtsLpwr2Ave'
_g='otsPtpPmOtsLpwr2Max'
_f='otsPtpPmOtsLpwr2Min'
_e='otsPtpPmOtsLpwr1Ave'
_d='otsPtpPmOtsLpwr1Max'
_c='otsPtpPmOtsLpwr1Min'
_b='otsPtpPmOtsLbc4Ave'
_a='otsPtpPmOtsLbc4Max'
_Z='otsPtpPmOtsLbc4Min'
_Y='otsPtpPmOtsLbc3Ave'
_X='otsPtpPmOtsLbc3Max'
_W='otsPtpPmOtsLbc3Min'
_V='otsPtpPmOtsLbc2Ave'
_U='otsPtpPmOtsLbc2Max'
_T='otsPtpPmOtsLbc2Min'
_S='otsPtpPmOtsLbc1Ave'
_R='otsPtpPmOtsLbc1Max'
_Q='otsPtpPmOtsLbc1Min'
_P='otsPtpPmOtsOprAve'
_O='otsPtpPmOtsOprMax'
_N='otsPtpPmOtsOprMin'
_M='otsPtpPmOtsOptAve'
_L='otsPtpPmOtsOptMax'
_K='otsPtpPmOtsOptMin'
_J='otsPtpPmValidity'
_I='not-accessible'
_H='otsPtpPmTimestamp'
_G='otsPtpPmSampleDuration'
_F='Integer32'
_E='ifIndex'
_D='IF-MIB'
_C='read-only'
_B='INFINERA-PM-OTSPTP-MIB'
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
otsPtpPmMIB=ModuleIdentity((1,3,6,1,4,1,21296,2,2,2,3,12))
if mibBuilder.loadTexts:otsPtpPmMIB.setRevisions(('2008-10-20 00:00',))
_OtsPtpPmRealTable_Object=MibTable
otsPtpPmRealTable=_OtsPtpPmRealTable_Object((1,3,6,1,4,1,21296,2,2,2,3,12,1))
if mibBuilder.loadTexts:otsPtpPmRealTable.setStatus(_A)
_OtsPtpPmRealEntry_Object=MibTableRow
otsPtpPmRealEntry=_OtsPtpPmRealEntry_Object((1,3,6,1,4,1,21296,2,2,2,3,12,1,1))
otsPtpPmRealEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:otsPtpPmRealEntry.setStatus(_A)
_OtsPtpPmRealOtsOpt_Type=FloatHundredths
_OtsPtpPmRealOtsOpt_Object=MibTableColumn
otsPtpPmRealOtsOpt=_OtsPtpPmRealOtsOpt_Object((1,3,6,1,4,1,21296,2,2,2,3,12,1,1,1),_OtsPtpPmRealOtsOpt_Type())
otsPtpPmRealOtsOpt.setMaxAccess(_C)
if mibBuilder.loadTexts:otsPtpPmRealOtsOpt.setStatus(_A)
_OtsPtpPmRealOtsOptOsaTapRatio_Type=FloatHundredths
_OtsPtpPmRealOtsOptOsaTapRatio_Object=MibTableColumn
otsPtpPmRealOtsOptOsaTapRatio=_OtsPtpPmRealOtsOptOsaTapRatio_Object((1,3,6,1,4,1,21296,2,2,2,3,12,1,1,2),_OtsPtpPmRealOtsOptOsaTapRatio_Type())
otsPtpPmRealOtsOptOsaTapRatio.setMaxAccess(_C)
if mibBuilder.loadTexts:otsPtpPmRealOtsOptOsaTapRatio.setStatus(_A)
_OtsPtpPmRealOtsOpr_Type=FloatHundredths
_OtsPtpPmRealOtsOpr_Object=MibTableColumn
otsPtpPmRealOtsOpr=_OtsPtpPmRealOtsOpr_Object((1,3,6,1,4,1,21296,2,2,2,3,12,1,1,3),_OtsPtpPmRealOtsOpr_Type())
otsPtpPmRealOtsOpr.setMaxAccess(_C)
if mibBuilder.loadTexts:otsPtpPmRealOtsOpr.setStatus(_A)
_OtsPtpPmRealOtsOprOsaTapRatio_Type=FloatHundredths
_OtsPtpPmRealOtsOprOsaTapRatio_Object=MibTableColumn
otsPtpPmRealOtsOprOsaTapRatio=_OtsPtpPmRealOtsOprOsaTapRatio_Object((1,3,6,1,4,1,21296,2,2,2,3,12,1,1,4),_OtsPtpPmRealOtsOprOsaTapRatio_Type())
otsPtpPmRealOtsOprOsaTapRatio.setMaxAccess(_C)
if mibBuilder.loadTexts:otsPtpPmRealOtsOprOsaTapRatio.setStatus(_A)
_OtsPtpPmRealOtsLbc1_Type=FloatHundredths
_OtsPtpPmRealOtsLbc1_Object=MibTableColumn
otsPtpPmRealOtsLbc1=_OtsPtpPmRealOtsLbc1_Object((1,3,6,1,4,1,21296,2,2,2,3,12,1,1,5),_OtsPtpPmRealOtsLbc1_Type())
otsPtpPmRealOtsLbc1.setMaxAccess(_C)
if mibBuilder.loadTexts:otsPtpPmRealOtsLbc1.setStatus(_A)
_OtsPtpPmRealOtsLbc2_Type=FloatHundredths
_OtsPtpPmRealOtsLbc2_Object=MibTableColumn
otsPtpPmRealOtsLbc2=_OtsPtpPmRealOtsLbc2_Object((1,3,6,1,4,1,21296,2,2,2,3,12,1,1,6),_OtsPtpPmRealOtsLbc2_Type())
otsPtpPmRealOtsLbc2.setMaxAccess(_C)
if mibBuilder.loadTexts:otsPtpPmRealOtsLbc2.setStatus(_A)
_OtsPtpPmRealOtsLbc3_Type=FloatHundredths
_OtsPtpPmRealOtsLbc3_Object=MibTableColumn
otsPtpPmRealOtsLbc3=_OtsPtpPmRealOtsLbc3_Object((1,3,6,1,4,1,21296,2,2,2,3,12,1,1,7),_OtsPtpPmRealOtsLbc3_Type())
otsPtpPmRealOtsLbc3.setMaxAccess(_C)
if mibBuilder.loadTexts:otsPtpPmRealOtsLbc3.setStatus(_A)
_OtsPtpPmRealOtsLbc4_Type=FloatHundredths
_OtsPtpPmRealOtsLbc4_Object=MibTableColumn
otsPtpPmRealOtsLbc4=_OtsPtpPmRealOtsLbc4_Object((1,3,6,1,4,1,21296,2,2,2,3,12,1,1,8),_OtsPtpPmRealOtsLbc4_Type())
otsPtpPmRealOtsLbc4.setMaxAccess(_C)
if mibBuilder.loadTexts:otsPtpPmRealOtsLbc4.setStatus(_A)
_OtsPtpPmRealOtsLpwr1_Type=FloatHundredths
_OtsPtpPmRealOtsLpwr1_Object=MibTableColumn
otsPtpPmRealOtsLpwr1=_OtsPtpPmRealOtsLpwr1_Object((1,3,6,1,4,1,21296,2,2,2,3,12,1,1,9),_OtsPtpPmRealOtsLpwr1_Type())
otsPtpPmRealOtsLpwr1.setMaxAccess(_C)
if mibBuilder.loadTexts:otsPtpPmRealOtsLpwr1.setStatus(_A)
_OtsPtpPmRealOtsLpwr2_Type=FloatHundredths
_OtsPtpPmRealOtsLpwr2_Object=MibTableColumn
otsPtpPmRealOtsLpwr2=_OtsPtpPmRealOtsLpwr2_Object((1,3,6,1,4,1,21296,2,2,2,3,12,1,1,10),_OtsPtpPmRealOtsLpwr2_Type())
otsPtpPmRealOtsLpwr2.setMaxAccess(_C)
if mibBuilder.loadTexts:otsPtpPmRealOtsLpwr2.setStatus(_A)
_OtsPtpPmRealOtsLpwr3_Type=FloatHundredths
_OtsPtpPmRealOtsLpwr3_Object=MibTableColumn
otsPtpPmRealOtsLpwr3=_OtsPtpPmRealOtsLpwr3_Object((1,3,6,1,4,1,21296,2,2,2,3,12,1,1,11),_OtsPtpPmRealOtsLpwr3_Type())
otsPtpPmRealOtsLpwr3.setMaxAccess(_C)
if mibBuilder.loadTexts:otsPtpPmRealOtsLpwr3.setStatus(_A)
_OtsPtpPmRealOtsLpwr4_Type=FloatHundredths
_OtsPtpPmRealOtsLpwr4_Object=MibTableColumn
otsPtpPmRealOtsLpwr4=_OtsPtpPmRealOtsLpwr4_Object((1,3,6,1,4,1,21296,2,2,2,3,12,1,1,12),_OtsPtpPmRealOtsLpwr4_Type())
otsPtpPmRealOtsLpwr4.setMaxAccess(_C)
if mibBuilder.loadTexts:otsPtpPmRealOtsLpwr4.setStatus(_A)
_OtsPtpPmRealOtsAlsOpr_Type=FloatHundredths
_OtsPtpPmRealOtsAlsOpr_Object=MibTableColumn
otsPtpPmRealOtsAlsOpr=_OtsPtpPmRealOtsAlsOpr_Object((1,3,6,1,4,1,21296,2,2,2,3,12,1,1,13),_OtsPtpPmRealOtsAlsOpr_Type())
otsPtpPmRealOtsAlsOpr.setMaxAccess(_C)
if mibBuilder.loadTexts:otsPtpPmRealOtsAlsOpr.setStatus(_A)
_OtsPtpPmRealOtsAlsOpt_Type=FloatHundredths
_OtsPtpPmRealOtsAlsOpt_Object=MibTableColumn
otsPtpPmRealOtsAlsOpt=_OtsPtpPmRealOtsAlsOpt_Object((1,3,6,1,4,1,21296,2,2,2,3,12,1,1,14),_OtsPtpPmRealOtsAlsOpt_Type())
otsPtpPmRealOtsAlsOpt.setMaxAccess(_C)
if mibBuilder.loadTexts:otsPtpPmRealOtsAlsOpt.setStatus(_A)
_OtsPtpPmRealOtsAlsLbc_Type=FloatHundredths
_OtsPtpPmRealOtsAlsLbc_Object=MibTableColumn
otsPtpPmRealOtsAlsLbc=_OtsPtpPmRealOtsAlsLbc_Object((1,3,6,1,4,1,21296,2,2,2,3,12,1,1,15),_OtsPtpPmRealOtsAlsLbc_Type())
otsPtpPmRealOtsAlsLbc.setMaxAccess(_C)
if mibBuilder.loadTexts:otsPtpPmRealOtsAlsLbc.setStatus(_A)
_OtsPtpPmRealRxPostEdfaOsaTapRatio_Type=FloatHundredths
_OtsPtpPmRealRxPostEdfaOsaTapRatio_Object=MibTableColumn
otsPtpPmRealRxPostEdfaOsaTapRatio=_OtsPtpPmRealRxPostEdfaOsaTapRatio_Object((1,3,6,1,4,1,21296,2,2,2,3,12,1,1,16),_OtsPtpPmRealRxPostEdfaOsaTapRatio_Type())
otsPtpPmRealRxPostEdfaOsaTapRatio.setMaxAccess(_C)
if mibBuilder.loadTexts:otsPtpPmRealRxPostEdfaOsaTapRatio.setStatus(_A)
_OtsPtpPmRealOprQ_Type=DisplayString
_OtsPtpPmRealOprQ_Object=MibTableColumn
otsPtpPmRealOprQ=_OtsPtpPmRealOprQ_Object((1,3,6,1,4,1,21296,2,2,2,3,12,1,1,17),_OtsPtpPmRealOprQ_Type())
otsPtpPmRealOprQ.setMaxAccess(_C)
if mibBuilder.loadTexts:otsPtpPmRealOprQ.setStatus(_A)
_OtsPtpPmTable_Object=MibTable
otsPtpPmTable=_OtsPtpPmTable_Object((1,3,6,1,4,1,21296,2,2,2,3,12,2))
if mibBuilder.loadTexts:otsPtpPmTable.setStatus(_A)
_OtsPtpPmEntry_Object=MibTableRow
otsPtpPmEntry=_OtsPtpPmEntry_Object((1,3,6,1,4,1,21296,2,2,2,3,12,2,1))
otsPtpPmEntry.setIndexNames((0,_D,_E),(0,_B,_G),(0,_B,_H))
if mibBuilder.loadTexts:otsPtpPmEntry.setStatus(_A)
class _OtsPtpPmTimestamp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_OtsPtpPmTimestamp_Type.__name__=_F
_OtsPtpPmTimestamp_Object=MibTableColumn
otsPtpPmTimestamp=_OtsPtpPmTimestamp_Object((1,3,6,1,4,1,21296,2,2,2,3,12,2,1,1),_OtsPtpPmTimestamp_Type())
otsPtpPmTimestamp.setMaxAccess(_I)
if mibBuilder.loadTexts:otsPtpPmTimestamp.setStatus(_A)
class _OtsPtpPmSampleDuration_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('fifteenMinutes',1),('day',2)))
_OtsPtpPmSampleDuration_Type.__name__=_F
_OtsPtpPmSampleDuration_Object=MibTableColumn
otsPtpPmSampleDuration=_OtsPtpPmSampleDuration_Object((1,3,6,1,4,1,21296,2,2,2,3,12,2,1,2),_OtsPtpPmSampleDuration_Type())
otsPtpPmSampleDuration.setMaxAccess(_I)
if mibBuilder.loadTexts:otsPtpPmSampleDuration.setStatus(_A)
_OtsPtpPmValidity_Type=TruthValue
_OtsPtpPmValidity_Object=MibTableColumn
otsPtpPmValidity=_OtsPtpPmValidity_Object((1,3,6,1,4,1,21296,2,2,2,3,12,2,1,3),_OtsPtpPmValidity_Type())
otsPtpPmValidity.setMaxAccess(_C)
if mibBuilder.loadTexts:otsPtpPmValidity.setStatus(_A)
_OtsPtpPmOtsOptMin_Type=FloatHundredths
_OtsPtpPmOtsOptMin_Object=MibTableColumn
otsPtpPmOtsOptMin=_OtsPtpPmOtsOptMin_Object((1,3,6,1,4,1,21296,2,2,2,3,12,2,1,4),_OtsPtpPmOtsOptMin_Type())
otsPtpPmOtsOptMin.setMaxAccess(_C)
if mibBuilder.loadTexts:otsPtpPmOtsOptMin.setStatus(_A)
_OtsPtpPmOtsOptMax_Type=FloatHundredths
_OtsPtpPmOtsOptMax_Object=MibTableColumn
otsPtpPmOtsOptMax=_OtsPtpPmOtsOptMax_Object((1,3,6,1,4,1,21296,2,2,2,3,12,2,1,5),_OtsPtpPmOtsOptMax_Type())
otsPtpPmOtsOptMax.setMaxAccess(_C)
if mibBuilder.loadTexts:otsPtpPmOtsOptMax.setStatus(_A)
_OtsPtpPmOtsOptAve_Type=FloatHundredths
_OtsPtpPmOtsOptAve_Object=MibTableColumn
otsPtpPmOtsOptAve=_OtsPtpPmOtsOptAve_Object((1,3,6,1,4,1,21296,2,2,2,3,12,2,1,6),_OtsPtpPmOtsOptAve_Type())
otsPtpPmOtsOptAve.setMaxAccess(_C)
if mibBuilder.loadTexts:otsPtpPmOtsOptAve.setStatus(_A)
_OtsPtpPmOtsOprMin_Type=FloatHundredths
_OtsPtpPmOtsOprMin_Object=MibTableColumn
otsPtpPmOtsOprMin=_OtsPtpPmOtsOprMin_Object((1,3,6,1,4,1,21296,2,2,2,3,12,2,1,7),_OtsPtpPmOtsOprMin_Type())
otsPtpPmOtsOprMin.setMaxAccess(_C)
if mibBuilder.loadTexts:otsPtpPmOtsOprMin.setStatus(_A)
_OtsPtpPmOtsOprMax_Type=FloatHundredths
_OtsPtpPmOtsOprMax_Object=MibTableColumn
otsPtpPmOtsOprMax=_OtsPtpPmOtsOprMax_Object((1,3,6,1,4,1,21296,2,2,2,3,12,2,1,8),_OtsPtpPmOtsOprMax_Type())
otsPtpPmOtsOprMax.setMaxAccess(_C)
if mibBuilder.loadTexts:otsPtpPmOtsOprMax.setStatus(_A)
_OtsPtpPmOtsOprAve_Type=FloatHundredths
_OtsPtpPmOtsOprAve_Object=MibTableColumn
otsPtpPmOtsOprAve=_OtsPtpPmOtsOprAve_Object((1,3,6,1,4,1,21296,2,2,2,3,12,2,1,9),_OtsPtpPmOtsOprAve_Type())
otsPtpPmOtsOprAve.setMaxAccess(_C)
if mibBuilder.loadTexts:otsPtpPmOtsOprAve.setStatus(_A)
_OtsPtpPmOtsLbc1Min_Type=FloatHundredths
_OtsPtpPmOtsLbc1Min_Object=MibTableColumn
otsPtpPmOtsLbc1Min=_OtsPtpPmOtsLbc1Min_Object((1,3,6,1,4,1,21296,2,2,2,3,12,2,1,10),_OtsPtpPmOtsLbc1Min_Type())
otsPtpPmOtsLbc1Min.setMaxAccess(_C)
if mibBuilder.loadTexts:otsPtpPmOtsLbc1Min.setStatus(_A)
_OtsPtpPmOtsLbc1Max_Type=FloatHundredths
_OtsPtpPmOtsLbc1Max_Object=MibTableColumn
otsPtpPmOtsLbc1Max=_OtsPtpPmOtsLbc1Max_Object((1,3,6,1,4,1,21296,2,2,2,3,12,2,1,11),_OtsPtpPmOtsLbc1Max_Type())
otsPtpPmOtsLbc1Max.setMaxAccess(_C)
if mibBuilder.loadTexts:otsPtpPmOtsLbc1Max.setStatus(_A)
_OtsPtpPmOtsLbc1Ave_Type=FloatHundredths
_OtsPtpPmOtsLbc1Ave_Object=MibTableColumn
otsPtpPmOtsLbc1Ave=_OtsPtpPmOtsLbc1Ave_Object((1,3,6,1,4,1,21296,2,2,2,3,12,2,1,12),_OtsPtpPmOtsLbc1Ave_Type())
otsPtpPmOtsLbc1Ave.setMaxAccess(_C)
if mibBuilder.loadTexts:otsPtpPmOtsLbc1Ave.setStatus(_A)
_OtsPtpPmOtsLbc2Min_Type=FloatHundredths
_OtsPtpPmOtsLbc2Min_Object=MibTableColumn
otsPtpPmOtsLbc2Min=_OtsPtpPmOtsLbc2Min_Object((1,3,6,1,4,1,21296,2,2,2,3,12,2,1,13),_OtsPtpPmOtsLbc2Min_Type())
otsPtpPmOtsLbc2Min.setMaxAccess(_C)
if mibBuilder.loadTexts:otsPtpPmOtsLbc2Min.setStatus(_A)
_OtsPtpPmOtsLbc2Max_Type=FloatHundredths
_OtsPtpPmOtsLbc2Max_Object=MibTableColumn
otsPtpPmOtsLbc2Max=_OtsPtpPmOtsLbc2Max_Object((1,3,6,1,4,1,21296,2,2,2,3,12,2,1,14),_OtsPtpPmOtsLbc2Max_Type())
otsPtpPmOtsLbc2Max.setMaxAccess(_C)
if mibBuilder.loadTexts:otsPtpPmOtsLbc2Max.setStatus(_A)
_OtsPtpPmOtsLbc2Ave_Type=FloatHundredths
_OtsPtpPmOtsLbc2Ave_Object=MibTableColumn
otsPtpPmOtsLbc2Ave=_OtsPtpPmOtsLbc2Ave_Object((1,3,6,1,4,1,21296,2,2,2,3,12,2,1,15),_OtsPtpPmOtsLbc2Ave_Type())
otsPtpPmOtsLbc2Ave.setMaxAccess(_C)
if mibBuilder.loadTexts:otsPtpPmOtsLbc2Ave.setStatus(_A)
_OtsPtpPmOtsLbc3Min_Type=FloatHundredths
_OtsPtpPmOtsLbc3Min_Object=MibTableColumn
otsPtpPmOtsLbc3Min=_OtsPtpPmOtsLbc3Min_Object((1,3,6,1,4,1,21296,2,2,2,3,12,2,1,16),_OtsPtpPmOtsLbc3Min_Type())
otsPtpPmOtsLbc3Min.setMaxAccess(_C)
if mibBuilder.loadTexts:otsPtpPmOtsLbc3Min.setStatus(_A)
_OtsPtpPmOtsLbc3Max_Type=FloatHundredths
_OtsPtpPmOtsLbc3Max_Object=MibTableColumn
otsPtpPmOtsLbc3Max=_OtsPtpPmOtsLbc3Max_Object((1,3,6,1,4,1,21296,2,2,2,3,12,2,1,17),_OtsPtpPmOtsLbc3Max_Type())
otsPtpPmOtsLbc3Max.setMaxAccess(_C)
if mibBuilder.loadTexts:otsPtpPmOtsLbc3Max.setStatus(_A)
_OtsPtpPmOtsLbc3Ave_Type=FloatHundredths
_OtsPtpPmOtsLbc3Ave_Object=MibTableColumn
otsPtpPmOtsLbc3Ave=_OtsPtpPmOtsLbc3Ave_Object((1,3,6,1,4,1,21296,2,2,2,3,12,2,1,18),_OtsPtpPmOtsLbc3Ave_Type())
otsPtpPmOtsLbc3Ave.setMaxAccess(_C)
if mibBuilder.loadTexts:otsPtpPmOtsLbc3Ave.setStatus(_A)
_OtsPtpPmOtsLbc4Min_Type=FloatHundredths
_OtsPtpPmOtsLbc4Min_Object=MibTableColumn
otsPtpPmOtsLbc4Min=_OtsPtpPmOtsLbc4Min_Object((1,3,6,1,4,1,21296,2,2,2,3,12,2,1,19),_OtsPtpPmOtsLbc4Min_Type())
otsPtpPmOtsLbc4Min.setMaxAccess(_C)
if mibBuilder.loadTexts:otsPtpPmOtsLbc4Min.setStatus(_A)
_OtsPtpPmOtsLbc4Max_Type=FloatHundredths
_OtsPtpPmOtsLbc4Max_Object=MibTableColumn
otsPtpPmOtsLbc4Max=_OtsPtpPmOtsLbc4Max_Object((1,3,6,1,4,1,21296,2,2,2,3,12,2,1,20),_OtsPtpPmOtsLbc4Max_Type())
otsPtpPmOtsLbc4Max.setMaxAccess(_C)
if mibBuilder.loadTexts:otsPtpPmOtsLbc4Max.setStatus(_A)
_OtsPtpPmOtsLbc4Ave_Type=FloatHundredths
_OtsPtpPmOtsLbc4Ave_Object=MibTableColumn
otsPtpPmOtsLbc4Ave=_OtsPtpPmOtsLbc4Ave_Object((1,3,6,1,4,1,21296,2,2,2,3,12,2,1,21),_OtsPtpPmOtsLbc4Ave_Type())
otsPtpPmOtsLbc4Ave.setMaxAccess(_C)
if mibBuilder.loadTexts:otsPtpPmOtsLbc4Ave.setStatus(_A)
_OtsPtpPmOtsLpwr1Min_Type=FloatHundredths
_OtsPtpPmOtsLpwr1Min_Object=MibTableColumn
otsPtpPmOtsLpwr1Min=_OtsPtpPmOtsLpwr1Min_Object((1,3,6,1,4,1,21296,2,2,2,3,12,2,1,22),_OtsPtpPmOtsLpwr1Min_Type())
otsPtpPmOtsLpwr1Min.setMaxAccess(_C)
if mibBuilder.loadTexts:otsPtpPmOtsLpwr1Min.setStatus(_A)
_OtsPtpPmOtsLpwr1Max_Type=FloatHundredths
_OtsPtpPmOtsLpwr1Max_Object=MibTableColumn
otsPtpPmOtsLpwr1Max=_OtsPtpPmOtsLpwr1Max_Object((1,3,6,1,4,1,21296,2,2,2,3,12,2,1,23),_OtsPtpPmOtsLpwr1Max_Type())
otsPtpPmOtsLpwr1Max.setMaxAccess(_C)
if mibBuilder.loadTexts:otsPtpPmOtsLpwr1Max.setStatus(_A)
_OtsPtpPmOtsLpwr1Ave_Type=FloatHundredths
_OtsPtpPmOtsLpwr1Ave_Object=MibTableColumn
otsPtpPmOtsLpwr1Ave=_OtsPtpPmOtsLpwr1Ave_Object((1,3,6,1,4,1,21296,2,2,2,3,12,2,1,24),_OtsPtpPmOtsLpwr1Ave_Type())
otsPtpPmOtsLpwr1Ave.setMaxAccess(_C)
if mibBuilder.loadTexts:otsPtpPmOtsLpwr1Ave.setStatus(_A)
_OtsPtpPmOtsLpwr2Min_Type=FloatHundredths
_OtsPtpPmOtsLpwr2Min_Object=MibTableColumn
otsPtpPmOtsLpwr2Min=_OtsPtpPmOtsLpwr2Min_Object((1,3,6,1,4,1,21296,2,2,2,3,12,2,1,25),_OtsPtpPmOtsLpwr2Min_Type())
otsPtpPmOtsLpwr2Min.setMaxAccess(_C)
if mibBuilder.loadTexts:otsPtpPmOtsLpwr2Min.setStatus(_A)
_OtsPtpPmOtsLpwr2Max_Type=FloatHundredths
_OtsPtpPmOtsLpwr2Max_Object=MibTableColumn
otsPtpPmOtsLpwr2Max=_OtsPtpPmOtsLpwr2Max_Object((1,3,6,1,4,1,21296,2,2,2,3,12,2,1,26),_OtsPtpPmOtsLpwr2Max_Type())
otsPtpPmOtsLpwr2Max.setMaxAccess(_C)
if mibBuilder.loadTexts:otsPtpPmOtsLpwr2Max.setStatus(_A)
_OtsPtpPmOtsLpwr2Ave_Type=FloatHundredths
_OtsPtpPmOtsLpwr2Ave_Object=MibTableColumn
otsPtpPmOtsLpwr2Ave=_OtsPtpPmOtsLpwr2Ave_Object((1,3,6,1,4,1,21296,2,2,2,3,12,2,1,27),_OtsPtpPmOtsLpwr2Ave_Type())
otsPtpPmOtsLpwr2Ave.setMaxAccess(_C)
if mibBuilder.loadTexts:otsPtpPmOtsLpwr2Ave.setStatus(_A)
_OtsPtpPmOtsLpwr3Min_Type=FloatHundredths
_OtsPtpPmOtsLpwr3Min_Object=MibTableColumn
otsPtpPmOtsLpwr3Min=_OtsPtpPmOtsLpwr3Min_Object((1,3,6,1,4,1,21296,2,2,2,3,12,2,1,28),_OtsPtpPmOtsLpwr3Min_Type())
otsPtpPmOtsLpwr3Min.setMaxAccess(_C)
if mibBuilder.loadTexts:otsPtpPmOtsLpwr3Min.setStatus(_A)
_OtsPtpPmOtsLpwr3Max_Type=FloatHundredths
_OtsPtpPmOtsLpwr3Max_Object=MibTableColumn
otsPtpPmOtsLpwr3Max=_OtsPtpPmOtsLpwr3Max_Object((1,3,6,1,4,1,21296,2,2,2,3,12,2,1,29),_OtsPtpPmOtsLpwr3Max_Type())
otsPtpPmOtsLpwr3Max.setMaxAccess(_C)
if mibBuilder.loadTexts:otsPtpPmOtsLpwr3Max.setStatus(_A)
_OtsPtpPmOtsLpwr3Ave_Type=FloatHundredths
_OtsPtpPmOtsLpwr3Ave_Object=MibTableColumn
otsPtpPmOtsLpwr3Ave=_OtsPtpPmOtsLpwr3Ave_Object((1,3,6,1,4,1,21296,2,2,2,3,12,2,1,30),_OtsPtpPmOtsLpwr3Ave_Type())
otsPtpPmOtsLpwr3Ave.setMaxAccess(_C)
if mibBuilder.loadTexts:otsPtpPmOtsLpwr3Ave.setStatus(_A)
_OtsPtpPmOtsLpwr4Min_Type=FloatHundredths
_OtsPtpPmOtsLpwr4Min_Object=MibTableColumn
otsPtpPmOtsLpwr4Min=_OtsPtpPmOtsLpwr4Min_Object((1,3,6,1,4,1,21296,2,2,2,3,12,2,1,31),_OtsPtpPmOtsLpwr4Min_Type())
otsPtpPmOtsLpwr4Min.setMaxAccess(_C)
if mibBuilder.loadTexts:otsPtpPmOtsLpwr4Min.setStatus(_A)
_OtsPtpPmOtsLpwr4Max_Type=FloatHundredths
_OtsPtpPmOtsLpwr4Max_Object=MibTableColumn
otsPtpPmOtsLpwr4Max=_OtsPtpPmOtsLpwr4Max_Object((1,3,6,1,4,1,21296,2,2,2,3,12,2,1,32),_OtsPtpPmOtsLpwr4Max_Type())
otsPtpPmOtsLpwr4Max.setMaxAccess(_C)
if mibBuilder.loadTexts:otsPtpPmOtsLpwr4Max.setStatus(_A)
_OtsPtpPmOtsLpwr4Ave_Type=FloatHundredths
_OtsPtpPmOtsLpwr4Ave_Object=MibTableColumn
otsPtpPmOtsLpwr4Ave=_OtsPtpPmOtsLpwr4Ave_Object((1,3,6,1,4,1,21296,2,2,2,3,12,2,1,33),_OtsPtpPmOtsLpwr4Ave_Type())
otsPtpPmOtsLpwr4Ave.setMaxAccess(_C)
if mibBuilder.loadTexts:otsPtpPmOtsLpwr4Ave.setStatus(_A)
_OtsPtpOtsAlsOprMin_Type=FloatHundredths
_OtsPtpOtsAlsOprMin_Object=MibTableColumn
otsPtpOtsAlsOprMin=_OtsPtpOtsAlsOprMin_Object((1,3,6,1,4,1,21296,2,2,2,3,12,2,1,34),_OtsPtpOtsAlsOprMin_Type())
otsPtpOtsAlsOprMin.setMaxAccess(_C)
if mibBuilder.loadTexts:otsPtpOtsAlsOprMin.setStatus(_A)
_OtsPtpOtsAlsOprMax_Type=FloatHundredths
_OtsPtpOtsAlsOprMax_Object=MibTableColumn
otsPtpOtsAlsOprMax=_OtsPtpOtsAlsOprMax_Object((1,3,6,1,4,1,21296,2,2,2,3,12,2,1,35),_OtsPtpOtsAlsOprMax_Type())
otsPtpOtsAlsOprMax.setMaxAccess(_C)
if mibBuilder.loadTexts:otsPtpOtsAlsOprMax.setStatus(_A)
_OtsPtpOtsAlsOprAve_Type=FloatHundredths
_OtsPtpOtsAlsOprAve_Object=MibTableColumn
otsPtpOtsAlsOprAve=_OtsPtpOtsAlsOprAve_Object((1,3,6,1,4,1,21296,2,2,2,3,12,2,1,36),_OtsPtpOtsAlsOprAve_Type())
otsPtpOtsAlsOprAve.setMaxAccess(_C)
if mibBuilder.loadTexts:otsPtpOtsAlsOprAve.setStatus(_A)
_OtsPtpOtsAlsOptMin_Type=FloatHundredths
_OtsPtpOtsAlsOptMin_Object=MibTableColumn
otsPtpOtsAlsOptMin=_OtsPtpOtsAlsOptMin_Object((1,3,6,1,4,1,21296,2,2,2,3,12,2,1,37),_OtsPtpOtsAlsOptMin_Type())
otsPtpOtsAlsOptMin.setMaxAccess(_C)
if mibBuilder.loadTexts:otsPtpOtsAlsOptMin.setStatus(_A)
_OtsPtpOtsAlsOptMax_Type=FloatHundredths
_OtsPtpOtsAlsOptMax_Object=MibTableColumn
otsPtpOtsAlsOptMax=_OtsPtpOtsAlsOptMax_Object((1,3,6,1,4,1,21296,2,2,2,3,12,2,1,38),_OtsPtpOtsAlsOptMax_Type())
otsPtpOtsAlsOptMax.setMaxAccess(_C)
if mibBuilder.loadTexts:otsPtpOtsAlsOptMax.setStatus(_A)
_OtsPtpOtsAlsOptAve_Type=FloatHundredths
_OtsPtpOtsAlsOptAve_Object=MibTableColumn
otsPtpOtsAlsOptAve=_OtsPtpOtsAlsOptAve_Object((1,3,6,1,4,1,21296,2,2,2,3,12,2,1,39),_OtsPtpOtsAlsOptAve_Type())
otsPtpOtsAlsOptAve.setMaxAccess(_C)
if mibBuilder.loadTexts:otsPtpOtsAlsOptAve.setStatus(_A)
_OtsPtpOtsAlsLbcMin_Type=FloatHundredths
_OtsPtpOtsAlsLbcMin_Object=MibTableColumn
otsPtpOtsAlsLbcMin=_OtsPtpOtsAlsLbcMin_Object((1,3,6,1,4,1,21296,2,2,2,3,12,2,1,40),_OtsPtpOtsAlsLbcMin_Type())
otsPtpOtsAlsLbcMin.setMaxAccess(_C)
if mibBuilder.loadTexts:otsPtpOtsAlsLbcMin.setStatus(_A)
_OtsPtpOtsAlsLbcMax_Type=FloatHundredths
_OtsPtpOtsAlsLbcMax_Object=MibTableColumn
otsPtpOtsAlsLbcMax=_OtsPtpOtsAlsLbcMax_Object((1,3,6,1,4,1,21296,2,2,2,3,12,2,1,41),_OtsPtpOtsAlsLbcMax_Type())
otsPtpOtsAlsLbcMax.setMaxAccess(_C)
if mibBuilder.loadTexts:otsPtpOtsAlsLbcMax.setStatus(_A)
_OtsPtpOtsAlsLbcAve_Type=FloatHundredths
_OtsPtpOtsAlsLbcAve_Object=MibTableColumn
otsPtpOtsAlsLbcAve=_OtsPtpOtsAlsLbcAve_Object((1,3,6,1,4,1,21296,2,2,2,3,12,2,1,42),_OtsPtpOtsAlsLbcAve_Type())
otsPtpOtsAlsLbcAve.setMaxAccess(_C)
if mibBuilder.loadTexts:otsPtpOtsAlsLbcAve.setStatus(_A)
_OtsPtpPmConformance_ObjectIdentity=ObjectIdentity
otsPtpPmConformance=_OtsPtpPmConformance_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,3,12,3))
_OtsPtpPmCompliances_ObjectIdentity=ObjectIdentity
otsPtpPmCompliances=_OtsPtpPmCompliances_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,3,12,3,1))
_OtsPtpPmGroups_ObjectIdentity=ObjectIdentity
otsPtpPmGroups=_OtsPtpPmGroups_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,3,12,3,2))
otsPtpPmGroup=ObjectGroup((1,3,6,1,4,1,21296,2,2,2,3,12,3,2,1))
otsPtpPmGroup.setObjects(*((_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w)))
if mibBuilder.loadTexts:otsPtpPmGroup.setStatus(_A)
otsPtpPmRealGroup=ObjectGroup((1,3,6,1,4,1,21296,2,2,2,3,12,3,2,2))
otsPtpPmRealGroup.setObjects(*((_B,_x),(_B,_y),(_B,_z),(_B,_A0),(_B,_A1),(_B,_A2),(_B,_A3),(_B,_A4),(_B,_A5),(_B,_A6),(_B,_A7),(_B,_A8),(_B,_A9),(_B,_AA),(_B,_AB),(_B,_AC),(_B,_AD)))
if mibBuilder.loadTexts:otsPtpPmRealGroup.setStatus(_A)
otsPtpPmCompliance=ModuleCompliance((1,3,6,1,4,1,21296,2,2,2,3,12,3,1,1))
otsPtpPmCompliance.setObjects((_B,_AE))
if mibBuilder.loadTexts:otsPtpPmCompliance.setStatus(_A)
otsPtpPmRealCompliance=ModuleCompliance((1,3,6,1,4,1,21296,2,2,2,3,12,3,1,2))
otsPtpPmRealCompliance.setObjects((_B,_AF))
if mibBuilder.loadTexts:otsPtpPmRealCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'otsPtpPmMIB':otsPtpPmMIB,'otsPtpPmRealTable':otsPtpPmRealTable,'otsPtpPmRealEntry':otsPtpPmRealEntry,_x:otsPtpPmRealOtsOpt,_y:otsPtpPmRealOtsOptOsaTapRatio,_z:otsPtpPmRealOtsOpr,_A0:otsPtpPmRealOtsOprOsaTapRatio,_A1:otsPtpPmRealOtsLbc1,_A2:otsPtpPmRealOtsLbc2,_A3:otsPtpPmRealOtsLbc3,_A4:otsPtpPmRealOtsLbc4,_A5:otsPtpPmRealOtsLpwr1,_A6:otsPtpPmRealOtsLpwr2,_A7:otsPtpPmRealOtsLpwr3,_A8:otsPtpPmRealOtsLpwr4,_A9:otsPtpPmRealOtsAlsOpr,_AA:otsPtpPmRealOtsAlsOpt,_AB:otsPtpPmRealOtsAlsLbc,_AC:otsPtpPmRealRxPostEdfaOsaTapRatio,_AD:otsPtpPmRealOprQ,'otsPtpPmTable':otsPtpPmTable,'otsPtpPmEntry':otsPtpPmEntry,_H:otsPtpPmTimestamp,_G:otsPtpPmSampleDuration,_J:otsPtpPmValidity,_K:otsPtpPmOtsOptMin,_L:otsPtpPmOtsOptMax,_M:otsPtpPmOtsOptAve,_N:otsPtpPmOtsOprMin,_O:otsPtpPmOtsOprMax,_P:otsPtpPmOtsOprAve,_Q:otsPtpPmOtsLbc1Min,_R:otsPtpPmOtsLbc1Max,_S:otsPtpPmOtsLbc1Ave,_T:otsPtpPmOtsLbc2Min,_U:otsPtpPmOtsLbc2Max,_V:otsPtpPmOtsLbc2Ave,_W:otsPtpPmOtsLbc3Min,_X:otsPtpPmOtsLbc3Max,_Y:otsPtpPmOtsLbc3Ave,_Z:otsPtpPmOtsLbc4Min,_a:otsPtpPmOtsLbc4Max,_b:otsPtpPmOtsLbc4Ave,_c:otsPtpPmOtsLpwr1Min,_d:otsPtpPmOtsLpwr1Max,_e:otsPtpPmOtsLpwr1Ave,_f:otsPtpPmOtsLpwr2Min,_g:otsPtpPmOtsLpwr2Max,_h:otsPtpPmOtsLpwr2Ave,_i:otsPtpPmOtsLpwr3Min,_j:otsPtpPmOtsLpwr3Max,_k:otsPtpPmOtsLpwr3Ave,_l:otsPtpPmOtsLpwr4Min,_m:otsPtpPmOtsLpwr4Max,_n:otsPtpPmOtsLpwr4Ave,_o:otsPtpOtsAlsOprMin,_p:otsPtpOtsAlsOprMax,_q:otsPtpOtsAlsOprAve,_r:otsPtpOtsAlsOptMin,_s:otsPtpOtsAlsOptMax,_t:otsPtpOtsAlsOptAve,_u:otsPtpOtsAlsLbcMin,_v:otsPtpOtsAlsLbcMax,_w:otsPtpOtsAlsLbcAve,'otsPtpPmConformance':otsPtpPmConformance,'otsPtpPmCompliances':otsPtpPmCompliances,'otsPtpPmCompliance':otsPtpPmCompliance,'otsPtpPmRealCompliance':otsPtpPmRealCompliance,'otsPtpPmGroups':otsPtpPmGroups,_AE:otsPtpPmGroup,_AF:otsPtpPmRealGroup})