_E='mwWncTrapCommunityTableIndex'
_D='MERU-CONFIG-SNMP-MIB'
_C='DisplayString'
_B='read-create'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
Ipv6Address,=mibBuilder.importSymbols('IPV6-TC','Ipv6Address')
mwConfiguration,=mibBuilder.importSymbols('MERU-SMI','mwConfiguration')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DateAndTime,DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TimeInterval,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime',_C,'MacAddress','PhysAddress','RowStatus','TextualConvention','TimeInterval','TimeStamp','TruthValue')
mwConfigSnmp=ModuleIdentity((1,3,6,1,4,1,15983,1,1,4,12))
_MwWncTrapCommunityTable_Object=MibTable
mwWncTrapCommunityTable=_MwWncTrapCommunityTable_Object((1,3,6,1,4,1,15983,1,1,4,12,2))
if mibBuilder.loadTexts:mwWncTrapCommunityTable.setStatus(_A)
_MwWncTrapCommunityEntry_Object=MibTableRow
mwWncTrapCommunityEntry=_MwWncTrapCommunityEntry_Object((1,3,6,1,4,1,15983,1,1,4,12,2,1))
mwWncTrapCommunityEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:mwWncTrapCommunityEntry.setStatus(_A)
_MwWncTrapCommunityTableIndex_Type=Integer32
_MwWncTrapCommunityTableIndex_Object=MibTableColumn
mwWncTrapCommunityTableIndex=_MwWncTrapCommunityTableIndex_Object((1,3,6,1,4,1,15983,1,1,4,12,2,1,1),_MwWncTrapCommunityTableIndex_Type())
mwWncTrapCommunityTableIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:mwWncTrapCommunityTableIndex.setStatus(_A)
class _MwWncTrapCommunitypCommunityStr_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_MwWncTrapCommunitypCommunityStr_Type.__name__=_C
_MwWncTrapCommunitypCommunityStr_Object=MibTableColumn
mwWncTrapCommunitypCommunityStr=_MwWncTrapCommunitypCommunityStr_Object((1,3,6,1,4,1,15983,1,1,4,12,2,1,2),_MwWncTrapCommunitypCommunityStr_Type())
mwWncTrapCommunitypCommunityStr.setMaxAccess(_B)
if mibBuilder.loadTexts:mwWncTrapCommunitypCommunityStr.setStatus(_A)
_MwWncTrapCommunityClientIpAddress_Type=IpAddress
_MwWncTrapCommunityClientIpAddress_Object=MibTableColumn
mwWncTrapCommunityClientIpAddress=_MwWncTrapCommunityClientIpAddress_Object((1,3,6,1,4,1,15983,1,1,4,12,2,1,3),_MwWncTrapCommunityClientIpAddress_Type())
mwWncTrapCommunityClientIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:mwWncTrapCommunityClientIpAddress.setStatus(_A)
_MwWncTrapCommunityRowStatus_Type=RowStatus
_MwWncTrapCommunityRowStatus_Object=MibTableColumn
mwWncTrapCommunityRowStatus=_MwWncTrapCommunityRowStatus_Object((1,3,6,1,4,1,15983,1,1,4,12,2,1,4),_MwWncTrapCommunityRowStatus_Type())
mwWncTrapCommunityRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:mwWncTrapCommunityRowStatus.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'mwConfigSnmp':mwConfigSnmp,'mwWncTrapCommunityTable':mwWncTrapCommunityTable,'mwWncTrapCommunityEntry':mwWncTrapCommunityEntry,_E:mwWncTrapCommunityTableIndex,'mwWncTrapCommunitypCommunityStr':mwWncTrapCommunitypCommunityStr,'mwWncTrapCommunityClientIpAddress':mwWncTrapCommunityClientIpAddress,'mwWncTrapCommunityRowStatus':mwWncTrapCommunityRowStatus})