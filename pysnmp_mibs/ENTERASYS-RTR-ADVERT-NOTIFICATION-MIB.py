#
# PySNMP MIB module ENTERASYS-RTR-ADVERT-NOTIFICATION-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/enterasys/ENTERASYS-RTR-ADVERT-NOTIFICATION-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:17:26 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
etsysModules, = mibBuilder.importSymbols("ENTERASYS-MIB-NAMES", "etsysModules")
ifName, = mibBuilder.importSymbols("IF-MIB", "ifName")
InetAddressType, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetAddress")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, iso, Counter32, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "iso", "Counter32", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention")
etsysRtrAdvertNotificationMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 5624, 1, 2, 82))
etsysRtrAdvertNotificationMIB.setRevisions(('2011-05-13 13:47',))
if mibBuilder.loadTexts: etsysRtrAdvertNotificationMIB.setLastUpdated('201105131347Z')
if mibBuilder.loadTexts: etsysRtrAdvertNotificationMIB.setOrganization('Enterasys Networks, Inc')
etsysRtrAdvertNotificationObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 82, 1))
etsysRtrAdvertConfigBranch = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 82, 1, 0))
etsysRtrAdvertInformationBranch = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 82, 1, 1))
etsysRtrAdvertNotificationBranch = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 82, 1, 2))
etsysRtrAdvertInconsistentEnabled = MibScalar((1, 3, 6, 1, 4, 1, 5624, 1, 2, 82, 1, 0, 1), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsysRtrAdvertInconsistentEnabled.setStatus('current')
etsysRtrAdvertInetAddrType = MibScalar((1, 3, 6, 1, 4, 1, 5624, 1, 2, 82, 1, 1, 1), InetAddressType()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: etsysRtrAdvertInetAddrType.setStatus('current')
etsysRtrAdvertInetAddress = MibScalar((1, 3, 6, 1, 4, 1, 5624, 1, 2, 82, 1, 1, 2), InetAddress()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: etsysRtrAdvertInetAddress.setStatus('current')
etsysRtrAdvertUserData = MibScalar((1, 3, 6, 1, 4, 1, 5624, 1, 2, 82, 1, 1, 3), SnmpAdminString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: etsysRtrAdvertUserData.setStatus('current')
etsysRtrAdvertInconsistent = NotificationType((1, 3, 6, 1, 4, 1, 5624, 1, 2, 82, 1, 2, 1)).setObjects(("ENTERASYS-RTR-ADVERT-NOTIFICATION-MIB", "etsysRtrAdvertInetAddrType"), ("ENTERASYS-RTR-ADVERT-NOTIFICATION-MIB", "etsysRtrAdvertInetAddress"), ("IF-MIB", "ifName"), ("ENTERASYS-RTR-ADVERT-NOTIFICATION-MIB", "etsysRtrAdvertUserData"))
if mibBuilder.loadTexts: etsysRtrAdvertInconsistent.setStatus('current')
etsysRtrAdvertConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 82, 2))
etsysRtrAdvertGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 82, 2, 1))
etsysRtrAdvertCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 82, 2, 2))
etsysRtrAdvertConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 5624, 1, 2, 82, 2, 1, 1)).setObjects(("ENTERASYS-RTR-ADVERT-NOTIFICATION-MIB", "etsysRtrAdvertInconsistentEnabled"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysRtrAdvertConfigGroup = etsysRtrAdvertConfigGroup.setStatus('current')
etsysRtrAdvertInformationGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 5624, 1, 2, 82, 2, 1, 2)).setObjects(("ENTERASYS-RTR-ADVERT-NOTIFICATION-MIB", "etsysRtrAdvertInetAddrType"), ("ENTERASYS-RTR-ADVERT-NOTIFICATION-MIB", "etsysRtrAdvertInetAddress"), ("ENTERASYS-RTR-ADVERT-NOTIFICATION-MIB", "etsysRtrAdvertUserData"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysRtrAdvertInformationGroup = etsysRtrAdvertInformationGroup.setStatus('current')
etsysRtrAdvertNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 5624, 1, 2, 82, 2, 1, 3)).setObjects(("ENTERASYS-RTR-ADVERT-NOTIFICATION-MIB", "etsysRtrAdvertInconsistent"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysRtrAdvertNotificationGroup = etsysRtrAdvertNotificationGroup.setStatus('current')
etsysRtrAdvertCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 5624, 1, 2, 82, 2, 2, 1)).setObjects(("ENTERASYS-RTR-ADVERT-NOTIFICATION-MIB", "etsysRtrAdvertConfigGroup"), ("ENTERASYS-RTR-ADVERT-NOTIFICATION-MIB", "etsysRtrAdvertInformationGroup"), ("ENTERASYS-RTR-ADVERT-NOTIFICATION-MIB", "etsysRtrAdvertNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysRtrAdvertCompliance = etsysRtrAdvertCompliance.setStatus('current')
mibBuilder.exportSymbols("ENTERASYS-RTR-ADVERT-NOTIFICATION-MIB", PYSNMP_MODULE_ID=etsysRtrAdvertNotificationMIB, etsysRtrAdvertUserData=etsysRtrAdvertUserData, etsysRtrAdvertInetAddress=etsysRtrAdvertInetAddress, etsysRtrAdvertGroups=etsysRtrAdvertGroups, etsysRtrAdvertNotificationObjects=etsysRtrAdvertNotificationObjects, etsysRtrAdvertNotificationMIB=etsysRtrAdvertNotificationMIB, etsysRtrAdvertConformance=etsysRtrAdvertConformance, etsysRtrAdvertConfigGroup=etsysRtrAdvertConfigGroup, etsysRtrAdvertNotificationBranch=etsysRtrAdvertNotificationBranch, etsysRtrAdvertInconsistent=etsysRtrAdvertInconsistent, etsysRtrAdvertNotificationGroup=etsysRtrAdvertNotificationGroup, etsysRtrAdvertInetAddrType=etsysRtrAdvertInetAddrType, etsysRtrAdvertCompliances=etsysRtrAdvertCompliances, etsysRtrAdvertCompliance=etsysRtrAdvertCompliance, etsysRtrAdvertInconsistentEnabled=etsysRtrAdvertInconsistentEnabled, etsysRtrAdvertInformationGroup=etsysRtrAdvertInformationGroup, etsysRtrAdvertConfigBranch=etsysRtrAdvertConfigBranch, etsysRtrAdvertInformationBranch=etsysRtrAdvertInformationBranch)
