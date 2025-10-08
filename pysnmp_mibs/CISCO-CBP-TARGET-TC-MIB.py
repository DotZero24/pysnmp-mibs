#
# PySNMP MIB module CISCO-CBP-TARGET-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/cisco/CISCO-CBP-TARGET-TC-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:31:02 2025
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
ciscoCbpTargetTCMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 511))
ciscoCbpTargetTCMIB.setRevisions(('2006-03-24 00:00',))
if mibBuilder.loadTexts: ciscoCbpTargetTCMIB.setLastUpdated('200603240000Z')
if mibBuilder.loadTexts: ciscoCbpTargetTCMIB.setOrganization('Cisco Systems, Inc.')
class CcbptTargetType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("genIf", 1), ("atmPvc", 2), ("frDlci", 3), ("entity", 4), ("fwZone", 5), ("fwZonePair", 6), ("aaaSession", 7))

class CcbptTargetDirection(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("undirected", 1), ("input", 2), ("output", 3), ("inOut", 4))

class CcbptTargetId(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 64)

class CcbptTargetIdIf(TextualConvention, OctetString):
    status = 'current'
    displayHint = '4d'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(4, 4)
    fixedLength = 4

class CcbptTargetIdAtmPvc(TextualConvention, OctetString):
    status = 'current'
    displayHint = '4d:2d:2d'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(8, 8)
    fixedLength = 8

class CcbptTargetIdFrDlci(TextualConvention, OctetString):
    status = 'current'
    displayHint = '4d:2d'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(6, 6)
    fixedLength = 6

class CcbptTargetIdEntity(TextualConvention, OctetString):
    status = 'current'
    displayHint = '4d'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(4, 4)
    fixedLength = 4

class CcbptTargetIdNameString(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 64)

class CcbptTargetIdAaaSession(TextualConvention, OctetString):
    status = 'current'
    displayHint = '4d'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(4, 4)
    fixedLength = 4

class CcbptPolicySourceType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("ciscoCbQos", 1), ("ciscoCbpBase", 2))

class CcbptPolicyIdentifier(TextualConvention, Unsigned32):
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 4294967295)

class CcbptPolicyIdentifierOrZero(TextualConvention, Unsigned32):
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 4294967295)

mibBuilder.exportSymbols("CISCO-CBP-TARGET-TC-MIB", CcbptPolicySourceType=CcbptPolicySourceType, CcbptTargetType=CcbptTargetType, CcbptPolicyIdentifierOrZero=CcbptPolicyIdentifierOrZero, CcbptPolicyIdentifier=CcbptPolicyIdentifier, CcbptTargetIdAtmPvc=CcbptTargetIdAtmPvc, CcbptTargetId=CcbptTargetId, CcbptTargetIdNameString=CcbptTargetIdNameString, CcbptTargetIdFrDlci=CcbptTargetIdFrDlci, PYSNMP_MODULE_ID=ciscoCbpTargetTCMIB, CcbptTargetIdEntity=CcbptTargetIdEntity, ciscoCbpTargetTCMIB=ciscoCbpTargetTCMIB, CcbptTargetDirection=CcbptTargetDirection, CcbptTargetIdIf=CcbptTargetIdIf, CcbptTargetIdAaaSession=CcbptTargetIdAaaSession)
