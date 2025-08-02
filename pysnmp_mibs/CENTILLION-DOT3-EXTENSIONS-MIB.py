_H='fullDuplex'
_G='halfDuplex'
_F='read-write'
_E='cnDot3ExtnIfIndex'
_D='CENTILLION-DOT3-EXTENSIONS-MIB'
_C='read-only'
_B='Integer32'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
extensions,=mibBuilder.importSymbols('CENTILLION-ROOT-MIB','extensions')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
_CnDot3Extensions_ObjectIdentity=ObjectIdentity
cnDot3Extensions=_CnDot3Extensions_ObjectIdentity((1,3,6,1,4,1,930,3,4))
_CnDot3ExtnTable_Object=MibTable
cnDot3ExtnTable=_CnDot3ExtnTable_Object((1,3,6,1,4,1,930,3,4,1))
if mibBuilder.loadTexts:cnDot3ExtnTable.setStatus(_A)
_CnDot3ExtnEntry_Object=MibTableRow
cnDot3ExtnEntry=_CnDot3ExtnEntry_Object((1,3,6,1,4,1,930,3,4,1,1))
cnDot3ExtnEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:cnDot3ExtnEntry.setStatus(_A)
_CnDot3ExtnIfIndex_Type=Integer32
_CnDot3ExtnIfIndex_Object=MibTableColumn
cnDot3ExtnIfIndex=_CnDot3ExtnIfIndex_Object((1,3,6,1,4,1,930,3,4,1,1,1),_CnDot3ExtnIfIndex_Type())
cnDot3ExtnIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:cnDot3ExtnIfIndex.setStatus(_A)
class _CnDot3ExtnIfAdminSpeed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('forced10',1),('forced100',2),('auto',3),('forced1000',4)))
_CnDot3ExtnIfAdminSpeed_Type.__name__=_B
_CnDot3ExtnIfAdminSpeed_Object=MibTableColumn
cnDot3ExtnIfAdminSpeed=_CnDot3ExtnIfAdminSpeed_Object((1,3,6,1,4,1,930,3,4,1,1,2),_CnDot3ExtnIfAdminSpeed_Type())
cnDot3ExtnIfAdminSpeed.setMaxAccess(_F)
if mibBuilder.loadTexts:cnDot3ExtnIfAdminSpeed.setStatus(_A)
_CnDot3ExtnIfOperSpeed_Type=Gauge32
_CnDot3ExtnIfOperSpeed_Object=MibTableColumn
cnDot3ExtnIfOperSpeed=_CnDot3ExtnIfOperSpeed_Object((1,3,6,1,4,1,930,3,4,1,1,3),_CnDot3ExtnIfOperSpeed_Type())
cnDot3ExtnIfOperSpeed.setMaxAccess(_C)
if mibBuilder.loadTexts:cnDot3ExtnIfOperSpeed.setStatus(_A)
class _CnDot3ExtnIfAdminConnectionType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_G,1),(_H,2),('auto',3)))
_CnDot3ExtnIfAdminConnectionType_Type.__name__=_B
_CnDot3ExtnIfAdminConnectionType_Object=MibTableColumn
cnDot3ExtnIfAdminConnectionType=_CnDot3ExtnIfAdminConnectionType_Object((1,3,6,1,4,1,930,3,4,1,1,4),_CnDot3ExtnIfAdminConnectionType_Type())
cnDot3ExtnIfAdminConnectionType.setMaxAccess(_F)
if mibBuilder.loadTexts:cnDot3ExtnIfAdminConnectionType.setStatus(_A)
class _CnDot3ExtnIfOperConnectionType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_CnDot3ExtnIfOperConnectionType_Type.__name__=_B
_CnDot3ExtnIfOperConnectionType_Object=MibTableColumn
cnDot3ExtnIfOperConnectionType=_CnDot3ExtnIfOperConnectionType_Object((1,3,6,1,4,1,930,3,4,1,1,5),_CnDot3ExtnIfOperConnectionType_Type())
cnDot3ExtnIfOperConnectionType.setMaxAccess(_C)
if mibBuilder.loadTexts:cnDot3ExtnIfOperConnectionType.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'cnDot3Extensions':cnDot3Extensions,'cnDot3ExtnTable':cnDot3ExtnTable,'cnDot3ExtnEntry':cnDot3ExtnEntry,_E:cnDot3ExtnIfIndex,'cnDot3ExtnIfAdminSpeed':cnDot3ExtnIfAdminSpeed,'cnDot3ExtnIfOperSpeed':cnDot3ExtnIfOperSpeed,'cnDot3ExtnIfAdminConnectionType':cnDot3ExtnIfAdminConnectionType,'cnDot3ExtnIfOperConnectionType':cnDot3ExtnIfOperConnectionType})