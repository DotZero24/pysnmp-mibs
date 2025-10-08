#
# PySNMP MIB module INFINERA-TP-PXMNEXTHOP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/infinera/INFINERA-TP-PXMNEXTHOP-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:20:37 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
terminationPoint, = mibBuilder.importSymbols("INFINERA-REG-MIB", "terminationPoint")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("INFINERA-TP-PXMNEXTHOP-MIB", pxmNextHopGroups=pxmNextHopGroups, pxmNextHopCompliances=pxmNextHopCompliances, pxmNextHopTable=pxmNextHopTable, PYSNMP_MODULE_ID=pxmNextHopMIB, pxmNextHopMacAddress=pxmNextHopMacAddress, pxmNextHopGroup=pxmNextHopGroup, pxmNextHopMIB=pxmNextHopMIB, pxmNextHopConformance=pxmNextHopConformance, pxmNextHopEntry=pxmNextHopEntry, pxmNextHopCompliance=pxmNextHopCompliance)
