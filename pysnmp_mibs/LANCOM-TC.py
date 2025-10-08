#
# PySNMP MIB module LANCOM-TC (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/lancom/LANCOM-TC
# Produced by pysmi-1.1.12 at Wed Oct  8 11:11:38 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
fastPath, = mibBuilder.importSymbols("LANCOM-REF-MIB", "fastPath")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
fastPathTc = ModuleIdentity((1, 3, 6, 1, 4, 1, 2356, 16, 1, 99))
fastPathTc.setRevisions(('2020-04-21 00:00',))
if mibBuilder.loadTexts: fastPathTc.setLastUpdated('202004210000Z')
if mibBuilder.loadTexts: fastPathTc.setOrganization('Broadcom')
class DeciInteger32(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd-1'

class CentiInteger32(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd-2'

class MilliInteger32(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd-3'

class DBmTenths(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd-1'

class DBmHundreths(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd-3'

mibBuilder.exportSymbols("LANCOM-TC", fastPathTc=fastPathTc, DBmHundreths=DBmHundreths, CentiInteger32=CentiInteger32, MilliInteger32=MilliInteger32, DBmTenths=DBmTenths, DeciInteger32=DeciInteger32, PYSNMP_MODULE_ID=fastPathTc)
