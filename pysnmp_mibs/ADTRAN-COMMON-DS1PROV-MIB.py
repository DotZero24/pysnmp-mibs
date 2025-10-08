#
# PySNMP MIB module ADTRAN-COMMON-DS1PROV-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/adtran/ADTRAN-COMMON-DS1PROV-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:29:48 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
adGenTa5kCommonDs1ProvID, adGenTa5kCommonDs1Prov = mibBuilder.importSymbols("ADTRAN-GENTA5K-MIB", "adGenTa5kCommonDs1ProvID", "adGenTa5kCommonDs1Prov")
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
adGenCommonDs1ProvMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 664, 6, 10000, 67, 1, 6, 1))
if mibBuilder.loadTexts: adGenCommonDs1ProvMIB.setLastUpdated('200711062117Z')
if mibBuilder.loadTexts: adGenCommonDs1ProvMIB.setOrganization('ADTRAN, Inc.')
adDs1vgDs1Mgmt = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 6, 1))
adDs1vgT1InterfaceProvisioningTable = MibTable((1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 6, 1, 1), )
if mibBuilder.loadTexts: adDs1vgT1InterfaceProvisioningTable.setStatus('current')
adDs1vgT1InterfaceProvisioningTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 6, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: adDs1vgT1InterfaceProvisioningTableEntry.setStatus('current')
adDs1vgT1InterfaceProvTableLineBuildout = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 6, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("lineLength0ft", 1), ("lineLength0133ft", 2), ("lineLength133266ft", 3), ("lineLength266399ft", 4), ("lineLength399533ft", 5), ("lineLength533655ft", 6)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: adDs1vgT1InterfaceProvTableLineBuildout.setStatus('current')
adDs1vgT1InterfaceProvTableLineMode = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 6, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("gr303cesop", 1), ("satop", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: adDs1vgT1InterfaceProvTableLineMode.setStatus('current')
adDs1vgT1InterfaceClearPMCounters = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 6, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: adDs1vgT1InterfaceClearPMCounters.setStatus('current')
mibBuilder.exportSymbols("ADTRAN-COMMON-DS1PROV-MIB", PYSNMP_MODULE_ID=adGenCommonDs1ProvMIB, adDs1vgT1InterfaceClearPMCounters=adDs1vgT1InterfaceClearPMCounters, adDs1vgT1InterfaceProvTableLineMode=adDs1vgT1InterfaceProvTableLineMode, adDs1vgT1InterfaceProvisioningTableEntry=adDs1vgT1InterfaceProvisioningTableEntry, adDs1vgT1InterfaceProvTableLineBuildout=adDs1vgT1InterfaceProvTableLineBuildout, adDs1vgDs1Mgmt=adDs1vgDs1Mgmt, adDs1vgT1InterfaceProvisioningTable=adDs1vgT1InterfaceProvisioningTable, adGenCommonDs1ProvMIB=adGenCommonDs1ProvMIB)
