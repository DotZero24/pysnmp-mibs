#
# PySNMP MIB module NETAPP-INVENTORY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/netapp/NETAPP-INVENTORY-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 09:59:14 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
fastPath, = mibBuilder.importSymbols("NETAPP-REF-MIB", "fastPath")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Integer32, Bits, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Integer32", "Bits", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
RowStatus, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "DisplayString", "TextualConvention")
fastPathInventory = ModuleIdentity((1, 3, 6, 1, 4, 1, 789, 4413, 1, 1, 13))
fastPathInventory.setRevisions(('2013-10-15 00:00', '2011-01-26 00:00', '2007-05-23 00:00', '2004-10-28 20:37', '2003-05-26 19:30',))
if mibBuilder.loadTexts: fastPathInventory.setLastUpdated('201310150000Z')
if mibBuilder.loadTexts: fastPathInventory.setOrganization('Broadcom Corporation')
class AgentInventoryUnitPreference(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("disabled", 0), ("unsassigned", 1), ("assigned", 2))

class AgentInventoryUnitType(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'x'

class AgentInventoryCardType(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'x'

agentInventoryStackGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 789, 4413, 1, 1, 13, 1))
agentInventoryStackSTKname = MibScalar((1, 3, 6, 1, 4, 1, 789, 4413, 1, 1, 13, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("unconfigured", 1), ("image1", 2), ("image2", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentInventoryStackSTKname.setStatus('current')
agentInventoryStackActivateSTK = MibScalar((1, 3, 6, 1, 4, 1, 789, 4413, 1, 1, 13, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentInventoryStackActivateSTK.setStatus('current')
agentInventoryStackDeleteSTK = MibScalar((1, 3, 6, 1, 4, 1, 789, 4413, 1, 1, 13, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentInventoryStackDeleteSTK.setStatus('current')
agentInventoryCardGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 789, 4413, 1, 1, 13, 4))
agentInventoryCardTypeTable = MibTable((1, 3, 6, 1, 4, 1, 789, 4413, 1, 1, 13, 4, 1), )
if mibBuilder.loadTexts: agentInventoryCardTypeTable.setStatus('current')
agentInventoryCardTypeEntry = MibTableRow((1, 3, 6, 1, 4, 1, 789, 4413, 1, 1, 13, 4, 1, 1), ).setIndexNames((0, "NETAPP-INVENTORY-MIB", "agentInventoryCardIndex"))
if mibBuilder.loadTexts: agentInventoryCardTypeEntry.setStatus('current')
agentInventoryCardIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 789, 4413, 1, 1, 13, 4, 1, 1, 1), Unsigned32())
if mibBuilder.loadTexts: agentInventoryCardIndex.setStatus('current')
agentInventoryCardType = MibTableColumn((1, 3, 6, 1, 4, 1, 789, 4413, 1, 1, 13, 4, 1, 1, 2), AgentInventoryCardType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentInventoryCardType.setStatus('current')
agentInventoryCardModelIdentifier = MibTableColumn((1, 3, 6, 1, 4, 1, 789, 4413, 1, 1, 13, 4, 1, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentInventoryCardModelIdentifier.setStatus('current')
agentInventoryCardDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 789, 4413, 1, 1, 13, 4, 1, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentInventoryCardDescription.setStatus('current')
agentInventoryComponentGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 789, 4413, 1, 1, 13, 5))
agentInventoryComponentTable = MibTable((1, 3, 6, 1, 4, 1, 789, 4413, 1, 1, 13, 5, 1), )
if mibBuilder.loadTexts: agentInventoryComponentTable.setStatus('current')
agentInventoryComponentEntry = MibTableRow((1, 3, 6, 1, 4, 1, 789, 4413, 1, 1, 13, 5, 1, 1), ).setIndexNames((0, "NETAPP-INVENTORY-MIB", "agentInventoryComponentIndex"))
if mibBuilder.loadTexts: agentInventoryComponentEntry.setStatus('current')
agentInventoryComponentIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 789, 4413, 1, 1, 13, 5, 1, 1, 1), Unsigned32())
if mibBuilder.loadTexts: agentInventoryComponentIndex.setStatus('current')
agentInventoryComponentMnemonic = MibTableColumn((1, 3, 6, 1, 4, 1, 789, 4413, 1, 1, 13, 5, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentInventoryComponentMnemonic.setStatus('current')
agentInventoryComponentName = MibTableColumn((1, 3, 6, 1, 4, 1, 789, 4413, 1, 1, 13, 5, 1, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentInventoryComponentName.setStatus('current')
mibBuilder.exportSymbols("NETAPP-INVENTORY-MIB", agentInventoryCardTypeEntry=agentInventoryCardTypeEntry, agentInventoryStackActivateSTK=agentInventoryStackActivateSTK, agentInventoryCardDescription=agentInventoryCardDescription, agentInventoryCardType=agentInventoryCardType, agentInventoryComponentIndex=agentInventoryComponentIndex, agentInventoryComponentName=agentInventoryComponentName, AgentInventoryUnitPreference=AgentInventoryUnitPreference, agentInventoryComponentEntry=agentInventoryComponentEntry, AgentInventoryCardType=AgentInventoryCardType, agentInventoryComponentMnemonic=agentInventoryComponentMnemonic, agentInventoryCardModelIdentifier=agentInventoryCardModelIdentifier, PYSNMP_MODULE_ID=fastPathInventory, agentInventoryComponentTable=agentInventoryComponentTable, agentInventoryCardTypeTable=agentInventoryCardTypeTable, AgentInventoryUnitType=AgentInventoryUnitType, agentInventoryComponentGroup=agentInventoryComponentGroup, agentInventoryStackDeleteSTK=agentInventoryStackDeleteSTK, agentInventoryCardGroup=agentInventoryCardGroup, agentInventoryStackSTKname=agentInventoryStackSTKname, agentInventoryCardIndex=agentInventoryCardIndex, agentInventoryStackGroup=agentInventoryStackGroup, fastPathInventory=fastPathInventory)
