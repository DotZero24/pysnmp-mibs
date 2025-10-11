# SNMP MIB module (INFINERA-TP-BPP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/INFINERA-TP-BPP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:16:04 2025
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

bppPtpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 66)
)
if mibBuilder.loadTexts:
    bppPtpMIB.setRevisions(
        ("2013-10-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_BppPtpTable_Object = MibTable
bppPtpTable = _BppPtpTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 66, 1)
)
if mibBuilder.loadTexts:
    bppPtpTable.setStatus("current")
_BppPtpEntry_Object = MibTableRow
bppPtpEntry = _BppPtpEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 66, 1, 1)
)
bppPtpEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    bppPtpEntry.setStatus("current")
_BppPtpProvNbrTP_Type = DisplayString
_BppPtpProvNbrTP_Object = MibTableColumn
bppPtpProvNbrTP = _BppPtpProvNbrTP_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 66, 1, 1, 1),
    _BppPtpProvNbrTP_Type()
)
bppPtpProvNbrTP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bppPtpProvNbrTP.setStatus("current")
_BppPtpConformance_ObjectIdentity = ObjectIdentity
bppPtpConformance = _BppPtpConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 66, 3)
)
_BppPtpCompliances_ObjectIdentity = ObjectIdentity
bppPtpCompliances = _BppPtpCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 66, 3, 1)
)
_BppPtpGroups_ObjectIdentity = ObjectIdentity
bppPtpGroups = _BppPtpGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 66, 3, 2)
)

# Managed Objects groups

bppPtpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 66, 3, 2, 1)
)
bppPtpGroup.setObjects(
    ("INFINERA-TP-BPP-MIB", "bppPtpProvNbrTP")
)
if mibBuilder.loadTexts:
    bppPtpGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

bppPtpCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 66, 3, 1, 1)
)
bppPtpCompliance.setObjects(
    ("INFINERA-TP-BPP-MIB", "bppPtpGroup")
)
if mibBuilder.loadTexts:
    bppPtpCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INFINERA-TP-BPP-MIB",
    **{"bppPtpMIB": bppPtpMIB,
       "bppPtpTable": bppPtpTable,
       "bppPtpEntry": bppPtpEntry,
       "bppPtpProvNbrTP": bppPtpProvNbrTP,
       "bppPtpConformance": bppPtpConformance,
       "bppPtpCompliances": bppPtpCompliances,
       "bppPtpCompliance": bppPtpCompliance,
       "bppPtpGroups": bppPtpGroups,
       "bppPtpGroup": bppPtpGroup}
)
