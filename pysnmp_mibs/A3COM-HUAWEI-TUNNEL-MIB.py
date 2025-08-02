_K='h3cTunnelInetConfigTunnNum'
_J='h3cTunnelInetConfigSubSlot'
_I='h3cTunnelInetConfigSlot'
_H='ifIndex'
_G='IF-MIB'
_F='not-accessible'
_E='A3COM-HUAWEI-TUNNEL-MIB'
_D='read-write'
_C='read-only'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
h3cCommon,=mibBuilder.importSymbols('A3COM-HUAWEI-OID-MIB','h3cCommon')
InterfaceIndexOrZero,ifIndex=mibBuilder.importSymbols(_G,'InterfaceIndexOrZero',_H)
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
IPv6FlowLabelOrAny,=mibBuilder.importSymbols('IPV6-FLOW-LABEL-MIB','IPv6FlowLabelOrAny')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,StorageType,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','StorageType','TextualConvention')
h3cTunnel=ModuleIdentity((1,3,6,1,4,1,43,45,1,10,2,53))
if mibBuilder.loadTexts:h3cTunnel.setRevisions(('2005-06-04 00:00',))
class H3cTunnelType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50)));namedValues=NamedValues(*(('other',1),('direct',2),('gre',3),('minimal',4),('l2tp',5),('pptp',6),('l2f',7),('udp',8),('atmp',9),('msdp',10),('sixToFour',11),('sixOverFour',12),('isatap',13),('teredo',14),('tunnelModeReserve',35),('tunnelModeIPv4Gre',36),('tunnelModeIPv6Gre',37),('tunnelModeIPv4IPv4',38),('tunnelModeIPv4IPv6Config',39),('tunnelModeIPv4IPv6Auto',40),('tunnelModeIPv4IPv66to4',41),('tunnelModeIPv4IPv6Isatap',42),('tunnelModeIPv6IPv4',43),('tunnelModeIPv6IPv6',44),('tunnelModeIPv4UdpDVPN',45),('tunnelModeIPv4GreDVPN',46),('tunnelModeIPv6UdpDVPN',47),('tunnelModeIPv6GreDVPN',48),('tunnelModeCrLsp',49),('tunnelModeMax',50)))
_H3cTunnelMIBObjects_ObjectIdentity=ObjectIdentity
h3cTunnelMIBObjects=_H3cTunnelMIBObjects_ObjectIdentity((1,3,6,1,4,1,43,45,1,10,2,53,1))
_H3cTunnelTables_ObjectIdentity=ObjectIdentity
h3cTunnelTables=_H3cTunnelTables_ObjectIdentity((1,3,6,1,4,1,43,45,1,10,2,53,1,1))
_H3cTunnelIfTable_Object=MibTable
h3cTunnelIfTable=_H3cTunnelIfTable_Object((1,3,6,1,4,1,43,45,1,10,2,53,1,1,1))
if mibBuilder.loadTexts:h3cTunnelIfTable.setStatus(_A)
_H3cTunnelIfEntry_Object=MibTableRow
h3cTunnelIfEntry=_H3cTunnelIfEntry_Object((1,3,6,1,4,1,43,45,1,10,2,53,1,1,1,1))
h3cTunnelIfEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:h3cTunnelIfEntry.setStatus(_A)
_H3cTunnelIfEncapsMethod_Type=H3cTunnelType
_H3cTunnelIfEncapsMethod_Object=MibTableColumn
h3cTunnelIfEncapsMethod=_H3cTunnelIfEncapsMethod_Object((1,3,6,1,4,1,43,45,1,10,2,53,1,1,1,1,3),_H3cTunnelIfEncapsMethod_Type())
h3cTunnelIfEncapsMethod.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cTunnelIfEncapsMethod.setStatus(_A)
class _H3cTunnelIfHopLimit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,255))
_H3cTunnelIfHopLimit_Type.__name__=_B
_H3cTunnelIfHopLimit_Object=MibTableColumn
h3cTunnelIfHopLimit=_H3cTunnelIfHopLimit_Object((1,3,6,1,4,1,43,45,1,10,2,53,1,1,1,1,4),_H3cTunnelIfHopLimit_Type())
h3cTunnelIfHopLimit.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cTunnelIfHopLimit.setStatus(_A)
class _H3cTunnelIfSecurity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('none',1),('ipsec',2),('other',3)))
_H3cTunnelIfSecurity_Type.__name__=_B
_H3cTunnelIfSecurity_Object=MibTableColumn
h3cTunnelIfSecurity=_H3cTunnelIfSecurity_Object((1,3,6,1,4,1,43,45,1,10,2,53,1,1,1,1,5),_H3cTunnelIfSecurity_Type())
h3cTunnelIfSecurity.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cTunnelIfSecurity.setStatus(_A)
class _H3cTunnelIfTOS_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2,63))
_H3cTunnelIfTOS_Type.__name__=_B
_H3cTunnelIfTOS_Object=MibTableColumn
h3cTunnelIfTOS=_H3cTunnelIfTOS_Object((1,3,6,1,4,1,43,45,1,10,2,53,1,1,1,1,6),_H3cTunnelIfTOS_Type())
h3cTunnelIfTOS.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cTunnelIfTOS.setStatus(_A)
_H3cTunnelIfFlowLabel_Type=IPv6FlowLabelOrAny
_H3cTunnelIfFlowLabel_Object=MibTableColumn
h3cTunnelIfFlowLabel=_H3cTunnelIfFlowLabel_Object((1,3,6,1,4,1,43,45,1,10,2,53,1,1,1,1,7),_H3cTunnelIfFlowLabel_Type())
h3cTunnelIfFlowLabel.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cTunnelIfFlowLabel.setStatus(_A)
_H3cTunnelIfAddressType_Type=InetAddressType
_H3cTunnelIfAddressType_Object=MibTableColumn
h3cTunnelIfAddressType=_H3cTunnelIfAddressType_Object((1,3,6,1,4,1,43,45,1,10,2,53,1,1,1,1,8),_H3cTunnelIfAddressType_Type())
h3cTunnelIfAddressType.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cTunnelIfAddressType.setStatus(_A)
_H3cTunnelIfLocalInetAddress_Type=InetAddress
_H3cTunnelIfLocalInetAddress_Object=MibTableColumn
h3cTunnelIfLocalInetAddress=_H3cTunnelIfLocalInetAddress_Object((1,3,6,1,4,1,43,45,1,10,2,53,1,1,1,1,9),_H3cTunnelIfLocalInetAddress_Type())
h3cTunnelIfLocalInetAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cTunnelIfLocalInetAddress.setStatus(_A)
_H3cTunnelIfRemoteInetAddress_Type=InetAddress
_H3cTunnelIfRemoteInetAddress_Object=MibTableColumn
h3cTunnelIfRemoteInetAddress=_H3cTunnelIfRemoteInetAddress_Object((1,3,6,1,4,1,43,45,1,10,2,53,1,1,1,1,10),_H3cTunnelIfRemoteInetAddress_Type())
h3cTunnelIfRemoteInetAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cTunnelIfRemoteInetAddress.setStatus(_A)
class _H3cTunnelIfEncapsLimit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,-1),ValueRangeConstraint(0,255))
_H3cTunnelIfEncapsLimit_Type.__name__=_B
_H3cTunnelIfEncapsLimit_Object=MibTableColumn
h3cTunnelIfEncapsLimit=_H3cTunnelIfEncapsLimit_Object((1,3,6,1,4,1,43,45,1,10,2,53,1,1,1,1,11),_H3cTunnelIfEncapsLimit_Type())
h3cTunnelIfEncapsLimit.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cTunnelIfEncapsLimit.setStatus(_A)
_H3cTunnelInetConfigTable_Object=MibTable
h3cTunnelInetConfigTable=_H3cTunnelInetConfigTable_Object((1,3,6,1,4,1,43,45,1,10,2,53,1,1,3))
if mibBuilder.loadTexts:h3cTunnelInetConfigTable.setStatus(_A)
_H3cTunnelInetConfigEntry_Object=MibTableRow
h3cTunnelInetConfigEntry=_H3cTunnelInetConfigEntry_Object((1,3,6,1,4,1,43,45,1,10,2,53,1,1,3,1))
h3cTunnelInetConfigEntry.setIndexNames((0,_E,_I),(0,_E,_J),(0,_E,_K))
if mibBuilder.loadTexts:h3cTunnelInetConfigEntry.setStatus(_A)
class _H3cTunnelInetConfigSlot_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_H3cTunnelInetConfigSlot_Type.__name__=_B
_H3cTunnelInetConfigSlot_Object=MibTableColumn
h3cTunnelInetConfigSlot=_H3cTunnelInetConfigSlot_Object((1,3,6,1,4,1,43,45,1,10,2,53,1,1,3,1,1),_H3cTunnelInetConfigSlot_Type())
h3cTunnelInetConfigSlot.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cTunnelInetConfigSlot.setStatus(_A)
class _H3cTunnelInetConfigSubSlot_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_H3cTunnelInetConfigSubSlot_Type.__name__=_B
_H3cTunnelInetConfigSubSlot_Object=MibTableColumn
h3cTunnelInetConfigSubSlot=_H3cTunnelInetConfigSubSlot_Object((1,3,6,1,4,1,43,45,1,10,2,53,1,1,3,1,2),_H3cTunnelInetConfigSubSlot_Type())
h3cTunnelInetConfigSubSlot.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cTunnelInetConfigSubSlot.setStatus(_A)
class _H3cTunnelInetConfigTunnNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_H3cTunnelInetConfigTunnNum_Type.__name__=_B
_H3cTunnelInetConfigTunnNum_Object=MibTableColumn
h3cTunnelInetConfigTunnNum=_H3cTunnelInetConfigTunnNum_Object((1,3,6,1,4,1,43,45,1,10,2,53,1,1,3,1,3),_H3cTunnelInetConfigTunnNum_Type())
h3cTunnelInetConfigTunnNum.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cTunnelInetConfigTunnNum.setStatus(_A)
_H3cTunnelInetConfigIfIndex_Type=InterfaceIndexOrZero
_H3cTunnelInetConfigIfIndex_Object=MibTableColumn
h3cTunnelInetConfigIfIndex=_H3cTunnelInetConfigIfIndex_Object((1,3,6,1,4,1,43,45,1,10,2,53,1,1,3,1,6),_H3cTunnelInetConfigIfIndex_Type())
h3cTunnelInetConfigIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cTunnelInetConfigIfIndex.setStatus(_A)
_H3cTunnelInetConfigStatus_Type=RowStatus
_H3cTunnelInetConfigStatus_Object=MibTableColumn
h3cTunnelInetConfigStatus=_H3cTunnelInetConfigStatus_Object((1,3,6,1,4,1,43,45,1,10,2,53,1,1,3,1,7),_H3cTunnelInetConfigStatus_Type())
h3cTunnelInetConfigStatus.setMaxAccess('read-create')
if mibBuilder.loadTexts:h3cTunnelInetConfigStatus.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'H3cTunnelType':H3cTunnelType,'h3cTunnel':h3cTunnel,'h3cTunnelMIBObjects':h3cTunnelMIBObjects,'h3cTunnelTables':h3cTunnelTables,'h3cTunnelIfTable':h3cTunnelIfTable,'h3cTunnelIfEntry':h3cTunnelIfEntry,'h3cTunnelIfEncapsMethod':h3cTunnelIfEncapsMethod,'h3cTunnelIfHopLimit':h3cTunnelIfHopLimit,'h3cTunnelIfSecurity':h3cTunnelIfSecurity,'h3cTunnelIfTOS':h3cTunnelIfTOS,'h3cTunnelIfFlowLabel':h3cTunnelIfFlowLabel,'h3cTunnelIfAddressType':h3cTunnelIfAddressType,'h3cTunnelIfLocalInetAddress':h3cTunnelIfLocalInetAddress,'h3cTunnelIfRemoteInetAddress':h3cTunnelIfRemoteInetAddress,'h3cTunnelIfEncapsLimit':h3cTunnelIfEncapsLimit,'h3cTunnelInetConfigTable':h3cTunnelInetConfigTable,'h3cTunnelInetConfigEntry':h3cTunnelInetConfigEntry,_I:h3cTunnelInetConfigSlot,_J:h3cTunnelInetConfigSubSlot,_K:h3cTunnelInetConfigTunnNum,'h3cTunnelInetConfigIfIndex':h3cTunnelInetConfigIfIndex,'h3cTunnelInetConfigStatus':h3cTunnelInetConfigStatus})