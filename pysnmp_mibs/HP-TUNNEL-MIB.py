_w='hpTunnelNotificationsGroup'
_v='hpTunnelNotifyScalarsGroup'
_u='hpTunnelProvisionGroup2'
_t='hpTunnelProvisionGroup'
_s='hpTunnelIcmpErrorRcvd'
_r='hpTunnelMTUDropNotifyEnable'
_q='hpTunnelInterfaceIndex'
_p='hpicfVlanTunnelMappingRowStatus'
_o='hpicfUDPTunnelType'
_n='hpTunnelIpsecName'
_m='hpTunnelInetConfigEncapsMethod'
_l='hpTunnelIfIndex'
_k='hpicfUDPTunnelTypeEntry'
_j='hpTunnelInetConfigEntry'
_i='hpTunnelIfEntry'
_h='hpicfTunnelIfIndex'
_g='hpicfVLANIndex'
_f='hpTunnelID'
_e='tunnelIfRemoteInetAddress'
_d='tunnelIfLocalInetAddress'
_c='tunnelIfAddressType'
_b='Unsigned32'
_a='SnmpAdminString'
_Z='hpVlanTunnelMappingGroup'
_Y='hpTunnelInetConfigGroup'
_X='hpTunnelMTUDropInIfIndex'
_W='hpTunnelMTUDropTunnelDest'
_V='hpTunnelMTUDropTunnelDstAddrType'
_U='hpTunnelMTUDropTunnelSource'
_T='hpTunnelMTUDropTunnelSrcAddrType'
_S='hpTunnelMTUDropRouterMTU'
_R='hpTunnelMTUDropRouterAddr'
_Q='hpTunnelMTUDropRouterAddrType'
_P='hpTunnelRowStatus'
_O='hpTunnelIfNUD'
_N='hpTunnelIfMTU'
_M='hpTunnelIfPMTU'
_L='hpTunnelEncapsMethod'
_K='disable'
_J='enable'
_I='deprecated'
_H='not-accessible'
_G='read-create'
_F='TUNNEL-MIB'
_E='Integer32'
_D='read-write'
_C='accessible-for-notify'
_B='current'
_A='HP-TUNNEL-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hpSwitch,=mibBuilder.importSymbols('HP-ICF-OID','hpSwitch')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
VlanIndex,=mibBuilder.importSymbols('Q-BRIDGE-MIB','VlanIndex')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_a)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_b,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
tunnelIfAddressType,tunnelIfEntry,tunnelIfLocalInetAddress,tunnelIfRemoteInetAddress,tunnelInetConfigEntry=mibBuilder.importSymbols(_F,_c,'tunnelIfEntry',_d,_e,'tunnelInetConfigEntry')
hpTunnelMIB=ModuleIdentity((1,3,6,1,4,1,11,2,14,11,5,1,77))
if mibBuilder.loadTexts:hpTunnelMIB.setRevisions(('2015-02-02 00:00','2014-08-15 00:00','2014-08-13 00:00','2010-07-22 00:00'))
class HpTunnelType(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('unspecified',1),('direct4in4',2),('direct6in4',3),('direct6in4Ipsec',4),('direct6in6',5),('ipsecIpv4',6),('ipsecIpv6',7),('macinudp',8)))
_HpTunnelNotifications_ObjectIdentity=ObjectIdentity
hpTunnelNotifications=_HpTunnelNotifications_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,77,0))
_HpTunnelObjects_ObjectIdentity=ObjectIdentity
hpTunnelObjects=_HpTunnelObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,77,1))
_HpTunnelConfigTable_Object=MibTable
hpTunnelConfigTable=_HpTunnelConfigTable_Object((1,3,6,1,4,1,11,2,14,11,5,1,77,1,1))
if mibBuilder.loadTexts:hpTunnelConfigTable.setStatus(_B)
_HpTunnelConfigEntry_Object=MibTableRow
hpTunnelConfigEntry=_HpTunnelConfigEntry_Object((1,3,6,1,4,1,11,2,14,11,5,1,77,1,1,1))
hpTunnelConfigEntry.setIndexNames((0,_A,_f))
if mibBuilder.loadTexts:hpTunnelConfigEntry.setStatus(_B)
class _HpTunnelID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_HpTunnelID_Type.__name__=_E
_HpTunnelID_Object=MibTableColumn
hpTunnelID=_HpTunnelID_Object((1,3,6,1,4,1,11,2,14,11,5,1,77,1,1,1,1),_HpTunnelID_Type())
hpTunnelID.setMaxAccess(_H)
if mibBuilder.loadTexts:hpTunnelID.setStatus(_B)
_HpTunnelIfIndex_Type=InterfaceIndex
_HpTunnelIfIndex_Object=MibTableColumn
hpTunnelIfIndex=_HpTunnelIfIndex_Object((1,3,6,1,4,1,11,2,14,11,5,1,77,1,1,1,2),_HpTunnelIfIndex_Type())
hpTunnelIfIndex.setMaxAccess('read-only')
if mibBuilder.loadTexts:hpTunnelIfIndex.setStatus(_I)
_HpTunnelRowStatus_Type=RowStatus
_HpTunnelRowStatus_Object=MibTableColumn
hpTunnelRowStatus=_HpTunnelRowStatus_Object((1,3,6,1,4,1,11,2,14,11,5,1,77,1,1,1,3),_HpTunnelRowStatus_Type())
hpTunnelRowStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:hpTunnelRowStatus.setStatus(_B)
_HpTunnelInterfaceIndex_Type=InterfaceIndex
_HpTunnelInterfaceIndex_Object=MibTableColumn
hpTunnelInterfaceIndex=_HpTunnelInterfaceIndex_Object((1,3,6,1,4,1,11,2,14,11,5,1,77,1,1,1,4),_HpTunnelInterfaceIndex_Type())
hpTunnelInterfaceIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:hpTunnelInterfaceIndex.setStatus(_B)
_HpTunnelIfTable_Object=MibTable
hpTunnelIfTable=_HpTunnelIfTable_Object((1,3,6,1,4,1,11,2,14,11,5,1,77,1,2))
if mibBuilder.loadTexts:hpTunnelIfTable.setStatus(_B)
_HpTunnelIfEntry_Object=MibTableRow
hpTunnelIfEntry=_HpTunnelIfEntry_Object((1,3,6,1,4,1,11,2,14,11,5,1,77,1,2,1))
if mibBuilder.loadTexts:hpTunnelIfEntry.setStatus(_B)
class _HpTunnelIfPMTU_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_HpTunnelIfPMTU_Type.__name__=_E
_HpTunnelIfPMTU_Object=MibTableColumn
hpTunnelIfPMTU=_HpTunnelIfPMTU_Object((1,3,6,1,4,1,11,2,14,11,5,1,77,1,2,1,1),_HpTunnelIfPMTU_Type())
hpTunnelIfPMTU.setMaxAccess(_D)
if mibBuilder.loadTexts:hpTunnelIfPMTU.setStatus(_B)
class _HpTunnelIfNUD_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_HpTunnelIfNUD_Type.__name__=_E
_HpTunnelIfNUD_Object=MibTableColumn
hpTunnelIfNUD=_HpTunnelIfNUD_Object((1,3,6,1,4,1,11,2,14,11,5,1,77,1,2,1,2),_HpTunnelIfNUD_Type())
hpTunnelIfNUD.setMaxAccess(_D)
if mibBuilder.loadTexts:hpTunnelIfNUD.setStatus(_B)
class _HpTunnelIfMTU_Type(Unsigned32):defaultValue=1280
_HpTunnelIfMTU_Type.__name__=_b
_HpTunnelIfMTU_Object=MibTableColumn
hpTunnelIfMTU=_HpTunnelIfMTU_Object((1,3,6,1,4,1,11,2,14,11,5,1,77,1,2,1,3),_HpTunnelIfMTU_Type())
hpTunnelIfMTU.setMaxAccess(_D)
if mibBuilder.loadTexts:hpTunnelIfMTU.setStatus(_B)
_HpTunnelEncapsMethod_Type=HpTunnelType
_HpTunnelEncapsMethod_Object=MibTableColumn
hpTunnelEncapsMethod=_HpTunnelEncapsMethod_Object((1,3,6,1,4,1,11,2,14,11,5,1,77,1,2,1,4),_HpTunnelEncapsMethod_Type())
hpTunnelEncapsMethod.setMaxAccess(_D)
if mibBuilder.loadTexts:hpTunnelEncapsMethod.setStatus(_B)
class _HpTunnelIpsecName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_HpTunnelIpsecName_Type.__name__=_a
_HpTunnelIpsecName_Object=MibTableColumn
hpTunnelIpsecName=_HpTunnelIpsecName_Object((1,3,6,1,4,1,11,2,14,11,5,1,77,1,2,1,5),_HpTunnelIpsecName_Type())
hpTunnelIpsecName.setMaxAccess(_D)
if mibBuilder.loadTexts:hpTunnelIpsecName.setStatus(_B)
_HpTunnelInetConfigTable_Object=MibTable
hpTunnelInetConfigTable=_HpTunnelInetConfigTable_Object((1,3,6,1,4,1,11,2,14,11,5,1,77,1,3))
if mibBuilder.loadTexts:hpTunnelInetConfigTable.setStatus(_B)
_HpTunnelInetConfigEntry_Object=MibTableRow
hpTunnelInetConfigEntry=_HpTunnelInetConfigEntry_Object((1,3,6,1,4,1,11,2,14,11,5,1,77,1,3,1))
if mibBuilder.loadTexts:hpTunnelInetConfigEntry.setStatus(_B)
_HpTunnelInetConfigEncapsMethod_Type=HpTunnelType
_HpTunnelInetConfigEncapsMethod_Object=MibTableColumn
hpTunnelInetConfigEncapsMethod=_HpTunnelInetConfigEncapsMethod_Object((1,3,6,1,4,1,11,2,14,11,5,1,77,1,3,1,1),_HpTunnelInetConfigEncapsMethod_Type())
hpTunnelInetConfigEncapsMethod.setMaxAccess(_D)
if mibBuilder.loadTexts:hpTunnelInetConfigEncapsMethod.setStatus(_B)
_HpicfVlanTunnelMappingTable_Object=MibTable
hpicfVlanTunnelMappingTable=_HpicfVlanTunnelMappingTable_Object((1,3,6,1,4,1,11,2,14,11,5,1,77,1,4))
if mibBuilder.loadTexts:hpicfVlanTunnelMappingTable.setStatus(_B)
_HpicfVlanTunnelMappingEntry_Object=MibTableRow
hpicfVlanTunnelMappingEntry=_HpicfVlanTunnelMappingEntry_Object((1,3,6,1,4,1,11,2,14,11,5,1,77,1,4,1))
hpicfVlanTunnelMappingEntry.setIndexNames((0,_A,_g),(0,_A,_h))
if mibBuilder.loadTexts:hpicfVlanTunnelMappingEntry.setStatus(_B)
_HpicfVLANIndex_Type=VlanIndex
_HpicfVLANIndex_Object=MibTableColumn
hpicfVLANIndex=_HpicfVLANIndex_Object((1,3,6,1,4,1,11,2,14,11,5,1,77,1,4,1,1),_HpicfVLANIndex_Type())
hpicfVLANIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:hpicfVLANIndex.setStatus(_B)
_HpicfTunnelIfIndex_Type=InterfaceIndex
_HpicfTunnelIfIndex_Object=MibTableColumn
hpicfTunnelIfIndex=_HpicfTunnelIfIndex_Object((1,3,6,1,4,1,11,2,14,11,5,1,77,1,4,1,2),_HpicfTunnelIfIndex_Type())
hpicfTunnelIfIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:hpicfTunnelIfIndex.setStatus(_B)
_HpicfVlanTunnelMappingRowStatus_Type=RowStatus
_HpicfVlanTunnelMappingRowStatus_Object=MibTableColumn
hpicfVlanTunnelMappingRowStatus=_HpicfVlanTunnelMappingRowStatus_Object((1,3,6,1,4,1,11,2,14,11,5,1,77,1,4,1,3),_HpicfVlanTunnelMappingRowStatus_Type())
hpicfVlanTunnelMappingRowStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:hpicfVlanTunnelMappingRowStatus.setStatus(_B)
_HpicfUDPTunnelTypeTable_Object=MibTable
hpicfUDPTunnelTypeTable=_HpicfUDPTunnelTypeTable_Object((1,3,6,1,4,1,11,2,14,11,5,1,77,1,5))
if mibBuilder.loadTexts:hpicfUDPTunnelTypeTable.setStatus(_B)
_HpicfUDPTunnelTypeEntry_Object=MibTableRow
hpicfUDPTunnelTypeEntry=_HpicfUDPTunnelTypeEntry_Object((1,3,6,1,4,1,11,2,14,11,5,1,77,1,5,1))
if mibBuilder.loadTexts:hpicfUDPTunnelTypeEntry.setStatus(_B)
class _HpicfUDPTunnelType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('none',0),('remotemirror',1),('vxlan',2)))
_HpicfUDPTunnelType_Type.__name__=_E
_HpicfUDPTunnelType_Object=MibTableColumn
hpicfUDPTunnelType=_HpicfUDPTunnelType_Object((1,3,6,1,4,1,11,2,14,11,5,1,77,1,5,1,1),_HpicfUDPTunnelType_Type())
hpicfUDPTunnelType.setMaxAccess(_G)
if mibBuilder.loadTexts:hpicfUDPTunnelType.setStatus(_B)
_HpTunnelNotifyScalars_ObjectIdentity=ObjectIdentity
hpTunnelNotifyScalars=_HpTunnelNotifyScalars_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,77,1,6))
_HpTunnelMTUDropRouterAddrType_Type=InetAddressType
_HpTunnelMTUDropRouterAddrType_Object=MibScalar
hpTunnelMTUDropRouterAddrType=_HpTunnelMTUDropRouterAddrType_Object((1,3,6,1,4,1,11,2,14,11,5,1,77,1,6,1),_HpTunnelMTUDropRouterAddrType_Type())
hpTunnelMTUDropRouterAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:hpTunnelMTUDropRouterAddrType.setStatus(_B)
_HpTunnelMTUDropRouterAddr_Type=InetAddress
_HpTunnelMTUDropRouterAddr_Object=MibScalar
hpTunnelMTUDropRouterAddr=_HpTunnelMTUDropRouterAddr_Object((1,3,6,1,4,1,11,2,14,11,5,1,77,1,6,2),_HpTunnelMTUDropRouterAddr_Type())
hpTunnelMTUDropRouterAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:hpTunnelMTUDropRouterAddr.setStatus(_B)
_HpTunnelMTUDropRouterMTU_Type=Integer32
_HpTunnelMTUDropRouterMTU_Object=MibScalar
hpTunnelMTUDropRouterMTU=_HpTunnelMTUDropRouterMTU_Object((1,3,6,1,4,1,11,2,14,11,5,1,77,1,6,3),_HpTunnelMTUDropRouterMTU_Type())
hpTunnelMTUDropRouterMTU.setMaxAccess(_C)
if mibBuilder.loadTexts:hpTunnelMTUDropRouterMTU.setStatus(_B)
_HpTunnelMTUDropTunnelSrcAddrType_Type=InetAddressType
_HpTunnelMTUDropTunnelSrcAddrType_Object=MibScalar
hpTunnelMTUDropTunnelSrcAddrType=_HpTunnelMTUDropTunnelSrcAddrType_Object((1,3,6,1,4,1,11,2,14,11,5,1,77,1,6,4),_HpTunnelMTUDropTunnelSrcAddrType_Type())
hpTunnelMTUDropTunnelSrcAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:hpTunnelMTUDropTunnelSrcAddrType.setStatus(_B)
_HpTunnelMTUDropTunnelSource_Type=InetAddress
_HpTunnelMTUDropTunnelSource_Object=MibScalar
hpTunnelMTUDropTunnelSource=_HpTunnelMTUDropTunnelSource_Object((1,3,6,1,4,1,11,2,14,11,5,1,77,1,6,5),_HpTunnelMTUDropTunnelSource_Type())
hpTunnelMTUDropTunnelSource.setMaxAccess(_C)
if mibBuilder.loadTexts:hpTunnelMTUDropTunnelSource.setStatus(_B)
_HpTunnelMTUDropTunnelDstAddrType_Type=InetAddressType
_HpTunnelMTUDropTunnelDstAddrType_Object=MibScalar
hpTunnelMTUDropTunnelDstAddrType=_HpTunnelMTUDropTunnelDstAddrType_Object((1,3,6,1,4,1,11,2,14,11,5,1,77,1,6,6),_HpTunnelMTUDropTunnelDstAddrType_Type())
hpTunnelMTUDropTunnelDstAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:hpTunnelMTUDropTunnelDstAddrType.setStatus(_B)
_HpTunnelMTUDropTunnelDest_Type=InetAddress
_HpTunnelMTUDropTunnelDest_Object=MibScalar
hpTunnelMTUDropTunnelDest=_HpTunnelMTUDropTunnelDest_Object((1,3,6,1,4,1,11,2,14,11,5,1,77,1,6,7),_HpTunnelMTUDropTunnelDest_Type())
hpTunnelMTUDropTunnelDest.setMaxAccess(_C)
if mibBuilder.loadTexts:hpTunnelMTUDropTunnelDest.setStatus(_B)
_HpTunnelMTUDropInIfIndex_Type=InterfaceIndex
_HpTunnelMTUDropInIfIndex_Object=MibScalar
hpTunnelMTUDropInIfIndex=_HpTunnelMTUDropInIfIndex_Object((1,3,6,1,4,1,11,2,14,11,5,1,77,1,6,8),_HpTunnelMTUDropInIfIndex_Type())
hpTunnelMTUDropInIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:hpTunnelMTUDropInIfIndex.setStatus(_B)
class _HpTunnelMTUDropNotifyEnable_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_HpTunnelMTUDropNotifyEnable_Type.__name__=_E
_HpTunnelMTUDropNotifyEnable_Object=MibScalar
hpTunnelMTUDropNotifyEnable=_HpTunnelMTUDropNotifyEnable_Object((1,3,6,1,4,1,11,2,14,11,5,1,77,1,6,9),_HpTunnelMTUDropNotifyEnable_Type())
hpTunnelMTUDropNotifyEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:hpTunnelMTUDropNotifyEnable.setStatus(_B)
_HpTunnelConformance_ObjectIdentity=ObjectIdentity
hpTunnelConformance=_HpTunnelConformance_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,77,2))
_HpTunnelMIBCompliances_ObjectIdentity=ObjectIdentity
hpTunnelMIBCompliances=_HpTunnelMIBCompliances_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,77,2,1))
_HpTunnelMIBGroups_ObjectIdentity=ObjectIdentity
hpTunnelMIBGroups=_HpTunnelMIBGroups_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,77,2,2))
tunnelIfEntry.registerAugmentions((_A,_i))
hpTunnelIfEntry.setIndexNames(*tunnelIfEntry.getIndexNames())
tunnelInetConfigEntry.registerAugmentions((_A,_j))
hpTunnelInetConfigEntry.setIndexNames(*tunnelInetConfigEntry.getIndexNames())
tunnelInetConfigEntry.registerAugmentions((_A,_k))
hpicfUDPTunnelTypeEntry.setIndexNames(*tunnelInetConfigEntry.getIndexNames())
hpTunnelProvisionGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,77,2,2,1))
hpTunnelProvisionGroup.setObjects(*((_A,_l),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P)))
if mibBuilder.loadTexts:hpTunnelProvisionGroup.setStatus(_I)
hpTunnelInetConfigGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,77,2,2,2))
hpTunnelInetConfigGroup.setObjects(*((_A,_m),(_A,_n),(_A,_o)))
if mibBuilder.loadTexts:hpTunnelInetConfigGroup.setStatus(_B)
hpVlanTunnelMappingGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,77,2,2,3))
hpVlanTunnelMappingGroup.setObjects((_A,_p))
if mibBuilder.loadTexts:hpVlanTunnelMappingGroup.setStatus(_B)
hpTunnelProvisionGroup2=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,77,2,2,4))
hpTunnelProvisionGroup2.setObjects(*((_A,_q),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P)))
if mibBuilder.loadTexts:hpTunnelProvisionGroup2.setStatus(_B)
hpTunnelNotifyScalarsGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,77,2,2,5))
hpTunnelNotifyScalarsGroup.setObjects(*((_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_r)))
if mibBuilder.loadTexts:hpTunnelNotifyScalarsGroup.setStatus(_B)
hpTunnelIcmpErrorRcvd=NotificationType((1,3,6,1,4,1,11,2,14,11,5,1,77,0,1))
hpTunnelIcmpErrorRcvd.setObjects(*((_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_F,_c),(_F,_d),(_F,_e)))
if mibBuilder.loadTexts:hpTunnelIcmpErrorRcvd.setStatus(_B)
hpTunnelNotificationsGroup=NotificationGroup((1,3,6,1,4,1,11,2,14,11,5,1,77,2,2,6))
hpTunnelNotificationsGroup.setObjects((_A,_s))
if mibBuilder.loadTexts:hpTunnelNotificationsGroup.setStatus(_B)
hpTunnelMIBCompliance=ModuleCompliance((1,3,6,1,4,1,11,2,14,11,5,1,77,2,1,1))
hpTunnelMIBCompliance.setObjects(*((_A,_t),(_A,_Y),(_A,_Z)))
if mibBuilder.loadTexts:hpTunnelMIBCompliance.setStatus(_I)
hpTunnelMIBCompliance2=ModuleCompliance((1,3,6,1,4,1,11,2,14,11,5,1,77,2,1,2))
hpTunnelMIBCompliance2.setObjects(*((_A,_u),(_A,_Y),(_A,_v),(_A,_w),(_A,_Z)))
if mibBuilder.loadTexts:hpTunnelMIBCompliance2.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'HpTunnelType':HpTunnelType,'hpTunnelMIB':hpTunnelMIB,'hpTunnelNotifications':hpTunnelNotifications,_s:hpTunnelIcmpErrorRcvd,'hpTunnelObjects':hpTunnelObjects,'hpTunnelConfigTable':hpTunnelConfigTable,'hpTunnelConfigEntry':hpTunnelConfigEntry,_f:hpTunnelID,_l:hpTunnelIfIndex,_P:hpTunnelRowStatus,_q:hpTunnelInterfaceIndex,'hpTunnelIfTable':hpTunnelIfTable,_i:hpTunnelIfEntry,_M:hpTunnelIfPMTU,_O:hpTunnelIfNUD,_N:hpTunnelIfMTU,_L:hpTunnelEncapsMethod,_n:hpTunnelIpsecName,'hpTunnelInetConfigTable':hpTunnelInetConfigTable,_j:hpTunnelInetConfigEntry,_m:hpTunnelInetConfigEncapsMethod,'hpicfVlanTunnelMappingTable':hpicfVlanTunnelMappingTable,'hpicfVlanTunnelMappingEntry':hpicfVlanTunnelMappingEntry,_g:hpicfVLANIndex,_h:hpicfTunnelIfIndex,_p:hpicfVlanTunnelMappingRowStatus,'hpicfUDPTunnelTypeTable':hpicfUDPTunnelTypeTable,_k:hpicfUDPTunnelTypeEntry,_o:hpicfUDPTunnelType,'hpTunnelNotifyScalars':hpTunnelNotifyScalars,_Q:hpTunnelMTUDropRouterAddrType,_R:hpTunnelMTUDropRouterAddr,_S:hpTunnelMTUDropRouterMTU,_T:hpTunnelMTUDropTunnelSrcAddrType,_U:hpTunnelMTUDropTunnelSource,_V:hpTunnelMTUDropTunnelDstAddrType,_W:hpTunnelMTUDropTunnelDest,_X:hpTunnelMTUDropInIfIndex,_r:hpTunnelMTUDropNotifyEnable,'hpTunnelConformance':hpTunnelConformance,'hpTunnelMIBCompliances':hpTunnelMIBCompliances,'hpTunnelMIBCompliance':hpTunnelMIBCompliance,'hpTunnelMIBCompliance2':hpTunnelMIBCompliance2,'hpTunnelMIBGroups':hpTunnelMIBGroups,_t:hpTunnelProvisionGroup,_Y:hpTunnelInetConfigGroup,_Z:hpVlanTunnelMappingGroup,_u:hpTunnelProvisionGroup2,_v:hpTunnelNotifyScalarsGroup,_w:hpTunnelNotificationsGroup})