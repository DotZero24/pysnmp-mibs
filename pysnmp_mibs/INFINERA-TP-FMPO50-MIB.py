# SNMP MIB module (INFINERA-TP-FMPO50-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/INFINERA-TP-FMPO50-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:17:16 2025
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

(terminationPoint,) = mibBuilder.importSymbols(
    "INFINERA-REG-MIB",
    "terminationPoint")

(FloatHundredths,
 InfnEnableDisable) = mibBuilder.importSymbols(
    "INFINERA-TC-MIB",
    "FloatHundredths",
    "InfnEnableDisable")

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

fmpo50PtpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 41)
)
if mibBuilder.loadTexts:
    fmpo50PtpMIB.setRevisions(
        ("2013-10-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Fmpo50PtpTable_Object = MibTable
fmpo50PtpTable = _Fmpo50PtpTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 41, 1)
)
if mibBuilder.loadTexts:
    fmpo50PtpTable.setStatus("current")
_Fmpo50PtpEntry_Object = MibTableRow
fmpo50PtpEntry = _Fmpo50PtpEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 41, 1, 1)
)
fmpo50PtpEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    fmpo50PtpEntry.setStatus("current")
_Fmpo50PtpProvNbrTP_Type = DisplayString
_Fmpo50PtpProvNbrTP_Object = MibTableColumn
fmpo50PtpProvNbrTP = _Fmpo50PtpProvNbrTP_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 41, 1, 1, 1),
    _Fmpo50PtpProvNbrTP_Type()
)
fmpo50PtpProvNbrTP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fmpo50PtpProvNbrTP.setStatus("current")
_Fmpo50PtpConformance_ObjectIdentity = ObjectIdentity
fmpo50PtpConformance = _Fmpo50PtpConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 41, 3)
)
_Fmpo50PtpCompliances_ObjectIdentity = ObjectIdentity
fmpo50PtpCompliances = _Fmpo50PtpCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 41, 3, 1)
)
_Fmpo50PtpGroups_ObjectIdentity = ObjectIdentity
fmpo50PtpGroups = _Fmpo50PtpGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 41, 3, 2)
)

# Managed Objects groups

fmpo50PtpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 41, 3, 2, 1)
)
fmpo50PtpGroup.setObjects(
    ("INFINERA-TP-FMPO50-MIB", "fmpo50PtpProvNbrTP")
)
if mibBuilder.loadTexts:
    fmpo50PtpGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

fmpo50PtpCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 41, 3, 1, 1)
)
fmpo50PtpCompliance.setObjects(
    ("INFINERA-TP-FMPO50-MIB", "fmpo50PtpGroup")
)
if mibBuilder.loadTexts:
    fmpo50PtpCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INFINERA-TP-FMPO50-MIB",
    **{"fmpo50PtpMIB": fmpo50PtpMIB,
       "fmpo50PtpTable": fmpo50PtpTable,
       "fmpo50PtpEntry": fmpo50PtpEntry,
       "fmpo50PtpProvNbrTP": fmpo50PtpProvNbrTP,
       "fmpo50PtpConformance": fmpo50PtpConformance,
       "fmpo50PtpCompliances": fmpo50PtpCompliances,
       "fmpo50PtpCompliance": fmpo50PtpCompliance,
       "fmpo50PtpGroups": fmpo50PtpGroups,
       "fmpo50PtpGroup": fmpo50PtpGroup}
)
