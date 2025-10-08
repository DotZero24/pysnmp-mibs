#
# PySNMP MIB module HP-ICF-DEVICEIDENTITY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/hp/HP-ICF-DEVICEIDENTITY-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:02:34 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
hpSwitch, = mibBuilder.importSymbols("HP-ICF-OID", "hpSwitch")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Unsigned32, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Unsigned32", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention")
hpicfDeviceIdentityMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 135))
hpicfDeviceIdentityMIB.setRevisions(('2019-07-16 00:00', '2017-12-05 00:00', '2017-01-03 00:00',))
if mibBuilder.loadTexts: hpicfDeviceIdentityMIB.setLastUpdated('201907160000Z')
if mibBuilder.loadTexts: hpicfDeviceIdentityMIB.setOrganization('HP Networking')
hpicfDeviceIdentityConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 135, 1))
hpicfDeviceIdentityConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 135, 2))
hpicfDeviceIdentityTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 135, 1, 1), )
if mibBuilder.loadTexts: hpicfDeviceIdentityTable.setStatus('current')
hpicfDeviceIdentityEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 135, 1, 1, 1), ).setIndexNames((0, "HP-ICF-DEVICEIDENTITY-MIB", "hpicfDeviceIdentityIndex"))
if mibBuilder.loadTexts: hpicfDeviceIdentityEntry.setStatus('current')
hpicfDeviceIdentityIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 135, 1, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 16)))
if mibBuilder.loadTexts: hpicfDeviceIdentityIndex.setStatus('current')
hpicfDeviceIdentityRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 135, 1, 1, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpicfDeviceIdentityRowStatus.setStatus('current')
hpicfDeviceIdentityName = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 135, 1, 1, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 20))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpicfDeviceIdentityName.setStatus('current')
hpicfDeviceIdentityLldpOui = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 135, 1, 1, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(3, 3)).setFixedLength(3)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpicfDeviceIdentityLldpOui.setStatus('current')
hpicfDeviceIdentityLldpSubType = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 135, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpicfDeviceIdentityLldpSubType.setStatus('current')
hpicfDeviceIdentityLldpSysName = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 135, 1, 1, 1, 6), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 512))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpicfDeviceIdentityLldpSysName.setStatus('current')
hpicfDeviceIdentityLldpSysDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 135, 1, 1, 1, 7), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 512))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpicfDeviceIdentityLldpSysDescr.setStatus('current')
hpicfCdpBypassTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 135, 1, 2), )
if mibBuilder.loadTexts: hpicfCdpBypassTable.setStatus('current')
hpicfCdpBypassEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 135, 1, 2, 1), ).setIndexNames((0, "HP-ICF-DEVICEIDENTITY-MIB", "hpicfDeviceIdentityIndex"), (0, "HP-ICF-DEVICEIDENTITY-MIB", "hpicfDevIdentityCdpType"))
if mibBuilder.loadTexts: hpicfCdpBypassEntry.setStatus('current')
hpicfDevIdentityCdpType = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 135, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 19)))
if mibBuilder.loadTexts: hpicfDevIdentityCdpType.setStatus('current')
hpicfDevIdentityCdpValue = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 135, 1, 2, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpicfDevIdentityCdpValue.setStatus('current')
hpicfDevIdentityCdpRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 135, 1, 2, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpicfDevIdentityCdpRowStatus.setStatus('current')
hpicfDeviceIdentityGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 135, 2, 1))
hpicfDeviceIdentityCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 135, 2, 2))
hpicfiDeviceIdentityCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 135, 2, 2, 1)).setObjects(("HP-ICF-DEVICEIDENTITY-MIB", "hpicfDeviceIdentityGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfiDeviceIdentityCompliance = hpicfiDeviceIdentityCompliance.setStatus('deprecated')
hpicfiDeviceIdentityCompliance1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 135, 2, 2, 2)).setObjects(("HP-ICF-DEVICEIDENTITY-MIB", "hpicfDeviceIdentityGroup1"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfiDeviceIdentityCompliance1 = hpicfiDeviceIdentityCompliance1.setStatus('deprecated')
hpicfDeviceIdentityCompliance2 = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 135, 2, 2, 3)).setObjects(("HP-ICF-DEVICEIDENTITY-MIB", "hpicfDeviceIdentityGroup2"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfDeviceIdentityCompliance2 = hpicfDeviceIdentityCompliance2.setStatus('current')
hpicfDeviceIdentityGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 135, 2, 1, 1)).setObjects(("HP-ICF-DEVICEIDENTITY-MIB", "hpicfDeviceIdentityRowStatus"), ("HP-ICF-DEVICEIDENTITY-MIB", "hpicfDeviceIdentityName"), ("HP-ICF-DEVICEIDENTITY-MIB", "hpicfDeviceIdentityLldpOui"), ("HP-ICF-DEVICEIDENTITY-MIB", "hpicfDeviceIdentityLldpSubType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfDeviceIdentityGroup = hpicfDeviceIdentityGroup.setStatus('deprecated')
hpicfDeviceIdentityGroup1 = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 135, 2, 1, 2)).setObjects(("HP-ICF-DEVICEIDENTITY-MIB", "hpicfDeviceIdentityRowStatus"), ("HP-ICF-DEVICEIDENTITY-MIB", "hpicfDeviceIdentityName"), ("HP-ICF-DEVICEIDENTITY-MIB", "hpicfDeviceIdentityLldpOui"), ("HP-ICF-DEVICEIDENTITY-MIB", "hpicfDeviceIdentityLldpSubType"), ("HP-ICF-DEVICEIDENTITY-MIB", "hpicfDevIdentityCdpValue"), ("HP-ICF-DEVICEIDENTITY-MIB", "hpicfDevIdentityCdpRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfDeviceIdentityGroup1 = hpicfDeviceIdentityGroup1.setStatus('deprecated')
hpicfDeviceIdentityGroup2 = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 135, 2, 1, 3)).setObjects(("HP-ICF-DEVICEIDENTITY-MIB", "hpicfDeviceIdentityRowStatus"), ("HP-ICF-DEVICEIDENTITY-MIB", "hpicfDeviceIdentityName"), ("HP-ICF-DEVICEIDENTITY-MIB", "hpicfDeviceIdentityLldpOui"), ("HP-ICF-DEVICEIDENTITY-MIB", "hpicfDeviceIdentityLldpSubType"), ("HP-ICF-DEVICEIDENTITY-MIB", "hpicfDeviceIdentityLldpSysName"), ("HP-ICF-DEVICEIDENTITY-MIB", "hpicfDeviceIdentityLldpSysDescr"), ("HP-ICF-DEVICEIDENTITY-MIB", "hpicfDevIdentityCdpValue"), ("HP-ICF-DEVICEIDENTITY-MIB", "hpicfDevIdentityCdpRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfDeviceIdentityGroup2 = hpicfDeviceIdentityGroup2.setStatus('current')
mibBuilder.exportSymbols("HP-ICF-DEVICEIDENTITY-MIB", hpicfDeviceIdentityGroup=hpicfDeviceIdentityGroup, hpicfDeviceIdentityRowStatus=hpicfDeviceIdentityRowStatus, hpicfCdpBypassEntry=hpicfCdpBypassEntry, hpicfDeviceIdentityMIB=hpicfDeviceIdentityMIB, hpicfDevIdentityCdpRowStatus=hpicfDevIdentityCdpRowStatus, hpicfDeviceIdentityGroup2=hpicfDeviceIdentityGroup2, hpicfiDeviceIdentityCompliance=hpicfiDeviceIdentityCompliance, hpicfDeviceIdentityLldpOui=hpicfDeviceIdentityLldpOui, hpicfDeviceIdentityGroup1=hpicfDeviceIdentityGroup1, hpicfDevIdentityCdpValue=hpicfDevIdentityCdpValue, hpicfDeviceIdentityLldpSysDescr=hpicfDeviceIdentityLldpSysDescr, hpicfDeviceIdentityIndex=hpicfDeviceIdentityIndex, hpicfDeviceIdentityConformance=hpicfDeviceIdentityConformance, PYSNMP_MODULE_ID=hpicfDeviceIdentityMIB, hpicfDevIdentityCdpType=hpicfDevIdentityCdpType, hpicfDeviceIdentityLldpSubType=hpicfDeviceIdentityLldpSubType, hpicfiDeviceIdentityCompliance1=hpicfiDeviceIdentityCompliance1, hpicfDeviceIdentityLldpSysName=hpicfDeviceIdentityLldpSysName, hpicfCdpBypassTable=hpicfCdpBypassTable, hpicfDeviceIdentityCompliances=hpicfDeviceIdentityCompliances, hpicfDeviceIdentityEntry=hpicfDeviceIdentityEntry, hpicfDeviceIdentityConfig=hpicfDeviceIdentityConfig, hpicfDeviceIdentityCompliance2=hpicfDeviceIdentityCompliance2, hpicfDeviceIdentityName=hpicfDeviceIdentityName, hpicfDeviceIdentityTable=hpicfDeviceIdentityTable, hpicfDeviceIdentityGroups=hpicfDeviceIdentityGroups)
