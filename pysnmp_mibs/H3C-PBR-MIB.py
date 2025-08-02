_S='h3cPBRNexthopAddr'
_R='h3cPBRNexthopAddrType'
_Q='h3cPBRMibApplyDefaultNexthopIndex'
_P='h3cPBRMibApplyNexthopIndex'
_O='h3cPBRMibPolicyAddressType'
_N='accessible-for-notify'
_M='ifIndex'
_L='IF-MIB'
_K='Integer32'
_J='read-write'
_I='not-accessible'
_H='h3cPBRMibPolicyNodeId'
_G='h3cPBRMibPolicyName'
_F='h3cPBRMibPolicyNodeAddrType'
_E='TruthValue'
_D='DisplayString'
_C='read-create'
_B='H3C-PBR-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
h3cCommon,=mibBuilder.importSymbols('HUAWEI-3COM-OID-MIB','h3cCommon')
ifIndex,=mibBuilder.importSymbols(_L,_M)
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_K,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_D,'PhysAddress','RowStatus','TextualConvention',_E)
h3cPBR=ModuleIdentity((1,3,6,1,4,1,2011,10,2,113))
if mibBuilder.loadTexts:h3cPBR.setRevisions(('2010-12-10 15:58',))
_H3cPBRObjects_ObjectIdentity=ObjectIdentity
h3cPBRObjects=_H3cPBRObjects_ObjectIdentity((1,3,6,1,4,1,2011,10,2,113,1))
_H3cPBRGlobal_ObjectIdentity=ObjectIdentity
h3cPBRGlobal=_H3cPBRGlobal_ObjectIdentity((1,3,6,1,4,1,2011,10,2,113,1,1))
class _H3cPBRNexthopTrapEnabled_Type(TruthValue):defaultValue=1
_H3cPBRNexthopTrapEnabled_Type.__name__=_E
_H3cPBRNexthopTrapEnabled_Object=MibScalar
h3cPBRNexthopTrapEnabled=_H3cPBRNexthopTrapEnabled_Object((1,3,6,1,4,1,2011,10,2,113,1,1,1),_H3cPBRNexthopTrapEnabled_Type())
h3cPBRNexthopTrapEnabled.setMaxAccess(_J)
if mibBuilder.loadTexts:h3cPBRNexthopTrapEnabled.setStatus(_A)
class _H3cPBRLocalPolicy_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,19))
_H3cPBRLocalPolicy_Type.__name__=_D
_H3cPBRLocalPolicy_Object=MibScalar
h3cPBRLocalPolicy=_H3cPBRLocalPolicy_Object((1,3,6,1,4,1,2011,10,2,113,1,1,2),_H3cPBRLocalPolicy_Type())
h3cPBRLocalPolicy.setMaxAccess(_J)
if mibBuilder.loadTexts:h3cPBRLocalPolicy.setStatus(_A)
class _H3cPBRIPv6NexthopTrapEnabled_Type(TruthValue):defaultValue=1
_H3cPBRIPv6NexthopTrapEnabled_Type.__name__=_E
_H3cPBRIPv6NexthopTrapEnabled_Object=MibScalar
h3cPBRIPv6NexthopTrapEnabled=_H3cPBRIPv6NexthopTrapEnabled_Object((1,3,6,1,4,1,2011,10,2,113,1,1,3),_H3cPBRIPv6NexthopTrapEnabled_Type())
h3cPBRIPv6NexthopTrapEnabled.setMaxAccess(_J)
if mibBuilder.loadTexts:h3cPBRIPv6NexthopTrapEnabled.setStatus(_A)
_H3cPBRMibTrap_ObjectIdentity=ObjectIdentity
h3cPBRMibTrap=_H3cPBRMibTrap_ObjectIdentity((1,3,6,1,4,1,2011,10,2,113,1,2))
_H3cPBRTrapObjects_ObjectIdentity=ObjectIdentity
h3cPBRTrapObjects=_H3cPBRTrapObjects_ObjectIdentity((1,3,6,1,4,1,2011,10,2,113,1,2,1))
_H3cPBRNexthopAddrType_Type=InetAddressType
_H3cPBRNexthopAddrType_Object=MibScalar
h3cPBRNexthopAddrType=_H3cPBRNexthopAddrType_Object((1,3,6,1,4,1,2011,10,2,113,1,2,1,1),_H3cPBRNexthopAddrType_Type())
h3cPBRNexthopAddrType.setMaxAccess(_N)
if mibBuilder.loadTexts:h3cPBRNexthopAddrType.setStatus(_A)
_H3cPBRNexthopAddr_Type=InetAddress
_H3cPBRNexthopAddr_Object=MibScalar
h3cPBRNexthopAddr=_H3cPBRNexthopAddr_Object((1,3,6,1,4,1,2011,10,2,113,1,2,1,2),_H3cPBRNexthopAddr_Type())
h3cPBRNexthopAddr.setMaxAccess(_N)
if mibBuilder.loadTexts:h3cPBRNexthopAddr.setStatus(_A)
_H3cPBRTraps_ObjectIdentity=ObjectIdentity
h3cPBRTraps=_H3cPBRTraps_ObjectIdentity((1,3,6,1,4,1,2011,10,2,113,1,2,2))
_H3cPBRTrapsPrefix_ObjectIdentity=ObjectIdentity
h3cPBRTrapsPrefix=_H3cPBRTrapsPrefix_ObjectIdentity((1,3,6,1,4,1,2011,10,2,113,1,2,2,0))
_H3cPBRTables_ObjectIdentity=ObjectIdentity
h3cPBRTables=_H3cPBRTables_ObjectIdentity((1,3,6,1,4,1,2011,10,2,113,2))
_H3cPBRMibPolicyNodeTable_Object=MibTable
h3cPBRMibPolicyNodeTable=_H3cPBRMibPolicyNodeTable_Object((1,3,6,1,4,1,2011,10,2,113,2,1))
if mibBuilder.loadTexts:h3cPBRMibPolicyNodeTable.setStatus(_A)
_H3cPBRMibPolicyNodeEntry_Object=MibTableRow
h3cPBRMibPolicyNodeEntry=_H3cPBRMibPolicyNodeEntry_Object((1,3,6,1,4,1,2011,10,2,113,2,1,1))
h3cPBRMibPolicyNodeEntry.setIndexNames((0,_B,_F),(0,_B,_G),(0,_B,_H))
if mibBuilder.loadTexts:h3cPBRMibPolicyNodeEntry.setStatus(_A)
_H3cPBRMibPolicyNodeAddrType_Type=InetAddressType
_H3cPBRMibPolicyNodeAddrType_Object=MibTableColumn
h3cPBRMibPolicyNodeAddrType=_H3cPBRMibPolicyNodeAddrType_Object((1,3,6,1,4,1,2011,10,2,113,2,1,1,1),_H3cPBRMibPolicyNodeAddrType_Type())
h3cPBRMibPolicyNodeAddrType.setMaxAccess(_I)
if mibBuilder.loadTexts:h3cPBRMibPolicyNodeAddrType.setStatus(_A)
class _H3cPBRMibPolicyName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,19))
_H3cPBRMibPolicyName_Type.__name__=_D
_H3cPBRMibPolicyName_Object=MibTableColumn
h3cPBRMibPolicyName=_H3cPBRMibPolicyName_Object((1,3,6,1,4,1,2011,10,2,113,2,1,1,2),_H3cPBRMibPolicyName_Type())
h3cPBRMibPolicyName.setMaxAccess(_I)
if mibBuilder.loadTexts:h3cPBRMibPolicyName.setStatus(_A)
class _H3cPBRMibPolicyNodeId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_H3cPBRMibPolicyNodeId_Type.__name__=_K
_H3cPBRMibPolicyNodeId_Object=MibTableColumn
h3cPBRMibPolicyNodeId=_H3cPBRMibPolicyNodeId_Object((1,3,6,1,4,1,2011,10,2,113,2,1,1,3),_H3cPBRMibPolicyNodeId_Type())
h3cPBRMibPolicyNodeId.setMaxAccess(_I)
if mibBuilder.loadTexts:h3cPBRMibPolicyNodeId.setStatus(_A)
class _H3cPBRMibPolicyNodeMode_Type(TruthValue):defaultValue=1
_H3cPBRMibPolicyNodeMode_Type.__name__=_E
_H3cPBRMibPolicyNodeMode_Object=MibTableColumn
h3cPBRMibPolicyNodeMode=_H3cPBRMibPolicyNodeMode_Object((1,3,6,1,4,1,2011,10,2,113,2,1,1,4),_H3cPBRMibPolicyNodeMode_Type())
h3cPBRMibPolicyNodeMode.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cPBRMibPolicyNodeMode.setStatus(_A)
_H3cPBRMibPolicyNodeRowStatus_Type=RowStatus
_H3cPBRMibPolicyNodeRowStatus_Object=MibTableColumn
h3cPBRMibPolicyNodeRowStatus=_H3cPBRMibPolicyNodeRowStatus_Object((1,3,6,1,4,1,2011,10,2,113,2,1,1,5),_H3cPBRMibPolicyNodeRowStatus_Type())
h3cPBRMibPolicyNodeRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cPBRMibPolicyNodeRowStatus.setStatus(_A)
_H3cPBRMibIfPolicyTable_Object=MibTable
h3cPBRMibIfPolicyTable=_H3cPBRMibIfPolicyTable_Object((1,3,6,1,4,1,2011,10,2,113,2,2))
if mibBuilder.loadTexts:h3cPBRMibIfPolicyTable.setStatus(_A)
_H3cPBRMibIfPolicyEntry_Object=MibTableRow
h3cPBRMibIfPolicyEntry=_H3cPBRMibIfPolicyEntry_Object((1,3,6,1,4,1,2011,10,2,113,2,2,1))
h3cPBRMibIfPolicyEntry.setIndexNames((0,_B,_O),(0,_L,_M))
if mibBuilder.loadTexts:h3cPBRMibIfPolicyEntry.setStatus(_A)
_H3cPBRMibPolicyAddressType_Type=InetAddressType
_H3cPBRMibPolicyAddressType_Object=MibTableColumn
h3cPBRMibPolicyAddressType=_H3cPBRMibPolicyAddressType_Object((1,3,6,1,4,1,2011,10,2,113,2,2,1,1),_H3cPBRMibPolicyAddressType_Type())
h3cPBRMibPolicyAddressType.setMaxAccess(_I)
if mibBuilder.loadTexts:h3cPBRMibPolicyAddressType.setStatus(_A)
class _H3cPBRMibAppliedPolicyName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,19))
_H3cPBRMibAppliedPolicyName_Type.__name__=_D
_H3cPBRMibAppliedPolicyName_Object=MibTableColumn
h3cPBRMibAppliedPolicyName=_H3cPBRMibAppliedPolicyName_Object((1,3,6,1,4,1,2011,10,2,113,2,2,1,2),_H3cPBRMibAppliedPolicyName_Type())
h3cPBRMibAppliedPolicyName.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cPBRMibAppliedPolicyName.setStatus(_A)
_H3cPBRMibIfPolicyRowStatus_Type=RowStatus
_H3cPBRMibIfPolicyRowStatus_Object=MibTableColumn
h3cPBRMibIfPolicyRowStatus=_H3cPBRMibIfPolicyRowStatus_Object((1,3,6,1,4,1,2011,10,2,113,2,2,1,3),_H3cPBRMibIfPolicyRowStatus_Type())
h3cPBRMibIfPolicyRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cPBRMibIfPolicyRowStatus.setStatus(_A)
_H3cPBRMibMatchAclTable_Object=MibTable
h3cPBRMibMatchAclTable=_H3cPBRMibMatchAclTable_Object((1,3,6,1,4,1,2011,10,2,113,2,3))
if mibBuilder.loadTexts:h3cPBRMibMatchAclTable.setStatus(_A)
_H3cPBRMibMatchAclEntry_Object=MibTableRow
h3cPBRMibMatchAclEntry=_H3cPBRMibMatchAclEntry_Object((1,3,6,1,4,1,2011,10,2,113,2,3,1))
h3cPBRMibMatchAclEntry.setIndexNames((0,_B,_F),(0,_B,_G),(0,_B,_H))
if mibBuilder.loadTexts:h3cPBRMibMatchAclEntry.setStatus(_A)
_H3cPBRMibAclGroupId_Type=Integer32
_H3cPBRMibAclGroupId_Object=MibTableColumn
h3cPBRMibAclGroupId=_H3cPBRMibAclGroupId_Object((1,3,6,1,4,1,2011,10,2,113,2,3,1,1),_H3cPBRMibAclGroupId_Type())
h3cPBRMibAclGroupId.setMaxAccess(_J)
if mibBuilder.loadTexts:h3cPBRMibAclGroupId.setStatus(_A)
_H3cPBRMibApplyPrecedenceTable_Object=MibTable
h3cPBRMibApplyPrecedenceTable=_H3cPBRMibApplyPrecedenceTable_Object((1,3,6,1,4,1,2011,10,2,113,2,4))
if mibBuilder.loadTexts:h3cPBRMibApplyPrecedenceTable.setStatus(_A)
_H3cPBRMibApplyPrecedenceEntry_Object=MibTableRow
h3cPBRMibApplyPrecedenceEntry=_H3cPBRMibApplyPrecedenceEntry_Object((1,3,6,1,4,1,2011,10,2,113,2,4,1))
h3cPBRMibApplyPrecedenceEntry.setIndexNames((0,_B,_F),(0,_B,_G),(0,_B,_H))
if mibBuilder.loadTexts:h3cPBRMibApplyPrecedenceEntry.setStatus(_A)
_H3cPBRMibApplyPrecedenceValue_Type=Integer32
_H3cPBRMibApplyPrecedenceValue_Object=MibTableColumn
h3cPBRMibApplyPrecedenceValue=_H3cPBRMibApplyPrecedenceValue_Object((1,3,6,1,4,1,2011,10,2,113,2,4,1,1),_H3cPBRMibApplyPrecedenceValue_Type())
h3cPBRMibApplyPrecedenceValue.setMaxAccess(_J)
if mibBuilder.loadTexts:h3cPBRMibApplyPrecedenceValue.setStatus(_A)
_H3cPBRMibApplyNexthopTable_Object=MibTable
h3cPBRMibApplyNexthopTable=_H3cPBRMibApplyNexthopTable_Object((1,3,6,1,4,1,2011,10,2,113,2,5))
if mibBuilder.loadTexts:h3cPBRMibApplyNexthopTable.setStatus(_A)
_H3cPBRMibApplyNexthopEntry_Object=MibTableRow
h3cPBRMibApplyNexthopEntry=_H3cPBRMibApplyNexthopEntry_Object((1,3,6,1,4,1,2011,10,2,113,2,5,1))
h3cPBRMibApplyNexthopEntry.setIndexNames((0,_B,_F),(0,_B,_G),(0,_B,_H),(0,_B,_P))
if mibBuilder.loadTexts:h3cPBRMibApplyNexthopEntry.setStatus(_A)
class _H3cPBRMibApplyNexthopIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_H3cPBRMibApplyNexthopIndex_Type.__name__=_K
_H3cPBRMibApplyNexthopIndex_Object=MibTableColumn
h3cPBRMibApplyNexthopIndex=_H3cPBRMibApplyNexthopIndex_Object((1,3,6,1,4,1,2011,10,2,113,2,5,1,1),_H3cPBRMibApplyNexthopIndex_Type())
h3cPBRMibApplyNexthopIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:h3cPBRMibApplyNexthopIndex.setStatus(_A)
class _H3cPBRMibApplyNexthopVpnName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_H3cPBRMibApplyNexthopVpnName_Type.__name__=_D
_H3cPBRMibApplyNexthopVpnName_Object=MibTableColumn
h3cPBRMibApplyNexthopVpnName=_H3cPBRMibApplyNexthopVpnName_Object((1,3,6,1,4,1,2011,10,2,113,2,5,1,2),_H3cPBRMibApplyNexthopVpnName_Type())
h3cPBRMibApplyNexthopVpnName.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cPBRMibApplyNexthopVpnName.setStatus(_A)
_H3cPBRMibApplyNexthopAddressType_Type=InetAddressType
_H3cPBRMibApplyNexthopAddressType_Object=MibTableColumn
h3cPBRMibApplyNexthopAddressType=_H3cPBRMibApplyNexthopAddressType_Object((1,3,6,1,4,1,2011,10,2,113,2,5,1,3),_H3cPBRMibApplyNexthopAddressType_Type())
h3cPBRMibApplyNexthopAddressType.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cPBRMibApplyNexthopAddressType.setStatus(_A)
_H3cPBRMibApplyNexthopAddress_Type=InetAddress
_H3cPBRMibApplyNexthopAddress_Object=MibTableColumn
h3cPBRMibApplyNexthopAddress=_H3cPBRMibApplyNexthopAddress_Object((1,3,6,1,4,1,2011,10,2,113,2,5,1,4),_H3cPBRMibApplyNexthopAddress_Type())
h3cPBRMibApplyNexthopAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cPBRMibApplyNexthopAddress.setStatus(_A)
_H3cPBRMibApplyNexthopTrackId_Type=Integer32
_H3cPBRMibApplyNexthopTrackId_Object=MibTableColumn
h3cPBRMibApplyNexthopTrackId=_H3cPBRMibApplyNexthopTrackId_Object((1,3,6,1,4,1,2011,10,2,113,2,5,1,5),_H3cPBRMibApplyNexthopTrackId_Type())
h3cPBRMibApplyNexthopTrackId.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cPBRMibApplyNexthopTrackId.setStatus(_A)
class _H3cPBRMibApplyNexthopDirect_Type(TruthValue):defaultValue=2
_H3cPBRMibApplyNexthopDirect_Type.__name__=_E
_H3cPBRMibApplyNexthopDirect_Object=MibTableColumn
h3cPBRMibApplyNexthopDirect=_H3cPBRMibApplyNexthopDirect_Object((1,3,6,1,4,1,2011,10,2,113,2,5,1,6),_H3cPBRMibApplyNexthopDirect_Type())
h3cPBRMibApplyNexthopDirect.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cPBRMibApplyNexthopDirect.setStatus(_A)
_H3cPBRMibApplyNexthopRowStatus_Type=RowStatus
_H3cPBRMibApplyNexthopRowStatus_Object=MibTableColumn
h3cPBRMibApplyNexthopRowStatus=_H3cPBRMibApplyNexthopRowStatus_Object((1,3,6,1,4,1,2011,10,2,113,2,5,1,7),_H3cPBRMibApplyNexthopRowStatus_Type())
h3cPBRMibApplyNexthopRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cPBRMibApplyNexthopRowStatus.setStatus(_A)
_H3cPBRMibApplyDefaultNexthopTable_Object=MibTable
h3cPBRMibApplyDefaultNexthopTable=_H3cPBRMibApplyDefaultNexthopTable_Object((1,3,6,1,4,1,2011,10,2,113,2,6))
if mibBuilder.loadTexts:h3cPBRMibApplyDefaultNexthopTable.setStatus(_A)
_H3cPBRMibApplyDefaultNexthopEntry_Object=MibTableRow
h3cPBRMibApplyDefaultNexthopEntry=_H3cPBRMibApplyDefaultNexthopEntry_Object((1,3,6,1,4,1,2011,10,2,113,2,6,1))
h3cPBRMibApplyDefaultNexthopEntry.setIndexNames((0,_B,_F),(0,_B,_G),(0,_B,_H),(0,_B,_Q))
if mibBuilder.loadTexts:h3cPBRMibApplyDefaultNexthopEntry.setStatus(_A)
class _H3cPBRMibApplyDefaultNexthopIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_H3cPBRMibApplyDefaultNexthopIndex_Type.__name__=_K
_H3cPBRMibApplyDefaultNexthopIndex_Object=MibTableColumn
h3cPBRMibApplyDefaultNexthopIndex=_H3cPBRMibApplyDefaultNexthopIndex_Object((1,3,6,1,4,1,2011,10,2,113,2,6,1,1),_H3cPBRMibApplyDefaultNexthopIndex_Type())
h3cPBRMibApplyDefaultNexthopIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:h3cPBRMibApplyDefaultNexthopIndex.setStatus(_A)
class _H3cPBRMibApplyDefaultNexthopVpnName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_H3cPBRMibApplyDefaultNexthopVpnName_Type.__name__=_D
_H3cPBRMibApplyDefaultNexthopVpnName_Object=MibTableColumn
h3cPBRMibApplyDefaultNexthopVpnName=_H3cPBRMibApplyDefaultNexthopVpnName_Object((1,3,6,1,4,1,2011,10,2,113,2,6,1,2),_H3cPBRMibApplyDefaultNexthopVpnName_Type())
h3cPBRMibApplyDefaultNexthopVpnName.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cPBRMibApplyDefaultNexthopVpnName.setStatus(_A)
_H3cPBRMibApplyDefaultNexthopAddressType_Type=InetAddressType
_H3cPBRMibApplyDefaultNexthopAddressType_Object=MibTableColumn
h3cPBRMibApplyDefaultNexthopAddressType=_H3cPBRMibApplyDefaultNexthopAddressType_Object((1,3,6,1,4,1,2011,10,2,113,2,6,1,3),_H3cPBRMibApplyDefaultNexthopAddressType_Type())
h3cPBRMibApplyDefaultNexthopAddressType.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cPBRMibApplyDefaultNexthopAddressType.setStatus(_A)
_H3cPBRMibApplyDefaultNexthopAddress_Type=InetAddress
_H3cPBRMibApplyDefaultNexthopAddress_Object=MibTableColumn
h3cPBRMibApplyDefaultNexthopAddress=_H3cPBRMibApplyDefaultNexthopAddress_Object((1,3,6,1,4,1,2011,10,2,113,2,6,1,4),_H3cPBRMibApplyDefaultNexthopAddress_Type())
h3cPBRMibApplyDefaultNexthopAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cPBRMibApplyDefaultNexthopAddress.setStatus(_A)
_H3cPBRMibApplyDefaultNexthopTrackId_Type=Integer32
_H3cPBRMibApplyDefaultNexthopTrackId_Object=MibTableColumn
h3cPBRMibApplyDefaultNexthopTrackId=_H3cPBRMibApplyDefaultNexthopTrackId_Object((1,3,6,1,4,1,2011,10,2,113,2,6,1,5),_H3cPBRMibApplyDefaultNexthopTrackId_Type())
h3cPBRMibApplyDefaultNexthopTrackId.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cPBRMibApplyDefaultNexthopTrackId.setStatus(_A)
class _H3cPBRMibApplyDefaultNexthopDirect_Type(TruthValue):defaultValue=2
_H3cPBRMibApplyDefaultNexthopDirect_Type.__name__=_E
_H3cPBRMibApplyDefaultNexthopDirect_Object=MibTableColumn
h3cPBRMibApplyDefaultNexthopDirect=_H3cPBRMibApplyDefaultNexthopDirect_Object((1,3,6,1,4,1,2011,10,2,113,2,6,1,6),_H3cPBRMibApplyDefaultNexthopDirect_Type())
h3cPBRMibApplyDefaultNexthopDirect.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cPBRMibApplyDefaultNexthopDirect.setStatus(_A)
_H3cPBRMibApplyDefaultNexthopRowStatus_Type=RowStatus
_H3cPBRMibApplyDefaultNexthopRowStatus_Object=MibTableColumn
h3cPBRMibApplyDefaultNexthopRowStatus=_H3cPBRMibApplyDefaultNexthopRowStatus_Object((1,3,6,1,4,1,2011,10,2,113,2,6,1,7),_H3cPBRMibApplyDefaultNexthopRowStatus_Type())
h3cPBRMibApplyDefaultNexthopRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cPBRMibApplyDefaultNexthopRowStatus.setStatus(_A)
h3cPBRNexthopFailedTrap=NotificationType((1,3,6,1,4,1,2011,10,2,113,1,2,2,0,1))
h3cPBRNexthopFailedTrap.setObjects(*((_B,_R),(_B,_S)))
if mibBuilder.loadTexts:h3cPBRNexthopFailedTrap.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'h3cPBR':h3cPBR,'h3cPBRObjects':h3cPBRObjects,'h3cPBRGlobal':h3cPBRGlobal,'h3cPBRNexthopTrapEnabled':h3cPBRNexthopTrapEnabled,'h3cPBRLocalPolicy':h3cPBRLocalPolicy,'h3cPBRIPv6NexthopTrapEnabled':h3cPBRIPv6NexthopTrapEnabled,'h3cPBRMibTrap':h3cPBRMibTrap,'h3cPBRTrapObjects':h3cPBRTrapObjects,_R:h3cPBRNexthopAddrType,_S:h3cPBRNexthopAddr,'h3cPBRTraps':h3cPBRTraps,'h3cPBRTrapsPrefix':h3cPBRTrapsPrefix,'h3cPBRNexthopFailedTrap':h3cPBRNexthopFailedTrap,'h3cPBRTables':h3cPBRTables,'h3cPBRMibPolicyNodeTable':h3cPBRMibPolicyNodeTable,'h3cPBRMibPolicyNodeEntry':h3cPBRMibPolicyNodeEntry,_F:h3cPBRMibPolicyNodeAddrType,_G:h3cPBRMibPolicyName,_H:h3cPBRMibPolicyNodeId,'h3cPBRMibPolicyNodeMode':h3cPBRMibPolicyNodeMode,'h3cPBRMibPolicyNodeRowStatus':h3cPBRMibPolicyNodeRowStatus,'h3cPBRMibIfPolicyTable':h3cPBRMibIfPolicyTable,'h3cPBRMibIfPolicyEntry':h3cPBRMibIfPolicyEntry,_O:h3cPBRMibPolicyAddressType,'h3cPBRMibAppliedPolicyName':h3cPBRMibAppliedPolicyName,'h3cPBRMibIfPolicyRowStatus':h3cPBRMibIfPolicyRowStatus,'h3cPBRMibMatchAclTable':h3cPBRMibMatchAclTable,'h3cPBRMibMatchAclEntry':h3cPBRMibMatchAclEntry,'h3cPBRMibAclGroupId':h3cPBRMibAclGroupId,'h3cPBRMibApplyPrecedenceTable':h3cPBRMibApplyPrecedenceTable,'h3cPBRMibApplyPrecedenceEntry':h3cPBRMibApplyPrecedenceEntry,'h3cPBRMibApplyPrecedenceValue':h3cPBRMibApplyPrecedenceValue,'h3cPBRMibApplyNexthopTable':h3cPBRMibApplyNexthopTable,'h3cPBRMibApplyNexthopEntry':h3cPBRMibApplyNexthopEntry,_P:h3cPBRMibApplyNexthopIndex,'h3cPBRMibApplyNexthopVpnName':h3cPBRMibApplyNexthopVpnName,'h3cPBRMibApplyNexthopAddressType':h3cPBRMibApplyNexthopAddressType,'h3cPBRMibApplyNexthopAddress':h3cPBRMibApplyNexthopAddress,'h3cPBRMibApplyNexthopTrackId':h3cPBRMibApplyNexthopTrackId,'h3cPBRMibApplyNexthopDirect':h3cPBRMibApplyNexthopDirect,'h3cPBRMibApplyNexthopRowStatus':h3cPBRMibApplyNexthopRowStatus,'h3cPBRMibApplyDefaultNexthopTable':h3cPBRMibApplyDefaultNexthopTable,'h3cPBRMibApplyDefaultNexthopEntry':h3cPBRMibApplyDefaultNexthopEntry,_Q:h3cPBRMibApplyDefaultNexthopIndex,'h3cPBRMibApplyDefaultNexthopVpnName':h3cPBRMibApplyDefaultNexthopVpnName,'h3cPBRMibApplyDefaultNexthopAddressType':h3cPBRMibApplyDefaultNexthopAddressType,'h3cPBRMibApplyDefaultNexthopAddress':h3cPBRMibApplyDefaultNexthopAddress,'h3cPBRMibApplyDefaultNexthopTrackId':h3cPBRMibApplyDefaultNexthopTrackId,'h3cPBRMibApplyDefaultNexthopDirect':h3cPBRMibApplyDefaultNexthopDirect,'h3cPBRMibApplyDefaultNexthopRowStatus':h3cPBRMibApplyDefaultNexthopRowStatus})