_A1='pBridgePortGmrpGroup2'
_A0='pBridgePortGmrpGroup'
_z='dot1dPortRestrictedGroupRegistration'
_y='dot1dTpPortInOverflowDiscards'
_x='dot1dTpPortOutOverflowFrames'
_w='dot1dTpPortInOverflowFrames'
_v='dot1dTpHCPortInDiscards'
_u='dot1dTpHCPortOutFrames'
_t='dot1dTpHCPortInFrames'
_s='deprecated'
_r='dot1dPortGarpLeaveAllTime'
_q='dot1dPortGarpLeaveTime'
_p='dot1dPortGarpJoinTime'
_o='dot1dPortOutboundAccessPriority'
_n='dot1dTrafficClass'
_m='dot1dPortNumTrafficClasses'
_l='dot1dPortDefaultUserPriority'
_k='dot1dTrafficClassesEnabled'
_j='dot1dGmrpStatus'
_i='dot1dPortCapabilities'
_h='dot1dDeviceCapabilities'
_g='dot1dPortGmrpEntry'
_f='dot1dPortGarpEntry'
_e='dot1dPortPriorityEntry'
_d='dot1dPortCapabilitiesEntry'
_c='dot1dTrafficClassPriority'
_b='not-accessible'
_a='dot1dUserPriority'
_Z='pBridgePortOverflowGroup'
_Y='pBridgeHCPortGroup'
_X='pBridgePortGarpGroup'
_W='pBridgeAccessPriorityGroup'
_V='pBridgePriorityGroup'
_U='pBridgeRegenPriorityGroup'
_T='pBridgeDefaultPriorityGroup'
_S='pBridgeDevicePriorityGroup'
_R='pBridgeDeviceGmrpGroup'
_Q='pBridgeExtCapGroup'
_P='dot1dPortGmrpLastPduOrigin'
_O='dot1dPortGmrpFailedRegistrations'
_N='dot1dPortGmrpStatus'
_M='dot1dRegenUserPriority'
_L='EnabledStatus'
_K='TruthValue'
_J='Bits'
_I='dot1dTpPort'
_H='TimeInterval'
_G='dot1dBasePort'
_F='BRIDGE-MIB'
_E='Integer32'
_D='read-write'
_C='read-only'
_B='P-BRIDGE-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dot1dBasePort,dot1dBasePortEntry,dot1dBridge,dot1dTp,dot1dTpPort=mibBuilder.importSymbols(_F,_G,'dot1dBasePortEntry','dot1dBridge','dot1dTp',_I)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI',_J,'Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,TextualConvention,TimeInterval,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','TextualConvention',_H,_K)
pBridgeMIB=ModuleIdentity((1,3,6,1,2,1,17,6))
if mibBuilder.loadTexts:pBridgeMIB.setRevisions(('2006-01-09 00:00','1999-08-25 00:00'))
class EnabledStatus(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),('disabled',2)))
_Dot1dTpHCPortTable_Object=MibTable
dot1dTpHCPortTable=_Dot1dTpHCPortTable_Object((1,3,6,1,2,1,17,4,5))
if mibBuilder.loadTexts:dot1dTpHCPortTable.setStatus(_A)
_Dot1dTpHCPortEntry_Object=MibTableRow
dot1dTpHCPortEntry=_Dot1dTpHCPortEntry_Object((1,3,6,1,2,1,17,4,5,1))
dot1dTpHCPortEntry.setIndexNames((0,_F,_I))
if mibBuilder.loadTexts:dot1dTpHCPortEntry.setStatus(_A)
_Dot1dTpHCPortInFrames_Type=Counter64
_Dot1dTpHCPortInFrames_Object=MibTableColumn
dot1dTpHCPortInFrames=_Dot1dTpHCPortInFrames_Object((1,3,6,1,2,1,17,4,5,1,1),_Dot1dTpHCPortInFrames_Type())
dot1dTpHCPortInFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:dot1dTpHCPortInFrames.setStatus(_A)
_Dot1dTpHCPortOutFrames_Type=Counter64
_Dot1dTpHCPortOutFrames_Object=MibTableColumn
dot1dTpHCPortOutFrames=_Dot1dTpHCPortOutFrames_Object((1,3,6,1,2,1,17,4,5,1,2),_Dot1dTpHCPortOutFrames_Type())
dot1dTpHCPortOutFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:dot1dTpHCPortOutFrames.setStatus(_A)
_Dot1dTpHCPortInDiscards_Type=Counter64
_Dot1dTpHCPortInDiscards_Object=MibTableColumn
dot1dTpHCPortInDiscards=_Dot1dTpHCPortInDiscards_Object((1,3,6,1,2,1,17,4,5,1,3),_Dot1dTpHCPortInDiscards_Type())
dot1dTpHCPortInDiscards.setMaxAccess(_C)
if mibBuilder.loadTexts:dot1dTpHCPortInDiscards.setStatus(_A)
_Dot1dTpPortOverflowTable_Object=MibTable
dot1dTpPortOverflowTable=_Dot1dTpPortOverflowTable_Object((1,3,6,1,2,1,17,4,6))
if mibBuilder.loadTexts:dot1dTpPortOverflowTable.setStatus(_A)
_Dot1dTpPortOverflowEntry_Object=MibTableRow
dot1dTpPortOverflowEntry=_Dot1dTpPortOverflowEntry_Object((1,3,6,1,2,1,17,4,6,1))
dot1dTpPortOverflowEntry.setIndexNames((0,_F,_I))
if mibBuilder.loadTexts:dot1dTpPortOverflowEntry.setStatus(_A)
_Dot1dTpPortInOverflowFrames_Type=Counter32
_Dot1dTpPortInOverflowFrames_Object=MibTableColumn
dot1dTpPortInOverflowFrames=_Dot1dTpPortInOverflowFrames_Object((1,3,6,1,2,1,17,4,6,1,1),_Dot1dTpPortInOverflowFrames_Type())
dot1dTpPortInOverflowFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:dot1dTpPortInOverflowFrames.setStatus(_A)
_Dot1dTpPortOutOverflowFrames_Type=Counter32
_Dot1dTpPortOutOverflowFrames_Object=MibTableColumn
dot1dTpPortOutOverflowFrames=_Dot1dTpPortOutOverflowFrames_Object((1,3,6,1,2,1,17,4,6,1,2),_Dot1dTpPortOutOverflowFrames_Type())
dot1dTpPortOutOverflowFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:dot1dTpPortOutOverflowFrames.setStatus(_A)
_Dot1dTpPortInOverflowDiscards_Type=Counter32
_Dot1dTpPortInOverflowDiscards_Object=MibTableColumn
dot1dTpPortInOverflowDiscards=_Dot1dTpPortInOverflowDiscards_Object((1,3,6,1,2,1,17,4,6,1,3),_Dot1dTpPortInOverflowDiscards_Type())
dot1dTpPortInOverflowDiscards.setMaxAccess(_C)
if mibBuilder.loadTexts:dot1dTpPortInOverflowDiscards.setStatus(_A)
_PBridgeMIBObjects_ObjectIdentity=ObjectIdentity
pBridgeMIBObjects=_PBridgeMIBObjects_ObjectIdentity((1,3,6,1,2,1,17,6,1))
_Dot1dExtBase_ObjectIdentity=ObjectIdentity
dot1dExtBase=_Dot1dExtBase_ObjectIdentity((1,3,6,1,2,1,17,6,1,1))
class _Dot1dDeviceCapabilities_Type(Bits):namedValues=NamedValues(*(('dot1dExtendedFilteringServices',0),('dot1dTrafficClasses',1),('dot1qStaticEntryIndividualPort',2),('dot1qIVLCapable',3),('dot1qSVLCapable',4),('dot1qHybridCapable',5),('dot1qConfigurablePvidTagging',6),('dot1dLocalVlanCapable',7)))
_Dot1dDeviceCapabilities_Type.__name__=_J
_Dot1dDeviceCapabilities_Object=MibScalar
dot1dDeviceCapabilities=_Dot1dDeviceCapabilities_Object((1,3,6,1,2,1,17,6,1,1,1),_Dot1dDeviceCapabilities_Type())
dot1dDeviceCapabilities.setMaxAccess(_C)
if mibBuilder.loadTexts:dot1dDeviceCapabilities.setStatus(_A)
class _Dot1dTrafficClassesEnabled_Type(TruthValue):defaultValue=1
_Dot1dTrafficClassesEnabled_Type.__name__=_K
_Dot1dTrafficClassesEnabled_Object=MibScalar
dot1dTrafficClassesEnabled=_Dot1dTrafficClassesEnabled_Object((1,3,6,1,2,1,17,6,1,1,2),_Dot1dTrafficClassesEnabled_Type())
dot1dTrafficClassesEnabled.setMaxAccess(_D)
if mibBuilder.loadTexts:dot1dTrafficClassesEnabled.setStatus(_A)
class _Dot1dGmrpStatus_Type(EnabledStatus):defaultValue=1
_Dot1dGmrpStatus_Type.__name__=_L
_Dot1dGmrpStatus_Object=MibScalar
dot1dGmrpStatus=_Dot1dGmrpStatus_Object((1,3,6,1,2,1,17,6,1,1,3),_Dot1dGmrpStatus_Type())
dot1dGmrpStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:dot1dGmrpStatus.setStatus(_A)
_Dot1dPortCapabilitiesTable_Object=MibTable
dot1dPortCapabilitiesTable=_Dot1dPortCapabilitiesTable_Object((1,3,6,1,2,1,17,6,1,1,4))
if mibBuilder.loadTexts:dot1dPortCapabilitiesTable.setStatus(_A)
_Dot1dPortCapabilitiesEntry_Object=MibTableRow
dot1dPortCapabilitiesEntry=_Dot1dPortCapabilitiesEntry_Object((1,3,6,1,2,1,17,6,1,1,4,1))
if mibBuilder.loadTexts:dot1dPortCapabilitiesEntry.setStatus(_A)
class _Dot1dPortCapabilities_Type(Bits):namedValues=NamedValues(*(('dot1qDot1qTagging',0),('dot1qConfigurableAcceptableFrameTypes',1),('dot1qIngressFiltering',2)))
_Dot1dPortCapabilities_Type.__name__=_J
_Dot1dPortCapabilities_Object=MibTableColumn
dot1dPortCapabilities=_Dot1dPortCapabilities_Object((1,3,6,1,2,1,17,6,1,1,4,1,1),_Dot1dPortCapabilities_Type())
dot1dPortCapabilities.setMaxAccess(_C)
if mibBuilder.loadTexts:dot1dPortCapabilities.setStatus(_A)
_Dot1dPriority_ObjectIdentity=ObjectIdentity
dot1dPriority=_Dot1dPriority_ObjectIdentity((1,3,6,1,2,1,17,6,1,2))
_Dot1dPortPriorityTable_Object=MibTable
dot1dPortPriorityTable=_Dot1dPortPriorityTable_Object((1,3,6,1,2,1,17,6,1,2,1))
if mibBuilder.loadTexts:dot1dPortPriorityTable.setStatus(_A)
_Dot1dPortPriorityEntry_Object=MibTableRow
dot1dPortPriorityEntry=_Dot1dPortPriorityEntry_Object((1,3,6,1,2,1,17,6,1,2,1,1))
if mibBuilder.loadTexts:dot1dPortPriorityEntry.setStatus(_A)
class _Dot1dPortDefaultUserPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_Dot1dPortDefaultUserPriority_Type.__name__=_E
_Dot1dPortDefaultUserPriority_Object=MibTableColumn
dot1dPortDefaultUserPriority=_Dot1dPortDefaultUserPriority_Object((1,3,6,1,2,1,17,6,1,2,1,1,1),_Dot1dPortDefaultUserPriority_Type())
dot1dPortDefaultUserPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:dot1dPortDefaultUserPriority.setStatus(_A)
class _Dot1dPortNumTrafficClasses_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_Dot1dPortNumTrafficClasses_Type.__name__=_E
_Dot1dPortNumTrafficClasses_Object=MibTableColumn
dot1dPortNumTrafficClasses=_Dot1dPortNumTrafficClasses_Object((1,3,6,1,2,1,17,6,1,2,1,1,2),_Dot1dPortNumTrafficClasses_Type())
dot1dPortNumTrafficClasses.setMaxAccess(_D)
if mibBuilder.loadTexts:dot1dPortNumTrafficClasses.setStatus(_A)
_Dot1dUserPriorityRegenTable_Object=MibTable
dot1dUserPriorityRegenTable=_Dot1dUserPriorityRegenTable_Object((1,3,6,1,2,1,17,6,1,2,2))
if mibBuilder.loadTexts:dot1dUserPriorityRegenTable.setStatus(_A)
_Dot1dUserPriorityRegenEntry_Object=MibTableRow
dot1dUserPriorityRegenEntry=_Dot1dUserPriorityRegenEntry_Object((1,3,6,1,2,1,17,6,1,2,2,1))
dot1dUserPriorityRegenEntry.setIndexNames((0,_F,_G),(0,_B,_a))
if mibBuilder.loadTexts:dot1dUserPriorityRegenEntry.setStatus(_A)
class _Dot1dUserPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_Dot1dUserPriority_Type.__name__=_E
_Dot1dUserPriority_Object=MibTableColumn
dot1dUserPriority=_Dot1dUserPriority_Object((1,3,6,1,2,1,17,6,1,2,2,1,1),_Dot1dUserPriority_Type())
dot1dUserPriority.setMaxAccess(_b)
if mibBuilder.loadTexts:dot1dUserPriority.setStatus(_A)
class _Dot1dRegenUserPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_Dot1dRegenUserPriority_Type.__name__=_E
_Dot1dRegenUserPriority_Object=MibTableColumn
dot1dRegenUserPriority=_Dot1dRegenUserPriority_Object((1,3,6,1,2,1,17,6,1,2,2,1,2),_Dot1dRegenUserPriority_Type())
dot1dRegenUserPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:dot1dRegenUserPriority.setStatus(_A)
_Dot1dTrafficClassTable_Object=MibTable
dot1dTrafficClassTable=_Dot1dTrafficClassTable_Object((1,3,6,1,2,1,17,6,1,2,3))
if mibBuilder.loadTexts:dot1dTrafficClassTable.setStatus(_A)
_Dot1dTrafficClassEntry_Object=MibTableRow
dot1dTrafficClassEntry=_Dot1dTrafficClassEntry_Object((1,3,6,1,2,1,17,6,1,2,3,1))
dot1dTrafficClassEntry.setIndexNames((0,_F,_G),(0,_B,_c))
if mibBuilder.loadTexts:dot1dTrafficClassEntry.setStatus(_A)
class _Dot1dTrafficClassPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_Dot1dTrafficClassPriority_Type.__name__=_E
_Dot1dTrafficClassPriority_Object=MibTableColumn
dot1dTrafficClassPriority=_Dot1dTrafficClassPriority_Object((1,3,6,1,2,1,17,6,1,2,3,1,1),_Dot1dTrafficClassPriority_Type())
dot1dTrafficClassPriority.setMaxAccess(_b)
if mibBuilder.loadTexts:dot1dTrafficClassPriority.setStatus(_A)
class _Dot1dTrafficClass_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_Dot1dTrafficClass_Type.__name__=_E
_Dot1dTrafficClass_Object=MibTableColumn
dot1dTrafficClass=_Dot1dTrafficClass_Object((1,3,6,1,2,1,17,6,1,2,3,1,2),_Dot1dTrafficClass_Type())
dot1dTrafficClass.setMaxAccess(_D)
if mibBuilder.loadTexts:dot1dTrafficClass.setStatus(_A)
_Dot1dPortOutboundAccessPriorityTable_Object=MibTable
dot1dPortOutboundAccessPriorityTable=_Dot1dPortOutboundAccessPriorityTable_Object((1,3,6,1,2,1,17,6,1,2,4))
if mibBuilder.loadTexts:dot1dPortOutboundAccessPriorityTable.setStatus(_A)
_Dot1dPortOutboundAccessPriorityEntry_Object=MibTableRow
dot1dPortOutboundAccessPriorityEntry=_Dot1dPortOutboundAccessPriorityEntry_Object((1,3,6,1,2,1,17,6,1,2,4,1))
dot1dPortOutboundAccessPriorityEntry.setIndexNames((0,_F,_G),(0,_B,_M))
if mibBuilder.loadTexts:dot1dPortOutboundAccessPriorityEntry.setStatus(_A)
class _Dot1dPortOutboundAccessPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_Dot1dPortOutboundAccessPriority_Type.__name__=_E
_Dot1dPortOutboundAccessPriority_Object=MibTableColumn
dot1dPortOutboundAccessPriority=_Dot1dPortOutboundAccessPriority_Object((1,3,6,1,2,1,17,6,1,2,4,1,1),_Dot1dPortOutboundAccessPriority_Type())
dot1dPortOutboundAccessPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:dot1dPortOutboundAccessPriority.setStatus(_A)
_Dot1dGarp_ObjectIdentity=ObjectIdentity
dot1dGarp=_Dot1dGarp_ObjectIdentity((1,3,6,1,2,1,17,6,1,3))
_Dot1dPortGarpTable_Object=MibTable
dot1dPortGarpTable=_Dot1dPortGarpTable_Object((1,3,6,1,2,1,17,6,1,3,1))
if mibBuilder.loadTexts:dot1dPortGarpTable.setStatus(_A)
_Dot1dPortGarpEntry_Object=MibTableRow
dot1dPortGarpEntry=_Dot1dPortGarpEntry_Object((1,3,6,1,2,1,17,6,1,3,1,1))
if mibBuilder.loadTexts:dot1dPortGarpEntry.setStatus(_A)
class _Dot1dPortGarpJoinTime_Type(TimeInterval):defaultValue=20
_Dot1dPortGarpJoinTime_Type.__name__=_H
_Dot1dPortGarpJoinTime_Object=MibTableColumn
dot1dPortGarpJoinTime=_Dot1dPortGarpJoinTime_Object((1,3,6,1,2,1,17,6,1,3,1,1,1),_Dot1dPortGarpJoinTime_Type())
dot1dPortGarpJoinTime.setMaxAccess(_D)
if mibBuilder.loadTexts:dot1dPortGarpJoinTime.setStatus(_A)
class _Dot1dPortGarpLeaveTime_Type(TimeInterval):defaultValue=60
_Dot1dPortGarpLeaveTime_Type.__name__=_H
_Dot1dPortGarpLeaveTime_Object=MibTableColumn
dot1dPortGarpLeaveTime=_Dot1dPortGarpLeaveTime_Object((1,3,6,1,2,1,17,6,1,3,1,1,2),_Dot1dPortGarpLeaveTime_Type())
dot1dPortGarpLeaveTime.setMaxAccess(_D)
if mibBuilder.loadTexts:dot1dPortGarpLeaveTime.setStatus(_A)
class _Dot1dPortGarpLeaveAllTime_Type(TimeInterval):defaultValue=1000
_Dot1dPortGarpLeaveAllTime_Type.__name__=_H
_Dot1dPortGarpLeaveAllTime_Object=MibTableColumn
dot1dPortGarpLeaveAllTime=_Dot1dPortGarpLeaveAllTime_Object((1,3,6,1,2,1,17,6,1,3,1,1,3),_Dot1dPortGarpLeaveAllTime_Type())
dot1dPortGarpLeaveAllTime.setMaxAccess(_D)
if mibBuilder.loadTexts:dot1dPortGarpLeaveAllTime.setStatus(_A)
_Dot1dGmrp_ObjectIdentity=ObjectIdentity
dot1dGmrp=_Dot1dGmrp_ObjectIdentity((1,3,6,1,2,1,17,6,1,4))
_Dot1dPortGmrpTable_Object=MibTable
dot1dPortGmrpTable=_Dot1dPortGmrpTable_Object((1,3,6,1,2,1,17,6,1,4,1))
if mibBuilder.loadTexts:dot1dPortGmrpTable.setStatus(_A)
_Dot1dPortGmrpEntry_Object=MibTableRow
dot1dPortGmrpEntry=_Dot1dPortGmrpEntry_Object((1,3,6,1,2,1,17,6,1,4,1,1))
if mibBuilder.loadTexts:dot1dPortGmrpEntry.setStatus(_A)
class _Dot1dPortGmrpStatus_Type(EnabledStatus):defaultValue=1
_Dot1dPortGmrpStatus_Type.__name__=_L
_Dot1dPortGmrpStatus_Object=MibTableColumn
dot1dPortGmrpStatus=_Dot1dPortGmrpStatus_Object((1,3,6,1,2,1,17,6,1,4,1,1,1),_Dot1dPortGmrpStatus_Type())
dot1dPortGmrpStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:dot1dPortGmrpStatus.setStatus(_A)
_Dot1dPortGmrpFailedRegistrations_Type=Counter32
_Dot1dPortGmrpFailedRegistrations_Object=MibTableColumn
dot1dPortGmrpFailedRegistrations=_Dot1dPortGmrpFailedRegistrations_Object((1,3,6,1,2,1,17,6,1,4,1,1,2),_Dot1dPortGmrpFailedRegistrations_Type())
dot1dPortGmrpFailedRegistrations.setMaxAccess(_C)
if mibBuilder.loadTexts:dot1dPortGmrpFailedRegistrations.setStatus(_A)
_Dot1dPortGmrpLastPduOrigin_Type=MacAddress
_Dot1dPortGmrpLastPduOrigin_Object=MibTableColumn
dot1dPortGmrpLastPduOrigin=_Dot1dPortGmrpLastPduOrigin_Object((1,3,6,1,2,1,17,6,1,4,1,1,3),_Dot1dPortGmrpLastPduOrigin_Type())
dot1dPortGmrpLastPduOrigin.setMaxAccess(_C)
if mibBuilder.loadTexts:dot1dPortGmrpLastPduOrigin.setStatus(_A)
class _Dot1dPortRestrictedGroupRegistration_Type(TruthValue):defaultValue=2
_Dot1dPortRestrictedGroupRegistration_Type.__name__=_K
_Dot1dPortRestrictedGroupRegistration_Object=MibTableColumn
dot1dPortRestrictedGroupRegistration=_Dot1dPortRestrictedGroupRegistration_Object((1,3,6,1,2,1,17,6,1,4,1,1,4),_Dot1dPortRestrictedGroupRegistration_Type())
dot1dPortRestrictedGroupRegistration.setMaxAccess(_D)
if mibBuilder.loadTexts:dot1dPortRestrictedGroupRegistration.setStatus(_A)
_PBridgeConformance_ObjectIdentity=ObjectIdentity
pBridgeConformance=_PBridgeConformance_ObjectIdentity((1,3,6,1,2,1,17,6,2))
_PBridgeGroups_ObjectIdentity=ObjectIdentity
pBridgeGroups=_PBridgeGroups_ObjectIdentity((1,3,6,1,2,1,17,6,2,1))
_PBridgeCompliances_ObjectIdentity=ObjectIdentity
pBridgeCompliances=_PBridgeCompliances_ObjectIdentity((1,3,6,1,2,1,17,6,2,2))
dot1dBasePortEntry.registerAugmentions((_B,_d))
dot1dPortCapabilitiesEntry.setIndexNames(*dot1dBasePortEntry.getIndexNames())
dot1dBasePortEntry.registerAugmentions((_B,_e))
dot1dPortPriorityEntry.setIndexNames(*dot1dBasePortEntry.getIndexNames())
dot1dBasePortEntry.registerAugmentions((_B,_f))
dot1dPortGarpEntry.setIndexNames(*dot1dBasePortEntry.getIndexNames())
dot1dBasePortEntry.registerAugmentions((_B,_g))
dot1dPortGmrpEntry.setIndexNames(*dot1dBasePortEntry.getIndexNames())
pBridgeExtCapGroup=ObjectGroup((1,3,6,1,2,1,17,6,2,1,1))
pBridgeExtCapGroup.setObjects(*((_B,_h),(_B,_i)))
if mibBuilder.loadTexts:pBridgeExtCapGroup.setStatus(_A)
pBridgeDeviceGmrpGroup=ObjectGroup((1,3,6,1,2,1,17,6,2,1,2))
pBridgeDeviceGmrpGroup.setObjects((_B,_j))
if mibBuilder.loadTexts:pBridgeDeviceGmrpGroup.setStatus(_A)
pBridgeDevicePriorityGroup=ObjectGroup((1,3,6,1,2,1,17,6,2,1,3))
pBridgeDevicePriorityGroup.setObjects((_B,_k))
if mibBuilder.loadTexts:pBridgeDevicePriorityGroup.setStatus(_A)
pBridgeDefaultPriorityGroup=ObjectGroup((1,3,6,1,2,1,17,6,2,1,4))
pBridgeDefaultPriorityGroup.setObjects((_B,_l))
if mibBuilder.loadTexts:pBridgeDefaultPriorityGroup.setStatus(_A)
pBridgeRegenPriorityGroup=ObjectGroup((1,3,6,1,2,1,17,6,2,1,5))
pBridgeRegenPriorityGroup.setObjects((_B,_M))
if mibBuilder.loadTexts:pBridgeRegenPriorityGroup.setStatus(_A)
pBridgePriorityGroup=ObjectGroup((1,3,6,1,2,1,17,6,2,1,6))
pBridgePriorityGroup.setObjects(*((_B,_m),(_B,_n)))
if mibBuilder.loadTexts:pBridgePriorityGroup.setStatus(_A)
pBridgeAccessPriorityGroup=ObjectGroup((1,3,6,1,2,1,17,6,2,1,7))
pBridgeAccessPriorityGroup.setObjects((_B,_o))
if mibBuilder.loadTexts:pBridgeAccessPriorityGroup.setStatus(_A)
pBridgePortGarpGroup=ObjectGroup((1,3,6,1,2,1,17,6,2,1,8))
pBridgePortGarpGroup.setObjects(*((_B,_p),(_B,_q),(_B,_r)))
if mibBuilder.loadTexts:pBridgePortGarpGroup.setStatus(_A)
pBridgePortGmrpGroup=ObjectGroup((1,3,6,1,2,1,17,6,2,1,9))
pBridgePortGmrpGroup.setObjects(*((_B,_N),(_B,_O),(_B,_P)))
if mibBuilder.loadTexts:pBridgePortGmrpGroup.setStatus(_s)
pBridgeHCPortGroup=ObjectGroup((1,3,6,1,2,1,17,6,2,1,10))
pBridgeHCPortGroup.setObjects(*((_B,_t),(_B,_u),(_B,_v)))
if mibBuilder.loadTexts:pBridgeHCPortGroup.setStatus(_A)
pBridgePortOverflowGroup=ObjectGroup((1,3,6,1,2,1,17,6,2,1,11))
pBridgePortOverflowGroup.setObjects(*((_B,_w),(_B,_x),(_B,_y)))
if mibBuilder.loadTexts:pBridgePortOverflowGroup.setStatus(_A)
pBridgePortGmrpGroup2=ObjectGroup((1,3,6,1,2,1,17,6,2,1,12))
pBridgePortGmrpGroup2.setObjects(*((_B,_N),(_B,_O),(_B,_P),(_B,_z)))
if mibBuilder.loadTexts:pBridgePortGmrpGroup2.setStatus(_A)
pBridgeCompliance=ModuleCompliance((1,3,6,1,2,1,17,6,2,2,1))
pBridgeCompliance.setObjects(*((_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_A0),(_B,_Y),(_B,_Z)))
if mibBuilder.loadTexts:pBridgeCompliance.setStatus(_s)
pBridgeCompliance2=ModuleCompliance((1,3,6,1,2,1,17,6,2,2,2))
pBridgeCompliance2.setObjects(*((_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_A1),(_B,_Y),(_B,_Z)))
if mibBuilder.loadTexts:pBridgeCompliance2.setStatus(_A)
mibBuilder.exportSymbols(_B,**{_L:EnabledStatus,'dot1dTpHCPortTable':dot1dTpHCPortTable,'dot1dTpHCPortEntry':dot1dTpHCPortEntry,_t:dot1dTpHCPortInFrames,_u:dot1dTpHCPortOutFrames,_v:dot1dTpHCPortInDiscards,'dot1dTpPortOverflowTable':dot1dTpPortOverflowTable,'dot1dTpPortOverflowEntry':dot1dTpPortOverflowEntry,_w:dot1dTpPortInOverflowFrames,_x:dot1dTpPortOutOverflowFrames,_y:dot1dTpPortInOverflowDiscards,'pBridgeMIB':pBridgeMIB,'pBridgeMIBObjects':pBridgeMIBObjects,'dot1dExtBase':dot1dExtBase,_h:dot1dDeviceCapabilities,_k:dot1dTrafficClassesEnabled,_j:dot1dGmrpStatus,'dot1dPortCapabilitiesTable':dot1dPortCapabilitiesTable,_d:dot1dPortCapabilitiesEntry,_i:dot1dPortCapabilities,'dot1dPriority':dot1dPriority,'dot1dPortPriorityTable':dot1dPortPriorityTable,_e:dot1dPortPriorityEntry,_l:dot1dPortDefaultUserPriority,_m:dot1dPortNumTrafficClasses,'dot1dUserPriorityRegenTable':dot1dUserPriorityRegenTable,'dot1dUserPriorityRegenEntry':dot1dUserPriorityRegenEntry,_a:dot1dUserPriority,_M:dot1dRegenUserPriority,'dot1dTrafficClassTable':dot1dTrafficClassTable,'dot1dTrafficClassEntry':dot1dTrafficClassEntry,_c:dot1dTrafficClassPriority,_n:dot1dTrafficClass,'dot1dPortOutboundAccessPriorityTable':dot1dPortOutboundAccessPriorityTable,'dot1dPortOutboundAccessPriorityEntry':dot1dPortOutboundAccessPriorityEntry,_o:dot1dPortOutboundAccessPriority,'dot1dGarp':dot1dGarp,'dot1dPortGarpTable':dot1dPortGarpTable,_f:dot1dPortGarpEntry,_p:dot1dPortGarpJoinTime,_q:dot1dPortGarpLeaveTime,_r:dot1dPortGarpLeaveAllTime,'dot1dGmrp':dot1dGmrp,'dot1dPortGmrpTable':dot1dPortGmrpTable,_g:dot1dPortGmrpEntry,_N:dot1dPortGmrpStatus,_O:dot1dPortGmrpFailedRegistrations,_P:dot1dPortGmrpLastPduOrigin,_z:dot1dPortRestrictedGroupRegistration,'pBridgeConformance':pBridgeConformance,'pBridgeGroups':pBridgeGroups,_Q:pBridgeExtCapGroup,_R:pBridgeDeviceGmrpGroup,_S:pBridgeDevicePriorityGroup,_T:pBridgeDefaultPriorityGroup,_U:pBridgeRegenPriorityGroup,_V:pBridgePriorityGroup,_W:pBridgeAccessPriorityGroup,_X:pBridgePortGarpGroup,_A0:pBridgePortGmrpGroup,_Y:pBridgeHCPortGroup,_Z:pBridgePortOverflowGroup,_A1:pBridgePortGmrpGroup2,'pBridgeCompliances':pBridgeCompliances,'pBridgeCompliance':pBridgeCompliance,'pBridgeCompliance2':pBridgeCompliance2})