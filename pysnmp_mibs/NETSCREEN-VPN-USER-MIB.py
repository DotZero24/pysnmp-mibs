_J='nsVpnAILUsrIndex'
_I='nsVpnManualKeyUsrIndex'
_H='nsVpnUsrDialupGrpIndex'
_G='yes'
_F='null'
_E='NETSCREEN-VPN-USER-MIB'
_D='DisplayString'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
netscreenVpn,netscreenVpnMibModule=mibBuilder.importSymbols('NETSCREEN-SMI','netscreenVpn','netscreenVpnMibModule')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_D,'PhysAddress','TextualConvention')
netscreenUserMibModule=ModuleIdentity((1,3,6,1,4,1,3224,4,0,10))
if mibBuilder.loadTexts:netscreenUserMibModule.setRevisions(('2004-05-03 00:00','2004-03-03 00:00','2003-11-13 00:00','2002-05-05 00:00','2001-05-14 00:00'))
_NsVpnUser_ObjectIdentity=ObjectIdentity
nsVpnUser=_NsVpnUser_ObjectIdentity((1,3,6,1,4,1,3224,4,10))
_NsVpnUsrDialupGrpTable_Object=MibTable
nsVpnUsrDialupGrpTable=_NsVpnUsrDialupGrpTable_Object((1,3,6,1,4,1,3224,4,10,1))
if mibBuilder.loadTexts:nsVpnUsrDialupGrpTable.setStatus(_A)
_NsVpnUsrDialupGrpEntry_Object=MibTableRow
nsVpnUsrDialupGrpEntry=_NsVpnUsrDialupGrpEntry_Object((1,3,6,1,4,1,3224,4,10,1,1))
nsVpnUsrDialupGrpEntry.setIndexNames((0,_E,_H))
if mibBuilder.loadTexts:nsVpnUsrDialupGrpEntry.setStatus(_A)
class _NsVpnUsrDialupGrpIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_NsVpnUsrDialupGrpIndex_Type.__name__=_C
_NsVpnUsrDialupGrpIndex_Object=MibTableColumn
nsVpnUsrDialupGrpIndex=_NsVpnUsrDialupGrpIndex_Object((1,3,6,1,4,1,3224,4,10,1,1,1),_NsVpnUsrDialupGrpIndex_Type())
nsVpnUsrDialupGrpIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVpnUsrDialupGrpIndex.setStatus(_A)
class _NsVpnUsrDialupGrpName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_NsVpnUsrDialupGrpName_Type.__name__=_D
_NsVpnUsrDialupGrpName_Object=MibTableColumn
nsVpnUsrDialupGrpName=_NsVpnUsrDialupGrpName_Object((1,3,6,1,4,1,3224,4,10,1,1,2),_NsVpnUsrDialupGrpName_Type())
nsVpnUsrDialupGrpName.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVpnUsrDialupGrpName.setStatus(_A)
class _NsVpnUsrDialupGrpType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6)));namedValues=NamedValues(*(('undefined',0),('manual',1),('ike',2),('l2tp',3),('xauth',4),('auth',5),('external',6)))
_NsVpnUsrDialupGrpType_Type.__name__=_C
_NsVpnUsrDialupGrpType_Object=MibTableColumn
nsVpnUsrDialupGrpType=_NsVpnUsrDialupGrpType_Object((1,3,6,1,4,1,3224,4,10,1,1,3),_NsVpnUsrDialupGrpType_Type())
nsVpnUsrDialupGrpType.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVpnUsrDialupGrpType.setStatus(_A)
_NsVpnUsrDialupGrpVsys_Type=Integer32
_NsVpnUsrDialupGrpVsys_Object=MibTableColumn
nsVpnUsrDialupGrpVsys=_NsVpnUsrDialupGrpVsys_Object((1,3,6,1,4,1,3224,4,10,1,1,4),_NsVpnUsrDialupGrpVsys_Type())
nsVpnUsrDialupGrpVsys.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVpnUsrDialupGrpVsys.setStatus(_A)
_NsVpnManualKeyUsrTable_Object=MibTable
nsVpnManualKeyUsrTable=_NsVpnManualKeyUsrTable_Object((1,3,6,1,4,1,3224,4,10,2))
if mibBuilder.loadTexts:nsVpnManualKeyUsrTable.setStatus(_A)
_NsVpnManualKeyUsrEntry_Object=MibTableRow
nsVpnManualKeyUsrEntry=_NsVpnManualKeyUsrEntry_Object((1,3,6,1,4,1,3224,4,10,2,1))
nsVpnManualKeyUsrEntry.setIndexNames((0,_E,_I))
if mibBuilder.loadTexts:nsVpnManualKeyUsrEntry.setStatus(_A)
class _NsVpnManualKeyUsrIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_NsVpnManualKeyUsrIndex_Type.__name__=_C
_NsVpnManualKeyUsrIndex_Object=MibTableColumn
nsVpnManualKeyUsrIndex=_NsVpnManualKeyUsrIndex_Object((1,3,6,1,4,1,3224,4,10,2,1,1),_NsVpnManualKeyUsrIndex_Type())
nsVpnManualKeyUsrIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVpnManualKeyUsrIndex.setStatus(_A)
class _NsVpnManualKeyUsrName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_NsVpnManualKeyUsrName_Type.__name__=_D
_NsVpnManualKeyUsrName_Object=MibTableColumn
nsVpnManualKeyUsrName=_NsVpnManualKeyUsrName_Object((1,3,6,1,4,1,3224,4,10,2,1,2),_NsVpnManualKeyUsrName_Type())
nsVpnManualKeyUsrName.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVpnManualKeyUsrName.setStatus(_A)
class _NsVpnManualKeyUsrGrp_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_NsVpnManualKeyUsrGrp_Type.__name__=_D
_NsVpnManualKeyUsrGrp_Object=MibTableColumn
nsVpnManualKeyUsrGrp=_NsVpnManualKeyUsrGrp_Object((1,3,6,1,4,1,3224,4,10,2,1,3),_NsVpnManualKeyUsrGrp_Type())
nsVpnManualKeyUsrGrp.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVpnManualKeyUsrGrp.setStatus(_A)
_NsVpnManualKeyUsrSILocal_Type=Integer32
_NsVpnManualKeyUsrSILocal_Object=MibTableColumn
nsVpnManualKeyUsrSILocal=_NsVpnManualKeyUsrSILocal_Object((1,3,6,1,4,1,3224,4,10,2,1,4),_NsVpnManualKeyUsrSILocal_Type())
nsVpnManualKeyUsrSILocal.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVpnManualKeyUsrSILocal.setStatus(_A)
_NsVpnManualKeyUsrSIRemote_Type=Integer32
_NsVpnManualKeyUsrSIRemote_Object=MibTableColumn
nsVpnManualKeyUsrSIRemote=_NsVpnManualKeyUsrSIRemote_Object((1,3,6,1,4,1,3224,4,10,2,1,5),_NsVpnManualKeyUsrSIRemote_Type())
nsVpnManualKeyUsrSIRemote.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVpnManualKeyUsrSIRemote.setStatus(_A)
class _NsVpnManualKeyUsrTunnelType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('esp',0),('ah',1)))
_NsVpnManualKeyUsrTunnelType_Type.__name__=_C
_NsVpnManualKeyUsrTunnelType_Object=MibTableColumn
nsVpnManualKeyUsrTunnelType=_NsVpnManualKeyUsrTunnelType_Object((1,3,6,1,4,1,3224,4,10,2,1,6),_NsVpnManualKeyUsrTunnelType_Type())
nsVpnManualKeyUsrTunnelType.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVpnManualKeyUsrTunnelType.setStatus(_A)
class _NsVpnManualKeyUsrEspEncAlg_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*((_F,0),('des-cbc',1),('triple-des-cbc',2),('aes',3),('aes-192',4),('aes-256',5)))
_NsVpnManualKeyUsrEspEncAlg_Type.__name__=_C
_NsVpnManualKeyUsrEspEncAlg_Object=MibTableColumn
nsVpnManualKeyUsrEspEncAlg=_NsVpnManualKeyUsrEspEncAlg_Object((1,3,6,1,4,1,3224,4,10,2,1,7),_NsVpnManualKeyUsrEspEncAlg_Type())
nsVpnManualKeyUsrEspEncAlg.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVpnManualKeyUsrEspEncAlg.setStatus(_A)
class _NsVpnManualKeyUsrEspAuthAlg_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_F,0),('md5',1),('sha',2)))
_NsVpnManualKeyUsrEspAuthAlg_Type.__name__=_C
_NsVpnManualKeyUsrEspAuthAlg_Object=MibTableColumn
nsVpnManualKeyUsrEspAuthAlg=_NsVpnManualKeyUsrEspAuthAlg_Object((1,3,6,1,4,1,3224,4,10,2,1,8),_NsVpnManualKeyUsrEspAuthAlg_Type())
nsVpnManualKeyUsrEspAuthAlg.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVpnManualKeyUsrEspAuthAlg.setStatus(_A)
class _NsVpnManualKeyUsrAhHash_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_F,0),('md5',1),('sha',2)))
_NsVpnManualKeyUsrAhHash_Type.__name__=_C
_NsVpnManualKeyUsrAhHash_Object=MibTableColumn
nsVpnManualKeyUsrAhHash=_NsVpnManualKeyUsrAhHash_Object((1,3,6,1,4,1,3224,4,10,2,1,9),_NsVpnManualKeyUsrAhHash_Type())
nsVpnManualKeyUsrAhHash.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVpnManualKeyUsrAhHash.setStatus(_A)
_NsVpnManualKeyUsrVsys_Type=Integer32
_NsVpnManualKeyUsrVsys_Object=MibTableColumn
nsVpnManualKeyUsrVsys=_NsVpnManualKeyUsrVsys_Object((1,3,6,1,4,1,3224,4,10,2,1,10),_NsVpnManualKeyUsrVsys_Type())
nsVpnManualKeyUsrVsys.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVpnManualKeyUsrVsys.setStatus(_A)
_NsVpnAILUsrTable_Object=MibTable
nsVpnAILUsrTable=_NsVpnAILUsrTable_Object((1,3,6,1,4,1,3224,4,10,3))
if mibBuilder.loadTexts:nsVpnAILUsrTable.setStatus(_A)
_NsVpnAILUsrEntry_Object=MibTableRow
nsVpnAILUsrEntry=_NsVpnAILUsrEntry_Object((1,3,6,1,4,1,3224,4,10,3,1))
nsVpnAILUsrEntry.setIndexNames((0,_E,_J))
if mibBuilder.loadTexts:nsVpnAILUsrEntry.setStatus(_A)
class _NsVpnAILUsrIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_NsVpnAILUsrIndex_Type.__name__=_C
_NsVpnAILUsrIndex_Object=MibTableColumn
nsVpnAILUsrIndex=_NsVpnAILUsrIndex_Object((1,3,6,1,4,1,3224,4,10,3,1,1),_NsVpnAILUsrIndex_Type())
nsVpnAILUsrIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVpnAILUsrIndex.setStatus(_A)
class _NsVpnAILUsrName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_NsVpnAILUsrName_Type.__name__=_D
_NsVpnAILUsrName_Object=MibTableColumn
nsVpnAILUsrName=_NsVpnAILUsrName_Object((1,3,6,1,4,1,3224,4,10,3,1,2),_NsVpnAILUsrName_Type())
nsVpnAILUsrName.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVpnAILUsrName.setStatus(_A)
class _NsVpnAILUsrGrp_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_NsVpnAILUsrGrp_Type.__name__=_D
_NsVpnAILUsrGrp_Object=MibTableColumn
nsVpnAILUsrGrp=_NsVpnAILUsrGrp_Object((1,3,6,1,4,1,3224,4,10,3,1,3),_NsVpnAILUsrGrp_Type())
nsVpnAILUsrGrp.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVpnAILUsrGrp.setStatus(_A)
class _NsVpnAILUsrStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('disable',0),('enabled',1)))
_NsVpnAILUsrStatus_Type.__name__=_C
_NsVpnAILUsrStatus_Object=MibTableColumn
nsVpnAILUsrStatus=_NsVpnAILUsrStatus_Object((1,3,6,1,4,1,3224,4,10,3,1,4),_NsVpnAILUsrStatus_Type())
nsVpnAILUsrStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVpnAILUsrStatus.setStatus(_A)
class _NsVpnAILUsrIKE_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('no',0),(_G,1)))
_NsVpnAILUsrIKE_Type.__name__=_C
_NsVpnAILUsrIKE_Object=MibTableColumn
nsVpnAILUsrIKE=_NsVpnAILUsrIKE_Object((1,3,6,1,4,1,3224,4,10,3,1,5),_NsVpnAILUsrIKE_Type())
nsVpnAILUsrIKE.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVpnAILUsrIKE.setStatus(_A)
class _NsVpnAILUsrIKEIdType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*(('not-set',0),('ipv4-addr',1),('fqdn',2),('usr-fqdn',3),('ipv4-addr-subnet',4),('ipv6-addr',5),('ipv6-addr-subnet',6),('ipv4-addr-addr-range',7),('ipv6-addr-addr-range',8),('der-asn1-dn',9),('der-asn1-gn',10)))
_NsVpnAILUsrIKEIdType_Type.__name__=_C
_NsVpnAILUsrIKEIdType_Object=MibTableColumn
nsVpnAILUsrIKEIdType=_NsVpnAILUsrIKEIdType_Object((1,3,6,1,4,1,3224,4,10,3,1,6),_NsVpnAILUsrIKEIdType_Type())
nsVpnAILUsrIKEIdType.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVpnAILUsrIKEIdType.setStatus(_A)
_NsVpnAILUsrIKEId_Type=DisplayString
_NsVpnAILUsrIKEId_Object=MibTableColumn
nsVpnAILUsrIKEId=_NsVpnAILUsrIKEId_Object((1,3,6,1,4,1,3224,4,10,3,1,7),_NsVpnAILUsrIKEId_Type())
nsVpnAILUsrIKEId.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVpnAILUsrIKEId.setStatus(_A)
class _NsVpnAILUsrAuth_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('no',0),(_G,1)))
_NsVpnAILUsrAuth_Type.__name__=_C
_NsVpnAILUsrAuth_Object=MibTableColumn
nsVpnAILUsrAuth=_NsVpnAILUsrAuth_Object((1,3,6,1,4,1,3224,4,10,3,1,8),_NsVpnAILUsrAuth_Type())
nsVpnAILUsrAuth.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVpnAILUsrAuth.setStatus(_A)
class _NsVpnAILUsrL2TP_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('no',0),(_G,1)))
_NsVpnAILUsrL2TP_Type.__name__=_C
_NsVpnAILUsrL2TP_Object=MibTableColumn
nsVpnAILUsrL2TP=_NsVpnAILUsrL2TP_Object((1,3,6,1,4,1,3224,4,10,3,1,9),_NsVpnAILUsrL2TP_Type())
nsVpnAILUsrL2TP.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVpnAILUsrL2TP.setStatus(_A)
_NsVpnAILUsrL2tpRemoteIp_Type=IpAddress
_NsVpnAILUsrL2tpRemoteIp_Object=MibTableColumn
nsVpnAILUsrL2tpRemoteIp=_NsVpnAILUsrL2tpRemoteIp_Object((1,3,6,1,4,1,3224,4,10,3,1,10),_NsVpnAILUsrL2tpRemoteIp_Type())
nsVpnAILUsrL2tpRemoteIp.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVpnAILUsrL2tpRemoteIp.setStatus(_A)
_NsVpnAILUsrL2tpIpPool_Type=DisplayString
_NsVpnAILUsrL2tpIpPool_Object=MibTableColumn
nsVpnAILUsrL2tpIpPool=_NsVpnAILUsrL2tpIpPool_Object((1,3,6,1,4,1,3224,4,10,3,1,11),_NsVpnAILUsrL2tpIpPool_Type())
nsVpnAILUsrL2tpIpPool.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVpnAILUsrL2tpIpPool.setStatus(_A)
_NsVpnAILUsrL2tpIp_Type=IpAddress
_NsVpnAILUsrL2tpIp_Object=MibTableColumn
nsVpnAILUsrL2tpIp=_NsVpnAILUsrL2tpIp_Object((1,3,6,1,4,1,3224,4,10,3,1,12),_NsVpnAILUsrL2tpIp_Type())
nsVpnAILUsrL2tpIp.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVpnAILUsrL2tpIp.setStatus(_A)
_NsVpnAILUsrL2tpPriDnsIp_Type=IpAddress
_NsVpnAILUsrL2tpPriDnsIp_Object=MibTableColumn
nsVpnAILUsrL2tpPriDnsIp=_NsVpnAILUsrL2tpPriDnsIp_Object((1,3,6,1,4,1,3224,4,10,3,1,13),_NsVpnAILUsrL2tpPriDnsIp_Type())
nsVpnAILUsrL2tpPriDnsIp.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVpnAILUsrL2tpPriDnsIp.setStatus(_A)
_NsVpnAILUsrL2tpSecDnsIp_Type=IpAddress
_NsVpnAILUsrL2tpSecDnsIp_Object=MibTableColumn
nsVpnAILUsrL2tpSecDnsIp=_NsVpnAILUsrL2tpSecDnsIp_Object((1,3,6,1,4,1,3224,4,10,3,1,14),_NsVpnAILUsrL2tpSecDnsIp_Type())
nsVpnAILUsrL2tpSecDnsIp.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVpnAILUsrL2tpSecDnsIp.setStatus(_A)
_NsVpnAILUsrL2tpPriWinsIp_Type=IpAddress
_NsVpnAILUsrL2tpPriWinsIp_Object=MibTableColumn
nsVpnAILUsrL2tpPriWinsIp=_NsVpnAILUsrL2tpPriWinsIp_Object((1,3,6,1,4,1,3224,4,10,3,1,15),_NsVpnAILUsrL2tpPriWinsIp_Type())
nsVpnAILUsrL2tpPriWinsIp.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVpnAILUsrL2tpPriWinsIp.setStatus(_A)
_NsVpnAILUsrL2tpSecWinsIp_Type=IpAddress
_NsVpnAILUsrL2tpSecWinsIp_Object=MibTableColumn
nsVpnAILUsrL2tpSecWinsIp=_NsVpnAILUsrL2tpSecWinsIp_Object((1,3,6,1,4,1,3224,4,10,3,1,16),_NsVpnAILUsrL2tpSecWinsIp_Type())
nsVpnAILUsrL2tpSecWinsIp.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVpnAILUsrL2tpSecWinsIp.setStatus(_A)
_NsVpnAILUsrVsys_Type=Integer32
_NsVpnAILUsrVsys_Object=MibTableColumn
nsVpnAILUsrVsys=_NsVpnAILUsrVsys_Object((1,3,6,1,4,1,3224,4,10,3,1,17),_NsVpnAILUsrVsys_Type())
nsVpnAILUsrVsys.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVpnAILUsrVsys.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'netscreenUserMibModule':netscreenUserMibModule,'nsVpnUser':nsVpnUser,'nsVpnUsrDialupGrpTable':nsVpnUsrDialupGrpTable,'nsVpnUsrDialupGrpEntry':nsVpnUsrDialupGrpEntry,_H:nsVpnUsrDialupGrpIndex,'nsVpnUsrDialupGrpName':nsVpnUsrDialupGrpName,'nsVpnUsrDialupGrpType':nsVpnUsrDialupGrpType,'nsVpnUsrDialupGrpVsys':nsVpnUsrDialupGrpVsys,'nsVpnManualKeyUsrTable':nsVpnManualKeyUsrTable,'nsVpnManualKeyUsrEntry':nsVpnManualKeyUsrEntry,_I:nsVpnManualKeyUsrIndex,'nsVpnManualKeyUsrName':nsVpnManualKeyUsrName,'nsVpnManualKeyUsrGrp':nsVpnManualKeyUsrGrp,'nsVpnManualKeyUsrSILocal':nsVpnManualKeyUsrSILocal,'nsVpnManualKeyUsrSIRemote':nsVpnManualKeyUsrSIRemote,'nsVpnManualKeyUsrTunnelType':nsVpnManualKeyUsrTunnelType,'nsVpnManualKeyUsrEspEncAlg':nsVpnManualKeyUsrEspEncAlg,'nsVpnManualKeyUsrEspAuthAlg':nsVpnManualKeyUsrEspAuthAlg,'nsVpnManualKeyUsrAhHash':nsVpnManualKeyUsrAhHash,'nsVpnManualKeyUsrVsys':nsVpnManualKeyUsrVsys,'nsVpnAILUsrTable':nsVpnAILUsrTable,'nsVpnAILUsrEntry':nsVpnAILUsrEntry,_J:nsVpnAILUsrIndex,'nsVpnAILUsrName':nsVpnAILUsrName,'nsVpnAILUsrGrp':nsVpnAILUsrGrp,'nsVpnAILUsrStatus':nsVpnAILUsrStatus,'nsVpnAILUsrIKE':nsVpnAILUsrIKE,'nsVpnAILUsrIKEIdType':nsVpnAILUsrIKEIdType,'nsVpnAILUsrIKEId':nsVpnAILUsrIKEId,'nsVpnAILUsrAuth':nsVpnAILUsrAuth,'nsVpnAILUsrL2TP':nsVpnAILUsrL2TP,'nsVpnAILUsrL2tpRemoteIp':nsVpnAILUsrL2tpRemoteIp,'nsVpnAILUsrL2tpIpPool':nsVpnAILUsrL2tpIpPool,'nsVpnAILUsrL2tpIp':nsVpnAILUsrL2tpIp,'nsVpnAILUsrL2tpPriDnsIp':nsVpnAILUsrL2tpPriDnsIp,'nsVpnAILUsrL2tpSecDnsIp':nsVpnAILUsrL2tpSecDnsIp,'nsVpnAILUsrL2tpPriWinsIp':nsVpnAILUsrL2tpPriWinsIp,'nsVpnAILUsrL2tpSecWinsIp':nsVpnAILUsrL2tpSecWinsIp,'nsVpnAILUsrVsys':nsVpnAILUsrVsys})