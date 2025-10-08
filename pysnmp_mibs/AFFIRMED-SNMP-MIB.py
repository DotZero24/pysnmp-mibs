#
# PySNMP MIB module AFFIRMED-SNMP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/microsoft/AFFIRMED-SNMP-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:17:05 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, enterprises, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "enterprises", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("AFFIRMED-SNMP-MIB", affirmedSnmpDomains=affirmedSnmpDomains, affirmedSnmpObjects=affirmedSnmpObjects, affirmedSnmp=affirmedSnmp, affirmedSnmpGeneral=affirmedSnmpGeneral, affirmedSnmpModuleIDs=affirmedSnmpModuleIDs, affirmedSnmpExperimental=affirmedSnmpExperimental, affirmedSnmpCompliances=affirmedSnmpCompliances, PYSNMP_MODULE_ID=affirmedSnmp, affirmedSnmpPlaypen=affirmedSnmpPlaypen, affirmedSnmpNotificationObjects=affirmedSnmpNotificationObjects, affirmedSnmpConformance=affirmedSnmpConformance, affirmedSnmpGroups=affirmedSnmpGroups, affirmedSnmpAgentOIDs=affirmedSnmpAgentOIDs, affirmedSnmpNotifications=affirmedSnmpNotifications, affirmedSnmpNotificationPrefix=affirmedSnmpNotificationPrefix, affirmedSnmpEnumerations=affirmedSnmpEnumerations)
