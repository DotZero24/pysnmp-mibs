#
# PySNMP MIB module TN-SAS-IEEE8021-CFM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/nokia/TN-SAS-IEEE8021-CFM-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:21:31 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
dot1agCfmMepEntry, = mibBuilder.importSymbols("IEEE8021-CFM-MIB", "dot1agCfmMepEntry")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Unsigned32, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Unsigned32", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention")
tnSASModules, tnSASObjs = mibBuilder.importSymbols("TROPIC-GLOBAL-REG", "tnSASModules", "tnSASObjs")
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
mibBuilder.exportSymbols("TN-SAS-IEEE8021-CFM-MIB", tnDot1agCfmMepExtnTable=tnDot1agCfmMepExtnTable, tnDot1agCfmMepControlSapTag=tnDot1agCfmMepControlSapTag, tnDot1agCfmMepSendAisOnPortDown=tnDot1agCfmMepSendAisOnPortDown, tnSASIEEE8021CfmMIBModule=tnSASIEEE8021CfmMIBModule, PYSNMP_MODULE_ID=tnSASIEEE8021CfmMIBModule, tnSASDot1agMIBObjs=tnSASDot1agMIBObjs, tnDot1agCfmMepExtnEntry=tnDot1agCfmMepExtnEntry, tnSASDot1agCfmMep=tnSASDot1agCfmMep)
