_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dnOS,=mibBuilder.importSymbols('DELL-REF-MIB','dnOS')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
fastPathTc=ModuleIdentity((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,99))
if mibBuilder.loadTexts:fastPathTc.setRevisions(('2020-04-21 00:00',))
class DeciInteger32(TextualConvention,Integer32):status=_A;displayHint='d-1'
class CentiInteger32(TextualConvention,Integer32):status=_A;displayHint='d-2'
class MilliInteger32(TextualConvention,Integer32):status=_A;displayHint='d-3'
class DBmTenths(TextualConvention,Integer32):status=_A;displayHint='d-1'
class DBmHundreths(TextualConvention,Integer32):status=_A;displayHint='d-3'
mibBuilder.exportSymbols('DNOS-TC',**{'DeciInteger32':DeciInteger32,'CentiInteger32':CentiInteger32,'MilliInteger32':MilliInteger32,'DBmTenths':DBmTenths,'DBmHundreths':DBmHundreths,'fastPathTc':fastPathTc})