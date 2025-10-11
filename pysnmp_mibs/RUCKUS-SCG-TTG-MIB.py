# SNMP MIB module (RUCKUS-SCG-TTG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/ruckus/RUCKUS-SCG-TTG-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:13:40 2025
# On host Robs-Air.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]

if 'mibBuilder' not in globals():
    import sys

    sys.stderr.write(__doc__)
    sys.exit(1)

# Import base ASN.1 objects even if this MIB does not use it

(Integer,
 OctetString,
 ObjectIdentifier) = mibBuilder.importSymbols(
    "ASN1",
    "Integer",
    "OctetString",
    "ObjectIdentifier")

(NamedValues,) = mibBuilder.importSymbols(
    "ASN1-ENUMERATION",
    "NamedValues")
(ConstraintsIntersection,
 ConstraintsUnion,
 SingleValueConstraint,
 ValueRangeConstraint,
 ValueSizeConstraint) = mibBuilder.importSymbols(
    "ASN1-REFINEMENT",
    "ConstraintsIntersection",
    "ConstraintsUnion",
    "SingleValueConstraint",
    "ValueRangeConstraint",
    "ValueSizeConstraint")

# Import SMI symbols from the MIBs this MIB depends on

(ruckusSCGTTGModule,) = mibBuilder.importSymbols(
    "RUCKUS-ROOT-MIB",
    "ruckusSCGTTGModule")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(Bits,
 Counter32,
 Counter64,
 Gauge32,
 Integer32,
 IpAddress,
 ModuleIdentity,
 MibIdentifier,
 NotificationType,
 ObjectIdentity,
 MibScalar,
 MibTable,
 MibTableRow,
 MibTableColumn,
 TimeTicks,
 Unsigned32,
 iso) = mibBuilder.importSymbols(
    "SNMPv2-SMI",
    "Bits",
    "Counter32",
    "Counter64",
    "Gauge32",
    "Integer32",
    "IpAddress",
    "ModuleIdentity",
    "MibIdentifier",
    "NotificationType",
    "ObjectIdentity",
    "MibScalar",
    "MibTable",
    "MibTableRow",
    "MibTableColumn",
    "TimeTicks",
    "Unsigned32",
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

ruckusTTGMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 3, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RuckusTTGObjects_ObjectIdentity = ObjectIdentity
ruckusTTGObjects = _RuckusTTGObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 3, 1, 1)
)
_RuckusAAAInfo_ObjectIdentity = ObjectIdentity
ruckusAAAInfo = _RuckusAAAInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 3, 1, 1, 1)
)
_RuckusAAATable_Object = MibTable
ruckusAAATable = _RuckusAAATable_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 3, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    ruckusAAATable.setStatus("current")
_RuckusAAAEntry_Object = MibTableRow
ruckusAAAEntry = _RuckusAAAEntry_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 3, 1, 1, 1, 1, 1)
)
ruckusAAAEntry.setIndexNames(
    (0, "RUCKUS-SCG-TTG-MIB", "ruckusAAAIndex"),
)
if mibBuilder.loadTexts:
    ruckusAAAEntry.setStatus("current")
_RuckusAAAAaaIp_Type = DisplayString
_RuckusAAAAaaIp_Object = MibTableColumn
ruckusAAAAaaIp = _RuckusAAAAaaIp_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 3, 1, 1, 1, 1, 1, 1),
    _RuckusAAAAaaIp_Type()
)
ruckusAAAAaaIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusAAAAaaIp.setStatus("current")
_RuckusAAANumSuccAuthPerm_Type = Counter64
_RuckusAAANumSuccAuthPerm_Object = MibTableColumn
ruckusAAANumSuccAuthPerm = _RuckusAAANumSuccAuthPerm_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 3, 1, 1, 1, 1, 1, 2),
    _RuckusAAANumSuccAuthPerm_Type()
)
ruckusAAANumSuccAuthPerm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusAAANumSuccAuthPerm.setStatus("current")
_RuckusAAANumFailAuthPerm_Type = Counter64
_RuckusAAANumFailAuthPerm_Object = MibTableColumn
ruckusAAANumFailAuthPerm = _RuckusAAANumFailAuthPerm_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 3, 1, 1, 1, 1, 1, 3),
    _RuckusAAANumFailAuthPerm_Type()
)
ruckusAAANumFailAuthPerm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusAAANumFailAuthPerm.setStatus("current")
_RuckusAAANumSuccAuthPsd_Type = Counter64
_RuckusAAANumSuccAuthPsd_Object = MibTableColumn
ruckusAAANumSuccAuthPsd = _RuckusAAANumSuccAuthPsd_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 3, 1, 1, 1, 1, 1, 4),
    _RuckusAAANumSuccAuthPsd_Type()
)
ruckusAAANumSuccAuthPsd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusAAANumSuccAuthPsd.setStatus("current")
_RuckusAAANumFailAuthPsd_Type = Counter64
_RuckusAAANumFailAuthPsd_Object = MibTableColumn
ruckusAAANumFailAuthPsd = _RuckusAAANumFailAuthPsd_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 3, 1, 1, 1, 1, 1, 5),
    _RuckusAAANumFailAuthPsd_Type()
)
ruckusAAANumFailAuthPsd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusAAANumFailAuthPsd.setStatus("current")
_RuckusAAANumSuccFastAuth_Type = Counter64
_RuckusAAANumSuccFastAuth_Object = MibTableColumn
ruckusAAANumSuccFastAuth = _RuckusAAANumSuccFastAuth_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 3, 1, 1, 1, 1, 1, 6),
    _RuckusAAANumSuccFastAuth_Type()
)
ruckusAAANumSuccFastAuth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusAAANumSuccFastAuth.setStatus("current")
_RuckusAAANumFailFastAuth_Type = Counter64
_RuckusAAANumFailFastAuth_Object = MibTableColumn
ruckusAAANumFailFastAuth = _RuckusAAANumFailFastAuth_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 3, 1, 1, 1, 1, 1, 7),
    _RuckusAAANumFailFastAuth_Type()
)
ruckusAAANumFailFastAuth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusAAANumFailFastAuth.setStatus("current")
_RuckusAAANumAuthUnknPsd_Type = Counter64
_RuckusAAANumAuthUnknPsd_Object = MibTableColumn
ruckusAAANumAuthUnknPsd = _RuckusAAANumAuthUnknPsd_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 3, 1, 1, 1, 1, 1, 8),
    _RuckusAAANumAuthUnknPsd_Type()
)
ruckusAAANumAuthUnknPsd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusAAANumAuthUnknPsd.setStatus("current")
_RuckusAAANumAuthUnknFR_Type = Counter64
_RuckusAAANumAuthUnknFR_Object = MibTableColumn
ruckusAAANumAuthUnknFR = _RuckusAAANumAuthUnknFR_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 3, 1, 1, 1, 1, 1, 9),
    _RuckusAAANumAuthUnknFR_Type()
)
ruckusAAANumAuthUnknFR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusAAANumAuthUnknFR.setStatus("current")
_RuckusAAANumIncompleteAuth_Type = Counter64
_RuckusAAANumIncompleteAuth_Object = MibTableColumn
ruckusAAANumIncompleteAuth = _RuckusAAANumIncompleteAuth_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 3, 1, 1, 1, 1, 1, 10),
    _RuckusAAANumIncompleteAuth_Type()
)
ruckusAAANumIncompleteAuth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusAAANumIncompleteAuth.setStatus("current")
_RuckusAAANumSuccAcc_Type = Counter64
_RuckusAAANumSuccAcc_Object = MibTableColumn
ruckusAAANumSuccAcc = _RuckusAAANumSuccAcc_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 3, 1, 1, 1, 1, 1, 11),
    _RuckusAAANumSuccAcc_Type()
)
ruckusAAANumSuccAcc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusAAANumSuccAcc.setStatus("current")
_RuckusAAANumFailAcc_Type = Counter64
_RuckusAAANumFailAcc_Object = MibTableColumn
ruckusAAANumFailAcc = _RuckusAAANumFailAcc_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 3, 1, 1, 1, 1, 1, 12),
    _RuckusAAANumFailAcc_Type()
)
ruckusAAANumFailAcc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusAAANumFailAcc.setStatus("current")
_RuckusAAANumRadAcsRq_Type = Counter64
_RuckusAAANumRadAcsRq_Object = MibTableColumn
ruckusAAANumRadAcsRq = _RuckusAAANumRadAcsRq_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 3, 1, 1, 1, 1, 1, 13),
    _RuckusAAANumRadAcsRq_Type()
)
ruckusAAANumRadAcsRq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusAAANumRadAcsRq.setStatus("current")
_RuckusAAANumRadAcsAcpt_Type = Counter64
_RuckusAAANumRadAcsAcpt_Object = MibTableColumn
ruckusAAANumRadAcsAcpt = _RuckusAAANumRadAcsAcpt_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 3, 1, 1, 1, 1, 1, 14),
    _RuckusAAANumRadAcsAcpt_Type()
)
ruckusAAANumRadAcsAcpt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusAAANumRadAcsAcpt.setStatus("current")
_RuckusAAANumRadAcsChlg_Type = Counter64
_RuckusAAANumRadAcsChlg_Object = MibTableColumn
ruckusAAANumRadAcsChlg = _RuckusAAANumRadAcsChlg_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 3, 1, 1, 1, 1, 1, 15),
    _RuckusAAANumRadAcsChlg_Type()
)
ruckusAAANumRadAcsChlg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusAAANumRadAcsChlg.setStatus("current")
_RuckusAAANumRadAcsRej_Type = Counter64
_RuckusAAANumRadAcsRej_Object = MibTableColumn
ruckusAAANumRadAcsRej = _RuckusAAANumRadAcsRej_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 3, 1, 1, 1, 1, 1, 16),
    _RuckusAAANumRadAcsRej_Type()
)
ruckusAAANumRadAcsRej.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusAAANumRadAcsRej.setStatus("current")
_RuckusAAANumRadAccRq_Type = Counter64
_RuckusAAANumRadAccRq_Object = MibTableColumn
ruckusAAANumRadAccRq = _RuckusAAANumRadAccRq_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 3, 1, 1, 1, 1, 1, 17),
    _RuckusAAANumRadAccRq_Type()
)
ruckusAAANumRadAccRq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusAAANumRadAccRq.setStatus("current")
_RuckusAAANumRadAccAcpt_Type = Counter64
_RuckusAAANumRadAccAcpt_Object = MibTableColumn
ruckusAAANumRadAccAcpt = _RuckusAAANumRadAccAcpt_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 3, 1, 1, 1, 1, 1, 18),
    _RuckusAAANumRadAccAcpt_Type()
)
ruckusAAANumRadAccAcpt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusAAANumRadAccAcpt.setStatus("current")
_RuckusAAANumRadCoaRq_Type = Counter64
_RuckusAAANumRadCoaRq_Object = MibTableColumn
ruckusAAANumRadCoaRq = _RuckusAAANumRadCoaRq_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 3, 1, 1, 1, 1, 1, 19),
    _RuckusAAANumRadCoaRq_Type()
)
ruckusAAANumRadCoaRq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusAAANumRadCoaRq.setStatus("current")
_RuckusAAANumSuccCoaAcpt_Type = Counter64
_RuckusAAANumSuccCoaAcpt_Object = MibTableColumn
ruckusAAANumSuccCoaAcpt = _RuckusAAANumSuccCoaAcpt_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 3, 1, 1, 1, 1, 1, 20),
    _RuckusAAANumSuccCoaAcpt_Type()
)
ruckusAAANumSuccCoaAcpt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusAAANumSuccCoaAcpt.setStatus("current")
_RuckusAAANumFailCoaAcpt_Type = Counter64
_RuckusAAANumFailCoaAcpt_Object = MibTableColumn
ruckusAAANumFailCoaAcpt = _RuckusAAANumFailCoaAcpt_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 3, 1, 1, 1, 1, 1, 21),
    _RuckusAAANumFailCoaAcpt_Type()
)
ruckusAAANumFailCoaAcpt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusAAANumFailCoaAcpt.setStatus("current")
_RuckusAAANumRadDmRq_Type = Counter64
_RuckusAAANumRadDmRq_Object = MibTableColumn
ruckusAAANumRadDmRq = _RuckusAAANumRadDmRq_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 3, 1, 1, 1, 1, 1, 22),
    _RuckusAAANumRadDmRq_Type()
)
ruckusAAANumRadDmRq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusAAANumRadDmRq.setStatus("current")
_RuckusAAANumSuccDmAcpt_Type = Counter64
_RuckusAAANumSuccDmAcpt_Object = MibTableColumn
ruckusAAANumSuccDmAcpt = _RuckusAAANumSuccDmAcpt_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 3, 1, 1, 1, 1, 1, 23),
    _RuckusAAANumSuccDmAcpt_Type()
)
ruckusAAANumSuccDmAcpt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusAAANumSuccDmAcpt.setStatus("current")
_RuckusAAANumFailDmAcpt_Type = Counter64
_RuckusAAANumFailDmAcpt_Object = MibTableColumn
ruckusAAANumFailDmAcpt = _RuckusAAANumFailDmAcpt_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 3, 1, 1, 1, 1, 1, 24),
    _RuckusAAANumFailDmAcpt_Type()
)
ruckusAAANumFailDmAcpt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusAAANumFailDmAcpt.setStatus("current")
_RuckusAAAIndex_Type = Integer32
_RuckusAAAIndex_Object = MibTableColumn
ruckusAAAIndex = _RuckusAAAIndex_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 3, 1, 1, 1, 1, 1, 99),
    _RuckusAAAIndex_Type()
)
ruckusAAAIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusAAAIndex.setStatus("current")
_RuckusAAAProxyInfo_ObjectIdentity = ObjectIdentity
ruckusAAAProxyInfo = _RuckusAAAProxyInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 3, 1, 1, 2)
)
_RuckusAAAProxyTable_Object = MibTable
ruckusAAAProxyTable = _RuckusAAAProxyTable_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 3, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    ruckusAAAProxyTable.setStatus("current")
_RuckusAAAProxyEntry_Object = MibTableRow
ruckusAAAProxyEntry = _RuckusAAAProxyEntry_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 3, 1, 1, 2, 1, 1)
)
ruckusAAAProxyEntry.setIndexNames(
    (0, "RUCKUS-SCG-TTG-MIB", "ruckusAAAProxyIndex"),
)
if mibBuilder.loadTexts:
    ruckusAAAProxyEntry.setStatus("current")
_RuckusAAAProxyAaaIp_Type = DisplayString
_RuckusAAAProxyAaaIp_Object = MibTableColumn
ruckusAAAProxyAaaIp = _RuckusAAAProxyAaaIp_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 3, 1, 1, 2, 1, 1, 1),
    _RuckusAAAProxyAaaIp_Type()
)
ruckusAAAProxyAaaIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusAAAProxyAaaIp.setStatus("current")
_RuckusAAAProxyNumSuccAuth_Type = Counter64
_RuckusAAAProxyNumSuccAuth_Object = MibTableColumn
ruckusAAAProxyNumSuccAuth = _RuckusAAAProxyNumSuccAuth_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 3, 1, 1, 2, 1, 1, 2),
    _RuckusAAAProxyNumSuccAuth_Type()
)
ruckusAAAProxyNumSuccAuth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusAAAProxyNumSuccAuth.setStatus("current")
_RuckusAAAProxyNumFailAuth_Type = Counter64
_RuckusAAAProxyNumFailAuth_Object = MibTableColumn
ruckusAAAProxyNumFailAuth = _RuckusAAAProxyNumFailAuth_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 3, 1, 1, 2, 1, 1, 3),
    _RuckusAAAProxyNumFailAuth_Type()
)
ruckusAAAProxyNumFailAuth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusAAAProxyNumFailAuth.setStatus("current")
_RuckusAAAProxyNumIncmpltAuth_Type = Counter64
_RuckusAAAProxyNumIncmpltAuth_Object = MibTableColumn
ruckusAAAProxyNumIncmpltAuth = _RuckusAAAProxyNumIncmpltAuth_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 3, 1, 1, 2, 1, 1, 4),
    _RuckusAAAProxyNumIncmpltAuth_Type()
)
ruckusAAAProxyNumIncmpltAuth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusAAAProxyNumIncmpltAuth.setStatus("current")
_RuckusAAAProxyNumSuccAcc_Type = Counter64
_RuckusAAAProxyNumSuccAcc_Object = MibTableColumn
ruckusAAAProxyNumSuccAcc = _RuckusAAAProxyNumSuccAcc_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 3, 1, 1, 2, 1, 1, 5),
    _RuckusAAAProxyNumSuccAcc_Type()
)
ruckusAAAProxyNumSuccAcc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusAAAProxyNumSuccAcc.setStatus("current")
_RuckusAAAProxyNumFailAcc_Type = Counter64
_RuckusAAAProxyNumFailAcc_Object = MibTableColumn
ruckusAAAProxyNumFailAcc = _RuckusAAAProxyNumFailAcc_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 3, 1, 1, 2, 1, 1, 6),
    _RuckusAAAProxyNumFailAcc_Type()
)
ruckusAAAProxyNumFailAcc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusAAAProxyNumFailAcc.setStatus("current")
_RuckusAAAProxyNumAcsRqRcvdNas_Type = Counter64
_RuckusAAAProxyNumAcsRqRcvdNas_Object = MibTableColumn
ruckusAAAProxyNumAcsRqRcvdNas = _RuckusAAAProxyNumAcsRqRcvdNas_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 3, 1, 1, 2, 1, 1, 7),
    _RuckusAAAProxyNumAcsRqRcvdNas_Type()
)
ruckusAAAProxyNumAcsRqRcvdNas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusAAAProxyNumAcsRqRcvdNas.setStatus("current")
_RuckusAAAProxyNumAcsRqSntAaa_Type = Counter64
_RuckusAAAProxyNumAcsRqSntAaa_Object = MibTableColumn
ruckusAAAProxyNumAcsRqSntAaa = _RuckusAAAProxyNumAcsRqSntAaa_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 3, 1, 1, 2, 1, 1, 8),
    _RuckusAAAProxyNumAcsRqSntAaa_Type()
)
ruckusAAAProxyNumAcsRqSntAaa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusAAAProxyNumAcsRqSntAaa.setStatus("current")
_RuckusAAAProxyNumAcsChRcvdAaa_Type = Counter64
_RuckusAAAProxyNumAcsChRcvdAaa_Object = MibTableColumn
ruckusAAAProxyNumAcsChRcvdAaa = _RuckusAAAProxyNumAcsChRcvdAaa_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 3, 1, 1, 2, 1, 1, 9),
    _RuckusAAAProxyNumAcsChRcvdAaa_Type()
)
ruckusAAAProxyNumAcsChRcvdAaa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusAAAProxyNumAcsChRcvdAaa.setStatus("current")
_RuckusAAAProxyNumAcsChSntNas_Type = Counter64
_RuckusAAAProxyNumAcsChSntNas_Object = MibTableColumn
ruckusAAAProxyNumAcsChSntNas = _RuckusAAAProxyNumAcsChSntNas_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 3, 1, 1, 2, 1, 1, 10),
    _RuckusAAAProxyNumAcsChSntNas_Type()
)
ruckusAAAProxyNumAcsChSntNas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusAAAProxyNumAcsChSntNas.setStatus("current")
_RuckusAAAProxyNumAcsAcpRcvdAaa_Type = Counter64
_RuckusAAAProxyNumAcsAcpRcvdAaa_Object = MibTableColumn
ruckusAAAProxyNumAcsAcpRcvdAaa = _RuckusAAAProxyNumAcsAcpRcvdAaa_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 3, 1, 1, 2, 1, 1, 11),
    _RuckusAAAProxyNumAcsAcpRcvdAaa_Type()
)
ruckusAAAProxyNumAcsAcpRcvdAaa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusAAAProxyNumAcsAcpRcvdAaa.setStatus("current")
_RuckusAAAProxyNumAcsAcpSntNas_Type = Counter64
_RuckusAAAProxyNumAcsAcpSntNas_Object = MibTableColumn
ruckusAAAProxyNumAcsAcpSntNas = _RuckusAAAProxyNumAcsAcpSntNas_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 3, 1, 1, 2, 1, 1, 12),
    _RuckusAAAProxyNumAcsAcpSntNas_Type()
)
ruckusAAAProxyNumAcsAcpSntNas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusAAAProxyNumAcsAcpSntNas.setStatus("current")
_RuckusAAAProxyNumAcsRejRcvdAaa_Type = Counter64
_RuckusAAAProxyNumAcsRejRcvdAaa_Object = MibTableColumn
ruckusAAAProxyNumAcsRejRcvdAaa = _RuckusAAAProxyNumAcsRejRcvdAaa_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 3, 1, 1, 2, 1, 1, 13),
    _RuckusAAAProxyNumAcsRejRcvdAaa_Type()
)
ruckusAAAProxyNumAcsRejRcvdAaa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusAAAProxyNumAcsRejRcvdAaa.setStatus("current")
_RuckusAAAProxyNumAcsRejSntNas_Type = Counter64
_RuckusAAAProxyNumAcsRejSntNas_Object = MibTableColumn
ruckusAAAProxyNumAcsRejSntNas = _RuckusAAAProxyNumAcsRejSntNas_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 3, 1, 1, 2, 1, 1, 14),
    _RuckusAAAProxyNumAcsRejSntNas_Type()
)
ruckusAAAProxyNumAcsRejSntNas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusAAAProxyNumAcsRejSntNas.setStatus("current")
_RuckusAAAProxyNumAccRqRcvdNas_Type = Counter64
_RuckusAAAProxyNumAccRqRcvdNas_Object = MibTableColumn
ruckusAAAProxyNumAccRqRcvdNas = _RuckusAAAProxyNumAccRqRcvdNas_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 3, 1, 1, 2, 1, 1, 15),
    _RuckusAAAProxyNumAccRqRcvdNas_Type()
)
ruckusAAAProxyNumAccRqRcvdNas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusAAAProxyNumAccRqRcvdNas.setStatus("current")
_RuckusAAAProxyNumAccRqSntAaa_Type = Counter64
_RuckusAAAProxyNumAccRqSntAaa_Object = MibTableColumn
ruckusAAAProxyNumAccRqSntAaa = _RuckusAAAProxyNumAccRqSntAaa_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 3, 1, 1, 2, 1, 1, 16),
    _RuckusAAAProxyNumAccRqSntAaa_Type()
)
ruckusAAAProxyNumAccRqSntAaa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusAAAProxyNumAccRqSntAaa.setStatus("current")
_RuckusAAAProxyNumAccRspRcdAaa_Type = Counter64
_RuckusAAAProxyNumAccRspRcdAaa_Object = MibTableColumn
ruckusAAAProxyNumAccRspRcdAaa = _RuckusAAAProxyNumAccRspRcdAaa_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 3, 1, 1, 2, 1, 1, 17),
    _RuckusAAAProxyNumAccRspRcdAaa_Type()
)
ruckusAAAProxyNumAccRspRcdAaa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusAAAProxyNumAccRspRcdAaa.setStatus("current")
_RuckusAAAProxyNumAccRspSntNas_Type = Counter64
_RuckusAAAProxyNumAccRspSntNas_Object = MibTableColumn
ruckusAAAProxyNumAccRspSntNas = _RuckusAAAProxyNumAccRspSntNas_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 3, 1, 1, 2, 1, 1, 18),
    _RuckusAAAProxyNumAccRspSntNas_Type()
)
ruckusAAAProxyNumAccRspSntNas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusAAAProxyNumAccRspSntNas.setStatus("current")
_RuckusAAAProxyNumCoaRcvdAaa_Type = Counter64
_RuckusAAAProxyNumCoaRcvdAaa_Object = MibTableColumn
ruckusAAAProxyNumCoaRcvdAaa = _RuckusAAAProxyNumCoaRcvdAaa_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 3, 1, 1, 2, 1, 1, 19),
    _RuckusAAAProxyNumCoaRcvdAaa_Type()
)
ruckusAAAProxyNumCoaRcvdAaa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusAAAProxyNumCoaRcvdAaa.setStatus("current")
_RuckusAAAProxyNumCoaSucSntAaa_Type = Counter64
_RuckusAAAProxyNumCoaSucSntAaa_Object = MibTableColumn
ruckusAAAProxyNumCoaSucSntAaa = _RuckusAAAProxyNumCoaSucSntAaa_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 3, 1, 1, 2, 1, 1, 20),
    _RuckusAAAProxyNumCoaSucSntAaa_Type()
)
ruckusAAAProxyNumCoaSucSntAaa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusAAAProxyNumCoaSucSntAaa.setStatus("current")
_RuckusAAAProxyNumCoaFailSntAaa_Type = Counter64
_RuckusAAAProxyNumCoaFailSntAaa_Object = MibTableColumn
ruckusAAAProxyNumCoaFailSntAaa = _RuckusAAAProxyNumCoaFailSntAaa_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 3, 1, 1, 2, 1, 1, 21),
    _RuckusAAAProxyNumCoaFailSntAaa_Type()
)
ruckusAAAProxyNumCoaFailSntAaa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusAAAProxyNumCoaFailSntAaa.setStatus("current")
_RuckusAAAProxyNumDmRcvdAaa_Type = Counter64
_RuckusAAAProxyNumDmRcvdAaa_Object = MibTableColumn
ruckusAAAProxyNumDmRcvdAaa = _RuckusAAAProxyNumDmRcvdAaa_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 3, 1, 1, 2, 1, 1, 22),
    _RuckusAAAProxyNumDmRcvdAaa_Type()
)
ruckusAAAProxyNumDmRcvdAaa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusAAAProxyNumDmRcvdAaa.setStatus("current")
_RuckusAAAProxyNumDmSntNas_Type = Counter64
_RuckusAAAProxyNumDmSntNas_Object = MibTableColumn
ruckusAAAProxyNumDmSntNas = _RuckusAAAProxyNumDmSntNas_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 3, 1, 1, 2, 1, 1, 23),
    _RuckusAAAProxyNumDmSntNas_Type()
)
ruckusAAAProxyNumDmSntNas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusAAAProxyNumDmSntNas.setStatus("current")
_RuckusAAAProxyNumDmSucRcdNas_Type = Counter64
_RuckusAAAProxyNumDmSucRcdNas_Object = MibTableColumn
ruckusAAAProxyNumDmSucRcdNas = _RuckusAAAProxyNumDmSucRcdNas_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 3, 1, 1, 2, 1, 1, 24),
    _RuckusAAAProxyNumDmSucRcdNas_Type()
)
ruckusAAAProxyNumDmSucRcdNas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusAAAProxyNumDmSucRcdNas.setStatus("current")
_RuckusAAAProxyNumDmSucSntAaa_Type = Counter64
_RuckusAAAProxyNumDmSucSntAaa_Object = MibTableColumn
ruckusAAAProxyNumDmSucSntAaa = _RuckusAAAProxyNumDmSucSntAaa_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 3, 1, 1, 2, 1, 1, 25),
    _RuckusAAAProxyNumDmSucSntAaa_Type()
)
ruckusAAAProxyNumDmSucSntAaa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusAAAProxyNumDmSucSntAaa.setStatus("current")
_RuckusAAAProxyNumDmFailRcdNas_Type = Counter64
_RuckusAAAProxyNumDmFailRcdNas_Object = MibTableColumn
ruckusAAAProxyNumDmFailRcdNas = _RuckusAAAProxyNumDmFailRcdNas_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 3, 1, 1, 2, 1, 1, 26),
    _RuckusAAAProxyNumDmFailRcdNas_Type()
)
ruckusAAAProxyNumDmFailRcdNas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusAAAProxyNumDmFailRcdNas.setStatus("current")
_RuckusAAAProxyNumDmFailSntAaa_Type = Counter64
_RuckusAAAProxyNumDmFailSntAaa_Object = MibTableColumn
ruckusAAAProxyNumDmFailSntAaa = _RuckusAAAProxyNumDmFailSntAaa_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 3, 1, 1, 2, 1, 1, 27),
    _RuckusAAAProxyNumDmFailSntAaa_Type()
)
ruckusAAAProxyNumDmFailSntAaa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusAAAProxyNumDmFailSntAaa.setStatus("current")
_RuckusAAAProxyIndex_Type = Integer32
_RuckusAAAProxyIndex_Object = MibTableColumn
ruckusAAAProxyIndex = _RuckusAAAProxyIndex_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 3, 1, 1, 2, 1, 1, 99),
    _RuckusAAAProxyIndex_Type()
)
ruckusAAAProxyIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusAAAProxyIndex.setStatus("current")
_RuckusCGFInfo_ObjectIdentity = ObjectIdentity
ruckusCGFInfo = _RuckusCGFInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 3, 1, 1, 3)
)
_RuckusCGFTable_Object = MibTable
ruckusCGFTable = _RuckusCGFTable_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 3, 1, 1, 3, 1)
)
if mibBuilder.loadTexts:
    ruckusCGFTable.setStatus("current")
_RuckusCGFEntry_Object = MibTableRow
ruckusCGFEntry = _RuckusCGFEntry_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 3, 1, 1, 3, 1, 1)
)
ruckusCGFEntry.setIndexNames(
    (0, "RUCKUS-SCG-TTG-MIB", "ruckusCGFIndex"),
)
if mibBuilder.loadTexts:
    ruckusCGFEntry.setStatus("current")
_RuckusCGFCgfSrvcName_Type = DisplayString
_RuckusCGFCgfSrvcName_Object = MibTableColumn
ruckusCGFCgfSrvcName = _RuckusCGFCgfSrvcName_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 3, 1, 1, 3, 1, 1, 1),
    _RuckusCGFCgfSrvcName_Type()
)
ruckusCGFCgfSrvcName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCGFCgfSrvcName.setStatus("current")
_RuckusCGFCgfIp_Type = DisplayString
_RuckusCGFCgfIp_Object = MibTableColumn
ruckusCGFCgfIp = _RuckusCGFCgfIp_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 3, 1, 1, 3, 1, 1, 2),
    _RuckusCGFCgfIp_Type()
)
ruckusCGFCgfIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCGFCgfIp.setStatus("current")
_RuckusCGFNumSuccCdrTxfd_Type = Counter64
_RuckusCGFNumSuccCdrTxfd_Object = MibTableColumn
ruckusCGFNumSuccCdrTxfd = _RuckusCGFNumSuccCdrTxfd_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 3, 1, 1, 3, 1, 1, 3),
    _RuckusCGFNumSuccCdrTxfd_Type()
)
ruckusCGFNumSuccCdrTxfd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCGFNumSuccCdrTxfd.setStatus("current")
_RuckusCGFNumCdrTxfrFail_Type = Counter64
_RuckusCGFNumCdrTxfrFail_Object = MibTableColumn
ruckusCGFNumCdrTxfrFail = _RuckusCGFNumCdrTxfrFail_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 3, 1, 1, 3, 1, 1, 4),
    _RuckusCGFNumCdrTxfrFail_Type()
)
ruckusCGFNumCdrTxfrFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCGFNumCdrTxfrFail.setStatus("current")
_RuckusCGFNumCdrPossDup_Type = Counter64
_RuckusCGFNumCdrPossDup_Object = MibTableColumn
ruckusCGFNumCdrPossDup = _RuckusCGFNumCdrPossDup_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 3, 1, 1, 3, 1, 1, 5),
    _RuckusCGFNumCdrPossDup_Type()
)
ruckusCGFNumCdrPossDup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCGFNumCdrPossDup.setStatus("current")
_RuckusCGFNumCdrRlsReq_Type = Counter64
_RuckusCGFNumCdrRlsReq_Object = MibTableColumn
ruckusCGFNumCdrRlsReq = _RuckusCGFNumCdrRlsReq_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 3, 1, 1, 3, 1, 1, 6),
    _RuckusCGFNumCdrRlsReq_Type()
)
ruckusCGFNumCdrRlsReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCGFNumCdrRlsReq.setStatus("current")
_RuckusCGFNumCdrCnclReq_Type = Counter64
_RuckusCGFNumCdrCnclReq_Object = MibTableColumn
ruckusCGFNumCdrCnclReq = _RuckusCGFNumCdrCnclReq_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 3, 1, 1, 3, 1, 1, 7),
    _RuckusCGFNumCdrCnclReq_Type()
)
ruckusCGFNumCdrCnclReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCGFNumCdrCnclReq.setStatus("current")
_RuckusCGFNumDrtrReqSnt_Type = Counter64
_RuckusCGFNumDrtrReqSnt_Object = MibTableColumn
ruckusCGFNumDrtrReqSnt = _RuckusCGFNumDrtrReqSnt_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 3, 1, 1, 3, 1, 1, 8),
    _RuckusCGFNumDrtrReqSnt_Type()
)
ruckusCGFNumDrtrReqSnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCGFNumDrtrReqSnt.setStatus("current")
_RuckusCGFNumDrtrSucRspRcvd_Type = Counter64
_RuckusCGFNumDrtrSucRspRcvd_Object = MibTableColumn
ruckusCGFNumDrtrSucRspRcvd = _RuckusCGFNumDrtrSucRspRcvd_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 3, 1, 1, 3, 1, 1, 9),
    _RuckusCGFNumDrtrSucRspRcvd_Type()
)
ruckusCGFNumDrtrSucRspRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCGFNumDrtrSucRspRcvd.setStatus("current")
_RuckusCGFNumDrtrFailRspRcvd_Type = Counter64
_RuckusCGFNumDrtrFailRspRcvd_Object = MibTableColumn
ruckusCGFNumDrtrFailRspRcvd = _RuckusCGFNumDrtrFailRspRcvd_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 3, 1, 1, 3, 1, 1, 10),
    _RuckusCGFNumDrtrFailRspRcvd_Type()
)
ruckusCGFNumDrtrFailRspRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCGFNumDrtrFailRspRcvd.setStatus("current")
_RuckusCGFIndex_Type = Integer32
_RuckusCGFIndex_Object = MibTableColumn
ruckusCGFIndex = _RuckusCGFIndex_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 3, 1, 1, 3, 1, 1, 99),
    _RuckusCGFIndex_Type()
)
ruckusCGFIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusCGFIndex.setStatus("current")
_RuckusGTPUInfo_ObjectIdentity = ObjectIdentity
ruckusGTPUInfo = _RuckusGTPUInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 3, 1, 1, 4)
)
_RuckusGTPUTable_Object = MibTable
ruckusGTPUTable = _RuckusGTPUTable_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 3, 1, 1, 4, 1)
)
if mibBuilder.loadTexts:
    ruckusGTPUTable.setStatus("current")
_RuckusGTPUEntry_Object = MibTableRow
ruckusGTPUEntry = _RuckusGTPUEntry_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 3, 1, 1, 4, 1, 1)
)
ruckusGTPUEntry.setIndexNames(
    (0, "RUCKUS-SCG-TTG-MIB", "ruckusGTPUIndex"),
)
if mibBuilder.loadTexts:
    ruckusGTPUEntry.setStatus("current")
_RuckusGTPUGgsnIPAddr_Type = DisplayString
_RuckusGTPUGgsnIPAddr_Object = MibTableColumn
ruckusGTPUGgsnIPAddr = _RuckusGTPUGgsnIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 3, 1, 1, 4, 1, 1, 1),
    _RuckusGTPUGgsnIPAddr_Type()
)
ruckusGTPUGgsnIPAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusGTPUGgsnIPAddr.setStatus("current")
_RuckusGTPUTxPkts_Type = Counter64
_RuckusGTPUTxPkts_Object = MibTableColumn
ruckusGTPUTxPkts = _RuckusGTPUTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 3, 1, 1, 4, 1, 1, 2),
    _RuckusGTPUTxPkts_Type()
)
ruckusGTPUTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusGTPUTxPkts.setStatus("current")
_RuckusGTPUTxBytes_Type = Counter64
_RuckusGTPUTxBytes_Object = MibTableColumn
ruckusGTPUTxBytes = _RuckusGTPUTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 3, 1, 1, 4, 1, 1, 3),
    _RuckusGTPUTxBytes_Type()
)
ruckusGTPUTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusGTPUTxBytes.setStatus("current")
_RuckusGTPURxPkts_Type = Counter64
_RuckusGTPURxPkts_Object = MibTableColumn
ruckusGTPURxPkts = _RuckusGTPURxPkts_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 3, 1, 1, 4, 1, 1, 4),
    _RuckusGTPURxPkts_Type()
)
ruckusGTPURxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusGTPURxPkts.setStatus("current")
_RuckusGTPURxBytes_Type = Counter64
_RuckusGTPURxBytes_Object = MibTableColumn
ruckusGTPURxBytes = _RuckusGTPURxBytes_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 3, 1, 1, 4, 1, 1, 5),
    _RuckusGTPURxBytes_Type()
)
ruckusGTPURxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusGTPURxBytes.setStatus("current")
_RuckusGTPUTxDrops_Type = Counter64
_RuckusGTPUTxDrops_Object = MibTableColumn
ruckusGTPUTxDrops = _RuckusGTPUTxDrops_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 3, 1, 1, 4, 1, 1, 6),
    _RuckusGTPUTxDrops_Type()
)
ruckusGTPUTxDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusGTPUTxDrops.setStatus("current")
_RuckusGTPURxDrops_Type = Counter64
_RuckusGTPURxDrops_Object = MibTableColumn
ruckusGTPURxDrops = _RuckusGTPURxDrops_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 3, 1, 1, 4, 1, 1, 7),
    _RuckusGTPURxDrops_Type()
)
ruckusGTPURxDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusGTPURxDrops.setStatus("current")
_RuckusGTPUNumBadGTPU_Type = Counter64
_RuckusGTPUNumBadGTPU_Object = MibTableColumn
ruckusGTPUNumBadGTPU = _RuckusGTPUNumBadGTPU_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 3, 1, 1, 4, 1, 1, 8),
    _RuckusGTPUNumBadGTPU_Type()
)
ruckusGTPUNumBadGTPU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusGTPUNumBadGTPU.setStatus("current")
_RuckusGTPUNumRXTeidInvalid_Type = Counter64
_RuckusGTPUNumRXTeidInvalid_Object = MibTableColumn
ruckusGTPUNumRXTeidInvalid = _RuckusGTPUNumRXTeidInvalid_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 3, 1, 1, 4, 1, 1, 9),
    _RuckusGTPUNumRXTeidInvalid_Type()
)
ruckusGTPUNumRXTeidInvalid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusGTPUNumRXTeidInvalid.setStatus("current")
_RuckusGTPUNumTXTeidInvalid_Type = Counter64
_RuckusGTPUNumTXTeidInvalid_Object = MibTableColumn
ruckusGTPUNumTXTeidInvalid = _RuckusGTPUNumTXTeidInvalid_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 3, 1, 1, 4, 1, 1, 10),
    _RuckusGTPUNumTXTeidInvalid_Type()
)
ruckusGTPUNumTXTeidInvalid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusGTPUNumTXTeidInvalid.setStatus("current")
_RuckusGTPUNumOfEchoRX_Type = Counter64
_RuckusGTPUNumOfEchoRX_Object = MibTableColumn
ruckusGTPUNumOfEchoRX = _RuckusGTPUNumOfEchoRX_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 3, 1, 1, 4, 1, 1, 11),
    _RuckusGTPUNumOfEchoRX_Type()
)
ruckusGTPUNumOfEchoRX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusGTPUNumOfEchoRX.setStatus("current")
_RuckusGTPUIndex_Type = Integer32
_RuckusGTPUIndex_Object = MibTableColumn
ruckusGTPUIndex = _RuckusGTPUIndex_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 3, 1, 1, 4, 1, 1, 99),
    _RuckusGTPUIndex_Type()
)
ruckusGTPUIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusGTPUIndex.setStatus("current")
_RuckusGGSNGTPCInfo_ObjectIdentity = ObjectIdentity
ruckusGGSNGTPCInfo = _RuckusGGSNGTPCInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 3, 1, 1, 5)
)
_RuckusGGSNGTPCTable_Object = MibTable
ruckusGGSNGTPCTable = _RuckusGGSNGTPCTable_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 3, 1, 1, 5, 1)
)
if mibBuilder.loadTexts:
    ruckusGGSNGTPCTable.setStatus("current")
_RuckusGGSNGTPCEntry_Object = MibTableRow
ruckusGGSNGTPCEntry = _RuckusGGSNGTPCEntry_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 3, 1, 1, 5, 1, 1)
)
ruckusGGSNGTPCEntry.setIndexNames(
    (0, "RUCKUS-SCG-TTG-MIB", "ruckusGGSNGTPCIndex"),
)
if mibBuilder.loadTexts:
    ruckusGGSNGTPCEntry.setStatus("current")
_RuckusGGSNGTPCGgsnIp_Type = DisplayString
_RuckusGGSNGTPCGgsnIp_Object = MibTableColumn
ruckusGGSNGTPCGgsnIp = _RuckusGGSNGTPCGgsnIp_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 3, 1, 1, 5, 1, 1, 1),
    _RuckusGGSNGTPCGgsnIp_Type()
)
ruckusGGSNGTPCGgsnIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusGGSNGTPCGgsnIp.setStatus("current")
_RuckusGGSNGTPCNumActPdp_Type = Counter64
_RuckusGGSNGTPCNumActPdp_Object = MibTableColumn
ruckusGGSNGTPCNumActPdp = _RuckusGGSNGTPCNumActPdp_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 3, 1, 1, 5, 1, 1, 2),
    _RuckusGGSNGTPCNumActPdp_Type()
)
ruckusGGSNGTPCNumActPdp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusGGSNGTPCNumActPdp.setStatus("current")
_RuckusGGSNGTPCSuccPdpCrt_Type = Counter64
_RuckusGGSNGTPCSuccPdpCrt_Object = MibTableColumn
ruckusGGSNGTPCSuccPdpCrt = _RuckusGGSNGTPCSuccPdpCrt_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 3, 1, 1, 5, 1, 1, 3),
    _RuckusGGSNGTPCSuccPdpCrt_Type()
)
ruckusGGSNGTPCSuccPdpCrt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusGGSNGTPCSuccPdpCrt.setStatus("current")
_RuckusGGSNGTPCFailPdpCrt_Type = Counter64
_RuckusGGSNGTPCFailPdpCrt_Object = MibTableColumn
ruckusGGSNGTPCFailPdpCrt = _RuckusGGSNGTPCFailPdpCrt_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 3, 1, 1, 5, 1, 1, 4),
    _RuckusGGSNGTPCFailPdpCrt_Type()
)
ruckusGGSNGTPCFailPdpCrt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusGGSNGTPCFailPdpCrt.setStatus("current")
_RuckusGGSNGTPCSuccPdpUpdRcvd_Type = Counter64
_RuckusGGSNGTPCSuccPdpUpdRcvd_Object = MibTableColumn
ruckusGGSNGTPCSuccPdpUpdRcvd = _RuckusGGSNGTPCSuccPdpUpdRcvd_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 3, 1, 1, 5, 1, 1, 5),
    _RuckusGGSNGTPCSuccPdpUpdRcvd_Type()
)
ruckusGGSNGTPCSuccPdpUpdRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusGGSNGTPCSuccPdpUpdRcvd.setStatus("current")
_RuckusGGSNGTPCFailPdpUpdRcvd_Type = Counter64
_RuckusGGSNGTPCFailPdpUpdRcvd_Object = MibTableColumn
ruckusGGSNGTPCFailPdpUpdRcvd = _RuckusGGSNGTPCFailPdpUpdRcvd_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 3, 1, 1, 5, 1, 1, 6),
    _RuckusGGSNGTPCFailPdpUpdRcvd_Type()
)
ruckusGGSNGTPCFailPdpUpdRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusGGSNGTPCFailPdpUpdRcvd.setStatus("current")
_RuckusGGSNGTPCSuccPdpUpdInitRM_Type = Counter64
_RuckusGGSNGTPCSuccPdpUpdInitRM_Object = MibTableColumn
ruckusGGSNGTPCSuccPdpUpdInitRM = _RuckusGGSNGTPCSuccPdpUpdInitRM_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 3, 1, 1, 5, 1, 1, 7),
    _RuckusGGSNGTPCSuccPdpUpdInitRM_Type()
)
ruckusGGSNGTPCSuccPdpUpdInitRM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusGGSNGTPCSuccPdpUpdInitRM.setStatus("current")
_RuckusGGSNGTPCFailPdpUpdInitRM_Type = Counter64
_RuckusGGSNGTPCFailPdpUpdInitRM_Object = MibTableColumn
ruckusGGSNGTPCFailPdpUpdInitRM = _RuckusGGSNGTPCFailPdpUpdInitRM_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 3, 1, 1, 5, 1, 1, 8),
    _RuckusGGSNGTPCFailPdpUpdInitRM_Type()
)
ruckusGGSNGTPCFailPdpUpdInitRM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusGGSNGTPCFailPdpUpdInitRM.setStatus("current")
_RuckusGGSNGTPCSuccPdpUpdInitAAA_Type = Counter64
_RuckusGGSNGTPCSuccPdpUpdInitAAA_Object = MibTableColumn
ruckusGGSNGTPCSuccPdpUpdInitAAA = _RuckusGGSNGTPCSuccPdpUpdInitAAA_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 3, 1, 1, 5, 1, 1, 9),
    _RuckusGGSNGTPCSuccPdpUpdInitAAA_Type()
)
ruckusGGSNGTPCSuccPdpUpdInitAAA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusGGSNGTPCSuccPdpUpdInitAAA.setStatus("current")
_RuckusGGSNGTPCFailPdpUpdInitAAA_Type = Counter64
_RuckusGGSNGTPCFailPdpUpdInitAAA_Object = MibTableColumn
ruckusGGSNGTPCFailPdpUpdInitAAA = _RuckusGGSNGTPCFailPdpUpdInitAAA_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 3, 1, 1, 5, 1, 1, 10),
    _RuckusGGSNGTPCFailPdpUpdInitAAA_Type()
)
ruckusGGSNGTPCFailPdpUpdInitAAA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusGGSNGTPCFailPdpUpdInitAAA.setStatus("current")
_RuckusGGSNGTPCSuccPdpUpdInitHLR_Type = Counter64
_RuckusGGSNGTPCSuccPdpUpdInitHLR_Object = MibTableColumn
ruckusGGSNGTPCSuccPdpUpdInitHLR = _RuckusGGSNGTPCSuccPdpUpdInitHLR_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 3, 1, 1, 5, 1, 1, 11),
    _RuckusGGSNGTPCSuccPdpUpdInitHLR_Type()
)
ruckusGGSNGTPCSuccPdpUpdInitHLR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusGGSNGTPCSuccPdpUpdInitHLR.setStatus("current")
_RuckusGGSNGTPCFailPdpUpdInitHLR_Type = Counter64
_RuckusGGSNGTPCFailPdpUpdInitHLR_Object = MibTableColumn
ruckusGGSNGTPCFailPdpUpdInitHLR = _RuckusGGSNGTPCFailPdpUpdInitHLR_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 3, 1, 1, 5, 1, 1, 12),
    _RuckusGGSNGTPCFailPdpUpdInitHLR_Type()
)
ruckusGGSNGTPCFailPdpUpdInitHLR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusGGSNGTPCFailPdpUpdInitHLR.setStatus("current")
_RuckusGGSNGTPCSuccDelPdpRcvd_Type = Counter64
_RuckusGGSNGTPCSuccDelPdpRcvd_Object = MibTableColumn
ruckusGGSNGTPCSuccDelPdpRcvd = _RuckusGGSNGTPCSuccDelPdpRcvd_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 3, 1, 1, 5, 1, 1, 13),
    _RuckusGGSNGTPCSuccDelPdpRcvd_Type()
)
ruckusGGSNGTPCSuccDelPdpRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusGGSNGTPCSuccDelPdpRcvd.setStatus("current")
_RuckusGGSNGTPCFailDelPdpRcvd_Type = Counter64
_RuckusGGSNGTPCFailDelPdpRcvd_Object = MibTableColumn
ruckusGGSNGTPCFailDelPdpRcvd = _RuckusGGSNGTPCFailDelPdpRcvd_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 3, 1, 1, 5, 1, 1, 14),
    _RuckusGGSNGTPCFailDelPdpRcvd_Type()
)
ruckusGGSNGTPCFailDelPdpRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusGGSNGTPCFailDelPdpRcvd.setStatus("current")
_RuckusGGSNGTPCSuccDelPdpInitErr_Type = Counter64
_RuckusGGSNGTPCSuccDelPdpInitErr_Object = MibTableColumn
ruckusGGSNGTPCSuccDelPdpInitErr = _RuckusGGSNGTPCSuccDelPdpInitErr_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 3, 1, 1, 5, 1, 1, 15),
    _RuckusGGSNGTPCSuccDelPdpInitErr_Type()
)
ruckusGGSNGTPCSuccDelPdpInitErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusGGSNGTPCSuccDelPdpInitErr.setStatus("current")
_RuckusGGSNGTPCFailDelPdpInitErr_Type = Counter64
_RuckusGGSNGTPCFailDelPdpInitErr_Object = MibTableColumn
ruckusGGSNGTPCFailDelPdpInitErr = _RuckusGGSNGTPCFailDelPdpInitErr_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 3, 1, 1, 5, 1, 1, 16),
    _RuckusGGSNGTPCFailDelPdpInitErr_Type()
)
ruckusGGSNGTPCFailDelPdpInitErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusGGSNGTPCFailDelPdpInitErr.setStatus("current")
_RuckusGGSNGTPCSuccDelPdpInitDM_Type = Counter64
_RuckusGGSNGTPCSuccDelPdpInitDM_Object = MibTableColumn
ruckusGGSNGTPCSuccDelPdpInitDM = _RuckusGGSNGTPCSuccDelPdpInitDM_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 3, 1, 1, 5, 1, 1, 17),
    _RuckusGGSNGTPCSuccDelPdpInitDM_Type()
)
ruckusGGSNGTPCSuccDelPdpInitDM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusGGSNGTPCSuccDelPdpInitDM.setStatus("current")
_RuckusGGSNGTPCFailDelPdpInitDM_Type = Counter64
_RuckusGGSNGTPCFailDelPdpInitDM_Object = MibTableColumn
ruckusGGSNGTPCFailDelPdpInitDM = _RuckusGGSNGTPCFailDelPdpInitDM_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 3, 1, 1, 5, 1, 1, 18),
    _RuckusGGSNGTPCFailDelPdpInitDM_Type()
)
ruckusGGSNGTPCFailDelPdpInitDM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusGGSNGTPCFailDelPdpInitDM.setStatus("current")
_RuckusGGSNGTPCSuccDelPdpInitHLR_Type = Counter64
_RuckusGGSNGTPCSuccDelPdpInitHLR_Object = MibTableColumn
ruckusGGSNGTPCSuccDelPdpInitHLR = _RuckusGGSNGTPCSuccDelPdpInitHLR_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 3, 1, 1, 5, 1, 1, 19),
    _RuckusGGSNGTPCSuccDelPdpInitHLR_Type()
)
ruckusGGSNGTPCSuccDelPdpInitHLR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusGGSNGTPCSuccDelPdpInitHLR.setStatus("current")
_RuckusGGSNGTPCFailDelPdpInitHLR_Type = Counter64
_RuckusGGSNGTPCFailDelPdpInitHLR_Object = MibTableColumn
ruckusGGSNGTPCFailDelPdpInitHLR = _RuckusGGSNGTPCFailDelPdpInitHLR_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 3, 1, 1, 5, 1, 1, 20),
    _RuckusGGSNGTPCFailDelPdpInitHLR_Type()
)
ruckusGGSNGTPCFailDelPdpInitHLR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusGGSNGTPCFailDelPdpInitHLR.setStatus("current")
_RuckusGGSNGTPCSuccDelPdpInitSCG_Type = Counter64
_RuckusGGSNGTPCSuccDelPdpInitSCG_Object = MibTableColumn
ruckusGGSNGTPCSuccDelPdpInitSCG = _RuckusGGSNGTPCSuccDelPdpInitSCG_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 3, 1, 1, 5, 1, 1, 21),
    _RuckusGGSNGTPCSuccDelPdpInitSCG_Type()
)
ruckusGGSNGTPCSuccDelPdpInitSCG.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusGGSNGTPCSuccDelPdpInitSCG.setStatus("current")
_RuckusGGSNGTPCFailDelPdpInitSCG_Type = Counter64
_RuckusGGSNGTPCFailDelPdpInitSCG_Object = MibTableColumn
ruckusGGSNGTPCFailDelPdpInitSCG = _RuckusGGSNGTPCFailDelPdpInitSCG_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 3, 1, 1, 5, 1, 1, 22),
    _RuckusGGSNGTPCFailDelPdpInitSCG_Type()
)
ruckusGGSNGTPCFailDelPdpInitSCG.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusGGSNGTPCFailDelPdpInitSCG.setStatus("current")
_RuckusGGSNGTPCSuccDelPdpInitAP_Type = Counter64
_RuckusGGSNGTPCSuccDelPdpInitAP_Object = MibTableColumn
ruckusGGSNGTPCSuccDelPdpInitAP = _RuckusGGSNGTPCSuccDelPdpInitAP_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 3, 1, 1, 5, 1, 1, 23),
    _RuckusGGSNGTPCSuccDelPdpInitAP_Type()
)
ruckusGGSNGTPCSuccDelPdpInitAP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusGGSNGTPCSuccDelPdpInitAP.setStatus("current")
_RuckusGGSNGTPCFailDelPdpInitAP_Type = Counter64
_RuckusGGSNGTPCFailDelPdpInitAP_Object = MibTableColumn
ruckusGGSNGTPCFailDelPdpInitAP = _RuckusGGSNGTPCFailDelPdpInitAP_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 3, 1, 1, 5, 1, 1, 24),
    _RuckusGGSNGTPCFailDelPdpInitAP_Type()
)
ruckusGGSNGTPCFailDelPdpInitAP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusGGSNGTPCFailDelPdpInitAP.setStatus("current")
_RuckusGGSNGTPCSuccDelPdpInitD_Type = Counter64
_RuckusGGSNGTPCSuccDelPdpInitD_Object = MibTableColumn
ruckusGGSNGTPCSuccDelPdpInitD = _RuckusGGSNGTPCSuccDelPdpInitD_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 3, 1, 1, 5, 1, 1, 25),
    _RuckusGGSNGTPCSuccDelPdpInitD_Type()
)
ruckusGGSNGTPCSuccDelPdpInitD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusGGSNGTPCSuccDelPdpInitD.setStatus("current")
_RuckusGGSNGTPCFailDelPdpInitD_Type = Counter64
_RuckusGGSNGTPCFailDelPdpInitD_Object = MibTableColumn
ruckusGGSNGTPCFailDelPdpInitD = _RuckusGGSNGTPCFailDelPdpInitD_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 3, 1, 1, 5, 1, 1, 26),
    _RuckusGGSNGTPCFailDelPdpInitD_Type()
)
ruckusGGSNGTPCFailDelPdpInitD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusGGSNGTPCFailDelPdpInitD.setStatus("current")
_RuckusGGSNGTPCSuccDelPdpInitClnt_Type = Counter64
_RuckusGGSNGTPCSuccDelPdpInitClnt_Object = MibTableColumn
ruckusGGSNGTPCSuccDelPdpInitClnt = _RuckusGGSNGTPCSuccDelPdpInitClnt_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 3, 1, 1, 5, 1, 1, 27),
    _RuckusGGSNGTPCSuccDelPdpInitClnt_Type()
)
ruckusGGSNGTPCSuccDelPdpInitClnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusGGSNGTPCSuccDelPdpInitClnt.setStatus("current")
_RuckusGGSNGTPCFailDelPdpInitClnt_Type = Counter64
_RuckusGGSNGTPCFailDelPdpInitClnt_Object = MibTableColumn
ruckusGGSNGTPCFailDelPdpInitClnt = _RuckusGGSNGTPCFailDelPdpInitClnt_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 3, 1, 1, 5, 1, 1, 28),
    _RuckusGGSNGTPCFailDelPdpInitClnt_Type()
)
ruckusGGSNGTPCFailDelPdpInitClnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusGGSNGTPCFailDelPdpInitClnt.setStatus("current")
_RuckusGGSNGTPCIndex_Type = Integer32
_RuckusGGSNGTPCIndex_Object = MibTableColumn
ruckusGGSNGTPCIndex = _RuckusGGSNGTPCIndex_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 3, 1, 1, 5, 1, 1, 99),
    _RuckusGGSNGTPCIndex_Type()
)
ruckusGGSNGTPCIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusGGSNGTPCIndex.setStatus("current")
_RuckusHLRInfo_ObjectIdentity = ObjectIdentity
ruckusHLRInfo = _RuckusHLRInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 3, 1, 1, 7)
)
_RuckusHLRTable_Object = MibTable
ruckusHLRTable = _RuckusHLRTable_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 3, 1, 1, 7, 1)
)
if mibBuilder.loadTexts:
    ruckusHLRTable.setStatus("current")
_RuckusHLREntry_Object = MibTableRow
ruckusHLREntry = _RuckusHLREntry_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 3, 1, 1, 7, 1, 1)
)
ruckusHLREntry.setIndexNames(
    (0, "RUCKUS-SCG-TTG-MIB", "ruckusHLRIndex"),
)
if mibBuilder.loadTexts:
    ruckusHLREntry.setStatus("current")
_RuckusHLRHlrSrvcName_Type = DisplayString
_RuckusHLRHlrSrvcName_Object = MibTableColumn
ruckusHLRHlrSrvcName = _RuckusHLRHlrSrvcName_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 3, 1, 1, 7, 1, 1, 1),
    _RuckusHLRHlrSrvcName_Type()
)
ruckusHLRHlrSrvcName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusHLRHlrSrvcName.setStatus("current")
_RuckusHLRNumSucAuthInfoReqSim_Type = Counter64
_RuckusHLRNumSucAuthInfoReqSim_Object = MibTableColumn
ruckusHLRNumSucAuthInfoReqSim = _RuckusHLRNumSucAuthInfoReqSim_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 3, 1, 1, 7, 1, 1, 2),
    _RuckusHLRNumSucAuthInfoReqSim_Type()
)
ruckusHLRNumSucAuthInfoReqSim.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusHLRNumSucAuthInfoReqSim.setStatus("current")
_RuckusHLRNumAuthInfoRqErrHlrSim_Type = Counter64
_RuckusHLRNumAuthInfoRqErrHlrSim_Object = MibTableColumn
ruckusHLRNumAuthInfoRqErrHlrSim = _RuckusHLRNumAuthInfoRqErrHlrSim_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 3, 1, 1, 7, 1, 1, 3),
    _RuckusHLRNumAuthInfoRqErrHlrSim_Type()
)
ruckusHLRNumAuthInfoRqErrHlrSim.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusHLRNumAuthInfoRqErrHlrSim.setStatus("current")
_RuckusHLRNumAuthInfoRqTmotSim_Type = Counter64
_RuckusHLRNumAuthInfoRqTmotSim_Object = MibTableColumn
ruckusHLRNumAuthInfoRqTmotSim = _RuckusHLRNumAuthInfoRqTmotSim_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 3, 1, 1, 7, 1, 1, 4),
    _RuckusHLRNumAuthInfoRqTmotSim_Type()
)
ruckusHLRNumAuthInfoRqTmotSim.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusHLRNumAuthInfoRqTmotSim.setStatus("current")
_RuckusHLRNumSucAuthInfoReqAka_Type = Counter64
_RuckusHLRNumSucAuthInfoReqAka_Object = MibTableColumn
ruckusHLRNumSucAuthInfoReqAka = _RuckusHLRNumSucAuthInfoReqAka_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 3, 1, 1, 7, 1, 1, 5),
    _RuckusHLRNumSucAuthInfoReqAka_Type()
)
ruckusHLRNumSucAuthInfoReqAka.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusHLRNumSucAuthInfoReqAka.setStatus("current")
_RuckusHLRNumAuthInfoRqErrHlrAka_Type = Counter64
_RuckusHLRNumAuthInfoRqErrHlrAka_Object = MibTableColumn
ruckusHLRNumAuthInfoRqErrHlrAka = _RuckusHLRNumAuthInfoRqErrHlrAka_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 3, 1, 1, 7, 1, 1, 6),
    _RuckusHLRNumAuthInfoRqErrHlrAka_Type()
)
ruckusHLRNumAuthInfoRqErrHlrAka.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusHLRNumAuthInfoRqErrHlrAka.setStatus("current")
_RuckusHLRNumAuthInfoRqTmotAka_Type = Counter64
_RuckusHLRNumAuthInfoRqTmotAka_Object = MibTableColumn
ruckusHLRNumAuthInfoRqTmotAka = _RuckusHLRNumAuthInfoRqTmotAka_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 3, 1, 1, 7, 1, 1, 7),
    _RuckusHLRNumAuthInfoRqTmotAka_Type()
)
ruckusHLRNumAuthInfoRqTmotAka.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusHLRNumAuthInfoRqTmotAka.setStatus("current")
_RuckusHLRNumUpdGprsSuccSim_Type = Counter64
_RuckusHLRNumUpdGprsSuccSim_Object = MibTableColumn
ruckusHLRNumUpdGprsSuccSim = _RuckusHLRNumUpdGprsSuccSim_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 3, 1, 1, 7, 1, 1, 8),
    _RuckusHLRNumUpdGprsSuccSim_Type()
)
ruckusHLRNumUpdGprsSuccSim.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusHLRNumUpdGprsSuccSim.setStatus("current")
_RuckusHLRNumUpdGprsFailErrSim_Type = Counter64
_RuckusHLRNumUpdGprsFailErrSim_Object = MibTableColumn
ruckusHLRNumUpdGprsFailErrSim = _RuckusHLRNumUpdGprsFailErrSim_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 3, 1, 1, 7, 1, 1, 9),
    _RuckusHLRNumUpdGprsFailErrSim_Type()
)
ruckusHLRNumUpdGprsFailErrSim.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusHLRNumUpdGprsFailErrSim.setStatus("current")
_RuckusHLRNumUpdGprsFailTmoSim_Type = Counter64
_RuckusHLRNumUpdGprsFailTmoSim_Object = MibTableColumn
ruckusHLRNumUpdGprsFailTmoSim = _RuckusHLRNumUpdGprsFailTmoSim_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 3, 1, 1, 7, 1, 1, 10),
    _RuckusHLRNumUpdGprsFailTmoSim_Type()
)
ruckusHLRNumUpdGprsFailTmoSim.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusHLRNumUpdGprsFailTmoSim.setStatus("current")
_RuckusHLRNumUpdGprsSuccAka_Type = Counter64
_RuckusHLRNumUpdGprsSuccAka_Object = MibTableColumn
ruckusHLRNumUpdGprsSuccAka = _RuckusHLRNumUpdGprsSuccAka_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 3, 1, 1, 7, 1, 1, 11),
    _RuckusHLRNumUpdGprsSuccAka_Type()
)
ruckusHLRNumUpdGprsSuccAka.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusHLRNumUpdGprsSuccAka.setStatus("current")
_RuckusHLRNumUpdGprsFailErrAka_Type = Counter64
_RuckusHLRNumUpdGprsFailErrAka_Object = MibTableColumn
ruckusHLRNumUpdGprsFailErrAka = _RuckusHLRNumUpdGprsFailErrAka_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 3, 1, 1, 7, 1, 1, 12),
    _RuckusHLRNumUpdGprsFailErrAka_Type()
)
ruckusHLRNumUpdGprsFailErrAka.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusHLRNumUpdGprsFailErrAka.setStatus("current")
_RuckusHLRNumUpdGprsFailTmoAka_Type = Counter64
_RuckusHLRNumUpdGprsFailTmoAka_Object = MibTableColumn
ruckusHLRNumUpdGprsFailTmoAka = _RuckusHLRNumUpdGprsFailTmoAka_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 3, 1, 1, 7, 1, 1, 13),
    _RuckusHLRNumUpdGprsFailTmoAka_Type()
)
ruckusHLRNumUpdGprsFailTmoAka.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusHLRNumUpdGprsFailTmoAka.setStatus("current")
_RuckusHLRNumRstDtaSuccSim_Type = Counter64
_RuckusHLRNumRstDtaSuccSim_Object = MibTableColumn
ruckusHLRNumRstDtaSuccSim = _RuckusHLRNumRstDtaSuccSim_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 3, 1, 1, 7, 1, 1, 14),
    _RuckusHLRNumRstDtaSuccSim_Type()
)
ruckusHLRNumRstDtaSuccSim.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusHLRNumRstDtaSuccSim.setStatus("current")
_RuckusHLRNumRstDtaFailErrHlrSim_Type = Counter64
_RuckusHLRNumRstDtaFailErrHlrSim_Object = MibTableColumn
ruckusHLRNumRstDtaFailErrHlrSim = _RuckusHLRNumRstDtaFailErrHlrSim_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 3, 1, 1, 7, 1, 1, 15),
    _RuckusHLRNumRstDtaFailErrHlrSim_Type()
)
ruckusHLRNumRstDtaFailErrHlrSim.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusHLRNumRstDtaFailErrHlrSim.setStatus("current")
_RuckusHLRNumRstDtaFailTmoSim_Type = Counter64
_RuckusHLRNumRstDtaFailTmoSim_Object = MibTableColumn
ruckusHLRNumRstDtaFailTmoSim = _RuckusHLRNumRstDtaFailTmoSim_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 3, 1, 1, 7, 1, 1, 16),
    _RuckusHLRNumRstDtaFailTmoSim_Type()
)
ruckusHLRNumRstDtaFailTmoSim.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusHLRNumRstDtaFailTmoSim.setStatus("current")
_RuckusHLRNumRstDtaSuccAka_Type = Counter64
_RuckusHLRNumRstDtaSuccAka_Object = MibTableColumn
ruckusHLRNumRstDtaSuccAka = _RuckusHLRNumRstDtaSuccAka_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 3, 1, 1, 7, 1, 1, 17),
    _RuckusHLRNumRstDtaSuccAka_Type()
)
ruckusHLRNumRstDtaSuccAka.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusHLRNumRstDtaSuccAka.setStatus("current")
_RuckusHLRNumRstDtaFailErrHlrAka_Type = Counter64
_RuckusHLRNumRstDtaFailErrHlrAka_Object = MibTableColumn
ruckusHLRNumRstDtaFailErrHlrAka = _RuckusHLRNumRstDtaFailErrHlrAka_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 3, 1, 1, 7, 1, 1, 18),
    _RuckusHLRNumRstDtaFailErrHlrAka_Type()
)
ruckusHLRNumRstDtaFailErrHlrAka.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusHLRNumRstDtaFailErrHlrAka.setStatus("current")
_RuckusHLRNumRstDtaFailTmoAka_Type = Counter64
_RuckusHLRNumRstDtaFailTmoAka_Object = MibTableColumn
ruckusHLRNumRstDtaFailTmoAka = _RuckusHLRNumRstDtaFailTmoAka_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 3, 1, 1, 7, 1, 1, 19),
    _RuckusHLRNumRstDtaFailTmoAka_Type()
)
ruckusHLRNumRstDtaFailTmoAka.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusHLRNumRstDtaFailTmoAka.setStatus("current")
_RuckusHLRNumInsrtDtaSuccSim_Type = Counter64
_RuckusHLRNumInsrtDtaSuccSim_Object = MibTableColumn
ruckusHLRNumInsrtDtaSuccSim = _RuckusHLRNumInsrtDtaSuccSim_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 3, 1, 1, 7, 1, 1, 20),
    _RuckusHLRNumInsrtDtaSuccSim_Type()
)
ruckusHLRNumInsrtDtaSuccSim.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusHLRNumInsrtDtaSuccSim.setStatus("current")
_RuckusHLRNumInsrtDtaFailSim_Type = Counter64
_RuckusHLRNumInsrtDtaFailSim_Object = MibTableColumn
ruckusHLRNumInsrtDtaFailSim = _RuckusHLRNumInsrtDtaFailSim_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 3, 1, 1, 7, 1, 1, 21),
    _RuckusHLRNumInsrtDtaFailSim_Type()
)
ruckusHLRNumInsrtDtaFailSim.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusHLRNumInsrtDtaFailSim.setStatus("current")
_RuckusHLRNumInsrtDtaSuccAka_Type = Counter64
_RuckusHLRNumInsrtDtaSuccAka_Object = MibTableColumn
ruckusHLRNumInsrtDtaSuccAka = _RuckusHLRNumInsrtDtaSuccAka_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 3, 1, 1, 7, 1, 1, 22),
    _RuckusHLRNumInsrtDtaSuccAka_Type()
)
ruckusHLRNumInsrtDtaSuccAka.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusHLRNumInsrtDtaSuccAka.setStatus("current")
_RuckusHLRNumInsrtDtaFailAka_Type = Counter64
_RuckusHLRNumInsrtDtaFailAka_Object = MibTableColumn
ruckusHLRNumInsrtDtaFailAka = _RuckusHLRNumInsrtDtaFailAka_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 3, 1, 1, 7, 1, 1, 23),
    _RuckusHLRNumInsrtDtaFailAka_Type()
)
ruckusHLRNumInsrtDtaFailAka.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusHLRNumInsrtDtaFailAka.setStatus("current")
_RuckusHLRNumSaInsrtDtaSucc_Type = Counter64
_RuckusHLRNumSaInsrtDtaSucc_Object = MibTableColumn
ruckusHLRNumSaInsrtDtaSucc = _RuckusHLRNumSaInsrtDtaSucc_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 3, 1, 1, 7, 1, 1, 24),
    _RuckusHLRNumSaInsrtDtaSucc_Type()
)
ruckusHLRNumSaInsrtDtaSucc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusHLRNumSaInsrtDtaSucc.setStatus("current")
_RuckusHLRNumSaInsrtDtaFailUnkS_Type = Counter64
_RuckusHLRNumSaInsrtDtaFailUnkS_Object = MibTableColumn
ruckusHLRNumSaInsrtDtaFailUnkS = _RuckusHLRNumSaInsrtDtaFailUnkS_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 3, 1, 1, 7, 1, 1, 25),
    _RuckusHLRNumSaInsrtDtaFailUnkS_Type()
)
ruckusHLRNumSaInsrtDtaFailUnkS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusHLRNumSaInsrtDtaFailUnkS.setStatus("current")
_RuckusHLRNumSaInsrtDtaFailErr_Type = Counter64
_RuckusHLRNumSaInsrtDtaFailErr_Object = MibTableColumn
ruckusHLRNumSaInsrtDtaFailErr = _RuckusHLRNumSaInsrtDtaFailErr_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 3, 1, 1, 7, 1, 1, 26),
    _RuckusHLRNumSaInsrtDtaFailErr_Type()
)
ruckusHLRNumSaInsrtDtaFailErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusHLRNumSaInsrtDtaFailErr.setStatus("current")
_RuckusHLRNumCfgAssoc_Type = Counter64
_RuckusHLRNumCfgAssoc_Object = MibTableColumn
ruckusHLRNumCfgAssoc = _RuckusHLRNumCfgAssoc_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 3, 1, 1, 7, 1, 1, 27),
    _RuckusHLRNumCfgAssoc_Type()
)
ruckusHLRNumCfgAssoc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusHLRNumCfgAssoc.setStatus("current")
_RuckusHLRNumActAssoc_Type = Counter64
_RuckusHLRNumActAssoc_Object = MibTableColumn
ruckusHLRNumActAssoc = _RuckusHLRNumActAssoc_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 3, 1, 1, 7, 1, 1, 28),
    _RuckusHLRNumActAssoc_Type()
)
ruckusHLRNumActAssoc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusHLRNumActAssoc.setStatus("current")
_RuckusHLRNumRtgFail_Type = Counter64
_RuckusHLRNumRtgFail_Object = MibTableColumn
ruckusHLRNumRtgFail = _RuckusHLRNumRtgFail_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 3, 1, 1, 7, 1, 1, 29),
    _RuckusHLRNumRtgFail_Type()
)
ruckusHLRNumRtgFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusHLRNumRtgFail.setStatus("current")
_RuckusHLRIndex_Type = Integer32
_RuckusHLRIndex_Object = MibTableColumn
ruckusHLRIndex = _RuckusHLRIndex_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 3, 1, 1, 7, 1, 1, 99),
    _RuckusHLRIndex_Type()
)
ruckusHLRIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusHLRIndex.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RUCKUS-SCG-TTG-MIB",
    **{"ruckusTTGMIB": ruckusTTGMIB,
       "ruckusTTGObjects": ruckusTTGObjects,
       "ruckusAAAInfo": ruckusAAAInfo,
       "ruckusAAATable": ruckusAAATable,
       "ruckusAAAEntry": ruckusAAAEntry,
       "ruckusAAAAaaIp": ruckusAAAAaaIp,
       "ruckusAAANumSuccAuthPerm": ruckusAAANumSuccAuthPerm,
       "ruckusAAANumFailAuthPerm": ruckusAAANumFailAuthPerm,
       "ruckusAAANumSuccAuthPsd": ruckusAAANumSuccAuthPsd,
       "ruckusAAANumFailAuthPsd": ruckusAAANumFailAuthPsd,
       "ruckusAAANumSuccFastAuth": ruckusAAANumSuccFastAuth,
       "ruckusAAANumFailFastAuth": ruckusAAANumFailFastAuth,
       "ruckusAAANumAuthUnknPsd": ruckusAAANumAuthUnknPsd,
       "ruckusAAANumAuthUnknFR": ruckusAAANumAuthUnknFR,
       "ruckusAAANumIncompleteAuth": ruckusAAANumIncompleteAuth,
       "ruckusAAANumSuccAcc": ruckusAAANumSuccAcc,
       "ruckusAAANumFailAcc": ruckusAAANumFailAcc,
       "ruckusAAANumRadAcsRq": ruckusAAANumRadAcsRq,
       "ruckusAAANumRadAcsAcpt": ruckusAAANumRadAcsAcpt,
       "ruckusAAANumRadAcsChlg": ruckusAAANumRadAcsChlg,
       "ruckusAAANumRadAcsRej": ruckusAAANumRadAcsRej,
       "ruckusAAANumRadAccRq": ruckusAAANumRadAccRq,
       "ruckusAAANumRadAccAcpt": ruckusAAANumRadAccAcpt,
       "ruckusAAANumRadCoaRq": ruckusAAANumRadCoaRq,
       "ruckusAAANumSuccCoaAcpt": ruckusAAANumSuccCoaAcpt,
       "ruckusAAANumFailCoaAcpt": ruckusAAANumFailCoaAcpt,
       "ruckusAAANumRadDmRq": ruckusAAANumRadDmRq,
       "ruckusAAANumSuccDmAcpt": ruckusAAANumSuccDmAcpt,
       "ruckusAAANumFailDmAcpt": ruckusAAANumFailDmAcpt,
       "ruckusAAAIndex": ruckusAAAIndex,
       "ruckusAAAProxyInfo": ruckusAAAProxyInfo,
       "ruckusAAAProxyTable": ruckusAAAProxyTable,
       "ruckusAAAProxyEntry": ruckusAAAProxyEntry,
       "ruckusAAAProxyAaaIp": ruckusAAAProxyAaaIp,
       "ruckusAAAProxyNumSuccAuth": ruckusAAAProxyNumSuccAuth,
       "ruckusAAAProxyNumFailAuth": ruckusAAAProxyNumFailAuth,
       "ruckusAAAProxyNumIncmpltAuth": ruckusAAAProxyNumIncmpltAuth,
       "ruckusAAAProxyNumSuccAcc": ruckusAAAProxyNumSuccAcc,
       "ruckusAAAProxyNumFailAcc": ruckusAAAProxyNumFailAcc,
       "ruckusAAAProxyNumAcsRqRcvdNas": ruckusAAAProxyNumAcsRqRcvdNas,
       "ruckusAAAProxyNumAcsRqSntAaa": ruckusAAAProxyNumAcsRqSntAaa,
       "ruckusAAAProxyNumAcsChRcvdAaa": ruckusAAAProxyNumAcsChRcvdAaa,
       "ruckusAAAProxyNumAcsChSntNas": ruckusAAAProxyNumAcsChSntNas,
       "ruckusAAAProxyNumAcsAcpRcvdAaa": ruckusAAAProxyNumAcsAcpRcvdAaa,
       "ruckusAAAProxyNumAcsAcpSntNas": ruckusAAAProxyNumAcsAcpSntNas,
       "ruckusAAAProxyNumAcsRejRcvdAaa": ruckusAAAProxyNumAcsRejRcvdAaa,
       "ruckusAAAProxyNumAcsRejSntNas": ruckusAAAProxyNumAcsRejSntNas,
       "ruckusAAAProxyNumAccRqRcvdNas": ruckusAAAProxyNumAccRqRcvdNas,
       "ruckusAAAProxyNumAccRqSntAaa": ruckusAAAProxyNumAccRqSntAaa,
       "ruckusAAAProxyNumAccRspRcdAaa": ruckusAAAProxyNumAccRspRcdAaa,
       "ruckusAAAProxyNumAccRspSntNas": ruckusAAAProxyNumAccRspSntNas,
       "ruckusAAAProxyNumCoaRcvdAaa": ruckusAAAProxyNumCoaRcvdAaa,
       "ruckusAAAProxyNumCoaSucSntAaa": ruckusAAAProxyNumCoaSucSntAaa,
       "ruckusAAAProxyNumCoaFailSntAaa": ruckusAAAProxyNumCoaFailSntAaa,
       "ruckusAAAProxyNumDmRcvdAaa": ruckusAAAProxyNumDmRcvdAaa,
       "ruckusAAAProxyNumDmSntNas": ruckusAAAProxyNumDmSntNas,
       "ruckusAAAProxyNumDmSucRcdNas": ruckusAAAProxyNumDmSucRcdNas,
       "ruckusAAAProxyNumDmSucSntAaa": ruckusAAAProxyNumDmSucSntAaa,
       "ruckusAAAProxyNumDmFailRcdNas": ruckusAAAProxyNumDmFailRcdNas,
       "ruckusAAAProxyNumDmFailSntAaa": ruckusAAAProxyNumDmFailSntAaa,
       "ruckusAAAProxyIndex": ruckusAAAProxyIndex,
       "ruckusCGFInfo": ruckusCGFInfo,
       "ruckusCGFTable": ruckusCGFTable,
       "ruckusCGFEntry": ruckusCGFEntry,
       "ruckusCGFCgfSrvcName": ruckusCGFCgfSrvcName,
       "ruckusCGFCgfIp": ruckusCGFCgfIp,
       "ruckusCGFNumSuccCdrTxfd": ruckusCGFNumSuccCdrTxfd,
       "ruckusCGFNumCdrTxfrFail": ruckusCGFNumCdrTxfrFail,
       "ruckusCGFNumCdrPossDup": ruckusCGFNumCdrPossDup,
       "ruckusCGFNumCdrRlsReq": ruckusCGFNumCdrRlsReq,
       "ruckusCGFNumCdrCnclReq": ruckusCGFNumCdrCnclReq,
       "ruckusCGFNumDrtrReqSnt": ruckusCGFNumDrtrReqSnt,
       "ruckusCGFNumDrtrSucRspRcvd": ruckusCGFNumDrtrSucRspRcvd,
       "ruckusCGFNumDrtrFailRspRcvd": ruckusCGFNumDrtrFailRspRcvd,
       "ruckusCGFIndex": ruckusCGFIndex,
       "ruckusGTPUInfo": ruckusGTPUInfo,
       "ruckusGTPUTable": ruckusGTPUTable,
       "ruckusGTPUEntry": ruckusGTPUEntry,
       "ruckusGTPUGgsnIPAddr": ruckusGTPUGgsnIPAddr,
       "ruckusGTPUTxPkts": ruckusGTPUTxPkts,
       "ruckusGTPUTxBytes": ruckusGTPUTxBytes,
       "ruckusGTPURxPkts": ruckusGTPURxPkts,
       "ruckusGTPURxBytes": ruckusGTPURxBytes,
       "ruckusGTPUTxDrops": ruckusGTPUTxDrops,
       "ruckusGTPURxDrops": ruckusGTPURxDrops,
       "ruckusGTPUNumBadGTPU": ruckusGTPUNumBadGTPU,
       "ruckusGTPUNumRXTeidInvalid": ruckusGTPUNumRXTeidInvalid,
       "ruckusGTPUNumTXTeidInvalid": ruckusGTPUNumTXTeidInvalid,
       "ruckusGTPUNumOfEchoRX": ruckusGTPUNumOfEchoRX,
       "ruckusGTPUIndex": ruckusGTPUIndex,
       "ruckusGGSNGTPCInfo": ruckusGGSNGTPCInfo,
       "ruckusGGSNGTPCTable": ruckusGGSNGTPCTable,
       "ruckusGGSNGTPCEntry": ruckusGGSNGTPCEntry,
       "ruckusGGSNGTPCGgsnIp": ruckusGGSNGTPCGgsnIp,
       "ruckusGGSNGTPCNumActPdp": ruckusGGSNGTPCNumActPdp,
       "ruckusGGSNGTPCSuccPdpCrt": ruckusGGSNGTPCSuccPdpCrt,
       "ruckusGGSNGTPCFailPdpCrt": ruckusGGSNGTPCFailPdpCrt,
       "ruckusGGSNGTPCSuccPdpUpdRcvd": ruckusGGSNGTPCSuccPdpUpdRcvd,
       "ruckusGGSNGTPCFailPdpUpdRcvd": ruckusGGSNGTPCFailPdpUpdRcvd,
       "ruckusGGSNGTPCSuccPdpUpdInitRM": ruckusGGSNGTPCSuccPdpUpdInitRM,
       "ruckusGGSNGTPCFailPdpUpdInitRM": ruckusGGSNGTPCFailPdpUpdInitRM,
       "ruckusGGSNGTPCSuccPdpUpdInitAAA": ruckusGGSNGTPCSuccPdpUpdInitAAA,
       "ruckusGGSNGTPCFailPdpUpdInitAAA": ruckusGGSNGTPCFailPdpUpdInitAAA,
       "ruckusGGSNGTPCSuccPdpUpdInitHLR": ruckusGGSNGTPCSuccPdpUpdInitHLR,
       "ruckusGGSNGTPCFailPdpUpdInitHLR": ruckusGGSNGTPCFailPdpUpdInitHLR,
       "ruckusGGSNGTPCSuccDelPdpRcvd": ruckusGGSNGTPCSuccDelPdpRcvd,
       "ruckusGGSNGTPCFailDelPdpRcvd": ruckusGGSNGTPCFailDelPdpRcvd,
       "ruckusGGSNGTPCSuccDelPdpInitErr": ruckusGGSNGTPCSuccDelPdpInitErr,
       "ruckusGGSNGTPCFailDelPdpInitErr": ruckusGGSNGTPCFailDelPdpInitErr,
       "ruckusGGSNGTPCSuccDelPdpInitDM": ruckusGGSNGTPCSuccDelPdpInitDM,
       "ruckusGGSNGTPCFailDelPdpInitDM": ruckusGGSNGTPCFailDelPdpInitDM,
       "ruckusGGSNGTPCSuccDelPdpInitHLR": ruckusGGSNGTPCSuccDelPdpInitHLR,
       "ruckusGGSNGTPCFailDelPdpInitHLR": ruckusGGSNGTPCFailDelPdpInitHLR,
       "ruckusGGSNGTPCSuccDelPdpInitSCG": ruckusGGSNGTPCSuccDelPdpInitSCG,
       "ruckusGGSNGTPCFailDelPdpInitSCG": ruckusGGSNGTPCFailDelPdpInitSCG,
       "ruckusGGSNGTPCSuccDelPdpInitAP": ruckusGGSNGTPCSuccDelPdpInitAP,
       "ruckusGGSNGTPCFailDelPdpInitAP": ruckusGGSNGTPCFailDelPdpInitAP,
       "ruckusGGSNGTPCSuccDelPdpInitD": ruckusGGSNGTPCSuccDelPdpInitD,
       "ruckusGGSNGTPCFailDelPdpInitD": ruckusGGSNGTPCFailDelPdpInitD,
       "ruckusGGSNGTPCSuccDelPdpInitClnt": ruckusGGSNGTPCSuccDelPdpInitClnt,
       "ruckusGGSNGTPCFailDelPdpInitClnt": ruckusGGSNGTPCFailDelPdpInitClnt,
       "ruckusGGSNGTPCIndex": ruckusGGSNGTPCIndex,
       "ruckusHLRInfo": ruckusHLRInfo,
       "ruckusHLRTable": ruckusHLRTable,
       "ruckusHLREntry": ruckusHLREntry,
       "ruckusHLRHlrSrvcName": ruckusHLRHlrSrvcName,
       "ruckusHLRNumSucAuthInfoReqSim": ruckusHLRNumSucAuthInfoReqSim,
       "ruckusHLRNumAuthInfoRqErrHlrSim": ruckusHLRNumAuthInfoRqErrHlrSim,
       "ruckusHLRNumAuthInfoRqTmotSim": ruckusHLRNumAuthInfoRqTmotSim,
       "ruckusHLRNumSucAuthInfoReqAka": ruckusHLRNumSucAuthInfoReqAka,
       "ruckusHLRNumAuthInfoRqErrHlrAka": ruckusHLRNumAuthInfoRqErrHlrAka,
       "ruckusHLRNumAuthInfoRqTmotAka": ruckusHLRNumAuthInfoRqTmotAka,
       "ruckusHLRNumUpdGprsSuccSim": ruckusHLRNumUpdGprsSuccSim,
       "ruckusHLRNumUpdGprsFailErrSim": ruckusHLRNumUpdGprsFailErrSim,
       "ruckusHLRNumUpdGprsFailTmoSim": ruckusHLRNumUpdGprsFailTmoSim,
       "ruckusHLRNumUpdGprsSuccAka": ruckusHLRNumUpdGprsSuccAka,
       "ruckusHLRNumUpdGprsFailErrAka": ruckusHLRNumUpdGprsFailErrAka,
       "ruckusHLRNumUpdGprsFailTmoAka": ruckusHLRNumUpdGprsFailTmoAka,
       "ruckusHLRNumRstDtaSuccSim": ruckusHLRNumRstDtaSuccSim,
       "ruckusHLRNumRstDtaFailErrHlrSim": ruckusHLRNumRstDtaFailErrHlrSim,
       "ruckusHLRNumRstDtaFailTmoSim": ruckusHLRNumRstDtaFailTmoSim,
       "ruckusHLRNumRstDtaSuccAka": ruckusHLRNumRstDtaSuccAka,
       "ruckusHLRNumRstDtaFailErrHlrAka": ruckusHLRNumRstDtaFailErrHlrAka,
       "ruckusHLRNumRstDtaFailTmoAka": ruckusHLRNumRstDtaFailTmoAka,
       "ruckusHLRNumInsrtDtaSuccSim": ruckusHLRNumInsrtDtaSuccSim,
       "ruckusHLRNumInsrtDtaFailSim": ruckusHLRNumInsrtDtaFailSim,
       "ruckusHLRNumInsrtDtaSuccAka": ruckusHLRNumInsrtDtaSuccAka,
       "ruckusHLRNumInsrtDtaFailAka": ruckusHLRNumInsrtDtaFailAka,
       "ruckusHLRNumSaInsrtDtaSucc": ruckusHLRNumSaInsrtDtaSucc,
       "ruckusHLRNumSaInsrtDtaFailUnkS": ruckusHLRNumSaInsrtDtaFailUnkS,
       "ruckusHLRNumSaInsrtDtaFailErr": ruckusHLRNumSaInsrtDtaFailErr,
       "ruckusHLRNumCfgAssoc": ruckusHLRNumCfgAssoc,
       "ruckusHLRNumActAssoc": ruckusHLRNumActAssoc,
       "ruckusHLRNumRtgFail": ruckusHLRNumRtgFail,
       "ruckusHLRIndex": ruckusHLRIndex}
)
