#
# PySNMP MIB module PDN-MPE-ARP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/paradyne/PDN-MPE-ARP-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 09:56:44 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
entPhysicalIndex, = mibBuilder.importSymbols("ENTITY-MIB", "entPhysicalIndex")
mpe_arp, = mibBuilder.importSymbols("PDN-HEADER-MIB", "mpe-arp")
VnidRange, SwitchState = mibBuilder.importSymbols("PDN-TC", "VnidRange", "SwitchState")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, MacAddress, RowStatus, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "MacAddress", "RowStatus", "TruthValue", "TextualConvention")
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
mibBuilder.exportSymbols("PDN-MPE-ARP-MIB", mpePdnNetTo8023MediaParamsIncompEntryTimeout=mpePdnNetTo8023MediaParamsIncompEntryTimeout, Bit32=Bit32, mpePdnNetTo8023MediaParams=mpePdnNetTo8023MediaParams, mpePdnNetToMediaGenericMIBObjects=mpePdnNetToMediaGenericMIBObjects, mpePdnNetTo8023MediaConfig=mpePdnNetTo8023MediaConfig, mpePdnNetTo8023MediaParamsDefRouteEntryTimeout=mpePdnNetTo8023MediaParamsDefRouteEntryTimeout, mpePdnNetTo8023MediaParamsTable=mpePdnNetTo8023MediaParamsTable, mpePdnNetToMediaMIBTraps=mpePdnNetToMediaMIBTraps, mpePdnNetTo8023MediaParamsEntry=mpePdnNetTo8023MediaParamsEntry, mpePdnNetTo8023MediaParamsCompEntryTimeout=mpePdnNetTo8023MediaParamsCompEntryTimeout)
