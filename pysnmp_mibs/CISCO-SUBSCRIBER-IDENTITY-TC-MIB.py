_U='tunnelName'
_T='dhcpClass'
_S='serviceName'
_R='protocol'
_Q='mlpNegotiated'
_P='acctSessionId'
_O='username'
_N='domain'
_M='nasPort'
_L='circuitId'
_K='remoteId'
_J='domainIpAddress'
_I='domainVrf'
_H='nativeIpAddress'
_G='nativeVrf'
_F='macAddress'
_E='subscriberLabel'
_D='ifIndex'
_C='other'
_B='255a'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
ciscoSubscriberIdentityTcMIB=ModuleIdentity((1,3,6,1,4,1,9,9,782))
if mibBuilder.loadTexts:ciscoSubscriberIdentityTcMIB.setRevisions(('2011-12-23 00:00',))
class SubSessionIdentity(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22)));namedValues=NamedValues(*((_C,1),(_D,2),(_E,3),(_F,4),(_G,5),(_H,6),(_I,7),(_J,8),('pbhk',9),(_K,10),(_L,11),(_M,12),(_N,13),(_O,14),(_P,15),('dnis',16),('media',17),(_Q,18),(_R,19),(_S,20),(_T,21),(_U,22)))
class SubSessionIdentities(TextualConvention,Bits):status=_A;namedValues=NamedValues(*((_D,0),(_E,1),(_F,2),(_G,3),(_H,4),(_I,5),(_J,6),('pbhk',7),(_K,8),(_L,9),(_M,10),(_N,11),(_O,12),(_P,13),('dnis',14),('media',15),(_Q,16),(_R,17),(_S,18),(_T,19),(_U,20)))
class SubscriberLabel(TextualConvention,Unsigned32):status=_A;displayHint='x';subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
class SubscriberVRF(TextualConvention,OctetString):status=_A;displayHint=_B;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
class SubscriberPbhk(TextualConvention,OctetString):status=_A;displayHint='1x:';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
class SubscriberRemoteId(TextualConvention,OctetString):status=_A;displayHint=_B;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
class SubscriberCircuitId(TextualConvention,OctetString):status=_A;displayHint=_B;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
class SubscriberNasPort(TextualConvention,OctetString):status=_A;displayHint='1x:';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
class SubscriberDomain(TextualConvention,OctetString):status=_A;displayHint=_B;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
class SubscriberUsername(TextualConvention,OctetString):status=_A;displayHint=_B;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
class SubscriberAcctSessionId(TextualConvention,Unsigned32):status=_A;displayHint='x';subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
class SubscriberDnis(TextualConvention,OctetString):status=_A;displayHint=_B;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
class SubscriberMediaType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_C,1),('async',2),('atm',3),('ethernet',4),('ip',5),('isdn',6),('mpls',7),('sync',8)))
class SubscriberProtocolType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_C,1),('atom',2),('ip',3),('psdn',4),('ppp',5),('vpdn',6)))
class SubscriberDhcpClass(TextualConvention,OctetString):status=_A;displayHint=_B;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
class SubscriberTunnelName(TextualConvention,OctetString):status=_A;displayHint=_B;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
class SubscriberLocationName(TextualConvention,OctetString):status=_A;displayHint=_B;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
class SubscriberServiceName(TextualConvention,OctetString):status=_A;displayHint=_B;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
mibBuilder.exportSymbols('CISCO-SUBSCRIBER-IDENTITY-TC-MIB',**{'SubSessionIdentity':SubSessionIdentity,'SubSessionIdentities':SubSessionIdentities,'SubscriberLabel':SubscriberLabel,'SubscriberVRF':SubscriberVRF,'SubscriberPbhk':SubscriberPbhk,'SubscriberRemoteId':SubscriberRemoteId,'SubscriberCircuitId':SubscriberCircuitId,'SubscriberNasPort':SubscriberNasPort,'SubscriberDomain':SubscriberDomain,'SubscriberUsername':SubscriberUsername,'SubscriberAcctSessionId':SubscriberAcctSessionId,'SubscriberDnis':SubscriberDnis,'SubscriberMediaType':SubscriberMediaType,'SubscriberProtocolType':SubscriberProtocolType,'SubscriberDhcpClass':SubscriberDhcpClass,'SubscriberTunnelName':SubscriberTunnelName,'SubscriberLocationName':SubscriberLocationName,'SubscriberServiceName':SubscriberServiceName,'ciscoSubscriberIdentityTcMIB':ciscoSubscriberIdentityTcMIB})