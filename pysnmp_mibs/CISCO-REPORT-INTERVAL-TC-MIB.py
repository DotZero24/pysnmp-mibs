#
# PySNMP MIB module CISCO-REPORT-INTERVAL-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/cisco/CISCO-REPORT-INTERVAL-TC-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:32:40 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoReportIntervalTcMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 670))
ciscoReportIntervalTcMIB.setRevisions(('2008-08-22 00:00',))
if mibBuilder.loadTexts: ciscoReportIntervalTcMIB.setLastUpdated('200808220000Z')
if mibBuilder.loadTexts: ciscoReportIntervalTcMIB.setOrganization('Cisco Systems, Inc.')
class ReportCurrentCount(TextualConvention, Gauge32):
    status = 'current'
    displayHint = 'd'

class ReportIntervalCount(TextualConvention, Gauge32):
    status = 'current'
    displayHint = 'd'

mibBuilder.exportSymbols("CISCO-REPORT-INTERVAL-TC-MIB", PYSNMP_MODULE_ID=ciscoReportIntervalTcMIB, ReportCurrentCount=ReportCurrentCount, ciscoReportIntervalTcMIB=ciscoReportIntervalTcMIB, ReportIntervalCount=ReportIntervalCount)
