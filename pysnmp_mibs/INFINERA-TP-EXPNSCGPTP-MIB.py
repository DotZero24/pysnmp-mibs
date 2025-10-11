# SNMP MIB module (INFINERA-TP-EXPNSCGPTP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/INFINERA-TP-EXPNSCGPTP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:15:31 2025
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

expnScgPtpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 47)
)
if mibBuilder.loadTexts:
    expnScgPtpMIB.setRevisions(
        ("2013-10-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ExpnScgPtpTable_Object = MibTable
expnScgPtpTable = _ExpnScgPtpTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 47, 1)
)
if mibBuilder.loadTexts:
    expnScgPtpTable.setStatus("current")
_ExpnScgPtpEntry_Object = MibTableRow
expnScgPtpEntry = _ExpnScgPtpEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 47, 1, 1)
)
expnScgPtpEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    expnScgPtpEntry.setStatus("current")
_ExpnScgPtpScgNumber_Type = Integer32
_ExpnScgPtpScgNumber_Object = MibTableColumn
expnScgPtpScgNumber = _ExpnScgPtpScgNumber_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 47, 1, 1, 1),
    _ExpnScgPtpScgNumber_Type()
)
expnScgPtpScgNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expnScgPtpScgNumber.setStatus("current")
_ExpnScgPtpMPOAID_Type = DisplayString
_ExpnScgPtpMPOAID_Object = MibTableColumn
expnScgPtpMPOAID = _ExpnScgPtpMPOAID_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 47, 1, 1, 2),
    _ExpnScgPtpMPOAID_Type()
)
expnScgPtpMPOAID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    expnScgPtpMPOAID.setStatus("current")


class _ExpnScgPtpPathLossCheckControlStatus_Type(Integer32):
    """Custom type expnScgPtpPathLossCheckControlStatus based on Integer32"""
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


_ExpnScgPtpPathLossCheckControlStatus_Type.__name__ = "Integer32"
_ExpnScgPtpPathLossCheckControlStatus_Object = MibTableColumn
expnScgPtpPathLossCheckControlStatus = _ExpnScgPtpPathLossCheckControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 47, 1, 1, 3),
    _ExpnScgPtpPathLossCheckControlStatus_Type()
)
expnScgPtpPathLossCheckControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expnScgPtpPathLossCheckControlStatus.setStatus("current")
_ExpnScgPtpLastSuccessfullPathLossCheckTS_Type = Integer32
_ExpnScgPtpLastSuccessfullPathLossCheckTS_Object = MibTableColumn
expnScgPtpLastSuccessfullPathLossCheckTS = _ExpnScgPtpLastSuccessfullPathLossCheckTS_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 47, 1, 1, 4),
    _ExpnScgPtpLastSuccessfullPathLossCheckTS_Type()
)
expnScgPtpLastSuccessfullPathLossCheckTS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expnScgPtpLastSuccessfullPathLossCheckTS.setStatus("current")
_ExpnScgPtpPathLoss_Type = FloatHundredths
_ExpnScgPtpPathLoss_Object = MibTableColumn
expnScgPtpPathLoss = _ExpnScgPtpPathLoss_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 47, 1, 1, 5),
    _ExpnScgPtpPathLoss_Type()
)
expnScgPtpPathLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expnScgPtpPathLoss.setStatus("current")
_ExpnScgPtpPathLossCheckDetectedPort_Type = DisplayString
_ExpnScgPtpPathLossCheckDetectedPort_Object = MibTableColumn
expnScgPtpPathLossCheckDetectedPort = _ExpnScgPtpPathLossCheckDetectedPort_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 47, 1, 1, 6),
    _ExpnScgPtpPathLossCheckDetectedPort_Type()
)
expnScgPtpPathLossCheckDetectedPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expnScgPtpPathLossCheckDetectedPort.setStatus("current")
_ExpnScgPtpLastPathLossCheckAttemptTS_Type = Integer32
_ExpnScgPtpLastPathLossCheckAttemptTS_Object = MibTableColumn
expnScgPtpLastPathLossCheckAttemptTS = _ExpnScgPtpLastPathLossCheckAttemptTS_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 47, 1, 1, 7),
    _ExpnScgPtpLastPathLossCheckAttemptTS_Type()
)
expnScgPtpLastPathLossCheckAttemptTS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expnScgPtpLastPathLossCheckAttemptTS.setStatus("current")


class _ExpnScgPtpLastPathLossCheckAttemptStatus_Type(Integer32):
    """Custom type expnScgPtpLastPathLossCheckAttemptStatus based on Integer32"""
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


_ExpnScgPtpLastPathLossCheckAttemptStatus_Type.__name__ = "Integer32"
_ExpnScgPtpLastPathLossCheckAttemptStatus_Object = MibTableColumn
expnScgPtpLastPathLossCheckAttemptStatus = _ExpnScgPtpLastPathLossCheckAttemptStatus_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 47, 1, 1, 8),
    _ExpnScgPtpLastPathLossCheckAttemptStatus_Type()
)
expnScgPtpLastPathLossCheckAttemptStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expnScgPtpLastPathLossCheckAttemptStatus.setStatus("current")


class _ExpnScgPtpLastPathLossCheckFailedReason_Type(Integer32):
    """Custom type expnScgPtpLastPathLossCheckFailedReason based on Integer32"""
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


_ExpnScgPtpLastPathLossCheckFailedReason_Type.__name__ = "Integer32"
_ExpnScgPtpLastPathLossCheckFailedReason_Object = MibTableColumn
expnScgPtpLastPathLossCheckFailedReason = _ExpnScgPtpLastPathLossCheckFailedReason_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 47, 1, 1, 9),
    _ExpnScgPtpLastPathLossCheckFailedReason_Type()
)
expnScgPtpLastPathLossCheckFailedReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expnScgPtpLastPathLossCheckFailedReason.setStatus("current")


class _ExpnScgPtpPathLossHigh_Type(Integer32):
    """Custom type expnScgPtpPathLossHigh based on Integer32"""
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


_ExpnScgPtpPathLossHigh_Type.__name__ = "Integer32"
_ExpnScgPtpPathLossHigh_Object = MibTableColumn
expnScgPtpPathLossHigh = _ExpnScgPtpPathLossHigh_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 47, 1, 1, 10),
    _ExpnScgPtpPathLossHigh_Type()
)
expnScgPtpPathLossHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expnScgPtpPathLossHigh.setStatus("current")
_ExpnScgPtpConformance_ObjectIdentity = ObjectIdentity
expnScgPtpConformance = _ExpnScgPtpConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 47, 3)
)
_ExpnScgPtpCompliances_ObjectIdentity = ObjectIdentity
expnScgPtpCompliances = _ExpnScgPtpCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 47, 3, 1)
)
_ExpnScgPtpGroups_ObjectIdentity = ObjectIdentity
expnScgPtpGroups = _ExpnScgPtpGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 47, 3, 2)
)

# Managed Objects groups

expnScgPtpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 47, 3, 2, 1)
)
expnScgPtpGroup.setObjects(
      *(("INFINERA-TP-EXPNSCGPTP-MIB", "expnScgPtpScgNumber"),
        ("INFINERA-TP-EXPNSCGPTP-MIB", "expnScgPtpMPOAID"),
        ("INFINERA-TP-EXPNSCGPTP-MIB", "expnScgPtpPathLossCheckControlStatus"),
        ("INFINERA-TP-EXPNSCGPTP-MIB", "expnScgPtpLastSuccessfullPathLossCheckTS"),
        ("INFINERA-TP-EXPNSCGPTP-MIB", "expnScgPtpPathLoss"),
        ("INFINERA-TP-EXPNSCGPTP-MIB", "expnScgPtpPathLossCheckDetectedPort"),
        ("INFINERA-TP-EXPNSCGPTP-MIB", "expnScgPtpLastPathLossCheckAttemptTS"),
        ("INFINERA-TP-EXPNSCGPTP-MIB", "expnScgPtpLastPathLossCheckAttemptStatus"),
        ("INFINERA-TP-EXPNSCGPTP-MIB", "expnScgPtpLastPathLossCheckFailedReason"),
        ("INFINERA-TP-EXPNSCGPTP-MIB", "expnScgPtpPathLossHigh"))
)
if mibBuilder.loadTexts:
    expnScgPtpGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

expnScgPtpCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 47, 3, 1, 1)
)
expnScgPtpCompliance.setObjects(
    ("INFINERA-TP-EXPNSCGPTP-MIB", "expnScgPtpGroup")
)
if mibBuilder.loadTexts:
    expnScgPtpCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INFINERA-TP-EXPNSCGPTP-MIB",
    **{"expnScgPtpMIB": expnScgPtpMIB,
       "expnScgPtpTable": expnScgPtpTable,
       "expnScgPtpEntry": expnScgPtpEntry,
       "expnScgPtpScgNumber": expnScgPtpScgNumber,
       "expnScgPtpMPOAID": expnScgPtpMPOAID,
       "expnScgPtpPathLossCheckControlStatus": expnScgPtpPathLossCheckControlStatus,
       "expnScgPtpLastSuccessfullPathLossCheckTS": expnScgPtpLastSuccessfullPathLossCheckTS,
       "expnScgPtpPathLoss": expnScgPtpPathLoss,
       "expnScgPtpPathLossCheckDetectedPort": expnScgPtpPathLossCheckDetectedPort,
       "expnScgPtpLastPathLossCheckAttemptTS": expnScgPtpLastPathLossCheckAttemptTS,
       "expnScgPtpLastPathLossCheckAttemptStatus": expnScgPtpLastPathLossCheckAttemptStatus,
       "expnScgPtpLastPathLossCheckFailedReason": expnScgPtpLastPathLossCheckFailedReason,
       "expnScgPtpPathLossHigh": expnScgPtpPathLossHigh,
       "expnScgPtpConformance": expnScgPtpConformance,
       "expnScgPtpCompliances": expnScgPtpCompliances,
       "expnScgPtpCompliance": expnScgPtpCompliance,
       "expnScgPtpGroups": expnScgPtpGroups,
       "expnScgPtpGroup": expnScgPtpGroup}
)
