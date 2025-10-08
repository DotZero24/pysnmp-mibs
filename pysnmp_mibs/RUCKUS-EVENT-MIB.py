#
# PySNMP MIB module RUCKUS-EVENT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/ruckus/RUCKUS-EVENT-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 11:08:37 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ruckusEvents, = mibBuilder.importSymbols("RUCKUS-ROOT-MIB", "ruckusEvents")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
MacAddress, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "MacAddress", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("RUCKUS-EVENT-MIB", ruckusEventConnectTrap=ruckusEventConnectTrap, ruckusEventSetErrorOID=ruckusEventSetErrorOID, ruckusEventDiassocTrap=ruckusEventDiassocTrap, ruckusEventTraps=ruckusEventTraps, PYSNMP_MODULE_ID=ruckusEventMIB, ruckusEventAssocTrap=ruckusEventAssocTrap, ruckusEventSetErrorTrap=ruckusEventSetErrorTrap, ruckusEventDisconnectTrap=ruckusEventDisconnectTrap, ruckusEventObjects=ruckusEventObjects, ruckusEventMIB=ruckusEventMIB, ruckusEventClientMacAddr=ruckusEventClientMacAddr)
