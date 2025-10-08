#
# PySNMP MIB module DMOS-REBOOT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/datacom/DMOS-REBOOT-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:22:41 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
datacomDevicesMIBs, = mibBuilder.importSymbols("DATACOM-SMI", "datacomDevicesMIBs")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Unsigned32, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Unsigned32", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, RowStatus, DateAndTime, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "DateAndTime", "TruthValue", "TextualConvention")
dmosRebootMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 3709, 3, 6, 10))
dmosRebootMIB.setRevisions(('2019-10-17 00:00',))
if mibBuilder.loadTexts: dmosRebootMIB.setLastUpdated('201910170000Z')
if mibBuilder.loadTexts: dmosRebootMIB.setOrganization('DATACOM')
class String(TextualConvention, OctetString):
    status = 'current'
    displayHint = '1t'

rebootReason = MibScalar((1, 3, 6, 1, 4, 1, 3709, 3, 6, 10, 1), String()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rebootReason.setStatus('current')
mibBuilder.exportSymbols("DMOS-REBOOT-MIB", String=String, PYSNMP_MODULE_ID=dmosRebootMIB, dmosRebootMIB=dmosRebootMIB, rebootReason=rebootReason)
