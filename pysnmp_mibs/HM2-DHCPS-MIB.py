_O='hm2DHCPServerCounterIfIndex'
_N='hm2DHCPServerIfConfigIndex'
_M='hm2DHCPServerLeaseIpAddress'
_L='hm2DHCPServerLeasePoolIndex'
_K='hm2DHCPServerPoolIndex'
_J='DisplayString'
_I='Unsigned32'
_H='Integer32'
_G='OctetString'
_F='read-write'
_E='HmEnabledStatus'
_D='HM2-DHCPS-MIB'
_C='read-create'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_G,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
HmEnabledStatus,hm2ConfigurationMibs=mibBuilder.importSymbols('HM2-TC-MIB',_E,'hm2ConfigurationMibs')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_H,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_I,'iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_J,'MacAddress','PhysAddress','RowStatus','TextualConvention')
hm2DhcpsMib=ModuleIdentity((1,3,6,1,4,1,248,11,91))
if mibBuilder.loadTexts:hm2DhcpsMib.setRevisions(('2012-03-16 00:00',))
_Hm2DHCPServerMibNotifications_ObjectIdentity=ObjectIdentity
hm2DHCPServerMibNotifications=_Hm2DHCPServerMibNotifications_ObjectIdentity((1,3,6,1,4,1,248,11,91,0))
_Hm2DHCPServerMibObjects_ObjectIdentity=ObjectIdentity
hm2DHCPServerMibObjects=_Hm2DHCPServerMibObjects_ObjectIdentity((1,3,6,1,4,1,248,11,91,1))
_Hm2DHCPServerGroup_ObjectIdentity=ObjectIdentity
hm2DHCPServerGroup=_Hm2DHCPServerGroup_ObjectIdentity((1,3,6,1,4,1,248,11,91,1,1))
_Hm2DHCPServerConfigGroup_ObjectIdentity=ObjectIdentity
hm2DHCPServerConfigGroup=_Hm2DHCPServerConfigGroup_ObjectIdentity((1,3,6,1,4,1,248,11,91,1,1,1))
class _Hm2DHCPServerMode_Type(HmEnabledStatus):defaultValue=2
_Hm2DHCPServerMode_Type.__name__=_E
_Hm2DHCPServerMode_Object=MibScalar
hm2DHCPServerMode=_Hm2DHCPServerMode_Object((1,3,6,1,4,1,248,11,91,1,1,1,1),_Hm2DHCPServerMode_Type())
hm2DHCPServerMode.setMaxAccess(_F)
if mibBuilder.loadTexts:hm2DHCPServerMode.setStatus(_A)
_Hm2DHCPServerMaxPoolEntries_Type=Unsigned32
_Hm2DHCPServerMaxPoolEntries_Object=MibScalar
hm2DHCPServerMaxPoolEntries=_Hm2DHCPServerMaxPoolEntries_Object((1,3,6,1,4,1,248,11,91,1,1,1,2),_Hm2DHCPServerMaxPoolEntries_Type())
hm2DHCPServerMaxPoolEntries.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2DHCPServerMaxPoolEntries.setStatus(_A)
_Hm2DHCPServerMaxLeaseEntries_Type=Unsigned32
_Hm2DHCPServerMaxLeaseEntries_Object=MibScalar
hm2DHCPServerMaxLeaseEntries=_Hm2DHCPServerMaxLeaseEntries_Object((1,3,6,1,4,1,248,11,91,1,1,1,3),_Hm2DHCPServerMaxLeaseEntries_Type())
hm2DHCPServerMaxLeaseEntries.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2DHCPServerMaxLeaseEntries.setStatus(_A)
class _Hm2DHCPServerAddrProbe_Type(HmEnabledStatus):defaultValue=1
_Hm2DHCPServerAddrProbe_Type.__name__=_E
_Hm2DHCPServerAddrProbe_Object=MibScalar
hm2DHCPServerAddrProbe=_Hm2DHCPServerAddrProbe_Object((1,3,6,1,4,1,248,11,91,1,1,1,4),_Hm2DHCPServerAddrProbe_Type())
hm2DHCPServerAddrProbe.setMaxAccess(_F)
if mibBuilder.loadTexts:hm2DHCPServerAddrProbe.setStatus(_A)
_Hm2DHCPServerPoolTable_Object=MibTable
hm2DHCPServerPoolTable=_Hm2DHCPServerPoolTable_Object((1,3,6,1,4,1,248,11,91,1,1,1,5))
if mibBuilder.loadTexts:hm2DHCPServerPoolTable.setStatus(_A)
_Hm2DHCPServerPoolEntry_Object=MibTableRow
hm2DHCPServerPoolEntry=_Hm2DHCPServerPoolEntry_Object((1,3,6,1,4,1,248,11,91,1,1,1,5,1))
hm2DHCPServerPoolEntry.setIndexNames((0,_D,_K))
if mibBuilder.loadTexts:hm2DHCPServerPoolEntry.setStatus(_A)
class _Hm2DHCPServerPoolIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,128))
_Hm2DHCPServerPoolIndex_Type.__name__=_I
_Hm2DHCPServerPoolIndex_Object=MibTableColumn
hm2DHCPServerPoolIndex=_Hm2DHCPServerPoolIndex_Object((1,3,6,1,4,1,248,11,91,1,1,1,5,1,1),_Hm2DHCPServerPoolIndex_Type())
hm2DHCPServerPoolIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2DHCPServerPoolIndex.setStatus(_A)
_Hm2DHCPServerPoolStartIpAddress_Type=IpAddress
_Hm2DHCPServerPoolStartIpAddress_Object=MibTableColumn
hm2DHCPServerPoolStartIpAddress=_Hm2DHCPServerPoolStartIpAddress_Object((1,3,6,1,4,1,248,11,91,1,1,1,5,1,2),_Hm2DHCPServerPoolStartIpAddress_Type())
hm2DHCPServerPoolStartIpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2DHCPServerPoolStartIpAddress.setStatus(_A)
_Hm2DHCPServerPoolEndIpAddress_Type=IpAddress
_Hm2DHCPServerPoolEndIpAddress_Object=MibTableColumn
hm2DHCPServerPoolEndIpAddress=_Hm2DHCPServerPoolEndIpAddress_Object((1,3,6,1,4,1,248,11,91,1,1,1,5,1,3),_Hm2DHCPServerPoolEndIpAddress_Type())
hm2DHCPServerPoolEndIpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2DHCPServerPoolEndIpAddress.setStatus(_A)
class _Hm2DHCPServerPoolLeaseTime_Type(Unsigned32):defaultValue=86400
_Hm2DHCPServerPoolLeaseTime_Type.__name__=_I
_Hm2DHCPServerPoolLeaseTime_Object=MibTableColumn
hm2DHCPServerPoolLeaseTime=_Hm2DHCPServerPoolLeaseTime_Object((1,3,6,1,4,1,248,11,91,1,1,1,5,1,4),_Hm2DHCPServerPoolLeaseTime_Type())
hm2DHCPServerPoolLeaseTime.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2DHCPServerPoolLeaseTime.setStatus(_A)
class _Hm2DHCPServerPoolFlags_Type(Bits):namedValues=NamedValues(*(('interface',0),('mac',1),('gateway',2),('clientid',3),('remoteid',4),('circuitid',5),('dynamic',6),('vlanid',7)))
_Hm2DHCPServerPoolFlags_Type.__name__='Bits'
_Hm2DHCPServerPoolFlags_Object=MibTableColumn
hm2DHCPServerPoolFlags=_Hm2DHCPServerPoolFlags_Object((1,3,6,1,4,1,248,11,91,1,1,1,5,1,5),_Hm2DHCPServerPoolFlags_Type())
hm2DHCPServerPoolFlags.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2DHCPServerPoolFlags.setStatus(_A)
_Hm2DHCPServerPoolIfIndex_Type=Integer32
_Hm2DHCPServerPoolIfIndex_Object=MibTableColumn
hm2DHCPServerPoolIfIndex=_Hm2DHCPServerPoolIfIndex_Object((1,3,6,1,4,1,248,11,91,1,1,1,5,1,6),_Hm2DHCPServerPoolIfIndex_Type())
hm2DHCPServerPoolIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2DHCPServerPoolIfIndex.setStatus(_A)
_Hm2DHCPServerPoolMacAddress_Type=MacAddress
_Hm2DHCPServerPoolMacAddress_Object=MibTableColumn
hm2DHCPServerPoolMacAddress=_Hm2DHCPServerPoolMacAddress_Object((1,3,6,1,4,1,248,11,91,1,1,1,5,1,7),_Hm2DHCPServerPoolMacAddress_Type())
hm2DHCPServerPoolMacAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2DHCPServerPoolMacAddress.setStatus(_A)
_Hm2DHCPServerPoolGateway_Type=IpAddress
_Hm2DHCPServerPoolGateway_Object=MibTableColumn
hm2DHCPServerPoolGateway=_Hm2DHCPServerPoolGateway_Object((1,3,6,1,4,1,248,11,91,1,1,1,5,1,8),_Hm2DHCPServerPoolGateway_Type())
hm2DHCPServerPoolGateway.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2DHCPServerPoolGateway.setStatus(_A)
_Hm2DHCPServerPoolClientId_Type=OctetString
_Hm2DHCPServerPoolClientId_Object=MibTableColumn
hm2DHCPServerPoolClientId=_Hm2DHCPServerPoolClientId_Object((1,3,6,1,4,1,248,11,91,1,1,1,5,1,9),_Hm2DHCPServerPoolClientId_Type())
hm2DHCPServerPoolClientId.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2DHCPServerPoolClientId.setStatus(_A)
_Hm2DHCPServerPoolRemoteId_Type=OctetString
_Hm2DHCPServerPoolRemoteId_Object=MibTableColumn
hm2DHCPServerPoolRemoteId=_Hm2DHCPServerPoolRemoteId_Object((1,3,6,1,4,1,248,11,91,1,1,1,5,1,10),_Hm2DHCPServerPoolRemoteId_Type())
hm2DHCPServerPoolRemoteId.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2DHCPServerPoolRemoteId.setStatus(_A)
_Hm2DHCPServerPoolCircuitId_Type=OctetString
_Hm2DHCPServerPoolCircuitId_Object=MibTableColumn
hm2DHCPServerPoolCircuitId=_Hm2DHCPServerPoolCircuitId_Object((1,3,6,1,4,1,248,11,91,1,1,1,5,1,11),_Hm2DHCPServerPoolCircuitId_Type())
hm2DHCPServerPoolCircuitId.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2DHCPServerPoolCircuitId.setStatus(_A)
class _Hm2DHCPServerPoolHirschmannClient_Type(HmEnabledStatus):defaultValue=2
_Hm2DHCPServerPoolHirschmannClient_Type.__name__=_E
_Hm2DHCPServerPoolHirschmannClient_Object=MibTableColumn
hm2DHCPServerPoolHirschmannClient=_Hm2DHCPServerPoolHirschmannClient_Object((1,3,6,1,4,1,248,11,91,1,1,1,5,1,12),_Hm2DHCPServerPoolHirschmannClient_Type())
hm2DHCPServerPoolHirschmannClient.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2DHCPServerPoolHirschmannClient.setStatus(_A)
_Hm2DHCPServerPoolVlanId_Type=Integer32
_Hm2DHCPServerPoolVlanId_Object=MibTableColumn
hm2DHCPServerPoolVlanId=_Hm2DHCPServerPoolVlanId_Object((1,3,6,1,4,1,248,11,91,1,1,1,5,1,13),_Hm2DHCPServerPoolVlanId_Type())
hm2DHCPServerPoolVlanId.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2DHCPServerPoolVlanId.setStatus(_A)
class _Hm2DHCPServerPoolOptionConfFileName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,70))
_Hm2DHCPServerPoolOptionConfFileName_Type.__name__=_J
_Hm2DHCPServerPoolOptionConfFileName_Object=MibTableColumn
hm2DHCPServerPoolOptionConfFileName=_Hm2DHCPServerPoolOptionConfFileName_Object((1,3,6,1,4,1,248,11,91,1,1,1,5,1,30),_Hm2DHCPServerPoolOptionConfFileName_Type())
hm2DHCPServerPoolOptionConfFileName.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2DHCPServerPoolOptionConfFileName.setStatus(_A)
_Hm2DHCPServerPoolOptionGateway_Type=IpAddress
_Hm2DHCPServerPoolOptionGateway_Object=MibTableColumn
hm2DHCPServerPoolOptionGateway=_Hm2DHCPServerPoolOptionGateway_Object((1,3,6,1,4,1,248,11,91,1,1,1,5,1,31),_Hm2DHCPServerPoolOptionGateway_Type())
hm2DHCPServerPoolOptionGateway.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2DHCPServerPoolOptionGateway.setStatus(_A)
_Hm2DHCPServerPoolOptionNetmask_Type=IpAddress
_Hm2DHCPServerPoolOptionNetmask_Object=MibTableColumn
hm2DHCPServerPoolOptionNetmask=_Hm2DHCPServerPoolOptionNetmask_Object((1,3,6,1,4,1,248,11,91,1,1,1,5,1,32),_Hm2DHCPServerPoolOptionNetmask_Type())
hm2DHCPServerPoolOptionNetmask.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2DHCPServerPoolOptionNetmask.setStatus(_A)
_Hm2DHCPServerPoolOptionWINS_Type=IpAddress
_Hm2DHCPServerPoolOptionWINS_Object=MibTableColumn
hm2DHCPServerPoolOptionWINS=_Hm2DHCPServerPoolOptionWINS_Object((1,3,6,1,4,1,248,11,91,1,1,1,5,1,33),_Hm2DHCPServerPoolOptionWINS_Type())
hm2DHCPServerPoolOptionWINS.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2DHCPServerPoolOptionWINS.setStatus(_A)
_Hm2DHCPServerPoolOptionDNS_Type=IpAddress
_Hm2DHCPServerPoolOptionDNS_Object=MibTableColumn
hm2DHCPServerPoolOptionDNS=_Hm2DHCPServerPoolOptionDNS_Object((1,3,6,1,4,1,248,11,91,1,1,1,5,1,34),_Hm2DHCPServerPoolOptionDNS_Type())
hm2DHCPServerPoolOptionDNS.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2DHCPServerPoolOptionDNS.setStatus(_A)
class _Hm2DHCPServerPoolOptionHostname_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_Hm2DHCPServerPoolOptionHostname_Type.__name__=_J
_Hm2DHCPServerPoolOptionHostname_Object=MibTableColumn
hm2DHCPServerPoolOptionHostname=_Hm2DHCPServerPoolOptionHostname_Object((1,3,6,1,4,1,248,11,91,1,1,1,5,1,35),_Hm2DHCPServerPoolOptionHostname_Type())
hm2DHCPServerPoolOptionHostname.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2DHCPServerPoolOptionHostname.setStatus(_A)
class _Hm2DHCPServerPoolMethod_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('none',1),('config',2),('ttdp',3)))
_Hm2DHCPServerPoolMethod_Type.__name__=_H
_Hm2DHCPServerPoolMethod_Object=MibTableColumn
hm2DHCPServerPoolMethod=_Hm2DHCPServerPoolMethod_Object((1,3,6,1,4,1,248,11,91,1,1,1,5,1,36),_Hm2DHCPServerPoolMethod_Type())
hm2DHCPServerPoolMethod.setMaxAccess(_F)
if mibBuilder.loadTexts:hm2DHCPServerPoolMethod.setStatus(_A)
_Hm2DHCPServerPoolErrorStatus_Type=Unsigned32
_Hm2DHCPServerPoolErrorStatus_Object=MibTableColumn
hm2DHCPServerPoolErrorStatus=_Hm2DHCPServerPoolErrorStatus_Object((1,3,6,1,4,1,248,11,91,1,1,1,5,1,99),_Hm2DHCPServerPoolErrorStatus_Type())
hm2DHCPServerPoolErrorStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2DHCPServerPoolErrorStatus.setStatus(_A)
_Hm2DHCPServerPoolRowStatus_Type=RowStatus
_Hm2DHCPServerPoolRowStatus_Object=MibTableColumn
hm2DHCPServerPoolRowStatus=_Hm2DHCPServerPoolRowStatus_Object((1,3,6,1,4,1,248,11,91,1,1,1,5,1,100),_Hm2DHCPServerPoolRowStatus_Type())
hm2DHCPServerPoolRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2DHCPServerPoolRowStatus.setStatus(_A)
_Hm2DHCPServerLeaseGroup_ObjectIdentity=ObjectIdentity
hm2DHCPServerLeaseGroup=_Hm2DHCPServerLeaseGroup_ObjectIdentity((1,3,6,1,4,1,248,11,91,1,1,2))
_Hm2DHCPServerLeaseTable_Object=MibTable
hm2DHCPServerLeaseTable=_Hm2DHCPServerLeaseTable_Object((1,3,6,1,4,1,248,11,91,1,1,2,1))
if mibBuilder.loadTexts:hm2DHCPServerLeaseTable.setStatus(_A)
_Hm2DHCPServerLeaseEntry_Object=MibTableRow
hm2DHCPServerLeaseEntry=_Hm2DHCPServerLeaseEntry_Object((1,3,6,1,4,1,248,11,91,1,1,2,1,1))
hm2DHCPServerLeaseEntry.setIndexNames((0,_D,_L),(0,_D,_M))
if mibBuilder.loadTexts:hm2DHCPServerLeaseEntry.setStatus(_A)
class _Hm2DHCPServerLeasePoolIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,128))
_Hm2DHCPServerLeasePoolIndex_Type.__name__=_I
_Hm2DHCPServerLeasePoolIndex_Object=MibTableColumn
hm2DHCPServerLeasePoolIndex=_Hm2DHCPServerLeasePoolIndex_Object((1,3,6,1,4,1,248,11,91,1,1,2,1,1,1),_Hm2DHCPServerLeasePoolIndex_Type())
hm2DHCPServerLeasePoolIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2DHCPServerLeasePoolIndex.setStatus(_A)
_Hm2DHCPServerLeaseIpAddress_Type=IpAddress
_Hm2DHCPServerLeaseIpAddress_Object=MibTableColumn
hm2DHCPServerLeaseIpAddress=_Hm2DHCPServerLeaseIpAddress_Object((1,3,6,1,4,1,248,11,91,1,1,2,1,1,2),_Hm2DHCPServerLeaseIpAddress_Type())
hm2DHCPServerLeaseIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2DHCPServerLeaseIpAddress.setStatus(_A)
class _Hm2DHCPServerLeaseState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('bootp',1),('offering',2),('requesting',3),('bound',4),('renewing',5),('rebinding',6),('declined',7),('released',8)))
_Hm2DHCPServerLeaseState_Type.__name__=_H
_Hm2DHCPServerLeaseState_Object=MibTableColumn
hm2DHCPServerLeaseState=_Hm2DHCPServerLeaseState_Object((1,3,6,1,4,1,248,11,91,1,1,2,1,1,3),_Hm2DHCPServerLeaseState_Type())
hm2DHCPServerLeaseState.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2DHCPServerLeaseState.setStatus(_A)
_Hm2DHCPServerLeaseTimeRemaining_Type=Unsigned32
_Hm2DHCPServerLeaseTimeRemaining_Object=MibTableColumn
hm2DHCPServerLeaseTimeRemaining=_Hm2DHCPServerLeaseTimeRemaining_Object((1,3,6,1,4,1,248,11,91,1,1,2,1,1,4),_Hm2DHCPServerLeaseTimeRemaining_Type())
hm2DHCPServerLeaseTimeRemaining.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2DHCPServerLeaseTimeRemaining.setStatus(_A)
_Hm2DHCPServerLeaseIfIndex_Type=Integer32
_Hm2DHCPServerLeaseIfIndex_Object=MibTableColumn
hm2DHCPServerLeaseIfIndex=_Hm2DHCPServerLeaseIfIndex_Object((1,3,6,1,4,1,248,11,91,1,1,2,1,1,5),_Hm2DHCPServerLeaseIfIndex_Type())
hm2DHCPServerLeaseIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2DHCPServerLeaseIfIndex.setStatus(_A)
_Hm2DHCPServerLeaseClientMacAddress_Type=MacAddress
_Hm2DHCPServerLeaseClientMacAddress_Object=MibTableColumn
hm2DHCPServerLeaseClientMacAddress=_Hm2DHCPServerLeaseClientMacAddress_Object((1,3,6,1,4,1,248,11,91,1,1,2,1,1,6),_Hm2DHCPServerLeaseClientMacAddress_Type())
hm2DHCPServerLeaseClientMacAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2DHCPServerLeaseClientMacAddress.setStatus(_A)
_Hm2DHCPServerLeaseGateway_Type=IpAddress
_Hm2DHCPServerLeaseGateway_Object=MibTableColumn
hm2DHCPServerLeaseGateway=_Hm2DHCPServerLeaseGateway_Object((1,3,6,1,4,1,248,11,91,1,1,2,1,1,7),_Hm2DHCPServerLeaseGateway_Type())
hm2DHCPServerLeaseGateway.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2DHCPServerLeaseGateway.setStatus(_A)
class _Hm2DHCPServerLeaseClientId_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_Hm2DHCPServerLeaseClientId_Type.__name__=_G
_Hm2DHCPServerLeaseClientId_Object=MibTableColumn
hm2DHCPServerLeaseClientId=_Hm2DHCPServerLeaseClientId_Object((1,3,6,1,4,1,248,11,91,1,1,2,1,1,8),_Hm2DHCPServerLeaseClientId_Type())
hm2DHCPServerLeaseClientId.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2DHCPServerLeaseClientId.setStatus(_A)
class _Hm2DHCPServerLeaseRemoteId_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_Hm2DHCPServerLeaseRemoteId_Type.__name__=_G
_Hm2DHCPServerLeaseRemoteId_Object=MibTableColumn
hm2DHCPServerLeaseRemoteId=_Hm2DHCPServerLeaseRemoteId_Object((1,3,6,1,4,1,248,11,91,1,1,2,1,1,9),_Hm2DHCPServerLeaseRemoteId_Type())
hm2DHCPServerLeaseRemoteId.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2DHCPServerLeaseRemoteId.setStatus(_A)
class _Hm2DHCPServerLeaseCircuitId_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_Hm2DHCPServerLeaseCircuitId_Type.__name__=_G
_Hm2DHCPServerLeaseCircuitId_Object=MibTableColumn
hm2DHCPServerLeaseCircuitId=_Hm2DHCPServerLeaseCircuitId_Object((1,3,6,1,4,1,248,11,91,1,1,2,1,1,10),_Hm2DHCPServerLeaseCircuitId_Type())
hm2DHCPServerLeaseCircuitId.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2DHCPServerLeaseCircuitId.setStatus(_A)
_Hm2DHCPServerLeaseStartTime_Type=Unsigned32
_Hm2DHCPServerLeaseStartTime_Object=MibTableColumn
hm2DHCPServerLeaseStartTime=_Hm2DHCPServerLeaseStartTime_Object((1,3,6,1,4,1,248,11,91,1,1,2,1,1,11),_Hm2DHCPServerLeaseStartTime_Type())
hm2DHCPServerLeaseStartTime.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2DHCPServerLeaseStartTime.setStatus(_A)
class _Hm2DHCPServerLeaseAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('other',1),('release',2)))
_Hm2DHCPServerLeaseAction_Type.__name__=_H
_Hm2DHCPServerLeaseAction_Object=MibTableColumn
hm2DHCPServerLeaseAction=_Hm2DHCPServerLeaseAction_Object((1,3,6,1,4,1,248,11,91,1,1,2,1,1,12),_Hm2DHCPServerLeaseAction_Type())
hm2DHCPServerLeaseAction.setMaxAccess(_F)
if mibBuilder.loadTexts:hm2DHCPServerLeaseAction.setStatus(_A)
_Hm2DHCPServerLeaseVlanId_Type=Integer32
_Hm2DHCPServerLeaseVlanId_Object=MibTableColumn
hm2DHCPServerLeaseVlanId=_Hm2DHCPServerLeaseVlanId_Object((1,3,6,1,4,1,248,11,91,1,1,2,1,1,13),_Hm2DHCPServerLeaseVlanId_Type())
hm2DHCPServerLeaseVlanId.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2DHCPServerLeaseVlanId.setStatus(_A)
_Hm2DHCPServerInterfaceGroup_ObjectIdentity=ObjectIdentity
hm2DHCPServerInterfaceGroup=_Hm2DHCPServerInterfaceGroup_ObjectIdentity((1,3,6,1,4,1,248,11,91,1,1,3))
_Hm2DHCPServerIfConfigTable_Object=MibTable
hm2DHCPServerIfConfigTable=_Hm2DHCPServerIfConfigTable_Object((1,3,6,1,4,1,248,11,91,1,1,3,1))
if mibBuilder.loadTexts:hm2DHCPServerIfConfigTable.setStatus(_A)
_Hm2DHCPServerIfConfigEntry_Object=MibTableRow
hm2DHCPServerIfConfigEntry=_Hm2DHCPServerIfConfigEntry_Object((1,3,6,1,4,1,248,11,91,1,1,3,1,1))
hm2DHCPServerIfConfigEntry.setIndexNames((0,_D,_N))
if mibBuilder.loadTexts:hm2DHCPServerIfConfigEntry.setStatus(_A)
_Hm2DHCPServerIfConfigIndex_Type=InterfaceIndex
_Hm2DHCPServerIfConfigIndex_Object=MibTableColumn
hm2DHCPServerIfConfigIndex=_Hm2DHCPServerIfConfigIndex_Object((1,3,6,1,4,1,248,11,91,1,1,3,1,1,1),_Hm2DHCPServerIfConfigIndex_Type())
hm2DHCPServerIfConfigIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2DHCPServerIfConfigIndex.setStatus(_A)
class _Hm2DHCPServerIfConfigMode_Type(HmEnabledStatus):defaultValue=1
_Hm2DHCPServerIfConfigMode_Type.__name__=_E
_Hm2DHCPServerIfConfigMode_Object=MibTableColumn
hm2DHCPServerIfConfigMode=_Hm2DHCPServerIfConfigMode_Object((1,3,6,1,4,1,248,11,91,1,1,3,1,1,2),_Hm2DHCPServerIfConfigMode_Type())
hm2DHCPServerIfConfigMode.setMaxAccess(_F)
if mibBuilder.loadTexts:hm2DHCPServerIfConfigMode.setStatus(_A)
_Hm2DHCPServerCounterGroup_ObjectIdentity=ObjectIdentity
hm2DHCPServerCounterGroup=_Hm2DHCPServerCounterGroup_ObjectIdentity((1,3,6,1,4,1,248,11,91,1,1,4))
_Hm2DHCPServerCounterIfTable_Object=MibTable
hm2DHCPServerCounterIfTable=_Hm2DHCPServerCounterIfTable_Object((1,3,6,1,4,1,248,11,91,1,1,4,2))
if mibBuilder.loadTexts:hm2DHCPServerCounterIfTable.setStatus(_A)
_Hm2DHCPServerCounterIfEntry_Object=MibTableRow
hm2DHCPServerCounterIfEntry=_Hm2DHCPServerCounterIfEntry_Object((1,3,6,1,4,1,248,11,91,1,1,4,2,1))
hm2DHCPServerCounterIfEntry.setIndexNames((0,_D,_O))
if mibBuilder.loadTexts:hm2DHCPServerCounterIfEntry.setStatus(_A)
_Hm2DHCPServerCounterIfIndex_Type=InterfaceIndex
_Hm2DHCPServerCounterIfIndex_Object=MibTableColumn
hm2DHCPServerCounterIfIndex=_Hm2DHCPServerCounterIfIndex_Object((1,3,6,1,4,1,248,11,91,1,1,4,2,1,1),_Hm2DHCPServerCounterIfIndex_Type())
hm2DHCPServerCounterIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2DHCPServerCounterIfIndex.setStatus(_A)
_Hm2DHCPServerCounterBootpRequests_Type=Counter32
_Hm2DHCPServerCounterBootpRequests_Object=MibTableColumn
hm2DHCPServerCounterBootpRequests=_Hm2DHCPServerCounterBootpRequests_Object((1,3,6,1,4,1,248,11,91,1,1,4,2,1,2),_Hm2DHCPServerCounterBootpRequests_Type())
hm2DHCPServerCounterBootpRequests.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2DHCPServerCounterBootpRequests.setStatus(_A)
_Hm2DHCPServerCounterBootpInvalids_Type=Counter32
_Hm2DHCPServerCounterBootpInvalids_Object=MibTableColumn
hm2DHCPServerCounterBootpInvalids=_Hm2DHCPServerCounterBootpInvalids_Object((1,3,6,1,4,1,248,11,91,1,1,4,2,1,3),_Hm2DHCPServerCounterBootpInvalids_Type())
hm2DHCPServerCounterBootpInvalids.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2DHCPServerCounterBootpInvalids.setStatus(_A)
_Hm2DHCPServerCounterBootpReplies_Type=Counter32
_Hm2DHCPServerCounterBootpReplies_Object=MibTableColumn
hm2DHCPServerCounterBootpReplies=_Hm2DHCPServerCounterBootpReplies_Object((1,3,6,1,4,1,248,11,91,1,1,4,2,1,4),_Hm2DHCPServerCounterBootpReplies_Type())
hm2DHCPServerCounterBootpReplies.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2DHCPServerCounterBootpReplies.setStatus(_A)
_Hm2DHCPServerCounterBootpDroppedUnknownClients_Type=Counter32
_Hm2DHCPServerCounterBootpDroppedUnknownClients_Object=MibTableColumn
hm2DHCPServerCounterBootpDroppedUnknownClients=_Hm2DHCPServerCounterBootpDroppedUnknownClients_Object((1,3,6,1,4,1,248,11,91,1,1,4,2,1,5),_Hm2DHCPServerCounterBootpDroppedUnknownClients_Type())
hm2DHCPServerCounterBootpDroppedUnknownClients.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2DHCPServerCounterBootpDroppedUnknownClients.setStatus(_A)
_Hm2DHCPServerCounterBootpDroppedNotServingSubnet_Type=Counter32
_Hm2DHCPServerCounterBootpDroppedNotServingSubnet_Object=MibTableColumn
hm2DHCPServerCounterBootpDroppedNotServingSubnet=_Hm2DHCPServerCounterBootpDroppedNotServingSubnet_Object((1,3,6,1,4,1,248,11,91,1,1,4,2,1,6),_Hm2DHCPServerCounterBootpDroppedNotServingSubnet_Type())
hm2DHCPServerCounterBootpDroppedNotServingSubnet.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2DHCPServerCounterBootpDroppedNotServingSubnet.setStatus(_A)
_Hm2DHCPServerCounterDhcpv4Discovers_Type=Counter32
_Hm2DHCPServerCounterDhcpv4Discovers_Object=MibTableColumn
hm2DHCPServerCounterDhcpv4Discovers=_Hm2DHCPServerCounterDhcpv4Discovers_Object((1,3,6,1,4,1,248,11,91,1,1,4,2,1,20),_Hm2DHCPServerCounterDhcpv4Discovers_Type())
hm2DHCPServerCounterDhcpv4Discovers.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2DHCPServerCounterDhcpv4Discovers.setStatus(_A)
_Hm2DHCPServerCounterDhcpv4Offers_Type=Counter32
_Hm2DHCPServerCounterDhcpv4Offers_Object=MibTableColumn
hm2DHCPServerCounterDhcpv4Offers=_Hm2DHCPServerCounterDhcpv4Offers_Object((1,3,6,1,4,1,248,11,91,1,1,4,2,1,21),_Hm2DHCPServerCounterDhcpv4Offers_Type())
hm2DHCPServerCounterDhcpv4Offers.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2DHCPServerCounterDhcpv4Offers.setStatus(_A)
_Hm2DHCPServerCounterDhcpv4Requests_Type=Counter32
_Hm2DHCPServerCounterDhcpv4Requests_Object=MibTableColumn
hm2DHCPServerCounterDhcpv4Requests=_Hm2DHCPServerCounterDhcpv4Requests_Object((1,3,6,1,4,1,248,11,91,1,1,4,2,1,22),_Hm2DHCPServerCounterDhcpv4Requests_Type())
hm2DHCPServerCounterDhcpv4Requests.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2DHCPServerCounterDhcpv4Requests.setStatus(_A)
_Hm2DHCPServerCounterDhcpv4Declines_Type=Counter32
_Hm2DHCPServerCounterDhcpv4Declines_Object=MibTableColumn
hm2DHCPServerCounterDhcpv4Declines=_Hm2DHCPServerCounterDhcpv4Declines_Object((1,3,6,1,4,1,248,11,91,1,1,4,2,1,23),_Hm2DHCPServerCounterDhcpv4Declines_Type())
hm2DHCPServerCounterDhcpv4Declines.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2DHCPServerCounterDhcpv4Declines.setStatus(_A)
_Hm2DHCPServerCounterDhcpv4Acks_Type=Counter32
_Hm2DHCPServerCounterDhcpv4Acks_Object=MibTableColumn
hm2DHCPServerCounterDhcpv4Acks=_Hm2DHCPServerCounterDhcpv4Acks_Object((1,3,6,1,4,1,248,11,91,1,1,4,2,1,24),_Hm2DHCPServerCounterDhcpv4Acks_Type())
hm2DHCPServerCounterDhcpv4Acks.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2DHCPServerCounterDhcpv4Acks.setStatus(_A)
_Hm2DHCPServerCounterDhcpv4Naks_Type=Counter32
_Hm2DHCPServerCounterDhcpv4Naks_Object=MibTableColumn
hm2DHCPServerCounterDhcpv4Naks=_Hm2DHCPServerCounterDhcpv4Naks_Object((1,3,6,1,4,1,248,11,91,1,1,4,2,1,25),_Hm2DHCPServerCounterDhcpv4Naks_Type())
hm2DHCPServerCounterDhcpv4Naks.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2DHCPServerCounterDhcpv4Naks.setStatus(_A)
_Hm2DHCPServerCounterDhcpv4Releases_Type=Counter32
_Hm2DHCPServerCounterDhcpv4Releases_Object=MibTableColumn
hm2DHCPServerCounterDhcpv4Releases=_Hm2DHCPServerCounterDhcpv4Releases_Object((1,3,6,1,4,1,248,11,91,1,1,4,2,1,26),_Hm2DHCPServerCounterDhcpv4Releases_Type())
hm2DHCPServerCounterDhcpv4Releases.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2DHCPServerCounterDhcpv4Releases.setStatus(_A)
_Hm2DHCPServerCounterDhcpv4Informs_Type=Counter32
_Hm2DHCPServerCounterDhcpv4Informs_Object=MibTableColumn
hm2DHCPServerCounterDhcpv4Informs=_Hm2DHCPServerCounterDhcpv4Informs_Object((1,3,6,1,4,1,248,11,91,1,1,4,2,1,27),_Hm2DHCPServerCounterDhcpv4Informs_Type())
hm2DHCPServerCounterDhcpv4Informs.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2DHCPServerCounterDhcpv4Informs.setStatus(_A)
_Hm2DHCPServerCounterDhcpv4ForcedRenews_Type=Counter32
_Hm2DHCPServerCounterDhcpv4ForcedRenews_Object=MibTableColumn
hm2DHCPServerCounterDhcpv4ForcedRenews=_Hm2DHCPServerCounterDhcpv4ForcedRenews_Object((1,3,6,1,4,1,248,11,91,1,1,4,2,1,28),_Hm2DHCPServerCounterDhcpv4ForcedRenews_Type())
hm2DHCPServerCounterDhcpv4ForcedRenews.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2DHCPServerCounterDhcpv4ForcedRenews.setStatus(_A)
_Hm2DHCPServerCounterDhcpv4Invalids_Type=Counter32
_Hm2DHCPServerCounterDhcpv4Invalids_Object=MibTableColumn
hm2DHCPServerCounterDhcpv4Invalids=_Hm2DHCPServerCounterDhcpv4Invalids_Object((1,3,6,1,4,1,248,11,91,1,1,4,2,1,29),_Hm2DHCPServerCounterDhcpv4Invalids_Type())
hm2DHCPServerCounterDhcpv4Invalids.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2DHCPServerCounterDhcpv4Invalids.setStatus(_A)
_Hm2DHCPServerCounterDhcpv4DroppedUnknownClient_Type=Counter32
_Hm2DHCPServerCounterDhcpv4DroppedUnknownClient_Object=MibTableColumn
hm2DHCPServerCounterDhcpv4DroppedUnknownClient=_Hm2DHCPServerCounterDhcpv4DroppedUnknownClient_Object((1,3,6,1,4,1,248,11,91,1,1,4,2,1,30),_Hm2DHCPServerCounterDhcpv4DroppedUnknownClient_Type())
hm2DHCPServerCounterDhcpv4DroppedUnknownClient.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2DHCPServerCounterDhcpv4DroppedUnknownClient.setStatus(_A)
_Hm2DHCPServerCounterDhcpv4DroppedNotServingSubnet_Type=Counter32
_Hm2DHCPServerCounterDhcpv4DroppedNotServingSubnet_Object=MibTableColumn
hm2DHCPServerCounterDhcpv4DroppedNotServingSubnet=_Hm2DHCPServerCounterDhcpv4DroppedNotServingSubnet_Object((1,3,6,1,4,1,248,11,91,1,1,4,2,1,31),_Hm2DHCPServerCounterDhcpv4DroppedNotServingSubnet_Type())
hm2DHCPServerCounterDhcpv4DroppedNotServingSubnet.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2DHCPServerCounterDhcpv4DroppedNotServingSubnet.setStatus(_A)
_Hm2DHCPServerCounterMiscOtherDhcpServer_Type=Counter32
_Hm2DHCPServerCounterMiscOtherDhcpServer_Object=MibTableColumn
hm2DHCPServerCounterMiscOtherDhcpServer=_Hm2DHCPServerCounterMiscOtherDhcpServer_Object((1,3,6,1,4,1,248,11,91,1,1,4,2,1,40),_Hm2DHCPServerCounterMiscOtherDhcpServer_Type())
hm2DHCPServerCounterMiscOtherDhcpServer.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2DHCPServerCounterMiscOtherDhcpServer.setStatus(_A)
_Hm2DHCPServerSNMPExtensionGroup_ObjectIdentity=ObjectIdentity
hm2DHCPServerSNMPExtensionGroup=_Hm2DHCPServerSNMPExtensionGroup_ObjectIdentity((1,3,6,1,4,1,248,11,91,3))
_Hm2DHCPServerRowStatusInvalidConfigurationErrorReturn_ObjectIdentity=ObjectIdentity
hm2DHCPServerRowStatusInvalidConfigurationErrorReturn=_Hm2DHCPServerRowStatusInvalidConfigurationErrorReturn_ObjectIdentity((1,3,6,1,4,1,248,11,91,3,1))
if mibBuilder.loadTexts:hm2DHCPServerRowStatusInvalidConfigurationErrorReturn.setStatus(_A)
_Hm2DHCPServerConflictDHCPRrelayErrorReturn_ObjectIdentity=ObjectIdentity
hm2DHCPServerConflictDHCPRrelayErrorReturn=_Hm2DHCPServerConflictDHCPRrelayErrorReturn_ObjectIdentity((1,3,6,1,4,1,248,11,91,3,2))
if mibBuilder.loadTexts:hm2DHCPServerConflictDHCPRrelayErrorReturn.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'hm2DhcpsMib':hm2DhcpsMib,'hm2DHCPServerMibNotifications':hm2DHCPServerMibNotifications,'hm2DHCPServerMibObjects':hm2DHCPServerMibObjects,'hm2DHCPServerGroup':hm2DHCPServerGroup,'hm2DHCPServerConfigGroup':hm2DHCPServerConfigGroup,'hm2DHCPServerMode':hm2DHCPServerMode,'hm2DHCPServerMaxPoolEntries':hm2DHCPServerMaxPoolEntries,'hm2DHCPServerMaxLeaseEntries':hm2DHCPServerMaxLeaseEntries,'hm2DHCPServerAddrProbe':hm2DHCPServerAddrProbe,'hm2DHCPServerPoolTable':hm2DHCPServerPoolTable,'hm2DHCPServerPoolEntry':hm2DHCPServerPoolEntry,_K:hm2DHCPServerPoolIndex,'hm2DHCPServerPoolStartIpAddress':hm2DHCPServerPoolStartIpAddress,'hm2DHCPServerPoolEndIpAddress':hm2DHCPServerPoolEndIpAddress,'hm2DHCPServerPoolLeaseTime':hm2DHCPServerPoolLeaseTime,'hm2DHCPServerPoolFlags':hm2DHCPServerPoolFlags,'hm2DHCPServerPoolIfIndex':hm2DHCPServerPoolIfIndex,'hm2DHCPServerPoolMacAddress':hm2DHCPServerPoolMacAddress,'hm2DHCPServerPoolGateway':hm2DHCPServerPoolGateway,'hm2DHCPServerPoolClientId':hm2DHCPServerPoolClientId,'hm2DHCPServerPoolRemoteId':hm2DHCPServerPoolRemoteId,'hm2DHCPServerPoolCircuitId':hm2DHCPServerPoolCircuitId,'hm2DHCPServerPoolHirschmannClient':hm2DHCPServerPoolHirschmannClient,'hm2DHCPServerPoolVlanId':hm2DHCPServerPoolVlanId,'hm2DHCPServerPoolOptionConfFileName':hm2DHCPServerPoolOptionConfFileName,'hm2DHCPServerPoolOptionGateway':hm2DHCPServerPoolOptionGateway,'hm2DHCPServerPoolOptionNetmask':hm2DHCPServerPoolOptionNetmask,'hm2DHCPServerPoolOptionWINS':hm2DHCPServerPoolOptionWINS,'hm2DHCPServerPoolOptionDNS':hm2DHCPServerPoolOptionDNS,'hm2DHCPServerPoolOptionHostname':hm2DHCPServerPoolOptionHostname,'hm2DHCPServerPoolMethod':hm2DHCPServerPoolMethod,'hm2DHCPServerPoolErrorStatus':hm2DHCPServerPoolErrorStatus,'hm2DHCPServerPoolRowStatus':hm2DHCPServerPoolRowStatus,'hm2DHCPServerLeaseGroup':hm2DHCPServerLeaseGroup,'hm2DHCPServerLeaseTable':hm2DHCPServerLeaseTable,'hm2DHCPServerLeaseEntry':hm2DHCPServerLeaseEntry,_L:hm2DHCPServerLeasePoolIndex,_M:hm2DHCPServerLeaseIpAddress,'hm2DHCPServerLeaseState':hm2DHCPServerLeaseState,'hm2DHCPServerLeaseTimeRemaining':hm2DHCPServerLeaseTimeRemaining,'hm2DHCPServerLeaseIfIndex':hm2DHCPServerLeaseIfIndex,'hm2DHCPServerLeaseClientMacAddress':hm2DHCPServerLeaseClientMacAddress,'hm2DHCPServerLeaseGateway':hm2DHCPServerLeaseGateway,'hm2DHCPServerLeaseClientId':hm2DHCPServerLeaseClientId,'hm2DHCPServerLeaseRemoteId':hm2DHCPServerLeaseRemoteId,'hm2DHCPServerLeaseCircuitId':hm2DHCPServerLeaseCircuitId,'hm2DHCPServerLeaseStartTime':hm2DHCPServerLeaseStartTime,'hm2DHCPServerLeaseAction':hm2DHCPServerLeaseAction,'hm2DHCPServerLeaseVlanId':hm2DHCPServerLeaseVlanId,'hm2DHCPServerInterfaceGroup':hm2DHCPServerInterfaceGroup,'hm2DHCPServerIfConfigTable':hm2DHCPServerIfConfigTable,'hm2DHCPServerIfConfigEntry':hm2DHCPServerIfConfigEntry,_N:hm2DHCPServerIfConfigIndex,'hm2DHCPServerIfConfigMode':hm2DHCPServerIfConfigMode,'hm2DHCPServerCounterGroup':hm2DHCPServerCounterGroup,'hm2DHCPServerCounterIfTable':hm2DHCPServerCounterIfTable,'hm2DHCPServerCounterIfEntry':hm2DHCPServerCounterIfEntry,_O:hm2DHCPServerCounterIfIndex,'hm2DHCPServerCounterBootpRequests':hm2DHCPServerCounterBootpRequests,'hm2DHCPServerCounterBootpInvalids':hm2DHCPServerCounterBootpInvalids,'hm2DHCPServerCounterBootpReplies':hm2DHCPServerCounterBootpReplies,'hm2DHCPServerCounterBootpDroppedUnknownClients':hm2DHCPServerCounterBootpDroppedUnknownClients,'hm2DHCPServerCounterBootpDroppedNotServingSubnet':hm2DHCPServerCounterBootpDroppedNotServingSubnet,'hm2DHCPServerCounterDhcpv4Discovers':hm2DHCPServerCounterDhcpv4Discovers,'hm2DHCPServerCounterDhcpv4Offers':hm2DHCPServerCounterDhcpv4Offers,'hm2DHCPServerCounterDhcpv4Requests':hm2DHCPServerCounterDhcpv4Requests,'hm2DHCPServerCounterDhcpv4Declines':hm2DHCPServerCounterDhcpv4Declines,'hm2DHCPServerCounterDhcpv4Acks':hm2DHCPServerCounterDhcpv4Acks,'hm2DHCPServerCounterDhcpv4Naks':hm2DHCPServerCounterDhcpv4Naks,'hm2DHCPServerCounterDhcpv4Releases':hm2DHCPServerCounterDhcpv4Releases,'hm2DHCPServerCounterDhcpv4Informs':hm2DHCPServerCounterDhcpv4Informs,'hm2DHCPServerCounterDhcpv4ForcedRenews':hm2DHCPServerCounterDhcpv4ForcedRenews,'hm2DHCPServerCounterDhcpv4Invalids':hm2DHCPServerCounterDhcpv4Invalids,'hm2DHCPServerCounterDhcpv4DroppedUnknownClient':hm2DHCPServerCounterDhcpv4DroppedUnknownClient,'hm2DHCPServerCounterDhcpv4DroppedNotServingSubnet':hm2DHCPServerCounterDhcpv4DroppedNotServingSubnet,'hm2DHCPServerCounterMiscOtherDhcpServer':hm2DHCPServerCounterMiscOtherDhcpServer,'hm2DHCPServerSNMPExtensionGroup':hm2DHCPServerSNMPExtensionGroup,'hm2DHCPServerRowStatusInvalidConfigurationErrorReturn':hm2DHCPServerRowStatusInvalidConfigurationErrorReturn,'hm2DHCPServerConflictDHCPRrelayErrorReturn':hm2DHCPServerConflictDHCPRrelayErrorReturn})