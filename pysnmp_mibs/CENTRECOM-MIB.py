#
# PySNMP MIB module CENTRECOM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/allied-old/CENTRECOM-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:41:16 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
sysUpTime, sysDescr = mibBuilder.importSymbols("SNMPv2-MIB", "sysUpTime", "sysDescr")
ModuleIdentity, NotificationType, Counter64, enterprises, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "NotificationType", "Counter64", "enterprises", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
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
mibBuilder.exportSymbols("CENTRECOM-MIB", centreCom=centreCom, extSwitchMIB=extSwitchMIB, centrecom8500sx=centrecom8500sx, ati=ati, atkkSwitchMIB=atkkSwitchMIB, products=products, mibObjects=mibObjects, centrecom8500lx=centrecom8500lx, centrecom9100sx=centrecom9100sx, centrecom9100lx=centrecom9100lx)
