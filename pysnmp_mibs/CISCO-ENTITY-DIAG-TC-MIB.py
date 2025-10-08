#
# PySNMP MIB module CISCO-ENTITY-DIAG-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/cisco/CISCO-ENTITY-DIAG-TC-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:14:43 2025
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

mibBuilder.exportSymbols("CISCO-ENTITY-DIAG-TC-MIB", CeDiagJobIdentifier=CeDiagJobIdentifier, CeDiagErrorIdentifier=CeDiagErrorIdentifier, CeDiagErrorIdentifierOrZero=CeDiagErrorIdentifierOrZero, ciscoEntityDiagTcMIB=ciscoEntityDiagTcMIB, CeDiagDiagnosticMethod=CeDiagDiagnosticMethod, CeDiagTestIdentifier=CeDiagTestIdentifier, PYSNMP_MODULE_ID=ciscoEntityDiagTcMIB, CeDiagPortList=CeDiagPortList, CeDiagJobSuite=CeDiagJobSuite, CeDiagTestList=CeDiagTestList, CeDiagDiagnosticLevel=CeDiagDiagnosticLevel)
