_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ericssonModules,=mibBuilder.importSymbols('ERICSSON-TOP-MIB','ericssonModules')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
ericssonAlarmTCMIB=ModuleIdentity((1,3,6,1,4,1,193,183,3))
if mibBuilder.loadTexts:ericssonAlarmTCMIB.setRevisions(('2008-10-17 00:00',))
class EriAlarmType(TextualConvention,Unsigned32):status=_A;displayHint='d'
class EriAlarmIndex(TextualConvention,Unsigned32):status=_A;displayHint='d'
class EriAdditionalText(TextualConvention,OctetString):status=_A;displayHint='1a';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,256))
class EriLargeAdditionalText(TextualConvention,OctetString):status=_A;displayHint='1a';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,512))
class EriAlarmSpecificProblem(TextualConvention,OctetString):status=_A;displayHint='1a';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,64))
class EriAlarmSequenceNumber(TextualConvention,Unsigned32):status=_A;displayHint='d'
mibBuilder.exportSymbols('ERICSSON-ALARM-TC-MIB',**{'EriAlarmType':EriAlarmType,'EriAlarmIndex':EriAlarmIndex,'EriAdditionalText':EriAdditionalText,'EriLargeAdditionalText':EriLargeAdditionalText,'EriAlarmSpecificProblem':EriAlarmSpecificProblem,'EriAlarmSequenceNumber':EriAlarmSequenceNumber,'ericssonAlarmTCMIB':ericssonAlarmTCMIB})