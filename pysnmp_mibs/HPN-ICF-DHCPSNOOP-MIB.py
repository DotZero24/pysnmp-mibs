_T='hpnicfDhcpSnoopBindingMac'
_S='hpnicfDhcpSnoopBindingIP'
_R='hpnicfDhcpSnoopSpoofServerIP'
_Q='hpnicfDhcpSnoopSpoofServerMac'
_P='hpnicfDhcpSnoopVlanIndex'
_O='hpnicfDhcpSnoopClientIpAddress'
_N='hpnicfDhcpSnoopClientIpAddressType'
_M='TruthValue'
_L='InetAddressType'
_K='hpnicfdot1qVlanIndex'
_J='HPN-ICF-LswVLAN-MIB'
_I='read-only'
_H='not-accessible'
_G='read-write'
_F='ifIndex'
_E='IF-MIB'
_D='accessible-for-notify'
_C='Integer32'
_B='HPN-ICF-DHCPSNOOP-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hpnicfdot1qVlanIndex,=mibBuilder.importSymbols(_J,_K)
hpnicfCommon,=mibBuilder.importSymbols('HPN-ICF-OID-MIB','hpnicfCommon')
ifIndex,=mibBuilder.importSymbols(_E,_F)
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress',_L)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','TextualConvention',_M)
hpnicfDhcpSnoop=ModuleIdentity((1,3,6,1,4,1,11,2,14,11,15,2,36))
_HpnicfDhcpSnoopMibObject_ObjectIdentity=ObjectIdentity
hpnicfDhcpSnoopMibObject=_HpnicfDhcpSnoopMibObject_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,36,1))
class _HpnicfDhcpSnoopEnable_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enable',1),('disable',2)))
_HpnicfDhcpSnoopEnable_Type.__name__=_C
_HpnicfDhcpSnoopEnable_Object=MibScalar
hpnicfDhcpSnoopEnable=_HpnicfDhcpSnoopEnable_Object((1,3,6,1,4,1,11,2,14,11,15,2,36,1,1),_HpnicfDhcpSnoopEnable_Type())
hpnicfDhcpSnoopEnable.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfDhcpSnoopEnable.setStatus(_A)
_HpnicfDhcpSnoopTable_Object=MibTable
hpnicfDhcpSnoopTable=_HpnicfDhcpSnoopTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,36,1,2))
if mibBuilder.loadTexts:hpnicfDhcpSnoopTable.setStatus(_A)
_HpnicfDhcpSnoopEntry_Object=MibTableRow
hpnicfDhcpSnoopEntry=_HpnicfDhcpSnoopEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,36,1,2,1))
hpnicfDhcpSnoopEntry.setIndexNames((0,_B,_N),(0,_B,_O))
if mibBuilder.loadTexts:hpnicfDhcpSnoopEntry.setStatus(_A)
class _HpnicfDhcpSnoopClientIpAddressType_Type(InetAddressType):defaultValue=1
_HpnicfDhcpSnoopClientIpAddressType_Type.__name__=_L
_HpnicfDhcpSnoopClientIpAddressType_Object=MibTableColumn
hpnicfDhcpSnoopClientIpAddressType=_HpnicfDhcpSnoopClientIpAddressType_Object((1,3,6,1,4,1,11,2,14,11,15,2,36,1,2,1,1),_HpnicfDhcpSnoopClientIpAddressType_Type())
hpnicfDhcpSnoopClientIpAddressType.setMaxAccess(_H)
if mibBuilder.loadTexts:hpnicfDhcpSnoopClientIpAddressType.setStatus(_A)
_HpnicfDhcpSnoopClientIpAddress_Type=InetAddress
_HpnicfDhcpSnoopClientIpAddress_Object=MibTableColumn
hpnicfDhcpSnoopClientIpAddress=_HpnicfDhcpSnoopClientIpAddress_Object((1,3,6,1,4,1,11,2,14,11,15,2,36,1,2,1,2),_HpnicfDhcpSnoopClientIpAddress_Type())
hpnicfDhcpSnoopClientIpAddress.setMaxAccess(_H)
if mibBuilder.loadTexts:hpnicfDhcpSnoopClientIpAddress.setStatus(_A)
_HpnicfDhcpSnoopClientMacAddress_Type=MacAddress
_HpnicfDhcpSnoopClientMacAddress_Object=MibTableColumn
hpnicfDhcpSnoopClientMacAddress=_HpnicfDhcpSnoopClientMacAddress_Object((1,3,6,1,4,1,11,2,14,11,15,2,36,1,2,1,3),_HpnicfDhcpSnoopClientMacAddress_Type())
hpnicfDhcpSnoopClientMacAddress.setMaxAccess(_I)
if mibBuilder.loadTexts:hpnicfDhcpSnoopClientMacAddress.setStatus(_A)
class _HpnicfDhcpSnoopClientProperty_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('static',1),('dynamic',2)))
_HpnicfDhcpSnoopClientProperty_Type.__name__=_C
_HpnicfDhcpSnoopClientProperty_Object=MibTableColumn
hpnicfDhcpSnoopClientProperty=_HpnicfDhcpSnoopClientProperty_Object((1,3,6,1,4,1,11,2,14,11,15,2,36,1,2,1,4),_HpnicfDhcpSnoopClientProperty_Type())
hpnicfDhcpSnoopClientProperty.setMaxAccess(_I)
if mibBuilder.loadTexts:hpnicfDhcpSnoopClientProperty.setStatus(_A)
_HpnicfDhcpSnoopClientUnitNum_Type=Integer32
_HpnicfDhcpSnoopClientUnitNum_Object=MibTableColumn
hpnicfDhcpSnoopClientUnitNum=_HpnicfDhcpSnoopClientUnitNum_Object((1,3,6,1,4,1,11,2,14,11,15,2,36,1,2,1,5),_HpnicfDhcpSnoopClientUnitNum_Type())
hpnicfDhcpSnoopClientUnitNum.setMaxAccess(_I)
if mibBuilder.loadTexts:hpnicfDhcpSnoopClientUnitNum.setStatus(_A)
_HpnicfDhcpSnoopTrustTable_Object=MibTable
hpnicfDhcpSnoopTrustTable=_HpnicfDhcpSnoopTrustTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,36,1,3))
if mibBuilder.loadTexts:hpnicfDhcpSnoopTrustTable.setStatus(_A)
_HpnicfDhcpSnoopTrustEntry_Object=MibTableRow
hpnicfDhcpSnoopTrustEntry=_HpnicfDhcpSnoopTrustEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,36,1,3,1))
hpnicfDhcpSnoopTrustEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:hpnicfDhcpSnoopTrustEntry.setStatus(_A)
class _HpnicfDhcpSnoopTrustStatus_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('untrusted',0),('trusted',1)))
_HpnicfDhcpSnoopTrustStatus_Type.__name__=_C
_HpnicfDhcpSnoopTrustStatus_Object=MibTableColumn
hpnicfDhcpSnoopTrustStatus=_HpnicfDhcpSnoopTrustStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,36,1,3,1,1),_HpnicfDhcpSnoopTrustStatus_Type())
hpnicfDhcpSnoopTrustStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfDhcpSnoopTrustStatus.setStatus(_A)
_HpnicfDhcpSnoopVlanTable_Object=MibTable
hpnicfDhcpSnoopVlanTable=_HpnicfDhcpSnoopVlanTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,36,1,4))
if mibBuilder.loadTexts:hpnicfDhcpSnoopVlanTable.setStatus(_A)
_HpnicfDhcpSnoopVlanEntry_Object=MibTableRow
hpnicfDhcpSnoopVlanEntry=_HpnicfDhcpSnoopVlanEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,36,1,4,1))
hpnicfDhcpSnoopVlanEntry.setIndexNames((0,_B,_P))
if mibBuilder.loadTexts:hpnicfDhcpSnoopVlanEntry.setStatus(_A)
class _HpnicfDhcpSnoopVlanIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_HpnicfDhcpSnoopVlanIndex_Type.__name__=_C
_HpnicfDhcpSnoopVlanIndex_Object=MibTableColumn
hpnicfDhcpSnoopVlanIndex=_HpnicfDhcpSnoopVlanIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,36,1,4,1,1),_HpnicfDhcpSnoopVlanIndex_Type())
hpnicfDhcpSnoopVlanIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:hpnicfDhcpSnoopVlanIndex.setStatus(_A)
class _HpnicfDhcpSnoopVlanEnable_Type(TruthValue):defaultValue=2
_HpnicfDhcpSnoopVlanEnable_Type.__name__=_M
_HpnicfDhcpSnoopVlanEnable_Object=MibTableColumn
hpnicfDhcpSnoopVlanEnable=_HpnicfDhcpSnoopVlanEnable_Object((1,3,6,1,4,1,11,2,14,11,15,2,36,1,4,1,2),_HpnicfDhcpSnoopVlanEnable_Type())
hpnicfDhcpSnoopVlanEnable.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfDhcpSnoopVlanEnable.setStatus(_A)
_HpnicfDhcpSnoopTraps_ObjectIdentity=ObjectIdentity
hpnicfDhcpSnoopTraps=_HpnicfDhcpSnoopTraps_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,36,2))
_HpnicfDhcpSnoopTrapsPrefix_ObjectIdentity=ObjectIdentity
hpnicfDhcpSnoopTrapsPrefix=_HpnicfDhcpSnoopTrapsPrefix_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,36,2,0))
_HpnicfDhcpSnoopTrapsObject_ObjectIdentity=ObjectIdentity
hpnicfDhcpSnoopTrapsObject=_HpnicfDhcpSnoopTrapsObject_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,36,2,1))
_HpnicfDhcpSnoopSpoofServerMac_Type=MacAddress
_HpnicfDhcpSnoopSpoofServerMac_Object=MibScalar
hpnicfDhcpSnoopSpoofServerMac=_HpnicfDhcpSnoopSpoofServerMac_Object((1,3,6,1,4,1,11,2,14,11,15,2,36,2,1,1),_HpnicfDhcpSnoopSpoofServerMac_Type())
hpnicfDhcpSnoopSpoofServerMac.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfDhcpSnoopSpoofServerMac.setStatus(_A)
_HpnicfDhcpSnoopSpoofServerIP_Type=IpAddress
_HpnicfDhcpSnoopSpoofServerIP_Object=MibScalar
hpnicfDhcpSnoopSpoofServerIP=_HpnicfDhcpSnoopSpoofServerIP_Object((1,3,6,1,4,1,11,2,14,11,15,2,36,2,1,2),_HpnicfDhcpSnoopSpoofServerIP_Type())
hpnicfDhcpSnoopSpoofServerIP.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfDhcpSnoopSpoofServerIP.setStatus(_A)
_HpnicfDhcpSnoopBindingIP_Type=IpAddress
_HpnicfDhcpSnoopBindingIP_Object=MibScalar
hpnicfDhcpSnoopBindingIP=_HpnicfDhcpSnoopBindingIP_Object((1,3,6,1,4,1,11,2,14,11,15,2,36,2,1,3),_HpnicfDhcpSnoopBindingIP_Type())
hpnicfDhcpSnoopBindingIP.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfDhcpSnoopBindingIP.setStatus(_A)
_HpnicfDhcpSnoopBindingMac_Type=MacAddress
_HpnicfDhcpSnoopBindingMac_Object=MibScalar
hpnicfDhcpSnoopBindingMac=_HpnicfDhcpSnoopBindingMac_Object((1,3,6,1,4,1,11,2,14,11,15,2,36,2,1,4),_HpnicfDhcpSnoopBindingMac_Type())
hpnicfDhcpSnoopBindingMac.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfDhcpSnoopBindingMac.setStatus(_A)
hpnicfDhcpSnoopSpoofServerDetected=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,36,2,0,1))
hpnicfDhcpSnoopSpoofServerDetected.setObjects(*((_E,_F),(_J,_K),(_B,_Q),(_B,_R)))
if mibBuilder.loadTexts:hpnicfDhcpSnoopSpoofServerDetected.setStatus(_A)
hpnicfDhcpSnoopNewBinding=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,36,2,0,2))
hpnicfDhcpSnoopNewBinding.setObjects(*((_B,_S),(_B,_T)))
if mibBuilder.loadTexts:hpnicfDhcpSnoopNewBinding.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'hpnicfDhcpSnoop':hpnicfDhcpSnoop,'hpnicfDhcpSnoopMibObject':hpnicfDhcpSnoopMibObject,'hpnicfDhcpSnoopEnable':hpnicfDhcpSnoopEnable,'hpnicfDhcpSnoopTable':hpnicfDhcpSnoopTable,'hpnicfDhcpSnoopEntry':hpnicfDhcpSnoopEntry,_N:hpnicfDhcpSnoopClientIpAddressType,_O:hpnicfDhcpSnoopClientIpAddress,'hpnicfDhcpSnoopClientMacAddress':hpnicfDhcpSnoopClientMacAddress,'hpnicfDhcpSnoopClientProperty':hpnicfDhcpSnoopClientProperty,'hpnicfDhcpSnoopClientUnitNum':hpnicfDhcpSnoopClientUnitNum,'hpnicfDhcpSnoopTrustTable':hpnicfDhcpSnoopTrustTable,'hpnicfDhcpSnoopTrustEntry':hpnicfDhcpSnoopTrustEntry,'hpnicfDhcpSnoopTrustStatus':hpnicfDhcpSnoopTrustStatus,'hpnicfDhcpSnoopVlanTable':hpnicfDhcpSnoopVlanTable,'hpnicfDhcpSnoopVlanEntry':hpnicfDhcpSnoopVlanEntry,_P:hpnicfDhcpSnoopVlanIndex,'hpnicfDhcpSnoopVlanEnable':hpnicfDhcpSnoopVlanEnable,'hpnicfDhcpSnoopTraps':hpnicfDhcpSnoopTraps,'hpnicfDhcpSnoopTrapsPrefix':hpnicfDhcpSnoopTrapsPrefix,'hpnicfDhcpSnoopSpoofServerDetected':hpnicfDhcpSnoopSpoofServerDetected,'hpnicfDhcpSnoopNewBinding':hpnicfDhcpSnoopNewBinding,'hpnicfDhcpSnoopTrapsObject':hpnicfDhcpSnoopTrapsObject,_Q:hpnicfDhcpSnoopSpoofServerMac,_R:hpnicfDhcpSnoopSpoofServerIP,_S:hpnicfDhcpSnoopBindingIP,_T:hpnicfDhcpSnoopBindingMac})