#
# PySNMP MIB module BDCOM-SMI (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/bdcom/BDCOM-SMI
# Produced by pysmi-1.1.12 at Thu Sep 11 10:22:50 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, enterprises, ObjectIdentity, Gauge32, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "enterprises", "ObjectIdentity", "Gauge32", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
bdcom = ModuleIdentity((1, 3, 6, 1, 4, 1, 3320))
if mibBuilder.loadTexts: bdcom.setLastUpdated('200006280000Z')
if mibBuilder.loadTexts: bdcom.setOrganization('BDCom, Inc.')
bdcomProducts = ObjectIdentity((1, 3, 6, 1, 4, 1, 3320, 1))
if mibBuilder.loadTexts: bdcomProducts.setStatus('current')
bdlocal = ObjectIdentity((1, 3, 6, 1, 4, 1, 3320, 2))
if mibBuilder.loadTexts: bdlocal.setStatus('current')
bdtemporary = ObjectIdentity((1, 3, 6, 1, 4, 1, 3320, 3))
if mibBuilder.loadTexts: bdtemporary.setStatus('current')
bdMgmt = ObjectIdentity((1, 3, 6, 1, 4, 1, 3320, 9))
if mibBuilder.loadTexts: bdMgmt.setStatus('current')
bdcomModules = ObjectIdentity((1, 3, 6, 1, 4, 1, 3320, 12))
if mibBuilder.loadTexts: bdcomModules.setStatus('current')
bdcomPolicyAuto = ObjectIdentity((1, 3, 6, 1, 4, 1, 3320, 18))
if mibBuilder.loadTexts: bdcomPolicyAuto.setStatus('current')
bdcomPibToMib = ObjectIdentity((1, 3, 6, 1, 4, 1, 3320, 18, 2))
if mibBuilder.loadTexts: bdcomPibToMib.setStatus('current')
mibBuilder.exportSymbols("BDCOM-SMI", bdtemporary=bdtemporary, bdcom=bdcom, PYSNMP_MODULE_ID=bdcom, bdcomPolicyAuto=bdcomPolicyAuto, bdcomProducts=bdcomProducts, bdcomPibToMib=bdcomPibToMib, bdcomModules=bdcomModules, bdlocal=bdlocal, bdMgmt=bdMgmt)
