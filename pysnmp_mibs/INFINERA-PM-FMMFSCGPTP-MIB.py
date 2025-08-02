_X='fmmfScgPtpPmRealGroup'
_W='fmmfScgPtpPmGroup'
_V='fmmfScgPtpPmRealOptOsaTapRatio'
_U='fmmfScgPtpPmRealCmnScgOpr'
_T='fmmfScgPtpPmRealCmnScgOpt'
_S='fmmfScgPtpPmOptOsaTapRatioAve'
_R='fmmfScgPtpPmOptOsaTapRatioMax'
_Q='fmmfScgPtpPmOptOsaTapRatioMin'
_P='fmmfScgPtpPmCmnScgOprAve'
_O='fmmfScgPtpPmCmnScgOprMax'
_N='fmmfScgPtpPmCmnScgOprMin'
_M='fmmfScgPtpPmCmnScgOptAve'
_L='fmmfScgPtpPmCmnScgOptMax'
_K='fmmfScgPtpPmCmnScgOptMin'
_J='fmmfScgPtpPmValidity'
_I='not-accessible'
_H='fmmfScgPtpPmTimestamp'
_G='fmmfScgPtpPmSampleDuration'
_F='Integer32'
_E='ifIndex'
_D='IF-MIB'
_C='read-only'
_B='INFINERA-PM-FMMFSCGPTP-MIB'
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
fmmfScgPtpPmMIB=ModuleIdentity((1,3,6,1,4,1,21296,2,2,2,3,49))
if mibBuilder.loadTexts:fmmfScgPtpPmMIB.setRevisions(('2015-04-18 00:00',))
_FmmfScgPtpPmRealTable_Object=MibTable
fmmfScgPtpPmRealTable=_FmmfScgPtpPmRealTable_Object((1,3,6,1,4,1,21296,2,2,2,3,49,1))
if mibBuilder.loadTexts:fmmfScgPtpPmRealTable.setStatus(_A)
_FmmfScgPtpPmRealEntry_Object=MibTableRow
fmmfScgPtpPmRealEntry=_FmmfScgPtpPmRealEntry_Object((1,3,6,1,4,1,21296,2,2,2,3,49,1,1))
fmmfScgPtpPmRealEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:fmmfScgPtpPmRealEntry.setStatus(_A)
_FmmfScgPtpPmRealCmnScgOpt_Type=FloatHundredths
_FmmfScgPtpPmRealCmnScgOpt_Object=MibTableColumn
fmmfScgPtpPmRealCmnScgOpt=_FmmfScgPtpPmRealCmnScgOpt_Object((1,3,6,1,4,1,21296,2,2,2,3,49,1,1,1),_FmmfScgPtpPmRealCmnScgOpt_Type())
fmmfScgPtpPmRealCmnScgOpt.setMaxAccess(_C)
if mibBuilder.loadTexts:fmmfScgPtpPmRealCmnScgOpt.setStatus(_A)
_FmmfScgPtpPmRealCmnScgOpr_Type=FloatHundredths
_FmmfScgPtpPmRealCmnScgOpr_Object=MibTableColumn
fmmfScgPtpPmRealCmnScgOpr=_FmmfScgPtpPmRealCmnScgOpr_Object((1,3,6,1,4,1,21296,2,2,2,3,49,1,1,2),_FmmfScgPtpPmRealCmnScgOpr_Type())
fmmfScgPtpPmRealCmnScgOpr.setMaxAccess(_C)
if mibBuilder.loadTexts:fmmfScgPtpPmRealCmnScgOpr.setStatus(_A)
_FmmfScgPtpPmRealOptOsaTapRatio_Type=FloatHundredths
_FmmfScgPtpPmRealOptOsaTapRatio_Object=MibTableColumn
fmmfScgPtpPmRealOptOsaTapRatio=_FmmfScgPtpPmRealOptOsaTapRatio_Object((1,3,6,1,4,1,21296,2,2,2,3,49,1,1,3),_FmmfScgPtpPmRealOptOsaTapRatio_Type())
fmmfScgPtpPmRealOptOsaTapRatio.setMaxAccess(_C)
if mibBuilder.loadTexts:fmmfScgPtpPmRealOptOsaTapRatio.setStatus(_A)
_FmmfScgPtpPmTable_Object=MibTable
fmmfScgPtpPmTable=_FmmfScgPtpPmTable_Object((1,3,6,1,4,1,21296,2,2,2,3,49,2))
if mibBuilder.loadTexts:fmmfScgPtpPmTable.setStatus(_A)
_FmmfScgPtpPmEntry_Object=MibTableRow
fmmfScgPtpPmEntry=_FmmfScgPtpPmEntry_Object((1,3,6,1,4,1,21296,2,2,2,3,49,2,1))
fmmfScgPtpPmEntry.setIndexNames((0,_D,_E),(0,_B,_G),(0,_B,_H))
if mibBuilder.loadTexts:fmmfScgPtpPmEntry.setStatus(_A)
class _FmmfScgPtpPmTimestamp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_FmmfScgPtpPmTimestamp_Type.__name__=_F
_FmmfScgPtpPmTimestamp_Object=MibTableColumn
fmmfScgPtpPmTimestamp=_FmmfScgPtpPmTimestamp_Object((1,3,6,1,4,1,21296,2,2,2,3,49,2,1,1),_FmmfScgPtpPmTimestamp_Type())
fmmfScgPtpPmTimestamp.setMaxAccess(_I)
if mibBuilder.loadTexts:fmmfScgPtpPmTimestamp.setStatus(_A)
class _FmmfScgPtpPmSampleDuration_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('fifteenMinutes',1),('day',2)))
_FmmfScgPtpPmSampleDuration_Type.__name__=_F
_FmmfScgPtpPmSampleDuration_Object=MibTableColumn
fmmfScgPtpPmSampleDuration=_FmmfScgPtpPmSampleDuration_Object((1,3,6,1,4,1,21296,2,2,2,3,49,2,1,2),_FmmfScgPtpPmSampleDuration_Type())
fmmfScgPtpPmSampleDuration.setMaxAccess(_I)
if mibBuilder.loadTexts:fmmfScgPtpPmSampleDuration.setStatus(_A)
_FmmfScgPtpPmValidity_Type=TruthValue
_FmmfScgPtpPmValidity_Object=MibTableColumn
fmmfScgPtpPmValidity=_FmmfScgPtpPmValidity_Object((1,3,6,1,4,1,21296,2,2,2,3,49,2,1,3),_FmmfScgPtpPmValidity_Type())
fmmfScgPtpPmValidity.setMaxAccess(_C)
if mibBuilder.loadTexts:fmmfScgPtpPmValidity.setStatus(_A)
_FmmfScgPtpPmCmnScgOptMin_Type=FloatHundredths
_FmmfScgPtpPmCmnScgOptMin_Object=MibTableColumn
fmmfScgPtpPmCmnScgOptMin=_FmmfScgPtpPmCmnScgOptMin_Object((1,3,6,1,4,1,21296,2,2,2,3,49,2,1,4),_FmmfScgPtpPmCmnScgOptMin_Type())
fmmfScgPtpPmCmnScgOptMin.setMaxAccess(_C)
if mibBuilder.loadTexts:fmmfScgPtpPmCmnScgOptMin.setStatus(_A)
_FmmfScgPtpPmCmnScgOptMax_Type=FloatHundredths
_FmmfScgPtpPmCmnScgOptMax_Object=MibTableColumn
fmmfScgPtpPmCmnScgOptMax=_FmmfScgPtpPmCmnScgOptMax_Object((1,3,6,1,4,1,21296,2,2,2,3,49,2,1,5),_FmmfScgPtpPmCmnScgOptMax_Type())
fmmfScgPtpPmCmnScgOptMax.setMaxAccess(_C)
if mibBuilder.loadTexts:fmmfScgPtpPmCmnScgOptMax.setStatus(_A)
_FmmfScgPtpPmCmnScgOptAve_Type=FloatHundredths
_FmmfScgPtpPmCmnScgOptAve_Object=MibTableColumn
fmmfScgPtpPmCmnScgOptAve=_FmmfScgPtpPmCmnScgOptAve_Object((1,3,6,1,4,1,21296,2,2,2,3,49,2,1,6),_FmmfScgPtpPmCmnScgOptAve_Type())
fmmfScgPtpPmCmnScgOptAve.setMaxAccess(_C)
if mibBuilder.loadTexts:fmmfScgPtpPmCmnScgOptAve.setStatus(_A)
_FmmfScgPtpPmCmnScgOprMin_Type=FloatHundredths
_FmmfScgPtpPmCmnScgOprMin_Object=MibTableColumn
fmmfScgPtpPmCmnScgOprMin=_FmmfScgPtpPmCmnScgOprMin_Object((1,3,6,1,4,1,21296,2,2,2,3,49,2,1,7),_FmmfScgPtpPmCmnScgOprMin_Type())
fmmfScgPtpPmCmnScgOprMin.setMaxAccess(_C)
if mibBuilder.loadTexts:fmmfScgPtpPmCmnScgOprMin.setStatus(_A)
_FmmfScgPtpPmCmnScgOprMax_Type=FloatHundredths
_FmmfScgPtpPmCmnScgOprMax_Object=MibTableColumn
fmmfScgPtpPmCmnScgOprMax=_FmmfScgPtpPmCmnScgOprMax_Object((1,3,6,1,4,1,21296,2,2,2,3,49,2,1,8),_FmmfScgPtpPmCmnScgOprMax_Type())
fmmfScgPtpPmCmnScgOprMax.setMaxAccess(_C)
if mibBuilder.loadTexts:fmmfScgPtpPmCmnScgOprMax.setStatus(_A)
_FmmfScgPtpPmCmnScgOprAve_Type=FloatHundredths
_FmmfScgPtpPmCmnScgOprAve_Object=MibTableColumn
fmmfScgPtpPmCmnScgOprAve=_FmmfScgPtpPmCmnScgOprAve_Object((1,3,6,1,4,1,21296,2,2,2,3,49,2,1,9),_FmmfScgPtpPmCmnScgOprAve_Type())
fmmfScgPtpPmCmnScgOprAve.setMaxAccess(_C)
if mibBuilder.loadTexts:fmmfScgPtpPmCmnScgOprAve.setStatus(_A)
_FmmfScgPtpPmOptOsaTapRatioMin_Type=FloatHundredths
_FmmfScgPtpPmOptOsaTapRatioMin_Object=MibTableColumn
fmmfScgPtpPmOptOsaTapRatioMin=_FmmfScgPtpPmOptOsaTapRatioMin_Object((1,3,6,1,4,1,21296,2,2,2,3,49,2,1,10),_FmmfScgPtpPmOptOsaTapRatioMin_Type())
fmmfScgPtpPmOptOsaTapRatioMin.setMaxAccess(_C)
if mibBuilder.loadTexts:fmmfScgPtpPmOptOsaTapRatioMin.setStatus(_A)
_FmmfScgPtpPmOptOsaTapRatioMax_Type=FloatHundredths
_FmmfScgPtpPmOptOsaTapRatioMax_Object=MibTableColumn
fmmfScgPtpPmOptOsaTapRatioMax=_FmmfScgPtpPmOptOsaTapRatioMax_Object((1,3,6,1,4,1,21296,2,2,2,3,49,2,1,11),_FmmfScgPtpPmOptOsaTapRatioMax_Type())
fmmfScgPtpPmOptOsaTapRatioMax.setMaxAccess(_C)
if mibBuilder.loadTexts:fmmfScgPtpPmOptOsaTapRatioMax.setStatus(_A)
_FmmfScgPtpPmOptOsaTapRatioAve_Type=FloatHundredths
_FmmfScgPtpPmOptOsaTapRatioAve_Object=MibTableColumn
fmmfScgPtpPmOptOsaTapRatioAve=_FmmfScgPtpPmOptOsaTapRatioAve_Object((1,3,6,1,4,1,21296,2,2,2,3,49,2,1,12),_FmmfScgPtpPmOptOsaTapRatioAve_Type())
fmmfScgPtpPmOptOsaTapRatioAve.setMaxAccess(_C)
if mibBuilder.loadTexts:fmmfScgPtpPmOptOsaTapRatioAve.setStatus(_A)
_FmmfScgPtpPmConformance_ObjectIdentity=ObjectIdentity
fmmfScgPtpPmConformance=_FmmfScgPtpPmConformance_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,3,49,3))
_FmmfScgPtpPmCompliances_ObjectIdentity=ObjectIdentity
fmmfScgPtpPmCompliances=_FmmfScgPtpPmCompliances_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,3,49,3,1))
_FmmfScgPtpPmGroups_ObjectIdentity=ObjectIdentity
fmmfScgPtpPmGroups=_FmmfScgPtpPmGroups_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,3,49,3,2))
fmmfScgPtpPmGroup=ObjectGroup((1,3,6,1,4,1,21296,2,2,2,3,49,3,2,1))
fmmfScgPtpPmGroup.setObjects(*((_B,_H),(_B,_G),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S)))
if mibBuilder.loadTexts:fmmfScgPtpPmGroup.setStatus(_A)
fmmfScgPtpPmRealGroup=ObjectGroup((1,3,6,1,4,1,21296,2,2,2,3,49,3,2,2))
fmmfScgPtpPmRealGroup.setObjects(*((_B,_T),(_B,_U),(_B,_V)))
if mibBuilder.loadTexts:fmmfScgPtpPmRealGroup.setStatus(_A)
fmmfScgPtpPmCompliance=ModuleCompliance((1,3,6,1,4,1,21296,2,2,2,3,49,3,1,1))
fmmfScgPtpPmCompliance.setObjects((_B,_W))
if mibBuilder.loadTexts:fmmfScgPtpPmCompliance.setStatus(_A)
fmmfScgPtpPmRealCompliance=ModuleCompliance((1,3,6,1,4,1,21296,2,2,2,3,49,3,1,2))
fmmfScgPtpPmRealCompliance.setObjects((_B,_X))
if mibBuilder.loadTexts:fmmfScgPtpPmRealCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'fmmfScgPtpPmMIB':fmmfScgPtpPmMIB,'fmmfScgPtpPmRealTable':fmmfScgPtpPmRealTable,'fmmfScgPtpPmRealEntry':fmmfScgPtpPmRealEntry,_T:fmmfScgPtpPmRealCmnScgOpt,_U:fmmfScgPtpPmRealCmnScgOpr,_V:fmmfScgPtpPmRealOptOsaTapRatio,'fmmfScgPtpPmTable':fmmfScgPtpPmTable,'fmmfScgPtpPmEntry':fmmfScgPtpPmEntry,_H:fmmfScgPtpPmTimestamp,_G:fmmfScgPtpPmSampleDuration,_J:fmmfScgPtpPmValidity,_K:fmmfScgPtpPmCmnScgOptMin,_L:fmmfScgPtpPmCmnScgOptMax,_M:fmmfScgPtpPmCmnScgOptAve,_N:fmmfScgPtpPmCmnScgOprMin,_O:fmmfScgPtpPmCmnScgOprMax,_P:fmmfScgPtpPmCmnScgOprAve,_Q:fmmfScgPtpPmOptOsaTapRatioMin,_R:fmmfScgPtpPmOptOsaTapRatioMax,_S:fmmfScgPtpPmOptOsaTapRatioAve,'fmmfScgPtpPmConformance':fmmfScgPtpPmConformance,'fmmfScgPtpPmCompliances':fmmfScgPtpPmCompliances,'fmmfScgPtpPmCompliance':fmmfScgPtpPmCompliance,'fmmfScgPtpPmRealCompliance':fmmfScgPtpPmRealCompliance,'fmmfScgPtpPmGroups':fmmfScgPtpPmGroups,_W:fmmfScgPtpPmGroup,_X:fmmfScgPtpPmRealGroup})