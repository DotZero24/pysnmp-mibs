#
# PySNMP MIB module CISCO-MPLS-TC-EXT-STD-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/cisco/CISCO-MPLS-TC-EXT-STD-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:12:15 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ciscoExperiment, = mibBuilder.importSymbols("CISCO-SMI", "ciscoExperiment")
mplsStdMIB, = mibBuilder.importSymbols("MPLS-TC-STD-MIB", "mplsStdMIB")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Unsigned32, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Unsigned32", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
cmplsTcExtStdMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 10, 144))
cmplsTcExtStdMIB.setRevisions(('2012-02-22 00:00',))
if mibBuilder.loadTexts: cmplsTcExtStdMIB.setLastUpdated('201202220000Z')
if mibBuilder.loadTexts: cmplsTcExtStdMIB.setOrganization('Multiprotocol Label Switching (MPLS) Working Group')
class CMplsGlobalId(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(4, 4)
    fixedLength = 4

class CMplsNodeId(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'd'

class CMplsIccId(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 6)

class CMplsLocalId(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 16777215)

mibBuilder.exportSymbols("CISCO-MPLS-TC-EXT-STD-MIB", CMplsIccId=CMplsIccId, cmplsTcExtStdMIB=cmplsTcExtStdMIB, CMplsGlobalId=CMplsGlobalId, PYSNMP_MODULE_ID=cmplsTcExtStdMIB, CMplsLocalId=CMplsLocalId, CMplsNodeId=CMplsNodeId)
