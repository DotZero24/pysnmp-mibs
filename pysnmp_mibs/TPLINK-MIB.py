#
# PySNMP MIB module TPLINK-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/tplink/TPLINK-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:36:32 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, enterprises, ObjectIdentity, Gauge32, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "enterprises", "ObjectIdentity", "Gauge32", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
tplink = MibIdentifier((1, 3, 6, 1, 4, 1, 11863))
switch = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 1))
router = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 2))
wireless = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 3))
adsl = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 4))
l2manageswitch = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 1, 1))
l3manageswitch = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 1, 2))
tplinkProducts = ObjectIdentity((1, 3, 6, 1, 4, 1, 11863, 5))
if mibBuilder.loadTexts: tplinkProducts.setStatus('current')
tplinkMgmt = ObjectIdentity((1, 3, 6, 1, 4, 1, 11863, 6))
if mibBuilder.loadTexts: tplinkMgmt.setStatus('current')
ap = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 10))
eap = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 10, 1))
systemTools = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 10, 1, 2))
mibBuilder.exportSymbols("TPLINK-MIB", tplink=tplink, router=router, eap=eap, systemTools=systemTools, l3manageswitch=l3manageswitch, wireless=wireless, ap=ap, adsl=adsl, switch=switch, tplinkProducts=tplinkProducts, l2manageswitch=l2manageswitch, tplinkMgmt=tplinkMgmt)
