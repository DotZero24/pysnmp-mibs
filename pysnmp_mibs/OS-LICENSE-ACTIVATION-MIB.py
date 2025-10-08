#
# PySNMP MIB module OS-LICENSE-ACTIVATION-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/mrv/OS-LICENSE-ACTIVATION-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:16:43 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
oaOptiSwitch, = mibBuilder.importSymbols("OS-COMMON-TC-MIB", "oaOptiSwitch")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, enterprises, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "enterprises", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
osLicenseActivation = ModuleIdentity((1, 3, 6, 1, 4, 1, 6926, 2, 27))
osLicenseActivation.setRevisions(('2014-02-04 00:00',))
if mibBuilder.loadTexts: osLicenseActivation.setLastUpdated('201402040000Z')
if mibBuilder.loadTexts: osLicenseActivation.setOrganization('MRV Communications, Inc.')
osRoutingProtocolsActivation = MibIdentifier((1, 3, 6, 1, 4, 1, 6926, 2, 27, 1))
osMplsActivation = MibIdentifier((1, 3, 6, 1, 4, 1, 6926, 2, 27, 2))
osLicenseActivationConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 6926, 2, 27, 100))
osLicenseActivationMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 6926, 2, 27, 100, 1))
osLicenseActivationMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 6926, 2, 27, 100, 2))
class OsActivationLicense(TextualConvention, OctetString):
    status = 'current'
    displayHint = '12a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(12, 12)
    fixedLength = 12

class OsActivationStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("unknown", 1), ("active", 2), ("notActive", 3), ("notSupported", 4))

osRoutingProtocolsActivationLicense = MibScalar((1, 3, 6, 1, 4, 1, 6926, 2, 27, 1, 1), OsActivationLicense()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: osRoutingProtocolsActivationLicense.setStatus('current')
osRoutingProtocolsActivationSatus = MibScalar((1, 3, 6, 1, 4, 1, 6926, 2, 27, 1, 2), OsActivationStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: osRoutingProtocolsActivationSatus.setStatus('current')
osMplsActivationLicense = MibScalar((1, 3, 6, 1, 4, 1, 6926, 2, 27, 2, 1), OsActivationLicense()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: osMplsActivationLicense.setStatus('current')
osMplsActivationSatus = MibScalar((1, 3, 6, 1, 4, 1, 6926, 2, 27, 2, 2), OsActivationStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: osMplsActivationSatus.setStatus('current')
osActvFeatMgmtTable = MibTable((1, 3, 6, 1, 4, 1, 6926, 2, 27, 8), )
if mibBuilder.loadTexts: osActvFeatMgmtTable.setStatus('current')
osActvFeatMgmtEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6926, 2, 27, 8, 1), ).setIndexNames((0, "OS-LICENSE-ACTIVATION-MIB", "osActvFeatMgmtId"))
if mibBuilder.loadTexts: osActvFeatMgmtEntry.setStatus('current')
osActvFeatMgmtId = MibTableColumn((1, 3, 6, 1, 4, 1, 6926, 2, 27, 8, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("os600withGigaPorts", 1), ("securePush", 2), ("routingProtocols", 3), ("mplsProtocols", 4))))
if mibBuilder.loadTexts: osActvFeatMgmtId.setStatus('current')
osActvFeatMgmtStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6926, 2, 27, 8, 1, 2), OsActivationStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: osActvFeatMgmtStatus.setStatus('current')
osActvFeatMgmtParam = MibTableColumn((1, 3, 6, 1, 4, 1, 6926, 2, 27, 8, 1, 3), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: osActvFeatMgmtParam.setStatus('current')
osActvFeatMgmtKey = MibTableColumn((1, 3, 6, 1, 4, 1, 6926, 2, 27, 8, 1, 4), OsActivationLicense()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: osActvFeatMgmtKey.setStatus('current')
osLicenseActivationMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 6926, 2, 27, 100, 1, 1)).setObjects(("OS-LICENSE-ACTIVATION-MIB", "osLicenseActivationMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    osLicenseActivationMIBCompliance = osLicenseActivationMIBCompliance.setStatus('current')
osLicenseActivationMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6926, 2, 27, 100, 2, 1)).setObjects(("OS-LICENSE-ACTIVATION-MIB", "osRoutingProtocolsActivationLicense"), ("OS-LICENSE-ACTIVATION-MIB", "osRoutingProtocolsActivationSatus"), ("OS-LICENSE-ACTIVATION-MIB", "osMplsActivationLicense"), ("OS-LICENSE-ACTIVATION-MIB", "osMplsActivationSatus"), ("OS-LICENSE-ACTIVATION-MIB", "osActvFeatMgmtStatus"), ("OS-LICENSE-ACTIVATION-MIB", "osActvFeatMgmtParam"), ("OS-LICENSE-ACTIVATION-MIB", "osActvFeatMgmtKey"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    osLicenseActivationMIBGroup = osLicenseActivationMIBGroup.setStatus('current')
mibBuilder.exportSymbols("OS-LICENSE-ACTIVATION-MIB", osActvFeatMgmtEntry=osActvFeatMgmtEntry, osActvFeatMgmtKey=osActvFeatMgmtKey, osMplsActivationSatus=osMplsActivationSatus, osLicenseActivationMIBCompliances=osLicenseActivationMIBCompliances, osActvFeatMgmtParam=osActvFeatMgmtParam, osRoutingProtocolsActivationLicense=osRoutingProtocolsActivationLicense, PYSNMP_MODULE_ID=osLicenseActivation, osMplsActivation=osMplsActivation, osLicenseActivationMIBGroups=osLicenseActivationMIBGroups, OsActivationStatus=OsActivationStatus, osLicenseActivationMIBCompliance=osLicenseActivationMIBCompliance, osActvFeatMgmtId=osActvFeatMgmtId, osLicenseActivationMIBGroup=osLicenseActivationMIBGroup, osMplsActivationLicense=osMplsActivationLicense, osLicenseActivation=osLicenseActivation, osLicenseActivationConformance=osLicenseActivationConformance, osActvFeatMgmtTable=osActvFeatMgmtTable, osRoutingProtocolsActivation=osRoutingProtocolsActivation, osActvFeatMgmtStatus=osActvFeatMgmtStatus, OsActivationLicense=OsActivationLicense, osRoutingProtocolsActivationSatus=osRoutingProtocolsActivationSatus)
