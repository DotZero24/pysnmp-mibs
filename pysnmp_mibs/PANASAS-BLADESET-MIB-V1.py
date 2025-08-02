_F='panBSetBladeIndex'
_E='panBSetName'
_D='obsolete'
_C='PANASAS-BLADESET-MIB-V1'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
panFs,=mibBuilder.importSymbols('PANASAS-PANFS-MIB-V1','panFs')
PanSerialNumber,=mibBuilder.importSymbols('PANASAS-TC-MIB','PanSerialNumber')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
panBSet=ModuleIdentity((1,3,6,1,4,1,10159,1,3,3))
if mibBuilder.loadTexts:panBSet.setRevisions(('2011-04-07 00:00',))
_PanBSetTable_Object=MibTable
panBSetTable=_PanBSetTable_Object((1,3,6,1,4,1,10159,1,3,3,1))
if mibBuilder.loadTexts:panBSetTable.setStatus(_A)
_PanBSetEntry_Object=MibTableRow
panBSetEntry=_PanBSetEntry_Object((1,3,6,1,4,1,10159,1,3,3,1,1))
panBSetEntry.setIndexNames((0,_C,_E))
if mibBuilder.loadTexts:panBSetEntry.setStatus(_A)
_PanBSetName_Type=DisplayString
_PanBSetName_Object=MibTableColumn
panBSetName=_PanBSetName_Object((1,3,6,1,4,1,10159,1,3,3,1,1,1),_PanBSetName_Type())
panBSetName.setMaxAccess(_B)
if mibBuilder.loadTexts:panBSetName.setStatus(_A)
_PanBSetNumBlades_Type=DisplayString
_PanBSetNumBlades_Object=MibTableColumn
panBSetNumBlades=_PanBSetNumBlades_Object((1,3,6,1,4,1,10159,1,3,3,1,1,2),_PanBSetNumBlades_Type())
panBSetNumBlades.setMaxAccess(_B)
if mibBuilder.loadTexts:panBSetNumBlades.setStatus(_A)
_PanBSetAvailSpares_Type=DisplayString
_PanBSetAvailSpares_Object=MibTableColumn
panBSetAvailSpares=_PanBSetAvailSpares_Object((1,3,6,1,4,1,10159,1,3,3,1,1,3),_PanBSetAvailSpares_Type())
panBSetAvailSpares.setMaxAccess(_B)
if mibBuilder.loadTexts:panBSetAvailSpares.setStatus(_A)
_PanBSetRequestedSpares_Type=DisplayString
_PanBSetRequestedSpares_Object=MibTableColumn
panBSetRequestedSpares=_PanBSetRequestedSpares_Object((1,3,6,1,4,1,10159,1,3,3,1,1,4),_PanBSetRequestedSpares_Type())
panBSetRequestedSpares.setMaxAccess(_B)
if mibBuilder.loadTexts:panBSetRequestedSpares.setStatus(_A)
_PanBSetTotalCapacity_Type=Unsigned32
_PanBSetTotalCapacity_Object=MibTableColumn
panBSetTotalCapacity=_PanBSetTotalCapacity_Object((1,3,6,1,4,1,10159,1,3,3,1,1,5),_PanBSetTotalCapacity_Type())
panBSetTotalCapacity.setMaxAccess(_B)
if mibBuilder.loadTexts:panBSetTotalCapacity.setStatus(_A)
_PanBSetReservedCapacity_Type=Unsigned32
_PanBSetReservedCapacity_Object=MibTableColumn
panBSetReservedCapacity=_PanBSetReservedCapacity_Object((1,3,6,1,4,1,10159,1,3,3,1,1,6),_PanBSetReservedCapacity_Type())
panBSetReservedCapacity.setMaxAccess(_B)
if mibBuilder.loadTexts:panBSetReservedCapacity.setStatus(_A)
_PanBSetUsedCapacity_Type=Unsigned32
_PanBSetUsedCapacity_Object=MibTableColumn
panBSetUsedCapacity=_PanBSetUsedCapacity_Object((1,3,6,1,4,1,10159,1,3,3,1,1,7),_PanBSetUsedCapacity_Type())
panBSetUsedCapacity.setMaxAccess(_B)
if mibBuilder.loadTexts:panBSetUsedCapacity.setStatus(_A)
_PanBSetAvailableCapacity_Type=Unsigned32
_PanBSetAvailableCapacity_Object=MibTableColumn
panBSetAvailableCapacity=_PanBSetAvailableCapacity_Object((1,3,6,1,4,1,10159,1,3,3,1,1,8),_PanBSetAvailableCapacity_Type())
panBSetAvailableCapacity.setMaxAccess(_B)
if mibBuilder.loadTexts:panBSetAvailableCapacity.setStatus(_A)
_PanBSetInfo_Type=DisplayString
_PanBSetInfo_Object=MibTableColumn
panBSetInfo=_PanBSetInfo_Object((1,3,6,1,4,1,10159,1,3,3,1,1,9),_PanBSetInfo_Type())
panBSetInfo.setMaxAccess(_B)
if mibBuilder.loadTexts:panBSetInfo.setStatus(_A)
_PanBSetBladesTable_Object=MibTable
panBSetBladesTable=_PanBSetBladesTable_Object((1,3,6,1,4,1,10159,1,3,3,2))
if mibBuilder.loadTexts:panBSetBladesTable.setStatus(_D)
_PanBSetBladesEntry_Object=MibTableRow
panBSetBladesEntry=_PanBSetBladesEntry_Object((1,3,6,1,4,1,10159,1,3,3,2,1))
panBSetBladesEntry.setIndexNames((0,_C,_E),(0,_C,_F))
if mibBuilder.loadTexts:panBSetBladesEntry.setStatus(_D)
_PanBSetBladeIndex_Type=Unsigned32
_PanBSetBladeIndex_Object=MibTableColumn
panBSetBladeIndex=_PanBSetBladeIndex_Object((1,3,6,1,4,1,10159,1,3,3,2,1,1),_PanBSetBladeIndex_Type())
panBSetBladeIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:panBSetBladeIndex.setStatus(_D)
_PanBSetBladeHwSn_Type=PanSerialNumber
_PanBSetBladeHwSn_Object=MibTableColumn
panBSetBladeHwSn=_PanBSetBladeHwSn_Object((1,3,6,1,4,1,10159,1,3,3,2,1,2),_PanBSetBladeHwSn_Type())
panBSetBladeHwSn.setMaxAccess(_B)
if mibBuilder.loadTexts:panBSetBladeHwSn.setStatus(_D)
mibBuilder.exportSymbols(_C,**{'panBSet':panBSet,'panBSetTable':panBSetTable,'panBSetEntry':panBSetEntry,_E:panBSetName,'panBSetNumBlades':panBSetNumBlades,'panBSetAvailSpares':panBSetAvailSpares,'panBSetRequestedSpares':panBSetRequestedSpares,'panBSetTotalCapacity':panBSetTotalCapacity,'panBSetReservedCapacity':panBSetReservedCapacity,'panBSetUsedCapacity':panBSetUsedCapacity,'panBSetAvailableCapacity':panBSetAvailableCapacity,'panBSetInfo':panBSetInfo,'panBSetBladesTable':panBSetBladesTable,'panBSetBladesEntry':panBSetBladesEntry,_F:panBSetBladeIndex,'panBSetBladeHwSn':panBSetBladeHwSn})