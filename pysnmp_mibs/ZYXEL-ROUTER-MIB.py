#
# PySNMP MIB module ZYXEL-ROUTER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/zyxel/ZYXEL-ROUTER-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 11:03:55 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
EnabledStatus, = mibBuilder.importSymbols("P-BRIDGE-MIB", "EnabledStatus")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
esMgmt, = mibBuilder.importSymbols("ZYXEL-ES-SMI", "esMgmt")
zyxelRouter = ModuleIdentity((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 113))
if mibBuilder.loadTexts: zyxelRouter.setLastUpdated('201612140000Z')
if mibBuilder.loadTexts: zyxelRouter.setOrganization('Enterprise Solution ZyXEL')
zyxelRouterNsf = MibIdentifier((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 113, 1))
zyxelRouterNsfSetup = MibIdentifier((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 113, 1, 1))
zyRouterNsfEnable = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 113, 1, 1, 1), EnabledStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyRouterNsfEnable.setStatus('current')
zyRouterNsfTimer = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 113, 1, 1, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyRouterNsfTimer.setStatus('current')
mibBuilder.exportSymbols("ZYXEL-ROUTER-MIB", PYSNMP_MODULE_ID=zyxelRouter, zyxelRouter=zyxelRouter, zyRouterNsfEnable=zyRouterNsfEnable, zyxelRouterNsf=zyxelRouterNsf, zyRouterNsfTimer=zyRouterNsfTimer, zyxelRouterNsfSetup=zyxelRouterNsfSetup)
