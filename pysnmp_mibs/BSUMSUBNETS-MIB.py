#
# PySNMP MIB module BSUMSUBNETS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/aperto/BSUMSUBNETS-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:07:54 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
bsu, = mibBuilder.importSymbols("ANIROOT-MIB", "bsu")
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
aniBsuWirelessPort, = mibBuilder.importSymbols("BSUWIRELESSIF-MIB", "aniBsuWirelessPort")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
aniBsuMultSubnets = ModuleIdentity((1, 3, 6, 1, 4, 1, 4325, 3, 6))
if mibBuilder.loadTexts: aniBsuMultSubnets.setLastUpdated('0105091130Z')
if mibBuilder.loadTexts: aniBsuMultSubnets.setOrganization('Aperto Networks')
aniBsuSubnetConfTable = MibTable((1, 3, 6, 1, 4, 1, 4325, 3, 6, 1), )
if mibBuilder.loadTexts: aniBsuSubnetConfTable.setStatus('current')
aniBsuSubnetConfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4325, 3, 6, 1, 1), ).setIndexNames((0, "BSUWIRELESSIF-MIB", "aniBsuWirelessPort"), (0, "BSUMSUBNETS-MIB", "aniBsuSubnetConfAddr"))
if mibBuilder.loadTexts: aniBsuSubnetConfEntry.setStatus('current')
aniBsuSubnetConfAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 4325, 3, 6, 1, 1, 1), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: aniBsuSubnetConfAddr.setStatus('current')
aniBsuSubnetConfMask = MibTableColumn((1, 3, 6, 1, 4, 1, 4325, 3, 6, 1, 1, 2), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: aniBsuSubnetConfMask.setStatus('current')
mibBuilder.exportSymbols("BSUMSUBNETS-MIB", aniBsuSubnetConfTable=aniBsuSubnetConfTable, aniBsuSubnetConfAddr=aniBsuSubnetConfAddr, aniBsuSubnetConfMask=aniBsuSubnetConfMask, aniBsuSubnetConfEntry=aniBsuSubnetConfEntry, aniBsuMultSubnets=aniBsuMultSubnets, PYSNMP_MODULE_ID=aniBsuMultSubnets)
