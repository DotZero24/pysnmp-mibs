#
# PySNMP MIB module NETAPP-INVENTORY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/netapp/NETAPP-INVENTORY-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 09:57:34 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
fastPath, = mibBuilder.importSymbols("NETAPP-REF-MIB", "fastPath")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, Unsigned32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, NotificationType, iso, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "Unsigned32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "NotificationType", "iso", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention")
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
mibBuilder.exportSymbols("NETAPP-INVENTORY-MIB", AgentInventoryCardType=AgentInventoryCardType, agentInventoryComponentGroup=agentInventoryComponentGroup, agentInventoryComponentEntry=agentInventoryComponentEntry, agentInventoryComponentIndex=agentInventoryComponentIndex, fastPathInventory=fastPathInventory, agentInventoryCardGroup=agentInventoryCardGroup, agentInventoryComponentMnemonic=agentInventoryComponentMnemonic, agentInventoryStackGroup=agentInventoryStackGroup, agentInventoryCardTypeEntry=agentInventoryCardTypeEntry, agentInventoryCardTypeTable=agentInventoryCardTypeTable, agentInventoryStackDeleteSTK=agentInventoryStackDeleteSTK, agentInventoryComponentName=agentInventoryComponentName, agentInventoryCardModelIdentifier=agentInventoryCardModelIdentifier, AgentInventoryUnitType=AgentInventoryUnitType, PYSNMP_MODULE_ID=fastPathInventory, agentInventoryStackSTKname=agentInventoryStackSTKname, agentInventoryStackActivateSTK=agentInventoryStackActivateSTK, agentInventoryComponentTable=agentInventoryComponentTable, agentInventoryCardIndex=agentInventoryCardIndex, AgentInventoryUnitPreference=AgentInventoryUnitPreference, agentInventoryCardType=agentInventoryCardType, agentInventoryCardDescription=agentInventoryCardDescription)
