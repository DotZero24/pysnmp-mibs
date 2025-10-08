#
# PySNMP MIB module CISCO-NAC-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/cisco/CISCO-NAC-TC-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:14:59 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoNacTcMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 530))
ciscoNacTcMIB.setRevisions(('2006-05-31 00:00',))
if mibBuilder.loadTexts: ciscoNacTcMIB.setLastUpdated('200605310000Z')
if mibBuilder.loadTexts: ciscoNacTcMIB.setOrganization('Cisco Systems, Inc.')
class CnnEouState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12))
    namedValues = NamedValues(("initialize", 1), ("hello", 2), ("clientless", 3), ("eapRequest", 4), ("response", 5), ("authenticated", 6), ("fail", 7), ("abort", 8), ("aaaFail", 9), ("hold", 10), ("client", 11), ("server", 12))

class CnnEouAuthType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("clientless", 1), ("eap", 2), ("static", 3), ("unknown", 4))

class CnnEouDeviceType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1))
    namedValues = NamedValues(("ciscoIpPhone", 1))

class CnnEouPostureToken(TextualConvention, Integer32):
    status = 'deprecated'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("unknown", 1), ("healthy", 2), ("checkup", 3), ("quarantine", 4), ("infected", 5))

class CnnEouPostureTokenString(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

mibBuilder.exportSymbols("CISCO-NAC-TC-MIB", CnnEouAuthType=CnnEouAuthType, ciscoNacTcMIB=ciscoNacTcMIB, CnnEouDeviceType=CnnEouDeviceType, CnnEouPostureTokenString=CnnEouPostureTokenString, CnnEouPostureToken=CnnEouPostureToken, PYSNMP_MODULE_ID=ciscoNacTcMIB, CnnEouState=CnnEouState)
