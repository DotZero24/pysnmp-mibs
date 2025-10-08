#
# PySNMP MIB module DATACOM-SMI (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/datacom/DATACOM-SMI
# Produced by pysmi-1.1.12 at Thu Sep 11 10:22:43 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, enterprises, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "enterprises", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
datacom = MibIdentifier((1, 3, 6, 1, 4, 1, 3709))
datacomRegistrations = MibIdentifier((1, 3, 6, 1, 4, 1, 3709, 1))
datacomGenericMIBs = MibIdentifier((1, 3, 6, 1, 4, 1, 3709, 2))
datacomProductsMIBs = MibIdentifier((1, 3, 6, 1, 4, 1, 3709, 3))
datacomExperimental = MibIdentifier((1, 3, 6, 1, 4, 1, 3709, 4))
datacomModules = MibIdentifier((1, 3, 6, 1, 4, 1, 3709, 1, 1))
datacomManagementCards = MibIdentifier((1, 3, 6, 1, 4, 1, 3709, 1, 2))
datacomModems = MibIdentifier((1, 3, 6, 1, 4, 1, 3709, 1, 3))
datacomAccessDevices = MibIdentifier((1, 3, 6, 1, 4, 1, 3709, 1, 5))
datacomDevices = MibIdentifier((1, 3, 6, 1, 4, 1, 3709, 1, 6))
datacomModemsMIBs = MibIdentifier((1, 3, 6, 1, 4, 1, 3709, 3, 3))
datacomAccessDevicesMIBs = MibIdentifier((1, 3, 6, 1, 4, 1, 3709, 3, 5))
datacomDevicesMIBs = MibIdentifier((1, 3, 6, 1, 4, 1, 3709, 3, 6))
datacomExpGenericMIBs = MibIdentifier((1, 3, 6, 1, 4, 1, 3709, 4, 2))
datacomExpProductsMIBs = MibIdentifier((1, 3, 6, 1, 4, 1, 3709, 4, 3))
datacomExpModemsMIBs = MibIdentifier((1, 3, 6, 1, 4, 1, 3709, 4, 3, 3))
datacomExpAccessDevicesMIBs = MibIdentifier((1, 3, 6, 1, 4, 1, 3709, 4, 3, 5))
mibBuilder.exportSymbols("DATACOM-SMI", datacomModules=datacomModules, datacomExpModemsMIBs=datacomExpModemsMIBs, datacomManagementCards=datacomManagementCards, datacomModems=datacomModems, datacomAccessDevices=datacomAccessDevices, datacomExperimental=datacomExperimental, datacomModemsMIBs=datacomModemsMIBs, datacomRegistrations=datacomRegistrations, datacomProductsMIBs=datacomProductsMIBs, datacomExpProductsMIBs=datacomExpProductsMIBs, datacom=datacom, datacomDevices=datacomDevices, datacomExpGenericMIBs=datacomExpGenericMIBs, datacomGenericMIBs=datacomGenericMIBs, datacomAccessDevicesMIBs=datacomAccessDevicesMIBs, datacomExpAccessDevicesMIBs=datacomExpAccessDevicesMIBs, datacomDevicesMIBs=datacomDevicesMIBs)
