#
# PySNMP MIB module SUPERMICRO-SSL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/supermicro/SUPERMICRO-SSL-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 09:56:53 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, enterprises, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "enterprises", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention")
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
mibBuilder.exportSymbols("SUPERMICRO-SSL-MIB", sslVersion=sslVersion, sslCiphers=sslCiphers, sslRestconfStatus=sslRestconfStatus, sslCipherList=sslCipherList, sslPort=sslPort, sslTrace=sslTrace, sslDefaultCipherList=sslDefaultCipherList, sslSecureHttpStatus=sslSecureHttpStatus, PYSNMP_MODULE_ID=ssl, ssl=ssl, sslGeneralGroup=sslGeneralGroup)
