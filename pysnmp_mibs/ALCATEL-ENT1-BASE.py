_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
alcatelIND1BaseMIB=ModuleIdentity((1,3,6,1,4,1,6486,801))
if mibBuilder.loadTexts:alcatelIND1BaseMIB.setRevisions(('2010-05-13 00:00','2010-03-01 00:08'))
_Alcatel_ObjectIdentity=ObjectIdentity
alcatel=_Alcatel_ObjectIdentity((1,3,6,1,4,1,6486))
if mibBuilder.loadTexts:alcatel.setStatus(_A)
_AlcatelIND1Management_ObjectIdentity=ObjectIdentity
alcatelIND1Management=_AlcatelIND1Management_ObjectIdentity((1,3,6,1,4,1,6486,801,1))
if mibBuilder.loadTexts:alcatelIND1Management.setStatus(_A)
_ManagementIND1Hardware_ObjectIdentity=ObjectIdentity
managementIND1Hardware=_ManagementIND1Hardware_ObjectIdentity((1,3,6,1,4,1,6486,801,1,1))
if mibBuilder.loadTexts:managementIND1Hardware.setStatus(_A)
_HardwareIND1Entities_ObjectIdentity=ObjectIdentity
hardwareIND1Entities=_HardwareIND1Entities_ObjectIdentity((1,3,6,1,4,1,6486,801,1,1,1))
if mibBuilder.loadTexts:hardwareIND1Entities.setStatus(_A)
_HardentIND1Physical_ObjectIdentity=ObjectIdentity
hardentIND1Physical=_HardentIND1Physical_ObjectIdentity((1,3,6,1,4,1,6486,801,1,1,1,1))
if mibBuilder.loadTexts:hardentIND1Physical.setStatus(_A)
_HardentIND1System_ObjectIdentity=ObjectIdentity
hardentIND1System=_HardentIND1System_ObjectIdentity((1,3,6,1,4,1,6486,801,1,1,1,2))
if mibBuilder.loadTexts:hardentIND1System.setStatus(_A)
_HardentIND1Chassis_ObjectIdentity=ObjectIdentity
hardentIND1Chassis=_HardentIND1Chassis_ObjectIdentity((1,3,6,1,4,1,6486,801,1,1,1,3))
if mibBuilder.loadTexts:hardentIND1Chassis.setStatus(_A)
_HardentIND1Pcam_ObjectIdentity=ObjectIdentity
hardentIND1Pcam=_HardentIND1Pcam_ObjectIdentity((1,3,6,1,4,1,6486,801,1,1,1,4))
if mibBuilder.loadTexts:hardentIND1Pcam.setStatus(_A)
_HardwareIND1Devices_ObjectIdentity=ObjectIdentity
hardwareIND1Devices=_HardwareIND1Devices_ObjectIdentity((1,3,6,1,4,1,6486,801,1,1,2))
if mibBuilder.loadTexts:hardwareIND1Devices.setStatus(_A)
_ManagementIND1Software_ObjectIdentity=ObjectIdentity
managementIND1Software=_ManagementIND1Software_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2))
if mibBuilder.loadTexts:managementIND1Software.setStatus(_A)
_SoftwareIND1Entities_ObjectIdentity=ObjectIdentity
softwareIND1Entities=_SoftwareIND1Entities_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1))
if mibBuilder.loadTexts:softwareIND1Entities.setStatus(_A)
_SoftentIND1SnmpAgt_ObjectIdentity=ObjectIdentity
softentIND1SnmpAgt=_SoftentIND1SnmpAgt_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,1))
if mibBuilder.loadTexts:softentIND1SnmpAgt.setStatus(_A)
_SoftentIND1TrapMgr_ObjectIdentity=ObjectIdentity
softentIND1TrapMgr=_SoftentIND1TrapMgr_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,2))
if mibBuilder.loadTexts:softentIND1TrapMgr.setStatus(_A)
_SoftentIND1VlanMgt_ObjectIdentity=ObjectIdentity
softentIND1VlanMgt=_SoftentIND1VlanMgt_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,3))
if mibBuilder.loadTexts:softentIND1VlanMgt.setStatus(_A)
_SoftentIND1GroupMobility_ObjectIdentity=ObjectIdentity
softentIND1GroupMobility=_SoftentIND1GroupMobility_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,4))
if mibBuilder.loadTexts:softentIND1GroupMobility.setStatus(_A)
_SoftentIND1Port_ObjectIdentity=ObjectIdentity
softentIND1Port=_SoftentIND1Port_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,5))
if mibBuilder.loadTexts:softentIND1Port.setStatus(_A)
_SoftentIND1Sesmgr_ObjectIdentity=ObjectIdentity
softentIND1Sesmgr=_SoftentIND1Sesmgr_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,7))
if mibBuilder.loadTexts:softentIND1Sesmgr.setStatus(_A)
_SoftentIND1MacAddress_ObjectIdentity=ObjectIdentity
softentIND1MacAddress=_SoftentIND1MacAddress_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,8))
if mibBuilder.loadTexts:softentIND1MacAddress.setStatus(_A)
_SoftentIND1Aip_ObjectIdentity=ObjectIdentity
softentIND1Aip=_SoftentIND1Aip_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,9))
if mibBuilder.loadTexts:softentIND1Aip.setStatus(_A)
_SoftentIND1Routing_ObjectIdentity=ObjectIdentity
softentIND1Routing=_SoftentIND1Routing_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,10))
if mibBuilder.loadTexts:softentIND1Routing.setStatus(_A)
_RoutingIND1Tm_ObjectIdentity=ObjectIdentity
routingIND1Tm=_RoutingIND1Tm_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,10,1))
if mibBuilder.loadTexts:routingIND1Tm.setStatus(_A)
_RoutingIND1Iprm_ObjectIdentity=ObjectIdentity
routingIND1Iprm=_RoutingIND1Iprm_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,10,2))
if mibBuilder.loadTexts:routingIND1Iprm.setStatus(_A)
_RoutingIND1Rip_ObjectIdentity=ObjectIdentity
routingIND1Rip=_RoutingIND1Rip_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,10,3))
if mibBuilder.loadTexts:routingIND1Rip.setStatus(_A)
_RoutingIND1Ospf_ObjectIdentity=ObjectIdentity
routingIND1Ospf=_RoutingIND1Ospf_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,10,4))
if mibBuilder.loadTexts:routingIND1Ospf.setStatus(_A)
_RoutingIND1Bgp_ObjectIdentity=ObjectIdentity
routingIND1Bgp=_RoutingIND1Bgp_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,10,5))
if mibBuilder.loadTexts:routingIND1Bgp.setStatus(_A)
_RoutingIND1Pim_ObjectIdentity=ObjectIdentity
routingIND1Pim=_RoutingIND1Pim_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,10,6))
if mibBuilder.loadTexts:routingIND1Pim.setStatus(_A)
_RoutingIND1Dvmrp_ObjectIdentity=ObjectIdentity
routingIND1Dvmrp=_RoutingIND1Dvmrp_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,10,7))
if mibBuilder.loadTexts:routingIND1Dvmrp.setStatus(_A)
_RoutingIND1Ipx_ObjectIdentity=ObjectIdentity
routingIND1Ipx=_RoutingIND1Ipx_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,10,8))
if mibBuilder.loadTexts:routingIND1Ipx.setStatus(_A)
_RoutingIND1UdpRelay_ObjectIdentity=ObjectIdentity
routingIND1UdpRelay=_RoutingIND1UdpRelay_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,10,9))
if mibBuilder.loadTexts:routingIND1UdpRelay.setStatus(_A)
_RoutingIND1Ipmrm_ObjectIdentity=ObjectIdentity
routingIND1Ipmrm=_RoutingIND1Ipmrm_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,10,10))
if mibBuilder.loadTexts:routingIND1Ipmrm.setStatus(_A)
_RoutingIND1RDP_ObjectIdentity=ObjectIdentity
routingIND1RDP=_RoutingIND1RDP_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,10,11))
if mibBuilder.loadTexts:routingIND1RDP.setStatus(_A)
_RoutingIND1Ripng_ObjectIdentity=ObjectIdentity
routingIND1Ripng=_RoutingIND1Ripng_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,10,12))
if mibBuilder.loadTexts:routingIND1Ripng.setStatus(_A)
_RoutingIND1Ospf3_ObjectIdentity=ObjectIdentity
routingIND1Ospf3=_RoutingIND1Ospf3_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,10,13))
if mibBuilder.loadTexts:routingIND1Ospf3.setStatus(_A)
_RoutingIND1ISIS_ObjectIdentity=ObjectIdentity
routingIND1ISIS=_RoutingIND1ISIS_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,10,14))
if mibBuilder.loadTexts:routingIND1ISIS.setStatus(_A)
_RoutingIND1Vrf_ObjectIdentity=ObjectIdentity
routingIND1Vrf=_RoutingIND1Vrf_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,10,15))
if mibBuilder.loadTexts:routingIND1Vrf.setStatus(_A)
_RoutingIND1GlobalRouteTable_ObjectIdentity=ObjectIdentity
routingIND1GlobalRouteTable=_RoutingIND1GlobalRouteTable_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,10,16))
if mibBuilder.loadTexts:routingIND1GlobalRouteTable.setStatus(_A)
_RoutingIND1IsisSpb_ObjectIdentity=ObjectIdentity
routingIND1IsisSpb=_RoutingIND1IsisSpb_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,10,17))
if mibBuilder.loadTexts:routingIND1IsisSpb.setStatus(_A)
_SoftentIND1Confmgr_ObjectIdentity=ObjectIdentity
softentIND1Confmgr=_SoftentIND1Confmgr_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,11))
if mibBuilder.loadTexts:softentIND1Confmgr.setStatus(_A)
_SoftentIND1VlanStp_ObjectIdentity=ObjectIdentity
softentIND1VlanStp=_SoftentIND1VlanStp_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,12))
if mibBuilder.loadTexts:softentIND1VlanStp.setStatus(_A)
_SoftentIND1LnkAgg_ObjectIdentity=ObjectIdentity
softentIND1LnkAgg=_SoftentIND1LnkAgg_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,13))
if mibBuilder.loadTexts:softentIND1LnkAgg.setStatus(_A)
_SoftentIND1Policy_ObjectIdentity=ObjectIdentity
softentIND1Policy=_SoftentIND1Policy_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,14))
if mibBuilder.loadTexts:softentIND1Policy.setStatus(_A)
_SoftentIND1AAA_ObjectIdentity=ObjectIdentity
softentIND1AAA=_SoftentIND1AAA_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,15))
if mibBuilder.loadTexts:softentIND1AAA.setStatus(_A)
_SoftentIND1Health_ObjectIdentity=ObjectIdentity
softentIND1Health=_SoftentIND1Health_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,16))
if mibBuilder.loadTexts:softentIND1Health.setStatus(_A)
_SoftentIND1WebMgt_ObjectIdentity=ObjectIdentity
softentIND1WebMgt=_SoftentIND1WebMgt_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,17))
if mibBuilder.loadTexts:softentIND1WebMgt.setStatus(_A)
_SoftentIND1Ipms_ObjectIdentity=ObjectIdentity
softentIND1Ipms=_SoftentIND1Ipms_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,18))
if mibBuilder.loadTexts:softentIND1Ipms.setStatus(_A)
_SoftentIND1PortMirroringMonitoring_ObjectIdentity=ObjectIdentity
softentIND1PortMirroringMonitoring=_SoftentIND1PortMirroringMonitoring_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,19))
if mibBuilder.loadTexts:softentIND1PortMirroringMonitoring.setStatus(_A)
_SoftentIND1Slb_ObjectIdentity=ObjectIdentity
softentIND1Slb=_SoftentIND1Slb_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,20))
if mibBuilder.loadTexts:softentIND1Slb.setStatus(_A)
_SoftentIND1Dot1Q_ObjectIdentity=ObjectIdentity
softentIND1Dot1Q=_SoftentIND1Dot1Q_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,21))
if mibBuilder.loadTexts:softentIND1Dot1Q.setStatus(_A)
_SoftentIND1QoS_ObjectIdentity=ObjectIdentity
softentIND1QoS=_SoftentIND1QoS_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,22))
if mibBuilder.loadTexts:softentIND1QoS.setStatus(_A)
_SoftentIND1Ip_ObjectIdentity=ObjectIdentity
softentIND1Ip=_SoftentIND1Ip_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,23))
if mibBuilder.loadTexts:softentIND1Ip.setStatus(_A)
_SoftentIND1StackMgr_ObjectIdentity=ObjectIdentity
softentIND1StackMgr=_SoftentIND1StackMgr_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,24))
if mibBuilder.loadTexts:softentIND1StackMgr.setStatus(_A)
_SoftentIND1Partmgr_ObjectIdentity=ObjectIdentity
softentIND1Partmgr=_SoftentIND1Partmgr_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,25))
if mibBuilder.loadTexts:softentIND1Partmgr.setStatus(_A)
_SoftentIND1Ntp_ObjectIdentity=ObjectIdentity
softentIND1Ntp=_SoftentIND1Ntp_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,26))
if mibBuilder.loadTexts:softentIND1Ntp.setStatus(_A)
_SoftentIND1InLinePower_ObjectIdentity=ObjectIdentity
softentIND1InLinePower=_SoftentIND1InLinePower_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,27))
if mibBuilder.loadTexts:softentIND1InLinePower.setStatus(_A)
_SoftentIND1Vrrp_ObjectIdentity=ObjectIdentity
softentIND1Vrrp=_SoftentIND1Vrrp_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,28))
if mibBuilder.loadTexts:softentIND1Vrrp.setStatus(_A)
_SoftentIND1Ipv6_ObjectIdentity=ObjectIdentity
softentIND1Ipv6=_SoftentIND1Ipv6_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,29))
if mibBuilder.loadTexts:softentIND1Ipv6.setStatus(_A)
_SoftentIND1Dot1X_ObjectIdentity=ObjectIdentity
softentIND1Dot1X=_SoftentIND1Dot1X_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,30))
if mibBuilder.loadTexts:softentIND1Dot1X.setStatus(_A)
_SoftentIND1Sonet_ObjectIdentity=ObjectIdentity
softentIND1Sonet=_SoftentIND1Sonet_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,31))
if mibBuilder.loadTexts:softentIND1Sonet.setStatus(_A)
_SoftentIND1Atm_ObjectIdentity=ObjectIdentity
softentIND1Atm=_SoftentIND1Atm_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,32))
if mibBuilder.loadTexts:softentIND1Atm.setStatus(_A)
_SoftentIND1PortMapping_ObjectIdentity=ObjectIdentity
softentIND1PortMapping=_SoftentIND1PortMapping_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,33))
if mibBuilder.loadTexts:softentIND1PortMapping.setStatus(_A)
_SoftentIND1Igmp_ObjectIdentity=ObjectIdentity
softentIND1Igmp=_SoftentIND1Igmp_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,34))
if mibBuilder.loadTexts:softentIND1Igmp.setStatus(_A)
_SoftentIND1Mld_ObjectIdentity=ObjectIdentity
softentIND1Mld=_SoftentIND1Mld_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,35))
if mibBuilder.loadTexts:softentIND1Mld.setStatus(_A)
_SoftentIND1Gvrp_ObjectIdentity=ObjectIdentity
softentIND1Gvrp=_SoftentIND1Gvrp_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,36))
if mibBuilder.loadTexts:softentIND1Gvrp.setStatus(_A)
_SoftentIND1VlanStackingMgt_ObjectIdentity=ObjectIdentity
softentIND1VlanStackingMgt=_SoftentIND1VlanStackingMgt_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,37))
if mibBuilder.loadTexts:softentIND1VlanStackingMgt.setStatus(_A)
_SoftentIND1Wccp_ObjectIdentity=ObjectIdentity
softentIND1Wccp=_SoftentIND1Wccp_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,38))
if mibBuilder.loadTexts:softentIND1Wccp.setStatus(_A)
_SoftentIND1Ssh_ObjectIdentity=ObjectIdentity
softentIND1Ssh=_SoftentIND1Ssh_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,39))
if mibBuilder.loadTexts:softentIND1Ssh.setStatus(_A)
_SoftentIND1EthernetOam_ObjectIdentity=ObjectIdentity
softentIND1EthernetOam=_SoftentIND1EthernetOam_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,40))
if mibBuilder.loadTexts:softentIND1EthernetOam.setStatus(_A)
_SoftentIND1IPMVlanMgt_ObjectIdentity=ObjectIdentity
softentIND1IPMVlanMgt=_SoftentIND1IPMVlanMgt_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,41))
if mibBuilder.loadTexts:softentIND1IPMVlanMgt.setStatus(_A)
_SoftentIND1IPsec_ObjectIdentity=ObjectIdentity
softentIND1IPsec=_SoftentIND1IPsec_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,43))
if mibBuilder.loadTexts:softentIND1IPsec.setStatus(_A)
_SoftentIND1Udld_ObjectIdentity=ObjectIdentity
softentIND1Udld=_SoftentIND1Udld_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,44))
if mibBuilder.loadTexts:softentIND1Udld.setStatus(_A)
_SoftentIND1BFD_ObjectIdentity=ObjectIdentity
softentIND1BFD=_SoftentIND1BFD_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,45))
if mibBuilder.loadTexts:softentIND1BFD.setStatus(_A)
_SoftentIND1Erp_ObjectIdentity=ObjectIdentity
softentIND1Erp=_SoftentIND1Erp_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,46))
if mibBuilder.loadTexts:softentIND1Erp.setStatus(_A)
_SoftentIND1NetSec_ObjectIdentity=ObjectIdentity
softentIND1NetSec=_SoftentIND1NetSec_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,48))
if mibBuilder.loadTexts:softentIND1NetSec.setStatus(_A)
_SoftentIND1eService_ObjectIdentity=ObjectIdentity
softentIND1eService=_SoftentIND1eService_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,50))
if mibBuilder.loadTexts:softentIND1eService.setStatus(_A)
_SoftentIND1serviceMgr_ObjectIdentity=ObjectIdentity
softentIND1serviceMgr=_SoftentIND1serviceMgr_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,51))
if mibBuilder.loadTexts:softentIND1serviceMgr.setStatus(_A)
_SoftentIND1Dot3Oam_ObjectIdentity=ObjectIdentity
softentIND1Dot3Oam=_SoftentIND1Dot3Oam_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,52))
if mibBuilder.loadTexts:softentIND1Dot3Oam.setStatus(_A)
_SoftentIND1MplsFrr_ObjectIdentity=ObjectIdentity
softentIND1MplsFrr=_SoftentIND1MplsFrr_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,53))
if mibBuilder.loadTexts:softentIND1MplsFrr.setStatus(_A)
_SoftentIND1LicenseManager_ObjectIdentity=ObjectIdentity
softentIND1LicenseManager=_SoftentIND1LicenseManager_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,54))
if mibBuilder.loadTexts:softentIND1LicenseManager.setStatus(_A)
_SoftentIND1MultiChassisManager_ObjectIdentity=ObjectIdentity
softentIND1MultiChassisManager=_SoftentIND1MultiChassisManager_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,55))
if mibBuilder.loadTexts:softentIND1MultiChassisManager.setStatus(_A)
_SoftentIND1Saa_ObjectIdentity=ObjectIdentity
softentIND1Saa=_SoftentIND1Saa_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,56))
if mibBuilder.loadTexts:softentIND1Saa.setStatus(_A)
_SoftentIND1LldpMed_ObjectIdentity=ObjectIdentity
softentIND1LldpMed=_SoftentIND1LldpMed_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,58))
if mibBuilder.loadTexts:softentIND1LldpMed.setStatus(_A)
_SoftentIND1DhcpSrv_ObjectIdentity=ObjectIdentity
softentIND1DhcpSrv=_SoftentIND1DhcpSrv_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,59))
if mibBuilder.loadTexts:softentIND1DhcpSrv.setStatus(_A)
_SoftentIND1CapMan_ObjectIdentity=ObjectIdentity
softentIND1CapMan=_SoftentIND1CapMan_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,60))
if mibBuilder.loadTexts:softentIND1CapMan.setStatus(_A)
_SoftentIND1Vfc_ObjectIdentity=ObjectIdentity
softentIND1Vfc=_SoftentIND1Vfc_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,61))
if mibBuilder.loadTexts:softentIND1Vfc.setStatus(_A)
_SoftentIND1Mvrp_ObjectIdentity=ObjectIdentity
softentIND1Mvrp=_SoftentIND1Mvrp_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,62))
if mibBuilder.loadTexts:softentIND1Mvrp.setStatus(_A)
_SoftentIND1Da_ObjectIdentity=ObjectIdentity
softentIND1Da=_SoftentIND1Da_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,63))
if mibBuilder.loadTexts:softentIND1Da.setStatus(_A)
_SoftentIND1HAVlan_ObjectIdentity=ObjectIdentity
softentIND1HAVlan=_SoftentIND1HAVlan_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,64))
if mibBuilder.loadTexts:softentIND1HAVlan.setStatus(_A)
_SoftentIND1DHL_ObjectIdentity=ObjectIdentity
softentIND1DHL=_SoftentIND1DHL_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,65))
if mibBuilder.loadTexts:softentIND1DHL.setStatus(_A)
_SoftentIND1PwrMon_ObjectIdentity=ObjectIdentity
softentIND1PwrMon=_SoftentIND1PwrMon_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,66))
if mibBuilder.loadTexts:softentIND1PwrMon.setStatus(_A)
_SoftentIND1EnergyAware_ObjectIdentity=ObjectIdentity
softentIND1EnergyAware=_SoftentIND1EnergyAware_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,67))
if mibBuilder.loadTexts:softentIND1EnergyAware.setStatus(_A)
_SoftentIND1PowerQuality_ObjectIdentity=ObjectIdentity
softentIND1PowerQuality=_SoftentIND1PowerQuality_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,68))
if mibBuilder.loadTexts:softentIND1PowerQuality.setStatus(_A)
_SoftentIND1VirtualChassisManager_ObjectIdentity=ObjectIdentity
softentIND1VirtualChassisManager=_SoftentIND1VirtualChassisManager_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,69))
if mibBuilder.loadTexts:softentIND1VirtualChassisManager.setStatus(_A)
_SoftentIND1EvbMib_ObjectIdentity=ObjectIdentity
softentIND1EvbMib=_SoftentIND1EvbMib_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,70))
if mibBuilder.loadTexts:softentIND1EvbMib.setStatus(_A)
_SoftentIND1QcnMib_ObjectIdentity=ObjectIdentity
softentIND1QcnMib=_SoftentIND1QcnMib_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,71))
if mibBuilder.loadTexts:softentIND1QcnMib.setStatus(_A)
_SoftentIND1Dcbx_ObjectIdentity=ObjectIdentity
softentIND1Dcbx=_SoftentIND1Dcbx_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,72))
if mibBuilder.loadTexts:softentIND1Dcbx.setStatus(_A)
_SoftentIND1AppFingerPrintMIB_ObjectIdentity=ObjectIdentity
softentIND1AppFingerPrintMIB=_SoftentIND1AppFingerPrintMIB_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,73))
if mibBuilder.loadTexts:softentIND1AppFingerPrintMIB.setStatus(_A)
_SoftentIND1Fips_ObjectIdentity=ObjectIdentity
softentIND1Fips=_SoftentIND1Fips_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,74))
if mibBuilder.loadTexts:softentIND1Fips.setStatus(_A)
_SoftentIND1AutoFabric_ObjectIdentity=ObjectIdentity
softentIND1AutoFabric=_SoftentIND1AutoFabric_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,75))
if mibBuilder.loadTexts:softentIND1AutoFabric.setStatus(_A)
_SoftentIND1SIPSnooping_ObjectIdentity=ObjectIdentity
softentIND1SIPSnooping=_SoftentIND1SIPSnooping_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,76))
if mibBuilder.loadTexts:softentIND1SIPSnooping.setStatus(_A)
_SoftentIND1OpenflowMIB_ObjectIdentity=ObjectIdentity
softentIND1OpenflowMIB=_SoftentIND1OpenflowMIB_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,77))
if mibBuilder.loadTexts:softentIND1OpenflowMIB.setStatus(_A)
_SoftentIND1DPI_ObjectIdentity=ObjectIdentity
softentIND1DPI=_SoftentIND1DPI_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,78))
if mibBuilder.loadTexts:softentIND1DPI.setStatus(_A)
_SoftentIND1MsgSrvMIB_ObjectIdentity=ObjectIdentity
softentIND1MsgSrvMIB=_SoftentIND1MsgSrvMIB_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,79))
if mibBuilder.loadTexts:softentIND1MsgSrvMIB.setStatus(_A)
_SoftentIND1ActiveLeaseSrvMIB_ObjectIdentity=ObjectIdentity
softentIND1ActiveLeaseSrvMIB=_SoftentIND1ActiveLeaseSrvMIB_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,80))
if mibBuilder.loadTexts:softentIND1ActiveLeaseSrvMIB.setStatus(_A)
_SoftentIND1AppMon_ObjectIdentity=ObjectIdentity
softentIND1AppMon=_SoftentIND1AppMon_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,81))
if mibBuilder.loadTexts:softentIND1AppMon.setStatus(_A)
_SoftentIND1Lbd_ObjectIdentity=ObjectIdentity
softentIND1Lbd=_SoftentIND1Lbd_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,82))
if mibBuilder.loadTexts:softentIND1Lbd.setStatus(_A)
_SoftentIND1AutoConfig_ObjectIdentity=ObjectIdentity
softentIND1AutoConfig=_SoftentIND1AutoConfig_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,83))
if mibBuilder.loadTexts:softentIND1AutoConfig.setStatus(_A)
_SoftentIND1VMSnooping_ObjectIdentity=ObjectIdentity
softentIND1VMSnooping=_SoftentIND1VMSnooping_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,84))
if mibBuilder.loadTexts:softentIND1VMSnooping.setStatus(_A)
_SoftentIND1PPPoEIA_ObjectIdentity=ObjectIdentity
softentIND1PPPoEIA=_SoftentIND1PPPoEIA_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,85))
if mibBuilder.loadTexts:softentIND1PPPoEIA.setStatus(_A)
_SoftentIND1EventScripting_ObjectIdentity=ObjectIdentity
softentIND1EventScripting=_SoftentIND1EventScripting_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,86))
if mibBuilder.loadTexts:softentIND1EventScripting.setStatus(_A)
_SoftentIND1LldpTrust_ObjectIdentity=ObjectIdentity
softentIND1LldpTrust=_SoftentIND1LldpTrust_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,87))
if mibBuilder.loadTexts:softentIND1LldpTrust.setStatus(_A)
_SoftentIND1TCAM_ObjectIdentity=ObjectIdentity
softentIND1TCAM=_SoftentIND1TCAM_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,88))
if mibBuilder.loadTexts:softentIND1TCAM.setStatus(_A)
_SoftentIND1PrivateVlan_ObjectIdentity=ObjectIdentity
softentIND1PrivateVlan=_SoftentIND1PrivateVlan_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,89))
if mibBuilder.loadTexts:softentIND1PrivateVlan.setStatus(_A)
_SoftwareIND1Services_ObjectIdentity=ObjectIdentity
softwareIND1Services=_SoftwareIND1Services_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,2))
if mibBuilder.loadTexts:softwareIND1Services.setStatus(_A)
_ServentIND1Aqe_ObjectIdentity=ObjectIdentity
serventIND1Aqe=_ServentIND1Aqe_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,2,1))
if mibBuilder.loadTexts:serventIND1Aqe.setStatus(_A)
_ManagementIND1Notifications_ObjectIdentity=ObjectIdentity
managementIND1Notifications=_ManagementIND1Notifications_ObjectIdentity((1,3,6,1,4,1,6486,801,1,3))
if mibBuilder.loadTexts:managementIND1Notifications.setStatus(_A)
_NotificationIND1Entities_ObjectIdentity=ObjectIdentity
notificationIND1Entities=_NotificationIND1Entities_ObjectIdentity((1,3,6,1,4,1,6486,801,1,3,1))
if mibBuilder.loadTexts:notificationIND1Entities.setStatus(_A)
_NotificationIND1Traps_ObjectIdentity=ObjectIdentity
notificationIND1Traps=_NotificationIND1Traps_ObjectIdentity((1,3,6,1,4,1,6486,801,1,3,2))
if mibBuilder.loadTexts:notificationIND1Traps.setStatus('deprecated')
_ManagementIND1AgentCapabilities_ObjectIdentity=ObjectIdentity
managementIND1AgentCapabilities=_ManagementIND1AgentCapabilities_ObjectIdentity((1,3,6,1,4,1,6486,801,1,4))
if mibBuilder.loadTexts:managementIND1AgentCapabilities.setStatus(_A)
mibBuilder.exportSymbols('ALCATEL-ENT1-BASE',**{'alcatel':alcatel,'alcatelIND1BaseMIB':alcatelIND1BaseMIB,'alcatelIND1Management':alcatelIND1Management,'managementIND1Hardware':managementIND1Hardware,'hardwareIND1Entities':hardwareIND1Entities,'hardentIND1Physical':hardentIND1Physical,'hardentIND1System':hardentIND1System,'hardentIND1Chassis':hardentIND1Chassis,'hardentIND1Pcam':hardentIND1Pcam,'hardwareIND1Devices':hardwareIND1Devices,'managementIND1Software':managementIND1Software,'softwareIND1Entities':softwareIND1Entities,'softentIND1SnmpAgt':softentIND1SnmpAgt,'softentIND1TrapMgr':softentIND1TrapMgr,'softentIND1VlanMgt':softentIND1VlanMgt,'softentIND1GroupMobility':softentIND1GroupMobility,'softentIND1Port':softentIND1Port,'softentIND1Sesmgr':softentIND1Sesmgr,'softentIND1MacAddress':softentIND1MacAddress,'softentIND1Aip':softentIND1Aip,'softentIND1Routing':softentIND1Routing,'routingIND1Tm':routingIND1Tm,'routingIND1Iprm':routingIND1Iprm,'routingIND1Rip':routingIND1Rip,'routingIND1Ospf':routingIND1Ospf,'routingIND1Bgp':routingIND1Bgp,'routingIND1Pim':routingIND1Pim,'routingIND1Dvmrp':routingIND1Dvmrp,'routingIND1Ipx':routingIND1Ipx,'routingIND1UdpRelay':routingIND1UdpRelay,'routingIND1Ipmrm':routingIND1Ipmrm,'routingIND1RDP':routingIND1RDP,'routingIND1Ripng':routingIND1Ripng,'routingIND1Ospf3':routingIND1Ospf3,'routingIND1ISIS':routingIND1ISIS,'routingIND1Vrf':routingIND1Vrf,'routingIND1GlobalRouteTable':routingIND1GlobalRouteTable,'routingIND1IsisSpb':routingIND1IsisSpb,'softentIND1Confmgr':softentIND1Confmgr,'softentIND1VlanStp':softentIND1VlanStp,'softentIND1LnkAgg':softentIND1LnkAgg,'softentIND1Policy':softentIND1Policy,'softentIND1AAA':softentIND1AAA,'softentIND1Health':softentIND1Health,'softentIND1WebMgt':softentIND1WebMgt,'softentIND1Ipms':softentIND1Ipms,'softentIND1PortMirroringMonitoring':softentIND1PortMirroringMonitoring,'softentIND1Slb':softentIND1Slb,'softentIND1Dot1Q':softentIND1Dot1Q,'softentIND1QoS':softentIND1QoS,'softentIND1Ip':softentIND1Ip,'softentIND1StackMgr':softentIND1StackMgr,'softentIND1Partmgr':softentIND1Partmgr,'softentIND1Ntp':softentIND1Ntp,'softentIND1InLinePower':softentIND1InLinePower,'softentIND1Vrrp':softentIND1Vrrp,'softentIND1Ipv6':softentIND1Ipv6,'softentIND1Dot1X':softentIND1Dot1X,'softentIND1Sonet':softentIND1Sonet,'softentIND1Atm':softentIND1Atm,'softentIND1PortMapping':softentIND1PortMapping,'softentIND1Igmp':softentIND1Igmp,'softentIND1Mld':softentIND1Mld,'softentIND1Gvrp':softentIND1Gvrp,'softentIND1VlanStackingMgt':softentIND1VlanStackingMgt,'softentIND1Wccp':softentIND1Wccp,'softentIND1Ssh':softentIND1Ssh,'softentIND1EthernetOam':softentIND1EthernetOam,'softentIND1IPMVlanMgt':softentIND1IPMVlanMgt,'softentIND1IPsec':softentIND1IPsec,'softentIND1Udld':softentIND1Udld,'softentIND1BFD':softentIND1BFD,'softentIND1Erp':softentIND1Erp,'softentIND1NetSec':softentIND1NetSec,'softentIND1eService':softentIND1eService,'softentIND1serviceMgr':softentIND1serviceMgr,'softentIND1Dot3Oam':softentIND1Dot3Oam,'softentIND1MplsFrr':softentIND1MplsFrr,'softentIND1LicenseManager':softentIND1LicenseManager,'softentIND1MultiChassisManager':softentIND1MultiChassisManager,'softentIND1Saa':softentIND1Saa,'softentIND1LldpMed':softentIND1LldpMed,'softentIND1DhcpSrv':softentIND1DhcpSrv,'softentIND1CapMan':softentIND1CapMan,'softentIND1Vfc':softentIND1Vfc,'softentIND1Mvrp':softentIND1Mvrp,'softentIND1Da':softentIND1Da,'softentIND1HAVlan':softentIND1HAVlan,'softentIND1DHL':softentIND1DHL,'softentIND1PwrMon':softentIND1PwrMon,'softentIND1EnergyAware':softentIND1EnergyAware,'softentIND1PowerQuality':softentIND1PowerQuality,'softentIND1VirtualChassisManager':softentIND1VirtualChassisManager,'softentIND1EvbMib':softentIND1EvbMib,'softentIND1QcnMib':softentIND1QcnMib,'softentIND1Dcbx':softentIND1Dcbx,'softentIND1AppFingerPrintMIB':softentIND1AppFingerPrintMIB,'softentIND1Fips':softentIND1Fips,'softentIND1AutoFabric':softentIND1AutoFabric,'softentIND1SIPSnooping':softentIND1SIPSnooping,'softentIND1OpenflowMIB':softentIND1OpenflowMIB,'softentIND1DPI':softentIND1DPI,'softentIND1MsgSrvMIB':softentIND1MsgSrvMIB,'softentIND1ActiveLeaseSrvMIB':softentIND1ActiveLeaseSrvMIB,'softentIND1AppMon':softentIND1AppMon,'softentIND1Lbd':softentIND1Lbd,'softentIND1AutoConfig':softentIND1AutoConfig,'softentIND1VMSnooping':softentIND1VMSnooping,'softentIND1PPPoEIA':softentIND1PPPoEIA,'softentIND1EventScripting':softentIND1EventScripting,'softentIND1LldpTrust':softentIND1LldpTrust,'softentIND1TCAM':softentIND1TCAM,'softentIND1PrivateVlan':softentIND1PrivateVlan,'softwareIND1Services':softwareIND1Services,'serventIND1Aqe':serventIND1Aqe,'managementIND1Notifications':managementIND1Notifications,'notificationIND1Entities':notificationIND1Entities,'notificationIND1Traps':notificationIND1Traps,'managementIND1AgentCapabilities':managementIND1AgentCapabilities})