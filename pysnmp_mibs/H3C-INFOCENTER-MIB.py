# SNMP MIB module (H3C-INFOCENTER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/h3c/H3C-INFOCENTER-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:19:50 2025
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

(h3cCommon,) = mibBuilder.importSymbols(
    "HUAWEI-3COM-OID-MIB",
    "h3cCommon")

(InterfaceIndexOrZero,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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
 TAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

h3cInfoCenter = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 119)
)
if mibBuilder.loadTexts:
    h3cInfoCenter.setRevisions(
        ("2014-09-05 03:25",
         "2012-11-03 19:00",
         "2012-03-07 19:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class ICMessageLevelType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("emergency", 0),
          ("alert", 1),
          ("critical", 2),
          ("error", 3),
          ("warning", 4),
          ("notice", 5),
          ("informational", 6),
          ("debug", 7),
          ("invalid", 8))
    )



class ICFacilityType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23)
        )
    )
    namedValues = NamedValues(
        *(("kernel", 0),
          ("userLevel", 1),
          ("mailSystem", 2),
          ("systemDaemons", 3),
          ("securityAuthorization", 4),
          ("internallyMessages", 5),
          ("linePrinter", 6),
          ("networkNews", 7),
          ("uucp", 8),
          ("clockDaemon", 9),
          ("securityAuthorization2", 10),
          ("ftpDaemon", 11),
          ("ntp", 12),
          ("logAudit", 13),
          ("logAlert", 14),
          ("clockDaemon2", 15),
          ("local0", 16),
          ("local1", 17),
          ("local2", 18),
          ("local3", 19),
          ("local4", 20),
          ("local5", 21),
          ("local6", 22),
          ("local7", 23))
    )



class ICTimeStampType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("date", 0),
          ("boot", 1),
          ("iso", 2),
          ("dateWithoutYear", 3),
          ("none", 4),
          ("isoWithTimezone", 5))
    )



# MIB Managed Objects in the order of their OIDs

_H3cICLogbuffer_ObjectIdentity = ObjectIdentity
h3cICLogbuffer = _H3cICLogbuffer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 119, 1)
)
_H3cICLogbufferObjects_ObjectIdentity = ObjectIdentity
h3cICLogbufferObjects = _H3cICLogbufferObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 119, 1, 1)
)
_H3cICMaxLogbufferSize_Type = Unsigned32
_H3cICMaxLogbufferSize_Object = MibScalar
h3cICMaxLogbufferSize = _H3cICMaxLogbufferSize_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 119, 1, 1, 1),
    _H3cICMaxLogbufferSize_Type()
)
h3cICMaxLogbufferSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cICMaxLogbufferSize.setStatus("current")


class _H3cICLogbufferSize_Type(Unsigned32):
    """Custom type h3cICLogbufferSize based on Unsigned32"""
    defaultValue = 512


_H3cICLogbufferSize_Type.__name__ = "Unsigned32"
_H3cICLogbufferSize_Object = MibScalar
h3cICLogbufferSize = _H3cICLogbufferSize_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 119, 1, 1, 2),
    _H3cICLogbufferSize_Type()
)
h3cICLogbufferSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cICLogbufferSize.setStatus("current")
_H3cICLogbufferCurrentMessages_Type = Unsigned32
_H3cICLogbufferCurrentMessages_Object = MibScalar
h3cICLogbufferCurrentMessages = _H3cICLogbufferCurrentMessages_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 119, 1, 1, 3),
    _H3cICLogbufferCurrentMessages_Type()
)
h3cICLogbufferCurrentMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cICLogbufferCurrentMessages.setStatus("current")
_H3cICLogbufferOverwrittenMessages_Type = Counter32
_H3cICLogbufferOverwrittenMessages_Object = MibScalar
h3cICLogbufferOverwrittenMessages = _H3cICLogbufferOverwrittenMessages_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 119, 1, 1, 4),
    _H3cICLogbufferOverwrittenMessages_Type()
)
h3cICLogbufferOverwrittenMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cICLogbufferOverwrittenMessages.setStatus("current")
_H3cICLogbufferDroppedMessages_Type = Counter32
_H3cICLogbufferDroppedMessages_Object = MibScalar
h3cICLogbufferDroppedMessages = _H3cICLogbufferDroppedMessages_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 119, 1, 1, 5),
    _H3cICLogbufferDroppedMessages_Type()
)
h3cICLogbufferDroppedMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cICLogbufferDroppedMessages.setStatus("current")
_H3cICLogbufferContTable_Object = MibTable
h3cICLogbufferContTable = _H3cICLogbufferContTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 119, 1, 2)
)
if mibBuilder.loadTexts:
    h3cICLogbufferContTable.setStatus("current")
_H3cICLogbufferContEntry_Object = MibTableRow
h3cICLogbufferContEntry = _H3cICLogbufferContEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 119, 1, 2, 1)
)
h3cICLogbufferContEntry.setIndexNames(
    (0, "H3C-INFOCENTER-MIB", "h3cICLogbufferContIndex"),
)
if mibBuilder.loadTexts:
    h3cICLogbufferContEntry.setStatus("current")


class _H3cICLogbufferContIndex_Type(Integer32):
    """Custom type h3cICLogbufferContIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_H3cICLogbufferContIndex_Type.__name__ = "Integer32"
_H3cICLogbufferContIndex_Object = MibTableColumn
h3cICLogbufferContIndex = _H3cICLogbufferContIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 119, 1, 2, 1, 1),
    _H3cICLogbufferContIndex_Type()
)
h3cICLogbufferContIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cICLogbufferContIndex.setStatus("current")


class _H3cICLogbufferContDescription_Type(DisplayString):
    """Custom type h3cICLogbufferContDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1600),
    )


_H3cICLogbufferContDescription_Type.__name__ = "DisplayString"
_H3cICLogbufferContDescription_Object = MibTableColumn
h3cICLogbufferContDescription = _H3cICLogbufferContDescription_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 119, 1, 2, 1, 2),
    _H3cICLogbufferContDescription_Type()
)
h3cICLogbufferContDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cICLogbufferContDescription.setStatus("current")
_H3cICLoghost_ObjectIdentity = ObjectIdentity
h3cICLoghost = _H3cICLoghost_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 119, 2)
)
_H3cICLoghostObjects_ObjectIdentity = ObjectIdentity
h3cICLoghostObjects = _H3cICLoghostObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 119, 2, 1)
)
_H3cICMaxLoghost_Type = Unsigned32
_H3cICMaxLoghost_Object = MibScalar
h3cICMaxLoghost = _H3cICMaxLoghost_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 119, 2, 1, 1),
    _H3cICMaxLoghost_Type()
)
h3cICMaxLoghost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cICMaxLoghost.setStatus("current")
_H3cICLoghostSourceInterface_Type = InterfaceIndexOrZero
_H3cICLoghostSourceInterface_Object = MibScalar
h3cICLoghostSourceInterface = _H3cICLoghostSourceInterface_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 119, 2, 1, 2),
    _H3cICLoghostSourceInterface_Type()
)
h3cICLoghostSourceInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cICLoghostSourceInterface.setStatus("current")


class _H3cICLoghostTimestampType_Type(ICTimeStampType):
    """Custom type h3cICLoghostTimestampType based on ICTimeStampType"""
    defaultValue = 0


_H3cICLoghostTimestampType_Type.__name__ = "ICTimeStampType"
_H3cICLoghostTimestampType_Object = MibScalar
h3cICLoghostTimestampType = _H3cICLoghostTimestampType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 119, 2, 1, 3),
    _H3cICLoghostTimestampType_Type()
)
h3cICLoghostTimestampType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cICLoghostTimestampType.setStatus("current")
_H3cICLoghostTable_Object = MibTable
h3cICLoghostTable = _H3cICLoghostTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 119, 2, 2)
)
if mibBuilder.loadTexts:
    h3cICLoghostTable.setStatus("current")
_H3cICLoghostEntry_Object = MibTableRow
h3cICLoghostEntry = _H3cICLoghostEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 119, 2, 2, 1)
)
h3cICLoghostEntry.setIndexNames(
    (0, "H3C-INFOCENTER-MIB", "h3cICLoghostIndex"),
)
if mibBuilder.loadTexts:
    h3cICLoghostEntry.setStatus("current")


class _H3cICLoghostIndex_Type(Unsigned32):
    """Custom type h3cICLoghostIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_H3cICLoghostIndex_Type.__name__ = "Unsigned32"
_H3cICLoghostIndex_Object = MibTableColumn
h3cICLoghostIndex = _H3cICLoghostIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 119, 2, 2, 1, 1),
    _H3cICLoghostIndex_Type()
)
h3cICLoghostIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cICLoghostIndex.setStatus("current")


class _H3cICLoghostIpaddressType_Type(InetAddressType):
    """Custom type h3cICLoghostIpaddressType based on InetAddressType"""
    defaultValue = 1


_H3cICLoghostIpaddressType_Type.__name__ = "InetAddressType"
_H3cICLoghostIpaddressType_Object = MibTableColumn
h3cICLoghostIpaddressType = _H3cICLoghostIpaddressType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 119, 2, 2, 1, 2),
    _H3cICLoghostIpaddressType_Type()
)
h3cICLoghostIpaddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cICLoghostIpaddressType.setStatus("current")
_H3cICLoghostIpaddress_Type = InetAddress
_H3cICLoghostIpaddress_Object = MibTableColumn
h3cICLoghostIpaddress = _H3cICLoghostIpaddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 119, 2, 2, 1, 3),
    _H3cICLoghostIpaddress_Type()
)
h3cICLoghostIpaddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cICLoghostIpaddress.setStatus("current")


class _H3cICLoghostVPNName_Type(DisplayString):
    """Custom type h3cICLoghostVPNName based on DisplayString"""
    defaultValue = OctetString("")


_H3cICLoghostVPNName_Type.__name__ = "DisplayString"
_H3cICLoghostVPNName_Object = MibTableColumn
h3cICLoghostVPNName = _H3cICLoghostVPNName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 119, 2, 2, 1, 4),
    _H3cICLoghostVPNName_Type()
)
h3cICLoghostVPNName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cICLoghostVPNName.setStatus("current")


class _H3cICLoghostFacility_Type(ICFacilityType):
    """Custom type h3cICLoghostFacility based on ICFacilityType"""
    defaultValue = 23


_H3cICLoghostFacility_Type.__name__ = "ICFacilityType"
_H3cICLoghostFacility_Object = MibTableColumn
h3cICLoghostFacility = _H3cICLoghostFacility_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 119, 2, 2, 1, 5),
    _H3cICLoghostFacility_Type()
)
h3cICLoghostFacility.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cICLoghostFacility.setStatus("current")
_H3cICLoghostOperateRowStatus_Type = RowStatus
_H3cICLoghostOperateRowStatus_Object = MibTableColumn
h3cICLoghostOperateRowStatus = _H3cICLoghostOperateRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 119, 2, 2, 1, 6),
    _H3cICLoghostOperateRowStatus_Type()
)
h3cICLoghostOperateRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cICLoghostOperateRowStatus.setStatus("current")


class _H3cICLoghostIpaddressPort_Type(Unsigned32):
    """Custom type h3cICLoghostIpaddressPort based on Unsigned32"""
    defaultValue = 514

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_H3cICLoghostIpaddressPort_Type.__name__ = "Unsigned32"
_H3cICLoghostIpaddressPort_Object = MibTableColumn
h3cICLoghostIpaddressPort = _H3cICLoghostIpaddressPort_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 119, 2, 2, 1, 7),
    _H3cICLoghostIpaddressPort_Type()
)
h3cICLoghostIpaddressPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cICLoghostIpaddressPort.setStatus("current")
_H3cICLoghostTAddress_Type = TAddress
_H3cICLoghostTAddress_Object = MibTableColumn
h3cICLoghostTAddress = _H3cICLoghostTAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 119, 2, 2, 1, 8),
    _H3cICLoghostTAddress_Type()
)
h3cICLoghostTAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cICLoghostTAddress.setStatus("current")
_H3cICDirection_ObjectIdentity = ObjectIdentity
h3cICDirection = _H3cICDirection_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 119, 3)
)
_H3cICDirectionTable_Object = MibTable
h3cICDirectionTable = _H3cICDirectionTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 119, 3, 1)
)
if mibBuilder.loadTexts:
    h3cICDirectionTable.setStatus("current")
_H3cICDirectionEntry_Object = MibTableRow
h3cICDirectionEntry = _H3cICDirectionEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 119, 3, 1, 1)
)
h3cICDirectionEntry.setIndexNames(
    (0, "H3C-INFOCENTER-MIB", "h3cICDirectionIndex"),
)
if mibBuilder.loadTexts:
    h3cICDirectionEntry.setStatus("current")
_H3cICDirectionIndex_Type = Unsigned32
_H3cICDirectionIndex_Object = MibTableColumn
h3cICDirectionIndex = _H3cICDirectionIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 119, 3, 1, 1, 1),
    _H3cICDirectionIndex_Type()
)
h3cICDirectionIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cICDirectionIndex.setStatus("current")


class _H3cICDirectionName_Type(DisplayString):
    """Custom type h3cICDirectionName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 30),
    )


_H3cICDirectionName_Type.__name__ = "DisplayString"
_H3cICDirectionName_Object = MibTableColumn
h3cICDirectionName = _H3cICDirectionName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 119, 3, 1, 1, 2),
    _H3cICDirectionName_Type()
)
h3cICDirectionName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cICDirectionName.setStatus("current")
_H3cICDirectionState_Type = TruthValue
_H3cICDirectionState_Object = MibTableColumn
h3cICDirectionState = _H3cICDirectionState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 119, 3, 1, 1, 3),
    _H3cICDirectionState_Type()
)
h3cICDirectionState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cICDirectionState.setStatus("current")
_H3cICModule_ObjectIdentity = ObjectIdentity
h3cICModule = _H3cICModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 119, 4)
)
_H3cICModuleTable_Object = MibTable
h3cICModuleTable = _H3cICModuleTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 119, 4, 1)
)
if mibBuilder.loadTexts:
    h3cICModuleTable.setStatus("current")
_H3cICModuleEntry_Object = MibTableRow
h3cICModuleEntry = _H3cICModuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 119, 4, 1, 1)
)
h3cICModuleEntry.setIndexNames(
    (1, "H3C-INFOCENTER-MIB", "h3cICModuleName"),
)
if mibBuilder.loadTexts:
    h3cICModuleEntry.setStatus("current")


class _H3cICModuleName_Type(DisplayString):
    """Custom type h3cICModuleName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_H3cICModuleName_Type.__name__ = "DisplayString"
_H3cICModuleName_Object = MibTableColumn
h3cICModuleName = _H3cICModuleName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 119, 4, 1, 1, 1),
    _H3cICModuleName_Type()
)
h3cICModuleName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cICModuleName.setStatus("current")
_H3cICLog_ObjectIdentity = ObjectIdentity
h3cICLog = _H3cICLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 119, 5)
)
_H3cICLogObjects_ObjectIdentity = ObjectIdentity
h3cICLogObjects = _H3cICLogObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 119, 5, 1)
)


class _H3cICLogGlobalState_Type(TruthValue):
    """Custom type h3cICLogGlobalState based on TruthValue"""
    defaultValue = 1


_H3cICLogGlobalState_Type.__name__ = "TruthValue"
_H3cICLogGlobalState_Object = MibScalar
h3cICLogGlobalState = _H3cICLogGlobalState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 119, 5, 1, 1),
    _H3cICLogGlobalState_Type()
)
h3cICLogGlobalState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cICLogGlobalState.setStatus("current")


class _H3cICLogTimestampType_Type(ICTimeStampType):
    """Custom type h3cICLogTimestampType based on ICTimeStampType"""
    defaultValue = 0


_H3cICLogTimestampType_Type.__name__ = "ICTimeStampType"
_H3cICLogTimestampType_Object = MibScalar
h3cICLogTimestampType = _H3cICLogTimestampType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 119, 5, 1, 2),
    _H3cICLogTimestampType_Type()
)
h3cICLogTimestampType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cICLogTimestampType.setStatus("current")
_H3cICLogTable_Object = MibTable
h3cICLogTable = _H3cICLogTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 119, 5, 2)
)
if mibBuilder.loadTexts:
    h3cICLogTable.setStatus("current")
_H3cICLogEntry_Object = MibTableRow
h3cICLogEntry = _H3cICLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 119, 5, 2, 1)
)
h3cICLogEntry.setIndexNames(
    (0, "H3C-INFOCENTER-MIB", "h3cICDirectionIndex"),
    (1, "H3C-INFOCENTER-MIB", "h3cICModuleName"),
)
if mibBuilder.loadTexts:
    h3cICLogEntry.setStatus("current")
_H3cICLogLevel_Type = ICMessageLevelType
_H3cICLogLevel_Object = MibTableColumn
h3cICLogLevel = _H3cICLogLevel_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 119, 5, 2, 1, 1),
    _H3cICLogLevel_Type()
)
h3cICLogLevel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cICLogLevel.setStatus("current")
_H3cICLogRowStatus_Type = RowStatus
_H3cICLogRowStatus_Object = MibTableColumn
h3cICLogRowStatus = _H3cICLogRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 119, 5, 2, 1, 2),
    _H3cICLogRowStatus_Type()
)
h3cICLogRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cICLogRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "H3C-INFOCENTER-MIB",
    **{"ICMessageLevelType": ICMessageLevelType,
       "ICFacilityType": ICFacilityType,
       "ICTimeStampType": ICTimeStampType,
       "h3cInfoCenter": h3cInfoCenter,
       "h3cICLogbuffer": h3cICLogbuffer,
       "h3cICLogbufferObjects": h3cICLogbufferObjects,
       "h3cICMaxLogbufferSize": h3cICMaxLogbufferSize,
       "h3cICLogbufferSize": h3cICLogbufferSize,
       "h3cICLogbufferCurrentMessages": h3cICLogbufferCurrentMessages,
       "h3cICLogbufferOverwrittenMessages": h3cICLogbufferOverwrittenMessages,
       "h3cICLogbufferDroppedMessages": h3cICLogbufferDroppedMessages,
       "h3cICLogbufferContTable": h3cICLogbufferContTable,
       "h3cICLogbufferContEntry": h3cICLogbufferContEntry,
       "h3cICLogbufferContIndex": h3cICLogbufferContIndex,
       "h3cICLogbufferContDescription": h3cICLogbufferContDescription,
       "h3cICLoghost": h3cICLoghost,
       "h3cICLoghostObjects": h3cICLoghostObjects,
       "h3cICMaxLoghost": h3cICMaxLoghost,
       "h3cICLoghostSourceInterface": h3cICLoghostSourceInterface,
       "h3cICLoghostTimestampType": h3cICLoghostTimestampType,
       "h3cICLoghostTable": h3cICLoghostTable,
       "h3cICLoghostEntry": h3cICLoghostEntry,
       "h3cICLoghostIndex": h3cICLoghostIndex,
       "h3cICLoghostIpaddressType": h3cICLoghostIpaddressType,
       "h3cICLoghostIpaddress": h3cICLoghostIpaddress,
       "h3cICLoghostVPNName": h3cICLoghostVPNName,
       "h3cICLoghostFacility": h3cICLoghostFacility,
       "h3cICLoghostOperateRowStatus": h3cICLoghostOperateRowStatus,
       "h3cICLoghostIpaddressPort": h3cICLoghostIpaddressPort,
       "h3cICLoghostTAddress": h3cICLoghostTAddress,
       "h3cICDirection": h3cICDirection,
       "h3cICDirectionTable": h3cICDirectionTable,
       "h3cICDirectionEntry": h3cICDirectionEntry,
       "h3cICDirectionIndex": h3cICDirectionIndex,
       "h3cICDirectionName": h3cICDirectionName,
       "h3cICDirectionState": h3cICDirectionState,
       "h3cICModule": h3cICModule,
       "h3cICModuleTable": h3cICModuleTable,
       "h3cICModuleEntry": h3cICModuleEntry,
       "h3cICModuleName": h3cICModuleName,
       "h3cICLog": h3cICLog,
       "h3cICLogObjects": h3cICLogObjects,
       "h3cICLogGlobalState": h3cICLogGlobalState,
       "h3cICLogTimestampType": h3cICLogTimestampType,
       "h3cICLogTable": h3cICLogTable,
       "h3cICLogEntry": h3cICLogEntry,
       "h3cICLogLevel": h3cICLogLevel,
       "h3cICLogRowStatus": h3cICLogRowStatus}
)
