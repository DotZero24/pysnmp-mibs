_F='nsVpnGwIndex'
_E='NETSCREEN-VPN-GATEWAY-MIB'
_D='Integer32'
_C='DisplayString'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
netscreenVpn,netscreenVpnMibModule=mibBuilder.importSymbols('NETSCREEN-SMI','netscreenVpn','netscreenVpnMibModule')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_C,'PhysAddress','TextualConvention')
netscreenVpnGatewayMibModule=ModuleIdentity((1,3,6,1,4,1,3224,4,0,4))
if mibBuilder.loadTexts:netscreenVpnGatewayMibModule.setRevisions(('2004-05-03 00:00','2004-03-03 00:00','2003-11-13 00:00','2001-09-28 00:00','2001-05-14 00:00'))
_NsVpnGateway_ObjectIdentity=ObjectIdentity
nsVpnGateway=_NsVpnGateway_ObjectIdentity((1,3,6,1,4,1,3224,4,4))
_NsVpnGwTable_Object=MibTable
nsVpnGwTable=_NsVpnGwTable_Object((1,3,6,1,4,1,3224,4,4,1))
if mibBuilder.loadTexts:nsVpnGwTable.setStatus(_A)
_NsVpnGwEntry_Object=MibTableRow
nsVpnGwEntry=_NsVpnGwEntry_Object((1,3,6,1,4,1,3224,4,4,1,1))
nsVpnGwEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:nsVpnGwEntry.setStatus(_A)
class _NsVpnGwIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_NsVpnGwIndex_Type.__name__=_D
_NsVpnGwIndex_Object=MibTableColumn
nsVpnGwIndex=_NsVpnGwIndex_Object((1,3,6,1,4,1,3224,4,4,1,1,1),_NsVpnGwIndex_Type())
nsVpnGwIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVpnGwIndex.setStatus(_A)
class _NsVpnGwName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_NsVpnGwName_Type.__name__=_C
_NsVpnGwName_Object=MibTableColumn
nsVpnGwName=_NsVpnGwName_Object((1,3,6,1,4,1,3224,4,4,1,1,2),_NsVpnGwName_Type())
nsVpnGwName.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVpnGwName.setStatus(_A)
class _NsVpnGwRemoteType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,3)));namedValues=NamedValues(*(('static-ip',0),('dynamic-ip',1),('dialup-user',3)))
_NsVpnGwRemoteType_Type.__name__=_D
_NsVpnGwRemoteType_Object=MibTableColumn
nsVpnGwRemoteType=_NsVpnGwRemoteType_Object((1,3,6,1,4,1,3224,4,4,1,1,3),_NsVpnGwRemoteType_Type())
nsVpnGwRemoteType.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVpnGwRemoteType.setStatus(_A)
_NsVpnGwRemoteStaticIp_Type=IpAddress
_NsVpnGwRemoteStaticIp_Object=MibTableColumn
nsVpnGwRemoteStaticIp=_NsVpnGwRemoteStaticIp_Object((1,3,6,1,4,1,3224,4,4,1,1,4),_NsVpnGwRemoteStaticIp_Type())
nsVpnGwRemoteStaticIp.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVpnGwRemoteStaticIp.setStatus(_A)
class _NsVpnGwRemotePeerId_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_NsVpnGwRemotePeerId_Type.__name__=_C
_NsVpnGwRemotePeerId_Object=MibTableColumn
nsVpnGwRemotePeerId=_NsVpnGwRemotePeerId_Object((1,3,6,1,4,1,3224,4,4,1,1,5),_NsVpnGwRemotePeerId_Type())
nsVpnGwRemotePeerId.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVpnGwRemotePeerId.setStatus(_A)
class _NsVpnGwDialup_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_NsVpnGwDialup_Type.__name__=_C
_NsVpnGwDialup_Object=MibTableColumn
nsVpnGwDialup=_NsVpnGwDialup_Object((1,3,6,1,4,1,3224,4,4,1,1,6),_NsVpnGwDialup_Type())
nsVpnGwDialup.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVpnGwDialup.setStatus(_A)
class _NsVpnGwInitMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('main',0),('aggressive',1)))
_NsVpnGwInitMode_Type.__name__=_D
_NsVpnGwInitMode_Object=MibTableColumn
nsVpnGwInitMode=_NsVpnGwInitMode_Object((1,3,6,1,4,1,3224,4,4,1,1,7),_NsVpnGwInitMode_Type())
nsVpnGwInitMode.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVpnGwInitMode.setStatus(_A)
class _NsVpnGwPhOnePropOne_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_NsVpnGwPhOnePropOne_Type.__name__=_C
_NsVpnGwPhOnePropOne_Object=MibTableColumn
nsVpnGwPhOnePropOne=_NsVpnGwPhOnePropOne_Object((1,3,6,1,4,1,3224,4,4,1,1,8),_NsVpnGwPhOnePropOne_Type())
nsVpnGwPhOnePropOne.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVpnGwPhOnePropOne.setStatus(_A)
class _NsVpnGwPhOnePropTwo_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_NsVpnGwPhOnePropTwo_Type.__name__=_C
_NsVpnGwPhOnePropTwo_Object=MibTableColumn
nsVpnGwPhOnePropTwo=_NsVpnGwPhOnePropTwo_Object((1,3,6,1,4,1,3224,4,4,1,1,9),_NsVpnGwPhOnePropTwo_Type())
nsVpnGwPhOnePropTwo.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVpnGwPhOnePropTwo.setStatus(_A)
class _NsVpnGwPhOnePropThree_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_NsVpnGwPhOnePropThree_Type.__name__=_C
_NsVpnGwPhOnePropThree_Object=MibTableColumn
nsVpnGwPhOnePropThree=_NsVpnGwPhOnePropThree_Object((1,3,6,1,4,1,3224,4,4,1,1,10),_NsVpnGwPhOnePropThree_Type())
nsVpnGwPhOnePropThree.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVpnGwPhOnePropThree.setStatus(_A)
class _NsVpnGwPhOnePropFour_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_NsVpnGwPhOnePropFour_Type.__name__=_C
_NsVpnGwPhOnePropFour_Object=MibTableColumn
nsVpnGwPhOnePropFour=_NsVpnGwPhOnePropFour_Object((1,3,6,1,4,1,3224,4,4,1,1,11),_NsVpnGwPhOnePropFour_Type())
nsVpnGwPhOnePropFour.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVpnGwPhOnePropFour.setStatus(_A)
class _NsVpnGwCertLocal_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_NsVpnGwCertLocal_Type.__name__=_C
_NsVpnGwCertLocal_Object=MibTableColumn
nsVpnGwCertLocal=_NsVpnGwCertLocal_Object((1,3,6,1,4,1,3224,4,4,1,1,12),_NsVpnGwCertLocal_Type())
nsVpnGwCertLocal.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVpnGwCertLocal.setStatus(_A)
class _NsVpnGwPeerCa_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_NsVpnGwPeerCa_Type.__name__=_C
_NsVpnGwPeerCa_Object=MibTableColumn
nsVpnGwPeerCa=_NsVpnGwPeerCa_Object((1,3,6,1,4,1,3224,4,4,1,1,13),_NsVpnGwPeerCa_Type())
nsVpnGwPeerCa.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVpnGwPeerCa.setStatus(_A)
class _NsVpnGwPeerType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*(('none',0),('pkcs7',1),('pgp',2),('dns',3),('x509-sig',4),('x509-ke',5),('keerberos',6),('crl',7),('arl',8),('spki',9),('x509-att',10)))
_NsVpnGwPeerType_Type.__name__=_D
_NsVpnGwPeerType_Object=MibTableColumn
nsVpnGwPeerType=_NsVpnGwPeerType_Object((1,3,6,1,4,1,3224,4,4,1,1,14),_NsVpnGwPeerType_Type())
nsVpnGwPeerType.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVpnGwPeerType.setStatus(_A)
_NsVpnGwVsys_Type=Integer32
_NsVpnGwVsys_Object=MibTableColumn
nsVpnGwVsys=_NsVpnGwVsys_Object((1,3,6,1,4,1,3224,4,4,1,1,15),_NsVpnGwVsys_Type())
nsVpnGwVsys.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVpnGwVsys.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'netscreenVpnGatewayMibModule':netscreenVpnGatewayMibModule,'nsVpnGateway':nsVpnGateway,'nsVpnGwTable':nsVpnGwTable,'nsVpnGwEntry':nsVpnGwEntry,_F:nsVpnGwIndex,'nsVpnGwName':nsVpnGwName,'nsVpnGwRemoteType':nsVpnGwRemoteType,'nsVpnGwRemoteStaticIp':nsVpnGwRemoteStaticIp,'nsVpnGwRemotePeerId':nsVpnGwRemotePeerId,'nsVpnGwDialup':nsVpnGwDialup,'nsVpnGwInitMode':nsVpnGwInitMode,'nsVpnGwPhOnePropOne':nsVpnGwPhOnePropOne,'nsVpnGwPhOnePropTwo':nsVpnGwPhOnePropTwo,'nsVpnGwPhOnePropThree':nsVpnGwPhOnePropThree,'nsVpnGwPhOnePropFour':nsVpnGwPhOnePropFour,'nsVpnGwCertLocal':nsVpnGwCertLocal,'nsVpnGwPeerCa':nsVpnGwPeerCa,'nsVpnGwPeerType':nsVpnGwPeerType,'nsVpnGwVsys':nsVpnGwVsys})