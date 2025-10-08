#
# PySNMP MIB module PDN-ATM-BRIDGE-IWF-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/paradyne/PDN-ATM-BRIDGE-IWF-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 09:56:35 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
pdn_common, = mibBuilder.importSymbols("PDN-HEADER-MIB", "pdn-common")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Unsigned32, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Unsigned32", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention")
pdnAtmBridgeIwfMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 43))
pdnAtmBridgeIwfMIB.setRevisions(('2003-04-24 00:00', '2003-03-24 00:00', '2003-03-17 00:00',))
if mibBuilder.loadTexts: pdnAtmBridgeIwfMIB.setLastUpdated('200303240000Z')
if mibBuilder.loadTexts: pdnAtmBridgeIwfMIB.setOrganization('Paradyne Networks MIB Working Group Other information about group editing the MIB')
pdnAtmBridgeIwfNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 43, 0))
pdnAtmBridgeIwfObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 43, 1))
pdnAtmBridgeIwfConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 43, 2))
pdnAtmBridgeIwfTable = MibTable((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 43, 1, 1), )
if mibBuilder.loadTexts: pdnAtmBridgeIwfTable.setStatus('current')
pdnAtmBridgeIwfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 43, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "PDN-ATM-BRIDGE-IWF-MIB", "pdnAtmBridgeIwfVclVpi"), (0, "PDN-ATM-BRIDGE-IWF-MIB", "pdnAtmBridgeIwfVclVci"))
if mibBuilder.loadTexts: pdnAtmBridgeIwfEntry.setStatus('current')
pdnAtmBridgeIwfVclVpi = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 43, 1, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4095)))
if mibBuilder.loadTexts: pdnAtmBridgeIwfVclVpi.setStatus('current')
pdnAtmBridgeIwfVclVci = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 43, 1, 1, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)))
if mibBuilder.loadTexts: pdnAtmBridgeIwfVclVci.setStatus('current')
pdnAtmBridgeIwfRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 43, 1, 1, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pdnAtmBridgeIwfRowStatus.setStatus('current')
pdnAtmBridgeIwfDot1dBasePort = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 43, 1, 1, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pdnAtmBridgeIwfDot1dBasePort.setStatus('current')
pdnAtmBridgeIwfCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 43, 2, 1))
pdnAtmBridgeIwfGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 43, 2, 2))
pdnAtmBridgeIwfMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 43, 2, 1, 1)).setObjects(("PDN-ATM-BRIDGE-IWF-MIB", "pdnAtmBridgeIwfGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pdnAtmBridgeIwfMIBCompliance = pdnAtmBridgeIwfMIBCompliance.setStatus('current')
pdnAtmBridgeIwfGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 43, 2, 2, 1)).setObjects(("PDN-ATM-BRIDGE-IWF-MIB", "pdnAtmBridgeIwfRowStatus"), ("PDN-ATM-BRIDGE-IWF-MIB", "pdnAtmBridgeIwfDot1dBasePort"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pdnAtmBridgeIwfGroup = pdnAtmBridgeIwfGroup.setStatus('current')
mibBuilder.exportSymbols("PDN-ATM-BRIDGE-IWF-MIB", pdnAtmBridgeIwfVclVpi=pdnAtmBridgeIwfVclVpi, pdnAtmBridgeIwfCompliances=pdnAtmBridgeIwfCompliances, pdnAtmBridgeIwfGroups=pdnAtmBridgeIwfGroups, pdnAtmBridgeIwfTable=pdnAtmBridgeIwfTable, pdnAtmBridgeIwfNotifications=pdnAtmBridgeIwfNotifications, PYSNMP_MODULE_ID=pdnAtmBridgeIwfMIB, pdnAtmBridgeIwfVclVci=pdnAtmBridgeIwfVclVci, pdnAtmBridgeIwfObjects=pdnAtmBridgeIwfObjects, pdnAtmBridgeIwfGroup=pdnAtmBridgeIwfGroup, pdnAtmBridgeIwfRowStatus=pdnAtmBridgeIwfRowStatus, pdnAtmBridgeIwfDot1dBasePort=pdnAtmBridgeIwfDot1dBasePort, pdnAtmBridgeIwfConformance=pdnAtmBridgeIwfConformance, pdnAtmBridgeIwfEntry=pdnAtmBridgeIwfEntry, pdnAtmBridgeIwfMIBCompliance=pdnAtmBridgeIwfMIBCompliance, pdnAtmBridgeIwfMIB=pdnAtmBridgeIwfMIB)
