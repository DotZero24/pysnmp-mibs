# SNMP MIB module (INFINERA-TP-EXPNPTP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/INFINERA-TP-EXPNPTP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:17:24 2025
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
 InfnExpnPtpMode) = mibBuilder.importSymbols(
    "INFINERA-TC-MIB",
    "FloatHundredths",
    "InfnExpnPtpMode")

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

expnPtpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 82)
)
if mibBuilder.loadTexts:
    expnPtpMIB.setRevisions(
        ("2017-02-02 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ExpnPtpTable_Object = MibTable
expnPtpTable = _ExpnPtpTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 82, 1)
)
if mibBuilder.loadTexts:
    expnPtpTable.setStatus("current")
_ExpnPtpEntry_Object = MibTableRow
expnPtpEntry = _ExpnPtpEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 82, 1, 1)
)
expnPtpEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    expnPtpEntry.setStatus("current")
_ExpnPtpMoId_Type = DisplayString
_ExpnPtpMoId_Object = MibTableColumn
expnPtpMoId = _ExpnPtpMoId_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 82, 1, 1, 1),
    _ExpnPtpMoId_Type()
)
expnPtpMoId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expnPtpMoId.setStatus("current")
_ExpnPtpExpectedNeighborPtp_Type = DisplayString
_ExpnPtpExpectedNeighborPtp_Object = MibTableColumn
expnPtpExpectedNeighborPtp = _ExpnPtpExpectedNeighborPtp_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 82, 1, 1, 2),
    _ExpnPtpExpectedNeighborPtp_Type()
)
expnPtpExpectedNeighborPtp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expnPtpExpectedNeighborPtp.setStatus("current")
_ExpnPtpMode_Type = InfnExpnPtpMode
_ExpnPtpMode_Object = MibTableColumn
expnPtpMode = _ExpnPtpMode_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 82, 1, 1, 3),
    _ExpnPtpMode_Type()
)
expnPtpMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    expnPtpMode.setStatus("current")
_ExpnPtpConformance_ObjectIdentity = ObjectIdentity
expnPtpConformance = _ExpnPtpConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 82, 3)
)
_ExpnPtpCompliances_ObjectIdentity = ObjectIdentity
expnPtpCompliances = _ExpnPtpCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 82, 3, 1)
)
_ExpnPtpGroups_ObjectIdentity = ObjectIdentity
expnPtpGroups = _ExpnPtpGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 82, 3, 2)
)

# Managed Objects groups

expnPtpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 82, 3, 2, 1)
)
expnPtpGroup.setObjects(
      *(("INFINERA-TP-EXPNPTP-MIB", "expnPtpMoId"),
        ("INFINERA-TP-EXPNPTP-MIB", "expnPtpExpectedNeighborPtp"),
        ("INFINERA-TP-EXPNPTP-MIB", "expnPtpMode"))
)
if mibBuilder.loadTexts:
    expnPtpGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

expnPtpCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 82, 3, 1, 1)
)
expnPtpCompliance.setObjects(
    ("INFINERA-TP-EXPNPTP-MIB", "expnPtpGroup")
)
if mibBuilder.loadTexts:
    expnPtpCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INFINERA-TP-EXPNPTP-MIB",
    **{"expnPtpMIB": expnPtpMIB,
       "expnPtpTable": expnPtpTable,
       "expnPtpEntry": expnPtpEntry,
       "expnPtpMoId": expnPtpMoId,
       "expnPtpExpectedNeighborPtp": expnPtpExpectedNeighborPtp,
       "expnPtpMode": expnPtpMode,
       "expnPtpConformance": expnPtpConformance,
       "expnPtpCompliances": expnPtpCompliances,
       "expnPtpCompliance": expnPtpCompliance,
       "expnPtpGroups": expnPtpGroups,
       "expnPtpGroup": expnPtpGroup}
)
