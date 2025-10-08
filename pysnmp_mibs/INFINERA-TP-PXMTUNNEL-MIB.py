#
# PySNMP MIB module INFINERA-TP-PXMTUNNEL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/infinera/INFINERA-TP-PXMTUNNEL-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:20:40 2025
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
pxmTunnelMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 69))
if mibBuilder.loadTexts: pxmTunnelMIB.setLastUpdated('201605200000Z')
if mibBuilder.loadTexts: pxmTunnelMIB.setOrganization('INFINERA')
pxmTunnelConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 69, 3))
pxmTunnelCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 69, 3, 1))
pxmTunnelGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 69, 3, 2))
pxmTunnelTable = MibTable((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 69, 1), )
if mibBuilder.loadTexts: pxmTunnelTable.setStatus('current')
pxmTunnelEntry = MibTableRow((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 69, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: pxmTunnelEntry.setStatus('current')
pxmTunnelMTUSize = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 69, 1, 1, 1), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pxmTunnelMTUSize.setStatus('current')
pxmTunnelNum = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 69, 1, 1, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pxmTunnelNum.setStatus('current')
pxmTunnelId = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 69, 1, 1, 3), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pxmTunnelId.setStatus('current')
pxmTunnelSupportingEqptAid = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 69, 1, 1, 4), DisplayString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pxmTunnelSupportingEqptAid.setStatus('current')
pxmTunnelAssociatedLSPList = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 69, 1, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pxmTunnelAssociatedLSPList.setStatus('current')
pxmTunnelCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 69, 3, 1, 1)).setObjects(("INFINERA-TP-PXMTUNNEL-MIB", "pxmTunnelGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pxmTunnelCompliance = pxmTunnelCompliance.setStatus('current')
pxmTunnelGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 69, 3, 2, 1)).setObjects(("INFINERA-TP-PXMTUNNEL-MIB", "pxmTunnelMTUSize"), ("INFINERA-TP-PXMTUNNEL-MIB", "pxmTunnelNum"), ("INFINERA-TP-PXMTUNNEL-MIB", "pxmTunnelId"), ("INFINERA-TP-PXMTUNNEL-MIB", "pxmTunnelSupportingEqptAid"), ("INFINERA-TP-PXMTUNNEL-MIB", "pxmTunnelAssociatedLSPList"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pxmTunnelGroup = pxmTunnelGroup.setStatus('current')
mibBuilder.exportSymbols("INFINERA-TP-PXMTUNNEL-MIB", pxmTunnelCompliance=pxmTunnelCompliance, pxmTunnelTable=pxmTunnelTable, pxmTunnelEntry=pxmTunnelEntry, pxmTunnelNum=pxmTunnelNum, pxmTunnelGroup=pxmTunnelGroup, pxmTunnelMIB=pxmTunnelMIB, pxmTunnelConformance=pxmTunnelConformance, pxmTunnelGroups=pxmTunnelGroups, PYSNMP_MODULE_ID=pxmTunnelMIB, pxmTunnelSupportingEqptAid=pxmTunnelSupportingEqptAid, pxmTunnelAssociatedLSPList=pxmTunnelAssociatedLSPList, pxmTunnelCompliances=pxmTunnelCompliances, pxmTunnelId=pxmTunnelId, pxmTunnelMTUSize=pxmTunnelMTUSize)
