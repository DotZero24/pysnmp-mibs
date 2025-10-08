#
# PySNMP MIB module SNMP-VACM-AAA-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/rfc/SNMP-VACM-AAA-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:49:22 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
SnmpSecurityModel, SnmpAdminString = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpSecurityModel", "SnmpAdminString")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
Gauge32, MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, mib_2 = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "mib-2")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
vacmAaaMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 199))
vacmAaaMIB.setRevisions(('2010-12-09 00:00',))
if mibBuilder.loadTexts: vacmAaaMIB.setLastUpdated('201012090000Z')
if mibBuilder.loadTexts: vacmAaaMIB.setOrganization('ISMS Working Group')
vacmAaaMIBObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 199, 1))
vacmAaaMIBConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 199, 2))
vacmAaaSecurityToGroupTable = MibTable((1, 3, 6, 1, 2, 1, 199, 1, 1), )
if mibBuilder.loadTexts: vacmAaaSecurityToGroupTable.setStatus('current')
vacmAaaSecurityToGroupEntry = MibTableRow((1, 3, 6, 1, 2, 1, 199, 1, 1, 1), ).setIndexNames((0, "SNMP-VACM-AAA-MIB", "vacmAaaSecurityModel"), (0, "SNMP-VACM-AAA-MIB", "vacmAaaSecurityName"), (0, "SNMP-VACM-AAA-MIB", "vacmAaaSessionID"))
if mibBuilder.loadTexts: vacmAaaSecurityToGroupEntry.setStatus('current')
vacmAaaSecurityModel = MibTableColumn((1, 3, 6, 1, 2, 1, 199, 1, 1, 1, 1), SnmpSecurityModel().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: vacmAaaSecurityModel.setStatus('current')
vacmAaaSecurityName = MibTableColumn((1, 3, 6, 1, 2, 1, 199, 1, 1, 1, 2), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 32)))
if mibBuilder.loadTexts: vacmAaaSecurityName.setStatus('current')
vacmAaaSessionID = MibTableColumn((1, 3, 6, 1, 2, 1, 199, 1, 1, 1, 3), Unsigned32())
if mibBuilder.loadTexts: vacmAaaSessionID.setStatus('current')
vacmAaaGroupName = MibTableColumn((1, 3, 6, 1, 2, 1, 199, 1, 1, 1, 4), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vacmAaaGroupName.setStatus('current')
vacmAaaMIBCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 199, 2, 1))
vacmAaaMIBGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 199, 2, 2))
vacmAaaMIBBasicCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 199, 2, 1, 1)).setObjects(("SNMP-VACM-AAA-MIB", "vacmAaaGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vacmAaaMIBBasicCompliance = vacmAaaMIBBasicCompliance.setStatus('current')
vacmAaaGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 199, 2, 2, 1)).setObjects(("SNMP-VACM-AAA-MIB", "vacmAaaGroupName"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vacmAaaGroup = vacmAaaGroup.setStatus('current')
mibBuilder.exportSymbols("SNMP-VACM-AAA-MIB", vacmAaaMIBConformance=vacmAaaMIBConformance, vacmAaaMIB=vacmAaaMIB, vacmAaaSecurityModel=vacmAaaSecurityModel, vacmAaaSessionID=vacmAaaSessionID, vacmAaaMIBBasicCompliance=vacmAaaMIBBasicCompliance, vacmAaaSecurityName=vacmAaaSecurityName, vacmAaaMIBCompliances=vacmAaaMIBCompliances, vacmAaaGroup=vacmAaaGroup, vacmAaaGroupName=vacmAaaGroupName, vacmAaaMIBObjects=vacmAaaMIBObjects, PYSNMP_MODULE_ID=vacmAaaMIB, vacmAaaMIBGroups=vacmAaaMIBGroups, vacmAaaSecurityToGroupEntry=vacmAaaSecurityToGroupEntry, vacmAaaSecurityToGroupTable=vacmAaaSecurityToGroupTable)
