# SNMP MIB module (INFINERA-PM-DLMOCGPTP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/INFINERA-PM-DLMOCGPTP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:14:34 2025
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

dlmOcgPtpPmMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 5)
)
if mibBuilder.loadTexts:
    dlmOcgPtpPmMIB.setRevisions(
        ("2008-10-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_DlmOcgPtpPmRealTable_Object = MibTable
dlmOcgPtpPmRealTable = _DlmOcgPtpPmRealTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 5, 1)
)
if mibBuilder.loadTexts:
    dlmOcgPtpPmRealTable.setStatus("current")
_DlmOcgPtpPmRealEntry_Object = MibTableRow
dlmOcgPtpPmRealEntry = _DlmOcgPtpPmRealEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 5, 1, 1)
)
dlmOcgPtpPmRealEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    dlmOcgPtpPmRealEntry.setStatus("current")
_DlmOcgPtpPmRealDlmOcgOpt_Type = FloatHundredths
_DlmOcgPtpPmRealDlmOcgOpt_Object = MibTableColumn
dlmOcgPtpPmRealDlmOcgOpt = _DlmOcgPtpPmRealDlmOcgOpt_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 5, 1, 1, 1),
    _DlmOcgPtpPmRealDlmOcgOpt_Type()
)
dlmOcgPtpPmRealDlmOcgOpt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlmOcgPtpPmRealDlmOcgOpt.setStatus("current")
_DlmOcgPtpPmRealDlmOcgOpr_Type = FloatHundredths
_DlmOcgPtpPmRealDlmOcgOpr_Object = MibTableColumn
dlmOcgPtpPmRealDlmOcgOpr = _DlmOcgPtpPmRealDlmOcgOpr_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 5, 1, 1, 2),
    _DlmOcgPtpPmRealDlmOcgOpr_Type()
)
dlmOcgPtpPmRealDlmOcgOpr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlmOcgPtpPmRealDlmOcgOpr.setStatus("current")
_DlmOcgPtpPmConformance_ObjectIdentity = ObjectIdentity
dlmOcgPtpPmConformance = _DlmOcgPtpPmConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 5, 3)
)
_DlmOcgPtpPmCompliances_ObjectIdentity = ObjectIdentity
dlmOcgPtpPmCompliances = _DlmOcgPtpPmCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 5, 3, 1)
)
_DlmOcgPtpPmGroups_ObjectIdentity = ObjectIdentity
dlmOcgPtpPmGroups = _DlmOcgPtpPmGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 5, 3, 2)
)

# Managed Objects groups

dlmOcgPtpPmRealGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 5, 3, 2, 1)
)
dlmOcgPtpPmRealGroup.setObjects(
      *(("INFINERA-PM-DLMOCGPTP-MIB", "dlmOcgPtpPmRealDlmOcgOpt"),
        ("INFINERA-PM-DLMOCGPTP-MIB", "dlmOcgPtpPmRealDlmOcgOpr"))
)
if mibBuilder.loadTexts:
    dlmOcgPtpPmRealGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

dlmOcgPtpPmRealCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 5, 3, 1, 1)
)
dlmOcgPtpPmRealCompliance.setObjects(
    ("INFINERA-PM-DLMOCGPTP-MIB", "dlmOcgPtpPmRealGroup")
)
if mibBuilder.loadTexts:
    dlmOcgPtpPmRealCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INFINERA-PM-DLMOCGPTP-MIB",
    **{"dlmOcgPtpPmMIB": dlmOcgPtpPmMIB,
       "dlmOcgPtpPmRealTable": dlmOcgPtpPmRealTable,
       "dlmOcgPtpPmRealEntry": dlmOcgPtpPmRealEntry,
       "dlmOcgPtpPmRealDlmOcgOpt": dlmOcgPtpPmRealDlmOcgOpt,
       "dlmOcgPtpPmRealDlmOcgOpr": dlmOcgPtpPmRealDlmOcgOpr,
       "dlmOcgPtpPmConformance": dlmOcgPtpPmConformance,
       "dlmOcgPtpPmCompliances": dlmOcgPtpPmCompliances,
       "dlmOcgPtpPmRealCompliance": dlmOcgPtpPmRealCompliance,
       "dlmOcgPtpPmGroups": dlmOcgPtpPmGroups,
       "dlmOcgPtpPmRealGroup": dlmOcgPtpPmRealGroup}
)
