#
# PySNMP MIB module HP-ICF-L3MAC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/hp/HP-ICF-L3MAC-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:03:02 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
hpSwitch, = mibBuilder.importSymbols("HP-ICF-OID", "hpSwitch")
ifRcvAddressEntry, = mibBuilder.importSymbols("IF-MIB", "ifRcvAddressEntry")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
hpicfL3MacConfigMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 36))
hpicfL3MacConfigMIB.setRevisions(('2008-10-01 00:00', '2006-08-08 16:00',))
if mibBuilder.loadTexts: hpicfL3MacConfigMIB.setLastUpdated('200810010000Z')
if mibBuilder.loadTexts: hpicfL3MacConfigMIB.setOrganization('HP Networking')
hpicfL3MacConfigObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 36, 1))
hpicfL3MacConfigConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 36, 2))
hpicfL3MacConfigIfTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 36, 1, 1), )
if mibBuilder.loadTexts: hpicfL3MacConfigIfTable.setStatus('current')
hpicfL3MacConfigIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 36, 1, 1, 1), )
ifRcvAddressEntry.registerAugmentions(("HP-ICF-L3MAC-MIB", "hpicfL3MacConfigIfEntry"))
hpicfL3MacConfigIfEntry.setIndexNames(*ifRcvAddressEntry.getIndexNames())
if mibBuilder.loadTexts: hpicfL3MacConfigIfEntry.setStatus('current')
hpicfL3MacConfigIfAdvTimer = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 36, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255)).clone(60)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfL3MacConfigIfAdvTimer.setStatus('current')
hpicfL3MacConfigMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 36, 2, 1))
hpicfL3MacConfigMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 36, 2, 2))
hpicfL3MacConfigMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 36, 2, 1, 1)).setObjects(("HP-ICF-L3MAC-MIB", "hpicfL3MacConfigGroup"), ("HP-ICF-L3MAC-MIB", "hpicfL3MacConfigGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfL3MacConfigMIBCompliance = hpicfL3MacConfigMIBCompliance.setStatus('current')
hpicfL3MacConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 36, 2, 2, 1)).setObjects(("HP-ICF-L3MAC-MIB", "hpicfL3MacConfigIfAdvTimer"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfL3MacConfigGroup = hpicfL3MacConfigGroup.setStatus('current')
mibBuilder.exportSymbols("HP-ICF-L3MAC-MIB", hpicfL3MacConfigMIBCompliances=hpicfL3MacConfigMIBCompliances, hpicfL3MacConfigMIBGroups=hpicfL3MacConfigMIBGroups, hpicfL3MacConfigIfAdvTimer=hpicfL3MacConfigIfAdvTimer, hpicfL3MacConfigMIBCompliance=hpicfL3MacConfigMIBCompliance, PYSNMP_MODULE_ID=hpicfL3MacConfigMIB, hpicfL3MacConfigGroup=hpicfL3MacConfigGroup, hpicfL3MacConfigConformance=hpicfL3MacConfigConformance, hpicfL3MacConfigIfTable=hpicfL3MacConfigIfTable, hpicfL3MacConfigMIB=hpicfL3MacConfigMIB, hpicfL3MacConfigObjects=hpicfL3MacConfigObjects, hpicfL3MacConfigIfEntry=hpicfL3MacConfigIfEntry)
