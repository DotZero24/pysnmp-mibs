_M='mplsVpnVrfRouteNextHop'
_L='mplsVpnVrfRouteMask'
_K='mplsVpnVrfRouteDest'
_J='mplsVpnVrfBgpNbrAddr'
_I='mplsVpnVrfRouteTargetType'
_H='mplsVpnVrfRouteTarget'
_G='mplsVpnInterfaceConfIndex'
_F='mplsVpnVrfName'
_E='Integer32'
_D='A3COM-HUAWEI-MPLS-BGP-VPN-MIB'
_C='read-only'
_B='read-create'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
huaweiMgmt,hwMpls=mibBuilder.importSymbols('A3COM-HUAWEI-OID-MIB','huaweiMgmt','hwMpls')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,experimental,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','experimental','iso')
DisplayString,PhysAddress,RowStatus,StorageType,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','StorageType','TextualConvention','TimeStamp','TruthValue')
hwMplsVpn=ModuleIdentity((1,3,6,1,4,1,43,45,1,5,12,3))
if mibBuilder.loadTexts:hwMplsVpn.setRevisions(('2001-07-20 12:00','2001-07-17 12:00','2001-07-10 12:00','2001-06-19 12:00','2001-05-30 12:00','2000-09-30 12:00'))
class MplsVpnId(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
class MplsVpnRouteDistinguisher(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,256))
_MplsVpnObjects_ObjectIdentity=ObjectIdentity
mplsVpnObjects=_MplsVpnObjects_ObjectIdentity((1,3,6,1,4,1,43,45,1,5,12,3,1))
_MplsVpnScalars_ObjectIdentity=ObjectIdentity
mplsVpnScalars=_MplsVpnScalars_ObjectIdentity((1,3,6,1,4,1,43,45,1,5,12,3,1,1))
_MplsVpnConfiguredVrfs_Type=Unsigned32
_MplsVpnConfiguredVrfs_Object=MibScalar
mplsVpnConfiguredVrfs=_MplsVpnConfiguredVrfs_Object((1,3,6,1,4,1,43,45,1,5,12,3,1,1,1),_MplsVpnConfiguredVrfs_Type())
mplsVpnConfiguredVrfs.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsVpnConfiguredVrfs.setStatus(_A)
_MplsVpnActiveVrfs_Type=Unsigned32
_MplsVpnActiveVrfs_Object=MibScalar
mplsVpnActiveVrfs=_MplsVpnActiveVrfs_Object((1,3,6,1,4,1,43,45,1,5,12,3,1,1,2),_MplsVpnActiveVrfs_Type())
mplsVpnActiveVrfs.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsVpnActiveVrfs.setStatus(_A)
_MplsVpnConf_ObjectIdentity=ObjectIdentity
mplsVpnConf=_MplsVpnConf_ObjectIdentity((1,3,6,1,4,1,43,45,1,5,12,3,1,2))
_MplsVpnInterfaceConfTable_Object=MibTable
mplsVpnInterfaceConfTable=_MplsVpnInterfaceConfTable_Object((1,3,6,1,4,1,43,45,1,5,12,3,1,2,1))
if mibBuilder.loadTexts:mplsVpnInterfaceConfTable.setStatus(_A)
_MplsVpnInterfaceConfEntry_Object=MibTableRow
mplsVpnInterfaceConfEntry=_MplsVpnInterfaceConfEntry_Object((1,3,6,1,4,1,43,45,1,5,12,3,1,2,1,1))
mplsVpnInterfaceConfEntry.setIndexNames((0,_D,_F),(0,_D,_G))
if mibBuilder.loadTexts:mplsVpnInterfaceConfEntry.setStatus(_A)
_MplsVpnInterfaceConfIndex_Type=InterfaceIndex
_MplsVpnInterfaceConfIndex_Object=MibTableColumn
mplsVpnInterfaceConfIndex=_MplsVpnInterfaceConfIndex_Object((1,3,6,1,4,1,43,45,1,5,12,3,1,2,1,1,1),_MplsVpnInterfaceConfIndex_Type())
mplsVpnInterfaceConfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsVpnInterfaceConfIndex.setStatus(_A)
class _MplsVpnInterfaceLabelEdgeType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('providerEdge',1),('customerEdge',2)))
_MplsVpnInterfaceLabelEdgeType_Type.__name__=_E
_MplsVpnInterfaceLabelEdgeType_Object=MibTableColumn
mplsVpnInterfaceLabelEdgeType=_MplsVpnInterfaceLabelEdgeType_Object((1,3,6,1,4,1,43,45,1,5,12,3,1,2,1,1,2),_MplsVpnInterfaceLabelEdgeType_Type())
mplsVpnInterfaceLabelEdgeType.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsVpnInterfaceLabelEdgeType.setStatus(_A)
class _MplsVpnInterfaceVpnClassification_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('carrierOfCarrier',1),('enterprise',2),('interProvider',3)))
_MplsVpnInterfaceVpnClassification_Type.__name__=_E
_MplsVpnInterfaceVpnClassification_Object=MibTableColumn
mplsVpnInterfaceVpnClassification=_MplsVpnInterfaceVpnClassification_Object((1,3,6,1,4,1,43,45,1,5,12,3,1,2,1,1,3),_MplsVpnInterfaceVpnClassification_Type())
mplsVpnInterfaceVpnClassification.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsVpnInterfaceVpnClassification.setStatus(_A)
_MplsVpnInterfaceIpAddress_Type=InetAddress
_MplsVpnInterfaceIpAddress_Object=MibTableColumn
mplsVpnInterfaceIpAddress=_MplsVpnInterfaceIpAddress_Object((1,3,6,1,4,1,43,45,1,5,12,3,1,2,1,1,4),_MplsVpnInterfaceIpAddress_Type())
mplsVpnInterfaceIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:mplsVpnInterfaceIpAddress.setStatus(_A)
_MplsVpnInterfaceIpAddressMask_Type=InetAddress
_MplsVpnInterfaceIpAddressMask_Object=MibTableColumn
mplsVpnInterfaceIpAddressMask=_MplsVpnInterfaceIpAddressMask_Object((1,3,6,1,4,1,43,45,1,5,12,3,1,2,1,1,5),_MplsVpnInterfaceIpAddressMask_Type())
mplsVpnInterfaceIpAddressMask.setMaxAccess(_B)
if mibBuilder.loadTexts:mplsVpnInterfaceIpAddressMask.setStatus(_A)
_MplsVpnInterfaceConfRowStatus_Type=RowStatus
_MplsVpnInterfaceConfRowStatus_Object=MibTableColumn
mplsVpnInterfaceConfRowStatus=_MplsVpnInterfaceConfRowStatus_Object((1,3,6,1,4,1,43,45,1,5,12,3,1,2,1,1,6),_MplsVpnInterfaceConfRowStatus_Type())
mplsVpnInterfaceConfRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:mplsVpnInterfaceConfRowStatus.setStatus(_A)
_MplsVpnVrfConfTable_Object=MibTable
mplsVpnVrfConfTable=_MplsVpnVrfConfTable_Object((1,3,6,1,4,1,43,45,1,5,12,3,1,2,2))
if mibBuilder.loadTexts:mplsVpnVrfConfTable.setStatus(_A)
_MplsVpnVrfConfEntry_Object=MibTableRow
mplsVpnVrfConfEntry=_MplsVpnVrfConfEntry_Object((1,3,6,1,4,1,43,45,1,5,12,3,1,2,2,1))
mplsVpnVrfConfEntry.setIndexNames((0,_D,_F))
if mibBuilder.loadTexts:mplsVpnVrfConfEntry.setStatus(_A)
_MplsVpnVrfName_Type=MplsVpnId
_MplsVpnVrfName_Object=MibTableColumn
mplsVpnVrfName=_MplsVpnVrfName_Object((1,3,6,1,4,1,43,45,1,5,12,3,1,2,2,1,1),_MplsVpnVrfName_Type())
mplsVpnVrfName.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsVpnVrfName.setStatus(_A)
_MplsVpnVrfRouteDistinguisher_Type=MplsVpnRouteDistinguisher
_MplsVpnVrfRouteDistinguisher_Object=MibTableColumn
mplsVpnVrfRouteDistinguisher=_MplsVpnVrfRouteDistinguisher_Object((1,3,6,1,4,1,43,45,1,5,12,3,1,2,2,1,2),_MplsVpnVrfRouteDistinguisher_Type())
mplsVpnVrfRouteDistinguisher.setMaxAccess(_B)
if mibBuilder.loadTexts:mplsVpnVrfRouteDistinguisher.setStatus(_A)
class _MplsVpnVrfNetPrefixType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('other',1),('rip',2),('ospf',3),('isis',4),('bgp',5),('static',6)))
_MplsVpnVrfNetPrefixType_Type.__name__=_E
_MplsVpnVrfNetPrefixType_Object=MibTableColumn
mplsVpnVrfNetPrefixType=_MplsVpnVrfNetPrefixType_Object((1,3,6,1,4,1,43,45,1,5,12,3,1,2,2,1,3),_MplsVpnVrfNetPrefixType_Type())
mplsVpnVrfNetPrefixType.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsVpnVrfNetPrefixType.setStatus(_A)
_MplsVpnVrfNetPrefix_Type=InetAddress
_MplsVpnVrfNetPrefix_Object=MibTableColumn
mplsVpnVrfNetPrefix=_MplsVpnVrfNetPrefix_Object((1,3,6,1,4,1,43,45,1,5,12,3,1,2,2,1,4),_MplsVpnVrfNetPrefix_Type())
mplsVpnVrfNetPrefix.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsVpnVrfNetPrefix.setStatus(_A)
_MplsVpnVrfIpRouteRedistributeConn_Type=TruthValue
_MplsVpnVrfIpRouteRedistributeConn_Object=MibTableColumn
mplsVpnVrfIpRouteRedistributeConn=_MplsVpnVrfIpRouteRedistributeConn_Object((1,3,6,1,4,1,43,45,1,5,12,3,1,2,2,1,5),_MplsVpnVrfIpRouteRedistributeConn_Type())
mplsVpnVrfIpRouteRedistributeConn.setMaxAccess(_B)
if mibBuilder.loadTexts:mplsVpnVrfIpRouteRedistributeConn.setStatus(_A)
_MplsVpnVrfIpRouteRedistributeStatic_Type=TruthValue
_MplsVpnVrfIpRouteRedistributeStatic_Object=MibTableColumn
mplsVpnVrfIpRouteRedistributeStatic=_MplsVpnVrfIpRouteRedistributeStatic_Object((1,3,6,1,4,1,43,45,1,5,12,3,1,2,2,1,6),_MplsVpnVrfIpRouteRedistributeStatic_Type())
mplsVpnVrfIpRouteRedistributeStatic.setMaxAccess(_B)
if mibBuilder.loadTexts:mplsVpnVrfIpRouteRedistributeStatic.setStatus(_A)
_MplsVpnVrfIpRouteRedistributeRip_Type=TruthValue
_MplsVpnVrfIpRouteRedistributeRip_Object=MibTableColumn
mplsVpnVrfIpRouteRedistributeRip=_MplsVpnVrfIpRouteRedistributeRip_Object((1,3,6,1,4,1,43,45,1,5,12,3,1,2,2,1,7),_MplsVpnVrfIpRouteRedistributeRip_Type())
mplsVpnVrfIpRouteRedistributeRip.setMaxAccess(_B)
if mibBuilder.loadTexts:mplsVpnVrfIpRouteRedistributeRip.setStatus(_A)
_MplsVpnVrfConfHighRouteThreshold_Type=Unsigned32
_MplsVpnVrfConfHighRouteThreshold_Object=MibTableColumn
mplsVpnVrfConfHighRouteThreshold=_MplsVpnVrfConfHighRouteThreshold_Object((1,3,6,1,4,1,43,45,1,5,12,3,1,2,2,1,8),_MplsVpnVrfConfHighRouteThreshold_Type())
mplsVpnVrfConfHighRouteThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:mplsVpnVrfConfHighRouteThreshold.setStatus(_A)
_MplsVpnVrfConfIsWarnOnly_Type=TruthValue
_MplsVpnVrfConfIsWarnOnly_Object=MibTableColumn
mplsVpnVrfConfIsWarnOnly=_MplsVpnVrfConfIsWarnOnly_Object((1,3,6,1,4,1,43,45,1,5,12,3,1,2,2,1,9),_MplsVpnVrfConfIsWarnOnly_Type())
mplsVpnVrfConfIsWarnOnly.setMaxAccess(_B)
if mibBuilder.loadTexts:mplsVpnVrfConfIsWarnOnly.setStatus(_A)
_MplsVpnVrfConfMaxRoutes_Type=Unsigned32
_MplsVpnVrfConfMaxRoutes_Object=MibTableColumn
mplsVpnVrfConfMaxRoutes=_MplsVpnVrfConfMaxRoutes_Object((1,3,6,1,4,1,43,45,1,5,12,3,1,2,2,1,10),_MplsVpnVrfConfMaxRoutes_Type())
mplsVpnVrfConfMaxRoutes.setMaxAccess(_B)
if mibBuilder.loadTexts:mplsVpnVrfConfMaxRoutes.setStatus(_A)
_MplsVpnVrfConfRowStatus_Type=RowStatus
_MplsVpnVrfConfRowStatus_Object=MibTableColumn
mplsVpnVrfConfRowStatus=_MplsVpnVrfConfRowStatus_Object((1,3,6,1,4,1,43,45,1,5,12,3,1,2,2,1,11),_MplsVpnVrfConfRowStatus_Type())
mplsVpnVrfConfRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:mplsVpnVrfConfRowStatus.setStatus(_A)
_MplsVpnVrfRouteTargetTable_Object=MibTable
mplsVpnVrfRouteTargetTable=_MplsVpnVrfRouteTargetTable_Object((1,3,6,1,4,1,43,45,1,5,12,3,1,2,3))
if mibBuilder.loadTexts:mplsVpnVrfRouteTargetTable.setStatus(_A)
_MplsVpnVrfRouteTargetEntry_Object=MibTableRow
mplsVpnVrfRouteTargetEntry=_MplsVpnVrfRouteTargetEntry_Object((1,3,6,1,4,1,43,45,1,5,12,3,1,2,3,1))
mplsVpnVrfRouteTargetEntry.setIndexNames((0,_D,_F),(0,_D,_H),(0,_D,_I))
if mibBuilder.loadTexts:mplsVpnVrfRouteTargetEntry.setStatus(_A)
_MplsVpnVrfRouteTarget_Type=MplsVpnRouteDistinguisher
_MplsVpnVrfRouteTarget_Object=MibTableColumn
mplsVpnVrfRouteTarget=_MplsVpnVrfRouteTarget_Object((1,3,6,1,4,1,43,45,1,5,12,3,1,2,3,1,1),_MplsVpnVrfRouteTarget_Type())
mplsVpnVrfRouteTarget.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsVpnVrfRouteTarget.setStatus(_A)
class _MplsVpnVrfRouteTargetType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('import',1),('export',2)))
_MplsVpnVrfRouteTargetType_Type.__name__=_E
_MplsVpnVrfRouteTargetType_Object=MibTableColumn
mplsVpnVrfRouteTargetType=_MplsVpnVrfRouteTargetType_Object((1,3,6,1,4,1,43,45,1,5,12,3,1,2,3,1,2),_MplsVpnVrfRouteTargetType_Type())
mplsVpnVrfRouteTargetType.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsVpnVrfRouteTargetType.setStatus(_A)
_MplsVpnVrfRouteTargetRowStatus_Type=RowStatus
_MplsVpnVrfRouteTargetRowStatus_Object=MibTableColumn
mplsVpnVrfRouteTargetRowStatus=_MplsVpnVrfRouteTargetRowStatus_Object((1,3,6,1,4,1,43,45,1,5,12,3,1,2,3,1,3),_MplsVpnVrfRouteTargetRowStatus_Type())
mplsVpnVrfRouteTargetRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:mplsVpnVrfRouteTargetRowStatus.setStatus(_A)
_MplsVpnVrfBgpNbrAddrTable_Object=MibTable
mplsVpnVrfBgpNbrAddrTable=_MplsVpnVrfBgpNbrAddrTable_Object((1,3,6,1,4,1,43,45,1,5,12,3,1,2,4))
if mibBuilder.loadTexts:mplsVpnVrfBgpNbrAddrTable.setStatus(_A)
_MplsVpnVrfBgpNbrAddrEntry_Object=MibTableRow
mplsVpnVrfBgpNbrAddrEntry=_MplsVpnVrfBgpNbrAddrEntry_Object((1,3,6,1,4,1,43,45,1,5,12,3,1,2,4,1))
mplsVpnVrfBgpNbrAddrEntry.setIndexNames((0,_D,_F),(0,_D,_J))
if mibBuilder.loadTexts:mplsVpnVrfBgpNbrAddrEntry.setStatus(_A)
_MplsVpnVrfBgpNbrAddr_Type=InetAddress
_MplsVpnVrfBgpNbrAddr_Object=MibTableColumn
mplsVpnVrfBgpNbrAddr=_MplsVpnVrfBgpNbrAddr_Object((1,3,6,1,4,1,43,45,1,5,12,3,1,2,4,1,1),_MplsVpnVrfBgpNbrAddr_Type())
mplsVpnVrfBgpNbrAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsVpnVrfBgpNbrAddr.setStatus(_A)
class _MplsVpnVrfBgpNbrRole_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('ce',1),('pe',2)))
_MplsVpnVrfBgpNbrRole_Type.__name__=_E
_MplsVpnVrfBgpNbrRole_Object=MibTableColumn
mplsVpnVrfBgpNbrRole=_MplsVpnVrfBgpNbrRole_Object((1,3,6,1,4,1,43,45,1,5,12,3,1,2,4,1,2),_MplsVpnVrfBgpNbrRole_Type())
mplsVpnVrfBgpNbrRole.setMaxAccess(_B)
if mibBuilder.loadTexts:mplsVpnVrfBgpNbrRole.setStatus(_A)
_MplsVpnVrfBgpNbrType_Type=InetAddressType
_MplsVpnVrfBgpNbrType_Object=MibTableColumn
mplsVpnVrfBgpNbrType=_MplsVpnVrfBgpNbrType_Object((1,3,6,1,4,1,43,45,1,5,12,3,1,2,4,1,3),_MplsVpnVrfBgpNbrType_Type())
mplsVpnVrfBgpNbrType.setMaxAccess(_B)
if mibBuilder.loadTexts:mplsVpnVrfBgpNbrType.setStatus(_A)
_MplsVpnVrfBgpNbrAsNumber_Type=Unsigned32
_MplsVpnVrfBgpNbrAsNumber_Object=MibTableColumn
mplsVpnVrfBgpNbrAsNumber=_MplsVpnVrfBgpNbrAsNumber_Object((1,3,6,1,4,1,43,45,1,5,12,3,1,2,4,1,4),_MplsVpnVrfBgpNbrAsNumber_Type())
mplsVpnVrfBgpNbrAsNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:mplsVpnVrfBgpNbrAsNumber.setStatus(_A)
class _MplsVpnVrfBgpNbrAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('mplsVpnVrfBgpNbrSetUp',1),('mplsVpnVrfBgpNbrSetDown',2)))
_MplsVpnVrfBgpNbrAdminStatus_Type.__name__=_E
_MplsVpnVrfBgpNbrAdminStatus_Object=MibTableColumn
mplsVpnVrfBgpNbrAdminStatus=_MplsVpnVrfBgpNbrAdminStatus_Object((1,3,6,1,4,1,43,45,1,5,12,3,1,2,4,1,5),_MplsVpnVrfBgpNbrAdminStatus_Type())
mplsVpnVrfBgpNbrAdminStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:mplsVpnVrfBgpNbrAdminStatus.setStatus(_A)
_MplsVpnVrfBgpNbrRowStatus_Type=RowStatus
_MplsVpnVrfBgpNbrRowStatus_Object=MibTableColumn
mplsVpnVrfBgpNbrRowStatus=_MplsVpnVrfBgpNbrRowStatus_Object((1,3,6,1,4,1,43,45,1,5,12,3,1,2,4,1,6),_MplsVpnVrfBgpNbrRowStatus_Type())
mplsVpnVrfBgpNbrRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:mplsVpnVrfBgpNbrRowStatus.setStatus(_A)
_MplsVpnRoute_ObjectIdentity=ObjectIdentity
mplsVpnRoute=_MplsVpnRoute_ObjectIdentity((1,3,6,1,4,1,43,45,1,5,12,3,1,3))
_MplsVpnVrfRouteTable_Object=MibTable
mplsVpnVrfRouteTable=_MplsVpnVrfRouteTable_Object((1,3,6,1,4,1,43,45,1,5,12,3,1,3,1))
if mibBuilder.loadTexts:mplsVpnVrfRouteTable.setStatus(_A)
_MplsVpnVrfRouteEntry_Object=MibTableRow
mplsVpnVrfRouteEntry=_MplsVpnVrfRouteEntry_Object((1,3,6,1,4,1,43,45,1,5,12,3,1,3,1,1))
mplsVpnVrfRouteEntry.setIndexNames((0,_D,_F),(0,_D,_K),(0,_D,_L),(0,_D,_M))
if mibBuilder.loadTexts:mplsVpnVrfRouteEntry.setStatus(_A)
_MplsVpnVrfRouteDest_Type=InetAddress
_MplsVpnVrfRouteDest_Object=MibTableColumn
mplsVpnVrfRouteDest=_MplsVpnVrfRouteDest_Object((1,3,6,1,4,1,43,45,1,5,12,3,1,3,1,1,1),_MplsVpnVrfRouteDest_Type())
mplsVpnVrfRouteDest.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsVpnVrfRouteDest.setStatus(_A)
_MplsVpnVrfRouteMask_Type=InetAddress
_MplsVpnVrfRouteMask_Object=MibTableColumn
mplsVpnVrfRouteMask=_MplsVpnVrfRouteMask_Object((1,3,6,1,4,1,43,45,1,5,12,3,1,3,1,1,2),_MplsVpnVrfRouteMask_Type())
mplsVpnVrfRouteMask.setMaxAccess(_B)
if mibBuilder.loadTexts:mplsVpnVrfRouteMask.setStatus(_A)
_MplsVpnVrfRouteNextHop_Type=InetAddress
_MplsVpnVrfRouteNextHop_Object=MibTableColumn
mplsVpnVrfRouteNextHop=_MplsVpnVrfRouteNextHop_Object((1,3,6,1,4,1,43,45,1,5,12,3,1,3,1,1,3),_MplsVpnVrfRouteNextHop_Type())
mplsVpnVrfRouteNextHop.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsVpnVrfRouteNextHop.setStatus(_A)
_MplsVpnVrfRouteIfIndex_Type=InterfaceIndex
_MplsVpnVrfRouteIfIndex_Object=MibTableColumn
mplsVpnVrfRouteIfIndex=_MplsVpnVrfRouteIfIndex_Object((1,3,6,1,4,1,43,45,1,5,12,3,1,3,1,1,4),_MplsVpnVrfRouteIfIndex_Type())
mplsVpnVrfRouteIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:mplsVpnVrfRouteIfIndex.setStatus(_A)
class _MplsVpnVrfRouteProto_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16)));namedValues=NamedValues(*(('other',1),('local',2),('netmgmt',3),('icmp',4),('egp',5),('ggp',6),('hello',7),('rip',8),('isIs',9),('esIs',10),('ciscoIgrp',11),('bbnSpfIgp',12),('ospf',13),('bgp',14),('idpr',15),('ciscoEigrp',16)))
_MplsVpnVrfRouteProto_Type.__name__=_E
_MplsVpnVrfRouteProto_Object=MibTableColumn
mplsVpnVrfRouteProto=_MplsVpnVrfRouteProto_Object((1,3,6,1,4,1,43,45,1,5,12,3,1,3,1,1,5),_MplsVpnVrfRouteProto_Type())
mplsVpnVrfRouteProto.setMaxAccess(_B)
if mibBuilder.loadTexts:mplsVpnVrfRouteProto.setStatus(_A)
_MplsVpnVrfRouteRowStatus_Type=RowStatus
_MplsVpnVrfRouteRowStatus_Object=MibTableColumn
mplsVpnVrfRouteRowStatus=_MplsVpnVrfRouteRowStatus_Object((1,3,6,1,4,1,43,45,1,5,12,3,1,3,1,1,6),_MplsVpnVrfRouteRowStatus_Type())
mplsVpnVrfRouteRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:mplsVpnVrfRouteRowStatus.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'MplsVpnId':MplsVpnId,'MplsVpnRouteDistinguisher':MplsVpnRouteDistinguisher,'hwMplsVpn':hwMplsVpn,'mplsVpnObjects':mplsVpnObjects,'mplsVpnScalars':mplsVpnScalars,'mplsVpnConfiguredVrfs':mplsVpnConfiguredVrfs,'mplsVpnActiveVrfs':mplsVpnActiveVrfs,'mplsVpnConf':mplsVpnConf,'mplsVpnInterfaceConfTable':mplsVpnInterfaceConfTable,'mplsVpnInterfaceConfEntry':mplsVpnInterfaceConfEntry,_G:mplsVpnInterfaceConfIndex,'mplsVpnInterfaceLabelEdgeType':mplsVpnInterfaceLabelEdgeType,'mplsVpnInterfaceVpnClassification':mplsVpnInterfaceVpnClassification,'mplsVpnInterfaceIpAddress':mplsVpnInterfaceIpAddress,'mplsVpnInterfaceIpAddressMask':mplsVpnInterfaceIpAddressMask,'mplsVpnInterfaceConfRowStatus':mplsVpnInterfaceConfRowStatus,'mplsVpnVrfConfTable':mplsVpnVrfConfTable,'mplsVpnVrfConfEntry':mplsVpnVrfConfEntry,_F:mplsVpnVrfName,'mplsVpnVrfRouteDistinguisher':mplsVpnVrfRouteDistinguisher,'mplsVpnVrfNetPrefixType':mplsVpnVrfNetPrefixType,'mplsVpnVrfNetPrefix':mplsVpnVrfNetPrefix,'mplsVpnVrfIpRouteRedistributeConn':mplsVpnVrfIpRouteRedistributeConn,'mplsVpnVrfIpRouteRedistributeStatic':mplsVpnVrfIpRouteRedistributeStatic,'mplsVpnVrfIpRouteRedistributeRip':mplsVpnVrfIpRouteRedistributeRip,'mplsVpnVrfConfHighRouteThreshold':mplsVpnVrfConfHighRouteThreshold,'mplsVpnVrfConfIsWarnOnly':mplsVpnVrfConfIsWarnOnly,'mplsVpnVrfConfMaxRoutes':mplsVpnVrfConfMaxRoutes,'mplsVpnVrfConfRowStatus':mplsVpnVrfConfRowStatus,'mplsVpnVrfRouteTargetTable':mplsVpnVrfRouteTargetTable,'mplsVpnVrfRouteTargetEntry':mplsVpnVrfRouteTargetEntry,_H:mplsVpnVrfRouteTarget,_I:mplsVpnVrfRouteTargetType,'mplsVpnVrfRouteTargetRowStatus':mplsVpnVrfRouteTargetRowStatus,'mplsVpnVrfBgpNbrAddrTable':mplsVpnVrfBgpNbrAddrTable,'mplsVpnVrfBgpNbrAddrEntry':mplsVpnVrfBgpNbrAddrEntry,_J:mplsVpnVrfBgpNbrAddr,'mplsVpnVrfBgpNbrRole':mplsVpnVrfBgpNbrRole,'mplsVpnVrfBgpNbrType':mplsVpnVrfBgpNbrType,'mplsVpnVrfBgpNbrAsNumber':mplsVpnVrfBgpNbrAsNumber,'mplsVpnVrfBgpNbrAdminStatus':mplsVpnVrfBgpNbrAdminStatus,'mplsVpnVrfBgpNbrRowStatus':mplsVpnVrfBgpNbrRowStatus,'mplsVpnRoute':mplsVpnRoute,'mplsVpnVrfRouteTable':mplsVpnVrfRouteTable,'mplsVpnVrfRouteEntry':mplsVpnVrfRouteEntry,_K:mplsVpnVrfRouteDest,_L:mplsVpnVrfRouteMask,_M:mplsVpnVrfRouteNextHop,'mplsVpnVrfRouteIfIndex':mplsVpnVrfRouteIfIndex,'mplsVpnVrfRouteProto':mplsVpnVrfRouteProto,'mplsVpnVrfRouteRowStatus':mplsVpnVrfRouteRowStatus})