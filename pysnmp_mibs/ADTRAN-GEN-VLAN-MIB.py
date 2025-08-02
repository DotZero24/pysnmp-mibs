_G='adGenVlanSTag'
_F='ADTRAN-GEN-VLAN-MIB'
_E='Integer32'
_D='adGenSlotInfoIndex'
_C='ADTRAN-GENSLOT-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
adGenSlotInfoIndex,=mibBuilder.importSymbols(_C,_D)
adGenVlan,adGenVlanID=mibBuilder.importSymbols('ADTRAN-SHARED-CND-SYSTEM-MIB','adGenVlan','adGenVlanID')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
adGenVlanModuleIdentity=ModuleIdentity((1,3,6,1,4,1,664,6,10000,70,39,1))
if mibBuilder.loadTexts:adGenVlanModuleIdentity.setRevisions(('2011-03-07 00:00',))
_AdGenVlanSlotTable_Object=MibTable
adGenVlanSlotTable=_AdGenVlanSlotTable_Object((1,3,6,1,4,1,664,5,70,39,1))
if mibBuilder.loadTexts:adGenVlanSlotTable.setStatus(_A)
_AdGenVlanSlotEntry_Object=MibTableRow
adGenVlanSlotEntry=_AdGenVlanSlotEntry_Object((1,3,6,1,4,1,664,5,70,39,1,1))
adGenVlanSlotEntry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:adGenVlanSlotEntry.setStatus(_A)
_AdGenVlanCount_Type=Integer32
_AdGenVlanCount_Object=MibTableColumn
adGenVlanCount=_AdGenVlanCount_Object((1,3,6,1,4,1,664,5,70,39,1,1,1),_AdGenVlanCount_Type())
adGenVlanCount.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenVlanCount.setStatus(_A)
_AdGenVlanInterfaceList_Type=DisplayString
_AdGenVlanInterfaceList_Object=MibTableColumn
adGenVlanInterfaceList=_AdGenVlanInterfaceList_Object((1,3,6,1,4,1,664,5,70,39,1,1,2),_AdGenVlanInterfaceList_Type())
adGenVlanInterfaceList.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenVlanInterfaceList.setStatus(_A)
_AdGenVlanDisplayTable_Object=MibTable
adGenVlanDisplayTable=_AdGenVlanDisplayTable_Object((1,3,6,1,4,1,664,5,70,39,2))
if mibBuilder.loadTexts:adGenVlanDisplayTable.setStatus(_A)
_AdGenVlanDisplayEntry_Object=MibTableRow
adGenVlanDisplayEntry=_AdGenVlanDisplayEntry_Object((1,3,6,1,4,1,664,5,70,39,2,1))
adGenVlanDisplayEntry.setIndexNames((0,_C,_D),(0,_F,_G))
if mibBuilder.loadTexts:adGenVlanDisplayEntry.setStatus(_A)
class _AdGenVlanSTag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_AdGenVlanSTag_Type.__name__=_E
_AdGenVlanSTag_Object=MibTableColumn
adGenVlanSTag=_AdGenVlanSTag_Object((1,3,6,1,4,1,664,5,70,39,2,1,1),_AdGenVlanSTag_Type())
adGenVlanSTag.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:adGenVlanSTag.setStatus(_A)
_AdGenVlanName_Type=DisplayString
_AdGenVlanName_Object=MibTableColumn
adGenVlanName=_AdGenVlanName_Object((1,3,6,1,4,1,664,5,70,39,2,1,2),_AdGenVlanName_Type())
adGenVlanName.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenVlanName.setStatus(_A)
_AdGenVlanDisplayText_Type=DisplayString
_AdGenVlanDisplayText_Object=MibTableColumn
adGenVlanDisplayText=_AdGenVlanDisplayText_Object((1,3,6,1,4,1,664,5,70,39,2,1,3),_AdGenVlanDisplayText_Type())
adGenVlanDisplayText.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenVlanDisplayText.setStatus(_A)
mibBuilder.exportSymbols(_F,**{'adGenVlanSlotTable':adGenVlanSlotTable,'adGenVlanSlotEntry':adGenVlanSlotEntry,'adGenVlanCount':adGenVlanCount,'adGenVlanInterfaceList':adGenVlanInterfaceList,'adGenVlanDisplayTable':adGenVlanDisplayTable,'adGenVlanDisplayEntry':adGenVlanDisplayEntry,_G:adGenVlanSTag,'adGenVlanName':adGenVlanName,'adGenVlanDisplayText':adGenVlanDisplayText,'adGenVlanModuleIdentity':adGenVlanModuleIdentity})