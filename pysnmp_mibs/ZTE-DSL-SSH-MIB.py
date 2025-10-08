#
# PySNMP MIB module ZTE-DSL-SSH-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/zte/ZTE-DSL-SSH-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:03:52 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, enterprises, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "enterprises", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
zxDslSshMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 3902, 1004, 35))
if mibBuilder.loadTexts: zxDslSshMib.setLastUpdated('0706090000Z')
if mibBuilder.loadTexts: zxDslSshMib.setOrganization('Zhongxing Telcom Co. Ltd.')
zte = MibIdentifier((1, 3, 6, 1, 4, 1, 3902))
zxDsl = MibIdentifier((1, 3, 6, 1, 4, 1, 3902, 1004))
zxDslSshglobal = MibIdentifier((1, 3, 6, 1, 4, 1, 3902, 1004, 35, 1))
zxDslSshGlobalState = MibScalar((1, 3, 6, 1, 4, 1, 3902, 1004, 35, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zxDslSshGlobalState.setStatus('current')
zxDslSshAuthMode = MibScalar((1, 3, 6, 1, 4, 1, 3902, 1004, 35, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("local", 1), ("radius", 2))).clone('local')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zxDslSshAuthMode.setStatus('current')
zxDslSshAuthType = MibScalar((1, 3, 6, 1, 4, 1, 3902, 1004, 35, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("pap", 1), ("chap", 2))).clone('chap')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zxDslSshAuthType.setStatus('current')
zxDslSshGenKey = MibScalar((1, 3, 6, 1, 4, 1, 3902, 1004, 35, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("value", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zxDslSshGenKey.setStatus('current')
zxDslSshServOnly = MibScalar((1, 3, 6, 1, 4, 1, 3902, 1004, 35, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zxDslSshServOnly.setStatus('current')
zxDslSshVersion = MibScalar((1, 3, 6, 1, 4, 1, 3902, 1004, 35, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("sshv1", 1), ("sshv2", 2))).clone('sshv1')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zxDslSshVersion.setStatus('current')
mibBuilder.exportSymbols("ZTE-DSL-SSH-MIB", zxDslSshGenKey=zxDslSshGenKey, zte=zte, zxDslSshMib=zxDslSshMib, zxDslSshGlobalState=zxDslSshGlobalState, zxDslSshServOnly=zxDslSshServOnly, zxDslSshAuthType=zxDslSshAuthType, zxDslSshAuthMode=zxDslSshAuthMode, zxDslSshVersion=zxDslSshVersion, PYSNMP_MODULE_ID=zxDslSshMib, zxDsl=zxDsl, zxDslSshglobal=zxDslSshglobal)
