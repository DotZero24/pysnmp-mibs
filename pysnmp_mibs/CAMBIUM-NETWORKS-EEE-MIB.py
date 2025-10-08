#
# PySNMP MIB module CAMBIUM-NETWORKS-EEE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/cambium/CAMBIUM-NETWORKS-EEE-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:39:47 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, enterprises, Unsigned32, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Counter32, iso, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "enterprises", "Unsigned32", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Counter32", "iso", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TruthValue, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "RowStatus", "TextualConvention")
cnEeeMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 17713, 24, 8))
cnEeeMib.setRevisions(('2021-04-19 00:00',))
if mibBuilder.loadTexts: cnEeeMib.setLastUpdated('202104190000Z')
if mibBuilder.loadTexts: cnEeeMib.setOrganization('Cambium Networks, Inc.')
cnEeeObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 17713, 24, 8, 0))
cnEeePortTable = MibTable((1, 3, 6, 1, 4, 1, 17713, 24, 8, 0, 1), )
if mibBuilder.loadTexts: cnEeePortTable.setStatus('current')
cnEeePortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 17713, 24, 8, 0, 1, 1), ).setIndexNames((0, "CAMBIUM-NETWORKS-EEE-MIB", "cnEeePortIndex"))
if mibBuilder.loadTexts: cnEeePortEntry.setStatus('current')
cnEeePortIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 17713, 24, 8, 0, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: cnEeePortIndex.setStatus('current')
cnEeeEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 17713, 24, 8, 0, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cnEeeEnabled.setStatus('current')
cnEeeCapabilities = MibTableColumn((1, 3, 6, 1, 4, 1, 17713, 24, 8, 0, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cnEeeCapabilities.setStatus('current')
cnEeeLpAbilities = MibTableColumn((1, 3, 6, 1, 4, 1, 17713, 24, 8, 0, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cnEeeLpAbilities.setStatus('current')
mibBuilder.exportSymbols("CAMBIUM-NETWORKS-EEE-MIB", PYSNMP_MODULE_ID=cnEeeMib, cnEeeMib=cnEeeMib, cnEeeEnabled=cnEeeEnabled, cnEeePortEntry=cnEeePortEntry, cnEeePortIndex=cnEeePortIndex, cnEeePortTable=cnEeePortTable, cnEeeCapabilities=cnEeeCapabilities, cnEeeLpAbilities=cnEeeLpAbilities, cnEeeObjects=cnEeeObjects)
