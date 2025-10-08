#
# PySNMP MIB module OS-SECURE-PUSH-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/mrv/OS-SECURE-PUSH-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:16:15 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
oaOptiSwitch, = mibBuilder.importSymbols("OS-COMMON-TC-MIB", "oaOptiSwitch")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, enterprises, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "enterprises", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
osSecurePush = ModuleIdentity((1, 3, 6, 1, 4, 1, 6926, 2, 24))
osSecurePush.setRevisions(('2012-12-19 00:00',))
if mibBuilder.loadTexts: osSecurePush.setLastUpdated('201212190000Z')
if mibBuilder.loadTexts: osSecurePush.setOrganization('MRV Communications, Inc.')
osSecurePushGeneral = MibIdentifier((1, 3, 6, 1, 4, 1, 6926, 2, 24, 1))
osSecurePushConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 6926, 2, 24, 100))
osSecurePushMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 6926, 2, 24, 100, 1))
osSecurePushMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 6926, 2, 24, 100, 2))
osSecurePushSupport = MibScalar((1, 3, 6, 1, 4, 1, 6926, 2, 24, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("notSupported", 1), ("supported", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: osSecurePushSupport.setStatus('current')
osSecurePushConfAdminStatus = MibScalar((1, 3, 6, 1, 4, 1, 6926, 2, 24, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("unknown", 1), ("askFromServer", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: osSecurePushConfAdminStatus.setStatus('current')
osSecurePushMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 6926, 2, 24, 100, 1, 1)).setObjects(("OS-SECURE-PUSH-MIB", "osSecurePushMibMandatoryGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    osSecurePushMIBCompliance = osSecurePushMIBCompliance.setStatus('current')
osSecurePushMibMandatoryGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6926, 2, 24, 100, 2, 1)).setObjects(("OS-SECURE-PUSH-MIB", "osSecurePushSupport"), ("OS-SECURE-PUSH-MIB", "osSecurePushConfAdminStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    osSecurePushMibMandatoryGroup = osSecurePushMibMandatoryGroup.setStatus('current')
mibBuilder.exportSymbols("OS-SECURE-PUSH-MIB", osSecurePushGeneral=osSecurePushGeneral, osSecurePushMIBGroups=osSecurePushMIBGroups, osSecurePushMIBCompliance=osSecurePushMIBCompliance, PYSNMP_MODULE_ID=osSecurePush, osSecurePush=osSecurePush, osSecurePushConformance=osSecurePushConformance, osSecurePushMibMandatoryGroup=osSecurePushMibMandatoryGroup, osSecurePushMIBCompliances=osSecurePushMIBCompliances, osSecurePushConfAdminStatus=osSecurePushConfAdminStatus, osSecurePushSupport=osSecurePushSupport)
