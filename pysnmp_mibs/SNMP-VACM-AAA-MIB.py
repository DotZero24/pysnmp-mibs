#
# PySNMP MIB module SNMP-VACM-AAA-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/rfc/SNMP-VACM-AAA-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:27:12 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
SnmpAdminString, SnmpSecurityModel = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString", "SnmpSecurityModel")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Unsigned32, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, TimeTicks, MibIdentifier, Integer32, Bits, mib_2, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Unsigned32", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "TimeTicks", "MibIdentifier", "Integer32", "Bits", "mib-2", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
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
mibBuilder.exportSymbols("SNMP-VACM-AAA-MIB", vacmAaaSecurityToGroupEntry=vacmAaaSecurityToGroupEntry, vacmAaaSessionID=vacmAaaSessionID, vacmAaaSecurityModel=vacmAaaSecurityModel, vacmAaaMIBConformance=vacmAaaMIBConformance, vacmAaaSecurityToGroupTable=vacmAaaSecurityToGroupTable, vacmAaaSecurityName=vacmAaaSecurityName, vacmAaaMIBGroups=vacmAaaMIBGroups, vacmAaaMIBObjects=vacmAaaMIBObjects, vacmAaaMIBCompliances=vacmAaaMIBCompliances, vacmAaaGroup=vacmAaaGroup, vacmAaaMIB=vacmAaaMIB, vacmAaaMIBBasicCompliance=vacmAaaMIBBasicCompliance, PYSNMP_MODULE_ID=vacmAaaMIB, vacmAaaGroupName=vacmAaaGroupName)
