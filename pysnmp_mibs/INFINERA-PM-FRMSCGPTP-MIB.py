_T='frmScgPtpPmRealGroup'
_S='frmScgPtpPmGroup'
_R='frmScgPtpPmRealCmnScgOpr'
_Q='frmScgPtpPmRealCmnScgOpt'
_P='frmScgPtpPmCmnScgOprAve'
_O='frmScgPtpPmCmnScgOprMax'
_N='frmScgPtpPmCmnScgOprMin'
_M='frmScgPtpPmCmnScgOptAve'
_L='frmScgPtpPmCmnScgOptMax'
_K='frmScgPtpPmCmnScgOptMin'
_J='frmScgPtpPmValidity'
_I='not-accessible'
_H='frmScgPtpPmTimestamp'
_G='frmScgPtpPmSampleDuration'
_F='Integer32'
_E='ifIndex'
_D='IF-MIB'
_C='read-only'
_B='INFINERA-PM-FRMSCGPTP-MIB'
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
frmScgPtpPmMIB=ModuleIdentity((1,3,6,1,4,1,21296,2,2,2,3,41))
if mibBuilder.loadTexts:frmScgPtpPmMIB.setRevisions(('2013-10-08 00:00',))
_FrmScgPtpPmRealTable_Object=MibTable
frmScgPtpPmRealTable=_FrmScgPtpPmRealTable_Object((1,3,6,1,4,1,21296,2,2,2,3,41,1))
if mibBuilder.loadTexts:frmScgPtpPmRealTable.setStatus(_A)
_FrmScgPtpPmRealEntry_Object=MibTableRow
frmScgPtpPmRealEntry=_FrmScgPtpPmRealEntry_Object((1,3,6,1,4,1,21296,2,2,2,3,41,1,1))
frmScgPtpPmRealEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:frmScgPtpPmRealEntry.setStatus(_A)
_FrmScgPtpPmRealCmnScgOpt_Type=FloatHundredths
_FrmScgPtpPmRealCmnScgOpt_Object=MibTableColumn
frmScgPtpPmRealCmnScgOpt=_FrmScgPtpPmRealCmnScgOpt_Object((1,3,6,1,4,1,21296,2,2,2,3,41,1,1,1),_FrmScgPtpPmRealCmnScgOpt_Type())
frmScgPtpPmRealCmnScgOpt.setMaxAccess(_C)
if mibBuilder.loadTexts:frmScgPtpPmRealCmnScgOpt.setStatus(_A)
_FrmScgPtpPmRealCmnScgOpr_Type=FloatHundredths
_FrmScgPtpPmRealCmnScgOpr_Object=MibTableColumn
frmScgPtpPmRealCmnScgOpr=_FrmScgPtpPmRealCmnScgOpr_Object((1,3,6,1,4,1,21296,2,2,2,3,41,1,1,2),_FrmScgPtpPmRealCmnScgOpr_Type())
frmScgPtpPmRealCmnScgOpr.setMaxAccess(_C)
if mibBuilder.loadTexts:frmScgPtpPmRealCmnScgOpr.setStatus(_A)
_FrmScgPtpPmTable_Object=MibTable
frmScgPtpPmTable=_FrmScgPtpPmTable_Object((1,3,6,1,4,1,21296,2,2,2,3,41,2))
if mibBuilder.loadTexts:frmScgPtpPmTable.setStatus(_A)
_FrmScgPtpPmEntry_Object=MibTableRow
frmScgPtpPmEntry=_FrmScgPtpPmEntry_Object((1,3,6,1,4,1,21296,2,2,2,3,41,2,1))
frmScgPtpPmEntry.setIndexNames((0,_D,_E),(0,_B,_G),(0,_B,_H))
if mibBuilder.loadTexts:frmScgPtpPmEntry.setStatus(_A)
class _FrmScgPtpPmTimestamp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_FrmScgPtpPmTimestamp_Type.__name__=_F
_FrmScgPtpPmTimestamp_Object=MibTableColumn
frmScgPtpPmTimestamp=_FrmScgPtpPmTimestamp_Object((1,3,6,1,4,1,21296,2,2,2,3,41,2,1,1),_FrmScgPtpPmTimestamp_Type())
frmScgPtpPmTimestamp.setMaxAccess(_I)
if mibBuilder.loadTexts:frmScgPtpPmTimestamp.setStatus(_A)
class _FrmScgPtpPmSampleDuration_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('fifteenMinutes',1),('day',2)))
_FrmScgPtpPmSampleDuration_Type.__name__=_F
_FrmScgPtpPmSampleDuration_Object=MibTableColumn
frmScgPtpPmSampleDuration=_FrmScgPtpPmSampleDuration_Object((1,3,6,1,4,1,21296,2,2,2,3,41,2,1,2),_FrmScgPtpPmSampleDuration_Type())
frmScgPtpPmSampleDuration.setMaxAccess(_I)
if mibBuilder.loadTexts:frmScgPtpPmSampleDuration.setStatus(_A)
_FrmScgPtpPmValidity_Type=TruthValue
_FrmScgPtpPmValidity_Object=MibTableColumn
frmScgPtpPmValidity=_FrmScgPtpPmValidity_Object((1,3,6,1,4,1,21296,2,2,2,3,41,2,1,3),_FrmScgPtpPmValidity_Type())
frmScgPtpPmValidity.setMaxAccess(_C)
if mibBuilder.loadTexts:frmScgPtpPmValidity.setStatus(_A)
_FrmScgPtpPmCmnScgOptMin_Type=FloatHundredths
_FrmScgPtpPmCmnScgOptMin_Object=MibTableColumn
frmScgPtpPmCmnScgOptMin=_FrmScgPtpPmCmnScgOptMin_Object((1,3,6,1,4,1,21296,2,2,2,3,41,2,1,4),_FrmScgPtpPmCmnScgOptMin_Type())
frmScgPtpPmCmnScgOptMin.setMaxAccess(_C)
if mibBuilder.loadTexts:frmScgPtpPmCmnScgOptMin.setStatus(_A)
_FrmScgPtpPmCmnScgOptMax_Type=FloatHundredths
_FrmScgPtpPmCmnScgOptMax_Object=MibTableColumn
frmScgPtpPmCmnScgOptMax=_FrmScgPtpPmCmnScgOptMax_Object((1,3,6,1,4,1,21296,2,2,2,3,41,2,1,5),_FrmScgPtpPmCmnScgOptMax_Type())
frmScgPtpPmCmnScgOptMax.setMaxAccess(_C)
if mibBuilder.loadTexts:frmScgPtpPmCmnScgOptMax.setStatus(_A)
_FrmScgPtpPmCmnScgOptAve_Type=FloatHundredths
_FrmScgPtpPmCmnScgOptAve_Object=MibTableColumn
frmScgPtpPmCmnScgOptAve=_FrmScgPtpPmCmnScgOptAve_Object((1,3,6,1,4,1,21296,2,2,2,3,41,2,1,6),_FrmScgPtpPmCmnScgOptAve_Type())
frmScgPtpPmCmnScgOptAve.setMaxAccess(_C)
if mibBuilder.loadTexts:frmScgPtpPmCmnScgOptAve.setStatus(_A)
_FrmScgPtpPmCmnScgOprMin_Type=FloatHundredths
_FrmScgPtpPmCmnScgOprMin_Object=MibTableColumn
frmScgPtpPmCmnScgOprMin=_FrmScgPtpPmCmnScgOprMin_Object((1,3,6,1,4,1,21296,2,2,2,3,41,2,1,7),_FrmScgPtpPmCmnScgOprMin_Type())
frmScgPtpPmCmnScgOprMin.setMaxAccess(_C)
if mibBuilder.loadTexts:frmScgPtpPmCmnScgOprMin.setStatus(_A)
_FrmScgPtpPmCmnScgOprMax_Type=FloatHundredths
_FrmScgPtpPmCmnScgOprMax_Object=MibTableColumn
frmScgPtpPmCmnScgOprMax=_FrmScgPtpPmCmnScgOprMax_Object((1,3,6,1,4,1,21296,2,2,2,3,41,2,1,8),_FrmScgPtpPmCmnScgOprMax_Type())
frmScgPtpPmCmnScgOprMax.setMaxAccess(_C)
if mibBuilder.loadTexts:frmScgPtpPmCmnScgOprMax.setStatus(_A)
_FrmScgPtpPmCmnScgOprAve_Type=FloatHundredths
_FrmScgPtpPmCmnScgOprAve_Object=MibTableColumn
frmScgPtpPmCmnScgOprAve=_FrmScgPtpPmCmnScgOprAve_Object((1,3,6,1,4,1,21296,2,2,2,3,41,2,1,9),_FrmScgPtpPmCmnScgOprAve_Type())
frmScgPtpPmCmnScgOprAve.setMaxAccess(_C)
if mibBuilder.loadTexts:frmScgPtpPmCmnScgOprAve.setStatus(_A)
_FrmScgPtpPmConformance_ObjectIdentity=ObjectIdentity
frmScgPtpPmConformance=_FrmScgPtpPmConformance_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,3,41,3))
_FrmScgPtpPmCompliances_ObjectIdentity=ObjectIdentity
frmScgPtpPmCompliances=_FrmScgPtpPmCompliances_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,3,41,3,1))
_FrmScgPtpPmGroups_ObjectIdentity=ObjectIdentity
frmScgPtpPmGroups=_FrmScgPtpPmGroups_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,3,41,3,2))
frmScgPtpPmGroup=ObjectGroup((1,3,6,1,4,1,21296,2,2,2,3,41,3,2,1))
frmScgPtpPmGroup.setObjects(*((_B,_H),(_B,_G),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P)))
if mibBuilder.loadTexts:frmScgPtpPmGroup.setStatus(_A)
frmScgPtpPmRealGroup=ObjectGroup((1,3,6,1,4,1,21296,2,2,2,3,41,3,2,2))
frmScgPtpPmRealGroup.setObjects(*((_B,_Q),(_B,_R)))
if mibBuilder.loadTexts:frmScgPtpPmRealGroup.setStatus(_A)
frmScgPtpPmCompliance=ModuleCompliance((1,3,6,1,4,1,21296,2,2,2,3,41,3,1,1))
frmScgPtpPmCompliance.setObjects((_B,_S))
if mibBuilder.loadTexts:frmScgPtpPmCompliance.setStatus(_A)
frmScgPtpPmRealCompliance=ModuleCompliance((1,3,6,1,4,1,21296,2,2,2,3,41,3,1,2))
frmScgPtpPmRealCompliance.setObjects((_B,_T))
if mibBuilder.loadTexts:frmScgPtpPmRealCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'frmScgPtpPmMIB':frmScgPtpPmMIB,'frmScgPtpPmRealTable':frmScgPtpPmRealTable,'frmScgPtpPmRealEntry':frmScgPtpPmRealEntry,_Q:frmScgPtpPmRealCmnScgOpt,_R:frmScgPtpPmRealCmnScgOpr,'frmScgPtpPmTable':frmScgPtpPmTable,'frmScgPtpPmEntry':frmScgPtpPmEntry,_H:frmScgPtpPmTimestamp,_G:frmScgPtpPmSampleDuration,_J:frmScgPtpPmValidity,_K:frmScgPtpPmCmnScgOptMin,_L:frmScgPtpPmCmnScgOptMax,_M:frmScgPtpPmCmnScgOptAve,_N:frmScgPtpPmCmnScgOprMin,_O:frmScgPtpPmCmnScgOprMax,_P:frmScgPtpPmCmnScgOprAve,'frmScgPtpPmConformance':frmScgPtpPmConformance,'frmScgPtpPmCompliances':frmScgPtpPmCompliances,'frmScgPtpPmCompliance':frmScgPtpPmCompliance,'frmScgPtpPmRealCompliance':frmScgPtpPmRealCompliance,'frmScgPtpPmGroups':frmScgPtpPmGroups,_S:frmScgPtpPmGroup,_T:frmScgPtpPmRealGroup})