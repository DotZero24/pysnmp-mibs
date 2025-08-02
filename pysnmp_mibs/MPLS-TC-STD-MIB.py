_B='unknown'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso,transmission=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso','transmission')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
mplsTCStdMIB=ModuleIdentity((1,3,6,1,2,1,10,166,1))
if mibBuilder.loadTexts:mplsTCStdMIB.setRevisions(('2004-06-03 00:00',))
class MplsAtmVcIdentifier(TextualConvention,Integer32):status=_A;displayHint='d';subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(32,65535))
class MplsBitRate(TextualConvention,Unsigned32):status=_A;displayHint='d';subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,4294967295))
class MplsBurstSize(TextualConvention,Unsigned32):status=_A;displayHint='d';subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
class MplsExtendedTunnelId(TextualConvention,Unsigned32):status=_A;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
class MplsLabel(TextualConvention,Unsigned32):status=_A;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
class MplsLabelDistributionMethod(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('downstreamOnDemand',1),('downstreamUnsolicited',2)))
class MplsLdpIdentifier(TextualConvention,OctetString):status=_A;displayHint='1d.1d.1d.1d:2d';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
class MplsLsrIdentifier(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
class MplsLdpLabelType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('generic',1),('atm',2),('frameRelay',3)))
class MplsLSPID(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,2),ValueSizeConstraint(6,6))
class MplsLspType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_B,1),('terminatingLsp',2),('originatingLsp',3),('crossConnectingLsp',4)))
class MplsOwner(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_B,1),('other',2),('snmp',3),('ldp',4),('crldp',5),('rsvpTe',6),('policyAgent',7)))
class MplsPathIndexOrZero(TextualConvention,Unsigned32):status=_A;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
class MplsPathIndex(TextualConvention,Unsigned32):status=_A;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
class MplsRetentionMode(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('conservative',1),('liberal',2)))
class MplsTunnelAffinity(TextualConvention,Unsigned32):status=_A;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
class MplsTunnelIndex(TextualConvention,Unsigned32):status=_A;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
class MplsTunnelInstanceIndex(TextualConvention,Unsigned32):status=_A;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,65535),ValueRangeConstraint(65536,4294967295))
class TeHopAddressType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*((_B,0),('ipv4',1),('ipv6',2),('asnumber',3),('unnum',4),('lspid',5)))
class TeHopAddress(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
class TeHopAddressAS(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
class TeHopAddressUnnum(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
_MplsStdMIB_ObjectIdentity=ObjectIdentity
mplsStdMIB=_MplsStdMIB_ObjectIdentity((1,3,6,1,2,1,10,166))
mibBuilder.exportSymbols('MPLS-TC-STD-MIB',**{'MplsAtmVcIdentifier':MplsAtmVcIdentifier,'MplsBitRate':MplsBitRate,'MplsBurstSize':MplsBurstSize,'MplsExtendedTunnelId':MplsExtendedTunnelId,'MplsLabel':MplsLabel,'MplsLabelDistributionMethod':MplsLabelDistributionMethod,'MplsLdpIdentifier':MplsLdpIdentifier,'MplsLsrIdentifier':MplsLsrIdentifier,'MplsLdpLabelType':MplsLdpLabelType,'MplsLSPID':MplsLSPID,'MplsLspType':MplsLspType,'MplsOwner':MplsOwner,'MplsPathIndexOrZero':MplsPathIndexOrZero,'MplsPathIndex':MplsPathIndex,'MplsRetentionMode':MplsRetentionMode,'MplsTunnelAffinity':MplsTunnelAffinity,'MplsTunnelIndex':MplsTunnelIndex,'MplsTunnelInstanceIndex':MplsTunnelInstanceIndex,'TeHopAddressType':TeHopAddressType,'TeHopAddress':TeHopAddress,'TeHopAddressAS':TeHopAddressAS,'TeHopAddressUnnum':TeHopAddressUnnum,'mplsStdMIB':mplsStdMIB,'mplsTCStdMIB':mplsTCStdMIB})