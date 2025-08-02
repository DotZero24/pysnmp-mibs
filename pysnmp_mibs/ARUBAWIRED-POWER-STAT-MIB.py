_P='arubaWiredPowerStatTableGroup'
_O='arubaWiredPowerStatPowerConsumedAveragePeriod'
_N='arubaWiredPowerStatPowerConsumedAverage'
_M='arubaWiredPowerStatPowerConsumed'
_L='arubaWiredPowerStatType'
_K='arubaWiredPowerStatName'
_J='RealDecTwo'
_I='arubaWiredPowerStatSlotIndex'
_H='arubaWiredPowerStatTypeIndex'
_G='arubaWiredPowerStatGroupIndex'
_F='not-accessible'
_E='DisplayString'
_D='read-only'
_C='Integer32'
_B='ARUBAWIRED-POWER-STAT-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
arubaWiredChassisMIB,=mibBuilder.importSymbols('ARUBAWIRED-CHASSIS-MIB','arubaWiredChassisMIB')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_E,'PhysAddress','TextualConvention')
arubaWiredPowerStat=ModuleIdentity((1,3,6,1,4,1,47196,4,1,1,3,11,8))
if mibBuilder.loadTexts:arubaWiredPowerStat.setRevisions(('2023-07-25 00:00','2023-06-20 00:00'))
class RealDecTwo(TextualConvention,Integer32):status=_A;displayHint='d-2'
_ArubaWiredPowerStatNotifications_ObjectIdentity=ObjectIdentity
arubaWiredPowerStatNotifications=_ArubaWiredPowerStatNotifications_ObjectIdentity((1,3,6,1,4,1,47196,4,1,1,3,11,8,0))
_ArubaWiredPowerStatObjects_ObjectIdentity=ObjectIdentity
arubaWiredPowerStatObjects=_ArubaWiredPowerStatObjects_ObjectIdentity((1,3,6,1,4,1,47196,4,1,1,3,11,8,1))
_ArubaWiredPowerStatSys_ObjectIdentity=ObjectIdentity
arubaWiredPowerStatSys=_ArubaWiredPowerStatSys_ObjectIdentity((1,3,6,1,4,1,47196,4,1,1,3,11,8,1,0))
_ArubaWiredPowerStatTable_Object=MibTable
arubaWiredPowerStatTable=_ArubaWiredPowerStatTable_Object((1,3,6,1,4,1,47196,4,1,1,3,11,8,1,0,1))
if mibBuilder.loadTexts:arubaWiredPowerStatTable.setStatus(_A)
_ArubaWiredPowerStatEntry_Object=MibTableRow
arubaWiredPowerStatEntry=_ArubaWiredPowerStatEntry_Object((1,3,6,1,4,1,47196,4,1,1,3,11,8,1,0,1,1))
arubaWiredPowerStatEntry.setIndexNames((0,_B,_G),(0,_B,_H),(0,_B,_I))
if mibBuilder.loadTexts:arubaWiredPowerStatEntry.setStatus(_A)
class _ArubaWiredPowerStatGroupIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_ArubaWiredPowerStatGroupIndex_Type.__name__=_C
_ArubaWiredPowerStatGroupIndex_Object=MibTableColumn
arubaWiredPowerStatGroupIndex=_ArubaWiredPowerStatGroupIndex_Object((1,3,6,1,4,1,47196,4,1,1,3,11,8,1,0,1,1,1),_ArubaWiredPowerStatGroupIndex_Type())
arubaWiredPowerStatGroupIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:arubaWiredPowerStatGroupIndex.setStatus(_A)
class _ArubaWiredPowerStatTypeIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_ArubaWiredPowerStatTypeIndex_Type.__name__=_C
_ArubaWiredPowerStatTypeIndex_Object=MibTableColumn
arubaWiredPowerStatTypeIndex=_ArubaWiredPowerStatTypeIndex_Object((1,3,6,1,4,1,47196,4,1,1,3,11,8,1,0,1,1,2),_ArubaWiredPowerStatTypeIndex_Type())
arubaWiredPowerStatTypeIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:arubaWiredPowerStatTypeIndex.setStatus(_A)
class _ArubaWiredPowerStatSlotIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_ArubaWiredPowerStatSlotIndex_Type.__name__=_C
_ArubaWiredPowerStatSlotIndex_Object=MibTableColumn
arubaWiredPowerStatSlotIndex=_ArubaWiredPowerStatSlotIndex_Object((1,3,6,1,4,1,47196,4,1,1,3,11,8,1,0,1,1,3),_ArubaWiredPowerStatSlotIndex_Type())
arubaWiredPowerStatSlotIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:arubaWiredPowerStatSlotIndex.setStatus(_A)
class _ArubaWiredPowerStatName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_ArubaWiredPowerStatName_Type.__name__=_E
_ArubaWiredPowerStatName_Object=MibTableColumn
arubaWiredPowerStatName=_ArubaWiredPowerStatName_Object((1,3,6,1,4,1,47196,4,1,1,3,11,8,1,0,1,1,4),_ArubaWiredPowerStatName_Type())
arubaWiredPowerStatName.setMaxAccess(_D)
if mibBuilder.loadTexts:arubaWiredPowerStatName.setStatus(_A)
class _ArubaWiredPowerStatType_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_ArubaWiredPowerStatType_Type.__name__=_E
_ArubaWiredPowerStatType_Object=MibTableColumn
arubaWiredPowerStatType=_ArubaWiredPowerStatType_Object((1,3,6,1,4,1,47196,4,1,1,3,11,8,1,0,1,1,5),_ArubaWiredPowerStatType_Type())
arubaWiredPowerStatType.setMaxAccess(_D)
if mibBuilder.loadTexts:arubaWiredPowerStatType.setStatus(_A)
class _ArubaWiredPowerStatPowerConsumed_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_ArubaWiredPowerStatPowerConsumed_Type.__name__=_C
_ArubaWiredPowerStatPowerConsumed_Object=MibTableColumn
arubaWiredPowerStatPowerConsumed=_ArubaWiredPowerStatPowerConsumed_Object((1,3,6,1,4,1,47196,4,1,1,3,11,8,1,0,1,1,6),_ArubaWiredPowerStatPowerConsumed_Type())
arubaWiredPowerStatPowerConsumed.setMaxAccess(_D)
if mibBuilder.loadTexts:arubaWiredPowerStatPowerConsumed.setStatus(_A)
if mibBuilder.loadTexts:arubaWiredPowerStatPowerConsumed.setUnits('Watts')
class _ArubaWiredPowerStatPowerConsumedAverage_Type(RealDecTwo):defaultValue=0
_ArubaWiredPowerStatPowerConsumedAverage_Type.__name__=_J
_ArubaWiredPowerStatPowerConsumedAverage_Object=MibTableColumn
arubaWiredPowerStatPowerConsumedAverage=_ArubaWiredPowerStatPowerConsumedAverage_Object((1,3,6,1,4,1,47196,4,1,1,3,11,8,1,0,1,1,7),_ArubaWiredPowerStatPowerConsumedAverage_Type())
arubaWiredPowerStatPowerConsumedAverage.setMaxAccess(_D)
if mibBuilder.loadTexts:arubaWiredPowerStatPowerConsumedAverage.setStatus(_A)
if mibBuilder.loadTexts:arubaWiredPowerStatPowerConsumedAverage.setUnits('Watts')
class _ArubaWiredPowerStatPowerConsumedAveragePeriod_Type(Integer32):defaultValue=600;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(60,3600))
_ArubaWiredPowerStatPowerConsumedAveragePeriod_Type.__name__=_C
_ArubaWiredPowerStatPowerConsumedAveragePeriod_Object=MibTableColumn
arubaWiredPowerStatPowerConsumedAveragePeriod=_ArubaWiredPowerStatPowerConsumedAveragePeriod_Object((1,3,6,1,4,1,47196,4,1,1,3,11,8,1,0,1,1,8),_ArubaWiredPowerStatPowerConsumedAveragePeriod_Type())
arubaWiredPowerStatPowerConsumedAveragePeriod.setMaxAccess('read-write')
if mibBuilder.loadTexts:arubaWiredPowerStatPowerConsumedAveragePeriod.setStatus(_A)
if mibBuilder.loadTexts:arubaWiredPowerStatPowerConsumedAveragePeriod.setUnits('seconds')
_ArubaWiredPowerStatConformance_ObjectIdentity=ObjectIdentity
arubaWiredPowerStatConformance=_ArubaWiredPowerStatConformance_ObjectIdentity((1,3,6,1,4,1,47196,4,1,1,3,11,8,2))
_ArubaWiredPowerStatCompliances_ObjectIdentity=ObjectIdentity
arubaWiredPowerStatCompliances=_ArubaWiredPowerStatCompliances_ObjectIdentity((1,3,6,1,4,1,47196,4,1,1,3,11,8,2,1))
_ArubaWiredPowerStatGroups_ObjectIdentity=ObjectIdentity
arubaWiredPowerStatGroups=_ArubaWiredPowerStatGroups_ObjectIdentity((1,3,6,1,4,1,47196,4,1,1,3,11,8,2,2))
arubaWiredPowerStatTableGroup=ObjectGroup((1,3,6,1,4,1,47196,4,1,1,3,11,8,2,2,1))
arubaWiredPowerStatTableGroup.setObjects(*((_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O)))
if mibBuilder.loadTexts:arubaWiredPowerStatTableGroup.setStatus(_A)
arubaWiredPowerStatCompliance=ModuleCompliance((1,3,6,1,4,1,47196,4,1,1,3,11,8,2,1,1))
arubaWiredPowerStatCompliance.setObjects((_B,_P))
if mibBuilder.loadTexts:arubaWiredPowerStatCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{_J:RealDecTwo,'arubaWiredPowerStat':arubaWiredPowerStat,'arubaWiredPowerStatNotifications':arubaWiredPowerStatNotifications,'arubaWiredPowerStatObjects':arubaWiredPowerStatObjects,'arubaWiredPowerStatSys':arubaWiredPowerStatSys,'arubaWiredPowerStatTable':arubaWiredPowerStatTable,'arubaWiredPowerStatEntry':arubaWiredPowerStatEntry,_G:arubaWiredPowerStatGroupIndex,_H:arubaWiredPowerStatTypeIndex,_I:arubaWiredPowerStatSlotIndex,_K:arubaWiredPowerStatName,_L:arubaWiredPowerStatType,_M:arubaWiredPowerStatPowerConsumed,_N:arubaWiredPowerStatPowerConsumedAverage,_O:arubaWiredPowerStatPowerConsumedAveragePeriod,'arubaWiredPowerStatConformance':arubaWiredPowerStatConformance,'arubaWiredPowerStatCompliances':arubaWiredPowerStatCompliances,'arubaWiredPowerStatCompliance':arubaWiredPowerStatCompliance,'arubaWiredPowerStatGroups':arubaWiredPowerStatGroups,_P:arubaWiredPowerStatTableGroup})