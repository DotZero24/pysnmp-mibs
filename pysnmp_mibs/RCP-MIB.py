# SNMP MIB module (RCP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/d-link/RCP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:48:16 2025
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

(dlink_common_mgmt,) = mibBuilder.importSymbols(
    "DLINK-ID-REC-MIB",
    "dlink-common-mgmt")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

swRCPMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 82)
)


# Types definitions



class UnitList(OctetString):
    """Custom type UnitList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 3),
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SwRCPMgmt_ObjectIdentity = ObjectIdentity
swRCPMgmt = _SwRCPMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 82, 1)
)
_SwRCPFileTable_Object = MibTable
swRCPFileTable = _SwRCPFileTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 82, 1, 1)
)
if mibBuilder.loadTexts:
    swRCPFileTable.setStatus("current")
_SwRCPFileEntry_Object = MibTableRow
swRCPFileEntry = _SwRCPFileEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 82, 1, 1, 1)
)
swRCPFileEntry.setIndexNames(
    (0, "RCP-MIB", "swRCPFileIndex"),
)
if mibBuilder.loadTexts:
    swRCPFileEntry.setStatus("current")
_SwRCPFileIndex_Type = Integer32
_SwRCPFileIndex_Object = MibTableColumn
swRCPFileIndex = _SwRCPFileIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 82, 1, 1, 1, 1),
    _SwRCPFileIndex_Type()
)
swRCPFileIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swRCPFileIndex.setStatus("current")


class _SwRCPFileLoadType_Type(Integer32):
    """Custom type swRCPFileLoadType based on Integer32"""
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
          ("upload", 2),
          ("download", 3))
    )


_SwRCPFileLoadType_Type.__name__ = "Integer32"
_SwRCPFileLoadType_Object = MibTableColumn
swRCPFileLoadType = _SwRCPFileLoadType_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 82, 1, 1, 1, 2),
    _SwRCPFileLoadType_Type()
)
swRCPFileLoadType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swRCPFileLoadType.setStatus("current")


class _SwRCPFileType_Type(DisplayString):
    """Custom type swRCPFileType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SwRCPFileType_Type.__name__ = "DisplayString"
_SwRCPFileType_Object = MibTableColumn
swRCPFileType = _SwRCPFileType_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 82, 1, 1, 1, 3),
    _SwRCPFileType_Type()
)
swRCPFileType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swRCPFileType.setStatus("current")


class _SwRCPFileServerUserName_Type(DisplayString):
    """Custom type swRCPFileServerUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_SwRCPFileServerUserName_Type.__name__ = "DisplayString"
_SwRCPFileServerUserName_Object = MibTableColumn
swRCPFileServerUserName = _SwRCPFileServerUserName_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 82, 1, 1, 1, 4),
    _SwRCPFileServerUserName_Type()
)
swRCPFileServerUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swRCPFileServerUserName.setStatus("current")
_SwRCPFileServerAddrType_Type = InetAddressType
_SwRCPFileServerAddrType_Object = MibTableColumn
swRCPFileServerAddrType = _SwRCPFileServerAddrType_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 82, 1, 1, 1, 5),
    _SwRCPFileServerAddrType_Type()
)
swRCPFileServerAddrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swRCPFileServerAddrType.setStatus("current")
_SwRCPFileServerAddr_Type = InetAddress
_SwRCPFileServerAddr_Object = MibTableColumn
swRCPFileServerAddr = _SwRCPFileServerAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 82, 1, 1, 1, 6),
    _SwRCPFileServerAddr_Type()
)
swRCPFileServerAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swRCPFileServerAddr.setStatus("current")


class _SwRCPFileServerPathFileName_Type(DisplayString):
    """Custom type swRCPFileServerPathFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_SwRCPFileServerPathFileName_Type.__name__ = "DisplayString"
_SwRCPFileServerPathFileName_Object = MibTableColumn
swRCPFileServerPathFileName = _SwRCPFileServerPathFileName_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 82, 1, 1, 1, 7),
    _SwRCPFileServerPathFileName_Type()
)
swRCPFileServerPathFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swRCPFileServerPathFileName.setStatus("current")
_SwRCPFileUnitID_Type = UnitList
_SwRCPFileUnitID_Object = MibTableColumn
swRCPFileUnitID = _SwRCPFileUnitID_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 82, 1, 1, 1, 8),
    _SwRCPFileUnitID_Type()
)
swRCPFileUnitID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swRCPFileUnitID.setStatus("current")
_SwRCPFileCtrlID_Type = Integer32
_SwRCPFileCtrlID_Object = MibTableColumn
swRCPFileCtrlID = _SwRCPFileCtrlID_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 82, 1, 1, 1, 9),
    _SwRCPFileCtrlID_Type()
)
swRCPFileCtrlID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swRCPFileCtrlID.setStatus("current")
_SwRCPFileBootUpImage_Type = TruthValue
_SwRCPFileBootUpImage_Object = MibTableColumn
swRCPFileBootUpImage = _SwRCPFileBootUpImage_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 82, 1, 1, 1, 10),
    _SwRCPFileBootUpImage_Type()
)
swRCPFileBootUpImage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swRCPFileBootUpImage.setStatus("current")
_SwRCPFileForceAgree_Type = TruthValue
_SwRCPFileForceAgree_Object = MibTableColumn
swRCPFileForceAgree = _SwRCPFileForceAgree_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 82, 1, 1, 1, 11),
    _SwRCPFileForceAgree_Type()
)
swRCPFileForceAgree.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swRCPFileForceAgree.setStatus("current")


class _SwRCPFileCtrl_Type(Integer32):
    """Custom type swRCPFileCtrl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("start", 2))
    )


_SwRCPFileCtrl_Type.__name__ = "Integer32"
_SwRCPFileCtrl_Object = MibTableColumn
swRCPFileCtrl = _SwRCPFileCtrl_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 82, 1, 1, 1, 12),
    _SwRCPFileCtrl_Type()
)
swRCPFileCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swRCPFileCtrl.setStatus("current")
_SwRCPFileSystemTable_Object = MibTable
swRCPFileSystemTable = _SwRCPFileSystemTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 82, 1, 2)
)
if mibBuilder.loadTexts:
    swRCPFileSystemTable.setStatus("current")
_SwRCPFileSystemEntry_Object = MibTableRow
swRCPFileSystemEntry = _SwRCPFileSystemEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 82, 1, 2, 1)
)
swRCPFileSystemEntry.setIndexNames(
    (0, "RCP-MIB", "swRCPFileSystemIndex"),
)
if mibBuilder.loadTexts:
    swRCPFileSystemEntry.setStatus("current")
_SwRCPFileSystemIndex_Type = Integer32
_SwRCPFileSystemIndex_Object = MibTableColumn
swRCPFileSystemIndex = _SwRCPFileSystemIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 82, 1, 2, 1, 1),
    _SwRCPFileSystemIndex_Type()
)
swRCPFileSystemIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swRCPFileSystemIndex.setStatus("current")


class _SwRCPFileSystemLoadType_Type(Integer32):
    """Custom type swRCPFileSystemLoadType based on Integer32"""
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
          ("upload", 2),
          ("download", 3))
    )


_SwRCPFileSystemLoadType_Type.__name__ = "Integer32"
_SwRCPFileSystemLoadType_Object = MibTableColumn
swRCPFileSystemLoadType = _SwRCPFileSystemLoadType_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 82, 1, 2, 1, 2),
    _SwRCPFileSystemLoadType_Type()
)
swRCPFileSystemLoadType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swRCPFileSystemLoadType.setStatus("current")


class _SwRCPFileSystemFileType_Type(DisplayString):
    """Custom type swRCPFileSystemFileType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SwRCPFileSystemFileType_Type.__name__ = "DisplayString"
_SwRCPFileSystemFileType_Object = MibTableColumn
swRCPFileSystemFileType = _SwRCPFileSystemFileType_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 82, 1, 2, 1, 3),
    _SwRCPFileSystemFileType_Type()
)
swRCPFileSystemFileType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swRCPFileSystemFileType.setStatus("current")


class _SwRCPFileSystemServerUserName_Type(DisplayString):
    """Custom type swRCPFileSystemServerUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_SwRCPFileSystemServerUserName_Type.__name__ = "DisplayString"
_SwRCPFileSystemServerUserName_Object = MibTableColumn
swRCPFileSystemServerUserName = _SwRCPFileSystemServerUserName_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 82, 1, 2, 1, 4),
    _SwRCPFileSystemServerUserName_Type()
)
swRCPFileSystemServerUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swRCPFileSystemServerUserName.setStatus("current")
_SwRCPFileSystemServerAddrType_Type = InetAddressType
_SwRCPFileSystemServerAddrType_Object = MibTableColumn
swRCPFileSystemServerAddrType = _SwRCPFileSystemServerAddrType_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 82, 1, 2, 1, 5),
    _SwRCPFileSystemServerAddrType_Type()
)
swRCPFileSystemServerAddrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swRCPFileSystemServerAddrType.setStatus("current")
_SwRCPFileSystemServerAddr_Type = InetAddress
_SwRCPFileSystemServerAddr_Object = MibTableColumn
swRCPFileSystemServerAddr = _SwRCPFileSystemServerAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 82, 1, 2, 1, 6),
    _SwRCPFileSystemServerAddr_Type()
)
swRCPFileSystemServerAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swRCPFileSystemServerAddr.setStatus("current")


class _SwRCPFileSystemServerPathFileName_Type(DisplayString):
    """Custom type swRCPFileSystemServerPathFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_SwRCPFileSystemServerPathFileName_Type.__name__ = "DisplayString"
_SwRCPFileSystemServerPathFileName_Object = MibTableColumn
swRCPFileSystemServerPathFileName = _SwRCPFileSystemServerPathFileName_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 82, 1, 2, 1, 7),
    _SwRCPFileSystemServerPathFileName_Type()
)
swRCPFileSystemServerPathFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swRCPFileSystemServerPathFileName.setStatus("current")


class _SwRCPFileSystemDevicePathFileName_Type(DisplayString):
    """Custom type swRCPFileSystemDevicePathFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_SwRCPFileSystemDevicePathFileName_Type.__name__ = "DisplayString"
_SwRCPFileSystemDevicePathFileName_Object = MibTableColumn
swRCPFileSystemDevicePathFileName = _SwRCPFileSystemDevicePathFileName_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 82, 1, 2, 1, 8),
    _SwRCPFileSystemDevicePathFileName_Type()
)
swRCPFileSystemDevicePathFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swRCPFileSystemDevicePathFileName.setStatus("current")
_SwRCPFileSystemUnitID_Type = UnitList
_SwRCPFileSystemUnitID_Object = MibTableColumn
swRCPFileSystemUnitID = _SwRCPFileSystemUnitID_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 82, 1, 2, 1, 9),
    _SwRCPFileSystemUnitID_Type()
)
swRCPFileSystemUnitID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swRCPFileSystemUnitID.setStatus("current")
_SwRCPFileSystemBootUpImage_Type = TruthValue
_SwRCPFileSystemBootUpImage_Object = MibTableColumn
swRCPFileSystemBootUpImage = _SwRCPFileSystemBootUpImage_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 82, 1, 2, 1, 10),
    _SwRCPFileSystemBootUpImage_Type()
)
swRCPFileSystemBootUpImage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swRCPFileSystemBootUpImage.setStatus("current")
_SwRCPFileSystemForceAgree_Type = TruthValue
_SwRCPFileSystemForceAgree_Object = MibTableColumn
swRCPFileSystemForceAgree = _SwRCPFileSystemForceAgree_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 82, 1, 2, 1, 11),
    _SwRCPFileSystemForceAgree_Type()
)
swRCPFileSystemForceAgree.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swRCPFileSystemForceAgree.setStatus("current")


class _SwRCPFileSystemCtrl_Type(Integer32):
    """Custom type swRCPFileSystemCtrl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("start", 2))
    )


_SwRCPFileSystemCtrl_Type.__name__ = "Integer32"
_SwRCPFileSystemCtrl_Object = MibTableColumn
swRCPFileSystemCtrl = _SwRCPFileSystemCtrl_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 82, 1, 2, 1, 12),
    _SwRCPFileSystemCtrl_Type()
)
swRCPFileSystemCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swRCPFileSystemCtrl.setStatus("current")
_SwRCPServerConfigTable_Object = MibTable
swRCPServerConfigTable = _SwRCPServerConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 82, 1, 3)
)
if mibBuilder.loadTexts:
    swRCPServerConfigTable.setStatus("current")
_SwRCPServerConfigEntry_Object = MibTableRow
swRCPServerConfigEntry = _SwRCPServerConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 82, 1, 3, 1)
)
swRCPServerConfigEntry.setIndexNames(
    (0, "RCP-MIB", "swRCPServerConfigIndex"),
)
if mibBuilder.loadTexts:
    swRCPServerConfigEntry.setStatus("current")
_SwRCPServerConfigIndex_Type = Integer32
_SwRCPServerConfigIndex_Object = MibTableColumn
swRCPServerConfigIndex = _SwRCPServerConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 82, 1, 3, 1, 1),
    _SwRCPServerConfigIndex_Type()
)
swRCPServerConfigIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swRCPServerConfigIndex.setStatus("current")
_SwRCPServerConfigAddrType_Type = InetAddressType
_SwRCPServerConfigAddrType_Object = MibTableColumn
swRCPServerConfigAddrType = _SwRCPServerConfigAddrType_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 82, 1, 3, 1, 2),
    _SwRCPServerConfigAddrType_Type()
)
swRCPServerConfigAddrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swRCPServerConfigAddrType.setStatus("current")
_SwRCPServerConfigAddr_Type = InetAddress
_SwRCPServerConfigAddr_Object = MibTableColumn
swRCPServerConfigAddr = _SwRCPServerConfigAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 82, 1, 3, 1, 3),
    _SwRCPServerConfigAddr_Type()
)
swRCPServerConfigAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swRCPServerConfigAddr.setStatus("current")


class _SwRCPServerConfigUserName_Type(DisplayString):
    """Custom type swRCPServerConfigUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_SwRCPServerConfigUserName_Type.__name__ = "DisplayString"
_SwRCPServerConfigUserName_Object = MibTableColumn
swRCPServerConfigUserName = _SwRCPServerConfigUserName_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 82, 1, 3, 1, 4),
    _SwRCPServerConfigUserName_Type()
)
swRCPServerConfigUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swRCPServerConfigUserName.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RCP-MIB",
    **{"UnitList": UnitList,
       "swRCPMIB": swRCPMIB,
       "swRCPMgmt": swRCPMgmt,
       "swRCPFileTable": swRCPFileTable,
       "swRCPFileEntry": swRCPFileEntry,
       "swRCPFileIndex": swRCPFileIndex,
       "swRCPFileLoadType": swRCPFileLoadType,
       "swRCPFileType": swRCPFileType,
       "swRCPFileServerUserName": swRCPFileServerUserName,
       "swRCPFileServerAddrType": swRCPFileServerAddrType,
       "swRCPFileServerAddr": swRCPFileServerAddr,
       "swRCPFileServerPathFileName": swRCPFileServerPathFileName,
       "swRCPFileUnitID": swRCPFileUnitID,
       "swRCPFileCtrlID": swRCPFileCtrlID,
       "swRCPFileBootUpImage": swRCPFileBootUpImage,
       "swRCPFileForceAgree": swRCPFileForceAgree,
       "swRCPFileCtrl": swRCPFileCtrl,
       "swRCPFileSystemTable": swRCPFileSystemTable,
       "swRCPFileSystemEntry": swRCPFileSystemEntry,
       "swRCPFileSystemIndex": swRCPFileSystemIndex,
       "swRCPFileSystemLoadType": swRCPFileSystemLoadType,
       "swRCPFileSystemFileType": swRCPFileSystemFileType,
       "swRCPFileSystemServerUserName": swRCPFileSystemServerUserName,
       "swRCPFileSystemServerAddrType": swRCPFileSystemServerAddrType,
       "swRCPFileSystemServerAddr": swRCPFileSystemServerAddr,
       "swRCPFileSystemServerPathFileName": swRCPFileSystemServerPathFileName,
       "swRCPFileSystemDevicePathFileName": swRCPFileSystemDevicePathFileName,
       "swRCPFileSystemUnitID": swRCPFileSystemUnitID,
       "swRCPFileSystemBootUpImage": swRCPFileSystemBootUpImage,
       "swRCPFileSystemForceAgree": swRCPFileSystemForceAgree,
       "swRCPFileSystemCtrl": swRCPFileSystemCtrl,
       "swRCPServerConfigTable": swRCPServerConfigTable,
       "swRCPServerConfigEntry": swRCPServerConfigEntry,
       "swRCPServerConfigIndex": swRCPServerConfigIndex,
       "swRCPServerConfigAddrType": swRCPServerConfigAddrType,
       "swRCPServerConfigAddr": swRCPServerConfigAddr,
       "swRCPServerConfigUserName": swRCPServerConfigUserName}
)
