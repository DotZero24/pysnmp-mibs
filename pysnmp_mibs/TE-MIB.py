_AR='teTunnelRerouted'
_AQ='teTunnelChanged'
_AP='teTunnelDown'
_AO='teTunnelUp'
_AN='tePathHopType'
_AM='tePathHopAddress'
_AL='tePathHopAddrType'
_AK='tePathHopStorageType'
_AJ='tePathHopRowStatus'
_AI='tePathConfiguredRoute'
_AH='tePathStorageType'
_AG='tePathRowStatus'
_AF='tePathType'
_AE='tePrimaryTunnels'
_AD='teActiveTunnels'
_AC='teConfiguredTunnels'
_AB='teAdminGroupRowStatus'
_AA='teAdminGroupName'
_A9='teNextPathHopIndex'
_A8='teNextTunnelIndex'
_A7='teNotificationEnable'
_A6='teSignalingProto'
_A5='teDistProtocol'
_A4='tePathRecordedRoute'
_A3='tePathComputedRoute'
_A2='tePathAdminStatus'
_A1='tePathOperStatus'
_A0='tePathProperties'
_z='tePathHoldPriority'
_y='tePathSetupPriority'
_x='tePathExclude'
_w='tePathIncludeAll'
_v='tePathIncludeAny'
_u='tePathBandwidth'
_t='teTunnelOperationalPaths'
_s='teTunnelStandbyPaths'
_r='teTunnelConfiguredPaths'
_q='teTunnelLastPathChange'
_p='teTunnelPathChanges'
_o='teTunnelLastTransition'
_n='teTunnelTransitions'
_m='teTunnelPrimaryTimeUp'
_l='teTunnelTimeUp'
_k='teTunnelAge'
_j='teTunnelLPPackets'
_i='teTunnelLPOctets'
_h='teTunnelPackets'
_g='teTunnelOctets'
_f='teTunnelDiscontinuityTimer'
_e='teTunnelState'
_d='teTunnelDestinationAddress'
_c='teTunnelDestinationAddressType'
_b='teTunnelSourceAddress'
_a='teTunnelSourceAddressType'
_Z='teTunnelStorageType'
_Y='teTunnelRowStatus'
_X='teTunnelNextPathIndex'
_W='tePathHopIndex'
_V='teHopListIndex'
_U='tePathIndex'
_T='teAdminGroupNumber'
_S='TruthValue'
_R='MplsBitRate'
_Q='testing'
_P='unknown'
_O='teTunnelIndex'
_N='other'
_M='Bits'
_L='SnmpAdminString'
_K='teNotificationGroup'
_J='teTrafficEngineeringGroup'
_I='not-accessible'
_H='tePathName'
_G='teTunnelName'
_F='Unsigned32'
_E='Integer32'
_D='read-create'
_C='read-only'
_B='current'
_A='TE-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
MplsBitRate,TeHopAddress,TeHopAddressType=mibBuilder.importSymbols('MPLS-TC-STD-MIB',_R,'TeHopAddress','TeHopAddressType')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_L)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso,mib_2=mibBuilder.importSymbols('SNMPv2-SMI',_M,'Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_F,'iso','mib-2')
DisplayString,PhysAddress,RowStatus,StorageType,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','StorageType','TextualConvention','TimeStamp',_S)
teMIB=ModuleIdentity((1,3,6,1,2,1,122))
if mibBuilder.loadTexts:teMIB.setRevisions(('2005-01-04 00:00',))
_TeMIBNotifications_ObjectIdentity=ObjectIdentity
teMIBNotifications=_TeMIBNotifications_ObjectIdentity((1,3,6,1,2,1,122,0))
_TeMIBObjects_ObjectIdentity=ObjectIdentity
teMIBObjects=_TeMIBObjects_ObjectIdentity((1,3,6,1,2,1,122,1))
_TeInfo_ObjectIdentity=ObjectIdentity
teInfo=_TeInfo_ObjectIdentity((1,3,6,1,2,1,122,1,1))
class _TeDistProtocol_Type(Bits):namedValues=NamedValues(*((_N,0),('isis',1),('ospf',2)))
_TeDistProtocol_Type.__name__=_M
_TeDistProtocol_Object=MibScalar
teDistProtocol=_TeDistProtocol_Object((1,3,6,1,2,1,122,1,1,1),_TeDistProtocol_Type())
teDistProtocol.setMaxAccess(_C)
if mibBuilder.loadTexts:teDistProtocol.setStatus(_B)
class _TeSignalingProto_Type(Bits):namedValues=NamedValues(*((_N,0),('rsvpte',1),('crldp',2),('static',3)))
_TeSignalingProto_Type.__name__=_M
_TeSignalingProto_Object=MibScalar
teSignalingProto=_TeSignalingProto_Object((1,3,6,1,2,1,122,1,1,2),_TeSignalingProto_Type())
teSignalingProto.setMaxAccess(_C)
if mibBuilder.loadTexts:teSignalingProto.setStatus(_B)
class _TeNotificationEnable_Type(TruthValue):defaultValue=2
_TeNotificationEnable_Type.__name__=_S
_TeNotificationEnable_Object=MibScalar
teNotificationEnable=_TeNotificationEnable_Object((1,3,6,1,2,1,122,1,1,3),_TeNotificationEnable_Type())
teNotificationEnable.setMaxAccess('read-write')
if mibBuilder.loadTexts:teNotificationEnable.setStatus(_B)
_TeNextTunnelIndex_Type=Unsigned32
_TeNextTunnelIndex_Object=MibScalar
teNextTunnelIndex=_TeNextTunnelIndex_Object((1,3,6,1,2,1,122,1,1,4),_TeNextTunnelIndex_Type())
teNextTunnelIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:teNextTunnelIndex.setStatus(_B)
_TeNextPathHopIndex_Type=Unsigned32
_TeNextPathHopIndex_Object=MibScalar
teNextPathHopIndex=_TeNextPathHopIndex_Object((1,3,6,1,2,1,122,1,1,5),_TeNextPathHopIndex_Type())
teNextPathHopIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:teNextPathHopIndex.setStatus(_B)
_TeConfiguredTunnels_Type=Gauge32
_TeConfiguredTunnels_Object=MibScalar
teConfiguredTunnels=_TeConfiguredTunnels_Object((1,3,6,1,2,1,122,1,1,6),_TeConfiguredTunnels_Type())
teConfiguredTunnels.setMaxAccess(_C)
if mibBuilder.loadTexts:teConfiguredTunnels.setStatus(_B)
_TeActiveTunnels_Type=Gauge32
_TeActiveTunnels_Object=MibScalar
teActiveTunnels=_TeActiveTunnels_Object((1,3,6,1,2,1,122,1,1,7),_TeActiveTunnels_Type())
teActiveTunnels.setMaxAccess(_C)
if mibBuilder.loadTexts:teActiveTunnels.setStatus(_B)
_TePrimaryTunnels_Type=Gauge32
_TePrimaryTunnels_Object=MibScalar
tePrimaryTunnels=_TePrimaryTunnels_Object((1,3,6,1,2,1,122,1,1,8),_TePrimaryTunnels_Type())
tePrimaryTunnels.setMaxAccess(_C)
if mibBuilder.loadTexts:tePrimaryTunnels.setStatus(_B)
_TeAdminGroupTable_Object=MibTable
teAdminGroupTable=_TeAdminGroupTable_Object((1,3,6,1,2,1,122,1,1,9))
if mibBuilder.loadTexts:teAdminGroupTable.setStatus(_B)
_TeAdminGroupEntry_Object=MibTableRow
teAdminGroupEntry=_TeAdminGroupEntry_Object((1,3,6,1,2,1,122,1,1,9,1))
teAdminGroupEntry.setIndexNames((0,_A,_T))
if mibBuilder.loadTexts:teAdminGroupEntry.setStatus(_B)
class _TeAdminGroupNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,32))
_TeAdminGroupNumber_Type.__name__=_E
_TeAdminGroupNumber_Object=MibTableColumn
teAdminGroupNumber=_TeAdminGroupNumber_Object((1,3,6,1,2,1,122,1,1,9,1,1),_TeAdminGroupNumber_Type())
teAdminGroupNumber.setMaxAccess(_I)
if mibBuilder.loadTexts:teAdminGroupNumber.setStatus(_B)
class _TeAdminGroupName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_TeAdminGroupName_Type.__name__=_L
_TeAdminGroupName_Object=MibTableColumn
teAdminGroupName=_TeAdminGroupName_Object((1,3,6,1,2,1,122,1,1,9,1,2),_TeAdminGroupName_Type())
teAdminGroupName.setMaxAccess(_D)
if mibBuilder.loadTexts:teAdminGroupName.setStatus(_B)
_TeAdminGroupRowStatus_Type=RowStatus
_TeAdminGroupRowStatus_Object=MibTableColumn
teAdminGroupRowStatus=_TeAdminGroupRowStatus_Object((1,3,6,1,2,1,122,1,1,9,1,3),_TeAdminGroupRowStatus_Type())
teAdminGroupRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:teAdminGroupRowStatus.setStatus(_B)
_TeTunnelTable_Object=MibTable
teTunnelTable=_TeTunnelTable_Object((1,3,6,1,2,1,122,1,2))
if mibBuilder.loadTexts:teTunnelTable.setStatus(_B)
_TeTunnelEntry_Object=MibTableRow
teTunnelEntry=_TeTunnelEntry_Object((1,3,6,1,2,1,122,1,2,1))
teTunnelEntry.setIndexNames((0,_A,_O))
if mibBuilder.loadTexts:teTunnelEntry.setStatus(_B)
class _TeTunnelIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_TeTunnelIndex_Type.__name__=_F
_TeTunnelIndex_Object=MibTableColumn
teTunnelIndex=_TeTunnelIndex_Object((1,3,6,1,2,1,122,1,2,1,1),_TeTunnelIndex_Type())
teTunnelIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:teTunnelIndex.setStatus(_B)
class _TeTunnelName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_TeTunnelName_Type.__name__=_L
_TeTunnelName_Object=MibTableColumn
teTunnelName=_TeTunnelName_Object((1,3,6,1,2,1,122,1,2,1,2),_TeTunnelName_Type())
teTunnelName.setMaxAccess(_D)
if mibBuilder.loadTexts:teTunnelName.setStatus(_B)
_TeTunnelNextPathIndex_Type=Unsigned32
_TeTunnelNextPathIndex_Object=MibTableColumn
teTunnelNextPathIndex=_TeTunnelNextPathIndex_Object((1,3,6,1,2,1,122,1,2,1,3),_TeTunnelNextPathIndex_Type())
teTunnelNextPathIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:teTunnelNextPathIndex.setStatus(_B)
_TeTunnelRowStatus_Type=RowStatus
_TeTunnelRowStatus_Object=MibTableColumn
teTunnelRowStatus=_TeTunnelRowStatus_Object((1,3,6,1,2,1,122,1,2,1,4),_TeTunnelRowStatus_Type())
teTunnelRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:teTunnelRowStatus.setStatus(_B)
_TeTunnelStorageType_Type=StorageType
_TeTunnelStorageType_Object=MibTableColumn
teTunnelStorageType=_TeTunnelStorageType_Object((1,3,6,1,2,1,122,1,2,1,5),_TeTunnelStorageType_Type())
teTunnelStorageType.setMaxAccess(_D)
if mibBuilder.loadTexts:teTunnelStorageType.setStatus(_B)
_TeTunnelSourceAddressType_Type=TeHopAddressType
_TeTunnelSourceAddressType_Object=MibTableColumn
teTunnelSourceAddressType=_TeTunnelSourceAddressType_Object((1,3,6,1,2,1,122,1,2,1,6),_TeTunnelSourceAddressType_Type())
teTunnelSourceAddressType.setMaxAccess(_D)
if mibBuilder.loadTexts:teTunnelSourceAddressType.setStatus(_B)
_TeTunnelSourceAddress_Type=TeHopAddress
_TeTunnelSourceAddress_Object=MibTableColumn
teTunnelSourceAddress=_TeTunnelSourceAddress_Object((1,3,6,1,2,1,122,1,2,1,7),_TeTunnelSourceAddress_Type())
teTunnelSourceAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:teTunnelSourceAddress.setStatus(_B)
_TeTunnelDestinationAddressType_Type=TeHopAddressType
_TeTunnelDestinationAddressType_Object=MibTableColumn
teTunnelDestinationAddressType=_TeTunnelDestinationAddressType_Object((1,3,6,1,2,1,122,1,2,1,8),_TeTunnelDestinationAddressType_Type())
teTunnelDestinationAddressType.setMaxAccess(_D)
if mibBuilder.loadTexts:teTunnelDestinationAddressType.setStatus(_B)
_TeTunnelDestinationAddress_Type=TeHopAddress
_TeTunnelDestinationAddress_Object=MibTableColumn
teTunnelDestinationAddress=_TeTunnelDestinationAddress_Object((1,3,6,1,2,1,122,1,2,1,9),_TeTunnelDestinationAddress_Type())
teTunnelDestinationAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:teTunnelDestinationAddress.setStatus(_B)
class _TeTunnelState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_P,1),('up',2),('down',3),(_Q,4)))
_TeTunnelState_Type.__name__=_E
_TeTunnelState_Object=MibTableColumn
teTunnelState=_TeTunnelState_Object((1,3,6,1,2,1,122,1,2,1,10),_TeTunnelState_Type())
teTunnelState.setMaxAccess(_C)
if mibBuilder.loadTexts:teTunnelState.setStatus(_B)
_TeTunnelDiscontinuityTimer_Type=TimeStamp
_TeTunnelDiscontinuityTimer_Object=MibTableColumn
teTunnelDiscontinuityTimer=_TeTunnelDiscontinuityTimer_Object((1,3,6,1,2,1,122,1,2,1,11),_TeTunnelDiscontinuityTimer_Type())
teTunnelDiscontinuityTimer.setMaxAccess(_C)
if mibBuilder.loadTexts:teTunnelDiscontinuityTimer.setStatus(_B)
_TeTunnelOctets_Type=Counter64
_TeTunnelOctets_Object=MibTableColumn
teTunnelOctets=_TeTunnelOctets_Object((1,3,6,1,2,1,122,1,2,1,12),_TeTunnelOctets_Type())
teTunnelOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:teTunnelOctets.setStatus(_B)
_TeTunnelPackets_Type=Counter64
_TeTunnelPackets_Object=MibTableColumn
teTunnelPackets=_TeTunnelPackets_Object((1,3,6,1,2,1,122,1,2,1,13),_TeTunnelPackets_Type())
teTunnelPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:teTunnelPackets.setStatus(_B)
_TeTunnelLPOctets_Type=Counter32
_TeTunnelLPOctets_Object=MibTableColumn
teTunnelLPOctets=_TeTunnelLPOctets_Object((1,3,6,1,2,1,122,1,2,1,14),_TeTunnelLPOctets_Type())
teTunnelLPOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:teTunnelLPOctets.setStatus(_B)
_TeTunnelLPPackets_Type=Counter32
_TeTunnelLPPackets_Object=MibTableColumn
teTunnelLPPackets=_TeTunnelLPPackets_Object((1,3,6,1,2,1,122,1,2,1,15),_TeTunnelLPPackets_Type())
teTunnelLPPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:teTunnelLPPackets.setStatus(_B)
_TeTunnelAge_Type=TimeTicks
_TeTunnelAge_Object=MibTableColumn
teTunnelAge=_TeTunnelAge_Object((1,3,6,1,2,1,122,1,2,1,16),_TeTunnelAge_Type())
teTunnelAge.setMaxAccess(_C)
if mibBuilder.loadTexts:teTunnelAge.setStatus(_B)
_TeTunnelTimeUp_Type=TimeTicks
_TeTunnelTimeUp_Object=MibTableColumn
teTunnelTimeUp=_TeTunnelTimeUp_Object((1,3,6,1,2,1,122,1,2,1,17),_TeTunnelTimeUp_Type())
teTunnelTimeUp.setMaxAccess(_C)
if mibBuilder.loadTexts:teTunnelTimeUp.setStatus(_B)
_TeTunnelPrimaryTimeUp_Type=TimeTicks
_TeTunnelPrimaryTimeUp_Object=MibTableColumn
teTunnelPrimaryTimeUp=_TeTunnelPrimaryTimeUp_Object((1,3,6,1,2,1,122,1,2,1,18),_TeTunnelPrimaryTimeUp_Type())
teTunnelPrimaryTimeUp.setMaxAccess(_C)
if mibBuilder.loadTexts:teTunnelPrimaryTimeUp.setStatus(_B)
_TeTunnelTransitions_Type=Counter32
_TeTunnelTransitions_Object=MibTableColumn
teTunnelTransitions=_TeTunnelTransitions_Object((1,3,6,1,2,1,122,1,2,1,19),_TeTunnelTransitions_Type())
teTunnelTransitions.setMaxAccess(_C)
if mibBuilder.loadTexts:teTunnelTransitions.setStatus(_B)
_TeTunnelLastTransition_Type=TimeTicks
_TeTunnelLastTransition_Object=MibTableColumn
teTunnelLastTransition=_TeTunnelLastTransition_Object((1,3,6,1,2,1,122,1,2,1,20),_TeTunnelLastTransition_Type())
teTunnelLastTransition.setMaxAccess(_C)
if mibBuilder.loadTexts:teTunnelLastTransition.setStatus(_B)
_TeTunnelPathChanges_Type=Counter32
_TeTunnelPathChanges_Object=MibTableColumn
teTunnelPathChanges=_TeTunnelPathChanges_Object((1,3,6,1,2,1,122,1,2,1,21),_TeTunnelPathChanges_Type())
teTunnelPathChanges.setMaxAccess(_C)
if mibBuilder.loadTexts:teTunnelPathChanges.setStatus(_B)
_TeTunnelLastPathChange_Type=TimeTicks
_TeTunnelLastPathChange_Object=MibTableColumn
teTunnelLastPathChange=_TeTunnelLastPathChange_Object((1,3,6,1,2,1,122,1,2,1,22),_TeTunnelLastPathChange_Type())
teTunnelLastPathChange.setMaxAccess(_C)
if mibBuilder.loadTexts:teTunnelLastPathChange.setStatus(_B)
_TeTunnelConfiguredPaths_Type=Gauge32
_TeTunnelConfiguredPaths_Object=MibTableColumn
teTunnelConfiguredPaths=_TeTunnelConfiguredPaths_Object((1,3,6,1,2,1,122,1,2,1,23),_TeTunnelConfiguredPaths_Type())
teTunnelConfiguredPaths.setMaxAccess(_C)
if mibBuilder.loadTexts:teTunnelConfiguredPaths.setStatus(_B)
_TeTunnelStandbyPaths_Type=Gauge32
_TeTunnelStandbyPaths_Object=MibTableColumn
teTunnelStandbyPaths=_TeTunnelStandbyPaths_Object((1,3,6,1,2,1,122,1,2,1,24),_TeTunnelStandbyPaths_Type())
teTunnelStandbyPaths.setMaxAccess(_C)
if mibBuilder.loadTexts:teTunnelStandbyPaths.setStatus(_B)
_TeTunnelOperationalPaths_Type=Gauge32
_TeTunnelOperationalPaths_Object=MibTableColumn
teTunnelOperationalPaths=_TeTunnelOperationalPaths_Object((1,3,6,1,2,1,122,1,2,1,25),_TeTunnelOperationalPaths_Type())
teTunnelOperationalPaths.setMaxAccess(_C)
if mibBuilder.loadTexts:teTunnelOperationalPaths.setStatus(_B)
_TePathTable_Object=MibTable
tePathTable=_TePathTable_Object((1,3,6,1,2,1,122,1,3))
if mibBuilder.loadTexts:tePathTable.setStatus(_B)
_TePathEntry_Object=MibTableRow
tePathEntry=_TePathEntry_Object((1,3,6,1,2,1,122,1,3,1))
tePathEntry.setIndexNames((0,_A,_O),(0,_A,_U))
if mibBuilder.loadTexts:tePathEntry.setStatus(_B)
class _TePathIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_TePathIndex_Type.__name__=_F
_TePathIndex_Object=MibTableColumn
tePathIndex=_TePathIndex_Object((1,3,6,1,2,1,122,1,3,1,1),_TePathIndex_Type())
tePathIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:tePathIndex.setStatus(_B)
class _TePathName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_TePathName_Type.__name__=_L
_TePathName_Object=MibTableColumn
tePathName=_TePathName_Object((1,3,6,1,2,1,122,1,3,1,2),_TePathName_Type())
tePathName.setMaxAccess(_D)
if mibBuilder.loadTexts:tePathName.setStatus(_B)
_TePathRowStatus_Type=RowStatus
_TePathRowStatus_Object=MibTableColumn
tePathRowStatus=_TePathRowStatus_Object((1,3,6,1,2,1,122,1,3,1,3),_TePathRowStatus_Type())
tePathRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:tePathRowStatus.setStatus(_B)
_TePathStorageType_Type=StorageType
_TePathStorageType_Object=MibTableColumn
tePathStorageType=_TePathStorageType_Object((1,3,6,1,2,1,122,1,3,1,4),_TePathStorageType_Type())
tePathStorageType.setMaxAccess(_D)
if mibBuilder.loadTexts:tePathStorageType.setStatus(_B)
class _TePathType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_N,1),('primary',2),('standby',3),('secondary',4)))
_TePathType_Type.__name__=_E
_TePathType_Object=MibTableColumn
tePathType=_TePathType_Object((1,3,6,1,2,1,122,1,3,1,5),_TePathType_Type())
tePathType.setMaxAccess(_D)
if mibBuilder.loadTexts:tePathType.setStatus(_B)
_TePathConfiguredRoute_Type=Unsigned32
_TePathConfiguredRoute_Object=MibTableColumn
tePathConfiguredRoute=_TePathConfiguredRoute_Object((1,3,6,1,2,1,122,1,3,1,6),_TePathConfiguredRoute_Type())
tePathConfiguredRoute.setMaxAccess(_D)
if mibBuilder.loadTexts:tePathConfiguredRoute.setStatus(_B)
class _TePathBandwidth_Type(MplsBitRate):defaultValue=0
_TePathBandwidth_Type.__name__=_R
_TePathBandwidth_Object=MibTableColumn
tePathBandwidth=_TePathBandwidth_Object((1,3,6,1,2,1,122,1,3,1,7),_TePathBandwidth_Type())
tePathBandwidth.setMaxAccess(_D)
if mibBuilder.loadTexts:tePathBandwidth.setStatus(_B)
if mibBuilder.loadTexts:tePathBandwidth.setUnits('Kilobits per second')
class _TePathIncludeAny_Type(Unsigned32):defaultValue=0
_TePathIncludeAny_Type.__name__=_F
_TePathIncludeAny_Object=MibTableColumn
tePathIncludeAny=_TePathIncludeAny_Object((1,3,6,1,2,1,122,1,3,1,8),_TePathIncludeAny_Type())
tePathIncludeAny.setMaxAccess(_D)
if mibBuilder.loadTexts:tePathIncludeAny.setStatus(_B)
class _TePathIncludeAll_Type(Unsigned32):defaultValue=0
_TePathIncludeAll_Type.__name__=_F
_TePathIncludeAll_Object=MibTableColumn
tePathIncludeAll=_TePathIncludeAll_Object((1,3,6,1,2,1,122,1,3,1,9),_TePathIncludeAll_Type())
tePathIncludeAll.setMaxAccess(_D)
if mibBuilder.loadTexts:tePathIncludeAll.setStatus(_B)
class _TePathExclude_Type(Unsigned32):defaultValue=0
_TePathExclude_Type.__name__=_F
_TePathExclude_Object=MibTableColumn
tePathExclude=_TePathExclude_Object((1,3,6,1,2,1,122,1,3,1,10),_TePathExclude_Type())
tePathExclude.setMaxAccess(_D)
if mibBuilder.loadTexts:tePathExclude.setStatus(_B)
class _TePathSetupPriority_Type(Integer32):defaultValue=7;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_TePathSetupPriority_Type.__name__=_E
_TePathSetupPriority_Object=MibTableColumn
tePathSetupPriority=_TePathSetupPriority_Object((1,3,6,1,2,1,122,1,3,1,11),_TePathSetupPriority_Type())
tePathSetupPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:tePathSetupPriority.setStatus(_B)
class _TePathHoldPriority_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_TePathHoldPriority_Type.__name__=_E
_TePathHoldPriority_Object=MibTableColumn
tePathHoldPriority=_TePathHoldPriority_Object((1,3,6,1,2,1,122,1,3,1,12),_TePathHoldPriority_Type())
tePathHoldPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:tePathHoldPriority.setStatus(_B)
class _TePathProperties_Type(Bits):namedValues=NamedValues(*(('recordRoute',0),('cspf',1),('makeBeforeBreak',2),('mergeable',3),('fastReroute',4),('protected',5)))
_TePathProperties_Type.__name__=_M
_TePathProperties_Object=MibTableColumn
tePathProperties=_TePathProperties_Object((1,3,6,1,2,1,122,1,3,1,13),_TePathProperties_Type())
tePathProperties.setMaxAccess(_D)
if mibBuilder.loadTexts:tePathProperties.setStatus(_B)
class _TePathOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*((_P,0),('down',1),(_Q,2),('dormant',3),('ready',4),('operational',5)))
_TePathOperStatus_Type.__name__=_E
_TePathOperStatus_Object=MibTableColumn
tePathOperStatus=_TePathOperStatus_Object((1,3,6,1,2,1,122,1,3,1,14),_TePathOperStatus_Type())
tePathOperStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:tePathOperStatus.setStatus(_B)
class _TePathAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('normal',1),(_Q,2)))
_TePathAdminStatus_Type.__name__=_E
_TePathAdminStatus_Object=MibTableColumn
tePathAdminStatus=_TePathAdminStatus_Object((1,3,6,1,2,1,122,1,3,1,15),_TePathAdminStatus_Type())
tePathAdminStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:tePathAdminStatus.setStatus(_B)
_TePathComputedRoute_Type=Unsigned32
_TePathComputedRoute_Object=MibTableColumn
tePathComputedRoute=_TePathComputedRoute_Object((1,3,6,1,2,1,122,1,3,1,16),_TePathComputedRoute_Type())
tePathComputedRoute.setMaxAccess(_C)
if mibBuilder.loadTexts:tePathComputedRoute.setStatus(_B)
_TePathRecordedRoute_Type=Unsigned32
_TePathRecordedRoute_Object=MibTableColumn
tePathRecordedRoute=_TePathRecordedRoute_Object((1,3,6,1,2,1,122,1,3,1,17),_TePathRecordedRoute_Type())
tePathRecordedRoute.setMaxAccess(_C)
if mibBuilder.loadTexts:tePathRecordedRoute.setStatus(_B)
_TePathHopTable_Object=MibTable
tePathHopTable=_TePathHopTable_Object((1,3,6,1,2,1,122,1,4))
if mibBuilder.loadTexts:tePathHopTable.setStatus(_B)
_TePathHopEntry_Object=MibTableRow
tePathHopEntry=_TePathHopEntry_Object((1,3,6,1,2,1,122,1,4,1))
tePathHopEntry.setIndexNames((0,_A,_V),(0,_A,_W))
if mibBuilder.loadTexts:tePathHopEntry.setStatus(_B)
class _TeHopListIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_TeHopListIndex_Type.__name__=_F
_TeHopListIndex_Object=MibTableColumn
teHopListIndex=_TeHopListIndex_Object((1,3,6,1,2,1,122,1,4,1,1),_TeHopListIndex_Type())
teHopListIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:teHopListIndex.setStatus(_B)
class _TePathHopIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_TePathHopIndex_Type.__name__=_F
_TePathHopIndex_Object=MibTableColumn
tePathHopIndex=_TePathHopIndex_Object((1,3,6,1,2,1,122,1,4,1,2),_TePathHopIndex_Type())
tePathHopIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:tePathHopIndex.setStatus(_B)
_TePathHopRowStatus_Type=RowStatus
_TePathHopRowStatus_Object=MibTableColumn
tePathHopRowStatus=_TePathHopRowStatus_Object((1,3,6,1,2,1,122,1,4,1,3),_TePathHopRowStatus_Type())
tePathHopRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:tePathHopRowStatus.setStatus(_B)
_TePathHopStorageType_Type=StorageType
_TePathHopStorageType_Object=MibTableColumn
tePathHopStorageType=_TePathHopStorageType_Object((1,3,6,1,2,1,122,1,4,1,4),_TePathHopStorageType_Type())
tePathHopStorageType.setMaxAccess(_D)
if mibBuilder.loadTexts:tePathHopStorageType.setStatus(_B)
_TePathHopAddrType_Type=TeHopAddressType
_TePathHopAddrType_Object=MibTableColumn
tePathHopAddrType=_TePathHopAddrType_Object((1,3,6,1,2,1,122,1,4,1,5),_TePathHopAddrType_Type())
tePathHopAddrType.setMaxAccess(_D)
if mibBuilder.loadTexts:tePathHopAddrType.setStatus(_B)
_TePathHopAddress_Type=TeHopAddress
_TePathHopAddress_Object=MibTableColumn
tePathHopAddress=_TePathHopAddress_Object((1,3,6,1,2,1,122,1,4,1,6),_TePathHopAddress_Type())
tePathHopAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:tePathHopAddress.setStatus(_B)
class _TePathHopType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_P,0),('loose',1),('strict',2)))
_TePathHopType_Type.__name__=_E
_TePathHopType_Object=MibTableColumn
tePathHopType=_TePathHopType_Object((1,3,6,1,2,1,122,1,4,1,7),_TePathHopType_Type())
tePathHopType.setMaxAccess(_C)
if mibBuilder.loadTexts:tePathHopType.setStatus(_B)
_TeMIBConformance_ObjectIdentity=ObjectIdentity
teMIBConformance=_TeMIBConformance_ObjectIdentity((1,3,6,1,2,1,122,2))
_TeGroups_ObjectIdentity=ObjectIdentity
teGroups=_TeGroups_ObjectIdentity((1,3,6,1,2,1,122,2,1))
_TeModuleCompliance_ObjectIdentity=ObjectIdentity
teModuleCompliance=_TeModuleCompliance_ObjectIdentity((1,3,6,1,2,1,122,2,2))
teTrafficEngineeringGroup=ObjectGroup((1,3,6,1,2,1,122,2,1,1))
teTrafficEngineeringGroup.setObjects(*((_A,_G),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_g),(_A,_h),(_A,_i),(_A,_j),(_A,_k),(_A,_l),(_A,_m),(_A,_n),(_A,_o),(_A,_p),(_A,_q),(_A,_r),(_A,_s),(_A,_t),(_A,_u),(_A,_v),(_A,_w),(_A,_x),(_A,_y),(_A,_z),(_A,_A0),(_A,_A1),(_A,_A2),(_A,_A3),(_A,_A4),(_A,_A5),(_A,_A6),(_A,_A7),(_A,_A8),(_A,_A9),(_A,_AA),(_A,_AB),(_A,_AC),(_A,_AD),(_A,_AE),(_A,_H),(_A,_AF),(_A,_AG),(_A,_AH),(_A,_AI),(_A,_AJ),(_A,_AK),(_A,_AL),(_A,_AM),(_A,_AN)))
if mibBuilder.loadTexts:teTrafficEngineeringGroup.setStatus(_B)
teTunnelUp=NotificationType((1,3,6,1,2,1,122,0,1))
teTunnelUp.setObjects(*((_A,_G),(_A,_H)))
if mibBuilder.loadTexts:teTunnelUp.setStatus(_B)
teTunnelDown=NotificationType((1,3,6,1,2,1,122,0,2))
teTunnelDown.setObjects(*((_A,_G),(_A,_H)))
if mibBuilder.loadTexts:teTunnelDown.setStatus(_B)
teTunnelChanged=NotificationType((1,3,6,1,2,1,122,0,3))
teTunnelChanged.setObjects(*((_A,_G),(_A,_H)))
if mibBuilder.loadTexts:teTunnelChanged.setStatus(_B)
teTunnelRerouted=NotificationType((1,3,6,1,2,1,122,0,4))
teTunnelRerouted.setObjects(*((_A,_G),(_A,_H)))
if mibBuilder.loadTexts:teTunnelRerouted.setStatus(_B)
teNotificationGroup=NotificationGroup((1,3,6,1,2,1,122,2,1,2))
teNotificationGroup.setObjects(*((_A,_AO),(_A,_AP),(_A,_AQ),(_A,_AR)))
if mibBuilder.loadTexts:teNotificationGroup.setStatus(_B)
teModuleReadOnlyCompliance=ModuleCompliance((1,3,6,1,2,1,122,2,2,1))
teModuleReadOnlyCompliance.setObjects(*((_A,_J),(_A,_K)))
if mibBuilder.loadTexts:teModuleReadOnlyCompliance.setStatus(_B)
teModuleFullCompliance=ModuleCompliance((1,3,6,1,2,1,122,2,2,2))
teModuleFullCompliance.setObjects(*((_A,_J),(_A,_K)))
if mibBuilder.loadTexts:teModuleFullCompliance.setStatus(_B)
teModuleServerReadOnlyCompliance=ModuleCompliance((1,3,6,1,2,1,122,2,2,3))
teModuleServerReadOnlyCompliance.setObjects(*((_A,_J),(_A,_K)))
if mibBuilder.loadTexts:teModuleServerReadOnlyCompliance.setStatus(_B)
teModuleServerFullCompliance=ModuleCompliance((1,3,6,1,2,1,122,2,2,4))
teModuleServerFullCompliance.setObjects(*((_A,_J),(_A,_K)))
if mibBuilder.loadTexts:teModuleServerFullCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'teMIB':teMIB,'teMIBNotifications':teMIBNotifications,_AO:teTunnelUp,_AP:teTunnelDown,_AQ:teTunnelChanged,_AR:teTunnelRerouted,'teMIBObjects':teMIBObjects,'teInfo':teInfo,_A5:teDistProtocol,_A6:teSignalingProto,_A7:teNotificationEnable,_A8:teNextTunnelIndex,_A9:teNextPathHopIndex,_AC:teConfiguredTunnels,_AD:teActiveTunnels,_AE:tePrimaryTunnels,'teAdminGroupTable':teAdminGroupTable,'teAdminGroupEntry':teAdminGroupEntry,_T:teAdminGroupNumber,_AA:teAdminGroupName,_AB:teAdminGroupRowStatus,'teTunnelTable':teTunnelTable,'teTunnelEntry':teTunnelEntry,_O:teTunnelIndex,_G:teTunnelName,_X:teTunnelNextPathIndex,_Y:teTunnelRowStatus,_Z:teTunnelStorageType,_a:teTunnelSourceAddressType,_b:teTunnelSourceAddress,_c:teTunnelDestinationAddressType,_d:teTunnelDestinationAddress,_e:teTunnelState,_f:teTunnelDiscontinuityTimer,_g:teTunnelOctets,_h:teTunnelPackets,_i:teTunnelLPOctets,_j:teTunnelLPPackets,_k:teTunnelAge,_l:teTunnelTimeUp,_m:teTunnelPrimaryTimeUp,_n:teTunnelTransitions,_o:teTunnelLastTransition,_p:teTunnelPathChanges,_q:teTunnelLastPathChange,_r:teTunnelConfiguredPaths,_s:teTunnelStandbyPaths,_t:teTunnelOperationalPaths,'tePathTable':tePathTable,'tePathEntry':tePathEntry,_U:tePathIndex,_H:tePathName,_AG:tePathRowStatus,_AH:tePathStorageType,_AF:tePathType,_AI:tePathConfiguredRoute,_u:tePathBandwidth,_v:tePathIncludeAny,_w:tePathIncludeAll,_x:tePathExclude,_y:tePathSetupPriority,_z:tePathHoldPriority,_A0:tePathProperties,_A1:tePathOperStatus,_A2:tePathAdminStatus,_A3:tePathComputedRoute,_A4:tePathRecordedRoute,'tePathHopTable':tePathHopTable,'tePathHopEntry':tePathHopEntry,_V:teHopListIndex,_W:tePathHopIndex,_AJ:tePathHopRowStatus,_AK:tePathHopStorageType,_AL:tePathHopAddrType,_AM:tePathHopAddress,_AN:tePathHopType,'teMIBConformance':teMIBConformance,'teGroups':teGroups,_J:teTrafficEngineeringGroup,_K:teNotificationGroup,'teModuleCompliance':teModuleCompliance,'teModuleReadOnlyCompliance':teModuleReadOnlyCompliance,'teModuleFullCompliance':teModuleFullCompliance,'teModuleServerReadOnlyCompliance':teModuleServerReadOnlyCompliance,'teModuleServerFullCompliance':teModuleServerFullCompliance})