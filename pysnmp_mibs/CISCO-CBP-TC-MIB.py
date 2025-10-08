#
# PySNMP MIB module CISCO-CBP-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/cisco/CISCO-CBP-TC-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:16:11 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Unsigned32, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Unsigned32", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoCbpTcMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 662))
ciscoCbpTcMIB.setRevisions(('2008-06-24 00:00',))
if mibBuilder.loadTexts: ciscoCbpTcMIB.setLastUpdated('200806240000Z')
if mibBuilder.loadTexts: ciscoCbpTcMIB.setOrganization('Cisco Systems, Inc.')
class CbpElementName(TextualConvention, OctetString):
    reference = "D. Harrington, R. Resuhn, B. Wijnen, 'An Architecture for Describing Simple Network Management Protocol (SNMP) Management Frameworks', RFC-3411, December 2002."
    status = 'current'
    displayHint = '127a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 127)

class CbpElementIdentifier(TextualConvention, Unsigned32):
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 4294967295)

class CbpElementIdentifierOrZero(TextualConvention, Unsigned32):
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 4294967295)

class CbpInstanceIdentifier(TextualConvention, Unsigned32):
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 4294967295)

class CbpInstanceIdentifierOrZero(TextualConvention, Unsigned32):
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 4294967295)

class CbpExecutionPriority(TextualConvention, Unsigned32):
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 4294967295)

class CbpExecutionStrategy(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("other", 1), ("doUntilSuccess", 2), ("doUntilFailure", 3), ("doAll", 4))

mibBuilder.exportSymbols("CISCO-CBP-TC-MIB", CbpInstanceIdentifier=CbpInstanceIdentifier, CbpElementName=CbpElementName, ciscoCbpTcMIB=ciscoCbpTcMIB, CbpInstanceIdentifierOrZero=CbpInstanceIdentifierOrZero, CbpExecutionPriority=CbpExecutionPriority, CbpElementIdentifier=CbpElementIdentifier, CbpElementIdentifierOrZero=CbpElementIdentifierOrZero, CbpExecutionStrategy=CbpExecutionStrategy, PYSNMP_MODULE_ID=ciscoCbpTcMIB)
