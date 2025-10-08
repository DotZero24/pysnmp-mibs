#
# PySNMP MIB module TPLINK-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/tplink/TPLINK-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 11:01:57 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, enterprises, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, Counter64, TimeTicks, ModuleIdentity, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "enterprises", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "Counter64", "TimeTicks", "ModuleIdentity", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("TPLINK-MIB", switch=switch, tplink=tplink, router=router, systemTools=systemTools, adsl=adsl, l3manageswitch=l3manageswitch, l2manageswitch=l2manageswitch, tplinkProducts=tplinkProducts, tplinkMgmt=tplinkMgmt, ap=ap, eap=eap, wireless=wireless)
