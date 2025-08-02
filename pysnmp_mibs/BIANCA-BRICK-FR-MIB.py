_E='frMprIfIndex'
_D='BIANCA-BRICK-FR-MIB'
_C='read-write'
_B='Integer32'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
_Bintec_ObjectIdentity=ObjectIdentity
bintec=_Bintec_ObjectIdentity((1,3,6,1,4,1,272))
_Bibo_ObjectIdentity=ObjectIdentity
bibo=_Bibo_ObjectIdentity((1,3,6,1,4,1,272,4))
_Fr_ObjectIdentity=ObjectIdentity
fr=_Fr_ObjectIdentity((1,3,6,1,4,1,272,4,13))
_FrMprTable_Object=MibTable
frMprTable=_FrMprTable_Object((1,3,6,1,4,1,272,4,13,1))
if mibBuilder.loadTexts:frMprTable.setStatus(_A)
_FrMprEntry_Object=MibTableRow
frMprEntry=_FrMprEntry_Object((1,3,6,1,4,1,272,4,13,1,1))
frMprEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:frMprEntry.setStatus(_A)
class _FrMprIfIndex_Type(Integer32):defaultValue=0
_FrMprIfIndex_Type.__name__=_B
_FrMprIfIndex_Object=MibTableColumn
frMprIfIndex=_FrMprIfIndex_Object((1,3,6,1,4,1,272,4,13,1,1,1),_FrMprIfIndex_Type())
frMprIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:frMprIfIndex.setStatus(_A)
class _FrMprMtu_Type(Integer32):defaultValue=1500;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(576,8180))
_FrMprMtu_Type.__name__=_B
_FrMprMtu_Object=MibTableColumn
frMprMtu=_FrMprMtu_Object((1,3,6,1,4,1,272,4,13,1,1,2),_FrMprMtu_Type())
frMprMtu.setMaxAccess(_C)
if mibBuilder.loadTexts:frMprMtu.setStatus(_A)
class _FrMprEncapsulation_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,7)));namedValues=NamedValues(*(('mpr',1),('delete',7)))
_FrMprEncapsulation_Type.__name__=_B
_FrMprEncapsulation_Object=MibTableColumn
frMprEncapsulation=_FrMprEncapsulation_Object((1,3,6,1,4,1,272,4,13,1,1,3),_FrMprEncapsulation_Type())
frMprEncapsulation.setMaxAccess(_C)
if mibBuilder.loadTexts:frMprEncapsulation.setStatus(_A)
class _FrMprIfcType_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('multipoint',1),('point-to-point',2)))
_FrMprIfcType_Type.__name__=_B
_FrMprIfcType_Object=MibTableColumn
frMprIfcType=_FrMprIfcType_Object((1,3,6,1,4,1,272,4,13,1,1,4),_FrMprIfcType_Type())
frMprIfcType.setMaxAccess(_C)
if mibBuilder.loadTexts:frMprIfcType.setStatus(_A)
class _FrMprInverseArp_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),('disabled',2)))
_FrMprInverseArp_Type.__name__=_B
_FrMprInverseArp_Object=MibTableColumn
frMprInverseArp=_FrMprInverseArp_Object((1,3,6,1,4,1,272,4,13,1,1,5),_FrMprInverseArp_Type())
frMprInverseArp.setMaxAccess(_C)
if mibBuilder.loadTexts:frMprInverseArp.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'bintec':bintec,'bibo':bibo,'fr':fr,'frMprTable':frMprTable,'frMprEntry':frMprEntry,_E:frMprIfIndex,'frMprMtu':frMprMtu,'frMprEncapsulation':frMprEncapsulation,'frMprIfcType':frMprIfcType,'frMprInverseArp':frMprInverseArp})