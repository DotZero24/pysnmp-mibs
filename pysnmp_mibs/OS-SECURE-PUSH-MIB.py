#
# PySNMP MIB module OS-SECURE-PUSH-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/mrv/OS-SECURE-PUSH-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:07:22 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
oaOptiSwitch, = mibBuilder.importSymbols("OS-COMMON-TC-MIB", "oaOptiSwitch")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, enterprises, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "enterprises", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
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
mibBuilder.exportSymbols("OS-SECURE-PUSH-MIB", PYSNMP_MODULE_ID=osSecurePush, osSecurePush=osSecurePush, osSecurePushMibMandatoryGroup=osSecurePushMibMandatoryGroup, osSecurePushSupport=osSecurePushSupport, osSecurePushConfAdminStatus=osSecurePushConfAdminStatus, osSecurePushGeneral=osSecurePushGeneral, osSecurePushMIBGroups=osSecurePushMIBGroups, osSecurePushConformance=osSecurePushConformance, osSecurePushMIBCompliances=osSecurePushMIBCompliances, osSecurePushMIBCompliance=osSecurePushMIBCompliance)
