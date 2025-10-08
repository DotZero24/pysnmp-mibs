#
# PySNMP MIB module LEFTHAND-NETWORKS-NSM-STATUS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/hp/LEFTHAND-NETWORKS-NSM-STATUS-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:02:56 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
lhnNsm, lhnModules = mibBuilder.importSymbols("LEFTHAND-NETWORKS-GLOBAL-REG-MIB", "lhnNsm", "lhnModules")
lhnNsmStatus, = mibBuilder.importSymbols("LEFTHAND-NETWORKS-NSM-MIB", "lhnNsmStatus")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
lhnNsmStatusModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 9804, 2, 1, 99))
lhnNsmStatusModule.setRevisions(('2013-11-21 00:00', '2013-06-25 00:00', '2012-09-04 00:00', '2011-06-21 00:00', '2010-09-07 00:00', '2010-07-19 00:00', '2009-11-20 00:00', '2009-03-10 00:00', '2008-01-24 00:00',))
if mibBuilder.loadTexts: lhnNsmStatusModule.setLastUpdated('201311210000Z')
if mibBuilder.loadTexts: lhnNsmStatusModule.setOrganization('Hewlett Packard Company, StorageWorks Division')
lhnNsmStatusModuleConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9804, 2, 1, 99, 1))
lhnNsmStatusModuleCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9804, 2, 1, 99, 1, 1))
lhnNsmStatusModuleGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9804, 2, 1, 99, 1, 2))
lefthandNetworksNsmStatusMibCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9804, 2, 1, 99, 1, 1, 1)).setObjects(("LEFTHAND-NETWORKS-NSM-STATUS-MIB", "lefthandNetworksNsmStatusGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    lefthandNetworksNsmStatusMibCompliance = lefthandNetworksNsmStatusMibCompliance.setStatus('current')
lefthandNetworksNsmStatusGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9804, 2, 1, 99, 1, 2, 1)).setObjects(("LEFTHAND-NETWORKS-NSM-STATUS-MIB", "status"), ("LEFTHAND-NETWORKS-NSM-STATUS-MIB", "statusMessage"), ("LEFTHAND-NETWORKS-NSM-STATUS-MIB", "statusSNMPD"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    lefthandNetworksNsmStatusGroup = lefthandNetworksNsmStatusGroup.setStatus('current')
status = MibScalar((1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 99, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("online", 1), ("offline", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: status.setStatus('current')
statusMessage = MibScalar((1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 99, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: statusMessage.setStatus('current')
statusSNMPD = MibScalar((1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 99, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: statusSNMPD.setStatus('current')
mibBuilder.exportSymbols("LEFTHAND-NETWORKS-NSM-STATUS-MIB", lefthandNetworksNsmStatusGroup=lefthandNetworksNsmStatusGroup, status=status, lhnNsmStatusModuleCompliances=lhnNsmStatusModuleCompliances, lhnNsmStatusModuleGroups=lhnNsmStatusModuleGroups, statusMessage=statusMessage, PYSNMP_MODULE_ID=lhnNsmStatusModule, lhnNsmStatusModuleConformance=lhnNsmStatusModuleConformance, lhnNsmStatusModule=lhnNsmStatusModule, lefthandNetworksNsmStatusMibCompliance=lefthandNetworksNsmStatusMibCompliance, statusSNMPD=statusSNMPD)
