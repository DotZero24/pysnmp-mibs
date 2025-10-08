#
# PySNMP MIB module CISCO-NAC-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/cisco/CISCO-NAC-TC-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:29:42 2025
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

mibBuilder.exportSymbols("CISCO-NAC-TC-MIB", CnnEouPostureToken=CnnEouPostureToken, CnnEouAuthType=CnnEouAuthType, PYSNMP_MODULE_ID=ciscoNacTcMIB, ciscoNacTcMIB=ciscoNacTcMIB, CnnEouState=CnnEouState, CnnEouDeviceType=CnnEouDeviceType, CnnEouPostureTokenString=CnnEouPostureTokenString)
