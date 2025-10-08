#
# PySNMP MIB module RUCKUS-EVENT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/ruckus/RUCKUS-EVENT-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:41:34 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ruckusEvents, = mibBuilder.importSymbols("RUCKUS-ROOT-MIB", "ruckusEvents")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Unsigned32, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Unsigned32", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, MacAddress, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "MacAddress", "TextualConvention")
ruckusEventMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 25053, 2, 1))
if mibBuilder.loadTexts: ruckusEventMIB.setLastUpdated('201010150000Z')
if mibBuilder.loadTexts: ruckusEventMIB.setOrganization('Ruckus Wireless, Inc.')
ruckusEventTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 2, 1, 1))
ruckusEventObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 2, 1, 2))
ruckusEventAssocTrap = NotificationType((1, 3, 6, 1, 4, 1, 25053, 2, 1, 1, 1)).setObjects(("RUCKUS-EVENT-MIB", "ruckusEventClientMacAddr"))
if mibBuilder.loadTexts: ruckusEventAssocTrap.setStatus('current')
ruckusEventDiassocTrap = NotificationType((1, 3, 6, 1, 4, 1, 25053, 2, 1, 1, 2)).setObjects(("RUCKUS-EVENT-MIB", "ruckusEventClientMacAddr"))
if mibBuilder.loadTexts: ruckusEventDiassocTrap.setStatus('current')
ruckusEventSetErrorTrap = NotificationType((1, 3, 6, 1, 4, 1, 25053, 2, 1, 1, 3)).setObjects(("RUCKUS-EVENT-MIB", "ruckusEventSetErrorOID"))
if mibBuilder.loadTexts: ruckusEventSetErrorTrap.setStatus('current')
ruckusEventConnectTrap = NotificationType((1, 3, 6, 1, 4, 1, 25053, 2, 1, 1, 25)).setObjects(("RUCKUS-EVENT-MIB", "ruckusEventClientMacAddr"))
if mibBuilder.loadTexts: ruckusEventConnectTrap.setStatus('current')
ruckusEventDisconnectTrap = NotificationType((1, 3, 6, 1, 4, 1, 25053, 2, 1, 1, 26)).setObjects(("RUCKUS-EVENT-MIB", "ruckusEventClientMacAddr"))
if mibBuilder.loadTexts: ruckusEventDisconnectTrap.setStatus('current')
ruckusEventClientMacAddr = MibScalar((1, 3, 6, 1, 4, 1, 25053, 2, 1, 2, 15), OctetString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: ruckusEventClientMacAddr.setStatus('current')
ruckusEventSetErrorOID = MibScalar((1, 3, 6, 1, 4, 1, 25053, 2, 1, 2, 20), ObjectIdentifier()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: ruckusEventSetErrorOID.setStatus('current')
mibBuilder.exportSymbols("RUCKUS-EVENT-MIB", ruckusEventDiassocTrap=ruckusEventDiassocTrap, PYSNMP_MODULE_ID=ruckusEventMIB, ruckusEventMIB=ruckusEventMIB, ruckusEventObjects=ruckusEventObjects, ruckusEventClientMacAddr=ruckusEventClientMacAddr, ruckusEventConnectTrap=ruckusEventConnectTrap, ruckusEventSetErrorOID=ruckusEventSetErrorOID, ruckusEventSetErrorTrap=ruckusEventSetErrorTrap, ruckusEventDisconnectTrap=ruckusEventDisconnectTrap, ruckusEventAssocTrap=ruckusEventAssocTrap, ruckusEventTraps=ruckusEventTraps)
