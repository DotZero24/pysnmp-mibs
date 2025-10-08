#
# PySNMP MIB module DLB-GENERIC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/deliberant/DLB-GENERIC-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 11:01:05 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
dlbMgmt, = mibBuilder.importSymbols("DELIBERANT-MIB", "dlbMgmt")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
sysLocation, = mibBuilder.importSymbols("SNMPv2-MIB", "sysLocation")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
dlbGenericMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 32761, 3, 1))
dlbGenericMIB.setRevisions(('2009-02-13 00:00',))
if mibBuilder.loadTexts: dlbGenericMIB.setLastUpdated('200902130000Z')
if mibBuilder.loadTexts: dlbGenericMIB.setOrganization('Deliberant')
dlbGenericMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 32761, 3, 1, 1))
dlbGenericNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 32761, 3, 1, 1, 0))
dlbGenericInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 32761, 3, 1, 1, 1))
dlbPowerLoss = NotificationType((1, 3, 6, 1, 4, 1, 32761, 3, 1, 1, 0, 1)).setObjects(("SNMPv2-MIB", "sysLocation"))
if mibBuilder.loadTexts: dlbPowerLoss.setStatus('current')
dlbAdministrativeReboot = NotificationType((1, 3, 6, 1, 4, 1, 32761, 3, 1, 1, 0, 2)).setObjects(("SNMPv2-MIB", "sysLocation"))
if mibBuilder.loadTexts: dlbAdministrativeReboot.setStatus('current')
mibBuilder.exportSymbols("DLB-GENERIC-MIB", dlbPowerLoss=dlbPowerLoss, dlbGenericMIB=dlbGenericMIB, dlbGenericInfo=dlbGenericInfo, PYSNMP_MODULE_ID=dlbGenericMIB, dlbAdministrativeReboot=dlbAdministrativeReboot, dlbGenericNotifs=dlbGenericNotifs, dlbGenericMIBObjects=dlbGenericMIBObjects)
