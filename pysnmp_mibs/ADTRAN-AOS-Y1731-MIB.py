#
# PySNMP MIB module ADTRAN-AOS-Y1731-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/adtran/ADTRAN-AOS-Y1731-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:53:32 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
adGenAOSConformance, adGenAOS, adGenAOSMef = mibBuilder.importSymbols("ADTRAN-AOS", "adGenAOSConformance", "adGenAOS", "adGenAOSMef")
adIdentity, = mibBuilder.importSymbols("ADTRAN-MIB", "adIdentity")
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
dot1agCfmMaIndex, dot1agCfmMdIndex = mibBuilder.importSymbols("IEEE8021-CFM-MIB", "dot1agCfmMaIndex", "dot1agCfmMdIndex")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
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
mibBuilder.exportSymbols("ADTRAN-AOS-Y1731-MIB", AdGenAosY1731Alarms=AdGenAosY1731Alarms, adGenAosY1731Groups=adGenAosY1731Groups, adGenAosY1731FullCompliance=adGenAosY1731FullCompliance, adGenAosY1731Group=adGenAosY1731Group, adGenAosY1731Compliances=adGenAosY1731Compliances, adGenAosY1731Conformance=adGenAosY1731Conformance, adGenAosY1731Alarms=adGenAosY1731Alarms, adGenAosY1731LocalMepTable=adGenAosY1731LocalMepTable, adGenAosY1731LocalMepId=adGenAosY1731LocalMepId, PYSNMP_MODULE_ID=adGenAosY1731Mib, adGenAosY1731Mib=adGenAosY1731Mib, adGenAosY1731LocalMepEntry=adGenAosY1731LocalMepEntry, adGenAosY1731=adGenAosY1731)
