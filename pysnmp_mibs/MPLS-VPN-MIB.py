_Ai='mplsVpnVrfRouteTargetGroup'
_Ah='mplsVpnVrfBgpNbrGroup'
_Ag='mplsVpnVrfRouteGroup'
_Af='mplsVpnPerfGroup'
_Ae='mplsVpnInterfaceGroup'
_Ad='mplsVpnVrfGroup'
_Ac='mplsVpnScalarGroup'
_Ab='mplsNumVrfSecIllegalLabelThreshExceeded'
_Aa='mplsNumVrfRouteMaxThreshExceeded'
_AZ='mplsNumVrfRouteMidThreshExceeded'
_AY='mplsVrfIfDown'
_AX='mplsVrfIfUp'
_AW='mplsVpnVrfRouteTargetRowStatus'
_AV='mplsVpnVrfRouteTargetDescr'
_AU='mplsVpnVrfRouteTarget'
_AT='mplsVpnVrfRouteStorageType'
_AS='mplsVpnVrfRouteRowStatus'
_AR='mplsVpnVrfRouteMetric5'
_AQ='mplsVpnVrfRouteMetric4'
_AP='mplsVpnVrfRouteMetric3'
_AO='mplsVpnVrfRouteMetric2'
_AN='mplsVpnVrfRouteMetric1'
_AM='mplsVpnVrfRouteNextHopAS'
_AL='mplsVpnVrfRouteInfo'
_AK='mplsVpnVrfRouteAge'
_AJ='mplsVpnVrfRouteProto'
_AI='mplsVpnVrfRouteType'
_AH='mplsVpnVrfRouteIfIndex'
_AG='mplsVpnVrfRouteNextHopAddrType'
_AF='mplsVpnVrfRouteMaskAddrType'
_AE='mplsVpnVrfRouteDestAddrType'
_AD='mplsVpnVrfSecIllegalLabelRcvThresh'
_AC='mplsVpnVrfSecIllegalLabelViolations'
_AB='mplsVpnVrfBgpPathAttrUnknown'
_AA='mplsVpnVrfBgpPathAttrBest'
_A9='mplsVpnVrfBgpPathAttrCalcLocalPref'
_A8='mplsVpnVrfBgpPathAttrAggregatorAddr'
_A7='mplsVpnVrfBgpPathAttrAggregatorAS'
_A6='mplsVpnVrfBgpPathAttrAtomicAggregate'
_A5='mplsVpnVrfBgpPathAttrLocalPref'
_A4='mplsVpnVrfBgpPathAttrMultiExitDisc'
_A3='mplsVpnVrfBgpPathAttrNextHop'
_A2='mplsVpnVrfBgpPathAttrASPathSegment'
_A1='mplsVpnVrfBgpPathAttrOrigin'
_A0='mplsVpnVrfBgpNbrStorageType'
_z='mplsVpnVrfBgpNbrRowStatus'
_y='mplsVpnVrfBgpNbrAddr'
_x='mplsVpnVrfBgpNbrType'
_w='mplsVpnVrfBgpNbrRole'
_v='mplsVpnVrfPerfCurrNumRoutes'
_u='mplsVpnVrfPerfRoutesDeleted'
_t='mplsVpnVrfPerfRoutesAdded'
_s='mplsVpnInterfaceConfRowStatus'
_r='mplsVpnInterfaceConfStorageType'
_q='mplsVpnInterfaceVpnRouteDistProtocol'
_p='mplsVpnInterfaceVpnClassification'
_o='mplsVpnInterfaceLabelEdgeType'
_n='mplsVpnVrfConfStorageType'
_m='mplsVpnVrfConfRowStatus'
_l='mplsVpnVrfConfLastChanged'
_k='mplsVpnVrfConfMaxRoutes'
_j='mplsVpnVrfConfHighRouteThreshold'
_i='mplsVpnVrfConfMidRouteThreshold'
_h='mplsVpnVrfAssociatedInterfaces'
_g='mplsVpnVrfActiveInterfaces'
_f='mplsVpnVrfOperStatus'
_e='mplsVpnVrfCreationTime'
_d='mplsVpnVrfRouteDistinguisher'
_c='mplsVpnVrfDescription'
_b='mplsVpnVrfConfMaxPossibleRoutes'
_a='mplsVpnNotificationEnable'
_Z='mplsVpnConnectedInterfaces'
_Y='mplsVpnActiveVrfs'
_X='mplsVpnConfiguredVrfs'
_W='mplsVpnVrfPerfEntry'
_V='mplsVpnVrfSecEntry'
_U='mplsVpnVrfRouteNextHop'
_T='mplsVpnVrfRouteTos'
_S='mplsVpnVrfRouteMask'
_R='mplsVpnVrfRouteDest'
_Q='mplsVpnVrfBgpPathAttrPeer'
_P='mplsVpnVrfBgpPathAttrIpAddrPrefixLen'
_O='mplsVpnVrfBgpPathAttrIpAddrPrefix'
_N='mplsVpnVrfBgpNbrIndex'
_M='mplsVpnVrfRouteTargetType'
_L='mplsVpnVrfRouteTargetIndex'
_K='TruthValue'
_J='other'
_I='mplsVpnInterfaceConfIndex'
_H='OctetString'
_G='mplsVpnVrfName'
_F='not-accessible'
_E='Integer32'
_D='read-only'
_C='read-create'
_B='MPLS-VPN-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_H,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,experimental,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','experimental','iso')
DisplayString,PhysAddress,RowStatus,StorageType,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','StorageType','TextualConvention','TimeStamp',_K)
mplsVpnMIB=ModuleIdentity((1,3,6,1,3,118))
if mibBuilder.loadTexts:mplsVpnMIB.setRevisions(('2001-10-15 12:00','2001-10-05 12:00','2001-07-17 12:00','2001-07-10 12:00','2001-06-19 12:00','2001-05-30 12:00','2000-09-30 12:00'))
class MplsVpnId(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
class MplsVpnRouteDistinguisher(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,256))
_MplsVpnNotifications_ObjectIdentity=ObjectIdentity
mplsVpnNotifications=_MplsVpnNotifications_ObjectIdentity((1,3,6,1,3,118,0))
_MplsVpnObjects_ObjectIdentity=ObjectIdentity
mplsVpnObjects=_MplsVpnObjects_ObjectIdentity((1,3,6,1,3,118,1))
_MplsVpnScalars_ObjectIdentity=ObjectIdentity
mplsVpnScalars=_MplsVpnScalars_ObjectIdentity((1,3,6,1,3,118,1,1))
_MplsVpnConfiguredVrfs_Type=Unsigned32
_MplsVpnConfiguredVrfs_Object=MibScalar
mplsVpnConfiguredVrfs=_MplsVpnConfiguredVrfs_Object((1,3,6,1,3,118,1,1,1),_MplsVpnConfiguredVrfs_Type())
mplsVpnConfiguredVrfs.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsVpnConfiguredVrfs.setStatus(_A)
_MplsVpnActiveVrfs_Type=Unsigned32
_MplsVpnActiveVrfs_Object=MibScalar
mplsVpnActiveVrfs=_MplsVpnActiveVrfs_Object((1,3,6,1,3,118,1,1,2),_MplsVpnActiveVrfs_Type())
mplsVpnActiveVrfs.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsVpnActiveVrfs.setStatus(_A)
_MplsVpnConnectedInterfaces_Type=Unsigned32
_MplsVpnConnectedInterfaces_Object=MibScalar
mplsVpnConnectedInterfaces=_MplsVpnConnectedInterfaces_Object((1,3,6,1,3,118,1,1,3),_MplsVpnConnectedInterfaces_Type())
mplsVpnConnectedInterfaces.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsVpnConnectedInterfaces.setStatus(_A)
class _MplsVpnNotificationEnable_Type(TruthValue):defaultValue=2
_MplsVpnNotificationEnable_Type.__name__=_K
_MplsVpnNotificationEnable_Object=MibScalar
mplsVpnNotificationEnable=_MplsVpnNotificationEnable_Object((1,3,6,1,3,118,1,1,4),_MplsVpnNotificationEnable_Type())
mplsVpnNotificationEnable.setMaxAccess('read-write')
if mibBuilder.loadTexts:mplsVpnNotificationEnable.setStatus(_A)
_MplsVpnVrfConfMaxPossibleRoutes_Type=Unsigned32
_MplsVpnVrfConfMaxPossibleRoutes_Object=MibScalar
mplsVpnVrfConfMaxPossibleRoutes=_MplsVpnVrfConfMaxPossibleRoutes_Object((1,3,6,1,3,118,1,1,5),_MplsVpnVrfConfMaxPossibleRoutes_Type())
mplsVpnVrfConfMaxPossibleRoutes.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsVpnVrfConfMaxPossibleRoutes.setStatus(_A)
_MplsVpnConf_ObjectIdentity=ObjectIdentity
mplsVpnConf=_MplsVpnConf_ObjectIdentity((1,3,6,1,3,118,1,2))
_MplsVpnInterfaceConfTable_Object=MibTable
mplsVpnInterfaceConfTable=_MplsVpnInterfaceConfTable_Object((1,3,6,1,3,118,1,2,1))
if mibBuilder.loadTexts:mplsVpnInterfaceConfTable.setStatus(_A)
_MplsVpnInterfaceConfEntry_Object=MibTableRow
mplsVpnInterfaceConfEntry=_MplsVpnInterfaceConfEntry_Object((1,3,6,1,3,118,1,2,1,1))
mplsVpnInterfaceConfEntry.setIndexNames((0,_B,_G),(0,_B,_I))
if mibBuilder.loadTexts:mplsVpnInterfaceConfEntry.setStatus(_A)
_MplsVpnInterfaceConfIndex_Type=InterfaceIndex
_MplsVpnInterfaceConfIndex_Object=MibTableColumn
mplsVpnInterfaceConfIndex=_MplsVpnInterfaceConfIndex_Object((1,3,6,1,3,118,1,2,1,1,1),_MplsVpnInterfaceConfIndex_Type())
mplsVpnInterfaceConfIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:mplsVpnInterfaceConfIndex.setStatus(_A)
class _MplsVpnInterfaceLabelEdgeType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('providerEdge',1),('customerEdge',2)))
_MplsVpnInterfaceLabelEdgeType_Type.__name__=_E
_MplsVpnInterfaceLabelEdgeType_Object=MibTableColumn
mplsVpnInterfaceLabelEdgeType=_MplsVpnInterfaceLabelEdgeType_Object((1,3,6,1,3,118,1,2,1,1,2),_MplsVpnInterfaceLabelEdgeType_Type())
mplsVpnInterfaceLabelEdgeType.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsVpnInterfaceLabelEdgeType.setStatus(_A)
class _MplsVpnInterfaceVpnClassification_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('carrierOfCarrier',1),('enterprise',2),('interProvider',3)))
_MplsVpnInterfaceVpnClassification_Type.__name__=_E
_MplsVpnInterfaceVpnClassification_Object=MibTableColumn
mplsVpnInterfaceVpnClassification=_MplsVpnInterfaceVpnClassification_Object((1,3,6,1,3,118,1,2,1,1,3),_MplsVpnInterfaceVpnClassification_Type())
mplsVpnInterfaceVpnClassification.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsVpnInterfaceVpnClassification.setStatus(_A)
class _MplsVpnInterfaceVpnRouteDistProtocol_Type(Bits):namedValues=NamedValues(*(('dummy',0),('none',1),('bgp',2),('ospf',3),('rip',4),('isis',5),(_J,6)))
_MplsVpnInterfaceVpnRouteDistProtocol_Type.__name__='Bits'
_MplsVpnInterfaceVpnRouteDistProtocol_Object=MibTableColumn
mplsVpnInterfaceVpnRouteDistProtocol=_MplsVpnInterfaceVpnRouteDistProtocol_Object((1,3,6,1,3,118,1,2,1,1,4),_MplsVpnInterfaceVpnRouteDistProtocol_Type())
mplsVpnInterfaceVpnRouteDistProtocol.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsVpnInterfaceVpnRouteDistProtocol.setStatus(_A)
_MplsVpnInterfaceConfStorageType_Type=StorageType
_MplsVpnInterfaceConfStorageType_Object=MibTableColumn
mplsVpnInterfaceConfStorageType=_MplsVpnInterfaceConfStorageType_Object((1,3,6,1,3,118,1,2,1,1,5),_MplsVpnInterfaceConfStorageType_Type())
mplsVpnInterfaceConfStorageType.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsVpnInterfaceConfStorageType.setStatus(_A)
_MplsVpnInterfaceConfRowStatus_Type=RowStatus
_MplsVpnInterfaceConfRowStatus_Object=MibTableColumn
mplsVpnInterfaceConfRowStatus=_MplsVpnInterfaceConfRowStatus_Object((1,3,6,1,3,118,1,2,1,1,6),_MplsVpnInterfaceConfRowStatus_Type())
mplsVpnInterfaceConfRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsVpnInterfaceConfRowStatus.setStatus(_A)
_MplsVpnVrfTable_Object=MibTable
mplsVpnVrfTable=_MplsVpnVrfTable_Object((1,3,6,1,3,118,1,2,2))
if mibBuilder.loadTexts:mplsVpnVrfTable.setStatus(_A)
_MplsVpnVrfEntry_Object=MibTableRow
mplsVpnVrfEntry=_MplsVpnVrfEntry_Object((1,3,6,1,3,118,1,2,2,1))
mplsVpnVrfEntry.setIndexNames((0,_B,_G))
if mibBuilder.loadTexts:mplsVpnVrfEntry.setStatus(_A)
_MplsVpnVrfName_Type=MplsVpnId
_MplsVpnVrfName_Object=MibTableColumn
mplsVpnVrfName=_MplsVpnVrfName_Object((1,3,6,1,3,118,1,2,2,1,1),_MplsVpnVrfName_Type())
mplsVpnVrfName.setMaxAccess(_F)
if mibBuilder.loadTexts:mplsVpnVrfName.setStatus(_A)
_MplsVpnVrfDescription_Type=SnmpAdminString
_MplsVpnVrfDescription_Object=MibTableColumn
mplsVpnVrfDescription=_MplsVpnVrfDescription_Object((1,3,6,1,3,118,1,2,2,1,2),_MplsVpnVrfDescription_Type())
mplsVpnVrfDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsVpnVrfDescription.setStatus(_A)
_MplsVpnVrfRouteDistinguisher_Type=MplsVpnRouteDistinguisher
_MplsVpnVrfRouteDistinguisher_Object=MibTableColumn
mplsVpnVrfRouteDistinguisher=_MplsVpnVrfRouteDistinguisher_Object((1,3,6,1,3,118,1,2,2,1,3),_MplsVpnVrfRouteDistinguisher_Type())
mplsVpnVrfRouteDistinguisher.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsVpnVrfRouteDistinguisher.setStatus(_A)
_MplsVpnVrfCreationTime_Type=TimeStamp
_MplsVpnVrfCreationTime_Object=MibTableColumn
mplsVpnVrfCreationTime=_MplsVpnVrfCreationTime_Object((1,3,6,1,3,118,1,2,2,1,4),_MplsVpnVrfCreationTime_Type())
mplsVpnVrfCreationTime.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsVpnVrfCreationTime.setStatus(_A)
class _MplsVpnVrfOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('up',1),('down',2)))
_MplsVpnVrfOperStatus_Type.__name__=_E
_MplsVpnVrfOperStatus_Object=MibTableColumn
mplsVpnVrfOperStatus=_MplsVpnVrfOperStatus_Object((1,3,6,1,3,118,1,2,2,1,5),_MplsVpnVrfOperStatus_Type())
mplsVpnVrfOperStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsVpnVrfOperStatus.setStatus(_A)
_MplsVpnVrfActiveInterfaces_Type=Unsigned32
_MplsVpnVrfActiveInterfaces_Object=MibTableColumn
mplsVpnVrfActiveInterfaces=_MplsVpnVrfActiveInterfaces_Object((1,3,6,1,3,118,1,2,2,1,6),_MplsVpnVrfActiveInterfaces_Type())
mplsVpnVrfActiveInterfaces.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsVpnVrfActiveInterfaces.setStatus(_A)
_MplsVpnVrfAssociatedInterfaces_Type=Unsigned32
_MplsVpnVrfAssociatedInterfaces_Object=MibTableColumn
mplsVpnVrfAssociatedInterfaces=_MplsVpnVrfAssociatedInterfaces_Object((1,3,6,1,3,118,1,2,2,1,7),_MplsVpnVrfAssociatedInterfaces_Type())
mplsVpnVrfAssociatedInterfaces.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsVpnVrfAssociatedInterfaces.setStatus(_A)
_MplsVpnVrfConfMidRouteThreshold_Type=Unsigned32
_MplsVpnVrfConfMidRouteThreshold_Object=MibTableColumn
mplsVpnVrfConfMidRouteThreshold=_MplsVpnVrfConfMidRouteThreshold_Object((1,3,6,1,3,118,1,2,2,1,8),_MplsVpnVrfConfMidRouteThreshold_Type())
mplsVpnVrfConfMidRouteThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsVpnVrfConfMidRouteThreshold.setStatus(_A)
_MplsVpnVrfConfHighRouteThreshold_Type=Unsigned32
_MplsVpnVrfConfHighRouteThreshold_Object=MibTableColumn
mplsVpnVrfConfHighRouteThreshold=_MplsVpnVrfConfHighRouteThreshold_Object((1,3,6,1,3,118,1,2,2,1,9),_MplsVpnVrfConfHighRouteThreshold_Type())
mplsVpnVrfConfHighRouteThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsVpnVrfConfHighRouteThreshold.setStatus(_A)
_MplsVpnVrfConfMaxRoutes_Type=Unsigned32
_MplsVpnVrfConfMaxRoutes_Object=MibTableColumn
mplsVpnVrfConfMaxRoutes=_MplsVpnVrfConfMaxRoutes_Object((1,3,6,1,3,118,1,2,2,1,10),_MplsVpnVrfConfMaxRoutes_Type())
mplsVpnVrfConfMaxRoutes.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsVpnVrfConfMaxRoutes.setStatus(_A)
_MplsVpnVrfConfLastChanged_Type=TimeStamp
_MplsVpnVrfConfLastChanged_Object=MibTableColumn
mplsVpnVrfConfLastChanged=_MplsVpnVrfConfLastChanged_Object((1,3,6,1,3,118,1,2,2,1,11),_MplsVpnVrfConfLastChanged_Type())
mplsVpnVrfConfLastChanged.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsVpnVrfConfLastChanged.setStatus(_A)
_MplsVpnVrfConfRowStatus_Type=RowStatus
_MplsVpnVrfConfRowStatus_Object=MibTableColumn
mplsVpnVrfConfRowStatus=_MplsVpnVrfConfRowStatus_Object((1,3,6,1,3,118,1,2,2,1,12),_MplsVpnVrfConfRowStatus_Type())
mplsVpnVrfConfRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsVpnVrfConfRowStatus.setStatus(_A)
_MplsVpnVrfConfStorageType_Type=StorageType
_MplsVpnVrfConfStorageType_Object=MibTableColumn
mplsVpnVrfConfStorageType=_MplsVpnVrfConfStorageType_Object((1,3,6,1,3,118,1,2,2,1,13),_MplsVpnVrfConfStorageType_Type())
mplsVpnVrfConfStorageType.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsVpnVrfConfStorageType.setStatus(_A)
_MplsVpnVrfRouteTargetTable_Object=MibTable
mplsVpnVrfRouteTargetTable=_MplsVpnVrfRouteTargetTable_Object((1,3,6,1,3,118,1,2,3))
if mibBuilder.loadTexts:mplsVpnVrfRouteTargetTable.setStatus(_A)
_MplsVpnVrfRouteTargetEntry_Object=MibTableRow
mplsVpnVrfRouteTargetEntry=_MplsVpnVrfRouteTargetEntry_Object((1,3,6,1,3,118,1,2,3,1))
mplsVpnVrfRouteTargetEntry.setIndexNames((0,_B,_G),(0,_B,_L),(0,_B,_M))
if mibBuilder.loadTexts:mplsVpnVrfRouteTargetEntry.setStatus(_A)
_MplsVpnVrfRouteTargetIndex_Type=Unsigned32
_MplsVpnVrfRouteTargetIndex_Object=MibTableColumn
mplsVpnVrfRouteTargetIndex=_MplsVpnVrfRouteTargetIndex_Object((1,3,6,1,3,118,1,2,3,1,2),_MplsVpnVrfRouteTargetIndex_Type())
mplsVpnVrfRouteTargetIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:mplsVpnVrfRouteTargetIndex.setStatus(_A)
class _MplsVpnVrfRouteTargetType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('import',1),('export',2),('both',3)))
_MplsVpnVrfRouteTargetType_Type.__name__=_E
_MplsVpnVrfRouteTargetType_Object=MibTableColumn
mplsVpnVrfRouteTargetType=_MplsVpnVrfRouteTargetType_Object((1,3,6,1,3,118,1,2,3,1,3),_MplsVpnVrfRouteTargetType_Type())
mplsVpnVrfRouteTargetType.setMaxAccess(_F)
if mibBuilder.loadTexts:mplsVpnVrfRouteTargetType.setStatus(_A)
_MplsVpnVrfRouteTarget_Type=MplsVpnRouteDistinguisher
_MplsVpnVrfRouteTarget_Object=MibTableColumn
mplsVpnVrfRouteTarget=_MplsVpnVrfRouteTarget_Object((1,3,6,1,3,118,1,2,3,1,4),_MplsVpnVrfRouteTarget_Type())
mplsVpnVrfRouteTarget.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsVpnVrfRouteTarget.setStatus(_A)
_MplsVpnVrfRouteTargetDescr_Type=DisplayString
_MplsVpnVrfRouteTargetDescr_Object=MibTableColumn
mplsVpnVrfRouteTargetDescr=_MplsVpnVrfRouteTargetDescr_Object((1,3,6,1,3,118,1,2,3,1,5),_MplsVpnVrfRouteTargetDescr_Type())
mplsVpnVrfRouteTargetDescr.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsVpnVrfRouteTargetDescr.setStatus(_A)
_MplsVpnVrfRouteTargetRowStatus_Type=RowStatus
_MplsVpnVrfRouteTargetRowStatus_Object=MibTableColumn
mplsVpnVrfRouteTargetRowStatus=_MplsVpnVrfRouteTargetRowStatus_Object((1,3,6,1,3,118,1,2,3,1,6),_MplsVpnVrfRouteTargetRowStatus_Type())
mplsVpnVrfRouteTargetRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsVpnVrfRouteTargetRowStatus.setStatus(_A)
_MplsVpnVrfBgpNbrAddrTable_Object=MibTable
mplsVpnVrfBgpNbrAddrTable=_MplsVpnVrfBgpNbrAddrTable_Object((1,3,6,1,3,118,1,2,4))
if mibBuilder.loadTexts:mplsVpnVrfBgpNbrAddrTable.setStatus(_A)
_MplsVpnVrfBgpNbrAddrEntry_Object=MibTableRow
mplsVpnVrfBgpNbrAddrEntry=_MplsVpnVrfBgpNbrAddrEntry_Object((1,3,6,1,3,118,1,2,4,1))
mplsVpnVrfBgpNbrAddrEntry.setIndexNames((0,_B,_G),(0,_B,_I),(0,_B,_N))
if mibBuilder.loadTexts:mplsVpnVrfBgpNbrAddrEntry.setStatus(_A)
_MplsVpnVrfBgpNbrIndex_Type=Unsigned32
_MplsVpnVrfBgpNbrIndex_Object=MibTableColumn
mplsVpnVrfBgpNbrIndex=_MplsVpnVrfBgpNbrIndex_Object((1,3,6,1,3,118,1,2,4,1,1),_MplsVpnVrfBgpNbrIndex_Type())
mplsVpnVrfBgpNbrIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:mplsVpnVrfBgpNbrIndex.setStatus(_A)
class _MplsVpnVrfBgpNbrRole_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('ce',1),('pe',2)))
_MplsVpnVrfBgpNbrRole_Type.__name__=_E
_MplsVpnVrfBgpNbrRole_Object=MibTableColumn
mplsVpnVrfBgpNbrRole=_MplsVpnVrfBgpNbrRole_Object((1,3,6,1,3,118,1,2,4,1,2),_MplsVpnVrfBgpNbrRole_Type())
mplsVpnVrfBgpNbrRole.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsVpnVrfBgpNbrRole.setStatus(_A)
_MplsVpnVrfBgpNbrType_Type=InetAddressType
_MplsVpnVrfBgpNbrType_Object=MibTableColumn
mplsVpnVrfBgpNbrType=_MplsVpnVrfBgpNbrType_Object((1,3,6,1,3,118,1,2,4,1,3),_MplsVpnVrfBgpNbrType_Type())
mplsVpnVrfBgpNbrType.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsVpnVrfBgpNbrType.setStatus(_A)
_MplsVpnVrfBgpNbrAddr_Type=InetAddress
_MplsVpnVrfBgpNbrAddr_Object=MibTableColumn
mplsVpnVrfBgpNbrAddr=_MplsVpnVrfBgpNbrAddr_Object((1,3,6,1,3,118,1,2,4,1,4),_MplsVpnVrfBgpNbrAddr_Type())
mplsVpnVrfBgpNbrAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsVpnVrfBgpNbrAddr.setStatus(_A)
_MplsVpnVrfBgpNbrRowStatus_Type=RowStatus
_MplsVpnVrfBgpNbrRowStatus_Object=MibTableColumn
mplsVpnVrfBgpNbrRowStatus=_MplsVpnVrfBgpNbrRowStatus_Object((1,3,6,1,3,118,1,2,4,1,5),_MplsVpnVrfBgpNbrRowStatus_Type())
mplsVpnVrfBgpNbrRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsVpnVrfBgpNbrRowStatus.setStatus(_A)
_MplsVpnVrfBgpNbrStorageType_Type=StorageType
_MplsVpnVrfBgpNbrStorageType_Object=MibTableColumn
mplsVpnVrfBgpNbrStorageType=_MplsVpnVrfBgpNbrStorageType_Object((1,3,6,1,3,118,1,2,4,1,6),_MplsVpnVrfBgpNbrStorageType_Type())
mplsVpnVrfBgpNbrStorageType.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsVpnVrfBgpNbrStorageType.setStatus(_A)
_MplsVpnVrfBgpNbrPrefixTable_Object=MibTable
mplsVpnVrfBgpNbrPrefixTable=_MplsVpnVrfBgpNbrPrefixTable_Object((1,3,6,1,3,118,1,2,5))
if mibBuilder.loadTexts:mplsVpnVrfBgpNbrPrefixTable.setStatus(_A)
_MplsVpnVrfBgpNbrPrefixEntry_Object=MibTableRow
mplsVpnVrfBgpNbrPrefixEntry=_MplsVpnVrfBgpNbrPrefixEntry_Object((1,3,6,1,3,118,1,2,5,1))
mplsVpnVrfBgpNbrPrefixEntry.setIndexNames((0,_B,_G),(0,_B,_O),(0,_B,_P),(0,_B,_Q))
if mibBuilder.loadTexts:mplsVpnVrfBgpNbrPrefixEntry.setStatus(_A)
_MplsVpnVrfBgpPathAttrPeer_Type=InetAddress
_MplsVpnVrfBgpPathAttrPeer_Object=MibTableColumn
mplsVpnVrfBgpPathAttrPeer=_MplsVpnVrfBgpPathAttrPeer_Object((1,3,6,1,3,118,1,2,5,1,1),_MplsVpnVrfBgpPathAttrPeer_Type())
mplsVpnVrfBgpPathAttrPeer.setMaxAccess(_F)
if mibBuilder.loadTexts:mplsVpnVrfBgpPathAttrPeer.setStatus(_A)
class _MplsVpnVrfBgpPathAttrIpAddrPrefixLen_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,32))
_MplsVpnVrfBgpPathAttrIpAddrPrefixLen_Type.__name__=_E
_MplsVpnVrfBgpPathAttrIpAddrPrefixLen_Object=MibTableColumn
mplsVpnVrfBgpPathAttrIpAddrPrefixLen=_MplsVpnVrfBgpPathAttrIpAddrPrefixLen_Object((1,3,6,1,3,118,1,2,5,1,2),_MplsVpnVrfBgpPathAttrIpAddrPrefixLen_Type())
mplsVpnVrfBgpPathAttrIpAddrPrefixLen.setMaxAccess(_F)
if mibBuilder.loadTexts:mplsVpnVrfBgpPathAttrIpAddrPrefixLen.setStatus(_A)
_MplsVpnVrfBgpPathAttrIpAddrPrefix_Type=InetAddress
_MplsVpnVrfBgpPathAttrIpAddrPrefix_Object=MibTableColumn
mplsVpnVrfBgpPathAttrIpAddrPrefix=_MplsVpnVrfBgpPathAttrIpAddrPrefix_Object((1,3,6,1,3,118,1,2,5,1,3),_MplsVpnVrfBgpPathAttrIpAddrPrefix_Type())
mplsVpnVrfBgpPathAttrIpAddrPrefix.setMaxAccess(_F)
if mibBuilder.loadTexts:mplsVpnVrfBgpPathAttrIpAddrPrefix.setStatus(_A)
class _MplsVpnVrfBgpPathAttrOrigin_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('igp',1),('egp',2),('incomplete',3)))
_MplsVpnVrfBgpPathAttrOrigin_Type.__name__=_E
_MplsVpnVrfBgpPathAttrOrigin_Object=MibTableColumn
mplsVpnVrfBgpPathAttrOrigin=_MplsVpnVrfBgpPathAttrOrigin_Object((1,3,6,1,3,118,1,2,5,1,4),_MplsVpnVrfBgpPathAttrOrigin_Type())
mplsVpnVrfBgpPathAttrOrigin.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsVpnVrfBgpPathAttrOrigin.setStatus(_A)
class _MplsVpnVrfBgpPathAttrASPathSegment_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,255))
_MplsVpnVrfBgpPathAttrASPathSegment_Type.__name__=_H
_MplsVpnVrfBgpPathAttrASPathSegment_Object=MibTableColumn
mplsVpnVrfBgpPathAttrASPathSegment=_MplsVpnVrfBgpPathAttrASPathSegment_Object((1,3,6,1,3,118,1,2,5,1,5),_MplsVpnVrfBgpPathAttrASPathSegment_Type())
mplsVpnVrfBgpPathAttrASPathSegment.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsVpnVrfBgpPathAttrASPathSegment.setStatus(_A)
_MplsVpnVrfBgpPathAttrNextHop_Type=InetAddress
_MplsVpnVrfBgpPathAttrNextHop_Object=MibTableColumn
mplsVpnVrfBgpPathAttrNextHop=_MplsVpnVrfBgpPathAttrNextHop_Object((1,3,6,1,3,118,1,2,5,1,6),_MplsVpnVrfBgpPathAttrNextHop_Type())
mplsVpnVrfBgpPathAttrNextHop.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsVpnVrfBgpPathAttrNextHop.setStatus(_A)
class _MplsVpnVrfBgpPathAttrMultiExitDisc_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,2147483647))
_MplsVpnVrfBgpPathAttrMultiExitDisc_Type.__name__=_E
_MplsVpnVrfBgpPathAttrMultiExitDisc_Object=MibTableColumn
mplsVpnVrfBgpPathAttrMultiExitDisc=_MplsVpnVrfBgpPathAttrMultiExitDisc_Object((1,3,6,1,3,118,1,2,5,1,7),_MplsVpnVrfBgpPathAttrMultiExitDisc_Type())
mplsVpnVrfBgpPathAttrMultiExitDisc.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsVpnVrfBgpPathAttrMultiExitDisc.setStatus(_A)
class _MplsVpnVrfBgpPathAttrLocalPref_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,2147483647))
_MplsVpnVrfBgpPathAttrLocalPref_Type.__name__=_E
_MplsVpnVrfBgpPathAttrLocalPref_Object=MibTableColumn
mplsVpnVrfBgpPathAttrLocalPref=_MplsVpnVrfBgpPathAttrLocalPref_Object((1,3,6,1,3,118,1,2,5,1,8),_MplsVpnVrfBgpPathAttrLocalPref_Type())
mplsVpnVrfBgpPathAttrLocalPref.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsVpnVrfBgpPathAttrLocalPref.setStatus(_A)
class _MplsVpnVrfBgpPathAttrAtomicAggregate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('lessSpecificRrouteNotSelected',1),('lessSpecificRouteSelected',2)))
_MplsVpnVrfBgpPathAttrAtomicAggregate_Type.__name__=_E
_MplsVpnVrfBgpPathAttrAtomicAggregate_Object=MibTableColumn
mplsVpnVrfBgpPathAttrAtomicAggregate=_MplsVpnVrfBgpPathAttrAtomicAggregate_Object((1,3,6,1,3,118,1,2,5,1,9),_MplsVpnVrfBgpPathAttrAtomicAggregate_Type())
mplsVpnVrfBgpPathAttrAtomicAggregate.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsVpnVrfBgpPathAttrAtomicAggregate.setStatus(_A)
class _MplsVpnVrfBgpPathAttrAggregatorAS_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_MplsVpnVrfBgpPathAttrAggregatorAS_Type.__name__=_E
_MplsVpnVrfBgpPathAttrAggregatorAS_Object=MibTableColumn
mplsVpnVrfBgpPathAttrAggregatorAS=_MplsVpnVrfBgpPathAttrAggregatorAS_Object((1,3,6,1,3,118,1,2,5,1,10),_MplsVpnVrfBgpPathAttrAggregatorAS_Type())
mplsVpnVrfBgpPathAttrAggregatorAS.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsVpnVrfBgpPathAttrAggregatorAS.setStatus(_A)
_MplsVpnVrfBgpPathAttrAggregatorAddr_Type=InetAddress
_MplsVpnVrfBgpPathAttrAggregatorAddr_Object=MibTableColumn
mplsVpnVrfBgpPathAttrAggregatorAddr=_MplsVpnVrfBgpPathAttrAggregatorAddr_Object((1,3,6,1,3,118,1,2,5,1,11),_MplsVpnVrfBgpPathAttrAggregatorAddr_Type())
mplsVpnVrfBgpPathAttrAggregatorAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsVpnVrfBgpPathAttrAggregatorAddr.setStatus(_A)
class _MplsVpnVrfBgpPathAttrCalcLocalPref_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,2147483647))
_MplsVpnVrfBgpPathAttrCalcLocalPref_Type.__name__=_E
_MplsVpnVrfBgpPathAttrCalcLocalPref_Object=MibTableColumn
mplsVpnVrfBgpPathAttrCalcLocalPref=_MplsVpnVrfBgpPathAttrCalcLocalPref_Object((1,3,6,1,3,118,1,2,5,1,12),_MplsVpnVrfBgpPathAttrCalcLocalPref_Type())
mplsVpnVrfBgpPathAttrCalcLocalPref.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsVpnVrfBgpPathAttrCalcLocalPref.setStatus(_A)
class _MplsVpnVrfBgpPathAttrBest_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('false',1),('true',2)))
_MplsVpnVrfBgpPathAttrBest_Type.__name__=_E
_MplsVpnVrfBgpPathAttrBest_Object=MibTableColumn
mplsVpnVrfBgpPathAttrBest=_MplsVpnVrfBgpPathAttrBest_Object((1,3,6,1,3,118,1,2,5,1,13),_MplsVpnVrfBgpPathAttrBest_Type())
mplsVpnVrfBgpPathAttrBest.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsVpnVrfBgpPathAttrBest.setStatus(_A)
class _MplsVpnVrfBgpPathAttrUnknown_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_MplsVpnVrfBgpPathAttrUnknown_Type.__name__=_H
_MplsVpnVrfBgpPathAttrUnknown_Object=MibTableColumn
mplsVpnVrfBgpPathAttrUnknown=_MplsVpnVrfBgpPathAttrUnknown_Object((1,3,6,1,3,118,1,2,5,1,14),_MplsVpnVrfBgpPathAttrUnknown_Type())
mplsVpnVrfBgpPathAttrUnknown.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsVpnVrfBgpPathAttrUnknown.setStatus(_A)
_MplsVpnVrfSecTable_Object=MibTable
mplsVpnVrfSecTable=_MplsVpnVrfSecTable_Object((1,3,6,1,3,118,1,2,6))
if mibBuilder.loadTexts:mplsVpnVrfSecTable.setStatus(_A)
_MplsVpnVrfSecEntry_Object=MibTableRow
mplsVpnVrfSecEntry=_MplsVpnVrfSecEntry_Object((1,3,6,1,3,118,1,2,6,1))
if mibBuilder.loadTexts:mplsVpnVrfSecEntry.setStatus(_A)
_MplsVpnVrfSecIllegalLabelViolations_Type=Counter32
_MplsVpnVrfSecIllegalLabelViolations_Object=MibTableColumn
mplsVpnVrfSecIllegalLabelViolations=_MplsVpnVrfSecIllegalLabelViolations_Object((1,3,6,1,3,118,1,2,6,1,1),_MplsVpnVrfSecIllegalLabelViolations_Type())
mplsVpnVrfSecIllegalLabelViolations.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsVpnVrfSecIllegalLabelViolations.setStatus(_A)
_MplsVpnVrfSecIllegalLabelRcvThresh_Type=Unsigned32
_MplsVpnVrfSecIllegalLabelRcvThresh_Object=MibTableColumn
mplsVpnVrfSecIllegalLabelRcvThresh=_MplsVpnVrfSecIllegalLabelRcvThresh_Object((1,3,6,1,3,118,1,2,6,1,2),_MplsVpnVrfSecIllegalLabelRcvThresh_Type())
mplsVpnVrfSecIllegalLabelRcvThresh.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsVpnVrfSecIllegalLabelRcvThresh.setStatus(_A)
_MplsVpnPerf_ObjectIdentity=ObjectIdentity
mplsVpnPerf=_MplsVpnPerf_ObjectIdentity((1,3,6,1,3,118,1,3))
_MplsVpnVrfPerfTable_Object=MibTable
mplsVpnVrfPerfTable=_MplsVpnVrfPerfTable_Object((1,3,6,1,3,118,1,3,1))
if mibBuilder.loadTexts:mplsVpnVrfPerfTable.setStatus(_A)
_MplsVpnVrfPerfEntry_Object=MibTableRow
mplsVpnVrfPerfEntry=_MplsVpnVrfPerfEntry_Object((1,3,6,1,3,118,1,3,1,1))
if mibBuilder.loadTexts:mplsVpnVrfPerfEntry.setStatus(_A)
_MplsVpnVrfPerfRoutesAdded_Type=Counter32
_MplsVpnVrfPerfRoutesAdded_Object=MibTableColumn
mplsVpnVrfPerfRoutesAdded=_MplsVpnVrfPerfRoutesAdded_Object((1,3,6,1,3,118,1,3,1,1,1),_MplsVpnVrfPerfRoutesAdded_Type())
mplsVpnVrfPerfRoutesAdded.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsVpnVrfPerfRoutesAdded.setStatus(_A)
_MplsVpnVrfPerfRoutesDeleted_Type=Counter32
_MplsVpnVrfPerfRoutesDeleted_Object=MibTableColumn
mplsVpnVrfPerfRoutesDeleted=_MplsVpnVrfPerfRoutesDeleted_Object((1,3,6,1,3,118,1,3,1,1,2),_MplsVpnVrfPerfRoutesDeleted_Type())
mplsVpnVrfPerfRoutesDeleted.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsVpnVrfPerfRoutesDeleted.setStatus(_A)
_MplsVpnVrfPerfCurrNumRoutes_Type=Unsigned32
_MplsVpnVrfPerfCurrNumRoutes_Object=MibTableColumn
mplsVpnVrfPerfCurrNumRoutes=_MplsVpnVrfPerfCurrNumRoutes_Object((1,3,6,1,3,118,1,3,1,1,3),_MplsVpnVrfPerfCurrNumRoutes_Type())
mplsVpnVrfPerfCurrNumRoutes.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsVpnVrfPerfCurrNumRoutes.setStatus(_A)
_MplsVpnRoute_ObjectIdentity=ObjectIdentity
mplsVpnRoute=_MplsVpnRoute_ObjectIdentity((1,3,6,1,3,118,1,4))
_MplsVpnVrfRouteTable_Object=MibTable
mplsVpnVrfRouteTable=_MplsVpnVrfRouteTable_Object((1,3,6,1,3,118,1,4,1))
if mibBuilder.loadTexts:mplsVpnVrfRouteTable.setStatus(_A)
_MplsVpnVrfRouteEntry_Object=MibTableRow
mplsVpnVrfRouteEntry=_MplsVpnVrfRouteEntry_Object((1,3,6,1,3,118,1,4,1,1))
mplsVpnVrfRouteEntry.setIndexNames((0,_B,_G),(0,_B,_R),(0,_B,_S),(0,_B,_T),(0,_B,_U))
if mibBuilder.loadTexts:mplsVpnVrfRouteEntry.setStatus(_A)
_MplsVpnVrfRouteDest_Type=InetAddress
_MplsVpnVrfRouteDest_Object=MibTableColumn
mplsVpnVrfRouteDest=_MplsVpnVrfRouteDest_Object((1,3,6,1,3,118,1,4,1,1,1),_MplsVpnVrfRouteDest_Type())
mplsVpnVrfRouteDest.setMaxAccess(_F)
if mibBuilder.loadTexts:mplsVpnVrfRouteDest.setStatus(_A)
_MplsVpnVrfRouteDestAddrType_Type=InetAddressType
_MplsVpnVrfRouteDestAddrType_Object=MibTableColumn
mplsVpnVrfRouteDestAddrType=_MplsVpnVrfRouteDestAddrType_Object((1,3,6,1,3,118,1,4,1,1,2),_MplsVpnVrfRouteDestAddrType_Type())
mplsVpnVrfRouteDestAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsVpnVrfRouteDestAddrType.setStatus(_A)
_MplsVpnVrfRouteMask_Type=InetAddress
_MplsVpnVrfRouteMask_Object=MibTableColumn
mplsVpnVrfRouteMask=_MplsVpnVrfRouteMask_Object((1,3,6,1,3,118,1,4,1,1,3),_MplsVpnVrfRouteMask_Type())
mplsVpnVrfRouteMask.setMaxAccess(_F)
if mibBuilder.loadTexts:mplsVpnVrfRouteMask.setStatus(_A)
_MplsVpnVrfRouteMaskAddrType_Type=InetAddressType
_MplsVpnVrfRouteMaskAddrType_Object=MibTableColumn
mplsVpnVrfRouteMaskAddrType=_MplsVpnVrfRouteMaskAddrType_Object((1,3,6,1,3,118,1,4,1,1,4),_MplsVpnVrfRouteMaskAddrType_Type())
mplsVpnVrfRouteMaskAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsVpnVrfRouteMaskAddrType.setStatus(_A)
_MplsVpnVrfRouteTos_Type=Unsigned32
_MplsVpnVrfRouteTos_Object=MibTableColumn
mplsVpnVrfRouteTos=_MplsVpnVrfRouteTos_Object((1,3,6,1,3,118,1,4,1,1,5),_MplsVpnVrfRouteTos_Type())
mplsVpnVrfRouteTos.setMaxAccess(_F)
if mibBuilder.loadTexts:mplsVpnVrfRouteTos.setStatus(_A)
_MplsVpnVrfRouteNextHop_Type=InetAddress
_MplsVpnVrfRouteNextHop_Object=MibTableColumn
mplsVpnVrfRouteNextHop=_MplsVpnVrfRouteNextHop_Object((1,3,6,1,3,118,1,4,1,1,6),_MplsVpnVrfRouteNextHop_Type())
mplsVpnVrfRouteNextHop.setMaxAccess(_F)
if mibBuilder.loadTexts:mplsVpnVrfRouteNextHop.setStatus(_A)
_MplsVpnVrfRouteNextHopAddrType_Type=InetAddressType
_MplsVpnVrfRouteNextHopAddrType_Object=MibTableColumn
mplsVpnVrfRouteNextHopAddrType=_MplsVpnVrfRouteNextHopAddrType_Object((1,3,6,1,3,118,1,4,1,1,7),_MplsVpnVrfRouteNextHopAddrType_Type())
mplsVpnVrfRouteNextHopAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsVpnVrfRouteNextHopAddrType.setStatus(_A)
_MplsVpnVrfRouteIfIndex_Type=InterfaceIndex
_MplsVpnVrfRouteIfIndex_Object=MibTableColumn
mplsVpnVrfRouteIfIndex=_MplsVpnVrfRouteIfIndex_Object((1,3,6,1,3,118,1,4,1,1,8),_MplsVpnVrfRouteIfIndex_Type())
mplsVpnVrfRouteIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsVpnVrfRouteIfIndex.setStatus(_A)
class _MplsVpnVrfRouteType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_J,1),('reject',2),('local',3),('remote',4)))
_MplsVpnVrfRouteType_Type.__name__=_E
_MplsVpnVrfRouteType_Object=MibTableColumn
mplsVpnVrfRouteType=_MplsVpnVrfRouteType_Object((1,3,6,1,3,118,1,4,1,1,9),_MplsVpnVrfRouteType_Type())
mplsVpnVrfRouteType.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsVpnVrfRouteType.setStatus(_A)
class _MplsVpnVrfRouteProto_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16)));namedValues=NamedValues(*((_J,1),('local',2),('netmgmt',3),('icmp',4),('egp',5),('ggp',6),('hello',7),('rip',8),('isIs',9),('esIs',10),('ciscoIgrp',11),('bbnSpfIgp',12),('ospf',13),('bgp',14),('idpr',15),('ciscoEigrp',16)))
_MplsVpnVrfRouteProto_Type.__name__=_E
_MplsVpnVrfRouteProto_Object=MibTableColumn
mplsVpnVrfRouteProto=_MplsVpnVrfRouteProto_Object((1,3,6,1,3,118,1,4,1,1,10),_MplsVpnVrfRouteProto_Type())
mplsVpnVrfRouteProto.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsVpnVrfRouteProto.setStatus(_A)
_MplsVpnVrfRouteAge_Type=Unsigned32
_MplsVpnVrfRouteAge_Object=MibTableColumn
mplsVpnVrfRouteAge=_MplsVpnVrfRouteAge_Object((1,3,6,1,3,118,1,4,1,1,11),_MplsVpnVrfRouteAge_Type())
mplsVpnVrfRouteAge.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsVpnVrfRouteAge.setStatus(_A)
_MplsVpnVrfRouteInfo_Type=ObjectIdentifier
_MplsVpnVrfRouteInfo_Object=MibTableColumn
mplsVpnVrfRouteInfo=_MplsVpnVrfRouteInfo_Object((1,3,6,1,3,118,1,4,1,1,12),_MplsVpnVrfRouteInfo_Type())
mplsVpnVrfRouteInfo.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsVpnVrfRouteInfo.setStatus(_A)
_MplsVpnVrfRouteNextHopAS_Type=Unsigned32
_MplsVpnVrfRouteNextHopAS_Object=MibTableColumn
mplsVpnVrfRouteNextHopAS=_MplsVpnVrfRouteNextHopAS_Object((1,3,6,1,3,118,1,4,1,1,13),_MplsVpnVrfRouteNextHopAS_Type())
mplsVpnVrfRouteNextHopAS.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsVpnVrfRouteNextHopAS.setStatus(_A)
_MplsVpnVrfRouteMetric1_Type=Integer32
_MplsVpnVrfRouteMetric1_Object=MibTableColumn
mplsVpnVrfRouteMetric1=_MplsVpnVrfRouteMetric1_Object((1,3,6,1,3,118,1,4,1,1,14),_MplsVpnVrfRouteMetric1_Type())
mplsVpnVrfRouteMetric1.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsVpnVrfRouteMetric1.setStatus(_A)
_MplsVpnVrfRouteMetric2_Type=Integer32
_MplsVpnVrfRouteMetric2_Object=MibTableColumn
mplsVpnVrfRouteMetric2=_MplsVpnVrfRouteMetric2_Object((1,3,6,1,3,118,1,4,1,1,15),_MplsVpnVrfRouteMetric2_Type())
mplsVpnVrfRouteMetric2.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsVpnVrfRouteMetric2.setStatus(_A)
_MplsVpnVrfRouteMetric3_Type=Integer32
_MplsVpnVrfRouteMetric3_Object=MibTableColumn
mplsVpnVrfRouteMetric3=_MplsVpnVrfRouteMetric3_Object((1,3,6,1,3,118,1,4,1,1,16),_MplsVpnVrfRouteMetric3_Type())
mplsVpnVrfRouteMetric3.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsVpnVrfRouteMetric3.setStatus(_A)
_MplsVpnVrfRouteMetric4_Type=Integer32
_MplsVpnVrfRouteMetric4_Object=MibTableColumn
mplsVpnVrfRouteMetric4=_MplsVpnVrfRouteMetric4_Object((1,3,6,1,3,118,1,4,1,1,17),_MplsVpnVrfRouteMetric4_Type())
mplsVpnVrfRouteMetric4.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsVpnVrfRouteMetric4.setStatus(_A)
_MplsVpnVrfRouteMetric5_Type=Integer32
_MplsVpnVrfRouteMetric5_Object=MibTableColumn
mplsVpnVrfRouteMetric5=_MplsVpnVrfRouteMetric5_Object((1,3,6,1,3,118,1,4,1,1,18),_MplsVpnVrfRouteMetric5_Type())
mplsVpnVrfRouteMetric5.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsVpnVrfRouteMetric5.setStatus(_A)
_MplsVpnVrfRouteRowStatus_Type=RowStatus
_MplsVpnVrfRouteRowStatus_Object=MibTableColumn
mplsVpnVrfRouteRowStatus=_MplsVpnVrfRouteRowStatus_Object((1,3,6,1,3,118,1,4,1,1,19),_MplsVpnVrfRouteRowStatus_Type())
mplsVpnVrfRouteRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsVpnVrfRouteRowStatus.setStatus(_A)
_MplsVpnVrfRouteStorageType_Type=StorageType
_MplsVpnVrfRouteStorageType_Object=MibTableColumn
mplsVpnVrfRouteStorageType=_MplsVpnVrfRouteStorageType_Object((1,3,6,1,3,118,1,4,1,1,20),_MplsVpnVrfRouteStorageType_Type())
mplsVpnVrfRouteStorageType.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsVpnVrfRouteStorageType.setStatus(_A)
_MplsVpnConformance_ObjectIdentity=ObjectIdentity
mplsVpnConformance=_MplsVpnConformance_ObjectIdentity((1,3,6,1,3,118,3))
_MplsVpnGroups_ObjectIdentity=ObjectIdentity
mplsVpnGroups=_MplsVpnGroups_ObjectIdentity((1,3,6,1,3,118,3,1))
_MplsVpnCompliances_ObjectIdentity=ObjectIdentity
mplsVpnCompliances=_MplsVpnCompliances_ObjectIdentity((1,3,6,1,3,118,3,2))
mplsVpnVrfEntry.registerAugmentions((_B,_V))
mplsVpnVrfSecEntry.setIndexNames(*mplsVpnVrfEntry.getIndexNames())
mplsVpnVrfEntry.registerAugmentions((_B,_W))
mplsVpnVrfPerfEntry.setIndexNames(*mplsVpnVrfEntry.getIndexNames())
mplsVpnScalarGroup=ObjectGroup((1,3,6,1,3,118,3,1,1))
mplsVpnScalarGroup.setObjects(*((_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b)))
if mibBuilder.loadTexts:mplsVpnScalarGroup.setStatus(_A)
mplsVpnVrfGroup=ObjectGroup((1,3,6,1,3,118,3,1,2))
mplsVpnVrfGroup.setObjects(*((_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n)))
if mibBuilder.loadTexts:mplsVpnVrfGroup.setStatus(_A)
mplsVpnInterfaceGroup=ObjectGroup((1,3,6,1,3,118,3,1,3))
mplsVpnInterfaceGroup.setObjects(*((_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s)))
if mibBuilder.loadTexts:mplsVpnInterfaceGroup.setStatus(_A)
mplsVpnPerfGroup=ObjectGroup((1,3,6,1,3,118,3,1,4))
mplsVpnPerfGroup.setObjects(*((_B,_t),(_B,_u),(_B,_v)))
if mibBuilder.loadTexts:mplsVpnPerfGroup.setStatus(_A)
mplsVpnVrfBgpNbrGroup=ObjectGroup((1,3,6,1,3,118,3,1,5))
mplsVpnVrfBgpNbrGroup.setObjects(*((_B,_w),(_B,_x),(_B,_y),(_B,_z),(_B,_A0)))
if mibBuilder.loadTexts:mplsVpnVrfBgpNbrGroup.setStatus(_A)
mplsVpnVrfBgpPrefixGroup=ObjectGroup((1,3,6,1,3,118,3,1,6))
mplsVpnVrfBgpPrefixGroup.setObjects(*((_B,_A1),(_B,_A2),(_B,_A3),(_B,_A4),(_B,_A5),(_B,_A6),(_B,_A7),(_B,_A8),(_B,_A9),(_B,_AA),(_B,_AB)))
if mibBuilder.loadTexts:mplsVpnVrfBgpPrefixGroup.setStatus(_A)
mplsVpnSecGroup=ObjectGroup((1,3,6,1,3,118,3,1,7))
mplsVpnSecGroup.setObjects(*((_B,_AC),(_B,_AD)))
if mibBuilder.loadTexts:mplsVpnSecGroup.setStatus(_A)
mplsVpnVrfRouteGroup=ObjectGroup((1,3,6,1,3,118,3,1,8))
mplsVpnVrfRouteGroup.setObjects(*((_B,_AE),(_B,_AF),(_B,_AG),(_B,_AH),(_B,_AI),(_B,_AJ),(_B,_AK),(_B,_AL),(_B,_AM),(_B,_AN),(_B,_AO),(_B,_AP),(_B,_AQ),(_B,_AR),(_B,_AS),(_B,_AT)))
if mibBuilder.loadTexts:mplsVpnVrfRouteGroup.setStatus(_A)
mplsVpnVrfRouteTargetGroup=ObjectGroup((1,3,6,1,3,118,3,1,9))
mplsVpnVrfRouteTargetGroup.setObjects(*((_B,_AU),(_B,_AV),(_B,_AW)))
if mibBuilder.loadTexts:mplsVpnVrfRouteTargetGroup.setStatus(_A)
mplsVrfIfUp=NotificationType((1,3,6,1,3,118,0,1))
if mibBuilder.loadTexts:mplsVrfIfUp.setStatus(_A)
mplsVrfIfDown=NotificationType((1,3,6,1,3,118,0,2))
if mibBuilder.loadTexts:mplsVrfIfDown.setStatus(_A)
mplsNumVrfRouteMidThreshExceeded=NotificationType((1,3,6,1,3,118,0,3))
if mibBuilder.loadTexts:mplsNumVrfRouteMidThreshExceeded.setStatus(_A)
mplsNumVrfRouteMaxThreshExceeded=NotificationType((1,3,6,1,3,118,0,4))
if mibBuilder.loadTexts:mplsNumVrfRouteMaxThreshExceeded.setStatus(_A)
mplsNumVrfSecIllegalLabelThreshExceeded=NotificationType((1,3,6,1,3,118,0,5))
if mibBuilder.loadTexts:mplsNumVrfSecIllegalLabelThreshExceeded.setStatus(_A)
mplsVpnNotificationGroup=NotificationGroup((1,3,6,1,3,118,3,1,10))
mplsVpnNotificationGroup.setObjects(*((_B,_AX),(_B,_AY),(_B,_AZ),(_B,_Aa),(_B,_Ab)))
if mibBuilder.loadTexts:mplsVpnNotificationGroup.setStatus(_A)
mplsVpnModuleCompliance=ModuleCompliance((1,3,6,1,3,118,3,2,1))
mplsVpnModuleCompliance.setObjects(*((_B,_Ac),(_B,_Ad),(_B,_Ae),(_B,_Af),(_B,_Ag),(_B,_Ah),(_B,_Ai)))
if mibBuilder.loadTexts:mplsVpnModuleCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'MplsVpnId':MplsVpnId,'MplsVpnRouteDistinguisher':MplsVpnRouteDistinguisher,'mplsVpnMIB':mplsVpnMIB,'mplsVpnNotifications':mplsVpnNotifications,_AX:mplsVrfIfUp,_AY:mplsVrfIfDown,_AZ:mplsNumVrfRouteMidThreshExceeded,_Aa:mplsNumVrfRouteMaxThreshExceeded,_Ab:mplsNumVrfSecIllegalLabelThreshExceeded,'mplsVpnObjects':mplsVpnObjects,'mplsVpnScalars':mplsVpnScalars,_X:mplsVpnConfiguredVrfs,_Y:mplsVpnActiveVrfs,_Z:mplsVpnConnectedInterfaces,_a:mplsVpnNotificationEnable,_b:mplsVpnVrfConfMaxPossibleRoutes,'mplsVpnConf':mplsVpnConf,'mplsVpnInterfaceConfTable':mplsVpnInterfaceConfTable,'mplsVpnInterfaceConfEntry':mplsVpnInterfaceConfEntry,_I:mplsVpnInterfaceConfIndex,_o:mplsVpnInterfaceLabelEdgeType,_p:mplsVpnInterfaceVpnClassification,_q:mplsVpnInterfaceVpnRouteDistProtocol,_r:mplsVpnInterfaceConfStorageType,_s:mplsVpnInterfaceConfRowStatus,'mplsVpnVrfTable':mplsVpnVrfTable,'mplsVpnVrfEntry':mplsVpnVrfEntry,_G:mplsVpnVrfName,_c:mplsVpnVrfDescription,_d:mplsVpnVrfRouteDistinguisher,_e:mplsVpnVrfCreationTime,_f:mplsVpnVrfOperStatus,_g:mplsVpnVrfActiveInterfaces,_h:mplsVpnVrfAssociatedInterfaces,_i:mplsVpnVrfConfMidRouteThreshold,_j:mplsVpnVrfConfHighRouteThreshold,_k:mplsVpnVrfConfMaxRoutes,_l:mplsVpnVrfConfLastChanged,_m:mplsVpnVrfConfRowStatus,_n:mplsVpnVrfConfStorageType,'mplsVpnVrfRouteTargetTable':mplsVpnVrfRouteTargetTable,'mplsVpnVrfRouteTargetEntry':mplsVpnVrfRouteTargetEntry,_L:mplsVpnVrfRouteTargetIndex,_M:mplsVpnVrfRouteTargetType,_AU:mplsVpnVrfRouteTarget,_AV:mplsVpnVrfRouteTargetDescr,_AW:mplsVpnVrfRouteTargetRowStatus,'mplsVpnVrfBgpNbrAddrTable':mplsVpnVrfBgpNbrAddrTable,'mplsVpnVrfBgpNbrAddrEntry':mplsVpnVrfBgpNbrAddrEntry,_N:mplsVpnVrfBgpNbrIndex,_w:mplsVpnVrfBgpNbrRole,_x:mplsVpnVrfBgpNbrType,_y:mplsVpnVrfBgpNbrAddr,_z:mplsVpnVrfBgpNbrRowStatus,_A0:mplsVpnVrfBgpNbrStorageType,'mplsVpnVrfBgpNbrPrefixTable':mplsVpnVrfBgpNbrPrefixTable,'mplsVpnVrfBgpNbrPrefixEntry':mplsVpnVrfBgpNbrPrefixEntry,_Q:mplsVpnVrfBgpPathAttrPeer,_P:mplsVpnVrfBgpPathAttrIpAddrPrefixLen,_O:mplsVpnVrfBgpPathAttrIpAddrPrefix,_A1:mplsVpnVrfBgpPathAttrOrigin,_A2:mplsVpnVrfBgpPathAttrASPathSegment,_A3:mplsVpnVrfBgpPathAttrNextHop,_A4:mplsVpnVrfBgpPathAttrMultiExitDisc,_A5:mplsVpnVrfBgpPathAttrLocalPref,_A6:mplsVpnVrfBgpPathAttrAtomicAggregate,_A7:mplsVpnVrfBgpPathAttrAggregatorAS,_A8:mplsVpnVrfBgpPathAttrAggregatorAddr,_A9:mplsVpnVrfBgpPathAttrCalcLocalPref,_AA:mplsVpnVrfBgpPathAttrBest,_AB:mplsVpnVrfBgpPathAttrUnknown,'mplsVpnVrfSecTable':mplsVpnVrfSecTable,_V:mplsVpnVrfSecEntry,_AC:mplsVpnVrfSecIllegalLabelViolations,_AD:mplsVpnVrfSecIllegalLabelRcvThresh,'mplsVpnPerf':mplsVpnPerf,'mplsVpnVrfPerfTable':mplsVpnVrfPerfTable,_W:mplsVpnVrfPerfEntry,_t:mplsVpnVrfPerfRoutesAdded,_u:mplsVpnVrfPerfRoutesDeleted,_v:mplsVpnVrfPerfCurrNumRoutes,'mplsVpnRoute':mplsVpnRoute,'mplsVpnVrfRouteTable':mplsVpnVrfRouteTable,'mplsVpnVrfRouteEntry':mplsVpnVrfRouteEntry,_R:mplsVpnVrfRouteDest,_AE:mplsVpnVrfRouteDestAddrType,_S:mplsVpnVrfRouteMask,_AF:mplsVpnVrfRouteMaskAddrType,_T:mplsVpnVrfRouteTos,_U:mplsVpnVrfRouteNextHop,_AG:mplsVpnVrfRouteNextHopAddrType,_AH:mplsVpnVrfRouteIfIndex,_AI:mplsVpnVrfRouteType,_AJ:mplsVpnVrfRouteProto,_AK:mplsVpnVrfRouteAge,_AL:mplsVpnVrfRouteInfo,_AM:mplsVpnVrfRouteNextHopAS,_AN:mplsVpnVrfRouteMetric1,_AO:mplsVpnVrfRouteMetric2,_AP:mplsVpnVrfRouteMetric3,_AQ:mplsVpnVrfRouteMetric4,_AR:mplsVpnVrfRouteMetric5,_AS:mplsVpnVrfRouteRowStatus,_AT:mplsVpnVrfRouteStorageType,'mplsVpnConformance':mplsVpnConformance,'mplsVpnGroups':mplsVpnGroups,_Ac:mplsVpnScalarGroup,_Ad:mplsVpnVrfGroup,_Ae:mplsVpnInterfaceGroup,_Af:mplsVpnPerfGroup,_Ah:mplsVpnVrfBgpNbrGroup,'mplsVpnVrfBgpPrefixGroup':mplsVpnVrfBgpPrefixGroup,'mplsVpnSecGroup':mplsVpnSecGroup,_Ag:mplsVpnVrfRouteGroup,_Ai:mplsVpnVrfRouteTargetGroup,'mplsVpnNotificationGroup':mplsVpnNotificationGroup,'mplsVpnCompliances':mplsVpnCompliances,'mplsVpnModuleCompliance':mplsVpnModuleCompliance})