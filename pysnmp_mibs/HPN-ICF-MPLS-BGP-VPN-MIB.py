_M='hpnicfmplsVpnVrfRouteNextHop'
_L='hpnicfmplsVpnVrfRouteMask'
_K='hpnicfmplsVpnVrfRouteDest'
_J='hpnicfmplsVpnVrfBgpNbrAddr'
_I='hpnicfmplsVpnVrfRouteTargetType'
_H='hpnicfmplsVpnVrfRouteTarget'
_G='hpnicfmplsVpnInterfaceConfIndex'
_F='hpnicfmplsVpnVrfName'
_E='Integer32'
_D='HPN-ICF-MPLS-BGP-VPN-MIB'
_C='read-only'
_B='read-create'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hpnicfMpls,=mibBuilder.importSymbols('HPN-ICF-OID-MIB','hpnicfMpls')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,experimental,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','experimental','iso')
DisplayString,PhysAddress,RowStatus,StorageType,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','StorageType','TextualConvention','TimeStamp','TruthValue')
hpnicfMplsVpn=ModuleIdentity((1,3,6,1,4,1,11,2,14,11,15,8,12,3))
if mibBuilder.loadTexts:hpnicfMplsVpn.setRevisions(('2001-07-20 12:00','2001-07-17 12:00','2001-07-10 12:00','2001-06-19 12:00','2001-05-30 12:00','2000-09-30 12:00'))
class HpnicfMplsVpnId(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
class HpnicfMplsVpnRouteDistinguisher(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,256))
_HpnicfmplsVpnObjects_ObjectIdentity=ObjectIdentity
hpnicfmplsVpnObjects=_HpnicfmplsVpnObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,8,12,3,1))
_HpnicfmplsVpnScalars_ObjectIdentity=ObjectIdentity
hpnicfmplsVpnScalars=_HpnicfmplsVpnScalars_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,8,12,3,1,1))
_HpnicfmplsVpnConfiguredVrfs_Type=Unsigned32
_HpnicfmplsVpnConfiguredVrfs_Object=MibScalar
hpnicfmplsVpnConfiguredVrfs=_HpnicfmplsVpnConfiguredVrfs_Object((1,3,6,1,4,1,11,2,14,11,15,8,12,3,1,1,1),_HpnicfmplsVpnConfiguredVrfs_Type())
hpnicfmplsVpnConfiguredVrfs.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfmplsVpnConfiguredVrfs.setStatus(_A)
_HpnicfmplsVpnActiveVrfs_Type=Unsigned32
_HpnicfmplsVpnActiveVrfs_Object=MibScalar
hpnicfmplsVpnActiveVrfs=_HpnicfmplsVpnActiveVrfs_Object((1,3,6,1,4,1,11,2,14,11,15,8,12,3,1,1,2),_HpnicfmplsVpnActiveVrfs_Type())
hpnicfmplsVpnActiveVrfs.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfmplsVpnActiveVrfs.setStatus(_A)
_HpnicfmplsVpnConf_ObjectIdentity=ObjectIdentity
hpnicfmplsVpnConf=_HpnicfmplsVpnConf_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,8,12,3,1,2))
_HpnicfmplsVpnInterfaceConfTable_Object=MibTable
hpnicfmplsVpnInterfaceConfTable=_HpnicfmplsVpnInterfaceConfTable_Object((1,3,6,1,4,1,11,2,14,11,15,8,12,3,1,2,1))
if mibBuilder.loadTexts:hpnicfmplsVpnInterfaceConfTable.setStatus(_A)
_HpnicfmplsVpnInterfaceConfEntry_Object=MibTableRow
hpnicfmplsVpnInterfaceConfEntry=_HpnicfmplsVpnInterfaceConfEntry_Object((1,3,6,1,4,1,11,2,14,11,15,8,12,3,1,2,1,1))
hpnicfmplsVpnInterfaceConfEntry.setIndexNames((0,_D,_F),(0,_D,_G))
if mibBuilder.loadTexts:hpnicfmplsVpnInterfaceConfEntry.setStatus(_A)
_HpnicfmplsVpnInterfaceConfIndex_Type=InterfaceIndex
_HpnicfmplsVpnInterfaceConfIndex_Object=MibTableColumn
hpnicfmplsVpnInterfaceConfIndex=_HpnicfmplsVpnInterfaceConfIndex_Object((1,3,6,1,4,1,11,2,14,11,15,8,12,3,1,2,1,1,1),_HpnicfmplsVpnInterfaceConfIndex_Type())
hpnicfmplsVpnInterfaceConfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfmplsVpnInterfaceConfIndex.setStatus(_A)
class _HpnicfmplsVpnInterfaceLabelEdgeType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('providerEdge',1),('customerEdge',2)))
_HpnicfmplsVpnInterfaceLabelEdgeType_Type.__name__=_E
_HpnicfmplsVpnInterfaceLabelEdgeType_Object=MibTableColumn
hpnicfmplsVpnInterfaceLabelEdgeType=_HpnicfmplsVpnInterfaceLabelEdgeType_Object((1,3,6,1,4,1,11,2,14,11,15,8,12,3,1,2,1,1,2),_HpnicfmplsVpnInterfaceLabelEdgeType_Type())
hpnicfmplsVpnInterfaceLabelEdgeType.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfmplsVpnInterfaceLabelEdgeType.setStatus(_A)
class _HpnicfmplsVpnInterfaceVpnClassification_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('carrierOfCarrier',1),('enterprise',2),('interProvider',3)))
_HpnicfmplsVpnInterfaceVpnClassification_Type.__name__=_E
_HpnicfmplsVpnInterfaceVpnClassification_Object=MibTableColumn
hpnicfmplsVpnInterfaceVpnClassification=_HpnicfmplsVpnInterfaceVpnClassification_Object((1,3,6,1,4,1,11,2,14,11,15,8,12,3,1,2,1,1,3),_HpnicfmplsVpnInterfaceVpnClassification_Type())
hpnicfmplsVpnInterfaceVpnClassification.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfmplsVpnInterfaceVpnClassification.setStatus(_A)
_HpnicfmplsVpnInterfaceIpAddress_Type=InetAddress
_HpnicfmplsVpnInterfaceIpAddress_Object=MibTableColumn
hpnicfmplsVpnInterfaceIpAddress=_HpnicfmplsVpnInterfaceIpAddress_Object((1,3,6,1,4,1,11,2,14,11,15,8,12,3,1,2,1,1,4),_HpnicfmplsVpnInterfaceIpAddress_Type())
hpnicfmplsVpnInterfaceIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfmplsVpnInterfaceIpAddress.setStatus(_A)
_HpnicfmplsVpnInterfaceIpAddressMask_Type=InetAddress
_HpnicfmplsVpnInterfaceIpAddressMask_Object=MibTableColumn
hpnicfmplsVpnInterfaceIpAddressMask=_HpnicfmplsVpnInterfaceIpAddressMask_Object((1,3,6,1,4,1,11,2,14,11,15,8,12,3,1,2,1,1,5),_HpnicfmplsVpnInterfaceIpAddressMask_Type())
hpnicfmplsVpnInterfaceIpAddressMask.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfmplsVpnInterfaceIpAddressMask.setStatus(_A)
_HpnicfmplsVpnInterfaceConfRowStatus_Type=RowStatus
_HpnicfmplsVpnInterfaceConfRowStatus_Object=MibTableColumn
hpnicfmplsVpnInterfaceConfRowStatus=_HpnicfmplsVpnInterfaceConfRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,8,12,3,1,2,1,1,6),_HpnicfmplsVpnInterfaceConfRowStatus_Type())
hpnicfmplsVpnInterfaceConfRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfmplsVpnInterfaceConfRowStatus.setStatus(_A)
_HpnicfmplsVpnVrfConfTable_Object=MibTable
hpnicfmplsVpnVrfConfTable=_HpnicfmplsVpnVrfConfTable_Object((1,3,6,1,4,1,11,2,14,11,15,8,12,3,1,2,2))
if mibBuilder.loadTexts:hpnicfmplsVpnVrfConfTable.setStatus(_A)
_HpnicfmplsVpnVrfConfEntry_Object=MibTableRow
hpnicfmplsVpnVrfConfEntry=_HpnicfmplsVpnVrfConfEntry_Object((1,3,6,1,4,1,11,2,14,11,15,8,12,3,1,2,2,1))
hpnicfmplsVpnVrfConfEntry.setIndexNames((0,_D,_F))
if mibBuilder.loadTexts:hpnicfmplsVpnVrfConfEntry.setStatus(_A)
_HpnicfmplsVpnVrfName_Type=HpnicfMplsVpnId
_HpnicfmplsVpnVrfName_Object=MibTableColumn
hpnicfmplsVpnVrfName=_HpnicfmplsVpnVrfName_Object((1,3,6,1,4,1,11,2,14,11,15,8,12,3,1,2,2,1,1),_HpnicfmplsVpnVrfName_Type())
hpnicfmplsVpnVrfName.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfmplsVpnVrfName.setStatus(_A)
_HpnicfmplsVpnVrfRouteDistinguisher_Type=HpnicfMplsVpnRouteDistinguisher
_HpnicfmplsVpnVrfRouteDistinguisher_Object=MibTableColumn
hpnicfmplsVpnVrfRouteDistinguisher=_HpnicfmplsVpnVrfRouteDistinguisher_Object((1,3,6,1,4,1,11,2,14,11,15,8,12,3,1,2,2,1,2),_HpnicfmplsVpnVrfRouteDistinguisher_Type())
hpnicfmplsVpnVrfRouteDistinguisher.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfmplsVpnVrfRouteDistinguisher.setStatus(_A)
class _HpnicfmplsVpnVrfNetPrefixType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('other',1),('rip',2),('ospf',3),('isis',4),('bgp',5),('static',6)))
_HpnicfmplsVpnVrfNetPrefixType_Type.__name__=_E
_HpnicfmplsVpnVrfNetPrefixType_Object=MibTableColumn
hpnicfmplsVpnVrfNetPrefixType=_HpnicfmplsVpnVrfNetPrefixType_Object((1,3,6,1,4,1,11,2,14,11,15,8,12,3,1,2,2,1,3),_HpnicfmplsVpnVrfNetPrefixType_Type())
hpnicfmplsVpnVrfNetPrefixType.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfmplsVpnVrfNetPrefixType.setStatus(_A)
_HpnicfmplsVpnVrfNetPrefix_Type=InetAddress
_HpnicfmplsVpnVrfNetPrefix_Object=MibTableColumn
hpnicfmplsVpnVrfNetPrefix=_HpnicfmplsVpnVrfNetPrefix_Object((1,3,6,1,4,1,11,2,14,11,15,8,12,3,1,2,2,1,4),_HpnicfmplsVpnVrfNetPrefix_Type())
hpnicfmplsVpnVrfNetPrefix.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfmplsVpnVrfNetPrefix.setStatus(_A)
_HpnicfmplsVpnVrfIpRouteRedistributeConn_Type=TruthValue
_HpnicfmplsVpnVrfIpRouteRedistributeConn_Object=MibTableColumn
hpnicfmplsVpnVrfIpRouteRedistributeConn=_HpnicfmplsVpnVrfIpRouteRedistributeConn_Object((1,3,6,1,4,1,11,2,14,11,15,8,12,3,1,2,2,1,5),_HpnicfmplsVpnVrfIpRouteRedistributeConn_Type())
hpnicfmplsVpnVrfIpRouteRedistributeConn.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfmplsVpnVrfIpRouteRedistributeConn.setStatus(_A)
_HpnicfmplsVpnVrfIpRouteRedistributeStatic_Type=TruthValue
_HpnicfmplsVpnVrfIpRouteRedistributeStatic_Object=MibTableColumn
hpnicfmplsVpnVrfIpRouteRedistributeStatic=_HpnicfmplsVpnVrfIpRouteRedistributeStatic_Object((1,3,6,1,4,1,11,2,14,11,15,8,12,3,1,2,2,1,6),_HpnicfmplsVpnVrfIpRouteRedistributeStatic_Type())
hpnicfmplsVpnVrfIpRouteRedistributeStatic.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfmplsVpnVrfIpRouteRedistributeStatic.setStatus(_A)
_HpnicfmplsVpnVrfIpRouteRedistributeRip_Type=TruthValue
_HpnicfmplsVpnVrfIpRouteRedistributeRip_Object=MibTableColumn
hpnicfmplsVpnVrfIpRouteRedistributeRip=_HpnicfmplsVpnVrfIpRouteRedistributeRip_Object((1,3,6,1,4,1,11,2,14,11,15,8,12,3,1,2,2,1,7),_HpnicfmplsVpnVrfIpRouteRedistributeRip_Type())
hpnicfmplsVpnVrfIpRouteRedistributeRip.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfmplsVpnVrfIpRouteRedistributeRip.setStatus(_A)
_HpnicfmplsVpnVrfConfHighRouteThreshold_Type=Unsigned32
_HpnicfmplsVpnVrfConfHighRouteThreshold_Object=MibTableColumn
hpnicfmplsVpnVrfConfHighRouteThreshold=_HpnicfmplsVpnVrfConfHighRouteThreshold_Object((1,3,6,1,4,1,11,2,14,11,15,8,12,3,1,2,2,1,8),_HpnicfmplsVpnVrfConfHighRouteThreshold_Type())
hpnicfmplsVpnVrfConfHighRouteThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfmplsVpnVrfConfHighRouteThreshold.setStatus(_A)
_HpnicfmplsVpnVrfConfIsWarnOnly_Type=TruthValue
_HpnicfmplsVpnVrfConfIsWarnOnly_Object=MibTableColumn
hpnicfmplsVpnVrfConfIsWarnOnly=_HpnicfmplsVpnVrfConfIsWarnOnly_Object((1,3,6,1,4,1,11,2,14,11,15,8,12,3,1,2,2,1,9),_HpnicfmplsVpnVrfConfIsWarnOnly_Type())
hpnicfmplsVpnVrfConfIsWarnOnly.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfmplsVpnVrfConfIsWarnOnly.setStatus(_A)
_HpnicfmplsVpnVrfConfMaxRoutes_Type=Unsigned32
_HpnicfmplsVpnVrfConfMaxRoutes_Object=MibTableColumn
hpnicfmplsVpnVrfConfMaxRoutes=_HpnicfmplsVpnVrfConfMaxRoutes_Object((1,3,6,1,4,1,11,2,14,11,15,8,12,3,1,2,2,1,10),_HpnicfmplsVpnVrfConfMaxRoutes_Type())
hpnicfmplsVpnVrfConfMaxRoutes.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfmplsVpnVrfConfMaxRoutes.setStatus(_A)
_HpnicfmplsVpnVrfConfRowStatus_Type=RowStatus
_HpnicfmplsVpnVrfConfRowStatus_Object=MibTableColumn
hpnicfmplsVpnVrfConfRowStatus=_HpnicfmplsVpnVrfConfRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,8,12,3,1,2,2,1,11),_HpnicfmplsVpnVrfConfRowStatus_Type())
hpnicfmplsVpnVrfConfRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfmplsVpnVrfConfRowStatus.setStatus(_A)
_HpnicfmplsVpnVrfRouteTargetTable_Object=MibTable
hpnicfmplsVpnVrfRouteTargetTable=_HpnicfmplsVpnVrfRouteTargetTable_Object((1,3,6,1,4,1,11,2,14,11,15,8,12,3,1,2,3))
if mibBuilder.loadTexts:hpnicfmplsVpnVrfRouteTargetTable.setStatus(_A)
_HpnicfmplsVpnVrfRouteTargetEntry_Object=MibTableRow
hpnicfmplsVpnVrfRouteTargetEntry=_HpnicfmplsVpnVrfRouteTargetEntry_Object((1,3,6,1,4,1,11,2,14,11,15,8,12,3,1,2,3,1))
hpnicfmplsVpnVrfRouteTargetEntry.setIndexNames((0,_D,_F),(0,_D,_H),(0,_D,_I))
if mibBuilder.loadTexts:hpnicfmplsVpnVrfRouteTargetEntry.setStatus(_A)
_HpnicfmplsVpnVrfRouteTarget_Type=HpnicfMplsVpnRouteDistinguisher
_HpnicfmplsVpnVrfRouteTarget_Object=MibTableColumn
hpnicfmplsVpnVrfRouteTarget=_HpnicfmplsVpnVrfRouteTarget_Object((1,3,6,1,4,1,11,2,14,11,15,8,12,3,1,2,3,1,1),_HpnicfmplsVpnVrfRouteTarget_Type())
hpnicfmplsVpnVrfRouteTarget.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfmplsVpnVrfRouteTarget.setStatus(_A)
class _HpnicfmplsVpnVrfRouteTargetType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('import',1),('export',2)))
_HpnicfmplsVpnVrfRouteTargetType_Type.__name__=_E
_HpnicfmplsVpnVrfRouteTargetType_Object=MibTableColumn
hpnicfmplsVpnVrfRouteTargetType=_HpnicfmplsVpnVrfRouteTargetType_Object((1,3,6,1,4,1,11,2,14,11,15,8,12,3,1,2,3,1,2),_HpnicfmplsVpnVrfRouteTargetType_Type())
hpnicfmplsVpnVrfRouteTargetType.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfmplsVpnVrfRouteTargetType.setStatus(_A)
_HpnicfmplsVpnVrfRouteTargetRowStatus_Type=RowStatus
_HpnicfmplsVpnVrfRouteTargetRowStatus_Object=MibTableColumn
hpnicfmplsVpnVrfRouteTargetRowStatus=_HpnicfmplsVpnVrfRouteTargetRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,8,12,3,1,2,3,1,3),_HpnicfmplsVpnVrfRouteTargetRowStatus_Type())
hpnicfmplsVpnVrfRouteTargetRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfmplsVpnVrfRouteTargetRowStatus.setStatus(_A)
_HpnicfmplsVpnVrfBgpNbrAddrTable_Object=MibTable
hpnicfmplsVpnVrfBgpNbrAddrTable=_HpnicfmplsVpnVrfBgpNbrAddrTable_Object((1,3,6,1,4,1,11,2,14,11,15,8,12,3,1,2,4))
if mibBuilder.loadTexts:hpnicfmplsVpnVrfBgpNbrAddrTable.setStatus(_A)
_HpnicfmplsVpnVrfBgpNbrAddrEntry_Object=MibTableRow
hpnicfmplsVpnVrfBgpNbrAddrEntry=_HpnicfmplsVpnVrfBgpNbrAddrEntry_Object((1,3,6,1,4,1,11,2,14,11,15,8,12,3,1,2,4,1))
hpnicfmplsVpnVrfBgpNbrAddrEntry.setIndexNames((0,_D,_F),(0,_D,_J))
if mibBuilder.loadTexts:hpnicfmplsVpnVrfBgpNbrAddrEntry.setStatus(_A)
_HpnicfmplsVpnVrfBgpNbrAddr_Type=InetAddress
_HpnicfmplsVpnVrfBgpNbrAddr_Object=MibTableColumn
hpnicfmplsVpnVrfBgpNbrAddr=_HpnicfmplsVpnVrfBgpNbrAddr_Object((1,3,6,1,4,1,11,2,14,11,15,8,12,3,1,2,4,1,1),_HpnicfmplsVpnVrfBgpNbrAddr_Type())
hpnicfmplsVpnVrfBgpNbrAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfmplsVpnVrfBgpNbrAddr.setStatus(_A)
class _HpnicfmplsVpnVrfBgpNbrRole_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('ce',1),('pe',2)))
_HpnicfmplsVpnVrfBgpNbrRole_Type.__name__=_E
_HpnicfmplsVpnVrfBgpNbrRole_Object=MibTableColumn
hpnicfmplsVpnVrfBgpNbrRole=_HpnicfmplsVpnVrfBgpNbrRole_Object((1,3,6,1,4,1,11,2,14,11,15,8,12,3,1,2,4,1,2),_HpnicfmplsVpnVrfBgpNbrRole_Type())
hpnicfmplsVpnVrfBgpNbrRole.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfmplsVpnVrfBgpNbrRole.setStatus(_A)
_HpnicfmplsVpnVrfBgpNbrType_Type=InetAddressType
_HpnicfmplsVpnVrfBgpNbrType_Object=MibTableColumn
hpnicfmplsVpnVrfBgpNbrType=_HpnicfmplsVpnVrfBgpNbrType_Object((1,3,6,1,4,1,11,2,14,11,15,8,12,3,1,2,4,1,3),_HpnicfmplsVpnVrfBgpNbrType_Type())
hpnicfmplsVpnVrfBgpNbrType.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfmplsVpnVrfBgpNbrType.setStatus(_A)
_HpnicfmplsVpnVrfBgpNbrAsNumber_Type=Unsigned32
_HpnicfmplsVpnVrfBgpNbrAsNumber_Object=MibTableColumn
hpnicfmplsVpnVrfBgpNbrAsNumber=_HpnicfmplsVpnVrfBgpNbrAsNumber_Object((1,3,6,1,4,1,11,2,14,11,15,8,12,3,1,2,4,1,4),_HpnicfmplsVpnVrfBgpNbrAsNumber_Type())
hpnicfmplsVpnVrfBgpNbrAsNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfmplsVpnVrfBgpNbrAsNumber.setStatus(_A)
class _HpnicfmplsVpnVrfBgpNbrAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('mplsVpnVrfBgpNbrSetUp',1),('mplsVpnVrfBgpNbrSetDown',2)))
_HpnicfmplsVpnVrfBgpNbrAdminStatus_Type.__name__=_E
_HpnicfmplsVpnVrfBgpNbrAdminStatus_Object=MibTableColumn
hpnicfmplsVpnVrfBgpNbrAdminStatus=_HpnicfmplsVpnVrfBgpNbrAdminStatus_Object((1,3,6,1,4,1,11,2,14,11,15,8,12,3,1,2,4,1,5),_HpnicfmplsVpnVrfBgpNbrAdminStatus_Type())
hpnicfmplsVpnVrfBgpNbrAdminStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfmplsVpnVrfBgpNbrAdminStatus.setStatus(_A)
_HpnicfmplsVpnVrfBgpNbrRowStatus_Type=RowStatus
_HpnicfmplsVpnVrfBgpNbrRowStatus_Object=MibTableColumn
hpnicfmplsVpnVrfBgpNbrRowStatus=_HpnicfmplsVpnVrfBgpNbrRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,8,12,3,1,2,4,1,6),_HpnicfmplsVpnVrfBgpNbrRowStatus_Type())
hpnicfmplsVpnVrfBgpNbrRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfmplsVpnVrfBgpNbrRowStatus.setStatus(_A)
_HpnicfmplsVpnRoute_ObjectIdentity=ObjectIdentity
hpnicfmplsVpnRoute=_HpnicfmplsVpnRoute_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,8,12,3,1,3))
_HpnicfmplsVpnVrfRouteTable_Object=MibTable
hpnicfmplsVpnVrfRouteTable=_HpnicfmplsVpnVrfRouteTable_Object((1,3,6,1,4,1,11,2,14,11,15,8,12,3,1,3,1))
if mibBuilder.loadTexts:hpnicfmplsVpnVrfRouteTable.setStatus(_A)
_HpnicfmplsVpnVrfRouteEntry_Object=MibTableRow
hpnicfmplsVpnVrfRouteEntry=_HpnicfmplsVpnVrfRouteEntry_Object((1,3,6,1,4,1,11,2,14,11,15,8,12,3,1,3,1,1))
hpnicfmplsVpnVrfRouteEntry.setIndexNames((0,_D,_F),(0,_D,_K),(0,_D,_L),(0,_D,_M))
if mibBuilder.loadTexts:hpnicfmplsVpnVrfRouteEntry.setStatus(_A)
_HpnicfmplsVpnVrfRouteDest_Type=InetAddress
_HpnicfmplsVpnVrfRouteDest_Object=MibTableColumn
hpnicfmplsVpnVrfRouteDest=_HpnicfmplsVpnVrfRouteDest_Object((1,3,6,1,4,1,11,2,14,11,15,8,12,3,1,3,1,1,1),_HpnicfmplsVpnVrfRouteDest_Type())
hpnicfmplsVpnVrfRouteDest.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfmplsVpnVrfRouteDest.setStatus(_A)
_HpnicfmplsVpnVrfRouteMask_Type=InetAddress
_HpnicfmplsVpnVrfRouteMask_Object=MibTableColumn
hpnicfmplsVpnVrfRouteMask=_HpnicfmplsVpnVrfRouteMask_Object((1,3,6,1,4,1,11,2,14,11,15,8,12,3,1,3,1,1,2),_HpnicfmplsVpnVrfRouteMask_Type())
hpnicfmplsVpnVrfRouteMask.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfmplsVpnVrfRouteMask.setStatus(_A)
_HpnicfmplsVpnVrfRouteNextHop_Type=InetAddress
_HpnicfmplsVpnVrfRouteNextHop_Object=MibTableColumn
hpnicfmplsVpnVrfRouteNextHop=_HpnicfmplsVpnVrfRouteNextHop_Object((1,3,6,1,4,1,11,2,14,11,15,8,12,3,1,3,1,1,3),_HpnicfmplsVpnVrfRouteNextHop_Type())
hpnicfmplsVpnVrfRouteNextHop.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfmplsVpnVrfRouteNextHop.setStatus(_A)
_HpnicfmplsVpnVrfRouteIfIndex_Type=InterfaceIndex
_HpnicfmplsVpnVrfRouteIfIndex_Object=MibTableColumn
hpnicfmplsVpnVrfRouteIfIndex=_HpnicfmplsVpnVrfRouteIfIndex_Object((1,3,6,1,4,1,11,2,14,11,15,8,12,3,1,3,1,1,4),_HpnicfmplsVpnVrfRouteIfIndex_Type())
hpnicfmplsVpnVrfRouteIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfmplsVpnVrfRouteIfIndex.setStatus(_A)
class _HpnicfmplsVpnVrfRouteProto_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16)));namedValues=NamedValues(*(('other',1),('local',2),('netmgmt',3),('icmp',4),('egp',5),('ggp',6),('hello',7),('rip',8),('isIs',9),('esIs',10),('ciscoIgrp',11),('bbnSpfIgp',12),('ospf',13),('bgp',14),('idpr',15),('ciscoEigrp',16)))
_HpnicfmplsVpnVrfRouteProto_Type.__name__=_E
_HpnicfmplsVpnVrfRouteProto_Object=MibTableColumn
hpnicfmplsVpnVrfRouteProto=_HpnicfmplsVpnVrfRouteProto_Object((1,3,6,1,4,1,11,2,14,11,15,8,12,3,1,3,1,1,5),_HpnicfmplsVpnVrfRouteProto_Type())
hpnicfmplsVpnVrfRouteProto.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfmplsVpnVrfRouteProto.setStatus(_A)
_HpnicfmplsVpnVrfRouteRowStatus_Type=RowStatus
_HpnicfmplsVpnVrfRouteRowStatus_Object=MibTableColumn
hpnicfmplsVpnVrfRouteRowStatus=_HpnicfmplsVpnVrfRouteRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,8,12,3,1,3,1,1,6),_HpnicfmplsVpnVrfRouteRowStatus_Type())
hpnicfmplsVpnVrfRouteRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfmplsVpnVrfRouteRowStatus.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'HpnicfMplsVpnId':HpnicfMplsVpnId,'HpnicfMplsVpnRouteDistinguisher':HpnicfMplsVpnRouteDistinguisher,'hpnicfMplsVpn':hpnicfMplsVpn,'hpnicfmplsVpnObjects':hpnicfmplsVpnObjects,'hpnicfmplsVpnScalars':hpnicfmplsVpnScalars,'hpnicfmplsVpnConfiguredVrfs':hpnicfmplsVpnConfiguredVrfs,'hpnicfmplsVpnActiveVrfs':hpnicfmplsVpnActiveVrfs,'hpnicfmplsVpnConf':hpnicfmplsVpnConf,'hpnicfmplsVpnInterfaceConfTable':hpnicfmplsVpnInterfaceConfTable,'hpnicfmplsVpnInterfaceConfEntry':hpnicfmplsVpnInterfaceConfEntry,_G:hpnicfmplsVpnInterfaceConfIndex,'hpnicfmplsVpnInterfaceLabelEdgeType':hpnicfmplsVpnInterfaceLabelEdgeType,'hpnicfmplsVpnInterfaceVpnClassification':hpnicfmplsVpnInterfaceVpnClassification,'hpnicfmplsVpnInterfaceIpAddress':hpnicfmplsVpnInterfaceIpAddress,'hpnicfmplsVpnInterfaceIpAddressMask':hpnicfmplsVpnInterfaceIpAddressMask,'hpnicfmplsVpnInterfaceConfRowStatus':hpnicfmplsVpnInterfaceConfRowStatus,'hpnicfmplsVpnVrfConfTable':hpnicfmplsVpnVrfConfTable,'hpnicfmplsVpnVrfConfEntry':hpnicfmplsVpnVrfConfEntry,_F:hpnicfmplsVpnVrfName,'hpnicfmplsVpnVrfRouteDistinguisher':hpnicfmplsVpnVrfRouteDistinguisher,'hpnicfmplsVpnVrfNetPrefixType':hpnicfmplsVpnVrfNetPrefixType,'hpnicfmplsVpnVrfNetPrefix':hpnicfmplsVpnVrfNetPrefix,'hpnicfmplsVpnVrfIpRouteRedistributeConn':hpnicfmplsVpnVrfIpRouteRedistributeConn,'hpnicfmplsVpnVrfIpRouteRedistributeStatic':hpnicfmplsVpnVrfIpRouteRedistributeStatic,'hpnicfmplsVpnVrfIpRouteRedistributeRip':hpnicfmplsVpnVrfIpRouteRedistributeRip,'hpnicfmplsVpnVrfConfHighRouteThreshold':hpnicfmplsVpnVrfConfHighRouteThreshold,'hpnicfmplsVpnVrfConfIsWarnOnly':hpnicfmplsVpnVrfConfIsWarnOnly,'hpnicfmplsVpnVrfConfMaxRoutes':hpnicfmplsVpnVrfConfMaxRoutes,'hpnicfmplsVpnVrfConfRowStatus':hpnicfmplsVpnVrfConfRowStatus,'hpnicfmplsVpnVrfRouteTargetTable':hpnicfmplsVpnVrfRouteTargetTable,'hpnicfmplsVpnVrfRouteTargetEntry':hpnicfmplsVpnVrfRouteTargetEntry,_H:hpnicfmplsVpnVrfRouteTarget,_I:hpnicfmplsVpnVrfRouteTargetType,'hpnicfmplsVpnVrfRouteTargetRowStatus':hpnicfmplsVpnVrfRouteTargetRowStatus,'hpnicfmplsVpnVrfBgpNbrAddrTable':hpnicfmplsVpnVrfBgpNbrAddrTable,'hpnicfmplsVpnVrfBgpNbrAddrEntry':hpnicfmplsVpnVrfBgpNbrAddrEntry,_J:hpnicfmplsVpnVrfBgpNbrAddr,'hpnicfmplsVpnVrfBgpNbrRole':hpnicfmplsVpnVrfBgpNbrRole,'hpnicfmplsVpnVrfBgpNbrType':hpnicfmplsVpnVrfBgpNbrType,'hpnicfmplsVpnVrfBgpNbrAsNumber':hpnicfmplsVpnVrfBgpNbrAsNumber,'hpnicfmplsVpnVrfBgpNbrAdminStatus':hpnicfmplsVpnVrfBgpNbrAdminStatus,'hpnicfmplsVpnVrfBgpNbrRowStatus':hpnicfmplsVpnVrfBgpNbrRowStatus,'hpnicfmplsVpnRoute':hpnicfmplsVpnRoute,'hpnicfmplsVpnVrfRouteTable':hpnicfmplsVpnVrfRouteTable,'hpnicfmplsVpnVrfRouteEntry':hpnicfmplsVpnVrfRouteEntry,_K:hpnicfmplsVpnVrfRouteDest,_L:hpnicfmplsVpnVrfRouteMask,_M:hpnicfmplsVpnVrfRouteNextHop,'hpnicfmplsVpnVrfRouteIfIndex':hpnicfmplsVpnVrfRouteIfIndex,'hpnicfmplsVpnVrfRouteProto':hpnicfmplsVpnVrfRouteProto,'hpnicfmplsVpnVrfRouteRowStatus':hpnicfmplsVpnVrfRouteRowStatus})