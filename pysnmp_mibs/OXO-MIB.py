_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
oxoMIB=ModuleIdentity((1,3,6,1,4,1,6486,64,4200,1))
if mibBuilder.loadTexts:oxoMIB.setRevisions(('2015-03-20 14:24',))
class PhysicalAddress(TextualConvention,OctetString):status=_A;displayHint='1d.1d.1d';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(3,3));fixedLength=3
class EventSeverity(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6)));namedValues=NamedValues(*(('reserved',0),('critical',1),('major',2),('minor',3),('warning',4),('indeterminate',5),('clear',6)))
class ActivationStatus(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('inactive',0),('active',1),('unknown',2)))
_Ale_ObjectIdentity=ObjectIdentity
ale=_Ale_ObjectIdentity((1,3,6,1,4,1,6486))
_AleCommunication_ObjectIdentity=ObjectIdentity
aleCommunication=_AleCommunication_ObjectIdentity((1,3,6,1,4,1,6486,64))
_AleCommunicationOXO_ObjectIdentity=ObjectIdentity
aleCommunicationOXO=_AleCommunicationOXO_ObjectIdentity((1,3,6,1,4,1,6486,64,4200))
mibBuilder.exportSymbols('OXO-MIB',**{'PhysicalAddress':PhysicalAddress,'EventSeverity':EventSeverity,'ActivationStatus':ActivationStatus,'ale':ale,'aleCommunication':aleCommunication,'aleCommunicationOXO':aleCommunicationOXO,'oxoMIB':oxoMIB})