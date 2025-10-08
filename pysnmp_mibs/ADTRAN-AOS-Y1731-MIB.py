#
# PySNMP MIB module ADTRAN-AOS-Y1731-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/adtran/ADTRAN-AOS-Y1731-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:30:01 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
adGenAOSConformance, adGenAOSMef, adGenAOS = mibBuilder.importSymbols("ADTRAN-AOS", "adGenAOSConformance", "adGenAOSMef", "adGenAOS")
adIdentity, = mibBuilder.importSymbols("ADTRAN-MIB", "adIdentity")
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
dot1agCfmMaIndex, dot1agCfmMdIndex = mibBuilder.importSymbols("IEEE8021-CFM-MIB", "dot1agCfmMaIndex", "dot1agCfmMdIndex")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Unsigned32, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Unsigned32", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
adGenAosY1731Mib = ModuleIdentity((1, 3, 6, 1, 4, 1, 664, 6, 10000, 53, 9, 9))
if mibBuilder.loadTexts: adGenAosY1731Mib.setLastUpdated('201801180000Z')
if mibBuilder.loadTexts: adGenAosY1731Mib.setOrganization('ADTRAN, Inc.')
adGenAosY1731 = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 9))
adGenAosY1731Conformance = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 34))
adGenAosY1731Groups = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 34, 1))
adGenAosY1731Compliances = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 34, 2))
class AdGenAosY1731Alarms(TextualConvention, Bits):
    reference = 'Y.1731 7.1.2 clause'
    status = 'current'
    namedValues = NamedValues(("bDefY1731CcmRxRDIAlarm", 0), ("bDefY1731CcmLossOfContinuityAlarm", 1), ("bDefY1731CcmUnexpectedMepAlarm", 2), ("bDefY1731CcmUnexpectedPeriodAlarm", 3), ("bDefY1731CcmMismergeAlarm", 4), ("bDefY1731CcmUnexpectedMegLevelAlarm", 5))

adGenAosY1731LocalMepTable = MibTable((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 9, 1), )
if mibBuilder.loadTexts: adGenAosY1731LocalMepTable.setStatus('current')
adGenAosY1731LocalMepEntry = MibTableRow((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 9, 1, 1), ).setIndexNames((0, "IEEE8021-CFM-MIB", "dot1agCfmMdIndex"), (0, "IEEE8021-CFM-MIB", "dot1agCfmMaIndex"), (0, "ADTRAN-AOS-Y1731-MIB", "adGenAosY1731LocalMepId"))
if mibBuilder.loadTexts: adGenAosY1731LocalMepEntry.setStatus('current')
adGenAosY1731LocalMepId = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 9, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 8191)))
if mibBuilder.loadTexts: adGenAosY1731LocalMepId.setStatus('current')
adGenAosY1731Alarms = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 9, 1, 1, 2), AdGenAosY1731Alarms()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adGenAosY1731Alarms.setStatus('current')
adGenAosY1731FullCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 34, 2, 1)).setObjects(("ADTRAN-AOS-Y1731-MIB", "adGenAosY1731Group"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    adGenAosY1731FullCompliance = adGenAosY1731FullCompliance.setStatus('current')
adGenAosY1731Group = ObjectGroup((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 34, 1, 1)).setObjects(("ADTRAN-AOS-Y1731-MIB", "adGenAosY1731Alarms"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    adGenAosY1731Group = adGenAosY1731Group.setStatus('current')
mibBuilder.exportSymbols("ADTRAN-AOS-Y1731-MIB", adGenAosY1731Conformance=adGenAosY1731Conformance, adGenAosY1731=adGenAosY1731, adGenAosY1731LocalMepEntry=adGenAosY1731LocalMepEntry, adGenAosY1731FullCompliance=adGenAosY1731FullCompliance, adGenAosY1731Compliances=adGenAosY1731Compliances, adGenAosY1731LocalMepId=adGenAosY1731LocalMepId, adGenAosY1731Alarms=adGenAosY1731Alarms, adGenAosY1731LocalMepTable=adGenAosY1731LocalMepTable, AdGenAosY1731Alarms=AdGenAosY1731Alarms, adGenAosY1731Groups=adGenAosY1731Groups, adGenAosY1731Group=adGenAosY1731Group, adGenAosY1731Mib=adGenAosY1731Mib, PYSNMP_MODULE_ID=adGenAosY1731Mib)
