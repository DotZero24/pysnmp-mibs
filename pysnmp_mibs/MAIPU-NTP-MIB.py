# SNMP MIB module (MAIPU-NTP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/maipu/MAIPU-NTP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:11:12 2025
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
 ObjectName,
 ObjectSyntax,
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
    "ObjectName",
    "ObjectSyntax",
    "TimeTicks",
    "Unsigned32",
    "iso")

(DateAndTime,
 DisplayString,
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ntpMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5651, 3, 97)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class EnabledStatus(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )



# MIB Managed Objects in the order of their OIDs

_NtpAuthenticationCntl_Type = EnabledStatus
_NtpAuthenticationCntl_Object = MibScalar
ntpAuthenticationCntl = _NtpAuthenticationCntl_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 97, 1),
    _NtpAuthenticationCntl_Type()
)
ntpAuthenticationCntl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntpAuthenticationCntl.setStatus("current")
_NtpMasterCntl_Type = EnabledStatus
_NtpMasterCntl_Object = MibScalar
ntpMasterCntl = _NtpMasterCntl_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 97, 2),
    _NtpMasterCntl_Type()
)
ntpMasterCntl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntpMasterCntl.setStatus("current")


class _NtpMasterStratum_Type(Integer32):
    """Custom type ntpMasterStratum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 15),
    )


_NtpMasterStratum_Type.__name__ = "Integer32"
_NtpMasterStratum_Object = MibScalar
ntpMasterStratum = _NtpMasterStratum_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 97, 3),
    _NtpMasterStratum_Type()
)
ntpMasterStratum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntpMasterStratum.setStatus("current")


class _NtpSynStatus_Type(Integer32):
    """Custom type ntpSynStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("synchronized", 1),
          ("unsynchronized", 2))
    )


_NtpSynStatus_Type.__name__ = "Integer32"
_NtpSynStatus_Object = MibScalar
ntpSynStatus = _NtpSynStatus_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 97, 4),
    _NtpSynStatus_Type()
)
ntpSynStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntpSynStatus.setStatus("current")


class _NtpSynTime_Type(DisplayString):
    """Custom type ntpSynTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NtpSynTime_Type.__name__ = "DisplayString"
_NtpSynTime_Object = MibScalar
ntpSynTime = _NtpSynTime_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 97, 5),
    _NtpSynTime_Type()
)
ntpSynTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntpSynTime.setStatus("current")
_NtpAuthenticationKeyTable_Object = MibTable
ntpAuthenticationKeyTable = _NtpAuthenticationKeyTable_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 97, 20)
)
if mibBuilder.loadTexts:
    ntpAuthenticationKeyTable.setStatus("current")
_NtpAuthenticationKeyEntry_Object = MibTableRow
ntpAuthenticationKeyEntry = _NtpAuthenticationKeyEntry_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 97, 20, 1)
)
ntpAuthenticationKeyEntry.setIndexNames(
    (0, "MAIPU-NTP-MIB", "ntpAuthKeyNum"),
)
if mibBuilder.loadTexts:
    ntpAuthenticationKeyEntry.setStatus("current")
_NtpAuthKeyNum_Type = Unsigned32
_NtpAuthKeyNum_Object = MibTableColumn
ntpAuthKeyNum = _NtpAuthKeyNum_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 97, 20, 1, 1),
    _NtpAuthKeyNum_Type()
)
ntpAuthKeyNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ntpAuthKeyNum.setStatus("current")


class _NtpAuthStr_Type(DisplayString):
    """Custom type ntpAuthStr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_NtpAuthStr_Type.__name__ = "DisplayString"
_NtpAuthStr_Object = MibTableColumn
ntpAuthStr = _NtpAuthStr_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 97, 20, 1, 2),
    _NtpAuthStr_Type()
)
ntpAuthStr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntpAuthStr.setStatus("current")
_NtpAuthKeyRowStatus_Type = RowStatus
_NtpAuthKeyRowStatus_Object = MibTableColumn
ntpAuthKeyRowStatus = _NtpAuthKeyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 97, 20, 1, 3),
    _NtpAuthKeyRowStatus_Type()
)
ntpAuthKeyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntpAuthKeyRowStatus.setStatus("current")
_NtpTrustKeyTable_Object = MibTable
ntpTrustKeyTable = _NtpTrustKeyTable_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 97, 21)
)
if mibBuilder.loadTexts:
    ntpTrustKeyTable.setStatus("current")
_NtpTrustKeyEntry_Object = MibTableRow
ntpTrustKeyEntry = _NtpTrustKeyEntry_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 97, 21, 1)
)
ntpTrustKeyEntry.setIndexNames(
    (0, "MAIPU-NTP-MIB", "ntpTrustKeyNum"),
)
if mibBuilder.loadTexts:
    ntpTrustKeyEntry.setStatus("current")
_NtpTrustKeyNum_Type = Unsigned32
_NtpTrustKeyNum_Object = MibTableColumn
ntpTrustKeyNum = _NtpTrustKeyNum_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 97, 21, 1, 1),
    _NtpTrustKeyNum_Type()
)
ntpTrustKeyNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ntpTrustKeyNum.setStatus("current")
_NtpTrustkeyRowStatus_Type = RowStatus
_NtpTrustkeyRowStatus_Object = MibTableColumn
ntpTrustkeyRowStatus = _NtpTrustkeyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 97, 21, 1, 2),
    _NtpTrustkeyRowStatus_Type()
)
ntpTrustkeyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntpTrustkeyRowStatus.setStatus("current")
_NtpServerTable_Object = MibTable
ntpServerTable = _NtpServerTable_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 97, 22)
)
if mibBuilder.loadTexts:
    ntpServerTable.setStatus("current")
_NtpServerEntry_Object = MibTableRow
ntpServerEntry = _NtpServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 97, 22, 1)
)
ntpServerEntry.setIndexNames(
    (0, "MAIPU-NTP-MIB", "ntpServerAddr"),
    (0, "MAIPU-NTP-MIB", "ntpServerVRF"),
)
if mibBuilder.loadTexts:
    ntpServerEntry.setStatus("current")
_NtpServerAddr_Type = IpAddress
_NtpServerAddr_Object = MibTableColumn
ntpServerAddr = _NtpServerAddr_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 97, 22, 1, 1),
    _NtpServerAddr_Type()
)
ntpServerAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ntpServerAddr.setStatus("current")


class _NtpServerVRF_Type(DisplayString):
    """Custom type ntpServerVRF based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_NtpServerVRF_Type.__name__ = "DisplayString"
_NtpServerVRF_Object = MibTableColumn
ntpServerVRF = _NtpServerVRF_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 97, 22, 1, 2),
    _NtpServerVRF_Type()
)
ntpServerVRF.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ntpServerVRF.setStatus("current")
_NtpServerKeyNum_Type = Unsigned32
_NtpServerKeyNum_Object = MibTableColumn
ntpServerKeyNum = _NtpServerKeyNum_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 97, 22, 1, 3),
    _NtpServerKeyNum_Type()
)
ntpServerKeyNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntpServerKeyNum.setStatus("current")


class _NtpServerVersion_Type(Integer32):
    """Custom type ntpServerVersion based on Integer32"""
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
        *(("ver1", 1),
          ("ver2", 2),
          ("ver3", 3),
          ("ver4", 4))
    )


_NtpServerVersion_Type.__name__ = "Integer32"
_NtpServerVersion_Object = MibTableColumn
ntpServerVersion = _NtpServerVersion_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 97, 22, 1, 4),
    _NtpServerVersion_Type()
)
ntpServerVersion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntpServerVersion.setStatus("current")
_NtpServerRowStatus_Type = RowStatus
_NtpServerRowStatus_Object = MibTableColumn
ntpServerRowStatus = _NtpServerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 97, 22, 1, 5),
    _NtpServerRowStatus_Type()
)
ntpServerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntpServerRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MAIPU-NTP-MIB",
    **{"EnabledStatus": EnabledStatus,
       "ntpMib": ntpMib,
       "ntpAuthenticationCntl": ntpAuthenticationCntl,
       "ntpMasterCntl": ntpMasterCntl,
       "ntpMasterStratum": ntpMasterStratum,
       "ntpSynStatus": ntpSynStatus,
       "ntpSynTime": ntpSynTime,
       "ntpAuthenticationKeyTable": ntpAuthenticationKeyTable,
       "ntpAuthenticationKeyEntry": ntpAuthenticationKeyEntry,
       "ntpAuthKeyNum": ntpAuthKeyNum,
       "ntpAuthStr": ntpAuthStr,
       "ntpAuthKeyRowStatus": ntpAuthKeyRowStatus,
       "ntpTrustKeyTable": ntpTrustKeyTable,
       "ntpTrustKeyEntry": ntpTrustKeyEntry,
       "ntpTrustKeyNum": ntpTrustKeyNum,
       "ntpTrustkeyRowStatus": ntpTrustkeyRowStatus,
       "ntpServerTable": ntpServerTable,
       "ntpServerEntry": ntpServerEntry,
       "ntpServerAddr": ntpServerAddr,
       "ntpServerVRF": ntpServerVRF,
       "ntpServerKeyNum": ntpServerKeyNum,
       "ntpServerVersion": ntpServerVersion,
       "ntpServerRowStatus": ntpServerRowStatus}
)
