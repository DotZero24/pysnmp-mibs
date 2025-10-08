#
# PySNMP MIB module CISCO-CBP-TARGET-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/cisco/CISCO-CBP-TARGET-TC-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:15:36 2025
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

mibBuilder.exportSymbols("CISCO-CBP-TARGET-TC-MIB", CcbptPolicySourceType=CcbptPolicySourceType, CcbptTargetIdAaaSession=CcbptTargetIdAaaSession, CcbptPolicyIdentifierOrZero=CcbptPolicyIdentifierOrZero, CcbptTargetIdFrDlci=CcbptTargetIdFrDlci, CcbptPolicyIdentifier=CcbptPolicyIdentifier, CcbptTargetIdAtmPvc=CcbptTargetIdAtmPvc, ciscoCbpTargetTCMIB=ciscoCbpTargetTCMIB, CcbptTargetId=CcbptTargetId, CcbptTargetIdEntity=CcbptTargetIdEntity, CcbptTargetType=CcbptTargetType, PYSNMP_MODULE_ID=ciscoCbpTargetTCMIB, CcbptTargetIdNameString=CcbptTargetIdNameString, CcbptTargetIdIf=CcbptTargetIdIf, CcbptTargetDirection=CcbptTargetDirection)
