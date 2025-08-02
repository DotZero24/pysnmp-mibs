_Z='adGenVectorBulkFilterInstance'
_Y='adGenVectorPhyStatusPhyIfIndex'
_X='deprecated'
_W='adGenVectorPhyMapPhyIfIndex'
_V='adGenVectorPhyMapGroupIfIndex'
_U='enable'
_T='disable'
_S='AdGenVectorGroupFallbackModes'
_R='adGenVectorGroupIfIndex'
_Q='DisplayString'
_P='adGenVectorGroupStatusIfIndex'
_O='sysName'
_N='SNMPv2-MIB'
_M='adTAeSCUTrapAlarmLevel'
_L='ADTRAN-TAeSCUEXT1-MIB'
_K='adTrapInformSeqNum'
_J='ADTRAN-GENTRAPINFORM-MIB'
_I='not-accessible'
_H='read-write'
_G='adGenSlotInfoIndex'
_F='ADTRAN-GENSLOT-MIB'
_E='ADTRAN-GENERIC-VECTORING-MIB'
_D='read-create'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
adGenPortTrapIdentifier,=mibBuilder.importSymbols('ADTRAN-GENPORT-MIB','adGenPortTrapIdentifier')
adGenSlotInfoIndex,=mibBuilder.importSymbols(_F,_G)
adTrapInformSeqNum,=mibBuilder.importSymbols(_J,_K)
adGenVector,adGenVectorID=mibBuilder.importSymbols('ADTRAN-SHARED-CND-SYSTEM-MIB','adGenVector','adGenVectorID')
adTAeSCUTrapAlarmLevel,=mibBuilder.importSymbols(_L,_M)
InterfaceIndex,ifIndex=mibBuilder.importSymbols('IF-MIB','InterfaceIndex','ifIndex')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
sysName,=mibBuilder.importSymbols(_N,_O)
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_Q,'PhysAddress','RowStatus','TextualConvention')
adGenVectorMIB=ModuleIdentity((1,3,6,1,4,1,664,6,10000,70,57,1))
if mibBuilder.loadTexts:adGenVectorMIB.setRevisions(('2018-02-01 00:00','2017-06-14 00:00','2016-09-22 00:00','2015-08-13 00:00','2015-07-17 00:00','2015-05-27 00:00','2014-07-26 00:00','2014-07-25 00:00','2014-03-03 00:00','2013-11-26 00:00'))
class AdGenVectorMode(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,7)));namedValues=NamedValues(*(('blv',1),('slv',2),('both',3),('none',4),('dlv',5),('blv-dlv-slv',7)))
class AdGenVectorGroupOperStatus(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('up',1),('down',2),('upPartial',3)))
class AdGenVectorLastChange(TextualConvention,TimeTicks):status=_A
class AdGenVectorPhyPortErrorTimestamp(TextualConvention,TimeTicks):status=_A
class AdGenVectorPhyLineState(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*(('notAvailable',0),('down',1),('train',2),('up',3),('deltActive',4),('deltDataExchange',5),('deltDataRequest',6),('deltComplete',7),('seltActive',8),('seltDataRequest',9),('seltComplete',10)))
class AdGenVectorPhyPortVectoringState(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31)));namedValues=NamedValues(*(('idle',0),('dsInit-1-0',1),('dsInit-2-1',2),('usInit-1',3),('usInit-2',4),('steady',5),('trans',6),('waitForStart',7),('dsInit-1-1',8),('dsInit-2-0',9),('reset',10),('nonVectoring',11),('handshake',12),('waitForStart-Legacy',13),('init-Legacy',14),('steady-Legacy',15),('steadyB',16),('stopPending',17),('idle-FF',18),('dsInit-1-0-ff',19),('dsInit-2-1-ff',20),('usInit-1-ff',21),('usInit-2-ff',22),('steady-ff',23),('trans-ff',24),('waitForStart-ff',25),('dsInit-1-1-ff',26),('dsInit-2-0-ff',27),('steadyB-ff',28),('stopPending-ff',29),('unknown',30),('fallback',31)))
class AdGenVectorGroupBandPlans(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('g998',1),('g998e',2),('g998ade',3),('g997',4),('g997e',5),('hpe',6)))
class AdGenVectorGroupFallbackModes(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('adsl2-multimode',1),('shutdown',2),('adsl2',3),('non-vectored',4)))
_AdGenVectorMIBObjects_ObjectIdentity=ObjectIdentity
adGenVectorMIBObjects=_AdGenVectorMIBObjects_ObjectIdentity((1,3,6,1,4,1,664,5,70,57,1))
_AdGenVectorModuleConfTable_Object=MibTable
adGenVectorModuleConfTable=_AdGenVectorModuleConfTable_Object((1,3,6,1,4,1,664,5,70,57,1,1))
if mibBuilder.loadTexts:adGenVectorModuleConfTable.setStatus(_A)
_AdGenVectorModuleConfEntry_Object=MibTableRow
adGenVectorModuleConfEntry=_AdGenVectorModuleConfEntry_Object((1,3,6,1,4,1,664,5,70,57,1,1,1))
adGenVectorModuleConfEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:adGenVectorModuleConfEntry.setStatus(_A)
_AdGenVectorModuleConfSupportedVectorModeTypes_Type=AdGenVectorMode
_AdGenVectorModuleConfSupportedVectorModeTypes_Object=MibTableColumn
adGenVectorModuleConfSupportedVectorModeTypes=_AdGenVectorModuleConfSupportedVectorModeTypes_Object((1,3,6,1,4,1,664,5,70,57,1,1,1,1),_AdGenVectorModuleConfSupportedVectorModeTypes_Type())
adGenVectorModuleConfSupportedVectorModeTypes.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenVectorModuleConfSupportedVectorModeTypes.setStatus(_A)
_AdGenVectorModuleConfMaxBLVGroups_Type=Integer32
_AdGenVectorModuleConfMaxBLVGroups_Object=MibTableColumn
adGenVectorModuleConfMaxBLVGroups=_AdGenVectorModuleConfMaxBLVGroups_Object((1,3,6,1,4,1,664,5,70,57,1,1,1,2),_AdGenVectorModuleConfMaxBLVGroups_Type())
adGenVectorModuleConfMaxBLVGroups.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenVectorModuleConfMaxBLVGroups.setStatus(_A)
_AdGenVectorModuleConfMaxSLVGroups_Type=Integer32
_AdGenVectorModuleConfMaxSLVGroups_Object=MibTableColumn
adGenVectorModuleConfMaxSLVGroups=_AdGenVectorModuleConfMaxSLVGroups_Object((1,3,6,1,4,1,664,5,70,57,1,1,1,3),_AdGenVectorModuleConfMaxSLVGroups_Type())
adGenVectorModuleConfMaxSLVGroups.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenVectorModuleConfMaxSLVGroups.setStatus(_A)
_AdGenVectorModuleConfMaxPhysPerSLVGroup_Type=Integer32
_AdGenVectorModuleConfMaxPhysPerSLVGroup_Object=MibTableColumn
adGenVectorModuleConfMaxPhysPerSLVGroup=_AdGenVectorModuleConfMaxPhysPerSLVGroup_Object((1,3,6,1,4,1,664,5,70,57,1,1,1,4),_AdGenVectorModuleConfMaxPhysPerSLVGroup_Type())
adGenVectorModuleConfMaxPhysPerSLVGroup.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenVectorModuleConfMaxPhysPerSLVGroup.setStatus(_A)
_AdGenVectorModuleConfNumPhys_Type=Integer32
_AdGenVectorModuleConfNumPhys_Object=MibTableColumn
adGenVectorModuleConfNumPhys=_AdGenVectorModuleConfNumPhys_Object((1,3,6,1,4,1,664,5,70,57,1,1,1,5),_AdGenVectorModuleConfNumPhys_Type())
adGenVectorModuleConfNumPhys.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenVectorModuleConfNumPhys.setStatus(_A)
_AdGenVectorModuleConfVectorEngineHwRev_Type=DisplayString
_AdGenVectorModuleConfVectorEngineHwRev_Object=MibTableColumn
adGenVectorModuleConfVectorEngineHwRev=_AdGenVectorModuleConfVectorEngineHwRev_Object((1,3,6,1,4,1,664,5,70,57,1,1,1,6),_AdGenVectorModuleConfVectorEngineHwRev_Type())
adGenVectorModuleConfVectorEngineHwRev.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenVectorModuleConfVectorEngineHwRev.setStatus(_A)
_AdGenVectorModuleConfVectorEngineSwRev_Type=DisplayString
_AdGenVectorModuleConfVectorEngineSwRev_Object=MibTableColumn
adGenVectorModuleConfVectorEngineSwRev=_AdGenVectorModuleConfVectorEngineSwRev_Object((1,3,6,1,4,1,664,5,70,57,1,1,1,7),_AdGenVectorModuleConfVectorEngineSwRev_Type())
adGenVectorModuleConfVectorEngineSwRev.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenVectorModuleConfVectorEngineSwRev.setStatus(_A)
_AdGenVectorGroupTableLastError_Type=DisplayString
_AdGenVectorGroupTableLastError_Object=MibScalar
adGenVectorGroupTableLastError=_AdGenVectorGroupTableLastError_Object((1,3,6,1,4,1,664,5,70,57,1,2),_AdGenVectorGroupTableLastError_Type())
adGenVectorGroupTableLastError.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenVectorGroupTableLastError.setStatus(_A)
_AdGenVectorGroupTable_Object=MibTable
adGenVectorGroupTable=_AdGenVectorGroupTable_Object((1,3,6,1,4,1,664,5,70,57,1,3))
if mibBuilder.loadTexts:adGenVectorGroupTable.setStatus(_A)
_AdGenVectorGroupEntry_Object=MibTableRow
adGenVectorGroupEntry=_AdGenVectorGroupEntry_Object((1,3,6,1,4,1,664,5,70,57,1,3,1))
adGenVectorGroupEntry.setIndexNames((0,_E,_R))
if mibBuilder.loadTexts:adGenVectorGroupEntry.setStatus(_A)
_AdGenVectorGroupIfIndex_Type=InterfaceIndex
_AdGenVectorGroupIfIndex_Object=MibTableColumn
adGenVectorGroupIfIndex=_AdGenVectorGroupIfIndex_Object((1,3,6,1,4,1,664,5,70,57,1,3,1,1),_AdGenVectorGroupIfIndex_Type())
adGenVectorGroupIfIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:adGenVectorGroupIfIndex.setStatus(_A)
class _AdGenVectorGroupDescription_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,80))
_AdGenVectorGroupDescription_Type.__name__=_Q
_AdGenVectorGroupDescription_Object=MibTableColumn
adGenVectorGroupDescription=_AdGenVectorGroupDescription_Object((1,3,6,1,4,1,664,5,70,57,1,3,1,2),_AdGenVectorGroupDescription_Type())
adGenVectorGroupDescription.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenVectorGroupDescription.setStatus(_A)
_AdGenVectorGroupLastError_Type=DisplayString
_AdGenVectorGroupLastError_Object=MibTableColumn
adGenVectorGroupLastError=_AdGenVectorGroupLastError_Object((1,3,6,1,4,1,664,5,70,57,1,3,1,3),_AdGenVectorGroupLastError_Type())
adGenVectorGroupLastError.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenVectorGroupLastError.setStatus(_A)
_AdGenVectorGroupBandPlan_Type=AdGenVectorGroupBandPlans
_AdGenVectorGroupBandPlan_Object=MibTableColumn
adGenVectorGroupBandPlan=_AdGenVectorGroupBandPlan_Object((1,3,6,1,4,1,664,5,70,57,1,3,1,4),_AdGenVectorGroupBandPlan_Type())
adGenVectorGroupBandPlan.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenVectorGroupBandPlan.setStatus(_A)
_AdGenVectorGroupRowStatus_Type=RowStatus
_AdGenVectorGroupRowStatus_Object=MibTableColumn
adGenVectorGroupRowStatus=_AdGenVectorGroupRowStatus_Object((1,3,6,1,4,1,664,5,70,57,1,3,1,5),_AdGenVectorGroupRowStatus_Type())
adGenVectorGroupRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenVectorGroupRowStatus.setStatus(_A)
class _AdGenVectorGroupFallbackMode_Type(AdGenVectorGroupFallbackModes):defaultValue=3
_AdGenVectorGroupFallbackMode_Type.__name__=_S
_AdGenVectorGroupFallbackMode_Object=MibTableColumn
adGenVectorGroupFallbackMode=_AdGenVectorGroupFallbackMode_Object((1,3,6,1,4,1,664,5,70,57,1,3,1,6),_AdGenVectorGroupFallbackMode_Type())
adGenVectorGroupFallbackMode.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenVectorGroupFallbackMode.setStatus(_A)
class _AdGenVectorGroupFallbackAlarmSeverity_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*(('critical',0),('major',1),('minor',2),('alert',3),('info',4)))
_AdGenVectorGroupFallbackAlarmSeverity_Type.__name__=_C
_AdGenVectorGroupFallbackAlarmSeverity_Object=MibTableColumn
adGenVectorGroupFallbackAlarmSeverity=_AdGenVectorGroupFallbackAlarmSeverity_Object((1,3,6,1,4,1,664,5,70,57,1,3,1,7),_AdGenVectorGroupFallbackAlarmSeverity_Type())
adGenVectorGroupFallbackAlarmSeverity.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenVectorGroupFallbackAlarmSeverity.setStatus(_A)
class _AdGenVectorGroupFallbackAlarmEnable_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_T,0),(_U,1)))
_AdGenVectorGroupFallbackAlarmEnable_Type.__name__=_C
_AdGenVectorGroupFallbackAlarmEnable_Object=MibTableColumn
adGenVectorGroupFallbackAlarmEnable=_AdGenVectorGroupFallbackAlarmEnable_Object((1,3,6,1,4,1,664,5,70,57,1,3,1,8),_AdGenVectorGroupFallbackAlarmEnable_Type())
adGenVectorGroupFallbackAlarmEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenVectorGroupFallbackAlarmEnable.setStatus(_A)
_AdGenVectorGroupVectoringMode_Type=AdGenVectorMode
_AdGenVectorGroupVectoringMode_Object=MibTableColumn
adGenVectorGroupVectoringMode=_AdGenVectorGroupVectoringMode_Object((1,3,6,1,4,1,664,5,70,57,1,3,1,9),_AdGenVectorGroupVectoringMode_Type())
adGenVectorGroupVectoringMode.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenVectorGroupVectoringMode.setStatus(_A)
class _AdGenVectorGroupAutoAddEnable_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_T,0),(_U,1)))
_AdGenVectorGroupAutoAddEnable_Type.__name__=_C
_AdGenVectorGroupAutoAddEnable_Object=MibTableColumn
adGenVectorGroupAutoAddEnable=_AdGenVectorGroupAutoAddEnable_Object((1,3,6,1,4,1,664,5,70,57,1,3,1,10),_AdGenVectorGroupAutoAddEnable_Type())
adGenVectorGroupAutoAddEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenVectorGroupAutoAddEnable.setStatus(_A)
_AdGenVectorPhyMapTableLastError_Type=DisplayString
_AdGenVectorPhyMapTableLastError_Object=MibScalar
adGenVectorPhyMapTableLastError=_AdGenVectorPhyMapTableLastError_Object((1,3,6,1,4,1,664,5,70,57,1,4),_AdGenVectorPhyMapTableLastError_Type())
adGenVectorPhyMapTableLastError.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenVectorPhyMapTableLastError.setStatus(_A)
_AdGenVectorPhyMapTable_Object=MibTable
adGenVectorPhyMapTable=_AdGenVectorPhyMapTable_Object((1,3,6,1,4,1,664,5,70,57,1,5))
if mibBuilder.loadTexts:adGenVectorPhyMapTable.setStatus(_A)
_AdGenVectorPhyMapEntry_Object=MibTableRow
adGenVectorPhyMapEntry=_AdGenVectorPhyMapEntry_Object((1,3,6,1,4,1,664,5,70,57,1,5,1))
adGenVectorPhyMapEntry.setIndexNames((0,_E,_V),(0,_E,_W))
if mibBuilder.loadTexts:adGenVectorPhyMapEntry.setStatus(_A)
_AdGenVectorPhyMapGroupIfIndex_Type=InterfaceIndex
_AdGenVectorPhyMapGroupIfIndex_Object=MibTableColumn
adGenVectorPhyMapGroupIfIndex=_AdGenVectorPhyMapGroupIfIndex_Object((1,3,6,1,4,1,664,5,70,57,1,5,1,1),_AdGenVectorPhyMapGroupIfIndex_Type())
adGenVectorPhyMapGroupIfIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:adGenVectorPhyMapGroupIfIndex.setStatus(_A)
_AdGenVectorPhyMapPhyIfIndex_Type=InterfaceIndex
_AdGenVectorPhyMapPhyIfIndex_Object=MibTableColumn
adGenVectorPhyMapPhyIfIndex=_AdGenVectorPhyMapPhyIfIndex_Object((1,3,6,1,4,1,664,5,70,57,1,5,1,2),_AdGenVectorPhyMapPhyIfIndex_Type())
adGenVectorPhyMapPhyIfIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:adGenVectorPhyMapPhyIfIndex.setStatus(_A)
_AdGenVectorPhyMapLastChange_Type=AdGenVectorLastChange
_AdGenVectorPhyMapLastChange_Object=MibTableColumn
adGenVectorPhyMapLastChange=_AdGenVectorPhyMapLastChange_Object((1,3,6,1,4,1,664,5,70,57,1,5,1,3),_AdGenVectorPhyMapLastChange_Type())
adGenVectorPhyMapLastChange.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenVectorPhyMapLastChange.setStatus(_A)
_AdGenVectorPhyMapLastError_Type=DisplayString
_AdGenVectorPhyMapLastError_Object=MibTableColumn
adGenVectorPhyMapLastError=_AdGenVectorPhyMapLastError_Object((1,3,6,1,4,1,664,5,70,57,1,5,1,4),_AdGenVectorPhyMapLastError_Type())
adGenVectorPhyMapLastError.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenVectorPhyMapLastError.setStatus(_A)
_AdGenVectorPhyMapRowStatus_Type=RowStatus
_AdGenVectorPhyMapRowStatus_Object=MibTableColumn
adGenVectorPhyMapRowStatus=_AdGenVectorPhyMapRowStatus_Object((1,3,6,1,4,1,664,5,70,57,1,5,1,5),_AdGenVectorPhyMapRowStatus_Type())
adGenVectorPhyMapRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenVectorPhyMapRowStatus.setStatus(_A)
_AdGenVectorGroupStatusTable_Object=MibTable
adGenVectorGroupStatusTable=_AdGenVectorGroupStatusTable_Object((1,3,6,1,4,1,664,5,70,57,1,6))
if mibBuilder.loadTexts:adGenVectorGroupStatusTable.setStatus(_A)
_AdGenVectorGroupStatusEntry_Object=MibTableRow
adGenVectorGroupStatusEntry=_AdGenVectorGroupStatusEntry_Object((1,3,6,1,4,1,664,5,70,57,1,6,1))
adGenVectorGroupStatusEntry.setIndexNames((0,_E,_P))
if mibBuilder.loadTexts:adGenVectorGroupStatusEntry.setStatus(_A)
_AdGenVectorGroupStatusIfIndex_Type=InterfaceIndex
_AdGenVectorGroupStatusIfIndex_Object=MibTableColumn
adGenVectorGroupStatusIfIndex=_AdGenVectorGroupStatusIfIndex_Object((1,3,6,1,4,1,664,5,70,57,1,6,1,1),_AdGenVectorGroupStatusIfIndex_Type())
adGenVectorGroupStatusIfIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:adGenVectorGroupStatusIfIndex.setStatus(_A)
_AdGenVectorGroupStatusNumProvisionedPorts_Type=Integer32
_AdGenVectorGroupStatusNumProvisionedPorts_Object=MibTableColumn
adGenVectorGroupStatusNumProvisionedPorts=_AdGenVectorGroupStatusNumProvisionedPorts_Object((1,3,6,1,4,1,664,5,70,57,1,6,1,2),_AdGenVectorGroupStatusNumProvisionedPorts_Type())
adGenVectorGroupStatusNumProvisionedPorts.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenVectorGroupStatusNumProvisionedPorts.setStatus(_A)
_AdGenVectorGroupStatusNumVectoredPorts_Type=Integer32
_AdGenVectorGroupStatusNumVectoredPorts_Object=MibTableColumn
adGenVectorGroupStatusNumVectoredPorts=_AdGenVectorGroupStatusNumVectoredPorts_Object((1,3,6,1,4,1,664,5,70,57,1,6,1,3),_AdGenVectorGroupStatusNumVectoredPorts_Type())
adGenVectorGroupStatusNumVectoredPorts.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenVectorGroupStatusNumVectoredPorts.setStatus(_A)
_AdGenVectorGroupStatusNumUntrainedPorts_Type=Integer32
_AdGenVectorGroupStatusNumUntrainedPorts_Object=MibTableColumn
adGenVectorGroupStatusNumUntrainedPorts=_AdGenVectorGroupStatusNumUntrainedPorts_Object((1,3,6,1,4,1,664,5,70,57,1,6,1,4),_AdGenVectorGroupStatusNumUntrainedPorts_Type())
adGenVectorGroupStatusNumUntrainedPorts.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenVectorGroupStatusNumUntrainedPorts.setStatus(_X)
_AdGenVectorGroupStatusNumVectorFriendlyPorts_Type=Integer32
_AdGenVectorGroupStatusNumVectorFriendlyPorts_Object=MibTableColumn
adGenVectorGroupStatusNumVectorFriendlyPorts=_AdGenVectorGroupStatusNumVectorFriendlyPorts_Object((1,3,6,1,4,1,664,5,70,57,1,6,1,5),_AdGenVectorGroupStatusNumVectorFriendlyPorts_Type())
adGenVectorGroupStatusNumVectorFriendlyPorts.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenVectorGroupStatusNumVectorFriendlyPorts.setStatus(_A)
_AdGenVectorGroupStatusNumNonVectoredPorts_Type=Integer32
_AdGenVectorGroupStatusNumNonVectoredPorts_Object=MibTableColumn
adGenVectorGroupStatusNumNonVectoredPorts=_AdGenVectorGroupStatusNumNonVectoredPorts_Object((1,3,6,1,4,1,664,5,70,57,1,6,1,6),_AdGenVectorGroupStatusNumNonVectoredPorts_Type())
adGenVectorGroupStatusNumNonVectoredPorts.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenVectorGroupStatusNumNonVectoredPorts.setStatus(_A)
_AdGenVectorGroupStatusNumLegacyPorts_Type=Integer32
_AdGenVectorGroupStatusNumLegacyPorts_Object=MibTableColumn
adGenVectorGroupStatusNumLegacyPorts=_AdGenVectorGroupStatusNumLegacyPorts_Object((1,3,6,1,4,1,664,5,70,57,1,6,1,7),_AdGenVectorGroupStatusNumLegacyPorts_Type())
adGenVectorGroupStatusNumLegacyPorts.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenVectorGroupStatusNumLegacyPorts.setStatus(_A)
_AdGenVectorGroupStatusOperStatus_Type=AdGenVectorGroupOperStatus
_AdGenVectorGroupStatusOperStatus_Object=MibTableColumn
adGenVectorGroupStatusOperStatus=_AdGenVectorGroupStatusOperStatus_Object((1,3,6,1,4,1,664,5,70,57,1,6,1,8),_AdGenVectorGroupStatusOperStatus_Type())
adGenVectorGroupStatusOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenVectorGroupStatusOperStatus.setStatus(_A)
class _AdGenVectorGroupStatusReset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('reset',1))
_AdGenVectorGroupStatusReset_Type.__name__=_C
_AdGenVectorGroupStatusReset_Object=MibTableColumn
adGenVectorGroupStatusReset=_AdGenVectorGroupStatusReset_Object((1,3,6,1,4,1,664,5,70,57,1,6,1,9),_AdGenVectorGroupStatusReset_Type())
adGenVectorGroupStatusReset.setMaxAccess(_H)
if mibBuilder.loadTexts:adGenVectorGroupStatusReset.setStatus(_A)
_AdGenVectorGroupStatusNumFallbackPorts_Type=Integer32
_AdGenVectorGroupStatusNumFallbackPorts_Object=MibTableColumn
adGenVectorGroupStatusNumFallbackPorts=_AdGenVectorGroupStatusNumFallbackPorts_Object((1,3,6,1,4,1,664,5,70,57,1,6,1,10),_AdGenVectorGroupStatusNumFallbackPorts_Type())
adGenVectorGroupStatusNumFallbackPorts.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenVectorGroupStatusNumFallbackPorts.setStatus(_A)
_AdGenVectorPhyStatusTable_Object=MibTable
adGenVectorPhyStatusTable=_AdGenVectorPhyStatusTable_Object((1,3,6,1,4,1,664,5,70,57,1,7))
if mibBuilder.loadTexts:adGenVectorPhyStatusTable.setStatus(_A)
_AdGenVectorPhyStatusEntry_Object=MibTableRow
adGenVectorPhyStatusEntry=_AdGenVectorPhyStatusEntry_Object((1,3,6,1,4,1,664,5,70,57,1,7,1))
adGenVectorPhyStatusEntry.setIndexNames((0,_E,_Y))
if mibBuilder.loadTexts:adGenVectorPhyStatusEntry.setStatus(_A)
_AdGenVectorPhyStatusPhyIfIndex_Type=InterfaceIndex
_AdGenVectorPhyStatusPhyIfIndex_Object=MibTableColumn
adGenVectorPhyStatusPhyIfIndex=_AdGenVectorPhyStatusPhyIfIndex_Object((1,3,6,1,4,1,664,5,70,57,1,7,1,1),_AdGenVectorPhyStatusPhyIfIndex_Type())
adGenVectorPhyStatusPhyIfIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:adGenVectorPhyStatusPhyIfIndex.setStatus(_A)
_AdGenVectorPhyStatusGroupIfIndex_Type=InterfaceIndex
_AdGenVectorPhyStatusGroupIfIndex_Object=MibTableColumn
adGenVectorPhyStatusGroupIfIndex=_AdGenVectorPhyStatusGroupIfIndex_Object((1,3,6,1,4,1,664,5,70,57,1,7,1,2),_AdGenVectorPhyStatusGroupIfIndex_Type())
adGenVectorPhyStatusGroupIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenVectorPhyStatusGroupIfIndex.setStatus(_A)
_AdGenVectorPhyStatusGroupType_Type=AdGenVectorMode
_AdGenVectorPhyStatusGroupType_Object=MibTableColumn
adGenVectorPhyStatusGroupType=_AdGenVectorPhyStatusGroupType_Object((1,3,6,1,4,1,664,5,70,57,1,7,1,3),_AdGenVectorPhyStatusGroupType_Type())
adGenVectorPhyStatusGroupType.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenVectorPhyStatusGroupType.setStatus(_A)
_AdGenVectorPhyStatusPortLineState_Type=AdGenVectorPhyLineState
_AdGenVectorPhyStatusPortLineState_Object=MibTableColumn
adGenVectorPhyStatusPortLineState=_AdGenVectorPhyStatusPortLineState_Object((1,3,6,1,4,1,664,5,70,57,1,7,1,4),_AdGenVectorPhyStatusPortLineState_Type())
adGenVectorPhyStatusPortLineState.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenVectorPhyStatusPortLineState.setStatus(_X)
_AdGenVectorPhyStatusPortVectoringState_Type=AdGenVectorPhyPortVectoringState
_AdGenVectorPhyStatusPortVectoringState_Object=MibTableColumn
adGenVectorPhyStatusPortVectoringState=_AdGenVectorPhyStatusPortVectoringState_Object((1,3,6,1,4,1,664,5,70,57,1,7,1,5),_AdGenVectorPhyStatusPortVectoringState_Type())
adGenVectorPhyStatusPortVectoringState.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenVectorPhyStatusPortVectoringState.setStatus(_A)
_AdGenVectorPhyStatusVectoringError_Type=DisplayString
_AdGenVectorPhyStatusVectoringError_Object=MibTableColumn
adGenVectorPhyStatusVectoringError=_AdGenVectorPhyStatusVectoringError_Object((1,3,6,1,4,1,664,5,70,57,1,7,1,6),_AdGenVectorPhyStatusVectoringError_Type())
adGenVectorPhyStatusVectoringError.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenVectorPhyStatusVectoringError.setStatus(_A)
_AdGenVectorPhyStatusVectoringErrorTimestamp_Type=AdGenVectorPhyPortErrorTimestamp
_AdGenVectorPhyStatusVectoringErrorTimestamp_Object=MibTableColumn
adGenVectorPhyStatusVectoringErrorTimestamp=_AdGenVectorPhyStatusVectoringErrorTimestamp_Object((1,3,6,1,4,1,664,5,70,57,1,7,1,7),_AdGenVectorPhyStatusVectoringErrorTimestamp_Type())
adGenVectorPhyStatusVectoringErrorTimestamp.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenVectorPhyStatusVectoringErrorTimestamp.setStatus(_A)
if mibBuilder.loadTexts:adGenVectorPhyStatusVectoringErrorTimestamp.setUnits('seconds')
_AdGenVectorPhyStatusVectoringErrorDateTime_Type=DisplayString
_AdGenVectorPhyStatusVectoringErrorDateTime_Object=MibTableColumn
adGenVectorPhyStatusVectoringErrorDateTime=_AdGenVectorPhyStatusVectoringErrorDateTime_Object((1,3,6,1,4,1,664,5,70,57,1,7,1,8),_AdGenVectorPhyStatusVectoringErrorDateTime_Type())
adGenVectorPhyStatusVectoringErrorDateTime.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenVectorPhyStatusVectoringErrorDateTime.setStatus(_A)
_AdGenVectorAlarmsPrefix_ObjectIdentity=ObjectIdentity
adGenVectorAlarmsPrefix=_AdGenVectorAlarmsPrefix_ObjectIdentity((1,3,6,1,4,1,664,5,70,57,1,8))
_AdGenVectorAlarms_ObjectIdentity=ObjectIdentity
adGenVectorAlarms=_AdGenVectorAlarms_ObjectIdentity((1,3,6,1,4,1,664,5,70,57,1,8,0))
_AdGenVectorSlotConfTable_Object=MibTable
adGenVectorSlotConfTable=_AdGenVectorSlotConfTable_Object((1,3,6,1,4,1,664,5,70,57,1,9))
if mibBuilder.loadTexts:adGenVectorSlotConfTable.setStatus(_A)
_AdGenVectorSlotConfEntry_Object=MibTableRow
adGenVectorSlotConfEntry=_AdGenVectorSlotConfEntry_Object((1,3,6,1,4,1,664,5,70,57,1,9,1))
adGenVectorSlotConfEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:adGenVectorSlotConfEntry.setStatus(_A)
class _AdGenVectorSlotConfForceFallback_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('forceSlotFallback',1),('allowVectoring',2)))
_AdGenVectorSlotConfForceFallback_Type.__name__=_C
_AdGenVectorSlotConfForceFallback_Object=MibTableColumn
adGenVectorSlotConfForceFallback=_AdGenVectorSlotConfForceFallback_Object((1,3,6,1,4,1,664,5,70,57,1,9,1,1),_AdGenVectorSlotConfForceFallback_Type())
adGenVectorSlotConfForceFallback.setMaxAccess(_H)
if mibBuilder.loadTexts:adGenVectorSlotConfForceFallback.setStatus(_A)
_AdGenVectorSlotStatusTable_Object=MibTable
adGenVectorSlotStatusTable=_AdGenVectorSlotStatusTable_Object((1,3,6,1,4,1,664,5,70,57,1,10))
if mibBuilder.loadTexts:adGenVectorSlotStatusTable.setStatus(_A)
_AdGenVectorSlotStatusEntry_Object=MibTableRow
adGenVectorSlotStatusEntry=_AdGenVectorSlotStatusEntry_Object((1,3,6,1,4,1,664,5,70,57,1,10,1))
adGenVectorSlotStatusEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:adGenVectorSlotStatusEntry.setStatus(_A)
class _AdGenVectorSlotStatusFallbackState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('fallbackActive',1),('fallbackInactive',2)))
_AdGenVectorSlotStatusFallbackState_Type.__name__=_C
_AdGenVectorSlotStatusFallbackState_Object=MibTableColumn
adGenVectorSlotStatusFallbackState=_AdGenVectorSlotStatusFallbackState_Object((1,3,6,1,4,1,664,5,70,57,1,10,1,1),_AdGenVectorSlotStatusFallbackState_Type())
adGenVectorSlotStatusFallbackState.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenVectorSlotStatusFallbackState.setStatus(_A)
_AdGenVectorBulk_ObjectIdentity=ObjectIdentity
adGenVectorBulk=_AdGenVectorBulk_ObjectIdentity((1,3,6,1,4,1,664,5,70,57,2))
_AdGenVectorBulkInstanceTable_Object=MibTable
adGenVectorBulkInstanceTable=_AdGenVectorBulkInstanceTable_Object((1,3,6,1,4,1,664,5,70,57,2,1))
if mibBuilder.loadTexts:adGenVectorBulkInstanceTable.setStatus(_A)
_AdGenVectorBulkInstanceEntry_Object=MibTableRow
adGenVectorBulkInstanceEntry=_AdGenVectorBulkInstanceEntry_Object((1,3,6,1,4,1,664,5,70,57,2,1,1))
adGenVectorBulkInstanceEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:adGenVectorBulkInstanceEntry.setStatus(_A)
_AdGenVectorBulkReserveSlotInstance_Type=Integer32
_AdGenVectorBulkReserveSlotInstance_Object=MibTableColumn
adGenVectorBulkReserveSlotInstance=_AdGenVectorBulkReserveSlotInstance_Object((1,3,6,1,4,1,664,5,70,57,2,1,1,1),_AdGenVectorBulkReserveSlotInstance_Type())
adGenVectorBulkReserveSlotInstance.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenVectorBulkReserveSlotInstance.setStatus(_A)
_AdGenVectorBulkFilterTable_Object=MibTable
adGenVectorBulkFilterTable=_AdGenVectorBulkFilterTable_Object((1,3,6,1,4,1,664,5,70,57,2,2))
if mibBuilder.loadTexts:adGenVectorBulkFilterTable.setStatus(_A)
_AdGenVectorBulkFilterEntry_Object=MibTableRow
adGenVectorBulkFilterEntry=_AdGenVectorBulkFilterEntry_Object((1,3,6,1,4,1,664,5,70,57,2,2,1))
adGenVectorBulkFilterEntry.setIndexNames((0,_E,_P),(0,_E,_Z))
if mibBuilder.loadTexts:adGenVectorBulkFilterEntry.setStatus(_A)
_AdGenVectorBulkFilterInstance_Type=Integer32
_AdGenVectorBulkFilterInstance_Object=MibTableColumn
adGenVectorBulkFilterInstance=_AdGenVectorBulkFilterInstance_Object((1,3,6,1,4,1,664,5,70,57,2,2,1,1),_AdGenVectorBulkFilterInstance_Type())
adGenVectorBulkFilterInstance.setMaxAccess(_I)
if mibBuilder.loadTexts:adGenVectorBulkFilterInstance.setStatus(_A)
_AdGenVectorBulkFilterInterface_Type=InterfaceIndex
_AdGenVectorBulkFilterInterface_Object=MibTableColumn
adGenVectorBulkFilterInterface=_AdGenVectorBulkFilterInterface_Object((1,3,6,1,4,1,664,5,70,57,2,2,1,2),_AdGenVectorBulkFilterInterface_Type())
adGenVectorBulkFilterInterface.setMaxAccess(_H)
if mibBuilder.loadTexts:adGenVectorBulkFilterInterface.setStatus(_A)
_AdGenVectorBulkFilterSlot_Type=Integer32
_AdGenVectorBulkFilterSlot_Object=MibTableColumn
adGenVectorBulkFilterSlot=_AdGenVectorBulkFilterSlot_Object((1,3,6,1,4,1,664,5,70,57,2,2,1,3),_AdGenVectorBulkFilterSlot_Type())
adGenVectorBulkFilterSlot.setMaxAccess(_H)
if mibBuilder.loadTexts:adGenVectorBulkFilterSlot.setStatus(_A)
class _AdGenVectorBulkFilterDirection_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('upstream',1),('downstream',2)))
_AdGenVectorBulkFilterDirection_Type.__name__=_C
_AdGenVectorBulkFilterDirection_Object=MibTableColumn
adGenVectorBulkFilterDirection=_AdGenVectorBulkFilterDirection_Object((1,3,6,1,4,1,664,5,70,57,2,2,1,4),_AdGenVectorBulkFilterDirection_Type())
adGenVectorBulkFilterDirection.setMaxAccess(_H)
if mibBuilder.loadTexts:adGenVectorBulkFilterDirection.setStatus(_A)
class _AdGenVectorBulkFilterType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('weights',1))
_AdGenVectorBulkFilterType_Type.__name__=_C
_AdGenVectorBulkFilterType_Object=MibTableColumn
adGenVectorBulkFilterType=_AdGenVectorBulkFilterType_Object((1,3,6,1,4,1,664,5,70,57,2,2,1,5),_AdGenVectorBulkFilterType_Type())
adGenVectorBulkFilterType.setMaxAccess(_H)
if mibBuilder.loadTexts:adGenVectorBulkFilterType.setStatus(_A)
class _AdGenVectorBulkSlotCreate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('updateinstance',1))
_AdGenVectorBulkSlotCreate_Type.__name__=_C
_AdGenVectorBulkSlotCreate_Object=MibTableColumn
adGenVectorBulkSlotCreate=_AdGenVectorBulkSlotCreate_Object((1,3,6,1,4,1,664,5,70,57,2,2,1,6),_AdGenVectorBulkSlotCreate_Type())
adGenVectorBulkSlotCreate.setMaxAccess(_H)
if mibBuilder.loadTexts:adGenVectorBulkSlotCreate.setStatus(_A)
adGenVectorAlarmsForcedFallbackClr=NotificationType((1,3,6,1,4,1,664,5,70,57,1,8,0,2))
adGenVectorAlarmsForcedFallbackClr.setObjects(*((_J,_K),(_N,_O),(_F,_G),(_L,_M)))
if mibBuilder.loadTexts:adGenVectorAlarmsForcedFallbackClr.setStatus(_A)
adGenVectorAlarmsForcedFallbackAct=NotificationType((1,3,6,1,4,1,664,5,70,57,1,8,0,3))
adGenVectorAlarmsForcedFallbackAct.setObjects(*((_J,_K),(_N,_O),(_F,_G),(_L,_M)))
if mibBuilder.loadTexts:adGenVectorAlarmsForcedFallbackAct.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'AdGenVectorMode':AdGenVectorMode,'AdGenVectorGroupOperStatus':AdGenVectorGroupOperStatus,'AdGenVectorLastChange':AdGenVectorLastChange,'AdGenVectorPhyPortErrorTimestamp':AdGenVectorPhyPortErrorTimestamp,'AdGenVectorPhyLineState':AdGenVectorPhyLineState,'AdGenVectorPhyPortVectoringState':AdGenVectorPhyPortVectoringState,'AdGenVectorGroupBandPlans':AdGenVectorGroupBandPlans,_S:AdGenVectorGroupFallbackModes,'adGenVectorMIBObjects':adGenVectorMIBObjects,'adGenVectorModuleConfTable':adGenVectorModuleConfTable,'adGenVectorModuleConfEntry':adGenVectorModuleConfEntry,'adGenVectorModuleConfSupportedVectorModeTypes':adGenVectorModuleConfSupportedVectorModeTypes,'adGenVectorModuleConfMaxBLVGroups':adGenVectorModuleConfMaxBLVGroups,'adGenVectorModuleConfMaxSLVGroups':adGenVectorModuleConfMaxSLVGroups,'adGenVectorModuleConfMaxPhysPerSLVGroup':adGenVectorModuleConfMaxPhysPerSLVGroup,'adGenVectorModuleConfNumPhys':adGenVectorModuleConfNumPhys,'adGenVectorModuleConfVectorEngineHwRev':adGenVectorModuleConfVectorEngineHwRev,'adGenVectorModuleConfVectorEngineSwRev':adGenVectorModuleConfVectorEngineSwRev,'adGenVectorGroupTableLastError':adGenVectorGroupTableLastError,'adGenVectorGroupTable':adGenVectorGroupTable,'adGenVectorGroupEntry':adGenVectorGroupEntry,_R:adGenVectorGroupIfIndex,'adGenVectorGroupDescription':adGenVectorGroupDescription,'adGenVectorGroupLastError':adGenVectorGroupLastError,'adGenVectorGroupBandPlan':adGenVectorGroupBandPlan,'adGenVectorGroupRowStatus':adGenVectorGroupRowStatus,'adGenVectorGroupFallbackMode':adGenVectorGroupFallbackMode,'adGenVectorGroupFallbackAlarmSeverity':adGenVectorGroupFallbackAlarmSeverity,'adGenVectorGroupFallbackAlarmEnable':adGenVectorGroupFallbackAlarmEnable,'adGenVectorGroupVectoringMode':adGenVectorGroupVectoringMode,'adGenVectorGroupAutoAddEnable':adGenVectorGroupAutoAddEnable,'adGenVectorPhyMapTableLastError':adGenVectorPhyMapTableLastError,'adGenVectorPhyMapTable':adGenVectorPhyMapTable,'adGenVectorPhyMapEntry':adGenVectorPhyMapEntry,_V:adGenVectorPhyMapGroupIfIndex,_W:adGenVectorPhyMapPhyIfIndex,'adGenVectorPhyMapLastChange':adGenVectorPhyMapLastChange,'adGenVectorPhyMapLastError':adGenVectorPhyMapLastError,'adGenVectorPhyMapRowStatus':adGenVectorPhyMapRowStatus,'adGenVectorGroupStatusTable':adGenVectorGroupStatusTable,'adGenVectorGroupStatusEntry':adGenVectorGroupStatusEntry,_P:adGenVectorGroupStatusIfIndex,'adGenVectorGroupStatusNumProvisionedPorts':adGenVectorGroupStatusNumProvisionedPorts,'adGenVectorGroupStatusNumVectoredPorts':adGenVectorGroupStatusNumVectoredPorts,'adGenVectorGroupStatusNumUntrainedPorts':adGenVectorGroupStatusNumUntrainedPorts,'adGenVectorGroupStatusNumVectorFriendlyPorts':adGenVectorGroupStatusNumVectorFriendlyPorts,'adGenVectorGroupStatusNumNonVectoredPorts':adGenVectorGroupStatusNumNonVectoredPorts,'adGenVectorGroupStatusNumLegacyPorts':adGenVectorGroupStatusNumLegacyPorts,'adGenVectorGroupStatusOperStatus':adGenVectorGroupStatusOperStatus,'adGenVectorGroupStatusReset':adGenVectorGroupStatusReset,'adGenVectorGroupStatusNumFallbackPorts':adGenVectorGroupStatusNumFallbackPorts,'adGenVectorPhyStatusTable':adGenVectorPhyStatusTable,'adGenVectorPhyStatusEntry':adGenVectorPhyStatusEntry,_Y:adGenVectorPhyStatusPhyIfIndex,'adGenVectorPhyStatusGroupIfIndex':adGenVectorPhyStatusGroupIfIndex,'adGenVectorPhyStatusGroupType':adGenVectorPhyStatusGroupType,'adGenVectorPhyStatusPortLineState':adGenVectorPhyStatusPortLineState,'adGenVectorPhyStatusPortVectoringState':adGenVectorPhyStatusPortVectoringState,'adGenVectorPhyStatusVectoringError':adGenVectorPhyStatusVectoringError,'adGenVectorPhyStatusVectoringErrorTimestamp':adGenVectorPhyStatusVectoringErrorTimestamp,'adGenVectorPhyStatusVectoringErrorDateTime':adGenVectorPhyStatusVectoringErrorDateTime,'adGenVectorAlarmsPrefix':adGenVectorAlarmsPrefix,'adGenVectorAlarms':adGenVectorAlarms,'adGenVectorAlarmsForcedFallbackClr':adGenVectorAlarmsForcedFallbackClr,'adGenVectorAlarmsForcedFallbackAct':adGenVectorAlarmsForcedFallbackAct,'adGenVectorSlotConfTable':adGenVectorSlotConfTable,'adGenVectorSlotConfEntry':adGenVectorSlotConfEntry,'adGenVectorSlotConfForceFallback':adGenVectorSlotConfForceFallback,'adGenVectorSlotStatusTable':adGenVectorSlotStatusTable,'adGenVectorSlotStatusEntry':adGenVectorSlotStatusEntry,'adGenVectorSlotStatusFallbackState':adGenVectorSlotStatusFallbackState,'adGenVectorBulk':adGenVectorBulk,'adGenVectorBulkInstanceTable':adGenVectorBulkInstanceTable,'adGenVectorBulkInstanceEntry':adGenVectorBulkInstanceEntry,'adGenVectorBulkReserveSlotInstance':adGenVectorBulkReserveSlotInstance,'adGenVectorBulkFilterTable':adGenVectorBulkFilterTable,'adGenVectorBulkFilterEntry':adGenVectorBulkFilterEntry,_Z:adGenVectorBulkFilterInstance,'adGenVectorBulkFilterInterface':adGenVectorBulkFilterInterface,'adGenVectorBulkFilterSlot':adGenVectorBulkFilterSlot,'adGenVectorBulkFilterDirection':adGenVectorBulkFilterDirection,'adGenVectorBulkFilterType':adGenVectorBulkFilterType,'adGenVectorBulkSlotCreate':adGenVectorBulkSlotCreate,'adGenVectorMIB':adGenVectorMIB})