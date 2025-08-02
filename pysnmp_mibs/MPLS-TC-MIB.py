_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso,transmission=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso','transmission')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
mplsTCMIB=ModuleIdentity((1,3,6,1,2,1,10,9999,1))
if mibBuilder.loadTexts:mplsTCMIB.setRevisions(('2001-01-04 12:00',))
class MplsAtmVcIdentifier(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(32,65535))
class MplsBitRate(TextualConvention,Integer32):status=_A;displayHint='d';subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
class MplsBurstSize(TextualConvention,Unsigned32):status=_A;displayHint='d';subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
class MplsExtendedTunnelId(TextualConvention,Unsigned32):status=_A
class MplsInitialCreationSource(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('other',1),('snmp',2),('ldp',3),('rsvp',4),('crldp',5),('policyAgent',6),('unknown',7)))
class MplsLSPID(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
class MplsLabel(TextualConvention,Unsigned32):status=_A;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
class MplsLdpGenAddr(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
class MplsLdpIdentifier(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
class MplsLdpLabelTypes(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('generic',1),('atm',2),('frameRelay',3)))
class MplsLsrIdentifier(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
class MplsPathIndex(TextualConvention,Unsigned32):status=_A
class MplsPathIndexOrZero(TextualConvention,Unsigned32):status=_A
class MplsPortNumber(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
class MplsTunnelAffinity(TextualConvention,Unsigned32):status=_A
class MplsTunnelIndex(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
class MplsTunnelInstanceIndex(TextualConvention,Unsigned32):status=_A;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_MplsMIB_ObjectIdentity=ObjectIdentity
mplsMIB=_MplsMIB_ObjectIdentity((1,3,6,1,2,1,10,9999))
mibBuilder.exportSymbols('MPLS-TC-MIB',**{'MplsAtmVcIdentifier':MplsAtmVcIdentifier,'MplsBitRate':MplsBitRate,'MplsBurstSize':MplsBurstSize,'MplsExtendedTunnelId':MplsExtendedTunnelId,'MplsInitialCreationSource':MplsInitialCreationSource,'MplsLSPID':MplsLSPID,'MplsLabel':MplsLabel,'MplsLdpGenAddr':MplsLdpGenAddr,'MplsLdpIdentifier':MplsLdpIdentifier,'MplsLdpLabelTypes':MplsLdpLabelTypes,'MplsLsrIdentifier':MplsLsrIdentifier,'MplsPathIndex':MplsPathIndex,'MplsPathIndexOrZero':MplsPathIndexOrZero,'MplsPortNumber':MplsPortNumber,'MplsTunnelAffinity':MplsTunnelAffinity,'MplsTunnelIndex':MplsTunnelIndex,'MplsTunnelInstanceIndex':MplsTunnelInstanceIndex,'mplsMIB':mplsMIB,'mplsTCMIB':mplsTCMIB})