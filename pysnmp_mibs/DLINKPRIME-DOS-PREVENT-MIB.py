#
# PySNMP MIB module DLINKPRIME-DOS-PREVENT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/d-link/DLINKPRIME-DOS-PREVENT-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:35:01 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
dlinkPrimeCommon, = mibBuilder.importSymbols("DLINK-ID-REC-MIB", "dlinkPrimeCommon")
InterfaceIndexOrZero, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndexOrZero")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Integer32, Unsigned32, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Counter64, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Integer32", "Unsigned32", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Counter64", "Bits", "TimeTicks", "IpAddress")
DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention")
dlinkPrimeDosPrevMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 171, 15, 4))
dlinkPrimeDosPrevMIB.setRevisions(('2014-04-26 00:00',))
if mibBuilder.loadTexts: dlinkPrimeDosPrevMIB.setLastUpdated('201404260000Z')
if mibBuilder.loadTexts: dlinkPrimeDosPrevMIB.setOrganization('D-Link Corp.')
class DosAttackType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 99))
    namedValues = NamedValues(("landAttack", 1), ("blatAttack", 2), ("tcpNullScan", 3), ("tcpXmasScan", 4), ("tcpSynFin", 5), ("tcpSynSrcPortLess1024", 6), ("pingDeathAttack", 7), ("all", 99))

dpDosPrevMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 15, 4, 0))
dpDosPrevMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 15, 4, 1))
dpDosPrevMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 15, 4, 2))
dpDosPrevCtrlTable = MibTable((1, 3, 6, 1, 4, 1, 171, 15, 4, 1, 1), )
if mibBuilder.loadTexts: dpDosPrevCtrlTable.setStatus('current')
dpDosPrevCtrlEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 15, 4, 1, 1, 1), ).setIndexNames((0, "DLINKPRIME-DOS-PREVENT-MIB", "dpDosPrevCtrlAttackType"))
if mibBuilder.loadTexts: dpDosPrevCtrlEntry.setStatus('current')
dpDosPrevCtrlAttackType = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 15, 4, 1, 1, 1, 1), DosAttackType())
if mibBuilder.loadTexts: dpDosPrevCtrlAttackType.setStatus('current')
dpDosPrevCtrlEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 15, 4, 1, 1, 1, 2), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dpDosPrevCtrlEnabled.setStatus('current')
dpDosPrevCtrlActionType = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 15, 4, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("drop", 1))).clone('drop')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dpDosPrevCtrlActionType.setStatus('current')
dpDosPrevMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 15, 4, 2, 1))
dpDosPrevMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 15, 4, 2, 2))
dpDosPrevMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 171, 15, 4, 2, 1, 1)).setObjects(("DLINKPRIME-DOS-PREVENT-MIB", "dpDosPrevBasicGroup"), ("DLINKPRIME-DOS-PREVENT-MIB", "dpDosPrevActionRedirectCtrlGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dpDosPrevMIBCompliance = dpDosPrevMIBCompliance.setStatus('current')
dpDosPrevBasicGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 171, 15, 4, 2, 2, 1)).setObjects(("DLINKPRIME-DOS-PREVENT-MIB", "dpDosPrevCtrlEnabled"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dpDosPrevBasicGroup = dpDosPrevBasicGroup.setStatus('current')
mibBuilder.exportSymbols("DLINKPRIME-DOS-PREVENT-MIB", dlinkPrimeDosPrevMIB=dlinkPrimeDosPrevMIB, dpDosPrevCtrlActionType=dpDosPrevCtrlActionType, dpDosPrevMIBConformance=dpDosPrevMIBConformance, dpDosPrevMIBNotifications=dpDosPrevMIBNotifications, DosAttackType=DosAttackType, dpDosPrevCtrlAttackType=dpDosPrevCtrlAttackType, dpDosPrevMIBCompliance=dpDosPrevMIBCompliance, dpDosPrevMIBGroups=dpDosPrevMIBGroups, dpDosPrevCtrlEnabled=dpDosPrevCtrlEnabled, dpDosPrevCtrlTable=dpDosPrevCtrlTable, dpDosPrevBasicGroup=dpDosPrevBasicGroup, dpDosPrevMIBObjects=dpDosPrevMIBObjects, PYSNMP_MODULE_ID=dlinkPrimeDosPrevMIB, dpDosPrevCtrlEntry=dpDosPrevCtrlEntry, dpDosPrevMIBCompliances=dpDosPrevMIBCompliances)
