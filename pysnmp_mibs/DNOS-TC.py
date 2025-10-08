#
# PySNMP MIB module DNOS-TC (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/dell/DNOS-TC
# Produced by pysmi-1.1.12 at Wed Oct  8 10:43:29 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
dnOS, = mibBuilder.importSymbols("DELL-REF-MIB", "dnOS")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
fastPathTc = ModuleIdentity((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 99))
fastPathTc.setRevisions(('2020-04-21 00:00',))
if mibBuilder.loadTexts: fastPathTc.setLastUpdated('202004210000Z')
if mibBuilder.loadTexts: fastPathTc.setOrganization('Dell')
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

mibBuilder.exportSymbols("DNOS-TC", fastPathTc=fastPathTc, DBmHundreths=DBmHundreths, CentiInteger32=CentiInteger32, MilliInteger32=MilliInteger32, DBmTenths=DBmTenths, DeciInteger32=DeciInteger32, PYSNMP_MODULE_ID=fastPathTc)
