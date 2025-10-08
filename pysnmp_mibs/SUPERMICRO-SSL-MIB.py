#
# PySNMP MIB module SUPERMICRO-SSL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/supermicro/SUPERMICRO-SSL-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 09:57:43 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, enterprises, NotificationType, Integer32, Bits, Unsigned32, iso, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "enterprises", "NotificationType", "Integer32", "Bits", "Unsigned32", "iso", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TruthValue, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "TextualConvention", "DisplayString")
ssl = ModuleIdentity((1, 3, 6, 1, 4, 1, 10876, 101, 1, 96))
ssl.setRevisions(('2012-09-05 00:00',))
if mibBuilder.loadTexts: ssl.setLastUpdated('201209050000Z')
if mibBuilder.loadTexts: ssl.setOrganization('Super Micro Computer Inc.')
sslGeneralGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 10876, 101, 1, 96, 1))
sslCiphers = MibIdentifier((1, 3, 6, 1, 4, 1, 10876, 101, 1, 96, 2))
sslSecureHttpStatus = MibScalar((1, 3, 6, 1, 4, 1, 10876, 101, 1, 96, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('enable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sslSecureHttpStatus.setStatus('current')
sslPort = MibScalar((1, 3, 6, 1, 4, 1, 10876, 101, 1, 96, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)).clone(443)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sslPort.setStatus('current')
sslTrace = MibScalar((1, 3, 6, 1, 4, 1, 10876, 101, 1, 96, 1, 4), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sslTrace.setStatus('current')
sslVersion = MibScalar((1, 3, 6, 1, 4, 1, 10876, 101, 1, 96, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("all", 1), ("ssl3", 2), ("tls1", 3))).clone('tls1')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sslVersion.setStatus('current')
sslRestconfStatus = MibScalar((1, 3, 6, 1, 4, 1, 10876, 101, 1, 96, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('enable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sslRestconfStatus.setStatus('current')
sslCipherList = MibScalar((1, 3, 6, 1, 4, 1, 10876, 101, 1, 96, 2, 1), Integer32().clone(76)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sslCipherList.setStatus('current')
sslDefaultCipherList = MibScalar((1, 3, 6, 1, 4, 1, 10876, 101, 1, 96, 2, 2), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sslDefaultCipherList.setStatus('current')
mibBuilder.exportSymbols("SUPERMICRO-SSL-MIB", sslTrace=sslTrace, sslGeneralGroup=sslGeneralGroup, sslCipherList=sslCipherList, sslVersion=sslVersion, sslDefaultCipherList=sslDefaultCipherList, sslCiphers=sslCiphers, sslPort=sslPort, PYSNMP_MODULE_ID=ssl, ssl=ssl, sslSecureHttpStatus=sslSecureHttpStatus, sslRestconfStatus=sslRestconfStatus)
