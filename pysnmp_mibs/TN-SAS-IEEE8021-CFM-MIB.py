#
# PySNMP MIB module TN-SAS-IEEE8021-CFM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/nokia/TN-SAS-IEEE8021-CFM-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:40:15 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
dot1agCfmMepEntry, = mibBuilder.importSymbols("IEEE8021-CFM-MIB", "dot1agCfmMepEntry")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TruthValue, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "TextualConvention", "DisplayString")
tnSASObjs, tnSASModules = mibBuilder.importSymbols("TROPIC-GLOBAL-REG", "tnSASObjs", "tnSASModules")
tnSASIEEE8021CfmMIBModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 7483, 7, 2, 1, 1, 11))
tnSASIEEE8021CfmMIBModule.setRevisions(('2010-01-01 00:00',))
if mibBuilder.loadTexts: tnSASIEEE8021CfmMIBModule.setLastUpdated('201001010000Z')
if mibBuilder.loadTexts: tnSASIEEE8021CfmMIBModule.setOrganization('Nokia')
tnSASDot1agMIBObjs = MibIdentifier((1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 11))
tnSASDot1agCfmMep = MibIdentifier((1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 11, 1))
tnDot1agCfmMepExtnTable = MibTable((1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 11, 1, 1), )
if mibBuilder.loadTexts: tnDot1agCfmMepExtnTable.setStatus('current')
tnDot1agCfmMepExtnEntry = MibTableRow((1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 11, 1, 1, 1), )
dot1agCfmMepEntry.registerAugmentions(("TN-SAS-IEEE8021-CFM-MIB", "tnDot1agCfmMepExtnEntry"))
tnDot1agCfmMepExtnEntry.setIndexNames(*dot1agCfmMepEntry.getIndexNames())
if mibBuilder.loadTexts: tnDot1agCfmMepExtnEntry.setStatus('current')
tnDot1agCfmMepSendAisOnPortDown = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 11, 1, 1, 1, 1), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tnDot1agCfmMepSendAisOnPortDown.setStatus('current')
tnDot1agCfmMepControlSapTag = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 11, 1, 1, 1, 2), Unsigned32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(512, 768), ))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tnDot1agCfmMepControlSapTag.setStatus('current')
mibBuilder.exportSymbols("TN-SAS-IEEE8021-CFM-MIB", tnDot1agCfmMepExtnTable=tnDot1agCfmMepExtnTable, PYSNMP_MODULE_ID=tnSASIEEE8021CfmMIBModule, tnDot1agCfmMepSendAisOnPortDown=tnDot1agCfmMepSendAisOnPortDown, tnDot1agCfmMepExtnEntry=tnDot1agCfmMepExtnEntry, tnSASIEEE8021CfmMIBModule=tnSASIEEE8021CfmMIBModule, tnDot1agCfmMepControlSapTag=tnDot1agCfmMepControlSapTag, tnSASDot1agMIBObjs=tnSASDot1agMIBObjs, tnSASDot1agCfmMep=tnSASDot1agCfmMep)
