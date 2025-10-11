# SNMP MIB module (INFINERA-TP-RBP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/INFINERA-TP-RBP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:14:05 2025
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

rbpPtpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 54)
)
if mibBuilder.loadTexts:
    rbpPtpMIB.setRevisions(
        ("2013-10-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RbpPtpTable_Object = MibTable
rbpPtpTable = _RbpPtpTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 54, 1)
)
if mibBuilder.loadTexts:
    rbpPtpTable.setStatus("current")
_RbpPtpEntry_Object = MibTableRow
rbpPtpEntry = _RbpPtpEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 54, 1, 1)
)
rbpPtpEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    rbpPtpEntry.setStatus("current")
_RbpPtpProvNbrTP_Type = DisplayString
_RbpPtpProvNbrTP_Object = MibTableColumn
rbpPtpProvNbrTP = _RbpPtpProvNbrTP_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 54, 1, 1, 1),
    _RbpPtpProvNbrTP_Type()
)
rbpPtpProvNbrTP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbpPtpProvNbrTP.setStatus("current")
_RbpPtpConformance_ObjectIdentity = ObjectIdentity
rbpPtpConformance = _RbpPtpConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 54, 3)
)
_RbpPtpCompliances_ObjectIdentity = ObjectIdentity
rbpPtpCompliances = _RbpPtpCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 54, 3, 1)
)
_RbpPtpGroups_ObjectIdentity = ObjectIdentity
rbpPtpGroups = _RbpPtpGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 54, 3, 2)
)

# Managed Objects groups

rbpPtpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 54, 3, 2, 1)
)
rbpPtpGroup.setObjects(
    ("INFINERA-TP-RBP-MIB", "rbpPtpProvNbrTP")
)
if mibBuilder.loadTexts:
    rbpPtpGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

rbpPtpCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 54, 3, 1, 1)
)
rbpPtpCompliance.setObjects(
    ("INFINERA-TP-RBP-MIB", "rbpPtpGroup")
)
if mibBuilder.loadTexts:
    rbpPtpCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INFINERA-TP-RBP-MIB",
    **{"rbpPtpMIB": rbpPtpMIB,
       "rbpPtpTable": rbpPtpTable,
       "rbpPtpEntry": rbpPtpEntry,
       "rbpPtpProvNbrTP": rbpPtpProvNbrTP,
       "rbpPtpConformance": rbpPtpConformance,
       "rbpPtpCompliances": rbpPtpCompliances,
       "rbpPtpCompliance": rbpPtpCompliance,
       "rbpPtpGroups": rbpPtpGroups,
       "rbpPtpGroup": rbpPtpGroup}
)
