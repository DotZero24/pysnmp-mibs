#
# PySNMP MIB module DNOS-TC (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/dell/DNOS-TC
# Produced by pysmi-1.1.12 at Thu Sep 11 10:23:22 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
dnOS, = mibBuilder.importSymbols("DELL-REF-MIB", "dnOS")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Integer32, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, TimeTicks, Bits, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Integer32", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "TimeTicks", "Bits", "IpAddress")
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

mibBuilder.exportSymbols("DNOS-TC", PYSNMP_MODULE_ID=fastPathTc, DeciInteger32=DeciInteger32, fastPathTc=fastPathTc, DBmTenths=DBmTenths, MilliInteger32=MilliInteger32, CentiInteger32=CentiInteger32, DBmHundreths=DBmHundreths)
