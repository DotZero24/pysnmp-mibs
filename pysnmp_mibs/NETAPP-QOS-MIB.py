#
# PySNMP MIB module NETAPP-QOS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/netapp/NETAPP-QOS-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 09:57:33 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
fastPath, = mibBuilder.importSymbols("NETAPP-REF-MIB", "fastPath")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, iso, Counter32, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "iso", "Counter32", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention")
fastPathQOS = ModuleIdentity((1, 3, 6, 1, 4, 1, 789, 4413, 1, 1, 3))
fastPathQOS.setRevisions(('2011-01-26 00:00', '2007-05-23 00:00', '2003-11-21 00:00', '2002-01-30 15:44',))
if mibBuilder.loadTexts: fastPathQOS.setLastUpdated('201101260000Z')
if mibBuilder.loadTexts: fastPathQOS.setOrganization('Broadcom Corporation')
mibBuilder.exportSymbols("NETAPP-QOS-MIB", PYSNMP_MODULE_ID=fastPathQOS, fastPathQOS=fastPathQOS)
