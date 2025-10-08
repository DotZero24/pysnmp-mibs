#
# PySNMP MIB module DMOS-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/datacom/DMOS-TC-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:41:58 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
datacomDevicesMIBs, = mibBuilder.importSymbols("DATACOM-SMI", "datacomDevicesMIBs")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
dmosTcMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 3709, 3, 6, 5))
dmosTcMIB.setRevisions(('2016-12-12 00:00',))
if mibBuilder.loadTexts: dmosTcMIB.setLastUpdated('201612120000Z')
if mibBuilder.loadTexts: dmosTcMIB.setOrganization('DATACOM')
class Unsigned8(TextualConvention, Gauge32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Gauge32.subtypeSpec + ValueRangeConstraint(0, 255)

class UnsignedPercent(TextualConvention, Gauge32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Gauge32.subtypeSpec + ValueRangeConstraint(0, 100)

class FixedPoint2Dec(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd-2'

mibBuilder.exportSymbols("DMOS-TC-MIB", PYSNMP_MODULE_ID=dmosTcMIB, dmosTcMIB=dmosTcMIB, FixedPoint2Dec=FixedPoint2Dec, UnsignedPercent=UnsignedPercent, Unsigned8=Unsigned8)
