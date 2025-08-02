_M='nbsObaAlsIfIndex'
_L='unknown'
_K='unconfigured'
_J='nbsObaDefineOrdinalIndex'
_I='nbsObaDefineLinePort'
_H='nbsObaInfoLineIfIndex'
_G='RowStatus'
_F='DisplayString'
_E='NBS-OBA-MIB'
_D='Integer32'
_C='read-create'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
NbsTcMHz,nbs=mibBuilder.importSymbols('NBS-MIB','NbsTcMHz','nbs')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_F,'PhysAddress',_G,'TextualConvention')
nbsObaMib=ModuleIdentity((1,3,6,1,4,1,629,240))
_NbsObaInfoGrp_ObjectIdentity=ObjectIdentity
nbsObaInfoGrp=_NbsObaInfoGrp_ObjectIdentity((1,3,6,1,4,1,629,240,1))
if mibBuilder.loadTexts:nbsObaInfoGrp.setStatus(_A)
_NbsObaInfoTable_Object=MibTable
nbsObaInfoTable=_NbsObaInfoTable_Object((1,3,6,1,4,1,629,240,1,1))
if mibBuilder.loadTexts:nbsObaInfoTable.setStatus(_A)
_NbsObaInfoEntry_Object=MibTableRow
nbsObaInfoEntry=_NbsObaInfoEntry_Object((1,3,6,1,4,1,629,240,1,1,1))
nbsObaInfoEntry.setIndexNames((0,_E,_H))
if mibBuilder.loadTexts:nbsObaInfoEntry.setStatus(_A)
_NbsObaInfoLineIfIndex_Type=InterfaceIndex
_NbsObaInfoLineIfIndex_Object=MibTableColumn
nbsObaInfoLineIfIndex=_NbsObaInfoLineIfIndex_Object((1,3,6,1,4,1,629,240,1,1,1,1),_NbsObaInfoLineIfIndex_Type())
nbsObaInfoLineIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsObaInfoLineIfIndex.setStatus(_A)
_NbsObaInfoAvails_Type=DisplayString
_NbsObaInfoAvails_Object=MibTableColumn
nbsObaInfoAvails=_NbsObaInfoAvails_Object((1,3,6,1,4,1,629,240,1,1,1,2),_NbsObaInfoAvails_Type())
nbsObaInfoAvails.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsObaInfoAvails.setStatus(_A)
_NbsObaInfoUnitSize_Type=NbsTcMHz
_NbsObaInfoUnitSize_Object=MibTableColumn
nbsObaInfoUnitSize=_NbsObaInfoUnitSize_Object((1,3,6,1,4,1,629,240,1,1,1,3),_NbsObaInfoUnitSize_Type())
nbsObaInfoUnitSize.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsObaInfoUnitSize.setStatus(_A)
_NbsObaInfoMaxUnits_Type=Integer32
_NbsObaInfoMaxUnits_Object=MibTableColumn
nbsObaInfoMaxUnits=_NbsObaInfoMaxUnits_Object((1,3,6,1,4,1,629,240,1,1,1,4),_NbsObaInfoMaxUnits_Type())
nbsObaInfoMaxUnits.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsObaInfoMaxUnits.setStatus(_A)
_NbsObaInfoMaxUnitsPerClientPort_Type=Integer32
_NbsObaInfoMaxUnitsPerClientPort_Object=MibTableColumn
nbsObaInfoMaxUnitsPerClientPort=_NbsObaInfoMaxUnitsPerClientPort_Object((1,3,6,1,4,1,629,240,1,1,1,5),_NbsObaInfoMaxUnitsPerClientPort_Type())
nbsObaInfoMaxUnitsPerClientPort.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsObaInfoMaxUnitsPerClientPort.setStatus(_A)
_NbsObaDefineGrp_ObjectIdentity=ObjectIdentity
nbsObaDefineGrp=_NbsObaDefineGrp_ObjectIdentity((1,3,6,1,4,1,629,240,2))
if mibBuilder.loadTexts:nbsObaDefineGrp.setStatus(_A)
_NbsObaDefineTableSize_Type=Integer32
_NbsObaDefineTableSize_Object=MibScalar
nbsObaDefineTableSize=_NbsObaDefineTableSize_Object((1,3,6,1,4,1,629,240,2,1),_NbsObaDefineTableSize_Type())
nbsObaDefineTableSize.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsObaDefineTableSize.setStatus(_A)
_NbsObaDefineTable_Object=MibTable
nbsObaDefineTable=_NbsObaDefineTable_Object((1,3,6,1,4,1,629,240,2,2))
if mibBuilder.loadTexts:nbsObaDefineTable.setStatus(_A)
_NbsObaDefineEntry_Object=MibTableRow
nbsObaDefineEntry=_NbsObaDefineEntry_Object((1,3,6,1,4,1,629,240,2,2,1))
nbsObaDefineEntry.setIndexNames((0,_E,_I),(0,_E,_J))
if mibBuilder.loadTexts:nbsObaDefineEntry.setStatus(_A)
_NbsObaDefineLinePort_Type=InterfaceIndex
_NbsObaDefineLinePort_Object=MibTableColumn
nbsObaDefineLinePort=_NbsObaDefineLinePort_Object((1,3,6,1,4,1,629,240,2,2,1,1),_NbsObaDefineLinePort_Type())
nbsObaDefineLinePort.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsObaDefineLinePort.setStatus(_A)
_NbsObaDefineOrdinalIndex_Type=Integer32
_NbsObaDefineOrdinalIndex_Object=MibTableColumn
nbsObaDefineOrdinalIndex=_NbsObaDefineOrdinalIndex_Object((1,3,6,1,4,1,629,240,2,2,1,2),_NbsObaDefineOrdinalIndex_Type())
nbsObaDefineOrdinalIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsObaDefineOrdinalIndex.setStatus(_A)
class _NbsObaDefineLabel_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_NbsObaDefineLabel_Type.__name__=_F
_NbsObaDefineLabel_Object=MibTableColumn
nbsObaDefineLabel=_NbsObaDefineLabel_Object((1,3,6,1,4,1,629,240,2,2,1,10),_NbsObaDefineLabel_Type())
nbsObaDefineLabel.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsObaDefineLabel.setStatus(_A)
class _NbsObaDefineOduType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),('odu0',2)))
_NbsObaDefineOduType_Type.__name__=_D
_NbsObaDefineOduType_Object=MibTableColumn
nbsObaDefineOduType=_NbsObaDefineOduType_Object((1,3,6,1,4,1,629,240,2,2,1,11),_NbsObaDefineOduType_Type())
nbsObaDefineOduType.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsObaDefineOduType.setStatus(_A)
class _NbsObaDefineOduList_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_NbsObaDefineOduList_Type.__name__=_F
_NbsObaDefineOduList_Object=MibTableColumn
nbsObaDefineOduList=_NbsObaDefineOduList_Object((1,3,6,1,4,1,629,240,2,2,1,12),_NbsObaDefineOduList_Type())
nbsObaDefineOduList.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsObaDefineOduList.setStatus(_A)
_NbsObaDefineOduCount_Type=Integer32
_NbsObaDefineOduCount_Object=MibTableColumn
nbsObaDefineOduCount=_NbsObaDefineOduCount_Object((1,3,6,1,4,1,629,240,2,2,1,13),_NbsObaDefineOduCount_Type())
nbsObaDefineOduCount.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsObaDefineOduCount.setStatus(_A)
class _NbsObaDefineMapType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_K,1),('express',2),('standAlone',3),('primary',4),('secondary',5)))
_NbsObaDefineMapType_Type.__name__=_D
_NbsObaDefineMapType_Object=MibTableColumn
nbsObaDefineMapType=_NbsObaDefineMapType_Object((1,3,6,1,4,1,629,240,2,2,1,20),_NbsObaDefineMapType_Type())
nbsObaDefineMapType.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsObaDefineMapType.setStatus(_A)
_NbsObaDefineClientPort_Type=InterfaceIndex
_NbsObaDefineClientPort_Object=MibTableColumn
nbsObaDefineClientPort=_NbsObaDefineClientPort_Object((1,3,6,1,4,1,629,240,2,2,1,21),_NbsObaDefineClientPort_Type())
nbsObaDefineClientPort.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsObaDefineClientPort.setStatus(_A)
class _NbsObaDefineCoupledWith_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_NbsObaDefineCoupledWith_Type.__name__=_F
_NbsObaDefineCoupledWith_Object=MibTableColumn
nbsObaDefineCoupledWith=_NbsObaDefineCoupledWith_Object((1,3,6,1,4,1,629,240,2,2,1,22),_NbsObaDefineCoupledWith_Type())
nbsObaDefineCoupledWith.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsObaDefineCoupledWith.setStatus(_A)
class _NbsObaDefinePresentState_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_L,1),('down',2),('active',3),('standby',4)))
_NbsObaDefinePresentState_Type.__name__=_D
_NbsObaDefinePresentState_Object=MibTableColumn
nbsObaDefinePresentState=_NbsObaDefinePresentState_Object((1,3,6,1,4,1,629,240,2,2,1,29),_NbsObaDefinePresentState_Type())
nbsObaDefinePresentState.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsObaDefinePresentState.setStatus(_A)
class _NbsObaDefineAllocationInfo_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_L,1),('unitsExceedProtocolSpec',2),('additionalUnitsNeededForProtocol',3),('unitsMatchProtocolSpec',4),('unitsExceedExpress',5),('additionalUnitsNeededForExpress',6),('unitsMatchExpress',7)))
_NbsObaDefineAllocationInfo_Type.__name__=_D
_NbsObaDefineAllocationInfo_Object=MibTableColumn
nbsObaDefineAllocationInfo=_NbsObaDefineAllocationInfo_Object((1,3,6,1,4,1,629,240,2,2,1,30),_NbsObaDefineAllocationInfo_Type())
nbsObaDefineAllocationInfo.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsObaDefineAllocationInfo.setStatus(_A)
class _NbsObaDefineRowStatus_Type(RowStatus):defaultValue=2
_NbsObaDefineRowStatus_Type.__name__=_G
_NbsObaDefineRowStatus_Object=MibTableColumn
nbsObaDefineRowStatus=_NbsObaDefineRowStatus_Object((1,3,6,1,4,1,629,240,2,2,1,99),_NbsObaDefineRowStatus_Type())
nbsObaDefineRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsObaDefineRowStatus.setStatus(_A)
_NbsObaAlsGrp_ObjectIdentity=ObjectIdentity
nbsObaAlsGrp=_NbsObaAlsGrp_ObjectIdentity((1,3,6,1,4,1,629,240,3))
if mibBuilder.loadTexts:nbsObaAlsGrp.setStatus(_A)
_NbsObaAlsTable_Object=MibTable
nbsObaAlsTable=_NbsObaAlsTable_Object((1,3,6,1,4,1,629,240,3,1))
if mibBuilder.loadTexts:nbsObaAlsTable.setStatus(_A)
_NbsObaAlsEntry_Object=MibTableRow
nbsObaAlsEntry=_NbsObaAlsEntry_Object((1,3,6,1,4,1,629,240,3,1,1))
nbsObaAlsEntry.setIndexNames((0,_E,_M))
if mibBuilder.loadTexts:nbsObaAlsEntry.setStatus(_A)
_NbsObaAlsIfIndex_Type=InterfaceIndex
_NbsObaAlsIfIndex_Object=MibTableColumn
nbsObaAlsIfIndex=_NbsObaAlsIfIndex_Object((1,3,6,1,4,1,629,240,3,1,1,1),_NbsObaAlsIfIndex_Type())
nbsObaAlsIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsObaAlsIfIndex.setStatus(_A)
class _NbsObaAlsState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('notSupported',1),('enable',2),('disable',3)))
_NbsObaAlsState_Type.__name__=_D
_NbsObaAlsState_Object=MibTableColumn
nbsObaAlsState=_NbsObaAlsState_Object((1,3,6,1,4,1,629,240,3,1,1,10),_NbsObaAlsState_Type())
nbsObaAlsState.setMaxAccess('read-write')
if mibBuilder.loadTexts:nbsObaAlsState.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'nbsObaMib':nbsObaMib,'nbsObaInfoGrp':nbsObaInfoGrp,'nbsObaInfoTable':nbsObaInfoTable,'nbsObaInfoEntry':nbsObaInfoEntry,_H:nbsObaInfoLineIfIndex,'nbsObaInfoAvails':nbsObaInfoAvails,'nbsObaInfoUnitSize':nbsObaInfoUnitSize,'nbsObaInfoMaxUnits':nbsObaInfoMaxUnits,'nbsObaInfoMaxUnitsPerClientPort':nbsObaInfoMaxUnitsPerClientPort,'nbsObaDefineGrp':nbsObaDefineGrp,'nbsObaDefineTableSize':nbsObaDefineTableSize,'nbsObaDefineTable':nbsObaDefineTable,'nbsObaDefineEntry':nbsObaDefineEntry,_I:nbsObaDefineLinePort,_J:nbsObaDefineOrdinalIndex,'nbsObaDefineLabel':nbsObaDefineLabel,'nbsObaDefineOduType':nbsObaDefineOduType,'nbsObaDefineOduList':nbsObaDefineOduList,'nbsObaDefineOduCount':nbsObaDefineOduCount,'nbsObaDefineMapType':nbsObaDefineMapType,'nbsObaDefineClientPort':nbsObaDefineClientPort,'nbsObaDefineCoupledWith':nbsObaDefineCoupledWith,'nbsObaDefinePresentState':nbsObaDefinePresentState,'nbsObaDefineAllocationInfo':nbsObaDefineAllocationInfo,'nbsObaDefineRowStatus':nbsObaDefineRowStatus,'nbsObaAlsGrp':nbsObaAlsGrp,'nbsObaAlsTable':nbsObaAlsTable,'nbsObaAlsEntry':nbsObaAlsEntry,_M:nbsObaAlsIfIndex,'nbsObaAlsState':nbsObaAlsState})