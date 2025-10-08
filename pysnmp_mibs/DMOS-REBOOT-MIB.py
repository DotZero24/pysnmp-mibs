#
# PySNMP MIB module DMOS-REBOOT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/datacom/DMOS-REBOOT-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:41:56 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
datacomDevicesMIBs, = mibBuilder.importSymbols("DATACOM-SMI", "datacomDevicesMIBs")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Integer32, Bits, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, Counter64, TimeTicks, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Integer32", "Bits", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "Counter64", "TimeTicks", "Gauge32")
RowStatus, DateAndTime, TextualConvention, TruthValue, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "DateAndTime", "TextualConvention", "TruthValue", "DisplayString")
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
