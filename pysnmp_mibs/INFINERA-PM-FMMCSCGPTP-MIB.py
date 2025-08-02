_f='fmmcScgPtpPmRealGroup'
_e='fmmcScgPtpPmGroup'
_d='fmmcScgPtpPmRealRxEdfaLbc'
_c='fmmcScgPtpPmRealEdfaLbcTx'
_b='fmmcScgPtpPmRealRxEdfaOpt'
_a='fmmcScgPtpPmRealTxEdfaOpr'
_Z='fmmcScgPtpPmRealOprOsaTapRatio'
_Y='fmmcScgPtpPmRealOptOsaTapRatio'
_X='fmmcScgPtpPmRealCmnScgOpr'
_W='fmmcScgPtpPmRealCmnScgOpt'
_V='fmmcScgPtpPmRxEdfaOptAve'
_U='fmmcScgPtpPmRxEdfaOptMax'
_T='fmmcScgPtpPmRxEdfaOptMin'
_S='fmmcScgPtpPmTxEdfaOprAve'
_R='fmmcScgPtpPmTxEdfaOprMax'
_Q='fmmcScgPtpPmTxEdfaOprMin'
_P='fmmcScgPtpPmCmnScgOprAve'
_O='fmmcScgPtpPmCmnScgOprMax'
_N='fmmcScgPtpPmCmnScgOprMin'
_M='fmmcScgPtpPmCmnScgOptAve'
_L='fmmcScgPtpPmCmnScgOptMax'
_K='fmmcScgPtpPmCmnScgOptMin'
_J='fmmcScgPtpPmValidity'
_I='not-accessible'
_H='fmmcScgPtpPmTimestamp'
_G='fmmcScgPtpPmSampleDuration'
_F='Integer32'
_E='ifIndex'
_D='IF-MIB'
_C='read-only'
_B='INFINERA-PM-FMMCSCGPTP-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_D,_E)
perfMon,=mibBuilder.importSymbols('INFINERA-REG-MIB','perfMon')
FloatHundredths,InfnSampleDuration=mibBuilder.importSymbols('INFINERA-TC-MIB','FloatHundredths','InfnSampleDuration')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
fmmcScgPtpPmMIB=ModuleIdentity((1,3,6,1,4,1,21296,2,2,2,3,43))
if mibBuilder.loadTexts:fmmcScgPtpPmMIB.setRevisions(('2015-04-18 00:00',))
_FmmcScgPtpPmRealTable_Object=MibTable
fmmcScgPtpPmRealTable=_FmmcScgPtpPmRealTable_Object((1,3,6,1,4,1,21296,2,2,2,3,43,1))
if mibBuilder.loadTexts:fmmcScgPtpPmRealTable.setStatus(_A)
_FmmcScgPtpPmRealEntry_Object=MibTableRow
fmmcScgPtpPmRealEntry=_FmmcScgPtpPmRealEntry_Object((1,3,6,1,4,1,21296,2,2,2,3,43,1,1))
fmmcScgPtpPmRealEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:fmmcScgPtpPmRealEntry.setStatus(_A)
_FmmcScgPtpPmRealCmnScgOpt_Type=FloatHundredths
_FmmcScgPtpPmRealCmnScgOpt_Object=MibTableColumn
fmmcScgPtpPmRealCmnScgOpt=_FmmcScgPtpPmRealCmnScgOpt_Object((1,3,6,1,4,1,21296,2,2,2,3,43,1,1,1),_FmmcScgPtpPmRealCmnScgOpt_Type())
fmmcScgPtpPmRealCmnScgOpt.setMaxAccess(_C)
if mibBuilder.loadTexts:fmmcScgPtpPmRealCmnScgOpt.setStatus(_A)
_FmmcScgPtpPmRealCmnScgOpr_Type=FloatHundredths
_FmmcScgPtpPmRealCmnScgOpr_Object=MibTableColumn
fmmcScgPtpPmRealCmnScgOpr=_FmmcScgPtpPmRealCmnScgOpr_Object((1,3,6,1,4,1,21296,2,2,2,3,43,1,1,2),_FmmcScgPtpPmRealCmnScgOpr_Type())
fmmcScgPtpPmRealCmnScgOpr.setMaxAccess(_C)
if mibBuilder.loadTexts:fmmcScgPtpPmRealCmnScgOpr.setStatus(_A)
_FmmcScgPtpPmRealOptOsaTapRatio_Type=FloatHundredths
_FmmcScgPtpPmRealOptOsaTapRatio_Object=MibTableColumn
fmmcScgPtpPmRealOptOsaTapRatio=_FmmcScgPtpPmRealOptOsaTapRatio_Object((1,3,6,1,4,1,21296,2,2,2,3,43,1,1,3),_FmmcScgPtpPmRealOptOsaTapRatio_Type())
fmmcScgPtpPmRealOptOsaTapRatio.setMaxAccess(_C)
if mibBuilder.loadTexts:fmmcScgPtpPmRealOptOsaTapRatio.setStatus(_A)
_FmmcScgPtpPmRealOprOsaTapRatio_Type=FloatHundredths
_FmmcScgPtpPmRealOprOsaTapRatio_Object=MibTableColumn
fmmcScgPtpPmRealOprOsaTapRatio=_FmmcScgPtpPmRealOprOsaTapRatio_Object((1,3,6,1,4,1,21296,2,2,2,3,43,1,1,4),_FmmcScgPtpPmRealOprOsaTapRatio_Type())
fmmcScgPtpPmRealOprOsaTapRatio.setMaxAccess(_C)
if mibBuilder.loadTexts:fmmcScgPtpPmRealOprOsaTapRatio.setStatus(_A)
_FmmcScgPtpPmRealTxEdfaOpr_Type=FloatHundredths
_FmmcScgPtpPmRealTxEdfaOpr_Object=MibTableColumn
fmmcScgPtpPmRealTxEdfaOpr=_FmmcScgPtpPmRealTxEdfaOpr_Object((1,3,6,1,4,1,21296,2,2,2,3,43,1,1,5),_FmmcScgPtpPmRealTxEdfaOpr_Type())
fmmcScgPtpPmRealTxEdfaOpr.setMaxAccess(_C)
if mibBuilder.loadTexts:fmmcScgPtpPmRealTxEdfaOpr.setStatus(_A)
_FmmcScgPtpPmRealRxEdfaOpt_Type=FloatHundredths
_FmmcScgPtpPmRealRxEdfaOpt_Object=MibTableColumn
fmmcScgPtpPmRealRxEdfaOpt=_FmmcScgPtpPmRealRxEdfaOpt_Object((1,3,6,1,4,1,21296,2,2,2,3,43,1,1,6),_FmmcScgPtpPmRealRxEdfaOpt_Type())
fmmcScgPtpPmRealRxEdfaOpt.setMaxAccess(_C)
if mibBuilder.loadTexts:fmmcScgPtpPmRealRxEdfaOpt.setStatus(_A)
_FmmcScgPtpPmRealEdfaLbcTx_Type=FloatHundredths
_FmmcScgPtpPmRealEdfaLbcTx_Object=MibTableColumn
fmmcScgPtpPmRealEdfaLbcTx=_FmmcScgPtpPmRealEdfaLbcTx_Object((1,3,6,1,4,1,21296,2,2,2,3,43,1,1,7),_FmmcScgPtpPmRealEdfaLbcTx_Type())
fmmcScgPtpPmRealEdfaLbcTx.setMaxAccess(_C)
if mibBuilder.loadTexts:fmmcScgPtpPmRealEdfaLbcTx.setStatus(_A)
_FmmcScgPtpPmRealRxEdfaLbc_Type=FloatHundredths
_FmmcScgPtpPmRealRxEdfaLbc_Object=MibTableColumn
fmmcScgPtpPmRealRxEdfaLbc=_FmmcScgPtpPmRealRxEdfaLbc_Object((1,3,6,1,4,1,21296,2,2,2,3,43,1,1,8),_FmmcScgPtpPmRealRxEdfaLbc_Type())
fmmcScgPtpPmRealRxEdfaLbc.setMaxAccess(_C)
if mibBuilder.loadTexts:fmmcScgPtpPmRealRxEdfaLbc.setStatus(_A)
_FmmcScgPtpPmTable_Object=MibTable
fmmcScgPtpPmTable=_FmmcScgPtpPmTable_Object((1,3,6,1,4,1,21296,2,2,2,3,43,2))
if mibBuilder.loadTexts:fmmcScgPtpPmTable.setStatus(_A)
_FmmcScgPtpPmEntry_Object=MibTableRow
fmmcScgPtpPmEntry=_FmmcScgPtpPmEntry_Object((1,3,6,1,4,1,21296,2,2,2,3,43,2,1))
fmmcScgPtpPmEntry.setIndexNames((0,_D,_E),(0,_B,_G),(0,_B,_H))
if mibBuilder.loadTexts:fmmcScgPtpPmEntry.setStatus(_A)
class _FmmcScgPtpPmTimestamp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_FmmcScgPtpPmTimestamp_Type.__name__=_F
_FmmcScgPtpPmTimestamp_Object=MibTableColumn
fmmcScgPtpPmTimestamp=_FmmcScgPtpPmTimestamp_Object((1,3,6,1,4,1,21296,2,2,2,3,43,2,1,1),_FmmcScgPtpPmTimestamp_Type())
fmmcScgPtpPmTimestamp.setMaxAccess(_I)
if mibBuilder.loadTexts:fmmcScgPtpPmTimestamp.setStatus(_A)
class _FmmcScgPtpPmSampleDuration_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('fifteenMinutes',1),('day',2)))
_FmmcScgPtpPmSampleDuration_Type.__name__=_F
_FmmcScgPtpPmSampleDuration_Object=MibTableColumn
fmmcScgPtpPmSampleDuration=_FmmcScgPtpPmSampleDuration_Object((1,3,6,1,4,1,21296,2,2,2,3,43,2,1,2),_FmmcScgPtpPmSampleDuration_Type())
fmmcScgPtpPmSampleDuration.setMaxAccess(_I)
if mibBuilder.loadTexts:fmmcScgPtpPmSampleDuration.setStatus(_A)
_FmmcScgPtpPmValidity_Type=TruthValue
_FmmcScgPtpPmValidity_Object=MibTableColumn
fmmcScgPtpPmValidity=_FmmcScgPtpPmValidity_Object((1,3,6,1,4,1,21296,2,2,2,3,43,2,1,3),_FmmcScgPtpPmValidity_Type())
fmmcScgPtpPmValidity.setMaxAccess(_C)
if mibBuilder.loadTexts:fmmcScgPtpPmValidity.setStatus(_A)
_FmmcScgPtpPmCmnScgOptMin_Type=FloatHundredths
_FmmcScgPtpPmCmnScgOptMin_Object=MibTableColumn
fmmcScgPtpPmCmnScgOptMin=_FmmcScgPtpPmCmnScgOptMin_Object((1,3,6,1,4,1,21296,2,2,2,3,43,2,1,4),_FmmcScgPtpPmCmnScgOptMin_Type())
fmmcScgPtpPmCmnScgOptMin.setMaxAccess(_C)
if mibBuilder.loadTexts:fmmcScgPtpPmCmnScgOptMin.setStatus(_A)
_FmmcScgPtpPmCmnScgOptMax_Type=FloatHundredths
_FmmcScgPtpPmCmnScgOptMax_Object=MibTableColumn
fmmcScgPtpPmCmnScgOptMax=_FmmcScgPtpPmCmnScgOptMax_Object((1,3,6,1,4,1,21296,2,2,2,3,43,2,1,5),_FmmcScgPtpPmCmnScgOptMax_Type())
fmmcScgPtpPmCmnScgOptMax.setMaxAccess(_C)
if mibBuilder.loadTexts:fmmcScgPtpPmCmnScgOptMax.setStatus(_A)
_FmmcScgPtpPmCmnScgOptAve_Type=FloatHundredths
_FmmcScgPtpPmCmnScgOptAve_Object=MibTableColumn
fmmcScgPtpPmCmnScgOptAve=_FmmcScgPtpPmCmnScgOptAve_Object((1,3,6,1,4,1,21296,2,2,2,3,43,2,1,6),_FmmcScgPtpPmCmnScgOptAve_Type())
fmmcScgPtpPmCmnScgOptAve.setMaxAccess(_C)
if mibBuilder.loadTexts:fmmcScgPtpPmCmnScgOptAve.setStatus(_A)
_FmmcScgPtpPmCmnScgOprMin_Type=FloatHundredths
_FmmcScgPtpPmCmnScgOprMin_Object=MibTableColumn
fmmcScgPtpPmCmnScgOprMin=_FmmcScgPtpPmCmnScgOprMin_Object((1,3,6,1,4,1,21296,2,2,2,3,43,2,1,7),_FmmcScgPtpPmCmnScgOprMin_Type())
fmmcScgPtpPmCmnScgOprMin.setMaxAccess(_C)
if mibBuilder.loadTexts:fmmcScgPtpPmCmnScgOprMin.setStatus(_A)
_FmmcScgPtpPmCmnScgOprMax_Type=FloatHundredths
_FmmcScgPtpPmCmnScgOprMax_Object=MibTableColumn
fmmcScgPtpPmCmnScgOprMax=_FmmcScgPtpPmCmnScgOprMax_Object((1,3,6,1,4,1,21296,2,2,2,3,43,2,1,8),_FmmcScgPtpPmCmnScgOprMax_Type())
fmmcScgPtpPmCmnScgOprMax.setMaxAccess(_C)
if mibBuilder.loadTexts:fmmcScgPtpPmCmnScgOprMax.setStatus(_A)
_FmmcScgPtpPmCmnScgOprAve_Type=FloatHundredths
_FmmcScgPtpPmCmnScgOprAve_Object=MibTableColumn
fmmcScgPtpPmCmnScgOprAve=_FmmcScgPtpPmCmnScgOprAve_Object((1,3,6,1,4,1,21296,2,2,2,3,43,2,1,9),_FmmcScgPtpPmCmnScgOprAve_Type())
fmmcScgPtpPmCmnScgOprAve.setMaxAccess(_C)
if mibBuilder.loadTexts:fmmcScgPtpPmCmnScgOprAve.setStatus(_A)
_FmmcScgPtpPmTxEdfaOprMin_Type=FloatHundredths
_FmmcScgPtpPmTxEdfaOprMin_Object=MibTableColumn
fmmcScgPtpPmTxEdfaOprMin=_FmmcScgPtpPmTxEdfaOprMin_Object((1,3,6,1,4,1,21296,2,2,2,3,43,2,1,10),_FmmcScgPtpPmTxEdfaOprMin_Type())
fmmcScgPtpPmTxEdfaOprMin.setMaxAccess(_C)
if mibBuilder.loadTexts:fmmcScgPtpPmTxEdfaOprMin.setStatus(_A)
_FmmcScgPtpPmTxEdfaOprMax_Type=FloatHundredths
_FmmcScgPtpPmTxEdfaOprMax_Object=MibTableColumn
fmmcScgPtpPmTxEdfaOprMax=_FmmcScgPtpPmTxEdfaOprMax_Object((1,3,6,1,4,1,21296,2,2,2,3,43,2,1,11),_FmmcScgPtpPmTxEdfaOprMax_Type())
fmmcScgPtpPmTxEdfaOprMax.setMaxAccess(_C)
if mibBuilder.loadTexts:fmmcScgPtpPmTxEdfaOprMax.setStatus(_A)
_FmmcScgPtpPmTxEdfaOprAve_Type=FloatHundredths
_FmmcScgPtpPmTxEdfaOprAve_Object=MibTableColumn
fmmcScgPtpPmTxEdfaOprAve=_FmmcScgPtpPmTxEdfaOprAve_Object((1,3,6,1,4,1,21296,2,2,2,3,43,2,1,12),_FmmcScgPtpPmTxEdfaOprAve_Type())
fmmcScgPtpPmTxEdfaOprAve.setMaxAccess(_C)
if mibBuilder.loadTexts:fmmcScgPtpPmTxEdfaOprAve.setStatus(_A)
_FmmcScgPtpPmRxEdfaOptMin_Type=FloatHundredths
_FmmcScgPtpPmRxEdfaOptMin_Object=MibTableColumn
fmmcScgPtpPmRxEdfaOptMin=_FmmcScgPtpPmRxEdfaOptMin_Object((1,3,6,1,4,1,21296,2,2,2,3,43,2,1,13),_FmmcScgPtpPmRxEdfaOptMin_Type())
fmmcScgPtpPmRxEdfaOptMin.setMaxAccess(_C)
if mibBuilder.loadTexts:fmmcScgPtpPmRxEdfaOptMin.setStatus(_A)
_FmmcScgPtpPmRxEdfaOptMax_Type=FloatHundredths
_FmmcScgPtpPmRxEdfaOptMax_Object=MibTableColumn
fmmcScgPtpPmRxEdfaOptMax=_FmmcScgPtpPmRxEdfaOptMax_Object((1,3,6,1,4,1,21296,2,2,2,3,43,2,1,14),_FmmcScgPtpPmRxEdfaOptMax_Type())
fmmcScgPtpPmRxEdfaOptMax.setMaxAccess(_C)
if mibBuilder.loadTexts:fmmcScgPtpPmRxEdfaOptMax.setStatus(_A)
_FmmcScgPtpPmRxEdfaOptAve_Type=FloatHundredths
_FmmcScgPtpPmRxEdfaOptAve_Object=MibTableColumn
fmmcScgPtpPmRxEdfaOptAve=_FmmcScgPtpPmRxEdfaOptAve_Object((1,3,6,1,4,1,21296,2,2,2,3,43,2,1,15),_FmmcScgPtpPmRxEdfaOptAve_Type())
fmmcScgPtpPmRxEdfaOptAve.setMaxAccess(_C)
if mibBuilder.loadTexts:fmmcScgPtpPmRxEdfaOptAve.setStatus(_A)
_FmmcScgPtpPmConformance_ObjectIdentity=ObjectIdentity
fmmcScgPtpPmConformance=_FmmcScgPtpPmConformance_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,3,43,3))
_FmmcScgPtpPmCompliances_ObjectIdentity=ObjectIdentity
fmmcScgPtpPmCompliances=_FmmcScgPtpPmCompliances_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,3,43,3,1))
_FmmcScgPtpPmGroups_ObjectIdentity=ObjectIdentity
fmmcScgPtpPmGroups=_FmmcScgPtpPmGroups_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,3,43,3,2))
fmmcScgPtpPmGroup=ObjectGroup((1,3,6,1,4,1,21296,2,2,2,3,43,3,2,1))
fmmcScgPtpPmGroup.setObjects(*((_B,_H),(_B,_G),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V)))
if mibBuilder.loadTexts:fmmcScgPtpPmGroup.setStatus(_A)
fmmcScgPtpPmRealGroup=ObjectGroup((1,3,6,1,4,1,21296,2,2,2,3,43,3,2,2))
fmmcScgPtpPmRealGroup.setObjects(*((_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d)))
if mibBuilder.loadTexts:fmmcScgPtpPmRealGroup.setStatus(_A)
fmmcScgPtpPmCompliance=ModuleCompliance((1,3,6,1,4,1,21296,2,2,2,3,43,3,1,1))
fmmcScgPtpPmCompliance.setObjects((_B,_e))
if mibBuilder.loadTexts:fmmcScgPtpPmCompliance.setStatus(_A)
fmmcScgPtpPmRealCompliance=ModuleCompliance((1,3,6,1,4,1,21296,2,2,2,3,43,3,1,2))
fmmcScgPtpPmRealCompliance.setObjects((_B,_f))
if mibBuilder.loadTexts:fmmcScgPtpPmRealCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'fmmcScgPtpPmMIB':fmmcScgPtpPmMIB,'fmmcScgPtpPmRealTable':fmmcScgPtpPmRealTable,'fmmcScgPtpPmRealEntry':fmmcScgPtpPmRealEntry,_W:fmmcScgPtpPmRealCmnScgOpt,_X:fmmcScgPtpPmRealCmnScgOpr,_Y:fmmcScgPtpPmRealOptOsaTapRatio,_Z:fmmcScgPtpPmRealOprOsaTapRatio,_a:fmmcScgPtpPmRealTxEdfaOpr,_b:fmmcScgPtpPmRealRxEdfaOpt,_c:fmmcScgPtpPmRealEdfaLbcTx,_d:fmmcScgPtpPmRealRxEdfaLbc,'fmmcScgPtpPmTable':fmmcScgPtpPmTable,'fmmcScgPtpPmEntry':fmmcScgPtpPmEntry,_H:fmmcScgPtpPmTimestamp,_G:fmmcScgPtpPmSampleDuration,_J:fmmcScgPtpPmValidity,_K:fmmcScgPtpPmCmnScgOptMin,_L:fmmcScgPtpPmCmnScgOptMax,_M:fmmcScgPtpPmCmnScgOptAve,_N:fmmcScgPtpPmCmnScgOprMin,_O:fmmcScgPtpPmCmnScgOprMax,_P:fmmcScgPtpPmCmnScgOprAve,_Q:fmmcScgPtpPmTxEdfaOprMin,_R:fmmcScgPtpPmTxEdfaOprMax,_S:fmmcScgPtpPmTxEdfaOprAve,_T:fmmcScgPtpPmRxEdfaOptMin,_U:fmmcScgPtpPmRxEdfaOptMax,_V:fmmcScgPtpPmRxEdfaOptAve,'fmmcScgPtpPmConformance':fmmcScgPtpPmConformance,'fmmcScgPtpPmCompliances':fmmcScgPtpPmCompliances,'fmmcScgPtpPmCompliance':fmmcScgPtpPmCompliance,'fmmcScgPtpPmRealCompliance':fmmcScgPtpPmRealCompliance,'fmmcScgPtpPmGroups':fmmcScgPtpPmGroups,_e:fmmcScgPtpPmGroup,_f:fmmcScgPtpPmRealGroup})