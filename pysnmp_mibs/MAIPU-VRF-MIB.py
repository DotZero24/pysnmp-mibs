_I='mVrfConfiguration2RouteDistinguisher'
_H='mVrfConfiguration2Type'
_G='mVrfConfiguration2Name'
_F='not-accessible'
_E='Integer32'
_D='read-create'
_C='MAIPU-VRF-MIB'
_B='DisplayString'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
mpMgmt,=mibBuilder.importSymbols('MAIPU-SMI','mpMgmt')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_B,'PhysAddress','RowStatus','TextualConvention','TruthValue')
mVrfMib=ModuleIdentity((1,3,6,1,4,1,5651,3,89))
if mibBuilder.loadTexts:mVrfMib.setRevisions(('1904-05-27 10:03',))
_MVrfMibObjects_ObjectIdentity=ObjectIdentity
mVrfMibObjects=_MVrfMibObjects_ObjectIdentity((1,3,6,1,4,1,5651,3,89,1))
_MVrfGlobal_ObjectIdentity=ObjectIdentity
mVrfGlobal=_MVrfGlobal_ObjectIdentity((1,3,6,1,4,1,5651,3,89,1,1))
_MVrfConfiguration1_ObjectIdentity=ObjectIdentity
mVrfConfiguration1=_MVrfConfiguration1_ObjectIdentity((1,3,6,1,4,1,5651,3,89,1,2))
_MVrfConfiguration1Table_Object=MibTable
mVrfConfiguration1Table=_MVrfConfiguration1Table_Object((1,3,6,1,4,1,5651,3,89,1,2,1))
if mibBuilder.loadTexts:mVrfConfiguration1Table.setStatus(_A)
_MVrfConfiguration1Entry_Object=MibTableRow
mVrfConfiguration1Entry=_MVrfConfiguration1Entry_Object((1,3,6,1,4,1,5651,3,89,1,2,1,1))
mVrfConfiguration1Entry.setIndexNames((0,_C,'mVrfConfiguration1NameIndex'))
if mibBuilder.loadTexts:mVrfConfiguration1Entry.setStatus(_A)
class _MVrfConfiguration1Name_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_MVrfConfiguration1Name_Type.__name__=_B
_MVrfConfiguration1Name_Object=MibTableColumn
mVrfConfiguration1Name=_MVrfConfiguration1Name_Object((1,3,6,1,4,1,5651,3,89,1,2,1,1,1),_MVrfConfiguration1Name_Type())
mVrfConfiguration1Name.setMaxAccess(_F)
if mibBuilder.loadTexts:mVrfConfiguration1Name.setStatus(_A)
class _MVrfConfiguration1RouteDistinguisher_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,27))
_MVrfConfiguration1RouteDistinguisher_Type.__name__=_B
_MVrfConfiguration1RouteDistinguisher_Object=MibTableColumn
mVrfConfiguration1RouteDistinguisher=_MVrfConfiguration1RouteDistinguisher_Object((1,3,6,1,4,1,5651,3,89,1,2,1,1,2),_MVrfConfiguration1RouteDistinguisher_Type())
mVrfConfiguration1RouteDistinguisher.setMaxAccess(_D)
if mibBuilder.loadTexts:mVrfConfiguration1RouteDistinguisher.setStatus(_A)
class _MVrfConfiguration1Description_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,50))
_MVrfConfiguration1Description_Type.__name__=_B
_MVrfConfiguration1Description_Object=MibTableColumn
mVrfConfiguration1Description=_MVrfConfiguration1Description_Object((1,3,6,1,4,1,5651,3,89,1,2,1,1,3),_MVrfConfiguration1Description_Type())
mVrfConfiguration1Description.setMaxAccess(_D)
if mibBuilder.loadTexts:mVrfConfiguration1Description.setStatus(_A)
class _MVrfConfiguration2Type_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('import',1),('export',2),('both',3)))
_MVrfConfiguration2Type_Type.__name__=_E
_MVrfConfiguration2Type_Object=MibTableColumn
mVrfConfiguration2Type=_MVrfConfiguration2Type_Object((1,3,6,1,4,1,5651,3,89,1,2,1,1,3),_MVrfConfiguration2Type_Type())
mVrfConfiguration2Type.setMaxAccess(_D)
if mibBuilder.loadTexts:mVrfConfiguration2Type.setStatus(_A)
_MVrfConfiguration2_ObjectIdentity=ObjectIdentity
mVrfConfiguration2=_MVrfConfiguration2_ObjectIdentity((1,3,6,1,4,1,5651,3,89,1,3))
_MVrfConfiguration2Table_Object=MibTable
mVrfConfiguration2Table=_MVrfConfiguration2Table_Object((1,3,6,1,4,1,5651,3,89,1,3,1))
if mibBuilder.loadTexts:mVrfConfiguration2Table.setStatus(_A)
_MVrfConfiguration2Entry_Object=MibTableRow
mVrfConfiguration2Entry=_MVrfConfiguration2Entry_Object((1,3,6,1,4,1,5651,3,89,1,3,1,1))
mVrfConfiguration2Entry.setIndexNames((0,_C,_G),(0,_C,_H),(0,_C,_I))
if mibBuilder.loadTexts:mVrfConfiguration2Entry.setStatus(_A)
class _MVrfConfiguration2Name_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_MVrfConfiguration2Name_Type.__name__=_B
_MVrfConfiguration2Name_Object=MibTableColumn
mVrfConfiguration2Name=_MVrfConfiguration2Name_Object((1,3,6,1,4,1,5651,3,89,1,3,1,1,1),_MVrfConfiguration2Name_Type())
mVrfConfiguration2Name.setMaxAccess(_F)
if mibBuilder.loadTexts:mVrfConfiguration2Name.setStatus(_A)
class _MVrfConfiguration2RouteDistinguisher_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,27))
_MVrfConfiguration2RouteDistinguisher_Type.__name__=_B
_MVrfConfiguration2RouteDistinguisher_Object=MibTableColumn
mVrfConfiguration2RouteDistinguisher=_MVrfConfiguration2RouteDistinguisher_Object((1,3,6,1,4,1,5651,3,89,1,3,1,1,3),_MVrfConfiguration2RouteDistinguisher_Type())
mVrfConfiguration2RouteDistinguisher.setMaxAccess(_D)
if mibBuilder.loadTexts:mVrfConfiguration2RouteDistinguisher.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'mVrfMib':mVrfMib,'mVrfMibObjects':mVrfMibObjects,'mVrfGlobal':mVrfGlobal,'mVrfConfiguration1':mVrfConfiguration1,'mVrfConfiguration1Table':mVrfConfiguration1Table,'mVrfConfiguration1Entry':mVrfConfiguration1Entry,'mVrfConfiguration1Name':mVrfConfiguration1Name,'mVrfConfiguration1RouteDistinguisher':mVrfConfiguration1RouteDistinguisher,'mVrfConfiguration1Description':mVrfConfiguration1Description,_H:mVrfConfiguration2Type,'mVrfConfiguration2':mVrfConfiguration2,'mVrfConfiguration2Table':mVrfConfiguration2Table,'mVrfConfiguration2Entry':mVrfConfiguration2Entry,_G:mVrfConfiguration2Name,_I:mVrfConfiguration2RouteDistinguisher})