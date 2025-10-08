#
# PySNMP MIB module CENTRECOM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/allied-old/CENTRECOM-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 11:08:19 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
sysDescr, sysUpTime = mibBuilder.importSymbols("SNMPv2-MIB", "sysDescr", "sysUpTime")
MibIdentifier, enterprises, NotificationType, Bits, Integer32, Unsigned32, NotificationType, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, Counter64, TimeTicks, ModuleIdentity, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "enterprises", "NotificationType", "Bits", "Integer32", "Unsigned32", "NotificationType", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "Counter64", "TimeTicks", "ModuleIdentity", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ati = MibIdentifier((1, 3, 6, 1, 4, 1, 207))
products = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1))
mibObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8))
atkkSwitchMIB = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 12))
extSwitchMIB = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 12, 2))
centreCom = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 4))
centrecom8500sx = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 4, 16))
centrecom8500lx = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 4, 17))
centrecom9100sx = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 4, 18))
centrecom9100lx = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 4, 19))
mibBuilder.exportSymbols("CENTRECOM-MIB", atkkSwitchMIB=atkkSwitchMIB, centrecom8500sx=centrecom8500sx, centrecom9100lx=centrecom9100lx, centrecom8500lx=centrecom8500lx, centreCom=centreCom, ati=ati, centrecom9100sx=centrecom9100sx, extSwitchMIB=extSwitchMIB, products=products, mibObjects=mibObjects)
