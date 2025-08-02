_J='interfaceAggDownMinLink'
_I='interfaceErrDisReason'
_H='Integer32'
_G='OCNOS-INTERFACE-MIB'
_F='vrVrId'
_E='OCNOS-VR-MIB'
_D='ifIndex'
_C='IF-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,ifName=mibBuilder.importSymbols(_C,_D,'ifName')
Ipv6Address,=mibBuilder.importSymbols('IPV6-TC','Ipv6Address')
ipi,=mibBuilder.importSymbols('OCNOS-IPI-MODULE-MIB','ipi')
vrVrId,=mibBuilder.importSymbols(_E,_F)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
snmpTraps,=mibBuilder.importSymbols('SNMPv2-MIB','snmpTraps')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_H,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DateAndTime,DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','RowStatus','TextualConvention')
interface=ModuleIdentity((1,3,6,1,4,1,36673,4))
if mibBuilder.loadTexts:interface.setRevisions(('2018-06-21 00:00',))
_InterfaceNotificationsPrefix_ObjectIdentity=ObjectIdentity
interfaceNotificationsPrefix=_InterfaceNotificationsPrefix_ObjectIdentity((1,3,6,1,4,1,36673,4,0))
_InterfaceIfIndexListTable_Object=MibTable
interfaceIfIndexListTable=_InterfaceIfIndexListTable_Object((1,3,6,1,4,1,36673,4,1))
if mibBuilder.loadTexts:interfaceIfIndexListTable.setStatus(_A)
_InterfaceIfIndexListEntry_Object=MibTableRow
interfaceIfIndexListEntry=_InterfaceIfIndexListEntry_Object((1,3,6,1,4,1,36673,4,1,1))
interfaceIfIndexListEntry.setIndexNames((0,_E,_F),(0,_C,_D))
if mibBuilder.loadTexts:interfaceIfIndexListEntry.setStatus(_A)
_InterfaceIfName1_Type=OctetString
_InterfaceIfName1_Object=MibTableColumn
interfaceIfName1=_InterfaceIfName1_Object((1,3,6,1,4,1,36673,4,1,1,1),_InterfaceIfName1_Type())
interfaceIfName1.setMaxAccess(_B)
if mibBuilder.loadTexts:interfaceIfName1.setStatus(_A)
class _InterfaceErrDisReason_Type(Bits):namedValues=NamedValues(*(('lagmismatch',0),('stpbpduguard',1),('linkflap',2)))
_InterfaceErrDisReason_Type.__name__='Bits'
_InterfaceErrDisReason_Object=MibTableColumn
interfaceErrDisReason=_InterfaceErrDisReason_Object((1,3,6,1,4,1,36673,4,1,1,2),_InterfaceErrDisReason_Type())
interfaceErrDisReason.setMaxAccess(_B)
if mibBuilder.loadTexts:interfaceErrDisReason.setStatus(_A)
class _InterfaceAggDownMinLink_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('false',0),('true',1)))
_InterfaceAggDownMinLink_Type.__name__=_H
_InterfaceAggDownMinLink_Object=MibTableColumn
interfaceAggDownMinLink=_InterfaceAggDownMinLink_Object((1,3,6,1,4,1,36673,4,1,1,3),_InterfaceAggDownMinLink_Type())
interfaceAggDownMinLink.setMaxAccess(_B)
if mibBuilder.loadTexts:interfaceAggDownMinLink.setStatus(_A)
_InterfaceArpDiscardPackets_Type=Counter64
_InterfaceArpDiscardPackets_Object=MibTableColumn
interfaceArpDiscardPackets=_InterfaceArpDiscardPackets_Object((1,3,6,1,4,1,36673,4,1,1,4),_InterfaceArpDiscardPackets_Type())
interfaceArpDiscardPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:interfaceArpDiscardPackets.setStatus(_A)
_InterfaceTxArpDiscardPackets_Type=Counter64
_InterfaceTxArpDiscardPackets_Object=MibTableColumn
interfaceTxArpDiscardPackets=_InterfaceTxArpDiscardPackets_Object((1,3,6,1,4,1,36673,4,1,1,5),_InterfaceTxArpDiscardPackets_Type())
interfaceTxArpDiscardPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:interfaceTxArpDiscardPackets.setStatus(_A)
_InterfaceRxArpRequestPackets_Type=Counter64
_InterfaceRxArpRequestPackets_Object=MibTableColumn
interfaceRxArpRequestPackets=_InterfaceRxArpRequestPackets_Object((1,3,6,1,4,1,36673,4,1,1,6),_InterfaceRxArpRequestPackets_Type())
interfaceRxArpRequestPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:interfaceRxArpRequestPackets.setStatus(_A)
_InterfaceRxArpReplyPackets_Type=Counter64
_InterfaceRxArpReplyPackets_Object=MibTableColumn
interfaceRxArpReplyPackets=_InterfaceRxArpReplyPackets_Object((1,3,6,1,4,1,36673,4,1,1,7),_InterfaceRxArpReplyPackets_Type())
interfaceRxArpReplyPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:interfaceRxArpReplyPackets.setStatus(_A)
_InterfaceTxArpRequestPackets_Type=Counter64
_InterfaceTxArpRequestPackets_Object=MibTableColumn
interfaceTxArpRequestPackets=_InterfaceTxArpRequestPackets_Object((1,3,6,1,4,1,36673,4,1,1,8),_InterfaceTxArpRequestPackets_Type())
interfaceTxArpRequestPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:interfaceTxArpRequestPackets.setStatus(_A)
_InterfaceTxArpReplyPackets_Type=Counter64
_InterfaceTxArpReplyPackets_Object=MibTableColumn
interfaceTxArpReplyPackets=_InterfaceTxArpReplyPackets_Object((1,3,6,1,4,1,36673,4,1,1,9),_InterfaceTxArpReplyPackets_Type())
interfaceTxArpReplyPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:interfaceTxArpReplyPackets.setStatus(_A)
_InterfaceNdDiscardPackets_Type=Counter64
_InterfaceNdDiscardPackets_Object=MibTableColumn
interfaceNdDiscardPackets=_InterfaceNdDiscardPackets_Object((1,3,6,1,4,1,36673,4,1,1,10),_InterfaceNdDiscardPackets_Type())
interfaceNdDiscardPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:interfaceNdDiscardPackets.setStatus(_A)
_InterfaceTxNdDiscardPackets_Type=Counter64
_InterfaceTxNdDiscardPackets_Object=MibTableColumn
interfaceTxNdDiscardPackets=_InterfaceTxNdDiscardPackets_Object((1,3,6,1,4,1,36673,4,1,1,11),_InterfaceTxNdDiscardPackets_Type())
interfaceTxNdDiscardPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:interfaceTxNdDiscardPackets.setStatus(_A)
_InterfaceRxNDRequestPackets_Type=Counter64
_InterfaceRxNDRequestPackets_Object=MibTableColumn
interfaceRxNDRequestPackets=_InterfaceRxNDRequestPackets_Object((1,3,6,1,4,1,36673,4,1,1,12),_InterfaceRxNDRequestPackets_Type())
interfaceRxNDRequestPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:interfaceRxNDRequestPackets.setStatus(_A)
_InterfaceRxNDReplyPackets_Type=Counter64
_InterfaceRxNDReplyPackets_Object=MibTableColumn
interfaceRxNDReplyPackets=_InterfaceRxNDReplyPackets_Object((1,3,6,1,4,1,36673,4,1,1,13),_InterfaceRxNDReplyPackets_Type())
interfaceRxNDReplyPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:interfaceRxNDReplyPackets.setStatus(_A)
_InterfaceTxNDRequestPackets_Type=Counter64
_InterfaceTxNDRequestPackets_Object=MibTableColumn
interfaceTxNDRequestPackets=_InterfaceTxNDRequestPackets_Object((1,3,6,1,4,1,36673,4,1,1,14),_InterfaceTxNDRequestPackets_Type())
interfaceTxNDRequestPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:interfaceTxNDRequestPackets.setStatus(_A)
_InterfaceTxNDReplyPackets_Type=Counter64
_InterfaceTxNDReplyPackets_Object=MibTableColumn
interfaceTxNDReplyPackets=_InterfaceTxNDReplyPackets_Object((1,3,6,1,4,1,36673,4,1,1,15),_InterfaceTxNDReplyPackets_Type())
interfaceTxNDReplyPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:interfaceTxNDReplyPackets.setStatus(_A)
interfaceErrdisNotif=NotificationType((1,3,6,1,4,1,36673,4,0,1))
interfaceErrdisNotif.setObjects(*((_C,_D),(_E,_F),(_G,_I)))
if mibBuilder.loadTexts:interfaceErrdisNotif.setStatus(_A)
aggMinLink=NotificationType((1,3,6,1,4,1,36673,4,0,2))
aggMinLink.setObjects(*((_C,_D),(_E,_F),(_G,_J)))
if mibBuilder.loadTexts:aggMinLink.setStatus(_A)
mibBuilder.exportSymbols(_G,**{'interface':interface,'interfaceNotificationsPrefix':interfaceNotificationsPrefix,'interfaceErrdisNotif':interfaceErrdisNotif,'aggMinLink':aggMinLink,'interfaceIfIndexListTable':interfaceIfIndexListTable,'interfaceIfIndexListEntry':interfaceIfIndexListEntry,'interfaceIfName1':interfaceIfName1,_I:interfaceErrDisReason,_J:interfaceAggDownMinLink,'interfaceArpDiscardPackets':interfaceArpDiscardPackets,'interfaceTxArpDiscardPackets':interfaceTxArpDiscardPackets,'interfaceRxArpRequestPackets':interfaceRxArpRequestPackets,'interfaceRxArpReplyPackets':interfaceRxArpReplyPackets,'interfaceTxArpRequestPackets':interfaceTxArpRequestPackets,'interfaceTxArpReplyPackets':interfaceTxArpReplyPackets,'interfaceNdDiscardPackets':interfaceNdDiscardPackets,'interfaceTxNdDiscardPackets':interfaceTxNdDiscardPackets,'interfaceRxNDRequestPackets':interfaceRxNDRequestPackets,'interfaceRxNDReplyPackets':interfaceRxNDReplyPackets,'interfaceTxNDRequestPackets':interfaceTxNDRequestPackets,'interfaceTxNDReplyPackets':interfaceTxNDReplyPackets})