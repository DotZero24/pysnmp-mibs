#
# PySNMP MIB module HP-ICF-L3MAC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/hp/HP-ICF-L3MAC-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:09:11 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
hpSwitch, = mibBuilder.importSymbols("HP-ICF-OID", "hpSwitch")
ifRcvAddressEntry, = mibBuilder.importSymbols("IF-MIB", "ifRcvAddressEntry")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("HP-ICF-L3MAC-MIB", hpicfL3MacConfigGroup=hpicfL3MacConfigGroup, hpicfL3MacConfigObjects=hpicfL3MacConfigObjects, hpicfL3MacConfigConformance=hpicfL3MacConfigConformance, PYSNMP_MODULE_ID=hpicfL3MacConfigMIB, hpicfL3MacConfigMIBCompliances=hpicfL3MacConfigMIBCompliances, hpicfL3MacConfigMIBCompliance=hpicfL3MacConfigMIBCompliance, hpicfL3MacConfigIfEntry=hpicfL3MacConfigIfEntry, hpicfL3MacConfigMIBGroups=hpicfL3MacConfigMIBGroups, hpicfL3MacConfigIfTable=hpicfL3MacConfigIfTable, hpicfL3MacConfigIfAdvTimer=hpicfL3MacConfigIfAdvTimer, hpicfL3MacConfigMIB=hpicfL3MacConfigMIB)
