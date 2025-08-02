_L='remain'
_K='tpDhcpServerBindingIp'
_J='tpDhcpServerBindIpAddr'
_I='tpDhcpServerAddrPoolNetwork'
_H='tpDhcpServerUnusedStartIp'
_G='TPLINK-DHCPSERVER-MIB'
_F='read-write'
_E='Integer32'
_D='OctetString'
_C='read-only'
_B='read-create'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_D,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
tplinkMgmt,=mibBuilder.importSymbols('TPLINK-MIB','tplinkMgmt')
TPRowStatus,=mibBuilder.importSymbols('TPLINK-TC-MIB','TPRowStatus')
tplinkDhcpServerMIB=ModuleIdentity((1,3,6,1,4,1,11863,6,38))
if mibBuilder.loadTexts:tplinkDhcpServerMIB.setRevisions(('2012-11-29 00:00',))
_TplinkDhcpServerMIBObjects_ObjectIdentity=ObjectIdentity
tplinkDhcpServerMIBObjects=_TplinkDhcpServerMIBObjects_ObjectIdentity((1,3,6,1,4,1,11863,6,38,1))
class _TpDhcpServerEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('disable',0),('enable',1)))
_TpDhcpServerEnable_Type.__name__=_E
_TpDhcpServerEnable_Object=MibScalar
tpDhcpServerEnable=_TpDhcpServerEnable_Object((1,3,6,1,4,1,11863,6,38,1,1),_TpDhcpServerEnable_Type())
tpDhcpServerEnable.setMaxAccess(_F)
if mibBuilder.loadTexts:tpDhcpServerEnable.setStatus(_A)
class _TpDhcpServerVendorClassId_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_TpDhcpServerVendorClassId_Type.__name__=_D
_TpDhcpServerVendorClassId_Object=MibScalar
tpDhcpServerVendorClassId=_TpDhcpServerVendorClassId_Object((1,3,6,1,4,1,11863,6,38,1,2),_TpDhcpServerVendorClassId_Type())
tpDhcpServerVendorClassId.setMaxAccess(_F)
if mibBuilder.loadTexts:tpDhcpServerVendorClassId.setStatus(_A)
_TpDhcpServerCapwapAcIp_Type=IpAddress
_TpDhcpServerCapwapAcIp_Object=MibScalar
tpDhcpServerCapwapAcIp=_TpDhcpServerCapwapAcIp_Object((1,3,6,1,4,1,11863,6,38,1,3),_TpDhcpServerCapwapAcIp_Type())
tpDhcpServerCapwapAcIp.setMaxAccess(_F)
if mibBuilder.loadTexts:tpDhcpServerCapwapAcIp.setStatus(_A)
_TpDhcpServerUnusedIpTable_Object=MibTable
tpDhcpServerUnusedIpTable=_TpDhcpServerUnusedIpTable_Object((1,3,6,1,4,1,11863,6,38,1,4))
if mibBuilder.loadTexts:tpDhcpServerUnusedIpTable.setStatus(_A)
_TpDhcpServerUnusedIpEntry_Object=MibTableRow
tpDhcpServerUnusedIpEntry=_TpDhcpServerUnusedIpEntry_Object((1,3,6,1,4,1,11863,6,38,1,4,1))
tpDhcpServerUnusedIpEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:tpDhcpServerUnusedIpEntry.setStatus(_A)
_TpDhcpServerUnusedStartIp_Type=IpAddress
_TpDhcpServerUnusedStartIp_Object=MibTableColumn
tpDhcpServerUnusedStartIp=_TpDhcpServerUnusedStartIp_Object((1,3,6,1,4,1,11863,6,38,1,4,1,1),_TpDhcpServerUnusedStartIp_Type())
tpDhcpServerUnusedStartIp.setMaxAccess(_C)
if mibBuilder.loadTexts:tpDhcpServerUnusedStartIp.setStatus(_A)
_TpDhcpServerUnusedEndIp_Type=IpAddress
_TpDhcpServerUnusedEndIp_Object=MibTableColumn
tpDhcpServerUnusedEndIp=_TpDhcpServerUnusedEndIp_Object((1,3,6,1,4,1,11863,6,38,1,4,1,2),_TpDhcpServerUnusedEndIp_Type())
tpDhcpServerUnusedEndIp.setMaxAccess(_B)
if mibBuilder.loadTexts:tpDhcpServerUnusedEndIp.setStatus(_A)
_TpDhcpServerUnusedIpStatus_Type=TPRowStatus
_TpDhcpServerUnusedIpStatus_Object=MibTableColumn
tpDhcpServerUnusedIpStatus=_TpDhcpServerUnusedIpStatus_Object((1,3,6,1,4,1,11863,6,38,1,4,1,3),_TpDhcpServerUnusedIpStatus_Type())
tpDhcpServerUnusedIpStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:tpDhcpServerUnusedIpStatus.setStatus(_A)
_TpDhcpServerAddrPoolTable_Object=MibTable
tpDhcpServerAddrPoolTable=_TpDhcpServerAddrPoolTable_Object((1,3,6,1,4,1,11863,6,38,1,5))
if mibBuilder.loadTexts:tpDhcpServerAddrPoolTable.setStatus(_A)
_TpDhcpServerAddrPoolEntry_Object=MibTableRow
tpDhcpServerAddrPoolEntry=_TpDhcpServerAddrPoolEntry_Object((1,3,6,1,4,1,11863,6,38,1,5,1))
tpDhcpServerAddrPoolEntry.setIndexNames((0,_G,_I))
if mibBuilder.loadTexts:tpDhcpServerAddrPoolEntry.setStatus(_A)
class _TpDhcpServerAddrPoolName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_TpDhcpServerAddrPoolName_Type.__name__=_D
_TpDhcpServerAddrPoolName_Object=MibTableColumn
tpDhcpServerAddrPoolName=_TpDhcpServerAddrPoolName_Object((1,3,6,1,4,1,11863,6,38,1,5,1,1),_TpDhcpServerAddrPoolName_Type())
tpDhcpServerAddrPoolName.setMaxAccess(_B)
if mibBuilder.loadTexts:tpDhcpServerAddrPoolName.setStatus(_A)
_TpDhcpServerAddrPoolNetwork_Type=IpAddress
_TpDhcpServerAddrPoolNetwork_Object=MibTableColumn
tpDhcpServerAddrPoolNetwork=_TpDhcpServerAddrPoolNetwork_Object((1,3,6,1,4,1,11863,6,38,1,5,1,2),_TpDhcpServerAddrPoolNetwork_Type())
tpDhcpServerAddrPoolNetwork.setMaxAccess(_B)
if mibBuilder.loadTexts:tpDhcpServerAddrPoolNetwork.setStatus(_A)
_TpDhcpServerAddrPoolSubnetMask_Type=IpAddress
_TpDhcpServerAddrPoolSubnetMask_Object=MibTableColumn
tpDhcpServerAddrPoolSubnetMask=_TpDhcpServerAddrPoolSubnetMask_Object((1,3,6,1,4,1,11863,6,38,1,5,1,3),_TpDhcpServerAddrPoolSubnetMask_Type())
tpDhcpServerAddrPoolSubnetMask.setMaxAccess(_B)
if mibBuilder.loadTexts:tpDhcpServerAddrPoolSubnetMask.setStatus(_A)
_TpDhcpServerAddrPoolRentTime_Type=Integer32
_TpDhcpServerAddrPoolRentTime_Object=MibTableColumn
tpDhcpServerAddrPoolRentTime=_TpDhcpServerAddrPoolRentTime_Object((1,3,6,1,4,1,11863,6,38,1,5,1,4),_TpDhcpServerAddrPoolRentTime_Type())
tpDhcpServerAddrPoolRentTime.setMaxAccess(_B)
if mibBuilder.loadTexts:tpDhcpServerAddrPoolRentTime.setStatus(_A)
_TpDhcpServerAddrPoolGateWayA_Type=IpAddress
_TpDhcpServerAddrPoolGateWayA_Object=MibTableColumn
tpDhcpServerAddrPoolGateWayA=_TpDhcpServerAddrPoolGateWayA_Object((1,3,6,1,4,1,11863,6,38,1,5,1,5),_TpDhcpServerAddrPoolGateWayA_Type())
tpDhcpServerAddrPoolGateWayA.setMaxAccess(_B)
if mibBuilder.loadTexts:tpDhcpServerAddrPoolGateWayA.setStatus(_A)
_TpDhcpServerAddrPoolGateWayB_Type=IpAddress
_TpDhcpServerAddrPoolGateWayB_Object=MibTableColumn
tpDhcpServerAddrPoolGateWayB=_TpDhcpServerAddrPoolGateWayB_Object((1,3,6,1,4,1,11863,6,38,1,5,1,6),_TpDhcpServerAddrPoolGateWayB_Type())
tpDhcpServerAddrPoolGateWayB.setMaxAccess(_B)
if mibBuilder.loadTexts:tpDhcpServerAddrPoolGateWayB.setStatus(_A)
_TpDhcpServerAddrPoolGateWayC_Type=IpAddress
_TpDhcpServerAddrPoolGateWayC_Object=MibTableColumn
tpDhcpServerAddrPoolGateWayC=_TpDhcpServerAddrPoolGateWayC_Object((1,3,6,1,4,1,11863,6,38,1,5,1,7),_TpDhcpServerAddrPoolGateWayC_Type())
tpDhcpServerAddrPoolGateWayC.setMaxAccess(_B)
if mibBuilder.loadTexts:tpDhcpServerAddrPoolGateWayC.setStatus(_A)
_TpDhcpServerAddrPoolGateWayD_Type=IpAddress
_TpDhcpServerAddrPoolGateWayD_Object=MibTableColumn
tpDhcpServerAddrPoolGateWayD=_TpDhcpServerAddrPoolGateWayD_Object((1,3,6,1,4,1,11863,6,38,1,5,1,8),_TpDhcpServerAddrPoolGateWayD_Type())
tpDhcpServerAddrPoolGateWayD.setMaxAccess(_B)
if mibBuilder.loadTexts:tpDhcpServerAddrPoolGateWayD.setStatus(_A)
_TpDhcpServerAddrPoolGateWayE_Type=IpAddress
_TpDhcpServerAddrPoolGateWayE_Object=MibTableColumn
tpDhcpServerAddrPoolGateWayE=_TpDhcpServerAddrPoolGateWayE_Object((1,3,6,1,4,1,11863,6,38,1,5,1,9),_TpDhcpServerAddrPoolGateWayE_Type())
tpDhcpServerAddrPoolGateWayE.setMaxAccess(_B)
if mibBuilder.loadTexts:tpDhcpServerAddrPoolGateWayE.setStatus(_A)
_TpDhcpServerAddrPoolGateWayF_Type=IpAddress
_TpDhcpServerAddrPoolGateWayF_Object=MibTableColumn
tpDhcpServerAddrPoolGateWayF=_TpDhcpServerAddrPoolGateWayF_Object((1,3,6,1,4,1,11863,6,38,1,5,1,10),_TpDhcpServerAddrPoolGateWayF_Type())
tpDhcpServerAddrPoolGateWayF.setMaxAccess(_B)
if mibBuilder.loadTexts:tpDhcpServerAddrPoolGateWayF.setStatus(_A)
_TpDhcpServerAddrPoolGateWayG_Type=IpAddress
_TpDhcpServerAddrPoolGateWayG_Object=MibTableColumn
tpDhcpServerAddrPoolGateWayG=_TpDhcpServerAddrPoolGateWayG_Object((1,3,6,1,4,1,11863,6,38,1,5,1,11),_TpDhcpServerAddrPoolGateWayG_Type())
tpDhcpServerAddrPoolGateWayG.setMaxAccess(_B)
if mibBuilder.loadTexts:tpDhcpServerAddrPoolGateWayG.setStatus(_A)
_TpDhcpServerAddrPoolGateWayH_Type=IpAddress
_TpDhcpServerAddrPoolGateWayH_Object=MibTableColumn
tpDhcpServerAddrPoolGateWayH=_TpDhcpServerAddrPoolGateWayH_Object((1,3,6,1,4,1,11863,6,38,1,5,1,12),_TpDhcpServerAddrPoolGateWayH_Type())
tpDhcpServerAddrPoolGateWayH.setMaxAccess(_B)
if mibBuilder.loadTexts:tpDhcpServerAddrPoolGateWayH.setStatus(_A)
_TpDhcpServerAddrPoolDnsA_Type=IpAddress
_TpDhcpServerAddrPoolDnsA_Object=MibTableColumn
tpDhcpServerAddrPoolDnsA=_TpDhcpServerAddrPoolDnsA_Object((1,3,6,1,4,1,11863,6,38,1,5,1,13),_TpDhcpServerAddrPoolDnsA_Type())
tpDhcpServerAddrPoolDnsA.setMaxAccess(_B)
if mibBuilder.loadTexts:tpDhcpServerAddrPoolDnsA.setStatus(_A)
_TpDhcpServerAddrPoolDnsB_Type=IpAddress
_TpDhcpServerAddrPoolDnsB_Object=MibTableColumn
tpDhcpServerAddrPoolDnsB=_TpDhcpServerAddrPoolDnsB_Object((1,3,6,1,4,1,11863,6,38,1,5,1,14),_TpDhcpServerAddrPoolDnsB_Type())
tpDhcpServerAddrPoolDnsB.setMaxAccess(_B)
if mibBuilder.loadTexts:tpDhcpServerAddrPoolDnsB.setStatus(_A)
_TpDhcpServerAddrPoolDnsC_Type=IpAddress
_TpDhcpServerAddrPoolDnsC_Object=MibTableColumn
tpDhcpServerAddrPoolDnsC=_TpDhcpServerAddrPoolDnsC_Object((1,3,6,1,4,1,11863,6,38,1,5,1,15),_TpDhcpServerAddrPoolDnsC_Type())
tpDhcpServerAddrPoolDnsC.setMaxAccess(_B)
if mibBuilder.loadTexts:tpDhcpServerAddrPoolDnsC.setStatus(_A)
_TpDhcpServerAddrPoolDnsD_Type=IpAddress
_TpDhcpServerAddrPoolDnsD_Object=MibTableColumn
tpDhcpServerAddrPoolDnsD=_TpDhcpServerAddrPoolDnsD_Object((1,3,6,1,4,1,11863,6,38,1,5,1,16),_TpDhcpServerAddrPoolDnsD_Type())
tpDhcpServerAddrPoolDnsD.setMaxAccess(_B)
if mibBuilder.loadTexts:tpDhcpServerAddrPoolDnsD.setStatus(_A)
_TpDhcpServerAddrPoolDnsE_Type=IpAddress
_TpDhcpServerAddrPoolDnsE_Object=MibTableColumn
tpDhcpServerAddrPoolDnsE=_TpDhcpServerAddrPoolDnsE_Object((1,3,6,1,4,1,11863,6,38,1,5,1,17),_TpDhcpServerAddrPoolDnsE_Type())
tpDhcpServerAddrPoolDnsE.setMaxAccess(_B)
if mibBuilder.loadTexts:tpDhcpServerAddrPoolDnsE.setStatus(_A)
_TpDhcpServerAddrPoolDnsF_Type=IpAddress
_TpDhcpServerAddrPoolDnsF_Object=MibTableColumn
tpDhcpServerAddrPoolDnsF=_TpDhcpServerAddrPoolDnsF_Object((1,3,6,1,4,1,11863,6,38,1,5,1,18),_TpDhcpServerAddrPoolDnsF_Type())
tpDhcpServerAddrPoolDnsF.setMaxAccess(_B)
if mibBuilder.loadTexts:tpDhcpServerAddrPoolDnsF.setStatus(_A)
_TpDhcpServerAddrPoolDnsG_Type=IpAddress
_TpDhcpServerAddrPoolDnsG_Object=MibTableColumn
tpDhcpServerAddrPoolDnsG=_TpDhcpServerAddrPoolDnsG_Object((1,3,6,1,4,1,11863,6,38,1,5,1,19),_TpDhcpServerAddrPoolDnsG_Type())
tpDhcpServerAddrPoolDnsG.setMaxAccess(_B)
if mibBuilder.loadTexts:tpDhcpServerAddrPoolDnsG.setStatus(_A)
_TpDhcpServerAddrPoolDnsH_Type=IpAddress
_TpDhcpServerAddrPoolDnsH_Object=MibTableColumn
tpDhcpServerAddrPoolDnsH=_TpDhcpServerAddrPoolDnsH_Object((1,3,6,1,4,1,11863,6,38,1,5,1,20),_TpDhcpServerAddrPoolDnsH_Type())
tpDhcpServerAddrPoolDnsH.setMaxAccess(_B)
if mibBuilder.loadTexts:tpDhcpServerAddrPoolDnsH.setStatus(_A)
_TpDhcpServerAddrPoolNBNServerA_Type=IpAddress
_TpDhcpServerAddrPoolNBNServerA_Object=MibTableColumn
tpDhcpServerAddrPoolNBNServerA=_TpDhcpServerAddrPoolNBNServerA_Object((1,3,6,1,4,1,11863,6,38,1,5,1,21),_TpDhcpServerAddrPoolNBNServerA_Type())
tpDhcpServerAddrPoolNBNServerA.setMaxAccess(_B)
if mibBuilder.loadTexts:tpDhcpServerAddrPoolNBNServerA.setStatus(_A)
_TpDhcpServerAddrPoolNBNServerB_Type=IpAddress
_TpDhcpServerAddrPoolNBNServerB_Object=MibTableColumn
tpDhcpServerAddrPoolNBNServerB=_TpDhcpServerAddrPoolNBNServerB_Object((1,3,6,1,4,1,11863,6,38,1,5,1,22),_TpDhcpServerAddrPoolNBNServerB_Type())
tpDhcpServerAddrPoolNBNServerB.setMaxAccess(_B)
if mibBuilder.loadTexts:tpDhcpServerAddrPoolNBNServerB.setStatus(_A)
_TpDhcpServerAddrPoolNBNServerC_Type=IpAddress
_TpDhcpServerAddrPoolNBNServerC_Object=MibTableColumn
tpDhcpServerAddrPoolNBNServerC=_TpDhcpServerAddrPoolNBNServerC_Object((1,3,6,1,4,1,11863,6,38,1,5,1,23),_TpDhcpServerAddrPoolNBNServerC_Type())
tpDhcpServerAddrPoolNBNServerC.setMaxAccess(_B)
if mibBuilder.loadTexts:tpDhcpServerAddrPoolNBNServerC.setStatus(_A)
_TpDhcpServerAddrPoolNBNServerD_Type=IpAddress
_TpDhcpServerAddrPoolNBNServerD_Object=MibTableColumn
tpDhcpServerAddrPoolNBNServerD=_TpDhcpServerAddrPoolNBNServerD_Object((1,3,6,1,4,1,11863,6,38,1,5,1,24),_TpDhcpServerAddrPoolNBNServerD_Type())
tpDhcpServerAddrPoolNBNServerD.setMaxAccess(_B)
if mibBuilder.loadTexts:tpDhcpServerAddrPoolNBNServerD.setStatus(_A)
_TpDhcpServerAddrPoolNBNServerE_Type=IpAddress
_TpDhcpServerAddrPoolNBNServerE_Object=MibTableColumn
tpDhcpServerAddrPoolNBNServerE=_TpDhcpServerAddrPoolNBNServerE_Object((1,3,6,1,4,1,11863,6,38,1,5,1,25),_TpDhcpServerAddrPoolNBNServerE_Type())
tpDhcpServerAddrPoolNBNServerE.setMaxAccess(_B)
if mibBuilder.loadTexts:tpDhcpServerAddrPoolNBNServerE.setStatus(_A)
_TpDhcpServerAddrPoolNBNServerF_Type=IpAddress
_TpDhcpServerAddrPoolNBNServerF_Object=MibTableColumn
tpDhcpServerAddrPoolNBNServerF=_TpDhcpServerAddrPoolNBNServerF_Object((1,3,6,1,4,1,11863,6,38,1,5,1,26),_TpDhcpServerAddrPoolNBNServerF_Type())
tpDhcpServerAddrPoolNBNServerF.setMaxAccess(_B)
if mibBuilder.loadTexts:tpDhcpServerAddrPoolNBNServerF.setStatus(_A)
_TpDhcpServerAddrPoolNBNServerG_Type=IpAddress
_TpDhcpServerAddrPoolNBNServerG_Object=MibTableColumn
tpDhcpServerAddrPoolNBNServerG=_TpDhcpServerAddrPoolNBNServerG_Object((1,3,6,1,4,1,11863,6,38,1,5,1,27),_TpDhcpServerAddrPoolNBNServerG_Type())
tpDhcpServerAddrPoolNBNServerG.setMaxAccess(_B)
if mibBuilder.loadTexts:tpDhcpServerAddrPoolNBNServerG.setStatus(_A)
_TpDhcpServerAddrPoolNBNServerH_Type=IpAddress
_TpDhcpServerAddrPoolNBNServerH_Object=MibTableColumn
tpDhcpServerAddrPoolNBNServerH=_TpDhcpServerAddrPoolNBNServerH_Object((1,3,6,1,4,1,11863,6,38,1,5,1,28),_TpDhcpServerAddrPoolNBNServerH_Type())
tpDhcpServerAddrPoolNBNServerH.setMaxAccess(_B)
if mibBuilder.loadTexts:tpDhcpServerAddrPoolNBNServerH.setStatus(_A)
class _TpDhcpServerAddrPoolNetbiosNodeType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,4,8)));namedValues=NamedValues(*(('none',0),('broadcast',1),('peer-to-peer',2),('mixed',4),('hybrid',8)))
_TpDhcpServerAddrPoolNetbiosNodeType_Type.__name__=_E
_TpDhcpServerAddrPoolNetbiosNodeType_Object=MibTableColumn
tpDhcpServerAddrPoolNetbiosNodeType=_TpDhcpServerAddrPoolNetbiosNodeType_Object((1,3,6,1,4,1,11863,6,38,1,5,1,29),_TpDhcpServerAddrPoolNetbiosNodeType_Type())
tpDhcpServerAddrPoolNetbiosNodeType.setMaxAccess(_B)
if mibBuilder.loadTexts:tpDhcpServerAddrPoolNetbiosNodeType.setStatus(_A)
_TpDhcpServerAddrPoolNextServer_Type=IpAddress
_TpDhcpServerAddrPoolNextServer_Object=MibTableColumn
tpDhcpServerAddrPoolNextServer=_TpDhcpServerAddrPoolNextServer_Object((1,3,6,1,4,1,11863,6,38,1,5,1,30),_TpDhcpServerAddrPoolNextServer_Type())
tpDhcpServerAddrPoolNextServer.setMaxAccess(_B)
if mibBuilder.loadTexts:tpDhcpServerAddrPoolNextServer.setStatus(_A)
class _TpDhcpServerAddrPoolDomainName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,200))
_TpDhcpServerAddrPoolDomainName_Type.__name__=_D
_TpDhcpServerAddrPoolDomainName_Object=MibTableColumn
tpDhcpServerAddrPoolDomainName=_TpDhcpServerAddrPoolDomainName_Object((1,3,6,1,4,1,11863,6,38,1,5,1,31),_TpDhcpServerAddrPoolDomainName_Type())
tpDhcpServerAddrPoolDomainName.setMaxAccess(_B)
if mibBuilder.loadTexts:tpDhcpServerAddrPoolDomainName.setStatus(_A)
class _TpDhcpServerAddrPoolBootfile_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_TpDhcpServerAddrPoolBootfile_Type.__name__=_D
_TpDhcpServerAddrPoolBootfile_Object=MibTableColumn
tpDhcpServerAddrPoolBootfile=_TpDhcpServerAddrPoolBootfile_Object((1,3,6,1,4,1,11863,6,38,1,5,1,32),_TpDhcpServerAddrPoolBootfile_Type())
tpDhcpServerAddrPoolBootfile.setMaxAccess(_B)
if mibBuilder.loadTexts:tpDhcpServerAddrPoolBootfile.setStatus(_A)
_TpDhcpServerAddrPoolStatus_Type=TPRowStatus
_TpDhcpServerAddrPoolStatus_Object=MibTableColumn
tpDhcpServerAddrPoolStatus=_TpDhcpServerAddrPoolStatus_Object((1,3,6,1,4,1,11863,6,38,1,5,1,33),_TpDhcpServerAddrPoolStatus_Type())
tpDhcpServerAddrPoolStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:tpDhcpServerAddrPoolStatus.setStatus(_A)
_TpDhcpServerStaticBindTable_Object=MibTable
tpDhcpServerStaticBindTable=_TpDhcpServerStaticBindTable_Object((1,3,6,1,4,1,11863,6,38,1,6))
if mibBuilder.loadTexts:tpDhcpServerStaticBindTable.setStatus(_A)
_TpDhcpServerStaticBindEntry_Object=MibTableRow
tpDhcpServerStaticBindEntry=_TpDhcpServerStaticBindEntry_Object((1,3,6,1,4,1,11863,6,38,1,6,1))
tpDhcpServerStaticBindEntry.setIndexNames((0,_G,_J))
if mibBuilder.loadTexts:tpDhcpServerStaticBindEntry.setStatus(_A)
class _TpDhcpServerStaticAddrPoolName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_TpDhcpServerStaticAddrPoolName_Type.__name__=_D
_TpDhcpServerStaticAddrPoolName_Object=MibTableColumn
tpDhcpServerStaticAddrPoolName=_TpDhcpServerStaticAddrPoolName_Object((1,3,6,1,4,1,11863,6,38,1,6,1,1),_TpDhcpServerStaticAddrPoolName_Type())
tpDhcpServerStaticAddrPoolName.setMaxAccess(_B)
if mibBuilder.loadTexts:tpDhcpServerStaticAddrPoolName.setStatus(_A)
_TpDhcpServerBindIpAddr_Type=IpAddress
_TpDhcpServerBindIpAddr_Object=MibTableColumn
tpDhcpServerBindIpAddr=_TpDhcpServerBindIpAddr_Object((1,3,6,1,4,1,11863,6,38,1,6,1,2),_TpDhcpServerBindIpAddr_Type())
tpDhcpServerBindIpAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:tpDhcpServerBindIpAddr.setStatus(_A)
class _TpDhcpServerStaticClientId_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,200))
_TpDhcpServerStaticClientId_Type.__name__=_D
_TpDhcpServerStaticClientId_Object=MibTableColumn
tpDhcpServerStaticClientId=_TpDhcpServerStaticClientId_Object((1,3,6,1,4,1,11863,6,38,1,6,1,3),_TpDhcpServerStaticClientId_Type())
tpDhcpServerStaticClientId.setMaxAccess(_B)
if mibBuilder.loadTexts:tpDhcpServerStaticClientId.setStatus(_A)
class _TpDhcpServerMacAddr_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_TpDhcpServerMacAddr_Type.__name__=_D
_TpDhcpServerMacAddr_Object=MibTableColumn
tpDhcpServerMacAddr=_TpDhcpServerMacAddr_Object((1,3,6,1,4,1,11863,6,38,1,6,1,4),_TpDhcpServerMacAddr_Type())
tpDhcpServerMacAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:tpDhcpServerMacAddr.setStatus(_A)
class _TpDhcpServerHardwareType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(-2,0,1,6)));namedValues=NamedValues(*(('ascii',-2),('hex',0),('ethernet',1),('ieee802',6)))
_TpDhcpServerHardwareType_Type.__name__=_E
_TpDhcpServerHardwareType_Object=MibTableColumn
tpDhcpServerHardwareType=_TpDhcpServerHardwareType_Object((1,3,6,1,4,1,11863,6,38,1,6,1,5),_TpDhcpServerHardwareType_Type())
tpDhcpServerHardwareType.setMaxAccess(_B)
if mibBuilder.loadTexts:tpDhcpServerHardwareType.setStatus(_A)
_TpDhcpServerStaticBindStatus_Type=TPRowStatus
_TpDhcpServerStaticBindStatus_Object=MibTableColumn
tpDhcpServerStaticBindStatus=_TpDhcpServerStaticBindStatus_Object((1,3,6,1,4,1,11863,6,38,1,6,1,6),_TpDhcpServerStaticBindStatus_Type())
tpDhcpServerStaticBindStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:tpDhcpServerStaticBindStatus.setStatus(_A)
_TpDhcpServerBindingTable_Object=MibTable
tpDhcpServerBindingTable=_TpDhcpServerBindingTable_Object((1,3,6,1,4,1,11863,6,38,1,7))
if mibBuilder.loadTexts:tpDhcpServerBindingTable.setStatus(_A)
_TpDhcpServerBindingEntry_Object=MibTableRow
tpDhcpServerBindingEntry=_TpDhcpServerBindingEntry_Object((1,3,6,1,4,1,11863,6,38,1,7,1))
tpDhcpServerBindingEntry.setIndexNames((0,_G,_K))
if mibBuilder.loadTexts:tpDhcpServerBindingEntry.setStatus(_A)
_TpDhcpServerBindingIp_Type=IpAddress
_TpDhcpServerBindingIp_Object=MibTableColumn
tpDhcpServerBindingIp=_TpDhcpServerBindingIp_Object((1,3,6,1,4,1,11863,6,38,1,7,1,1),_TpDhcpServerBindingIp_Type())
tpDhcpServerBindingIp.setMaxAccess(_C)
if mibBuilder.loadTexts:tpDhcpServerBindingIp.setStatus(_A)
class _TpDhcpServerBindingClientId_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,200))
_TpDhcpServerBindingClientId_Type.__name__=_D
_TpDhcpServerBindingClientId_Object=MibTableColumn
tpDhcpServerBindingClientId=_TpDhcpServerBindingClientId_Object((1,3,6,1,4,1,11863,6,38,1,7,1,2),_TpDhcpServerBindingClientId_Type())
tpDhcpServerBindingClientId.setMaxAccess(_C)
if mibBuilder.loadTexts:tpDhcpServerBindingClientId.setStatus(_A)
class _TpDhcpServerBindingMac_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_TpDhcpServerBindingMac_Type.__name__=_D
_TpDhcpServerBindingMac_Object=MibTableColumn
tpDhcpServerBindingMac=_TpDhcpServerBindingMac_Object((1,3,6,1,4,1,11863,6,38,1,7,1,3),_TpDhcpServerBindingMac_Type())
tpDhcpServerBindingMac.setMaxAccess(_C)
if mibBuilder.loadTexts:tpDhcpServerBindingMac.setStatus(_A)
class _TpDhcpServerBindingType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('automatic',0),('manual',1)))
_TpDhcpServerBindingType_Type.__name__=_E
_TpDhcpServerBindingType_Object=MibTableColumn
tpDhcpServerBindingType=_TpDhcpServerBindingType_Object((1,3,6,1,4,1,11863,6,38,1,7,1,4),_TpDhcpServerBindingType_Type())
tpDhcpServerBindingType.setMaxAccess(_C)
if mibBuilder.loadTexts:tpDhcpServerBindingType.setStatus(_A)
class _TpDhcpServerBindingRemainTime_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_TpDhcpServerBindingRemainTime_Type.__name__=_D
_TpDhcpServerBindingRemainTime_Object=MibTableColumn
tpDhcpServerBindingRemainTime=_TpDhcpServerBindingRemainTime_Object((1,3,6,1,4,1,11863,6,38,1,7,1,5),_TpDhcpServerBindingRemainTime_Type())
tpDhcpServerBindingRemainTime.setMaxAccess(_C)
if mibBuilder.loadTexts:tpDhcpServerBindingRemainTime.setStatus(_A)
_TpDhcpServerBindingStatus_Type=TPRowStatus
_TpDhcpServerBindingStatus_Object=MibTableColumn
tpDhcpServerBindingStatus=_TpDhcpServerBindingStatus_Object((1,3,6,1,4,1,11863,6,38,1,7,1,6),_TpDhcpServerBindingStatus_Type())
tpDhcpServerBindingStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:tpDhcpServerBindingStatus.setStatus(_A)
class _TpDhcpServerBindingClear_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_L,0),('clear',1)))
_TpDhcpServerBindingClear_Type.__name__=_E
_TpDhcpServerBindingClear_Object=MibScalar
tpDhcpServerBindingClear=_TpDhcpServerBindingClear_Object((1,3,6,1,4,1,11863,6,38,1,8),_TpDhcpServerBindingClear_Type())
tpDhcpServerBindingClear.setMaxAccess(_F)
if mibBuilder.loadTexts:tpDhcpServerBindingClear.setStatus(_A)
_TpDhcpServerStatistics_ObjectIdentity=ObjectIdentity
tpDhcpServerStatistics=_TpDhcpServerStatistics_ObjectIdentity((1,3,6,1,4,1,11863,6,38,1,9))
_TpDhcpServerStatisticsBootRequest_Type=Counter64
_TpDhcpServerStatisticsBootRequest_Object=MibScalar
tpDhcpServerStatisticsBootRequest=_TpDhcpServerStatisticsBootRequest_Object((1,3,6,1,4,1,11863,6,38,1,9,1),_TpDhcpServerStatisticsBootRequest_Type())
tpDhcpServerStatisticsBootRequest.setMaxAccess(_C)
if mibBuilder.loadTexts:tpDhcpServerStatisticsBootRequest.setStatus(_A)
_TpDhcpServerStatisticsDiscover_Type=Counter64
_TpDhcpServerStatisticsDiscover_Object=MibScalar
tpDhcpServerStatisticsDiscover=_TpDhcpServerStatisticsDiscover_Object((1,3,6,1,4,1,11863,6,38,1,9,2),_TpDhcpServerStatisticsDiscover_Type())
tpDhcpServerStatisticsDiscover.setMaxAccess(_C)
if mibBuilder.loadTexts:tpDhcpServerStatisticsDiscover.setStatus(_A)
_TpDhcpServerStatisticsRequest_Type=Counter64
_TpDhcpServerStatisticsRequest_Object=MibScalar
tpDhcpServerStatisticsRequest=_TpDhcpServerStatisticsRequest_Object((1,3,6,1,4,1,11863,6,38,1,9,3),_TpDhcpServerStatisticsRequest_Type())
tpDhcpServerStatisticsRequest.setMaxAccess(_C)
if mibBuilder.loadTexts:tpDhcpServerStatisticsRequest.setStatus(_A)
_TpDhcpServerStatisticsDecline_Type=Counter64
_TpDhcpServerStatisticsDecline_Object=MibScalar
tpDhcpServerStatisticsDecline=_TpDhcpServerStatisticsDecline_Object((1,3,6,1,4,1,11863,6,38,1,9,4),_TpDhcpServerStatisticsDecline_Type())
tpDhcpServerStatisticsDecline.setMaxAccess(_C)
if mibBuilder.loadTexts:tpDhcpServerStatisticsDecline.setStatus(_A)
_TpDhcpServerStatisticsRelease_Type=Counter64
_TpDhcpServerStatisticsRelease_Object=MibScalar
tpDhcpServerStatisticsRelease=_TpDhcpServerStatisticsRelease_Object((1,3,6,1,4,1,11863,6,38,1,9,5),_TpDhcpServerStatisticsRelease_Type())
tpDhcpServerStatisticsRelease.setMaxAccess(_C)
if mibBuilder.loadTexts:tpDhcpServerStatisticsRelease.setStatus(_A)
_TpDhcpServerStatisticsInform_Type=Counter64
_TpDhcpServerStatisticsInform_Object=MibScalar
tpDhcpServerStatisticsInform=_TpDhcpServerStatisticsInform_Object((1,3,6,1,4,1,11863,6,38,1,9,6),_TpDhcpServerStatisticsInform_Type())
tpDhcpServerStatisticsInform.setMaxAccess(_C)
if mibBuilder.loadTexts:tpDhcpServerStatisticsInform.setStatus(_A)
_TpDhcpServerStatisticsBootReply_Type=Counter64
_TpDhcpServerStatisticsBootReply_Object=MibScalar
tpDhcpServerStatisticsBootReply=_TpDhcpServerStatisticsBootReply_Object((1,3,6,1,4,1,11863,6,38,1,9,7),_TpDhcpServerStatisticsBootReply_Type())
tpDhcpServerStatisticsBootReply.setMaxAccess(_C)
if mibBuilder.loadTexts:tpDhcpServerStatisticsBootReply.setStatus(_A)
_TpDhcpServerStatisticsOffer_Type=Counter64
_TpDhcpServerStatisticsOffer_Object=MibScalar
tpDhcpServerStatisticsOffer=_TpDhcpServerStatisticsOffer_Object((1,3,6,1,4,1,11863,6,38,1,9,8),_TpDhcpServerStatisticsOffer_Type())
tpDhcpServerStatisticsOffer.setMaxAccess(_C)
if mibBuilder.loadTexts:tpDhcpServerStatisticsOffer.setStatus(_A)
_TpDhcpServerStatisticsAck_Type=Counter64
_TpDhcpServerStatisticsAck_Object=MibScalar
tpDhcpServerStatisticsAck=_TpDhcpServerStatisticsAck_Object((1,3,6,1,4,1,11863,6,38,1,9,9),_TpDhcpServerStatisticsAck_Type())
tpDhcpServerStatisticsAck.setMaxAccess(_C)
if mibBuilder.loadTexts:tpDhcpServerStatisticsAck.setStatus(_A)
_TpDhcpServerStatisticsNak_Type=Counter64
_TpDhcpServerStatisticsNak_Object=MibScalar
tpDhcpServerStatisticsNak=_TpDhcpServerStatisticsNak_Object((1,3,6,1,4,1,11863,6,38,1,9,10),_TpDhcpServerStatisticsNak_Type())
tpDhcpServerStatisticsNak.setMaxAccess(_C)
if mibBuilder.loadTexts:tpDhcpServerStatisticsNak.setStatus(_A)
class _TpDhcpServerStatisticsClear_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_L,0),('clear',1)))
_TpDhcpServerStatisticsClear_Type.__name__=_E
_TpDhcpServerStatisticsClear_Object=MibScalar
tpDhcpServerStatisticsClear=_TpDhcpServerStatisticsClear_Object((1,3,6,1,4,1,11863,6,38,1,9,11),_TpDhcpServerStatisticsClear_Type())
tpDhcpServerStatisticsClear.setMaxAccess(_F)
if mibBuilder.loadTexts:tpDhcpServerStatisticsClear.setStatus(_A)
class _TpDhcpServerPingPackets_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10))
_TpDhcpServerPingPackets_Type.__name__=_E
_TpDhcpServerPingPackets_Object=MibScalar
tpDhcpServerPingPackets=_TpDhcpServerPingPackets_Object((1,3,6,1,4,1,11863,6,38,1,10),_TpDhcpServerPingPackets_Type())
tpDhcpServerPingPackets.setMaxAccess(_F)
if mibBuilder.loadTexts:tpDhcpServerPingPackets.setStatus(_A)
class _TpDhcpServerPingTimeout_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(100,10000))
_TpDhcpServerPingTimeout_Type.__name__=_E
_TpDhcpServerPingTimeout_Object=MibScalar
tpDhcpServerPingTimeout=_TpDhcpServerPingTimeout_Object((1,3,6,1,4,1,11863,6,38,1,11),_TpDhcpServerPingTimeout_Type())
tpDhcpServerPingTimeout.setMaxAccess(_F)
if mibBuilder.loadTexts:tpDhcpServerPingTimeout.setStatus(_A)
_TplinkDhcpServerNotifications_ObjectIdentity=ObjectIdentity
tplinkDhcpServerNotifications=_TplinkDhcpServerNotifications_ObjectIdentity((1,3,6,1,4,1,11863,6,38,2))
mibBuilder.exportSymbols(_G,**{'tplinkDhcpServerMIB':tplinkDhcpServerMIB,'tplinkDhcpServerMIBObjects':tplinkDhcpServerMIBObjects,'tpDhcpServerEnable':tpDhcpServerEnable,'tpDhcpServerVendorClassId':tpDhcpServerVendorClassId,'tpDhcpServerCapwapAcIp':tpDhcpServerCapwapAcIp,'tpDhcpServerUnusedIpTable':tpDhcpServerUnusedIpTable,'tpDhcpServerUnusedIpEntry':tpDhcpServerUnusedIpEntry,_H:tpDhcpServerUnusedStartIp,'tpDhcpServerUnusedEndIp':tpDhcpServerUnusedEndIp,'tpDhcpServerUnusedIpStatus':tpDhcpServerUnusedIpStatus,'tpDhcpServerAddrPoolTable':tpDhcpServerAddrPoolTable,'tpDhcpServerAddrPoolEntry':tpDhcpServerAddrPoolEntry,'tpDhcpServerAddrPoolName':tpDhcpServerAddrPoolName,_I:tpDhcpServerAddrPoolNetwork,'tpDhcpServerAddrPoolSubnetMask':tpDhcpServerAddrPoolSubnetMask,'tpDhcpServerAddrPoolRentTime':tpDhcpServerAddrPoolRentTime,'tpDhcpServerAddrPoolGateWayA':tpDhcpServerAddrPoolGateWayA,'tpDhcpServerAddrPoolGateWayB':tpDhcpServerAddrPoolGateWayB,'tpDhcpServerAddrPoolGateWayC':tpDhcpServerAddrPoolGateWayC,'tpDhcpServerAddrPoolGateWayD':tpDhcpServerAddrPoolGateWayD,'tpDhcpServerAddrPoolGateWayE':tpDhcpServerAddrPoolGateWayE,'tpDhcpServerAddrPoolGateWayF':tpDhcpServerAddrPoolGateWayF,'tpDhcpServerAddrPoolGateWayG':tpDhcpServerAddrPoolGateWayG,'tpDhcpServerAddrPoolGateWayH':tpDhcpServerAddrPoolGateWayH,'tpDhcpServerAddrPoolDnsA':tpDhcpServerAddrPoolDnsA,'tpDhcpServerAddrPoolDnsB':tpDhcpServerAddrPoolDnsB,'tpDhcpServerAddrPoolDnsC':tpDhcpServerAddrPoolDnsC,'tpDhcpServerAddrPoolDnsD':tpDhcpServerAddrPoolDnsD,'tpDhcpServerAddrPoolDnsE':tpDhcpServerAddrPoolDnsE,'tpDhcpServerAddrPoolDnsF':tpDhcpServerAddrPoolDnsF,'tpDhcpServerAddrPoolDnsG':tpDhcpServerAddrPoolDnsG,'tpDhcpServerAddrPoolDnsH':tpDhcpServerAddrPoolDnsH,'tpDhcpServerAddrPoolNBNServerA':tpDhcpServerAddrPoolNBNServerA,'tpDhcpServerAddrPoolNBNServerB':tpDhcpServerAddrPoolNBNServerB,'tpDhcpServerAddrPoolNBNServerC':tpDhcpServerAddrPoolNBNServerC,'tpDhcpServerAddrPoolNBNServerD':tpDhcpServerAddrPoolNBNServerD,'tpDhcpServerAddrPoolNBNServerE':tpDhcpServerAddrPoolNBNServerE,'tpDhcpServerAddrPoolNBNServerF':tpDhcpServerAddrPoolNBNServerF,'tpDhcpServerAddrPoolNBNServerG':tpDhcpServerAddrPoolNBNServerG,'tpDhcpServerAddrPoolNBNServerH':tpDhcpServerAddrPoolNBNServerH,'tpDhcpServerAddrPoolNetbiosNodeType':tpDhcpServerAddrPoolNetbiosNodeType,'tpDhcpServerAddrPoolNextServer':tpDhcpServerAddrPoolNextServer,'tpDhcpServerAddrPoolDomainName':tpDhcpServerAddrPoolDomainName,'tpDhcpServerAddrPoolBootfile':tpDhcpServerAddrPoolBootfile,'tpDhcpServerAddrPoolStatus':tpDhcpServerAddrPoolStatus,'tpDhcpServerStaticBindTable':tpDhcpServerStaticBindTable,'tpDhcpServerStaticBindEntry':tpDhcpServerStaticBindEntry,'tpDhcpServerStaticAddrPoolName':tpDhcpServerStaticAddrPoolName,_J:tpDhcpServerBindIpAddr,'tpDhcpServerStaticClientId':tpDhcpServerStaticClientId,'tpDhcpServerMacAddr':tpDhcpServerMacAddr,'tpDhcpServerHardwareType':tpDhcpServerHardwareType,'tpDhcpServerStaticBindStatus':tpDhcpServerStaticBindStatus,'tpDhcpServerBindingTable':tpDhcpServerBindingTable,'tpDhcpServerBindingEntry':tpDhcpServerBindingEntry,_K:tpDhcpServerBindingIp,'tpDhcpServerBindingClientId':tpDhcpServerBindingClientId,'tpDhcpServerBindingMac':tpDhcpServerBindingMac,'tpDhcpServerBindingType':tpDhcpServerBindingType,'tpDhcpServerBindingRemainTime':tpDhcpServerBindingRemainTime,'tpDhcpServerBindingStatus':tpDhcpServerBindingStatus,'tpDhcpServerBindingClear':tpDhcpServerBindingClear,'tpDhcpServerStatistics':tpDhcpServerStatistics,'tpDhcpServerStatisticsBootRequest':tpDhcpServerStatisticsBootRequest,'tpDhcpServerStatisticsDiscover':tpDhcpServerStatisticsDiscover,'tpDhcpServerStatisticsRequest':tpDhcpServerStatisticsRequest,'tpDhcpServerStatisticsDecline':tpDhcpServerStatisticsDecline,'tpDhcpServerStatisticsRelease':tpDhcpServerStatisticsRelease,'tpDhcpServerStatisticsInform':tpDhcpServerStatisticsInform,'tpDhcpServerStatisticsBootReply':tpDhcpServerStatisticsBootReply,'tpDhcpServerStatisticsOffer':tpDhcpServerStatisticsOffer,'tpDhcpServerStatisticsAck':tpDhcpServerStatisticsAck,'tpDhcpServerStatisticsNak':tpDhcpServerStatisticsNak,'tpDhcpServerStatisticsClear':tpDhcpServerStatisticsClear,'tpDhcpServerPingPackets':tpDhcpServerPingPackets,'tpDhcpServerPingTimeout':tpDhcpServerPingTimeout,'tplinkDhcpServerNotifications':tplinkDhcpServerNotifications})