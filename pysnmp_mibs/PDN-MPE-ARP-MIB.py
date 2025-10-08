#
# PySNMP MIB module PDN-MPE-ARP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/paradyne/PDN-MPE-ARP-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 09:57:27 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
entPhysicalIndex, = mibBuilder.importSymbols("ENTITY-MIB", "entPhysicalIndex")
mpe_arp, = mibBuilder.importSymbols("PDN-HEADER-MIB", "mpe-arp")
VnidRange, SwitchState = mibBuilder.importSymbols("PDN-TC", "VnidRange", "SwitchState")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Counter32, Counter64, TimeTicks, ModuleIdentity, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Counter32", "Counter64", "TimeTicks", "ModuleIdentity", "Gauge32")
RowStatus, TextualConvention, MacAddress, TruthValue, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "MacAddress", "TruthValue", "DisplayString")
class Bit32(Integer32):
    pass

mpePdnNetToMediaGenericMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 27, 1))
mpePdnNetToMediaMIBTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 27, 2))
mpePdnNetTo8023MediaParams = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 27, 1, 1))
mpePdnNetTo8023MediaConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 27, 1, 2))
mpePdnNetTo8023MediaParamsTable = MibTable((1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 27, 1, 1, 1), )
if mibBuilder.loadTexts: mpePdnNetTo8023MediaParamsTable.setStatus('mandatory')
mpePdnNetTo8023MediaParamsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 27, 1, 1, 1, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"))
if mibBuilder.loadTexts: mpePdnNetTo8023MediaParamsEntry.setStatus('mandatory')
mpePdnNetTo8023MediaParamsCompEntryTimeout = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 27, 1, 1, 1, 1, 1), Integer32().clone(20)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mpePdnNetTo8023MediaParamsCompEntryTimeout.setStatus('mandatory')
mpePdnNetTo8023MediaParamsIncompEntryTimeout = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 27, 1, 1, 1, 1, 2), Integer32().clone(3)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mpePdnNetTo8023MediaParamsIncompEntryTimeout.setStatus('mandatory')
mpePdnNetTo8023MediaParamsDefRouteEntryTimeout = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 27, 1, 1, 1, 1, 3), Integer32().clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mpePdnNetTo8023MediaParamsDefRouteEntryTimeout.setStatus('mandatory')
mibBuilder.exportSymbols("PDN-MPE-ARP-MIB", mpePdnNetTo8023MediaConfig=mpePdnNetTo8023MediaConfig, mpePdnNetTo8023MediaParamsTable=mpePdnNetTo8023MediaParamsTable, mpePdnNetTo8023MediaParamsIncompEntryTimeout=mpePdnNetTo8023MediaParamsIncompEntryTimeout, mpePdnNetTo8023MediaParamsDefRouteEntryTimeout=mpePdnNetTo8023MediaParamsDefRouteEntryTimeout, mpePdnNetToMediaGenericMIBObjects=mpePdnNetToMediaGenericMIBObjects, mpePdnNetTo8023MediaParams=mpePdnNetTo8023MediaParams, mpePdnNetTo8023MediaParamsEntry=mpePdnNetTo8023MediaParamsEntry, Bit32=Bit32, mpePdnNetTo8023MediaParamsCompEntryTimeout=mpePdnNetTo8023MediaParamsCompEntryTimeout, mpePdnNetToMediaMIBTraps=mpePdnNetToMediaMIBTraps)
