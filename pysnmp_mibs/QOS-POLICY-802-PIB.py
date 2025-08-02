_n='qos802AclDefinitionGroup'
_m='qos802AceGroup'
_l='qos802CosToDscpGroup'
_k='qos802DscpMappingGroup'
_j='qos802AclDefinitionLabel'
_i='qos802AclDefinitionStatus'
_h='qos802AclDefinitionStorageType'
_g='qos802AclDefinitionAceOrder'
_f='qos802AclDefinitionAceId'
_e='qos802AclDefinitionAclId'
_d='qos802AceStatus'
_c='qos802AceStorageType'
_b='qos802AcePermit'
_a='qos802AceUserPriority'
_Z='qos802AceEtherType'
_Y='qos802AceVlanTagRequired'
_X='qos802AceVlanId'
_W='qos802AceSrcAddrMask'
_V='qos802AceSrcAddr'
_U='qos802AceDstAddrMask'
_T='qos802AceDstAddr'
_S='qos802CosToDscpStatus'
_R='qos802CosToDscpStorageType'
_Q='qos802CosToDscpDscp'
_P='qos802CosToDscpCos'
_O='qos802DscpMappingStatus'
_N='qos802DscpMappingStorageType'
_M='qos802DscpMapping802Cos'
_L='qos802DscpMappingDscp'
_K='qos802AclDefinitionId'
_J='qos802AceId'
_I='qos802CosToDscpId'
_H='qos802DscpMappingId'
_G='SnmpAdminString'
_F='not-accessible'
_E='Integer32'
_D='StorageType'
_C='read-create'
_B='QOS-POLICY-802-PIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
PolicyInstanceId,=mibBuilder.importSymbols('POLICY-FRAMEWORK-PIB','PolicyInstanceId')
Dscp,=mibBuilder.importSymbols('QOS-POLICY-IP-PIB','Dscp')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_G)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,StorageType,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus',_D,'TextualConvention','TruthValue')
policy,=mibBuilder.importSymbols('SYNOPTICS-ROOT-MIB','policy')
qosPolicy802Pib=ModuleIdentity((1,3,6,1,4,1,45,4,3))
if mibBuilder.loadTexts:qosPolicy802Pib.setRevisions(('2004-07-20 00:00',))
class QosIeee802Cos(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_QosPolicy802PibClasses_ObjectIdentity=ObjectIdentity
qosPolicy802PibClasses=_QosPolicy802PibClasses_ObjectIdentity((1,3,6,1,4,1,45,4,3,1))
_Qos802DomainConfig_ObjectIdentity=ObjectIdentity
qos802DomainConfig=_Qos802DomainConfig_ObjectIdentity((1,3,6,1,4,1,45,4,3,1,1))
_Qos802DscpMappingTable_Object=MibTable
qos802DscpMappingTable=_Qos802DscpMappingTable_Object((1,3,6,1,4,1,45,4,3,1,1,1))
if mibBuilder.loadTexts:qos802DscpMappingTable.setStatus(_A)
_Qos802DscpMappingEntry_Object=MibTableRow
qos802DscpMappingEntry=_Qos802DscpMappingEntry_Object((1,3,6,1,4,1,45,4,3,1,1,1,1))
qos802DscpMappingEntry.setIndexNames((0,_B,_H))
if mibBuilder.loadTexts:qos802DscpMappingEntry.setStatus(_A)
_Qos802DscpMappingId_Type=PolicyInstanceId
_Qos802DscpMappingId_Object=MibTableColumn
qos802DscpMappingId=_Qos802DscpMappingId_Object((1,3,6,1,4,1,45,4,3,1,1,1,1,1),_Qos802DscpMappingId_Type())
qos802DscpMappingId.setMaxAccess(_F)
if mibBuilder.loadTexts:qos802DscpMappingId.setStatus(_A)
_Qos802DscpMappingDscp_Type=Dscp
_Qos802DscpMappingDscp_Object=MibTableColumn
qos802DscpMappingDscp=_Qos802DscpMappingDscp_Object((1,3,6,1,4,1,45,4,3,1,1,1,1,2),_Qos802DscpMappingDscp_Type())
qos802DscpMappingDscp.setMaxAccess(_C)
if mibBuilder.loadTexts:qos802DscpMappingDscp.setStatus(_A)
_Qos802DscpMapping802Cos_Type=QosIeee802Cos
_Qos802DscpMapping802Cos_Object=MibTableColumn
qos802DscpMapping802Cos=_Qos802DscpMapping802Cos_Object((1,3,6,1,4,1,45,4,3,1,1,1,1,3),_Qos802DscpMapping802Cos_Type())
qos802DscpMapping802Cos.setMaxAccess(_C)
if mibBuilder.loadTexts:qos802DscpMapping802Cos.setStatus(_A)
class _Qos802DscpMappingStorageType_Type(StorageType):defaultValue=2
_Qos802DscpMappingStorageType_Type.__name__=_D
_Qos802DscpMappingStorageType_Object=MibTableColumn
qos802DscpMappingStorageType=_Qos802DscpMappingStorageType_Object((1,3,6,1,4,1,45,4,3,1,1,1,1,4),_Qos802DscpMappingStorageType_Type())
qos802DscpMappingStorageType.setMaxAccess(_C)
if mibBuilder.loadTexts:qos802DscpMappingStorageType.setStatus(_A)
_Qos802DscpMappingStatus_Type=RowStatus
_Qos802DscpMappingStatus_Object=MibTableColumn
qos802DscpMappingStatus=_Qos802DscpMappingStatus_Object((1,3,6,1,4,1,45,4,3,1,1,1,1,5),_Qos802DscpMappingStatus_Type())
qos802DscpMappingStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:qos802DscpMappingStatus.setStatus(_A)
_Qos802CosToDscpTable_Object=MibTable
qos802CosToDscpTable=_Qos802CosToDscpTable_Object((1,3,6,1,4,1,45,4,3,1,1,2))
if mibBuilder.loadTexts:qos802CosToDscpTable.setStatus(_A)
_Qos802CosToDscpEntry_Object=MibTableRow
qos802CosToDscpEntry=_Qos802CosToDscpEntry_Object((1,3,6,1,4,1,45,4,3,1,1,2,1))
qos802CosToDscpEntry.setIndexNames((0,_B,_I))
if mibBuilder.loadTexts:qos802CosToDscpEntry.setStatus(_A)
_Qos802CosToDscpId_Type=PolicyInstanceId
_Qos802CosToDscpId_Object=MibTableColumn
qos802CosToDscpId=_Qos802CosToDscpId_Object((1,3,6,1,4,1,45,4,3,1,1,2,1,1),_Qos802CosToDscpId_Type())
qos802CosToDscpId.setMaxAccess(_F)
if mibBuilder.loadTexts:qos802CosToDscpId.setStatus(_A)
_Qos802CosToDscpCos_Type=QosIeee802Cos
_Qos802CosToDscpCos_Object=MibTableColumn
qos802CosToDscpCos=_Qos802CosToDscpCos_Object((1,3,6,1,4,1,45,4,3,1,1,2,1,2),_Qos802CosToDscpCos_Type())
qos802CosToDscpCos.setMaxAccess(_C)
if mibBuilder.loadTexts:qos802CosToDscpCos.setStatus(_A)
_Qos802CosToDscpDscp_Type=Dscp
_Qos802CosToDscpDscp_Object=MibTableColumn
qos802CosToDscpDscp=_Qos802CosToDscpDscp_Object((1,3,6,1,4,1,45,4,3,1,1,2,1,3),_Qos802CosToDscpDscp_Type())
qos802CosToDscpDscp.setMaxAccess(_C)
if mibBuilder.loadTexts:qos802CosToDscpDscp.setStatus(_A)
class _Qos802CosToDscpStorageType_Type(StorageType):defaultValue=2
_Qos802CosToDscpStorageType_Type.__name__=_D
_Qos802CosToDscpStorageType_Object=MibTableColumn
qos802CosToDscpStorageType=_Qos802CosToDscpStorageType_Object((1,3,6,1,4,1,45,4,3,1,1,2,1,4),_Qos802CosToDscpStorageType_Type())
qos802CosToDscpStorageType.setMaxAccess(_C)
if mibBuilder.loadTexts:qos802CosToDscpStorageType.setStatus(_A)
_Qos802CosToDscpStatus_Type=RowStatus
_Qos802CosToDscpStatus_Object=MibTableColumn
qos802CosToDscpStatus=_Qos802CosToDscpStatus_Object((1,3,6,1,4,1,45,4,3,1,1,2,1,5),_Qos802CosToDscpStatus_Type())
qos802CosToDscpStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:qos802CosToDscpStatus.setStatus(_A)
_Qos802Qos_ObjectIdentity=ObjectIdentity
qos802Qos=_Qos802Qos_ObjectIdentity((1,3,6,1,4,1,45,4,3,1,2))
_Qos802AceTable_Object=MibTable
qos802AceTable=_Qos802AceTable_Object((1,3,6,1,4,1,45,4,3,1,2,1))
if mibBuilder.loadTexts:qos802AceTable.setStatus(_A)
_Qos802AceEntry_Object=MibTableRow
qos802AceEntry=_Qos802AceEntry_Object((1,3,6,1,4,1,45,4,3,1,2,1,1))
qos802AceEntry.setIndexNames((0,_B,_J))
if mibBuilder.loadTexts:qos802AceEntry.setStatus(_A)
_Qos802AceId_Type=PolicyInstanceId
_Qos802AceId_Object=MibTableColumn
qos802AceId=_Qos802AceId_Object((1,3,6,1,4,1,45,4,3,1,2,1,1,1),_Qos802AceId_Type())
qos802AceId.setMaxAccess(_F)
if mibBuilder.loadTexts:qos802AceId.setStatus(_A)
_Qos802AceDstAddr_Type=PhysAddress
_Qos802AceDstAddr_Object=MibTableColumn
qos802AceDstAddr=_Qos802AceDstAddr_Object((1,3,6,1,4,1,45,4,3,1,2,1,1,2),_Qos802AceDstAddr_Type())
qos802AceDstAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:qos802AceDstAddr.setStatus(_A)
_Qos802AceDstAddrMask_Type=PhysAddress
_Qos802AceDstAddrMask_Object=MibTableColumn
qos802AceDstAddrMask=_Qos802AceDstAddrMask_Object((1,3,6,1,4,1,45,4,3,1,2,1,1,3),_Qos802AceDstAddrMask_Type())
qos802AceDstAddrMask.setMaxAccess(_C)
if mibBuilder.loadTexts:qos802AceDstAddrMask.setStatus(_A)
_Qos802AceSrcAddr_Type=PhysAddress
_Qos802AceSrcAddr_Object=MibTableColumn
qos802AceSrcAddr=_Qos802AceSrcAddr_Object((1,3,6,1,4,1,45,4,3,1,2,1,1,4),_Qos802AceSrcAddr_Type())
qos802AceSrcAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:qos802AceSrcAddr.setStatus(_A)
_Qos802AceSrcAddrMask_Type=PhysAddress
_Qos802AceSrcAddrMask_Object=MibTableColumn
qos802AceSrcAddrMask=_Qos802AceSrcAddrMask_Object((1,3,6,1,4,1,45,4,3,1,2,1,1,5),_Qos802AceSrcAddrMask_Type())
qos802AceSrcAddrMask.setMaxAccess(_C)
if mibBuilder.loadTexts:qos802AceSrcAddrMask.setStatus(_A)
class _Qos802AceVlanId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,-1),ValueRangeConstraint(1,4094))
_Qos802AceVlanId_Type.__name__=_E
_Qos802AceVlanId_Object=MibTableColumn
qos802AceVlanId=_Qos802AceVlanId_Object((1,3,6,1,4,1,45,4,3,1,2,1,1,6),_Qos802AceVlanId_Type())
qos802AceVlanId.setMaxAccess(_C)
if mibBuilder.loadTexts:qos802AceVlanId.setStatus(_A)
class _Qos802AceVlanTagRequired_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('taggedOnly',1),('priorityTagged',2),('untaggedOnly',3),('ignoreTag',4)))
_Qos802AceVlanTagRequired_Type.__name__=_E
_Qos802AceVlanTagRequired_Object=MibTableColumn
qos802AceVlanTagRequired=_Qos802AceVlanTagRequired_Object((1,3,6,1,4,1,45,4,3,1,2,1,1,7),_Qos802AceVlanTagRequired_Type())
qos802AceVlanTagRequired.setMaxAccess(_C)
if mibBuilder.loadTexts:qos802AceVlanTagRequired.setStatus(_A)
class _Qos802AceEtherType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,-1),ValueRangeConstraint(0,65535))
_Qos802AceEtherType_Type.__name__=_E
_Qos802AceEtherType_Object=MibTableColumn
qos802AceEtherType=_Qos802AceEtherType_Object((1,3,6,1,4,1,45,4,3,1,2,1,1,8),_Qos802AceEtherType_Type())
qos802AceEtherType.setMaxAccess(_C)
if mibBuilder.loadTexts:qos802AceEtherType.setStatus(_A)
class _Qos802AceUserPriority_Type(Bits):namedValues=NamedValues(*(('matchPriority0',0),('matchPriority1',1),('matchPriority2',2),('matchPriority3',3),('matchPriority4',4),('matchPriority5',5),('matchPriority6',6),('matchPriority7',7)))
_Qos802AceUserPriority_Type.__name__='Bits'
_Qos802AceUserPriority_Object=MibTableColumn
qos802AceUserPriority=_Qos802AceUserPriority_Object((1,3,6,1,4,1,45,4,3,1,2,1,1,9),_Qos802AceUserPriority_Type())
qos802AceUserPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:qos802AceUserPriority.setStatus(_A)
_Qos802AcePermit_Type=TruthValue
_Qos802AcePermit_Object=MibTableColumn
qos802AcePermit=_Qos802AcePermit_Object((1,3,6,1,4,1,45,4,3,1,2,1,1,10),_Qos802AcePermit_Type())
qos802AcePermit.setMaxAccess(_C)
if mibBuilder.loadTexts:qos802AcePermit.setStatus(_A)
class _Qos802AceStorageType_Type(StorageType):defaultValue=2
_Qos802AceStorageType_Type.__name__=_D
_Qos802AceStorageType_Object=MibTableColumn
qos802AceStorageType=_Qos802AceStorageType_Object((1,3,6,1,4,1,45,4,3,1,2,1,1,11),_Qos802AceStorageType_Type())
qos802AceStorageType.setMaxAccess(_C)
if mibBuilder.loadTexts:qos802AceStorageType.setStatus(_A)
_Qos802AceStatus_Type=RowStatus
_Qos802AceStatus_Object=MibTableColumn
qos802AceStatus=_Qos802AceStatus_Object((1,3,6,1,4,1,45,4,3,1,2,1,1,12),_Qos802AceStatus_Type())
qos802AceStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:qos802AceStatus.setStatus(_A)
_Qos802AclDefinitionTable_Object=MibTable
qos802AclDefinitionTable=_Qos802AclDefinitionTable_Object((1,3,6,1,4,1,45,4,3,1,2,2))
if mibBuilder.loadTexts:qos802AclDefinitionTable.setStatus(_A)
_Qos802AclDefinitionEntry_Object=MibTableRow
qos802AclDefinitionEntry=_Qos802AclDefinitionEntry_Object((1,3,6,1,4,1,45,4,3,1,2,2,1))
qos802AclDefinitionEntry.setIndexNames((0,_B,_K))
if mibBuilder.loadTexts:qos802AclDefinitionEntry.setStatus(_A)
_Qos802AclDefinitionId_Type=PolicyInstanceId
_Qos802AclDefinitionId_Object=MibTableColumn
qos802AclDefinitionId=_Qos802AclDefinitionId_Object((1,3,6,1,4,1,45,4,3,1,2,2,1,1),_Qos802AclDefinitionId_Type())
qos802AclDefinitionId.setMaxAccess(_F)
if mibBuilder.loadTexts:qos802AclDefinitionId.setStatus(_A)
_Qos802AclDefinitionAclId_Type=PolicyInstanceId
_Qos802AclDefinitionAclId_Object=MibTableColumn
qos802AclDefinitionAclId=_Qos802AclDefinitionAclId_Object((1,3,6,1,4,1,45,4,3,1,2,2,1,2),_Qos802AclDefinitionAclId_Type())
qos802AclDefinitionAclId.setMaxAccess(_C)
if mibBuilder.loadTexts:qos802AclDefinitionAclId.setStatus(_A)
_Qos802AclDefinitionAceId_Type=PolicyInstanceId
_Qos802AclDefinitionAceId_Object=MibTableColumn
qos802AclDefinitionAceId=_Qos802AclDefinitionAceId_Object((1,3,6,1,4,1,45,4,3,1,2,2,1,3),_Qos802AclDefinitionAceId_Type())
qos802AclDefinitionAceId.setMaxAccess(_C)
if mibBuilder.loadTexts:qos802AclDefinitionAceId.setStatus(_A)
_Qos802AclDefinitionAceOrder_Type=Unsigned32
_Qos802AclDefinitionAceOrder_Object=MibTableColumn
qos802AclDefinitionAceOrder=_Qos802AclDefinitionAceOrder_Object((1,3,6,1,4,1,45,4,3,1,2,2,1,4),_Qos802AclDefinitionAceOrder_Type())
qos802AclDefinitionAceOrder.setMaxAccess(_C)
if mibBuilder.loadTexts:qos802AclDefinitionAceOrder.setStatus(_A)
class _Qos802AclDefinitionStorageType_Type(StorageType):defaultValue=2
_Qos802AclDefinitionStorageType_Type.__name__=_D
_Qos802AclDefinitionStorageType_Object=MibTableColumn
qos802AclDefinitionStorageType=_Qos802AclDefinitionStorageType_Object((1,3,6,1,4,1,45,4,3,1,2,2,1,5),_Qos802AclDefinitionStorageType_Type())
qos802AclDefinitionStorageType.setMaxAccess(_C)
if mibBuilder.loadTexts:qos802AclDefinitionStorageType.setStatus(_A)
_Qos802AclDefinitionStatus_Type=RowStatus
_Qos802AclDefinitionStatus_Object=MibTableColumn
qos802AclDefinitionStatus=_Qos802AclDefinitionStatus_Object((1,3,6,1,4,1,45,4,3,1,2,2,1,6),_Qos802AclDefinitionStatus_Type())
qos802AclDefinitionStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:qos802AclDefinitionStatus.setStatus(_A)
class _Qos802AclDefinitionLabel_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_Qos802AclDefinitionLabel_Type.__name__=_G
_Qos802AclDefinitionLabel_Object=MibTableColumn
qos802AclDefinitionLabel=_Qos802AclDefinitionLabel_Object((1,3,6,1,4,1,45,4,3,1,2,2,1,7),_Qos802AclDefinitionLabel_Type())
qos802AclDefinitionLabel.setMaxAccess(_C)
if mibBuilder.loadTexts:qos802AclDefinitionLabel.setStatus(_A)
_QosPolicy802PibConformance_ObjectIdentity=ObjectIdentity
qosPolicy802PibConformance=_QosPolicy802PibConformance_ObjectIdentity((1,3,6,1,4,1,45,4,3,2))
_QosPolicy802PibCompliances_ObjectIdentity=ObjectIdentity
qosPolicy802PibCompliances=_QosPolicy802PibCompliances_ObjectIdentity((1,3,6,1,4,1,45,4,3,2,1))
_QosPolicy802PibGroups_ObjectIdentity=ObjectIdentity
qosPolicy802PibGroups=_QosPolicy802PibGroups_ObjectIdentity((1,3,6,1,4,1,45,4,3,2,2))
qos802DscpMappingGroup=ObjectGroup((1,3,6,1,4,1,45,4,3,2,2,1))
qos802DscpMappingGroup.setObjects(*((_B,_L),(_B,_M),(_B,_N),(_B,_O)))
if mibBuilder.loadTexts:qos802DscpMappingGroup.setStatus(_A)
qos802CosToDscpGroup=ObjectGroup((1,3,6,1,4,1,45,4,3,2,2,2))
qos802CosToDscpGroup.setObjects(*((_B,_P),(_B,_Q),(_B,_R),(_B,_S)))
if mibBuilder.loadTexts:qos802CosToDscpGroup.setStatus(_A)
qos802AceGroup=ObjectGroup((1,3,6,1,4,1,45,4,3,2,2,3))
qos802AceGroup.setObjects(*((_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d)))
if mibBuilder.loadTexts:qos802AceGroup.setStatus(_A)
qos802AclDefinitionGroup=ObjectGroup((1,3,6,1,4,1,45,4,3,2,2,4))
qos802AclDefinitionGroup.setObjects(*((_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j)))
if mibBuilder.loadTexts:qos802AclDefinitionGroup.setStatus(_A)
qosPolicy802PibCompliance=ModuleCompliance((1,3,6,1,4,1,45,4,3,2,1,1))
qosPolicy802PibCompliance.setObjects(*((_B,_k),(_B,_l),(_B,_m),(_B,_n)))
if mibBuilder.loadTexts:qosPolicy802PibCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'QosIeee802Cos':QosIeee802Cos,'qosPolicy802Pib':qosPolicy802Pib,'qosPolicy802PibClasses':qosPolicy802PibClasses,'qos802DomainConfig':qos802DomainConfig,'qos802DscpMappingTable':qos802DscpMappingTable,'qos802DscpMappingEntry':qos802DscpMappingEntry,_H:qos802DscpMappingId,_L:qos802DscpMappingDscp,_M:qos802DscpMapping802Cos,_N:qos802DscpMappingStorageType,_O:qos802DscpMappingStatus,'qos802CosToDscpTable':qos802CosToDscpTable,'qos802CosToDscpEntry':qos802CosToDscpEntry,_I:qos802CosToDscpId,_P:qos802CosToDscpCos,_Q:qos802CosToDscpDscp,_R:qos802CosToDscpStorageType,_S:qos802CosToDscpStatus,'qos802Qos':qos802Qos,'qos802AceTable':qos802AceTable,'qos802AceEntry':qos802AceEntry,_J:qos802AceId,_T:qos802AceDstAddr,_U:qos802AceDstAddrMask,_V:qos802AceSrcAddr,_W:qos802AceSrcAddrMask,_X:qos802AceVlanId,_Y:qos802AceVlanTagRequired,_Z:qos802AceEtherType,_a:qos802AceUserPriority,_b:qos802AcePermit,_c:qos802AceStorageType,_d:qos802AceStatus,'qos802AclDefinitionTable':qos802AclDefinitionTable,'qos802AclDefinitionEntry':qos802AclDefinitionEntry,_K:qos802AclDefinitionId,_e:qos802AclDefinitionAclId,_f:qos802AclDefinitionAceId,_g:qos802AclDefinitionAceOrder,_h:qos802AclDefinitionStorageType,_i:qos802AclDefinitionStatus,_j:qos802AclDefinitionLabel,'qosPolicy802PibConformance':qosPolicy802PibConformance,'qosPolicy802PibCompliances':qosPolicy802PibCompliances,'qosPolicy802PibCompliance':qosPolicy802PibCompliance,'qosPolicy802PibGroups':qosPolicy802PibGroups,_k:qos802DscpMappingGroup,_l:qos802CosToDscpGroup,_m:qos802AceGroup,_n:qos802AclDefinitionGroup})