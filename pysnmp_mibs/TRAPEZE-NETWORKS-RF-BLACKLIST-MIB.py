_G='trpzRFBlacklistXmtrGroup'
_F='trpzRFBlacklistXmtrTimeToLive'
_E='trpzRFBlacklistXmtrType'
_D='read-only'
_C='trpzRFBlacklistXmtrMacAddress'
_B='TRAPEZE-NETWORKS-RF-BLACKLIST-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','TextualConvention')
trpzMibs,=mibBuilder.importSymbols('TRAPEZE-NETWORKS-ROOT-MIB','trpzMibs')
trpzRFBlacklistMib=ModuleIdentity((1,3,6,1,4,1,14525,4,18))
if mibBuilder.loadTexts:trpzRFBlacklistMib.setRevisions(('2011-02-24 00:14',))
class TrpzRFBlacklistedEntryType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('other',1),('unknownDynamic',2),('configuredPermanent',3),('configuredDynamic',4),('assocReqFlood',5),('reassocReqFlood',6),('disassocReqFlood',7)))
_TrpzRFBlacklistMibObjects_ObjectIdentity=ObjectIdentity
trpzRFBlacklistMibObjects=_TrpzRFBlacklistMibObjects_ObjectIdentity((1,3,6,1,4,1,14525,4,18,1))
_TrpzRFBlacklistXmtrTable_Object=MibTable
trpzRFBlacklistXmtrTable=_TrpzRFBlacklistXmtrTable_Object((1,3,6,1,4,1,14525,4,18,1,2))
if mibBuilder.loadTexts:trpzRFBlacklistXmtrTable.setStatus(_A)
_TrpzRFBlacklistXmtrEntry_Object=MibTableRow
trpzRFBlacklistXmtrEntry=_TrpzRFBlacklistXmtrEntry_Object((1,3,6,1,4,1,14525,4,18,1,2,1))
trpzRFBlacklistXmtrEntry.setIndexNames((0,_B,_C))
if mibBuilder.loadTexts:trpzRFBlacklistXmtrEntry.setStatus(_A)
_TrpzRFBlacklistXmtrMacAddress_Type=MacAddress
_TrpzRFBlacklistXmtrMacAddress_Object=MibTableColumn
trpzRFBlacklistXmtrMacAddress=_TrpzRFBlacklistXmtrMacAddress_Object((1,3,6,1,4,1,14525,4,18,1,2,1,1),_TrpzRFBlacklistXmtrMacAddress_Type())
trpzRFBlacklistXmtrMacAddress.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:trpzRFBlacklistXmtrMacAddress.setStatus(_A)
_TrpzRFBlacklistXmtrType_Type=TrpzRFBlacklistedEntryType
_TrpzRFBlacklistXmtrType_Object=MibTableColumn
trpzRFBlacklistXmtrType=_TrpzRFBlacklistXmtrType_Object((1,3,6,1,4,1,14525,4,18,1,2,1,2),_TrpzRFBlacklistXmtrType_Type())
trpzRFBlacklistXmtrType.setMaxAccess(_D)
if mibBuilder.loadTexts:trpzRFBlacklistXmtrType.setStatus(_A)
_TrpzRFBlacklistXmtrTimeToLive_Type=Unsigned32
_TrpzRFBlacklistXmtrTimeToLive_Object=MibTableColumn
trpzRFBlacklistXmtrTimeToLive=_TrpzRFBlacklistXmtrTimeToLive_Object((1,3,6,1,4,1,14525,4,18,1,2,1,3),_TrpzRFBlacklistXmtrTimeToLive_Type())
trpzRFBlacklistXmtrTimeToLive.setMaxAccess(_D)
if mibBuilder.loadTexts:trpzRFBlacklistXmtrTimeToLive.setStatus(_A)
_TrpzRFBlacklistConformance_ObjectIdentity=ObjectIdentity
trpzRFBlacklistConformance=_TrpzRFBlacklistConformance_ObjectIdentity((1,3,6,1,4,1,14525,4,18,2))
_TrpzRFBlacklistCompliances_ObjectIdentity=ObjectIdentity
trpzRFBlacklistCompliances=_TrpzRFBlacklistCompliances_ObjectIdentity((1,3,6,1,4,1,14525,4,18,2,1))
_TrpzRFBlacklistGroups_ObjectIdentity=ObjectIdentity
trpzRFBlacklistGroups=_TrpzRFBlacklistGroups_ObjectIdentity((1,3,6,1,4,1,14525,4,18,2,2))
trpzRFBlacklistXmtrGroup=ObjectGroup((1,3,6,1,4,1,14525,4,18,2,2,1))
trpzRFBlacklistXmtrGroup.setObjects(*((_B,_E),(_B,_F)))
if mibBuilder.loadTexts:trpzRFBlacklistXmtrGroup.setStatus(_A)
trpzRFBlacklistCompliance=ModuleCompliance((1,3,6,1,4,1,14525,4,18,2,1,1))
trpzRFBlacklistCompliance.setObjects((_B,_G))
if mibBuilder.loadTexts:trpzRFBlacklistCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'TrpzRFBlacklistedEntryType':TrpzRFBlacklistedEntryType,'trpzRFBlacklistMib':trpzRFBlacklistMib,'trpzRFBlacklistMibObjects':trpzRFBlacklistMibObjects,'trpzRFBlacklistXmtrTable':trpzRFBlacklistXmtrTable,'trpzRFBlacklistXmtrEntry':trpzRFBlacklistXmtrEntry,_C:trpzRFBlacklistXmtrMacAddress,_E:trpzRFBlacklistXmtrType,_F:trpzRFBlacklistXmtrTimeToLive,'trpzRFBlacklistConformance':trpzRFBlacklistConformance,'trpzRFBlacklistCompliances':trpzRFBlacklistCompliances,'trpzRFBlacklistCompliance':trpzRFBlacklistCompliance,'trpzRFBlacklistGroups':trpzRFBlacklistGroups,_G:trpzRFBlacklistXmtrGroup})