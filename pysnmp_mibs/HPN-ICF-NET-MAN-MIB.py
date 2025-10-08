#
# PySNMP MIB module HPN-ICF-NET-MAN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/hp/HPN-ICF-NET-MAN-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:02:48 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
hpnicfCommon, = mibBuilder.importSymbols("HPN-ICF-OID-MIB", "hpnicfCommon")
InetAddressType, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetAddress")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, iso, Counter32, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "iso", "Counter32", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
hpnicfNetMan = ModuleIdentity((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 90))
hpnicfNetMan.setRevisions(('2008-04-16 17:00',))
if mibBuilder.loadTexts: hpnicfNetMan.setLastUpdated('200804161700Z')
if mibBuilder.loadTexts: hpnicfNetMan.setOrganization('')
hpnicfNMConfigObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 90, 1))
hpnicfNMMonitorObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 90, 2))
hpnicfNMNotify = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 90, 3))
hpnicfNMNotifyScalarObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 90, 3, 1))
hpnicfNMIpAddressType = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 90, 3, 1, 1), InetAddressType()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hpnicfNMIpAddressType.setStatus('current')
hpnicfNMIpAddress = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 90, 3, 1, 2), InetAddress()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hpnicfNMIpAddress.setStatus('current')
hpnicfNMCustomBuildInfo = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 90, 3, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfNMCustomBuildInfo.setStatus('current')
hpnicfNMSerialNum = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 90, 3, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hpnicfNMSerialNum.setStatus('current')
hpnicfNMNotifyObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 90, 3, 2))
hpnicfNMNotifyObjectsPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 90, 3, 2, 0))
hpnicfIpAddrChangeNotify = NotificationType((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 90, 3, 2, 0, 1)).setObjects(("HPN-ICF-NET-MAN-MIB", "hpnicfNMIpAddressType"), ("HPN-ICF-NET-MAN-MIB", "hpnicfNMIpAddress"), ("HPN-ICF-NET-MAN-MIB", "hpnicfNMCustomBuildInfo"), ("HPN-ICF-NET-MAN-MIB", "hpnicfNMSerialNum"))
if mibBuilder.loadTexts: hpnicfIpAddrChangeNotify.setStatus('current')
hpnicfNetManConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 90, 4))
hpnicfNetManCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 90, 4, 1))
hpnicfNetManCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 90, 4, 1, 1)).setObjects(("HPN-ICF-NET-MAN-MIB", "hpnicfNMMonitorGroup"), ("HPN-ICF-NET-MAN-MIB", "hpnicfNMNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpnicfNetManCompliance = hpnicfNetManCompliance.setStatus('current')
hpnicfNetManGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 90, 4, 2))
hpnicfNMMonitorGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 90, 4, 2, 1)).setObjects(("HPN-ICF-NET-MAN-MIB", "hpnicfNMIpAddressType"), ("HPN-ICF-NET-MAN-MIB", "hpnicfNMIpAddress"), ("HPN-ICF-NET-MAN-MIB", "hpnicfNMCustomBuildInfo"), ("HPN-ICF-NET-MAN-MIB", "hpnicfNMSerialNum"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpnicfNMMonitorGroup = hpnicfNMMonitorGroup.setStatus('current')
hpnicfNMNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 90, 4, 2, 2)).setObjects(("HPN-ICF-NET-MAN-MIB", "hpnicfIpAddrChangeNotify"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpnicfNMNotificationGroup = hpnicfNMNotificationGroup.setStatus('current')
mibBuilder.exportSymbols("HPN-ICF-NET-MAN-MIB", hpnicfNMNotificationGroup=hpnicfNMNotificationGroup, hpnicfNetManCompliance=hpnicfNetManCompliance, hpnicfNMNotifyObjectsPrefix=hpnicfNMNotifyObjectsPrefix, hpnicfNMIpAddressType=hpnicfNMIpAddressType, hpnicfNetManCompliances=hpnicfNetManCompliances, hpnicfNMSerialNum=hpnicfNMSerialNum, hpnicfNMNotifyObjects=hpnicfNMNotifyObjects, hpnicfNetMan=hpnicfNetMan, hpnicfNMMonitorGroup=hpnicfNMMonitorGroup, hpnicfIpAddrChangeNotify=hpnicfIpAddrChangeNotify, hpnicfNMCustomBuildInfo=hpnicfNMCustomBuildInfo, hpnicfNMMonitorObjects=hpnicfNMMonitorObjects, hpnicfNMConfigObjects=hpnicfNMConfigObjects, hpnicfNetManGroups=hpnicfNetManGroups, PYSNMP_MODULE_ID=hpnicfNetMan, hpnicfNMIpAddress=hpnicfNMIpAddress, hpnicfNMNotify=hpnicfNMNotify, hpnicfNetManConformance=hpnicfNetManConformance, hpnicfNMNotifyScalarObjects=hpnicfNMNotifyScalarObjects)
