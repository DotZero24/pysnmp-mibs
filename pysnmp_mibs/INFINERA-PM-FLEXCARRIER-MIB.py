_V='flexCarrierPmRealGroup'
_U='flexCarrierPmGroup'
_T='flexCarrierPmRealLastPollTimeStampOpr'
_S='flexCarrierPmRealLastPollTimeStampOpt'
_R='flexCarrierPmRealCmnScgOpr'
_Q='flexCarrierPmRealCmnScgOpt'
_P='flexCarrierPmCmnScgOprAve'
_O='flexCarrierPmCmnScgOprMax'
_N='flexCarrierPmCmnScgOprMin'
_M='flexCarrierPmCmnScgOptAve'
_L='flexCarrierPmCmnScgOptMax'
_K='flexCarrierPmCmnScgOptMin'
_J='flexCarrierPmValidity'
_I='not-accessible'
_H='flexCarrierPmTimestamp'
_G='flexCarrierPmSampleDuration'
_F='Integer32'
_E='ifIndex'
_D='IF-MIB'
_C='read-only'
_B='INFINERA-PM-FLEXCARRIER-MIB'
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
flexCarrierPmMIB=ModuleIdentity((1,3,6,1,4,1,21296,2,2,2,3,60))
if mibBuilder.loadTexts:flexCarrierPmMIB.setRevisions(('2015-04-18 00:00',))
_FlexCarrierPmRealTable_Object=MibTable
flexCarrierPmRealTable=_FlexCarrierPmRealTable_Object((1,3,6,1,4,1,21296,2,2,2,3,60,1))
if mibBuilder.loadTexts:flexCarrierPmRealTable.setStatus(_A)
_FlexCarrierPmRealEntry_Object=MibTableRow
flexCarrierPmRealEntry=_FlexCarrierPmRealEntry_Object((1,3,6,1,4,1,21296,2,2,2,3,60,1,1))
flexCarrierPmRealEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:flexCarrierPmRealEntry.setStatus(_A)
_FlexCarrierPmRealCmnScgOpt_Type=FloatHundredths
_FlexCarrierPmRealCmnScgOpt_Object=MibTableColumn
flexCarrierPmRealCmnScgOpt=_FlexCarrierPmRealCmnScgOpt_Object((1,3,6,1,4,1,21296,2,2,2,3,60,1,1,1),_FlexCarrierPmRealCmnScgOpt_Type())
flexCarrierPmRealCmnScgOpt.setMaxAccess(_C)
if mibBuilder.loadTexts:flexCarrierPmRealCmnScgOpt.setStatus(_A)
_FlexCarrierPmRealCmnScgOpr_Type=FloatHundredths
_FlexCarrierPmRealCmnScgOpr_Object=MibTableColumn
flexCarrierPmRealCmnScgOpr=_FlexCarrierPmRealCmnScgOpr_Object((1,3,6,1,4,1,21296,2,2,2,3,60,1,1,2),_FlexCarrierPmRealCmnScgOpr_Type())
flexCarrierPmRealCmnScgOpr.setMaxAccess(_C)
if mibBuilder.loadTexts:flexCarrierPmRealCmnScgOpr.setStatus(_A)
_FlexCarrierPmRealLastPollTimeStampOpt_Type=Integer32
_FlexCarrierPmRealLastPollTimeStampOpt_Object=MibTableColumn
flexCarrierPmRealLastPollTimeStampOpt=_FlexCarrierPmRealLastPollTimeStampOpt_Object((1,3,6,1,4,1,21296,2,2,2,3,60,1,1,3),_FlexCarrierPmRealLastPollTimeStampOpt_Type())
flexCarrierPmRealLastPollTimeStampOpt.setMaxAccess(_C)
if mibBuilder.loadTexts:flexCarrierPmRealLastPollTimeStampOpt.setStatus(_A)
_FlexCarrierPmRealLastPollTimeStampOpr_Type=Integer32
_FlexCarrierPmRealLastPollTimeStampOpr_Object=MibTableColumn
flexCarrierPmRealLastPollTimeStampOpr=_FlexCarrierPmRealLastPollTimeStampOpr_Object((1,3,6,1,4,1,21296,2,2,2,3,60,1,1,4),_FlexCarrierPmRealLastPollTimeStampOpr_Type())
flexCarrierPmRealLastPollTimeStampOpr.setMaxAccess(_C)
if mibBuilder.loadTexts:flexCarrierPmRealLastPollTimeStampOpr.setStatus(_A)
_FlexCarrierPmTable_Object=MibTable
flexCarrierPmTable=_FlexCarrierPmTable_Object((1,3,6,1,4,1,21296,2,2,2,3,60,2))
if mibBuilder.loadTexts:flexCarrierPmTable.setStatus(_A)
_FlexCarrierPmEntry_Object=MibTableRow
flexCarrierPmEntry=_FlexCarrierPmEntry_Object((1,3,6,1,4,1,21296,2,2,2,3,60,2,1))
flexCarrierPmEntry.setIndexNames((0,_D,_E),(0,_B,_G),(0,_B,_H))
if mibBuilder.loadTexts:flexCarrierPmEntry.setStatus(_A)
class _FlexCarrierPmTimestamp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_FlexCarrierPmTimestamp_Type.__name__=_F
_FlexCarrierPmTimestamp_Object=MibTableColumn
flexCarrierPmTimestamp=_FlexCarrierPmTimestamp_Object((1,3,6,1,4,1,21296,2,2,2,3,60,2,1,1),_FlexCarrierPmTimestamp_Type())
flexCarrierPmTimestamp.setMaxAccess(_I)
if mibBuilder.loadTexts:flexCarrierPmTimestamp.setStatus(_A)
class _FlexCarrierPmSampleDuration_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('fifteenMinutes',1),('day',2)))
_FlexCarrierPmSampleDuration_Type.__name__=_F
_FlexCarrierPmSampleDuration_Object=MibTableColumn
flexCarrierPmSampleDuration=_FlexCarrierPmSampleDuration_Object((1,3,6,1,4,1,21296,2,2,2,3,60,2,1,2),_FlexCarrierPmSampleDuration_Type())
flexCarrierPmSampleDuration.setMaxAccess(_I)
if mibBuilder.loadTexts:flexCarrierPmSampleDuration.setStatus(_A)
_FlexCarrierPmValidity_Type=TruthValue
_FlexCarrierPmValidity_Object=MibTableColumn
flexCarrierPmValidity=_FlexCarrierPmValidity_Object((1,3,6,1,4,1,21296,2,2,2,3,60,2,1,3),_FlexCarrierPmValidity_Type())
flexCarrierPmValidity.setMaxAccess(_C)
if mibBuilder.loadTexts:flexCarrierPmValidity.setStatus(_A)
_FlexCarrierPmCmnScgOptMin_Type=FloatHundredths
_FlexCarrierPmCmnScgOptMin_Object=MibTableColumn
flexCarrierPmCmnScgOptMin=_FlexCarrierPmCmnScgOptMin_Object((1,3,6,1,4,1,21296,2,2,2,3,60,2,1,4),_FlexCarrierPmCmnScgOptMin_Type())
flexCarrierPmCmnScgOptMin.setMaxAccess(_C)
if mibBuilder.loadTexts:flexCarrierPmCmnScgOptMin.setStatus(_A)
_FlexCarrierPmCmnScgOptMax_Type=FloatHundredths
_FlexCarrierPmCmnScgOptMax_Object=MibTableColumn
flexCarrierPmCmnScgOptMax=_FlexCarrierPmCmnScgOptMax_Object((1,3,6,1,4,1,21296,2,2,2,3,60,2,1,5),_FlexCarrierPmCmnScgOptMax_Type())
flexCarrierPmCmnScgOptMax.setMaxAccess(_C)
if mibBuilder.loadTexts:flexCarrierPmCmnScgOptMax.setStatus(_A)
_FlexCarrierPmCmnScgOptAve_Type=FloatHundredths
_FlexCarrierPmCmnScgOptAve_Object=MibTableColumn
flexCarrierPmCmnScgOptAve=_FlexCarrierPmCmnScgOptAve_Object((1,3,6,1,4,1,21296,2,2,2,3,60,2,1,6),_FlexCarrierPmCmnScgOptAve_Type())
flexCarrierPmCmnScgOptAve.setMaxAccess(_C)
if mibBuilder.loadTexts:flexCarrierPmCmnScgOptAve.setStatus(_A)
_FlexCarrierPmCmnScgOprMin_Type=FloatHundredths
_FlexCarrierPmCmnScgOprMin_Object=MibTableColumn
flexCarrierPmCmnScgOprMin=_FlexCarrierPmCmnScgOprMin_Object((1,3,6,1,4,1,21296,2,2,2,3,60,2,1,7),_FlexCarrierPmCmnScgOprMin_Type())
flexCarrierPmCmnScgOprMin.setMaxAccess(_C)
if mibBuilder.loadTexts:flexCarrierPmCmnScgOprMin.setStatus(_A)
_FlexCarrierPmCmnScgOprMax_Type=FloatHundredths
_FlexCarrierPmCmnScgOprMax_Object=MibTableColumn
flexCarrierPmCmnScgOprMax=_FlexCarrierPmCmnScgOprMax_Object((1,3,6,1,4,1,21296,2,2,2,3,60,2,1,8),_FlexCarrierPmCmnScgOprMax_Type())
flexCarrierPmCmnScgOprMax.setMaxAccess(_C)
if mibBuilder.loadTexts:flexCarrierPmCmnScgOprMax.setStatus(_A)
_FlexCarrierPmCmnScgOprAve_Type=FloatHundredths
_FlexCarrierPmCmnScgOprAve_Object=MibTableColumn
flexCarrierPmCmnScgOprAve=_FlexCarrierPmCmnScgOprAve_Object((1,3,6,1,4,1,21296,2,2,2,3,60,2,1,9),_FlexCarrierPmCmnScgOprAve_Type())
flexCarrierPmCmnScgOprAve.setMaxAccess(_C)
if mibBuilder.loadTexts:flexCarrierPmCmnScgOprAve.setStatus(_A)
_FlexCarrierPmConformance_ObjectIdentity=ObjectIdentity
flexCarrierPmConformance=_FlexCarrierPmConformance_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,3,60,3))
_FlexCarrierPmCompliances_ObjectIdentity=ObjectIdentity
flexCarrierPmCompliances=_FlexCarrierPmCompliances_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,3,60,3,1))
_FlexCarrierPmGroups_ObjectIdentity=ObjectIdentity
flexCarrierPmGroups=_FlexCarrierPmGroups_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,3,60,3,2))
flexCarrierPmGroup=ObjectGroup((1,3,6,1,4,1,21296,2,2,2,3,60,3,2,1))
flexCarrierPmGroup.setObjects(*((_B,_H),(_B,_G),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P)))
if mibBuilder.loadTexts:flexCarrierPmGroup.setStatus(_A)
flexCarrierPmRealGroup=ObjectGroup((1,3,6,1,4,1,21296,2,2,2,3,60,3,2,2))
flexCarrierPmRealGroup.setObjects(*((_B,_Q),(_B,_R),(_B,_S),(_B,_T)))
if mibBuilder.loadTexts:flexCarrierPmRealGroup.setStatus(_A)
flexCarrierPmCompliance=ModuleCompliance((1,3,6,1,4,1,21296,2,2,2,3,60,3,1,1))
flexCarrierPmCompliance.setObjects((_B,_U))
if mibBuilder.loadTexts:flexCarrierPmCompliance.setStatus(_A)
flexCarrierPmRealCompliance=ModuleCompliance((1,3,6,1,4,1,21296,2,2,2,3,60,3,1,2))
flexCarrierPmRealCompliance.setObjects((_B,_V))
if mibBuilder.loadTexts:flexCarrierPmRealCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'flexCarrierPmMIB':flexCarrierPmMIB,'flexCarrierPmRealTable':flexCarrierPmRealTable,'flexCarrierPmRealEntry':flexCarrierPmRealEntry,_Q:flexCarrierPmRealCmnScgOpt,_R:flexCarrierPmRealCmnScgOpr,_S:flexCarrierPmRealLastPollTimeStampOpt,_T:flexCarrierPmRealLastPollTimeStampOpr,'flexCarrierPmTable':flexCarrierPmTable,'flexCarrierPmEntry':flexCarrierPmEntry,_H:flexCarrierPmTimestamp,_G:flexCarrierPmSampleDuration,_J:flexCarrierPmValidity,_K:flexCarrierPmCmnScgOptMin,_L:flexCarrierPmCmnScgOptMax,_M:flexCarrierPmCmnScgOptAve,_N:flexCarrierPmCmnScgOprMin,_O:flexCarrierPmCmnScgOprMax,_P:flexCarrierPmCmnScgOprAve,'flexCarrierPmConformance':flexCarrierPmConformance,'flexCarrierPmCompliances':flexCarrierPmCompliances,'flexCarrierPmCompliance':flexCarrierPmCompliance,'flexCarrierPmRealCompliance':flexCarrierPmRealCompliance,'flexCarrierPmGroups':flexCarrierPmGroups,_U:flexCarrierPmGroup,_V:flexCarrierPmRealGroup})