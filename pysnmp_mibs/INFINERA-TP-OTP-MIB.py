# SNMP MIB module (INFINERA-TP-OTP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/INFINERA-TP-OTP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:15:09 2025
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

optPtpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 39)
)
if mibBuilder.loadTexts:
    optPtpMIB.setRevisions(
        ("2013-10-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_OptPtpTable_Object = MibTable
optPtpTable = _OptPtpTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 39, 1)
)
if mibBuilder.loadTexts:
    optPtpTable.setStatus("current")
_OptPtpEntry_Object = MibTableRow
optPtpEntry = _OptPtpEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 39, 1, 1)
)
optPtpEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    optPtpEntry.setStatus("current")
_OptPtpProvNbrTP_Type = DisplayString
_OptPtpProvNbrTP_Object = MibTableColumn
optPtpProvNbrTP = _OptPtpProvNbrTP_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 39, 1, 1, 1),
    _OptPtpProvNbrTP_Type()
)
optPtpProvNbrTP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    optPtpProvNbrTP.setStatus("current")
_OptPtpConformance_ObjectIdentity = ObjectIdentity
optPtpConformance = _OptPtpConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 39, 3)
)
_OptPtpCompliances_ObjectIdentity = ObjectIdentity
optPtpCompliances = _OptPtpCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 39, 3, 1)
)
_OptPtpGroups_ObjectIdentity = ObjectIdentity
optPtpGroups = _OptPtpGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 39, 3, 2)
)

# Managed Objects groups

optPtpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 39, 3, 2, 1)
)
optPtpGroup.setObjects(
    ("INFINERA-TP-OTP-MIB", "optPtpProvNbrTP")
)
if mibBuilder.loadTexts:
    optPtpGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

optPtpCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 39, 3, 1, 1)
)
optPtpCompliance.setObjects(
    ("INFINERA-TP-OTP-MIB", "optPtpGroup")
)
if mibBuilder.loadTexts:
    optPtpCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INFINERA-TP-OTP-MIB",
    **{"optPtpMIB": optPtpMIB,
       "optPtpTable": optPtpTable,
       "optPtpEntry": optPtpEntry,
       "optPtpProvNbrTP": optPtpProvNbrTP,
       "optPtpConformance": optPtpConformance,
       "optPtpCompliances": optPtpCompliances,
       "optPtpCompliance": optPtpCompliance,
       "optPtpGroups": optPtpGroups,
       "optPtpGroup": optPtpGroup}
)
