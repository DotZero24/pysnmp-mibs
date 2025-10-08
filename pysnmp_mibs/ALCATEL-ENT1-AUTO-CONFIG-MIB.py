#
# PySNMP MIB module ALCATEL-ENT1-AUTO-CONFIG-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/alcatel-ent1/ALCATEL-ENT1-AUTO-CONFIG-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:00:04 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
softentIND1AutoConfig, = mibBuilder.importSymbols("ALCATEL-ENT1-BASE", "softentIND1AutoConfig")
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Integer32, Bits, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, Counter64, TimeTicks, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Integer32", "Bits", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "Counter64", "TimeTicks", "Gauge32")
RowStatus, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "DisplayString")
alaAUTOCONFIGMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 83, 1))
alaAUTOCONFIGMIB.setRevisions(('2012-05-04 00:00',))
if mibBuilder.loadTexts: alaAUTOCONFIGMIB.setLastUpdated('201205040000Z')
if mibBuilder.loadTexts: alaAUTOCONFIGMIB.setOrganization('Alcatel-Lucent')
alaAUTOCONFIGMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 83, 1, 0))
alaAUTOCONFIGMIBObjects = ObjectIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 83, 1, 1))
if mibBuilder.loadTexts: alaAUTOCONFIGMIBObjects.setStatus('current')
alaAUTOCONFIGMIBConformance = ObjectIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 83, 1, 2))
if mibBuilder.loadTexts: alaAUTOCONFIGMIBConformance.setStatus('current')
alaAUTOCONFIGMIBGroups = ObjectIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 83, 1, 2, 1))
if mibBuilder.loadTexts: alaAUTOCONFIGMIBGroups.setStatus('current')
alaAUTOCONFIGMIBCompliances = ObjectIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 83, 1, 2, 2))
if mibBuilder.loadTexts: alaAUTOCONFIGMIBCompliances.setStatus('current')
alaAUTOCONFIGGlobal = MibIdentifier((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 83, 1, 1, 1))
alaAutoConfigAbort = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 83, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("yes", 1), ("no", 2))).clone('no')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaAutoConfigAbort.setStatus('current')
alaAUTOCONFIGNotificationObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 83, 1, 1, 2))
alaAutoConfigTrapsObj = MibIdentifier((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 83, 1, 1, 3))
alaAutoConfigTrap = NotificationType((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 83, 1, 0, 1)).setObjects(("ALCATEL-ENT1-AUTO-CONFIG-MIB", "alaAutoConfigAutoFabricEnableTrap"))
if mibBuilder.loadTexts: alaAutoConfigTrap.setStatus('current')
alaAutoConfigAutoFabricEnableTrap = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 83, 1, 1, 3, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("yes", 1), ("no", 2)))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: alaAutoConfigAutoFabricEnableTrap.setStatus('current')
alaAUTOCONFIGMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 83, 1, 2, 2, 1)).setObjects(("ALCATEL-ENT1-AUTO-CONFIG-MIB", "alaAUTOCONFIGNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alaAUTOCONFIGMIBCompliance = alaAUTOCONFIGMIBCompliance.setStatus('current')
alaAUTOCONFIGNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 83, 1, 2, 1, 1)).setObjects(("ALCATEL-ENT1-AUTO-CONFIG-MIB", "alaAutoConfigTrap"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alaAUTOCONFIGNotificationGroup = alaAUTOCONFIGNotificationGroup.setStatus('current')
alaAutoConfigGlobalGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 83, 1, 2, 1, 2)).setObjects(("ALCATEL-ENT1-AUTO-CONFIG-MIB", "alaAutoConfigAbort"), ("ALCATEL-ENT1-AUTO-CONFIG-MIB", "alaAutoConfigAutoFabricEnableTrap"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alaAutoConfigGlobalGroup = alaAutoConfigGlobalGroup.setStatus('current')
mibBuilder.exportSymbols("ALCATEL-ENT1-AUTO-CONFIG-MIB", alaAutoConfigAbort=alaAutoConfigAbort, alaAUTOCONFIGMIBCompliance=alaAUTOCONFIGMIBCompliance, alaAutoConfigGlobalGroup=alaAutoConfigGlobalGroup, alaAUTOCONFIGMIBNotifications=alaAUTOCONFIGMIBNotifications, alaAUTOCONFIGMIB=alaAUTOCONFIGMIB, alaAutoConfigTrap=alaAutoConfigTrap, alaAUTOCONFIGMIBCompliances=alaAUTOCONFIGMIBCompliances, alaAUTOCONFIGGlobal=alaAUTOCONFIGGlobal, alaAutoConfigAutoFabricEnableTrap=alaAutoConfigAutoFabricEnableTrap, alaAUTOCONFIGNotificationObjects=alaAUTOCONFIGNotificationObjects, alaAUTOCONFIGNotificationGroup=alaAUTOCONFIGNotificationGroup, alaAUTOCONFIGMIBObjects=alaAUTOCONFIGMIBObjects, PYSNMP_MODULE_ID=alaAUTOCONFIGMIB, alaAutoConfigTrapsObj=alaAutoConfigTrapsObj, alaAUTOCONFIGMIBConformance=alaAUTOCONFIGMIBConformance, alaAUTOCONFIGMIBGroups=alaAUTOCONFIGMIBGroups)
