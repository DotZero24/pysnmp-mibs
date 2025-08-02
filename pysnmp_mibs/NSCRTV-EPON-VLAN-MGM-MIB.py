_e='pqEndVlanId'
_d='pqStartVlanId'
_c='pqPortIndex'
_b='pqCardIndex'
_a='pqDeviceIndex'
_Z='trunkPortIndex'
_Y='trunkCardIndex'
_X='trunkDeviceIndex'
_W='portAggregationVidIndex'
_V='pvaPortIndex'
_U='pvaCardIndex'
_T='pvaDeviceIndex'
_S='portVidIndex'
_R='pvtPortIndex'
_Q='pvtCardIndex'
_P='pvtDeviceIndex'
_O='pvlanPortIndex'
_N='pvlanCardIndex'
_M='pvlanDeviceIndex'
_L='onuVlanIndex'
_K='oltVlanDeviceIndex'
_J='oltVlanIndex'
_I='vlanDeviceIndex'
_H='read-only'
_G='read-write'
_F='Integer32'
_E='OctetString'
_D='read-create'
_C='not-accessible'
_B='NSCRTV-EPON-VLAN-MGM-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_E,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
AutoNegotiationTechAbility,EponAlarmCode,EponAlarmInstance,EponCardIndex,EponDeviceIndex,EponPortIndex,EponSeverityType,EponStats15MinRecordType,EponStats24HourRecordType,EponStatsThresholdType,TAddress,vlanManagementObjects=mibBuilder.importSymbols('NSCRTV-EPONEOC-EPON-MIB','AutoNegotiationTechAbility','EponAlarmCode','EponAlarmInstance','EponCardIndex','EponDeviceIndex','EponPortIndex','EponSeverityType','EponStats15MinRecordType','EponStats24HourRecordType','EponStatsThresholdType','TAddress','vlanManagementObjects')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention','TimeStamp','TruthValue')
_VlanGlobalInfoTable_Object=MibTable
vlanGlobalInfoTable=_VlanGlobalInfoTable_Object((1,3,6,1,4,1,17409,2,3,7,1))
if mibBuilder.loadTexts:vlanGlobalInfoTable.setStatus(_A)
_VlanGlobalInfoEntry_Object=MibTableRow
vlanGlobalInfoEntry=_VlanGlobalInfoEntry_Object((1,3,6,1,4,1,17409,2,3,7,1,1))
vlanGlobalInfoEntry.setIndexNames((0,_B,_I))
if mibBuilder.loadTexts:vlanGlobalInfoEntry.setStatus(_A)
_VlanDeviceIndex_Type=Integer32
_VlanDeviceIndex_Object=MibTableColumn
vlanDeviceIndex=_VlanDeviceIndex_Object((1,3,6,1,4,1,17409,2,3,7,1,1,1),_VlanDeviceIndex_Type())
vlanDeviceIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:vlanDeviceIndex.setStatus(_A)
_MaxVlanId_Type=Integer32
_MaxVlanId_Object=MibTableColumn
maxVlanId=_MaxVlanId_Object((1,3,6,1,4,1,17409,2,3,7,1,1,2),_MaxVlanId_Type())
maxVlanId.setMaxAccess(_H)
if mibBuilder.loadTexts:maxVlanId.setStatus(_A)
_MaxSupportVlans_Type=Integer32
_MaxSupportVlans_Object=MibTableColumn
maxSupportVlans=_MaxSupportVlans_Object((1,3,6,1,4,1,17409,2,3,7,1,1,3),_MaxSupportVlans_Type())
maxSupportVlans.setMaxAccess(_H)
if mibBuilder.loadTexts:maxSupportVlans.setStatus(_A)
_CreatedVlanNumber_Type=Integer32
_CreatedVlanNumber_Object=MibTableColumn
createdVlanNumber=_CreatedVlanNumber_Object((1,3,6,1,4,1,17409,2,3,7,1,1,4),_CreatedVlanNumber_Type())
createdVlanNumber.setMaxAccess(_H)
if mibBuilder.loadTexts:createdVlanNumber.setStatus(_A)
_VlanConfigGroup_ObjectIdentity=ObjectIdentity
vlanConfigGroup=_VlanConfigGroup_ObjectIdentity((1,3,6,1,4,1,17409,2,3,7,2))
if mibBuilder.loadTexts:vlanConfigGroup.setStatus(_A)
_OltVlanConfigTable_Object=MibTable
oltVlanConfigTable=_OltVlanConfigTable_Object((1,3,6,1,4,1,17409,2,3,7,2,1))
if mibBuilder.loadTexts:oltVlanConfigTable.setStatus(_A)
_OltVlanConfigEntry_Object=MibTableRow
oltVlanConfigEntry=_OltVlanConfigEntry_Object((1,3,6,1,4,1,17409,2,3,7,2,1,1))
oltVlanConfigEntry.setIndexNames((0,_B,_J),(0,_B,_K))
if mibBuilder.loadTexts:oltVlanConfigEntry.setStatus(_A)
_OltVlanIndex_Type=Integer32
_OltVlanIndex_Object=MibTableColumn
oltVlanIndex=_OltVlanIndex_Object((1,3,6,1,4,1,17409,2,3,7,2,1,1,1),_OltVlanIndex_Type())
oltVlanIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:oltVlanIndex.setStatus(_A)
_OltVlanDeviceIndex_Type=Integer32
_OltVlanDeviceIndex_Object=MibTableColumn
oltVlanDeviceIndex=_OltVlanDeviceIndex_Object((1,3,6,1,4,1,17409,2,3,7,2,1,1,2),_OltVlanDeviceIndex_Type())
oltVlanDeviceIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:oltVlanDeviceIndex.setStatus(_A)
class _OltVlanName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_OltVlanName_Type.__name__=_E
_OltVlanName_Object=MibTableColumn
oltVlanName=_OltVlanName_Object((1,3,6,1,4,1,17409,2,3,7,2,1,1,3),_OltVlanName_Type())
oltVlanName.setMaxAccess(_D)
if mibBuilder.loadTexts:oltVlanName.setStatus(_A)
_TaggedPort_Type=OctetString
_TaggedPort_Object=MibTableColumn
taggedPort=_TaggedPort_Object((1,3,6,1,4,1,17409,2,3,7,2,1,1,4),_TaggedPort_Type())
taggedPort.setMaxAccess(_D)
if mibBuilder.loadTexts:taggedPort.setStatus(_A)
_UntaggedPort_Type=OctetString
_UntaggedPort_Object=MibTableColumn
untaggedPort=_UntaggedPort_Object((1,3,6,1,4,1,17409,2,3,7,2,1,1,5),_UntaggedPort_Type())
untaggedPort.setMaxAccess(_D)
if mibBuilder.loadTexts:untaggedPort.setStatus(_A)
_OltVlanRowStatus_Type=RowStatus
_OltVlanRowStatus_Object=MibTableColumn
oltVlanRowStatus=_OltVlanRowStatus_Object((1,3,6,1,4,1,17409,2,3,7,2,1,1,6),_OltVlanRowStatus_Type())
oltVlanRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:oltVlanRowStatus.setStatus(_A)
_OnuVlanConfigTable_Object=MibTable
onuVlanConfigTable=_OnuVlanConfigTable_Object((1,3,6,1,4,1,17409,2,3,7,2,2))
if mibBuilder.loadTexts:onuVlanConfigTable.setStatus(_A)
_OnuVlanConfigEntry_Object=MibTableRow
onuVlanConfigEntry=_OnuVlanConfigEntry_Object((1,3,6,1,4,1,17409,2,3,7,2,2,1))
onuVlanConfigEntry.setIndexNames((0,_B,_L))
if mibBuilder.loadTexts:onuVlanConfigEntry.setStatus(_A)
_OnuVlanIndex_Type=Integer32
_OnuVlanIndex_Object=MibTableColumn
onuVlanIndex=_OnuVlanIndex_Object((1,3,6,1,4,1,17409,2,3,7,2,2,1,1),_OnuVlanIndex_Type())
onuVlanIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:onuVlanIndex.setStatus(_A)
class _OnuVlanName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_OnuVlanName_Type.__name__=_E
_OnuVlanName_Object=MibTableColumn
onuVlanName=_OnuVlanName_Object((1,3,6,1,4,1,17409,2,3,7,2,2,1,2),_OnuVlanName_Type())
onuVlanName.setMaxAccess(_D)
if mibBuilder.loadTexts:onuVlanName.setStatus(_A)
_OnuVlanTaggedPort_Type=OctetString
_OnuVlanTaggedPort_Object=MibTableColumn
onuVlanTaggedPort=_OnuVlanTaggedPort_Object((1,3,6,1,4,1,17409,2,3,7,2,2,1,3),_OnuVlanTaggedPort_Type())
onuVlanTaggedPort.setMaxAccess(_D)
if mibBuilder.loadTexts:onuVlanTaggedPort.setStatus(_A)
_OnuVlanUntaggedPort_Type=OctetString
_OnuVlanUntaggedPort_Object=MibTableColumn
onuVlanUntaggedPort=_OnuVlanUntaggedPort_Object((1,3,6,1,4,1,17409,2,3,7,2,2,1,4),_OnuVlanUntaggedPort_Type())
onuVlanUntaggedPort.setMaxAccess(_D)
if mibBuilder.loadTexts:onuVlanUntaggedPort.setStatus(_A)
_OnuVlanRowStatus_Type=RowStatus
_OnuVlanRowStatus_Object=MibTableColumn
onuVlanRowStatus=_OnuVlanRowStatus_Object((1,3,6,1,4,1,17409,2,3,7,2,2,1,5),_OnuVlanRowStatus_Type())
onuVlanRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:onuVlanRowStatus.setStatus(_A)
_PortVlanGroup_ObjectIdentity=ObjectIdentity
portVlanGroup=_PortVlanGroup_ObjectIdentity((1,3,6,1,4,1,17409,2,3,7,3))
if mibBuilder.loadTexts:portVlanGroup.setStatus(_A)
_PortVlanTable_Object=MibTable
portVlanTable=_PortVlanTable_Object((1,3,6,1,4,1,17409,2,3,7,3,1))
if mibBuilder.loadTexts:portVlanTable.setStatus(_A)
_PortVlanEntry_Object=MibTableRow
portVlanEntry=_PortVlanEntry_Object((1,3,6,1,4,1,17409,2,3,7,3,1,1))
portVlanEntry.setIndexNames((0,_B,_M),(0,_B,_N),(0,_B,_O))
if mibBuilder.loadTexts:portVlanEntry.setStatus(_A)
_PvlanDeviceIndex_Type=EponDeviceIndex
_PvlanDeviceIndex_Object=MibTableColumn
pvlanDeviceIndex=_PvlanDeviceIndex_Object((1,3,6,1,4,1,17409,2,3,7,3,1,1,1),_PvlanDeviceIndex_Type())
pvlanDeviceIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:pvlanDeviceIndex.setStatus(_A)
_PvlanCardIndex_Type=EponCardIndex
_PvlanCardIndex_Object=MibTableColumn
pvlanCardIndex=_PvlanCardIndex_Object((1,3,6,1,4,1,17409,2,3,7,3,1,1,2),_PvlanCardIndex_Type())
pvlanCardIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:pvlanCardIndex.setStatus(_A)
_PvlanPortIndex_Type=EponPortIndex
_PvlanPortIndex_Object=MibTableColumn
pvlanPortIndex=_PvlanPortIndex_Object((1,3,6,1,4,1,17409,2,3,7,3,1,1,3),_PvlanPortIndex_Type())
pvlanPortIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:pvlanPortIndex.setStatus(_A)
class _VlanTagTpid_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,2));fixedLength=2
_VlanTagTpid_Type.__name__=_E
_VlanTagTpid_Object=MibTableColumn
vlanTagTpid=_VlanTagTpid_Object((1,3,6,1,4,1,17409,2,3,7,3,1,1,4),_VlanTagTpid_Type())
vlanTagTpid.setMaxAccess(_G)
if mibBuilder.loadTexts:vlanTagTpid.setStatus(_A)
_VlanTagCfi_Type=TruthValue
_VlanTagCfi_Object=MibTableColumn
vlanTagCfi=_VlanTagCfi_Object((1,3,6,1,4,1,17409,2,3,7,3,1,1,5),_VlanTagCfi_Type())
vlanTagCfi.setMaxAccess(_G)
if mibBuilder.loadTexts:vlanTagCfi.setStatus(_A)
class _VlanTagPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_VlanTagPriority_Type.__name__=_F
_VlanTagPriority_Object=MibTableColumn
vlanTagPriority=_VlanTagPriority_Object((1,3,6,1,4,1,17409,2,3,7,3,1,1,6),_VlanTagPriority_Type())
vlanTagPriority.setMaxAccess(_G)
if mibBuilder.loadTexts:vlanTagPriority.setStatus(_A)
_VlanPVid_Type=Integer32
_VlanPVid_Object=MibTableColumn
vlanPVid=_VlanPVid_Object((1,3,6,1,4,1,17409,2,3,7,3,1,1,7),_VlanPVid_Type())
vlanPVid.setMaxAccess(_G)
if mibBuilder.loadTexts:vlanPVid.setStatus(_A)
class _VlanMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*(('transparent',0),('tag',1),('translation',2),('aggregation',3),('trunk',4),('stacking',5)))
_VlanMode_Type.__name__=_F
_VlanMode_Object=MibTableColumn
vlanMode=_VlanMode_Object((1,3,6,1,4,1,17409,2,3,7,3,1,1,8),_VlanMode_Type())
vlanMode.setMaxAccess(_G)
if mibBuilder.loadTexts:vlanMode.setStatus(_A)
_PortVlanTranslationTable_Object=MibTable
portVlanTranslationTable=_PortVlanTranslationTable_Object((1,3,6,1,4,1,17409,2,3,7,3,2))
if mibBuilder.loadTexts:portVlanTranslationTable.setStatus(_A)
_PortVlanTranslationEntry_Object=MibTableRow
portVlanTranslationEntry=_PortVlanTranslationEntry_Object((1,3,6,1,4,1,17409,2,3,7,3,2,1))
portVlanTranslationEntry.setIndexNames((0,_B,_P),(0,_B,_Q),(0,_B,_R),(0,_B,_S))
if mibBuilder.loadTexts:portVlanTranslationEntry.setStatus(_A)
_PvtDeviceIndex_Type=EponDeviceIndex
_PvtDeviceIndex_Object=MibTableColumn
pvtDeviceIndex=_PvtDeviceIndex_Object((1,3,6,1,4,1,17409,2,3,7,3,2,1,1),_PvtDeviceIndex_Type())
pvtDeviceIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:pvtDeviceIndex.setStatus(_A)
_PvtCardIndex_Type=EponCardIndex
_PvtCardIndex_Object=MibTableColumn
pvtCardIndex=_PvtCardIndex_Object((1,3,6,1,4,1,17409,2,3,7,3,2,1,2),_PvtCardIndex_Type())
pvtCardIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:pvtCardIndex.setStatus(_A)
_PvtPortIndex_Type=EponPortIndex
_PvtPortIndex_Object=MibTableColumn
pvtPortIndex=_PvtPortIndex_Object((1,3,6,1,4,1,17409,2,3,7,3,2,1,3),_PvtPortIndex_Type())
pvtPortIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:pvtPortIndex.setStatus(_A)
_PortVidIndex_Type=Unsigned32
_PortVidIndex_Object=MibTableColumn
portVidIndex=_PortVidIndex_Object((1,3,6,1,4,1,17409,2,3,7,3,2,1,4),_PortVidIndex_Type())
portVidIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:portVidIndex.setStatus(_A)
_TranslationNewVid_Type=Unsigned32
_TranslationNewVid_Object=MibTableColumn
translationNewVid=_TranslationNewVid_Object((1,3,6,1,4,1,17409,2,3,7,3,2,1,5),_TranslationNewVid_Type())
translationNewVid.setMaxAccess(_D)
if mibBuilder.loadTexts:translationNewVid.setStatus(_A)
_TranslationRowStatus_Type=RowStatus
_TranslationRowStatus_Object=MibTableColumn
translationRowStatus=_TranslationRowStatus_Object((1,3,6,1,4,1,17409,2,3,7,3,2,1,6),_TranslationRowStatus_Type())
translationRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:translationRowStatus.setStatus(_A)
_PortVlanAggregationManagement_ObjectIdentity=ObjectIdentity
portVlanAggregationManagement=_PortVlanAggregationManagement_ObjectIdentity((1,3,6,1,4,1,17409,2,3,7,3,3))
if mibBuilder.loadTexts:portVlanAggregationManagement.setStatus(_A)
_PortVlanAggregationConfigTable_Object=MibTable
portVlanAggregationConfigTable=_PortVlanAggregationConfigTable_Object((1,3,6,1,4,1,17409,2,3,7,3,3,1))
if mibBuilder.loadTexts:portVlanAggregationConfigTable.setStatus(_A)
_PortVlanAggregationConfigEntry_Object=MibTableRow
portVlanAggregationConfigEntry=_PortVlanAggregationConfigEntry_Object((1,3,6,1,4,1,17409,2,3,7,3,3,1,1))
portVlanAggregationConfigEntry.setIndexNames((0,_B,_T),(0,_B,_U),(0,_B,_V),(0,_B,_W))
if mibBuilder.loadTexts:portVlanAggregationConfigEntry.setStatus(_A)
_PvaDeviceIndex_Type=EponDeviceIndex
_PvaDeviceIndex_Object=MibTableColumn
pvaDeviceIndex=_PvaDeviceIndex_Object((1,3,6,1,4,1,17409,2,3,7,3,3,1,1,1),_PvaDeviceIndex_Type())
pvaDeviceIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:pvaDeviceIndex.setStatus(_A)
_PvaCardIndex_Type=EponCardIndex
_PvaCardIndex_Object=MibTableColumn
pvaCardIndex=_PvaCardIndex_Object((1,3,6,1,4,1,17409,2,3,7,3,3,1,1,2),_PvaCardIndex_Type())
pvaCardIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:pvaCardIndex.setStatus(_A)
_PvaPortIndex_Type=EponPortIndex
_PvaPortIndex_Object=MibTableColumn
pvaPortIndex=_PvaPortIndex_Object((1,3,6,1,4,1,17409,2,3,7,3,3,1,1,3),_PvaPortIndex_Type())
pvaPortIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:pvaPortIndex.setStatus(_A)
_PortAggregationVidIndex_Type=Unsigned32
_PortAggregationVidIndex_Object=MibTableColumn
portAggregationVidIndex=_PortAggregationVidIndex_Object((1,3,6,1,4,1,17409,2,3,7,3,3,1,1,4),_PortAggregationVidIndex_Type())
portAggregationVidIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:portAggregationVidIndex.setStatus(_A)
class _AggregationVidList_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(512,512));fixedLength=512
_AggregationVidList_Type.__name__=_E
_AggregationVidList_Object=MibTableColumn
aggregationVidList=_AggregationVidList_Object((1,3,6,1,4,1,17409,2,3,7,3,3,1,1,5),_AggregationVidList_Type())
aggregationVidList.setMaxAccess(_D)
if mibBuilder.loadTexts:aggregationVidList.setStatus(_A)
_AggregationRowStatus_Type=RowStatus
_AggregationRowStatus_Object=MibTableColumn
aggregationRowStatus=_AggregationRowStatus_Object((1,3,6,1,4,1,17409,2,3,7,3,3,1,1,6),_AggregationRowStatus_Type())
aggregationRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:aggregationRowStatus.setStatus(_A)
_PortVlanTrunkTable_Object=MibTable
portVlanTrunkTable=_PortVlanTrunkTable_Object((1,3,6,1,4,1,17409,2,3,7,3,4))
if mibBuilder.loadTexts:portVlanTrunkTable.setStatus(_A)
_PortVlanTrunkEntry_Object=MibTableRow
portVlanTrunkEntry=_PortVlanTrunkEntry_Object((1,3,6,1,4,1,17409,2,3,7,3,4,1))
portVlanTrunkEntry.setIndexNames((0,_B,_X),(0,_B,_Y),(0,_B,_Z))
if mibBuilder.loadTexts:portVlanTrunkEntry.setStatus(_A)
_TrunkDeviceIndex_Type=EponDeviceIndex
_TrunkDeviceIndex_Object=MibTableColumn
trunkDeviceIndex=_TrunkDeviceIndex_Object((1,3,6,1,4,1,17409,2,3,7,3,4,1,1),_TrunkDeviceIndex_Type())
trunkDeviceIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:trunkDeviceIndex.setStatus(_A)
_TrunkCardIndex_Type=EponCardIndex
_TrunkCardIndex_Object=MibTableColumn
trunkCardIndex=_TrunkCardIndex_Object((1,3,6,1,4,1,17409,2,3,7,3,4,1,2),_TrunkCardIndex_Type())
trunkCardIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:trunkCardIndex.setStatus(_A)
_TrunkPortIndex_Type=EponPortIndex
_TrunkPortIndex_Object=MibTableColumn
trunkPortIndex=_TrunkPortIndex_Object((1,3,6,1,4,1,17409,2,3,7,3,4,1,3),_TrunkPortIndex_Type())
trunkPortIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:trunkPortIndex.setStatus(_A)
class _TrunkVidList_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(512,512));fixedLength=512
_TrunkVidList_Type.__name__=_E
_TrunkVidList_Object=MibTableColumn
trunkVidList=_TrunkVidList_Object((1,3,6,1,4,1,17409,2,3,7,3,4,1,4),_TrunkVidList_Type())
trunkVidList.setMaxAccess(_D)
if mibBuilder.loadTexts:trunkVidList.setStatus(_A)
_PortVlanTrunkRowStatus_Type=RowStatus
_PortVlanTrunkRowStatus_Object=MibTableColumn
portVlanTrunkRowStatus=_PortVlanTrunkRowStatus_Object((1,3,6,1,4,1,17409,2,3,7,3,4,1,5),_PortVlanTrunkRowStatus_Type())
portVlanTrunkRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:portVlanTrunkRowStatus.setStatus(_A)
_QinQConfigGroup_ObjectIdentity=ObjectIdentity
qinQConfigGroup=_QinQConfigGroup_ObjectIdentity((1,3,6,1,4,1,17409,2,3,7,4))
if mibBuilder.loadTexts:qinQConfigGroup.setStatus(_A)
_PortQinQConfigTable_Object=MibTable
portQinQConfigTable=_PortQinQConfigTable_Object((1,3,6,1,4,1,17409,2,3,7,4,1))
if mibBuilder.loadTexts:portQinQConfigTable.setStatus(_A)
_PortQinQConfigEntry_Object=MibTableRow
portQinQConfigEntry=_PortQinQConfigEntry_Object((1,3,6,1,4,1,17409,2,3,7,4,1,1))
portQinQConfigEntry.setIndexNames((0,_B,_a),(0,_B,_b),(0,_B,_c),(0,_B,_d),(0,_B,_e))
if mibBuilder.loadTexts:portQinQConfigEntry.setStatus(_A)
_PqDeviceIndex_Type=EponDeviceIndex
_PqDeviceIndex_Object=MibTableColumn
pqDeviceIndex=_PqDeviceIndex_Object((1,3,6,1,4,1,17409,2,3,7,4,1,1,1),_PqDeviceIndex_Type())
pqDeviceIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:pqDeviceIndex.setStatus(_A)
_PqCardIndex_Type=EponCardIndex
_PqCardIndex_Object=MibTableColumn
pqCardIndex=_PqCardIndex_Object((1,3,6,1,4,1,17409,2,3,7,4,1,1,2),_PqCardIndex_Type())
pqCardIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:pqCardIndex.setStatus(_A)
_PqPortIndex_Type=EponPortIndex
_PqPortIndex_Object=MibTableColumn
pqPortIndex=_PqPortIndex_Object((1,3,6,1,4,1,17409,2,3,7,4,1,1,3),_PqPortIndex_Type())
pqPortIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:pqPortIndex.setStatus(_A)
_PqStartVlanId_Type=Integer32
_PqStartVlanId_Object=MibTableColumn
pqStartVlanId=_PqStartVlanId_Object((1,3,6,1,4,1,17409,2,3,7,4,1,1,4),_PqStartVlanId_Type())
pqStartVlanId.setMaxAccess(_C)
if mibBuilder.loadTexts:pqStartVlanId.setStatus(_A)
_PqEndVlanId_Type=Integer32
_PqEndVlanId_Object=MibTableColumn
pqEndVlanId=_PqEndVlanId_Object((1,3,6,1,4,1,17409,2,3,7,4,1,1,5),_PqEndVlanId_Type())
pqEndVlanId.setMaxAccess(_C)
if mibBuilder.loadTexts:pqEndVlanId.setStatus(_A)
_PqSVlanId_Type=Integer32
_PqSVlanId_Object=MibTableColumn
pqSVlanId=_PqSVlanId_Object((1,3,6,1,4,1,17409,2,3,7,4,1,1,6),_PqSVlanId_Type())
pqSVlanId.setMaxAccess(_D)
if mibBuilder.loadTexts:pqSVlanId.setStatus(_A)
class _PqSTagCosDetermine_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('redefine',1),('copyFromCTag',2)))
_PqSTagCosDetermine_Type.__name__=_F
_PqSTagCosDetermine_Object=MibTableColumn
pqSTagCosDetermine=_PqSTagCosDetermine_Object((1,3,6,1,4,1,17409,2,3,7,4,1,1,7),_PqSTagCosDetermine_Type())
pqSTagCosDetermine.setMaxAccess(_D)
if mibBuilder.loadTexts:pqSTagCosDetermine.setStatus(_A)
class _PqSTagCosNewValue_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_PqSTagCosNewValue_Type.__name__=_F
_PqSTagCosNewValue_Object=MibTableColumn
pqSTagCosNewValue=_PqSTagCosNewValue_Object((1,3,6,1,4,1,17409,2,3,7,4,1,1,8),_PqSTagCosNewValue_Type())
pqSTagCosNewValue.setMaxAccess(_D)
if mibBuilder.loadTexts:pqSTagCosNewValue.setStatus(_A)
_PqRowStatus_Type=RowStatus
_PqRowStatus_Object=MibTableColumn
pqRowStatus=_PqRowStatus_Object((1,3,6,1,4,1,17409,2,3,7,4,1,1,9),_PqRowStatus_Type())
pqRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:pqRowStatus.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'vlanGlobalInfoTable':vlanGlobalInfoTable,'vlanGlobalInfoEntry':vlanGlobalInfoEntry,_I:vlanDeviceIndex,'maxVlanId':maxVlanId,'maxSupportVlans':maxSupportVlans,'createdVlanNumber':createdVlanNumber,'vlanConfigGroup':vlanConfigGroup,'oltVlanConfigTable':oltVlanConfigTable,'oltVlanConfigEntry':oltVlanConfigEntry,_J:oltVlanIndex,_K:oltVlanDeviceIndex,'oltVlanName':oltVlanName,'taggedPort':taggedPort,'untaggedPort':untaggedPort,'oltVlanRowStatus':oltVlanRowStatus,'onuVlanConfigTable':onuVlanConfigTable,'onuVlanConfigEntry':onuVlanConfigEntry,_L:onuVlanIndex,'onuVlanName':onuVlanName,'onuVlanTaggedPort':onuVlanTaggedPort,'onuVlanUntaggedPort':onuVlanUntaggedPort,'onuVlanRowStatus':onuVlanRowStatus,'portVlanGroup':portVlanGroup,'portVlanTable':portVlanTable,'portVlanEntry':portVlanEntry,_M:pvlanDeviceIndex,_N:pvlanCardIndex,_O:pvlanPortIndex,'vlanTagTpid':vlanTagTpid,'vlanTagCfi':vlanTagCfi,'vlanTagPriority':vlanTagPriority,'vlanPVid':vlanPVid,'vlanMode':vlanMode,'portVlanTranslationTable':portVlanTranslationTable,'portVlanTranslationEntry':portVlanTranslationEntry,_P:pvtDeviceIndex,_Q:pvtCardIndex,_R:pvtPortIndex,_S:portVidIndex,'translationNewVid':translationNewVid,'translationRowStatus':translationRowStatus,'portVlanAggregationManagement':portVlanAggregationManagement,'portVlanAggregationConfigTable':portVlanAggregationConfigTable,'portVlanAggregationConfigEntry':portVlanAggregationConfigEntry,_T:pvaDeviceIndex,_U:pvaCardIndex,_V:pvaPortIndex,_W:portAggregationVidIndex,'aggregationVidList':aggregationVidList,'aggregationRowStatus':aggregationRowStatus,'portVlanTrunkTable':portVlanTrunkTable,'portVlanTrunkEntry':portVlanTrunkEntry,_X:trunkDeviceIndex,_Y:trunkCardIndex,_Z:trunkPortIndex,'trunkVidList':trunkVidList,'portVlanTrunkRowStatus':portVlanTrunkRowStatus,'qinQConfigGroup':qinQConfigGroup,'portQinQConfigTable':portQinQConfigTable,'portQinQConfigEntry':portQinQConfigEntry,_a:pqDeviceIndex,_b:pqCardIndex,_c:pqPortIndex,_d:pqStartVlanId,_e:pqEndVlanId,'pqSVlanId':pqSVlanId,'pqSTagCosDetermine':pqSTagCosDetermine,'pqSTagCosNewValue':pqSTagCosNewValue,'pqRowStatus':pqRowStatus})