#
# PySNMP MIB module OXO-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/alcatel/OXO-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:40:02 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, enterprises, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "enterprises", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
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

mibBuilder.exportSymbols("OXO-MIB", aleCommunicationOXO=aleCommunicationOXO, PYSNMP_MODULE_ID=oxoMIB, oxoMIB=oxoMIB, ale=ale, EventSeverity=EventSeverity, ActivationStatus=ActivationStatus, PhysicalAddress=PhysicalAddress, aleCommunication=aleCommunication)
