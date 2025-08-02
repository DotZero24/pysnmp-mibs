_H='read-only'
_G='nnethernetId'
_F='NT-ENTERPRISE-DATA-TASMAN-MGMT-ETHERNET-MIB'
_E='DisplayString'
_D='TruthValue'
_C='Integer32'
_B='read-create'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ntEnterpriseDataTasmanInterfaces,=mibBuilder.importSymbols('NT-ENTERPRISE-DATA-MIB','ntEnterpriseDataTasmanInterfaces')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_E,'PhysAddress','RowStatus','TextualConvention',_D)
nnethernetMib=ModuleIdentity((1,3,6,1,4,1,562,73,1,1,2,4))
if mibBuilder.loadTexts:nnethernetMib.setRevisions(('1999-07-01 00:00',))
_NnethernetTable_Object=MibTable
nnethernetTable=_NnethernetTable_Object((1,3,6,1,4,1,562,73,1,1,2,4,1))
if mibBuilder.loadTexts:nnethernetTable.setStatus(_A)
_NnethernetTableEntry_Object=MibTableRow
nnethernetTableEntry=_NnethernetTableEntry_Object((1,3,6,1,4,1,562,73,1,1,2,4,1,1))
nnethernetTableEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:nnethernetTableEntry.setStatus(_A)
class _NnethernetId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_NnethernetId_Type.__name__=_C
_NnethernetId_Object=MibTableColumn
nnethernetId=_NnethernetId_Object((1,3,6,1,4,1,562,73,1,1,2,4,1,1,1),_NnethernetId_Type())
nnethernetId.setMaxAccess(_H)
if mibBuilder.loadTexts:nnethernetId.setStatus('deprecated')
class _NnethernetDescr_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,25))
_NnethernetDescr_Type.__name__=_E
_NnethernetDescr_Object=MibTableColumn
nnethernetDescr=_NnethernetDescr_Object((1,3,6,1,4,1,562,73,1,1,2,4,1,1,2),_NnethernetDescr_Type())
nnethernetDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:nnethernetDescr.setStatus(_A)
_NnethernetDhcpRelayServerAddr_Type=IpAddress
_NnethernetDhcpRelayServerAddr_Object=MibTableColumn
nnethernetDhcpRelayServerAddr=_NnethernetDhcpRelayServerAddr_Object((1,3,6,1,4,1,562,73,1,1,2,4,1,1,3),_NnethernetDhcpRelayServerAddr_Type())
nnethernetDhcpRelayServerAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:nnethernetDhcpRelayServerAddr.setStatus(_A)
_NnethernetDhcpRelayGatewayAddr_Type=IpAddress
_NnethernetDhcpRelayGatewayAddr_Object=MibTableColumn
nnethernetDhcpRelayGatewayAddr=_NnethernetDhcpRelayGatewayAddr_Object((1,3,6,1,4,1,562,73,1,1,2,4,1,1,4),_NnethernetDhcpRelayGatewayAddr_Type())
nnethernetDhcpRelayGatewayAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:nnethernetDhcpRelayGatewayAddr.setStatus(_A)
class _NnethernetFailOverEnable_Type(TruthValue):defaultValue=2
_NnethernetFailOverEnable_Type.__name__=_D
_NnethernetFailOverEnable_Object=MibTableColumn
nnethernetFailOverEnable=_NnethernetFailOverEnable_Object((1,3,6,1,4,1,562,73,1,1,2,4,1,1,5),_NnethernetFailOverEnable_Type())
nnethernetFailOverEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:nnethernetFailOverEnable.setStatus(_A)
class _NnethernetHoldDownTime_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(3,900))
_NnethernetHoldDownTime_Type.__name__=_C
_NnethernetHoldDownTime_Object=MibTableColumn
nnethernetHoldDownTime=_NnethernetHoldDownTime_Object((1,3,6,1,4,1,562,73,1,1,2,4,1,1,6),_NnethernetHoldDownTime_Type())
nnethernetHoldDownTime.setMaxAccess(_B)
if mibBuilder.loadTexts:nnethernetHoldDownTime.setStatus(_A)
class _NnethernetIcmpRedirectEnable_Type(TruthValue):defaultValue=2
_NnethernetIcmpRedirectEnable_Type.__name__=_D
_NnethernetIcmpRedirectEnable_Object=MibTableColumn
nnethernetIcmpRedirectEnable=_NnethernetIcmpRedirectEnable_Object((1,3,6,1,4,1,562,73,1,1,2,4,1,1,7),_NnethernetIcmpRedirectEnable_Type())
nnethernetIcmpRedirectEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:nnethernetIcmpRedirectEnable.setStatus(_A)
class _NnethernetIcmpUnreachableEnable_Type(TruthValue):defaultValue=2
_NnethernetIcmpUnreachableEnable_Type.__name__=_D
_NnethernetIcmpUnreachableEnable_Object=MibTableColumn
nnethernetIcmpUnreachableEnable=_NnethernetIcmpUnreachableEnable_Object((1,3,6,1,4,1,562,73,1,1,2,4,1,1,8),_NnethernetIcmpUnreachableEnable_Type())
nnethernetIcmpUnreachableEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:nnethernetIcmpUnreachableEnable.setStatus(_A)
_NnethernetIpAddr_Type=IpAddress
_NnethernetIpAddr_Object=MibTableColumn
nnethernetIpAddr=_NnethernetIpAddr_Object((1,3,6,1,4,1,562,73,1,1,2,4,1,1,9),_NnethernetIpAddr_Type())
nnethernetIpAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:nnethernetIpAddr.setStatus(_A)
_NnethernetSubnetMask_Type=IpAddress
_NnethernetSubnetMask_Object=MibTableColumn
nnethernetSubnetMask=_NnethernetSubnetMask_Object((1,3,6,1,4,1,562,73,1,1,2,4,1,1,10),_NnethernetSubnetMask_Type())
nnethernetSubnetMask.setMaxAccess(_B)
if mibBuilder.loadTexts:nnethernetSubnetMask.setStatus(_A)
class _NnethernetIpDirectedBroadcastEnable_Type(TruthValue):defaultValue=2
_NnethernetIpDirectedBroadcastEnable_Type.__name__=_D
_NnethernetIpDirectedBroadcastEnable_Object=MibTableColumn
nnethernetIpDirectedBroadcastEnable=_NnethernetIpDirectedBroadcastEnable_Object((1,3,6,1,4,1,562,73,1,1,2,4,1,1,11),_NnethernetIpDirectedBroadcastEnable_Type())
nnethernetIpDirectedBroadcastEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:nnethernetIpDirectedBroadcastEnable.setStatus(_A)
class _NnethernetIpMulticast_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('pass',1),('block',2),('ospfrip2',3)))
_NnethernetIpMulticast_Type.__name__=_C
_NnethernetIpMulticast_Object=MibTableColumn
nnethernetIpMulticast=_NnethernetIpMulticast_Object((1,3,6,1,4,1,562,73,1,1,2,4,1,1,12),_NnethernetIpMulticast_Type())
nnethernetIpMulticast.setMaxAccess(_B)
if mibBuilder.loadTexts:nnethernetIpMulticast.setStatus(_A)
class _NnethernetMtu_Type(Integer32):defaultValue=1500
_NnethernetMtu_Type.__name__=_C
_NnethernetMtu_Object=MibTableColumn
nnethernetMtu=_NnethernetMtu_Object((1,3,6,1,4,1,562,73,1,1,2,4,1,1,13),_NnethernetMtu_Type())
nnethernetMtu.setMaxAccess(_B)
if mibBuilder.loadTexts:nnethernetMtu.setStatus(_A)
class _NnethernetSpeed_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('speed-10MBPs',1),('speed-100MBPs',2),('speed-Auto',3)))
_NnethernetSpeed_Type.__name__=_C
_NnethernetSpeed_Object=MibTableColumn
nnethernetSpeed=_NnethernetSpeed_Object((1,3,6,1,4,1,562,73,1,1,2,4,1,1,14),_NnethernetSpeed_Type())
nnethernetSpeed.setMaxAccess(_B)
if mibBuilder.loadTexts:nnethernetSpeed.setStatus(_A)
class _NnethernetMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('half-duplex',1),('full-duplex',2)))
_NnethernetMode_Type.__name__=_C
_NnethernetMode_Object=MibTableColumn
nnethernetMode=_NnethernetMode_Object((1,3,6,1,4,1,562,73,1,1,2,4,1,1,15),_NnethernetMode_Type())
nnethernetMode.setMaxAccess(_B)
if mibBuilder.loadTexts:nnethernetMode.setStatus(_A)
class _NnethernetShutdownEnable_Type(TruthValue):defaultValue=2
_NnethernetShutdownEnable_Type.__name__=_D
_NnethernetShutdownEnable_Object=MibTableColumn
nnethernetShutdownEnable=_NnethernetShutdownEnable_Object((1,3,6,1,4,1,562,73,1,1,2,4,1,1,16),_NnethernetShutdownEnable_Type())
nnethernetShutdownEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:nnethernetShutdownEnable.setStatus(_A)
class _NnethernetVlanId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4098))
_NnethernetVlanId_Type.__name__=_C
_NnethernetVlanId_Object=MibTableColumn
nnethernetVlanId=_NnethernetVlanId_Object((1,3,6,1,4,1,562,73,1,1,2,4,1,1,17),_NnethernetVlanId_Type())
nnethernetVlanId.setMaxAccess(_B)
if mibBuilder.loadTexts:nnethernetVlanId.setStatus(_A)
_NnethernetRowStatus_Type=RowStatus
_NnethernetRowStatus_Object=MibTableColumn
nnethernetRowStatus=_NnethernetRowStatus_Object((1,3,6,1,4,1,562,73,1,1,2,4,1,1,18),_NnethernetRowStatus_Type())
nnethernetRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:nnethernetRowStatus.setStatus(_A)
_NnethernetDropPackets_Type=Counter32
_NnethernetDropPackets_Object=MibTableColumn
nnethernetDropPackets=_NnethernetDropPackets_Object((1,3,6,1,4,1,562,73,1,1,2,4,1,1,19),_NnethernetDropPackets_Type())
nnethernetDropPackets.setMaxAccess(_H)
if mibBuilder.loadTexts:nnethernetDropPackets.setStatus(_A)
mibBuilder.exportSymbols(_F,**{'nnethernetMib':nnethernetMib,'nnethernetTable':nnethernetTable,'nnethernetTableEntry':nnethernetTableEntry,_G:nnethernetId,'nnethernetDescr':nnethernetDescr,'nnethernetDhcpRelayServerAddr':nnethernetDhcpRelayServerAddr,'nnethernetDhcpRelayGatewayAddr':nnethernetDhcpRelayGatewayAddr,'nnethernetFailOverEnable':nnethernetFailOverEnable,'nnethernetHoldDownTime':nnethernetHoldDownTime,'nnethernetIcmpRedirectEnable':nnethernetIcmpRedirectEnable,'nnethernetIcmpUnreachableEnable':nnethernetIcmpUnreachableEnable,'nnethernetIpAddr':nnethernetIpAddr,'nnethernetSubnetMask':nnethernetSubnetMask,'nnethernetIpDirectedBroadcastEnable':nnethernetIpDirectedBroadcastEnable,'nnethernetIpMulticast':nnethernetIpMulticast,'nnethernetMtu':nnethernetMtu,'nnethernetSpeed':nnethernetSpeed,'nnethernetMode':nnethernetMode,'nnethernetShutdownEnable':nnethernetShutdownEnable,'nnethernetVlanId':nnethernetVlanId,'nnethernetRowStatus':nnethernetRowStatus,'nnethernetDropPackets':nnethernetDropPackets})