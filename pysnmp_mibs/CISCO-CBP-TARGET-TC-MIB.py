_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
ciscoCbpTargetTCMIB=ModuleIdentity((1,3,6,1,4,1,9,9,511))
if mibBuilder.loadTexts:ciscoCbpTargetTCMIB.setRevisions(('2006-03-24 00:00',))
class CcbptTargetType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('genIf',1),('atmPvc',2),('frDlci',3),('entity',4),('fwZone',5),('fwZonePair',6),('aaaSession',7)))
class CcbptTargetDirection(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('undirected',1),('input',2),('output',3),('inOut',4)))
class CcbptTargetId(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
class CcbptTargetIdIf(TextualConvention,OctetString):status=_A;displayHint='4d';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
class CcbptTargetIdAtmPvc(TextualConvention,OctetString):status=_A;displayHint='4d:2d:2d';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
class CcbptTargetIdFrDlci(TextualConvention,OctetString):status=_A;displayHint='4d:2d';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
class CcbptTargetIdEntity(TextualConvention,OctetString):status=_A;displayHint='4d';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
class CcbptTargetIdNameString(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
class CcbptTargetIdAaaSession(TextualConvention,OctetString):status=_A;displayHint='4d';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
class CcbptPolicySourceType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('ciscoCbQos',1),('ciscoCbpBase',2)))
class CcbptPolicyIdentifier(TextualConvention,Unsigned32):status=_A;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
class CcbptPolicyIdentifierOrZero(TextualConvention,Unsigned32):status=_A;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
mibBuilder.exportSymbols('CISCO-CBP-TARGET-TC-MIB',**{'CcbptTargetType':CcbptTargetType,'CcbptTargetDirection':CcbptTargetDirection,'CcbptTargetId':CcbptTargetId,'CcbptTargetIdIf':CcbptTargetIdIf,'CcbptTargetIdAtmPvc':CcbptTargetIdAtmPvc,'CcbptTargetIdFrDlci':CcbptTargetIdFrDlci,'CcbptTargetIdEntity':CcbptTargetIdEntity,'CcbptTargetIdNameString':CcbptTargetIdNameString,'CcbptTargetIdAaaSession':CcbptTargetIdAaaSession,'CcbptPolicySourceType':CcbptPolicySourceType,'CcbptPolicyIdentifier':CcbptPolicyIdentifier,'CcbptPolicyIdentifierOrZero':CcbptPolicyIdentifierOrZero,'ciscoCbpTargetTCMIB':ciscoCbpTargetTCMIB})