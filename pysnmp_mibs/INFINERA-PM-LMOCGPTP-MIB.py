# SNMP MIB module (INFINERA-PM-LMOCGPTP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/INFINERA-PM-LMOCGPTP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:17:14 2025
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(perfMon,) = mibBuilder.importSymbols(
    "INFINERA-REG-MIB",
    "perfMon")

(FloatHundredths,) = mibBuilder.importSymbols(
    "INFINERA-TC-MIB",
    "FloatHundredths")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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

lmOcgPtpPmMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 32)
)
if mibBuilder.loadTexts:
    lmOcgPtpPmMIB.setRevisions(
        ("2008-10-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_LmOcgPtpPmRealTable_Object = MibTable
lmOcgPtpPmRealTable = _LmOcgPtpPmRealTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 32, 1)
)
if mibBuilder.loadTexts:
    lmOcgPtpPmRealTable.setStatus("current")
_LmOcgPtpPmRealEntry_Object = MibTableRow
lmOcgPtpPmRealEntry = _LmOcgPtpPmRealEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 32, 1, 1)
)
lmOcgPtpPmRealEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    lmOcgPtpPmRealEntry.setStatus("current")
_LmOcgPtpPmRealLmOcgOpt_Type = FloatHundredths
_LmOcgPtpPmRealLmOcgOpt_Object = MibTableColumn
lmOcgPtpPmRealLmOcgOpt = _LmOcgPtpPmRealLmOcgOpt_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 32, 1, 1, 1),
    _LmOcgPtpPmRealLmOcgOpt_Type()
)
lmOcgPtpPmRealLmOcgOpt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmOcgPtpPmRealLmOcgOpt.setStatus("current")
_LmOcgPtpPmRealLmOcgOpr_Type = FloatHundredths
_LmOcgPtpPmRealLmOcgOpr_Object = MibTableColumn
lmOcgPtpPmRealLmOcgOpr = _LmOcgPtpPmRealLmOcgOpr_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 32, 1, 1, 2),
    _LmOcgPtpPmRealLmOcgOpr_Type()
)
lmOcgPtpPmRealLmOcgOpr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmOcgPtpPmRealLmOcgOpr.setStatus("current")
_LmOcgPtpPmRealLmOcgTxEdfaOpr_Type = FloatHundredths
_LmOcgPtpPmRealLmOcgTxEdfaOpr_Object = MibTableColumn
lmOcgPtpPmRealLmOcgTxEdfaOpr = _LmOcgPtpPmRealLmOcgTxEdfaOpr_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 32, 1, 1, 3),
    _LmOcgPtpPmRealLmOcgTxEdfaOpr_Type()
)
lmOcgPtpPmRealLmOcgTxEdfaOpr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmOcgPtpPmRealLmOcgTxEdfaOpr.setStatus("current")
_LmOcgPtpPmRealLmOcgTxEdfaOpt_Type = FloatHundredths
_LmOcgPtpPmRealLmOcgTxEdfaOpt_Object = MibTableColumn
lmOcgPtpPmRealLmOcgTxEdfaOpt = _LmOcgPtpPmRealLmOcgTxEdfaOpt_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 32, 1, 1, 4),
    _LmOcgPtpPmRealLmOcgTxEdfaOpt_Type()
)
lmOcgPtpPmRealLmOcgTxEdfaOpt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmOcgPtpPmRealLmOcgTxEdfaOpt.setStatus("current")
_LmOcgPtpPmRealLmOcgTxEdfaLbc_Type = FloatHundredths
_LmOcgPtpPmRealLmOcgTxEdfaLbc_Object = MibTableColumn
lmOcgPtpPmRealLmOcgTxEdfaLbc = _LmOcgPtpPmRealLmOcgTxEdfaLbc_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 32, 1, 1, 5),
    _LmOcgPtpPmRealLmOcgTxEdfaLbc_Type()
)
lmOcgPtpPmRealLmOcgTxEdfaLbc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmOcgPtpPmRealLmOcgTxEdfaLbc.setStatus("current")
_LmOcgPtpPmRealLmOcgRxEdfaOpr_Type = FloatHundredths
_LmOcgPtpPmRealLmOcgRxEdfaOpr_Object = MibTableColumn
lmOcgPtpPmRealLmOcgRxEdfaOpr = _LmOcgPtpPmRealLmOcgRxEdfaOpr_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 32, 1, 1, 6),
    _LmOcgPtpPmRealLmOcgRxEdfaOpr_Type()
)
lmOcgPtpPmRealLmOcgRxEdfaOpr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmOcgPtpPmRealLmOcgRxEdfaOpr.setStatus("current")
_LmOcgPtpPmRealLmOcgRxEdfaOpt_Type = FloatHundredths
_LmOcgPtpPmRealLmOcgRxEdfaOpt_Object = MibTableColumn
lmOcgPtpPmRealLmOcgRxEdfaOpt = _LmOcgPtpPmRealLmOcgRxEdfaOpt_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 32, 1, 1, 7),
    _LmOcgPtpPmRealLmOcgRxEdfaOpt_Type()
)
lmOcgPtpPmRealLmOcgRxEdfaOpt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmOcgPtpPmRealLmOcgRxEdfaOpt.setStatus("current")
_LmOcgPtpPmRealLmOcgRxEdfaLbc_Type = FloatHundredths
_LmOcgPtpPmRealLmOcgRxEdfaLbc_Object = MibTableColumn
lmOcgPtpPmRealLmOcgRxEdfaLbc = _LmOcgPtpPmRealLmOcgRxEdfaLbc_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 32, 1, 1, 8),
    _LmOcgPtpPmRealLmOcgRxEdfaLbc_Type()
)
lmOcgPtpPmRealLmOcgRxEdfaLbc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmOcgPtpPmRealLmOcgRxEdfaLbc.setStatus("current")
_LmOcgPtpPmRealLmOcgPmd_Type = FloatHundredths
_LmOcgPtpPmRealLmOcgPmd_Object = MibTableColumn
lmOcgPtpPmRealLmOcgPmd = _LmOcgPtpPmRealLmOcgPmd_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 32, 1, 1, 9),
    _LmOcgPtpPmRealLmOcgPmd_Type()
)
lmOcgPtpPmRealLmOcgPmd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmOcgPtpPmRealLmOcgPmd.setStatus("current")
_LmOcgPtpPmRealLmOcgSoPmd_Type = FloatHundredths
_LmOcgPtpPmRealLmOcgSoPmd_Object = MibTableColumn
lmOcgPtpPmRealLmOcgSoPmd = _LmOcgPtpPmRealLmOcgSoPmd_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 32, 1, 1, 10),
    _LmOcgPtpPmRealLmOcgSoPmd_Type()
)
lmOcgPtpPmRealLmOcgSoPmd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmOcgPtpPmRealLmOcgSoPmd.setStatus("current")
_LmOcgPtpPmConformance_ObjectIdentity = ObjectIdentity
lmOcgPtpPmConformance = _LmOcgPtpPmConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 32, 3)
)
_LmOcgPtpPmCompliances_ObjectIdentity = ObjectIdentity
lmOcgPtpPmCompliances = _LmOcgPtpPmCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 32, 3, 1)
)
_LmOcgPtpPmGroups_ObjectIdentity = ObjectIdentity
lmOcgPtpPmGroups = _LmOcgPtpPmGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 32, 3, 2)
)

# Managed Objects groups

lmOcgPtpPmRealGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 32, 3, 2, 1)
)
lmOcgPtpPmRealGroup.setObjects(
      *(("INFINERA-PM-LMOCGPTP-MIB", "lmOcgPtpPmRealLmOcgOpt"),
        ("INFINERA-PM-LMOCGPTP-MIB", "lmOcgPtpPmRealLmOcgOpr"),
        ("INFINERA-PM-LMOCGPTP-MIB", "lmOcgPtpPmRealLmOcgTxEdfaOpr"),
        ("INFINERA-PM-LMOCGPTP-MIB", "lmOcgPtpPmRealLmOcgTxEdfaOpt"),
        ("INFINERA-PM-LMOCGPTP-MIB", "lmOcgPtpPmRealLmOcgTxEdfaLbc"),
        ("INFINERA-PM-LMOCGPTP-MIB", "lmOcgPtpPmRealLmOcgRxEdfaOpr"),
        ("INFINERA-PM-LMOCGPTP-MIB", "lmOcgPtpPmRealLmOcgRxEdfaOpt"),
        ("INFINERA-PM-LMOCGPTP-MIB", "lmOcgPtpPmRealLmOcgRxEdfaLbc"),
        ("INFINERA-PM-LMOCGPTP-MIB", "lmOcgPtpPmRealLmOcgPmd"),
        ("INFINERA-PM-LMOCGPTP-MIB", "lmOcgPtpPmRealLmOcgSoPmd"))
)
if mibBuilder.loadTexts:
    lmOcgPtpPmRealGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

lmOcgPtpPmRealCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 32, 3, 1, 1)
)
lmOcgPtpPmRealCompliance.setObjects(
    ("INFINERA-PM-LMOCGPTP-MIB", "lmOcgPtpPmRealGroup")
)
if mibBuilder.loadTexts:
    lmOcgPtpPmRealCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INFINERA-PM-LMOCGPTP-MIB",
    **{"lmOcgPtpPmMIB": lmOcgPtpPmMIB,
       "lmOcgPtpPmRealTable": lmOcgPtpPmRealTable,
       "lmOcgPtpPmRealEntry": lmOcgPtpPmRealEntry,
       "lmOcgPtpPmRealLmOcgOpt": lmOcgPtpPmRealLmOcgOpt,
       "lmOcgPtpPmRealLmOcgOpr": lmOcgPtpPmRealLmOcgOpr,
       "lmOcgPtpPmRealLmOcgTxEdfaOpr": lmOcgPtpPmRealLmOcgTxEdfaOpr,
       "lmOcgPtpPmRealLmOcgTxEdfaOpt": lmOcgPtpPmRealLmOcgTxEdfaOpt,
       "lmOcgPtpPmRealLmOcgTxEdfaLbc": lmOcgPtpPmRealLmOcgTxEdfaLbc,
       "lmOcgPtpPmRealLmOcgRxEdfaOpr": lmOcgPtpPmRealLmOcgRxEdfaOpr,
       "lmOcgPtpPmRealLmOcgRxEdfaOpt": lmOcgPtpPmRealLmOcgRxEdfaOpt,
       "lmOcgPtpPmRealLmOcgRxEdfaLbc": lmOcgPtpPmRealLmOcgRxEdfaLbc,
       "lmOcgPtpPmRealLmOcgPmd": lmOcgPtpPmRealLmOcgPmd,
       "lmOcgPtpPmRealLmOcgSoPmd": lmOcgPtpPmRealLmOcgSoPmd,
       "lmOcgPtpPmConformance": lmOcgPtpPmConformance,
       "lmOcgPtpPmCompliances": lmOcgPtpPmCompliances,
       "lmOcgPtpPmRealCompliance": lmOcgPtpPmRealCompliance,
       "lmOcgPtpPmGroups": lmOcgPtpPmGroups,
       "lmOcgPtpPmRealGroup": lmOcgPtpPmRealGroup}
)
