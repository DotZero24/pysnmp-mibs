_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
nmsModules,=mibBuilder.importSymbols('NMS-SMI','nmsModules')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
nmsTextualConventions=ModuleIdentity((1,3,6,1,4,1,3320,12,1))
if mibBuilder.loadTexts:nmsTextualConventions.setRevisions(('2003-10-16 00:00',))
class NMSNetworkProtocol(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,65535)));namedValues=NamedValues(*(('ip',1),('decnet',2),('pup',3),('chaos',4),('xns',5),('x121',6),('appletalk',7),('clns',8),('lat',9),('vines',10),('cons',11),('apollo',12),('stun',13),('novell',14),('qllc',15),('snapshot',16),('atmIlmi',17),('bstun',18),('x25pvc',19),('ipv6',20),('cdm',21),('nbf',22),('bpxIgx',23),('clnsPfx',24),('http',25),('unknown',65535)))
class NMSNetworkAddress(TextualConvention,OctetString):status=_A;displayHint='1x:'
class Unsigned64(TextualConvention,Counter64):status=_A
class InterfaceIndexOrZero(TextualConvention,Integer32):status=_A;displayHint='d';subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
class SAPType(TextualConvention,Integer32):status=_A;displayHint='d';subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,254))
class CountryCode(TextualConvention,OctetString):status=_A;displayHint='2a';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,0),ValueSizeConstraint(2,2))
class CountryCodeITU(TextualConvention,Unsigned32):status=_A;displayHint='d';subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
class EntPhysicalIndexOrZero(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
class NMSRowOperStatus(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('active',1),('activeDependencies',2),('inactiveDependency',3),('missingDependency',4)))
class NMSPort(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
class NMSIpProtocol(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
class NMSLocationClass(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('chassis',1),('shelf',2),('slot',3),('subSlot',4),('port',5),('subPort',6),('channel',7),('subChannel',8)))
class NMSLocationSpecifier(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
class NMSInetAddressMask(TextualConvention,Unsigned32):status=_A;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
class NMSAbsZeroBasedCounter32(TextualConvention,Gauge32):status=_A
class NMSSnapShotAbsCounter32(TextualConvention,Unsigned32):status=_A
class NMSAlarmSeverity(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('cleared',1),('indeterminate',2),('critical',3),('major',4),('minor',5),('warning',6),('info',7)))
class PerfHighIntervalCount(TextualConvention,Counter64):status=_A
class ConfigIterator(TextualConvention,Unsigned32):status=_A;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
class BulkConfigResult(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
class ListIndex(TextualConvention,Integer32):status=_A;displayHint='d';subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
class ListIndexOrZero(TextualConvention,Integer32):status=_A;displayHint='d';subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
class TimeIntervalSec(TextualConvention,Unsigned32):status=_A
class TimeIntervalMin(TextualConvention,Unsigned32):status=_A
class NMSMilliSeconds(TextualConvention,Unsigned32):status=_A
class MicroSeconds(TextualConvention,Unsigned32):status=_A
mibBuilder.exportSymbols('NMS-TC',**{'NMSNetworkProtocol':NMSNetworkProtocol,'NMSNetworkAddress':NMSNetworkAddress,'Unsigned64':Unsigned64,'InterfaceIndexOrZero':InterfaceIndexOrZero,'SAPType':SAPType,'CountryCode':CountryCode,'CountryCodeITU':CountryCodeITU,'EntPhysicalIndexOrZero':EntPhysicalIndexOrZero,'NMSRowOperStatus':NMSRowOperStatus,'NMSPort':NMSPort,'NMSIpProtocol':NMSIpProtocol,'NMSLocationClass':NMSLocationClass,'NMSLocationSpecifier':NMSLocationSpecifier,'NMSInetAddressMask':NMSInetAddressMask,'NMSAbsZeroBasedCounter32':NMSAbsZeroBasedCounter32,'NMSSnapShotAbsCounter32':NMSSnapShotAbsCounter32,'NMSAlarmSeverity':NMSAlarmSeverity,'PerfHighIntervalCount':PerfHighIntervalCount,'ConfigIterator':ConfigIterator,'BulkConfigResult':BulkConfigResult,'ListIndex':ListIndex,'ListIndexOrZero':ListIndexOrZero,'TimeIntervalSec':TimeIntervalSec,'TimeIntervalMin':TimeIntervalMin,'NMSMilliSeconds':NMSMilliSeconds,'MicroSeconds':MicroSeconds,'nmsTextualConventions':nmsTextualConventions})