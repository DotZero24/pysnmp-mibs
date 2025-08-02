_b='ciscoCpgPolicyGroupInfoGroup'
_a='ciscoCpgGroupIpInfoGroup'
_Z='ciscoCpgGroupInfoGroup'
_Y='ciscoCpgPolicyInfoGroup'
_X='cpgPolicyGroupRowStatus'
_W='cpgPolicyGroupCount'
_V='cpgGroupIpRowStatus'
_U='cpgGroupIpSourceType'
_T='cpgGroupIpMask'
_S='cpgGroupRowStatus'
_R='cpgGroupIpAddrCount'
_Q='cpgGroupSourceType'
_P='cpgPolicyGroupGroupName'
_O='cpgPolicyGroupPolicyName'
_N='cpgPolicyName'
_M='cpgGroupIpAddress'
_L='cpgGroupIpAddrType'
_K='cpgGroupIpGroupName'
_J='configured'
_I='cpgGroupName'
_H='128a'
_G='Integer32'
_F='InetAddress'
_E='read-create'
_D='read-only'
_C='not-accessible'
_B='CISCO-POLICY-GROUP-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB',_F,'InetAddressType')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_G,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
ciscoPolicyGroupMIB=ModuleIdentity((1,3,6,1,4,1,9,9,507))
if mibBuilder.loadTexts:ciscoPolicyGroupMIB.setRevisions(('2006-01-13 16:00',))
class CpgPolicyName(TextualConvention,OctetString):status=_A;displayHint=_H;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,128))
class CpgPolicyNameOrEmpty(TextualConvention,OctetString):status=_A;displayHint=_H;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
class CpgGroupName(TextualConvention,OctetString):status=_A;displayHint=_H;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,128))
_CiscoPolicyGroupMIBNotifs_ObjectIdentity=ObjectIdentity
ciscoPolicyGroupMIBNotifs=_CiscoPolicyGroupMIBNotifs_ObjectIdentity((1,3,6,1,4,1,9,9,507,0))
_CiscoPolicyGroupMIBObjects_ObjectIdentity=ObjectIdentity
ciscoPolicyGroupMIBObjects=_CiscoPolicyGroupMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,507,1))
_CpgGroup_ObjectIdentity=ObjectIdentity
cpgGroup=_CpgGroup_ObjectIdentity((1,3,6,1,4,1,9,9,507,1,1))
_CpgGroupTable_Object=MibTable
cpgGroupTable=_CpgGroupTable_Object((1,3,6,1,4,1,9,9,507,1,1,1))
if mibBuilder.loadTexts:cpgGroupTable.setStatus(_A)
_CpgGroupEntry_Object=MibTableRow
cpgGroupEntry=_CpgGroupEntry_Object((1,3,6,1,4,1,9,9,507,1,1,1,1))
cpgGroupEntry.setIndexNames((1,_B,_I))
if mibBuilder.loadTexts:cpgGroupEntry.setStatus(_A)
_CpgGroupName_Type=CpgGroupName
_CpgGroupName_Object=MibTableColumn
cpgGroupName=_CpgGroupName_Object((1,3,6,1,4,1,9,9,507,1,1,1,1,1),_CpgGroupName_Type())
cpgGroupName.setMaxAccess(_C)
if mibBuilder.loadTexts:cpgGroupName.setStatus(_A)
class _CpgGroupSourceType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('unknown',1),('accessList',2),(_J,3)))
_CpgGroupSourceType_Type.__name__=_G
_CpgGroupSourceType_Object=MibTableColumn
cpgGroupSourceType=_CpgGroupSourceType_Object((1,3,6,1,4,1,9,9,507,1,1,1,1,2),_CpgGroupSourceType_Type())
cpgGroupSourceType.setMaxAccess(_D)
if mibBuilder.loadTexts:cpgGroupSourceType.setStatus(_A)
_CpgGroupIpAddrCount_Type=Unsigned32
_CpgGroupIpAddrCount_Object=MibTableColumn
cpgGroupIpAddrCount=_CpgGroupIpAddrCount_Object((1,3,6,1,4,1,9,9,507,1,1,1,1,3),_CpgGroupIpAddrCount_Type())
cpgGroupIpAddrCount.setMaxAccess(_D)
if mibBuilder.loadTexts:cpgGroupIpAddrCount.setStatus(_A)
_CpgGroupRowStatus_Type=RowStatus
_CpgGroupRowStatus_Object=MibTableColumn
cpgGroupRowStatus=_CpgGroupRowStatus_Object((1,3,6,1,4,1,9,9,507,1,1,1,1,4),_CpgGroupRowStatus_Type())
cpgGroupRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:cpgGroupRowStatus.setStatus(_A)
_CpgGroupIpTable_Object=MibTable
cpgGroupIpTable=_CpgGroupIpTable_Object((1,3,6,1,4,1,9,9,507,1,1,2))
if mibBuilder.loadTexts:cpgGroupIpTable.setStatus(_A)
_CpgGroupIpEntry_Object=MibTableRow
cpgGroupIpEntry=_CpgGroupIpEntry_Object((1,3,6,1,4,1,9,9,507,1,1,2,1))
cpgGroupIpEntry.setIndexNames((0,_B,_K),(0,_B,_L),(0,_B,_M))
if mibBuilder.loadTexts:cpgGroupIpEntry.setStatus(_A)
_CpgGroupIpGroupName_Type=CpgGroupName
_CpgGroupIpGroupName_Object=MibTableColumn
cpgGroupIpGroupName=_CpgGroupIpGroupName_Object((1,3,6,1,4,1,9,9,507,1,1,2,1,1),_CpgGroupIpGroupName_Type())
cpgGroupIpGroupName.setMaxAccess(_C)
if mibBuilder.loadTexts:cpgGroupIpGroupName.setStatus(_A)
_CpgGroupIpAddrType_Type=InetAddressType
_CpgGroupIpAddrType_Object=MibTableColumn
cpgGroupIpAddrType=_CpgGroupIpAddrType_Object((1,3,6,1,4,1,9,9,507,1,1,2,1,2),_CpgGroupIpAddrType_Type())
cpgGroupIpAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:cpgGroupIpAddrType.setStatus(_A)
class _CpgGroupIpAddress_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_CpgGroupIpAddress_Type.__name__=_F
_CpgGroupIpAddress_Object=MibTableColumn
cpgGroupIpAddress=_CpgGroupIpAddress_Object((1,3,6,1,4,1,9,9,507,1,1,2,1,3),_CpgGroupIpAddress_Type())
cpgGroupIpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:cpgGroupIpAddress.setStatus(_A)
class _CpgGroupIpMask_Type(InetAddress):defaultHexValue='FFFFFFFF'
_CpgGroupIpMask_Type.__name__=_F
_CpgGroupIpMask_Object=MibTableColumn
cpgGroupIpMask=_CpgGroupIpMask_Object((1,3,6,1,4,1,9,9,507,1,1,2,1,4),_CpgGroupIpMask_Type())
cpgGroupIpMask.setMaxAccess(_E)
if mibBuilder.loadTexts:cpgGroupIpMask.setStatus(_A)
class _CpgGroupIpSourceType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('other',1),(_J,2),('dot1x',3),('nac',4),('webAuth',5),('macAuth',6)))
_CpgGroupIpSourceType_Type.__name__=_G
_CpgGroupIpSourceType_Object=MibTableColumn
cpgGroupIpSourceType=_CpgGroupIpSourceType_Object((1,3,6,1,4,1,9,9,507,1,1,2,1,5),_CpgGroupIpSourceType_Type())
cpgGroupIpSourceType.setMaxAccess(_D)
if mibBuilder.loadTexts:cpgGroupIpSourceType.setStatus(_A)
_CpgGroupIpRowStatus_Type=RowStatus
_CpgGroupIpRowStatus_Object=MibTableColumn
cpgGroupIpRowStatus=_CpgGroupIpRowStatus_Object((1,3,6,1,4,1,9,9,507,1,1,2,1,6),_CpgGroupIpRowStatus_Type())
cpgGroupIpRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:cpgGroupIpRowStatus.setStatus(_A)
_CpgPolicy_ObjectIdentity=ObjectIdentity
cpgPolicy=_CpgPolicy_ObjectIdentity((1,3,6,1,4,1,9,9,507,1,2))
_CpgPolicyTable_Object=MibTable
cpgPolicyTable=_CpgPolicyTable_Object((1,3,6,1,4,1,9,9,507,1,2,1))
if mibBuilder.loadTexts:cpgPolicyTable.setStatus(_A)
_CpgPolicyEntry_Object=MibTableRow
cpgPolicyEntry=_CpgPolicyEntry_Object((1,3,6,1,4,1,9,9,507,1,2,1,1))
cpgPolicyEntry.setIndexNames((1,_B,_N))
if mibBuilder.loadTexts:cpgPolicyEntry.setStatus(_A)
_CpgPolicyName_Type=CpgPolicyName
_CpgPolicyName_Object=MibTableColumn
cpgPolicyName=_CpgPolicyName_Object((1,3,6,1,4,1,9,9,507,1,2,1,1,1),_CpgPolicyName_Type())
cpgPolicyName.setMaxAccess(_C)
if mibBuilder.loadTexts:cpgPolicyName.setStatus(_A)
_CpgPolicyGroupCount_Type=Unsigned32
_CpgPolicyGroupCount_Object=MibTableColumn
cpgPolicyGroupCount=_CpgPolicyGroupCount_Object((1,3,6,1,4,1,9,9,507,1,2,1,1,2),_CpgPolicyGroupCount_Type())
cpgPolicyGroupCount.setMaxAccess(_D)
if mibBuilder.loadTexts:cpgPolicyGroupCount.setStatus(_A)
_CpgPolicyGroupTable_Object=MibTable
cpgPolicyGroupTable=_CpgPolicyGroupTable_Object((1,3,6,1,4,1,9,9,507,1,2,2))
if mibBuilder.loadTexts:cpgPolicyGroupTable.setStatus(_A)
_CpgPolicyGroupEntry_Object=MibTableRow
cpgPolicyGroupEntry=_CpgPolicyGroupEntry_Object((1,3,6,1,4,1,9,9,507,1,2,2,1))
cpgPolicyGroupEntry.setIndexNames((0,_B,_O),(1,_B,_P))
if mibBuilder.loadTexts:cpgPolicyGroupEntry.setStatus(_A)
_CpgPolicyGroupPolicyName_Type=CpgPolicyName
_CpgPolicyGroupPolicyName_Object=MibTableColumn
cpgPolicyGroupPolicyName=_CpgPolicyGroupPolicyName_Object((1,3,6,1,4,1,9,9,507,1,2,2,1,1),_CpgPolicyGroupPolicyName_Type())
cpgPolicyGroupPolicyName.setMaxAccess(_C)
if mibBuilder.loadTexts:cpgPolicyGroupPolicyName.setStatus(_A)
_CpgPolicyGroupGroupName_Type=CpgGroupName
_CpgPolicyGroupGroupName_Object=MibTableColumn
cpgPolicyGroupGroupName=_CpgPolicyGroupGroupName_Object((1,3,6,1,4,1,9,9,507,1,2,2,1,2),_CpgPolicyGroupGroupName_Type())
cpgPolicyGroupGroupName.setMaxAccess(_C)
if mibBuilder.loadTexts:cpgPolicyGroupGroupName.setStatus(_A)
_CpgPolicyGroupRowStatus_Type=RowStatus
_CpgPolicyGroupRowStatus_Object=MibTableColumn
cpgPolicyGroupRowStatus=_CpgPolicyGroupRowStatus_Object((1,3,6,1,4,1,9,9,507,1,2,2,1,3),_CpgPolicyGroupRowStatus_Type())
cpgPolicyGroupRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:cpgPolicyGroupRowStatus.setStatus(_A)
_CiscoPolicyGroupMIBConformance_ObjectIdentity=ObjectIdentity
ciscoPolicyGroupMIBConformance=_CiscoPolicyGroupMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,9,507,2))
_CiscoPolicyGroupMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoPolicyGroupMIBCompliances=_CiscoPolicyGroupMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,507,2,1))
_CiscoPolicyGroupMIBGroups_ObjectIdentity=ObjectIdentity
ciscoPolicyGroupMIBGroups=_CiscoPolicyGroupMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,507,2,2))
ciscoCpgGroupInfoGroup=ObjectGroup((1,3,6,1,4,1,9,9,507,2,2,1))
ciscoCpgGroupInfoGroup.setObjects(*((_B,_Q),(_B,_R),(_B,_S)))
if mibBuilder.loadTexts:ciscoCpgGroupInfoGroup.setStatus(_A)
ciscoCpgGroupIpInfoGroup=ObjectGroup((1,3,6,1,4,1,9,9,507,2,2,2))
ciscoCpgGroupIpInfoGroup.setObjects(*((_B,_T),(_B,_U),(_B,_V)))
if mibBuilder.loadTexts:ciscoCpgGroupIpInfoGroup.setStatus(_A)
ciscoCpgPolicyInfoGroup=ObjectGroup((1,3,6,1,4,1,9,9,507,2,2,3))
ciscoCpgPolicyInfoGroup.setObjects((_B,_W))
if mibBuilder.loadTexts:ciscoCpgPolicyInfoGroup.setStatus(_A)
ciscoCpgPolicyGroupInfoGroup=ObjectGroup((1,3,6,1,4,1,9,9,507,2,2,4))
ciscoCpgPolicyGroupInfoGroup.setObjects((_B,_X))
if mibBuilder.loadTexts:ciscoCpgPolicyGroupInfoGroup.setStatus(_A)
ciscoPolicyGroupMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,507,2,1,1))
ciscoPolicyGroupMIBCompliance.setObjects(*((_B,_Y),(_B,_Z),(_B,_a),(_B,_b)))
if mibBuilder.loadTexts:ciscoPolicyGroupMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'CpgPolicyName':CpgPolicyName,'CpgPolicyNameOrEmpty':CpgPolicyNameOrEmpty,'CpgGroupName':CpgGroupName,'ciscoPolicyGroupMIB':ciscoPolicyGroupMIB,'ciscoPolicyGroupMIBNotifs':ciscoPolicyGroupMIBNotifs,'ciscoPolicyGroupMIBObjects':ciscoPolicyGroupMIBObjects,'cpgGroup':cpgGroup,'cpgGroupTable':cpgGroupTable,'cpgGroupEntry':cpgGroupEntry,_I:cpgGroupName,_Q:cpgGroupSourceType,_R:cpgGroupIpAddrCount,_S:cpgGroupRowStatus,'cpgGroupIpTable':cpgGroupIpTable,'cpgGroupIpEntry':cpgGroupIpEntry,_K:cpgGroupIpGroupName,_L:cpgGroupIpAddrType,_M:cpgGroupIpAddress,_T:cpgGroupIpMask,_U:cpgGroupIpSourceType,_V:cpgGroupIpRowStatus,'cpgPolicy':cpgPolicy,'cpgPolicyTable':cpgPolicyTable,'cpgPolicyEntry':cpgPolicyEntry,_N:cpgPolicyName,_W:cpgPolicyGroupCount,'cpgPolicyGroupTable':cpgPolicyGroupTable,'cpgPolicyGroupEntry':cpgPolicyGroupEntry,_O:cpgPolicyGroupPolicyName,_P:cpgPolicyGroupGroupName,_X:cpgPolicyGroupRowStatus,'ciscoPolicyGroupMIBConformance':ciscoPolicyGroupMIBConformance,'ciscoPolicyGroupMIBCompliances':ciscoPolicyGroupMIBCompliances,'ciscoPolicyGroupMIBCompliance':ciscoPolicyGroupMIBCompliance,'ciscoPolicyGroupMIBGroups':ciscoPolicyGroupMIBGroups,_Z:ciscoCpgGroupInfoGroup,_a:ciscoCpgGroupIpInfoGroup,_Y:ciscoCpgPolicyInfoGroup,_b:ciscoCpgPolicyGroupInfoGroup})