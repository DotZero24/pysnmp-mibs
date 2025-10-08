#
# PySNMP MIB module AFFIRMED-SNMP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/microsoft/AFFIRMED-SNMP-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:07:49 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, enterprises, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "enterprises", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
affirmedSnmp = ModuleIdentity((1, 3, 6, 1, 4, 1, 37963))
affirmedSnmp.setRevisions(('2011-05-16 00:00',))
if mibBuilder.loadTexts: affirmedSnmp.setLastUpdated('201105160000Z')
if mibBuilder.loadTexts: affirmedSnmp.setOrganization('www.affirmednetworks.com')
affirmedSnmpObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 37963, 1))
affirmedSnmpEnumerations = MibIdentifier((1, 3, 6, 1, 4, 1, 37963, 3))
affirmedSnmpModuleIDs = MibIdentifier((1, 3, 6, 1, 4, 1, 37963, 3, 1))
affirmedSnmpAgentOIDs = MibIdentifier((1, 3, 6, 1, 4, 1, 37963, 3, 2))
affirmedSnmpDomains = MibIdentifier((1, 3, 6, 1, 4, 1, 37963, 3, 3))
affirmedSnmpGeneral = MibIdentifier((1, 3, 6, 1, 4, 1, 37963, 10))
affirmedSnmpExperimental = MibIdentifier((1, 3, 6, 1, 4, 1, 37963, 9999))
affirmedSnmpPlaypen = MibIdentifier((1, 3, 6, 1, 4, 1, 37963, 9999, 9999))
affirmedSnmpNotificationPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 37963, 4))
affirmedSnmpNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 37963, 4, 0))
affirmedSnmpNotificationObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 37963, 4, 1))
affirmedSnmpConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 37963, 5))
affirmedSnmpCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 37963, 5, 1))
affirmedSnmpGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 37963, 5, 2))
mibBuilder.exportSymbols("AFFIRMED-SNMP-MIB", affirmedSnmpGeneral=affirmedSnmpGeneral, affirmedSnmpModuleIDs=affirmedSnmpModuleIDs, affirmedSnmpAgentOIDs=affirmedSnmpAgentOIDs, affirmedSnmpEnumerations=affirmedSnmpEnumerations, affirmedSnmpExperimental=affirmedSnmpExperimental, affirmedSnmpNotificationObjects=affirmedSnmpNotificationObjects, affirmedSnmpPlaypen=affirmedSnmpPlaypen, affirmedSnmpCompliances=affirmedSnmpCompliances, affirmedSnmpGroups=affirmedSnmpGroups, affirmedSnmpObjects=affirmedSnmpObjects, affirmedSnmpNotificationPrefix=affirmedSnmpNotificationPrefix, PYSNMP_MODULE_ID=affirmedSnmp, affirmedSnmpNotifications=affirmedSnmpNotifications, affirmedSnmpConformance=affirmedSnmpConformance, affirmedSnmpDomains=affirmedSnmpDomains, affirmedSnmp=affirmedSnmp)
