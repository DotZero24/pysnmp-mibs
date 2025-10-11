# SNMP MIB module (H3C-SESSION-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/h3c/H3C-SESSION-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:19:57 2025
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

h3cSession = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 149)
)
if mibBuilder.loadTexts:
    h3cSession.setRevisions(
        ("2016-12-25 11:05",
         "2014-10-14 18:30",
         "2014-07-15 15:30",
         "2013-12-20 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_H3cSessionTables_ObjectIdentity = ObjectIdentity
h3cSessionTables = _H3cSessionTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 149, 1)
)
_H3cSessionStatTable_Object = MibTable
h3cSessionStatTable = _H3cSessionStatTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 149, 1, 1)
)
if mibBuilder.loadTexts:
    h3cSessionStatTable.setStatus("current")
_H3cSessionStatEntry_Object = MibTableRow
h3cSessionStatEntry = _H3cSessionStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 149, 1, 1, 1)
)
h3cSessionStatEntry.setIndexNames(
    (0, "H3C-SESSION-MIB", "h3cSessionStatChassis"),
    (0, "H3C-SESSION-MIB", "h3cSessionStatSlot"),
    (0, "H3C-SESSION-MIB", "h3cSessionStatCPUID"),
)
if mibBuilder.loadTexts:
    h3cSessionStatEntry.setStatus("current")


class _H3cSessionStatChassis_Type(Unsigned32):
    """Custom type h3cSessionStatChassis based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65534),
    )


_H3cSessionStatChassis_Type.__name__ = "Unsigned32"
_H3cSessionStatChassis_Object = MibTableColumn
h3cSessionStatChassis = _H3cSessionStatChassis_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 149, 1, 1, 1, 1),
    _H3cSessionStatChassis_Type()
)
h3cSessionStatChassis.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cSessionStatChassis.setStatus("current")


class _H3cSessionStatSlot_Type(Unsigned32):
    """Custom type h3cSessionStatSlot based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65534),
    )


_H3cSessionStatSlot_Type.__name__ = "Unsigned32"
_H3cSessionStatSlot_Object = MibTableColumn
h3cSessionStatSlot = _H3cSessionStatSlot_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 149, 1, 1, 1, 2),
    _H3cSessionStatSlot_Type()
)
h3cSessionStatSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cSessionStatSlot.setStatus("current")


class _H3cSessionStatCPUID_Type(Unsigned32):
    """Custom type h3cSessionStatCPUID based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_H3cSessionStatCPUID_Type.__name__ = "Unsigned32"
_H3cSessionStatCPUID_Object = MibTableColumn
h3cSessionStatCPUID = _H3cSessionStatCPUID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 149, 1, 1, 1, 3),
    _H3cSessionStatCPUID_Type()
)
h3cSessionStatCPUID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cSessionStatCPUID.setStatus("current")
_H3cSessionStatCount_Type = Unsigned32
_H3cSessionStatCount_Object = MibTableColumn
h3cSessionStatCount = _H3cSessionStatCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 149, 1, 1, 1, 4),
    _H3cSessionStatCount_Type()
)
h3cSessionStatCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cSessionStatCount.setStatus("current")
_H3cSessionStatCreateRate_Type = Unsigned32
_H3cSessionStatCreateRate_Object = MibTableColumn
h3cSessionStatCreateRate = _H3cSessionStatCreateRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 149, 1, 1, 1, 5),
    _H3cSessionStatCreateRate_Type()
)
h3cSessionStatCreateRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cSessionStatCreateRate.setStatus("current")
_H3cSessionStatTCPCount_Type = Unsigned32
_H3cSessionStatTCPCount_Object = MibTableColumn
h3cSessionStatTCPCount = _H3cSessionStatTCPCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 149, 1, 1, 1, 6),
    _H3cSessionStatTCPCount_Type()
)
h3cSessionStatTCPCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cSessionStatTCPCount.setStatus("current")
_H3cSessionStatUDPCount_Type = Unsigned32
_H3cSessionStatUDPCount_Object = MibTableColumn
h3cSessionStatUDPCount = _H3cSessionStatUDPCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 149, 1, 1, 1, 7),
    _H3cSessionStatUDPCount_Type()
)
h3cSessionStatUDPCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cSessionStatUDPCount.setStatus("current")
_H3cSessionStatOtherCount_Type = Unsigned32
_H3cSessionStatOtherCount_Object = MibTableColumn
h3cSessionStatOtherCount = _H3cSessionStatOtherCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 149, 1, 1, 1, 8),
    _H3cSessionStatOtherCount_Type()
)
h3cSessionStatOtherCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cSessionStatOtherCount.setStatus("current")
_H3cSessionStatTCPCreateRate_Type = Unsigned32
_H3cSessionStatTCPCreateRate_Object = MibTableColumn
h3cSessionStatTCPCreateRate = _H3cSessionStatTCPCreateRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 149, 1, 1, 1, 9),
    _H3cSessionStatTCPCreateRate_Type()
)
h3cSessionStatTCPCreateRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cSessionStatTCPCreateRate.setStatus("current")
_H3cSessionStatUDPCreateRate_Type = Unsigned32
_H3cSessionStatUDPCreateRate_Object = MibTableColumn
h3cSessionStatUDPCreateRate = _H3cSessionStatUDPCreateRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 149, 1, 1, 1, 10),
    _H3cSessionStatUDPCreateRate_Type()
)
h3cSessionStatUDPCreateRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cSessionStatUDPCreateRate.setStatus("current")
_H3cSessionStatOtherCreateRate_Type = Unsigned32
_H3cSessionStatOtherCreateRate_Object = MibTableColumn
h3cSessionStatOtherCreateRate = _H3cSessionStatOtherCreateRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 149, 1, 1, 1, 11),
    _H3cSessionStatOtherCreateRate_Type()
)
h3cSessionStatOtherCreateRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cSessionStatOtherCreateRate.setStatus("current")
_H3cSessionStatTCPTotal_Type = Counter64
_H3cSessionStatTCPTotal_Object = MibTableColumn
h3cSessionStatTCPTotal = _H3cSessionStatTCPTotal_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 149, 1, 1, 1, 12),
    _H3cSessionStatTCPTotal_Type()
)
h3cSessionStatTCPTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cSessionStatTCPTotal.setStatus("current")
_H3cSessionStatUDPTotal_Type = Counter64
_H3cSessionStatUDPTotal_Object = MibTableColumn
h3cSessionStatUDPTotal = _H3cSessionStatUDPTotal_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 149, 1, 1, 1, 13),
    _H3cSessionStatUDPTotal_Type()
)
h3cSessionStatUDPTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cSessionStatUDPTotal.setStatus("current")
_H3cSessionStatOtherTotal_Type = Counter64
_H3cSessionStatOtherTotal_Object = MibTableColumn
h3cSessionStatOtherTotal = _H3cSessionStatOtherTotal_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 149, 1, 1, 1, 14),
    _H3cSessionStatOtherTotal_Type()
)
h3cSessionStatOtherTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cSessionStatOtherTotal.setStatus("current")
_H3cSessionStatDNSCount_Type = Unsigned32
_H3cSessionStatDNSCount_Object = MibTableColumn
h3cSessionStatDNSCount = _H3cSessionStatDNSCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 149, 1, 1, 1, 15),
    _H3cSessionStatDNSCount_Type()
)
h3cSessionStatDNSCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cSessionStatDNSCount.setStatus("current")
_H3cSessionStatFTPCount_Type = Unsigned32
_H3cSessionStatFTPCount_Object = MibTableColumn
h3cSessionStatFTPCount = _H3cSessionStatFTPCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 149, 1, 1, 1, 16),
    _H3cSessionStatFTPCount_Type()
)
h3cSessionStatFTPCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cSessionStatFTPCount.setStatus("current")
_H3cSessionStatGTPCount_Type = Unsigned32
_H3cSessionStatGTPCount_Object = MibTableColumn
h3cSessionStatGTPCount = _H3cSessionStatGTPCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 149, 1, 1, 1, 17),
    _H3cSessionStatGTPCount_Type()
)
h3cSessionStatGTPCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cSessionStatGTPCount.setStatus("current")
_H3cSessionStatH323Count_Type = Unsigned32
_H3cSessionStatH323Count_Object = MibTableColumn
h3cSessionStatH323Count = _H3cSessionStatH323Count_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 149, 1, 1, 1, 18),
    _H3cSessionStatH323Count_Type()
)
h3cSessionStatH323Count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cSessionStatH323Count.setStatus("current")
_H3cSessionStatHTTPCount_Type = Unsigned32
_H3cSessionStatHTTPCount_Object = MibTableColumn
h3cSessionStatHTTPCount = _H3cSessionStatHTTPCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 149, 1, 1, 1, 19),
    _H3cSessionStatHTTPCount_Type()
)
h3cSessionStatHTTPCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cSessionStatHTTPCount.setStatus("current")
_H3cSessionStatILSCount_Type = Unsigned32
_H3cSessionStatILSCount_Object = MibTableColumn
h3cSessionStatILSCount = _H3cSessionStatILSCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 149, 1, 1, 1, 20),
    _H3cSessionStatILSCount_Type()
)
h3cSessionStatILSCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cSessionStatILSCount.setStatus("current")
_H3cSessionStatMGCPCount_Type = Unsigned32
_H3cSessionStatMGCPCount_Object = MibTableColumn
h3cSessionStatMGCPCount = _H3cSessionStatMGCPCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 149, 1, 1, 1, 21),
    _H3cSessionStatMGCPCount_Type()
)
h3cSessionStatMGCPCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cSessionStatMGCPCount.setStatus("current")
_H3cSessionStatNBTCount_Type = Unsigned32
_H3cSessionStatNBTCount_Object = MibTableColumn
h3cSessionStatNBTCount = _H3cSessionStatNBTCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 149, 1, 1, 1, 22),
    _H3cSessionStatNBTCount_Type()
)
h3cSessionStatNBTCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cSessionStatNBTCount.setStatus("current")
_H3cSessionStatPPTPCount_Type = Unsigned32
_H3cSessionStatPPTPCount_Object = MibTableColumn
h3cSessionStatPPTPCount = _H3cSessionStatPPTPCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 149, 1, 1, 1, 23),
    _H3cSessionStatPPTPCount_Type()
)
h3cSessionStatPPTPCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cSessionStatPPTPCount.setStatus("current")
_H3cSessionStatRSHCount_Type = Unsigned32
_H3cSessionStatRSHCount_Object = MibTableColumn
h3cSessionStatRSHCount = _H3cSessionStatRSHCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 149, 1, 1, 1, 24),
    _H3cSessionStatRSHCount_Type()
)
h3cSessionStatRSHCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cSessionStatRSHCount.setStatus("current")
_H3cSessionStatRTSPCount_Type = Unsigned32
_H3cSessionStatRTSPCount_Object = MibTableColumn
h3cSessionStatRTSPCount = _H3cSessionStatRTSPCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 149, 1, 1, 1, 25),
    _H3cSessionStatRTSPCount_Type()
)
h3cSessionStatRTSPCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cSessionStatRTSPCount.setStatus("current")
_H3cSessionStatSCCPCount_Type = Unsigned32
_H3cSessionStatSCCPCount_Object = MibTableColumn
h3cSessionStatSCCPCount = _H3cSessionStatSCCPCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 149, 1, 1, 1, 26),
    _H3cSessionStatSCCPCount_Type()
)
h3cSessionStatSCCPCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cSessionStatSCCPCount.setStatus("current")
_H3cSessionStatSIPCount_Type = Unsigned32
_H3cSessionStatSIPCount_Object = MibTableColumn
h3cSessionStatSIPCount = _H3cSessionStatSIPCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 149, 1, 1, 1, 27),
    _H3cSessionStatSIPCount_Type()
)
h3cSessionStatSIPCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cSessionStatSIPCount.setStatus("current")
_H3cSessionStatSMTPCount_Type = Unsigned32
_H3cSessionStatSMTPCount_Object = MibTableColumn
h3cSessionStatSMTPCount = _H3cSessionStatSMTPCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 149, 1, 1, 1, 28),
    _H3cSessionStatSMTPCount_Type()
)
h3cSessionStatSMTPCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cSessionStatSMTPCount.setStatus("current")
_H3cSessionStatSQLNETCount_Type = Unsigned32
_H3cSessionStatSQLNETCount_Object = MibTableColumn
h3cSessionStatSQLNETCount = _H3cSessionStatSQLNETCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 149, 1, 1, 1, 29),
    _H3cSessionStatSQLNETCount_Type()
)
h3cSessionStatSQLNETCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cSessionStatSQLNETCount.setStatus("current")
_H3cSessionStatSSHCount_Type = Unsigned32
_H3cSessionStatSSHCount_Object = MibTableColumn
h3cSessionStatSSHCount = _H3cSessionStatSSHCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 149, 1, 1, 1, 30),
    _H3cSessionStatSSHCount_Type()
)
h3cSessionStatSSHCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cSessionStatSSHCount.setStatus("current")
_H3cSessionStatTELNETCount_Type = Unsigned32
_H3cSessionStatTELNETCount_Object = MibTableColumn
h3cSessionStatTELNETCount = _H3cSessionStatTELNETCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 149, 1, 1, 1, 31),
    _H3cSessionStatTELNETCount_Type()
)
h3cSessionStatTELNETCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cSessionStatTELNETCount.setStatus("current")
_H3cSessionStatTFTPCount_Type = Unsigned32
_H3cSessionStatTFTPCount_Object = MibTableColumn
h3cSessionStatTFTPCount = _H3cSessionStatTFTPCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 149, 1, 1, 1, 32),
    _H3cSessionStatTFTPCount_Type()
)
h3cSessionStatTFTPCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cSessionStatTFTPCount.setStatus("current")
_H3cSessionStatXDMCPCount_Type = Unsigned32
_H3cSessionStatXDMCPCount_Object = MibTableColumn
h3cSessionStatXDMCPCount = _H3cSessionStatXDMCPCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 149, 1, 1, 1, 33),
    _H3cSessionStatXDMCPCount_Type()
)
h3cSessionStatXDMCPCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cSessionStatXDMCPCount.setStatus("current")
_H3cSessionEntTable_Object = MibTable
h3cSessionEntTable = _H3cSessionEntTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 149, 1, 2)
)
if mibBuilder.loadTexts:
    h3cSessionEntTable.setStatus("current")
_H3cSessionEntEntry_Object = MibTableRow
h3cSessionEntEntry = _H3cSessionEntEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 149, 1, 2, 1)
)
h3cSessionEntEntry.setIndexNames(
    (0, "H3C-SESSION-MIB", "h3cSessionEntIndex"),
)
if mibBuilder.loadTexts:
    h3cSessionEntEntry.setStatus("current")


class _H3cSessionEntIndex_Type(Unsigned32):
    """Custom type h3cSessionEntIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_H3cSessionEntIndex_Type.__name__ = "Unsigned32"
_H3cSessionEntIndex_Object = MibTableColumn
h3cSessionEntIndex = _H3cSessionEntIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 149, 1, 2, 1, 1),
    _H3cSessionEntIndex_Type()
)
h3cSessionEntIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cSessionEntIndex.setStatus("current")
_H3cSessionEntCount_Type = Unsigned32
_H3cSessionEntCount_Object = MibTableColumn
h3cSessionEntCount = _H3cSessionEntCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 149, 1, 2, 1, 2),
    _H3cSessionEntCount_Type()
)
h3cSessionEntCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cSessionEntCount.setStatus("current")
_H3cSessionEntCreateRate_Type = Unsigned32
_H3cSessionEntCreateRate_Object = MibTableColumn
h3cSessionEntCreateRate = _H3cSessionEntCreateRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 149, 1, 2, 1, 3),
    _H3cSessionEntCreateRate_Type()
)
h3cSessionEntCreateRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cSessionEntCreateRate.setStatus("current")
_H3cSessionEntTCPCount_Type = Unsigned32
_H3cSessionEntTCPCount_Object = MibTableColumn
h3cSessionEntTCPCount = _H3cSessionEntTCPCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 149, 1, 2, 1, 4),
    _H3cSessionEntTCPCount_Type()
)
h3cSessionEntTCPCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cSessionEntTCPCount.setStatus("current")
_H3cSessionEntUDPCount_Type = Unsigned32
_H3cSessionEntUDPCount_Object = MibTableColumn
h3cSessionEntUDPCount = _H3cSessionEntUDPCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 149, 1, 2, 1, 5),
    _H3cSessionEntUDPCount_Type()
)
h3cSessionEntUDPCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cSessionEntUDPCount.setStatus("current")
_H3cSessionEntOtherCount_Type = Unsigned32
_H3cSessionEntOtherCount_Object = MibTableColumn
h3cSessionEntOtherCount = _H3cSessionEntOtherCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 149, 1, 2, 1, 6),
    _H3cSessionEntOtherCount_Type()
)
h3cSessionEntOtherCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cSessionEntOtherCount.setStatus("current")
_H3cSessionEntTCPCreateRate_Type = Unsigned32
_H3cSessionEntTCPCreateRate_Object = MibTableColumn
h3cSessionEntTCPCreateRate = _H3cSessionEntTCPCreateRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 149, 1, 2, 1, 7),
    _H3cSessionEntTCPCreateRate_Type()
)
h3cSessionEntTCPCreateRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cSessionEntTCPCreateRate.setStatus("current")
_H3cSessionEntUDPCreateRate_Type = Unsigned32
_H3cSessionEntUDPCreateRate_Object = MibTableColumn
h3cSessionEntUDPCreateRate = _H3cSessionEntUDPCreateRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 149, 1, 2, 1, 8),
    _H3cSessionEntUDPCreateRate_Type()
)
h3cSessionEntUDPCreateRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cSessionEntUDPCreateRate.setStatus("current")
_H3cSessionEntOtherCreateRate_Type = Unsigned32
_H3cSessionEntOtherCreateRate_Object = MibTableColumn
h3cSessionEntOtherCreateRate = _H3cSessionEntOtherCreateRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 149, 1, 2, 1, 9),
    _H3cSessionEntOtherCreateRate_Type()
)
h3cSessionEntOtherCreateRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cSessionEntOtherCreateRate.setStatus("current")
_H3cSessionEntTCPTotal_Type = Counter64
_H3cSessionEntTCPTotal_Object = MibTableColumn
h3cSessionEntTCPTotal = _H3cSessionEntTCPTotal_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 149, 1, 2, 1, 10),
    _H3cSessionEntTCPTotal_Type()
)
h3cSessionEntTCPTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cSessionEntTCPTotal.setStatus("current")
_H3cSessionEntUDPTotal_Type = Counter64
_H3cSessionEntUDPTotal_Object = MibTableColumn
h3cSessionEntUDPTotal = _H3cSessionEntUDPTotal_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 149, 1, 2, 1, 11),
    _H3cSessionEntUDPTotal_Type()
)
h3cSessionEntUDPTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cSessionEntUDPTotal.setStatus("current")
_H3cSessionEntOtherTotal_Type = Counter64
_H3cSessionEntOtherTotal_Object = MibTableColumn
h3cSessionEntOtherTotal = _H3cSessionEntOtherTotal_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 149, 1, 2, 1, 12),
    _H3cSessionEntOtherTotal_Type()
)
h3cSessionEntOtherTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cSessionEntOtherTotal.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "H3C-SESSION-MIB",
    **{"h3cSession": h3cSession,
       "h3cSessionTables": h3cSessionTables,
       "h3cSessionStatTable": h3cSessionStatTable,
       "h3cSessionStatEntry": h3cSessionStatEntry,
       "h3cSessionStatChassis": h3cSessionStatChassis,
       "h3cSessionStatSlot": h3cSessionStatSlot,
       "h3cSessionStatCPUID": h3cSessionStatCPUID,
       "h3cSessionStatCount": h3cSessionStatCount,
       "h3cSessionStatCreateRate": h3cSessionStatCreateRate,
       "h3cSessionStatTCPCount": h3cSessionStatTCPCount,
       "h3cSessionStatUDPCount": h3cSessionStatUDPCount,
       "h3cSessionStatOtherCount": h3cSessionStatOtherCount,
       "h3cSessionStatTCPCreateRate": h3cSessionStatTCPCreateRate,
       "h3cSessionStatUDPCreateRate": h3cSessionStatUDPCreateRate,
       "h3cSessionStatOtherCreateRate": h3cSessionStatOtherCreateRate,
       "h3cSessionStatTCPTotal": h3cSessionStatTCPTotal,
       "h3cSessionStatUDPTotal": h3cSessionStatUDPTotal,
       "h3cSessionStatOtherTotal": h3cSessionStatOtherTotal,
       "h3cSessionStatDNSCount": h3cSessionStatDNSCount,
       "h3cSessionStatFTPCount": h3cSessionStatFTPCount,
       "h3cSessionStatGTPCount": h3cSessionStatGTPCount,
       "h3cSessionStatH323Count": h3cSessionStatH323Count,
       "h3cSessionStatHTTPCount": h3cSessionStatHTTPCount,
       "h3cSessionStatILSCount": h3cSessionStatILSCount,
       "h3cSessionStatMGCPCount": h3cSessionStatMGCPCount,
       "h3cSessionStatNBTCount": h3cSessionStatNBTCount,
       "h3cSessionStatPPTPCount": h3cSessionStatPPTPCount,
       "h3cSessionStatRSHCount": h3cSessionStatRSHCount,
       "h3cSessionStatRTSPCount": h3cSessionStatRTSPCount,
       "h3cSessionStatSCCPCount": h3cSessionStatSCCPCount,
       "h3cSessionStatSIPCount": h3cSessionStatSIPCount,
       "h3cSessionStatSMTPCount": h3cSessionStatSMTPCount,
       "h3cSessionStatSQLNETCount": h3cSessionStatSQLNETCount,
       "h3cSessionStatSSHCount": h3cSessionStatSSHCount,
       "h3cSessionStatTELNETCount": h3cSessionStatTELNETCount,
       "h3cSessionStatTFTPCount": h3cSessionStatTFTPCount,
       "h3cSessionStatXDMCPCount": h3cSessionStatXDMCPCount,
       "h3cSessionEntTable": h3cSessionEntTable,
       "h3cSessionEntEntry": h3cSessionEntEntry,
       "h3cSessionEntIndex": h3cSessionEntIndex,
       "h3cSessionEntCount": h3cSessionEntCount,
       "h3cSessionEntCreateRate": h3cSessionEntCreateRate,
       "h3cSessionEntTCPCount": h3cSessionEntTCPCount,
       "h3cSessionEntUDPCount": h3cSessionEntUDPCount,
       "h3cSessionEntOtherCount": h3cSessionEntOtherCount,
       "h3cSessionEntTCPCreateRate": h3cSessionEntTCPCreateRate,
       "h3cSessionEntUDPCreateRate": h3cSessionEntUDPCreateRate,
       "h3cSessionEntOtherCreateRate": h3cSessionEntOtherCreateRate,
       "h3cSessionEntTCPTotal": h3cSessionEntTCPTotal,
       "h3cSessionEntUDPTotal": h3cSessionEntUDPTotal,
       "h3cSessionEntOtherTotal": h3cSessionEntOtherTotal}
)
