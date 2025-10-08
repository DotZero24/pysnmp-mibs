#
# PySNMP MIB module OXO-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/alcatel/OXO-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 11:06:47 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, enterprises, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "enterprises", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
oxoMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 6486, 64, 4200, 1))
oxoMIB.setRevisions(('2015-03-20 14:24',))
if mibBuilder.loadTexts: oxoMIB.setLastUpdated('201503201424Z')
if mibBuilder.loadTexts: oxoMIB.setOrganization('ALE Communication')
aleCommunicationOXO = MibIdentifier((1, 3, 6, 1, 4, 1, 6486, 64, 4200))
aleCommunication = MibIdentifier((1, 3, 6, 1, 4, 1, 6486, 64))
ale = MibIdentifier((1, 3, 6, 1, 4, 1, 6486))
class PhysicalAddress(TextualConvention, OctetString):
    status = 'current'
    displayHint = '1d.1d.1d'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(3, 3)
    fixedLength = 3

class EventSeverity(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("reserved", 0), ("critical", 1), ("major", 2), ("minor", 3), ("warning", 4), ("indeterminate", 5), ("clear", 6))

class ActivationStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("inactive", 0), ("active", 1), ("unknown", 2))

mibBuilder.exportSymbols("OXO-MIB", aleCommunication=aleCommunication, ActivationStatus=ActivationStatus, PhysicalAddress=PhysicalAddress, aleCommunicationOXO=aleCommunicationOXO, PYSNMP_MODULE_ID=oxoMIB, oxoMIB=oxoMIB, ale=ale, EventSeverity=EventSeverity)
