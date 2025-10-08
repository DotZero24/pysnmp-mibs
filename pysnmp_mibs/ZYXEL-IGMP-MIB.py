#
# PySNMP MIB module ZYXEL-IGMP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/zyxel/ZYXEL-IGMP-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:37:40 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
EnabledStatus, = mibBuilder.importSymbols("P-BRIDGE-MIB", "EnabledStatus")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
esMgmt, = mibBuilder.importSymbols("ZYXEL-ES-SMI", "esMgmt")
zyRouteDomainIpMaskBits, zyRouteDomainIpAddress = mibBuilder.importSymbols("ZYXEL-IP-FORWARD-MIB", "zyRouteDomainIpMaskBits", "zyRouteDomainIpAddress")
zyxelIgmp = ModuleIdentity((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 29))
if mibBuilder.loadTexts: zyxelIgmp.setLastUpdated('201207010000Z')
if mibBuilder.loadTexts: zyxelIgmp.setOrganization('Enterprise Solution ZyXEL')
zyxelIgmpSetup = MibIdentifier((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 29, 1))
zyIgmpState = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 29, 1, 1), EnabledStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyIgmpState.setStatus('current')
zyxelIgmpRouteDomainTable = MibTable((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 29, 1, 2), )
if mibBuilder.loadTexts: zyxelIgmpRouteDomainTable.setStatus('current')
zyxelIgmpRouteDomainEntry = MibTableRow((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 29, 1, 2, 1), ).setIndexNames((0, "ZYXEL-IP-FORWARD-MIB", "zyRouteDomainIpAddress"), (0, "ZYXEL-IP-FORWARD-MIB", "zyRouteDomainIpMaskBits"))
if mibBuilder.loadTexts: zyxelIgmpRouteDomainEntry.setStatus('current')
zyIgmpRouteDomainVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 29, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("none", 0), ("igmpV1", 1), ("igmpV2", 2), ("igmpV3", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyIgmpRouteDomainVersion.setStatus('current')
mibBuilder.exportSymbols("ZYXEL-IGMP-MIB", zyIgmpState=zyIgmpState, zyxelIgmpRouteDomainEntry=zyxelIgmpRouteDomainEntry, zyxelIgmp=zyxelIgmp, zyxelIgmpRouteDomainTable=zyxelIgmpRouteDomainTable, PYSNMP_MODULE_ID=zyxelIgmp, zyxelIgmpSetup=zyxelIgmpSetup, zyIgmpRouteDomainVersion=zyIgmpRouteDomainVersion)
