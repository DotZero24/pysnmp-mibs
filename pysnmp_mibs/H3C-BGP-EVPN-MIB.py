# SNMP MIB module (H3C-BGP-EVPN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/h3c/H3C-BGP-EVPN-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:18:28 2025
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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

h3cBgpEvpn = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 172)
)
if mibBuilder.loadTexts:
    h3cBgpEvpn.setRevisions(
        ("2017-11-29 14:31",
         "2017-11-04 14:31")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_H3cBgpEvpnObjects_ObjectIdentity = ObjectIdentity
h3cBgpEvpnObjects = _H3cBgpEvpnObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 172, 1)
)
_H3cBgpEvpnConf_ObjectIdentity = ObjectIdentity
h3cBgpEvpnConf = _H3cBgpEvpnConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 172, 1, 1)
)
_H3cBgpEvpnNbrAddrTable_Object = MibTable
h3cBgpEvpnNbrAddrTable = _H3cBgpEvpnNbrAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 172, 1, 1, 1)
)
if mibBuilder.loadTexts:
    h3cBgpEvpnNbrAddrTable.setStatus("current")
_H3cBgpEvpnNbrAddrEntry_Object = MibTableRow
h3cBgpEvpnNbrAddrEntry = _H3cBgpEvpnNbrAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 172, 1, 1, 1, 1)
)
h3cBgpEvpnNbrAddrEntry.setIndexNames(
    (0, "H3C-BGP-EVPN-MIB", "h3cBgpEvpnNbrAddr"),
)
if mibBuilder.loadTexts:
    h3cBgpEvpnNbrAddrEntry.setStatus("current")
_H3cBgpEvpnNbrAddr_Type = IpAddress
_H3cBgpEvpnNbrAddr_Object = MibTableColumn
h3cBgpEvpnNbrAddr = _H3cBgpEvpnNbrAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 172, 1, 1, 1, 1, 1),
    _H3cBgpEvpnNbrAddr_Type()
)
h3cBgpEvpnNbrAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cBgpEvpnNbrAddr.setStatus("current")
_H3cBgpEvpnNbrAsNumber_Type = Unsigned32
_H3cBgpEvpnNbrAsNumber_Object = MibTableColumn
h3cBgpEvpnNbrAsNumber = _H3cBgpEvpnNbrAsNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 172, 1, 1, 1, 1, 2),
    _H3cBgpEvpnNbrAsNumber_Type()
)
h3cBgpEvpnNbrAsNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cBgpEvpnNbrAsNumber.setStatus("current")
_H3cBgpEvpnNbrPrefixTable_Object = MibTable
h3cBgpEvpnNbrPrefixTable = _H3cBgpEvpnNbrPrefixTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 172, 1, 1, 2)
)
if mibBuilder.loadTexts:
    h3cBgpEvpnNbrPrefixTable.setStatus("current")
_H3cBgpEvpnNbrPrefixEntry_Object = MibTableRow
h3cBgpEvpnNbrPrefixEntry = _H3cBgpEvpnNbrPrefixEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 172, 1, 1, 2, 1)
)
h3cBgpEvpnNbrPrefixEntry.setIndexNames(
    (0, "H3C-BGP-EVPN-MIB", "h3cBgpEvpnPAtrRD"),
    (0, "H3C-BGP-EVPN-MIB", "h3cBgpEvpnPAtrPeer"),
    (0, "H3C-BGP-EVPN-MIB", "h3cBgpEvpnPAtrAddrPrefixLen"),
    (0, "H3C-BGP-EVPN-MIB", "h3cBgpEvpnPAtrAddrPrefix"),
)
if mibBuilder.loadTexts:
    h3cBgpEvpnNbrPrefixEntry.setStatus("current")


class _H3cBgpEvpnPAtrRD_Type(OctetString):
    """Custom type h3cBgpEvpnPAtrRD based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 21),
    )


_H3cBgpEvpnPAtrRD_Type.__name__ = "OctetString"
_H3cBgpEvpnPAtrRD_Object = MibTableColumn
h3cBgpEvpnPAtrRD = _H3cBgpEvpnPAtrRD_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 172, 1, 1, 2, 1, 1),
    _H3cBgpEvpnPAtrRD_Type()
)
h3cBgpEvpnPAtrRD.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cBgpEvpnPAtrRD.setStatus("current")


class _H3cBgpEvpnPAtrPeer_Type(OctetString):
    """Custom type h3cBgpEvpnPAtrPeer based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 86),
    )


_H3cBgpEvpnPAtrPeer_Type.__name__ = "OctetString"
_H3cBgpEvpnPAtrPeer_Object = MibTableColumn
h3cBgpEvpnPAtrPeer = _H3cBgpEvpnPAtrPeer_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 172, 1, 1, 2, 1, 2),
    _H3cBgpEvpnPAtrPeer_Type()
)
h3cBgpEvpnPAtrPeer.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cBgpEvpnPAtrPeer.setStatus("current")


class _H3cBgpEvpnPAtrAddrPrefixLen_Type(Integer32):
    """Custom type h3cBgpEvpnPAtrAddrPrefixLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 300),
    )


_H3cBgpEvpnPAtrAddrPrefixLen_Type.__name__ = "Integer32"
_H3cBgpEvpnPAtrAddrPrefixLen_Object = MibTableColumn
h3cBgpEvpnPAtrAddrPrefixLen = _H3cBgpEvpnPAtrAddrPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 172, 1, 1, 2, 1, 3),
    _H3cBgpEvpnPAtrAddrPrefixLen_Type()
)
h3cBgpEvpnPAtrAddrPrefixLen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cBgpEvpnPAtrAddrPrefixLen.setStatus("current")
_H3cBgpEvpnPAtrAddrPrefix_Type = IpAddress
_H3cBgpEvpnPAtrAddrPrefix_Object = MibTableColumn
h3cBgpEvpnPAtrAddrPrefix = _H3cBgpEvpnPAtrAddrPrefix_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 172, 1, 1, 2, 1, 4),
    _H3cBgpEvpnPAtrAddrPrefix_Type()
)
h3cBgpEvpnPAtrAddrPrefix.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cBgpEvpnPAtrAddrPrefix.setStatus("current")
_H3cBgpEvpnPAtrRouteType_Type = Unsigned32
_H3cBgpEvpnPAtrRouteType_Object = MibTableColumn
h3cBgpEvpnPAtrRouteType = _H3cBgpEvpnPAtrRouteType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 172, 1, 1, 2, 1, 5),
    _H3cBgpEvpnPAtrRouteType_Type()
)
h3cBgpEvpnPAtrRouteType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cBgpEvpnPAtrRouteType.setStatus("current")


class _H3cBgpEvpnPAtrOrigin_Type(Integer32):
    """Custom type h3cBgpEvpnPAtrOrigin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("igp", 1),
          ("egp", 2),
          ("incomplete", 3))
    )


_H3cBgpEvpnPAtrOrigin_Type.__name__ = "Integer32"
_H3cBgpEvpnPAtrOrigin_Object = MibTableColumn
h3cBgpEvpnPAtrOrigin = _H3cBgpEvpnPAtrOrigin_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 172, 1, 1, 2, 1, 6),
    _H3cBgpEvpnPAtrOrigin_Type()
)
h3cBgpEvpnPAtrOrigin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cBgpEvpnPAtrOrigin.setStatus("current")


class _H3cBgpEvpnPAtrASPathSegment_Type(OctetString):
    """Custom type h3cBgpEvpnPAtrASPathSegment based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 255),
    )


_H3cBgpEvpnPAtrASPathSegment_Type.__name__ = "OctetString"
_H3cBgpEvpnPAtrASPathSegment_Object = MibTableColumn
h3cBgpEvpnPAtrASPathSegment = _H3cBgpEvpnPAtrASPathSegment_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 172, 1, 1, 2, 1, 7),
    _H3cBgpEvpnPAtrASPathSegment_Type()
)
h3cBgpEvpnPAtrASPathSegment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cBgpEvpnPAtrASPathSegment.setStatus("current")
_H3cBgpEvpnPAtrNextHop_Type = IpAddress
_H3cBgpEvpnPAtrNextHop_Object = MibTableColumn
h3cBgpEvpnPAtrNextHop = _H3cBgpEvpnPAtrNextHop_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 172, 1, 1, 2, 1, 8),
    _H3cBgpEvpnPAtrNextHop_Type()
)
h3cBgpEvpnPAtrNextHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cBgpEvpnPAtrNextHop.setStatus("current")


class _H3cBgpEvpnPAtrMultiExitDisc_Type(Integer32):
    """Custom type h3cBgpEvpnPAtrMultiExitDisc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_H3cBgpEvpnPAtrMultiExitDisc_Type.__name__ = "Integer32"
_H3cBgpEvpnPAtrMultiExitDisc_Object = MibTableColumn
h3cBgpEvpnPAtrMultiExitDisc = _H3cBgpEvpnPAtrMultiExitDisc_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 172, 1, 1, 2, 1, 9),
    _H3cBgpEvpnPAtrMultiExitDisc_Type()
)
h3cBgpEvpnPAtrMultiExitDisc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cBgpEvpnPAtrMultiExitDisc.setStatus("current")


class _H3cBgpEvpnPAtrLocalPref_Type(Integer32):
    """Custom type h3cBgpEvpnPAtrLocalPref based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_H3cBgpEvpnPAtrLocalPref_Type.__name__ = "Integer32"
_H3cBgpEvpnPAtrLocalPref_Object = MibTableColumn
h3cBgpEvpnPAtrLocalPref = _H3cBgpEvpnPAtrLocalPref_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 172, 1, 1, 2, 1, 10),
    _H3cBgpEvpnPAtrLocalPref_Type()
)
h3cBgpEvpnPAtrLocalPref.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cBgpEvpnPAtrLocalPref.setStatus("current")


class _H3cBgpEvpnPAtrIGMPFlags_Type(Integer32):
    """Custom type h3cBgpEvpnPAtrIGMPFlags based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("igmpv1", 1),
          ("igmpv2", 2),
          ("igmpv3", 3))
    )


_H3cBgpEvpnPAtrIGMPFlags_Type.__name__ = "Integer32"
_H3cBgpEvpnPAtrIGMPFlags_Object = MibTableColumn
h3cBgpEvpnPAtrIGMPFlags = _H3cBgpEvpnPAtrIGMPFlags_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 172, 1, 1, 2, 1, 11),
    _H3cBgpEvpnPAtrIGMPFlags_Type()
)
h3cBgpEvpnPAtrIGMPFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cBgpEvpnPAtrIGMPFlags.setStatus("current")
_H3cBgpEvpnPAtrMaxRespTime_Type = Unsigned32
_H3cBgpEvpnPAtrMaxRespTime_Object = MibTableColumn
h3cBgpEvpnPAtrMaxRespTime = _H3cBgpEvpnPAtrMaxRespTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 172, 1, 1, 2, 1, 12),
    _H3cBgpEvpnPAtrMaxRespTime_Type()
)
h3cBgpEvpnPAtrMaxRespTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cBgpEvpnPAtrMaxRespTime.setStatus("current")
if mibBuilder.loadTexts:
    h3cBgpEvpnPAtrMaxRespTime.setUnits("ms")


class _H3cBgpEvpnPAtrPMSITunnel_Type(OctetString):
    """Custom type h3cBgpEvpnPAtrPMSITunnel based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(9, 21),
    )


_H3cBgpEvpnPAtrPMSITunnel_Type.__name__ = "OctetString"
_H3cBgpEvpnPAtrPMSITunnel_Object = MibTableColumn
h3cBgpEvpnPAtrPMSITunnel = _H3cBgpEvpnPAtrPMSITunnel_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 172, 1, 1, 2, 1, 13),
    _H3cBgpEvpnPAtrPMSITunnel_Type()
)
h3cBgpEvpnPAtrPMSITunnel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cBgpEvpnPAtrPMSITunnel.setStatus("current")
_H3cBgpEvpnPAtrL2VNI_Type = Unsigned32
_H3cBgpEvpnPAtrL2VNI_Object = MibTableColumn
h3cBgpEvpnPAtrL2VNI = _H3cBgpEvpnPAtrL2VNI_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 172, 1, 1, 2, 1, 14),
    _H3cBgpEvpnPAtrL2VNI_Type()
)
h3cBgpEvpnPAtrL2VNI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cBgpEvpnPAtrL2VNI.setStatus("current")
_H3cBgpEvpnPAtrL3VNI_Type = Unsigned32
_H3cBgpEvpnPAtrL3VNI_Object = MibTableColumn
h3cBgpEvpnPAtrL3VNI = _H3cBgpEvpnPAtrL3VNI_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 172, 1, 1, 2, 1, 15),
    _H3cBgpEvpnPAtrL3VNI_Type()
)
h3cBgpEvpnPAtrL3VNI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cBgpEvpnPAtrL3VNI.setStatus("current")
_H3cBgpEvpnPAtrBest_Type = TruthValue
_H3cBgpEvpnPAtrBest_Object = MibTableColumn
h3cBgpEvpnPAtrBest = _H3cBgpEvpnPAtrBest_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 172, 1, 1, 2, 1, 16),
    _H3cBgpEvpnPAtrBest_Type()
)
h3cBgpEvpnPAtrBest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cBgpEvpnPAtrBest.setStatus("current")


class _H3cBgpEvpnPAtrUnknown_Type(OctetString):
    """Custom type h3cBgpEvpnPAtrUnknown based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_H3cBgpEvpnPAtrUnknown_Type.__name__ = "OctetString"
_H3cBgpEvpnPAtrUnknown_Object = MibTableColumn
h3cBgpEvpnPAtrUnknown = _H3cBgpEvpnPAtrUnknown_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 172, 1, 1, 2, 1, 17),
    _H3cBgpEvpnPAtrUnknown_Type()
)
h3cBgpEvpnPAtrUnknown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cBgpEvpnPAtrUnknown.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "H3C-BGP-EVPN-MIB",
    **{"h3cBgpEvpn": h3cBgpEvpn,
       "h3cBgpEvpnObjects": h3cBgpEvpnObjects,
       "h3cBgpEvpnConf": h3cBgpEvpnConf,
       "h3cBgpEvpnNbrAddrTable": h3cBgpEvpnNbrAddrTable,
       "h3cBgpEvpnNbrAddrEntry": h3cBgpEvpnNbrAddrEntry,
       "h3cBgpEvpnNbrAddr": h3cBgpEvpnNbrAddr,
       "h3cBgpEvpnNbrAsNumber": h3cBgpEvpnNbrAsNumber,
       "h3cBgpEvpnNbrPrefixTable": h3cBgpEvpnNbrPrefixTable,
       "h3cBgpEvpnNbrPrefixEntry": h3cBgpEvpnNbrPrefixEntry,
       "h3cBgpEvpnPAtrRD": h3cBgpEvpnPAtrRD,
       "h3cBgpEvpnPAtrPeer": h3cBgpEvpnPAtrPeer,
       "h3cBgpEvpnPAtrAddrPrefixLen": h3cBgpEvpnPAtrAddrPrefixLen,
       "h3cBgpEvpnPAtrAddrPrefix": h3cBgpEvpnPAtrAddrPrefix,
       "h3cBgpEvpnPAtrRouteType": h3cBgpEvpnPAtrRouteType,
       "h3cBgpEvpnPAtrOrigin": h3cBgpEvpnPAtrOrigin,
       "h3cBgpEvpnPAtrASPathSegment": h3cBgpEvpnPAtrASPathSegment,
       "h3cBgpEvpnPAtrNextHop": h3cBgpEvpnPAtrNextHop,
       "h3cBgpEvpnPAtrMultiExitDisc": h3cBgpEvpnPAtrMultiExitDisc,
       "h3cBgpEvpnPAtrLocalPref": h3cBgpEvpnPAtrLocalPref,
       "h3cBgpEvpnPAtrIGMPFlags": h3cBgpEvpnPAtrIGMPFlags,
       "h3cBgpEvpnPAtrMaxRespTime": h3cBgpEvpnPAtrMaxRespTime,
       "h3cBgpEvpnPAtrPMSITunnel": h3cBgpEvpnPAtrPMSITunnel,
       "h3cBgpEvpnPAtrL2VNI": h3cBgpEvpnPAtrL2VNI,
       "h3cBgpEvpnPAtrL3VNI": h3cBgpEvpnPAtrL3VNI,
       "h3cBgpEvpnPAtrBest": h3cBgpEvpnPAtrBest,
       "h3cBgpEvpnPAtrUnknown": h3cBgpEvpnPAtrUnknown}
)
