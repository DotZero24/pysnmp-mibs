# SNMP MIB module (INFINERA-TP-BASESCGPTP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/INFINERA-TP-BASESCGPTP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:12:53 2025
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

baseScgPtpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 46)
)
if mibBuilder.loadTexts:
    baseScgPtpMIB.setRevisions(
        ("2013-10-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_BaseScgPtpTable_Object = MibTable
baseScgPtpTable = _BaseScgPtpTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 46, 1)
)
if mibBuilder.loadTexts:
    baseScgPtpTable.setStatus("current")
_BaseScgPtpEntry_Object = MibTableRow
baseScgPtpEntry = _BaseScgPtpEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 46, 1, 1)
)
baseScgPtpEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    baseScgPtpEntry.setStatus("current")
_BaseScgPtpScgNumber_Type = Integer32
_BaseScgPtpScgNumber_Object = MibTableColumn
baseScgPtpScgNumber = _BaseScgPtpScgNumber_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 46, 1, 1, 1),
    _BaseScgPtpScgNumber_Type()
)
baseScgPtpScgNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    baseScgPtpScgNumber.setStatus("current")
_BaseScgPtpMPOAID_Type = DisplayString
_BaseScgPtpMPOAID_Object = MibTableColumn
baseScgPtpMPOAID = _BaseScgPtpMPOAID_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 46, 1, 1, 2),
    _BaseScgPtpMPOAID_Type()
)
baseScgPtpMPOAID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    baseScgPtpMPOAID.setStatus("current")


class _BaseScgPtpPathLossCheckControlStatus_Type(Integer32):
    """Custom type baseScgPtpPathLossCheckControlStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inProgress", 1),
          ("idle", 2))
    )


_BaseScgPtpPathLossCheckControlStatus_Type.__name__ = "Integer32"
_BaseScgPtpPathLossCheckControlStatus_Object = MibTableColumn
baseScgPtpPathLossCheckControlStatus = _BaseScgPtpPathLossCheckControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 46, 1, 1, 3),
    _BaseScgPtpPathLossCheckControlStatus_Type()
)
baseScgPtpPathLossCheckControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    baseScgPtpPathLossCheckControlStatus.setStatus("current")
_BaseScgPtpLastSuccessfullPathLossCheckTS_Type = Integer32
_BaseScgPtpLastSuccessfullPathLossCheckTS_Object = MibTableColumn
baseScgPtpLastSuccessfullPathLossCheckTS = _BaseScgPtpLastSuccessfullPathLossCheckTS_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 46, 1, 1, 4),
    _BaseScgPtpLastSuccessfullPathLossCheckTS_Type()
)
baseScgPtpLastSuccessfullPathLossCheckTS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    baseScgPtpLastSuccessfullPathLossCheckTS.setStatus("current")
_BaseScgPtpPathLoss_Type = FloatHundredths
_BaseScgPtpPathLoss_Object = MibTableColumn
baseScgPtpPathLoss = _BaseScgPtpPathLoss_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 46, 1, 1, 5),
    _BaseScgPtpPathLoss_Type()
)
baseScgPtpPathLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    baseScgPtpPathLoss.setStatus("current")
_BaseScgPtpPathLossCheckDetectedPort_Type = DisplayString
_BaseScgPtpPathLossCheckDetectedPort_Object = MibTableColumn
baseScgPtpPathLossCheckDetectedPort = _BaseScgPtpPathLossCheckDetectedPort_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 46, 1, 1, 6),
    _BaseScgPtpPathLossCheckDetectedPort_Type()
)
baseScgPtpPathLossCheckDetectedPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    baseScgPtpPathLossCheckDetectedPort.setStatus("current")
_BaseScgPtpLastPathLossCheckAttemptTS_Type = Integer32
_BaseScgPtpLastPathLossCheckAttemptTS_Object = MibTableColumn
baseScgPtpLastPathLossCheckAttemptTS = _BaseScgPtpLastPathLossCheckAttemptTS_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 46, 1, 1, 7),
    _BaseScgPtpLastPathLossCheckAttemptTS_Type()
)
baseScgPtpLastPathLossCheckAttemptTS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    baseScgPtpLastPathLossCheckAttemptTS.setStatus("current")


class _BaseScgPtpLastPathLossCheckAttemptStatus_Type(Integer32):
    """Custom type baseScgPtpLastPathLossCheckAttemptStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("successfull", 1),
          ("unsuccessfull", 2),
          ("notAttempted", 3))
    )


_BaseScgPtpLastPathLossCheckAttemptStatus_Type.__name__ = "Integer32"
_BaseScgPtpLastPathLossCheckAttemptStatus_Object = MibTableColumn
baseScgPtpLastPathLossCheckAttemptStatus = _BaseScgPtpLastPathLossCheckAttemptStatus_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 46, 1, 1, 8),
    _BaseScgPtpLastPathLossCheckAttemptStatus_Type()
)
baseScgPtpLastPathLossCheckAttemptStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    baseScgPtpLastPathLossCheckAttemptStatus.setStatus("current")


class _BaseScgPtpLastPathLossCheckFailedReason_Type(Integer32):
    """Custom type baseScgPtpLastPathLossCheckFailedReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("na", 1),
          ("timedOut", 2),
          ("interruptedbyAD", 3),
          ("interruptedbyReset", 4),
          ("portInService", 5))
    )


_BaseScgPtpLastPathLossCheckFailedReason_Type.__name__ = "Integer32"
_BaseScgPtpLastPathLossCheckFailedReason_Object = MibTableColumn
baseScgPtpLastPathLossCheckFailedReason = _BaseScgPtpLastPathLossCheckFailedReason_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 46, 1, 1, 9),
    _BaseScgPtpLastPathLossCheckFailedReason_Type()
)
baseScgPtpLastPathLossCheckFailedReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    baseScgPtpLastPathLossCheckFailedReason.setStatus("current")


class _BaseScgPtpPathLossHigh_Type(Integer32):
    """Custom type baseScgPtpPathLossHigh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("true", 1),
          ("false", 2))
    )


_BaseScgPtpPathLossHigh_Type.__name__ = "Integer32"
_BaseScgPtpPathLossHigh_Object = MibTableColumn
baseScgPtpPathLossHigh = _BaseScgPtpPathLossHigh_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 46, 1, 1, 10),
    _BaseScgPtpPathLossHigh_Type()
)
baseScgPtpPathLossHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    baseScgPtpPathLossHigh.setStatus("current")
_BaseScgPtpConformance_ObjectIdentity = ObjectIdentity
baseScgPtpConformance = _BaseScgPtpConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 46, 3)
)
_BaseScgPtpCompliances_ObjectIdentity = ObjectIdentity
baseScgPtpCompliances = _BaseScgPtpCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 46, 3, 1)
)
_BaseScgPtpGroups_ObjectIdentity = ObjectIdentity
baseScgPtpGroups = _BaseScgPtpGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 46, 3, 2)
)

# Managed Objects groups

baseScgPtpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 46, 3, 2, 1)
)
baseScgPtpGroup.setObjects(
      *(("INFINERA-TP-BASESCGPTP-MIB", "baseScgPtpScgNumber"),
        ("INFINERA-TP-BASESCGPTP-MIB", "baseScgPtpMPOAID"),
        ("INFINERA-TP-BASESCGPTP-MIB", "baseScgPtpPathLossCheckControlStatus"),
        ("INFINERA-TP-BASESCGPTP-MIB", "baseScgPtpLastSuccessfullPathLossCheckTS"),
        ("INFINERA-TP-BASESCGPTP-MIB", "baseScgPtpPathLoss"),
        ("INFINERA-TP-BASESCGPTP-MIB", "baseScgPtpPathLossCheckDetectedPort"),
        ("INFINERA-TP-BASESCGPTP-MIB", "baseScgPtpLastPathLossCheckAttemptTS"),
        ("INFINERA-TP-BASESCGPTP-MIB", "baseScgPtpLastPathLossCheckAttemptStatus"),
        ("INFINERA-TP-BASESCGPTP-MIB", "baseScgPtpLastPathLossCheckFailedReason"),
        ("INFINERA-TP-BASESCGPTP-MIB", "baseScgPtpPathLossHigh"))
)
if mibBuilder.loadTexts:
    baseScgPtpGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

baseScgPtpCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 46, 3, 1, 1)
)
baseScgPtpCompliance.setObjects(
    ("INFINERA-TP-BASESCGPTP-MIB", "baseScgPtpGroup")
)
if mibBuilder.loadTexts:
    baseScgPtpCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INFINERA-TP-BASESCGPTP-MIB",
    **{"baseScgPtpMIB": baseScgPtpMIB,
       "baseScgPtpTable": baseScgPtpTable,
       "baseScgPtpEntry": baseScgPtpEntry,
       "baseScgPtpScgNumber": baseScgPtpScgNumber,
       "baseScgPtpMPOAID": baseScgPtpMPOAID,
       "baseScgPtpPathLossCheckControlStatus": baseScgPtpPathLossCheckControlStatus,
       "baseScgPtpLastSuccessfullPathLossCheckTS": baseScgPtpLastSuccessfullPathLossCheckTS,
       "baseScgPtpPathLoss": baseScgPtpPathLoss,
       "baseScgPtpPathLossCheckDetectedPort": baseScgPtpPathLossCheckDetectedPort,
       "baseScgPtpLastPathLossCheckAttemptTS": baseScgPtpLastPathLossCheckAttemptTS,
       "baseScgPtpLastPathLossCheckAttemptStatus": baseScgPtpLastPathLossCheckAttemptStatus,
       "baseScgPtpLastPathLossCheckFailedReason": baseScgPtpLastPathLossCheckFailedReason,
       "baseScgPtpPathLossHigh": baseScgPtpPathLossHigh,
       "baseScgPtpConformance": baseScgPtpConformance,
       "baseScgPtpCompliances": baseScgPtpCompliances,
       "baseScgPtpCompliance": baseScgPtpCompliance,
       "baseScgPtpGroups": baseScgPtpGroups,
       "baseScgPtpGroup": baseScgPtpGroup}
)
