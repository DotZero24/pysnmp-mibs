_m='threshold'
_l='endOfHighUsageWindow'
_k='period'
_j='actionTaken'
_i='portNumber'
_h='loginDescription'
_g='loginResult'
_f='loginEmail'
_e='tunnelDescription'
_d='vpnPeer'
_c='radiusServerIp'
_b='changeDescription'
_a='networkAdmin'
_Z='userEmail'
_Y='userName'
_X='devInterfaceIndex'
_W='devInterfaceDevMac'
_V='ssidNumber'
_U='OctetString'
_T='devStatus'
_S='ssidName'
_R='devSubnet'
_Q='devInterfaceCarrier'
_P='devInterfaceModel'
_O='PhysAddress'
_N='devInterfacePortDescription'
_M='devInterfaceName'
_L='networkId'
_K='powerSupplyNum'
_J='devInterfaceDescription'
_I='vlanNumber'
_H='devLanIp'
_G='Integer32'
_F='devMac'
_E='organizationName'
_D='networkName'
_C='read-only'
_B='current'
_A='MERAKI-CLOUD-CONTROLLER-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_U,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,ifIndex=mibBuilder.importSymbols('IF-MIB','InterfaceIndex','ifIndex')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_G,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DateAndTime,DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString',_O,'TextualConvention')
cloudController=ModuleIdentity((1,3,6,1,4,1,29671,1))
if mibBuilder.loadTexts:cloudController.setRevisions(('2016-09-01 00:01','2015-06-25 00:01','2012-05-24 00:01'))
_Meraki_ObjectIdentity=ObjectIdentity
meraki=_Meraki_ObjectIdentity((1,3,6,1,4,1,29671))
_Organization_ObjectIdentity=ObjectIdentity
organization=_Organization_ObjectIdentity((1,3,6,1,4,1,29671,1,1))
_OrganizationName_Type=DisplayString
_OrganizationName_Object=MibScalar
organizationName=_OrganizationName_Object((1,3,6,1,4,1,29671,1,1,1),_OrganizationName_Type())
organizationName.setMaxAccess(_C)
if mibBuilder.loadTexts:organizationName.setStatus(_B)
_NetworkTable_Object=MibTable
networkTable=_NetworkTable_Object((1,3,6,1,4,1,29671,1,1,2))
if mibBuilder.loadTexts:networkTable.setStatus(_B)
_NetworkEntry_Object=MibTableRow
networkEntry=_NetworkEntry_Object((1,3,6,1,4,1,29671,1,1,2,1))
networkEntry.setIndexNames((0,_A,_L))
if mibBuilder.loadTexts:networkEntry.setStatus(_B)
class _NetworkId_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_NetworkId_Type.__name__=_U
_NetworkId_Object=MibTableColumn
networkId=_NetworkId_Object((1,3,6,1,4,1,29671,1,1,2,1,1),_NetworkId_Type())
networkId.setMaxAccess(_C)
if mibBuilder.loadTexts:networkId.setStatus(_B)
_NetworkName_Type=DisplayString
_NetworkName_Object=MibTableColumn
networkName=_NetworkName_Object((1,3,6,1,4,1,29671,1,1,2,1,2),_NetworkName_Type())
networkName.setMaxAccess(_C)
if mibBuilder.loadTexts:networkName.setStatus(_B)
_NetworkAdmin_Type=DisplayString
_NetworkAdmin_Object=MibScalar
networkAdmin=_NetworkAdmin_Object((1,3,6,1,4,1,29671,1,1,2,1,3),_NetworkAdmin_Type())
networkAdmin.setMaxAccess(_C)
if mibBuilder.loadTexts:networkAdmin.setStatus(_B)
_VpnPeer_Type=IpAddress
_VpnPeer_Object=MibScalar
vpnPeer=_VpnPeer_Object((1,3,6,1,4,1,29671,1,1,2,1,4),_VpnPeer_Type())
vpnPeer.setMaxAccess(_C)
if mibBuilder.loadTexts:vpnPeer.setStatus(_B)
_SsidTable_Object=MibTable
ssidTable=_SsidTable_Object((1,3,6,1,4,1,29671,1,1,3))
if mibBuilder.loadTexts:ssidTable.setStatus(_B)
_SsidEntry_Object=MibTableRow
ssidEntry=_SsidEntry_Object((1,3,6,1,4,1,29671,1,1,3,1))
ssidEntry.setIndexNames((0,_A,_L),(0,_A,_V))
if mibBuilder.loadTexts:ssidEntry.setStatus(_B)
_SsidNetworkName_Type=DisplayString
_SsidNetworkName_Object=MibTableColumn
ssidNetworkName=_SsidNetworkName_Object((1,3,6,1,4,1,29671,1,1,3,1,1),_SsidNetworkName_Type())
ssidNetworkName.setMaxAccess(_C)
if mibBuilder.loadTexts:ssidNetworkName.setStatus(_B)
class _SsidNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SsidNumber_Type.__name__=_G
_SsidNumber_Object=MibTableColumn
ssidNumber=_SsidNumber_Object((1,3,6,1,4,1,29671,1,1,3,1,2),_SsidNumber_Type())
ssidNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:ssidNumber.setStatus(_B)
_SsidName_Type=DisplayString
_SsidName_Object=MibTableColumn
ssidName=_SsidName_Object((1,3,6,1,4,1,29671,1,1,3,1,3),_SsidName_Type())
ssidName.setMaxAccess(_C)
if mibBuilder.loadTexts:ssidName.setStatus(_B)
_UserName_Type=DisplayString
_UserName_Object=MibScalar
userName=_UserName_Object((1,3,6,1,4,1,29671,1,1,3,1,4),_UserName_Type())
userName.setMaxAccess(_C)
if mibBuilder.loadTexts:userName.setStatus(_B)
_UserEmail_Type=DisplayString
_UserEmail_Object=MibScalar
userEmail=_UserEmail_Object((1,3,6,1,4,1,29671,1,1,3,1,5),_UserEmail_Type())
userEmail.setMaxAccess(_C)
if mibBuilder.loadTexts:userEmail.setStatus(_B)
_RadiusServerIp_Type=IpAddress
_RadiusServerIp_Object=MibScalar
radiusServerIp=_RadiusServerIp_Object((1,3,6,1,4,1,29671,1,1,3,1,6),_RadiusServerIp_Type())
radiusServerIp.setMaxAccess(_C)
if mibBuilder.loadTexts:radiusServerIp.setStatus(_B)
_RadiusServerPort_Type=IpAddress
_RadiusServerPort_Object=MibScalar
radiusServerPort=_RadiusServerPort_Object((1,3,6,1,4,1,29671,1,1,3,1,7),_RadiusServerPort_Type())
radiusServerPort.setMaxAccess(_C)
if mibBuilder.loadTexts:radiusServerPort.setStatus(_B)
_DevTable_Object=MibTable
devTable=_DevTable_Object((1,3,6,1,4,1,29671,1,1,4))
if mibBuilder.loadTexts:devTable.setStatus(_B)
_DevEntry_Object=MibTableRow
devEntry=_DevEntry_Object((1,3,6,1,4,1,29671,1,1,4,1))
devEntry.setIndexNames((0,_A,_F))
if mibBuilder.loadTexts:devEntry.setStatus(_B)
class _DevMac_Type(PhysAddress):subtypeSpec=PhysAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
_DevMac_Type.__name__=_O
_DevMac_Object=MibTableColumn
devMac=_DevMac_Object((1,3,6,1,4,1,29671,1,1,4,1,1),_DevMac_Type())
devMac.setMaxAccess(_C)
if mibBuilder.loadTexts:devMac.setStatus(_B)
_DevName_Type=DisplayString
_DevName_Object=MibTableColumn
devName=_DevName_Object((1,3,6,1,4,1,29671,1,1,4,1,2),_DevName_Type())
devName.setMaxAccess(_C)
if mibBuilder.loadTexts:devName.setStatus(_B)
class _DevStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('offline',0),('online',1)))
_DevStatus_Type.__name__=_G
_DevStatus_Object=MibTableColumn
devStatus=_DevStatus_Object((1,3,6,1,4,1,29671,1,1,4,1,3),_DevStatus_Type())
devStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:devStatus.setStatus(_B)
_DevContactedAt_Type=DateAndTime
_DevContactedAt_Object=MibTableColumn
devContactedAt=_DevContactedAt_Object((1,3,6,1,4,1,29671,1,1,4,1,4),_DevContactedAt_Type())
devContactedAt.setMaxAccess(_C)
if mibBuilder.loadTexts:devContactedAt.setStatus(_B)
_DevClientCount_Type=Integer32
_DevClientCount_Object=MibTableColumn
devClientCount=_DevClientCount_Object((1,3,6,1,4,1,29671,1,1,4,1,5),_DevClientCount_Type())
devClientCount.setMaxAccess(_C)
if mibBuilder.loadTexts:devClientCount.setStatus(_B)
class _DevMeshStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('gateway',0),('repeater',1)))
_DevMeshStatus_Type.__name__=_G
_DevMeshStatus_Object=MibTableColumn
devMeshStatus=_DevMeshStatus_Object((1,3,6,1,4,1,29671,1,1,4,1,6),_DevMeshStatus_Type())
devMeshStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:devMeshStatus.setStatus(_B)
_DevPublicIp_Type=IpAddress
_DevPublicIp_Object=MibTableColumn
devPublicIp=_DevPublicIp_Object((1,3,6,1,4,1,29671,1,1,4,1,7),_DevPublicIp_Type())
devPublicIp.setMaxAccess(_C)
if mibBuilder.loadTexts:devPublicIp.setStatus(_B)
_DevSerial_Type=DisplayString
_DevSerial_Object=MibTableColumn
devSerial=_DevSerial_Object((1,3,6,1,4,1,29671,1,1,4,1,8),_DevSerial_Type())
devSerial.setMaxAccess(_C)
if mibBuilder.loadTexts:devSerial.setStatus(_B)
_DevProductCode_Type=DisplayString
_DevProductCode_Object=MibTableColumn
devProductCode=_DevProductCode_Object((1,3,6,1,4,1,29671,1,1,4,1,9),_DevProductCode_Type())
devProductCode.setMaxAccess(_C)
if mibBuilder.loadTexts:devProductCode.setStatus(_B)
_DevProductDescription_Type=DisplayString
_DevProductDescription_Object=MibTableColumn
devProductDescription=_DevProductDescription_Object((1,3,6,1,4,1,29671,1,1,4,1,10),_DevProductDescription_Type())
devProductDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:devProductDescription.setStatus(_B)
_DevNetworkName_Type=DisplayString
_DevNetworkName_Object=MibTableColumn
devNetworkName=_DevNetworkName_Object((1,3,6,1,4,1,29671,1,1,4,1,11),_DevNetworkName_Type())
devNetworkName.setMaxAccess(_C)
if mibBuilder.loadTexts:devNetworkName.setStatus(_B)
_DevLanIp_Type=IpAddress
_DevLanIp_Object=MibScalar
devLanIp=_DevLanIp_Object((1,3,6,1,4,1,29671,1,1,4,1,12),_DevLanIp_Type())
devLanIp.setMaxAccess(_C)
if mibBuilder.loadTexts:devLanIp.setStatus(_B)
_DevSubnet_Type=DisplayString
_DevSubnet_Object=MibScalar
devSubnet=_DevSubnet_Object((1,3,6,1,4,1,29671,1,1,4,1,13),_DevSubnet_Type())
devSubnet.setMaxAccess(_C)
if mibBuilder.loadTexts:devSubnet.setStatus(_B)
_DevCellularStatus_Type=DisplayString
_DevCellularStatus_Object=MibTableColumn
devCellularStatus=_DevCellularStatus_Object((1,3,6,1,4,1,29671,1,1,4,1,14),_DevCellularStatus_Type())
devCellularStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:devCellularStatus.setStatus(_B)
_DevInterfaceTable_Object=MibTable
devInterfaceTable=_DevInterfaceTable_Object((1,3,6,1,4,1,29671,1,1,5))
if mibBuilder.loadTexts:devInterfaceTable.setStatus(_B)
_DevInterfaceEntry_Object=MibTableRow
devInterfaceEntry=_DevInterfaceEntry_Object((1,3,6,1,4,1,29671,1,1,5,1))
devInterfaceEntry.setIndexNames((0,_A,_W),(0,_A,_X))
if mibBuilder.loadTexts:devInterfaceEntry.setStatus(_B)
class _DevInterfaceDevMac_Type(PhysAddress):subtypeSpec=PhysAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
_DevInterfaceDevMac_Type.__name__=_O
_DevInterfaceDevMac_Object=MibScalar
devInterfaceDevMac=_DevInterfaceDevMac_Object((1,3,6,1,4,1,29671,1,1,5,1,1),_DevInterfaceDevMac_Type())
devInterfaceDevMac.setMaxAccess(_C)
if mibBuilder.loadTexts:devInterfaceDevMac.setStatus(_B)
class _DevInterfaceIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_DevInterfaceIndex_Type.__name__=_G
_DevInterfaceIndex_Object=MibScalar
devInterfaceIndex=_DevInterfaceIndex_Object((1,3,6,1,4,1,29671,1,1,5,1,2),_DevInterfaceIndex_Type())
devInterfaceIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:devInterfaceIndex.setStatus(_B)
_DevInterfaceName_Type=DisplayString
_DevInterfaceName_Object=MibScalar
devInterfaceName=_DevInterfaceName_Object((1,3,6,1,4,1,29671,1,1,5,1,3),_DevInterfaceName_Type())
devInterfaceName.setMaxAccess(_C)
if mibBuilder.loadTexts:devInterfaceName.setStatus(_B)
_DevInterfaceSentPkts_Type=Counter32
_DevInterfaceSentPkts_Object=MibScalar
devInterfaceSentPkts=_DevInterfaceSentPkts_Object((1,3,6,1,4,1,29671,1,1,5,1,4),_DevInterfaceSentPkts_Type())
devInterfaceSentPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:devInterfaceSentPkts.setStatus(_B)
_DevInterfaceRecvPkts_Type=Counter32
_DevInterfaceRecvPkts_Object=MibScalar
devInterfaceRecvPkts=_DevInterfaceRecvPkts_Object((1,3,6,1,4,1,29671,1,1,5,1,5),_DevInterfaceRecvPkts_Type())
devInterfaceRecvPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:devInterfaceRecvPkts.setStatus(_B)
_DevInterfaceSentBytes_Type=Counter32
_DevInterfaceSentBytes_Object=MibScalar
devInterfaceSentBytes=_DevInterfaceSentBytes_Object((1,3,6,1,4,1,29671,1,1,5,1,6),_DevInterfaceSentBytes_Type())
devInterfaceSentBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:devInterfaceSentBytes.setStatus(_B)
_DevInterfaceRecvBytes_Type=Counter32
_DevInterfaceRecvBytes_Object=MibScalar
devInterfaceRecvBytes=_DevInterfaceRecvBytes_Object((1,3,6,1,4,1,29671,1,1,5,1,7),_DevInterfaceRecvBytes_Type())
devInterfaceRecvBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:devInterfaceRecvBytes.setStatus(_B)
_DevInterfaceModel_Type=DisplayString
_DevInterfaceModel_Object=MibScalar
devInterfaceModel=_DevInterfaceModel_Object((1,3,6,1,4,1,29671,1,1,5,1,8),_DevInterfaceModel_Type())
devInterfaceModel.setMaxAccess(_C)
if mibBuilder.loadTexts:devInterfaceModel.setStatus(_B)
_DevInterfaceCarrier_Type=DisplayString
_DevInterfaceCarrier_Object=MibScalar
devInterfaceCarrier=_DevInterfaceCarrier_Object((1,3,6,1,4,1,29671,1,1,5,1,9),_DevInterfaceCarrier_Type())
devInterfaceCarrier.setMaxAccess(_C)
if mibBuilder.loadTexts:devInterfaceCarrier.setStatus(_B)
_DevInterfaceDescription_Type=DisplayString
_DevInterfaceDescription_Object=MibScalar
devInterfaceDescription=_DevInterfaceDescription_Object((1,3,6,1,4,1,29671,1,1,5,1,10),_DevInterfaceDescription_Type())
devInterfaceDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:devInterfaceDescription.setStatus(_B)
_DevInterfacePortDescription_Type=DisplayString
_DevInterfacePortDescription_Object=MibScalar
devInterfacePortDescription=_DevInterfacePortDescription_Object((1,3,6,1,4,1,29671,1,1,5,1,11),_DevInterfacePortDescription_Type())
devInterfacePortDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:devInterfacePortDescription.setStatus(_B)
_PowerSupplyNum_Type=DisplayString
_PowerSupplyNum_Object=MibScalar
powerSupplyNum=_PowerSupplyNum_Object((1,3,6,1,4,1,29671,1,1,5,1,12),_PowerSupplyNum_Type())
powerSupplyNum.setMaxAccess(_C)
if mibBuilder.loadTexts:powerSupplyNum.setStatus(_B)
_ActionTaken_Type=DisplayString
_ActionTaken_Object=MibScalar
actionTaken=_ActionTaken_Object((1,3,6,1,4,1,29671,1,1,5,1,13),_ActionTaken_Type())
actionTaken.setMaxAccess(_C)
if mibBuilder.loadTexts:actionTaken.setStatus(_B)
_PortNumber_Type=DisplayString
_PortNumber_Object=MibScalar
portNumber=_PortNumber_Object((1,3,6,1,4,1,29671,1,1,5,1,14),_PortNumber_Type())
portNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:portNumber.setStatus(_B)
_VlanTable_Object=MibTable
vlanTable=_VlanTable_Object((1,3,6,1,4,1,29671,1,1,6))
if mibBuilder.loadTexts:vlanTable.setStatus(_B)
_VlanEntry_Object=MibTableRow
vlanEntry=_VlanEntry_Object((1,3,6,1,4,1,29671,1,1,6,1))
vlanEntry.setIndexNames((0,_A,_L),(0,_A,_I))
if mibBuilder.loadTexts:vlanEntry.setStatus(_B)
_VlanNetworkName_Type=DisplayString
_VlanNetworkName_Object=MibTableColumn
vlanNetworkName=_VlanNetworkName_Object((1,3,6,1,4,1,29671,1,1,6,1,1),_VlanNetworkName_Type())
vlanNetworkName.setMaxAccess(_C)
if mibBuilder.loadTexts:vlanNetworkName.setStatus(_B)
class _VlanNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_VlanNumber_Type.__name__=_G
_VlanNumber_Object=MibTableColumn
vlanNumber=_VlanNumber_Object((1,3,6,1,4,1,29671,1,1,6,1,2),_VlanNumber_Type())
vlanNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:vlanNumber.setStatus(_B)
_VlanName_Type=DisplayString
_VlanName_Object=MibScalar
vlanName=_VlanName_Object((1,3,6,1,4,1,29671,1,1,6,1,3),_VlanName_Type())
vlanName.setMaxAccess(_C)
if mibBuilder.loadTexts:vlanName.setStatus(_B)
_Traps_ObjectIdentity=ObjectIdentity
traps=_Traps_ObjectIdentity((1,3,6,1,4,1,29671,1,1,7))
_MerakiProducts_ObjectIdentity=ObjectIdentity
merakiProducts=_MerakiProducts_ObjectIdentity((1,3,6,1,4,1,29671,2))
_Mini_ObjectIdentity=ObjectIdentity
mini=_Mini_ObjectIdentity((1,3,6,1,4,1,29671,2,1))
_Id2_ObjectIdentity=ObjectIdentity
id2=_Id2_ObjectIdentity((1,3,6,1,4,1,29671,2,2))
_Wpg_ObjectIdentity=ObjectIdentity
wpg=_Wpg_ObjectIdentity((1,3,6,1,4,1,29671,2,3))
_Od1_ObjectIdentity=ObjectIdentity
od1=_Od1_ObjectIdentity((1,3,6,1,4,1,29671,2,4))
_Od2_ObjectIdentity=ObjectIdentity
od2=_Od2_ObjectIdentity((1,3,6,1,4,1,29671,2,5))
_Od3_ObjectIdentity=ObjectIdentity
od3=_Od3_ObjectIdentity((1,3,6,1,4,1,29671,2,6))
_Mo1_ObjectIdentity=ObjectIdentity
mo1=_Mo1_ObjectIdentity((1,3,6,1,4,1,29671,2,7))
_Sol_ObjectIdentity=ObjectIdentity
sol=_Sol_ObjectIdentity((1,3,6,1,4,1,29671,2,8))
_Lr1_ObjectIdentity=ObjectIdentity
lr1=_Lr1_ObjectIdentity((1,3,6,1,4,1,29671,2,9))
_Mr11_ObjectIdentity=ObjectIdentity
mr11=_Mr11_ObjectIdentity((1,3,6,1,4,1,29671,2,10))
_Mr12_ObjectIdentity=ObjectIdentity
mr12=_Mr12_ObjectIdentity((1,3,6,1,4,1,29671,2,11))
_Mr14_ObjectIdentity=ObjectIdentity
mr14=_Mr14_ObjectIdentity((1,3,6,1,4,1,29671,2,12))
_Mr16_ObjectIdentity=ObjectIdentity
mr16=_Mr16_ObjectIdentity((1,3,6,1,4,1,29671,2,13))
_Mr24_ObjectIdentity=ObjectIdentity
mr24=_Mr24_ObjectIdentity((1,3,6,1,4,1,29671,2,14))
_Mr62_ObjectIdentity=ObjectIdentity
mr62=_Mr62_ObjectIdentity((1,3,6,1,4,1,29671,2,15))
_Mr66_ObjectIdentity=ObjectIdentity
mr66=_Mr66_ObjectIdentity((1,3,6,1,4,1,29671,2,16))
_Mr34_ObjectIdentity=ObjectIdentity
mr34=_Mr34_ObjectIdentity((1,3,6,1,4,1,29671,2,17))
_Mr18_ObjectIdentity=ObjectIdentity
mr18=_Mr18_ObjectIdentity((1,3,6,1,4,1,29671,2,18))
_Mr26_ObjectIdentity=ObjectIdentity
mr26=_Mr26_ObjectIdentity((1,3,6,1,4,1,29671,2,19))
_Mr32_ObjectIdentity=ObjectIdentity
mr32=_Mr32_ObjectIdentity((1,3,6,1,4,1,29671,2,20))
_Mr72_ObjectIdentity=ObjectIdentity
mr72=_Mr72_ObjectIdentity((1,3,6,1,4,1,29671,2,21))
_Mr42_ObjectIdentity=ObjectIdentity
mr42=_Mr42_ObjectIdentity((1,3,6,1,4,1,29671,2,22))
_Mr52_ObjectIdentity=ObjectIdentity
mr52=_Mr52_ObjectIdentity((1,3,6,1,4,1,29671,2,23))
_Mr53_ObjectIdentity=ObjectIdentity
mr53=_Mr53_ObjectIdentity((1,3,6,1,4,1,29671,2,24))
_Mr84_ObjectIdentity=ObjectIdentity
mr84=_Mr84_ObjectIdentity((1,3,6,1,4,1,29671,2,25))
_Mr30h_ObjectIdentity=ObjectIdentity
mr30h=_Mr30h_ObjectIdentity((1,3,6,1,4,1,29671,2,26))
_Mr33_ObjectIdentity=ObjectIdentity
mr33=_Mr33_ObjectIdentity((1,3,6,1,4,1,29671,2,27))
_Mr74_ObjectIdentity=ObjectIdentity
mr74=_Mr74_ObjectIdentity((1,3,6,1,4,1,29671,2,28))
_Mr70_ObjectIdentity=ObjectIdentity
mr70=_Mr70_ObjectIdentity((1,3,6,1,4,1,29671,2,29))
_Mr45_ObjectIdentity=ObjectIdentity
mr45=_Mr45_ObjectIdentity((1,3,6,1,4,1,29671,2,30))
_Mr55_ObjectIdentity=ObjectIdentity
mr55=_Mr55_ObjectIdentity((1,3,6,1,4,1,29671,2,31))
_Mr42e_ObjectIdentity=ObjectIdentity
mr42e=_Mr42e_ObjectIdentity((1,3,6,1,4,1,29671,2,32))
_Mr53e_ObjectIdentity=ObjectIdentity
mr53e=_Mr53e_ObjectIdentity((1,3,6,1,4,1,29671,2,33))
_Mr20_ObjectIdentity=ObjectIdentity
mr20=_Mr20_ObjectIdentity((1,3,6,1,4,1,29671,2,34))
_Gr10_ObjectIdentity=ObjectIdentity
gr10=_Gr10_ObjectIdentity((1,3,6,1,4,1,29671,2,35))
_Gr60_ObjectIdentity=ObjectIdentity
gr60=_Gr60_ObjectIdentity((1,3,6,1,4,1,29671,2,36))
_Mr36_ObjectIdentity=ObjectIdentity
mr36=_Mr36_ObjectIdentity((1,3,6,1,4,1,29671,2,37))
_Mr46_ObjectIdentity=ObjectIdentity
mr46=_Mr46_ObjectIdentity((1,3,6,1,4,1,29671,2,38))
_Mr46e_ObjectIdentity=ObjectIdentity
mr46e=_Mr46e_ObjectIdentity((1,3,6,1,4,1,29671,2,39))
_Mr56_ObjectIdentity=ObjectIdentity
mr56=_Mr56_ObjectIdentity((1,3,6,1,4,1,29671,2,40))
_Mr76_ObjectIdentity=ObjectIdentity
mr76=_Mr76_ObjectIdentity((1,3,6,1,4,1,29671,2,41))
_Mr86_ObjectIdentity=ObjectIdentity
mr86=_Mr86_ObjectIdentity((1,3,6,1,4,1,29671,2,42))
_Mr44_ObjectIdentity=ObjectIdentity
mr44=_Mr44_ObjectIdentity((1,3,6,1,4,1,29671,2,43))
_Mr36h_ObjectIdentity=ObjectIdentity
mr36h=_Mr36h_ObjectIdentity((1,3,6,1,4,1,29671,2,44))
_Z1_ObjectIdentity=ObjectIdentity
z1=_Z1_ObjectIdentity((1,3,6,1,4,1,29671,2,100))
_Mx70_ObjectIdentity=ObjectIdentity
mx70=_Mx70_ObjectIdentity((1,3,6,1,4,1,29671,2,101))
_Mx60_ObjectIdentity=ObjectIdentity
mx60=_Mx60_ObjectIdentity((1,3,6,1,4,1,29671,2,102))
_Mx60w_ObjectIdentity=ObjectIdentity
mx60w=_Mx60w_ObjectIdentity((1,3,6,1,4,1,29671,2,102))
_Mx80_ObjectIdentity=ObjectIdentity
mx80=_Mx80_ObjectIdentity((1,3,6,1,4,1,29671,2,102))
_Mx90_ObjectIdentity=ObjectIdentity
mx90=_Mx90_ObjectIdentity((1,3,6,1,4,1,29671,2,103))
_Mx400_ObjectIdentity=ObjectIdentity
mx400=_Mx400_ObjectIdentity((1,3,6,1,4,1,29671,2,104))
_Mx600_ObjectIdentity=ObjectIdentity
mx600=_Mx600_ObjectIdentity((1,3,6,1,4,1,29671,2,105))
_Mx100_ObjectIdentity=ObjectIdentity
mx100=_Mx100_ObjectIdentity((1,3,6,1,4,1,29671,2,106))
_Mx64_ObjectIdentity=ObjectIdentity
mx64=_Mx64_ObjectIdentity((1,3,6,1,4,1,29671,2,107))
_Mx64w_ObjectIdentity=ObjectIdentity
mx64w=_Mx64w_ObjectIdentity((1,3,6,1,4,1,29671,2,108))
_Mx84_ObjectIdentity=ObjectIdentity
mx84=_Mx84_ObjectIdentity((1,3,6,1,4,1,29671,2,109))
_Mx65_ObjectIdentity=ObjectIdentity
mx65=_Mx65_ObjectIdentity((1,3,6,1,4,1,29671,2,110))
_Mx65w_ObjectIdentity=ObjectIdentity
mx65w=_Mx65w_ObjectIdentity((1,3,6,1,4,1,29671,2,111))
_Mx250_ObjectIdentity=ObjectIdentity
mx250=_Mx250_ObjectIdentity((1,3,6,1,4,1,29671,2,112))
_Mx450_ObjectIdentity=ObjectIdentity
mx450=_Mx450_ObjectIdentity((1,3,6,1,4,1,29671,2,113))
_Z3_ObjectIdentity=ObjectIdentity
z3=_Z3_ObjectIdentity((1,3,6,1,4,1,29671,2,116))
_Gx20_ObjectIdentity=ObjectIdentity
gx20=_Gx20_ObjectIdentity((1,3,6,1,4,1,29671,2,117))
_Mx67_ObjectIdentity=ObjectIdentity
mx67=_Mx67_ObjectIdentity((1,3,6,1,4,1,29671,2,118))
_Mx67w_ObjectIdentity=ObjectIdentity
mx67w=_Mx67w_ObjectIdentity((1,3,6,1,4,1,29671,2,119))
_Mx67c_ObjectIdentity=ObjectIdentity
mx67c=_Mx67c_ObjectIdentity((1,3,6,1,4,1,29671,2,120))
_Mx68_ObjectIdentity=ObjectIdentity
mx68=_Mx68_ObjectIdentity((1,3,6,1,4,1,29671,2,121))
_Mx68w_ObjectIdentity=ObjectIdentity
mx68w=_Mx68w_ObjectIdentity((1,3,6,1,4,1,29671,2,122))
_Mx68cw_ObjectIdentity=ObjectIdentity
mx68cw=_Mx68cw_ObjectIdentity((1,3,6,1,4,1,29671,2,123))
_Z3c_ObjectIdentity=ObjectIdentity
z3c=_Z3c_ObjectIdentity((1,3,6,1,4,1,29671,2,124))
_Mx85_ObjectIdentity=ObjectIdentity
mx85=_Mx85_ObjectIdentity((1,3,6,1,4,1,29671,2,125))
_Mx75_ObjectIdentity=ObjectIdentity
mx75=_Mx75_ObjectIdentity((1,3,6,1,4,1,29671,2,126))
_Mx95_ObjectIdentity=ObjectIdentity
mx95=_Mx95_ObjectIdentity((1,3,6,1,4,1,29671,2,127))
_Mx105_ObjectIdentity=ObjectIdentity
mx105=_Mx105_ObjectIdentity((1,3,6,1,4,1,29671,2,128))
_MerakiVM10_ObjectIdentity=ObjectIdentity
merakiVM10=_MerakiVM10_ObjectIdentity((1,3,6,1,4,1,29671,2,200))
_Ms22_ObjectIdentity=ObjectIdentity
ms22=_Ms22_ObjectIdentity((1,3,6,1,4,1,29671,2,300))
_Ms22p_ObjectIdentity=ObjectIdentity
ms22p=_Ms22p_ObjectIdentity((1,3,6,1,4,1,29671,2,301))
_Ms42_ObjectIdentity=ObjectIdentity
ms42=_Ms42_ObjectIdentity((1,3,6,1,4,1,29671,2,302))
_Ms42p_ObjectIdentity=ObjectIdentity
ms42p=_Ms42p_ObjectIdentity((1,3,6,1,4,1,29671,2,303))
_Ms220_8_ObjectIdentity=ObjectIdentity
ms220_8=_Ms220_8_ObjectIdentity((1,3,6,1,4,1,29671,2,304))
_Ms220_8p_ObjectIdentity=ObjectIdentity
ms220_8p=_Ms220_8p_ObjectIdentity((1,3,6,1,4,1,29671,2,305))
_Ms220_24_ObjectIdentity=ObjectIdentity
ms220_24=_Ms220_24_ObjectIdentity((1,3,6,1,4,1,29671,2,306))
_Ms220_24p_ObjectIdentity=ObjectIdentity
ms220_24p=_Ms220_24p_ObjectIdentity((1,3,6,1,4,1,29671,2,307))
_Ms220_48_ObjectIdentity=ObjectIdentity
ms220_48=_Ms220_48_ObjectIdentity((1,3,6,1,4,1,29671,2,308))
_Ms220_48lp_ObjectIdentity=ObjectIdentity
ms220_48lp=_Ms220_48lp_ObjectIdentity((1,3,6,1,4,1,29671,2,309))
_Ms220_48fp_ObjectIdentity=ObjectIdentity
ms220_48fp=_Ms220_48fp_ObjectIdentity((1,3,6,1,4,1,29671,2,310))
_Ms320_24_ObjectIdentity=ObjectIdentity
ms320_24=_Ms320_24_ObjectIdentity((1,3,6,1,4,1,29671,2,311))
_Ms320_24p_ObjectIdentity=ObjectIdentity
ms320_24p=_Ms320_24p_ObjectIdentity((1,3,6,1,4,1,29671,2,312))
_Ms320_48_ObjectIdentity=ObjectIdentity
ms320_48=_Ms320_48_ObjectIdentity((1,3,6,1,4,1,29671,2,313))
_Ms320_48lp_ObjectIdentity=ObjectIdentity
ms320_48lp=_Ms320_48lp_ObjectIdentity((1,3,6,1,4,1,29671,2,314))
_Ms320_48fp_ObjectIdentity=ObjectIdentity
ms320_48fp=_Ms320_48fp_ObjectIdentity((1,3,6,1,4,1,29671,2,315))
_Ms420_24_ObjectIdentity=ObjectIdentity
ms420_24=_Ms420_24_ObjectIdentity((1,3,6,1,4,1,29671,2,316))
_Ms420_48_ObjectIdentity=ObjectIdentity
ms420_48=_Ms420_48_ObjectIdentity((1,3,6,1,4,1,29671,2,317))
_Ms350_24_ObjectIdentity=ObjectIdentity
ms350_24=_Ms350_24_ObjectIdentity((1,3,6,1,4,1,29671,2,318))
_Ms350_24p_ObjectIdentity=ObjectIdentity
ms350_24p=_Ms350_24p_ObjectIdentity((1,3,6,1,4,1,29671,2,319))
_Ms350_48_ObjectIdentity=ObjectIdentity
ms350_48=_Ms350_48_ObjectIdentity((1,3,6,1,4,1,29671,2,320))
_Ms350_48lp_ObjectIdentity=ObjectIdentity
ms350_48lp=_Ms350_48lp_ObjectIdentity((1,3,6,1,4,1,29671,2,321))
_Ms350_48fp_ObjectIdentity=ObjectIdentity
ms350_48fp=_Ms350_48fp_ObjectIdentity((1,3,6,1,4,1,29671,2,322))
_Ms410_16_ObjectIdentity=ObjectIdentity
ms410_16=_Ms410_16_ObjectIdentity((1,3,6,1,4,1,29671,2,323))
_Ms410_32_ObjectIdentity=ObjectIdentity
ms410_32=_Ms410_32_ObjectIdentity((1,3,6,1,4,1,29671,2,324))
_Ms425_16_ObjectIdentity=ObjectIdentity
ms425_16=_Ms425_16_ObjectIdentity((1,3,6,1,4,1,29671,2,325))
_Ms425_32_ObjectIdentity=ObjectIdentity
ms425_32=_Ms425_32_ObjectIdentity((1,3,6,1,4,1,29671,2,326))
_Ms350_24x_ObjectIdentity=ObjectIdentity
ms350_24x=_Ms350_24x_ObjectIdentity((1,3,6,1,4,1,29671,2,327))
_Ms225_24_ObjectIdentity=ObjectIdentity
ms225_24=_Ms225_24_ObjectIdentity((1,3,6,1,4,1,29671,2,328))
_Ms225_24p_ObjectIdentity=ObjectIdentity
ms225_24p=_Ms225_24p_ObjectIdentity((1,3,6,1,4,1,29671,2,329))
_Ms225_48_ObjectIdentity=ObjectIdentity
ms225_48=_Ms225_48_ObjectIdentity((1,3,6,1,4,1,29671,2,330))
_Ms225_48lp_ObjectIdentity=ObjectIdentity
ms225_48lp=_Ms225_48lp_ObjectIdentity((1,3,6,1,4,1,29671,2,331))
_Ms225_48fp_ObjectIdentity=ObjectIdentity
ms225_48fp=_Ms225_48fp_ObjectIdentity((1,3,6,1,4,1,29671,2,332))
_Ms250_24_ObjectIdentity=ObjectIdentity
ms250_24=_Ms250_24_ObjectIdentity((1,3,6,1,4,1,29671,2,333))
_Ms250_24p_ObjectIdentity=ObjectIdentity
ms250_24p=_Ms250_24p_ObjectIdentity((1,3,6,1,4,1,29671,2,334))
_Ms250_48_ObjectIdentity=ObjectIdentity
ms250_48=_Ms250_48_ObjectIdentity((1,3,6,1,4,1,29671,2,335))
_Ms250_48lp_ObjectIdentity=ObjectIdentity
ms250_48lp=_Ms250_48lp_ObjectIdentity((1,3,6,1,4,1,29671,2,336))
_Ms250_48fp_ObjectIdentity=ObjectIdentity
ms250_48fp=_Ms250_48fp_ObjectIdentity((1,3,6,1,4,1,29671,2,337))
_Ms120_8_ObjectIdentity=ObjectIdentity
ms120_8=_Ms120_8_ObjectIdentity((1,3,6,1,4,1,29671,2,338))
_Ms120_8lp_ObjectIdentity=ObjectIdentity
ms120_8lp=_Ms120_8lp_ObjectIdentity((1,3,6,1,4,1,29671,2,339))
_Ms120_8fp_ObjectIdentity=ObjectIdentity
ms120_8fp=_Ms120_8fp_ObjectIdentity((1,3,6,1,4,1,29671,2,340))
_Ms120_24_ObjectIdentity=ObjectIdentity
ms120_24=_Ms120_24_ObjectIdentity((1,3,6,1,4,1,29671,2,341))
_Ms120_24p_ObjectIdentity=ObjectIdentity
ms120_24p=_Ms120_24p_ObjectIdentity((1,3,6,1,4,1,29671,2,342))
_Ms120_48_ObjectIdentity=ObjectIdentity
ms120_48=_Ms120_48_ObjectIdentity((1,3,6,1,4,1,29671,2,343))
_Ms120_48lp_ObjectIdentity=ObjectIdentity
ms120_48lp=_Ms120_48lp_ObjectIdentity((1,3,6,1,4,1,29671,2,344))
_Ms210_24_ObjectIdentity=ObjectIdentity
ms210_24=_Ms210_24_ObjectIdentity((1,3,6,1,4,1,29671,2,345))
_Ms210_24p_ObjectIdentity=ObjectIdentity
ms210_24p=_Ms210_24p_ObjectIdentity((1,3,6,1,4,1,29671,2,346))
_Ms210_48_ObjectIdentity=ObjectIdentity
ms210_48=_Ms210_48_ObjectIdentity((1,3,6,1,4,1,29671,2,347))
_Ms210_48lp_ObjectIdentity=ObjectIdentity
ms210_48lp=_Ms210_48lp_ObjectIdentity((1,3,6,1,4,1,29671,2,348))
_Ms210_48fp_ObjectIdentity=ObjectIdentity
ms210_48fp=_Ms210_48fp_ObjectIdentity((1,3,6,1,4,1,29671,2,349))
_Ms120_48fp_ObjectIdentity=ObjectIdentity
ms120_48fp=_Ms120_48fp_ObjectIdentity((1,3,6,1,4,1,29671,2,356))
_Ms355_24x_ObjectIdentity=ObjectIdentity
ms355_24x=_Ms355_24x_ObjectIdentity((1,3,6,1,4,1,29671,2,357))
_Ms355_24x2_ObjectIdentity=ObjectIdentity
ms355_24x2=_Ms355_24x2_ObjectIdentity((1,3,6,1,4,1,29671,2,358))
_Ms355_48x_ObjectIdentity=ObjectIdentity
ms355_48x=_Ms355_48x_ObjectIdentity((1,3,6,1,4,1,29671,2,359))
_Ms355_48x2_ObjectIdentity=ObjectIdentity
ms355_48x2=_Ms355_48x2_ObjectIdentity((1,3,6,1,4,1,29671,2,360))
_Ms450_12_ObjectIdentity=ObjectIdentity
ms450_12=_Ms450_12_ObjectIdentity((1,3,6,1,4,1,29671,2,361))
_Ms390_24_ObjectIdentity=ObjectIdentity
ms390_24=_Ms390_24_ObjectIdentity((1,3,6,1,4,1,29671,2,362))
_Ms390_24p_ObjectIdentity=ObjectIdentity
ms390_24p=_Ms390_24p_ObjectIdentity((1,3,6,1,4,1,29671,2,363))
_Ms390_24u_ObjectIdentity=ObjectIdentity
ms390_24u=_Ms390_24u_ObjectIdentity((1,3,6,1,4,1,29671,2,364))
_Ms390_24ux_ObjectIdentity=ObjectIdentity
ms390_24ux=_Ms390_24ux_ObjectIdentity((1,3,6,1,4,1,29671,2,365))
_Ms390_48_ObjectIdentity=ObjectIdentity
ms390_48=_Ms390_48_ObjectIdentity((1,3,6,1,4,1,29671,2,366))
_Ms390_48p_ObjectIdentity=ObjectIdentity
ms390_48p=_Ms390_48p_ObjectIdentity((1,3,6,1,4,1,29671,2,367))
_Ms390_48u_ObjectIdentity=ObjectIdentity
ms390_48u=_Ms390_48u_ObjectIdentity((1,3,6,1,4,1,29671,2,368))
_Ms390_48ux_ObjectIdentity=ObjectIdentity
ms390_48ux=_Ms390_48ux_ObjectIdentity((1,3,6,1,4,1,29671,2,369))
_Ms390_48ux2_ObjectIdentity=ObjectIdentity
ms390_48ux2=_Ms390_48ux2_ObjectIdentity((1,3,6,1,4,1,29671,2,370))
_Ms125_24_ObjectIdentity=ObjectIdentity
ms125_24=_Ms125_24_ObjectIdentity((1,3,6,1,4,1,29671,2,371))
_Ms125_24p_ObjectIdentity=ObjectIdentity
ms125_24p=_Ms125_24p_ObjectIdentity((1,3,6,1,4,1,29671,2,372))
_Ms125_48_ObjectIdentity=ObjectIdentity
ms125_48=_Ms125_48_ObjectIdentity((1,3,6,1,4,1,29671,2,373))
_Ms125_48lp_ObjectIdentity=ObjectIdentity
ms125_48lp=_Ms125_48lp_ObjectIdentity((1,3,6,1,4,1,29671,2,374))
_Ms125_48fp_ObjectIdentity=ObjectIdentity
ms125_48fp=_Ms125_48fp_ObjectIdentity((1,3,6,1,4,1,29671,2,375))
_MerakiObjects_ObjectIdentity=ObjectIdentity
merakiObjects=_MerakiObjects_ObjectIdentity((1,3,6,1,4,1,29671,3))
_ChangeDescription_Type=DisplayString
_ChangeDescription_Object=MibScalar
changeDescription=_ChangeDescription_Object((1,3,6,1,4,1,29671,3,1),_ChangeDescription_Type())
changeDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:changeDescription.setStatus(_B)
_LoginEmail_Type=DisplayString
_LoginEmail_Object=MibScalar
loginEmail=_LoginEmail_Object((1,3,6,1,4,1,29671,3,2),_LoginEmail_Type())
loginEmail.setMaxAccess(_C)
if mibBuilder.loadTexts:loginEmail.setStatus(_B)
_LoginResult_Type=DisplayString
_LoginResult_Object=MibScalar
loginResult=_LoginResult_Object((1,3,6,1,4,1,29671,3,3),_LoginResult_Type())
loginResult.setMaxAccess(_C)
if mibBuilder.loadTexts:loginResult.setStatus(_B)
_LoginDescription_Type=DisplayString
_LoginDescription_Object=MibScalar
loginDescription=_LoginDescription_Object((1,3,6,1,4,1,29671,3,4),_LoginDescription_Type())
loginDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:loginDescription.setStatus(_B)
_TunnelDescription_Type=DisplayString
_TunnelDescription_Object=MibScalar
tunnelDescription=_TunnelDescription_Object((1,3,6,1,4,1,29671,3,5),_TunnelDescription_Type())
tunnelDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:tunnelDescription.setStatus(_B)
_Period_Type=DisplayString
_Period_Object=MibScalar
period=_Period_Object((1,3,6,1,4,1,29671,3,6),_Period_Type())
period.setMaxAccess(_C)
if mibBuilder.loadTexts:period.setStatus(_B)
_EndOfHighUsageWindow_Type=DisplayString
_EndOfHighUsageWindow_Object=MibScalar
endOfHighUsageWindow=_EndOfHighUsageWindow_Object((1,3,6,1,4,1,29671,3,7),_EndOfHighUsageWindow_Type())
endOfHighUsageWindow.setMaxAccess(_C)
if mibBuilder.loadTexts:endOfHighUsageWindow.setStatus(_B)
_Threshold_Type=DisplayString
_Threshold_Object=MibScalar
threshold=_Threshold_Object((1,3,6,1,4,1,29671,3,8),_Threshold_Type())
threshold.setMaxAccess(_C)
if mibBuilder.loadTexts:threshold.setStatus(_B)
_Usage_Type=DisplayString
_Usage_Object=MibScalar
usage=_Usage_Object((1,3,6,1,4,1,29671,3,9),_Usage_Type())
usage.setMaxAccess(_C)
if mibBuilder.loadTexts:usage.setStatus(_B)
testTrap=NotificationType((1,3,6,1,4,1,29671,1,1,7,1))
testTrap.setObjects((_A,_D))
if mibBuilder.loadTexts:testTrap.setStatus(_B)
deviceGoesDownTrap=NotificationType((1,3,6,1,4,1,29671,1,1,7,2))
deviceGoesDownTrap.setObjects(*((_A,_E),(_A,_D),(_A,_F)))
if mibBuilder.loadTexts:deviceGoesDownTrap.setStatus(_B)
deviceComesOnline=NotificationType((1,3,6,1,4,1,29671,1,1,7,3))
deviceComesOnline.setObjects(*((_A,_E),(_A,_D),(_A,_F)))
if mibBuilder.loadTexts:deviceComesOnline.setStatus(_B)
foreignAPDetected=NotificationType((1,3,6,1,4,1,29671,1,1,7,4))
foreignAPDetected.setObjects(*((_A,_E),(_A,_D),(_A,_F)))
if mibBuilder.loadTexts:foreignAPDetected.setStatus(_B)
cellularNetworkUp=NotificationType((1,3,6,1,4,1,29671,1,1,7,5))
cellularNetworkUp.setObjects(*((_A,_E),(_A,_D),(_A,_F),(_A,_P),(_A,_Q),(_A,_M)))
if mibBuilder.loadTexts:cellularNetworkUp.setStatus(_B)
cellularNetworkDown=NotificationType((1,3,6,1,4,1,29671,1,1,7,6))
cellularNetworkDown.setObjects(*((_A,_E),(_A,_D),(_A,_F),(_A,_P),(_A,_Q),(_A,_M)))
if mibBuilder.loadTexts:cellularNetworkDown.setStatus(_B)
newDhcpServerAlert=NotificationType((1,3,6,1,4,1,29671,1,1,7,7))
newDhcpServerAlert.setObjects(*((_A,_E),(_A,_D),(_A,_F),(_A,_H),(_A,_R),(_A,_I)))
if mibBuilder.loadTexts:newDhcpServerAlert.setStatus(_B)
noDhcpLeases=NotificationType((1,3,6,1,4,1,29671,1,1,7,8))
noDhcpLeases.setObjects(*((_A,_E),(_A,_D),(_A,_F),(_A,_H),(_A,_I)))
if mibBuilder.loadTexts:noDhcpLeases.setStatus(_B)
uplinkStatusChanged=NotificationType((1,3,6,1,4,1,29671,1,1,7,9))
uplinkStatusChanged.setObjects(*((_A,_E),(_A,_D),(_A,_F),(_A,_M)))
if mibBuilder.loadTexts:uplinkStatusChanged.setStatus(_B)
unreachableDevicesDetected=NotificationType((1,3,6,1,4,1,29671,1,1,7,10))
unreachableDevicesDetected.setObjects(*((_A,_E),(_A,_D)))
if mibBuilder.loadTexts:unreachableDevicesDetected.setStatus(_B)
upcomingFirewallInformationChanges=NotificationType((1,3,6,1,4,1,29671,1,1,7,11))
upcomingFirewallInformationChanges.setObjects(*((_A,_E),(_A,_D)))
if mibBuilder.loadTexts:upcomingFirewallInformationChanges.setStatus(_B)
gatewayToRepeater=NotificationType((1,3,6,1,4,1,29671,1,1,7,12))
gatewayToRepeater.setObjects(*((_A,_E),(_A,_D),(_A,_F)))
if mibBuilder.loadTexts:gatewayToRepeater.setStatus(_B)
ipConflict=NotificationType((1,3,6,1,4,1,29671,1,1,7,13))
ipConflict.setObjects(*((_A,_E),(_A,_D),(_A,_H),(_A,_F)))
if mibBuilder.loadTexts:ipConflict.setStatus(_B)
newSplashSignup=NotificationType((1,3,6,1,4,1,29671,1,1,7,14))
newSplashSignup.setObjects(*((_A,_E),(_A,_D),(_A,_S),(_A,_Y),(_A,_Z)))
if mibBuilder.loadTexts:newSplashSignup.setStatus(_B)
portCableError=NotificationType((1,3,6,1,4,1,29671,1,1,7,15))
portCableError.setObjects(*((_A,_E),(_A,_D),(_A,_F),(_A,_J),(_A,_N)))
if mibBuilder.loadTexts:portCableError.setStatus(_B)
portConnected=NotificationType((1,3,6,1,4,1,29671,1,1,7,16))
portConnected.setObjects(*((_A,_E),(_A,_D),(_A,_F),(_A,_J)))
if mibBuilder.loadTexts:portConnected.setStatus(_B)
portDisconnected=NotificationType((1,3,6,1,4,1,29671,1,1,7,17))
portDisconnected.setObjects(*((_A,_E),(_A,_D),(_A,_F),(_A,_J)))
if mibBuilder.loadTexts:portDisconnected.setStatus(_B)
portSpeedChange=NotificationType((1,3,6,1,4,1,29671,1,1,7,18))
portSpeedChange.setObjects(*((_A,_E),(_A,_D),(_A,_F),(_A,_J),(_A,_N)))
if mibBuilder.loadTexts:portSpeedChange.setStatus(_B)
rogueDhcpServer=NotificationType((1,3,6,1,4,1,29671,1,1,7,19))
rogueDhcpServer.setObjects(*((_A,_E),(_A,_D),(_A,_F),(_A,_R),(_A,_H),(_A,_I)))
if mibBuilder.loadTexts:rogueDhcpServer.setStatus(_B)
settingsChanged=NotificationType((1,3,6,1,4,1,29671,1,1,7,20))
settingsChanged.setObjects(*((_A,_E),(_A,_D),(_A,_a),(_A,_b)))
if mibBuilder.loadTexts:settingsChanged.setStatus(_B)
unreachableRadiusServer=NotificationType((1,3,6,1,4,1,29671,1,1,7,21))
unreachableRadiusServer.setObjects(*((_A,_E),(_A,_D),(_A,_c),(_A,_S),(_A,_H)))
if mibBuilder.loadTexts:unreachableRadiusServer.setStatus(_B)
vpnConnectivityChange=NotificationType((1,3,6,1,4,1,29671,1,1,7,22))
vpnConnectivityChange.setObjects(*((_A,_E),(_A,_D),(_A,_F),(_A,_d),(_A,_T),(_A,_e)))
if mibBuilder.loadTexts:vpnConnectivityChange.setStatus(_B)
warmSpareFailoverDetected=NotificationType((1,3,6,1,4,1,29671,1,1,7,23))
warmSpareFailoverDetected.setObjects(*((_A,_E),(_A,_D),(_A,_F),(_A,_T)))
if mibBuilder.loadTexts:warmSpareFailoverDetected.setStatus(_B)
loginAttempt=NotificationType((1,3,6,1,4,1,29671,1,1,7,24))
loginAttempt.setObjects(*((_A,_E),(_A,_D),(_A,_f),(_A,_g),(_A,_h)))
if mibBuilder.loadTexts:loginAttempt.setStatus(_B)
malwareDetected=NotificationType((1,3,6,1,4,1,29671,1,1,7,25))
malwareDetected.setObjects(*((_A,_E),(_A,_D)))
if mibBuilder.loadTexts:malwareDetected.setStatus(_B)
malwareBlocked=NotificationType((1,3,6,1,4,1,29671,1,1,7,26))
malwareBlocked.setObjects(*((_A,_E),(_A,_D)))
if mibBuilder.loadTexts:malwareBlocked.setStatus(_B)
powerSupplyUp=NotificationType((1,3,6,1,4,1,29671,1,1,7,27))
powerSupplyUp.setObjects(*((_A,_E),(_A,_D),(_A,_F),(_A,_K)))
if mibBuilder.loadTexts:powerSupplyUp.setStatus(_B)
powerSupplyDown=NotificationType((1,3,6,1,4,1,29671,1,1,7,28))
powerSupplyDown.setObjects(*((_A,_E),(_A,_D),(_A,_F),(_A,_K)))
if mibBuilder.loadTexts:powerSupplyDown.setStatus(_B)
redundantPowerSupplyBackup=NotificationType((1,3,6,1,4,1,29671,1,1,7,29))
redundantPowerSupplyBackup.setObjects(*((_A,_E),(_A,_D),(_A,_F),(_A,_K)))
if mibBuilder.loadTexts:redundantPowerSupplyBackup.setStatus(_B)
redundantPowerSupplyBackToPrimary=NotificationType((1,3,6,1,4,1,29671,1,1,7,30))
redundantPowerSupplyBackToPrimary.setObjects(*((_A,_E),(_A,_D),(_A,_F),(_A,_K)))
if mibBuilder.loadTexts:redundantPowerSupplyBackToPrimary.setStatus(_B)
udldError=NotificationType((1,3,6,1,4,1,29671,1,1,7,31))
udldError.setObjects(*((_A,_E),(_A,_D),(_A,_F),(_A,_i),(_A,_N),(_A,_j)))
if mibBuilder.loadTexts:udldError.setStatus(_B)
criticalTemperature=NotificationType((1,3,6,1,4,1,29671,1,1,7,32))
criticalTemperature.setObjects(*((_A,_E),(_A,_D),(_A,_F)))
if mibBuilder.loadTexts:criticalTemperature.setStatus(_B)
usageAlert=NotificationType((1,3,6,1,4,1,29671,1,1,7,33))
usageAlert.setObjects(*((_A,_E),(_A,_D),(_A,_k),(_A,_l),(_A,_m),(_A,'usage')))
if mibBuilder.loadTexts:usageAlert.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'meraki':meraki,'cloudController':cloudController,'organization':organization,_E:organizationName,'networkTable':networkTable,'networkEntry':networkEntry,_L:networkId,_D:networkName,_a:networkAdmin,_d:vpnPeer,'ssidTable':ssidTable,'ssidEntry':ssidEntry,'ssidNetworkName':ssidNetworkName,_V:ssidNumber,_S:ssidName,_Y:userName,_Z:userEmail,_c:radiusServerIp,'radiusServerPort':radiusServerPort,'devTable':devTable,'devEntry':devEntry,_F:devMac,'devName':devName,_T:devStatus,'devContactedAt':devContactedAt,'devClientCount':devClientCount,'devMeshStatus':devMeshStatus,'devPublicIp':devPublicIp,'devSerial':devSerial,'devProductCode':devProductCode,'devProductDescription':devProductDescription,'devNetworkName':devNetworkName,_H:devLanIp,_R:devSubnet,'devCellularStatus':devCellularStatus,'devInterfaceTable':devInterfaceTable,'devInterfaceEntry':devInterfaceEntry,_W:devInterfaceDevMac,_X:devInterfaceIndex,_M:devInterfaceName,'devInterfaceSentPkts':devInterfaceSentPkts,'devInterfaceRecvPkts':devInterfaceRecvPkts,'devInterfaceSentBytes':devInterfaceSentBytes,'devInterfaceRecvBytes':devInterfaceRecvBytes,_P:devInterfaceModel,_Q:devInterfaceCarrier,_J:devInterfaceDescription,_N:devInterfacePortDescription,_K:powerSupplyNum,_j:actionTaken,_i:portNumber,'vlanTable':vlanTable,'vlanEntry':vlanEntry,'vlanNetworkName':vlanNetworkName,_I:vlanNumber,'vlanName':vlanName,'traps':traps,'testTrap':testTrap,'deviceGoesDownTrap':deviceGoesDownTrap,'deviceComesOnline':deviceComesOnline,'foreignAPDetected':foreignAPDetected,'cellularNetworkUp':cellularNetworkUp,'cellularNetworkDown':cellularNetworkDown,'newDhcpServerAlert':newDhcpServerAlert,'noDhcpLeases':noDhcpLeases,'uplinkStatusChanged':uplinkStatusChanged,'unreachableDevicesDetected':unreachableDevicesDetected,'upcomingFirewallInformationChanges':upcomingFirewallInformationChanges,'gatewayToRepeater':gatewayToRepeater,'ipConflict':ipConflict,'newSplashSignup':newSplashSignup,'portCableError':portCableError,'portConnected':portConnected,'portDisconnected':portDisconnected,'portSpeedChange':portSpeedChange,'rogueDhcpServer':rogueDhcpServer,'settingsChanged':settingsChanged,'unreachableRadiusServer':unreachableRadiusServer,'vpnConnectivityChange':vpnConnectivityChange,'warmSpareFailoverDetected':warmSpareFailoverDetected,'loginAttempt':loginAttempt,'malwareDetected':malwareDetected,'malwareBlocked':malwareBlocked,'powerSupplyUp':powerSupplyUp,'powerSupplyDown':powerSupplyDown,'redundantPowerSupplyBackup':redundantPowerSupplyBackup,'redundantPowerSupplyBackToPrimary':redundantPowerSupplyBackToPrimary,'udldError':udldError,'criticalTemperature':criticalTemperature,'usageAlert':usageAlert,'merakiProducts':merakiProducts,'mini':mini,'id2':id2,'wpg':wpg,'od1':od1,'od2':od2,'od3':od3,'mo1':mo1,'sol':sol,'lr1':lr1,'mr11':mr11,'mr12':mr12,'mr14':mr14,'mr16':mr16,'mr24':mr24,'mr62':mr62,'mr66':mr66,'mr34':mr34,'mr18':mr18,'mr26':mr26,'mr32':mr32,'mr72':mr72,'mr42':mr42,'mr52':mr52,'mr53':mr53,'mr84':mr84,'mr30h':mr30h,'mr33':mr33,'mr74':mr74,'mr70':mr70,'mr45':mr45,'mr55':mr55,'mr42e':mr42e,'mr53e':mr53e,'mr20':mr20,'gr10':gr10,'gr60':gr60,'mr36':mr36,'mr46':mr46,'mr46e':mr46e,'mr56':mr56,'mr76':mr76,'mr86':mr86,'mr44':mr44,'mr36h':mr36h,'z1':z1,'mx70':mx70,'mx60':mx60,'mx60w':mx60w,'mx80':mx80,'mx90':mx90,'mx400':mx400,'mx600':mx600,'mx100':mx100,'mx64':mx64,'mx64w':mx64w,'mx84':mx84,'mx65':mx65,'mx65w':mx65w,'mx250':mx250,'mx450':mx450,'z3':z3,'gx20':gx20,'mx67':mx67,'mx67w':mx67w,'mx67c':mx67c,'mx68':mx68,'mx68w':mx68w,'mx68cw':mx68cw,'z3c':z3c,'mx85':mx85,'mx75':mx75,'mx95':mx95,'mx105':mx105,'merakiVM10':merakiVM10,'ms22':ms22,'ms22p':ms22p,'ms42':ms42,'ms42p':ms42p,'ms220-8':ms220_8,'ms220-8p':ms220_8p,'ms220-24':ms220_24,'ms220-24p':ms220_24p,'ms220-48':ms220_48,'ms220-48lp':ms220_48lp,'ms220-48fp':ms220_48fp,'ms320-24':ms320_24,'ms320-24p':ms320_24p,'ms320-48':ms320_48,'ms320-48lp':ms320_48lp,'ms320-48fp':ms320_48fp,'ms420-24':ms420_24,'ms420-48':ms420_48,'ms350-24':ms350_24,'ms350-24p':ms350_24p,'ms350-48':ms350_48,'ms350-48lp':ms350_48lp,'ms350-48fp':ms350_48fp,'ms410-16':ms410_16,'ms410-32':ms410_32,'ms425-16':ms425_16,'ms425-32':ms425_32,'ms350-24x':ms350_24x,'ms225-24':ms225_24,'ms225-24p':ms225_24p,'ms225-48':ms225_48,'ms225-48lp':ms225_48lp,'ms225-48fp':ms225_48fp,'ms250-24':ms250_24,'ms250-24p':ms250_24p,'ms250-48':ms250_48,'ms250-48lp':ms250_48lp,'ms250-48fp':ms250_48fp,'ms120-8':ms120_8,'ms120-8lp':ms120_8lp,'ms120-8fp':ms120_8fp,'ms120-24':ms120_24,'ms120-24p':ms120_24p,'ms120-48':ms120_48,'ms120-48lp':ms120_48lp,'ms210-24':ms210_24,'ms210-24p':ms210_24p,'ms210-48':ms210_48,'ms210-48lp':ms210_48lp,'ms210-48fp':ms210_48fp,'ms120-48fp':ms120_48fp,'ms355-24x':ms355_24x,'ms355-24x2':ms355_24x2,'ms355-48x':ms355_48x,'ms355-48x2':ms355_48x2,'ms450-12':ms450_12,'ms390-24':ms390_24,'ms390-24p':ms390_24p,'ms390-24u':ms390_24u,'ms390-24ux':ms390_24ux,'ms390-48':ms390_48,'ms390-48p':ms390_48p,'ms390-48u':ms390_48u,'ms390-48ux':ms390_48ux,'ms390-48ux2':ms390_48ux2,'ms125-24':ms125_24,'ms125-24p':ms125_24p,'ms125-48':ms125_48,'ms125-48lp':ms125_48lp,'ms125-48fp':ms125_48fp,'merakiObjects':merakiObjects,_b:changeDescription,_f:loginEmail,_g:loginResult,_h:loginDescription,_e:tunnelDescription,_k:period,_l:endOfHighUsageWindow,_m:threshold,'usage':usage})