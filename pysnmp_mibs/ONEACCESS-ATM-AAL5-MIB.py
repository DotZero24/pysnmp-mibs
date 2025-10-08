#
# PySNMP MIB module ONEACCESS-ATM-AAL5-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/oneaccess/ONEACCESS-ATM-AAL5-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 11:01:19 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
atmVclVci, atmVclVpi = mibBuilder.importSymbols("ATM-MIB", "atmVclVci", "atmVclVpi")
ifIndex, InterfaceIndex = mibBuilder.importSymbols("IF-MIB", "ifIndex", "InterfaceIndex")
oacRequirements, oacExpIMAtmAal5, oacMIBModules = mibBuilder.importSymbols("ONEACCESS-GLOBAL-REG", "oacRequirements", "oacExpIMAtmAal5", "oacMIBModules")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("ONEACCESS-ATM-AAL5-MIB", oacExpIMAtmAal5Objects=oacExpIMAtmAal5Objects, oacAtmAal5MIBModule=oacAtmAal5MIBModule, oacExpIMAtmAal5VclLogicalIndexTable=oacExpIMAtmAal5VclLogicalIndexTable, oacExpIMAtmAal5Compliance=oacExpIMAtmAal5Compliance, PYSNMP_MODULE_ID=oacAtmAal5MIBModule, oacExpIMAtmAal5VclLogicalIndexEntry=oacExpIMAtmAal5VclLogicalIndexEntry, oacExpIMAtmAal5Notifications=oacExpIMAtmAal5Notifications, oacExpIMAtmAal5VclLogicalIndexIfIndex=oacExpIMAtmAal5VclLogicalIndexIfIndex, oacExpIMAtmAal5Groups=oacExpIMAtmAal5Groups, oacExpIMAtmAal5Compliances=oacExpIMAtmAal5Compliances, oacExpIMAtmAal5GeneralGroup=oacExpIMAtmAal5GeneralGroup, oacExpIMAtmAal5Conformance=oacExpIMAtmAal5Conformance)
