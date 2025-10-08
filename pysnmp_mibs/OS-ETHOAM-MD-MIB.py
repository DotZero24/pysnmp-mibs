#
# PySNMP MIB module OS-ETHOAM-MD-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/mrv/OS-ETHOAM-MD-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:07:42 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
PortList, EntryValidator, oaOptiSwitch = mibBuilder.importSymbols("OS-COMMON-TC-MIB", "PortList", "EntryValidator", "oaOptiSwitch")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
osEthOamMd = ModuleIdentity((1, 3, 6, 1, 4, 1, 6926, 2, 13))
osEthOamMd.setRevisions(('2010-08-01 00:00',))
if mibBuilder.loadTexts: osEthOamMd.setLastUpdated('201008010000Z')
if mibBuilder.loadTexts: osEthOamMd.setOrganization('MRV Communications, Inc.')
osEthOamMdCapabilities = MibIdentifier((1, 3, 6, 1, 4, 1, 6926, 2, 13, 1))
osEthOamMdConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 6926, 2, 13, 100))
osEthOamMdMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 6926, 2, 13, 100, 1))
osEthOamMdMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 6926, 2, 13, 100, 2))
osEthOamMdSupport = MibScalar((1, 3, 6, 1, 4, 1, 6926, 2, 13, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("notSupported", 1), ("supported", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: osEthOamMdSupport.setStatus('current')
osEthOamMdTable = MibTable((1, 3, 6, 1, 4, 1, 6926, 2, 13, 2), )
if mibBuilder.loadTexts: osEthOamMdTable.setStatus('current')
osEthOamMdEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6926, 2, 13, 2, 1), ).setIndexNames((0, "OS-ETHOAM-MD-MIB", "osEthOamMdLevel"))
if mibBuilder.loadTexts: osEthOamMdEntry.setStatus('current')
osEthOamMdLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 6926, 2, 13, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7)))
if mibBuilder.loadTexts: osEthOamMdLevel.setStatus('current')
osEthOamMdFormat = MibTableColumn((1, 3, 6, 1, 4, 1, 6926, 2, 13, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("none", 1), ("dnsLikeName", 2), ("macAddressAndUint", 3), ("charString", 4))).clone('none')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: osEthOamMdFormat.setStatus('current')
osEthOamMdName = MibTableColumn((1, 3, 6, 1, 4, 1, 6926, 2, 13, 2, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 43))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: osEthOamMdName.setStatus('current')
osEthOamMdCPorts = MibTableColumn((1, 3, 6, 1, 4, 1, 6926, 2, 13, 2, 1, 4), PortList()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: osEthOamMdCPorts.setStatus('current')
osEthOamMdAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6926, 2, 13, 2, 1, 90), EntryValidator()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: osEthOamMdAdminStatus.setStatus('current')
osEthOamMdMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 6926, 2, 13, 100, 1, 1)).setObjects(("OS-ETHOAM-MD-MIB", "osEthOamMdMandatoryGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    osEthOamMdMIBCompliance = osEthOamMdMIBCompliance.setStatus('current')
osEthOamMdMandatoryGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6926, 2, 13, 100, 2, 1)).setObjects(("OS-ETHOAM-MD-MIB", "osEthOamMdSupport"), ("OS-ETHOAM-MD-MIB", "osEthOamMdFormat"), ("OS-ETHOAM-MD-MIB", "osEthOamMdName"), ("OS-ETHOAM-MD-MIB", "osEthOamMdCPorts"), ("OS-ETHOAM-MD-MIB", "osEthOamMdAdminStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    osEthOamMdMandatoryGroup = osEthOamMdMandatoryGroup.setStatus('current')
mibBuilder.exportSymbols("OS-ETHOAM-MD-MIB", osEthOamMdMIBCompliance=osEthOamMdMIBCompliance, osEthOamMdLevel=osEthOamMdLevel, osEthOamMdMIBGroups=osEthOamMdMIBGroups, PYSNMP_MODULE_ID=osEthOamMd, osEthOamMdMandatoryGroup=osEthOamMdMandatoryGroup, osEthOamMd=osEthOamMd, osEthOamMdEntry=osEthOamMdEntry, osEthOamMdCapabilities=osEthOamMdCapabilities, osEthOamMdTable=osEthOamMdTable, osEthOamMdName=osEthOamMdName, osEthOamMdMIBCompliances=osEthOamMdMIBCompliances, osEthOamMdCPorts=osEthOamMdCPorts, osEthOamMdFormat=osEthOamMdFormat, osEthOamMdAdminStatus=osEthOamMdAdminStatus, osEthOamMdSupport=osEthOamMdSupport, osEthOamMdConformance=osEthOamMdConformance)
