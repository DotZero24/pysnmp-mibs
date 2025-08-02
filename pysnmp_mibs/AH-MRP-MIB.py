_F='ahNeighberAPId'
_E='AH-MRP-MIB'
_D='ifIndex'
_C='IF-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
AhNodeID,AhString,ahAPMRP=mibBuilder.importSymbols('AH-SMI-MIB','AhNodeID','AhString','ahAPMRP')
ifEntry,ifIndex=mibBuilder.importSymbols(_C,'ifEntry',_D)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
ahMRP=ModuleIdentity((1,3,6,1,4,1,26928,1,1,1,3,1))
class AhLinkType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('ahETHERNET',0),('ahWIRELESS',1)))
_AhNeighborTable_Object=MibTable
ahNeighborTable=_AhNeighborTable_Object((1,3,6,1,4,1,26928,1,1,1,3,1,1))
if mibBuilder.loadTexts:ahNeighborTable.setStatus(_A)
_AhNeighborEntry_Object=MibTableRow
ahNeighborEntry=_AhNeighborEntry_Object((1,3,6,1,4,1,26928,1,1,1,3,1,1,1))
ahNeighborEntry.setIndexNames((0,_C,_D),(0,_E,_F))
if mibBuilder.loadTexts:ahNeighborEntry.setStatus(_A)
_AhNeighberAPId_Type=AhNodeID
_AhNeighberAPId_Object=MibTableColumn
ahNeighberAPId=_AhNeighberAPId_Object((1,3,6,1,4,1,26928,1,1,1,3,1,1,1,1),_AhNeighberAPId_Type())
ahNeighberAPId.setMaxAccess(_B)
if mibBuilder.loadTexts:ahNeighberAPId.setStatus(_A)
_AhLinkCost_Type=Counter32
_AhLinkCost_Object=MibTableColumn
ahLinkCost=_AhLinkCost_Object((1,3,6,1,4,1,26928,1,1,1,3,1,1,1,2),_AhLinkCost_Type())
ahLinkCost.setMaxAccess(_B)
if mibBuilder.loadTexts:ahLinkCost.setStatus(_A)
_AhRSSI_Type=Integer32
_AhRSSI_Object=MibTableColumn
ahRSSI=_AhRSSI_Object((1,3,6,1,4,1,26928,1,1,1,3,1,1,1,3),_AhRSSI_Type())
ahRSSI.setMaxAccess(_B)
if mibBuilder.loadTexts:ahRSSI.setStatus(_A)
_AhLinkUptime_Type=Counter32
_AhLinkUptime_Object=MibTableColumn
ahLinkUptime=_AhLinkUptime_Object((1,3,6,1,4,1,26928,1,1,1,3,1,1,1,4),_AhLinkUptime_Type())
ahLinkUptime.setMaxAccess(_B)
if mibBuilder.loadTexts:ahLinkUptime.setStatus(_A)
_AhLinkType_Type=AhLinkType
_AhLinkType_Object=MibTableColumn
ahLinkType=_AhLinkType_Object((1,3,6,1,4,1,26928,1,1,1,3,1,1,1,5),_AhLinkType_Type())
ahLinkType.setMaxAccess(_B)
if mibBuilder.loadTexts:ahLinkType.setStatus(_A)
_AhRxDataFrames_Type=Counter32
_AhRxDataFrames_Object=MibTableColumn
ahRxDataFrames=_AhRxDataFrames_Object((1,3,6,1,4,1,26928,1,1,1,3,1,1,1,6),_AhRxDataFrames_Type())
ahRxDataFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:ahRxDataFrames.setStatus(_A)
_AhRXDataOctets_Type=Counter32
_AhRXDataOctets_Object=MibTableColumn
ahRXDataOctets=_AhRXDataOctets_Object((1,3,6,1,4,1,26928,1,1,1,3,1,1,1,7),_AhRXDataOctets_Type())
ahRXDataOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:ahRXDataOctets.setStatus(_A)
_AhRxMgtFrames_Type=Counter32
_AhRxMgtFrames_Object=MibTableColumn
ahRxMgtFrames=_AhRxMgtFrames_Object((1,3,6,1,4,1,26928,1,1,1,3,1,1,1,8),_AhRxMgtFrames_Type())
ahRxMgtFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:ahRxMgtFrames.setStatus(_A)
_AhRxUnicastFrames_Type=Counter32
_AhRxUnicastFrames_Object=MibTableColumn
ahRxUnicastFrames=_AhRxUnicastFrames_Object((1,3,6,1,4,1,26928,1,1,1,3,1,1,1,9),_AhRxUnicastFrames_Type())
ahRxUnicastFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:ahRxUnicastFrames.setStatus(_A)
_AhRxMulticastFrames_Type=Counter32
_AhRxMulticastFrames_Object=MibTableColumn
ahRxMulticastFrames=_AhRxMulticastFrames_Object((1,3,6,1,4,1,26928,1,1,1,3,1,1,1,10),_AhRxMulticastFrames_Type())
ahRxMulticastFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:ahRxMulticastFrames.setStatus(_A)
_AhRxBroadcastFrames_Type=Counter32
_AhRxBroadcastFrames_Object=MibTableColumn
ahRxBroadcastFrames=_AhRxBroadcastFrames_Object((1,3,6,1,4,1,26928,1,1,1,3,1,1,1,11),_AhRxBroadcastFrames_Type())
ahRxBroadcastFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:ahRxBroadcastFrames.setStatus(_A)
_AhTxDataFrames_Type=Counter32
_AhTxDataFrames_Object=MibTableColumn
ahTxDataFrames=_AhTxDataFrames_Object((1,3,6,1,4,1,26928,1,1,1,3,1,1,1,12),_AhTxDataFrames_Type())
ahTxDataFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:ahTxDataFrames.setStatus(_A)
_AhTxMgtFrames_Type=Counter32
_AhTxMgtFrames_Object=MibTableColumn
ahTxMgtFrames=_AhTxMgtFrames_Object((1,3,6,1,4,1,26928,1,1,1,3,1,1,1,13),_AhTxMgtFrames_Type())
ahTxMgtFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:ahTxMgtFrames.setStatus(_A)
_AhTxDataOctets_Type=Counter32
_AhTxDataOctets_Object=MibTableColumn
ahTxDataOctets=_AhTxDataOctets_Object((1,3,6,1,4,1,26928,1,1,1,3,1,1,1,14),_AhTxDataOctets_Type())
ahTxDataOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:ahTxDataOctets.setStatus(_A)
_AhTxUnicastFrames_Type=Counter32
_AhTxUnicastFrames_Object=MibTableColumn
ahTxUnicastFrames=_AhTxUnicastFrames_Object((1,3,6,1,4,1,26928,1,1,1,3,1,1,1,15),_AhTxUnicastFrames_Type())
ahTxUnicastFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:ahTxUnicastFrames.setStatus(_A)
_AhTxMulticastFrames_Type=Counter32
_AhTxMulticastFrames_Object=MibTableColumn
ahTxMulticastFrames=_AhTxMulticastFrames_Object((1,3,6,1,4,1,26928,1,1,1,3,1,1,1,16),_AhTxMulticastFrames_Type())
ahTxMulticastFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:ahTxMulticastFrames.setStatus(_A)
_AhTxBroadcastFrames_Type=Counter32
_AhTxBroadcastFrames_Object=MibTableColumn
ahTxBroadcastFrames=_AhTxBroadcastFrames_Object((1,3,6,1,4,1,26928,1,1,1,3,1,1,1,17),_AhTxBroadcastFrames_Type())
ahTxBroadcastFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:ahTxBroadcastFrames.setStatus(_A)
_AhTxBeDataFrames_Type=Counter32
_AhTxBeDataFrames_Object=MibTableColumn
ahTxBeDataFrames=_AhTxBeDataFrames_Object((1,3,6,1,4,1,26928,1,1,1,3,1,1,1,18),_AhTxBeDataFrames_Type())
ahTxBeDataFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:ahTxBeDataFrames.setStatus(_A)
_AhTxBgDataFrames_Type=Counter32
_AhTxBgDataFrames_Object=MibTableColumn
ahTxBgDataFrames=_AhTxBgDataFrames_Object((1,3,6,1,4,1,26928,1,1,1,3,1,1,1,19),_AhTxBgDataFrames_Type())
ahTxBgDataFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:ahTxBgDataFrames.setStatus(_A)
_AhTxViDataFrames_Type=Counter32
_AhTxViDataFrames_Object=MibTableColumn
ahTxViDataFrames=_AhTxViDataFrames_Object((1,3,6,1,4,1,26928,1,1,1,3,1,1,1,20),_AhTxViDataFrames_Type())
ahTxViDataFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:ahTxViDataFrames.setStatus(_A)
_AhTxVoDataFrames_Type=Counter32
_AhTxVoDataFrames_Object=MibTableColumn
ahTxVoDataFrames=_AhTxVoDataFrames_Object((1,3,6,1,4,1,26928,1,1,1,3,1,1,1,21),_AhTxVoDataFrames_Type())
ahTxVoDataFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:ahTxVoDataFrames.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'AhLinkType':AhLinkType,'ahMRP':ahMRP,'ahNeighborTable':ahNeighborTable,'ahNeighborEntry':ahNeighborEntry,_F:ahNeighberAPId,'ahLinkCost':ahLinkCost,'ahRSSI':ahRSSI,'ahLinkUptime':ahLinkUptime,'ahLinkType':ahLinkType,'ahRxDataFrames':ahRxDataFrames,'ahRXDataOctets':ahRXDataOctets,'ahRxMgtFrames':ahRxMgtFrames,'ahRxUnicastFrames':ahRxUnicastFrames,'ahRxMulticastFrames':ahRxMulticastFrames,'ahRxBroadcastFrames':ahRxBroadcastFrames,'ahTxDataFrames':ahTxDataFrames,'ahTxMgtFrames':ahTxMgtFrames,'ahTxDataOctets':ahTxDataOctets,'ahTxUnicastFrames':ahTxUnicastFrames,'ahTxMulticastFrames':ahTxMulticastFrames,'ahTxBroadcastFrames':ahTxBroadcastFrames,'ahTxBeDataFrames':ahTxBeDataFrames,'ahTxBgDataFrames':ahTxBgDataFrames,'ahTxViDataFrames':ahTxViDataFrames,'ahTxVoDataFrames':ahTxVoDataFrames})