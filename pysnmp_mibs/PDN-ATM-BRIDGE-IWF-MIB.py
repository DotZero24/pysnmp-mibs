#
# PySNMP MIB module PDN-ATM-BRIDGE-IWF-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/paradyne/PDN-ATM-BRIDGE-IWF-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 09:57:09 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
pdn_common, = mibBuilder.importSymbols("PDN-HEADER-MIB", "pdn-common")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
RowStatus, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("PDN-ATM-BRIDGE-IWF-MIB", pdnAtmBridgeIwfCompliances=pdnAtmBridgeIwfCompliances, pdnAtmBridgeIwfRowStatus=pdnAtmBridgeIwfRowStatus, pdnAtmBridgeIwfGroups=pdnAtmBridgeIwfGroups, pdnAtmBridgeIwfVclVci=pdnAtmBridgeIwfVclVci, pdnAtmBridgeIwfDot1dBasePort=pdnAtmBridgeIwfDot1dBasePort, pdnAtmBridgeIwfObjects=pdnAtmBridgeIwfObjects, pdnAtmBridgeIwfConformance=pdnAtmBridgeIwfConformance, pdnAtmBridgeIwfGroup=pdnAtmBridgeIwfGroup, PYSNMP_MODULE_ID=pdnAtmBridgeIwfMIB, pdnAtmBridgeIwfTable=pdnAtmBridgeIwfTable, pdnAtmBridgeIwfMIBCompliance=pdnAtmBridgeIwfMIBCompliance, pdnAtmBridgeIwfEntry=pdnAtmBridgeIwfEntry, pdnAtmBridgeIwfVclVpi=pdnAtmBridgeIwfVclVpi, pdnAtmBridgeIwfNotifications=pdnAtmBridgeIwfNotifications, pdnAtmBridgeIwfMIB=pdnAtmBridgeIwfMIB)
