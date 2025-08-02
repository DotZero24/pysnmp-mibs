_J='btsvAdapterIndex'
_I='btsvTeamIndex'
_H='btspAdapterIndex'
_G='btspTeamIndex'
_F='btsTeamIndex'
_E='not-accessible'
_D='QLASP-Statistics-MIB'
_C='Integer32'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
_Qlogic_ObjectIdentity=ObjectIdentity
qlogic=_Qlogic_ObjectIdentity((1,3,6,1,4,1,3873))
_Enet_ObjectIdentity=ObjectIdentity
enet=_Enet_ObjectIdentity((1,3,6,1,4,1,3873,1))
_Qlasp_ObjectIdentity=ObjectIdentity
qlasp=_Qlasp_ObjectIdentity((1,3,6,1,4,1,3873,1,2))
_QlaspStat_ObjectIdentity=ObjectIdentity
qlaspStat=_QlaspStat_ObjectIdentity((1,3,6,1,4,1,3873,1,2,2))
_QlaspTeamStat_ObjectIdentity=ObjectIdentity
qlaspTeamStat=_QlaspTeamStat_ObjectIdentity((1,3,6,1,4,1,3873,1,2,2,1))
_BtsTeamNumber_Type=Integer32
_BtsTeamNumber_Object=MibScalar
btsTeamNumber=_BtsTeamNumber_Object((1,3,6,1,4,1,3873,1,2,2,1,1),_BtsTeamNumber_Type())
btsTeamNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:btsTeamNumber.setStatus(_A)
_BtsTeamTable_Object=MibTable
btsTeamTable=_BtsTeamTable_Object((1,3,6,1,4,1,3873,1,2,2,1,2))
if mibBuilder.loadTexts:btsTeamTable.setStatus(_A)
_BtsTeamEntry_Object=MibTableRow
btsTeamEntry=_BtsTeamEntry_Object((1,3,6,1,4,1,3873,1,2,2,1,2,1))
btsTeamEntry.setIndexNames((0,_D,_F))
if mibBuilder.loadTexts:btsTeamEntry.setStatus(_A)
class _BtsTeamIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_BtsTeamIndex_Type.__name__=_C
_BtsTeamIndex_Object=MibTableColumn
btsTeamIndex=_BtsTeamIndex_Object((1,3,6,1,4,1,3873,1,2,2,1,2,1,1),_BtsTeamIndex_Type())
btsTeamIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:btsTeamIndex.setStatus(_A)
_BtsTeamName_Type=DisplayString
_BtsTeamName_Object=MibTableColumn
btsTeamName=_BtsTeamName_Object((1,3,6,1,4,1,3873,1,2,2,1,2,1,2),_BtsTeamName_Type())
btsTeamName.setMaxAccess(_B)
if mibBuilder.loadTexts:btsTeamName.setStatus(_A)
_BtsPhyNumber_Type=Integer32
_BtsPhyNumber_Object=MibTableColumn
btsPhyNumber=_BtsPhyNumber_Object((1,3,6,1,4,1,3873,1,2,2,1,2,1,3),_BtsPhyNumber_Type())
btsPhyNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:btsPhyNumber.setStatus(_A)
_BtsVirNumber_Type=Integer32
_BtsVirNumber_Object=MibTableColumn
btsVirNumber=_BtsVirNumber_Object((1,3,6,1,4,1,3873,1,2,2,1,2,1,4),_BtsVirNumber_Type())
btsVirNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:btsVirNumber.setStatus(_A)
_BtsPacketSends_Type=Counter32
_BtsPacketSends_Object=MibTableColumn
btsPacketSends=_BtsPacketSends_Object((1,3,6,1,4,1,3873,1,2,2,1,2,1,5),_BtsPacketSends_Type())
btsPacketSends.setMaxAccess(_B)
if mibBuilder.loadTexts:btsPacketSends.setStatus(_A)
_BtsPacketSendDiscardeds_Type=Counter32
_BtsPacketSendDiscardeds_Object=MibTableColumn
btsPacketSendDiscardeds=_BtsPacketSendDiscardeds_Object((1,3,6,1,4,1,3873,1,2,2,1,2,1,6),_BtsPacketSendDiscardeds_Type())
btsPacketSendDiscardeds.setMaxAccess(_B)
if mibBuilder.loadTexts:btsPacketSendDiscardeds.setStatus(_A)
_BtsPacketSendQueueds_Type=Counter32
_BtsPacketSendQueueds_Object=MibTableColumn
btsPacketSendQueueds=_BtsPacketSendQueueds_Object((1,3,6,1,4,1,3873,1,2,2,1,2,1,7),_BtsPacketSendQueueds_Type())
btsPacketSendQueueds.setMaxAccess(_B)
if mibBuilder.loadTexts:btsPacketSendQueueds.setStatus(_A)
_BtsPacketRecvs_Type=Counter32
_BtsPacketRecvs_Object=MibTableColumn
btsPacketRecvs=_BtsPacketRecvs_Object((1,3,6,1,4,1,3873,1,2,2,1,2,1,8),_BtsPacketRecvs_Type())
btsPacketRecvs.setMaxAccess(_B)
if mibBuilder.loadTexts:btsPacketRecvs.setStatus(_A)
_BtsPacketRecvDiscardeds_Type=Counter32
_BtsPacketRecvDiscardeds_Object=MibTableColumn
btsPacketRecvDiscardeds=_BtsPacketRecvDiscardeds_Object((1,3,6,1,4,1,3873,1,2,2,1,2,1,9),_BtsPacketRecvDiscardeds_Type())
btsPacketRecvDiscardeds.setMaxAccess(_B)
if mibBuilder.loadTexts:btsPacketRecvDiscardeds.setStatus(_A)
_BtsLinkPacketsSents_Type=Counter32
_BtsLinkPacketsSents_Object=MibTableColumn
btsLinkPacketsSents=_BtsLinkPacketsSents_Object((1,3,6,1,4,1,3873,1,2,2,1,2,1,10),_BtsLinkPacketsSents_Type())
btsLinkPacketsSents.setMaxAccess(_B)
if mibBuilder.loadTexts:btsLinkPacketsSents.setStatus(_A)
_BtsLinkPacketsRetrieds_Type=Counter32
_BtsLinkPacketsRetrieds_Object=MibTableColumn
btsLinkPacketsRetrieds=_BtsLinkPacketsRetrieds_Object((1,3,6,1,4,1,3873,1,2,2,1,2,1,11),_BtsLinkPacketsRetrieds_Type())
btsLinkPacketsRetrieds.setMaxAccess(_B)
if mibBuilder.loadTexts:btsLinkPacketsRetrieds.setStatus(_A)
_QlaspPhyAdapterStat_ObjectIdentity=ObjectIdentity
qlaspPhyAdapterStat=_QlaspPhyAdapterStat_ObjectIdentity((1,3,6,1,4,1,3873,1,2,2,2))
_BtsPhyAdapterNumber_Type=Integer32
_BtsPhyAdapterNumber_Object=MibScalar
btsPhyAdapterNumber=_BtsPhyAdapterNumber_Object((1,3,6,1,4,1,3873,1,2,2,2,1),_BtsPhyAdapterNumber_Type())
btsPhyAdapterNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:btsPhyAdapterNumber.setStatus(_A)
_BtsPhyAdapterStatTable_Object=MibTable
btsPhyAdapterStatTable=_BtsPhyAdapterStatTable_Object((1,3,6,1,4,1,3873,1,2,2,2,2))
if mibBuilder.loadTexts:btsPhyAdapterStatTable.setStatus(_A)
_BtsPhyAdapterStatEntry_Object=MibTableRow
btsPhyAdapterStatEntry=_BtsPhyAdapterStatEntry_Object((1,3,6,1,4,1,3873,1,2,2,2,2,1))
btsPhyAdapterStatEntry.setIndexNames((0,_D,_G),(0,_D,_H))
if mibBuilder.loadTexts:btsPhyAdapterStatEntry.setStatus(_A)
class _BtspTeamIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_BtspTeamIndex_Type.__name__=_C
_BtspTeamIndex_Object=MibTableColumn
btspTeamIndex=_BtspTeamIndex_Object((1,3,6,1,4,1,3873,1,2,2,2,2,1,1),_BtspTeamIndex_Type())
btspTeamIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:btspTeamIndex.setStatus(_A)
class _BtspAdapterIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_BtspAdapterIndex_Type.__name__=_C
_BtspAdapterIndex_Object=MibTableColumn
btspAdapterIndex=_BtspAdapterIndex_Object((1,3,6,1,4,1,3873,1,2,2,2,2,1,2),_BtspAdapterIndex_Type())
btspAdapterIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:btspAdapterIndex.setStatus(_A)
_BtspAdapterDesc_Type=DisplayString
_BtspAdapterDesc_Object=MibTableColumn
btspAdapterDesc=_BtspAdapterDesc_Object((1,3,6,1,4,1,3873,1,2,2,2,2,1,3),_BtspAdapterDesc_Type())
btspAdapterDesc.setMaxAccess(_B)
if mibBuilder.loadTexts:btspAdapterDesc.setStatus(_A)
_BtspPacketSends_Type=Counter32
_BtspPacketSends_Object=MibTableColumn
btspPacketSends=_BtspPacketSends_Object((1,3,6,1,4,1,3873,1,2,2,2,2,1,4),_BtspPacketSends_Type())
btspPacketSends.setMaxAccess(_B)
if mibBuilder.loadTexts:btspPacketSends.setStatus(_A)
_BtspPacketSendDiscardeds_Type=Counter32
_BtspPacketSendDiscardeds_Object=MibTableColumn
btspPacketSendDiscardeds=_BtspPacketSendDiscardeds_Object((1,3,6,1,4,1,3873,1,2,2,2,2,1,5),_BtspPacketSendDiscardeds_Type())
btspPacketSendDiscardeds.setMaxAccess(_B)
if mibBuilder.loadTexts:btspPacketSendDiscardeds.setStatus(_A)
_BtspPacketRecvs_Type=Counter32
_BtspPacketRecvs_Object=MibTableColumn
btspPacketRecvs=_BtspPacketRecvs_Object((1,3,6,1,4,1,3873,1,2,2,2,2,1,6),_BtspPacketRecvs_Type())
btspPacketRecvs.setMaxAccess(_B)
if mibBuilder.loadTexts:btspPacketRecvs.setStatus(_A)
_BtspPacketRecvDiscardeds_Type=Counter32
_BtspPacketRecvDiscardeds_Object=MibTableColumn
btspPacketRecvDiscardeds=_BtspPacketRecvDiscardeds_Object((1,3,6,1,4,1,3873,1,2,2,2,2,1,7),_BtspPacketRecvDiscardeds_Type())
btspPacketRecvDiscardeds.setMaxAccess(_B)
if mibBuilder.loadTexts:btspPacketRecvDiscardeds.setStatus(_A)
_BtspLinkPacketsSents_Type=Counter32
_BtspLinkPacketsSents_Object=MibTableColumn
btspLinkPacketsSents=_BtspLinkPacketsSents_Object((1,3,6,1,4,1,3873,1,2,2,2,2,1,8),_BtspLinkPacketsSents_Type())
btspLinkPacketsSents.setMaxAccess(_B)
if mibBuilder.loadTexts:btspLinkPacketsSents.setStatus(_A)
_BtspLinkPacketsRetrieds_Type=Counter32
_BtspLinkPacketsRetrieds_Object=MibTableColumn
btspLinkPacketsRetrieds=_BtspLinkPacketsRetrieds_Object((1,3,6,1,4,1,3873,1,2,2,2,2,1,9),_BtspLinkPacketsRetrieds_Type())
btspLinkPacketsRetrieds.setMaxAccess(_B)
if mibBuilder.loadTexts:btspLinkPacketsRetrieds.setStatus(_A)
_QlaspVirAdapterStat_ObjectIdentity=ObjectIdentity
qlaspVirAdapterStat=_QlaspVirAdapterStat_ObjectIdentity((1,3,6,1,4,1,3873,1,2,2,3))
_BtsVirAdapterNumber_Type=Integer32
_BtsVirAdapterNumber_Object=MibScalar
btsVirAdapterNumber=_BtsVirAdapterNumber_Object((1,3,6,1,4,1,3873,1,2,2,3,1),_BtsVirAdapterNumber_Type())
btsVirAdapterNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:btsVirAdapterNumber.setStatus(_A)
_BtsVirAdapterStatTable_Object=MibTable
btsVirAdapterStatTable=_BtsVirAdapterStatTable_Object((1,3,6,1,4,1,3873,1,2,2,3,2))
if mibBuilder.loadTexts:btsVirAdapterStatTable.setStatus(_A)
_BtsVirAdapterStatEntry_Object=MibTableRow
btsVirAdapterStatEntry=_BtsVirAdapterStatEntry_Object((1,3,6,1,4,1,3873,1,2,2,3,2,1))
btsVirAdapterStatEntry.setIndexNames((0,_D,_I),(0,_D,_J))
if mibBuilder.loadTexts:btsVirAdapterStatEntry.setStatus(_A)
class _BtsvTeamIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_BtsvTeamIndex_Type.__name__=_C
_BtsvTeamIndex_Object=MibTableColumn
btsvTeamIndex=_BtsvTeamIndex_Object((1,3,6,1,4,1,3873,1,2,2,3,2,1,1),_BtsvTeamIndex_Type())
btsvTeamIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:btsvTeamIndex.setStatus(_A)
class _BtsvAdapterIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_BtsvAdapterIndex_Type.__name__=_C
_BtsvAdapterIndex_Object=MibTableColumn
btsvAdapterIndex=_BtsvAdapterIndex_Object((1,3,6,1,4,1,3873,1,2,2,3,2,1,2),_BtsvAdapterIndex_Type())
btsvAdapterIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:btsvAdapterIndex.setStatus(_A)
_BtsvAdapterDesc_Type=DisplayString
_BtsvAdapterDesc_Object=MibTableColumn
btsvAdapterDesc=_BtsvAdapterDesc_Object((1,3,6,1,4,1,3873,1,2,2,3,2,1,3),_BtsvAdapterDesc_Type())
btsvAdapterDesc.setMaxAccess(_B)
if mibBuilder.loadTexts:btsvAdapterDesc.setStatus(_A)
_BtsvPacketSends_Type=Counter32
_BtsvPacketSends_Object=MibTableColumn
btsvPacketSends=_BtsvPacketSends_Object((1,3,6,1,4,1,3873,1,2,2,3,2,1,4),_BtsvPacketSends_Type())
btsvPacketSends.setMaxAccess(_B)
if mibBuilder.loadTexts:btsvPacketSends.setStatus(_A)
_BtsvPacketSendQueueds_Type=Counter32
_BtsvPacketSendQueueds_Object=MibTableColumn
btsvPacketSendQueueds=_BtsvPacketSendQueueds_Object((1,3,6,1,4,1,3873,1,2,2,3,2,1,5),_BtsvPacketSendQueueds_Type())
btsvPacketSendQueueds.setMaxAccess(_B)
if mibBuilder.loadTexts:btsvPacketSendQueueds.setStatus(_A)
_BtsvPacketRecvs_Type=Counter32
_BtsvPacketRecvs_Object=MibTableColumn
btsvPacketRecvs=_BtsvPacketRecvs_Object((1,3,6,1,4,1,3873,1,2,2,3,2,1,6),_BtsvPacketRecvs_Type())
btsvPacketRecvs.setMaxAccess(_B)
if mibBuilder.loadTexts:btsvPacketRecvs.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'qlogic':qlogic,'enet':enet,'qlasp':qlasp,'qlaspStat':qlaspStat,'qlaspTeamStat':qlaspTeamStat,'btsTeamNumber':btsTeamNumber,'btsTeamTable':btsTeamTable,'btsTeamEntry':btsTeamEntry,_F:btsTeamIndex,'btsTeamName':btsTeamName,'btsPhyNumber':btsPhyNumber,'btsVirNumber':btsVirNumber,'btsPacketSends':btsPacketSends,'btsPacketSendDiscardeds':btsPacketSendDiscardeds,'btsPacketSendQueueds':btsPacketSendQueueds,'btsPacketRecvs':btsPacketRecvs,'btsPacketRecvDiscardeds':btsPacketRecvDiscardeds,'btsLinkPacketsSents':btsLinkPacketsSents,'btsLinkPacketsRetrieds':btsLinkPacketsRetrieds,'qlaspPhyAdapterStat':qlaspPhyAdapterStat,'btsPhyAdapterNumber':btsPhyAdapterNumber,'btsPhyAdapterStatTable':btsPhyAdapterStatTable,'btsPhyAdapterStatEntry':btsPhyAdapterStatEntry,_G:btspTeamIndex,_H:btspAdapterIndex,'btspAdapterDesc':btspAdapterDesc,'btspPacketSends':btspPacketSends,'btspPacketSendDiscardeds':btspPacketSendDiscardeds,'btspPacketRecvs':btspPacketRecvs,'btspPacketRecvDiscardeds':btspPacketRecvDiscardeds,'btspLinkPacketsSents':btspLinkPacketsSents,'btspLinkPacketsRetrieds':btspLinkPacketsRetrieds,'qlaspVirAdapterStat':qlaspVirAdapterStat,'btsVirAdapterNumber':btsVirAdapterNumber,'btsVirAdapterStatTable':btsVirAdapterStatTable,'btsVirAdapterStatEntry':btsVirAdapterStatEntry,_I:btsvTeamIndex,_J:btsvAdapterIndex,'btsvAdapterDesc':btsvAdapterDesc,'btsvPacketSends':btsvPacketSends,'btsvPacketSendQueueds':btsvPacketSendQueueds,'btsvPacketRecvs':btsvPacketRecvs})