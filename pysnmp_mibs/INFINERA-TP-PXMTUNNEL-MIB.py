#
# PySNMP MIB module INFINERA-TP-PXMTUNNEL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/infinera/INFINERA-TP-PXMTUNNEL-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:09:34 2025
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
mibBuilder.exportSymbols("INFINERA-TP-PXMTUNNEL-MIB", pxmTunnelCompliance=pxmTunnelCompliance, pxmTunnelMTUSize=pxmTunnelMTUSize, pxmTunnelId=pxmTunnelId, pxmTunnelTable=pxmTunnelTable, pxmTunnelEntry=pxmTunnelEntry, pxmTunnelGroups=pxmTunnelGroups, pxmTunnelMIB=pxmTunnelMIB, pxmTunnelCompliances=pxmTunnelCompliances, pxmTunnelAssociatedLSPList=pxmTunnelAssociatedLSPList, pxmTunnelSupportingEqptAid=pxmTunnelSupportingEqptAid, pxmTunnelConformance=pxmTunnelConformance, PYSNMP_MODULE_ID=pxmTunnelMIB, pxmTunnelGroup=pxmTunnelGroup, pxmTunnelNum=pxmTunnelNum)
