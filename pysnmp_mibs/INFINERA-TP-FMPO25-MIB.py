# SNMP MIB module (INFINERA-TP-FMPO25-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/INFINERA-TP-FMPO25-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:15:44 2025
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

fmpo25PtpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 40)
)
if mibBuilder.loadTexts:
    fmpo25PtpMIB.setRevisions(
        ("2013-10-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Fmpo25PtpTable_Object = MibTable
fmpo25PtpTable = _Fmpo25PtpTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 40, 1)
)
if mibBuilder.loadTexts:
    fmpo25PtpTable.setStatus("current")
_Fmpo25PtpEntry_Object = MibTableRow
fmpo25PtpEntry = _Fmpo25PtpEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 40, 1, 1)
)
fmpo25PtpEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    fmpo25PtpEntry.setStatus("current")
_Fmpo25PtpProvNbrTP_Type = DisplayString
_Fmpo25PtpProvNbrTP_Object = MibTableColumn
fmpo25PtpProvNbrTP = _Fmpo25PtpProvNbrTP_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 40, 1, 1, 1),
    _Fmpo25PtpProvNbrTP_Type()
)
fmpo25PtpProvNbrTP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fmpo25PtpProvNbrTP.setStatus("current")
_Fmpo25PtpConformance_ObjectIdentity = ObjectIdentity
fmpo25PtpConformance = _Fmpo25PtpConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 40, 3)
)
_Fmpo25PtpCompliances_ObjectIdentity = ObjectIdentity
fmpo25PtpCompliances = _Fmpo25PtpCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 40, 3, 1)
)
_Fmpo25PtpGroups_ObjectIdentity = ObjectIdentity
fmpo25PtpGroups = _Fmpo25PtpGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 40, 3, 2)
)

# Managed Objects groups

fmpo25PtpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 40, 3, 2, 1)
)
fmpo25PtpGroup.setObjects(
    ("INFINERA-TP-FMPO25-MIB", "fmpo25PtpProvNbrTP")
)
if mibBuilder.loadTexts:
    fmpo25PtpGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

fmpo25PtpCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 40, 3, 1, 1)
)
fmpo25PtpCompliance.setObjects(
    ("INFINERA-TP-FMPO25-MIB", "fmpo25PtpGroup")
)
if mibBuilder.loadTexts:
    fmpo25PtpCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INFINERA-TP-FMPO25-MIB",
    **{"fmpo25PtpMIB": fmpo25PtpMIB,
       "fmpo25PtpTable": fmpo25PtpTable,
       "fmpo25PtpEntry": fmpo25PtpEntry,
       "fmpo25PtpProvNbrTP": fmpo25PtpProvNbrTP,
       "fmpo25PtpConformance": fmpo25PtpConformance,
       "fmpo25PtpCompliances": fmpo25PtpCompliances,
       "fmpo25PtpCompliance": fmpo25PtpCompliance,
       "fmpo25PtpGroups": fmpo25PtpGroups,
       "fmpo25PtpGroup": fmpo25PtpGroup}
)
