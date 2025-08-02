_e='cpqClusterNetworkIndex'
_d='clientAndInternal'
_c='internal'
_b='client'
_a='cpqClusterInterconnectIndex'
_Z='offline'
_Y='online'
_X='cpqClusterResourceIndex'
_W='cpqClusterNodeIndex'
_V='cpqClusterOsCommonModuleIndex'
_U='read-write'
_T='NotificationType'
_S='OctetString'
_R='cpqClusterNetworkName'
_Q='cpqClusterResourceName'
_P='cpqClusterNodeName'
_O='cpqClusterName'
_N='deprecated'
_M='degraded'
_L='ok'
_K='failed'
_J='sysName'
_I='SNMPv2-MIB'
_H='cpqHoTrapFlags'
_G='CPQHOST-MIB'
_F='other'
_E='CPQCLUSTER-MIB'
_D='Integer32'
_C='DisplayString'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_S,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
compaq,cpqHoTrapFlags=mibBuilder.importSymbols(_G,'compaq',_H)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
sysName,=mibBuilder.importSymbols(_I,_J)
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,NotificationType,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier',_T,'ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn',_T,'TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_C,'PhysAddress','TextualConvention')
_CpqCluster_ObjectIdentity=ObjectIdentity
cpqCluster=_CpqCluster_ObjectIdentity((1,3,6,1,4,1,232,15))
_CpqClusterMibRev_ObjectIdentity=ObjectIdentity
cpqClusterMibRev=_CpqClusterMibRev_ObjectIdentity((1,3,6,1,4,1,232,15,1))
class _CpqClusterMibRevMajor_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_CpqClusterMibRevMajor_Type.__name__=_D
_CpqClusterMibRevMajor_Object=MibScalar
cpqClusterMibRevMajor=_CpqClusterMibRevMajor_Object((1,3,6,1,4,1,232,15,1,1),_CpqClusterMibRevMajor_Type())
cpqClusterMibRevMajor.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqClusterMibRevMajor.setStatus(_A)
class _CpqClusterMibRevMinor_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CpqClusterMibRevMinor_Type.__name__=_D
_CpqClusterMibRevMinor_Object=MibScalar
cpqClusterMibRevMinor=_CpqClusterMibRevMinor_Object((1,3,6,1,4,1,232,15,1,2),_CpqClusterMibRevMinor_Type())
cpqClusterMibRevMinor.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqClusterMibRevMinor.setStatus(_A)
class _CpqClusterMibCondition_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_F,1),(_L,2),(_M,3),(_K,4)))
_CpqClusterMibCondition_Type.__name__=_D
_CpqClusterMibCondition_Object=MibScalar
cpqClusterMibCondition=_CpqClusterMibCondition_Object((1,3,6,1,4,1,232,15,1,3),_CpqClusterMibCondition_Type())
cpqClusterMibCondition.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqClusterMibCondition.setStatus(_A)
_CpqClusterComponent_ObjectIdentity=ObjectIdentity
cpqClusterComponent=_CpqClusterComponent_ObjectIdentity((1,3,6,1,4,1,232,15,2))
_CpqClusterInterface_ObjectIdentity=ObjectIdentity
cpqClusterInterface=_CpqClusterInterface_ObjectIdentity((1,3,6,1,4,1,232,15,2,1))
_CpqClusterOsCommon_ObjectIdentity=ObjectIdentity
cpqClusterOsCommon=_CpqClusterOsCommon_ObjectIdentity((1,3,6,1,4,1,232,15,2,1,4))
class _CpqClusterOsCommonPollFreq_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CpqClusterOsCommonPollFreq_Type.__name__=_D
_CpqClusterOsCommonPollFreq_Object=MibScalar
cpqClusterOsCommonPollFreq=_CpqClusterOsCommonPollFreq_Object((1,3,6,1,4,1,232,15,2,1,4,1),_CpqClusterOsCommonPollFreq_Type())
cpqClusterOsCommonPollFreq.setMaxAccess(_U)
if mibBuilder.loadTexts:cpqClusterOsCommonPollFreq.setStatus(_A)
_CpqClusterOsCommonModuleTable_Object=MibTable
cpqClusterOsCommonModuleTable=_CpqClusterOsCommonModuleTable_Object((1,3,6,1,4,1,232,15,2,1,4,2))
if mibBuilder.loadTexts:cpqClusterOsCommonModuleTable.setStatus(_N)
_CpqClusterOsCommonModuleEntry_Object=MibTableRow
cpqClusterOsCommonModuleEntry=_CpqClusterOsCommonModuleEntry_Object((1,3,6,1,4,1,232,15,2,1,4,2,1))
cpqClusterOsCommonModuleEntry.setIndexNames((0,_E,_V))
if mibBuilder.loadTexts:cpqClusterOsCommonModuleEntry.setStatus(_N)
class _CpqClusterOsCommonModuleIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CpqClusterOsCommonModuleIndex_Type.__name__=_D
_CpqClusterOsCommonModuleIndex_Object=MibTableColumn
cpqClusterOsCommonModuleIndex=_CpqClusterOsCommonModuleIndex_Object((1,3,6,1,4,1,232,15,2,1,4,2,1,1),_CpqClusterOsCommonModuleIndex_Type())
cpqClusterOsCommonModuleIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqClusterOsCommonModuleIndex.setStatus(_N)
class _CpqClusterOsCommonModuleName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CpqClusterOsCommonModuleName_Type.__name__=_C
_CpqClusterOsCommonModuleName_Object=MibTableColumn
cpqClusterOsCommonModuleName=_CpqClusterOsCommonModuleName_Object((1,3,6,1,4,1,232,15,2,1,4,2,1,2),_CpqClusterOsCommonModuleName_Type())
cpqClusterOsCommonModuleName.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqClusterOsCommonModuleName.setStatus(_N)
class _CpqClusterOsCommonModuleVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,5))
_CpqClusterOsCommonModuleVersion_Type.__name__=_C
_CpqClusterOsCommonModuleVersion_Object=MibTableColumn
cpqClusterOsCommonModuleVersion=_CpqClusterOsCommonModuleVersion_Object((1,3,6,1,4,1,232,15,2,1,4,2,1,3),_CpqClusterOsCommonModuleVersion_Type())
cpqClusterOsCommonModuleVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqClusterOsCommonModuleVersion.setStatus(_N)
class _CpqClusterOsCommonModuleDate_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(7,7));fixedLength=7
_CpqClusterOsCommonModuleDate_Type.__name__=_S
_CpqClusterOsCommonModuleDate_Object=MibTableColumn
cpqClusterOsCommonModuleDate=_CpqClusterOsCommonModuleDate_Object((1,3,6,1,4,1,232,15,2,1,4,2,1,4),_CpqClusterOsCommonModuleDate_Type())
cpqClusterOsCommonModuleDate.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqClusterOsCommonModuleDate.setStatus(_N)
class _CpqClusterOsCommonModulePurpose_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CpqClusterOsCommonModulePurpose_Type.__name__=_C
_CpqClusterOsCommonModulePurpose_Object=MibTableColumn
cpqClusterOsCommonModulePurpose=_CpqClusterOsCommonModulePurpose_Object((1,3,6,1,4,1,232,15,2,1,4,2,1,5),_CpqClusterOsCommonModulePurpose_Type())
cpqClusterOsCommonModulePurpose.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqClusterOsCommonModulePurpose.setStatus(_N)
_CpqClusterInfo_ObjectIdentity=ObjectIdentity
cpqClusterInfo=_CpqClusterInfo_ObjectIdentity((1,3,6,1,4,1,232,15,2,2))
class _CpqClusterName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CpqClusterName_Type.__name__=_C
_CpqClusterName_Object=MibScalar
cpqClusterName=_CpqClusterName_Object((1,3,6,1,4,1,232,15,2,2,1),_CpqClusterName_Type())
cpqClusterName.setMaxAccess(_U)
if mibBuilder.loadTexts:cpqClusterName.setStatus(_A)
class _CpqClusterCondition_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_F,1),(_L,2),(_M,3),(_K,4)))
_CpqClusterCondition_Type.__name__=_D
_CpqClusterCondition_Object=MibScalar
cpqClusterCondition=_CpqClusterCondition_Object((1,3,6,1,4,1,232,15,2,2,2),_CpqClusterCondition_Type())
cpqClusterCondition.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqClusterCondition.setStatus(_A)
class _CpqClusterIpAddress_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_CpqClusterIpAddress_Type.__name__=_C
_CpqClusterIpAddress_Object=MibScalar
cpqClusterIpAddress=_CpqClusterIpAddress_Object((1,3,6,1,4,1,232,15,2,2,3),_CpqClusterIpAddress_Type())
cpqClusterIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqClusterIpAddress.setStatus(_A)
_CpqClusterQuorumResource_Type=Integer32
_CpqClusterQuorumResource_Object=MibScalar
cpqClusterQuorumResource=_CpqClusterQuorumResource_Object((1,3,6,1,4,1,232,15,2,2,4),_CpqClusterQuorumResource_Type())
cpqClusterQuorumResource.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqClusterQuorumResource.setStatus(_A)
_CpqClusterMajorVersion_Type=Integer32
_CpqClusterMajorVersion_Object=MibScalar
cpqClusterMajorVersion=_CpqClusterMajorVersion_Object((1,3,6,1,4,1,232,15,2,2,5),_CpqClusterMajorVersion_Type())
cpqClusterMajorVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqClusterMajorVersion.setStatus(_A)
_CpqClusterMinorVersion_Type=Integer32
_CpqClusterMinorVersion_Object=MibScalar
cpqClusterMinorVersion=_CpqClusterMinorVersion_Object((1,3,6,1,4,1,232,15,2,2,6),_CpqClusterMinorVersion_Type())
cpqClusterMinorVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqClusterMinorVersion.setStatus(_A)
class _CpqClusterCSDVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_CpqClusterCSDVersion_Type.__name__=_C
_CpqClusterCSDVersion_Object=MibScalar
cpqClusterCSDVersion=_CpqClusterCSDVersion_Object((1,3,6,1,4,1,232,15,2,2,7),_CpqClusterCSDVersion_Type())
cpqClusterCSDVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqClusterCSDVersion.setStatus(_A)
class _CpqClusterVendorId_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_CpqClusterVendorId_Type.__name__=_C
_CpqClusterVendorId_Object=MibScalar
cpqClusterVendorId=_CpqClusterVendorId_Object((1,3,6,1,4,1,232,15,2,2,8),_CpqClusterVendorId_Type())
cpqClusterVendorId.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqClusterVendorId.setStatus(_A)
class _CpqClusterResourceAggregateCondition_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_F,1),(_L,2),(_M,3),(_K,4)))
_CpqClusterResourceAggregateCondition_Type.__name__=_D
_CpqClusterResourceAggregateCondition_Object=MibScalar
cpqClusterResourceAggregateCondition=_CpqClusterResourceAggregateCondition_Object((1,3,6,1,4,1,232,15,2,2,9),_CpqClusterResourceAggregateCondition_Type())
cpqClusterResourceAggregateCondition.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqClusterResourceAggregateCondition.setStatus(_A)
class _CpqClusterNetworkAggregateCondition_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_F,1),(_L,2),(_M,3),(_K,4)))
_CpqClusterNetworkAggregateCondition_Type.__name__=_D
_CpqClusterNetworkAggregateCondition_Object=MibScalar
cpqClusterNetworkAggregateCondition=_CpqClusterNetworkAggregateCondition_Object((1,3,6,1,4,1,232,15,2,2,10),_CpqClusterNetworkAggregateCondition_Type())
cpqClusterNetworkAggregateCondition.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqClusterNetworkAggregateCondition.setStatus(_A)
_CpqClusterNode_ObjectIdentity=ObjectIdentity
cpqClusterNode=_CpqClusterNode_ObjectIdentity((1,3,6,1,4,1,232,15,2,3))
_CpqClusterNodeTable_Object=MibTable
cpqClusterNodeTable=_CpqClusterNodeTable_Object((1,3,6,1,4,1,232,15,2,3,1))
if mibBuilder.loadTexts:cpqClusterNodeTable.setStatus(_A)
_CpqClusterNodeEntry_Object=MibTableRow
cpqClusterNodeEntry=_CpqClusterNodeEntry_Object((1,3,6,1,4,1,232,15,2,3,1,1))
cpqClusterNodeEntry.setIndexNames((0,_E,_W))
if mibBuilder.loadTexts:cpqClusterNodeEntry.setStatus(_A)
class _CpqClusterNodeIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CpqClusterNodeIndex_Type.__name__=_D
_CpqClusterNodeIndex_Object=MibTableColumn
cpqClusterNodeIndex=_CpqClusterNodeIndex_Object((1,3,6,1,4,1,232,15,2,3,1,1,1),_CpqClusterNodeIndex_Type())
cpqClusterNodeIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqClusterNodeIndex.setStatus(_A)
class _CpqClusterNodeName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_CpqClusterNodeName_Type.__name__=_C
_CpqClusterNodeName_Object=MibTableColumn
cpqClusterNodeName=_CpqClusterNodeName_Object((1,3,6,1,4,1,232,15,2,3,1,1,2),_CpqClusterNodeName_Type())
cpqClusterNodeName.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqClusterNodeName.setStatus(_A)
class _CpqClusterNodeStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_F,1),('nodeUp',2),('nodeDown',3),('nodePaused',4),('nodeJoining',5)))
_CpqClusterNodeStatus_Type.__name__=_D
_CpqClusterNodeStatus_Object=MibTableColumn
cpqClusterNodeStatus=_CpqClusterNodeStatus_Object((1,3,6,1,4,1,232,15,2,3,1,1,3),_CpqClusterNodeStatus_Type())
cpqClusterNodeStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqClusterNodeStatus.setStatus(_A)
class _CpqClusterNodeCondition_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_F,1),(_L,2),(_M,3),(_K,4)))
_CpqClusterNodeCondition_Type.__name__=_D
_CpqClusterNodeCondition_Object=MibTableColumn
cpqClusterNodeCondition=_CpqClusterNodeCondition_Object((1,3,6,1,4,1,232,15,2,3,1,1,4),_CpqClusterNodeCondition_Type())
cpqClusterNodeCondition.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqClusterNodeCondition.setStatus(_A)
_CpqClusterResource_ObjectIdentity=ObjectIdentity
cpqClusterResource=_CpqClusterResource_ObjectIdentity((1,3,6,1,4,1,232,15,2,4))
_CpqClusterResourceTable_Object=MibTable
cpqClusterResourceTable=_CpqClusterResourceTable_Object((1,3,6,1,4,1,232,15,2,4,1))
if mibBuilder.loadTexts:cpqClusterResourceTable.setStatus(_A)
_CpqClusterResourceEntry_Object=MibTableRow
cpqClusterResourceEntry=_CpqClusterResourceEntry_Object((1,3,6,1,4,1,232,15,2,4,1,1))
cpqClusterResourceEntry.setIndexNames((0,_E,_X))
if mibBuilder.loadTexts:cpqClusterResourceEntry.setStatus(_A)
class _CpqClusterResourceIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CpqClusterResourceIndex_Type.__name__=_D
_CpqClusterResourceIndex_Object=MibTableColumn
cpqClusterResourceIndex=_CpqClusterResourceIndex_Object((1,3,6,1,4,1,232,15,2,4,1,1,1),_CpqClusterResourceIndex_Type())
cpqClusterResourceIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqClusterResourceIndex.setStatus(_A)
class _CpqClusterResourceName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_CpqClusterResourceName_Type.__name__=_C
_CpqClusterResourceName_Object=MibTableColumn
cpqClusterResourceName=_CpqClusterResourceName_Object((1,3,6,1,4,1,232,15,2,4,1,1,2),_CpqClusterResourceName_Type())
cpqClusterResourceName.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqClusterResourceName.setStatus(_A)
class _CpqClusterResourceType_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_CpqClusterResourceType_Type.__name__=_C
_CpqClusterResourceType_Object=MibTableColumn
cpqClusterResourceType=_CpqClusterResourceType_Object((1,3,6,1,4,1,232,15,2,4,1,1,3),_CpqClusterResourceType_Type())
cpqClusterResourceType.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqClusterResourceType.setStatus(_A)
class _CpqClusterResourceState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_F,1),(_Y,2),(_Z,3),(_K,4),('onlinePending',5),('offlinePending',6)))
_CpqClusterResourceState_Type.__name__=_D
_CpqClusterResourceState_Object=MibTableColumn
cpqClusterResourceState=_CpqClusterResourceState_Object((1,3,6,1,4,1,232,15,2,4,1,1,4),_CpqClusterResourceState_Type())
cpqClusterResourceState.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqClusterResourceState.setStatus(_A)
class _CpqClusterResourceOwnerNode_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_CpqClusterResourceOwnerNode_Type.__name__=_C
_CpqClusterResourceOwnerNode_Object=MibTableColumn
cpqClusterResourceOwnerNode=_CpqClusterResourceOwnerNode_Object((1,3,6,1,4,1,232,15,2,4,1,1,5),_CpqClusterResourceOwnerNode_Type())
cpqClusterResourceOwnerNode.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqClusterResourceOwnerNode.setStatus(_A)
class _CpqClusterResourcePhysId_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_CpqClusterResourcePhysId_Type.__name__=_C
_CpqClusterResourcePhysId_Object=MibTableColumn
cpqClusterResourcePhysId=_CpqClusterResourcePhysId_Object((1,3,6,1,4,1,232,15,2,4,1,1,6),_CpqClusterResourcePhysId_Type())
cpqClusterResourcePhysId.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqClusterResourcePhysId.setStatus(_A)
class _CpqClusterResourceCondition_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_F,1),(_L,2),(_M,3),(_K,4)))
_CpqClusterResourceCondition_Type.__name__=_D
_CpqClusterResourceCondition_Object=MibTableColumn
cpqClusterResourceCondition=_CpqClusterResourceCondition_Object((1,3,6,1,4,1,232,15,2,4,1,1,7),_CpqClusterResourceCondition_Type())
cpqClusterResourceCondition.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqClusterResourceCondition.setStatus(_A)
class _CpqClusterResourceDriveLetter_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_CpqClusterResourceDriveLetter_Type.__name__=_C
_CpqClusterResourceDriveLetter_Object=MibTableColumn
cpqClusterResourceDriveLetter=_CpqClusterResourceDriveLetter_Object((1,3,6,1,4,1,232,15,2,4,1,1,8),_CpqClusterResourceDriveLetter_Type())
cpqClusterResourceDriveLetter.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqClusterResourceDriveLetter.setStatus(_A)
class _CpqClusterResourceIpAddress_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_CpqClusterResourceIpAddress_Type.__name__=_C
_CpqClusterResourceIpAddress_Object=MibTableColumn
cpqClusterResourceIpAddress=_CpqClusterResourceIpAddress_Object((1,3,6,1,4,1,232,15,2,4,1,1,9),_CpqClusterResourceIpAddress_Type())
cpqClusterResourceIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqClusterResourceIpAddress.setStatus(_A)
class _CpqClusterResourceGroupName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_CpqClusterResourceGroupName_Type.__name__=_C
_CpqClusterResourceGroupName_Object=MibTableColumn
cpqClusterResourceGroupName=_CpqClusterResourceGroupName_Object((1,3,6,1,4,1,232,15,2,4,1,1,10),_CpqClusterResourceGroupName_Type())
cpqClusterResourceGroupName.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqClusterResourceGroupName.setStatus(_A)
_CpqClusterInterconnect_ObjectIdentity=ObjectIdentity
cpqClusterInterconnect=_CpqClusterInterconnect_ObjectIdentity((1,3,6,1,4,1,232,15,2,5))
_CpqClusterInterconnectTable_Object=MibTable
cpqClusterInterconnectTable=_CpqClusterInterconnectTable_Object((1,3,6,1,4,1,232,15,2,5,1))
if mibBuilder.loadTexts:cpqClusterInterconnectTable.setStatus(_A)
_CpqClusterInterconnectEntry_Object=MibTableRow
cpqClusterInterconnectEntry=_CpqClusterInterconnectEntry_Object((1,3,6,1,4,1,232,15,2,5,1,1))
cpqClusterInterconnectEntry.setIndexNames((0,_E,_a))
if mibBuilder.loadTexts:cpqClusterInterconnectEntry.setStatus(_A)
class _CpqClusterInterconnectIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_CpqClusterInterconnectIndex_Type.__name__=_D
_CpqClusterInterconnectIndex_Object=MibTableColumn
cpqClusterInterconnectIndex=_CpqClusterInterconnectIndex_Object((1,3,6,1,4,1,232,15,2,5,1,1,1),_CpqClusterInterconnectIndex_Type())
cpqClusterInterconnectIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqClusterInterconnectIndex.setStatus(_A)
class _CpqClusterInterconnectPhysId_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_CpqClusterInterconnectPhysId_Type.__name__=_C
_CpqClusterInterconnectPhysId_Object=MibTableColumn
cpqClusterInterconnectPhysId=_CpqClusterInterconnectPhysId_Object((1,3,6,1,4,1,232,15,2,5,1,1,2),_CpqClusterInterconnectPhysId_Type())
cpqClusterInterconnectPhysId.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqClusterInterconnectPhysId.setStatus(_A)
class _CpqClusterInterconnectTransport_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_CpqClusterInterconnectTransport_Type.__name__=_C
_CpqClusterInterconnectTransport_Object=MibTableColumn
cpqClusterInterconnectTransport=_CpqClusterInterconnectTransport_Object((1,3,6,1,4,1,232,15,2,5,1,1,3),_CpqClusterInterconnectTransport_Type())
cpqClusterInterconnectTransport.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqClusterInterconnectTransport.setStatus(_A)
class _CpqClusterInterconnectAddress_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_CpqClusterInterconnectAddress_Type.__name__=_C
_CpqClusterInterconnectAddress_Object=MibTableColumn
cpqClusterInterconnectAddress=_CpqClusterInterconnectAddress_Object((1,3,6,1,4,1,232,15,2,5,1,1,4),_CpqClusterInterconnectAddress_Type())
cpqClusterInterconnectAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqClusterInterconnectAddress.setStatus(_A)
class _CpqClusterInterconnectNetworkName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_CpqClusterInterconnectNetworkName_Type.__name__=_C
_CpqClusterInterconnectNetworkName_Object=MibTableColumn
cpqClusterInterconnectNetworkName=_CpqClusterInterconnectNetworkName_Object((1,3,6,1,4,1,232,15,2,5,1,1,5),_CpqClusterInterconnectNetworkName_Type())
cpqClusterInterconnectNetworkName.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqClusterInterconnectNetworkName.setStatus(_A)
class _CpqClusterInterconnectNodeName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_CpqClusterInterconnectNodeName_Type.__name__=_C
_CpqClusterInterconnectNodeName_Object=MibTableColumn
cpqClusterInterconnectNodeName=_CpqClusterInterconnectNodeName_Object((1,3,6,1,4,1,232,15,2,5,1,1,6),_CpqClusterInterconnectNodeName_Type())
cpqClusterInterconnectNodeName.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqClusterInterconnectNodeName.setStatus(_A)
class _CpqClusterInterconnectRole_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('none',1),(_b,2),(_c,3),(_d,4)))
_CpqClusterInterconnectRole_Type.__name__=_D
_CpqClusterInterconnectRole_Object=MibTableColumn
cpqClusterInterconnectRole=_CpqClusterInterconnectRole_Object((1,3,6,1,4,1,232,15,2,5,1,1,7),_CpqClusterInterconnectRole_Type())
cpqClusterInterconnectRole.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqClusterInterconnectRole.setStatus(_A)
_CpqClusterNetwork_ObjectIdentity=ObjectIdentity
cpqClusterNetwork=_CpqClusterNetwork_ObjectIdentity((1,3,6,1,4,1,232,15,2,6))
_CpqClusterNetworkTable_Object=MibTable
cpqClusterNetworkTable=_CpqClusterNetworkTable_Object((1,3,6,1,4,1,232,15,2,6,1))
if mibBuilder.loadTexts:cpqClusterNetworkTable.setStatus(_A)
_CpqClusterNetworkEntry_Object=MibTableRow
cpqClusterNetworkEntry=_CpqClusterNetworkEntry_Object((1,3,6,1,4,1,232,15,2,6,1,1))
cpqClusterNetworkEntry.setIndexNames((0,_E,_e))
if mibBuilder.loadTexts:cpqClusterNetworkEntry.setStatus(_A)
class _CpqClusterNetworkIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_CpqClusterNetworkIndex_Type.__name__=_D
_CpqClusterNetworkIndex_Object=MibTableColumn
cpqClusterNetworkIndex=_CpqClusterNetworkIndex_Object((1,3,6,1,4,1,232,15,2,6,1,1,1),_CpqClusterNetworkIndex_Type())
cpqClusterNetworkIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqClusterNetworkIndex.setStatus(_A)
class _CpqClusterNetworkName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_CpqClusterNetworkName_Type.__name__=_C
_CpqClusterNetworkName_Object=MibTableColumn
cpqClusterNetworkName=_CpqClusterNetworkName_Object((1,3,6,1,4,1,232,15,2,6,1,1,2),_CpqClusterNetworkName_Type())
cpqClusterNetworkName.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqClusterNetworkName.setStatus(_A)
class _CpqClusterNetworkAddressMask_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_CpqClusterNetworkAddressMask_Type.__name__=_C
_CpqClusterNetworkAddressMask_Object=MibTableColumn
cpqClusterNetworkAddressMask=_CpqClusterNetworkAddressMask_Object((1,3,6,1,4,1,232,15,2,6,1,1,3),_CpqClusterNetworkAddressMask_Type())
cpqClusterNetworkAddressMask.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqClusterNetworkAddressMask.setStatus(_A)
class _CpqClusterNetworkDescription_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_CpqClusterNetworkDescription_Type.__name__=_C
_CpqClusterNetworkDescription_Object=MibTableColumn
cpqClusterNetworkDescription=_CpqClusterNetworkDescription_Object((1,3,6,1,4,1,232,15,2,6,1,1,4),_CpqClusterNetworkDescription_Type())
cpqClusterNetworkDescription.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqClusterNetworkDescription.setStatus(_A)
class _CpqClusterNetworkRole_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('none',1),(_b,2),(_c,3),(_d,4)))
_CpqClusterNetworkRole_Type.__name__=_D
_CpqClusterNetworkRole_Object=MibTableColumn
cpqClusterNetworkRole=_CpqClusterNetworkRole_Object((1,3,6,1,4,1,232,15,2,6,1,1,5),_CpqClusterNetworkRole_Type())
cpqClusterNetworkRole.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqClusterNetworkRole.setStatus(_A)
class _CpqClusterNetworkState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_F,1),(_Y,2),(_Z,3),('partitioned',4),('unavailable',5)))
_CpqClusterNetworkState_Type.__name__=_D
_CpqClusterNetworkState_Object=MibTableColumn
cpqClusterNetworkState=_CpqClusterNetworkState_Object((1,3,6,1,4,1,232,15,2,6,1,1,6),_CpqClusterNetworkState_Type())
cpqClusterNetworkState.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqClusterNetworkState.setStatus(_A)
class _CpqClusterNetworkCondition_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_F,1),(_L,2),(_M,3),(_K,4)))
_CpqClusterNetworkCondition_Type.__name__=_D
_CpqClusterNetworkCondition_Object=MibTableColumn
cpqClusterNetworkCondition=_CpqClusterNetworkCondition_Object((1,3,6,1,4,1,232,15,2,6,1,1,7),_CpqClusterNetworkCondition_Type())
cpqClusterNetworkCondition.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqClusterNetworkCondition.setStatus(_A)
_CpqClusterTrap_ObjectIdentity=ObjectIdentity
cpqClusterTrap=_CpqClusterTrap_ObjectIdentity((1,3,6,1,4,1,232,15,3))
cpqClusterDegraded=NotificationType((1,3,6,1,4,1,232,0,15001))
cpqClusterDegraded.setObjects(*((_I,_J),(_G,_H),(_E,_O)))
if mibBuilder.loadTexts:cpqClusterDegraded.setStatus('')
cpqClusterFailed=NotificationType((1,3,6,1,4,1,232,0,15002))
cpqClusterFailed.setObjects(*((_I,_J),(_G,_H),(_E,_O)))
if mibBuilder.loadTexts:cpqClusterFailed.setStatus('')
cpqClusterNodeDegraded=NotificationType((1,3,6,1,4,1,232,0,15003))
cpqClusterNodeDegraded.setObjects(*((_I,_J),(_G,_H),(_E,_P)))
if mibBuilder.loadTexts:cpqClusterNodeDegraded.setStatus('')
cpqClusterNodeFailed=NotificationType((1,3,6,1,4,1,232,0,15004))
cpqClusterNodeFailed.setObjects(*((_I,_J),(_G,_H),(_E,_P)))
if mibBuilder.loadTexts:cpqClusterNodeFailed.setStatus('')
cpqClusterResourceDegraded=NotificationType((1,3,6,1,4,1,232,0,15005))
cpqClusterResourceDegraded.setObjects(*((_I,_J),(_G,_H),(_E,_Q)))
if mibBuilder.loadTexts:cpqClusterResourceDegraded.setStatus('')
cpqClusterResourceFailed=NotificationType((1,3,6,1,4,1,232,0,15006))
cpqClusterResourceFailed.setObjects(*((_I,_J),(_G,_H),(_E,_Q)))
if mibBuilder.loadTexts:cpqClusterResourceFailed.setStatus('')
cpqClusterNetworkDegraded=NotificationType((1,3,6,1,4,1,232,0,15007))
cpqClusterNetworkDegraded.setObjects(*((_I,_J),(_G,_H),(_E,_R)))
if mibBuilder.loadTexts:cpqClusterNetworkDegraded.setStatus('')
cpqClusterNetworkFailed=NotificationType((1,3,6,1,4,1,232,0,15008))
cpqClusterNetworkFailed.setObjects(*((_I,_J),(_G,_H),(_E,_R)))
if mibBuilder.loadTexts:cpqClusterNetworkFailed.setStatus('')
mibBuilder.exportSymbols(_E,**{'cpqClusterDegraded':cpqClusterDegraded,'cpqClusterFailed':cpqClusterFailed,'cpqClusterNodeDegraded':cpqClusterNodeDegraded,'cpqClusterNodeFailed':cpqClusterNodeFailed,'cpqClusterResourceDegraded':cpqClusterResourceDegraded,'cpqClusterResourceFailed':cpqClusterResourceFailed,'cpqClusterNetworkDegraded':cpqClusterNetworkDegraded,'cpqClusterNetworkFailed':cpqClusterNetworkFailed,'cpqCluster':cpqCluster,'cpqClusterMibRev':cpqClusterMibRev,'cpqClusterMibRevMajor':cpqClusterMibRevMajor,'cpqClusterMibRevMinor':cpqClusterMibRevMinor,'cpqClusterMibCondition':cpqClusterMibCondition,'cpqClusterComponent':cpqClusterComponent,'cpqClusterInterface':cpqClusterInterface,'cpqClusterOsCommon':cpqClusterOsCommon,'cpqClusterOsCommonPollFreq':cpqClusterOsCommonPollFreq,'cpqClusterOsCommonModuleTable':cpqClusterOsCommonModuleTable,'cpqClusterOsCommonModuleEntry':cpqClusterOsCommonModuleEntry,_V:cpqClusterOsCommonModuleIndex,'cpqClusterOsCommonModuleName':cpqClusterOsCommonModuleName,'cpqClusterOsCommonModuleVersion':cpqClusterOsCommonModuleVersion,'cpqClusterOsCommonModuleDate':cpqClusterOsCommonModuleDate,'cpqClusterOsCommonModulePurpose':cpqClusterOsCommonModulePurpose,'cpqClusterInfo':cpqClusterInfo,_O:cpqClusterName,'cpqClusterCondition':cpqClusterCondition,'cpqClusterIpAddress':cpqClusterIpAddress,'cpqClusterQuorumResource':cpqClusterQuorumResource,'cpqClusterMajorVersion':cpqClusterMajorVersion,'cpqClusterMinorVersion':cpqClusterMinorVersion,'cpqClusterCSDVersion':cpqClusterCSDVersion,'cpqClusterVendorId':cpqClusterVendorId,'cpqClusterResourceAggregateCondition':cpqClusterResourceAggregateCondition,'cpqClusterNetworkAggregateCondition':cpqClusterNetworkAggregateCondition,'cpqClusterNode':cpqClusterNode,'cpqClusterNodeTable':cpqClusterNodeTable,'cpqClusterNodeEntry':cpqClusterNodeEntry,_W:cpqClusterNodeIndex,_P:cpqClusterNodeName,'cpqClusterNodeStatus':cpqClusterNodeStatus,'cpqClusterNodeCondition':cpqClusterNodeCondition,'cpqClusterResource':cpqClusterResource,'cpqClusterResourceTable':cpqClusterResourceTable,'cpqClusterResourceEntry':cpqClusterResourceEntry,_X:cpqClusterResourceIndex,_Q:cpqClusterResourceName,'cpqClusterResourceType':cpqClusterResourceType,'cpqClusterResourceState':cpqClusterResourceState,'cpqClusterResourceOwnerNode':cpqClusterResourceOwnerNode,'cpqClusterResourcePhysId':cpqClusterResourcePhysId,'cpqClusterResourceCondition':cpqClusterResourceCondition,'cpqClusterResourceDriveLetter':cpqClusterResourceDriveLetter,'cpqClusterResourceIpAddress':cpqClusterResourceIpAddress,'cpqClusterResourceGroupName':cpqClusterResourceGroupName,'cpqClusterInterconnect':cpqClusterInterconnect,'cpqClusterInterconnectTable':cpqClusterInterconnectTable,'cpqClusterInterconnectEntry':cpqClusterInterconnectEntry,_a:cpqClusterInterconnectIndex,'cpqClusterInterconnectPhysId':cpqClusterInterconnectPhysId,'cpqClusterInterconnectTransport':cpqClusterInterconnectTransport,'cpqClusterInterconnectAddress':cpqClusterInterconnectAddress,'cpqClusterInterconnectNetworkName':cpqClusterInterconnectNetworkName,'cpqClusterInterconnectNodeName':cpqClusterInterconnectNodeName,'cpqClusterInterconnectRole':cpqClusterInterconnectRole,'cpqClusterNetwork':cpqClusterNetwork,'cpqClusterNetworkTable':cpqClusterNetworkTable,'cpqClusterNetworkEntry':cpqClusterNetworkEntry,_e:cpqClusterNetworkIndex,_R:cpqClusterNetworkName,'cpqClusterNetworkAddressMask':cpqClusterNetworkAddressMask,'cpqClusterNetworkDescription':cpqClusterNetworkDescription,'cpqClusterNetworkRole':cpqClusterNetworkRole,'cpqClusterNetworkState':cpqClusterNetworkState,'cpqClusterNetworkCondition':cpqClusterNetworkCondition,'cpqClusterTrap':cpqClusterTrap})