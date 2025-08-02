_N='ciscoPrpMIBNotificationGroup'
_M='ciscoPrpMIBMainObjectGroup'
_L='ciscoPrpLanBStateChange'
_K='ciscoPrpLanAStateChange'
_J='ciscoPrpChannelStateChange'
_I='ciscoPrpChannelIndex'
_H='ciscoPrpChannelLanBStatus'
_G='ciscoPrpChannelLanAStatus'
_F='ciscoPrpChannelStatus'
_E='ciscoPrpChannelName'
_D='ciscoPrpChannelId'
_C='read-only'
_B='current'
_A='CISCO-PRP-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
ciscoPrpMIB=ModuleIdentity((1,3,6,1,4,1,9,9,866))
if mibBuilder.loadTexts:ciscoPrpMIB.setRevisions(('2019-09-11 00:00',))
class PrpStatus(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('undefined',0),('stateUp',1),('stateDown',2)))
_CiscoPrpMIBNotifs_ObjectIdentity=ObjectIdentity
ciscoPrpMIBNotifs=_CiscoPrpMIBNotifs_ObjectIdentity((1,3,6,1,4,1,9,9,866,0))
_CiscoPrpMIBObjects_ObjectIdentity=ObjectIdentity
ciscoPrpMIBObjects=_CiscoPrpMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,866,1))
_CiscoPrpChannelTable_Object=MibTable
ciscoPrpChannelTable=_CiscoPrpChannelTable_Object((1,3,6,1,4,1,9,9,866,1,1))
if mibBuilder.loadTexts:ciscoPrpChannelTable.setStatus(_B)
_CiscoPrpChannelEntry_Object=MibTableRow
ciscoPrpChannelEntry=_CiscoPrpChannelEntry_Object((1,3,6,1,4,1,9,9,866,1,1,1))
ciscoPrpChannelEntry.setIndexNames((0,_A,_I))
if mibBuilder.loadTexts:ciscoPrpChannelEntry.setStatus(_B)
_CiscoPrpChannelIndex_Type=Unsigned32
_CiscoPrpChannelIndex_Object=MibTableColumn
ciscoPrpChannelIndex=_CiscoPrpChannelIndex_Object((1,3,6,1,4,1,9,9,866,1,1,1,1),_CiscoPrpChannelIndex_Type())
ciscoPrpChannelIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:ciscoPrpChannelIndex.setStatus(_B)
_CiscoPrpChannelId_Type=Unsigned32
_CiscoPrpChannelId_Object=MibTableColumn
ciscoPrpChannelId=_CiscoPrpChannelId_Object((1,3,6,1,4,1,9,9,866,1,1,1,2),_CiscoPrpChannelId_Type())
ciscoPrpChannelId.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoPrpChannelId.setStatus(_B)
_CiscoPrpChannelName_Type=DisplayString
_CiscoPrpChannelName_Object=MibTableColumn
ciscoPrpChannelName=_CiscoPrpChannelName_Object((1,3,6,1,4,1,9,9,866,1,1,1,3),_CiscoPrpChannelName_Type())
ciscoPrpChannelName.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoPrpChannelName.setStatus(_B)
_CiscoPrpChannelStatus_Type=PrpStatus
_CiscoPrpChannelStatus_Object=MibTableColumn
ciscoPrpChannelStatus=_CiscoPrpChannelStatus_Object((1,3,6,1,4,1,9,9,866,1,1,1,4),_CiscoPrpChannelStatus_Type())
ciscoPrpChannelStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoPrpChannelStatus.setStatus(_B)
_CiscoPrpChannelLanAStatus_Type=PrpStatus
_CiscoPrpChannelLanAStatus_Object=MibTableColumn
ciscoPrpChannelLanAStatus=_CiscoPrpChannelLanAStatus_Object((1,3,6,1,4,1,9,9,866,1,1,1,5),_CiscoPrpChannelLanAStatus_Type())
ciscoPrpChannelLanAStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoPrpChannelLanAStatus.setStatus(_B)
_CiscoPrpChannelLanBStatus_Type=PrpStatus
_CiscoPrpChannelLanBStatus_Object=MibTableColumn
ciscoPrpChannelLanBStatus=_CiscoPrpChannelLanBStatus_Object((1,3,6,1,4,1,9,9,866,1,1,1,6),_CiscoPrpChannelLanBStatus_Type())
ciscoPrpChannelLanBStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoPrpChannelLanBStatus.setStatus(_B)
_CiscoPrpMIBConform_ObjectIdentity=ObjectIdentity
ciscoPrpMIBConform=_CiscoPrpMIBConform_ObjectIdentity((1,3,6,1,4,1,9,9,866,2))
_CiscoPrpMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoPrpMIBCompliances=_CiscoPrpMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,866,2,1))
_CiscoPrpMIBGroups_ObjectIdentity=ObjectIdentity
ciscoPrpMIBGroups=_CiscoPrpMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,866,2,2))
ciscoPrpMIBMainObjectGroup=ObjectGroup((1,3,6,1,4,1,9,9,866,2,2,1))
ciscoPrpMIBMainObjectGroup.setObjects(*((_A,_D),(_A,_F),(_A,_G),(_A,_H),(_A,_E)))
if mibBuilder.loadTexts:ciscoPrpMIBMainObjectGroup.setStatus(_B)
ciscoPrpChannelStateChange=NotificationType((1,3,6,1,4,1,9,9,866,0,1))
ciscoPrpChannelStateChange.setObjects(*((_A,_D),(_A,_E),(_A,_F)))
if mibBuilder.loadTexts:ciscoPrpChannelStateChange.setStatus(_B)
ciscoPrpLanAStateChange=NotificationType((1,3,6,1,4,1,9,9,866,0,2))
ciscoPrpLanAStateChange.setObjects(*((_A,_D),(_A,_E),(_A,_G)))
if mibBuilder.loadTexts:ciscoPrpLanAStateChange.setStatus(_B)
ciscoPrpLanBStateChange=NotificationType((1,3,6,1,4,1,9,9,866,0,3))
ciscoPrpLanBStateChange.setObjects(*((_A,_D),(_A,_E),(_A,_H)))
if mibBuilder.loadTexts:ciscoPrpLanBStateChange.setStatus(_B)
ciscoPrpMIBNotificationGroup=NotificationGroup((1,3,6,1,4,1,9,9,866,2,2,2))
ciscoPrpMIBNotificationGroup.setObjects(*((_A,_J),(_A,_K),(_A,_L)))
if mibBuilder.loadTexts:ciscoPrpMIBNotificationGroup.setStatus(_B)
ciscoPrpMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,866,2,1,1))
ciscoPrpMIBCompliance.setObjects(*((_A,_M),(_A,_N)))
if mibBuilder.loadTexts:ciscoPrpMIBCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'PrpStatus':PrpStatus,'ciscoPrpMIB':ciscoPrpMIB,'ciscoPrpMIBNotifs':ciscoPrpMIBNotifs,_J:ciscoPrpChannelStateChange,_K:ciscoPrpLanAStateChange,_L:ciscoPrpLanBStateChange,'ciscoPrpMIBObjects':ciscoPrpMIBObjects,'ciscoPrpChannelTable':ciscoPrpChannelTable,'ciscoPrpChannelEntry':ciscoPrpChannelEntry,_I:ciscoPrpChannelIndex,_D:ciscoPrpChannelId,_E:ciscoPrpChannelName,_F:ciscoPrpChannelStatus,_G:ciscoPrpChannelLanAStatus,_H:ciscoPrpChannelLanBStatus,'ciscoPrpMIBConform':ciscoPrpMIBConform,'ciscoPrpMIBCompliances':ciscoPrpMIBCompliances,'ciscoPrpMIBCompliance':ciscoPrpMIBCompliance,'ciscoPrpMIBGroups':ciscoPrpMIBGroups,_M:ciscoPrpMIBMainObjectGroup,_N:ciscoPrpMIBNotificationGroup})