_C='inactive'
_B='active'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
pktcEUEMibs,=mibBuilder.importSymbols('CLAB-DEF-MIB','pktcEUEMibs')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
pktcEUETCMIB=ModuleIdentity((1,3,6,1,4,1,4491,2,2,10,2))
if mibBuilder.loadTexts:pktcEUETCMIB.setRevisions(('2008-07-10 00:00','2007-11-06 00:00'))
class PktcEUETCID(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,1023))
class PktcEUETCIDType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('other',1),('gruu',2),('publicIdentity',3),('privateIdentity',4),('publicPrivatePair',5),('username',6),('macaddress',7),('packetcableIdentity',8)))
class PktcEUETCAdminStatus(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_B,1),(_C,2)))
class PktcEUETCOperStatus(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_B,1),(_C,2),('notPresent',3),('unknown',4)))
class PktcEUETCStatusInfo(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
class PktcEUETCUsrElementIndexType(TextualConvention,Unsigned32):status=_A;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
class PktcEUETCAppOrgIdentifier(TextualConvention,Unsigned32):status=_A
class PktcEUETCAppIdentifier(TextualConvention,Unsigned32):status=_A;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,127))
class PktcEUETCUsrAppIndexType(TextualConvention,Unsigned32):status=_A;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,31))
class PktcEUETCCredsType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('other',1),('none',2),('password',3),('preSharedKey',4),('certificate',5)))
class PktcEUETCCreds(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8192))
_PktcEUETCNotifications_ObjectIdentity=ObjectIdentity
pktcEUETCNotifications=_PktcEUETCNotifications_ObjectIdentity((1,3,6,1,4,1,4491,2,2,10,2,0))
_PktcEUETCObjects_ObjectIdentity=ObjectIdentity
pktcEUETCObjects=_PktcEUETCObjects_ObjectIdentity((1,3,6,1,4,1,4491,2,2,10,2,1))
_PktcEUETCUsageObjs_ObjectIdentity=ObjectIdentity
pktcEUETCUsageObjs=_PktcEUETCUsageObjs_ObjectIdentity((1,3,6,1,4,1,4491,2,2,10,2,1,1))
_PktcEUETCConformance_ObjectIdentity=ObjectIdentity
pktcEUETCConformance=_PktcEUETCConformance_ObjectIdentity((1,3,6,1,4,1,4491,2,2,10,2,2))
_PktcEUETCCompliances_ObjectIdentity=ObjectIdentity
pktcEUETCCompliances=_PktcEUETCCompliances_ObjectIdentity((1,3,6,1,4,1,4491,2,2,10,2,2,1))
_PktcEUETCGroups_ObjectIdentity=ObjectIdentity
pktcEUETCGroups=_PktcEUETCGroups_ObjectIdentity((1,3,6,1,4,1,4491,2,2,10,2,2,2))
mibBuilder.exportSymbols('CL-PKTC-EUE-TC-MIB',**{'PktcEUETCID':PktcEUETCID,'PktcEUETCIDType':PktcEUETCIDType,'PktcEUETCAdminStatus':PktcEUETCAdminStatus,'PktcEUETCOperStatus':PktcEUETCOperStatus,'PktcEUETCStatusInfo':PktcEUETCStatusInfo,'PktcEUETCUsrElementIndexType':PktcEUETCUsrElementIndexType,'PktcEUETCAppOrgIdentifier':PktcEUETCAppOrgIdentifier,'PktcEUETCAppIdentifier':PktcEUETCAppIdentifier,'PktcEUETCUsrAppIndexType':PktcEUETCUsrAppIndexType,'PktcEUETCCredsType':PktcEUETCCredsType,'PktcEUETCCreds':PktcEUETCCreds,'pktcEUETCMIB':pktcEUETCMIB,'pktcEUETCNotifications':pktcEUETCNotifications,'pktcEUETCObjects':pktcEUETCObjects,'pktcEUETCUsageObjs':pktcEUETCUsageObjs,'pktcEUETCConformance':pktcEUETCConformance,'pktcEUETCCompliances':pktcEUETCCompliances,'pktcEUETCGroups':pktcEUETCGroups})