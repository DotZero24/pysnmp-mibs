#
# PySNMP MIB module MITEL-TRAPGROUP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/mitel/MITEL-TRAPGROUP-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 11:04:58 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, enterprises, NotificationType, Integer32, Bits, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "enterprises", "NotificationType", "Integer32", "Bits", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
mitelRouterSnmpTrapGroup = ModuleIdentity((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 7))
mitelRouterSnmpTrapGroup.setRevisions(('2003-03-24 10:50', '2002-04-02 00:00',))
if mibBuilder.loadTexts: mitelRouterSnmpTrapGroup.setLastUpdated('200303241050Z')
if mibBuilder.loadTexts: mitelRouterSnmpTrapGroup.setOrganization('MITEL Networks Corporation')
mitel = MibIdentifier((1, 3, 6, 1, 4, 1, 1027))
mitelProprietary = MibIdentifier((1, 3, 6, 1, 4, 1, 1027, 4))
mitelPropIpNetworking = MibIdentifier((1, 3, 6, 1, 4, 1, 1027, 4, 8))
mitelIpNetRouter = MibIdentifier((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1))
mitelSnmpTrapGlobal = MibScalar((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 7, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mitelSnmpTrapGlobal.setStatus('current')
mitelSnmpTrapControl = MibScalar((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 7, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mitelSnmpTrapControl.setStatus('current')
mibBuilder.exportSymbols("MITEL-TRAPGROUP-MIB", mitelIpNetRouter=mitelIpNetRouter, mitelProprietary=mitelProprietary, mitel=mitel, mitelSnmpTrapGlobal=mitelSnmpTrapGlobal, PYSNMP_MODULE_ID=mitelRouterSnmpTrapGroup, mitelPropIpNetworking=mitelPropIpNetworking, mitelRouterSnmpTrapGroup=mitelRouterSnmpTrapGroup, mitelSnmpTrapControl=mitelSnmpTrapControl)
