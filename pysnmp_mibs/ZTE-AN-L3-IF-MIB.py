_N='zxAnL3IfIpv6IpAddress'
_M='zxAnL3IfIpAddress'
_L='read-only'
_K='DisplayString'
_J='OctetString'
_I='read-write'
_H='disable'
_G='enable'
_F='not-accessible'
_E='zxAnL3IfIndex'
_D='ZTE-AN-L3-IF-MIB'
_C='Integer32'
_B='read-create'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_J,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InetAddress,InetAddressPrefixLength=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressPrefixLength')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_K,'PhysAddress','RowStatus','TextualConvention')
ZxAnIfindex,zxAn=mibBuilder.importSymbols('ZTE-AN-TC-MIB','ZxAnIfindex','zxAn')
zxAnL3InterfaceMib=ModuleIdentity((1,3,6,1,4,1,3902,1015,4))
_ZxAnL3InterfaceObjects_ObjectIdentity=ObjectIdentity
zxAnL3InterfaceObjects=_ZxAnL3InterfaceObjects_ObjectIdentity((1,3,6,1,4,1,3902,1015,4,1))
_ZxAnL3IfTable_Object=MibTable
zxAnL3IfTable=_ZxAnL3IfTable_Object((1,3,6,1,4,1,3902,1015,4,1,1))
if mibBuilder.loadTexts:zxAnL3IfTable.setStatus(_A)
_ZxAnL3IfEntry_Object=MibTableRow
zxAnL3IfEntry=_ZxAnL3IfEntry_Object((1,3,6,1,4,1,3902,1015,4,1,1,1))
zxAnL3IfEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:zxAnL3IfEntry.setStatus(_A)
_ZxAnL3IfIndex_Type=ZxAnIfindex
_ZxAnL3IfIndex_Object=MibTableColumn
zxAnL3IfIndex=_ZxAnL3IfIndex_Object((1,3,6,1,4,1,3902,1015,4,1,1,1,1),_ZxAnL3IfIndex_Type())
zxAnL3IfIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:zxAnL3IfIndex.setStatus(_A)
class _ZxAnL3IfName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_ZxAnL3IfName_Type.__name__=_K
_ZxAnL3IfName_Object=MibTableColumn
zxAnL3IfName=_ZxAnL3IfName_Object((1,3,6,1,4,1,3902,1015,4,1,1,1,2),_ZxAnL3IfName_Type())
zxAnL3IfName.setMaxAccess(_L)
if mibBuilder.loadTexts:zxAnL3IfName.setStatus(_A)
_ZxAnIfReferIndex_Type=Integer32
_ZxAnIfReferIndex_Object=MibTableColumn
zxAnIfReferIndex=_ZxAnIfReferIndex_Object((1,3,6,1,4,1,3902,1015,4,1,1,1,3),_ZxAnIfReferIndex_Type())
zxAnIfReferIndex.setMaxAccess(_L)
if mibBuilder.loadTexts:zxAnIfReferIndex.setStatus(_A)
class _ZxAnL3IfArpProxyEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_ZxAnL3IfArpProxyEnable_Type.__name__=_C
_ZxAnL3IfArpProxyEnable_Object=MibTableColumn
zxAnL3IfArpProxyEnable=_ZxAnL3IfArpProxyEnable_Object((1,3,6,1,4,1,3902,1015,4,1,1,1,4),_ZxAnL3IfArpProxyEnable_Type())
zxAnL3IfArpProxyEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnL3IfArpProxyEnable.setStatus(_A)
_ZxAnL3IfRowStatus_Type=RowStatus
_ZxAnL3IfRowStatus_Object=MibTableColumn
zxAnL3IfRowStatus=_ZxAnL3IfRowStatus_Object((1,3,6,1,4,1,3902,1015,4,1,1,1,5),_ZxAnL3IfRowStatus_Type())
zxAnL3IfRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnL3IfRowStatus.setStatus(_A)
class _ZxAnL3IfArpAgingTime_Type(Integer32):defaultValue=300;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967))
_ZxAnL3IfArpAgingTime_Type.__name__=_C
_ZxAnL3IfArpAgingTime_Object=MibTableColumn
zxAnL3IfArpAgingTime=_ZxAnL3IfArpAgingTime_Object((1,3,6,1,4,1,3902,1015,4,1,1,1,6),_ZxAnL3IfArpAgingTime_Type())
zxAnL3IfArpAgingTime.setMaxAccess(_I)
if mibBuilder.loadTexts:zxAnL3IfArpAgingTime.setStatus(_A)
if mibBuilder.loadTexts:zxAnL3IfArpAgingTime.setUnits('second')
_ZxAnL3IfSuperVlanTable_Object=MibTable
zxAnL3IfSuperVlanTable=_ZxAnL3IfSuperVlanTable_Object((1,3,6,1,4,1,3902,1015,4,1,2))
if mibBuilder.loadTexts:zxAnL3IfSuperVlanTable.setStatus(_A)
_ZxAnL3IfSuperVlanEntry_Object=MibTableRow
zxAnL3IfSuperVlanEntry=_ZxAnL3IfSuperVlanEntry_Object((1,3,6,1,4,1,3902,1015,4,1,2,1))
zxAnL3IfSuperVlanEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:zxAnL3IfSuperVlanEntry.setStatus(_A)
class _ZxAnL3IfSubvlanRoutingEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_ZxAnL3IfSubvlanRoutingEnable_Type.__name__=_C
_ZxAnL3IfSubvlanRoutingEnable_Object=MibTableColumn
zxAnL3IfSubvlanRoutingEnable=_ZxAnL3IfSubvlanRoutingEnable_Object((1,3,6,1,4,1,3902,1015,4,1,2,1,1),_ZxAnL3IfSubvlanRoutingEnable_Type())
zxAnL3IfSubvlanRoutingEnable.setMaxAccess(_I)
if mibBuilder.loadTexts:zxAnL3IfSubvlanRoutingEnable.setStatus(_A)
class _ZxAnL3IfSubvlanList_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,5472))
_ZxAnL3IfSubvlanList_Type.__name__=_J
_ZxAnL3IfSubvlanList_Object=MibTableColumn
zxAnL3IfSubvlanList=_ZxAnL3IfSubvlanList_Object((1,3,6,1,4,1,3902,1015,4,1,2,1,2),_ZxAnL3IfSubvlanList_Type())
zxAnL3IfSubvlanList.setMaxAccess(_I)
if mibBuilder.loadTexts:zxAnL3IfSubvlanList.setStatus(_A)
_ZxAnL3IfIpAddressTable_Object=MibTable
zxAnL3IfIpAddressTable=_ZxAnL3IfIpAddressTable_Object((1,3,6,1,4,1,3902,1015,4,1,3))
if mibBuilder.loadTexts:zxAnL3IfIpAddressTable.setStatus(_A)
_ZxAnL3IfIpAddressEntry_Object=MibTableRow
zxAnL3IfIpAddressEntry=_ZxAnL3IfIpAddressEntry_Object((1,3,6,1,4,1,3902,1015,4,1,3,1))
zxAnL3IfIpAddressEntry.setIndexNames((0,_D,_E),(0,_D,_M))
if mibBuilder.loadTexts:zxAnL3IfIpAddressEntry.setStatus(_A)
_ZxAnL3IfIpAddress_Type=IpAddress
_ZxAnL3IfIpAddress_Object=MibTableColumn
zxAnL3IfIpAddress=_ZxAnL3IfIpAddress_Object((1,3,6,1,4,1,3902,1015,4,1,3,1,1),_ZxAnL3IfIpAddress_Type())
zxAnL3IfIpAddress.setMaxAccess(_F)
if mibBuilder.loadTexts:zxAnL3IfIpAddress.setStatus(_A)
_ZxAnL3IfIpAddressMask_Type=IpAddress
_ZxAnL3IfIpAddressMask_Object=MibTableColumn
zxAnL3IfIpAddressMask=_ZxAnL3IfIpAddressMask_Object((1,3,6,1,4,1,3902,1015,4,1,3,1,2),_ZxAnL3IfIpAddressMask_Type())
zxAnL3IfIpAddressMask.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnL3IfIpAddressMask.setStatus(_A)
class _ZxAnL3IfIpCategory_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('single',1),('primary',2),('secondary',3)))
_ZxAnL3IfIpCategory_Type.__name__=_C
_ZxAnL3IfIpCategory_Object=MibTableColumn
zxAnL3IfIpCategory=_ZxAnL3IfIpCategory_Object((1,3,6,1,4,1,3902,1015,4,1,3,1,3),_ZxAnL3IfIpCategory_Type())
zxAnL3IfIpCategory.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnL3IfIpCategory.setStatus(_A)
_ZxAnL3IfIpRowStatus_Type=RowStatus
_ZxAnL3IfIpRowStatus_Object=MibTableColumn
zxAnL3IfIpRowStatus=_ZxAnL3IfIpRowStatus_Object((1,3,6,1,4,1,3902,1015,4,1,3,1,4),_ZxAnL3IfIpRowStatus_Type())
zxAnL3IfIpRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnL3IfIpRowStatus.setStatus(_A)
_ZxAnL3IfIpv6IpAddressTable_Object=MibTable
zxAnL3IfIpv6IpAddressTable=_ZxAnL3IfIpv6IpAddressTable_Object((1,3,6,1,4,1,3902,1015,4,1,4))
if mibBuilder.loadTexts:zxAnL3IfIpv6IpAddressTable.setStatus(_A)
_ZxAnL3IfIpv6IpAddressEntry_Object=MibTableRow
zxAnL3IfIpv6IpAddressEntry=_ZxAnL3IfIpv6IpAddressEntry_Object((1,3,6,1,4,1,3902,1015,4,1,4,1))
zxAnL3IfIpv6IpAddressEntry.setIndexNames((0,_D,_E),(0,_D,_N))
if mibBuilder.loadTexts:zxAnL3IfIpv6IpAddressEntry.setStatus(_A)
_ZxAnL3IfIpv6IpAddress_Type=InetAddress
_ZxAnL3IfIpv6IpAddress_Object=MibTableColumn
zxAnL3IfIpv6IpAddress=_ZxAnL3IfIpv6IpAddress_Object((1,3,6,1,4,1,3902,1015,4,1,4,1,1),_ZxAnL3IfIpv6IpAddress_Type())
zxAnL3IfIpv6IpAddress.setMaxAccess(_F)
if mibBuilder.loadTexts:zxAnL3IfIpv6IpAddress.setStatus(_A)
_ZxAnL3IfIpv6IpPfxLen_Type=InetAddressPrefixLength
_ZxAnL3IfIpv6IpPfxLen_Object=MibTableColumn
zxAnL3IfIpv6IpPfxLen=_ZxAnL3IfIpv6IpPfxLen_Object((1,3,6,1,4,1,3902,1015,4,1,4,1,2),_ZxAnL3IfIpv6IpPfxLen_Type())
zxAnL3IfIpv6IpPfxLen.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnL3IfIpv6IpPfxLen.setStatus(_A)
class _ZxAnL3IfIpv6Enable_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_ZxAnL3IfIpv6Enable_Type.__name__=_C
_ZxAnL3IfIpv6Enable_Object=MibTableColumn
zxAnL3IfIpv6Enable=_ZxAnL3IfIpv6Enable_Object((1,3,6,1,4,1,3902,1015,4,1,4,1,3),_ZxAnL3IfIpv6Enable_Type())
zxAnL3IfIpv6Enable.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnL3IfIpv6Enable.setStatus(_A)
class _ZxAnL3IfIpv6Mtu_Type(Integer32):defaultValue=1500;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1280,1500))
_ZxAnL3IfIpv6Mtu_Type.__name__=_C
_ZxAnL3IfIpv6Mtu_Object=MibTableColumn
zxAnL3IfIpv6Mtu=_ZxAnL3IfIpv6Mtu_Object((1,3,6,1,4,1,3902,1015,4,1,4,1,4),_ZxAnL3IfIpv6Mtu_Type())
zxAnL3IfIpv6Mtu.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnL3IfIpv6Mtu.setStatus(_A)
class _ZxAnL3IfIpv6DadAttemps_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,60))
_ZxAnL3IfIpv6DadAttemps_Type.__name__=_C
_ZxAnL3IfIpv6DadAttemps_Object=MibTableColumn
zxAnL3IfIpv6DadAttemps=_ZxAnL3IfIpv6DadAttemps_Object((1,3,6,1,4,1,3902,1015,4,1,4,1,5),_ZxAnL3IfIpv6DadAttemps_Type())
zxAnL3IfIpv6DadAttemps.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnL3IfIpv6DadAttemps.setStatus(_A)
_ZxAnL3IfIpv6RowStatus_Type=RowStatus
_ZxAnL3IfIpv6RowStatus_Object=MibTableColumn
zxAnL3IfIpv6RowStatus=_ZxAnL3IfIpv6RowStatus_Object((1,3,6,1,4,1,3902,1015,4,1,4,1,20),_ZxAnL3IfIpv6RowStatus_Type())
zxAnL3IfIpv6RowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnL3IfIpv6RowStatus.setStatus(_A)
_ZxAnL3InterfaceTrapObjects_ObjectIdentity=ObjectIdentity
zxAnL3InterfaceTrapObjects=_ZxAnL3InterfaceTrapObjects_ObjectIdentity((1,3,6,1,4,1,3902,1015,4,2))
mibBuilder.exportSymbols(_D,**{'zxAnL3InterfaceMib':zxAnL3InterfaceMib,'zxAnL3InterfaceObjects':zxAnL3InterfaceObjects,'zxAnL3IfTable':zxAnL3IfTable,'zxAnL3IfEntry':zxAnL3IfEntry,_E:zxAnL3IfIndex,'zxAnL3IfName':zxAnL3IfName,'zxAnIfReferIndex':zxAnIfReferIndex,'zxAnL3IfArpProxyEnable':zxAnL3IfArpProxyEnable,'zxAnL3IfRowStatus':zxAnL3IfRowStatus,'zxAnL3IfArpAgingTime':zxAnL3IfArpAgingTime,'zxAnL3IfSuperVlanTable':zxAnL3IfSuperVlanTable,'zxAnL3IfSuperVlanEntry':zxAnL3IfSuperVlanEntry,'zxAnL3IfSubvlanRoutingEnable':zxAnL3IfSubvlanRoutingEnable,'zxAnL3IfSubvlanList':zxAnL3IfSubvlanList,'zxAnL3IfIpAddressTable':zxAnL3IfIpAddressTable,'zxAnL3IfIpAddressEntry':zxAnL3IfIpAddressEntry,_M:zxAnL3IfIpAddress,'zxAnL3IfIpAddressMask':zxAnL3IfIpAddressMask,'zxAnL3IfIpCategory':zxAnL3IfIpCategory,'zxAnL3IfIpRowStatus':zxAnL3IfIpRowStatus,'zxAnL3IfIpv6IpAddressTable':zxAnL3IfIpv6IpAddressTable,'zxAnL3IfIpv6IpAddressEntry':zxAnL3IfIpv6IpAddressEntry,_N:zxAnL3IfIpv6IpAddress,'zxAnL3IfIpv6IpPfxLen':zxAnL3IfIpv6IpPfxLen,'zxAnL3IfIpv6Enable':zxAnL3IfIpv6Enable,'zxAnL3IfIpv6Mtu':zxAnL3IfIpv6Mtu,'zxAnL3IfIpv6DadAttemps':zxAnL3IfIpv6DadAttemps,'zxAnL3IfIpv6RowStatus':zxAnL3IfIpv6RowStatus,'zxAnL3InterfaceTrapObjects':zxAnL3InterfaceTrapObjects})