# SNMP MIB module (ZTE-AN-REMOTE-UNIT-MGMT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/zte/ZTE-AN-REMOTE-UNIT-MGMT-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:45:02 2025
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

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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

(ZxAnIfindex,
 zxAn) = mibBuilder.importSymbols(
    "ZTE-AN-TC-MIB",
    "ZxAnIfindex",
    "zxAn")


# MODULE-IDENTITY

zxAnRemoteUnitMgmtMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 80)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ZxAnRemoteUnitSoftware_ObjectIdentity = ObjectIdentity
zxAnRemoteUnitSoftware = _ZxAnRemoteUnitSoftware_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 80, 1)
)
_ZxAnRuSwGlobalObjects_ObjectIdentity = ObjectIdentity
zxAnRuSwGlobalObjects = _ZxAnRuSwGlobalObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 80, 1, 1)
)
_ZxAnRuSwFtpServerObjects_ObjectIdentity = ObjectIdentity
zxAnRuSwFtpServerObjects = _ZxAnRuSwFtpServerObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 80, 1, 1, 1)
)


class _ZxAnRuSwFtpServerProtocolType_Type(Integer32):
    """Custom type zxAnRuSwFtpServerProtocolType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ftp", 1),
          ("sftp", 2))
    )


_ZxAnRuSwFtpServerProtocolType_Type.__name__ = "Integer32"
_ZxAnRuSwFtpServerProtocolType_Object = MibScalar
zxAnRuSwFtpServerProtocolType = _ZxAnRuSwFtpServerProtocolType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 80, 1, 1, 1, 1),
    _ZxAnRuSwFtpServerProtocolType_Type()
)
zxAnRuSwFtpServerProtocolType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnRuSwFtpServerProtocolType.setStatus("current")
_ZxAnRuSwFtpServerIpAddrType_Type = InetAddressType
_ZxAnRuSwFtpServerIpAddrType_Object = MibScalar
zxAnRuSwFtpServerIpAddrType = _ZxAnRuSwFtpServerIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 80, 1, 1, 1, 2),
    _ZxAnRuSwFtpServerIpAddrType_Type()
)
zxAnRuSwFtpServerIpAddrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnRuSwFtpServerIpAddrType.setStatus("current")
_ZxAnRuSwFtpServerIpAddr_Type = InetAddress
_ZxAnRuSwFtpServerIpAddr_Object = MibScalar
zxAnRuSwFtpServerIpAddr = _ZxAnRuSwFtpServerIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 80, 1, 1, 1, 3),
    _ZxAnRuSwFtpServerIpAddr_Type()
)
zxAnRuSwFtpServerIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnRuSwFtpServerIpAddr.setStatus("current")


class _ZxAnRuSwFtpServerUserName_Type(DisplayString):
    """Custom type zxAnRuSwFtpServerUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_ZxAnRuSwFtpServerUserName_Type.__name__ = "DisplayString"
_ZxAnRuSwFtpServerUserName_Object = MibScalar
zxAnRuSwFtpServerUserName = _ZxAnRuSwFtpServerUserName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 80, 1, 1, 1, 4),
    _ZxAnRuSwFtpServerUserName_Type()
)
zxAnRuSwFtpServerUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnRuSwFtpServerUserName.setStatus("current")


class _ZxAnRuSwFtpServerUserPassword_Type(DisplayString):
    """Custom type zxAnRuSwFtpServerUserPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ZxAnRuSwFtpServerUserPassword_Type.__name__ = "DisplayString"
_ZxAnRuSwFtpServerUserPassword_Object = MibScalar
zxAnRuSwFtpServerUserPassword = _ZxAnRuSwFtpServerUserPassword_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 80, 1, 1, 1, 5),
    _ZxAnRuSwFtpServerUserPassword_Type()
)
zxAnRuSwFtpServerUserPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnRuSwFtpServerUserPassword.setStatus("current")


class _ZxAnRuCapabilities_Type(Bits):
    """Custom type zxAnRuCapabilities based on Bits"""
    namedValues = NamedValues(
        ("parallelLmtEnable", 0)
    )

_ZxAnRuCapabilities_Type.__name__ = "Bits"
_ZxAnRuCapabilities_Object = MibScalar
zxAnRuCapabilities = _ZxAnRuCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 80, 1, 1, 100),
    _ZxAnRuCapabilities_Type()
)
zxAnRuCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnRuCapabilities.setStatus("current")
_ZxAnRuSwObjects_ObjectIdentity = ObjectIdentity
zxAnRuSwObjects = _ZxAnRuSwObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 80, 1, 2)
)
_ZxAnRuSwManualUpdateObjects_ObjectIdentity = ObjectIdentity
zxAnRuSwManualUpdateObjects = _ZxAnRuSwManualUpdateObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 80, 1, 2, 1)
)


class _ZxAnRuSwManualUpdateList_Type(OctetString):
    """Custom type zxAnRuSwManualUpdateList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 2048),
    )


_ZxAnRuSwManualUpdateList_Type.__name__ = "OctetString"
_ZxAnRuSwManualUpdateList_Object = MibScalar
zxAnRuSwManualUpdateList = _ZxAnRuSwManualUpdateList_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 80, 1, 2, 1, 1),
    _ZxAnRuSwManualUpdateList_Type()
)
zxAnRuSwManualUpdateList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnRuSwManualUpdateList.setStatus("current")


class _ZxAnRuSwManualUpdateAction_Type(Integer32):
    """Custom type zxAnRuSwManualUpdateAction based on Integer32"""
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
        *(("update", 1),
          ("updateAndReboot", 2),
          ("activate", 3),
          ("commit", 4),
          ("abort", 5),
          ("updateLinkup", 6),
          ("updateAndCommit", 7))
    )


_ZxAnRuSwManualUpdateAction_Type.__name__ = "Integer32"
_ZxAnRuSwManualUpdateAction_Object = MibScalar
zxAnRuSwManualUpdateAction = _ZxAnRuSwManualUpdateAction_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 80, 1, 2, 1, 6),
    _ZxAnRuSwManualUpdateAction_Type()
)
zxAnRuSwManualUpdateAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnRuSwManualUpdateAction.setStatus("current")


class _ZxAnRuSwManualUpdateFileName_Type(DisplayString):
    """Custom type zxAnRuSwManualUpdateFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_ZxAnRuSwManualUpdateFileName_Type.__name__ = "DisplayString"
_ZxAnRuSwManualUpdateFileName_Object = MibScalar
zxAnRuSwManualUpdateFileName = _ZxAnRuSwManualUpdateFileName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 80, 1, 2, 1, 7),
    _ZxAnRuSwManualUpdateFileName_Type()
)
zxAnRuSwManualUpdateFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnRuSwManualUpdateFileName.setStatus("current")


class _ZxAnRuSwManualUpdateLocate_Type(Integer32):
    """Custom type zxAnRuSwManualUpdateLocate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("local", 1),
          ("remote", 2))
    )


_ZxAnRuSwManualUpdateLocate_Type.__name__ = "Integer32"
_ZxAnRuSwManualUpdateLocate_Object = MibScalar
zxAnRuSwManualUpdateLocate = _ZxAnRuSwManualUpdateLocate_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 80, 1, 2, 1, 8),
    _ZxAnRuSwManualUpdateLocate_Type()
)
zxAnRuSwManualUpdateLocate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnRuSwManualUpdateLocate.setStatus("current")
_ZxAnRuSwUpdatingTaskTable_Object = MibTable
zxAnRuSwUpdatingTaskTable = _ZxAnRuSwUpdatingTaskTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 80, 1, 2, 2)
)
if mibBuilder.loadTexts:
    zxAnRuSwUpdatingTaskTable.setStatus("current")
_ZxAnRuSwUpdatingTaskEntry_Object = MibTableRow
zxAnRuSwUpdatingTaskEntry = _ZxAnRuSwUpdatingTaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 80, 1, 2, 2, 1)
)
zxAnRuSwUpdatingTaskEntry.setIndexNames(
    (0, "ZTE-AN-REMOTE-UNIT-MGMT-MIB", "zxAnRuSwUpdatingTaskName"),
)
if mibBuilder.loadTexts:
    zxAnRuSwUpdatingTaskEntry.setStatus("current")


class _ZxAnRuSwUpdatingTaskName_Type(DisplayString):
    """Custom type zxAnRuSwUpdatingTaskName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_ZxAnRuSwUpdatingTaskName_Type.__name__ = "DisplayString"
_ZxAnRuSwUpdatingTaskName_Object = MibTableColumn
zxAnRuSwUpdatingTaskName = _ZxAnRuSwUpdatingTaskName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 80, 1, 2, 2, 1, 1),
    _ZxAnRuSwUpdatingTaskName_Type()
)
zxAnRuSwUpdatingTaskName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnRuSwUpdatingTaskName.setStatus("current")


class _ZxAnRuSwUpdatingTaskDesc_Type(DisplayString):
    """Custom type zxAnRuSwUpdatingTaskDesc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_ZxAnRuSwUpdatingTaskDesc_Type.__name__ = "DisplayString"
_ZxAnRuSwUpdatingTaskDesc_Object = MibTableColumn
zxAnRuSwUpdatingTaskDesc = _ZxAnRuSwUpdatingTaskDesc_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 80, 1, 2, 2, 1, 2),
    _ZxAnRuSwUpdatingTaskDesc_Type()
)
zxAnRuSwUpdatingTaskDesc.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnRuSwUpdatingTaskDesc.setStatus("current")


class _ZxAnRuSwUpdatingTaskMode_Type(Integer32):
    """Custom type zxAnRuSwUpdatingTaskMode based on Integer32"""
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
        *(("online", 1),
          ("offline", 2),
          ("both", 3))
    )


_ZxAnRuSwUpdatingTaskMode_Type.__name__ = "Integer32"
_ZxAnRuSwUpdatingTaskMode_Object = MibTableColumn
zxAnRuSwUpdatingTaskMode = _ZxAnRuSwUpdatingTaskMode_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 80, 1, 2, 2, 1, 3),
    _ZxAnRuSwUpdatingTaskMode_Type()
)
zxAnRuSwUpdatingTaskMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnRuSwUpdatingTaskMode.setStatus("current")


class _ZxAnRuSwUpdatingTaskServiceType_Type(DisplayString):
    """Custom type zxAnRuSwUpdatingTaskServiceType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_ZxAnRuSwUpdatingTaskServiceType_Type.__name__ = "DisplayString"
_ZxAnRuSwUpdatingTaskServiceType_Object = MibTableColumn
zxAnRuSwUpdatingTaskServiceType = _ZxAnRuSwUpdatingTaskServiceType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 80, 1, 2, 2, 1, 4),
    _ZxAnRuSwUpdatingTaskServiceType_Type()
)
zxAnRuSwUpdatingTaskServiceType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnRuSwUpdatingTaskServiceType.setStatus("current")


class _ZxAnRuSwUpdatingTaskVendor_Type(DisplayString):
    """Custom type zxAnRuSwUpdatingTaskVendor based on DisplayString"""
    defaultValue = OctetString("zte")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_ZxAnRuSwUpdatingTaskVendor_Type.__name__ = "DisplayString"
_ZxAnRuSwUpdatingTaskVendor_Object = MibTableColumn
zxAnRuSwUpdatingTaskVendor = _ZxAnRuSwUpdatingTaskVendor_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 80, 1, 2, 2, 1, 5),
    _ZxAnRuSwUpdatingTaskVendor_Type()
)
zxAnRuSwUpdatingTaskVendor.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnRuSwUpdatingTaskVendor.setStatus("current")


class _ZxAnRuSwUpdatingTaskEquipType_Type(DisplayString):
    """Custom type zxAnRuSwUpdatingTaskEquipType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_ZxAnRuSwUpdatingTaskEquipType_Type.__name__ = "DisplayString"
_ZxAnRuSwUpdatingTaskEquipType_Object = MibTableColumn
zxAnRuSwUpdatingTaskEquipType = _ZxAnRuSwUpdatingTaskEquipType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 80, 1, 2, 2, 1, 6),
    _ZxAnRuSwUpdatingTaskEquipType_Type()
)
zxAnRuSwUpdatingTaskEquipType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnRuSwUpdatingTaskEquipType.setStatus("current")


class _ZxAnRuSwUpdatingTaskCrtrnType_Type(Integer32):
    """Custom type zxAnRuSwUpdatingTaskCrtrnType based on Integer32"""
    defaultValue = 1

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
        *(("ignore", 1),
          ("equal", 2),
          ("notEqual", 3),
          ("below", 4),
          ("upper", 5))
    )


_ZxAnRuSwUpdatingTaskCrtrnType_Type.__name__ = "Integer32"
_ZxAnRuSwUpdatingTaskCrtrnType_Object = MibTableColumn
zxAnRuSwUpdatingTaskCrtrnType = _ZxAnRuSwUpdatingTaskCrtrnType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 80, 1, 2, 2, 1, 7),
    _ZxAnRuSwUpdatingTaskCrtrnType_Type()
)
zxAnRuSwUpdatingTaskCrtrnType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnRuSwUpdatingTaskCrtrnType.setStatus("current")


class _ZxAnRuSwUpdatingTaskCrtrnVer_Type(DisplayString):
    """Custom type zxAnRuSwUpdatingTaskCrtrnVer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_ZxAnRuSwUpdatingTaskCrtrnVer_Type.__name__ = "DisplayString"
_ZxAnRuSwUpdatingTaskCrtrnVer_Object = MibTableColumn
zxAnRuSwUpdatingTaskCrtrnVer = _ZxAnRuSwUpdatingTaskCrtrnVer_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 80, 1, 2, 2, 1, 8),
    _ZxAnRuSwUpdatingTaskCrtrnVer_Type()
)
zxAnRuSwUpdatingTaskCrtrnVer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnRuSwUpdatingTaskCrtrnVer.setStatus("current")


class _ZxAnRuSwUpdatingTaskOperObjType_Type(Integer32):
    """Custom type zxAnRuSwUpdatingTaskOperObjType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ne", 1),
          ("port", 2))
    )


_ZxAnRuSwUpdatingTaskOperObjType_Type.__name__ = "Integer32"
_ZxAnRuSwUpdatingTaskOperObjType_Object = MibTableColumn
zxAnRuSwUpdatingTaskOperObjType = _ZxAnRuSwUpdatingTaskOperObjType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 80, 1, 2, 2, 1, 9),
    _ZxAnRuSwUpdatingTaskOperObjType_Type()
)
zxAnRuSwUpdatingTaskOperObjType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnRuSwUpdatingTaskOperObjType.setStatus("current")


class _ZxAnRuSwUpdatingTaskOperObjList_Type(OctetString):
    """Custom type zxAnRuSwUpdatingTaskOperObjList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 2048),
    )


_ZxAnRuSwUpdatingTaskOperObjList_Type.__name__ = "OctetString"
_ZxAnRuSwUpdatingTaskOperObjList_Object = MibTableColumn
zxAnRuSwUpdatingTaskOperObjList = _ZxAnRuSwUpdatingTaskOperObjList_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 80, 1, 2, 2, 1, 10),
    _ZxAnRuSwUpdatingTaskOperObjList_Type()
)
zxAnRuSwUpdatingTaskOperObjList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnRuSwUpdatingTaskOperObjList.setStatus("current")


class _ZxAnRuSwUpdatingTaskAction_Type(Integer32):
    """Custom type zxAnRuSwUpdatingTaskAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("abort", 1),
          ("restart", 2))
    )


_ZxAnRuSwUpdatingTaskAction_Type.__name__ = "Integer32"
_ZxAnRuSwUpdatingTaskAction_Object = MibTableColumn
zxAnRuSwUpdatingTaskAction = _ZxAnRuSwUpdatingTaskAction_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 80, 1, 2, 2, 1, 11),
    _ZxAnRuSwUpdatingTaskAction_Type()
)
zxAnRuSwUpdatingTaskAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnRuSwUpdatingTaskAction.setStatus("current")


class _ZxAnRuSwUpdatingTaskFileName_Type(DisplayString):
    """Custom type zxAnRuSwUpdatingTaskFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_ZxAnRuSwUpdatingTaskFileName_Type.__name__ = "DisplayString"
_ZxAnRuSwUpdatingTaskFileName_Object = MibTableColumn
zxAnRuSwUpdatingTaskFileName = _ZxAnRuSwUpdatingTaskFileName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 80, 1, 2, 2, 1, 12),
    _ZxAnRuSwUpdatingTaskFileName_Type()
)
zxAnRuSwUpdatingTaskFileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnRuSwUpdatingTaskFileName.setStatus("current")


class _ZxAnRuSwUpdatingTaskFileLocate_Type(Integer32):
    """Custom type zxAnRuSwUpdatingTaskFileLocate based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("local", 1),
          ("remote", 2))
    )


_ZxAnRuSwUpdatingTaskFileLocate_Type.__name__ = "Integer32"
_ZxAnRuSwUpdatingTaskFileLocate_Object = MibTableColumn
zxAnRuSwUpdatingTaskFileLocate = _ZxAnRuSwUpdatingTaskFileLocate_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 80, 1, 2, 2, 1, 13),
    _ZxAnRuSwUpdatingTaskFileLocate_Type()
)
zxAnRuSwUpdatingTaskFileLocate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnRuSwUpdatingTaskFileLocate.setStatus("current")


class _ZxAnRuSwUpdatingTaskStatus_Type(Integer32):
    """Custom type zxAnRuSwUpdatingTaskStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("processing", 1),
          ("aborted", 2),
          ("finished", 3))
    )


_ZxAnRuSwUpdatingTaskStatus_Type.__name__ = "Integer32"
_ZxAnRuSwUpdatingTaskStatus_Object = MibTableColumn
zxAnRuSwUpdatingTaskStatus = _ZxAnRuSwUpdatingTaskStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 80, 1, 2, 2, 1, 14),
    _ZxAnRuSwUpdatingTaskStatus_Type()
)
zxAnRuSwUpdatingTaskStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnRuSwUpdatingTaskStatus.setStatus("current")


class _ZxAnRuSwUpdatingTaskRuAction_Type(Integer32):
    """Custom type zxAnRuSwUpdatingTaskRuAction based on Integer32"""
    defaultValue = 2

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
        *(("update", 1),
          ("updateAndReboot", 2),
          ("reboot", 3),
          ("updateLinkup", 4),
          ("updateAndCommit", 5))
    )


_ZxAnRuSwUpdatingTaskRuAction_Type.__name__ = "Integer32"
_ZxAnRuSwUpdatingTaskRuAction_Object = MibTableColumn
zxAnRuSwUpdatingTaskRuAction = _ZxAnRuSwUpdatingTaskRuAction_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 80, 1, 2, 2, 1, 15),
    _ZxAnRuSwUpdatingTaskRuAction_Type()
)
zxAnRuSwUpdatingTaskRuAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnRuSwUpdatingTaskRuAction.setStatus("current")


class _ZxAnRuSwUpdatingTaskParallelLmt_Type(Integer32):
    """Custom type zxAnRuSwUpdatingTaskParallelLmt based on Integer32"""
    defaultValue = 64

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_ZxAnRuSwUpdatingTaskParallelLmt_Type.__name__ = "Integer32"
_ZxAnRuSwUpdatingTaskParallelLmt_Object = MibTableColumn
zxAnRuSwUpdatingTaskParallelLmt = _ZxAnRuSwUpdatingTaskParallelLmt_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 80, 1, 2, 2, 1, 16),
    _ZxAnRuSwUpdatingTaskParallelLmt_Type()
)
zxAnRuSwUpdatingTaskParallelLmt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnRuSwUpdatingTaskParallelLmt.setStatus("current")
_ZxAnRuSwUpdatingTaskRowStatus_Type = RowStatus
_ZxAnRuSwUpdatingTaskRowStatus_Object = MibTableColumn
zxAnRuSwUpdatingTaskRowStatus = _ZxAnRuSwUpdatingTaskRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 80, 1, 2, 2, 1, 30),
    _ZxAnRuSwUpdatingTaskRowStatus_Type()
)
zxAnRuSwUpdatingTaskRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnRuSwUpdatingTaskRowStatus.setStatus("current")
_ZxAnRuSwTaskStatTable_Object = MibTable
zxAnRuSwTaskStatTable = _ZxAnRuSwTaskStatTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 80, 1, 2, 3)
)
if mibBuilder.loadTexts:
    zxAnRuSwTaskStatTable.setStatus("current")
_ZxAnRuSwTaskStatEntry_Object = MibTableRow
zxAnRuSwTaskStatEntry = _ZxAnRuSwTaskStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 80, 1, 2, 3, 1)
)
zxAnRuSwTaskStatEntry.setIndexNames(
    (0, "ZTE-AN-REMOTE-UNIT-MGMT-MIB", "zxAnRuSwUpdatingTaskName"),
)
if mibBuilder.loadTexts:
    zxAnRuSwTaskStatEntry.setStatus("current")
_ZxAnRuSwTaskStatsSuccesses_Type = Integer32
_ZxAnRuSwTaskStatsSuccesses_Object = MibTableColumn
zxAnRuSwTaskStatsSuccesses = _ZxAnRuSwTaskStatsSuccesses_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 80, 1, 2, 3, 1, 1),
    _ZxAnRuSwTaskStatsSuccesses_Type()
)
zxAnRuSwTaskStatsSuccesses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnRuSwTaskStatsSuccesses.setStatus("current")
_ZxAnRuSwTaskStatsFailures_Type = Integer32
_ZxAnRuSwTaskStatsFailures_Object = MibTableColumn
zxAnRuSwTaskStatsFailures = _ZxAnRuSwTaskStatsFailures_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 80, 1, 2, 3, 1, 2),
    _ZxAnRuSwTaskStatsFailures_Type()
)
zxAnRuSwTaskStatsFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnRuSwTaskStatsFailures.setStatus("current")
_ZxAnRuSwTaskStatsUpdatings_Type = Integer32
_ZxAnRuSwTaskStatsUpdatings_Object = MibTableColumn
zxAnRuSwTaskStatsUpdatings = _ZxAnRuSwTaskStatsUpdatings_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 80, 1, 2, 3, 1, 3),
    _ZxAnRuSwTaskStatsUpdatings_Type()
)
zxAnRuSwTaskStatsUpdatings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnRuSwTaskStatsUpdatings.setStatus("current")
_ZxAnRuSwTaskStatsWaitings_Type = Integer32
_ZxAnRuSwTaskStatsWaitings_Object = MibTableColumn
zxAnRuSwTaskStatsWaitings = _ZxAnRuSwTaskStatsWaitings_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 80, 1, 2, 3, 1, 4),
    _ZxAnRuSwTaskStatsWaitings_Type()
)
zxAnRuSwTaskStatsWaitings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnRuSwTaskStatsWaitings.setStatus("current")
_ZxAnRuSwUpdateStatusTable_Object = MibTable
zxAnRuSwUpdateStatusTable = _ZxAnRuSwUpdateStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 80, 1, 2, 4)
)
if mibBuilder.loadTexts:
    zxAnRuSwUpdateStatusTable.setStatus("current")
_ZxAnRuSwUpdateStatusEntry_Object = MibTableRow
zxAnRuSwUpdateStatusEntry = _ZxAnRuSwUpdateStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 80, 1, 2, 4, 1)
)
zxAnRuSwUpdateStatusEntry.setIndexNames(
    (0, "ZTE-AN-REMOTE-UNIT-MGMT-MIB", "zxAnRuSwRack"),
    (0, "ZTE-AN-REMOTE-UNIT-MGMT-MIB", "zxAnRuSwShelf"),
    (0, "ZTE-AN-REMOTE-UNIT-MGMT-MIB", "zxAnRuSwSlot"),
    (0, "ZTE-AN-REMOTE-UNIT-MGMT-MIB", "zxAnRuSwPort"),
    (0, "ZTE-AN-REMOTE-UNIT-MGMT-MIB", "zxAnRuSwOnu"),
)
if mibBuilder.loadTexts:
    zxAnRuSwUpdateStatusEntry.setStatus("current")
_ZxAnRuSwRack_Type = Integer32
_ZxAnRuSwRack_Object = MibTableColumn
zxAnRuSwRack = _ZxAnRuSwRack_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 80, 1, 2, 4, 1, 1),
    _ZxAnRuSwRack_Type()
)
zxAnRuSwRack.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnRuSwRack.setStatus("current")
_ZxAnRuSwShelf_Type = Integer32
_ZxAnRuSwShelf_Object = MibTableColumn
zxAnRuSwShelf = _ZxAnRuSwShelf_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 80, 1, 2, 4, 1, 2),
    _ZxAnRuSwShelf_Type()
)
zxAnRuSwShelf.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnRuSwShelf.setStatus("current")
_ZxAnRuSwSlot_Type = Integer32
_ZxAnRuSwSlot_Object = MibTableColumn
zxAnRuSwSlot = _ZxAnRuSwSlot_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 80, 1, 2, 4, 1, 3),
    _ZxAnRuSwSlot_Type()
)
zxAnRuSwSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnRuSwSlot.setStatus("current")
_ZxAnRuSwPort_Type = Integer32
_ZxAnRuSwPort_Object = MibTableColumn
zxAnRuSwPort = _ZxAnRuSwPort_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 80, 1, 2, 4, 1, 4),
    _ZxAnRuSwPort_Type()
)
zxAnRuSwPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnRuSwPort.setStatus("current")
_ZxAnRuSwOnu_Type = Integer32
_ZxAnRuSwOnu_Object = MibTableColumn
zxAnRuSwOnu = _ZxAnRuSwOnu_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 80, 1, 2, 4, 1, 5),
    _ZxAnRuSwOnu_Type()
)
zxAnRuSwOnu.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnRuSwOnu.setStatus("current")


class _ZxAnRuSwUpdateStatusServiceType_Type(DisplayString):
    """Custom type zxAnRuSwUpdateStatusServiceType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_ZxAnRuSwUpdateStatusServiceType_Type.__name__ = "DisplayString"
_ZxAnRuSwUpdateStatusServiceType_Object = MibTableColumn
zxAnRuSwUpdateStatusServiceType = _ZxAnRuSwUpdateStatusServiceType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 80, 1, 2, 4, 1, 6),
    _ZxAnRuSwUpdateStatusServiceType_Type()
)
zxAnRuSwUpdateStatusServiceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnRuSwUpdateStatusServiceType.setStatus("current")


class _ZxAnRuSwUpdateStatusEquipType_Type(DisplayString):
    """Custom type zxAnRuSwUpdateStatusEquipType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_ZxAnRuSwUpdateStatusEquipType_Type.__name__ = "DisplayString"
_ZxAnRuSwUpdateStatusEquipType_Object = MibTableColumn
zxAnRuSwUpdateStatusEquipType = _ZxAnRuSwUpdateStatusEquipType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 80, 1, 2, 4, 1, 7),
    _ZxAnRuSwUpdateStatusEquipType_Type()
)
zxAnRuSwUpdateStatusEquipType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnRuSwUpdateStatusEquipType.setStatus("current")


class _ZxAnRuSwUpdateStatusFileName_Type(DisplayString):
    """Custom type zxAnRuSwUpdateStatusFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 14),
    )


_ZxAnRuSwUpdateStatusFileName_Type.__name__ = "DisplayString"
_ZxAnRuSwUpdateStatusFileName_Object = MibTableColumn
zxAnRuSwUpdateStatusFileName = _ZxAnRuSwUpdateStatusFileName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 80, 1, 2, 4, 1, 8),
    _ZxAnRuSwUpdateStatusFileName_Type()
)
zxAnRuSwUpdateStatusFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnRuSwUpdateStatusFileName.setStatus("current")


class _ZxAnRuSwUpdateStatusResult_Type(Integer32):
    """Custom type zxAnRuSwUpdateStatusResult based on Integer32"""
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
        *(("notStarted", 1),
          ("inProgress", 2),
          ("success", 3),
          ("failure", 4),
          ("waiting", 5))
    )


_ZxAnRuSwUpdateStatusResult_Type.__name__ = "Integer32"
_ZxAnRuSwUpdateStatusResult_Object = MibTableColumn
zxAnRuSwUpdateStatusResult = _ZxAnRuSwUpdateStatusResult_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 80, 1, 2, 4, 1, 9),
    _ZxAnRuSwUpdateStatusResult_Type()
)
zxAnRuSwUpdateStatusResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnRuSwUpdateStatusResult.setStatus("current")


class _ZxAnRuSwUpdateStatusFailReason_Type(Integer32):
    """Custom type zxAnRuSwUpdateStatusFailReason based on Integer32"""
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
              9,
              10,
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("downloadErr", 2),
          ("commitErr", 3),
          ("activateErr", 4),
          ("crcErr", 5),
          ("validErr", 6),
          ("useAbort", 7),
          ("offline", 8),
          ("rebootErr", 9),
          ("ruDeleted", 10),
          ("timeout", 11),
          ("notSupport", 12))
    )


_ZxAnRuSwUpdateStatusFailReason_Type.__name__ = "Integer32"
_ZxAnRuSwUpdateStatusFailReason_Object = MibTableColumn
zxAnRuSwUpdateStatusFailReason = _ZxAnRuSwUpdateStatusFailReason_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 80, 1, 2, 4, 1, 10),
    _ZxAnRuSwUpdateStatusFailReason_Type()
)
zxAnRuSwUpdateStatusFailReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnRuSwUpdateStatusFailReason.setStatus("current")


class _ZxAnRuSwUpdateStatusProgress_Type(Integer32):
    """Custom type zxAnRuSwUpdateStatusProgress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ZxAnRuSwUpdateStatusProgress_Type.__name__ = "Integer32"
_ZxAnRuSwUpdateStatusProgress_Object = MibTableColumn
zxAnRuSwUpdateStatusProgress = _ZxAnRuSwUpdateStatusProgress_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 80, 1, 2, 4, 1, 11),
    _ZxAnRuSwUpdateStatusProgress_Type()
)
zxAnRuSwUpdateStatusProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnRuSwUpdateStatusProgress.setStatus("current")


class _ZxAnRuSwUpdateStatusSource_Type(Integer32):
    """Custom type zxAnRuSwUpdateStatusSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("task", 1),
          ("manual", 2))
    )


_ZxAnRuSwUpdateStatusSource_Type.__name__ = "Integer32"
_ZxAnRuSwUpdateStatusSource_Object = MibTableColumn
zxAnRuSwUpdateStatusSource = _ZxAnRuSwUpdateStatusSource_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 80, 1, 2, 4, 1, 12),
    _ZxAnRuSwUpdateStatusSource_Type()
)
zxAnRuSwUpdateStatusSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnRuSwUpdateStatusSource.setStatus("current")


class _ZxAnRuSwUpdateStatusTaskName_Type(DisplayString):
    """Custom type zxAnRuSwUpdateStatusTaskName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ZxAnRuSwUpdateStatusTaskName_Type.__name__ = "DisplayString"
_ZxAnRuSwUpdateStatusTaskName_Object = MibTableColumn
zxAnRuSwUpdateStatusTaskName = _ZxAnRuSwUpdateStatusTaskName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 80, 1, 2, 4, 1, 13),
    _ZxAnRuSwUpdateStatusTaskName_Type()
)
zxAnRuSwUpdateStatusTaskName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnRuSwUpdateStatusTaskName.setStatus("current")


class _ZxAnRuSwUpdateStatusModifyTime_Type(DisplayString):
    """Custom type zxAnRuSwUpdateStatusModifyTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 19),
    )


_ZxAnRuSwUpdateStatusModifyTime_Type.__name__ = "DisplayString"
_ZxAnRuSwUpdateStatusModifyTime_Object = MibTableColumn
zxAnRuSwUpdateStatusModifyTime = _ZxAnRuSwUpdateStatusModifyTime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 80, 1, 2, 4, 1, 14),
    _ZxAnRuSwUpdateStatusModifyTime_Type()
)
zxAnRuSwUpdateStatusModifyTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnRuSwUpdateStatusModifyTime.setStatus("current")


class _ZxAnRuSwUpdateStatusCurrVersion_Type(DisplayString):
    """Custom type zxAnRuSwUpdateStatusCurrVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 14),
    )


_ZxAnRuSwUpdateStatusCurrVersion_Type.__name__ = "DisplayString"
_ZxAnRuSwUpdateStatusCurrVersion_Object = MibTableColumn
zxAnRuSwUpdateStatusCurrVersion = _ZxAnRuSwUpdateStatusCurrVersion_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 80, 1, 2, 4, 1, 15),
    _ZxAnRuSwUpdateStatusCurrVersion_Type()
)
zxAnRuSwUpdateStatusCurrVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnRuSwUpdateStatusCurrVersion.setStatus("current")


class _ZxAnRuSwUpdateStatusLastVersion_Type(DisplayString):
    """Custom type zxAnRuSwUpdateStatusLastVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 14),
    )


_ZxAnRuSwUpdateStatusLastVersion_Type.__name__ = "DisplayString"
_ZxAnRuSwUpdateStatusLastVersion_Object = MibTableColumn
zxAnRuSwUpdateStatusLastVersion = _ZxAnRuSwUpdateStatusLastVersion_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 80, 1, 2, 4, 1, 16),
    _ZxAnRuSwUpdateStatusLastVersion_Type()
)
zxAnRuSwUpdateStatusLastVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnRuSwUpdateStatusLastVersion.setStatus("current")
_ZxAnRuSwImageTable_Object = MibTable
zxAnRuSwImageTable = _ZxAnRuSwImageTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 80, 1, 2, 5)
)
if mibBuilder.loadTexts:
    zxAnRuSwImageTable.setStatus("current")
_ZxAnRuSwImageEntry_Object = MibTableRow
zxAnRuSwImageEntry = _ZxAnRuSwImageEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 80, 1, 2, 5, 1)
)
zxAnRuSwImageEntry.setIndexNames(
    (0, "ZTE-AN-REMOTE-UNIT-MGMT-MIB", "zxAnRuSwRack"),
    (0, "ZTE-AN-REMOTE-UNIT-MGMT-MIB", "zxAnRuSwShelf"),
    (0, "ZTE-AN-REMOTE-UNIT-MGMT-MIB", "zxAnRuSwSlot"),
    (0, "ZTE-AN-REMOTE-UNIT-MGMT-MIB", "zxAnRuSwPort"),
    (0, "ZTE-AN-REMOTE-UNIT-MGMT-MIB", "zxAnRuSwOnu"),
    (0, "ZTE-AN-REMOTE-UNIT-MGMT-MIB", "zxAnRuSwImageIndex"),
)
if mibBuilder.loadTexts:
    zxAnRuSwImageEntry.setStatus("current")
_ZxAnRuSwImageRack_Type = Integer32
_ZxAnRuSwImageRack_Object = MibTableColumn
zxAnRuSwImageRack = _ZxAnRuSwImageRack_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 80, 1, 2, 5, 1, 1),
    _ZxAnRuSwImageRack_Type()
)
zxAnRuSwImageRack.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnRuSwImageRack.setStatus("current")
_ZxAnRuSwImageShelf_Type = Integer32
_ZxAnRuSwImageShelf_Object = MibTableColumn
zxAnRuSwImageShelf = _ZxAnRuSwImageShelf_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 80, 1, 2, 5, 1, 2),
    _ZxAnRuSwImageShelf_Type()
)
zxAnRuSwImageShelf.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnRuSwImageShelf.setStatus("current")
_ZxAnRuSwImageSlot_Type = Integer32
_ZxAnRuSwImageSlot_Object = MibTableColumn
zxAnRuSwImageSlot = _ZxAnRuSwImageSlot_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 80, 1, 2, 5, 1, 3),
    _ZxAnRuSwImageSlot_Type()
)
zxAnRuSwImageSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnRuSwImageSlot.setStatus("current")
_ZxAnRuSwImagePort_Type = Integer32
_ZxAnRuSwImagePort_Object = MibTableColumn
zxAnRuSwImagePort = _ZxAnRuSwImagePort_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 80, 1, 2, 5, 1, 4),
    _ZxAnRuSwImagePort_Type()
)
zxAnRuSwImagePort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnRuSwImagePort.setStatus("current")
_ZxAnRuSwImageOnu_Type = Integer32
_ZxAnRuSwImageOnu_Object = MibTableColumn
zxAnRuSwImageOnu = _ZxAnRuSwImageOnu_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 80, 1, 2, 5, 1, 5),
    _ZxAnRuSwImageOnu_Type()
)
zxAnRuSwImageOnu.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnRuSwImageOnu.setStatus("current")


class _ZxAnRuSwImageIndex_Type(Integer32):
    """Custom type zxAnRuSwImageIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ZxAnRuSwImageIndex_Type.__name__ = "Integer32"
_ZxAnRuSwImageIndex_Object = MibTableColumn
zxAnRuSwImageIndex = _ZxAnRuSwImageIndex_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 80, 1, 2, 5, 1, 6),
    _ZxAnRuSwImageIndex_Type()
)
zxAnRuSwImageIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnRuSwImageIndex.setStatus("current")


class _ZxAnRuSwImageVersion_Type(DisplayString):
    """Custom type zxAnRuSwImageVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 14),
    )


_ZxAnRuSwImageVersion_Type.__name__ = "DisplayString"
_ZxAnRuSwImageVersion_Object = MibTableColumn
zxAnRuSwImageVersion = _ZxAnRuSwImageVersion_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 80, 1, 2, 5, 1, 7),
    _ZxAnRuSwImageVersion_Type()
)
zxAnRuSwImageVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnRuSwImageVersion.setStatus("current")


class _ZxAnRuSwImageStatus_Type(Bits):
    """Custom type zxAnRuSwImageStatus based on Bits"""
    namedValues = NamedValues(
        *(("isCommitted", 0),
          ("isActive", 1),
          ("isValid", 2))
    )

_ZxAnRuSwImageStatus_Type.__name__ = "Bits"
_ZxAnRuSwImageStatus_Object = MibTableColumn
zxAnRuSwImageStatus = _ZxAnRuSwImageStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 80, 1, 2, 5, 1, 8),
    _ZxAnRuSwImageStatus_Type()
)
zxAnRuSwImageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnRuSwImageStatus.setStatus("current")
_ZxAnRuSwNotifications_ObjectIdentity = ObjectIdentity
zxAnRuSwNotifications = _ZxAnRuSwNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 80, 1, 20)
)

# Managed Objects groups


# Notification objects

zxAnRuSwUpdatedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 80, 1, 20, 1)
)
zxAnRuSwUpdatedTrap.setObjects(
      *(("ZTE-AN-REMOTE-UNIT-MGMT-MIB", "zxAnRuSwUpdateStatusServiceType"),
        ("ZTE-AN-REMOTE-UNIT-MGMT-MIB", "zxAnRuSwUpdateStatusEquipType"),
        ("ZTE-AN-REMOTE-UNIT-MGMT-MIB", "zxAnRuSwUpdateStatusFileName"),
        ("ZTE-AN-REMOTE-UNIT-MGMT-MIB", "zxAnRuSwUpdateStatusResult"),
        ("ZTE-AN-REMOTE-UNIT-MGMT-MIB", "zxAnRuSwUpdateStatusFailReason"),
        ("ZTE-AN-REMOTE-UNIT-MGMT-MIB", "zxAnRuSwUpdateStatusSource"),
        ("ZTE-AN-REMOTE-UNIT-MGMT-MIB", "zxAnRuSwUpdateStatusTaskName"),
        ("ZTE-AN-REMOTE-UNIT-MGMT-MIB", "zxAnRuSwUpdateStatusCurrVersion"),
        ("ZTE-AN-REMOTE-UNIT-MGMT-MIB", "zxAnRuSwUpdateStatusLastVersion"),
        ("ZTE-AN-REMOTE-UNIT-MGMT-MIB", "zxAnRuSwUpdateStatusModifyTime"))
)
if mibBuilder.loadTexts:
    zxAnRuSwUpdatedTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZTE-AN-REMOTE-UNIT-MGMT-MIB",
    **{"zxAnRemoteUnitMgmtMib": zxAnRemoteUnitMgmtMib,
       "zxAnRemoteUnitSoftware": zxAnRemoteUnitSoftware,
       "zxAnRuSwGlobalObjects": zxAnRuSwGlobalObjects,
       "zxAnRuSwFtpServerObjects": zxAnRuSwFtpServerObjects,
       "zxAnRuSwFtpServerProtocolType": zxAnRuSwFtpServerProtocolType,
       "zxAnRuSwFtpServerIpAddrType": zxAnRuSwFtpServerIpAddrType,
       "zxAnRuSwFtpServerIpAddr": zxAnRuSwFtpServerIpAddr,
       "zxAnRuSwFtpServerUserName": zxAnRuSwFtpServerUserName,
       "zxAnRuSwFtpServerUserPassword": zxAnRuSwFtpServerUserPassword,
       "zxAnRuCapabilities": zxAnRuCapabilities,
       "zxAnRuSwObjects": zxAnRuSwObjects,
       "zxAnRuSwManualUpdateObjects": zxAnRuSwManualUpdateObjects,
       "zxAnRuSwManualUpdateList": zxAnRuSwManualUpdateList,
       "zxAnRuSwManualUpdateAction": zxAnRuSwManualUpdateAction,
       "zxAnRuSwManualUpdateFileName": zxAnRuSwManualUpdateFileName,
       "zxAnRuSwManualUpdateLocate": zxAnRuSwManualUpdateLocate,
       "zxAnRuSwUpdatingTaskTable": zxAnRuSwUpdatingTaskTable,
       "zxAnRuSwUpdatingTaskEntry": zxAnRuSwUpdatingTaskEntry,
       "zxAnRuSwUpdatingTaskName": zxAnRuSwUpdatingTaskName,
       "zxAnRuSwUpdatingTaskDesc": zxAnRuSwUpdatingTaskDesc,
       "zxAnRuSwUpdatingTaskMode": zxAnRuSwUpdatingTaskMode,
       "zxAnRuSwUpdatingTaskServiceType": zxAnRuSwUpdatingTaskServiceType,
       "zxAnRuSwUpdatingTaskVendor": zxAnRuSwUpdatingTaskVendor,
       "zxAnRuSwUpdatingTaskEquipType": zxAnRuSwUpdatingTaskEquipType,
       "zxAnRuSwUpdatingTaskCrtrnType": zxAnRuSwUpdatingTaskCrtrnType,
       "zxAnRuSwUpdatingTaskCrtrnVer": zxAnRuSwUpdatingTaskCrtrnVer,
       "zxAnRuSwUpdatingTaskOperObjType": zxAnRuSwUpdatingTaskOperObjType,
       "zxAnRuSwUpdatingTaskOperObjList": zxAnRuSwUpdatingTaskOperObjList,
       "zxAnRuSwUpdatingTaskAction": zxAnRuSwUpdatingTaskAction,
       "zxAnRuSwUpdatingTaskFileName": zxAnRuSwUpdatingTaskFileName,
       "zxAnRuSwUpdatingTaskFileLocate": zxAnRuSwUpdatingTaskFileLocate,
       "zxAnRuSwUpdatingTaskStatus": zxAnRuSwUpdatingTaskStatus,
       "zxAnRuSwUpdatingTaskRuAction": zxAnRuSwUpdatingTaskRuAction,
       "zxAnRuSwUpdatingTaskParallelLmt": zxAnRuSwUpdatingTaskParallelLmt,
       "zxAnRuSwUpdatingTaskRowStatus": zxAnRuSwUpdatingTaskRowStatus,
       "zxAnRuSwTaskStatTable": zxAnRuSwTaskStatTable,
       "zxAnRuSwTaskStatEntry": zxAnRuSwTaskStatEntry,
       "zxAnRuSwTaskStatsSuccesses": zxAnRuSwTaskStatsSuccesses,
       "zxAnRuSwTaskStatsFailures": zxAnRuSwTaskStatsFailures,
       "zxAnRuSwTaskStatsUpdatings": zxAnRuSwTaskStatsUpdatings,
       "zxAnRuSwTaskStatsWaitings": zxAnRuSwTaskStatsWaitings,
       "zxAnRuSwUpdateStatusTable": zxAnRuSwUpdateStatusTable,
       "zxAnRuSwUpdateStatusEntry": zxAnRuSwUpdateStatusEntry,
       "zxAnRuSwRack": zxAnRuSwRack,
       "zxAnRuSwShelf": zxAnRuSwShelf,
       "zxAnRuSwSlot": zxAnRuSwSlot,
       "zxAnRuSwPort": zxAnRuSwPort,
       "zxAnRuSwOnu": zxAnRuSwOnu,
       "zxAnRuSwUpdateStatusServiceType": zxAnRuSwUpdateStatusServiceType,
       "zxAnRuSwUpdateStatusEquipType": zxAnRuSwUpdateStatusEquipType,
       "zxAnRuSwUpdateStatusFileName": zxAnRuSwUpdateStatusFileName,
       "zxAnRuSwUpdateStatusResult": zxAnRuSwUpdateStatusResult,
       "zxAnRuSwUpdateStatusFailReason": zxAnRuSwUpdateStatusFailReason,
       "zxAnRuSwUpdateStatusProgress": zxAnRuSwUpdateStatusProgress,
       "zxAnRuSwUpdateStatusSource": zxAnRuSwUpdateStatusSource,
       "zxAnRuSwUpdateStatusTaskName": zxAnRuSwUpdateStatusTaskName,
       "zxAnRuSwUpdateStatusModifyTime": zxAnRuSwUpdateStatusModifyTime,
       "zxAnRuSwUpdateStatusCurrVersion": zxAnRuSwUpdateStatusCurrVersion,
       "zxAnRuSwUpdateStatusLastVersion": zxAnRuSwUpdateStatusLastVersion,
       "zxAnRuSwImageTable": zxAnRuSwImageTable,
       "zxAnRuSwImageEntry": zxAnRuSwImageEntry,
       "zxAnRuSwImageRack": zxAnRuSwImageRack,
       "zxAnRuSwImageShelf": zxAnRuSwImageShelf,
       "zxAnRuSwImageSlot": zxAnRuSwImageSlot,
       "zxAnRuSwImagePort": zxAnRuSwImagePort,
       "zxAnRuSwImageOnu": zxAnRuSwImageOnu,
       "zxAnRuSwImageIndex": zxAnRuSwImageIndex,
       "zxAnRuSwImageVersion": zxAnRuSwImageVersion,
       "zxAnRuSwImageStatus": zxAnRuSwImageStatus,
       "zxAnRuSwNotifications": zxAnRuSwNotifications,
       "zxAnRuSwUpdatedTrap": zxAnRuSwUpdatedTrap}
)
