#
# PySNMP MIB module TPT-ATA-REG-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/trendmicro/TPT-ATA-REG-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 09:57:15 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, ObjectIdentity, Gauge32, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "ObjectIdentity", "Gauge32", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
tpt_reg, = mibBuilder.importSymbols("TIPPINGPOINT-REG-MIB", "tpt-reg")
tpt_ata_family = ModuleIdentity((1, 3, 6, 1, 4, 1, 10734, 1, 10)).setLabel("tpt-ata-family")
tpt_ata_family.setRevisions(('2016-05-25 18:54', '2015-07-30 17:35',))
if mibBuilder.loadTexts: tpt_ata_family.setLastUpdated('201605251854Z')
if mibBuilder.loadTexts: tpt_ata_family.setOrganization('Trend Micro, Inc.')
tpt_model_ata_network = ObjectIdentity((1, 3, 6, 1, 4, 1, 10734, 1, 10, 1)).setLabel("tpt-model-ata-network")
if mibBuilder.loadTexts: tpt_model_ata_network.setStatus('current')
tpt_model_ata_mail = ObjectIdentity((1, 3, 6, 1, 4, 1, 10734, 1, 10, 2)).setLabel("tpt-model-ata-mail")
if mibBuilder.loadTexts: tpt_model_ata_mail.setStatus('current')
mibBuilder.exportSymbols("TPT-ATA-REG-MIB", PYSNMP_MODULE_ID=tpt_ata_family, tpt_model_ata_mail=tpt_model_ata_mail, tpt_model_ata_network=tpt_model_ata_network, tpt_ata_family=tpt_ata_family)
