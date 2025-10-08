#
# PySNMP MIB module HP-ICF-GENERIC-VLAN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/hp/HP-ICF-GENERIC-VLAN-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:08:15 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
hpSwitch, = mibBuilder.importSymbols("HP-ICF-OID", "hpSwitch")
VlanId, dot1qTpFdbEntry = mibBuilder.importSymbols("Q-BRIDGE-MIB", "VlanId", "dot1qTpFdbEntry")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
hpicfGenericVlanMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 67))
hpicfGenericVlanMIB.setRevisions(('2017-06-28 00:00', '2010-02-08 00:00',))
if mibBuilder.loadTexts: hpicfGenericVlanMIB.setLastUpdated('201706280000Z')
if mibBuilder.loadTexts: hpicfGenericVlanMIB.setOrganization('HP Networking')
hpicfGenericVlanFeaturesObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 67, 1))
hpicfGenericVlanFeaturesConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 67, 2))
hpicfGenericVlanFeaturesTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 67, 1, 1), )
if mibBuilder.loadTexts: hpicfGenericVlanFeaturesTable.setStatus('current')
hpicfGenericVlanFeaturesEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 67, 1, 1, 1), )
dot1qTpFdbEntry.registerAugmentions(("HP-ICF-GENERIC-VLAN-MIB", "hpicfGenericVlanFeaturesEntry"))
hpicfGenericVlanFeaturesEntry.setIndexNames(*dot1qTpFdbEntry.getIndexNames())
if mibBuilder.loadTexts: hpicfGenericVlanFeaturesEntry.setStatus('current')
hpicfMacNotifyClearVlanControl = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 67, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("noOperation", 1), ("macNotifyClearVlan", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfMacNotifyClearVlanControl.setStatus('current')
hpicfDot1qTpFdbVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 67, 1, 1, 1, 2), VlanId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfDot1qTpFdbVlanId.setStatus('current')
hpicfDot1qTpFdbInstalledTime = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 67, 1, 1, 1, 3), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfDot1qTpFdbInstalledTime.setStatus('current')
hpicfGenericVlanFeaturesCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 67, 2, 1))
hpicfGenericVlanFeaturesGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 67, 2, 2))
hpicfGenericVlanFeaturesCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 67, 2, 1, 1)).setObjects(("HP-ICF-GENERIC-VLAN-MIB", "hpicfGenericVlanFeaturesConfigGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfGenericVlanFeaturesCompliance = hpicfGenericVlanFeaturesCompliance.setStatus('deprecated')
hpicfGenericVlanFeaturesComp1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 67, 2, 1, 2)).setObjects(("HP-ICF-GENERIC-VLAN-MIB", "hpicfGenericVlanFeaturesConfGrp1"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfGenericVlanFeaturesComp1 = hpicfGenericVlanFeaturesComp1.setStatus('current')
hpicfGenericVlanFeaturesConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 67, 2, 2, 2)).setObjects(("HP-ICF-GENERIC-VLAN-MIB", "hpicfMacNotifyClearVlanControl"), ("HP-ICF-GENERIC-VLAN-MIB", "hpicfDot1qTpFdbVlanId"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfGenericVlanFeaturesConfigGroup = hpicfGenericVlanFeaturesConfigGroup.setStatus('deprecated')
hpicfGenericVlanFeaturesConfGrp1 = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 67, 2, 2, 3)).setObjects(("HP-ICF-GENERIC-VLAN-MIB", "hpicfMacNotifyClearVlanControl"), ("HP-ICF-GENERIC-VLAN-MIB", "hpicfDot1qTpFdbVlanId"), ("HP-ICF-GENERIC-VLAN-MIB", "hpicfDot1qTpFdbInstalledTime"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfGenericVlanFeaturesConfGrp1 = hpicfGenericVlanFeaturesConfGrp1.setStatus('current')
mibBuilder.exportSymbols("HP-ICF-GENERIC-VLAN-MIB", hpicfGenericVlanFeaturesTable=hpicfGenericVlanFeaturesTable, hpicfDot1qTpFdbInstalledTime=hpicfDot1qTpFdbInstalledTime, PYSNMP_MODULE_ID=hpicfGenericVlanMIB, hpicfGenericVlanFeaturesConformance=hpicfGenericVlanFeaturesConformance, hpicfGenericVlanFeaturesCompliances=hpicfGenericVlanFeaturesCompliances, hpicfGenericVlanFeaturesComp1=hpicfGenericVlanFeaturesComp1, hpicfGenericVlanFeaturesObjects=hpicfGenericVlanFeaturesObjects, hpicfGenericVlanFeaturesConfGrp1=hpicfGenericVlanFeaturesConfGrp1, hpicfMacNotifyClearVlanControl=hpicfMacNotifyClearVlanControl, hpicfGenericVlanFeaturesEntry=hpicfGenericVlanFeaturesEntry, hpicfDot1qTpFdbVlanId=hpicfDot1qTpFdbVlanId, hpicfGenericVlanFeaturesGroups=hpicfGenericVlanFeaturesGroups, hpicfGenericVlanMIB=hpicfGenericVlanMIB, hpicfGenericVlanFeaturesConfigGroup=hpicfGenericVlanFeaturesConfigGroup, hpicfGenericVlanFeaturesCompliance=hpicfGenericVlanFeaturesCompliance)
