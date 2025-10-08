#
# PySNMP MIB module SO-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/smartoptics/SO-TC-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:07:36 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
smartoptics, = mibBuilder.importSymbols("SO-MIB", "smartoptics")
soTcMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 30826, 3))
soTcMIB.setRevisions(('2022-09-05 14:10', '2022-03-18 13:49', '2021-04-12 10:49', '2018-10-08 14:44',))
if mibBuilder.loadTexts: soTcMIB.setLastUpdated('202209051410Z')
if mibBuilder.loadTexts: soTcMIB.setOrganization('Smartoptics')
class OpticalPower1Decimal(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd-1'

class DcpTenths(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd-1'

class DcpHundreds(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd-2'

class InterfaceStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("idle", 1), ("down", 2), ("up", 3))

class ItuPerceivedSeverity(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("cleared", 1), ("indeterminate", 2), ("critical", 3), ("major", 4), ("minor", 5), ("warning", 6))

class OchPortMode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("on", 1), ("off", 2), ("edfa", 3), ("express", 4))

class InterfacePortMode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
    namedValues = NamedValues(("na", 1), ("localAD", 2), ("xc1", 3), ("xc2", 4), ("xc3", 5), ("xc4Wss1", 6), ("xc4Wss2", 7), ("xc4Wss3", 8), ("xc4Wss4", 9), ("xc4Wss5", 10))

class FanStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("notPresent", 1), ("ok", 2), ("alarm", 3))

class FanMode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("na", 1), ("high", 2), ("medium", 3), ("low", 4))

mibBuilder.exportSymbols("SO-TC-MIB", DcpTenths=DcpTenths, FanMode=FanMode, OpticalPower1Decimal=OpticalPower1Decimal, InterfaceStatus=InterfaceStatus, ItuPerceivedSeverity=ItuPerceivedSeverity, soTcMIB=soTcMIB, OchPortMode=OchPortMode, InterfacePortMode=InterfacePortMode, DcpHundreds=DcpHundreds, PYSNMP_MODULE_ID=soTcMIB, FanStatus=FanStatus)
