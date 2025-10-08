#
# PySNMP MIB module DATACOM-SMI (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/datacom/DATACOM-SMI
# Produced by pysmi-1.1.12 at Wed Oct  8 10:41:58 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, enterprises, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, Counter64, TimeTicks, ModuleIdentity, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "enterprises", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "Counter64", "TimeTicks", "ModuleIdentity", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("DATACOM-SMI", datacomDevicesMIBs=datacomDevicesMIBs, datacomExpAccessDevicesMIBs=datacomExpAccessDevicesMIBs, datacom=datacom, datacomExpProductsMIBs=datacomExpProductsMIBs, datacomExpModemsMIBs=datacomExpModemsMIBs, datacomAccessDevices=datacomAccessDevices, datacomProductsMIBs=datacomProductsMIBs, datacomGenericMIBs=datacomGenericMIBs, datacomManagementCards=datacomManagementCards, datacomModems=datacomModems, datacomModemsMIBs=datacomModemsMIBs, datacomExperimental=datacomExperimental, datacomDevices=datacomDevices, datacomExpGenericMIBs=datacomExpGenericMIBs, datacomAccessDevicesMIBs=datacomAccessDevicesMIBs, datacomModules=datacomModules, datacomRegistrations=datacomRegistrations)
