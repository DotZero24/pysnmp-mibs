#
# PySNMP MIB module CISCO-GGSN-GEO-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/cisco/CISCO-GGSN-GEO-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:28:13 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TruthValue, RowStatus, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "RowStatus", "TextualConvention", "DisplayString")
cggsnGeoMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 724))
cggsnGeoMIB.setRevisions(('2010-02-19 00:00',))
if mibBuilder.loadTexts: cggsnGeoMIB.setLastUpdated('201002190000Z')
if mibBuilder.loadTexts: cggsnGeoMIB.setOrganization('Cisco Systems, Inc.')
cggsnGeoPassiveTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 724, 1), )
if mibBuilder.loadTexts: cggsnGeoPassiveTable.setStatus('current')
cggsnGeoPassiveEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 724, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "CISCO-GGSN-GEO-MIB", "cggsnGeoProcessNumber"))
if mibBuilder.loadTexts: cggsnGeoPassiveEntry.setStatus('current')
cggsnGeoProcessNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 724, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)))
if mibBuilder.loadTexts: cggsnGeoProcessNumber.setStatus('current')
cggsnGeoPassiveStdbyIfName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 724, 1, 1, 2), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cggsnGeoPassiveStdbyIfName.setStatus('current')
cggsnGeoPassiveIfOnStdby = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 724, 1, 1, 3), TruthValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cggsnGeoPassiveIfOnStdby.setStatus('current')
cggsnGeoVRFEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 724, 1, 1, 4), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cggsnGeoVRFEnabled.setStatus('current')
cggsnGeoRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 724, 1, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cggsnGeoRowStatus.setStatus('current')
cggsnGeoConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 724, 2))
cggsnGeogroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 724, 2, 1))
cggsnGeoCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 724, 2, 2))
cggsnGeoCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 724, 2, 2, 1)).setObjects(("CISCO-GGSN-GEO-MIB", "cggsnGeoPassiveGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cggsnGeoCompliance = cggsnGeoCompliance.setStatus('current')
cggsnGeoPassiveGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 724, 2, 1, 1)).setObjects(("CISCO-GGSN-GEO-MIB", "cggsnGeoPassiveStdbyIfName"), ("CISCO-GGSN-GEO-MIB", "cggsnGeoPassiveIfOnStdby"), ("CISCO-GGSN-GEO-MIB", "cggsnGeoVRFEnabled"), ("CISCO-GGSN-GEO-MIB", "cggsnGeoRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cggsnGeoPassiveGroup = cggsnGeoPassiveGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-GGSN-GEO-MIB", cggsnGeoPassiveStdbyIfName=cggsnGeoPassiveStdbyIfName, cggsnGeogroups=cggsnGeogroups, cggsnGeoRowStatus=cggsnGeoRowStatus, cggsnGeoPassiveGroup=cggsnGeoPassiveGroup, cggsnGeoMIB=cggsnGeoMIB, cggsnGeoCompliances=cggsnGeoCompliances, cggsnGeoConformance=cggsnGeoConformance, cggsnGeoCompliance=cggsnGeoCompliance, cggsnGeoProcessNumber=cggsnGeoProcessNumber, PYSNMP_MODULE_ID=cggsnGeoMIB, cggsnGeoPassiveIfOnStdby=cggsnGeoPassiveIfOnStdby, cggsnGeoPassiveTable=cggsnGeoPassiveTable, cggsnGeoPassiveEntry=cggsnGeoPassiveEntry, cggsnGeoVRFEnabled=cggsnGeoVRFEnabled)
