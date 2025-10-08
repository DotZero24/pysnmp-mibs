#
# PySNMP MIB module ZYXEL-ROUTER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/zyxel/ZYXEL-ROUTER-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:38:02 2025
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
zyxelRouter = ModuleIdentity((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 113))
if mibBuilder.loadTexts: zyxelRouter.setLastUpdated('201612140000Z')
if mibBuilder.loadTexts: zyxelRouter.setOrganization('Enterprise Solution ZyXEL')
zyxelRouterNsf = MibIdentifier((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 113, 1))
zyxelRouterNsfSetup = MibIdentifier((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 113, 1, 1))
zyRouterNsfEnable = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 113, 1, 1, 1), EnabledStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyRouterNsfEnable.setStatus('current')
zyRouterNsfTimer = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 113, 1, 1, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyRouterNsfTimer.setStatus('current')
mibBuilder.exportSymbols("ZYXEL-ROUTER-MIB", PYSNMP_MODULE_ID=zyxelRouter, zyxelRouter=zyxelRouter, zyxelRouterNsf=zyxelRouterNsf, zyRouterNsfTimer=zyRouterNsfTimer, zyxelRouterNsfSetup=zyxelRouterNsfSetup, zyRouterNsfEnable=zyRouterNsfEnable)
