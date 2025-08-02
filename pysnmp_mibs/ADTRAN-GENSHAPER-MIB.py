_K='adGenShaperProvName'
_J='ADTRAN-GENSHAPER-MIB'
_I='DisplayString'
_H='ifIndex'
_G='IF-MIB'
_F='Integer32'
_E='adGenSlotInfoIndex'
_D='ADTRAN-GENSLOT-MIB'
_C='read-only'
_B='read-create'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
adGenSlotInfoIndex,=mibBuilder.importSymbols(_D,_E)
adGenShaper,adGenShaperID=mibBuilder.importSymbols('ADTRAN-SHARED-CND-SYSTEM-MIB','adGenShaper','adGenShaperID')
InterfaceIndex,InterfaceIndexOrZero,ifIndex=mibBuilder.importSymbols(_G,'InterfaceIndex','InterfaceIndexOrZero',_H)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_I,'PhysAddress','RowStatus','TextualConvention')
adGenShaperMIB=ModuleIdentity((1,3,6,1,4,1,664,6,10000,70,19,1))
if mibBuilder.loadTexts:adGenShaperMIB.setRevisions(('2009-09-03 00:00',))
_AdGenShaperProvisioning_ObjectIdentity=ObjectIdentity
adGenShaperProvisioning=_AdGenShaperProvisioning_ObjectIdentity((1,3,6,1,4,1,664,5,70,19,1))
_AdGenShaperProvTable_Object=MibTable
adGenShaperProvTable=_AdGenShaperProvTable_Object((1,3,6,1,4,1,664,5,70,19,1,1))
if mibBuilder.loadTexts:adGenShaperProvTable.setStatus(_A)
_AdGenShaperProvEntry_Object=MibTableRow
adGenShaperProvEntry=_AdGenShaperProvEntry_Object((1,3,6,1,4,1,664,5,70,19,1,1,1))
adGenShaperProvEntry.setIndexNames((0,_D,_E),(1,_J,_K))
if mibBuilder.loadTexts:adGenShaperProvEntry.setStatus(_A)
class _AdGenShaperProvName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,50))
_AdGenShaperProvName_Type.__name__=_I
_AdGenShaperProvName_Object=MibTableColumn
adGenShaperProvName=_AdGenShaperProvName_Object((1,3,6,1,4,1,664,5,70,19,1,1,1,1),_AdGenShaperProvName_Type())
adGenShaperProvName.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:adGenShaperProvName.setStatus(_A)
_AdGenShaperProvRowStatus_Type=RowStatus
_AdGenShaperProvRowStatus_Object=MibTableColumn
adGenShaperProvRowStatus=_AdGenShaperProvRowStatus_Object((1,3,6,1,4,1,664,5,70,19,1,1,1,2),_AdGenShaperProvRowStatus_Type())
adGenShaperProvRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenShaperProvRowStatus.setStatus(_A)
class _AdGenShaperProvOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('up',1),('down',2)))
_AdGenShaperProvOperStatus_Type.__name__=_F
_AdGenShaperProvOperStatus_Object=MibTableColumn
adGenShaperProvOperStatus=_AdGenShaperProvOperStatus_Object((1,3,6,1,4,1,664,5,70,19,1,1,1,3),_AdGenShaperProvOperStatus_Type())
adGenShaperProvOperStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenShaperProvOperStatus.setStatus(_A)
_AdGenShaperProvOperStatusDetail_Type=DisplayString
_AdGenShaperProvOperStatusDetail_Object=MibTableColumn
adGenShaperProvOperStatusDetail=_AdGenShaperProvOperStatusDetail_Object((1,3,6,1,4,1,664,5,70,19,1,1,1,4),_AdGenShaperProvOperStatusDetail_Type())
adGenShaperProvOperStatusDetail.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenShaperProvOperStatusDetail.setStatus(_A)
_AdGenShaperProvLastProvError_Type=DisplayString
_AdGenShaperProvLastProvError_Object=MibTableColumn
adGenShaperProvLastProvError=_AdGenShaperProvLastProvError_Object((1,3,6,1,4,1,664,5,70,19,1,1,1,5),_AdGenShaperProvLastProvError_Type())
adGenShaperProvLastProvError.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenShaperProvLastProvError.setStatus(_A)
class _AdGenShaperProvApplication_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('unspecified',1),('perInterface',2)))
_AdGenShaperProvApplication_Type.__name__=_F
_AdGenShaperProvApplication_Object=MibTableColumn
adGenShaperProvApplication=_AdGenShaperProvApplication_Object((1,3,6,1,4,1,664,5,70,19,1,1,1,6),_AdGenShaperProvApplication_Type())
adGenShaperProvApplication.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenShaperProvApplication.setStatus(_A)
_AdGenShaperProvRate_Type=Unsigned32
_AdGenShaperProvRate_Object=MibTableColumn
adGenShaperProvRate=_AdGenShaperProvRate_Object((1,3,6,1,4,1,664,5,70,19,1,1,1,7),_AdGenShaperProvRate_Type())
adGenShaperProvRate.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenShaperProvRate.setStatus(_A)
_AdGenShaperProvInterface_Type=InterfaceIndexOrZero
_AdGenShaperProvInterface_Object=MibTableColumn
adGenShaperProvInterface=_AdGenShaperProvInterface_Object((1,3,6,1,4,1,664,5,70,19,1,1,1,8),_AdGenShaperProvInterface_Type())
adGenShaperProvInterface.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenShaperProvInterface.setStatus(_A)
_AdGenShaperBurstSize_Type=Unsigned32
_AdGenShaperBurstSize_Object=MibTableColumn
adGenShaperBurstSize=_AdGenShaperBurstSize_Object((1,3,6,1,4,1,664,5,70,19,1,1,1,9),_AdGenShaperBurstSize_Type())
adGenShaperBurstSize.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenShaperBurstSize.setStatus(_A)
_AdGenShaperSlotTable_Object=MibTable
adGenShaperSlotTable=_AdGenShaperSlotTable_Object((1,3,6,1,4,1,664,5,70,19,1,2))
if mibBuilder.loadTexts:adGenShaperSlotTable.setStatus(_A)
_AdGenShaperSlotEntry_Object=MibTableRow
adGenShaperSlotEntry=_AdGenShaperSlotEntry_Object((1,3,6,1,4,1,664,5,70,19,1,2,1))
adGenShaperSlotEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:adGenShaperSlotEntry.setStatus(_A)
_AdGenShaperSlotLastCreateError_Type=DisplayString
_AdGenShaperSlotLastCreateError_Object=MibTableColumn
adGenShaperSlotLastCreateError=_AdGenShaperSlotLastCreateError_Object((1,3,6,1,4,1,664,5,70,19,1,2,1,1),_AdGenShaperSlotLastCreateError_Type())
adGenShaperSlotLastCreateError.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenShaperSlotLastCreateError.setStatus(_A)
_AdGenShaperLookupPerInterfaceTable_Object=MibTable
adGenShaperLookupPerInterfaceTable=_AdGenShaperLookupPerInterfaceTable_Object((1,3,6,1,4,1,664,5,70,19,1,3))
if mibBuilder.loadTexts:adGenShaperLookupPerInterfaceTable.setStatus(_A)
_AdGenShaperLookupPerInterfaceEntry_Object=MibTableRow
adGenShaperLookupPerInterfaceEntry=_AdGenShaperLookupPerInterfaceEntry_Object((1,3,6,1,4,1,664,5,70,19,1,3,1))
adGenShaperLookupPerInterfaceEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:adGenShaperLookupPerInterfaceEntry.setStatus(_A)
_AdGenShaperLookupPerInterface_Type=DisplayString
_AdGenShaperLookupPerInterface_Object=MibTableColumn
adGenShaperLookupPerInterface=_AdGenShaperLookupPerInterface_Object((1,3,6,1,4,1,664,5,70,19,1,3,1,1),_AdGenShaperLookupPerInterface_Type())
adGenShaperLookupPerInterface.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenShaperLookupPerInterface.setStatus(_A)
mibBuilder.exportSymbols(_J,**{'adGenShaperProvisioning':adGenShaperProvisioning,'adGenShaperProvTable':adGenShaperProvTable,'adGenShaperProvEntry':adGenShaperProvEntry,_K:adGenShaperProvName,'adGenShaperProvRowStatus':adGenShaperProvRowStatus,'adGenShaperProvOperStatus':adGenShaperProvOperStatus,'adGenShaperProvOperStatusDetail':adGenShaperProvOperStatusDetail,'adGenShaperProvLastProvError':adGenShaperProvLastProvError,'adGenShaperProvApplication':adGenShaperProvApplication,'adGenShaperProvRate':adGenShaperProvRate,'adGenShaperProvInterface':adGenShaperProvInterface,'adGenShaperBurstSize':adGenShaperBurstSize,'adGenShaperSlotTable':adGenShaperSlotTable,'adGenShaperSlotEntry':adGenShaperSlotEntry,'adGenShaperSlotLastCreateError':adGenShaperSlotLastCreateError,'adGenShaperLookupPerInterfaceTable':adGenShaperLookupPerInterfaceTable,'adGenShaperLookupPerInterfaceEntry':adGenShaperLookupPerInterfaceEntry,'adGenShaperLookupPerInterface':adGenShaperLookupPerInterface,'adGenShaperMIB':adGenShaperMIB})