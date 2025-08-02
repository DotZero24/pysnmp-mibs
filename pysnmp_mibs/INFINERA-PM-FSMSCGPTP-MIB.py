_T='fsmScgPtpPmRealGroup'
_S='fsmScgPtpPmGroup'
_R='fsmScgPtpPmRealCmnScgOpr'
_Q='fsmScgPtpPmRealCmnScgOpt'
_P='fsmScgPtpPmCmnScgOprAve'
_O='fsmScgPtpPmCmnScgOprMax'
_N='fsmScgPtpPmCmnScgOprMin'
_M='fsmScgPtpPmCmnScgOptAve'
_L='fsmScgPtpPmCmnScgOptMax'
_K='fsmScgPtpPmCmnScgOptMin'
_J='fsmScgPtpPmValidity'
_I='not-accessible'
_H='Integer32'
_G='fsmScgPtpPmTimestamp'
_F='fsmScgPtpPmSampleDuration'
_E='ifIndex'
_D='IF-MIB'
_C='read-only'
_B='INFINERA-PM-FSMSCGPTP-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_D,_E)
perfMon,=mibBuilder.importSymbols('INFINERA-REG-MIB','perfMon')
FloatHundredths,InfnSampleDuration=mibBuilder.importSymbols('INFINERA-TC-MIB','FloatHundredths','InfnSampleDuration')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_H,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
fsmScgPtpPmMIB=ModuleIdentity((1,3,6,1,4,1,21296,2,2,2,3,40))
if mibBuilder.loadTexts:fsmScgPtpPmMIB.setRevisions(('2013-10-08 00:00',))
_FsmScgPtpPmRealTable_Object=MibTable
fsmScgPtpPmRealTable=_FsmScgPtpPmRealTable_Object((1,3,6,1,4,1,21296,2,2,2,3,40,1))
if mibBuilder.loadTexts:fsmScgPtpPmRealTable.setStatus(_A)
_FsmScgPtpPmRealEntry_Object=MibTableRow
fsmScgPtpPmRealEntry=_FsmScgPtpPmRealEntry_Object((1,3,6,1,4,1,21296,2,2,2,3,40,1,1))
fsmScgPtpPmRealEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:fsmScgPtpPmRealEntry.setStatus(_A)
_FsmScgPtpPmRealCmnScgOpt_Type=FloatHundredths
_FsmScgPtpPmRealCmnScgOpt_Object=MibTableColumn
fsmScgPtpPmRealCmnScgOpt=_FsmScgPtpPmRealCmnScgOpt_Object((1,3,6,1,4,1,21296,2,2,2,3,40,1,1,1),_FsmScgPtpPmRealCmnScgOpt_Type())
fsmScgPtpPmRealCmnScgOpt.setMaxAccess(_C)
if mibBuilder.loadTexts:fsmScgPtpPmRealCmnScgOpt.setStatus(_A)
_FsmScgPtpPmRealCmnScgOpr_Type=FloatHundredths
_FsmScgPtpPmRealCmnScgOpr_Object=MibTableColumn
fsmScgPtpPmRealCmnScgOpr=_FsmScgPtpPmRealCmnScgOpr_Object((1,3,6,1,4,1,21296,2,2,2,3,40,1,1,2),_FsmScgPtpPmRealCmnScgOpr_Type())
fsmScgPtpPmRealCmnScgOpr.setMaxAccess(_C)
if mibBuilder.loadTexts:fsmScgPtpPmRealCmnScgOpr.setStatus(_A)
_FsmScgPtpPmTable_Object=MibTable
fsmScgPtpPmTable=_FsmScgPtpPmTable_Object((1,3,6,1,4,1,21296,2,2,2,3,40,2))
if mibBuilder.loadTexts:fsmScgPtpPmTable.setStatus(_A)
_FsmScgPtpPmEntry_Object=MibTableRow
fsmScgPtpPmEntry=_FsmScgPtpPmEntry_Object((1,3,6,1,4,1,21296,2,2,2,3,40,2,1))
fsmScgPtpPmEntry.setIndexNames((0,_D,_E),(0,_B,_F),(0,_B,_G))
if mibBuilder.loadTexts:fsmScgPtpPmEntry.setStatus(_A)
class _FsmScgPtpPmTimestamp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_FsmScgPtpPmTimestamp_Type.__name__=_H
_FsmScgPtpPmTimestamp_Object=MibTableColumn
fsmScgPtpPmTimestamp=_FsmScgPtpPmTimestamp_Object((1,3,6,1,4,1,21296,2,2,2,3,40,2,1,1),_FsmScgPtpPmTimestamp_Type())
fsmScgPtpPmTimestamp.setMaxAccess(_I)
if mibBuilder.loadTexts:fsmScgPtpPmTimestamp.setStatus(_A)
_FsmScgPtpPmSampleDuration_Type=InfnSampleDuration
_FsmScgPtpPmSampleDuration_Object=MibTableColumn
fsmScgPtpPmSampleDuration=_FsmScgPtpPmSampleDuration_Object((1,3,6,1,4,1,21296,2,2,2,3,40,2,1,2),_FsmScgPtpPmSampleDuration_Type())
fsmScgPtpPmSampleDuration.setMaxAccess(_I)
if mibBuilder.loadTexts:fsmScgPtpPmSampleDuration.setStatus(_A)
_FsmScgPtpPmValidity_Type=TruthValue
_FsmScgPtpPmValidity_Object=MibTableColumn
fsmScgPtpPmValidity=_FsmScgPtpPmValidity_Object((1,3,6,1,4,1,21296,2,2,2,3,40,2,1,3),_FsmScgPtpPmValidity_Type())
fsmScgPtpPmValidity.setMaxAccess(_C)
if mibBuilder.loadTexts:fsmScgPtpPmValidity.setStatus(_A)
_FsmScgPtpPmCmnScgOptMin_Type=FloatHundredths
_FsmScgPtpPmCmnScgOptMin_Object=MibTableColumn
fsmScgPtpPmCmnScgOptMin=_FsmScgPtpPmCmnScgOptMin_Object((1,3,6,1,4,1,21296,2,2,2,3,40,2,1,4),_FsmScgPtpPmCmnScgOptMin_Type())
fsmScgPtpPmCmnScgOptMin.setMaxAccess(_C)
if mibBuilder.loadTexts:fsmScgPtpPmCmnScgOptMin.setStatus(_A)
_FsmScgPtpPmCmnScgOptMax_Type=FloatHundredths
_FsmScgPtpPmCmnScgOptMax_Object=MibTableColumn
fsmScgPtpPmCmnScgOptMax=_FsmScgPtpPmCmnScgOptMax_Object((1,3,6,1,4,1,21296,2,2,2,3,40,2,1,5),_FsmScgPtpPmCmnScgOptMax_Type())
fsmScgPtpPmCmnScgOptMax.setMaxAccess(_C)
if mibBuilder.loadTexts:fsmScgPtpPmCmnScgOptMax.setStatus(_A)
_FsmScgPtpPmCmnScgOptAve_Type=FloatHundredths
_FsmScgPtpPmCmnScgOptAve_Object=MibTableColumn
fsmScgPtpPmCmnScgOptAve=_FsmScgPtpPmCmnScgOptAve_Object((1,3,6,1,4,1,21296,2,2,2,3,40,2,1,6),_FsmScgPtpPmCmnScgOptAve_Type())
fsmScgPtpPmCmnScgOptAve.setMaxAccess(_C)
if mibBuilder.loadTexts:fsmScgPtpPmCmnScgOptAve.setStatus(_A)
_FsmScgPtpPmCmnScgOprMin_Type=FloatHundredths
_FsmScgPtpPmCmnScgOprMin_Object=MibTableColumn
fsmScgPtpPmCmnScgOprMin=_FsmScgPtpPmCmnScgOprMin_Object((1,3,6,1,4,1,21296,2,2,2,3,40,2,1,7),_FsmScgPtpPmCmnScgOprMin_Type())
fsmScgPtpPmCmnScgOprMin.setMaxAccess(_C)
if mibBuilder.loadTexts:fsmScgPtpPmCmnScgOprMin.setStatus(_A)
_FsmScgPtpPmCmnScgOprMax_Type=FloatHundredths
_FsmScgPtpPmCmnScgOprMax_Object=MibTableColumn
fsmScgPtpPmCmnScgOprMax=_FsmScgPtpPmCmnScgOprMax_Object((1,3,6,1,4,1,21296,2,2,2,3,40,2,1,8),_FsmScgPtpPmCmnScgOprMax_Type())
fsmScgPtpPmCmnScgOprMax.setMaxAccess(_C)
if mibBuilder.loadTexts:fsmScgPtpPmCmnScgOprMax.setStatus(_A)
_FsmScgPtpPmCmnScgOprAve_Type=FloatHundredths
_FsmScgPtpPmCmnScgOprAve_Object=MibTableColumn
fsmScgPtpPmCmnScgOprAve=_FsmScgPtpPmCmnScgOprAve_Object((1,3,6,1,4,1,21296,2,2,2,3,40,2,1,9),_FsmScgPtpPmCmnScgOprAve_Type())
fsmScgPtpPmCmnScgOprAve.setMaxAccess(_C)
if mibBuilder.loadTexts:fsmScgPtpPmCmnScgOprAve.setStatus(_A)
_FsmScgPtpPmConformance_ObjectIdentity=ObjectIdentity
fsmScgPtpPmConformance=_FsmScgPtpPmConformance_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,3,40,3))
_FsmScgPtpPmCompliances_ObjectIdentity=ObjectIdentity
fsmScgPtpPmCompliances=_FsmScgPtpPmCompliances_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,3,40,3,1))
_FsmScgPtpPmGroups_ObjectIdentity=ObjectIdentity
fsmScgPtpPmGroups=_FsmScgPtpPmGroups_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,3,40,3,2))
fsmScgPtpPmGroup=ObjectGroup((1,3,6,1,4,1,21296,2,2,2,3,40,3,2,1))
fsmScgPtpPmGroup.setObjects(*((_B,_G),(_B,_F),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P)))
if mibBuilder.loadTexts:fsmScgPtpPmGroup.setStatus(_A)
fsmScgPtpPmRealGroup=ObjectGroup((1,3,6,1,4,1,21296,2,2,2,3,40,3,2,2))
fsmScgPtpPmRealGroup.setObjects(*((_B,_Q),(_B,_R)))
if mibBuilder.loadTexts:fsmScgPtpPmRealGroup.setStatus(_A)
fsmScgPtpPmCompliance=ModuleCompliance((1,3,6,1,4,1,21296,2,2,2,3,40,3,1,1))
fsmScgPtpPmCompliance.setObjects((_B,_S))
if mibBuilder.loadTexts:fsmScgPtpPmCompliance.setStatus(_A)
fsmScgPtpPmRealCompliance=ModuleCompliance((1,3,6,1,4,1,21296,2,2,2,3,40,3,1,2))
fsmScgPtpPmRealCompliance.setObjects((_B,_T))
if mibBuilder.loadTexts:fsmScgPtpPmRealCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'fsmScgPtpPmMIB':fsmScgPtpPmMIB,'fsmScgPtpPmRealTable':fsmScgPtpPmRealTable,'fsmScgPtpPmRealEntry':fsmScgPtpPmRealEntry,_Q:fsmScgPtpPmRealCmnScgOpt,_R:fsmScgPtpPmRealCmnScgOpr,'fsmScgPtpPmTable':fsmScgPtpPmTable,'fsmScgPtpPmEntry':fsmScgPtpPmEntry,_G:fsmScgPtpPmTimestamp,_F:fsmScgPtpPmSampleDuration,_J:fsmScgPtpPmValidity,_K:fsmScgPtpPmCmnScgOptMin,_L:fsmScgPtpPmCmnScgOptMax,_M:fsmScgPtpPmCmnScgOptAve,_N:fsmScgPtpPmCmnScgOprMin,_O:fsmScgPtpPmCmnScgOprMax,_P:fsmScgPtpPmCmnScgOprAve,'fsmScgPtpPmConformance':fsmScgPtpPmConformance,'fsmScgPtpPmCompliances':fsmScgPtpPmCompliances,'fsmScgPtpPmCompliance':fsmScgPtpPmCompliance,'fsmScgPtpPmRealCompliance':fsmScgPtpPmRealCompliance,'fsmScgPtpPmGroups':fsmScgPtpPmGroups,_S:fsmScgPtpPmGroup,_T:fsmScgPtpPmRealGroup})