_T='dcfPtpPmRealGroup'
_S='dcfPtpPmGroup'
_R='dcfPtpPmRealOpr'
_Q='dcfPtpPmRealOpt'
_P='dcfPtpPmOprAve'
_O='dcfPtpPmOprMax'
_N='dcfPtpPmOprMin'
_M='dcfPtpPmOptAve'
_L='dcfPtpPmOptMax'
_K='dcfPtpPmOptMin'
_J='dcfPtpPmValidity'
_I='not-accessible'
_H='dcfPtpPmTimestamp'
_G='dcfPtpPmSampleDuration'
_F='Integer32'
_E='ifIndex'
_D='IF-MIB'
_C='read-only'
_B='INFINERA-PM-DCFPTP-MIB'
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
dcfPtpPmMIB=ModuleIdentity((1,3,6,1,4,1,21296,2,2,2,3,17))
if mibBuilder.loadTexts:dcfPtpPmMIB.setRevisions(('2008-10-20 00:00',))
_DcfPtpPmRealTable_Object=MibTable
dcfPtpPmRealTable=_DcfPtpPmRealTable_Object((1,3,6,1,4,1,21296,2,2,2,3,17,1))
if mibBuilder.loadTexts:dcfPtpPmRealTable.setStatus(_A)
_DcfPtpPmRealEntry_Object=MibTableRow
dcfPtpPmRealEntry=_DcfPtpPmRealEntry_Object((1,3,6,1,4,1,21296,2,2,2,3,17,1,1))
dcfPtpPmRealEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:dcfPtpPmRealEntry.setStatus(_A)
_DcfPtpPmRealOpt_Type=FloatHundredths
_DcfPtpPmRealOpt_Object=MibTableColumn
dcfPtpPmRealOpt=_DcfPtpPmRealOpt_Object((1,3,6,1,4,1,21296,2,2,2,3,17,1,1,1),_DcfPtpPmRealOpt_Type())
dcfPtpPmRealOpt.setMaxAccess(_C)
if mibBuilder.loadTexts:dcfPtpPmRealOpt.setStatus(_A)
_DcfPtpPmRealOpr_Type=FloatHundredths
_DcfPtpPmRealOpr_Object=MibTableColumn
dcfPtpPmRealOpr=_DcfPtpPmRealOpr_Object((1,3,6,1,4,1,21296,2,2,2,3,17,1,1,2),_DcfPtpPmRealOpr_Type())
dcfPtpPmRealOpr.setMaxAccess(_C)
if mibBuilder.loadTexts:dcfPtpPmRealOpr.setStatus(_A)
_DcfPtpPmTable_Object=MibTable
dcfPtpPmTable=_DcfPtpPmTable_Object((1,3,6,1,4,1,21296,2,2,2,3,17,2))
if mibBuilder.loadTexts:dcfPtpPmTable.setStatus(_A)
_DcfPtpPmEntry_Object=MibTableRow
dcfPtpPmEntry=_DcfPtpPmEntry_Object((1,3,6,1,4,1,21296,2,2,2,3,17,2,1))
dcfPtpPmEntry.setIndexNames((0,_D,_E),(0,_B,_G),(0,_B,_H))
if mibBuilder.loadTexts:dcfPtpPmEntry.setStatus(_A)
class _DcfPtpPmTimestamp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_DcfPtpPmTimestamp_Type.__name__=_F
_DcfPtpPmTimestamp_Object=MibTableColumn
dcfPtpPmTimestamp=_DcfPtpPmTimestamp_Object((1,3,6,1,4,1,21296,2,2,2,3,17,2,1,1),_DcfPtpPmTimestamp_Type())
dcfPtpPmTimestamp.setMaxAccess(_I)
if mibBuilder.loadTexts:dcfPtpPmTimestamp.setStatus(_A)
class _DcfPtpPmSampleDuration_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('fifteenMinutes',1),('day',2)))
_DcfPtpPmSampleDuration_Type.__name__=_F
_DcfPtpPmSampleDuration_Object=MibTableColumn
dcfPtpPmSampleDuration=_DcfPtpPmSampleDuration_Object((1,3,6,1,4,1,21296,2,2,2,3,17,2,1,2),_DcfPtpPmSampleDuration_Type())
dcfPtpPmSampleDuration.setMaxAccess(_I)
if mibBuilder.loadTexts:dcfPtpPmSampleDuration.setStatus(_A)
_DcfPtpPmValidity_Type=TruthValue
_DcfPtpPmValidity_Object=MibTableColumn
dcfPtpPmValidity=_DcfPtpPmValidity_Object((1,3,6,1,4,1,21296,2,2,2,3,17,2,1,3),_DcfPtpPmValidity_Type())
dcfPtpPmValidity.setMaxAccess(_C)
if mibBuilder.loadTexts:dcfPtpPmValidity.setStatus(_A)
_DcfPtpPmOptMin_Type=FloatHundredths
_DcfPtpPmOptMin_Object=MibTableColumn
dcfPtpPmOptMin=_DcfPtpPmOptMin_Object((1,3,6,1,4,1,21296,2,2,2,3,17,2,1,4),_DcfPtpPmOptMin_Type())
dcfPtpPmOptMin.setMaxAccess(_C)
if mibBuilder.loadTexts:dcfPtpPmOptMin.setStatus(_A)
_DcfPtpPmOptMax_Type=FloatHundredths
_DcfPtpPmOptMax_Object=MibTableColumn
dcfPtpPmOptMax=_DcfPtpPmOptMax_Object((1,3,6,1,4,1,21296,2,2,2,3,17,2,1,5),_DcfPtpPmOptMax_Type())
dcfPtpPmOptMax.setMaxAccess(_C)
if mibBuilder.loadTexts:dcfPtpPmOptMax.setStatus(_A)
_DcfPtpPmOptAve_Type=FloatHundredths
_DcfPtpPmOptAve_Object=MibTableColumn
dcfPtpPmOptAve=_DcfPtpPmOptAve_Object((1,3,6,1,4,1,21296,2,2,2,3,17,2,1,6),_DcfPtpPmOptAve_Type())
dcfPtpPmOptAve.setMaxAccess(_C)
if mibBuilder.loadTexts:dcfPtpPmOptAve.setStatus(_A)
_DcfPtpPmOprMin_Type=FloatHundredths
_DcfPtpPmOprMin_Object=MibTableColumn
dcfPtpPmOprMin=_DcfPtpPmOprMin_Object((1,3,6,1,4,1,21296,2,2,2,3,17,2,1,7),_DcfPtpPmOprMin_Type())
dcfPtpPmOprMin.setMaxAccess(_C)
if mibBuilder.loadTexts:dcfPtpPmOprMin.setStatus(_A)
_DcfPtpPmOprMax_Type=FloatHundredths
_DcfPtpPmOprMax_Object=MibTableColumn
dcfPtpPmOprMax=_DcfPtpPmOprMax_Object((1,3,6,1,4,1,21296,2,2,2,3,17,2,1,8),_DcfPtpPmOprMax_Type())
dcfPtpPmOprMax.setMaxAccess(_C)
if mibBuilder.loadTexts:dcfPtpPmOprMax.setStatus(_A)
_DcfPtpPmOprAve_Type=FloatHundredths
_DcfPtpPmOprAve_Object=MibTableColumn
dcfPtpPmOprAve=_DcfPtpPmOprAve_Object((1,3,6,1,4,1,21296,2,2,2,3,17,2,1,9),_DcfPtpPmOprAve_Type())
dcfPtpPmOprAve.setMaxAccess(_C)
if mibBuilder.loadTexts:dcfPtpPmOprAve.setStatus(_A)
_DcfPtpPmConformance_ObjectIdentity=ObjectIdentity
dcfPtpPmConformance=_DcfPtpPmConformance_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,3,17,3))
_DcfPtpPmCompliances_ObjectIdentity=ObjectIdentity
dcfPtpPmCompliances=_DcfPtpPmCompliances_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,3,17,3,1))
_DcfPtpPmGroups_ObjectIdentity=ObjectIdentity
dcfPtpPmGroups=_DcfPtpPmGroups_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,3,17,3,2))
dcfPtpPmGroup=ObjectGroup((1,3,6,1,4,1,21296,2,2,2,3,17,3,2,1))
dcfPtpPmGroup.setObjects(*((_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P)))
if mibBuilder.loadTexts:dcfPtpPmGroup.setStatus(_A)
dcfPtpPmRealGroup=ObjectGroup((1,3,6,1,4,1,21296,2,2,2,3,17,3,2,2))
dcfPtpPmRealGroup.setObjects(*((_B,_Q),(_B,_R)))
if mibBuilder.loadTexts:dcfPtpPmRealGroup.setStatus(_A)
dcfPtpPmCompliance=ModuleCompliance((1,3,6,1,4,1,21296,2,2,2,3,17,3,1,1))
dcfPtpPmCompliance.setObjects((_B,_S))
if mibBuilder.loadTexts:dcfPtpPmCompliance.setStatus(_A)
dcfPtpPmRealCompliance=ModuleCompliance((1,3,6,1,4,1,21296,2,2,2,3,17,3,1,2))
dcfPtpPmRealCompliance.setObjects((_B,_T))
if mibBuilder.loadTexts:dcfPtpPmRealCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'dcfPtpPmMIB':dcfPtpPmMIB,'dcfPtpPmRealTable':dcfPtpPmRealTable,'dcfPtpPmRealEntry':dcfPtpPmRealEntry,_Q:dcfPtpPmRealOpt,_R:dcfPtpPmRealOpr,'dcfPtpPmTable':dcfPtpPmTable,'dcfPtpPmEntry':dcfPtpPmEntry,_H:dcfPtpPmTimestamp,_G:dcfPtpPmSampleDuration,_J:dcfPtpPmValidity,_K:dcfPtpPmOptMin,_L:dcfPtpPmOptMax,_M:dcfPtpPmOptAve,_N:dcfPtpPmOprMin,_O:dcfPtpPmOprMax,_P:dcfPtpPmOprAve,'dcfPtpPmConformance':dcfPtpPmConformance,'dcfPtpPmCompliances':dcfPtpPmCompliances,'dcfPtpPmCompliance':dcfPtpPmCompliance,'dcfPtpPmRealCompliance':dcfPtpPmRealCompliance,'dcfPtpPmGroups':dcfPtpPmGroups,_S:dcfPtpPmGroup,_T:dcfPtpPmRealGroup})