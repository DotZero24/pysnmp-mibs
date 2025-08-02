_G='nbsTrapIfIndex'
_F='not-accessible'
_E='nbsTrapListIndex'
_D='NBS-TRAPCONTROL-MIB'
_C='DisplayString'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
nbs,=mibBuilder.importSymbols('NBS-MIB','nbs')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_C,'PhysAddress','TextualConvention')
nbsTrapControlMib=ModuleIdentity((1,3,6,1,4,1,629,209))
_NbsTrapListGrp_ObjectIdentity=ObjectIdentity
nbsTrapListGrp=_NbsTrapListGrp_ObjectIdentity((1,3,6,1,4,1,629,209,1))
if mibBuilder.loadTexts:nbsTrapListGrp.setStatus(_A)
_NbsTrapListTableSize_Type=Unsigned32
_NbsTrapListTableSize_Object=MibScalar
nbsTrapListTableSize=_NbsTrapListTableSize_Object((1,3,6,1,4,1,629,209,1,1),_NbsTrapListTableSize_Type())
nbsTrapListTableSize.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsTrapListTableSize.setStatus(_A)
_NbsTrapListTable_Object=MibTable
nbsTrapListTable=_NbsTrapListTable_Object((1,3,6,1,4,1,629,209,1,2))
if mibBuilder.loadTexts:nbsTrapListTable.setStatus(_A)
_NbsTrapListEntry_Object=MibTableRow
nbsTrapListEntry=_NbsTrapListEntry_Object((1,3,6,1,4,1,629,209,1,2,1))
nbsTrapListEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:nbsTrapListEntry.setStatus(_A)
_NbsTrapListIndex_Type=Unsigned32
_NbsTrapListIndex_Object=MibTableColumn
nbsTrapListIndex=_NbsTrapListIndex_Object((1,3,6,1,4,1,629,209,1,2,1,1),_NbsTrapListIndex_Type())
nbsTrapListIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:nbsTrapListIndex.setStatus(_A)
class _NbsTrapListTrapMib_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_NbsTrapListTrapMib_Type.__name__=_C
_NbsTrapListTrapMib_Object=MibTableColumn
nbsTrapListTrapMib=_NbsTrapListTrapMib_Object((1,3,6,1,4,1,629,209,1,2,1,2),_NbsTrapListTrapMib_Type())
nbsTrapListTrapMib.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsTrapListTrapMib.setStatus(_A)
class _NbsTrapListTrapName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,50))
_NbsTrapListTrapName_Type.__name__=_C
_NbsTrapListTrapName_Object=MibTableColumn
nbsTrapListTrapName=_NbsTrapListTrapName_Object((1,3,6,1,4,1,629,209,1,2,1,3),_NbsTrapListTrapName_Type())
nbsTrapListTrapName.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsTrapListTrapName.setStatus(_A)
class _NbsTrapListTrapDescription_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,100))
_NbsTrapListTrapDescription_Type.__name__=_C
_NbsTrapListTrapDescription_Object=MibTableColumn
nbsTrapListTrapDescription=_NbsTrapListTrapDescription_Object((1,3,6,1,4,1,629,209,1,2,1,4),_NbsTrapListTrapDescription_Type())
nbsTrapListTrapDescription.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsTrapListTrapDescription.setStatus(_A)
class _NbsTrapListTrapOID_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,100))
_NbsTrapListTrapOID_Type.__name__=_C
_NbsTrapListTrapOID_Object=MibTableColumn
nbsTrapListTrapOID=_NbsTrapListTrapOID_Object((1,3,6,1,4,1,629,209,1,2,1,5),_NbsTrapListTrapOID_Type())
nbsTrapListTrapOID.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsTrapListTrapOID.setStatus(_A)
_NbsTrapIfGrp_ObjectIdentity=ObjectIdentity
nbsTrapIfGrp=_NbsTrapIfGrp_ObjectIdentity((1,3,6,1,4,1,629,209,2))
if mibBuilder.loadTexts:nbsTrapIfGrp.setStatus(_A)
_NbsTrapIfTableSize_Type=Unsigned32
_NbsTrapIfTableSize_Object=MibScalar
nbsTrapIfTableSize=_NbsTrapIfTableSize_Object((1,3,6,1,4,1,629,209,2,1),_NbsTrapIfTableSize_Type())
nbsTrapIfTableSize.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsTrapIfTableSize.setStatus(_A)
_NbsTrapIfTable_Object=MibTable
nbsTrapIfTable=_NbsTrapIfTable_Object((1,3,6,1,4,1,629,209,2,2))
if mibBuilder.loadTexts:nbsTrapIfTable.setStatus(_A)
_NbsTrapIfEntry_Object=MibTableRow
nbsTrapIfEntry=_NbsTrapIfEntry_Object((1,3,6,1,4,1,629,209,2,2,1))
nbsTrapIfEntry.setIndexNames((0,_D,_G))
if mibBuilder.loadTexts:nbsTrapIfEntry.setStatus(_A)
_NbsTrapIfIndex_Type=InterfaceIndex
_NbsTrapIfIndex_Object=MibTableColumn
nbsTrapIfIndex=_NbsTrapIfIndex_Object((1,3,6,1,4,1,629,209,2,2,1,1),_NbsTrapIfIndex_Type())
nbsTrapIfIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:nbsTrapIfIndex.setStatus(_A)
_NbsTrapIfTrapsCaps_Type=OctetString
_NbsTrapIfTrapsCaps_Object=MibTableColumn
nbsTrapIfTrapsCaps=_NbsTrapIfTrapsCaps_Object((1,3,6,1,4,1,629,209,2,2,1,2),_NbsTrapIfTrapsCaps_Type())
nbsTrapIfTrapsCaps.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsTrapIfTrapsCaps.setStatus(_A)
_NbsTrapIfTrapsSelect_Type=OctetString
_NbsTrapIfTrapsSelect_Object=MibTableColumn
nbsTrapIfTrapsSelect=_NbsTrapIfTrapsSelect_Object((1,3,6,1,4,1,629,209,2,2,1,3),_NbsTrapIfTrapsSelect_Type())
nbsTrapIfTrapsSelect.setMaxAccess('read-write')
if mibBuilder.loadTexts:nbsTrapIfTrapsSelect.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'nbsTrapControlMib':nbsTrapControlMib,'nbsTrapListGrp':nbsTrapListGrp,'nbsTrapListTableSize':nbsTrapListTableSize,'nbsTrapListTable':nbsTrapListTable,'nbsTrapListEntry':nbsTrapListEntry,_E:nbsTrapListIndex,'nbsTrapListTrapMib':nbsTrapListTrapMib,'nbsTrapListTrapName':nbsTrapListTrapName,'nbsTrapListTrapDescription':nbsTrapListTrapDescription,'nbsTrapListTrapOID':nbsTrapListTrapOID,'nbsTrapIfGrp':nbsTrapIfGrp,'nbsTrapIfTableSize':nbsTrapIfTableSize,'nbsTrapIfTable':nbsTrapIfTable,'nbsTrapIfEntry':nbsTrapIfEntry,_G:nbsTrapIfIndex,'nbsTrapIfTrapsCaps':nbsTrapIfTrapsCaps,'nbsTrapIfTrapsSelect':nbsTrapIfTrapsSelect})