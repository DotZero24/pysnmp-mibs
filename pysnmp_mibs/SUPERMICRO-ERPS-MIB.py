_i='fsErpsTypeOfFailure'
_h='fsErpsRingNodeStatus'
_g='fsErpsRingSemState'
_f='fsErpsTrapSwitchingMechanism'
_e='accessible-for-notify'
_d='fsErpsRingTcPropRingId'
_c='remote'
_b='secondary'
_a='primary'
_Z='RingServiceType'
_Y='disabled'
_X='unblocked'
_W='blocked'
_V='RingMonitorMechanismType'
_U='fsErpsVlanGroupId'
_T='fsErpsVlanId'
_S='fsErpsRingName'
_R='fsErpsCtxtName'
_Q='none'
_P='disable'
_O='enable'
_N='not-accessible'
_M='DisplayString'
_L='OctetString'
_K='milliseconds'
_J='InterfaceIndexOrZero'
_I='fsErpsRingId'
_H='TruthValue'
_G='Unsigned32'
_F='fsErpsContextId'
_E='Integer32'
_D='SUPERMICRO-ERPS-MIB'
_C='read-write'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_L,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
Dot1agCfmMepId,=mibBuilder.importSymbols('IEEE8021-CFM-MIB','Dot1agCfmMepId')
InterfaceIndex,InterfaceIndexOrZero=mibBuilder.importSymbols('IF-MIB','InterfaceIndex',_J)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_G,'enterprises','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_M,'MacAddress','PhysAddress','RowStatus','TextualConvention',_H)
VlanId,=mibBuilder.importSymbols('SUPERMICROQ-BRIDGE-MIB','VlanId')
fsErpsMIB=ModuleIdentity((1,3,6,1,4,1,10876,101,2,40))
if mibBuilder.loadTexts:fsErpsMIB.setRevisions(('2012-09-05 00:00',))
class RingId(TextualConvention,Unsigned32):status=_A;displayHint='d';subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
class RingMonitorMechanismType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('cfm',1),('mplsOam',2)))
class RingIdOrNone(TextualConvention,Unsigned32):status=_A;displayHint='d';subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,4294967295))
class RingServiceType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('vlan',1),('mplsLSP',2),('mplsPW',3),('mplsLSPPW',4)))
_FsErpsContext_ObjectIdentity=ObjectIdentity
fsErpsContext=_FsErpsContext_ObjectIdentity((1,3,6,1,4,1,10876,101,2,40,1))
_FsErpsContextTable_Object=MibTable
fsErpsContextTable=_FsErpsContextTable_Object((1,3,6,1,4,1,10876,101,2,40,1,1))
if mibBuilder.loadTexts:fsErpsContextTable.setStatus(_A)
_FsErpsContextEntry_Object=MibTableRow
fsErpsContextEntry=_FsErpsContextEntry_Object((1,3,6,1,4,1,10876,101,2,40,1,1,1))
fsErpsContextEntry.setIndexNames((0,_D,_F))
if mibBuilder.loadTexts:fsErpsContextEntry.setStatus(_A)
_FsErpsContextId_Type=Unsigned32
_FsErpsContextId_Object=MibTableColumn
fsErpsContextId=_FsErpsContextId_Object((1,3,6,1,4,1,10876,101,2,40,1,1,1,1),_FsErpsContextId_Type())
fsErpsContextId.setMaxAccess(_N)
if mibBuilder.loadTexts:fsErpsContextId.setStatus(_A)
class _FsErpsCtxtName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_FsErpsCtxtName_Type.__name__=_M
_FsErpsCtxtName_Object=MibTableColumn
fsErpsCtxtName=_FsErpsCtxtName_Object((1,3,6,1,4,1,10876,101,2,40,1,1,1,2),_FsErpsCtxtName_Type())
fsErpsCtxtName.setMaxAccess(_B)
if mibBuilder.loadTexts:fsErpsCtxtName.setStatus(_A)
class _FsErpsCtxtSystemControl_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('start',1),('shutdown',2)))
_FsErpsCtxtSystemControl_Type.__name__=_E
_FsErpsCtxtSystemControl_Object=MibTableColumn
fsErpsCtxtSystemControl=_FsErpsCtxtSystemControl_Object((1,3,6,1,4,1,10876,101,2,40,1,1,1,3),_FsErpsCtxtSystemControl_Type())
fsErpsCtxtSystemControl.setMaxAccess(_C)
if mibBuilder.loadTexts:fsErpsCtxtSystemControl.setStatus(_A)
class _FsErpsCtxtModuleStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_O,1),(_P,2)))
_FsErpsCtxtModuleStatus_Type.__name__=_E
_FsErpsCtxtModuleStatus_Object=MibTableColumn
fsErpsCtxtModuleStatus=_FsErpsCtxtModuleStatus_Object((1,3,6,1,4,1,10876,101,2,40,1,1,1,4),_FsErpsCtxtModuleStatus_Type())
fsErpsCtxtModuleStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:fsErpsCtxtModuleStatus.setStatus(_A)
class _FsErpsCtxtTraceInput_Type(DisplayString):defaultValue=OctetString('critical');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_FsErpsCtxtTraceInput_Type.__name__=_M
_FsErpsCtxtTraceInput_Object=MibTableColumn
fsErpsCtxtTraceInput=_FsErpsCtxtTraceInput_Object((1,3,6,1,4,1,10876,101,2,40,1,1,1,5),_FsErpsCtxtTraceInput_Type())
fsErpsCtxtTraceInput.setMaxAccess(_C)
if mibBuilder.loadTexts:fsErpsCtxtTraceInput.setStatus(_A)
class _FsErpsCtxtTrapStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_O,1),(_P,2)))
_FsErpsCtxtTrapStatus_Type.__name__=_E
_FsErpsCtxtTrapStatus_Object=MibTableColumn
fsErpsCtxtTrapStatus=_FsErpsCtxtTrapStatus_Object((1,3,6,1,4,1,10876,101,2,40,1,1,1,6),_FsErpsCtxtTrapStatus_Type())
fsErpsCtxtTrapStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:fsErpsCtxtTrapStatus.setStatus(_A)
class _FsErpsCtxtClearRingStats_Type(TruthValue):defaultValue=2
_FsErpsCtxtClearRingStats_Type.__name__=_H
_FsErpsCtxtClearRingStats_Object=MibTableColumn
fsErpsCtxtClearRingStats=_FsErpsCtxtClearRingStats_Object((1,3,6,1,4,1,10876,101,2,40,1,1,1,7),_FsErpsCtxtClearRingStats_Type())
fsErpsCtxtClearRingStats.setMaxAccess(_C)
if mibBuilder.loadTexts:fsErpsCtxtClearRingStats.setStatus(_A)
_FsErpsCtxtRowStatus_Type=RowStatus
_FsErpsCtxtRowStatus_Object=MibTableColumn
fsErpsCtxtRowStatus=_FsErpsCtxtRowStatus_Object((1,3,6,1,4,1,10876,101,2,40,1,1,1,8),_FsErpsCtxtRowStatus_Type())
fsErpsCtxtRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:fsErpsCtxtRowStatus.setStatus(_A)
class _FsErpsCtxtVlanGroupManager_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('mstp',1),('erps',2)))
_FsErpsCtxtVlanGroupManager_Type.__name__=_E
_FsErpsCtxtVlanGroupManager_Object=MibTableColumn
fsErpsCtxtVlanGroupManager=_FsErpsCtxtVlanGroupManager_Object((1,3,6,1,4,1,10876,101,2,40,1,1,1,9),_FsErpsCtxtVlanGroupManager_Type())
fsErpsCtxtVlanGroupManager.setMaxAccess(_C)
if mibBuilder.loadTexts:fsErpsCtxtVlanGroupManager.setStatus(_A)
class _FsErpsCtxtProprietaryClearFS_Type(TruthValue):defaultValue=2
_FsErpsCtxtProprietaryClearFS_Type.__name__=_H
_FsErpsCtxtProprietaryClearFS_Object=MibTableColumn
fsErpsCtxtProprietaryClearFS=_FsErpsCtxtProprietaryClearFS_Object((1,3,6,1,4,1,10876,101,2,40,1,1,1,10),_FsErpsCtxtProprietaryClearFS_Type())
fsErpsCtxtProprietaryClearFS.setMaxAccess(_C)
if mibBuilder.loadTexts:fsErpsCtxtProprietaryClearFS.setStatus(_A)
_FsErpsVlanGroupTable_Object=MibTable
fsErpsVlanGroupTable=_FsErpsVlanGroupTable_Object((1,3,6,1,4,1,10876,101,2,40,1,2))
if mibBuilder.loadTexts:fsErpsVlanGroupTable.setStatus(_A)
_FsErpsVlanGroupEntry_Object=MibTableRow
fsErpsVlanGroupEntry=_FsErpsVlanGroupEntry_Object((1,3,6,1,4,1,10876,101,2,40,1,2,1))
fsErpsVlanGroupEntry.setIndexNames((0,_D,_F),(0,_D,_T),(0,_D,_U))
if mibBuilder.loadTexts:fsErpsVlanGroupEntry.setStatus(_A)
_FsErpsVlanId_Type=VlanId
_FsErpsVlanId_Object=MibTableColumn
fsErpsVlanId=_FsErpsVlanId_Object((1,3,6,1,4,1,10876,101,2,40,1,2,1,1),_FsErpsVlanId_Type())
fsErpsVlanId.setMaxAccess(_N)
if mibBuilder.loadTexts:fsErpsVlanId.setStatus(_A)
class _FsErpsVlanGroupId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,64))
_FsErpsVlanGroupId_Type.__name__=_E
_FsErpsVlanGroupId_Object=MibTableColumn
fsErpsVlanGroupId=_FsErpsVlanGroupId_Object((1,3,6,1,4,1,10876,101,2,40,1,2,1,2),_FsErpsVlanGroupId_Type())
fsErpsVlanGroupId.setMaxAccess(_N)
if mibBuilder.loadTexts:fsErpsVlanGroupId.setStatus(_A)
_FsErpsVlanGroupRowStatus_Type=RowStatus
_FsErpsVlanGroupRowStatus_Object=MibTableColumn
fsErpsVlanGroupRowStatus=_FsErpsVlanGroupRowStatus_Object((1,3,6,1,4,1,10876,101,2,40,1,2,1,3),_FsErpsVlanGroupRowStatus_Type())
fsErpsVlanGroupRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:fsErpsVlanGroupRowStatus.setStatus(_A)
_FsErpsRing_ObjectIdentity=ObjectIdentity
fsErpsRing=_FsErpsRing_ObjectIdentity((1,3,6,1,4,1,10876,101,2,40,2))
_FsErpsRingTable_Object=MibTable
fsErpsRingTable=_FsErpsRingTable_Object((1,3,6,1,4,1,10876,101,2,40,2,1))
if mibBuilder.loadTexts:fsErpsRingTable.setStatus(_A)
_FsErpsRingEntry_Object=MibTableRow
fsErpsRingEntry=_FsErpsRingEntry_Object((1,3,6,1,4,1,10876,101,2,40,2,1,1))
fsErpsRingEntry.setIndexNames((0,_D,_F),(0,_D,_I))
if mibBuilder.loadTexts:fsErpsRingEntry.setStatus(_A)
_FsErpsRingId_Type=RingId
_FsErpsRingId_Object=MibTableColumn
fsErpsRingId=_FsErpsRingId_Object((1,3,6,1,4,1,10876,101,2,40,2,1,1,1),_FsErpsRingId_Type())
fsErpsRingId.setMaxAccess(_N)
if mibBuilder.loadTexts:fsErpsRingId.setStatus(_A)
_FsErpsRingVlanId_Type=VlanId
_FsErpsRingVlanId_Object=MibTableColumn
fsErpsRingVlanId=_FsErpsRingVlanId_Object((1,3,6,1,4,1,10876,101,2,40,2,1,1,2),_FsErpsRingVlanId_Type())
fsErpsRingVlanId.setMaxAccess(_C)
if mibBuilder.loadTexts:fsErpsRingVlanId.setStatus(_A)
_FsErpsRingName_Type=DisplayString
_FsErpsRingName_Object=MibTableColumn
fsErpsRingName=_FsErpsRingName_Object((1,3,6,1,4,1,10876,101,2,40,2,1,1,3),_FsErpsRingName_Type())
fsErpsRingName.setMaxAccess(_C)
if mibBuilder.loadTexts:fsErpsRingName.setStatus(_A)
_FsErpsRingPort1_Type=InterfaceIndex
_FsErpsRingPort1_Object=MibTableColumn
fsErpsRingPort1=_FsErpsRingPort1_Object((1,3,6,1,4,1,10876,101,2,40,2,1,1,4),_FsErpsRingPort1_Type())
fsErpsRingPort1.setMaxAccess(_C)
if mibBuilder.loadTexts:fsErpsRingPort1.setStatus(_A)
_FsErpsRingPort2_Type=InterfaceIndexOrZero
_FsErpsRingPort2_Object=MibTableColumn
fsErpsRingPort2=_FsErpsRingPort2_Object((1,3,6,1,4,1,10876,101,2,40,2,1,1,5),_FsErpsRingPort2_Type())
fsErpsRingPort2.setMaxAccess(_C)
if mibBuilder.loadTexts:fsErpsRingPort2.setStatus(_A)
class _FsErpsRingRplPort_Type(InterfaceIndexOrZero):defaultValue=0
_FsErpsRingRplPort_Type.__name__=_J
_FsErpsRingRplPort_Object=MibTableColumn
fsErpsRingRplPort=_FsErpsRingRplPort_Object((1,3,6,1,4,1,10876,101,2,40,2,1,1,6),_FsErpsRingRplPort_Type())
fsErpsRingRplPort.setMaxAccess(_C)
if mibBuilder.loadTexts:fsErpsRingRplPort.setStatus(_A)
class _FsErpsRingPortBlockingOnVcRecovery_Type(TruthValue):defaultValue=2
_FsErpsRingPortBlockingOnVcRecovery_Type.__name__=_H
_FsErpsRingPortBlockingOnVcRecovery_Object=MibTableColumn
fsErpsRingPortBlockingOnVcRecovery=_FsErpsRingPortBlockingOnVcRecovery_Object((1,3,6,1,4,1,10876,101,2,40,2,1,1,7),_FsErpsRingPortBlockingOnVcRecovery_Type())
fsErpsRingPortBlockingOnVcRecovery.setMaxAccess(_C)
if mibBuilder.loadTexts:fsErpsRingPortBlockingOnVcRecovery.setStatus(_A)
class _FsErpsRingNodeType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('rplOwner',1),('nonRplOwner',2)))
_FsErpsRingNodeType_Type.__name__=_E
_FsErpsRingNodeType_Object=MibTableColumn
fsErpsRingNodeType=_FsErpsRingNodeType_Object((1,3,6,1,4,1,10876,101,2,40,2,1,1,8),_FsErpsRingNodeType_Type())
fsErpsRingNodeType.setMaxAccess(_B)
if mibBuilder.loadTexts:fsErpsRingNodeType.setStatus(_A)
class _FsErpsRingOperatingMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('revertive',1),('nonRevertive',2)))
_FsErpsRingOperatingMode_Type.__name__=_E
_FsErpsRingOperatingMode_Object=MibTableColumn
fsErpsRingOperatingMode=_FsErpsRingOperatingMode_Object((1,3,6,1,4,1,10876,101,2,40,2,1,1,9),_FsErpsRingOperatingMode_Type())
fsErpsRingOperatingMode.setMaxAccess(_C)
if mibBuilder.loadTexts:fsErpsRingOperatingMode.setStatus(_A)
class _FsErpsRingMonitorMechanism_Type(RingMonitorMechanismType):defaultValue=1
_FsErpsRingMonitorMechanism_Type.__name__=_V
_FsErpsRingMonitorMechanism_Object=MibTableColumn
fsErpsRingMonitorMechanism=_FsErpsRingMonitorMechanism_Object((1,3,6,1,4,1,10876,101,2,40,2,1,1,10),_FsErpsRingMonitorMechanism_Type())
fsErpsRingMonitorMechanism.setMaxAccess(_C)
if mibBuilder.loadTexts:fsErpsRingMonitorMechanism.setStatus(_A)
class _FsErpsRingPort1Status_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_W,1),(_X,2)))
_FsErpsRingPort1Status_Type.__name__=_E
_FsErpsRingPort1Status_Object=MibTableColumn
fsErpsRingPort1Status=_FsErpsRingPort1Status_Object((1,3,6,1,4,1,10876,101,2,40,2,1,1,11),_FsErpsRingPort1Status_Type())
fsErpsRingPort1Status.setMaxAccess(_B)
if mibBuilder.loadTexts:fsErpsRingPort1Status.setStatus(_A)
class _FsErpsRingPort2Status_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_W,1),(_X,2)))
_FsErpsRingPort2Status_Type.__name__=_E
_FsErpsRingPort2Status_Object=MibTableColumn
fsErpsRingPort2Status=_FsErpsRingPort2Status_Object((1,3,6,1,4,1,10876,101,2,40,2,1,1,12),_FsErpsRingPort2Status_Type())
fsErpsRingPort2Status.setMaxAccess(_B)
if mibBuilder.loadTexts:fsErpsRingPort2Status.setStatus(_A)
class _FsErpsRingSemState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*((_Y,0),('idle',1),('protection',2),('manualswitch',3),('forcedswitch',4),('pending',5)))
_FsErpsRingSemState_Type.__name__=_E
_FsErpsRingSemState_Object=MibTableColumn
fsErpsRingSemState=_FsErpsRingSemState_Object((1,3,6,1,4,1,10876,101,2,40,2,1,1,13),_FsErpsRingSemState_Type())
fsErpsRingSemState.setMaxAccess(_B)
if mibBuilder.loadTexts:fsErpsRingSemState.setStatus(_A)
_FsErpsRingNodeStatus_Type=Integer32
_FsErpsRingNodeStatus_Object=MibTableColumn
fsErpsRingNodeStatus=_FsErpsRingNodeStatus_Object((1,3,6,1,4,1,10876,101,2,40,2,1,1,14),_FsErpsRingNodeStatus_Type())
fsErpsRingNodeStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:fsErpsRingNodeStatus.setStatus(_A)
_FsErpsRingRowStatus_Type=RowStatus
_FsErpsRingRowStatus_Object=MibTableColumn
fsErpsRingRowStatus=_FsErpsRingRowStatus_Object((1,3,6,1,4,1,10876,101,2,40,2,1,1,15),_FsErpsRingRowStatus_Type())
fsErpsRingRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:fsErpsRingRowStatus.setStatus(_A)
class _FsErpsRingMacId_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_FsErpsRingMacId_Type.__name__=_E
_FsErpsRingMacId_Object=MibTableColumn
fsErpsRingMacId=_FsErpsRingMacId_Object((1,3,6,1,4,1,10876,101,2,40,2,1,1,16),_FsErpsRingMacId_Type())
fsErpsRingMacId.setMaxAccess(_C)
if mibBuilder.loadTexts:fsErpsRingMacId.setStatus(_A)
class _FsErpsRingProtectedVlanGroupId_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,64))
_FsErpsRingProtectedVlanGroupId_Type.__name__=_E
_FsErpsRingProtectedVlanGroupId_Object=MibTableColumn
fsErpsRingProtectedVlanGroupId=_FsErpsRingProtectedVlanGroupId_Object((1,3,6,1,4,1,10876,101,2,40,2,1,1,17),_FsErpsRingProtectedVlanGroupId_Type())
fsErpsRingProtectedVlanGroupId.setMaxAccess(_C)
if mibBuilder.loadTexts:fsErpsRingProtectedVlanGroupId.setStatus(_A)
class _FsErpsRingProtectionType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('portBased',1),('serviceBased',2)))
_FsErpsRingProtectionType_Type.__name__=_E
_FsErpsRingProtectionType_Object=MibTableColumn
fsErpsRingProtectionType=_FsErpsRingProtectionType_Object((1,3,6,1,4,1,10876,101,2,40,2,1,1,18),_FsErpsRingProtectionType_Type())
fsErpsRingProtectionType.setMaxAccess(_C)
if mibBuilder.loadTexts:fsErpsRingProtectionType.setStatus(_A)
class _FsErpsRingRAPSCompatibleVersion_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('v1',1),('v2',2)))
_FsErpsRingRAPSCompatibleVersion_Type.__name__=_E
_FsErpsRingRAPSCompatibleVersion_Object=MibTableColumn
fsErpsRingRAPSCompatibleVersion=_FsErpsRingRAPSCompatibleVersion_Object((1,3,6,1,4,1,10876,101,2,40,2,1,1,19),_FsErpsRingRAPSCompatibleVersion_Type())
fsErpsRingRAPSCompatibleVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:fsErpsRingRAPSCompatibleVersion.setStatus(_A)
class _FsErpsRingRplNeighbourPort_Type(InterfaceIndexOrZero):defaultValue=0
_FsErpsRingRplNeighbourPort_Type.__name__=_J
_FsErpsRingRplNeighbourPort_Object=MibTableColumn
fsErpsRingRplNeighbourPort=_FsErpsRingRplNeighbourPort_Object((1,3,6,1,4,1,10876,101,2,40,2,1,1,20),_FsErpsRingRplNeighbourPort_Type())
fsErpsRingRplNeighbourPort.setMaxAccess(_C)
if mibBuilder.loadTexts:fsErpsRingRplNeighbourPort.setStatus(_A)
class _FsErpsRingRAPSSubRingWithoutVC_Type(TruthValue):defaultValue=2
_FsErpsRingRAPSSubRingWithoutVC_Type.__name__=_H
_FsErpsRingRAPSSubRingWithoutVC_Object=MibTableColumn
fsErpsRingRAPSSubRingWithoutVC=_FsErpsRingRAPSSubRingWithoutVC_Object((1,3,6,1,4,1,10876,101,2,40,2,1,1,21),_FsErpsRingRAPSSubRingWithoutVC_Type())
fsErpsRingRAPSSubRingWithoutVC.setMaxAccess(_C)
if mibBuilder.loadTexts:fsErpsRingRAPSSubRingWithoutVC.setStatus(_A)
class _FsErpsRingRplNextNeighbourPort_Type(InterfaceIndexOrZero):defaultValue=0
_FsErpsRingRplNextNeighbourPort_Type.__name__=_J
_FsErpsRingRplNextNeighbourPort_Object=MibTableColumn
fsErpsRingRplNextNeighbourPort=_FsErpsRingRplNextNeighbourPort_Object((1,3,6,1,4,1,10876,101,2,40,2,1,1,22),_FsErpsRingRplNextNeighbourPort_Type())
fsErpsRingRplNextNeighbourPort.setMaxAccess(_C)
if mibBuilder.loadTexts:fsErpsRingRplNextNeighbourPort.setStatus(_A)
_FsErpsRingPort1NodeID_Type=MacAddress
_FsErpsRingPort1NodeID_Object=MibTableColumn
fsErpsRingPort1NodeID=_FsErpsRingPort1NodeID_Object((1,3,6,1,4,1,10876,101,2,40,2,1,1,23),_FsErpsRingPort1NodeID_Type())
fsErpsRingPort1NodeID.setMaxAccess(_B)
if mibBuilder.loadTexts:fsErpsRingPort1NodeID.setStatus(_A)
_FsErpsRingPort2NodeID_Type=MacAddress
_FsErpsRingPort2NodeID_Object=MibTableColumn
fsErpsRingPort2NodeID=_FsErpsRingPort2NodeID_Object((1,3,6,1,4,1,10876,101,2,40,2,1,1,24),_FsErpsRingPort2NodeID_Type())
fsErpsRingPort2NodeID.setMaxAccess(_B)
if mibBuilder.loadTexts:fsErpsRingPort2NodeID.setStatus(_A)
_FsErpsRingPort1BPRBitVal_Type=TruthValue
_FsErpsRingPort1BPRBitVal_Object=MibTableColumn
fsErpsRingPort1BPRBitVal=_FsErpsRingPort1BPRBitVal_Object((1,3,6,1,4,1,10876,101,2,40,2,1,1,25),_FsErpsRingPort1BPRBitVal_Type())
fsErpsRingPort1BPRBitVal.setMaxAccess(_B)
if mibBuilder.loadTexts:fsErpsRingPort1BPRBitVal.setStatus(_A)
_FsErpsRingPort2BPRBitVal_Type=TruthValue
_FsErpsRingPort2BPRBitVal_Object=MibTableColumn
fsErpsRingPort2BPRBitVal=_FsErpsRingPort2BPRBitVal_Object((1,3,6,1,4,1,10876,101,2,40,2,1,1,26),_FsErpsRingPort2BPRBitVal_Type())
fsErpsRingPort2BPRBitVal.setMaxAccess(_B)
if mibBuilder.loadTexts:fsErpsRingPort2BPRBitVal.setStatus(_A)
class _FsErpsRingProtectedVlanGroupList_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_FsErpsRingProtectedVlanGroupList_Type.__name__=_L
_FsErpsRingProtectedVlanGroupList_Object=MibTableColumn
fsErpsRingProtectedVlanGroupList=_FsErpsRingProtectedVlanGroupList_Object((1,3,6,1,4,1,10876,101,2,40,2,1,1,27),_FsErpsRingProtectedVlanGroupList_Type())
fsErpsRingProtectedVlanGroupList.setMaxAccess(_C)
if mibBuilder.loadTexts:fsErpsRingProtectedVlanGroupList.setStatus(_A)
class _FsErpsRingServiceType_Type(RingServiceType):defaultValue=1
_FsErpsRingServiceType_Type.__name__=_Z
_FsErpsRingServiceType_Object=MibTableColumn
fsErpsRingServiceType=_FsErpsRingServiceType_Object((1,3,6,1,4,1,10876,101,2,40,2,1,1,28),_FsErpsRingServiceType_Type())
fsErpsRingServiceType.setMaxAccess(_C)
if mibBuilder.loadTexts:fsErpsRingServiceType.setStatus(_A)
class _FsErpsRingPort1SubPortList_Type(OctetString):defaultValue=OctetString('0')
_FsErpsRingPort1SubPortList_Type.__name__=_L
_FsErpsRingPort1SubPortList_Object=MibTableColumn
fsErpsRingPort1SubPortList=_FsErpsRingPort1SubPortList_Object((1,3,6,1,4,1,10876,101,2,40,2,1,1,29),_FsErpsRingPort1SubPortList_Type())
fsErpsRingPort1SubPortList.setMaxAccess(_C)
if mibBuilder.loadTexts:fsErpsRingPort1SubPortList.setStatus(_A)
class _FsErpsRingPort2SubPortList_Type(OctetString):defaultValue=OctetString('0')
_FsErpsRingPort2SubPortList_Type.__name__=_L
_FsErpsRingPort2SubPortList_Object=MibTableColumn
fsErpsRingPort2SubPortList=_FsErpsRingPort2SubPortList_Object((1,3,6,1,4,1,10876,101,2,40,2,1,1,30),_FsErpsRingPort2SubPortList_Type())
fsErpsRingPort2SubPortList.setMaxAccess(_C)
if mibBuilder.loadTexts:fsErpsRingPort2SubPortList.setStatus(_A)
_FsErpsRingCfmTable_Object=MibTable
fsErpsRingCfmTable=_FsErpsRingCfmTable_Object((1,3,6,1,4,1,10876,101,2,40,2,2))
if mibBuilder.loadTexts:fsErpsRingCfmTable.setStatus(_A)
_FsErpsRingCfmEntry_Object=MibTableRow
fsErpsRingCfmEntry=_FsErpsRingCfmEntry_Object((1,3,6,1,4,1,10876,101,2,40,2,2,1))
fsErpsRingCfmEntry.setIndexNames((0,_D,_F),(0,_D,_I))
if mibBuilder.loadTexts:fsErpsRingCfmEntry.setStatus(_A)
_FsErpsRingMEG1_Type=Unsigned32
_FsErpsRingMEG1_Object=MibTableColumn
fsErpsRingMEG1=_FsErpsRingMEG1_Object((1,3,6,1,4,1,10876,101,2,40,2,2,1,1),_FsErpsRingMEG1_Type())
fsErpsRingMEG1.setMaxAccess(_C)
if mibBuilder.loadTexts:fsErpsRingMEG1.setStatus(_A)
_FsErpsRingCfmME1_Type=Unsigned32
_FsErpsRingCfmME1_Object=MibTableColumn
fsErpsRingCfmME1=_FsErpsRingCfmME1_Object((1,3,6,1,4,1,10876,101,2,40,2,2,1,2),_FsErpsRingCfmME1_Type())
fsErpsRingCfmME1.setMaxAccess(_C)
if mibBuilder.loadTexts:fsErpsRingCfmME1.setStatus(_A)
_FsErpsRingCfmMEP1_Type=Dot1agCfmMepId
_FsErpsRingCfmMEP1_Object=MibTableColumn
fsErpsRingCfmMEP1=_FsErpsRingCfmMEP1_Object((1,3,6,1,4,1,10876,101,2,40,2,2,1,3),_FsErpsRingCfmMEP1_Type())
fsErpsRingCfmMEP1.setMaxAccess(_C)
if mibBuilder.loadTexts:fsErpsRingCfmMEP1.setStatus(_A)
_FsErpsRingMEG2_Type=Unsigned32
_FsErpsRingMEG2_Object=MibTableColumn
fsErpsRingMEG2=_FsErpsRingMEG2_Object((1,3,6,1,4,1,10876,101,2,40,2,2,1,4),_FsErpsRingMEG2_Type())
fsErpsRingMEG2.setMaxAccess(_C)
if mibBuilder.loadTexts:fsErpsRingMEG2.setStatus(_A)
_FsErpsRingCfmME2_Type=Unsigned32
_FsErpsRingCfmME2_Object=MibTableColumn
fsErpsRingCfmME2=_FsErpsRingCfmME2_Object((1,3,6,1,4,1,10876,101,2,40,2,2,1,5),_FsErpsRingCfmME2_Type())
fsErpsRingCfmME2.setMaxAccess(_C)
if mibBuilder.loadTexts:fsErpsRingCfmME2.setStatus(_A)
_FsErpsRingCfmMEP2_Type=Dot1agCfmMepId
_FsErpsRingCfmMEP2_Object=MibTableColumn
fsErpsRingCfmMEP2=_FsErpsRingCfmMEP2_Object((1,3,6,1,4,1,10876,101,2,40,2,2,1,6),_FsErpsRingCfmMEP2_Type())
fsErpsRingCfmMEP2.setMaxAccess(_C)
if mibBuilder.loadTexts:fsErpsRingCfmMEP2.setStatus(_A)
_FsErpsRingCfmRowStatus_Type=RowStatus
_FsErpsRingCfmRowStatus_Object=MibTableColumn
fsErpsRingCfmRowStatus=_FsErpsRingCfmRowStatus_Object((1,3,6,1,4,1,10876,101,2,40,2,2,1,7),_FsErpsRingCfmRowStatus_Type())
fsErpsRingCfmRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:fsErpsRingCfmRowStatus.setStatus(_A)
_FsErpsRingConfigTable_Object=MibTable
fsErpsRingConfigTable=_FsErpsRingConfigTable_Object((1,3,6,1,4,1,10876,101,2,40,2,3))
if mibBuilder.loadTexts:fsErpsRingConfigTable.setStatus(_A)
_FsErpsRingConfigEntry_Object=MibTableRow
fsErpsRingConfigEntry=_FsErpsRingConfigEntry_Object((1,3,6,1,4,1,10876,101,2,40,2,3,1))
fsErpsRingConfigEntry.setIndexNames((0,_D,_F),(0,_D,_I))
if mibBuilder.loadTexts:fsErpsRingConfigEntry.setStatus(_A)
class _FsErpsRingConfigHoldOffTime_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3600000))
_FsErpsRingConfigHoldOffTime_Type.__name__=_G
_FsErpsRingConfigHoldOffTime_Object=MibTableColumn
fsErpsRingConfigHoldOffTime=_FsErpsRingConfigHoldOffTime_Object((1,3,6,1,4,1,10876,101,2,40,2,3,1,1),_FsErpsRingConfigHoldOffTime_Type())
fsErpsRingConfigHoldOffTime.setMaxAccess(_C)
if mibBuilder.loadTexts:fsErpsRingConfigHoldOffTime.setStatus(_A)
if mibBuilder.loadTexts:fsErpsRingConfigHoldOffTime.setUnits(_K)
class _FsErpsRingConfigGuardTime_Type(Unsigned32):defaultValue=500;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3600000))
_FsErpsRingConfigGuardTime_Type.__name__=_G
_FsErpsRingConfigGuardTime_Object=MibTableColumn
fsErpsRingConfigGuardTime=_FsErpsRingConfigGuardTime_Object((1,3,6,1,4,1,10876,101,2,40,2,3,1,2),_FsErpsRingConfigGuardTime_Type())
fsErpsRingConfigGuardTime.setMaxAccess(_C)
if mibBuilder.loadTexts:fsErpsRingConfigGuardTime.setStatus(_A)
if mibBuilder.loadTexts:fsErpsRingConfigGuardTime.setUnits(_K)
class _FsErpsRingConfigWTRTime_Type(Unsigned32):defaultValue=300000;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,86400000))
_FsErpsRingConfigWTRTime_Type.__name__=_G
_FsErpsRingConfigWTRTime_Object=MibTableColumn
fsErpsRingConfigWTRTime=_FsErpsRingConfigWTRTime_Object((1,3,6,1,4,1,10876,101,2,40,2,3,1,3),_FsErpsRingConfigWTRTime_Type())
fsErpsRingConfigWTRTime.setMaxAccess(_C)
if mibBuilder.loadTexts:fsErpsRingConfigWTRTime.setStatus(_A)
if mibBuilder.loadTexts:fsErpsRingConfigWTRTime.setUnits(_K)
class _FsErpsRingConfigPeriodicTime_Type(Unsigned32):defaultValue=5000;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,3600000))
_FsErpsRingConfigPeriodicTime_Type.__name__=_G
_FsErpsRingConfigPeriodicTime_Object=MibTableColumn
fsErpsRingConfigPeriodicTime=_FsErpsRingConfigPeriodicTime_Object((1,3,6,1,4,1,10876,101,2,40,2,3,1,4),_FsErpsRingConfigPeriodicTime_Type())
fsErpsRingConfigPeriodicTime.setMaxAccess(_C)
if mibBuilder.loadTexts:fsErpsRingConfigPeriodicTime.setStatus(_A)
if mibBuilder.loadTexts:fsErpsRingConfigPeriodicTime.setUnits(_K)
class _FsErpsRingConfigSwitchPort_Type(InterfaceIndexOrZero):defaultValue=0
_FsErpsRingConfigSwitchPort_Type.__name__=_J
_FsErpsRingConfigSwitchPort_Object=MibTableColumn
fsErpsRingConfigSwitchPort=_FsErpsRingConfigSwitchPort_Object((1,3,6,1,4,1,10876,101,2,40,2,3,1,5),_FsErpsRingConfigSwitchPort_Type())
fsErpsRingConfigSwitchPort.setMaxAccess(_C)
if mibBuilder.loadTexts:fsErpsRingConfigSwitchPort.setStatus(_A)
class _FsErpsRingConfigSwitchCmd_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_Q,1),('forceSwitch',2),('manualSwitch',3)))
_FsErpsRingConfigSwitchCmd_Type.__name__=_E
_FsErpsRingConfigSwitchCmd_Object=MibTableColumn
fsErpsRingConfigSwitchCmd=_FsErpsRingConfigSwitchCmd_Object((1,3,6,1,4,1,10876,101,2,40,2,3,1,6),_FsErpsRingConfigSwitchCmd_Type())
fsErpsRingConfigSwitchCmd.setMaxAccess(_C)
if mibBuilder.loadTexts:fsErpsRingConfigSwitchCmd.setStatus(_A)
class _FsErpsRingConfigRecoveryMethod_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('auto',1),('manual',2)))
_FsErpsRingConfigRecoveryMethod_Type.__name__=_E
_FsErpsRingConfigRecoveryMethod_Object=MibTableColumn
fsErpsRingConfigRecoveryMethod=_FsErpsRingConfigRecoveryMethod_Object((1,3,6,1,4,1,10876,101,2,40,2,3,1,7),_FsErpsRingConfigRecoveryMethod_Type())
fsErpsRingConfigRecoveryMethod.setMaxAccess(_C)
if mibBuilder.loadTexts:fsErpsRingConfigRecoveryMethod.setStatus(_A)
class _FsErpsRingConfigPropagateTC_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_O,1),(_P,2)))
_FsErpsRingConfigPropagateTC_Type.__name__=_E
_FsErpsRingConfigPropagateTC_Object=MibTableColumn
fsErpsRingConfigPropagateTC=_FsErpsRingConfigPropagateTC_Object((1,3,6,1,4,1,10876,101,2,40,2,3,1,8),_FsErpsRingConfigPropagateTC_Type())
fsErpsRingConfigPropagateTC.setMaxAccess(_C)
if mibBuilder.loadTexts:fsErpsRingConfigPropagateTC.setStatus(_A)
class _FsErpsRingConfigWTBTime_Type(Unsigned32):defaultValue=5500;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,86400000))
_FsErpsRingConfigWTBTime_Type.__name__=_G
_FsErpsRingConfigWTBTime_Object=MibTableColumn
fsErpsRingConfigWTBTime=_FsErpsRingConfigWTBTime_Object((1,3,6,1,4,1,10876,101,2,40,2,3,1,9),_FsErpsRingConfigWTBTime_Type())
fsErpsRingConfigWTBTime.setMaxAccess(_C)
if mibBuilder.loadTexts:fsErpsRingConfigWTBTime.setStatus(_A)
if mibBuilder.loadTexts:fsErpsRingConfigWTBTime.setUnits(_K)
class _FsErpsRingConfigClear_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_Q,1),('clear',2)))
_FsErpsRingConfigClear_Type.__name__=_E
_FsErpsRingConfigClear_Object=MibTableColumn
fsErpsRingConfigClear=_FsErpsRingConfigClear_Object((1,3,6,1,4,1,10876,101,2,40,2,3,1,10),_FsErpsRingConfigClear_Type())
fsErpsRingConfigClear.setMaxAccess(_C)
if mibBuilder.loadTexts:fsErpsRingConfigClear.setStatus(_A)
class _FsErpsRingConfigInterConnNode_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_Q,0),(_a,1),(_b,2)))
_FsErpsRingConfigInterConnNode_Type.__name__=_E
_FsErpsRingConfigInterConnNode_Object=MibTableColumn
fsErpsRingConfigInterConnNode=_FsErpsRingConfigInterConnNode_Object((1,3,6,1,4,1,10876,101,2,40,2,3,1,11),_FsErpsRingConfigInterConnNode_Type())
fsErpsRingConfigInterConnNode.setMaxAccess(_C)
if mibBuilder.loadTexts:fsErpsRingConfigInterConnNode.setStatus(_A)
class _FsErpsRingConfigMultipleFailure_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_Y,0),(_a,1),(_b,2)))
_FsErpsRingConfigMultipleFailure_Type.__name__=_E
_FsErpsRingConfigMultipleFailure_Object=MibTableColumn
fsErpsRingConfigMultipleFailure=_FsErpsRingConfigMultipleFailure_Object((1,3,6,1,4,1,10876,101,2,40,2,3,1,12),_FsErpsRingConfigMultipleFailure_Type())
fsErpsRingConfigMultipleFailure.setMaxAccess(_C)
if mibBuilder.loadTexts:fsErpsRingConfigMultipleFailure.setStatus(_A)
class _FsErpsRingConfigIsPort1Present_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('local',1),(_c,2)))
_FsErpsRingConfigIsPort1Present_Type.__name__=_E
_FsErpsRingConfigIsPort1Present_Object=MibTableColumn
fsErpsRingConfigIsPort1Present=_FsErpsRingConfigIsPort1Present_Object((1,3,6,1,4,1,10876,101,2,40,2,3,1,13),_FsErpsRingConfigIsPort1Present_Type())
fsErpsRingConfigIsPort1Present.setMaxAccess(_C)
if mibBuilder.loadTexts:fsErpsRingConfigIsPort1Present.setStatus(_A)
class _FsErpsRingConfigIsPort2Present_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('local',1),(_c,2)))
_FsErpsRingConfigIsPort2Present_Type.__name__=_E
_FsErpsRingConfigIsPort2Present_Object=MibTableColumn
fsErpsRingConfigIsPort2Present=_FsErpsRingConfigIsPort2Present_Object((1,3,6,1,4,1,10876,101,2,40,2,3,1,14),_FsErpsRingConfigIsPort2Present_Type())
fsErpsRingConfigIsPort2Present.setMaxAccess(_C)
if mibBuilder.loadTexts:fsErpsRingConfigIsPort2Present.setStatus(_A)
class _FsErpsRingConfigInfoDistributingPort_Type(InterfaceIndexOrZero):defaultValue=0
_FsErpsRingConfigInfoDistributingPort_Type.__name__=_J
_FsErpsRingConfigInfoDistributingPort_Object=MibTableColumn
fsErpsRingConfigInfoDistributingPort=_FsErpsRingConfigInfoDistributingPort_Object((1,3,6,1,4,1,10876,101,2,40,2,3,1,15),_FsErpsRingConfigInfoDistributingPort_Type())
fsErpsRingConfigInfoDistributingPort.setMaxAccess(_C)
if mibBuilder.loadTexts:fsErpsRingConfigInfoDistributingPort.setStatus(_A)
class _FsErpsRingConfigKValue_Type(OctetString):defaultValue=OctetString('3.50');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
_FsErpsRingConfigKValue_Type.__name__=_L
_FsErpsRingConfigKValue_Object=MibTableColumn
fsErpsRingConfigKValue=_FsErpsRingConfigKValue_Object((1,3,6,1,4,1,10876,101,2,40,2,3,1,16),_FsErpsRingConfigKValue_Type())
fsErpsRingConfigKValue.setMaxAccess(_C)
if mibBuilder.loadTexts:fsErpsRingConfigKValue.setStatus(_A)
class _FsErpsRingConfigFailureOfProtocol_Type(TruthValue):defaultValue=2
_FsErpsRingConfigFailureOfProtocol_Type.__name__=_H
_FsErpsRingConfigFailureOfProtocol_Object=MibTableColumn
fsErpsRingConfigFailureOfProtocol=_FsErpsRingConfigFailureOfProtocol_Object((1,3,6,1,4,1,10876,101,2,40,2,3,1,17),_FsErpsRingConfigFailureOfProtocol_Type())
fsErpsRingConfigFailureOfProtocol.setMaxAccess(_C)
if mibBuilder.loadTexts:fsErpsRingConfigFailureOfProtocol.setStatus(_A)
_FsErpsRingTcPropTable_Object=MibTable
fsErpsRingTcPropTable=_FsErpsRingTcPropTable_Object((1,3,6,1,4,1,10876,101,2,40,2,4))
if mibBuilder.loadTexts:fsErpsRingTcPropTable.setStatus(_A)
_FsErpsRingTcPropEntry_Object=MibTableRow
fsErpsRingTcPropEntry=_FsErpsRingTcPropEntry_Object((1,3,6,1,4,1,10876,101,2,40,2,4,1))
fsErpsRingTcPropEntry.setIndexNames((0,_D,_F),(0,_D,_I),(0,_D,_d))
if mibBuilder.loadTexts:fsErpsRingTcPropEntry.setStatus(_A)
_FsErpsRingTcPropRingId_Type=RingId
_FsErpsRingTcPropRingId_Object=MibTableColumn
fsErpsRingTcPropRingId=_FsErpsRingTcPropRingId_Object((1,3,6,1,4,1,10876,101,2,40,2,4,1,1),_FsErpsRingTcPropRingId_Type())
fsErpsRingTcPropRingId.setMaxAccess(_N)
if mibBuilder.loadTexts:fsErpsRingTcPropRingId.setStatus(_A)
_FsErpsRingTcPropRowStatus_Type=RowStatus
_FsErpsRingTcPropRowStatus_Object=MibTableColumn
fsErpsRingTcPropRowStatus=_FsErpsRingTcPropRowStatus_Object((1,3,6,1,4,1,10876,101,2,40,2,4,1,2),_FsErpsRingTcPropRowStatus_Type())
fsErpsRingTcPropRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:fsErpsRingTcPropRowStatus.setStatus(_A)
_FsErpsRingConfigExtTable_Object=MibTable
fsErpsRingConfigExtTable=_FsErpsRingConfigExtTable_Object((1,3,6,1,4,1,10876,101,2,40,2,5))
if mibBuilder.loadTexts:fsErpsRingConfigExtTable.setStatus(_A)
_FsErpsRingConfigExtEntry_Object=MibTableRow
fsErpsRingConfigExtEntry=_FsErpsRingConfigExtEntry_Object((1,3,6,1,4,1,10876,101,2,40,2,5,1))
fsErpsRingConfigExtEntry.setIndexNames((0,_D,_F),(0,_D,_I))
if mibBuilder.loadTexts:fsErpsRingConfigExtEntry.setStatus(_A)
class _FsErpsRingConfigExtVCRecoveryPeriodicTime_Type(Unsigned32):defaultValue=5560;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3600000))
_FsErpsRingConfigExtVCRecoveryPeriodicTime_Type.__name__=_G
_FsErpsRingConfigExtVCRecoveryPeriodicTime_Object=MibTableColumn
fsErpsRingConfigExtVCRecoveryPeriodicTime=_FsErpsRingConfigExtVCRecoveryPeriodicTime_Object((1,3,6,1,4,1,10876,101,2,40,2,5,1,1),_FsErpsRingConfigExtVCRecoveryPeriodicTime_Type())
fsErpsRingConfigExtVCRecoveryPeriodicTime.setMaxAccess(_C)
if mibBuilder.loadTexts:fsErpsRingConfigExtVCRecoveryPeriodicTime.setStatus(_A)
if mibBuilder.loadTexts:fsErpsRingConfigExtVCRecoveryPeriodicTime.setUnits(_K)
_FsErpsRingConfigExtMainRingId_Type=RingIdOrNone
_FsErpsRingConfigExtMainRingId_Object=MibTableColumn
fsErpsRingConfigExtMainRingId=_FsErpsRingConfigExtMainRingId_Object((1,3,6,1,4,1,10876,101,2,40,2,5,1,2),_FsErpsRingConfigExtMainRingId_Type())
fsErpsRingConfigExtMainRingId.setMaxAccess(_C)
if mibBuilder.loadTexts:fsErpsRingConfigExtMainRingId.setStatus(_A)
_FsErpsStats_ObjectIdentity=ObjectIdentity
fsErpsStats=_FsErpsStats_ObjectIdentity((1,3,6,1,4,1,10876,101,2,40,3))
_FsErpsMemFailCount_Type=Counter32
_FsErpsMemFailCount_Object=MibScalar
fsErpsMemFailCount=_FsErpsMemFailCount_Object((1,3,6,1,4,1,10876,101,2,40,3,1),_FsErpsMemFailCount_Type())
fsErpsMemFailCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsErpsMemFailCount.setStatus(_A)
_FsErpsBufFailCount_Type=Counter32
_FsErpsBufFailCount_Object=MibScalar
fsErpsBufFailCount=_FsErpsBufFailCount_Object((1,3,6,1,4,1,10876,101,2,40,3,2),_FsErpsBufFailCount_Type())
fsErpsBufFailCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsErpsBufFailCount.setStatus(_A)
_FsErpsTimerFailCount_Type=Counter32
_FsErpsTimerFailCount_Object=MibScalar
fsErpsTimerFailCount=_FsErpsTimerFailCount_Object((1,3,6,1,4,1,10876,101,2,40,3,3),_FsErpsTimerFailCount_Type())
fsErpsTimerFailCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsErpsTimerFailCount.setStatus(_A)
_FsErpsRingStatsTable_Object=MibTable
fsErpsRingStatsTable=_FsErpsRingStatsTable_Object((1,3,6,1,4,1,10876,101,2,40,3,4))
if mibBuilder.loadTexts:fsErpsRingStatsTable.setStatus(_A)
_FsErpsRingStatsEntry_Object=MibTableRow
fsErpsRingStatsEntry=_FsErpsRingStatsEntry_Object((1,3,6,1,4,1,10876,101,2,40,3,4,1))
fsErpsRingStatsEntry.setIndexNames((0,_D,_F),(0,_D,_I))
if mibBuilder.loadTexts:fsErpsRingStatsEntry.setStatus(_A)
class _FsErpsRingClearRingStats_Type(TruthValue):defaultValue=2
_FsErpsRingClearRingStats_Type.__name__=_H
_FsErpsRingClearRingStats_Object=MibTableColumn
fsErpsRingClearRingStats=_FsErpsRingClearRingStats_Object((1,3,6,1,4,1,10876,101,2,40,3,4,1,1),_FsErpsRingClearRingStats_Type())
fsErpsRingClearRingStats.setMaxAccess(_C)
if mibBuilder.loadTexts:fsErpsRingClearRingStats.setStatus(_A)
_FsErpsRingPort1RapsPduSentCount_Type=Counter32
_FsErpsRingPort1RapsPduSentCount_Object=MibTableColumn
fsErpsRingPort1RapsPduSentCount=_FsErpsRingPort1RapsPduSentCount_Object((1,3,6,1,4,1,10876,101,2,40,3,4,1,2),_FsErpsRingPort1RapsPduSentCount_Type())
fsErpsRingPort1RapsPduSentCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsErpsRingPort1RapsPduSentCount.setStatus(_A)
_FsErpsRingPort2RapsPduSentCount_Type=Counter32
_FsErpsRingPort2RapsPduSentCount_Object=MibTableColumn
fsErpsRingPort2RapsPduSentCount=_FsErpsRingPort2RapsPduSentCount_Object((1,3,6,1,4,1,10876,101,2,40,3,4,1,3),_FsErpsRingPort2RapsPduSentCount_Type())
fsErpsRingPort2RapsPduSentCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsErpsRingPort2RapsPduSentCount.setStatus(_A)
_FsErpsRingPort1RapsPduRcvdCount_Type=Counter32
_FsErpsRingPort1RapsPduRcvdCount_Object=MibTableColumn
fsErpsRingPort1RapsPduRcvdCount=_FsErpsRingPort1RapsPduRcvdCount_Object((1,3,6,1,4,1,10876,101,2,40,3,4,1,4),_FsErpsRingPort1RapsPduRcvdCount_Type())
fsErpsRingPort1RapsPduRcvdCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsErpsRingPort1RapsPduRcvdCount.setStatus(_A)
_FsErpsRingPort2RapsPduRcvdCount_Type=Counter32
_FsErpsRingPort2RapsPduRcvdCount_Object=MibTableColumn
fsErpsRingPort2RapsPduRcvdCount=_FsErpsRingPort2RapsPduRcvdCount_Object((1,3,6,1,4,1,10876,101,2,40,3,4,1,5),_FsErpsRingPort2RapsPduRcvdCount_Type())
fsErpsRingPort2RapsPduRcvdCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsErpsRingPort2RapsPduRcvdCount.setStatus(_A)
_FsErpsRingPort1RapsPduDiscardCount_Type=Counter32
_FsErpsRingPort1RapsPduDiscardCount_Object=MibTableColumn
fsErpsRingPort1RapsPduDiscardCount=_FsErpsRingPort1RapsPduDiscardCount_Object((1,3,6,1,4,1,10876,101,2,40,3,4,1,6),_FsErpsRingPort1RapsPduDiscardCount_Type())
fsErpsRingPort1RapsPduDiscardCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsErpsRingPort1RapsPduDiscardCount.setStatus(_A)
_FsErpsRingPort2RapsPduDiscardCount_Type=Counter32
_FsErpsRingPort2RapsPduDiscardCount_Object=MibTableColumn
fsErpsRingPort2RapsPduDiscardCount=_FsErpsRingPort2RapsPduDiscardCount_Object((1,3,6,1,4,1,10876,101,2,40,3,4,1,7),_FsErpsRingPort2RapsPduDiscardCount_Type())
fsErpsRingPort2RapsPduDiscardCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsErpsRingPort2RapsPduDiscardCount.setStatus(_A)
_FsErpsRingPort1BlockedCount_Type=Counter32
_FsErpsRingPort1BlockedCount_Object=MibTableColumn
fsErpsRingPort1BlockedCount=_FsErpsRingPort1BlockedCount_Object((1,3,6,1,4,1,10876,101,2,40,3,4,1,8),_FsErpsRingPort1BlockedCount_Type())
fsErpsRingPort1BlockedCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsErpsRingPort1BlockedCount.setStatus(_A)
_FsErpsRingPort2BlockedCount_Type=Counter32
_FsErpsRingPort2BlockedCount_Object=MibTableColumn
fsErpsRingPort2BlockedCount=_FsErpsRingPort2BlockedCount_Object((1,3,6,1,4,1,10876,101,2,40,3,4,1,9),_FsErpsRingPort2BlockedCount_Type())
fsErpsRingPort2BlockedCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsErpsRingPort2BlockedCount.setStatus(_A)
_FsErpsRingPort1UnblockedCount_Type=Counter32
_FsErpsRingPort1UnblockedCount_Object=MibTableColumn
fsErpsRingPort1UnblockedCount=_FsErpsRingPort1UnblockedCount_Object((1,3,6,1,4,1,10876,101,2,40,3,4,1,10),_FsErpsRingPort1UnblockedCount_Type())
fsErpsRingPort1UnblockedCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsErpsRingPort1UnblockedCount.setStatus(_A)
_FsErpsRingPort2UnblockedCount_Type=Counter32
_FsErpsRingPort2UnblockedCount_Object=MibTableColumn
fsErpsRingPort2UnblockedCount=_FsErpsRingPort2UnblockedCount_Object((1,3,6,1,4,1,10876,101,2,40,3,4,1,11),_FsErpsRingPort2UnblockedCount_Type())
fsErpsRingPort2UnblockedCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsErpsRingPort2UnblockedCount.setStatus(_A)
_FsErpsRingPort1FailedCount_Type=Counter32
_FsErpsRingPort1FailedCount_Object=MibTableColumn
fsErpsRingPort1FailedCount=_FsErpsRingPort1FailedCount_Object((1,3,6,1,4,1,10876,101,2,40,3,4,1,12),_FsErpsRingPort1FailedCount_Type())
fsErpsRingPort1FailedCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsErpsRingPort1FailedCount.setStatus(_A)
_FsErpsRingPort2FailedCount_Type=Counter32
_FsErpsRingPort2FailedCount_Object=MibTableColumn
fsErpsRingPort2FailedCount=_FsErpsRingPort2FailedCount_Object((1,3,6,1,4,1,10876,101,2,40,3,4,1,13),_FsErpsRingPort2FailedCount_Type())
fsErpsRingPort2FailedCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsErpsRingPort2FailedCount.setStatus(_A)
_FsErpsRingPort1RecoveredCount_Type=Counter32
_FsErpsRingPort1RecoveredCount_Object=MibTableColumn
fsErpsRingPort1RecoveredCount=_FsErpsRingPort1RecoveredCount_Object((1,3,6,1,4,1,10876,101,2,40,3,4,1,14),_FsErpsRingPort1RecoveredCount_Type())
fsErpsRingPort1RecoveredCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsErpsRingPort1RecoveredCount.setStatus(_A)
_FsErpsRingPort2RecoveredCount_Type=Counter32
_FsErpsRingPort2RecoveredCount_Object=MibTableColumn
fsErpsRingPort2RecoveredCount=_FsErpsRingPort2RecoveredCount_Object((1,3,6,1,4,1,10876,101,2,40,3,4,1,15),_FsErpsRingPort2RecoveredCount_Type())
fsErpsRingPort2RecoveredCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsErpsRingPort2RecoveredCount.setStatus(_A)
_FsErpsRingPort1VersionDiscardCount_Type=Counter32
_FsErpsRingPort1VersionDiscardCount_Object=MibTableColumn
fsErpsRingPort1VersionDiscardCount=_FsErpsRingPort1VersionDiscardCount_Object((1,3,6,1,4,1,10876,101,2,40,3,4,1,16),_FsErpsRingPort1VersionDiscardCount_Type())
fsErpsRingPort1VersionDiscardCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsErpsRingPort1VersionDiscardCount.setStatus(_A)
_FsErpsRingPort2VersionDiscardCount_Type=Counter32
_FsErpsRingPort2VersionDiscardCount_Object=MibTableColumn
fsErpsRingPort2VersionDiscardCount=_FsErpsRingPort2VersionDiscardCount_Object((1,3,6,1,4,1,10876,101,2,40,3,4,1,17),_FsErpsRingPort2VersionDiscardCount_Type())
fsErpsRingPort2VersionDiscardCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsErpsRingPort2VersionDiscardCount.setStatus(_A)
_FsErpsRingPort1RapsFSPduRxCount_Type=Counter32
_FsErpsRingPort1RapsFSPduRxCount_Object=MibTableColumn
fsErpsRingPort1RapsFSPduRxCount=_FsErpsRingPort1RapsFSPduRxCount_Object((1,3,6,1,4,1,10876,101,2,40,3,4,1,18),_FsErpsRingPort1RapsFSPduRxCount_Type())
fsErpsRingPort1RapsFSPduRxCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsErpsRingPort1RapsFSPduRxCount.setStatus(_A)
_FsErpsRingPort1RapsFSPduTxCount_Type=Counter32
_FsErpsRingPort1RapsFSPduTxCount_Object=MibTableColumn
fsErpsRingPort1RapsFSPduTxCount=_FsErpsRingPort1RapsFSPduTxCount_Object((1,3,6,1,4,1,10876,101,2,40,3,4,1,19),_FsErpsRingPort1RapsFSPduTxCount_Type())
fsErpsRingPort1RapsFSPduTxCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsErpsRingPort1RapsFSPduTxCount.setStatus(_A)
_FsErpsRingPort2RapsFSPduRxCount_Type=Counter32
_FsErpsRingPort2RapsFSPduRxCount_Object=MibTableColumn
fsErpsRingPort2RapsFSPduRxCount=_FsErpsRingPort2RapsFSPduRxCount_Object((1,3,6,1,4,1,10876,101,2,40,3,4,1,20),_FsErpsRingPort2RapsFSPduRxCount_Type())
fsErpsRingPort2RapsFSPduRxCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsErpsRingPort2RapsFSPduRxCount.setStatus(_A)
_FsErpsRingPort2RapsFSPduTxCount_Type=Counter32
_FsErpsRingPort2RapsFSPduTxCount_Object=MibTableColumn
fsErpsRingPort2RapsFSPduTxCount=_FsErpsRingPort2RapsFSPduTxCount_Object((1,3,6,1,4,1,10876,101,2,40,3,4,1,21),_FsErpsRingPort2RapsFSPduTxCount_Type())
fsErpsRingPort2RapsFSPduTxCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsErpsRingPort2RapsFSPduTxCount.setStatus(_A)
_FsErpsRingPort1RapsMSPduRxCount_Type=Counter32
_FsErpsRingPort1RapsMSPduRxCount_Object=MibTableColumn
fsErpsRingPort1RapsMSPduRxCount=_FsErpsRingPort1RapsMSPduRxCount_Object((1,3,6,1,4,1,10876,101,2,40,3,4,1,22),_FsErpsRingPort1RapsMSPduRxCount_Type())
fsErpsRingPort1RapsMSPduRxCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsErpsRingPort1RapsMSPduRxCount.setStatus(_A)
_FsErpsRingPort1RapsMSPduTxCount_Type=Counter32
_FsErpsRingPort1RapsMSPduTxCount_Object=MibTableColumn
fsErpsRingPort1RapsMSPduTxCount=_FsErpsRingPort1RapsMSPduTxCount_Object((1,3,6,1,4,1,10876,101,2,40,3,4,1,23),_FsErpsRingPort1RapsMSPduTxCount_Type())
fsErpsRingPort1RapsMSPduTxCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsErpsRingPort1RapsMSPduTxCount.setStatus(_A)
_FsErpsRingPort2RapsMSPduRxCount_Type=Counter32
_FsErpsRingPort2RapsMSPduRxCount_Object=MibTableColumn
fsErpsRingPort2RapsMSPduRxCount=_FsErpsRingPort2RapsMSPduRxCount_Object((1,3,6,1,4,1,10876,101,2,40,3,4,1,24),_FsErpsRingPort2RapsMSPduRxCount_Type())
fsErpsRingPort2RapsMSPduRxCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsErpsRingPort2RapsMSPduRxCount.setStatus(_A)
_FsErpsRingPort2RapsMSPduTxCount_Type=Counter32
_FsErpsRingPort2RapsMSPduTxCount_Object=MibTableColumn
fsErpsRingPort2RapsMSPduTxCount=_FsErpsRingPort2RapsMSPduTxCount_Object((1,3,6,1,4,1,10876,101,2,40,3,4,1,25),_FsErpsRingPort2RapsMSPduTxCount_Type())
fsErpsRingPort2RapsMSPduTxCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsErpsRingPort2RapsMSPduTxCount.setStatus(_A)
_FsErpsRingPort1RapsEventPduRxCount_Type=Counter32
_FsErpsRingPort1RapsEventPduRxCount_Object=MibTableColumn
fsErpsRingPort1RapsEventPduRxCount=_FsErpsRingPort1RapsEventPduRxCount_Object((1,3,6,1,4,1,10876,101,2,40,3,4,1,26),_FsErpsRingPort1RapsEventPduRxCount_Type())
fsErpsRingPort1RapsEventPduRxCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsErpsRingPort1RapsEventPduRxCount.setStatus(_A)
_FsErpsRingPort1RapsEventPduTxCount_Type=Counter32
_FsErpsRingPort1RapsEventPduTxCount_Object=MibTableColumn
fsErpsRingPort1RapsEventPduTxCount=_FsErpsRingPort1RapsEventPduTxCount_Object((1,3,6,1,4,1,10876,101,2,40,3,4,1,27),_FsErpsRingPort1RapsEventPduTxCount_Type())
fsErpsRingPort1RapsEventPduTxCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsErpsRingPort1RapsEventPduTxCount.setStatus(_A)
_FsErpsRingPort2RapsEventPduRxCount_Type=Counter32
_FsErpsRingPort2RapsEventPduRxCount_Object=MibTableColumn
fsErpsRingPort2RapsEventPduRxCount=_FsErpsRingPort2RapsEventPduRxCount_Object((1,3,6,1,4,1,10876,101,2,40,3,4,1,28),_FsErpsRingPort2RapsEventPduRxCount_Type())
fsErpsRingPort2RapsEventPduRxCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsErpsRingPort2RapsEventPduRxCount.setStatus(_A)
_FsErpsRingPort2RapsEventPduTxCount_Type=Counter32
_FsErpsRingPort2RapsEventPduTxCount_Object=MibTableColumn
fsErpsRingPort2RapsEventPduTxCount=_FsErpsRingPort2RapsEventPduTxCount_Object((1,3,6,1,4,1,10876,101,2,40,3,4,1,29),_FsErpsRingPort2RapsEventPduTxCount_Type())
fsErpsRingPort2RapsEventPduTxCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsErpsRingPort2RapsEventPduTxCount.setStatus(_A)
_FsErpsRingPort1RapsSFPduRxCount_Type=Counter32
_FsErpsRingPort1RapsSFPduRxCount_Object=MibTableColumn
fsErpsRingPort1RapsSFPduRxCount=_FsErpsRingPort1RapsSFPduRxCount_Object((1,3,6,1,4,1,10876,101,2,40,3,4,1,30),_FsErpsRingPort1RapsSFPduRxCount_Type())
fsErpsRingPort1RapsSFPduRxCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsErpsRingPort1RapsSFPduRxCount.setStatus(_A)
_FsErpsRingPort1RapsSFPduTxCount_Type=Counter32
_FsErpsRingPort1RapsSFPduTxCount_Object=MibTableColumn
fsErpsRingPort1RapsSFPduTxCount=_FsErpsRingPort1RapsSFPduTxCount_Object((1,3,6,1,4,1,10876,101,2,40,3,4,1,31),_FsErpsRingPort1RapsSFPduTxCount_Type())
fsErpsRingPort1RapsSFPduTxCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsErpsRingPort1RapsSFPduTxCount.setStatus(_A)
_FsErpsRingPort2RapsSFPduRxCount_Type=Counter32
_FsErpsRingPort2RapsSFPduRxCount_Object=MibTableColumn
fsErpsRingPort2RapsSFPduRxCount=_FsErpsRingPort2RapsSFPduRxCount_Object((1,3,6,1,4,1,10876,101,2,40,3,4,1,32),_FsErpsRingPort2RapsSFPduRxCount_Type())
fsErpsRingPort2RapsSFPduRxCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsErpsRingPort2RapsSFPduRxCount.setStatus(_A)
_FsErpsRingPort2RapsSFPduTxCount_Type=Counter32
_FsErpsRingPort2RapsSFPduTxCount_Object=MibTableColumn
fsErpsRingPort2RapsSFPduTxCount=_FsErpsRingPort2RapsSFPduTxCount_Object((1,3,6,1,4,1,10876,101,2,40,3,4,1,33),_FsErpsRingPort2RapsSFPduTxCount_Type())
fsErpsRingPort2RapsSFPduTxCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsErpsRingPort2RapsSFPduTxCount.setStatus(_A)
_FsErpsRingPort1RapsNRPduRxCount_Type=Counter32
_FsErpsRingPort1RapsNRPduRxCount_Object=MibTableColumn
fsErpsRingPort1RapsNRPduRxCount=_FsErpsRingPort1RapsNRPduRxCount_Object((1,3,6,1,4,1,10876,101,2,40,3,4,1,34),_FsErpsRingPort1RapsNRPduRxCount_Type())
fsErpsRingPort1RapsNRPduRxCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsErpsRingPort1RapsNRPduRxCount.setStatus(_A)
_FsErpsRingPort1RapsNRPduTxCount_Type=Counter32
_FsErpsRingPort1RapsNRPduTxCount_Object=MibTableColumn
fsErpsRingPort1RapsNRPduTxCount=_FsErpsRingPort1RapsNRPduTxCount_Object((1,3,6,1,4,1,10876,101,2,40,3,4,1,35),_FsErpsRingPort1RapsNRPduTxCount_Type())
fsErpsRingPort1RapsNRPduTxCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsErpsRingPort1RapsNRPduTxCount.setStatus(_A)
_FsErpsRingPort2RapsNRPduRxCount_Type=Counter32
_FsErpsRingPort2RapsNRPduRxCount_Object=MibTableColumn
fsErpsRingPort2RapsNRPduRxCount=_FsErpsRingPort2RapsNRPduRxCount_Object((1,3,6,1,4,1,10876,101,2,40,3,4,1,36),_FsErpsRingPort2RapsNRPduRxCount_Type())
fsErpsRingPort2RapsNRPduRxCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsErpsRingPort2RapsNRPduRxCount.setStatus(_A)
_FsErpsRingPort2RapsNRPduTxCount_Type=Counter32
_FsErpsRingPort2RapsNRPduTxCount_Object=MibTableColumn
fsErpsRingPort2RapsNRPduTxCount=_FsErpsRingPort2RapsNRPduTxCount_Object((1,3,6,1,4,1,10876,101,2,40,3,4,1,37),_FsErpsRingPort2RapsNRPduTxCount_Type())
fsErpsRingPort2RapsNRPduTxCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsErpsRingPort2RapsNRPduTxCount.setStatus(_A)
_FsErpsRingPort1RapsNRRBPduRxCount_Type=Counter32
_FsErpsRingPort1RapsNRRBPduRxCount_Object=MibTableColumn
fsErpsRingPort1RapsNRRBPduRxCount=_FsErpsRingPort1RapsNRRBPduRxCount_Object((1,3,6,1,4,1,10876,101,2,40,3,4,1,38),_FsErpsRingPort1RapsNRRBPduRxCount_Type())
fsErpsRingPort1RapsNRRBPduRxCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsErpsRingPort1RapsNRRBPduRxCount.setStatus(_A)
_FsErpsRingPort1RapsNRRBPduTxCount_Type=Counter32
_FsErpsRingPort1RapsNRRBPduTxCount_Object=MibTableColumn
fsErpsRingPort1RapsNRRBPduTxCount=_FsErpsRingPort1RapsNRRBPduTxCount_Object((1,3,6,1,4,1,10876,101,2,40,3,4,1,39),_FsErpsRingPort1RapsNRRBPduTxCount_Type())
fsErpsRingPort1RapsNRRBPduTxCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsErpsRingPort1RapsNRRBPduTxCount.setStatus(_A)
_FsErpsRingPort2RapsNRRBPduRxCount_Type=Counter32
_FsErpsRingPort2RapsNRRBPduRxCount_Object=MibTableColumn
fsErpsRingPort2RapsNRRBPduRxCount=_FsErpsRingPort2RapsNRRBPduRxCount_Object((1,3,6,1,4,1,10876,101,2,40,3,4,1,40),_FsErpsRingPort2RapsNRRBPduRxCount_Type())
fsErpsRingPort2RapsNRRBPduRxCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsErpsRingPort2RapsNRRBPduRxCount.setStatus(_A)
_FsErpsRingPort2RapsNRRBPduTxCount_Type=Counter32
_FsErpsRingPort2RapsNRRBPduTxCount_Object=MibTableColumn
fsErpsRingPort2RapsNRRBPduTxCount=_FsErpsRingPort2RapsNRRBPduTxCount_Object((1,3,6,1,4,1,10876,101,2,40,3,4,1,41),_FsErpsRingPort2RapsNRRBPduTxCount_Type())
fsErpsRingPort2RapsNRRBPduTxCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsErpsRingPort2RapsNRRBPduTxCount.setStatus(_A)
_FsErpsRingGeneratedTrapsCount_Type=Counter32
_FsErpsRingGeneratedTrapsCount_Object=MibTableColumn
fsErpsRingGeneratedTrapsCount=_FsErpsRingGeneratedTrapsCount_Object((1,3,6,1,4,1,10876,101,2,40,3,4,1,42),_FsErpsRingGeneratedTrapsCount_Type())
fsErpsRingGeneratedTrapsCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsErpsRingGeneratedTrapsCount.setStatus(_A)
_FsErpsRingPort1DefectEncTimeSec_Type=Unsigned32
_FsErpsRingPort1DefectEncTimeSec_Object=MibTableColumn
fsErpsRingPort1DefectEncTimeSec=_FsErpsRingPort1DefectEncTimeSec_Object((1,3,6,1,4,1,10876,101,2,40,3,4,1,43),_FsErpsRingPort1DefectEncTimeSec_Type())
fsErpsRingPort1DefectEncTimeSec.setMaxAccess(_B)
if mibBuilder.loadTexts:fsErpsRingPort1DefectEncTimeSec.setStatus(_A)
_FsErpsRingPort2DefectEncTimeSec_Type=Unsigned32
_FsErpsRingPort2DefectEncTimeSec_Object=MibTableColumn
fsErpsRingPort2DefectEncTimeSec=_FsErpsRingPort2DefectEncTimeSec_Object((1,3,6,1,4,1,10876,101,2,40,3,4,1,44),_FsErpsRingPort2DefectEncTimeSec_Type())
fsErpsRingPort2DefectEncTimeSec.setMaxAccess(_B)
if mibBuilder.loadTexts:fsErpsRingPort2DefectEncTimeSec.setStatus(_A)
_FsErpsRingPort1DefectClearedTimeSec_Type=Unsigned32
_FsErpsRingPort1DefectClearedTimeSec_Object=MibTableColumn
fsErpsRingPort1DefectClearedTimeSec=_FsErpsRingPort1DefectClearedTimeSec_Object((1,3,6,1,4,1,10876,101,2,40,3,4,1,45),_FsErpsRingPort1DefectClearedTimeSec_Type())
fsErpsRingPort1DefectClearedTimeSec.setMaxAccess(_B)
if mibBuilder.loadTexts:fsErpsRingPort1DefectClearedTimeSec.setStatus(_A)
_FsErpsRingPort2DefectClearedTimeSec_Type=Unsigned32
_FsErpsRingPort2DefectClearedTimeSec_Object=MibTableColumn
fsErpsRingPort2DefectClearedTimeSec=_FsErpsRingPort2DefectClearedTimeSec_Object((1,3,6,1,4,1,10876,101,2,40,3,4,1,46),_FsErpsRingPort2DefectClearedTimeSec_Type())
fsErpsRingPort2DefectClearedTimeSec.setMaxAccess(_B)
if mibBuilder.loadTexts:fsErpsRingPort2DefectClearedTimeSec.setStatus(_A)
_FsErpsRingRplPortStatChgTimeSec_Type=Unsigned32
_FsErpsRingRplPortStatChgTimeSec_Object=MibTableColumn
fsErpsRingRplPortStatChgTimeSec=_FsErpsRingRplPortStatChgTimeSec_Object((1,3,6,1,4,1,10876,101,2,40,3,4,1,47),_FsErpsRingRplPortStatChgTimeSec_Type())
fsErpsRingRplPortStatChgTimeSec.setMaxAccess(_B)
if mibBuilder.loadTexts:fsErpsRingRplPortStatChgTimeSec.setStatus(_A)
_FsErpsRingRplNbrPortStatChgTime_Type=Unsigned32
_FsErpsRingRplNbrPortStatChgTime_Object=MibTableColumn
fsErpsRingRplNbrPortStatChgTime=_FsErpsRingRplNbrPortStatChgTime_Object((1,3,6,1,4,1,10876,101,2,40,3,4,1,48),_FsErpsRingRplNbrPortStatChgTime_Type())
fsErpsRingRplNbrPortStatChgTime.setMaxAccess(_B)
if mibBuilder.loadTexts:fsErpsRingRplNbrPortStatChgTime.setStatus(_A)
_FsErpsRingDistPortPduRxCount_Type=Counter32
_FsErpsRingDistPortPduRxCount_Object=MibTableColumn
fsErpsRingDistPortPduRxCount=_FsErpsRingDistPortPduRxCount_Object((1,3,6,1,4,1,10876,101,2,40,3,4,1,49),_FsErpsRingDistPortPduRxCount_Type())
fsErpsRingDistPortPduRxCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsErpsRingDistPortPduRxCount.setStatus(_A)
_FsErpsRingDistPortPduTxCount_Type=Counter32
_FsErpsRingDistPortPduTxCount_Object=MibTableColumn
fsErpsRingDistPortPduTxCount=_FsErpsRingDistPortPduTxCount_Object((1,3,6,1,4,1,10876,101,2,40,3,4,1,50),_FsErpsRingDistPortPduTxCount_Type())
fsErpsRingDistPortPduTxCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsErpsRingDistPortPduTxCount.setStatus(_A)
_FsErpsRingRapsPort1DefectEncTimeNSec_Type=Unsigned32
_FsErpsRingRapsPort1DefectEncTimeNSec_Object=MibTableColumn
fsErpsRingRapsPort1DefectEncTimeNSec=_FsErpsRingRapsPort1DefectEncTimeNSec_Object((1,3,6,1,4,1,10876,101,2,40,3,4,1,51),_FsErpsRingRapsPort1DefectEncTimeNSec_Type())
fsErpsRingRapsPort1DefectEncTimeNSec.setMaxAccess(_B)
if mibBuilder.loadTexts:fsErpsRingRapsPort1DefectEncTimeNSec.setStatus(_A)
_FsErpsRingRapsPort1DefectClearedTimeNSec_Type=Unsigned32
_FsErpsRingRapsPort1DefectClearedTimeNSec_Object=MibTableColumn
fsErpsRingRapsPort1DefectClearedTimeNSec=_FsErpsRingRapsPort1DefectClearedTimeNSec_Object((1,3,6,1,4,1,10876,101,2,40,3,4,1,52),_FsErpsRingRapsPort1DefectClearedTimeNSec_Type())
fsErpsRingRapsPort1DefectClearedTimeNSec.setMaxAccess(_B)
if mibBuilder.loadTexts:fsErpsRingRapsPort1DefectClearedTimeNSec.setStatus(_A)
_FsErpsRingRapsPort2DefectEncTimeNSec_Type=Unsigned32
_FsErpsRingRapsPort2DefectEncTimeNSec_Object=MibTableColumn
fsErpsRingRapsPort2DefectEncTimeNSec=_FsErpsRingRapsPort2DefectEncTimeNSec_Object((1,3,6,1,4,1,10876,101,2,40,3,4,1,53),_FsErpsRingRapsPort2DefectEncTimeNSec_Type())
fsErpsRingRapsPort2DefectEncTimeNSec.setMaxAccess(_B)
if mibBuilder.loadTexts:fsErpsRingRapsPort2DefectEncTimeNSec.setStatus(_A)
_FsErpsRingRapsPort2DefectClearedTimeNSec_Type=Unsigned32
_FsErpsRingRapsPort2DefectClearedTimeNSec_Object=MibTableColumn
fsErpsRingRapsPort2DefectClearedTimeNSec=_FsErpsRingRapsPort2DefectClearedTimeNSec_Object((1,3,6,1,4,1,10876,101,2,40,3,4,1,54),_FsErpsRingRapsPort2DefectClearedTimeNSec_Type())
fsErpsRingRapsPort2DefectClearedTimeNSec.setMaxAccess(_B)
if mibBuilder.loadTexts:fsErpsRingRapsPort2DefectClearedTimeNSec.setStatus(_A)
_FsErpsRingRapsRplPortStatChgTimeNSec_Type=Unsigned32
_FsErpsRingRapsRplPortStatChgTimeNSec_Object=MibTableColumn
fsErpsRingRapsRplPortStatChgTimeNSec=_FsErpsRingRapsRplPortStatChgTimeNSec_Object((1,3,6,1,4,1,10876,101,2,40,3,4,1,55),_FsErpsRingRapsRplPortStatChgTimeNSec_Type())
fsErpsRingRapsRplPortStatChgTimeNSec.setMaxAccess(_B)
if mibBuilder.loadTexts:fsErpsRingRapsRplPortStatChgTimeNSec.setStatus(_A)
_FsErpsRingDefectSwitchOverTimeMSec_Type=Unsigned32
_FsErpsRingDefectSwitchOverTimeMSec_Object=MibTableColumn
fsErpsRingDefectSwitchOverTimeMSec=_FsErpsRingDefectSwitchOverTimeMSec_Object((1,3,6,1,4,1,10876,101,2,40,3,4,1,56),_FsErpsRingDefectSwitchOverTimeMSec_Type())
fsErpsRingDefectSwitchOverTimeMSec.setMaxAccess(_B)
if mibBuilder.loadTexts:fsErpsRingDefectSwitchOverTimeMSec.setStatus(_A)
_FsErpsRingDefectClearedSwitchOverTimeMSec_Type=Unsigned32
_FsErpsRingDefectClearedSwitchOverTimeMSec_Object=MibTableColumn
fsErpsRingDefectClearedSwitchOverTimeMSec=_FsErpsRingDefectClearedSwitchOverTimeMSec_Object((1,3,6,1,4,1,10876,101,2,40,3,4,1,57),_FsErpsRingDefectClearedSwitchOverTimeMSec_Type())
fsErpsRingDefectClearedSwitchOverTimeMSec.setMaxAccess(_B)
if mibBuilder.loadTexts:fsErpsRingDefectClearedSwitchOverTimeMSec.setStatus(_A)
_FsErpsNotifications_ObjectIdentity=ObjectIdentity
fsErpsNotifications=_FsErpsNotifications_ObjectIdentity((1,3,6,1,4,1,10876,101,2,40,4))
_FsErpsTraps_ObjectIdentity=ObjectIdentity
fsErpsTraps=_FsErpsTraps_ObjectIdentity((1,3,6,1,4,1,10876,101,2,40,4,0))
class _FsErpsTypeOfFailure_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_FsErpsTypeOfFailure_Type.__name__=_M
_FsErpsTypeOfFailure_Object=MibScalar
fsErpsTypeOfFailure=_FsErpsTypeOfFailure_Object((1,3,6,1,4,1,10876,101,2,40,4,1),_FsErpsTypeOfFailure_Type())
fsErpsTypeOfFailure.setMaxAccess(_e)
if mibBuilder.loadTexts:fsErpsTypeOfFailure.setStatus(_A)
class _FsErpsTrapSwitchingMechanism_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_FsErpsTrapSwitchingMechanism_Type.__name__=_M
_FsErpsTrapSwitchingMechanism_Object=MibScalar
fsErpsTrapSwitchingMechanism=_FsErpsTrapSwitchingMechanism_Object((1,3,6,1,4,1,10876,101,2,40,4,2),_FsErpsTrapSwitchingMechanism_Type())
fsErpsTrapSwitchingMechanism.setMaxAccess(_e)
if mibBuilder.loadTexts:fsErpsTrapSwitchingMechanism.setStatus(_A)
fsErpsStateChangeTrap=NotificationType((1,3,6,1,4,1,10876,101,2,40,4,0,1))
fsErpsStateChangeTrap.setObjects(*((_D,_R),(_D,_S),(_D,_f),(_D,_g),(_D,_h)))
if mibBuilder.loadTexts:fsErpsStateChangeTrap.setStatus(_A)
fsErpsFailureTrap=NotificationType((1,3,6,1,4,1,10876,101,2,40,4,0,2))
fsErpsFailureTrap.setObjects(*((_D,_R),(_D,_S),(_D,_i)))
if mibBuilder.loadTexts:fsErpsFailureTrap.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'RingId':RingId,_V:RingMonitorMechanismType,'RingIdOrNone':RingIdOrNone,_Z:RingServiceType,'fsErpsMIB':fsErpsMIB,'fsErpsContext':fsErpsContext,'fsErpsContextTable':fsErpsContextTable,'fsErpsContextEntry':fsErpsContextEntry,_F:fsErpsContextId,_R:fsErpsCtxtName,'fsErpsCtxtSystemControl':fsErpsCtxtSystemControl,'fsErpsCtxtModuleStatus':fsErpsCtxtModuleStatus,'fsErpsCtxtTraceInput':fsErpsCtxtTraceInput,'fsErpsCtxtTrapStatus':fsErpsCtxtTrapStatus,'fsErpsCtxtClearRingStats':fsErpsCtxtClearRingStats,'fsErpsCtxtRowStatus':fsErpsCtxtRowStatus,'fsErpsCtxtVlanGroupManager':fsErpsCtxtVlanGroupManager,'fsErpsCtxtProprietaryClearFS':fsErpsCtxtProprietaryClearFS,'fsErpsVlanGroupTable':fsErpsVlanGroupTable,'fsErpsVlanGroupEntry':fsErpsVlanGroupEntry,_T:fsErpsVlanId,_U:fsErpsVlanGroupId,'fsErpsVlanGroupRowStatus':fsErpsVlanGroupRowStatus,'fsErpsRing':fsErpsRing,'fsErpsRingTable':fsErpsRingTable,'fsErpsRingEntry':fsErpsRingEntry,_I:fsErpsRingId,'fsErpsRingVlanId':fsErpsRingVlanId,_S:fsErpsRingName,'fsErpsRingPort1':fsErpsRingPort1,'fsErpsRingPort2':fsErpsRingPort2,'fsErpsRingRplPort':fsErpsRingRplPort,'fsErpsRingPortBlockingOnVcRecovery':fsErpsRingPortBlockingOnVcRecovery,'fsErpsRingNodeType':fsErpsRingNodeType,'fsErpsRingOperatingMode':fsErpsRingOperatingMode,'fsErpsRingMonitorMechanism':fsErpsRingMonitorMechanism,'fsErpsRingPort1Status':fsErpsRingPort1Status,'fsErpsRingPort2Status':fsErpsRingPort2Status,_g:fsErpsRingSemState,_h:fsErpsRingNodeStatus,'fsErpsRingRowStatus':fsErpsRingRowStatus,'fsErpsRingMacId':fsErpsRingMacId,'fsErpsRingProtectedVlanGroupId':fsErpsRingProtectedVlanGroupId,'fsErpsRingProtectionType':fsErpsRingProtectionType,'fsErpsRingRAPSCompatibleVersion':fsErpsRingRAPSCompatibleVersion,'fsErpsRingRplNeighbourPort':fsErpsRingRplNeighbourPort,'fsErpsRingRAPSSubRingWithoutVC':fsErpsRingRAPSSubRingWithoutVC,'fsErpsRingRplNextNeighbourPort':fsErpsRingRplNextNeighbourPort,'fsErpsRingPort1NodeID':fsErpsRingPort1NodeID,'fsErpsRingPort2NodeID':fsErpsRingPort2NodeID,'fsErpsRingPort1BPRBitVal':fsErpsRingPort1BPRBitVal,'fsErpsRingPort2BPRBitVal':fsErpsRingPort2BPRBitVal,'fsErpsRingProtectedVlanGroupList':fsErpsRingProtectedVlanGroupList,'fsErpsRingServiceType':fsErpsRingServiceType,'fsErpsRingPort1SubPortList':fsErpsRingPort1SubPortList,'fsErpsRingPort2SubPortList':fsErpsRingPort2SubPortList,'fsErpsRingCfmTable':fsErpsRingCfmTable,'fsErpsRingCfmEntry':fsErpsRingCfmEntry,'fsErpsRingMEG1':fsErpsRingMEG1,'fsErpsRingCfmME1':fsErpsRingCfmME1,'fsErpsRingCfmMEP1':fsErpsRingCfmMEP1,'fsErpsRingMEG2':fsErpsRingMEG2,'fsErpsRingCfmME2':fsErpsRingCfmME2,'fsErpsRingCfmMEP2':fsErpsRingCfmMEP2,'fsErpsRingCfmRowStatus':fsErpsRingCfmRowStatus,'fsErpsRingConfigTable':fsErpsRingConfigTable,'fsErpsRingConfigEntry':fsErpsRingConfigEntry,'fsErpsRingConfigHoldOffTime':fsErpsRingConfigHoldOffTime,'fsErpsRingConfigGuardTime':fsErpsRingConfigGuardTime,'fsErpsRingConfigWTRTime':fsErpsRingConfigWTRTime,'fsErpsRingConfigPeriodicTime':fsErpsRingConfigPeriodicTime,'fsErpsRingConfigSwitchPort':fsErpsRingConfigSwitchPort,'fsErpsRingConfigSwitchCmd':fsErpsRingConfigSwitchCmd,'fsErpsRingConfigRecoveryMethod':fsErpsRingConfigRecoveryMethod,'fsErpsRingConfigPropagateTC':fsErpsRingConfigPropagateTC,'fsErpsRingConfigWTBTime':fsErpsRingConfigWTBTime,'fsErpsRingConfigClear':fsErpsRingConfigClear,'fsErpsRingConfigInterConnNode':fsErpsRingConfigInterConnNode,'fsErpsRingConfigMultipleFailure':fsErpsRingConfigMultipleFailure,'fsErpsRingConfigIsPort1Present':fsErpsRingConfigIsPort1Present,'fsErpsRingConfigIsPort2Present':fsErpsRingConfigIsPort2Present,'fsErpsRingConfigInfoDistributingPort':fsErpsRingConfigInfoDistributingPort,'fsErpsRingConfigKValue':fsErpsRingConfigKValue,'fsErpsRingConfigFailureOfProtocol':fsErpsRingConfigFailureOfProtocol,'fsErpsRingTcPropTable':fsErpsRingTcPropTable,'fsErpsRingTcPropEntry':fsErpsRingTcPropEntry,_d:fsErpsRingTcPropRingId,'fsErpsRingTcPropRowStatus':fsErpsRingTcPropRowStatus,'fsErpsRingConfigExtTable':fsErpsRingConfigExtTable,'fsErpsRingConfigExtEntry':fsErpsRingConfigExtEntry,'fsErpsRingConfigExtVCRecoveryPeriodicTime':fsErpsRingConfigExtVCRecoveryPeriodicTime,'fsErpsRingConfigExtMainRingId':fsErpsRingConfigExtMainRingId,'fsErpsStats':fsErpsStats,'fsErpsMemFailCount':fsErpsMemFailCount,'fsErpsBufFailCount':fsErpsBufFailCount,'fsErpsTimerFailCount':fsErpsTimerFailCount,'fsErpsRingStatsTable':fsErpsRingStatsTable,'fsErpsRingStatsEntry':fsErpsRingStatsEntry,'fsErpsRingClearRingStats':fsErpsRingClearRingStats,'fsErpsRingPort1RapsPduSentCount':fsErpsRingPort1RapsPduSentCount,'fsErpsRingPort2RapsPduSentCount':fsErpsRingPort2RapsPduSentCount,'fsErpsRingPort1RapsPduRcvdCount':fsErpsRingPort1RapsPduRcvdCount,'fsErpsRingPort2RapsPduRcvdCount':fsErpsRingPort2RapsPduRcvdCount,'fsErpsRingPort1RapsPduDiscardCount':fsErpsRingPort1RapsPduDiscardCount,'fsErpsRingPort2RapsPduDiscardCount':fsErpsRingPort2RapsPduDiscardCount,'fsErpsRingPort1BlockedCount':fsErpsRingPort1BlockedCount,'fsErpsRingPort2BlockedCount':fsErpsRingPort2BlockedCount,'fsErpsRingPort1UnblockedCount':fsErpsRingPort1UnblockedCount,'fsErpsRingPort2UnblockedCount':fsErpsRingPort2UnblockedCount,'fsErpsRingPort1FailedCount':fsErpsRingPort1FailedCount,'fsErpsRingPort2FailedCount':fsErpsRingPort2FailedCount,'fsErpsRingPort1RecoveredCount':fsErpsRingPort1RecoveredCount,'fsErpsRingPort2RecoveredCount':fsErpsRingPort2RecoveredCount,'fsErpsRingPort1VersionDiscardCount':fsErpsRingPort1VersionDiscardCount,'fsErpsRingPort2VersionDiscardCount':fsErpsRingPort2VersionDiscardCount,'fsErpsRingPort1RapsFSPduRxCount':fsErpsRingPort1RapsFSPduRxCount,'fsErpsRingPort1RapsFSPduTxCount':fsErpsRingPort1RapsFSPduTxCount,'fsErpsRingPort2RapsFSPduRxCount':fsErpsRingPort2RapsFSPduRxCount,'fsErpsRingPort2RapsFSPduTxCount':fsErpsRingPort2RapsFSPduTxCount,'fsErpsRingPort1RapsMSPduRxCount':fsErpsRingPort1RapsMSPduRxCount,'fsErpsRingPort1RapsMSPduTxCount':fsErpsRingPort1RapsMSPduTxCount,'fsErpsRingPort2RapsMSPduRxCount':fsErpsRingPort2RapsMSPduRxCount,'fsErpsRingPort2RapsMSPduTxCount':fsErpsRingPort2RapsMSPduTxCount,'fsErpsRingPort1RapsEventPduRxCount':fsErpsRingPort1RapsEventPduRxCount,'fsErpsRingPort1RapsEventPduTxCount':fsErpsRingPort1RapsEventPduTxCount,'fsErpsRingPort2RapsEventPduRxCount':fsErpsRingPort2RapsEventPduRxCount,'fsErpsRingPort2RapsEventPduTxCount':fsErpsRingPort2RapsEventPduTxCount,'fsErpsRingPort1RapsSFPduRxCount':fsErpsRingPort1RapsSFPduRxCount,'fsErpsRingPort1RapsSFPduTxCount':fsErpsRingPort1RapsSFPduTxCount,'fsErpsRingPort2RapsSFPduRxCount':fsErpsRingPort2RapsSFPduRxCount,'fsErpsRingPort2RapsSFPduTxCount':fsErpsRingPort2RapsSFPduTxCount,'fsErpsRingPort1RapsNRPduRxCount':fsErpsRingPort1RapsNRPduRxCount,'fsErpsRingPort1RapsNRPduTxCount':fsErpsRingPort1RapsNRPduTxCount,'fsErpsRingPort2RapsNRPduRxCount':fsErpsRingPort2RapsNRPduRxCount,'fsErpsRingPort2RapsNRPduTxCount':fsErpsRingPort2RapsNRPduTxCount,'fsErpsRingPort1RapsNRRBPduRxCount':fsErpsRingPort1RapsNRRBPduRxCount,'fsErpsRingPort1RapsNRRBPduTxCount':fsErpsRingPort1RapsNRRBPduTxCount,'fsErpsRingPort2RapsNRRBPduRxCount':fsErpsRingPort2RapsNRRBPduRxCount,'fsErpsRingPort2RapsNRRBPduTxCount':fsErpsRingPort2RapsNRRBPduTxCount,'fsErpsRingGeneratedTrapsCount':fsErpsRingGeneratedTrapsCount,'fsErpsRingPort1DefectEncTimeSec':fsErpsRingPort1DefectEncTimeSec,'fsErpsRingPort2DefectEncTimeSec':fsErpsRingPort2DefectEncTimeSec,'fsErpsRingPort1DefectClearedTimeSec':fsErpsRingPort1DefectClearedTimeSec,'fsErpsRingPort2DefectClearedTimeSec':fsErpsRingPort2DefectClearedTimeSec,'fsErpsRingRplPortStatChgTimeSec':fsErpsRingRplPortStatChgTimeSec,'fsErpsRingRplNbrPortStatChgTime':fsErpsRingRplNbrPortStatChgTime,'fsErpsRingDistPortPduRxCount':fsErpsRingDistPortPduRxCount,'fsErpsRingDistPortPduTxCount':fsErpsRingDistPortPduTxCount,'fsErpsRingRapsPort1DefectEncTimeNSec':fsErpsRingRapsPort1DefectEncTimeNSec,'fsErpsRingRapsPort1DefectClearedTimeNSec':fsErpsRingRapsPort1DefectClearedTimeNSec,'fsErpsRingRapsPort2DefectEncTimeNSec':fsErpsRingRapsPort2DefectEncTimeNSec,'fsErpsRingRapsPort2DefectClearedTimeNSec':fsErpsRingRapsPort2DefectClearedTimeNSec,'fsErpsRingRapsRplPortStatChgTimeNSec':fsErpsRingRapsRplPortStatChgTimeNSec,'fsErpsRingDefectSwitchOverTimeMSec':fsErpsRingDefectSwitchOverTimeMSec,'fsErpsRingDefectClearedSwitchOverTimeMSec':fsErpsRingDefectClearedSwitchOverTimeMSec,'fsErpsNotifications':fsErpsNotifications,'fsErpsTraps':fsErpsTraps,'fsErpsStateChangeTrap':fsErpsStateChangeTrap,'fsErpsFailureTrap':fsErpsFailureTrap,_i:fsErpsTypeOfFailure,_f:fsErpsTrapSwitchingMechanism})