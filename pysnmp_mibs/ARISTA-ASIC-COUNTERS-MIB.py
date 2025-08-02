_R='aristaAsicCountersMibDropTableGroup'
_Q='aristaAsicCountersMibDropScalarGroup'
_P='aristaAsicInternalDropStatsLastTime'
_O='aristaAsicInternalDropStatsFirstTime'
_N='aristaAsicInternalDropStats1Week'
_M='aristaAsicInternalDropStats1Day'
_L='aristaAsicInternalDropStats1Hr'
_K='aristaAsicInternalDropStats10Min'
_J='aristaAsicInternalDropStats1Min'
_I='aristaAsicInternalDropStatsCount'
_H='aristaAsicInternalDropStatsRatesSupported'
_G='not-accessible'
_F='aristaAsicInternalDropStatsCounterName'
_E='aristaAsicInternalDropStatsChipName'
_D='DisplayString'
_C='read-only'
_B='ARISTA-ASIC-COUNTERS-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
aristaMibs,=mibBuilder.importSymbols('ARISTA-SMI-MIB','aristaMibs')
CounterBasedGauge64,=mibBuilder.importSymbols('HCNUM-TC','CounterBasedGauge64')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TimeStamp=mibBuilder.importSymbols('SNMPv2-TC',_D,'PhysAddress','TextualConvention','TimeStamp')
aristaAsicCountersMIB=ModuleIdentity((1,3,6,1,4,1,30065,3,29))
if mibBuilder.loadTexts:aristaAsicCountersMIB.setRevisions(('2021-02-03 00:00',))
_AristaAsicCountersMibNotifications_ObjectIdentity=ObjectIdentity
aristaAsicCountersMibNotifications=_AristaAsicCountersMibNotifications_ObjectIdentity((1,3,6,1,4,1,30065,3,29,0))
_AristaAsicCountersMibObjects_ObjectIdentity=ObjectIdentity
aristaAsicCountersMibObjects=_AristaAsicCountersMibObjects_ObjectIdentity((1,3,6,1,4,1,30065,3,29,1))
class _AristaAsicInternalDropStatsRatesSupported_Type(Bits):namedValues=NamedValues(*(('last1Min',0),('last10Min',1),('last1Hr',2),('last1Day',3),('last1Week',4)))
_AristaAsicInternalDropStatsRatesSupported_Type.__name__='Bits'
_AristaAsicInternalDropStatsRatesSupported_Object=MibScalar
aristaAsicInternalDropStatsRatesSupported=_AristaAsicInternalDropStatsRatesSupported_Object((1,3,6,1,4,1,30065,3,29,1,1),_AristaAsicInternalDropStatsRatesSupported_Type())
aristaAsicInternalDropStatsRatesSupported.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaAsicInternalDropStatsRatesSupported.setStatus(_A)
_AristaAsicInternalDropStatsTable_Object=MibTable
aristaAsicInternalDropStatsTable=_AristaAsicInternalDropStatsTable_Object((1,3,6,1,4,1,30065,3,29,1,2))
if mibBuilder.loadTexts:aristaAsicInternalDropStatsTable.setStatus(_A)
_AristaAsicInternalDropStatsEntry_Object=MibTableRow
aristaAsicInternalDropStatsEntry=_AristaAsicInternalDropStatsEntry_Object((1,3,6,1,4,1,30065,3,29,1,2,1))
aristaAsicInternalDropStatsEntry.setIndexNames((0,_B,_E),(0,_B,_F))
if mibBuilder.loadTexts:aristaAsicInternalDropStatsEntry.setStatus(_A)
class _AristaAsicInternalDropStatsChipName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_AristaAsicInternalDropStatsChipName_Type.__name__=_D
_AristaAsicInternalDropStatsChipName_Object=MibTableColumn
aristaAsicInternalDropStatsChipName=_AristaAsicInternalDropStatsChipName_Object((1,3,6,1,4,1,30065,3,29,1,2,1,1),_AristaAsicInternalDropStatsChipName_Type())
aristaAsicInternalDropStatsChipName.setMaxAccess(_G)
if mibBuilder.loadTexts:aristaAsicInternalDropStatsChipName.setStatus(_A)
class _AristaAsicInternalDropStatsCounterName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_AristaAsicInternalDropStatsCounterName_Type.__name__=_D
_AristaAsicInternalDropStatsCounterName_Object=MibTableColumn
aristaAsicInternalDropStatsCounterName=_AristaAsicInternalDropStatsCounterName_Object((1,3,6,1,4,1,30065,3,29,1,2,1,2),_AristaAsicInternalDropStatsCounterName_Type())
aristaAsicInternalDropStatsCounterName.setMaxAccess(_G)
if mibBuilder.loadTexts:aristaAsicInternalDropStatsCounterName.setStatus(_A)
_AristaAsicInternalDropStatsCount_Type=Counter64
_AristaAsicInternalDropStatsCount_Object=MibTableColumn
aristaAsicInternalDropStatsCount=_AristaAsicInternalDropStatsCount_Object((1,3,6,1,4,1,30065,3,29,1,2,1,3),_AristaAsicInternalDropStatsCount_Type())
aristaAsicInternalDropStatsCount.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaAsicInternalDropStatsCount.setStatus(_A)
_AristaAsicInternalDropStats1Min_Type=CounterBasedGauge64
_AristaAsicInternalDropStats1Min_Object=MibTableColumn
aristaAsicInternalDropStats1Min=_AristaAsicInternalDropStats1Min_Object((1,3,6,1,4,1,30065,3,29,1,2,1,4),_AristaAsicInternalDropStats1Min_Type())
aristaAsicInternalDropStats1Min.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaAsicInternalDropStats1Min.setStatus(_A)
_AristaAsicInternalDropStats10Min_Type=CounterBasedGauge64
_AristaAsicInternalDropStats10Min_Object=MibTableColumn
aristaAsicInternalDropStats10Min=_AristaAsicInternalDropStats10Min_Object((1,3,6,1,4,1,30065,3,29,1,2,1,5),_AristaAsicInternalDropStats10Min_Type())
aristaAsicInternalDropStats10Min.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaAsicInternalDropStats10Min.setStatus(_A)
_AristaAsicInternalDropStats1Hr_Type=CounterBasedGauge64
_AristaAsicInternalDropStats1Hr_Object=MibTableColumn
aristaAsicInternalDropStats1Hr=_AristaAsicInternalDropStats1Hr_Object((1,3,6,1,4,1,30065,3,29,1,2,1,6),_AristaAsicInternalDropStats1Hr_Type())
aristaAsicInternalDropStats1Hr.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaAsicInternalDropStats1Hr.setStatus(_A)
_AristaAsicInternalDropStats1Day_Type=CounterBasedGauge64
_AristaAsicInternalDropStats1Day_Object=MibTableColumn
aristaAsicInternalDropStats1Day=_AristaAsicInternalDropStats1Day_Object((1,3,6,1,4,1,30065,3,29,1,2,1,7),_AristaAsicInternalDropStats1Day_Type())
aristaAsicInternalDropStats1Day.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaAsicInternalDropStats1Day.setStatus(_A)
_AristaAsicInternalDropStats1Week_Type=CounterBasedGauge64
_AristaAsicInternalDropStats1Week_Object=MibTableColumn
aristaAsicInternalDropStats1Week=_AristaAsicInternalDropStats1Week_Object((1,3,6,1,4,1,30065,3,29,1,2,1,8),_AristaAsicInternalDropStats1Week_Type())
aristaAsicInternalDropStats1Week.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaAsicInternalDropStats1Week.setStatus(_A)
_AristaAsicInternalDropStatsFirstTime_Type=TimeStamp
_AristaAsicInternalDropStatsFirstTime_Object=MibTableColumn
aristaAsicInternalDropStatsFirstTime=_AristaAsicInternalDropStatsFirstTime_Object((1,3,6,1,4,1,30065,3,29,1,2,1,9),_AristaAsicInternalDropStatsFirstTime_Type())
aristaAsicInternalDropStatsFirstTime.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaAsicInternalDropStatsFirstTime.setStatus(_A)
_AristaAsicInternalDropStatsLastTime_Type=TimeStamp
_AristaAsicInternalDropStatsLastTime_Object=MibTableColumn
aristaAsicInternalDropStatsLastTime=_AristaAsicInternalDropStatsLastTime_Object((1,3,6,1,4,1,30065,3,29,1,2,1,10),_AristaAsicInternalDropStatsLastTime_Type())
aristaAsicInternalDropStatsLastTime.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaAsicInternalDropStatsLastTime.setStatus(_A)
_AristaAsicCountersMibConformance_ObjectIdentity=ObjectIdentity
aristaAsicCountersMibConformance=_AristaAsicCountersMibConformance_ObjectIdentity((1,3,6,1,4,1,30065,3,29,2))
_AristaAsicCountersMibCompliances_ObjectIdentity=ObjectIdentity
aristaAsicCountersMibCompliances=_AristaAsicCountersMibCompliances_ObjectIdentity((1,3,6,1,4,1,30065,3,29,2,1))
_AristaAsicCountersMibGroups_ObjectIdentity=ObjectIdentity
aristaAsicCountersMibGroups=_AristaAsicCountersMibGroups_ObjectIdentity((1,3,6,1,4,1,30065,3,29,2,2))
aristaAsicCountersMibDropScalarGroup=ObjectGroup((1,3,6,1,4,1,30065,3,29,2,2,1))
aristaAsicCountersMibDropScalarGroup.setObjects((_B,_H))
if mibBuilder.loadTexts:aristaAsicCountersMibDropScalarGroup.setStatus(_A)
aristaAsicCountersMibDropTableGroup=ObjectGroup((1,3,6,1,4,1,30065,3,29,2,2,2))
aristaAsicCountersMibDropTableGroup.setObjects(*((_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P)))
if mibBuilder.loadTexts:aristaAsicCountersMibDropTableGroup.setStatus(_A)
aristaAsicCountersMibCompliance=ModuleCompliance((1,3,6,1,4,1,30065,3,29,2,1,1))
aristaAsicCountersMibCompliance.setObjects(*((_B,_Q),(_B,_R)))
if mibBuilder.loadTexts:aristaAsicCountersMibCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'aristaAsicCountersMIB':aristaAsicCountersMIB,'aristaAsicCountersMibNotifications':aristaAsicCountersMibNotifications,'aristaAsicCountersMibObjects':aristaAsicCountersMibObjects,_H:aristaAsicInternalDropStatsRatesSupported,'aristaAsicInternalDropStatsTable':aristaAsicInternalDropStatsTable,'aristaAsicInternalDropStatsEntry':aristaAsicInternalDropStatsEntry,_E:aristaAsicInternalDropStatsChipName,_F:aristaAsicInternalDropStatsCounterName,_I:aristaAsicInternalDropStatsCount,_J:aristaAsicInternalDropStats1Min,_K:aristaAsicInternalDropStats10Min,_L:aristaAsicInternalDropStats1Hr,_M:aristaAsicInternalDropStats1Day,_N:aristaAsicInternalDropStats1Week,_O:aristaAsicInternalDropStatsFirstTime,_P:aristaAsicInternalDropStatsLastTime,'aristaAsicCountersMibConformance':aristaAsicCountersMibConformance,'aristaAsicCountersMibCompliances':aristaAsicCountersMibCompliances,'aristaAsicCountersMibCompliance':aristaAsicCountersMibCompliance,'aristaAsicCountersMibGroups':aristaAsicCountersMibGroups,_Q:aristaAsicCountersMibDropScalarGroup,_R:aristaAsicCountersMibDropTableGroup})