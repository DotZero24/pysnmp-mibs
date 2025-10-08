#
# PySNMP MIB module OPTIX-GLOBAL-PER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/huawei/OPTIX-GLOBAL-PER-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 09:59:43 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
PerformanceEventType, ValidflagType, MOD2Type = mibBuilder.importSymbols("OPTIX-GLOBAL-TC-MIB", "PerformanceEventType", "ValidflagType", "MOD2Type")
optixCommonGlobal, = mibBuilder.importSymbols("OPTIX-OID-MIB", "optixCommonGlobal")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Unsigned32, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Unsigned32", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, DateAndTime, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "DateAndTime", "TextualConvention")
optixGlobalPER = ModuleIdentity((1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 20))
optixGlobalPER.setRevisions(('2008-05-24 00:00',))
if mibBuilder.loadTexts: optixGlobalPER.setLastUpdated('200805240000Z')
if mibBuilder.loadTexts: optixGlobalPER.setOrganization('Huawei Technologies co.,Ltd.')
perMonitorTime = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 20, 10))
per15mMonitorTime = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 20, 10, 10))
per15mMonitorStartTime = MibScalar((1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 20, 10, 10, 10), DateAndTime()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: per15mMonitorStartTime.setStatus('current')
per15mMonitorEndTime = MibScalar((1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 20, 10, 10, 20), DateAndTime()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: per15mMonitorEndTime.setStatus('current')
per24hMonitorTime = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 20, 10, 20))
per24hMonitorStartTime = MibScalar((1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 20, 10, 20, 10), DateAndTime()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: per24hMonitorStartTime.setStatus('current')
per24hMonitorEndTime = MibScalar((1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40, 20, 10, 20, 20), DateAndTime()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: per24hMonitorEndTime.setStatus('current')
mibBuilder.exportSymbols("OPTIX-GLOBAL-PER-MIB", PYSNMP_MODULE_ID=optixGlobalPER, per15mMonitorTime=per15mMonitorTime, per15mMonitorStartTime=per15mMonitorStartTime, per24hMonitorTime=per24hMonitorTime, per24hMonitorStartTime=per24hMonitorStartTime, perMonitorTime=perMonitorTime, per24hMonitorEndTime=per24hMonitorEndTime, optixGlobalPER=optixGlobalPER, per15mMonitorEndTime=per15mMonitorEndTime)
