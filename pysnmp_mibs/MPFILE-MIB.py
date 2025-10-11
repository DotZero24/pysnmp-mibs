# SNMP MIB module (MPFILE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/maipu/MPFILE-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:11:07 2025
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

(mpMgmt,) = mibBuilder.importSymbols(
    "MAIPU-SMI",
    "mpMgmt")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

mpFileMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5651, 3, 3)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs



class _MpSoftVersion_Type(DisplayString):
    """Custom type mpSoftVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_MpSoftVersion_Type.__name__ = "DisplayString"
_MpSoftVersion_Object = MibScalar
mpSoftVersion = _MpSoftVersion_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 3, 1),
    _MpSoftVersion_Type()
)
mpSoftVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpSoftVersion.setStatus("current")
_MpFileTable_Object = MibTable
mpFileTable = _MpFileTable_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 3, 2)
)
if mibBuilder.loadTexts:
    mpFileTable.setStatus("current")
_MpFileEntry_Object = MibTableRow
mpFileEntry = _MpFileEntry_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 3, 2, 1)
)
mpFileEntry.setIndexNames(
    (0, "MPFILE-MIB", "mpFileCommand"),
)
if mibBuilder.loadTexts:
    mpFileEntry.setStatus("current")


class _MpFileCommand_Type(Integer32):
    """Custom type mpFileCommand based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("backup", 1),
          ("restore", 2),
          ("update", 3),
          ("reboot", 4))
    )


_MpFileCommand_Type.__name__ = "Integer32"
_MpFileCommand_Object = MibTableColumn
mpFileCommand = _MpFileCommand_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 3, 2, 1, 1),
    _MpFileCommand_Type()
)
mpFileCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpFileCommand.setStatus("current")


class _MpFileName_Type(DisplayString):
    """Custom type mpFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_MpFileName_Type.__name__ = "DisplayString"
_MpFileName_Object = MibTableColumn
mpFileName = _MpFileName_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 3, 2, 1, 2),
    _MpFileName_Type()
)
mpFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpFileName.setStatus("current")
_MpFileSize_Type = Integer32
_MpFileSize_Object = MibTableColumn
mpFileSize = _MpFileSize_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 3, 2, 1, 3),
    _MpFileSize_Type()
)
mpFileSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpFileSize.setStatus("current")


class _MpFileConfigType_Type(Integer32):
    """Custom type mpFileConfigType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("running", 2),
          ("startup", 3))
    )


_MpFileConfigType_Type.__name__ = "Integer32"
_MpFileConfigType_Object = MibTableColumn
mpFileConfigType = _MpFileConfigType_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 3, 2, 1, 4),
    _MpFileConfigType_Type()
)
mpFileConfigType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpFileConfigType.setStatus("current")


class _MpFileTransMode_Type(Integer32):
    """Custom type mpFileTransMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ftp", 1),
          ("tftp", 2),
          ("rcp", 3))
    )


_MpFileTransMode_Type.__name__ = "Integer32"
_MpFileTransMode_Object = MibTableColumn
mpFileTransMode = _MpFileTransMode_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 3, 2, 1, 5),
    _MpFileTransMode_Type()
)
mpFileTransMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpFileTransMode.setStatus("current")
_MpFileServerIP_Type = IpAddress
_MpFileServerIP_Object = MibTableColumn
mpFileServerIP = _MpFileServerIP_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 3, 2, 1, 6),
    _MpFileServerIP_Type()
)
mpFileServerIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpFileServerIP.setStatus("current")


class _MpFileUser_Type(DisplayString):
    """Custom type mpFileUser based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_MpFileUser_Type.__name__ = "DisplayString"
_MpFileUser_Object = MibTableColumn
mpFileUser = _MpFileUser_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 3, 2, 1, 7),
    _MpFileUser_Type()
)
mpFileUser.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpFileUser.setStatus("current")


class _MpFilePassword_Type(OctetString):
    """Custom type mpFilePassword based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MpFilePassword_Type.__name__ = "OctetString"
_MpFilePassword_Object = MibTableColumn
mpFilePassword = _MpFilePassword_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 3, 2, 1, 8),
    _MpFilePassword_Type()
)
mpFilePassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpFilePassword.setStatus("current")


class _MpFileEncrypt_Type(Integer32):
    """Custom type mpFileEncrypt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("none", 1)
    )


_MpFileEncrypt_Type.__name__ = "Integer32"
_MpFileEncrypt_Object = MibTableColumn
mpFileEncrypt = _MpFileEncrypt_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 3, 2, 1, 9),
    _MpFileEncrypt_Type()
)
mpFileEncrypt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpFileEncrypt.setStatus("current")
_MpRtrCommand_ObjectIdentity = ObjectIdentity
mpRtrCommand = _MpRtrCommand_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5651, 3, 3, 3)
)


class _MpRtrCommWrite_Type(Integer32):
    """Custom type mpRtrCommWrite based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noop", 1),
          ("write", 2))
    )


_MpRtrCommWrite_Type.__name__ = "Integer32"
_MpRtrCommWrite_Object = MibScalar
mpRtrCommWrite = _MpRtrCommWrite_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 3, 3, 1),
    _MpRtrCommWrite_Type()
)
mpRtrCommWrite.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpRtrCommWrite.setStatus("current")


class _MpRtrCommBackup_Type(Integer32):
    """Custom type mpRtrCommBackup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MpRtrCommBackup_Type.__name__ = "Integer32"
_MpRtrCommBackup_Object = MibScalar
mpRtrCommBackup = _MpRtrCommBackup_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 3, 3, 2),
    _MpRtrCommBackup_Type()
)
mpRtrCommBackup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpRtrCommBackup.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MPFILE-MIB",
    **{"mpFileMib": mpFileMib,
       "mpSoftVersion": mpSoftVersion,
       "mpFileTable": mpFileTable,
       "mpFileEntry": mpFileEntry,
       "mpFileCommand": mpFileCommand,
       "mpFileName": mpFileName,
       "mpFileSize": mpFileSize,
       "mpFileConfigType": mpFileConfigType,
       "mpFileTransMode": mpFileTransMode,
       "mpFileServerIP": mpFileServerIP,
       "mpFileUser": mpFileUser,
       "mpFilePassword": mpFilePassword,
       "mpFileEncrypt": mpFileEncrypt,
       "mpRtrCommand": mpRtrCommand,
       "mpRtrCommWrite": mpRtrCommWrite,
       "mpRtrCommBackup": mpRtrCommBackup}
)
