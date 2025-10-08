#
# PySNMP MIB module ELTEX-TRAPS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/eltex/ELTEX-TRAPS-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:04:37 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
elt, = mibBuilder.importSymbols("ELTEX-MIB", "elt")
rldot1dStpTrapVrblifIndex, rldot1dStpTrapVrblVID = mibBuilder.importSymbols("RADLAN-BRIDGEMIBOBJECTS-MIB", "rldot1dStpTrapVrblifIndex", "rldot1dStpTrapVrblVID")
rndErrorDesc, rndErrorSeverity = mibBuilder.importSymbols("RADLAN-DEVICEPARAMS-MIB", "rndErrorDesc", "rndErrorSeverity")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, iso, Counter32, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "iso", "Counter32", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
eltNotifications = ModuleIdentity((1, 3, 6, 1, 4, 1, 35265, 0))
eltNotifications.setRevisions(('2012-07-13 00:00',))
if mibBuilder.loadTexts: eltNotifications.setLastUpdated('201207130000Z')
if mibBuilder.loadTexts: eltNotifications.setOrganization('Eltex Enterprise Co, Ltd.')
i2cBusFailure = NotificationType((1, 3, 6, 1, 4, 1, 35265, 0, 3)).setObjects(("RADLAN-DEVICEPARAMS-MIB", "rndErrorDesc"), ("RADLAN-DEVICEPARAMS-MIB", "rndErrorSeverity"))
if mibBuilder.loadTexts: i2cBusFailure.setStatus('current')
i2cBusOperational = NotificationType((1, 3, 6, 1, 4, 1, 35265, 0, 4)).setObjects(("RADLAN-DEVICEPARAMS-MIB", "rndErrorDesc"), ("RADLAN-DEVICEPARAMS-MIB", "rndErrorSeverity"))
if mibBuilder.loadTexts: i2cBusOperational.setStatus('current')
mibBuilder.exportSymbols("ELTEX-TRAPS-MIB", eltNotifications=eltNotifications, i2cBusOperational=i2cBusOperational, PYSNMP_MODULE_ID=eltNotifications, i2cBusFailure=i2cBusFailure)
