# SNMP MIB module (TIMETRA-PIM-SNOOPING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/nokia/TIMETRA-PIM-SNOOPING-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:58:00 2025
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

(vxlanVNI,
 vxlanVTEPAddr) = mibBuilder.importSymbols(
    "ALCATEL-IGMP-SNOOPING-MIB",
    "vxlanVNI",
    "vxlanVTEPAddr")

(InterfaceIndexOrZero,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero")

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
 RowStatus,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")

(tmnxCardHwIndex,) = mibBuilder.importSymbols(
    "TIMETRA-CHASSIS-MIB",
    "tmnxCardHwIndex")

(timetraSRMIBModules,
 tmnxSRConfs,
 tmnxSRNotifyPrefix,
 tmnxSRObjs) = mibBuilder.importSymbols(
    "TIMETRA-GLOBAL-MIB",
    "timetraSRMIBModules",
    "tmnxSRConfs",
    "tmnxSRNotifyPrefix",
    "tmnxSRObjs")

(vRtrPimNgAFGenAFType,) = mibBuilder.importSymbols(
    "TIMETRA-PIM-NG-MIB",
    "vRtrPimNgAFGenAFType")

(svcId,) = mibBuilder.importSymbols(
    "TIMETRA-SERV-MIB",
    "svcId")

(ServiceOperStatus,
 TNamedItemOrEmpty,
 TmnxAdminState,
 TmnxEncapVal,
 TmnxPortID) = mibBuilder.importSymbols(
    "TIMETRA-TC-MIB",
    "ServiceOperStatus",
    "TNamedItemOrEmpty",
    "TmnxAdminState",
    "TmnxEncapVal",
    "TmnxPortID")

(vRtrID,
 vRtrIfIndex) = mibBuilder.importSymbols(
    "TIMETRA-VRTR-MIB",
    "vRtrID",
    "vRtrIfIndex")


# MODULE-IDENTITY

timetraPimSnoopingMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 1, 1, 3, 53)
)
if mibBuilder.loadTexts:
    timetraPimSnoopingMIBModule.setRevisions(
        ("2017-01-01 00:00",
         "2016-01-01 00:00",
         "2015-01-01 00:00",
         "2009-02-28 00:00",
         "2008-01-01 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class TmnxPimSnpgOperState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 1),
          ("snoop", 2),
          ("proxy", 3))
    )



# MIB Managed Objects in the order of their OIDs

_TmnxPimSnpgConformance_ObjectIdentity = ObjectIdentity
tmnxPimSnpgConformance = _TmnxPimSnpgConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 53)
)
_TmnxPimSnpgCompliances_ObjectIdentity = ObjectIdentity
tmnxPimSnpgCompliances = _TmnxPimSnpgCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 53, 1)
)
_TmnxPimSnpgGroups_ObjectIdentity = ObjectIdentity
tmnxPimSnpgGroups = _TmnxPimSnpgGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 53, 2)
)
_TmnxPimSnpgVxlanCompliances_ObjectIdentity = ObjectIdentity
tmnxPimSnpgVxlanCompliances = _TmnxPimSnpgVxlanCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 53, 3)
)
_TmnxPimSnpgVxlanGroups_ObjectIdentity = ObjectIdentity
tmnxPimSnpgVxlanGroups = _TmnxPimSnpgVxlanGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 53, 4)
)
_TmnxPimSnpgEMplsCompliances_ObjectIdentity = ObjectIdentity
tmnxPimSnpgEMplsCompliances = _TmnxPimSnpgEMplsCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 53, 5)
)
_TmnxPimSnpgEMplsGroups_ObjectIdentity = ObjectIdentity
tmnxPimSnpgEMplsGroups = _TmnxPimSnpgEMplsGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 53, 6)
)
_TmnxPimSnpgRvplsCompliances_ObjectIdentity = ObjectIdentity
tmnxPimSnpgRvplsCompliances = _TmnxPimSnpgRvplsCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 53, 7)
)
_TmnxPimSnpgRvplsIfGroups_ObjectIdentity = ObjectIdentity
tmnxPimSnpgRvplsIfGroups = _TmnxPimSnpgRvplsIfGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 53, 8)
)
_TmnxPimSnpgObjs_ObjectIdentity = ObjectIdentity
tmnxPimSnpgObjs = _TmnxPimSnpgObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53)
)
_TmnxPimSnpgProtocolObjs_ObjectIdentity = ObjectIdentity
tmnxPimSnpgProtocolObjs = _TmnxPimSnpgProtocolObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 1)
)
_TmnxPimSnpgGenTableLstChanged_Type = TimeStamp
_TmnxPimSnpgGenTableLstChanged_Object = MibScalar
tmnxPimSnpgGenTableLstChanged = _TmnxPimSnpgGenTableLstChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 1, 1),
    _TmnxPimSnpgGenTableLstChanged_Type()
)
tmnxPimSnpgGenTableLstChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPimSnpgGenTableLstChanged.setStatus("current")
_TmnxPimSnpgGeneralTable_Object = MibTable
tmnxPimSnpgGeneralTable = _TmnxPimSnpgGeneralTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 1, 2)
)
if mibBuilder.loadTexts:
    tmnxPimSnpgGeneralTable.setStatus("current")
_TmnxPimSnpgGeneralEntry_Object = MibTableRow
tmnxPimSnpgGeneralEntry = _TmnxPimSnpgGeneralEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 1, 2, 1)
)
tmnxPimSnpgGeneralEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-PIM-NG-MIB", "vRtrPimNgAFGenAFType"),
)
if mibBuilder.loadTexts:
    tmnxPimSnpgGeneralEntry.setStatus("current")
_TmnxPimSnpgGenRowStatus_Type = RowStatus
_TmnxPimSnpgGenRowStatus_Object = MibTableColumn
tmnxPimSnpgGenRowStatus = _TmnxPimSnpgGenRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 1, 2, 1, 1),
    _TmnxPimSnpgGenRowStatus_Type()
)
tmnxPimSnpgGenRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxPimSnpgGenRowStatus.setStatus("current")
_TmnxPimSnpgGenRowLastChanged_Type = TimeStamp
_TmnxPimSnpgGenRowLastChanged_Object = MibTableColumn
tmnxPimSnpgGenRowLastChanged = _TmnxPimSnpgGenRowLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 1, 2, 1, 2),
    _TmnxPimSnpgGenRowLastChanged_Type()
)
tmnxPimSnpgGenRowLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPimSnpgGenRowLastChanged.setStatus("current")


class _TmnxPimSnpgGenAdminState_Type(TmnxAdminState):
    """Custom type tmnxPimSnpgGenAdminState based on TmnxAdminState"""
    defaultValue = 2


_TmnxPimSnpgGenAdminState_Type.__name__ = "TmnxAdminState"
_TmnxPimSnpgGenAdminState_Object = MibTableColumn
tmnxPimSnpgGenAdminState = _TmnxPimSnpgGenAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 1, 2, 1, 3),
    _TmnxPimSnpgGenAdminState_Type()
)
tmnxPimSnpgGenAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxPimSnpgGenAdminState.setStatus("current")


class _TmnxPimSnpgGenOperState_Type(TmnxPimSnpgOperState):
    """Custom type tmnxPimSnpgGenOperState based on TmnxPimSnpgOperState"""
    defaultValue = 1


_TmnxPimSnpgGenOperState_Type.__name__ = "TmnxPimSnpgOperState"
_TmnxPimSnpgGenOperState_Object = MibTableColumn
tmnxPimSnpgGenOperState = _TmnxPimSnpgGenOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 1, 2, 1, 4),
    _TmnxPimSnpgGenOperState_Type()
)
tmnxPimSnpgGenOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPimSnpgGenOperState.setStatus("current")


class _TmnxPimSnpgGenHoldTime_Type(Unsigned32):
    """Custom type tmnxPimSnpgGenHoldTime based on Unsigned32"""
    defaultValue = 90

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 300),
    )


_TmnxPimSnpgGenHoldTime_Type.__name__ = "Unsigned32"
_TmnxPimSnpgGenHoldTime_Object = MibTableColumn
tmnxPimSnpgGenHoldTime = _TmnxPimSnpgGenHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 1, 2, 1, 5),
    _TmnxPimSnpgGenHoldTime_Type()
)
tmnxPimSnpgGenHoldTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxPimSnpgGenHoldTime.setStatus("current")
if mibBuilder.loadTexts:
    tmnxPimSnpgGenHoldTime.setUnits("seconds")
_TmnxPimSnpgGenDRType_Type = InetAddressType
_TmnxPimSnpgGenDRType_Object = MibTableColumn
tmnxPimSnpgGenDRType = _TmnxPimSnpgGenDRType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 1, 2, 1, 6),
    _TmnxPimSnpgGenDRType_Type()
)
tmnxPimSnpgGenDRType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPimSnpgGenDRType.setStatus("current")


class _TmnxPimSnpgGenDR_Type(InetAddress):
    """Custom type tmnxPimSnpgGenDR based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxPimSnpgGenDR_Type.__name__ = "InetAddress"
_TmnxPimSnpgGenDR_Object = MibTableColumn
tmnxPimSnpgGenDR = _TmnxPimSnpgGenDR_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 1, 2, 1, 7),
    _TmnxPimSnpgGenDR_Type()
)
tmnxPimSnpgGenDR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPimSnpgGenDR.setStatus("current")
_TmnxPimSnpgGenTrackingSupport_Type = TruthValue
_TmnxPimSnpgGenTrackingSupport_Object = MibTableColumn
tmnxPimSnpgGenTrackingSupport = _TmnxPimSnpgGenTrackingSupport_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 1, 2, 1, 8),
    _TmnxPimSnpgGenTrackingSupport_Type()
)
tmnxPimSnpgGenTrackingSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPimSnpgGenTrackingSupport.setStatus("current")
_TmnxPimSnpgGenUpTime_Type = Unsigned32
_TmnxPimSnpgGenUpTime_Object = MibTableColumn
tmnxPimSnpgGenUpTime = _TmnxPimSnpgGenUpTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 1, 2, 1, 9),
    _TmnxPimSnpgGenUpTime_Type()
)
tmnxPimSnpgGenUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPimSnpgGenUpTime.setStatus("current")
if mibBuilder.loadTexts:
    tmnxPimSnpgGenUpTime.setUnits("seconds")


class _TmnxPimSnpgGenMode_Type(Integer32):
    """Custom type tmnxPimSnpgGenMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("proxy", 1),
          ("snoop", 2))
    )


_TmnxPimSnpgGenMode_Type.__name__ = "Integer32"
_TmnxPimSnpgGenMode_Object = MibTableColumn
tmnxPimSnpgGenMode = _TmnxPimSnpgGenMode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 1, 2, 1, 10),
    _TmnxPimSnpgGenMode_Type()
)
tmnxPimSnpgGenMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxPimSnpgGenMode.setStatus("current")


class _TmnxPimSnpgGenGroupPolicy1_Type(TNamedItemOrEmpty):
    """Custom type tmnxPimSnpgGenGroupPolicy1 based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxPimSnpgGenGroupPolicy1_Type.__name__ = "TNamedItemOrEmpty"
_TmnxPimSnpgGenGroupPolicy1_Object = MibTableColumn
tmnxPimSnpgGenGroupPolicy1 = _TmnxPimSnpgGenGroupPolicy1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 1, 2, 1, 11),
    _TmnxPimSnpgGenGroupPolicy1_Type()
)
tmnxPimSnpgGenGroupPolicy1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxPimSnpgGenGroupPolicy1.setStatus("current")


class _TmnxPimSnpgGenGroupPolicy2_Type(TNamedItemOrEmpty):
    """Custom type tmnxPimSnpgGenGroupPolicy2 based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxPimSnpgGenGroupPolicy2_Type.__name__ = "TNamedItemOrEmpty"
_TmnxPimSnpgGenGroupPolicy2_Object = MibTableColumn
tmnxPimSnpgGenGroupPolicy2 = _TmnxPimSnpgGenGroupPolicy2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 1, 2, 1, 12),
    _TmnxPimSnpgGenGroupPolicy2_Type()
)
tmnxPimSnpgGenGroupPolicy2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxPimSnpgGenGroupPolicy2.setStatus("current")


class _TmnxPimSnpgGenGroupPolicy3_Type(TNamedItemOrEmpty):
    """Custom type tmnxPimSnpgGenGroupPolicy3 based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxPimSnpgGenGroupPolicy3_Type.__name__ = "TNamedItemOrEmpty"
_TmnxPimSnpgGenGroupPolicy3_Object = MibTableColumn
tmnxPimSnpgGenGroupPolicy3 = _TmnxPimSnpgGenGroupPolicy3_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 1, 2, 1, 13),
    _TmnxPimSnpgGenGroupPolicy3_Type()
)
tmnxPimSnpgGenGroupPolicy3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxPimSnpgGenGroupPolicy3.setStatus("current")


class _TmnxPimSnpgGenGroupPolicy4_Type(TNamedItemOrEmpty):
    """Custom type tmnxPimSnpgGenGroupPolicy4 based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxPimSnpgGenGroupPolicy4_Type.__name__ = "TNamedItemOrEmpty"
_TmnxPimSnpgGenGroupPolicy4_Object = MibTableColumn
tmnxPimSnpgGenGroupPolicy4 = _TmnxPimSnpgGenGroupPolicy4_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 1, 2, 1, 14),
    _TmnxPimSnpgGenGroupPolicy4_Type()
)
tmnxPimSnpgGenGroupPolicy4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxPimSnpgGenGroupPolicy4.setStatus("current")


class _TmnxPimSnpgGenGroupPolicy5_Type(TNamedItemOrEmpty):
    """Custom type tmnxPimSnpgGenGroupPolicy5 based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxPimSnpgGenGroupPolicy5_Type.__name__ = "TNamedItemOrEmpty"
_TmnxPimSnpgGenGroupPolicy5_Object = MibTableColumn
tmnxPimSnpgGenGroupPolicy5 = _TmnxPimSnpgGenGroupPolicy5_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 1, 2, 1, 15),
    _TmnxPimSnpgGenGroupPolicy5_Type()
)
tmnxPimSnpgGenGroupPolicy5.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxPimSnpgGenGroupPolicy5.setStatus("current")
_TmnxPimSnpgGrpSrcTable_Object = MibTable
tmnxPimSnpgGrpSrcTable = _TmnxPimSnpgGrpSrcTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 1, 3)
)
if mibBuilder.loadTexts:
    tmnxPimSnpgGrpSrcTable.setStatus("current")
_TmnxPimSnpgGrpSrcEntry_Object = MibTableRow
tmnxPimSnpgGrpSrcEntry = _TmnxPimSnpgGrpSrcEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 1, 3, 1)
)
tmnxPimSnpgGrpSrcEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-PIM-SNOOPING-MIB", "tmnxPimSnpgGrpSrcGrpAddrType"),
    (0, "TIMETRA-PIM-SNOOPING-MIB", "tmnxPimSnpgGrpSrcGroupAddress"),
    (0, "TIMETRA-PIM-SNOOPING-MIB", "tmnxPimSnpgGrpSrcSrcAddrType"),
    (0, "TIMETRA-PIM-SNOOPING-MIB", "tmnxPimSnpgGrpSrcSourceAddress"),
)
if mibBuilder.loadTexts:
    tmnxPimSnpgGrpSrcEntry.setStatus("current")
_TmnxPimSnpgGrpSrcGrpAddrType_Type = InetAddressType
_TmnxPimSnpgGrpSrcGrpAddrType_Object = MibTableColumn
tmnxPimSnpgGrpSrcGrpAddrType = _TmnxPimSnpgGrpSrcGrpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 1, 3, 1, 1),
    _TmnxPimSnpgGrpSrcGrpAddrType_Type()
)
tmnxPimSnpgGrpSrcGrpAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxPimSnpgGrpSrcGrpAddrType.setStatus("current")


class _TmnxPimSnpgGrpSrcGroupAddress_Type(InetAddress):
    """Custom type tmnxPimSnpgGrpSrcGroupAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxPimSnpgGrpSrcGroupAddress_Type.__name__ = "InetAddress"
_TmnxPimSnpgGrpSrcGroupAddress_Object = MibTableColumn
tmnxPimSnpgGrpSrcGroupAddress = _TmnxPimSnpgGrpSrcGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 1, 3, 1, 2),
    _TmnxPimSnpgGrpSrcGroupAddress_Type()
)
tmnxPimSnpgGrpSrcGroupAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxPimSnpgGrpSrcGroupAddress.setStatus("current")
_TmnxPimSnpgGrpSrcSrcAddrType_Type = InetAddressType
_TmnxPimSnpgGrpSrcSrcAddrType_Object = MibTableColumn
tmnxPimSnpgGrpSrcSrcAddrType = _TmnxPimSnpgGrpSrcSrcAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 1, 3, 1, 3),
    _TmnxPimSnpgGrpSrcSrcAddrType_Type()
)
tmnxPimSnpgGrpSrcSrcAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxPimSnpgGrpSrcSrcAddrType.setStatus("current")


class _TmnxPimSnpgGrpSrcSourceAddress_Type(InetAddress):
    """Custom type tmnxPimSnpgGrpSrcSourceAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxPimSnpgGrpSrcSourceAddress_Type.__name__ = "InetAddress"
_TmnxPimSnpgGrpSrcSourceAddress_Object = MibTableColumn
tmnxPimSnpgGrpSrcSourceAddress = _TmnxPimSnpgGrpSrcSourceAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 1, 3, 1, 4),
    _TmnxPimSnpgGrpSrcSourceAddress_Type()
)
tmnxPimSnpgGrpSrcSourceAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxPimSnpgGrpSrcSourceAddress.setStatus("current")
_TmnxPimSnpgGrpSrcRpfNbrAddrType_Type = InetAddressType
_TmnxPimSnpgGrpSrcRpfNbrAddrType_Object = MibTableColumn
tmnxPimSnpgGrpSrcRpfNbrAddrType = _TmnxPimSnpgGrpSrcRpfNbrAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 1, 3, 1, 5),
    _TmnxPimSnpgGrpSrcRpfNbrAddrType_Type()
)
tmnxPimSnpgGrpSrcRpfNbrAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPimSnpgGrpSrcRpfNbrAddrType.setStatus("current")


class _TmnxPimSnpgGrpSrcRpfNbrAddr_Type(InetAddress):
    """Custom type tmnxPimSnpgGrpSrcRpfNbrAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxPimSnpgGrpSrcRpfNbrAddr_Type.__name__ = "InetAddress"
_TmnxPimSnpgGrpSrcRpfNbrAddr_Object = MibTableColumn
tmnxPimSnpgGrpSrcRpfNbrAddr = _TmnxPimSnpgGrpSrcRpfNbrAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 1, 3, 1, 6),
    _TmnxPimSnpgGrpSrcRpfNbrAddr_Type()
)
tmnxPimSnpgGrpSrcRpfNbrAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPimSnpgGrpSrcRpfNbrAddr.setStatus("current")
_TmnxPimSnpgGrpSrcRpfIfIndex_Type = InterfaceIndexOrZero
_TmnxPimSnpgGrpSrcRpfIfIndex_Object = MibTableColumn
tmnxPimSnpgGrpSrcRpfIfIndex = _TmnxPimSnpgGrpSrcRpfIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 1, 3, 1, 7),
    _TmnxPimSnpgGrpSrcRpfIfIndex_Type()
)
tmnxPimSnpgGrpSrcRpfIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPimSnpgGrpSrcRpfIfIndex.setStatus("current")
_TmnxPimSnpgGrpSrcRptRpfNbrAdrTp_Type = InetAddressType
_TmnxPimSnpgGrpSrcRptRpfNbrAdrTp_Object = MibTableColumn
tmnxPimSnpgGrpSrcRptRpfNbrAdrTp = _TmnxPimSnpgGrpSrcRptRpfNbrAdrTp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 1, 3, 1, 8),
    _TmnxPimSnpgGrpSrcRptRpfNbrAdrTp_Type()
)
tmnxPimSnpgGrpSrcRptRpfNbrAdrTp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPimSnpgGrpSrcRptRpfNbrAdrTp.setStatus("current")


class _TmnxPimSnpgGrpSrcRptRpfNbrAddr_Type(InetAddress):
    """Custom type tmnxPimSnpgGrpSrcRptRpfNbrAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxPimSnpgGrpSrcRptRpfNbrAddr_Type.__name__ = "InetAddress"
_TmnxPimSnpgGrpSrcRptRpfNbrAddr_Object = MibTableColumn
tmnxPimSnpgGrpSrcRptRpfNbrAddr = _TmnxPimSnpgGrpSrcRptRpfNbrAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 1, 3, 1, 9),
    _TmnxPimSnpgGrpSrcRptRpfNbrAddr_Type()
)
tmnxPimSnpgGrpSrcRptRpfNbrAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPimSnpgGrpSrcRptRpfNbrAddr.setStatus("current")


class _TmnxPimSnpgGrpSrcUstrmJpState_Type(Integer32):
    """Custom type tmnxPimSnpgGrpSrcUstrmJpState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("no-info", 0),
          ("joined", 1),
          ("prune-pend", 2),
          ("pruned", 3))
    )


_TmnxPimSnpgGrpSrcUstrmJpState_Type.__name__ = "Integer32"
_TmnxPimSnpgGrpSrcUstrmJpState_Object = MibTableColumn
tmnxPimSnpgGrpSrcUstrmJpState = _TmnxPimSnpgGrpSrcUstrmJpState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 1, 3, 1, 10),
    _TmnxPimSnpgGrpSrcUstrmJpState_Type()
)
tmnxPimSnpgGrpSrcUstrmJpState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPimSnpgGrpSrcUstrmJpState.setStatus("current")
_TmnxPimSnpgGrpSrcUstrmJpTimer_Type = Unsigned32
_TmnxPimSnpgGrpSrcUstrmJpTimer_Object = MibTableColumn
tmnxPimSnpgGrpSrcUstrmJpTimer = _TmnxPimSnpgGrpSrcUstrmJpTimer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 1, 3, 1, 11),
    _TmnxPimSnpgGrpSrcUstrmJpTimer_Type()
)
tmnxPimSnpgGrpSrcUstrmJpTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPimSnpgGrpSrcUstrmJpTimer.setStatus("current")
if mibBuilder.loadTexts:
    tmnxPimSnpgGrpSrcUstrmJpTimer.setUnits("seconds")


class _TmnxPimSnpgGrpSrcUstrmRptJpSt_Type(Integer32):
    """Custom type tmnxPimSnpgGrpSrcUstrmRptJpSt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notJoinedStarG", 0),
          ("notPruned", 1),
          ("pruned", 2))
    )


_TmnxPimSnpgGrpSrcUstrmRptJpSt_Type.__name__ = "Integer32"
_TmnxPimSnpgGrpSrcUstrmRptJpSt_Object = MibTableColumn
tmnxPimSnpgGrpSrcUstrmRptJpSt = _TmnxPimSnpgGrpSrcUstrmRptJpSt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 1, 3, 1, 12),
    _TmnxPimSnpgGrpSrcUstrmRptJpSt_Type()
)
tmnxPimSnpgGrpSrcUstrmRptJpSt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPimSnpgGrpSrcUstrmRptJpSt.setStatus("current")
_TmnxPimSnpgGrpSrcUstrmRptOvdTmr_Type = Unsigned32
_TmnxPimSnpgGrpSrcUstrmRptOvdTmr_Object = MibTableColumn
tmnxPimSnpgGrpSrcUstrmRptOvdTmr = _TmnxPimSnpgGrpSrcUstrmRptOvdTmr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 1, 3, 1, 13),
    _TmnxPimSnpgGrpSrcUstrmRptOvdTmr_Type()
)
tmnxPimSnpgGrpSrcUstrmRptOvdTmr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPimSnpgGrpSrcUstrmRptOvdTmr.setStatus("current")
if mibBuilder.loadTexts:
    tmnxPimSnpgGrpSrcUstrmRptOvdTmr.setUnits("seconds")
_TmnxPimSnpgGrpSrcNumJoinOif_Type = Gauge32
_TmnxPimSnpgGrpSrcNumJoinOif_Object = MibTableColumn
tmnxPimSnpgGrpSrcNumJoinOif = _TmnxPimSnpgGrpSrcNumJoinOif_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 1, 3, 1, 14),
    _TmnxPimSnpgGrpSrcNumJoinOif_Type()
)
tmnxPimSnpgGrpSrcNumJoinOif.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPimSnpgGrpSrcNumJoinOif.setStatus("current")
_TmnxPimSnpgGrpSrcNumImdiateOif_Type = Gauge32
_TmnxPimSnpgGrpSrcNumImdiateOif_Object = MibTableColumn
tmnxPimSnpgGrpSrcNumImdiateOif = _TmnxPimSnpgGrpSrcNumImdiateOif_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 1, 3, 1, 15),
    _TmnxPimSnpgGrpSrcNumImdiateOif_Type()
)
tmnxPimSnpgGrpSrcNumImdiateOif.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPimSnpgGrpSrcNumImdiateOif.setStatus("current")
_TmnxPimSnpgGrpSrcNumInhritedOif_Type = Gauge32
_TmnxPimSnpgGrpSrcNumInhritedOif_Object = MibTableColumn
tmnxPimSnpgGrpSrcNumInhritedOif = _TmnxPimSnpgGrpSrcNumInhritedOif_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 1, 3, 1, 16),
    _TmnxPimSnpgGrpSrcNumInhritedOif_Type()
)
tmnxPimSnpgGrpSrcNumInhritedOif.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPimSnpgGrpSrcNumInhritedOif.setStatus("current")
_TmnxPimSnpgGrpSrcNumInherRptOif_Type = Gauge32
_TmnxPimSnpgGrpSrcNumInherRptOif_Object = MibTableColumn
tmnxPimSnpgGrpSrcNumInherRptOif = _TmnxPimSnpgGrpSrcNumInherRptOif_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 1, 3, 1, 17),
    _TmnxPimSnpgGrpSrcNumInherRptOif_Type()
)
tmnxPimSnpgGrpSrcNumInherRptOif.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPimSnpgGrpSrcNumInherRptOif.setStatus("current")
_TmnxPimSnpgGrpSrcNumIif_Type = Gauge32
_TmnxPimSnpgGrpSrcNumIif_Object = MibTableColumn
tmnxPimSnpgGrpSrcNumIif = _TmnxPimSnpgGrpSrcNumIif_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 1, 3, 1, 18),
    _TmnxPimSnpgGrpSrcNumIif_Type()
)
tmnxPimSnpgGrpSrcNumIif.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPimSnpgGrpSrcNumIif.setStatus("current")
_TmnxPimSnpgGrpSrcUpTime_Type = Unsigned32
_TmnxPimSnpgGrpSrcUpTime_Object = MibTableColumn
tmnxPimSnpgGrpSrcUpTime = _TmnxPimSnpgGrpSrcUpTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 1, 3, 1, 19),
    _TmnxPimSnpgGrpSrcUpTime_Type()
)
tmnxPimSnpgGrpSrcUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPimSnpgGrpSrcUpTime.setStatus("current")
if mibBuilder.loadTexts:
    tmnxPimSnpgGrpSrcUpTime.setUnits("seconds")
_TmnxPimSnpgGrpSrcIfTable_Object = MibTable
tmnxPimSnpgGrpSrcIfTable = _TmnxPimSnpgGrpSrcIfTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 1, 4)
)
if mibBuilder.loadTexts:
    tmnxPimSnpgGrpSrcIfTable.setStatus("current")
_TmnxPimSnpgGrpSrcIfEntry_Object = MibTableRow
tmnxPimSnpgGrpSrcIfEntry = _TmnxPimSnpgGrpSrcIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 1, 4, 1)
)
tmnxPimSnpgGrpSrcIfEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-PIM-SNOOPING-MIB", "tmnxPimSnpgGrpSrcGrpAddrType"),
    (0, "TIMETRA-PIM-SNOOPING-MIB", "tmnxPimSnpgGrpSrcGroupAddress"),
    (0, "TIMETRA-PIM-SNOOPING-MIB", "tmnxPimSnpgGrpSrcSrcAddrType"),
    (0, "TIMETRA-PIM-SNOOPING-MIB", "tmnxPimSnpgGrpSrcSourceAddress"),
    (0, "TIMETRA-PIM-SNOOPING-MIB", "tmnxPimSnpgPortId"),
    (0, "TIMETRA-PIM-SNOOPING-MIB", "tmnxPimSnpgEncapValue"),
)
if mibBuilder.loadTexts:
    tmnxPimSnpgGrpSrcIfEntry.setStatus("current")
_TmnxPimSnpgPortId_Type = TmnxPortID
_TmnxPimSnpgPortId_Object = MibTableColumn
tmnxPimSnpgPortId = _TmnxPimSnpgPortId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 1, 4, 1, 1),
    _TmnxPimSnpgPortId_Type()
)
tmnxPimSnpgPortId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxPimSnpgPortId.setStatus("current")
_TmnxPimSnpgEncapValue_Type = TmnxEncapVal
_TmnxPimSnpgEncapValue_Object = MibTableColumn
tmnxPimSnpgEncapValue = _TmnxPimSnpgEncapValue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 1, 4, 1, 2),
    _TmnxPimSnpgEncapValue_Type()
)
tmnxPimSnpgEncapValue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxPimSnpgEncapValue.setStatus("current")


class _TmnxPimSnpgGrpSrcIfFlags_Type(Bits):
    """Custom type tmnxPimSnpgGrpSrcIfFlags based on Bits"""
    namedValues = NamedValues(
        *(("immediateOifList", 0),
          ("inheritedOifList", 1),
          ("inheritedRptOifList", 2),
          ("joined", 3),
          ("rpfPort", 4))
    )

_TmnxPimSnpgGrpSrcIfFlags_Type.__name__ = "Bits"
_TmnxPimSnpgGrpSrcIfFlags_Object = MibTableColumn
tmnxPimSnpgGrpSrcIfFlags = _TmnxPimSnpgGrpSrcIfFlags_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 1, 4, 1, 3),
    _TmnxPimSnpgGrpSrcIfFlags_Type()
)
tmnxPimSnpgGrpSrcIfFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPimSnpgGrpSrcIfFlags.setStatus("current")
_TmnxPimSnpgGenStatsTable_Object = MibTable
tmnxPimSnpgGenStatsTable = _TmnxPimSnpgGenStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 1, 5)
)
if mibBuilder.loadTexts:
    tmnxPimSnpgGenStatsTable.setStatus("current")
_TmnxPimSnpgGenStatsEntry_Object = MibTableRow
tmnxPimSnpgGenStatsEntry = _TmnxPimSnpgGenStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 1, 5, 1)
)
if mibBuilder.loadTexts:
    tmnxPimSnpgGenStatsEntry.setStatus("current")
_TmnxPimSnpgGenStatsStarGTypes_Type = Gauge32
_TmnxPimSnpgGenStatsStarGTypes_Object = MibTableColumn
tmnxPimSnpgGenStatsStarGTypes = _TmnxPimSnpgGenStatsStarGTypes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 1, 5, 1, 1),
    _TmnxPimSnpgGenStatsStarGTypes_Type()
)
tmnxPimSnpgGenStatsStarGTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPimSnpgGenStatsStarGTypes.setStatus("current")
_TmnxPimSnpgGenStatsSGTypes_Type = Gauge32
_TmnxPimSnpgGenStatsSGTypes_Object = MibTableColumn
tmnxPimSnpgGenStatsSGTypes = _TmnxPimSnpgGenStatsSGTypes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 1, 5, 1, 2),
    _TmnxPimSnpgGenStatsSGTypes_Type()
)
tmnxPimSnpgGenStatsSGTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPimSnpgGenStatsSGTypes.setStatus("current")
_TmnxPimSnpgGrpSrcStatsTable_Object = MibTable
tmnxPimSnpgGrpSrcStatsTable = _TmnxPimSnpgGrpSrcStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 1, 6)
)
if mibBuilder.loadTexts:
    tmnxPimSnpgGrpSrcStatsTable.setStatus("current")
_TmnxPimSnpgGrpSrcStatsEntry_Object = MibTableRow
tmnxPimSnpgGrpSrcStatsEntry = _TmnxPimSnpgGrpSrcStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 1, 6, 1)
)
if mibBuilder.loadTexts:
    tmnxPimSnpgGrpSrcStatsEntry.setStatus("current")
_TmnxPimSnpgGrpSrcStatsFwdedPkts_Type = Counter32
_TmnxPimSnpgGrpSrcStatsFwdedPkts_Object = MibTableColumn
tmnxPimSnpgGrpSrcStatsFwdedPkts = _TmnxPimSnpgGrpSrcStatsFwdedPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 1, 6, 1, 1),
    _TmnxPimSnpgGrpSrcStatsFwdedPkts_Type()
)
tmnxPimSnpgGrpSrcStatsFwdedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPimSnpgGrpSrcStatsFwdedPkts.setStatus("current")
_TmnxPimSnpgGrpSrcStatsFwdedOct_Type = Counter32
_TmnxPimSnpgGrpSrcStatsFwdedOct_Object = MibTableColumn
tmnxPimSnpgGrpSrcStatsFwdedOct = _TmnxPimSnpgGrpSrcStatsFwdedOct_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 1, 6, 1, 2),
    _TmnxPimSnpgGrpSrcStatsFwdedOct_Type()
)
tmnxPimSnpgGrpSrcStatsFwdedOct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPimSnpgGrpSrcStatsFwdedOct.setStatus("current")
_TmnxPimSnpgIfObjs_ObjectIdentity = ObjectIdentity
tmnxPimSnpgIfObjs = _TmnxPimSnpgIfObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 2)
)
_TmnxPimSnpgIfTableLastChanged_Type = TimeStamp
_TmnxPimSnpgIfTableLastChanged_Object = MibScalar
tmnxPimSnpgIfTableLastChanged = _TmnxPimSnpgIfTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 2, 1),
    _TmnxPimSnpgIfTableLastChanged_Type()
)
tmnxPimSnpgIfTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPimSnpgIfTableLastChanged.setStatus("current")
_TmnxPimSnpgIfTable_Object = MibTable
tmnxPimSnpgIfTable = _TmnxPimSnpgIfTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 2, 2)
)
if mibBuilder.loadTexts:
    tmnxPimSnpgIfTable.setStatus("current")
_TmnxPimSnpgIfEntry_Object = MibTableRow
tmnxPimSnpgIfEntry = _TmnxPimSnpgIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 2, 2, 1)
)
tmnxPimSnpgIfEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-PIM-SNOOPING-MIB", "tmnxPimSnpgPortId"),
    (0, "TIMETRA-PIM-SNOOPING-MIB", "tmnxPimSnpgEncapValue"),
    (0, "TIMETRA-PIM-NG-MIB", "vRtrPimNgAFGenAFType"),
)
if mibBuilder.loadTexts:
    tmnxPimSnpgIfEntry.setStatus("current")
_TmnxPimSnpgIfLastChangeTime_Type = TimeStamp
_TmnxPimSnpgIfLastChangeTime_Object = MibTableColumn
tmnxPimSnpgIfLastChangeTime = _TmnxPimSnpgIfLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 2, 2, 1, 1),
    _TmnxPimSnpgIfLastChangeTime_Type()
)
tmnxPimSnpgIfLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPimSnpgIfLastChangeTime.setStatus("current")
_TmnxPimSnpgIfOperState_Type = ServiceOperStatus
_TmnxPimSnpgIfOperState_Object = MibTableColumn
tmnxPimSnpgIfOperState = _TmnxPimSnpgIfOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 2, 2, 1, 2),
    _TmnxPimSnpgIfOperState_Type()
)
tmnxPimSnpgIfOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPimSnpgIfOperState.setStatus("current")
_TmnxPimSnpgIfUpTime_Type = Unsigned32
_TmnxPimSnpgIfUpTime_Object = MibTableColumn
tmnxPimSnpgIfUpTime = _TmnxPimSnpgIfUpTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 2, 2, 1, 3),
    _TmnxPimSnpgIfUpTime_Type()
)
tmnxPimSnpgIfUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPimSnpgIfUpTime.setStatus("current")
if mibBuilder.loadTexts:
    tmnxPimSnpgIfUpTime.setUnits("seconds")


class _TmnxPimSnpgIfMaxGroups_Type(Unsigned32):
    """Custom type tmnxPimSnpgIfMaxGroups based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 16000),
    )


_TmnxPimSnpgIfMaxGroups_Type.__name__ = "Unsigned32"
_TmnxPimSnpgIfMaxGroups_Object = MibTableColumn
tmnxPimSnpgIfMaxGroups = _TmnxPimSnpgIfMaxGroups_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 2, 2, 1, 4),
    _TmnxPimSnpgIfMaxGroups_Type()
)
tmnxPimSnpgIfMaxGroups.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxPimSnpgIfMaxGroups.setStatus("current")
_TmnxPimSnpgIfCurrentGroups_Type = Gauge32
_TmnxPimSnpgIfCurrentGroups_Object = MibTableColumn
tmnxPimSnpgIfCurrentGroups = _TmnxPimSnpgIfCurrentGroups_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 2, 2, 1, 5),
    _TmnxPimSnpgIfCurrentGroups_Type()
)
tmnxPimSnpgIfCurrentGroups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPimSnpgIfCurrentGroups.setStatus("current")
_TmnxPimSnpgIfMaxGroupsTillNow_Type = Counter32
_TmnxPimSnpgIfMaxGroupsTillNow_Object = MibTableColumn
tmnxPimSnpgIfMaxGroupsTillNow = _TmnxPimSnpgIfMaxGroupsTillNow_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 2, 2, 1, 6),
    _TmnxPimSnpgIfMaxGroupsTillNow_Type()
)
tmnxPimSnpgIfMaxGroupsTillNow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPimSnpgIfMaxGroupsTillNow.setStatus("current")


class _TmnxPimSnpgIfPwFwding_Type(TruthValue):
    """Custom type tmnxPimSnpgIfPwFwding based on TruthValue"""
    defaultValue = 1


_TmnxPimSnpgIfPwFwding_Type.__name__ = "TruthValue"
_TmnxPimSnpgIfPwFwding_Object = MibTableColumn
tmnxPimSnpgIfPwFwding = _TmnxPimSnpgIfPwFwding_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 2, 2, 1, 7),
    _TmnxPimSnpgIfPwFwding_Type()
)
tmnxPimSnpgIfPwFwding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPimSnpgIfPwFwding.setStatus("current")
_TmnxPimSnpgIfNbrTable_Object = MibTable
tmnxPimSnpgIfNbrTable = _TmnxPimSnpgIfNbrTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 2, 3)
)
if mibBuilder.loadTexts:
    tmnxPimSnpgIfNbrTable.setStatus("current")
_TmnxPimSnpgIfNbrEntry_Object = MibTableRow
tmnxPimSnpgIfNbrEntry = _TmnxPimSnpgIfNbrEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 2, 3, 1)
)
tmnxPimSnpgIfNbrEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-PIM-SNOOPING-MIB", "tmnxPimSnpgPortId"),
    (0, "TIMETRA-PIM-SNOOPING-MIB", "tmnxPimSnpgEncapValue"),
    (0, "TIMETRA-PIM-SNOOPING-MIB", "tmnxPimSnpgIfNbrAddrType"),
    (0, "TIMETRA-PIM-SNOOPING-MIB", "tmnxPimSnpgIfNbrAddress"),
)
if mibBuilder.loadTexts:
    tmnxPimSnpgIfNbrEntry.setStatus("current")
_TmnxPimSnpgIfNbrAddrType_Type = InetAddressType
_TmnxPimSnpgIfNbrAddrType_Object = MibTableColumn
tmnxPimSnpgIfNbrAddrType = _TmnxPimSnpgIfNbrAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 2, 3, 1, 1),
    _TmnxPimSnpgIfNbrAddrType_Type()
)
tmnxPimSnpgIfNbrAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxPimSnpgIfNbrAddrType.setStatus("current")


class _TmnxPimSnpgIfNbrAddress_Type(InetAddress):
    """Custom type tmnxPimSnpgIfNbrAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxPimSnpgIfNbrAddress_Type.__name__ = "InetAddress"
_TmnxPimSnpgIfNbrAddress_Object = MibTableColumn
tmnxPimSnpgIfNbrAddress = _TmnxPimSnpgIfNbrAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 2, 3, 1, 2),
    _TmnxPimSnpgIfNbrAddress_Type()
)
tmnxPimSnpgIfNbrAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxPimSnpgIfNbrAddress.setStatus("current")
_TmnxPimSnpgIfNbrUpTime_Type = Unsigned32
_TmnxPimSnpgIfNbrUpTime_Object = MibTableColumn
tmnxPimSnpgIfNbrUpTime = _TmnxPimSnpgIfNbrUpTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 2, 3, 1, 3),
    _TmnxPimSnpgIfNbrUpTime_Type()
)
tmnxPimSnpgIfNbrUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPimSnpgIfNbrUpTime.setStatus("current")
if mibBuilder.loadTexts:
    tmnxPimSnpgIfNbrUpTime.setUnits("seconds")
_TmnxPimSnpgIfNbrExpiryTime_Type = Unsigned32
_TmnxPimSnpgIfNbrExpiryTime_Object = MibTableColumn
tmnxPimSnpgIfNbrExpiryTime = _TmnxPimSnpgIfNbrExpiryTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 2, 3, 1, 4),
    _TmnxPimSnpgIfNbrExpiryTime_Type()
)
tmnxPimSnpgIfNbrExpiryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPimSnpgIfNbrExpiryTime.setStatus("current")
if mibBuilder.loadTexts:
    tmnxPimSnpgIfNbrExpiryTime.setUnits("seconds")
_TmnxPimSnpgIfNbrGenId_Type = Unsigned32
_TmnxPimSnpgIfNbrGenId_Object = MibTableColumn
tmnxPimSnpgIfNbrGenId = _TmnxPimSnpgIfNbrGenId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 2, 3, 1, 5),
    _TmnxPimSnpgIfNbrGenId_Type()
)
tmnxPimSnpgIfNbrGenId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPimSnpgIfNbrGenId.setStatus("current")
_TmnxPimSnpgIfNbrDrPriority_Type = Unsigned32
_TmnxPimSnpgIfNbrDrPriority_Object = MibTableColumn
tmnxPimSnpgIfNbrDrPriority = _TmnxPimSnpgIfNbrDrPriority_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 2, 3, 1, 6),
    _TmnxPimSnpgIfNbrDrPriority_Type()
)
tmnxPimSnpgIfNbrDrPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPimSnpgIfNbrDrPriority.setStatus("current")
_TmnxPimSnpgIfNbrDrPriorPresent_Type = TruthValue
_TmnxPimSnpgIfNbrDrPriorPresent_Object = MibTableColumn
tmnxPimSnpgIfNbrDrPriorPresent = _TmnxPimSnpgIfNbrDrPriorPresent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 2, 3, 1, 7),
    _TmnxPimSnpgIfNbrDrPriorPresent_Type()
)
tmnxPimSnpgIfNbrDrPriorPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPimSnpgIfNbrDrPriorPresent.setStatus("current")
_TmnxPimSnpgIfNbrLanDelay_Type = Unsigned32
_TmnxPimSnpgIfNbrLanDelay_Object = MibTableColumn
tmnxPimSnpgIfNbrLanDelay = _TmnxPimSnpgIfNbrLanDelay_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 2, 3, 1, 8),
    _TmnxPimSnpgIfNbrLanDelay_Type()
)
tmnxPimSnpgIfNbrLanDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPimSnpgIfNbrLanDelay.setStatus("current")
if mibBuilder.loadTexts:
    tmnxPimSnpgIfNbrLanDelay.setUnits("milliseconds")
_TmnxPimSnpgIfNbrLanDlayPrsnt_Type = TruthValue
_TmnxPimSnpgIfNbrLanDlayPrsnt_Object = MibTableColumn
tmnxPimSnpgIfNbrLanDlayPrsnt = _TmnxPimSnpgIfNbrLanDlayPrsnt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 2, 3, 1, 9),
    _TmnxPimSnpgIfNbrLanDlayPrsnt_Type()
)
tmnxPimSnpgIfNbrLanDlayPrsnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPimSnpgIfNbrLanDlayPrsnt.setStatus("current")
_TmnxPimSnpgIfNbrTrckngSpprt_Type = TruthValue
_TmnxPimSnpgIfNbrTrckngSpprt_Object = MibTableColumn
tmnxPimSnpgIfNbrTrckngSpprt = _TmnxPimSnpgIfNbrTrckngSpprt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 2, 3, 1, 10),
    _TmnxPimSnpgIfNbrTrckngSpprt_Type()
)
tmnxPimSnpgIfNbrTrckngSpprt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPimSnpgIfNbrTrckngSpprt.setStatus("current")
_TmnxPimSnpgIfNbrHoldTime_Type = Unsigned32
_TmnxPimSnpgIfNbrHoldTime_Object = MibTableColumn
tmnxPimSnpgIfNbrHoldTime = _TmnxPimSnpgIfNbrHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 2, 3, 1, 11),
    _TmnxPimSnpgIfNbrHoldTime_Type()
)
tmnxPimSnpgIfNbrHoldTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPimSnpgIfNbrHoldTime.setStatus("current")
if mibBuilder.loadTexts:
    tmnxPimSnpgIfNbrHoldTime.setUnits("seconds")
_TmnxPimSnpgIfNbrOvrdeIntrvl_Type = Unsigned32
_TmnxPimSnpgIfNbrOvrdeIntrvl_Object = MibTableColumn
tmnxPimSnpgIfNbrOvrdeIntrvl = _TmnxPimSnpgIfNbrOvrdeIntrvl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 2, 3, 1, 12),
    _TmnxPimSnpgIfNbrOvrdeIntrvl_Type()
)
tmnxPimSnpgIfNbrOvrdeIntrvl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPimSnpgIfNbrOvrdeIntrvl.setStatus("current")
if mibBuilder.loadTexts:
    tmnxPimSnpgIfNbrOvrdeIntrvl.setUnits("milliseconds")
_TmnxPimSnpgIfGrpSrcTable_Object = MibTable
tmnxPimSnpgIfGrpSrcTable = _TmnxPimSnpgIfGrpSrcTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 2, 4)
)
if mibBuilder.loadTexts:
    tmnxPimSnpgIfGrpSrcTable.setStatus("current")
_TmnxPimSnpgIfGrpSrcEntry_Object = MibTableRow
tmnxPimSnpgIfGrpSrcEntry = _TmnxPimSnpgIfGrpSrcEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 2, 4, 1)
)
tmnxPimSnpgIfGrpSrcEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-PIM-SNOOPING-MIB", "tmnxPimSnpgPortId"),
    (0, "TIMETRA-PIM-SNOOPING-MIB", "tmnxPimSnpgEncapValue"),
    (0, "TIMETRA-PIM-SNOOPING-MIB", "tmnxPimSnpgIfGrpSrcGrpAddrType"),
    (0, "TIMETRA-PIM-SNOOPING-MIB", "tmnxPimSnpgIfGrpSrcGroupAddr"),
    (0, "TIMETRA-PIM-SNOOPING-MIB", "tmnxPimSnpgIfGrpSrcSrcAddrType"),
    (0, "TIMETRA-PIM-SNOOPING-MIB", "tmnxPimSnpgIfGrpSrcSourceAddr"),
)
if mibBuilder.loadTexts:
    tmnxPimSnpgIfGrpSrcEntry.setStatus("current")
_TmnxPimSnpgIfGrpSrcGrpAddrType_Type = InetAddressType
_TmnxPimSnpgIfGrpSrcGrpAddrType_Object = MibTableColumn
tmnxPimSnpgIfGrpSrcGrpAddrType = _TmnxPimSnpgIfGrpSrcGrpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 2, 4, 1, 1),
    _TmnxPimSnpgIfGrpSrcGrpAddrType_Type()
)
tmnxPimSnpgIfGrpSrcGrpAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxPimSnpgIfGrpSrcGrpAddrType.setStatus("current")


class _TmnxPimSnpgIfGrpSrcGroupAddr_Type(InetAddress):
    """Custom type tmnxPimSnpgIfGrpSrcGroupAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxPimSnpgIfGrpSrcGroupAddr_Type.__name__ = "InetAddress"
_TmnxPimSnpgIfGrpSrcGroupAddr_Object = MibTableColumn
tmnxPimSnpgIfGrpSrcGroupAddr = _TmnxPimSnpgIfGrpSrcGroupAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 2, 4, 1, 2),
    _TmnxPimSnpgIfGrpSrcGroupAddr_Type()
)
tmnxPimSnpgIfGrpSrcGroupAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxPimSnpgIfGrpSrcGroupAddr.setStatus("current")
_TmnxPimSnpgIfGrpSrcSrcAddrType_Type = InetAddressType
_TmnxPimSnpgIfGrpSrcSrcAddrType_Object = MibTableColumn
tmnxPimSnpgIfGrpSrcSrcAddrType = _TmnxPimSnpgIfGrpSrcSrcAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 2, 4, 1, 3),
    _TmnxPimSnpgIfGrpSrcSrcAddrType_Type()
)
tmnxPimSnpgIfGrpSrcSrcAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxPimSnpgIfGrpSrcSrcAddrType.setStatus("current")


class _TmnxPimSnpgIfGrpSrcSourceAddr_Type(InetAddress):
    """Custom type tmnxPimSnpgIfGrpSrcSourceAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxPimSnpgIfGrpSrcSourceAddr_Type.__name__ = "InetAddress"
_TmnxPimSnpgIfGrpSrcSourceAddr_Object = MibTableColumn
tmnxPimSnpgIfGrpSrcSourceAddr = _TmnxPimSnpgIfGrpSrcSourceAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 2, 4, 1, 4),
    _TmnxPimSnpgIfGrpSrcSourceAddr_Type()
)
tmnxPimSnpgIfGrpSrcSourceAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxPimSnpgIfGrpSrcSourceAddr.setStatus("current")


class _TmnxPimSnpgIfGrpSrcJPState_Type(Integer32):
    """Custom type tmnxPimSnpgIfGrpSrcJPState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noInfo", 0),
          ("join", 1),
          ("prunePend", 2),
          ("pruned", 3))
    )


_TmnxPimSnpgIfGrpSrcJPState_Type.__name__ = "Integer32"
_TmnxPimSnpgIfGrpSrcJPState_Object = MibTableColumn
tmnxPimSnpgIfGrpSrcJPState = _TmnxPimSnpgIfGrpSrcJPState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 2, 4, 1, 5),
    _TmnxPimSnpgIfGrpSrcJPState_Type()
)
tmnxPimSnpgIfGrpSrcJPState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPimSnpgIfGrpSrcJPState.setStatus("current")
_TmnxPimSnpgIfGrpSrcPrunePendTmr_Type = Unsigned32
_TmnxPimSnpgIfGrpSrcPrunePendTmr_Object = MibTableColumn
tmnxPimSnpgIfGrpSrcPrunePendTmr = _TmnxPimSnpgIfGrpSrcPrunePendTmr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 2, 4, 1, 6),
    _TmnxPimSnpgIfGrpSrcPrunePendTmr_Type()
)
tmnxPimSnpgIfGrpSrcPrunePendTmr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPimSnpgIfGrpSrcPrunePendTmr.setStatus("current")
if mibBuilder.loadTexts:
    tmnxPimSnpgIfGrpSrcPrunePendTmr.setUnits("seconds")
_TmnxPimSnpgIfGrpSrcJPTimer_Type = Unsigned32
_TmnxPimSnpgIfGrpSrcJPTimer_Object = MibTableColumn
tmnxPimSnpgIfGrpSrcJPTimer = _TmnxPimSnpgIfGrpSrcJPTimer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 2, 4, 1, 7),
    _TmnxPimSnpgIfGrpSrcJPTimer_Type()
)
tmnxPimSnpgIfGrpSrcJPTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPimSnpgIfGrpSrcJPTimer.setStatus("current")
if mibBuilder.loadTexts:
    tmnxPimSnpgIfGrpSrcJPTimer.setUnits("seconds")


class _TmnxPimSnpgIfGrpSrcJPRptState_Type(Integer32):
    """Custom type tmnxPimSnpgIfGrpSrcJPRptState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noInfo", 0),
          ("join", 1),
          ("prunePend", 2),
          ("pruned", 3))
    )


_TmnxPimSnpgIfGrpSrcJPRptState_Type.__name__ = "Integer32"
_TmnxPimSnpgIfGrpSrcJPRptState_Object = MibTableColumn
tmnxPimSnpgIfGrpSrcJPRptState = _TmnxPimSnpgIfGrpSrcJPRptState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 2, 4, 1, 8),
    _TmnxPimSnpgIfGrpSrcJPRptState_Type()
)
tmnxPimSnpgIfGrpSrcJPRptState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPimSnpgIfGrpSrcJPRptState.setStatus("current")
_TmnxPimSnpgIfGrpSrcRptPrnPndTmr_Type = Unsigned32
_TmnxPimSnpgIfGrpSrcRptPrnPndTmr_Object = MibTableColumn
tmnxPimSnpgIfGrpSrcRptPrnPndTmr = _TmnxPimSnpgIfGrpSrcRptPrnPndTmr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 2, 4, 1, 9),
    _TmnxPimSnpgIfGrpSrcRptPrnPndTmr_Type()
)
tmnxPimSnpgIfGrpSrcRptPrnPndTmr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPimSnpgIfGrpSrcRptPrnPndTmr.setStatus("current")
if mibBuilder.loadTexts:
    tmnxPimSnpgIfGrpSrcRptPrnPndTmr.setUnits("seconds")
_TmnxPimSnpgIfGrpSrcRptJPTimer_Type = Unsigned32
_TmnxPimSnpgIfGrpSrcRptJPTimer_Object = MibTableColumn
tmnxPimSnpgIfGrpSrcRptJPTimer = _TmnxPimSnpgIfGrpSrcRptJPTimer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 2, 4, 1, 10),
    _TmnxPimSnpgIfGrpSrcRptJPTimer_Type()
)
tmnxPimSnpgIfGrpSrcRptJPTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPimSnpgIfGrpSrcRptJPTimer.setStatus("current")
if mibBuilder.loadTexts:
    tmnxPimSnpgIfGrpSrcRptJPTimer.setUnits("seconds")
_TmnxPimSnpgIfGrpSrcUpTime_Type = Unsigned32
_TmnxPimSnpgIfGrpSrcUpTime_Object = MibTableColumn
tmnxPimSnpgIfGrpSrcUpTime = _TmnxPimSnpgIfGrpSrcUpTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 2, 4, 1, 11),
    _TmnxPimSnpgIfGrpSrcUpTime_Type()
)
tmnxPimSnpgIfGrpSrcUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPimSnpgIfGrpSrcUpTime.setStatus("current")
if mibBuilder.loadTexts:
    tmnxPimSnpgIfGrpSrcUpTime.setUnits("seconds")
_TmnxPimSnpgIfStatsTable_Object = MibTable
tmnxPimSnpgIfStatsTable = _TmnxPimSnpgIfStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 2, 5)
)
if mibBuilder.loadTexts:
    tmnxPimSnpgIfStatsTable.setStatus("current")
_TmnxPimSnpgIfStatsEntry_Object = MibTableRow
tmnxPimSnpgIfStatsEntry = _TmnxPimSnpgIfStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 2, 5, 1)
)
if mibBuilder.loadTexts:
    tmnxPimSnpgIfStatsEntry.setStatus("current")
_TmnxPimSnpgIfTxPkts_Type = Counter32
_TmnxPimSnpgIfTxPkts_Object = MibTableColumn
tmnxPimSnpgIfTxPkts = _TmnxPimSnpgIfTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 2, 5, 1, 1),
    _TmnxPimSnpgIfTxPkts_Type()
)
tmnxPimSnpgIfTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPimSnpgIfTxPkts.setStatus("current")
_TmnxPimSnpgIfRxPkts_Type = Counter32
_TmnxPimSnpgIfRxPkts_Object = MibTableColumn
tmnxPimSnpgIfRxPkts = _TmnxPimSnpgIfRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 2, 5, 1, 2),
    _TmnxPimSnpgIfRxPkts_Type()
)
tmnxPimSnpgIfRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPimSnpgIfRxPkts.setStatus("current")
_TmnxPimSnpgIfRxHellos_Type = Counter32
_TmnxPimSnpgIfRxHellos_Object = MibTableColumn
tmnxPimSnpgIfRxHellos = _TmnxPimSnpgIfRxHellos_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 2, 5, 1, 3),
    _TmnxPimSnpgIfRxHellos_Type()
)
tmnxPimSnpgIfRxHellos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPimSnpgIfRxHellos.setStatus("current")
_TmnxPimSnpgIfRxHellosDropped_Type = Counter32
_TmnxPimSnpgIfRxHellosDropped_Object = MibTableColumn
tmnxPimSnpgIfRxHellosDropped = _TmnxPimSnpgIfRxHellosDropped_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 2, 5, 1, 4),
    _TmnxPimSnpgIfRxHellosDropped_Type()
)
tmnxPimSnpgIfRxHellosDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPimSnpgIfRxHellosDropped.setStatus("current")
_TmnxPimSnpgIfRxNbrUnknown_Type = Counter32
_TmnxPimSnpgIfRxNbrUnknown_Object = MibTableColumn
tmnxPimSnpgIfRxNbrUnknown = _TmnxPimSnpgIfRxNbrUnknown_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 2, 5, 1, 5),
    _TmnxPimSnpgIfRxNbrUnknown_Type()
)
tmnxPimSnpgIfRxNbrUnknown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPimSnpgIfRxNbrUnknown.setStatus("current")
_TmnxPimSnpgIfRxBadChecksumDscrd_Type = Counter32
_TmnxPimSnpgIfRxBadChecksumDscrd_Object = MibTableColumn
tmnxPimSnpgIfRxBadChecksumDscrd = _TmnxPimSnpgIfRxBadChecksumDscrd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 2, 5, 1, 6),
    _TmnxPimSnpgIfRxBadChecksumDscrd_Type()
)
tmnxPimSnpgIfRxBadChecksumDscrd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPimSnpgIfRxBadChecksumDscrd.setStatus("current")
_TmnxPimSnpgIfRxBadVersionDscrd_Type = Counter32
_TmnxPimSnpgIfRxBadVersionDscrd_Object = MibTableColumn
tmnxPimSnpgIfRxBadVersionDscrd = _TmnxPimSnpgIfRxBadVersionDscrd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 2, 5, 1, 7),
    _TmnxPimSnpgIfRxBadVersionDscrd_Type()
)
tmnxPimSnpgIfRxBadVersionDscrd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPimSnpgIfRxBadVersionDscrd.setStatus("current")
_TmnxPimSnpgIfRxBadEncodings_Type = Counter32
_TmnxPimSnpgIfRxBadEncodings_Object = MibTableColumn
tmnxPimSnpgIfRxBadEncodings = _TmnxPimSnpgIfRxBadEncodings_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 2, 5, 1, 8),
    _TmnxPimSnpgIfRxBadEncodings_Type()
)
tmnxPimSnpgIfRxBadEncodings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPimSnpgIfRxBadEncodings.setStatus("current")
_TmnxPimSnpgIfStarGTypes_Type = Gauge32
_TmnxPimSnpgIfStarGTypes_Object = MibTableColumn
tmnxPimSnpgIfStarGTypes = _TmnxPimSnpgIfStarGTypes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 2, 5, 1, 9),
    _TmnxPimSnpgIfStarGTypes_Type()
)
tmnxPimSnpgIfStarGTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPimSnpgIfStarGTypes.setStatus("current")
_TmnxPimSnpgIfSGTypes_Type = Gauge32
_TmnxPimSnpgIfSGTypes_Object = MibTableColumn
tmnxPimSnpgIfSGTypes = _TmnxPimSnpgIfSGTypes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 2, 5, 1, 10),
    _TmnxPimSnpgIfSGTypes_Type()
)
tmnxPimSnpgIfSGTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPimSnpgIfSGTypes.setStatus("current")
_TmnxPimSnpgIfJoinPolicyDrops_Type = Counter32
_TmnxPimSnpgIfJoinPolicyDrops_Object = MibTableColumn
tmnxPimSnpgIfJoinPolicyDrops = _TmnxPimSnpgIfJoinPolicyDrops_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 2, 5, 1, 11),
    _TmnxPimSnpgIfJoinPolicyDrops_Type()
)
tmnxPimSnpgIfJoinPolicyDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPimSnpgIfJoinPolicyDrops.setStatus("current")
_TmnxPimSnpgIfTxJoinPrunes_Type = Counter32
_TmnxPimSnpgIfTxJoinPrunes_Object = MibTableColumn
tmnxPimSnpgIfTxJoinPrunes = _TmnxPimSnpgIfTxJoinPrunes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 2, 5, 1, 12),
    _TmnxPimSnpgIfTxJoinPrunes_Type()
)
tmnxPimSnpgIfTxJoinPrunes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPimSnpgIfTxJoinPrunes.setStatus("current")
_TmnxPimSnpgIfRxJoinPrunes_Type = Counter32
_TmnxPimSnpgIfRxJoinPrunes_Object = MibTableColumn
tmnxPimSnpgIfRxJoinPrunes = _TmnxPimSnpgIfRxJoinPrunes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 2, 5, 1, 13),
    _TmnxPimSnpgIfRxJoinPrunes_Type()
)
tmnxPimSnpgIfRxJoinPrunes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPimSnpgIfRxJoinPrunes.setStatus("current")
_TmnxPimSnpgIfRxJoinPruneErrs_Type = Counter32
_TmnxPimSnpgIfRxJoinPruneErrs_Object = MibTableColumn
tmnxPimSnpgIfRxJoinPruneErrs = _TmnxPimSnpgIfRxJoinPruneErrs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 2, 5, 1, 14),
    _TmnxPimSnpgIfRxJoinPruneErrs_Type()
)
tmnxPimSnpgIfRxJoinPruneErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPimSnpgIfRxJoinPruneErrs.setStatus("current")
_TmnxPimSnpgIfSecNbrTblLstChanged_Type = TimeStamp
_TmnxPimSnpgIfSecNbrTblLstChanged_Object = MibScalar
tmnxPimSnpgIfSecNbrTblLstChanged = _TmnxPimSnpgIfSecNbrTblLstChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 2, 6),
    _TmnxPimSnpgIfSecNbrTblLstChanged_Type()
)
tmnxPimSnpgIfSecNbrTblLstChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPimSnpgIfSecNbrTblLstChanged.setStatus("current")
_TmnxPimSnpgIfSecNbrTable_Object = MibTable
tmnxPimSnpgIfSecNbrTable = _TmnxPimSnpgIfSecNbrTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 2, 7)
)
if mibBuilder.loadTexts:
    tmnxPimSnpgIfSecNbrTable.setStatus("current")
_TmnxPimSnpgIfSecNbrEntry_Object = MibTableRow
tmnxPimSnpgIfSecNbrEntry = _TmnxPimSnpgIfSecNbrEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 2, 7, 1)
)
tmnxPimSnpgIfSecNbrEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-PIM-SNOOPING-MIB", "tmnxPimSnpgPortId"),
    (0, "TIMETRA-PIM-SNOOPING-MIB", "tmnxPimSnpgEncapValue"),
    (0, "TIMETRA-PIM-SNOOPING-MIB", "tmnxPimSnpgIfNbrAddrType"),
    (0, "TIMETRA-PIM-SNOOPING-MIB", "tmnxPimSnpgIfNbrAddress"),
    (0, "TIMETRA-PIM-SNOOPING-MIB", "tmnxPimSnpgIfSecNbrAddrType"),
    (0, "TIMETRA-PIM-SNOOPING-MIB", "tmnxPimSnpgIfSecNbrAddress"),
)
if mibBuilder.loadTexts:
    tmnxPimSnpgIfSecNbrEntry.setStatus("current")
_TmnxPimSnpgIfSecNbrAddrType_Type = InetAddressType
_TmnxPimSnpgIfSecNbrAddrType_Object = MibTableColumn
tmnxPimSnpgIfSecNbrAddrType = _TmnxPimSnpgIfSecNbrAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 2, 7, 1, 1),
    _TmnxPimSnpgIfSecNbrAddrType_Type()
)
tmnxPimSnpgIfSecNbrAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPimSnpgIfSecNbrAddrType.setStatus("current")


class _TmnxPimSnpgIfSecNbrAddress_Type(InetAddress):
    """Custom type tmnxPimSnpgIfSecNbrAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxPimSnpgIfSecNbrAddress_Type.__name__ = "InetAddress"
_TmnxPimSnpgIfSecNbrAddress_Object = MibTableColumn
tmnxPimSnpgIfSecNbrAddress = _TmnxPimSnpgIfSecNbrAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 2, 7, 1, 2),
    _TmnxPimSnpgIfSecNbrAddress_Type()
)
tmnxPimSnpgIfSecNbrAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPimSnpgIfSecNbrAddress.setStatus("current")
_TmnxPimSnpgNotificationObjs_ObjectIdentity = ObjectIdentity
tmnxPimSnpgNotificationObjs = _TmnxPimSnpgNotificationObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 3)
)
_TmnxPimSnpgVxlanIfObjs_ObjectIdentity = ObjectIdentity
tmnxPimSnpgVxlanIfObjs = _TmnxPimSnpgVxlanIfObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 4)
)
_VxlanPimSnpgIfTable_Object = MibTable
vxlanPimSnpgIfTable = _VxlanPimSnpgIfTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 4, 1)
)
if mibBuilder.loadTexts:
    vxlanPimSnpgIfTable.setStatus("current")
_VxlanPimSnpgIfEntry_Object = MibTableRow
vxlanPimSnpgIfEntry = _VxlanPimSnpgIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 4, 1, 1)
)
vxlanPimSnpgIfEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "ALCATEL-IGMP-SNOOPING-MIB", "vxlanVTEPAddr"),
    (0, "ALCATEL-IGMP-SNOOPING-MIB", "vxlanVNI"),
    (0, "TIMETRA-PIM-NG-MIB", "vRtrPimNgAFGenAFType"),
)
if mibBuilder.loadTexts:
    vxlanPimSnpgIfEntry.setStatus("current")
_VxlanPimSnpgIfLastChangeTime_Type = TimeStamp
_VxlanPimSnpgIfLastChangeTime_Object = MibTableColumn
vxlanPimSnpgIfLastChangeTime = _VxlanPimSnpgIfLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 4, 1, 1, 1),
    _VxlanPimSnpgIfLastChangeTime_Type()
)
vxlanPimSnpgIfLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vxlanPimSnpgIfLastChangeTime.setStatus("current")
_VxlanPimSnpgIfOperState_Type = ServiceOperStatus
_VxlanPimSnpgIfOperState_Object = MibTableColumn
vxlanPimSnpgIfOperState = _VxlanPimSnpgIfOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 4, 1, 1, 2),
    _VxlanPimSnpgIfOperState_Type()
)
vxlanPimSnpgIfOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vxlanPimSnpgIfOperState.setStatus("current")
_VxlanPimSnpgIfUpTime_Type = Unsigned32
_VxlanPimSnpgIfUpTime_Object = MibTableColumn
vxlanPimSnpgIfUpTime = _VxlanPimSnpgIfUpTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 4, 1, 1, 3),
    _VxlanPimSnpgIfUpTime_Type()
)
vxlanPimSnpgIfUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vxlanPimSnpgIfUpTime.setStatus("current")
if mibBuilder.loadTexts:
    vxlanPimSnpgIfUpTime.setUnits("seconds")
_VxlanPimSnpgIfCurrentGroups_Type = Gauge32
_VxlanPimSnpgIfCurrentGroups_Object = MibTableColumn
vxlanPimSnpgIfCurrentGroups = _VxlanPimSnpgIfCurrentGroups_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 4, 1, 1, 4),
    _VxlanPimSnpgIfCurrentGroups_Type()
)
vxlanPimSnpgIfCurrentGroups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vxlanPimSnpgIfCurrentGroups.setStatus("current")
_VxlanPimSnpgIfMaxGroupsTillNow_Type = Counter32
_VxlanPimSnpgIfMaxGroupsTillNow_Object = MibTableColumn
vxlanPimSnpgIfMaxGroupsTillNow = _VxlanPimSnpgIfMaxGroupsTillNow_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 4, 1, 1, 5),
    _VxlanPimSnpgIfMaxGroupsTillNow_Type()
)
vxlanPimSnpgIfMaxGroupsTillNow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vxlanPimSnpgIfMaxGroupsTillNow.setStatus("current")


class _VxlanPimSnpgIfPwFwding_Type(TruthValue):
    """Custom type vxlanPimSnpgIfPwFwding based on TruthValue"""
    defaultValue = 1


_VxlanPimSnpgIfPwFwding_Type.__name__ = "TruthValue"
_VxlanPimSnpgIfPwFwding_Object = MibTableColumn
vxlanPimSnpgIfPwFwding = _VxlanPimSnpgIfPwFwding_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 4, 1, 1, 6),
    _VxlanPimSnpgIfPwFwding_Type()
)
vxlanPimSnpgIfPwFwding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vxlanPimSnpgIfPwFwding.setStatus("current")
_VxlanPimSnpgIfStatsTable_Object = MibTable
vxlanPimSnpgIfStatsTable = _VxlanPimSnpgIfStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 4, 2)
)
if mibBuilder.loadTexts:
    vxlanPimSnpgIfStatsTable.setStatus("current")
_VxlanPimSnpgIfStatsEntry_Object = MibTableRow
vxlanPimSnpgIfStatsEntry = _VxlanPimSnpgIfStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 4, 2, 1)
)
if mibBuilder.loadTexts:
    vxlanPimSnpgIfStatsEntry.setStatus("current")
_VxlanPimSnpgIfTxPkts_Type = Counter32
_VxlanPimSnpgIfTxPkts_Object = MibTableColumn
vxlanPimSnpgIfTxPkts = _VxlanPimSnpgIfTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 4, 2, 1, 1),
    _VxlanPimSnpgIfTxPkts_Type()
)
vxlanPimSnpgIfTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vxlanPimSnpgIfTxPkts.setStatus("current")
_VxlanPimSnpgIfRxPkts_Type = Counter32
_VxlanPimSnpgIfRxPkts_Object = MibTableColumn
vxlanPimSnpgIfRxPkts = _VxlanPimSnpgIfRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 4, 2, 1, 2),
    _VxlanPimSnpgIfRxPkts_Type()
)
vxlanPimSnpgIfRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vxlanPimSnpgIfRxPkts.setStatus("current")
_VxlanPimSnpgIfRxHellos_Type = Counter32
_VxlanPimSnpgIfRxHellos_Object = MibTableColumn
vxlanPimSnpgIfRxHellos = _VxlanPimSnpgIfRxHellos_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 4, 2, 1, 3),
    _VxlanPimSnpgIfRxHellos_Type()
)
vxlanPimSnpgIfRxHellos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vxlanPimSnpgIfRxHellos.setStatus("current")
_VxlanPimSnpgIfRxHellosDropped_Type = Counter32
_VxlanPimSnpgIfRxHellosDropped_Object = MibTableColumn
vxlanPimSnpgIfRxHellosDropped = _VxlanPimSnpgIfRxHellosDropped_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 4, 2, 1, 4),
    _VxlanPimSnpgIfRxHellosDropped_Type()
)
vxlanPimSnpgIfRxHellosDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vxlanPimSnpgIfRxHellosDropped.setStatus("current")
_VxlanPimSnpgIfRxNbrUnknown_Type = Counter32
_VxlanPimSnpgIfRxNbrUnknown_Object = MibTableColumn
vxlanPimSnpgIfRxNbrUnknown = _VxlanPimSnpgIfRxNbrUnknown_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 4, 2, 1, 5),
    _VxlanPimSnpgIfRxNbrUnknown_Type()
)
vxlanPimSnpgIfRxNbrUnknown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vxlanPimSnpgIfRxNbrUnknown.setStatus("current")
_VxlanPimSnpgIfRxBadChecksumDscrd_Type = Counter32
_VxlanPimSnpgIfRxBadChecksumDscrd_Object = MibTableColumn
vxlanPimSnpgIfRxBadChecksumDscrd = _VxlanPimSnpgIfRxBadChecksumDscrd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 4, 2, 1, 6),
    _VxlanPimSnpgIfRxBadChecksumDscrd_Type()
)
vxlanPimSnpgIfRxBadChecksumDscrd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vxlanPimSnpgIfRxBadChecksumDscrd.setStatus("current")
_VxlanPimSnpgIfRxBadVersionDscrd_Type = Counter32
_VxlanPimSnpgIfRxBadVersionDscrd_Object = MibTableColumn
vxlanPimSnpgIfRxBadVersionDscrd = _VxlanPimSnpgIfRxBadVersionDscrd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 4, 2, 1, 7),
    _VxlanPimSnpgIfRxBadVersionDscrd_Type()
)
vxlanPimSnpgIfRxBadVersionDscrd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vxlanPimSnpgIfRxBadVersionDscrd.setStatus("current")
_VxlanPimSnpgIfRxBadEncodings_Type = Counter32
_VxlanPimSnpgIfRxBadEncodings_Object = MibTableColumn
vxlanPimSnpgIfRxBadEncodings = _VxlanPimSnpgIfRxBadEncodings_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 4, 2, 1, 8),
    _VxlanPimSnpgIfRxBadEncodings_Type()
)
vxlanPimSnpgIfRxBadEncodings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vxlanPimSnpgIfRxBadEncodings.setStatus("current")
_VxlanPimSnpgIfStarGTypes_Type = Gauge32
_VxlanPimSnpgIfStarGTypes_Object = MibTableColumn
vxlanPimSnpgIfStarGTypes = _VxlanPimSnpgIfStarGTypes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 4, 2, 1, 9),
    _VxlanPimSnpgIfStarGTypes_Type()
)
vxlanPimSnpgIfStarGTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vxlanPimSnpgIfStarGTypes.setStatus("current")
_VxlanPimSnpgIfSGTypes_Type = Gauge32
_VxlanPimSnpgIfSGTypes_Object = MibTableColumn
vxlanPimSnpgIfSGTypes = _VxlanPimSnpgIfSGTypes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 4, 2, 1, 10),
    _VxlanPimSnpgIfSGTypes_Type()
)
vxlanPimSnpgIfSGTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vxlanPimSnpgIfSGTypes.setStatus("current")
_VxlanPimSnpgIfJoinPolicyDrops_Type = Counter32
_VxlanPimSnpgIfJoinPolicyDrops_Object = MibTableColumn
vxlanPimSnpgIfJoinPolicyDrops = _VxlanPimSnpgIfJoinPolicyDrops_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 4, 2, 1, 11),
    _VxlanPimSnpgIfJoinPolicyDrops_Type()
)
vxlanPimSnpgIfJoinPolicyDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vxlanPimSnpgIfJoinPolicyDrops.setStatus("current")
_VxlanPimSnpgIfTxJoinPrunes_Type = Counter32
_VxlanPimSnpgIfTxJoinPrunes_Object = MibTableColumn
vxlanPimSnpgIfTxJoinPrunes = _VxlanPimSnpgIfTxJoinPrunes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 4, 2, 1, 12),
    _VxlanPimSnpgIfTxJoinPrunes_Type()
)
vxlanPimSnpgIfTxJoinPrunes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vxlanPimSnpgIfTxJoinPrunes.setStatus("current")
_VxlanPimSnpgIfRxJoinPrunes_Type = Counter32
_VxlanPimSnpgIfRxJoinPrunes_Object = MibTableColumn
vxlanPimSnpgIfRxJoinPrunes = _VxlanPimSnpgIfRxJoinPrunes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 4, 2, 1, 13),
    _VxlanPimSnpgIfRxJoinPrunes_Type()
)
vxlanPimSnpgIfRxJoinPrunes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vxlanPimSnpgIfRxJoinPrunes.setStatus("current")
_VxlanPimSnpgIfRxJoinPruneErrs_Type = Counter32
_VxlanPimSnpgIfRxJoinPruneErrs_Object = MibTableColumn
vxlanPimSnpgIfRxJoinPruneErrs = _VxlanPimSnpgIfRxJoinPruneErrs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 4, 2, 1, 14),
    _VxlanPimSnpgIfRxJoinPruneErrs_Type()
)
vxlanPimSnpgIfRxJoinPruneErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vxlanPimSnpgIfRxJoinPruneErrs.setStatus("current")
_VxlanPimSnpgIfNbrTable_Object = MibTable
vxlanPimSnpgIfNbrTable = _VxlanPimSnpgIfNbrTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 4, 3)
)
if mibBuilder.loadTexts:
    vxlanPimSnpgIfNbrTable.setStatus("current")
_VxlanPimSnpgIfNbrEntry_Object = MibTableRow
vxlanPimSnpgIfNbrEntry = _VxlanPimSnpgIfNbrEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 4, 3, 1)
)
vxlanPimSnpgIfNbrEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "ALCATEL-IGMP-SNOOPING-MIB", "vxlanVTEPAddr"),
    (0, "ALCATEL-IGMP-SNOOPING-MIB", "vxlanVNI"),
    (0, "TIMETRA-PIM-SNOOPING-MIB", "vxlanPimSnpgIfNbrAddrType"),
    (0, "TIMETRA-PIM-SNOOPING-MIB", "vxlanPimSnpgIfNbrAddress"),
)
if mibBuilder.loadTexts:
    vxlanPimSnpgIfNbrEntry.setStatus("current")
_VxlanPimSnpgIfNbrAddrType_Type = InetAddressType
_VxlanPimSnpgIfNbrAddrType_Object = MibTableColumn
vxlanPimSnpgIfNbrAddrType = _VxlanPimSnpgIfNbrAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 4, 3, 1, 1),
    _VxlanPimSnpgIfNbrAddrType_Type()
)
vxlanPimSnpgIfNbrAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vxlanPimSnpgIfNbrAddrType.setStatus("current")


class _VxlanPimSnpgIfNbrAddress_Type(InetAddress):
    """Custom type vxlanPimSnpgIfNbrAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_VxlanPimSnpgIfNbrAddress_Type.__name__ = "InetAddress"
_VxlanPimSnpgIfNbrAddress_Object = MibTableColumn
vxlanPimSnpgIfNbrAddress = _VxlanPimSnpgIfNbrAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 4, 3, 1, 2),
    _VxlanPimSnpgIfNbrAddress_Type()
)
vxlanPimSnpgIfNbrAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vxlanPimSnpgIfNbrAddress.setStatus("current")
_VxlanPimSnpgIfNbrUpTime_Type = Unsigned32
_VxlanPimSnpgIfNbrUpTime_Object = MibTableColumn
vxlanPimSnpgIfNbrUpTime = _VxlanPimSnpgIfNbrUpTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 4, 3, 1, 3),
    _VxlanPimSnpgIfNbrUpTime_Type()
)
vxlanPimSnpgIfNbrUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vxlanPimSnpgIfNbrUpTime.setStatus("current")
if mibBuilder.loadTexts:
    vxlanPimSnpgIfNbrUpTime.setUnits("seconds")
_VxlanPimSnpgIfNbrExpiryTime_Type = Unsigned32
_VxlanPimSnpgIfNbrExpiryTime_Object = MibTableColumn
vxlanPimSnpgIfNbrExpiryTime = _VxlanPimSnpgIfNbrExpiryTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 4, 3, 1, 4),
    _VxlanPimSnpgIfNbrExpiryTime_Type()
)
vxlanPimSnpgIfNbrExpiryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vxlanPimSnpgIfNbrExpiryTime.setStatus("current")
if mibBuilder.loadTexts:
    vxlanPimSnpgIfNbrExpiryTime.setUnits("seconds")
_VxlanPimSnpgIfNbrGenId_Type = Unsigned32
_VxlanPimSnpgIfNbrGenId_Object = MibTableColumn
vxlanPimSnpgIfNbrGenId = _VxlanPimSnpgIfNbrGenId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 4, 3, 1, 5),
    _VxlanPimSnpgIfNbrGenId_Type()
)
vxlanPimSnpgIfNbrGenId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vxlanPimSnpgIfNbrGenId.setStatus("current")
_VxlanPimSnpgIfNbrDrPriority_Type = Unsigned32
_VxlanPimSnpgIfNbrDrPriority_Object = MibTableColumn
vxlanPimSnpgIfNbrDrPriority = _VxlanPimSnpgIfNbrDrPriority_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 4, 3, 1, 6),
    _VxlanPimSnpgIfNbrDrPriority_Type()
)
vxlanPimSnpgIfNbrDrPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vxlanPimSnpgIfNbrDrPriority.setStatus("current")
_VxlanPimSnpgIfNbrDrPriorPresent_Type = TruthValue
_VxlanPimSnpgIfNbrDrPriorPresent_Object = MibTableColumn
vxlanPimSnpgIfNbrDrPriorPresent = _VxlanPimSnpgIfNbrDrPriorPresent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 4, 3, 1, 7),
    _VxlanPimSnpgIfNbrDrPriorPresent_Type()
)
vxlanPimSnpgIfNbrDrPriorPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vxlanPimSnpgIfNbrDrPriorPresent.setStatus("current")
_VxlanPimSnpgIfNbrLanDelay_Type = Unsigned32
_VxlanPimSnpgIfNbrLanDelay_Object = MibTableColumn
vxlanPimSnpgIfNbrLanDelay = _VxlanPimSnpgIfNbrLanDelay_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 4, 3, 1, 8),
    _VxlanPimSnpgIfNbrLanDelay_Type()
)
vxlanPimSnpgIfNbrLanDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vxlanPimSnpgIfNbrLanDelay.setStatus("current")
if mibBuilder.loadTexts:
    vxlanPimSnpgIfNbrLanDelay.setUnits("milliseconds")
_VxlanPimSnpgIfNbrLanDlayPrsnt_Type = TruthValue
_VxlanPimSnpgIfNbrLanDlayPrsnt_Object = MibTableColumn
vxlanPimSnpgIfNbrLanDlayPrsnt = _VxlanPimSnpgIfNbrLanDlayPrsnt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 4, 3, 1, 9),
    _VxlanPimSnpgIfNbrLanDlayPrsnt_Type()
)
vxlanPimSnpgIfNbrLanDlayPrsnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vxlanPimSnpgIfNbrLanDlayPrsnt.setStatus("current")
_VxlanPimSnpgIfNbrTrckngSpprt_Type = TruthValue
_VxlanPimSnpgIfNbrTrckngSpprt_Object = MibTableColumn
vxlanPimSnpgIfNbrTrckngSpprt = _VxlanPimSnpgIfNbrTrckngSpprt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 4, 3, 1, 10),
    _VxlanPimSnpgIfNbrTrckngSpprt_Type()
)
vxlanPimSnpgIfNbrTrckngSpprt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vxlanPimSnpgIfNbrTrckngSpprt.setStatus("current")
_VxlanPimSnpgIfNbrHoldTime_Type = Unsigned32
_VxlanPimSnpgIfNbrHoldTime_Object = MibTableColumn
vxlanPimSnpgIfNbrHoldTime = _VxlanPimSnpgIfNbrHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 4, 3, 1, 11),
    _VxlanPimSnpgIfNbrHoldTime_Type()
)
vxlanPimSnpgIfNbrHoldTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vxlanPimSnpgIfNbrHoldTime.setStatus("current")
if mibBuilder.loadTexts:
    vxlanPimSnpgIfNbrHoldTime.setUnits("seconds")
_VxlanPimSnpgIfNbrOvrdeIntrvl_Type = Unsigned32
_VxlanPimSnpgIfNbrOvrdeIntrvl_Object = MibTableColumn
vxlanPimSnpgIfNbrOvrdeIntrvl = _VxlanPimSnpgIfNbrOvrdeIntrvl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 4, 3, 1, 12),
    _VxlanPimSnpgIfNbrOvrdeIntrvl_Type()
)
vxlanPimSnpgIfNbrOvrdeIntrvl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vxlanPimSnpgIfNbrOvrdeIntrvl.setStatus("current")
if mibBuilder.loadTexts:
    vxlanPimSnpgIfNbrOvrdeIntrvl.setUnits("milliseconds")
_VxlanPimSnpgIfSecNbrTable_Object = MibTable
vxlanPimSnpgIfSecNbrTable = _VxlanPimSnpgIfSecNbrTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 4, 4)
)
if mibBuilder.loadTexts:
    vxlanPimSnpgIfSecNbrTable.setStatus("current")
_VxlanPimSnpgIfSecNbrEntry_Object = MibTableRow
vxlanPimSnpgIfSecNbrEntry = _VxlanPimSnpgIfSecNbrEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 4, 4, 1)
)
vxlanPimSnpgIfSecNbrEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "ALCATEL-IGMP-SNOOPING-MIB", "vxlanVTEPAddr"),
    (0, "ALCATEL-IGMP-SNOOPING-MIB", "vxlanVNI"),
    (0, "TIMETRA-PIM-SNOOPING-MIB", "vxlanPimSnpgIfNbrAddrType"),
    (0, "TIMETRA-PIM-SNOOPING-MIB", "vxlanPimSnpgIfNbrAddress"),
    (0, "TIMETRA-PIM-SNOOPING-MIB", "vxlanPimSnpgIfSecNbrAddrType"),
    (0, "TIMETRA-PIM-SNOOPING-MIB", "vxlanPimSnpgIfSecNbrAddress"),
)
if mibBuilder.loadTexts:
    vxlanPimSnpgIfSecNbrEntry.setStatus("current")
_VxlanPimSnpgIfSecNbrAddrType_Type = InetAddressType
_VxlanPimSnpgIfSecNbrAddrType_Object = MibTableColumn
vxlanPimSnpgIfSecNbrAddrType = _VxlanPimSnpgIfSecNbrAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 4, 4, 1, 1),
    _VxlanPimSnpgIfSecNbrAddrType_Type()
)
vxlanPimSnpgIfSecNbrAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vxlanPimSnpgIfSecNbrAddrType.setStatus("current")


class _VxlanPimSnpgIfSecNbrAddress_Type(InetAddress):
    """Custom type vxlanPimSnpgIfSecNbrAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_VxlanPimSnpgIfSecNbrAddress_Type.__name__ = "InetAddress"
_VxlanPimSnpgIfSecNbrAddress_Object = MibTableColumn
vxlanPimSnpgIfSecNbrAddress = _VxlanPimSnpgIfSecNbrAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 4, 4, 1, 2),
    _VxlanPimSnpgIfSecNbrAddress_Type()
)
vxlanPimSnpgIfSecNbrAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vxlanPimSnpgIfSecNbrAddress.setStatus("current")
_VxlanPimSnpgIfGrpSrcTable_Object = MibTable
vxlanPimSnpgIfGrpSrcTable = _VxlanPimSnpgIfGrpSrcTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 4, 5)
)
if mibBuilder.loadTexts:
    vxlanPimSnpgIfGrpSrcTable.setStatus("current")
_VxlanPimSnpgIfGrpSrcEntry_Object = MibTableRow
vxlanPimSnpgIfGrpSrcEntry = _VxlanPimSnpgIfGrpSrcEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 4, 5, 1)
)
vxlanPimSnpgIfGrpSrcEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "ALCATEL-IGMP-SNOOPING-MIB", "vxlanVTEPAddr"),
    (0, "ALCATEL-IGMP-SNOOPING-MIB", "vxlanVNI"),
    (0, "TIMETRA-PIM-SNOOPING-MIB", "vxlanPimSnpgIfGrpSrcGrpAddrType"),
    (0, "TIMETRA-PIM-SNOOPING-MIB", "vxlanPimSnpgIfGrpSrcGroupAddr"),
    (0, "TIMETRA-PIM-SNOOPING-MIB", "vxlanPimSnpgIfGrpSrcSrcAddrType"),
    (0, "TIMETRA-PIM-SNOOPING-MIB", "vxlanPimSnpgIfGrpSrcSourceAddr"),
)
if mibBuilder.loadTexts:
    vxlanPimSnpgIfGrpSrcEntry.setStatus("current")
_VxlanPimSnpgIfGrpSrcGrpAddrType_Type = InetAddressType
_VxlanPimSnpgIfGrpSrcGrpAddrType_Object = MibTableColumn
vxlanPimSnpgIfGrpSrcGrpAddrType = _VxlanPimSnpgIfGrpSrcGrpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 4, 5, 1, 1),
    _VxlanPimSnpgIfGrpSrcGrpAddrType_Type()
)
vxlanPimSnpgIfGrpSrcGrpAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vxlanPimSnpgIfGrpSrcGrpAddrType.setStatus("current")


class _VxlanPimSnpgIfGrpSrcGroupAddr_Type(InetAddress):
    """Custom type vxlanPimSnpgIfGrpSrcGroupAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_VxlanPimSnpgIfGrpSrcGroupAddr_Type.__name__ = "InetAddress"
_VxlanPimSnpgIfGrpSrcGroupAddr_Object = MibTableColumn
vxlanPimSnpgIfGrpSrcGroupAddr = _VxlanPimSnpgIfGrpSrcGroupAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 4, 5, 1, 2),
    _VxlanPimSnpgIfGrpSrcGroupAddr_Type()
)
vxlanPimSnpgIfGrpSrcGroupAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vxlanPimSnpgIfGrpSrcGroupAddr.setStatus("current")
_VxlanPimSnpgIfGrpSrcSrcAddrType_Type = InetAddressType
_VxlanPimSnpgIfGrpSrcSrcAddrType_Object = MibTableColumn
vxlanPimSnpgIfGrpSrcSrcAddrType = _VxlanPimSnpgIfGrpSrcSrcAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 4, 5, 1, 3),
    _VxlanPimSnpgIfGrpSrcSrcAddrType_Type()
)
vxlanPimSnpgIfGrpSrcSrcAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vxlanPimSnpgIfGrpSrcSrcAddrType.setStatus("current")


class _VxlanPimSnpgIfGrpSrcSourceAddr_Type(InetAddress):
    """Custom type vxlanPimSnpgIfGrpSrcSourceAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_VxlanPimSnpgIfGrpSrcSourceAddr_Type.__name__ = "InetAddress"
_VxlanPimSnpgIfGrpSrcSourceAddr_Object = MibTableColumn
vxlanPimSnpgIfGrpSrcSourceAddr = _VxlanPimSnpgIfGrpSrcSourceAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 4, 5, 1, 4),
    _VxlanPimSnpgIfGrpSrcSourceAddr_Type()
)
vxlanPimSnpgIfGrpSrcSourceAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vxlanPimSnpgIfGrpSrcSourceAddr.setStatus("current")


class _VxlanPimSnpgIfGrpSrcJPState_Type(Integer32):
    """Custom type vxlanPimSnpgIfGrpSrcJPState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noInfo", 0),
          ("join", 1),
          ("prunePend", 2),
          ("pruned", 3))
    )


_VxlanPimSnpgIfGrpSrcJPState_Type.__name__ = "Integer32"
_VxlanPimSnpgIfGrpSrcJPState_Object = MibTableColumn
vxlanPimSnpgIfGrpSrcJPState = _VxlanPimSnpgIfGrpSrcJPState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 4, 5, 1, 5),
    _VxlanPimSnpgIfGrpSrcJPState_Type()
)
vxlanPimSnpgIfGrpSrcJPState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vxlanPimSnpgIfGrpSrcJPState.setStatus("current")
_VxlanPimSnpgIfGrpSrcPrunePendTmr_Type = Unsigned32
_VxlanPimSnpgIfGrpSrcPrunePendTmr_Object = MibTableColumn
vxlanPimSnpgIfGrpSrcPrunePendTmr = _VxlanPimSnpgIfGrpSrcPrunePendTmr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 4, 5, 1, 6),
    _VxlanPimSnpgIfGrpSrcPrunePendTmr_Type()
)
vxlanPimSnpgIfGrpSrcPrunePendTmr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vxlanPimSnpgIfGrpSrcPrunePendTmr.setStatus("current")
if mibBuilder.loadTexts:
    vxlanPimSnpgIfGrpSrcPrunePendTmr.setUnits("seconds")
_VxlanPimSnpgIfGrpSrcJPTimer_Type = Unsigned32
_VxlanPimSnpgIfGrpSrcJPTimer_Object = MibTableColumn
vxlanPimSnpgIfGrpSrcJPTimer = _VxlanPimSnpgIfGrpSrcJPTimer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 4, 5, 1, 7),
    _VxlanPimSnpgIfGrpSrcJPTimer_Type()
)
vxlanPimSnpgIfGrpSrcJPTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vxlanPimSnpgIfGrpSrcJPTimer.setStatus("current")
if mibBuilder.loadTexts:
    vxlanPimSnpgIfGrpSrcJPTimer.setUnits("seconds")


class _VxlanPimSnpgIfGrpSrcJPRptState_Type(Integer32):
    """Custom type vxlanPimSnpgIfGrpSrcJPRptState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noInfo", 0),
          ("join", 1),
          ("prunePend", 2),
          ("pruned", 3))
    )


_VxlanPimSnpgIfGrpSrcJPRptState_Type.__name__ = "Integer32"
_VxlanPimSnpgIfGrpSrcJPRptState_Object = MibTableColumn
vxlanPimSnpgIfGrpSrcJPRptState = _VxlanPimSnpgIfGrpSrcJPRptState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 4, 5, 1, 8),
    _VxlanPimSnpgIfGrpSrcJPRptState_Type()
)
vxlanPimSnpgIfGrpSrcJPRptState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vxlanPimSnpgIfGrpSrcJPRptState.setStatus("current")
_VxlanPimSnpgIfGrpSrcRptPrnPndTmr_Type = Unsigned32
_VxlanPimSnpgIfGrpSrcRptPrnPndTmr_Object = MibTableColumn
vxlanPimSnpgIfGrpSrcRptPrnPndTmr = _VxlanPimSnpgIfGrpSrcRptPrnPndTmr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 4, 5, 1, 9),
    _VxlanPimSnpgIfGrpSrcRptPrnPndTmr_Type()
)
vxlanPimSnpgIfGrpSrcRptPrnPndTmr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vxlanPimSnpgIfGrpSrcRptPrnPndTmr.setStatus("current")
if mibBuilder.loadTexts:
    vxlanPimSnpgIfGrpSrcRptPrnPndTmr.setUnits("seconds")
_VxlanPimSnpgIfGrpSrcRptJPTimer_Type = Unsigned32
_VxlanPimSnpgIfGrpSrcRptJPTimer_Object = MibTableColumn
vxlanPimSnpgIfGrpSrcRptJPTimer = _VxlanPimSnpgIfGrpSrcRptJPTimer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 4, 5, 1, 10),
    _VxlanPimSnpgIfGrpSrcRptJPTimer_Type()
)
vxlanPimSnpgIfGrpSrcRptJPTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vxlanPimSnpgIfGrpSrcRptJPTimer.setStatus("current")
if mibBuilder.loadTexts:
    vxlanPimSnpgIfGrpSrcRptJPTimer.setUnits("seconds")
_VxlanPimSnpgIfGrpSrcUpTime_Type = Unsigned32
_VxlanPimSnpgIfGrpSrcUpTime_Object = MibTableColumn
vxlanPimSnpgIfGrpSrcUpTime = _VxlanPimSnpgIfGrpSrcUpTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 4, 5, 1, 11),
    _VxlanPimSnpgIfGrpSrcUpTime_Type()
)
vxlanPimSnpgIfGrpSrcUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vxlanPimSnpgIfGrpSrcUpTime.setStatus("current")
if mibBuilder.loadTexts:
    vxlanPimSnpgIfGrpSrcUpTime.setUnits("seconds")
_VxlanPimSnpgGrpSrcIfTable_Object = MibTable
vxlanPimSnpgGrpSrcIfTable = _VxlanPimSnpgGrpSrcIfTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 4, 6)
)
if mibBuilder.loadTexts:
    vxlanPimSnpgGrpSrcIfTable.setStatus("current")
_VxlanPimSnpgGrpSrcIfEntry_Object = MibTableRow
vxlanPimSnpgGrpSrcIfEntry = _VxlanPimSnpgGrpSrcIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 4, 6, 1)
)
vxlanPimSnpgGrpSrcIfEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-PIM-SNOOPING-MIB", "vxlanPimSnpgGrpSrcGrpAddrType"),
    (0, "TIMETRA-PIM-SNOOPING-MIB", "vxlanPimSnpgGrpSrcGroupAddress"),
    (0, "TIMETRA-PIM-SNOOPING-MIB", "vxlanPimSnpgGrpSrcSrcAddrType"),
    (0, "TIMETRA-PIM-SNOOPING-MIB", "vxlanPimSnpgGrpSrcSourceAddress"),
    (0, "ALCATEL-IGMP-SNOOPING-MIB", "vxlanVTEPAddr"),
    (0, "ALCATEL-IGMP-SNOOPING-MIB", "vxlanVNI"),
)
if mibBuilder.loadTexts:
    vxlanPimSnpgGrpSrcIfEntry.setStatus("current")
_VxlanPimSnpgGrpSrcGrpAddrType_Type = InetAddressType
_VxlanPimSnpgGrpSrcGrpAddrType_Object = MibTableColumn
vxlanPimSnpgGrpSrcGrpAddrType = _VxlanPimSnpgGrpSrcGrpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 4, 6, 1, 1),
    _VxlanPimSnpgGrpSrcGrpAddrType_Type()
)
vxlanPimSnpgGrpSrcGrpAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vxlanPimSnpgGrpSrcGrpAddrType.setStatus("current")


class _VxlanPimSnpgGrpSrcGroupAddress_Type(InetAddress):
    """Custom type vxlanPimSnpgGrpSrcGroupAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_VxlanPimSnpgGrpSrcGroupAddress_Type.__name__ = "InetAddress"
_VxlanPimSnpgGrpSrcGroupAddress_Object = MibTableColumn
vxlanPimSnpgGrpSrcGroupAddress = _VxlanPimSnpgGrpSrcGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 4, 6, 1, 2),
    _VxlanPimSnpgGrpSrcGroupAddress_Type()
)
vxlanPimSnpgGrpSrcGroupAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vxlanPimSnpgGrpSrcGroupAddress.setStatus("current")
_VxlanPimSnpgGrpSrcSrcAddrType_Type = InetAddressType
_VxlanPimSnpgGrpSrcSrcAddrType_Object = MibTableColumn
vxlanPimSnpgGrpSrcSrcAddrType = _VxlanPimSnpgGrpSrcSrcAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 4, 6, 1, 3),
    _VxlanPimSnpgGrpSrcSrcAddrType_Type()
)
vxlanPimSnpgGrpSrcSrcAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vxlanPimSnpgGrpSrcSrcAddrType.setStatus("current")


class _VxlanPimSnpgGrpSrcSourceAddress_Type(InetAddress):
    """Custom type vxlanPimSnpgGrpSrcSourceAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_VxlanPimSnpgGrpSrcSourceAddress_Type.__name__ = "InetAddress"
_VxlanPimSnpgGrpSrcSourceAddress_Object = MibTableColumn
vxlanPimSnpgGrpSrcSourceAddress = _VxlanPimSnpgGrpSrcSourceAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 4, 6, 1, 4),
    _VxlanPimSnpgGrpSrcSourceAddress_Type()
)
vxlanPimSnpgGrpSrcSourceAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vxlanPimSnpgGrpSrcSourceAddress.setStatus("current")


class _VxlanPimSnpgGrpSrcIfFlags_Type(Bits):
    """Custom type vxlanPimSnpgGrpSrcIfFlags based on Bits"""
    namedValues = NamedValues(
        *(("immediateOifList", 0),
          ("inheritedOifList", 1),
          ("inheritedRptOifList", 2),
          ("joined", 3),
          ("rpfPort", 4))
    )

_VxlanPimSnpgGrpSrcIfFlags_Type.__name__ = "Bits"
_VxlanPimSnpgGrpSrcIfFlags_Object = MibTableColumn
vxlanPimSnpgGrpSrcIfFlags = _VxlanPimSnpgGrpSrcIfFlags_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 4, 6, 1, 5),
    _VxlanPimSnpgGrpSrcIfFlags_Type()
)
vxlanPimSnpgGrpSrcIfFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vxlanPimSnpgGrpSrcIfFlags.setStatus("current")
_TmnxPimSnpgEMplsIfObjs_ObjectIdentity = ObjectIdentity
tmnxPimSnpgEMplsIfObjs = _TmnxPimSnpgEMplsIfObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 5)
)
_EMplsPimSnpgIfTable_Object = MibTable
eMplsPimSnpgIfTable = _EMplsPimSnpgIfTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 5, 1)
)
if mibBuilder.loadTexts:
    eMplsPimSnpgIfTable.setStatus("current")
_EMplsPimSnpgIfEntry_Object = MibTableRow
eMplsPimSnpgIfEntry = _EMplsPimSnpgIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 5, 1, 1)
)
eMplsPimSnpgIfEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-PIM-NG-MIB", "vRtrPimNgAFGenAFType"),
)
if mibBuilder.loadTexts:
    eMplsPimSnpgIfEntry.setStatus("current")
_EMplsPimSnpgIfLastChangeTime_Type = TimeStamp
_EMplsPimSnpgIfLastChangeTime_Object = MibTableColumn
eMplsPimSnpgIfLastChangeTime = _EMplsPimSnpgIfLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 5, 1, 1, 1),
    _EMplsPimSnpgIfLastChangeTime_Type()
)
eMplsPimSnpgIfLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eMplsPimSnpgIfLastChangeTime.setStatus("current")
_EMplsPimSnpgIfOperState_Type = ServiceOperStatus
_EMplsPimSnpgIfOperState_Object = MibTableColumn
eMplsPimSnpgIfOperState = _EMplsPimSnpgIfOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 5, 1, 1, 2),
    _EMplsPimSnpgIfOperState_Type()
)
eMplsPimSnpgIfOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eMplsPimSnpgIfOperState.setStatus("current")
_EMplsPimSnpgIfUpTime_Type = Unsigned32
_EMplsPimSnpgIfUpTime_Object = MibTableColumn
eMplsPimSnpgIfUpTime = _EMplsPimSnpgIfUpTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 5, 1, 1, 3),
    _EMplsPimSnpgIfUpTime_Type()
)
eMplsPimSnpgIfUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eMplsPimSnpgIfUpTime.setStatus("current")
if mibBuilder.loadTexts:
    eMplsPimSnpgIfUpTime.setUnits("seconds")
_EMplsPimSnpgIfCurrentGroups_Type = Gauge32
_EMplsPimSnpgIfCurrentGroups_Object = MibTableColumn
eMplsPimSnpgIfCurrentGroups = _EMplsPimSnpgIfCurrentGroups_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 5, 1, 1, 4),
    _EMplsPimSnpgIfCurrentGroups_Type()
)
eMplsPimSnpgIfCurrentGroups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eMplsPimSnpgIfCurrentGroups.setStatus("current")
_EMplsPimSnpgIfMaxGroupsTillNow_Type = Counter32
_EMplsPimSnpgIfMaxGroupsTillNow_Object = MibTableColumn
eMplsPimSnpgIfMaxGroupsTillNow = _EMplsPimSnpgIfMaxGroupsTillNow_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 5, 1, 1, 5),
    _EMplsPimSnpgIfMaxGroupsTillNow_Type()
)
eMplsPimSnpgIfMaxGroupsTillNow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eMplsPimSnpgIfMaxGroupsTillNow.setStatus("current")


class _EMplsPimSnpgIfPwFwding_Type(TruthValue):
    """Custom type eMplsPimSnpgIfPwFwding based on TruthValue"""
    defaultValue = 1


_EMplsPimSnpgIfPwFwding_Type.__name__ = "TruthValue"
_EMplsPimSnpgIfPwFwding_Object = MibTableColumn
eMplsPimSnpgIfPwFwding = _EMplsPimSnpgIfPwFwding_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 5, 1, 1, 6),
    _EMplsPimSnpgIfPwFwding_Type()
)
eMplsPimSnpgIfPwFwding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eMplsPimSnpgIfPwFwding.setStatus("current")
_EMplsPimSnpgIfStatsTable_Object = MibTable
eMplsPimSnpgIfStatsTable = _EMplsPimSnpgIfStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 5, 2)
)
if mibBuilder.loadTexts:
    eMplsPimSnpgIfStatsTable.setStatus("current")
_EMplsPimSnpgIfStatsEntry_Object = MibTableRow
eMplsPimSnpgIfStatsEntry = _EMplsPimSnpgIfStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 5, 2, 1)
)
if mibBuilder.loadTexts:
    eMplsPimSnpgIfStatsEntry.setStatus("current")
_EMplsPimSnpgIfTxPkts_Type = Counter32
_EMplsPimSnpgIfTxPkts_Object = MibTableColumn
eMplsPimSnpgIfTxPkts = _EMplsPimSnpgIfTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 5, 2, 1, 1),
    _EMplsPimSnpgIfTxPkts_Type()
)
eMplsPimSnpgIfTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eMplsPimSnpgIfTxPkts.setStatus("current")
_EMplsPimSnpgIfRxPkts_Type = Counter32
_EMplsPimSnpgIfRxPkts_Object = MibTableColumn
eMplsPimSnpgIfRxPkts = _EMplsPimSnpgIfRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 5, 2, 1, 2),
    _EMplsPimSnpgIfRxPkts_Type()
)
eMplsPimSnpgIfRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eMplsPimSnpgIfRxPkts.setStatus("current")
_EMplsPimSnpgIfRxHellos_Type = Counter32
_EMplsPimSnpgIfRxHellos_Object = MibTableColumn
eMplsPimSnpgIfRxHellos = _EMplsPimSnpgIfRxHellos_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 5, 2, 1, 3),
    _EMplsPimSnpgIfRxHellos_Type()
)
eMplsPimSnpgIfRxHellos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eMplsPimSnpgIfRxHellos.setStatus("current")
_EMplsPimSnpgIfRxHellosDropped_Type = Counter32
_EMplsPimSnpgIfRxHellosDropped_Object = MibTableColumn
eMplsPimSnpgIfRxHellosDropped = _EMplsPimSnpgIfRxHellosDropped_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 5, 2, 1, 4),
    _EMplsPimSnpgIfRxHellosDropped_Type()
)
eMplsPimSnpgIfRxHellosDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eMplsPimSnpgIfRxHellosDropped.setStatus("current")
_EMplsPimSnpgIfRxNbrUnknown_Type = Counter32
_EMplsPimSnpgIfRxNbrUnknown_Object = MibTableColumn
eMplsPimSnpgIfRxNbrUnknown = _EMplsPimSnpgIfRxNbrUnknown_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 5, 2, 1, 5),
    _EMplsPimSnpgIfRxNbrUnknown_Type()
)
eMplsPimSnpgIfRxNbrUnknown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eMplsPimSnpgIfRxNbrUnknown.setStatus("current")
_EMplsPimSnpgIfRxBadChecksumDscrd_Type = Counter32
_EMplsPimSnpgIfRxBadChecksumDscrd_Object = MibTableColumn
eMplsPimSnpgIfRxBadChecksumDscrd = _EMplsPimSnpgIfRxBadChecksumDscrd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 5, 2, 1, 6),
    _EMplsPimSnpgIfRxBadChecksumDscrd_Type()
)
eMplsPimSnpgIfRxBadChecksumDscrd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eMplsPimSnpgIfRxBadChecksumDscrd.setStatus("current")
_EMplsPimSnpgIfRxBadVersionDscrd_Type = Counter32
_EMplsPimSnpgIfRxBadVersionDscrd_Object = MibTableColumn
eMplsPimSnpgIfRxBadVersionDscrd = _EMplsPimSnpgIfRxBadVersionDscrd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 5, 2, 1, 7),
    _EMplsPimSnpgIfRxBadVersionDscrd_Type()
)
eMplsPimSnpgIfRxBadVersionDscrd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eMplsPimSnpgIfRxBadVersionDscrd.setStatus("current")
_EMplsPimSnpgIfRxBadEncodings_Type = Counter32
_EMplsPimSnpgIfRxBadEncodings_Object = MibTableColumn
eMplsPimSnpgIfRxBadEncodings = _EMplsPimSnpgIfRxBadEncodings_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 5, 2, 1, 8),
    _EMplsPimSnpgIfRxBadEncodings_Type()
)
eMplsPimSnpgIfRxBadEncodings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eMplsPimSnpgIfRxBadEncodings.setStatus("current")
_EMplsPimSnpgIfStarGTypes_Type = Gauge32
_EMplsPimSnpgIfStarGTypes_Object = MibTableColumn
eMplsPimSnpgIfStarGTypes = _EMplsPimSnpgIfStarGTypes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 5, 2, 1, 9),
    _EMplsPimSnpgIfStarGTypes_Type()
)
eMplsPimSnpgIfStarGTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eMplsPimSnpgIfStarGTypes.setStatus("current")
_EMplsPimSnpgIfSGTypes_Type = Gauge32
_EMplsPimSnpgIfSGTypes_Object = MibTableColumn
eMplsPimSnpgIfSGTypes = _EMplsPimSnpgIfSGTypes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 5, 2, 1, 10),
    _EMplsPimSnpgIfSGTypes_Type()
)
eMplsPimSnpgIfSGTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eMplsPimSnpgIfSGTypes.setStatus("current")
_EMplsPimSnpgIfJoinPolicyDrops_Type = Counter32
_EMplsPimSnpgIfJoinPolicyDrops_Object = MibTableColumn
eMplsPimSnpgIfJoinPolicyDrops = _EMplsPimSnpgIfJoinPolicyDrops_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 5, 2, 1, 11),
    _EMplsPimSnpgIfJoinPolicyDrops_Type()
)
eMplsPimSnpgIfJoinPolicyDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eMplsPimSnpgIfJoinPolicyDrops.setStatus("current")
_EMplsPimSnpgIfTxJoinPrunes_Type = Counter32
_EMplsPimSnpgIfTxJoinPrunes_Object = MibTableColumn
eMplsPimSnpgIfTxJoinPrunes = _EMplsPimSnpgIfTxJoinPrunes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 5, 2, 1, 12),
    _EMplsPimSnpgIfTxJoinPrunes_Type()
)
eMplsPimSnpgIfTxJoinPrunes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eMplsPimSnpgIfTxJoinPrunes.setStatus("current")
_EMplsPimSnpgIfRxJoinPrunes_Type = Counter32
_EMplsPimSnpgIfRxJoinPrunes_Object = MibTableColumn
eMplsPimSnpgIfRxJoinPrunes = _EMplsPimSnpgIfRxJoinPrunes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 5, 2, 1, 13),
    _EMplsPimSnpgIfRxJoinPrunes_Type()
)
eMplsPimSnpgIfRxJoinPrunes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eMplsPimSnpgIfRxJoinPrunes.setStatus("current")
_EMplsPimSnpgIfRxJoinPruneErrs_Type = Counter32
_EMplsPimSnpgIfRxJoinPruneErrs_Object = MibTableColumn
eMplsPimSnpgIfRxJoinPruneErrs = _EMplsPimSnpgIfRxJoinPruneErrs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 5, 2, 1, 14),
    _EMplsPimSnpgIfRxJoinPruneErrs_Type()
)
eMplsPimSnpgIfRxJoinPruneErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eMplsPimSnpgIfRxJoinPruneErrs.setStatus("current")
_EMplsPimSnpgIfNbrTable_Object = MibTable
eMplsPimSnpgIfNbrTable = _EMplsPimSnpgIfNbrTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 5, 3)
)
if mibBuilder.loadTexts:
    eMplsPimSnpgIfNbrTable.setStatus("current")
_EMplsPimSnpgIfNbrEntry_Object = MibTableRow
eMplsPimSnpgIfNbrEntry = _EMplsPimSnpgIfNbrEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 5, 3, 1)
)
eMplsPimSnpgIfNbrEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-PIM-SNOOPING-MIB", "eMplsPimSnpgIfNbrAddrType"),
    (0, "TIMETRA-PIM-SNOOPING-MIB", "eMplsPimSnpgIfNbrAddress"),
)
if mibBuilder.loadTexts:
    eMplsPimSnpgIfNbrEntry.setStatus("current")
_EMplsPimSnpgIfNbrAddrType_Type = InetAddressType
_EMplsPimSnpgIfNbrAddrType_Object = MibTableColumn
eMplsPimSnpgIfNbrAddrType = _EMplsPimSnpgIfNbrAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 5, 3, 1, 1),
    _EMplsPimSnpgIfNbrAddrType_Type()
)
eMplsPimSnpgIfNbrAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eMplsPimSnpgIfNbrAddrType.setStatus("current")


class _EMplsPimSnpgIfNbrAddress_Type(InetAddress):
    """Custom type eMplsPimSnpgIfNbrAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_EMplsPimSnpgIfNbrAddress_Type.__name__ = "InetAddress"
_EMplsPimSnpgIfNbrAddress_Object = MibTableColumn
eMplsPimSnpgIfNbrAddress = _EMplsPimSnpgIfNbrAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 5, 3, 1, 2),
    _EMplsPimSnpgIfNbrAddress_Type()
)
eMplsPimSnpgIfNbrAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eMplsPimSnpgIfNbrAddress.setStatus("current")
_EMplsPimSnpgIfNbrUpTime_Type = Unsigned32
_EMplsPimSnpgIfNbrUpTime_Object = MibTableColumn
eMplsPimSnpgIfNbrUpTime = _EMplsPimSnpgIfNbrUpTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 5, 3, 1, 3),
    _EMplsPimSnpgIfNbrUpTime_Type()
)
eMplsPimSnpgIfNbrUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eMplsPimSnpgIfNbrUpTime.setStatus("current")
if mibBuilder.loadTexts:
    eMplsPimSnpgIfNbrUpTime.setUnits("seconds")
_EMplsPimSnpgIfNbrExpiryTime_Type = Unsigned32
_EMplsPimSnpgIfNbrExpiryTime_Object = MibTableColumn
eMplsPimSnpgIfNbrExpiryTime = _EMplsPimSnpgIfNbrExpiryTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 5, 3, 1, 4),
    _EMplsPimSnpgIfNbrExpiryTime_Type()
)
eMplsPimSnpgIfNbrExpiryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eMplsPimSnpgIfNbrExpiryTime.setStatus("current")
if mibBuilder.loadTexts:
    eMplsPimSnpgIfNbrExpiryTime.setUnits("seconds")
_EMplsPimSnpgIfNbrGenId_Type = Unsigned32
_EMplsPimSnpgIfNbrGenId_Object = MibTableColumn
eMplsPimSnpgIfNbrGenId = _EMplsPimSnpgIfNbrGenId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 5, 3, 1, 5),
    _EMplsPimSnpgIfNbrGenId_Type()
)
eMplsPimSnpgIfNbrGenId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eMplsPimSnpgIfNbrGenId.setStatus("current")
_EMplsPimSnpgIfNbrDrPriority_Type = Unsigned32
_EMplsPimSnpgIfNbrDrPriority_Object = MibTableColumn
eMplsPimSnpgIfNbrDrPriority = _EMplsPimSnpgIfNbrDrPriority_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 5, 3, 1, 6),
    _EMplsPimSnpgIfNbrDrPriority_Type()
)
eMplsPimSnpgIfNbrDrPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eMplsPimSnpgIfNbrDrPriority.setStatus("current")
_EMplsPimSnpgIfNbrDrPriorPresent_Type = TruthValue
_EMplsPimSnpgIfNbrDrPriorPresent_Object = MibTableColumn
eMplsPimSnpgIfNbrDrPriorPresent = _EMplsPimSnpgIfNbrDrPriorPresent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 5, 3, 1, 7),
    _EMplsPimSnpgIfNbrDrPriorPresent_Type()
)
eMplsPimSnpgIfNbrDrPriorPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eMplsPimSnpgIfNbrDrPriorPresent.setStatus("current")
_EMplsPimSnpgIfNbrLanDelay_Type = Unsigned32
_EMplsPimSnpgIfNbrLanDelay_Object = MibTableColumn
eMplsPimSnpgIfNbrLanDelay = _EMplsPimSnpgIfNbrLanDelay_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 5, 3, 1, 8),
    _EMplsPimSnpgIfNbrLanDelay_Type()
)
eMplsPimSnpgIfNbrLanDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eMplsPimSnpgIfNbrLanDelay.setStatus("current")
if mibBuilder.loadTexts:
    eMplsPimSnpgIfNbrLanDelay.setUnits("milliseconds")
_EMplsPimSnpgIfNbrLanDlayPrsnt_Type = TruthValue
_EMplsPimSnpgIfNbrLanDlayPrsnt_Object = MibTableColumn
eMplsPimSnpgIfNbrLanDlayPrsnt = _EMplsPimSnpgIfNbrLanDlayPrsnt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 5, 3, 1, 9),
    _EMplsPimSnpgIfNbrLanDlayPrsnt_Type()
)
eMplsPimSnpgIfNbrLanDlayPrsnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eMplsPimSnpgIfNbrLanDlayPrsnt.setStatus("current")
_EMplsPimSnpgIfNbrTrckngSpprt_Type = TruthValue
_EMplsPimSnpgIfNbrTrckngSpprt_Object = MibTableColumn
eMplsPimSnpgIfNbrTrckngSpprt = _EMplsPimSnpgIfNbrTrckngSpprt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 5, 3, 1, 10),
    _EMplsPimSnpgIfNbrTrckngSpprt_Type()
)
eMplsPimSnpgIfNbrTrckngSpprt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eMplsPimSnpgIfNbrTrckngSpprt.setStatus("current")
_EMplsPimSnpgIfNbrHoldTime_Type = Unsigned32
_EMplsPimSnpgIfNbrHoldTime_Object = MibTableColumn
eMplsPimSnpgIfNbrHoldTime = _EMplsPimSnpgIfNbrHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 5, 3, 1, 11),
    _EMplsPimSnpgIfNbrHoldTime_Type()
)
eMplsPimSnpgIfNbrHoldTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eMplsPimSnpgIfNbrHoldTime.setStatus("current")
if mibBuilder.loadTexts:
    eMplsPimSnpgIfNbrHoldTime.setUnits("seconds")
_EMplsPimSnpgIfNbrOvrdeIntrvl_Type = Unsigned32
_EMplsPimSnpgIfNbrOvrdeIntrvl_Object = MibTableColumn
eMplsPimSnpgIfNbrOvrdeIntrvl = _EMplsPimSnpgIfNbrOvrdeIntrvl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 5, 3, 1, 12),
    _EMplsPimSnpgIfNbrOvrdeIntrvl_Type()
)
eMplsPimSnpgIfNbrOvrdeIntrvl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eMplsPimSnpgIfNbrOvrdeIntrvl.setStatus("current")
if mibBuilder.loadTexts:
    eMplsPimSnpgIfNbrOvrdeIntrvl.setUnits("milliseconds")
_EMplsPimSnpgIfSecNbrTable_Object = MibTable
eMplsPimSnpgIfSecNbrTable = _EMplsPimSnpgIfSecNbrTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 5, 4)
)
if mibBuilder.loadTexts:
    eMplsPimSnpgIfSecNbrTable.setStatus("current")
_EMplsPimSnpgIfSecNbrEntry_Object = MibTableRow
eMplsPimSnpgIfSecNbrEntry = _EMplsPimSnpgIfSecNbrEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 5, 4, 1)
)
eMplsPimSnpgIfSecNbrEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-PIM-SNOOPING-MIB", "eMplsPimSnpgIfNbrAddrType"),
    (0, "TIMETRA-PIM-SNOOPING-MIB", "eMplsPimSnpgIfNbrAddress"),
    (0, "TIMETRA-PIM-SNOOPING-MIB", "eMplsPimSnpgIfSecNbrAddrType"),
    (0, "TIMETRA-PIM-SNOOPING-MIB", "eMplsPimSnpgIfSecNbrAddress"),
)
if mibBuilder.loadTexts:
    eMplsPimSnpgIfSecNbrEntry.setStatus("current")
_EMplsPimSnpgIfSecNbrAddrType_Type = InetAddressType
_EMplsPimSnpgIfSecNbrAddrType_Object = MibTableColumn
eMplsPimSnpgIfSecNbrAddrType = _EMplsPimSnpgIfSecNbrAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 5, 4, 1, 1),
    _EMplsPimSnpgIfSecNbrAddrType_Type()
)
eMplsPimSnpgIfSecNbrAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eMplsPimSnpgIfSecNbrAddrType.setStatus("current")


class _EMplsPimSnpgIfSecNbrAddress_Type(InetAddress):
    """Custom type eMplsPimSnpgIfSecNbrAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_EMplsPimSnpgIfSecNbrAddress_Type.__name__ = "InetAddress"
_EMplsPimSnpgIfSecNbrAddress_Object = MibTableColumn
eMplsPimSnpgIfSecNbrAddress = _EMplsPimSnpgIfSecNbrAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 5, 4, 1, 2),
    _EMplsPimSnpgIfSecNbrAddress_Type()
)
eMplsPimSnpgIfSecNbrAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eMplsPimSnpgIfSecNbrAddress.setStatus("current")
_EMplsPimSnpgIfGrpSrcTable_Object = MibTable
eMplsPimSnpgIfGrpSrcTable = _EMplsPimSnpgIfGrpSrcTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 5, 5)
)
if mibBuilder.loadTexts:
    eMplsPimSnpgIfGrpSrcTable.setStatus("current")
_EMplsPimSnpgIfGrpSrcEntry_Object = MibTableRow
eMplsPimSnpgIfGrpSrcEntry = _EMplsPimSnpgIfGrpSrcEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 5, 5, 1)
)
eMplsPimSnpgIfGrpSrcEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-PIM-SNOOPING-MIB", "eMplsPimSnpgIfGrpSrcGrpAddrType"),
    (0, "TIMETRA-PIM-SNOOPING-MIB", "eMplsPimSnpgIfGrpSrcGroupAddr"),
    (0, "TIMETRA-PIM-SNOOPING-MIB", "eMplsPimSnpgIfGrpSrcSrcAddrType"),
    (0, "TIMETRA-PIM-SNOOPING-MIB", "eMplsPimSnpgIfGrpSrcSourceAddr"),
)
if mibBuilder.loadTexts:
    eMplsPimSnpgIfGrpSrcEntry.setStatus("current")
_EMplsPimSnpgIfGrpSrcGrpAddrType_Type = InetAddressType
_EMplsPimSnpgIfGrpSrcGrpAddrType_Object = MibTableColumn
eMplsPimSnpgIfGrpSrcGrpAddrType = _EMplsPimSnpgIfGrpSrcGrpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 5, 5, 1, 1),
    _EMplsPimSnpgIfGrpSrcGrpAddrType_Type()
)
eMplsPimSnpgIfGrpSrcGrpAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eMplsPimSnpgIfGrpSrcGrpAddrType.setStatus("current")


class _EMplsPimSnpgIfGrpSrcGroupAddr_Type(InetAddress):
    """Custom type eMplsPimSnpgIfGrpSrcGroupAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_EMplsPimSnpgIfGrpSrcGroupAddr_Type.__name__ = "InetAddress"
_EMplsPimSnpgIfGrpSrcGroupAddr_Object = MibTableColumn
eMplsPimSnpgIfGrpSrcGroupAddr = _EMplsPimSnpgIfGrpSrcGroupAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 5, 5, 1, 2),
    _EMplsPimSnpgIfGrpSrcGroupAddr_Type()
)
eMplsPimSnpgIfGrpSrcGroupAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eMplsPimSnpgIfGrpSrcGroupAddr.setStatus("current")
_EMplsPimSnpgIfGrpSrcSrcAddrType_Type = InetAddressType
_EMplsPimSnpgIfGrpSrcSrcAddrType_Object = MibTableColumn
eMplsPimSnpgIfGrpSrcSrcAddrType = _EMplsPimSnpgIfGrpSrcSrcAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 5, 5, 1, 3),
    _EMplsPimSnpgIfGrpSrcSrcAddrType_Type()
)
eMplsPimSnpgIfGrpSrcSrcAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eMplsPimSnpgIfGrpSrcSrcAddrType.setStatus("current")


class _EMplsPimSnpgIfGrpSrcSourceAddr_Type(InetAddress):
    """Custom type eMplsPimSnpgIfGrpSrcSourceAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_EMplsPimSnpgIfGrpSrcSourceAddr_Type.__name__ = "InetAddress"
_EMplsPimSnpgIfGrpSrcSourceAddr_Object = MibTableColumn
eMplsPimSnpgIfGrpSrcSourceAddr = _EMplsPimSnpgIfGrpSrcSourceAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 5, 5, 1, 4),
    _EMplsPimSnpgIfGrpSrcSourceAddr_Type()
)
eMplsPimSnpgIfGrpSrcSourceAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eMplsPimSnpgIfGrpSrcSourceAddr.setStatus("current")


class _EMplsPimSnpgIfGrpSrcJPState_Type(Integer32):
    """Custom type eMplsPimSnpgIfGrpSrcJPState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noInfo", 0),
          ("join", 1),
          ("prunePend", 2),
          ("pruned", 3))
    )


_EMplsPimSnpgIfGrpSrcJPState_Type.__name__ = "Integer32"
_EMplsPimSnpgIfGrpSrcJPState_Object = MibTableColumn
eMplsPimSnpgIfGrpSrcJPState = _EMplsPimSnpgIfGrpSrcJPState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 5, 5, 1, 5),
    _EMplsPimSnpgIfGrpSrcJPState_Type()
)
eMplsPimSnpgIfGrpSrcJPState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eMplsPimSnpgIfGrpSrcJPState.setStatus("current")
_EMplsPimSnpgIfGrpSrcPrunePendTmr_Type = Unsigned32
_EMplsPimSnpgIfGrpSrcPrunePendTmr_Object = MibTableColumn
eMplsPimSnpgIfGrpSrcPrunePendTmr = _EMplsPimSnpgIfGrpSrcPrunePendTmr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 5, 5, 1, 6),
    _EMplsPimSnpgIfGrpSrcPrunePendTmr_Type()
)
eMplsPimSnpgIfGrpSrcPrunePendTmr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eMplsPimSnpgIfGrpSrcPrunePendTmr.setStatus("current")
if mibBuilder.loadTexts:
    eMplsPimSnpgIfGrpSrcPrunePendTmr.setUnits("seconds")
_EMplsPimSnpgIfGrpSrcJPTimer_Type = Unsigned32
_EMplsPimSnpgIfGrpSrcJPTimer_Object = MibTableColumn
eMplsPimSnpgIfGrpSrcJPTimer = _EMplsPimSnpgIfGrpSrcJPTimer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 5, 5, 1, 7),
    _EMplsPimSnpgIfGrpSrcJPTimer_Type()
)
eMplsPimSnpgIfGrpSrcJPTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eMplsPimSnpgIfGrpSrcJPTimer.setStatus("current")
if mibBuilder.loadTexts:
    eMplsPimSnpgIfGrpSrcJPTimer.setUnits("seconds")


class _EMplsPimSnpgIfGrpSrcJPRptState_Type(Integer32):
    """Custom type eMplsPimSnpgIfGrpSrcJPRptState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noInfo", 0),
          ("join", 1),
          ("prunePend", 2),
          ("pruned", 3))
    )


_EMplsPimSnpgIfGrpSrcJPRptState_Type.__name__ = "Integer32"
_EMplsPimSnpgIfGrpSrcJPRptState_Object = MibTableColumn
eMplsPimSnpgIfGrpSrcJPRptState = _EMplsPimSnpgIfGrpSrcJPRptState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 5, 5, 1, 8),
    _EMplsPimSnpgIfGrpSrcJPRptState_Type()
)
eMplsPimSnpgIfGrpSrcJPRptState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eMplsPimSnpgIfGrpSrcJPRptState.setStatus("current")
_EMplsPimSnpgIfGrpSrcRptPrnPndTmr_Type = Unsigned32
_EMplsPimSnpgIfGrpSrcRptPrnPndTmr_Object = MibTableColumn
eMplsPimSnpgIfGrpSrcRptPrnPndTmr = _EMplsPimSnpgIfGrpSrcRptPrnPndTmr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 5, 5, 1, 9),
    _EMplsPimSnpgIfGrpSrcRptPrnPndTmr_Type()
)
eMplsPimSnpgIfGrpSrcRptPrnPndTmr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eMplsPimSnpgIfGrpSrcRptPrnPndTmr.setStatus("current")
if mibBuilder.loadTexts:
    eMplsPimSnpgIfGrpSrcRptPrnPndTmr.setUnits("seconds")
_EMplsPimSnpgIfGrpSrcRptJPTimer_Type = Unsigned32
_EMplsPimSnpgIfGrpSrcRptJPTimer_Object = MibTableColumn
eMplsPimSnpgIfGrpSrcRptJPTimer = _EMplsPimSnpgIfGrpSrcRptJPTimer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 5, 5, 1, 10),
    _EMplsPimSnpgIfGrpSrcRptJPTimer_Type()
)
eMplsPimSnpgIfGrpSrcRptJPTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eMplsPimSnpgIfGrpSrcRptJPTimer.setStatus("current")
if mibBuilder.loadTexts:
    eMplsPimSnpgIfGrpSrcRptJPTimer.setUnits("seconds")
_EMplsPimSnpgIfGrpSrcUpTime_Type = Unsigned32
_EMplsPimSnpgIfGrpSrcUpTime_Object = MibTableColumn
eMplsPimSnpgIfGrpSrcUpTime = _EMplsPimSnpgIfGrpSrcUpTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 5, 5, 1, 11),
    _EMplsPimSnpgIfGrpSrcUpTime_Type()
)
eMplsPimSnpgIfGrpSrcUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eMplsPimSnpgIfGrpSrcUpTime.setStatus("current")
if mibBuilder.loadTexts:
    eMplsPimSnpgIfGrpSrcUpTime.setUnits("seconds")
_EMplsPimSnpgGrpSrcIfTable_Object = MibTable
eMplsPimSnpgGrpSrcIfTable = _EMplsPimSnpgGrpSrcIfTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 5, 6)
)
if mibBuilder.loadTexts:
    eMplsPimSnpgGrpSrcIfTable.setStatus("current")
_EMplsPimSnpgGrpSrcIfEntry_Object = MibTableRow
eMplsPimSnpgGrpSrcIfEntry = _EMplsPimSnpgGrpSrcIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 5, 6, 1)
)
eMplsPimSnpgGrpSrcIfEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-PIM-SNOOPING-MIB", "eMplsPimSnpgGrpSrcGrpAddrType"),
    (0, "TIMETRA-PIM-SNOOPING-MIB", "eMplsPimSnpgGrpSrcGroupAddress"),
    (0, "TIMETRA-PIM-SNOOPING-MIB", "eMplsPimSnpgGrpSrcSrcAddrType"),
    (0, "TIMETRA-PIM-SNOOPING-MIB", "eMplsPimSnpgGrpSrcSourceAddress"),
)
if mibBuilder.loadTexts:
    eMplsPimSnpgGrpSrcIfEntry.setStatus("current")
_EMplsPimSnpgGrpSrcGrpAddrType_Type = InetAddressType
_EMplsPimSnpgGrpSrcGrpAddrType_Object = MibTableColumn
eMplsPimSnpgGrpSrcGrpAddrType = _EMplsPimSnpgGrpSrcGrpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 5, 6, 1, 1),
    _EMplsPimSnpgGrpSrcGrpAddrType_Type()
)
eMplsPimSnpgGrpSrcGrpAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eMplsPimSnpgGrpSrcGrpAddrType.setStatus("current")


class _EMplsPimSnpgGrpSrcGroupAddress_Type(InetAddress):
    """Custom type eMplsPimSnpgGrpSrcGroupAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_EMplsPimSnpgGrpSrcGroupAddress_Type.__name__ = "InetAddress"
_EMplsPimSnpgGrpSrcGroupAddress_Object = MibTableColumn
eMplsPimSnpgGrpSrcGroupAddress = _EMplsPimSnpgGrpSrcGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 5, 6, 1, 2),
    _EMplsPimSnpgGrpSrcGroupAddress_Type()
)
eMplsPimSnpgGrpSrcGroupAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eMplsPimSnpgGrpSrcGroupAddress.setStatus("current")
_EMplsPimSnpgGrpSrcSrcAddrType_Type = InetAddressType
_EMplsPimSnpgGrpSrcSrcAddrType_Object = MibTableColumn
eMplsPimSnpgGrpSrcSrcAddrType = _EMplsPimSnpgGrpSrcSrcAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 5, 6, 1, 3),
    _EMplsPimSnpgGrpSrcSrcAddrType_Type()
)
eMplsPimSnpgGrpSrcSrcAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eMplsPimSnpgGrpSrcSrcAddrType.setStatus("current")


class _EMplsPimSnpgGrpSrcSourceAddress_Type(InetAddress):
    """Custom type eMplsPimSnpgGrpSrcSourceAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_EMplsPimSnpgGrpSrcSourceAddress_Type.__name__ = "InetAddress"
_EMplsPimSnpgGrpSrcSourceAddress_Object = MibTableColumn
eMplsPimSnpgGrpSrcSourceAddress = _EMplsPimSnpgGrpSrcSourceAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 5, 6, 1, 4),
    _EMplsPimSnpgGrpSrcSourceAddress_Type()
)
eMplsPimSnpgGrpSrcSourceAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eMplsPimSnpgGrpSrcSourceAddress.setStatus("current")


class _EMplsPimSnpgGrpSrcIfFlags_Type(Bits):
    """Custom type eMplsPimSnpgGrpSrcIfFlags based on Bits"""
    namedValues = NamedValues(
        *(("immediateOifList", 0),
          ("inheritedOifList", 1),
          ("inheritedRptOifList", 2),
          ("joined", 3),
          ("rpfPort", 4))
    )

_EMplsPimSnpgGrpSrcIfFlags_Type.__name__ = "Bits"
_EMplsPimSnpgGrpSrcIfFlags_Object = MibTableColumn
eMplsPimSnpgGrpSrcIfFlags = _EMplsPimSnpgGrpSrcIfFlags_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 5, 6, 1, 5),
    _EMplsPimSnpgGrpSrcIfFlags_Type()
)
eMplsPimSnpgGrpSrcIfFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eMplsPimSnpgGrpSrcIfFlags.setStatus("current")
_TmnxPimSnpgRVplsIfObjs_ObjectIdentity = ObjectIdentity
tmnxPimSnpgRVplsIfObjs = _TmnxPimSnpgRVplsIfObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 6)
)
_RVplsPimSnpgIfTable_Object = MibTable
rVplsPimSnpgIfTable = _RVplsPimSnpgIfTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 6, 1)
)
if mibBuilder.loadTexts:
    rVplsPimSnpgIfTable.setStatus("current")
_RVplsPimSnpgIfEntry_Object = MibTableRow
rVplsPimSnpgIfEntry = _RVplsPimSnpgIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 6, 1, 1)
)
rVplsPimSnpgIfEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-VRTR-MIB", "vRtrIfIndex"),
    (0, "TIMETRA-PIM-NG-MIB", "vRtrPimNgAFGenAFType"),
)
if mibBuilder.loadTexts:
    rVplsPimSnpgIfEntry.setStatus("current")
_RVplsPimSnpgIfLastChangeTime_Type = TimeStamp
_RVplsPimSnpgIfLastChangeTime_Object = MibTableColumn
rVplsPimSnpgIfLastChangeTime = _RVplsPimSnpgIfLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 6, 1, 1, 1),
    _RVplsPimSnpgIfLastChangeTime_Type()
)
rVplsPimSnpgIfLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rVplsPimSnpgIfLastChangeTime.setStatus("current")
_RVplsPimSnpgIfOperState_Type = ServiceOperStatus
_RVplsPimSnpgIfOperState_Object = MibTableColumn
rVplsPimSnpgIfOperState = _RVplsPimSnpgIfOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 6, 1, 1, 2),
    _RVplsPimSnpgIfOperState_Type()
)
rVplsPimSnpgIfOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rVplsPimSnpgIfOperState.setStatus("current")
_RVplsPimSnpgIfUpTime_Type = Unsigned32
_RVplsPimSnpgIfUpTime_Object = MibTableColumn
rVplsPimSnpgIfUpTime = _RVplsPimSnpgIfUpTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 6, 1, 1, 3),
    _RVplsPimSnpgIfUpTime_Type()
)
rVplsPimSnpgIfUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rVplsPimSnpgIfUpTime.setStatus("current")
if mibBuilder.loadTexts:
    rVplsPimSnpgIfUpTime.setUnits("seconds")
_RVplsPimSnpgIfCurrentGroups_Type = Gauge32
_RVplsPimSnpgIfCurrentGroups_Object = MibTableColumn
rVplsPimSnpgIfCurrentGroups = _RVplsPimSnpgIfCurrentGroups_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 6, 1, 1, 4),
    _RVplsPimSnpgIfCurrentGroups_Type()
)
rVplsPimSnpgIfCurrentGroups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rVplsPimSnpgIfCurrentGroups.setStatus("current")
_RVplsPimSnpgIfMaxGroupsTillNow_Type = Counter32
_RVplsPimSnpgIfMaxGroupsTillNow_Object = MibTableColumn
rVplsPimSnpgIfMaxGroupsTillNow = _RVplsPimSnpgIfMaxGroupsTillNow_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 6, 1, 1, 5),
    _RVplsPimSnpgIfMaxGroupsTillNow_Type()
)
rVplsPimSnpgIfMaxGroupsTillNow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rVplsPimSnpgIfMaxGroupsTillNow.setStatus("current")


class _RVplsPimSnpgIfPwFwding_Type(TruthValue):
    """Custom type rVplsPimSnpgIfPwFwding based on TruthValue"""
    defaultValue = 1


_RVplsPimSnpgIfPwFwding_Type.__name__ = "TruthValue"
_RVplsPimSnpgIfPwFwding_Object = MibTableColumn
rVplsPimSnpgIfPwFwding = _RVplsPimSnpgIfPwFwding_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 6, 1, 1, 6),
    _RVplsPimSnpgIfPwFwding_Type()
)
rVplsPimSnpgIfPwFwding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rVplsPimSnpgIfPwFwding.setStatus("current")
_RVplsPimSnpgIfStatsTable_Object = MibTable
rVplsPimSnpgIfStatsTable = _RVplsPimSnpgIfStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 6, 2)
)
if mibBuilder.loadTexts:
    rVplsPimSnpgIfStatsTable.setStatus("current")
_RVplsPimSnpgIfStatsEntry_Object = MibTableRow
rVplsPimSnpgIfStatsEntry = _RVplsPimSnpgIfStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 6, 2, 1)
)
if mibBuilder.loadTexts:
    rVplsPimSnpgIfStatsEntry.setStatus("current")
_RVplsPimSnpgIfTxPkts_Type = Counter32
_RVplsPimSnpgIfTxPkts_Object = MibTableColumn
rVplsPimSnpgIfTxPkts = _RVplsPimSnpgIfTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 6, 2, 1, 1),
    _RVplsPimSnpgIfTxPkts_Type()
)
rVplsPimSnpgIfTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rVplsPimSnpgIfTxPkts.setStatus("current")
_RVplsPimSnpgIfRxPkts_Type = Counter32
_RVplsPimSnpgIfRxPkts_Object = MibTableColumn
rVplsPimSnpgIfRxPkts = _RVplsPimSnpgIfRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 6, 2, 1, 2),
    _RVplsPimSnpgIfRxPkts_Type()
)
rVplsPimSnpgIfRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rVplsPimSnpgIfRxPkts.setStatus("current")
_RVplsPimSnpgIfRxHellos_Type = Counter32
_RVplsPimSnpgIfRxHellos_Object = MibTableColumn
rVplsPimSnpgIfRxHellos = _RVplsPimSnpgIfRxHellos_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 6, 2, 1, 3),
    _RVplsPimSnpgIfRxHellos_Type()
)
rVplsPimSnpgIfRxHellos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rVplsPimSnpgIfRxHellos.setStatus("current")
_RVplsPimSnpgIfRxHellosDropped_Type = Counter32
_RVplsPimSnpgIfRxHellosDropped_Object = MibTableColumn
rVplsPimSnpgIfRxHellosDropped = _RVplsPimSnpgIfRxHellosDropped_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 6, 2, 1, 4),
    _RVplsPimSnpgIfRxHellosDropped_Type()
)
rVplsPimSnpgIfRxHellosDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rVplsPimSnpgIfRxHellosDropped.setStatus("current")
_RVplsPimSnpgIfRxNbrUnknown_Type = Counter32
_RVplsPimSnpgIfRxNbrUnknown_Object = MibTableColumn
rVplsPimSnpgIfRxNbrUnknown = _RVplsPimSnpgIfRxNbrUnknown_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 6, 2, 1, 5),
    _RVplsPimSnpgIfRxNbrUnknown_Type()
)
rVplsPimSnpgIfRxNbrUnknown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rVplsPimSnpgIfRxNbrUnknown.setStatus("current")
_RVplsPimSnpgIfRxBadChecksumDscrd_Type = Counter32
_RVplsPimSnpgIfRxBadChecksumDscrd_Object = MibTableColumn
rVplsPimSnpgIfRxBadChecksumDscrd = _RVplsPimSnpgIfRxBadChecksumDscrd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 6, 2, 1, 6),
    _RVplsPimSnpgIfRxBadChecksumDscrd_Type()
)
rVplsPimSnpgIfRxBadChecksumDscrd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rVplsPimSnpgIfRxBadChecksumDscrd.setStatus("current")
_RVplsPimSnpgIfRxBadVersionDscrd_Type = Counter32
_RVplsPimSnpgIfRxBadVersionDscrd_Object = MibTableColumn
rVplsPimSnpgIfRxBadVersionDscrd = _RVplsPimSnpgIfRxBadVersionDscrd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 6, 2, 1, 7),
    _RVplsPimSnpgIfRxBadVersionDscrd_Type()
)
rVplsPimSnpgIfRxBadVersionDscrd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rVplsPimSnpgIfRxBadVersionDscrd.setStatus("current")
_RVplsPimSnpgIfRxBadEncodings_Type = Counter32
_RVplsPimSnpgIfRxBadEncodings_Object = MibTableColumn
rVplsPimSnpgIfRxBadEncodings = _RVplsPimSnpgIfRxBadEncodings_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 6, 2, 1, 8),
    _RVplsPimSnpgIfRxBadEncodings_Type()
)
rVplsPimSnpgIfRxBadEncodings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rVplsPimSnpgIfRxBadEncodings.setStatus("current")
_RVplsPimSnpgIfStarGTypes_Type = Gauge32
_RVplsPimSnpgIfStarGTypes_Object = MibTableColumn
rVplsPimSnpgIfStarGTypes = _RVplsPimSnpgIfStarGTypes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 6, 2, 1, 9),
    _RVplsPimSnpgIfStarGTypes_Type()
)
rVplsPimSnpgIfStarGTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rVplsPimSnpgIfStarGTypes.setStatus("current")
_RVplsPimSnpgIfSGTypes_Type = Gauge32
_RVplsPimSnpgIfSGTypes_Object = MibTableColumn
rVplsPimSnpgIfSGTypes = _RVplsPimSnpgIfSGTypes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 6, 2, 1, 10),
    _RVplsPimSnpgIfSGTypes_Type()
)
rVplsPimSnpgIfSGTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rVplsPimSnpgIfSGTypes.setStatus("current")
_RVplsPimSnpgIfJoinPolicyDrops_Type = Counter32
_RVplsPimSnpgIfJoinPolicyDrops_Object = MibTableColumn
rVplsPimSnpgIfJoinPolicyDrops = _RVplsPimSnpgIfJoinPolicyDrops_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 6, 2, 1, 11),
    _RVplsPimSnpgIfJoinPolicyDrops_Type()
)
rVplsPimSnpgIfJoinPolicyDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rVplsPimSnpgIfJoinPolicyDrops.setStatus("current")
_RVplsPimSnpgIfTxJoinPrunes_Type = Counter32
_RVplsPimSnpgIfTxJoinPrunes_Object = MibTableColumn
rVplsPimSnpgIfTxJoinPrunes = _RVplsPimSnpgIfTxJoinPrunes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 6, 2, 1, 12),
    _RVplsPimSnpgIfTxJoinPrunes_Type()
)
rVplsPimSnpgIfTxJoinPrunes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rVplsPimSnpgIfTxJoinPrunes.setStatus("current")
_RVplsPimSnpgIfRxJoinPrunes_Type = Counter32
_RVplsPimSnpgIfRxJoinPrunes_Object = MibTableColumn
rVplsPimSnpgIfRxJoinPrunes = _RVplsPimSnpgIfRxJoinPrunes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 6, 2, 1, 13),
    _RVplsPimSnpgIfRxJoinPrunes_Type()
)
rVplsPimSnpgIfRxJoinPrunes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rVplsPimSnpgIfRxJoinPrunes.setStatus("current")
_RVplsPimSnpgIfRxJoinPruneErrs_Type = Counter32
_RVplsPimSnpgIfRxJoinPruneErrs_Object = MibTableColumn
rVplsPimSnpgIfRxJoinPruneErrs = _RVplsPimSnpgIfRxJoinPruneErrs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 6, 2, 1, 14),
    _RVplsPimSnpgIfRxJoinPruneErrs_Type()
)
rVplsPimSnpgIfRxJoinPruneErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rVplsPimSnpgIfRxJoinPruneErrs.setStatus("current")
_RVplsPimSnpgIfNbrTable_Object = MibTable
rVplsPimSnpgIfNbrTable = _RVplsPimSnpgIfNbrTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 6, 3)
)
if mibBuilder.loadTexts:
    rVplsPimSnpgIfNbrTable.setStatus("current")
_RVplsPimSnpgIfNbrEntry_Object = MibTableRow
rVplsPimSnpgIfNbrEntry = _RVplsPimSnpgIfNbrEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 6, 3, 1)
)
rVplsPimSnpgIfNbrEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-VRTR-MIB", "vRtrIfIndex"),
    (0, "TIMETRA-PIM-SNOOPING-MIB", "rVplsPimSnpgIfNbrAddrType"),
    (0, "TIMETRA-PIM-SNOOPING-MIB", "rVplsPimSnpgIfNbrAddress"),
)
if mibBuilder.loadTexts:
    rVplsPimSnpgIfNbrEntry.setStatus("current")
_RVplsPimSnpgIfNbrAddrType_Type = InetAddressType
_RVplsPimSnpgIfNbrAddrType_Object = MibTableColumn
rVplsPimSnpgIfNbrAddrType = _RVplsPimSnpgIfNbrAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 6, 3, 1, 1),
    _RVplsPimSnpgIfNbrAddrType_Type()
)
rVplsPimSnpgIfNbrAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rVplsPimSnpgIfNbrAddrType.setStatus("current")


class _RVplsPimSnpgIfNbrAddress_Type(InetAddress):
    """Custom type rVplsPimSnpgIfNbrAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_RVplsPimSnpgIfNbrAddress_Type.__name__ = "InetAddress"
_RVplsPimSnpgIfNbrAddress_Object = MibTableColumn
rVplsPimSnpgIfNbrAddress = _RVplsPimSnpgIfNbrAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 6, 3, 1, 2),
    _RVplsPimSnpgIfNbrAddress_Type()
)
rVplsPimSnpgIfNbrAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rVplsPimSnpgIfNbrAddress.setStatus("current")
_RVplsPimSnpgIfNbrUpTime_Type = Unsigned32
_RVplsPimSnpgIfNbrUpTime_Object = MibTableColumn
rVplsPimSnpgIfNbrUpTime = _RVplsPimSnpgIfNbrUpTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 6, 3, 1, 3),
    _RVplsPimSnpgIfNbrUpTime_Type()
)
rVplsPimSnpgIfNbrUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rVplsPimSnpgIfNbrUpTime.setStatus("current")
if mibBuilder.loadTexts:
    rVplsPimSnpgIfNbrUpTime.setUnits("seconds")
_RVplsPimSnpgIfNbrExpiryTime_Type = Unsigned32
_RVplsPimSnpgIfNbrExpiryTime_Object = MibTableColumn
rVplsPimSnpgIfNbrExpiryTime = _RVplsPimSnpgIfNbrExpiryTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 6, 3, 1, 4),
    _RVplsPimSnpgIfNbrExpiryTime_Type()
)
rVplsPimSnpgIfNbrExpiryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rVplsPimSnpgIfNbrExpiryTime.setStatus("current")
if mibBuilder.loadTexts:
    rVplsPimSnpgIfNbrExpiryTime.setUnits("seconds")
_RVplsPimSnpgIfNbrGenId_Type = Unsigned32
_RVplsPimSnpgIfNbrGenId_Object = MibTableColumn
rVplsPimSnpgIfNbrGenId = _RVplsPimSnpgIfNbrGenId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 6, 3, 1, 5),
    _RVplsPimSnpgIfNbrGenId_Type()
)
rVplsPimSnpgIfNbrGenId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rVplsPimSnpgIfNbrGenId.setStatus("current")
_RVplsPimSnpgIfNbrDrPriority_Type = Unsigned32
_RVplsPimSnpgIfNbrDrPriority_Object = MibTableColumn
rVplsPimSnpgIfNbrDrPriority = _RVplsPimSnpgIfNbrDrPriority_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 6, 3, 1, 6),
    _RVplsPimSnpgIfNbrDrPriority_Type()
)
rVplsPimSnpgIfNbrDrPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rVplsPimSnpgIfNbrDrPriority.setStatus("current")
_RVplsPimSnpgIfNbrDrPriorPresent_Type = TruthValue
_RVplsPimSnpgIfNbrDrPriorPresent_Object = MibTableColumn
rVplsPimSnpgIfNbrDrPriorPresent = _RVplsPimSnpgIfNbrDrPriorPresent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 6, 3, 1, 7),
    _RVplsPimSnpgIfNbrDrPriorPresent_Type()
)
rVplsPimSnpgIfNbrDrPriorPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rVplsPimSnpgIfNbrDrPriorPresent.setStatus("current")
_RVplsPimSnpgIfNbrLanDelay_Type = Unsigned32
_RVplsPimSnpgIfNbrLanDelay_Object = MibTableColumn
rVplsPimSnpgIfNbrLanDelay = _RVplsPimSnpgIfNbrLanDelay_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 6, 3, 1, 8),
    _RVplsPimSnpgIfNbrLanDelay_Type()
)
rVplsPimSnpgIfNbrLanDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rVplsPimSnpgIfNbrLanDelay.setStatus("current")
if mibBuilder.loadTexts:
    rVplsPimSnpgIfNbrLanDelay.setUnits("milliseconds")
_RVplsPimSnpgIfNbrLanDlayPrsnt_Type = TruthValue
_RVplsPimSnpgIfNbrLanDlayPrsnt_Object = MibTableColumn
rVplsPimSnpgIfNbrLanDlayPrsnt = _RVplsPimSnpgIfNbrLanDlayPrsnt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 6, 3, 1, 9),
    _RVplsPimSnpgIfNbrLanDlayPrsnt_Type()
)
rVplsPimSnpgIfNbrLanDlayPrsnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rVplsPimSnpgIfNbrLanDlayPrsnt.setStatus("current")
_RVplsPimSnpgIfNbrTrckngSpprt_Type = TruthValue
_RVplsPimSnpgIfNbrTrckngSpprt_Object = MibTableColumn
rVplsPimSnpgIfNbrTrckngSpprt = _RVplsPimSnpgIfNbrTrckngSpprt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 6, 3, 1, 10),
    _RVplsPimSnpgIfNbrTrckngSpprt_Type()
)
rVplsPimSnpgIfNbrTrckngSpprt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rVplsPimSnpgIfNbrTrckngSpprt.setStatus("current")
_RVplsPimSnpgIfNbrHoldTime_Type = Unsigned32
_RVplsPimSnpgIfNbrHoldTime_Object = MibTableColumn
rVplsPimSnpgIfNbrHoldTime = _RVplsPimSnpgIfNbrHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 6, 3, 1, 11),
    _RVplsPimSnpgIfNbrHoldTime_Type()
)
rVplsPimSnpgIfNbrHoldTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rVplsPimSnpgIfNbrHoldTime.setStatus("current")
if mibBuilder.loadTexts:
    rVplsPimSnpgIfNbrHoldTime.setUnits("seconds")
_RVplsPimSnpgIfNbrOvrdeIntrvl_Type = Unsigned32
_RVplsPimSnpgIfNbrOvrdeIntrvl_Object = MibTableColumn
rVplsPimSnpgIfNbrOvrdeIntrvl = _RVplsPimSnpgIfNbrOvrdeIntrvl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 6, 3, 1, 12),
    _RVplsPimSnpgIfNbrOvrdeIntrvl_Type()
)
rVplsPimSnpgIfNbrOvrdeIntrvl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rVplsPimSnpgIfNbrOvrdeIntrvl.setStatus("current")
if mibBuilder.loadTexts:
    rVplsPimSnpgIfNbrOvrdeIntrvl.setUnits("milliseconds")
_RVplsPimSnpgIfSecNbrTable_Object = MibTable
rVplsPimSnpgIfSecNbrTable = _RVplsPimSnpgIfSecNbrTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 6, 4)
)
if mibBuilder.loadTexts:
    rVplsPimSnpgIfSecNbrTable.setStatus("current")
_RVplsPimSnpgIfSecNbrEntry_Object = MibTableRow
rVplsPimSnpgIfSecNbrEntry = _RVplsPimSnpgIfSecNbrEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 6, 4, 1)
)
rVplsPimSnpgIfSecNbrEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-VRTR-MIB", "vRtrIfIndex"),
    (0, "TIMETRA-PIM-SNOOPING-MIB", "rVplsPimSnpgIfNbrAddrType"),
    (0, "TIMETRA-PIM-SNOOPING-MIB", "rVplsPimSnpgIfNbrAddress"),
    (0, "TIMETRA-PIM-SNOOPING-MIB", "rVplsPimSnpgIfSecNbrAddrType"),
    (0, "TIMETRA-PIM-SNOOPING-MIB", "rVplsPimSnpgIfSecNbrAddress"),
)
if mibBuilder.loadTexts:
    rVplsPimSnpgIfSecNbrEntry.setStatus("current")
_RVplsPimSnpgIfSecNbrAddrType_Type = InetAddressType
_RVplsPimSnpgIfSecNbrAddrType_Object = MibTableColumn
rVplsPimSnpgIfSecNbrAddrType = _RVplsPimSnpgIfSecNbrAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 6, 4, 1, 1),
    _RVplsPimSnpgIfSecNbrAddrType_Type()
)
rVplsPimSnpgIfSecNbrAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rVplsPimSnpgIfSecNbrAddrType.setStatus("current")


class _RVplsPimSnpgIfSecNbrAddress_Type(InetAddress):
    """Custom type rVplsPimSnpgIfSecNbrAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_RVplsPimSnpgIfSecNbrAddress_Type.__name__ = "InetAddress"
_RVplsPimSnpgIfSecNbrAddress_Object = MibTableColumn
rVplsPimSnpgIfSecNbrAddress = _RVplsPimSnpgIfSecNbrAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 6, 4, 1, 2),
    _RVplsPimSnpgIfSecNbrAddress_Type()
)
rVplsPimSnpgIfSecNbrAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rVplsPimSnpgIfSecNbrAddress.setStatus("current")
_RVplsPimSnpgIfGrpSrcTable_Object = MibTable
rVplsPimSnpgIfGrpSrcTable = _RVplsPimSnpgIfGrpSrcTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 6, 5)
)
if mibBuilder.loadTexts:
    rVplsPimSnpgIfGrpSrcTable.setStatus("current")
_RVplsPimSnpgIfGrpSrcEntry_Object = MibTableRow
rVplsPimSnpgIfGrpSrcEntry = _RVplsPimSnpgIfGrpSrcEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 6, 5, 1)
)
rVplsPimSnpgIfGrpSrcEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-VRTR-MIB", "vRtrIfIndex"),
    (0, "TIMETRA-PIM-SNOOPING-MIB", "rVplsPimSnpgIfGrpSrcGrpAddrType"),
    (0, "TIMETRA-PIM-SNOOPING-MIB", "rVplsPimSnpgIfGrpSrcGroupAddr"),
    (0, "TIMETRA-PIM-SNOOPING-MIB", "rVplsPimSnpgIfGrpSrcSrcAddrType"),
    (0, "TIMETRA-PIM-SNOOPING-MIB", "rVplsPimSnpgIfGrpSrcSourceAddr"),
)
if mibBuilder.loadTexts:
    rVplsPimSnpgIfGrpSrcEntry.setStatus("current")
_RVplsPimSnpgIfGrpSrcGrpAddrType_Type = InetAddressType
_RVplsPimSnpgIfGrpSrcGrpAddrType_Object = MibTableColumn
rVplsPimSnpgIfGrpSrcGrpAddrType = _RVplsPimSnpgIfGrpSrcGrpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 6, 5, 1, 1),
    _RVplsPimSnpgIfGrpSrcGrpAddrType_Type()
)
rVplsPimSnpgIfGrpSrcGrpAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rVplsPimSnpgIfGrpSrcGrpAddrType.setStatus("current")


class _RVplsPimSnpgIfGrpSrcGroupAddr_Type(InetAddress):
    """Custom type rVplsPimSnpgIfGrpSrcGroupAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_RVplsPimSnpgIfGrpSrcGroupAddr_Type.__name__ = "InetAddress"
_RVplsPimSnpgIfGrpSrcGroupAddr_Object = MibTableColumn
rVplsPimSnpgIfGrpSrcGroupAddr = _RVplsPimSnpgIfGrpSrcGroupAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 6, 5, 1, 2),
    _RVplsPimSnpgIfGrpSrcGroupAddr_Type()
)
rVplsPimSnpgIfGrpSrcGroupAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rVplsPimSnpgIfGrpSrcGroupAddr.setStatus("current")
_RVplsPimSnpgIfGrpSrcSrcAddrType_Type = InetAddressType
_RVplsPimSnpgIfGrpSrcSrcAddrType_Object = MibTableColumn
rVplsPimSnpgIfGrpSrcSrcAddrType = _RVplsPimSnpgIfGrpSrcSrcAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 6, 5, 1, 3),
    _RVplsPimSnpgIfGrpSrcSrcAddrType_Type()
)
rVplsPimSnpgIfGrpSrcSrcAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rVplsPimSnpgIfGrpSrcSrcAddrType.setStatus("current")


class _RVplsPimSnpgIfGrpSrcSourceAddr_Type(InetAddress):
    """Custom type rVplsPimSnpgIfGrpSrcSourceAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_RVplsPimSnpgIfGrpSrcSourceAddr_Type.__name__ = "InetAddress"
_RVplsPimSnpgIfGrpSrcSourceAddr_Object = MibTableColumn
rVplsPimSnpgIfGrpSrcSourceAddr = _RVplsPimSnpgIfGrpSrcSourceAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 6, 5, 1, 4),
    _RVplsPimSnpgIfGrpSrcSourceAddr_Type()
)
rVplsPimSnpgIfGrpSrcSourceAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rVplsPimSnpgIfGrpSrcSourceAddr.setStatus("current")


class _RVplsPimSnpgIfGrpSrcJPState_Type(Integer32):
    """Custom type rVplsPimSnpgIfGrpSrcJPState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noInfo", 0),
          ("join", 1),
          ("prunePend", 2),
          ("pruned", 3))
    )


_RVplsPimSnpgIfGrpSrcJPState_Type.__name__ = "Integer32"
_RVplsPimSnpgIfGrpSrcJPState_Object = MibTableColumn
rVplsPimSnpgIfGrpSrcJPState = _RVplsPimSnpgIfGrpSrcJPState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 6, 5, 1, 5),
    _RVplsPimSnpgIfGrpSrcJPState_Type()
)
rVplsPimSnpgIfGrpSrcJPState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rVplsPimSnpgIfGrpSrcJPState.setStatus("current")
_RVplsPimSnpgIfGrpSrcPrunePendTmr_Type = Unsigned32
_RVplsPimSnpgIfGrpSrcPrunePendTmr_Object = MibTableColumn
rVplsPimSnpgIfGrpSrcPrunePendTmr = _RVplsPimSnpgIfGrpSrcPrunePendTmr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 6, 5, 1, 6),
    _RVplsPimSnpgIfGrpSrcPrunePendTmr_Type()
)
rVplsPimSnpgIfGrpSrcPrunePendTmr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rVplsPimSnpgIfGrpSrcPrunePendTmr.setStatus("current")
if mibBuilder.loadTexts:
    rVplsPimSnpgIfGrpSrcPrunePendTmr.setUnits("seconds")
_RVplsPimSnpgIfGrpSrcJPTimer_Type = Unsigned32
_RVplsPimSnpgIfGrpSrcJPTimer_Object = MibTableColumn
rVplsPimSnpgIfGrpSrcJPTimer = _RVplsPimSnpgIfGrpSrcJPTimer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 6, 5, 1, 7),
    _RVplsPimSnpgIfGrpSrcJPTimer_Type()
)
rVplsPimSnpgIfGrpSrcJPTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rVplsPimSnpgIfGrpSrcJPTimer.setStatus("current")
if mibBuilder.loadTexts:
    rVplsPimSnpgIfGrpSrcJPTimer.setUnits("seconds")


class _RVplsPimSnpgIfGrpSrcJPRptState_Type(Integer32):
    """Custom type rVplsPimSnpgIfGrpSrcJPRptState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noInfo", 0),
          ("join", 1),
          ("prunePend", 2),
          ("pruned", 3))
    )


_RVplsPimSnpgIfGrpSrcJPRptState_Type.__name__ = "Integer32"
_RVplsPimSnpgIfGrpSrcJPRptState_Object = MibTableColumn
rVplsPimSnpgIfGrpSrcJPRptState = _RVplsPimSnpgIfGrpSrcJPRptState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 6, 5, 1, 8),
    _RVplsPimSnpgIfGrpSrcJPRptState_Type()
)
rVplsPimSnpgIfGrpSrcJPRptState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rVplsPimSnpgIfGrpSrcJPRptState.setStatus("current")
_RVplsPimSnpgIfGrpSrcRptPrnPndTmr_Type = Unsigned32
_RVplsPimSnpgIfGrpSrcRptPrnPndTmr_Object = MibTableColumn
rVplsPimSnpgIfGrpSrcRptPrnPndTmr = _RVplsPimSnpgIfGrpSrcRptPrnPndTmr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 6, 5, 1, 9),
    _RVplsPimSnpgIfGrpSrcRptPrnPndTmr_Type()
)
rVplsPimSnpgIfGrpSrcRptPrnPndTmr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rVplsPimSnpgIfGrpSrcRptPrnPndTmr.setStatus("current")
if mibBuilder.loadTexts:
    rVplsPimSnpgIfGrpSrcRptPrnPndTmr.setUnits("seconds")
_RVplsPimSnpgIfGrpSrcRptJPTimer_Type = Unsigned32
_RVplsPimSnpgIfGrpSrcRptJPTimer_Object = MibTableColumn
rVplsPimSnpgIfGrpSrcRptJPTimer = _RVplsPimSnpgIfGrpSrcRptJPTimer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 6, 5, 1, 10),
    _RVplsPimSnpgIfGrpSrcRptJPTimer_Type()
)
rVplsPimSnpgIfGrpSrcRptJPTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rVplsPimSnpgIfGrpSrcRptJPTimer.setStatus("current")
if mibBuilder.loadTexts:
    rVplsPimSnpgIfGrpSrcRptJPTimer.setUnits("seconds")
_RVplsPimSnpgIfGrpSrcUpTime_Type = Unsigned32
_RVplsPimSnpgIfGrpSrcUpTime_Object = MibTableColumn
rVplsPimSnpgIfGrpSrcUpTime = _RVplsPimSnpgIfGrpSrcUpTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 6, 5, 1, 11),
    _RVplsPimSnpgIfGrpSrcUpTime_Type()
)
rVplsPimSnpgIfGrpSrcUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rVplsPimSnpgIfGrpSrcUpTime.setStatus("current")
if mibBuilder.loadTexts:
    rVplsPimSnpgIfGrpSrcUpTime.setUnits("seconds")
_RVplsPimSnpgGrpSrcIfTable_Object = MibTable
rVplsPimSnpgGrpSrcIfTable = _RVplsPimSnpgGrpSrcIfTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 6, 6)
)
if mibBuilder.loadTexts:
    rVplsPimSnpgGrpSrcIfTable.setStatus("current")
_RVplsPimSnpgGrpSrcIfEntry_Object = MibTableRow
rVplsPimSnpgGrpSrcIfEntry = _RVplsPimSnpgGrpSrcIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 6, 6, 1)
)
rVplsPimSnpgGrpSrcIfEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-PIM-SNOOPING-MIB", "rVplsPimSnpgGrpSrcGrpAddrType"),
    (0, "TIMETRA-PIM-SNOOPING-MIB", "rVplsPimSnpgGrpSrcGroupAddress"),
    (0, "TIMETRA-PIM-SNOOPING-MIB", "rVplsPimSnpgGrpSrcSrcAddrType"),
    (0, "TIMETRA-PIM-SNOOPING-MIB", "rVplsPimSnpgGrpSrcSourceAddress"),
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-VRTR-MIB", "vRtrIfIndex"),
)
if mibBuilder.loadTexts:
    rVplsPimSnpgGrpSrcIfEntry.setStatus("current")
_RVplsPimSnpgGrpSrcGrpAddrType_Type = InetAddressType
_RVplsPimSnpgGrpSrcGrpAddrType_Object = MibTableColumn
rVplsPimSnpgGrpSrcGrpAddrType = _RVplsPimSnpgGrpSrcGrpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 6, 6, 1, 1),
    _RVplsPimSnpgGrpSrcGrpAddrType_Type()
)
rVplsPimSnpgGrpSrcGrpAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rVplsPimSnpgGrpSrcGrpAddrType.setStatus("current")


class _RVplsPimSnpgGrpSrcGroupAddress_Type(InetAddress):
    """Custom type rVplsPimSnpgGrpSrcGroupAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_RVplsPimSnpgGrpSrcGroupAddress_Type.__name__ = "InetAddress"
_RVplsPimSnpgGrpSrcGroupAddress_Object = MibTableColumn
rVplsPimSnpgGrpSrcGroupAddress = _RVplsPimSnpgGrpSrcGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 6, 6, 1, 2),
    _RVplsPimSnpgGrpSrcGroupAddress_Type()
)
rVplsPimSnpgGrpSrcGroupAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rVplsPimSnpgGrpSrcGroupAddress.setStatus("current")
_RVplsPimSnpgGrpSrcSrcAddrType_Type = InetAddressType
_RVplsPimSnpgGrpSrcSrcAddrType_Object = MibTableColumn
rVplsPimSnpgGrpSrcSrcAddrType = _RVplsPimSnpgGrpSrcSrcAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 6, 6, 1, 3),
    _RVplsPimSnpgGrpSrcSrcAddrType_Type()
)
rVplsPimSnpgGrpSrcSrcAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rVplsPimSnpgGrpSrcSrcAddrType.setStatus("current")


class _RVplsPimSnpgGrpSrcSourceAddress_Type(InetAddress):
    """Custom type rVplsPimSnpgGrpSrcSourceAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_RVplsPimSnpgGrpSrcSourceAddress_Type.__name__ = "InetAddress"
_RVplsPimSnpgGrpSrcSourceAddress_Object = MibTableColumn
rVplsPimSnpgGrpSrcSourceAddress = _RVplsPimSnpgGrpSrcSourceAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 6, 6, 1, 4),
    _RVplsPimSnpgGrpSrcSourceAddress_Type()
)
rVplsPimSnpgGrpSrcSourceAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rVplsPimSnpgGrpSrcSourceAddress.setStatus("current")


class _RVplsPimSnpgGrpSrcIfFlags_Type(Bits):
    """Custom type rVplsPimSnpgGrpSrcIfFlags based on Bits"""
    namedValues = NamedValues(
        *(("immediateOifList", 0),
          ("inheritedOifList", 1),
          ("inheritedRptOifList", 2),
          ("joined", 3),
          ("rpfPort", 4))
    )

_RVplsPimSnpgGrpSrcIfFlags_Type.__name__ = "Bits"
_RVplsPimSnpgGrpSrcIfFlags_Object = MibTableColumn
rVplsPimSnpgGrpSrcIfFlags = _RVplsPimSnpgGrpSrcIfFlags_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 6, 6, 1, 5),
    _RVplsPimSnpgGrpSrcIfFlags_Type()
)
rVplsPimSnpgGrpSrcIfFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rVplsPimSnpgGrpSrcIfFlags.setStatus("current")
_TmnxPimSnpgNotifyPrefix_ObjectIdentity = ObjectIdentity
tmnxPimSnpgNotifyPrefix = _TmnxPimSnpgNotifyPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 53)
)
_TmnxPimSnpgNotifications_ObjectIdentity = ObjectIdentity
tmnxPimSnpgNotifications = _TmnxPimSnpgNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 53, 0)
)
tmnxPimSnpgGeneralEntry.registerAugmentions(
    ("TIMETRA-PIM-SNOOPING-MIB",
     "tmnxPimSnpgGenStatsEntry")
)
tmnxPimSnpgGenStatsEntry.setIndexNames(*tmnxPimSnpgGeneralEntry.getIndexNames())
tmnxPimSnpgGrpSrcEntry.registerAugmentions(
    ("TIMETRA-PIM-SNOOPING-MIB",
     "tmnxPimSnpgGrpSrcStatsEntry")
)
tmnxPimSnpgGrpSrcStatsEntry.setIndexNames(*tmnxPimSnpgGrpSrcEntry.getIndexNames())
tmnxPimSnpgIfEntry.registerAugmentions(
    ("TIMETRA-PIM-SNOOPING-MIB",
     "tmnxPimSnpgIfStatsEntry")
)
tmnxPimSnpgIfStatsEntry.setIndexNames(*tmnxPimSnpgIfEntry.getIndexNames())
vxlanPimSnpgIfEntry.registerAugmentions(
    ("TIMETRA-PIM-SNOOPING-MIB",
     "vxlanPimSnpgIfStatsEntry")
)
vxlanPimSnpgIfStatsEntry.setIndexNames(*vxlanPimSnpgIfEntry.getIndexNames())
eMplsPimSnpgIfEntry.registerAugmentions(
    ("TIMETRA-PIM-SNOOPING-MIB",
     "eMplsPimSnpgIfStatsEntry")
)
eMplsPimSnpgIfStatsEntry.setIndexNames(*eMplsPimSnpgIfEntry.getIndexNames())
rVplsPimSnpgIfEntry.registerAugmentions(
    ("TIMETRA-PIM-SNOOPING-MIB",
     "rVplsPimSnpgIfStatsEntry")
)
rVplsPimSnpgIfStatsEntry.setIndexNames(*rVplsPimSnpgIfEntry.getIndexNames())

# Managed Objects groups

tmnxPimSnpgGlobalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 53, 2, 1)
)
tmnxPimSnpgGlobalGroup.setObjects(
      *(("TIMETRA-PIM-SNOOPING-MIB", "tmnxPimSnpgGenTableLstChanged"),
        ("TIMETRA-PIM-SNOOPING-MIB", "tmnxPimSnpgGenRowStatus"),
        ("TIMETRA-PIM-SNOOPING-MIB", "tmnxPimSnpgGenRowLastChanged"),
        ("TIMETRA-PIM-SNOOPING-MIB", "tmnxPimSnpgGenAdminState"),
        ("TIMETRA-PIM-SNOOPING-MIB", "tmnxPimSnpgGenOperState"),
        ("TIMETRA-PIM-SNOOPING-MIB", "tmnxPimSnpgGenHoldTime"),
        ("TIMETRA-PIM-SNOOPING-MIB", "tmnxPimSnpgGenDRType"),
        ("TIMETRA-PIM-SNOOPING-MIB", "tmnxPimSnpgGenDR"),
        ("TIMETRA-PIM-SNOOPING-MIB", "tmnxPimSnpgGenTrackingSupport"),
        ("TIMETRA-PIM-SNOOPING-MIB", "tmnxPimSnpgGenUpTime"),
        ("TIMETRA-PIM-SNOOPING-MIB", "tmnxPimSnpgGenMode"),
        ("TIMETRA-PIM-SNOOPING-MIB", "tmnxPimSnpgGenGroupPolicy1"),
        ("TIMETRA-PIM-SNOOPING-MIB", "tmnxPimSnpgGenGroupPolicy2"),
        ("TIMETRA-PIM-SNOOPING-MIB", "tmnxPimSnpgGenGroupPolicy3"),
        ("TIMETRA-PIM-SNOOPING-MIB", "tmnxPimSnpgGenGroupPolicy4"),
        ("TIMETRA-PIM-SNOOPING-MIB", "tmnxPimSnpgGenGroupPolicy5"),
        ("TIMETRA-PIM-SNOOPING-MIB", "tmnxPimSnpgGrpSrcRpfNbrAddrType"),
        ("TIMETRA-PIM-SNOOPING-MIB", "tmnxPimSnpgGrpSrcRpfNbrAddr"),
        ("TIMETRA-PIM-SNOOPING-MIB", "tmnxPimSnpgGrpSrcRpfIfIndex"),
        ("TIMETRA-PIM-SNOOPING-MIB", "tmnxPimSnpgGrpSrcRptRpfNbrAdrTp"),
        ("TIMETRA-PIM-SNOOPING-MIB", "tmnxPimSnpgGrpSrcRptRpfNbrAddr"),
        ("TIMETRA-PIM-SNOOPING-MIB", "tmnxPimSnpgGrpSrcUstrmJpState"),
        ("TIMETRA-PIM-SNOOPING-MIB", "tmnxPimSnpgGrpSrcUstrmJpTimer"),
        ("TIMETRA-PIM-SNOOPING-MIB", "tmnxPimSnpgGrpSrcUstrmRptJpSt"),
        ("TIMETRA-PIM-SNOOPING-MIB", "tmnxPimSnpgGrpSrcUstrmRptOvdTmr"),
        ("TIMETRA-PIM-SNOOPING-MIB", "tmnxPimSnpgGrpSrcNumJoinOif"),
        ("TIMETRA-PIM-SNOOPING-MIB", "tmnxPimSnpgGrpSrcNumImdiateOif"),
        ("TIMETRA-PIM-SNOOPING-MIB", "tmnxPimSnpgGrpSrcNumInhritedOif"),
        ("TIMETRA-PIM-SNOOPING-MIB", "tmnxPimSnpgGrpSrcNumInherRptOif"),
        ("TIMETRA-PIM-SNOOPING-MIB", "tmnxPimSnpgGrpSrcNumIif"),
        ("TIMETRA-PIM-SNOOPING-MIB", "tmnxPimSnpgGrpSrcUpTime"),
        ("TIMETRA-PIM-SNOOPING-MIB", "tmnxPimSnpgGrpSrcIfFlags"),
        ("TIMETRA-PIM-SNOOPING-MIB", "tmnxPimSnpgGenStatsStarGTypes"),
        ("TIMETRA-PIM-SNOOPING-MIB", "tmnxPimSnpgGenStatsSGTypes"),
        ("TIMETRA-PIM-SNOOPING-MIB", "tmnxPimSnpgGrpSrcStatsFwdedPkts"),
        ("TIMETRA-PIM-SNOOPING-MIB", "tmnxPimSnpgGrpSrcStatsFwdedOct"))
)
if mibBuilder.loadTexts:
    tmnxPimSnpgGlobalGroup.setStatus("current")

tmnxPimSnpgIfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 53, 2, 2)
)
tmnxPimSnpgIfGroup.setObjects(
      *(("TIMETRA-PIM-SNOOPING-MIB", "tmnxPimSnpgIfTableLastChanged"),
        ("TIMETRA-PIM-SNOOPING-MIB", "tmnxPimSnpgIfLastChangeTime"),
        ("TIMETRA-PIM-SNOOPING-MIB", "tmnxPimSnpgIfOperState"),
        ("TIMETRA-PIM-SNOOPING-MIB", "tmnxPimSnpgIfUpTime"),
        ("TIMETRA-PIM-SNOOPING-MIB", "tmnxPimSnpgIfMaxGroups"),
        ("TIMETRA-PIM-SNOOPING-MIB", "tmnxPimSnpgIfCurrentGroups"),
        ("TIMETRA-PIM-SNOOPING-MIB", "tmnxPimSnpgIfMaxGroupsTillNow"),
        ("TIMETRA-PIM-SNOOPING-MIB", "tmnxPimSnpgIfNbrUpTime"),
        ("TIMETRA-PIM-SNOOPING-MIB", "tmnxPimSnpgIfNbrExpiryTime"),
        ("TIMETRA-PIM-SNOOPING-MIB", "tmnxPimSnpgIfNbrGenId"),
        ("TIMETRA-PIM-SNOOPING-MIB", "tmnxPimSnpgIfNbrDrPriority"),
        ("TIMETRA-PIM-SNOOPING-MIB", "tmnxPimSnpgIfNbrDrPriorPresent"),
        ("TIMETRA-PIM-SNOOPING-MIB", "tmnxPimSnpgIfNbrLanDelay"),
        ("TIMETRA-PIM-SNOOPING-MIB", "tmnxPimSnpgIfNbrLanDlayPrsnt"),
        ("TIMETRA-PIM-SNOOPING-MIB", "tmnxPimSnpgIfNbrTrckngSpprt"),
        ("TIMETRA-PIM-SNOOPING-MIB", "tmnxPimSnpgIfNbrHoldTime"),
        ("TIMETRA-PIM-SNOOPING-MIB", "tmnxPimSnpgIfNbrOvrdeIntrvl"),
        ("TIMETRA-PIM-SNOOPING-MIB", "tmnxPimSnpgIfGrpSrcJPState"),
        ("TIMETRA-PIM-SNOOPING-MIB", "tmnxPimSnpgIfGrpSrcPrunePendTmr"),
        ("TIMETRA-PIM-SNOOPING-MIB", "tmnxPimSnpgIfGrpSrcJPTimer"),
        ("TIMETRA-PIM-SNOOPING-MIB", "tmnxPimSnpgIfGrpSrcJPRptState"),
        ("TIMETRA-PIM-SNOOPING-MIB", "tmnxPimSnpgIfGrpSrcRptPrnPndTmr"),
        ("TIMETRA-PIM-SNOOPING-MIB", "tmnxPimSnpgIfGrpSrcRptJPTimer"),
        ("TIMETRA-PIM-SNOOPING-MIB", "tmnxPimSnpgIfGrpSrcUpTime"),
        ("TIMETRA-PIM-SNOOPING-MIB", "tmnxPimSnpgIfTxPkts"),
        ("TIMETRA-PIM-SNOOPING-MIB", "tmnxPimSnpgIfRxPkts"),
        ("TIMETRA-PIM-SNOOPING-MIB", "tmnxPimSnpgIfRxHellos"),
        ("TIMETRA-PIM-SNOOPING-MIB", "tmnxPimSnpgIfRxHellosDropped"),
        ("TIMETRA-PIM-SNOOPING-MIB", "tmnxPimSnpgIfRxNbrUnknown"),
        ("TIMETRA-PIM-SNOOPING-MIB", "tmnxPimSnpgIfRxBadChecksumDscrd"),
        ("TIMETRA-PIM-SNOOPING-MIB", "tmnxPimSnpgIfRxBadVersionDscrd"),
        ("TIMETRA-PIM-SNOOPING-MIB", "tmnxPimSnpgIfRxBadEncodings"),
        ("TIMETRA-PIM-SNOOPING-MIB", "tmnxPimSnpgIfStarGTypes"),
        ("TIMETRA-PIM-SNOOPING-MIB", "tmnxPimSnpgIfSGTypes"),
        ("TIMETRA-PIM-SNOOPING-MIB", "tmnxPimSnpgIfJoinPolicyDrops"),
        ("TIMETRA-PIM-SNOOPING-MIB", "tmnxPimSnpgIfTxJoinPrunes"),
        ("TIMETRA-PIM-SNOOPING-MIB", "tmnxPimSnpgIfRxJoinPrunes"),
        ("TIMETRA-PIM-SNOOPING-MIB", "tmnxPimSnpgIfRxJoinPruneErrs"))
)
if mibBuilder.loadTexts:
    tmnxPimSnpgIfGroup.setStatus("current")

tmnxPimSnpgIfSecNbrV6v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 53, 2, 4)
)
tmnxPimSnpgIfSecNbrV6v0Group.setObjects(
      *(("TIMETRA-PIM-SNOOPING-MIB", "tmnxPimSnpgIfSecNbrTblLstChanged"),
        ("TIMETRA-PIM-SNOOPING-MIB", "tmnxPimSnpgIfSecNbrAddrType"),
        ("TIMETRA-PIM-SNOOPING-MIB", "tmnxPimSnpgIfSecNbrAddress"))
)
if mibBuilder.loadTexts:
    tmnxPimSnpgIfSecNbrV6v0Group.setStatus("current")

tmnxPimSnpgIfV14v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 53, 2, 5)
)
tmnxPimSnpgIfV14v0Group.setObjects(
    ("TIMETRA-PIM-SNOOPING-MIB", "tmnxPimSnpgIfPwFwding")
)
if mibBuilder.loadTexts:
    tmnxPimSnpgIfV14v0Group.setStatus("current")

tmnxPimSnpgVxlanIfV15v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 53, 4, 1)
)
tmnxPimSnpgVxlanIfV15v0Group.setObjects(
      *(("TIMETRA-PIM-SNOOPING-MIB", "vxlanPimSnpgIfLastChangeTime"),
        ("TIMETRA-PIM-SNOOPING-MIB", "vxlanPimSnpgIfOperState"),
        ("TIMETRA-PIM-SNOOPING-MIB", "vxlanPimSnpgIfUpTime"),
        ("TIMETRA-PIM-SNOOPING-MIB", "vxlanPimSnpgIfCurrentGroups"),
        ("TIMETRA-PIM-SNOOPING-MIB", "vxlanPimSnpgIfMaxGroupsTillNow"),
        ("TIMETRA-PIM-SNOOPING-MIB", "vxlanPimSnpgIfPwFwding"),
        ("TIMETRA-PIM-SNOOPING-MIB", "vxlanPimSnpgIfTxPkts"),
        ("TIMETRA-PIM-SNOOPING-MIB", "vxlanPimSnpgIfRxPkts"),
        ("TIMETRA-PIM-SNOOPING-MIB", "vxlanPimSnpgIfRxHellos"),
        ("TIMETRA-PIM-SNOOPING-MIB", "vxlanPimSnpgIfRxHellosDropped"),
        ("TIMETRA-PIM-SNOOPING-MIB", "vxlanPimSnpgIfRxNbrUnknown"),
        ("TIMETRA-PIM-SNOOPING-MIB", "vxlanPimSnpgIfRxBadChecksumDscrd"),
        ("TIMETRA-PIM-SNOOPING-MIB", "vxlanPimSnpgIfRxBadVersionDscrd"),
        ("TIMETRA-PIM-SNOOPING-MIB", "vxlanPimSnpgIfRxBadEncodings"),
        ("TIMETRA-PIM-SNOOPING-MIB", "vxlanPimSnpgIfStarGTypes"),
        ("TIMETRA-PIM-SNOOPING-MIB", "vxlanPimSnpgIfSGTypes"),
        ("TIMETRA-PIM-SNOOPING-MIB", "vxlanPimSnpgIfJoinPolicyDrops"),
        ("TIMETRA-PIM-SNOOPING-MIB", "vxlanPimSnpgIfTxJoinPrunes"),
        ("TIMETRA-PIM-SNOOPING-MIB", "vxlanPimSnpgIfRxJoinPrunes"),
        ("TIMETRA-PIM-SNOOPING-MIB", "vxlanPimSnpgIfRxJoinPruneErrs"),
        ("TIMETRA-PIM-SNOOPING-MIB", "vxlanPimSnpgIfNbrUpTime"),
        ("TIMETRA-PIM-SNOOPING-MIB", "vxlanPimSnpgIfNbrExpiryTime"),
        ("TIMETRA-PIM-SNOOPING-MIB", "vxlanPimSnpgIfNbrGenId"),
        ("TIMETRA-PIM-SNOOPING-MIB", "vxlanPimSnpgIfNbrDrPriority"),
        ("TIMETRA-PIM-SNOOPING-MIB", "vxlanPimSnpgIfNbrDrPriorPresent"),
        ("TIMETRA-PIM-SNOOPING-MIB", "vxlanPimSnpgIfNbrLanDelay"),
        ("TIMETRA-PIM-SNOOPING-MIB", "vxlanPimSnpgIfNbrLanDlayPrsnt"),
        ("TIMETRA-PIM-SNOOPING-MIB", "vxlanPimSnpgIfNbrTrckngSpprt"),
        ("TIMETRA-PIM-SNOOPING-MIB", "vxlanPimSnpgIfNbrHoldTime"),
        ("TIMETRA-PIM-SNOOPING-MIB", "vxlanPimSnpgIfNbrOvrdeIntrvl"),
        ("TIMETRA-PIM-SNOOPING-MIB", "vxlanPimSnpgIfSecNbrAddrType"),
        ("TIMETRA-PIM-SNOOPING-MIB", "vxlanPimSnpgIfSecNbrAddress"),
        ("TIMETRA-PIM-SNOOPING-MIB", "vxlanPimSnpgIfGrpSrcJPState"),
        ("TIMETRA-PIM-SNOOPING-MIB", "vxlanPimSnpgIfGrpSrcPrunePendTmr"),
        ("TIMETRA-PIM-SNOOPING-MIB", "vxlanPimSnpgIfGrpSrcJPTimer"),
        ("TIMETRA-PIM-SNOOPING-MIB", "vxlanPimSnpgIfGrpSrcJPRptState"),
        ("TIMETRA-PIM-SNOOPING-MIB", "vxlanPimSnpgIfGrpSrcRptPrnPndTmr"),
        ("TIMETRA-PIM-SNOOPING-MIB", "vxlanPimSnpgIfGrpSrcRptJPTimer"),
        ("TIMETRA-PIM-SNOOPING-MIB", "vxlanPimSnpgIfGrpSrcUpTime"),
        ("TIMETRA-PIM-SNOOPING-MIB", "vxlanPimSnpgGrpSrcIfFlags"))
)
if mibBuilder.loadTexts:
    tmnxPimSnpgVxlanIfV15v0Group.setStatus("current")

tmnxPimSnpgEMplsIfV15v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 53, 6, 1)
)
tmnxPimSnpgEMplsIfV15v0Group.setObjects(
      *(("TIMETRA-PIM-SNOOPING-MIB", "eMplsPimSnpgIfLastChangeTime"),
        ("TIMETRA-PIM-SNOOPING-MIB", "eMplsPimSnpgIfOperState"),
        ("TIMETRA-PIM-SNOOPING-MIB", "eMplsPimSnpgIfUpTime"),
        ("TIMETRA-PIM-SNOOPING-MIB", "eMplsPimSnpgIfCurrentGroups"),
        ("TIMETRA-PIM-SNOOPING-MIB", "eMplsPimSnpgIfMaxGroupsTillNow"),
        ("TIMETRA-PIM-SNOOPING-MIB", "eMplsPimSnpgIfPwFwding"),
        ("TIMETRA-PIM-SNOOPING-MIB", "eMplsPimSnpgIfTxPkts"),
        ("TIMETRA-PIM-SNOOPING-MIB", "eMplsPimSnpgIfRxPkts"),
        ("TIMETRA-PIM-SNOOPING-MIB", "eMplsPimSnpgIfRxHellos"),
        ("TIMETRA-PIM-SNOOPING-MIB", "eMplsPimSnpgIfRxHellosDropped"),
        ("TIMETRA-PIM-SNOOPING-MIB", "eMplsPimSnpgIfRxNbrUnknown"),
        ("TIMETRA-PIM-SNOOPING-MIB", "eMplsPimSnpgIfRxBadChecksumDscrd"),
        ("TIMETRA-PIM-SNOOPING-MIB", "eMplsPimSnpgIfRxBadVersionDscrd"),
        ("TIMETRA-PIM-SNOOPING-MIB", "eMplsPimSnpgIfRxBadEncodings"),
        ("TIMETRA-PIM-SNOOPING-MIB", "eMplsPimSnpgIfStarGTypes"),
        ("TIMETRA-PIM-SNOOPING-MIB", "eMplsPimSnpgIfSGTypes"),
        ("TIMETRA-PIM-SNOOPING-MIB", "eMplsPimSnpgIfJoinPolicyDrops"),
        ("TIMETRA-PIM-SNOOPING-MIB", "eMplsPimSnpgIfTxJoinPrunes"),
        ("TIMETRA-PIM-SNOOPING-MIB", "eMplsPimSnpgIfRxJoinPrunes"),
        ("TIMETRA-PIM-SNOOPING-MIB", "eMplsPimSnpgIfRxJoinPruneErrs"),
        ("TIMETRA-PIM-SNOOPING-MIB", "eMplsPimSnpgIfNbrUpTime"),
        ("TIMETRA-PIM-SNOOPING-MIB", "eMplsPimSnpgIfNbrExpiryTime"),
        ("TIMETRA-PIM-SNOOPING-MIB", "eMplsPimSnpgIfNbrGenId"),
        ("TIMETRA-PIM-SNOOPING-MIB", "eMplsPimSnpgIfNbrDrPriority"),
        ("TIMETRA-PIM-SNOOPING-MIB", "eMplsPimSnpgIfNbrDrPriorPresent"),
        ("TIMETRA-PIM-SNOOPING-MIB", "eMplsPimSnpgIfNbrLanDelay"),
        ("TIMETRA-PIM-SNOOPING-MIB", "eMplsPimSnpgIfNbrLanDlayPrsnt"),
        ("TIMETRA-PIM-SNOOPING-MIB", "eMplsPimSnpgIfNbrTrckngSpprt"),
        ("TIMETRA-PIM-SNOOPING-MIB", "eMplsPimSnpgIfNbrHoldTime"),
        ("TIMETRA-PIM-SNOOPING-MIB", "eMplsPimSnpgIfNbrOvrdeIntrvl"),
        ("TIMETRA-PIM-SNOOPING-MIB", "eMplsPimSnpgIfSecNbrAddrType"),
        ("TIMETRA-PIM-SNOOPING-MIB", "eMplsPimSnpgIfSecNbrAddress"),
        ("TIMETRA-PIM-SNOOPING-MIB", "eMplsPimSnpgIfGrpSrcJPState"),
        ("TIMETRA-PIM-SNOOPING-MIB", "eMplsPimSnpgIfGrpSrcPrunePendTmr"),
        ("TIMETRA-PIM-SNOOPING-MIB", "eMplsPimSnpgIfGrpSrcJPTimer"),
        ("TIMETRA-PIM-SNOOPING-MIB", "eMplsPimSnpgIfGrpSrcJPRptState"),
        ("TIMETRA-PIM-SNOOPING-MIB", "eMplsPimSnpgIfGrpSrcRptPrnPndTmr"),
        ("TIMETRA-PIM-SNOOPING-MIB", "eMplsPimSnpgIfGrpSrcRptJPTimer"),
        ("TIMETRA-PIM-SNOOPING-MIB", "eMplsPimSnpgIfGrpSrcUpTime"),
        ("TIMETRA-PIM-SNOOPING-MIB", "eMplsPimSnpgGrpSrcIfFlags"))
)
if mibBuilder.loadTexts:
    tmnxPimSnpgEMplsIfV15v0Group.setStatus("current")

tmnxPimSnpgRvplsIfV16v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 53, 8, 1)
)
tmnxPimSnpgRvplsIfV16v0Group.setObjects(
      *(("TIMETRA-PIM-SNOOPING-MIB", "rVplsPimSnpgIfLastChangeTime"),
        ("TIMETRA-PIM-SNOOPING-MIB", "rVplsPimSnpgIfOperState"),
        ("TIMETRA-PIM-SNOOPING-MIB", "rVplsPimSnpgIfUpTime"),
        ("TIMETRA-PIM-SNOOPING-MIB", "rVplsPimSnpgIfCurrentGroups"),
        ("TIMETRA-PIM-SNOOPING-MIB", "rVplsPimSnpgIfMaxGroupsTillNow"),
        ("TIMETRA-PIM-SNOOPING-MIB", "rVplsPimSnpgIfPwFwding"),
        ("TIMETRA-PIM-SNOOPING-MIB", "rVplsPimSnpgIfTxPkts"),
        ("TIMETRA-PIM-SNOOPING-MIB", "rVplsPimSnpgIfRxPkts"),
        ("TIMETRA-PIM-SNOOPING-MIB", "rVplsPimSnpgIfRxHellos"),
        ("TIMETRA-PIM-SNOOPING-MIB", "rVplsPimSnpgIfRxHellosDropped"),
        ("TIMETRA-PIM-SNOOPING-MIB", "rVplsPimSnpgIfRxNbrUnknown"),
        ("TIMETRA-PIM-SNOOPING-MIB", "rVplsPimSnpgIfRxBadChecksumDscrd"),
        ("TIMETRA-PIM-SNOOPING-MIB", "rVplsPimSnpgIfRxBadVersionDscrd"),
        ("TIMETRA-PIM-SNOOPING-MIB", "rVplsPimSnpgIfRxBadEncodings"),
        ("TIMETRA-PIM-SNOOPING-MIB", "rVplsPimSnpgIfStarGTypes"),
        ("TIMETRA-PIM-SNOOPING-MIB", "rVplsPimSnpgIfSGTypes"),
        ("TIMETRA-PIM-SNOOPING-MIB", "rVplsPimSnpgIfJoinPolicyDrops"),
        ("TIMETRA-PIM-SNOOPING-MIB", "rVplsPimSnpgIfTxJoinPrunes"),
        ("TIMETRA-PIM-SNOOPING-MIB", "rVplsPimSnpgIfRxJoinPrunes"),
        ("TIMETRA-PIM-SNOOPING-MIB", "rVplsPimSnpgIfRxJoinPruneErrs"),
        ("TIMETRA-PIM-SNOOPING-MIB", "rVplsPimSnpgIfNbrUpTime"),
        ("TIMETRA-PIM-SNOOPING-MIB", "rVplsPimSnpgIfNbrExpiryTime"),
        ("TIMETRA-PIM-SNOOPING-MIB", "rVplsPimSnpgIfNbrGenId"),
        ("TIMETRA-PIM-SNOOPING-MIB", "rVplsPimSnpgIfNbrDrPriority"),
        ("TIMETRA-PIM-SNOOPING-MIB", "rVplsPimSnpgIfNbrDrPriorPresent"),
        ("TIMETRA-PIM-SNOOPING-MIB", "rVplsPimSnpgIfNbrLanDelay"),
        ("TIMETRA-PIM-SNOOPING-MIB", "rVplsPimSnpgIfNbrLanDlayPrsnt"),
        ("TIMETRA-PIM-SNOOPING-MIB", "rVplsPimSnpgIfNbrTrckngSpprt"),
        ("TIMETRA-PIM-SNOOPING-MIB", "rVplsPimSnpgIfNbrHoldTime"),
        ("TIMETRA-PIM-SNOOPING-MIB", "rVplsPimSnpgIfNbrOvrdeIntrvl"),
        ("TIMETRA-PIM-SNOOPING-MIB", "rVplsPimSnpgIfSecNbrAddrType"),
        ("TIMETRA-PIM-SNOOPING-MIB", "rVplsPimSnpgIfSecNbrAddress"),
        ("TIMETRA-PIM-SNOOPING-MIB", "rVplsPimSnpgIfGrpSrcJPState"),
        ("TIMETRA-PIM-SNOOPING-MIB", "rVplsPimSnpgIfGrpSrcPrunePendTmr"),
        ("TIMETRA-PIM-SNOOPING-MIB", "rVplsPimSnpgIfGrpSrcJPTimer"),
        ("TIMETRA-PIM-SNOOPING-MIB", "rVplsPimSnpgIfGrpSrcJPRptState"),
        ("TIMETRA-PIM-SNOOPING-MIB", "rVplsPimSnpgIfGrpSrcRptPrnPndTmr"),
        ("TIMETRA-PIM-SNOOPING-MIB", "rVplsPimSnpgIfGrpSrcRptJPTimer"),
        ("TIMETRA-PIM-SNOOPING-MIB", "rVplsPimSnpgIfGrpSrcUpTime"),
        ("TIMETRA-PIM-SNOOPING-MIB", "rVplsPimSnpgGrpSrcIfFlags"))
)
if mibBuilder.loadTexts:
    tmnxPimSnpgRvplsIfV16v0Group.setStatus("current")


# Notification objects

tmnxPimSnpgIfNeighborLoss = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 53, 0, 1)
)
tmnxPimSnpgIfNeighborLoss.setObjects(
    ("TIMETRA-PIM-SNOOPING-MIB", "tmnxPimSnpgIfNbrUpTime")
)
if mibBuilder.loadTexts:
    tmnxPimSnpgIfNeighborLoss.setStatus(
        "current"
    )

tmnxPimSnpgIfNeighborUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 53, 0, 2)
)
tmnxPimSnpgIfNeighborUp.setObjects(
    ("TIMETRA-PIM-SNOOPING-MIB", "tmnxPimSnpgIfNbrUpTime")
)
if mibBuilder.loadTexts:
    tmnxPimSnpgIfNeighborUp.setStatus(
        "current"
    )

tmnxPimSnpgSGLimitExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 53, 0, 3)
)
tmnxPimSnpgSGLimitExceeded.setObjects(
    ("TIMETRA-CHASSIS-MIB", "tmnxCardHwIndex")
)
if mibBuilder.loadTexts:
    tmnxPimSnpgSGLimitExceeded.setStatus(
        "current"
    )

tmnxPimSnpgSnoopModeChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 53, 0, 4)
)
tmnxPimSnpgSnoopModeChanged.setObjects(
      *(("TIMETRA-PIM-SNOOPING-MIB", "tmnxPimSnpgGenOperState"),
        ("TIMETRA-PIM-SNOOPING-MIB", "tmnxPimSnpgGenMode"))
)
if mibBuilder.loadTexts:
    tmnxPimSnpgSnoopModeChanged.setStatus(
        "current"
    )


# Notifications groups

tmnxPimSnpgNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 53, 2, 3)
)
tmnxPimSnpgNotificationGroup.setObjects(
      *(("TIMETRA-PIM-SNOOPING-MIB", "tmnxPimSnpgIfNeighborLoss"),
        ("TIMETRA-PIM-SNOOPING-MIB", "tmnxPimSnpgIfNeighborUp"),
        ("TIMETRA-PIM-SNOOPING-MIB", "tmnxPimSnpgSGLimitExceeded"),
        ("TIMETRA-PIM-SNOOPING-MIB", "tmnxPimSnpgSnoopModeChanged"))
)
if mibBuilder.loadTexts:
    tmnxPimSnpgNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

tmnxPimSnpgCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 53, 1, 1)
)
tmnxPimSnpgCompliance.setObjects(
      *(("TIMETRA-PIM-SNOOPING-MIB", "tmnxPimSnpgGlobalGroup"),
        ("TIMETRA-PIM-SNOOPING-MIB", "tmnxPimSnpgIfGroup"),
        ("TIMETRA-PIM-SNOOPING-MIB", "tmnxPimSnpgNotificationGroup"),
        ("TIMETRA-PIM-SNOOPING-MIB", "tmnxPimSnpgIfSecNbrV6v0Group"))
)
if mibBuilder.loadTexts:
    tmnxPimSnpgCompliance.setStatus(
        "current"
    )

tmnxPimSnpgComplianceV14v0 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 53, 1, 2)
)
tmnxPimSnpgComplianceV14v0.setObjects(
      *(("TIMETRA-PIM-SNOOPING-MIB", "tmnxPimSnpgGlobalGroup"),
        ("TIMETRA-PIM-SNOOPING-MIB", "tmnxPimSnpgIfGroup"),
        ("TIMETRA-PIM-SNOOPING-MIB", "tmnxPimSnpgNotificationGroup"),
        ("TIMETRA-PIM-SNOOPING-MIB", "tmnxPimSnpgIfSecNbrV6v0Group"),
        ("TIMETRA-PIM-SNOOPING-MIB", "tmnxPimSnpgIfV14v0Group"))
)
if mibBuilder.loadTexts:
    tmnxPimSnpgComplianceV14v0.setStatus(
        "current"
    )

tmnxPimSnpgVxlanComplianceV15v0 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 53, 3, 1)
)
tmnxPimSnpgVxlanComplianceV15v0.setObjects(
    ("TIMETRA-PIM-SNOOPING-MIB", "tmnxPimSnpgVxlanIfV15v0Group")
)
if mibBuilder.loadTexts:
    tmnxPimSnpgVxlanComplianceV15v0.setStatus(
        "current"
    )

tmnxPimSnpgEMplsComplianceV15v0 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 53, 5, 1)
)
tmnxPimSnpgEMplsComplianceV15v0.setObjects(
    ("TIMETRA-PIM-SNOOPING-MIB", "tmnxPimSnpgEMplsIfV15v0Group")
)
if mibBuilder.loadTexts:
    tmnxPimSnpgEMplsComplianceV15v0.setStatus(
        "current"
    )

tmnxPimSnpgRvplsComplianceV16v0 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 53, 7, 1)
)
tmnxPimSnpgRvplsComplianceV16v0.setObjects(
    ("TIMETRA-PIM-SNOOPING-MIB", "tmnxPimSnpgRvplsIfV16v0Group")
)
if mibBuilder.loadTexts:
    tmnxPimSnpgRvplsComplianceV16v0.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TIMETRA-PIM-SNOOPING-MIB",
    **{"TmnxPimSnpgOperState": TmnxPimSnpgOperState,
       "timetraPimSnoopingMIBModule": timetraPimSnoopingMIBModule,
       "tmnxPimSnpgConformance": tmnxPimSnpgConformance,
       "tmnxPimSnpgCompliances": tmnxPimSnpgCompliances,
       "tmnxPimSnpgCompliance": tmnxPimSnpgCompliance,
       "tmnxPimSnpgComplianceV14v0": tmnxPimSnpgComplianceV14v0,
       "tmnxPimSnpgGroups": tmnxPimSnpgGroups,
       "tmnxPimSnpgGlobalGroup": tmnxPimSnpgGlobalGroup,
       "tmnxPimSnpgIfGroup": tmnxPimSnpgIfGroup,
       "tmnxPimSnpgNotificationGroup": tmnxPimSnpgNotificationGroup,
       "tmnxPimSnpgIfSecNbrV6v0Group": tmnxPimSnpgIfSecNbrV6v0Group,
       "tmnxPimSnpgIfV14v0Group": tmnxPimSnpgIfV14v0Group,
       "tmnxPimSnpgVxlanCompliances": tmnxPimSnpgVxlanCompliances,
       "tmnxPimSnpgVxlanComplianceV15v0": tmnxPimSnpgVxlanComplianceV15v0,
       "tmnxPimSnpgVxlanGroups": tmnxPimSnpgVxlanGroups,
       "tmnxPimSnpgVxlanIfV15v0Group": tmnxPimSnpgVxlanIfV15v0Group,
       "tmnxPimSnpgEMplsCompliances": tmnxPimSnpgEMplsCompliances,
       "tmnxPimSnpgEMplsComplianceV15v0": tmnxPimSnpgEMplsComplianceV15v0,
       "tmnxPimSnpgEMplsGroups": tmnxPimSnpgEMplsGroups,
       "tmnxPimSnpgEMplsIfV15v0Group": tmnxPimSnpgEMplsIfV15v0Group,
       "tmnxPimSnpgRvplsCompliances": tmnxPimSnpgRvplsCompliances,
       "tmnxPimSnpgRvplsComplianceV16v0": tmnxPimSnpgRvplsComplianceV16v0,
       "tmnxPimSnpgRvplsIfGroups": tmnxPimSnpgRvplsIfGroups,
       "tmnxPimSnpgRvplsIfV16v0Group": tmnxPimSnpgRvplsIfV16v0Group,
       "tmnxPimSnpgObjs": tmnxPimSnpgObjs,
       "tmnxPimSnpgProtocolObjs": tmnxPimSnpgProtocolObjs,
       "tmnxPimSnpgGenTableLstChanged": tmnxPimSnpgGenTableLstChanged,
       "tmnxPimSnpgGeneralTable": tmnxPimSnpgGeneralTable,
       "tmnxPimSnpgGeneralEntry": tmnxPimSnpgGeneralEntry,
       "tmnxPimSnpgGenRowStatus": tmnxPimSnpgGenRowStatus,
       "tmnxPimSnpgGenRowLastChanged": tmnxPimSnpgGenRowLastChanged,
       "tmnxPimSnpgGenAdminState": tmnxPimSnpgGenAdminState,
       "tmnxPimSnpgGenOperState": tmnxPimSnpgGenOperState,
       "tmnxPimSnpgGenHoldTime": tmnxPimSnpgGenHoldTime,
       "tmnxPimSnpgGenDRType": tmnxPimSnpgGenDRType,
       "tmnxPimSnpgGenDR": tmnxPimSnpgGenDR,
       "tmnxPimSnpgGenTrackingSupport": tmnxPimSnpgGenTrackingSupport,
       "tmnxPimSnpgGenUpTime": tmnxPimSnpgGenUpTime,
       "tmnxPimSnpgGenMode": tmnxPimSnpgGenMode,
       "tmnxPimSnpgGenGroupPolicy1": tmnxPimSnpgGenGroupPolicy1,
       "tmnxPimSnpgGenGroupPolicy2": tmnxPimSnpgGenGroupPolicy2,
       "tmnxPimSnpgGenGroupPolicy3": tmnxPimSnpgGenGroupPolicy3,
       "tmnxPimSnpgGenGroupPolicy4": tmnxPimSnpgGenGroupPolicy4,
       "tmnxPimSnpgGenGroupPolicy5": tmnxPimSnpgGenGroupPolicy5,
       "tmnxPimSnpgGrpSrcTable": tmnxPimSnpgGrpSrcTable,
       "tmnxPimSnpgGrpSrcEntry": tmnxPimSnpgGrpSrcEntry,
       "tmnxPimSnpgGrpSrcGrpAddrType": tmnxPimSnpgGrpSrcGrpAddrType,
       "tmnxPimSnpgGrpSrcGroupAddress": tmnxPimSnpgGrpSrcGroupAddress,
       "tmnxPimSnpgGrpSrcSrcAddrType": tmnxPimSnpgGrpSrcSrcAddrType,
       "tmnxPimSnpgGrpSrcSourceAddress": tmnxPimSnpgGrpSrcSourceAddress,
       "tmnxPimSnpgGrpSrcRpfNbrAddrType": tmnxPimSnpgGrpSrcRpfNbrAddrType,
       "tmnxPimSnpgGrpSrcRpfNbrAddr": tmnxPimSnpgGrpSrcRpfNbrAddr,
       "tmnxPimSnpgGrpSrcRpfIfIndex": tmnxPimSnpgGrpSrcRpfIfIndex,
       "tmnxPimSnpgGrpSrcRptRpfNbrAdrTp": tmnxPimSnpgGrpSrcRptRpfNbrAdrTp,
       "tmnxPimSnpgGrpSrcRptRpfNbrAddr": tmnxPimSnpgGrpSrcRptRpfNbrAddr,
       "tmnxPimSnpgGrpSrcUstrmJpState": tmnxPimSnpgGrpSrcUstrmJpState,
       "tmnxPimSnpgGrpSrcUstrmJpTimer": tmnxPimSnpgGrpSrcUstrmJpTimer,
       "tmnxPimSnpgGrpSrcUstrmRptJpSt": tmnxPimSnpgGrpSrcUstrmRptJpSt,
       "tmnxPimSnpgGrpSrcUstrmRptOvdTmr": tmnxPimSnpgGrpSrcUstrmRptOvdTmr,
       "tmnxPimSnpgGrpSrcNumJoinOif": tmnxPimSnpgGrpSrcNumJoinOif,
       "tmnxPimSnpgGrpSrcNumImdiateOif": tmnxPimSnpgGrpSrcNumImdiateOif,
       "tmnxPimSnpgGrpSrcNumInhritedOif": tmnxPimSnpgGrpSrcNumInhritedOif,
       "tmnxPimSnpgGrpSrcNumInherRptOif": tmnxPimSnpgGrpSrcNumInherRptOif,
       "tmnxPimSnpgGrpSrcNumIif": tmnxPimSnpgGrpSrcNumIif,
       "tmnxPimSnpgGrpSrcUpTime": tmnxPimSnpgGrpSrcUpTime,
       "tmnxPimSnpgGrpSrcIfTable": tmnxPimSnpgGrpSrcIfTable,
       "tmnxPimSnpgGrpSrcIfEntry": tmnxPimSnpgGrpSrcIfEntry,
       "tmnxPimSnpgPortId": tmnxPimSnpgPortId,
       "tmnxPimSnpgEncapValue": tmnxPimSnpgEncapValue,
       "tmnxPimSnpgGrpSrcIfFlags": tmnxPimSnpgGrpSrcIfFlags,
       "tmnxPimSnpgGenStatsTable": tmnxPimSnpgGenStatsTable,
       "tmnxPimSnpgGenStatsEntry": tmnxPimSnpgGenStatsEntry,
       "tmnxPimSnpgGenStatsStarGTypes": tmnxPimSnpgGenStatsStarGTypes,
       "tmnxPimSnpgGenStatsSGTypes": tmnxPimSnpgGenStatsSGTypes,
       "tmnxPimSnpgGrpSrcStatsTable": tmnxPimSnpgGrpSrcStatsTable,
       "tmnxPimSnpgGrpSrcStatsEntry": tmnxPimSnpgGrpSrcStatsEntry,
       "tmnxPimSnpgGrpSrcStatsFwdedPkts": tmnxPimSnpgGrpSrcStatsFwdedPkts,
       "tmnxPimSnpgGrpSrcStatsFwdedOct": tmnxPimSnpgGrpSrcStatsFwdedOct,
       "tmnxPimSnpgIfObjs": tmnxPimSnpgIfObjs,
       "tmnxPimSnpgIfTableLastChanged": tmnxPimSnpgIfTableLastChanged,
       "tmnxPimSnpgIfTable": tmnxPimSnpgIfTable,
       "tmnxPimSnpgIfEntry": tmnxPimSnpgIfEntry,
       "tmnxPimSnpgIfLastChangeTime": tmnxPimSnpgIfLastChangeTime,
       "tmnxPimSnpgIfOperState": tmnxPimSnpgIfOperState,
       "tmnxPimSnpgIfUpTime": tmnxPimSnpgIfUpTime,
       "tmnxPimSnpgIfMaxGroups": tmnxPimSnpgIfMaxGroups,
       "tmnxPimSnpgIfCurrentGroups": tmnxPimSnpgIfCurrentGroups,
       "tmnxPimSnpgIfMaxGroupsTillNow": tmnxPimSnpgIfMaxGroupsTillNow,
       "tmnxPimSnpgIfPwFwding": tmnxPimSnpgIfPwFwding,
       "tmnxPimSnpgIfNbrTable": tmnxPimSnpgIfNbrTable,
       "tmnxPimSnpgIfNbrEntry": tmnxPimSnpgIfNbrEntry,
       "tmnxPimSnpgIfNbrAddrType": tmnxPimSnpgIfNbrAddrType,
       "tmnxPimSnpgIfNbrAddress": tmnxPimSnpgIfNbrAddress,
       "tmnxPimSnpgIfNbrUpTime": tmnxPimSnpgIfNbrUpTime,
       "tmnxPimSnpgIfNbrExpiryTime": tmnxPimSnpgIfNbrExpiryTime,
       "tmnxPimSnpgIfNbrGenId": tmnxPimSnpgIfNbrGenId,
       "tmnxPimSnpgIfNbrDrPriority": tmnxPimSnpgIfNbrDrPriority,
       "tmnxPimSnpgIfNbrDrPriorPresent": tmnxPimSnpgIfNbrDrPriorPresent,
       "tmnxPimSnpgIfNbrLanDelay": tmnxPimSnpgIfNbrLanDelay,
       "tmnxPimSnpgIfNbrLanDlayPrsnt": tmnxPimSnpgIfNbrLanDlayPrsnt,
       "tmnxPimSnpgIfNbrTrckngSpprt": tmnxPimSnpgIfNbrTrckngSpprt,
       "tmnxPimSnpgIfNbrHoldTime": tmnxPimSnpgIfNbrHoldTime,
       "tmnxPimSnpgIfNbrOvrdeIntrvl": tmnxPimSnpgIfNbrOvrdeIntrvl,
       "tmnxPimSnpgIfGrpSrcTable": tmnxPimSnpgIfGrpSrcTable,
       "tmnxPimSnpgIfGrpSrcEntry": tmnxPimSnpgIfGrpSrcEntry,
       "tmnxPimSnpgIfGrpSrcGrpAddrType": tmnxPimSnpgIfGrpSrcGrpAddrType,
       "tmnxPimSnpgIfGrpSrcGroupAddr": tmnxPimSnpgIfGrpSrcGroupAddr,
       "tmnxPimSnpgIfGrpSrcSrcAddrType": tmnxPimSnpgIfGrpSrcSrcAddrType,
       "tmnxPimSnpgIfGrpSrcSourceAddr": tmnxPimSnpgIfGrpSrcSourceAddr,
       "tmnxPimSnpgIfGrpSrcJPState": tmnxPimSnpgIfGrpSrcJPState,
       "tmnxPimSnpgIfGrpSrcPrunePendTmr": tmnxPimSnpgIfGrpSrcPrunePendTmr,
       "tmnxPimSnpgIfGrpSrcJPTimer": tmnxPimSnpgIfGrpSrcJPTimer,
       "tmnxPimSnpgIfGrpSrcJPRptState": tmnxPimSnpgIfGrpSrcJPRptState,
       "tmnxPimSnpgIfGrpSrcRptPrnPndTmr": tmnxPimSnpgIfGrpSrcRptPrnPndTmr,
       "tmnxPimSnpgIfGrpSrcRptJPTimer": tmnxPimSnpgIfGrpSrcRptJPTimer,
       "tmnxPimSnpgIfGrpSrcUpTime": tmnxPimSnpgIfGrpSrcUpTime,
       "tmnxPimSnpgIfStatsTable": tmnxPimSnpgIfStatsTable,
       "tmnxPimSnpgIfStatsEntry": tmnxPimSnpgIfStatsEntry,
       "tmnxPimSnpgIfTxPkts": tmnxPimSnpgIfTxPkts,
       "tmnxPimSnpgIfRxPkts": tmnxPimSnpgIfRxPkts,
       "tmnxPimSnpgIfRxHellos": tmnxPimSnpgIfRxHellos,
       "tmnxPimSnpgIfRxHellosDropped": tmnxPimSnpgIfRxHellosDropped,
       "tmnxPimSnpgIfRxNbrUnknown": tmnxPimSnpgIfRxNbrUnknown,
       "tmnxPimSnpgIfRxBadChecksumDscrd": tmnxPimSnpgIfRxBadChecksumDscrd,
       "tmnxPimSnpgIfRxBadVersionDscrd": tmnxPimSnpgIfRxBadVersionDscrd,
       "tmnxPimSnpgIfRxBadEncodings": tmnxPimSnpgIfRxBadEncodings,
       "tmnxPimSnpgIfStarGTypes": tmnxPimSnpgIfStarGTypes,
       "tmnxPimSnpgIfSGTypes": tmnxPimSnpgIfSGTypes,
       "tmnxPimSnpgIfJoinPolicyDrops": tmnxPimSnpgIfJoinPolicyDrops,
       "tmnxPimSnpgIfTxJoinPrunes": tmnxPimSnpgIfTxJoinPrunes,
       "tmnxPimSnpgIfRxJoinPrunes": tmnxPimSnpgIfRxJoinPrunes,
       "tmnxPimSnpgIfRxJoinPruneErrs": tmnxPimSnpgIfRxJoinPruneErrs,
       "tmnxPimSnpgIfSecNbrTblLstChanged": tmnxPimSnpgIfSecNbrTblLstChanged,
       "tmnxPimSnpgIfSecNbrTable": tmnxPimSnpgIfSecNbrTable,
       "tmnxPimSnpgIfSecNbrEntry": tmnxPimSnpgIfSecNbrEntry,
       "tmnxPimSnpgIfSecNbrAddrType": tmnxPimSnpgIfSecNbrAddrType,
       "tmnxPimSnpgIfSecNbrAddress": tmnxPimSnpgIfSecNbrAddress,
       "tmnxPimSnpgNotificationObjs": tmnxPimSnpgNotificationObjs,
       "tmnxPimSnpgVxlanIfObjs": tmnxPimSnpgVxlanIfObjs,
       "vxlanPimSnpgIfTable": vxlanPimSnpgIfTable,
       "vxlanPimSnpgIfEntry": vxlanPimSnpgIfEntry,
       "vxlanPimSnpgIfLastChangeTime": vxlanPimSnpgIfLastChangeTime,
       "vxlanPimSnpgIfOperState": vxlanPimSnpgIfOperState,
       "vxlanPimSnpgIfUpTime": vxlanPimSnpgIfUpTime,
       "vxlanPimSnpgIfCurrentGroups": vxlanPimSnpgIfCurrentGroups,
       "vxlanPimSnpgIfMaxGroupsTillNow": vxlanPimSnpgIfMaxGroupsTillNow,
       "vxlanPimSnpgIfPwFwding": vxlanPimSnpgIfPwFwding,
       "vxlanPimSnpgIfStatsTable": vxlanPimSnpgIfStatsTable,
       "vxlanPimSnpgIfStatsEntry": vxlanPimSnpgIfStatsEntry,
       "vxlanPimSnpgIfTxPkts": vxlanPimSnpgIfTxPkts,
       "vxlanPimSnpgIfRxPkts": vxlanPimSnpgIfRxPkts,
       "vxlanPimSnpgIfRxHellos": vxlanPimSnpgIfRxHellos,
       "vxlanPimSnpgIfRxHellosDropped": vxlanPimSnpgIfRxHellosDropped,
       "vxlanPimSnpgIfRxNbrUnknown": vxlanPimSnpgIfRxNbrUnknown,
       "vxlanPimSnpgIfRxBadChecksumDscrd": vxlanPimSnpgIfRxBadChecksumDscrd,
       "vxlanPimSnpgIfRxBadVersionDscrd": vxlanPimSnpgIfRxBadVersionDscrd,
       "vxlanPimSnpgIfRxBadEncodings": vxlanPimSnpgIfRxBadEncodings,
       "vxlanPimSnpgIfStarGTypes": vxlanPimSnpgIfStarGTypes,
       "vxlanPimSnpgIfSGTypes": vxlanPimSnpgIfSGTypes,
       "vxlanPimSnpgIfJoinPolicyDrops": vxlanPimSnpgIfJoinPolicyDrops,
       "vxlanPimSnpgIfTxJoinPrunes": vxlanPimSnpgIfTxJoinPrunes,
       "vxlanPimSnpgIfRxJoinPrunes": vxlanPimSnpgIfRxJoinPrunes,
       "vxlanPimSnpgIfRxJoinPruneErrs": vxlanPimSnpgIfRxJoinPruneErrs,
       "vxlanPimSnpgIfNbrTable": vxlanPimSnpgIfNbrTable,
       "vxlanPimSnpgIfNbrEntry": vxlanPimSnpgIfNbrEntry,
       "vxlanPimSnpgIfNbrAddrType": vxlanPimSnpgIfNbrAddrType,
       "vxlanPimSnpgIfNbrAddress": vxlanPimSnpgIfNbrAddress,
       "vxlanPimSnpgIfNbrUpTime": vxlanPimSnpgIfNbrUpTime,
       "vxlanPimSnpgIfNbrExpiryTime": vxlanPimSnpgIfNbrExpiryTime,
       "vxlanPimSnpgIfNbrGenId": vxlanPimSnpgIfNbrGenId,
       "vxlanPimSnpgIfNbrDrPriority": vxlanPimSnpgIfNbrDrPriority,
       "vxlanPimSnpgIfNbrDrPriorPresent": vxlanPimSnpgIfNbrDrPriorPresent,
       "vxlanPimSnpgIfNbrLanDelay": vxlanPimSnpgIfNbrLanDelay,
       "vxlanPimSnpgIfNbrLanDlayPrsnt": vxlanPimSnpgIfNbrLanDlayPrsnt,
       "vxlanPimSnpgIfNbrTrckngSpprt": vxlanPimSnpgIfNbrTrckngSpprt,
       "vxlanPimSnpgIfNbrHoldTime": vxlanPimSnpgIfNbrHoldTime,
       "vxlanPimSnpgIfNbrOvrdeIntrvl": vxlanPimSnpgIfNbrOvrdeIntrvl,
       "vxlanPimSnpgIfSecNbrTable": vxlanPimSnpgIfSecNbrTable,
       "vxlanPimSnpgIfSecNbrEntry": vxlanPimSnpgIfSecNbrEntry,
       "vxlanPimSnpgIfSecNbrAddrType": vxlanPimSnpgIfSecNbrAddrType,
       "vxlanPimSnpgIfSecNbrAddress": vxlanPimSnpgIfSecNbrAddress,
       "vxlanPimSnpgIfGrpSrcTable": vxlanPimSnpgIfGrpSrcTable,
       "vxlanPimSnpgIfGrpSrcEntry": vxlanPimSnpgIfGrpSrcEntry,
       "vxlanPimSnpgIfGrpSrcGrpAddrType": vxlanPimSnpgIfGrpSrcGrpAddrType,
       "vxlanPimSnpgIfGrpSrcGroupAddr": vxlanPimSnpgIfGrpSrcGroupAddr,
       "vxlanPimSnpgIfGrpSrcSrcAddrType": vxlanPimSnpgIfGrpSrcSrcAddrType,
       "vxlanPimSnpgIfGrpSrcSourceAddr": vxlanPimSnpgIfGrpSrcSourceAddr,
       "vxlanPimSnpgIfGrpSrcJPState": vxlanPimSnpgIfGrpSrcJPState,
       "vxlanPimSnpgIfGrpSrcPrunePendTmr": vxlanPimSnpgIfGrpSrcPrunePendTmr,
       "vxlanPimSnpgIfGrpSrcJPTimer": vxlanPimSnpgIfGrpSrcJPTimer,
       "vxlanPimSnpgIfGrpSrcJPRptState": vxlanPimSnpgIfGrpSrcJPRptState,
       "vxlanPimSnpgIfGrpSrcRptPrnPndTmr": vxlanPimSnpgIfGrpSrcRptPrnPndTmr,
       "vxlanPimSnpgIfGrpSrcRptJPTimer": vxlanPimSnpgIfGrpSrcRptJPTimer,
       "vxlanPimSnpgIfGrpSrcUpTime": vxlanPimSnpgIfGrpSrcUpTime,
       "vxlanPimSnpgGrpSrcIfTable": vxlanPimSnpgGrpSrcIfTable,
       "vxlanPimSnpgGrpSrcIfEntry": vxlanPimSnpgGrpSrcIfEntry,
       "vxlanPimSnpgGrpSrcGrpAddrType": vxlanPimSnpgGrpSrcGrpAddrType,
       "vxlanPimSnpgGrpSrcGroupAddress": vxlanPimSnpgGrpSrcGroupAddress,
       "vxlanPimSnpgGrpSrcSrcAddrType": vxlanPimSnpgGrpSrcSrcAddrType,
       "vxlanPimSnpgGrpSrcSourceAddress": vxlanPimSnpgGrpSrcSourceAddress,
       "vxlanPimSnpgGrpSrcIfFlags": vxlanPimSnpgGrpSrcIfFlags,
       "tmnxPimSnpgEMplsIfObjs": tmnxPimSnpgEMplsIfObjs,
       "eMplsPimSnpgIfTable": eMplsPimSnpgIfTable,
       "eMplsPimSnpgIfEntry": eMplsPimSnpgIfEntry,
       "eMplsPimSnpgIfLastChangeTime": eMplsPimSnpgIfLastChangeTime,
       "eMplsPimSnpgIfOperState": eMplsPimSnpgIfOperState,
       "eMplsPimSnpgIfUpTime": eMplsPimSnpgIfUpTime,
       "eMplsPimSnpgIfCurrentGroups": eMplsPimSnpgIfCurrentGroups,
       "eMplsPimSnpgIfMaxGroupsTillNow": eMplsPimSnpgIfMaxGroupsTillNow,
       "eMplsPimSnpgIfPwFwding": eMplsPimSnpgIfPwFwding,
       "eMplsPimSnpgIfStatsTable": eMplsPimSnpgIfStatsTable,
       "eMplsPimSnpgIfStatsEntry": eMplsPimSnpgIfStatsEntry,
       "eMplsPimSnpgIfTxPkts": eMplsPimSnpgIfTxPkts,
       "eMplsPimSnpgIfRxPkts": eMplsPimSnpgIfRxPkts,
       "eMplsPimSnpgIfRxHellos": eMplsPimSnpgIfRxHellos,
       "eMplsPimSnpgIfRxHellosDropped": eMplsPimSnpgIfRxHellosDropped,
       "eMplsPimSnpgIfRxNbrUnknown": eMplsPimSnpgIfRxNbrUnknown,
       "eMplsPimSnpgIfRxBadChecksumDscrd": eMplsPimSnpgIfRxBadChecksumDscrd,
       "eMplsPimSnpgIfRxBadVersionDscrd": eMplsPimSnpgIfRxBadVersionDscrd,
       "eMplsPimSnpgIfRxBadEncodings": eMplsPimSnpgIfRxBadEncodings,
       "eMplsPimSnpgIfStarGTypes": eMplsPimSnpgIfStarGTypes,
       "eMplsPimSnpgIfSGTypes": eMplsPimSnpgIfSGTypes,
       "eMplsPimSnpgIfJoinPolicyDrops": eMplsPimSnpgIfJoinPolicyDrops,
       "eMplsPimSnpgIfTxJoinPrunes": eMplsPimSnpgIfTxJoinPrunes,
       "eMplsPimSnpgIfRxJoinPrunes": eMplsPimSnpgIfRxJoinPrunes,
       "eMplsPimSnpgIfRxJoinPruneErrs": eMplsPimSnpgIfRxJoinPruneErrs,
       "eMplsPimSnpgIfNbrTable": eMplsPimSnpgIfNbrTable,
       "eMplsPimSnpgIfNbrEntry": eMplsPimSnpgIfNbrEntry,
       "eMplsPimSnpgIfNbrAddrType": eMplsPimSnpgIfNbrAddrType,
       "eMplsPimSnpgIfNbrAddress": eMplsPimSnpgIfNbrAddress,
       "eMplsPimSnpgIfNbrUpTime": eMplsPimSnpgIfNbrUpTime,
       "eMplsPimSnpgIfNbrExpiryTime": eMplsPimSnpgIfNbrExpiryTime,
       "eMplsPimSnpgIfNbrGenId": eMplsPimSnpgIfNbrGenId,
       "eMplsPimSnpgIfNbrDrPriority": eMplsPimSnpgIfNbrDrPriority,
       "eMplsPimSnpgIfNbrDrPriorPresent": eMplsPimSnpgIfNbrDrPriorPresent,
       "eMplsPimSnpgIfNbrLanDelay": eMplsPimSnpgIfNbrLanDelay,
       "eMplsPimSnpgIfNbrLanDlayPrsnt": eMplsPimSnpgIfNbrLanDlayPrsnt,
       "eMplsPimSnpgIfNbrTrckngSpprt": eMplsPimSnpgIfNbrTrckngSpprt,
       "eMplsPimSnpgIfNbrHoldTime": eMplsPimSnpgIfNbrHoldTime,
       "eMplsPimSnpgIfNbrOvrdeIntrvl": eMplsPimSnpgIfNbrOvrdeIntrvl,
       "eMplsPimSnpgIfSecNbrTable": eMplsPimSnpgIfSecNbrTable,
       "eMplsPimSnpgIfSecNbrEntry": eMplsPimSnpgIfSecNbrEntry,
       "eMplsPimSnpgIfSecNbrAddrType": eMplsPimSnpgIfSecNbrAddrType,
       "eMplsPimSnpgIfSecNbrAddress": eMplsPimSnpgIfSecNbrAddress,
       "eMplsPimSnpgIfGrpSrcTable": eMplsPimSnpgIfGrpSrcTable,
       "eMplsPimSnpgIfGrpSrcEntry": eMplsPimSnpgIfGrpSrcEntry,
       "eMplsPimSnpgIfGrpSrcGrpAddrType": eMplsPimSnpgIfGrpSrcGrpAddrType,
       "eMplsPimSnpgIfGrpSrcGroupAddr": eMplsPimSnpgIfGrpSrcGroupAddr,
       "eMplsPimSnpgIfGrpSrcSrcAddrType": eMplsPimSnpgIfGrpSrcSrcAddrType,
       "eMplsPimSnpgIfGrpSrcSourceAddr": eMplsPimSnpgIfGrpSrcSourceAddr,
       "eMplsPimSnpgIfGrpSrcJPState": eMplsPimSnpgIfGrpSrcJPState,
       "eMplsPimSnpgIfGrpSrcPrunePendTmr": eMplsPimSnpgIfGrpSrcPrunePendTmr,
       "eMplsPimSnpgIfGrpSrcJPTimer": eMplsPimSnpgIfGrpSrcJPTimer,
       "eMplsPimSnpgIfGrpSrcJPRptState": eMplsPimSnpgIfGrpSrcJPRptState,
       "eMplsPimSnpgIfGrpSrcRptPrnPndTmr": eMplsPimSnpgIfGrpSrcRptPrnPndTmr,
       "eMplsPimSnpgIfGrpSrcRptJPTimer": eMplsPimSnpgIfGrpSrcRptJPTimer,
       "eMplsPimSnpgIfGrpSrcUpTime": eMplsPimSnpgIfGrpSrcUpTime,
       "eMplsPimSnpgGrpSrcIfTable": eMplsPimSnpgGrpSrcIfTable,
       "eMplsPimSnpgGrpSrcIfEntry": eMplsPimSnpgGrpSrcIfEntry,
       "eMplsPimSnpgGrpSrcGrpAddrType": eMplsPimSnpgGrpSrcGrpAddrType,
       "eMplsPimSnpgGrpSrcGroupAddress": eMplsPimSnpgGrpSrcGroupAddress,
       "eMplsPimSnpgGrpSrcSrcAddrType": eMplsPimSnpgGrpSrcSrcAddrType,
       "eMplsPimSnpgGrpSrcSourceAddress": eMplsPimSnpgGrpSrcSourceAddress,
       "eMplsPimSnpgGrpSrcIfFlags": eMplsPimSnpgGrpSrcIfFlags,
       "tmnxPimSnpgRVplsIfObjs": tmnxPimSnpgRVplsIfObjs,
       "rVplsPimSnpgIfTable": rVplsPimSnpgIfTable,
       "rVplsPimSnpgIfEntry": rVplsPimSnpgIfEntry,
       "rVplsPimSnpgIfLastChangeTime": rVplsPimSnpgIfLastChangeTime,
       "rVplsPimSnpgIfOperState": rVplsPimSnpgIfOperState,
       "rVplsPimSnpgIfUpTime": rVplsPimSnpgIfUpTime,
       "rVplsPimSnpgIfCurrentGroups": rVplsPimSnpgIfCurrentGroups,
       "rVplsPimSnpgIfMaxGroupsTillNow": rVplsPimSnpgIfMaxGroupsTillNow,
       "rVplsPimSnpgIfPwFwding": rVplsPimSnpgIfPwFwding,
       "rVplsPimSnpgIfStatsTable": rVplsPimSnpgIfStatsTable,
       "rVplsPimSnpgIfStatsEntry": rVplsPimSnpgIfStatsEntry,
       "rVplsPimSnpgIfTxPkts": rVplsPimSnpgIfTxPkts,
       "rVplsPimSnpgIfRxPkts": rVplsPimSnpgIfRxPkts,
       "rVplsPimSnpgIfRxHellos": rVplsPimSnpgIfRxHellos,
       "rVplsPimSnpgIfRxHellosDropped": rVplsPimSnpgIfRxHellosDropped,
       "rVplsPimSnpgIfRxNbrUnknown": rVplsPimSnpgIfRxNbrUnknown,
       "rVplsPimSnpgIfRxBadChecksumDscrd": rVplsPimSnpgIfRxBadChecksumDscrd,
       "rVplsPimSnpgIfRxBadVersionDscrd": rVplsPimSnpgIfRxBadVersionDscrd,
       "rVplsPimSnpgIfRxBadEncodings": rVplsPimSnpgIfRxBadEncodings,
       "rVplsPimSnpgIfStarGTypes": rVplsPimSnpgIfStarGTypes,
       "rVplsPimSnpgIfSGTypes": rVplsPimSnpgIfSGTypes,
       "rVplsPimSnpgIfJoinPolicyDrops": rVplsPimSnpgIfJoinPolicyDrops,
       "rVplsPimSnpgIfTxJoinPrunes": rVplsPimSnpgIfTxJoinPrunes,
       "rVplsPimSnpgIfRxJoinPrunes": rVplsPimSnpgIfRxJoinPrunes,
       "rVplsPimSnpgIfRxJoinPruneErrs": rVplsPimSnpgIfRxJoinPruneErrs,
       "rVplsPimSnpgIfNbrTable": rVplsPimSnpgIfNbrTable,
       "rVplsPimSnpgIfNbrEntry": rVplsPimSnpgIfNbrEntry,
       "rVplsPimSnpgIfNbrAddrType": rVplsPimSnpgIfNbrAddrType,
       "rVplsPimSnpgIfNbrAddress": rVplsPimSnpgIfNbrAddress,
       "rVplsPimSnpgIfNbrUpTime": rVplsPimSnpgIfNbrUpTime,
       "rVplsPimSnpgIfNbrExpiryTime": rVplsPimSnpgIfNbrExpiryTime,
       "rVplsPimSnpgIfNbrGenId": rVplsPimSnpgIfNbrGenId,
       "rVplsPimSnpgIfNbrDrPriority": rVplsPimSnpgIfNbrDrPriority,
       "rVplsPimSnpgIfNbrDrPriorPresent": rVplsPimSnpgIfNbrDrPriorPresent,
       "rVplsPimSnpgIfNbrLanDelay": rVplsPimSnpgIfNbrLanDelay,
       "rVplsPimSnpgIfNbrLanDlayPrsnt": rVplsPimSnpgIfNbrLanDlayPrsnt,
       "rVplsPimSnpgIfNbrTrckngSpprt": rVplsPimSnpgIfNbrTrckngSpprt,
       "rVplsPimSnpgIfNbrHoldTime": rVplsPimSnpgIfNbrHoldTime,
       "rVplsPimSnpgIfNbrOvrdeIntrvl": rVplsPimSnpgIfNbrOvrdeIntrvl,
       "rVplsPimSnpgIfSecNbrTable": rVplsPimSnpgIfSecNbrTable,
       "rVplsPimSnpgIfSecNbrEntry": rVplsPimSnpgIfSecNbrEntry,
       "rVplsPimSnpgIfSecNbrAddrType": rVplsPimSnpgIfSecNbrAddrType,
       "rVplsPimSnpgIfSecNbrAddress": rVplsPimSnpgIfSecNbrAddress,
       "rVplsPimSnpgIfGrpSrcTable": rVplsPimSnpgIfGrpSrcTable,
       "rVplsPimSnpgIfGrpSrcEntry": rVplsPimSnpgIfGrpSrcEntry,
       "rVplsPimSnpgIfGrpSrcGrpAddrType": rVplsPimSnpgIfGrpSrcGrpAddrType,
       "rVplsPimSnpgIfGrpSrcGroupAddr": rVplsPimSnpgIfGrpSrcGroupAddr,
       "rVplsPimSnpgIfGrpSrcSrcAddrType": rVplsPimSnpgIfGrpSrcSrcAddrType,
       "rVplsPimSnpgIfGrpSrcSourceAddr": rVplsPimSnpgIfGrpSrcSourceAddr,
       "rVplsPimSnpgIfGrpSrcJPState": rVplsPimSnpgIfGrpSrcJPState,
       "rVplsPimSnpgIfGrpSrcPrunePendTmr": rVplsPimSnpgIfGrpSrcPrunePendTmr,
       "rVplsPimSnpgIfGrpSrcJPTimer": rVplsPimSnpgIfGrpSrcJPTimer,
       "rVplsPimSnpgIfGrpSrcJPRptState": rVplsPimSnpgIfGrpSrcJPRptState,
       "rVplsPimSnpgIfGrpSrcRptPrnPndTmr": rVplsPimSnpgIfGrpSrcRptPrnPndTmr,
       "rVplsPimSnpgIfGrpSrcRptJPTimer": rVplsPimSnpgIfGrpSrcRptJPTimer,
       "rVplsPimSnpgIfGrpSrcUpTime": rVplsPimSnpgIfGrpSrcUpTime,
       "rVplsPimSnpgGrpSrcIfTable": rVplsPimSnpgGrpSrcIfTable,
       "rVplsPimSnpgGrpSrcIfEntry": rVplsPimSnpgGrpSrcIfEntry,
       "rVplsPimSnpgGrpSrcGrpAddrType": rVplsPimSnpgGrpSrcGrpAddrType,
       "rVplsPimSnpgGrpSrcGroupAddress": rVplsPimSnpgGrpSrcGroupAddress,
       "rVplsPimSnpgGrpSrcSrcAddrType": rVplsPimSnpgGrpSrcSrcAddrType,
       "rVplsPimSnpgGrpSrcSourceAddress": rVplsPimSnpgGrpSrcSourceAddress,
       "rVplsPimSnpgGrpSrcIfFlags": rVplsPimSnpgGrpSrcIfFlags,
       "tmnxPimSnpgNotifyPrefix": tmnxPimSnpgNotifyPrefix,
       "tmnxPimSnpgNotifications": tmnxPimSnpgNotifications,
       "tmnxPimSnpgIfNeighborLoss": tmnxPimSnpgIfNeighborLoss,
       "tmnxPimSnpgIfNeighborUp": tmnxPimSnpgIfNeighborUp,
       "tmnxPimSnpgSGLimitExceeded": tmnxPimSnpgSGLimitExceeded,
       "tmnxPimSnpgSnoopModeChanged": tmnxPimSnpgSnoopModeChanged}
)
