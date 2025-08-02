_M='l2RadiusSubscriber'
_L='l2Dhcpv4Subscriber'
_K='l2MacSubscriber'
_J='ipRadiusSubscriber'
_I='ipDhcpv4Subscriber'
_H='ipPktSubscriber'
_G='ipInterfaceSubscriber'
_F='l2fSubscriber'
_E='l2tpSubscriber'
_D='pppoeSubscriber'
_C='pppSubscriber'
_B='other'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
ciscoSubscriberSessionTcMIB=ModuleIdentity((1,3,6,1,4,1,9,9,785))
if mibBuilder.loadTexts:ciscoSubscriberSessionTcMIB.setRevisions(('2007-09-26 00:00',))
class SubSessionType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13)));namedValues=NamedValues(*(('all',1),(_B,2),(_C,3),(_D,4),(_E,5),(_F,6),(_G,7),(_H,8),(_I,9),(_J,10),(_K,11),(_L,12),(_M,13)))
class SubSessionTypes(TextualConvention,Bits):status=_A;namedValues=NamedValues(*((_C,0),(_D,1),(_E,2),(_F,3),(_G,4),(_H,5),(_I,6),(_J,7),(_K,8),(_L,9),(_M,10)))
class SubSessionState(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_B,1),('pending',2),('up',3)))
class SubSessionRedundancyMode(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('none',1),(_B,2),('active',3),('standby',4)))
mibBuilder.exportSymbols('CISCO-SUBSCRIBER-SESSION-TC-MIB',**{'SubSessionType':SubSessionType,'SubSessionTypes':SubSessionTypes,'SubSessionState':SubSessionState,'SubSessionRedundancyMode':SubSessionRedundancyMode,'ciscoSubscriberSessionTcMIB':ciscoSubscriberSessionTcMIB})