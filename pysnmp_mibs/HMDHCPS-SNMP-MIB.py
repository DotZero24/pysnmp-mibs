_P='hmDHCPServerCounterIfIndex'
_O='hmDHCPServerIfConfigIndex'
_N='hmDHCPServerLeaseIpAddress'
_M='hmDHCPServerLeasePoolIndex'
_L='hmDHCPServerPoolIndex'
_K='DisplayString'
_J='Unsigned32'
_I='disable'
_H='enable'
_G='read-write'
_F='OctetString'
_E='HMDHCPS-SNMP-MIB'
_D='Integer32'
_C='read-create'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_F,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hmConfiguration,=mibBuilder.importSymbols('HMPRIV-MGMT-SNMP-MIB','hmConfiguration')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_J,'iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_K,'MacAddress','PhysAddress','RowStatus','TextualConvention')
hmDhcps=ModuleIdentity((1,3,6,1,4,1,248,14,16))
if mibBuilder.loadTexts:hmDhcps.setRevisions(('2013-04-18 12:00','2011-12-20 12:00','2007-10-16 12:00'))
_HmDHCPServerGroup_ObjectIdentity=ObjectIdentity
hmDHCPServerGroup=_HmDHCPServerGroup_ObjectIdentity((1,3,6,1,4,1,248,14,16,1))
_HmDHCPServerConfigGroup_ObjectIdentity=ObjectIdentity
hmDHCPServerConfigGroup=_HmDHCPServerConfigGroup_ObjectIdentity((1,3,6,1,4,1,248,14,16,1,1))
class _HmDHCPServerMode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_HmDHCPServerMode_Type.__name__=_D
_HmDHCPServerMode_Object=MibScalar
hmDHCPServerMode=_HmDHCPServerMode_Object((1,3,6,1,4,1,248,14,16,1,1,1),_HmDHCPServerMode_Type())
hmDHCPServerMode.setMaxAccess(_G)
if mibBuilder.loadTexts:hmDHCPServerMode.setStatus(_A)
_HmDHCPServerMaxPoolEntries_Type=Unsigned32
_HmDHCPServerMaxPoolEntries_Object=MibScalar
hmDHCPServerMaxPoolEntries=_HmDHCPServerMaxPoolEntries_Object((1,3,6,1,4,1,248,14,16,1,1,2),_HmDHCPServerMaxPoolEntries_Type())
hmDHCPServerMaxPoolEntries.setMaxAccess(_B)
if mibBuilder.loadTexts:hmDHCPServerMaxPoolEntries.setStatus(_A)
_HmDHCPServerMaxLeaseEntries_Type=Unsigned32
_HmDHCPServerMaxLeaseEntries_Object=MibScalar
hmDHCPServerMaxLeaseEntries=_HmDHCPServerMaxLeaseEntries_Object((1,3,6,1,4,1,248,14,16,1,1,3),_HmDHCPServerMaxLeaseEntries_Type())
hmDHCPServerMaxLeaseEntries.setMaxAccess(_B)
if mibBuilder.loadTexts:hmDHCPServerMaxLeaseEntries.setStatus(_A)
class _HmDHCPServerAddrProbe_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_HmDHCPServerAddrProbe_Type.__name__=_D
_HmDHCPServerAddrProbe_Object=MibScalar
hmDHCPServerAddrProbe=_HmDHCPServerAddrProbe_Object((1,3,6,1,4,1,248,14,16,1,1,4),_HmDHCPServerAddrProbe_Type())
hmDHCPServerAddrProbe.setMaxAccess(_G)
if mibBuilder.loadTexts:hmDHCPServerAddrProbe.setStatus(_A)
_HmDHCPServerPoolTable_Object=MibTable
hmDHCPServerPoolTable=_HmDHCPServerPoolTable_Object((1,3,6,1,4,1,248,14,16,1,1,5))
if mibBuilder.loadTexts:hmDHCPServerPoolTable.setStatus(_A)
_HmDHCPServerPoolEntry_Object=MibTableRow
hmDHCPServerPoolEntry=_HmDHCPServerPoolEntry_Object((1,3,6,1,4,1,248,14,16,1,1,5,1))
hmDHCPServerPoolEntry.setIndexNames((0,_E,_L))
if mibBuilder.loadTexts:hmDHCPServerPoolEntry.setStatus(_A)
_HmDHCPServerPoolIndex_Type=Unsigned32
_HmDHCPServerPoolIndex_Object=MibTableColumn
hmDHCPServerPoolIndex=_HmDHCPServerPoolIndex_Object((1,3,6,1,4,1,248,14,16,1,1,5,1,1),_HmDHCPServerPoolIndex_Type())
hmDHCPServerPoolIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:hmDHCPServerPoolIndex.setStatus(_A)
_HmDHCPServerPoolStartIpAddress_Type=IpAddress
_HmDHCPServerPoolStartIpAddress_Object=MibTableColumn
hmDHCPServerPoolStartIpAddress=_HmDHCPServerPoolStartIpAddress_Object((1,3,6,1,4,1,248,14,16,1,1,5,1,2),_HmDHCPServerPoolStartIpAddress_Type())
hmDHCPServerPoolStartIpAddress.setMaxAccess(_G)
if mibBuilder.loadTexts:hmDHCPServerPoolStartIpAddress.setStatus(_A)
_HmDHCPServerPoolEndIpAddress_Type=IpAddress
_HmDHCPServerPoolEndIpAddress_Object=MibTableColumn
hmDHCPServerPoolEndIpAddress=_HmDHCPServerPoolEndIpAddress_Object((1,3,6,1,4,1,248,14,16,1,1,5,1,3),_HmDHCPServerPoolEndIpAddress_Type())
hmDHCPServerPoolEndIpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:hmDHCPServerPoolEndIpAddress.setStatus(_A)
class _HmDHCPServerPoolLeaseTime_Type(Unsigned32):defaultValue=86400
_HmDHCPServerPoolLeaseTime_Type.__name__=_J
_HmDHCPServerPoolLeaseTime_Object=MibTableColumn
hmDHCPServerPoolLeaseTime=_HmDHCPServerPoolLeaseTime_Object((1,3,6,1,4,1,248,14,16,1,1,5,1,4),_HmDHCPServerPoolLeaseTime_Type())
hmDHCPServerPoolLeaseTime.setMaxAccess(_C)
if mibBuilder.loadTexts:hmDHCPServerPoolLeaseTime.setStatus(_A)
class _HmDHCPServerPoolFlags_Type(Bits):namedValues=NamedValues(*(('interface',0),('mac',1),('gateway',2),('clientid',3),('remoteid',4),('circuitid',5),('dynamic',6),('vlanid',7)))
_HmDHCPServerPoolFlags_Type.__name__='Bits'
_HmDHCPServerPoolFlags_Object=MibTableColumn
hmDHCPServerPoolFlags=_HmDHCPServerPoolFlags_Object((1,3,6,1,4,1,248,14,16,1,1,5,1,5),_HmDHCPServerPoolFlags_Type())
hmDHCPServerPoolFlags.setMaxAccess(_C)
if mibBuilder.loadTexts:hmDHCPServerPoolFlags.setStatus(_A)
_HmDHCPServerPoolIfIndex_Type=Integer32
_HmDHCPServerPoolIfIndex_Object=MibTableColumn
hmDHCPServerPoolIfIndex=_HmDHCPServerPoolIfIndex_Object((1,3,6,1,4,1,248,14,16,1,1,5,1,6),_HmDHCPServerPoolIfIndex_Type())
hmDHCPServerPoolIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:hmDHCPServerPoolIfIndex.setStatus(_A)
_HmDHCPServerPoolMacAddress_Type=MacAddress
_HmDHCPServerPoolMacAddress_Object=MibTableColumn
hmDHCPServerPoolMacAddress=_HmDHCPServerPoolMacAddress_Object((1,3,6,1,4,1,248,14,16,1,1,5,1,7),_HmDHCPServerPoolMacAddress_Type())
hmDHCPServerPoolMacAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:hmDHCPServerPoolMacAddress.setStatus(_A)
_HmDHCPServerPoolGateway_Type=IpAddress
_HmDHCPServerPoolGateway_Object=MibTableColumn
hmDHCPServerPoolGateway=_HmDHCPServerPoolGateway_Object((1,3,6,1,4,1,248,14,16,1,1,5,1,8),_HmDHCPServerPoolGateway_Type())
hmDHCPServerPoolGateway.setMaxAccess(_C)
if mibBuilder.loadTexts:hmDHCPServerPoolGateway.setStatus(_A)
_HmDHCPServerPoolClientId_Type=OctetString
_HmDHCPServerPoolClientId_Object=MibTableColumn
hmDHCPServerPoolClientId=_HmDHCPServerPoolClientId_Object((1,3,6,1,4,1,248,14,16,1,1,5,1,9),_HmDHCPServerPoolClientId_Type())
hmDHCPServerPoolClientId.setMaxAccess(_C)
if mibBuilder.loadTexts:hmDHCPServerPoolClientId.setStatus(_A)
_HmDHCPServerPoolRemoteId_Type=OctetString
_HmDHCPServerPoolRemoteId_Object=MibTableColumn
hmDHCPServerPoolRemoteId=_HmDHCPServerPoolRemoteId_Object((1,3,6,1,4,1,248,14,16,1,1,5,1,10),_HmDHCPServerPoolRemoteId_Type())
hmDHCPServerPoolRemoteId.setMaxAccess(_C)
if mibBuilder.loadTexts:hmDHCPServerPoolRemoteId.setStatus(_A)
_HmDHCPServerPoolCircuitId_Type=OctetString
_HmDHCPServerPoolCircuitId_Object=MibTableColumn
hmDHCPServerPoolCircuitId=_HmDHCPServerPoolCircuitId_Object((1,3,6,1,4,1,248,14,16,1,1,5,1,11),_HmDHCPServerPoolCircuitId_Type())
hmDHCPServerPoolCircuitId.setMaxAccess(_C)
if mibBuilder.loadTexts:hmDHCPServerPoolCircuitId.setStatus(_A)
class _HmDHCPServerPoolHirschmannClient_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_HmDHCPServerPoolHirschmannClient_Type.__name__=_D
_HmDHCPServerPoolHirschmannClient_Object=MibTableColumn
hmDHCPServerPoolHirschmannClient=_HmDHCPServerPoolHirschmannClient_Object((1,3,6,1,4,1,248,14,16,1,1,5,1,12),_HmDHCPServerPoolHirschmannClient_Type())
hmDHCPServerPoolHirschmannClient.setMaxAccess(_C)
if mibBuilder.loadTexts:hmDHCPServerPoolHirschmannClient.setStatus(_A)
_HmDHCPServerPoolVlanId_Type=Integer32
_HmDHCPServerPoolVlanId_Object=MibTableColumn
hmDHCPServerPoolVlanId=_HmDHCPServerPoolVlanId_Object((1,3,6,1,4,1,248,14,16,1,1,5,1,13),_HmDHCPServerPoolVlanId_Type())
hmDHCPServerPoolVlanId.setMaxAccess(_C)
if mibBuilder.loadTexts:hmDHCPServerPoolVlanId.setStatus(_A)
class _HmDHCPServerPoolOptionConfFileName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,70))
_HmDHCPServerPoolOptionConfFileName_Type.__name__=_K
_HmDHCPServerPoolOptionConfFileName_Object=MibTableColumn
hmDHCPServerPoolOptionConfFileName=_HmDHCPServerPoolOptionConfFileName_Object((1,3,6,1,4,1,248,14,16,1,1,5,1,30),_HmDHCPServerPoolOptionConfFileName_Type())
hmDHCPServerPoolOptionConfFileName.setMaxAccess(_C)
if mibBuilder.loadTexts:hmDHCPServerPoolOptionConfFileName.setStatus(_A)
_HmDHCPServerPoolOptionGateway_Type=IpAddress
_HmDHCPServerPoolOptionGateway_Object=MibTableColumn
hmDHCPServerPoolOptionGateway=_HmDHCPServerPoolOptionGateway_Object((1,3,6,1,4,1,248,14,16,1,1,5,1,31),_HmDHCPServerPoolOptionGateway_Type())
hmDHCPServerPoolOptionGateway.setMaxAccess(_C)
if mibBuilder.loadTexts:hmDHCPServerPoolOptionGateway.setStatus(_A)
_HmDHCPServerPoolOptionNetmask_Type=IpAddress
_HmDHCPServerPoolOptionNetmask_Object=MibTableColumn
hmDHCPServerPoolOptionNetmask=_HmDHCPServerPoolOptionNetmask_Object((1,3,6,1,4,1,248,14,16,1,1,5,1,32),_HmDHCPServerPoolOptionNetmask_Type())
hmDHCPServerPoolOptionNetmask.setMaxAccess(_C)
if mibBuilder.loadTexts:hmDHCPServerPoolOptionNetmask.setStatus(_A)
_HmDHCPServerPoolOptionWINS_Type=IpAddress
_HmDHCPServerPoolOptionWINS_Object=MibTableColumn
hmDHCPServerPoolOptionWINS=_HmDHCPServerPoolOptionWINS_Object((1,3,6,1,4,1,248,14,16,1,1,5,1,33),_HmDHCPServerPoolOptionWINS_Type())
hmDHCPServerPoolOptionWINS.setMaxAccess(_C)
if mibBuilder.loadTexts:hmDHCPServerPoolOptionWINS.setStatus(_A)
_HmDHCPServerPoolOptionDNS_Type=IpAddress
_HmDHCPServerPoolOptionDNS_Object=MibTableColumn
hmDHCPServerPoolOptionDNS=_HmDHCPServerPoolOptionDNS_Object((1,3,6,1,4,1,248,14,16,1,1,5,1,34),_HmDHCPServerPoolOptionDNS_Type())
hmDHCPServerPoolOptionDNS.setMaxAccess(_C)
if mibBuilder.loadTexts:hmDHCPServerPoolOptionDNS.setStatus(_A)
_HmDHCPServerPoolOptionHostname_Type=DisplayString
_HmDHCPServerPoolOptionHostname_Object=MibTableColumn
hmDHCPServerPoolOptionHostname=_HmDHCPServerPoolOptionHostname_Object((1,3,6,1,4,1,248,14,16,1,1,5,1,35),_HmDHCPServerPoolOptionHostname_Type())
hmDHCPServerPoolOptionHostname.setMaxAccess(_C)
if mibBuilder.loadTexts:hmDHCPServerPoolOptionHostname.setStatus(_A)
class _HmDHCPServerPoolOptionVendor_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_HmDHCPServerPoolOptionVendor_Type.__name__=_F
_HmDHCPServerPoolOptionVendor_Object=MibTableColumn
hmDHCPServerPoolOptionVendor=_HmDHCPServerPoolOptionVendor_Object((1,3,6,1,4,1,248,14,16,1,1,5,1,36),_HmDHCPServerPoolOptionVendor_Type())
hmDHCPServerPoolOptionVendor.setMaxAccess(_C)
if mibBuilder.loadTexts:hmDHCPServerPoolOptionVendor.setStatus(_A)
_HmDHCPServerPoolErrorStatus_Type=Unsigned32
_HmDHCPServerPoolErrorStatus_Object=MibTableColumn
hmDHCPServerPoolErrorStatus=_HmDHCPServerPoolErrorStatus_Object((1,3,6,1,4,1,248,14,16,1,1,5,1,99),_HmDHCPServerPoolErrorStatus_Type())
hmDHCPServerPoolErrorStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hmDHCPServerPoolErrorStatus.setStatus(_A)
_HmDHCPServerPoolRowStatus_Type=RowStatus
_HmDHCPServerPoolRowStatus_Object=MibTableColumn
hmDHCPServerPoolRowStatus=_HmDHCPServerPoolRowStatus_Object((1,3,6,1,4,1,248,14,16,1,1,5,1,100),_HmDHCPServerPoolRowStatus_Type())
hmDHCPServerPoolRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hmDHCPServerPoolRowStatus.setStatus(_A)
_HmDHCPServerLeaseGroup_ObjectIdentity=ObjectIdentity
hmDHCPServerLeaseGroup=_HmDHCPServerLeaseGroup_ObjectIdentity((1,3,6,1,4,1,248,14,16,1,2))
_HmDHCPServerLeaseTable_Object=MibTable
hmDHCPServerLeaseTable=_HmDHCPServerLeaseTable_Object((1,3,6,1,4,1,248,14,16,1,2,1))
if mibBuilder.loadTexts:hmDHCPServerLeaseTable.setStatus(_A)
_HmDHCPServerLeaseEntry_Object=MibTableRow
hmDHCPServerLeaseEntry=_HmDHCPServerLeaseEntry_Object((1,3,6,1,4,1,248,14,16,1,2,1,1))
hmDHCPServerLeaseEntry.setIndexNames((0,_E,_M),(0,_E,_N))
if mibBuilder.loadTexts:hmDHCPServerLeaseEntry.setStatus(_A)
_HmDHCPServerLeasePoolIndex_Type=Unsigned32
_HmDHCPServerLeasePoolIndex_Object=MibTableColumn
hmDHCPServerLeasePoolIndex=_HmDHCPServerLeasePoolIndex_Object((1,3,6,1,4,1,248,14,16,1,2,1,1,1),_HmDHCPServerLeasePoolIndex_Type())
hmDHCPServerLeasePoolIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:hmDHCPServerLeasePoolIndex.setStatus(_A)
_HmDHCPServerLeaseIpAddress_Type=IpAddress
_HmDHCPServerLeaseIpAddress_Object=MibTableColumn
hmDHCPServerLeaseIpAddress=_HmDHCPServerLeaseIpAddress_Object((1,3,6,1,4,1,248,14,16,1,2,1,1,2),_HmDHCPServerLeaseIpAddress_Type())
hmDHCPServerLeaseIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:hmDHCPServerLeaseIpAddress.setStatus(_A)
class _HmDHCPServerLeaseState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('bootp',1),('offering',2),('requesting',3),('bound',4),('renewing',5),('rebinding',6),('declined',7),('released',8)))
_HmDHCPServerLeaseState_Type.__name__=_D
_HmDHCPServerLeaseState_Object=MibTableColumn
hmDHCPServerLeaseState=_HmDHCPServerLeaseState_Object((1,3,6,1,4,1,248,14,16,1,2,1,1,3),_HmDHCPServerLeaseState_Type())
hmDHCPServerLeaseState.setMaxAccess(_B)
if mibBuilder.loadTexts:hmDHCPServerLeaseState.setStatus(_A)
_HmDHCPServerLeaseTimeRemaining_Type=Unsigned32
_HmDHCPServerLeaseTimeRemaining_Object=MibTableColumn
hmDHCPServerLeaseTimeRemaining=_HmDHCPServerLeaseTimeRemaining_Object((1,3,6,1,4,1,248,14,16,1,2,1,1,4),_HmDHCPServerLeaseTimeRemaining_Type())
hmDHCPServerLeaseTimeRemaining.setMaxAccess(_B)
if mibBuilder.loadTexts:hmDHCPServerLeaseTimeRemaining.setStatus(_A)
_HmDHCPServerLeaseIfIndex_Type=Integer32
_HmDHCPServerLeaseIfIndex_Object=MibTableColumn
hmDHCPServerLeaseIfIndex=_HmDHCPServerLeaseIfIndex_Object((1,3,6,1,4,1,248,14,16,1,2,1,1,5),_HmDHCPServerLeaseIfIndex_Type())
hmDHCPServerLeaseIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:hmDHCPServerLeaseIfIndex.setStatus(_A)
_HmDHCPServerLeaseClientMacAddress_Type=MacAddress
_HmDHCPServerLeaseClientMacAddress_Object=MibTableColumn
hmDHCPServerLeaseClientMacAddress=_HmDHCPServerLeaseClientMacAddress_Object((1,3,6,1,4,1,248,14,16,1,2,1,1,6),_HmDHCPServerLeaseClientMacAddress_Type())
hmDHCPServerLeaseClientMacAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:hmDHCPServerLeaseClientMacAddress.setStatus(_A)
_HmDHCPServerLeaseGateway_Type=IpAddress
_HmDHCPServerLeaseGateway_Object=MibTableColumn
hmDHCPServerLeaseGateway=_HmDHCPServerLeaseGateway_Object((1,3,6,1,4,1,248,14,16,1,2,1,1,7),_HmDHCPServerLeaseGateway_Type())
hmDHCPServerLeaseGateway.setMaxAccess(_B)
if mibBuilder.loadTexts:hmDHCPServerLeaseGateway.setStatus(_A)
class _HmDHCPServerLeaseClientId_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_HmDHCPServerLeaseClientId_Type.__name__=_F
_HmDHCPServerLeaseClientId_Object=MibTableColumn
hmDHCPServerLeaseClientId=_HmDHCPServerLeaseClientId_Object((1,3,6,1,4,1,248,14,16,1,2,1,1,8),_HmDHCPServerLeaseClientId_Type())
hmDHCPServerLeaseClientId.setMaxAccess(_B)
if mibBuilder.loadTexts:hmDHCPServerLeaseClientId.setStatus(_A)
class _HmDHCPServerLeaseRemoteId_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_HmDHCPServerLeaseRemoteId_Type.__name__=_F
_HmDHCPServerLeaseRemoteId_Object=MibTableColumn
hmDHCPServerLeaseRemoteId=_HmDHCPServerLeaseRemoteId_Object((1,3,6,1,4,1,248,14,16,1,2,1,1,9),_HmDHCPServerLeaseRemoteId_Type())
hmDHCPServerLeaseRemoteId.setMaxAccess(_B)
if mibBuilder.loadTexts:hmDHCPServerLeaseRemoteId.setStatus(_A)
class _HmDHCPServerLeaseCircuitId_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_HmDHCPServerLeaseCircuitId_Type.__name__=_F
_HmDHCPServerLeaseCircuitId_Object=MibTableColumn
hmDHCPServerLeaseCircuitId=_HmDHCPServerLeaseCircuitId_Object((1,3,6,1,4,1,248,14,16,1,2,1,1,10),_HmDHCPServerLeaseCircuitId_Type())
hmDHCPServerLeaseCircuitId.setMaxAccess(_B)
if mibBuilder.loadTexts:hmDHCPServerLeaseCircuitId.setStatus(_A)
_HmDHCPServerLeaseStartTime_Type=Unsigned32
_HmDHCPServerLeaseStartTime_Object=MibTableColumn
hmDHCPServerLeaseStartTime=_HmDHCPServerLeaseStartTime_Object((1,3,6,1,4,1,248,14,16,1,2,1,1,11),_HmDHCPServerLeaseStartTime_Type())
hmDHCPServerLeaseStartTime.setMaxAccess(_B)
if mibBuilder.loadTexts:hmDHCPServerLeaseStartTime.setStatus(_A)
class _HmDHCPServerLeaseAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('other',1),('release',2)))
_HmDHCPServerLeaseAction_Type.__name__=_D
_HmDHCPServerLeaseAction_Object=MibTableColumn
hmDHCPServerLeaseAction=_HmDHCPServerLeaseAction_Object((1,3,6,1,4,1,248,14,16,1,2,1,1,12),_HmDHCPServerLeaseAction_Type())
hmDHCPServerLeaseAction.setMaxAccess(_G)
if mibBuilder.loadTexts:hmDHCPServerLeaseAction.setStatus(_A)
_HmDHCPServerLeaseVlanId_Type=Integer32
_HmDHCPServerLeaseVlanId_Object=MibTableColumn
hmDHCPServerLeaseVlanId=_HmDHCPServerLeaseVlanId_Object((1,3,6,1,4,1,248,14,16,1,2,1,1,13),_HmDHCPServerLeaseVlanId_Type())
hmDHCPServerLeaseVlanId.setMaxAccess(_B)
if mibBuilder.loadTexts:hmDHCPServerLeaseVlanId.setStatus(_A)
_HmDHCPServerInterfaceGroup_ObjectIdentity=ObjectIdentity
hmDHCPServerInterfaceGroup=_HmDHCPServerInterfaceGroup_ObjectIdentity((1,3,6,1,4,1,248,14,16,1,3))
_HmDHCPServerIfConfigTable_Object=MibTable
hmDHCPServerIfConfigTable=_HmDHCPServerIfConfigTable_Object((1,3,6,1,4,1,248,14,16,1,3,1))
if mibBuilder.loadTexts:hmDHCPServerIfConfigTable.setStatus(_A)
_HmDHCPServerIfConfigEntry_Object=MibTableRow
hmDHCPServerIfConfigEntry=_HmDHCPServerIfConfigEntry_Object((1,3,6,1,4,1,248,14,16,1,3,1,1))
hmDHCPServerIfConfigEntry.setIndexNames((0,_E,_O))
if mibBuilder.loadTexts:hmDHCPServerIfConfigEntry.setStatus(_A)
_HmDHCPServerIfConfigIndex_Type=Integer32
_HmDHCPServerIfConfigIndex_Object=MibTableColumn
hmDHCPServerIfConfigIndex=_HmDHCPServerIfConfigIndex_Object((1,3,6,1,4,1,248,14,16,1,3,1,1,1),_HmDHCPServerIfConfigIndex_Type())
hmDHCPServerIfConfigIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:hmDHCPServerIfConfigIndex.setStatus(_A)
class _HmDHCPServerIfConfigMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_HmDHCPServerIfConfigMode_Type.__name__=_D
_HmDHCPServerIfConfigMode_Object=MibTableColumn
hmDHCPServerIfConfigMode=_HmDHCPServerIfConfigMode_Object((1,3,6,1,4,1,248,14,16,1,3,1,1,2),_HmDHCPServerIfConfigMode_Type())
hmDHCPServerIfConfigMode.setMaxAccess(_G)
if mibBuilder.loadTexts:hmDHCPServerIfConfigMode.setStatus(_A)
_HmDHCPServerCounterGroup_ObjectIdentity=ObjectIdentity
hmDHCPServerCounterGroup=_HmDHCPServerCounterGroup_ObjectIdentity((1,3,6,1,4,1,248,14,16,1,4))
_HmDHCPServerCounterIfTable_Object=MibTable
hmDHCPServerCounterIfTable=_HmDHCPServerCounterIfTable_Object((1,3,6,1,4,1,248,14,16,1,4,2))
if mibBuilder.loadTexts:hmDHCPServerCounterIfTable.setStatus(_A)
_HmDHCPServerCounterIfEntry_Object=MibTableRow
hmDHCPServerCounterIfEntry=_HmDHCPServerCounterIfEntry_Object((1,3,6,1,4,1,248,14,16,1,4,2,1))
hmDHCPServerCounterIfEntry.setIndexNames((0,_E,_P))
if mibBuilder.loadTexts:hmDHCPServerCounterIfEntry.setStatus(_A)
class _HmDHCPServerCounterIfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,128))
_HmDHCPServerCounterIfIndex_Type.__name__=_D
_HmDHCPServerCounterIfIndex_Object=MibTableColumn
hmDHCPServerCounterIfIndex=_HmDHCPServerCounterIfIndex_Object((1,3,6,1,4,1,248,14,16,1,4,2,1,1),_HmDHCPServerCounterIfIndex_Type())
hmDHCPServerCounterIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:hmDHCPServerCounterIfIndex.setStatus(_A)
_HmDHCPServerCounterBootpRequests_Type=Counter32
_HmDHCPServerCounterBootpRequests_Object=MibTableColumn
hmDHCPServerCounterBootpRequests=_HmDHCPServerCounterBootpRequests_Object((1,3,6,1,4,1,248,14,16,1,4,2,1,2),_HmDHCPServerCounterBootpRequests_Type())
hmDHCPServerCounterBootpRequests.setMaxAccess(_B)
if mibBuilder.loadTexts:hmDHCPServerCounterBootpRequests.setStatus(_A)
_HmDHCPServerCounterBootpInvalids_Type=Counter32
_HmDHCPServerCounterBootpInvalids_Object=MibTableColumn
hmDHCPServerCounterBootpInvalids=_HmDHCPServerCounterBootpInvalids_Object((1,3,6,1,4,1,248,14,16,1,4,2,1,3),_HmDHCPServerCounterBootpInvalids_Type())
hmDHCPServerCounterBootpInvalids.setMaxAccess(_B)
if mibBuilder.loadTexts:hmDHCPServerCounterBootpInvalids.setStatus(_A)
_HmDHCPServerCounterBootpReplies_Type=Counter32
_HmDHCPServerCounterBootpReplies_Object=MibTableColumn
hmDHCPServerCounterBootpReplies=_HmDHCPServerCounterBootpReplies_Object((1,3,6,1,4,1,248,14,16,1,4,2,1,4),_HmDHCPServerCounterBootpReplies_Type())
hmDHCPServerCounterBootpReplies.setMaxAccess(_B)
if mibBuilder.loadTexts:hmDHCPServerCounterBootpReplies.setStatus(_A)
_HmDHCPServerCounterBootpDroppedUnknownClients_Type=Counter32
_HmDHCPServerCounterBootpDroppedUnknownClients_Object=MibTableColumn
hmDHCPServerCounterBootpDroppedUnknownClients=_HmDHCPServerCounterBootpDroppedUnknownClients_Object((1,3,6,1,4,1,248,14,16,1,4,2,1,5),_HmDHCPServerCounterBootpDroppedUnknownClients_Type())
hmDHCPServerCounterBootpDroppedUnknownClients.setMaxAccess(_B)
if mibBuilder.loadTexts:hmDHCPServerCounterBootpDroppedUnknownClients.setStatus(_A)
_HmDHCPServerCounterBootpDroppedNotServingSubnet_Type=Counter32
_HmDHCPServerCounterBootpDroppedNotServingSubnet_Object=MibTableColumn
hmDHCPServerCounterBootpDroppedNotServingSubnet=_HmDHCPServerCounterBootpDroppedNotServingSubnet_Object((1,3,6,1,4,1,248,14,16,1,4,2,1,6),_HmDHCPServerCounterBootpDroppedNotServingSubnet_Type())
hmDHCPServerCounterBootpDroppedNotServingSubnet.setMaxAccess(_B)
if mibBuilder.loadTexts:hmDHCPServerCounterBootpDroppedNotServingSubnet.setStatus(_A)
_HmDHCPServerCounterDhcpv4Discovers_Type=Counter32
_HmDHCPServerCounterDhcpv4Discovers_Object=MibTableColumn
hmDHCPServerCounterDhcpv4Discovers=_HmDHCPServerCounterDhcpv4Discovers_Object((1,3,6,1,4,1,248,14,16,1,4,2,1,20),_HmDHCPServerCounterDhcpv4Discovers_Type())
hmDHCPServerCounterDhcpv4Discovers.setMaxAccess(_B)
if mibBuilder.loadTexts:hmDHCPServerCounterDhcpv4Discovers.setStatus(_A)
_HmDHCPServerCounterDhcpv4Offers_Type=Counter32
_HmDHCPServerCounterDhcpv4Offers_Object=MibTableColumn
hmDHCPServerCounterDhcpv4Offers=_HmDHCPServerCounterDhcpv4Offers_Object((1,3,6,1,4,1,248,14,16,1,4,2,1,21),_HmDHCPServerCounterDhcpv4Offers_Type())
hmDHCPServerCounterDhcpv4Offers.setMaxAccess(_B)
if mibBuilder.loadTexts:hmDHCPServerCounterDhcpv4Offers.setStatus(_A)
_HmDHCPServerCounterDhcpv4Requests_Type=Counter32
_HmDHCPServerCounterDhcpv4Requests_Object=MibTableColumn
hmDHCPServerCounterDhcpv4Requests=_HmDHCPServerCounterDhcpv4Requests_Object((1,3,6,1,4,1,248,14,16,1,4,2,1,22),_HmDHCPServerCounterDhcpv4Requests_Type())
hmDHCPServerCounterDhcpv4Requests.setMaxAccess(_B)
if mibBuilder.loadTexts:hmDHCPServerCounterDhcpv4Requests.setStatus(_A)
_HmDHCPServerCounterDhcpv4Declines_Type=Counter32
_HmDHCPServerCounterDhcpv4Declines_Object=MibTableColumn
hmDHCPServerCounterDhcpv4Declines=_HmDHCPServerCounterDhcpv4Declines_Object((1,3,6,1,4,1,248,14,16,1,4,2,1,23),_HmDHCPServerCounterDhcpv4Declines_Type())
hmDHCPServerCounterDhcpv4Declines.setMaxAccess(_B)
if mibBuilder.loadTexts:hmDHCPServerCounterDhcpv4Declines.setStatus(_A)
_HmDHCPServerCounterDhcpv4Acks_Type=Counter32
_HmDHCPServerCounterDhcpv4Acks_Object=MibTableColumn
hmDHCPServerCounterDhcpv4Acks=_HmDHCPServerCounterDhcpv4Acks_Object((1,3,6,1,4,1,248,14,16,1,4,2,1,24),_HmDHCPServerCounterDhcpv4Acks_Type())
hmDHCPServerCounterDhcpv4Acks.setMaxAccess(_B)
if mibBuilder.loadTexts:hmDHCPServerCounterDhcpv4Acks.setStatus(_A)
_HmDHCPServerCounterDhcpv4Naks_Type=Counter32
_HmDHCPServerCounterDhcpv4Naks_Object=MibTableColumn
hmDHCPServerCounterDhcpv4Naks=_HmDHCPServerCounterDhcpv4Naks_Object((1,3,6,1,4,1,248,14,16,1,4,2,1,25),_HmDHCPServerCounterDhcpv4Naks_Type())
hmDHCPServerCounterDhcpv4Naks.setMaxAccess(_B)
if mibBuilder.loadTexts:hmDHCPServerCounterDhcpv4Naks.setStatus(_A)
_HmDHCPServerCounterDhcpv4Releases_Type=Counter32
_HmDHCPServerCounterDhcpv4Releases_Object=MibTableColumn
hmDHCPServerCounterDhcpv4Releases=_HmDHCPServerCounterDhcpv4Releases_Object((1,3,6,1,4,1,248,14,16,1,4,2,1,26),_HmDHCPServerCounterDhcpv4Releases_Type())
hmDHCPServerCounterDhcpv4Releases.setMaxAccess(_B)
if mibBuilder.loadTexts:hmDHCPServerCounterDhcpv4Releases.setStatus(_A)
_HmDHCPServerCounterDhcpv4Informs_Type=Counter32
_HmDHCPServerCounterDhcpv4Informs_Object=MibTableColumn
hmDHCPServerCounterDhcpv4Informs=_HmDHCPServerCounterDhcpv4Informs_Object((1,3,6,1,4,1,248,14,16,1,4,2,1,27),_HmDHCPServerCounterDhcpv4Informs_Type())
hmDHCPServerCounterDhcpv4Informs.setMaxAccess(_B)
if mibBuilder.loadTexts:hmDHCPServerCounterDhcpv4Informs.setStatus(_A)
_HmDHCPServerCounterDhcpv4ForcedRenews_Type=Counter32
_HmDHCPServerCounterDhcpv4ForcedRenews_Object=MibTableColumn
hmDHCPServerCounterDhcpv4ForcedRenews=_HmDHCPServerCounterDhcpv4ForcedRenews_Object((1,3,6,1,4,1,248,14,16,1,4,2,1,28),_HmDHCPServerCounterDhcpv4ForcedRenews_Type())
hmDHCPServerCounterDhcpv4ForcedRenews.setMaxAccess(_B)
if mibBuilder.loadTexts:hmDHCPServerCounterDhcpv4ForcedRenews.setStatus(_A)
_HmDHCPServerCounterDhcpv4Invalids_Type=Counter32
_HmDHCPServerCounterDhcpv4Invalids_Object=MibTableColumn
hmDHCPServerCounterDhcpv4Invalids=_HmDHCPServerCounterDhcpv4Invalids_Object((1,3,6,1,4,1,248,14,16,1,4,2,1,29),_HmDHCPServerCounterDhcpv4Invalids_Type())
hmDHCPServerCounterDhcpv4Invalids.setMaxAccess(_B)
if mibBuilder.loadTexts:hmDHCPServerCounterDhcpv4Invalids.setStatus(_A)
_HmDHCPServerCounterDhcpv4DroppedUnknownClient_Type=Counter32
_HmDHCPServerCounterDhcpv4DroppedUnknownClient_Object=MibTableColumn
hmDHCPServerCounterDhcpv4DroppedUnknownClient=_HmDHCPServerCounterDhcpv4DroppedUnknownClient_Object((1,3,6,1,4,1,248,14,16,1,4,2,1,30),_HmDHCPServerCounterDhcpv4DroppedUnknownClient_Type())
hmDHCPServerCounterDhcpv4DroppedUnknownClient.setMaxAccess(_B)
if mibBuilder.loadTexts:hmDHCPServerCounterDhcpv4DroppedUnknownClient.setStatus(_A)
_HmDHCPServerCounterDhcpv4DroppedNotServingSubnet_Type=Counter32
_HmDHCPServerCounterDhcpv4DroppedNotServingSubnet_Object=MibTableColumn
hmDHCPServerCounterDhcpv4DroppedNotServingSubnet=_HmDHCPServerCounterDhcpv4DroppedNotServingSubnet_Object((1,3,6,1,4,1,248,14,16,1,4,2,1,31),_HmDHCPServerCounterDhcpv4DroppedNotServingSubnet_Type())
hmDHCPServerCounterDhcpv4DroppedNotServingSubnet.setMaxAccess(_B)
if mibBuilder.loadTexts:hmDHCPServerCounterDhcpv4DroppedNotServingSubnet.setStatus(_A)
_HmDHCPServerCounterMiscOtherDhcpServer_Type=Counter32
_HmDHCPServerCounterMiscOtherDhcpServer_Object=MibTableColumn
hmDHCPServerCounterMiscOtherDhcpServer=_HmDHCPServerCounterMiscOtherDhcpServer_Object((1,3,6,1,4,1,248,14,16,1,4,2,1,40),_HmDHCPServerCounterMiscOtherDhcpServer_Type())
hmDHCPServerCounterMiscOtherDhcpServer.setMaxAccess(_B)
if mibBuilder.loadTexts:hmDHCPServerCounterMiscOtherDhcpServer.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'hmDhcps':hmDhcps,'hmDHCPServerGroup':hmDHCPServerGroup,'hmDHCPServerConfigGroup':hmDHCPServerConfigGroup,'hmDHCPServerMode':hmDHCPServerMode,'hmDHCPServerMaxPoolEntries':hmDHCPServerMaxPoolEntries,'hmDHCPServerMaxLeaseEntries':hmDHCPServerMaxLeaseEntries,'hmDHCPServerAddrProbe':hmDHCPServerAddrProbe,'hmDHCPServerPoolTable':hmDHCPServerPoolTable,'hmDHCPServerPoolEntry':hmDHCPServerPoolEntry,_L:hmDHCPServerPoolIndex,'hmDHCPServerPoolStartIpAddress':hmDHCPServerPoolStartIpAddress,'hmDHCPServerPoolEndIpAddress':hmDHCPServerPoolEndIpAddress,'hmDHCPServerPoolLeaseTime':hmDHCPServerPoolLeaseTime,'hmDHCPServerPoolFlags':hmDHCPServerPoolFlags,'hmDHCPServerPoolIfIndex':hmDHCPServerPoolIfIndex,'hmDHCPServerPoolMacAddress':hmDHCPServerPoolMacAddress,'hmDHCPServerPoolGateway':hmDHCPServerPoolGateway,'hmDHCPServerPoolClientId':hmDHCPServerPoolClientId,'hmDHCPServerPoolRemoteId':hmDHCPServerPoolRemoteId,'hmDHCPServerPoolCircuitId':hmDHCPServerPoolCircuitId,'hmDHCPServerPoolHirschmannClient':hmDHCPServerPoolHirschmannClient,'hmDHCPServerPoolVlanId':hmDHCPServerPoolVlanId,'hmDHCPServerPoolOptionConfFileName':hmDHCPServerPoolOptionConfFileName,'hmDHCPServerPoolOptionGateway':hmDHCPServerPoolOptionGateway,'hmDHCPServerPoolOptionNetmask':hmDHCPServerPoolOptionNetmask,'hmDHCPServerPoolOptionWINS':hmDHCPServerPoolOptionWINS,'hmDHCPServerPoolOptionDNS':hmDHCPServerPoolOptionDNS,'hmDHCPServerPoolOptionHostname':hmDHCPServerPoolOptionHostname,'hmDHCPServerPoolOptionVendor':hmDHCPServerPoolOptionVendor,'hmDHCPServerPoolErrorStatus':hmDHCPServerPoolErrorStatus,'hmDHCPServerPoolRowStatus':hmDHCPServerPoolRowStatus,'hmDHCPServerLeaseGroup':hmDHCPServerLeaseGroup,'hmDHCPServerLeaseTable':hmDHCPServerLeaseTable,'hmDHCPServerLeaseEntry':hmDHCPServerLeaseEntry,_M:hmDHCPServerLeasePoolIndex,_N:hmDHCPServerLeaseIpAddress,'hmDHCPServerLeaseState':hmDHCPServerLeaseState,'hmDHCPServerLeaseTimeRemaining':hmDHCPServerLeaseTimeRemaining,'hmDHCPServerLeaseIfIndex':hmDHCPServerLeaseIfIndex,'hmDHCPServerLeaseClientMacAddress':hmDHCPServerLeaseClientMacAddress,'hmDHCPServerLeaseGateway':hmDHCPServerLeaseGateway,'hmDHCPServerLeaseClientId':hmDHCPServerLeaseClientId,'hmDHCPServerLeaseRemoteId':hmDHCPServerLeaseRemoteId,'hmDHCPServerLeaseCircuitId':hmDHCPServerLeaseCircuitId,'hmDHCPServerLeaseStartTime':hmDHCPServerLeaseStartTime,'hmDHCPServerLeaseAction':hmDHCPServerLeaseAction,'hmDHCPServerLeaseVlanId':hmDHCPServerLeaseVlanId,'hmDHCPServerInterfaceGroup':hmDHCPServerInterfaceGroup,'hmDHCPServerIfConfigTable':hmDHCPServerIfConfigTable,'hmDHCPServerIfConfigEntry':hmDHCPServerIfConfigEntry,_O:hmDHCPServerIfConfigIndex,'hmDHCPServerIfConfigMode':hmDHCPServerIfConfigMode,'hmDHCPServerCounterGroup':hmDHCPServerCounterGroup,'hmDHCPServerCounterIfTable':hmDHCPServerCounterIfTable,'hmDHCPServerCounterIfEntry':hmDHCPServerCounterIfEntry,_P:hmDHCPServerCounterIfIndex,'hmDHCPServerCounterBootpRequests':hmDHCPServerCounterBootpRequests,'hmDHCPServerCounterBootpInvalids':hmDHCPServerCounterBootpInvalids,'hmDHCPServerCounterBootpReplies':hmDHCPServerCounterBootpReplies,'hmDHCPServerCounterBootpDroppedUnknownClients':hmDHCPServerCounterBootpDroppedUnknownClients,'hmDHCPServerCounterBootpDroppedNotServingSubnet':hmDHCPServerCounterBootpDroppedNotServingSubnet,'hmDHCPServerCounterDhcpv4Discovers':hmDHCPServerCounterDhcpv4Discovers,'hmDHCPServerCounterDhcpv4Offers':hmDHCPServerCounterDhcpv4Offers,'hmDHCPServerCounterDhcpv4Requests':hmDHCPServerCounterDhcpv4Requests,'hmDHCPServerCounterDhcpv4Declines':hmDHCPServerCounterDhcpv4Declines,'hmDHCPServerCounterDhcpv4Acks':hmDHCPServerCounterDhcpv4Acks,'hmDHCPServerCounterDhcpv4Naks':hmDHCPServerCounterDhcpv4Naks,'hmDHCPServerCounterDhcpv4Releases':hmDHCPServerCounterDhcpv4Releases,'hmDHCPServerCounterDhcpv4Informs':hmDHCPServerCounterDhcpv4Informs,'hmDHCPServerCounterDhcpv4ForcedRenews':hmDHCPServerCounterDhcpv4ForcedRenews,'hmDHCPServerCounterDhcpv4Invalids':hmDHCPServerCounterDhcpv4Invalids,'hmDHCPServerCounterDhcpv4DroppedUnknownClient':hmDHCPServerCounterDhcpv4DroppedUnknownClient,'hmDHCPServerCounterDhcpv4DroppedNotServingSubnet':hmDHCPServerCounterDhcpv4DroppedNotServingSubnet,'hmDHCPServerCounterMiscOtherDhcpServer':hmDHCPServerCounterMiscOtherDhcpServer})