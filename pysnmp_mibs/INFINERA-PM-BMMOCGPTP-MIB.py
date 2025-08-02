_T='bmmOcgPtpPmRealGroup'
_S='bmmOcgPtpPmGroup'
_R='bmmOcgPtpPmRealBmmOcgOpr'
_Q='bmmOcgPtpPmRealBmmOcgOpt'
_P='bmmOcgPtpPmBmmOcgOprAve'
_O='bmmOcgPtpPmBmmOcgOprMax'
_N='bmmOcgPtpPmBmmOcgOprMin'
_M='bmmOcgPtpPmBmmOcgOptAve'
_L='bmmOcgPtpPmBmmOcgOptMax'
_K='bmmOcgPtpPmBmmOcgOptMin'
_J='bmmOcgPtpPmValidity'
_I='not-accessible'
_H='bmmOcgPtpPmTimestamp'
_G='bmmOcgPtpPmSampleDuration'
_F='Integer32'
_E='ifIndex'
_D='IF-MIB'
_C='read-only'
_B='INFINERA-PM-BMMOCGPTP-MIB'
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
bmmOcgPtpPmMIB=ModuleIdentity((1,3,6,1,4,1,21296,2,2,2,3,2))
if mibBuilder.loadTexts:bmmOcgPtpPmMIB.setRevisions(('2008-10-20 00:00',))
_BmmOcgPtpPmRealTable_Object=MibTable
bmmOcgPtpPmRealTable=_BmmOcgPtpPmRealTable_Object((1,3,6,1,4,1,21296,2,2,2,3,2,1))
if mibBuilder.loadTexts:bmmOcgPtpPmRealTable.setStatus(_A)
_BmmOcgPtpPmRealEntry_Object=MibTableRow
bmmOcgPtpPmRealEntry=_BmmOcgPtpPmRealEntry_Object((1,3,6,1,4,1,21296,2,2,2,3,2,1,1))
bmmOcgPtpPmRealEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:bmmOcgPtpPmRealEntry.setStatus(_A)
_BmmOcgPtpPmRealBmmOcgOpt_Type=FloatHundredths
_BmmOcgPtpPmRealBmmOcgOpt_Object=MibTableColumn
bmmOcgPtpPmRealBmmOcgOpt=_BmmOcgPtpPmRealBmmOcgOpt_Object((1,3,6,1,4,1,21296,2,2,2,3,2,1,1,1),_BmmOcgPtpPmRealBmmOcgOpt_Type())
bmmOcgPtpPmRealBmmOcgOpt.setMaxAccess(_C)
if mibBuilder.loadTexts:bmmOcgPtpPmRealBmmOcgOpt.setStatus(_A)
_BmmOcgPtpPmRealBmmOcgOpr_Type=FloatHundredths
_BmmOcgPtpPmRealBmmOcgOpr_Object=MibTableColumn
bmmOcgPtpPmRealBmmOcgOpr=_BmmOcgPtpPmRealBmmOcgOpr_Object((1,3,6,1,4,1,21296,2,2,2,3,2,1,1,2),_BmmOcgPtpPmRealBmmOcgOpr_Type())
bmmOcgPtpPmRealBmmOcgOpr.setMaxAccess(_C)
if mibBuilder.loadTexts:bmmOcgPtpPmRealBmmOcgOpr.setStatus(_A)
_BmmOcgPtpPmTable_Object=MibTable
bmmOcgPtpPmTable=_BmmOcgPtpPmTable_Object((1,3,6,1,4,1,21296,2,2,2,3,2,2))
if mibBuilder.loadTexts:bmmOcgPtpPmTable.setStatus(_A)
_BmmOcgPtpPmEntry_Object=MibTableRow
bmmOcgPtpPmEntry=_BmmOcgPtpPmEntry_Object((1,3,6,1,4,1,21296,2,2,2,3,2,2,1))
bmmOcgPtpPmEntry.setIndexNames((0,_D,_E),(0,_B,_G),(0,_B,_H))
if mibBuilder.loadTexts:bmmOcgPtpPmEntry.setStatus(_A)
class _BmmOcgPtpPmTimestamp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_BmmOcgPtpPmTimestamp_Type.__name__=_F
_BmmOcgPtpPmTimestamp_Object=MibTableColumn
bmmOcgPtpPmTimestamp=_BmmOcgPtpPmTimestamp_Object((1,3,6,1,4,1,21296,2,2,2,3,2,2,1,1),_BmmOcgPtpPmTimestamp_Type())
bmmOcgPtpPmTimestamp.setMaxAccess(_I)
if mibBuilder.loadTexts:bmmOcgPtpPmTimestamp.setStatus(_A)
class _BmmOcgPtpPmSampleDuration_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('fifteenMinutes',1),('day',2)))
_BmmOcgPtpPmSampleDuration_Type.__name__=_F
_BmmOcgPtpPmSampleDuration_Object=MibTableColumn
bmmOcgPtpPmSampleDuration=_BmmOcgPtpPmSampleDuration_Object((1,3,6,1,4,1,21296,2,2,2,3,2,2,1,2),_BmmOcgPtpPmSampleDuration_Type())
bmmOcgPtpPmSampleDuration.setMaxAccess(_I)
if mibBuilder.loadTexts:bmmOcgPtpPmSampleDuration.setStatus(_A)
_BmmOcgPtpPmValidity_Type=TruthValue
_BmmOcgPtpPmValidity_Object=MibTableColumn
bmmOcgPtpPmValidity=_BmmOcgPtpPmValidity_Object((1,3,6,1,4,1,21296,2,2,2,3,2,2,1,3),_BmmOcgPtpPmValidity_Type())
bmmOcgPtpPmValidity.setMaxAccess(_C)
if mibBuilder.loadTexts:bmmOcgPtpPmValidity.setStatus(_A)
_BmmOcgPtpPmBmmOcgOptMin_Type=FloatHundredths
_BmmOcgPtpPmBmmOcgOptMin_Object=MibTableColumn
bmmOcgPtpPmBmmOcgOptMin=_BmmOcgPtpPmBmmOcgOptMin_Object((1,3,6,1,4,1,21296,2,2,2,3,2,2,1,4),_BmmOcgPtpPmBmmOcgOptMin_Type())
bmmOcgPtpPmBmmOcgOptMin.setMaxAccess(_C)
if mibBuilder.loadTexts:bmmOcgPtpPmBmmOcgOptMin.setStatus(_A)
_BmmOcgPtpPmBmmOcgOptMax_Type=FloatHundredths
_BmmOcgPtpPmBmmOcgOptMax_Object=MibTableColumn
bmmOcgPtpPmBmmOcgOptMax=_BmmOcgPtpPmBmmOcgOptMax_Object((1,3,6,1,4,1,21296,2,2,2,3,2,2,1,5),_BmmOcgPtpPmBmmOcgOptMax_Type())
bmmOcgPtpPmBmmOcgOptMax.setMaxAccess(_C)
if mibBuilder.loadTexts:bmmOcgPtpPmBmmOcgOptMax.setStatus(_A)
_BmmOcgPtpPmBmmOcgOptAve_Type=FloatHundredths
_BmmOcgPtpPmBmmOcgOptAve_Object=MibTableColumn
bmmOcgPtpPmBmmOcgOptAve=_BmmOcgPtpPmBmmOcgOptAve_Object((1,3,6,1,4,1,21296,2,2,2,3,2,2,1,6),_BmmOcgPtpPmBmmOcgOptAve_Type())
bmmOcgPtpPmBmmOcgOptAve.setMaxAccess(_C)
if mibBuilder.loadTexts:bmmOcgPtpPmBmmOcgOptAve.setStatus(_A)
_BmmOcgPtpPmBmmOcgOprMin_Type=FloatHundredths
_BmmOcgPtpPmBmmOcgOprMin_Object=MibTableColumn
bmmOcgPtpPmBmmOcgOprMin=_BmmOcgPtpPmBmmOcgOprMin_Object((1,3,6,1,4,1,21296,2,2,2,3,2,2,1,7),_BmmOcgPtpPmBmmOcgOprMin_Type())
bmmOcgPtpPmBmmOcgOprMin.setMaxAccess(_C)
if mibBuilder.loadTexts:bmmOcgPtpPmBmmOcgOprMin.setStatus(_A)
_BmmOcgPtpPmBmmOcgOprMax_Type=FloatHundredths
_BmmOcgPtpPmBmmOcgOprMax_Object=MibTableColumn
bmmOcgPtpPmBmmOcgOprMax=_BmmOcgPtpPmBmmOcgOprMax_Object((1,3,6,1,4,1,21296,2,2,2,3,2,2,1,8),_BmmOcgPtpPmBmmOcgOprMax_Type())
bmmOcgPtpPmBmmOcgOprMax.setMaxAccess(_C)
if mibBuilder.loadTexts:bmmOcgPtpPmBmmOcgOprMax.setStatus(_A)
_BmmOcgPtpPmBmmOcgOprAve_Type=FloatHundredths
_BmmOcgPtpPmBmmOcgOprAve_Object=MibTableColumn
bmmOcgPtpPmBmmOcgOprAve=_BmmOcgPtpPmBmmOcgOprAve_Object((1,3,6,1,4,1,21296,2,2,2,3,2,2,1,9),_BmmOcgPtpPmBmmOcgOprAve_Type())
bmmOcgPtpPmBmmOcgOprAve.setMaxAccess(_C)
if mibBuilder.loadTexts:bmmOcgPtpPmBmmOcgOprAve.setStatus(_A)
_BmmOcgPtpPmConformance_ObjectIdentity=ObjectIdentity
bmmOcgPtpPmConformance=_BmmOcgPtpPmConformance_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,3,2,3))
_BmmOcgPtpPmCompliances_ObjectIdentity=ObjectIdentity
bmmOcgPtpPmCompliances=_BmmOcgPtpPmCompliances_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,3,2,3,1))
_BmmOcgPtpPmGroups_ObjectIdentity=ObjectIdentity
bmmOcgPtpPmGroups=_BmmOcgPtpPmGroups_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,3,2,3,2))
bmmOcgPtpPmGroup=ObjectGroup((1,3,6,1,4,1,21296,2,2,2,3,2,3,2,1))
bmmOcgPtpPmGroup.setObjects(*((_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P)))
if mibBuilder.loadTexts:bmmOcgPtpPmGroup.setStatus(_A)
bmmOcgPtpPmRealGroup=ObjectGroup((1,3,6,1,4,1,21296,2,2,2,3,2,3,2,2))
bmmOcgPtpPmRealGroup.setObjects(*((_B,_Q),(_B,_R)))
if mibBuilder.loadTexts:bmmOcgPtpPmRealGroup.setStatus(_A)
bmmOcgPtpPmCompliance=ModuleCompliance((1,3,6,1,4,1,21296,2,2,2,3,2,3,1,1))
bmmOcgPtpPmCompliance.setObjects((_B,_S))
if mibBuilder.loadTexts:bmmOcgPtpPmCompliance.setStatus(_A)
bmmOcgPtpPmRealCompliance=ModuleCompliance((1,3,6,1,4,1,21296,2,2,2,3,2,3,1,2))
bmmOcgPtpPmRealCompliance.setObjects((_B,_T))
if mibBuilder.loadTexts:bmmOcgPtpPmRealCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'bmmOcgPtpPmMIB':bmmOcgPtpPmMIB,'bmmOcgPtpPmRealTable':bmmOcgPtpPmRealTable,'bmmOcgPtpPmRealEntry':bmmOcgPtpPmRealEntry,_Q:bmmOcgPtpPmRealBmmOcgOpt,_R:bmmOcgPtpPmRealBmmOcgOpr,'bmmOcgPtpPmTable':bmmOcgPtpPmTable,'bmmOcgPtpPmEntry':bmmOcgPtpPmEntry,_H:bmmOcgPtpPmTimestamp,_G:bmmOcgPtpPmSampleDuration,_J:bmmOcgPtpPmValidity,_K:bmmOcgPtpPmBmmOcgOptMin,_L:bmmOcgPtpPmBmmOcgOptMax,_M:bmmOcgPtpPmBmmOcgOptAve,_N:bmmOcgPtpPmBmmOcgOprMin,_O:bmmOcgPtpPmBmmOcgOprMax,_P:bmmOcgPtpPmBmmOcgOprAve,'bmmOcgPtpPmConformance':bmmOcgPtpPmConformance,'bmmOcgPtpPmCompliances':bmmOcgPtpPmCompliances,'bmmOcgPtpPmCompliance':bmmOcgPtpPmCompliance,'bmmOcgPtpPmRealCompliance':bmmOcgPtpPmRealCompliance,'bmmOcgPtpPmGroups':bmmOcgPtpPmGroups,_S:bmmOcgPtpPmGroup,_T:bmmOcgPtpPmRealGroup})