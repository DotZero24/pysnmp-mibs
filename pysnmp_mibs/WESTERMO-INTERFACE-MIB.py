_J='wmoInterfaceGroup'
_I='ifRefifType'
_H='ifRefifDescr'
_G='ifRefifName'
_F='ifRefifIndex'
_E='ifRefIndex'
_D='DisplayString'
_C='read-only'
_B='WESTERMO-INTERFACE-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
IANAifType,=mibBuilder.importSymbols('IANAifType-MIB','IANAifType')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_D,'PhysAddress','TextualConvention')
common,=mibBuilder.importSymbols('WESTERMO-OID-MIB','common')
wmoInterface=ModuleIdentity((1,3,6,1,4,1,16177,2,4))
if mibBuilder.loadTexts:wmoInterface.setRevisions(('2019-08-30 00:00',))
class IfaceRefIndex(TextualConvention,Integer32):status=_A;displayHint='d';subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1000))
_WmoInterfaceObjects_ObjectIdentity=ObjectIdentity
wmoInterfaceObjects=_WmoInterfaceObjects_ObjectIdentity((1,3,6,1,4,1,16177,2,4,1))
_IfRefTable_Object=MibTable
ifRefTable=_IfRefTable_Object((1,3,6,1,4,1,16177,2,4,1,1))
if mibBuilder.loadTexts:ifRefTable.setStatus(_A)
_IfRefEntry_Object=MibTableRow
ifRefEntry=_IfRefEntry_Object((1,3,6,1,4,1,16177,2,4,1,1,1))
ifRefEntry.setIndexNames((0,_B,_E))
if mibBuilder.loadTexts:ifRefEntry.setStatus(_A)
_IfRefIndex_Type=IfaceRefIndex
_IfRefIndex_Object=MibTableColumn
ifRefIndex=_IfRefIndex_Object((1,3,6,1,4,1,16177,2,4,1,1,1,1),_IfRefIndex_Type())
ifRefIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:ifRefIndex.setStatus(_A)
_IfRefifIndex_Type=InterfaceIndex
_IfRefifIndex_Object=MibTableColumn
ifRefifIndex=_IfRefifIndex_Object((1,3,6,1,4,1,16177,2,4,1,1,1,2),_IfRefifIndex_Type())
ifRefifIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:ifRefifIndex.setStatus(_A)
class _IfRefifName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_IfRefifName_Type.__name__=_D
_IfRefifName_Object=MibTableColumn
ifRefifName=_IfRefifName_Object((1,3,6,1,4,1,16177,2,4,1,1,1,3),_IfRefifName_Type())
ifRefifName.setMaxAccess(_C)
if mibBuilder.loadTexts:ifRefifName.setStatus(_A)
class _IfRefifDescr_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_IfRefifDescr_Type.__name__=_D
_IfRefifDescr_Object=MibTableColumn
ifRefifDescr=_IfRefifDescr_Object((1,3,6,1,4,1,16177,2,4,1,1,1,4),_IfRefifDescr_Type())
ifRefifDescr.setMaxAccess(_C)
if mibBuilder.loadTexts:ifRefifDescr.setStatus(_A)
_IfRefifType_Type=IANAifType
_IfRefifType_Object=MibTableColumn
ifRefifType=_IfRefifType_Object((1,3,6,1,4,1,16177,2,4,1,1,1,5),_IfRefifType_Type())
ifRefifType.setMaxAccess(_C)
if mibBuilder.loadTexts:ifRefifType.setStatus(_A)
_WmoInterfaceConformance_ObjectIdentity=ObjectIdentity
wmoInterfaceConformance=_WmoInterfaceConformance_ObjectIdentity((1,3,6,1,4,1,16177,2,4,2))
_WmoInterfaceGroups_ObjectIdentity=ObjectIdentity
wmoInterfaceGroups=_WmoInterfaceGroups_ObjectIdentity((1,3,6,1,4,1,16177,2,4,2,1))
_WmoInterfaceCompliances_ObjectIdentity=ObjectIdentity
wmoInterfaceCompliances=_WmoInterfaceCompliances_ObjectIdentity((1,3,6,1,4,1,16177,2,4,2,2))
wmoInterfaceGroup=ObjectGroup((1,3,6,1,4,1,16177,2,4,2,1,1))
wmoInterfaceGroup.setObjects(*((_B,_F),(_B,_G),(_B,_H),(_B,_I)))
if mibBuilder.loadTexts:wmoInterfaceGroup.setStatus(_A)
wmoInterfaceCompliance=ModuleCompliance((1,3,6,1,4,1,16177,2,4,2,2,1))
wmoInterfaceCompliance.setObjects((_B,_J))
if mibBuilder.loadTexts:wmoInterfaceCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'IfaceRefIndex':IfaceRefIndex,'wmoInterface':wmoInterface,'wmoInterfaceObjects':wmoInterfaceObjects,'ifRefTable':ifRefTable,'ifRefEntry':ifRefEntry,_E:ifRefIndex,_F:ifRefifIndex,_G:ifRefifName,_H:ifRefifDescr,_I:ifRefifType,'wmoInterfaceConformance':wmoInterfaceConformance,'wmoInterfaceGroups':wmoInterfaceGroups,_J:wmoInterfaceGroup,'wmoInterfaceCompliances':wmoInterfaceCompliances,'wmoInterfaceCompliance':wmoInterfaceCompliance})