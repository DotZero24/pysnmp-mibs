_L='cnpvTrafficMapGroup'
_K='cnpvTrafficMapLastChange'
_J='cnpvTrafficMapRowStatus'
_I='cnpvTrafficMapStorageType'
_H='cnpvTrafficMapToIfIndexList'
_G='cnpvTrafficAutoLoadbalance'
_F='cnpvTrafficMapFromIfIndex'
_E='StorageType'
_D='InterfaceIndexList'
_C='read-create'
_B='CISCO-NPORT-VIRTUALIZATION-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndexList,=mibBuilder.importSymbols('CISCO-IF-EXTENSION-MIB',_D)
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,StorageType,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus',_E,'TextualConvention','TimeStamp','TruthValue')
ciscoNportVirtualizationMIB=ModuleIdentity((1,3,6,1,4,1,9,9,660))
if mibBuilder.loadTexts:ciscoNportVirtualizationMIB.setRevisions(('2008-06-13 00:00',))
_CiscoNportVirtualizationMIBNotifs_ObjectIdentity=ObjectIdentity
ciscoNportVirtualizationMIBNotifs=_CiscoNportVirtualizationMIBNotifs_ObjectIdentity((1,3,6,1,4,1,9,9,660,0))
_CiscoNportVirtualizationMIBObjects_ObjectIdentity=ObjectIdentity
ciscoNportVirtualizationMIBObjects=_CiscoNportVirtualizationMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,660,1))
_CnpvConfiguration_ObjectIdentity=ObjectIdentity
cnpvConfiguration=_CnpvConfiguration_ObjectIdentity((1,3,6,1,4,1,9,9,660,1,1))
_CnpvGlobal_ObjectIdentity=ObjectIdentity
cnpvGlobal=_CnpvGlobal_ObjectIdentity((1,3,6,1,4,1,9,9,660,1,1,1))
_CnpvTrafficAutoLoadbalance_Type=TruthValue
_CnpvTrafficAutoLoadbalance_Object=MibScalar
cnpvTrafficAutoLoadbalance=_CnpvTrafficAutoLoadbalance_Object((1,3,6,1,4,1,9,9,660,1,1,1,1),_CnpvTrafficAutoLoadbalance_Type())
cnpvTrafficAutoLoadbalance.setMaxAccess('read-write')
if mibBuilder.loadTexts:cnpvTrafficAutoLoadbalance.setStatus(_A)
_CnpvTrafficMap_ObjectIdentity=ObjectIdentity
cnpvTrafficMap=_CnpvTrafficMap_ObjectIdentity((1,3,6,1,4,1,9,9,660,1,1,2))
_CnpvTrafficMapTable_Object=MibTable
cnpvTrafficMapTable=_CnpvTrafficMapTable_Object((1,3,6,1,4,1,9,9,660,1,1,2,1))
if mibBuilder.loadTexts:cnpvTrafficMapTable.setStatus(_A)
_CnpvTrafficMapEntry_Object=MibTableRow
cnpvTrafficMapEntry=_CnpvTrafficMapEntry_Object((1,3,6,1,4,1,9,9,660,1,1,2,1,1))
cnpvTrafficMapEntry.setIndexNames((0,_B,_F))
if mibBuilder.loadTexts:cnpvTrafficMapEntry.setStatus(_A)
_CnpvTrafficMapFromIfIndex_Type=InterfaceIndex
_CnpvTrafficMapFromIfIndex_Object=MibTableColumn
cnpvTrafficMapFromIfIndex=_CnpvTrafficMapFromIfIndex_Object((1,3,6,1,4,1,9,9,660,1,1,2,1,1,1),_CnpvTrafficMapFromIfIndex_Type())
cnpvTrafficMapFromIfIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:cnpvTrafficMapFromIfIndex.setStatus(_A)
class _CnpvTrafficMapToIfIndexList_Type(InterfaceIndexList):subtypeSpec=InterfaceIndexList.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,256))
_CnpvTrafficMapToIfIndexList_Type.__name__=_D
_CnpvTrafficMapToIfIndexList_Object=MibTableColumn
cnpvTrafficMapToIfIndexList=_CnpvTrafficMapToIfIndexList_Object((1,3,6,1,4,1,9,9,660,1,1,2,1,1,2),_CnpvTrafficMapToIfIndexList_Type())
cnpvTrafficMapToIfIndexList.setMaxAccess(_C)
if mibBuilder.loadTexts:cnpvTrafficMapToIfIndexList.setStatus(_A)
_CnpvTrafficMapLastChange_Type=TimeStamp
_CnpvTrafficMapLastChange_Object=MibTableColumn
cnpvTrafficMapLastChange=_CnpvTrafficMapLastChange_Object((1,3,6,1,4,1,9,9,660,1,1,2,1,1,3),_CnpvTrafficMapLastChange_Type())
cnpvTrafficMapLastChange.setMaxAccess('read-only')
if mibBuilder.loadTexts:cnpvTrafficMapLastChange.setStatus(_A)
class _CnpvTrafficMapStorageType_Type(StorageType):defaultValue=2
_CnpvTrafficMapStorageType_Type.__name__=_E
_CnpvTrafficMapStorageType_Object=MibTableColumn
cnpvTrafficMapStorageType=_CnpvTrafficMapStorageType_Object((1,3,6,1,4,1,9,9,660,1,1,2,1,1,4),_CnpvTrafficMapStorageType_Type())
cnpvTrafficMapStorageType.setMaxAccess(_C)
if mibBuilder.loadTexts:cnpvTrafficMapStorageType.setStatus(_A)
_CnpvTrafficMapRowStatus_Type=RowStatus
_CnpvTrafficMapRowStatus_Object=MibTableColumn
cnpvTrafficMapRowStatus=_CnpvTrafficMapRowStatus_Object((1,3,6,1,4,1,9,9,660,1,1,2,1,1,5),_CnpvTrafficMapRowStatus_Type())
cnpvTrafficMapRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cnpvTrafficMapRowStatus.setStatus(_A)
_CiscoNportVirtualizationMIBConform_ObjectIdentity=ObjectIdentity
ciscoNportVirtualizationMIBConform=_CiscoNportVirtualizationMIBConform_ObjectIdentity((1,3,6,1,4,1,9,9,660,2))
_CiscoNportVirtualizationMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoNportVirtualizationMIBCompliances=_CiscoNportVirtualizationMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,660,2,1))
_CiscoNportVirtualizationMIBGroups_ObjectIdentity=ObjectIdentity
ciscoNportVirtualizationMIBGroups=_CiscoNportVirtualizationMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,660,2,2))
cnpvTrafficMapGroup=ObjectGroup((1,3,6,1,4,1,9,9,660,2,2,1))
cnpvTrafficMapGroup.setObjects(*((_B,_G),(_B,_H),(_B,_I),(_B,_J),(_B,_K)))
if mibBuilder.loadTexts:cnpvTrafficMapGroup.setStatus(_A)
ciscoNportVirtualizationMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,660,2,1,1))
ciscoNportVirtualizationMIBCompliance.setObjects((_B,_L))
if mibBuilder.loadTexts:ciscoNportVirtualizationMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ciscoNportVirtualizationMIB':ciscoNportVirtualizationMIB,'ciscoNportVirtualizationMIBNotifs':ciscoNportVirtualizationMIBNotifs,'ciscoNportVirtualizationMIBObjects':ciscoNportVirtualizationMIBObjects,'cnpvConfiguration':cnpvConfiguration,'cnpvGlobal':cnpvGlobal,_G:cnpvTrafficAutoLoadbalance,'cnpvTrafficMap':cnpvTrafficMap,'cnpvTrafficMapTable':cnpvTrafficMapTable,'cnpvTrafficMapEntry':cnpvTrafficMapEntry,_F:cnpvTrafficMapFromIfIndex,_H:cnpvTrafficMapToIfIndexList,_K:cnpvTrafficMapLastChange,_I:cnpvTrafficMapStorageType,_J:cnpvTrafficMapRowStatus,'ciscoNportVirtualizationMIBConform':ciscoNportVirtualizationMIBConform,'ciscoNportVirtualizationMIBCompliances':ciscoNportVirtualizationMIBCompliances,'ciscoNportVirtualizationMIBCompliance':ciscoNportVirtualizationMIBCompliance,'ciscoNportVirtualizationMIBGroups':ciscoNportVirtualizationMIBGroups,_L:cnpvTrafficMapGroup})