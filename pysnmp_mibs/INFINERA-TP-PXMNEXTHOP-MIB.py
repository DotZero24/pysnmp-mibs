#
# PySNMP MIB module INFINERA-TP-PXMNEXTHOP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/infinera/INFINERA-TP-PXMNEXTHOP-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:09:33 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
terminationPoint, = mibBuilder.importSymbols("INFINERA-REG-MIB", "terminationPoint")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Unsigned32, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Unsigned32", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
pxmNextHopMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 68))
if mibBuilder.loadTexts: pxmNextHopMIB.setLastUpdated('201605200000Z')
if mibBuilder.loadTexts: pxmNextHopMIB.setOrganization('INFINERA')
pxmNextHopConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 68, 3))
pxmNextHopCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 68, 3, 1))
pxmNextHopGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 68, 3, 2))
pxmNextHopTable = MibTable((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 68, 1), )
if mibBuilder.loadTexts: pxmNextHopTable.setStatus('current')
pxmNextHopEntry = MibTableRow((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 68, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: pxmNextHopEntry.setStatus('current')
pxmNextHopMacAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 68, 1, 1, 1), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pxmNextHopMacAddress.setStatus('current')
pxmNextHopCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 68, 3, 1, 1)).setObjects(("INFINERA-TP-PXMNEXTHOP-MIB", "pxmNextHopGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pxmNextHopCompliance = pxmNextHopCompliance.setStatus('current')
pxmNextHopGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 68, 3, 2, 1)).setObjects(("INFINERA-TP-PXMNEXTHOP-MIB", "pxmNextHopMacAddress"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pxmNextHopGroup = pxmNextHopGroup.setStatus('current')
mibBuilder.exportSymbols("INFINERA-TP-PXMNEXTHOP-MIB", pxmNextHopMIB=pxmNextHopMIB, pxmNextHopConformance=pxmNextHopConformance, pxmNextHopTable=pxmNextHopTable, pxmNextHopGroup=pxmNextHopGroup, pxmNextHopCompliance=pxmNextHopCompliance, pxmNextHopGroups=pxmNextHopGroups, pxmNextHopMacAddress=pxmNextHopMacAddress, pxmNextHopCompliances=pxmNextHopCompliances, pxmNextHopEntry=pxmNextHopEntry, PYSNMP_MODULE_ID=pxmNextHopMIB)
