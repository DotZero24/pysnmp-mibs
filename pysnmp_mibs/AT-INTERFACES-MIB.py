_K='arIfXIndex'
_J='arInterfacePosition'
_I='arInterfaceBoardIndex'
_H='arSlotSlotIndex'
_G='arSlotBoardIndex'
_F='arBoardIndex'
_E='ifName'
_D='IF-MIB'
_C='AT-INTERFACES-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
atRouter,traps=mibBuilder.importSymbols('AT-SMI-MIB','atRouter','traps')
InterfaceIndexOrZero,ifName=mibBuilder.importSymbols(_D,'InterfaceIndexOrZero',_E)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
arInterfaces=ModuleIdentity((1,3,6,1,4,1,207,8,4,4,5))
if mibBuilder.loadTexts:arInterfaces.setRevisions(('2006-06-14 00:00',))
_IgmpTraps_ObjectIdentity=ObjectIdentity
igmpTraps=_IgmpTraps_ObjectIdentity((1,3,6,1,4,1,207,8,4,4,2,1))
if mibBuilder.loadTexts:igmpTraps.setStatus(_A)
_ArBoardMaxIndex_Type=Integer32
_ArBoardMaxIndex_Object=MibScalar
arBoardMaxIndex=_ArBoardMaxIndex_Object((1,3,6,1,4,1,207,8,4,4,5,1),_ArBoardMaxIndex_Type())
arBoardMaxIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:arBoardMaxIndex.setStatus(_A)
_ArBoardTable_Object=MibTable
arBoardTable=_ArBoardTable_Object((1,3,6,1,4,1,207,8,4,4,5,2))
if mibBuilder.loadTexts:arBoardTable.setStatus(_A)
_ArBoardEntry_Object=MibTableRow
arBoardEntry=_ArBoardEntry_Object((1,3,6,1,4,1,207,8,4,4,5,2,1))
arBoardEntry.setIndexNames((0,_C,_F))
if mibBuilder.loadTexts:arBoardEntry.setStatus(_A)
_ArBoardIndex_Type=Integer32
_ArBoardIndex_Object=MibTableColumn
arBoardIndex=_ArBoardIndex_Object((1,3,6,1,4,1,207,8,4,4,5,2,1,1),_ArBoardIndex_Type())
arBoardIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:arBoardIndex.setStatus(_A)
_ArBoardId_Type=ObjectIdentifier
_ArBoardId_Object=MibTableColumn
arBoardId=_ArBoardId_Object((1,3,6,1,4,1,207,8,4,4,5,2,1,2),_ArBoardId_Type())
arBoardId.setMaxAccess(_B)
if mibBuilder.loadTexts:arBoardId.setStatus(_A)
_ArBoardName_Type=DisplayString
_ArBoardName_Object=MibTableColumn
arBoardName=_ArBoardName_Object((1,3,6,1,4,1,207,8,4,4,5,2,1,3),_ArBoardName_Type())
arBoardName.setMaxAccess(_B)
if mibBuilder.loadTexts:arBoardName.setStatus(_A)
_ArBoardRevision_Type=DisplayString
_ArBoardRevision_Object=MibTableColumn
arBoardRevision=_ArBoardRevision_Object((1,3,6,1,4,1,207,8,4,4,5,2,1,4),_ArBoardRevision_Type())
arBoardRevision.setMaxAccess(_B)
if mibBuilder.loadTexts:arBoardRevision.setStatus(_A)
_ArBoardSerialNumber_Type=DisplayString
_ArBoardSerialNumber_Object=MibTableColumn
arBoardSerialNumber=_ArBoardSerialNumber_Object((1,3,6,1,4,1,207,8,4,4,5,2,1,5),_ArBoardSerialNumber_Type())
arBoardSerialNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:arBoardSerialNumber.setStatus(_A)
_ArBoardTotalSlots_Type=Integer32
_ArBoardTotalSlots_Object=MibTableColumn
arBoardTotalSlots=_ArBoardTotalSlots_Object((1,3,6,1,4,1,207,8,4,4,5,2,1,6),_ArBoardTotalSlots_Type())
arBoardTotalSlots.setMaxAccess(_B)
if mibBuilder.loadTexts:arBoardTotalSlots.setStatus(_A)
_ArBoardTotalPositions_Type=Integer32
_ArBoardTotalPositions_Object=MibTableColumn
arBoardTotalPositions=_ArBoardTotalPositions_Object((1,3,6,1,4,1,207,8,4,4,5,2,1,7),_ArBoardTotalPositions_Type())
arBoardTotalPositions.setMaxAccess(_B)
if mibBuilder.loadTexts:arBoardTotalPositions.setStatus(_A)
_ArSlotTable_Object=MibTable
arSlotTable=_ArSlotTable_Object((1,3,6,1,4,1,207,8,4,4,5,3))
if mibBuilder.loadTexts:arSlotTable.setStatus(_A)
_ArSlotEntry_Object=MibTableRow
arSlotEntry=_ArSlotEntry_Object((1,3,6,1,4,1,207,8,4,4,5,3,1))
arSlotEntry.setIndexNames((0,_C,_G),(0,_C,_H))
if mibBuilder.loadTexts:arSlotEntry.setStatus(_A)
_ArSlotBoardIndex_Type=Integer32
_ArSlotBoardIndex_Object=MibTableColumn
arSlotBoardIndex=_ArSlotBoardIndex_Object((1,3,6,1,4,1,207,8,4,4,5,3,1,1),_ArSlotBoardIndex_Type())
arSlotBoardIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:arSlotBoardIndex.setStatus(_A)
_ArSlotSlotIndex_Type=Integer32
_ArSlotSlotIndex_Object=MibTableColumn
arSlotSlotIndex=_ArSlotSlotIndex_Object((1,3,6,1,4,1,207,8,4,4,5,3,1,2),_ArSlotSlotIndex_Type())
arSlotSlotIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:arSlotSlotIndex.setStatus(_A)
_ArSlotHeldBoardIndex_Type=Integer32
_ArSlotHeldBoardIndex_Object=MibTableColumn
arSlotHeldBoardIndex=_ArSlotHeldBoardIndex_Object((1,3,6,1,4,1,207,8,4,4,5,3,1,3),_ArSlotHeldBoardIndex_Type())
arSlotHeldBoardIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:arSlotHeldBoardIndex.setStatus(_A)
_ArSlotDescription_Type=DisplayString
_ArSlotDescription_Object=MibTableColumn
arSlotDescription=_ArSlotDescription_Object((1,3,6,1,4,1,207,8,4,4,5,3,1,4),_ArSlotDescription_Type())
arSlotDescription.setMaxAccess(_B)
if mibBuilder.loadTexts:arSlotDescription.setStatus(_A)
_ArInterfaceTable_Object=MibTable
arInterfaceTable=_ArInterfaceTable_Object((1,3,6,1,4,1,207,8,4,4,5,4))
if mibBuilder.loadTexts:arInterfaceTable.setStatus(_A)
_ArInterfaceEntry_Object=MibTableRow
arInterfaceEntry=_ArInterfaceEntry_Object((1,3,6,1,4,1,207,8,4,4,5,4,1))
arInterfaceEntry.setIndexNames((0,_C,_I),(0,_C,_J))
if mibBuilder.loadTexts:arInterfaceEntry.setStatus(_A)
_ArInterfaceBoardIndex_Type=Integer32
_ArInterfaceBoardIndex_Object=MibTableColumn
arInterfaceBoardIndex=_ArInterfaceBoardIndex_Object((1,3,6,1,4,1,207,8,4,4,5,4,1,1),_ArInterfaceBoardIndex_Type())
arInterfaceBoardIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:arInterfaceBoardIndex.setStatus(_A)
_ArInterfacePosition_Type=Integer32
_ArInterfacePosition_Object=MibTableColumn
arInterfacePosition=_ArInterfacePosition_Object((1,3,6,1,4,1,207,8,4,4,5,4,1,2),_ArInterfacePosition_Type())
arInterfacePosition.setMaxAccess(_B)
if mibBuilder.loadTexts:arInterfacePosition.setStatus(_A)
_ArInterfaceIfIndex_Type=InterfaceIndexOrZero
_ArInterfaceIfIndex_Object=MibTableColumn
arInterfaceIfIndex=_ArInterfaceIfIndex_Object((1,3,6,1,4,1,207,8,4,4,5,4,1,3),_ArInterfaceIfIndex_Type())
arInterfaceIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:arInterfaceIfIndex.setStatus(_A)
_ArInterfaceName_Type=DisplayString
_ArInterfaceName_Object=MibTableColumn
arInterfaceName=_ArInterfaceName_Object((1,3,6,1,4,1,207,8,4,4,5,4,1,4),_ArInterfaceName_Type())
arInterfaceName.setMaxAccess(_B)
if mibBuilder.loadTexts:arInterfaceName.setStatus(_A)
_ArInterfaceFullName_Type=DisplayString
_ArInterfaceFullName_Object=MibTableColumn
arInterfaceFullName=_ArInterfaceFullName_Object((1,3,6,1,4,1,207,8,4,4,5,4,1,5),_ArInterfaceFullName_Type())
arInterfaceFullName.setMaxAccess(_B)
if mibBuilder.loadTexts:arInterfaceFullName.setStatus(_A)
_ArIfXTable_Object=MibTable
arIfXTable=_ArIfXTable_Object((1,3,6,1,4,1,207,8,4,4,5,5))
if mibBuilder.loadTexts:arIfXTable.setStatus(_A)
_ArIfXEntry_Object=MibTableRow
arIfXEntry=_ArIfXEntry_Object((1,3,6,1,4,1,207,8,4,4,5,5,1))
arIfXEntry.setIndexNames((0,_C,_K))
if mibBuilder.loadTexts:arIfXEntry.setStatus(_A)
_ArIfXIndex_Type=Integer32
_ArIfXIndex_Object=MibTableColumn
arIfXIndex=_ArIfXIndex_Object((1,3,6,1,4,1,207,8,4,4,5,5,1,1),_ArIfXIndex_Type())
arIfXIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:arIfXIndex.setStatus(_A)
_ArIfXAverageInputBitsSecond_Type=Integer32
_ArIfXAverageInputBitsSecond_Object=MibTableColumn
arIfXAverageInputBitsSecond=_ArIfXAverageInputBitsSecond_Object((1,3,6,1,4,1,207,8,4,4,5,5,1,2),_ArIfXAverageInputBitsSecond_Type())
arIfXAverageInputBitsSecond.setMaxAccess(_B)
if mibBuilder.loadTexts:arIfXAverageInputBitsSecond.setStatus(_A)
_ArIfXAverageInputPacketsSecond_Type=Integer32
_ArIfXAverageInputPacketsSecond_Object=MibTableColumn
arIfXAverageInputPacketsSecond=_ArIfXAverageInputPacketsSecond_Object((1,3,6,1,4,1,207,8,4,4,5,5,1,3),_ArIfXAverageInputPacketsSecond_Type())
arIfXAverageInputPacketsSecond.setMaxAccess(_B)
if mibBuilder.loadTexts:arIfXAverageInputPacketsSecond.setStatus(_A)
_ArIfXAverageOutputBitsSecond_Type=Integer32
_ArIfXAverageOutputBitsSecond_Object=MibTableColumn
arIfXAverageOutputBitsSecond=_ArIfXAverageOutputBitsSecond_Object((1,3,6,1,4,1,207,8,4,4,5,5,1,4),_ArIfXAverageOutputBitsSecond_Type())
arIfXAverageOutputBitsSecond.setMaxAccess(_B)
if mibBuilder.loadTexts:arIfXAverageOutputBitsSecond.setStatus(_A)
_ArIfXAverageOutputPacketsSecond_Type=Integer32
_ArIfXAverageOutputPacketsSecond_Object=MibTableColumn
arIfXAverageOutputPacketsSecond=_ArIfXAverageOutputPacketsSecond_Object((1,3,6,1,4,1,207,8,4,4,5,5,1,5),_ArIfXAverageOutputPacketsSecond_Type())
arIfXAverageOutputPacketsSecond.setMaxAccess(_B)
if mibBuilder.loadTexts:arIfXAverageOutputPacketsSecond.setStatus(_A)
igmpGeneralQueryNotReceivedEvent=NotificationType((1,3,6,1,4,1,207,8,4,4,2,1,1))
igmpGeneralQueryNotReceivedEvent.setObjects((_D,_E))
if mibBuilder.loadTexts:igmpGeneralQueryNotReceivedEvent.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'igmpTraps':igmpTraps,'igmpGeneralQueryNotReceivedEvent':igmpGeneralQueryNotReceivedEvent,'arInterfaces':arInterfaces,'arBoardMaxIndex':arBoardMaxIndex,'arBoardTable':arBoardTable,'arBoardEntry':arBoardEntry,_F:arBoardIndex,'arBoardId':arBoardId,'arBoardName':arBoardName,'arBoardRevision':arBoardRevision,'arBoardSerialNumber':arBoardSerialNumber,'arBoardTotalSlots':arBoardTotalSlots,'arBoardTotalPositions':arBoardTotalPositions,'arSlotTable':arSlotTable,'arSlotEntry':arSlotEntry,_G:arSlotBoardIndex,_H:arSlotSlotIndex,'arSlotHeldBoardIndex':arSlotHeldBoardIndex,'arSlotDescription':arSlotDescription,'arInterfaceTable':arInterfaceTable,'arInterfaceEntry':arInterfaceEntry,_I:arInterfaceBoardIndex,_J:arInterfacePosition,'arInterfaceIfIndex':arInterfaceIfIndex,'arInterfaceName':arInterfaceName,'arInterfaceFullName':arInterfaceFullName,'arIfXTable':arIfXTable,'arIfXEntry':arIfXEntry,_K:arIfXIndex,'arIfXAverageInputBitsSecond':arIfXAverageInputBitsSecond,'arIfXAverageInputPacketsSecond':arIfXAverageInputPacketsSecond,'arIfXAverageOutputBitsSecond':arIfXAverageOutputBitsSecond,'arIfXAverageOutputPacketsSecond':arIfXAverageOutputPacketsSecond})