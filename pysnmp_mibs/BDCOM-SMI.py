#
# PySNMP MIB module BDCOM-SMI (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/bdcom/BDCOM-SMI
# Produced by pysmi-1.1.12 at Wed Oct  8 10:42:19 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, enterprises, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "enterprises", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("BDCOM-SMI", bdcomPibToMib=bdcomPibToMib, bdcomProducts=bdcomProducts, bdcomModules=bdcomModules, bdlocal=bdlocal, bdcom=bdcom, bdcomPolicyAuto=bdcomPolicyAuto, bdtemporary=bdtemporary, PYSNMP_MODULE_ID=bdcom, bdMgmt=bdMgmt)
