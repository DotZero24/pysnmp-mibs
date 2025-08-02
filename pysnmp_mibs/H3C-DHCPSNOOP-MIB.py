_T='h3cDhcpSnoopBindingMac'
_S='h3cDhcpSnoopBindingIP'
_R='h3cDhcpSnoopSpoofServerIP'
_Q='h3cDhcpSnoopSpoofServerMac'
_P='h3cDhcpSnoopVlanIndex'
_O='h3cDhcpSnoopClientIpAddress'
_N='h3cDhcpSnoopClientIpAddressType'
_M='TruthValue'
_L='InetAddressType'
_K='hwdot1qVlanIndex'
_J='HUAWEI-LswVLAN-MIB'
_I='read-only'
_H='not-accessible'
_G='read-write'
_F='ifIndex'
_E='IF-MIB'
_D='accessible-for-notify'
_C='Integer32'
_B='H3C-DHCPSNOOP-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
h3cCommon,=mibBuilder.importSymbols('HUAWEI-3COM-OID-MIB','h3cCommon')
hwdot1qVlanIndex,=mibBuilder.importSymbols(_J,_K)
ifIndex,=mibBuilder.importSymbols(_E,_F)
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress',_L)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','TextualConvention',_M)
h3cDhcpSnoop=ModuleIdentity((1,3,6,1,4,1,2011,10,2,36))
_H3cDhcpSnoopMibObject_ObjectIdentity=ObjectIdentity
h3cDhcpSnoopMibObject=_H3cDhcpSnoopMibObject_ObjectIdentity((1,3,6,1,4,1,2011,10,2,36,1))
class _H3cDhcpSnoopEnable_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enable',1),('disable',2)))
_H3cDhcpSnoopEnable_Type.__name__=_C
_H3cDhcpSnoopEnable_Object=MibScalar
h3cDhcpSnoopEnable=_H3cDhcpSnoopEnable_Object((1,3,6,1,4,1,2011,10,2,36,1,1),_H3cDhcpSnoopEnable_Type())
h3cDhcpSnoopEnable.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cDhcpSnoopEnable.setStatus(_A)
_H3cDhcpSnoopTable_Object=MibTable
h3cDhcpSnoopTable=_H3cDhcpSnoopTable_Object((1,3,6,1,4,1,2011,10,2,36,1,2))
if mibBuilder.loadTexts:h3cDhcpSnoopTable.setStatus(_A)
_H3cDhcpSnoopEntry_Object=MibTableRow
h3cDhcpSnoopEntry=_H3cDhcpSnoopEntry_Object((1,3,6,1,4,1,2011,10,2,36,1,2,1))
h3cDhcpSnoopEntry.setIndexNames((0,_B,_N),(0,_B,_O))
if mibBuilder.loadTexts:h3cDhcpSnoopEntry.setStatus(_A)
class _H3cDhcpSnoopClientIpAddressType_Type(InetAddressType):defaultValue=1
_H3cDhcpSnoopClientIpAddressType_Type.__name__=_L
_H3cDhcpSnoopClientIpAddressType_Object=MibTableColumn
h3cDhcpSnoopClientIpAddressType=_H3cDhcpSnoopClientIpAddressType_Object((1,3,6,1,4,1,2011,10,2,36,1,2,1,1),_H3cDhcpSnoopClientIpAddressType_Type())
h3cDhcpSnoopClientIpAddressType.setMaxAccess(_H)
if mibBuilder.loadTexts:h3cDhcpSnoopClientIpAddressType.setStatus(_A)
_H3cDhcpSnoopClientIpAddress_Type=InetAddress
_H3cDhcpSnoopClientIpAddress_Object=MibTableColumn
h3cDhcpSnoopClientIpAddress=_H3cDhcpSnoopClientIpAddress_Object((1,3,6,1,4,1,2011,10,2,36,1,2,1,2),_H3cDhcpSnoopClientIpAddress_Type())
h3cDhcpSnoopClientIpAddress.setMaxAccess(_H)
if mibBuilder.loadTexts:h3cDhcpSnoopClientIpAddress.setStatus(_A)
_H3cDhcpSnoopClientMacAddress_Type=MacAddress
_H3cDhcpSnoopClientMacAddress_Object=MibTableColumn
h3cDhcpSnoopClientMacAddress=_H3cDhcpSnoopClientMacAddress_Object((1,3,6,1,4,1,2011,10,2,36,1,2,1,3),_H3cDhcpSnoopClientMacAddress_Type())
h3cDhcpSnoopClientMacAddress.setMaxAccess(_I)
if mibBuilder.loadTexts:h3cDhcpSnoopClientMacAddress.setStatus(_A)
class _H3cDhcpSnoopClientProperty_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('static',1),('dynamic',2)))
_H3cDhcpSnoopClientProperty_Type.__name__=_C
_H3cDhcpSnoopClientProperty_Object=MibTableColumn
h3cDhcpSnoopClientProperty=_H3cDhcpSnoopClientProperty_Object((1,3,6,1,4,1,2011,10,2,36,1,2,1,4),_H3cDhcpSnoopClientProperty_Type())
h3cDhcpSnoopClientProperty.setMaxAccess(_I)
if mibBuilder.loadTexts:h3cDhcpSnoopClientProperty.setStatus(_A)
_H3cDhcpSnoopClientUnitNum_Type=Integer32
_H3cDhcpSnoopClientUnitNum_Object=MibTableColumn
h3cDhcpSnoopClientUnitNum=_H3cDhcpSnoopClientUnitNum_Object((1,3,6,1,4,1,2011,10,2,36,1,2,1,5),_H3cDhcpSnoopClientUnitNum_Type())
h3cDhcpSnoopClientUnitNum.setMaxAccess(_I)
if mibBuilder.loadTexts:h3cDhcpSnoopClientUnitNum.setStatus(_A)
_H3cDhcpSnoopTrustTable_Object=MibTable
h3cDhcpSnoopTrustTable=_H3cDhcpSnoopTrustTable_Object((1,3,6,1,4,1,2011,10,2,36,1,3))
if mibBuilder.loadTexts:h3cDhcpSnoopTrustTable.setStatus(_A)
_H3cDhcpSnoopTrustEntry_Object=MibTableRow
h3cDhcpSnoopTrustEntry=_H3cDhcpSnoopTrustEntry_Object((1,3,6,1,4,1,2011,10,2,36,1,3,1))
h3cDhcpSnoopTrustEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:h3cDhcpSnoopTrustEntry.setStatus(_A)
class _H3cDhcpSnoopTrustStatus_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('untrusted',0),('trusted',1)))
_H3cDhcpSnoopTrustStatus_Type.__name__=_C
_H3cDhcpSnoopTrustStatus_Object=MibTableColumn
h3cDhcpSnoopTrustStatus=_H3cDhcpSnoopTrustStatus_Object((1,3,6,1,4,1,2011,10,2,36,1,3,1,1),_H3cDhcpSnoopTrustStatus_Type())
h3cDhcpSnoopTrustStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cDhcpSnoopTrustStatus.setStatus(_A)
_H3cDhcpSnoopVlanTable_Object=MibTable
h3cDhcpSnoopVlanTable=_H3cDhcpSnoopVlanTable_Object((1,3,6,1,4,1,2011,10,2,36,1,4))
if mibBuilder.loadTexts:h3cDhcpSnoopVlanTable.setStatus(_A)
_H3cDhcpSnoopVlanEntry_Object=MibTableRow
h3cDhcpSnoopVlanEntry=_H3cDhcpSnoopVlanEntry_Object((1,3,6,1,4,1,2011,10,2,36,1,4,1))
h3cDhcpSnoopVlanEntry.setIndexNames((0,_B,_P))
if mibBuilder.loadTexts:h3cDhcpSnoopVlanEntry.setStatus(_A)
class _H3cDhcpSnoopVlanIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_H3cDhcpSnoopVlanIndex_Type.__name__=_C
_H3cDhcpSnoopVlanIndex_Object=MibTableColumn
h3cDhcpSnoopVlanIndex=_H3cDhcpSnoopVlanIndex_Object((1,3,6,1,4,1,2011,10,2,36,1,4,1,1),_H3cDhcpSnoopVlanIndex_Type())
h3cDhcpSnoopVlanIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:h3cDhcpSnoopVlanIndex.setStatus(_A)
class _H3cDhcpSnoopVlanEnable_Type(TruthValue):defaultValue=2
_H3cDhcpSnoopVlanEnable_Type.__name__=_M
_H3cDhcpSnoopVlanEnable_Object=MibTableColumn
h3cDhcpSnoopVlanEnable=_H3cDhcpSnoopVlanEnable_Object((1,3,6,1,4,1,2011,10,2,36,1,4,1,2),_H3cDhcpSnoopVlanEnable_Type())
h3cDhcpSnoopVlanEnable.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cDhcpSnoopVlanEnable.setStatus(_A)
_H3cDhcpSnoopTraps_ObjectIdentity=ObjectIdentity
h3cDhcpSnoopTraps=_H3cDhcpSnoopTraps_ObjectIdentity((1,3,6,1,4,1,2011,10,2,36,2))
_H3cDhcpSnoopTrapsPrefix_ObjectIdentity=ObjectIdentity
h3cDhcpSnoopTrapsPrefix=_H3cDhcpSnoopTrapsPrefix_ObjectIdentity((1,3,6,1,4,1,2011,10,2,36,2,0))
_H3cDhcpSnoopTrapsObject_ObjectIdentity=ObjectIdentity
h3cDhcpSnoopTrapsObject=_H3cDhcpSnoopTrapsObject_ObjectIdentity((1,3,6,1,4,1,2011,10,2,36,2,1))
_H3cDhcpSnoopSpoofServerMac_Type=MacAddress
_H3cDhcpSnoopSpoofServerMac_Object=MibScalar
h3cDhcpSnoopSpoofServerMac=_H3cDhcpSnoopSpoofServerMac_Object((1,3,6,1,4,1,2011,10,2,36,2,1,1),_H3cDhcpSnoopSpoofServerMac_Type())
h3cDhcpSnoopSpoofServerMac.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cDhcpSnoopSpoofServerMac.setStatus(_A)
_H3cDhcpSnoopSpoofServerIP_Type=IpAddress
_H3cDhcpSnoopSpoofServerIP_Object=MibScalar
h3cDhcpSnoopSpoofServerIP=_H3cDhcpSnoopSpoofServerIP_Object((1,3,6,1,4,1,2011,10,2,36,2,1,2),_H3cDhcpSnoopSpoofServerIP_Type())
h3cDhcpSnoopSpoofServerIP.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cDhcpSnoopSpoofServerIP.setStatus(_A)
_H3cDhcpSnoopBindingIP_Type=IpAddress
_H3cDhcpSnoopBindingIP_Object=MibScalar
h3cDhcpSnoopBindingIP=_H3cDhcpSnoopBindingIP_Object((1,3,6,1,4,1,2011,10,2,36,2,1,3),_H3cDhcpSnoopBindingIP_Type())
h3cDhcpSnoopBindingIP.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cDhcpSnoopBindingIP.setStatus(_A)
_H3cDhcpSnoopBindingMac_Type=MacAddress
_H3cDhcpSnoopBindingMac_Object=MibScalar
h3cDhcpSnoopBindingMac=_H3cDhcpSnoopBindingMac_Object((1,3,6,1,4,1,2011,10,2,36,2,1,4),_H3cDhcpSnoopBindingMac_Type())
h3cDhcpSnoopBindingMac.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cDhcpSnoopBindingMac.setStatus(_A)
h3cDhcpSnoopSpoofServerDetected=NotificationType((1,3,6,1,4,1,2011,10,2,36,2,0,1))
h3cDhcpSnoopSpoofServerDetected.setObjects(*((_E,_F),(_J,_K),(_B,_Q),(_B,_R)))
if mibBuilder.loadTexts:h3cDhcpSnoopSpoofServerDetected.setStatus(_A)
h3cDhcpSnoopNewBinding=NotificationType((1,3,6,1,4,1,2011,10,2,36,2,0,2))
h3cDhcpSnoopNewBinding.setObjects(*((_B,_S),(_B,_T)))
if mibBuilder.loadTexts:h3cDhcpSnoopNewBinding.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'h3cDhcpSnoop':h3cDhcpSnoop,'h3cDhcpSnoopMibObject':h3cDhcpSnoopMibObject,'h3cDhcpSnoopEnable':h3cDhcpSnoopEnable,'h3cDhcpSnoopTable':h3cDhcpSnoopTable,'h3cDhcpSnoopEntry':h3cDhcpSnoopEntry,_N:h3cDhcpSnoopClientIpAddressType,_O:h3cDhcpSnoopClientIpAddress,'h3cDhcpSnoopClientMacAddress':h3cDhcpSnoopClientMacAddress,'h3cDhcpSnoopClientProperty':h3cDhcpSnoopClientProperty,'h3cDhcpSnoopClientUnitNum':h3cDhcpSnoopClientUnitNum,'h3cDhcpSnoopTrustTable':h3cDhcpSnoopTrustTable,'h3cDhcpSnoopTrustEntry':h3cDhcpSnoopTrustEntry,'h3cDhcpSnoopTrustStatus':h3cDhcpSnoopTrustStatus,'h3cDhcpSnoopVlanTable':h3cDhcpSnoopVlanTable,'h3cDhcpSnoopVlanEntry':h3cDhcpSnoopVlanEntry,_P:h3cDhcpSnoopVlanIndex,'h3cDhcpSnoopVlanEnable':h3cDhcpSnoopVlanEnable,'h3cDhcpSnoopTraps':h3cDhcpSnoopTraps,'h3cDhcpSnoopTrapsPrefix':h3cDhcpSnoopTrapsPrefix,'h3cDhcpSnoopSpoofServerDetected':h3cDhcpSnoopSpoofServerDetected,'h3cDhcpSnoopNewBinding':h3cDhcpSnoopNewBinding,'h3cDhcpSnoopTrapsObject':h3cDhcpSnoopTrapsObject,_Q:h3cDhcpSnoopSpoofServerMac,_R:h3cDhcpSnoopSpoofServerIP,_S:h3cDhcpSnoopBindingIP,_T:h3cDhcpSnoopBindingMac})