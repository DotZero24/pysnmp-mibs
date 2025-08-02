_AL='ffHostCacheEntryType'
_AK='ffHostCacheIfIndex'
_AJ='fmMemAllocFailCount'
_AI='fmTimerReqFailCount'
_AH='ifHCErrorEntry'
_AG='ifMainExtEntry'
_AF='fsPacketTransmitterIndex'
_AE='fsPacketAnalyserIndex'
_AD='ffHostCacheDestAddr'
_AC='ifUfdGroupId'
_AB='ifIvrAssociatedVlan'
_AA='ifTypeProtoDenyProtocol'
_A9='ifTypeProtoDenyBrgPortType'
_A8='ifTypeProtoDenyMainType'
_A7='ifTypeProtoDenyContextId'
_A6='ifCustOpaqueAttributeID'
_A5='ifCustTLVType'
_A4='ifSecondaryIpAddress'
_A3='ifAutoProfileIfIndex'
_A2='negotiation'
_A1='customerBackbonePort'
_A0='providerInstancePort'
_z='virtualInstancePort'
_y='customerNetworkPortCtagged'
_x='customerBridgePort'
_w='propProviderNetworkPort'
_v='propCustomerNetworkPort'
_u='propCustomerEdgePort'
_t='customerEdgePort'
_s='customerNetworkPortStagged'
_r='customerNetworkPortPortBased'
_q='providerNetworkPort'
_p='vcMultiplexed'
_o='llcSnap'
_n='cudNlpidSnap'
_m='cudNlpid'
_l='nlpidSnap'
_k='testing'
_j='brgPort'
_i='ieee8023ad'
_h='atmSubInterface'
_g='ipOverAtm'
_f='pppMultilinkBundle'
_e='frameRelayMPI'
_d='propVirtual'
_c='miox25'
_b='frameRelay'
_a='ethernetCsmacd'
_Z='rfc877x25'
_Y='StorageType'
_X='ifType'
_W='ifIndex'
_V='ifMainUfdOperStatus'
_U='IF-MIB'
_T='00000000'
_S='down'
_R='up'
_Q='disabled'
_P='enabled'
_O='DisplayString'
_N='IpAddress'
_M='other'
_L='Unsigned32'
_K='OctetString'
_J='TruthValue'
_I='not-accessible'
_H='ifMainIndex'
_G='read-create'
_F='read-only'
_E='ARICENT-CFA-MIB'
_D='Integer32'
_C='deprecated'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_K,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,ifEntry,ifIndex,ifType=mibBuilder.importSymbols(_U,'InterfaceIndex','ifEntry',_W,_X)
PortList,VlanId=mibBuilder.importSymbols('Q-BRIDGE-MIB','PortList','VlanId')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,_N,'ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_L,'enterprises','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,StorageType,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_O,'MacAddress','PhysAddress','RowStatus',_Y,'TextualConvention','TimeStamp',_J)
fscfa=ModuleIdentity((1,3,6,1,4,1,2076,27))
if mibBuilder.loadTexts:fscfa.setRevisions(('2012-09-05 00:00','1999-12-17 13:30'))
__pysmi_if_ObjectIdentity=ObjectIdentity
_pysmi_if=__pysmi_if_ObjectIdentity((1,3,6,1,4,1,2076,27,1))
_IfMaxInterfaces_Type=InterfaceIndex
_IfMaxInterfaces_Object=MibScalar
ifMaxInterfaces=_IfMaxInterfaces_Object((1,3,6,1,4,1,2076,27,1,1),_IfMaxInterfaces_Type())
ifMaxInterfaces.setMaxAccess(_B)
if mibBuilder.loadTexts:ifMaxInterfaces.setStatus(_C)
_IfMaxPhysInterfaces_Type=InterfaceIndex
_IfMaxPhysInterfaces_Object=MibScalar
ifMaxPhysInterfaces=_IfMaxPhysInterfaces_Object((1,3,6,1,4,1,2076,27,1,2),_IfMaxPhysInterfaces_Type())
ifMaxPhysInterfaces.setMaxAccess(_B)
if mibBuilder.loadTexts:ifMaxPhysInterfaces.setStatus(_C)
_IfAvailableIndex_Type=InterfaceIndex
_IfAvailableIndex_Object=MibScalar
ifAvailableIndex=_IfAvailableIndex_Object((1,3,6,1,4,1,2076,27,1,3),_IfAvailableIndex_Type())
ifAvailableIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:ifAvailableIndex.setStatus(_A)
_IfMainTable_Object=MibTable
ifMainTable=_IfMainTable_Object((1,3,6,1,4,1,2076,27,1,4))
if mibBuilder.loadTexts:ifMainTable.setStatus(_A)
_IfMainEntry_Object=MibTableRow
ifMainEntry=_IfMainEntry_Object((1,3,6,1,4,1,2076,27,1,4,1))
ifMainEntry.setIndexNames((0,_E,_H))
if mibBuilder.loadTexts:ifMainEntry.setStatus(_A)
_IfMainIndex_Type=InterfaceIndex
_IfMainIndex_Object=MibTableColumn
ifMainIndex=_IfMainIndex_Object((1,3,6,1,4,1,2076,27,1,4,1,1),_IfMainIndex_Type())
ifMainIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:ifMainIndex.setStatus(_A)
class _IfMainType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(5,6,9,23,24,32,38,49,53,84,92,108,114,118,131,134,136,150,161,166,200,209,246,247,248)));namedValues=NamedValues(*((_Z,5),(_a,6),('iso88025TokenRing',9),('ppp',23),('softwareLoopback',24),(_b,32),(_c,38),('aal5',49),(_d,53),('async',84),(_e,92),(_f,108),(_g,114),('hdlc',118),('tunnel',131),(_h,134),('l3ipvlan',136),('mplsTunnel',150),(_i,161),('mpls',166),('teLink',200),(_j,209),('ifPwType',246),('ilan',247),('pip',248)))
_IfMainType_Type.__name__=_D
_IfMainType_Object=MibTableColumn
ifMainType=_IfMainType_Object((1,3,6,1,4,1,2076,27,1,4,1,2),_IfMainType_Type())
ifMainType.setMaxAccess(_G)
if mibBuilder.loadTexts:ifMainType.setStatus(_A)
_IfMainMtu_Type=Integer32
_IfMainMtu_Object=MibTableColumn
ifMainMtu=_IfMainMtu_Object((1,3,6,1,4,1,2076,27,1,4,1,3),_IfMainMtu_Type())
ifMainMtu.setMaxAccess(_G)
if mibBuilder.loadTexts:ifMainMtu.setStatus(_A)
class _IfMainAdminStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,50)));namedValues=NamedValues(*((_R,1),(_S,2),(_k,3),('loopback',4),('loopbackExternal',50)))
_IfMainAdminStatus_Type.__name__=_D
_IfMainAdminStatus_Object=MibTableColumn
ifMainAdminStatus=_IfMainAdminStatus_Object((1,3,6,1,4,1,2076,27,1,4,1,4),_IfMainAdminStatus_Type())
ifMainAdminStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:ifMainAdminStatus.setStatus(_A)
class _IfMainOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_R,1),(_S,2),(_k,3),('unknown',4),('dormant',5),('notPresent',6),('lowerLayerDown',7)))
_IfMainOperStatus_Type.__name__=_D
_IfMainOperStatus_Object=MibTableColumn
ifMainOperStatus=_IfMainOperStatus_Object((1,3,6,1,4,1,2076,27,1,4,1,5),_IfMainOperStatus_Type())
ifMainOperStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:ifMainOperStatus.setStatus(_A)
class _IfMainEncapType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_M,1),('nlpid',2),(_l,3),(_m,4),(_n,5),(_o,6),(_p,7),('ethernetV2',8)))
_IfMainEncapType_Type.__name__=_D
_IfMainEncapType_Object=MibTableColumn
ifMainEncapType=_IfMainEncapType_Object((1,3,6,1,4,1,2076,27,1,4,1,6),_IfMainEncapType_Type())
ifMainEncapType.setMaxAccess(_B)
if mibBuilder.loadTexts:ifMainEncapType.setStatus(_A)
class _IfMainBrgPortType_Type(Integer32):defaultValue=8;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14)));namedValues=NamedValues(*((_q,1),(_r,2),(_s,3),(_t,4),(_u,5),(_v,6),(_w,7),(_x,8),(_y,9),(_z,10),(_A0,11),(_A1,12),('uplinkAccessPort',13),('stationFacingBridgePort',14)))
_IfMainBrgPortType_Type.__name__=_D
_IfMainBrgPortType_Object=MibTableColumn
ifMainBrgPortType=_IfMainBrgPortType_Object((1,3,6,1,4,1,2076,27,1,4,1,7),_IfMainBrgPortType_Type())
ifMainBrgPortType.setMaxAccess(_B)
if mibBuilder.loadTexts:ifMainBrgPortType.setStatus(_A)
_IfMainRowStatus_Type=RowStatus
_IfMainRowStatus_Object=MibTableColumn
ifMainRowStatus=_IfMainRowStatus_Object((1,3,6,1,4,1,2076,27,1,4,1,8),_IfMainRowStatus_Type())
ifMainRowStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:ifMainRowStatus.setStatus(_A)
class _IfMainSubType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(251,252,253,254,255)));namedValues=NamedValues(*(('extremeEther',251),('fastEther',252),('gigabitEthernet',253),('xlEthernet',254),('notApplicable',255)))
_IfMainSubType_Type.__name__=_D
_IfMainSubType_Object=MibTableColumn
ifMainSubType=_IfMainSubType_Object((1,3,6,1,4,1,2076,27,1,4,1,9),_IfMainSubType_Type())
ifMainSubType.setMaxAccess(_B)
if mibBuilder.loadTexts:ifMainSubType.setStatus(_A)
class _IfMainNetworkType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('lan',1),('wan',2)))
_IfMainNetworkType_Type.__name__=_D
_IfMainNetworkType_Object=MibTableColumn
ifMainNetworkType=_IfMainNetworkType_Object((1,3,6,1,4,1,2076,27,1,4,1,10),_IfMainNetworkType_Type())
ifMainNetworkType.setMaxAccess(_B)
if mibBuilder.loadTexts:ifMainNetworkType.setStatus(_A)
class _IfMainWanType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_M,0),('private',1),('public',2)))
_IfMainWanType_Type.__name__=_D
_IfMainWanType_Object=MibTableColumn
ifMainWanType=_IfMainWanType_Object((1,3,6,1,4,1,2076,27,1,4,1,11),_IfMainWanType_Type())
ifMainWanType.setMaxAccess(_B)
if mibBuilder.loadTexts:ifMainWanType.setStatus(_A)
_IfMainDesc_Type=DisplayString
_IfMainDesc_Object=MibTableColumn
ifMainDesc=_IfMainDesc_Object((1,3,6,1,4,1,2076,27,1,4,1,12),_IfMainDesc_Type())
ifMainDesc.setMaxAccess(_B)
if mibBuilder.loadTexts:ifMainDesc.setStatus(_A)
class _IfMainStorageType_Type(StorageType):defaultValue=3
_IfMainStorageType_Type.__name__=_Y
_IfMainStorageType_Object=MibTableColumn
ifMainStorageType=_IfMainStorageType_Object((1,3,6,1,4,1,2076,27,1,4,1,13),_IfMainStorageType_Type())
ifMainStorageType.setMaxAccess(_G)
if mibBuilder.loadTexts:ifMainStorageType.setStatus(_A)
class _IfMainExtSubType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('sisp',0),('attachmentCircuit',1),('openflow',2)))
_IfMainExtSubType_Type.__name__=_D
_IfMainExtSubType_Object=MibTableColumn
ifMainExtSubType=_IfMainExtSubType_Object((1,3,6,1,4,1,2076,27,1,4,1,14),_IfMainExtSubType_Type())
ifMainExtSubType.setMaxAccess(_B)
if mibBuilder.loadTexts:ifMainExtSubType.setStatus(_A)
class _IfMainPortRole_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('uplink',1),('downlink',2)))
_IfMainPortRole_Type.__name__=_D
_IfMainPortRole_Object=MibTableColumn
ifMainPortRole=_IfMainPortRole_Object((1,3,6,1,4,1,2076,27,1,4,1,15),_IfMainPortRole_Type())
ifMainPortRole.setMaxAccess(_B)
if mibBuilder.loadTexts:ifMainPortRole.setStatus(_A)
class _IfMainUfdOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_R,1),(_S,2),('ufdErrorDisabled',3)))
_IfMainUfdOperStatus_Type.__name__=_D
_IfMainUfdOperStatus_Object=MibTableColumn
ifMainUfdOperStatus=_IfMainUfdOperStatus_Object((1,3,6,1,4,1,2076,27,1,4,1,16),_IfMainUfdOperStatus_Type())
ifMainUfdOperStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:ifMainUfdOperStatus.setStatus(_A)
class _IfMainUfdGroupId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_IfMainUfdGroupId_Type.__name__=_D
_IfMainUfdGroupId_Object=MibTableColumn
ifMainUfdGroupId=_IfMainUfdGroupId_Object((1,3,6,1,4,1,2076,27,1,4,1,17),_IfMainUfdGroupId_Type())
ifMainUfdGroupId.setMaxAccess(_B)
if mibBuilder.loadTexts:ifMainUfdGroupId.setStatus(_A)
_IfMainUfdDownlinkDisabledCount_Type=Counter32
_IfMainUfdDownlinkDisabledCount_Object=MibTableColumn
ifMainUfdDownlinkDisabledCount=_IfMainUfdDownlinkDisabledCount_Object((1,3,6,1,4,1,2076,27,1,4,1,18),_IfMainUfdDownlinkDisabledCount_Type())
ifMainUfdDownlinkDisabledCount.setMaxAccess(_F)
if mibBuilder.loadTexts:ifMainUfdDownlinkDisabledCount.setStatus(_C)
_IfMainUfdDownlinkEnabledCount_Type=Counter32
_IfMainUfdDownlinkEnabledCount_Object=MibTableColumn
ifMainUfdDownlinkEnabledCount=_IfMainUfdDownlinkEnabledCount_Object((1,3,6,1,4,1,2076,27,1,4,1,19),_IfMainUfdDownlinkEnabledCount_Type())
ifMainUfdDownlinkEnabledCount.setMaxAccess(_F)
if mibBuilder.loadTexts:ifMainUfdDownlinkEnabledCount.setStatus(_C)
class _IfMainDesigUplinkStatus_Type(TruthValue):defaultValue=2
_IfMainDesigUplinkStatus_Type.__name__=_J
_IfMainDesigUplinkStatus_Object=MibTableColumn
ifMainDesigUplinkStatus=_IfMainDesigUplinkStatus_Object((1,3,6,1,4,1,2076,27,1,4,1,20),_IfMainDesigUplinkStatus_Type())
ifMainDesigUplinkStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:ifMainDesigUplinkStatus.setStatus(_A)
_IfIpTable_Object=MibTable
ifIpTable=_IfIpTable_Object((1,3,6,1,4,1,2076,27,1,5))
if mibBuilder.loadTexts:ifIpTable.setStatus(_A)
_IfIpEntry_Object=MibTableRow
ifIpEntry=_IfIpEntry_Object((1,3,6,1,4,1,2076,27,1,5,1))
ifIpEntry.setIndexNames((0,_E,_H))
if mibBuilder.loadTexts:ifIpEntry.setStatus(_A)
class _IfIpAddrAllocMethod_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('manual',1),(_A2,2),('dynamic',3),('none',4)))
_IfIpAddrAllocMethod_Type.__name__=_D
_IfIpAddrAllocMethod_Object=MibTableColumn
ifIpAddrAllocMethod=_IfIpAddrAllocMethod_Object((1,3,6,1,4,1,2076,27,1,5,1,1),_IfIpAddrAllocMethod_Type())
ifIpAddrAllocMethod.setMaxAccess(_B)
if mibBuilder.loadTexts:ifIpAddrAllocMethod.setStatus(_A)
class _IfIpAddr_Type(IpAddress):defaultHexValue=_T
_IfIpAddr_Type.__name__=_N
_IfIpAddr_Object=MibTableColumn
ifIpAddr=_IfIpAddr_Object((1,3,6,1,4,1,2076,27,1,5,1,2),_IfIpAddr_Type())
ifIpAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:ifIpAddr.setStatus(_A)
_IfIpSubnetMask_Type=IpAddress
_IfIpSubnetMask_Object=MibTableColumn
ifIpSubnetMask=_IfIpSubnetMask_Object((1,3,6,1,4,1,2076,27,1,5,1,3),_IfIpSubnetMask_Type())
ifIpSubnetMask.setMaxAccess(_B)
if mibBuilder.loadTexts:ifIpSubnetMask.setStatus(_A)
_IfIpBroadcastAddr_Type=IpAddress
_IfIpBroadcastAddr_Object=MibTableColumn
ifIpBroadcastAddr=_IfIpBroadcastAddr_Object((1,3,6,1,4,1,2076,27,1,5,1,4),_IfIpBroadcastAddr_Type())
ifIpBroadcastAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:ifIpBroadcastAddr.setStatus(_A)
class _IfIpForwardingEnable_Type(TruthValue):defaultValue=1
_IfIpForwardingEnable_Type.__name__=_J
_IfIpForwardingEnable_Object=MibTableColumn
ifIpForwardingEnable=_IfIpForwardingEnable_Object((1,3,6,1,4,1,2076,27,1,5,1,5),_IfIpForwardingEnable_Type())
ifIpForwardingEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:ifIpForwardingEnable.setStatus(_A)
class _IfIpAddrAllocProtocol_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('rarp',1),('dhcp',2)))
_IfIpAddrAllocProtocol_Type.__name__=_D
_IfIpAddrAllocProtocol_Object=MibTableColumn
ifIpAddrAllocProtocol=_IfIpAddrAllocProtocol_Object((1,3,6,1,4,1,2076,27,1,5,1,6),_IfIpAddrAllocProtocol_Type())
ifIpAddrAllocProtocol.setMaxAccess(_B)
if mibBuilder.loadTexts:ifIpAddrAllocProtocol.setStatus(_A)
_IfIpDestMacAddress_Type=MacAddress
_IfIpDestMacAddress_Object=MibTableColumn
ifIpDestMacAddress=_IfIpDestMacAddress_Object((1,3,6,1,4,1,2076,27,1,5,1,7),_IfIpDestMacAddress_Type())
ifIpDestMacAddress.setMaxAccess(_G)
if mibBuilder.loadTexts:ifIpDestMacAddress.setStatus(_A)
_IfIpUnnumAssocIPIf_Type=InterfaceIndex
_IfIpUnnumAssocIPIf_Object=MibTableColumn
ifIpUnnumAssocIPIf=_IfIpUnnumAssocIPIf_Object((1,3,6,1,4,1,2076,27,1,5,1,8),_IfIpUnnumAssocIPIf_Type())
ifIpUnnumAssocIPIf.setMaxAccess(_G)
if mibBuilder.loadTexts:ifIpUnnumAssocIPIf.setStatus(_A)
class _IfIpIntfStatsEnable_Type(TruthValue):defaultValue=2
_IfIpIntfStatsEnable_Type.__name__=_J
_IfIpIntfStatsEnable_Object=MibTableColumn
ifIpIntfStatsEnable=_IfIpIntfStatsEnable_Object((1,3,6,1,4,1,2076,27,1,5,1,9),_IfIpIntfStatsEnable_Type())
ifIpIntfStatsEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:ifIpIntfStatsEnable.setStatus(_A)
class _IfIpPortVlanId_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4094))
_IfIpPortVlanId_Type.__name__=_D
_IfIpPortVlanId_Object=MibTableColumn
ifIpPortVlanId=_IfIpPortVlanId_Object((1,3,6,1,4,1,2076,27,1,5,1,10),_IfIpPortVlanId_Type())
ifIpPortVlanId.setMaxAccess(_B)
if mibBuilder.loadTexts:ifIpPortVlanId.setStatus(_A)
_IfWanTable_Object=MibTable
ifWanTable=_IfWanTable_Object((1,3,6,1,4,1,2076,27,1,6))
if mibBuilder.loadTexts:ifWanTable.setStatus(_C)
_IfWanEntry_Object=MibTableRow
ifWanEntry=_IfWanEntry_Object((1,3,6,1,4,1,2076,27,1,6,1))
ifWanEntry.setIndexNames((0,_E,_H))
if mibBuilder.loadTexts:ifWanEntry.setStatus(_C)
class _IfWanInterfaceType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(23,38,92,108,134)));namedValues=NamedValues(*(('ppp',23),(_c,38),(_e,92),(_f,108),(_h,134)))
_IfWanInterfaceType_Type.__name__=_D
_IfWanInterfaceType_Object=MibTableColumn
ifWanInterfaceType=_IfWanInterfaceType_Object((1,3,6,1,4,1,2076,27,1,6,1,1),_IfWanInterfaceType_Type())
ifWanInterfaceType.setMaxAccess(_F)
if mibBuilder.loadTexts:ifWanInterfaceType.setStatus(_C)
class _IfWanConnectionType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_M,0),('permanent',1),('switched',2)))
_IfWanConnectionType_Type.__name__=_D
_IfWanConnectionType_Object=MibTableColumn
ifWanConnectionType=_IfWanConnectionType_Object((1,3,6,1,4,1,2076,27,1,6,1,2),_IfWanConnectionType_Type())
ifWanConnectionType.setMaxAccess(_B)
if mibBuilder.loadTexts:ifWanConnectionType.setStatus(_C)
class _IfWanVirtualPathId_Type(Integer32):defaultValue=0
_IfWanVirtualPathId_Type.__name__=_D
_IfWanVirtualPathId_Object=MibTableColumn
ifWanVirtualPathId=_IfWanVirtualPathId_Object((1,3,6,1,4,1,2076,27,1,6,1,3),_IfWanVirtualPathId_Type())
ifWanVirtualPathId.setMaxAccess(_B)
if mibBuilder.loadTexts:ifWanVirtualPathId.setStatus(_C)
class _IfWanVirtualCircuitId_Type(Integer32):defaultValue=0
_IfWanVirtualCircuitId_Type.__name__=_D
_IfWanVirtualCircuitId_Object=MibTableColumn
ifWanVirtualCircuitId=_IfWanVirtualCircuitId_Object((1,3,6,1,4,1,2076,27,1,6,1,4),_IfWanVirtualCircuitId_Type())
ifWanVirtualCircuitId.setMaxAccess(_B)
if mibBuilder.loadTexts:ifWanVirtualCircuitId.setStatus(_C)
class _IfWanPeerMediaAddress_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,40))
_IfWanPeerMediaAddress_Type.__name__=_K
_IfWanPeerMediaAddress_Object=MibTableColumn
ifWanPeerMediaAddress=_IfWanPeerMediaAddress_Object((1,3,6,1,4,1,2076,27,1,6,1,5),_IfWanPeerMediaAddress_Type())
ifWanPeerMediaAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:ifWanPeerMediaAddress.setStatus(_C)
_IfWanSustainedSpeed_Type=Integer32
_IfWanSustainedSpeed_Object=MibTableColumn
ifWanSustainedSpeed=_IfWanSustainedSpeed_Object((1,3,6,1,4,1,2076,27,1,6,1,6),_IfWanSustainedSpeed_Type())
ifWanSustainedSpeed.setMaxAccess(_B)
if mibBuilder.loadTexts:ifWanSustainedSpeed.setStatus(_C)
_IfWanPeakSpeed_Type=Integer32
_IfWanPeakSpeed_Object=MibTableColumn
ifWanPeakSpeed=_IfWanPeakSpeed_Object((1,3,6,1,4,1,2076,27,1,6,1,7),_IfWanPeakSpeed_Type())
ifWanPeakSpeed.setMaxAccess(_B)
if mibBuilder.loadTexts:ifWanPeakSpeed.setStatus(_C)
_IfWanMaxBurstSize_Type=Integer32
_IfWanMaxBurstSize_Object=MibTableColumn
ifWanMaxBurstSize=_IfWanMaxBurstSize_Object((1,3,6,1,4,1,2076,27,1,6,1,8),_IfWanMaxBurstSize_Type())
ifWanMaxBurstSize.setMaxAccess(_B)
if mibBuilder.loadTexts:ifWanMaxBurstSize.setStatus(_C)
class _IfWanIpQosProfileIndex_Type(Integer32):defaultValue=0
_IfWanIpQosProfileIndex_Type.__name__=_D
_IfWanIpQosProfileIndex_Object=MibTableColumn
ifWanIpQosProfileIndex=_IfWanIpQosProfileIndex_Object((1,3,6,1,4,1,2076,27,1,6,1,9),_IfWanIpQosProfileIndex_Type())
ifWanIpQosProfileIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ifWanIpQosProfileIndex.setStatus(_C)
class _IfWanIdleTimeout_Type(Integer32):defaultValue=0
_IfWanIdleTimeout_Type.__name__=_D
_IfWanIdleTimeout_Object=MibTableColumn
ifWanIdleTimeout=_IfWanIdleTimeout_Object((1,3,6,1,4,1,2076,27,1,6,1,10),_IfWanIdleTimeout_Type())
ifWanIdleTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:ifWanIdleTimeout.setStatus(_C)
class _IfWanPeerIpAddr_Type(IpAddress):defaultHexValue=_T
_IfWanPeerIpAddr_Type.__name__=_N
_IfWanPeerIpAddr_Object=MibTableColumn
ifWanPeerIpAddr=_IfWanPeerIpAddr_Object((1,3,6,1,4,1,2076,27,1,6,1,11),_IfWanPeerIpAddr_Type())
ifWanPeerIpAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:ifWanPeerIpAddr.setStatus(_C)
class _IfWanRtpHdrComprEnable_Type(TruthValue):defaultValue=2
_IfWanRtpHdrComprEnable_Type.__name__=_J
_IfWanRtpHdrComprEnable_Object=MibTableColumn
ifWanRtpHdrComprEnable=_IfWanRtpHdrComprEnable_Object((1,3,6,1,4,1,2076,27,1,6,1,12),_IfWanRtpHdrComprEnable_Type())
ifWanRtpHdrComprEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:ifWanRtpHdrComprEnable.setStatus(_C)
class _IfWanPersistence_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_M,1),('demand',2)))
_IfWanPersistence_Type.__name__=_D
_IfWanPersistence_Object=MibTableColumn
ifWanPersistence=_IfWanPersistence_Object((1,3,6,1,4,1,2076,27,1,6,1,13),_IfWanPersistence_Type())
ifWanPersistence.setMaxAccess(_B)
if mibBuilder.loadTexts:ifWanPersistence.setStatus(_C)
_IfAutoCktProfileTable_Object=MibTable
ifAutoCktProfileTable=_IfAutoCktProfileTable_Object((1,3,6,1,4,1,2076,27,1,7))
if mibBuilder.loadTexts:ifAutoCktProfileTable.setStatus(_C)
_IfAutoProfileEntry_Object=MibTableRow
ifAutoProfileEntry=_IfAutoProfileEntry_Object((1,3,6,1,4,1,2076,27,1,7,1))
ifAutoProfileEntry.setIndexNames((0,_E,_A3))
if mibBuilder.loadTexts:ifAutoProfileEntry.setStatus(_A)
_IfAutoProfileIfIndex_Type=InterfaceIndex
_IfAutoProfileIfIndex_Object=MibTableColumn
ifAutoProfileIfIndex=_IfAutoProfileIfIndex_Object((1,3,6,1,4,1,2076,27,1,7,1,1),_IfAutoProfileIfIndex_Type())
ifAutoProfileIfIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:ifAutoProfileIfIndex.setStatus(_C)
class _IfAutoProfileIfType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(5,32,49,114)));namedValues=NamedValues(*((_Z,5),(_b,32),('aal5',49),(_g,114)))
_IfAutoProfileIfType_Type.__name__=_D
_IfAutoProfileIfType_Object=MibTableColumn
ifAutoProfileIfType=_IfAutoProfileIfType_Object((1,3,6,1,4,1,2076,27,1,7,1,2),_IfAutoProfileIfType_Type())
ifAutoProfileIfType.setMaxAccess(_F)
if mibBuilder.loadTexts:ifAutoProfileIfType.setStatus(_C)
class _IfAutoProfileIpAddrAllocMethod_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_M,1),(_A2,2),('localAddressPool',3)))
_IfAutoProfileIpAddrAllocMethod_Type.__name__=_D
_IfAutoProfileIpAddrAllocMethod_Object=MibTableColumn
ifAutoProfileIpAddrAllocMethod=_IfAutoProfileIpAddrAllocMethod_Object((1,3,6,1,4,1,2076,27,1,7,1,3),_IfAutoProfileIpAddrAllocMethod_Type())
ifAutoProfileIpAddrAllocMethod.setMaxAccess(_G)
if mibBuilder.loadTexts:ifAutoProfileIpAddrAllocMethod.setStatus(_C)
_IfAutoProfileDefIpSubnetMask_Type=IpAddress
_IfAutoProfileDefIpSubnetMask_Object=MibTableColumn
ifAutoProfileDefIpSubnetMask=_IfAutoProfileDefIpSubnetMask_Object((1,3,6,1,4,1,2076,27,1,7,1,4),_IfAutoProfileDefIpSubnetMask_Type())
ifAutoProfileDefIpSubnetMask.setMaxAccess(_G)
if mibBuilder.loadTexts:ifAutoProfileDefIpSubnetMask.setStatus(_C)
_IfAutoProfileDefIpBroadcastAddr_Type=IpAddress
_IfAutoProfileDefIpBroadcastAddr_Object=MibTableColumn
ifAutoProfileDefIpBroadcastAddr=_IfAutoProfileDefIpBroadcastAddr_Object((1,3,6,1,4,1,2076,27,1,7,1,5),_IfAutoProfileDefIpBroadcastAddr_Type())
ifAutoProfileDefIpBroadcastAddr.setMaxAccess(_G)
if mibBuilder.loadTexts:ifAutoProfileDefIpBroadcastAddr.setStatus(_C)
_IfAutoProfileIdleTimeout_Type=Integer32
_IfAutoProfileIdleTimeout_Object=MibTableColumn
ifAutoProfileIdleTimeout=_IfAutoProfileIdleTimeout_Object((1,3,6,1,4,1,2076,27,1,7,1,6),_IfAutoProfileIdleTimeout_Type())
ifAutoProfileIdleTimeout.setMaxAccess(_G)
if mibBuilder.loadTexts:ifAutoProfileIdleTimeout.setStatus(_C)
class _IfAutoProfileEncapType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_M,1),('nlpid',2),(_l,3),(_m,4),(_n,5),(_o,6),(_p,7)))
_IfAutoProfileEncapType_Type.__name__=_D
_IfAutoProfileEncapType_Object=MibTableColumn
ifAutoProfileEncapType=_IfAutoProfileEncapType_Object((1,3,6,1,4,1,2076,27,1,7,1,7),_IfAutoProfileEncapType_Type())
ifAutoProfileEncapType.setMaxAccess(_G)
if mibBuilder.loadTexts:ifAutoProfileEncapType.setStatus(_C)
class _IfAutoProfileIpQosProfileIndex_Type(Integer32):defaultValue=0
_IfAutoProfileIpQosProfileIndex_Type.__name__=_D
_IfAutoProfileIpQosProfileIndex_Object=MibTableColumn
ifAutoProfileIpQosProfileIndex=_IfAutoProfileIpQosProfileIndex_Object((1,3,6,1,4,1,2076,27,1,7,1,8),_IfAutoProfileIpQosProfileIndex_Type())
ifAutoProfileIpQosProfileIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:ifAutoProfileIpQosProfileIndex.setStatus(_C)
_IfAutoProfileRowStatus_Type=RowStatus
_IfAutoProfileRowStatus_Object=MibTableColumn
ifAutoProfileRowStatus=_IfAutoProfileRowStatus_Object((1,3,6,1,4,1,2076,27,1,7,1,9),_IfAutoProfileRowStatus_Type())
ifAutoProfileRowStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:ifAutoProfileRowStatus.setStatus(_C)
_IfIvrTable_Object=MibTable
ifIvrTable=_IfIvrTable_Object((1,3,6,1,4,1,2076,27,1,8))
if mibBuilder.loadTexts:ifIvrTable.setStatus(_A)
_IfIvrEntry_Object=MibTableRow
ifIvrEntry=_IfIvrEntry_Object((1,3,6,1,4,1,2076,27,1,8,1))
ifIvrEntry.setIndexNames((0,_E,_H))
if mibBuilder.loadTexts:ifIvrEntry.setStatus(_A)
_IfIvrBridgedIface_Type=TruthValue
_IfIvrBridgedIface_Object=MibTableColumn
ifIvrBridgedIface=_IfIvrBridgedIface_Object((1,3,6,1,4,1,2076,27,1,8,1,1),_IfIvrBridgedIface_Type())
ifIvrBridgedIface.setMaxAccess(_B)
if mibBuilder.loadTexts:ifIvrBridgedIface.setStatus(_A)
class _IfSetMgmtVlanList_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,512))
_IfSetMgmtVlanList_Type.__name__=_K
_IfSetMgmtVlanList_Object=MibScalar
ifSetMgmtVlanList=_IfSetMgmtVlanList_Object((1,3,6,1,4,1,2076,27,1,9),_IfSetMgmtVlanList_Type())
ifSetMgmtVlanList.setMaxAccess(_B)
if mibBuilder.loadTexts:ifSetMgmtVlanList.setStatus(_A)
class _IfResetMgmtVlanList_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,512))
_IfResetMgmtVlanList_Type.__name__=_K
_IfResetMgmtVlanList_Object=MibScalar
ifResetMgmtVlanList=_IfResetMgmtVlanList_Object((1,3,6,1,4,1,2076,27,1,10),_IfResetMgmtVlanList_Type())
ifResetMgmtVlanList.setMaxAccess(_B)
if mibBuilder.loadTexts:ifResetMgmtVlanList.setStatus(_A)
_IfSecondaryIpAddressTable_Object=MibTable
ifSecondaryIpAddressTable=_IfSecondaryIpAddressTable_Object((1,3,6,1,4,1,2076,27,1,11))
if mibBuilder.loadTexts:ifSecondaryIpAddressTable.setStatus(_A)
_IfSecondaryIpAddressEntry_Object=MibTableRow
ifSecondaryIpAddressEntry=_IfSecondaryIpAddressEntry_Object((1,3,6,1,4,1,2076,27,1,11,1))
ifSecondaryIpAddressEntry.setIndexNames((0,_E,_H),(0,_E,_A4))
if mibBuilder.loadTexts:ifSecondaryIpAddressEntry.setStatus(_A)
_IfSecondaryIpAddress_Type=IpAddress
_IfSecondaryIpAddress_Object=MibTableColumn
ifSecondaryIpAddress=_IfSecondaryIpAddress_Object((1,3,6,1,4,1,2076,27,1,11,1,1),_IfSecondaryIpAddress_Type())
ifSecondaryIpAddress.setMaxAccess(_I)
if mibBuilder.loadTexts:ifSecondaryIpAddress.setStatus(_A)
_IfSecondaryIpSubnetMask_Type=IpAddress
_IfSecondaryIpSubnetMask_Object=MibTableColumn
ifSecondaryIpSubnetMask=_IfSecondaryIpSubnetMask_Object((1,3,6,1,4,1,2076,27,1,11,1,2),_IfSecondaryIpSubnetMask_Type())
ifSecondaryIpSubnetMask.setMaxAccess(_B)
if mibBuilder.loadTexts:ifSecondaryIpSubnetMask.setStatus(_A)
_IfSecondaryIpBroadcastAddr_Type=IpAddress
_IfSecondaryIpBroadcastAddr_Object=MibTableColumn
ifSecondaryIpBroadcastAddr=_IfSecondaryIpBroadcastAddr_Object((1,3,6,1,4,1,2076,27,1,11,1,3),_IfSecondaryIpBroadcastAddr_Type())
ifSecondaryIpBroadcastAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:ifSecondaryIpBroadcastAddr.setStatus(_A)
_IfSecondaryIpRowStatus_Type=RowStatus
_IfSecondaryIpRowStatus_Object=MibTableColumn
ifSecondaryIpRowStatus=_IfSecondaryIpRowStatus_Object((1,3,6,1,4,1,2076,27,1,11,1,4),_IfSecondaryIpRowStatus_Type())
ifSecondaryIpRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:ifSecondaryIpRowStatus.setStatus(_A)
_IfMainExtTable_Object=MibTable
ifMainExtTable=_IfMainExtTable_Object((1,3,6,1,4,1,2076,27,1,12))
if mibBuilder.loadTexts:ifMainExtTable.setStatus(_A)
_IfMainExtEntry_Object=MibTableRow
ifMainExtEntry=_IfMainExtEntry_Object((1,3,6,1,4,1,2076,27,1,12,1))
if mibBuilder.loadTexts:ifMainExtEntry.setStatus(_A)
_IfMainExtMacAddress_Type=MacAddress
_IfMainExtMacAddress_Object=MibTableColumn
ifMainExtMacAddress=_IfMainExtMacAddress_Object((1,3,6,1,4,1,2076,27,1,12,1,8),_IfMainExtMacAddress_Type())
ifMainExtMacAddress.setMaxAccess(_G)
if mibBuilder.loadTexts:ifMainExtMacAddress.setStatus(_A)
class _IfMainExtSysSpecificPortID_Type(Unsigned32):defaultValue=0
_IfMainExtSysSpecificPortID_Type.__name__=_L
_IfMainExtSysSpecificPortID_Object=MibTableColumn
ifMainExtSysSpecificPortID=_IfMainExtSysSpecificPortID_Object((1,3,6,1,4,1,2076,27,1,12,1,9),_IfMainExtSysSpecificPortID_Type())
ifMainExtSysSpecificPortID.setMaxAccess(_B)
if mibBuilder.loadTexts:ifMainExtSysSpecificPortID.setStatus(_A)
class _IfMainExtInterfaceType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('frontpanelport',1),('backplaneport',2)))
_IfMainExtInterfaceType_Type.__name__=_D
_IfMainExtInterfaceType_Object=MibTableColumn
ifMainExtInterfaceType=_IfMainExtInterfaceType_Object((1,3,6,1,4,1,2076,27,1,12,1,10),_IfMainExtInterfaceType_Type())
ifMainExtInterfaceType.setMaxAccess(_B)
if mibBuilder.loadTexts:ifMainExtInterfaceType.setStatus(_A)
class _IfMainExtPortSecState_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('untrusted',0),('trusted',1)))
_IfMainExtPortSecState_Type.__name__=_D
_IfMainExtPortSecState_Object=MibTableColumn
ifMainExtPortSecState=_IfMainExtPortSecState_Object((1,3,6,1,4,1,2076,27,1,12,1,11),_IfMainExtPortSecState_Type())
ifMainExtPortSecState.setMaxAccess(_B)
if mibBuilder.loadTexts:ifMainExtPortSecState.setStatus(_A)
_IfMainExtInPkts_Type=Counter32
_IfMainExtInPkts_Object=MibTableColumn
ifMainExtInPkts=_IfMainExtInPkts_Object((1,3,6,1,4,1,2076,27,1,12,1,12),_IfMainExtInPkts_Type())
ifMainExtInPkts.setMaxAccess(_F)
if mibBuilder.loadTexts:ifMainExtInPkts.setStatus(_A)
class _IfMainExtLinkUpEnabledStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_P,1),(_Q,2)))
_IfMainExtLinkUpEnabledStatus_Type.__name__=_D
_IfMainExtLinkUpEnabledStatus_Object=MibTableColumn
ifMainExtLinkUpEnabledStatus=_IfMainExtLinkUpEnabledStatus_Object((1,3,6,1,4,1,2076,27,1,12,1,13),_IfMainExtLinkUpEnabledStatus_Type())
ifMainExtLinkUpEnabledStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:ifMainExtLinkUpEnabledStatus.setStatus(_A)
class _IfMainExtLinkUpDelayTimer_Type(Unsigned32):defaultValue=2
_IfMainExtLinkUpDelayTimer_Type.__name__=_L
_IfMainExtLinkUpDelayTimer_Object=MibTableColumn
ifMainExtLinkUpDelayTimer=_IfMainExtLinkUpDelayTimer_Object((1,3,6,1,4,1,2076,27,1,12,1,14),_IfMainExtLinkUpDelayTimer_Type())
ifMainExtLinkUpDelayTimer.setMaxAccess(_B)
if mibBuilder.loadTexts:ifMainExtLinkUpDelayTimer.setStatus(_A)
if mibBuilder.loadTexts:ifMainExtLinkUpDelayTimer.setUnits('seconds')
_IfMainExtLinkUpRemainingTime_Type=Unsigned32
_IfMainExtLinkUpRemainingTime_Object=MibTableColumn
ifMainExtLinkUpRemainingTime=_IfMainExtLinkUpRemainingTime_Object((1,3,6,1,4,1,2076,27,1,12,1,15),_IfMainExtLinkUpRemainingTime_Type())
ifMainExtLinkUpRemainingTime.setMaxAccess(_F)
if mibBuilder.loadTexts:ifMainExtLinkUpRemainingTime.setStatus(_A)
_IfCustTLVTable_Object=MibTable
ifCustTLVTable=_IfCustTLVTable_Object((1,3,6,1,4,1,2076,27,1,13))
if mibBuilder.loadTexts:ifCustTLVTable.setStatus(_A)
_IfCustTLVEntry_Object=MibTableRow
ifCustTLVEntry=_IfCustTLVEntry_Object((1,3,6,1,4,1,2076,27,1,13,1))
ifCustTLVEntry.setIndexNames((0,_E,_H),(0,_E,_A5))
if mibBuilder.loadTexts:ifCustTLVEntry.setStatus(_A)
_IfCustTLVType_Type=Unsigned32
_IfCustTLVType_Object=MibTableColumn
ifCustTLVType=_IfCustTLVType_Object((1,3,6,1,4,1,2076,27,1,13,1,1),_IfCustTLVType_Type())
ifCustTLVType.setMaxAccess(_I)
if mibBuilder.loadTexts:ifCustTLVType.setStatus(_A)
_IfCustTLVLength_Type=Unsigned32
_IfCustTLVLength_Object=MibTableColumn
ifCustTLVLength=_IfCustTLVLength_Object((1,3,6,1,4,1,2076,27,1,13,1,2),_IfCustTLVLength_Type())
ifCustTLVLength.setMaxAccess(_G)
if mibBuilder.loadTexts:ifCustTLVLength.setStatus(_A)
_IfCustTLVValue_Type=DisplayString
_IfCustTLVValue_Object=MibTableColumn
ifCustTLVValue=_IfCustTLVValue_Object((1,3,6,1,4,1,2076,27,1,13,1,3),_IfCustTLVValue_Type())
ifCustTLVValue.setMaxAccess(_G)
if mibBuilder.loadTexts:ifCustTLVValue.setStatus(_A)
_IfCustTLVRowStatus_Type=RowStatus
_IfCustTLVRowStatus_Object=MibTableColumn
ifCustTLVRowStatus=_IfCustTLVRowStatus_Object((1,3,6,1,4,1,2076,27,1,13,1,4),_IfCustTLVRowStatus_Type())
ifCustTLVRowStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:ifCustTLVRowStatus.setStatus(_A)
_IfCustOpaqueAttrTable_Object=MibTable
ifCustOpaqueAttrTable=_IfCustOpaqueAttrTable_Object((1,3,6,1,4,1,2076,27,1,14))
if mibBuilder.loadTexts:ifCustOpaqueAttrTable.setStatus(_A)
_IfCustOpaqueAttrEntry_Object=MibTableRow
ifCustOpaqueAttrEntry=_IfCustOpaqueAttrEntry_Object((1,3,6,1,4,1,2076,27,1,14,1))
ifCustOpaqueAttrEntry.setIndexNames((0,_E,_H),(0,_E,_A6))
if mibBuilder.loadTexts:ifCustOpaqueAttrEntry.setStatus(_A)
class _IfCustOpaqueAttributeID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('opaqueAttr1',1),('opaqueAttr2',2),('opaqueAttr3',3),('opaqueAttr4',4)))
_IfCustOpaqueAttributeID_Type.__name__=_D
_IfCustOpaqueAttributeID_Object=MibTableColumn
ifCustOpaqueAttributeID=_IfCustOpaqueAttributeID_Object((1,3,6,1,4,1,2076,27,1,14,1,1),_IfCustOpaqueAttributeID_Type())
ifCustOpaqueAttributeID.setMaxAccess(_I)
if mibBuilder.loadTexts:ifCustOpaqueAttributeID.setStatus(_A)
class _IfCustOpaqueAttribute_Type(Unsigned32):defaultValue=0
_IfCustOpaqueAttribute_Type.__name__=_L
_IfCustOpaqueAttribute_Object=MibTableColumn
ifCustOpaqueAttribute=_IfCustOpaqueAttribute_Object((1,3,6,1,4,1,2076,27,1,14,1,2),_IfCustOpaqueAttribute_Type())
ifCustOpaqueAttribute.setMaxAccess(_G)
if mibBuilder.loadTexts:ifCustOpaqueAttribute.setStatus(_A)
_IfCustOpaqueRowStatus_Type=RowStatus
_IfCustOpaqueRowStatus_Object=MibTableColumn
ifCustOpaqueRowStatus=_IfCustOpaqueRowStatus_Object((1,3,6,1,4,1,2076,27,1,14,1,3),_IfCustOpaqueRowStatus_Type())
ifCustOpaqueRowStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:ifCustOpaqueRowStatus.setStatus(_A)
_IfBridgeILanIfTable_Object=MibTable
ifBridgeILanIfTable=_IfBridgeILanIfTable_Object((1,3,6,1,4,1,2076,27,1,15))
if mibBuilder.loadTexts:ifBridgeILanIfTable.setStatus(_A)
_IfBridgeILanIfEntry_Object=MibTableRow
ifBridgeILanIfEntry=_IfBridgeILanIfEntry_Object((1,3,6,1,4,1,2076,27,1,15,1))
ifBridgeILanIfEntry.setIndexNames((0,_U,_W))
if mibBuilder.loadTexts:ifBridgeILanIfEntry.setStatus(_A)
class _IfBridgeILanIfStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('active',1),('outOfService',2)))
_IfBridgeILanIfStatus_Type.__name__=_D
_IfBridgeILanIfStatus_Object=MibTableColumn
ifBridgeILanIfStatus=_IfBridgeILanIfStatus_Object((1,3,6,1,4,1,2076,27,1,15,1,1),_IfBridgeILanIfStatus_Type())
ifBridgeILanIfStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:ifBridgeILanIfStatus.setStatus(_A)
_IfTypeProtoDenyTable_Object=MibTable
ifTypeProtoDenyTable=_IfTypeProtoDenyTable_Object((1,3,6,1,4,1,2076,27,1,16))
if mibBuilder.loadTexts:ifTypeProtoDenyTable.setStatus(_A)
_IfTypeProtoDenyEntry_Object=MibTableRow
ifTypeProtoDenyEntry=_IfTypeProtoDenyEntry_Object((1,3,6,1,4,1,2076,27,1,16,1))
ifTypeProtoDenyEntry.setIndexNames((0,_E,_A7),(0,_E,_A8),(0,_E,_A9),(0,_E,_AA))
if mibBuilder.loadTexts:ifTypeProtoDenyEntry.setStatus(_A)
class _IfTypeProtoDenyContextId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_IfTypeProtoDenyContextId_Type.__name__=_L
_IfTypeProtoDenyContextId_Object=MibTableColumn
ifTypeProtoDenyContextId=_IfTypeProtoDenyContextId_Object((1,3,6,1,4,1,2076,27,1,16,1,1),_IfTypeProtoDenyContextId_Type())
ifTypeProtoDenyContextId.setMaxAccess(_I)
if mibBuilder.loadTexts:ifTypeProtoDenyContextId.setStatus(_A)
class _IfTypeProtoDenyMainType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(6,53,161,209,248)));namedValues=NamedValues(*((_a,6),(_d,53),(_i,161),(_j,209),('pip',248)))
_IfTypeProtoDenyMainType_Type.__name__=_D
_IfTypeProtoDenyMainType_Object=MibTableColumn
ifTypeProtoDenyMainType=_IfTypeProtoDenyMainType_Object((1,3,6,1,4,1,2076,27,1,16,1,2),_IfTypeProtoDenyMainType_Type())
ifTypeProtoDenyMainType.setMaxAccess(_I)
if mibBuilder.loadTexts:ifTypeProtoDenyMainType.setStatus(_A)
class _IfTypeProtoDenyBrgPortType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12)));namedValues=NamedValues(*((_q,1),(_r,2),(_s,3),(_t,4),(_u,5),(_v,6),(_w,7),(_x,8),(_y,9),(_z,10),(_A0,11),(_A1,12)))
_IfTypeProtoDenyBrgPortType_Type.__name__=_D
_IfTypeProtoDenyBrgPortType_Object=MibTableColumn
ifTypeProtoDenyBrgPortType=_IfTypeProtoDenyBrgPortType_Object((1,3,6,1,4,1,2076,27,1,16,1,3),_IfTypeProtoDenyBrgPortType_Type())
ifTypeProtoDenyBrgPortType.setMaxAccess(_I)
if mibBuilder.loadTexts:ifTypeProtoDenyBrgPortType.setStatus(_A)
class _IfTypeProtoDenyProtocol_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13)));namedValues=NamedValues(*(('pnac',1),('la',2),('xstp',3),('vlan',4),('garp',5),('mrp',6),('pbb',7),('ecfm',8),('elmi',9),('snoop',10),('lldp',11),('bridge',12),('qos',13)))
_IfTypeProtoDenyProtocol_Type.__name__=_D
_IfTypeProtoDenyProtocol_Object=MibTableColumn
ifTypeProtoDenyProtocol=_IfTypeProtoDenyProtocol_Object((1,3,6,1,4,1,2076,27,1,16,1,4),_IfTypeProtoDenyProtocol_Type())
ifTypeProtoDenyProtocol.setMaxAccess(_I)
if mibBuilder.loadTexts:ifTypeProtoDenyProtocol.setStatus(_A)
_IfTypeProtoDenyRowStatus_Type=RowStatus
_IfTypeProtoDenyRowStatus_Object=MibTableColumn
ifTypeProtoDenyRowStatus=_IfTypeProtoDenyRowStatus_Object((1,3,6,1,4,1,2076,27,1,16,1,5),_IfTypeProtoDenyRowStatus_Type())
ifTypeProtoDenyRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:ifTypeProtoDenyRowStatus.setStatus(_A)
class _IfmDebug_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_IfmDebug_Type.__name__=_L
_IfmDebug_Object=MibScalar
ifmDebug=_IfmDebug_Object((1,3,6,1,4,1,2076,27,1,17),_IfmDebug_Type())
ifmDebug.setMaxAccess(_B)
if mibBuilder.loadTexts:ifmDebug.setStatus(_A)
_IfIvrMappingTable_Object=MibTable
ifIvrMappingTable=_IfIvrMappingTable_Object((1,3,6,1,4,1,2076,27,1,18))
if mibBuilder.loadTexts:ifIvrMappingTable.setStatus(_A)
_IfIvrMappingEntry_Object=MibTableRow
ifIvrMappingEntry=_IfIvrMappingEntry_Object((1,3,6,1,4,1,2076,27,1,18,1))
ifIvrMappingEntry.setIndexNames((0,_E,_H),(0,_E,_AB))
if mibBuilder.loadTexts:ifIvrMappingEntry.setStatus(_A)
_IfIvrAssociatedVlan_Type=VlanId
_IfIvrAssociatedVlan_Object=MibTableColumn
ifIvrAssociatedVlan=_IfIvrAssociatedVlan_Object((1,3,6,1,4,1,2076,27,1,18,1,1),_IfIvrAssociatedVlan_Type())
ifIvrAssociatedVlan.setMaxAccess(_I)
if mibBuilder.loadTexts:ifIvrAssociatedVlan.setStatus(_A)
_IfIvrMappingRowStatus_Type=RowStatus
_IfIvrMappingRowStatus_Object=MibTableColumn
ifIvrMappingRowStatus=_IfIvrMappingRowStatus_Object((1,3,6,1,4,1,2076,27,1,18,1,2),_IfIvrMappingRowStatus_Type())
ifIvrMappingRowStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:ifIvrMappingRowStatus.setStatus(_A)
_IfHCErrorTable_Object=MibTable
ifHCErrorTable=_IfHCErrorTable_Object((1,3,6,1,4,1,2076,27,1,19))
if mibBuilder.loadTexts:ifHCErrorTable.setStatus(_A)
_IfHCErrorEntry_Object=MibTableRow
ifHCErrorEntry=_IfHCErrorEntry_Object((1,3,6,1,4,1,2076,27,1,19,1))
if mibBuilder.loadTexts:ifHCErrorEntry.setStatus(_A)
_IfHCInDiscards_Type=Counter64
_IfHCInDiscards_Object=MibTableColumn
ifHCInDiscards=_IfHCInDiscards_Object((1,3,6,1,4,1,2076,27,1,19,1,1),_IfHCInDiscards_Type())
ifHCInDiscards.setMaxAccess(_F)
if mibBuilder.loadTexts:ifHCInDiscards.setStatus(_A)
_IfHCInErrors_Type=Counter64
_IfHCInErrors_Object=MibTableColumn
ifHCInErrors=_IfHCInErrors_Object((1,3,6,1,4,1,2076,27,1,19,1,2),_IfHCInErrors_Type())
ifHCInErrors.setMaxAccess(_F)
if mibBuilder.loadTexts:ifHCInErrors.setStatus(_A)
_IfHCInUnknownProtos_Type=Counter64
_IfHCInUnknownProtos_Object=MibTableColumn
ifHCInUnknownProtos=_IfHCInUnknownProtos_Object((1,3,6,1,4,1,2076,27,1,19,1,3),_IfHCInUnknownProtos_Type())
ifHCInUnknownProtos.setMaxAccess(_F)
if mibBuilder.loadTexts:ifHCInUnknownProtos.setStatus(_A)
_IfHCOutDiscards_Type=Counter64
_IfHCOutDiscards_Object=MibTableColumn
ifHCOutDiscards=_IfHCOutDiscards_Object((1,3,6,1,4,1,2076,27,1,19,1,4),_IfHCOutDiscards_Type())
ifHCOutDiscards.setMaxAccess(_F)
if mibBuilder.loadTexts:ifHCOutDiscards.setStatus(_A)
_IfHCOutErrors_Type=Counter64
_IfHCOutErrors_Object=MibTableColumn
ifHCOutErrors=_IfHCOutErrors_Object((1,3,6,1,4,1,2076,27,1,19,1,5),_IfHCOutErrors_Type())
ifHCOutErrors.setMaxAccess(_F)
if mibBuilder.loadTexts:ifHCOutErrors.setStatus(_A)
class _IfSecurityBridging_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_P,1),(_Q,2)))
_IfSecurityBridging_Type.__name__=_D
_IfSecurityBridging_Object=MibScalar
ifSecurityBridging=_IfSecurityBridging_Object((1,3,6,1,4,1,2076,27,1,20),_IfSecurityBridging_Type())
ifSecurityBridging.setMaxAccess(_B)
if mibBuilder.loadTexts:ifSecurityBridging.setStatus(_A)
class _IfSetSecVlanList_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,512))
_IfSetSecVlanList_Type.__name__=_K
_IfSetSecVlanList_Object=MibScalar
ifSetSecVlanList=_IfSetSecVlanList_Object((1,3,6,1,4,1,2076,27,1,21),_IfSetSecVlanList_Type())
ifSetSecVlanList.setMaxAccess(_B)
if mibBuilder.loadTexts:ifSetSecVlanList.setStatus(_A)
class _IfResetSecVlanList_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,512))
_IfResetSecVlanList_Type.__name__=_K
_IfResetSecVlanList_Object=MibScalar
ifResetSecVlanList=_IfResetSecVlanList_Object((1,3,6,1,4,1,2076,27,1,22),_IfResetSecVlanList_Type())
ifResetSecVlanList.setMaxAccess(_B)
if mibBuilder.loadTexts:ifResetSecVlanList.setStatus(_A)
_IfSecIvrIfIndex_Type=Integer32
_IfSecIvrIfIndex_Object=MibScalar
ifSecIvrIfIndex=_IfSecIvrIfIndex_Object((1,3,6,1,4,1,2076,27,1,23),_IfSecIvrIfIndex_Type())
ifSecIvrIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ifSecIvrIfIndex.setStatus(_A)
_IfAvailableIndexTable_Object=MibTable
ifAvailableIndexTable=_IfAvailableIndexTable_Object((1,3,6,1,4,1,2076,27,1,24))
if mibBuilder.loadTexts:ifAvailableIndexTable.setStatus(_A)
_IfAvailableIndexEntry_Object=MibTableRow
ifAvailableIndexEntry=_IfAvailableIndexEntry_Object((1,3,6,1,4,1,2076,27,1,24,1))
ifAvailableIndexEntry.setIndexNames((0,_U,_X))
if mibBuilder.loadTexts:ifAvailableIndexEntry.setStatus(_A)
_IfAvailableFreeIndex_Type=InterfaceIndex
_IfAvailableFreeIndex_Object=MibTableColumn
ifAvailableFreeIndex=_IfAvailableFreeIndex_Object((1,3,6,1,4,1,2076,27,1,24,1,1),_IfAvailableFreeIndex_Type())
ifAvailableFreeIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:ifAvailableFreeIndex.setStatus(_A)
_IfACTable_Object=MibTable
ifACTable=_IfACTable_Object((1,3,6,1,4,1,2076,27,1,25))
if mibBuilder.loadTexts:ifACTable.setStatus(_A)
_IfACEntry_Object=MibTableRow
ifACEntry=_IfACEntry_Object((1,3,6,1,4,1,2076,27,1,25,1))
ifACEntry.setIndexNames((0,_E,_H))
if mibBuilder.loadTexts:ifACEntry.setStatus(_A)
_IfACPortIdentifier_Type=InterfaceIndex
_IfACPortIdentifier_Object=MibTableColumn
ifACPortIdentifier=_IfACPortIdentifier_Object((1,3,6,1,4,1,2076,27,1,25,1,1),_IfACPortIdentifier_Type())
ifACPortIdentifier.setMaxAccess(_B)
if mibBuilder.loadTexts:ifACPortIdentifier.setStatus(_A)
_IfACCustomerVlan_Type=VlanId
_IfACCustomerVlan_Object=MibTableColumn
ifACCustomerVlan=_IfACCustomerVlan_Object((1,3,6,1,4,1,2076,27,1,25,1,2),_IfACCustomerVlan_Type())
ifACCustomerVlan.setMaxAccess(_B)
if mibBuilder.loadTexts:ifACCustomerVlan.setStatus(_A)
class _IfUfdSystemControl_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('start',1),('shutdown',2)))
_IfUfdSystemControl_Type.__name__=_D
_IfUfdSystemControl_Object=MibScalar
ifUfdSystemControl=_IfUfdSystemControl_Object((1,3,6,1,4,1,2076,27,1,26),_IfUfdSystemControl_Type())
ifUfdSystemControl.setMaxAccess(_B)
if mibBuilder.loadTexts:ifUfdSystemControl.setStatus(_A)
class _IfUfdModuleStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_P,1),(_Q,2)))
_IfUfdModuleStatus_Type.__name__=_D
_IfUfdModuleStatus_Object=MibScalar
ifUfdModuleStatus=_IfUfdModuleStatus_Object((1,3,6,1,4,1,2076,27,1,27),_IfUfdModuleStatus_Type())
ifUfdModuleStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:ifUfdModuleStatus.setStatus(_A)
class _IfSplitHorizonSysControl_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('start',1),('shutdown',2)))
_IfSplitHorizonSysControl_Type.__name__=_D
_IfSplitHorizonSysControl_Object=MibScalar
ifSplitHorizonSysControl=_IfSplitHorizonSysControl_Object((1,3,6,1,4,1,2076,27,1,28),_IfSplitHorizonSysControl_Type())
ifSplitHorizonSysControl.setMaxAccess(_B)
if mibBuilder.loadTexts:ifSplitHorizonSysControl.setStatus(_A)
class _IfSplitHorizonModStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_P,1),(_Q,2)))
_IfSplitHorizonModStatus_Type.__name__=_D
_IfSplitHorizonModStatus_Object=MibScalar
ifSplitHorizonModStatus=_IfSplitHorizonModStatus_Object((1,3,6,1,4,1,2076,27,1,29),_IfSplitHorizonModStatus_Type())
ifSplitHorizonModStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:ifSplitHorizonModStatus.setStatus(_A)
_IfUfdGroupTable_Object=MibTable
ifUfdGroupTable=_IfUfdGroupTable_Object((1,3,6,1,4,1,2076,27,1,30))
if mibBuilder.loadTexts:ifUfdGroupTable.setStatus(_A)
_IfUfdGroupEntry_Object=MibTableRow
ifUfdGroupEntry=_IfUfdGroupEntry_Object((1,3,6,1,4,1,2076,27,1,30,1))
ifUfdGroupEntry.setIndexNames((0,_E,_AC))
if mibBuilder.loadTexts:ifUfdGroupEntry.setStatus(_A)
class _IfUfdGroupId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_IfUfdGroupId_Type.__name__=_D
_IfUfdGroupId_Object=MibTableColumn
ifUfdGroupId=_IfUfdGroupId_Object((1,3,6,1,4,1,2076,27,1,30,1,1),_IfUfdGroupId_Type())
ifUfdGroupId.setMaxAccess(_I)
if mibBuilder.loadTexts:ifUfdGroupId.setStatus(_A)
class _IfUfdGroupName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_IfUfdGroupName_Type.__name__=_O
_IfUfdGroupName_Object=MibTableColumn
ifUfdGroupName=_IfUfdGroupName_Object((1,3,6,1,4,1,2076,27,1,30,1,2),_IfUfdGroupName_Type())
ifUfdGroupName.setMaxAccess(_B)
if mibBuilder.loadTexts:ifUfdGroupName.setStatus(_A)
class _IfUfdGroupStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_R,1),(_S,2)))
_IfUfdGroupStatus_Type.__name__=_D
_IfUfdGroupStatus_Object=MibTableColumn
ifUfdGroupStatus=_IfUfdGroupStatus_Object((1,3,6,1,4,1,2076,27,1,30,1,3),_IfUfdGroupStatus_Type())
ifUfdGroupStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:ifUfdGroupStatus.setStatus(_A)
_IfUfdGroupUplinkPorts_Type=PortList
_IfUfdGroupUplinkPorts_Object=MibTableColumn
ifUfdGroupUplinkPorts=_IfUfdGroupUplinkPorts_Object((1,3,6,1,4,1,2076,27,1,30,1,4),_IfUfdGroupUplinkPorts_Type())
ifUfdGroupUplinkPorts.setMaxAccess(_B)
if mibBuilder.loadTexts:ifUfdGroupUplinkPorts.setStatus(_A)
_IfUfdGroupDownlinkPorts_Type=PortList
_IfUfdGroupDownlinkPorts_Object=MibTableColumn
ifUfdGroupDownlinkPorts=_IfUfdGroupDownlinkPorts_Object((1,3,6,1,4,1,2076,27,1,30,1,5),_IfUfdGroupDownlinkPorts_Type())
ifUfdGroupDownlinkPorts.setMaxAccess(_B)
if mibBuilder.loadTexts:ifUfdGroupDownlinkPorts.setStatus(_A)
_IfUfdGroupDesigUplinkPort_Type=InterfaceIndex
_IfUfdGroupDesigUplinkPort_Object=MibTableColumn
ifUfdGroupDesigUplinkPort=_IfUfdGroupDesigUplinkPort_Object((1,3,6,1,4,1,2076,27,1,30,1,6),_IfUfdGroupDesigUplinkPort_Type())
ifUfdGroupDesigUplinkPort.setMaxAccess(_B)
if mibBuilder.loadTexts:ifUfdGroupDesigUplinkPort.setStatus(_C)
class _IfUfdGroupUplinkCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,48))
_IfUfdGroupUplinkCount_Type.__name__=_D
_IfUfdGroupUplinkCount_Object=MibTableColumn
ifUfdGroupUplinkCount=_IfUfdGroupUplinkCount_Object((1,3,6,1,4,1,2076,27,1,30,1,7),_IfUfdGroupUplinkCount_Type())
ifUfdGroupUplinkCount.setMaxAccess(_F)
if mibBuilder.loadTexts:ifUfdGroupUplinkCount.setStatus(_A)
class _IfUfdGroupDownlinkCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,48))
_IfUfdGroupDownlinkCount_Type.__name__=_D
_IfUfdGroupDownlinkCount_Object=MibTableColumn
ifUfdGroupDownlinkCount=_IfUfdGroupDownlinkCount_Object((1,3,6,1,4,1,2076,27,1,30,1,8),_IfUfdGroupDownlinkCount_Type())
ifUfdGroupDownlinkCount.setMaxAccess(_F)
if mibBuilder.loadTexts:ifUfdGroupDownlinkCount.setStatus(_A)
_IfUfdGroupRowStatus_Type=RowStatus
_IfUfdGroupRowStatus_Object=MibTableColumn
ifUfdGroupRowStatus=_IfUfdGroupRowStatus_Object((1,3,6,1,4,1,2076,27,1,30,1,9),_IfUfdGroupRowStatus_Type())
ifUfdGroupRowStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:ifUfdGroupRowStatus.setStatus(_A)
class _IfLinkUpEnabledStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_P,1),(_Q,2)))
_IfLinkUpEnabledStatus_Type.__name__=_D
_IfLinkUpEnabledStatus_Object=MibScalar
ifLinkUpEnabledStatus=_IfLinkUpEnabledStatus_Object((1,3,6,1,4,1,2076,27,1,31),_IfLinkUpEnabledStatus_Type())
ifLinkUpEnabledStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:ifLinkUpEnabledStatus.setStatus(_A)
class _IfOOBNode0SecondaryIpAddress_Type(IpAddress):defaultHexValue=_T
_IfOOBNode0SecondaryIpAddress_Type.__name__=_N
_IfOOBNode0SecondaryIpAddress_Object=MibScalar
ifOOBNode0SecondaryIpAddress=_IfOOBNode0SecondaryIpAddress_Object((1,3,6,1,4,1,2076,27,1,32),_IfOOBNode0SecondaryIpAddress_Type())
ifOOBNode0SecondaryIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:ifOOBNode0SecondaryIpAddress.setStatus(_A)
_IfOOBNode0SecondaryIpMask_Type=IpAddress
_IfOOBNode0SecondaryIpMask_Object=MibScalar
ifOOBNode0SecondaryIpMask=_IfOOBNode0SecondaryIpMask_Object((1,3,6,1,4,1,2076,27,1,33),_IfOOBNode0SecondaryIpMask_Type())
ifOOBNode0SecondaryIpMask.setMaxAccess(_B)
if mibBuilder.loadTexts:ifOOBNode0SecondaryIpMask.setStatus(_A)
class _IfOOBNode1SecondaryIpAddress_Type(IpAddress):defaultHexValue=_T
_IfOOBNode1SecondaryIpAddress_Type.__name__=_N
_IfOOBNode1SecondaryIpAddress_Object=MibScalar
ifOOBNode1SecondaryIpAddress=_IfOOBNode1SecondaryIpAddress_Object((1,3,6,1,4,1,2076,27,1,34),_IfOOBNode1SecondaryIpAddress_Type())
ifOOBNode1SecondaryIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:ifOOBNode1SecondaryIpAddress.setStatus(_A)
_IfOOBNode1SecondaryIpMask_Type=IpAddress
_IfOOBNode1SecondaryIpMask_Object=MibScalar
ifOOBNode1SecondaryIpMask=_IfOOBNode1SecondaryIpMask_Object((1,3,6,1,4,1,2076,27,1,35),_IfOOBNode1SecondaryIpMask_Type())
ifOOBNode1SecondaryIpMask.setMaxAccess(_B)
if mibBuilder.loadTexts:ifOOBNode1SecondaryIpMask.setStatus(_A)
_Ff_ObjectIdentity=ObjectIdentity
ff=_Ff_ObjectIdentity((1,3,6,1,4,1,2076,27,2))
class _FfFastForwardingEnable_Type(TruthValue):defaultValue=2
_FfFastForwardingEnable_Type.__name__=_J
_FfFastForwardingEnable_Object=MibScalar
ffFastForwardingEnable=_FfFastForwardingEnable_Object((1,3,6,1,4,1,2076,27,2,1),_FfFastForwardingEnable_Type())
ffFastForwardingEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:ffFastForwardingEnable.setStatus(_C)
class _FfCacheSize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,65535))
_FfCacheSize_Type.__name__=_D
_FfCacheSize_Object=MibScalar
ffCacheSize=_FfCacheSize_Object((1,3,6,1,4,1,2076,27,2,2),_FfCacheSize_Type())
ffCacheSize.setMaxAccess(_B)
if mibBuilder.loadTexts:ffCacheSize.setStatus(_C)
class _FfIpChecksumValidationEnable_Type(TruthValue):defaultValue=1
_FfIpChecksumValidationEnable_Type.__name__=_J
_FfIpChecksumValidationEnable_Object=MibScalar
ffIpChecksumValidationEnable=_FfIpChecksumValidationEnable_Object((1,3,6,1,4,1,2076,27,2,3),_FfIpChecksumValidationEnable_Type())
ffIpChecksumValidationEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:ffIpChecksumValidationEnable.setStatus(_C)
_FfCachePurgeCount_Type=Counter32
_FfCachePurgeCount_Object=MibScalar
ffCachePurgeCount=_FfCachePurgeCount_Object((1,3,6,1,4,1,2076,27,2,4),_FfCachePurgeCount_Type())
ffCachePurgeCount.setMaxAccess(_F)
if mibBuilder.loadTexts:ffCachePurgeCount.setStatus(_C)
_FfCacheLastPurgeTime_Type=TimeStamp
_FfCacheLastPurgeTime_Object=MibScalar
ffCacheLastPurgeTime=_FfCacheLastPurgeTime_Object((1,3,6,1,4,1,2076,27,2,5),_FfCacheLastPurgeTime_Type())
ffCacheLastPurgeTime.setMaxAccess(_F)
if mibBuilder.loadTexts:ffCacheLastPurgeTime.setStatus(_C)
class _FfStaticEntryInvalidTrapEnable_Type(TruthValue):defaultValue=1
_FfStaticEntryInvalidTrapEnable_Type.__name__=_J
_FfStaticEntryInvalidTrapEnable_Object=MibScalar
ffStaticEntryInvalidTrapEnable=_FfStaticEntryInvalidTrapEnable_Object((1,3,6,1,4,1,2076,27,2,6),_FfStaticEntryInvalidTrapEnable_Type())
ffStaticEntryInvalidTrapEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:ffStaticEntryInvalidTrapEnable.setStatus(_C)
_FfCurrentStaticEntryInvalidCount_Type=Counter32
_FfCurrentStaticEntryInvalidCount_Object=MibScalar
ffCurrentStaticEntryInvalidCount=_FfCurrentStaticEntryInvalidCount_Object((1,3,6,1,4,1,2076,27,2,7),_FfCurrentStaticEntryInvalidCount_Type())
ffCurrentStaticEntryInvalidCount.setMaxAccess(_F)
if mibBuilder.loadTexts:ffCurrentStaticEntryInvalidCount.setStatus(_C)
_FfTotalEntryCount_Type=Counter32
_FfTotalEntryCount_Object=MibScalar
ffTotalEntryCount=_FfTotalEntryCount_Object((1,3,6,1,4,1,2076,27,2,8),_FfTotalEntryCount_Type())
ffTotalEntryCount.setMaxAccess(_F)
if mibBuilder.loadTexts:ffTotalEntryCount.setStatus(_C)
_FfStaticEntryCount_Type=Counter32
_FfStaticEntryCount_Object=MibScalar
ffStaticEntryCount=_FfStaticEntryCount_Object((1,3,6,1,4,1,2076,27,2,9),_FfStaticEntryCount_Type())
ffStaticEntryCount.setMaxAccess(_F)
if mibBuilder.loadTexts:ffStaticEntryCount.setStatus(_C)
_FfTotalPktsFastForwarded_Type=Counter32
_FfTotalPktsFastForwarded_Object=MibScalar
ffTotalPktsFastForwarded=_FfTotalPktsFastForwarded_Object((1,3,6,1,4,1,2076,27,2,10),_FfTotalPktsFastForwarded_Type())
ffTotalPktsFastForwarded.setMaxAccess(_F)
if mibBuilder.loadTexts:ffTotalPktsFastForwarded.setStatus(_C)
_FfHostCacheTable_Object=MibTable
ffHostCacheTable=_FfHostCacheTable_Object((1,3,6,1,4,1,2076,27,2,11))
if mibBuilder.loadTexts:ffHostCacheTable.setStatus(_C)
_FfHostCacheEntry_Object=MibTableRow
ffHostCacheEntry=_FfHostCacheEntry_Object((1,3,6,1,4,1,2076,27,2,11,1))
ffHostCacheEntry.setIndexNames((0,_E,_AD))
if mibBuilder.loadTexts:ffHostCacheEntry.setStatus(_C)
_FfHostCacheDestAddr_Type=IpAddress
_FfHostCacheDestAddr_Object=MibTableColumn
ffHostCacheDestAddr=_FfHostCacheDestAddr_Object((1,3,6,1,4,1,2076,27,2,11,1,1),_FfHostCacheDestAddr_Type())
ffHostCacheDestAddr.setMaxAccess(_I)
if mibBuilder.loadTexts:ffHostCacheDestAddr.setStatus(_C)
_FfHostCacheNextHopAddr_Type=IpAddress
_FfHostCacheNextHopAddr_Object=MibTableColumn
ffHostCacheNextHopAddr=_FfHostCacheNextHopAddr_Object((1,3,6,1,4,1,2076,27,2,11,1,2),_FfHostCacheNextHopAddr_Type())
ffHostCacheNextHopAddr.setMaxAccess(_G)
if mibBuilder.loadTexts:ffHostCacheNextHopAddr.setStatus(_C)
_FfHostCacheIfIndex_Type=InterfaceIndex
_FfHostCacheIfIndex_Object=MibTableColumn
ffHostCacheIfIndex=_FfHostCacheIfIndex_Object((1,3,6,1,4,1,2076,27,2,11,1,3),_FfHostCacheIfIndex_Type())
ffHostCacheIfIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:ffHostCacheIfIndex.setStatus(_C)
class _FfHostCacheNextHopMediaAddr_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,6))
_FfHostCacheNextHopMediaAddr_Type.__name__=_K
_FfHostCacheNextHopMediaAddr_Object=MibTableColumn
ffHostCacheNextHopMediaAddr=_FfHostCacheNextHopMediaAddr_Object((1,3,6,1,4,1,2076,27,2,11,1,4),_FfHostCacheNextHopMediaAddr_Type())
ffHostCacheNextHopMediaAddr.setMaxAccess(_G)
if mibBuilder.loadTexts:ffHostCacheNextHopMediaAddr.setStatus(_C)
_FfHostCacheHits_Type=Counter32
_FfHostCacheHits_Object=MibTableColumn
ffHostCacheHits=_FfHostCacheHits_Object((1,3,6,1,4,1,2076,27,2,11,1,5),_FfHostCacheHits_Type())
ffHostCacheHits.setMaxAccess(_F)
if mibBuilder.loadTexts:ffHostCacheHits.setStatus(_C)
_FfHostCacheLastHitTime_Type=TimeStamp
_FfHostCacheLastHitTime_Object=MibTableColumn
ffHostCacheLastHitTime=_FfHostCacheLastHitTime_Object((1,3,6,1,4,1,2076,27,2,11,1,6),_FfHostCacheLastHitTime_Type())
ffHostCacheLastHitTime.setMaxAccess(_F)
if mibBuilder.loadTexts:ffHostCacheLastHitTime.setStatus(_C)
class _FfHostCacheEntryType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('static',1),('dynamic',2)))
_FfHostCacheEntryType_Type.__name__=_D
_FfHostCacheEntryType_Object=MibTableColumn
ffHostCacheEntryType=_FfHostCacheEntryType_Object((1,3,6,1,4,1,2076,27,2,11,1,7),_FfHostCacheEntryType_Type())
ffHostCacheEntryType.setMaxAccess(_G)
if mibBuilder.loadTexts:ffHostCacheEntryType.setStatus(_C)
_FfHostCacheRowStatus_Type=RowStatus
_FfHostCacheRowStatus_Object=MibTableColumn
ffHostCacheRowStatus=_FfHostCacheRowStatus_Object((1,3,6,1,4,1,2076,27,2,11,1,8),_FfHostCacheRowStatus_Type())
ffHostCacheRowStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:ffHostCacheRowStatus.setStatus(_C)
_Fm_ObjectIdentity=ObjectIdentity
fm=_Fm_ObjectIdentity((1,3,6,1,4,1,2076,27,3))
class _FmMemoryResourceTrapEnable_Type(TruthValue):defaultValue=1
_FmMemoryResourceTrapEnable_Type.__name__=_J
_FmMemoryResourceTrapEnable_Object=MibScalar
fmMemoryResourceTrapEnable=_FmMemoryResourceTrapEnable_Object((1,3,6,1,4,1,2076,27,3,1),_FmMemoryResourceTrapEnable_Type())
fmMemoryResourceTrapEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:fmMemoryResourceTrapEnable.setStatus(_C)
class _FmTimersResourceTrapEnable_Type(TruthValue):defaultValue=1
_FmTimersResourceTrapEnable_Type.__name__=_J
_FmTimersResourceTrapEnable_Object=MibScalar
fmTimersResourceTrapEnable=_FmTimersResourceTrapEnable_Object((1,3,6,1,4,1,2076,27,3,2),_FmTimersResourceTrapEnable_Type())
fmTimersResourceTrapEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:fmTimersResourceTrapEnable.setStatus(_C)
class _FmTracingEnable_Type(Integer32):defaultValue=0
_FmTracingEnable_Type.__name__=_D
_FmTracingEnable_Object=MibScalar
fmTracingEnable=_FmTracingEnable_Object((1,3,6,1,4,1,2076,27,3,3),_FmTracingEnable_Type())
fmTracingEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:fmTracingEnable.setStatus(_C)
_FmMemAllocFailCount_Type=Counter32
_FmMemAllocFailCount_Object=MibScalar
fmMemAllocFailCount=_FmMemAllocFailCount_Object((1,3,6,1,4,1,2076,27,3,4),_FmMemAllocFailCount_Type())
fmMemAllocFailCount.setMaxAccess(_F)
if mibBuilder.loadTexts:fmMemAllocFailCount.setStatus(_A)
_FmTimerReqFailCount_Type=Counter32
_FmTimerReqFailCount_Object=MibScalar
fmTimerReqFailCount=_FmTimerReqFailCount_Object((1,3,6,1,4,1,2076,27,3,5),_FmTimerReqFailCount_Type())
fmTimerReqFailCount.setMaxAccess(_F)
if mibBuilder.loadTexts:fmTimerReqFailCount.setStatus(_A)
_Traps_ObjectIdentity=ObjectIdentity
traps=_Traps_ObjectIdentity((1,3,6,1,4,1,2076,27,4))
_TrapPrefix_ObjectIdentity=ObjectIdentity
trapPrefix=_TrapPrefix_ObjectIdentity((1,3,6,1,4,1,2076,27,4,0))
_Pa_ObjectIdentity=ObjectIdentity
pa=_Pa_ObjectIdentity((1,3,6,1,4,1,2076,27,5))
_FsPacketAnalyserTable_Object=MibTable
fsPacketAnalyserTable=_FsPacketAnalyserTable_Object((1,3,6,1,4,1,2076,27,5,1))
if mibBuilder.loadTexts:fsPacketAnalyserTable.setStatus(_A)
_FsPacketAnalyserEntry_Object=MibTableRow
fsPacketAnalyserEntry=_FsPacketAnalyserEntry_Object((1,3,6,1,4,1,2076,27,5,1,1))
fsPacketAnalyserEntry.setIndexNames((0,_E,_AE))
if mibBuilder.loadTexts:fsPacketAnalyserEntry.setStatus(_A)
_FsPacketAnalyserIndex_Type=Unsigned32
_FsPacketAnalyserIndex_Object=MibTableColumn
fsPacketAnalyserIndex=_FsPacketAnalyserIndex_Object((1,3,6,1,4,1,2076,27,5,1,1,1),_FsPacketAnalyserIndex_Type())
fsPacketAnalyserIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:fsPacketAnalyserIndex.setStatus(_A)
class _FsPacketAnalyserWatchValue_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,1600))
_FsPacketAnalyserWatchValue_Type.__name__=_O
_FsPacketAnalyserWatchValue_Object=MibTableColumn
fsPacketAnalyserWatchValue=_FsPacketAnalyserWatchValue_Object((1,3,6,1,4,1,2076,27,5,1,1,2),_FsPacketAnalyserWatchValue_Type())
fsPacketAnalyserWatchValue.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPacketAnalyserWatchValue.setStatus(_A)
class _FsPacketAnalyserWatchMask_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,1600))
_FsPacketAnalyserWatchMask_Type.__name__=_O
_FsPacketAnalyserWatchMask_Object=MibTableColumn
fsPacketAnalyserWatchMask=_FsPacketAnalyserWatchMask_Object((1,3,6,1,4,1,2076,27,5,1,1,3),_FsPacketAnalyserWatchMask_Type())
fsPacketAnalyserWatchMask.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPacketAnalyserWatchMask.setStatus(_A)
_FsPacketAnalyserWatchPorts_Type=PortList
_FsPacketAnalyserWatchPorts_Object=MibTableColumn
fsPacketAnalyserWatchPorts=_FsPacketAnalyserWatchPorts_Object((1,3,6,1,4,1,2076,27,5,1,1,4),_FsPacketAnalyserWatchPorts_Type())
fsPacketAnalyserWatchPorts.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPacketAnalyserWatchPorts.setStatus(_A)
_FsPacketAnalyserMatchPorts_Type=PortList
_FsPacketAnalyserMatchPorts_Object=MibTableColumn
fsPacketAnalyserMatchPorts=_FsPacketAnalyserMatchPorts_Object((1,3,6,1,4,1,2076,27,5,1,1,5),_FsPacketAnalyserMatchPorts_Type())
fsPacketAnalyserMatchPorts.setMaxAccess(_F)
if mibBuilder.loadTexts:fsPacketAnalyserMatchPorts.setStatus(_A)
_FsPacketAnalyserCounter_Type=Counter32
_FsPacketAnalyserCounter_Object=MibTableColumn
fsPacketAnalyserCounter=_FsPacketAnalyserCounter_Object((1,3,6,1,4,1,2076,27,5,1,1,6),_FsPacketAnalyserCounter_Type())
fsPacketAnalyserCounter.setMaxAccess(_F)
if mibBuilder.loadTexts:fsPacketAnalyserCounter.setStatus(_A)
_FsPacketAnalyserTime_Type=TimeTicks
_FsPacketAnalyserTime_Object=MibTableColumn
fsPacketAnalyserTime=_FsPacketAnalyserTime_Object((1,3,6,1,4,1,2076,27,5,1,1,7),_FsPacketAnalyserTime_Type())
fsPacketAnalyserTime.setMaxAccess(_F)
if mibBuilder.loadTexts:fsPacketAnalyserTime.setStatus(_A)
_FsPacketAnalyserCreateTime_Type=TimeTicks
_FsPacketAnalyserCreateTime_Object=MibTableColumn
fsPacketAnalyserCreateTime=_FsPacketAnalyserCreateTime_Object((1,3,6,1,4,1,2076,27,5,1,1,8),_FsPacketAnalyserCreateTime_Type())
fsPacketAnalyserCreateTime.setMaxAccess(_F)
if mibBuilder.loadTexts:fsPacketAnalyserCreateTime.setStatus(_A)
_FsPacketAnalyserStatus_Type=RowStatus
_FsPacketAnalyserStatus_Object=MibTableColumn
fsPacketAnalyserStatus=_FsPacketAnalyserStatus_Object((1,3,6,1,4,1,2076,27,5,1,1,9),_FsPacketAnalyserStatus_Type())
fsPacketAnalyserStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPacketAnalyserStatus.setStatus(_A)
_FsPacketTransmitterTable_Object=MibTable
fsPacketTransmitterTable=_FsPacketTransmitterTable_Object((1,3,6,1,4,1,2076,27,5,2))
if mibBuilder.loadTexts:fsPacketTransmitterTable.setStatus(_A)
_FsPacketTransmitterEntry_Object=MibTableRow
fsPacketTransmitterEntry=_FsPacketTransmitterEntry_Object((1,3,6,1,4,1,2076,27,5,2,1))
fsPacketTransmitterEntry.setIndexNames((0,_E,_AF))
if mibBuilder.loadTexts:fsPacketTransmitterEntry.setStatus(_A)
_FsPacketTransmitterIndex_Type=Unsigned32
_FsPacketTransmitterIndex_Object=MibTableColumn
fsPacketTransmitterIndex=_FsPacketTransmitterIndex_Object((1,3,6,1,4,1,2076,27,5,2,1,1),_FsPacketTransmitterIndex_Type())
fsPacketTransmitterIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:fsPacketTransmitterIndex.setStatus(_A)
class _FsPacketTransmitterValue_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,1600))
_FsPacketTransmitterValue_Type.__name__=_O
_FsPacketTransmitterValue_Object=MibTableColumn
fsPacketTransmitterValue=_FsPacketTransmitterValue_Object((1,3,6,1,4,1,2076,27,5,2,1,2),_FsPacketTransmitterValue_Type())
fsPacketTransmitterValue.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPacketTransmitterValue.setStatus(_A)
_FsPacketTransmitterPort_Type=PortList
_FsPacketTransmitterPort_Object=MibTableColumn
fsPacketTransmitterPort=_FsPacketTransmitterPort_Object((1,3,6,1,4,1,2076,27,5,2,1,3),_FsPacketTransmitterPort_Type())
fsPacketTransmitterPort.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPacketTransmitterPort.setStatus(_A)
_FsPacketTransmitterInterval_Type=TimeTicks
_FsPacketTransmitterInterval_Object=MibTableColumn
fsPacketTransmitterInterval=_FsPacketTransmitterInterval_Object((1,3,6,1,4,1,2076,27,5,2,1,4),_FsPacketTransmitterInterval_Type())
fsPacketTransmitterInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPacketTransmitterInterval.setStatus(_A)
_FsPacketTransmitterCount_Type=Unsigned32
_FsPacketTransmitterCount_Object=MibTableColumn
fsPacketTransmitterCount=_FsPacketTransmitterCount_Object((1,3,6,1,4,1,2076,27,5,2,1,5),_FsPacketTransmitterCount_Type())
fsPacketTransmitterCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPacketTransmitterCount.setStatus(_A)
_FsPacketTransmitterStatus_Type=RowStatus
_FsPacketTransmitterStatus_Object=MibTableColumn
fsPacketTransmitterStatus=_FsPacketTransmitterStatus_Object((1,3,6,1,4,1,2076,27,5,2,1,6),_FsPacketTransmitterStatus_Type())
fsPacketTransmitterStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPacketTransmitterStatus.setStatus(_A)
ifMainEntry.registerAugmentions((_E,_AG))
ifMainExtEntry.setIndexNames(*ifMainEntry.getIndexNames())
ifEntry.registerAugmentions((_E,_AH))
ifHCErrorEntry.setIndexNames(*ifEntry.getIndexNames())
fmLowTimerResource=NotificationType((1,3,6,1,4,1,2076,27,4,0,1))
fmLowTimerResource.setObjects((_E,_AI))
if mibBuilder.loadTexts:fmLowTimerResource.setStatus(_C)
fmLowBufferResource=NotificationType((1,3,6,1,4,1,2076,27,4,0,2))
fmLowBufferResource.setObjects((_E,_AJ))
if mibBuilder.loadTexts:fmLowBufferResource.setStatus(_C)
ffStaticEntryInvalid=NotificationType((1,3,6,1,4,1,2076,27,4,0,3))
ffStaticEntryInvalid.setObjects(*((_E,_AK),(_E,_AL)))
if mibBuilder.loadTexts:ffStaticEntryInvalid.setStatus(_C)
ifCreated=NotificationType((1,3,6,1,4,1,2076,27,4,0,4))
ifCreated.setObjects((_E,_H))
if mibBuilder.loadTexts:ifCreated.setStatus(_A)
ifDeleted=NotificationType((1,3,6,1,4,1,2076,27,4,0,5))
ifDeleted.setObjects((_E,_H))
if mibBuilder.loadTexts:ifDeleted.setStatus(_A)
ifUfdEnabled=NotificationType((1,3,6,1,4,1,2076,27,4,0,6))
ifUfdEnabled.setObjects(*((_E,_H),(_E,_V)))
if mibBuilder.loadTexts:ifUfdEnabled.setStatus(_A)
ifUfdErrorDisabled=NotificationType((1,3,6,1,4,1,2076,27,4,0,7))
ifUfdErrorDisabled.setObjects(*((_E,_H),(_E,_V)))
if mibBuilder.loadTexts:ifUfdErrorDisabled.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'fscfa':fscfa,'if':_pysmi_if,'ifMaxInterfaces':ifMaxInterfaces,'ifMaxPhysInterfaces':ifMaxPhysInterfaces,'ifAvailableIndex':ifAvailableIndex,'ifMainTable':ifMainTable,'ifMainEntry':ifMainEntry,_H:ifMainIndex,'ifMainType':ifMainType,'ifMainMtu':ifMainMtu,'ifMainAdminStatus':ifMainAdminStatus,'ifMainOperStatus':ifMainOperStatus,'ifMainEncapType':ifMainEncapType,'ifMainBrgPortType':ifMainBrgPortType,'ifMainRowStatus':ifMainRowStatus,'ifMainSubType':ifMainSubType,'ifMainNetworkType':ifMainNetworkType,'ifMainWanType':ifMainWanType,'ifMainDesc':ifMainDesc,'ifMainStorageType':ifMainStorageType,'ifMainExtSubType':ifMainExtSubType,'ifMainPortRole':ifMainPortRole,_V:ifMainUfdOperStatus,'ifMainUfdGroupId':ifMainUfdGroupId,'ifMainUfdDownlinkDisabledCount':ifMainUfdDownlinkDisabledCount,'ifMainUfdDownlinkEnabledCount':ifMainUfdDownlinkEnabledCount,'ifMainDesigUplinkStatus':ifMainDesigUplinkStatus,'ifIpTable':ifIpTable,'ifIpEntry':ifIpEntry,'ifIpAddrAllocMethod':ifIpAddrAllocMethod,'ifIpAddr':ifIpAddr,'ifIpSubnetMask':ifIpSubnetMask,'ifIpBroadcastAddr':ifIpBroadcastAddr,'ifIpForwardingEnable':ifIpForwardingEnable,'ifIpAddrAllocProtocol':ifIpAddrAllocProtocol,'ifIpDestMacAddress':ifIpDestMacAddress,'ifIpUnnumAssocIPIf':ifIpUnnumAssocIPIf,'ifIpIntfStatsEnable':ifIpIntfStatsEnable,'ifIpPortVlanId':ifIpPortVlanId,'ifWanTable':ifWanTable,'ifWanEntry':ifWanEntry,'ifWanInterfaceType':ifWanInterfaceType,'ifWanConnectionType':ifWanConnectionType,'ifWanVirtualPathId':ifWanVirtualPathId,'ifWanVirtualCircuitId':ifWanVirtualCircuitId,'ifWanPeerMediaAddress':ifWanPeerMediaAddress,'ifWanSustainedSpeed':ifWanSustainedSpeed,'ifWanPeakSpeed':ifWanPeakSpeed,'ifWanMaxBurstSize':ifWanMaxBurstSize,'ifWanIpQosProfileIndex':ifWanIpQosProfileIndex,'ifWanIdleTimeout':ifWanIdleTimeout,'ifWanPeerIpAddr':ifWanPeerIpAddr,'ifWanRtpHdrComprEnable':ifWanRtpHdrComprEnable,'ifWanPersistence':ifWanPersistence,'ifAutoCktProfileTable':ifAutoCktProfileTable,'ifAutoProfileEntry':ifAutoProfileEntry,_A3:ifAutoProfileIfIndex,'ifAutoProfileIfType':ifAutoProfileIfType,'ifAutoProfileIpAddrAllocMethod':ifAutoProfileIpAddrAllocMethod,'ifAutoProfileDefIpSubnetMask':ifAutoProfileDefIpSubnetMask,'ifAutoProfileDefIpBroadcastAddr':ifAutoProfileDefIpBroadcastAddr,'ifAutoProfileIdleTimeout':ifAutoProfileIdleTimeout,'ifAutoProfileEncapType':ifAutoProfileEncapType,'ifAutoProfileIpQosProfileIndex':ifAutoProfileIpQosProfileIndex,'ifAutoProfileRowStatus':ifAutoProfileRowStatus,'ifIvrTable':ifIvrTable,'ifIvrEntry':ifIvrEntry,'ifIvrBridgedIface':ifIvrBridgedIface,'ifSetMgmtVlanList':ifSetMgmtVlanList,'ifResetMgmtVlanList':ifResetMgmtVlanList,'ifSecondaryIpAddressTable':ifSecondaryIpAddressTable,'ifSecondaryIpAddressEntry':ifSecondaryIpAddressEntry,_A4:ifSecondaryIpAddress,'ifSecondaryIpSubnetMask':ifSecondaryIpSubnetMask,'ifSecondaryIpBroadcastAddr':ifSecondaryIpBroadcastAddr,'ifSecondaryIpRowStatus':ifSecondaryIpRowStatus,'ifMainExtTable':ifMainExtTable,_AG:ifMainExtEntry,'ifMainExtMacAddress':ifMainExtMacAddress,'ifMainExtSysSpecificPortID':ifMainExtSysSpecificPortID,'ifMainExtInterfaceType':ifMainExtInterfaceType,'ifMainExtPortSecState':ifMainExtPortSecState,'ifMainExtInPkts':ifMainExtInPkts,'ifMainExtLinkUpEnabledStatus':ifMainExtLinkUpEnabledStatus,'ifMainExtLinkUpDelayTimer':ifMainExtLinkUpDelayTimer,'ifMainExtLinkUpRemainingTime':ifMainExtLinkUpRemainingTime,'ifCustTLVTable':ifCustTLVTable,'ifCustTLVEntry':ifCustTLVEntry,_A5:ifCustTLVType,'ifCustTLVLength':ifCustTLVLength,'ifCustTLVValue':ifCustTLVValue,'ifCustTLVRowStatus':ifCustTLVRowStatus,'ifCustOpaqueAttrTable':ifCustOpaqueAttrTable,'ifCustOpaqueAttrEntry':ifCustOpaqueAttrEntry,_A6:ifCustOpaqueAttributeID,'ifCustOpaqueAttribute':ifCustOpaqueAttribute,'ifCustOpaqueRowStatus':ifCustOpaqueRowStatus,'ifBridgeILanIfTable':ifBridgeILanIfTable,'ifBridgeILanIfEntry':ifBridgeILanIfEntry,'ifBridgeILanIfStatus':ifBridgeILanIfStatus,'ifTypeProtoDenyTable':ifTypeProtoDenyTable,'ifTypeProtoDenyEntry':ifTypeProtoDenyEntry,_A7:ifTypeProtoDenyContextId,_A8:ifTypeProtoDenyMainType,_A9:ifTypeProtoDenyBrgPortType,_AA:ifTypeProtoDenyProtocol,'ifTypeProtoDenyRowStatus':ifTypeProtoDenyRowStatus,'ifmDebug':ifmDebug,'ifIvrMappingTable':ifIvrMappingTable,'ifIvrMappingEntry':ifIvrMappingEntry,_AB:ifIvrAssociatedVlan,'ifIvrMappingRowStatus':ifIvrMappingRowStatus,'ifHCErrorTable':ifHCErrorTable,_AH:ifHCErrorEntry,'ifHCInDiscards':ifHCInDiscards,'ifHCInErrors':ifHCInErrors,'ifHCInUnknownProtos':ifHCInUnknownProtos,'ifHCOutDiscards':ifHCOutDiscards,'ifHCOutErrors':ifHCOutErrors,'ifSecurityBridging':ifSecurityBridging,'ifSetSecVlanList':ifSetSecVlanList,'ifResetSecVlanList':ifResetSecVlanList,'ifSecIvrIfIndex':ifSecIvrIfIndex,'ifAvailableIndexTable':ifAvailableIndexTable,'ifAvailableIndexEntry':ifAvailableIndexEntry,'ifAvailableFreeIndex':ifAvailableFreeIndex,'ifACTable':ifACTable,'ifACEntry':ifACEntry,'ifACPortIdentifier':ifACPortIdentifier,'ifACCustomerVlan':ifACCustomerVlan,'ifUfdSystemControl':ifUfdSystemControl,'ifUfdModuleStatus':ifUfdModuleStatus,'ifSplitHorizonSysControl':ifSplitHorizonSysControl,'ifSplitHorizonModStatus':ifSplitHorizonModStatus,'ifUfdGroupTable':ifUfdGroupTable,'ifUfdGroupEntry':ifUfdGroupEntry,_AC:ifUfdGroupId,'ifUfdGroupName':ifUfdGroupName,'ifUfdGroupStatus':ifUfdGroupStatus,'ifUfdGroupUplinkPorts':ifUfdGroupUplinkPorts,'ifUfdGroupDownlinkPorts':ifUfdGroupDownlinkPorts,'ifUfdGroupDesigUplinkPort':ifUfdGroupDesigUplinkPort,'ifUfdGroupUplinkCount':ifUfdGroupUplinkCount,'ifUfdGroupDownlinkCount':ifUfdGroupDownlinkCount,'ifUfdGroupRowStatus':ifUfdGroupRowStatus,'ifLinkUpEnabledStatus':ifLinkUpEnabledStatus,'ifOOBNode0SecondaryIpAddress':ifOOBNode0SecondaryIpAddress,'ifOOBNode0SecondaryIpMask':ifOOBNode0SecondaryIpMask,'ifOOBNode1SecondaryIpAddress':ifOOBNode1SecondaryIpAddress,'ifOOBNode1SecondaryIpMask':ifOOBNode1SecondaryIpMask,'ff':ff,'ffFastForwardingEnable':ffFastForwardingEnable,'ffCacheSize':ffCacheSize,'ffIpChecksumValidationEnable':ffIpChecksumValidationEnable,'ffCachePurgeCount':ffCachePurgeCount,'ffCacheLastPurgeTime':ffCacheLastPurgeTime,'ffStaticEntryInvalidTrapEnable':ffStaticEntryInvalidTrapEnable,'ffCurrentStaticEntryInvalidCount':ffCurrentStaticEntryInvalidCount,'ffTotalEntryCount':ffTotalEntryCount,'ffStaticEntryCount':ffStaticEntryCount,'ffTotalPktsFastForwarded':ffTotalPktsFastForwarded,'ffHostCacheTable':ffHostCacheTable,'ffHostCacheEntry':ffHostCacheEntry,_AD:ffHostCacheDestAddr,'ffHostCacheNextHopAddr':ffHostCacheNextHopAddr,_AK:ffHostCacheIfIndex,'ffHostCacheNextHopMediaAddr':ffHostCacheNextHopMediaAddr,'ffHostCacheHits':ffHostCacheHits,'ffHostCacheLastHitTime':ffHostCacheLastHitTime,_AL:ffHostCacheEntryType,'ffHostCacheRowStatus':ffHostCacheRowStatus,'fm':fm,'fmMemoryResourceTrapEnable':fmMemoryResourceTrapEnable,'fmTimersResourceTrapEnable':fmTimersResourceTrapEnable,'fmTracingEnable':fmTracingEnable,_AJ:fmMemAllocFailCount,_AI:fmTimerReqFailCount,'traps':traps,'trapPrefix':trapPrefix,'fmLowTimerResource':fmLowTimerResource,'fmLowBufferResource':fmLowBufferResource,'ffStaticEntryInvalid':ffStaticEntryInvalid,'ifCreated':ifCreated,'ifDeleted':ifDeleted,'ifUfdEnabled':ifUfdEnabled,'ifUfdErrorDisabled':ifUfdErrorDisabled,'pa':pa,'fsPacketAnalyserTable':fsPacketAnalyserTable,'fsPacketAnalyserEntry':fsPacketAnalyserEntry,_AE:fsPacketAnalyserIndex,'fsPacketAnalyserWatchValue':fsPacketAnalyserWatchValue,'fsPacketAnalyserWatchMask':fsPacketAnalyserWatchMask,'fsPacketAnalyserWatchPorts':fsPacketAnalyserWatchPorts,'fsPacketAnalyserMatchPorts':fsPacketAnalyserMatchPorts,'fsPacketAnalyserCounter':fsPacketAnalyserCounter,'fsPacketAnalyserTime':fsPacketAnalyserTime,'fsPacketAnalyserCreateTime':fsPacketAnalyserCreateTime,'fsPacketAnalyserStatus':fsPacketAnalyserStatus,'fsPacketTransmitterTable':fsPacketTransmitterTable,'fsPacketTransmitterEntry':fsPacketTransmitterEntry,_AF:fsPacketTransmitterIndex,'fsPacketTransmitterValue':fsPacketTransmitterValue,'fsPacketTransmitterPort':fsPacketTransmitterPort,'fsPacketTransmitterInterval':fsPacketTransmitterInterval,'fsPacketTransmitterCount':fsPacketTransmitterCount,'fsPacketTransmitterStatus':fsPacketTransmitterStatus})