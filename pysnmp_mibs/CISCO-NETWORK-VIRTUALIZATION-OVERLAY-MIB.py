_A9='cnvoVNetVrfStatsGroup'
_A8='cnvoNvoPerPeerInMulticastStatsGroup'
_A7='cnvoNvoPerPeerInUnicastStatsGroup'
_A6='cnvoNvoPerPeerOutMulticastStatsGroup'
_A5='cnvoNvoPerPeerOutUnicastStatsGroup'
_A4='cnvoVirtualNetworkStatsGroup'
_A3='cnvoPeerGroup'
_A2='cnvoVirtualNetworkGroup'
_A1='cnvoNvoGroup'
_A0='cnvoVNetVrfEgressBytes'
_z='cnvoVNetVrfEgressPackets'
_y='cnvoVNetVrfIngressBytes'
_x='cnvoVNetVrfIngressPackets'
_w='cnvoNvoPeerOutMulticastBytes'
_v='cnvoNvoPeerOutMulticastPackets'
_u='cnvoNvoPeerInMulticastBytes'
_t='cnvoNvoPeerInMulticastPackets'
_s='cnvoNvoPeerInUnicastBytes'
_r='cnvoNvoPeerInUnicastPackets'
_q='cnvoNvoPeerOutUnicastBytes'
_p='cnvoNvoPeerOutUnicastPackets'
_o='cnvoVNetInMulticastBytes'
_n='cnvoVNetInMulticastPackets'
_m='cnvoVNetInUnicastBytes'
_l='cnvoVNetInUnicastPackets'
_k='cnvoVNetOutMulticastBytes'
_j='cnvoVNetOutMulticastPackets'
_i='cnvoVNetOutUnicastBytes'
_h='cnvoVNetOutUnicastPackets'
_g='cnvoPeerLearningSourceType'
_f='cnvoPeerUpTime'
_e='cnvoVNetRouterMacAddr'
_d='cnvoVNetIpVrfOrBridgeDomainName'
_c='cnvoVNetVniType'
_b='cnvoVNetHostReachability'
_a='cnvoVNetReplication'
_Z='cnvoVNetArpSuppression'
_Y='cnvoVNetVlan'
_X='cnvoVNetIpMcastAddr'
_W='cnvoVNetIpMcastAddrType'
_V='cnvoNvoRowStatus'
_U='cnvoNvoStorageType'
_T='cnvoNvoConfiguredVni'
_S='cnvoNvoSourceInterface'
_R='cnvoNvoEncapType'
_Q='cnvoVNetVrfStatsVni'
_P='cnvoVNetVrfStatsVrfName'
_O='StorageType'
_N='InetAddress'
_M='InterfaceIndexOrZero'
_L='cnvoPeerIpAddr'
_K='cnvoPeerIpAddrType'
_J='cnvoVNetLocalVNetId'
_I='read-create'
_H='unknown'
_G='not-accessible'
_F='cnvoNvoInstanceId'
_E='read-write'
_D='Integer32'
_C='read-only'
_B='CISCO-NETWORK-VIRTUALIZATION-OVERLAY-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
VlanIndexOrZero,=mibBuilder.importSymbols('CISCO-PRIVATE-VLAN-MIB','VlanIndexOrZero')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
InterfaceIndexOrZero,=mibBuilder.importSymbols('IF-MIB',_M)
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB',_N,'InetAddressType')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,PhysAddress,RowStatus,StorageType,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','RowStatus',_O,'TextualConvention')
ciscoNetworkVirtualizationOverlayMIB=ModuleIdentity((1,3,6,1,4,1,9,9,820))
if mibBuilder.loadTexts:ciscoNetworkVirtualizationOverlayMIB.setRevisions(('2015-01-26 00:00',))
_CnvoMIBNotifs_ObjectIdentity=ObjectIdentity
cnvoMIBNotifs=_CnvoMIBNotifs_ObjectIdentity((1,3,6,1,4,1,9,9,820,0))
_CnvoMIBObjects_ObjectIdentity=ObjectIdentity
cnvoMIBObjects=_CnvoMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,820,1))
_CnvoNvoObjects_ObjectIdentity=ObjectIdentity
cnvoNvoObjects=_CnvoNvoObjects_ObjectIdentity((1,3,6,1,4,1,9,9,820,1,1))
_CnvoNvoTable_Object=MibTable
cnvoNvoTable=_CnvoNvoTable_Object((1,3,6,1,4,1,9,9,820,1,1,1))
if mibBuilder.loadTexts:cnvoNvoTable.setStatus(_A)
_CnvoNvoEntry_Object=MibTableRow
cnvoNvoEntry=_CnvoNvoEntry_Object((1,3,6,1,4,1,9,9,820,1,1,1,1))
cnvoNvoEntry.setIndexNames((0,_B,_F))
if mibBuilder.loadTexts:cnvoNvoEntry.setStatus(_A)
_CnvoNvoInstanceId_Type=Unsigned32
_CnvoNvoInstanceId_Object=MibTableColumn
cnvoNvoInstanceId=_CnvoNvoInstanceId_Object((1,3,6,1,4,1,9,9,820,1,1,1,1,1),_CnvoNvoInstanceId_Type())
cnvoNvoInstanceId.setMaxAccess(_G)
if mibBuilder.loadTexts:cnvoNvoInstanceId.setStatus(_A)
class _CnvoNvoEncapType_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_H,1),('vxlan',2),('nvgre',3)))
_CnvoNvoEncapType_Type.__name__=_D
_CnvoNvoEncapType_Object=MibTableColumn
cnvoNvoEncapType=_CnvoNvoEncapType_Object((1,3,6,1,4,1,9,9,820,1,1,1,1,2),_CnvoNvoEncapType_Type())
cnvoNvoEncapType.setMaxAccess(_I)
if mibBuilder.loadTexts:cnvoNvoEncapType.setStatus(_A)
class _CnvoNvoSourceInterface_Type(InterfaceIndexOrZero):defaultValue=0
_CnvoNvoSourceInterface_Type.__name__=_M
_CnvoNvoSourceInterface_Object=MibTableColumn
cnvoNvoSourceInterface=_CnvoNvoSourceInterface_Object((1,3,6,1,4,1,9,9,820,1,1,1,1,3),_CnvoNvoSourceInterface_Type())
cnvoNvoSourceInterface.setMaxAccess(_I)
if mibBuilder.loadTexts:cnvoNvoSourceInterface.setStatus(_A)
_CnvoNvoConfiguredVni_Type=SnmpAdminString
_CnvoNvoConfiguredVni_Object=MibTableColumn
cnvoNvoConfiguredVni=_CnvoNvoConfiguredVni_Object((1,3,6,1,4,1,9,9,820,1,1,1,1,4),_CnvoNvoConfiguredVni_Type())
cnvoNvoConfiguredVni.setMaxAccess(_C)
if mibBuilder.loadTexts:cnvoNvoConfiguredVni.setStatus(_A)
class _CnvoNvoStorageType_Type(StorageType):defaultValue=2
_CnvoNvoStorageType_Type.__name__=_O
_CnvoNvoStorageType_Object=MibTableColumn
cnvoNvoStorageType=_CnvoNvoStorageType_Object((1,3,6,1,4,1,9,9,820,1,1,1,1,5),_CnvoNvoStorageType_Type())
cnvoNvoStorageType.setMaxAccess(_I)
if mibBuilder.loadTexts:cnvoNvoStorageType.setStatus(_A)
_CnvoNvoRowStatus_Type=RowStatus
_CnvoNvoRowStatus_Object=MibTableColumn
cnvoNvoRowStatus=_CnvoNvoRowStatus_Object((1,3,6,1,4,1,9,9,820,1,1,1,1,6),_CnvoNvoRowStatus_Type())
cnvoNvoRowStatus.setMaxAccess(_I)
if mibBuilder.loadTexts:cnvoNvoRowStatus.setStatus(_A)
_CnvoVNetTable_Object=MibTable
cnvoVNetTable=_CnvoVNetTable_Object((1,3,6,1,4,1,9,9,820,1,1,2))
if mibBuilder.loadTexts:cnvoVNetTable.setStatus(_A)
_CnvoVNetEntry_Object=MibTableRow
cnvoVNetEntry=_CnvoVNetEntry_Object((1,3,6,1,4,1,9,9,820,1,1,2,1))
cnvoVNetEntry.setIndexNames((0,_B,_F),(0,_B,_J))
if mibBuilder.loadTexts:cnvoVNetEntry.setStatus(_A)
_CnvoVNetLocalVNetId_Type=Unsigned32
_CnvoVNetLocalVNetId_Object=MibTableColumn
cnvoVNetLocalVNetId=_CnvoVNetLocalVNetId_Object((1,3,6,1,4,1,9,9,820,1,1,2,1,1),_CnvoVNetLocalVNetId_Type())
cnvoVNetLocalVNetId.setMaxAccess(_G)
if mibBuilder.loadTexts:cnvoVNetLocalVNetId.setStatus(_A)
_CnvoVNetIpMcastAddrType_Type=InetAddressType
_CnvoVNetIpMcastAddrType_Object=MibTableColumn
cnvoVNetIpMcastAddrType=_CnvoVNetIpMcastAddrType_Object((1,3,6,1,4,1,9,9,820,1,1,2,1,2),_CnvoVNetIpMcastAddrType_Type())
cnvoVNetIpMcastAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:cnvoVNetIpMcastAddrType.setStatus(_A)
_CnvoVNetIpMcastAddr_Type=InetAddress
_CnvoVNetIpMcastAddr_Object=MibTableColumn
cnvoVNetIpMcastAddr=_CnvoVNetIpMcastAddr_Object((1,3,6,1,4,1,9,9,820,1,1,2,1,3),_CnvoVNetIpMcastAddr_Type())
cnvoVNetIpMcastAddr.setMaxAccess(_E)
if mibBuilder.loadTexts:cnvoVNetIpMcastAddr.setStatus(_A)
_CnvoVNetVlan_Type=VlanIndexOrZero
_CnvoVNetVlan_Object=MibTableColumn
cnvoVNetVlan=_CnvoVNetVlan_Object((1,3,6,1,4,1,9,9,820,1,1,2,1,4),_CnvoVNetVlan_Type())
cnvoVNetVlan.setMaxAccess(_E)
if mibBuilder.loadTexts:cnvoVNetVlan.setStatus(_A)
class _CnvoVNetArpSuppression_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('arpSupON',1),('arpSupOFF',2)))
_CnvoVNetArpSuppression_Type.__name__=_D
_CnvoVNetArpSuppression_Object=MibTableColumn
cnvoVNetArpSuppression=_CnvoVNetArpSuppression_Object((1,3,6,1,4,1,9,9,820,1,1,2,1,5),_CnvoVNetArpSuppression_Type())
cnvoVNetArpSuppression.setMaxAccess(_E)
if mibBuilder.loadTexts:cnvoVNetArpSuppression.setStatus(_A)
class _CnvoVNetReplication_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('mcast',1),('unconf',2),('ucastBgp',3),('ucastStatic',4)))
_CnvoVNetReplication_Type.__name__=_D
_CnvoVNetReplication_Object=MibTableColumn
cnvoVNetReplication=_CnvoVNetReplication_Object((1,3,6,1,4,1,9,9,820,1,1,2,1,6),_CnvoVNetReplication_Type())
cnvoVNetReplication.setMaxAccess(_E)
if mibBuilder.loadTexts:cnvoVNetReplication.setStatus(_A)
class _CnvoVNetHostReachability_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_H,1),('hostReachabilityUnconf',2),('dataPlaneL2',3),('controlPlaneL3',4)))
_CnvoVNetHostReachability_Type.__name__=_D
_CnvoVNetHostReachability_Object=MibTableColumn
cnvoVNetHostReachability=_CnvoVNetHostReachability_Object((1,3,6,1,4,1,9,9,820,1,1,2,1,7),_CnvoVNetHostReachability_Type())
cnvoVNetHostReachability.setMaxAccess(_E)
if mibBuilder.loadTexts:cnvoVNetHostReachability.setStatus(_A)
class _CnvoVNetVniType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_H,1),('l2',2),('l3',3)))
_CnvoVNetVniType_Type.__name__=_D
_CnvoVNetVniType_Object=MibTableColumn
cnvoVNetVniType=_CnvoVNetVniType_Object((1,3,6,1,4,1,9,9,820,1,1,2,1,8),_CnvoVNetVniType_Type())
cnvoVNetVniType.setMaxAccess(_E)
if mibBuilder.loadTexts:cnvoVNetVniType.setStatus(_A)
_CnvoVNetIpVrfOrBridgeDomainName_Type=SnmpAdminString
_CnvoVNetIpVrfOrBridgeDomainName_Object=MibTableColumn
cnvoVNetIpVrfOrBridgeDomainName=_CnvoVNetIpVrfOrBridgeDomainName_Object((1,3,6,1,4,1,9,9,820,1,1,2,1,9),_CnvoVNetIpVrfOrBridgeDomainName_Type())
cnvoVNetIpVrfOrBridgeDomainName.setMaxAccess(_E)
if mibBuilder.loadTexts:cnvoVNetIpVrfOrBridgeDomainName.setStatus(_A)
_CnvoVNetRouterMacAddr_Type=InetAddress
_CnvoVNetRouterMacAddr_Object=MibTableColumn
cnvoVNetRouterMacAddr=_CnvoVNetRouterMacAddr_Object((1,3,6,1,4,1,9,9,820,1,1,2,1,10),_CnvoVNetRouterMacAddr_Type())
cnvoVNetRouterMacAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:cnvoVNetRouterMacAddr.setStatus(_A)
_CnvoPeerTable_Object=MibTable
cnvoPeerTable=_CnvoPeerTable_Object((1,3,6,1,4,1,9,9,820,1,1,3))
if mibBuilder.loadTexts:cnvoPeerTable.setStatus(_A)
_CnvoPeerEntry_Object=MibTableRow
cnvoPeerEntry=_CnvoPeerEntry_Object((1,3,6,1,4,1,9,9,820,1,1,3,1))
cnvoPeerEntry.setIndexNames((0,_B,_F),(0,_B,_K),(0,_B,_L))
if mibBuilder.loadTexts:cnvoPeerEntry.setStatus(_A)
_CnvoPeerIpAddrType_Type=InetAddressType
_CnvoPeerIpAddrType_Object=MibTableColumn
cnvoPeerIpAddrType=_CnvoPeerIpAddrType_Object((1,3,6,1,4,1,9,9,820,1,1,3,1,1),_CnvoPeerIpAddrType_Type())
cnvoPeerIpAddrType.setMaxAccess(_G)
if mibBuilder.loadTexts:cnvoPeerIpAddrType.setStatus(_A)
class _CnvoPeerIpAddr_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_CnvoPeerIpAddr_Type.__name__=_N
_CnvoPeerIpAddr_Object=MibTableColumn
cnvoPeerIpAddr=_CnvoPeerIpAddr_Object((1,3,6,1,4,1,9,9,820,1,1,3,1,2),_CnvoPeerIpAddr_Type())
cnvoPeerIpAddr.setMaxAccess(_G)
if mibBuilder.loadTexts:cnvoPeerIpAddr.setStatus(_A)
_CnvoPeerUpTime_Type=DateAndTime
_CnvoPeerUpTime_Object=MibTableColumn
cnvoPeerUpTime=_CnvoPeerUpTime_Object((1,3,6,1,4,1,9,9,820,1,1,3,1,3),_CnvoPeerUpTime_Type())
cnvoPeerUpTime.setMaxAccess(_C)
if mibBuilder.loadTexts:cnvoPeerUpTime.setStatus(_A)
class _CnvoPeerLearningSourceType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_H,1),('dataPlane',2),('controlPlane',3)))
_CnvoPeerLearningSourceType_Type.__name__=_D
_CnvoPeerLearningSourceType_Object=MibTableColumn
cnvoPeerLearningSourceType=_CnvoPeerLearningSourceType_Object((1,3,6,1,4,1,9,9,820,1,1,3,1,4),_CnvoPeerLearningSourceType_Type())
cnvoPeerLearningSourceType.setMaxAccess(_C)
if mibBuilder.loadTexts:cnvoPeerLearningSourceType.setStatus(_A)
_CnvoVNetStatsTable_Object=MibTable
cnvoVNetStatsTable=_CnvoVNetStatsTable_Object((1,3,6,1,4,1,9,9,820,1,1,4))
if mibBuilder.loadTexts:cnvoVNetStatsTable.setStatus(_A)
_CnvoVNetStatsEntry_Object=MibTableRow
cnvoVNetStatsEntry=_CnvoVNetStatsEntry_Object((1,3,6,1,4,1,9,9,820,1,1,4,1))
cnvoVNetStatsEntry.setIndexNames((0,_B,_F),(0,_B,_J))
if mibBuilder.loadTexts:cnvoVNetStatsEntry.setStatus(_A)
_CnvoVNetOutUnicastPackets_Type=Counter64
_CnvoVNetOutUnicastPackets_Object=MibTableColumn
cnvoVNetOutUnicastPackets=_CnvoVNetOutUnicastPackets_Object((1,3,6,1,4,1,9,9,820,1,1,4,1,1),_CnvoVNetOutUnicastPackets_Type())
cnvoVNetOutUnicastPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:cnvoVNetOutUnicastPackets.setStatus(_A)
_CnvoVNetOutUnicastBytes_Type=Counter64
_CnvoVNetOutUnicastBytes_Object=MibTableColumn
cnvoVNetOutUnicastBytes=_CnvoVNetOutUnicastBytes_Object((1,3,6,1,4,1,9,9,820,1,1,4,1,2),_CnvoVNetOutUnicastBytes_Type())
cnvoVNetOutUnicastBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:cnvoVNetOutUnicastBytes.setStatus(_A)
_CnvoVNetOutMulticastPackets_Type=Counter64
_CnvoVNetOutMulticastPackets_Object=MibTableColumn
cnvoVNetOutMulticastPackets=_CnvoVNetOutMulticastPackets_Object((1,3,6,1,4,1,9,9,820,1,1,4,1,3),_CnvoVNetOutMulticastPackets_Type())
cnvoVNetOutMulticastPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:cnvoVNetOutMulticastPackets.setStatus(_A)
_CnvoVNetOutMulticastBytes_Type=Counter64
_CnvoVNetOutMulticastBytes_Object=MibTableColumn
cnvoVNetOutMulticastBytes=_CnvoVNetOutMulticastBytes_Object((1,3,6,1,4,1,9,9,820,1,1,4,1,4),_CnvoVNetOutMulticastBytes_Type())
cnvoVNetOutMulticastBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:cnvoVNetOutMulticastBytes.setStatus(_A)
_CnvoVNetInUnicastPackets_Type=Counter64
_CnvoVNetInUnicastPackets_Object=MibTableColumn
cnvoVNetInUnicastPackets=_CnvoVNetInUnicastPackets_Object((1,3,6,1,4,1,9,9,820,1,1,4,1,5),_CnvoVNetInUnicastPackets_Type())
cnvoVNetInUnicastPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:cnvoVNetInUnicastPackets.setStatus(_A)
_CnvoVNetInUnicastBytes_Type=Counter64
_CnvoVNetInUnicastBytes_Object=MibTableColumn
cnvoVNetInUnicastBytes=_CnvoVNetInUnicastBytes_Object((1,3,6,1,4,1,9,9,820,1,1,4,1,6),_CnvoVNetInUnicastBytes_Type())
cnvoVNetInUnicastBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:cnvoVNetInUnicastBytes.setStatus(_A)
_CnvoVNetInMulticastPackets_Type=Counter64
_CnvoVNetInMulticastPackets_Object=MibTableColumn
cnvoVNetInMulticastPackets=_CnvoVNetInMulticastPackets_Object((1,3,6,1,4,1,9,9,820,1,1,4,1,7),_CnvoVNetInMulticastPackets_Type())
cnvoVNetInMulticastPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:cnvoVNetInMulticastPackets.setStatus(_A)
_CnvoVNetInMulticastBytes_Type=Counter64
_CnvoVNetInMulticastBytes_Object=MibTableColumn
cnvoVNetInMulticastBytes=_CnvoVNetInMulticastBytes_Object((1,3,6,1,4,1,9,9,820,1,1,4,1,8),_CnvoVNetInMulticastBytes_Type())
cnvoVNetInMulticastBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:cnvoVNetInMulticastBytes.setStatus(_A)
_CnvoNvoPeerStatsTable_Object=MibTable
cnvoNvoPeerStatsTable=_CnvoNvoPeerStatsTable_Object((1,3,6,1,4,1,9,9,820,1,1,5))
if mibBuilder.loadTexts:cnvoNvoPeerStatsTable.setStatus(_A)
_CnvoNvoPeerStatsEntry_Object=MibTableRow
cnvoNvoPeerStatsEntry=_CnvoNvoPeerStatsEntry_Object((1,3,6,1,4,1,9,9,820,1,1,5,1))
cnvoNvoPeerStatsEntry.setIndexNames((0,_B,_F),(0,_B,_K),(0,_B,_L))
if mibBuilder.loadTexts:cnvoNvoPeerStatsEntry.setStatus(_A)
_CnvoNvoPeerOutUnicastPackets_Type=Counter64
_CnvoNvoPeerOutUnicastPackets_Object=MibTableColumn
cnvoNvoPeerOutUnicastPackets=_CnvoNvoPeerOutUnicastPackets_Object((1,3,6,1,4,1,9,9,820,1,1,5,1,1),_CnvoNvoPeerOutUnicastPackets_Type())
cnvoNvoPeerOutUnicastPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:cnvoNvoPeerOutUnicastPackets.setStatus(_A)
_CnvoNvoPeerOutUnicastBytes_Type=Counter64
_CnvoNvoPeerOutUnicastBytes_Object=MibTableColumn
cnvoNvoPeerOutUnicastBytes=_CnvoNvoPeerOutUnicastBytes_Object((1,3,6,1,4,1,9,9,820,1,1,5,1,2),_CnvoNvoPeerOutUnicastBytes_Type())
cnvoNvoPeerOutUnicastBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:cnvoNvoPeerOutUnicastBytes.setStatus(_A)
_CnvoNvoPeerOutMulticastPackets_Type=Counter64
_CnvoNvoPeerOutMulticastPackets_Object=MibTableColumn
cnvoNvoPeerOutMulticastPackets=_CnvoNvoPeerOutMulticastPackets_Object((1,3,6,1,4,1,9,9,820,1,1,5,1,3),_CnvoNvoPeerOutMulticastPackets_Type())
cnvoNvoPeerOutMulticastPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:cnvoNvoPeerOutMulticastPackets.setStatus(_A)
_CnvoNvoPeerOutMulticastBytes_Type=Counter64
_CnvoNvoPeerOutMulticastBytes_Object=MibTableColumn
cnvoNvoPeerOutMulticastBytes=_CnvoNvoPeerOutMulticastBytes_Object((1,3,6,1,4,1,9,9,820,1,1,5,1,4),_CnvoNvoPeerOutMulticastBytes_Type())
cnvoNvoPeerOutMulticastBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:cnvoNvoPeerOutMulticastBytes.setStatus(_A)
_CnvoNvoPeerInUnicastPackets_Type=Counter64
_CnvoNvoPeerInUnicastPackets_Object=MibTableColumn
cnvoNvoPeerInUnicastPackets=_CnvoNvoPeerInUnicastPackets_Object((1,3,6,1,4,1,9,9,820,1,1,5,1,5),_CnvoNvoPeerInUnicastPackets_Type())
cnvoNvoPeerInUnicastPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:cnvoNvoPeerInUnicastPackets.setStatus(_A)
_CnvoNvoPeerInUnicastBytes_Type=Counter64
_CnvoNvoPeerInUnicastBytes_Object=MibTableColumn
cnvoNvoPeerInUnicastBytes=_CnvoNvoPeerInUnicastBytes_Object((1,3,6,1,4,1,9,9,820,1,1,5,1,6),_CnvoNvoPeerInUnicastBytes_Type())
cnvoNvoPeerInUnicastBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:cnvoNvoPeerInUnicastBytes.setStatus(_A)
_CnvoNvoPeerInMulticastPackets_Type=Counter64
_CnvoNvoPeerInMulticastPackets_Object=MibTableColumn
cnvoNvoPeerInMulticastPackets=_CnvoNvoPeerInMulticastPackets_Object((1,3,6,1,4,1,9,9,820,1,1,5,1,7),_CnvoNvoPeerInMulticastPackets_Type())
cnvoNvoPeerInMulticastPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:cnvoNvoPeerInMulticastPackets.setStatus(_A)
_CnvoNvoPeerInMulticastBytes_Type=Counter64
_CnvoNvoPeerInMulticastBytes_Object=MibTableColumn
cnvoNvoPeerInMulticastBytes=_CnvoNvoPeerInMulticastBytes_Object((1,3,6,1,4,1,9,9,820,1,1,5,1,8),_CnvoNvoPeerInMulticastBytes_Type())
cnvoNvoPeerInMulticastBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:cnvoNvoPeerInMulticastBytes.setStatus(_A)
_CnvoVNetVrfStatsTable_Object=MibTable
cnvoVNetVrfStatsTable=_CnvoVNetVrfStatsTable_Object((1,3,6,1,4,1,9,9,820,1,1,6))
if mibBuilder.loadTexts:cnvoVNetVrfStatsTable.setStatus(_A)
_CnvoVNetVrfStatsEntry_Object=MibTableRow
cnvoVNetVrfStatsEntry=_CnvoVNetVrfStatsEntry_Object((1,3,6,1,4,1,9,9,820,1,1,6,1))
cnvoVNetVrfStatsEntry.setIndexNames((0,_B,_P),(0,_B,_Q))
if mibBuilder.loadTexts:cnvoVNetVrfStatsEntry.setStatus(_A)
_CnvoVNetVrfStatsVrfName_Type=SnmpAdminString
_CnvoVNetVrfStatsVrfName_Object=MibTableColumn
cnvoVNetVrfStatsVrfName=_CnvoVNetVrfStatsVrfName_Object((1,3,6,1,4,1,9,9,820,1,1,6,1,1),_CnvoVNetVrfStatsVrfName_Type())
cnvoVNetVrfStatsVrfName.setMaxAccess(_G)
if mibBuilder.loadTexts:cnvoVNetVrfStatsVrfName.setStatus(_A)
_CnvoVNetVrfStatsVni_Type=Unsigned32
_CnvoVNetVrfStatsVni_Object=MibTableColumn
cnvoVNetVrfStatsVni=_CnvoVNetVrfStatsVni_Object((1,3,6,1,4,1,9,9,820,1,1,6,1,2),_CnvoVNetVrfStatsVni_Type())
cnvoVNetVrfStatsVni.setMaxAccess(_G)
if mibBuilder.loadTexts:cnvoVNetVrfStatsVni.setStatus(_A)
_CnvoVNetVrfIngressPackets_Type=Counter64
_CnvoVNetVrfIngressPackets_Object=MibTableColumn
cnvoVNetVrfIngressPackets=_CnvoVNetVrfIngressPackets_Object((1,3,6,1,4,1,9,9,820,1,1,6,1,3),_CnvoVNetVrfIngressPackets_Type())
cnvoVNetVrfIngressPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:cnvoVNetVrfIngressPackets.setStatus(_A)
_CnvoVNetVrfIngressBytes_Type=Counter64
_CnvoVNetVrfIngressBytes_Object=MibTableColumn
cnvoVNetVrfIngressBytes=_CnvoVNetVrfIngressBytes_Object((1,3,6,1,4,1,9,9,820,1,1,6,1,4),_CnvoVNetVrfIngressBytes_Type())
cnvoVNetVrfIngressBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:cnvoVNetVrfIngressBytes.setStatus(_A)
_CnvoVNetVrfEgressPackets_Type=Counter64
_CnvoVNetVrfEgressPackets_Object=MibTableColumn
cnvoVNetVrfEgressPackets=_CnvoVNetVrfEgressPackets_Object((1,3,6,1,4,1,9,9,820,1,1,6,1,5),_CnvoVNetVrfEgressPackets_Type())
cnvoVNetVrfEgressPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:cnvoVNetVrfEgressPackets.setStatus(_A)
_CnvoVNetVrfEgressBytes_Type=Counter64
_CnvoVNetVrfEgressBytes_Object=MibTableColumn
cnvoVNetVrfEgressBytes=_CnvoVNetVrfEgressBytes_Object((1,3,6,1,4,1,9,9,820,1,1,6,1,6),_CnvoVNetVrfEgressBytes_Type())
cnvoVNetVrfEgressBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:cnvoVNetVrfEgressBytes.setStatus(_A)
_CnvoMIBConform_ObjectIdentity=ObjectIdentity
cnvoMIBConform=_CnvoMIBConform_ObjectIdentity((1,3,6,1,4,1,9,9,820,2))
_CnvoMIBCompliances_ObjectIdentity=ObjectIdentity
cnvoMIBCompliances=_CnvoMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,820,2,1))
_CnvoMIBGroups_ObjectIdentity=ObjectIdentity
cnvoMIBGroups=_CnvoMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,820,2,2))
cnvoNvoGroup=ObjectGroup((1,3,6,1,4,1,9,9,820,2,2,1))
cnvoNvoGroup.setObjects(*((_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V)))
if mibBuilder.loadTexts:cnvoNvoGroup.setStatus(_A)
cnvoVirtualNetworkGroup=ObjectGroup((1,3,6,1,4,1,9,9,820,2,2,2))
cnvoVirtualNetworkGroup.setObjects(*((_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e)))
if mibBuilder.loadTexts:cnvoVirtualNetworkGroup.setStatus(_A)
cnvoPeerGroup=ObjectGroup((1,3,6,1,4,1,9,9,820,2,2,3))
cnvoPeerGroup.setObjects(*((_B,_f),(_B,_g)))
if mibBuilder.loadTexts:cnvoPeerGroup.setStatus(_A)
cnvoVirtualNetworkStatsGroup=ObjectGroup((1,3,6,1,4,1,9,9,820,2,2,4))
cnvoVirtualNetworkStatsGroup.setObjects(*((_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o)))
if mibBuilder.loadTexts:cnvoVirtualNetworkStatsGroup.setStatus(_A)
cnvoNvoPerPeerOutUnicastStatsGroup=ObjectGroup((1,3,6,1,4,1,9,9,820,2,2,5))
cnvoNvoPerPeerOutUnicastStatsGroup.setObjects(*((_B,_p),(_B,_q)))
if mibBuilder.loadTexts:cnvoNvoPerPeerOutUnicastStatsGroup.setStatus(_A)
cnvoNvoPerPeerInUnicastStatsGroup=ObjectGroup((1,3,6,1,4,1,9,9,820,2,2,6))
cnvoNvoPerPeerInUnicastStatsGroup.setObjects(*((_B,_r),(_B,_s)))
if mibBuilder.loadTexts:cnvoNvoPerPeerInUnicastStatsGroup.setStatus(_A)
cnvoNvoPerPeerInMulticastStatsGroup=ObjectGroup((1,3,6,1,4,1,9,9,820,2,2,7))
cnvoNvoPerPeerInMulticastStatsGroup.setObjects(*((_B,_t),(_B,_u)))
if mibBuilder.loadTexts:cnvoNvoPerPeerInMulticastStatsGroup.setStatus(_A)
cnvoNvoPerPeerOutMulticastStatsGroup=ObjectGroup((1,3,6,1,4,1,9,9,820,2,2,8))
cnvoNvoPerPeerOutMulticastStatsGroup.setObjects(*((_B,_v),(_B,_w)))
if mibBuilder.loadTexts:cnvoNvoPerPeerOutMulticastStatsGroup.setStatus(_A)
cnvoVNetVrfStatsGroup=ObjectGroup((1,3,6,1,4,1,9,9,820,2,2,9))
cnvoVNetVrfStatsGroup.setObjects(*((_B,_x),(_B,_y),(_B,_z),(_B,_A0)))
if mibBuilder.loadTexts:cnvoVNetVrfStatsGroup.setStatus(_A)
cnvoMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,820,2,1,1))
cnvoMIBCompliance.setObjects(*((_B,_A1),(_B,_A2),(_B,_A3),(_B,_A4),(_B,_A5),(_B,_A6),(_B,_A7),(_B,_A8),(_B,_A9)))
if mibBuilder.loadTexts:cnvoMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ciscoNetworkVirtualizationOverlayMIB':ciscoNetworkVirtualizationOverlayMIB,'cnvoMIBNotifs':cnvoMIBNotifs,'cnvoMIBObjects':cnvoMIBObjects,'cnvoNvoObjects':cnvoNvoObjects,'cnvoNvoTable':cnvoNvoTable,'cnvoNvoEntry':cnvoNvoEntry,_F:cnvoNvoInstanceId,_R:cnvoNvoEncapType,_S:cnvoNvoSourceInterface,_T:cnvoNvoConfiguredVni,_U:cnvoNvoStorageType,_V:cnvoNvoRowStatus,'cnvoVNetTable':cnvoVNetTable,'cnvoVNetEntry':cnvoVNetEntry,_J:cnvoVNetLocalVNetId,_W:cnvoVNetIpMcastAddrType,_X:cnvoVNetIpMcastAddr,_Y:cnvoVNetVlan,_Z:cnvoVNetArpSuppression,_a:cnvoVNetReplication,_b:cnvoVNetHostReachability,_c:cnvoVNetVniType,_d:cnvoVNetIpVrfOrBridgeDomainName,_e:cnvoVNetRouterMacAddr,'cnvoPeerTable':cnvoPeerTable,'cnvoPeerEntry':cnvoPeerEntry,_K:cnvoPeerIpAddrType,_L:cnvoPeerIpAddr,_f:cnvoPeerUpTime,_g:cnvoPeerLearningSourceType,'cnvoVNetStatsTable':cnvoVNetStatsTable,'cnvoVNetStatsEntry':cnvoVNetStatsEntry,_h:cnvoVNetOutUnicastPackets,_i:cnvoVNetOutUnicastBytes,_j:cnvoVNetOutMulticastPackets,_k:cnvoVNetOutMulticastBytes,_l:cnvoVNetInUnicastPackets,_m:cnvoVNetInUnicastBytes,_n:cnvoVNetInMulticastPackets,_o:cnvoVNetInMulticastBytes,'cnvoNvoPeerStatsTable':cnvoNvoPeerStatsTable,'cnvoNvoPeerStatsEntry':cnvoNvoPeerStatsEntry,_p:cnvoNvoPeerOutUnicastPackets,_q:cnvoNvoPeerOutUnicastBytes,_v:cnvoNvoPeerOutMulticastPackets,_w:cnvoNvoPeerOutMulticastBytes,_r:cnvoNvoPeerInUnicastPackets,_s:cnvoNvoPeerInUnicastBytes,_t:cnvoNvoPeerInMulticastPackets,_u:cnvoNvoPeerInMulticastBytes,'cnvoVNetVrfStatsTable':cnvoVNetVrfStatsTable,'cnvoVNetVrfStatsEntry':cnvoVNetVrfStatsEntry,_P:cnvoVNetVrfStatsVrfName,_Q:cnvoVNetVrfStatsVni,_x:cnvoVNetVrfIngressPackets,_y:cnvoVNetVrfIngressBytes,_z:cnvoVNetVrfEgressPackets,_A0:cnvoVNetVrfEgressBytes,'cnvoMIBConform':cnvoMIBConform,'cnvoMIBCompliances':cnvoMIBCompliances,'cnvoMIBCompliance':cnvoMIBCompliance,'cnvoMIBGroups':cnvoMIBGroups,_A1:cnvoNvoGroup,_A2:cnvoVirtualNetworkGroup,_A3:cnvoPeerGroup,_A4:cnvoVirtualNetworkStatsGroup,_A5:cnvoNvoPerPeerOutUnicastStatsGroup,_A7:cnvoNvoPerPeerInUnicastStatsGroup,_A8:cnvoNvoPerPeerInMulticastStatsGroup,_A6:cnvoNvoPerPeerOutMulticastStatsGroup,_A9:cnvoVNetVrfStatsGroup})