_W='brocadeVcsObjectsGroup'
_V='vcsFabricIslIsTrunk'
_U='vcsFabricIslBW'
_T='vcsFabricIslNbrName'
_S='vcsFabricIslNbrWWN'
_R='vcsFabricIslNbrIntfName'
_Q='vcsFabricIslIntfName'
_P='vcsClusterCondition'
_O='vcsNumNodesInCluster'
_N='vcsVirtualIpV6OperStatus'
_M='vcsVirtualIpV4OperStatus'
_L='vcsVirtualIpInterfaceId'
_K='vcsVirtualIpAssociatedRbridgeId'
_J='vcsVirtualIpV6Address'
_I='vcsVirtualIpV4Address'
_H='vcsIdentifier'
_G='vcsModeOfOperation'
_F='vcsConfigMode'
_E='vcsFabricIslIndex'
_D='Integer32'
_C='read-only'
_B='BROCADE-VCS-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
bcsiModules,=mibBuilder.importSymbols('Brocade-REG-MIB','bcsiModules')
FcWwn,=mibBuilder.importSymbols('Brocade-TC','FcWwn')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
brocadeVcsMIB=ModuleIdentity((1,3,6,1,4,1,1588,3,1,6))
if mibBuilder.loadTexts:brocadeVcsMIB.setRevisions(('2015-04-08 00:00',))
class VcsConfigMode(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('local',1),('distributed',2)))
class VcsOperationMode(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('fabricCluster',1),('logicalChassis',2)))
class VcsIdentifier(TextualConvention,Unsigned32):status=_A;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8192))
class VcsRbridgeId(TextualConvention,Unsigned32):status=_A;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,239))
class VcsClusterCondition(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('good',1),('degraded',2),('error',3)))
_BrocadeVcsMIBObjects_ObjectIdentity=ObjectIdentity
brocadeVcsMIBObjects=_BrocadeVcsMIBObjects_ObjectIdentity((1,3,6,1,4,1,1588,3,1,6,1))
_VcsConfigMode_Type=VcsConfigMode
_VcsConfigMode_Object=MibScalar
vcsConfigMode=_VcsConfigMode_Object((1,3,6,1,4,1,1588,3,1,6,1,1),_VcsConfigMode_Type())
vcsConfigMode.setMaxAccess(_C)
if mibBuilder.loadTexts:vcsConfigMode.setStatus(_A)
_VcsModeOfOperation_Type=VcsOperationMode
_VcsModeOfOperation_Object=MibScalar
vcsModeOfOperation=_VcsModeOfOperation_Object((1,3,6,1,4,1,1588,3,1,6,1,2),_VcsModeOfOperation_Type())
vcsModeOfOperation.setMaxAccess(_C)
if mibBuilder.loadTexts:vcsModeOfOperation.setStatus(_A)
_VcsIdentifier_Type=VcsIdentifier
_VcsIdentifier_Object=MibScalar
vcsIdentifier=_VcsIdentifier_Object((1,3,6,1,4,1,1588,3,1,6,1,3),_VcsIdentifier_Type())
vcsIdentifier.setMaxAccess(_C)
if mibBuilder.loadTexts:vcsIdentifier.setStatus(_A)
_VcsVirtualIpV4Address_Type=InetAddress
_VcsVirtualIpV4Address_Object=MibScalar
vcsVirtualIpV4Address=_VcsVirtualIpV4Address_Object((1,3,6,1,4,1,1588,3,1,6,1,4),_VcsVirtualIpV4Address_Type())
vcsVirtualIpV4Address.setMaxAccess(_C)
if mibBuilder.loadTexts:vcsVirtualIpV4Address.setStatus(_A)
_VcsVirtualIpV6Address_Type=InetAddress
_VcsVirtualIpV6Address_Object=MibScalar
vcsVirtualIpV6Address=_VcsVirtualIpV6Address_Object((1,3,6,1,4,1,1588,3,1,6,1,5),_VcsVirtualIpV6Address_Type())
vcsVirtualIpV6Address.setMaxAccess(_C)
if mibBuilder.loadTexts:vcsVirtualIpV6Address.setStatus(_A)
_VcsVirtualIpAssociatedRbridgeId_Type=VcsRbridgeId
_VcsVirtualIpAssociatedRbridgeId_Object=MibScalar
vcsVirtualIpAssociatedRbridgeId=_VcsVirtualIpAssociatedRbridgeId_Object((1,3,6,1,4,1,1588,3,1,6,1,6),_VcsVirtualIpAssociatedRbridgeId_Type())
vcsVirtualIpAssociatedRbridgeId.setMaxAccess(_C)
if mibBuilder.loadTexts:vcsVirtualIpAssociatedRbridgeId.setStatus(_A)
_VcsVirtualIpInterfaceId_Type=Unsigned32
_VcsVirtualIpInterfaceId_Object=MibScalar
vcsVirtualIpInterfaceId=_VcsVirtualIpInterfaceId_Object((1,3,6,1,4,1,1588,3,1,6,1,7),_VcsVirtualIpInterfaceId_Type())
vcsVirtualIpInterfaceId.setMaxAccess(_C)
if mibBuilder.loadTexts:vcsVirtualIpInterfaceId.setStatus(_A)
class _VcsVirtualIpV4OperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('up',1),('down',2)))
_VcsVirtualIpV4OperStatus_Type.__name__=_D
_VcsVirtualIpV4OperStatus_Object=MibScalar
vcsVirtualIpV4OperStatus=_VcsVirtualIpV4OperStatus_Object((1,3,6,1,4,1,1588,3,1,6,1,8),_VcsVirtualIpV4OperStatus_Type())
vcsVirtualIpV4OperStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:vcsVirtualIpV4OperStatus.setStatus(_A)
class _VcsVirtualIpV6OperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('up',1),('down',2)))
_VcsVirtualIpV6OperStatus_Type.__name__=_D
_VcsVirtualIpV6OperStatus_Object=MibScalar
vcsVirtualIpV6OperStatus=_VcsVirtualIpV6OperStatus_Object((1,3,6,1,4,1,1588,3,1,6,1,9),_VcsVirtualIpV6OperStatus_Type())
vcsVirtualIpV6OperStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:vcsVirtualIpV6OperStatus.setStatus(_A)
_VcsNumNodesInCluster_Type=Unsigned32
_VcsNumNodesInCluster_Object=MibScalar
vcsNumNodesInCluster=_VcsNumNodesInCluster_Object((1,3,6,1,4,1,1588,3,1,6,1,10),_VcsNumNodesInCluster_Type())
vcsNumNodesInCluster.setMaxAccess(_C)
if mibBuilder.loadTexts:vcsNumNodesInCluster.setStatus(_A)
_VcsClusterCondition_Type=VcsClusterCondition
_VcsClusterCondition_Object=MibScalar
vcsClusterCondition=_VcsClusterCondition_Object((1,3,6,1,4,1,1588,3,1,6,1,11),_VcsClusterCondition_Type())
vcsClusterCondition.setMaxAccess(_C)
if mibBuilder.loadTexts:vcsClusterCondition.setStatus(_A)
_VcsFabricIslTable_Object=MibTable
vcsFabricIslTable=_VcsFabricIslTable_Object((1,3,6,1,4,1,1588,3,1,6,1,12))
if mibBuilder.loadTexts:vcsFabricIslTable.setStatus(_A)
_VcsFabricIslEntry_Object=MibTableRow
vcsFabricIslEntry=_VcsFabricIslEntry_Object((1,3,6,1,4,1,1588,3,1,6,1,12,1))
vcsFabricIslEntry.setIndexNames((0,_B,_E))
if mibBuilder.loadTexts:vcsFabricIslEntry.setStatus(_A)
_VcsFabricIslIndex_Type=Unsigned32
_VcsFabricIslIndex_Object=MibTableColumn
vcsFabricIslIndex=_VcsFabricIslIndex_Object((1,3,6,1,4,1,1588,3,1,6,1,12,1,1),_VcsFabricIslIndex_Type())
vcsFabricIslIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:vcsFabricIslIndex.setStatus(_A)
_VcsFabricIslIntfName_Type=DisplayString
_VcsFabricIslIntfName_Object=MibTableColumn
vcsFabricIslIntfName=_VcsFabricIslIntfName_Object((1,3,6,1,4,1,1588,3,1,6,1,12,1,2),_VcsFabricIslIntfName_Type())
vcsFabricIslIntfName.setMaxAccess(_C)
if mibBuilder.loadTexts:vcsFabricIslIntfName.setStatus(_A)
_VcsFabricIslNbrIntfName_Type=DisplayString
_VcsFabricIslNbrIntfName_Object=MibTableColumn
vcsFabricIslNbrIntfName=_VcsFabricIslNbrIntfName_Object((1,3,6,1,4,1,1588,3,1,6,1,12,1,3),_VcsFabricIslNbrIntfName_Type())
vcsFabricIslNbrIntfName.setMaxAccess(_C)
if mibBuilder.loadTexts:vcsFabricIslNbrIntfName.setStatus(_A)
_VcsFabricIslNbrWWN_Type=FcWwn
_VcsFabricIslNbrWWN_Object=MibTableColumn
vcsFabricIslNbrWWN=_VcsFabricIslNbrWWN_Object((1,3,6,1,4,1,1588,3,1,6,1,12,1,4),_VcsFabricIslNbrWWN_Type())
vcsFabricIslNbrWWN.setMaxAccess(_C)
if mibBuilder.loadTexts:vcsFabricIslNbrWWN.setStatus(_A)
_VcsFabricIslNbrName_Type=DisplayString
_VcsFabricIslNbrName_Object=MibTableColumn
vcsFabricIslNbrName=_VcsFabricIslNbrName_Object((1,3,6,1,4,1,1588,3,1,6,1,12,1,5),_VcsFabricIslNbrName_Type())
vcsFabricIslNbrName.setMaxAccess(_C)
if mibBuilder.loadTexts:vcsFabricIslNbrName.setStatus(_A)
_VcsFabricIslBW_Type=Unsigned32
_VcsFabricIslBW_Object=MibTableColumn
vcsFabricIslBW=_VcsFabricIslBW_Object((1,3,6,1,4,1,1588,3,1,6,1,12,1,6),_VcsFabricIslBW_Type())
vcsFabricIslBW.setMaxAccess(_C)
if mibBuilder.loadTexts:vcsFabricIslBW.setStatus(_A)
if mibBuilder.loadTexts:vcsFabricIslBW.setUnits('megabytes')
_VcsFabricIslIsTrunk_Type=TruthValue
_VcsFabricIslIsTrunk_Object=MibTableColumn
vcsFabricIslIsTrunk=_VcsFabricIslIsTrunk_Object((1,3,6,1,4,1,1588,3,1,6,1,12,1,7),_VcsFabricIslIsTrunk_Type())
vcsFabricIslIsTrunk.setMaxAccess(_C)
if mibBuilder.loadTexts:vcsFabricIslIsTrunk.setStatus(_A)
_BrocadeVcsMIBConformance_ObjectIdentity=ObjectIdentity
brocadeVcsMIBConformance=_BrocadeVcsMIBConformance_ObjectIdentity((1,3,6,1,4,1,1588,3,1,6,2))
_BrocadeVcsConformanceGroups_ObjectIdentity=ObjectIdentity
brocadeVcsConformanceGroups=_BrocadeVcsConformanceGroups_ObjectIdentity((1,3,6,1,4,1,1588,3,1,6,2,1))
_BrocadeVcsCompliances_ObjectIdentity=ObjectIdentity
brocadeVcsCompliances=_BrocadeVcsCompliances_ObjectIdentity((1,3,6,1,4,1,1588,3,1,6,2,2))
brocadeVcsObjectsGroup=ObjectGroup((1,3,6,1,4,1,1588,3,1,6,2,1,1))
brocadeVcsObjectsGroup.setObjects(*((_B,_F),(_B,_G),(_B,_H),(_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_E),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V)))
if mibBuilder.loadTexts:brocadeVcsObjectsGroup.setStatus(_A)
brocadeVcsCompliance=ModuleCompliance((1,3,6,1,4,1,1588,3,1,6,2,2,1))
brocadeVcsCompliance.setObjects((_B,_W))
if mibBuilder.loadTexts:brocadeVcsCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'VcsConfigMode':VcsConfigMode,'VcsOperationMode':VcsOperationMode,'VcsIdentifier':VcsIdentifier,'VcsRbridgeId':VcsRbridgeId,'VcsClusterCondition':VcsClusterCondition,'brocadeVcsMIB':brocadeVcsMIB,'brocadeVcsMIBObjects':brocadeVcsMIBObjects,_F:vcsConfigMode,_G:vcsModeOfOperation,_H:vcsIdentifier,_I:vcsVirtualIpV4Address,_J:vcsVirtualIpV6Address,_K:vcsVirtualIpAssociatedRbridgeId,_L:vcsVirtualIpInterfaceId,_M:vcsVirtualIpV4OperStatus,_N:vcsVirtualIpV6OperStatus,_O:vcsNumNodesInCluster,_P:vcsClusterCondition,'vcsFabricIslTable':vcsFabricIslTable,'vcsFabricIslEntry':vcsFabricIslEntry,_E:vcsFabricIslIndex,_Q:vcsFabricIslIntfName,_R:vcsFabricIslNbrIntfName,_S:vcsFabricIslNbrWWN,_T:vcsFabricIslNbrName,_U:vcsFabricIslBW,_V:vcsFabricIslIsTrunk,'brocadeVcsMIBConformance':brocadeVcsMIBConformance,'brocadeVcsConformanceGroups':brocadeVcsConformanceGroups,_W:brocadeVcsObjectsGroup,'brocadeVcsCompliances':brocadeVcsCompliances,'brocadeVcsCompliance':brocadeVcsCompliance})