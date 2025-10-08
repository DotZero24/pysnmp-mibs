#
# PySNMP MIB module UTSTARCOM-ROOT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/utstarcom/UTSTARCOM-ROOT-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:17:11 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, enterprises, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "enterprises", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
utstarcom = ModuleIdentity((1, 3, 6, 1, 4, 1, 1949))
utstarcom.setRevisions(('2005-09-01 16:21',))
if mibBuilder.loadTexts: utstarcom.setLastUpdated('200509011621Z')
if mibBuilder.loadTexts: utstarcom.setOrganization('UTStarcom, Inc.')
utsRoot = MibIdentifier((1, 3, 6, 1, 4, 1, 1949, 1))
utsProducts = MibIdentifier((1, 3, 6, 1, 4, 1, 1949, 1, 3))
utsBroadbandSwitch = MibIdentifier((1, 3, 6, 1, 4, 1, 1949, 1, 3, 10))
utsBBSProductSysId = MibIdentifier((1, 3, 6, 1, 4, 1, 1949, 1, 3, 10, 2))
utBBSEponOnuSysId = MibIdentifier((1, 3, 6, 1, 4, 1, 1949, 1, 3, 10, 2, 100))
utBBSEponOnuSysId2004 = ObjectIdentity((1, 3, 6, 1, 4, 1, 1949, 1, 3, 10, 2, 100, 6))
if mibBuilder.loadTexts: utBBSEponOnuSysId2004.setStatus('current')
utBBSGeponOnu = ObjectIdentity((1, 3, 6, 1, 4, 1, 1949, 1, 3, 10, 100))
if mibBuilder.loadTexts: utBBSGeponOnu.setStatus('current')
utBBSGeponOnu2004 = ObjectIdentity((1, 3, 6, 1, 4, 1, 1949, 1, 3, 10, 100, 6))
if mibBuilder.loadTexts: utBBSGeponOnu2004.setStatus('current')
utBBSGeponOnu404 = ObjectIdentity((1, 3, 6, 1, 4, 1, 1949, 1, 3, 10, 100, 7))
if mibBuilder.loadTexts: utBBSGeponOnu404.setStatus('current')
mibBuilder.exportSymbols("UTSTARCOM-ROOT-MIB", utsBroadbandSwitch=utsBroadbandSwitch, utsProducts=utsProducts, utBBSGeponOnu=utBBSGeponOnu, PYSNMP_MODULE_ID=utstarcom, utBBSGeponOnu404=utBBSGeponOnu404, utsBBSProductSysId=utsBBSProductSysId, utBBSEponOnuSysId2004=utBBSEponOnuSysId2004, utBBSGeponOnu2004=utBBSGeponOnu2004, utBBSEponOnuSysId=utBBSEponOnuSysId, utsRoot=utsRoot, utstarcom=utstarcom)
