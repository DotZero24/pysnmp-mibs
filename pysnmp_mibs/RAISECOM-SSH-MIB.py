# SNMP MIB module (RAISECOM-SSH-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/raisecom/RAISECOM-SSH-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:36:14 2025
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

(raisecomAgent,) = mibBuilder.importSymbols(
    "RAISECOM-BASE-MIB",
    "raisecomAgent")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")

(EnableVar,) = mibBuilder.importSymbols(
    "SWITCH-TC",
    "EnableVar")


# MODULE-IDENTITY

raisecomSsh = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 1, 15)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RaisecomSshObjects_ObjectIdentity = ObjectIdentity
raisecomSshObjects = _RaisecomSshObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 1, 15, 1)
)
_RaisecomSshSvrConfiguration_ObjectIdentity = ObjectIdentity
raisecomSshSvrConfiguration = _RaisecomSshSvrConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 1, 15, 1, 1)
)


class _SshServerVersion_Type(Integer32):
    """Custom type sshServerVersion based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ssh-1", 1),
          ("ssh-2", 2),
          ("both", 3))
    )


_SshServerVersion_Type.__name__ = "Integer32"
_SshServerVersion_Object = MibScalar
sshServerVersion = _SshServerVersion_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 15, 1, 1, 1),
    _SshServerVersion_Type()
)
sshServerVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sshServerVersion.setStatus("current")


class _SshServerAuthenTimeout_Type(Integer32):
    """Custom type sshServerAuthenTimeout based on Integer32"""
    defaultValue = 600

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 65535),
    )


_SshServerAuthenTimeout_Type.__name__ = "Integer32"
_SshServerAuthenTimeout_Object = MibScalar
sshServerAuthenTimeout = _SshServerAuthenTimeout_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 15, 1, 1, 2),
    _SshServerAuthenTimeout_Type()
)
sshServerAuthenTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sshServerAuthenTimeout.setStatus("current")


class _SshServerAuthenRetries_Type(Integer32):
    """Custom type sshServerAuthenRetries based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_SshServerAuthenRetries_Type.__name__ = "Integer32"
_SshServerAuthenRetries_Object = MibScalar
sshServerAuthenRetries = _SshServerAuthenRetries_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 15, 1, 1, 3),
    _SshServerAuthenRetries_Type()
)
sshServerAuthenRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sshServerAuthenRetries.setStatus("current")


class _SshServerHostKeyName_Type(OctetString):
    """Custom type sshServerHostKeyName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_SshServerHostKeyName_Type.__name__ = "OctetString"
_SshServerHostKeyName_Object = MibScalar
sshServerHostKeyName = _SshServerHostKeyName_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 15, 1, 1, 4),
    _SshServerHostKeyName_Type()
)
sshServerHostKeyName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sshServerHostKeyName.setStatus("current")
_SshServerEnable_Type = EnableVar
_SshServerEnable_Object = MibScalar
sshServerEnable = _SshServerEnable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 15, 1, 1, 5),
    _SshServerEnable_Type()
)
sshServerEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sshServerEnable.setStatus("current")


class _SshServerAuthenType_Type(Integer32):
    """Custom type sshServerAuthenType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("public_key", 2),
          ("pass_word", 3))
    )


_SshServerAuthenType_Type.__name__ = "Integer32"
_SshServerAuthenType_Object = MibScalar
sshServerAuthenType = _SshServerAuthenType_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 15, 1, 1, 6),
    _SshServerAuthenType_Type()
)
sshServerAuthenType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sshServerAuthenType.setStatus("current")


class _SshServerPort_Type(Integer32):
    """Custom type sshServerPort based on Integer32"""
    defaultValue = 22

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SshServerPort_Type.__name__ = "Integer32"
_SshServerPort_Object = MibScalar
sshServerPort = _SshServerPort_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 15, 1, 1, 7),
    _SshServerPort_Type()
)
sshServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sshServerPort.setStatus("current")
_RaisecomSshKeyPairMgnt_ObjectIdentity = ObjectIdentity
raisecomSshKeyPairMgnt = _RaisecomSshKeyPairMgnt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 1, 15, 1, 2)
)


class _SshKeyPairGenerationStatus_Type(Integer32):
    """Custom type sshKeyPairGenerationStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("keyGenerationSuccess", 1),
          ("keyGenerationInProgress", 2),
          ("keyGenerationInvalidName", 3),
          ("keyGenerationInvalidModulus", 4),
          ("keyGenerationKeyExist", 5),
          ("keyGenerationNumLimit", 6),
          ("keyGenerationKeySavingError", 7))
    )


_SshKeyPairGenerationStatus_Type.__name__ = "Integer32"
_SshKeyPairGenerationStatus_Object = MibScalar
sshKeyPairGenerationStatus = _SshKeyPairGenerationStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 15, 1, 2, 1),
    _SshKeyPairGenerationStatus_Type()
)
sshKeyPairGenerationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshKeyPairGenerationStatus.setStatus("current")
_SshKeyPairTable_Object = MibTable
sshKeyPairTable = _SshKeyPairTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 15, 1, 2, 2)
)
if mibBuilder.loadTexts:
    sshKeyPairTable.setStatus("current")
_SshKeyPairEntry_Object = MibTableRow
sshKeyPairEntry = _SshKeyPairEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 15, 1, 2, 2, 1)
)
sshKeyPairEntry.setIndexNames(
    (0, "RAISECOM-SSH-MIB", "sshKeyPairName"),
)
if mibBuilder.loadTexts:
    sshKeyPairEntry.setStatus("current")


class _SshKeyPairName_Type(OctetString):
    """Custom type sshKeyPairName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_SshKeyPairName_Type.__name__ = "OctetString"
_SshKeyPairName_Object = MibTableColumn
sshKeyPairName = _SshKeyPairName_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 15, 1, 2, 2, 1, 1),
    _SshKeyPairName_Type()
)
sshKeyPairName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sshKeyPairName.setStatus("current")


class _SshKeyPairType_Type(Integer32):
    """Custom type sshKeyPairType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("rsa", 1),
          ("dsa", 2))
    )


_SshKeyPairType_Type.__name__ = "Integer32"
_SshKeyPairType_Object = MibTableColumn
sshKeyPairType = _SshKeyPairType_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 15, 1, 2, 2, 1, 2),
    _SshKeyPairType_Type()
)
sshKeyPairType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sshKeyPairType.setStatus("current")


class _SshKeyPairModulusSz_Type(Integer32):
    """Custom type sshKeyPairModulusSz based on Integer32"""
    defaultValue = 512

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(512, 2048),
    )


_SshKeyPairModulusSz_Type.__name__ = "Integer32"
_SshKeyPairModulusSz_Object = MibTableColumn
sshKeyPairModulusSz = _SshKeyPairModulusSz_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 15, 1, 2, 2, 1, 3),
    _SshKeyPairModulusSz_Type()
)
sshKeyPairModulusSz.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sshKeyPairModulusSz.setStatus("current")


class _SshKeyPairComment_Type(OctetString):
    """Custom type sshKeyPairComment based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SshKeyPairComment_Type.__name__ = "OctetString"
_SshKeyPairComment_Object = MibTableColumn
sshKeyPairComment = _SshKeyPairComment_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 15, 1, 2, 2, 1, 4),
    _SshKeyPairComment_Type()
)
sshKeyPairComment.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sshKeyPairComment.setStatus("current")
_SshKeyPairTrapOnComplete_Type = TruthValue
_SshKeyPairTrapOnComplete_Object = MibTableColumn
sshKeyPairTrapOnComplete = _SshKeyPairTrapOnComplete_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 15, 1, 2, 2, 1, 5),
    _SshKeyPairTrapOnComplete_Type()
)
sshKeyPairTrapOnComplete.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sshKeyPairTrapOnComplete.setStatus("current")


class _SshKeyPairPubData_Type(OctetString):
    """Custom type sshKeyPairPubData based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SshKeyPairPubData_Type.__name__ = "OctetString"
_SshKeyPairPubData_Object = MibTableColumn
sshKeyPairPubData = _SshKeyPairPubData_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 15, 1, 2, 2, 1, 6),
    _SshKeyPairPubData_Type()
)
sshKeyPairPubData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshKeyPairPubData.setStatus("current")
_SshKeyPairStatus_Type = RowStatus
_SshKeyPairStatus_Object = MibTableColumn
sshKeyPairStatus = _SshKeyPairStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 15, 1, 2, 2, 1, 7),
    _SshKeyPairStatus_Type()
)
sshKeyPairStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sshKeyPairStatus.setStatus("current")
_RaisecomSshSessionInfo_ObjectIdentity = ObjectIdentity
raisecomSshSessionInfo = _RaisecomSshSessionInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 1, 15, 1, 3)
)
_SshSessionTable_Object = MibTable
sshSessionTable = _SshSessionTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 15, 1, 3, 1)
)
if mibBuilder.loadTexts:
    sshSessionTable.setStatus("current")
_SshSessionEntry_Object = MibTableRow
sshSessionEntry = _SshSessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 15, 1, 3, 1, 1)
)
sshSessionEntry.setIndexNames(
    (0, "RAISECOM-SSH-MIB", "sshSessionId"),
)
if mibBuilder.loadTexts:
    sshSessionEntry.setStatus("current")
_SshSessionId_Type = Gauge32
_SshSessionId_Object = MibTableColumn
sshSessionId = _SshSessionId_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 15, 1, 3, 1, 1, 1),
    _SshSessionId_Type()
)
sshSessionId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sshSessionId.setStatus("current")


class _SshSessionVersion_Type(Integer32):
    """Custom type sshSessionVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ssh-1", 1),
          ("ssh-2", 2))
    )


_SshSessionVersion_Type.__name__ = "Integer32"
_SshSessionVersion_Object = MibTableColumn
sshSessionVersion = _SshSessionVersion_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 15, 1, 3, 1, 1, 2),
    _SshSessionVersion_Type()
)
sshSessionVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshSessionVersion.setStatus("current")


class _SshSessionState_Type(Integer32):
    """Custom type sshSessionState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("sessionVersionOk", 1),
          ("sessionKeysExchanged", 2),
          ("sessionAuthenticated", 3),
          ("sessionOpen", 4),
          ("sessionDisconnecting", 5),
          ("sessionDisconnected", 6),
          ("sessionClosed", 7))
    )


_SshSessionState_Type.__name__ = "Integer32"
_SshSessionState_Object = MibTableColumn
sshSessionState = _SshSessionState_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 15, 1, 3, 1, 1, 3),
    _SshSessionState_Type()
)
sshSessionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshSessionState.setStatus("current")


class _SshSessionUserId_Type(OctetString):
    """Custom type sshSessionUserId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_SshSessionUserId_Type.__name__ = "OctetString"
_SshSessionUserId_Object = MibTableColumn
sshSessionUserId = _SshSessionUserId_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 15, 1, 3, 1, 1, 4),
    _SshSessionUserId_Type()
)
sshSessionUserId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshSessionUserId.setStatus("current")
_SshSessionHostAddr_Type = IpAddress
_SshSessionHostAddr_Object = MibTableColumn
sshSessionHostAddr = _SshSessionHostAddr_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 15, 1, 3, 1, 1, 5),
    _SshSessionHostAddr_Type()
)
sshSessionHostAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshSessionHostAddr.setStatus("current")


class _SshSessionInEncrypt_Type(OctetString):
    """Custom type sshSessionInEncrypt based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_SshSessionInEncrypt_Type.__name__ = "OctetString"
_SshSessionInEncrypt_Object = MibTableColumn
sshSessionInEncrypt = _SshSessionInEncrypt_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 15, 1, 3, 1, 1, 6),
    _SshSessionInEncrypt_Type()
)
sshSessionInEncrypt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshSessionInEncrypt.setStatus("current")


class _SshSessionOutEncrypt_Type(OctetString):
    """Custom type sshSessionOutEncrypt based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_SshSessionOutEncrypt_Type.__name__ = "OctetString"
_SshSessionOutEncrypt_Object = MibTableColumn
sshSessionOutEncrypt = _SshSessionOutEncrypt_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 15, 1, 3, 1, 1, 7),
    _SshSessionOutEncrypt_Type()
)
sshSessionOutEncrypt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshSessionOutEncrypt.setStatus("current")


class _SshSessionInHmac_Type(OctetString):
    """Custom type sshSessionInHmac based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_SshSessionInHmac_Type.__name__ = "OctetString"
_SshSessionInHmac_Object = MibTableColumn
sshSessionInHmac = _SshSessionInHmac_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 15, 1, 3, 1, 1, 8),
    _SshSessionInHmac_Type()
)
sshSessionInHmac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshSessionInHmac.setStatus("current")


class _SshSessionOutHmac_Type(OctetString):
    """Custom type sshSessionOutHmac based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_SshSessionOutHmac_Type.__name__ = "OctetString"
_SshSessionOutHmac_Object = MibTableColumn
sshSessionOutHmac = _SshSessionOutHmac_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 15, 1, 3, 1, 1, 9),
    _SshSessionOutHmac_Type()
)
sshSessionOutHmac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshSessionOutHmac.setStatus("current")


class _SshSessionConnectTime_Type(OctetString):
    """Custom type sshSessionConnectTime based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65535),
    )


_SshSessionConnectTime_Type.__name__ = "OctetString"
_SshSessionConnectTime_Object = MibTableColumn
sshSessionConnectTime = _SshSessionConnectTime_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 15, 1, 3, 1, 1, 10),
    _SshSessionConnectTime_Type()
)
sshSessionConnectTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshSessionConnectTime.setStatus("current")
_SshSessionEnable_Type = EnableVar
_SshSessionEnable_Object = MibTableColumn
sshSessionEnable = _SshSessionEnable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 15, 1, 3, 1, 1, 11),
    _SshSessionEnable_Type()
)
sshSessionEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sshSessionEnable.setStatus("current")
_RaisecomSshTraps_ObjectIdentity = ObjectIdentity
raisecomSshTraps = _RaisecomSshTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 1, 15, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups

sshKeyPairGenerationCompletion = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 8886, 1, 15, 2, 1)
)
sshKeyPairGenerationCompletion.setObjects(
      *(("RAISECOM-SSH-MIB", "sshKeyPairGenerationStatus"),
        ("RAISECOM-SSH-MIB", "sshKeyPairName"))
)
if mibBuilder.loadTexts:
    sshKeyPairGenerationCompletion.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RAISECOM-SSH-MIB",
    **{"raisecomSsh": raisecomSsh,
       "raisecomSshObjects": raisecomSshObjects,
       "raisecomSshSvrConfiguration": raisecomSshSvrConfiguration,
       "sshServerVersion": sshServerVersion,
       "sshServerAuthenTimeout": sshServerAuthenTimeout,
       "sshServerAuthenRetries": sshServerAuthenRetries,
       "sshServerHostKeyName": sshServerHostKeyName,
       "sshServerEnable": sshServerEnable,
       "sshServerAuthenType": sshServerAuthenType,
       "sshServerPort": sshServerPort,
       "raisecomSshKeyPairMgnt": raisecomSshKeyPairMgnt,
       "sshKeyPairGenerationStatus": sshKeyPairGenerationStatus,
       "sshKeyPairTable": sshKeyPairTable,
       "sshKeyPairEntry": sshKeyPairEntry,
       "sshKeyPairName": sshKeyPairName,
       "sshKeyPairType": sshKeyPairType,
       "sshKeyPairModulusSz": sshKeyPairModulusSz,
       "sshKeyPairComment": sshKeyPairComment,
       "sshKeyPairTrapOnComplete": sshKeyPairTrapOnComplete,
       "sshKeyPairPubData": sshKeyPairPubData,
       "sshKeyPairStatus": sshKeyPairStatus,
       "raisecomSshSessionInfo": raisecomSshSessionInfo,
       "sshSessionTable": sshSessionTable,
       "sshSessionEntry": sshSessionEntry,
       "sshSessionId": sshSessionId,
       "sshSessionVersion": sshSessionVersion,
       "sshSessionState": sshSessionState,
       "sshSessionUserId": sshSessionUserId,
       "sshSessionHostAddr": sshSessionHostAddr,
       "sshSessionInEncrypt": sshSessionInEncrypt,
       "sshSessionOutEncrypt": sshSessionOutEncrypt,
       "sshSessionInHmac": sshSessionInHmac,
       "sshSessionOutHmac": sshSessionOutHmac,
       "sshSessionConnectTime": sshSessionConnectTime,
       "sshSessionEnable": sshSessionEnable,
       "raisecomSshTraps": raisecomSshTraps,
       "sshKeyPairGenerationCompletion": sshKeyPairGenerationCompletion}
)
