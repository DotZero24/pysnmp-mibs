_S='raisecomMplsCccPwEntry'
_R='raisecomMplsLspEntry'
_Q='deprecated'
_P='raisecomMplsLdpInterfaceIndex'
_O='read-create'
_N='raisecomMplsL2vpnInterfaceIndex'
_M='raisecomMplsInterfaceIndex'
_L='ifIndex'
_K='IF-MIB'
_J='OctetString'
_I='RefreshInterval'
_H='not-accessible'
_G='RAISECOM-MPLS-MIB'
_F='Unsigned32'
_E='read-only'
_D='Integer32'
_C='TruthValue'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_J,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndexOrZero,ifIndex=mibBuilder.importSymbols(_K,'InterfaceIndexOrZero',_L)
InetAddress,InetAddressIPv4,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressIPv4','InetAddressType')
mplsXCEntry,=mibBuilder.importSymbols('MPLS-LSR-STD-MIB','mplsXCEntry')
pwEntry,=mibBuilder.importSymbols('PW-STD-MIB','pwEntry')
raisecomAgent,=mibBuilder.importSymbols('RAISECOM-BASE-MIB','raisecomAgent')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_F,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention',_C)
raisecomMpls=ModuleIdentity((1,3,6,1,4,1,8886,1,25))
class RefreshInterval(TextualConvention,Integer32):status=_A;displayHint='d';subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_RaisecomMplsLsrObjects_ObjectIdentity=ObjectIdentity
raisecomMplsLsrObjects=_RaisecomMplsLsrObjects_ObjectIdentity((1,3,6,1,4,1,8886,1,25,1))
_RaisecomMplsLsrId_Type=InetAddressIPv4
_RaisecomMplsLsrId_Object=MibScalar
raisecomMplsLsrId=_RaisecomMplsLsrId_Object((1,3,6,1,4,1,8886,1,25,1,1),_RaisecomMplsLsrId_Type())
raisecomMplsLsrId.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomMplsLsrId.setStatus(_A)
class _RaisecomMplsEnable_Type(TruthValue):defaultValue=2
_RaisecomMplsEnable_Type.__name__=_C
_RaisecomMplsEnable_Object=MibScalar
raisecomMplsEnable=_RaisecomMplsEnable_Object((1,3,6,1,4,1,8886,1,25,1,2),_RaisecomMplsEnable_Type())
raisecomMplsEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomMplsEnable.setStatus(_A)
class _RaisecomMplsLspStatisticsClear_Type(TruthValue):defaultValue=2
_RaisecomMplsLspStatisticsClear_Type.__name__=_C
_RaisecomMplsLspStatisticsClear_Object=MibScalar
raisecomMplsLspStatisticsClear=_RaisecomMplsLspStatisticsClear_Object((1,3,6,1,4,1,8886,1,25,1,3),_RaisecomMplsLspStatisticsClear_Type())
raisecomMplsLspStatisticsClear.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomMplsLspStatisticsClear.setStatus(_A)
_RaisecomMplsInterfaceTable_Object=MibTable
raisecomMplsInterfaceTable=_RaisecomMplsInterfaceTable_Object((1,3,6,1,4,1,8886,1,25,1,4))
if mibBuilder.loadTexts:raisecomMplsInterfaceTable.setStatus(_A)
_RaisecomMplsInterfaceEntry_Object=MibTableRow
raisecomMplsInterfaceEntry=_RaisecomMplsInterfaceEntry_Object((1,3,6,1,4,1,8886,1,25,1,4,1))
raisecomMplsInterfaceEntry.setIndexNames((0,_G,_M))
if mibBuilder.loadTexts:raisecomMplsInterfaceEntry.setStatus(_A)
_RaisecomMplsInterfaceIndex_Type=InterfaceIndexOrZero
_RaisecomMplsInterfaceIndex_Object=MibTableColumn
raisecomMplsInterfaceIndex=_RaisecomMplsInterfaceIndex_Object((1,3,6,1,4,1,8886,1,25,1,4,1,1),_RaisecomMplsInterfaceIndex_Type())
raisecomMplsInterfaceIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:raisecomMplsInterfaceIndex.setStatus(_A)
class _RaisecomMplsInterfaceEnable_Type(TruthValue):defaultValue=1
_RaisecomMplsInterfaceEnable_Type.__name__=_C
_RaisecomMplsInterfaceEnable_Object=MibTableColumn
raisecomMplsInterfaceEnable=_RaisecomMplsInterfaceEnable_Object((1,3,6,1,4,1,8886,1,25,1,4,1,2),_RaisecomMplsInterfaceEnable_Type())
raisecomMplsInterfaceEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomMplsInterfaceEnable.setStatus(_A)
_RaisecomMplsLspTable_Object=MibTable
raisecomMplsLspTable=_RaisecomMplsLspTable_Object((1,3,6,1,4,1,8886,1,25,1,5))
if mibBuilder.loadTexts:raisecomMplsLspTable.setStatus(_A)
_RaisecomMplsLspEntry_Object=MibTableRow
raisecomMplsLspEntry=_RaisecomMplsLspEntry_Object((1,3,6,1,4,1,8886,1,25,1,5,1))
if mibBuilder.loadTexts:raisecomMplsLspEntry.setStatus(_A)
class _RaisecomMplsLspName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_RaisecomMplsLspName_Type.__name__=_J
_RaisecomMplsLspName_Object=MibTableColumn
raisecomMplsLspName=_RaisecomMplsLspName_Object((1,3,6,1,4,1,8886,1,25,1,5,1,1),_RaisecomMplsLspName_Type())
raisecomMplsLspName.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomMplsLspName.setStatus(_A)
_RaisecomMplsLspStatisticsObjects_ObjectIdentity=ObjectIdentity
raisecomMplsLspStatisticsObjects=_RaisecomMplsLspStatisticsObjects_ObjectIdentity((1,3,6,1,4,1,8886,1,25,1,6))
_RaisecomMplsLspConfigured_Type=Unsigned32
_RaisecomMplsLspConfigured_Object=MibScalar
raisecomMplsLspConfigured=_RaisecomMplsLspConfigured_Object((1,3,6,1,4,1,8886,1,25,1,6,1),_RaisecomMplsLspConfigured_Type())
raisecomMplsLspConfigured.setMaxAccess(_E)
if mibBuilder.loadTexts:raisecomMplsLspConfigured.setStatus(_A)
_RaisecomMplsLspActicve_Type=Unsigned32
_RaisecomMplsLspActicve_Object=MibScalar
raisecomMplsLspActicve=_RaisecomMplsLspActicve_Object((1,3,6,1,4,1,8886,1,25,1,6,2),_RaisecomMplsLspActicve_Type())
raisecomMplsLspActicve.setMaxAccess(_E)
if mibBuilder.loadTexts:raisecomMplsLspActicve.setStatus(_A)
_RaisecomMplsLspInActicve_Type=Unsigned32
_RaisecomMplsLspInActicve_Object=MibScalar
raisecomMplsLspInActicve=_RaisecomMplsLspInActicve_Object((1,3,6,1,4,1,8886,1,25,1,6,3),_RaisecomMplsLspInActicve_Type())
raisecomMplsLspInActicve.setMaxAccess(_E)
if mibBuilder.loadTexts:raisecomMplsLspInActicve.setStatus(_A)
_RaisecomMplsLspIngress_Type=Unsigned32
_RaisecomMplsLspIngress_Object=MibScalar
raisecomMplsLspIngress=_RaisecomMplsLspIngress_Object((1,3,6,1,4,1,8886,1,25,1,6,4),_RaisecomMplsLspIngress_Type())
raisecomMplsLspIngress.setMaxAccess(_E)
if mibBuilder.loadTexts:raisecomMplsLspIngress.setStatus(_A)
_RaisecomMplsLspTransit_Type=Unsigned32
_RaisecomMplsLspTransit_Object=MibScalar
raisecomMplsLspTransit=_RaisecomMplsLspTransit_Object((1,3,6,1,4,1,8886,1,25,1,6,5),_RaisecomMplsLspTransit_Type())
raisecomMplsLspTransit.setMaxAccess(_E)
if mibBuilder.loadTexts:raisecomMplsLspTransit.setStatus(_A)
_RaisecomMplsLspEgress_Type=Unsigned32
_RaisecomMplsLspEgress_Object=MibScalar
raisecomMplsLspEgress=_RaisecomMplsLspEgress_Object((1,3,6,1,4,1,8886,1,25,1,6,6),_RaisecomMplsLspEgress_Type())
raisecomMplsLspEgress.setMaxAccess(_E)
if mibBuilder.loadTexts:raisecomMplsLspEgress.setStatus(_A)
_RaisecomMplsLspStatic_Type=Unsigned32
_RaisecomMplsLspStatic_Object=MibScalar
raisecomMplsLspStatic=_RaisecomMplsLspStatic_Object((1,3,6,1,4,1,8886,1,25,1,6,7),_RaisecomMplsLspStatic_Type())
raisecomMplsLspStatic.setMaxAccess(_E)
if mibBuilder.loadTexts:raisecomMplsLspStatic.setStatus(_A)
_RaisecomMplsLspLdp_Type=Unsigned32
_RaisecomMplsLspLdp_Object=MibScalar
raisecomMplsLspLdp=_RaisecomMplsLspLdp_Object((1,3,6,1,4,1,8886,1,25,1,6,8),_RaisecomMplsLspLdp_Type())
raisecomMplsLspLdp.setMaxAccess(_E)
if mibBuilder.loadTexts:raisecomMplsLspLdp.setStatus(_A)
_RaisecomMplsLspRsvpTe_Type=Unsigned32
_RaisecomMplsLspRsvpTe_Object=MibScalar
raisecomMplsLspRsvpTe=_RaisecomMplsLspRsvpTe_Object((1,3,6,1,4,1,8886,1,25,1,6,9),_RaisecomMplsLspRsvpTe_Type())
raisecomMplsLspRsvpTe.setMaxAccess(_E)
if mibBuilder.loadTexts:raisecomMplsLspRsvpTe.setStatus(_A)
class _RaisecomMplsTunnelReroutedNotifEnable_Type(TruthValue):defaultValue=2
_RaisecomMplsTunnelReroutedNotifEnable_Type.__name__=_C
_RaisecomMplsTunnelReroutedNotifEnable_Object=MibScalar
raisecomMplsTunnelReroutedNotifEnable=_RaisecomMplsTunnelReroutedNotifEnable_Object((1,3,6,1,4,1,8886,1,25,1,7),_RaisecomMplsTunnelReroutedNotifEnable_Type())
raisecomMplsTunnelReroutedNotifEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomMplsTunnelReroutedNotifEnable.setStatus(_A)
class _RaisecomMplsTunnelReoptimizedNotifEnable_Type(TruthValue):defaultValue=2
_RaisecomMplsTunnelReoptimizedNotifEnable_Type.__name__=_C
_RaisecomMplsTunnelReoptimizedNotifEnable_Object=MibScalar
raisecomMplsTunnelReoptimizedNotifEnable=_RaisecomMplsTunnelReoptimizedNotifEnable_Object((1,3,6,1,4,1,8886,1,25,1,8),_RaisecomMplsTunnelReoptimizedNotifEnable_Type())
raisecomMplsTunnelReoptimizedNotifEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomMplsTunnelReoptimizedNotifEnable.setStatus(_A)
class _RaisecomMplsTtlPublicPropagate_Type(TruthValue):defaultValue=1
_RaisecomMplsTtlPublicPropagate_Type.__name__=_C
_RaisecomMplsTtlPublicPropagate_Object=MibScalar
raisecomMplsTtlPublicPropagate=_RaisecomMplsTtlPublicPropagate_Object((1,3,6,1,4,1,8886,1,25,1,9),_RaisecomMplsTtlPublicPropagate_Type())
raisecomMplsTtlPublicPropagate.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomMplsTtlPublicPropagate.setStatus(_A)
class _RaisecomMplsTtlVpnPropagate_Type(TruthValue):defaultValue=2
_RaisecomMplsTtlVpnPropagate_Type.__name__=_C
_RaisecomMplsTtlVpnPropagate_Object=MibScalar
raisecomMplsTtlVpnPropagate=_RaisecomMplsTtlVpnPropagate_Object((1,3,6,1,4,1,8886,1,25,1,10),_RaisecomMplsTtlVpnPropagate_Type())
raisecomMplsTtlVpnPropagate.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomMplsTtlVpnPropagate.setStatus(_A)
_RaisecomMplsVpnObjects_ObjectIdentity=ObjectIdentity
raisecomMplsVpnObjects=_RaisecomMplsVpnObjects_ObjectIdentity((1,3,6,1,4,1,8886,1,25,2))
_RaisecomMplsL2VpnObjects_ObjectIdentity=ObjectIdentity
raisecomMplsL2VpnObjects=_RaisecomMplsL2VpnObjects_ObjectIdentity((1,3,6,1,4,1,8886,1,25,2,1))
class _RaisecomMplsL2vpnEnable_Type(TruthValue):defaultValue=2
_RaisecomMplsL2vpnEnable_Type.__name__=_C
_RaisecomMplsL2vpnEnable_Object=MibScalar
raisecomMplsL2vpnEnable=_RaisecomMplsL2vpnEnable_Object((1,3,6,1,4,1,8886,1,25,2,1,1),_RaisecomMplsL2vpnEnable_Type())
raisecomMplsL2vpnEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomMplsL2vpnEnable.setStatus(_A)
class _RaisecomMplsL2vpnMartiniEnable_Type(TruthValue):defaultValue=2
_RaisecomMplsL2vpnMartiniEnable_Type.__name__=_C
_RaisecomMplsL2vpnMartiniEnable_Object=MibScalar
raisecomMplsL2vpnMartiniEnable=_RaisecomMplsL2vpnMartiniEnable_Object((1,3,6,1,4,1,8886,1,25,2,1,2),_RaisecomMplsL2vpnMartiniEnable_Type())
raisecomMplsL2vpnMartiniEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomMplsL2vpnMartiniEnable.setStatus(_A)
_RaisecomMplsL2vpnInterfaceTable_Object=MibTable
raisecomMplsL2vpnInterfaceTable=_RaisecomMplsL2vpnInterfaceTable_Object((1,3,6,1,4,1,8886,1,25,2,1,3))
if mibBuilder.loadTexts:raisecomMplsL2vpnInterfaceTable.setStatus(_A)
_RaisecomMplsL2vpnInterfaceEntry_Object=MibTableRow
raisecomMplsL2vpnInterfaceEntry=_RaisecomMplsL2vpnInterfaceEntry_Object((1,3,6,1,4,1,8886,1,25,2,1,3,1))
raisecomMplsL2vpnInterfaceEntry.setIndexNames((0,_G,_N))
if mibBuilder.loadTexts:raisecomMplsL2vpnInterfaceEntry.setStatus(_A)
_RaisecomMplsL2vpnInterfaceIndex_Type=InterfaceIndexOrZero
_RaisecomMplsL2vpnInterfaceIndex_Object=MibTableColumn
raisecomMplsL2vpnInterfaceIndex=_RaisecomMplsL2vpnInterfaceIndex_Object((1,3,6,1,4,1,8886,1,25,2,1,3,1,1),_RaisecomMplsL2vpnInterfaceIndex_Type())
raisecomMplsL2vpnInterfaceIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:raisecomMplsL2vpnInterfaceIndex.setStatus(_A)
class _RaisecomMplsL2vpnInterfaceEnable_Type(TruthValue):defaultValue=1
_RaisecomMplsL2vpnInterfaceEnable_Type.__name__=_C
_RaisecomMplsL2vpnInterfaceEnable_Object=MibTableColumn
raisecomMplsL2vpnInterfaceEnable=_RaisecomMplsL2vpnInterfaceEnable_Object((1,3,6,1,4,1,8886,1,25,2,1,3,1,2),_RaisecomMplsL2vpnInterfaceEnable_Type())
raisecomMplsL2vpnInterfaceEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomMplsL2vpnInterfaceEnable.setStatus(_A)
_RaisecomMplsCccPwTable_Object=MibTable
raisecomMplsCccPwTable=_RaisecomMplsCccPwTable_Object((1,3,6,1,4,1,8886,1,25,2,1,4))
if mibBuilder.loadTexts:raisecomMplsCccPwTable.setStatus(_A)
_RaisecomMplsCccPwEntry_Object=MibTableRow
raisecomMplsCccPwEntry=_RaisecomMplsCccPwEntry_Object((1,3,6,1,4,1,8886,1,25,2,1,4,1))
if mibBuilder.loadTexts:raisecomMplsCccPwEntry.setStatus(_A)
_RaisecomMplsCccNexthopType_Type=InetAddressType
_RaisecomMplsCccNexthopType_Object=MibTableColumn
raisecomMplsCccNexthopType=_RaisecomMplsCccNexthopType_Object((1,3,6,1,4,1,8886,1,25,2,1,4,1,1),_RaisecomMplsCccNexthopType_Type())
raisecomMplsCccNexthopType.setMaxAccess(_O)
if mibBuilder.loadTexts:raisecomMplsCccNexthopType.setStatus(_A)
_RaisecomMplsCccNexthop_Type=InetAddress
_RaisecomMplsCccNexthop_Object=MibTableColumn
raisecomMplsCccNexthop=_RaisecomMplsCccNexthop_Object((1,3,6,1,4,1,8886,1,25,2,1,4,1,2),_RaisecomMplsCccNexthop_Type())
raisecomMplsCccNexthop.setMaxAccess(_O)
if mibBuilder.loadTexts:raisecomMplsCccNexthop.setStatus(_A)
_RaisecomMplsLdpObjects_ObjectIdentity=ObjectIdentity
raisecomMplsLdpObjects=_RaisecomMplsLdpObjects_ObjectIdentity((1,3,6,1,4,1,8886,1,25,3))
class _RaisecomMplsLdpEnable_Type(TruthValue):defaultValue=2
_RaisecomMplsLdpEnable_Type.__name__=_C
_RaisecomMplsLdpEnable_Object=MibScalar
raisecomMplsLdpEnable=_RaisecomMplsLdpEnable_Object((1,3,6,1,4,1,8886,1,25,3,1),_RaisecomMplsLdpEnable_Type())
raisecomMplsLdpEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomMplsLdpEnable.setStatus(_A)
_RaisecomMplsLdpInterfaceTable_Object=MibTable
raisecomMplsLdpInterfaceTable=_RaisecomMplsLdpInterfaceTable_Object((1,3,6,1,4,1,8886,1,25,3,2))
if mibBuilder.loadTexts:raisecomMplsLdpInterfaceTable.setStatus(_A)
_RaisecomMplsLdpInterfaceEntry_Object=MibTableRow
raisecomMplsLdpInterfaceEntry=_RaisecomMplsLdpInterfaceEntry_Object((1,3,6,1,4,1,8886,1,25,3,2,1))
raisecomMplsLdpInterfaceEntry.setIndexNames((0,_G,_P))
if mibBuilder.loadTexts:raisecomMplsLdpInterfaceEntry.setStatus(_A)
_RaisecomMplsLdpInterfaceIndex_Type=InterfaceIndexOrZero
_RaisecomMplsLdpInterfaceIndex_Object=MibTableColumn
raisecomMplsLdpInterfaceIndex=_RaisecomMplsLdpInterfaceIndex_Object((1,3,6,1,4,1,8886,1,25,3,2,1,1),_RaisecomMplsLdpInterfaceIndex_Type())
raisecomMplsLdpInterfaceIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:raisecomMplsLdpInterfaceIndex.setStatus(_A)
class _RaisecomMplsLdpInterfaceEnable_Type(TruthValue):defaultValue=1
_RaisecomMplsLdpInterfaceEnable_Type.__name__=_C
_RaisecomMplsLdpInterfaceEnable_Object=MibTableColumn
raisecomMplsLdpInterfaceEnable=_RaisecomMplsLdpInterfaceEnable_Object((1,3,6,1,4,1,8886,1,25,3,2,1,2),_RaisecomMplsLdpInterfaceEnable_Type())
raisecomMplsLdpInterfaceEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomMplsLdpInterfaceEnable.setStatus(_A)
_RaisecomMplsLdpInterfaceLAM_Type=Integer32
_RaisecomMplsLdpInterfaceLAM_Object=MibTableColumn
raisecomMplsLdpInterfaceLAM=_RaisecomMplsLdpInterfaceLAM_Object((1,3,6,1,4,1,8886,1,25,3,2,1,3),_RaisecomMplsLdpInterfaceLAM_Type())
raisecomMplsLdpInterfaceLAM.setMaxAccess(_E)
if mibBuilder.loadTexts:raisecomMplsLdpInterfaceLAM.setStatus(_A)
_RaisecomMplsLdpInterfaceTransportAddress_Type=InetAddress
_RaisecomMplsLdpInterfaceTransportAddress_Object=MibTableColumn
raisecomMplsLdpInterfaceTransportAddress=_RaisecomMplsLdpInterfaceTransportAddress_Object((1,3,6,1,4,1,8886,1,25,3,2,1,4),_RaisecomMplsLdpInterfaceTransportAddress_Type())
raisecomMplsLdpInterfaceTransportAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:raisecomMplsLdpInterfaceTransportAddress.setStatus(_A)
_RaisecomMplsLdpInterfaceLdpID_Type=OctetString
_RaisecomMplsLdpInterfaceLdpID_Object=MibTableColumn
raisecomMplsLdpInterfaceLdpID=_RaisecomMplsLdpInterfaceLdpID_Object((1,3,6,1,4,1,8886,1,25,3,2,1,5),_RaisecomMplsLdpInterfaceLdpID_Type())
raisecomMplsLdpInterfaceLdpID.setMaxAccess(_E)
if mibBuilder.loadTexts:raisecomMplsLdpInterfaceLdpID.setStatus(_A)
class _RaisecomMplsLdpInterfaceMTU_Type(Integer32):defaultValue=1500
_RaisecomMplsLdpInterfaceMTU_Type.__name__=_D
_RaisecomMplsLdpInterfaceMTU_Object=MibTableColumn
raisecomMplsLdpInterfaceMTU=_RaisecomMplsLdpInterfaceMTU_Object((1,3,6,1,4,1,8886,1,25,3,2,1,6),_RaisecomMplsLdpInterfaceMTU_Type())
raisecomMplsLdpInterfaceMTU.setMaxAccess(_E)
if mibBuilder.loadTexts:raisecomMplsLdpInterfaceMTU.setStatus(_A)
class _RaisecomMplsLdpInterfaceKeepAliveHoldTimer_Type(Integer32):defaultValue=40
_RaisecomMplsLdpInterfaceKeepAliveHoldTimer_Type.__name__=_D
_RaisecomMplsLdpInterfaceKeepAliveHoldTimer_Object=MibTableColumn
raisecomMplsLdpInterfaceKeepAliveHoldTimer=_RaisecomMplsLdpInterfaceKeepAliveHoldTimer_Object((1,3,6,1,4,1,8886,1,25,3,2,1,7),_RaisecomMplsLdpInterfaceKeepAliveHoldTimer_Type())
raisecomMplsLdpInterfaceKeepAliveHoldTimer.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomMplsLdpInterfaceKeepAliveHoldTimer.setStatus(_A)
class _RaisecomMplsLdpInterfaceHelloHoldTimer_Type(Integer32):defaultValue=0
_RaisecomMplsLdpInterfaceHelloHoldTimer_Type.__name__=_D
_RaisecomMplsLdpInterfaceHelloHoldTimer_Object=MibTableColumn
raisecomMplsLdpInterfaceHelloHoldTimer=_RaisecomMplsLdpInterfaceHelloHoldTimer_Object((1,3,6,1,4,1,8886,1,25,3,2,1,8),_RaisecomMplsLdpInterfaceHelloHoldTimer_Type())
raisecomMplsLdpInterfaceHelloHoldTimer.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomMplsLdpInterfaceHelloHoldTimer.setStatus(_A)
class _RaisecomMplsLdpSessionStatusTrapEnable_Type(TruthValue):defaultValue=2
_RaisecomMplsLdpSessionStatusTrapEnable_Type.__name__=_C
_RaisecomMplsLdpSessionStatusTrapEnable_Object=MibScalar
raisecomMplsLdpSessionStatusTrapEnable=_RaisecomMplsLdpSessionStatusTrapEnable_Object((1,3,6,1,4,1,8886,1,25,3,3),_RaisecomMplsLdpSessionStatusTrapEnable_Type())
raisecomMplsLdpSessionStatusTrapEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomMplsLdpSessionStatusTrapEnable.setStatus(_A)
class _RaisecomMplsLdpPathVecLimitTrapEnable_Type(TruthValue):defaultValue=2
_RaisecomMplsLdpPathVecLimitTrapEnable_Type.__name__=_C
_RaisecomMplsLdpPathVecLimitTrapEnable_Object=MibScalar
raisecomMplsLdpPathVecLimitTrapEnable=_RaisecomMplsLdpPathVecLimitTrapEnable_Object((1,3,6,1,4,1,8886,1,25,3,4),_RaisecomMplsLdpPathVecLimitTrapEnable_Type())
raisecomMplsLdpPathVecLimitTrapEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomMplsLdpPathVecLimitTrapEnable.setStatus(_A)
class _RaisecomMplsLdpSessionThreshTrapEnable_Type(TruthValue):defaultValue=2
_RaisecomMplsLdpSessionThreshTrapEnable_Type.__name__=_C
_RaisecomMplsLdpSessionThreshTrapEnable_Object=MibScalar
raisecomMplsLdpSessionThreshTrapEnable=_RaisecomMplsLdpSessionThreshTrapEnable_Object((1,3,6,1,4,1,8886,1,25,3,5),_RaisecomMplsLdpSessionThreshTrapEnable_Type())
raisecomMplsLdpSessionThreshTrapEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomMplsLdpSessionThreshTrapEnable.setStatus(_A)
_RaisecomMplsRsvpTEObjects_ObjectIdentity=ObjectIdentity
raisecomMplsRsvpTEObjects=_RaisecomMplsRsvpTEObjects_ObjectIdentity((1,3,6,1,4,1,8886,1,25,4))
class _RaisecomMplsRsvpTEEnabled_Type(TruthValue):defaultValue=2
_RaisecomMplsRsvpTEEnabled_Type.__name__=_C
_RaisecomMplsRsvpTEEnabled_Object=MibScalar
raisecomMplsRsvpTEEnabled=_RaisecomMplsRsvpTEEnabled_Object((1,3,6,1,4,1,8886,1,25,4,1),_RaisecomMplsRsvpTEEnabled_Type())
raisecomMplsRsvpTEEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomMplsRsvpTEEnabled.setStatus(_A)
class _RaisecomMplsRsvpTERefreshInterval_Type(RefreshInterval):defaultValue=3000
_RaisecomMplsRsvpTERefreshInterval_Type.__name__=_I
_RaisecomMplsRsvpTERefreshInterval_Object=MibScalar
raisecomMplsRsvpTERefreshInterval=_RaisecomMplsRsvpTERefreshInterval_Object((1,3,6,1,4,1,8886,1,25,4,2),_RaisecomMplsRsvpTERefreshInterval_Type())
raisecomMplsRsvpTERefreshInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomMplsRsvpTERefreshInterval.setStatus(_A)
class _RaisecomMplsRsvpTERefreshMultiple_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65536))
_RaisecomMplsRsvpTERefreshMultiple_Type.__name__=_D
_RaisecomMplsRsvpTERefreshMultiple_Object=MibScalar
raisecomMplsRsvpTERefreshMultiple=_RaisecomMplsRsvpTERefreshMultiple_Object((1,3,6,1,4,1,8886,1,25,4,3),_RaisecomMplsRsvpTERefreshMultiple_Type())
raisecomMplsRsvpTERefreshMultiple.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomMplsRsvpTERefreshMultiple.setStatus(_A)
class _RaisecomMplsRsvpTERefreshBlockadeMultiple_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_RaisecomMplsRsvpTERefreshBlockadeMultiple_Type.__name__=_D
_RaisecomMplsRsvpTERefreshBlockadeMultiple_Object=MibScalar
raisecomMplsRsvpTERefreshBlockadeMultiple=_RaisecomMplsRsvpTERefreshBlockadeMultiple_Object((1,3,6,1,4,1,8886,1,25,4,4),_RaisecomMplsRsvpTERefreshBlockadeMultiple_Type())
raisecomMplsRsvpTERefreshBlockadeMultiple.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomMplsRsvpTERefreshBlockadeMultiple.setStatus(_A)
class _RaisecomMplsRsvpTELSPSetupPriority_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_RaisecomMplsRsvpTELSPSetupPriority_Type.__name__=_D
_RaisecomMplsRsvpTELSPSetupPriority_Object=MibScalar
raisecomMplsRsvpTELSPSetupPriority=_RaisecomMplsRsvpTELSPSetupPriority_Object((1,3,6,1,4,1,8886,1,25,4,5),_RaisecomMplsRsvpTELSPSetupPriority_Type())
raisecomMplsRsvpTELSPSetupPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomMplsRsvpTELSPSetupPriority.setStatus(_Q)
class _RaisecomMplsRsvpTELSPHoldingPriority_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_RaisecomMplsRsvpTELSPHoldingPriority_Type.__name__=_D
_RaisecomMplsRsvpTELSPHoldingPriority_Object=MibScalar
raisecomMplsRsvpTELSPHoldingPriority=_RaisecomMplsRsvpTELSPHoldingPriority_Object((1,3,6,1,4,1,8886,1,25,4,6),_RaisecomMplsRsvpTELSPHoldingPriority_Type())
raisecomMplsRsvpTELSPHoldingPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomMplsRsvpTELSPHoldingPriority.setStatus(_Q)
class _RaisecomMplsRsvpTEInitPathRRInterval_Type(Integer32):defaultValue=2000
_RaisecomMplsRsvpTEInitPathRRInterval_Type.__name__=_D
_RaisecomMplsRsvpTEInitPathRRInterval_Object=MibScalar
raisecomMplsRsvpTEInitPathRRInterval=_RaisecomMplsRsvpTEInitPathRRInterval_Object((1,3,6,1,4,1,8886,1,25,4,7),_RaisecomMplsRsvpTEInitPathRRInterval_Type())
raisecomMplsRsvpTEInitPathRRInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomMplsRsvpTEInitPathRRInterval.setStatus(_A)
class _RaisecomMplsRsvpTEInitPathRRDecay_Type(Integer32):defaultValue=100
_RaisecomMplsRsvpTEInitPathRRDecay_Type.__name__=_D
_RaisecomMplsRsvpTEInitPathRRDecay_Object=MibScalar
raisecomMplsRsvpTEInitPathRRDecay=_RaisecomMplsRsvpTEInitPathRRDecay_Object((1,3,6,1,4,1,8886,1,25,4,8),_RaisecomMplsRsvpTEInitPathRRDecay_Type())
raisecomMplsRsvpTEInitPathRRDecay.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomMplsRsvpTEInitPathRRDecay.setStatus(_A)
class _RaisecomMplsRsvpTEInitPathRRLimit_Type(Integer32):defaultValue=2
_RaisecomMplsRsvpTEInitPathRRLimit_Type.__name__=_D
_RaisecomMplsRsvpTEInitPathRRLimit_Object=MibScalar
raisecomMplsRsvpTEInitPathRRLimit=_RaisecomMplsRsvpTEInitPathRRLimit_Object((1,3,6,1,4,1,8886,1,25,4,9),_RaisecomMplsRsvpTEInitPathRRLimit_Type())
raisecomMplsRsvpTEInitPathRRLimit.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomMplsRsvpTEInitPathRRLimit.setStatus(_A)
_RaisecomMplsRsvpTEInterfaceTable_Object=MibTable
raisecomMplsRsvpTEInterfaceTable=_RaisecomMplsRsvpTEInterfaceTable_Object((1,3,6,1,4,1,8886,1,25,4,10))
if mibBuilder.loadTexts:raisecomMplsRsvpTEInterfaceTable.setStatus(_A)
_RaisecomMplsRsvpTEInterfaceEntry_Object=MibTableRow
raisecomMplsRsvpTEInterfaceEntry=_RaisecomMplsRsvpTEInterfaceEntry_Object((1,3,6,1,4,1,8886,1,25,4,10,1))
raisecomMplsRsvpTEInterfaceEntry.setIndexNames((0,_K,_L))
if mibBuilder.loadTexts:raisecomMplsRsvpTEInterfaceEntry.setStatus(_A)
class _RaisecomMplsRsvpTEIfRefreshInterval_Type(RefreshInterval):defaultValue=0
_RaisecomMplsRsvpTEIfRefreshInterval_Type.__name__=_I
_RaisecomMplsRsvpTEIfRefreshInterval_Object=MibTableColumn
raisecomMplsRsvpTEIfRefreshInterval=_RaisecomMplsRsvpTEIfRefreshInterval_Object((1,3,6,1,4,1,8886,1,25,4,10,1,1),_RaisecomMplsRsvpTEIfRefreshInterval_Type())
raisecomMplsRsvpTEIfRefreshInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomMplsRsvpTEIfRefreshInterval.setStatus(_A)
if mibBuilder.loadTexts:raisecomMplsRsvpTEIfRefreshInterval.setUnits('milliseconds')
class _RaisecomMplsRsvpTEIfRefreshMultiple_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_RaisecomMplsRsvpTEIfRefreshMultiple_Type.__name__=_D
_RaisecomMplsRsvpTEIfRefreshMultiple_Object=MibTableColumn
raisecomMplsRsvpTEIfRefreshMultiple=_RaisecomMplsRsvpTEIfRefreshMultiple_Object((1,3,6,1,4,1,8886,1,25,4,10,1,2),_RaisecomMplsRsvpTEIfRefreshMultiple_Type())
raisecomMplsRsvpTEIfRefreshMultiple.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomMplsRsvpTEIfRefreshMultiple.setStatus(_A)
class _RaisecomMplsRsvpTEIfBlockadeMultiple_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_RaisecomMplsRsvpTEIfBlockadeMultiple_Type.__name__=_D
_RaisecomMplsRsvpTEIfBlockadeMultiple_Object=MibTableColumn
raisecomMplsRsvpTEIfBlockadeMultiple=_RaisecomMplsRsvpTEIfBlockadeMultiple_Object((1,3,6,1,4,1,8886,1,25,4,10,1,3),_RaisecomMplsRsvpTEIfBlockadeMultiple_Type())
raisecomMplsRsvpTEIfBlockadeMultiple.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomMplsRsvpTEIfBlockadeMultiple.setStatus(_A)
class _RaisecomMplsRsvpTEIfRRInterval_Type(Unsigned32):defaultValue=500
_RaisecomMplsRsvpTEIfRRInterval_Type.__name__=_F
_RaisecomMplsRsvpTEIfRRInterval_Object=MibTableColumn
raisecomMplsRsvpTEIfRRInterval=_RaisecomMplsRsvpTEIfRRInterval_Object((1,3,6,1,4,1,8886,1,25,4,10,1,4),_RaisecomMplsRsvpTEIfRRInterval_Type())
raisecomMplsRsvpTEIfRRInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomMplsRsvpTEIfRRInterval.setStatus(_A)
class _RaisecomMplsRsvpTEIfRRDecay_Type(Integer32):defaultValue=100
_RaisecomMplsRsvpTEIfRRDecay_Type.__name__=_D
_RaisecomMplsRsvpTEIfRRDecay_Object=MibTableColumn
raisecomMplsRsvpTEIfRRDecay=_RaisecomMplsRsvpTEIfRRDecay_Object((1,3,6,1,4,1,8886,1,25,4,10,1,5),_RaisecomMplsRsvpTEIfRRDecay_Type())
raisecomMplsRsvpTEIfRRDecay.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomMplsRsvpTEIfRRDecay.setStatus(_A)
class _RaisecomMplsRsvpTEIfRRLimit_Type(Unsigned32):defaultValue=2
_RaisecomMplsRsvpTEIfRRLimit_Type.__name__=_F
_RaisecomMplsRsvpTEIfRRLimit_Object=MibTableColumn
raisecomMplsRsvpTEIfRRLimit=_RaisecomMplsRsvpTEIfRRLimit_Object((1,3,6,1,4,1,8886,1,25,4,10,1,6),_RaisecomMplsRsvpTEIfRRLimit_Type())
raisecomMplsRsvpTEIfRRLimit.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomMplsRsvpTEIfRRLimit.setStatus(_A)
class _RaisecomMplsRsvpTEIfHelloPeriod_Type(Unsigned32):defaultValue=0
_RaisecomMplsRsvpTEIfHelloPeriod_Type.__name__=_F
_RaisecomMplsRsvpTEIfHelloPeriod_Object=MibTableColumn
raisecomMplsRsvpTEIfHelloPeriod=_RaisecomMplsRsvpTEIfHelloPeriod_Object((1,3,6,1,4,1,8886,1,25,4,10,1,7),_RaisecomMplsRsvpTEIfHelloPeriod_Type())
raisecomMplsRsvpTEIfHelloPeriod.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomMplsRsvpTEIfHelloPeriod.setStatus(_A)
class _RaisecomMplsRsvpTEIfHelloHoldPeriod_Type(Unsigned32):defaultValue=3
_RaisecomMplsRsvpTEIfHelloHoldPeriod_Type.__name__=_F
_RaisecomMplsRsvpTEIfHelloHoldPeriod_Object=MibTableColumn
raisecomMplsRsvpTEIfHelloHoldPeriod=_RaisecomMplsRsvpTEIfHelloHoldPeriod_Object((1,3,6,1,4,1,8886,1,25,4,10,1,8),_RaisecomMplsRsvpTEIfHelloHoldPeriod_Type())
raisecomMplsRsvpTEIfHelloHoldPeriod.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomMplsRsvpTEIfHelloHoldPeriod.setStatus(_A)
class _RaisecomMplsRsvpTEIfHelloDecay_Type(Unsigned32):defaultValue=0
_RaisecomMplsRsvpTEIfHelloDecay_Type.__name__=_F
_RaisecomMplsRsvpTEIfHelloDecay_Object=MibTableColumn
raisecomMplsRsvpTEIfHelloDecay=_RaisecomMplsRsvpTEIfHelloDecay_Object((1,3,6,1,4,1,8886,1,25,4,10,1,9),_RaisecomMplsRsvpTEIfHelloDecay_Type())
raisecomMplsRsvpTEIfHelloDecay.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomMplsRsvpTEIfHelloDecay.setStatus(_A)
_RaisecomMplsRsvpTEIfHelloPersist_Type=Unsigned32
_RaisecomMplsRsvpTEIfHelloPersist_Object=MibTableColumn
raisecomMplsRsvpTEIfHelloPersist=_RaisecomMplsRsvpTEIfHelloPersist_Object((1,3,6,1,4,1,8886,1,25,4,10,1,10),_RaisecomMplsRsvpTEIfHelloPersist_Type())
raisecomMplsRsvpTEIfHelloPersist.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomMplsRsvpTEIfHelloPersist.setStatus(_A)
_RaisecomMplsRsvpTEIfEnabled_Type=TruthValue
_RaisecomMplsRsvpTEIfEnabled_Object=MibTableColumn
raisecomMplsRsvpTEIfEnabled=_RaisecomMplsRsvpTEIfEnabled_Object((1,3,6,1,4,1,8886,1,25,4,10,1,11),_RaisecomMplsRsvpTEIfEnabled_Type())
raisecomMplsRsvpTEIfEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomMplsRsvpTEIfEnabled.setStatus(_A)
_RaisecomMplsRsvpTEIfStatus_Type=RowStatus
_RaisecomMplsRsvpTEIfStatus_Object=MibTableColumn
raisecomMplsRsvpTEIfStatus=_RaisecomMplsRsvpTEIfStatus_Object((1,3,6,1,4,1,8886,1,25,4,10,1,12),_RaisecomMplsRsvpTEIfStatus_Type())
raisecomMplsRsvpTEIfStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:raisecomMplsRsvpTEIfStatus.setStatus(_A)
mplsXCEntry.registerAugmentions((_G,_R))
raisecomMplsLspEntry.setIndexNames(*mplsXCEntry.getIndexNames())
pwEntry.registerAugmentions((_G,_S))
raisecomMplsCccPwEntry.setIndexNames(*pwEntry.getIndexNames())
mibBuilder.exportSymbols(_G,**{_I:RefreshInterval,'raisecomMpls':raisecomMpls,'raisecomMplsLsrObjects':raisecomMplsLsrObjects,'raisecomMplsLsrId':raisecomMplsLsrId,'raisecomMplsEnable':raisecomMplsEnable,'raisecomMplsLspStatisticsClear':raisecomMplsLspStatisticsClear,'raisecomMplsInterfaceTable':raisecomMplsInterfaceTable,'raisecomMplsInterfaceEntry':raisecomMplsInterfaceEntry,_M:raisecomMplsInterfaceIndex,'raisecomMplsInterfaceEnable':raisecomMplsInterfaceEnable,'raisecomMplsLspTable':raisecomMplsLspTable,_R:raisecomMplsLspEntry,'raisecomMplsLspName':raisecomMplsLspName,'raisecomMplsLspStatisticsObjects':raisecomMplsLspStatisticsObjects,'raisecomMplsLspConfigured':raisecomMplsLspConfigured,'raisecomMplsLspActicve':raisecomMplsLspActicve,'raisecomMplsLspInActicve':raisecomMplsLspInActicve,'raisecomMplsLspIngress':raisecomMplsLspIngress,'raisecomMplsLspTransit':raisecomMplsLspTransit,'raisecomMplsLspEgress':raisecomMplsLspEgress,'raisecomMplsLspStatic':raisecomMplsLspStatic,'raisecomMplsLspLdp':raisecomMplsLspLdp,'raisecomMplsLspRsvpTe':raisecomMplsLspRsvpTe,'raisecomMplsTunnelReroutedNotifEnable':raisecomMplsTunnelReroutedNotifEnable,'raisecomMplsTunnelReoptimizedNotifEnable':raisecomMplsTunnelReoptimizedNotifEnable,'raisecomMplsTtlPublicPropagate':raisecomMplsTtlPublicPropagate,'raisecomMplsTtlVpnPropagate':raisecomMplsTtlVpnPropagate,'raisecomMplsVpnObjects':raisecomMplsVpnObjects,'raisecomMplsL2VpnObjects':raisecomMplsL2VpnObjects,'raisecomMplsL2vpnEnable':raisecomMplsL2vpnEnable,'raisecomMplsL2vpnMartiniEnable':raisecomMplsL2vpnMartiniEnable,'raisecomMplsL2vpnInterfaceTable':raisecomMplsL2vpnInterfaceTable,'raisecomMplsL2vpnInterfaceEntry':raisecomMplsL2vpnInterfaceEntry,_N:raisecomMplsL2vpnInterfaceIndex,'raisecomMplsL2vpnInterfaceEnable':raisecomMplsL2vpnInterfaceEnable,'raisecomMplsCccPwTable':raisecomMplsCccPwTable,_S:raisecomMplsCccPwEntry,'raisecomMplsCccNexthopType':raisecomMplsCccNexthopType,'raisecomMplsCccNexthop':raisecomMplsCccNexthop,'raisecomMplsLdpObjects':raisecomMplsLdpObjects,'raisecomMplsLdpEnable':raisecomMplsLdpEnable,'raisecomMplsLdpInterfaceTable':raisecomMplsLdpInterfaceTable,'raisecomMplsLdpInterfaceEntry':raisecomMplsLdpInterfaceEntry,_P:raisecomMplsLdpInterfaceIndex,'raisecomMplsLdpInterfaceEnable':raisecomMplsLdpInterfaceEnable,'raisecomMplsLdpInterfaceLAM':raisecomMplsLdpInterfaceLAM,'raisecomMplsLdpInterfaceTransportAddress':raisecomMplsLdpInterfaceTransportAddress,'raisecomMplsLdpInterfaceLdpID':raisecomMplsLdpInterfaceLdpID,'raisecomMplsLdpInterfaceMTU':raisecomMplsLdpInterfaceMTU,'raisecomMplsLdpInterfaceKeepAliveHoldTimer':raisecomMplsLdpInterfaceKeepAliveHoldTimer,'raisecomMplsLdpInterfaceHelloHoldTimer':raisecomMplsLdpInterfaceHelloHoldTimer,'raisecomMplsLdpSessionStatusTrapEnable':raisecomMplsLdpSessionStatusTrapEnable,'raisecomMplsLdpPathVecLimitTrapEnable':raisecomMplsLdpPathVecLimitTrapEnable,'raisecomMplsLdpSessionThreshTrapEnable':raisecomMplsLdpSessionThreshTrapEnable,'raisecomMplsRsvpTEObjects':raisecomMplsRsvpTEObjects,'raisecomMplsRsvpTEEnabled':raisecomMplsRsvpTEEnabled,'raisecomMplsRsvpTERefreshInterval':raisecomMplsRsvpTERefreshInterval,'raisecomMplsRsvpTERefreshMultiple':raisecomMplsRsvpTERefreshMultiple,'raisecomMplsRsvpTERefreshBlockadeMultiple':raisecomMplsRsvpTERefreshBlockadeMultiple,'raisecomMplsRsvpTELSPSetupPriority':raisecomMplsRsvpTELSPSetupPriority,'raisecomMplsRsvpTELSPHoldingPriority':raisecomMplsRsvpTELSPHoldingPriority,'raisecomMplsRsvpTEInitPathRRInterval':raisecomMplsRsvpTEInitPathRRInterval,'raisecomMplsRsvpTEInitPathRRDecay':raisecomMplsRsvpTEInitPathRRDecay,'raisecomMplsRsvpTEInitPathRRLimit':raisecomMplsRsvpTEInitPathRRLimit,'raisecomMplsRsvpTEInterfaceTable':raisecomMplsRsvpTEInterfaceTable,'raisecomMplsRsvpTEInterfaceEntry':raisecomMplsRsvpTEInterfaceEntry,'raisecomMplsRsvpTEIfRefreshInterval':raisecomMplsRsvpTEIfRefreshInterval,'raisecomMplsRsvpTEIfRefreshMultiple':raisecomMplsRsvpTEIfRefreshMultiple,'raisecomMplsRsvpTEIfBlockadeMultiple':raisecomMplsRsvpTEIfBlockadeMultiple,'raisecomMplsRsvpTEIfRRInterval':raisecomMplsRsvpTEIfRRInterval,'raisecomMplsRsvpTEIfRRDecay':raisecomMplsRsvpTEIfRRDecay,'raisecomMplsRsvpTEIfRRLimit':raisecomMplsRsvpTEIfRRLimit,'raisecomMplsRsvpTEIfHelloPeriod':raisecomMplsRsvpTEIfHelloPeriod,'raisecomMplsRsvpTEIfHelloHoldPeriod':raisecomMplsRsvpTEIfHelloHoldPeriod,'raisecomMplsRsvpTEIfHelloDecay':raisecomMplsRsvpTEIfHelloDecay,'raisecomMplsRsvpTEIfHelloPersist':raisecomMplsRsvpTEIfHelloPersist,'raisecomMplsRsvpTEIfEnabled':raisecomMplsRsvpTEIfEnabled,'raisecomMplsRsvpTEIfStatus':raisecomMplsRsvpTEIfStatus})