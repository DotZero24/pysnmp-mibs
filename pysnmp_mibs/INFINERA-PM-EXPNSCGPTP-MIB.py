_P='expnScgPtpPmRealGroup'
_O='expnScgPtpPmGroup'
_N='expnScgPtpPmRealCmnScgOpr'
_M='expnScgPtpPmRealCmnScgOpt'
_L='expnScgPtpPmCmnScgOprAve'
_K='expnScgPtpPmCmnScgOprMax'
_J='expnScgPtpPmCmnScgOprMin'
_I='expnScgPtpPmCmnScgOptAve'
_H='expnScgPtpPmCmnScgOptMax'
_G='expnScgPtpPmCmnScgOptMin'
_F='expnScgPtpPmValidity'
_E='ifIndex'
_D='IF-MIB'
_C='read-only'
_B='INFINERA-PM-EXPNSCGPTP-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_D,_E)
perfMon,=mibBuilder.importSymbols('INFINERA-REG-MIB','perfMon')
FloatHundredths,=mibBuilder.importSymbols('INFINERA-TC-MIB','FloatHundredths')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
expnScgPtpPmMIB=ModuleIdentity((1,3,6,1,4,1,21296,2,2,2,3,48))
if mibBuilder.loadTexts:expnScgPtpPmMIB.setRevisions(('2013-10-08 00:00',))
_ExpnScgPtpPmRealTable_Object=MibTable
expnScgPtpPmRealTable=_ExpnScgPtpPmRealTable_Object((1,3,6,1,4,1,21296,2,2,2,3,48,1))
if mibBuilder.loadTexts:expnScgPtpPmRealTable.setStatus(_A)
_ExpnScgPtpPmRealEntry_Object=MibTableRow
expnScgPtpPmRealEntry=_ExpnScgPtpPmRealEntry_Object((1,3,6,1,4,1,21296,2,2,2,3,48,1,1))
expnScgPtpPmRealEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:expnScgPtpPmRealEntry.setStatus(_A)
_ExpnScgPtpPmRealCmnScgOpt_Type=FloatHundredths
_ExpnScgPtpPmRealCmnScgOpt_Object=MibTableColumn
expnScgPtpPmRealCmnScgOpt=_ExpnScgPtpPmRealCmnScgOpt_Object((1,3,6,1,4,1,21296,2,2,2,3,48,1,1,1),_ExpnScgPtpPmRealCmnScgOpt_Type())
expnScgPtpPmRealCmnScgOpt.setMaxAccess(_C)
if mibBuilder.loadTexts:expnScgPtpPmRealCmnScgOpt.setStatus(_A)
_ExpnScgPtpPmRealCmnScgOpr_Type=FloatHundredths
_ExpnScgPtpPmRealCmnScgOpr_Object=MibTableColumn
expnScgPtpPmRealCmnScgOpr=_ExpnScgPtpPmRealCmnScgOpr_Object((1,3,6,1,4,1,21296,2,2,2,3,48,1,1,2),_ExpnScgPtpPmRealCmnScgOpr_Type())
expnScgPtpPmRealCmnScgOpr.setMaxAccess(_C)
if mibBuilder.loadTexts:expnScgPtpPmRealCmnScgOpr.setStatus(_A)
_ExpnScgPtpPmTable_Object=MibTable
expnScgPtpPmTable=_ExpnScgPtpPmTable_Object((1,3,6,1,4,1,21296,2,2,2,3,48,2))
if mibBuilder.loadTexts:expnScgPtpPmTable.setStatus(_A)
_ExpnScgPtpPmEntry_Object=MibTableRow
expnScgPtpPmEntry=_ExpnScgPtpPmEntry_Object((1,3,6,1,4,1,21296,2,2,2,3,48,2,1))
expnScgPtpPmEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:expnScgPtpPmEntry.setStatus(_A)
_ExpnScgPtpPmValidity_Type=TruthValue
_ExpnScgPtpPmValidity_Object=MibTableColumn
expnScgPtpPmValidity=_ExpnScgPtpPmValidity_Object((1,3,6,1,4,1,21296,2,2,2,3,48,2,1,3),_ExpnScgPtpPmValidity_Type())
expnScgPtpPmValidity.setMaxAccess(_C)
if mibBuilder.loadTexts:expnScgPtpPmValidity.setStatus(_A)
_ExpnScgPtpPmCmnScgOptMin_Type=FloatHundredths
_ExpnScgPtpPmCmnScgOptMin_Object=MibTableColumn
expnScgPtpPmCmnScgOptMin=_ExpnScgPtpPmCmnScgOptMin_Object((1,3,6,1,4,1,21296,2,2,2,3,48,2,1,4),_ExpnScgPtpPmCmnScgOptMin_Type())
expnScgPtpPmCmnScgOptMin.setMaxAccess(_C)
if mibBuilder.loadTexts:expnScgPtpPmCmnScgOptMin.setStatus(_A)
_ExpnScgPtpPmCmnScgOptMax_Type=FloatHundredths
_ExpnScgPtpPmCmnScgOptMax_Object=MibTableColumn
expnScgPtpPmCmnScgOptMax=_ExpnScgPtpPmCmnScgOptMax_Object((1,3,6,1,4,1,21296,2,2,2,3,48,2,1,5),_ExpnScgPtpPmCmnScgOptMax_Type())
expnScgPtpPmCmnScgOptMax.setMaxAccess(_C)
if mibBuilder.loadTexts:expnScgPtpPmCmnScgOptMax.setStatus(_A)
_ExpnScgPtpPmCmnScgOptAve_Type=FloatHundredths
_ExpnScgPtpPmCmnScgOptAve_Object=MibTableColumn
expnScgPtpPmCmnScgOptAve=_ExpnScgPtpPmCmnScgOptAve_Object((1,3,6,1,4,1,21296,2,2,2,3,48,2,1,6),_ExpnScgPtpPmCmnScgOptAve_Type())
expnScgPtpPmCmnScgOptAve.setMaxAccess(_C)
if mibBuilder.loadTexts:expnScgPtpPmCmnScgOptAve.setStatus(_A)
_ExpnScgPtpPmCmnScgOprMin_Type=FloatHundredths
_ExpnScgPtpPmCmnScgOprMin_Object=MibTableColumn
expnScgPtpPmCmnScgOprMin=_ExpnScgPtpPmCmnScgOprMin_Object((1,3,6,1,4,1,21296,2,2,2,3,48,2,1,7),_ExpnScgPtpPmCmnScgOprMin_Type())
expnScgPtpPmCmnScgOprMin.setMaxAccess(_C)
if mibBuilder.loadTexts:expnScgPtpPmCmnScgOprMin.setStatus(_A)
_ExpnScgPtpPmCmnScgOprMax_Type=FloatHundredths
_ExpnScgPtpPmCmnScgOprMax_Object=MibTableColumn
expnScgPtpPmCmnScgOprMax=_ExpnScgPtpPmCmnScgOprMax_Object((1,3,6,1,4,1,21296,2,2,2,3,48,2,1,8),_ExpnScgPtpPmCmnScgOprMax_Type())
expnScgPtpPmCmnScgOprMax.setMaxAccess(_C)
if mibBuilder.loadTexts:expnScgPtpPmCmnScgOprMax.setStatus(_A)
_ExpnScgPtpPmCmnScgOprAve_Type=FloatHundredths
_ExpnScgPtpPmCmnScgOprAve_Object=MibTableColumn
expnScgPtpPmCmnScgOprAve=_ExpnScgPtpPmCmnScgOprAve_Object((1,3,6,1,4,1,21296,2,2,2,3,48,2,1,9),_ExpnScgPtpPmCmnScgOprAve_Type())
expnScgPtpPmCmnScgOprAve.setMaxAccess(_C)
if mibBuilder.loadTexts:expnScgPtpPmCmnScgOprAve.setStatus(_A)
_ExpnScgPtpPmConformance_ObjectIdentity=ObjectIdentity
expnScgPtpPmConformance=_ExpnScgPtpPmConformance_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,3,48,3))
_ExpnScgPtpPmCompliances_ObjectIdentity=ObjectIdentity
expnScgPtpPmCompliances=_ExpnScgPtpPmCompliances_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,3,48,3,1))
_ExpnScgPtpPmGroups_ObjectIdentity=ObjectIdentity
expnScgPtpPmGroups=_ExpnScgPtpPmGroups_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,3,48,3,2))
expnScgPtpPmGroup=ObjectGroup((1,3,6,1,4,1,21296,2,2,2,3,48,3,2,1))
expnScgPtpPmGroup.setObjects(*((_B,_F),(_B,_G),(_B,_H),(_B,_I),(_B,_J),(_B,_K),(_B,_L)))
if mibBuilder.loadTexts:expnScgPtpPmGroup.setStatus(_A)
expnScgPtpPmRealGroup=ObjectGroup((1,3,6,1,4,1,21296,2,2,2,3,48,3,2,2))
expnScgPtpPmRealGroup.setObjects(*((_B,_M),(_B,_N)))
if mibBuilder.loadTexts:expnScgPtpPmRealGroup.setStatus(_A)
expnScgPtpPmCompliance=ModuleCompliance((1,3,6,1,4,1,21296,2,2,2,3,48,3,1,1))
expnScgPtpPmCompliance.setObjects((_B,_O))
if mibBuilder.loadTexts:expnScgPtpPmCompliance.setStatus(_A)
expnScgPtpPmRealCompliance=ModuleCompliance((1,3,6,1,4,1,21296,2,2,2,3,48,3,1,2))
expnScgPtpPmRealCompliance.setObjects((_B,_P))
if mibBuilder.loadTexts:expnScgPtpPmRealCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'expnScgPtpPmMIB':expnScgPtpPmMIB,'expnScgPtpPmRealTable':expnScgPtpPmRealTable,'expnScgPtpPmRealEntry':expnScgPtpPmRealEntry,_M:expnScgPtpPmRealCmnScgOpt,_N:expnScgPtpPmRealCmnScgOpr,'expnScgPtpPmTable':expnScgPtpPmTable,'expnScgPtpPmEntry':expnScgPtpPmEntry,_F:expnScgPtpPmValidity,_G:expnScgPtpPmCmnScgOptMin,_H:expnScgPtpPmCmnScgOptMax,_I:expnScgPtpPmCmnScgOptAve,_J:expnScgPtpPmCmnScgOprMin,_K:expnScgPtpPmCmnScgOprMax,_L:expnScgPtpPmCmnScgOprAve,'expnScgPtpPmConformance':expnScgPtpPmConformance,'expnScgPtpPmCompliances':expnScgPtpPmCompliances,'expnScgPtpPmCompliance':expnScgPtpPmCompliance,'expnScgPtpPmRealCompliance':expnScgPtpPmRealCompliance,'expnScgPtpPmGroups':expnScgPtpPmGroups,_O:expnScgPtpPmGroup,_P:expnScgPtpPmRealGroup})