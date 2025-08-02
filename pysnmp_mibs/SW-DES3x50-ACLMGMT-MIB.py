_c='swACLPayloadRuleAccessID'
_b='swACLPayloadRuleProfileID'
_a='swACLIpRuleAccessID'
_Z='swACLIpRuleProfileID'
_Y='swACLEtherRuleAccessID'
_X='swACLEtherRuleProfileID'
_W='swACLPayloadProfileID'
_V='dst-src-addr'
_U='src-addr'
_T='dst-addr'
_S='disable'
_R='enable'
_Q='protocolId'
_P='swACLIpProfileID'
_O='swACLEthernetProfileID'
_N='deny'
_M='permit'
_L='none'
_K='SnmpAdminString'
_J='other'
_I='PortList'
_H='read-only'
_G='SW-DES3x50-ACLMGMT-MIB'
_F='disabled'
_E='enabled'
_D='OctetString'
_C='Integer32'
_B='read-create'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_D,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dlink_mgmt,=mibBuilder.importSymbols('DLINK-ID-REC-MIB','dlink-mgmt')
PortList,=mibBuilder.importSymbols('Q-BRIDGE-MIB',_I)
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_K)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention')
swAclMgmtMIB=ModuleIdentity((1,3,6,1,4,1,171,11,5))
_SwAclMaskMgmt_ObjectIdentity=ObjectIdentity
swAclMaskMgmt=_SwAclMaskMgmt_ObjectIdentity((1,3,6,1,4,1,171,11,5,1))
_SwACLEthernetTable_Object=MibTable
swACLEthernetTable=_SwACLEthernetTable_Object((1,3,6,1,4,1,171,11,5,1,1))
if mibBuilder.loadTexts:swACLEthernetTable.setStatus(_A)
_SwACLEthernetEntry_Object=MibTableRow
swACLEthernetEntry=_SwACLEthernetEntry_Object((1,3,6,1,4,1,171,11,5,1,1,1))
swACLEthernetEntry.setIndexNames((0,_G,_O))
if mibBuilder.loadTexts:swACLEthernetEntry.setStatus(_A)
class _SwACLEthernetProfileID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_SwACLEthernetProfileID_Type.__name__=_C
_SwACLEthernetProfileID_Object=MibTableColumn
swACLEthernetProfileID=_SwACLEthernetProfileID_Object((1,3,6,1,4,1,171,11,5,1,1,1,1),_SwACLEthernetProfileID_Type())
swACLEthernetProfileID.setMaxAccess(_H)
if mibBuilder.loadTexts:swACLEthernetProfileID.setStatus(_A)
class _SwACLEthernetUsevlan_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_SwACLEthernetUsevlan_Type.__name__=_C
_SwACLEthernetUsevlan_Object=MibTableColumn
swACLEthernetUsevlan=_SwACLEthernetUsevlan_Object((1,3,6,1,4,1,171,11,5,1,1,1,2),_SwACLEthernetUsevlan_Type())
swACLEthernetUsevlan.setMaxAccess(_B)
if mibBuilder.loadTexts:swACLEthernetUsevlan.setStatus(_A)
class _SwACLEthernetMacAddrMaskState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_J,1),('dst-mac-addr',2),('src-mac-addr',3),('dst-src-mac-addr',4)))
_SwACLEthernetMacAddrMaskState_Type.__name__=_C
_SwACLEthernetMacAddrMaskState_Object=MibTableColumn
swACLEthernetMacAddrMaskState=_SwACLEthernetMacAddrMaskState_Object((1,3,6,1,4,1,171,11,5,1,1,1,3),_SwACLEthernetMacAddrMaskState_Type())
swACLEthernetMacAddrMaskState.setMaxAccess(_B)
if mibBuilder.loadTexts:swACLEthernetMacAddrMaskState.setStatus(_A)
_SwACLEthernetSrcMacAddrMask_Type=MacAddress
_SwACLEthernetSrcMacAddrMask_Object=MibTableColumn
swACLEthernetSrcMacAddrMask=_SwACLEthernetSrcMacAddrMask_Object((1,3,6,1,4,1,171,11,5,1,1,1,4),_SwACLEthernetSrcMacAddrMask_Type())
swACLEthernetSrcMacAddrMask.setMaxAccess(_B)
if mibBuilder.loadTexts:swACLEthernetSrcMacAddrMask.setStatus(_A)
_SwACLEthernetDstMacAddrMask_Type=MacAddress
_SwACLEthernetDstMacAddrMask_Object=MibTableColumn
swACLEthernetDstMacAddrMask=_SwACLEthernetDstMacAddrMask_Object((1,3,6,1,4,1,171,11,5,1,1,1,5),_SwACLEthernetDstMacAddrMask_Type())
swACLEthernetDstMacAddrMask.setMaxAccess(_B)
if mibBuilder.loadTexts:swACLEthernetDstMacAddrMask.setStatus(_A)
class _SwACLEthernetUse8021p_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_SwACLEthernetUse8021p_Type.__name__=_C
_SwACLEthernetUse8021p_Object=MibTableColumn
swACLEthernetUse8021p=_SwACLEthernetUse8021p_Object((1,3,6,1,4,1,171,11,5,1,1,1,6),_SwACLEthernetUse8021p_Type())
swACLEthernetUse8021p.setMaxAccess(_B)
if mibBuilder.loadTexts:swACLEthernetUse8021p.setStatus(_A)
class _SwACLEthernetUseEthernetType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_SwACLEthernetUseEthernetType_Type.__name__=_C
_SwACLEthernetUseEthernetType_Object=MibTableColumn
swACLEthernetUseEthernetType=_SwACLEthernetUseEthernetType_Object((1,3,6,1,4,1,171,11,5,1,1,1,7),_SwACLEthernetUseEthernetType_Type())
swACLEthernetUseEthernetType.setMaxAccess(_B)
if mibBuilder.loadTexts:swACLEthernetUseEthernetType.setStatus(_A)
class _SwACLEthernetPort_Type(PortList):subtypeSpec=PortList.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_SwACLEthernetPort_Type.__name__=_I
_SwACLEthernetPort_Object=MibTableColumn
swACLEthernetPort=_SwACLEthernetPort_Object((1,3,6,1,4,1,171,11,5,1,1,1,8),_SwACLEthernetPort_Type())
swACLEthernetPort.setMaxAccess(_B)
if mibBuilder.loadTexts:swACLEthernetPort.setStatus(_A)
_SwACLEthernetRowStatus_Type=RowStatus
_SwACLEthernetRowStatus_Object=MibTableColumn
swACLEthernetRowStatus=_SwACLEthernetRowStatus_Object((1,3,6,1,4,1,171,11,5,1,1,1,9),_SwACLEthernetRowStatus_Type())
swACLEthernetRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:swACLEthernetRowStatus.setStatus(_A)
_SwACLIpTable_Object=MibTable
swACLIpTable=_SwACLIpTable_Object((1,3,6,1,4,1,171,11,5,1,2))
if mibBuilder.loadTexts:swACLIpTable.setStatus(_A)
_SwACLIpEntry_Object=MibTableRow
swACLIpEntry=_SwACLIpEntry_Object((1,3,6,1,4,1,171,11,5,1,2,1))
swACLIpEntry.setIndexNames((0,_G,_P))
if mibBuilder.loadTexts:swACLIpEntry.setStatus(_A)
class _SwACLIpProfileID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_SwACLIpProfileID_Type.__name__=_C
_SwACLIpProfileID_Object=MibTableColumn
swACLIpProfileID=_SwACLIpProfileID_Object((1,3,6,1,4,1,171,11,5,1,2,1,1),_SwACLIpProfileID_Type())
swACLIpProfileID.setMaxAccess(_H)
if mibBuilder.loadTexts:swACLIpProfileID.setStatus(_A)
class _SwACLIpUsevlan_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_SwACLIpUsevlan_Type.__name__=_C
_SwACLIpUsevlan_Object=MibTableColumn
swACLIpUsevlan=_SwACLIpUsevlan_Object((1,3,6,1,4,1,171,11,5,1,2,1,2),_SwACLIpUsevlan_Type())
swACLIpUsevlan.setMaxAccess(_B)
if mibBuilder.loadTexts:swACLIpUsevlan.setStatus(_A)
class _SwACLIpIpAddrMaskState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_J,1),('dst-ip-addr',2),('src-ip-addr',3),('dst-src-ip-addr',4)))
_SwACLIpIpAddrMaskState_Type.__name__=_C
_SwACLIpIpAddrMaskState_Object=MibTableColumn
swACLIpIpAddrMaskState=_SwACLIpIpAddrMaskState_Object((1,3,6,1,4,1,171,11,5,1,2,1,3),_SwACLIpIpAddrMaskState_Type())
swACLIpIpAddrMaskState.setMaxAccess(_B)
if mibBuilder.loadTexts:swACLIpIpAddrMaskState.setStatus(_A)
_SwACLIpSrcIpAddrMask_Type=IpAddress
_SwACLIpSrcIpAddrMask_Object=MibTableColumn
swACLIpSrcIpAddrMask=_SwACLIpSrcIpAddrMask_Object((1,3,6,1,4,1,171,11,5,1,2,1,4),_SwACLIpSrcIpAddrMask_Type())
swACLIpSrcIpAddrMask.setMaxAccess(_B)
if mibBuilder.loadTexts:swACLIpSrcIpAddrMask.setStatus(_A)
_SwACLIpDstIpAddrMask_Type=IpAddress
_SwACLIpDstIpAddrMask_Object=MibTableColumn
swACLIpDstIpAddrMask=_SwACLIpDstIpAddrMask_Object((1,3,6,1,4,1,171,11,5,1,2,1,5),_SwACLIpDstIpAddrMask_Type())
swACLIpDstIpAddrMask.setMaxAccess(_B)
if mibBuilder.loadTexts:swACLIpDstIpAddrMask.setStatus(_A)
class _SwACLIpUseDSCP_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_SwACLIpUseDSCP_Type.__name__=_C
_SwACLIpUseDSCP_Object=MibTableColumn
swACLIpUseDSCP=_SwACLIpUseDSCP_Object((1,3,6,1,4,1,171,11,5,1,2,1,6),_SwACLIpUseDSCP_Type())
swACLIpUseDSCP.setMaxAccess(_B)
if mibBuilder.loadTexts:swACLIpUseDSCP.setStatus(_A)
class _SwACLIpUseProtoType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_L,1),('icmp',2),('igmp',3),('tcp',4),('udp',5),(_Q,6)))
_SwACLIpUseProtoType_Type.__name__=_C
_SwACLIpUseProtoType_Object=MibTableColumn
swACLIpUseProtoType=_SwACLIpUseProtoType_Object((1,3,6,1,4,1,171,11,5,1,2,1,7),_SwACLIpUseProtoType_Type())
swACLIpUseProtoType.setMaxAccess(_B)
if mibBuilder.loadTexts:swACLIpUseProtoType.setStatus(_A)
class _SwACLIpIcmpOption_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_L,1),('type',2),('code',3),('type-code',4)))
_SwACLIpIcmpOption_Type.__name__=_C
_SwACLIpIcmpOption_Object=MibTableColumn
swACLIpIcmpOption=_SwACLIpIcmpOption_Object((1,3,6,1,4,1,171,11,5,1,2,1,8),_SwACLIpIcmpOption_Type())
swACLIpIcmpOption.setMaxAccess(_B)
if mibBuilder.loadTexts:swACLIpIcmpOption.setStatus(_A)
class _SwACLIpIgmpOption_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_R,1),(_S,2)))
_SwACLIpIgmpOption_Type.__name__=_C
_SwACLIpIgmpOption_Object=MibTableColumn
swACLIpIgmpOption=_SwACLIpIgmpOption_Object((1,3,6,1,4,1,171,11,5,1,2,1,9),_SwACLIpIgmpOption_Type())
swACLIpIgmpOption.setMaxAccess(_B)
if mibBuilder.loadTexts:swACLIpIgmpOption.setStatus(_A)
class _SwACLIpTcpOption_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_J,1),(_T,2),(_U,3),(_V,4)))
_SwACLIpTcpOption_Type.__name__=_C
_SwACLIpTcpOption_Object=MibTableColumn
swACLIpTcpOption=_SwACLIpTcpOption_Object((1,3,6,1,4,1,171,11,5,1,2,1,10),_SwACLIpTcpOption_Type())
swACLIpTcpOption.setMaxAccess(_B)
if mibBuilder.loadTexts:swACLIpTcpOption.setStatus(_A)
class _SwACLIpUdpOption_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_J,1),(_T,2),(_U,3),(_V,4)))
_SwACLIpUdpOption_Type.__name__=_C
_SwACLIpUdpOption_Object=MibTableColumn
swACLIpUdpOption=_SwACLIpUdpOption_Object((1,3,6,1,4,1,171,11,5,1,2,1,11),_SwACLIpUdpOption_Type())
swACLIpUdpOption.setMaxAccess(_B)
if mibBuilder.loadTexts:swACLIpUdpOption.setStatus(_A)
class _SwACLIpTCPorUDPSrcPortMask_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,2));fixedLength=2
_SwACLIpTCPorUDPSrcPortMask_Type.__name__=_D
_SwACLIpTCPorUDPSrcPortMask_Object=MibTableColumn
swACLIpTCPorUDPSrcPortMask=_SwACLIpTCPorUDPSrcPortMask_Object((1,3,6,1,4,1,171,11,5,1,2,1,12),_SwACLIpTCPorUDPSrcPortMask_Type())
swACLIpTCPorUDPSrcPortMask.setMaxAccess(_B)
if mibBuilder.loadTexts:swACLIpTCPorUDPSrcPortMask.setStatus(_A)
class _SwACLIpTCPorUDPDstPortMask_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,2));fixedLength=2
_SwACLIpTCPorUDPDstPortMask_Type.__name__=_D
_SwACLIpTCPorUDPDstPortMask_Object=MibTableColumn
swACLIpTCPorUDPDstPortMask=_SwACLIpTCPorUDPDstPortMask_Object((1,3,6,1,4,1,171,11,5,1,2,1,13),_SwACLIpTCPorUDPDstPortMask_Type())
swACLIpTCPorUDPDstPortMask.setMaxAccess(_B)
if mibBuilder.loadTexts:swACLIpTCPorUDPDstPortMask.setStatus(_A)
class _SwACLIpTCPFlagBit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
_SwACLIpTCPFlagBit_Type.__name__=_C
_SwACLIpTCPFlagBit_Object=MibTableColumn
swACLIpTCPFlagBit=_SwACLIpTCPFlagBit_Object((1,3,6,1,4,1,171,11,5,1,2,1,14),_SwACLIpTCPFlagBit_Type())
swACLIpTCPFlagBit.setMaxAccess(_B)
if mibBuilder.loadTexts:swACLIpTCPFlagBit.setStatus(_A)
class _SwACLIpProtoIDOption_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_R,1),(_S,2)))
_SwACLIpProtoIDOption_Type.__name__=_C
_SwACLIpProtoIDOption_Object=MibTableColumn
swACLIpProtoIDOption=_SwACLIpProtoIDOption_Object((1,3,6,1,4,1,171,11,5,1,2,1,15),_SwACLIpProtoIDOption_Type())
swACLIpProtoIDOption.setMaxAccess(_B)
if mibBuilder.loadTexts:swACLIpProtoIDOption.setStatus(_A)
class _SwACLIpProtoIDMask_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
_SwACLIpProtoIDMask_Type.__name__=_D
_SwACLIpProtoIDMask_Object=MibTableColumn
swACLIpProtoIDMask=_SwACLIpProtoIDMask_Object((1,3,6,1,4,1,171,11,5,1,2,1,16),_SwACLIpProtoIDMask_Type())
swACLIpProtoIDMask.setMaxAccess(_B)
if mibBuilder.loadTexts:swACLIpProtoIDMask.setStatus(_A)
class _SwACLIpPort_Type(PortList):subtypeSpec=PortList.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_SwACLIpPort_Type.__name__=_I
_SwACLIpPort_Object=MibTableColumn
swACLIpPort=_SwACLIpPort_Object((1,3,6,1,4,1,171,11,5,1,2,1,17),_SwACLIpPort_Type())
swACLIpPort.setMaxAccess(_B)
if mibBuilder.loadTexts:swACLIpPort.setStatus(_A)
_SwACLIpRowStatus_Type=RowStatus
_SwACLIpRowStatus_Object=MibTableColumn
swACLIpRowStatus=_SwACLIpRowStatus_Object((1,3,6,1,4,1,171,11,5,1,2,1,18),_SwACLIpRowStatus_Type())
swACLIpRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:swACLIpRowStatus.setStatus(_A)
_SwACLPayloadTable_Object=MibTable
swACLPayloadTable=_SwACLPayloadTable_Object((1,3,6,1,4,1,171,11,5,1,3))
if mibBuilder.loadTexts:swACLPayloadTable.setStatus(_A)
_SwACLPayloadEntry_Object=MibTableRow
swACLPayloadEntry=_SwACLPayloadEntry_Object((1,3,6,1,4,1,171,11,5,1,3,1))
swACLPayloadEntry.setIndexNames((0,_G,_W))
if mibBuilder.loadTexts:swACLPayloadEntry.setStatus(_A)
class _SwACLPayloadProfileID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_SwACLPayloadProfileID_Type.__name__=_C
_SwACLPayloadProfileID_Object=MibTableColumn
swACLPayloadProfileID=_SwACLPayloadProfileID_Object((1,3,6,1,4,1,171,11,5,1,3,1,1),_SwACLPayloadProfileID_Type())
swACLPayloadProfileID.setMaxAccess(_H)
if mibBuilder.loadTexts:swACLPayloadProfileID.setStatus(_A)
class _SwACLPayloadOffSet0to15_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,16));fixedLength=16
_SwACLPayloadOffSet0to15_Type.__name__=_D
_SwACLPayloadOffSet0to15_Object=MibTableColumn
swACLPayloadOffSet0to15=_SwACLPayloadOffSet0to15_Object((1,3,6,1,4,1,171,11,5,1,3,1,2),_SwACLPayloadOffSet0to15_Type())
swACLPayloadOffSet0to15.setMaxAccess(_B)
if mibBuilder.loadTexts:swACLPayloadOffSet0to15.setStatus(_A)
class _SwACLPayloadOffSet16to31_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,16));fixedLength=16
_SwACLPayloadOffSet16to31_Type.__name__=_D
_SwACLPayloadOffSet16to31_Object=MibTableColumn
swACLPayloadOffSet16to31=_SwACLPayloadOffSet16to31_Object((1,3,6,1,4,1,171,11,5,1,3,1,3),_SwACLPayloadOffSet16to31_Type())
swACLPayloadOffSet16to31.setMaxAccess(_B)
if mibBuilder.loadTexts:swACLPayloadOffSet16to31.setStatus(_A)
class _SwACLPayloadOffSet32to47_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,16));fixedLength=16
_SwACLPayloadOffSet32to47_Type.__name__=_D
_SwACLPayloadOffSet32to47_Object=MibTableColumn
swACLPayloadOffSet32to47=_SwACLPayloadOffSet32to47_Object((1,3,6,1,4,1,171,11,5,1,3,1,4),_SwACLPayloadOffSet32to47_Type())
swACLPayloadOffSet32to47.setMaxAccess(_B)
if mibBuilder.loadTexts:swACLPayloadOffSet32to47.setStatus(_A)
class _SwACLPayloadOffSet48to63_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,16));fixedLength=16
_SwACLPayloadOffSet48to63_Type.__name__=_D
_SwACLPayloadOffSet48to63_Object=MibTableColumn
swACLPayloadOffSet48to63=_SwACLPayloadOffSet48to63_Object((1,3,6,1,4,1,171,11,5,1,3,1,5),_SwACLPayloadOffSet48to63_Type())
swACLPayloadOffSet48to63.setMaxAccess(_B)
if mibBuilder.loadTexts:swACLPayloadOffSet48to63.setStatus(_A)
class _SwACLPayloadOffSet64to79_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,16));fixedLength=16
_SwACLPayloadOffSet64to79_Type.__name__=_D
_SwACLPayloadOffSet64to79_Object=MibTableColumn
swACLPayloadOffSet64to79=_SwACLPayloadOffSet64to79_Object((1,3,6,1,4,1,171,11,5,1,3,1,6),_SwACLPayloadOffSet64to79_Type())
swACLPayloadOffSet64to79.setMaxAccess(_B)
if mibBuilder.loadTexts:swACLPayloadOffSet64to79.setStatus(_A)
class _SwACLPayloadPort_Type(PortList):subtypeSpec=PortList.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_SwACLPayloadPort_Type.__name__=_I
_SwACLPayloadPort_Object=MibTableColumn
swACLPayloadPort=_SwACLPayloadPort_Object((1,3,6,1,4,1,171,11,5,1,3,1,7),_SwACLPayloadPort_Type())
swACLPayloadPort.setMaxAccess(_B)
if mibBuilder.loadTexts:swACLPayloadPort.setStatus(_A)
_SwACLPayloadRowStatus_Type=RowStatus
_SwACLPayloadRowStatus_Object=MibTableColumn
swACLPayloadRowStatus=_SwACLPayloadRowStatus_Object((1,3,6,1,4,1,171,11,5,1,3,1,8),_SwACLPayloadRowStatus_Type())
swACLPayloadRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:swACLPayloadRowStatus.setStatus(_A)
_SwAclRuleMgmt_ObjectIdentity=ObjectIdentity
swAclRuleMgmt=_SwAclRuleMgmt_ObjectIdentity((1,3,6,1,4,1,171,11,5,2))
_SwACLEtherRuleTable_Object=MibTable
swACLEtherRuleTable=_SwACLEtherRuleTable_Object((1,3,6,1,4,1,171,11,5,2,1))
if mibBuilder.loadTexts:swACLEtherRuleTable.setStatus(_A)
_SwACLEtherRuleEntry_Object=MibTableRow
swACLEtherRuleEntry=_SwACLEtherRuleEntry_Object((1,3,6,1,4,1,171,11,5,2,1,1))
swACLEtherRuleEntry.setIndexNames((0,_G,_X),(0,_G,_Y))
if mibBuilder.loadTexts:swACLEtherRuleEntry.setStatus(_A)
class _SwACLEtherRuleProfileID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_SwACLEtherRuleProfileID_Type.__name__=_C
_SwACLEtherRuleProfileID_Object=MibTableColumn
swACLEtherRuleProfileID=_SwACLEtherRuleProfileID_Object((1,3,6,1,4,1,171,11,5,2,1,1,1),_SwACLEtherRuleProfileID_Type())
swACLEtherRuleProfileID.setMaxAccess(_H)
if mibBuilder.loadTexts:swACLEtherRuleProfileID.setStatus(_A)
class _SwACLEtherRuleAccessID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_SwACLEtherRuleAccessID_Type.__name__=_C
_SwACLEtherRuleAccessID_Object=MibTableColumn
swACLEtherRuleAccessID=_SwACLEtherRuleAccessID_Object((1,3,6,1,4,1,171,11,5,2,1,1,2),_SwACLEtherRuleAccessID_Type())
swACLEtherRuleAccessID.setMaxAccess(_H)
if mibBuilder.loadTexts:swACLEtherRuleAccessID.setStatus(_A)
class _SwACLEtherRuleVlan_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_SwACLEtherRuleVlan_Type.__name__=_K
_SwACLEtherRuleVlan_Object=MibTableColumn
swACLEtherRuleVlan=_SwACLEtherRuleVlan_Object((1,3,6,1,4,1,171,11,5,2,1,1,3),_SwACLEtherRuleVlan_Type())
swACLEtherRuleVlan.setMaxAccess(_B)
if mibBuilder.loadTexts:swACLEtherRuleVlan.setStatus(_A)
_SwACLEtherRuleSrcMacAddress_Type=MacAddress
_SwACLEtherRuleSrcMacAddress_Object=MibTableColumn
swACLEtherRuleSrcMacAddress=_SwACLEtherRuleSrcMacAddress_Object((1,3,6,1,4,1,171,11,5,2,1,1,4),_SwACLEtherRuleSrcMacAddress_Type())
swACLEtherRuleSrcMacAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:swACLEtherRuleSrcMacAddress.setStatus(_A)
_SwACLEtherRuleDstMacAddress_Type=MacAddress
_SwACLEtherRuleDstMacAddress_Object=MibTableColumn
swACLEtherRuleDstMacAddress=_SwACLEtherRuleDstMacAddress_Object((1,3,6,1,4,1,171,11,5,2,1,1,5),_SwACLEtherRuleDstMacAddress_Type())
swACLEtherRuleDstMacAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:swACLEtherRuleDstMacAddress.setStatus(_A)
class _SwACLEtherRule8021P_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_SwACLEtherRule8021P_Type.__name__=_C
_SwACLEtherRule8021P_Object=MibTableColumn
swACLEtherRule8021P=_SwACLEtherRule8021P_Object((1,3,6,1,4,1,171,11,5,2,1,1,6),_SwACLEtherRule8021P_Type())
swACLEtherRule8021P.setMaxAccess(_B)
if mibBuilder.loadTexts:swACLEtherRule8021P.setStatus(_A)
class _SwACLEtherRuleEtherType_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,2));fixedLength=2
_SwACLEtherRuleEtherType_Type.__name__=_D
_SwACLEtherRuleEtherType_Object=MibTableColumn
swACLEtherRuleEtherType=_SwACLEtherRuleEtherType_Object((1,3,6,1,4,1,171,11,5,2,1,1,7),_SwACLEtherRuleEtherType_Type())
swACLEtherRuleEtherType.setMaxAccess(_B)
if mibBuilder.loadTexts:swACLEtherRuleEtherType.setStatus(_A)
class _SwACLEtherRuleEnablePriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_SwACLEtherRuleEnablePriority_Type.__name__=_C
_SwACLEtherRuleEnablePriority_Object=MibTableColumn
swACLEtherRuleEnablePriority=_SwACLEtherRuleEnablePriority_Object((1,3,6,1,4,1,171,11,5,2,1,1,8),_SwACLEtherRuleEnablePriority_Type())
swACLEtherRuleEnablePriority.setMaxAccess(_B)
if mibBuilder.loadTexts:swACLEtherRuleEnablePriority.setStatus(_A)
class _SwACLEtherRulePriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_SwACLEtherRulePriority_Type.__name__=_C
_SwACLEtherRulePriority_Object=MibTableColumn
swACLEtherRulePriority=_SwACLEtherRulePriority_Object((1,3,6,1,4,1,171,11,5,2,1,1,9),_SwACLEtherRulePriority_Type())
swACLEtherRulePriority.setMaxAccess(_B)
if mibBuilder.loadTexts:swACLEtherRulePriority.setStatus(_A)
class _SwACLEtherRuleReplacePriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_SwACLEtherRuleReplacePriority_Type.__name__=_C
_SwACLEtherRuleReplacePriority_Object=MibTableColumn
swACLEtherRuleReplacePriority=_SwACLEtherRuleReplacePriority_Object((1,3,6,1,4,1,171,11,5,2,1,1,10),_SwACLEtherRuleReplacePriority_Type())
swACLEtherRuleReplacePriority.setMaxAccess(_B)
if mibBuilder.loadTexts:swACLEtherRuleReplacePriority.setStatus(_A)
class _SwACLEtherRuleEnableReplaceDscp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_SwACLEtherRuleEnableReplaceDscp_Type.__name__=_C
_SwACLEtherRuleEnableReplaceDscp_Object=MibTableColumn
swACLEtherRuleEnableReplaceDscp=_SwACLEtherRuleEnableReplaceDscp_Object((1,3,6,1,4,1,171,11,5,2,1,1,11),_SwACLEtherRuleEnableReplaceDscp_Type())
swACLEtherRuleEnableReplaceDscp.setMaxAccess(_B)
if mibBuilder.loadTexts:swACLEtherRuleEnableReplaceDscp.setStatus(_A)
class _SwACLEtherRuleRepDscp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
_SwACLEtherRuleRepDscp_Type.__name__=_C
_SwACLEtherRuleRepDscp_Object=MibTableColumn
swACLEtherRuleRepDscp=_SwACLEtherRuleRepDscp_Object((1,3,6,1,4,1,171,11,5,2,1,1,12),_SwACLEtherRuleRepDscp_Type())
swACLEtherRuleRepDscp.setMaxAccess(_B)
if mibBuilder.loadTexts:swACLEtherRuleRepDscp.setStatus(_A)
class _SwACLEtherRulePermit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_M,1),(_N,2)))
_SwACLEtherRulePermit_Type.__name__=_C
_SwACLEtherRulePermit_Object=MibTableColumn
swACLEtherRulePermit=_SwACLEtherRulePermit_Object((1,3,6,1,4,1,171,11,5,2,1,1,13),_SwACLEtherRulePermit_Type())
swACLEtherRulePermit.setMaxAccess(_B)
if mibBuilder.loadTexts:swACLEtherRulePermit.setStatus(_A)
_SwACLEtherRuleRowStatus_Type=RowStatus
_SwACLEtherRuleRowStatus_Object=MibTableColumn
swACLEtherRuleRowStatus=_SwACLEtherRuleRowStatus_Object((1,3,6,1,4,1,171,11,5,2,1,1,14),_SwACLEtherRuleRowStatus_Type())
swACLEtherRuleRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:swACLEtherRuleRowStatus.setStatus(_A)
_SwACLIpRuleTable_Object=MibTable
swACLIpRuleTable=_SwACLIpRuleTable_Object((1,3,6,1,4,1,171,11,5,2,2))
if mibBuilder.loadTexts:swACLIpRuleTable.setStatus(_A)
_SwACLIpRuleEntry_Object=MibTableRow
swACLIpRuleEntry=_SwACLIpRuleEntry_Object((1,3,6,1,4,1,171,11,5,2,2,1))
swACLIpRuleEntry.setIndexNames((0,_G,_Z),(0,_G,_a))
if mibBuilder.loadTexts:swACLIpRuleEntry.setStatus(_A)
class _SwACLIpRuleProfileID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_SwACLIpRuleProfileID_Type.__name__=_C
_SwACLIpRuleProfileID_Object=MibTableColumn
swACLIpRuleProfileID=_SwACLIpRuleProfileID_Object((1,3,6,1,4,1,171,11,5,2,2,1,1),_SwACLIpRuleProfileID_Type())
swACLIpRuleProfileID.setMaxAccess(_H)
if mibBuilder.loadTexts:swACLIpRuleProfileID.setStatus(_A)
class _SwACLIpRuleAccessID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_SwACLIpRuleAccessID_Type.__name__=_C
_SwACLIpRuleAccessID_Object=MibTableColumn
swACLIpRuleAccessID=_SwACLIpRuleAccessID_Object((1,3,6,1,4,1,171,11,5,2,2,1,2),_SwACLIpRuleAccessID_Type())
swACLIpRuleAccessID.setMaxAccess(_H)
if mibBuilder.loadTexts:swACLIpRuleAccessID.setStatus(_A)
class _SwACLIpRuleVlan_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_SwACLIpRuleVlan_Type.__name__=_K
_SwACLIpRuleVlan_Object=MibTableColumn
swACLIpRuleVlan=_SwACLIpRuleVlan_Object((1,3,6,1,4,1,171,11,5,2,2,1,3),_SwACLIpRuleVlan_Type())
swACLIpRuleVlan.setMaxAccess(_B)
if mibBuilder.loadTexts:swACLIpRuleVlan.setStatus(_A)
_SwACLIpRuleSrcIpaddress_Type=IpAddress
_SwACLIpRuleSrcIpaddress_Object=MibTableColumn
swACLIpRuleSrcIpaddress=_SwACLIpRuleSrcIpaddress_Object((1,3,6,1,4,1,171,11,5,2,2,1,4),_SwACLIpRuleSrcIpaddress_Type())
swACLIpRuleSrcIpaddress.setMaxAccess(_B)
if mibBuilder.loadTexts:swACLIpRuleSrcIpaddress.setStatus(_A)
_SwACLIpRuleDstIpaddress_Type=IpAddress
_SwACLIpRuleDstIpaddress_Object=MibTableColumn
swACLIpRuleDstIpaddress=_SwACLIpRuleDstIpaddress_Object((1,3,6,1,4,1,171,11,5,2,2,1,5),_SwACLIpRuleDstIpaddress_Type())
swACLIpRuleDstIpaddress.setMaxAccess(_B)
if mibBuilder.loadTexts:swACLIpRuleDstIpaddress.setStatus(_A)
class _SwACLIpRuleDscp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
_SwACLIpRuleDscp_Type.__name__=_C
_SwACLIpRuleDscp_Object=MibTableColumn
swACLIpRuleDscp=_SwACLIpRuleDscp_Object((1,3,6,1,4,1,171,11,5,2,2,1,6),_SwACLIpRuleDscp_Type())
swACLIpRuleDscp.setMaxAccess(_B)
if mibBuilder.loadTexts:swACLIpRuleDscp.setStatus(_A)
class _SwACLIpRuleProtocol_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_L,1),('icmp',2),('igmp',3),('tcp',4),('udp',5),(_Q,6)))
_SwACLIpRuleProtocol_Type.__name__=_C
_SwACLIpRuleProtocol_Object=MibTableColumn
swACLIpRuleProtocol=_SwACLIpRuleProtocol_Object((1,3,6,1,4,1,171,11,5,2,2,1,7),_SwACLIpRuleProtocol_Type())
swACLIpRuleProtocol.setMaxAccess(_H)
if mibBuilder.loadTexts:swACLIpRuleProtocol.setStatus(_A)
class _SwACLIpRuleType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_SwACLIpRuleType_Type.__name__=_C
_SwACLIpRuleType_Object=MibTableColumn
swACLIpRuleType=_SwACLIpRuleType_Object((1,3,6,1,4,1,171,11,5,2,2,1,8),_SwACLIpRuleType_Type())
swACLIpRuleType.setMaxAccess(_B)
if mibBuilder.loadTexts:swACLIpRuleType.setStatus(_A)
class _SwACLIpRuleCode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_SwACLIpRuleCode_Type.__name__=_C
_SwACLIpRuleCode_Object=MibTableColumn
swACLIpRuleCode=_SwACLIpRuleCode_Object((1,3,6,1,4,1,171,11,5,2,2,1,9),_SwACLIpRuleCode_Type())
swACLIpRuleCode.setMaxAccess(_B)
if mibBuilder.loadTexts:swACLIpRuleCode.setStatus(_A)
class _SwACLIpRuleSrcPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SwACLIpRuleSrcPort_Type.__name__=_C
_SwACLIpRuleSrcPort_Object=MibTableColumn
swACLIpRuleSrcPort=_SwACLIpRuleSrcPort_Object((1,3,6,1,4,1,171,11,5,2,2,1,10),_SwACLIpRuleSrcPort_Type())
swACLIpRuleSrcPort.setMaxAccess(_B)
if mibBuilder.loadTexts:swACLIpRuleSrcPort.setStatus(_A)
class _SwACLIpRuleDstPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SwACLIpRuleDstPort_Type.__name__=_C
_SwACLIpRuleDstPort_Object=MibTableColumn
swACLIpRuleDstPort=_SwACLIpRuleDstPort_Object((1,3,6,1,4,1,171,11,5,2,2,1,11),_SwACLIpRuleDstPort_Type())
swACLIpRuleDstPort.setMaxAccess(_B)
if mibBuilder.loadTexts:swACLIpRuleDstPort.setStatus(_A)
class _SwACLIpRuleFlagBits_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
_SwACLIpRuleFlagBits_Type.__name__=_C
_SwACLIpRuleFlagBits_Object=MibTableColumn
swACLIpRuleFlagBits=_SwACLIpRuleFlagBits_Object((1,3,6,1,4,1,171,11,5,2,2,1,12),_SwACLIpRuleFlagBits_Type())
swACLIpRuleFlagBits.setMaxAccess(_B)
if mibBuilder.loadTexts:swACLIpRuleFlagBits.setStatus(_A)
class _SwACLIpRuleProtoID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_SwACLIpRuleProtoID_Type.__name__=_C
_SwACLIpRuleProtoID_Object=MibTableColumn
swACLIpRuleProtoID=_SwACLIpRuleProtoID_Object((1,3,6,1,4,1,171,11,5,2,2,1,13),_SwACLIpRuleProtoID_Type())
swACLIpRuleProtoID.setMaxAccess(_B)
if mibBuilder.loadTexts:swACLIpRuleProtoID.setStatus(_A)
class _SwACLIpRuleUserMask_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
_SwACLIpRuleUserMask_Type.__name__=_D
_SwACLIpRuleUserMask_Object=MibTableColumn
swACLIpRuleUserMask=_SwACLIpRuleUserMask_Object((1,3,6,1,4,1,171,11,5,2,2,1,14),_SwACLIpRuleUserMask_Type())
swACLIpRuleUserMask.setMaxAccess(_B)
if mibBuilder.loadTexts:swACLIpRuleUserMask.setStatus(_A)
class _SwACLIpRuleEnablePriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_SwACLIpRuleEnablePriority_Type.__name__=_C
_SwACLIpRuleEnablePriority_Object=MibTableColumn
swACLIpRuleEnablePriority=_SwACLIpRuleEnablePriority_Object((1,3,6,1,4,1,171,11,5,2,2,1,15),_SwACLIpRuleEnablePriority_Type())
swACLIpRuleEnablePriority.setMaxAccess(_B)
if mibBuilder.loadTexts:swACLIpRuleEnablePriority.setStatus(_A)
class _SwACLIpRulePriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_SwACLIpRulePriority_Type.__name__=_C
_SwACLIpRulePriority_Object=MibTableColumn
swACLIpRulePriority=_SwACLIpRulePriority_Object((1,3,6,1,4,1,171,11,5,2,2,1,16),_SwACLIpRulePriority_Type())
swACLIpRulePriority.setMaxAccess(_B)
if mibBuilder.loadTexts:swACLIpRulePriority.setStatus(_A)
class _SwACLIpRuleReplacePriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_SwACLIpRuleReplacePriority_Type.__name__=_C
_SwACLIpRuleReplacePriority_Object=MibTableColumn
swACLIpRuleReplacePriority=_SwACLIpRuleReplacePriority_Object((1,3,6,1,4,1,171,11,5,2,2,1,17),_SwACLIpRuleReplacePriority_Type())
swACLIpRuleReplacePriority.setMaxAccess(_B)
if mibBuilder.loadTexts:swACLIpRuleReplacePriority.setStatus(_A)
class _SwACLIpRuleEnableReplaceDscp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_SwACLIpRuleEnableReplaceDscp_Type.__name__=_C
_SwACLIpRuleEnableReplaceDscp_Object=MibTableColumn
swACLIpRuleEnableReplaceDscp=_SwACLIpRuleEnableReplaceDscp_Object((1,3,6,1,4,1,171,11,5,2,2,1,18),_SwACLIpRuleEnableReplaceDscp_Type())
swACLIpRuleEnableReplaceDscp.setMaxAccess(_B)
if mibBuilder.loadTexts:swACLIpRuleEnableReplaceDscp.setStatus(_A)
class _SwACLIpRuleRepDscp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
_SwACLIpRuleRepDscp_Type.__name__=_C
_SwACLIpRuleRepDscp_Object=MibTableColumn
swACLIpRuleRepDscp=_SwACLIpRuleRepDscp_Object((1,3,6,1,4,1,171,11,5,2,2,1,19),_SwACLIpRuleRepDscp_Type())
swACLIpRuleRepDscp.setMaxAccess(_B)
if mibBuilder.loadTexts:swACLIpRuleRepDscp.setStatus(_A)
class _SwACLIpRulePermit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_N,1),(_M,2)))
_SwACLIpRulePermit_Type.__name__=_C
_SwACLIpRulePermit_Object=MibTableColumn
swACLIpRulePermit=_SwACLIpRulePermit_Object((1,3,6,1,4,1,171,11,5,2,2,1,20),_SwACLIpRulePermit_Type())
swACLIpRulePermit.setMaxAccess(_B)
if mibBuilder.loadTexts:swACLIpRulePermit.setStatus(_A)
_SwACLIpRuleRowStatus_Type=RowStatus
_SwACLIpRuleRowStatus_Object=MibTableColumn
swACLIpRuleRowStatus=_SwACLIpRuleRowStatus_Object((1,3,6,1,4,1,171,11,5,2,2,1,21),_SwACLIpRuleRowStatus_Type())
swACLIpRuleRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:swACLIpRuleRowStatus.setStatus(_A)
_SwACLPayloadRuleTable_Object=MibTable
swACLPayloadRuleTable=_SwACLPayloadRuleTable_Object((1,3,6,1,4,1,171,11,5,2,3))
if mibBuilder.loadTexts:swACLPayloadRuleTable.setStatus(_A)
_SwACLPayloadRuleEntry_Object=MibTableRow
swACLPayloadRuleEntry=_SwACLPayloadRuleEntry_Object((1,3,6,1,4,1,171,11,5,2,3,1))
swACLPayloadRuleEntry.setIndexNames((0,_G,_b),(0,_G,_c))
if mibBuilder.loadTexts:swACLPayloadRuleEntry.setStatus(_A)
class _SwACLPayloadRuleProfileID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_SwACLPayloadRuleProfileID_Type.__name__=_C
_SwACLPayloadRuleProfileID_Object=MibTableColumn
swACLPayloadRuleProfileID=_SwACLPayloadRuleProfileID_Object((1,3,6,1,4,1,171,11,5,2,3,1,1),_SwACLPayloadRuleProfileID_Type())
swACLPayloadRuleProfileID.setMaxAccess(_H)
if mibBuilder.loadTexts:swACLPayloadRuleProfileID.setStatus(_A)
class _SwACLPayloadRuleAccessID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_SwACLPayloadRuleAccessID_Type.__name__=_C
_SwACLPayloadRuleAccessID_Object=MibTableColumn
swACLPayloadRuleAccessID=_SwACLPayloadRuleAccessID_Object((1,3,6,1,4,1,171,11,5,2,3,1,2),_SwACLPayloadRuleAccessID_Type())
swACLPayloadRuleAccessID.setMaxAccess(_H)
if mibBuilder.loadTexts:swACLPayloadRuleAccessID.setStatus(_A)
class _SwACLPayloadRuleOffSet0to15_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,16));fixedLength=16
_SwACLPayloadRuleOffSet0to15_Type.__name__=_D
_SwACLPayloadRuleOffSet0to15_Object=MibTableColumn
swACLPayloadRuleOffSet0to15=_SwACLPayloadRuleOffSet0to15_Object((1,3,6,1,4,1,171,11,5,2,3,1,3),_SwACLPayloadRuleOffSet0to15_Type())
swACLPayloadRuleOffSet0to15.setMaxAccess(_B)
if mibBuilder.loadTexts:swACLPayloadRuleOffSet0to15.setStatus(_A)
class _SwACLPayloadRuleOffSet16to31_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,16));fixedLength=16
_SwACLPayloadRuleOffSet16to31_Type.__name__=_D
_SwACLPayloadRuleOffSet16to31_Object=MibTableColumn
swACLPayloadRuleOffSet16to31=_SwACLPayloadRuleOffSet16to31_Object((1,3,6,1,4,1,171,11,5,2,3,1,4),_SwACLPayloadRuleOffSet16to31_Type())
swACLPayloadRuleOffSet16to31.setMaxAccess(_B)
if mibBuilder.loadTexts:swACLPayloadRuleOffSet16to31.setStatus(_A)
class _SwACLPayloadRuleOffSet32to47_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,16));fixedLength=16
_SwACLPayloadRuleOffSet32to47_Type.__name__=_D
_SwACLPayloadRuleOffSet32to47_Object=MibTableColumn
swACLPayloadRuleOffSet32to47=_SwACLPayloadRuleOffSet32to47_Object((1,3,6,1,4,1,171,11,5,2,3,1,5),_SwACLPayloadRuleOffSet32to47_Type())
swACLPayloadRuleOffSet32to47.setMaxAccess(_B)
if mibBuilder.loadTexts:swACLPayloadRuleOffSet32to47.setStatus(_A)
class _SwACLPayloadRuleOffSet48to63_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,16));fixedLength=16
_SwACLPayloadRuleOffSet48to63_Type.__name__=_D
_SwACLPayloadRuleOffSet48to63_Object=MibTableColumn
swACLPayloadRuleOffSet48to63=_SwACLPayloadRuleOffSet48to63_Object((1,3,6,1,4,1,171,11,5,2,3,1,6),_SwACLPayloadRuleOffSet48to63_Type())
swACLPayloadRuleOffSet48to63.setMaxAccess(_B)
if mibBuilder.loadTexts:swACLPayloadRuleOffSet48to63.setStatus(_A)
class _SwACLPayloadRuleOffSet64to79_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,16));fixedLength=16
_SwACLPayloadRuleOffSet64to79_Type.__name__=_D
_SwACLPayloadRuleOffSet64to79_Object=MibTableColumn
swACLPayloadRuleOffSet64to79=_SwACLPayloadRuleOffSet64to79_Object((1,3,6,1,4,1,171,11,5,2,3,1,7),_SwACLPayloadRuleOffSet64to79_Type())
swACLPayloadRuleOffSet64to79.setMaxAccess(_B)
if mibBuilder.loadTexts:swACLPayloadRuleOffSet64to79.setStatus(_A)
class _SwACLPayloadRuleEnablePriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_SwACLPayloadRuleEnablePriority_Type.__name__=_C
_SwACLPayloadRuleEnablePriority_Object=MibTableColumn
swACLPayloadRuleEnablePriority=_SwACLPayloadRuleEnablePriority_Object((1,3,6,1,4,1,171,11,5,2,3,1,8),_SwACLPayloadRuleEnablePriority_Type())
swACLPayloadRuleEnablePriority.setMaxAccess(_B)
if mibBuilder.loadTexts:swACLPayloadRuleEnablePriority.setStatus(_A)
class _SwACLPayloadRulePriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_SwACLPayloadRulePriority_Type.__name__=_C
_SwACLPayloadRulePriority_Object=MibTableColumn
swACLPayloadRulePriority=_SwACLPayloadRulePriority_Object((1,3,6,1,4,1,171,11,5,2,3,1,9),_SwACLPayloadRulePriority_Type())
swACLPayloadRulePriority.setMaxAccess(_B)
if mibBuilder.loadTexts:swACLPayloadRulePriority.setStatus(_A)
class _SwACLPayloadRuleReplacePriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_SwACLPayloadRuleReplacePriority_Type.__name__=_C
_SwACLPayloadRuleReplacePriority_Object=MibTableColumn
swACLPayloadRuleReplacePriority=_SwACLPayloadRuleReplacePriority_Object((1,3,6,1,4,1,171,11,5,2,3,1,10),_SwACLPayloadRuleReplacePriority_Type())
swACLPayloadRuleReplacePriority.setMaxAccess(_B)
if mibBuilder.loadTexts:swACLPayloadRuleReplacePriority.setStatus(_A)
class _SwACLPayloadRuleEnableReplaceDscp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_SwACLPayloadRuleEnableReplaceDscp_Type.__name__=_C
_SwACLPayloadRuleEnableReplaceDscp_Object=MibTableColumn
swACLPayloadRuleEnableReplaceDscp=_SwACLPayloadRuleEnableReplaceDscp_Object((1,3,6,1,4,1,171,11,5,2,3,1,11),_SwACLPayloadRuleEnableReplaceDscp_Type())
swACLPayloadRuleEnableReplaceDscp.setMaxAccess(_B)
if mibBuilder.loadTexts:swACLPayloadRuleEnableReplaceDscp.setStatus(_A)
class _SwACLPayloadRuleRepDscp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
_SwACLPayloadRuleRepDscp_Type.__name__=_C
_SwACLPayloadRuleRepDscp_Object=MibTableColumn
swACLPayloadRuleRepDscp=_SwACLPayloadRuleRepDscp_Object((1,3,6,1,4,1,171,11,5,2,3,1,12),_SwACLPayloadRuleRepDscp_Type())
swACLPayloadRuleRepDscp.setMaxAccess(_B)
if mibBuilder.loadTexts:swACLPayloadRuleRepDscp.setStatus(_A)
class _SwACLPayloadRulePermit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_M,1),(_N,2)))
_SwACLPayloadRulePermit_Type.__name__=_C
_SwACLPayloadRulePermit_Object=MibTableColumn
swACLPayloadRulePermit=_SwACLPayloadRulePermit_Object((1,3,6,1,4,1,171,11,5,2,3,1,13),_SwACLPayloadRulePermit_Type())
swACLPayloadRulePermit.setMaxAccess(_B)
if mibBuilder.loadTexts:swACLPayloadRulePermit.setStatus(_A)
_SwACLPayloadRuleRowStatus_Type=RowStatus
_SwACLPayloadRuleRowStatus_Object=MibTableColumn
swACLPayloadRuleRowStatus=_SwACLPayloadRuleRowStatus_Object((1,3,6,1,4,1,171,11,5,2,3,1,14),_SwACLPayloadRuleRowStatus_Type())
swACLPayloadRuleRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:swACLPayloadRuleRowStatus.setStatus(_A)
mibBuilder.exportSymbols(_G,**{'swAclMgmtMIB':swAclMgmtMIB,'swAclMaskMgmt':swAclMaskMgmt,'swACLEthernetTable':swACLEthernetTable,'swACLEthernetEntry':swACLEthernetEntry,_O:swACLEthernetProfileID,'swACLEthernetUsevlan':swACLEthernetUsevlan,'swACLEthernetMacAddrMaskState':swACLEthernetMacAddrMaskState,'swACLEthernetSrcMacAddrMask':swACLEthernetSrcMacAddrMask,'swACLEthernetDstMacAddrMask':swACLEthernetDstMacAddrMask,'swACLEthernetUse8021p':swACLEthernetUse8021p,'swACLEthernetUseEthernetType':swACLEthernetUseEthernetType,'swACLEthernetPort':swACLEthernetPort,'swACLEthernetRowStatus':swACLEthernetRowStatus,'swACLIpTable':swACLIpTable,'swACLIpEntry':swACLIpEntry,_P:swACLIpProfileID,'swACLIpUsevlan':swACLIpUsevlan,'swACLIpIpAddrMaskState':swACLIpIpAddrMaskState,'swACLIpSrcIpAddrMask':swACLIpSrcIpAddrMask,'swACLIpDstIpAddrMask':swACLIpDstIpAddrMask,'swACLIpUseDSCP':swACLIpUseDSCP,'swACLIpUseProtoType':swACLIpUseProtoType,'swACLIpIcmpOption':swACLIpIcmpOption,'swACLIpIgmpOption':swACLIpIgmpOption,'swACLIpTcpOption':swACLIpTcpOption,'swACLIpUdpOption':swACLIpUdpOption,'swACLIpTCPorUDPSrcPortMask':swACLIpTCPorUDPSrcPortMask,'swACLIpTCPorUDPDstPortMask':swACLIpTCPorUDPDstPortMask,'swACLIpTCPFlagBit':swACLIpTCPFlagBit,'swACLIpProtoIDOption':swACLIpProtoIDOption,'swACLIpProtoIDMask':swACLIpProtoIDMask,'swACLIpPort':swACLIpPort,'swACLIpRowStatus':swACLIpRowStatus,'swACLPayloadTable':swACLPayloadTable,'swACLPayloadEntry':swACLPayloadEntry,_W:swACLPayloadProfileID,'swACLPayloadOffSet0to15':swACLPayloadOffSet0to15,'swACLPayloadOffSet16to31':swACLPayloadOffSet16to31,'swACLPayloadOffSet32to47':swACLPayloadOffSet32to47,'swACLPayloadOffSet48to63':swACLPayloadOffSet48to63,'swACLPayloadOffSet64to79':swACLPayloadOffSet64to79,'swACLPayloadPort':swACLPayloadPort,'swACLPayloadRowStatus':swACLPayloadRowStatus,'swAclRuleMgmt':swAclRuleMgmt,'swACLEtherRuleTable':swACLEtherRuleTable,'swACLEtherRuleEntry':swACLEtherRuleEntry,_X:swACLEtherRuleProfileID,_Y:swACLEtherRuleAccessID,'swACLEtherRuleVlan':swACLEtherRuleVlan,'swACLEtherRuleSrcMacAddress':swACLEtherRuleSrcMacAddress,'swACLEtherRuleDstMacAddress':swACLEtherRuleDstMacAddress,'swACLEtherRule8021P':swACLEtherRule8021P,'swACLEtherRuleEtherType':swACLEtherRuleEtherType,'swACLEtherRuleEnablePriority':swACLEtherRuleEnablePriority,'swACLEtherRulePriority':swACLEtherRulePriority,'swACLEtherRuleReplacePriority':swACLEtherRuleReplacePriority,'swACLEtherRuleEnableReplaceDscp':swACLEtherRuleEnableReplaceDscp,'swACLEtherRuleRepDscp':swACLEtherRuleRepDscp,'swACLEtherRulePermit':swACLEtherRulePermit,'swACLEtherRuleRowStatus':swACLEtherRuleRowStatus,'swACLIpRuleTable':swACLIpRuleTable,'swACLIpRuleEntry':swACLIpRuleEntry,_Z:swACLIpRuleProfileID,_a:swACLIpRuleAccessID,'swACLIpRuleVlan':swACLIpRuleVlan,'swACLIpRuleSrcIpaddress':swACLIpRuleSrcIpaddress,'swACLIpRuleDstIpaddress':swACLIpRuleDstIpaddress,'swACLIpRuleDscp':swACLIpRuleDscp,'swACLIpRuleProtocol':swACLIpRuleProtocol,'swACLIpRuleType':swACLIpRuleType,'swACLIpRuleCode':swACLIpRuleCode,'swACLIpRuleSrcPort':swACLIpRuleSrcPort,'swACLIpRuleDstPort':swACLIpRuleDstPort,'swACLIpRuleFlagBits':swACLIpRuleFlagBits,'swACLIpRuleProtoID':swACLIpRuleProtoID,'swACLIpRuleUserMask':swACLIpRuleUserMask,'swACLIpRuleEnablePriority':swACLIpRuleEnablePriority,'swACLIpRulePriority':swACLIpRulePriority,'swACLIpRuleReplacePriority':swACLIpRuleReplacePriority,'swACLIpRuleEnableReplaceDscp':swACLIpRuleEnableReplaceDscp,'swACLIpRuleRepDscp':swACLIpRuleRepDscp,'swACLIpRulePermit':swACLIpRulePermit,'swACLIpRuleRowStatus':swACLIpRuleRowStatus,'swACLPayloadRuleTable':swACLPayloadRuleTable,'swACLPayloadRuleEntry':swACLPayloadRuleEntry,_b:swACLPayloadRuleProfileID,_c:swACLPayloadRuleAccessID,'swACLPayloadRuleOffSet0to15':swACLPayloadRuleOffSet0to15,'swACLPayloadRuleOffSet16to31':swACLPayloadRuleOffSet16to31,'swACLPayloadRuleOffSet32to47':swACLPayloadRuleOffSet32to47,'swACLPayloadRuleOffSet48to63':swACLPayloadRuleOffSet48to63,'swACLPayloadRuleOffSet64to79':swACLPayloadRuleOffSet64to79,'swACLPayloadRuleEnablePriority':swACLPayloadRuleEnablePriority,'swACLPayloadRulePriority':swACLPayloadRulePriority,'swACLPayloadRuleReplacePriority':swACLPayloadRuleReplacePriority,'swACLPayloadRuleEnableReplaceDscp':swACLPayloadRuleEnableReplaceDscp,'swACLPayloadRuleRepDscp':swACLPayloadRuleRepDscp,'swACLPayloadRulePermit':swACLPayloadRulePermit,'swACLPayloadRuleRowStatus':swACLPayloadRuleRowStatus})