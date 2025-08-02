_F='nsVpnIasSessIndex'
_E='nsVpnIasType'
_D='Integer32'
_C='NETSCREEN-VPN-IAS-MIB'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
netscreenVpn,=mibBuilder.importSymbols('NETSCREEN-SMI','netscreenVpn')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
_NsVpnIas_ObjectIdentity=ObjectIdentity
nsVpnIas=_NsVpnIas_ObjectIdentity((1,3,6,1,4,1,3224,4,11))
_NsVpnIasTable_Object=MibTable
nsVpnIasTable=_NsVpnIasTable_Object((1,3,6,1,4,1,3224,4,11,1))
if mibBuilder.loadTexts:nsVpnIasTable.setStatus(_A)
_NsVpnIasEntry_Object=MibTableRow
nsVpnIasEntry=_NsVpnIasEntry_Object((1,3,6,1,4,1,3224,4,11,1,1))
nsVpnIasEntry.setIndexNames((0,_C,_E))
if mibBuilder.loadTexts:nsVpnIasEntry.setStatus(_A)
class _NsVpnIasType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('ipv4',1),('ipv6',2)))
_NsVpnIasType_Type.__name__=_D
_NsVpnIasType_Object=MibTableColumn
nsVpnIasType=_NsVpnIasType_Object((1,3,6,1,4,1,3224,4,11,1,1,1),_NsVpnIasType_Type())
nsVpnIasType.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVpnIasType.setStatus(_A)
_NsVpnIasTotal_Type=Counter32
_NsVpnIasTotal_Object=MibTableColumn
nsVpnIasTotal=_NsVpnIasTotal_Object((1,3,6,1,4,1,3224,4,11,1,1,2),_NsVpnIasTotal_Type())
nsVpnIasTotal.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVpnIasTotal.setStatus(_A)
_NsVpnIasSessTable_Object=MibTable
nsVpnIasSessTable=_NsVpnIasSessTable_Object((1,3,6,1,4,1,3224,4,11,2))
if mibBuilder.loadTexts:nsVpnIasSessTable.setStatus(_A)
_NsVpnIasSessEntry_Object=MibTableRow
nsVpnIasSessEntry=_NsVpnIasSessEntry_Object((1,3,6,1,4,1,3224,4,11,2,1))
nsVpnIasSessEntry.setIndexNames((0,_C,_F))
if mibBuilder.loadTexts:nsVpnIasSessEntry.setStatus(_A)
_NsVpnIasSessIndex_Type=Integer32
_NsVpnIasSessIndex_Object=MibTableColumn
nsVpnIasSessIndex=_NsVpnIasSessIndex_Object((1,3,6,1,4,1,3224,4,11,2,1,1),_NsVpnIasSessIndex_Type())
nsVpnIasSessIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVpnIasSessIndex.setStatus(_A)
_NsVpnIasSessXauthUserName_Type=DisplayString
_NsVpnIasSessXauthUserName_Object=MibTableColumn
nsVpnIasSessXauthUserName=_NsVpnIasSessXauthUserName_Object((1,3,6,1,4,1,3224,4,11,2,1,2),_NsVpnIasSessXauthUserName_Type())
nsVpnIasSessXauthUserName.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVpnIasSessXauthUserName.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'nsVpnIas':nsVpnIas,'nsVpnIasTable':nsVpnIasTable,'nsVpnIasEntry':nsVpnIasEntry,_E:nsVpnIasType,'nsVpnIasTotal':nsVpnIasTotal,'nsVpnIasSessTable':nsVpnIasSessTable,'nsVpnIasSessEntry':nsVpnIasSessEntry,_F:nsVpnIasSessIndex,'nsVpnIasSessXauthUserName':nsVpnIasSessXauthUserName})