_E='mwIcrTableIndex'
_D='MERU-CONFIG-ICR-MIB'
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
mwConfigIcr=ModuleIdentity((1,3,6,1,4,1,15983,1,1,4,18))
_MwIcrTable_Object=MibTable
mwIcrTable=_MwIcrTable_Object((1,3,6,1,4,1,15983,1,1,4,18,1))
if mibBuilder.loadTexts:mwIcrTable.setStatus(_A)
_MwIcrEntry_Object=MibTableRow
mwIcrEntry=_MwIcrEntry_Object((1,3,6,1,4,1,15983,1,1,4,18,1,1))
mwIcrEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:mwIcrEntry.setStatus(_A)
_MwIcrTableIndex_Type=Integer32
_MwIcrTableIndex_Object=MibTableColumn
mwIcrTableIndex=_MwIcrTableIndex_Object((1,3,6,1,4,1,15983,1,1,4,18,1,1,1),_MwIcrTableIndex_Type())
mwIcrTableIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:mwIcrTableIndex.setStatus(_A)
class _MwIcrEssId_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_MwIcrEssId_Type.__name__=_C
_MwIcrEssId_Object=MibTableColumn
mwIcrEssId=_MwIcrEssId_Object((1,3,6,1,4,1,15983,1,1,4,18,1,1,2),_MwIcrEssId_Type())
mwIcrEssId.setMaxAccess(_B)
if mibBuilder.loadTexts:mwIcrEssId.setStatus(_A)
_MwIcrControllerIp_Type=IpAddress
_MwIcrControllerIp_Object=MibTableColumn
mwIcrControllerIp=_MwIcrControllerIp_Object((1,3,6,1,4,1,15983,1,1,4,18,1,1,3),_MwIcrControllerIp_Type())
mwIcrControllerIp.setMaxAccess(_B)
if mibBuilder.loadTexts:mwIcrControllerIp.setStatus(_A)
_MwIcrHomeDhcpIp_Type=IpAddress
_MwIcrHomeDhcpIp_Object=MibTableColumn
mwIcrHomeDhcpIp=_MwIcrHomeDhcpIp_Object((1,3,6,1,4,1,15983,1,1,4,18,1,1,4),_MwIcrHomeDhcpIp_Type())
mwIcrHomeDhcpIp.setMaxAccess(_B)
if mibBuilder.loadTexts:mwIcrHomeDhcpIp.setStatus(_A)
_MwIcrRowStatus_Type=RowStatus
_MwIcrRowStatus_Object=MibTableColumn
mwIcrRowStatus=_MwIcrRowStatus_Object((1,3,6,1,4,1,15983,1,1,4,18,1,1,5),_MwIcrRowStatus_Type())
mwIcrRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:mwIcrRowStatus.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'mwConfigIcr':mwConfigIcr,'mwIcrTable':mwIcrTable,'mwIcrEntry':mwIcrEntry,_E:mwIcrTableIndex,'mwIcrEssId':mwIcrEssId,'mwIcrControllerIp':mwIcrControllerIp,'mwIcrHomeDhcpIp':mwIcrHomeDhcpIp,'mwIcrRowStatus':mwIcrRowStatus})