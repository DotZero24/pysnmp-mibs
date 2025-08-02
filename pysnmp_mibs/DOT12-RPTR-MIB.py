_AL='vgRptrStats64Group'
_AK='vgRptrNotificationsGroup'
_AJ='vgRptrAddrGroup'
_AI='vgRptrStatsGroup'
_AH='vgRptrConfigGroup'
_AG='vgRptrResetEvent'
_AF='vgRptrHealth'
_AE='vgRptrMgrDetectedDupAddress'
_AD='vgRptrRptrDetectedDupAddress'
_AC='vgRptrAddrTrainedAddrChanges'
_AB='vgRptrAddrLastTrainedAddress'
_AA='vgRptrPortHCNormPriorityOctets'
_A9='vgRptrPortHCHighPriorityOctets'
_A8='vgRptrPortHCUnreadableOctets'
_A7='vgRptrPortHCReadableOctets'
_A6='vgRptrMonHCTotalReadableOctets'
_A5='vgRptrPortLastChange'
_A4='vgRptrPortTransitionToTrainings'
_A3='vgRptrPortPriorityPromotions'
_A2='vgRptrPortDataErrorFrames'
_A1='vgRptrPortOversizeFrames'
_A0='vgRptrPortIPMFrames'
_z='vgRptrPortNullAddressedFrames'
_y='vgRptrPortMulticastFrames'
_x='vgRptrPortBroadcastFrames'
_w='vgRptrPortNormPriOctetRollovers'
_v='vgRptrPortNormPriorityOctets'
_u='vgRptrPortNormPriorityFrames'
_t='vgRptrPortHighPriOctetRollovers'
_s='vgRptrPortHighPriorityOctets'
_r='vgRptrPortHighPriorityFrames'
_q='vgRptrPortUnreadOctetRollovers'
_p='vgRptrPortUnreadableOctets'
_o='vgRptrPortReadOctetRollovers'
_n='vgRptrPortReadableOctets'
_m='vgRptrPortReadableFrames'
_l='vgRptrMonTotalErrors'
_k='vgRptrMonReadableOctetRollovers'
_j='vgRptrMonTotalReadableOctets'
_i='vgRptrMonTotalReadableFrames'
_h='vgRptrPortRptrInfoIndex'
_g='vgRptrPortPriorityEnable'
_f='vgRptrPortTrainingResult'
_e='vgRptrPortLastTrainConfig'
_d='vgRptrPortAllowedTrainType'
_c='vgRptrPortSupportedCascadeMode'
_b='vgRptrPortSupportedPromiscMode'
_a='vgRptrPortOperStatus'
_Z='vgRptrPortAdminStatus'
_Y='vgRptrPortType'
_X='vgRptrGroupCablesBundled'
_W='vgRptrGroupPortCapacity'
_V='vgRptrGroupOperStatus'
_U='vgRptrGroupObjectID'
_T='vgRptrInfoLastChange'
_S='vgRptrInfoReset'
_R='vgRptrInfoTrainingVersion'
_Q='vgRptrInfoFramingCapability'
_P='vgRptrInfoDesiredFramingType'
_O='vgRptrInfoCurrentFramingType'
_N='vgRptrInfoMACAddress'
_M='frameType88025'
_L='frameType88023'
_K='not-accessible'
_J='vgRptrInfoIndex'
_I='vgRptrInfoOperStatus'
_H='vgRptrPortIndex'
_G='OctetString'
_F='vgRptrGroupIndex'
_E='read-write'
_D='Integer32'
_C='read-only'
_B='DOT12-RPTR-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_G,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso,mib_2=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso','mib-2')
DisplayString,MacAddress,PhysAddress,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','TextualConvention','TimeStamp','TruthValue')
vgRptrMIB=ModuleIdentity((1,3,6,1,2,1,53))
_VgRptrObjects_ObjectIdentity=ObjectIdentity
vgRptrObjects=_VgRptrObjects_ObjectIdentity((1,3,6,1,2,1,53,1))
_VgRptrBasic_ObjectIdentity=ObjectIdentity
vgRptrBasic=_VgRptrBasic_ObjectIdentity((1,3,6,1,2,1,53,1,1))
_VgRptrBasicRptr_ObjectIdentity=ObjectIdentity
vgRptrBasicRptr=_VgRptrBasicRptr_ObjectIdentity((1,3,6,1,2,1,53,1,1,1))
_VgRptrInfoTable_Object=MibTable
vgRptrInfoTable=_VgRptrInfoTable_Object((1,3,6,1,2,1,53,1,1,1,1))
if mibBuilder.loadTexts:vgRptrInfoTable.setStatus(_A)
_VgRptrInfoEntry_Object=MibTableRow
vgRptrInfoEntry=_VgRptrInfoEntry_Object((1,3,6,1,2,1,53,1,1,1,1,1))
vgRptrInfoEntry.setIndexNames((0,_B,_J))
if mibBuilder.loadTexts:vgRptrInfoEntry.setStatus(_A)
class _VgRptrInfoIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_VgRptrInfoIndex_Type.__name__=_D
_VgRptrInfoIndex_Object=MibTableColumn
vgRptrInfoIndex=_VgRptrInfoIndex_Object((1,3,6,1,2,1,53,1,1,1,1,1,1),_VgRptrInfoIndex_Type())
vgRptrInfoIndex.setMaxAccess(_K)
if mibBuilder.loadTexts:vgRptrInfoIndex.setStatus(_A)
_VgRptrInfoMACAddress_Type=MacAddress
_VgRptrInfoMACAddress_Object=MibTableColumn
vgRptrInfoMACAddress=_VgRptrInfoMACAddress_Object((1,3,6,1,2,1,53,1,1,1,1,1,2),_VgRptrInfoMACAddress_Type())
vgRptrInfoMACAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:vgRptrInfoMACAddress.setStatus(_A)
class _VgRptrInfoCurrentFramingType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_L,1),(_M,2)))
_VgRptrInfoCurrentFramingType_Type.__name__=_D
_VgRptrInfoCurrentFramingType_Object=MibTableColumn
vgRptrInfoCurrentFramingType=_VgRptrInfoCurrentFramingType_Object((1,3,6,1,2,1,53,1,1,1,1,1,3),_VgRptrInfoCurrentFramingType_Type())
vgRptrInfoCurrentFramingType.setMaxAccess(_C)
if mibBuilder.loadTexts:vgRptrInfoCurrentFramingType.setStatus(_A)
class _VgRptrInfoDesiredFramingType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_L,1),(_M,2)))
_VgRptrInfoDesiredFramingType_Type.__name__=_D
_VgRptrInfoDesiredFramingType_Object=MibTableColumn
vgRptrInfoDesiredFramingType=_VgRptrInfoDesiredFramingType_Object((1,3,6,1,2,1,53,1,1,1,1,1,4),_VgRptrInfoDesiredFramingType_Type())
vgRptrInfoDesiredFramingType.setMaxAccess(_E)
if mibBuilder.loadTexts:vgRptrInfoDesiredFramingType.setStatus(_A)
class _VgRptrInfoFramingCapability_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_L,1),(_M,2),('frameTypeEither',3)))
_VgRptrInfoFramingCapability_Type.__name__=_D
_VgRptrInfoFramingCapability_Object=MibTableColumn
vgRptrInfoFramingCapability=_VgRptrInfoFramingCapability_Object((1,3,6,1,2,1,53,1,1,1,1,1,5),_VgRptrInfoFramingCapability_Type())
vgRptrInfoFramingCapability.setMaxAccess(_C)
if mibBuilder.loadTexts:vgRptrInfoFramingCapability.setStatus(_A)
class _VgRptrInfoTrainingVersion_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_VgRptrInfoTrainingVersion_Type.__name__=_D
_VgRptrInfoTrainingVersion_Object=MibTableColumn
vgRptrInfoTrainingVersion=_VgRptrInfoTrainingVersion_Object((1,3,6,1,2,1,53,1,1,1,1,1,6),_VgRptrInfoTrainingVersion_Type())
vgRptrInfoTrainingVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:vgRptrInfoTrainingVersion.setStatus(_A)
class _VgRptrInfoOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('other',1),('ok',2),('generalFailure',3)))
_VgRptrInfoOperStatus_Type.__name__=_D
_VgRptrInfoOperStatus_Object=MibTableColumn
vgRptrInfoOperStatus=_VgRptrInfoOperStatus_Object((1,3,6,1,2,1,53,1,1,1,1,1,7),_VgRptrInfoOperStatus_Type())
vgRptrInfoOperStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:vgRptrInfoOperStatus.setStatus(_A)
class _VgRptrInfoReset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('noReset',1),('reset',2)))
_VgRptrInfoReset_Type.__name__=_D
_VgRptrInfoReset_Object=MibTableColumn
vgRptrInfoReset=_VgRptrInfoReset_Object((1,3,6,1,2,1,53,1,1,1,1,1,8),_VgRptrInfoReset_Type())
vgRptrInfoReset.setMaxAccess(_E)
if mibBuilder.loadTexts:vgRptrInfoReset.setStatus(_A)
_VgRptrInfoLastChange_Type=TimeStamp
_VgRptrInfoLastChange_Object=MibTableColumn
vgRptrInfoLastChange=_VgRptrInfoLastChange_Object((1,3,6,1,2,1,53,1,1,1,1,1,9),_VgRptrInfoLastChange_Type())
vgRptrInfoLastChange.setMaxAccess(_C)
if mibBuilder.loadTexts:vgRptrInfoLastChange.setStatus(_A)
_VgRptrBasicGroup_ObjectIdentity=ObjectIdentity
vgRptrBasicGroup=_VgRptrBasicGroup_ObjectIdentity((1,3,6,1,2,1,53,1,1,2))
_VgRptrBasicGroupTable_Object=MibTable
vgRptrBasicGroupTable=_VgRptrBasicGroupTable_Object((1,3,6,1,2,1,53,1,1,2,1))
if mibBuilder.loadTexts:vgRptrBasicGroupTable.setStatus(_A)
_VgRptrBasicGroupEntry_Object=MibTableRow
vgRptrBasicGroupEntry=_VgRptrBasicGroupEntry_Object((1,3,6,1,2,1,53,1,1,2,1,1))
vgRptrBasicGroupEntry.setIndexNames((0,_B,_F))
if mibBuilder.loadTexts:vgRptrBasicGroupEntry.setStatus(_A)
class _VgRptrGroupIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2146483647))
_VgRptrGroupIndex_Type.__name__=_D
_VgRptrGroupIndex_Object=MibTableColumn
vgRptrGroupIndex=_VgRptrGroupIndex_Object((1,3,6,1,2,1,53,1,1,2,1,1,1),_VgRptrGroupIndex_Type())
vgRptrGroupIndex.setMaxAccess(_K)
if mibBuilder.loadTexts:vgRptrGroupIndex.setStatus(_A)
_VgRptrGroupObjectID_Type=ObjectIdentifier
_VgRptrGroupObjectID_Object=MibTableColumn
vgRptrGroupObjectID=_VgRptrGroupObjectID_Object((1,3,6,1,2,1,53,1,1,2,1,1,2),_VgRptrGroupObjectID_Type())
vgRptrGroupObjectID.setMaxAccess(_C)
if mibBuilder.loadTexts:vgRptrGroupObjectID.setStatus(_A)
class _VgRptrGroupOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('other',1),('operational',2),('malfunctioning',3),('notPresent',4),('underTest',5),('resetInProgress',6)))
_VgRptrGroupOperStatus_Type.__name__=_D
_VgRptrGroupOperStatus_Object=MibTableColumn
vgRptrGroupOperStatus=_VgRptrGroupOperStatus_Object((1,3,6,1,2,1,53,1,1,2,1,1,3),_VgRptrGroupOperStatus_Type())
vgRptrGroupOperStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:vgRptrGroupOperStatus.setStatus(_A)
class _VgRptrGroupPortCapacity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2146483647))
_VgRptrGroupPortCapacity_Type.__name__=_D
_VgRptrGroupPortCapacity_Object=MibTableColumn
vgRptrGroupPortCapacity=_VgRptrGroupPortCapacity_Object((1,3,6,1,2,1,53,1,1,2,1,1,4),_VgRptrGroupPortCapacity_Type())
vgRptrGroupPortCapacity.setMaxAccess(_C)
if mibBuilder.loadTexts:vgRptrGroupPortCapacity.setStatus(_A)
class _VgRptrGroupCablesBundled_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('someCablesBundled',1),('noCablesBundled',2)))
_VgRptrGroupCablesBundled_Type.__name__=_D
_VgRptrGroupCablesBundled_Object=MibTableColumn
vgRptrGroupCablesBundled=_VgRptrGroupCablesBundled_Object((1,3,6,1,2,1,53,1,1,2,1,1,5),_VgRptrGroupCablesBundled_Type())
vgRptrGroupCablesBundled.setMaxAccess(_E)
if mibBuilder.loadTexts:vgRptrGroupCablesBundled.setStatus(_A)
_VgRptrBasicPort_ObjectIdentity=ObjectIdentity
vgRptrBasicPort=_VgRptrBasicPort_ObjectIdentity((1,3,6,1,2,1,53,1,1,3))
_VgRptrBasicPortTable_Object=MibTable
vgRptrBasicPortTable=_VgRptrBasicPortTable_Object((1,3,6,1,2,1,53,1,1,3,1))
if mibBuilder.loadTexts:vgRptrBasicPortTable.setStatus(_A)
_VgRptrBasicPortEntry_Object=MibTableRow
vgRptrBasicPortEntry=_VgRptrBasicPortEntry_Object((1,3,6,1,2,1,53,1,1,3,1,1))
vgRptrBasicPortEntry.setIndexNames((0,_B,_F),(0,_B,_H))
if mibBuilder.loadTexts:vgRptrBasicPortEntry.setStatus(_A)
class _VgRptrPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_VgRptrPortIndex_Type.__name__=_D
_VgRptrPortIndex_Object=MibTableColumn
vgRptrPortIndex=_VgRptrPortIndex_Object((1,3,6,1,2,1,53,1,1,3,1,1,1),_VgRptrPortIndex_Type())
vgRptrPortIndex.setMaxAccess(_K)
if mibBuilder.loadTexts:vgRptrPortIndex.setStatus(_A)
class _VgRptrPortType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('cascadeExternal',1),('cascadeInternal',2),('localExternal',3),('localInternal',4)))
_VgRptrPortType_Type.__name__=_D
_VgRptrPortType_Object=MibTableColumn
vgRptrPortType=_VgRptrPortType_Object((1,3,6,1,2,1,53,1,1,3,1,1,2),_VgRptrPortType_Type())
vgRptrPortType.setMaxAccess(_C)
if mibBuilder.loadTexts:vgRptrPortType.setStatus(_A)
class _VgRptrPortAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),('disabled',2)))
_VgRptrPortAdminStatus_Type.__name__=_D
_VgRptrPortAdminStatus_Object=MibTableColumn
vgRptrPortAdminStatus=_VgRptrPortAdminStatus_Object((1,3,6,1,2,1,53,1,1,3,1,1,3),_VgRptrPortAdminStatus_Type())
vgRptrPortAdminStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:vgRptrPortAdminStatus.setStatus(_A)
class _VgRptrPortOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('active',1),('inactive',2),('training',3)))
_VgRptrPortOperStatus_Type.__name__=_D
_VgRptrPortOperStatus_Object=MibTableColumn
vgRptrPortOperStatus=_VgRptrPortOperStatus_Object((1,3,6,1,2,1,53,1,1,3,1,1,4),_VgRptrPortOperStatus_Type())
vgRptrPortOperStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:vgRptrPortOperStatus.setStatus(_A)
class _VgRptrPortSupportedPromiscMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('singleModeOnly',1),('singleOrPromiscMode',2),('promiscModeOnly',3)))
_VgRptrPortSupportedPromiscMode_Type.__name__=_D
_VgRptrPortSupportedPromiscMode_Object=MibTableColumn
vgRptrPortSupportedPromiscMode=_VgRptrPortSupportedPromiscMode_Object((1,3,6,1,2,1,53,1,1,3,1,1,5),_VgRptrPortSupportedPromiscMode_Type())
vgRptrPortSupportedPromiscMode.setMaxAccess(_C)
if mibBuilder.loadTexts:vgRptrPortSupportedPromiscMode.setStatus(_A)
class _VgRptrPortSupportedCascadeMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('endNodesOnly',1),('endNodesOrRepeaters',2),('cascadePort',3)))
_VgRptrPortSupportedCascadeMode_Type.__name__=_D
_VgRptrPortSupportedCascadeMode_Object=MibTableColumn
vgRptrPortSupportedCascadeMode=_VgRptrPortSupportedCascadeMode_Object((1,3,6,1,2,1,53,1,1,3,1,1,6),_VgRptrPortSupportedCascadeMode_Type())
vgRptrPortSupportedCascadeMode.setMaxAccess(_C)
if mibBuilder.loadTexts:vgRptrPortSupportedCascadeMode.setStatus(_A)
class _VgRptrPortAllowedTrainType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('allowEndNodesOnly',1),('allowPromiscuousEndNodes',2),('allowEndNodesOrRepeaters',3),('allowAnything',4)))
_VgRptrPortAllowedTrainType_Type.__name__=_D
_VgRptrPortAllowedTrainType_Object=MibTableColumn
vgRptrPortAllowedTrainType=_VgRptrPortAllowedTrainType_Object((1,3,6,1,2,1,53,1,1,3,1,1,7),_VgRptrPortAllowedTrainType_Type())
vgRptrPortAllowedTrainType.setMaxAccess(_E)
if mibBuilder.loadTexts:vgRptrPortAllowedTrainType.setStatus(_A)
class _VgRptrPortLastTrainConfig_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,2));fixedLength=2
_VgRptrPortLastTrainConfig_Type.__name__=_G
_VgRptrPortLastTrainConfig_Object=MibTableColumn
vgRptrPortLastTrainConfig=_VgRptrPortLastTrainConfig_Object((1,3,6,1,2,1,53,1,1,3,1,1,8),_VgRptrPortLastTrainConfig_Type())
vgRptrPortLastTrainConfig.setMaxAccess(_C)
if mibBuilder.loadTexts:vgRptrPortLastTrainConfig.setStatus(_A)
class _VgRptrPortTrainingResult_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(3,3));fixedLength=3
_VgRptrPortTrainingResult_Type.__name__=_G
_VgRptrPortTrainingResult_Object=MibTableColumn
vgRptrPortTrainingResult=_VgRptrPortTrainingResult_Object((1,3,6,1,2,1,53,1,1,3,1,1,9),_VgRptrPortTrainingResult_Type())
vgRptrPortTrainingResult.setMaxAccess(_C)
if mibBuilder.loadTexts:vgRptrPortTrainingResult.setStatus(_A)
_VgRptrPortPriorityEnable_Type=TruthValue
_VgRptrPortPriorityEnable_Object=MibTableColumn
vgRptrPortPriorityEnable=_VgRptrPortPriorityEnable_Object((1,3,6,1,2,1,53,1,1,3,1,1,10),_VgRptrPortPriorityEnable_Type())
vgRptrPortPriorityEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:vgRptrPortPriorityEnable.setStatus(_A)
class _VgRptrPortRptrInfoIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_VgRptrPortRptrInfoIndex_Type.__name__=_D
_VgRptrPortRptrInfoIndex_Object=MibTableColumn
vgRptrPortRptrInfoIndex=_VgRptrPortRptrInfoIndex_Object((1,3,6,1,2,1,53,1,1,3,1,1,11),_VgRptrPortRptrInfoIndex_Type())
vgRptrPortRptrInfoIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:vgRptrPortRptrInfoIndex.setStatus(_A)
_VgRptrMonitor_ObjectIdentity=ObjectIdentity
vgRptrMonitor=_VgRptrMonitor_ObjectIdentity((1,3,6,1,2,1,53,1,2))
_VgRptrMonRepeater_ObjectIdentity=ObjectIdentity
vgRptrMonRepeater=_VgRptrMonRepeater_ObjectIdentity((1,3,6,1,2,1,53,1,2,1))
_VgRptrMonitorTable_Object=MibTable
vgRptrMonitorTable=_VgRptrMonitorTable_Object((1,3,6,1,2,1,53,1,2,1,1))
if mibBuilder.loadTexts:vgRptrMonitorTable.setStatus(_A)
_VgRptrMonitorEntry_Object=MibTableRow
vgRptrMonitorEntry=_VgRptrMonitorEntry_Object((1,3,6,1,2,1,53,1,2,1,1,1))
vgRptrMonitorEntry.setIndexNames((0,_B,_J))
if mibBuilder.loadTexts:vgRptrMonitorEntry.setStatus(_A)
_VgRptrMonTotalReadableFrames_Type=Counter32
_VgRptrMonTotalReadableFrames_Object=MibTableColumn
vgRptrMonTotalReadableFrames=_VgRptrMonTotalReadableFrames_Object((1,3,6,1,2,1,53,1,2,1,1,1,1),_VgRptrMonTotalReadableFrames_Type())
vgRptrMonTotalReadableFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:vgRptrMonTotalReadableFrames.setStatus(_A)
_VgRptrMonTotalReadableOctets_Type=Counter32
_VgRptrMonTotalReadableOctets_Object=MibTableColumn
vgRptrMonTotalReadableOctets=_VgRptrMonTotalReadableOctets_Object((1,3,6,1,2,1,53,1,2,1,1,1,2),_VgRptrMonTotalReadableOctets_Type())
vgRptrMonTotalReadableOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:vgRptrMonTotalReadableOctets.setStatus(_A)
_VgRptrMonReadableOctetRollovers_Type=Counter32
_VgRptrMonReadableOctetRollovers_Object=MibTableColumn
vgRptrMonReadableOctetRollovers=_VgRptrMonReadableOctetRollovers_Object((1,3,6,1,2,1,53,1,2,1,1,1,3),_VgRptrMonReadableOctetRollovers_Type())
vgRptrMonReadableOctetRollovers.setMaxAccess(_C)
if mibBuilder.loadTexts:vgRptrMonReadableOctetRollovers.setStatus(_A)
_VgRptrMonHCTotalReadableOctets_Type=Counter64
_VgRptrMonHCTotalReadableOctets_Object=MibTableColumn
vgRptrMonHCTotalReadableOctets=_VgRptrMonHCTotalReadableOctets_Object((1,3,6,1,2,1,53,1,2,1,1,1,4),_VgRptrMonHCTotalReadableOctets_Type())
vgRptrMonHCTotalReadableOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:vgRptrMonHCTotalReadableOctets.setStatus(_A)
_VgRptrMonTotalErrors_Type=Counter32
_VgRptrMonTotalErrors_Object=MibTableColumn
vgRptrMonTotalErrors=_VgRptrMonTotalErrors_Object((1,3,6,1,2,1,53,1,2,1,1,1,5),_VgRptrMonTotalErrors_Type())
vgRptrMonTotalErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:vgRptrMonTotalErrors.setStatus(_A)
_VgRptrMonGroup_ObjectIdentity=ObjectIdentity
vgRptrMonGroup=_VgRptrMonGroup_ObjectIdentity((1,3,6,1,2,1,53,1,2,2))
_VgRptrMonPort_ObjectIdentity=ObjectIdentity
vgRptrMonPort=_VgRptrMonPort_ObjectIdentity((1,3,6,1,2,1,53,1,2,3))
_VgRptrMonPortTable_Object=MibTable
vgRptrMonPortTable=_VgRptrMonPortTable_Object((1,3,6,1,2,1,53,1,2,3,1))
if mibBuilder.loadTexts:vgRptrMonPortTable.setStatus(_A)
_VgRptrMonPortEntry_Object=MibTableRow
vgRptrMonPortEntry=_VgRptrMonPortEntry_Object((1,3,6,1,2,1,53,1,2,3,1,1))
vgRptrMonPortEntry.setIndexNames((0,_B,_F),(0,_B,_H))
if mibBuilder.loadTexts:vgRptrMonPortEntry.setStatus(_A)
_VgRptrPortReadableFrames_Type=Counter32
_VgRptrPortReadableFrames_Object=MibTableColumn
vgRptrPortReadableFrames=_VgRptrPortReadableFrames_Object((1,3,6,1,2,1,53,1,2,3,1,1,1),_VgRptrPortReadableFrames_Type())
vgRptrPortReadableFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:vgRptrPortReadableFrames.setStatus(_A)
_VgRptrPortReadableOctets_Type=Counter32
_VgRptrPortReadableOctets_Object=MibTableColumn
vgRptrPortReadableOctets=_VgRptrPortReadableOctets_Object((1,3,6,1,2,1,53,1,2,3,1,1,2),_VgRptrPortReadableOctets_Type())
vgRptrPortReadableOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:vgRptrPortReadableOctets.setStatus(_A)
_VgRptrPortReadOctetRollovers_Type=Counter32
_VgRptrPortReadOctetRollovers_Object=MibTableColumn
vgRptrPortReadOctetRollovers=_VgRptrPortReadOctetRollovers_Object((1,3,6,1,2,1,53,1,2,3,1,1,3),_VgRptrPortReadOctetRollovers_Type())
vgRptrPortReadOctetRollovers.setMaxAccess(_C)
if mibBuilder.loadTexts:vgRptrPortReadOctetRollovers.setStatus(_A)
_VgRptrPortHCReadableOctets_Type=Counter64
_VgRptrPortHCReadableOctets_Object=MibTableColumn
vgRptrPortHCReadableOctets=_VgRptrPortHCReadableOctets_Object((1,3,6,1,2,1,53,1,2,3,1,1,4),_VgRptrPortHCReadableOctets_Type())
vgRptrPortHCReadableOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:vgRptrPortHCReadableOctets.setStatus(_A)
_VgRptrPortUnreadableOctets_Type=Counter32
_VgRptrPortUnreadableOctets_Object=MibTableColumn
vgRptrPortUnreadableOctets=_VgRptrPortUnreadableOctets_Object((1,3,6,1,2,1,53,1,2,3,1,1,5),_VgRptrPortUnreadableOctets_Type())
vgRptrPortUnreadableOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:vgRptrPortUnreadableOctets.setStatus(_A)
_VgRptrPortUnreadOctetRollovers_Type=Counter32
_VgRptrPortUnreadOctetRollovers_Object=MibTableColumn
vgRptrPortUnreadOctetRollovers=_VgRptrPortUnreadOctetRollovers_Object((1,3,6,1,2,1,53,1,2,3,1,1,6),_VgRptrPortUnreadOctetRollovers_Type())
vgRptrPortUnreadOctetRollovers.setMaxAccess(_C)
if mibBuilder.loadTexts:vgRptrPortUnreadOctetRollovers.setStatus(_A)
_VgRptrPortHCUnreadableOctets_Type=Counter64
_VgRptrPortHCUnreadableOctets_Object=MibTableColumn
vgRptrPortHCUnreadableOctets=_VgRptrPortHCUnreadableOctets_Object((1,3,6,1,2,1,53,1,2,3,1,1,7),_VgRptrPortHCUnreadableOctets_Type())
vgRptrPortHCUnreadableOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:vgRptrPortHCUnreadableOctets.setStatus(_A)
_VgRptrPortHighPriorityFrames_Type=Counter32
_VgRptrPortHighPriorityFrames_Object=MibTableColumn
vgRptrPortHighPriorityFrames=_VgRptrPortHighPriorityFrames_Object((1,3,6,1,2,1,53,1,2,3,1,1,8),_VgRptrPortHighPriorityFrames_Type())
vgRptrPortHighPriorityFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:vgRptrPortHighPriorityFrames.setStatus(_A)
_VgRptrPortHighPriorityOctets_Type=Counter32
_VgRptrPortHighPriorityOctets_Object=MibTableColumn
vgRptrPortHighPriorityOctets=_VgRptrPortHighPriorityOctets_Object((1,3,6,1,2,1,53,1,2,3,1,1,9),_VgRptrPortHighPriorityOctets_Type())
vgRptrPortHighPriorityOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:vgRptrPortHighPriorityOctets.setStatus(_A)
_VgRptrPortHighPriOctetRollovers_Type=Counter32
_VgRptrPortHighPriOctetRollovers_Object=MibTableColumn
vgRptrPortHighPriOctetRollovers=_VgRptrPortHighPriOctetRollovers_Object((1,3,6,1,2,1,53,1,2,3,1,1,10),_VgRptrPortHighPriOctetRollovers_Type())
vgRptrPortHighPriOctetRollovers.setMaxAccess(_C)
if mibBuilder.loadTexts:vgRptrPortHighPriOctetRollovers.setStatus(_A)
_VgRptrPortHCHighPriorityOctets_Type=Counter64
_VgRptrPortHCHighPriorityOctets_Object=MibTableColumn
vgRptrPortHCHighPriorityOctets=_VgRptrPortHCHighPriorityOctets_Object((1,3,6,1,2,1,53,1,2,3,1,1,11),_VgRptrPortHCHighPriorityOctets_Type())
vgRptrPortHCHighPriorityOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:vgRptrPortHCHighPriorityOctets.setStatus(_A)
_VgRptrPortNormPriorityFrames_Type=Counter32
_VgRptrPortNormPriorityFrames_Object=MibTableColumn
vgRptrPortNormPriorityFrames=_VgRptrPortNormPriorityFrames_Object((1,3,6,1,2,1,53,1,2,3,1,1,12),_VgRptrPortNormPriorityFrames_Type())
vgRptrPortNormPriorityFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:vgRptrPortNormPriorityFrames.setStatus(_A)
_VgRptrPortNormPriorityOctets_Type=Counter32
_VgRptrPortNormPriorityOctets_Object=MibTableColumn
vgRptrPortNormPriorityOctets=_VgRptrPortNormPriorityOctets_Object((1,3,6,1,2,1,53,1,2,3,1,1,13),_VgRptrPortNormPriorityOctets_Type())
vgRptrPortNormPriorityOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:vgRptrPortNormPriorityOctets.setStatus(_A)
_VgRptrPortNormPriOctetRollovers_Type=Counter32
_VgRptrPortNormPriOctetRollovers_Object=MibTableColumn
vgRptrPortNormPriOctetRollovers=_VgRptrPortNormPriOctetRollovers_Object((1,3,6,1,2,1,53,1,2,3,1,1,14),_VgRptrPortNormPriOctetRollovers_Type())
vgRptrPortNormPriOctetRollovers.setMaxAccess(_C)
if mibBuilder.loadTexts:vgRptrPortNormPriOctetRollovers.setStatus(_A)
_VgRptrPortHCNormPriorityOctets_Type=Counter64
_VgRptrPortHCNormPriorityOctets_Object=MibTableColumn
vgRptrPortHCNormPriorityOctets=_VgRptrPortHCNormPriorityOctets_Object((1,3,6,1,2,1,53,1,2,3,1,1,15),_VgRptrPortHCNormPriorityOctets_Type())
vgRptrPortHCNormPriorityOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:vgRptrPortHCNormPriorityOctets.setStatus(_A)
_VgRptrPortBroadcastFrames_Type=Counter32
_VgRptrPortBroadcastFrames_Object=MibTableColumn
vgRptrPortBroadcastFrames=_VgRptrPortBroadcastFrames_Object((1,3,6,1,2,1,53,1,2,3,1,1,16),_VgRptrPortBroadcastFrames_Type())
vgRptrPortBroadcastFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:vgRptrPortBroadcastFrames.setStatus(_A)
_VgRptrPortMulticastFrames_Type=Counter32
_VgRptrPortMulticastFrames_Object=MibTableColumn
vgRptrPortMulticastFrames=_VgRptrPortMulticastFrames_Object((1,3,6,1,2,1,53,1,2,3,1,1,17),_VgRptrPortMulticastFrames_Type())
vgRptrPortMulticastFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:vgRptrPortMulticastFrames.setStatus(_A)
_VgRptrPortNullAddressedFrames_Type=Counter32
_VgRptrPortNullAddressedFrames_Object=MibTableColumn
vgRptrPortNullAddressedFrames=_VgRptrPortNullAddressedFrames_Object((1,3,6,1,2,1,53,1,2,3,1,1,18),_VgRptrPortNullAddressedFrames_Type())
vgRptrPortNullAddressedFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:vgRptrPortNullAddressedFrames.setStatus(_A)
_VgRptrPortIPMFrames_Type=Counter32
_VgRptrPortIPMFrames_Object=MibTableColumn
vgRptrPortIPMFrames=_VgRptrPortIPMFrames_Object((1,3,6,1,2,1,53,1,2,3,1,1,19),_VgRptrPortIPMFrames_Type())
vgRptrPortIPMFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:vgRptrPortIPMFrames.setStatus(_A)
_VgRptrPortOversizeFrames_Type=Counter32
_VgRptrPortOversizeFrames_Object=MibTableColumn
vgRptrPortOversizeFrames=_VgRptrPortOversizeFrames_Object((1,3,6,1,2,1,53,1,2,3,1,1,20),_VgRptrPortOversizeFrames_Type())
vgRptrPortOversizeFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:vgRptrPortOversizeFrames.setStatus(_A)
_VgRptrPortDataErrorFrames_Type=Counter32
_VgRptrPortDataErrorFrames_Object=MibTableColumn
vgRptrPortDataErrorFrames=_VgRptrPortDataErrorFrames_Object((1,3,6,1,2,1,53,1,2,3,1,1,21),_VgRptrPortDataErrorFrames_Type())
vgRptrPortDataErrorFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:vgRptrPortDataErrorFrames.setStatus(_A)
_VgRptrPortPriorityPromotions_Type=Counter32
_VgRptrPortPriorityPromotions_Object=MibTableColumn
vgRptrPortPriorityPromotions=_VgRptrPortPriorityPromotions_Object((1,3,6,1,2,1,53,1,2,3,1,1,22),_VgRptrPortPriorityPromotions_Type())
vgRptrPortPriorityPromotions.setMaxAccess(_C)
if mibBuilder.loadTexts:vgRptrPortPriorityPromotions.setStatus(_A)
_VgRptrPortTransitionToTrainings_Type=Counter32
_VgRptrPortTransitionToTrainings_Object=MibTableColumn
vgRptrPortTransitionToTrainings=_VgRptrPortTransitionToTrainings_Object((1,3,6,1,2,1,53,1,2,3,1,1,23),_VgRptrPortTransitionToTrainings_Type())
vgRptrPortTransitionToTrainings.setMaxAccess(_C)
if mibBuilder.loadTexts:vgRptrPortTransitionToTrainings.setStatus(_A)
_VgRptrPortLastChange_Type=TimeStamp
_VgRptrPortLastChange_Object=MibTableColumn
vgRptrPortLastChange=_VgRptrPortLastChange_Object((1,3,6,1,2,1,53,1,2,3,1,1,24),_VgRptrPortLastChange_Type())
vgRptrPortLastChange.setMaxAccess(_C)
if mibBuilder.loadTexts:vgRptrPortLastChange.setStatus(_A)
_VgRptrAddrTrack_ObjectIdentity=ObjectIdentity
vgRptrAddrTrack=_VgRptrAddrTrack_ObjectIdentity((1,3,6,1,2,1,53,1,3))
_VgRptrAddrTrackRptr_ObjectIdentity=ObjectIdentity
vgRptrAddrTrackRptr=_VgRptrAddrTrackRptr_ObjectIdentity((1,3,6,1,2,1,53,1,3,1))
_VgRptrAddrTrackGroup_ObjectIdentity=ObjectIdentity
vgRptrAddrTrackGroup=_VgRptrAddrTrackGroup_ObjectIdentity((1,3,6,1,2,1,53,1,3,2))
_VgRptrAddrTrackPort_ObjectIdentity=ObjectIdentity
vgRptrAddrTrackPort=_VgRptrAddrTrackPort_ObjectIdentity((1,3,6,1,2,1,53,1,3,3))
_VgRptrAddrTrackTable_Object=MibTable
vgRptrAddrTrackTable=_VgRptrAddrTrackTable_Object((1,3,6,1,2,1,53,1,3,3,1))
if mibBuilder.loadTexts:vgRptrAddrTrackTable.setStatus(_A)
_VgRptrAddrTrackEntry_Object=MibTableRow
vgRptrAddrTrackEntry=_VgRptrAddrTrackEntry_Object((1,3,6,1,2,1,53,1,3,3,1,1))
vgRptrAddrTrackEntry.setIndexNames((0,_B,_F),(0,_B,_H))
if mibBuilder.loadTexts:vgRptrAddrTrackEntry.setStatus(_A)
class _VgRptrAddrLastTrainedAddress_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,0),ValueSizeConstraint(6,6))
_VgRptrAddrLastTrainedAddress_Type.__name__=_G
_VgRptrAddrLastTrainedAddress_Object=MibTableColumn
vgRptrAddrLastTrainedAddress=_VgRptrAddrLastTrainedAddress_Object((1,3,6,1,2,1,53,1,3,3,1,1,1),_VgRptrAddrLastTrainedAddress_Type())
vgRptrAddrLastTrainedAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:vgRptrAddrLastTrainedAddress.setStatus(_A)
_VgRptrAddrTrainedAddrChanges_Type=Counter32
_VgRptrAddrTrainedAddrChanges_Object=MibTableColumn
vgRptrAddrTrainedAddrChanges=_VgRptrAddrTrainedAddrChanges_Object((1,3,6,1,2,1,53,1,3,3,1,1,2),_VgRptrAddrTrainedAddrChanges_Type())
vgRptrAddrTrainedAddrChanges.setMaxAccess(_C)
if mibBuilder.loadTexts:vgRptrAddrTrainedAddrChanges.setStatus(_A)
_VgRptrRptrDetectedDupAddress_Type=TruthValue
_VgRptrRptrDetectedDupAddress_Object=MibTableColumn
vgRptrRptrDetectedDupAddress=_VgRptrRptrDetectedDupAddress_Object((1,3,6,1,2,1,53,1,3,3,1,1,3),_VgRptrRptrDetectedDupAddress_Type())
vgRptrRptrDetectedDupAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:vgRptrRptrDetectedDupAddress.setStatus(_A)
_VgRptrMgrDetectedDupAddress_Type=TruthValue
_VgRptrMgrDetectedDupAddress_Object=MibTableColumn
vgRptrMgrDetectedDupAddress=_VgRptrMgrDetectedDupAddress_Object((1,3,6,1,2,1,53,1,3,3,1,1,4),_VgRptrMgrDetectedDupAddress_Type())
vgRptrMgrDetectedDupAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:vgRptrMgrDetectedDupAddress.setStatus(_A)
_VgRptrTraps_ObjectIdentity=ObjectIdentity
vgRptrTraps=_VgRptrTraps_ObjectIdentity((1,3,6,1,2,1,53,2))
_VgRptrTrapPrefix_ObjectIdentity=ObjectIdentity
vgRptrTrapPrefix=_VgRptrTrapPrefix_ObjectIdentity((1,3,6,1,2,1,53,2,0))
_VgRptrConformance_ObjectIdentity=ObjectIdentity
vgRptrConformance=_VgRptrConformance_ObjectIdentity((1,3,6,1,2,1,53,3))
_VgRptrCompliances_ObjectIdentity=ObjectIdentity
vgRptrCompliances=_VgRptrCompliances_ObjectIdentity((1,3,6,1,2,1,53,3,1))
_VgRptrGroups_ObjectIdentity=ObjectIdentity
vgRptrGroups=_VgRptrGroups_ObjectIdentity((1,3,6,1,2,1,53,3,2))
vgRptrConfigGroup=ObjectGroup((1,3,6,1,2,1,53,3,2,1))
vgRptrConfigGroup.setObjects(*((_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_I),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h)))
if mibBuilder.loadTexts:vgRptrConfigGroup.setStatus(_A)
vgRptrStatsGroup=ObjectGroup((1,3,6,1,2,1,53,3,2,2))
vgRptrStatsGroup.setObjects(*((_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_x),(_B,_y),(_B,_z),(_B,_A0),(_B,_A1),(_B,_A2),(_B,_A3),(_B,_A4),(_B,_A5)))
if mibBuilder.loadTexts:vgRptrStatsGroup.setStatus(_A)
vgRptrStats64Group=ObjectGroup((1,3,6,1,2,1,53,3,2,3))
vgRptrStats64Group.setObjects(*((_B,_A6),(_B,_A7),(_B,_A8),(_B,_A9),(_B,_AA)))
if mibBuilder.loadTexts:vgRptrStats64Group.setStatus(_A)
vgRptrAddrGroup=ObjectGroup((1,3,6,1,2,1,53,3,2,4))
vgRptrAddrGroup.setObjects(*((_B,_AB),(_B,_AC),(_B,_AD),(_B,_AE)))
if mibBuilder.loadTexts:vgRptrAddrGroup.setStatus(_A)
vgRptrHealth=NotificationType((1,3,6,1,2,1,53,2,0,1))
vgRptrHealth.setObjects((_B,_I))
if mibBuilder.loadTexts:vgRptrHealth.setStatus(_A)
vgRptrResetEvent=NotificationType((1,3,6,1,2,1,53,2,0,2))
vgRptrResetEvent.setObjects((_B,_I))
if mibBuilder.loadTexts:vgRptrResetEvent.setStatus(_A)
vgRptrNotificationsGroup=NotificationGroup((1,3,6,1,2,1,53,3,2,5))
vgRptrNotificationsGroup.setObjects(*((_B,_AF),(_B,_AG)))
if mibBuilder.loadTexts:vgRptrNotificationsGroup.setStatus(_A)
vgRptrCompliance=ModuleCompliance((1,3,6,1,2,1,53,3,1,1))
vgRptrCompliance.setObjects(*((_B,_AH),(_B,_AI),(_B,_AJ),(_B,_AK),(_B,_AL),('SNMP-REPEATER-MIB','snmpRptrGrpRptrAddrSearch')))
if mibBuilder.loadTexts:vgRptrCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'vgRptrMIB':vgRptrMIB,'vgRptrObjects':vgRptrObjects,'vgRptrBasic':vgRptrBasic,'vgRptrBasicRptr':vgRptrBasicRptr,'vgRptrInfoTable':vgRptrInfoTable,'vgRptrInfoEntry':vgRptrInfoEntry,_J:vgRptrInfoIndex,_N:vgRptrInfoMACAddress,_O:vgRptrInfoCurrentFramingType,_P:vgRptrInfoDesiredFramingType,_Q:vgRptrInfoFramingCapability,_R:vgRptrInfoTrainingVersion,_I:vgRptrInfoOperStatus,_S:vgRptrInfoReset,_T:vgRptrInfoLastChange,'vgRptrBasicGroup':vgRptrBasicGroup,'vgRptrBasicGroupTable':vgRptrBasicGroupTable,'vgRptrBasicGroupEntry':vgRptrBasicGroupEntry,_F:vgRptrGroupIndex,_U:vgRptrGroupObjectID,_V:vgRptrGroupOperStatus,_W:vgRptrGroupPortCapacity,_X:vgRptrGroupCablesBundled,'vgRptrBasicPort':vgRptrBasicPort,'vgRptrBasicPortTable':vgRptrBasicPortTable,'vgRptrBasicPortEntry':vgRptrBasicPortEntry,_H:vgRptrPortIndex,_Y:vgRptrPortType,_Z:vgRptrPortAdminStatus,_a:vgRptrPortOperStatus,_b:vgRptrPortSupportedPromiscMode,_c:vgRptrPortSupportedCascadeMode,_d:vgRptrPortAllowedTrainType,_e:vgRptrPortLastTrainConfig,_f:vgRptrPortTrainingResult,_g:vgRptrPortPriorityEnable,_h:vgRptrPortRptrInfoIndex,'vgRptrMonitor':vgRptrMonitor,'vgRptrMonRepeater':vgRptrMonRepeater,'vgRptrMonitorTable':vgRptrMonitorTable,'vgRptrMonitorEntry':vgRptrMonitorEntry,_i:vgRptrMonTotalReadableFrames,_j:vgRptrMonTotalReadableOctets,_k:vgRptrMonReadableOctetRollovers,_A6:vgRptrMonHCTotalReadableOctets,_l:vgRptrMonTotalErrors,'vgRptrMonGroup':vgRptrMonGroup,'vgRptrMonPort':vgRptrMonPort,'vgRptrMonPortTable':vgRptrMonPortTable,'vgRptrMonPortEntry':vgRptrMonPortEntry,_m:vgRptrPortReadableFrames,_n:vgRptrPortReadableOctets,_o:vgRptrPortReadOctetRollovers,_A7:vgRptrPortHCReadableOctets,_p:vgRptrPortUnreadableOctets,_q:vgRptrPortUnreadOctetRollovers,_A8:vgRptrPortHCUnreadableOctets,_r:vgRptrPortHighPriorityFrames,_s:vgRptrPortHighPriorityOctets,_t:vgRptrPortHighPriOctetRollovers,_A9:vgRptrPortHCHighPriorityOctets,_u:vgRptrPortNormPriorityFrames,_v:vgRptrPortNormPriorityOctets,_w:vgRptrPortNormPriOctetRollovers,_AA:vgRptrPortHCNormPriorityOctets,_x:vgRptrPortBroadcastFrames,_y:vgRptrPortMulticastFrames,_z:vgRptrPortNullAddressedFrames,_A0:vgRptrPortIPMFrames,_A1:vgRptrPortOversizeFrames,_A2:vgRptrPortDataErrorFrames,_A3:vgRptrPortPriorityPromotions,_A4:vgRptrPortTransitionToTrainings,_A5:vgRptrPortLastChange,'vgRptrAddrTrack':vgRptrAddrTrack,'vgRptrAddrTrackRptr':vgRptrAddrTrackRptr,'vgRptrAddrTrackGroup':vgRptrAddrTrackGroup,'vgRptrAddrTrackPort':vgRptrAddrTrackPort,'vgRptrAddrTrackTable':vgRptrAddrTrackTable,'vgRptrAddrTrackEntry':vgRptrAddrTrackEntry,_AB:vgRptrAddrLastTrainedAddress,_AC:vgRptrAddrTrainedAddrChanges,_AD:vgRptrRptrDetectedDupAddress,_AE:vgRptrMgrDetectedDupAddress,'vgRptrTraps':vgRptrTraps,'vgRptrTrapPrefix':vgRptrTrapPrefix,_AF:vgRptrHealth,_AG:vgRptrResetEvent,'vgRptrConformance':vgRptrConformance,'vgRptrCompliances':vgRptrCompliances,'vgRptrCompliance':vgRptrCompliance,'vgRptrGroups':vgRptrGroups,_AH:vgRptrConfigGroup,_AI:vgRptrStatsGroup,_AL:vgRptrStats64Group,_AJ:vgRptrAddrGroup,_AK:vgRptrNotificationsGroup})