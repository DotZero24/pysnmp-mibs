# SNMP MIB module (DLINKPRIME-SYSTEM-FILE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/d-link/DLINKPRIME-SYSTEM-FILE-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:47:00 2025
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

(dlinkPrimeCommon,) = mibBuilder.importSymbols(
    "DLINK-ID-REC-MIB",
    "dlinkPrimeCommon")

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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

dlinkPrimeSystemFileMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 171, 15, 22)
)
if mibBuilder.loadTexts:
    dlinkPrimeSystemFileMIB.setRevisions(
        ("2014-05-26 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_DpsfMIBNotifications_ObjectIdentity = ObjectIdentity
dpsfMIBNotifications = _DpsfMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 15, 22, 0)
)
_DpsfMIBObjects_ObjectIdentity = ObjectIdentity
dpsfMIBObjects = _DpsfMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 15, 22, 1)
)
_DpsfBootInfoObjects_ObjectIdentity = ObjectIdentity
dpsfBootInfoObjects = _DpsfBootInfoObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 15, 22, 1, 1)
)
_DpsfCheckingBootImageCheck_Type = TruthValue
_DpsfCheckingBootImageCheck_Object = MibScalar
dpsfCheckingBootImageCheck = _DpsfCheckingBootImageCheck_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 22, 1, 1, 1),
    _DpsfCheckingBootImageCheck_Type()
)
dpsfCheckingBootImageCheck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpsfCheckingBootImageCheck.setStatus("current")
_DpsfBootImageCheckResult_Type = DisplayString
_DpsfBootImageCheckResult_Object = MibScalar
dpsfBootImageCheckResult = _DpsfBootImageCheckResult_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 22, 1, 1, 2),
    _DpsfBootImageCheckResult_Type()
)
dpsfBootImageCheckResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpsfBootImageCheckResult.setStatus("current")
_DpsfBootImageTable_Object = MibTable
dpsfBootImageTable = _DpsfBootImageTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 22, 1, 1, 3)
)
if mibBuilder.loadTexts:
    dpsfBootImageTable.setStatus("current")
_DpsfBootImageEntry_Object = MibTableRow
dpsfBootImageEntry = _DpsfBootImageEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 22, 1, 1, 3, 1)
)
dpsfBootImageEntry.setIndexNames(
    (0, "DLINKPRIME-SYSTEM-FILE-MIB", "dpsfBootImageIndex"),
)
if mibBuilder.loadTexts:
    dpsfBootImageEntry.setStatus("current")


class _DpsfBootImageIndex_Type(Unsigned32):
    """Custom type dpsfBootImageIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_DpsfBootImageIndex_Type.__name__ = "Unsigned32"
_DpsfBootImageIndex_Object = MibTableColumn
dpsfBootImageIndex = _DpsfBootImageIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 22, 1, 1, 3, 1, 1),
    _DpsfBootImageIndex_Type()
)
dpsfBootImageIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dpsfBootImageIndex.setStatus("current")
_DpsfBootImageInWorking_Type = TruthValue
_DpsfBootImageInWorking_Object = MibTableColumn
dpsfBootImageInWorking = _DpsfBootImageInWorking_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 22, 1, 1, 3, 1, 2),
    _DpsfBootImageInWorking_Type()
)
dpsfBootImageInWorking.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpsfBootImageInWorking.setStatus("current")
_DpsfCopyTable_Object = MibTable
dpsfCopyTable = _DpsfCopyTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 22, 1, 2)
)
if mibBuilder.loadTexts:
    dpsfCopyTable.setStatus("current")
_DpsfCopyEntry_Object = MibTableRow
dpsfCopyEntry = _DpsfCopyEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 22, 1, 2, 1)
)
dpsfCopyEntry.setIndexNames(
    (0, "DLINKPRIME-SYSTEM-FILE-MIB", "dpsfCopyIndex"),
)
if mibBuilder.loadTexts:
    dpsfCopyEntry.setStatus("current")


class _DpsfCopyIndex_Type(Unsigned32):
    """Custom type dpsfCopyIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_DpsfCopyIndex_Type.__name__ = "Unsigned32"
_DpsfCopyIndex_Object = MibTableColumn
dpsfCopyIndex = _DpsfCopyIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 22, 1, 2, 1, 1),
    _DpsfCopyIndex_Type()
)
dpsfCopyIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dpsfCopyIndex.setStatus("current")


class _DpsfCopyType_Type(Integer32):
    """Custom type dpsfCopyType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("localToTftpRemote", 1),
          ("tftpRemoteToLocal", 2))
    )


_DpsfCopyType_Type.__name__ = "Integer32"
_DpsfCopyType_Object = MibTableColumn
dpsfCopyType = _DpsfCopyType_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 22, 1, 2, 1, 2),
    _DpsfCopyType_Type()
)
dpsfCopyType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dpsfCopyType.setStatus("current")


class _DpsfCopySrcUrl_Type(OctetString):
    """Custom type dpsfCopySrcUrl based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 799),
    )


_DpsfCopySrcUrl_Type.__name__ = "OctetString"
_DpsfCopySrcUrl_Object = MibTableColumn
dpsfCopySrcUrl = _DpsfCopySrcUrl_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 22, 1, 2, 1, 3),
    _DpsfCopySrcUrl_Type()
)
dpsfCopySrcUrl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dpsfCopySrcUrl.setStatus("current")


class _DpsfCopyDstUrl_Type(OctetString):
    """Custom type dpsfCopyDstUrl based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 799),
    )


_DpsfCopyDstUrl_Type.__name__ = "OctetString"
_DpsfCopyDstUrl_Object = MibTableColumn
dpsfCopyDstUrl = _DpsfCopyDstUrl_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 22, 1, 2, 1, 4),
    _DpsfCopyDstUrl_Type()
)
dpsfCopyDstUrl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dpsfCopyDstUrl.setStatus("current")
_DpsfCopyRemoteAddr_Type = IpAddress
_DpsfCopyRemoteAddr_Object = MibTableColumn
dpsfCopyRemoteAddr = _DpsfCopyRemoteAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 22, 1, 2, 1, 5),
    _DpsfCopyRemoteAddr_Type()
)
dpsfCopyRemoteAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dpsfCopyRemoteAddr.setStatus("current")
_DpsfCopyErrorStatus_Type = DisplayString
_DpsfCopyErrorStatus_Object = MibTableColumn
dpsfCopyErrorStatus = _DpsfCopyErrorStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 22, 1, 2, 1, 6),
    _DpsfCopyErrorStatus_Type()
)
dpsfCopyErrorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpsfCopyErrorStatus.setStatus("current")
_DpsfCopyRowStatus_Type = RowStatus
_DpsfCopyRowStatus_Object = MibTableColumn
dpsfCopyRowStatus = _DpsfCopyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 22, 1, 2, 1, 7),
    _DpsfCopyRowStatus_Type()
)
dpsfCopyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dpsfCopyRowStatus.setStatus("current")
_DpsfCfgReplaceTable_Object = MibTable
dpsfCfgReplaceTable = _DpsfCfgReplaceTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 22, 1, 3)
)
if mibBuilder.loadTexts:
    dpsfCfgReplaceTable.setStatus("current")
_DpsfCfgReplaceEntry_Object = MibTableRow
dpsfCfgReplaceEntry = _DpsfCfgReplaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 22, 1, 3, 1)
)
dpsfCfgReplaceEntry.setIndexNames(
    (0, "DLINKPRIME-SYSTEM-FILE-MIB", "dpsfCfgReplaceIndex"),
)
if mibBuilder.loadTexts:
    dpsfCfgReplaceEntry.setStatus("current")


class _DpsfCfgReplaceIndex_Type(Unsigned32):
    """Custom type dpsfCfgReplaceIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_DpsfCfgReplaceIndex_Type.__name__ = "Unsigned32"
_DpsfCfgReplaceIndex_Object = MibTableColumn
dpsfCfgReplaceIndex = _DpsfCfgReplaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 22, 1, 3, 1, 1),
    _DpsfCfgReplaceIndex_Type()
)
dpsfCfgReplaceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dpsfCfgReplaceIndex.setStatus("current")


class _DpsfCfgReplaceSrcType_Type(Integer32):
    """Custom type dpsfCfgReplaceSrcType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("tftpRemote", 1)
    )


_DpsfCfgReplaceSrcType_Type.__name__ = "Integer32"
_DpsfCfgReplaceSrcType_Object = MibTableColumn
dpsfCfgReplaceSrcType = _DpsfCfgReplaceSrcType_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 22, 1, 3, 1, 2),
    _DpsfCfgReplaceSrcType_Type()
)
dpsfCfgReplaceSrcType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpsfCfgReplaceSrcType.setStatus("current")


class _DpsfCfgReplaceSrcUrl_Type(OctetString):
    """Custom type dpsfCfgReplaceSrcUrl based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 799),
    )


_DpsfCfgReplaceSrcUrl_Type.__name__ = "OctetString"
_DpsfCfgReplaceSrcUrl_Object = MibTableColumn
dpsfCfgReplaceSrcUrl = _DpsfCfgReplaceSrcUrl_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 22, 1, 3, 1, 3),
    _DpsfCfgReplaceSrcUrl_Type()
)
dpsfCfgReplaceSrcUrl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dpsfCfgReplaceSrcUrl.setStatus("current")
_DpsfCfgReplaceRemoteAddr_Type = IpAddress
_DpsfCfgReplaceRemoteAddr_Object = MibTableColumn
dpsfCfgReplaceRemoteAddr = _DpsfCfgReplaceRemoteAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 22, 1, 3, 1, 4),
    _DpsfCfgReplaceRemoteAddr_Type()
)
dpsfCfgReplaceRemoteAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dpsfCfgReplaceRemoteAddr.setStatus("current")
_DpsfCfgReplaceErrorStatus_Type = DisplayString
_DpsfCfgReplaceErrorStatus_Object = MibTableColumn
dpsfCfgReplaceErrorStatus = _DpsfCfgReplaceErrorStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 22, 1, 3, 1, 5),
    _DpsfCfgReplaceErrorStatus_Type()
)
dpsfCfgReplaceErrorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpsfCfgReplaceErrorStatus.setStatus("current")
_DpsfCfgReplaceRowStatus_Type = RowStatus
_DpsfCfgReplaceRowStatus_Object = MibTableColumn
dpsfCfgReplaceRowStatus = _DpsfCfgReplaceRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 22, 1, 3, 1, 6),
    _DpsfCfgReplaceRowStatus_Type()
)
dpsfCfgReplaceRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dpsfCfgReplaceRowStatus.setStatus("current")


class _DpsfClearRunCfg_Type(Integer32):
    """Custom type dpsfClearRunCfg based on Integer32"""
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
        *(("clear_cfg_ip_reboot", 1),
          ("clear_cfg_no_ip_reboot", 2),
          ("clear_cfg_no_reboot", 3),
          ("noOp", 4))
    )


_DpsfClearRunCfg_Type.__name__ = "Integer32"
_DpsfClearRunCfg_Object = MibScalar
dpsfClearRunCfg = _DpsfClearRunCfg_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 22, 1, 4),
    _DpsfClearRunCfg_Type()
)
dpsfClearRunCfg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpsfClearRunCfg.setStatus("current")


class _DpsfResetSystem_Type(Integer32):
    """Custom type dpsfResetSystem based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("reset", 1),
          ("noOp", 2))
    )


_DpsfResetSystem_Type.__name__ = "Integer32"
_DpsfResetSystem_Object = MibScalar
dpsfResetSystem = _DpsfResetSystem_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 22, 1, 5),
    _DpsfResetSystem_Type()
)
dpsfResetSystem.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpsfResetSystem.setStatus("current")
_DpsfMIBConformance_ObjectIdentity = ObjectIdentity
dpsfMIBConformance = _DpsfMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 15, 22, 2)
)
_DpsfCompliances_ObjectIdentity = ObjectIdentity
dpsfCompliances = _DpsfCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 15, 22, 2, 1)
)
_DpsfGroups_ObjectIdentity = ObjectIdentity
dpsfGroups = _DpsfGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 15, 22, 2, 2)
)

# Managed Objects groups

dpsfBootInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 15, 22, 2, 2, 1)
)
dpsfBootInfoGroup.setObjects(
      *(("DLINKPRIME-SYSTEM-FILE-MIB", "dpsfCheckingBootImageCheck"),
        ("DLINKPRIME-SYSTEM-FILE-MIB", "dpsfBootImageCheckResult"),
        ("DLINKPRIME-SYSTEM-FILE-MIB", "dpsfBootImageInWorking"))
)
if mibBuilder.loadTexts:
    dpsfBootInfoGroup.setStatus("current")

dpsfCopyGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 15, 22, 2, 2, 2)
)
dpsfCopyGroup.setObjects(
      *(("DLINKPRIME-SYSTEM-FILE-MIB", "dpsfCopyType"),
        ("DLINKPRIME-SYSTEM-FILE-MIB", "dpsfCopySrcUrl"),
        ("DLINKPRIME-SYSTEM-FILE-MIB", "dpsfCopyDstUrl"),
        ("DLINKPRIME-SYSTEM-FILE-MIB", "dpsfCopyRemoteAddr"),
        ("DLINKPRIME-SYSTEM-FILE-MIB", "dpsfCopyErrorStatus"),
        ("DLINKPRIME-SYSTEM-FILE-MIB", "dpsfCopyRowStatus"))
)
if mibBuilder.loadTexts:
    dpsfCopyGroup.setStatus("current")

dpsfCfgReplaceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 15, 22, 2, 2, 3)
)
dpsfCfgReplaceGroup.setObjects(
      *(("DLINKPRIME-SYSTEM-FILE-MIB", "dpsfCfgReplaceSrcType"),
        ("DLINKPRIME-SYSTEM-FILE-MIB", "dpsfCfgReplaceSrcUrl"),
        ("DLINKPRIME-SYSTEM-FILE-MIB", "dpsfCfgReplaceRemoteAddr"),
        ("DLINKPRIME-SYSTEM-FILE-MIB", "dpsfCfgReplaceErrorStatus"),
        ("DLINKPRIME-SYSTEM-FILE-MIB", "dpsfCfgReplaceRowStatus"))
)
if mibBuilder.loadTexts:
    dpsfCfgReplaceGroup.setStatus("current")

dpsfClearCfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 15, 22, 2, 2, 4)
)
dpsfClearCfgGroup.setObjects(
      *(("DLINKPRIME-SYSTEM-FILE-MIB", "dpsfClearRunCfg"),
        ("DLINKPRIME-SYSTEM-FILE-MIB", "dpsfResetSystem"))
)
if mibBuilder.loadTexts:
    dpsfClearCfgGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

dpsfCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 171, 15, 22, 2, 1, 1)
)
dpsfCompliance.setObjects(
      *(("DLINKPRIME-SYSTEM-FILE-MIB", "dpsfBootInfoGroup"),
        ("DLINKPRIME-SYSTEM-FILE-MIB", "dpsfCopyGroup"),
        ("DLINKPRIME-SYSTEM-FILE-MIB", "dpsfCfgReplaceGroup"),
        ("DLINKPRIME-SYSTEM-FILE-MIB", "dpsfClearCfgGroup"))
)
if mibBuilder.loadTexts:
    dpsfCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DLINKPRIME-SYSTEM-FILE-MIB",
    **{"dlinkPrimeSystemFileMIB": dlinkPrimeSystemFileMIB,
       "dpsfMIBNotifications": dpsfMIBNotifications,
       "dpsfMIBObjects": dpsfMIBObjects,
       "dpsfBootInfoObjects": dpsfBootInfoObjects,
       "dpsfCheckingBootImageCheck": dpsfCheckingBootImageCheck,
       "dpsfBootImageCheckResult": dpsfBootImageCheckResult,
       "dpsfBootImageTable": dpsfBootImageTable,
       "dpsfBootImageEntry": dpsfBootImageEntry,
       "dpsfBootImageIndex": dpsfBootImageIndex,
       "dpsfBootImageInWorking": dpsfBootImageInWorking,
       "dpsfCopyTable": dpsfCopyTable,
       "dpsfCopyEntry": dpsfCopyEntry,
       "dpsfCopyIndex": dpsfCopyIndex,
       "dpsfCopyType": dpsfCopyType,
       "dpsfCopySrcUrl": dpsfCopySrcUrl,
       "dpsfCopyDstUrl": dpsfCopyDstUrl,
       "dpsfCopyRemoteAddr": dpsfCopyRemoteAddr,
       "dpsfCopyErrorStatus": dpsfCopyErrorStatus,
       "dpsfCopyRowStatus": dpsfCopyRowStatus,
       "dpsfCfgReplaceTable": dpsfCfgReplaceTable,
       "dpsfCfgReplaceEntry": dpsfCfgReplaceEntry,
       "dpsfCfgReplaceIndex": dpsfCfgReplaceIndex,
       "dpsfCfgReplaceSrcType": dpsfCfgReplaceSrcType,
       "dpsfCfgReplaceSrcUrl": dpsfCfgReplaceSrcUrl,
       "dpsfCfgReplaceRemoteAddr": dpsfCfgReplaceRemoteAddr,
       "dpsfCfgReplaceErrorStatus": dpsfCfgReplaceErrorStatus,
       "dpsfCfgReplaceRowStatus": dpsfCfgReplaceRowStatus,
       "dpsfClearRunCfg": dpsfClearRunCfg,
       "dpsfResetSystem": dpsfResetSystem,
       "dpsfMIBConformance": dpsfMIBConformance,
       "dpsfCompliances": dpsfCompliances,
       "dpsfCompliance": dpsfCompliance,
       "dpsfGroups": dpsfGroups,
       "dpsfBootInfoGroup": dpsfBootInfoGroup,
       "dpsfCopyGroup": dpsfCopyGroup,
       "dpsfCfgReplaceGroup": dpsfCfgReplaceGroup,
       "dpsfClearCfgGroup": dpsfClearCfgGroup}
)
