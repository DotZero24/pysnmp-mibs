_P='baseScgPtpPmRealGroup'
_O='baseScgPtpPmGroup'
_N='baseScgPtpPmRealCmnScgOpr'
_M='baseScgPtpPmRealCmnScgOpt'
_L='baseScgPtpPmCmnScgOprAve'
_K='baseScgPtpPmCmnScgOprMax'
_J='baseScgPtpPmCmnScgOprMin'
_I='baseScgPtpPmCmnScgOptAve'
_H='baseScgPtpPmCmnScgOptMax'
_G='baseScgPtpPmCmnScgOptMin'
_F='baseScgPtpPmValidity'
_E='ifIndex'
_D='IF-MIB'
_C='read-only'
_B='INFINERA-PM-BASESCGPTP-MIB'
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
baseScgPtpPmMIB=ModuleIdentity((1,3,6,1,4,1,21296,2,2,2,3,45))
if mibBuilder.loadTexts:baseScgPtpPmMIB.setRevisions(('2013-10-08 00:00',))
_BaseScgPtpPmRealTable_Object=MibTable
baseScgPtpPmRealTable=_BaseScgPtpPmRealTable_Object((1,3,6,1,4,1,21296,2,2,2,3,45,1))
if mibBuilder.loadTexts:baseScgPtpPmRealTable.setStatus(_A)
_BaseScgPtpPmRealEntry_Object=MibTableRow
baseScgPtpPmRealEntry=_BaseScgPtpPmRealEntry_Object((1,3,6,1,4,1,21296,2,2,2,3,45,1,1))
baseScgPtpPmRealEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:baseScgPtpPmRealEntry.setStatus(_A)
_BaseScgPtpPmRealCmnScgOpt_Type=FloatHundredths
_BaseScgPtpPmRealCmnScgOpt_Object=MibTableColumn
baseScgPtpPmRealCmnScgOpt=_BaseScgPtpPmRealCmnScgOpt_Object((1,3,6,1,4,1,21296,2,2,2,3,45,1,1,1),_BaseScgPtpPmRealCmnScgOpt_Type())
baseScgPtpPmRealCmnScgOpt.setMaxAccess(_C)
if mibBuilder.loadTexts:baseScgPtpPmRealCmnScgOpt.setStatus(_A)
_BaseScgPtpPmRealCmnScgOpr_Type=FloatHundredths
_BaseScgPtpPmRealCmnScgOpr_Object=MibTableColumn
baseScgPtpPmRealCmnScgOpr=_BaseScgPtpPmRealCmnScgOpr_Object((1,3,6,1,4,1,21296,2,2,2,3,45,1,1,2),_BaseScgPtpPmRealCmnScgOpr_Type())
baseScgPtpPmRealCmnScgOpr.setMaxAccess(_C)
if mibBuilder.loadTexts:baseScgPtpPmRealCmnScgOpr.setStatus(_A)
_BaseScgPtpPmTable_Object=MibTable
baseScgPtpPmTable=_BaseScgPtpPmTable_Object((1,3,6,1,4,1,21296,2,2,2,3,45,2))
if mibBuilder.loadTexts:baseScgPtpPmTable.setStatus(_A)
_BaseScgPtpPmEntry_Object=MibTableRow
baseScgPtpPmEntry=_BaseScgPtpPmEntry_Object((1,3,6,1,4,1,21296,2,2,2,3,45,2,1))
baseScgPtpPmEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:baseScgPtpPmEntry.setStatus(_A)
_BaseScgPtpPmValidity_Type=TruthValue
_BaseScgPtpPmValidity_Object=MibTableColumn
baseScgPtpPmValidity=_BaseScgPtpPmValidity_Object((1,3,6,1,4,1,21296,2,2,2,3,45,2,1,3),_BaseScgPtpPmValidity_Type())
baseScgPtpPmValidity.setMaxAccess(_C)
if mibBuilder.loadTexts:baseScgPtpPmValidity.setStatus(_A)
_BaseScgPtpPmCmnScgOptMin_Type=FloatHundredths
_BaseScgPtpPmCmnScgOptMin_Object=MibTableColumn
baseScgPtpPmCmnScgOptMin=_BaseScgPtpPmCmnScgOptMin_Object((1,3,6,1,4,1,21296,2,2,2,3,45,2,1,4),_BaseScgPtpPmCmnScgOptMin_Type())
baseScgPtpPmCmnScgOptMin.setMaxAccess(_C)
if mibBuilder.loadTexts:baseScgPtpPmCmnScgOptMin.setStatus(_A)
_BaseScgPtpPmCmnScgOptMax_Type=FloatHundredths
_BaseScgPtpPmCmnScgOptMax_Object=MibTableColumn
baseScgPtpPmCmnScgOptMax=_BaseScgPtpPmCmnScgOptMax_Object((1,3,6,1,4,1,21296,2,2,2,3,45,2,1,5),_BaseScgPtpPmCmnScgOptMax_Type())
baseScgPtpPmCmnScgOptMax.setMaxAccess(_C)
if mibBuilder.loadTexts:baseScgPtpPmCmnScgOptMax.setStatus(_A)
_BaseScgPtpPmCmnScgOptAve_Type=FloatHundredths
_BaseScgPtpPmCmnScgOptAve_Object=MibTableColumn
baseScgPtpPmCmnScgOptAve=_BaseScgPtpPmCmnScgOptAve_Object((1,3,6,1,4,1,21296,2,2,2,3,45,2,1,6),_BaseScgPtpPmCmnScgOptAve_Type())
baseScgPtpPmCmnScgOptAve.setMaxAccess(_C)
if mibBuilder.loadTexts:baseScgPtpPmCmnScgOptAve.setStatus(_A)
_BaseScgPtpPmCmnScgOprMin_Type=FloatHundredths
_BaseScgPtpPmCmnScgOprMin_Object=MibTableColumn
baseScgPtpPmCmnScgOprMin=_BaseScgPtpPmCmnScgOprMin_Object((1,3,6,1,4,1,21296,2,2,2,3,45,2,1,7),_BaseScgPtpPmCmnScgOprMin_Type())
baseScgPtpPmCmnScgOprMin.setMaxAccess(_C)
if mibBuilder.loadTexts:baseScgPtpPmCmnScgOprMin.setStatus(_A)
_BaseScgPtpPmCmnScgOprMax_Type=FloatHundredths
_BaseScgPtpPmCmnScgOprMax_Object=MibTableColumn
baseScgPtpPmCmnScgOprMax=_BaseScgPtpPmCmnScgOprMax_Object((1,3,6,1,4,1,21296,2,2,2,3,45,2,1,8),_BaseScgPtpPmCmnScgOprMax_Type())
baseScgPtpPmCmnScgOprMax.setMaxAccess(_C)
if mibBuilder.loadTexts:baseScgPtpPmCmnScgOprMax.setStatus(_A)
_BaseScgPtpPmCmnScgOprAve_Type=FloatHundredths
_BaseScgPtpPmCmnScgOprAve_Object=MibTableColumn
baseScgPtpPmCmnScgOprAve=_BaseScgPtpPmCmnScgOprAve_Object((1,3,6,1,4,1,21296,2,2,2,3,45,2,1,9),_BaseScgPtpPmCmnScgOprAve_Type())
baseScgPtpPmCmnScgOprAve.setMaxAccess(_C)
if mibBuilder.loadTexts:baseScgPtpPmCmnScgOprAve.setStatus(_A)
_BaseScgPtpPmConformance_ObjectIdentity=ObjectIdentity
baseScgPtpPmConformance=_BaseScgPtpPmConformance_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,3,45,3))
_BaseScgPtpPmCompliances_ObjectIdentity=ObjectIdentity
baseScgPtpPmCompliances=_BaseScgPtpPmCompliances_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,3,45,3,1))
_BaseScgPtpPmGroups_ObjectIdentity=ObjectIdentity
baseScgPtpPmGroups=_BaseScgPtpPmGroups_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,3,45,3,2))
baseScgPtpPmGroup=ObjectGroup((1,3,6,1,4,1,21296,2,2,2,3,45,3,2,1))
baseScgPtpPmGroup.setObjects(*((_B,_F),(_B,_G),(_B,_H),(_B,_I),(_B,_J),(_B,_K),(_B,_L)))
if mibBuilder.loadTexts:baseScgPtpPmGroup.setStatus(_A)
baseScgPtpPmRealGroup=ObjectGroup((1,3,6,1,4,1,21296,2,2,2,3,45,3,2,2))
baseScgPtpPmRealGroup.setObjects(*((_B,_M),(_B,_N)))
if mibBuilder.loadTexts:baseScgPtpPmRealGroup.setStatus(_A)
baseScgPtpPmCompliance=ModuleCompliance((1,3,6,1,4,1,21296,2,2,2,3,45,3,1,1))
baseScgPtpPmCompliance.setObjects((_B,_O))
if mibBuilder.loadTexts:baseScgPtpPmCompliance.setStatus(_A)
baseScgPtpPmRealCompliance=ModuleCompliance((1,3,6,1,4,1,21296,2,2,2,3,45,3,1,2))
baseScgPtpPmRealCompliance.setObjects((_B,_P))
if mibBuilder.loadTexts:baseScgPtpPmRealCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'baseScgPtpPmMIB':baseScgPtpPmMIB,'baseScgPtpPmRealTable':baseScgPtpPmRealTable,'baseScgPtpPmRealEntry':baseScgPtpPmRealEntry,_M:baseScgPtpPmRealCmnScgOpt,_N:baseScgPtpPmRealCmnScgOpr,'baseScgPtpPmTable':baseScgPtpPmTable,'baseScgPtpPmEntry':baseScgPtpPmEntry,_F:baseScgPtpPmValidity,_G:baseScgPtpPmCmnScgOptMin,_H:baseScgPtpPmCmnScgOptMax,_I:baseScgPtpPmCmnScgOptAve,_J:baseScgPtpPmCmnScgOprMin,_K:baseScgPtpPmCmnScgOprMax,_L:baseScgPtpPmCmnScgOprAve,'baseScgPtpPmConformance':baseScgPtpPmConformance,'baseScgPtpPmCompliances':baseScgPtpPmCompliances,'baseScgPtpPmCompliance':baseScgPtpPmCompliance,'baseScgPtpPmRealCompliance':baseScgPtpPmRealCompliance,'baseScgPtpPmGroups':baseScgPtpPmGroups,_O:baseScgPtpPmGroup,_P:baseScgPtpPmRealGroup})