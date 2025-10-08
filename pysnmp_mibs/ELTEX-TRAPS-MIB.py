#
# PySNMP MIB module ELTEX-TRAPS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/eltex/ELTEX-TRAPS-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:11:52 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
elt, = mibBuilder.importSymbols("ELTEX-MIB", "elt")
rldot1dStpTrapVrblifIndex, rldot1dStpTrapVrblVID = mibBuilder.importSymbols("RADLAN-BRIDGEMIBOBJECTS-MIB", "rldot1dStpTrapVrblifIndex", "rldot1dStpTrapVrblVID")
rndErrorSeverity, rndErrorDesc = mibBuilder.importSymbols("RADLAN-DEVICEPARAMS-MIB", "rndErrorSeverity", "rndErrorDesc")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, Counter64, TimeTicks, ModuleIdentity, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "Counter64", "TimeTicks", "ModuleIdentity", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
eltNotifications = ModuleIdentity((1, 3, 6, 1, 4, 1, 35265, 0))
eltNotifications.setRevisions(('2012-07-13 00:00',))
if mibBuilder.loadTexts: eltNotifications.setLastUpdated('201207130000Z')
if mibBuilder.loadTexts: eltNotifications.setOrganization('Eltex Enterprise Co, Ltd.')
i2cBusFailure = NotificationType((1, 3, 6, 1, 4, 1, 35265, 0, 3)).setObjects(("RADLAN-DEVICEPARAMS-MIB", "rndErrorDesc"), ("RADLAN-DEVICEPARAMS-MIB", "rndErrorSeverity"))
if mibBuilder.loadTexts: i2cBusFailure.setStatus('current')
i2cBusOperational = NotificationType((1, 3, 6, 1, 4, 1, 35265, 0, 4)).setObjects(("RADLAN-DEVICEPARAMS-MIB", "rndErrorDesc"), ("RADLAN-DEVICEPARAMS-MIB", "rndErrorSeverity"))
if mibBuilder.loadTexts: i2cBusOperational.setStatus('current')
mibBuilder.exportSymbols("ELTEX-TRAPS-MIB", i2cBusFailure=i2cBusFailure, i2cBusOperational=i2cBusOperational, eltNotifications=eltNotifications, PYSNMP_MODULE_ID=eltNotifications)
