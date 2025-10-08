#
# PySNMP MIB module RUCKUS-HWINFO-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/ruckus/RUCKUS-HWINFO-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:41:36 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ruckusCommonHwInfoModule, = mibBuilder.importSymbols("RUCKUS-ROOT-MIB", "ruckusCommonHwInfoModule")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Unsigned32, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Unsigned32", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
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
mibBuilder.exportSymbols("RUCKUS-HWINFO-MIB", ruckusHwInfoMIB=ruckusHwInfoMIB, ruckusHwInfoSerialNumber=ruckusHwInfoSerialNumber, ruckusHwInfoHWMajorRevision=ruckusHwInfoHWMajorRevision, ruckusHwInfoEvents=ruckusHwInfoEvents, ruckusHwInfoObjects=ruckusHwInfoObjects, ruckusHwInfoTemperature=ruckusHwInfoTemperature, ruckusHwInfoCustomerID=ruckusHwInfoCustomerID, ruckusHwInfo=ruckusHwInfo, PYSNMP_MODULE_ID=ruckusHwInfoMIB, ruckusHwInfoHWMinorRevision=ruckusHwInfoHWMinorRevision, ruckusHwInfoModelNumber=ruckusHwInfoModelNumber)
