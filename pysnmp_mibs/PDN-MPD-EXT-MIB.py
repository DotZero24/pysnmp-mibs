_D='pdnMpdExtGroup'
_C='pdnMpdExtSecurityModeConfig'
_B='PDN-MPD-EXT-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
pdnMpdExt,=mibBuilder.importSymbols('PDN-HEADER-MIB','pdnMpdExt')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
pdnMpdExtMIB=ModuleIdentity((1,3,6,1,4,1,1795,2,24,2,44,1))
class PdnMpdExtSecurityMode(TextualConvention,Bits):status=_A;namedValues=NamedValues(*(('none',0),('snmpv1NoAuthNoPriv',1),('snmpv2cNoAuthNoPriv',2),('snmpv3NoAuthNoPriv',3),('snmpv3AuthNoPriv',4),('snmpv3AuthPriv',5)))
_PdnMpdExtMIBObjects_ObjectIdentity=ObjectIdentity
pdnMpdExtMIBObjects=_PdnMpdExtMIBObjects_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,44,1,1))
_PdnMpdExtSecurityModeConfig_Type=PdnMpdExtSecurityMode
_PdnMpdExtSecurityModeConfig_Object=MibScalar
pdnMpdExtSecurityModeConfig=_PdnMpdExtSecurityModeConfig_Object((1,3,6,1,4,1,1795,2,24,2,44,1,1,1),_PdnMpdExtSecurityModeConfig_Type())
pdnMpdExtSecurityModeConfig.setMaxAccess('read-write')
if mibBuilder.loadTexts:pdnMpdExtSecurityModeConfig.setStatus(_A)
_PdnMpdExtMIBConformance_ObjectIdentity=ObjectIdentity
pdnMpdExtMIBConformance=_PdnMpdExtMIBConformance_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,44,1,2))
_PdnMpdExtCompliances_ObjectIdentity=ObjectIdentity
pdnMpdExtCompliances=_PdnMpdExtCompliances_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,44,1,2,1))
_PdnMpdExtGroups_ObjectIdentity=ObjectIdentity
pdnMpdExtGroups=_PdnMpdExtGroups_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,44,1,2,2))
pdnMpdExtGroup=ObjectGroup((1,3,6,1,4,1,1795,2,24,2,44,1,2,2,1))
pdnMpdExtGroup.setObjects((_B,_C))
if mibBuilder.loadTexts:pdnMpdExtGroup.setStatus(_A)
pdnMpdExtCompliance=ModuleCompliance((1,3,6,1,4,1,1795,2,24,2,44,1,2,1,1))
pdnMpdExtCompliance.setObjects((_B,_D))
if mibBuilder.loadTexts:pdnMpdExtCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'PdnMpdExtSecurityMode':PdnMpdExtSecurityMode,'pdnMpdExtMIB':pdnMpdExtMIB,'pdnMpdExtMIBObjects':pdnMpdExtMIBObjects,_C:pdnMpdExtSecurityModeConfig,'pdnMpdExtMIBConformance':pdnMpdExtMIBConformance,'pdnMpdExtCompliances':pdnMpdExtCompliances,'pdnMpdExtCompliance':pdnMpdExtCompliance,'pdnMpdExtGroups':pdnMpdExtGroups,_D:pdnMpdExtGroup})