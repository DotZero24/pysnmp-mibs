_F='nsVpnIpPoolIndex'
_E='NETSCREEN-IPPOOL-MIB'
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
netscreenIppoolMibModule=ModuleIdentity((1,3,6,1,4,1,3224,4,0,9))
if mibBuilder.loadTexts:netscreenIppoolMibModule.setRevisions(('2004-05-03 00:00','2004-03-03 00:00','2003-11-13 00:00','2001-09-28 00:00','2000-08-27 00:00'))
_NsVpnIpPool_ObjectIdentity=ObjectIdentity
nsVpnIpPool=_NsVpnIpPool_ObjectIdentity((1,3,6,1,4,1,3224,4,9))
_NsVpnIpPoolTable_Object=MibTable
nsVpnIpPoolTable=_NsVpnIpPoolTable_Object((1,3,6,1,4,1,3224,4,9,1))
if mibBuilder.loadTexts:nsVpnIpPoolTable.setStatus(_A)
_NsVpnIpPoolEntry_Object=MibTableRow
nsVpnIpPoolEntry=_NsVpnIpPoolEntry_Object((1,3,6,1,4,1,3224,4,9,1,1))
nsVpnIpPoolEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:nsVpnIpPoolEntry.setStatus(_A)
class _NsVpnIpPoolIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_NsVpnIpPoolIndex_Type.__name__=_C
_NsVpnIpPoolIndex_Object=MibTableColumn
nsVpnIpPoolIndex=_NsVpnIpPoolIndex_Object((1,3,6,1,4,1,3224,4,9,1,1,1),_NsVpnIpPoolIndex_Type())
nsVpnIpPoolIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVpnIpPoolIndex.setStatus(_A)
class _NsVpnIpPoolName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_NsVpnIpPoolName_Type.__name__=_D
_NsVpnIpPoolName_Object=MibTableColumn
nsVpnIpPoolName=_NsVpnIpPoolName_Object((1,3,6,1,4,1,3224,4,9,1,1,2),_NsVpnIpPoolName_Type())
nsVpnIpPoolName.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVpnIpPoolName.setStatus(_A)
_NsVpnIpPoolStartIp_Type=IpAddress
_NsVpnIpPoolStartIp_Object=MibTableColumn
nsVpnIpPoolStartIp=_NsVpnIpPoolStartIp_Object((1,3,6,1,4,1,3224,4,9,1,1,3),_NsVpnIpPoolStartIp_Type())
nsVpnIpPoolStartIp.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVpnIpPoolStartIp.setStatus(_A)
_NsVpnIpPoolEndIp_Type=IpAddress
_NsVpnIpPoolEndIp_Object=MibTableColumn
nsVpnIpPoolEndIp=_NsVpnIpPoolEndIp_Object((1,3,6,1,4,1,3224,4,9,1,1,4),_NsVpnIpPoolEndIp_Type())
nsVpnIpPoolEndIp.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVpnIpPoolEndIp.setStatus(_A)
_NsVpnIpPoolIpUsed_Type=Integer32
_NsVpnIpPoolIpUsed_Object=MibTableColumn
nsVpnIpPoolIpUsed=_NsVpnIpPoolIpUsed_Object((1,3,6,1,4,1,3224,4,9,1,1,5),_NsVpnIpPoolIpUsed_Type())
nsVpnIpPoolIpUsed.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVpnIpPoolIpUsed.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'netscreenIppoolMibModule':netscreenIppoolMibModule,'nsVpnIpPool':nsVpnIpPool,'nsVpnIpPoolTable':nsVpnIpPoolTable,'nsVpnIpPoolEntry':nsVpnIpPoolEntry,_F:nsVpnIpPoolIndex,'nsVpnIpPoolName':nsVpnIpPoolName,'nsVpnIpPoolStartIp':nsVpnIpPoolStartIp,'nsVpnIpPoolEndIp':nsVpnIpPoolEndIp,'nsVpnIpPoolIpUsed':nsVpnIpPoolIpUsed})