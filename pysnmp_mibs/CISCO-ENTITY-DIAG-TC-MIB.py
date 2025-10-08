#
# PySNMP MIB module CISCO-ENTITY-DIAG-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/cisco/CISCO-ENTITY-DIAG-TC-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:29:09 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoEntityDiagTcMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 584))
ciscoEntityDiagTcMIB.setRevisions(('2009-07-01 00:00', '2006-12-21 00:00',))
if mibBuilder.loadTexts: ciscoEntityDiagTcMIB.setLastUpdated('200907010000Z')
if mibBuilder.loadTexts: ciscoEntityDiagTcMIB.setOrganization('Cisco Systems, Inc.')
class CeDiagDiagnosticLevel(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("bypass", 1), ("minimal", 2), ("complete", 3))

class CeDiagDiagnosticMethod(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("bootup", 1), ("onDemand", 2), ("scheduled", 3), ("healthMonitor", 4), ("none", 5))

class CeDiagTestIdentifier(TextualConvention, Unsigned32):
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 4294967295)

class CeDiagErrorIdentifier(TextualConvention, Unsigned32):
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 4294967295)

class CeDiagErrorIdentifierOrZero(TextualConvention, Unsigned32):
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 4294967295)

class CeDiagJobIdentifier(TextualConvention, Unsigned32):
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 4294967295)

class CeDiagPortList(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 32)

class CeDiagTestList(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 32)

class CeDiagJobSuite(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("none", 1), ("complete", 2), ("minimal", 3), ("nonDisruptive", 4), ("perPort", 5))

mibBuilder.exportSymbols("CISCO-ENTITY-DIAG-TC-MIB", CeDiagTestIdentifier=CeDiagTestIdentifier, CeDiagErrorIdentifierOrZero=CeDiagErrorIdentifierOrZero, CeDiagDiagnosticLevel=CeDiagDiagnosticLevel, PYSNMP_MODULE_ID=ciscoEntityDiagTcMIB, CeDiagDiagnosticMethod=CeDiagDiagnosticMethod, CeDiagJobIdentifier=CeDiagJobIdentifier, CeDiagPortList=CeDiagPortList, CeDiagTestList=CeDiagTestList, CeDiagErrorIdentifier=CeDiagErrorIdentifier, CeDiagJobSuite=CeDiagJobSuite, ciscoEntityDiagTcMIB=ciscoEntityDiagTcMIB)
