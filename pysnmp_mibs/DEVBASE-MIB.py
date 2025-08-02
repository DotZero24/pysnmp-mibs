_C='DisplayString'
_B='current'
_A='read-only'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
device,=mibBuilder.importSymbols('ANIROOT-MIB','device')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_C,'MacAddress','PhysAddress','TextualConvention')
aniDevBase=ModuleIdentity((1,3,6,1,4,1,4325,2,1))
class _AniDevProductName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_AniDevProductName_Type.__name__=_C
_AniDevProductName_Object=MibScalar
aniDevProductName=_AniDevProductName_Object((1,3,6,1,4,1,4325,2,1,1),_AniDevProductName_Type())
aniDevProductName.setMaxAccess(_A)
if mibBuilder.loadTexts:aniDevProductName.setStatus(_B)
_AniDevLanIpAddr_Type=IpAddress
_AniDevLanIpAddr_Object=MibScalar
aniDevLanIpAddr=_AniDevLanIpAddr_Object((1,3,6,1,4,1,4325,2,1,2),_AniDevLanIpAddr_Type())
aniDevLanIpAddr.setMaxAccess(_A)
if mibBuilder.loadTexts:aniDevLanIpAddr.setStatus(_B)
_AniDevLanSubnetMask_Type=IpAddress
_AniDevLanSubnetMask_Object=MibScalar
aniDevLanSubnetMask=_AniDevLanSubnetMask_Object((1,3,6,1,4,1,4325,2,1,3),_AniDevLanSubnetMask_Type())
aniDevLanSubnetMask.setMaxAccess(_A)
if mibBuilder.loadTexts:aniDevLanSubnetMask.setStatus(_B)
_AniDevDefaultGateway_Type=IpAddress
_AniDevDefaultGateway_Object=MibScalar
aniDevDefaultGateway=_AniDevDefaultGateway_Object((1,3,6,1,4,1,4325,2,1,4),_AniDevDefaultGateway_Type())
aniDevDefaultGateway.setMaxAccess(_A)
if mibBuilder.loadTexts:aniDevDefaultGateway.setStatus(_B)
_AniDevMacAddr_Type=MacAddress
_AniDevMacAddr_Object=MibScalar
aniDevMacAddr=_AniDevMacAddr_Object((1,3,6,1,4,1,4325,2,1,5),_AniDevMacAddr_Type())
aniDevMacAddr.setMaxAccess(_A)
if mibBuilder.loadTexts:aniDevMacAddr.setStatus(_B)
mibBuilder.exportSymbols('DEVBASE-MIB',**{'aniDevBase':aniDevBase,'aniDevProductName':aniDevProductName,'aniDevLanIpAddr':aniDevLanIpAddr,'aniDevLanSubnetMask':aniDevLanSubnetMask,'aniDevDefaultGateway':aniDevDefaultGateway,'aniDevMacAddr':aniDevMacAddr})