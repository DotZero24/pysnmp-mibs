_O='zyIpv6sgBindingIpv6PrefixLength'
_N='zyIpv6sgBindingIpv6Address'
_M='zyIpv6sgBindingIpv6AddressType'
_L='zyIpv6sgPolicyName'
_K='zyIpv6sgStaticBindingIpv6PrefixLength'
_J='zyIpv6sgStaticBindingIpv6Address'
_I='zyIpv6sgStaticBindingIpv6AddressType'
_H='Integer32'
_G='dot1dBasePort'
_F='BRIDGE-MIB'
_E='not-accessible'
_D='read-only'
_C='ZYXEL-IPv6SG-MIB'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dot1dBasePort,=mibBuilder.importSymbols(_F,_G)
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
EnabledStatus,=mibBuilder.importSymbols('P-BRIDGE-MIB','EnabledStatus')
PortList,=mibBuilder.importSymbols('Q-BRIDGE-MIB','PortList')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_H,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention')
esMgmt,=mibBuilder.importSymbols('ZYXEL-ES-SMI','esMgmt')
zyxelIpv6sg=ModuleIdentity((1,3,6,1,4,1,890,1,15,3,108))
_ZyxelIpv6sgSetup_ObjectIdentity=ObjectIdentity
zyxelIpv6sgSetup=_ZyxelIpv6sgSetup_ObjectIdentity((1,3,6,1,4,1,890,1,15,3,108,1))
_ZyxelIpv6sgStaticBindingMaxNumberOfRules_Type=Integer32
_ZyxelIpv6sgStaticBindingMaxNumberOfRules_Object=MibScalar
zyxelIpv6sgStaticBindingMaxNumberOfRules=_ZyxelIpv6sgStaticBindingMaxNumberOfRules_Object((1,3,6,1,4,1,890,1,15,3,108,1,1),_ZyxelIpv6sgStaticBindingMaxNumberOfRules_Type())
zyxelIpv6sgStaticBindingMaxNumberOfRules.setMaxAccess(_D)
if mibBuilder.loadTexts:zyxelIpv6sgStaticBindingMaxNumberOfRules.setStatus(_A)
_ZyxelIpv6sgStaticBindingTable_Object=MibTable
zyxelIpv6sgStaticBindingTable=_ZyxelIpv6sgStaticBindingTable_Object((1,3,6,1,4,1,890,1,15,3,108,1,2))
if mibBuilder.loadTexts:zyxelIpv6sgStaticBindingTable.setStatus(_A)
_ZyxelIpv6sgStaticBindingEntry_Object=MibTableRow
zyxelIpv6sgStaticBindingEntry=_ZyxelIpv6sgStaticBindingEntry_Object((1,3,6,1,4,1,890,1,15,3,108,1,2,1))
zyxelIpv6sgStaticBindingEntry.setIndexNames((0,_C,_I),(0,_C,_J),(0,_C,_K))
if mibBuilder.loadTexts:zyxelIpv6sgStaticBindingEntry.setStatus(_A)
_ZyIpv6sgStaticBindingIpv6AddressType_Type=InetAddressType
_ZyIpv6sgStaticBindingIpv6AddressType_Object=MibTableColumn
zyIpv6sgStaticBindingIpv6AddressType=_ZyIpv6sgStaticBindingIpv6AddressType_Object((1,3,6,1,4,1,890,1,15,3,108,1,2,1,1),_ZyIpv6sgStaticBindingIpv6AddressType_Type())
zyIpv6sgStaticBindingIpv6AddressType.setMaxAccess(_E)
if mibBuilder.loadTexts:zyIpv6sgStaticBindingIpv6AddressType.setStatus(_A)
_ZyIpv6sgStaticBindingIpv6Address_Type=InetAddress
_ZyIpv6sgStaticBindingIpv6Address_Object=MibTableColumn
zyIpv6sgStaticBindingIpv6Address=_ZyIpv6sgStaticBindingIpv6Address_Object((1,3,6,1,4,1,890,1,15,3,108,1,2,1,2),_ZyIpv6sgStaticBindingIpv6Address_Type())
zyIpv6sgStaticBindingIpv6Address.setMaxAccess(_E)
if mibBuilder.loadTexts:zyIpv6sgStaticBindingIpv6Address.setStatus(_A)
_ZyIpv6sgStaticBindingIpv6PrefixLength_Type=Integer32
_ZyIpv6sgStaticBindingIpv6PrefixLength_Object=MibTableColumn
zyIpv6sgStaticBindingIpv6PrefixLength=_ZyIpv6sgStaticBindingIpv6PrefixLength_Object((1,3,6,1,4,1,890,1,15,3,108,1,2,1,3),_ZyIpv6sgStaticBindingIpv6PrefixLength_Type())
zyIpv6sgStaticBindingIpv6PrefixLength.setMaxAccess(_E)
if mibBuilder.loadTexts:zyIpv6sgStaticBindingIpv6PrefixLength.setStatus(_A)
_ZyIpv6sgStaticBindingMacAddress_Type=MacAddress
_ZyIpv6sgStaticBindingMacAddress_Object=MibTableColumn
zyIpv6sgStaticBindingMacAddress=_ZyIpv6sgStaticBindingMacAddress_Object((1,3,6,1,4,1,890,1,15,3,108,1,2,1,4),_ZyIpv6sgStaticBindingMacAddress_Type())
zyIpv6sgStaticBindingMacAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:zyIpv6sgStaticBindingMacAddress.setStatus(_A)
_ZyIpv6sgStaticBindingVid_Type=Integer32
_ZyIpv6sgStaticBindingVid_Object=MibTableColumn
zyIpv6sgStaticBindingVid=_ZyIpv6sgStaticBindingVid_Object((1,3,6,1,4,1,890,1,15,3,108,1,2,1,5),_ZyIpv6sgStaticBindingVid_Type())
zyIpv6sgStaticBindingVid.setMaxAccess(_B)
if mibBuilder.loadTexts:zyIpv6sgStaticBindingVid.setStatus(_A)
_ZyIpv6sgStaticBindingPort_Type=Integer32
_ZyIpv6sgStaticBindingPort_Object=MibTableColumn
zyIpv6sgStaticBindingPort=_ZyIpv6sgStaticBindingPort_Object((1,3,6,1,4,1,890,1,15,3,108,1,2,1,6),_ZyIpv6sgStaticBindingPort_Type())
zyIpv6sgStaticBindingPort.setMaxAccess(_B)
if mibBuilder.loadTexts:zyIpv6sgStaticBindingPort.setStatus(_A)
_ZyIpv6sgStaticBindingRowStatus_Type=RowStatus
_ZyIpv6sgStaticBindingRowStatus_Object=MibTableColumn
zyIpv6sgStaticBindingRowStatus=_ZyIpv6sgStaticBindingRowStatus_Object((1,3,6,1,4,1,890,1,15,3,108,1,2,1,7),_ZyIpv6sgStaticBindingRowStatus_Type())
zyIpv6sgStaticBindingRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:zyIpv6sgStaticBindingRowStatus.setStatus(_A)
_ZyxelIpv6sgPolicyMaxNumberOfRules_Type=Integer32
_ZyxelIpv6sgPolicyMaxNumberOfRules_Object=MibScalar
zyxelIpv6sgPolicyMaxNumberOfRules=_ZyxelIpv6sgPolicyMaxNumberOfRules_Object((1,3,6,1,4,1,890,1,15,3,108,1,3),_ZyxelIpv6sgPolicyMaxNumberOfRules_Type())
zyxelIpv6sgPolicyMaxNumberOfRules.setMaxAccess(_D)
if mibBuilder.loadTexts:zyxelIpv6sgPolicyMaxNumberOfRules.setStatus(_A)
_ZyxelIpv6sgPolicyTable_Object=MibTable
zyxelIpv6sgPolicyTable=_ZyxelIpv6sgPolicyTable_Object((1,3,6,1,4,1,890,1,15,3,108,1,4))
if mibBuilder.loadTexts:zyxelIpv6sgPolicyTable.setStatus(_A)
_ZyxelIpv6sgPolicyEntry_Object=MibTableRow
zyxelIpv6sgPolicyEntry=_ZyxelIpv6sgPolicyEntry_Object((1,3,6,1,4,1,890,1,15,3,108,1,4,1))
zyxelIpv6sgPolicyEntry.setIndexNames((0,_C,_L))
if mibBuilder.loadTexts:zyxelIpv6sgPolicyEntry.setStatus(_A)
_ZyIpv6sgPolicyName_Type=DisplayString
_ZyIpv6sgPolicyName_Object=MibTableColumn
zyIpv6sgPolicyName=_ZyIpv6sgPolicyName_Object((1,3,6,1,4,1,890,1,15,3,108,1,4,1,1),_ZyIpv6sgPolicyName_Type())
zyIpv6sgPolicyName.setMaxAccess(_E)
if mibBuilder.loadTexts:zyIpv6sgPolicyName.setStatus(_A)
_ZyIpv6sgPolicyValidateAddressState_Type=EnabledStatus
_ZyIpv6sgPolicyValidateAddressState_Object=MibTableColumn
zyIpv6sgPolicyValidateAddressState=_ZyIpv6sgPolicyValidateAddressState_Object((1,3,6,1,4,1,890,1,15,3,108,1,4,1,2),_ZyIpv6sgPolicyValidateAddressState_Type())
zyIpv6sgPolicyValidateAddressState.setMaxAccess(_B)
if mibBuilder.loadTexts:zyIpv6sgPolicyValidateAddressState.setStatus(_A)
_ZyIpv6sgPolicyValidatePrefixState_Type=EnabledStatus
_ZyIpv6sgPolicyValidatePrefixState_Object=MibTableColumn
zyIpv6sgPolicyValidatePrefixState=_ZyIpv6sgPolicyValidatePrefixState_Object((1,3,6,1,4,1,890,1,15,3,108,1,4,1,3),_ZyIpv6sgPolicyValidatePrefixState_Type())
zyIpv6sgPolicyValidatePrefixState.setMaxAccess(_B)
if mibBuilder.loadTexts:zyIpv6sgPolicyValidatePrefixState.setStatus(_A)
_ZyIpv6sgPolicyPermitLinkLocalState_Type=EnabledStatus
_ZyIpv6sgPolicyPermitLinkLocalState_Object=MibTableColumn
zyIpv6sgPolicyPermitLinkLocalState=_ZyIpv6sgPolicyPermitLinkLocalState_Object((1,3,6,1,4,1,890,1,15,3,108,1,4,1,4),_ZyIpv6sgPolicyPermitLinkLocalState_Type())
zyIpv6sgPolicyPermitLinkLocalState.setMaxAccess(_B)
if mibBuilder.loadTexts:zyIpv6sgPolicyPermitLinkLocalState.setStatus(_A)
_ZyIpv6sgPolicyRowStatus_Type=RowStatus
_ZyIpv6sgPolicyRowStatus_Object=MibTableColumn
zyIpv6sgPolicyRowStatus=_ZyIpv6sgPolicyRowStatus_Object((1,3,6,1,4,1,890,1,15,3,108,1,4,1,100),_ZyIpv6sgPolicyRowStatus_Type())
zyIpv6sgPolicyRowStatus.setMaxAccess('read-create')
if mibBuilder.loadTexts:zyIpv6sgPolicyRowStatus.setStatus(_A)
_ZyxelIpv6sgPolicyPortTable_Object=MibTable
zyxelIpv6sgPolicyPortTable=_ZyxelIpv6sgPolicyPortTable_Object((1,3,6,1,4,1,890,1,15,3,108,1,5))
if mibBuilder.loadTexts:zyxelIpv6sgPolicyPortTable.setStatus(_A)
_ZyxelIpv6sgPolicyPortEntry_Object=MibTableRow
zyxelIpv6sgPolicyPortEntry=_ZyxelIpv6sgPolicyPortEntry_Object((1,3,6,1,4,1,890,1,15,3,108,1,5,1))
zyxelIpv6sgPolicyPortEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:zyxelIpv6sgPolicyPortEntry.setStatus(_A)
_ZyIpv6sgPolicyPortAttachPolicy_Type=DisplayString
_ZyIpv6sgPolicyPortAttachPolicy_Object=MibTableColumn
zyIpv6sgPolicyPortAttachPolicy=_ZyIpv6sgPolicyPortAttachPolicy_Object((1,3,6,1,4,1,890,1,15,3,108,1,5,1,1),_ZyIpv6sgPolicyPortAttachPolicy_Type())
zyIpv6sgPolicyPortAttachPolicy.setMaxAccess(_B)
if mibBuilder.loadTexts:zyIpv6sgPolicyPortAttachPolicy.setStatus(_A)
_ZyxelIpv6sgStatus_ObjectIdentity=ObjectIdentity
zyxelIpv6sgStatus=_ZyxelIpv6sgStatus_ObjectIdentity((1,3,6,1,4,1,890,1,15,3,108,2))
_ZyIpv6sgBindingClearAll_Type=EnabledStatus
_ZyIpv6sgBindingClearAll_Object=MibScalar
zyIpv6sgBindingClearAll=_ZyIpv6sgBindingClearAll_Object((1,3,6,1,4,1,890,1,15,3,108,2,1),_ZyIpv6sgBindingClearAll_Type())
zyIpv6sgBindingClearAll.setMaxAccess(_B)
if mibBuilder.loadTexts:zyIpv6sgBindingClearAll.setStatus(_A)
_ZyxelIpv6sgBindingTable_Object=MibTable
zyxelIpv6sgBindingTable=_ZyxelIpv6sgBindingTable_Object((1,3,6,1,4,1,890,1,15,3,108,2,2))
if mibBuilder.loadTexts:zyxelIpv6sgBindingTable.setStatus(_A)
_ZyxelIpv6sgBindingEntry_Object=MibTableRow
zyxelIpv6sgBindingEntry=_ZyxelIpv6sgBindingEntry_Object((1,3,6,1,4,1,890,1,15,3,108,2,2,1))
zyxelIpv6sgBindingEntry.setIndexNames((0,_C,_M),(0,_C,_N),(0,_C,_O))
if mibBuilder.loadTexts:zyxelIpv6sgBindingEntry.setStatus(_A)
_ZyIpv6sgBindingIpv6AddressType_Type=InetAddressType
_ZyIpv6sgBindingIpv6AddressType_Object=MibTableColumn
zyIpv6sgBindingIpv6AddressType=_ZyIpv6sgBindingIpv6AddressType_Object((1,3,6,1,4,1,890,1,15,3,108,2,2,1,1),_ZyIpv6sgBindingIpv6AddressType_Type())
zyIpv6sgBindingIpv6AddressType.setMaxAccess(_E)
if mibBuilder.loadTexts:zyIpv6sgBindingIpv6AddressType.setStatus(_A)
_ZyIpv6sgBindingIpv6Address_Type=InetAddress
_ZyIpv6sgBindingIpv6Address_Object=MibTableColumn
zyIpv6sgBindingIpv6Address=_ZyIpv6sgBindingIpv6Address_Object((1,3,6,1,4,1,890,1,15,3,108,2,2,1,2),_ZyIpv6sgBindingIpv6Address_Type())
zyIpv6sgBindingIpv6Address.setMaxAccess(_E)
if mibBuilder.loadTexts:zyIpv6sgBindingIpv6Address.setStatus(_A)
_ZyIpv6sgBindingIpv6PrefixLength_Type=Integer32
_ZyIpv6sgBindingIpv6PrefixLength_Object=MibTableColumn
zyIpv6sgBindingIpv6PrefixLength=_ZyIpv6sgBindingIpv6PrefixLength_Object((1,3,6,1,4,1,890,1,15,3,108,2,2,1,3),_ZyIpv6sgBindingIpv6PrefixLength_Type())
zyIpv6sgBindingIpv6PrefixLength.setMaxAccess(_E)
if mibBuilder.loadTexts:zyIpv6sgBindingIpv6PrefixLength.setStatus(_A)
_ZyIpv6sgBindingMacAddress_Type=MacAddress
_ZyIpv6sgBindingMacAddress_Object=MibTableColumn
zyIpv6sgBindingMacAddress=_ZyIpv6sgBindingMacAddress_Object((1,3,6,1,4,1,890,1,15,3,108,2,2,1,4),_ZyIpv6sgBindingMacAddress_Type())
zyIpv6sgBindingMacAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:zyIpv6sgBindingMacAddress.setStatus(_A)
_ZyIpv6sgBindingVid_Type=Integer32
_ZyIpv6sgBindingVid_Object=MibTableColumn
zyIpv6sgBindingVid=_ZyIpv6sgBindingVid_Object((1,3,6,1,4,1,890,1,15,3,108,2,2,1,5),_ZyIpv6sgBindingVid_Type())
zyIpv6sgBindingVid.setMaxAccess(_D)
if mibBuilder.loadTexts:zyIpv6sgBindingVid.setStatus(_A)
_ZyIpv6sgBindingPort_Type=Integer32
_ZyIpv6sgBindingPort_Object=MibTableColumn
zyIpv6sgBindingPort=_ZyIpv6sgBindingPort_Object((1,3,6,1,4,1,890,1,15,3,108,2,2,1,6),_ZyIpv6sgBindingPort_Type())
zyIpv6sgBindingPort.setMaxAccess(_D)
if mibBuilder.loadTexts:zyIpv6sgBindingPort.setStatus(_A)
_ZyIpv6sgBindingLeaseTime_Type=Integer32
_ZyIpv6sgBindingLeaseTime_Object=MibTableColumn
zyIpv6sgBindingLeaseTime=_ZyIpv6sgBindingLeaseTime_Object((1,3,6,1,4,1,890,1,15,3,108,2,2,1,7),_ZyIpv6sgBindingLeaseTime_Type())
zyIpv6sgBindingLeaseTime.setMaxAccess(_D)
if mibBuilder.loadTexts:zyIpv6sgBindingLeaseTime.setStatus(_A)
class _ZyIpv6sgBindingType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('static',1),('dhcp',2)))
_ZyIpv6sgBindingType_Type.__name__=_H
_ZyIpv6sgBindingType_Object=MibTableColumn
zyIpv6sgBindingType=_ZyIpv6sgBindingType_Object((1,3,6,1,4,1,890,1,15,3,108,2,2,1,8),_ZyIpv6sgBindingType_Type())
zyIpv6sgBindingType.setMaxAccess(_D)
if mibBuilder.loadTexts:zyIpv6sgBindingType.setStatus(_A)
_ZyIpv6sgBindingClear_Type=EnabledStatus
_ZyIpv6sgBindingClear_Object=MibTableColumn
zyIpv6sgBindingClear=_ZyIpv6sgBindingClear_Object((1,3,6,1,4,1,890,1,15,3,108,2,2,1,9),_ZyIpv6sgBindingClear_Type())
zyIpv6sgBindingClear.setMaxAccess(_B)
if mibBuilder.loadTexts:zyIpv6sgBindingClear.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'zyxelIpv6sg':zyxelIpv6sg,'zyxelIpv6sgSetup':zyxelIpv6sgSetup,'zyxelIpv6sgStaticBindingMaxNumberOfRules':zyxelIpv6sgStaticBindingMaxNumberOfRules,'zyxelIpv6sgStaticBindingTable':zyxelIpv6sgStaticBindingTable,'zyxelIpv6sgStaticBindingEntry':zyxelIpv6sgStaticBindingEntry,_I:zyIpv6sgStaticBindingIpv6AddressType,_J:zyIpv6sgStaticBindingIpv6Address,_K:zyIpv6sgStaticBindingIpv6PrefixLength,'zyIpv6sgStaticBindingMacAddress':zyIpv6sgStaticBindingMacAddress,'zyIpv6sgStaticBindingVid':zyIpv6sgStaticBindingVid,'zyIpv6sgStaticBindingPort':zyIpv6sgStaticBindingPort,'zyIpv6sgStaticBindingRowStatus':zyIpv6sgStaticBindingRowStatus,'zyxelIpv6sgPolicyMaxNumberOfRules':zyxelIpv6sgPolicyMaxNumberOfRules,'zyxelIpv6sgPolicyTable':zyxelIpv6sgPolicyTable,'zyxelIpv6sgPolicyEntry':zyxelIpv6sgPolicyEntry,_L:zyIpv6sgPolicyName,'zyIpv6sgPolicyValidateAddressState':zyIpv6sgPolicyValidateAddressState,'zyIpv6sgPolicyValidatePrefixState':zyIpv6sgPolicyValidatePrefixState,'zyIpv6sgPolicyPermitLinkLocalState':zyIpv6sgPolicyPermitLinkLocalState,'zyIpv6sgPolicyRowStatus':zyIpv6sgPolicyRowStatus,'zyxelIpv6sgPolicyPortTable':zyxelIpv6sgPolicyPortTable,'zyxelIpv6sgPolicyPortEntry':zyxelIpv6sgPolicyPortEntry,'zyIpv6sgPolicyPortAttachPolicy':zyIpv6sgPolicyPortAttachPolicy,'zyxelIpv6sgStatus':zyxelIpv6sgStatus,'zyIpv6sgBindingClearAll':zyIpv6sgBindingClearAll,'zyxelIpv6sgBindingTable':zyxelIpv6sgBindingTable,'zyxelIpv6sgBindingEntry':zyxelIpv6sgBindingEntry,_M:zyIpv6sgBindingIpv6AddressType,_N:zyIpv6sgBindingIpv6Address,_O:zyIpv6sgBindingIpv6PrefixLength,'zyIpv6sgBindingMacAddress':zyIpv6sgBindingMacAddress,'zyIpv6sgBindingVid':zyIpv6sgBindingVid,'zyIpv6sgBindingPort':zyIpv6sgBindingPort,'zyIpv6sgBindingLeaseTime':zyIpv6sgBindingLeaseTime,'zyIpv6sgBindingType':zyIpv6sgBindingType,'zyIpv6sgBindingClear':zyIpv6sgBindingClear})