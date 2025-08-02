_N='atAlmMonInputContactNumber'
_M='atAlmMonInputContactStkId'
_L='atAlmMonOutputRelayNumber'
_K='atAlmMonAvailableAlarmId'
_J='atAlmMonActionIndex'
_I='atAlmMonActionStackMemberId'
_H='closed'
_G='atAlmMonOutputRelayAlarmId'
_F='atAlmMonOutputRelayStkId'
_E='DisplayStringUnsized'
_D='read-write'
_C='AT-ALMMON-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
DisplayStringUnsized,=mibBuilder.importSymbols('AT-SMI-MIB',_E)
sysinfo,=mibBuilder.importSymbols('AT-SYSINFO-MIB','sysinfo')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
atAlmMon=ModuleIdentity((1,3,6,1,4,1,207,8,4,4,3,26))
if mibBuilder.loadTexts:atAlmMon.setRevisions(('2019-02-12 00:00','2018-09-20 00:00','2017-02-08 00:00','2014-05-12 00:15','2013-12-13 11:46'))
class AtAlmMonAlarmType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*(('externalPSU',1),('epsr',2),('contactInput',3),('portLinkDown',4),('loopDetect',5),('mainPse',6),('portPoeFailure',7),('temperature',8),('g8032',9),('ufo',10)))
class AtAlmMonActionUseOutput(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('unused',1),('used',2)))
class AtAlmMonAbnormalState(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('open',1),(_H,2)))
class AtAlmMonActionState(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('inactive',1),('active',2)))
class AtAlmMonContactPosition(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('open',1),(_H,2)))
_AtAlmMonActionTable_Object=MibTable
atAlmMonActionTable=_AtAlmMonActionTable_Object((1,3,6,1,4,1,207,8,4,4,3,26,1))
if mibBuilder.loadTexts:atAlmMonActionTable.setStatus(_A)
_AtAlmMonActionEntry_Object=MibTableRow
atAlmMonActionEntry=_AtAlmMonActionEntry_Object((1,3,6,1,4,1,207,8,4,4,3,26,1,1))
atAlmMonActionEntry.setIndexNames((0,_C,_I),(0,_C,_J))
if mibBuilder.loadTexts:atAlmMonActionEntry.setStatus(_A)
_AtAlmMonActionStackMemberId_Type=Unsigned32
_AtAlmMonActionStackMemberId_Object=MibTableColumn
atAlmMonActionStackMemberId=_AtAlmMonActionStackMemberId_Object((1,3,6,1,4,1,207,8,4,4,3,26,1,1,1),_AtAlmMonActionStackMemberId_Type())
atAlmMonActionStackMemberId.setMaxAccess(_B)
if mibBuilder.loadTexts:atAlmMonActionStackMemberId.setStatus(_A)
_AtAlmMonActionIndex_Type=Unsigned32
_AtAlmMonActionIndex_Object=MibTableColumn
atAlmMonActionIndex=_AtAlmMonActionIndex_Object((1,3,6,1,4,1,207,8,4,4,3,26,1,1,2),_AtAlmMonActionIndex_Type())
atAlmMonActionIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:atAlmMonActionIndex.setStatus(_A)
_AtAlmMonAlarmType_Type=AtAlmMonAlarmType
_AtAlmMonAlarmType_Object=MibTableColumn
atAlmMonAlarmType=_AtAlmMonAlarmType_Object((1,3,6,1,4,1,207,8,4,4,3,26,1,1,3),_AtAlmMonAlarmType_Type())
atAlmMonAlarmType.setMaxAccess(_B)
if mibBuilder.loadTexts:atAlmMonAlarmType.setStatus(_A)
_AtAlmMonAlarmTypeSelection_Type=Unsigned32
_AtAlmMonAlarmTypeSelection_Object=MibTableColumn
atAlmMonAlarmTypeSelection=_AtAlmMonAlarmTypeSelection_Object((1,3,6,1,4,1,207,8,4,4,3,26,1,1,4),_AtAlmMonAlarmTypeSelection_Type())
atAlmMonAlarmTypeSelection.setMaxAccess(_B)
if mibBuilder.loadTexts:atAlmMonAlarmTypeSelection.setStatus(_A)
class _AtAlmMonActionDescription_Type(DisplayStringUnsized):subtypeSpec=DisplayStringUnsized.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,30))
_AtAlmMonActionDescription_Type.__name__=_E
_AtAlmMonActionDescription_Object=MibTableColumn
atAlmMonActionDescription=_AtAlmMonActionDescription_Object((1,3,6,1,4,1,207,8,4,4,3,26,1,1,5),_AtAlmMonActionDescription_Type())
atAlmMonActionDescription.setMaxAccess(_B)
if mibBuilder.loadTexts:atAlmMonActionDescription.setStatus(_A)
_AtAlmMonActionUseRelay1_Type=AtAlmMonActionUseOutput
_AtAlmMonActionUseRelay1_Object=MibTableColumn
atAlmMonActionUseRelay1=_AtAlmMonActionUseRelay1_Object((1,3,6,1,4,1,207,8,4,4,3,26,1,1,6),_AtAlmMonActionUseRelay1_Type())
atAlmMonActionUseRelay1.setMaxAccess(_D)
if mibBuilder.loadTexts:atAlmMonActionUseRelay1.setStatus(_A)
_AtAlmMonActionUseRelay2_Type=AtAlmMonActionUseOutput
_AtAlmMonActionUseRelay2_Object=MibTableColumn
atAlmMonActionUseRelay2=_AtAlmMonActionUseRelay2_Object((1,3,6,1,4,1,207,8,4,4,3,26,1,1,7),_AtAlmMonActionUseRelay2_Type())
atAlmMonActionUseRelay2.setMaxAccess(_D)
if mibBuilder.loadTexts:atAlmMonActionUseRelay2.setStatus(_A)
_AtAlmMonActionUseRelay3_Type=AtAlmMonActionUseOutput
_AtAlmMonActionUseRelay3_Object=MibTableColumn
atAlmMonActionUseRelay3=_AtAlmMonActionUseRelay3_Object((1,3,6,1,4,1,207,8,4,4,3,26,1,1,8),_AtAlmMonActionUseRelay3_Type())
atAlmMonActionUseRelay3.setMaxAccess(_D)
if mibBuilder.loadTexts:atAlmMonActionUseRelay3.setStatus(_A)
_AtAlmMonActionUseFaultLed_Type=AtAlmMonActionUseOutput
_AtAlmMonActionUseFaultLed_Object=MibTableColumn
atAlmMonActionUseFaultLed=_AtAlmMonActionUseFaultLed_Object((1,3,6,1,4,1,207,8,4,4,3,26,1,1,9),_AtAlmMonActionUseFaultLed_Type())
atAlmMonActionUseFaultLed.setMaxAccess(_D)
if mibBuilder.loadTexts:atAlmMonActionUseFaultLed.setStatus(_A)
_AtAlmMonAbnormalState_Type=AtAlmMonAbnormalState
_AtAlmMonAbnormalState_Object=MibTableColumn
atAlmMonAbnormalState=_AtAlmMonAbnormalState_Object((1,3,6,1,4,1,207,8,4,4,3,26,1,1,10),_AtAlmMonAbnormalState_Type())
atAlmMonAbnormalState.setMaxAccess(_D)
if mibBuilder.loadTexts:atAlmMonAbnormalState.setStatus(_A)
_AtAlmMonActionState_Type=AtAlmMonActionState
_AtAlmMonActionState_Object=MibTableColumn
atAlmMonActionState=_AtAlmMonActionState_Object((1,3,6,1,4,1,207,8,4,4,3,26,1,1,11),_AtAlmMonActionState_Type())
atAlmMonActionState.setMaxAccess(_B)
if mibBuilder.loadTexts:atAlmMonActionState.setStatus(_A)
_AtAlmMonPerStackConfiguration_Type=TruthValue
_AtAlmMonPerStackConfiguration_Object=MibScalar
atAlmMonPerStackConfiguration=_AtAlmMonPerStackConfiguration_Object((1,3,6,1,4,1,207,8,4,4,3,26,2),_AtAlmMonPerStackConfiguration_Type())
atAlmMonPerStackConfiguration.setMaxAccess(_D)
if mibBuilder.loadTexts:atAlmMonPerStackConfiguration.setStatus(_A)
_AtAlmMonAvailableTable_Object=MibTable
atAlmMonAvailableTable=_AtAlmMonAvailableTable_Object((1,3,6,1,4,1,207,8,4,4,3,26,3))
if mibBuilder.loadTexts:atAlmMonAvailableTable.setStatus(_A)
_AtAlmMonAvailableEntry_Object=MibTableRow
atAlmMonAvailableEntry=_AtAlmMonAvailableEntry_Object((1,3,6,1,4,1,207,8,4,4,3,26,3,1))
atAlmMonAvailableEntry.setIndexNames((0,_C,_K))
if mibBuilder.loadTexts:atAlmMonAvailableEntry.setStatus(_A)
_AtAlmMonAvailableAlarmId_Type=Unsigned32
_AtAlmMonAvailableAlarmId_Object=MibTableColumn
atAlmMonAvailableAlarmId=_AtAlmMonAvailableAlarmId_Object((1,3,6,1,4,1,207,8,4,4,3,26,3,1,1),_AtAlmMonAvailableAlarmId_Type())
atAlmMonAvailableAlarmId.setMaxAccess(_B)
if mibBuilder.loadTexts:atAlmMonAvailableAlarmId.setStatus(_A)
_AtAlmMonAvailableType_Type=AtAlmMonAlarmType
_AtAlmMonAvailableType_Object=MibTableColumn
atAlmMonAvailableType=_AtAlmMonAvailableType_Object((1,3,6,1,4,1,207,8,4,4,3,26,3,1,2),_AtAlmMonAvailableType_Type())
atAlmMonAvailableType.setMaxAccess(_B)
if mibBuilder.loadTexts:atAlmMonAvailableType.setStatus(_A)
_AtAlmMonAvailableTypeIndex_Type=Unsigned32
_AtAlmMonAvailableTypeIndex_Object=MibTableColumn
atAlmMonAvailableTypeIndex=_AtAlmMonAvailableTypeIndex_Object((1,3,6,1,4,1,207,8,4,4,3,26,3,1,3),_AtAlmMonAvailableTypeIndex_Type())
atAlmMonAvailableTypeIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:atAlmMonAvailableTypeIndex.setStatus(_A)
_AtAlmMonAvailableStkId_Type=Unsigned32
_AtAlmMonAvailableStkId_Object=MibTableColumn
atAlmMonAvailableStkId=_AtAlmMonAvailableStkId_Object((1,3,6,1,4,1,207,8,4,4,3,26,3,1,4),_AtAlmMonAvailableStkId_Type())
atAlmMonAvailableStkId.setMaxAccess(_B)
if mibBuilder.loadTexts:atAlmMonAvailableStkId.setStatus(_A)
class _AtAlmMonAvailableIfName_Type(DisplayStringUnsized):subtypeSpec=DisplayStringUnsized.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_AtAlmMonAvailableIfName_Type.__name__=_E
_AtAlmMonAvailableIfName_Object=MibTableColumn
atAlmMonAvailableIfName=_AtAlmMonAvailableIfName_Object((1,3,6,1,4,1,207,8,4,4,3,26,3,1,5),_AtAlmMonAvailableIfName_Type())
atAlmMonAvailableIfName.setMaxAccess(_B)
if mibBuilder.loadTexts:atAlmMonAvailableIfName.setStatus(_A)
_AtAlmMonAvailableState_Type=AtAlmMonActionState
_AtAlmMonAvailableState_Object=MibTableColumn
atAlmMonAvailableState=_AtAlmMonAvailableState_Object((1,3,6,1,4,1,207,8,4,4,3,26,3,1,6),_AtAlmMonAvailableState_Type())
atAlmMonAvailableState.setMaxAccess(_B)
if mibBuilder.loadTexts:atAlmMonAvailableState.setStatus(_A)
_AtAlmMonOutputRelayTable_Object=MibTable
atAlmMonOutputRelayTable=_AtAlmMonOutputRelayTable_Object((1,3,6,1,4,1,207,8,4,4,3,26,4))
if mibBuilder.loadTexts:atAlmMonOutputRelayTable.setStatus(_A)
_AtAlmMonOutputRelayEntry_Object=MibTableRow
atAlmMonOutputRelayEntry=_AtAlmMonOutputRelayEntry_Object((1,3,6,1,4,1,207,8,4,4,3,26,4,1))
atAlmMonOutputRelayEntry.setIndexNames((0,_C,_F),(0,_C,_L),(0,_C,_G))
if mibBuilder.loadTexts:atAlmMonOutputRelayEntry.setStatus(_A)
_AtAlmMonOutputRelayStkId_Type=Unsigned32
_AtAlmMonOutputRelayStkId_Object=MibTableColumn
atAlmMonOutputRelayStkId=_AtAlmMonOutputRelayStkId_Object((1,3,6,1,4,1,207,8,4,4,3,26,4,1,1),_AtAlmMonOutputRelayStkId_Type())
atAlmMonOutputRelayStkId.setMaxAccess(_B)
if mibBuilder.loadTexts:atAlmMonOutputRelayStkId.setStatus(_A)
_AtAlmMonOutputRelayNumber_Type=Unsigned32
_AtAlmMonOutputRelayNumber_Object=MibTableColumn
atAlmMonOutputRelayNumber=_AtAlmMonOutputRelayNumber_Object((1,3,6,1,4,1,207,8,4,4,3,26,4,1,2),_AtAlmMonOutputRelayNumber_Type())
atAlmMonOutputRelayNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:atAlmMonOutputRelayNumber.setStatus(_A)
_AtAlmMonOutputRelayAlarmId_Type=Unsigned32
_AtAlmMonOutputRelayAlarmId_Object=MibTableColumn
atAlmMonOutputRelayAlarmId=_AtAlmMonOutputRelayAlarmId_Object((1,3,6,1,4,1,207,8,4,4,3,26,4,1,3),_AtAlmMonOutputRelayAlarmId_Type())
atAlmMonOutputRelayAlarmId.setMaxAccess(_B)
if mibBuilder.loadTexts:atAlmMonOutputRelayAlarmId.setStatus(_A)
_AtAlmMonOutputRelayUsage_Type=AtAlmMonActionUseOutput
_AtAlmMonOutputRelayUsage_Object=MibTableColumn
atAlmMonOutputRelayUsage=_AtAlmMonOutputRelayUsage_Object((1,3,6,1,4,1,207,8,4,4,3,26,4,1,4),_AtAlmMonOutputRelayUsage_Type())
atAlmMonOutputRelayUsage.setMaxAccess(_D)
if mibBuilder.loadTexts:atAlmMonOutputRelayUsage.setStatus(_A)
_AtAlmMonOutputLedTable_Object=MibTable
atAlmMonOutputLedTable=_AtAlmMonOutputLedTable_Object((1,3,6,1,4,1,207,8,4,4,3,26,5))
if mibBuilder.loadTexts:atAlmMonOutputLedTable.setStatus(_A)
_AtAlmMonOutputLedEntry_Object=MibTableRow
atAlmMonOutputLedEntry=_AtAlmMonOutputLedEntry_Object((1,3,6,1,4,1,207,8,4,4,3,26,5,1))
atAlmMonOutputLedEntry.setIndexNames((0,_C,_F),(0,_C,_G))
if mibBuilder.loadTexts:atAlmMonOutputLedEntry.setStatus(_A)
_AtAlmMonOutputLedStkId_Type=Unsigned32
_AtAlmMonOutputLedStkId_Object=MibTableColumn
atAlmMonOutputLedStkId=_AtAlmMonOutputLedStkId_Object((1,3,6,1,4,1,207,8,4,4,3,26,5,1,1),_AtAlmMonOutputLedStkId_Type())
atAlmMonOutputLedStkId.setMaxAccess(_B)
if mibBuilder.loadTexts:atAlmMonOutputLedStkId.setStatus(_A)
_AtAlmMonOutputLedAlarmId_Type=Unsigned32
_AtAlmMonOutputLedAlarmId_Object=MibTableColumn
atAlmMonOutputLedAlarmId=_AtAlmMonOutputLedAlarmId_Object((1,3,6,1,4,1,207,8,4,4,3,26,5,1,2),_AtAlmMonOutputLedAlarmId_Type())
atAlmMonOutputLedAlarmId.setMaxAccess(_B)
if mibBuilder.loadTexts:atAlmMonOutputLedAlarmId.setStatus(_A)
_AtAlmMonOutputLedUsage_Type=AtAlmMonActionUseOutput
_AtAlmMonOutputLedUsage_Object=MibTableColumn
atAlmMonOutputLedUsage=_AtAlmMonOutputLedUsage_Object((1,3,6,1,4,1,207,8,4,4,3,26,5,1,3),_AtAlmMonOutputLedUsage_Type())
atAlmMonOutputLedUsage.setMaxAccess(_D)
if mibBuilder.loadTexts:atAlmMonOutputLedUsage.setStatus(_A)
_AtAlmMonInputContactTable_Object=MibTable
atAlmMonInputContactTable=_AtAlmMonInputContactTable_Object((1,3,6,1,4,1,207,8,4,4,3,26,6))
if mibBuilder.loadTexts:atAlmMonInputContactTable.setStatus(_A)
_AtAlmMonInputContactEntry_Object=MibTableRow
atAlmMonInputContactEntry=_AtAlmMonInputContactEntry_Object((1,3,6,1,4,1,207,8,4,4,3,26,6,1))
atAlmMonInputContactEntry.setIndexNames((0,_C,_M),(0,_C,_N))
if mibBuilder.loadTexts:atAlmMonInputContactEntry.setStatus(_A)
_AtAlmMonInputContactStkId_Type=Unsigned32
_AtAlmMonInputContactStkId_Object=MibTableColumn
atAlmMonInputContactStkId=_AtAlmMonInputContactStkId_Object((1,3,6,1,4,1,207,8,4,4,3,26,6,1,1),_AtAlmMonInputContactStkId_Type())
atAlmMonInputContactStkId.setMaxAccess(_B)
if mibBuilder.loadTexts:atAlmMonInputContactStkId.setStatus(_A)
_AtAlmMonInputContactNumber_Type=Unsigned32
_AtAlmMonInputContactNumber_Object=MibTableColumn
atAlmMonInputContactNumber=_AtAlmMonInputContactNumber_Object((1,3,6,1,4,1,207,8,4,4,3,26,6,1,2),_AtAlmMonInputContactNumber_Type())
atAlmMonInputContactNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:atAlmMonInputContactNumber.setStatus(_A)
_AtAlmMonInputContactPosition_Type=AtAlmMonContactPosition
_AtAlmMonInputContactPosition_Object=MibTableColumn
atAlmMonInputContactPosition=_AtAlmMonInputContactPosition_Object((1,3,6,1,4,1,207,8,4,4,3,26,6,1,3),_AtAlmMonInputContactPosition_Type())
atAlmMonInputContactPosition.setMaxAccess(_D)
if mibBuilder.loadTexts:atAlmMonInputContactPosition.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'AtAlmMonAlarmType':AtAlmMonAlarmType,'AtAlmMonActionUseOutput':AtAlmMonActionUseOutput,'AtAlmMonAbnormalState':AtAlmMonAbnormalState,'AtAlmMonActionState':AtAlmMonActionState,'AtAlmMonContactPosition':AtAlmMonContactPosition,'atAlmMon':atAlmMon,'atAlmMonActionTable':atAlmMonActionTable,'atAlmMonActionEntry':atAlmMonActionEntry,_I:atAlmMonActionStackMemberId,_J:atAlmMonActionIndex,'atAlmMonAlarmType':atAlmMonAlarmType,'atAlmMonAlarmTypeSelection':atAlmMonAlarmTypeSelection,'atAlmMonActionDescription':atAlmMonActionDescription,'atAlmMonActionUseRelay1':atAlmMonActionUseRelay1,'atAlmMonActionUseRelay2':atAlmMonActionUseRelay2,'atAlmMonActionUseRelay3':atAlmMonActionUseRelay3,'atAlmMonActionUseFaultLed':atAlmMonActionUseFaultLed,'atAlmMonAbnormalState':atAlmMonAbnormalState,'atAlmMonActionState':atAlmMonActionState,'atAlmMonPerStackConfiguration':atAlmMonPerStackConfiguration,'atAlmMonAvailableTable':atAlmMonAvailableTable,'atAlmMonAvailableEntry':atAlmMonAvailableEntry,_K:atAlmMonAvailableAlarmId,'atAlmMonAvailableType':atAlmMonAvailableType,'atAlmMonAvailableTypeIndex':atAlmMonAvailableTypeIndex,'atAlmMonAvailableStkId':atAlmMonAvailableStkId,'atAlmMonAvailableIfName':atAlmMonAvailableIfName,'atAlmMonAvailableState':atAlmMonAvailableState,'atAlmMonOutputRelayTable':atAlmMonOutputRelayTable,'atAlmMonOutputRelayEntry':atAlmMonOutputRelayEntry,_F:atAlmMonOutputRelayStkId,_L:atAlmMonOutputRelayNumber,_G:atAlmMonOutputRelayAlarmId,'atAlmMonOutputRelayUsage':atAlmMonOutputRelayUsage,'atAlmMonOutputLedTable':atAlmMonOutputLedTable,'atAlmMonOutputLedEntry':atAlmMonOutputLedEntry,'atAlmMonOutputLedStkId':atAlmMonOutputLedStkId,'atAlmMonOutputLedAlarmId':atAlmMonOutputLedAlarmId,'atAlmMonOutputLedUsage':atAlmMonOutputLedUsage,'atAlmMonInputContactTable':atAlmMonInputContactTable,'atAlmMonInputContactEntry':atAlmMonInputContactEntry,_M:atAlmMonInputContactStkId,_N:atAlmMonInputContactNumber,'atAlmMonInputContactPosition':atAlmMonInputContactPosition})