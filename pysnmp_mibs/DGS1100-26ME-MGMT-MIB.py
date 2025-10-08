#
# PySNMP MIB module DGS1100-26ME-MGMT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/d-link/DGS1100-26ME-MGMT-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:59:03 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
dgs1100_26ME, = mibBuilder.importSymbols("DGS1100PRIMGMT-MIB", "dgs1100-26ME")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
MacAddress, RowStatus, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "MacAddress", "RowStatus", "TextualConvention", "DisplayString")
swL2MgmtMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 171, 10, 134, 12, 12))
if mibBuilder.loadTexts: swL2MgmtMIB.setLastUpdated('201404260000Z')
if mibBuilder.loadTexts: swL2MgmtMIB.setOrganization('D-Link Corp.')
class PortList(OctetString):
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 127)

class VlanIndex(Unsigned32):
    pass

class VlanId(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 4094)

mibBuilder.exportSymbols("DGS1100-26ME-MGMT-MIB", swL2MgmtMIB=swL2MgmtMIB, PYSNMP_MODULE_ID=swL2MgmtMIB, VlanIndex=VlanIndex, PortList=PortList, VlanId=VlanId)
