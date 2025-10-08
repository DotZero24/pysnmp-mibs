#
# PySNMP MIB module ZTE-DSL-SSH-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/zte/ZTE-DSL-SSH-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:10:37 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, enterprises, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "enterprises", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("ZTE-DSL-SSH-MIB", zxDslSshGlobalState=zxDslSshGlobalState, zxDslSshAuthType=zxDslSshAuthType, zxDslSshVersion=zxDslSshVersion, PYSNMP_MODULE_ID=zxDslSshMib, zxDslSshMib=zxDslSshMib, zxDslSshGenKey=zxDslSshGenKey, zte=zte, zxDsl=zxDsl, zxDslSshAuthMode=zxDslSshAuthMode, zxDslSshglobal=zxDslSshglobal, zxDslSshServOnly=zxDslSshServOnly)
