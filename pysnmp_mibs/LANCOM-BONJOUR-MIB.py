#
# PySNMP MIB module LANCOM-BONJOUR-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/lancom/LANCOM-BONJOUR-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 11:11:21 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
fastPath, = mibBuilder.importSymbols("LANCOM-REF-MIB", "fastPath")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
fastPathBonjour = ModuleIdentity((1, 3, 6, 1, 4, 1, 2356, 16, 1, 71))
fastPathBonjour.setRevisions(('2017-06-06 00:00',))
if mibBuilder.loadTexts: fastPathBonjour.setLastUpdated('201706060000Z')
if mibBuilder.loadTexts: fastPathBonjour.setOrganization('Broadcom ')
agentBonjourObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2356, 16, 1, 71, 1))
agentBonjourGlobal = MibIdentifier((1, 3, 6, 1, 4, 1, 2356, 16, 1, 71, 1, 1))
agentBonjourAdminMode = MibScalar((1, 3, 6, 1, 4, 1, 2356, 16, 1, 71, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enable", 1))).clone('enable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentBonjourAdminMode.setStatus('current')
mibBuilder.exportSymbols("LANCOM-BONJOUR-MIB", agentBonjourGlobal=agentBonjourGlobal, PYSNMP_MODULE_ID=fastPathBonjour, agentBonjourObjects=agentBonjourObjects, agentBonjourAdminMode=agentBonjourAdminMode, fastPathBonjour=fastPathBonjour)
