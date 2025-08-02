_v='cePfeMIBTotalGroup'
_u='cePfeMIBIntervalGroup'
_t='cePfeMIBHistEventGroup'
_s='cePfeMIBHistGroup'
_r='cePfeMIBCurrentGroup'
_q='cePfeMIBPerformanceGroup'
_p='cePfeHistRestartEvent'
_o='cePfeHistThldEvent'
_n='cePfeHistTimeStamp'
_m='cePfePerfTotalEfficiency'
_l='cePfePerfTotalUtilization'
_k='cePfePerfIntervalEfficiency'
_j='cePfePerfIntervalUtilization'
_i='cePfePerfCurrent5MinEfficiency'
_h='cePfePerfCurrent5MinUtilization'
_g='cePfePerfCurrent1MinEfficiency'
_f='cePfePerfCurrent1MinUtilization'
_e='cePfePerfCurrentEfficiency'
_d='cePfePerfCurrentUtilization'
_c='cePfePerfConfigThld5MinEfficiency'
_b='cePfePerfConfigThld5MinUtilization'
_a='cePfePerfConfigThld1MinEfficiency'
_Z='cePfePerfConfigThld1MinUtilization'
_Y='cePfePerfConfigThldEfficiency'
_X='cePfePerfConfigThldUtilization'
_W='cePfePerfConfigValidIntervals'
_V='cePfePerfConfigTimeElapsed'
_U='cePfeHistNotifiesEnable'
_T='cePfeHistTableLastIndex'
_S='cePfeHistTableSize'
_R='cePfePerfCurrentEntry'
_Q='cePfeHistIndex'
_P='EventType'
_O='not-accessible'
_N='cePfePerfIntervalNumber'
_M='cePfeHistRestartReason'
_L='cePfeHistValue'
_K='cePfeHistThld'
_J='cePfeHistType'
_I='cePfeHistEntPhysIndex'
_H='entPhysicalIndex'
_G='ENTITY-MIB'
_F='Percentage'
_E='Unsigned32'
_D='read-write'
_C='read-only'
_B='CISCO-ENTITY-PFE-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
PhysicalIndex,entPhysicalIndex=mibBuilder.importSymbols(_G,'PhysicalIndex',_H)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_E,'iso')
DisplayString,PhysAddress,TextualConvention,TimeStamp=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TimeStamp')
ciscoEntityPfeMib=ModuleIdentity((1,3,6,1,4,1,9,9,265))
if mibBuilder.loadTexts:ciscoEntityPfeMib.setRevisions(('2002-11-27 16:00',))
class CurrentUtilization(TextualConvention,Gauge32):status=_A;subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
class CurrentEfficiency(TextualConvention,Gauge32):status=_A;subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
class IntervalUtilization(TextualConvention,Gauge32):status=_A;subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
class IntervalEfficiency(TextualConvention,Gauge32):status=_A;subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
class TotalUtilization(TextualConvention,Gauge32):status=_A;subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
class TotalEfficiency(TextualConvention,Gauge32):status=_A;subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
class Percentage(TextualConvention,Unsigned32):status=_A;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
class EventType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('none',1),('log',2),('notify',3),('logAndNotify',4)))
class HistEventType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('thldUtilizationEvent',1),('thldEfficiencyEvent',2),('thld1MinUtilizationEvent',3),('thld1MinEfficiencyEvent',4),('thld5MinUtilizationEvent',5),('thld5MinEfficiencyEvent',6),('restartEvent',7)))
_CePfeMIBNotifications_ObjectIdentity=ObjectIdentity
cePfeMIBNotifications=_CePfeMIBNotifications_ObjectIdentity((1,3,6,1,4,1,9,9,265,0))
_CePfeMIBObjects_ObjectIdentity=ObjectIdentity
cePfeMIBObjects=_CePfeMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,265,1))
_CePfePerformance_ObjectIdentity=ObjectIdentity
cePfePerformance=_CePfePerformance_ObjectIdentity((1,3,6,1,4,1,9,9,265,1,1))
_CePfePerfConfigTable_Object=MibTable
cePfePerfConfigTable=_CePfePerfConfigTable_Object((1,3,6,1,4,1,9,9,265,1,1,1))
if mibBuilder.loadTexts:cePfePerfConfigTable.setStatus(_A)
_CePfePerfConfigEntry_Object=MibTableRow
cePfePerfConfigEntry=_CePfePerfConfigEntry_Object((1,3,6,1,4,1,9,9,265,1,1,1,1))
cePfePerfConfigEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:cePfePerfConfigEntry.setStatus(_A)
class _CePfePerfConfigTimeElapsed_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,899))
_CePfePerfConfigTimeElapsed_Type.__name__=_E
_CePfePerfConfigTimeElapsed_Object=MibTableColumn
cePfePerfConfigTimeElapsed=_CePfePerfConfigTimeElapsed_Object((1,3,6,1,4,1,9,9,265,1,1,1,1,1),_CePfePerfConfigTimeElapsed_Type())
cePfePerfConfigTimeElapsed.setMaxAccess(_C)
if mibBuilder.loadTexts:cePfePerfConfigTimeElapsed.setStatus(_A)
if mibBuilder.loadTexts:cePfePerfConfigTimeElapsed.setUnits('seconds')
class _CePfePerfConfigValidIntervals_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,96))
_CePfePerfConfigValidIntervals_Type.__name__=_E
_CePfePerfConfigValidIntervals_Object=MibTableColumn
cePfePerfConfigValidIntervals=_CePfePerfConfigValidIntervals_Object((1,3,6,1,4,1,9,9,265,1,1,1,1,2),_CePfePerfConfigValidIntervals_Type())
cePfePerfConfigValidIntervals.setMaxAccess(_C)
if mibBuilder.loadTexts:cePfePerfConfigValidIntervals.setStatus(_A)
class _CePfePerfConfigThldUtilization_Type(Percentage):defaultValue=0
_CePfePerfConfigThldUtilization_Type.__name__=_F
_CePfePerfConfigThldUtilization_Object=MibTableColumn
cePfePerfConfigThldUtilization=_CePfePerfConfigThldUtilization_Object((1,3,6,1,4,1,9,9,265,1,1,1,1,3),_CePfePerfConfigThldUtilization_Type())
cePfePerfConfigThldUtilization.setMaxAccess(_D)
if mibBuilder.loadTexts:cePfePerfConfigThldUtilization.setStatus(_A)
class _CePfePerfConfigThldEfficiency_Type(Percentage):defaultValue=0
_CePfePerfConfigThldEfficiency_Type.__name__=_F
_CePfePerfConfigThldEfficiency_Object=MibTableColumn
cePfePerfConfigThldEfficiency=_CePfePerfConfigThldEfficiency_Object((1,3,6,1,4,1,9,9,265,1,1,1,1,4),_CePfePerfConfigThldEfficiency_Type())
cePfePerfConfigThldEfficiency.setMaxAccess(_D)
if mibBuilder.loadTexts:cePfePerfConfigThldEfficiency.setStatus(_A)
class _CePfePerfConfigThld1MinUtilization_Type(Percentage):defaultValue=0
_CePfePerfConfigThld1MinUtilization_Type.__name__=_F
_CePfePerfConfigThld1MinUtilization_Object=MibTableColumn
cePfePerfConfigThld1MinUtilization=_CePfePerfConfigThld1MinUtilization_Object((1,3,6,1,4,1,9,9,265,1,1,1,1,5),_CePfePerfConfigThld1MinUtilization_Type())
cePfePerfConfigThld1MinUtilization.setMaxAccess(_D)
if mibBuilder.loadTexts:cePfePerfConfigThld1MinUtilization.setStatus(_A)
class _CePfePerfConfigThld1MinEfficiency_Type(Percentage):defaultValue=0
_CePfePerfConfigThld1MinEfficiency_Type.__name__=_F
_CePfePerfConfigThld1MinEfficiency_Object=MibTableColumn
cePfePerfConfigThld1MinEfficiency=_CePfePerfConfigThld1MinEfficiency_Object((1,3,6,1,4,1,9,9,265,1,1,1,1,6),_CePfePerfConfigThld1MinEfficiency_Type())
cePfePerfConfigThld1MinEfficiency.setMaxAccess(_D)
if mibBuilder.loadTexts:cePfePerfConfigThld1MinEfficiency.setStatus(_A)
class _CePfePerfConfigThld5MinUtilization_Type(Percentage):defaultValue=0
_CePfePerfConfigThld5MinUtilization_Type.__name__=_F
_CePfePerfConfigThld5MinUtilization_Object=MibTableColumn
cePfePerfConfigThld5MinUtilization=_CePfePerfConfigThld5MinUtilization_Object((1,3,6,1,4,1,9,9,265,1,1,1,1,7),_CePfePerfConfigThld5MinUtilization_Type())
cePfePerfConfigThld5MinUtilization.setMaxAccess(_D)
if mibBuilder.loadTexts:cePfePerfConfigThld5MinUtilization.setStatus(_A)
class _CePfePerfConfigThld5MinEfficiency_Type(Percentage):defaultValue=0
_CePfePerfConfigThld5MinEfficiency_Type.__name__=_F
_CePfePerfConfigThld5MinEfficiency_Object=MibTableColumn
cePfePerfConfigThld5MinEfficiency=_CePfePerfConfigThld5MinEfficiency_Object((1,3,6,1,4,1,9,9,265,1,1,1,1,8),_CePfePerfConfigThld5MinEfficiency_Type())
cePfePerfConfigThld5MinEfficiency.setMaxAccess(_D)
if mibBuilder.loadTexts:cePfePerfConfigThld5MinEfficiency.setStatus(_A)
_CePfePerfCurrentTable_Object=MibTable
cePfePerfCurrentTable=_CePfePerfCurrentTable_Object((1,3,6,1,4,1,9,9,265,1,1,2))
if mibBuilder.loadTexts:cePfePerfCurrentTable.setStatus(_A)
_CePfePerfCurrentEntry_Object=MibTableRow
cePfePerfCurrentEntry=_CePfePerfCurrentEntry_Object((1,3,6,1,4,1,9,9,265,1,1,2,1))
if mibBuilder.loadTexts:cePfePerfCurrentEntry.setStatus(_A)
_CePfePerfCurrentUtilization_Type=CurrentUtilization
_CePfePerfCurrentUtilization_Object=MibTableColumn
cePfePerfCurrentUtilization=_CePfePerfCurrentUtilization_Object((1,3,6,1,4,1,9,9,265,1,1,2,1,1),_CePfePerfCurrentUtilization_Type())
cePfePerfCurrentUtilization.setMaxAccess(_C)
if mibBuilder.loadTexts:cePfePerfCurrentUtilization.setStatus(_A)
_CePfePerfCurrentEfficiency_Type=CurrentEfficiency
_CePfePerfCurrentEfficiency_Object=MibTableColumn
cePfePerfCurrentEfficiency=_CePfePerfCurrentEfficiency_Object((1,3,6,1,4,1,9,9,265,1,1,2,1,2),_CePfePerfCurrentEfficiency_Type())
cePfePerfCurrentEfficiency.setMaxAccess(_C)
if mibBuilder.loadTexts:cePfePerfCurrentEfficiency.setStatus(_A)
_CePfePerfCurrent1MinUtilization_Type=CurrentUtilization
_CePfePerfCurrent1MinUtilization_Object=MibTableColumn
cePfePerfCurrent1MinUtilization=_CePfePerfCurrent1MinUtilization_Object((1,3,6,1,4,1,9,9,265,1,1,2,1,3),_CePfePerfCurrent1MinUtilization_Type())
cePfePerfCurrent1MinUtilization.setMaxAccess(_C)
if mibBuilder.loadTexts:cePfePerfCurrent1MinUtilization.setStatus(_A)
_CePfePerfCurrent1MinEfficiency_Type=CurrentEfficiency
_CePfePerfCurrent1MinEfficiency_Object=MibTableColumn
cePfePerfCurrent1MinEfficiency=_CePfePerfCurrent1MinEfficiency_Object((1,3,6,1,4,1,9,9,265,1,1,2,1,4),_CePfePerfCurrent1MinEfficiency_Type())
cePfePerfCurrent1MinEfficiency.setMaxAccess(_C)
if mibBuilder.loadTexts:cePfePerfCurrent1MinEfficiency.setStatus(_A)
_CePfePerfCurrent5MinUtilization_Type=CurrentUtilization
_CePfePerfCurrent5MinUtilization_Object=MibTableColumn
cePfePerfCurrent5MinUtilization=_CePfePerfCurrent5MinUtilization_Object((1,3,6,1,4,1,9,9,265,1,1,2,1,5),_CePfePerfCurrent5MinUtilization_Type())
cePfePerfCurrent5MinUtilization.setMaxAccess(_C)
if mibBuilder.loadTexts:cePfePerfCurrent5MinUtilization.setStatus(_A)
_CePfePerfCurrent5MinEfficiency_Type=CurrentEfficiency
_CePfePerfCurrent5MinEfficiency_Object=MibTableColumn
cePfePerfCurrent5MinEfficiency=_CePfePerfCurrent5MinEfficiency_Object((1,3,6,1,4,1,9,9,265,1,1,2,1,6),_CePfePerfCurrent5MinEfficiency_Type())
cePfePerfCurrent5MinEfficiency.setMaxAccess(_C)
if mibBuilder.loadTexts:cePfePerfCurrent5MinEfficiency.setStatus(_A)
_CePfePerfIntervalTable_Object=MibTable
cePfePerfIntervalTable=_CePfePerfIntervalTable_Object((1,3,6,1,4,1,9,9,265,1,1,3))
if mibBuilder.loadTexts:cePfePerfIntervalTable.setStatus(_A)
_CePfePerfIntervalEntry_Object=MibTableRow
cePfePerfIntervalEntry=_CePfePerfIntervalEntry_Object((1,3,6,1,4,1,9,9,265,1,1,3,1))
cePfePerfIntervalEntry.setIndexNames((0,_G,_H),(0,_B,_N))
if mibBuilder.loadTexts:cePfePerfIntervalEntry.setStatus(_A)
class _CePfePerfIntervalNumber_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,96))
_CePfePerfIntervalNumber_Type.__name__=_E
_CePfePerfIntervalNumber_Object=MibTableColumn
cePfePerfIntervalNumber=_CePfePerfIntervalNumber_Object((1,3,6,1,4,1,9,9,265,1,1,3,1,1),_CePfePerfIntervalNumber_Type())
cePfePerfIntervalNumber.setMaxAccess(_O)
if mibBuilder.loadTexts:cePfePerfIntervalNumber.setStatus(_A)
_CePfePerfIntervalUtilization_Type=IntervalUtilization
_CePfePerfIntervalUtilization_Object=MibTableColumn
cePfePerfIntervalUtilization=_CePfePerfIntervalUtilization_Object((1,3,6,1,4,1,9,9,265,1,1,3,1,2),_CePfePerfIntervalUtilization_Type())
cePfePerfIntervalUtilization.setMaxAccess(_C)
if mibBuilder.loadTexts:cePfePerfIntervalUtilization.setStatus(_A)
_CePfePerfIntervalEfficiency_Type=IntervalEfficiency
_CePfePerfIntervalEfficiency_Object=MibTableColumn
cePfePerfIntervalEfficiency=_CePfePerfIntervalEfficiency_Object((1,3,6,1,4,1,9,9,265,1,1,3,1,3),_CePfePerfIntervalEfficiency_Type())
cePfePerfIntervalEfficiency.setMaxAccess(_C)
if mibBuilder.loadTexts:cePfePerfIntervalEfficiency.setStatus(_A)
_CePfePerfTotalTable_Object=MibTable
cePfePerfTotalTable=_CePfePerfTotalTable_Object((1,3,6,1,4,1,9,9,265,1,1,4))
if mibBuilder.loadTexts:cePfePerfTotalTable.setStatus(_A)
_CePfePerfTotalEntry_Object=MibTableRow
cePfePerfTotalEntry=_CePfePerfTotalEntry_Object((1,3,6,1,4,1,9,9,265,1,1,4,1))
cePfePerfTotalEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:cePfePerfTotalEntry.setStatus(_A)
_CePfePerfTotalUtilization_Type=TotalUtilization
_CePfePerfTotalUtilization_Object=MibTableColumn
cePfePerfTotalUtilization=_CePfePerfTotalUtilization_Object((1,3,6,1,4,1,9,9,265,1,1,4,1,1),_CePfePerfTotalUtilization_Type())
cePfePerfTotalUtilization.setMaxAccess(_C)
if mibBuilder.loadTexts:cePfePerfTotalUtilization.setStatus(_A)
_CePfePerfTotalEfficiency_Type=TotalEfficiency
_CePfePerfTotalEfficiency_Object=MibTableColumn
cePfePerfTotalEfficiency=_CePfePerfTotalEfficiency_Object((1,3,6,1,4,1,9,9,265,1,1,4,1,2),_CePfePerfTotalEfficiency_Type())
cePfePerfTotalEfficiency.setMaxAccess(_C)
if mibBuilder.loadTexts:cePfePerfTotalEfficiency.setStatus(_A)
_CePfeHistory_ObjectIdentity=ObjectIdentity
cePfeHistory=_CePfeHistory_ObjectIdentity((1,3,6,1,4,1,9,9,265,1,2))
class _CePfeHistNotifiesEnable_Type(EventType):defaultValue=1
_CePfeHistNotifiesEnable_Type.__name__=_P
_CePfeHistNotifiesEnable_Object=MibScalar
cePfeHistNotifiesEnable=_CePfeHistNotifiesEnable_Object((1,3,6,1,4,1,9,9,265,1,2,1),_CePfeHistNotifiesEnable_Type())
cePfeHistNotifiesEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:cePfeHistNotifiesEnable.setStatus(_A)
class _CePfeHistTableSize_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,500))
_CePfeHistTableSize_Type.__name__=_E
_CePfeHistTableSize_Object=MibScalar
cePfeHistTableSize=_CePfeHistTableSize_Object((1,3,6,1,4,1,9,9,265,1,2,2),_CePfeHistTableSize_Type())
cePfeHistTableSize.setMaxAccess(_D)
if mibBuilder.loadTexts:cePfeHistTableSize.setStatus(_A)
class _CePfeHistTableLastIndex_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_CePfeHistTableLastIndex_Type.__name__=_E
_CePfeHistTableLastIndex_Object=MibScalar
cePfeHistTableLastIndex=_CePfeHistTableLastIndex_Object((1,3,6,1,4,1,9,9,265,1,2,3),_CePfeHistTableLastIndex_Type())
cePfeHistTableLastIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:cePfeHistTableLastIndex.setStatus(_A)
_CePfeHistTable_Object=MibTable
cePfeHistTable=_CePfeHistTable_Object((1,3,6,1,4,1,9,9,265,1,2,4))
if mibBuilder.loadTexts:cePfeHistTable.setStatus(_A)
_CePfeHistEntry_Object=MibTableRow
cePfeHistEntry=_CePfeHistEntry_Object((1,3,6,1,4,1,9,9,265,1,2,4,1))
cePfeHistEntry.setIndexNames((0,_B,_Q))
if mibBuilder.loadTexts:cePfeHistEntry.setStatus(_A)
class _CePfeHistIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_CePfeHistIndex_Type.__name__=_E
_CePfeHistIndex_Object=MibTableColumn
cePfeHistIndex=_CePfeHistIndex_Object((1,3,6,1,4,1,9,9,265,1,2,4,1,1),_CePfeHistIndex_Type())
cePfeHistIndex.setMaxAccess(_O)
if mibBuilder.loadTexts:cePfeHistIndex.setStatus(_A)
_CePfeHistEntPhysIndex_Type=PhysicalIndex
_CePfeHistEntPhysIndex_Object=MibTableColumn
cePfeHistEntPhysIndex=_CePfeHistEntPhysIndex_Object((1,3,6,1,4,1,9,9,265,1,2,4,1,2),_CePfeHistEntPhysIndex_Type())
cePfeHistEntPhysIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:cePfeHistEntPhysIndex.setStatus(_A)
_CePfeHistType_Type=HistEventType
_CePfeHistType_Object=MibTableColumn
cePfeHistType=_CePfeHistType_Object((1,3,6,1,4,1,9,9,265,1,2,4,1,3),_CePfeHistType_Type())
cePfeHistType.setMaxAccess(_C)
if mibBuilder.loadTexts:cePfeHistType.setStatus(_A)
_CePfeHistThld_Type=Percentage
_CePfeHistThld_Object=MibTableColumn
cePfeHistThld=_CePfeHistThld_Object((1,3,6,1,4,1,9,9,265,1,2,4,1,4),_CePfeHistThld_Type())
cePfeHistThld.setMaxAccess(_C)
if mibBuilder.loadTexts:cePfeHistThld.setStatus(_A)
_CePfeHistValue_Type=Percentage
_CePfeHistValue_Object=MibTableColumn
cePfeHistValue=_CePfeHistValue_Object((1,3,6,1,4,1,9,9,265,1,2,4,1,5),_CePfeHistValue_Type())
cePfeHistValue.setMaxAccess(_C)
if mibBuilder.loadTexts:cePfeHistValue.setStatus(_A)
_CePfeHistRestartReason_Type=DisplayString
_CePfeHistRestartReason_Object=MibTableColumn
cePfeHistRestartReason=_CePfeHistRestartReason_Object((1,3,6,1,4,1,9,9,265,1,2,4,1,6),_CePfeHistRestartReason_Type())
cePfeHistRestartReason.setMaxAccess(_C)
if mibBuilder.loadTexts:cePfeHistRestartReason.setStatus(_A)
_CePfeHistTimeStamp_Type=TimeStamp
_CePfeHistTimeStamp_Object=MibTableColumn
cePfeHistTimeStamp=_CePfeHistTimeStamp_Object((1,3,6,1,4,1,9,9,265,1,2,4,1,7),_CePfeHistTimeStamp_Type())
cePfeHistTimeStamp.setMaxAccess(_C)
if mibBuilder.loadTexts:cePfeHistTimeStamp.setStatus(_A)
_CePfeMIBConformance_ObjectIdentity=ObjectIdentity
cePfeMIBConformance=_CePfeMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,9,265,2))
_CePfeMIBCompliances_ObjectIdentity=ObjectIdentity
cePfeMIBCompliances=_CePfeMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,265,2,1))
_CePfeMIBGroups_ObjectIdentity=ObjectIdentity
cePfeMIBGroups=_CePfeMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,265,2,2))
cePfePerfConfigEntry.registerAugmentions((_B,_R))
cePfePerfCurrentEntry.setIndexNames(*cePfePerfConfigEntry.getIndexNames())
cePfeMIBPerformanceGroup=ObjectGroup((1,3,6,1,4,1,9,9,265,2,2,1))
cePfeMIBPerformanceGroup.setObjects(*((_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c)))
if mibBuilder.loadTexts:cePfeMIBPerformanceGroup.setStatus(_A)
cePfeMIBCurrentGroup=ObjectGroup((1,3,6,1,4,1,9,9,265,2,2,2))
cePfeMIBCurrentGroup.setObjects(*((_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i)))
if mibBuilder.loadTexts:cePfeMIBCurrentGroup.setStatus(_A)
cePfeMIBIntervalGroup=ObjectGroup((1,3,6,1,4,1,9,9,265,2,2,3))
cePfeMIBIntervalGroup.setObjects(*((_B,_j),(_B,_k)))
if mibBuilder.loadTexts:cePfeMIBIntervalGroup.setStatus(_A)
cePfeMIBTotalGroup=ObjectGroup((1,3,6,1,4,1,9,9,265,2,2,4))
cePfeMIBTotalGroup.setObjects(*((_B,_l),(_B,_m)))
if mibBuilder.loadTexts:cePfeMIBTotalGroup.setStatus(_A)
cePfeMIBHistGroup=ObjectGroup((1,3,6,1,4,1,9,9,265,2,2,5))
cePfeMIBHistGroup.setObjects(*((_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_n)))
if mibBuilder.loadTexts:cePfeMIBHistGroup.setStatus(_A)
cePfeHistThldEvent=NotificationType((1,3,6,1,4,1,9,9,265,0,1))
cePfeHistThldEvent.setObjects(*((_B,_I),(_B,_J),(_B,_K),(_B,_L)))
if mibBuilder.loadTexts:cePfeHistThldEvent.setStatus(_A)
cePfeHistRestartEvent=NotificationType((1,3,6,1,4,1,9,9,265,0,2))
cePfeHistRestartEvent.setObjects(*((_B,_I),(_B,_M)))
if mibBuilder.loadTexts:cePfeHistRestartEvent.setStatus(_A)
cePfeMIBHistEventGroup=NotificationGroup((1,3,6,1,4,1,9,9,265,2,2,6))
cePfeMIBHistEventGroup.setObjects(*((_B,_o),(_B,_p)))
if mibBuilder.loadTexts:cePfeMIBHistEventGroup.setStatus(_A)
cePfeMIBPerformanceCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,265,2,1,1))
cePfeMIBPerformanceCompliance.setObjects(*((_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v)))
if mibBuilder.loadTexts:cePfeMIBPerformanceCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'CurrentUtilization':CurrentUtilization,'CurrentEfficiency':CurrentEfficiency,'IntervalUtilization':IntervalUtilization,'IntervalEfficiency':IntervalEfficiency,'TotalUtilization':TotalUtilization,'TotalEfficiency':TotalEfficiency,_F:Percentage,_P:EventType,'HistEventType':HistEventType,'ciscoEntityPfeMib':ciscoEntityPfeMib,'cePfeMIBNotifications':cePfeMIBNotifications,_o:cePfeHistThldEvent,_p:cePfeHistRestartEvent,'cePfeMIBObjects':cePfeMIBObjects,'cePfePerformance':cePfePerformance,'cePfePerfConfigTable':cePfePerfConfigTable,'cePfePerfConfigEntry':cePfePerfConfigEntry,_V:cePfePerfConfigTimeElapsed,_W:cePfePerfConfigValidIntervals,_X:cePfePerfConfigThldUtilization,_Y:cePfePerfConfigThldEfficiency,_Z:cePfePerfConfigThld1MinUtilization,_a:cePfePerfConfigThld1MinEfficiency,_b:cePfePerfConfigThld5MinUtilization,_c:cePfePerfConfigThld5MinEfficiency,'cePfePerfCurrentTable':cePfePerfCurrentTable,_R:cePfePerfCurrentEntry,_d:cePfePerfCurrentUtilization,_e:cePfePerfCurrentEfficiency,_f:cePfePerfCurrent1MinUtilization,_g:cePfePerfCurrent1MinEfficiency,_h:cePfePerfCurrent5MinUtilization,_i:cePfePerfCurrent5MinEfficiency,'cePfePerfIntervalTable':cePfePerfIntervalTable,'cePfePerfIntervalEntry':cePfePerfIntervalEntry,_N:cePfePerfIntervalNumber,_j:cePfePerfIntervalUtilization,_k:cePfePerfIntervalEfficiency,'cePfePerfTotalTable':cePfePerfTotalTable,'cePfePerfTotalEntry':cePfePerfTotalEntry,_l:cePfePerfTotalUtilization,_m:cePfePerfTotalEfficiency,'cePfeHistory':cePfeHistory,_U:cePfeHistNotifiesEnable,_S:cePfeHistTableSize,_T:cePfeHistTableLastIndex,'cePfeHistTable':cePfeHistTable,'cePfeHistEntry':cePfeHistEntry,_Q:cePfeHistIndex,_I:cePfeHistEntPhysIndex,_J:cePfeHistType,_K:cePfeHistThld,_L:cePfeHistValue,_M:cePfeHistRestartReason,_n:cePfeHistTimeStamp,'cePfeMIBConformance':cePfeMIBConformance,'cePfeMIBCompliances':cePfeMIBCompliances,'cePfeMIBPerformanceCompliance':cePfeMIBPerformanceCompliance,'cePfeMIBGroups':cePfeMIBGroups,_q:cePfeMIBPerformanceGroup,_r:cePfeMIBCurrentGroup,_u:cePfeMIBIntervalGroup,_v:cePfeMIBTotalGroup,_s:cePfeMIBHistGroup,_t:cePfeMIBHistEventGroup})