_J='lldpGlobalCountNeighborAged'
_I='lldpGlobalCountNeighborDroped'
_H='lldpGlobalCountNeighborDeleted'
_G='lldpGlobalCountNeighborInserted'
_F='ifIndex'
_E='IF-MIB'
_D='OctetString'
_C='TPLINK-LLDPCOUNT-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_D,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_E,_F)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
tplinkLldpMIBNotifications,tplinkLldpMIBObjects=mibBuilder.importSymbols('TPLINK-LLDP-MIB','tplinkLldpMIBNotifications','tplinkLldpMIBObjects')
class MacAddress(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
_LldpCount_ObjectIdentity=ObjectIdentity
lldpCount=_LldpCount_ObjectIdentity((1,3,6,1,4,1,11863,6,35,1,3))
_LldpGlobalCount_ObjectIdentity=ObjectIdentity
lldpGlobalCount=_LldpGlobalCount_ObjectIdentity((1,3,6,1,4,1,11863,6,35,1,3,1))
class _LldpGlobalCountUpdateTime_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_LldpGlobalCountUpdateTime_Type.__name__=_D
_LldpGlobalCountUpdateTime_Object=MibScalar
lldpGlobalCountUpdateTime=_LldpGlobalCountUpdateTime_Object((1,3,6,1,4,1,11863,6,35,1,3,1,1),_LldpGlobalCountUpdateTime_Type())
lldpGlobalCountUpdateTime.setMaxAccess(_B)
if mibBuilder.loadTexts:lldpGlobalCountUpdateTime.setStatus(_A)
_LldpGlobalCountNeighborInserted_Type=Integer32
_LldpGlobalCountNeighborInserted_Object=MibScalar
lldpGlobalCountNeighborInserted=_LldpGlobalCountNeighborInserted_Object((1,3,6,1,4,1,11863,6,35,1,3,1,2),_LldpGlobalCountNeighborInserted_Type())
lldpGlobalCountNeighborInserted.setMaxAccess(_B)
if mibBuilder.loadTexts:lldpGlobalCountNeighborInserted.setStatus(_A)
_LldpGlobalCountNeighborDeleted_Type=Integer32
_LldpGlobalCountNeighborDeleted_Object=MibScalar
lldpGlobalCountNeighborDeleted=_LldpGlobalCountNeighborDeleted_Object((1,3,6,1,4,1,11863,6,35,1,3,1,3),_LldpGlobalCountNeighborDeleted_Type())
lldpGlobalCountNeighborDeleted.setMaxAccess(_B)
if mibBuilder.loadTexts:lldpGlobalCountNeighborDeleted.setStatus(_A)
_LldpGlobalCountNeighborDroped_Type=Integer32
_LldpGlobalCountNeighborDroped_Object=MibScalar
lldpGlobalCountNeighborDroped=_LldpGlobalCountNeighborDroped_Object((1,3,6,1,4,1,11863,6,35,1,3,1,4),_LldpGlobalCountNeighborDroped_Type())
lldpGlobalCountNeighborDroped.setMaxAccess(_B)
if mibBuilder.loadTexts:lldpGlobalCountNeighborDroped.setStatus(_A)
_LldpGlobalCountNeighborAged_Type=Integer32
_LldpGlobalCountNeighborAged_Object=MibScalar
lldpGlobalCountNeighborAged=_LldpGlobalCountNeighborAged_Object((1,3,6,1,4,1,11863,6,35,1,3,1,5),_LldpGlobalCountNeighborAged_Type())
lldpGlobalCountNeighborAged.setMaxAccess(_B)
if mibBuilder.loadTexts:lldpGlobalCountNeighborAged.setStatus(_A)
_LldpCountNeighborInfoTable_Object=MibTable
lldpCountNeighborInfoTable=_LldpCountNeighborInfoTable_Object((1,3,6,1,4,1,11863,6,35,1,3,2))
if mibBuilder.loadTexts:lldpCountNeighborInfoTable.setStatus(_A)
_LldpCountNeighborInfoEntry_Object=MibTableRow
lldpCountNeighborInfoEntry=_LldpCountNeighborInfoEntry_Object((1,3,6,1,4,1,11863,6,35,1,3,2,1))
lldpCountNeighborInfoEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:lldpCountNeighborInfoEntry.setStatus(_A)
class _LldpCountNeighborPortId_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_LldpCountNeighborPortId_Type.__name__=_D
_LldpCountNeighborPortId_Object=MibTableColumn
lldpCountNeighborPortId=_LldpCountNeighborPortId_Object((1,3,6,1,4,1,11863,6,35,1,3,2,1,1),_LldpCountNeighborPortId_Type())
lldpCountNeighborPortId.setMaxAccess(_B)
if mibBuilder.loadTexts:lldpCountNeighborPortId.setStatus(_A)
_LldpNeighborFramesOut_Type=Integer32
_LldpNeighborFramesOut_Object=MibTableColumn
lldpNeighborFramesOut=_LldpNeighborFramesOut_Object((1,3,6,1,4,1,11863,6,35,1,3,2,1,2),_LldpNeighborFramesOut_Type())
lldpNeighborFramesOut.setMaxAccess(_B)
if mibBuilder.loadTexts:lldpNeighborFramesOut.setStatus(_A)
_LldpNeighborFramesIn_Type=Integer32
_LldpNeighborFramesIn_Object=MibTableColumn
lldpNeighborFramesIn=_LldpNeighborFramesIn_Object((1,3,6,1,4,1,11863,6,35,1,3,2,1,3),_LldpNeighborFramesIn_Type())
lldpNeighborFramesIn.setMaxAccess(_B)
if mibBuilder.loadTexts:lldpNeighborFramesIn.setStatus(_A)
_LldpNeighborFramesDiscarded_Type=Integer32
_LldpNeighborFramesDiscarded_Object=MibTableColumn
lldpNeighborFramesDiscarded=_LldpNeighborFramesDiscarded_Object((1,3,6,1,4,1,11863,6,35,1,3,2,1,4),_LldpNeighborFramesDiscarded_Type())
lldpNeighborFramesDiscarded.setMaxAccess(_B)
if mibBuilder.loadTexts:lldpNeighborFramesDiscarded.setStatus(_A)
_LldpNeighborFramesInErrors_Type=Integer32
_LldpNeighborFramesInErrors_Object=MibTableColumn
lldpNeighborFramesInErrors=_LldpNeighborFramesInErrors_Object((1,3,6,1,4,1,11863,6,35,1,3,2,1,5),_LldpNeighborFramesInErrors_Type())
lldpNeighborFramesInErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:lldpNeighborFramesInErrors.setStatus(_A)
_LldpNeighborAgeOuts_Type=Integer32
_LldpNeighborAgeOuts_Object=MibTableColumn
lldpNeighborAgeOuts=_LldpNeighborAgeOuts_Object((1,3,6,1,4,1,11863,6,35,1,3,2,1,6),_LldpNeighborAgeOuts_Type())
lldpNeighborAgeOuts.setMaxAccess(_B)
if mibBuilder.loadTexts:lldpNeighborAgeOuts.setStatus(_A)
_LldpNeighborTlvDiscarded_Type=Integer32
_LldpNeighborTlvDiscarded_Object=MibTableColumn
lldpNeighborTlvDiscarded=_LldpNeighborTlvDiscarded_Object((1,3,6,1,4,1,11863,6,35,1,3,2,1,7),_LldpNeighborTlvDiscarded_Type())
lldpNeighborTlvDiscarded.setMaxAccess(_B)
if mibBuilder.loadTexts:lldpNeighborTlvDiscarded.setStatus(_A)
_LldpNeighborTlvUnrecognized_Type=Integer32
_LldpNeighborTlvUnrecognized_Object=MibTableColumn
lldpNeighborTlvUnrecognized=_LldpNeighborTlvUnrecognized_Object((1,3,6,1,4,1,11863,6,35,1,3,2,1,8),_LldpNeighborTlvUnrecognized_Type())
lldpNeighborTlvUnrecognized.setMaxAccess(_B)
if mibBuilder.loadTexts:lldpNeighborTlvUnrecognized.setStatus(_A)
lldpNeighborChange=NotificationType((1,3,6,1,4,1,11863,6,35,2,1))
lldpNeighborChange.setObjects(*((_C,_G),(_C,_H),(_C,_I),(_C,_J)))
if mibBuilder.loadTexts:lldpNeighborChange.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'MacAddress':MacAddress,'lldpCount':lldpCount,'lldpGlobalCount':lldpGlobalCount,'lldpGlobalCountUpdateTime':lldpGlobalCountUpdateTime,_G:lldpGlobalCountNeighborInserted,_H:lldpGlobalCountNeighborDeleted,_I:lldpGlobalCountNeighborDroped,_J:lldpGlobalCountNeighborAged,'lldpCountNeighborInfoTable':lldpCountNeighborInfoTable,'lldpCountNeighborInfoEntry':lldpCountNeighborInfoEntry,'lldpCountNeighborPortId':lldpCountNeighborPortId,'lldpNeighborFramesOut':lldpNeighborFramesOut,'lldpNeighborFramesIn':lldpNeighborFramesIn,'lldpNeighborFramesDiscarded':lldpNeighborFramesDiscarded,'lldpNeighborFramesInErrors':lldpNeighborFramesInErrors,'lldpNeighborAgeOuts':lldpNeighborAgeOuts,'lldpNeighborTlvDiscarded':lldpNeighborTlvDiscarded,'lldpNeighborTlvUnrecognized':lldpNeighborTlvUnrecognized,'lldpNeighborChange':lldpNeighborChange})