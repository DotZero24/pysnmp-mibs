_T='ctVlanProtoEtherType'
_S='ctVlanEgressVID'
_R='ctVlanEgressPortSlotNum'
_Q='delete'
_P='create'
_O='ctVlanPortNum'
_N='ctVlanPortSlotNum'
_M='ctVlanTriggerSlotNum'
_L='ctVlanSupportedSlotNum'
_K='deprecated'
_J='static'
_I='DisplayString'
_H='ctVlanVID'
_G='disable'
_F='enable'
_E='CTRON-VLAN-EXTENSIONS-MIB'
_D='read-write'
_C='read-only'
_B='Integer32'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ctVlanExt,=mibBuilder.importSymbols('CTRON-MIB-NAMES','ctVlanExt')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_I,'PhysAddress','TextualConvention')
_CtVlanBridgeConfig_ObjectIdentity=ObjectIdentity
ctVlanBridgeConfig=_CtVlanBridgeConfig_ObjectIdentity((1,3,6,1,4,1,52,4,1,2,16,1))
_CtVlanVersionNumber_Type=Integer32
_CtVlanVersionNumber_Object=MibScalar
ctVlanVersionNumber=_CtVlanVersionNumber_Object((1,3,6,1,4,1,52,4,1,2,16,1,1),_CtVlanVersionNumber_Type())
ctVlanVersionNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:ctVlanVersionNumber.setStatus(_A)
class _CtVlanSupportedOperationalMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),('configurable',2)))
_CtVlanSupportedOperationalMode_Type.__name__=_B
_CtVlanSupportedOperationalMode_Object=MibScalar
ctVlanSupportedOperationalMode=_CtVlanSupportedOperationalMode_Object((1,3,6,1,4,1,52,4,1,2,16,1,2),_CtVlanSupportedOperationalMode_Type())
ctVlanSupportedOperationalMode.setMaxAccess(_C)
if mibBuilder.loadTexts:ctVlanSupportedOperationalMode.setStatus(_K)
class _CtVlanCurrentOperationalMode_Type(Integer32):defaultValue=12;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,12))
_CtVlanCurrentOperationalMode_Type.__name__=_B
_CtVlanCurrentOperationalMode_Object=MibScalar
ctVlanCurrentOperationalMode=_CtVlanCurrentOperationalMode_Object((1,3,6,1,4,1,52,4,1,2,16,1,3),_CtVlanCurrentOperationalMode_Type())
ctVlanCurrentOperationalMode.setMaxAccess(_D)
if mibBuilder.loadTexts:ctVlanCurrentOperationalMode.setStatus(_K)
class _CtVlanResetDefaults_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('current',1),('reset',2)))
_CtVlanResetDefaults_Type.__name__=_B
_CtVlanResetDefaults_Object=MibScalar
ctVlanResetDefaults=_CtVlanResetDefaults_Object((1,3,6,1,4,1,52,4,1,2,16,1,4),_CtVlanResetDefaults_Type())
ctVlanResetDefaults.setMaxAccess(_D)
if mibBuilder.loadTexts:ctVlanResetDefaults.setStatus(_A)
class _CtVlanDefaultVIDStickyEgress_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_CtVlanDefaultVIDStickyEgress_Type.__name__=_B
_CtVlanDefaultVIDStickyEgress_Object=MibScalar
ctVlanDefaultVIDStickyEgress=_CtVlanDefaultVIDStickyEgress_Object((1,3,6,1,4,1,52,4,1,2,16,1,5),_CtVlanDefaultVIDStickyEgress_Type())
ctVlanDefaultVIDStickyEgress.setMaxAccess(_D)
if mibBuilder.loadTexts:ctVlanDefaultVIDStickyEgress.setStatus(_A)
_CtVlanSupportedPortTable_Object=MibTable
ctVlanSupportedPortTable=_CtVlanSupportedPortTable_Object((1,3,6,1,4,1,52,4,1,2,16,1,6))
if mibBuilder.loadTexts:ctVlanSupportedPortTable.setStatus(_A)
_CtVlanSupportedPortEntry_Object=MibTableRow
ctVlanSupportedPortEntry=_CtVlanSupportedPortEntry_Object((1,3,6,1,4,1,52,4,1,2,16,1,6,1))
ctVlanSupportedPortEntry.setIndexNames((0,_E,_L))
if mibBuilder.loadTexts:ctVlanSupportedPortEntry.setStatus(_A)
_CtVlanSupportedSlotNum_Type=Integer32
_CtVlanSupportedSlotNum_Object=MibTableColumn
ctVlanSupportedSlotNum=_CtVlanSupportedSlotNum_Object((1,3,6,1,4,1,52,4,1,2,16,1,6,1,1),_CtVlanSupportedSlotNum_Type())
ctVlanSupportedSlotNum.setMaxAccess(_C)
if mibBuilder.loadTexts:ctVlanSupportedSlotNum.setStatus(_A)
_CtVlanSupportedPortNum_Type=OctetString
_CtVlanSupportedPortNum_Object=MibTableColumn
ctVlanSupportedPortNum=_CtVlanSupportedPortNum_Object((1,3,6,1,4,1,52,4,1,2,16,1,6,1,2),_CtVlanSupportedPortNum_Type())
ctVlanSupportedPortNum.setMaxAccess(_C)
if mibBuilder.loadTexts:ctVlanSupportedPortNum.setStatus(_A)
class _CtVlanLearningMode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('ivl',1),('svl',2),('svlivl',3)))
_CtVlanLearningMode_Type.__name__=_B
_CtVlanLearningMode_Object=MibScalar
ctVlanLearningMode=_CtVlanLearningMode_Object((1,3,6,1,4,1,52,4,1,2,16,1,7),_CtVlanLearningMode_Type())
ctVlanLearningMode.setMaxAccess(_C)
if mibBuilder.loadTexts:ctVlanLearningMode.setStatus(_A)
_CtVlanTriggerPortConfig_ObjectIdentity=ObjectIdentity
ctVlanTriggerPortConfig=_CtVlanTriggerPortConfig_ObjectIdentity((1,3,6,1,4,1,52,4,1,2,16,2))
_CtVlanTriggerPortSetTable_Object=MibTable
ctVlanTriggerPortSetTable=_CtVlanTriggerPortSetTable_Object((1,3,6,1,4,1,52,4,1,2,16,2,1))
if mibBuilder.loadTexts:ctVlanTriggerPortSetTable.setStatus(_A)
_CtVlanTriggerPortEntry_Object=MibTableRow
ctVlanTriggerPortEntry=_CtVlanTriggerPortEntry_Object((1,3,6,1,4,1,52,4,1,2,16,2,1,1))
ctVlanTriggerPortEntry.setIndexNames((0,_E,_M))
if mibBuilder.loadTexts:ctVlanTriggerPortEntry.setStatus(_A)
_CtVlanTriggerSlotNum_Type=Integer32
_CtVlanTriggerSlotNum_Object=MibTableColumn
ctVlanTriggerSlotNum=_CtVlanTriggerSlotNum_Object((1,3,6,1,4,1,52,4,1,2,16,2,1,1,1),_CtVlanTriggerSlotNum_Type())
ctVlanTriggerSlotNum.setMaxAccess(_C)
if mibBuilder.loadTexts:ctVlanTriggerSlotNum.setStatus(_A)
_CtVlanTriggerStatus_Type=OctetString
_CtVlanTriggerStatus_Object=MibTableColumn
ctVlanTriggerStatus=_CtVlanTriggerStatus_Object((1,3,6,1,4,1,52,4,1,2,16,2,1,1,2),_CtVlanTriggerStatus_Type())
ctVlanTriggerStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:ctVlanTriggerStatus.setStatus(_A)
_CtVlanPortConfig_ObjectIdentity=ObjectIdentity
ctVlanPortConfig=_CtVlanPortConfig_ObjectIdentity((1,3,6,1,4,1,52,4,1,2,16,3))
_CtVlanPortConfigTable_Object=MibTable
ctVlanPortConfigTable=_CtVlanPortConfigTable_Object((1,3,6,1,4,1,52,4,1,2,16,3,1))
if mibBuilder.loadTexts:ctVlanPortConfigTable.setStatus(_A)
_CtVlanPortConfigEntry_Object=MibTableRow
ctVlanPortConfigEntry=_CtVlanPortConfigEntry_Object((1,3,6,1,4,1,52,4,1,2,16,3,1,1))
ctVlanPortConfigEntry.setIndexNames((0,_E,_N),(0,_E,_O))
if mibBuilder.loadTexts:ctVlanPortConfigEntry.setStatus(_A)
_CtVlanPortSlotNum_Type=Integer32
_CtVlanPortSlotNum_Object=MibTableColumn
ctVlanPortSlotNum=_CtVlanPortSlotNum_Object((1,3,6,1,4,1,52,4,1,2,16,3,1,1,1),_CtVlanPortSlotNum_Type())
ctVlanPortSlotNum.setMaxAccess(_C)
if mibBuilder.loadTexts:ctVlanPortSlotNum.setStatus(_A)
_CtVlanPortNum_Type=Integer32
_CtVlanPortNum_Object=MibTableColumn
ctVlanPortNum=_CtVlanPortNum_Object((1,3,6,1,4,1,52,4,1,2,16,3,1,1,2),_CtVlanPortNum_Type())
ctVlanPortNum.setMaxAccess(_C)
if mibBuilder.loadTexts:ctVlanPortNum.setStatus(_A)
class _CtVlanPortVID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_CtVlanPortVID_Type.__name__=_B
_CtVlanPortVID_Object=MibTableColumn
ctVlanPortVID=_CtVlanPortVID_Object((1,3,6,1,4,1,52,4,1,2,16,3,1,1,3),_CtVlanPortVID_Type())
ctVlanPortVID.setMaxAccess(_D)
if mibBuilder.loadTexts:ctVlanPortVID.setStatus(_A)
class _CtVlanPortDiscardFrame_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('noDiscard',1),('discardUntagged',2),('discardTagged',3)))
_CtVlanPortDiscardFrame_Type.__name__=_B
_CtVlanPortDiscardFrame_Object=MibTableColumn
ctVlanPortDiscardFrame=_CtVlanPortDiscardFrame_Object((1,3,6,1,4,1,52,4,1,2,16,3,1,1,4),_CtVlanPortDiscardFrame_Type())
ctVlanPortDiscardFrame.setMaxAccess(_D)
if mibBuilder.loadTexts:ctVlanPortDiscardFrame.setStatus(_A)
class _CtVlanPortOperationalMode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('dot1QTrunk',1),('hybrid',2),('dot1dTrunk',3)))
_CtVlanPortOperationalMode_Type.__name__=_B
_CtVlanPortOperationalMode_Object=MibTableColumn
ctVlanPortOperationalMode=_CtVlanPortOperationalMode_Object((1,3,6,1,4,1,52,4,1,2,16,3,1,1,5),_CtVlanPortOperationalMode_Type())
ctVlanPortOperationalMode.setMaxAccess(_D)
if mibBuilder.loadTexts:ctVlanPortOperationalMode.setStatus(_A)
class _CtVlanPortIngressFiltering_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_CtVlanPortIngressFiltering_Type.__name__=_B
_CtVlanPortIngressFiltering_Object=MibTableColumn
ctVlanPortIngressFiltering=_CtVlanPortIngressFiltering_Object((1,3,6,1,4,1,52,4,1,2,16,3,1,1,6),_CtVlanPortIngressFiltering_Type())
ctVlanPortIngressFiltering.setMaxAccess(_D)
if mibBuilder.loadTexts:ctVlanPortIngressFiltering.setStatus(_A)
_CtVlanConfig_ObjectIdentity=ObjectIdentity
ctVlanConfig=_CtVlanConfig_ObjectIdentity((1,3,6,1,4,1,52,4,1,2,16,4))
_CtVlanNumActiveEntries_Type=Integer32
_CtVlanNumActiveEntries_Object=MibScalar
ctVlanNumActiveEntries=_CtVlanNumActiveEntries_Object((1,3,6,1,4,1,52,4,1,2,16,4,1),_CtVlanNumActiveEntries_Type())
ctVlanNumActiveEntries.setMaxAccess(_C)
if mibBuilder.loadTexts:ctVlanNumActiveEntries.setStatus(_A)
_CtVlanNumConfiguredEntries_Type=Integer32
_CtVlanNumConfiguredEntries_Object=MibScalar
ctVlanNumConfiguredEntries=_CtVlanNumConfiguredEntries_Object((1,3,6,1,4,1,52,4,1,2,16,4,2),_CtVlanNumConfiguredEntries_Type())
ctVlanNumConfiguredEntries.setMaxAccess(_C)
if mibBuilder.loadTexts:ctVlanNumConfiguredEntries.setStatus(_A)
_CtVlanMaxNumEntries_Type=Integer32
_CtVlanMaxNumEntries_Object=MibScalar
ctVlanMaxNumEntries=_CtVlanMaxNumEntries_Object((1,3,6,1,4,1,52,4,1,2,16,4,3),_CtVlanMaxNumEntries_Type())
ctVlanMaxNumEntries.setMaxAccess(_C)
if mibBuilder.loadTexts:ctVlanMaxNumEntries.setStatus(_A)
_CtVlanConfigTable_Object=MibTable
ctVlanConfigTable=_CtVlanConfigTable_Object((1,3,6,1,4,1,52,4,1,2,16,4,4))
if mibBuilder.loadTexts:ctVlanConfigTable.setStatus(_A)
_CtVlanConfigEntry_Object=MibTableRow
ctVlanConfigEntry=_CtVlanConfigEntry_Object((1,3,6,1,4,1,52,4,1,2,16,4,4,1))
ctVlanConfigEntry.setIndexNames((0,_E,_H))
if mibBuilder.loadTexts:ctVlanConfigEntry.setStatus(_A)
class _CtVlanVID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_CtVlanVID_Type.__name__=_B
_CtVlanVID_Object=MibTableColumn
ctVlanVID=_CtVlanVID_Object((1,3,6,1,4,1,52,4,1,2,16,4,4,1,1),_CtVlanVID_Type())
ctVlanVID.setMaxAccess(_C)
if mibBuilder.loadTexts:ctVlanVID.setStatus(_A)
class _CtVlanName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_CtVlanName_Type.__name__=_I
_CtVlanName_Object=MibTableColumn
ctVlanName=_CtVlanName_Object((1,3,6,1,4,1,52,4,1,2,16,4,4,1,2),_CtVlanName_Type())
ctVlanName.setMaxAccess(_D)
if mibBuilder.loadTexts:ctVlanName.setStatus(_A)
class _CtVlanStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_CtVlanStatus_Type.__name__=_B
_CtVlanStatus_Object=MibTableColumn
ctVlanStatus=_CtVlanStatus_Object((1,3,6,1,4,1,52,4,1,2,16,4,4,1,3),_CtVlanStatus_Type())
ctVlanStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:ctVlanStatus.setStatus(_A)
class _CtVlanEstablish_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_P,1),(_Q,2)))
_CtVlanEstablish_Type.__name__=_B
_CtVlanEstablish_Object=MibTableColumn
ctVlanEstablish=_CtVlanEstablish_Object((1,3,6,1,4,1,52,4,1,2,16,4,4,1,4),_CtVlanEstablish_Type())
ctVlanEstablish.setMaxAccess(_D)
if mibBuilder.loadTexts:ctVlanEstablish.setStatus(_A)
class _CtVlanIdToFidMapping_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_CtVlanIdToFidMapping_Type.__name__=_B
_CtVlanIdToFidMapping_Object=MibTableColumn
ctVlanIdToFidMapping=_CtVlanIdToFidMapping_Object((1,3,6,1,4,1,52,4,1,2,16,4,4,1,5),_CtVlanIdToFidMapping_Type())
ctVlanIdToFidMapping.setMaxAccess(_D)
if mibBuilder.loadTexts:ctVlanIdToFidMapping.setStatus(_A)
class _CtVlanType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('other',1),(_J,2),('dynamicGvrp',3)))
_CtVlanType_Type.__name__=_B
_CtVlanType_Object=MibTableColumn
ctVlanType=_CtVlanType_Object((1,3,6,1,4,1,52,4,1,2,16,4,4,1,6),_CtVlanType_Type())
ctVlanType.setMaxAccess(_C)
if mibBuilder.loadTexts:ctVlanType.setStatus(_A)
_CtVlanEgressPortsTable_Object=MibTable
ctVlanEgressPortsTable=_CtVlanEgressPortsTable_Object((1,3,6,1,4,1,52,4,1,2,16,4,5))
if mibBuilder.loadTexts:ctVlanEgressPortsTable.setStatus(_A)
_CtVlanEgressPortEntry_Object=MibTableRow
ctVlanEgressPortEntry=_CtVlanEgressPortEntry_Object((1,3,6,1,4,1,52,4,1,2,16,4,5,1))
ctVlanEgressPortEntry.setIndexNames((0,_E,_R),(0,_E,_S))
if mibBuilder.loadTexts:ctVlanEgressPortEntry.setStatus(_A)
_CtVlanEgressPortSlotNum_Type=Integer32
_CtVlanEgressPortSlotNum_Object=MibTableColumn
ctVlanEgressPortSlotNum=_CtVlanEgressPortSlotNum_Object((1,3,6,1,4,1,52,4,1,2,16,4,5,1,1),_CtVlanEgressPortSlotNum_Type())
ctVlanEgressPortSlotNum.setMaxAccess(_C)
if mibBuilder.loadTexts:ctVlanEgressPortSlotNum.setStatus(_A)
class _CtVlanEgressVID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_CtVlanEgressVID_Type.__name__=_B
_CtVlanEgressVID_Object=MibTableColumn
ctVlanEgressVID=_CtVlanEgressVID_Object((1,3,6,1,4,1,52,4,1,2,16,4,5,1,2),_CtVlanEgressVID_Type())
ctVlanEgressVID.setMaxAccess(_C)
if mibBuilder.loadTexts:ctVlanEgressVID.setStatus(_A)
_CtVlanEgressList_Type=OctetString
_CtVlanEgressList_Object=MibTableColumn
ctVlanEgressList=_CtVlanEgressList_Object((1,3,6,1,4,1,52,4,1,2,16,4,5,1,3),_CtVlanEgressList_Type())
ctVlanEgressList.setMaxAccess(_D)
if mibBuilder.loadTexts:ctVlanEgressList.setStatus(_A)
_CtVlanEgressUntaggedList_Type=OctetString
_CtVlanEgressUntaggedList_Object=MibTableColumn
ctVlanEgressUntaggedList=_CtVlanEgressUntaggedList_Object((1,3,6,1,4,1,52,4,1,2,16,4,5,1,4),_CtVlanEgressUntaggedList_Type())
ctVlanEgressUntaggedList.setMaxAccess(_D)
if mibBuilder.loadTexts:ctVlanEgressUntaggedList.setStatus(_A)
_CtVlanProtocolAssign_ObjectIdentity=ObjectIdentity
ctVlanProtocolAssign=_CtVlanProtocolAssign_ObjectIdentity((1,3,6,1,4,1,52,4,1,2,16,5))
class _CtVlanProtocolStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_CtVlanProtocolStatus_Type.__name__=_B
_CtVlanProtocolStatus_Object=MibScalar
ctVlanProtocolStatus=_CtVlanProtocolStatus_Object((1,3,6,1,4,1,52,4,1,2,16,5,1),_CtVlanProtocolStatus_Type())
ctVlanProtocolStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:ctVlanProtocolStatus.setStatus(_A)
_CtMaxNumVlanProtoEntries_Type=Integer32
_CtMaxNumVlanProtoEntries_Object=MibScalar
ctMaxNumVlanProtoEntries=_CtMaxNumVlanProtoEntries_Object((1,3,6,1,4,1,52,4,1,2,16,5,2),_CtMaxNumVlanProtoEntries_Type())
ctMaxNumVlanProtoEntries.setMaxAccess(_C)
if mibBuilder.loadTexts:ctMaxNumVlanProtoEntries.setStatus(_A)
_CtVlanProtoAssignTable_Object=MibTable
ctVlanProtoAssignTable=_CtVlanProtoAssignTable_Object((1,3,6,1,4,1,52,4,1,2,16,5,3))
if mibBuilder.loadTexts:ctVlanProtoAssignTable.setStatus(_A)
_CtVlanProtoAssignEntry_Object=MibTableRow
ctVlanProtoAssignEntry=_CtVlanProtoAssignEntry_Object((1,3,6,1,4,1,52,4,1,2,16,5,3,1))
ctVlanProtoAssignEntry.setIndexNames((0,_E,_H),(0,_E,_T))
if mibBuilder.loadTexts:ctVlanProtoAssignEntry.setStatus(_A)
_CtVlanProtoEtherType_Type=Integer32
_CtVlanProtoEtherType_Object=MibTableColumn
ctVlanProtoEtherType=_CtVlanProtoEtherType_Object((1,3,6,1,4,1,52,4,1,2,16,5,3,1,1),_CtVlanProtoEtherType_Type())
ctVlanProtoEtherType.setMaxAccess(_C)
if mibBuilder.loadTexts:ctVlanProtoEtherType.setStatus(_A)
class _CtVlanProtoEstablish_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_P,1),(_Q,2)))
_CtVlanProtoEstablish_Type.__name__=_B
_CtVlanProtoEstablish_Object=MibTableColumn
ctVlanProtoEstablish=_CtVlanProtoEstablish_Object((1,3,6,1,4,1,52,4,1,2,16,5,3,1,2),_CtVlanProtoEstablish_Type())
ctVlanProtoEstablish.setMaxAccess(_D)
if mibBuilder.loadTexts:ctVlanProtoEstablish.setStatus(_A)
_CtVlanProtoPortList_Type=OctetString
_CtVlanProtoPortList_Object=MibTableColumn
ctVlanProtoPortList=_CtVlanProtoPortList_Object((1,3,6,1,4,1,52,4,1,2,16,5,3,1,3),_CtVlanProtoPortList_Type())
ctVlanProtoPortList.setMaxAccess(_D)
if mibBuilder.loadTexts:ctVlanProtoPortList.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'ctVlanBridgeConfig':ctVlanBridgeConfig,'ctVlanVersionNumber':ctVlanVersionNumber,'ctVlanSupportedOperationalMode':ctVlanSupportedOperationalMode,'ctVlanCurrentOperationalMode':ctVlanCurrentOperationalMode,'ctVlanResetDefaults':ctVlanResetDefaults,'ctVlanDefaultVIDStickyEgress':ctVlanDefaultVIDStickyEgress,'ctVlanSupportedPortTable':ctVlanSupportedPortTable,'ctVlanSupportedPortEntry':ctVlanSupportedPortEntry,_L:ctVlanSupportedSlotNum,'ctVlanSupportedPortNum':ctVlanSupportedPortNum,'ctVlanLearningMode':ctVlanLearningMode,'ctVlanTriggerPortConfig':ctVlanTriggerPortConfig,'ctVlanTriggerPortSetTable':ctVlanTriggerPortSetTable,'ctVlanTriggerPortEntry':ctVlanTriggerPortEntry,_M:ctVlanTriggerSlotNum,'ctVlanTriggerStatus':ctVlanTriggerStatus,'ctVlanPortConfig':ctVlanPortConfig,'ctVlanPortConfigTable':ctVlanPortConfigTable,'ctVlanPortConfigEntry':ctVlanPortConfigEntry,_N:ctVlanPortSlotNum,_O:ctVlanPortNum,'ctVlanPortVID':ctVlanPortVID,'ctVlanPortDiscardFrame':ctVlanPortDiscardFrame,'ctVlanPortOperationalMode':ctVlanPortOperationalMode,'ctVlanPortIngressFiltering':ctVlanPortIngressFiltering,'ctVlanConfig':ctVlanConfig,'ctVlanNumActiveEntries':ctVlanNumActiveEntries,'ctVlanNumConfiguredEntries':ctVlanNumConfiguredEntries,'ctVlanMaxNumEntries':ctVlanMaxNumEntries,'ctVlanConfigTable':ctVlanConfigTable,'ctVlanConfigEntry':ctVlanConfigEntry,_H:ctVlanVID,'ctVlanName':ctVlanName,'ctVlanStatus':ctVlanStatus,'ctVlanEstablish':ctVlanEstablish,'ctVlanIdToFidMapping':ctVlanIdToFidMapping,'ctVlanType':ctVlanType,'ctVlanEgressPortsTable':ctVlanEgressPortsTable,'ctVlanEgressPortEntry':ctVlanEgressPortEntry,_R:ctVlanEgressPortSlotNum,_S:ctVlanEgressVID,'ctVlanEgressList':ctVlanEgressList,'ctVlanEgressUntaggedList':ctVlanEgressUntaggedList,'ctVlanProtocolAssign':ctVlanProtocolAssign,'ctVlanProtocolStatus':ctVlanProtocolStatus,'ctMaxNumVlanProtoEntries':ctMaxNumVlanProtoEntries,'ctVlanProtoAssignTable':ctVlanProtoAssignTable,'ctVlanProtoAssignEntry':ctVlanProtoAssignEntry,_T:ctVlanProtoEtherType,'ctVlanProtoEstablish':ctVlanProtoEstablish,'ctVlanProtoPortList':ctVlanProtoPortList})