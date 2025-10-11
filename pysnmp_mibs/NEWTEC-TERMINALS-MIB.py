# SNMP MIB module (NEWTEC-TERMINALS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/newtec/NEWTEC-TERMINALS-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:04:14 2025
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

(ntcFunction,) = mibBuilder.importSymbols(
    "NEWTEC-MAIN-MIB",
    "ntcFunction")

(NtcEnable,) = mibBuilder.importSymbols(
    "NEWTEC-TC-MIB",
    "NtcEnable")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

ntcTerminals = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2700)
)
if mibBuilder.loadTexts:
    ntcTerminals.setRevisions(
        ("2018-02-02 09:00",
         "2015-04-13 07:00",
         "2014-07-15 08:00",
         "2014-02-03 12:00",
         "2013-01-08 12:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NtcTermsObjects_ObjectIdentity = ObjectIdentity
ntcTermsObjects = _NtcTermsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2700, 1)
)
if mibBuilder.loadTexts:
    ntcTermsObjects.setStatus("current")
_NtcTermsMon_ObjectIdentity = ObjectIdentity
ntcTermsMon = _NtcTermsMon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2700, 1, 1)
)
if mibBuilder.loadTexts:
    ntcTermsMon.setStatus("current")
_NtcTermsMonStateTable_Object = MibTable
ntcTermsMonStateTable = _NtcTermsMonStateTable_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2700, 1, 1, 1)
)
if mibBuilder.loadTexts:
    ntcTermsMonStateTable.setStatus("current")
_NtcTermsMonStateEntry_Object = MibTableRow
ntcTermsMonStateEntry = _NtcTermsMonStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2700, 1, 1, 1, 1)
)
ntcTermsMonStateEntry.setIndexNames(
    (0, "NEWTEC-TERMINALS-MIB", "ntcTermsMonStateInx"),
)
if mibBuilder.loadTexts:
    ntcTermsMonStateEntry.setStatus("current")
_NtcTermsMonStateInx_Type = Unsigned32
_NtcTermsMonStateInx_Object = MibTableColumn
ntcTermsMonStateInx = _NtcTermsMonStateInx_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2700, 1, 1, 1, 1, 1),
    _NtcTermsMonStateInx_Type()
)
ntcTermsMonStateInx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ntcTermsMonStateInx.setStatus("current")


class _NtcTermsMonName_Type(DisplayString):
    """Custom type ntcTermsMonName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_NtcTermsMonName_Type.__name__ = "DisplayString"
_NtcTermsMonName_Object = MibTableColumn
ntcTermsMonName = _NtcTermsMonName_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2700, 1, 1, 1, 1, 2),
    _NtcTermsMonName_Type()
)
ntcTermsMonName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcTermsMonName.setStatus("current")


class _NtcTermsMonState_Type(Integer32):
    """Custom type ntcTermsMonState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_NtcTermsMonState_Type.__name__ = "Integer32"
_NtcTermsMonState_Object = MibTableColumn
ntcTermsMonState = _NtcTermsMonState_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2700, 1, 1, 1, 1, 3),
    _NtcTermsMonState_Type()
)
ntcTermsMonState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcTermsMonState.setStatus("current")


class _NtcTermsMonEsNo_Type(Integer32):
    """Custom type ntcTermsMonEsNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1000, 3000),
    )


_NtcTermsMonEsNo_Type.__name__ = "Integer32"
_NtcTermsMonEsNo_Object = MibTableColumn
ntcTermsMonEsNo = _NtcTermsMonEsNo_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2700, 1, 1, 1, 1, 4),
    _NtcTermsMonEsNo_Type()
)
ntcTermsMonEsNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcTermsMonEsNo.setStatus("current")
if mibBuilder.loadTexts:
    ntcTermsMonEsNo.setUnits("dB")
_NtcTermsCfgStateTable_Object = MibTable
ntcTermsCfgStateTable = _NtcTermsCfgStateTable_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2700, 1, 2)
)
if mibBuilder.loadTexts:
    ntcTermsCfgStateTable.setStatus("current")
_NtcTermsCfgStateEntry_Object = MibTableRow
ntcTermsCfgStateEntry = _NtcTermsCfgStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2700, 1, 2, 1)
)
ntcTermsCfgStateEntry.setIndexNames(
    (0, "NEWTEC-TERMINALS-MIB", "ntcTermsCfgStateName"),
)
if mibBuilder.loadTexts:
    ntcTermsCfgStateEntry.setStatus("current")


class _NtcTermsCfgStateName_Type(DisplayString):
    """Custom type ntcTermsCfgStateName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_NtcTermsCfgStateName_Type.__name__ = "DisplayString"
_NtcTermsCfgStateName_Object = MibTableColumn
ntcTermsCfgStateName = _NtcTermsCfgStateName_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2700, 1, 2, 1, 1),
    _NtcTermsCfgStateName_Type()
)
ntcTermsCfgStateName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ntcTermsCfgStateName.setStatus("current")
_NtcTermsCfgStateRowStatus_Type = RowStatus
_NtcTermsCfgStateRowStatus_Object = MibTableColumn
ntcTermsCfgStateRowStatus = _NtcTermsCfgStateRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2700, 1, 2, 1, 2),
    _NtcTermsCfgStateRowStatus_Type()
)
ntcTermsCfgStateRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntcTermsCfgStateRowStatus.setStatus("current")


class _NtcTermsId_Type(Unsigned32):
    """Custom type ntcTermsId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65277),
    )


_NtcTermsId_Type.__name__ = "Unsigned32"
_NtcTermsId_Object = MibTableColumn
ntcTermsId = _NtcTermsId_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2700, 1, 2, 1, 3),
    _NtcTermsId_Type()
)
ntcTermsId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntcTermsId.setStatus("current")
_NtcTermsCtrlIpAddr_Type = IpAddress
_NtcTermsCtrlIpAddr_Object = MibTableColumn
ntcTermsCtrlIpAddr = _NtcTermsCtrlIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2700, 1, 2, 1, 4),
    _NtcTermsCtrlIpAddr_Type()
)
ntcTermsCtrlIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntcTermsCtrlIpAddr.setStatus("current")
_NtcTermsAdminState_Type = NtcEnable
_NtcTermsAdminState_Object = MibTableColumn
ntcTermsAdminState = _NtcTermsAdminState_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2700, 1, 2, 1, 5),
    _NtcTermsAdminState_Type()
)
ntcTermsAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntcTermsAdminState.setStatus("current")
_NtcTermsConformance_ObjectIdentity = ObjectIdentity
ntcTermsConformance = _NtcTermsConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2700, 2)
)
if mibBuilder.loadTexts:
    ntcTermsConformance.setStatus("current")
_NtcTermsConfCompliance_ObjectIdentity = ObjectIdentity
ntcTermsConfCompliance = _NtcTermsConfCompliance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2700, 2, 1)
)
if mibBuilder.loadTexts:
    ntcTermsConfCompliance.setStatus("current")
_NtcTermsConfGroup_ObjectIdentity = ObjectIdentity
ntcTermsConfGroup = _NtcTermsConfGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2700, 2, 2)
)
if mibBuilder.loadTexts:
    ntcTermsConfGroup.setStatus("current")

# Managed Objects groups

ntcTermsConfGrpV1Standard = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2700, 2, 2, 1)
)
ntcTermsConfGrpV1Standard.setObjects(
      *(("NEWTEC-TERMINALS-MIB", "ntcTermsMonName"),
        ("NEWTEC-TERMINALS-MIB", "ntcTermsMonState"),
        ("NEWTEC-TERMINALS-MIB", "ntcTermsMonEsNo"),
        ("NEWTEC-TERMINALS-MIB", "ntcTermsCfgStateRowStatus"),
        ("NEWTEC-TERMINALS-MIB", "ntcTermsId"),
        ("NEWTEC-TERMINALS-MIB", "ntcTermsCtrlIpAddr"),
        ("NEWTEC-TERMINALS-MIB", "ntcTermsAdminState"))
)
if mibBuilder.loadTexts:
    ntcTermsConfGrpV1Standard.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ntcTermsConfCompV1Standard = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 2700, 2, 1, 1)
)
ntcTermsConfCompV1Standard.setObjects(
    ("NEWTEC-TERMINALS-MIB", "ntcTermsConfGrpV1Standard")
)
if mibBuilder.loadTexts:
    ntcTermsConfCompV1Standard.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NEWTEC-TERMINALS-MIB",
    **{"ntcTerminals": ntcTerminals,
       "ntcTermsObjects": ntcTermsObjects,
       "ntcTermsMon": ntcTermsMon,
       "ntcTermsMonStateTable": ntcTermsMonStateTable,
       "ntcTermsMonStateEntry": ntcTermsMonStateEntry,
       "ntcTermsMonStateInx": ntcTermsMonStateInx,
       "ntcTermsMonName": ntcTermsMonName,
       "ntcTermsMonState": ntcTermsMonState,
       "ntcTermsMonEsNo": ntcTermsMonEsNo,
       "ntcTermsCfgStateTable": ntcTermsCfgStateTable,
       "ntcTermsCfgStateEntry": ntcTermsCfgStateEntry,
       "ntcTermsCfgStateName": ntcTermsCfgStateName,
       "ntcTermsCfgStateRowStatus": ntcTermsCfgStateRowStatus,
       "ntcTermsId": ntcTermsId,
       "ntcTermsCtrlIpAddr": ntcTermsCtrlIpAddr,
       "ntcTermsAdminState": ntcTermsAdminState,
       "ntcTermsConformance": ntcTermsConformance,
       "ntcTermsConfCompliance": ntcTermsConfCompliance,
       "ntcTermsConfCompV1Standard": ntcTermsConfCompV1Standard,
       "ntcTermsConfGroup": ntcTermsConfGroup,
       "ntcTermsConfGrpV1Standard": ntcTermsConfGrpV1Standard}
)
