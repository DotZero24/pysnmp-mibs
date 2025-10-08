#
# PySNMP MIB module HP-ICF-LAYER3VLAN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/hp/HP-ICF-LAYER3VLAN-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:09:27 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
hpSwitch, = mibBuilder.importSymbols("HP-ICF-OID", "hpSwitch")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
hpicfLayer3VlanConfigMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 70))
hpicfLayer3VlanConfigMIB.setRevisions(('2010-03-23 00:00',))
if mibBuilder.loadTexts: hpicfLayer3VlanConfigMIB.setLastUpdated('201003230000Z')
if mibBuilder.loadTexts: hpicfLayer3VlanConfigMIB.setOrganization('HP Networking')
hpicfLayer3VlanConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 70, 1))
hpicfLayer3VlanConfigConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 70, 2))
hpicfLayer3VlanConfigTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 70, 1, 1), )
if mibBuilder.loadTexts: hpicfLayer3VlanConfigTable.setStatus('current')
hpicfLayer3VlanConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 70, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: hpicfLayer3VlanConfigEntry.setStatus('current')
hpicfLayer3VlanStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 70, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('enable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfLayer3VlanStatus.setStatus('current')
hpicfL3VlanConfigMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 70, 2, 1))
hpicfLayer3VlanConfigMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 70, 2, 2))
hpicfL3VlanConfigMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 70, 2, 1, 1)).setObjects(("HP-ICF-LAYER3VLAN-MIB", "hpicfLayer3VlanConfigGroup"), ("HP-ICF-LAYER3VLAN-MIB", "hpicfLayer3VlanConfigGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfL3VlanConfigMIBCompliance = hpicfL3VlanConfigMIBCompliance.setStatus('current')
hpicfLayer3VlanConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 70, 2, 2, 1)).setObjects(("HP-ICF-LAYER3VLAN-MIB", "hpicfLayer3VlanStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfLayer3VlanConfigGroup = hpicfLayer3VlanConfigGroup.setStatus('current')
mibBuilder.exportSymbols("HP-ICF-LAYER3VLAN-MIB", hpicfL3VlanConfigMIBCompliances=hpicfL3VlanConfigMIBCompliances, PYSNMP_MODULE_ID=hpicfLayer3VlanConfigMIB, hpicfLayer3VlanConfigConformance=hpicfLayer3VlanConfigConformance, hpicfLayer3VlanConfig=hpicfLayer3VlanConfig, hpicfLayer3VlanConfigMIBGroups=hpicfLayer3VlanConfigMIBGroups, hpicfLayer3VlanStatus=hpicfLayer3VlanStatus, hpicfLayer3VlanConfigEntry=hpicfLayer3VlanConfigEntry, hpicfLayer3VlanConfigTable=hpicfLayer3VlanConfigTable, hpicfL3VlanConfigMIBCompliance=hpicfL3VlanConfigMIBCompliance, hpicfLayer3VlanConfigGroup=hpicfLayer3VlanConfigGroup, hpicfLayer3VlanConfigMIB=hpicfLayer3VlanConfigMIB)
