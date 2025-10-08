#
# PySNMP MIB module CISCO-REPORT-INTERVAL-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/cisco/CISCO-REPORT-INTERVAL-TC-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:16:32 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
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

mibBuilder.exportSymbols("CISCO-REPORT-INTERVAL-TC-MIB", ReportCurrentCount=ReportCurrentCount, ciscoReportIntervalTcMIB=ciscoReportIntervalTcMIB, ReportIntervalCount=ReportIntervalCount, PYSNMP_MODULE_ID=ciscoReportIntervalTcMIB)
