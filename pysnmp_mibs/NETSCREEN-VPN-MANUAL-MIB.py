_I='enabled'
_H='disable'
_G='nsVpnManualKeyIndex'
_F='NETSCREEN-VPN-MANUAL-MIB'
_E='DisplayString'
_D='null'
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
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_E,'PhysAddress','TextualConvention')
netscreenVpnManualMibModule=ModuleIdentity((1,3,6,1,4,1,3224,4,0,2))
if mibBuilder.loadTexts:netscreenVpnManualMibModule.setRevisions(('2004-05-03 00:00','2004-03-03 00:00','2003-11-13 00:00','2002-05-21 00:00','2001-09-28 00:00','2001-05-14 00:00'))
_NsVpnManualKey_ObjectIdentity=ObjectIdentity
nsVpnManualKey=_NsVpnManualKey_ObjectIdentity((1,3,6,1,4,1,3224,4,2))
_NsVpnManualKeyTable_Object=MibTable
nsVpnManualKeyTable=_NsVpnManualKeyTable_Object((1,3,6,1,4,1,3224,4,2,1))
if mibBuilder.loadTexts:nsVpnManualKeyTable.setStatus(_A)
_NsVpnManualKeyEntry_Object=MibTableRow
nsVpnManualKeyEntry=_NsVpnManualKeyEntry_Object((1,3,6,1,4,1,3224,4,2,1,1))
nsVpnManualKeyEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:nsVpnManualKeyEntry.setStatus(_A)
class _NsVpnManualKeyIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_NsVpnManualKeyIndex_Type.__name__=_C
_NsVpnManualKeyIndex_Object=MibTableColumn
nsVpnManualKeyIndex=_NsVpnManualKeyIndex_Object((1,3,6,1,4,1,3224,4,2,1,1,1),_NsVpnManualKeyIndex_Type())
nsVpnManualKeyIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVpnManualKeyIndex.setStatus(_A)
class _NsVpnManualKeyTunName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_NsVpnManualKeyTunName_Type.__name__=_E
_NsVpnManualKeyTunName_Object=MibTableColumn
nsVpnManualKeyTunName=_NsVpnManualKeyTunName_Object((1,3,6,1,4,1,3224,4,2,1,1,2),_NsVpnManualKeyTunName_Type())
nsVpnManualKeyTunName.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVpnManualKeyTunName.setStatus(_A)
_NsVpnManualKeyGW_Type=IpAddress
_NsVpnManualKeyGW_Object=MibTableColumn
nsVpnManualKeyGW=_NsVpnManualKeyGW_Object((1,3,6,1,4,1,3224,4,2,1,1,3),_NsVpnManualKeyGW_Type())
nsVpnManualKeyGW.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVpnManualKeyGW.setStatus(_A)
_NsVpnManualKeySILocal_Type=Integer32
_NsVpnManualKeySILocal_Object=MibTableColumn
nsVpnManualKeySILocal=_NsVpnManualKeySILocal_Object((1,3,6,1,4,1,3224,4,2,1,1,4),_NsVpnManualKeySILocal_Type())
nsVpnManualKeySILocal.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVpnManualKeySILocal.setStatus(_A)
_NsVpnManualKeySIRemote_Type=Integer32
_NsVpnManualKeySIRemote_Object=MibTableColumn
nsVpnManualKeySIRemote=_NsVpnManualKeySIRemote_Object((1,3,6,1,4,1,3224,4,2,1,1,5),_NsVpnManualKeySIRemote_Type())
nsVpnManualKeySIRemote.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVpnManualKeySIRemote.setStatus(_A)
class _NsVpnManualKeyTunnelType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('esp',0),('ah',1)))
_NsVpnManualKeyTunnelType_Type.__name__=_C
_NsVpnManualKeyTunnelType_Object=MibTableColumn
nsVpnManualKeyTunnelType=_NsVpnManualKeyTunnelType_Object((1,3,6,1,4,1,3224,4,2,1,1,6),_NsVpnManualKeyTunnelType_Type())
nsVpnManualKeyTunnelType.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVpnManualKeyTunnelType.setStatus(_A)
class _NsVpnManualKeyEspEncAlg_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*((_D,0),('des-cbc',1),('tripple-des-cbc',2),('aes-cbc',3),('aes-192',4),('aes-256',5)))
_NsVpnManualKeyEspEncAlg_Type.__name__=_C
_NsVpnManualKeyEspEncAlg_Object=MibTableColumn
nsVpnManualKeyEspEncAlg=_NsVpnManualKeyEspEncAlg_Object((1,3,6,1,4,1,3224,4,2,1,1,7),_NsVpnManualKeyEspEncAlg_Type())
nsVpnManualKeyEspEncAlg.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVpnManualKeyEspEncAlg.setStatus(_A)
class _NsVpnManualKeyEspAuthAlg_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_D,0),('md5',1),('sha',2),('sha256',3)))
_NsVpnManualKeyEspAuthAlg_Type.__name__=_C
_NsVpnManualKeyEspAuthAlg_Object=MibTableColumn
nsVpnManualKeyEspAuthAlg=_NsVpnManualKeyEspAuthAlg_Object((1,3,6,1,4,1,3224,4,2,1,1,8),_NsVpnManualKeyEspAuthAlg_Type())
nsVpnManualKeyEspAuthAlg.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVpnManualKeyEspAuthAlg.setStatus(_A)
class _NsVpnManualKeyAhHash_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_D,0),('md5',1),('sha',2)))
_NsVpnManualKeyAhHash_Type.__name__=_C
_NsVpnManualKeyAhHash_Object=MibTableColumn
nsVpnManualKeyAhHash=_NsVpnManualKeyAhHash_Object((1,3,6,1,4,1,3224,4,2,1,1,9),_NsVpnManualKeyAhHash_Type())
nsVpnManualKeyAhHash.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVpnManualKeyAhHash.setStatus(_A)
class _NsVpnManualKeyMonitorEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_H,0),(_I,1)))
_NsVpnManualKeyMonitorEnable_Type.__name__=_C
_NsVpnManualKeyMonitorEnable_Object=MibTableColumn
nsVpnManualKeyMonitorEnable=_NsVpnManualKeyMonitorEnable_Object((1,3,6,1,4,1,3224,4,2,1,1,10),_NsVpnManualKeyMonitorEnable_Type())
nsVpnManualKeyMonitorEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVpnManualKeyMonitorEnable.setStatus(_A)
class _NsVpnManualKeyTunToTrust_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_H,0),(_I,1)))
_NsVpnManualKeyTunToTrust_Type.__name__=_C
_NsVpnManualKeyTunToTrust_Object=MibTableColumn
nsVpnManualKeyTunToTrust=_NsVpnManualKeyTunToTrust_Object((1,3,6,1,4,1,3224,4,2,1,1,11),_NsVpnManualKeyTunToTrust_Type())
nsVpnManualKeyTunToTrust.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVpnManualKeyTunToTrust.setStatus(_A)
_NsVpnManualKeyVsys_Type=Integer32
_NsVpnManualKeyVsys_Object=MibTableColumn
nsVpnManualKeyVsys=_NsVpnManualKeyVsys_Object((1,3,6,1,4,1,3224,4,2,1,1,12),_NsVpnManualKeyVsys_Type())
nsVpnManualKeyVsys.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVpnManualKeyVsys.setStatus(_A)
mibBuilder.exportSymbols(_F,**{'netscreenVpnManualMibModule':netscreenVpnManualMibModule,'nsVpnManualKey':nsVpnManualKey,'nsVpnManualKeyTable':nsVpnManualKeyTable,'nsVpnManualKeyEntry':nsVpnManualKeyEntry,_G:nsVpnManualKeyIndex,'nsVpnManualKeyTunName':nsVpnManualKeyTunName,'nsVpnManualKeyGW':nsVpnManualKeyGW,'nsVpnManualKeySILocal':nsVpnManualKeySILocal,'nsVpnManualKeySIRemote':nsVpnManualKeySIRemote,'nsVpnManualKeyTunnelType':nsVpnManualKeyTunnelType,'nsVpnManualKeyEspEncAlg':nsVpnManualKeyEspEncAlg,'nsVpnManualKeyEspAuthAlg':nsVpnManualKeyEspAuthAlg,'nsVpnManualKeyAhHash':nsVpnManualKeyAhHash,'nsVpnManualKeyMonitorEnable':nsVpnManualKeyMonitorEnable,'nsVpnManualKeyTunToTrust':nsVpnManualKeyTunToTrust,'nsVpnManualKeyVsys':nsVpnManualKeyVsys})