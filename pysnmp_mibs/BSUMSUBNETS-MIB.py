#
# PySNMP MIB module BSUMSUBNETS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/aperto/BSUMSUBNETS-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:17:16 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
bsu, = mibBuilder.importSymbols("ANIROOT-MIB", "bsu")
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
aniBsuWirelessPort, = mibBuilder.importSymbols("BSUWIRELESSIF-MIB", "aniBsuWirelessPort")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("BSUMSUBNETS-MIB", aniBsuSubnetConfEntry=aniBsuSubnetConfEntry, aniBsuSubnetConfAddr=aniBsuSubnetConfAddr, aniBsuSubnetConfMask=aniBsuSubnetConfMask, PYSNMP_MODULE_ID=aniBsuMultSubnets, aniBsuSubnetConfTable=aniBsuSubnetConfTable, aniBsuMultSubnets=aniBsuMultSubnets)
