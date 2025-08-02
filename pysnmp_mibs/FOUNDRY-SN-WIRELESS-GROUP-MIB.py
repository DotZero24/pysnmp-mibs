_V='wgVpnPTPolicyId'
_U='wgVpnPTFilterPort'
_T='wgVpnPTFilterProtocol'
_S='wgVpnPTFilterPolicyId'
_R='wgVpnPTServerIpAddress'
_Q='wgVpnPTServerPolicyId'
_P='wgPnPMacAddress'
_O='wgPnPIfIndex'
_N='configured'
_M='wgRoamingPeerIpAddress'
_L='wgIfIndex'
_K='create'
_J='delete'
_I='valid'
_H='disable'
_G='enable'
_F='other'
_E='FOUNDRY-SN-WIRELESS-GROUP-MIB'
_D='Integer32'
_C='read-only'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
MacAddress,=mibBuilder.importSymbols('FOUNDRY-SN-AGENT-MIB','MacAddress')
snSwitch,=mibBuilder.importSymbols('FOUNDRY-SN-SWITCH-GROUP-MIB','snSwitch')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
snWireless=ModuleIdentity((1,3,6,1,4,1,1991,1,1,3,23))
if mibBuilder.loadTexts:snWireless.setRevisions(('2009-09-30 00:00','2017-08-07 00:00'))
class IfIndexList(TextualConvention,OctetString):status=_A
_WgGroup_ObjectIdentity=ObjectIdentity
wgGroup=_WgGroup_ObjectIdentity((1,3,6,1,4,1,1991,1,1,3,23,1))
_WgMobilityId_Type=Integer32
_WgMobilityId_Object=MibScalar
wgMobilityId=_WgMobilityId_Object((1,3,6,1,4,1,1991,1,1,3,23,1,1),_WgMobilityId_Type())
wgMobilityId.setMaxAccess(_B)
if mibBuilder.loadTexts:wgMobilityId.setStatus(_A)
_WgVpnPTDeletePolicy_Type=Integer32
_WgVpnPTDeletePolicy_Object=MibScalar
wgVpnPTDeletePolicy=_WgVpnPTDeletePolicy_Object((1,3,6,1,4,1,1991,1,1,3,23,1,2),_WgVpnPTDeletePolicy_Type())
wgVpnPTDeletePolicy.setMaxAccess(_B)
if mibBuilder.loadTexts:wgVpnPTDeletePolicy.setStatus(_A)
_WgIfTable_Object=MibTable
wgIfTable=_WgIfTable_Object((1,3,6,1,4,1,1991,1,1,3,23,2))
if mibBuilder.loadTexts:wgIfTable.setStatus(_A)
_WgIfEntry_Object=MibTableRow
wgIfEntry=_WgIfEntry_Object((1,3,6,1,4,1,1991,1,1,3,23,2,1))
wgIfEntry.setIndexNames((0,_E,_L))
if mibBuilder.loadTexts:wgIfEntry.setStatus(_A)
_WgIfIndex_Type=Integer32
_WgIfIndex_Object=MibTableColumn
wgIfIndex=_WgIfIndex_Object((1,3,6,1,4,1,1991,1,1,3,23,2,1,1),_WgIfIndex_Type())
wgIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:wgIfIndex.setStatus(_A)
class _WgIfWirelessEnable_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_G,2),(_H,3)))
_WgIfWirelessEnable_Type.__name__=_D
_WgIfWirelessEnable_Object=MibTableColumn
wgIfWirelessEnable=_WgIfWirelessEnable_Object((1,3,6,1,4,1,1991,1,1,3,23,2,1,2),_WgIfWirelessEnable_Type())
wgIfWirelessEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:wgIfWirelessEnable.setStatus(_A)
class _WgIfPnPLearnNewAP_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_G,2),(_H,3)))
_WgIfPnPLearnNewAP_Type.__name__=_D
_WgIfPnPLearnNewAP_Object=MibTableColumn
wgIfPnPLearnNewAP=_WgIfPnPLearnNewAP_Object((1,3,6,1,4,1,1991,1,1,3,23,2,1,3),_WgIfPnPLearnNewAP_Type())
wgIfPnPLearnNewAP.setMaxAccess(_B)
if mibBuilder.loadTexts:wgIfPnPLearnNewAP.setStatus(_A)
class _WgIfAutoPortDisable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_G,2),(_H,3)))
_WgIfAutoPortDisable_Type.__name__=_D
_WgIfAutoPortDisable_Object=MibTableColumn
wgIfAutoPortDisable=_WgIfAutoPortDisable_Object((1,3,6,1,4,1,1991,1,1,3,23,2,1,4),_WgIfAutoPortDisable_Type())
wgIfAutoPortDisable.setMaxAccess(_B)
if mibBuilder.loadTexts:wgIfAutoPortDisable.setStatus(_A)
_WgIfVpnPTPolicyId_Type=Integer32
_WgIfVpnPTPolicyId_Object=MibTableColumn
wgIfVpnPTPolicyId=_WgIfVpnPTPolicyId_Object((1,3,6,1,4,1,1991,1,1,3,23,2,1,5),_WgIfVpnPTPolicyId_Type())
wgIfVpnPTPolicyId.setMaxAccess(_B)
if mibBuilder.loadTexts:wgIfVpnPTPolicyId.setStatus(_A)
class _WgIfFullCompRoamingEnable_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_G,2),(_H,3)))
_WgIfFullCompRoamingEnable_Type.__name__=_D
_WgIfFullCompRoamingEnable_Object=MibTableColumn
wgIfFullCompRoamingEnable=_WgIfFullCompRoamingEnable_Object((1,3,6,1,4,1,1991,1,1,3,23,2,1,6),_WgIfFullCompRoamingEnable_Type())
wgIfFullCompRoamingEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:wgIfFullCompRoamingEnable.setStatus(_A)
_WgRoamingPeerTable_Object=MibTable
wgRoamingPeerTable=_WgRoamingPeerTable_Object((1,3,6,1,4,1,1991,1,1,3,23,3))
if mibBuilder.loadTexts:wgRoamingPeerTable.setStatus(_A)
_WgRoamingPeerEntry_Object=MibTableRow
wgRoamingPeerEntry=_WgRoamingPeerEntry_Object((1,3,6,1,4,1,1991,1,1,3,23,3,1))
wgRoamingPeerEntry.setIndexNames((0,_E,_M))
if mibBuilder.loadTexts:wgRoamingPeerEntry.setStatus(_A)
_WgRoamingPeerIpAddress_Type=IpAddress
_WgRoamingPeerIpAddress_Object=MibTableColumn
wgRoamingPeerIpAddress=_WgRoamingPeerIpAddress_Object((1,3,6,1,4,1,1991,1,1,3,23,3,1,1),_WgRoamingPeerIpAddress_Type())
wgRoamingPeerIpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:wgRoamingPeerIpAddress.setStatus(_A)
class _WgRoamingPeerConnectionStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_N,2),('established',3)))
_WgRoamingPeerConnectionStatus_Type.__name__=_D
_WgRoamingPeerConnectionStatus_Object=MibTableColumn
wgRoamingPeerConnectionStatus=_WgRoamingPeerConnectionStatus_Object((1,3,6,1,4,1,1991,1,1,3,23,3,1,2),_WgRoamingPeerConnectionStatus_Type())
wgRoamingPeerConnectionStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:wgRoamingPeerConnectionStatus.setStatus(_A)
class _WgRoamingPeerRowStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_F,1),(_I,2),(_J,3),(_K,4)))
_WgRoamingPeerRowStatus_Type.__name__=_D
_WgRoamingPeerRowStatus_Object=MibTableColumn
wgRoamingPeerRowStatus=_WgRoamingPeerRowStatus_Object((1,3,6,1,4,1,1991,1,1,3,23,3,1,3),_WgRoamingPeerRowStatus_Type())
wgRoamingPeerRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:wgRoamingPeerRowStatus.setStatus(_A)
_WgPnPTable_Object=MibTable
wgPnPTable=_WgPnPTable_Object((1,3,6,1,4,1,1991,1,1,3,23,4))
if mibBuilder.loadTexts:wgPnPTable.setStatus(_A)
_WgPnPEntry_Object=MibTableRow
wgPnPEntry=_WgPnPEntry_Object((1,3,6,1,4,1,1991,1,1,3,23,4,1))
wgPnPEntry.setIndexNames((0,_E,_O),(0,_E,_P))
if mibBuilder.loadTexts:wgPnPEntry.setStatus(_A)
_WgPnPIfIndex_Type=Integer32
_WgPnPIfIndex_Object=MibTableColumn
wgPnPIfIndex=_WgPnPIfIndex_Object((1,3,6,1,4,1,1991,1,1,3,23,4,1,1),_WgPnPIfIndex_Type())
wgPnPIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:wgPnPIfIndex.setStatus(_A)
_WgPnPMacAddress_Type=MacAddress
_WgPnPMacAddress_Object=MibTableColumn
wgPnPMacAddress=_WgPnPMacAddress_Object((1,3,6,1,4,1,1991,1,1,3,23,4,1,2),_WgPnPMacAddress_Type())
wgPnPMacAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:wgPnPMacAddress.setStatus(_A)
_WgPnPIpAddress_Type=IpAddress
_WgPnPIpAddress_Object=MibTableColumn
wgPnPIpAddress=_WgPnPIpAddress_Object((1,3,6,1,4,1,1991,1,1,3,23,4,1,3),_WgPnPIpAddress_Type())
wgPnPIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:wgPnPIpAddress.setStatus(_A)
_WgPnPIpMask_Type=IpAddress
_WgPnPIpMask_Object=MibTableColumn
wgPnPIpMask=_WgPnPIpMask_Object((1,3,6,1,4,1,1991,1,1,3,23,4,1,4),_WgPnPIpMask_Type())
wgPnPIpMask.setMaxAccess(_B)
if mibBuilder.loadTexts:wgPnPIpMask.setStatus(_A)
_WgPnPIpDefaultGw_Type=IpAddress
_WgPnPIpDefaultGw_Object=MibTableColumn
wgPnPIpDefaultGw=_WgPnPIpDefaultGw_Object((1,3,6,1,4,1,1991,1,1,3,23,4,1,5),_WgPnPIpDefaultGw_Type())
wgPnPIpDefaultGw.setMaxAccess(_B)
if mibBuilder.loadTexts:wgPnPIpDefaultGw.setStatus(_A)
class _WgPnPStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_F,1),('discovered',2),(_N,3),('operational',4)))
_WgPnPStatus_Type.__name__=_D
_WgPnPStatus_Object=MibTableColumn
wgPnPStatus=_WgPnPStatus_Object((1,3,6,1,4,1,1991,1,1,3,23,4,1,6),_WgPnPStatus_Type())
wgPnPStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:wgPnPStatus.setStatus(_A)
class _WgPnPRowStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_F,1),(_I,2),(_J,3),(_K,4),('modify',5)))
_WgPnPRowStatus_Type.__name__=_D
_WgPnPRowStatus_Object=MibTableColumn
wgPnPRowStatus=_WgPnPRowStatus_Object((1,3,6,1,4,1,1991,1,1,3,23,4,1,7),_WgPnPRowStatus_Type())
wgPnPRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:wgPnPRowStatus.setStatus(_A)
_WgVpnPTServerTable_Object=MibTable
wgVpnPTServerTable=_WgVpnPTServerTable_Object((1,3,6,1,4,1,1991,1,1,3,23,5))
if mibBuilder.loadTexts:wgVpnPTServerTable.setStatus(_A)
_WgVpnPTServerEntry_Object=MibTableRow
wgVpnPTServerEntry=_WgVpnPTServerEntry_Object((1,3,6,1,4,1,1991,1,1,3,23,5,1))
wgVpnPTServerEntry.setIndexNames((0,_E,_Q),(0,_E,_R))
if mibBuilder.loadTexts:wgVpnPTServerEntry.setStatus(_A)
_WgVpnPTServerPolicyId_Type=Integer32
_WgVpnPTServerPolicyId_Object=MibTableColumn
wgVpnPTServerPolicyId=_WgVpnPTServerPolicyId_Object((1,3,6,1,4,1,1991,1,1,3,23,5,1,1),_WgVpnPTServerPolicyId_Type())
wgVpnPTServerPolicyId.setMaxAccess(_C)
if mibBuilder.loadTexts:wgVpnPTServerPolicyId.setStatus(_A)
_WgVpnPTServerIpAddress_Type=IpAddress
_WgVpnPTServerIpAddress_Object=MibTableColumn
wgVpnPTServerIpAddress=_WgVpnPTServerIpAddress_Object((1,3,6,1,4,1,1991,1,1,3,23,5,1,2),_WgVpnPTServerIpAddress_Type())
wgVpnPTServerIpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:wgVpnPTServerIpAddress.setStatus(_A)
class _WgVpnPTServerRowStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_F,1),(_I,2),(_J,3),(_K,4)))
_WgVpnPTServerRowStatus_Type.__name__=_D
_WgVpnPTServerRowStatus_Object=MibTableColumn
wgVpnPTServerRowStatus=_WgVpnPTServerRowStatus_Object((1,3,6,1,4,1,1991,1,1,3,23,5,1,3),_WgVpnPTServerRowStatus_Type())
wgVpnPTServerRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:wgVpnPTServerRowStatus.setStatus(_A)
_WgVpnPTFilterTable_Object=MibTable
wgVpnPTFilterTable=_WgVpnPTFilterTable_Object((1,3,6,1,4,1,1991,1,1,3,23,6))
if mibBuilder.loadTexts:wgVpnPTFilterTable.setStatus(_A)
_WgVpnPTFilterEntry_Object=MibTableRow
wgVpnPTFilterEntry=_WgVpnPTFilterEntry_Object((1,3,6,1,4,1,1991,1,1,3,23,6,1))
wgVpnPTFilterEntry.setIndexNames((0,_E,_S),(0,_E,_T),(0,_E,_U))
if mibBuilder.loadTexts:wgVpnPTFilterEntry.setStatus(_A)
_WgVpnPTFilterPolicyId_Type=Integer32
_WgVpnPTFilterPolicyId_Object=MibTableColumn
wgVpnPTFilterPolicyId=_WgVpnPTFilterPolicyId_Object((1,3,6,1,4,1,1991,1,1,3,23,6,1,1),_WgVpnPTFilterPolicyId_Type())
wgVpnPTFilterPolicyId.setMaxAccess(_C)
if mibBuilder.loadTexts:wgVpnPTFilterPolicyId.setStatus(_A)
class _WgVpnPTFilterProtocol_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),('udp',2),('tcp',3)))
_WgVpnPTFilterProtocol_Type.__name__=_D
_WgVpnPTFilterProtocol_Object=MibTableColumn
wgVpnPTFilterProtocol=_WgVpnPTFilterProtocol_Object((1,3,6,1,4,1,1991,1,1,3,23,6,1,2),_WgVpnPTFilterProtocol_Type())
wgVpnPTFilterProtocol.setMaxAccess(_C)
if mibBuilder.loadTexts:wgVpnPTFilterProtocol.setStatus(_A)
_WgVpnPTFilterPort_Type=Integer32
_WgVpnPTFilterPort_Object=MibTableColumn
wgVpnPTFilterPort=_WgVpnPTFilterPort_Object((1,3,6,1,4,1,1991,1,1,3,23,6,1,3),_WgVpnPTFilterPort_Type())
wgVpnPTFilterPort.setMaxAccess(_C)
if mibBuilder.loadTexts:wgVpnPTFilterPort.setStatus(_A)
class _WgVpnPTFilterRowStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_F,1),(_I,2),(_J,3),(_K,4)))
_WgVpnPTFilterRowStatus_Type.__name__=_D
_WgVpnPTFilterRowStatus_Object=MibTableColumn
wgVpnPTFilterRowStatus=_WgVpnPTFilterRowStatus_Object((1,3,6,1,4,1,1991,1,1,3,23,6,1,4),_WgVpnPTFilterRowStatus_Type())
wgVpnPTFilterRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:wgVpnPTFilterRowStatus.setStatus(_A)
_WgVpnPTPolicyTable_Object=MibTable
wgVpnPTPolicyTable=_WgVpnPTPolicyTable_Object((1,3,6,1,4,1,1991,1,1,3,23,7))
if mibBuilder.loadTexts:wgVpnPTPolicyTable.setStatus(_A)
_WgVpnPTPolicyEntry_Object=MibTableRow
wgVpnPTPolicyEntry=_WgVpnPTPolicyEntry_Object((1,3,6,1,4,1,1991,1,1,3,23,7,1))
wgVpnPTPolicyEntry.setIndexNames((0,_E,_V))
if mibBuilder.loadTexts:wgVpnPTPolicyEntry.setStatus(_A)
_WgVpnPTPolicyId_Type=Integer32
_WgVpnPTPolicyId_Object=MibTableColumn
wgVpnPTPolicyId=_WgVpnPTPolicyId_Object((1,3,6,1,4,1,1991,1,1,3,23,7,1,1),_WgVpnPTPolicyId_Type())
wgVpnPTPolicyId.setMaxAccess(_C)
if mibBuilder.loadTexts:wgVpnPTPolicyId.setStatus(_A)
_WgVpnPTPolicyPortList_Type=IfIndexList
_WgVpnPTPolicyPortList_Object=MibTableColumn
wgVpnPTPolicyPortList=_WgVpnPTPolicyPortList_Object((1,3,6,1,4,1,1991,1,1,3,23,7,1,2),_WgVpnPTPolicyPortList_Type())
wgVpnPTPolicyPortList.setMaxAccess(_C)
if mibBuilder.loadTexts:wgVpnPTPolicyPortList.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'IfIndexList':IfIndexList,'snWireless':snWireless,'wgGroup':wgGroup,'wgMobilityId':wgMobilityId,'wgVpnPTDeletePolicy':wgVpnPTDeletePolicy,'wgIfTable':wgIfTable,'wgIfEntry':wgIfEntry,_L:wgIfIndex,'wgIfWirelessEnable':wgIfWirelessEnable,'wgIfPnPLearnNewAP':wgIfPnPLearnNewAP,'wgIfAutoPortDisable':wgIfAutoPortDisable,'wgIfVpnPTPolicyId':wgIfVpnPTPolicyId,'wgIfFullCompRoamingEnable':wgIfFullCompRoamingEnable,'wgRoamingPeerTable':wgRoamingPeerTable,'wgRoamingPeerEntry':wgRoamingPeerEntry,_M:wgRoamingPeerIpAddress,'wgRoamingPeerConnectionStatus':wgRoamingPeerConnectionStatus,'wgRoamingPeerRowStatus':wgRoamingPeerRowStatus,'wgPnPTable':wgPnPTable,'wgPnPEntry':wgPnPEntry,_O:wgPnPIfIndex,_P:wgPnPMacAddress,'wgPnPIpAddress':wgPnPIpAddress,'wgPnPIpMask':wgPnPIpMask,'wgPnPIpDefaultGw':wgPnPIpDefaultGw,'wgPnPStatus':wgPnPStatus,'wgPnPRowStatus':wgPnPRowStatus,'wgVpnPTServerTable':wgVpnPTServerTable,'wgVpnPTServerEntry':wgVpnPTServerEntry,_Q:wgVpnPTServerPolicyId,_R:wgVpnPTServerIpAddress,'wgVpnPTServerRowStatus':wgVpnPTServerRowStatus,'wgVpnPTFilterTable':wgVpnPTFilterTable,'wgVpnPTFilterEntry':wgVpnPTFilterEntry,_S:wgVpnPTFilterPolicyId,_T:wgVpnPTFilterProtocol,_U:wgVpnPTFilterPort,'wgVpnPTFilterRowStatus':wgVpnPTFilterRowStatus,'wgVpnPTPolicyTable':wgVpnPTPolicyTable,'wgVpnPTPolicyEntry':wgVpnPTPolicyEntry,_V:wgVpnPTPolicyId,'wgVpnPTPolicyPortList':wgVpnPTPolicyPortList})