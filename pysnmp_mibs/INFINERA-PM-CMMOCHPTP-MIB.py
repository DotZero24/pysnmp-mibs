_T='cmmOchPtpPmRealGroup'
_S='cmmOchPtpPmGroup'
_R='cmmOchPtpPmRealCmmOchOpr'
_Q='cmmOchPtpPmRealCmmOchOpt'
_P='cmmOchPtpPmCmmOchOprAve'
_O='cmmOchPtpPmCmmOchOprMax'
_N='cmmOchPtpPmCmmOchOprMin'
_M='cmmOchPtpPmCmmOchOptAve'
_L='cmmOchPtpPmCmmOchOptMax'
_K='cmmOchPtpPmCmmOchOptMin'
_J='cmmOchPtpPmValidity'
_I='not-accessible'
_H='cmmOchPtpPmTimestamp'
_G='cmmOchPtpPmSampleDuration'
_F='Integer32'
_E='ifIndex'
_D='IF-MIB'
_C='read-only'
_B='INFINERA-PM-CMMOCHPTP-MIB'
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
cmmOchPtpPmMIB=ModuleIdentity((1,3,6,1,4,1,21296,2,2,2,3,26))
if mibBuilder.loadTexts:cmmOchPtpPmMIB.setRevisions(('2008-10-20 00:00',))
_CmmOchPtpPmRealTable_Object=MibTable
cmmOchPtpPmRealTable=_CmmOchPtpPmRealTable_Object((1,3,6,1,4,1,21296,2,2,2,3,26,1))
if mibBuilder.loadTexts:cmmOchPtpPmRealTable.setStatus(_A)
_CmmOchPtpPmRealEntry_Object=MibTableRow
cmmOchPtpPmRealEntry=_CmmOchPtpPmRealEntry_Object((1,3,6,1,4,1,21296,2,2,2,3,26,1,1))
cmmOchPtpPmRealEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:cmmOchPtpPmRealEntry.setStatus(_A)
_CmmOchPtpPmRealCmmOchOpt_Type=FloatHundredths
_CmmOchPtpPmRealCmmOchOpt_Object=MibTableColumn
cmmOchPtpPmRealCmmOchOpt=_CmmOchPtpPmRealCmmOchOpt_Object((1,3,6,1,4,1,21296,2,2,2,3,26,1,1,1),_CmmOchPtpPmRealCmmOchOpt_Type())
cmmOchPtpPmRealCmmOchOpt.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmOchPtpPmRealCmmOchOpt.setStatus(_A)
_CmmOchPtpPmRealCmmOchOpr_Type=FloatHundredths
_CmmOchPtpPmRealCmmOchOpr_Object=MibTableColumn
cmmOchPtpPmRealCmmOchOpr=_CmmOchPtpPmRealCmmOchOpr_Object((1,3,6,1,4,1,21296,2,2,2,3,26,1,1,2),_CmmOchPtpPmRealCmmOchOpr_Type())
cmmOchPtpPmRealCmmOchOpr.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmOchPtpPmRealCmmOchOpr.setStatus(_A)
_CmmOchPtpPmTable_Object=MibTable
cmmOchPtpPmTable=_CmmOchPtpPmTable_Object((1,3,6,1,4,1,21296,2,2,2,3,26,2))
if mibBuilder.loadTexts:cmmOchPtpPmTable.setStatus(_A)
_CmmOchPtpPmEntry_Object=MibTableRow
cmmOchPtpPmEntry=_CmmOchPtpPmEntry_Object((1,3,6,1,4,1,21296,2,2,2,3,26,2,1))
cmmOchPtpPmEntry.setIndexNames((0,_D,_E),(0,_B,_G),(0,_B,_H))
if mibBuilder.loadTexts:cmmOchPtpPmEntry.setStatus(_A)
class _CmmOchPtpPmTimestamp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CmmOchPtpPmTimestamp_Type.__name__=_F
_CmmOchPtpPmTimestamp_Object=MibTableColumn
cmmOchPtpPmTimestamp=_CmmOchPtpPmTimestamp_Object((1,3,6,1,4,1,21296,2,2,2,3,26,2,1,1),_CmmOchPtpPmTimestamp_Type())
cmmOchPtpPmTimestamp.setMaxAccess(_I)
if mibBuilder.loadTexts:cmmOchPtpPmTimestamp.setStatus(_A)
class _CmmOchPtpPmSampleDuration_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('fifteenMinutes',1),('day',2)))
_CmmOchPtpPmSampleDuration_Type.__name__=_F
_CmmOchPtpPmSampleDuration_Object=MibTableColumn
cmmOchPtpPmSampleDuration=_CmmOchPtpPmSampleDuration_Object((1,3,6,1,4,1,21296,2,2,2,3,26,2,1,2),_CmmOchPtpPmSampleDuration_Type())
cmmOchPtpPmSampleDuration.setMaxAccess(_I)
if mibBuilder.loadTexts:cmmOchPtpPmSampleDuration.setStatus(_A)
_CmmOchPtpPmValidity_Type=TruthValue
_CmmOchPtpPmValidity_Object=MibTableColumn
cmmOchPtpPmValidity=_CmmOchPtpPmValidity_Object((1,3,6,1,4,1,21296,2,2,2,3,26,2,1,3),_CmmOchPtpPmValidity_Type())
cmmOchPtpPmValidity.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmOchPtpPmValidity.setStatus(_A)
_CmmOchPtpPmCmmOchOptMin_Type=FloatHundredths
_CmmOchPtpPmCmmOchOptMin_Object=MibTableColumn
cmmOchPtpPmCmmOchOptMin=_CmmOchPtpPmCmmOchOptMin_Object((1,3,6,1,4,1,21296,2,2,2,3,26,2,1,4),_CmmOchPtpPmCmmOchOptMin_Type())
cmmOchPtpPmCmmOchOptMin.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmOchPtpPmCmmOchOptMin.setStatus(_A)
_CmmOchPtpPmCmmOchOptMax_Type=FloatHundredths
_CmmOchPtpPmCmmOchOptMax_Object=MibTableColumn
cmmOchPtpPmCmmOchOptMax=_CmmOchPtpPmCmmOchOptMax_Object((1,3,6,1,4,1,21296,2,2,2,3,26,2,1,5),_CmmOchPtpPmCmmOchOptMax_Type())
cmmOchPtpPmCmmOchOptMax.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmOchPtpPmCmmOchOptMax.setStatus(_A)
_CmmOchPtpPmCmmOchOptAve_Type=FloatHundredths
_CmmOchPtpPmCmmOchOptAve_Object=MibTableColumn
cmmOchPtpPmCmmOchOptAve=_CmmOchPtpPmCmmOchOptAve_Object((1,3,6,1,4,1,21296,2,2,2,3,26,2,1,6),_CmmOchPtpPmCmmOchOptAve_Type())
cmmOchPtpPmCmmOchOptAve.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmOchPtpPmCmmOchOptAve.setStatus(_A)
_CmmOchPtpPmCmmOchOprMin_Type=FloatHundredths
_CmmOchPtpPmCmmOchOprMin_Object=MibTableColumn
cmmOchPtpPmCmmOchOprMin=_CmmOchPtpPmCmmOchOprMin_Object((1,3,6,1,4,1,21296,2,2,2,3,26,2,1,7),_CmmOchPtpPmCmmOchOprMin_Type())
cmmOchPtpPmCmmOchOprMin.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmOchPtpPmCmmOchOprMin.setStatus(_A)
_CmmOchPtpPmCmmOchOprMax_Type=FloatHundredths
_CmmOchPtpPmCmmOchOprMax_Object=MibTableColumn
cmmOchPtpPmCmmOchOprMax=_CmmOchPtpPmCmmOchOprMax_Object((1,3,6,1,4,1,21296,2,2,2,3,26,2,1,8),_CmmOchPtpPmCmmOchOprMax_Type())
cmmOchPtpPmCmmOchOprMax.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmOchPtpPmCmmOchOprMax.setStatus(_A)
_CmmOchPtpPmCmmOchOprAve_Type=FloatHundredths
_CmmOchPtpPmCmmOchOprAve_Object=MibTableColumn
cmmOchPtpPmCmmOchOprAve=_CmmOchPtpPmCmmOchOprAve_Object((1,3,6,1,4,1,21296,2,2,2,3,26,2,1,9),_CmmOchPtpPmCmmOchOprAve_Type())
cmmOchPtpPmCmmOchOprAve.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmOchPtpPmCmmOchOprAve.setStatus(_A)
_CmmOchPtpPmConformance_ObjectIdentity=ObjectIdentity
cmmOchPtpPmConformance=_CmmOchPtpPmConformance_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,3,26,3))
_CmmOchPtpPmCompliances_ObjectIdentity=ObjectIdentity
cmmOchPtpPmCompliances=_CmmOchPtpPmCompliances_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,3,26,3,1))
_CmmOchPtpPmGroups_ObjectIdentity=ObjectIdentity
cmmOchPtpPmGroups=_CmmOchPtpPmGroups_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,3,26,3,2))
cmmOchPtpPmGroup=ObjectGroup((1,3,6,1,4,1,21296,2,2,2,3,26,3,2,1))
cmmOchPtpPmGroup.setObjects(*((_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P)))
if mibBuilder.loadTexts:cmmOchPtpPmGroup.setStatus(_A)
cmmOchPtpPmRealGroup=ObjectGroup((1,3,6,1,4,1,21296,2,2,2,3,26,3,2,2))
cmmOchPtpPmRealGroup.setObjects(*((_B,_Q),(_B,_R)))
if mibBuilder.loadTexts:cmmOchPtpPmRealGroup.setStatus(_A)
cmmOchPtpPmCompliance=ModuleCompliance((1,3,6,1,4,1,21296,2,2,2,3,26,3,1,1))
cmmOchPtpPmCompliance.setObjects((_B,_S))
if mibBuilder.loadTexts:cmmOchPtpPmCompliance.setStatus(_A)
cmmOchPtpPmRealCompliance=ModuleCompliance((1,3,6,1,4,1,21296,2,2,2,3,26,3,1,2))
cmmOchPtpPmRealCompliance.setObjects((_B,_T))
if mibBuilder.loadTexts:cmmOchPtpPmRealCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'cmmOchPtpPmMIB':cmmOchPtpPmMIB,'cmmOchPtpPmRealTable':cmmOchPtpPmRealTable,'cmmOchPtpPmRealEntry':cmmOchPtpPmRealEntry,_Q:cmmOchPtpPmRealCmmOchOpt,_R:cmmOchPtpPmRealCmmOchOpr,'cmmOchPtpPmTable':cmmOchPtpPmTable,'cmmOchPtpPmEntry':cmmOchPtpPmEntry,_H:cmmOchPtpPmTimestamp,_G:cmmOchPtpPmSampleDuration,_J:cmmOchPtpPmValidity,_K:cmmOchPtpPmCmmOchOptMin,_L:cmmOchPtpPmCmmOchOptMax,_M:cmmOchPtpPmCmmOchOptAve,_N:cmmOchPtpPmCmmOchOprMin,_O:cmmOchPtpPmCmmOchOprMax,_P:cmmOchPtpPmCmmOchOprAve,'cmmOchPtpPmConformance':cmmOchPtpPmConformance,'cmmOchPtpPmCompliances':cmmOchPtpPmCompliances,'cmmOchPtpPmCompliance':cmmOchPtpPmCompliance,'cmmOchPtpPmRealCompliance':cmmOchPtpPmRealCompliance,'cmmOchPtpPmGroups':cmmOchPtpPmGroups,_S:cmmOchPtpPmGroup,_T:cmmOchPtpPmRealGroup})