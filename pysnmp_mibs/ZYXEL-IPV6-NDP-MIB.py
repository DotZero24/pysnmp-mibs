_N='zyNdpNSTrackingNetAddress'
_M='zyNdpNSTrackingNetAddressType'
_L='zyNdpNSTrackingIfIndex'
_K='read-create'
_J='zyNdpPrefixPrefixLength'
_I='zyNdpPrefixPrefixIpAddress'
_H='zyNdpPrefixPrefixType'
_G='zyNdpPrefixIfIndex'
_F='zyNdpIfIndex'
_E='PhysAddress'
_D='not-accessible'
_C='read-write'
_B='ZYXEL-IPV6-NDP-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
EnabledStatus,=mibBuilder.importSymbols('P-BRIDGE-MIB','EnabledStatus')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString',_E,'RowStatus','TextualConvention')
esMgmt,=mibBuilder.importSymbols('ZYXEL-ES-SMI','esMgmt')
zyxelIpv6Ndp=ModuleIdentity((1,3,6,1,4,1,890,1,15,3,35))
_ZyxelNdpSetup_ObjectIdentity=ObjectIdentity
zyxelNdpSetup=_ZyxelNdpSetup_ObjectIdentity((1,3,6,1,4,1,890,1,15,3,35,1))
_ZyNdpMaxNumberOfPrefixes_Type=Integer32
_ZyNdpMaxNumberOfPrefixes_Object=MibScalar
zyNdpMaxNumberOfPrefixes=_ZyNdpMaxNumberOfPrefixes_Object((1,3,6,1,4,1,890,1,15,3,35,1,1),_ZyNdpMaxNumberOfPrefixes_Type())
zyNdpMaxNumberOfPrefixes.setMaxAccess('read-only')
if mibBuilder.loadTexts:zyNdpMaxNumberOfPrefixes.setStatus(_A)
_ZyxelNdpTable_Object=MibTable
zyxelNdpTable=_ZyxelNdpTable_Object((1,3,6,1,4,1,890,1,15,3,35,1,2))
if mibBuilder.loadTexts:zyxelNdpTable.setStatus(_A)
_ZyxelNdpEntry_Object=MibTableRow
zyxelNdpEntry=_ZyxelNdpEntry_Object((1,3,6,1,4,1,890,1,15,3,35,1,2,1))
zyxelNdpEntry.setIndexNames((0,_B,_F))
if mibBuilder.loadTexts:zyxelNdpEntry.setStatus(_A)
_ZyNdpIfIndex_Type=Integer32
_ZyNdpIfIndex_Object=MibTableColumn
zyNdpIfIndex=_ZyNdpIfIndex_Object((1,3,6,1,4,1,890,1,15,3,35,1,2,1,1),_ZyNdpIfIndex_Type())
zyNdpIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:zyNdpIfIndex.setStatus(_A)
_ZyNdpDadAttempts_Type=Integer32
_ZyNdpDadAttempts_Object=MibTableColumn
zyNdpDadAttempts=_ZyNdpDadAttempts_Object((1,3,6,1,4,1,890,1,15,3,35,1,2,1,2),_ZyNdpDadAttempts_Type())
zyNdpDadAttempts.setMaxAccess(_C)
if mibBuilder.loadTexts:zyNdpDadAttempts.setStatus(_A)
_ZyNdpNsInterval_Type=Integer32
_ZyNdpNsInterval_Object=MibTableColumn
zyNdpNsInterval=_ZyNdpNsInterval_Object((1,3,6,1,4,1,890,1,15,3,35,1,2,1,3),_ZyNdpNsInterval_Type())
zyNdpNsInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:zyNdpNsInterval.setStatus(_A)
_ZyNdpReachableTime_Type=Integer32
_ZyNdpReachableTime_Object=MibTableColumn
zyNdpReachableTime=_ZyNdpReachableTime_Object((1,3,6,1,4,1,890,1,15,3,35,1,2,1,4),_ZyNdpReachableTime_Type())
zyNdpReachableTime.setMaxAccess(_C)
if mibBuilder.loadTexts:zyNdpReachableTime.setStatus(_A)
_ZyxelNdpPrefixTable_Object=MibTable
zyxelNdpPrefixTable=_ZyxelNdpPrefixTable_Object((1,3,6,1,4,1,890,1,15,3,35,1,3))
if mibBuilder.loadTexts:zyxelNdpPrefixTable.setStatus(_A)
_ZyxelNdpPrefixEntry_Object=MibTableRow
zyxelNdpPrefixEntry=_ZyxelNdpPrefixEntry_Object((1,3,6,1,4,1,890,1,15,3,35,1,3,1))
zyxelNdpPrefixEntry.setIndexNames((0,_B,_G),(0,_B,_H),(0,_B,_I),(0,_B,_J))
if mibBuilder.loadTexts:zyxelNdpPrefixEntry.setStatus(_A)
_ZyNdpPrefixIfIndex_Type=Integer32
_ZyNdpPrefixIfIndex_Object=MibTableColumn
zyNdpPrefixIfIndex=_ZyNdpPrefixIfIndex_Object((1,3,6,1,4,1,890,1,15,3,35,1,3,1,1),_ZyNdpPrefixIfIndex_Type())
zyNdpPrefixIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:zyNdpPrefixIfIndex.setStatus(_A)
_ZyNdpPrefixPrefixType_Type=InetAddressType
_ZyNdpPrefixPrefixType_Object=MibTableColumn
zyNdpPrefixPrefixType=_ZyNdpPrefixPrefixType_Object((1,3,6,1,4,1,890,1,15,3,35,1,3,1,2),_ZyNdpPrefixPrefixType_Type())
zyNdpPrefixPrefixType.setMaxAccess(_D)
if mibBuilder.loadTexts:zyNdpPrefixPrefixType.setStatus(_A)
_ZyNdpPrefixPrefixIpAddress_Type=InetAddress
_ZyNdpPrefixPrefixIpAddress_Object=MibTableColumn
zyNdpPrefixPrefixIpAddress=_ZyNdpPrefixPrefixIpAddress_Object((1,3,6,1,4,1,890,1,15,3,35,1,3,1,3),_ZyNdpPrefixPrefixIpAddress_Type())
zyNdpPrefixPrefixIpAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:zyNdpPrefixPrefixIpAddress.setStatus(_A)
_ZyNdpPrefixPrefixLength_Type=Integer32
_ZyNdpPrefixPrefixLength_Object=MibTableColumn
zyNdpPrefixPrefixLength=_ZyNdpPrefixPrefixLength_Object((1,3,6,1,4,1,890,1,15,3,35,1,3,1,4),_ZyNdpPrefixPrefixLength_Type())
zyNdpPrefixPrefixLength.setMaxAccess(_D)
if mibBuilder.loadTexts:zyNdpPrefixPrefixLength.setStatus(_A)
_ZyNdpPrefixValidLifetime_Type=Unsigned32
_ZyNdpPrefixValidLifetime_Object=MibTableColumn
zyNdpPrefixValidLifetime=_ZyNdpPrefixValidLifetime_Object((1,3,6,1,4,1,890,1,15,3,35,1,3,1,5),_ZyNdpPrefixValidLifetime_Type())
zyNdpPrefixValidLifetime.setMaxAccess(_C)
if mibBuilder.loadTexts:zyNdpPrefixValidLifetime.setStatus(_A)
_ZyNdpPrefixPreferredLifetime_Type=Unsigned32
_ZyNdpPrefixPreferredLifetime_Object=MibTableColumn
zyNdpPrefixPreferredLifetime=_ZyNdpPrefixPreferredLifetime_Object((1,3,6,1,4,1,890,1,15,3,35,1,3,1,6),_ZyNdpPrefixPreferredLifetime_Type())
zyNdpPrefixPreferredLifetime.setMaxAccess(_C)
if mibBuilder.loadTexts:zyNdpPrefixPreferredLifetime.setStatus(_A)
_ZyNdpPrefixNoAutonomousFlagState_Type=EnabledStatus
_ZyNdpPrefixNoAutonomousFlagState_Object=MibTableColumn
zyNdpPrefixNoAutonomousFlagState=_ZyNdpPrefixNoAutonomousFlagState_Object((1,3,6,1,4,1,890,1,15,3,35,1,3,1,7),_ZyNdpPrefixNoAutonomousFlagState_Type())
zyNdpPrefixNoAutonomousFlagState.setMaxAccess(_C)
if mibBuilder.loadTexts:zyNdpPrefixNoAutonomousFlagState.setStatus(_A)
_ZyNdpPrefixNoOnLinkFlagState_Type=EnabledStatus
_ZyNdpPrefixNoOnLinkFlagState_Object=MibTableColumn
zyNdpPrefixNoOnLinkFlagState=_ZyNdpPrefixNoOnLinkFlagState_Object((1,3,6,1,4,1,890,1,15,3,35,1,3,1,8),_ZyNdpPrefixNoOnLinkFlagState_Type())
zyNdpPrefixNoOnLinkFlagState.setMaxAccess(_C)
if mibBuilder.loadTexts:zyNdpPrefixNoOnLinkFlagState.setStatus(_A)
_ZyNdpPrefixNoAdvertiseFlagState_Type=EnabledStatus
_ZyNdpPrefixNoAdvertiseFlagState_Object=MibTableColumn
zyNdpPrefixNoAdvertiseFlagState=_ZyNdpPrefixNoAdvertiseFlagState_Object((1,3,6,1,4,1,890,1,15,3,35,1,3,1,9),_ZyNdpPrefixNoAdvertiseFlagState_Type())
zyNdpPrefixNoAdvertiseFlagState.setMaxAccess(_C)
if mibBuilder.loadTexts:zyNdpPrefixNoAdvertiseFlagState.setStatus(_A)
_ZyNdpPrefixRowStatus_Type=RowStatus
_ZyNdpPrefixRowStatus_Object=MibTableColumn
zyNdpPrefixRowStatus=_ZyNdpPrefixRowStatus_Object((1,3,6,1,4,1,890,1,15,3,35,1,3,1,10),_ZyNdpPrefixRowStatus_Type())
zyNdpPrefixRowStatus.setMaxAccess(_K)
if mibBuilder.loadTexts:zyNdpPrefixRowStatus.setStatus(_A)
_ZyNdpNSTrackingAgingTime_Type=Integer32
_ZyNdpNSTrackingAgingTime_Object=MibScalar
zyNdpNSTrackingAgingTime=_ZyNdpNSTrackingAgingTime_Object((1,3,6,1,4,1,890,1,15,3,35,1,4),_ZyNdpNSTrackingAgingTime_Type())
zyNdpNSTrackingAgingTime.setMaxAccess(_C)
if mibBuilder.loadTexts:zyNdpNSTrackingAgingTime.setStatus(_A)
_ZyxelNdpStatus_ObjectIdentity=ObjectIdentity
zyxelNdpStatus=_ZyxelNdpStatus_ObjectIdentity((1,3,6,1,4,1,890,1,15,3,35,2))
_ZyxelNdpNSTrackingTable_Object=MibTable
zyxelNdpNSTrackingTable=_ZyxelNdpNSTrackingTable_Object((1,3,6,1,4,1,890,1,15,3,35,2,1))
if mibBuilder.loadTexts:zyxelNdpNSTrackingTable.setStatus(_A)
_ZyxelNdpNSTrackingEntry_Object=MibTableRow
zyxelNdpNSTrackingEntry=_ZyxelNdpNSTrackingEntry_Object((1,3,6,1,4,1,890,1,15,3,35,2,1,1))
zyxelNdpNSTrackingEntry.setIndexNames((0,_B,_L),(0,_B,_M),(0,_B,_N))
if mibBuilder.loadTexts:zyxelNdpNSTrackingEntry.setStatus(_A)
_ZyNdpNSTrackingIfIndex_Type=InterfaceIndex
_ZyNdpNSTrackingIfIndex_Object=MibTableColumn
zyNdpNSTrackingIfIndex=_ZyNdpNSTrackingIfIndex_Object((1,3,6,1,4,1,890,1,15,3,35,2,1,1,1),_ZyNdpNSTrackingIfIndex_Type())
zyNdpNSTrackingIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:zyNdpNSTrackingIfIndex.setStatus(_A)
_ZyNdpNSTrackingNetAddressType_Type=InetAddressType
_ZyNdpNSTrackingNetAddressType_Object=MibTableColumn
zyNdpNSTrackingNetAddressType=_ZyNdpNSTrackingNetAddressType_Object((1,3,6,1,4,1,890,1,15,3,35,2,1,1,2),_ZyNdpNSTrackingNetAddressType_Type())
zyNdpNSTrackingNetAddressType.setMaxAccess(_D)
if mibBuilder.loadTexts:zyNdpNSTrackingNetAddressType.setStatus(_A)
_ZyNdpNSTrackingNetAddress_Type=InetAddress
_ZyNdpNSTrackingNetAddress_Object=MibTableColumn
zyNdpNSTrackingNetAddress=_ZyNdpNSTrackingNetAddress_Object((1,3,6,1,4,1,890,1,15,3,35,2,1,1,3),_ZyNdpNSTrackingNetAddress_Type())
zyNdpNSTrackingNetAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:zyNdpNSTrackingNetAddress.setStatus(_A)
class _ZyNdpNSTrackingPhysAddress_Type(PhysAddress):subtypeSpec=PhysAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,65535))
_ZyNdpNSTrackingPhysAddress_Type.__name__=_E
_ZyNdpNSTrackingPhysAddress_Object=MibTableColumn
zyNdpNSTrackingPhysAddress=_ZyNdpNSTrackingPhysAddress_Object((1,3,6,1,4,1,890,1,15,3,35,2,1,1,4),_ZyNdpNSTrackingPhysAddress_Type())
zyNdpNSTrackingPhysAddress.setMaxAccess(_K)
if mibBuilder.loadTexts:zyNdpNSTrackingPhysAddress.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'zyxelIpv6Ndp':zyxelIpv6Ndp,'zyxelNdpSetup':zyxelNdpSetup,'zyNdpMaxNumberOfPrefixes':zyNdpMaxNumberOfPrefixes,'zyxelNdpTable':zyxelNdpTable,'zyxelNdpEntry':zyxelNdpEntry,_F:zyNdpIfIndex,'zyNdpDadAttempts':zyNdpDadAttempts,'zyNdpNsInterval':zyNdpNsInterval,'zyNdpReachableTime':zyNdpReachableTime,'zyxelNdpPrefixTable':zyxelNdpPrefixTable,'zyxelNdpPrefixEntry':zyxelNdpPrefixEntry,_G:zyNdpPrefixIfIndex,_H:zyNdpPrefixPrefixType,_I:zyNdpPrefixPrefixIpAddress,_J:zyNdpPrefixPrefixLength,'zyNdpPrefixValidLifetime':zyNdpPrefixValidLifetime,'zyNdpPrefixPreferredLifetime':zyNdpPrefixPreferredLifetime,'zyNdpPrefixNoAutonomousFlagState':zyNdpPrefixNoAutonomousFlagState,'zyNdpPrefixNoOnLinkFlagState':zyNdpPrefixNoOnLinkFlagState,'zyNdpPrefixNoAdvertiseFlagState':zyNdpPrefixNoAdvertiseFlagState,'zyNdpPrefixRowStatus':zyNdpPrefixRowStatus,'zyNdpNSTrackingAgingTime':zyNdpNSTrackingAgingTime,'zyxelNdpStatus':zyxelNdpStatus,'zyxelNdpNSTrackingTable':zyxelNdpNSTrackingTable,'zyxelNdpNSTrackingEntry':zyxelNdpNSTrackingEntry,_L:zyNdpNSTrackingIfIndex,_M:zyNdpNSTrackingNetAddressType,_N:zyNdpNSTrackingNetAddress,'zyNdpNSTrackingPhysAddress':zyNdpNSTrackingPhysAddress})