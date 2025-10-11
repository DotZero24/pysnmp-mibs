# SNMP MIB module (INFINERA-TP-ampOtdrPtp-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/INFINERA-TP-ampOtdrPtp-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:13:12 2025
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

ampOtdrPtpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 49)
)
if mibBuilder.loadTexts:
    ampOtdrPtpMIB.setRevisions(
        ("2013-10-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AmpOtdrPtpTable_Object = MibTable
ampOtdrPtpTable = _AmpOtdrPtpTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 49, 1)
)
if mibBuilder.loadTexts:
    ampOtdrPtpTable.setStatus("current")
_AmpOtdrPtpEntry_Object = MibTableRow
ampOtdrPtpEntry = _AmpOtdrPtpEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 49, 1, 1)
)
ampOtdrPtpEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    ampOtdrPtpEntry.setStatus("current")


class _AmpOtdrPtpConnectivityState_Type(Integer32):
    """Custom type ampOtdrPtpConnectivityState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notVerified", 1),
          ("valid", 2),
          ("inValid", 3))
    )


_AmpOtdrPtpConnectivityState_Type.__name__ = "Integer32"
_AmpOtdrPtpConnectivityState_Object = MibTableColumn
ampOtdrPtpConnectivityState = _AmpOtdrPtpConnectivityState_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 49, 1, 1, 1),
    _AmpOtdrPtpConnectivityState_Type()
)
ampOtdrPtpConnectivityState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ampOtdrPtpConnectivityState.setStatus("current")
_AmpOtdrPtpLstSuccConnValidationTime_Type = Integer32
_AmpOtdrPtpLstSuccConnValidationTime_Object = MibTableColumn
ampOtdrPtpLstSuccConnValidationTime = _AmpOtdrPtpLstSuccConnValidationTime_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 49, 1, 1, 2),
    _AmpOtdrPtpLstSuccConnValidationTime_Type()
)
ampOtdrPtpLstSuccConnValidationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ampOtdrPtpLstSuccConnValidationTime.setStatus("current")
_AmpOtdrPtpExpectedNeighborPtp_Type = DisplayString
_AmpOtdrPtpExpectedNeighborPtp_Object = MibTableColumn
ampOtdrPtpExpectedNeighborPtp = _AmpOtdrPtpExpectedNeighborPtp_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 49, 1, 1, 3),
    _AmpOtdrPtpExpectedNeighborPtp_Type()
)
ampOtdrPtpExpectedNeighborPtp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ampOtdrPtpExpectedNeighborPtp.setStatus("current")
_AmpOtdrPtpConformance_ObjectIdentity = ObjectIdentity
ampOtdrPtpConformance = _AmpOtdrPtpConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 49, 3)
)
_AmpOtdrPtpCompliances_ObjectIdentity = ObjectIdentity
ampOtdrPtpCompliances = _AmpOtdrPtpCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 49, 3, 1)
)
_AmpOtdrPtpGroups_ObjectIdentity = ObjectIdentity
ampOtdrPtpGroups = _AmpOtdrPtpGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 49, 3, 2)
)

# Managed Objects groups

ampOtdrPtpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 49, 3, 2, 1)
)
ampOtdrPtpGroup.setObjects(
      *(("INFINERA-TP-ampOtdrPtp-MIB", "ampOtdrPtpConnectivityState"),
        ("INFINERA-TP-ampOtdrPtp-MIB", "ampOtdrPtpLstSuccConnValidationTime"),
        ("INFINERA-TP-ampOtdrPtp-MIB", "ampOtdrPtpExpectedNeighborPtp"))
)
if mibBuilder.loadTexts:
    ampOtdrPtpGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ampOtdrPtpCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 49, 3, 1, 1)
)
ampOtdrPtpCompliance.setObjects(
    ("INFINERA-TP-ampOtdrPtp-MIB", "ampOtdrPtpGroup")
)
if mibBuilder.loadTexts:
    ampOtdrPtpCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INFINERA-TP-ampOtdrPtp-MIB",
    **{"ampOtdrPtpMIB": ampOtdrPtpMIB,
       "ampOtdrPtpTable": ampOtdrPtpTable,
       "ampOtdrPtpEntry": ampOtdrPtpEntry,
       "ampOtdrPtpConnectivityState": ampOtdrPtpConnectivityState,
       "ampOtdrPtpLstSuccConnValidationTime": ampOtdrPtpLstSuccConnValidationTime,
       "ampOtdrPtpExpectedNeighborPtp": ampOtdrPtpExpectedNeighborPtp,
       "ampOtdrPtpConformance": ampOtdrPtpConformance,
       "ampOtdrPtpCompliances": ampOtdrPtpCompliances,
       "ampOtdrPtpCompliance": ampOtdrPtpCompliance,
       "ampOtdrPtpGroups": ampOtdrPtpGroups,
       "ampOtdrPtpGroup": ampOtdrPtpGroup}
)
