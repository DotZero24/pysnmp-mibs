_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
mimosa,=mibBuilder.importSymbols('MIMOSA-NETWORKS-BASE-MIB','mimosa')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
mimosaMibTC=ModuleIdentity((1,3,6,1,4,1,43356,3))
if mibBuilder.loadTexts:mimosaMibTC.setRevisions(('2017-02-15 00:00',))
class DecimalOne(TextualConvention,Integer32):status=_A;displayHint='d-1'
class DecimalTwo(TextualConvention,Integer32):status=_A;displayHint='d-2'
class DecimalFive(TextualConvention,Integer32):status=_A;displayHint='d-5'
class Mimosa5GHzFrequency(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(4800,6200))
class Mimosa5GHzChannelNumber(TextualConvention,Integer32):status=_A
mibBuilder.exportSymbols('MIMOSA-MIB-TC',**{'DecimalOne':DecimalOne,'DecimalTwo':DecimalTwo,'DecimalFive':DecimalFive,'Mimosa5GHzFrequency':Mimosa5GHzFrequency,'Mimosa5GHzChannelNumber':Mimosa5GHzChannelNumber,'mimosaMibTC':mimosaMibTC})