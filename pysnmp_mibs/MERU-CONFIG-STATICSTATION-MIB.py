_D='mwStaticStationTableIndex'
_C='MERU-CONFIG-STATICSTATION-MIB'
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
DateAndTime,DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TimeInterval,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention','TimeInterval','TimeStamp','TruthValue')
mwConfigStaticStation=ModuleIdentity((1,3,6,1,4,1,15983,1,1,4,16))
_MwStaticStationTable_Object=MibTable
mwStaticStationTable=_MwStaticStationTable_Object((1,3,6,1,4,1,15983,1,1,4,16,1))
if mibBuilder.loadTexts:mwStaticStationTable.setStatus(_A)
_MwStaticStationEntry_Object=MibTableRow
mwStaticStationEntry=_MwStaticStationEntry_Object((1,3,6,1,4,1,15983,1,1,4,16,1,1))
mwStaticStationEntry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:mwStaticStationEntry.setStatus(_A)
_MwStaticStationTableIndex_Type=Integer32
_MwStaticStationTableIndex_Object=MibTableColumn
mwStaticStationTableIndex=_MwStaticStationTableIndex_Object((1,3,6,1,4,1,15983,1,1,4,16,1,1,1),_MwStaticStationTableIndex_Type())
mwStaticStationTableIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:mwStaticStationTableIndex.setStatus(_A)
_MwStaticStationIpAddress_Type=IpAddress
_MwStaticStationIpAddress_Object=MibTableColumn
mwStaticStationIpAddress=_MwStaticStationIpAddress_Object((1,3,6,1,4,1,15983,1,1,4,16,1,1,2),_MwStaticStationIpAddress_Type())
mwStaticStationIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:mwStaticStationIpAddress.setStatus(_A)
_MwStaticStationMacAddress_Type=MacAddress
_MwStaticStationMacAddress_Object=MibTableColumn
mwStaticStationMacAddress=_MwStaticStationMacAddress_Object((1,3,6,1,4,1,15983,1,1,4,16,1,1,3),_MwStaticStationMacAddress_Type())
mwStaticStationMacAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:mwStaticStationMacAddress.setStatus(_A)
_MwStaticStationRowStatus_Type=RowStatus
_MwStaticStationRowStatus_Object=MibTableColumn
mwStaticStationRowStatus=_MwStaticStationRowStatus_Object((1,3,6,1,4,1,15983,1,1,4,16,1,1,4),_MwStaticStationRowStatus_Type())
mwStaticStationRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:mwStaticStationRowStatus.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'mwConfigStaticStation':mwConfigStaticStation,'mwStaticStationTable':mwStaticStationTable,'mwStaticStationEntry':mwStaticStationEntry,_D:mwStaticStationTableIndex,'mwStaticStationIpAddress':mwStaticStationIpAddress,'mwStaticStationMacAddress':mwStaticStationMacAddress,'mwStaticStationRowStatus':mwStaticStationRowStatus})