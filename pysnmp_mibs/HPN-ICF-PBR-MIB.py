_S='hpnicfPBRNexthopAddr'
_R='hpnicfPBRNexthopAddrType'
_Q='hpnicfPBRMibApplyDefaultNexthopIndex'
_P='hpnicfPBRMibApplyNexthopIndex'
_O='hpnicfPBRMibPolicyAddressType'
_N='accessible-for-notify'
_M='ifIndex'
_L='IF-MIB'
_K='Integer32'
_J='read-write'
_I='not-accessible'
_H='hpnicfPBRMibPolicyNodeId'
_G='hpnicfPBRMibPolicyName'
_F='hpnicfPBRMibPolicyNodeAddrType'
_E='TruthValue'
_D='DisplayString'
_C='read-create'
_B='HPN-ICF-PBR-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hpnicfCommon,=mibBuilder.importSymbols('HPN-ICF-OID-MIB','hpnicfCommon')
ifIndex,=mibBuilder.importSymbols(_L,_M)
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_K,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_D,'PhysAddress','RowStatus','TextualConvention',_E)
hpnicfPBR=ModuleIdentity((1,3,6,1,4,1,11,2,14,11,15,2,113))
if mibBuilder.loadTexts:hpnicfPBR.setRevisions(('2010-12-10 15:58',))
_HpnicfPBRObjects_ObjectIdentity=ObjectIdentity
hpnicfPBRObjects=_HpnicfPBRObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,113,1))
_HpnicfPBRGlobal_ObjectIdentity=ObjectIdentity
hpnicfPBRGlobal=_HpnicfPBRGlobal_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,113,1,1))
class _HpnicfPBRNexthopTrapEnabled_Type(TruthValue):defaultValue=1
_HpnicfPBRNexthopTrapEnabled_Type.__name__=_E
_HpnicfPBRNexthopTrapEnabled_Object=MibScalar
hpnicfPBRNexthopTrapEnabled=_HpnicfPBRNexthopTrapEnabled_Object((1,3,6,1,4,1,11,2,14,11,15,2,113,1,1,1),_HpnicfPBRNexthopTrapEnabled_Type())
hpnicfPBRNexthopTrapEnabled.setMaxAccess(_J)
if mibBuilder.loadTexts:hpnicfPBRNexthopTrapEnabled.setStatus(_A)
class _HpnicfPBRLocalPolicy_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,19))
_HpnicfPBRLocalPolicy_Type.__name__=_D
_HpnicfPBRLocalPolicy_Object=MibScalar
hpnicfPBRLocalPolicy=_HpnicfPBRLocalPolicy_Object((1,3,6,1,4,1,11,2,14,11,15,2,113,1,1,2),_HpnicfPBRLocalPolicy_Type())
hpnicfPBRLocalPolicy.setMaxAccess(_J)
if mibBuilder.loadTexts:hpnicfPBRLocalPolicy.setStatus(_A)
class _HpnicfPBRIPv6NexthopTrapEnabled_Type(TruthValue):defaultValue=1
_HpnicfPBRIPv6NexthopTrapEnabled_Type.__name__=_E
_HpnicfPBRIPv6NexthopTrapEnabled_Object=MibScalar
hpnicfPBRIPv6NexthopTrapEnabled=_HpnicfPBRIPv6NexthopTrapEnabled_Object((1,3,6,1,4,1,11,2,14,11,15,2,113,1,1,3),_HpnicfPBRIPv6NexthopTrapEnabled_Type())
hpnicfPBRIPv6NexthopTrapEnabled.setMaxAccess(_J)
if mibBuilder.loadTexts:hpnicfPBRIPv6NexthopTrapEnabled.setStatus(_A)
_HpnicfPBRMibTrap_ObjectIdentity=ObjectIdentity
hpnicfPBRMibTrap=_HpnicfPBRMibTrap_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,113,1,2))
_HpnicfPBRTrapObjects_ObjectIdentity=ObjectIdentity
hpnicfPBRTrapObjects=_HpnicfPBRTrapObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,113,1,2,1))
_HpnicfPBRNexthopAddrType_Type=InetAddressType
_HpnicfPBRNexthopAddrType_Object=MibScalar
hpnicfPBRNexthopAddrType=_HpnicfPBRNexthopAddrType_Object((1,3,6,1,4,1,11,2,14,11,15,2,113,1,2,1,1),_HpnicfPBRNexthopAddrType_Type())
hpnicfPBRNexthopAddrType.setMaxAccess(_N)
if mibBuilder.loadTexts:hpnicfPBRNexthopAddrType.setStatus(_A)
_HpnicfPBRNexthopAddr_Type=InetAddress
_HpnicfPBRNexthopAddr_Object=MibScalar
hpnicfPBRNexthopAddr=_HpnicfPBRNexthopAddr_Object((1,3,6,1,4,1,11,2,14,11,15,2,113,1,2,1,2),_HpnicfPBRNexthopAddr_Type())
hpnicfPBRNexthopAddr.setMaxAccess(_N)
if mibBuilder.loadTexts:hpnicfPBRNexthopAddr.setStatus(_A)
_HpnicfPBRTraps_ObjectIdentity=ObjectIdentity
hpnicfPBRTraps=_HpnicfPBRTraps_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,113,1,2,2))
_HpnicfPBRTrapsPrefix_ObjectIdentity=ObjectIdentity
hpnicfPBRTrapsPrefix=_HpnicfPBRTrapsPrefix_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,113,1,2,2,0))
_HpnicfPBRTables_ObjectIdentity=ObjectIdentity
hpnicfPBRTables=_HpnicfPBRTables_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,113,2))
_HpnicfPBRMibPolicyNodeTable_Object=MibTable
hpnicfPBRMibPolicyNodeTable=_HpnicfPBRMibPolicyNodeTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,113,2,1))
if mibBuilder.loadTexts:hpnicfPBRMibPolicyNodeTable.setStatus(_A)
_HpnicfPBRMibPolicyNodeEntry_Object=MibTableRow
hpnicfPBRMibPolicyNodeEntry=_HpnicfPBRMibPolicyNodeEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,113,2,1,1))
hpnicfPBRMibPolicyNodeEntry.setIndexNames((0,_B,_F),(0,_B,_G),(0,_B,_H))
if mibBuilder.loadTexts:hpnicfPBRMibPolicyNodeEntry.setStatus(_A)
_HpnicfPBRMibPolicyNodeAddrType_Type=InetAddressType
_HpnicfPBRMibPolicyNodeAddrType_Object=MibTableColumn
hpnicfPBRMibPolicyNodeAddrType=_HpnicfPBRMibPolicyNodeAddrType_Object((1,3,6,1,4,1,11,2,14,11,15,2,113,2,1,1,1),_HpnicfPBRMibPolicyNodeAddrType_Type())
hpnicfPBRMibPolicyNodeAddrType.setMaxAccess(_I)
if mibBuilder.loadTexts:hpnicfPBRMibPolicyNodeAddrType.setStatus(_A)
class _HpnicfPBRMibPolicyName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,19))
_HpnicfPBRMibPolicyName_Type.__name__=_D
_HpnicfPBRMibPolicyName_Object=MibTableColumn
hpnicfPBRMibPolicyName=_HpnicfPBRMibPolicyName_Object((1,3,6,1,4,1,11,2,14,11,15,2,113,2,1,1,2),_HpnicfPBRMibPolicyName_Type())
hpnicfPBRMibPolicyName.setMaxAccess(_I)
if mibBuilder.loadTexts:hpnicfPBRMibPolicyName.setStatus(_A)
class _HpnicfPBRMibPolicyNodeId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HpnicfPBRMibPolicyNodeId_Type.__name__=_K
_HpnicfPBRMibPolicyNodeId_Object=MibTableColumn
hpnicfPBRMibPolicyNodeId=_HpnicfPBRMibPolicyNodeId_Object((1,3,6,1,4,1,11,2,14,11,15,2,113,2,1,1,3),_HpnicfPBRMibPolicyNodeId_Type())
hpnicfPBRMibPolicyNodeId.setMaxAccess(_I)
if mibBuilder.loadTexts:hpnicfPBRMibPolicyNodeId.setStatus(_A)
class _HpnicfPBRMibPolicyNodeMode_Type(TruthValue):defaultValue=1
_HpnicfPBRMibPolicyNodeMode_Type.__name__=_E
_HpnicfPBRMibPolicyNodeMode_Object=MibTableColumn
hpnicfPBRMibPolicyNodeMode=_HpnicfPBRMibPolicyNodeMode_Object((1,3,6,1,4,1,11,2,14,11,15,2,113,2,1,1,4),_HpnicfPBRMibPolicyNodeMode_Type())
hpnicfPBRMibPolicyNodeMode.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfPBRMibPolicyNodeMode.setStatus(_A)
_HpnicfPBRMibPolicyNodeRowStatus_Type=RowStatus
_HpnicfPBRMibPolicyNodeRowStatus_Object=MibTableColumn
hpnicfPBRMibPolicyNodeRowStatus=_HpnicfPBRMibPolicyNodeRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,113,2,1,1,5),_HpnicfPBRMibPolicyNodeRowStatus_Type())
hpnicfPBRMibPolicyNodeRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfPBRMibPolicyNodeRowStatus.setStatus(_A)
_HpnicfPBRMibIfPolicyTable_Object=MibTable
hpnicfPBRMibIfPolicyTable=_HpnicfPBRMibIfPolicyTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,113,2,2))
if mibBuilder.loadTexts:hpnicfPBRMibIfPolicyTable.setStatus(_A)
_HpnicfPBRMibIfPolicyEntry_Object=MibTableRow
hpnicfPBRMibIfPolicyEntry=_HpnicfPBRMibIfPolicyEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,113,2,2,1))
hpnicfPBRMibIfPolicyEntry.setIndexNames((0,_B,_O),(0,_L,_M))
if mibBuilder.loadTexts:hpnicfPBRMibIfPolicyEntry.setStatus(_A)
_HpnicfPBRMibPolicyAddressType_Type=InetAddressType
_HpnicfPBRMibPolicyAddressType_Object=MibTableColumn
hpnicfPBRMibPolicyAddressType=_HpnicfPBRMibPolicyAddressType_Object((1,3,6,1,4,1,11,2,14,11,15,2,113,2,2,1,1),_HpnicfPBRMibPolicyAddressType_Type())
hpnicfPBRMibPolicyAddressType.setMaxAccess(_I)
if mibBuilder.loadTexts:hpnicfPBRMibPolicyAddressType.setStatus(_A)
class _HpnicfPBRMibAppliedPolicyName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,19))
_HpnicfPBRMibAppliedPolicyName_Type.__name__=_D
_HpnicfPBRMibAppliedPolicyName_Object=MibTableColumn
hpnicfPBRMibAppliedPolicyName=_HpnicfPBRMibAppliedPolicyName_Object((1,3,6,1,4,1,11,2,14,11,15,2,113,2,2,1,2),_HpnicfPBRMibAppliedPolicyName_Type())
hpnicfPBRMibAppliedPolicyName.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfPBRMibAppliedPolicyName.setStatus(_A)
_HpnicfPBRMibIfPolicyRowStatus_Type=RowStatus
_HpnicfPBRMibIfPolicyRowStatus_Object=MibTableColumn
hpnicfPBRMibIfPolicyRowStatus=_HpnicfPBRMibIfPolicyRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,113,2,2,1,3),_HpnicfPBRMibIfPolicyRowStatus_Type())
hpnicfPBRMibIfPolicyRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfPBRMibIfPolicyRowStatus.setStatus(_A)
_HpnicfPBRMibMatchAclTable_Object=MibTable
hpnicfPBRMibMatchAclTable=_HpnicfPBRMibMatchAclTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,113,2,3))
if mibBuilder.loadTexts:hpnicfPBRMibMatchAclTable.setStatus(_A)
_HpnicfPBRMibMatchAclEntry_Object=MibTableRow
hpnicfPBRMibMatchAclEntry=_HpnicfPBRMibMatchAclEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,113,2,3,1))
hpnicfPBRMibMatchAclEntry.setIndexNames((0,_B,_F),(0,_B,_G),(0,_B,_H))
if mibBuilder.loadTexts:hpnicfPBRMibMatchAclEntry.setStatus(_A)
_HpnicfPBRMibAclGroupId_Type=Integer32
_HpnicfPBRMibAclGroupId_Object=MibTableColumn
hpnicfPBRMibAclGroupId=_HpnicfPBRMibAclGroupId_Object((1,3,6,1,4,1,11,2,14,11,15,2,113,2,3,1,1),_HpnicfPBRMibAclGroupId_Type())
hpnicfPBRMibAclGroupId.setMaxAccess(_J)
if mibBuilder.loadTexts:hpnicfPBRMibAclGroupId.setStatus(_A)
_HpnicfPBRMibApplyPrecedenceTable_Object=MibTable
hpnicfPBRMibApplyPrecedenceTable=_HpnicfPBRMibApplyPrecedenceTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,113,2,4))
if mibBuilder.loadTexts:hpnicfPBRMibApplyPrecedenceTable.setStatus(_A)
_HpnicfPBRMibApplyPrecedenceEntry_Object=MibTableRow
hpnicfPBRMibApplyPrecedenceEntry=_HpnicfPBRMibApplyPrecedenceEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,113,2,4,1))
hpnicfPBRMibApplyPrecedenceEntry.setIndexNames((0,_B,_F),(0,_B,_G),(0,_B,_H))
if mibBuilder.loadTexts:hpnicfPBRMibApplyPrecedenceEntry.setStatus(_A)
_HpnicfPBRMibApplyPrecedenceValue_Type=Integer32
_HpnicfPBRMibApplyPrecedenceValue_Object=MibTableColumn
hpnicfPBRMibApplyPrecedenceValue=_HpnicfPBRMibApplyPrecedenceValue_Object((1,3,6,1,4,1,11,2,14,11,15,2,113,2,4,1,1),_HpnicfPBRMibApplyPrecedenceValue_Type())
hpnicfPBRMibApplyPrecedenceValue.setMaxAccess(_J)
if mibBuilder.loadTexts:hpnicfPBRMibApplyPrecedenceValue.setStatus(_A)
_HpnicfPBRMibApplyNexthopTable_Object=MibTable
hpnicfPBRMibApplyNexthopTable=_HpnicfPBRMibApplyNexthopTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,113,2,5))
if mibBuilder.loadTexts:hpnicfPBRMibApplyNexthopTable.setStatus(_A)
_HpnicfPBRMibApplyNexthopEntry_Object=MibTableRow
hpnicfPBRMibApplyNexthopEntry=_HpnicfPBRMibApplyNexthopEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,113,2,5,1))
hpnicfPBRMibApplyNexthopEntry.setIndexNames((0,_B,_F),(0,_B,_G),(0,_B,_H),(0,_B,_P))
if mibBuilder.loadTexts:hpnicfPBRMibApplyNexthopEntry.setStatus(_A)
class _HpnicfPBRMibApplyNexthopIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_HpnicfPBRMibApplyNexthopIndex_Type.__name__=_K
_HpnicfPBRMibApplyNexthopIndex_Object=MibTableColumn
hpnicfPBRMibApplyNexthopIndex=_HpnicfPBRMibApplyNexthopIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,113,2,5,1,1),_HpnicfPBRMibApplyNexthopIndex_Type())
hpnicfPBRMibApplyNexthopIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:hpnicfPBRMibApplyNexthopIndex.setStatus(_A)
class _HpnicfPBRMibApplyNexthopVpnName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_HpnicfPBRMibApplyNexthopVpnName_Type.__name__=_D
_HpnicfPBRMibApplyNexthopVpnName_Object=MibTableColumn
hpnicfPBRMibApplyNexthopVpnName=_HpnicfPBRMibApplyNexthopVpnName_Object((1,3,6,1,4,1,11,2,14,11,15,2,113,2,5,1,2),_HpnicfPBRMibApplyNexthopVpnName_Type())
hpnicfPBRMibApplyNexthopVpnName.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfPBRMibApplyNexthopVpnName.setStatus(_A)
_HpnicfPBRMibApplyNexthopAddressType_Type=InetAddressType
_HpnicfPBRMibApplyNexthopAddressType_Object=MibTableColumn
hpnicfPBRMibApplyNexthopAddressType=_HpnicfPBRMibApplyNexthopAddressType_Object((1,3,6,1,4,1,11,2,14,11,15,2,113,2,5,1,3),_HpnicfPBRMibApplyNexthopAddressType_Type())
hpnicfPBRMibApplyNexthopAddressType.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfPBRMibApplyNexthopAddressType.setStatus(_A)
_HpnicfPBRMibApplyNexthopAddress_Type=InetAddress
_HpnicfPBRMibApplyNexthopAddress_Object=MibTableColumn
hpnicfPBRMibApplyNexthopAddress=_HpnicfPBRMibApplyNexthopAddress_Object((1,3,6,1,4,1,11,2,14,11,15,2,113,2,5,1,4),_HpnicfPBRMibApplyNexthopAddress_Type())
hpnicfPBRMibApplyNexthopAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfPBRMibApplyNexthopAddress.setStatus(_A)
_HpnicfPBRMibApplyNexthopTrackId_Type=Integer32
_HpnicfPBRMibApplyNexthopTrackId_Object=MibTableColumn
hpnicfPBRMibApplyNexthopTrackId=_HpnicfPBRMibApplyNexthopTrackId_Object((1,3,6,1,4,1,11,2,14,11,15,2,113,2,5,1,5),_HpnicfPBRMibApplyNexthopTrackId_Type())
hpnicfPBRMibApplyNexthopTrackId.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfPBRMibApplyNexthopTrackId.setStatus(_A)
class _HpnicfPBRMibApplyNexthopDirect_Type(TruthValue):defaultValue=2
_HpnicfPBRMibApplyNexthopDirect_Type.__name__=_E
_HpnicfPBRMibApplyNexthopDirect_Object=MibTableColumn
hpnicfPBRMibApplyNexthopDirect=_HpnicfPBRMibApplyNexthopDirect_Object((1,3,6,1,4,1,11,2,14,11,15,2,113,2,5,1,6),_HpnicfPBRMibApplyNexthopDirect_Type())
hpnicfPBRMibApplyNexthopDirect.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfPBRMibApplyNexthopDirect.setStatus(_A)
_HpnicfPBRMibApplyNexthopRowStatus_Type=RowStatus
_HpnicfPBRMibApplyNexthopRowStatus_Object=MibTableColumn
hpnicfPBRMibApplyNexthopRowStatus=_HpnicfPBRMibApplyNexthopRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,113,2,5,1,7),_HpnicfPBRMibApplyNexthopRowStatus_Type())
hpnicfPBRMibApplyNexthopRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfPBRMibApplyNexthopRowStatus.setStatus(_A)
_HpnicfPBRMibApplyDefaultNexthopTable_Object=MibTable
hpnicfPBRMibApplyDefaultNexthopTable=_HpnicfPBRMibApplyDefaultNexthopTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,113,2,6))
if mibBuilder.loadTexts:hpnicfPBRMibApplyDefaultNexthopTable.setStatus(_A)
_HpnicfPBRMibApplyDefaultNexthopEntry_Object=MibTableRow
hpnicfPBRMibApplyDefaultNexthopEntry=_HpnicfPBRMibApplyDefaultNexthopEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,113,2,6,1))
hpnicfPBRMibApplyDefaultNexthopEntry.setIndexNames((0,_B,_F),(0,_B,_G),(0,_B,_H),(0,_B,_Q))
if mibBuilder.loadTexts:hpnicfPBRMibApplyDefaultNexthopEntry.setStatus(_A)
class _HpnicfPBRMibApplyDefaultNexthopIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_HpnicfPBRMibApplyDefaultNexthopIndex_Type.__name__=_K
_HpnicfPBRMibApplyDefaultNexthopIndex_Object=MibTableColumn
hpnicfPBRMibApplyDefaultNexthopIndex=_HpnicfPBRMibApplyDefaultNexthopIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,113,2,6,1,1),_HpnicfPBRMibApplyDefaultNexthopIndex_Type())
hpnicfPBRMibApplyDefaultNexthopIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:hpnicfPBRMibApplyDefaultNexthopIndex.setStatus(_A)
class _HpnicfPBRMibApplyDefaultNexthopVpnName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_HpnicfPBRMibApplyDefaultNexthopVpnName_Type.__name__=_D
_HpnicfPBRMibApplyDefaultNexthopVpnName_Object=MibTableColumn
hpnicfPBRMibApplyDefaultNexthopVpnName=_HpnicfPBRMibApplyDefaultNexthopVpnName_Object((1,3,6,1,4,1,11,2,14,11,15,2,113,2,6,1,2),_HpnicfPBRMibApplyDefaultNexthopVpnName_Type())
hpnicfPBRMibApplyDefaultNexthopVpnName.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfPBRMibApplyDefaultNexthopVpnName.setStatus(_A)
_HpnicfPBRMibApplyDefaultNexthopAddressType_Type=InetAddressType
_HpnicfPBRMibApplyDefaultNexthopAddressType_Object=MibTableColumn
hpnicfPBRMibApplyDefaultNexthopAddressType=_HpnicfPBRMibApplyDefaultNexthopAddressType_Object((1,3,6,1,4,1,11,2,14,11,15,2,113,2,6,1,3),_HpnicfPBRMibApplyDefaultNexthopAddressType_Type())
hpnicfPBRMibApplyDefaultNexthopAddressType.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfPBRMibApplyDefaultNexthopAddressType.setStatus(_A)
_HpnicfPBRMibApplyDefaultNexthopAddress_Type=InetAddress
_HpnicfPBRMibApplyDefaultNexthopAddress_Object=MibTableColumn
hpnicfPBRMibApplyDefaultNexthopAddress=_HpnicfPBRMibApplyDefaultNexthopAddress_Object((1,3,6,1,4,1,11,2,14,11,15,2,113,2,6,1,4),_HpnicfPBRMibApplyDefaultNexthopAddress_Type())
hpnicfPBRMibApplyDefaultNexthopAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfPBRMibApplyDefaultNexthopAddress.setStatus(_A)
_HpnicfPBRMibApplyDefaultNexthopTrackId_Type=Integer32
_HpnicfPBRMibApplyDefaultNexthopTrackId_Object=MibTableColumn
hpnicfPBRMibApplyDefaultNexthopTrackId=_HpnicfPBRMibApplyDefaultNexthopTrackId_Object((1,3,6,1,4,1,11,2,14,11,15,2,113,2,6,1,5),_HpnicfPBRMibApplyDefaultNexthopTrackId_Type())
hpnicfPBRMibApplyDefaultNexthopTrackId.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfPBRMibApplyDefaultNexthopTrackId.setStatus(_A)
class _HpnicfPBRMibApplyDefaultNexthopDirect_Type(TruthValue):defaultValue=2
_HpnicfPBRMibApplyDefaultNexthopDirect_Type.__name__=_E
_HpnicfPBRMibApplyDefaultNexthopDirect_Object=MibTableColumn
hpnicfPBRMibApplyDefaultNexthopDirect=_HpnicfPBRMibApplyDefaultNexthopDirect_Object((1,3,6,1,4,1,11,2,14,11,15,2,113,2,6,1,6),_HpnicfPBRMibApplyDefaultNexthopDirect_Type())
hpnicfPBRMibApplyDefaultNexthopDirect.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfPBRMibApplyDefaultNexthopDirect.setStatus(_A)
_HpnicfPBRMibApplyDefaultNexthopRowStatus_Type=RowStatus
_HpnicfPBRMibApplyDefaultNexthopRowStatus_Object=MibTableColumn
hpnicfPBRMibApplyDefaultNexthopRowStatus=_HpnicfPBRMibApplyDefaultNexthopRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,113,2,6,1,7),_HpnicfPBRMibApplyDefaultNexthopRowStatus_Type())
hpnicfPBRMibApplyDefaultNexthopRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfPBRMibApplyDefaultNexthopRowStatus.setStatus(_A)
hpnicfPBRNexthopFailedTrap=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,113,1,2,2,0,1))
hpnicfPBRNexthopFailedTrap.setObjects(*((_B,_R),(_B,_S)))
if mibBuilder.loadTexts:hpnicfPBRNexthopFailedTrap.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'hpnicfPBR':hpnicfPBR,'hpnicfPBRObjects':hpnicfPBRObjects,'hpnicfPBRGlobal':hpnicfPBRGlobal,'hpnicfPBRNexthopTrapEnabled':hpnicfPBRNexthopTrapEnabled,'hpnicfPBRLocalPolicy':hpnicfPBRLocalPolicy,'hpnicfPBRIPv6NexthopTrapEnabled':hpnicfPBRIPv6NexthopTrapEnabled,'hpnicfPBRMibTrap':hpnicfPBRMibTrap,'hpnicfPBRTrapObjects':hpnicfPBRTrapObjects,_R:hpnicfPBRNexthopAddrType,_S:hpnicfPBRNexthopAddr,'hpnicfPBRTraps':hpnicfPBRTraps,'hpnicfPBRTrapsPrefix':hpnicfPBRTrapsPrefix,'hpnicfPBRNexthopFailedTrap':hpnicfPBRNexthopFailedTrap,'hpnicfPBRTables':hpnicfPBRTables,'hpnicfPBRMibPolicyNodeTable':hpnicfPBRMibPolicyNodeTable,'hpnicfPBRMibPolicyNodeEntry':hpnicfPBRMibPolicyNodeEntry,_F:hpnicfPBRMibPolicyNodeAddrType,_G:hpnicfPBRMibPolicyName,_H:hpnicfPBRMibPolicyNodeId,'hpnicfPBRMibPolicyNodeMode':hpnicfPBRMibPolicyNodeMode,'hpnicfPBRMibPolicyNodeRowStatus':hpnicfPBRMibPolicyNodeRowStatus,'hpnicfPBRMibIfPolicyTable':hpnicfPBRMibIfPolicyTable,'hpnicfPBRMibIfPolicyEntry':hpnicfPBRMibIfPolicyEntry,_O:hpnicfPBRMibPolicyAddressType,'hpnicfPBRMibAppliedPolicyName':hpnicfPBRMibAppliedPolicyName,'hpnicfPBRMibIfPolicyRowStatus':hpnicfPBRMibIfPolicyRowStatus,'hpnicfPBRMibMatchAclTable':hpnicfPBRMibMatchAclTable,'hpnicfPBRMibMatchAclEntry':hpnicfPBRMibMatchAclEntry,'hpnicfPBRMibAclGroupId':hpnicfPBRMibAclGroupId,'hpnicfPBRMibApplyPrecedenceTable':hpnicfPBRMibApplyPrecedenceTable,'hpnicfPBRMibApplyPrecedenceEntry':hpnicfPBRMibApplyPrecedenceEntry,'hpnicfPBRMibApplyPrecedenceValue':hpnicfPBRMibApplyPrecedenceValue,'hpnicfPBRMibApplyNexthopTable':hpnicfPBRMibApplyNexthopTable,'hpnicfPBRMibApplyNexthopEntry':hpnicfPBRMibApplyNexthopEntry,_P:hpnicfPBRMibApplyNexthopIndex,'hpnicfPBRMibApplyNexthopVpnName':hpnicfPBRMibApplyNexthopVpnName,'hpnicfPBRMibApplyNexthopAddressType':hpnicfPBRMibApplyNexthopAddressType,'hpnicfPBRMibApplyNexthopAddress':hpnicfPBRMibApplyNexthopAddress,'hpnicfPBRMibApplyNexthopTrackId':hpnicfPBRMibApplyNexthopTrackId,'hpnicfPBRMibApplyNexthopDirect':hpnicfPBRMibApplyNexthopDirect,'hpnicfPBRMibApplyNexthopRowStatus':hpnicfPBRMibApplyNexthopRowStatus,'hpnicfPBRMibApplyDefaultNexthopTable':hpnicfPBRMibApplyDefaultNexthopTable,'hpnicfPBRMibApplyDefaultNexthopEntry':hpnicfPBRMibApplyDefaultNexthopEntry,_Q:hpnicfPBRMibApplyDefaultNexthopIndex,'hpnicfPBRMibApplyDefaultNexthopVpnName':hpnicfPBRMibApplyDefaultNexthopVpnName,'hpnicfPBRMibApplyDefaultNexthopAddressType':hpnicfPBRMibApplyDefaultNexthopAddressType,'hpnicfPBRMibApplyDefaultNexthopAddress':hpnicfPBRMibApplyDefaultNexthopAddress,'hpnicfPBRMibApplyDefaultNexthopTrackId':hpnicfPBRMibApplyDefaultNexthopTrackId,'hpnicfPBRMibApplyDefaultNexthopDirect':hpnicfPBRMibApplyDefaultNexthopDirect,'hpnicfPBRMibApplyDefaultNexthopRowStatus':hpnicfPBRMibApplyDefaultNexthopRowStatus})