_D='DisplayString'
_C='Integer32'
_B='current'
_A='read-only'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
netscreenSetting,netscreenSettingMibModule=mibBuilder.importSymbols('NETSCREEN-SMI','netscreenSetting','netscreenSettingMibModule')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_D,'PhysAddress','TextualConvention')
netscreenSetDnsMibModule=ModuleIdentity((1,3,6,1,4,1,3224,7,0,3))
if mibBuilder.loadTexts:netscreenSetDnsMibModule.setRevisions(('2004-05-03 00:00','2004-03-03 00:00','2003-11-10 00:00','2001-09-28 00:00','2001-05-27 00:00'))
_NsSetDNS_ObjectIdentity=ObjectIdentity
nsSetDNS=_NsSetDNS_ObjectIdentity((1,3,6,1,4,1,3224,7,3))
_NsConfigDnsPriSer_Type=IpAddress
_NsConfigDnsPriSer_Object=MibScalar
nsConfigDnsPriSer=_NsConfigDnsPriSer_Object((1,3,6,1,4,1,3224,7,3,1),_NsConfigDnsPriSer_Type())
nsConfigDnsPriSer.setMaxAccess(_A)
if mibBuilder.loadTexts:nsConfigDnsPriSer.setStatus(_B)
_NsConfigDnsSecSer_Type=IpAddress
_NsConfigDnsSecSer_Object=MibScalar
nsConfigDnsSecSer=_NsConfigDnsSecSer_Object((1,3,6,1,4,1,3224,7,3,2),_NsConfigDnsSecSer_Type())
nsConfigDnsSecSer.setMaxAccess(_A)
if mibBuilder.loadTexts:nsConfigDnsSecSer.setStatus(_B)
class _NsConfigDnsRefEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('disable',0),('enabled',1)))
_NsConfigDnsRefEnable_Type.__name__=_C
_NsConfigDnsRefEnable_Object=MibScalar
nsConfigDnsRefEnable=_NsConfigDnsRefEnable_Object((1,3,6,1,4,1,3224,7,3,3),_NsConfigDnsRefEnable_Type())
nsConfigDnsRefEnable.setMaxAccess(_A)
if mibBuilder.loadTexts:nsConfigDnsRefEnable.setStatus(_B)
class _NsConfigDnsRefTime_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
_NsConfigDnsRefTime_Type.__name__=_D
_NsConfigDnsRefTime_Object=MibScalar
nsConfigDnsRefTime=_NsConfigDnsRefTime_Object((1,3,6,1,4,1,3224,7,3,4),_NsConfigDnsRefTime_Type())
nsConfigDnsRefTime.setMaxAccess(_A)
if mibBuilder.loadTexts:nsConfigDnsRefTime.setStatus(_B)
mibBuilder.exportSymbols('NETSCREEN-SET-DNS-MIB',**{'netscreenSetDnsMibModule':netscreenSetDnsMibModule,'nsSetDNS':nsSetDNS,'nsConfigDnsPriSer':nsConfigDnsPriSer,'nsConfigDnsSecSer':nsConfigDnsSecSer,'nsConfigDnsRefEnable':nsConfigDnsRefEnable,'nsConfigDnsRefTime':nsConfigDnsRefTime})