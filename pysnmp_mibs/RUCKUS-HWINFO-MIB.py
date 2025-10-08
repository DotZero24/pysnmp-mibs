#
# PySNMP MIB module RUCKUS-HWINFO-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/ruckus/RUCKUS-HWINFO-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 11:08:39 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ruckusCommonHwInfoModule, = mibBuilder.importSymbols("RUCKUS-ROOT-MIB", "ruckusCommonHwInfoModule")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ruckusHwInfoMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 25053, 1, 1, 2, 1))
if mibBuilder.loadTexts: ruckusHwInfoMIB.setLastUpdated('201010150800Z')
if mibBuilder.loadTexts: ruckusHwInfoMIB.setOrganization('Ruckus Wireless, Inc.')
ruckusHwInfoObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 1, 1, 2, 1, 1))
ruckusHwInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 1, 1, 2, 1, 1, 1))
ruckusHwInfoEvents = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 1, 1, 2, 1, 2))
ruckusHwInfoModelNumber = MibScalar((1, 3, 6, 1, 4, 1, 25053, 1, 1, 2, 1, 1, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ruckusHwInfoModelNumber.setStatus('current')
ruckusHwInfoSerialNumber = MibScalar((1, 3, 6, 1, 4, 1, 25053, 1, 1, 2, 1, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ruckusHwInfoSerialNumber.setStatus('current')
ruckusHwInfoCustomerID = MibScalar((1, 3, 6, 1, 4, 1, 25053, 1, 1, 2, 1, 1, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ruckusHwInfoCustomerID.setStatus('current')
ruckusHwInfoHWMajorRevision = MibScalar((1, 3, 6, 1, 4, 1, 25053, 1, 1, 2, 1, 1, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ruckusHwInfoHWMajorRevision.setStatus('current')
ruckusHwInfoHWMinorRevision = MibScalar((1, 3, 6, 1, 4, 1, 25053, 1, 1, 2, 1, 1, 1, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ruckusHwInfoHWMinorRevision.setStatus('current')
ruckusHwInfoTemperature = MibScalar((1, 3, 6, 1, 4, 1, 25053, 1, 1, 2, 1, 1, 1, 10), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ruckusHwInfoTemperature.setStatus('current')
mibBuilder.exportSymbols("RUCKUS-HWINFO-MIB", ruckusHwInfoHWMinorRevision=ruckusHwInfoHWMinorRevision, ruckusHwInfoModelNumber=ruckusHwInfoModelNumber, ruckusHwInfoObjects=ruckusHwInfoObjects, ruckusHwInfo=ruckusHwInfo, PYSNMP_MODULE_ID=ruckusHwInfoMIB, ruckusHwInfoCustomerID=ruckusHwInfoCustomerID, ruckusHwInfoEvents=ruckusHwInfoEvents, ruckusHwInfoSerialNumber=ruckusHwInfoSerialNumber, ruckusHwInfoHWMajorRevision=ruckusHwInfoHWMajorRevision, ruckusHwInfoTemperature=ruckusHwInfoTemperature, ruckusHwInfoMIB=ruckusHwInfoMIB)
