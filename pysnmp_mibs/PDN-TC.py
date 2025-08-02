_F='unknown'
_E='secondary'
_D='primary'
_C='disabled'
_B='enabled'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
class VnidMode(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('implicit',1),('explicit',2),('notagging',3)))
class ClientState(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('static',1),('dynamic',2)))
class VnidTaggingState(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_B,1),(_C,2)))
class VnidRange(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,4000))
class SwitchState(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_B,1),(_C,2)))
class ResetStates(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('noOp',1),('reset',2),('resetToFactoryDefaults',3),('resetToNewActiveConfig',4)))
class ResultTypes(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('none',1),('success',2),('failure',3),('inProgress',4)))
class InitiatorTypes(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('noop',1),('telnet',2),('console',3),('snmp',4)))
class NTPMode(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('unicast',1),('broadcast',2),('multicast',3)))
class DNSServerType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
class MibOidType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('scalar',1),('table',2),('mib',3),('section',4)))
class SocketType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_F,1),('stream',2),('datagram',3),('rawProtocol',4),('reliableMessageDelivery',5),('sequencedPacket',6)))
class SocketFamily(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23)));namedValues=NamedValues(*((_F,1),('unix',2),('darpaInternet',3),('darpaIMP',4),('pUP',5),('cHAOSFamily',6),('xeroxNovell',7),('nBS',8),('eCMA',9),('dATAKIT',10),('cCITT',11),('sNA',12),('dECnet',13),('directDataLinkInterface',14),('dECLAT',15),('nSCHyperChannel',16),('appleTalk',17),('netqorkInterfaceTap',18),('iEEE8020ISO8802',19),('oSI',20),('x25',21),('oSIAFI47IDI4',22),('uSGovermentOSI',23)))
class SocketState(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11)));namedValues=NamedValues(*(('closed',1),('listen',2),('sYNSent',3),('sYNRCVD',4),('established',5),('closeWait',6),('fINWait',7),('closing',8),('lastAck',9),('fINWait2',10),('timeWait',11)))
class DomainName(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
class SnmpAdminString(TextualConvention,OctetString):status=_A;displayHint='255a';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
class InetAddressType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
class ManagementType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('inband',1),('outband',2)))
class ContactState(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('open',1),('close',2)))
class IdslClockMode(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('triState',1),('portCardSinkClock',2),('portCardDriveClock',3),('portCardDriveClockOnboard',4)))
class TimeOfDay(TextualConvention,OctetString):status=_A;displayHint='1d:1d';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,2));fixedLength=2
class DayOfWeek(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('sunday',1),('monday',2),('tuesday',3),('wednesday',4),('thursday',5),('friday',6),('saturday',7),('daily',8)))
_Pdyn_ObjectIdentity=ObjectIdentity
pdyn=_Pdyn_ObjectIdentity((1,3,6,1,4,1,1795))
mibBuilder.exportSymbols('PDN-TC',**{'VnidMode':VnidMode,'ClientState':ClientState,'VnidTaggingState':VnidTaggingState,'VnidRange':VnidRange,'SwitchState':SwitchState,'ResetStates':ResetStates,'ResultTypes':ResultTypes,'InitiatorTypes':InitiatorTypes,'NTPMode':NTPMode,'DNSServerType':DNSServerType,'MibOidType':MibOidType,'SocketType':SocketType,'SocketFamily':SocketFamily,'SocketState':SocketState,'DomainName':DomainName,'SnmpAdminString':SnmpAdminString,'InetAddressType':InetAddressType,'ManagementType':ManagementType,'ContactState':ContactState,'IdslClockMode':IdslClockMode,'TimeOfDay':TimeOfDay,'DayOfWeek':DayOfWeek,'pdyn':pdyn})