# SNMP MIB module (CAMBIUM-NETWORKS-DEVICE-AGENT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/cambium/CAMBIUM-NETWORKS-DEVICE-AGENT-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:07:40 2025
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
 enterprises,
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
    "enterprises",
    "iso")

(DateAndTime,
 DisplayString,
 PhysAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

deviceAgent = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 24, 2)
)
if mibBuilder.loadTexts:
    deviceAgent.setRevisions(
        ("2021-11-30 00:00",
         "2020-06-24 00:00",
         "2019-02-19 15:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CnMatrix_ObjectIdentity = ObjectIdentity
cnMatrix = _CnMatrix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 24)
)


class _CambiumDeviceAgentEnable_Type(TruthValue):
    """Custom type cambiumDeviceAgentEnable based on TruthValue"""
    defaultValue = 1


_CambiumDeviceAgentEnable_Type.__name__ = "TruthValue"
_CambiumDeviceAgentEnable_Object = MibScalar
cambiumDeviceAgentEnable = _CambiumDeviceAgentEnable_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 2, 1),
    _CambiumDeviceAgentEnable_Type()
)
cambiumDeviceAgentEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cambiumDeviceAgentEnable.setStatus("current")


class _CambiumDeviceAgentStaticURL_Type(DisplayString):
    """Custom type cambiumDeviceAgentStaticURL based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CambiumDeviceAgentStaticURL_Type.__name__ = "DisplayString"
_CambiumDeviceAgentStaticURL_Object = MibScalar
cambiumDeviceAgentStaticURL = _CambiumDeviceAgentStaticURL_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 2, 2),
    _CambiumDeviceAgentStaticURL_Type()
)
cambiumDeviceAgentStaticURL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cambiumDeviceAgentStaticURL.setStatus("current")


class _CambiumCNSDeviceAgentID_Type(DisplayString):
    """Custom type cambiumCNSDeviceAgentID based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_CambiumCNSDeviceAgentID_Type.__name__ = "DisplayString"
_CambiumCNSDeviceAgentID_Object = MibScalar
cambiumCNSDeviceAgentID = _CambiumCNSDeviceAgentID_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 2, 3),
    _CambiumCNSDeviceAgentID_Type()
)
cambiumCNSDeviceAgentID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cambiumCNSDeviceAgentID.setStatus("current")


class _CambiumCNSDeviceAgentPassword_Type(DisplayString):
    """Custom type cambiumCNSDeviceAgentPassword based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_CambiumCNSDeviceAgentPassword_Type.__name__ = "DisplayString"
_CambiumCNSDeviceAgentPassword_Object = MibScalar
cambiumCNSDeviceAgentPassword = _CambiumCNSDeviceAgentPassword_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 2, 4),
    _CambiumCNSDeviceAgentPassword_Type()
)
cambiumCNSDeviceAgentPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cambiumCNSDeviceAgentPassword.setStatus("current")


class _CambiumDeviceAgentValidateCert_Type(Integer32):
    """Custom type cambiumDeviceAgentValidateCert based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("cloud-only", 1),
          ("disabled", 2),
          ("full", 3))
    )


_CambiumDeviceAgentValidateCert_Type.__name__ = "Integer32"
_CambiumDeviceAgentValidateCert_Object = MibScalar
cambiumDeviceAgentValidateCert = _CambiumDeviceAgentValidateCert_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 2, 5),
    _CambiumDeviceAgentValidateCert_Type()
)
cambiumDeviceAgentValidateCert.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cambiumDeviceAgentValidateCert.setStatus("current")


class _CambiumDeviceAgentStatus_Type(Integer32):
    """Custom type cambiumDeviceAgentStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("notConnected", 1),
          ("dnsFailed", 2),
          ("noCambiumId", 3),
          ("error", 4),
          ("connecting", 5),
          ("approvalPending", 6),
          ("connected", 7),
          ("ownershipError", 8),
          ("messageFromCNS", 9))
    )


_CambiumDeviceAgentStatus_Type.__name__ = "Integer32"
_CambiumDeviceAgentStatus_Object = MibScalar
cambiumDeviceAgentStatus = _CambiumDeviceAgentStatus_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 2, 6),
    _CambiumDeviceAgentStatus_Type()
)
cambiumDeviceAgentStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumDeviceAgentStatus.setStatus("current")


class _CambiumDeviceAgentStatusMessage_Type(DisplayString):
    """Custom type cambiumDeviceAgentStatusMessage based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_CambiumDeviceAgentStatusMessage_Type.__name__ = "DisplayString"
_CambiumDeviceAgentStatusMessage_Object = MibScalar
cambiumDeviceAgentStatusMessage = _CambiumDeviceAgentStatusMessage_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 2, 7),
    _CambiumDeviceAgentStatusMessage_Type()
)
cambiumDeviceAgentStatusMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumDeviceAgentStatusMessage.setStatus("current")


class _CambiumDeviceAgentCNSURL_Type(DisplayString):
    """Custom type cambiumDeviceAgentCNSURL based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CambiumDeviceAgentCNSURL_Type.__name__ = "DisplayString"
_CambiumDeviceAgentCNSURL_Object = MibScalar
cambiumDeviceAgentCNSURL = _CambiumDeviceAgentCNSURL_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 2, 8),
    _CambiumDeviceAgentCNSURL_Type()
)
cambiumDeviceAgentCNSURL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumDeviceAgentCNSURL.setStatus("current")


class _CambiumDeviceAgentAccountID_Type(DisplayString):
    """Custom type cambiumDeviceAgentAccountID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_CambiumDeviceAgentAccountID_Type.__name__ = "DisplayString"
_CambiumDeviceAgentAccountID_Object = MibScalar
cambiumDeviceAgentAccountID = _CambiumDeviceAgentAccountID_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 2, 9),
    _CambiumDeviceAgentAccountID_Type()
)
cambiumDeviceAgentAccountID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumDeviceAgentAccountID.setStatus("current")


class _CambiumDeviceAgentLastAction_Type(DisplayString):
    """Custom type cambiumDeviceAgentLastAction based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_CambiumDeviceAgentLastAction_Type.__name__ = "DisplayString"
_CambiumDeviceAgentLastAction_Object = MibScalar
cambiumDeviceAgentLastAction = _CambiumDeviceAgentLastAction_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 2, 10),
    _CambiumDeviceAgentLastAction_Type()
)
cambiumDeviceAgentLastAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumDeviceAgentLastAction.setStatus("current")
_CambiumDeviceAgentLastSync_Type = DateAndTime
_CambiumDeviceAgentLastSync_Object = MibScalar
cambiumDeviceAgentLastSync = _CambiumDeviceAgentLastSync_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 2, 11),
    _CambiumDeviceAgentLastSync_Type()
)
cambiumDeviceAgentLastSync.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumDeviceAgentLastSync.setStatus("current")


class _CambiumDeviceAgentRemoteManager_Type(TruthValue):
    """Custom type cambiumDeviceAgentRemoteManager based on TruthValue"""
    defaultValue = 2


_CambiumDeviceAgentRemoteManager_Type.__name__ = "TruthValue"
_CambiumDeviceAgentRemoteManager_Object = MibScalar
cambiumDeviceAgentRemoteManager = _CambiumDeviceAgentRemoteManager_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 2, 12),
    _CambiumDeviceAgentRemoteManager_Type()
)
cambiumDeviceAgentRemoteManager.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumDeviceAgentRemoteManager.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CAMBIUM-NETWORKS-DEVICE-AGENT-MIB",
    **{"cnMatrix": cnMatrix,
       "deviceAgent": deviceAgent,
       "cambiumDeviceAgentEnable": cambiumDeviceAgentEnable,
       "cambiumDeviceAgentStaticURL": cambiumDeviceAgentStaticURL,
       "cambiumCNSDeviceAgentID": cambiumCNSDeviceAgentID,
       "cambiumCNSDeviceAgentPassword": cambiumCNSDeviceAgentPassword,
       "cambiumDeviceAgentValidateCert": cambiumDeviceAgentValidateCert,
       "cambiumDeviceAgentStatus": cambiumDeviceAgentStatus,
       "cambiumDeviceAgentStatusMessage": cambiumDeviceAgentStatusMessage,
       "cambiumDeviceAgentCNSURL": cambiumDeviceAgentCNSURL,
       "cambiumDeviceAgentAccountID": cambiumDeviceAgentAccountID,
       "cambiumDeviceAgentLastAction": cambiumDeviceAgentLastAction,
       "cambiumDeviceAgentLastSync": cambiumDeviceAgentLastSync,
       "cambiumDeviceAgentRemoteManager": cambiumDeviceAgentRemoteManager}
)
