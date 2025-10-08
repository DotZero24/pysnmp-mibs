#
# PySNMP MIB module LANCOM-BONJOUR-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/lancom/LANCOM-BONJOUR-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:43:33 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
fastPath, = mibBuilder.importSymbols("LANCOM-REF-MIB", "fastPath")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
fastPathBonjour = ModuleIdentity((1, 3, 6, 1, 4, 1, 2356, 16, 1, 71))
fastPathBonjour.setRevisions(('2017-06-06 00:00',))
if mibBuilder.loadTexts: fastPathBonjour.setLastUpdated('201706060000Z')
if mibBuilder.loadTexts: fastPathBonjour.setOrganization('Broadcom ')
agentBonjourObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2356, 16, 1, 71, 1))
agentBonjourGlobal = MibIdentifier((1, 3, 6, 1, 4, 1, 2356, 16, 1, 71, 1, 1))
agentBonjourAdminMode = MibScalar((1, 3, 6, 1, 4, 1, 2356, 16, 1, 71, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enable", 1))).clone('enable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentBonjourAdminMode.setStatus('current')
mibBuilder.exportSymbols("LANCOM-BONJOUR-MIB", agentBonjourAdminMode=agentBonjourAdminMode, fastPathBonjour=fastPathBonjour, agentBonjourGlobal=agentBonjourGlobal, PYSNMP_MODULE_ID=fastPathBonjour, agentBonjourObjects=agentBonjourObjects)
