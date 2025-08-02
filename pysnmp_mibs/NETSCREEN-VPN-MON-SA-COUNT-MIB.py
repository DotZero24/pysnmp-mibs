_E='nsVpnMonSACountType'
_D='NETSCREEN-VPN-MON-SA-COUNT-MIB'
_C='Integer32'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
netscreenVpn,=mibBuilder.importSymbols('NETSCREEN-SMI','netscreenVpn')
netscreenVpnMon,=mibBuilder.importSymbols('NETSCREEN-VPN-MON-MIB','netscreenVpnMon')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
_NsVpnMonSACountTable_Object=MibTable
nsVpnMonSACountTable=_NsVpnMonSACountTable_Object((1,3,6,1,4,1,3224,4,1,2))
if mibBuilder.loadTexts:nsVpnMonSACountTable.setStatus(_A)
_NsVpnMonSACountEntry_Object=MibTableRow
nsVpnMonSACountEntry=_NsVpnMonSACountEntry_Object((1,3,6,1,4,1,3224,4,1,2,1))
nsVpnMonSACountEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:nsVpnMonSACountEntry.setStatus(_A)
class _NsVpnMonSACountType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('ipv4',1),('ipv6',2)))
_NsVpnMonSACountType_Type.__name__=_C
_NsVpnMonSACountType_Object=MibTableColumn
nsVpnMonSACountType=_NsVpnMonSACountType_Object((1,3,6,1,4,1,3224,4,1,2,1,1),_NsVpnMonSACountType_Type())
nsVpnMonSACountType.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVpnMonSACountType.setStatus(_A)
_NsVpnMonSACountTotal_Type=Counter32
_NsVpnMonSACountTotal_Object=MibTableColumn
nsVpnMonSACountTotal=_NsVpnMonSACountTotal_Object((1,3,6,1,4,1,3224,4,1,2,1,2),_NsVpnMonSACountTotal_Type())
nsVpnMonSACountTotal.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVpnMonSACountTotal.setStatus(_A)
_NsVpnMonSACountAct_Type=Counter32
_NsVpnMonSACountAct_Object=MibTableColumn
nsVpnMonSACountAct=_NsVpnMonSACountAct_Object((1,3,6,1,4,1,3224,4,1,2,1,3),_NsVpnMonSACountAct_Type())
nsVpnMonSACountAct.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVpnMonSACountAct.setStatus(_A)
_NsVpnMonSACountInTotal_Type=Counter32
_NsVpnMonSACountInTotal_Object=MibTableColumn
nsVpnMonSACountInTotal=_NsVpnMonSACountInTotal_Object((1,3,6,1,4,1,3224,4,1,2,1,4),_NsVpnMonSACountInTotal_Type())
nsVpnMonSACountInTotal.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVpnMonSACountInTotal.setStatus(_A)
_NsVpnMonSACountInAct_Type=Counter32
_NsVpnMonSACountInAct_Object=MibTableColumn
nsVpnMonSACountInAct=_NsVpnMonSACountInAct_Object((1,3,6,1,4,1,3224,4,1,2,1,5),_NsVpnMonSACountInAct_Type())
nsVpnMonSACountInAct.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVpnMonSACountInAct.setStatus(_A)
_NsVpnMonSACountOutTotal_Type=Counter32
_NsVpnMonSACountOutTotal_Object=MibTableColumn
nsVpnMonSACountOutTotal=_NsVpnMonSACountOutTotal_Object((1,3,6,1,4,1,3224,4,1,2,1,6),_NsVpnMonSACountOutTotal_Type())
nsVpnMonSACountOutTotal.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVpnMonSACountOutTotal.setStatus(_A)
_NsVpnMonSACountOutAct_Type=Counter32
_NsVpnMonSACountOutAct_Object=MibTableColumn
nsVpnMonSACountOutAct=_NsVpnMonSACountOutAct_Object((1,3,6,1,4,1,3224,4,1,2,1,7),_NsVpnMonSACountOutAct_Type())
nsVpnMonSACountOutAct.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVpnMonSACountOutAct.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'nsVpnMonSACountTable':nsVpnMonSACountTable,'nsVpnMonSACountEntry':nsVpnMonSACountEntry,_E:nsVpnMonSACountType,'nsVpnMonSACountTotal':nsVpnMonSACountTotal,'nsVpnMonSACountAct':nsVpnMonSACountAct,'nsVpnMonSACountInTotal':nsVpnMonSACountInTotal,'nsVpnMonSACountInAct':nsVpnMonSACountInAct,'nsVpnMonSACountOutTotal':nsVpnMonSACountOutTotal,'nsVpnMonSACountOutAct':nsVpnMonSACountOutAct})