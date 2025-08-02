_P='opsmPmRealGroup'
_O='opsmPmGroup'
_N='opsmPmRealOpr'
_M='opsmPmOprAve'
_L='opsmPmOprMax'
_K='opsmPmOprMin'
_J='opsmPmValidity'
_I='not-accessible'
_H='opsmPmTimestamp'
_G='opsmPmSampleDuration'
_F='Integer32'
_E='ifIndex'
_D='IF-MIB'
_C='read-only'
_B='INFINERA-PM-OPSM-MIB'
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
opsmPmMIB=ModuleIdentity((1,3,6,1,4,1,21296,2,2,2,3,50))
if mibBuilder.loadTexts:opsmPmMIB.setRevisions(('2015-05-18 00:00',))
_OpsmPmRealTable_Object=MibTable
opsmPmRealTable=_OpsmPmRealTable_Object((1,3,6,1,4,1,21296,2,2,2,3,50,1))
if mibBuilder.loadTexts:opsmPmRealTable.setStatus(_A)
_OpsmPmRealEntry_Object=MibTableRow
opsmPmRealEntry=_OpsmPmRealEntry_Object((1,3,6,1,4,1,21296,2,2,2,3,50,1,1))
opsmPmRealEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:opsmPmRealEntry.setStatus(_A)
_OpsmPmRealOpr_Type=FloatHundredths
_OpsmPmRealOpr_Object=MibTableColumn
opsmPmRealOpr=_OpsmPmRealOpr_Object((1,3,6,1,4,1,21296,2,2,2,3,50,1,1,1),_OpsmPmRealOpr_Type())
opsmPmRealOpr.setMaxAccess(_C)
if mibBuilder.loadTexts:opsmPmRealOpr.setStatus(_A)
_OpsmPmTable_Object=MibTable
opsmPmTable=_OpsmPmTable_Object((1,3,6,1,4,1,21296,2,2,2,3,50,2))
if mibBuilder.loadTexts:opsmPmTable.setStatus(_A)
_OpsmPmEntry_Object=MibTableRow
opsmPmEntry=_OpsmPmEntry_Object((1,3,6,1,4,1,21296,2,2,2,3,50,2,1))
opsmPmEntry.setIndexNames((0,_D,_E),(0,_B,_G),(0,_B,_H))
if mibBuilder.loadTexts:opsmPmEntry.setStatus(_A)
class _OpsmPmTimestamp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_OpsmPmTimestamp_Type.__name__=_F
_OpsmPmTimestamp_Object=MibTableColumn
opsmPmTimestamp=_OpsmPmTimestamp_Object((1,3,6,1,4,1,21296,2,2,2,3,50,2,1,1),_OpsmPmTimestamp_Type())
opsmPmTimestamp.setMaxAccess(_I)
if mibBuilder.loadTexts:opsmPmTimestamp.setStatus(_A)
class _OpsmPmSampleDuration_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('fifteenMinutes',1),('day',2)))
_OpsmPmSampleDuration_Type.__name__=_F
_OpsmPmSampleDuration_Object=MibTableColumn
opsmPmSampleDuration=_OpsmPmSampleDuration_Object((1,3,6,1,4,1,21296,2,2,2,3,50,2,1,2),_OpsmPmSampleDuration_Type())
opsmPmSampleDuration.setMaxAccess(_I)
if mibBuilder.loadTexts:opsmPmSampleDuration.setStatus(_A)
_OpsmPmValidity_Type=TruthValue
_OpsmPmValidity_Object=MibTableColumn
opsmPmValidity=_OpsmPmValidity_Object((1,3,6,1,4,1,21296,2,2,2,3,50,2,1,3),_OpsmPmValidity_Type())
opsmPmValidity.setMaxAccess(_C)
if mibBuilder.loadTexts:opsmPmValidity.setStatus(_A)
_OpsmPmOprMin_Type=FloatHundredths
_OpsmPmOprMin_Object=MibTableColumn
opsmPmOprMin=_OpsmPmOprMin_Object((1,3,6,1,4,1,21296,2,2,2,3,50,2,1,4),_OpsmPmOprMin_Type())
opsmPmOprMin.setMaxAccess(_C)
if mibBuilder.loadTexts:opsmPmOprMin.setStatus(_A)
_OpsmPmOprMax_Type=FloatHundredths
_OpsmPmOprMax_Object=MibTableColumn
opsmPmOprMax=_OpsmPmOprMax_Object((1,3,6,1,4,1,21296,2,2,2,3,50,2,1,5),_OpsmPmOprMax_Type())
opsmPmOprMax.setMaxAccess(_C)
if mibBuilder.loadTexts:opsmPmOprMax.setStatus(_A)
_OpsmPmOprAve_Type=FloatHundredths
_OpsmPmOprAve_Object=MibTableColumn
opsmPmOprAve=_OpsmPmOprAve_Object((1,3,6,1,4,1,21296,2,2,2,3,50,2,1,6),_OpsmPmOprAve_Type())
opsmPmOprAve.setMaxAccess(_C)
if mibBuilder.loadTexts:opsmPmOprAve.setStatus(_A)
_OpsmPmConformance_ObjectIdentity=ObjectIdentity
opsmPmConformance=_OpsmPmConformance_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,3,50,3))
_OpsmPmCompliances_ObjectIdentity=ObjectIdentity
opsmPmCompliances=_OpsmPmCompliances_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,3,50,3,1))
_OpsmPmGroups_ObjectIdentity=ObjectIdentity
opsmPmGroups=_OpsmPmGroups_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,3,50,3,2))
opsmPmGroup=ObjectGroup((1,3,6,1,4,1,21296,2,2,2,3,50,3,2,1))
opsmPmGroup.setObjects(*((_B,_H),(_B,_G),(_B,_J),(_B,_K),(_B,_L),(_B,_M)))
if mibBuilder.loadTexts:opsmPmGroup.setStatus(_A)
opsmPmRealGroup=ObjectGroup((1,3,6,1,4,1,21296,2,2,2,3,50,3,2,2))
opsmPmRealGroup.setObjects((_B,_N))
if mibBuilder.loadTexts:opsmPmRealGroup.setStatus(_A)
opsmPmCompliance=ModuleCompliance((1,3,6,1,4,1,21296,2,2,2,3,50,3,1,1))
opsmPmCompliance.setObjects((_B,_O))
if mibBuilder.loadTexts:opsmPmCompliance.setStatus(_A)
opsmPmRealCompliance=ModuleCompliance((1,3,6,1,4,1,21296,2,2,2,3,50,3,1,2))
opsmPmRealCompliance.setObjects((_B,_P))
if mibBuilder.loadTexts:opsmPmRealCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'opsmPmMIB':opsmPmMIB,'opsmPmRealTable':opsmPmRealTable,'opsmPmRealEntry':opsmPmRealEntry,_N:opsmPmRealOpr,'opsmPmTable':opsmPmTable,'opsmPmEntry':opsmPmEntry,_H:opsmPmTimestamp,_G:opsmPmSampleDuration,_J:opsmPmValidity,_K:opsmPmOprMin,_L:opsmPmOprMax,_M:opsmPmOprAve,'opsmPmConformance':opsmPmConformance,'opsmPmCompliances':opsmPmCompliances,'opsmPmCompliance':opsmPmCompliance,'opsmPmRealCompliance':opsmPmRealCompliance,'opsmPmGroups':opsmPmGroups,_O:opsmPmGroup,_P:opsmPmRealGroup})