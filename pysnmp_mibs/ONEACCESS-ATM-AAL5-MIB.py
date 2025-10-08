#
# PySNMP MIB module ONEACCESS-ATM-AAL5-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/oneaccess/ONEACCESS-ATM-AAL5-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:36:01 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
atmVclVpi, atmVclVci = mibBuilder.importSymbols("ATM-MIB", "atmVclVpi", "atmVclVci")
ifIndex, InterfaceIndex = mibBuilder.importSymbols("IF-MIB", "ifIndex", "InterfaceIndex")
oacRequirements, oacMIBModules, oacExpIMAtmAal5 = mibBuilder.importSymbols("ONEACCESS-GLOBAL-REG", "oacRequirements", "oacMIBModules", "oacExpIMAtmAal5")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
oacAtmAal5MIBModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 13191, 1, 100, 800))
oacAtmAal5MIBModule.setRevisions(('2011-10-27 00:00', '2010-07-08 10:00',))
if mibBuilder.loadTexts: oacAtmAal5MIBModule.setLastUpdated('201110270000Z')
if mibBuilder.loadTexts: oacAtmAal5MIBModule.setOrganization(' OneAccess ')
oacExpIMAtmAal5Objects = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 10, 3, 2, 3, 1))
oacExpIMAtmAal5Notifications = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 10, 3, 2, 3, 2))
oacExpIMAtmAal5VclLogicalIndexTable = MibTable((1, 3, 6, 1, 4, 1, 13191, 10, 3, 2, 3, 1, 1), )
if mibBuilder.loadTexts: oacExpIMAtmAal5VclLogicalIndexTable.setStatus('current')
oacExpIMAtmAal5VclLogicalIndexEntry = MibTableRow((1, 3, 6, 1, 4, 1, 13191, 10, 3, 2, 3, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "ATM-MIB", "atmVclVpi"), (0, "ATM-MIB", "atmVclVci"))
if mibBuilder.loadTexts: oacExpIMAtmAal5VclLogicalIndexEntry.setStatus('current')
oacExpIMAtmAal5VclLogicalIndexIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 2, 3, 1, 1, 1, 1), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacExpIMAtmAal5VclLogicalIndexIfIndex.setStatus('current')
oacExpIMAtmAal5Conformance = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 5, 800))
oacExpIMAtmAal5Groups = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 5, 800, 1))
oacExpIMAtmAal5Compliances = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 5, 800, 2))
oacExpIMAtmAal5Compliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 13191, 5, 800, 2, 1)).setObjects(("ONEACCESS-ATM-AAL5-MIB", "oacExpIMAtmAal5GeneralGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    oacExpIMAtmAal5Compliance = oacExpIMAtmAal5Compliance.setStatus('current')
oacExpIMAtmAal5GeneralGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 13191, 5, 800, 1, 1)).setObjects(("ONEACCESS-ATM-AAL5-MIB", "oacExpIMAtmAal5VclLogicalIndexIfIndex"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    oacExpIMAtmAal5GeneralGroup = oacExpIMAtmAal5GeneralGroup.setStatus('current')
mibBuilder.exportSymbols("ONEACCESS-ATM-AAL5-MIB", oacExpIMAtmAal5Compliance=oacExpIMAtmAal5Compliance, PYSNMP_MODULE_ID=oacAtmAal5MIBModule, oacExpIMAtmAal5GeneralGroup=oacExpIMAtmAal5GeneralGroup, oacExpIMAtmAal5Objects=oacExpIMAtmAal5Objects, oacExpIMAtmAal5VclLogicalIndexEntry=oacExpIMAtmAal5VclLogicalIndexEntry, oacAtmAal5MIBModule=oacAtmAal5MIBModule, oacExpIMAtmAal5Compliances=oacExpIMAtmAal5Compliances, oacExpIMAtmAal5VclLogicalIndexIfIndex=oacExpIMAtmAal5VclLogicalIndexIfIndex, oacExpIMAtmAal5VclLogicalIndexTable=oacExpIMAtmAal5VclLogicalIndexTable, oacExpIMAtmAal5Conformance=oacExpIMAtmAal5Conformance, oacExpIMAtmAal5Groups=oacExpIMAtmAal5Groups, oacExpIMAtmAal5Notifications=oacExpIMAtmAal5Notifications)
