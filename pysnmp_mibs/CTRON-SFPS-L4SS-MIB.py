_c='sfpsL4CDRFlowIndexFlowID'
_b='sfpsL4CDRTermedFlowFlowID'
_a='sfpsL4CDRActiveFlowFlowID'
_Z='sfpsL4CPCallableDeviceDeviceID'
_Y='sfpsL4CPPortNum'
_X='sfpsL4CPIPRouteSubnet'
_W='sfpsL4CPIPRouteSubnetMask'
_V='sfpsL4CPNetAddrUserNetAddr'
_U='sfpsL4CPNetAddrUserProtocol'
_T='sfpsL4CPMACAddrSubDestIP'
_S='HexInteger'
_R='sfpsL4CPFlowPrimProtPort'
_Q='sfpsL4CPFlowSecProtPort'
_P='sfpsL4CPFlowPrimMatchAnyDyn'
_O='sfpsL4CPFlowSecMatchAnyDyn'
_N='sfpsL4CPFlowSubprotocol'
_M='sfpsL4CPFlowPrimL3Address'
_L='sfpsL4CPFlowSecL3Address'
_K='sfpsL4CPFlowCnxIndex'
_J='invalid'
_I='terminated'
_H='active'
_G='initialized'
_F='no'
_E='yes'
_D='CTRON-SFPS-L4SS-MIB'
_C='Integer32'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
switchSFPS,=mibBuilder.importSymbols('CTRON-SFPS-INCLUDE-MIB','switchSFPS')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
class HexInteger(Integer32):0
class SfpsAddress(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
_SfpsL4SS_ObjectIdentity=ObjectIdentity
sfpsL4SS=_SfpsL4SS_ObjectIdentity((1,3,6,1,4,1,52,4,2,4,2,6))
_SfpsL4CP_ObjectIdentity=ObjectIdentity
sfpsL4CP=_SfpsL4CP_ObjectIdentity((1,3,6,1,4,1,52,4,2,4,2,6,1))
_L4cpStats_ObjectIdentity=ObjectIdentity
l4cpStats=_L4cpStats_ObjectIdentity((1,3,6,1,4,1,52,4,2,4,2,6,1,1))
_L4cpConfig_ObjectIdentity=ObjectIdentity
l4cpConfig=_L4cpConfig_ObjectIdentity((1,3,6,1,4,1,52,4,2,4,2,6,1,2))
class _SfpsL4CPDisableTCPAckCheck_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_SfpsL4CPDisableTCPAckCheck_Type.__name__=_C
_SfpsL4CPDisableTCPAckCheck_Object=MibScalar
sfpsL4CPDisableTCPAckCheck=_SfpsL4CPDisableTCPAckCheck_Object((1,3,6,1,4,1,52,4,2,4,2,6,1,2,1),_SfpsL4CPDisableTCPAckCheck_Type())
sfpsL4CPDisableTCPAckCheck.setMaxAccess('read-write')
if mibBuilder.loadTexts:sfpsL4CPDisableTCPAckCheck.setStatus(_A)
_L4cpActions_ObjectIdentity=ObjectIdentity
l4cpActions=_L4cpActions_ObjectIdentity((1,3,6,1,4,1,52,4,2,4,2,6,1,3))
_SfpsL4CPFlowTable_Object=MibTable
sfpsL4CPFlowTable=_SfpsL4CPFlowTable_Object((1,3,6,1,4,1,52,4,2,4,2,6,1,4))
if mibBuilder.loadTexts:sfpsL4CPFlowTable.setStatus(_A)
_SfpsL4CPFlowEntry_Object=MibTableRow
sfpsL4CPFlowEntry=_SfpsL4CPFlowEntry_Object((1,3,6,1,4,1,52,4,2,4,2,6,1,4,1))
sfpsL4CPFlowEntry.setIndexNames((0,_D,_K),(0,_D,_L),(0,_D,_M),(0,_D,_N),(0,_D,_O),(0,_D,_P),(0,_D,_Q),(0,_D,_R))
if mibBuilder.loadTexts:sfpsL4CPFlowEntry.setStatus(_A)
class _SfpsL4CPFlowCnxIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_SfpsL4CPFlowCnxIndex_Type.__name__=_C
_SfpsL4CPFlowCnxIndex_Object=MibTableColumn
sfpsL4CPFlowCnxIndex=_SfpsL4CPFlowCnxIndex_Object((1,3,6,1,4,1,52,4,2,4,2,6,1,4,1,1),_SfpsL4CPFlowCnxIndex_Type())
sfpsL4CPFlowCnxIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsL4CPFlowCnxIndex.setStatus(_A)
_SfpsL4CPFlowSecL3Address_Type=DisplayString
_SfpsL4CPFlowSecL3Address_Object=MibTableColumn
sfpsL4CPFlowSecL3Address=_SfpsL4CPFlowSecL3Address_Object((1,3,6,1,4,1,52,4,2,4,2,6,1,4,1,2),_SfpsL4CPFlowSecL3Address_Type())
sfpsL4CPFlowSecL3Address.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsL4CPFlowSecL3Address.setStatus(_A)
_SfpsL4CPFlowPrimL3Address_Type=DisplayString
_SfpsL4CPFlowPrimL3Address_Object=MibTableColumn
sfpsL4CPFlowPrimL3Address=_SfpsL4CPFlowPrimL3Address_Object((1,3,6,1,4,1,52,4,2,4,2,6,1,4,1,3),_SfpsL4CPFlowPrimL3Address_Type())
sfpsL4CPFlowPrimL3Address.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsL4CPFlowPrimL3Address.setStatus(_A)
class _SfpsL4CPFlowSubprotocol_Type(HexInteger):subtypeSpec=HexInteger.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_SfpsL4CPFlowSubprotocol_Type.__name__=_S
_SfpsL4CPFlowSubprotocol_Object=MibTableColumn
sfpsL4CPFlowSubprotocol=_SfpsL4CPFlowSubprotocol_Object((1,3,6,1,4,1,52,4,2,4,2,6,1,4,1,4),_SfpsL4CPFlowSubprotocol_Type())
sfpsL4CPFlowSubprotocol.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsL4CPFlowSubprotocol.setStatus(_A)
class _SfpsL4CPFlowSecMatchAnyDyn_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_SfpsL4CPFlowSecMatchAnyDyn_Type.__name__=_C
_SfpsL4CPFlowSecMatchAnyDyn_Object=MibTableColumn
sfpsL4CPFlowSecMatchAnyDyn=_SfpsL4CPFlowSecMatchAnyDyn_Object((1,3,6,1,4,1,52,4,2,4,2,6,1,4,1,5),_SfpsL4CPFlowSecMatchAnyDyn_Type())
sfpsL4CPFlowSecMatchAnyDyn.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsL4CPFlowSecMatchAnyDyn.setStatus(_A)
class _SfpsL4CPFlowPrimMatchAnyDyn_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_SfpsL4CPFlowPrimMatchAnyDyn_Type.__name__=_C
_SfpsL4CPFlowPrimMatchAnyDyn_Object=MibTableColumn
sfpsL4CPFlowPrimMatchAnyDyn=_SfpsL4CPFlowPrimMatchAnyDyn_Object((1,3,6,1,4,1,52,4,2,4,2,6,1,4,1,6),_SfpsL4CPFlowPrimMatchAnyDyn_Type())
sfpsL4CPFlowPrimMatchAnyDyn.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsL4CPFlowPrimMatchAnyDyn.setStatus(_A)
class _SfpsL4CPFlowSecProtPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SfpsL4CPFlowSecProtPort_Type.__name__=_C
_SfpsL4CPFlowSecProtPort_Object=MibTableColumn
sfpsL4CPFlowSecProtPort=_SfpsL4CPFlowSecProtPort_Object((1,3,6,1,4,1,52,4,2,4,2,6,1,4,1,7),_SfpsL4CPFlowSecProtPort_Type())
sfpsL4CPFlowSecProtPort.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsL4CPFlowSecProtPort.setStatus(_A)
class _SfpsL4CPFlowPrimProtPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SfpsL4CPFlowPrimProtPort_Type.__name__=_C
_SfpsL4CPFlowPrimProtPort_Object=MibTableColumn
sfpsL4CPFlowPrimProtPort=_SfpsL4CPFlowPrimProtPort_Object((1,3,6,1,4,1,52,4,2,4,2,6,1,4,1,8),_SfpsL4CPFlowPrimProtPort_Type())
sfpsL4CPFlowPrimProtPort.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsL4CPFlowPrimProtPort.setStatus(_A)
class _SfpsL4CPFlowSecSubstApplies_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_SfpsL4CPFlowSecSubstApplies_Type.__name__=_C
_SfpsL4CPFlowSecSubstApplies_Object=MibTableColumn
sfpsL4CPFlowSecSubstApplies=_SfpsL4CPFlowSecSubstApplies_Object((1,3,6,1,4,1,52,4,2,4,2,6,1,4,1,9),_SfpsL4CPFlowSecSubstApplies_Type())
sfpsL4CPFlowSecSubstApplies.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsL4CPFlowSecSubstApplies.setStatus(_A)
class _SfpsL4CPFlowPrimSubstApplies_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_SfpsL4CPFlowPrimSubstApplies_Type.__name__=_C
_SfpsL4CPFlowPrimSubstApplies_Object=MibTableColumn
sfpsL4CPFlowPrimSubstApplies=_SfpsL4CPFlowPrimSubstApplies_Object((1,3,6,1,4,1,52,4,2,4,2,6,1,4,1,10),_SfpsL4CPFlowPrimSubstApplies_Type())
sfpsL4CPFlowPrimSubstApplies.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsL4CPFlowPrimSubstApplies.setStatus(_A)
_SfpsL4CPFlowSecInPkts_Type=Counter32
_SfpsL4CPFlowSecInPkts_Object=MibTableColumn
sfpsL4CPFlowSecInPkts=_SfpsL4CPFlowSecInPkts_Object((1,3,6,1,4,1,52,4,2,4,2,6,1,4,1,11),_SfpsL4CPFlowSecInPkts_Type())
sfpsL4CPFlowSecInPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsL4CPFlowSecInPkts.setStatus(_A)
_SfpsL4CPFlowSecInOctets_Type=Counter32
_SfpsL4CPFlowSecInOctets_Object=MibTableColumn
sfpsL4CPFlowSecInOctets=_SfpsL4CPFlowSecInOctets_Object((1,3,6,1,4,1,52,4,2,4,2,6,1,4,1,12),_SfpsL4CPFlowSecInOctets_Type())
sfpsL4CPFlowSecInOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsL4CPFlowSecInOctets.setStatus(_A)
_SfpsL4CPFlowPrimInPkts_Type=Counter32
_SfpsL4CPFlowPrimInPkts_Object=MibTableColumn
sfpsL4CPFlowPrimInPkts=_SfpsL4CPFlowPrimInPkts_Object((1,3,6,1,4,1,52,4,2,4,2,6,1,4,1,13),_SfpsL4CPFlowPrimInPkts_Type())
sfpsL4CPFlowPrimInPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsL4CPFlowPrimInPkts.setStatus(_A)
_SfpsL4CPFlowPrimInOctets_Type=Counter32
_SfpsL4CPFlowPrimInOctets_Object=MibTableColumn
sfpsL4CPFlowPrimInOctets=_SfpsL4CPFlowPrimInOctets_Object((1,3,6,1,4,1,52,4,2,4,2,6,1,4,1,14),_SfpsL4CPFlowPrimInOctets_Type())
sfpsL4CPFlowPrimInOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsL4CPFlowPrimInOctets.setStatus(_A)
_SfpsL4CPFlowFlowAge_Type=TimeTicks
_SfpsL4CPFlowFlowAge_Object=MibTableColumn
sfpsL4CPFlowFlowAge=_SfpsL4CPFlowFlowAge_Object((1,3,6,1,4,1,52,4,2,4,2,6,1,4,1,15),_SfpsL4CPFlowFlowAge_Type())
sfpsL4CPFlowFlowAge.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsL4CPFlowFlowAge.setStatus(_A)
_SfpsL4CPFlowFlowLastUse_Type=TimeTicks
_SfpsL4CPFlowFlowLastUse_Object=MibTableColumn
sfpsL4CPFlowFlowLastUse=_SfpsL4CPFlowFlowLastUse_Object((1,3,6,1,4,1,52,4,2,4,2,6,1,4,1,16),_SfpsL4CPFlowFlowLastUse_Type())
sfpsL4CPFlowFlowLastUse.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsL4CPFlowFlowLastUse.setStatus(_A)
_SfpsL4CPFlowID_Type=Integer32
_SfpsL4CPFlowID_Object=MibTableColumn
sfpsL4CPFlowID=_SfpsL4CPFlowID_Object((1,3,6,1,4,1,52,4,2,4,2,6,1,4,1,17),_SfpsL4CPFlowID_Type())
sfpsL4CPFlowID.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsL4CPFlowID.setStatus(_A)
_SfpsL4CPMACAddrSubTable_Object=MibTable
sfpsL4CPMACAddrSubTable=_SfpsL4CPMACAddrSubTable_Object((1,3,6,1,4,1,52,4,2,4,2,6,1,5))
if mibBuilder.loadTexts:sfpsL4CPMACAddrSubTable.setStatus(_A)
_SfpsL4CPMACAddrSubEntry_Object=MibTableRow
sfpsL4CPMACAddrSubEntry=_SfpsL4CPMACAddrSubEntry_Object((1,3,6,1,4,1,52,4,2,4,2,6,1,5,1))
sfpsL4CPMACAddrSubEntry.setIndexNames((0,_D,_T))
if mibBuilder.loadTexts:sfpsL4CPMACAddrSubEntry.setStatus(_A)
_SfpsL4CPMACAddrSubDestIP_Type=IpAddress
_SfpsL4CPMACAddrSubDestIP_Object=MibTableColumn
sfpsL4CPMACAddrSubDestIP=_SfpsL4CPMACAddrSubDestIP_Object((1,3,6,1,4,1,52,4,2,4,2,6,1,5,1,1),_SfpsL4CPMACAddrSubDestIP_Type())
sfpsL4CPMACAddrSubDestIP.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsL4CPMACAddrSubDestIP.setStatus(_A)
_SfpsL4CPMACAddrSubNextHopMAC_Type=PhysAddress
_SfpsL4CPMACAddrSubNextHopMAC_Object=MibTableColumn
sfpsL4CPMACAddrSubNextHopMAC=_SfpsL4CPMACAddrSubNextHopMAC_Object((1,3,6,1,4,1,52,4,2,4,2,6,1,5,1,2),_SfpsL4CPMACAddrSubNextHopMAC_Type())
sfpsL4CPMACAddrSubNextHopMAC.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsL4CPMACAddrSubNextHopMAC.setStatus(_A)
class _SfpsL4CPMACAddrSubRefCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_SfpsL4CPMACAddrSubRefCount_Type.__name__=_C
_SfpsL4CPMACAddrSubRefCount_Object=MibTableColumn
sfpsL4CPMACAddrSubRefCount=_SfpsL4CPMACAddrSubRefCount_Object((1,3,6,1,4,1,52,4,2,4,2,6,1,5,1,3),_SfpsL4CPMACAddrSubRefCount_Type())
sfpsL4CPMACAddrSubRefCount.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsL4CPMACAddrSubRefCount.setStatus(_A)
_SfpsL4CPNetAddrUserTable_Object=MibTable
sfpsL4CPNetAddrUserTable=_SfpsL4CPNetAddrUserTable_Object((1,3,6,1,4,1,52,4,2,4,2,6,1,7))
if mibBuilder.loadTexts:sfpsL4CPNetAddrUserTable.setStatus(_A)
_SfpsL4CPNetAddrUserEntry_Object=MibTableRow
sfpsL4CPNetAddrUserEntry=_SfpsL4CPNetAddrUserEntry_Object((1,3,6,1,4,1,52,4,2,4,2,6,1,7,1))
sfpsL4CPNetAddrUserEntry.setIndexNames((0,_D,_U),(0,_D,_V))
if mibBuilder.loadTexts:sfpsL4CPNetAddrUserEntry.setStatus(_A)
class _SfpsL4CPNetAddrUserProtocol_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_SfpsL4CPNetAddrUserProtocol_Type.__name__=_C
_SfpsL4CPNetAddrUserProtocol_Object=MibTableColumn
sfpsL4CPNetAddrUserProtocol=_SfpsL4CPNetAddrUserProtocol_Object((1,3,6,1,4,1,52,4,2,4,2,6,1,7,1,1),_SfpsL4CPNetAddrUserProtocol_Type())
sfpsL4CPNetAddrUserProtocol.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsL4CPNetAddrUserProtocol.setStatus(_A)
_SfpsL4CPNetAddrUserNetAddr_Type=DisplayString
_SfpsL4CPNetAddrUserNetAddr_Object=MibTableColumn
sfpsL4CPNetAddrUserNetAddr=_SfpsL4CPNetAddrUserNetAddr_Object((1,3,6,1,4,1,52,4,2,4,2,6,1,7,1,2),_SfpsL4CPNetAddrUserNetAddr_Type())
sfpsL4CPNetAddrUserNetAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsL4CPNetAddrUserNetAddr.setStatus(_A)
_SfpsL4CPNetAddrUserLoginID_Type=Integer32
_SfpsL4CPNetAddrUserLoginID_Object=MibTableColumn
sfpsL4CPNetAddrUserLoginID=_SfpsL4CPNetAddrUserLoginID_Object((1,3,6,1,4,1,52,4,2,4,2,6,1,7,1,3),_SfpsL4CPNetAddrUserLoginID_Type())
sfpsL4CPNetAddrUserLoginID.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsL4CPNetAddrUserLoginID.setStatus(_A)
_SfpsL4CPNetAddrUserUserID_Type=Integer32
_SfpsL4CPNetAddrUserUserID_Object=MibTableColumn
sfpsL4CPNetAddrUserUserID=_SfpsL4CPNetAddrUserUserID_Object((1,3,6,1,4,1,52,4,2,4,2,6,1,7,1,4),_SfpsL4CPNetAddrUserUserID_Type())
sfpsL4CPNetAddrUserUserID.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsL4CPNetAddrUserUserID.setStatus(_A)
_SfpsL4CPNetAddrUserUserName_Type=DisplayString
_SfpsL4CPNetAddrUserUserName_Object=MibTableColumn
sfpsL4CPNetAddrUserUserName=_SfpsL4CPNetAddrUserUserName_Object((1,3,6,1,4,1,52,4,2,4,2,6,1,7,1,5),_SfpsL4CPNetAddrUserUserName_Type())
sfpsL4CPNetAddrUserUserName.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsL4CPNetAddrUserUserName.setStatus(_A)
_SfpsL4CPIPRouteTable_Object=MibTable
sfpsL4CPIPRouteTable=_SfpsL4CPIPRouteTable_Object((1,3,6,1,4,1,52,4,2,4,2,6,1,8))
if mibBuilder.loadTexts:sfpsL4CPIPRouteTable.setStatus(_A)
_SfpsL4CPIPRouteEntry_Object=MibTableRow
sfpsL4CPIPRouteEntry=_SfpsL4CPIPRouteEntry_Object((1,3,6,1,4,1,52,4,2,4,2,6,1,8,1))
sfpsL4CPIPRouteEntry.setIndexNames((0,_D,_W),(0,_D,_X))
if mibBuilder.loadTexts:sfpsL4CPIPRouteEntry.setStatus(_A)
_SfpsL4CPIPRouteSubnetMask_Type=IpAddress
_SfpsL4CPIPRouteSubnetMask_Object=MibTableColumn
sfpsL4CPIPRouteSubnetMask=_SfpsL4CPIPRouteSubnetMask_Object((1,3,6,1,4,1,52,4,2,4,2,6,1,8,1,1),_SfpsL4CPIPRouteSubnetMask_Type())
sfpsL4CPIPRouteSubnetMask.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsL4CPIPRouteSubnetMask.setStatus(_A)
_SfpsL4CPIPRouteSubnet_Type=IpAddress
_SfpsL4CPIPRouteSubnet_Object=MibTableColumn
sfpsL4CPIPRouteSubnet=_SfpsL4CPIPRouteSubnet_Object((1,3,6,1,4,1,52,4,2,4,2,6,1,8,1,2),_SfpsL4CPIPRouteSubnet_Type())
sfpsL4CPIPRouteSubnet.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsL4CPIPRouteSubnet.setStatus(_A)
_SfpsL4CPIPRouteRouteID_Type=Integer32
_SfpsL4CPIPRouteRouteID_Object=MibTableColumn
sfpsL4CPIPRouteRouteID=_SfpsL4CPIPRouteRouteID_Object((1,3,6,1,4,1,52,4,2,4,2,6,1,8,1,3),_SfpsL4CPIPRouteRouteID_Type())
sfpsL4CPIPRouteRouteID.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsL4CPIPRouteRouteID.setStatus(_A)
class _SfpsL4CPIPRouteRouteSubsystem_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('local',1),('remote',2)))
_SfpsL4CPIPRouteRouteSubsystem_Type.__name__=_C
_SfpsL4CPIPRouteRouteSubsystem_Object=MibTableColumn
sfpsL4CPIPRouteRouteSubsystem=_SfpsL4CPIPRouteRouteSubsystem_Object((1,3,6,1,4,1,52,4,2,4,2,6,1,8,1,4),_SfpsL4CPIPRouteRouteSubsystem_Type())
sfpsL4CPIPRouteRouteSubsystem.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsL4CPIPRouteRouteSubsystem.setStatus(_A)
_SfpsL4CPIPRouteDeviceID_Type=Integer32
_SfpsL4CPIPRouteDeviceID_Object=MibTableColumn
sfpsL4CPIPRouteDeviceID=_SfpsL4CPIPRouteDeviceID_Object((1,3,6,1,4,1,52,4,2,4,2,6,1,8,1,5),_SfpsL4CPIPRouteDeviceID_Type())
sfpsL4CPIPRouteDeviceID.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsL4CPIPRouteDeviceID.setStatus(_A)
_SfpsL4CPIPRouteDeviceName_Type=DisplayString
_SfpsL4CPIPRouteDeviceName_Object=MibTableColumn
sfpsL4CPIPRouteDeviceName=_SfpsL4CPIPRouteDeviceName_Object((1,3,6,1,4,1,52,4,2,4,2,6,1,8,1,6),_SfpsL4CPIPRouteDeviceName_Type())
sfpsL4CPIPRouteDeviceName.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsL4CPIPRouteDeviceName.setStatus(_A)
_SfpsL4CPIPRouteMACAddress_Type=SfpsAddress
_SfpsL4CPIPRouteMACAddress_Object=MibTableColumn
sfpsL4CPIPRouteMACAddress=_SfpsL4CPIPRouteMACAddress_Object((1,3,6,1,4,1,52,4,2,4,2,6,1,8,1,7),_SfpsL4CPIPRouteMACAddress_Type())
sfpsL4CPIPRouteMACAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsL4CPIPRouteMACAddress.setStatus(_A)
_SfpsL4CPIPRouteMetric_Type=Integer32
_SfpsL4CPIPRouteMetric_Object=MibTableColumn
sfpsL4CPIPRouteMetric=_SfpsL4CPIPRouteMetric_Object((1,3,6,1,4,1,52,4,2,4,2,6,1,8,1,8),_SfpsL4CPIPRouteMetric_Type())
sfpsL4CPIPRouteMetric.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsL4CPIPRouteMetric.setStatus(_A)
class _SfpsL4CPIPRouteCallable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_SfpsL4CPIPRouteCallable_Type.__name__=_C
_SfpsL4CPIPRouteCallable_Object=MibTableColumn
sfpsL4CPIPRouteCallable=_SfpsL4CPIPRouteCallable_Object((1,3,6,1,4,1,52,4,2,4,2,6,1,8,1,9),_SfpsL4CPIPRouteCallable_Type())
sfpsL4CPIPRouteCallable.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsL4CPIPRouteCallable.setStatus(_A)
_SfpsL4CPPortTable_Object=MibTable
sfpsL4CPPortTable=_SfpsL4CPPortTable_Object((1,3,6,1,4,1,52,4,2,4,2,6,1,9))
if mibBuilder.loadTexts:sfpsL4CPPortTable.setStatus(_A)
_SfpsL4CPPortEntry_Object=MibTableRow
sfpsL4CPPortEntry=_SfpsL4CPPortEntry_Object((1,3,6,1,4,1,52,4,2,4,2,6,1,9,1))
sfpsL4CPPortEntry.setIndexNames((0,_D,_Y))
if mibBuilder.loadTexts:sfpsL4CPPortEntry.setStatus(_A)
class _SfpsL4CPPortNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_SfpsL4CPPortNum_Type.__name__=_C
_SfpsL4CPPortNum_Object=MibTableColumn
sfpsL4CPPortNum=_SfpsL4CPPortNum_Object((1,3,6,1,4,1,52,4,2,4,2,6,1,9,1,1),_SfpsL4CPPortNum_Type())
sfpsL4CPPortNum.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsL4CPPortNum.setStatus(_A)
_SfpsL4CPPortID_Type=Integer32
_SfpsL4CPPortID_Object=MibTableColumn
sfpsL4CPPortID=_SfpsL4CPPortID_Object((1,3,6,1,4,1,52,4,2,4,2,6,1,9,1,2),_SfpsL4CPPortID_Type())
sfpsL4CPPortID.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsL4CPPortID.setStatus(_A)
class _SfpsL4CPPortApplyPolicyIn_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_SfpsL4CPPortApplyPolicyIn_Type.__name__=_C
_SfpsL4CPPortApplyPolicyIn_Object=MibTableColumn
sfpsL4CPPortApplyPolicyIn=_SfpsL4CPPortApplyPolicyIn_Object((1,3,6,1,4,1,52,4,2,4,2,6,1,9,1,3),_SfpsL4CPPortApplyPolicyIn_Type())
sfpsL4CPPortApplyPolicyIn.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsL4CPPortApplyPolicyIn.setStatus(_A)
class _SfpsL4CPPortApplyPolicyOut_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_SfpsL4CPPortApplyPolicyOut_Type.__name__=_C
_SfpsL4CPPortApplyPolicyOut_Object=MibTableColumn
sfpsL4CPPortApplyPolicyOut=_SfpsL4CPPortApplyPolicyOut_Object((1,3,6,1,4,1,52,4,2,4,2,6,1,9,1,4),_SfpsL4CPPortApplyPolicyOut_Type())
sfpsL4CPPortApplyPolicyOut.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsL4CPPortApplyPolicyOut.setStatus(_A)
_SfpsL4CPPortDefaultUserID_Type=Integer32
_SfpsL4CPPortDefaultUserID_Object=MibTableColumn
sfpsL4CPPortDefaultUserID=_SfpsL4CPPortDefaultUserID_Object((1,3,6,1,4,1,52,4,2,4,2,6,1,9,1,5),_SfpsL4CPPortDefaultUserID_Type())
sfpsL4CPPortDefaultUserID.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsL4CPPortDefaultUserID.setStatus(_A)
_SfpsL4CPPortDefaultUserName_Type=DisplayString
_SfpsL4CPPortDefaultUserName_Object=MibTableColumn
sfpsL4CPPortDefaultUserName=_SfpsL4CPPortDefaultUserName_Object((1,3,6,1,4,1,52,4,2,4,2,6,1,9,1,6),_SfpsL4CPPortDefaultUserName_Type())
sfpsL4CPPortDefaultUserName.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsL4CPPortDefaultUserName.setStatus(_A)
_SfpsL4CPCallableDeviceTable_Object=MibTable
sfpsL4CPCallableDeviceTable=_SfpsL4CPCallableDeviceTable_Object((1,3,6,1,4,1,52,4,2,4,2,6,1,11))
if mibBuilder.loadTexts:sfpsL4CPCallableDeviceTable.setStatus(_A)
_SfpsL4CPCallableDeviceEntry_Object=MibTableRow
sfpsL4CPCallableDeviceEntry=_SfpsL4CPCallableDeviceEntry_Object((1,3,6,1,4,1,52,4,2,4,2,6,1,11,1))
sfpsL4CPCallableDeviceEntry.setIndexNames((0,_D,_Z))
if mibBuilder.loadTexts:sfpsL4CPCallableDeviceEntry.setStatus(_A)
class _SfpsL4CPCallableDeviceDeviceID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_SfpsL4CPCallableDeviceDeviceID_Type.__name__=_C
_SfpsL4CPCallableDeviceDeviceID_Object=MibTableColumn
sfpsL4CPCallableDeviceDeviceID=_SfpsL4CPCallableDeviceDeviceID_Object((1,3,6,1,4,1,52,4,2,4,2,6,1,11,1,1),_SfpsL4CPCallableDeviceDeviceID_Type())
sfpsL4CPCallableDeviceDeviceID.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsL4CPCallableDeviceDeviceID.setStatus(_A)
_SfpsL4CPCallableDeviceDeviceName_Type=DisplayString
_SfpsL4CPCallableDeviceDeviceName_Object=MibTableColumn
sfpsL4CPCallableDeviceDeviceName=_SfpsL4CPCallableDeviceDeviceName_Object((1,3,6,1,4,1,52,4,2,4,2,6,1,11,1,2),_SfpsL4CPCallableDeviceDeviceName_Type())
sfpsL4CPCallableDeviceDeviceName.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsL4CPCallableDeviceDeviceName.setStatus(_A)
_SfpsL4CPCallableDeviceDefaultUserName_Type=DisplayString
_SfpsL4CPCallableDeviceDefaultUserName_Object=MibTableColumn
sfpsL4CPCallableDeviceDefaultUserName=_SfpsL4CPCallableDeviceDefaultUserName_Object((1,3,6,1,4,1,52,4,2,4,2,6,1,11,1,3),_SfpsL4CPCallableDeviceDefaultUserName_Type())
sfpsL4CPCallableDeviceDefaultUserName.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsL4CPCallableDeviceDefaultUserName.setStatus(_A)
_SfpsL4CDR_ObjectIdentity=ObjectIdentity
sfpsL4CDR=_SfpsL4CDR_ObjectIdentity((1,3,6,1,4,1,52,4,2,4,2,6,2))
_L4cdrStats_ObjectIdentity=ObjectIdentity
l4cdrStats=_L4cdrStats_ObjectIdentity((1,3,6,1,4,1,52,4,2,4,2,6,2,1))
_L4cdrConfig_ObjectIdentity=ObjectIdentity
l4cdrConfig=_L4cdrConfig_ObjectIdentity((1,3,6,1,4,1,52,4,2,4,2,6,2,2))
_L4cdrActions_ObjectIdentity=ObjectIdentity
l4cdrActions=_L4cdrActions_ObjectIdentity((1,3,6,1,4,1,52,4,2,4,2,6,2,3))
_SfpsL4CDRActiveFlowTable_Object=MibTable
sfpsL4CDRActiveFlowTable=_SfpsL4CDRActiveFlowTable_Object((1,3,6,1,4,1,52,4,2,4,2,6,2,4))
if mibBuilder.loadTexts:sfpsL4CDRActiveFlowTable.setStatus(_A)
_SfpsL4CDRActiveFlowEntry_Object=MibTableRow
sfpsL4CDRActiveFlowEntry=_SfpsL4CDRActiveFlowEntry_Object((1,3,6,1,4,1,52,4,2,4,2,6,2,4,1))
sfpsL4CDRActiveFlowEntry.setIndexNames((0,_D,_a))
if mibBuilder.loadTexts:sfpsL4CDRActiveFlowEntry.setStatus(_A)
class _SfpsL4CDRActiveFlowFlowID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_SfpsL4CDRActiveFlowFlowID_Type.__name__=_C
_SfpsL4CDRActiveFlowFlowID_Object=MibTableColumn
sfpsL4CDRActiveFlowFlowID=_SfpsL4CDRActiveFlowFlowID_Object((1,3,6,1,4,1,52,4,2,4,2,6,2,4,1,1),_SfpsL4CDRActiveFlowFlowID_Type())
sfpsL4CDRActiveFlowFlowID.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsL4CDRActiveFlowFlowID.setStatus(_A)
_SfpsL4CDRActiveFlowSubProtocol_Type=Integer32
_SfpsL4CDRActiveFlowSubProtocol_Object=MibTableColumn
sfpsL4CDRActiveFlowSubProtocol=_SfpsL4CDRActiveFlowSubProtocol_Object((1,3,6,1,4,1,52,4,2,4,2,6,2,4,1,2),_SfpsL4CDRActiveFlowSubProtocol_Type())
sfpsL4CDRActiveFlowSubProtocol.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsL4CDRActiveFlowSubProtocol.setStatus(_A)
_SfpsL4CDRActiveFlowEtherType_Type=Integer32
_SfpsL4CDRActiveFlowEtherType_Object=MibTableColumn
sfpsL4CDRActiveFlowEtherType=_SfpsL4CDRActiveFlowEtherType_Object((1,3,6,1,4,1,52,4,2,4,2,6,2,4,1,3),_SfpsL4CDRActiveFlowEtherType_Type())
sfpsL4CDRActiveFlowEtherType.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsL4CDRActiveFlowEtherType.setStatus(_A)
_SfpsL4CDRActiveFlowSourceUser_Type=DisplayString
_SfpsL4CDRActiveFlowSourceUser_Object=MibTableColumn
sfpsL4CDRActiveFlowSourceUser=_SfpsL4CDRActiveFlowSourceUser_Object((1,3,6,1,4,1,52,4,2,4,2,6,2,4,1,4),_SfpsL4CDRActiveFlowSourceUser_Type())
sfpsL4CDRActiveFlowSourceUser.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsL4CDRActiveFlowSourceUser.setStatus(_A)
_SfpsL4CDRActiveFlowSourceMACAddr_Type=DisplayString
_SfpsL4CDRActiveFlowSourceMACAddr_Object=MibTableColumn
sfpsL4CDRActiveFlowSourceMACAddr=_SfpsL4CDRActiveFlowSourceMACAddr_Object((1,3,6,1,4,1,52,4,2,4,2,6,2,4,1,5),_SfpsL4CDRActiveFlowSourceMACAddr_Type())
sfpsL4CDRActiveFlowSourceMACAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsL4CDRActiveFlowSourceMACAddr.setStatus(_A)
_SfpsL4CDRActiveFlowSourceNetAddr_Type=DisplayString
_SfpsL4CDRActiveFlowSourceNetAddr_Object=MibTableColumn
sfpsL4CDRActiveFlowSourceNetAddr=_SfpsL4CDRActiveFlowSourceNetAddr_Object((1,3,6,1,4,1,52,4,2,4,2,6,2,4,1,6),_SfpsL4CDRActiveFlowSourceNetAddr_Type())
sfpsL4CDRActiveFlowSourceNetAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsL4CDRActiveFlowSourceNetAddr.setStatus(_A)
_SfpsL4CDRActiveFlowSourceProtocolPort_Type=Integer32
_SfpsL4CDRActiveFlowSourceProtocolPort_Object=MibTableColumn
sfpsL4CDRActiveFlowSourceProtocolPort=_SfpsL4CDRActiveFlowSourceProtocolPort_Object((1,3,6,1,4,1,52,4,2,4,2,6,2,4,1,7),_SfpsL4CDRActiveFlowSourceProtocolPort_Type())
sfpsL4CDRActiveFlowSourceProtocolPort.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsL4CDRActiveFlowSourceProtocolPort.setStatus(_A)
class _SfpsL4CDRActiveFlowSourcePPRangeEnabled_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_SfpsL4CDRActiveFlowSourcePPRangeEnabled_Type.__name__=_C
_SfpsL4CDRActiveFlowSourcePPRangeEnabled_Object=MibTableColumn
sfpsL4CDRActiveFlowSourcePPRangeEnabled=_SfpsL4CDRActiveFlowSourcePPRangeEnabled_Object((1,3,6,1,4,1,52,4,2,4,2,6,2,4,1,8),_SfpsL4CDRActiveFlowSourcePPRangeEnabled_Type())
sfpsL4CDRActiveFlowSourcePPRangeEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsL4CDRActiveFlowSourcePPRangeEnabled.setStatus(_A)
_SfpsL4CDRActiveFlowSourceConnNumber_Type=Integer32
_SfpsL4CDRActiveFlowSourceConnNumber_Object=MibTableColumn
sfpsL4CDRActiveFlowSourceConnNumber=_SfpsL4CDRActiveFlowSourceConnNumber_Object((1,3,6,1,4,1,52,4,2,4,2,6,2,4,1,9),_SfpsL4CDRActiveFlowSourceConnNumber_Type())
sfpsL4CDRActiveFlowSourceConnNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsL4CDRActiveFlowSourceConnNumber.setStatus(_A)
_SfpsL4CDRActiveFlowDestUser_Type=DisplayString
_SfpsL4CDRActiveFlowDestUser_Object=MibTableColumn
sfpsL4CDRActiveFlowDestUser=_SfpsL4CDRActiveFlowDestUser_Object((1,3,6,1,4,1,52,4,2,4,2,6,2,4,1,10),_SfpsL4CDRActiveFlowDestUser_Type())
sfpsL4CDRActiveFlowDestUser.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsL4CDRActiveFlowDestUser.setStatus(_A)
_SfpsL4CDRActiveFlowDestMACAddr_Type=DisplayString
_SfpsL4CDRActiveFlowDestMACAddr_Object=MibTableColumn
sfpsL4CDRActiveFlowDestMACAddr=_SfpsL4CDRActiveFlowDestMACAddr_Object((1,3,6,1,4,1,52,4,2,4,2,6,2,4,1,11),_SfpsL4CDRActiveFlowDestMACAddr_Type())
sfpsL4CDRActiveFlowDestMACAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsL4CDRActiveFlowDestMACAddr.setStatus(_A)
_SfpsL4CDRActiveFlowDestNetAddr_Type=DisplayString
_SfpsL4CDRActiveFlowDestNetAddr_Object=MibTableColumn
sfpsL4CDRActiveFlowDestNetAddr=_SfpsL4CDRActiveFlowDestNetAddr_Object((1,3,6,1,4,1,52,4,2,4,2,6,2,4,1,12),_SfpsL4CDRActiveFlowDestNetAddr_Type())
sfpsL4CDRActiveFlowDestNetAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsL4CDRActiveFlowDestNetAddr.setStatus(_A)
_SfpsL4CDRActiveFlowDestProtocolPort_Type=Integer32
_SfpsL4CDRActiveFlowDestProtocolPort_Object=MibTableColumn
sfpsL4CDRActiveFlowDestProtocolPort=_SfpsL4CDRActiveFlowDestProtocolPort_Object((1,3,6,1,4,1,52,4,2,4,2,6,2,4,1,13),_SfpsL4CDRActiveFlowDestProtocolPort_Type())
sfpsL4CDRActiveFlowDestProtocolPort.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsL4CDRActiveFlowDestProtocolPort.setStatus(_A)
class _SfpsL4CDRActiveFlowDestPPRangeEnabled_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_SfpsL4CDRActiveFlowDestPPRangeEnabled_Type.__name__=_C
_SfpsL4CDRActiveFlowDestPPRangeEnabled_Object=MibTableColumn
sfpsL4CDRActiveFlowDestPPRangeEnabled=_SfpsL4CDRActiveFlowDestPPRangeEnabled_Object((1,3,6,1,4,1,52,4,2,4,2,6,2,4,1,14),_SfpsL4CDRActiveFlowDestPPRangeEnabled_Type())
sfpsL4CDRActiveFlowDestPPRangeEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsL4CDRActiveFlowDestPPRangeEnabled.setStatus(_A)
_SfpsL4CDRActiveFlowDestConnNumber_Type=Integer32
_SfpsL4CDRActiveFlowDestConnNumber_Object=MibTableColumn
sfpsL4CDRActiveFlowDestConnNumber=_SfpsL4CDRActiveFlowDestConnNumber_Object((1,3,6,1,4,1,52,4,2,4,2,6,2,4,1,15),_SfpsL4CDRActiveFlowDestConnNumber_Type())
sfpsL4CDRActiveFlowDestConnNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsL4CDRActiveFlowDestConnNumber.setStatus(_A)
_SfpsL4CDRActiveFlowStartTime_Type=TimeTicks
_SfpsL4CDRActiveFlowStartTime_Object=MibTableColumn
sfpsL4CDRActiveFlowStartTime=_SfpsL4CDRActiveFlowStartTime_Object((1,3,6,1,4,1,52,4,2,4,2,6,2,4,1,16),_SfpsL4CDRActiveFlowStartTime_Type())
sfpsL4CDRActiveFlowStartTime.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsL4CDRActiveFlowStartTime.setStatus(_A)
_SfpsL4CDRActiveFlowLastPktTime_Type=TimeTicks
_SfpsL4CDRActiveFlowLastPktTime_Object=MibTableColumn
sfpsL4CDRActiveFlowLastPktTime=_SfpsL4CDRActiveFlowLastPktTime_Object((1,3,6,1,4,1,52,4,2,4,2,6,2,4,1,17),_SfpsL4CDRActiveFlowLastPktTime_Type())
sfpsL4CDRActiveFlowLastPktTime.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsL4CDRActiveFlowLastPktTime.setStatus(_A)
_SfpsL4CDRActiveFlowEndTime_Type=TimeTicks
_SfpsL4CDRActiveFlowEndTime_Object=MibTableColumn
sfpsL4CDRActiveFlowEndTime=_SfpsL4CDRActiveFlowEndTime_Object((1,3,6,1,4,1,52,4,2,4,2,6,2,4,1,18),_SfpsL4CDRActiveFlowEndTime_Type())
sfpsL4CDRActiveFlowEndTime.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsL4CDRActiveFlowEndTime.setStatus(_A)
_SfpsL4CDRActiveFlowInOctets_Type=Counter32
_SfpsL4CDRActiveFlowInOctets_Object=MibTableColumn
sfpsL4CDRActiveFlowInOctets=_SfpsL4CDRActiveFlowInOctets_Object((1,3,6,1,4,1,52,4,2,4,2,6,2,4,1,19),_SfpsL4CDRActiveFlowInOctets_Type())
sfpsL4CDRActiveFlowInOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsL4CDRActiveFlowInOctets.setStatus(_A)
_SfpsL4CDRActiveFlowOutOctets_Type=Counter32
_SfpsL4CDRActiveFlowOutOctets_Object=MibTableColumn
sfpsL4CDRActiveFlowOutOctets=_SfpsL4CDRActiveFlowOutOctets_Object((1,3,6,1,4,1,52,4,2,4,2,6,2,4,1,20),_SfpsL4CDRActiveFlowOutOctets_Type())
sfpsL4CDRActiveFlowOutOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsL4CDRActiveFlowOutOctets.setStatus(_A)
_SfpsL4CDRActiveFlowInPkts_Type=Counter32
_SfpsL4CDRActiveFlowInPkts_Object=MibTableColumn
sfpsL4CDRActiveFlowInPkts=_SfpsL4CDRActiveFlowInPkts_Object((1,3,6,1,4,1,52,4,2,4,2,6,2,4,1,21),_SfpsL4CDRActiveFlowInPkts_Type())
sfpsL4CDRActiveFlowInPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsL4CDRActiveFlowInPkts.setStatus(_A)
_SfpsL4CDRActiveFlowOutPkts_Type=Counter32
_SfpsL4CDRActiveFlowOutPkts_Object=MibTableColumn
sfpsL4CDRActiveFlowOutPkts=_SfpsL4CDRActiveFlowOutPkts_Object((1,3,6,1,4,1,52,4,2,4,2,6,2,4,1,22),_SfpsL4CDRActiveFlowOutPkts_Type())
sfpsL4CDRActiveFlowOutPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsL4CDRActiveFlowOutPkts.setStatus(_A)
class _SfpsL4CDRActiveFlowDemandAccessConnMade_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_SfpsL4CDRActiveFlowDemandAccessConnMade_Type.__name__=_C
_SfpsL4CDRActiveFlowDemandAccessConnMade_Object=MibTableColumn
sfpsL4CDRActiveFlowDemandAccessConnMade=_SfpsL4CDRActiveFlowDemandAccessConnMade_Object((1,3,6,1,4,1,52,4,2,4,2,6,2,4,1,23),_SfpsL4CDRActiveFlowDemandAccessConnMade_Type())
sfpsL4CDRActiveFlowDemandAccessConnMade.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsL4CDRActiveFlowDemandAccessConnMade.setStatus(_A)
class _SfpsL4CDRActiveFlowFlowRecordState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_G,1),(_H,2),(_I,3),(_J,4)))
_SfpsL4CDRActiveFlowFlowRecordState_Type.__name__=_C
_SfpsL4CDRActiveFlowFlowRecordState_Object=MibTableColumn
sfpsL4CDRActiveFlowFlowRecordState=_SfpsL4CDRActiveFlowFlowRecordState_Object((1,3,6,1,4,1,52,4,2,4,2,6,2,4,1,24),_SfpsL4CDRActiveFlowFlowRecordState_Type())
sfpsL4CDRActiveFlowFlowRecordState.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsL4CDRActiveFlowFlowRecordState.setStatus(_A)
_SfpsL4CDRTermedFlowTable_Object=MibTable
sfpsL4CDRTermedFlowTable=_SfpsL4CDRTermedFlowTable_Object((1,3,6,1,4,1,52,4,2,4,2,6,2,5))
if mibBuilder.loadTexts:sfpsL4CDRTermedFlowTable.setStatus(_A)
_SfpsL4CDRTermedFlowEntry_Object=MibTableRow
sfpsL4CDRTermedFlowEntry=_SfpsL4CDRTermedFlowEntry_Object((1,3,6,1,4,1,52,4,2,4,2,6,2,5,1))
sfpsL4CDRTermedFlowEntry.setIndexNames((0,_D,_b))
if mibBuilder.loadTexts:sfpsL4CDRTermedFlowEntry.setStatus(_A)
class _SfpsL4CDRTermedFlowFlowID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_SfpsL4CDRTermedFlowFlowID_Type.__name__=_C
_SfpsL4CDRTermedFlowFlowID_Object=MibTableColumn
sfpsL4CDRTermedFlowFlowID=_SfpsL4CDRTermedFlowFlowID_Object((1,3,6,1,4,1,52,4,2,4,2,6,2,5,1,1),_SfpsL4CDRTermedFlowFlowID_Type())
sfpsL4CDRTermedFlowFlowID.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsL4CDRTermedFlowFlowID.setStatus(_A)
_SfpsL4CDRTermedFlowSubProtocol_Type=Integer32
_SfpsL4CDRTermedFlowSubProtocol_Object=MibTableColumn
sfpsL4CDRTermedFlowSubProtocol=_SfpsL4CDRTermedFlowSubProtocol_Object((1,3,6,1,4,1,52,4,2,4,2,6,2,5,1,2),_SfpsL4CDRTermedFlowSubProtocol_Type())
sfpsL4CDRTermedFlowSubProtocol.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsL4CDRTermedFlowSubProtocol.setStatus(_A)
_SfpsL4CDRTermedFlowEtherType_Type=Integer32
_SfpsL4CDRTermedFlowEtherType_Object=MibTableColumn
sfpsL4CDRTermedFlowEtherType=_SfpsL4CDRTermedFlowEtherType_Object((1,3,6,1,4,1,52,4,2,4,2,6,2,5,1,3),_SfpsL4CDRTermedFlowEtherType_Type())
sfpsL4CDRTermedFlowEtherType.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsL4CDRTermedFlowEtherType.setStatus(_A)
_SfpsL4CDRTermedFlowSourceUser_Type=DisplayString
_SfpsL4CDRTermedFlowSourceUser_Object=MibTableColumn
sfpsL4CDRTermedFlowSourceUser=_SfpsL4CDRTermedFlowSourceUser_Object((1,3,6,1,4,1,52,4,2,4,2,6,2,5,1,4),_SfpsL4CDRTermedFlowSourceUser_Type())
sfpsL4CDRTermedFlowSourceUser.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsL4CDRTermedFlowSourceUser.setStatus(_A)
_SfpsL4CDRTermedFlowSourceMACAddr_Type=DisplayString
_SfpsL4CDRTermedFlowSourceMACAddr_Object=MibTableColumn
sfpsL4CDRTermedFlowSourceMACAddr=_SfpsL4CDRTermedFlowSourceMACAddr_Object((1,3,6,1,4,1,52,4,2,4,2,6,2,5,1,5),_SfpsL4CDRTermedFlowSourceMACAddr_Type())
sfpsL4CDRTermedFlowSourceMACAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsL4CDRTermedFlowSourceMACAddr.setStatus(_A)
_SfpsL4CDRTermedFlowSourceNetAddr_Type=DisplayString
_SfpsL4CDRTermedFlowSourceNetAddr_Object=MibTableColumn
sfpsL4CDRTermedFlowSourceNetAddr=_SfpsL4CDRTermedFlowSourceNetAddr_Object((1,3,6,1,4,1,52,4,2,4,2,6,2,5,1,6),_SfpsL4CDRTermedFlowSourceNetAddr_Type())
sfpsL4CDRTermedFlowSourceNetAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsL4CDRTermedFlowSourceNetAddr.setStatus(_A)
_SfpsL4CDRTermedFlowSourceProtocolPort_Type=Integer32
_SfpsL4CDRTermedFlowSourceProtocolPort_Object=MibTableColumn
sfpsL4CDRTermedFlowSourceProtocolPort=_SfpsL4CDRTermedFlowSourceProtocolPort_Object((1,3,6,1,4,1,52,4,2,4,2,6,2,5,1,7),_SfpsL4CDRTermedFlowSourceProtocolPort_Type())
sfpsL4CDRTermedFlowSourceProtocolPort.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsL4CDRTermedFlowSourceProtocolPort.setStatus(_A)
class _SfpsL4CDRTermedFlowSourcePPRangeEnabled_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_SfpsL4CDRTermedFlowSourcePPRangeEnabled_Type.__name__=_C
_SfpsL4CDRTermedFlowSourcePPRangeEnabled_Object=MibTableColumn
sfpsL4CDRTermedFlowSourcePPRangeEnabled=_SfpsL4CDRTermedFlowSourcePPRangeEnabled_Object((1,3,6,1,4,1,52,4,2,4,2,6,2,5,1,8),_SfpsL4CDRTermedFlowSourcePPRangeEnabled_Type())
sfpsL4CDRTermedFlowSourcePPRangeEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsL4CDRTermedFlowSourcePPRangeEnabled.setStatus(_A)
_SfpsL4CDRTermedFlowSourceConnNumber_Type=Integer32
_SfpsL4CDRTermedFlowSourceConnNumber_Object=MibTableColumn
sfpsL4CDRTermedFlowSourceConnNumber=_SfpsL4CDRTermedFlowSourceConnNumber_Object((1,3,6,1,4,1,52,4,2,4,2,6,2,5,1,9),_SfpsL4CDRTermedFlowSourceConnNumber_Type())
sfpsL4CDRTermedFlowSourceConnNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsL4CDRTermedFlowSourceConnNumber.setStatus(_A)
_SfpsL4CDRTermedFlowDestUser_Type=DisplayString
_SfpsL4CDRTermedFlowDestUser_Object=MibTableColumn
sfpsL4CDRTermedFlowDestUser=_SfpsL4CDRTermedFlowDestUser_Object((1,3,6,1,4,1,52,4,2,4,2,6,2,5,1,10),_SfpsL4CDRTermedFlowDestUser_Type())
sfpsL4CDRTermedFlowDestUser.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsL4CDRTermedFlowDestUser.setStatus(_A)
_SfpsL4CDRTermedFlowDestMACAddr_Type=DisplayString
_SfpsL4CDRTermedFlowDestMACAddr_Object=MibTableColumn
sfpsL4CDRTermedFlowDestMACAddr=_SfpsL4CDRTermedFlowDestMACAddr_Object((1,3,6,1,4,1,52,4,2,4,2,6,2,5,1,11),_SfpsL4CDRTermedFlowDestMACAddr_Type())
sfpsL4CDRTermedFlowDestMACAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsL4CDRTermedFlowDestMACAddr.setStatus(_A)
_SfpsL4CDRTermedFlowDestNetAddr_Type=DisplayString
_SfpsL4CDRTermedFlowDestNetAddr_Object=MibTableColumn
sfpsL4CDRTermedFlowDestNetAddr=_SfpsL4CDRTermedFlowDestNetAddr_Object((1,3,6,1,4,1,52,4,2,4,2,6,2,5,1,12),_SfpsL4CDRTermedFlowDestNetAddr_Type())
sfpsL4CDRTermedFlowDestNetAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsL4CDRTermedFlowDestNetAddr.setStatus(_A)
_SfpsL4CDRTermedFlowDestProtocolPort_Type=Integer32
_SfpsL4CDRTermedFlowDestProtocolPort_Object=MibTableColumn
sfpsL4CDRTermedFlowDestProtocolPort=_SfpsL4CDRTermedFlowDestProtocolPort_Object((1,3,6,1,4,1,52,4,2,4,2,6,2,5,1,13),_SfpsL4CDRTermedFlowDestProtocolPort_Type())
sfpsL4CDRTermedFlowDestProtocolPort.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsL4CDRTermedFlowDestProtocolPort.setStatus(_A)
class _SfpsL4CDRTermedFlowDestPPRangeEnabled_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_SfpsL4CDRTermedFlowDestPPRangeEnabled_Type.__name__=_C
_SfpsL4CDRTermedFlowDestPPRangeEnabled_Object=MibTableColumn
sfpsL4CDRTermedFlowDestPPRangeEnabled=_SfpsL4CDRTermedFlowDestPPRangeEnabled_Object((1,3,6,1,4,1,52,4,2,4,2,6,2,5,1,14),_SfpsL4CDRTermedFlowDestPPRangeEnabled_Type())
sfpsL4CDRTermedFlowDestPPRangeEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsL4CDRTermedFlowDestPPRangeEnabled.setStatus(_A)
_SfpsL4CDRTermedFlowDestConnNumber_Type=Integer32
_SfpsL4CDRTermedFlowDestConnNumber_Object=MibTableColumn
sfpsL4CDRTermedFlowDestConnNumber=_SfpsL4CDRTermedFlowDestConnNumber_Object((1,3,6,1,4,1,52,4,2,4,2,6,2,5,1,15),_SfpsL4CDRTermedFlowDestConnNumber_Type())
sfpsL4CDRTermedFlowDestConnNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsL4CDRTermedFlowDestConnNumber.setStatus(_A)
_SfpsL4CDRTermedFlowStartTime_Type=TimeTicks
_SfpsL4CDRTermedFlowStartTime_Object=MibTableColumn
sfpsL4CDRTermedFlowStartTime=_SfpsL4CDRTermedFlowStartTime_Object((1,3,6,1,4,1,52,4,2,4,2,6,2,5,1,16),_SfpsL4CDRTermedFlowStartTime_Type())
sfpsL4CDRTermedFlowStartTime.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsL4CDRTermedFlowStartTime.setStatus(_A)
_SfpsL4CDRTermedFlowLastPktTime_Type=TimeTicks
_SfpsL4CDRTermedFlowLastPktTime_Object=MibTableColumn
sfpsL4CDRTermedFlowLastPktTime=_SfpsL4CDRTermedFlowLastPktTime_Object((1,3,6,1,4,1,52,4,2,4,2,6,2,5,1,17),_SfpsL4CDRTermedFlowLastPktTime_Type())
sfpsL4CDRTermedFlowLastPktTime.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsL4CDRTermedFlowLastPktTime.setStatus(_A)
_SfpsL4CDRTermedFlowEndTime_Type=TimeTicks
_SfpsL4CDRTermedFlowEndTime_Object=MibTableColumn
sfpsL4CDRTermedFlowEndTime=_SfpsL4CDRTermedFlowEndTime_Object((1,3,6,1,4,1,52,4,2,4,2,6,2,5,1,18),_SfpsL4CDRTermedFlowEndTime_Type())
sfpsL4CDRTermedFlowEndTime.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsL4CDRTermedFlowEndTime.setStatus(_A)
_SfpsL4CDRTermedFlowInOctets_Type=Counter32
_SfpsL4CDRTermedFlowInOctets_Object=MibTableColumn
sfpsL4CDRTermedFlowInOctets=_SfpsL4CDRTermedFlowInOctets_Object((1,3,6,1,4,1,52,4,2,4,2,6,2,5,1,19),_SfpsL4CDRTermedFlowInOctets_Type())
sfpsL4CDRTermedFlowInOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsL4CDRTermedFlowInOctets.setStatus(_A)
_SfpsL4CDRTermedFlowOutOctets_Type=Counter32
_SfpsL4CDRTermedFlowOutOctets_Object=MibTableColumn
sfpsL4CDRTermedFlowOutOctets=_SfpsL4CDRTermedFlowOutOctets_Object((1,3,6,1,4,1,52,4,2,4,2,6,2,5,1,20),_SfpsL4CDRTermedFlowOutOctets_Type())
sfpsL4CDRTermedFlowOutOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsL4CDRTermedFlowOutOctets.setStatus(_A)
_SfpsL4CDRTermedFlowInPkts_Type=Counter32
_SfpsL4CDRTermedFlowInPkts_Object=MibTableColumn
sfpsL4CDRTermedFlowInPkts=_SfpsL4CDRTermedFlowInPkts_Object((1,3,6,1,4,1,52,4,2,4,2,6,2,5,1,21),_SfpsL4CDRTermedFlowInPkts_Type())
sfpsL4CDRTermedFlowInPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsL4CDRTermedFlowInPkts.setStatus(_A)
_SfpsL4CDRTermedFlowOutPkts_Type=Counter32
_SfpsL4CDRTermedFlowOutPkts_Object=MibTableColumn
sfpsL4CDRTermedFlowOutPkts=_SfpsL4CDRTermedFlowOutPkts_Object((1,3,6,1,4,1,52,4,2,4,2,6,2,5,1,22),_SfpsL4CDRTermedFlowOutPkts_Type())
sfpsL4CDRTermedFlowOutPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsL4CDRTermedFlowOutPkts.setStatus(_A)
class _SfpsL4CDRTermedFlowDemandAccessConnMade_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_SfpsL4CDRTermedFlowDemandAccessConnMade_Type.__name__=_C
_SfpsL4CDRTermedFlowDemandAccessConnMade_Object=MibTableColumn
sfpsL4CDRTermedFlowDemandAccessConnMade=_SfpsL4CDRTermedFlowDemandAccessConnMade_Object((1,3,6,1,4,1,52,4,2,4,2,6,2,5,1,23),_SfpsL4CDRTermedFlowDemandAccessConnMade_Type())
sfpsL4CDRTermedFlowDemandAccessConnMade.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsL4CDRTermedFlowDemandAccessConnMade.setStatus(_A)
class _SfpsL4CDRTermedFlowFlowRecordState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_G,1),(_H,2),(_I,3),(_J,4)))
_SfpsL4CDRTermedFlowFlowRecordState_Type.__name__=_C
_SfpsL4CDRTermedFlowFlowRecordState_Object=MibTableColumn
sfpsL4CDRTermedFlowFlowRecordState=_SfpsL4CDRTermedFlowFlowRecordState_Object((1,3,6,1,4,1,52,4,2,4,2,6,2,5,1,24),_SfpsL4CDRTermedFlowFlowRecordState_Type())
sfpsL4CDRTermedFlowFlowRecordState.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsL4CDRTermedFlowFlowRecordState.setStatus(_A)
_SfpsL4CDRFlowIndexTable_Object=MibTable
sfpsL4CDRFlowIndexTable=_SfpsL4CDRFlowIndexTable_Object((1,3,6,1,4,1,52,4,2,4,2,6,2,6))
if mibBuilder.loadTexts:sfpsL4CDRFlowIndexTable.setStatus(_A)
_SfpsL4CDRFlowIndexEntry_Object=MibTableRow
sfpsL4CDRFlowIndexEntry=_SfpsL4CDRFlowIndexEntry_Object((1,3,6,1,4,1,52,4,2,4,2,6,2,6,1))
sfpsL4CDRFlowIndexEntry.setIndexNames((0,_D,_c))
if mibBuilder.loadTexts:sfpsL4CDRFlowIndexEntry.setStatus(_A)
class _SfpsL4CDRFlowIndexFlowID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_SfpsL4CDRFlowIndexFlowID_Type.__name__=_C
_SfpsL4CDRFlowIndexFlowID_Object=MibTableColumn
sfpsL4CDRFlowIndexFlowID=_SfpsL4CDRFlowIndexFlowID_Object((1,3,6,1,4,1,52,4,2,4,2,6,2,6,1,1),_SfpsL4CDRFlowIndexFlowID_Type())
sfpsL4CDRFlowIndexFlowID.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsL4CDRFlowIndexFlowID.setStatus(_A)
_SfpsL4CDRFlowIndexSFPSFlowTblIndex_Type=Integer32
_SfpsL4CDRFlowIndexSFPSFlowTblIndex_Object=MibTableColumn
sfpsL4CDRFlowIndexSFPSFlowTblIndex=_SfpsL4CDRFlowIndexSFPSFlowTblIndex_Object((1,3,6,1,4,1,52,4,2,4,2,6,2,6,1,2),_SfpsL4CDRFlowIndexSFPSFlowTblIndex_Type())
sfpsL4CDRFlowIndexSFPSFlowTblIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsL4CDRFlowIndexSFPSFlowTblIndex.setStatus(_A)
_SfpsL4CDRFlowIndexSFlowStatsPtr_Type=Integer32
_SfpsL4CDRFlowIndexSFlowStatsPtr_Object=MibTableColumn
sfpsL4CDRFlowIndexSFlowStatsPtr=_SfpsL4CDRFlowIndexSFlowStatsPtr_Object((1,3,6,1,4,1,52,4,2,4,2,6,2,6,1,3),_SfpsL4CDRFlowIndexSFlowStatsPtr_Type())
sfpsL4CDRFlowIndexSFlowStatsPtr.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsL4CDRFlowIndexSFlowStatsPtr.setStatus(_A)
_SfpsL4CDRFlowIndexStaticFlowInfoPtr_Type=Integer32
_SfpsL4CDRFlowIndexStaticFlowInfoPtr_Object=MibTableColumn
sfpsL4CDRFlowIndexStaticFlowInfoPtr=_SfpsL4CDRFlowIndexStaticFlowInfoPtr_Object((1,3,6,1,4,1,52,4,2,4,2,6,2,6,1,4),_SfpsL4CDRFlowIndexStaticFlowInfoPtr_Type())
sfpsL4CDRFlowIndexStaticFlowInfoPtr.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsL4CDRFlowIndexStaticFlowInfoPtr.setStatus(_A)
_SfpsL4CDRFlowIndexFlowTblEntryPtr_Type=Integer32
_SfpsL4CDRFlowIndexFlowTblEntryPtr_Object=MibTableColumn
sfpsL4CDRFlowIndexFlowTblEntryPtr=_SfpsL4CDRFlowIndexFlowTblEntryPtr_Object((1,3,6,1,4,1,52,4,2,4,2,6,2,6,1,5),_SfpsL4CDRFlowIndexFlowTblEntryPtr_Type())
sfpsL4CDRFlowIndexFlowTblEntryPtr.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsL4CDRFlowIndexFlowTblEntryPtr.setStatus(_A)
class _SfpsL4CDRFlowIndexFlowState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_G,1),(_H,2),(_I,3),(_J,4)))
_SfpsL4CDRFlowIndexFlowState_Type.__name__=_C
_SfpsL4CDRFlowIndexFlowState_Object=MibTableColumn
sfpsL4CDRFlowIndexFlowState=_SfpsL4CDRFlowIndexFlowState_Object((1,3,6,1,4,1,52,4,2,4,2,6,2,6,1,6),_SfpsL4CDRFlowIndexFlowState_Type())
sfpsL4CDRFlowIndexFlowState.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsL4CDRFlowIndexFlowState.setStatus(_A)
mibBuilder.exportSymbols(_D,**{_S:HexInteger,'SfpsAddress':SfpsAddress,'sfpsL4SS':sfpsL4SS,'sfpsL4CP':sfpsL4CP,'l4cpStats':l4cpStats,'l4cpConfig':l4cpConfig,'sfpsL4CPDisableTCPAckCheck':sfpsL4CPDisableTCPAckCheck,'l4cpActions':l4cpActions,'sfpsL4CPFlowTable':sfpsL4CPFlowTable,'sfpsL4CPFlowEntry':sfpsL4CPFlowEntry,_K:sfpsL4CPFlowCnxIndex,_L:sfpsL4CPFlowSecL3Address,_M:sfpsL4CPFlowPrimL3Address,_N:sfpsL4CPFlowSubprotocol,_O:sfpsL4CPFlowSecMatchAnyDyn,_P:sfpsL4CPFlowPrimMatchAnyDyn,_Q:sfpsL4CPFlowSecProtPort,_R:sfpsL4CPFlowPrimProtPort,'sfpsL4CPFlowSecSubstApplies':sfpsL4CPFlowSecSubstApplies,'sfpsL4CPFlowPrimSubstApplies':sfpsL4CPFlowPrimSubstApplies,'sfpsL4CPFlowSecInPkts':sfpsL4CPFlowSecInPkts,'sfpsL4CPFlowSecInOctets':sfpsL4CPFlowSecInOctets,'sfpsL4CPFlowPrimInPkts':sfpsL4CPFlowPrimInPkts,'sfpsL4CPFlowPrimInOctets':sfpsL4CPFlowPrimInOctets,'sfpsL4CPFlowFlowAge':sfpsL4CPFlowFlowAge,'sfpsL4CPFlowFlowLastUse':sfpsL4CPFlowFlowLastUse,'sfpsL4CPFlowID':sfpsL4CPFlowID,'sfpsL4CPMACAddrSubTable':sfpsL4CPMACAddrSubTable,'sfpsL4CPMACAddrSubEntry':sfpsL4CPMACAddrSubEntry,_T:sfpsL4CPMACAddrSubDestIP,'sfpsL4CPMACAddrSubNextHopMAC':sfpsL4CPMACAddrSubNextHopMAC,'sfpsL4CPMACAddrSubRefCount':sfpsL4CPMACAddrSubRefCount,'sfpsL4CPNetAddrUserTable':sfpsL4CPNetAddrUserTable,'sfpsL4CPNetAddrUserEntry':sfpsL4CPNetAddrUserEntry,_U:sfpsL4CPNetAddrUserProtocol,_V:sfpsL4CPNetAddrUserNetAddr,'sfpsL4CPNetAddrUserLoginID':sfpsL4CPNetAddrUserLoginID,'sfpsL4CPNetAddrUserUserID':sfpsL4CPNetAddrUserUserID,'sfpsL4CPNetAddrUserUserName':sfpsL4CPNetAddrUserUserName,'sfpsL4CPIPRouteTable':sfpsL4CPIPRouteTable,'sfpsL4CPIPRouteEntry':sfpsL4CPIPRouteEntry,_W:sfpsL4CPIPRouteSubnetMask,_X:sfpsL4CPIPRouteSubnet,'sfpsL4CPIPRouteRouteID':sfpsL4CPIPRouteRouteID,'sfpsL4CPIPRouteRouteSubsystem':sfpsL4CPIPRouteRouteSubsystem,'sfpsL4CPIPRouteDeviceID':sfpsL4CPIPRouteDeviceID,'sfpsL4CPIPRouteDeviceName':sfpsL4CPIPRouteDeviceName,'sfpsL4CPIPRouteMACAddress':sfpsL4CPIPRouteMACAddress,'sfpsL4CPIPRouteMetric':sfpsL4CPIPRouteMetric,'sfpsL4CPIPRouteCallable':sfpsL4CPIPRouteCallable,'sfpsL4CPPortTable':sfpsL4CPPortTable,'sfpsL4CPPortEntry':sfpsL4CPPortEntry,_Y:sfpsL4CPPortNum,'sfpsL4CPPortID':sfpsL4CPPortID,'sfpsL4CPPortApplyPolicyIn':sfpsL4CPPortApplyPolicyIn,'sfpsL4CPPortApplyPolicyOut':sfpsL4CPPortApplyPolicyOut,'sfpsL4CPPortDefaultUserID':sfpsL4CPPortDefaultUserID,'sfpsL4CPPortDefaultUserName':sfpsL4CPPortDefaultUserName,'sfpsL4CPCallableDeviceTable':sfpsL4CPCallableDeviceTable,'sfpsL4CPCallableDeviceEntry':sfpsL4CPCallableDeviceEntry,_Z:sfpsL4CPCallableDeviceDeviceID,'sfpsL4CPCallableDeviceDeviceName':sfpsL4CPCallableDeviceDeviceName,'sfpsL4CPCallableDeviceDefaultUserName':sfpsL4CPCallableDeviceDefaultUserName,'sfpsL4CDR':sfpsL4CDR,'l4cdrStats':l4cdrStats,'l4cdrConfig':l4cdrConfig,'l4cdrActions':l4cdrActions,'sfpsL4CDRActiveFlowTable':sfpsL4CDRActiveFlowTable,'sfpsL4CDRActiveFlowEntry':sfpsL4CDRActiveFlowEntry,_a:sfpsL4CDRActiveFlowFlowID,'sfpsL4CDRActiveFlowSubProtocol':sfpsL4CDRActiveFlowSubProtocol,'sfpsL4CDRActiveFlowEtherType':sfpsL4CDRActiveFlowEtherType,'sfpsL4CDRActiveFlowSourceUser':sfpsL4CDRActiveFlowSourceUser,'sfpsL4CDRActiveFlowSourceMACAddr':sfpsL4CDRActiveFlowSourceMACAddr,'sfpsL4CDRActiveFlowSourceNetAddr':sfpsL4CDRActiveFlowSourceNetAddr,'sfpsL4CDRActiveFlowSourceProtocolPort':sfpsL4CDRActiveFlowSourceProtocolPort,'sfpsL4CDRActiveFlowSourcePPRangeEnabled':sfpsL4CDRActiveFlowSourcePPRangeEnabled,'sfpsL4CDRActiveFlowSourceConnNumber':sfpsL4CDRActiveFlowSourceConnNumber,'sfpsL4CDRActiveFlowDestUser':sfpsL4CDRActiveFlowDestUser,'sfpsL4CDRActiveFlowDestMACAddr':sfpsL4CDRActiveFlowDestMACAddr,'sfpsL4CDRActiveFlowDestNetAddr':sfpsL4CDRActiveFlowDestNetAddr,'sfpsL4CDRActiveFlowDestProtocolPort':sfpsL4CDRActiveFlowDestProtocolPort,'sfpsL4CDRActiveFlowDestPPRangeEnabled':sfpsL4CDRActiveFlowDestPPRangeEnabled,'sfpsL4CDRActiveFlowDestConnNumber':sfpsL4CDRActiveFlowDestConnNumber,'sfpsL4CDRActiveFlowStartTime':sfpsL4CDRActiveFlowStartTime,'sfpsL4CDRActiveFlowLastPktTime':sfpsL4CDRActiveFlowLastPktTime,'sfpsL4CDRActiveFlowEndTime':sfpsL4CDRActiveFlowEndTime,'sfpsL4CDRActiveFlowInOctets':sfpsL4CDRActiveFlowInOctets,'sfpsL4CDRActiveFlowOutOctets':sfpsL4CDRActiveFlowOutOctets,'sfpsL4CDRActiveFlowInPkts':sfpsL4CDRActiveFlowInPkts,'sfpsL4CDRActiveFlowOutPkts':sfpsL4CDRActiveFlowOutPkts,'sfpsL4CDRActiveFlowDemandAccessConnMade':sfpsL4CDRActiveFlowDemandAccessConnMade,'sfpsL4CDRActiveFlowFlowRecordState':sfpsL4CDRActiveFlowFlowRecordState,'sfpsL4CDRTermedFlowTable':sfpsL4CDRTermedFlowTable,'sfpsL4CDRTermedFlowEntry':sfpsL4CDRTermedFlowEntry,_b:sfpsL4CDRTermedFlowFlowID,'sfpsL4CDRTermedFlowSubProtocol':sfpsL4CDRTermedFlowSubProtocol,'sfpsL4CDRTermedFlowEtherType':sfpsL4CDRTermedFlowEtherType,'sfpsL4CDRTermedFlowSourceUser':sfpsL4CDRTermedFlowSourceUser,'sfpsL4CDRTermedFlowSourceMACAddr':sfpsL4CDRTermedFlowSourceMACAddr,'sfpsL4CDRTermedFlowSourceNetAddr':sfpsL4CDRTermedFlowSourceNetAddr,'sfpsL4CDRTermedFlowSourceProtocolPort':sfpsL4CDRTermedFlowSourceProtocolPort,'sfpsL4CDRTermedFlowSourcePPRangeEnabled':sfpsL4CDRTermedFlowSourcePPRangeEnabled,'sfpsL4CDRTermedFlowSourceConnNumber':sfpsL4CDRTermedFlowSourceConnNumber,'sfpsL4CDRTermedFlowDestUser':sfpsL4CDRTermedFlowDestUser,'sfpsL4CDRTermedFlowDestMACAddr':sfpsL4CDRTermedFlowDestMACAddr,'sfpsL4CDRTermedFlowDestNetAddr':sfpsL4CDRTermedFlowDestNetAddr,'sfpsL4CDRTermedFlowDestProtocolPort':sfpsL4CDRTermedFlowDestProtocolPort,'sfpsL4CDRTermedFlowDestPPRangeEnabled':sfpsL4CDRTermedFlowDestPPRangeEnabled,'sfpsL4CDRTermedFlowDestConnNumber':sfpsL4CDRTermedFlowDestConnNumber,'sfpsL4CDRTermedFlowStartTime':sfpsL4CDRTermedFlowStartTime,'sfpsL4CDRTermedFlowLastPktTime':sfpsL4CDRTermedFlowLastPktTime,'sfpsL4CDRTermedFlowEndTime':sfpsL4CDRTermedFlowEndTime,'sfpsL4CDRTermedFlowInOctets':sfpsL4CDRTermedFlowInOctets,'sfpsL4CDRTermedFlowOutOctets':sfpsL4CDRTermedFlowOutOctets,'sfpsL4CDRTermedFlowInPkts':sfpsL4CDRTermedFlowInPkts,'sfpsL4CDRTermedFlowOutPkts':sfpsL4CDRTermedFlowOutPkts,'sfpsL4CDRTermedFlowDemandAccessConnMade':sfpsL4CDRTermedFlowDemandAccessConnMade,'sfpsL4CDRTermedFlowFlowRecordState':sfpsL4CDRTermedFlowFlowRecordState,'sfpsL4CDRFlowIndexTable':sfpsL4CDRFlowIndexTable,'sfpsL4CDRFlowIndexEntry':sfpsL4CDRFlowIndexEntry,_c:sfpsL4CDRFlowIndexFlowID,'sfpsL4CDRFlowIndexSFPSFlowTblIndex':sfpsL4CDRFlowIndexSFPSFlowTblIndex,'sfpsL4CDRFlowIndexSFlowStatsPtr':sfpsL4CDRFlowIndexSFlowStatsPtr,'sfpsL4CDRFlowIndexStaticFlowInfoPtr':sfpsL4CDRFlowIndexStaticFlowInfoPtr,'sfpsL4CDRFlowIndexFlowTblEntryPtr':sfpsL4CDRFlowIndexFlowTblEntryPtr,'sfpsL4CDRFlowIndexFlowState':sfpsL4CDRFlowIndexFlowState})