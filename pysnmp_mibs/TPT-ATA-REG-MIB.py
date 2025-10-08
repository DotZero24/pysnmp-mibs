#
# PySNMP MIB module TPT-ATA-REG-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/trendmicro/TPT-ATA-REG-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 09:58:32 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
tpt_reg, = mibBuilder.importSymbols("TIPPINGPOINT-REG-MIB", "tpt-reg")
tpt_ata_family = ModuleIdentity((1, 3, 6, 1, 4, 1, 10734, 1, 10)).setLabel("tpt-ata-family")
tpt_ata_family.setRevisions(('2016-05-25 18:54', '2015-07-30 17:35',))
if mibBuilder.loadTexts: tpt_ata_family.setLastUpdated('201605251854Z')
if mibBuilder.loadTexts: tpt_ata_family.setOrganization('Trend Micro, Inc.')
tpt_model_ata_network = ObjectIdentity((1, 3, 6, 1, 4, 1, 10734, 1, 10, 1)).setLabel("tpt-model-ata-network")
if mibBuilder.loadTexts: tpt_model_ata_network.setStatus('current')
tpt_model_ata_mail = ObjectIdentity((1, 3, 6, 1, 4, 1, 10734, 1, 10, 2)).setLabel("tpt-model-ata-mail")
if mibBuilder.loadTexts: tpt_model_ata_mail.setStatus('current')
mibBuilder.exportSymbols("TPT-ATA-REG-MIB", tpt_model_ata_network=tpt_model_ata_network, tpt_ata_family=tpt_ata_family, PYSNMP_MODULE_ID=tpt_ata_family, tpt_model_ata_mail=tpt_model_ata_mail)
