_M='zyIpv6GlobalAddressEUI64State'
_L='zyIpv6GlobalAddressPrefixLength'
_K='zyIpv6GlobalAddressIpAddress'
_J='zyIpv6GlobalAddressIpAddressType'
_I='zyIpv6GlobalAddressIfIndex'
_H='zyIpv6IfIndex'
_G='Integer32'
_F='EnabledStatus'
_E='read-only'
_D='not-accessible'
_C='ZYXEL-IPV6-MIB'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
EnabledStatus,=mibBuilder.importSymbols('P-BRIDGE-MIB',_F)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_G,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
esMgmt,=mibBuilder.importSymbols('ZYXEL-ES-SMI','esMgmt')
zyxelIpv6=ModuleIdentity((1,3,6,1,4,1,890,1,15,3,34))
_ZyxelIpv6Setup_ObjectIdentity=ObjectIdentity
zyxelIpv6Setup=_ZyxelIpv6Setup_ObjectIdentity((1,3,6,1,4,1,890,1,15,3,34,1))
_ZyIpv6HopLimit_Type=Integer32
_ZyIpv6HopLimit_Object=MibScalar
zyIpv6HopLimit=_ZyIpv6HopLimit_Object((1,3,6,1,4,1,890,1,15,3,34,1,1),_ZyIpv6HopLimit_Type())
zyIpv6HopLimit.setMaxAccess(_B)
if mibBuilder.loadTexts:zyIpv6HopLimit.setStatus(_A)
_ZyIpv6IcmpRateLimitErrorInterval_Type=Integer32
_ZyIpv6IcmpRateLimitErrorInterval_Object=MibScalar
zyIpv6IcmpRateLimitErrorInterval=_ZyIpv6IcmpRateLimitErrorInterval_Object((1,3,6,1,4,1,890,1,15,3,34,1,2),_ZyIpv6IcmpRateLimitErrorInterval_Type())
zyIpv6IcmpRateLimitErrorInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:zyIpv6IcmpRateLimitErrorInterval.setStatus(_A)
_ZyIpv6IcmpRateLimitBucketSize_Type=Integer32
_ZyIpv6IcmpRateLimitBucketSize_Object=MibScalar
zyIpv6IcmpRateLimitBucketSize=_ZyIpv6IcmpRateLimitBucketSize_Object((1,3,6,1,4,1,890,1,15,3,34,1,3),_ZyIpv6IcmpRateLimitBucketSize_Type())
zyIpv6IcmpRateLimitBucketSize.setMaxAccess(_B)
if mibBuilder.loadTexts:zyIpv6IcmpRateLimitBucketSize.setStatus(_A)
_ZyIpv6MaxNumberOfGlobalAddrresses_Type=Integer32
_ZyIpv6MaxNumberOfGlobalAddrresses_Object=MibScalar
zyIpv6MaxNumberOfGlobalAddrresses=_ZyIpv6MaxNumberOfGlobalAddrresses_Object((1,3,6,1,4,1,890,1,15,3,34,1,4),_ZyIpv6MaxNumberOfGlobalAddrresses_Type())
zyIpv6MaxNumberOfGlobalAddrresses.setMaxAccess(_E)
if mibBuilder.loadTexts:zyIpv6MaxNumberOfGlobalAddrresses.setStatus(_A)
_ZyxelIpv6Table_Object=MibTable
zyxelIpv6Table=_ZyxelIpv6Table_Object((1,3,6,1,4,1,890,1,15,3,34,1,5))
if mibBuilder.loadTexts:zyxelIpv6Table.setStatus(_A)
_ZyxelIpv6Entry_Object=MibTableRow
zyxelIpv6Entry=_ZyxelIpv6Entry_Object((1,3,6,1,4,1,890,1,15,3,34,1,5,1))
zyxelIpv6Entry.setIndexNames((0,_C,_H))
if mibBuilder.loadTexts:zyxelIpv6Entry.setStatus(_A)
_ZyIpv6IfIndex_Type=Integer32
_ZyIpv6IfIndex_Object=MibTableColumn
zyIpv6IfIndex=_ZyIpv6IfIndex_Object((1,3,6,1,4,1,890,1,15,3,34,1,5,1,1),_ZyIpv6IfIndex_Type())
zyIpv6IfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:zyIpv6IfIndex.setStatus(_A)
_ZyIpv6State_Type=EnabledStatus
_ZyIpv6State_Object=MibTableColumn
zyIpv6State=_ZyIpv6State_Object((1,3,6,1,4,1,890,1,15,3,34,1,5,1,2),_ZyIpv6State_Type())
zyIpv6State.setMaxAccess(_B)
if mibBuilder.loadTexts:zyIpv6State.setStatus(_A)
class _ZyIpv6AddressAutoConfigState_Type(EnabledStatus):subtypeSpec=EnabledStatus.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('stateless',1),('stateful',2)))
_ZyIpv6AddressAutoConfigState_Type.__name__=_F
_ZyIpv6AddressAutoConfigState_Object=MibTableColumn
zyIpv6AddressAutoConfigState=_ZyIpv6AddressAutoConfigState_Object((1,3,6,1,4,1,890,1,15,3,34,1,5,1,3),_ZyIpv6AddressAutoConfigState_Type())
zyIpv6AddressAutoConfigState.setMaxAccess(_B)
if mibBuilder.loadTexts:zyIpv6AddressAutoConfigState.setStatus(_A)
_ZyIpv6LinkLocalIpAddrressType_Type=InetAddressType
_ZyIpv6LinkLocalIpAddrressType_Object=MibTableColumn
zyIpv6LinkLocalIpAddrressType=_ZyIpv6LinkLocalIpAddrressType_Object((1,3,6,1,4,1,890,1,15,3,34,1,5,1,4),_ZyIpv6LinkLocalIpAddrressType_Type())
zyIpv6LinkLocalIpAddrressType.setMaxAccess(_E)
if mibBuilder.loadTexts:zyIpv6LinkLocalIpAddrressType.setStatus(_A)
_ZyIpv6LinkLocalIpAddrress_Type=InetAddress
_ZyIpv6LinkLocalIpAddrress_Object=MibTableColumn
zyIpv6LinkLocalIpAddrress=_ZyIpv6LinkLocalIpAddrress_Object((1,3,6,1,4,1,890,1,15,3,34,1,5,1,5),_ZyIpv6LinkLocalIpAddrress_Type())
zyIpv6LinkLocalIpAddrress.setMaxAccess(_B)
if mibBuilder.loadTexts:zyIpv6LinkLocalIpAddrress.setStatus(_A)
_ZyIpv6DefaultGatewayType_Type=InetAddressType
_ZyIpv6DefaultGatewayType_Object=MibTableColumn
zyIpv6DefaultGatewayType=_ZyIpv6DefaultGatewayType_Object((1,3,6,1,4,1,890,1,15,3,34,1,5,1,6),_ZyIpv6DefaultGatewayType_Type())
zyIpv6DefaultGatewayType.setMaxAccess(_E)
if mibBuilder.loadTexts:zyIpv6DefaultGatewayType.setStatus(_A)
_ZyIpv6DefaultGateway_Type=InetAddress
_ZyIpv6DefaultGateway_Object=MibTableColumn
zyIpv6DefaultGateway=_ZyIpv6DefaultGateway_Object((1,3,6,1,4,1,890,1,15,3,34,1,5,1,7),_ZyIpv6DefaultGateway_Type())
zyIpv6DefaultGateway.setMaxAccess(_B)
if mibBuilder.loadTexts:zyIpv6DefaultGateway.setStatus(_A)
_ZyxelIpv6GlobalAddressTable_Object=MibTable
zyxelIpv6GlobalAddressTable=_ZyxelIpv6GlobalAddressTable_Object((1,3,6,1,4,1,890,1,15,3,34,1,6))
if mibBuilder.loadTexts:zyxelIpv6GlobalAddressTable.setStatus(_A)
_ZyxelIpv6GlobalAddressEntry_Object=MibTableRow
zyxelIpv6GlobalAddressEntry=_ZyxelIpv6GlobalAddressEntry_Object((1,3,6,1,4,1,890,1,15,3,34,1,6,1))
zyxelIpv6GlobalAddressEntry.setIndexNames((0,_C,_I),(0,_C,_J),(0,_C,_K),(0,_C,_L),(0,_C,_M))
if mibBuilder.loadTexts:zyxelIpv6GlobalAddressEntry.setStatus(_A)
_ZyIpv6GlobalAddressIfIndex_Type=Integer32
_ZyIpv6GlobalAddressIfIndex_Object=MibTableColumn
zyIpv6GlobalAddressIfIndex=_ZyIpv6GlobalAddressIfIndex_Object((1,3,6,1,4,1,890,1,15,3,34,1,6,1,1),_ZyIpv6GlobalAddressIfIndex_Type())
zyIpv6GlobalAddressIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:zyIpv6GlobalAddressIfIndex.setStatus(_A)
_ZyIpv6GlobalAddressIpAddressType_Type=InetAddressType
_ZyIpv6GlobalAddressIpAddressType_Object=MibTableColumn
zyIpv6GlobalAddressIpAddressType=_ZyIpv6GlobalAddressIpAddressType_Object((1,3,6,1,4,1,890,1,15,3,34,1,6,1,2),_ZyIpv6GlobalAddressIpAddressType_Type())
zyIpv6GlobalAddressIpAddressType.setMaxAccess(_D)
if mibBuilder.loadTexts:zyIpv6GlobalAddressIpAddressType.setStatus(_A)
_ZyIpv6GlobalAddressIpAddress_Type=InetAddress
_ZyIpv6GlobalAddressIpAddress_Object=MibTableColumn
zyIpv6GlobalAddressIpAddress=_ZyIpv6GlobalAddressIpAddress_Object((1,3,6,1,4,1,890,1,15,3,34,1,6,1,3),_ZyIpv6GlobalAddressIpAddress_Type())
zyIpv6GlobalAddressIpAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:zyIpv6GlobalAddressIpAddress.setStatus(_A)
_ZyIpv6GlobalAddressPrefixLength_Type=Integer32
_ZyIpv6GlobalAddressPrefixLength_Object=MibTableColumn
zyIpv6GlobalAddressPrefixLength=_ZyIpv6GlobalAddressPrefixLength_Object((1,3,6,1,4,1,890,1,15,3,34,1,6,1,4),_ZyIpv6GlobalAddressPrefixLength_Type())
zyIpv6GlobalAddressPrefixLength.setMaxAccess(_D)
if mibBuilder.loadTexts:zyIpv6GlobalAddressPrefixLength.setStatus(_A)
_ZyIpv6GlobalAddressEUI64State_Type=EnabledStatus
_ZyIpv6GlobalAddressEUI64State_Object=MibTableColumn
zyIpv6GlobalAddressEUI64State=_ZyIpv6GlobalAddressEUI64State_Object((1,3,6,1,4,1,890,1,15,3,34,1,6,1,5),_ZyIpv6GlobalAddressEUI64State_Type())
zyIpv6GlobalAddressEUI64State.setMaxAccess(_D)
if mibBuilder.loadTexts:zyIpv6GlobalAddressEUI64State.setStatus(_A)
class _ZyIpv6GlobalAddressStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('preferred',1),('deprecated',2),('invalid',3),('inaccessible',4),('unknown',5),('tentative',6),('duplicate',7)))
_ZyIpv6GlobalAddressStatus_Type.__name__=_G
_ZyIpv6GlobalAddressStatus_Object=MibTableColumn
zyIpv6GlobalAddressStatus=_ZyIpv6GlobalAddressStatus_Object((1,3,6,1,4,1,890,1,15,3,34,1,6,1,6),_ZyIpv6GlobalAddressStatus_Type())
zyIpv6GlobalAddressStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:zyIpv6GlobalAddressStatus.setStatus(_A)
_ZyIpv6GlobalAddressRowStatus_Type=RowStatus
_ZyIpv6GlobalAddressRowStatus_Object=MibTableColumn
zyIpv6GlobalAddressRowStatus=_ZyIpv6GlobalAddressRowStatus_Object((1,3,6,1,4,1,890,1,15,3,34,1,6,1,7),_ZyIpv6GlobalAddressRowStatus_Type())
zyIpv6GlobalAddressRowStatus.setMaxAccess('read-create')
if mibBuilder.loadTexts:zyIpv6GlobalAddressRowStatus.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'zyxelIpv6':zyxelIpv6,'zyxelIpv6Setup':zyxelIpv6Setup,'zyIpv6HopLimit':zyIpv6HopLimit,'zyIpv6IcmpRateLimitErrorInterval':zyIpv6IcmpRateLimitErrorInterval,'zyIpv6IcmpRateLimitBucketSize':zyIpv6IcmpRateLimitBucketSize,'zyIpv6MaxNumberOfGlobalAddrresses':zyIpv6MaxNumberOfGlobalAddrresses,'zyxelIpv6Table':zyxelIpv6Table,'zyxelIpv6Entry':zyxelIpv6Entry,_H:zyIpv6IfIndex,'zyIpv6State':zyIpv6State,'zyIpv6AddressAutoConfigState':zyIpv6AddressAutoConfigState,'zyIpv6LinkLocalIpAddrressType':zyIpv6LinkLocalIpAddrressType,'zyIpv6LinkLocalIpAddrress':zyIpv6LinkLocalIpAddrress,'zyIpv6DefaultGatewayType':zyIpv6DefaultGatewayType,'zyIpv6DefaultGateway':zyIpv6DefaultGateway,'zyxelIpv6GlobalAddressTable':zyxelIpv6GlobalAddressTable,'zyxelIpv6GlobalAddressEntry':zyxelIpv6GlobalAddressEntry,_I:zyIpv6GlobalAddressIfIndex,_J:zyIpv6GlobalAddressIpAddressType,_K:zyIpv6GlobalAddressIpAddress,_L:zyIpv6GlobalAddressPrefixLength,_M:zyIpv6GlobalAddressEUI64State,'zyIpv6GlobalAddressStatus':zyIpv6GlobalAddressStatus,'zyIpv6GlobalAddressRowStatus':zyIpv6GlobalAddressRowStatus})