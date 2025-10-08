#
# PySNMP MIB module OPTIX-GLOBAL-PER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/huawei/OPTIX-GLOBAL-PER-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:03:35 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
PerformanceEventType, ValidflagType, MOD2Type = mibBuilder.importSymbols("OPTIX-GLOBAL-TC-MIB", "PerformanceEventType", "ValidflagType", "MOD2Type")
optixCommonGlobal, = mibBuilder.importSymbols("OPTIX-OID-MIB", "optixCommonGlobal")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Integer32, Bits, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Integer32", "Bits", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
DateAndTime, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "DateAndTime", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("OPTIX-GLOBAL-PER-MIB", perMonitorTime=perMonitorTime, per24hMonitorStartTime=per24hMonitorStartTime, optixGlobalPER=optixGlobalPER, per24hMonitorEndTime=per24hMonitorEndTime, PYSNMP_MODULE_ID=optixGlobalPER, per15mMonitorTime=per15mMonitorTime, per15mMonitorEndTime=per15mMonitorEndTime, per24hMonitorTime=per24hMonitorTime, per15mMonitorStartTime=per15mMonitorStartTime)
