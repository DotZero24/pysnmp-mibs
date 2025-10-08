#
# PySNMP MIB module Accton-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/edgecore/Accton-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:05:30 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, enterprises, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "enterprises", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
accton = MibIdentifier((1, 3, 6, 1, 4, 1, 259))
edgecorenetworks = MibIdentifier((1, 3, 6, 1, 4, 1, 259, 10))
edgeCoreNetworksMgt = MibIdentifier((1, 3, 6, 1, 4, 1, 259, 10, 1))
ecs5510_48sMIB = MibIdentifier((1, 3, 6, 1, 4, 1, 259, 10, 1, 14)).setLabel("ecs5510-48sMIB")
rnd = MibIdentifier((1, 3, 6, 1, 4, 1, 259, 10, 1, 14, 89))
mibBuilder.exportSymbols("Accton-MIB", ecs5510_48sMIB=ecs5510_48sMIB, accton=accton, edgecorenetworks=edgecorenetworks, rnd=rnd, edgeCoreNetworksMgt=edgeCoreNetworksMgt)
