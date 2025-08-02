_P='chassisPmRealGroup'
_O='chassisPmGroup'
_N='chassisPmRealInPRaw'
_M='chassisPmInPAvg'
_L='chassisPmInPMax'
_K='chassisPmInPMin'
_J='chassisPmValidity'
_I='not-accessible'
_H='chassisPmTimestamp'
_G='chassisPmSampleDuration'
_F='Integer32'
_E='ifIndex'
_D='IF-MIB'
_C='read-only'
_B='INFINERA-PM-CHASSIS-MIB'
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
chassisPmMIB=ModuleIdentity((1,3,6,1,4,1,21296,2,2,2,3,51))
if mibBuilder.loadTexts:chassisPmMIB.setRevisions(('2015-05-18 00:00',))
_ChassisPmRealTable_Object=MibTable
chassisPmRealTable=_ChassisPmRealTable_Object((1,3,6,1,4,1,21296,2,2,2,3,51,1))
if mibBuilder.loadTexts:chassisPmRealTable.setStatus(_A)
_ChassisPmRealEntry_Object=MibTableRow
chassisPmRealEntry=_ChassisPmRealEntry_Object((1,3,6,1,4,1,21296,2,2,2,3,51,1,1))
chassisPmRealEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:chassisPmRealEntry.setStatus(_A)
_ChassisPmRealInPRaw_Type=FloatHundredths
_ChassisPmRealInPRaw_Object=MibTableColumn
chassisPmRealInPRaw=_ChassisPmRealInPRaw_Object((1,3,6,1,4,1,21296,2,2,2,3,51,1,1,1),_ChassisPmRealInPRaw_Type())
chassisPmRealInPRaw.setMaxAccess(_C)
if mibBuilder.loadTexts:chassisPmRealInPRaw.setStatus(_A)
_ChassisPmTable_Object=MibTable
chassisPmTable=_ChassisPmTable_Object((1,3,6,1,4,1,21296,2,2,2,3,51,2))
if mibBuilder.loadTexts:chassisPmTable.setStatus(_A)
_ChassisPmEntry_Object=MibTableRow
chassisPmEntry=_ChassisPmEntry_Object((1,3,6,1,4,1,21296,2,2,2,3,51,2,1))
chassisPmEntry.setIndexNames((0,_D,_E),(0,_B,_G),(0,_B,_H))
if mibBuilder.loadTexts:chassisPmEntry.setStatus(_A)
class _ChassisPmTimestamp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_ChassisPmTimestamp_Type.__name__=_F
_ChassisPmTimestamp_Object=MibTableColumn
chassisPmTimestamp=_ChassisPmTimestamp_Object((1,3,6,1,4,1,21296,2,2,2,3,51,2,1,1),_ChassisPmTimestamp_Type())
chassisPmTimestamp.setMaxAccess(_I)
if mibBuilder.loadTexts:chassisPmTimestamp.setStatus(_A)
class _ChassisPmSampleDuration_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('fifteenMinutes',1),('day',2)))
_ChassisPmSampleDuration_Type.__name__=_F
_ChassisPmSampleDuration_Object=MibTableColumn
chassisPmSampleDuration=_ChassisPmSampleDuration_Object((1,3,6,1,4,1,21296,2,2,2,3,51,2,1,2),_ChassisPmSampleDuration_Type())
chassisPmSampleDuration.setMaxAccess(_I)
if mibBuilder.loadTexts:chassisPmSampleDuration.setStatus(_A)
_ChassisPmValidity_Type=TruthValue
_ChassisPmValidity_Object=MibTableColumn
chassisPmValidity=_ChassisPmValidity_Object((1,3,6,1,4,1,21296,2,2,2,3,51,2,1,3),_ChassisPmValidity_Type())
chassisPmValidity.setMaxAccess(_C)
if mibBuilder.loadTexts:chassisPmValidity.setStatus(_A)
_ChassisPmInPMin_Type=FloatHundredths
_ChassisPmInPMin_Object=MibTableColumn
chassisPmInPMin=_ChassisPmInPMin_Object((1,3,6,1,4,1,21296,2,2,2,3,51,2,1,4),_ChassisPmInPMin_Type())
chassisPmInPMin.setMaxAccess(_C)
if mibBuilder.loadTexts:chassisPmInPMin.setStatus(_A)
_ChassisPmInPMax_Type=FloatHundredths
_ChassisPmInPMax_Object=MibTableColumn
chassisPmInPMax=_ChassisPmInPMax_Object((1,3,6,1,4,1,21296,2,2,2,3,51,2,1,5),_ChassisPmInPMax_Type())
chassisPmInPMax.setMaxAccess(_C)
if mibBuilder.loadTexts:chassisPmInPMax.setStatus(_A)
_ChassisPmInPAvg_Type=FloatHundredths
_ChassisPmInPAvg_Object=MibTableColumn
chassisPmInPAvg=_ChassisPmInPAvg_Object((1,3,6,1,4,1,21296,2,2,2,3,51,2,1,6),_ChassisPmInPAvg_Type())
chassisPmInPAvg.setMaxAccess(_C)
if mibBuilder.loadTexts:chassisPmInPAvg.setStatus(_A)
_ChassisPmConformance_ObjectIdentity=ObjectIdentity
chassisPmConformance=_ChassisPmConformance_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,3,51,3))
_ChassisPmCompliances_ObjectIdentity=ObjectIdentity
chassisPmCompliances=_ChassisPmCompliances_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,3,51,3,1))
_ChassisPmGroups_ObjectIdentity=ObjectIdentity
chassisPmGroups=_ChassisPmGroups_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,3,51,3,2))
chassisPmGroup=ObjectGroup((1,3,6,1,4,1,21296,2,2,2,3,51,3,2,1))
chassisPmGroup.setObjects(*((_B,_H),(_B,_G),(_B,_J),(_B,_K),(_B,_L),(_B,_M)))
if mibBuilder.loadTexts:chassisPmGroup.setStatus(_A)
chassisPmRealGroup=ObjectGroup((1,3,6,1,4,1,21296,2,2,2,3,51,3,2,2))
chassisPmRealGroup.setObjects((_B,_N))
if mibBuilder.loadTexts:chassisPmRealGroup.setStatus(_A)
chassisPmCompliance=ModuleCompliance((1,3,6,1,4,1,21296,2,2,2,3,51,3,1,1))
chassisPmCompliance.setObjects((_B,_O))
if mibBuilder.loadTexts:chassisPmCompliance.setStatus(_A)
chassisPmRealCompliance=ModuleCompliance((1,3,6,1,4,1,21296,2,2,2,3,51,3,1,2))
chassisPmRealCompliance.setObjects((_B,_P))
if mibBuilder.loadTexts:chassisPmRealCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'chassisPmMIB':chassisPmMIB,'chassisPmRealTable':chassisPmRealTable,'chassisPmRealEntry':chassisPmRealEntry,_N:chassisPmRealInPRaw,'chassisPmTable':chassisPmTable,'chassisPmEntry':chassisPmEntry,_H:chassisPmTimestamp,_G:chassisPmSampleDuration,_J:chassisPmValidity,_K:chassisPmInPMin,_L:chassisPmInPMax,_M:chassisPmInPAvg,'chassisPmConformance':chassisPmConformance,'chassisPmCompliances':chassisPmCompliances,'chassisPmCompliance':chassisPmCompliance,'chassisPmRealCompliance':chassisPmRealCompliance,'chassisPmGroups':chassisPmGroups,_O:chassisPmGroup,_P:chassisPmRealGroup})