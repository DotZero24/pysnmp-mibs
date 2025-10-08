#
# PySNMP MIB module UTSTARCOM-ROOT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/utstarcom/UTSTARCOM-ROOT-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:33:41 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, enterprises, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "enterprises", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("UTSTARCOM-ROOT-MIB", utsBroadbandSwitch=utsBroadbandSwitch, utstarcom=utstarcom, utBBSGeponOnu404=utBBSGeponOnu404, utBBSGeponOnu=utBBSGeponOnu, utsProducts=utsProducts, utBBSEponOnuSysId=utBBSEponOnuSysId, utsRoot=utsRoot, utsBBSProductSysId=utsBBSProductSysId, utBBSEponOnuSysId2004=utBBSEponOnuSysId2004, PYSNMP_MODULE_ID=utstarcom, utBBSGeponOnu2004=utBBSGeponOnu2004)
